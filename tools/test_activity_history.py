import unittest
from datetime import datetime, timezone

from activity_history import compact_history, freeze_addition_context


class ActivityHistoryTest(unittest.TestCase):
    def test_old_commits_merge_by_project_and_local_day_without_duplicate_shas(self):
        now = datetime(2026, 9, 26, tzinfo=timezone.utc)
        commit = lambda sha, date: {
            "type": "commit", "date": date, "project_id": "p", "repository": "a/b",
            "sha": sha, "title": sha, "url": "https://example.com/" + sha,
        }
        events = [
            commit("old", "2026-09-01T22:00:00Z"),
            commit("next", "2026-09-02T02:00:00Z"),
            commit("old", "2026-09-01T22:00:00Z"),
            commit("fresh", "2026-09-25T02:00:00Z"),
        ]
        result = compact_history(events, now)
        self.assertEqual(len(result), 2)
        summary = next(event for event in result if event["type"] == "daily_commits")
        self.assertEqual(summary["day"], "2026-09-02")
        self.assertEqual(summary["count"], 2)
        self.assertEqual(summary["shas"], ["next", "old"])
        self.assertEqual(summary["latest_title"], "next")

    def test_backfilled_sha_does_not_inflate_existing_summary(self):
        now = datetime(2026, 9, 26, tzinfo=timezone.utc)
        previous = {"type": "daily_commits", "date": "2026-08-01T01:00:00Z",
                    "day": "2026-08-01", "project_id": "p", "repository": "a/b",
                    "shas": ["a", "b"], "count": 2, "latest_title": "b"}
        repeated = {"type": "commit", "date": "2026-08-01T01:00:00Z",
                    "project_id": "p", "repository": "a/b", "sha": "b", "title": "b"}
        result = compact_history([previous, repeated], now)
        self.assertEqual(result[0]["count"], 2)

    def test_addition_context_waits_for_scan_then_freezes_release_and_activity(self):
        now = datetime(2026, 9, 26, tzinfo=timezone.utc)
        addition = {"type": "project_added", "date": "2026-09-25T00:00:00Z", "project_id": "p"}
        summary = {"type": "daily_commits", "date": "2026-09-20T02:00:00Z", "day": "2026-09-20",
                   "project_id": "p", "count": 3}
        project = {"id": "p", "last_activity": "2026-09-20", "github": {
            "repository": "a/b", "latest_commit": {"date": "2026-09-20"},
            "latest_release": {"tag": "v1", "published_at": "2026-09-19"}}}
        freeze_addition_context([addition, summary], [project],
                                {"a/b": {"last_deep_scan": "2026-09-24T23:00:00Z"}}, now)
        self.assertNotIn("activity_context", addition)
        freeze_addition_context([addition, summary], [project],
                                {"a/b": {"last_deep_scan": "2026-09-25T01:00:00Z"}}, now)
        self.assertEqual(addition["activity_context"]["commits_90d"], 3)
        self.assertEqual(addition["activity_context"]["active_days_90d"], 1)
        self.assertEqual(addition["activity_context"]["latest_release"]["tag"], "v1")
        project["github"]["latest_release"]["tag"] = "v2"
        self.assertEqual(addition["activity_context"]["latest_release"]["tag"], "v1")


if __name__ == "__main__":
    unittest.main()
