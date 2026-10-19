"""Regression for runner-only values being initialized after job admission."""

from pathlib import Path
import unittest


class WorkflowRuntimeTests(unittest.TestCase):
    def test_runtime_bundle_survives_checkout_reset(self):
        workflow = (Path(__file__).resolve().parents[1] / ".github/workflows/refresh-github.yml").read_text()
        job_env = workflow.split("    env:", 1)[1].split("    steps:", 1)[0]
        self.assertNotRegex(job_env, r"\$\{\{[^}]*\brunner\.")
        self.assertIn('--bundle "$RUNNER_TEMP/refresh-bundle.json"', workflow)
        self.assertLess(
            workflow.index("name: Preserve collected results"), workflow.index("name: Publish results")
        )
        retry = workflow.split("git reset --hard origin/main", 1)[1].split("  continue:", 1)[0]
        self.assertIn("refresh_pipeline.py apply", retry)
        self.assertNotIn("refresh_pipeline.py collect", retry)
        self.assertNotIn("refresh_github.py", retry)
        self.assertIn("actions: write", workflow)
        self.assertIn("gh workflow run refresh-github.yml", workflow)
        self.assertIn("recovery_attempt", workflow)
        self.assertIn("needs.refresh.result == 'success' || needs.refresh.result == 'failure'", workflow)

    def test_pages_serializes_admission_deployment_and_latest_main_reconciliation(self):
        root = Path(__file__).resolve().parents[1]
        workflow = (root / ".github/workflows/pages.yml").read_text()
        self.assertNotIn("workflow_run:", workflow)
        self.assertIn("group: github-pages", workflow.split("jobs:", 1)[0])
        self.assertIn("cancel-in-progress: false", workflow.split("jobs:", 1)[0])
        self.assertNotIn("cancel-in-progress: true", workflow)
        gate = workflow.split("  gate:", 1)[1].split("  deploy:", 1)[0]
        self.assertNotIn("environment:", gate)  # No false successful-deploy receipt.
        self.assertIn("ref: ${{ needs.gate.outputs.snapshot }}", workflow)
        self.assertIn("pages_publication.py verify", workflow)
        self.assertIn("needs: [gate, deploy]", workflow)
        self.assertIn("always() && !cancelled()", workflow)
        self.assertIn("pages_publication.py request --attempt", workflow)
        self.assertIn("schedule:", workflow)
        for control in (
            "tools/test_",
            "tools/validate_site_data.py",
            "tools/apply_discovery_batch.py",
            ".github/workflows/pages.yml",
        ):
            self.assertNotIn('"' + control, workflow)
        for name in ("refresh-github.yml", "enrich-evidence.yml"):
            collector = (root / ".github/workflows" / name).read_text()
            notification = collector.split("name: Request publication of new complete public content", 1)[
                1
            ].split("  continue:", 1)[0]
            self.assertIn("continue-on-error: true", notification)
            self.assertIn("always() && !cancelled()", notification)
            self.assertIn("pages_publication.py request", notification)
            self.assertIn("deployments: read", collector)
            self.assertIn("actions: write", collector)


class StorageWorkflowTests(unittest.TestCase):
    def test_partition_paths_trigger_refresh_and_pages_and_are_staged(self):
        root = Path(__file__).resolve().parents[1]
        refresh = (root / ".github/workflows/refresh-github.yml").read_text()
        pages = (root / ".github/workflows/pages.yml").read_text()
        enrich = (root / ".github/workflows/enrich-evidence.yml").read_text()
        for workflow in (refresh, pages):
            self.assertIn('"data/projects.index.json"', workflow)
            self.assertIn('"data/projects/**"', workflow)
            self.assertIn('"tools/catalogue_storage.py"', workflow)
        self.assertIn('"data/project-audits/**"', pages)
        for workflow in (refresh, enrich):
            for line in workflow.splitlines():
                if "git add " in line:
                    self.assertIn("data/projects.index.json data/projects/", line)
                    self.assertNotIn("data/projects.json", line)
        self.assertIn("data/project-audits.index.json data/project-audits/", refresh)
        gate = (root / "tools/pages_publication.py").read_text()
        self.assertIn("load_git_projects", gate)
        self.assertIn("load_git_dataset", gate)


if __name__ == "__main__":
    unittest.main()
