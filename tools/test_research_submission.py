"""Offline transactions, replay, concurrent Git writers, outbox recovery and data-only input."""
import copy
from contextlib import redirect_stdout
from io import StringIO
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

import research_submission as submission
from catalogue_storage import encode, load_all, load_projects, load_dataset, storage_paths, write_all, write_projects
from merge_pending_projects import new_audit
from research_record import seal_review
from test_research_record import sample_record
from record_project_activity import snapshot


class SubmissionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'repo'
        self.root.mkdir()
        self.git('init', '--initial-branch=main')
        self.git('config', 'user.name', 'Test')
        self.git('config', 'user.email', 'test@example.org')
        self.project = {'id': 'existing', 'title': 'Existing', 'upstream_name': 'Existing',
                        'display_title': 'Existing', 'subjects': ['Existing'], 'repo': 'https://example.org/existing',
                        'record_class': 'subject', 'target_kinds': ['game'], 'work_kinds': [], 'tool_kinds': [],
                        'notes': 'Preserve curated facts', 'github': {'checked_at': '2026-10-19'}}
        write_all(self.root / 'data', {
            'projects.json': [self.project], 'project-audits.json': {'projects': [new_audit('existing')]},
            'discovery-sources.json': {'sources': [{'id': 'web-6502disassembly-com', 'source': 'https://example.org',
                'first_indexed': '2026-10-06', 'last_reviewed': '2026-10-06', 'review_state': 'partial',
                'projects_promoted': [], 'open_task_ids': []}], 'backlog': []},
            'discovery-decisions.json': {'indexed_at': '2026-10-06', 'decisions': []},
            'research-activity.json': {'events': []}})
        self.put('data/activity.json', {'generated_at': '2026-10-19T00:00:00Z', 'window_days': 30, 'events': []})
        self.put('data/pending-projects.json', [])
        self.put('state/project-catalog-state.json', {'projects': {'existing': snapshot(self.project)}})
        self.put('state/github-poll-state.json', {'repositories': {}})
        (self.root / 'web').mkdir()
        (self.root / 'web/tracker.js').write_text('console.log("ok")')
        (self.root / 'web/reading-state.js').write_text('console.log("reading state")')
        (self.root / 'web/tracker.css').write_text('body{}')
        (self.root / 'index.html').write_text('<link href="web/tracker.css"><script src="web/reading-state.js"></script><script src="web/tracker.js"></script>')
        for name in ('sources.md', 'log.md'):
            (self.root / name).write_text('# Existing provenance\n')
        self.refresh_mock = patch.object(submission, 'dispatch_refresh')
        self.refresh_mock.start()
        self.addCleanup(self.refresh_mock.stop)
        self.document = seal_review(sample_record())
        self.input(self.document)
        self.commit()
        self.result = Path(self.temp.name) / 'result.json'
        self.quiet = redirect_stdout(StringIO())
        self.quiet.__enter__()
        self.addCleanup(self.quiet.__exit__, None, None, None)

    def git(self, *args):
        return subprocess.check_output(['git', *args], cwd=self.root, stderr=subprocess.DEVNULL).decode().strip()

    def put(self, path, value):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(encode(value))

    def input(self, document):
        raw, info = submission.package(document)
        target = self.root / info['path']
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(raw)

    def commit(self):
        self.git('add', '-A')
        self.git('commit', '-qm', 'Snapshot')
        return self.git('rev-parse', 'HEAD')

    def apply(self):
        return submission.apply(self.root, self.document['event_id'])

    def remote(self):
        origin = Path(self.temp.name) / 'origin.git'
        subprocess.run(['git', 'clone', '--bare', str(self.root), str(origin)], check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        self.git('remote', 'add', 'origin', str(origin))
        self.git('fetch', 'origin')
        return origin

    def proof_document(self):
        from research_record import git_blob_sha
        document = copy.deepcopy(self.document)
        document['proofs'] = {'source': {'repository': 'https://github.com/owner/repo',
            'commit': 'a' * 40, 'path': 'source.txt', 'blob': git_blob_sha('source\r\n'),
            'text': 'source\r\n'}}
        return seal_review(document)

    def test_package_omits_bodies_preserves_seal_and_accepts_identity_only(self):
        from research_record import EvidenceCache
        document = self.proof_document()
        raw, info = submission.package(document)
        lean = submission.decode(raw)
        self.assertNotIn('text', lean['proofs']['source'])
        self.assertEqual(lean['review'], document['review'])
        self.assertIn('text', document['proofs']['source'])
        self.assertEqual(submission.package(lean), (raw, info))
        cache = Path(self.temp.name) / 'local-cache'
        EvidenceCache(cache).put(document['proofs']['source'], 'source\r\n')
        self.assertEqual(submission.package(lean, cache), (raw, info))
        document['proofs']['source']['text'] = 'wrong'
        with self.assertRaisesRegex(ValueError, 'text/blob'):
            submission.package(document)

    def test_lean_first_apply_fetches_and_receipt_replay_is_offline(self):
        from research_record import EvidenceCache
        document = self.proof_document()
        self.input(document); self.commit()
        directories = []
        def hydrate(doc, directory, fetcher=None):
            self.assertNotIn('text', doc['proofs']['source'])
            directories.append(directory)
            cache = EvidenceCache(directory)
            cache.put(doc['proofs']['source'], 'source\r\n')
            return cache
        with patch('research_evidence.hydrate', side_effect=hydrate) as fetch:
            self.apply()
            fetch.assert_called_once()
        self.assertFalse(directories[0].exists())
        self.commit()
        with patch('research_evidence.hydrate', side_effect=AssertionError('must stay offline')):
            self.assertTrue(self.apply()['duplicate'])
            self.assertEqual(submission.selected(self.root), [self.document['event_id']])
        (self.root / submission.path_for(submission.OUTBOX, self.document['event_id'])).unlink()
        self.commit()
        with patch('research_evidence.hydrate', side_effect=AssertionError('must stay offline')):
            self.assertEqual(submission.selected(self.root), [])

    def test_compact_archive_retains_original_receipt_and_replays_offline(self):
        from compact_research_evidence import compact
        from research_record import EvidenceCache
        document = self.proof_document()
        # Preserve a legacy inline input exactly, rather than the new packager.
        input_path = submission.path_for(submission.INBOX, document['event_id'])
        self.put(input_path, document); self.commit()
        def hydrate(doc, directory, fetcher=None):
            cache = EvidenceCache(directory)
            cache.put(doc['proofs']['source'], 'source\r\n')
            return cache
        original_input_blob = self.git('rev-parse', 'HEAD:' + input_path)
        with patch('research_evidence.hydrate', side_effect=hydrate):
            result = self.apply()
        self.assertIn(input_path, result['changed'])
        self.assertNotIn('text', submission.decode((self.root / input_path).read_bytes())['proofs']['source'])
        receipt_path = self.root / submission.path_for(submission.RECEIPTS, document['event_id'])
        self.assertEqual(json.loads(receipt_path.read_bytes())['input_blob'], original_input_blob)
        self.commit()
        with patch('research_evidence.hydrate', side_effect=AssertionError('must stay offline')):
            self.assertTrue(self.apply()['duplicate'])
        # Recreate an archive written by the historical publisher to exercise
        # standalone migration, independently of the new first-apply compaction.
        self.put(input_path, document); self.commit()
        receipt_path = self.root / submission.path_for(submission.RECEIPTS, document['event_id'])
        original_receipt = receipt_path.read_bytes()
        state = load_all(self.root / 'data')
        report = (self.root / f"docs/research/{document['event_id']}.md").read_bytes()
        stats = compact(self.root, write=True)
        self.assertEqual(stats['proof_bodies'], 1)
        self.assertEqual(compact(self.root, write=True)['submissions'], 0)
        self.assertEqual(receipt_path.read_bytes(), original_receipt)
        self.assertEqual(state, load_all(self.root / 'data'))
        self.assertEqual(report, (self.root / f"docs/research/{document['event_id']}.md").read_bytes())
        self.commit()
        current_blob = self.git('rev-parse', 'HEAD:' + input_path)
        self.assertNotEqual(current_blob, json.loads(original_receipt)['input_blob'])
        with patch('research_evidence.hydrate', side_effect=AssertionError('must stay offline')):
            self.assertTrue(self.apply()['duplicate'])
            submission.selected(self.root)
        changed = submission.decode((self.root / input_path).read_bytes())
        changed['summary'] = 'different authored conclusion'
        self.put(input_path, seal_review(changed)); self.commit()
        with self.assertRaisesRegex(ValueError, 'conflicting reviewed content'):
            self.apply()

    def test_inline_compaction_write_failure_rolls_back_original_input(self):
        from research_record import EvidenceCache
        document = self.proof_document()
        input_path = self.root / submission.path_for(submission.INBOX, document['event_id'])
        self.put(str(input_path.relative_to(self.root)), document); self.commit()
        original_input = input_path.read_bytes()
        before = load_all(self.root / 'data')
        def hydrate(doc, directory, fetcher=None):
            cache = EvidenceCache(directory)
            cache.put(doc['proofs']['source'], 'source\r\n')
            return cache
        original_write = Path.write_bytes
        failed = False
        def write(path, raw):
            nonlocal failed
            result = original_write(path, raw)
            if path == input_path and not failed:
                failed = True
                raise OSError('compaction write interrupted')
            return result
        with patch('research_evidence.hydrate', side_effect=hydrate), patch.object(Path, 'write_bytes', write):
            with self.assertRaisesRegex(OSError, 'compaction write'):
                self.apply()
        self.assertEqual(input_path.read_bytes(), original_input)
        self.assertEqual(load_all(self.root / 'data'), before)
        self.assertFalse((self.root / submission.path_for(submission.RECEIPTS, document['event_id'])).exists())

    def test_failed_first_fetch_leaves_canonical_state_and_receipts_untouched(self):
        self.input(self.proof_document()); self.commit()
        before = load_all(self.root / 'data')
        with patch('research_evidence.hydrate', side_effect=ValueError('missing source')):
            with self.assertRaisesRegex(ValueError, 'missing source'):
                self.apply()
        self.assertEqual(before, load_all(self.root / 'data'))
        self.assertFalse((self.root / submission.RECEIPTS).exists())

    def test_atomic_validated_apply_receipt_and_identical_replay(self):
        before = copy.deepcopy(self.project)
        result = self.apply()
        self.assertFalse(result['duplicate'])
        records = load_projects(self.root / 'data/projects.json')
        self.assertEqual(next(p for p in records if p['id'] == 'existing'), before)
        self.assertIn(submission.path_for(submission.RECEIPTS, self.document['event_id']), result['changed'])
        self.assertIn(submission.path_for(submission.OUTBOX, self.document['event_id']), result['changed'])
        self.commit()
        state = load_all(self.root / 'data')
        repeated = self.apply()
        self.assertTrue(repeated['duplicate'])
        self.assertEqual(state, load_all(self.root / 'data'))
        self.assertEqual(len([e for e in state['research-activity.json']['events'] if e['id'] == self.document['event_id']]), 1)

    def test_submission_migrates_legacy_decisions_atomically(self):
        data = self.root / 'data'
        value = load_dataset(data, 'discovery-decisions.json')
        for name in storage_paths(data, ['discovery-decisions.json']):
            (data / name).unlink()
        self.put('data/discovery-decisions.json', value)
        self.commit()
        result = self.apply()
        self.assertIn('data/discovery-decisions.json', result['changed'])
        self.assertIn('data/discovery-decisions.index.json', result['changed'])
        self.assertFalse((data / 'discovery-decisions.json').exists())
        self.assertEqual(load_dataset(data, 'discovery-decisions.json')['decisions'], value['decisions'])
        self.commit()
        self.assertTrue(self.apply()['duplicate'])

    def test_conflicting_id_and_unreviewed_input_preserve_all_data(self):
        self.apply(); self.commit()
        before = load_all(self.root / 'data')
        changed = copy.deepcopy(self.document); changed['summary'] = 'Conflicting content'
        self.input(seal_review(changed)); self.commit()
        with self.assertRaisesRegex(ValueError, 'conflicting reviewed content'):
            self.apply()
        self.assertEqual(before, load_all(self.root / 'data'))
        changed['review'] = {'status': 'draft'}
        self.put(submission.path_for(submission.INBOX, self.document['event_id']), changed); self.commit()
        with self.assertRaisesRegex(ValueError, 'review seal'):
            self.apply()
        self.assertEqual(before, load_all(self.root / 'data'))

    def test_invalid_project_fails_before_any_write(self):
        document = copy.deepcopy(self.document)
        document['records'][0]['project']['record_class'] = 'invalid'
        self.input(seal_review(document)); self.commit()
        before = load_all(self.root / 'data')
        with self.assertRaises((ValueError, SystemExit)):
            self.apply()
        self.assertEqual(before, load_all(self.root / 'data'))
        self.assertFalse((self.root / submission.RECEIPTS).exists())

    def test_retries_concurrent_refresh_without_overwriting_existing_records(self):
        origin = self.remote()
        real_git = submission.git
        raced = False
        def command(root, *args, **kwargs):
            nonlocal raced
            if args[:2] == ('push', 'origin') and not raced:
                raced = True
                other = Path(self.temp.name) / 'other'
                subprocess.run(['git', 'clone', str(origin), str(other)], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                subprocess.run(['git', 'config', 'user.name', 'Concurrent'], cwd=other, check=True)
                subprocess.run(['git', 'config', 'user.email', 'concurrent@example.org'], cwd=other, check=True)
                records = load_projects(other / 'data/projects.json')
                records[0]['github']['stars'] = 99
                write_projects(other / 'data/projects.json', records)
                subprocess.run(['git', 'add', 'data'], cwd=other, check=True)
                subprocess.run(['git', 'commit', '-qm', 'Concurrent refresh'], cwd=other, check=True)
                subprocess.run(['git', 'push', 'origin', 'main'], cwd=other, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return real_git(root, *args, **kwargs)
        with patch.object(submission, 'git', side_effect=command):
            submission.publish(self.root, self.result)
        records = load_projects(self.root / 'data/projects.json')
        self.assertEqual(next(p for p in records if p['id'] == 'existing')['github']['stars'], 99)
        self.assertEqual(len(records), 2)
        self.assertEqual(submission.selected(self.root), [self.document['event_id']])  # Durable pending handoff.

    def test_handoff_failure_leaves_outbox_then_acknowledges_without_reapplication(self):
        self.remote()
        submission.publish(self.root, self.result)
        published = self.git('rev-parse', 'HEAD')
        before = load_all(self.root / 'data')
        with patch('pages_publication.GitHub'), patch('pages_publication.request', side_effect=RuntimeError('notification failed')):
            with self.assertRaises(RuntimeError):
                submission.handoff(self.root, self.result)
        self.assertTrue((self.root / submission.path_for(submission.OUTBOX, self.document['event_id'])).exists())
        with patch('pages_publication.GitHub'), patch('pages_publication.request', return_value={'deploy': False}) as request:
            submission.handoff(self.root, self.result)
            self.assertEqual(request.call_count, 1)
            self.assertNotEqual(self.git('rev-parse', 'HEAD'), published)
        self.assertEqual(before, load_all(self.root / 'data'))
        self.assertEqual(submission.selected(self.root), [])
        with patch('pages_publication.request') as request:
            submission.handoff(self.root, self.result)
            request.assert_not_called()

    def test_failed_push_cannot_notify_or_lose_pending_submission(self):
        self.remote(); real_git = submission.git
        def command(root, *args, **kwargs):
            if args[:2] == ('push', 'origin'):
                return subprocess.CompletedProcess(args, 1, b'', b'Race')
            return real_git(root, *args, **kwargs)
        with patch.object(submission, 'git', side_effect=command), patch('pages_publication.request') as request:
            with self.assertRaises(RuntimeError):
                submission.publish(self.root, self.result)
            request.assert_not_called()
        self.assertFalse(self.result.exists())
        submission.sync(self.root)
        self.assertEqual(len(load_projects(self.root / 'data/projects.json')), 1)
        submission.publish(self.root, self.result)
        self.assertEqual(len(load_projects(self.root / 'data/projects.json')), 2)

    def test_input_limits_duplicate_keys_paths_and_shell_text_are_data(self):
        for value in ('../escape', 'a/b', 'x\nrun', '-option', 'a' * 129):
            with self.assertRaises(ValueError):
                submission.event_name(value)
        with self.assertRaisesRegex(ValueError, 'Duplicate JSON'):
            submission.decode(b'{"a":1,"a":2}')
        with self.assertRaises(ValueError):
            submission.decode(b' ' * (submission.MAX_BYTES + 1))
        document = copy.deepcopy(self.document)
        document['summary'] = 'Literal $(touch /tmp/no-execution) `id` ${{ secrets.GITHUB_TOKEN }}'
        self.input(seal_review(document)); self.commit()
        self.apply()
        self.assertIn('$(touch', (self.root / f"docs/research/{document['event_id']}.md").read_text())

    def test_pending_scan_survives_coalesced_wakeups_and_is_bounded(self):
        for n in range(6):
            document = copy.deepcopy(self.document)
            document['event_id'] = f'queued-{n}'
            self.input(seal_review(document))
        self.commit()
        pending = submission.selected(self.root)
        self.assertEqual(len(pending), submission.MAX_BATCHES)
        self.assertEqual(pending, ['queued-0', 'queued-1', 'queued-2', 'queued-3'])

    def test_changed_trusted_tools_abort_for_a_fresh_job(self):
        self.remote()
        submission.sync(self.root)
        tools = self.root / 'tools'
        tools.mkdir()
        (tools / 'changed.py').write_text('# changed trusted tool')
        self.commit(); self.git('push', 'origin', 'main')
        before = load_all(self.root / 'data')
        with self.assertRaisesRegex(ValueError, 'tools changed'):
            submission.sync(self.root)
        self.assertEqual(before, load_all(self.root / 'data'))

    def test_connector_bundle_contains_only_small_input_and_resumes(self):
        output = Path(self.temp.name) / 'submission'
        info = submission.submission_bundle(self.document, self.root, output)
        manifest = json.loads((output / 'manifest.json').read_bytes())
        self.assertEqual(manifest['submission'], {'version': 1, 'event_id': self.document['event_id'], 'digest': info['digest']})
        self.assertEqual(len(manifest['files']), 1)
        self.assertTrue(manifest['files'][0]['path'].startswith('submissions/research/'))
        self.assertLess(info['bytes'], 10000)
        self.assertEqual(info, submission.submission_bundle(self.document, self.root, output))

    def test_partial_local_write_rolls_back_without_a_receipt(self):
        before = load_all(self.root / 'data')
        original = Path.write_bytes
        failed = False
        def write(path, content):
            nonlocal failed
            if str(path).endswith(submission.path_for(submission.RECEIPTS, self.document['event_id'])) and not failed:
                failed = True
                raise OSError('Simulated disk failure')
            return original(path, content)
        with patch.object(Path, 'write_bytes', write):
            with self.assertRaises(OSError):
                self.apply()
        self.assertEqual(before, load_all(self.root / 'data'))
        self.assertFalse((self.root / submission.path_for(submission.RECEIPTS, self.document['event_id'])).exists())

    def test_new_catalogue_cannot_deploy_before_enrichment(self):
        import pages_publication
        self.apply()
        head = self.commit()
        self.assertFalse(pages_publication.publishable(self.root, head))

    def test_trusted_workflow_never_checks_out_or_executes_submission_code(self):
        workflow = (Path(__file__).resolve().parents[1] / '.github/workflows/apply-research.yml').read_text()
        self.assertNotIn('pull_request', workflow)
        self.assertIn("if: github.ref == 'refs/heads/main'", workflow)
        self.assertIn('ref: main', workflow)
        self.assertNotIn('${{ inputs.', workflow.split('run: >-', 1)[1])
        self.assertIn('timeout-minutes: 15', workflow)

    def test_equivalent_serialization_does_not_requeue_delivered_input(self):
        self.apply(); self.commit()
        (self.root / submission.path_for(submission.OUTBOX, self.document['event_id'])).unlink(); self.commit()
        (self.root / submission.path_for(submission.INBOX, self.document['event_id'])).write_text(json.dumps(self.document, indent=2))
        self.commit()
        self.assertEqual(submission.selected(self.root), [])

    def test_refresh_scope_resolves_added_updated_current_urls_and_shared_repositories(self):
        result = self.apply()
        request = 'research-' + result['digest']
        path = submission.path_for(submission.RECEIPTS, self.document['event_id'])
        receipt = json.loads((self.root / path).read_bytes())
        receipt['summary'] = {'projects': ['new', 'shared', 'new', 'removed'],
                              'updated_projects': ['updated', 'web', 'new']}
        self.put(path, receipt)
        records = [
            {'id': 'new', 'repo': 'https://github.com/Mixed/Repository.git/'},
            {'id': 'shared', 'repo': 'https://github.com/Mixed/Repository'},
            {'id': 'updated', 'repo': 'https://github.com/Current/Location',
             'github': {'repository': 'stale/old-location'}},
            {'id': 'web', 'repo': 'https://example.org/source', 'github': {'repository': 'stale/web'}},
            {'id': 'untouched', 'repo': 'https://github.com/owner/due'},
        ]
        self.assertEqual(submission.refresh_repositories(self.root, request, records),
                         {'Mixed/Repository', 'Current/Location'})
        self.assertIsNone(submission.refresh_repositories(self.root, 'manual', records))
        self.assertEqual(submission.refresh_repositories(self.root, request, []), set())

    def test_refresh_scope_fails_closed_on_missing_ambiguous_or_invalid_intended_receipt(self):
        result = self.apply()
        request = 'research-' + result['digest']
        path = submission.path_for(submission.RECEIPTS, self.document['event_id'])
        original = json.loads((self.root / path).read_bytes())
        for invalid in ('research-', 'research-../escape', 'research-' + 'A' * 64,
                        'research-' + '0' * 64):
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                submission.refresh_repositories(self.root, invalid, [])
        for summary in (None, {}, {'projects': ['a'], 'updated_projects': 'a'},
                        {'projects': [None], 'updated_projects': []}):
            self.put(path, {**original, 'summary': summary})
            with self.subTest(summary=summary), self.assertRaises(ValueError):
                submission.refresh_repositories(self.root, request, [])
        self.put(path, {**original, 'event_id': 'wrong'})
        with self.assertRaisesRegex(ValueError, 'receipt'):
            submission.refresh_repositories(self.root, request, [])
        self.put(path, original)
        self.put(submission.path_for(submission.RECEIPTS, 'duplicate'), {**original, 'event_id': 'duplicate'})
        with self.assertRaisesRegex(ValueError, 'exactly one'):
            submission.refresh_repositories(self.root, request, [])

    def test_refresh_scope_ignores_unrelated_bad_receipts_and_bounds_scan(self):
        result = self.apply()
        request = 'research-' + result['digest']
        self.put(submission.path_for(submission.RECEIPTS, 'unrelated'), {'digest': '0' * 64})
        (self.root / submission.path_for(submission.RECEIPTS, 'damaged')).write_text('{not JSON')
        self.assertEqual(submission.refresh_repositories(self.root, request, []), set())
        with patch.object(submission, 'MAX_SCAN', 2), self.assertRaisesRegex(ValueError, 'scan ceiling'):
            submission.refresh_repositories(self.root, request, [])


if __name__ == '__main__':
    unittest.main()
