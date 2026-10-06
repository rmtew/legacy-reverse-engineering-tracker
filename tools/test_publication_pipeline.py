"""Repeatable preparation, optimistic updates and exact publication proofs."""
import copy
import json
from pathlib import Path
import shutil
import unittest
from unittest.mock import patch

from apply_discovery_batch import FILES, run
from publication_pipeline import blob_sha, digest, prepare, verify_files, verify_live, verify_remote
from test_discovery_batch import DiscoveryBatchTests


class PublicationPipelineTests(DiscoveryBatchTests):
    def setUp(self):
        super().setUp()
        for name in ("sources.md", "log.md"):
            (self.root / name).write_text("# Existing research\n")
        self.tree = {"tree": [{"path": str(path.relative_to(self.root)), "type": "blob", "sha": blob_sha(path.read_bytes())}
                              for path in self.root.rglob("*") if path.is_file()]}
        self.out = self.root.parent / (self.root.name + "-bundle")
        self.addCleanup(lambda: shutil.rmtree(self.out, ignore_errors=True))

    def prepare(self):
        return prepare(self.batch(), self.root, self.out, "a" * 40, self.tree)

    def test_prepare_is_isolated_and_idempotent(self):
        first = self.prepare()
        self.assertEqual(first, self.prepare())
        self.assertTrue(all((self.data / name).read_bytes() == value for name, value in self.before.items()))
        verify_files(self.out / "payload", first)
        review = json.loads((self.out / "review.json").read_text())
        self.assertEqual(review["added_ids"], ["sample-research-test"])
        self.assertEqual(review["updated_ids"], [])
        self.assertTrue((self.out / "payload/docs/research" / (self.batch()["event_id"] + ".md")).is_file())

    def test_changed_payload_cannot_be_reused(self):
        self.prepare()
        (self.out / "payload/data/projects.json").write_text("[]\n")
        with self.assertRaisesRegex(ValueError, "changed after preparation"):
            self.prepare()

    def test_changed_input_requires_new_bundle(self):
        self.prepare()
        batch = self.batch()
        batch["summary"] = "Different reviewed delta"
        with self.assertRaisesRegex(ValueError, "different input"):
            prepare(batch, self.root, self.out, "a" * 40, self.tree)

    def test_stale_baseline_refuses_before_output(self):
        (self.root / "log.md").write_text("new main")
        with self.assertRaisesRegex(ValueError, "Baseline file"):
            self.prepare()
        self.assertFalse(self.out.exists())

    def test_remote_tree_must_match_every_authored_file(self):
        manifest = self.prepare()
        tree = {"tree": [{"path": x["path"], "type": "blob", "sha": x["sha"]} for x in manifest["files"]]}
        self.assertEqual(verify_remote(manifest, tree)["authored_files_verified"], len(manifest["files"]))
        tree["tree"][0]["sha"] = "0" * 40
        with self.assertRaisesRegex(ValueError, "Remote publication mismatch"):
            verify_remote(manifest, tree)

    def test_source_only_publication_rejects_old_self_consistent_deployment(self):
        batch = self.batch()
        batch["projects"] = []
        batch["decisions"] = []
        batch["source_updates"] = [{"id": self.source_id, "reason": "Explicit reviewed source correction."}]
        prepare(batch, self.root, self.out, "a" * 40, self.tree)
        live = self.root / "served"
        shutil.copytree(self.data, live / "data")
        (live / "activity.xml").write_text("<rss/>")
        with patch("publication_pipeline.validate"):
            with self.assertRaisesRegex(ValueError, "Published research record missing or changed"):
                verify_live(self.out, live, self.tree)

    def test_restored_project_events_are_valid_publication_results(self):
        self.out.mkdir()
        shutil.copytree(self.data, self.out / "payload/data")
        projects = json.loads(self.before["projects.json"])
        project = next(p for p in projects if "github.com/" not in (p.get("repo") or ""))
        pid = project["id"]
        (self.out / "manifest.json").write_text(json.dumps({"summary": {"projects": [pid]}}))
        live = self.root / "served"
        shutil.copytree(self.data, live / "data")
        event = {"project_id": pid, "type": "project_restored", "date": "2026-10-06T12:00:00Z"}
        (live / "data/activity.json").write_text(json.dumps({"events": [event]}))
        for days in (30, 180):
            (live / f"data/activity-{days}d.json").write_text(json.dumps({"events": [event]}))
        (live / "activity.xml").write_text(f"<rss><channel><item><guid>legacy-re:{pid}:project_restored:2026-10-06</guid></item></channel></rss>")
        tree = {"tree": [{"path": str(p.relative_to(live)), "type": "blob", "sha": blob_sha(p.read_bytes())}
                          for p in (live / "data").glob("*.json")]}
        with patch("publication_pipeline.validate"):
            result = verify_live(self.out, live, tree)
        self.assertEqual(result["initial_context_activity_windows_rss_verified"], 1)

    def update_batch(self):
        batch = self.batch()
        original = json.loads(self.before["projects.json"])[0]
        audit = next(a for a in json.loads(self.before["project-audits.json"])["projects"] if a["project_id"] == original["id"])
        audit["last_reviewed"] = batch["date"]
        for area in ("source_cpu", "target_cpu"):
            audit["areas"][area]["state"] = "reviewed"
        batch["projects"] = []
        batch["decisions"] = []
        batch["project_updates"] = [{"project_id": original["id"], "expected_sha256": digest(original),
                                     "changes": {"notes": original.get("notes", "") + " Reviewed detail."}, "audit": audit}]
        return batch, original

    def test_update_preserves_all_omitted_fields(self):
        batch, original = self.update_batch()
        run(self.root, batch, True)
        updated = next(p for p in json.loads((self.data / "projects.json").read_text()) if p["id"] == original["id"])
        self.assertEqual({k: v for k, v in original.items() if k != "notes"}, {k: v for k, v in updated.items() if k != "notes"})
        with self.assertRaisesRegex(ValueError, "Stale project update"):
            run(self.root, batch, True)

    def test_stale_update_writes_nothing(self):
        batch, _ = self.update_batch()
        batch["project_updates"][0]["expected_sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "Stale project update"):
            run(self.root, batch, True)
        self.assertTrue(all((self.data / name).read_bytes() == value for name, value in self.before.items()))

    def test_duplicate_update_rejected_without_writes(self):
        batch, _ = self.update_batch()
        batch["project_updates"].append(copy.deepcopy(batch["project_updates"][0]))
        with self.assertRaisesRegex(ValueError, "Duplicate or unknown"):
            run(self.root, batch, True)
        self.assertTrue(all((self.data / name).read_bytes() == value for name, value in self.before.items()))


if __name__ == "__main__":
    unittest.main()
