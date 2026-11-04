import copy
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import validate_site_data as v

class ProviderValidationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.project = {'id':'p','upstream_name':'P','display_title':'P','subjects':['P'], 'record_class':'subject','target_kinds':['game'], 'work_kinds':['source-restoration'], 'tool_kinds':[]}
        self.event = {'type':'release','date':'2026-11-04T20:00:00Z','project_id':'p','repository':'gitlab.com/g/p','tag':'v1','title':'Version 1','url':'https://gitlab.com/g/p/-/releases/v1'}
    def check(self, events=None):
        path = self.root/'activity.json'
        path.write_text(json.dumps({'generated_at':'2026-11-04T21:00:00Z','events':events or []}))
        with patch.object(v,'load_projects',return_value=[self.project]), patch.object(v,'validate_research_state',return_value=(0,0,0,0)):
            v.validate(self.root/'projects.json',path)
    def test_gitlab_release_and_source_status(self):
        self.project['gitlab']={'source_availability': {'status':'unavailable','http_status':404,'retryable':True,'checked_at':'2026-11-04T20:00:00Z'}}
        self.check([self.event])
    def test_duplicate_release_fails(self):
        with self.assertRaises(SystemExit): self.check([self.event,copy.deepcopy(self.event)])
    def test_bad_status_timestamp_fails(self):
        self.project['gitlab']={'source_availability': {'status':'unavailable','http_status':404,'retryable':True,'checked_at':'nope'}}
        with self.assertRaises(SystemExit): self.check()
if __name__ == '__main__': unittest.main()
