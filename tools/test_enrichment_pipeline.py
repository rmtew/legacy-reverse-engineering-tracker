"""Offline budgets, cache semantics and compare-and-set publication replay."""
import copy
from contextlib import redirect_stdout
from datetime import datetime, timedelta, timezone
from io import BytesIO, StringIO
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch
from urllib.error import HTTPError, URLError

import enrichment_pipeline as pipeline
from catalogue_storage import encode, load_projects, request_size, write_projects

NOW = datetime(2026, 10, 19, tzinfo=timezone.utc)
SHA = 'a' * 40


def project(pid='a'):
    return {'id': pid, 'repo': 'https://github.com/owner/' + pid,
            'build': {'compilable': None, 'playable': None, 'byte_exact': None, 'runnable': None},
            're_started': None, 'notes': 'Curated notes', 'evidence': {'curated': {'note': 'Preserve me'}}}


class Response(BytesIO):
    status = 200


class Network:
    def __init__(self):
        self.calls = []
        self.commit, self.document, self.failure, self.delay, self.time = SHA, 'The project builds.\nThe game is playable.', None, 0, 0
        self.ci_runs = []

    def clock(self):
        return self.time

    def open(self, request, timeout):
        url = request.full_url
        self.calls.append((url, timeout))
        self.time += self.delay
        if self.failure and self.failure in url:
            raise URLError('temporary network failure')
        if '/git/ref/heads/' in url:
            return Response(encode({'object': {'sha': self.commit, 'type': 'commit'}}))
        if '/actions/runs?' in url:
            return Response(encode({'workflow_runs': self.ci_runs}))
        if url.endswith('/README.md') and self.document is not None:
            return Response(self.document.encode())
        raise HTTPError(url, 404, 'Not Found', {}, None)


class EnrichmentTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'repo'
        self.root.mkdir()
        self.bundle = Path(self.temp.name) / 'bundle.json'
        self.network = Network()
        self.records = [project('a'), project('b'), project('c')]
        write_projects(self.root / 'data/projects.json', self.records)
        self.state = {'version': 1, 'records': {}}
        self.output = StringIO()
        self.quiet = redirect_stdout(self.output)
        self.quiet.__enter__()
        self.addCleanup(self.quiet.__exit__, None, None, None)

    def collect(self, *, state=None, records=None, now=NOW, limit=20, requests=300, seconds=600):
        if records is not None:
            write_projects(self.root / 'data/projects.json', records)
        if state is not None:
            path = self.root / pipeline.STATE
            path.parent.mkdir(exist_ok=True)
            path.write_bytes(encode(state))
        self.bundle.unlink(missing_ok=True)
        budget = pipeline.Budget(seconds, requests, clock=self.network.clock)
        client = pipeline.Client(budget, opener=self.network.open, token='')
        result = pipeline.collect(self.root, self.bundle, budget, now=now, limit=limit, client=client)
        return result, budget

    def complete_one(self):
        bundle, _ = self.collect(limit=1)
        records, state, summary = pipeline.replay(self.records, self.state, bundle)
        self.assertEqual(summary['accepted'], ['a'])
        return records, state

    def test_selection_resume_and_progress_are_published_with_results(self):
        before = {p: p.read_bytes() for p in (self.root/'data').rglob('*.json')}
        bundle, _ = self.collect(limit=1)
        self.assertTrue(all(p.read_bytes() == content for p, content in before.items()))
        self.assertFalse((self.root / pipeline.STATE).exists())
        self.assertEqual([p['id'] for p in pipeline.select(self.records, self.state, NOW)], ['a','b','c'])
        records, state, _ = pipeline.replay(self.records, self.state, bundle)
        self.assertTrue(records[0]['build']['compilable'])
        self.assertEqual([p['id'] for p in pipeline.select(records, state, NOW)], ['b','c'])
        self.assertEqual(state['records']['a']['fingerprint'], pipeline.fingerprint(records[0]))

    def test_changed_or_overdue_only_and_oldest_attempt_is_fair(self):
        records, state = self.complete_one()
        state['records']['b'] = {'last_attempt_at': pipeline.stamp(NOW-timedelta(days=2))}
        self.assertEqual([p['id'] for p in pipeline.select(records,state,NOW)], ['c','b'])
        changed = copy.deepcopy(records)
        changed[0]['github'] = {'pushed_at':'2026-10-19T01:00:00Z'}
        self.assertIn('a',[p['id'] for p in pipeline.select(changed,state,NOW)])
        self.assertIn('a',[p['id'] for p in pipeline.select(records,state,NOW+timedelta(days=8))])

    def test_request_budget_reserves_complete_record_and_stops_cleanly(self):
        bundle, budget = self.collect(requests=20)
        self.assertEqual(bundle['summary']['completed'],1)
        self.assertLessEqual(budget.requests,20)
        self.assertEqual(bundle['results'][1]['status'],'deferred')
        self.assertNotIn('fingerprint',bundle['results'][1]['state_after'])
        records,state,_=pipeline.replay(self.records,self.state,bundle)
        self.assertEqual(state['records']['a']['fingerprint'],pipeline.fingerprint(records[0]))
        self.assertEqual([p['id'] for p in pipeline.select(records,state,NOW)],['c','b'])

    def test_zero_requests_advances_no_record(self):
        bundle,budget=self.collect(requests=0)
        self.assertEqual(bundle['results'],[])
        self.assertEqual(budget.requests,0)

    def test_deadline_mid_record_keeps_prior_evidence_and_no_completion(self):
        records,state=self.complete_one()
        self.network.commit='b'*40;self.network.delay=.3
        bundle,budget=self.collect(records=[records[0]],state=state,now=NOW+timedelta(days=2),seconds=.5,limit=1)
        self.assertEqual(bundle['summary']['completed'],0)
        replayed,after,_=pipeline.replay([records[0]],state,bundle)
        self.assertEqual(replayed,[records[0]])
        self.assertEqual(after['records']['a']['docs_checked_at'],state['records']['a']['docs_checked_at'])
        self.assertTrue(all(timeout<=10 for _,timeout in self.network.calls))

    def test_transient_failure_preserves_evidence_and_moves_retry_out_of_way(self):
        records,state=self.complete_one()
        self.network.failure='/README.md'
        self.network.commit='b'*40
        bundle,_=self.collect(records=[records[0]],state=state,now=NOW+timedelta(days=2))
        replayed,after,_=pipeline.replay([records[0]],state,bundle)
        self.assertEqual(replayed,[records[0]])
        entry=after['records']['a']
        self.assertEqual(entry['docs_key'],state['records']['a']['docs_key'])
        self.assertEqual(pipeline.select(replayed,after,NOW+timedelta(days=2)),[])
        self.assertGreater(pipeline.parsed(entry['retry_at']),NOW+timedelta(days=2))

    def test_genuine_absence_retracts_previous_automated_claims(self):
        records,state=self.complete_one()
        self.network.commit='b'*40;self.network.document=None
        bundle,_=self.collect(records=[records[0]],state=state,now=NOW+timedelta(days=2))
        replayed,after,_=pipeline.replay([records[0]],state,bundle)
        self.assertEqual(bundle['summary']['completed'],1)
        self.assertIsNone(replayed[0]['build']['compilable'])
        self.assertNotIn('automated',replayed[0]['evidence'])
        self.assertEqual(replayed[0]['evidence']['curated'],records[0]['evidence']['curated'])
        self.assertNotEqual(after['records']['a']['docs_key'],state['records']['a']['docs_key'])

    def test_unchanged_docs_reused_while_ci_refreshes_without_project_rewrite(self):
        records,state=self.complete_one()
        self.network.calls=[]
        bundle,budget=self.collect(records=[records[0]],state=state,now=NOW+timedelta(days=2))
        self.assertEqual(budget.requests,2)
        self.assertFalse(any('raw.githubusercontent.com' in url for url,_ in self.network.calls))
        self.assertEqual(bundle['results'][0]['patch'],[])
        self.assertGreater(budget.cache_hits,0)
        replayed,after,_=pipeline.replay([records[0]],state,bundle)
        self.assertEqual(replayed,[records[0]])
        self.assertGreater(after['records']['a']['ci_checked_at'],state['records']['a']['ci_checked_at'])

    def test_empty_document_result_is_also_cached(self):
        self.network.document=None
        bundle,_=self.collect(records=[self.records[0]])
        records,state,_=pipeline.replay([self.records[0]],self.state,bundle)
        self.network.calls=[]
        again,budget=self.collect(records=records,state=state,now=NOW+timedelta(days=2))
        self.assertEqual(budget.requests,2)
        self.assertEqual(again['results'][0]['patch'],[])

    def test_ci_error_does_not_turn_into_successful_empty_result(self):
        records,state=self.complete_one()
        self.network.failure='/actions/runs?'
        bundle,_=self.collect(records=[records[0]],state=state,now=NOW+timedelta(days=2))
        self.assertEqual(bundle['summary']['completed'],0)
        replayed,after,_=pipeline.replay([records[0]],state,bundle)
        self.assertEqual(replayed,[records[0]])
        self.assertEqual(after['records']['a']['ci_checked_at'],state['records']['a']['ci_checked_at'])

    def test_rate_limit_stops_slice_and_preserves_existing_results(self):
        original=self.network.open
        def limited(request,timeout):
            if 'owner/b/' in request.full_url:
                raise HTTPError(request.full_url,403,'rate limit',{'X-RateLimit-Remaining':'0'},None)
            return original(request,timeout)
        self.network.open=limited
        bundle,_=self.collect()
        self.assertEqual([r['id'] for r in bundle['results']],['a','b'])
        self.assertEqual(bundle['summary']['completed'],1)

    def test_replay_keeps_concurrent_unrelated_edits_and_requires_no_network(self):
        bundle,_=self.collect(limit=1)
        concurrent=copy.deepcopy(self.records)
        concurrent[0]['notes']='New authored notes'
        concurrent[0]['github']={'checked_at':'new poll timestamp'}
        concurrent[0]['evidence']['curated']['note']='New curated evidence'
        calls=len(self.network.calls)
        records,state,summary=pipeline.replay(concurrent,self.state,bundle)
        self.assertEqual(len(self.network.calls),calls)
        self.assertEqual(summary['conflicts'],[])
        self.assertEqual(records[0]['notes'],'New authored notes')
        self.assertEqual(records[0]['evidence']['curated']['note'],'New curated evidence')
        self.assertTrue(records[0]['build']['compilable'])
        again,again_state,_=pipeline.replay(records,state,bundle)
        self.assertEqual(again,records);self.assertEqual(again_state,state)

    def test_conflicting_fields_tracking_and_progress_are_not_overwritten(self):
        bundle,_=self.collect(limit=1)
        for modify in [lambda p:p['build'].update(compilable=False),
                       lambda p:p['build'].update(compilable=True),
                       lambda p:p.update(github_branch='different'),
                       lambda p:p['evidence'].update(automated={'curated':'manual edit'})]:
            records=copy.deepcopy(self.records);modify(records[0])
            after,state,summary=pipeline.replay(records,self.state,bundle)
            self.assertEqual(after,records);self.assertEqual(state,self.state)
            self.assertEqual(summary['conflicts'],['a'])
        state={'version':1,'records':{'a':{'last_attempt_at':'2026-10-19T01:00:00Z'}}}
        _,after,summary=pipeline.replay(self.records,state,bundle)
        self.assertEqual(after,state);self.assertEqual(summary['conflicts'],['a'])

    def test_manual_reversion_after_publication_does_not_get_reapplied(self):
        bundle,_=self.collect(limit=1)
        records,state,_=pipeline.replay(self.records,self.state,bundle)
        records[0]['build']['compilable']=None
        again,after,summary=pipeline.replay(records,state,bundle)
        self.assertEqual(again,records);self.assertEqual(after,state)
        self.assertEqual(summary['conflicts'],['a'])

    def test_removed_records_pruned_and_state_has_no_evidence_copy_or_history(self):
        records,state=self.complete_one()
        bundle,_=self.collect(records=[records[0]],state=state,now=NOW+timedelta(days=2))
        _,after,_=pipeline.replay([],state,bundle)
        self.assertEqual(after['records'],{})
        for entry in state['records'].values():
            self.assertNotIn('evidence',entry);self.assertNotIn('documents',entry)
            self.assertTrue(all(not isinstance(v,(dict,list)) for v in entry.values()))
        expanded={'version':1,'records':{str(i):copy.deepcopy(state['records']['a']) for i in range(3307)}}
        self.assertLess(request_size(encode(expanded)),4*1024*1024)
        bounded=pipeline.bounded
        with patch.object(pipeline,'bounded',side_effect=lambda b,n:bounded(b,n,limit=200)):
            with self.assertRaisesRegex(ValueError,'exceeds'):
                pipeline.replay(records,state,bundle)

    def test_staged_validation_failure_does_not_advance_progress(self):
        bundle,_=self.collect(limit=1)
        (self.root/'data/activity.json').write_bytes(encode({}))
        before={p:p.read_bytes() for p in (self.root/'data').rglob('*.json')}
        with patch('validate_site_data.validate',side_effect=ValueError('invalid staged data')):
            with self.assertRaisesRegex(ValueError,'invalid staged data'):
                pipeline.apply_bundle(self.root,bundle)
        self.assertTrue(all(p.read_bytes()==b for p,b in before.items()))
        self.assertFalse((self.root/pipeline.STATE).exists())

    def test_data_and_progress_form_one_commit_and_retry_is_idempotent(self):
        def git(*args):return subprocess.check_output(['git',*args],cwd=self.root,stderr=subprocess.DEVNULL).decode().strip()
        git('init','-q');git('config','user.email','test@example.invalid');git('config','user.name','Test')
        (self.root/'data/activity.json').write_bytes(encode({}))
        git('add','.');git('commit','-qm','baseline')
        bundle,_=self.collect(limit=1)
        with patch('validate_site_data.validate'):
            pipeline.apply_bundle(self.root,bundle)
        git('add','data',pipeline.STATE);git('commit','-qm','results and progress')
        paths=git('diff','--name-only','HEAD^','HEAD').splitlines()
        self.assertIn(pipeline.STATE,paths)
        self.assertIn('data/projects.index.json',paths)
        with patch('validate_site_data.validate'):
            pipeline.apply_bundle(self.root,bundle)
        self.assertEqual(git('status','--porcelain'),'')
        self.assertTrue(load_projects(self.root/'data/projects.json')[0]['build']['compilable'])

    def test_logs_are_immediate_structured_request_and_progress_counters(self):
        bundle,_=self.collect(limit=1)
        lines=[json.loads(line) for line in self.output.getvalue().splitlines()]
        self.assertTrue(any('request' in line and 'status' in line and 'seconds' in line for line in lines))
        self.assertTrue(any('project' in line and 'completed' in line for line in lines))
        self.assertEqual(lines[-1]['collection']['completed'],1)

    def test_completed_docs_survive_ci_failure_without_marking_ci_fresh(self):
        records,state=self.complete_one()
        self.network.commit='b'*40
        self.network.failure='/actions/runs?'
        bundle,_=self.collect(records=[records[0]],state=state,now=NOW+timedelta(days=2))
        self.assertEqual(bundle['results'][0]['status'],'partial')
        replayed,after,_=pipeline.replay([records[0]],state,bundle)
        self.assertIn('b'*40,replayed[0]['evidence']['automated']['compilable'][0]['url'])
        self.assertGreater(after['records']['a']['docs_checked_at'],state['records']['a']['docs_checked_at'])
        self.assertEqual(after['records']['a']['ci_checked_at'],state['records']['a']['ci_checked_at'])
        self.assertTrue(replayed[0]['build']['compilable'])

    def test_existing_bundle_fails_before_any_network_requests(self):
        self.bundle.write_text('{}')
        budget=pipeline.Budget()
        with self.assertRaisesRegex(ValueError,'already exists'):
            pipeline.collect(self.root,self.bundle,budget,client=pipeline.Client(budget,opener=self.network.open))
        self.assertEqual(self.network.calls,[])

    def test_concurrent_parent_shape_change_is_a_conflict(self):
        bundle,_=self.collect(limit=1)
        records=copy.deepcopy(self.records);records[0]['evidence']=None
        after,state,summary=pipeline.replay(records,self.state,bundle)
        self.assertEqual(after,records);self.assertEqual(state,self.state)
        self.assertEqual(summary['conflicts'],['a'])



class WorkflowTests(unittest.TestCase):
    def test_collection_occurs_once_and_retry_replays_same_external_bundle(self):
        workflow=(Path(__file__).resolve().parents[1]/'.github/workflows/enrich-evidence.yml').read_text()
        self.assertIn('timeout-minutes: 20',workflow)
        self.assertIn('cancel-in-progress: false',workflow)
        self.assertEqual(workflow.count('enrich_evidence.py collect'),1)
        loop=workflow.split('for attempt in 1 2 3; do',1)[1]
        self.assertNotIn(' collect',loop)
        self.assertIn('enrich_evidence.py apply',loop)
        self.assertIn('state/enrichment-state.json',loop)
        self.assertIn('data/projects.index.json data/projects/',loop)
        self.assertIn('git push origin HEAD:main',loop)
        self.assertNotIn('--force',loop)
        self.assertIn('$RUNNER_TEMP/enrichment-bundle.json',workflow)
