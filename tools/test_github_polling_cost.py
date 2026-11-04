"""Offline regression tests for independent GitHub polling clocks and request cost."""
import copy
from contextlib import redirect_stdout, redirect_stderr
from datetime import datetime, timedelta, timezone
from io import StringIO
import unittest
from unittest.mock import patch

import refresh_github as probe

NOW = datetime(2026, 11, 4, 12, tzinfo=timezone.utc)
PUSH = "2026-11-04T11:00:00Z"
RELEASE = {"tag_name": "v2", "name": "Version 2", "published_at": PUSH,
           "html_url": "https://github.com/owner/repo/releases/tag/v2"}


def stamp(now):
    return now.isoformat(timespec="seconds").replace("+00:00", "Z")


def project():
    return {"id": "p", "repo": "https://github.com/owner/repo", "last_activity": "2026-11-04",
            "github": {"default_branch": "main", "languages": ["C"],
                       "latest_commit": {"sha": "a" * 40, "date": "2026-11-04"}}}


def repo_state():
    return {"project_ids": ["p"], "default_branch": "main", "last_seen_pushed_at": PUSH,
            "last_deep_scan": stamp(NOW), "last_metadata_check_at": stamp(NOW - timedelta(hours=1)),
            "last_release_check_at": stamp(NOW), "scan_requested": False}


class PollingCostTests(unittest.TestCase):
    def run_probe(self, row=None, rs=None, *, now=NOW, push=PUSH, repo_status=200,
                  release_status=404, release=RELEASE, error_endpoint=None):
        row = copy.deepcopy(row if row is not None else project())
        rs = copy.deepcopy(rs if rs is not None else repo_state())
        state = {"repositories": {"owner/repo": rs}}
        calls = []
        def request(path, **kwargs):
            calls.append((path, kwargs))
            if error_endpoint and path.endswith(error_endpoint):
                raise RuntimeError("temporary failure")
            if path == "/repos/owner/repo":
                info = {"pushed_at": push, "default_branch": "main", "archived": False}
                return (info if repo_status == 200 else None), {}, repo_status
            if path.endswith("/languages"):
                return {"C": 100}, {}, 200
            if "/contents?" in path:
                return [], {}, 200
            if path.endswith("/releases/latest"):
                return (release if release_status == 200 else None), {"ETag": '"release"'}, release_status
            self.fail("Unexpected API request: " + path)
        with patch.multiple(probe, RUN_AT=now, TODAY=now.date(), FORCE_FULL_PROBE=True,
                            REQUESTS=0, RATE_LIMIT=None, RATE_REMAINING=None, RATE_RESET=None,
                            RATE_START_REMAINING=None), \
                patch.object(probe, "get_json", side_effect=request), \
                redirect_stdout(StringIO()), redirect_stderr(StringIO()):
            probe.main(records=[row], state=state, scope={"mode": "adaptive"}, persist=False)
        return row, rs, calls

    def test_push_queues_commits_without_repeating_slow_metadata_or_release(self):
        row, rs, calls = self.run_probe(push="2026-11-04T11:59:00Z")
        self.assertEqual([path for path, _ in calls], ["/repos/owner/repo"])
        self.assertTrue(rs["scan_requested"])
        self.assertEqual(rs["scan_reason"], "changed")
        self.assertEqual(rs["last_seen_pushed_at"], "2026-11-04T11:59:00Z")
        self.assertEqual(row["github"]["languages"], ["C"])

    def test_repeated_pushes_do_not_bypass_confirmed_empty_release_backoff(self):
        rs = repo_state()
        rs.update(release_empty_checks=3, last_release_check_at=stamp(NOW - timedelta(hours=7)))
        _, rs, calls = self.run_probe(rs=rs, push="2026-11-04T11:59:00Z")
        self.assertEqual(len(calls), 1)
        self.assertTrue(rs["scan_requested"])
        self.assertEqual(rs["release_empty_checks"], 3)

    def test_known_release_keeps_six_hour_checks_without_a_push(self):
        row, rs = project(), repo_state()
        probe.update_latest_release([row], RELEASE)
        rs["last_release_check_at"] = stamp(NOW - timedelta(hours=6))
        row, rs, calls = self.run_probe(row, rs, release_status=200)
        self.assertEqual([path for path, _ in calls], ["/repos/owner/repo", "/repos/owner/repo/releases/latest"])
        self.assertFalse(rs["scan_requested"])
        self.assertEqual(row["github"]["latest_release"]["tag"], "v2")
        self.assertEqual(rs["last_release_check_at"], stamp(NOW))

    def test_confirmed_absence_backs_off_to_daily_and_recovers_without_push(self):
        rs = repo_state()
        row = project()
        now = NOW
        for count, delay in ((1, 6), (2, 12), (3, 24), (3, 24)):
            rs["last_release_check_at"] = stamp(now - timedelta(hours=24))
            row, rs, calls = self.run_probe(row, rs, now=now)
            self.assertEqual(rs["release_empty_checks"], count)
            with patch.object(probe, "TODAY", now.date()):
                self.assertEqual(probe.release_interval_hours([row], rs, row["last_activity"]), delay)
            now += timedelta(hours=delay)
        # The daily expiry still discovers a release even if repository pushed_at never changes.
        rs["last_release_check_at"] = stamp(now - timedelta(hours=24))
        row, rs, calls = self.run_probe(row, rs, now=now, release_status=200)
        self.assertNotIn("release_empty_checks", rs)
        self.assertEqual(row["github"]["latest_release"]["tag"], "v2")
        with patch.object(probe, "TODAY", now.date()):
            self.assertEqual(probe.release_interval_hours([row], rs, row["last_activity"]), 6)

    def test_release_error_never_counts_as_absent_or_fresh(self):
        rs = repo_state()
        rs.update(release_empty_checks=1, last_release_check_at=stamp(NOW - timedelta(hours=6)))
        _, result, _ = self.run_probe(rs=rs, error_endpoint="/releases/latest")
        self.assertEqual(result["release_empty_checks"], 1)
        self.assertEqual(result["last_release_check_at"], rs["last_release_check_at"])

    def test_conditional_release_304_keeps_existing_release(self):
        row, rs = project(), repo_state()
        probe.update_latest_release([row], RELEASE)
        rs.update(release_etag='"old"', last_release_check_at=stamp(NOW - timedelta(hours=6)))
        row, rs, calls = self.run_probe(row, rs, repo_status=304, release_status=304)
        self.assertEqual(calls[-1][1]["etag"], '"old"')
        self.assertEqual(row["github"]["latest_release"]["tag"], "v2")
        self.assertEqual(rs["last_release_check_at"], stamp(NOW))
        self.assertNotIn("release_empty_checks", rs)

    def test_no_release_etag_is_used_without_cached_release(self):
        rs = repo_state()
        rs.update(release_etag='"obsolete"', last_release_check_at=stamp(NOW - timedelta(days=1)))
        _, rs, calls = self.run_probe(rs=rs)
        self.assertIsNone(calls[-1][1]["etag"])
        self.assertNotIn("release_etag", rs)

    def test_metadata_refreshes_daily_even_on_repository_304(self):
        rs = repo_state()
        rs["last_metadata_check_at"] = stamp(NOW - timedelta(days=1))
        _, rs, calls = self.run_probe(rs=rs, repo_status=304)
        self.assertEqual([path for path, _ in calls], [
            "/repos/owner/repo", "/repos/owner/repo/languages", "/repos/owner/repo/contents?ref=main"])
        self.assertEqual(rs["last_metadata_check_at"], stamp(NOW))

    def test_completed_metadata_is_reused_while_push_and_branch_are_unchanged(self):
        rs = repo_state()
        rs.update(last_metadata_check_at=stamp(NOW - timedelta(days=30)),
                  last_metadata_pushed_at=PUSH, last_metadata_branch="main")
        _, _, calls = self.run_probe(rs=rs)
        self.assertEqual(len(calls), 1)
        # A later observed push is refreshed when the metadata clock is due.
        _, result, calls = self.run_probe(rs=rs, push="2026-11-04T11:59:00Z")
        self.assertEqual(len(calls), 3)
        self.assertEqual(result["last_metadata_pushed_at"], "2026-11-04T11:59:00Z")

    def test_push_seen_before_metadata_deadline_is_not_forgotten(self):
        rs = repo_state()
        rs.update(last_metadata_check_at=stamp(NOW - timedelta(hours=1)),
                  last_metadata_pushed_at=PUSH, last_metadata_branch="main")
        _, rs, calls = self.run_probe(rs=rs, push="2026-11-04T11:59:00Z")
        self.assertEqual(len(calls), 1)
        rs["last_release_check_at"] = stamp(NOW + timedelta(days=1))
        _, rs, calls = self.run_probe(rs=rs, push="2026-11-04T11:59:00Z", now=NOW + timedelta(days=1))
        self.assertEqual(len(calls), 3)
        self.assertEqual(rs["last_metadata_pushed_at"], "2026-11-04T11:59:00Z")

    def test_dormant_metadata_is_weekly_not_every_daily_probe(self):
        row, rs = project(), repo_state()
        row["last_activity"] = "2020-01-01"
        rs["last_metadata_check_at"] = stamp(NOW - timedelta(days=6))
        _, _, calls = self.run_probe(row, rs)
        self.assertEqual(len(calls), 1)
        rs["last_metadata_check_at"] = stamp(NOW - timedelta(days=7))
        _, _, calls = self.run_probe(row, rs)
        self.assertEqual(len(calls), 3)

    def test_empty_languages_are_cached_but_configuration_has_its_own_refresh(self):
        row, rs = project(), repo_state()
        row["github"]["languages"] = []
        rs.update(empty_languages_checked_at="2026-11-03", empty_languages_pushed_at=PUSH,
                  last_metadata_check_at=stamp(NOW - timedelta(days=1)))
        _, _, calls = self.run_probe(row, rs)
        self.assertEqual([path for path, _ in calls], ["/repos/owner/repo", "/repos/owner/repo/contents?ref=main"])
        # A new push invalidates empty languages only at the slow metadata deadline.
        _, _, calls = self.run_probe(row, rs, push="2026-11-04T11:59:00Z")
        self.assertIn("/repos/owner/repo/languages", [path for path, _ in calls])
        rs["last_metadata_check_at"] = stamp(NOW - timedelta(hours=1))
        _, _, calls = self.run_probe(row, rs, push="2026-11-04T11:59:00Z")
        self.assertEqual(len(calls), 1)
        rs.update(last_metadata_check_at=stamp(NOW - timedelta(days=1)),
                  empty_languages_checked_at="2026-10-05")
        _, _, calls = self.run_probe(row, rs)
        self.assertIn("/repos/owner/repo/languages", [path for path, _ in calls])

    def test_publication_bypasses_metadata_and_release_cooldowns(self):
        rs = repo_state()
        rs.update(release_empty_checks=3, publication={"metadata_complete": False, "history_complete": False})
        _, rs, calls = self.run_probe(rs=rs, release_status=200)
        self.assertEqual(len(calls), 4)
        self.assertTrue(rs["publication"]["metadata_complete"])
        self.assertNotIn("release_empty_checks", rs)

    def test_migration_staggers_populated_metadata_without_claiming_freshness(self):
        due_dates = set()
        with patch.multiple(probe, RUN_AT=NOW, TODAY=NOW.date()):
            for number in range(100):
                rs = {}
                self.assertFalse(probe.metadata_due(f"o/r{number}", rs, [project()], "2020-01-01"))
                self.assertNotIn("last_metadata_check_at", rs)
                due = probe.parse_time(rs["next_metadata_due_at"])
                self.assertGreater(due, NOW)
                self.assertLessEqual(due, NOW + timedelta(days=7))
                due_dates.add(due)
                with patch.object(probe, "RUN_AT", due):
                    self.assertTrue(probe.metadata_due(f"o/r{number}", rs, [project()], "2020-01-01"))
        self.assertGreater(len(due_dates), 20)

    def test_missing_metadata_is_not_staggered(self):
        row = project()
        del row["github"]["languages"]
        with patch.multiple(probe, RUN_AT=NOW, TODAY=NOW.date()):
            self.assertTrue(probe.metadata_due("o/r", {}, [row], "2020-01-01"))
        rs = repo_state()
        rs.update(empty_languages_checked_at="2026-11-03", empty_languages_pushed_at=PUSH)
        row, _, calls = self.run_probe(row, rs)
        self.assertIn("/repos/owner/repo/languages", [path for path, _ in calls])
        self.assertEqual(row["github"]["languages"], ["C"])


if __name__ == "__main__":
    unittest.main()
