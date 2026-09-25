import unittest
from datetime import date
from unittest.mock import patch

import refresh_github


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


if __name__ == "__main__":
    unittest.main()
