import unittest

from generate_recent_activity import recent_activity


class RecentActivityTest(unittest.TestCase):
    def test_preserves_complete_events_including_cutoff_and_historical_project(self):
        activity = {
            "generated_at": "2026-09-25T08:00:00Z",
            "window_days": 180,
            "events": [
                {"date": "2026-09-25T07:00:00Z", "type": "commit", "message": "new"},
                {"date": "2026-08-26T08:00:00Z", "type": "project_removed", "project": {"id": "old"}},
                {"date": "2026-08-26T07:59:59Z", "type": "commit", "message": "old"},
            ],
        }
        output = recent_activity(activity)
        self.assertEqual(output["window_days"], 30)
        self.assertEqual(output["generated_at"], activity["generated_at"])
        self.assertEqual(output["events"], [
            {"date": "2026-09-25T07:00:00Z", "type": "commit"},
            activity["events"][1],
        ])
        self.assertEqual(len(activity["events"]), 3)

    def test_preserves_summary_membership_for_reading_inbox(self):
        event = {"date": "2026-09-20T07:00:00Z", "type": "daily_commits", "project_id": "p", "count": 2, "shas": ["a", "b"]}
        result = recent_activity({"generated_at": "2026-09-25T08:00:00Z", "events": [event]})
        self.assertEqual(result["events"][0]["shas"], ["a", "b"])


if __name__ == "__main__":
    unittest.main()
