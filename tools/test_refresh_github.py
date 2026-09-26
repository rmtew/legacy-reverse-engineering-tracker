import unittest
import json
import tempfile
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import patch

import refresh_github
import collect_activity


class HistoricalLatestCommitTest(unittest.TestCase):
    def test_resolves_old_branch_and_path_commits_without_activity_events(self):
        root = {"id": "root", "github": {"tracking_branch": "master"}}
        shared = {"id": "shared", "github": {"tracking_branch": "master"}}
        subproject = {"id": "sub", "github_path": "games/sub", "github": {"tracking_branch": "master"}}
        repos = {"a/b": [root, shared, subproject]}
        state = {"repositories": {"a/b": {"last_seen_pushed_at": "2026-03-01T00:00:00Z"}}}
        paths = []

        def request(path, **kwargs):
            paths.append(path)
            older = "path=games%2Fsub" in path
            sha = "path-sha" if older else "root-sha"
            return ([{"sha": sha, "html_url": "https://github.com/a/b/commit/" + sha,
                      "commit": {"committer": {"date": "2021-07-10T08:44:15Z"},
                                 "message": "Historical change\nmore detail"}}], {}, 200)

        with patch.object(refresh_github, "TODAY", date(2026, 9, 26)):
            checked, found, unavailable = refresh_github.fill_missing_latest_commits(repos, state, request)
        self.assertEqual((checked, found, unavailable), (2, 3, 0))
        self.assertTrue(all("per_page=1" in path and "sha=master" in path for path in paths))
        self.assertEqual(root["github"]["latest_commit"]["date"], "2021-07-10")
        self.assertEqual(shared["github"]["latest_commit"]["sha"], "root-sha")
        self.assertEqual(subproject["github"]["latest_commit"]["sha"], "path-sha")
        self.assertEqual(subproject["last_activity"], "2021-07-10")
        self.assertEqual(root["github"]["activity_state"], "dormant")

    def test_empty_path_is_cached_without_claiming_a_commit(self):
        project = {"id": "p", "github_path": "missing", "github": {"tracking_branch": "main"}}
        state = {"repositories": {"a/b": {"last_seen_pushed_at": "2026-01-01T00:00:00Z"}}}
        calls = []

        def request(path, **kwargs):
            calls.append(path)
            return ([], {}, 200)

        with patch.object(refresh_github, "TODAY", date(2026, 9, 26)):
            self.assertEqual(refresh_github.fill_missing_latest_commits({"a/b": [project]}, state, request), (1, 0, 1))
            self.assertEqual(refresh_github.fill_missing_latest_commits({"a/b": [project]}, state, request), (0, 0, 0))
        self.assertEqual(len(calls), 1)
        self.assertEqual(project["github"]["latest_commit_lookup"], "unavailable")
        self.assertNotIn("last_activity", project)


class ProbeCadenceTest(unittest.TestCase):
    def test_probe_tiers_and_archived_override(self):
        with patch.object(refresh_github, "TODAY", date(2026, 9, 26)):
            self.assertEqual(refresh_github.probe_interval_minutes("2026-09-25"), 15)
            self.assertEqual(refresh_github.probe_interval_minutes("2026-09-11"), 60)
            self.assertEqual(refresh_github.probe_interval_minutes("2026-07-26"), 240)
            self.assertEqual(refresh_github.probe_interval_minutes("2025-01-01"), 720)
            self.assertEqual(refresh_github.probe_interval_minutes("2026-09-26", archived=True), 720)

    def test_migration_stagger_never_exceeds_probe_interval(self):
        last = datetime(2026, 9, 26, 0, 0, tzinfo=timezone.utc)
        rs = {"last_probe_at": "2026-09-26T00:00:00Z"}
        for minutes in (15, 60, 240, 720):
            with patch.object(refresh_github, "RUN_AT", last + timedelta(minutes=minutes)):
                self.assertTrue(refresh_github.probe_due("owner/repo", rs, minutes))
            with patch.object(refresh_github, "RUN_AT", last):
                self.assertFalse(refresh_github.probe_due("owner/repo", rs, minutes))
        rs["next_probe_due_at"] = "2026-09-26T01:00:00Z"
        with patch.object(refresh_github, "RUN_AT", last + timedelta(minutes=59)):
            self.assertFalse(refresh_github.probe_due("owner/repo", rs, 60))
        with patch.object(refresh_github, "RUN_AT", last + timedelta(minutes=60)):
            self.assertTrue(refresh_github.probe_due("owner/repo", rs, 60))

    def test_new_project_bypasses_quiet_repo_probe_deadline(self):
        with tempfile.TemporaryDirectory() as directory:
            projects = Path(directory) / "projects.json"
            state_path = Path(directory) / "state.json"
            projects.write_text(json.dumps([{
                "id": "new", "repo": "https://github.com/owner/repo",
                "github_path": "game", "last_activity": "2022-01-01",
                "github": {"latest_commit": {"sha": "abc"}, "languages": ["C"]},
            }]))
            state_path.write_text(json.dumps({"repositories": {"owner/repo": {
                "project_ids": ["old"], "next_probe_due_at": "2026-09-27T00:00:00Z",
                "last_seen_pushed_at": "2026-09-01T00:00:00Z",
                "last_deep_scan": "2026-09-25T00:00:00Z",
            }}}))
            info = {"pushed_at": "2026-09-01T00:00:00Z", "default_branch": "main"}
            with patch.multiple(refresh_github, PROJECTS=projects, STATE=state_path,
                                RUN_AT=datetime(2026, 9, 26, 4, 0, tzinfo=timezone.utc),
                                TODAY=date(2026, 9, 26)), \
                    patch.object(refresh_github, "get_json", return_value=(info, {}, 200)) as request:
                refresh_github.main()
            result = json.loads(state_path.read_text())["repositories"]["owner/repo"]
            self.assertTrue(result["scan_requested"])
            self.assertEqual(result["scan_reason"], "new-project")
            self.assertEqual(result["probe_interval_minutes"], 720)
            self.assertEqual(request.call_count, 1)

    def test_unchanged_repo_can_refresh_release_without_repeating_empty_languages(self):
        with tempfile.TemporaryDirectory() as directory:
            projects = Path(directory) / "projects.json"
            state_path = Path(directory) / "state.json"
            projects.write_text(json.dumps([{
                "id": "known", "repo": "https://github.com/owner/repo",
                "last_activity": "2026-09-25",
                "github": {"latest_commit": {"sha": "abc"}, "languages": []},
            }]))
            state_path.write_text(json.dumps({"repositories": {"owner/repo": {
                "project_ids": ["known"], "next_probe_due_at": "2026-09-26T03:00:00Z",
                "last_seen_pushed_at": "2026-09-01T00:00:00Z",
                "empty_languages_checked_at": "2026-09-25",
                "last_release_check_at": "2026-09-25T20:00:00Z",
                "last_deep_scan": "2026-09-26T00:00:00Z",
            }}}))
            info = {"pushed_at": "2026-09-01T00:00:00Z", "default_branch": "main"}
            release = {"tag_name": "v2", "name": "Version 2",
                       "published_at": "2026-09-26T02:00:00Z", "html_url": "https://github.com/owner/repo/releases/tag/v2"}
            def request(path, **kwargs):
                return (release if path.endswith("/releases/latest") else info, {}, 200)
            with patch.multiple(refresh_github, PROJECTS=projects, STATE=state_path,
                                RUN_AT=datetime(2026, 9, 26, 4, 0, tzinfo=timezone.utc),
                                TODAY=date(2026, 9, 26)), \
                    patch.object(refresh_github, "get_json", side_effect=request) as mocked, \
                    patch.object(refresh_github, "enrich_changed_repo") as enrichment:
                refresh_github.main()
            enrichment.assert_not_called()
            self.assertEqual(mocked.call_count, 2)
            result = json.loads(projects.read_text())[0]
            self.assertEqual(result["github"]["latest_release"]["tag"], "v2")
            self.assertEqual(result["github"]["latest_release"]["published_at"], "2026-09-26")

    def test_new_project_scan_promotes_the_next_probe(self):
        state = {"repositories": {"owner/repo": {
            "probe_interval_minutes": 720,
            "next_probe_due_at": "2026-09-26T16:00:00Z",
        }}}
        projects = {"owner/repo": [{"id": "new", "last_activity": "2026-09-26", "github": {}}]}
        now = datetime(2026, 9, 26, 4, 0, tzinfo=timezone.utc)
        with patch.object(refresh_github, "TODAY", date(2026, 9, 26)):
            collect_activity.advance_probe_deadlines(projects, state, now)
        self.assertEqual(state["repositories"]["owner/repo"]["probe_interval_minutes"], 15)
        self.assertEqual(state["repositories"]["owner/repo"]["next_probe_due_at"], "2026-09-26T04:15:00Z")

    def test_idle_activity_run_preserves_existing_ai_evidence(self):
        with tempfile.TemporaryDirectory() as directory:
            projects = Path(directory) / "projects.json"
            activity = Path(directory) / "activity.json"
            state_path = Path(directory) / "state.json"
            evidence = "Claude co-author trailer observed in recent tracked commits: 9 in this scan (example abc)"
            projects.write_text(json.dumps([{
                "id": "known", "repo": "https://github.com/owner/repo",
                "title": "Known", "github": {"tracking_branch": "main"},
                "ai": {"usage": True, "tools": ["Claude"], "evidence": [evidence]},
            }]))
            activity.write_text(json.dumps({"generated_at": "2026-09-26T01:00:00Z", "events": [{
                "type": "commit", "project_id": "known", "repository": "owner/repo",
                "sha": "abc", "date": "2026-09-26T02:00:00Z", "branches": ["main"],
                "title": "Work", "message": "Work\nCo-authored-by: Claude <bot@example.com>",
            }]}))
            state_path.write_text(json.dumps({"repositories": {"owner/repo": {"scan_requested": False}}}))
            now = datetime(2026, 9, 26, 4, 0, tzinfo=timezone.utc)
            with patch.multiple(collect_activity, PROJECTS=projects, ACTIVITY=activity, STATE=state_path,
                                NOW=now, NOW_ISO="2026-09-26T04:00:00Z",
                                CUTOFF=now - timedelta(days=180)):
                collect_activity.main()
            self.assertEqual(json.loads(projects.read_text())[0]["ai"]["evidence"], [evidence])


if __name__ == "__main__":
    unittest.main()
