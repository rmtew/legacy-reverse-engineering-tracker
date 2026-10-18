#!/usr/bin/env python3
"""Bounded evidence collection and offline replay against the latest catalogue.

Only the Git commit publishes results and their scheduler state. The temporary
bundle is outside the checkout so publication retries never recollect evidence.
Canonical automated evidence doubles as the cache; state contains no fact copy,
raw documents or history, only one bounded scheduling entry per active project.
"""
from __future__ import annotations

import argparse
import copy
from datetime import datetime, timedelta, timezone
import hashlib
from http.client import HTTPException
import json
import os
from pathlib import Path
import re
import shutil
import tempfile
import time
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode, urljoin, urlsplit
from urllib.request import Request, build_opener, HTTPRedirectHandler

import enrich_evidence as evidence
from catalogue_storage import bounded, encode, load_projects, write_projects

STATE = 'state/enrichment-state.json'
DOC_FIELDS = ('compilable', 'playable', 'byte_exact', 're_started')
OWNED = [('evidence', 'automated'), ('re_started',),
         *(('build', key) for key in (*DOC_FIELDS[:3], 'runnable'))]
DOC_TTL = timedelta(days=7)
CI_TTL = timedelta(days=1)
MAX_RESPONSE = 700_000
STATE_FIELDS = {'fingerprint', 'last_attempt_at', 'docs_key', 'docs_digest', 'docs_checked_at',
                'ci_checked_at', 'failures', 'retry_at'}


def log(**values):
    print(json.dumps(values, ensure_ascii=False, separators=(',', ':')), flush=True)


def digest(value):
    return hashlib.sha256(encode(value)).hexdigest()


def stamp(now):
    return now.astimezone(timezone.utc).isoformat(timespec='seconds').replace('+00:00', 'Z')


def parsed(value):
    result = datetime.fromisoformat(value.replace('Z', '+00:00')) if value else datetime.min.replace(tzinfo=timezone.utc)
    if result.tzinfo is None:
        raise ValueError('Enrichment timestamps require a timezone')
    return result


def identity(record):
    gh = record.get('github') or {}
    return {'repo': evidence.repo_name(record.get('repo')),
            'branch': record.get('github_branch') or gh.get('tracking_branch') or gh.get('default_branch') or 'main',
            'path': (record.get('github_path') or '').strip('/')}


def fingerprint(record):
    gh = record.get('github') or {}
    return digest({**identity(record), 'collector': evidence.COLLECTOR,
                   'pushed_at': gh.get('pushed_at'), 'latest': (gh.get('latest_commit') or {}).get('sha')})


def state_read(root):
    path = Path(root) / STATE
    value = json.loads(path.read_bytes()) if path.exists() else {'version': 1, 'records': {}}
    if not isinstance(value, dict) or set(value) != {'version', 'records'} or value.get('version') != 1 or not isinstance(value.get('records'), dict):
        raise ValueError('Invalid enrichment scheduler state')
    for pid, entry in value['records'].items():
        if not isinstance(pid, str) or not isinstance(entry, dict) or set(entry) - STATE_FIELDS:
            raise ValueError('Invalid enrichment scheduler entry')
        for key, item in entry.items():
            if key.endswith('_at'):
                parsed(item)
            elif key == 'failures':
                if type(item) is not int or not 0 <= item <= 5:
                    raise ValueError('Invalid enrichment failure count')
            elif not isinstance(item, str) or not re.fullmatch(r'[0-9a-f]{64}', item):
                raise ValueError('Invalid enrichment fingerprint')
    bounded(encode(value), STATE)
    return value


def select(records, state, now):
    due = []
    for record in records:
        if not identity(record)['repo']:
            continue
        previous = state['records'].get(record['id'], {})
        if parsed(previous.get('retry_at')) > now:
            continue
        changed = previous.get('fingerprint') != fingerprint(record)
        docs_due = now - parsed(previous.get('docs_checked_at')) >= DOC_TTL
        ci_due = not identity(record)['path'] and now - parsed(previous.get('ci_checked_at')) >= CI_TTL
        if changed or docs_due or ci_due:
            due.append(record)
    # Oldest attempt first among changed/overdue work, including failed attempts:
    # a permanently broken first record cannot starve the rest of the queue.
    return sorted(due, key=lambda r: (parsed(state['records'].get(r['id'], {}).get('last_attempt_at')), r['id']))


class BudgetStop(Exception):
    pass


class FetchFailure(Exception):
    def __init__(self, message, *, rate_limited=False):
        super().__init__(message)
        self.rate_limited = rate_limited


class Budget:
    def __init__(self, seconds=600, requests=300, *, clock=time.monotonic):
        if seconds <= 0 or requests < 0:
            raise ValueError('Collection budgets must be positive (requests may be zero)')
        self.clock, self.start = clock, clock()
        self.deadline, self.limit = self.start + seconds, requests
        self.requests, self.statuses, self.http_seconds, self.cache_hits = 0, {}, 0.0, 0

    def check(self, reserve=0):
        if self.clock() >= self.deadline:
            raise BudgetStop('wall-time budget')
        if self.requests + reserve > self.limit:
            raise BudgetStop('request budget')

    def before_request(self):
        self.check(1)
        self.requests += 1
        return min(10.0, max(0.05, self.deadline - self.clock()))

    def summary(self):
        return {'requests': self.requests, 'request_limit': self.limit,
                'statuses': self.statuses, 'http_seconds': round(self.http_seconds, 3),
                'elapsed_seconds': round(self.clock() - self.start, 3), 'cache_hits': self.cache_hits}


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, request, response, code, message, headers, target):
        return None  # Redirect hops must consume the explicit request budget.


class Redirect(Exception):
    pass


class Client:
    def __init__(self, budget, *, token=None, opener=None):
        self.budget, self.opener = budget, opener or build_opener(NoRedirect()).open
        self.token = os.environ.get('GITHUB_TOKEN', '') if token is None else token
        self.heads, self.ci_results = {}, {}

    def get(self, url, kind, *, absence=False):
        for _ in range(4):
            try:
                return self._get_once(url, kind, absence=absence)
            except Redirect as exc:
                target = urljoin(url, str(exc))
                parts = urlsplit(target)
                if parts.scheme != 'https' or parts.netloc not in {'api.github.com', 'raw.githubusercontent.com'}:
                    raise FetchFailure('unsupported redirect') from exc
                url = target
        raise FetchFailure('redirect limit')

    def _get_once(self, url, kind, *, absence=False):
        timeout, started = self.budget.before_request(), self.budget.clock()
        headers = {'User-Agent': 'legacy-reverse-engineering-tracker', 'Accept': 'application/vnd.github+json'}
        if url.startswith(evidence.API + '/') and self.token:
            headers['Authorization'] = 'Bearer ' + self.token
        status = 'network-error'
        try:
            with self.opener(Request(url, headers=headers), timeout=timeout) as response:
                status = str(response.status)
                content = bytearray()
                while True:
                    self.budget.check()
                    chunk = response.read(min(65536, MAX_RESPONSE + 1 - len(content)))
                    if not chunk:
                        break
                    content.extend(chunk)
                    if len(content) > MAX_RESPONSE:
                        raise FetchFailure('oversized response')
                return bytes(content).decode('utf-8', errors='strict')
        except HTTPError as exc:
            status = str(exc.code)
            if exc.code in {301, 302, 303, 307, 308} and exc.headers.get('Location'):
                raise Redirect(exc.headers['Location']) from exc
            if absence and exc.code == 404:
                return None  # Only immutable paths under a confirmed accessible commit.
            raise FetchFailure('HTTP ' + status, rate_limited=exc.code == 429 or
                               (exc.code == 403 and (exc.headers.get('X-RateLimit-Remaining') == '0' or bool(exc.headers.get('Retry-After'))))) from exc
        except (URLError, TimeoutError, UnicodeError, OSError, HTTPException) as exc:
            raise FetchFailure(type(exc).__name__) from exc
        finally:
            elapsed = self.budget.clock() - started
            self.budget.http_seconds += elapsed
            self.budget.statuses[status] = self.budget.statuses.get(status, 0) + 1
            log(request=self.budget.requests, kind=kind, status=status, seconds=round(elapsed, 3))

    def head(self, target):
        key = target['repo'], target['branch']
        if key not in self.heads:
            text = self.get(f"{evidence.API}/repos/{key[0]}/git/ref/heads/{quote(key[1], safe='/')}", 'head')
            try:
                obj = json.loads(text)['object']
                sha = obj['sha']
                if obj.get('type') != 'commit' or not re.fullmatch(r'[0-9a-f]{40}', sha):
                    raise ValueError('invalid commit')
            except (ValueError, KeyError, TypeError) as exc:
                raise FetchFailure('invalid head response') from exc
            self.heads[key] = sha
        return self.heads[key]

    def ci(self, target, day):
        key = target['repo'], target['branch']
        if key in self.ci_results:
            self.budget.cache_hits += 1
            return copy.deepcopy(self.ci_results[key])
        query = urlencode({'branch': target['branch'], 'status': 'completed', 'per_page': 30})
        text = self.get(f"{evidence.API}/repos/{target['repo']}/actions/runs?{query}", 'ci')
        try:
            runs = json.loads(text)['workflow_runs']
            if not isinstance(runs, list):
                raise ValueError('invalid workflows')
            result, names = [], set()
            for run in runs:
                name = run.get('name') or ''
                if name in names or not evidence.CI_NAME.search(name) or evidence.CI_EXCLUDE.search(name):
                    continue
                names.add(name)
                result.append({'workflow': name, 'conclusion': run.get('conclusion'), 'event': run.get('event'),
                               'branch': run.get('head_branch'), 'url': run.get('html_url'),
                               'completed_at': (run.get('updated_at') or '')[:10] or None,
                               'checked_at': day, 'collector': evidence.COLLECTOR, 'strength': 'supporting'})
                if len(result) == 5:
                    break
        except (ValueError, KeyError, TypeError, AttributeError) as exc:
            raise FetchFailure('invalid CI response') from exc
        self.ci_results[key] = result
        return copy.deepcopy(result)


def doc_payload(auto):
    return {field: copy.deepcopy(auto.get(field, [])) for field in DOC_FIELDS}


def without_checked(value):
    if isinstance(value, dict):
        return {k: without_checked(v) for k, v in value.items() if k != 'checked_at'}
    if isinstance(value, list):
        return [without_checked(v) for v in value]
    return value


def collect_record(record, previous, client, now):
    target, day = identity(record), now.date().isoformat()
    if any(key in record and not isinstance(record[key], dict) for key in ('build', 'evidence')):
        raise FetchFailure('invalid project build/evidence container')
    commit = client.head(target)
    old_auto = (record.get('evidence') or {}).get('automated') or {}
    base = target['path']
    paths = [f'{base}/{name}' if base else name for name in evidence.DOCS] + ([] if base else evidence.ROOT_EXTRA)
    key = digest({**target, 'commit': commit, 'paths': paths, 'collector': evidence.COLLECTOR})
    cache = (previous.get('docs_key') == key and previous.get('docs_digest') == digest(doc_payload(old_auto)))
    ci_due = not base and (previous.get('fingerprint') != fingerprint(record) or
                          now - parsed(previous.get('ci_checked_at')) >= CI_TTL)
    # Reserve enough requests for a whole record before expensive document work.
    client.budget.check((0 if cache else len(paths)) + int(ci_due))
    if cache:
        auto = doc_payload(old_auto)
        client.budget.cache_hits += 1
    else:
        auto = {field: [] for field in DOC_FIELDS}
        found = 0
        for path in paths:
            text = client.get(evidence.raw(target['repo'], commit, path), 'document', absence=True)
            if text is None:
                continue
            auto['compilable'] += evidence.scan_bool(text, target['repo'], commit, path, evidence.POS_COMPILE, evidence.NEG_COMPILE)
            auto['playable'] += evidence.scan_bool(text, target['repo'], commit, path, evidence.POS_PLAY, evidence.NEG_PLAY)
            auto['byte_exact'] += evidence.scan_bool(text, target['repo'], commit, path, evidence.POS_BYTE, evidence.NEG_BYTE, evidence.BYTE_REJECT)
            auto['re_started'] += evidence.scan_start(text, target['repo'], commit, path)
            client.budget.check()
            found += 1
            if found == 6:
                break
        auto = {field: evidence.uniq(values) for field, values in auto.items()}
        for values in auto.values():
            for item in values:
                item['checked_at'] = day
    ci_failure = None
    ci_values = [] if base else copy.deepcopy(old_auto.get('ci', []))
    if ci_due:
        try:
            ci_values = client.ci(target, day)
        except (FetchFailure, BudgetStop) as exc:
            # Documentation is independently complete. Publish that evidence,
            # retain prior CI signals and leave CI freshness due for a retry.
            ci_failure = exc
    auto.update(collector=evidence.COLLECTOR, checked_at=day, ci=ci_values)
    # Freshness lives in scheduler state. Identical evidence keeps canonical bytes.
    if without_checked(auto) == without_checked({k: v for k, v in old_auto.items() if k != 'applied'}):
        auto = copy.deepcopy(old_auto)
        auto.pop('applied', None)
    candidate = copy.deepcopy(record)
    evidence.apply(candidate, auto)
    after = {**previous, 'fingerprint': fingerprint(record), 'last_attempt_at': stamp(now),
             'docs_key': key, 'docs_digest': digest(doc_payload(auto)), 'docs_checked_at': stamp(now), 'failures': 0}
    after.pop('retry_at', None)
    if ci_due and ci_failure is None:
        after['ci_checked_at'] = stamp(now)
    return candidate, after, ci_failure


def value_at(record, path):
    value = record
    for key in path:
        if not isinstance(value, dict) or key not in value:
            return {'exists': False}
        value = value[key]
    return {'exists': True, 'value': copy.deepcopy(value)}


def writable_parent(record, path):
    target = record
    if not isinstance(target, dict):
        return False
    for key in path[:-1]:
        if key not in target:
            return True
        target = target[key]
        if not isinstance(target, dict):
            return False
    return True


def patch_between(before, after):
    return [{'path': list(path), 'before': value_at(before, path), 'after': value_at(after, path)}
            for path in OWNED if value_at(before, path) != value_at(after, path)]


def collect(root, bundle, budget, *, limit=20, now=None, client=None):
    now = now or datetime.now(timezone.utc)
    if Path(bundle).exists():
        raise ValueError('Collection bundle already exists; choose a fresh path')
    records, state = load_projects(Path(root) / 'data/projects.json'), state_read(root)
    client = client or Client(budget)
    due, results = select(records, state, now), []
    for record in due[:limit]:
        try:
            budget.check(1)
        except BudgetStop as exc:
            log(stop=str(exc)); break
        previous = copy.deepcopy(state['records'].get(record['id'], {}))
        stop = False
        try:
            candidate, after, ci_failure = collect_record(record, previous, client, now)
            outcome = {'status': 'complete' if ci_failure is None else 'partial',
                       'patch': patch_between(record, candidate), 'state_after': after}
            if ci_failure is not None:
                failures = min(5, previous.get('failures', 0) + int(isinstance(ci_failure, FetchFailure)))
                after['failures'] = failures
                if isinstance(ci_failure, FetchFailure):
                    after['retry_at'] = stamp(now + timedelta(hours=2 ** (failures - 1)))
                outcome['reason'] = str(ci_failure)
                stop = isinstance(ci_failure, BudgetStop) or ci_failure.rate_limited
        except (FetchFailure, BudgetStop) as exc:
            stop = isinstance(exc, BudgetStop) or (isinstance(exc, FetchFailure) and exc.rate_limited)
            failures = min(5, previous.get('failures', 0) + int(isinstance(exc, FetchFailure)))
            after = {**previous, 'last_attempt_at': stamp(now), 'failures': failures}
            if isinstance(exc, FetchFailure):
                after['retry_at'] = stamp(now + timedelta(hours=min(24, 2 ** (failures - 1))))
            outcome = {'status': 'deferred', 'patch': [], 'state_after': after, 'reason': str(exc)}
        results.append({'id': record['id'], 'fingerprint': fingerprint(record), 'state_before': previous,
                        'guards': [{'path': list(path), 'before': value_at(record, path)} for path in OWNED], **outcome})
        log(project=record['id'], status=outcome['status'], completed=sum(r['status'] == 'complete' for r in results),
            **budget.summary())
        if stop:
            break
    result = {'version': 1, 'created_at': stamp(now), 'results': results, 'summary': {
        'due': len(due), 'attempted': len(results), 'completed': sum(r['status'] == 'complete' for r in results),
        'partial': sum(r['status'] == 'partial' for r in results),
        'deferred': sum(r['status'] == 'deferred' for r in results), **budget.summary()}}
    path = Path(bundle)
    if path.exists():
        raise ValueError('Collection bundle already exists; choose a fresh path')
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_bytes(encode(result)); temporary.replace(path)
    log(collection=result['summary'])
    return result


def replay(records, state, bundle):
    """Compare-and-set owned leaves; never replace a current project snapshot."""
    if bundle.get('version') != 1:
        raise ValueError('Invalid collection bundle')
    records, state = copy.deepcopy(records), copy.deepcopy(state)
    by_id = {r['id']: r for r in records}
    eligible = {r['id'] for r in records if identity(r)['repo']}
    state['records'] = {pid: entry for pid, entry in state['records'].items() if pid in eligible}
    accepted, conflicts = [], []
    for result in bundle['results']:
        record = by_id.get(result['id'])
        current_state = state['records'].get(result['id'], {})
        patches = {tuple(p['path']): p for p in result['patch']}
        guards = result.get('guards', [])
        safe = (set(patches).issubset(OWNED) and {tuple(g['path']) for g in guards} == set(OWNED)
                and all(writable_parent(record, p['path']) for p in result['patch']))
        fresh = (current_state == result['state_before'] and all(
            value_at(record, g['path']) == g['before'] for g in guards))
        already = (current_state == result['state_after'] and all(
            value_at(record, g['path']) == patches.get(tuple(g['path']), {}).get('after', g['before']) for g in guards))
        if record is None or fingerprint(record) != result['fingerprint'] or not safe or not (fresh or already):
            conflicts.append(result['id']); continue
        for patch in result['patch']:
            target = record
            for key in patch['path'][:-1]:
                target = target.setdefault(key, {})
            if patch['after']['exists']:
                target[patch['path'][-1]] = copy.deepcopy(patch['after']['value'])
            else:
                target.pop(patch['path'][-1], None)
        state['records'][result['id']] = copy.deepcopy(result['state_after'])
        accepted.append(result['id'])
    bounded(encode(state), STATE)
    return records, state, {'accepted': accepted, 'conflicts': conflicts}


class PublicationPending(Exception):
    pass


def sync_material(staged, root, before, records):
    """Use the existing event recorder, only for a healthy material baseline."""
    from record_project_activity import snapshot, main as record_activity
    if {r['id']: snapshot(r) for r in before} == {r['id']: snapshot(r) for r in records}:
        return False
    catalogue_path = root / 'state/project-catalog-state.json'
    catalogue = json.loads(catalogue_path.read_bytes())
    previous = {pid: snapshot(record) for pid, record in catalogue.get('projects', {}).items()}
    if previous != {r['id']: snapshot(r) for r in before}:
        raise PublicationPending('Latest main has unrecorded catalogue changes; wait for metadata refresh')
    (staged / 'state').mkdir(exist_ok=True)
    for name in ('project-catalog-state.json', 'github-poll-state.json'):
        source = root / 'state' / name
        if source.exists():
            shutil.copy2(source, staged / 'state' / name)
    record_activity(staged)
    return True


def apply_bundle(root, bundle):
    from validate_site_data import validate
    root = Path(root)
    before = load_projects(root / 'data/projects.json')
    records, state, summary = replay(before, state_read(root), bundle)
    # Stage and validate before making any working-tree changes. Publication is
    # one atomic fast-forward Git commit containing both data and progress.
    with tempfile.TemporaryDirectory(prefix='enrichment-stage-') as temporary:
        staged = Path(temporary)
        shutil.copytree(root / 'data', staged / 'data')
        write_projects(staged / 'data/projects.json', records)
        material_changed = sync_material(staged, root, before, records)
        validate(staged / 'data/projects.json', staged / 'data/activity.json')
        content = bounded(encode(state), STATE)
        write_projects(root / 'data/projects.json', load_projects(staged / 'data/projects.json'))
        if material_changed:
            shutil.copy2(staged / 'data/activity.json', root / 'data/activity.json')
            shutil.copy2(staged / 'state/project-catalog-state.json', root / 'state/project-catalog-state.json')
        path = root / STATE
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
    summary['material_changes'] = material_changed
    log(replay=summary)
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    for command in ('collect', 'apply'):
        sub = commands.add_parser(command)
        sub.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
        sub.add_argument('--bundle', type=Path, required=True)
        if command == 'collect':
            sub.add_argument('--seconds', type=int, default=600)
            sub.add_argument('--requests', type=int, default=300)
            sub.add_argument('--records', type=int, default=20)
    args = parser.parse_args()
    if args.root.resolve() in args.bundle.resolve().parents:
        parser.error('Collection bundle must be outside the checkout (use RUNNER_TEMP)')
    if args.command == 'collect':
        if not 1 <= args.seconds <= 600 or not 0 <= args.requests <= 1000 or not 1 <= args.records <= 100:
            parser.error('Budgets: seconds 1..600, requests 0..1000, records 1..100')
        collect(args.root, args.bundle, Budget(args.seconds, args.requests), limit=args.records)
    else:
        try:
            apply_bundle(args.root, json.loads(args.bundle.read_bytes()))
        except PublicationPending as exc:
            parser.exit(75, str(exc) + '\n')


if __name__ == '__main__':
    main()
