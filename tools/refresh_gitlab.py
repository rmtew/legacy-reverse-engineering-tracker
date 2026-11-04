"""Public GitLab.com project collection, with bounded resumable histories.

No token is sent. A root lookup is the only operation allowed to declare a
project unavailable. Commit pages are pinned to immutable SHAs and retain the
same 30-day lower bound for the entire scan; no incremental date watermark is
used, because commit dates need not follow graph/discovery order.
"""
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
import hashlib
import json
import time
from urllib.error import HTTPError
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen

from activity_history import RETENTION_DAYS, compact_history, freeze_addition_context
from catalogue_storage import bounded, encode
from repository_provider import selectors

REQUEST_DELAY = 0.5
PER_PAGE = 100


def stamp(now):
    return now.astimezone(timezone.utc).isoformat(timespec='seconds').replace('+00:00', 'Z')


def parse_time(value):
    return datetime.fromisoformat(value.replace('Z', '+00:00'))


class VerifyRoot(Exception):
    pass


class RootUnavailable(Exception):
    pass


class RateStop(Exception):
    def __init__(self, retry_at, reason='GitLab rate limit'):
        super().__init__(reason)
        self.retry_at = retry_at


def retry_time(headers, now):
    candidates = [now + timedelta(minutes=2)]
    for name in ('Retry-After', 'retry-after'):
        if value := headers.get(name):
            try:
                candidates.append(now + timedelta(seconds=max(0, float(value))))
            except (TypeError, ValueError):
                try:
                    candidates.append(parsedate_to_datetime(value).astimezone(timezone.utc))
                except (TypeError, ValueError, OverflowError):
                    pass
    for name in ('RateLimit-Reset', 'ratelimit-reset', 'X-RateLimit-Reset', 'x-ratelimit-reset'):
        if value := headers.get(name):
            try:
                candidates.append(datetime.fromtimestamp(float(value), timezone.utc))
            except (TypeError, ValueError, OverflowError):
                pass
    return max(candidates)


class Client:
    def __init__(self, repo, budget, now, opener=None, before_request=None):
        if not repo.startswith('gitlab.com/'):
            raise ValueError('Unsupported GitLab host')
        self.repo, self.budget, self.now = repo, budget, now
        self.open = opener or urlopen
        self.before_request = before_request
        self.base = 'https://gitlab.com/api/v4/projects/' + quote(repo.split('/', 1)[1], safe='')
        self.root_status = None
        self.retry_at = None

    def observe_quota(self, headers):
        observed = self.now + timedelta(seconds=max(0, self.budget.clock() - self.budget.start))
        quota = {k.lower(): str(v) for k, v in headers.items()}
        if quota.get('ratelimit-remaining') == '0' or quota.get('x-ratelimit-remaining') == '0':
            self.retry_at = retry_time(headers, observed)

    def get(self, suffix='', *, etag=None, params=None):
        url = self.base + suffix + ('?' + urlencode(params) if params else '')
        headers = {'Accept': 'application/json', 'User-Agent': 'retro-project-tracker/1.0'}
        if etag:
            headers['If-None-Match'] = etag
        self.budget.check(1)
        if REQUEST_DELAY:
            time.sleep(REQUEST_DELAY)
        if self.before_request:
            self.before_request(url)
        timeout = self.budget.before_request(api=True)
        started = self.budget.clock()
        try:
            with self.open(Request(url, headers=headers), timeout=timeout) as response:
                code, response_headers = response.status, dict(response.headers)
                if not suffix:
                    self.root_status = code
                self.budget.statuses[str(code)] = self.budget.statuses.get(str(code), 0) + 1
                out = bytearray()
                while True:
                    self.budget.check()
                    chunk = response.read(65536)
                    if not chunk:
                        break
                    out.extend(chunk)
                    if len(out) > 8 * 1024 * 1024:
                        raise ValueError('Oversized GitLab API response')
                value = json.loads(out)
        except HTTPError as exc:
            self.budget.statuses[str(exc.code)] = self.budget.statuses.get(str(exc.code), 0) + 1
            if not suffix:
                self.root_status = exc.code
            if exc.code == 304 and etag:
                self.observe_quota(exc.headers)
                return None, dict(exc.headers), 304
            error_headers = {k.lower(): str(v) for k, v in exc.headers.items()}
            if exc.code == 429 or (exc.code == 403 and (
                    error_headers.get('ratelimit-remaining') == '0'
                    or error_headers.get('x-ratelimit-remaining') == '0'
                    or 'retry-after' in error_headers)):
                raise RateStop(retry_time(exc.headers, self.now + timedelta(seconds=max(0, self.budget.clock() - self.budget.start)))) from exc
            raise
        finally:
            self.budget.http_seconds += self.budget.clock() - started
        self.observe_quota(response_headers)
        if code != 200:
            raise ValueError(f'Unexpected GitLab status {code}')
        return value, response_headers, code


def next_page(headers, page, rows):
    # GitLab may omit total counts for large histories, but next-page is useful.
    lowered = {k.lower(): str(v) for k, v in headers.items()}
    if 'x-next-page' in lowered:
        value = lowered['x-next-page']
        if not value:
            return None
        if not value.isdigit() or int(value) != page + 1:
            raise ValueError('Invalid GitLab next-page cursor')
        return int(value)
    return page + 1 if len(rows) == PER_PAGE else None


def commit_metadata(item, repo):
    sha = item.get('id')
    when = item.get('committed_date') or item.get('created_at')
    if not isinstance(sha, str) or not len(sha) in (40, 64) or any(c not in '0123456789abcdef' for c in sha):
        raise ValueError('Invalid GitLab commit SHA')
    if not when or not parse_time(when).tzinfo:
        raise ValueError('Invalid GitLab commit date')
    title = (item.get('title') or (item.get('message') or '').split('\n')[0]).strip()
    return {'sha': sha, 'date': parse_time(when).astimezone(timezone.utc).date().isoformat(),
            'committed_at': when, 'title': title,
            'url': f'https://{repo}/-/commit/{sha}', 'message': title}


def probe_unit(repo, records, rs, events, now, client):
    value, headers, status = client.get(etag=rs.get('etag'))
    if status == 200:
        if not isinstance(value, dict) or 'default_branch' not in value:
            raise ValueError('Invalid GitLab project metadata')
        rs['default_branch'] = value.get('default_branch')
        rs['empty_repository'] = bool(value.get('empty_repo') or not value.get('default_branch'))
        rs['project_metadata'] = {key: value.get(key) for key in
                                  ('default_branch', 'created_at', 'archived', 'web_url')}
        if headers.get('ETag') or headers.get('etag'):
            rs['etag'] = headers.get('ETag') or headers['etag']
        else:
            rs.pop('etag', None)
    if not rs.get('project_metadata'):
        raise ValueError('GitLab 304 has no retained project metadata')
    for project in records:
        meta = project.setdefault('gitlab', {})
        branch, path = selectors(project)
        meta.update(rs['project_metadata'])
        meta.update(repository=repo, tracking_branch=branch or rs.get('default_branch'),
                    checked_at=stamp(now))
        meta.pop('source_availability', None)
    rs['project_ids'] = sorted(p['id'] for p in records)
    rs['last_probe_at'] = stamp(now)
    rs['scan_requested'] = True  # Repository last_activity_at also includes non-commit activity.
    rs.pop('last_error', None)
    if rs.get('publication'):
        rs['publication']['metadata_complete'] = True
    return records, rs, events, True


def activity_unit(repo, records, rs, events, now, client):
    identity = hashlib.sha256(encode([
        [(p['id'], *selectors(p), (p.get('gitlab') or {}).get('tracking_branch')) for p in records],
        (rs.get('publication') or {}).get('fingerprint'), RETENTION_DAYS, 'committed-at-v1',
    ])).hexdigest()
    cursor = rs.get('refresh_activity')
    if not cursor or cursor.get('identity') != identity:
        branches = sorted({selectors(p)[0] or rs.get('default_branch') for p in records} - {None})
        cursor = {'identity': identity, 'started_at': stamp(now),
                  'since': stamp(now - timedelta(days=RETENTION_DAYS)),
                  'pending_branches': branches, 'branches': {}, 'queries': [], 'reset_applied': False,
                  'listed': all(selectors(p)[0] for p in records),
                  'branch_page': 1, 'latest': {}, 'path_latest': {}}
        rs['refresh_activity'] = cursor
    publication = rs.get('publication') or {}
    backfill = bool(publication and not publication.get('history_complete')) or sorted(p['id'] for p in records) != rs.get('last_deep_scan_project_ids')
    def choose_latest(project, latest):
        chosen = cursor.setdefault('latest', {}).get(project['id'])
        if latest and (not chosen or parse_time(latest.get('committed_at', latest['date'])) >= parse_time(chosen.get('committed_at', chosen['date']))):
            cursor['latest'][project['id']] = latest
            project['gitlab']['latest_commit'] = latest
            project['last_activity'] = latest['date']
            project['gitlab'].pop('latest_commit_lookup', None)

    def capture_branch(item):
        if not isinstance(item, dict) or not item.get('name') or not isinstance(item.get('commit'), dict):
            raise ValueError('Invalid GitLab branch response')
        branch = item['name']
        latest = commit_metadata(item['commit'], repo)
        if branch in cursor['branches']:
            return  # A moving branch list must not replace an already pinned tip.
        cursor['branches'][branch] = latest['sha']
        if branch in cursor['pending_branches']:
            cursor['pending_branches'].remove(branch)
        matching = [p for p in records if not selectors(p)[0] or selectors(p)[0] == branch]
        previous = (rs.get('branches') or {}).get(branch) or {}
        for project in matching:
            if not selectors(project)[1]:
                choose_latest(project, latest)
        changed = backfill or latest['sha'] != previous.get('tip_sha')
        for path in sorted({selectors(p)[1] or '' for p in matching}):
            if (not changed and path and path in previous.get('path_latest', {})
                    and (previous['path_latest'][path] is None or previous['path_latest'][path].get('committed_at'))):
                retained = previous['path_latest'][path]
                cursor.setdefault('path_latest', {}).setdefault(branch, {})[path] = retained
                for project in matching:
                    if selectors(project)[1] == path:
                        choose_latest(project, retained)
            elif changed or path:
                cursor['queries'].append({'branch': branch, 'tip': latest['sha'], 'path': path,
                                          'page': 1, 'history': changed})

    if not cursor.get('listed', True):
        items, headers, _ = client.get('/repository/branches', params={
            'page': cursor['branch_page'], 'per_page': PER_PAGE})
        if not isinstance(items, list):
            raise ValueError('Invalid GitLab branch list')
        for item in items:
            capture_branch(item)
        following = next_page(headers, cursor['branch_page'], items)
        if following:
            cursor['branch_page'] = following
        else:
            cursor['listed'] = True
        bounded(encode(cursor), 'GitLab activity cursor')
        return records, rs, events, False
    if cursor['pending_branches']:
        branch = cursor['pending_branches'][0]
        item, _, _ = client.get('/repository/branches/' + quote(branch, safe=''))
        if isinstance(item, dict):
            item['name'] = branch
        capture_branch(item)
        return records, rs, events, False
    if not cursor['reset_applied']:
        # Keep previously collected history until a page succeeds. Never erase
        # it just because an upstream branch request fails.
        reset = set(publication.get('reset_project_ids') or []) if backfill else set()
        events = [e for e in events if not (e.get('project_id') in reset and e.get('type') in ('commit', 'daily_commits'))]
        cursor['reset_applied'] = True
    if cursor['queries']:
        query = cursor['queries'][0]
        if query['path'] and not query.get('latest_checked'):
            newest, _, _ = client.get('/repository/commits', params={
                'ref_name': query['tip'], 'path': query['path'], 'per_page': 1})
            if not isinstance(newest, list):
                raise ValueError('Invalid GitLab path head')
            latest = commit_metadata(newest[0], repo) if newest else None
            cursor.setdefault('path_latest', {}).setdefault(query['branch'], {})[query['path']] = latest
            for project in records:
                if ((not selectors(project)[0] or selectors(project)[0] == query['branch'])
                        and (selectors(project)[1] or '') == query['path']):
                    choose_latest(project, latest)
            query['latest_checked'] = True
            if not query.get('history', True):
                cursor['queries'].pop(0)
            return records, rs, events, False
        params = {'ref_name': query['tip'], 'since': cursor['since'], 'page': query['page'], 'per_page': PER_PAGE}
        if query['path']:
            params['path'] = query['path']
        chunk, headers, _ = client.get('/repository/commits', params=params)
        if not isinstance(chunk, list):
            raise ValueError('Invalid GitLab commits page')
        known = {(e.get('project_id'), e.get('repository'), e.get('sha')): e for e in events if e.get('type') == 'commit'}
        other = [e for e in events if e.get('type') != 'commit']
        for item in chunk:
            latest = commit_metadata(item, repo)
            when = item.get('committed_date') or item['created_at']
            if parse_time(when) < now - timedelta(days=RETENTION_DAYS):
                continue  # Keep paging; dates do not establish traversal completeness.
            for project in records:
                if (selectors(project)[0] and selectors(project)[0] != query['branch']) or (selectors(project)[1] or '') != query['path']:
                    continue
                key = project['id'], repo, latest['sha']
                row = known.setdefault(key, {'type': 'commit', 'project_id': project['id'], 'repository': repo,
                    'sha': latest['sha'], 'date': when, 'title': latest['title'], 'url': latest['url'],
                    'author': item.get('author_name') or '', 'branches': []})
                row['branches'] = sorted(set(row.get('branches') or []) | {query['branch']})
        events = compact_history(list(known.values()) + other, now)
        following = next_page(headers, query['page'], chunk)
        if following:
            query['page'] = following
        else:
            cursor['queries'].pop(0)
    complete = not cursor['queries']
    if complete:
        rs['branches'] = {branch: {'tip_sha': tip, 'last_scan_at': cursor['started_at'],
                                  'path_latest': cursor.get('path_latest', {}).get(branch, {})}
                          for branch, tip in cursor['branches'].items()}
        for project in records:
            if selectors(project)[1] and project['id'] not in cursor.get('latest', {}):
                project['gitlab'].pop('latest_commit', None)
                project['gitlab']['latest_commit_lookup'] = 'unavailable'
        rs['last_deep_scan'] = cursor['started_at']
        rs['last_deep_scan_project_ids'] = sorted(p['id'] for p in records)
        newer_probe = bool(rs.get('last_probe_at') and parse_time(rs['last_probe_at']) > parse_time(cursor['started_at']))
        rs['scan_requested'] = newer_probe
        rs.pop('refresh_activity', None)
        rs.pop('last_error', None)
        if publication:
            publication['history_complete'] = not newer_probe
        if newer_probe:
            complete = False
        if not newer_probe:
            freeze_addition_context(events, records, {repo: rs}, now)
    bounded(encode(rs.get('refresh_activity', {})), 'GitLab activity cursor')
    return records, rs, events, complete


def release_unit(repo, records, rs, events, now, client):
    if all(selectors(p)[1] for p in records):
        rs['last_release_check_at'] = stamp(now)
        if rs.get('publication'):
            rs['publication']['releases_complete'] = True
        rs.pop('refresh_releases', None)
        return records, rs, events, True
    identity = hashlib.sha256(encode([
        [(p['id'], *selectors(p)) for p in records],
        (rs.get('publication') or {}).get('fingerprint'),
    ])).hexdigest()
    cursor = rs.get('refresh_releases')
    if not cursor or cursor.get('identity') != identity:
        cursor = {'identity': identity, 'started_at': stamp(now), 'page': 1}
        rs['refresh_releases'] = cursor
    chunk, headers, _ = client.get('/releases', params={'per_page': PER_PAGE, 'page': cursor['page'],
                                                     'order_by': 'released_at', 'sort': 'desc'})
    if not isinstance(chunk, list):
        raise ValueError('Invalid GitLab releases page')
    releases = {(e['project_id'], e.get('tag')): e for e in events if e.get('type') == 'release'}
    other = [e for e in events if e.get('type') != 'release']
    cutoff = now - timedelta(days=RETENTION_DAYS)
    for item in chunk:
        tag, when = item.get('tag_name'), item.get('released_at')
        if not isinstance(tag, str) or not tag or not when or not parse_time(when).tzinfo:
            raise ValueError('Invalid GitLab release')
        if parse_time(when) > now:
            continue  # Scheduled releases are not published activity yet.
        latest = {'tag': tag, 'name': item.get('name') or tag, 'published_at': when,
                  'url': f'https://{repo}/-/releases/{quote(tag, safe="")}' }
        if not cursor.get('latest') or parse_time(when) > parse_time(cursor['latest']['published_at']):
            cursor['latest'] = latest
        for project in records:
            if selectors(project)[1]:
                continue  # Repository releases cannot be attributed to a subtree.
            meta = project.setdefault('gitlab', {'repository': repo})
            if parse_time(when) >= cutoff:
                releases[project['id'], tag] = {'type': 'release', 'project_id': project['id'], 'repository': repo,
                    'tag': tag, 'title': latest['name'], 'name': latest['name'], 'date': when, 'url': latest['url']}
    following = next_page(headers, cursor['page'], chunk)
    # Releases are explicitly sorted by released_at (unlike commit topology).
    complete = not following or bool(chunk and all(parse_time(r['released_at']) < cutoff for r in chunk))
    if complete:
        rs.pop('release_availability', None)
        rs.pop('release_access_verification', None)
        if rs.get('publication'):
            rs['publication'].pop('release_outcome', None)
        for project in records:
            if not selectors(project)[1]:
                (project.get('gitlab') or {}).pop('release_availability', None)
                if cursor.get('latest'):
                    project.setdefault('gitlab', {'repository': repo})['latest_release'] = cursor['latest']
                else:
                    (project.get('gitlab') or {}).pop('latest_release', None)
        rs['last_release_check_at'] = cursor['started_at']
        if rs.get('publication'):
            rs['publication']['releases_complete'] = True
        rs.pop('refresh_releases', None)
    else:
        cursor['page'] = following
    return records, rs, compact_history(other + list(releases.values()), now), complete
