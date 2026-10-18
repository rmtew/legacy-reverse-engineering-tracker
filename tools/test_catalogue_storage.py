"""Storage invariants, migration equality, localized writes and bounded growth."""
import copy
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from catalogue_storage import (FILES, KINDS, REQUEST_LIMIT, bounded, encode, load_all,
    load_dataset, load_git_projects, load_projects, render, request_size, route, storage_paths, write_all)
from cpu_audit_queue import queue
from merge_pending_projects import new_audit

ROOT = Path(__file__).resolve().parents[1]


class StorageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.data = Path(self.temp.name)

    def test_exact_migration_from_git_baseline_and_deterministic_noop(self):
        original = load_all(ROOT / 'data')
        for name in FILES:
            (self.data/name).write_bytes(encode(original[name]))
        self.assertEqual(load_all(self.data), original)
        write_all(self.data, original)
        self.assertEqual(load_all(self.data), original)
        self.assertEqual(write_all(self.data, original), [])
        projects = original['projects.json']
        audits = original['project-audits.json']['projects']
        self.assertEqual({p['id'] for p in projects}, {a['project_id'] for a in audits})
        self.assertTrue(all(request_size((self.data/p).read_bytes()) <= REQUEST_LIMIT for p in storage_paths(self.data)))

    def test_explicit_legacy_filename_is_honored_with_or_without_sibling_catalogue(self):
        custom = self.data / 'custom-projects.json'
        records = [{'id':'explicit-legacy','nested':{'value':None}}]
        custom.write_bytes(encode(records))
        self.assertEqual(load_projects(custom), records)
        canonical = [{'id':'canonical-sibling'}]
        write_all(self.data, {'projects.json':canonical})
        self.assertEqual(load_projects(custom), records)
        self.assertEqual(load_projects(self.data/'projects.json'), canonical)
        self.assertEqual(load_projects(self.data/'projects.index.json'), canonical)

    def test_explicit_legacy_filename_never_falls_back_to_sibling_catalogue(self):
        write_all(self.data, {'projects.json':[{'id':'canonical-sibling'}]})
        custom = self.data / 'custom-projects.json'
        with self.assertRaises(FileNotFoundError):
            load_projects(custom)
        custom.write_text('invalid json')
        with self.assertRaises(json.JSONDecodeError):
            load_projects(custom)

    def test_one_record_changes_only_partition_and_index(self):
        records = [{'id':str(i), 'note':'original'} for i in range(1000)]
        write_all(self.data, {'projects.json':records})
        records[12]['note']='reviewed'
        self.assertEqual(set(write_all(self.data, {'projects.json':records})),
                         {'projects.index.json',f'projects/{route("12")[:1]}.json'})
        self.assertEqual(load_projects(self.data/'projects.json'), records)
        self.assertEqual(write_all(self.data, {'projects.json':records}), [])

    def test_growth_splits_only_overflowing_hash_prefix(self):
        ids = [str(i) for i in range(2000)]
        same = [pid for pid in ids if route(pid).startswith('ab')][:3]
        self.assertEqual(len(same),3)
        records = [{'id':pid,'text':'x'*500} for pid in same] + [{'id':'unrelated'}]
        output = render('projects.json', records, limit=1400)
        paths = [p for p in output if p.startswith('projects/ab')]
        self.assertTrue(paths)
        self.assertNotIn('projects/ab.json',output)
        self.assertTrue(all(request_size(b)<=1400 for b in output.values()))
        other = f'projects/{route("unrelated")[:1]}.json'
        self.assertIn(other,output)
        with self.assertRaisesRegex(ValueError,'oversized record'):
            render('projects.json',[{'id':'huge','text':'"\\'*2000}],limit=1400)
        with self.assertRaisesRegex(ValueError,'projects.index.json'):
            render('projects.json',[{'id':str(i)} for i in range(1000)],limit=1400)
        with self.assertRaisesRegex(ValueError,'exceeds'):
            bounded(encode({'id':'"'*1000}), 'escaped',limit=1500)

    def test_legacy_is_read_only_and_mixed_layout_rejected(self):
        value = [{'id':'old','all':None,'nested':{'yes':[1,True,'🦊']}}]
        (self.data/'projects.json').write_bytes(encode(value))
        self.assertEqual(load_projects(self.data/'projects.json'),value)
        changed = write_all(self.data,{'projects.json':value})
        self.assertIn('projects.json',changed)
        self.assertFalse((self.data/'projects.json').exists())
        (self.data/'projects.json').write_bytes(encode(value))
        with self.assertRaisesRegex(ValueError,'mixed'):
            load_projects(self.data/'projects.json')

    def test_invalid_missing_and_traversing_shard_references(self):
        write_all(self.data,{'projects.json':[{'id':'one'}]})
        path = self.data/'projects.index.json'
        original = json.loads(path.read_bytes())
        shard = self.data/original['shards'][0]['path']
        content = shard.read_bytes()
        for bad in ['../projects.json','/projects/ab.json','projects/../../secret','projects/AB.json']:
            index = copy.deepcopy(original);index['shards'][0]['path']=bad;path.write_bytes(encode(index))
            with self.assertRaisesRegex(ValueError,'Invalid shard reference'):
                load_projects(self.data/'projects.json')
        path.write_bytes(encode(original));shard.unlink()
        with self.assertRaises(FileNotFoundError):load_projects(self.data/'projects.json')
        shard.write_bytes(content+b' ')
        with self.assertRaisesRegex(ValueError,'digest'):load_projects(self.data/'projects.json')
        shard.write_bytes(content)
        index=copy.deepcopy(original);index['order'].append('missing');path.write_bytes(encode(index))
        with self.assertRaisesRegex(ValueError,'coverage'):load_projects(self.data/'projects.json')
        path.write_bytes(encode(original))
        index=copy.deepcopy(original);index['shards']=[None];path.write_bytes(encode(index))
        with self.assertRaisesRegex(ValueError,'Invalid shard reference'):load_projects(self.data/'projects.json')
        path.write_bytes(encode(original));shard.unlink()
        with tempfile.NamedTemporaryFile() as external:
            shard.symlink_to(external.name)
            with self.assertRaisesRegex(ValueError,'escapes data directory'):load_projects(self.data/'projects.json')

    def test_pending_placeholder_and_cpu_queue(self):
        import merge_pending_projects as pending
        records=[{'id':'existing','title':'Existing'}]
        audits={'indexed_at':'2026-10-01','projects':[new_audit('existing')]}
        write_all(self.data,{'projects.json':records,'project-audits.json':audits})
        path=self.data/'pending-projects.json'
        path.write_bytes(encode([{'id':'new','title':'New','source_cpu':[],'target_cpu':[]}]))
        with patch.multiple(pending,PROJECTS=self.data/'projects.json',AUDITS=self.data/'project-audits.json',PENDING=path):pending.main()
        records=load_projects(self.data/'projects.json')
        audits=load_dataset(self.data,'project-audits.json')['projects']
        self.assertEqual({r['id'] for r in queue(records,audits)},{'existing','new'})
        self.assertEqual(json.loads(path.read_bytes()),[])
        self.assertFalse((self.data/'projects.json').exists())

    def test_historical_git_loader_accepts_each_layout_and_rejects_mixed(self):
        root=self.data
        def git(*args):return subprocess.check_output(['git',*args],cwd=root,stderr=subprocess.DEVNULL).decode().strip()
        git('init','-q');git('config','user.email','test@example.invalid');git('config','user.name','Test')
        data=root/'data';data.mkdir()
        records=[{'id':'historical','value':None}]
        (data/'projects.json').write_bytes(encode(records))
        git('add','.');git('commit','-qm','legacy');legacy=git('rev-parse','HEAD')
        write_all(data,{'projects.json':records})
        git('add','-A');git('commit','-qm','partitioned');current=git('rev-parse','HEAD')
        self.assertEqual(load_git_projects(legacy,root),records)
        self.assertEqual(load_git_projects(current,root),records)
        (data/'projects.json').write_bytes(encode(records))
        git('add','.');git('commit','-qm','ambiguous')
        with self.assertRaisesRegex(ValueError,'mixed'):load_git_projects('HEAD',root)

    def test_split_cleanup_deletes_obsolete_partitions_and_keeps_noop_stable(self):
        ids=[str(i) for i in range(2000) if route(str(i)).startswith('ab')][:3]
        records=[{'id':pid,'note':'x'*500} for pid in ids]
        split=render('projects.json',records,limit=1400)
        for path,content in split.items():
            target=self.data/path;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(content)
        obsolete={p for p in split if p.startswith('projects/')}
        changed=write_all(self.data,{'projects.json':records})
        self.assertTrue(obsolete.issubset(changed))
        self.assertTrue(all(not (self.data/p).exists() for p in obsolete))
        self.assertEqual(load_projects(self.data/'projects.json'),records)
        self.assertEqual(write_all(self.data,{'projects.json':records}),[])
