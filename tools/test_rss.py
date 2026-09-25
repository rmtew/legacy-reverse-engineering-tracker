import json
import tempfile
import unittest
from pathlib import Path
from xml.etree import ElementTree as ET

from generate_rss import generate


class RssTest(unittest.TestCase):
    def test_settled_days_and_project_addition_context(self):
        activity = {"generated_at": "2026-09-28T20:00:00Z", "events": [
            {"type": "project_added", "date": "2026-09-27T00:00:00Z", "project_id": "p",
             "project": {"id": "p", "title": "Example"}, "title": "Project added",
             "activity_context": {"last_commit": {"date": "2026-09-24"},
                                  "latest_release": {"tag": "v1", "published_at": "2026-08-01"},
                                  "commits_90d": 2, "active_days_90d": 1}},
            {"type": "commit", "date": "2026-09-28T02:00:00Z", "project_id": "p", "sha": "new", "title": "new"},
            {"type": "commit", "date": "2026-09-27T02:00:00Z", "project_id": "p", "sha": "settled", "title": "settled"},
            {"type": "commit", "date": "2026-09-26T02:00:00Z", "project_id": "p", "sha": "backfill", "title": "backfill"},
        ]}
        projects = [{"id": "p", "title": "Example", "repo": "https://github.com/a/b"}]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "activity.json").write_text(json.dumps(activity))
            (root / "projects.json").write_text(json.dumps(projects))
            generate(root / "activity.json", root / "projects.json", root / "feed.xml", 500)
            items = ET.parse(root / "feed.xml").getroot().find("channel").findall("item")
        self.assertEqual(len(items), 2)
        self.assertEqual(items[0].findtext("guid"), "legacy-re:p:day:2026-09-27")
        self.assertIn("Latest release", items[1].findtext("description"))
        self.assertIn("Last 90 days", items[1].findtext("description"))


if __name__ == "__main__":
    unittest.main()
