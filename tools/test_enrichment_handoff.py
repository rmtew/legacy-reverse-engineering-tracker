"""Durable evidence handoff: no re-collection for dependency waits or Git races."""
import copy
from contextlib import redirect_stdout
import hashlib
from io import BytesIO, StringIO
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch
import zipfile

import enrichment_handoff as handoff
import enrichment_pipeline as pipeline
from catalogue_storage import encode, load_projects, write_all, write_projects
from collection_budget import Budget
from merge_pending_projects import new_audit
from record_project_activity import snapshot
from test_enrichment_pipeline import Network, NOW


class Artifacts:
    def __init__(self, bundle):
        self.payload = encode(bundle)
        self.bundle = bundle
        self.artifact = {'id': 100, 'workflow_run': {'id': 77}}
        self.downloads = 0
        self.wakeups = 0

    def pending(self, after):
        return [self.artifact] if after < 100 else []

    def request(self):
        self.wakeups += 1

    def download(self, artifact):
        self.downloads += 1
        return self.payload, copy.deepcopy(self.bundle)


class HandoffTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'repo'; self.root.mkdir()
        self.git('init', '--initial-branch=main')
        self.git('config', 'user.name', 'Test'); self.git('config', 'user.email', 'test@example.org')
        self.project = {'id': 'a', 'title': 'Example', 'upstream_name': 'Example', 'display_title': 'Example',
                        'subjects': ['Example'], 'repo': 'https://github.com/owner/a', 'record_class': 'subject',
                        'target_kinds': ['game'], 'work_kinds': [], 'tool_kinds': [], 'notes': 'Curated',
                        'build': {'compilable': None, 'playable': None, 'runnable': None, 'byte_exact': None}}
        write_all(self.root / 'data', {'projects.json': [self.project],
            'project-audits.json': {'projects': [new_audit('a')]},
            'discovery-sources.json': {'sources': [], 'backlog': []},
            'discovery-decisions.json': {'indexed_at': '2026-10-19', 'decisions': []},
            'research-activity.json': {'events': []}})
        self.put('data/activity.json', {'generated_at': '2026-10-19T00:00:00Z', 'window_days': 30, 'events': []})
        self.put('state/project-catalog-state.json', {'projects': {'a': snapshot(self.project)}})
        self.put('state/github-poll-state.json', {'repositories': {}})
        self.commit()
        self.origin = Path(self.temp.name) / 'origin.git'
        subprocess.run(['git', 'clone', '--bare', str(self.root), str(self.origin)], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        self.git('remote', 'add', 'origin', str(self.origin)); self.git('fetch', 'origin')
        self.network = Network()
        client = pipeline.Client(Budget(clock=self.network.clock), opener=self.network.open, token='')
        self.quiet = redirect_stdout(StringIO()); self.quiet.__enter__(); self.addCleanup(self.quiet.__exit__, None, None, None)
        bundle = pipeline.collect(self.root, Path(self.temp.name) / 'bundle.json', client.budget,
                                  now=NOW, client=client, ci_limit=0, docs_limit=1)
        self.artifacts = Artifacts(bundle)
        self.requests = len(self.network.calls)

    def git(self, *args):
        return subprocess.check_output(['git', *args], cwd=self.root, stderr=subprocess.DEVNULL).decode().strip()

    def put(self, path, value):
        target = self.root / path; target.parent.mkdir(parents=True, exist_ok=True); target.write_bytes(encode(value))

    def commit(self):
        self.git('add', '-A'); self.git('commit', '-qm', 'Snapshot')
        return self.git('rev-parse', 'HEAD')

    def push(self):
        self.commit(); self.git('push', 'origin', 'main')

    def test_metadata_wait_retains_artifact_then_replays_once_without_collection(self):
        record = load_projects(self.root / 'data/projects.json')[0]
        record['notes'] = 'New catalogue material awaiting metadata'
        write_projects(self.root / 'data/projects.json', [record]); self.push()
        before = self.git('rev-parse', 'HEAD')
        waiting = handoff.publish(self.root, self.artifacts)
        self.assertTrue(waiting['waiting_metadata']); self.assertFalse(waiting['published'])
        self.assertEqual(self.git('rev-parse', 'HEAD'), before)
        self.assertEqual(handoff.checkpoint(self.root)['artifact_id'], 0)
        self.assertIsNone(load_projects(self.root / 'data/projects.json')[0]['build']['playable'])
        # The metadata prerequisite records the current catalogue, then wakes publication.
        self.put('state/project-catalog-state.json', {'projects': {'a': snapshot(record)}}); self.push()
        result = handoff.publish(self.root, self.artifacts)
        self.assertTrue(result['published']); self.assertFalse(result['waiting_metadata'])
        after = load_projects(self.root / 'data/projects.json')[0]
        self.assertTrue(after['build']['playable']); self.assertEqual(after['notes'], record['notes'])
        checkpoint = handoff.checkpoint(self.root)
        self.assertEqual(checkpoint['artifact_id'], 100)
        self.assertEqual(checkpoint['bundle_sha256'], hashlib.sha256(self.artifacts.payload).hexdigest())
        head = self.git('rev-parse', 'HEAD')
        self.assertFalse(handoff.publish(self.root, self.artifacts)['published'])
        self.assertEqual(self.git('rev-parse', 'HEAD'), head)
        self.assertEqual(self.artifacts.downloads, 2)  # One per wake-up, none after acknowledgement.
        self.assertEqual(len(self.network.calls), self.requests)

    def test_metadata_request_wakes_pending_replay_without_collection_or_acknowledgement(self):
        head = self.git('rev-parse', 'HEAD')
        result = handoff.request(self.root, self.artifacts)
        self.assertTrue(result['requested']); self.assertEqual(self.artifacts.wakeups, 1)
        self.assertEqual(self.artifacts.downloads, 0)
        self.assertEqual(handoff.checkpoint(self.root)['artifact_id'], 0)
        self.assertEqual(self.git('rev-parse', 'HEAD'), head)
        self.assertEqual(len(self.network.calls), self.requests)
        handoff.publish(self.root, self.artifacts)
        self.assertFalse(handoff.request(self.root, self.artifacts)['requested'])
        self.assertEqual(self.artifacts.wakeups, 1)

    def test_failed_explicit_dispatch_retains_pending_artifact_and_checkpoint(self):
        head = self.git('rev-parse', 'HEAD')
        with patch.object(self.artifacts, 'request', side_effect=subprocess.CalledProcessError(1, ['gh'])):
            with self.assertRaises(subprocess.CalledProcessError):
                handoff.request(self.root, self.artifacts)
        self.assertEqual(handoff.checkpoint(self.root)['artifact_id'], 0)
        self.assertEqual(self.git('rev-parse', 'HEAD'), head)
        self.assertEqual(len(self.artifacts.pending(0)), 1)
        self.assertEqual(self.artifacts.downloads, 0)

    def test_individual_stale_evidence_is_acknowledged_without_overwriting_curated_values(self):
        record = load_projects(self.root / 'data/projects.json')[0]
        record['build']['playable'] = False
        write_projects(self.root / 'data/projects.json', [record]); self.push()
        result = handoff.publish(self.root, self.artifacts)
        self.assertTrue(result['published'])
        self.assertIs(load_projects(self.root / 'data/projects.json')[0]['build']['playable'], False)
        self.assertEqual(handoff.checkpoint(self.root)['conflicts'], 1)
        self.assertNotIn('a', pipeline.state_read(self.root)['records'])
        self.assertEqual(len(self.network.calls), self.requests)

    def test_fast_forward_race_reuses_download_and_preserves_concurrent_metadata(self):
        real_git = handoff.git; raced = False
        def command(root, *args, **kwargs):
            nonlocal raced
            if args[:2] == ('push', 'origin') and not raced:
                raced = True
                other = Path(self.temp.name) / 'other'
                subprocess.run(['git', 'clone', str(self.origin), str(other)], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                subprocess.run(['git', 'config', 'user.name', 'Concurrent'], cwd=other, check=True)
                subprocess.run(['git', 'config', 'user.email', 'concurrent@example.org'], cwd=other, check=True)
                records = load_projects(other / 'data/projects.json'); records[0]['github'] = {'stars': 99}
                write_projects(other / 'data/projects.json', records)
                subprocess.run(['git', 'add', 'data'], cwd=other, check=True)
                subprocess.run(['git', 'commit', '-qm', 'Concurrent metadata'], cwd=other, check=True)
                subprocess.run(['git', 'push', 'origin', 'main'], cwd=other, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return real_git(root, *args, **kwargs)
        with patch.object(handoff, 'git', side_effect=command):
            result = handoff.publish(self.root, self.artifacts)
        self.assertTrue(result['published'])
        self.assertEqual(load_projects(self.root / 'data/projects.json')[0]['github']['stars'], 99)
        self.assertEqual(self.artifacts.downloads, 1)
        self.assertEqual(len(self.network.calls), self.requests)

    def test_lost_push_response_resolves_checkpoint_without_duplicate_commit(self):
        real_git = handoff.git; pushes = 0
        def command(root, *args, **kwargs):
            nonlocal pushes
            result = real_git(root, *args, **kwargs)
            if args[:2] == ('push', 'origin'):
                pushes += 1
                return subprocess.CompletedProcess(args, 1, result.stdout, b'Lost response')
            return result
        with patch.object(handoff, 'git', side_effect=command):
            result = handoff.publish(self.root, self.artifacts)
        self.assertTrue(result['published']); self.assertEqual(pushes, 1)
        self.assertEqual(handoff.checkpoint(self.root)['artifact_id'], 100)
        self.assertEqual(self.artifacts.downloads, 1)

    def test_exhausted_push_races_leave_artifact_available_for_later_replay(self):
        real_git = handoff.git
        def command(root, *args, **kwargs):
            if args[:2] == ('push', 'origin'):
                return subprocess.CompletedProcess(args, 1, b'', b'Race')
            return real_git(root, *args, **kwargs)
        with patch.object(handoff, 'git', side_effect=command):
            with self.assertRaisesRegex(RuntimeError, 'three fast-forward'):
                handoff.publish(self.root, self.artifacts)
        handoff.sync(self.root)
        self.assertEqual(handoff.checkpoint(self.root)['artifact_id'], 0)
        self.assertTrue(handoff.publish(self.root, self.artifacts)['published'])
        self.assertEqual(len(self.network.calls), self.requests)


class ArtifactBoundaryTests(unittest.TestCase):
    def artifact(self, identity=10, **changes):
        return {'id': identity, 'name': handoff.ARTIFACT, 'expired': False, 'size_in_bytes': 100,
                'workflow_run': {'id': identity}, **changes}

    def source_run(self, **changes):
        return {'path': handoff.SOURCE, 'repository': {'full_name': 'owner/repo'},
                'head_repository': {'full_name': 'owner/repo'}, 'head_branch': 'main', 'event': 'push', **changes}

    def client(self, artifacts, run=None):
        client = handoff.GitHub('owner/repo')
        client.get = lambda path: {'artifacts': artifacts} if path.startswith('actions/artifacts?') else (run or self.source_run())
        return client

    def test_origin_filters_pr_fork_branch_and_other_workflows(self):
        for change in ({'event': 'pull_request'}, {'head_branch': 'feature'}, {'head_repository': {'full_name': 'fork/repo'}}, {'path': '.github/workflows/other.yml'}):
            self.assertEqual(self.client([self.artifact()], self.source_run(**change)).pending(0), [])
        self.assertEqual(len(self.client([self.artifact()]).pending(0)), 1)
        self.assertEqual(self.client([self.artifact()]).pending(10), [])

    def test_expired_pending_artifact_blocks_collection_without_silent_discard(self):
        with self.assertRaisesRegex(ValueError, 'expired'):
            self.client([self.artifact(expired=True)]).pending(0)

    def test_artifact_listing_is_bounded_and_rejects_unexpected_order(self):
        with self.assertRaisesRegex(ValueError, 'order'):
            self.client([self.artifact(9), self.artifact(10)]).pending(0)
        client = self.client([])
        client.get = lambda path: {'artifacts': [self.artifact(10000-int(path.rsplit('=',1)[1])*100-n) for n in range(100)]} if path.startswith('actions/artifacts?') else self.source_run()
        with self.assertRaisesRegex(ValueError, 'source inspection ceiling'):
            client.pending(0)

    def zip(self, name='enrichment-bundle.json', extra=False):
        output = BytesIO()
        with zipfile.ZipFile(output, 'w') as archive:
            archive.writestr(name, encode({'version': 1, 'results': []}))
            if extra: archive.writestr('tool.py', 'raise RuntimeError()')
        return output.getvalue()

    def test_archive_is_only_bounded_json_data_never_extracted_code_or_paths(self):
        self.assertEqual(handoff.unpack(self.zip())[1], {'version': 1, 'results': []})
        for raw in (self.zip('../enrichment-bundle.json'), self.zip(extra=True), self.zip('/tmp/enrichment-bundle.json')):
            with self.assertRaises(ValueError): handoff.unpack(raw)

    def test_archive_size_and_digest_bounds_fail_before_replay(self):
        raw = self.zip()
        with patch.object(handoff, 'MAX_ZIP', len(raw) - 1):
            with self.assertRaisesRegex(ValueError, 'Oversized'):
                handoff.unpack(raw)
        with patch.object(handoff, 'MAX_BUNDLE', 1):
            with self.assertRaisesRegex(ValueError, 'bounded JSON'):
                handoff.unpack(raw)
        client = handoff.GitHub('owner/repo')
        result = subprocess.CompletedProcess([], 0, raw, b'')
        with patch.object(handoff.subprocess, 'run', return_value=result):
            with self.assertRaisesRegex(ValueError, 'digest mismatch'):
                client.download(self.artifact(digest='sha256:' + '0' * 64))

    def test_explicit_request_is_one_fixed_trusted_main_dispatch(self):
        client = handoff.GitHub('owner/repo')
        with patch.object(handoff.subprocess, 'run') as run:
            client.request()
        run.assert_called_once_with(
            ['gh', 'workflow', 'run', 'publish-enrichment.yml', '--ref', 'main', '--repo', 'owner/repo'],
            check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=30)

    def test_metadata_finalizer_explicitly_wakes_retained_replay_without_recollecting(self):
        root = Path(__file__).resolve().parents[1]
        workflow = (root / '.github/workflows/refresh-github.yml').read_text()
        finalizer = workflow.split('name: Resume retained evidence after metadata publication', 1)[1].split('  continue:', 1)[0]
        self.assertIn('always() && !cancelled()', finalizer)
        self.assertIn('continue-on-error: true', finalizer)
        self.assertIn('enrichment_handoff.py request', finalizer)
        self.assertNotIn(' collect', finalizer)
        self.assertNotIn('sleep ', finalizer)
        self.assertIn('actions: write', workflow)

    def test_workflow_graph_has_no_self_trigger_or_wait_loop(self):
        root = Path(__file__).resolve().parents[1]
        collector = (root / '.github/workflows/enrich-evidence.yml').read_text()
        publisher = (root / '.github/workflows/publish-enrichment.yml').read_text()
        self.assertNotIn('sleep ', collector + publisher)
        self.assertNotIn('contents: write', collector)
        self.assertIn('retention-days: 90', collector)
        self.assertIn("workflows: ['Enrich project evidence', 'Refresh GitHub metadata']", publisher)
        self.assertIn('ref: main', publisher)
        self.assertNotIn('pull_request_target', publisher)
        self.assertIn('head_repository.full_name == github.repository', publisher)


if __name__ == '__main__':
    unittest.main()
