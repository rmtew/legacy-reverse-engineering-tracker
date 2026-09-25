"""Checks the CPU research queue selects unresolved audits without inventing CPUs."""
from __future__ import annotations

import unittest

from cpu_audit_queue import queue


def project(id, source_cpu=None, source_language=None, kind="subject"):
    return {"id": id, "repo": f"https://example.org/{id}", "record_class": kind,
            "source_cpu": source_cpu or [], "target_cpu": [],
            "source_platforms": ["Atari ST"], "target_platforms": ["Amiga"],
            "source_language": source_language or []}


def audit(id, source, target="not-applicable"):
    return {"project_id": id, "last_reviewed": None,
            "areas": {"source_cpu": {"state": source}, "target_cpu": {"state": target}}}


class CpuAuditQueueTests(unittest.TestCase):
    def test_unresolved_binary_ranks_ahead_of_data_only_and_resolved(self):
        projects = [
            project("data-only", source_language=["archive data"]),
            project("binary", source_language=["m68000 machine code"]),
            project("reviewed", source_cpu=["m68000"], source_language=["machine code"]),
        ]
        audits = [audit("data-only", "needs-research"),
                  audit("binary", "needs-research"),
                  audit("reviewed", "reviewed")]
        result = queue(projects, audits)
        self.assertEqual([item["id"] for item in result], ["binary", "data-only"])
        self.assertEqual(result[0]["source_cpu"], [])

    def test_known_cpu_with_unreviewed_audit_is_still_visible(self):
        result = queue([project("known", source_cpu=["6502"])],
                       [audit("known", "unreviewed")])
        self.assertEqual(result[0]["source_cpu"], ["6502"])

    def test_missing_audit_fails_loudly(self):
        with self.assertRaisesRegex(ValueError, "Missing audit"):
            queue([project("orphan")], [])


if __name__ == "__main__":
    unittest.main()
