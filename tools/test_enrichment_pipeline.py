"""Offline budgets, cache semantics and compare-and-set publication replay."""
import copy
from contextlib import redirect_stdout
from datetime import datetime, timedelta, timezone
from io import BytesIO, StringIO
import json
import shutil
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
        self.confirm_status, self.confirm_sha = 200, None

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
        if '/git/commits/' in url:
            if self.confirm_status != 200:
                raise HTTPError(url, self.confirm_status, 'Unavailable', {}, None)
            return Response(encode({'sha': self.confirm_sha or url.rsplit('/', 1)[1]}))
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

    def collect(self, *, state=None, records=None, now=NOW, limit=20, requests=300, seconds=600, polling=None, docs_limit=64, ci_limit=60, api_requests=80):
        if records is not None:
            write_projects(self.root / 'data/projects.json', records)
        if state is not None:
            path = self.root / pipeline.STATE
            path.parent.mkdir(exist_ok=True)
            path.write_bytes(encode(state))
        if polling is not None:
            path=self.root/'state/github-poll-state.json';path.parent.mkdir(exist_ok=True)
            path.write_bytes(encode({'repositories':polling}))
        self.bundle.unlink(missing_ok=True)
        budget = pipeline.Budget(seconds, requests, api_requests=api_requests, clock=self.network.clock)
        client = pipeline.Client(budget, opener=self.network.open, token='')
        result = pipeline.collect(self.root, self.bundle, budget, now=now, limit=limit, client=client, docs_limit=docs_limit, ci_limit=ci_limit)
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
        self.assertIn('a',[p['id'] for p in pipeline.select(records,state,NOW+timedelta(days=31))])

    def test_inherited_instructions_supply_context_without_parent_facts(self):
        record = project('a')
        record['github_path'] = 'game'
        self.network.document = ''
        original_open = self.network.open
        def documents(request, timeout):
            if request.full_url.endswith('/' + SHA + '/AGENTS.md'):
                self.network.calls.append((request.full_url, timeout))
                return Response(b'We used Claude.\nTarget CPU: Z80\nThe game is playable.')
            return original_open(request, timeout)
        self.network.open = documents
        bundle, _ = self.collect(records=[record], ci_limit=0, limit=1)
        after, _, _ = pipeline.replay([record], self.state, bundle)
        self.assertNotIn('ai', after[0])
        self.assertNotIn('target_cpu', after[0])
        self.assertIsNone(after[0]['build']['playable'])
        self.assertEqual(after[0]['evidence']['automated']['ai_config'][0]['source'], 'AGENTS.md')

    def test_routine_promotions_publish_provenance_and_guard_curated_concurrent_edits(self):
        self.network.document = 'We used Claude.\nTarget CPU: 68020\nTarget platform: Amiga AGA'
        bundle, _ = self.collect(records=[self.records[0]], limit=1)
        records, _, summary = pipeline.replay([self.records[0]], self.state, bundle)
        self.assertEqual(records[0]['ai']['usage'], True)
        self.assertEqual(records[0]['target_cpu'], ['68020'])
        self.assertEqual(records[0]['target_platforms'], ['Amiga AGA'])
        self.assertIn(SHA, records[0]['evidence']['routine']['target_cpu'][0]['url'])
        self.assertEqual(records[0]['notes'], 'Curated notes')
        concurrent = copy.deepcopy(self.records[0])
        concurrent['ai'] = {'usage': False, 'tools': []}
        after, state, summary = pipeline.replay([concurrent], self.state, bundle)
        self.assertEqual(after, [concurrent])
        self.assertEqual(summary['conflicts'], ['a'])
        self.assertEqual(state, self.state)

    def test_request_budget_reserves_complete_record_and_stops_cleanly(self):
        bundle, budget = self.collect(requests=36)
        self.assertEqual(bundle['summary']['completed'],1)
        self.assertLessEqual(budget.requests,36)
        self.assertEqual(bundle['results'][1]['status'],'partial')
        self.assertNotIn('fingerprint',bundle['results'][1]['state_after'])
        records,state,_=pipeline.replay(self.records,self.state,bundle)
        self.assertEqual(state['records']['a']['fingerprint'],pipeline.fingerprint(records[0]))
        self.assertEqual([p['id'] for p in pipeline.select(records,state,NOW)],['b','c'])

    def test_zero_requests_advances_no_record(self):
        bundle,budget=self.collect(requests=0)
        self.assertEqual(bundle['results'],[])
        self.assertEqual(budget.requests,0)

    def test_deadline_mid_record_keeps_prior_evidence_and_no_completion(self):
        records,state=self.complete_one()
        self.network.commit='b'*40;self.network.delay=.3
        bundle,budget=self.collect(records=[records[0]],state=state,now=NOW+timedelta(days=31),seconds=.5,limit=1)
        self.assertEqual(bundle['summary']['completed'],0)
        replayed,after,_=pipeline.replay([records[0]],state,bundle)
        self.assertEqual(replayed,[records[0]])
        self.assertEqual(after['records']['a']['docs_checked_at'],state['records']['a']['docs_checked_at'])
        self.assertTrue(all(timeout<=10 for _,timeout in self.network.calls))

    def test_transient_failure_preserves_evidence_and_moves_retry_out_of_way(self):
        records,state=self.complete_one()
        self.network.failure='/README.md'
        self.network.commit='b'*40
        bundle,_=self.collect(records=[records[0]],state=state,now=NOW+timedelta(days=31))
        replayed,after,_=pipeline.replay([records[0]],state,bundle)
        self.assertEqual(replayed,[records[0]])
        entry=after['records']['a']
        self.assertEqual(entry['docs_key'],state['records']['a']['docs_key'])
        self.assertEqual(pipeline.select(replayed,after,NOW+timedelta(days=31)),[])
        self.assertGreater(pipeline.parsed(entry['retry_at']),NOW+timedelta(days=31))

    def test_genuine_absence_retracts_previous_automated_claims(self):
        records,state=self.complete_one()
        self.network.commit='b'*40;self.network.document=None
        bundle,_=self.collect(records=[records[0]],state=state,now=NOW+timedelta(days=31))
        replayed,after,_=pipeline.replay([records[0]],state,bundle)
        self.assertEqual(bundle['summary']['completed'],1)
        self.assertIsNone(replayed[0]['build']['compilable'])
        self.assertNotIn('automated',replayed[0]['evidence'])
        self.assertEqual(replayed[0]['evidence']['curated'],records[0]['evidence']['curated'])
        self.assertNotEqual(after['records']['a']['docs_key'],state['records']['a']['docs_key'])

    def test_unchanged_docs_reused_while_ci_refreshes_without_project_rewrite(self):
        records,state=self.complete_one()
        self.network.calls=[]
        bundle,budget=self.collect(records=[records[0]],state=state,now=NOW+timedelta(days=8))
        self.assertEqual(budget.requests,1)
        self.assertFalse(any('raw.githubusercontent.com' in url for url,_ in self.network.calls))
        self.assertEqual(bundle['results'][0]['patch'],[])
        self.assertFalse(any('/git/ref/' in url or '/git/commits/' in url for url,_ in self.network.calls))
        self.assertEqual(bundle['summary']['docs_completed'],0)
        self.assertEqual(bundle['summary']['ci_completed'],1)
        replayed,after,_=pipeline.replay([records[0]],state,bundle)
        self.assertEqual(replayed,[records[0]])
        self.assertGreater(after['records']['a']['ci_checked_at'],state['records']['a']['ci_checked_at'])
        self.assertEqual(after['records']['a']['docs_checked_at'],state['records']['a']['docs_checked_at'])
        self.assertEqual(after['records']['a']['last_attempt_at'],state['records']['a']['last_attempt_at'])

    def test_empty_document_result_is_also_cached(self):
        self.network.document=None
        bundle,_=self.collect(records=[self.records[0]])
        records,state,_=pipeline.replay([self.records[0]],self.state,bundle)
        self.network.calls=[]
        again,budget=self.collect(records=records,state=state,now=NOW+timedelta(days=31))
        self.assertEqual(budget.requests,2)
        self.assertEqual(again['results'][0]['patch'],[])

    def test_ci_error_does_not_turn_into_successful_empty_result(self):
        records,state=self.complete_one()
        self.network.failure='/actions/runs?'
        bundle,_=self.collect(records=[records[0]],state=state,now=NOW+timedelta(days=31))
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
        self.assertEqual(bundle['summary']['ci_completed'],1)
        self.assertEqual(bundle['summary']['docs_completed'],0)

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
        bundle,_=self.collect(records=[records[0]],state=state,now=NOW+timedelta(days=31))
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
        with patch.object(pipeline,'sync_material',return_value=False), patch('validate_site_data.validate',side_effect=ValueError('invalid staged data')):
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
        with patch.object(pipeline,'sync_material',return_value=False), patch('validate_site_data.validate'):
            pipeline.apply_bundle(self.root,bundle)
        git('add','data',pipeline.STATE);git('commit','-qm','results and progress')
        paths=git('diff','--name-only','HEAD^','HEAD').splitlines()
        self.assertIn(pipeline.STATE,paths)
        self.assertIn('data/projects.index.json',paths)
        with patch.object(pipeline,'sync_material',return_value=False), patch('validate_site_data.validate'):
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
        bundle,_=self.collect(records=[records[0]],state=state,now=NOW+timedelta(days=31))
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


    def test_redirect_hops_count_toward_request_budget(self):
        def redirects(request,timeout):
            raise HTTPError(request.full_url,302,'Moved',{'Location':request.full_url+'x'},None)
        budget=pipeline.Budget(requests=2)
        client=pipeline.Client(budget,opener=redirects)
        with self.assertRaises(pipeline.BudgetStop):
            client.get('https://api.github.com/repos/owner/a/git/ref/heads/main','head')
        self.assertEqual(budget.requests,2)
        self.assertEqual(budget.statuses,{'302':2})

    def test_unsupported_redirect_is_deferred_without_following_it(self):
        def redirects(request,timeout):
            raise HTTPError(request.full_url,302,'Moved',{'Location':'https://unrelated.invalid/path'},None)
        budget=pipeline.Budget(requests=20)
        client=pipeline.Client(budget,opener=redirects)
        with self.assertRaisesRegex(pipeline.FetchFailure,'unsupported redirect'):
            client.get('https://api.github.com/repos/owner/a/git/ref/heads/main','head')
        self.assertEqual(budget.requests,1)


    def test_material_promotions_record_activity_and_keep_pages_publishable(self):
        from record_project_activity import snapshot
        from refresh_scope import check_publishable
        source=Path(__file__).resolve().parents[1]
        shutil.rmtree(self.root/'data')
        shutil.copytree(source/'data',self.root/'data')
        (self.root/'state').mkdir(exist_ok=True)
        for name in ('github-poll-state.json','project-catalog-state.json'):
            shutil.copy2(source/'state'/name,self.root/'state'/name)
        records=load_projects(self.root/'data/projects.json')
        # Isolate promotion recording from pending live catalogue migrations.
        baseline=json.loads((self.root/'state/project-catalog-state.json').read_bytes())
        baseline['projects']={r['id']:snapshot(r) for r in records}
        (self.root/'state/project-catalog-state.json').write_bytes(encode(baseline))
        before=next(r for r in records if (r.get('build') or {}).get('compilable') is None)
        after=copy.deepcopy(before);after.setdefault('build',{})['compilable']=True
        bundle={'version':1,'results':[{'id':before['id'],'fingerprint':pipeline.fingerprint(before),
            'guards':[{'path':list(path),'before':pipeline.value_at(before,path)} for path in pipeline.OWNED],
            'patch':pipeline.patch_between(before,after),'state_before':{},
            'state_after':{'fingerprint':pipeline.fingerprint(before),'last_attempt_at':pipeline.stamp(NOW)}}]}
        pipeline.apply_bundle(self.root,bundle)
        updated=load_projects(self.root/'data/projects.json')
        catalogue=json.loads((self.root/'state/project-catalog-state.json').read_bytes())
        # This fixture tests material recording independently of the live backlog.
        check_publishable({'repositories':{}},updated,catalogue)
        activity=json.loads((self.root/'data/activity.json').read_bytes())
        self.assertTrue(any(e.get('type')=='project_updated' and e['project_id']==before['id'] for e in activity['events']))
        self.assertTrue(catalogue['projects'][before['id']]['build']['compilable'])

    def test_pending_material_baseline_cannot_be_blessed_by_enrichment(self):
        from record_project_activity import snapshot
        staged=Path(self.temp.name)/'stage';staged.mkdir()
        (self.root/'state').mkdir(exist_ok=True)
        (self.root/'state/project-catalog-state.json').write_bytes(encode({'projects':{}}))
        after=copy.deepcopy(self.records);after[0]['build']['compilable']=True
        with self.assertRaises(pipeline.PublicationPending):
            pipeline.sync_material(staged,self.root,self.records,after)
        self.assertFalse((staged/'state').exists())


    def metadata(self, records):
        return {pipeline.identity(r)['repo']:{
            'last_seen_pushed_at':pipeline.stamp(NOW-timedelta(days=1)),
            'last_probe_at':pipeline.stamp(NOW-timedelta(hours=1)),
            'last_deep_scan':pipeline.stamp(NOW-timedelta(hours=2)),
            'scan_requested':False, 'branches':{'main':{'tip_sha':SHA}}} for r in records}

    def test_warm_ci_services_sixty_records_with_sixty_requests_and_no_heads(self):
        records=[project(f'w{i:03}') for i in range(200)]
        state={'version':1,'records':{r['id']:{
            'fingerprint':pipeline.fingerprint(r),'docs_checked_at':pipeline.stamp(NOW),
            'ci_fingerprint':pipeline.fingerprint(r),'ci_checked_at':pipeline.stamp(NOW-timedelta(days=8))} for r in records}}
        bundle,budget=self.collect(records=records,state=state,limit=None)
        self.assertEqual(bundle['summary']['ci_completed'],60)
        self.assertEqual(bundle['summary']['docs_completed'],0)
        self.assertEqual(bundle['summary']['completed'],60)
        self.assertEqual(budget.requests,60);self.assertEqual(budget.api_requests,60)
        self.assertTrue(all('/actions/runs?' in url for url,_ in self.network.calls))

    def test_cold_backlog_uses_separate_ci_and_document_capacity(self):
        records=[project(f'cold{i:03}') for i in range(200)]
        bundle,budget=self.collect(records=records,limit=None)
        self.assertEqual(bundle['summary']['ci_completed'],60)
        self.assertEqual(bundle['summary']['docs_completed'],9)
        self.assertLessEqual(budget.requests,300);self.assertLessEqual(budget.api_requests,80)
        self.assertGreater(bundle['summary']['attempted'],20)
        replayed,state,_=pipeline.replay(records,self.state,bundle)
        self.assertEqual(sum('ci_checked_at' in e for e in state['records'].values()),60)
        self.assertEqual(sum('docs_checked_at' in e for e in state['records'].values()),9)
        next_ci=pipeline.select(replayed,state,NOW,work='ci')
        self.assertEqual(next_ci[0]['id'],'cold060')

    def test_priority_shares_reserve_oldest_overdue_work_under_changed_flood(self):
        changed=[project(f'changed{i:03}') for i in range(100)]
        old=[project(f'overdue{i:03}') for i in range(100)]
        records=changed+old;state={'version':1,'records':{}}
        for r in records:
            fp=pipeline.digest('previous version') if r in changed else pipeline.fingerprint(r)
            state['records'][r['id']]={'fingerprint':fp,'ci_fingerprint':fp,
                'docs_checked_at':pipeline.stamp(NOW-timedelta(days=31)),
                'ci_checked_at':pipeline.stamp(NOW-timedelta(days=8)),
                'last_attempt_at':pipeline.stamp(NOW-timedelta(days=2)),
                'ci_attempt_at':pipeline.stamp(NOW-timedelta(days=2))}
        bundle,budget=self.collect(records=records,state=state,limit=None)
        done=lambda prefix,work:sum(r['id'].startswith(prefix) and r['work'].get(work)=='complete' for r in bundle['results'])
        self.assertEqual(done('changed','ci'),15)
        self.assertEqual(done('overdue','ci'),45)
        self.assertEqual(done('changed','docs'),4)
        self.assertEqual(done('overdue','docs'),5)
        self.assertLessEqual(budget.requests,300);self.assertLessEqual(budget.api_requests,80)
        self.assertTrue(next(r for r in bundle['results'] if r['id']=='changed000')['work']['docs']=='complete')

    def test_completed_poll_metadata_reuses_immutable_tip_without_head_request(self):
        record=project('meta');record['github']={'latest_commit':{'sha':'b'*40}}
        polling=self.metadata([record])
        bundle,budget=self.collect(records=[record],polling=polling,limit=None)
        self.assertEqual(bundle['summary']['docs_completed'],1)
        self.assertFalse(any('/git/ref/' in url for url,_ in self.network.calls))
        item=bundle['results'][0]
        after,_,_=pipeline.replay([record],self.state,bundle,polling=polling)
        self.assertIn(SHA,after[0]['evidence']['automated']['compilable'][0]['url'])
        self.assertEqual(budget.requests,25)  # one CI + twenty-four scoped document/configuration paths

    def test_cached_tip_all_missing_requires_accessible_same_commit(self):
        records, state = self.complete_one()
        record = records[0]
        self.assertTrue(record['build']['compilable'])
        polling = self.metadata([record])
        for status in (404, 403, 500):
            with self.subTest(status=status):
                self.network.document = None
                self.network.confirm_status = status
                budget = pipeline.Budget(600, 300, clock=self.network.clock)
                client = pipeline.Client(budget, opener=self.network.open, token='')
                before = copy.deepcopy(record)
                with self.assertRaises(pipeline.FetchFailure):
                    pipeline.collect_record(record, {}, client, NOW, polling=polling)
                self.assertEqual(record, before)
                self.assertEqual(budget.requests, 25)
                self.assertEqual(budget.api_requests, 1)
                self.assertIn('/git/commits/' + SHA, self.network.calls[-1][0])
        # A successful response for a different commit cannot establish absence.
        self.network.confirm_status = 200
        self.network.confirm_sha = 'b' * 40
        client = pipeline.Client(pipeline.Budget(600, 300), opener=self.network.open, token='')
        with self.assertRaises(pipeline.FetchFailure):
            pipeline.collect_record(record, {}, client, NOW, polling=polling)

    def test_cached_tip_confirmed_removed_documents_retract_only_automated_claims(self):
        records, _ = self.complete_one()
        record = records[0]
        self.network.document = None
        client = pipeline.Client(pipeline.Budget(600, 300), opener=self.network.open, token='')
        after, state = pipeline.collect_record(record, {}, client, NOW, polling=self.metadata([record]))
        self.assertIsNone(after['build']['compilable'])
        self.assertIsNone(after['build']['playable'])
        self.assertEqual(after['evidence']['curated'], record['evidence']['curated'])
        self.assertEqual(state['docs_checked_at'], pipeline.stamp(NOW))
        self.assertIn(('owner/a', SHA), client.accessible_commits)
        requests = client.budget.requests
        client.confirm_commit(pipeline.identity(record), SHA)
        self.assertEqual(client.budget.requests, requests)

    def test_confirmation_exhaustion_defers_without_accepting_absence(self):
        records, state = self.complete_one()
        state['records']['a'].pop('docs_key')  # Force a fresh document scan.
        record = records[0]
        self.network.document = None
        for requests, api_requests in ((24, 80), (300, 0)):
            with self.subTest(requests=requests, api_requests=api_requests):
                bundle, budget = self.collect(records=[record], state=state,
                    polling=self.metadata([record]), limit=None, ci_limit=0,
                    requests=requests, api_requests=api_requests)
                self.assertEqual(bundle['summary']['docs_completed'], 0)
                after, after_state, _ = pipeline.replay([record], state, bundle,
                    polling=self.metadata([record]))
                self.assertEqual(after, [record])
                self.assertEqual(after_state['records']['a'].get('docs_checked_at'),
                                 state['records']['a']['docs_checked_at'])
                self.assertEqual(budget.requests, 24)

    def test_pending_stale_or_incomplete_metadata_falls_back_to_head_lookup(self):
        record=project('meta')
        for mutate in [lambda r:r.update(scan_requested=True),
                       lambda r:r.update(last_probe_at=pipeline.stamp(NOW-timedelta(hours=14))),
                       lambda r:r.update(last_deep_scan=pipeline.stamp(NOW-timedelta(days=2))),
                       lambda r:r.update(last_error='previous scan failed'),
                       lambda r:r.update(publication={'metadata_complete':True,'history_complete':False})]:
            polling=self.metadata([record]);mutate(polling[pipeline.identity(record)['repo']])
            self.assertIsNone(pipeline.metadata_commit(record,polling,NOW))
        self.assertIsNone(pipeline.metadata_commit({'id':'x','repo':record['repo'],'github':{'latest_commit':{'sha':SHA}}},{},NOW))

    def test_same_day_push_uses_precise_poll_signal_and_invalidates_replay(self):
        record=project('meta');polling=self.metadata([record])
        bundle,_=self.collect(records=[record],polling=polling,limit=None)
        records,state,_=pipeline.replay([record],self.state,bundle,polling=polling)
        changed=copy.deepcopy(polling)
        changed['owner/meta']['last_seen_pushed_at']=pipeline.stamp(NOW-timedelta(hours=3))
        # Both pushes have the same day; project latest_commit/path are unchanged.
        self.assertNotEqual(pipeline.source_fingerprint(record,polling),pipeline.source_fingerprint(record,changed))
        priority,_=pipeline.queues(records,state,NOW,work='docs',polling=changed)
        self.assertEqual([r['id'] for r in priority],['meta'])
        _,untouched,summary=pipeline.replay([record],self.state,bundle,polling=changed)
        self.assertEqual(untouched,self.state);self.assertEqual(summary['conflicts'],['meta'])

    def test_metadata_cold_scan_cost_supports_ten_documents_per_hour(self):
        records=[project(f'cold{i:03}') for i in range(200)]
        bundle,budget=self.collect(records=records,polling=self.metadata(records),limit=None)
        self.assertEqual(bundle['summary']['ci_completed'],60)
        self.assertEqual(bundle['summary']['docs_completed'],10)
        self.assertEqual(budget.requests,300);self.assertEqual(budget.api_requests,60)

    def test_api_budget_is_independent_of_raw_document_budget(self):
        budget=pipeline.Budget(requests=300,api_requests=1)
        client=pipeline.Client(budget,opener=self.network.open)
        client.ci(pipeline.identity(project('a')),NOW.date().isoformat())
        with self.assertRaises(pipeline.APIStop):client.head(pipeline.identity(project('a')))
        self.assertIsNotNone(client.get('https://raw.githubusercontent.com/owner/a/'+SHA+'/README.md','document',absence=True))
        self.assertEqual(budget.api_requests,1);self.assertEqual(budget.requests,2)

    def test_priority_wall_time_leaves_room_for_oldest_overdue_ci(self):
        records=[project(f'changed{i}') for i in range(20)]+[project(f'old{i}') for i in range(20)]
        state={'version':1,'records':{r['id']:{'ci_fingerprint':pipeline.digest('old') if r['id'].startswith('changed') else pipeline.fingerprint(r),
             'ci_checked_at':pipeline.stamp(NOW-timedelta(days=8))} for r in records}}
        self.network.delay=.3
        bundle,budget=self.collect(records=records,state=state,limit=None,seconds=10,docs_limit=0)
        self.assertGreater(sum(r['id'].startswith('old') and r['work'].get('ci')=='complete' for r in bundle['results']),0)
        self.assertLessEqual(budget.clock(),10.1)


    def test_changed_signal_prioritizes_the_other_unfinished_component(self):
        record=project('cross')
        old=pipeline.digest('older observed source')
        for work,entry in [('docs',{'ci_fingerprint':old}),('ci',{'fingerprint':old})]:
            state={'version':1,'records':{'cross':entry}}
            changed,_=pipeline.queues([record],state,NOW,work=work)
            self.assertEqual([r['id'] for r in changed],['cross'])


    def test_disabling_ci_does_not_steal_manual_document_selection(self):
        sub=project('a-sub');sub['github_path']='game'
        root=project('z-root')
        bundle,_=self.collect(records=[sub,root],ci_limit=0,docs_limit=1,limit=1)
        self.assertEqual([r['id'] for r in bundle['results']],['a-sub'])
        self.assertEqual(bundle['summary']['ci_completed'],0)
        self.assertEqual(bundle['summary']['docs_completed'],1)


    def test_publishing_one_component_keeps_change_priority_for_unfinished_other(self):
        record=project('unfinished');old=pipeline.digest('previous source')
        for completed,missing in [('ci','docs'),('docs','ci')]:
            fp='ci_fingerprint' if completed=='ci' else 'fingerprint'
            state={'version':1,'records':{'unfinished':{fp:old}}}
            bundle,_=self.collect(records=[record],state=state,limit=1,
                docs_limit=0 if completed=='ci' else 1,ci_limit=0 if completed=='docs' else 1)
            records,after,_=pipeline.replay([record],state,bundle)
            changed,_=pipeline.queues(records,after,NOW,work=missing)
            self.assertEqual([r['id'] for r in changed],['unfinished'])
            self.assertNotIn('ci_fingerprint' if missing=='ci' else 'fingerprint',after['records']['unfinished'])


    def test_slice_exhaustion_preserves_queue_position_for_next_slice(self):
        records=[project(f'old{i:03}') for i in range(200)]
        bundle,_=self.collect(records=records,limit=None)
        replayed,state,_=pipeline.replay(records,self.state,bundle)
        deferred=next(r['id'] for r in bundle['results'] if r['work'].get('docs')=='deferred')
        self.assertNotIn('last_attempt_at',state['records'][deferred])
        self.assertEqual(pipeline.select(replayed,state,NOW,work='docs')[0]['id'],deferred)

    def test_slow_record_is_deferred_with_backoff_before_it_blocks_the_lane(self):
        self.network.delay=4
        bundle,budget=self.collect(records=[self.records[0]],ci_limit=0,limit=1)
        self.assertEqual(bundle['summary']['docs_completed'],0)
        self.assertEqual(bundle['results'][0]['work']['docs_reason'],'record wall-time budget')
        self.assertIn('retry_at',bundle['results'][0]['state_after'])
        self.assertLessEqual(budget.clock(),34)

    def test_due_thresholds_leave_capacity_margin_before_freshness_objectives(self):
        record=project('margin');signal=pipeline.fingerprint(record)
        state={'version':1,'records':{'margin':{'fingerprint':signal,'ci_fingerprint':signal,
            'docs_checked_at':pipeline.stamp(NOW-timedelta(days=10)),
            'ci_checked_at':pipeline.stamp(NOW-timedelta(days=4))}}}
        self.assertEqual(pipeline.select([record],state,NOW,work='ci'),[record])
        self.assertEqual(pipeline.select([record],state,NOW,work='docs'),[record])
        self.assertEqual(pipeline.DOC_TTL+timedelta(days=20),timedelta(days=30))
        self.assertEqual(pipeline.CI_TTL+timedelta(days=3),timedelta(days=7))



class WorkflowTests(unittest.TestCase):
    def test_collection_occurs_once_and_retains_external_bundle(self):
        workflow=(Path(__file__).resolve().parents[1]/'.github/workflows/enrich-evidence.yml').read_text()
        self.assertIn('timeout-minutes: 20',workflow)
        self.assertIn("github.ref == 'refs/heads/main'",workflow)
        self.assertIn('cancel-in-progress: false',workflow)
        self.assertEqual(workflow.count('enrich_evidence.py collect'),1)
        self.assertIn('actions/upload-artifact@v4',workflow)
        self.assertIn('retention-days: 90',workflow)
        self.assertIn('enrichment_handoff.py collect-allowed',workflow)
        self.assertNotIn('enrich_evidence.py apply',workflow)
        self.assertNotIn('sleep ',workflow)
        self.assertIn('$RUNNER_TEMP/enrichment-bundle.json',workflow)
        self.assertIn('--doc-records',workflow)
        self.assertIn('--ci-records',workflow)
        self.assertIn('--api-requests',workflow)
        self.assertNotIn("inputs.records || '20'",workflow)
