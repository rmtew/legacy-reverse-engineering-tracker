import json
import tempfile
import unittest
from pathlib import Path
from xml.etree import ElementTree as ET

from generate_rss import generate, release_events, daily_description, release_description, change_description


class RssTest(unittest.TestCase):
    def test_unavailable_status_discloses_retained_facts_without_removing_history(self):
        for provider in ("github", "gitlab"):
            project = {"id": "p", "repo": f"https://{provider}.com/a/b", provider: {"source_availability": {
                "status": "unavailable", "http_status": 404, "retryable": True}}}
            for render in (daily_description, release_description, change_description):
                with self.subTest(provider=provider, render=render.__name__):
                    text = render({}, project)
                    self.assertIn("prior metadata retained; retryable", text)
                    self.assertNotIn("removed", text)
                    self.assertNotIn("unavailable", render({}, {"id": "p"}))

    def test_release_keeps_calendar_date_without_inventing_noon_utc(self):
        project = {"id": "p", "github": {"latest_release": {
            "tag": "v1", "published_at": "2026-09-26"}}}
        self.assertEqual(release_events([project])[0]["date"], "2026-09-26")

    def test_gitlab_release_metadata_uses_its_repository_and_upstream_link(self):
        project = {"id": "p", "repo": "https://gitlab.com/group/subgroup/project", "gitlab": {
            "repository": "gitlab.com/group/subgroup/project", "latest_release": {
                "tag": "v1", "name": "First release", "published_at": "2026-09-26",
                "url": "https://gitlab.com/group/subgroup/project/-/releases/v1"}}}
        event = release_events([project])[0]
        self.assertEqual(event["repository"], project["gitlab"]["repository"])
        self.assertEqual(event["url"], project["gitlab"]["latest_release"]["url"])
        self.assertEqual(event["message"], "First release")
        self.assertEqual(event["date"], "2026-09-26")
        project["gitlab"]["source_availability"] = {"status": "unavailable", "http_status": 404}
        self.assertEqual(release_events([project]), [event])

    def test_moved_project_does_not_use_old_provider_release_metadata(self):
        project = {"id": "p", "repo": "https://gitlab.com/a/b", "github": {
            "latest_release": {"tag": "stale", "published_at": "2026-09-26"}}}
        self.assertEqual(release_events([project]), [])

    def test_no_release_is_invented_when_gitlab_release_lookup_has_no_result(self):
        for release in (None, {}, {"tag": "v1"}):
            with self.subTest(release=release):
                project = {"id": "p", "repo": "https://gitlab.com/a/b", "gitlab": {
                    "repository": "gitlab.com/a/b", "latest_release": release,
                    "source_availability": {"status": "unavailable", "http_status": 404}}}
                self.assertEqual(release_events([project]), [])

    def test_stored_releases_preserve_intermediate_versions_and_dedupe_latest(self):
        project = {"id": "p", "repo": "https://gitlab.com/a/b", "gitlab": {
            "latest_release": {"tag": "v2", "published_at": "2026-09-27"}}}
        first = {"type": "release", "project_id": "p", "tag": "v1", "date": "2026-09-26T12:00:00Z",
                 "url": "https://gitlab.com/a/b/-/releases/v1"}
        latest = {**first, "tag": "v2", "date": "2026-09-27T12:00:00Z",
                  "url": "https://gitlab.com/a/b/-/releases/v2"}
        removed = {**first, "project_id": "removed"}
        self.assertEqual(release_events([project], [first, latest, latest.copy(), removed]), [first, latest])
        project["gitlab"]["latest_release"] = None
        self.assertEqual(release_events([project], [first, latest]), [first, latest])

    def test_gitlab_pending_scan_and_commit_links_are_provider_neutral(self):
        project = {"id": "p", "title": "Project", "repo": "https://gitlab.com/a/subgroup/b"}
        self.assertIn("Initial activity scan pending", change_description({"type": "project_added"}, project))
        commit = {"sha": "abc", "title": "Fix & build", "url": project["repo"] + "/-/commit/abc"}
        description = daily_description({"commits": [commit]}, project)
        self.assertIn('href="https://gitlab.com/a/subgroup/b/-/commit/abc"', description)
        self.assertIn("Fix &amp; build", description)

    def test_feed_keeps_stored_release_timestamp_and_stable_guids(self):
        activity = {"generated_at": "2026-09-28T20:00:00Z", "events": [
            {"type": "release", "project_id": "p", "tag": "v2", "date": "2026-09-27T12:00:00Z",
             "url": "https://gitlab.com/a/b/-/releases/v2", "name": "Second release"},
            {"type": "release", "project_id": "p", "tag": "v1", "date": "2026-09-26T12:00:00Z",
             "url": "https://gitlab.com/a/b/-/releases/v1"}]}
        projects = [{"id": "p", "title": "Example", "repo": "https://gitlab.com/a/b", "gitlab": {
            "latest_release": {"tag": "v2", "published_at": "2026-09-27"}}}]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "activity.json").write_text(json.dumps(activity))
            (root / "projects.json").write_text(json.dumps(projects))
            generate(root / "activity.json", root / "projects.json", root / "feed.xml", 500)
            items = ET.parse(root / "feed.xml").findall(".//item")
        self.assertEqual([item.findtext("guid") for item in items], ["legacy-re:p:release:v2", "legacy-re:p:release:v1"])
        self.assertEqual(items[0].findtext("link"), activity["events"][0]["url"])
        self.assertEqual(items[0].findtext("pubDate"), "Sun, 27 Sep 2026 12:00:00 +0000")
        self.assertIn("Second release", items[0].findtext("description"))

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
        self.assertIn("At addition (90-day window)", items[1].findtext("description"))

    def test_expired_releases_and_catalogue_events_are_not_regenerated(self):
        activity = {"generated_at": "2026-10-19T00:00:00Z", "events": [
            {"type": "project_added", "project_id": "p", "date": "2026-09-18T23:59:59Z", "title": "old"}]}
        projects = [{"id": "p", "title": "Old", "github": {"latest_release": {
            "tag": "old", "published_at": "2026-09-18"}}}]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "activity.json").write_text(json.dumps(activity))
            (root / "projects.json").write_text(json.dumps(projects))
            generate(root / "activity.json", root / "projects.json", root / "feed.xml", 500)
            self.assertEqual(ET.parse(root / "feed.xml").findall(".//item"), [])


if __name__ == "__main__":
    unittest.main()
