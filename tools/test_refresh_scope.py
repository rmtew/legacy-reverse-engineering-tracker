"""Publication scope contracts, with local fixtures and no GitHub requests."""
import copy
import io
import json
import os
import subprocess
import tempfile
import unittest
from contextlib import ExitStack
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import patch
from urllib.parse import parse_qs, urlparse

import collect_activity as collector
import refresh_github as refresh
import refresh_scope as scope

NOW = datetime(2026, 10, 1, 12, tzinfo=timezone.utc)
NOW_ISO = "2026-10-01T12:00:00Z"


def project(pid, repo="owner/repo", **extra):
    return {"id": pid, "title": pid.title(), "repo": "https://github.com/" + repo, **extra}


def commit(sha="abc", day="2026-08-01", message="Historical work"):
    return {"sha": sha, "html_url": "https://github.com/owner/repo/commit/" + sha,
            "commit": {"committer": {"date": day + "T00:00:00Z"}, "message": message}}


class CatalogueScopeTest(unittest.TestCase):
    def test_only_new_or_materially_changed_repositories_are_selected(self):
        before = [project("same"), project("edit", "a/b"), project("removed", "a/gone")]
        after = copy.deepcopy(before[:2]) + [project("new", "a/new")]
        after[0]["github"] = {"checked_at": "2026-10-01"}
        after[0]["last_activity"] = "2026-10-01"
        after[1]["title"] = "Renamed"
        delta = scope.catalogue_delta(before, after)
        self.assertEqual(delta["repositories"], ["a/b", "a/new"])
        self.assertEqual(delta["changed_project_ids"], ["edit", "new"])
        self.assertEqual(delta["reset_project_ids"], ["new"])
        self.assertEqual(delta["removed_project_ids"], ["removed"])

    def test_new_project_in_existing_repo_requires_backfill(self):
        first = project("old", github={"languages": ["C"]})
        second = project("new", github_path="game", github_branch="port")
        delta = scope.catalogue_delta([first], [first, second])
        self.assertEqual(delta["repositories"], ["owner/repo"])
        self.assertEqual(delta["reset_project_ids"], ["new"])

    def test_tracking_changes_reset_history_even_when_ids_are_unchanged(self):
        before = [project("p", github_path="old", github_branch="main")]
        for change in ({"github_path": "new"}, {"github_branch": "dev"}, {"repo": "https://github.com/new/repo"}):
            after = [{**before[0], **change}]
            self.assertEqual(scope.catalogue_delta(before, after)["reset_project_ids"], ["p"])

    def test_new_non_github_project_preserves_its_authored_activity_date(self):
        records = [{"id": "external", "title": "External", "repo": "https://example.org/project",
                    "last_activity": "2020-01-01"}]
        original = copy.deepcopy(records)
        delta = scope.catalogue_delta([], records)
        scope.prepare_publication({}, {"repositories": {}}, delta, records)
        self.assertEqual(records, original)
        self.assertEqual(delta["left_github_project_ids"], [])

    def test_move_away_from_github_removes_generated_metadata(self):
        before = [project("move", github={"repository": "owner/repo", "latest_commit": {"sha": "old"}},
                          last_activity="2026-09-01")]
        after = [{**before[0], "repo": "https://gitlab.com/owner/project"}]
        delta = scope.catalogue_delta(before, after)
        state = {"repositories": {"owner/repo": {"project_ids": ["move"]}}}
        scope.prepare_publication({}, state, delta, after)
        self.assertEqual(state["repositories"], {})
        self.assertNotIn("github", after[0])
        self.assertNotIn("last_activity", after[0])

    def test_deletions_update_membership_without_probing_survivors(self):
        before = [project("keep"), project("remove"), project("gone", "gone/repo")]
        after = before[:1]
        delta = scope.catalogue_delta(before, after)
        state = {"repositories": {"owner/repo": {"project_ids": ["keep", "remove"],
                   "last_deep_scan_project_ids": ["keep", "remove"], "scan_requested": True},
                   "gone/repo": {"last_error": "old"}}}
        scope.prepare_publication({"owner/repo": after}, state, delta)
        self.assertEqual(delta["repositories"], [])
        self.assertNotIn("gone/repo", state["repositories"])
        self.assertEqual(state["repositories"]["owner/repo"]["project_ids"], ["keep"])
        self.assertEqual(state["repositories"]["owner/repo"]["last_deep_scan_project_ids"], ["keep"])
        self.assertTrue(state["repositories"]["owner/repo"]["scan_requested"])

    def test_schedule_default_manual_and_push_modes(self):
        self.assertEqual(scope.select_base("schedule", {}), (None, None))
        self.assertEqual(scope.select_base("workflow_dispatch", {}), (None, None))
        self.assertEqual(scope.select_base("push", {"before": "b", "after": "a"}), ("b", "a"))
        self.assertEqual(scope.select_base("workflow_dispatch", {}, "b", "a"), ("b", "a"))
        with self.assertRaises(ValueError):
            scope.select_base("workflow_dispatch", {}, "b", "")
        with self.assertRaises(ValueError):
            scope.select_base("schedule", {}, "b", "a")

    def test_incomplete_manifest_fails_closed_and_adaptive_stays_broad(self):
        repos = {"a/b": [], "c/d": []}
        self.assertEqual(scope.select_repositories(repos, {"mode": "adaptive"}), repos)
        self.assertEqual(scope.select_repositories(repos, {"mode": "publication", "repositories": []}), {})
        with tempfile.TemporaryDirectory() as directory, patch.dict(os.environ, {"GITHUB_REFRESH_SCOPE_FILE": directory + "/missing"}):
            with self.assertRaises(FileNotFoundError):
                scope.load_scope()

    def test_pending_work_is_idempotent_and_blocks_deploy(self):
        p = project("p")
        delta = scope.catalogue_delta([], [p])
        state = {"repositories": {}}
        scope.prepare_publication({"owner/repo": [p]}, state, delta)
        rs = state["repositories"]["owner/repo"]
        rs["publication"]["metadata_complete"] = True
        p["github"] = {"latest_commit": {"sha": "abc"}}
        scope.prepare_publication({"owner/repo": [p]}, state, delta)
        self.assertTrue(rs["publication"]["metadata_complete"])
        self.assertIn("github", p)
        with self.assertRaises(SystemExit):
            scope.check_complete(delta, state)
        with self.assertRaises(SystemExit):
            scope.check_publishable(state, [p])
        rs["publication"]["history_complete"] = True
        scope.check_complete(delta, state)
        scope.check_publishable(state, [p])

    def test_pages_blocks_new_catalogue_before_pending_marker_exists(self):
        old = project("old")
        catalogue = {"projects": {"old": scope.material(old)}}
        state = {"repositories": {"owner/repo": {"last_deep_scan_project_ids": ["old"]}}}
        scope.check_publishable(state, [old], catalogue)
        variants = ([old, project("new")], [{**old, "github_path": "new-path"}],
                    [{**old, "github_branch": "port"}], [{**old, "title": "Renamed"}], [])
        for records in variants:
            with self.subTest(records=records), self.assertRaises(SystemExit):
                scope.check_publishable(state, records, catalogue)

    def test_adaptive_run_racing_publication_initializes_required_work(self):
        before = [project("old", "unrelated/repo")]
        after = before + [project("new")]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            projects, catalogue, manifest = (root / name for name in ("projects.json", "catalogue.json", "scope.json"))
            projects.write_text(json.dumps(after))
            catalogue.write_text(json.dumps({"projects": {p["id"]: scope.material(p) for p in before}}))
            with patch.multiple(scope, PROJECTS=projects, CATALOGUE=catalogue), patch.dict(os.environ, {
                    "GITHUB_EVENT_NAME": "schedule", "GITHUB_EVENT_PATH": "", "PUBLICATION_BASE": "",
                    "PUBLICATION_HEAD": "", "GITHUB_REFRESH_SCOPE_FILE": str(manifest)}), patch("sys.argv", ["refresh_scope.py"]):
                scope.main()
            selected = json.loads(manifest.read_text())
        self.assertEqual(selected["mode"], "adaptive")
        self.assertEqual(selected["publication"]["repositories"], ["owner/repo"])
        repos = {"unrelated/repo": before, "owner/repo": after[1:]}
        state = {"repositories": {}}
        scope.prepare_publication(repos, state, selected)
        self.assertTrue(scope.pending_publication(state["repositories"]["owner/repo"]))
        self.assertEqual(scope.select_repositories(repos, selected), repos)
        with self.assertRaises(SystemExit):
            scope.check_complete(selected, state)

    def test_removed_repository_pending_marker_does_not_block_pages(self):
        state = {"repositories": {"gone/repo": {"publication": {"metadata_complete": False}}}}
        scope.check_publishable(state, [], {"projects": {}})

    def test_advanced_main_rebuild_keeps_original_base_and_actual_pending_delta(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "data").mkdir()
            path = root / "data/projects.json"
            def git(*args):
                return subprocess.check_output(["git", *args], cwd=root, text=True, stderr=subprocess.DEVNULL).strip()
            git("init")
            git("config", "user.name", "Test")
            git("config", "user.email", "test@example.com")
            path.write_text(json.dumps([project("old")]))
            git("add", ".")
            git("commit", "-m", "base")
            base = git("rev-parse", "HEAD")
            path.write_text(json.dumps([project("old"), project("new", "new/repo")]))
            git("commit", "-am", "published")
            head = git("rev-parse", "HEAD")
            path.write_text(json.dumps([project("old"), project("new", "new/repo"), project("later", "later/repo")]))
            git("commit", "-am", "interleaved main update")
            # Include the actual result of merging pending entries after checkout.
            path.write_text(json.dumps(json.loads(path.read_text()) + [project("pending", "pending/repo")]))
            manifest = root / "scope.json"
            catalogue = root / "catalogue.json"
            catalogue.write_text(json.dumps({"projects": {"old": scope.material(project("old"))}}))
            with patch.multiple(scope, ROOT=root, PROJECTS=path, CATALOGUE=catalogue), patch.dict(os.environ, {
                    "GITHUB_EVENT_NAME": "workflow_dispatch", "PUBLICATION_BASE": base,
                    "PUBLICATION_HEAD": head, "GITHUB_EVENT_PATH": "", "GITHUB_REFRESH_SCOPE_FILE": str(manifest)}), \
                    patch("sys.argv", ["refresh_scope.py"]):
                scope.main()
            result = json.loads(manifest.read_text())
            self.assertEqual(result["base"], base)
            self.assertEqual(result["repositories"], ["later/repo", "new/repo", "pending/repo"])

    def test_later_code_only_push_and_dispatch_recover_unrecorded_publication(self):
        for event_name in ("push", "workflow_dispatch"):
            with self.subTest(event_name=event_name), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                (root / "data").mkdir()
                path = root / "data/projects.json"
                old, new = project("old", "old/repo"), project("new", "new/repo")
                def git(*args):
                    return subprocess.check_output(["git", *args], cwd=root, text=True, stderr=subprocess.DEVNULL).strip()
                git("init")
                git("config", "user.name", "Test")
                git("config", "user.email", "test@example.com")
                path.write_text(json.dumps([old]))
                git("add", ".")
                git("commit", "-m", "original catalogue")
                catalogue = root / "catalogue.json"
                catalogue.write_text(json.dumps({"projects": {"old": scope.material(old)}}))
                path.write_text(json.dumps([old, new]))
                git("add", "data/projects.json")
                git("commit", "-m", "A: publication whose refresh did not run")
                base = git("rev-parse", "HEAD")
                (root / "code.py").write_text("# B: unrelated code change\n")
                git("add", "code.py")
                git("commit", "-m", "B: code-only push")
                head = git("rev-parse", "HEAD")
                event = root / "event.json"
                event.write_text(json.dumps({"before": base, "after": head}))
                manifest = root / "scope.json"
                with patch.multiple(scope, ROOT=root, PROJECTS=path, CATALOGUE=catalogue), patch.dict(os.environ, {
                        "GITHUB_EVENT_NAME": event_name, "GITHUB_EVENT_PATH": str(event),
                        "PUBLICATION_BASE": base if event_name == "workflow_dispatch" else "",
                        "PUBLICATION_HEAD": head if event_name == "workflow_dispatch" else "",
                        "GITHUB_REFRESH_SCOPE_FILE": str(manifest)}), patch("sys.argv", ["refresh_scope.py"]):
                    scope.main()
                selected = json.loads(manifest.read_text())
                self.assertEqual(selected["repositories"], ["new/repo"])
                self.assertEqual(selected["reset_project_ids"], ["new"])
                state = {"repositories": {}}
                scope.prepare_publication({"old/repo": [old], "new/repo": [new]}, state, selected, [old, new])
                # Even after the ordinary recorder advances its snapshot, the
                # missed publication cannot deploy until both phases finish.
                recorded = {"projects": {p["id"]: scope.material(p) for p in (old, new)}}
                with self.assertRaises(SystemExit):
                    scope.check_publishable(state, [old, new], recorded)
                state["repositories"]["new/repo"]["publication"]["metadata_complete"] = True
                with self.assertRaises(SystemExit):
                    scope.check_publishable(state, [old, new], recorded)
                state["repositories"]["new/repo"]["publication"]["history_complete"] = True
                scope.check_publishable(state, [old, new], recorded)

    def test_delta_union_preserves_old_membership_moves_deletions_and_fingerprints(self):
        persisted = [project("move", "old/repo"), project("gone", "gone/repo"),
                     project("path", "path/repo", github_path="old"), project("left", "left/repo")]
        current = [project("move", "new/repo"), project("path", "path/repo", github_path="new"),
                   {**project("left"), "repo": "https://gitlab.com/left/repo"}, project("added", "added/repo")]
        # The triggering event remembers a different prior repository than the
        # persisted catalogue; both obsolete memberships must be cleaned up.
        event_before = [{**p, "repo": "https://github.com/intermediate/repo"} if p["id"] == "move" else p
                        for p in current]
        outstanding = scope.catalogue_delta(persisted, current)
        event = scope.catalogue_delta(event_before, current)
        merged = scope.union_catalogue_deltas(event, outstanding)
        self.assertEqual(merged["reset_project_ids"], ["added", "left", "move", "path"])
        self.assertEqual(merged["removed_project_ids"], ["gone"])
        self.assertEqual(merged["left_github_project_ids"], ["left"])
        self.assertTrue({"old/repo", "intermediate/repo", "gone/repo", "left/repo"} <= set(merged["membership_repositories"]))
        self.assertEqual(merged["fingerprints"], outstanding["fingerprints"])


class PublicationPipelineTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.projects = self.root / "projects.json"
        self.activity = self.root / "activity.json"
        self.state = self.root / "state.json"
        self.manifest = self.root / "scope.json"
        self.stack = ExitStack()
        self.addCleanup(self.stack.close)
        self.stack.enter_context(patch.dict(os.environ, {"GITHUB_REFRESH_SCOPE_FILE": str(self.manifest)}))
        self.stack.enter_context(patch.multiple(refresh, PROJECTS=self.projects, STATE=self.state,
            RUN_AT=NOW, TODAY=NOW.date(), FORCE_FULL_PROBE=False, RATE_LIMIT=None, RATE_REMAINING=None, RATE_RESET=None))
        self.stack.enter_context(patch.multiple(collector, PROJECTS=self.projects, ACTIVITY=self.activity, STATE=self.state,
            NOW=NOW, NOW_ISO=NOW_ISO, CUTOFF=NOW - timedelta(days=180)))

    def seed(self, before=None, after=None):
        old = project("old", "unrelated/repo", last_activity="2026-09-30",
                      github={"tracking_branch": "main", "latest_commit": {"sha": "old"}},
                      ai={"usage": True, "tools": ["Pi"], "evidence": ["keep"]})
        before = [old] if before is None else before
        after = [old, project("new")] if after is None else after
        self.projects.write_text(json.dumps(after))
        self.manifest.write_text(json.dumps(scope.catalogue_delta(before, after)))
        unrelated = {"project_ids": ["old"], "next_probe_due_at": "2020-01-01T00:00:00Z",
                     "scan_requested": True, "scan_reason": "changed", "branches": {"main": {"tip_sha": "old"}}}
        self.state.write_text(json.dumps({"repositories": {"unrelated/repo": unrelated}}))
        self.activity.write_text(json.dumps({"generated_at": "2026-10-01T11:00:00Z", "events": [
            {"type": "project_added", "project_id": "new", "date": "2026-10-01T10:00:00Z"},
            {"type": "commit", "project_id": "old", "repository": "unrelated/repo", "sha": "old",
             "date": "2026-09-01T00:00:00Z", "branches": ["main"], "title": "Keep unchanged"}]}))
        return old, unrelated

    def metadata(self, path, **kwargs):
        self.assertNotIn("unrelated/repo", path)
        if path.endswith("/languages"):
            return {"C": 20}, {}, 200
        if "/contents?" in path:
            return [], {}, 200
        if path.endswith("/releases/latest"):
            return {"tag_name": "v1", "published_at": "2026-07-01T00:00:00Z"}, {}, 200
        if "/commits?" in path:
            return [commit()], {}, 200
        return {"default_branch": "main", "pushed_at": "2026-08-01T00:00:00Z"}, {"ETag": "cached"}, 200

    def history(self, path, **kwargs):
        self.assertNotIn("unrelated/repo", path)
        if "/branches?" in path:
            return [{"name": "main", "commit": {"sha": "abc"}}]
        if "/commits?" in path:
            params = parse_qs(urlparse(path).query)
            self.assertEqual(params["since"], [(NOW - timedelta(days=180)).isoformat(timespec="seconds").replace("+00:00", "Z")])
            return [commit(message="Work\nCo-authored-by: Pi <pi@example.com>")]
        self.fail("Unexpected history request " + path)

    def test_publication_does_full_initial_context_and_preserves_unrelated_due_work(self):
        old, unrelated = self.seed()
        previous_event = json.loads(self.activity.read_text())["events"][1]
        with patch.object(refresh, "get_json", side_effect=self.metadata):
            refresh.main()
        with patch.object(collector, "api", side_effect=self.history):
            collector.main()
        state = json.loads(self.state.read_text())
        result = {p["id"]: p for p in json.loads(self.projects.read_text())}
        self.assertEqual(result["old"], old)
        self.assertEqual(state["repositories"]["unrelated/repo"], unrelated)
        new = result["new"]
        self.assertEqual(new["github"]["languages"], ["C"])
        self.assertEqual(new["ai"]["tools"], ["Pi"])
        self.assertEqual(new["github"]["latest_commit"]["date"], "2026-08-01")
        events = json.loads(self.activity.read_text())["events"]
        self.assertEqual(next(e for e in events if e["project_id"] == "old"), previous_event)
        addition = next(e for e in events if e["type"] == "project_added")
        self.assertEqual(addition["activity_context"]["commits_90d"], 1)
        self.assertEqual(addition["activity_context"]["latest_release"]["tag"], "v1")
        scope.check_complete(json.loads(self.manifest.read_text()), state)

    def test_metadata_failure_stays_pending_and_retries_on_schedule(self):
        self.seed()
        def failure(path, **kwargs):
            if path.endswith("/languages"):
                raise refresh.PrimaryReserve("quota reserve")
            return self.metadata(path, **kwargs)
        with patch.object(refresh, "get_json", side_effect=failure):
            refresh.main()
        with patch.object(collector, "api") as request:
            collector.main()
        request.assert_not_called()
        state = json.loads(self.state.read_text())
        self.assertTrue(scope.pending_publication(state["repositories"]["owner/repo"]))
        self.assertNotIn("last_deep_scan", state["repositories"]["owner/repo"])
        self.assertNotIn("activity_context", json.loads(self.activity.read_text())["events"][0])
        with self.assertRaises(SystemExit):
            scope.check_complete(json.loads(self.manifest.read_text()), state)
        # Scheduled recovery retains the required full-history marker even when
        # ordinary polling would skip this repository until a future deadline.
        state["repositories"]["unrelated/repo"]["scan_requested"] = False
        state["repositories"]["unrelated/repo"]["next_probe_due_at"] = "2030-01-01T00:00:00Z"
        self.state.write_text(json.dumps(state))
        self.manifest.write_text(json.dumps({"mode": "adaptive"}))
        with patch.object(refresh, "get_json", side_effect=self.metadata):
            refresh.main()
        with patch.object(collector, "api", side_effect=self.history):
            collector.main()
        scope.check_publishable(json.loads(self.state.read_text()), json.loads(self.projects.read_text()))

    def test_history_only_retry_keeps_completed_metadata_without_heavy_reenrichment(self):
        self.seed()
        with patch.object(refresh, "get_json", side_effect=self.metadata):
            refresh.main()
        self.manifest.write_text(json.dumps({"mode": "adaptive"}))
        state = json.loads(self.state.read_text())
        state["repositories"]["unrelated/repo"]["next_probe_due_at"] = "2030-01-01T00:00:00Z"
        self.state.write_text(json.dumps(state))
        with patch.object(refresh, "get_json") as request:
            refresh.main()
        request.assert_not_called()
        work = json.loads(self.state.read_text())["repositories"]["owner/repo"]["publication"]
        self.assertTrue(work["metadata_complete"])
        self.assertFalse(work["history_complete"])

    def test_history_failure_does_not_freeze_partial_context(self):
        self.seed()
        with patch.object(refresh, "get_json", side_effect=self.metadata):
            refresh.main()
        def failed(path, **kwargs):
            if "/branches?" in path:
                return self.history(path, **kwargs)
            raise collector.RateStop("budget exhausted on page 2")
        with patch.object(collector, "api", side_effect=failed):
            collector.main()
        state = json.loads(self.state.read_text())
        rs = state["repositories"]["owner/repo"]
        self.assertTrue(rs["scan_requested"])
        self.assertFalse(rs["publication"]["history_complete"])
        self.assertNotIn("last_deep_scan", rs)
        with patch.object(collector, "api", side_effect=self.history):
            collector.main()
        scope.check_complete(json.loads(self.manifest.read_text()), json.loads(self.state.read_text()))

    def test_missing_nonempty_root_metadata_cannot_be_marked_complete(self):
        self.seed()
        def request(path, **kwargs):
            if "/contents?" in path:
                return None, {}, 404
            return self.metadata(path, **kwargs)
        with patch.object(refresh, "get_json", side_effect=request):
            refresh.main()
        rs = json.loads(self.state.read_text())["repositories"]["owner/repo"]
        self.assertFalse(rs["publication"]["metadata_complete"])
        self.assertIn("Root metadata unavailable", rs["last_error"])

    def test_no_published_release_is_a_complete_empty_result(self):
        self.seed()
        def request(path, **kwargs):
            if path.endswith("/releases/latest"):
                self.assertTrue(kwargs.get("allow_404"))
                return None, {}, 404
            return self.metadata(path, **kwargs)
        with patch.object(refresh, "get_json", side_effect=request):
            refresh.main()
        rs = json.loads(self.state.read_text())["repositories"]["owner/repo"]
        self.assertTrue(rs["publication"]["metadata_complete"])
        new = next(p for p in json.loads(self.projects.read_text()) if p["id"] == "new")
        self.assertNotIn("latest_release", new["github"])

    def test_required_language_failure_does_not_get_waived(self):
        self.seed()
        def request(path, **kwargs):
            if path.endswith("/languages"):
                self.assertFalse(kwargs.get("allow_404"))
                raise RuntimeError("GitHub API 404 for languages")
            return self.metadata(path, **kwargs)
        with patch.object(refresh, "get_json", side_effect=request):
            refresh.main()
        rs = json.loads(self.state.read_text())["repositories"]["owner/repo"]
        self.assertFalse(rs["publication"]["metadata_complete"])
        self.assertTrue(rs["scan_requested"])

    def test_many_historical_heads_share_metadata_slice_and_ordinary_probe_continues(self):
        self.check_metadata_slice(40, False)

    def test_unknown_quota_metadata_slice_tightens_on_live_headers_and_ordinary_probe_continues(self):
        self.check_metadata_slice(4000, True)

    def check_metadata_slice(self, http_cap, live_quota):
        old, _ = self.seed()
        old["github"]["languages"] = ["C"]
        paths = [project("path-" + str(index), github_path="path-" + str(index)) for index in range(20)]
        other = project("other", "z/pending", github_path="other")
        records = [old, *paths, other]
        self.projects.write_text(json.dumps(records))
        delta = scope.catalogue_delta([old], records)
        self.manifest.write_text(json.dumps({"mode": "adaptive", "publication": delta}))
        state = json.loads(self.state.read_text())
        state["repositories"]["unrelated/repo"]["last_release_check_at"] = NOW_ISO
        self.state.write_text(json.dumps(state))
        requests = []
        class Response(io.BytesIO):
            status = 200
            headers = {}
        def network(request, **kwargs):
            url = request.full_url
            requests.append(url)
            self.assertNotIn("z/pending", url, "Each pending repository must share the same metadata slice")
            if "/languages" in url:
                payload = {"C": 100}
            elif "/contents?" in url:
                payload = []
            elif "/commits?" in url:
                payload = [commit()]
            else:
                payload = {"default_branch": "main", "pushed_at": "2026-08-01T00:00:00Z"}
            response = Response(json.dumps(payload).encode())
            if live_quota:
                response.headers = {"X-RateLimit-Limit": "5000", "X-RateLimit-Remaining": str(291 - len(requests))}
            return response
        with patch.multiple(refresh, REQUESTS=0, MAX_HTTP_REQUESTS=http_cap, REQUEST_DELAY=0), \
                patch.object(refresh, "urlopen", side_effect=network):
            refresh.main()
            self.assertEqual(refresh.PUBLICATION_REQUEST_LIMIT, 10)
            self.assertEqual(refresh.PUBLICATION_REQUESTS, 10)
            self.assertEqual(refresh.REQUESTS, 11)
        state = json.loads(self.state.read_text())
        pending = state["repositories"]["owner/repo"]
        self.assertFalse(pending["publication"]["metadata_complete"])
        self.assertFalse(pending["publication"]["history_complete"])
        self.assertTrue(pending["scan_requested"])
        self.assertIn("publication-only refresh", pending["last_error"])
        self.assertEqual(state["repositories"]["unrelated/repo"]["last_probe_at"], NOW_ISO)
        self.assertEqual(sum("unrelated/repo" in url for url in requests), 1)
        self.assertEqual(sum("/commits?" in url for url in requests), 7)
        self.assertTrue(scope.pending_publication(state["repositories"]["z/pending"]))
        with self.assertRaises(SystemExit):
            scope.check_complete(delta, state)

    def test_oversized_publications_share_adaptive_slice_and_ordinary_work_continues(self):
        self.check_history_slice(12, False)

    def test_unknown_quota_history_slice_tightens_on_live_headers_and_ordinary_scan_continues(self):
        self.check_history_slice(4000, True)

    def check_history_slice(self, http_cap, live_quota):
        self.seed()
        projects = json.loads(self.projects.read_text()) + [project("other", "other/pending")]
        self.projects.write_text(json.dumps(projects))
        self.manifest.write_text(json.dumps({"mode": "adaptive"}))
        state = json.loads(self.state.read_text())
        state["repositories"]["owner/repo"] = {
            "scan_requested": True, "scan_reason": "publication", "default_branch": "main",
            "publication": {"metadata_complete": True, "history_complete": False, "reset_project_ids": ["new"]}}
        state["repositories"]["other/pending"] = {
            "scan_requested": True, "scan_reason": "publication", "default_branch": "main",
            "last_deep_scan_attempt_at": "2026-10-01T11:00:00Z",
            "publication": {"metadata_complete": True, "history_complete": False, "reset_project_ids": ["other"]}}
        self.state.write_text(json.dumps(state))
        requests = []
        class Response(io.BytesIO):
            status = 200
            headers = {}
        def network(request, **kwargs):
            url = request.full_url
            requests.append(url)
            self.assertNotIn("other/pending", url, "The publication slice must be shared, not reset per repository")
            if "/branches?" in url:
                payload = [{"name": "main", "commit": {"sha": "ordinary-new"}}]
            elif "unrelated/repo" in url:
                payload = [commit("ordinary-new", day="2026-09-30")]
            else:
                page = int(parse_qs(urlparse(url).query)["page"][0])
                payload = [commit(f"huge-{page}-{index}") for index in range(100)]
            response = Response(json.dumps(payload).encode())
            if live_quota:
                response.headers = {"X-RateLimit-Limit": "5000", "X-RateLimit-Remaining": str(263 - len(requests))}
            return response
        with patch.multiple(collector, REQUESTS=0, MAX_HTTP_REQUESTS=http_cap, REQUEST_DELAY=0), \
                patch.object(collector, "urlopen", side_effect=network):
            collector.main()
            self.assertEqual(collector.PUBLICATION_REQUEST_LIMIT, 3)
            self.assertEqual(collector.PUBLICATION_REQUESTS, 3)
            self.assertEqual(collector.REQUESTS, 5)
        state = json.loads(self.state.read_text())
        huge = state["repositories"]["owner/repo"]
        ordinary = state["repositories"]["unrelated/repo"]
        self.assertTrue(huge["scan_requested"])
        self.assertFalse(huge["publication"]["history_complete"])
        self.assertNotIn("last_deep_scan", huge)
        self.assertIn("publication-only refresh", huge["last_error"])
        self.assertTrue(state["repositories"]["other/pending"]["scan_requested"])
        self.assertFalse(ordinary["scan_requested"])
        self.assertEqual(ordinary["last_deep_scan"], NOW_ISO)
        self.assertEqual(sum("unrelated/repo" in url for url in requests), 2)

    def test_path_change_clears_stale_aggregates_and_backfills_unchanged_tip(self):
        before = project("new", github_path="old", github={"tracking_branch": "main", "latest_commit": {"sha": "wrong"}})
        after = {**before, "github_path": "new"}
        self.seed([before], [after])
        state = json.loads(self.state.read_text())
        state["repositories"]["owner/repo"] = {"project_ids": ["new"], "last_deep_scan": NOW_ISO,
            "branches": {"main": {"tip_sha": "abc", "last_scan_at": NOW_ISO}}, "next_probe_due_at": "2030-01-01T00:00:00Z"}
        self.state.write_text(json.dumps(state))
        payload = json.loads(self.activity.read_text())
        payload["events"].append({"type": "daily_commits", "project_id": "new", "repository": "owner/repo",
            "date": "2026-08-01T00:00:00Z", "day": "2026-08-01", "shas": ["wrong"], "count": 1})
        self.activity.write_text(json.dumps(payload))
        with patch.object(refresh, "get_json", side_effect=self.metadata):
            refresh.main()
        calls = []
        def history(path, **kwargs):
            calls.append(path)
            return self.history(path, **kwargs)
        with patch.object(collector, "api", side_effect=history):
            collector.main()
        self.assertTrue(any("path=new" in path for path in calls))
        summaries = [e for e in json.loads(self.activity.read_text())["events"] if e["type"] == "daily_commits"]
        self.assertEqual(summaries[0]["shas"], ["abc"])


class CompletePaginationTest(unittest.TestCase):
    def test_history_exceeds_old_five_page_cap(self):
        def request(path, **kwargs):
            page = int(parse_qs(urlparse(path).query)["page"][0])
            return [commit(str(i)) for i in range((page - 1) * 100, min(page * 100, 601))]
        with patch.object(collector, "api", side_effect=request) as api:
            items = collector.fetch_commits("a/b", "main", NOW - timedelta(days=180), complete=True)
        self.assertEqual(len(items), 601)
        self.assertEqual(api.call_count, 7)

    def test_branches_exceed_first_hundred_and_missing_branch_is_failure(self):
        def request(path, **kwargs):
            page = int(parse_qs(urlparse(path).query)["page"][0])
            return [{"name": "branch" + str(i)} for i in range((page - 1) * 100, min(page * 100, 101))]
        with patch.object(collector, "api", side_effect=request):
            self.assertEqual(len(collector.list_branches("a/b", {"branch100"}, complete=True)), 101)
        with patch.object(collector, "api", side_effect=[[{"name": "main"}], None]):
            with self.assertRaises(RuntimeError):
                collector.list_branches("a/b", {"missing"})

    def test_normal_incremental_scans_keep_their_existing_caps(self):
        with patch.object(collector, "api", return_value=[commit()] * 100) as request:
            self.assertEqual(len(collector.fetch_commits("a/b", "main", NOW)), 500)
            self.assertEqual(request.call_count, 5)
        with patch.object(collector, "api", return_value=[{"name": "main"}] * 100) as request:
            self.assertEqual(set(collector.list_branches("a/b", {"main"})), {"main"})
            self.assertEqual(request.call_count, 1)

    def test_pagination_errors_propagate_instead_of_returning_partial_data(self):
        with patch.object(collector, "api", side_effect=[[commit()] * 100, collector.RateStop("limited")]):
            with self.assertRaises(collector.RateStop):
                collector.fetch_commits("a/b", "main", NOW, complete=True)


class RequestBudgetTest(unittest.TestCase):
    def test_adaptive_slice_uses_remaining_quota_and_publication_only_is_unrestricted(self):
        for module in (refresh, collector):
            with patch.multiple(module, REQUESTS=0, MAX_HTTP_REQUESTS=4000, RATE_LIMIT=5000, RATE_REMAINING=650):
                module.configure_publication_budget(True)
                self.assertEqual(module.PUBLICATION_REQUEST_LIMIT, 100)
                module.configure_publication_budget(False)
                self.assertIsNone(module.PUBLICATION_REQUEST_LIMIT)
            with patch.multiple(module, REQUESTS=0, MAX_HTTP_REQUESTS=10000, RATE_REMAINING=None):
                module.configure_publication_budget(True)
                self.assertEqual(module.PUBLICATION_REQUEST_LIMIT, 1000)
            module.configure_publication_budget(False)

    def test_live_quota_changes_can_only_tighten_the_adaptive_slice(self):
        for module in (refresh, collector):
            with patch.multiple(module, REQUESTS=0, MAX_HTTP_REQUESTS=4000, RATE_LIMIT=None, RATE_REMAINING=None):
                module.configure_publication_budget(True)
                self.assertEqual(module.PUBLICATION_REQUEST_LIMIT, 1000)
                module.PUBLICATION_REQUESTS = 1
                module.update_rate({"X-RateLimit-Limit": "5000", "X-RateLimit-Remaining": "290"})
                self.assertEqual(module.PUBLICATION_REQUEST_LIMIT, 10)
                module.update_rate({"X-RateLimit-Limit": "5000", "X-RateLimit-Remaining": "4000"})
                self.assertEqual(module.PUBLICATION_REQUEST_LIMIT, 10)
                module.update_rate({"X-RateLimit-Limit": "5000", "X-RateLimit-Remaining": "270"})
                self.assertEqual(module.PUBLICATION_REQUEST_LIMIT, 5)
                module.configure_publication_budget(False)

    def test_complete_pagination_is_still_bounded_by_http_and_rate_guards(self):
        for module in (refresh, collector):
            with patch.object(module, "REQUESTS", module.MAX_HTTP_REQUESTS), patch.object(module, "urlopen") as network:
                with self.assertRaises(module.RateStop):
                    module.api("/repos/a/b")
                network.assert_not_called()
            with patch.multiple(module, REQUESTS=0, RATE_LIMIT=5000, RATE_REMAINING=0), patch.object(module, "urlopen") as network:
                with self.assertRaises(module.PrimaryReserve):
                    module.api("/repos/a/b")
                network.assert_not_called()


class PublicationFairnessTest(unittest.TestCase):
    def test_pending_publications_precede_ordinary_work_and_failed_attempts_rotate(self):
        pending = {"metadata_complete": True, "history_complete": False}
        state = {"repositories": {
            "ordinary": {"scan_reason": "changed", "last_probe_at": "2020-01-01T00:00:00Z"},
            "scheduled": {"scan_reason": "scheduled"},
            "attempted": {"publication": pending, "scan_reason": "publication",
                          "last_deep_scan_attempt_at": "2026-10-01T11:00:00Z", "last_probe_at": NOW_ISO},
            "fresh": {"publication": pending, "scan_reason": "changed", "last_probe_at": NOW_ISO},
        }}
        repos = state["repositories"]
        self.assertEqual(collector.scan_order(repos, state), ["fresh", "attempted", "ordinary", "scheduled"])
        self.assertEqual(set(refresh.probe_order(repos, state)[:2]), {"fresh", "attempted"})
        state["repositories"]["fresh"]["last_deep_scan_attempt_at"] = NOW_ISO
        self.assertEqual(collector.scan_order(repos, state)[:2], ["attempted", "fresh"])


class WorkflowScopeTest(unittest.TestCase):
    def test_retry_recomputes_scope_with_job_level_auth_and_budget(self):
        text = (Path(__file__).resolve().parents[1] / ".github/workflows/refresh-github.yml").read_text()
        job_env = text.split("    env:", 1)[1].split("    steps:", 1)[0]
        for variable in ("GITHUB_TOKEN", "GITHUB_MIN_RATE_RESERVE", "GITHUB_HTTP_SAFETY_CAP", "GITHUB_REFRESH_SCOPE_FILE", "PUBLICATION_BASE", "PUBLICATION_HEAD"):
            self.assertIn(variable + ":", job_env)
        retry = text.split("git reset --hard origin/main", 1)[1]
        self.assertLess(retry.index("python tools/refresh_scope.py"), retry.index("python tools/refresh_github.py"))
        self.assertGreater(text.index("name: Require complete publication enrichment"), text.index("name: Commit changes"))


if __name__ == "__main__":
    unittest.main()
