"""Public GitLab collection and provider-isolated durable scheduler contracts."""
import copy
from datetime import timedelta
from io import BytesIO
import unittest
from unittest.mock import patch
from urllib.error import HTTPError
from urllib.parse import parse_qs, urlsplit

import refresh_pipeline as pipeline
import refresh_gitlab as gitlab
from repository_provider import repository, provider, metadata
from catalogue_storage import encode, load_projects, write_projects
from record_project_activity import snapshot
import test_refresh_pipeline as fixtures
from test_refresh_pipeline import Network, Response, project, commit, NOW, SHA

KEY = 'gitlab.com/group/subgroup/project'


def glproject(pid='gl', **extra):
    row = project(pid, repo='https://' + KEY, **extra)
    row.pop('github', None)
    return row


def glcommit(index=1, when='2026-10-18T12:00:00Z'):
    return {'id': f'{index:040x}', 'committed_date': when, 'title': f'GL {index}', 'author_name': 'Someone'}


def release(tag, when='2026-10-18T12:00:00Z'):
    return {'tag_name': tag, 'released_at': when, 'name': 'Release ' + tag,
            '_links': {'self': 'https://gitlab.com/api/v4/projects/1/releases/' + tag}}


class GitLabNetwork(Network):
    def __init__(self):
        super().__init__()
        self.gl_pages, self.releases = {1: [glcommit()]}, {1: [release('v1')]}
        self.errors = {}
        self.head = glcommit(500)
        self.branches = None
        self.by_ref = {}
        self.response_headers = {}
        self.root_headers = {}
        self.default_branch = 'main'
        self.requests = []

    def open(self, request, timeout):
        if urlsplit(request.full_url).hostname != 'gitlab.com':
            return super().open(request, timeout)
        self.calls.append((request.full_url, timeout))
        self.requests.append(request)
        self.time += self.delay
        url = urlsplit(request.full_url)
        suffix = url.path.split('/projects/', 1)[1].split('/', 1)
        path = '/' + suffix[1] if len(suffix) > 1 else ''
        query = parse_qs(url.query)
        if path in self.errors:
            code = self.errors[path]
            raise HTTPError(request.full_url, code, 'test failure', self.response_headers, BytesIO())
        if not path:
            value = {'default_branch': self.default_branch, 'created_at': '2020-01-01T00:00:00Z', 'archived': False}
        elif path == '/repository/branches':
            value = self.branches.get(int(query.get('page', ['1'])[0]), []) if self.branches is not None else [{'name': 'main', 'commit': self.head}]
        elif path.startswith('/repository/branches/'):
            value = {'name': path.rsplit('/', 1)[1], 'commit': self.head}
        elif path == '/repository/commits':
            value = self.by_ref.get(query.get('ref_name', [''])[0], self.gl_pages.get(int(query.get('page', ['1'])[0]), []))
        elif path == '/releases':
            value = self.releases.get(int(query.get('page', ['1'])[0]), [])
        else:
            raise AssertionError(request.full_url)
        result = Response(encode(value))
        result.headers = self.root_headers if not path else self.response_headers
        return result


class GitLabTests(unittest.TestCase):
    setUp = fixtures.RefreshPipelineTests.setUp
    seed = fixtures.RefreshPipelineTests.seed
    put = fixtures.RefreshPipelineTests.put
    read = fixtures.RefreshPipelineTests.read
    collect = fixtures.RefreshPipelineTests.collect
    apply = fixtures.RefreshPipelineTests.apply

    def setup_gitlab(self, records=None, state=None):
        self.net = GitLabNetwork()
        self.stack.enter_context(patch('record_project_activity.NOW', NOW))
        self.stack.enter_context(patch('record_project_activity.NOW_ISO', pipeline.stamp(NOW)))
        self.stack.enter_context(patch('record_project_activity.CUTOFF', NOW - timedelta(days=30)))
        self.stack.enter_context(patch.object(gitlab, 'REQUEST_DELAY', 0))
        self.seed(records or [glproject()], state)

    def activity_state(self, **extra):
        row = glproject(gitlab={'repository': KEY, 'default_branch': 'main', 'tracking_branch': 'main'})
        self.setup_gitlab([row], {KEY: {'last_probe_at': pipeline.stamp(NOW), 'default_branch': 'main',
            'scan_requested': True, 'last_release_check_at': pipeline.stamp(NOW), **extra}})

    def test_nested_root_identity_and_non_project_urls(self):
        self.assertEqual(repository(glproject()), KEY)
        for suffix in ('/-/tree/main', '/-/commits/main', '?x=1', '#readme'):
            self.assertIsNone(repository({'repo': 'https://' + KEY + suffix}))
        self.assertIsNone(repository({'repo': 'https://gitlab.example/group/repo'}))
        self.assertEqual(provider(KEY), 'gitlab')
        self.assertEqual(metadata({'gitlab': {'repository': KEY}}), {'repository': KEY})

    def test_collects_commits_and_releases_atomically_without_token(self):
        self.setup_gitlab()
        result = self.collect(full=True)
        self.assertEqual(result['summary']['completed'], {'probe': 1, 'activity': 1, 'releases': 1})
        self.assertNotIn('gitlab', load_projects(self.root / 'data/projects.json')[0])
        self.apply(result)
        row = load_projects(self.root / 'data/projects.json')[0]
        self.assertEqual(row['gitlab']['repository'], KEY)
        self.assertEqual(row['gitlab']['latest_release']['tag'], 'v1')
        self.assertEqual(row['gitlab']['latest_commit']['sha'], self.net.head['id'])
        events = self.read('data/activity.json')['events']
        self.assertEqual({e['type'] for e in events}, {'commit', 'release'})
        self.assertEqual(next(e['url'] for e in events if e['type'] == 'release'), 'https://' + KEY + '/-/releases/v1')
        self.assertTrue(all('Authorization' not in req.headers and 'Private-token' not in req.headers for req in self.net.requests))
        self.assertIn('group%2Fsubgroup%2Fproject', self.net.calls[0][0])

    def test_pinned_pages_resume_and_failure_never_advances_cursor(self):
        self.activity_state()
        self.net.gl_pages = {1: [glcommit(i) for i in range(100)], 2: [glcommit(101)]}
        first = self.collect(requests=2)
        self.apply(first)
        cursor = self.read(pipeline.POLL)['repositories'][KEY]['refresh_activity']
        self.assertEqual(cursor['queries'][0]['page'], 2)
        self.assertEqual(len(self.read('data/activity.json')['events']), 100)
        self.net.errors['/repository/commits'] = 500
        failed = self.collect(requests=1, now=NOW + timedelta(minutes=1))
        self.apply(failed)
        self.assertEqual(self.read(pipeline.POLL)['repositories'][KEY]['refresh_activity'], cursor)
        self.assertEqual(len(self.read('data/activity.json')['events']), 100)
        self.net.errors.clear()
        self.net.head = glcommit(999)
        self.net.calls.clear()
        final = self.collect(requests=1, now=NOW + timedelta(minutes=10))
        self.apply(final)
        self.assertEqual(len(self.net.calls), 1)
        self.assertIn('ref_name=' + glcommit(500)['id'], self.net.calls[0][0])
        self.assertIn('page=2', self.net.calls[0][0])
        self.assertEqual(len(self.read('data/activity.json')['events']), 101)

    def test_non_monotonic_dates_do_not_stop_pagination_and_changed_tip_rescans_window(self):
        self.activity_state()
        self.net.gl_pages = {1: [glcommit(i, '2026-09-01T00:00:00Z') for i in range(100)],
                             2: [glcommit(101)]}
        self.apply(self.collect())
        self.assertIn(glcommit(101)['id'], [e.get('sha') for e in self.read('data/activity.json')['events']])
        self.net.calls.clear()
        self.net.head = glcommit(999, '2001-01-01T00:00:00Z')
        self.net.gl_pages = {1: [glcommit(102, '2026-09-25T00:00:00Z')]}
        self.apply(self.collect(now=NOW + timedelta(hours=1)))
        request = next(url for url, _ in self.net.calls if '/repository/commits?' in url)
        self.assertIn('since=2026-09-19', request)
        row = load_projects(self.root / 'data/projects.json')[0]
        self.assertEqual(row['gitlab']['latest_commit']['date'], '2001-01-01')
        self.assertTrue(any(glcommit(102)['id'] in e.get('shas', []) for e in self.read('data/activity.json')['events']))

    def test_releases_checked_without_push_and_multiple_tags_preserved(self):
        self.setup_gitlab()
        self.apply(self.collect())
        self.net.calls.clear()
        self.net.releases = {1: [release('v3'), release('v2'), release('v1')]}
        self.apply(self.collect(now=NOW + timedelta(hours=1)))
        self.assertTrue(any('/releases?' in url for url, _ in self.net.calls))
        self.assertFalse(any('/repository/commits?' in url for url, _ in self.net.calls))
        self.assertEqual({e['tag'] for e in self.read('data/activity.json')['events'] if e['type'] == 'release'}, {'v1', 'v2', 'v3'})
        self.assertEqual(len([e for e in self.read('data/activity.json')['events'] if e['type'] == 'commit']), 1)

    def test_future_release_skipped(self):
        self.setup_gitlab()
        self.net.releases = {1: [release('future', '2026-12-01T00:00:00Z'), release('v1')]}
        self.apply(self.collect())
        self.assertEqual(load_projects(self.root / 'data/projects.json')[0]['gitlab']['latest_release']['tag'], 'v1')
        self.assertNotIn('future', [e.get('tag') for e in self.read('data/activity.json')['events']])

    def test_gitlab_429_never_blocks_github(self):
        self.setup_gitlab([glproject(), project('a')])
        self.net.errors[''] = 429
        self.net.response_headers = {'Retry-After': '3600'}
        result = self.collect(full=True)
        self.assertIn('gitlab', result['progress_after']['provider_blocked_until'])
        self.assertNotIn('github', result['progress_after']['provider_blocked_until'])
        self.assertEqual(result['summary']['completed']['probe'], 1)
        self.assertEqual(result['summary']['completed']['activity'], 1)
        self.assertTrue(any(url.startswith('https://api.github.com/') for url, _ in self.net.calls))
        self.apply(result)
        self.net.calls.clear()
        self.collect(now=NOW + timedelta(minutes=1))
        self.assertFalse(any(url.startswith('https://gitlab.com/') for url, _ in self.net.calls))

    def test_github_cooldown_does_not_block_gitlab(self):
        self.setup_gitlab([glproject(), project('a')])
        self.put(pipeline.PROGRESS, {'version': 1, 'revision': 0, 'cycle': None,
            'retry': {'probe': {}, 'activity': {}}, 'blocked_until': pipeline.stamp(NOW + timedelta(hours=1))})
        result = self.collect(full=True)
        self.assertEqual(result['summary']['completed'], {'probe': 1, 'activity': 1, 'releases': 1})
        self.assertFalse(any(url.startswith('https://api.github.com/') for url, _ in self.net.calls))

    def test_hourly_budget_persists_across_continuations_and_no_boundary_burst(self):
        self.activity_state()
        self.net.gl_pages = {1: [glcommit(i) for i in range(100)], 2: [glcommit(101)]}
        with patch.dict(pipeline.HOURLY_LIMITS, {'gitlab': 2}):
            first = self.collect(requests=2, now=NOW + timedelta(minutes=59))
            self.apply(first, now=NOW + timedelta(minutes=59))
            self.net.calls.clear()
            second = self.collect(requests=2, now=NOW + timedelta(hours=1))
            self.apply(second, now=NOW + timedelta(hours=1))
            self.assertEqual(self.net.calls, [])
            self.assertFalse(pipeline.status(pipeline.progress_read(self.root), NOW + timedelta(hours=1))['eligible'])
            third = self.collect(requests=2, now=NOW + timedelta(hours=2, minutes=1))
            self.assertGreater(third['summary']['requests'], 0)

    def test_branch_and_path_filters_are_sent_and_attributed(self):
        self.setup_gitlab([glproject(gitlab_branch='feature/topic', gitlab_path='src/game')])
        self.apply(self.collect())
        urls = [url for url, _ in self.net.calls]
        self.assertTrue(any('/branches/feature%2Ftopic' in url for url in urls))
        self.assertTrue(any('path=src%2Fgame' in url for url in urls))
        commits = [e for e in self.read('data/activity.json')['events'] if e['type'] == 'commit']
        self.assertEqual(commits[0]['branches'], ['feature/topic'])

    def test_root_404_retains_facts_and_only_root_failure_marks_unavailable(self):
        self.setup_gitlab()
        self.apply(self.collect())
        prior = load_projects(self.root / 'data/projects.json')[0]
        self.net.errors[''] = 404
        self.net.calls.clear()
        self.apply(self.collect(now=NOW + timedelta(days=1)))
        current = load_projects(self.root / 'data/projects.json')[0]
        self.assertEqual(current['gitlab']['latest_commit'], prior['gitlab']['latest_commit'])
        self.assertEqual(current['gitlab']['checked_at'], prior['gitlab']['checked_at'])
        self.assertEqual(current['gitlab']['source_availability']['http_status'], 404)
        self.assertFalse(any('/releases?' in url or '/commits?' in url for url, _ in self.net.calls))
        self.net.errors.clear()
        self.apply(self.collect(now=NOW + timedelta(days=2)))
        self.assertNotIn('source_availability', load_projects(self.root / 'data/projects.json')[0]['gitlab'])
        self.net.errors['/repository/branches'] = 404
        self.apply(self.collect(now=NOW + timedelta(days=2, hours=1)))
        self.assertNotIn('source_availability', load_projects(self.root / 'data/projects.json')[0]['gitlab'])

    def test_github_successful_root_survives_optional_metadata_budget_stop(self):
        self.setup_gitlab([project('a')], {'owner/a': {'last_seen_pushed_at': '2026-10-16T00:00:00Z'}})
        result = self.collect(requests=1)
        self.apply(result)
        rs = self.read(pipeline.POLL)['repositories']['owner/a']
        self.assertEqual(rs['last_seen_pushed_at'], '2026-10-18T00:00:00Z')
        self.assertTrue(rs['scan_requested'])
        self.assertIn('owner/a', pipeline.progress_read(self.root)['cycle']['pending']['activity'])

    def test_stale_public_unavailable_flag_requires_fresh_root_verification(self):
        row = project('a')
        row['github']['source_availability'] = {'status': 'unavailable', 'http_status': 404, 'retryable': True}
        self.setup_gitlab([row], {'owner/a': {'last_probe_at': pipeline.stamp(NOW), 'last_deep_scan': pipeline.stamp(NOW),
                                             'next_probe_due_at': pipeline.stamp(NOW + timedelta(hours=12))}})
        self.apply(self.collect(requests=0))
        self.assertIn('source_availability', load_projects(self.root / 'data/projects.json')[0]['github'])
        self.assertTrue(self.read(pipeline.POLL)['repositories']['owner/a']['availability_recheck_requested'])
        self.assertEqual(self.net.calls, [])
        self.apply(self.collect())
        self.assertTrue(any('/repos/owner/a' in url for url, _ in self.net.calls))
        self.assertNotIn('source_availability', load_projects(self.root / 'data/projects.json')[0]['github'])
        self.assertNotIn('availability_recheck_requested', self.read(pipeline.POLL)['repositories']['owner/a'])

    def test_all_branch_enumeration_resumes_and_dedupes_shared_commits(self):
        self.activity_state()
        self.net.branches = {1: [{'name': 'main', 'commit': self.net.head}] * 100,
                             2: [{'name': 'feature', 'commit': glcommit(600)}]}
        self.apply(self.collect(requests=1))
        cursor = self.read(pipeline.POLL)['repositories'][KEY]['refresh_activity']
        self.assertEqual(cursor['branch_page'], 2)
        self.net.calls.clear()
        self.apply(self.collect(requests=10, now=NOW + timedelta(minutes=1)))
        self.assertTrue(any('/repository/branches?page=2' in url for url, _ in self.net.calls))
        self.assertFalse(any('/repository/branches?page=1' in url for url, _ in self.net.calls))
        event = next(e for e in self.read('data/activity.json')['events'] if e['type'] == 'commit')
        self.assertEqual(event['branches'], ['feature', 'main'])
        self.assertEqual(set(self.read(pipeline.POLL)['repositories'][KEY]['branches']), {'main', 'feature'})

    def test_path_projects_never_inherit_repo_release(self):
        self.setup_gitlab([glproject('root'), glproject('sub', gitlab_path='src/game')])
        self.apply(self.collect())
        records = {p['id']: p for p in load_projects(self.root / 'data/projects.json')}
        self.assertIn('latest_release', records['root']['gitlab'])
        self.assertNotIn('latest_release', records['sub']['gitlab'])
        self.assertEqual({e['project_id'] for e in self.read('data/activity.json')['events'] if e['type'] == 'release'}, {'root'})

    def test_initial_release_failure_keeps_publication_pending_but_recovers(self):
        from refresh_scope import check_publishable
        self.setup_gitlab()
        self.put('state/project-catalog-state.json', {'version': 1, 'projects': {}, 'removed': {}})
        self.net.errors['/releases'] = 500
        first = self.collect(full=True)
        self.apply(first)
        publication = self.read(pipeline.POLL)['repositories'][KEY]['publication']
        self.assertTrue(publication['metadata_complete'])
        self.assertTrue(publication['history_complete'])
        self.assertFalse(publication['releases_complete'])
        with self.assertRaises(SystemExit):
            check_publishable(self.read(pipeline.POLL), load_projects(self.root / 'data/projects.json'))
        self.net.errors.clear()
        self.apply(self.collect(now=NOW + timedelta(minutes=10)))
        check_publishable(self.read(pipeline.POLL), load_projects(self.root / 'data/projects.json'))
        self.assertTrue(self.read(pipeline.POLL)['repositories'][KEY]['publication']['releases_complete'])

    def test_latest_release_tracks_removal_without_erasing_history(self):
        self.setup_gitlab()
        self.net.releases = {1: [release('v2'), release('v1', '2026-10-17T00:00:00Z')]}
        self.apply(self.collect())
        self.net.releases = {1: [release('v1', '2026-10-17T00:00:00Z')]}
        self.apply(self.collect(now=NOW + timedelta(hours=1)))
        self.assertEqual(load_projects(self.root / 'data/projects.json')[0]['gitlab']['latest_release']['tag'], 'v1')
        self.net.releases = {1: []}
        self.apply(self.collect(now=NOW + timedelta(hours=2)))
        self.assertNotIn('latest_release', load_projects(self.root / 'data/projects.json')[0]['gitlab'])
        self.assertEqual({e['tag'] for e in self.read('data/activity.json')['events'] if e['type'] == 'release'}, {'v1', 'v2'})

    def test_release_pagination_partial_failure_retains_tags_and_old_latest(self):
        self.activity_state()
        row = load_projects(self.root / 'data/projects.json')[0]
        row['gitlab']['latest_release'] = {'tag': 'old', 'published_at': '2026-10-17T00:00:00Z'}
        write_projects(self.root / 'data/projects.json', [row])
        poll = self.read(pipeline.POLL)
        poll['repositories'][KEY]['last_release_check_at'] = pipeline.stamp(NOW - timedelta(hours=1))
        poll['repositories'][KEY]['scan_requested'] = False
        poll['repositories'][KEY]['last_deep_scan'] = pipeline.stamp(NOW)
        self.put(pipeline.POLL, poll)
        self.net.releases = {1: [release(f'v{i}') for i in range(100)], 2: [release('last')]}
        self.apply(self.collect(requests=1))
        self.assertEqual(len(self.read('data/activity.json')['events']), 100)
        self.assertEqual(load_projects(self.root / 'data/projects.json')[0]['gitlab']['latest_release']['tag'], 'old')
        self.net.errors['/releases'] = 503
        self.apply(self.collect(requests=1, now=NOW + timedelta(minutes=1)))
        self.assertEqual(self.read(pipeline.POLL)['repositories'][KEY]['refresh_releases']['page'], 2)
        self.assertEqual(len(self.read('data/activity.json')['events']), 100)
        self.net.errors.clear()
        self.apply(self.collect(requests=1, now=NOW + timedelta(minutes=10)))
        self.assertEqual(len(self.read('data/activity.json')['events']), 101)

    def test_late_retry_after_uses_response_time(self):
        self.setup_gitlab()
        budget = pipeline.Budget(600, 10, api_requests=10, clock=self.net.clock)
        self.net.time = 300
        self.net.errors[''] = 429
        self.net.response_headers = {'Retry-After': '120'}
        client = gitlab.Client(KEY, budget, NOW, self.net.open)
        with self.assertRaises(gitlab.RateStop) as context:
            client.get()
        self.assertEqual(context.exception.retry_at, NOW + timedelta(seconds=420))

    def test_pre_gitlab_bundle_replays_with_original_owned_and_source_guards(self):
        self.setup_gitlab([project('a')])
        batch = self.collect()
        for phase in ('progress_before', 'progress_after'):
            batch[phase]['retry'].pop('releases')
            if batch[phase].get('cycle'):
                for field in ('targets', 'pending', 'deferred'):
                    batch[phase]['cycle'][field].pop('releases')
        for result in batch['results']:
            for field in ('before', 'after'):
                for owned in result[field].values():
                    owned.pop('gitlab')
            old = snapshot(project('a'))
            old.pop('gitlab_branch')
            old.pop('gitlab_path')
            result['source'] = pipeline.digest([old])
        published = self.apply(batch)
        self.assertEqual(published['accepted'], 1)
        self.assertEqual(published['conflicts'], [])


    def test_full_work_survives_provider_cooldown_even_when_not_due(self):
        records = [project('a')]
        poll = {'repositories': {'owner/a': {'next_probe_due_at': pipeline.stamp(NOW + timedelta(days=1)),
                                             'scan_requested': False}}}
        progress = {'version': 1, 'revision': 0, 'cycle': None, 'retry': {'probe': {}, 'activity': {}, 'releases': {}}}
        progress = pipeline.plan(progress, records, poll, NOW, 'full', full=True)
        progress['provider_blocked_until'] = {'github': pipeline.stamp(NOW + timedelta(hours=1))}
        progress = pipeline.plan(progress, records, poll, NOW + timedelta(minutes=1), 'scheduled-1')
        self.assertIn('owner/a', progress['retry']['probe'])
        self.assertIn('owner/a', progress['retry']['activity'])
        resumed = pipeline.plan(progress, records, poll, NOW + timedelta(hours=2), 'scheduled-2')
        self.assertEqual(resumed['cycle']['pending']['probe'], ['owner/a'])
        self.assertEqual(resumed['cycle']['pending']['activity'], ['owner/a'])
        # A fresh full request while already blocked also remains durable.
        progress['cycle'] = None
        progress['retry'] = {'probe': {}, 'activity': {}, 'releases': {}}
        blocked = pipeline.plan(progress, records, poll, NOW, 'new-full', full=True)
        self.assertIn('owner/a', blocked['retry']['activity'])

    def test_path_latest_chooses_all_branches_and_reuses_unchanged_heads(self):
        self.setup_gitlab([glproject(gitlab_path='src')])
        newer, older = glcommit(500), glcommit(600, '2026-10-10T00:00:00Z')
        self.net.branches = {1: [{'name': 'main', 'commit': newer}, {'name': 'old', 'commit': older}]}
        self.net.by_ref = {newer['id']: [newer], older['id']: [older]}
        self.apply(self.collect())
        row = load_projects(self.root / 'data/projects.json')[0]
        self.assertEqual(row['gitlab']['latest_commit']['date'], '2026-10-18')
        self.assertEqual(row['last_activity'], '2026-10-18')
        # Only old changes; main's cached per-path head must still win.
        changed = glcommit(700, '2026-10-11T00:00:00Z')
        self.net.branches[1][1]['commit'] = changed
        self.net.by_ref[changed['id']] = [changed]
        self.net.calls.clear()
        self.apply(self.collect(now=NOW + timedelta(hours=1)))
        self.assertEqual(load_projects(self.root / 'data/projects.json')[0]['gitlab']['latest_commit']['date'], '2026-10-18')
        self.assertFalse(any('ref_name=' + newer['id'] in url for url, _ in self.net.calls))

    def test_changed_path_purges_old_repository_releases(self):
        self.setup_gitlab()
        self.apply(self.collect())
        row = load_projects(self.root / 'data/projects.json')[0]
        row['gitlab_path'] = 'src'
        write_projects(self.root / 'data/projects.json', [row])
        self.apply(self.collect(now=NOW + timedelta(hours=1)))
        self.assertFalse(any(e['type'] == 'release' for e in self.read('data/activity.json')['events']))
        self.assertNotIn('latest_release', load_projects(self.root / 'data/projects.json')[0]['gitlab'])


    def test_release_cursor_restarts_when_project_joins_repository(self):
        self.activity_state()
        poll = self.read(pipeline.POLL)
        poll['repositories'][KEY]['last_release_check_at'] = pipeline.stamp(NOW - timedelta(hours=1))
        poll['repositories'][KEY]['scan_requested'] = False
        poll['repositories'][KEY]['last_deep_scan'] = pipeline.stamp(NOW)
        self.put(pipeline.POLL, poll)
        self.net.releases = {1: [release(f'v{i}') for i in range(100)], 2: [release('last')]}
        self.apply(self.collect(requests=1))
        self.assertEqual(self.read(pipeline.POLL)['repositories'][KEY]['refresh_releases']['page'], 2)
        old = load_projects(self.root / 'data/projects.json')[0]
        poll, events, catalogue = self.read(pipeline.POLL), self.read('data/activity.json'), self.read('state/project-catalog-state.json')
        self.seed([old, glproject('joined')], poll['repositories'])
        self.put('data/activity.json', events)
        self.put('state/project-catalog-state.json', catalogue)
        self.net.calls.clear()
        self.apply(self.collect(requests=20, now=NOW + timedelta(minutes=1)))
        self.assertTrue(any('/releases?' in url and 'page=1&' in url for url, _ in self.net.calls))
        tags = {e['tag'] for e in self.read('data/activity.json')['events'] if e['type'] == 'release' and e['project_id'] == 'joined'}
        self.assertEqual(len(tags), 101)

    def test_zero_remaining_header_publishes_success_then_cools_provider(self):
        self.setup_gitlab()
        self.net.root_headers = {'RateLimit-Remaining': '0', 'RateLimit-Reset': str(int(NOW.timestamp()) + 3600)}
        batch = self.collect(full=True)
        self.assertEqual(batch['summary']['completed']['probe'], 1)
        self.assertEqual(len(self.net.calls), 1)
        self.apply(batch)
        self.assertFalse(pipeline.status(pipeline.progress_read(self.root), NOW)['eligible'])
        self.assertEqual(load_projects(self.root / 'data/projects.json')[0]['gitlab']['repository'], KEY)


    def test_conditional_304_zero_quota_headers_are_honored(self):
        self.setup_gitlab()
        budget = pipeline.Budget(600, 10, api_requests=10, clock=self.net.clock)
        self.net.errors[''] = 304
        self.net.response_headers = {'RateLimit-Remaining': '0', 'RateLimit-Reset': str(int(NOW.timestamp()) + 3600)}
        client = gitlab.Client(KEY, budget, NOW, self.net.open)
        value, _, code = client.get(etag='old')
        self.assertEqual(code, 304)
        self.assertIsNone(value)
        self.assertEqual(client.retry_at, NOW + timedelta(hours=1))


    def test_hourly_gitlab_work_requeues_while_github_sweep_remains_active(self):
        records = [project('a'), glproject()]
        poll = {'repositories': {'owner/a': {}, KEY: {'last_probe_at': pipeline.stamp(NOW),
            'last_release_check_at': pipeline.stamp(NOW), 'scan_requested': False}}}
        progress = {'version': 1, 'revision': 0, 'cycle': None, 'retry': {'probe': {}, 'activity': {}, 'releases': {}}}
        progress = pipeline.plan(progress, records, poll, NOW, 'start')
        cycle_id = progress['cycle']['id']
        self.assertEqual(progress['cycle']['pending']['probe'], ['owner/a'])
        later = pipeline.plan(progress, records, poll, NOW + timedelta(hours=1), 'next-hour')
        self.assertEqual(later['cycle']['id'], cycle_id)
        self.assertNotIn(KEY, later['cycle']['pending']['probe'])
        self.assertIn(KEY, later['cycle']['pending']['activity'])
        self.assertIn(KEY, later['cycle']['pending']['releases'])
        self.assertIn('owner/a', later['cycle']['pending']['probe'])


    def test_hourly_activity_and_releases_do_not_repeat_daily_metadata(self):
        self.setup_gitlab()
        self.apply(self.collect())
        self.net.calls.clear()
        self.apply(self.collect(now=NOW + timedelta(hours=1)))
        urls = [url for url, _ in self.net.calls]
        self.assertEqual(len(urls), 2)
        self.assertTrue(any('/repository/branches?' in url for url in urls))
        self.assertTrue(any('/releases?' in url for url in urls))
        self.net.calls.clear()
        self.apply(self.collect(now=NOW + timedelta(hours=24)))
        self.assertEqual(len(self.net.calls), 3)
        self.assertTrue(any(urlsplit(url).path.endswith('group%2Fsubgroup%2Fproject') for url, _ in self.net.calls))

    def test_ambiguous_404_verifies_root_and_caches_success_on_repeated_branch_failure(self):
        self.setup_gitlab()
        self.apply(self.collect())
        self.net.errors['/repository/branches'] = 404
        self.apply(self.collect(now=NOW + timedelta(hours=1)))
        self.assertTrue(self.read(pipeline.POLL)['repositories'][KEY]['availability_recheck_requested'])
        self.assertNotIn('source_availability', load_projects(self.root / 'data/projects.json')[0]['gitlab'])
        self.net.calls.clear()
        self.apply(self.collect(now=NOW + timedelta(hours=1, minutes=1)))
        self.assertTrue(any(urlsplit(url).path.endswith('group%2Fsubgroup%2Fproject') for url, _ in self.net.calls))
        self.assertNotIn('availability_recheck_requested', self.read(pipeline.POLL)['repositories'][KEY])
        self.net.calls.clear()
        self.apply(self.collect(now=NOW + timedelta(hours=1, minutes=10)))
        self.assertFalse(any(urlsplit(url).path.endswith('group%2Fsubgroup%2Fproject') for url, _ in self.net.calls))
        self.assertNotIn('availability_recheck_requested', self.read(pipeline.POLL)['repositories'][KEY])
        self.assertNotIn('source_availability', load_projects(self.root / 'data/projects.json')[0]['gitlab'])

    def test_ambiguous_endpoint_404_requires_confirmed_root_404_to_mark_unavailable(self):
        self.setup_gitlab()
        self.apply(self.collect())
        self.net.errors = {'': 404, '/repository/branches': 404, '/releases': 404}
        self.apply(self.collect(now=NOW + timedelta(hours=1)))
        self.assertNotIn('source_availability', load_projects(self.root / 'data/projects.json')[0]['gitlab'])
        self.net.calls.clear()
        self.apply(self.collect(now=NOW + timedelta(hours=1, minutes=1)))
        self.assertEqual(len(self.net.calls), 1)
        self.assertEqual(load_projects(self.root / 'data/projects.json')[0]['gitlab']['source_availability']['http_status'], 404)
        self.assertTrue(self.read(pipeline.POLL)['repositories'][KEY]['repository_availability']['retryable'])

    def test_renamed_default_branch_triggers_root_refresh_then_resumes(self):
        self.setup_gitlab()
        self.apply(self.collect())
        self.net.default_branch = 'develop'
        self.net.branches = {1: [{'name': 'develop', 'commit': glcommit(900)}]}
        self.net.errors['/repository/branches/main'] = 404
        self.apply(self.collect(now=NOW + timedelta(hours=1)))
        self.assertTrue(self.read(pipeline.POLL)['repositories'][KEY]['availability_recheck_requested'])
        self.apply(self.collect(now=NOW + timedelta(hours=1, minutes=3)))
        row = load_projects(self.root / 'data/projects.json')[0]
        self.assertEqual(row['gitlab']['default_branch'], 'develop')
        self.assertEqual(row['gitlab']['tracking_branch'], 'develop')
        self.assertNotIn('source_availability', row['gitlab'])
        self.assertNotIn('refresh_activity', self.read(pipeline.POLL)['repositories'][KEY])

    def test_empty_repository_is_still_checked_hourly_for_first_commits(self):
        self.setup_gitlab()
        self.net.default_branch = None
        self.net.branches = {1: []}
        self.apply(self.collect())
        self.assertFalse(any(e['type'] == 'commit' for e in self.read('data/activity.json')['events']))
        self.net.branches = {1: [{'name': 'main', 'commit': self.net.head}]}
        self.net.calls.clear()
        self.apply(self.collect(now=NOW + timedelta(hours=1)))
        self.assertTrue(any(e['type'] == 'commit' for e in self.read('data/activity.json')['events']))
        self.assertFalse(any(urlsplit(url).path.endswith('group%2Fsubgroup%2Fproject') for url, _ in self.net.calls))

    def test_failed_root_then_missing_branch_keeps_retry_queues_valid(self):
        self.setup_gitlab()
        self.apply(self.collect())
        self.net.errors = {'': 500, '/repository/branches': 404}
        self.apply(self.collect(now=NOW + timedelta(days=1)))
        progress = pipeline.progress_read(self.root)
        for work in pipeline.WORKS:
            self.assertFalse(set(progress['cycle']['pending'][work]) & set(progress['cycle']['deferred'][work]))
        self.assertNotIn('source_availability', load_projects(self.root / 'data/projects.json')[0]['gitlab'])


    def test_mixed_offset_saved_bundle_replays_chronologically_without_identity_changes(self):
        self.setup_gitlab()
        self.net.gl_pages = {1: [glcommit(1, '2026-10-18T02:53:29.000+00:00'),
                                  glcommit(2, '2026-10-17T22:56:14.000-04:00'),
                                  glcommit(3, '2026-10-18T02:56:14.001Z')]}
        batch = self.collect()
        for row in batch['results']:
            row['events_after'].sort(key=lambda e: e['date'], reverse=True)  # Pre-fix retained artifact.
        original = {e['sha']: e['date'] for e in batch['results'][0]['events_after'] if e['type'] == 'commit'}
        self.assertEqual(self.apply(batch)['accepted'], 1)
        events = self.read('data/activity.json')['events']
        self.assertTrue(all(gitlab.parse_time(a['date']) >= gitlab.parse_time(b['date']) for a, b in zip(events, events[1:])))
        self.assertEqual({e['sha']: e['date'] for e in events if e['type'] == 'commit'}, original)
        self.assertTrue(self.apply(batch)['duplicate'])

    def test_latest_commit_uses_full_instants_and_utc_day_across_offset_midnight(self):
        self.setup_gitlab()
        older = glcommit(1, '2026-10-18T00:30:00+14:00')
        newer = glcommit(2, '2026-10-17T23:30:00-02:00')
        self.net.branches = {1: [{'name': 'main', 'commit': older}, {'name': 'newer', 'commit': newer}]}
        self.net.by_ref = {older['id']: [older], newer['id']: [newer]}
        self.apply(self.collect())
        project = load_projects(self.root / 'data/projects.json')[0]
        self.assertEqual(project['gitlab']['latest_commit']['sha'], newer['id'])
        self.assertEqual(project['gitlab']['latest_commit']['date'], '2026-10-18')
        self.assertEqual(project['gitlab']['latest_commit']['committed_at'], newer['committed_date'])
        self.assertEqual(gitlab.commit_metadata(older, KEY)['date'], '2026-10-17')

    def test_legacy_cursor_without_commit_instant_is_restarted_safely(self):
        self.activity_state()
        self.apply(self.collect(requests=1))
        poll = self.read(pipeline.POLL)
        cursor = poll['repositories'][KEY]['refresh_activity']
        cursor['identity'] = 'pre-committed-at-collector'
        for latest in cursor['latest'].values():
            latest.pop('committed_at', None)
        self.put(pipeline.POLL, poll)
        self.net.calls.clear()
        self.apply(self.collect())
        self.assertTrue(any('/repository/branches?' in url for url, _ in self.net.calls))
        self.assertIn('committed_at', load_projects(self.root / 'data/projects.json')[0]['gitlab']['latest_commit'])

    def test_release_403_verified_root_preserves_cache_and_resolves_as_unknown_with_daily_retry(self):
        from refresh_scope import check_publishable
        cached = {'tag': 'cached', 'published_at': '2026-10-17T00:00:00Z', 'url': 'https://' + KEY + '/-/releases/cached'}
        self.setup_gitlab([glproject(gitlab={'repository': KEY, 'latest_release': cached})])
        self.put('state/project-catalog-state.json', {'version': 1, 'projects': {}, 'removed': {}})
        self.net.errors['/releases'] = 403
        batch = self.collect()
        self.apply(batch)
        row = load_projects(self.root / 'data/projects.json')[0]
        state = self.read(pipeline.POLL)['repositories'][KEY]
        self.assertEqual(row['gitlab']['release_availability']['http_status'], 403)
        self.assertNotIn('source_availability', row['gitlab'])
        # New-publication reset intentionally clears old generated metadata, so
        # verify cache preservation separately in the next routine attempt.
        self.assertFalse(state['publication']['releases_complete'])
        self.assertEqual(state['publication']['release_outcome'], 'capability-unavailable')
        self.assertNotIn('last_release_check_at', state)
        check_publishable(self.read(pipeline.POLL), [row])
        row['gitlab']['latest_release'] = cached
        write_projects(self.root / 'data/projects.json', [row])
        self.net.calls.clear()
        self.apply(self.collect(now=NOW + timedelta(hours=1)))
        self.assertFalse(any('/releases?' in url for url, _ in self.net.calls))
        self.assertEqual(load_projects(self.root / 'data/projects.json')[0]['gitlab']['latest_release'], cached)
        self.net.calls.clear()
        self.apply(self.collect(now=NOW + timedelta(days=1)))
        self.assertEqual(load_projects(self.root / 'data/projects.json')[0]['gitlab']['latest_release'], cached)
        self.net.errors.clear()
        self.apply(self.collect(now=NOW + timedelta(days=2)))
        row = load_projects(self.root / 'data/projects.json')[0]
        state = self.read(pipeline.POLL)['repositories'][KEY]
        self.assertNotIn('release_availability', row['gitlab'])
        self.assertNotIn('release_availability', state)
        self.assertTrue(state['publication']['releases_complete'])

    def test_release_403_cannot_waive_unfinished_commit_history(self):
        from refresh_scope import check_publishable
        self.setup_gitlab()
        self.put('state/project-catalog-state.json', {'version': 1, 'projects': {}, 'removed': {}})
        self.net.errors['/releases'] = 403
        self.apply(self.collect(requests=3))
        state = self.read(pipeline.POLL)['repositories'][KEY]
        self.assertIn('release_availability', state)
        self.assertFalse(state['publication']['history_complete'])
        with self.assertRaises(SystemExit):
            check_publishable(self.read(pipeline.POLL), load_projects(self.root / 'data/projects.json'))
        self.apply(self.collect())
        check_publishable(self.read(pipeline.POLL), load_projects(self.root / 'data/projects.json'))

    def test_release_quota_403_never_becomes_capability_waiver(self):
        for headers in ({'X-RateLimit-Remaining': '0'}, {'Retry-After': '3600'}, {'RateLimit-Remaining': '0'}):
            with self.subTest(headers=headers):
                (self.root / pipeline.PROGRESS).unlink(missing_ok=True)
                self.setup_gitlab()
                self.net.errors['/releases'] = 403
                self.net.response_headers = headers
                batch = self.collect()
                self.apply(batch)
                self.assertIn('gitlab', batch['progress_after']['provider_blocked_until'])
                row = load_projects(self.root / 'data/projects.json')[0]
                self.assertNotIn('release_availability', row['gitlab'])
                self.assertNotIn('release_availability', self.read(pipeline.POLL)['repositories'][KEY])

    def test_release_403_requires_a_current_accessible_root(self):
        self.setup_gitlab()
        self.apply(self.collect())
        self.net.errors = {'/releases': 403, '': 403}
        self.apply(self.collect(now=NOW + timedelta(hours=1)))
        row = load_projects(self.root / 'data/projects.json')[0]
        self.assertNotIn('release_availability', row['gitlab'])
        self.assertNotIn('release_availability', self.read(pipeline.POLL)['repositories'][KEY])


    def test_one_request_slices_finish_release_403_root_verification_without_livelock(self):
        from refresh_scope import publication_fingerprint, publication_resolved
        self.setup_gitlab()
        self.apply(self.collect())
        poll = self.read(pipeline.POLL)
        state = poll['repositories'][KEY]
        state['last_root_check_at'] = pipeline.stamp(NOW - timedelta(hours=2))
        state['last_release_check_at'] = pipeline.stamp(NOW - timedelta(hours=1))
        records = load_projects(self.root / 'data/projects.json')
        fingerprint = publication_fingerprint(records)
        state['publication'] = {'fingerprint': fingerprint, 'metadata_complete': True,
                                'history_complete': True, 'releases_complete': False, 'reset_project_ids': []}
        self.put(pipeline.POLL, poll)
        self.net.errors['/releases'] = 403
        self.net.calls.clear()
        for minute in range(5):
            self.apply(self.collect(requests=1, now=NOW + timedelta(minutes=minute), request_id=f"403-slice-{minute}"))
        state = self.read(pipeline.POLL)['repositories'][KEY]
        self.assertTrue(publication_resolved(KEY, state, fingerprint))
        self.assertNotIn('release_access_verification', state)
        self.assertFalse(state['publication']['releases_complete'])
        self.assertEqual(sum('/releases?' in url for url, _ in self.net.calls), 1)
        self.assertEqual(sum(urlsplit(url).path.endswith('group%2Fsubgroup%2Fproject') for url, _ in self.net.calls), 1)


    def test_fresh_release_403_replaces_expired_pending_verification_timestamp(self):
        from refresh_scope import publication_fingerprint, publication_resolved
        self.setup_gitlab()
        self.apply(self.collect())
        poll = self.read(pipeline.POLL)
        state = poll['repositories'][KEY]
        fingerprint = publication_fingerprint(load_projects(self.root / 'data/projects.json'))
        state['publication'] = {'fingerprint': fingerprint, 'metadata_complete': True,
                                'history_complete': True, 'releases_complete': False, 'reset_project_ids': []}
        state['release_access_verification'] = {'http_status': 403, 'observed_at': pipeline.stamp(NOW - timedelta(hours=2)),
                                                'fingerprint': fingerprint}
        self.put(pipeline.POLL, poll)
        self.net.errors['/releases'] = 403
        later = NOW + timedelta(hours=1)
        self.apply(self.collect(now=later))
        state = self.read(pipeline.POLL)['repositories'][KEY]
        self.assertEqual(state['release_availability']['observed_at'], pipeline.stamp(later))
        self.assertTrue(publication_resolved(KEY, state, fingerprint))



if __name__ == '__main__':
    unittest.main()
