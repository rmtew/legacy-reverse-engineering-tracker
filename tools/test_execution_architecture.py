"""Canonical architecture migration, immutable inputs and replay boundaries."""
import copy
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from apply_discovery_batch import apply_batch
from catalogue_storage import encode, load_projects, render, write_all, write_projects
from execution_architecture import activity_v1_event, check_methods
from generate_recent_activity import recent_activity
from migrate_baked_emulation import migrate, migrate_record, path_digest
from research_record import compile_records, render_report, review_digest, seal_review
from test_research_record import sample_record

OLD = 'game-specific-emulation'  # Only historical-format fixtures use this key.


def record(pid='example', method=OLD, name='embedded runtime'):
    return {'id': pid, 'title': 'Example', 'notes': 'Recorded evidence',
            'execution_paths': [{'name': name, 'method': method, 'status': 'partial',
                                 'notes': 'guest registers and machine memory',
                                 'evidence': ['https://example.org/source']}]}


class ExecutionArchitectureTests(unittest.TestCase):
    def test_versioned_sealed_input_is_verified_then_decoded_without_hash_mutation(self):
        document = sample_record()
        document['records'][0]['project']['execution_paths'] = record()['execution_paths']
        # Historical seal fixture, made before the authoring migration. The
        # current seal_review API must reject creation/resealing of this input.
        document['review'] = {'status': 'ready', 'digest': review_digest(document)}
        before = copy.deepcopy(document); digest = review_digest(document)
        with self.assertRaisesRegex(ValueError, 'canonical execution method'):
            seal_review(document)
        project = compile_records(document)['projects'][0]['project']
        self.assertEqual(project['execution_paths'][0]['method'], 'baked-emulation')
        self.assertEqual(document, before); self.assertEqual(review_digest(document), digest)
        document['records'][0]['project']['execution_paths'][0]['method'] = 'baked-emulation'
        with self.assertRaisesRegex(ValueError, 'Stale research review'):
            compile_records(document)

    def test_current_authoring_and_sealing_reject_legacy_but_accept_canonical(self):
        document = sample_record()
        document['records'][0]['project']['execution_paths'] = record()['execution_paths']
        original = copy.deepcopy(document)
        with self.assertRaisesRegex(ValueError, 'canonical execution method'):
            seal_review(document)
        for status in ('draft', 'ready'):
            document['review'] = {'status': status}
            with self.assertRaisesRegex(ValueError, 'canonical execution method'):
                render_report(document)
        document['review'] = {'status': 'ready'}
        with self.assertRaisesRegex(ValueError, 'canonical execution method'):
            compile_records(document)
        document['records'][0]['project']['execution_paths'][0]['method'] = 'baked-emulation'
        sealed = seal_review(document)
        self.assertEqual(compile_records(sealed)['projects'][0]['project']['execution_paths'][0]['method'], 'baked-emulation')
        self.assertIn('baked-emulation', render_report(sealed))
        self.assertEqual(original['records'][0]['project']['execution_paths'][0]['method'], OLD)

    def test_canonical_writer_rejects_old_method_without_writing(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            with self.assertRaisesRegex(ValueError, 'canonical execution method'):
                write_projects(root / 'projects.json', [record()])
            self.assertEqual(list(root.iterdir()), [])
        check_methods(record(method='baked-emulation'))
        check_methods(record(method='native-translation'))

    def test_explicit_compiled_runtime_migration_preserves_ordinary_native_and_mixed_paths(self):
        compiled = record('pop2-macintosh-static-recompilation', 'native-translation',
                          'Statically translated C++ with Toolbox API shims')
        ordinary = record(method='native-translation', name='Recovered game logic with API shims')
        mixed = record()
        mixed['execution_paths'].append(ordinary['execution_paths'][0])
        with patch.dict('migrate_baked_emulation.EXPECTED_COMPILED_PATHS', {compiled['id']: path_digest(compiled['execution_paths'][0])}):
            migrated = migrate_record(compiled)
            changed = copy.deepcopy(compiled); changed['execution_paths'][0]['notes'] = 'Concurrent architecture revision'
            with self.assertRaisesRegex(ValueError, 'Execution path changed'):
                migrate_record(changed)
        self.assertEqual(migrated['execution_paths'][0]['method'], 'baked-emulation')
        self.assertEqual(migrated['execution_paths'][0]['evidence'], compiled['execution_paths'][0]['evidence'])
        self.assertEqual(migrated['execution_paths'][0]['status'], 'partial')
        self.assertEqual(migrate_record(ordinary), ordinary)
        self.assertEqual([p['method'] for p in migrate_record(mixed)['execution_paths']],
                         ['baked-emulation', 'native-translation'])
        self.assertEqual(migrate_record(migrated), migrated)

    def test_migration_preserves_coverage_evidence_pending_baseline_and_noop_bytes(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); data = root / 'data'; data.mkdir(); (root / 'state').mkdir()
            original = [record(), record('native', 'native-translation')]
            # Materialize a historical storage fixture, bypassing the NEW writer.
            for name, raw in render('projects.json', original).items():
                target = data / name; target.parent.mkdir(exist_ok=True); target.write_bytes(raw)
            write_all(data, {'project-audits.json': {'projects': [{'project_id': p['id']} for p in original]}})
            state = {'generated_at': 'unchanged', 'projects': {p['id']: copy.deepcopy(p) for p in original}}
            state['projects']['example']['notes'] = 'Previous notes awaiting metadata'
            (root / 'state/project-catalog-state.json').write_bytes(encode(state))
            audit_bytes = {p.name: p.read_bytes() for p in (data / 'project-audits').iterdir()}
            outcome = migrate(root); after = load_projects(data / 'projects.json')
            self.assertEqual(outcome['changed_projects'], ['example'])
            self.assertEqual([p['id'] for p in after], [p['id'] for p in original])
            self.assertEqual(after[0]['notes'], original[0]['notes'])
            baseline = json.loads((root / 'state/project-catalog-state.json').read_bytes())
            self.assertEqual(baseline['projects']['example']['notes'], 'Previous notes awaiting metadata')
            self.assertEqual(baseline, state)
            self.assertEqual(audit_bytes, {p.name: p.read_bytes() for p in (data / 'project-audits').iterdir()})
            before_bytes = {str(p.relative_to(root)): p.read_bytes() for p in root.rglob('*') if p.is_file()}
            self.assertEqual(migrate(root)['changed_projects'], [])
            self.assertEqual(before_bytes, {str(p.relative_to(root)): p.read_bytes() for p in root.rglob('*') if p.is_file()})

    def test_historical_activity_projection_normalizes_only_structured_values(self):
        event = {'type': 'project_removed', 'project_id': 'example', 'date': '2026-10-22T00:00:00Z',
                 'project': record(), 'message': 'Historical source judgment: ' + OLD,
                 'change_details': [{'field': 'execution_paths', 'before': record()['execution_paths'], 'after': None}]}
        before = copy.deepcopy(event)
        projected = activity_v1_event(event)
        self.assertEqual(event, before)
        self.assertEqual(projected['project']['execution_paths'][0]['method'], 'baked-emulation')
        self.assertIsNone(projected['change_details'][0]['after'])
        self.assertEqual(projected['message'], event['message'])
        feed = recent_activity({'generated_at': event['date'], 'events': [event]}, projects=[])
        self.assertEqual(feed['events'][0]['project']['execution_paths'][0]['method'], 'baked-emulation')

    def test_pending_full_record_with_pre_migration_hash_fails_safely(self):
        old = record(); current = migrate_record(old)
        data = {'projects.json': [current], 'project-audits.json': {'projects': []},
                'discovery-sources.json': {'sources': [], 'backlog': []},
                'discovery-decisions.json': {'decisions': []}, 'research-activity.json': {'events': []}}
        before = copy.deepcopy(data)
        expected = hashlib.sha256(json.dumps(old, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()).hexdigest()
        batch = {'date': '2026-10-22', 'event_id': 'fixture', 'summary': 'Fixture only',
                 'project_updates': [{'project_id': 'example', 'expected_sha256': expected,
                                      'changes': {'title': 'New title'}}]}
        with self.assertRaisesRegex(ValueError, 'Stale project update'):
            apply_batch(data, batch)
        self.assertEqual(data, before)

    def test_enrichment_cannot_restore_obsolete_method(self):
        import enrichment_pipeline as pipeline
        project = sample_record()['records'][0]['project']
        project['execution_paths'] = record(method='baked-emulation')['execution_paths']
        row = {'id': project['id'], 'fingerprint': pipeline.fingerprint(project),
               'state_before': {}, 'state_after': {},
               'guards': [{'path': list(p), 'before': pipeline.value_at(project, p)} for p in pipeline.OWNED],
               'patch': [{'path': ['execution_paths'], 'after': {'exists': True, 'value': record()['execution_paths']}}]}
        after, _, summary = pipeline.replay([project], {'records': {}}, {'version': 1, 'results': [row]})
        self.assertEqual(after, [project]); self.assertEqual(summary['conflicts'], [project['id']])

    def test_schema_validator_accepts_new_method_and_rejects_legacy_method(self):
        import validate_site_data as site
        project = compile_records(seal_review(sample_record()))['projects'][0]['project']
        project['execution_paths'] = record(method='baked-emulation')['execution_paths']
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); activity = root / 'activity.json'
            activity.write_bytes(encode({'generated_at': '2026-10-22T00:00:00Z', 'events': []}))
            with patch.object(site, 'load_projects', return_value=[project]), patch.object(site, 'validate_research_state', return_value=(0, 0, 0, 0)), redirect_stdout(StringIO()):
                site.validate(root / 'projects.json', activity)
                project['execution_paths'][0]['method'] = OLD
                errors = StringIO()
                with redirect_stderr(errors), self.assertRaises(SystemExit):
                    site.validate(root / 'projects.json', activity)
                self.assertIn('invalid method', errors.getvalue())

    def test_retained_enrichment_owned_patch_survives_canonical_migration(self):
        import enrichment_pipeline as pipeline
        before = compile_records(seal_review(sample_record()))['projects'][0]['project']
        before['execution_paths'] = record()['execution_paths']
        current = migrate_record(before)
        row = {'id': before['id'], 'fingerprint': pipeline.fingerprint(before),
               'state_before': {}, 'state_after': {'fingerprint': pipeline.fingerprint(before)},
               'guards': [{'path': list(p), 'before': pipeline.value_at(before, p)} for p in pipeline.OWNED],
               'patch': [{'path': ['build', 'compilable'], 'after': {'exists': True, 'value': True}}]}
        after, _, summary = pipeline.replay([current], {'records': {}}, {'version': 1, 'results': [row]})
        self.assertEqual(summary['accepted'], [before['id']])
        self.assertTrue(after[0]['build']['compilable'])
        self.assertEqual(after[0]['execution_paths'], current['execution_paths'])
