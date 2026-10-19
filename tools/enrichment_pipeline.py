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

from collection_budget import Budget, BudgetStop, LaneStop, APIStop, FetchFailure, RecordStop

import enrich_evidence as evidence
from catalogue_storage import bounded, encode, load_projects, write_projects

STATE = 'state/enrichment-state.json'
DOC_FIELDS = ('compilable', 'playable', 'byte_exact', 're_started')
OWNED = [('evidence', 'automated'), ('re_started',),
         *(('build', key) for key in (*DOC_FIELDS[:3], 'runnable'))]
# Eligibility leaves the measured backlog-drain margin before freshness targets.
DOC_TTL = timedelta(days=10)  # 30-day objective minus 20-day cold reserve drain.
CI_TTL = timedelta(days=4)    # Seven-day objective minus three-day CI reserve drain.
METADATA_MAX_AGE = timedelta(hours=13)
MAX_RESPONSE = 700_000
STATE_FIELDS = {'fingerprint', 'last_attempt_at', 'docs_key', 'docs_digest', 'docs_checked_at',
                'ci_checked_at', 'failures', 'retry_at', 'ci_fingerprint', 'ci_attempt_at', 'ci_retry_at', 'ci_failures',
                'docs_observed_fingerprint', 'ci_observed_fingerprint'}


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
            elif key in {'failures', 'ci_failures'}:
                if type(item) is not int or not 0 <= item <= 5:
                    raise ValueError('Invalid enrichment failure count')
            elif not isinstance(item, str) or not re.fullmatch(r'[0-9a-f]{64}', item):
                raise ValueError('Invalid enrichment fingerprint')
    bounded(encode(value), STATE)
    return value


def poll_read(root):
    path = Path(root) / 'state/github-poll-state.json'
    return json.loads(path.read_bytes()).get('repositories', {}) if path.exists() else {}


def source_fingerprint(record, polling):
    target = identity(record)
    repo = polling.get(target['repo'], {})
    if not repo:
        return fingerprint(record)
    branch = repo.get('branches', {}).get(target['branch'], {})
    # Project pushed_at is day-only and latest_commit can be path-filtered or
    # historical. The poller's full timestamp + observed branch tip detects
    # same-day pushes, including pushes outside a monorepo project's path.
    return digest({'project': fingerprint(record), 'pushed_at': repo.get('last_seen_pushed_at'),
                   'tip': branch.get('tip_sha')})


def metadata_commit(record, polling, now):
    target = identity(record)
    repo = polling.get(target['repo'], {})
    branch = repo.get('branches', {}).get(target['branch'], {})
    tip = branch.get('tip_sha')
    work = repo.get('publication') or {}
    pending = work and (not work.get('metadata_complete') or not work.get('history_complete'))
    if (not isinstance(tip, str) or not re.fullmatch(r'[0-9a-f]{40}', tip)
            or repo.get('scan_requested') or repo.get('last_error') or pending
            or not repo.get('last_seen_pushed_at') or not repo.get('last_deep_scan')
            or not repo.get('last_probe_at')):
        return None
    try:
        age = now - parsed(repo['last_probe_at'])
        if not timedelta(0) <= age <= METADATA_MAX_AGE:
            return None
        if parsed(repo['last_deep_scan']) < parsed(repo['last_seen_pushed_at']):
            return None
    except (ValueError, TypeError):
        return None
    return tip


def queues(records, state, now, *, work='docs', polling=None):
    changed, overdue = [], []
    polling = polling or {}
    ci = work == 'ci'
    fp_key, time_key = ('ci_fingerprint', 'ci_checked_at') if ci else ('fingerprint', 'docs_checked_at')
    retry_key = 'ci_retry_at' if ci else 'retry_at'
    attempt_key = 'ci_attempt_at' if ci else 'last_attempt_at'
    for record in records:
        target = identity(record)
        if not target['repo'] or (ci and target['path']):
            continue
        previous = state['records'].get(record['id'], {})
        if parsed(previous.get(retry_key)) > now:
            continue
        prior = previous.get(fp_key)
        reference = prior or previous.get('ci_observed_fingerprint' if ci else 'docs_observed_fingerprint') or previous.get('fingerprint' if ci else 'ci_fingerprint')
        is_changed = bool(reference) and reference != source_fingerprint(record, polling)
        if is_changed:
            changed.append(record)
        elif not prior or now - parsed(previous.get(time_key)) >= (CI_TTL if ci else DOC_TTL):
            overdue.append(record)
    order = lambda r: (parsed(state['records'].get(r['id'], {}).get(attempt_key)), r['id'])
    return sorted(changed, key=order), sorted(overdue, key=order)


def select(records, state, now, *, work='docs', polling=None):
    changed, overdue = queues(records, state, now, work=work, polling=polling)
    return changed + overdue




class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, request, response, code, message, headers, target):
        return None  # Redirect hops must consume the explicit request budget.


class Redirect(Exception):
    pass


class Client:
    def __init__(self, budget, *, token=None, opener=None):
        self.budget, self.opener = budget, opener or build_opener(NoRedirect()).open
        self.token = os.environ.get('GITHUB_TOKEN', '') if token is None else token
        self.heads, self.ci_results, self.accessible_commits = {}, {}, set()

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
        timeout, started = self.budget.before_request(api=url.startswith(evidence.API + '/')), self.budget.clock()
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
                return None  # Caller confirms accessibility before accepting all-missing cached tips.
            raise FetchFailure('HTTP ' + status, rate_limited=exc.code == 429 or
                               (exc.code == 403 and (exc.headers.get('X-RateLimit-Remaining') == '0' or bool(exc.headers.get('Retry-After'))))) from exc
        except (URLError, TimeoutError, UnicodeError, OSError, HTTPException) as exc:
            raise FetchFailure(type(exc).__name__) from exc
        finally:
            elapsed = self.budget.clock() - started
            self.budget.http_seconds += elapsed
            self.budget.statuses[status] = self.budget.statuses.get(status, 0) + 1
            log(request=self.budget.requests, lane=self.budget.lane_name, kind=kind, status=status, seconds=round(elapsed, 3))

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

    def confirm_commit(self, target, commit):
        """Confirm negative document results against the same cached commit."""
        key = target['repo'], commit
        if key in self.accessible_commits:
            self.budget.cache_hits += 1
            return
        text = self.get(f"{evidence.API}/repos/{key[0]}/git/commits/{commit}", 'confirm-commit')
        try:
            if json.loads(text)['sha'] != commit:
                raise ValueError('commit mismatch')
        except (ValueError, KeyError, TypeError) as exc:
            raise FetchFailure('invalid commit confirmation') from exc
        self.accessible_commits.add(key)

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


def collect_record(record, previous, client, now, *, work='docs', polling=None):
    target, day = identity(record), now.date().isoformat()
    if any(key in record and not isinstance(record[key], dict) for key in ('build', 'evidence')):
        raise FetchFailure('invalid project build/evidence container')
    signal = source_fingerprint(record, polling or {})
    old_auto = (record.get('evidence') or {}).get('automated') or {}
    if work == 'ci':
        # Actions already filters by the configured branch. No branch-head or
        # document request is necessary, including for a cold CI backlog.
        values = client.ci(target, day)
        auto = copy.deepcopy(old_auto) if old_auto else {'collector': evidence.COLLECTOR, 'checked_at': day}
        auto['ci'] = values
        candidate = copy.deepcopy(record)
        if without_checked(auto) != without_checked(old_auto):
            auto['checked_at'] = day
            if values or any(auto.get(field) for field in DOC_FIELDS) or auto.get('applied'):
                candidate.setdefault('evidence', {})['automated'] = auto
            else:
                candidate.setdefault('evidence', {}).pop('automated', None)
        after = {**previous, 'ci_fingerprint': signal, 'ci_attempt_at': stamp(now),
                 'ci_checked_at': stamp(now), 'ci_failures': 0}
        after.pop('ci_retry_at', None)
        after.pop('ci_observed_fingerprint', None)
        return candidate, after
    commit = metadata_commit(record, polling or {}, now)
    metadata_tip = commit is not None
    if commit:
        client.budget.cache_hits += 1
    else:
        commit = client.head(target)
    old_auto = (record.get('evidence') or {}).get('automated') or {}
    base = target['path']
    paths = [f'{base}/{name}' if base else name for name in evidence.DOCS] + ([] if base else evidence.ROOT_EXTRA)
    key = digest({**target, 'commit': commit, 'paths': paths, 'collector': evidence.COLLECTOR})
    cache = (previous.get('docs_key') == key and previous.get('docs_digest') == digest(doc_payload(old_auto)))
    # Reserve enough requests for a whole record before expensive document work.
    client.budget.check(0 if cache else len(paths))
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
        if metadata_tip and found == 0:
            # A poll tip can predate a visibility change or inaccessible commit.
            # Raw 404s alone must not retract evidence from that earlier scan.
            client.confirm_commit(target, commit)
        auto = {field: evidence.uniq(values) for field, values in auto.items()}
        for values in auto.values():
            for item in values:
                item['checked_at'] = day
    auto.update(collector=evidence.COLLECTOR, checked_at=day,
                ci=[] if base else copy.deepcopy(old_auto.get('ci', [])))
    if without_checked(auto) == without_checked({k: v for k, v in old_auto.items() if k != 'applied'}):
        auto = copy.deepcopy(old_auto)
        auto.pop('applied', None)
    candidate = copy.deepcopy(record)
    evidence.apply(candidate, auto)
    after = {**previous, 'fingerprint': signal, 'last_attempt_at': stamp(now),
             'docs_key': key, 'docs_digest': digest(doc_payload(auto)), 'docs_checked_at': stamp(now), 'failures': 0}
    after.pop('retry_at', None)
    after.pop('docs_observed_fingerprint', None)
    return candidate, after


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


def collect(root, bundle, budget, *, limit=None, docs_limit=64, ci_limit=60, now=None, client=None):
    now = now or datetime.now(timezone.utc)
    if Path(bundle).exists():
        raise ValueError('Collection bundle already exists; choose a fresh path')
    records, state = load_projects(Path(root) / 'data/projects.json'), state_read(root)
    polling = poll_read(root)
    client = client or Client(budget)
    originals = {r['id']: r for r in records}
    working, progress = copy.deepcopy(originals), copy.deepcopy(state['records'])
    pending = {work: queues(records, state, now, work=work, polling=polling)
               if (ci_limit if work == 'ci' else docs_limit) else ([], []) for work in ('ci', 'docs')}
    if limit is not None:
        order = pending['ci'][0] + pending['docs'][0] + pending['ci'][1] + pending['docs'][1]
        allowed = set(list(dict.fromkeys(r['id'] for r in order))[:limit])
        pending = {work: tuple([r for r in group if r['id'] in allowed] for group in groups) for work, groups in pending.items()}
    required = {}
    for work, groups in pending.items():
        if (ci_limit if work == 'ci' else docs_limit) == 0:
            continue
        for record in groups[0] + groups[1]:
            required.setdefault(record['id'], set()).add(work)
    outcomes, attempted = {}, {'ci': set(), 'docs': set()}
    completed = {'ci': 0, 'docs': 0}
    stop_all = False
    # At most 20% of the existing 300-request ceiling goes to one-request CI
    # work (60/h). Documents receive the remainder and any unused CI allocation.
    ci_cap = min(ci_limit, budget.limit // 5)
    ci_deadline = budget.clock() + max(0, budget.deadline - budget.clock()) * .3
    for work, record_cap in (('ci', ci_limit), ('docs', docs_limit)):
        if not record_cap or stop_all:
            continue
        changed, overdue = pending[work]
        request_cap = ci_cap if work == 'ci' else max(0, budget.limit - budget.requests)
        started_requests, started_clock = budget.requests, budget.clock()
        started_api = budget.api_requests
        api_cap = min(ci_cap, budget.api_limit - started_api) if work == 'ci' else max(0, budget.api_limit - started_api)
        deadline = ci_deadline if work == 'ci' else budget.deadline
        fraction = (.25 if work == 'ci' else .5) if overdue else 1.0
        priority_records = max(1, int(record_cap * fraction))
        for priority in (True, False):
            if stop_all:
                break
            spent = budget.requests - started_requests
            requests = int(request_cap * fraction) if priority else max(0, request_cap - spent)
            lane_deadline = started_clock + max(0, deadline - started_clock) * fraction if priority else deadline
            api_requests = int(api_cap * fraction) if priority else max(0, api_cap - (budget.api_requests - started_api))
            budget.begin_lane(work + ('.changed' if priority else '.overdue'), requests, lane_deadline, api_requests)
            candidates = changed if priority else overdue + changed
            for record in candidates:
                pid = record['id']
                if pid in attempted[work]:
                    continue
                if len(attempted[work]) >= (priority_records if priority else record_cap):
                    break
                if limit is not None and pid not in outcomes and len(outcomes) >= limit:
                    continue
                try:
                    budget.check(1)
                except BudgetStop as exc:
                    stop_all = exc.scope == 'global'; break
                attempted[work].add(pid)
                previous = copy.deepcopy(progress.get(pid, {}))
                signal = source_fingerprint(record, polling)
                # Observation is not completion. Preserve an unfinished lane's
                # old input baseline when the other lane publishes newer work.
                if not previous.get('fingerprint'):
                    previous.setdefault('docs_observed_fingerprint', previous.get('ci_fingerprint') or signal)
                if not identity(record)['path'] and not previous.get('ci_fingerprint'):
                    previous.setdefault('ci_observed_fingerprint', previous.get('fingerprint') or signal)
                info = outcomes.setdefault(pid, {})
                stop_phase = False
                budget.begin_record()
                try:
                    candidate, after = collect_record(working[pid], previous, client, now, work=work, polling=polling)
                    working[pid], progress[pid] = candidate, after
                    info[work] = 'complete'
                    completed[work] += 1
                except (FetchFailure, BudgetStop) as exc:
                    attempt_key, failure_key, retry_key = (('ci_attempt_at', 'ci_failures', 'ci_retry_at')
                                                         if work == 'ci' else ('last_attempt_at', 'failures', 'retry_at'))
                    failures = min(5, previous.get(failure_key, 0) + int(isinstance(exc, FetchFailure)))
                    after = {**previous, failure_key: failures}
                    if isinstance(exc, FetchFailure):
                        after[attempt_key] = stamp(now)
                        after[retry_key] = stamp(now + timedelta(hours=2 ** (failures - 1)))
                    progress[pid] = after
                    info[work] = 'deferred'
                    info[work + '_reason'] = str(exc)
                    stop_all = (isinstance(exc, BudgetStop) and exc.scope == 'global') or (isinstance(exc, FetchFailure) and exc.rate_limited)
                    stop_phase = isinstance(exc, BudgetStop) or stop_all
                budget.end_record()
                log(project=pid, work=work, status=info[work], reason=info.get(work + '_reason'), completed=sum(
                    all(v.get(task) == 'complete' for task in required[key]) for key, v in outcomes.items()),
                    docs_completed=completed['docs'], ci_completed=completed['ci'], **budget.summary())
                if stop_phase:
                    break
            budget.end_lane()
    results = []
    for pid, info in outcomes.items():
        done = {work for work in ('ci', 'docs') if info.get(work) == 'complete'}
        status = 'complete' if required[pid] <= done else 'partial' if done else 'deferred'
        results.append({'id': pid, 'fingerprint': fingerprint(originals[pid]),
                        'source_fingerprint': source_fingerprint(originals[pid], polling),
                        'state_before': state['records'].get(pid, {}), 'state_after': progress[pid],
                        'guards': [{'path': list(path), 'before': value_at(originals[pid], path)} for path in OWNED],
                        'patch': patch_between(originals[pid], working[pid]), 'status': status, 'work': info})
    result = {'version': 1, 'created_at': stamp(now), 'results': results, 'summary': {
        'due': len(required), 'docs_due': sum(len(q) for q in pending['docs']), 'ci_due': sum(len(q) for q in pending['ci']),
        'docs_changed_due': len(pending['docs'][0]), 'ci_changed_due': len(pending['ci'][0]),
        'attempted': len(results), 'completed': sum(r['status'] == 'complete' for r in results),
        'partial': sum(r['status'] == 'partial' for r in results), 'deferred': sum(r['status'] == 'deferred' for r in results),
        'docs_completed': completed['docs'], 'ci_completed': completed['ci'], **budget.summary()}}
    path = Path(bundle)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_bytes(encode(result)); temporary.replace(path)
    log(collection=result['summary'])
    return result


def replay(records, state, bundle, *, polling=None):
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
        if (record is None or fingerprint(record) != result['fingerprint'] or not safe or not (fresh or already)
                or ('source_fingerprint' in result and result['source_fingerprint'] != source_fingerprint(record, polling or {}))):
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
    records, state, summary = replay(before, state_read(root), bundle, polling=poll_read(root))
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
            sub.add_argument('--api-requests', type=int, default=80)
            sub.add_argument('--records', type=int, default=0, help='Optional total project cap; zero uses separate work limits')
            sub.add_argument('--doc-records', type=int, default=64)
            sub.add_argument('--ci-records', type=int, default=60)
    args = parser.parse_args()
    if args.root.resolve() in args.bundle.resolve().parents:
        parser.error('Collection bundle must be outside the checkout (use RUNNER_TEMP)')
    if args.command == 'collect':
        if not 1 <= args.seconds <= 600 or not 0 <= args.requests <= 1000 or not 0 <= args.api_requests <= 200 or not 0 <= args.records <= 256 or not 0 <= args.doc_records <= 256 or not 0 <= args.ci_records <= 256:
            parser.error('Budgets: seconds 1..600, requests 0..1000, API requests 0..200, record caps 0..256')
        collect(args.root, args.bundle, Budget(args.seconds, args.requests, api_requests=args.api_requests), limit=args.records or None, docs_limit=args.doc_records, ci_limit=args.ci_records)
    else:
        try:
            apply_bundle(args.root, json.loads(args.bundle.read_bytes()))
        except PublicationPending as exc:
            parser.exit(75, str(exc) + '\n')


if __name__ == '__main__':
    main()
