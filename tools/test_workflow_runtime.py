"""Regression for runner-only values being initialized after job admission."""
import os
from pathlib import Path
import re
import subprocess
import tempfile
import unittest


class WorkflowRuntimeTests(unittest.TestCase):
    def test_runtime_bundle_survives_checkout_reset(self):
        workflow = (Path(__file__).resolve().parents[1] / '.github/workflows/refresh-github.yml').read_text()
        job_env = workflow.split('    env:', 1)[1].split('    steps:', 1)[0]
        self.assertNotRegex(job_env, r"\$\{\{[^}]*\brunner\.")
        self.assertIn('--bundle "$RUNNER_TEMP/refresh-bundle.json"', workflow)
        self.assertLess(workflow.index('name: Preserve collected results'), workflow.index('name: Publish results'))
        retry = workflow.split('git reset --hard origin/main', 1)[1].split('  continue:', 1)[0]
        self.assertIn('refresh_pipeline.py apply', retry)
        self.assertNotIn('refresh_pipeline.py collect', retry)
        self.assertNotIn('refresh_github.py', retry)
        self.assertIn('actions: write', workflow)
        self.assertIn('gh workflow run refresh-github.yml', workflow)
        self.assertIn('recovery_attempt', workflow)
        self.assertIn("needs.refresh.result == 'success' || needs.refresh.result == 'failure'", workflow)

    def test_pages_checks_publication_before_any_workflow_run_shortcut(self):
        workflow = (Path(__file__).resolve().parents[1] / '.github/workflows/pages.yml').read_text()
        gate = workflow.split('if [ "$GITHUB_EVENT_NAME" = "workflow_run" ]; then', 1)[1]
        self.assertLess(gate.index('refresh_scope.py --check-publishable'), gate.index('echo "deploy=true"'))


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
