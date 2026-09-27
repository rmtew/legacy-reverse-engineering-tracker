"""Bounded preflight reads root inventories and case-insensitive README files."""
from __future__ import annotations

import base64
import unittest

from discovery_triage import inventory, triage


class Client:
    def __init__(self):
        self.count, self.max_requests = 0, 2

    def get(self, url):
        self.count += 1
        if url.endswith("/contents"):
            return [{"name": "ReadMe.md", "type": "file"},
                    {"name": "game.bin", "type": "file"},
                    {"name": "src", "type": "dir"}]
        self.last = url
        return {"content": base64.b64encode(b"# A game\nDetails").decode(),
                "html_url": "https://github.com/example/repo/blob/main/ReadMe.md"}


class TriageTests(unittest.TestCase):
    def test_release_artifacts_keep_tool_and_source_visible(self):
        row = inventory([{'name': n, 'type': 'file'} for n in
                         ('README.md', 'MAD-example.6502', 'machine-auto-detect.ssd',
                          'machine-auto-detect.uef', 'max65.vsix')])
        self.assertTrue(row['root_signals']['source_files'])
        self.assertTrue(row['root_signals']['binary_files'])
        self.assertEqual(len(row['root_signals']['release_artifacts']), 3)
        self.assertNotIn('decision', row)

    def test_case_insensitive_readme_and_bounded_root_signals(self):
        client = Client()
        report = triage([("https://github.com/example/repo", {"origins": []})], client, 1)
        lead = report["leads"][0]
        self.assertEqual(report["requests"], 2)
        self.assertEqual(lead["readme_path"], "ReadMe.md")
        self.assertTrue(client.last.endswith("/contents/ReadMe.md"))
        self.assertIn("# A game", lead["readme_intro"])
        self.assertTrue(lead["root_signals"]["binary_files"])
        self.assertFalse(lead["root_signals"]["source_files"])
        self.assertEqual(lead["root_signals"]["source_directories"], ["src"])
        self.assertNotIn("decision", lead)


if __name__ == "__main__":
    unittest.main()
