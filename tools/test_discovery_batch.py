"""Integration checks for cross-file discovery batches and failure isolation."""
from __future__ import annotations

import copy
from contextlib import redirect_stderr
import io
import json
from pathlib import Path
import shutil
import tempfile
import unittest

from apply_discovery_batch import FILES, ROOT, run
from merge_pending_projects import new_audit


class DiscoveryBatchTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.data = self.root / "data"
        self.data.mkdir()
        for name in (*FILES, "activity.json"):
            shutil.copy2(ROOT / "data" / name, self.data / name)
        self.before = {name: (self.data / name).read_bytes() for name in FILES}
        self.source_id = "web-6502disassembly-com"

    def batch(self):
        original = json.loads((self.data / "projects.json").read_text())
        day = json.loads((self.data / "research-activity.json").read_text())["events"][0]["date"]
        project = copy.deepcopy(next(item for item in original if item["id"] == "abm-apple2-6502disassembly"))
        project.update(id="sample-research-test", title="Sample research", upstream_name="Sample research",
                       display_title="Sample research — test disassembly", subjects=["Sample research"],
                       repo="https://example.org/sample-research", project_url="https://example.org/sample-research")
        return {
            "date": day, "event_id": day + "-test-research", "summary": "Test discovery batch",
            "projects": [{"project": project, "source_ids": [self.source_id],
                          "audit": self.researched_audit(day)}],
            "decisions": [{"id": "sample-exclusion", "title": "Sample excluded lead",
                           "url": "https://example.org/excluded", "decision": "excluded",
                           "reason": "Verified conversion of an existing listing.",
                           "evidence_urls": ["https://example.org/excluded"],
                           "source_ids": [self.source_id]}],
        }

    def researched_audit(self, day):
        audit = new_audit("sample-research-test")
        audit["last_reviewed"] = day
        audit["overall_state"] = "partial"
        for area in ("source_cpu", "target_cpu"):
            audit["areas"][area] = {"state": "reviewed" if area == "source_cpu" else "not-applicable",
                                     "checked_at": day}
        return audit

    def test_preview_then_apply_links_all_records(self):
        batch = self.batch()
        preview = run(self.root, batch, write=False)
        self.assertEqual(preview["projects"], ["sample-research-test"])
        self.assertTrue(all((self.data / name).read_bytes() == content for name, content in self.before.items()))

        run(self.root, batch, write=True)
        audits = json.loads((self.data / "project-audits.json").read_text())
        sources = json.loads((self.data / "discovery-sources.json").read_text())
        events = json.loads((self.data / "research-activity.json").read_text())
        self.assertEqual(next(a for a in audits["projects"] if a["project_id"] == "sample-research-test")["overall_state"], "partial")
        self.assertIn("sample-research-test", next(s for s in sources["sources"] if s["id"] == self.source_id)["projects_promoted"])
        self.assertEqual(events["events"][0]["id"], batch["event_id"])
        original_count = len(json.loads(self.before["discovery-decisions.json"])["decisions"])
        self.assertEqual(len(json.loads((self.data / "discovery-decisions.json").read_text())["decisions"]), original_count + 1)

    def test_new_project_requires_cpu_review(self):
        batch = self.batch()
        del batch["projects"][0]["audit"]
        with self.assertRaisesRegex(ValueError, "explicit researched audit"):
            run(self.root, batch, write=True)
        self.assertTrue(all((self.data / name).read_bytes() == content for name, content in self.before.items()))

    def test_invalid_link_never_writes(self):
        batch = self.batch()
        batch["decisions"][0]["project_ids"] = ["missing-project"]
        with redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit):
                run(self.root, batch, write=True)
        self.assertTrue(all((self.data / name).read_bytes() == content for name, content in self.before.items()))

    def test_repeated_project_url_needs_explicit_override(self):
        batch = self.batch()
        batch["projects"][0]["project"]["project_url"] = "https://6502disassembly.com/a2-abm/"
        with self.assertRaisesRegex(ValueError, "shares URL"):
            run(self.root, batch, write=True)
        self.assertTrue(all((self.data / name).read_bytes() == content for name, content in self.before.items()))


if __name__ == "__main__":
    unittest.main()
