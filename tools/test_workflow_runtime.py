"""Regression for runner-only values being initialized after job admission."""
import os
from pathlib import Path
import re
import subprocess
import tempfile
import unittest


class WorkflowRuntimeTests(unittest.TestCase):
    def test_scope_path_initializes_at_runtime_outside_checkout(self):
        root = Path(__file__).resolve().parents[1]
        workflow = (root / ".github/workflows/refresh-github.yml").read_text()
        job_env = workflow.split("    env:", 1)[1].split("    steps:", 1)[0]
        # GitHub does not expose runner at jobs.<job_id>.env. YAML parsing alone
        # accepts the invalid expression, but Actions rejects the entire job.
        self.assertNotRegex(job_env, r"\$\{\{[^}]*\brunner\.")
        match = re.search(r"name: Initialize refresh scope path\n\s+shell: bash\n\s+run: (.+)", workflow)
        self.assertIsNotNone(match)
        self.assertLess(match.start(), workflow.index("uses: actions/checkout"))
        with tempfile.TemporaryDirectory() as temp:
            temp = Path(temp)
            runner = temp / "runner temporary"
            runner.mkdir()
            checkout = temp / "checkout"
            checkout.mkdir()
            env_file = temp / "job environment"
            subprocess.run(["bash", "-eu", "-c", match[1]], cwd=checkout, check=True,
                           env={**os.environ, "RUNNER_TEMP": str(runner), "GITHUB_ENV": str(env_file)})
            self.assertEqual(env_file.read_text(), f"GITHUB_REFRESH_SCOPE_FILE={runner}/github-refresh-scope.json\n")
            scope = Path(env_file.read_text().strip().split("=", 1)[1])
            scope.write_text('{"mode":"publication"}')
            checkout.rmdir()  # Checkout reset/replacement cannot erase the scope.
            self.assertTrue(scope.is_file())


class StorageWorkflowTests(unittest.TestCase):
    def test_partition_paths_trigger_refresh_and_pages_and_are_staged(self):
        root=Path(__file__).resolve().parents[1]
        refresh=(root/'.github/workflows/refresh-github.yml').read_text()
        pages=(root/'.github/workflows/pages.yml').read_text()
        enrich=(root/'.github/workflows/enrich-evidence.yml').read_text()
        for workflow in (refresh,pages):
            self.assertIn('"data/projects.index.json"',workflow)
            self.assertIn('"data/projects/**"',workflow)
            self.assertIn('"tools/catalogue_storage.py"',workflow)
        self.assertIn('"data/project-audits/**"',pages)
        for workflow in (refresh,enrich):
            for line in workflow.splitlines():
                if 'git add ' in line:
                    self.assertIn('data/projects.index.json data/projects/',line)
                    self.assertNotIn('data/projects.json',line)
        self.assertIn('data/project-audits.index.json data/project-audits/',refresh)
        self.assertIn('load_git_projects',pages)
        self.assertIn('load_git_dataset',pages)
        # Exercise the exact push gate pattern against both layouts and research.
        pattern=re.search("grep -Eq '([^']+)'",pages)[1]
        for name in ['data/projects.json','data/projects.index.json','data/projects/a.json']:
            self.assertEqual(subprocess.run(['grep','-Eq',pattern],input=name,text=True).returncode,0)
        for name in ['data/project-audits/a.json','data/discovery-sources.json']:
            self.assertEqual(subprocess.run(['grep','-Eq',pattern],input=name,text=True).returncode,1)


if __name__ == "__main__":
    unittest.main()
