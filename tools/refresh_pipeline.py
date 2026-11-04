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
import re
from pathlib import Path
import shutil
import tempfile
from urllib.parse import quote, urlencode, urlsplit
from urllib.error import HTTPError

import collect_activity as activity
import refresh_github as probe
import refresh_gitlab as gitlab
from repository_provider import provider, metadata, matches_branch, selectors
from activity_history import RETENTION_DAYS, compact_history, freeze_addition_context, write_activity
from catalogue_storage import bounded, encode, load_projects, write_projects, storage_paths
from collection_budget import Budget, BudgetStop, RecordStop
from merge_pending_projects import main as merge_pending
from record_project_activity import main as record_catalogue, snapshot
from refresh_scope import (catalogue_delta, pending_publication, prepare_publication, repository,
                           publication_fingerprint, retained_metadata)
from research_submission import REFRESH_REQUEST, refresh_repositories
from validate_site_data import validate

PROGRESS = "state/refresh-progress.json"
POLL = "state/github-poll-state.json"
OWNED = ("github", "gitlab", "last_activity", "last_checked", "ai")
RESEARCH_REQUEST_HISTORY = 128
WORKS = ("probe", "activity", "releases")
HOURLY_LIMITS = {"github": int(os.environ.get("GITHUB_REFRESH_HOURLY_REQUESTS", "3000")),
                 "gitlab": int(os.environ.get("GITLAB_REFRESH_HOURLY_REQUESTS", "120"))}


def log(**value):
    print(json.dumps(value, separators=(",", ":"), ensure_ascii=False), flush=True)


def stamp(now):
    return now.astimezone(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def digest(value):
    return hashlib.sha256(encode(value)).hexdigest()


def read(path, default):
    return json.loads(path.read_bytes()) if path.exists() else copy.deepcopy(default)


class ProviderStop(Exception):
    def __init__(self, retry_at):
        super().__init__("provider hourly request budget")
        self.retry_at = retry_at


def provider_request(progress, kind, url, now, budget):
    """Count actual attempts across published continuations, never cached units.

    Retain each minute bucket until an hour after its END. This conservative
    sliding window prevents a fixed-hour boundary burst without per-request logs.
    """
    observed = now + timedelta(seconds=max(0, budget.clock() - budget.start))
    minute = int(observed.timestamp()) // 60
    usage = progress.setdefault("provider_usage", {}).setdefault(kind, {})
    buckets = usage.setdefault("minutes", {})
    for key in list(buckets):
        if int(key) < minute - 60:
            buckets.pop(key)
    limit = HOURLY_LIMITS[kind]
    if limit < 1:
        raise ValueError("Provider hourly request budget must be positive")
    if sum(sum(row.values()) for row in buckets.values()) >= limit:
        earliest = min(map(int, buckets))
        raise ProviderStop(datetime.fromtimestamp((earliest + 61) * 60, timezone.utc))
    path = urlsplit(url).path
    if kind == "github":
        path = re.sub(r"^/repos/[^/]+/[^/]+", "/repos/:repo", path)
        endpoint = path.split("/repos/:repo/", 1)[-1].split("/", 1)[0] if path != "/repos/:repo" else "repository"
    else:
        suffix = path.split("/projects/", 1)[-1].split("/", 1)
        endpoint = suffix[1].split("/", 2) if len(suffix) > 1 else []
        endpoint = "/".join(endpoint[:2]) or "project"
    row = buckets.setdefault(str(minute), {})
    row[endpoint] = row.get(endpoint, 0) + 1
    usage["limit"] = limit
    usage["checked_at"] = stamp(observed)
    if sum(sum(row.values()) for row in buckets.values()) >= limit:
        until = stamp(datetime.fromtimestamp((min(map(int, buckets)) + 61) * 60, timezone.utc))
        blocked = progress.setdefault("provider_blocked_until", {})
        blocked[kind] = max(blocked.get(kind, ""), until)
    bounded(encode(progress["provider_usage"]), "provider request usage")


def migrate_progress(value):
    value = copy.deepcopy(value)
    value.setdefault("retry", {}).setdefault("releases", {})
    if value.get("cycle"):
        for field in ("targets", "pending", "deferred"):
            value["cycle"].setdefault(field, {}).setdefault("releases", [])
    return value


def source_matches(records, expected):
    if source(records) == expected:
        return True
    # Replay pre-GitLab bundles only when new selector/owned fields are absent.
    # Their source hash omitted two newly introduced material null fields.
    if any(provider(p) != "github" or p.get("gitlab") or p.get("gitlab_branch") or p.get("gitlab_path") for p in records):
        return False
    legacy = []
    for project in records:
        row = snapshot(project)
        row.pop("gitlab_branch", None)
        row.pop("gitlab_path", None)
        legacy.append(row)
    return digest(sorted(legacy, key=lambda p: p["id"])) == expected


def progress_read(root):
    value = read(
        Path(root) / PROGRESS,
        {"version": 1, "revision": 0, "cycle": None, "retry": {"probe": {}, "activity": {}}},
    )
    if value.get("version") != 1 or type(value.get("revision")) is not int or value["revision"] < 0:
        raise ValueError("Invalid refresh progress")
    value.setdefault("retry", {}).setdefault("releases", {})
    for work in WORKS:
        if not isinstance(value.get("retry", {}).get(work), dict):
            raise ValueError("Invalid refresh retry queue")
    requests = value.get("research_requests", [])
    if (not isinstance(requests, list) or len(requests) > RESEARCH_REQUEST_HISTORY
            or any(not isinstance(r, str) or not REFRESH_REQUEST.fullmatch(r) for r in requests)
            or len(set(requests)) != len(requests)):
        raise ValueError("Invalid research refresh request history")
    cycle = value.get("cycle")
    if cycle:
        if not isinstance(cycle.get("id"), str):
            raise ValueError("Invalid refresh cycle")
        cycle.setdefault("deferred", {"probe": [], "activity": []})
        for field in ("targets", "pending", "deferred"):
            cycle.setdefault(field, {}).setdefault("releases", [])
        for work in WORKS:
            for field in ("targets", "pending", "deferred"):
                rows = cycle.get(field, {}).get(work)
                if (
                    not isinstance(rows, list)
                    or any(not isinstance(r, str) for r in rows)
                    or len(set(rows)) != len(rows)
                ):
                    raise ValueError("Invalid refresh cycle queue")
            if set(cycle["pending"][work]) & set(cycle["deferred"][work]) or not (
                set(cycle["pending"][work]) | set(cycle["deferred"][work])
            ) <= set(cycle["targets"][work]):
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
    if provider(repo) == "gitlab":
        last = activity.parse_time(rs.get("last_probe_at"))
        return last is None or now - last >= timedelta(hours=24)
    latest = max((p.get("last_activity") or "" for p in record_group), default="")
    archived = any((p.get("github") or {}).get("archived") for p in record_group)
    old, old_today = probe.RUN_AT, probe.TODAY
    try:
        probe.RUN_AT, probe.TODAY = now, now.date()
        interval = probe.probe_interval_minutes(latest or None, archived)
        return probe.probe_due(repo, rs, interval)
    finally:
        probe.RUN_AT, probe.TODAY = old, old_today


def history_ready(repo, rs):
    return not ((provider(repo) == "gitlab" and not rs.get("last_probe_at")) or
                (pending_publication(rs) and not rs["publication"].get("metadata_complete")))


def activity_due(repo, rs, now):
    if rs.get("scan_requested") or rs.get("refresh_activity"):
        return True
    last = activity.parse_time(rs.get("last_deep_scan"))
    return provider(repo) == "gitlab" and (last is None or now - last >= timedelta(hours=1))


def plan(progress, records, poll, now, request_id, full=False, research_repositories=None):
    progress = copy.deepcopy(progress)
    progress.setdefault("retry", {}).setdefault("releases", {})
    if progress.get("cycle"):
        for field in ("targets", "pending", "deferred"):
            progress["cycle"].setdefault(field, {}).setdefault("releases", [])
    # Long unavailable-source retries must not pin the active cycle and prevent
    # later healthy repositories from entering a new sweep.
    if cycle := progress.get("cycle"):
        for work in WORKS:
            for repo in list(cycle["pending"][work]):
                if not ready(progress, repo, work, now):
                    preserve_blocked_work(progress, repo, work, now)
                    cycle["pending"][work].remove(repo)
                    cycle["deferred"][work].append(repo)
    research = research_repositories is not None
    if research and full:
        raise ValueError("A research refresh cannot request a full sweep")
    seen_research = research and request_id in progress.get("research_requests", [])
    if (
        progress.get("blocked_until")
        and datetime.fromisoformat(progress["blocked_until"].replace("Z", "+00:00")) <= now
    ):
        progress.pop("blocked_until")
    by_repo = groups(records)
    repos = set(by_repo)
    selected = repos & set(research_repositories) if research else repos
    if full or (research and not seen_research):
        for repo in selected:
            for work in WORKS:
                if work == "releases" and provider(repo) != "gitlab":
                    continue
                if research and work == "activity" and not poll["repositories"].get(repo, {}).get("scan_requested"):
                    continue
                if not ready(progress, repo, work, now):
                    preserve_blocked_work(progress, repo, work, now)
    if not active(progress) and not seen_research and not (full and progress.get("last_full_request") == request_id):
        probes = sorted(
            repo
            for repo, rows in by_repo.items()
            if repo in selected and ready(progress, repo, "probe", now) and (
                research or full
                or repo in progress["retry"]["probe"]
                or poll["repositories"].get(repo, {}).get("availability_recheck_requested")
                or due(repo, rows, poll["repositories"].get(repo, {}), now)
            )
        )
        scans = sorted(
            repo
            for repo in selected
            if ready(progress, repo, "activity", now) and (full
            or repo in progress["retry"]["activity"]
            or activity_due(repo, poll["repositories"].get(repo, {}), now))
        )
        releases = sorted(repo for repo in selected if provider(repo) == "gitlab"
                          and ready(progress, repo, "releases", now)
                          and (full or research or repo in progress["retry"]["releases"]
                               or not poll["repositories"].get(repo, {}).get("last_release_check_at")
                               or now - activity.parse_time(poll["repositories"][repo]["last_release_check_at"]) >= timedelta(hours=1)))
        progress["cycle"] = {
            "id": digest([request_id, progress["revision"], stamp(now)])[:24],
            "mode": "research" if research else "full" if full else "adaptive",
            "started_at": stamp(now),
            "targets": {"probe": probes[:], "activity": scans[:], "releases": releases[:]},
            "pending": {"probe": probes[:], "activity": scans[:], "releases": releases[:]},
            "deferred": {"probe": [], "activity": [], "releases": []},
        }
    if research and not seen_research:
        # Coalesce into the one durable cycle. Do not replace an active broad
        # sweep, replay its completed work, or discard activity page cursors.
        cycle = progress["cycle"]
        for work in WORKS:
            requested = selected if work == "probe" else {
                repo for repo in selected if repo in progress["retry"][work]
                or poll["repositories"].get(repo, {}).get("scan_requested")
            }
            if work == "releases":
                requested = {r for r in selected if provider(r) == "gitlab"}
            extra = sorted(r for r in requested - set(cycle["targets"][work]) if ready(progress, r, work, now))
            cycle["targets"][work].extend(extra)
            cycle["pending"][work].extend(extra)
        # Bounded replay suppression. Very late duplicates may recheck only
        # their receipt's repositories, never restart an all-due sweep.
        progress["research_requests"] = (
            progress.get("research_requests", []) + [request_id]
        )[-RESEARCH_REQUEST_HISTORY:]
    if full and active(progress) and progress["cycle"]["mode"] != "full":
        # A manual full request upgrades an adaptive cycle without losing its
        # completed units or page cursors. Newly included repositories stay due.
        cycle = progress["cycle"]
        cycle["mode"] = "full"
        for work in WORKS:
            extra = sorted(r for r in repos - set(cycle["targets"][work]) if ready(progress, r, work, now)
                           and (work != "releases" or provider(r) == "gitlab"))
            cycle["targets"][work].extend(extra)
            cycle["pending"][work].extend(extra)
    if full:
        progress["last_full_request"] = request_id
    cycle = progress.get("cycle")
    if cycle:
        for work in WORKS:
            cycle["pending"][work] = [r for r in cycle["pending"][work] if r in repos]
            cycle["targets"][work] = [r for r in cycle["targets"][work] if r in repos]
            cycle["deferred"][work] = [r for r in cycle["deferred"][work] if r in repos]
        # GitLab's hourly lanes must not wait for a large GitHub sweep to end.
        # Re-enqueue only the due provider's units; retain every other queue and
        # immutable cursor. Receipt-scoped research cycles stay receipt-scoped.
        gitlab_scope = selected if research else (repos if cycle["mode"] != "research" else
                       set(cycle["targets"]["probe"]) | set(cycle["targets"]["releases"]))
        for repo in sorted(r for r in gitlab_scope if provider(r) == "gitlab"):
            rs = poll["repositories"].get(repo, {})
            release_at = activity.parse_time(rs.get("last_release_check_at"))
            required = {
                "probe": due(repo, by_repo[repo], rs, now) or rs.get("availability_recheck_requested"),
                "activity": activity_due(repo, rs, now),
                "releases": release_at is None or now - release_at >= timedelta(hours=1),
            }
            for work in WORKS:
                if not (required[work] or repo in progress["retry"][work]) or not ready(progress, repo, work, now):
                    continue
                if repo in cycle["deferred"][work]:
                    cycle["deferred"][work].remove(repo)
                for field in ("targets", "pending"):
                    if repo not in cycle[field][work]:
                        cycle[field][work].append(repo)
        # New or changed catalogue work must survive a coalesced push run.
        for repo in sorted(repos):
            rs = poll["repositories"].get(repo, {})
            publication = rs.get("publication") or {}
            if pending_publication(rs):
                for work, complete in (("probe", "metadata_complete"), ("activity", "history_complete"), ("releases", "releases_complete")):
                    if work == "releases" and provider(repo) != "gitlab":
                        continue
                    if not publication.get(complete) and ready(progress, repo, work, now) and repo not in cycle["deferred"][work]:
                        for field in ("targets", "pending"):
                            if repo not in cycle[field][work]:
                                cycle[field][work].append(repo)
    for work in WORKS:
        progress["retry"][work] = {r: v for r, v in progress["retry"][work].items() if r in repos}
    return progress


def preserve_blocked_work(progress, repo, work, now):
    """A provider cooldown must not erase full/research work on cycle rollover."""
    retry = progress["retry"][work].setdefault(repo, {"failures": 0, "attempt_at": stamp(now)})
    blocked = (progress.get("provider_blocked_until") or {}).get(provider(repo), "")
    if provider(repo) == "github":
        blocked = max(blocked, progress.get("blocked_until") or "")
    if blocked:
        retry["retry_at"] = max(retry.get("retry_at", ""), blocked)


def ready(progress, repo, work, now):
    blocked = (progress.get("provider_blocked_until") or {}).get(provider(repo))
    if provider(repo) == "github":
        blocked = max(blocked or "", progress.get("blocked_until") or "")
    if blocked and activity.parse_time(blocked) > now:
        return False
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
            or rs.get({"probe": "last_probe_at", "activity": "last_deep_scan", "releases": "last_release_check_at"}[work])
            or ""
        )
        return provider(repo) != "gitlab", last, repo.casefold()

    priority = sorted((r for r in rows if pending_publication(poll["repositories"].get(r, {}))), key=key)
    ordinary = sorted(set(rows) - set(priority), key=key)
    share = max(1, cap // 4) if ordinary else len(priority)
    return priority[:share] + ordinary + priority[share:]


def defer(progress, poll, repo, work, now, outcomes, *, seconds=None, block_activity=False):
    retry = progress["retry"][work].get(repo, {})
    failures = min(5, retry.get("failures", 0) + 1)
    entry = {
        "failures": failures,
        "attempt_at": stamp(now),
        "retry_at": stamp(now + timedelta(seconds=seconds if seconds is not None else 60 * 2**failures)),
    }
    lanes = [work]
    rs = poll["repositories"].get(repo, {})
    if work == "probe" and ((pending_publication(rs) and not rs["publication"].get("metadata_complete"))
                            or block_activity):
        lanes.append("activity")
        if provider(repo) == "gitlab":
            lanes.append("releases")
    for lane in lanes:
        progress["retry"][lane][repo] = copy.deepcopy(entry)
        cycle = progress["cycle"]
        if repo in cycle["pending"][lane]:
            cycle["pending"][lane].remove(repo)
            cycle["deferred"][lane].append(repo)
        outcomes.setdefault(repo, {})[lane] = "retry"


def clear_unavailability(records, rs):
    rs.pop("repository_availability", None)
    rs.pop("availability_recheck_requested", None)
    work = rs.get("publication") or {}
    if work.get("outcome") == "source-unavailable":
        work.pop("outcome")
    for project in records:
        metadata(project).pop("source_availability", None)


def unavailable(progress, poll, working, repo, now, outcomes):
    """Record a verified root 404, never successful metadata/history/freshness."""
    rs, records = poll["repositories"].setdefault(repo, {}), working[repo]
    defer(progress, poll, repo, "probe", now, outcomes, seconds=24 * 60 * 60, block_activity=True)
    rs["repository_availability"] = {
        "repository": repo, "status": "unavailable", "http_status": 404,
        "observed_at": stamp(now), "retry_at": progress["retry"]["probe"][repo]["retry_at"], "retryable": True,
    }
    rs.pop("availability_recheck_requested", None)
    rs.pop("release_access_verification", None)
    rs["last_error"] = "Repository lookup returned HTTP 404; retained facts; retryable"
    work = rs.get("publication") or {}
    if (pending_publication(rs) and work.get("reset_project_ids") == []
            and work.get("fingerprint") == publication_fingerprint(records)
            and retained_metadata(repo, records, rs)):
        work["outcome"] = "source-unavailable"
    for project in records:
        kind = provider(repo)
        project.setdefault(kind, {"repository": repo})
        if project.get(kind):
            project[kind]["source_availability"] = {
                "status": "unavailable", "http_status": 404, "retryable": True,
                "checked_at": (metadata(project).get("source_availability") or {}).get("checked_at") or stamp(now),
            }
    log(repo=repo, work="probe", status="source-unavailable", retry_at=rs["repository_availability"]["retry_at"],
        publication_outcome=work.get("outcome", "pending"))


def release_unavailable(progress, poll, working, repo, now, outcomes):
    """A root-accessible project's disabled/forbidden releases remain unknown."""
    rs = poll["repositories"][repo]
    observed = (rs.pop("release_access_verification", {}) or {}).get("observed_at") or stamp(now)
    defer(progress, poll, repo, "releases", now, outcomes, seconds=24 * 60 * 60)
    rs["release_availability"] = {
        "repository": repo, "status": "unavailable", "http_status": 403, "retryable": True,
        "root_checked_at": rs["last_root_check_at"], "observed_at": observed,
        "retry_at": progress["retry"]["releases"][repo]["retry_at"],
        "fingerprint": publication_fingerprint(working[repo]),
    }
    if rs.get("publication"):
        rs["publication"]["releases_complete"] = False
        rs["publication"]["release_outcome"] = "capability-unavailable"
    for project in working[repo]:
        if not selectors(project)[1]:
            meta = project.setdefault("gitlab", {"repository": repo})
            meta["release_availability"] = {
                "status": "unavailable", "http_status": 403, "retryable": True,
                "checked_at": (meta.get("release_availability") or {}).get("checked_at") or observed,
            }
    log(repo=repo, work="releases", status="capability-unavailable", retry_at=rs["release_availability"]["retry_at"])


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
def transport(module, budget, now, opener=None, before_request=None):
    root_lookups = {}
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
            budget.check(1)
            if before_request:
                before_request(request.full_url)
            timeout = min(timeout, budget.before_request(api=True))
        except (BudgetStop, RecordStop, ProviderStop) as exc:
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
            result = original_api(*args, **kwargs)
        except (module.RateStop, module.PublicationBudget) as exc:
            raise Interrupted(exc) from exc
        except Exception as exc:
            cause = exc if isinstance(exc, HTTPError) else exc.__cause__
            if isinstance(cause, HTTPError) and args and re.fullmatch(r"/repos/[^/]+/[^/]+", args[0]):
                root_lookups[args[0]] = cause.code
            raise
        else:
            if args and re.fullmatch(r"/repos/[^/]+/[^/]+", args[0]):
                root_lookups[args[0]] = result[0]
            return result

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
        yield root_lookups
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
            RETENTION_DAYS,
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
            "window_days": RETENTION_DAYS,
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
        cutoff = now - timedelta(days=RETENTION_DAYS)
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
    if not cursor["reset_applied"]:
        # Reset changed tracking only while its publication is pending. The
        # completed marker remains in poll state and must not erase old history
        # during a later incremental scan. Empty repositories need this too.
        reset = set((rs.get("publication") or {}).get("reset_project_ids") or []) if required else set()
        events = [
            e
            for e in events
            if not (e.get("project_id") in reset and e.get("type") in {"commit", "daily_commits"})
        ]
        cursor["reset_applied"] = True
    if cursor["queries"]:
        query = cursor["queries"][0]
        params = {"sha": query["tip"], "since": query["since"], "per_page": 100, "page": query["page"]}
        if query["path"]:
            params["path"] = query["path"]
        chunk = activity.api(f"/repos/{repo}/commits?{urlencode(params)}", allow_empty_repo=True) or []
        if not isinstance(chunk, list):
            raise ValueError("Invalid commits page")
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
            # Fresh API objects retain linked bot identity and co-author trailers;
            # canonical lean events deliberately omit full messages.
            activity.detect_ai(project, chunk)
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


def perform(repo, work, records, rs, events, budget, now, opener=None, rate=None, before_request=None):
    records, rs, events = copy.deepcopy(records), copy.deepcopy(rs), copy.deepcopy(events)
    if provider(repo) == "gitlab":
        pending_release = rs.get("release_access_verification") or {}
        observed = activity.parse_time(pending_release.get("observed_at"))
        verified = activity.parse_time(rs.get("last_root_check_at"))
        if (work == "releases" and pending_release.get("http_status") == 403
                and pending_release.get("fingerprint") == publication_fingerprint(records)
                and observed and verified and observed <= verified <= now
                and now - observed <= timedelta(hours=1) and not rs.get("repository_availability")):
            rs["_release_lookup_status"] = 403
            return records, rs, events, False, rate or {}
        verifying = rs.get("availability_recheck_requested")
        client = gitlab.Client(repo, budget, now, opener, before_request)
        try:
            function = {"probe": gitlab.probe_unit, "activity": gitlab.activity_unit,
                        "releases": gitlab.release_unit}[work]
            records, rs, events, complete = function(repo, records, rs, events, now, client)
        except HTTPError as exc:
            if work == "releases" and exc.code == 403:
                rs["release_access_verification"] = {
                    "http_status": 403, "observed_at": stamp(now),
                    "fingerprint": publication_fingerprint(records),
                }
                # Only a non-quota 403 (Client handles quota signals separately)
                # can represent an unavailable release capability. Verify the
                # root now; never turn an inaccessible/private project into a waiver.
                try:
                    if rs.get("last_root_check_at") != stamp(now):
                        records, rs, events, _ = gitlab.probe_unit(repo, records, rs, events, now, client)
                except (BudgetStop, RecordStop, gitlab.RateStop, ProviderStop) as limited:
                    # Preserve the observed403 if a one-request slice cannot
                    # also verify the root. A later successful root observation
                    # can resolve this bounded proof without re-fetching403 forever.
                    rs["release_access_verification"] = {
                        "http_status": 403, "observed_at": stamp(now),
                        "fingerprint": publication_fingerprint(records),
                    }
                    rs["availability_recheck_requested"] = True
                    interrupted = Interrupted(limited)
                    interrupted.partial = (records, rs, events)
                    raise interrupted from limited
                except HTTPError as root_error:
                    if root_error.code == 404:
                        raise gitlab.RootUnavailable("Release 403 verification confirmed root HTTP 404") from root_error
                    raise
                clear_unavailability(records, rs)
                rs["last_root_check_at"] = stamp(now)
                rs["_release_lookup_status"] = 403
                complete = False
            else:
                if work != "probe" and exc.code == 404:
                    raise gitlab.VerifyRoot("GitLab endpoint returned 404; root verification required") from exc
                if work != "probe" or client.root_status != 404:
                    raise
                complete = False
        except (gitlab.RateStop, ProviderStop) as exc:
            raise Interrupted(exc) from exc
        if work == "probe":
            if client.root_status in (200, 304):
                clear_unavailability(records, rs)
                rs["last_root_check_at"] = stamp(now)
                if verifying:
                    rs["last_availability_verification_at"] = stamp(now)
            rs["_repository_lookup_status"] = client.root_status
        if client.retry_at:
            rs["_provider_blocked_until"] = stamp(client.retry_at)
        return records, rs, events, complete, rate or {}
    module = probe if work == "probe" else activity
    poll = {"version": 1, "repositories": {repo: rs}, "rate": {"probe": rate or {}}}
    if (
        rate
        and rate.get("reset_at")
        and datetime.fromisoformat(rate["reset_at"].replace("Z", "+00:00")) <= now
    ):
        poll["rate"]["probe"] = {}
    lookups = {}
    previous_push = rs.get("last_seen_pushed_at")
    try:
        with transport(module, budget, now, opener, before_request) as lookups, redirect_stdout(StringIO()):
            if work == "probe":
                records, poll = probe.main(records=records, state=poll, scope={"mode": "adaptive"}, persist=False)
                rs = poll["repositories"][repo]
                complete = bool(rs.get("last_probe_at") == stamp(now) and not rs.get("last_error"))
                if pending_publication(rs) and not rs["publication"].get("metadata_complete"):
                    complete = False
                status_code = lookups.get(f"/repos/{repo}")
                if status_code in (200, 304):
                    clear_unavailability(records, rs)
                    rs["last_root_check_at"] = stamp(now)
                rs["_repository_lookup_status"] = status_code  # Popped before any persistence below.
            else:
                activity.load_rate_from_state(poll)
                records, rs, events, complete = activity_unit(repo, records, rs, events, now)
            rate = module.rate_snapshot()
    except Interrupted as exc:
        if work == "probe" and lookups.get(f"/repos/{repo}") in (200, 304) and rs.get("last_probe_at") == stamp(now):
            clear_unavailability(records, rs)
            rs["default_branch"] = next((metadata(p).get("default_branch") for p in records
                                         if metadata(p).get("default_branch")), rs.get("default_branch"))
            if pending_publication(rs) or previous_push != rs.get("last_seen_pushed_at") or not rs.get("last_deep_scan"):
                rs["scan_requested"] = True
                rs["scan_reason"] = "publication" if pending_publication(rs) else "changed"
            exc.partial = (records, rs, events)
        raise
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
    research_repositories = refresh_repositories(root, request_id, records)
    if research_repositories is not None:
        log(research_request=request_id, research_repositories=sorted(research_repositories))
    poll = read(root / POLL, {"version": 1, "repositories": {}})
    before_poll = copy.deepcopy(poll)
    catalogue = read(root / "state/project-catalog-state.json", {"projects": {}})
    publication = catalogue_delta(list(catalogue.get("projects", {}).values()), records)
    working = groups(records)
    prepare_publication(working, poll, publication, records)
    for repo, rows in working.items():
        rs = poll["repositories"].setdefault(repo, {})
        unavailable_state = (rs.get("repository_availability") or {}).get("status") == "unavailable"
        if any(((metadata(p).get("source_availability") or {}).get("status") == "unavailable") != unavailable_state
               for p in rows):
            rs["availability_recheck_requested"] = True
    progress = plan(before_progress, records, poll, now, request_id, full, research_repositories)
    activity_payload = read(root / "data/activity.json", {"events": [], "window_days": RETENTION_DAYS})
    original_events = event_groups(activity_payload, records)
    events = copy.deepcopy(original_events)
    touched, outcomes, rate = set(), {}, (poll.get("rate") or {}).get("probe", {})
    units = {work: 0 for work in WORKS}
    completed = {work: 0 for work in WORKS}
    cycle = progress.get("cycle")
    for work in ("probe", "releases", "activity"):
        remaining = budget.limit - budget.requests
        deadline = budget.deadline
        if work in ("probe", "releases") and cycle and any(
            ready(progress, r, "activity", now) and history_ready(r, poll["repositories"].get(r, {}))
            for r in cycle["pending"]["activity"]
        ):
            remaining //= 2
            deadline = budget.clock() + max(0, deadline - budget.clock()) / 2
        budget.begin_lane(work, remaining, deadline, remaining)
        # Activity repeats fair rounds so a small publication can finish multiple
        # pages in one slice while large repositories retain durable page cursors.
        while True:
            advanced = False
            for repo in candidates(progress, poll, work, now, limit):
                if not ready(progress, repo, work, now):
                    continue
                if repo not in touched and len(touched) >= limit:
                    continue
                if (
                    work == "activity" and not history_ready(repo, poll["repositories"].get(repo, {}))
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
                        lambda url: provider_request(progress, provider(repo), url, now, budget),
                    )
                    lookup_status = rs.pop("_repository_lookup_status", None)
                    release_status = rs.pop("_release_lookup_status", None)
                    if until := rs.pop("_provider_blocked_until", None):
                        blocked = progress.setdefault("provider_blocked_until", {})
                        blocked[provider(repo)] = max(blocked.get(provider(repo), ""), until)
                except BudgetStop:
                    break
                except Interrupted as exc:
                    cause = exc.cause
                    if partial := getattr(exc, "partial", None):
                        working[repo], poll["repositories"][repo], events[repo] = partial
                        units[work] += 1
                        outcomes.setdefault(repo, {})[work] = "partial"
                        progress["retry"][work][repo] = {"failures": 0, "attempt_at": stamp(now)}
                        if partial[1].get("availability_recheck_requested") and ready(progress, repo, "probe", now):
                            if repo in cycle["deferred"]["probe"]:
                                cycle["deferred"]["probe"].remove(repo)
                            for field in ("targets", "pending"):
                                if repo not in cycle[field]["probe"]:
                                    cycle[field]["probe"].append(repo)
                        if partial[1].get("scan_requested") and repo not in cycle["deferred"]["activity"]:
                            for field in ("targets", "pending"):
                                if repo not in cycle[field]["activity"]:
                                    cycle[field]["activity"].append(repo)
                    rate = getattr(exc, "rate", rate)
                    if isinstance(cause, BudgetStop):
                        break
                    if isinstance(cause, (ProviderStop, gitlab.RateStop)):
                        progress.setdefault("provider_blocked_until", {})[provider(repo)] = max(
                            progress.get("provider_blocked_until", {}).get(provider(repo), ""), stamp(cause.retry_at))
                        log(repo=repo, work=work, status="provider-cooldown", reason=str(cause), retry_at=stamp(cause.retry_at))
                        continue
                    if isinstance(
                        cause,
                        (probe.PrimaryReserve, activity.PrimaryReserve, probe.RateStop, activity.RateStop),
                    ):
                        reset = activity.parse_time(rate.get("reset_at")) if rate else None
                        progress.setdefault("provider_blocked_until", {})["github"] = stamp(
                            max(now + timedelta(minutes=2), reset or now + timedelta(minutes=15))
                        )
                        log(repo=repo, work=work, status="quota-stop", reason=str(cause))
                        continue
                    defer(progress, poll, repo, work, now, outcomes)
                    log(repo=repo, work=work, status="retry", reason=str(cause))
                    continue
                except gitlab.RootUnavailable:
                    unavailable(progress, poll, working, repo, now, outcomes)
                    continue
                except gitlab.VerifyRoot as exc:
                    rs = poll["repositories"].setdefault(repo, {})
                    verified = activity.parse_time(rs.get("last_availability_verification_at"))
                    fresh_root = rs.get("last_root_check_at") == stamp(now)
                    needs_verification = not fresh_root and (verified is None or now - verified >= timedelta(hours=6))
                    defer(progress, poll, repo, work, now, outcomes)
                    if not needs_verification:
                        log(repo=repo, work=work, status="endpoint-unavailable", reason=str(exc))
                        continue
                    rs["availability_recheck_requested"] = True
                    # A branch/release 404 does not prove the root is unavailable.
                    # The next bounded continuation verifies it and can discover
                    # a renamed default branch without waiting for daily metadata.
                    if ready(progress, repo, "probe", now):
                        for field in ("targets", "pending"):
                            if repo not in cycle[field]["probe"]:
                                cycle[field]["probe"].append(repo)
                        if repo in cycle["deferred"]["probe"]:
                            cycle["deferred"]["probe"].remove(repo)
                    log(repo=repo, work=work, status="verify-root", reason=str(exc))
                    continue
                except Exception as exc:
                    defer(progress, poll, repo, work, now, outcomes)
                    log(repo=repo, work=work, status="retry", reason=str(exc))
                    continue
                finally:
                    budget.end_record()
                touched.add(repo)
                if release_status == 403:
                    working[repo], poll["repositories"][repo], events[repo] = rows, rs, evs
                    release_unavailable(progress, poll, working, repo, now, outcomes)
                    continue
                if not done and work == "probe":
                    if lookup_status == 404:
                        unavailable(progress, poll, working, repo, now, outcomes)
                    else:
                        if lookup_status in (200, 304):
                            clear_unavailability(working[repo], rs)
                            rs["last_root_check_at"] = stamp(now)
                            poll["repositories"][repo] = rs
                        defer(progress, poll, repo, work, now, outcomes)
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
                if (
                    work == "probe"
                    and rs.get("scan_requested")
                    and repo not in cycle["pending"]["activity"]
                    and repo not in cycle["deferred"]["activity"]
                ):
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
                if work in ("activity", "releases") and advanced:
                    continue
            break
        budget.end_lane()
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


def add_publication_work(progress, records, poll, now):
    cycle = progress.get("cycle")
    if not cycle:
        return
    current = groups(records)
    for work in WORKS:
        for field in ("targets", "pending", "deferred"):
            cycle[field][work] = [r for r in cycle[field][work] if r in current]
    for repo in sorted(current):
        rs = poll["repositories"].get(repo, {})
        if not pending_publication(rs):
            continue
        for work, field in (("probe", "metadata_complete"), ("activity", "history_complete"), ("releases", "releases_complete")):
            if work == "releases" and provider(repo) != "gitlab":
                continue
            if not rs["publication"].get(field) and ready(progress, repo, work, now) and repo not in cycle["deferred"][work]:
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


def provider_status(progress, now):
    minute = int(now.timestamp()) // 60
    out = {}
    for kind, usage in progress.get("provider_usage", {}).items():
        endpoints = {}
        for key, row in usage.get("minutes", {}).items():
            if int(key) < minute - 60:
                continue
            for endpoint, count in row.items():
                endpoints[endpoint] = endpoints.get(endpoint, 0) + count
        out[kind] = {"requests_past_hour": sum(endpoints.values()), "hourly_limit": HOURLY_LIMITS[kind],
                     "endpoints": endpoints,
                     "blocked_until": progress.get("provider_blocked_until", {}).get(kind)}
    return out


def status(progress, now=None, poll=None):
    now = now or datetime.now(timezone.utc)
    cycle = progress.get("cycle")
    result = {
        "active": active(progress),
        "token": token(progress),
        "cycle": cycle.get("id") if cycle else None,
        "mode": cycle.get("mode") if cycle else None,
        "providers": provider_status(progress, now),
        "completed": {},
        "remaining": {},
        "deferred": {},
        "retry_pending": {
            work: sum(bool(v.get("retry_at")) for v in progress["retry"][work].values())
            for work in WORKS
        },
    }
    if cycle:
        for work in WORKS:
            result["remaining"][work] = len(cycle["pending"][work])
            result["deferred"][work] = len(cycle["deferred"][work])
            result["completed"][work] = (
                len(cycle["targets"][work]) - len(cycle["pending"][work]) - len(cycle["deferred"][work])
            )
    result["eligible"] = bool(
        active(progress)
        and any(
            ready(progress, repo, work, now)
            and not (
                work == "activity"
                and poll is not None
                and not history_ready(repo, poll.get("repositories", {}).get(repo, {}))
            )
            for work in WORKS
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
    if before_progress != migrate_progress(bundle["progress_before"]):
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
        payload = read(stage / "data/activity.json", {"window_days": RETENTION_DAYS, "events": []})
        original_activity = copy.deepcopy(payload)
        events = event_groups(payload, records)
        catalogue = read(stage / "state/project-catalog-state.json", {"projects": {}})
        publication = catalogue_delta(list(catalogue.get("projects", {}).values()), records)
        prepare_publication(by_repo, poll, publication, records)
        progress = copy.deepcopy(bundle["progress_after"])
        progress.setdefault("retry", {}).setdefault("releases", {})
        if progress.get("cycle"):
            for field in ("targets", "pending", "deferred"):
                progress["cycle"].setdefault(field, {}).setdefault("releases", [])
        accepted, conflicts = [], []
        for row in bundle["results"]:
            repo = row["repo"]
            originals = guard_records.get(repo, [])
            safe = (
                source_matches(originals, row["source"])
                and all(set(fields) in (set(OWNED), set(OWNED) - {"gitlab"}) for fields in row["before"].values())
                and all(set(row["before"].get(pid, {})) == set(fields) for pid, fields in row["after"].items())
                and {p["id"]: {k: v for k, v in owned(p).items() if k in row["before"].get(p["id"], {})} for p in originals} == row["before"]
                and guard_poll["repositories"].get(repo, {}) == row["state_before"]
                and events.get(repo, []) == row["events_before"]
                and set(row["after"]) == {p["id"] for p in originals}
                and all(set(fields) in (set(OWNED), set(OWNED) - {"gitlab"}) for fields in row["after"].values())
            )
            if not safe:
                conflicts.append(repo)
                for work in WORKS:
                    if (
                        row["outcomes"].get(work) in {"complete", "retry"}
                        and repo in progress["cycle"]["targets"][work]
                        and repo not in progress["cycle"]["pending"][work]
                    ):
                        progress["cycle"]["pending"][work].append(repo)
                    if repo in progress["cycle"]["deferred"][work]:
                        progress["cycle"]["deferred"][work].remove(repo)
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
        add_publication_work(progress, records, poll, now)
        live = set(by_repo)
        poll["repositories"] = {r: v for r, v in poll["repositories"].items() if r in live}
        for work in WORKS:
            progress["retry"][work] = {r: v for r, v in progress["retry"][work].items() if r in live}
        old_rate = (poll.get("rate") or {}).get("probe") or {}
        if bundle.get("rate") and (bundle["rate"].get("checked_at") or "") >= (
            old_rate.get("checked_at") or ""
        ):
            poll.setdefault("rate", {})["probe"] = bundle["rate"]
        cutoff = now - timedelta(days=RETENTION_DAYS)
        current_projects = {p["id"]: p for p in records}
        joined = [
            e
            for rows in events.values()
            for e in rows
            if (
                e.get("type") not in {"commit", "daily_commits", "release"}
                or (
                    e.get("project_id") in current_projects
                    and e.get("repository") == repository(current_projects[e["project_id"]])
                    and (e.get("type") != "release" or not selectors(current_projects[e["project_id"]])[1])
                    and (
                        e.get("type") != "commit"
                        or not e.get("branches")
                        or any(
                            matches_branch(current_projects[e["project_id"]], b)
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
        write_activity(stage / "data/activity.json", payload, records)
        (stage / POLL).write_bytes(encode(poll))
        with redirect_stdout(StringIO()):
            record_catalogue(stage)
        validate(stage / "data/projects.json", stage / "data/activity.json")
        # A zero-work retry must not manufacture continuation progress.
        made_progress = (
            progress != before_progress
            or bool(accepted)
            or original_activity.get("window_days") != RETENTION_DAYS
            or original_activity.get("events") != read(stage / "data/activity.json", {})["events"]
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
