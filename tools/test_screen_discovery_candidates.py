"""Checks that early screening saves research without hiding new subprojects."""
from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest

from screen_discovery_candidates import CandidateIndex, canonical_url, read_candidates, screen_batch


class CandidateScreenTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        data = Path(self.temp.name)
        (data / "projects.json").write_text(json.dumps([
            {"id": "game-a", "repo": "https://github.com/Example/Collection",
             "project_url": "https://github.com/Example/Collection/tree/main/games/A"},
            {"id": "single", "repo": "https://github.com/Example/Single"},
        ]))
        (data / "discovery-sources.json").write_text(json.dumps({"sources": [
            {"id": "example-profile", "source": "https://github.com/Example", "review_state": "partial"},
            {"id": "catalogue", "source": "https://example.org/catalogue", "review_state": "unreviewed"},
        ]}))
        (data / "discovery-decisions.json").write_text(json.dumps({"decisions": [
            {"id": "old-game-a", "url": "https://github.com/Old/A/tree/master",
             "decision": "duplicate", "project_ids": ["game-a"]},
            {"id": "deferred", "url": "https://example.org/unknown", "decision": "deferred"},
        ]}))
        self.index = CandidateIndex(data)

    def test_url_variations_and_case_sensitive_repository_paths(self):
        self.assertEqual(canonical_url("http://www.GitHub.com/EXAMPLE/Collection.git/?utm_source=a#readme"),
                         "https://github.com/example/collection")
        self.assertEqual(self.index.screen("https://github.com/EXAMPLE/collection/tree/main/games/A/")["status"],
                         "tracked_project")
        self.assertEqual(self.index.screen("https://github.com/example/collection/tree/main/games/a")["status"],
                         "known_repository_path")
        self.assertNotEqual(canonical_url("https://example.org/item?a=1"),
                            canonical_url("https://example.org/item?a=2"))

    def test_known_parent_does_not_hide_new_repository_or_directory(self):
        self.assertEqual(self.index.screen("https://github.com/example/new-repo")["status"], "new")
        self.assertEqual(self.index.screen("https://github.com/example/collection/tree/main/games/B")["status"],
                         "known_repository_path")
        self.assertEqual(self.index.screen("https://github.com/example/collection")["status"], "known_repository")
        self.assertEqual(self.index.screen("https://github.com/example")["status"], "known_source")
        self.assertEqual(self.index.screen("https://example.org/catalogue")["matches"][0]["review_state"],
                         "unreviewed")

    def test_decision_alias_retains_target_and_deferred_state(self):
        result = self.index.screen("https://github.com/Old/A/tree/master")
        self.assertEqual(result["status"], "reviewed_decision")
        self.assertEqual(result["target_project_urls"],
                         ["https://github.com/Example/Collection/tree/main/games/A"])
        self.assertEqual(self.index.screen("https://example.org/unknown")["matches"][0]["decision"], "deferred")

    def test_route_counts_and_repeated_hits(self):
        report = screen_batch(self.index, [
            {"url": "https://github.com/Example/Single", "route": "repository search"},
            {"url": "https://github.com/example/single/", "route": "web search"},
            {"url": "https://github.com/Example/Collection/tree/main/games/B", "route": "web search"},
        ])
        self.assertEqual(report["summary"]["unique_urls"], 2)
        self.assertEqual(report["summary"]["by_route"]["web search"],
                         {"repeat_in_batch": 1, "known_repository_path": 1})

    def test_newline_and_json_inputs(self):
        path = Path(self.temp.name) / "candidates.txt"
        path.write_text("# comment\nhttps://example.org/a\n")
        self.assertEqual(read_candidates(str(path), "web"), [{"url": "https://example.org/a", "route": "web"}])
        path.write_text('[{"url":"https://example.org/a","route":"code search"}]')
        self.assertEqual(read_candidates(str(path), "web")[0]["route"], "code search")


if __name__ == "__main__":
    unittest.main()
