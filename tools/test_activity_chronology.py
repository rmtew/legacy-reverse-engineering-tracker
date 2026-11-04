"""Mixed provider offsets/precision must never change chronology or identities."""
import copy
from datetime import datetime, timezone
import json
from pathlib import Path
import tempfile
import unittest

from activity_history import compact_history, parse_time, write_activity


class ActivityChronologyTests(unittest.TestCase):
    def event(self, sha, when, **extra):
        return {'type': 'commit', 'date': when, 'project_id': 'p', 'repository': 'gitlab.com/group/repo',
                'sha': sha, 'title': sha, 'url': 'https://gitlab.com/group/repo/-/commit/' + sha, **extra}

    def test_mixed_offsets_and_fractional_seconds_order_actual_instants(self):
        events = [self.event('utc', '2026-10-31T02:53:29.000+00:00'),
                  self.event('newer', '2026-10-30T22:56:14.000-04:00'),
                  self.event('whole', '2026-10-31T02:56:14Z'),
                  self.event('fraction', '2026-10-31T02:56:14.001Z'),
                  self.event('positive', '2026-10-31T10:55:00+08:00')]
        original = copy.deepcopy(events)
        result = compact_history(events, datetime(2026, 11, 4, tzinfo=timezone.utc))
        self.assertEqual([e['sha'] for e in result], ['fraction', 'whole', 'newer', 'positive', 'utc'])
        self.assertEqual(events, original)
        self.assertEqual({e['sha']: e['date'] for e in result}, {e['sha']: e['date'] for e in original})
        self.assertEqual(compact_history(result, datetime(2026, 11, 4, tzinfo=timezone.utc)), result)

    def test_daily_summary_latest_uses_chronology_not_offset_clock(self):
        events = [self.event('older', '2026-10-10T10:00:00+02:00'),
                  self.event('newer', '2026-10-10T09:00:00Z')]
        for rows in (events, list(reversed(events))):
            result = compact_history(rows, datetime(2026, 11, 4, tzinfo=timezone.utc))
            self.assertEqual(len(result), 1)
            self.assertEqual(result[0]['shas'], ['newer', 'older'])
            self.assertEqual(result[0]['date'], events[1]['date'])
            self.assertEqual(result[0]['latest_title'], 'newer')
            self.assertEqual(result[0]['latest_url'], events[1]['url'])

    def test_canonical_writer_repairs_any_input_sort_without_rewriting_event_identity(self):
        events = [self.event('old', '2026-11-04T00:30:00+14:00'),
                  {'type': 'release', 'project_id': 'p', 'repository': 'gitlab.com/group/repo',
                   'tag': 'v1', 'date': '2026-11-03T23:00:00-02:00', 'url': 'https://example.org/release'},
                  {'type': 'project_added', 'project_id': 'p', 'date': '2026-11-04T01:15:00.500+00:00', 'title': 'P'},
                  self.event('new', '2026-11-03T23:30:00-02:00')]
        original = copy.deepcopy(events)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'activity.json'
            write_activity(path, {'generated_at': '2026-11-04T12:00:00Z', 'events': events}, [{'id': 'p'}])
            payload = json.loads(path.read_bytes())
            result = payload['events']
            self.assertEqual([e['date'] for e in result], [original[i]['date'] for i in (3, 2, 1, 0)])
            self.assertEqual(next(e['tag'] for e in result if e['type'] == 'release'), 'v1')
            self.assertEqual(events, original)
            first = path.read_bytes()
            write_activity(path, payload, [{'id': 'p'}])
            self.assertEqual(path.read_bytes(), first)


if __name__ == '__main__':
    unittest.main()
