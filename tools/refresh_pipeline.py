#!/usr/bin/env python3
"""Bounded repository refresh, durable work cycles, and offline publication replay."""

from __future__ import annotations

import argparse
import copy
from contextlib import contextmanager, redirect_stdout
from datetime import datetime, timedelta, timezone
import hashlib
from io import StringIO
import json
import os
from pathlib import Path
import shutil
import tempfile
from urllib.parse import quote, urlencode

import collect_activity as activity
import refresh_github as probe
from activity_history import compact_history, freeze_addition_context, write_activity
from catalogue_storage import bounded, encode, load_projects, write_projects, storage_paths
from collection_budget import Budget, BudgetStop, RecordStop
from merge_pending_projects import main as merge_pending
from record_project_activity import main as record_catalogue, snapshot
from refresh_scope import catalogue_delta, pending_publication, prepare_publication, repository
from validate_site_data import validate

PROGRESS = "state/refresh-progress.json"
POLL = "state/github-poll-state.json"
OWNED = ("github", "last_activity", "last_checked", "ai")


def log(**value):
    print(json.dumps(value, separators=(",", ":"), ensure_ascii=False), flush=True)


def stamp(now):
    return now.astimezone(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def digest(value):
    return hashlib.sha256(encode(value)).hexdigest()


def read(path, default):
    return json.loads(path.read_bytes()) if path.exists() else copy.deepcopy(default)


def progress_read(root):
    value = read(
        Path(root) / PROGRESS,
        {"version": 1, "revision": 0, "cycle": None, "retry": {"probe": {}, "activity": {}}},
    )
    if value.get("version") != 1 or type(value.get("revision")) is not int or value["revision"] < 0:
        raise ValueError("Invalid refresh progress")
    for work in ("probe", "activity"):
        if not isinstance(value.get("retry", {}).get(work), dict):
            raise ValueError("Invalid refresh retry queue")
    cycle = value.get("cycle")
    if cycle:
        if not isinstance(cycle.get("id"), str):
            raise ValueError("Invalid refresh cycle")
        for work in ("probe", "activity"):
            for field in ("targets", "pending"):
                rows = cycle.get(field, {}).get(work)
                if (
                    not isinstance(rows, list)
                    or any(not isinstance(r, str) for r in rows)
                    or len(set(rows)) != len(rows)
                ):
                    raise ValueError("Invalid refresh cycle queue")
            if not set(cycle["pending"][work]) <= set(cycle["targets"][work]):
                raise ValueError("Pending work outside refresh cycle")
    bounded(encode(value), PROGRESS)
    return value


def active(progress):
    return bool(progress.get("cycle") and any(progress["cycle"]["pending"].values()))


def token(progress):
    return f"{progress['cycle']['id']}:{progress['revision']}" if active(progress) else ""


def groups(records):
    out = {}
    for record in records:
        if repo := repository(record):
            out.setdefault(repo, []).append(record)
    return out


def source(records):
    return digest(sorted((snapshot(p) for p in records), key=lambda p: p["id"]))


def owned(record):
    return {key: {"exists": key in record, "value": copy.deepcopy(record.get(key))} for key in OWNED}


def due(repo, record_group, rs, now):
    latest = max((p.get("last_activity") or "" for p in record_group), default="")
    archived = any((p.get("github") or {}).get("archived") for p in record_group)
    old, old_today = probe.RUN_AT, probe.TODAY
    try:
        probe.RUN_AT, probe.TODAY = now, now.date()
        interval = probe.probe_interval_minutes(latest or None, archived)
        return probe.probe_due(repo, rs, interval)
    finally:
        probe.RUN_AT, probe.TODAY = old, old_today


def plan(progress, records, poll, now, request_id, full=False):
    progress = copy.deepcopy(progress)
    if (
        progress.get("blocked_until")
        and datetime.fromisoformat(progress["blocked_until"].replace("Z", "+00:00")) <= now
    ):
        progress.pop("blocked_until")
    by_repo = groups(records)
    repos = set(by_repo)
    if not active(progress) and not (full and progress.get("last_full_request") == request_id):
        probes = sorted(
            repo
            for repo, rows in by_repo.items()
            if full or due(repo, rows, poll["repositories"].get(repo, {}), now)
        )
        scans = sorted(
            repo for repo in repos if full or poll["repositories"].get(repo, {}).get("scan_requested")
        )
        progress["cycle"] = {
            "id": digest([request_id, progress["revision"], stamp(now)])[:24],
            "mode": "full" if full else "adaptive",
            "started_at": stamp(now),
            "targets": {"probe": probes[:], "activity": scans[:]},
            "pending": {"probe": probes[:], "activity": scans[:]},
        }
    if full and active(progress) and progress["cycle"]["mode"] != "full":
        # A manual full request upgrades an adaptive cycle without losing its
        # completed units or page cursors. Newly included repositories stay due.
        cycle = progress["cycle"]
        cycle["mode"] = "full"
        for work in ("probe", "activity"):
            extra = sorted(repos - set(cycle["targets"][work]))
            cycle["targets"][work].extend(extra)
            cycle["pending"][work].extend(extra)
    if full:
        progress["last_full_request"] = request_id
    cycle = progress.get("cycle")
    if cycle:
        for work in ("probe", "activity"):
            cycle["pending"][work] = [r for r in cycle["pending"][work] if r in repos]
            cycle["targets"][work] = [r for r in cycle["targets"][work] if r in repos]
        # New or changed catalogue work must survive a coalesced push run.
        for repo in sorted(repos):
            rs = poll["repositories"].get(repo, {})
            publication = rs.get("publication") or {}
            if pending_publication(rs):
                for work, complete in (("probe", "metadata_complete"), ("activity", "history_complete")):
                    if not publication.get(complete):
                        for field in ("targets", "pending"):
                            if repo not in cycle[field][work]:
                                cycle[field][work].append(repo)
    for work in ("probe", "activity"):
        progress["retry"][work] = {r: v for r, v in progress["retry"][work].items() if r in repos}
    return progress


def ready(progress, repo, work, now):
    retry = progress["retry"][work].get(repo, {}).get("retry_at")
    return not retry or datetime.fromisoformat(retry.replace("Z", "+00:00")) <= now


def candidates(progress, poll, work, now, cap):
    cycle = progress.get("cycle")
    if not cycle:
        return []
    rows = [r for r in cycle["pending"][work] if ready(progress, r, work, now)]

    def key(repo):
        rs = poll["repositories"].get(repo, {})
        last = (
            progress["retry"][work].get(repo, {}).get("attempt_at")
            or rs.get("last_probe_at" if work == "probe" else "last_deep_scan")
            or ""
        )
        return last, repo.casefold()

    priority = sorted((r for r in rows if pending_publication(poll["repositories"].get(r, {}))), key=key)
    ordinary = sorted(set(rows) - set(priority), key=key)
    share = max(1, cap // 4) if ordinary else len(priority)
    return priority[:share] + ordinary + priority[share:]


class Interrupted(BaseException):
    def __init__(self, cause):
        self.cause = cause


class Response:
    def __init__(self, response, budget):
        self.response, self.budget = response, budget

    def __enter__(self):
        self.response.__enter__()
        return self

    def __exit__(self, *args):
        return self.response.__exit__(*args)

    def __getattr__(self, key):
        return getattr(self.response, key)

    def read(self, size=-1):
        out = bytearray()
        while size < 0 or len(out) < size:
            try:
                self.budget.check()
            except (BudgetStop, RecordStop) as exc:
                raise Interrupted(exc) from exc
            chunk = self.response.read(min(65536, size - len(out)) if size >= 0 else 65536)
            if not chunk:
                break
            out.extend(chunk)
            if len(out) > 8 * 1024 * 1024:
                raise ValueError("Oversized GitHub API response")
        return bytes(out)


@contextmanager
def transport(module, budget, now, opener=None):
    names = (
        "urlopen",
        "api",
        "RUN_AT",
        "TODAY",
        "NOW",
        "NOW_ISO",
        "REQUESTS",
        "NOT_MODIFIED",
        "CONDITIONAL_REQUESTS",
        "STATUS_COUNTS",
        "RATE_LIMIT",
        "RATE_REMAINING",
        "RATE_RESET",
        "RATE_START_REMAINING",
        "PUBLICATION_REQUEST_LIMIT",
        "PUBLICATION_REQUESTS",
        "PUBLICATION_ACTIVE",
        "FORCE_FULL_PROBE",
    )
    before = {n: getattr(module, n) for n in names if hasattr(module, n)}
    original_api = module.api
    original_open = opener or module.urlopen

    def open_request(request, timeout=30):
        try:
            timeout = min(timeout, budget.before_request(api=True))
        except (BudgetStop, RecordStop) as exc:
            raise Interrupted(exc) from exc
        started = budget.clock()
        try:
            response = original_open(request, timeout=timeout)
        except Exception as exc:
            code = getattr(exc, "code", "error")
            budget.statuses[str(code)] = budget.statuses.get(str(code), 0) + 1
            raise
        else:
            code = str(response.status)
            budget.statuses[code] = budget.statuses.get(code, 0) + 1
            return Response(response, budget)
        finally:
            budget.http_seconds += budget.clock() - started

    def api(*args, **kwargs):
        try:
            return original_api(*args, **kwargs)
        except (module.RateStop, module.PublicationBudget) as exc:
            raise Interrupted(exc) from exc

    for name in ("REQUESTS", "NOT_MODIFIED", "CONDITIONAL_REQUESTS"):
        if hasattr(module, name):
            setattr(module, name, 0)
    if hasattr(module, "STATUS_COUNTS"):
        module.STATUS_COUNTS = {}
    module.RATE_LIMIT = module.RATE_REMAINING = module.RATE_RESET = None
    if hasattr(module, "RATE_START_REMAINING"):
        module.RATE_START_REMAINING = None
    module.PUBLICATION_REQUEST_LIMIT = None
    module.PUBLICATION_REQUESTS = 0
    module.PUBLICATION_ACTIVE = False
    module.urlopen, module.api = open_request, api
    module.RUN_AT, module.TODAY = now, now.date()
    module.NOW, module.NOW_ISO = now, stamp(now)
    module.FORCE_FULL_PROBE = True
    try:
        yield
    except Interrupted as exc:
        exc.rate = module.rate_snapshot()
        raise
    finally:
        for name in names:
            if name in before:
                setattr(module, name, before[name])
            elif hasattr(module, name):
                delattr(module, name)


def activity_unit(repo, records, rs, events, now):
    """One immutable commit page (or branch-list page), with no raw page cache."""
    identity = digest(
        [
            [
                (
                    p["id"],
                    p.get("github_branch"),
                    p.get("github_path"),
                    (p.get("github") or {}).get("tracking_branch"),
                    (p.get("github") or {}).get("default_branch"),
                )
                for p in records
            ],
            (rs.get("publication") or {}).get("fingerprint"),
        ]
    )
    cursor = rs.get("refresh_activity")
    if not cursor or cursor.get("identity") != identity:
        cursor = {
            "identity": identity,
            "started_at": stamp(now),
            "branch_page": 1,
            "listed": False,
            "branches": {},
            "queries": [],
            "reset_applied": False,
            "pushed_at": rs.get("last_seen_pushed_at"),
        }
        rs["refresh_activity"] = cursor
    explicit = {
        p.get("github_branch")
        or (p.get("github") or {}).get("tracking_branch")
        or (p.get("github") or {}).get("default_branch")
        or rs.get("default_branch")
        or "main"
        for p in records
    }
    required = pending_publication(rs)
    if required and not (rs.get("publication") or {}).get("metadata_complete"):
        return records, rs, events, False
    backfill = required or rs.get("scan_reason") in {"new", "new-project", "backfill"}
    if not cursor["listed"]:
        page = (
            activity.api(
                f"/repos/{repo}/branches?per_page=100&page={cursor['branch_page']}", allow_empty_repo=True
            )
            or []
        )
        cursor["branches"].update(
            {b["name"]: (b.get("commit") or {}).get("sha") for b in page if b.get("name")}
        )
        cursor["branch_page"] += 1
        if len(page) < 100 or not backfill:
            cursor["listed"] = True
            cursor["complete_list"] = len(page) < 100
        bounded(encode(cursor), "repository activity cursor")
        return records, rs, events, False
    missing = sorted(explicit - set(cursor["branches"])) if not cursor.get("empty") else []
    if missing:
        branch = missing[0]
        item = activity.api(f"/repos/{repo}/branches/{quote(branch, safe='')}", allow_404=True)
        if not item:
            if cursor["branches"]:
                raise ValueError(f"Tracked branch {branch} is unavailable in {repo}")
            # A genuinely empty repository has no tracked branch yet.
            cursor["empty"] = True
        else:
            cursor["branches"][branch] = (item.get("commit") or {}).get("sha")
            return records, rs, events, False
    if not cursor.get("queries_started"):
        cutoff = now - timedelta(days=180)
        for branch, tip in sorted(cursor["branches"].items()):
            matching = [p for p in records if activity.project_matches_branch(p, branch)]
            if not matching:
                continue
            if not isinstance(tip, str) or len(tip) != 40:
                raise ValueError("Invalid branch tip in activity snapshot")
            bs = rs.setdefault("branches", {}).get(branch, {})
            if not backfill and tip == bs.get("tip_sha"):
                continue
            since = (
                cutoff
                if backfill
                else max(
                    cutoff,
                    (
                        activity.parse_time(bs.get("last_scan_at"))
                        or activity.parse_time(rs.get("last_deep_scan"))
                        or cutoff
                    )
                    - timedelta(days=1),
                )
            )
            for path in sorted({p.get("github_path") or "" for p in matching}):
                cursor["queries"].append(
                    {"branch": branch, "tip": tip, "path": path, "since": stamp(since), "page": 1}
                )
        cursor["queries_started"] = True
    if cursor["queries"]:
        query = cursor["queries"][0]
        params = {"sha": query["tip"], "since": query["since"], "per_page": 100, "page": query["page"]}
        if query["path"]:
            params["path"] = query["path"]
        chunk = activity.api(f"/repos/{repo}/commits?{urlencode(params)}", allow_empty_repo=True) or []
        if not isinstance(chunk, list):
            raise ValueError("Invalid commits page")
        if not cursor["reset_applied"]:
            reset = set((rs.get("publication") or {}).get("reset_project_ids") or [])
            events = [
                e
                for e in events
                if not (e.get("project_id") in reset and e.get("type") in {"commit", "daily_commits"})
            ]
            cursor["reset_applied"] = True
        known = {
            (e.get("project_id"), e.get("repository"), e.get("sha")): e
            for e in events
            if e.get("type") == "commit"
        }
        other = [e for e in events if e.get("type") != "commit"]
        newest = {}
        first_page = query["page"] == 1
        for project in records:
            if (
                not activity.project_matches_branch(project, query["branch"])
                or (project.get("github_path") or "") != query["path"]
            ):
                continue
            for item in chunk:
                activity.add_event(known, project, repo, item, query["branch"], newest)
            observed = [e for e in known.values() if e.get("project_id") == project["id"]]
            activity.detect_ai(
                project,
                [{"sha": e.get("sha"), "commit": {"message": e.get("message", "")}} for e in observed],
            )
            if (
                first_page
                and project["id"] in newest
                and (activity.commit_date(newest[project["id"]]) or "")[:10]
                >= ((project.get("github") or {}).get("latest_commit") or {}).get("date", "")
            ):
                activity.update_project_latest(project, newest[project["id"]])
        events = compact_history(list(known.values()) + other, now)
        if len(chunk) < 100:
            cursor["queries"].pop(0)
        else:
            query["page"] += 1
    complete = not cursor["queries"]
    if complete:
        if cursor.get("complete_list"):
            rs["branches"] = {b: v for b, v in rs.get("branches", {}).items() if b in cursor["branches"]}
        for branch, tip in cursor["branches"].items():
            rs.setdefault("branches", {}).setdefault(branch, {}).update(
                tip_sha=tip, last_scan_at=cursor["started_at"]
            )
        rs["last_deep_scan"] = cursor["started_at"]
        rs["last_deep_scan_project_ids"] = sorted(p["id"] for p in records)
        changed = rs.get("last_seen_pushed_at") != cursor.get("pushed_at")
        rs["scan_requested"] = changed
        if changed:
            rs["scan_reason"] = "changed"
        else:
            rs.pop("scan_reason", None)
        if rs.get("publication"):
            rs["publication"]["history_complete"] = not changed
        rs.pop("refresh_activity", None)
        rs.pop("last_error", None)
        if changed and required:
            complete = False
        activity.advance_probe_deadlines({repo: records}, {"repositories": {repo: rs}}, now)
        freeze_addition_context(events, records, {repo: rs}, now)
    bounded(encode(rs.get("refresh_activity", {})), "repository activity cursor")
    return records, rs, events, complete


def perform(repo, work, records, rs, events, budget, now, opener=None, rate=None):
    records, rs, events = copy.deepcopy(records), copy.deepcopy(rs), copy.deepcopy(events)
    module = probe if work == "probe" else activity
    poll = {"version": 1, "repositories": {repo: rs}, "rate": {"probe": rate or {}}}
    if (
        rate
        and rate.get("reset_at")
        and datetime.fromisoformat(rate["reset_at"].replace("Z", "+00:00")) <= now
    ):
        poll["rate"]["probe"] = {}
    with transport(module, budget, now, opener), redirect_stdout(StringIO()):
        if work == "probe":
            records, poll = probe.main(records=records, state=poll, scope={"mode": "adaptive"}, persist=False)
            rs = poll["repositories"][repo]
            complete = bool(rs.get("last_probe_at") == stamp(now) and not rs.get("last_error"))
            if pending_publication(rs) and not rs["publication"].get("metadata_complete"):
                complete = False
        else:
            activity.load_rate_from_state(poll)
            records, rs, events, complete = activity_unit(repo, records, rs, events, now)
        rate = module.rate_snapshot()
    return records, rs, events, complete, rate


def collect(
    root,
    bundle_path,
    budget,
    *,
    limit=500,
    full=False,
    request_id="manual",
    continuation="",
    now=None,
    opener=None,
):
    root, bundle_path = Path(root), Path(bundle_path)
    if bundle_path.exists() or root.resolve() in bundle_path.resolve().parents:
        raise ValueError("Use a new bundle outside the checkout")
    now = now or datetime.now(timezone.utc)
    before_progress = progress_read(root)
    if continuation and continuation != token(before_progress):
        result = {"version": 1, "id": digest([request_id, continuation]), "stale": True, "results": []}
        bundle_path.write_bytes(encode(result))
        return result
    before_pending = read(root / "data/pending-projects.json", [])
    with tempfile.TemporaryDirectory(prefix="refresh-collect-") as directory:
        stage = Path(directory)
        shutil.copytree(root / "data", stage / "data")
        with redirect_stdout(StringIO()):
            merge_pending(stage)
        records = load_projects(stage / "data/projects.json")
    original = copy.deepcopy(groups(records))
    poll = read(root / POLL, {"version": 1, "repositories": {}})
    before_poll = copy.deepcopy(poll)
    catalogue = read(root / "state/project-catalog-state.json", {"projects": {}})
    publication = catalogue_delta(list(catalogue.get("projects", {}).values()), records)
    working = groups(records)
    prepare_publication(working, poll, publication, records)
    progress = plan(before_progress, records, poll, now, request_id, full)
    activity_payload = read(root / "data/activity.json", {"events": [], "window_days": 180})
    original_events = event_groups(activity_payload, records)
    events = copy.deepcopy(original_events)
    touched, outcomes, rate = set(), {}, (poll.get("rate") or {}).get("probe", {})
    units = {"probe": 0, "activity": 0}
    completed = {"probe": 0, "activity": 0}
    cycle = progress.get("cycle")
    for work in ("probe", "activity"):
        if progress.get("blocked_until"):
            break
        remaining = budget.limit - budget.requests
        deadline = budget.deadline
        if work == "probe" and cycle and cycle["pending"]["activity"]:
            remaining //= 2
            deadline = budget.clock() + max(0, deadline - budget.clock()) / 2
        budget.begin_lane(work, remaining, deadline, remaining)
        # Activity repeats fair rounds so a small publication can finish multiple
        # pages in one slice while large repositories retain durable page cursors.
        while True:
            advanced = False
            for repo in candidates(progress, poll, work, now, limit):
                if repo not in touched and len(touched) >= limit:
                    continue
                if (
                    work == "activity"
                    and pending_publication(poll["repositories"].get(repo, {}))
                    and not poll["repositories"][repo]["publication"].get("metadata_complete")
                ):
                    continue
                try:
                    budget.check(1)
                    budget.begin_record()
                    touched.add(repo)
                    rows, rs, evs, done, rate = perform(
                        repo,
                        work,
                        working[repo],
                        poll["repositories"].get(repo, {}),
                        events.get(repo, []),
                        budget,
                        now,
                        opener,
                        rate,
                    )
                except BudgetStop:
                    break
                except Interrupted as exc:
                    cause = exc.cause
                    rate = getattr(exc, "rate", rate)
                    if isinstance(cause, BudgetStop):
                        break
                    if isinstance(
                        cause,
                        (probe.PrimaryReserve, activity.PrimaryReserve, probe.RateStop, activity.RateStop),
                    ):
                        reset = activity.parse_time(rate.get("reset_at")) if rate else None
                        progress["blocked_until"] = stamp(
                            max(now + timedelta(minutes=2), reset or now + timedelta(minutes=15))
                        )
                        log(repo=repo, work=work, status="quota-stop", reason=str(cause))
                        break
                    retry = progress["retry"][work].get(repo, {})
                    failures = min(5, retry.get("failures", 0) + 1)
                    progress["retry"][work][repo] = {
                        "failures": failures,
                        "attempt_at": stamp(now),
                        "retry_at": stamp(now + timedelta(seconds=60 * 2**failures)),
                    }
                    touched.add(repo)
                    outcomes.setdefault(repo, {})[work] = "retry"
                    log(repo=repo, work=work, status="retry", reason=str(cause))
                    continue
                except Exception as exc:
                    retry = progress["retry"][work].get(repo, {})
                    failures = min(5, retry.get("failures", 0) + 1)
                    progress["retry"][work][repo] = {
                        "failures": failures,
                        "attempt_at": stamp(now),
                        "retry_at": stamp(now + timedelta(seconds=60 * 2**failures)),
                    }
                    touched.add(repo)
                    outcomes.setdefault(repo, {})[work] = "retry"
                    log(repo=repo, work=work, status="retry", reason=str(exc))
                    continue
                finally:
                    budget.end_record()
                touched.add(repo)
                if not done and work == "probe":
                    retry = progress["retry"][work].get(repo, {})
                    failures = min(5, retry.get("failures", 0) + 1)
                    progress["retry"][work][repo] = {
                        "failures": failures,
                        "attempt_at": stamp(now),
                        "retry_at": stamp(now + timedelta(seconds=60 * 2**failures)),
                    }
                    outcomes.setdefault(repo, {})[work] = "retry"
                    continue
                before = digest([working[repo], poll["repositories"].get(repo, {}), events.get(repo, [])])
                after = digest([rows, rs, evs])
                if not done and before == after:
                    continue
                working[repo], poll["repositories"][repo], events[repo] = rows, rs, evs
                units[work] += 1
                advanced = True
                if done:
                    progress["retry"][work].pop(repo, None)
                else:
                    progress["retry"][work][repo] = {"failures": 0, "attempt_at": stamp(now)}
                if done:
                    cycle["pending"][work].remove(repo)
                    completed[work] += 1
                outcomes.setdefault(repo, {})[work] = "complete" if done else "partial"
                if work == "probe" and rs.get("scan_requested") and repo not in cycle["pending"]["activity"]:
                    for field in ("targets", "pending"):
                        if repo not in cycle[field]["activity"]:
                            cycle[field]["activity"].append(repo)
                log(
                    repo=repo,
                    work=work,
                    status="complete" if done else "partial",
                    requests=budget.requests,
                    completed=completed,
                    units=units,
                )
            else:
                if work == "activity" and advanced:
                    continue
            break
        budget.end_lane()
        if progress.get("blocked_until"):
            break
    result_rows = []
    for repo in sorted(working):
        before_rs = before_poll["repositories"].get(repo, {})
        rs = poll["repositories"].get(repo, {})
        if repo not in outcomes and rs == before_rs and working[repo] == original[repo]:
            continue
        result_rows.append(
            {
                "repo": repo,
                "source": source(original[repo]),
                "before": {p["id"]: owned(p) for p in original[repo]},
                "after": {p["id"]: owned(p) for p in working[repo]},
                "state_before": before_rs,
                "state_after": rs,
                "events_before": original_events.get(repo, []),
                "events_after": events.get(repo, []),
                "outcomes": outcomes.get(repo, {}),
            }
        )
    bundle = {
        "version": 1,
        "id": digest([request_id, token(before_progress), stamp(now)]),
        "created_at": stamp(now),
        "progress_before": before_progress,
        "progress_after": progress,
        "pending_before": before_pending,
        "results": result_rows,
        "rate": rate,
        "summary": {"repositories": len(touched), "completed": completed, "units": units, **budget.summary()},
    }
    bundle_path.parent.mkdir(parents=True, exist_ok=True)
    bundle_path.write_bytes(encode(bundle))
    log(collection=bundle["summary"], sweep=status(progress, now, poll))
    return bundle


def add_publication_work(progress, records, poll):
    cycle = progress.get("cycle")
    if not cycle:
        return
    current = groups(records)
    for work in ("probe", "activity"):
        for field in ("targets", "pending"):
            cycle[field][work] = [r for r in cycle[field][work] if r in current]
    for repo in sorted(current):
        rs = poll["repositories"].get(repo, {})
        if not pending_publication(rs):
            continue
        for work, field in (("probe", "metadata_complete"), ("activity", "history_complete")):
            if not rs["publication"].get(field):
                for queue in ("targets", "pending"):
                    if repo not in cycle[queue][work]:
                        cycle[queue][work].append(repo)


def event_groups(payload, records):
    memberships = {p["id"]: repository(p) for p in records}
    out = {}
    for event in payload["events"]:
        repo = memberships.get(event.get("project_id"))
        out.setdefault(repo, []).append(event)
    return out


def status(progress, now=None, poll=None):
    now = now or datetime.now(timezone.utc)
    cycle = progress.get("cycle")
    result = {
        "active": active(progress),
        "token": token(progress),
        "cycle": cycle.get("id") if cycle else None,
        "mode": cycle.get("mode") if cycle else None,
        "completed": {},
        "remaining": {},
    }
    if cycle:
        for work in ("probe", "activity"):
            result["remaining"][work] = len(cycle["pending"][work])
            result["completed"][work] = len(cycle["targets"][work]) - len(cycle["pending"][work])
    blocked = progress.get("blocked_until")
    blocked = bool(blocked and datetime.fromisoformat(blocked.replace("Z", "+00:00")) > now)
    result["eligible"] = bool(
        active(progress)
        and not blocked
        and any(
            ready(progress, repo, work, now)
            and not (
                work == "activity"
                and poll is not None
                and pending_publication(poll.get("repositories", {}).get(repo, {}))
                and not poll["repositories"][repo]["publication"].get("metadata_complete")
            )
            for work in ("probe", "activity")
            for repo in cycle["pending"][work]
        )
    )
    return result


def apply_bundle(root, bundle, now=None):
    """Replay completed units only; a Git commit publishes all files atomically."""
    root = Path(root)
    now = now or datetime.now(timezone.utc)
    before_progress = progress_read(root)
    if bundle.get("version") != 1:
        raise ValueError("Invalid refresh bundle")
    poll_status = read(root / POLL, {"repositories": {}})
    if bundle.get("stale"):
        return {
            "published": False,
            "stale": True,
            "continue": False,
            **status(before_progress, now, poll_status),
        }
    if before_progress.get("last_batch") == bundle["id"]:
        current = status(before_progress, now, poll_status)
        # The push may have succeeded before its response was lost. Repair the
        # handoff using the published token; duplicate handoffs are harmless.
        return {"published": False, "duplicate": True, "continue": current["eligible"], **current}
    if before_progress != bundle["progress_before"]:
        return {"published": False, "stale": True, "continue": False, **status(before_progress, now)}
    with tempfile.TemporaryDirectory(prefix="refresh-apply-") as directory:
        stage = Path(directory)
        shutil.copytree(root / "data", stage / "data")
        shutil.copytree(root / "state", stage / "state")
        pending = read(root / "data/pending-projects.json", [])
        if pending == bundle["pending_before"]:
            with redirect_stdout(StringIO()):
                merge_pending(stage)
        records = load_projects(stage / "data/projects.json")
        by_repo = groups(records)
        poll = read(stage / POLL, {"version": 1, "repositories": {}})
        guard_poll = copy.deepcopy(poll)
        guard_records = copy.deepcopy(by_repo)
        payload = read(stage / "data/activity.json", {"window_days": 180, "events": []})
        events = event_groups(payload, records)
        catalogue = read(stage / "state/project-catalog-state.json", {"projects": {}})
        publication = catalogue_delta(list(catalogue.get("projects", {}).values()), records)
        prepare_publication(by_repo, poll, publication, records)
        progress = copy.deepcopy(bundle["progress_after"])
        accepted, conflicts = [], []
        for row in bundle["results"]:
            repo = row["repo"]
            originals = guard_records.get(repo, [])
            safe = (
                source(originals) == row["source"]
                and {p["id"]: owned(p) for p in originals} == row["before"]
                and guard_poll["repositories"].get(repo, {}) == row["state_before"]
                and events.get(repo, []) == row["events_before"]
                and set(row["after"]) == {p["id"] for p in originals}
                and all(set(fields) == set(OWNED) for fields in row["after"].values())
            )
            if not safe:
                conflicts.append(repo)
                for work in ("probe", "activity"):
                    if (
                        row["outcomes"].get(work) == "complete"
                        and repo in progress["cycle"]["targets"][work]
                        and repo not in progress["cycle"]["pending"][work]
                    ):
                        progress["cycle"]["pending"][work].append(repo)
                    if repo in before_progress["retry"][work]:
                        progress["retry"][work][repo] = copy.deepcopy(before_progress["retry"][work][repo])
                    else:
                        progress["retry"][work].pop(repo, None)
                continue
            for project in by_repo[repo]:
                for key, value in row["after"][project["id"]].items():
                    if value["exists"]:
                        project[key] = copy.deepcopy(value["value"])
                    else:
                        project.pop(key, None)
            poll["repositories"][repo] = copy.deepcopy(row["state_after"])
            events[repo] = copy.deepcopy(row["events_after"])
            accepted.append(repo)
        add_publication_work(progress, records, poll)
        live = set(by_repo)
        poll["repositories"] = {r: v for r, v in poll["repositories"].items() if r in live}
        for work in ("probe", "activity"):
            progress["retry"][work] = {r: v for r, v in progress["retry"][work].items() if r in live}
        old_rate = (poll.get("rate") or {}).get("probe") or {}
        if bundle.get("rate") and (bundle["rate"].get("checked_at") or "") >= (
            old_rate.get("checked_at") or ""
        ):
            poll.setdefault("rate", {})["probe"] = bundle["rate"]
        cutoff = now - timedelta(days=180)
        current_projects = {p["id"]: p for p in records}
        joined = [
            e
            for rows in events.values()
            for e in rows
            if (
                e.get("type") not in {"commit", "daily_commits"}
                or (
                    e.get("project_id") in current_projects
                    and e.get("repository") == repository(current_projects[e["project_id"]])
                    and (
                        e.get("type") != "commit"
                        or not e.get("branches")
                        or any(
                            activity.project_matches_branch(current_projects[e["project_id"]], b)
                            for b in e["branches"]
                        )
                    )
                )
            )
            and (activity.parse_time(e.get("date")) or now) >= cutoff
        ]
        payload["events"] = compact_history(joined, now)
        freeze_addition_context(payload["events"], records, poll["repositories"], now)
        payload["generated_at"] = stamp(now)
        write_projects(stage / "data/projects.json", records)
        write_activity(stage / "data/activity.json", payload)
        (stage / POLL).write_bytes(encode(poll))
        with redirect_stdout(StringIO()):
            record_catalogue(stage)
        validate(stage / "data/projects.json", stage / "data/activity.json")
        # A zero-work retry must not manufacture continuation progress.
        made_progress = (
            progress != before_progress
            or bool(accepted)
            or pending != read(stage / "data/pending-projects.json", [])
        )
        if not made_progress:
            return {
                "published": False,
                "continue": False,
                "conflicts": conflicts,
                **status(before_progress, now),
            }
        progress["revision"] = before_progress["revision"] + 1
        progress["last_batch"] = bundle["id"]
        (stage / PROGRESS).write_bytes(bounded(encode(progress), PROGRESS))
        # All validation precedes checkout writes; the workflow commits once.
        before_paths = set(storage_paths(root / "data"))
        after_paths = set(storage_paths(stage / "data"))
        names = ["data/" + p for p in sorted(after_paths)]
        names += [
            "data/activity.json",
            "data/pending-projects.json",
            POLL,
            PROGRESS,
            "state/project-catalog-state.json",
        ]
        for name in names:
            src, dst = stage / name, root / name
            if src.exists() and (not dst.exists() or src.read_bytes() != dst.read_bytes()):
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
        for obsolete in before_paths - after_paths:
            (root / "data" / obsolete).unlink(missing_ok=True)
        result = {
            "published": True,
            "accepted": len(accepted),
            "conflicts": conflicts,
            "continue": status(progress, now, poll)["eligible"],
            **status(progress, now, poll),
        }
        log(publication=result)
        return result


def outputs(result):
    if filename := os.environ.get("GITHUB_OUTPUT"):
        with open(filename, "a", encoding="utf-8") as handle:
            handle.write("continue=" + str(bool(result.get("continue"))).lower() + "\n")
            handle.write("continuation=" + result.get("token", "") + "\n")
    if filename := os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(filename, "a", encoding="utf-8") as handle:
            handle.write(
                "### Repository refresh progress\n\n```json\n" + json.dumps(result, indent=2) + "\n```\n"
            )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("collect", "apply", "status"))
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--bundle", type=Path)
    parser.add_argument("--seconds", type=int, default=600)
    parser.add_argument("--requests", type=int, default=1000)
    parser.add_argument("--repositories", type=int, default=500)
    parser.add_argument("--full", action="store_true")
    parser.add_argument("--request-id", default=os.environ.get("GITHUB_RUN_ID", "manual"))
    parser.add_argument("--continuation", default="")
    args = parser.parse_args()
    if args.command == "status":
        result = status(progress_read(args.root), poll=read(args.root / POLL, {"repositories": {}}))
        outputs(result)
        log(progress=result)
        return
    if args.bundle is None or args.root.resolve() in args.bundle.resolve().parents:
        parser.error("Use a bundle outside the checkout")
    if args.command == "collect":
        if (
            not 1 <= args.seconds <= 900
            or not 0 <= args.requests <= 2000
            or not 1 <= args.repositories <= 500
        ):
            parser.error("Budgets: seconds 1..900; requests 0..2000; repositories 1..500")
        collect(
            args.root,
            args.bundle,
            Budget(args.seconds, args.requests, api_requests=args.requests),
            limit=args.repositories,
            full=args.full,
            request_id=args.request_id,
            continuation=args.continuation,
        )
    else:
        result = apply_bundle(args.root, json.loads(args.bundle.read_bytes()))
        outputs(result)


if __name__ == "__main__":
    main()
