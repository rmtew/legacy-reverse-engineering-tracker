"""Offline checks for single-authored research and immutable evidence reuse."""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from apply_discovery_batch import FILES, ROOT, apply_batch
from research_record import (AREAS, EvidenceCache, compile_records, git_blob_sha,
                             proof_url, render_report, review_digest, seal_review)


def sample_record() -> dict:
    """Fictional, bounded evidence fixture, never a catalogue addition."""
    url = "https://example.org/research-example"
    narratives = {
        "identity": "The reviewed page identifies a source archive of Example Game.",
        "classification": "The archive preserves original source; no binary-derived reconstruction is claimed.",
        "source_cpu": "The reviewed listing uses Motorola data and address registers.",
        "target_cpu": "No output architecture was established in the reviewed material.",
        "build": "Source files are present; no source build or byte comparison was performed.",
        "runtime_profiles": "No tested runtime or documented minimum hardware was found in the reviewed page.",
        "ai": "No development-AI disclosure was found in the reviewed page; non-use is not established.",
        "relationships": "The page has a predecessor link whose lineage needs inspection.",
    }
    areas = {name: {"state": "reviewed", "narrative": text, "evidence_urls": [url]}
             for name, text in narratives.items()}
    for name in ("target_cpu", "runtime_profiles", "ai"):
        areas[name]["state"] = "no-evidence-found"
    areas["build"]["limitations"] = "No compilation, execution or gameplay test was run."
    areas["relationships"].update(state="needs-research", next_action="Inspect the linked predecessor's author and history.")
    project = {
        "id": "research-format-example", "title": "Example Game", "upstream_name": "Example Game",
        "display_title": "Example Game source archive", "subjects": ["Example Game"], "repo": url,
        "source_platforms": ["Amiga"], "target_platforms": [], "source_cpu": ["m68k"], "target_cpu": [],
        "runtime_profiles": [], "source_language": ["m68k assembly"], "reconstructed_languages": [],
        "record_class": "subject", "target_kinds": ["game"], "work_kinds": ["source-restoration"],
        "tool_kinds": [], "types": ["original-source archive"], "re_started": None,
        "last_activity": None, "last_checked": "2026-10-06", "status": "Source archive; build untested",
        "build": {"compilable": None, "runnable": None, "playable": None, "byte_exact": None},
        "ai": {"usage": None, "tools": []}, "techniques": [], "tags": [],
        "evidence": {"curated": {"unresolved": None, "excerpt": "Unverified claim retained verbatim."}},
    }
    return {"format": "research-records/v1", "date": "2026-10-06", "event_id": "test-research-records",
            "summary": "Review one fictional source archive", "review": {"status": "ready"},
            "records": [{"project": project, "source_ids": ["web-6502disassembly-com"],
                         "overall_state": "partial", "areas": areas}]}


def sample_proof() -> dict:
    text = "A source file's contents are evidence, not a reviewer.\n"
    return {"repository": "https://github.com/example/source", "commit": "a" * 40,
            "path": "docs/source note.txt", "blob": git_blob_sha(text), "text": text}


class ResearchRecordTests(unittest.TestCase):
    def setUp(self):
        self.document = sample_record()
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.cache = EvidenceCache(Path(self.temp.name) / "cache")

    def with_proof(self):
        self.document["proofs"] = {"source": sample_proof()}
        self.document["records"][0]["areas"]["identity"]["evidence_ids"] = ["source"]
        return self.document

    def test_shared_narratives_generate_notes_audits_and_report(self):
        original = copy.deepcopy(self.document)
        batch = compile_records(self.document)
        entry = batch["projects"][0]
        report = render_report(self.document)
        for name in AREAS:
            narrative = original["records"][0]["areas"][name]["narrative"]
            self.assertIn(narrative, entry["project"]["notes"])
            self.assertIn(narrative, entry["audit"]["areas"][name]["note"])
            self.assertIn(narrative, report)
        self.assertEqual(list(entry["audit"]["areas"]), list(AREAS))
        self.assertEqual(entry["audit"]["next_actions"], [original["records"][0]["areas"]["relationships"]["next_action"]])
        self.assertEqual(self.document, original)

    def test_typed_values_unknowns_and_unrecognized_evidence_are_retained(self):
        self.with_proof()["proofs"]["source"]["text"] = "This would be playable and byte exact if finished.\n"
        self.document["proofs"]["source"]["blob"] = git_blob_sha(self.document["proofs"]["source"]["text"])
        project = compile_records(self.document)["projects"][0]["project"]
        authored = self.document["records"][0]["project"]
        self.assertEqual({k: v for k, v in project.items() if k != "notes"}, authored)
        self.assertTrue(all(v is None for v in project["build"].values()))
        self.assertIsNone(project["ai"]["usage"])
        self.assertEqual(project["target_cpu"], [])
        self.assertIn("No compilation, execution or gameplay test was run.", project["notes"])

    def test_compiled_batch_is_accepted_without_changing_catalogue_schema(self):
        data = {name: json.loads((ROOT / "data" / name).read_text()) for name in FILES}
        result = apply_batch(data, compile_records(self.document))
        self.assertEqual(result["projects"], ["research-format-example"])
        self.assertEqual(data["projects.json"][-1]["ai"]["usage"], None)

    def test_reproducible_despite_dictionary_insertion_order(self):
        self.with_proof()
        reordered = dict(reversed(list(self.document.items())))
        reordered["records"] = copy.deepcopy(self.document["records"])
        reordered["records"][0]["areas"] = dict(reversed(list(reordered["records"][0]["areas"].items())))
        self.assertEqual(compile_records(self.document), compile_records(reordered))
        self.assertEqual(render_report(self.document), render_report(reordered))
        self.assertEqual(review_digest(self.document), review_digest(reordered))

    def test_uncertainties_come_before_project_detail(self):
        report = render_report(self.document)
        self.assertLess(report.index("## Uncertainty"), report.index("## Example Game"))
        self.assertIn("AI (no-evidence-found)", report)
        self.assertIn("upstream heads were not checked", report)
        self.document["title"] = "A focused review"
        self.assertTrue(render_report(self.document).startswith("# A focused review\n"))

    def test_review_status_and_stale_digest_are_deliberate_errors(self):
        self.document["review"]["status"] = "draft"
        self.assertIn("Review: draft", render_report(self.document))
        with self.assertRaisesRegex(ValueError, "review is not ready"):
            compile_records(self.document)
        sealed = seal_review(self.document)
        compile_records(sealed)
        sealed["records"][0]["project"]["build"]["runnable"] = True
        with self.assertRaisesRegex(ValueError, "Stale research review digest"):
            compile_records(sealed)

    def test_optional_review_digest_does_not_depend_on_inline_content_location(self):
        self.with_proof()
        compile_records(self.document, evidence_cache=self.cache)
        sealed = seal_review(self.document)
        del sealed["proofs"]["source"]["text"]
        compile_records(sealed, evidence_cache=self.cache)
        self.assertEqual(sealed["review"]["digest"], review_digest(sealed))

    def test_raw_duplicate_notes_and_missing_area_judgments_rejected(self):
        for field in ("state", "narrative"):
            bad = copy.deepcopy(self.document)
            del bad["records"][0]["areas"]["ai"][field]
            with self.assertRaises(ValueError):
                compile_records(bad)
        self.document["records"][0]["project"]["notes"] = "Duplicate narrative"
        with self.assertRaisesRegex(ValueError, "duplicated project.notes"):
            compile_records(self.document)

    def test_unreviewed_cpu_and_missing_next_check_are_rejected(self):
        self.document["records"][0]["areas"]["source_cpu"]["state"] = "unreviewed"
        with self.assertRaisesRegex(ValueError, "explicit CPU audit"):
            compile_records(self.document)
        self.document = sample_record()
        del self.document["records"][0]["areas"]["relationships"]["next_action"]
        with self.assertRaisesRegex(ValueError, "concrete next_action"):
            compile_records(self.document)

    def test_reviewed_areas_need_evidence_unknown_proofs_are_rejected(self):
        area = self.document["records"][0]["areas"]["build"]
        area["evidence_urls"] = []
        with self.assertRaisesRegex(ValueError, "needs evidence"):
            compile_records(self.document)
        area["evidence_ids"] = ["absent"]
        with self.assertRaisesRegex(ValueError, "unknown proof"):
            compile_records(self.document)

    def test_record_and_url_collisions_need_explicit_handling(self):
        second = copy.deepcopy(self.document["records"][0])
        self.document["records"].append(second)
        with self.assertRaisesRegex(ValueError, "Duplicate project ID"):
            compile_records(self.document)
        second["project"]["id"] = "second-project"
        second["project"]["repo"] = second["project"]["repo"].upper() + "/"
        with self.assertRaisesRegex(ValueError, "shares URL"):
            compile_records(self.document)
        second["allow_shared_url"] = True
        self.assertEqual(len(compile_records(self.document)["projects"]), 2)

    def test_immutable_cache_reuses_only_exact_proof_identity(self):
        self.with_proof()
        first = compile_records(self.document, evidence_cache=self.cache)
        proof = self.document["proofs"]["source"]
        cached = self.cache.path_for(proof)
        before = cached.read_bytes()
        del proof["text"]
        self.assertEqual(first, compile_records(self.document, evidence_cache=self.cache))
        self.assertEqual(before, cached.read_bytes())
        for field, value in (("commit", "b" * 40), ("path", "other.txt"),
                             ("blob", "c" * 40), ("repository", "https://github.com/example/other")):
            bad = copy.deepcopy(self.document)
            bad["proofs"]["source"][field] = value
            with self.subTest(field=field), self.assertRaisesRegex(ValueError, "Missing pinned proof"):
                compile_records(bad, evidence_cache=self.cache)

    def test_expected_heads_reject_stale_snapshot_even_if_cached(self):
        self.with_proof()
        compile_records(self.document, evidence_cache=self.cache)
        heads = {"https://github.com/EXAMPLE/source/": "a" * 40}
        report = render_report(self.document, expected_commits=heads)
        self.assertIn("match the supplied expected commits", report)
        with self.assertRaisesRegex(ValueError, "Stale proof commit"):
            compile_records(self.document, evidence_cache=self.cache,
                            expected_commits={"https://github.com/example/source": "b" * 40})
        with self.assertRaisesRegex(ValueError, "No expected commit"):
            compile_records(self.document, expected_commits={})

    def test_blob_integrity_pinned_urls_and_cache_tampering(self):
        self.with_proof()
        proof = self.document["proofs"]["source"]
        self.assertIn("/blob/" + "a" * 40 + "/docs/source%20note.txt", proof_url(proof))
        compile_records(self.document, evidence_cache=self.cache)
        path = self.cache.path_for(proof)
        cache_data = json.loads(path.read_text())
        cache_data["text"] = "Changed behind the cache key"
        path.write_text(json.dumps(cache_data))
        del proof["text"]
        with self.assertRaisesRegex(ValueError, "Mismatched proof cache blob"):
            compile_records(self.document, evidence_cache=self.cache)
        proof["text"] = "The input changed too"
        with self.assertRaisesRegex(ValueError, "Mismatched proof text/blob"):
            compile_records(self.document, evidence_cache=self.cache)

    def test_cache_identity_and_conflicting_location_rejected(self):
        self.with_proof()
        proof = self.document["proofs"]["source"]
        compile_records(self.document, evidence_cache=self.cache)
        path = self.cache.path_for(proof)
        entry = json.loads(path.read_text())
        entry["identity"]["path"] = "wrong.txt"
        path.write_text(json.dumps(entry))
        with self.assertRaisesRegex(ValueError, "Mismatched proof cache identity"):
            self.cache.get(proof)
        conflicting = copy.deepcopy(proof)
        conflicting["text"] = "Another blob at the same supposedly immutable location"
        conflicting["blob"] = git_blob_sha(conflicting["text"])
        self.document["proofs"]["conflict"] = conflicting
        with self.assertRaisesRegex(ValueError, "Conflicting blobs"):
            compile_records(self.document)

    def test_unpinned_proofs_and_escaping_paths_are_rejected(self):
        self.with_proof()
        for field, value in (("commit", "main"), ("blob", "1234"), ("path", "../README.md"),
                             ("path", "/README.md"), ("path", "docs/./README.md")):
            bad = copy.deepcopy(self.document)
            bad["proofs"]["source"][field] = value
            with self.subTest(field=field, value=value), self.assertRaises(ValueError):
                compile_records(bad)

    def test_pinned_blob_content_does_not_inflate_compiled_payload_or_report(self):
        self.with_proof()
        batch = compile_records(self.document)
        self.assertNotIn("proofs", batch)
        self.assertNotIn(sample_proof()["text"], json.dumps(batch))
        self.assertNotIn(sample_proof()["text"], render_report(self.document))

    def test_partial_project_update_preserves_omitted_fields(self):
        record = self.document["records"][0]
        record["update"] = {"project_id": record["project"]["id"], "expected_sha256": "a" * 64}
        record["project"] = {"ai": {"usage": None, "tools": []}}
        del record["source_ids"]
        batch = compile_records(self.document)
        self.assertEqual(batch["projects"], [])
        update = batch["project_updates"][0]
        self.assertEqual(set(update["changes"]), {"ai", "notes"})
        self.assertEqual(update["expected_sha256"], "a" * 64)
        self.assertNotIn("source_ids", update)
        report = render_report(self.document)
        self.assertIn("Typed catalogue changes", report)
        self.assertIn("Expected existing project SHA256: " + "a" * 64, report)

    def test_compiled_update_applies_to_exact_snapshot_and_rejects_stale_baseline(self):
        data = {name: json.loads((ROOT / "data" / name).read_text()) for name in FILES}
        project = next(p for p in data["projects.json"] if p["id"] == "abm-apple2-6502disassembly")
        before = copy.deepcopy(project)
        digest = hashlib.sha256(json.dumps(project, sort_keys=True, separators=(",", ":"),
                                          ensure_ascii=False).encode()).hexdigest()
        record = self.document["records"][0]
        record["update"] = {"project_id": project["id"], "expected_sha256": digest}
        record["project"] = {"status": "Fictional update in an isolated test"}
        batch = compile_records(self.document)
        stale_data = copy.deepcopy(data)
        stale_data["projects.json"][data["projects.json"].index(project)]["status"] = "Concurrent edit"
        with self.assertRaisesRegex(ValueError, "Stale project update"):
            apply_batch(stale_data, batch)
        result = apply_batch(data, batch)
        self.assertEqual(result["updated_projects"], [project["id"]])
        self.assertEqual(project["build"], before["build"])
        self.assertEqual(project["repo"], before["repo"])
        self.assertEqual(project["status"], "Fictional update in an isolated test")

    def test_cli_explicit_reseal_after_edit(self):
        root = Path(self.temp.name)
        source, sealed = root / "record.json", root / "ready.json"
        document = seal_review(self.document)
        document["summary"] = "An explicitly re-reviewed edit"
        source.write_text(json.dumps(document))
        result = subprocess.run([sys.executable, str(ROOT / "tools/research_record.py"), str(source),
                                 "--seal", str(sealed)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        changed = json.loads(sealed.read_text())
        self.assertEqual(changed["review"]["digest"], review_digest(changed))
        compile_records(changed)

    def test_legacy_nonproject_entries_passthrough(self):
        self.document["records"] = []
        self.document["decisions"] = [{"id": "fictional", "decision": "deferred", "reason": "Inspect provenance."}]
        self.assertEqual(compile_records(self.document)["decisions"], self.document["decisions"])
        self.assertIn("Inspect provenance.", render_report(self.document))

    def test_cli_seal_then_compile(self):
        root = Path(self.temp.name)
        source, sealed, output, report = [root / n for n in ("record.json", "ready.json", "batch.json", "report.md")]
        self.document["review"]["status"] = "draft"
        source.write_text(json.dumps(self.document))
        result = subprocess.run([sys.executable, str(ROOT / "tools/research_record.py"), str(source),
                                 "--seal", str(sealed), "--output", str(output), "--report", str(report)],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(sealed.read_text())["review"]["status"], "ready")
        self.assertEqual(json.loads(output.read_text())["projects"][0]["project"]["id"], "research-format-example")
        self.assertTrue(report.read_text().startswith("# Review one fictional source archive"))


if __name__ == "__main__":
    unittest.main()
