"""Deterministic checks for search rotation, source mining and queue reconciliation."""
from __future__ import annotations

import base64
import json
from pathlib import Path
import tempfile
import unittest

from discovery_intake import (add_hits, collect_query, collect_source, empty_state, format_review_entry, github_candidate,
                              merge_state, rank_queue, review_entries, run)
from screen_discovery_candidates import CandidateIndex


class FakeClient:
    def __init__(self, responses):
        self.responses = responses
        self.count = 0
        self.max_requests = 30

    def get(self, url):
        self.count += 1
        for prefix, response in sorted(self.responses.items(), key=lambda item: -len(item[0])):
            if url.startswith(prefix):
                return response
        raise AssertionError(url)


class IntakeTests(unittest.TestCase):
    def test_nested_repository_source_collects_direct_children_with_two_requests(self):
        source = {'id': 'tools', 'kind': 'github-repository',
                  'source': 'https://github.com/owner/collection/tree/master/Amiga/Tools'}
        api = 'https://api.github.com/repos/owner/collection/contents/Amiga/Tools'
        readme = base64.b64encode(b'See https://github.com/other/engine').decode()
        client = FakeClient({
            api + '?ref=master': [
                {'name': 'ADFinder', 'type': 'dir',
                 'html_url': source['source'] + '/ADFinder'},
                {'name': 'readme.md', 'type': 'file', 'url': api + '/readme.md'}],
            api + '/readme.md?ref=master': {'content': readme, 'html_url': source['source'] + '/readme.md'},
        })
        leads = collect_source(client, source, 25)
        self.assertEqual(client.count, 2)
        self.assertEqual([lead['url'] for lead in leads], [
            source['source'] + '/ADFinder', 'https://github.com/other/engine'])

    def test_known_repository_review_line_shows_tracked_project(self):
        entry = {'score': 92, 'status': 'known_repository',
                 'url': 'https://github.com/old/collection',
                 'origins': [{'origin': 'source-profile'}]}
        line = format_review_entry(entry['url'], entry, self.index)
        self.assertIn('[tracked: old]', line)
        entry['status'] = 'new'
        self.assertNotIn('[tracked:', format_review_entry(entry['url'], entry, self.index))

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        data = self.root / "data"
        data.mkdir()
        (data / "projects.json").write_text(json.dumps([
            {"id": "old", "repo": "https://github.com/old/collection",
             "project_url": "https://github.com/old/collection/tree/main/games/old"},
        ]))
        (data / "discovery-sources.json").write_text(json.dumps({"sources": [
            {"id": "profile", "kind": "github-profile", "source": "https://github.com/author",
             "review_state": "partial"},
            {"id": "collection", "kind": "github-repository", "source": "https://github.com/old/collection",
             "review_state": "partial"},
        ]}))
        (data / "discovery-decisions.json").write_text(json.dumps({"decisions": [
            {"id": "excluded", "url": "https://github.com/author/excluded", "decision": "excluded"},
        ]}))
        self.index = CandidateIndex(data)

    def test_search_and_sources_extract_candidates(self):
        readme = base64.b64encode(b"See https://github.com/author/new-reassembly and https://github.com/old/collection").decode()
        client = FakeClient({
            "https://api.github.com/search/repositories?": {"items": [
                {"html_url": "https://github.com/author/new-reassembly", "full_name": "author/new-reassembly",
                 "description": "Amiga disassembly"},
                {"html_url": "https://github.com/author/fork", "fork": True},
            ]},
            "https://api.github.com/users/author/repos?": [
                {"html_url": "https://github.com/author/new-reassembly", "name": "new-reassembly"},
            ],
            "https://api.github.com/repos/old/collection/readme": {"content": readme,
                "html_url": "https://github.com/old/collection/blob/main/README.md"},
            "https://api.github.com/repos/old/collection/contents": [
                {"type": "dir", "name": "games", "url": "https://api.github.com/repos/old/collection/contents/games"},
            ],
            "https://api.github.com/repos/old/collection/contents/games": [
                {"type": "dir", "name": "new", "html_url": "https://github.com/old/collection/tree/main/games/new"},
            ],
        })
        query = collect_query(client, {"kind": "repositories", "id": "amiga", "q": "amiga"}, 20)
        self.assertEqual(len(query), 1)
        profile = collect_source(client, {"id": "profile", "kind": "github-profile",
                                          "source": "https://github.com/author"}, 25)
        repo = collect_source(client, {"id": "collection", "kind": "github-repository",
                                       "source": "https://github.com/old/collection"}, 25)
        self.assertEqual(profile[0]["origin"], "profile")
        self.assertIn("https://github.com/old/collection/tree/main/games/new", [h["url"] for h in repo])
        self.assertEqual(github_candidate("https://github.com/New/Repo/blob/main/README.md"),
                         "https://github.com/new/repo")
        self.assertEqual(github_candidate("https://github.com/New/Repo/tree/main/games/new"),
                         "https://github.com/new/repo/tree/main/games/new")

    def test_queue_keeps_provenance_and_resolves_new_decisions(self):
        state = empty_state()
        when = "2026-09-27T00:00:00Z"
        counts = add_hits(state, self.index, [
            {"url": "https://github.com/author/new-reassembly", "route": "github-repositories", "origin": "amiga",
             "description": "Amiga disassembly and reconstruction"},
            {"url": "https://github.com/author/new-reassembly/", "route": "source-github-profile", "origin": "profile"},
            {"url": "https://github.com/old/collection/tree/main/games/new", "route": "source-github-repository",
             "origin": "collection"},
            {"url": "https://github.com/author/excluded", "route": "github-repositories", "origin": "amiga"},
        ], when)
        self.assertEqual(counts["github-repositories"]["reviewed_decision"], 1)
        self.assertEqual(rank_queue(state, self.index)["open"], 2)
        new = state["queue"]["https://github.com/author/new-reassembly"]
        self.assertEqual(len(new["origins"]), 2)
        self.assertGreater(new["score"], 100)
        self.index.add("https://github.com/author/new-reassembly", {"kind": "project", "id": "added"})
        self.assertEqual(rank_queue(state, self.index)["resolved"], 1)

    def test_readme_search_platform_mismatch_changes_rank_without_dropping_lead(self):
        state = empty_state()
        add_hits(state, self.index, [
            {"url": "https://github.com/author/atari-st-emulator", "route": "github-repositories",
             "origin": "atari-st-disassembly", "description": "Atari ST emulator and debugger"},
            {"url": "https://github.com/author/generic-debugger", "route": "github-repositories",
             "origin": "atari-st-disassembly", "description": "Generic debugger for modern programs"},
            {"url": "https://github.com/author/atari-2600-emulator", "route": "github-repositories",
             "origin": "atari-st-disassembly", "description": "Atari 2600 emulator and debugger"},
        ], "2026-09-27T00:00:00Z")
        self.assertEqual(rank_queue(state, self.index)["open"], 3)
        self.assertEqual(next(iter(state["queue"])), "https://github.com/author/atari-st-emulator")
        self.assertLess(state["queue"]["https://github.com/author/atari-2600-emulator"]["score"],
                        state["queue"]["https://github.com/author/atari-st-emulator"]["score"])

    def test_code_search_bonus_requires_described_platform_match(self):
        state = empty_state()
        add_hits(state, self.index, [
            {"url": "https://github.com/author/atari-st", "route": "github-code",
             "origin": "atari-code", "description": "Atari ST debugger"},
            {"url": "https://github.com/author/generic", "route": "github-code",
             "origin": "atari-code", "description": "Archive recovery for generic files"},
        ], "2026-09-27T00:00:00Z")
        self.assertEqual(rank_queue(state, self.index)["open"], 2)
        self.assertGreater(state["queue"]["https://github.com/author/atari-st"]["score"],
                           state["queue"]["https://github.com/author/generic"]["score"])

    def test_rotate_queries_and_merge_after_concurrent_push(self):
        config = {"queries": [
            {"kind": "repositories", "id": "first", "q": "first"},
            {"kind": "repositories", "id": "second", "q": "second"}],
            "queries_per_run": 1, "results_per_query": 20, "sources_per_run": {}, "max_links_per_source": 10}
        client = FakeClient({"https://api.github.com/search/repositories?": {"items": [
            {"html_url": "https://github.com/author/new"}]}})
        produced = empty_state()
        run(self.root, client, config, produced, when="2026-09-27T01:00:00Z")
        self.assertEqual(produced["query_cursor"], 1)
        baseline = empty_state()
        baseline["queue"]["https://example.org/existing"] = {
            "url": "https://example.org/existing", "first_seen": "2026-09-26T00:00:00Z",
            "last_seen": "2026-09-26T00:00:00Z", "origins": []}
        merged = merge_state(baseline, produced)
        self.assertEqual(len(merged["queue"]), 2)
        self.assertEqual(merged["query_cursor"], 1)
        self.assertEqual(len(merged["runs"]), 1)

    def test_review_slice_diversifies_profile_without_losing_or_reordering_queue(self):
        queue = {f"https://github.com/owner/repo{i}": {
            "origins": [{"route": "source-github-profile", "origin": "owner"}]}
            for i in range(6)}
        queue.update({f"https://github.com/other/repo{i}": {
            "origins": [{"route": "github-repositories", "origin": "amiga-disassembly"}]}
            for i in range(2)})
        chosen = [key for key, _ in review_entries(queue, 4, max_per_profile=2)]
        self.assertEqual(chosen, ["https://github.com/owner/repo0", "https://github.com/owner/repo1",
                                  "https://github.com/other/repo0", "https://github.com/other/repo1"])
        self.assertEqual(len(review_entries(queue, 8, max_per_profile=2)), 8)
        self.assertEqual(len(queue), 8)

    def test_review_slice_caps_linked_repository_source_and_fills_spare_slots(self):
        queue = {f"https://github.com/dependency/repo{i}": {
            "origins": [{"route": "source-github-repository", "origin": "tool-readme"}]}
            for i in range(5)}
        queue.update({f"https://github.com/independent/repo{i}": {
            "origins": [{"route": "github-repositories", "origin": "amiga-tools"}]}
            for i in range(2)})
        selected = [key for key, _ in review_entries(queue, 4, max_per_source=2)]
        self.assertEqual(selected, ["https://github.com/dependency/repo0",
                                    "https://github.com/dependency/repo1",
                                    "https://github.com/independent/repo0",
                                    "https://github.com/independent/repo1"])
        self.assertEqual(len(review_entries(queue, 7, max_per_source=2)), 7)
        self.assertEqual(len(queue), 7)


if __name__ == "__main__":
    unittest.main()
