#!/usr/bin/env python3
"""Incrementally collect GitHub commit activity for repositories due to scan.

The collector consumes state/github-poll-state.json written by refresh_github.py.
It keeps 180 days of local history but only requests commits since each branch's
last successful scan, with a one-day overlap for safety.
"""
from __future__ import annotations

import json
import math
import os
import re
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen

from activity_history import compact_history, freeze_addition_context, write_activity
from refresh_github import probe_interval_minutes

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = ROOT / "data" / "projects.json"
ACTIVITY = ROOT / "data" / "activity.json"
STATE = ROOT / "state" / "github-poll-state.json"
API = "https://api.github.com"
TOKEN = os.environ.get("GITHUB_TOKEN", "")
NOW = datetime.now(timezone.utc)
NOW_ISO = NOW.isoformat(timespec="seconds").replace("+00:00", "Z")
DAYS = 180
CUTOFF = NOW - timedelta(days=DAYS)
MIN_RESERVE = int(os.environ.get("GITHUB_MIN_RATE_RESERVE", "100"))
MAX_RESERVE = int(os.environ.get("GITHUB_MAX_RATE_RESERVE", "250"))
RESERVE_FRACTION = float(os.environ.get("GITHUB_RATE_RESERVE_FRACTION", "0.15"))
MAX_HTTP_REQUESTS = int(os.environ.get("GITHUB_HTTP_SAFETY_CAP", "4000"))
REQUEST_DELAY = float(os.environ.get("GITHUB_REQUEST_DELAY", "0.10"))
REQUESTS = 0
RATE_LIMIT = None
RATE_REMAINING = None
RATE_RESET = None
MAX_BRANCHES = 100
MAX_PAGES = 5
DETAIL_THRESHOLD = 25

AI_PATTERNS = [
    (re.compile(r"co-authored-by:.*\b(?:claude|anthropic)\b", re.I), "Claude"),
    (re.compile(r"co-authored-by:.*\b(?:chatgpt|openai)\b", re.I), "ChatGPT"),
    (re.compile(r"co-authored-by:.*\bcopilot\b", re.I), "GitHub Copilot"),
    (re.compile(r"co-authored-by:.*\bgemini\b", re.I), "Gemini"),
]

class RateStop(RuntimeError):
    pass

class PrimaryReserve(RateStop):
    pass

def effective_reserve():
    if RATE_LIMIT is None:
        return MIN_RESERVE
    proportional = int(math.ceil(RATE_LIMIT * RESERVE_FRACTION))
    floor = min(MIN_RESERVE, max(1, RATE_LIMIT // 4))
    return min(MAX_RESERVE, max(floor, proportional))

def update_rate(headers):
    global RATE_LIMIT, RATE_REMAINING, RATE_RESET
    if not headers:
        return
    try:
        if headers.get("X-RateLimit-Limit") is not None:
            RATE_LIMIT = int(headers["X-RateLimit-Limit"])
        if headers.get("X-RateLimit-Remaining") is not None:
            RATE_REMAINING = int(headers["X-RateLimit-Remaining"])
        if headers.get("X-RateLimit-Reset") is not None:
            RATE_RESET = int(headers["X-RateLimit-Reset"])
    except (TypeError, ValueError):
        pass

def load_rate_from_state(state):
    global RATE_LIMIT, RATE_REMAINING, RATE_RESET
    snap = ((state.get("rate") or {}).get("probe") or {})
    RATE_LIMIT = snap.get("limit")
    RATE_REMAINING = snap.get("remaining")
    reset = snap.get("reset_at")
    if reset:
        try:
            RATE_RESET = int(datetime.fromisoformat(reset.replace("Z", "+00:00")).timestamp())
        except ValueError:
            RATE_RESET = None

def rate_snapshot():
    reset_at = None
    if RATE_RESET:
        reset_at = datetime.fromtimestamp(RATE_RESET, timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
    return {
        "checked_at": datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
        "http_requests": REQUESTS,
        "limit": RATE_LIMIT,
        "remaining": RATE_REMAINING,
        "reserve": effective_reserve(),
        "reset_at": reset_at,
    }

def primary_available():
    return RATE_REMAINING is None or RATE_REMAINING > effective_reserve()

def append_summary(label):
    path = os.environ.get("GITHUB_STEP_SUMMARY")
    if not path:
        return
    snap = rate_snapshot()
    with open(path, "a", encoding="utf-8") as handle:
        handle.write(
            f"### {label}\n"
            f"- HTTP requests: **{snap['http_requests']}**\n"
            f"- Primary REST quota: **{snap['remaining'] if snap['remaining'] is not None else '?'}"
            f" / {snap['limit'] if snap['limit'] is not None else '?'}** remaining"
            f"; dynamic reserve **{snap['reserve']}**\n"
            f"- Rate reset: **{snap['reset_at'] or '?'}**\n\n"
        )

def github_repo(url):
    match = re.fullmatch(r"https?://github\.com/([^/]+)/([^/#?]+?)(?:\.git)?/?", url or "")
    return f"{match.group(1)}/{match.group(2)}" if match else None

def load_json(path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return default

def save_state(state):
    STATE.parent.mkdir(parents=True, exist_ok=True)
    state["updated_at"] = NOW_ISO
    STATE.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def api(path, allow_404=False):
    global REQUESTS
    if REQUESTS >= MAX_HTTP_REQUESTS:
        raise RateStop(f"HTTP safety cap reached ({MAX_HTTP_REQUESTS})")
    if not primary_available():
        raise PrimaryReserve(
            f"primary rate reserve reached ({RATE_REMAINING} remaining; reserve {effective_reserve()})"
        )

    REQUESTS += 1
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "legacy-reverse-engineering-tracker",
        "X-GitHub-Api-Version": "2026-03-10",
    }
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    try:
        with urlopen(Request(API + path, headers=headers), timeout=30) as response:
            update_rate(dict(response.headers))
            body = json.load(response)
            time.sleep(REQUEST_DELAY)
            return body
    except HTTPError as exc:
        response_headers = dict(exc.headers) if exc.headers else {}
        update_rate(response_headers)
        body = exc.read().decode("utf-8", "replace")
        time.sleep(REQUEST_DELAY)
        if allow_404 and exc.code == 404:
            return None
        if exc.code in (403, 429) and (
            "rate limit" in body.lower() or "secondary" in body.lower()
        ):
            raise RateStop(f"GitHub rate limit response {exc.code}: {body[:180]}")
        raise RuntimeError(f"GitHub API {exc.code} for {path}: {body[:300]}") from exc

def parse_time(value):
    if not value:
        return None
    try:
        if len(value) == 10:
            return datetime.fromisoformat(value + "T00:00:00+00:00")
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (TypeError, ValueError):
        return None

def commit_date(item):
    commit = item.get("commit") or {}
    return (commit.get("committer") or {}).get("date") or (commit.get("author") or {}).get("date")

def list_branches(repo, explicit):
    branches = api(f"/repos/{repo}/branches?per_page={MAX_BRANCHES}") or []
    by_name = {b.get("name"): b for b in branches if b.get("name")}
    for branch in explicit:
        if branch and branch not in by_name:
            found = api(f"/repos/{repo}/branches/{quote(branch, safe='')}", allow_404=True)
            if found:
                by_name[branch] = found
    return by_name

def fetch_commits(repo, branch, since, path=None):
    out = []
    for page in range(1, MAX_PAGES + 1):
        params = {
            "sha": branch,
            "since": since.isoformat(timespec="seconds").replace("+00:00", "Z"),
            "per_page": 100,
            "page": page,
        }
        if path:
            params["path"] = path
        chunk = api(f"/repos/{repo}/commits?{urlencode(params)}", allow_404=True) or []
        out.extend(chunk)
        if len(chunk) < 100:
            break
    return out

def event_from_commit(project_id, repo, item):
    commit = item.get("commit") or {}
    author = item.get("author") or {}
    commit_author = commit.get("author") or {}
    message = commit.get("message") or ""
    return {
        "type": "commit",
        "date": commit_date(item),
        "project_id": project_id,
        "repository": repo,
        "sha": item.get("sha"),
        "title": message.splitlines()[0] if message else (item.get("sha") or "")[:12],
        "message": message,
        "url": item.get("html_url"),
        "author": author.get("login") or commit_author.get("name"),
        "branches": [],
    }

def project_matches_branch(project, branch):
    explicit = project.get("github_branch")
    if explicit:
        return explicit == branch
    gh = project.get("github") or {}
    tracked = gh.get("tracking_branch") or gh.get("default_branch")
    return tracked == branch if tracked else True

def path_touched(files, project_path):
    prefix = project_path.rstrip("/") + "/"
    exact = project_path.rstrip("/")
    return any(
        (f.get("filename") == exact or (f.get("filename") or "").startswith(prefix))
        for f in files
    )

def add_event(events, project, repo, item, branch, newest):
    sha = item.get("sha")
    when = commit_date(item)
    if not sha or not when:
        return
    key = (project["id"], repo, sha)
    event = events.get(key)
    if not event:
        event = event_from_commit(project["id"], repo, item)
        events[key] = event
    if branch not in event["branches"]:
        event["branches"].append(branch)
    old = newest.get(project["id"])
    if old is None or parse_time(when) > parse_time(commit_date(old)):
        newest[project["id"]] = item

def attribute_with_details(events, newest, repo, branch, items, root_projects, path_projects):
    for item in items:
        for project in root_projects:
            add_event(events, project, repo, item, branch, newest)
        if not path_projects:
            continue
        detail = api(f"/repos/{repo}/commits/{item.get('sha')}") or {}
        files = detail.get("files") or []
        for project in path_projects:
            if path_touched(files, project["github_path"]):
                add_event(events, project, repo, item, branch, newest)

def attribute_with_path_queries(events, newest, repo, branch, since, items, root_projects, path_projects):
    for item in items:
        for project in root_projects:
            add_event(events, project, repo, item, branch, newest)
    for project in path_projects:
        matched = fetch_commits(repo, branch, since, project["github_path"])
        for item in matched:
            add_event(events, project, repo, item, branch, newest)

def detect_ai(record, items):
    ai = record.setdefault("ai", {"usage": None, "tools": []})
    tools = set(ai.get("tools") or [])
    evidence = list(ai.get("evidence") or [])
    hits = {}
    examples = {}
    for item in items:
        message = ((item.get("commit") or {}).get("message") or "")
        for pattern, tool in AI_PATTERNS:
            if pattern.search(message):
                hits[tool] = hits.get(tool, 0) + 1
                examples.setdefault(tool, (item.get("sha") or "")[:12])
                tools.add(tool)
    for tool, count in hits.items():
        marker = f"{tool} co-author trailer observed in recent tracked commits"
        evidence = [e for e in evidence if not e.startswith(marker)]
        evidence.append(f"{marker}: {count} in this scan (example {examples[tool]})")
    if tools:
        ai["usage"] = True
        ai["tools"] = sorted(tools)
        ai["evidence"] = evidence

def activity_state(value):
    day = parse_time(value)
    if not day:
        return None
    age = (NOW.date() - day.date()).days
    if age <= 90:
        return "active"
    if age <= 365:
        return "recent"
    if age <= 730:
        return "quiet"
    return "dormant"

def scan_order(repositories, state):
    """Prioritize detected changes, then repositories least recently deep-scanned."""
    repo_state = state.get("repositories", {})
    reason_rank = {"changed": 0, "new": 1, "new-project": 1, "backfill": 1, "scheduled": 2}
    def key(repo):
        rs = repo_state.get(repo, {})
        reason = rs.get("scan_reason") or "scheduled"
        last = rs.get("last_deep_scan") or rs.get("first_seen_at") or ""
        return (reason_rank.get(reason, 3), last, repo.casefold())
    return sorted(repositories, key=key)

def update_project_latest(project, item):
    when = commit_date(item)
    if not when:
        return
    day = when[:10]
    current = parse_time(project.get("last_activity"))
    if current is None or parse_time(when) >= current:
        project["last_activity"] = day
        gh = project.setdefault("github", {})
        commit = item.get("commit") or {}
        gh["latest_commit"] = {
            "sha": item.get("sha"),
            "date": day,
            "message": (commit.get("message") or "").splitlines()[0],
            "url": item.get("html_url"),
        }
        gh["activity_state"] = activity_state(day)

def repair_project_latest(project, event):
    """Repair a latest-commit pointer proven to have come from the wrong branch."""
    when = event.get("date") or ""
    if not when:
        return
    day = when[:10]
    project["last_activity"] = day
    gh = project.setdefault("github", {})
    gh["latest_commit"] = {
        "sha": event.get("sha"),
        "date": day,
        "message": event.get("title") or (event.get("message") or "").splitlines()[0],
        "url": event.get("url"),
    }
    gh["activity_state"] = activity_state(day)

def advance_probe_deadlines(by_repo, state, now=NOW):
    """Promote newly scanned projects to a faster probe tier immediately."""
    for repo, projects in by_repo.items():
        rs = state["repositories"].get(repo)
        if not rs:
            continue
        newest = max((parse_time(p.get("last_activity")) for p in projects if parse_time(p.get("last_activity"))), default=None)
        archived = any((p.get("github") or {}).get("archived") for p in projects)
        interval = probe_interval_minutes(newest.date().isoformat() if newest else None, archived)
        prior = rs.get("probe_interval_minutes")
        if prior is not None and interval >= prior:
            continue
        rs["probe_interval_minutes"] = interval
        due = now + timedelta(minutes=interval)
        old_due = parse_time(rs.get("next_probe_due_at"))
        if old_due is None or due < old_due:
            rs["next_probe_due_at"] = due.isoformat(timespec="seconds").replace("+00:00", "Z")

def main():
    projects = load_json(PROJECTS, [])
    payload = load_json(ACTIVITY, {"generated_at": None, "window_days": DAYS, "events": []})
    state = load_json(STATE, {"version": 1, "repositories": {}})
    state.setdefault("repositories", {})
    load_rate_from_state(state)

    by_repo = {}
    project_by_id = {p["id"]: p for p in projects}
    for project in projects:
        repo = github_repo(project.get("repo"))
        if repo:
            by_repo.setdefault(repo, []).append(project)

    events = {}
    summaries = []
    project_events = []
    repair_latest_ids = set()
    for old in payload.get("events", []):
        when = parse_time(old.get("date"))
        if not when or when < CUTOFF:
            continue
        if old.get("type") != "commit":
            if old.get("type") == "daily_commits":
                if old.get("project_id") in project_by_id:
                    summaries.append(old)
                continue
            # Catalogue-change events are persisted independently of the current
            # project set so a removal remains visible after its record is gone.
            project_events.append(old)
            continue
        project = project_by_id.get(old.get("project_id"))
        if not project:
            continue
        old["branches"] = sorted(set(old.get("branches") or []))
        if old["branches"] and not any(project_matches_branch(project, branch) for branch in old["branches"]):
            latest = ((project.get("github") or {}).get("latest_commit") or {}).get("sha")
            if latest and latest == old.get("sha"):
                repair_latest_ids.add(project["id"])
            continue
        key = (old.get("project_id"), old.get("repository"), old.get("sha"))
        events[key] = old

    baseline = parse_time(payload.get("generated_at")) or (NOW - timedelta(days=2))
    newest = {}
    scanned = commits_seen = pruned_branches = 0
    stopped = None

    for repo in scan_order(by_repo, state):
        rs = state["repositories"].setdefault(repo, {})
        if not rs.get("scan_requested"):
            continue

        repo_projects = by_repo[repo]
        default = rs.get("default_branch") or next(
            (p.get("github", {}).get("default_branch") for p in repo_projects if p.get("github")),
            "main",
        )
        explicit = {p.get("github_branch") for p in repo_projects if p.get("github_branch")}
        explicit.add(default)
        branch_state = rs.setdefault("branches", {})
        full_success = True
        backfill = rs.get("scan_reason") in {"new", "new-project", "backfill"}

        try:
            branches = list_branches(repo, explicit)
            present_branches = set(branches)
            for stale in list(branch_state):
                if stale not in present_branches:
                    branch_state.pop(stale, None)
                    pruned_branches += 1
            for branch, branch_info in branches.items():
                bs = branch_state.setdefault(branch, {})
                tip = ((branch_info.get("commit") or {}).get("sha"))
                if tip and tip == bs.get("tip_sha") and not backfill:
                    continue

                if backfill:
                    since = CUTOFF
                else:
                    last_scan = (
                        parse_time(bs.get("last_scan_at"))
                        or parse_time(rs.get("last_deep_scan"))
                        or parse_time(rs.get("first_seen_at"))
                        or baseline
                    )
                    since = max(CUTOFF, last_scan - timedelta(days=1))
                # A newly tracked repository may be scanned long after its recent
                # history happened. Bootstrap its first branch scan from the retained
                # activity window rather than from first_seen_at, otherwise pre-existing
                # commits (e.g. a commit a few days before the project was added) never
                # enter data/activity.json.
                if not bs.get("last_scan_at") and not rs.get("last_deep_scan"):
                    since = CUTOFF
                items = fetch_commits(repo, branch, since)
                commits_seen += len(items)

                candidates = [p for p in repo_projects if project_matches_branch(p, branch)]
                root_projects = [p for p in candidates if not p.get("github_path")]
                path_projects = [p for p in candidates if p.get("github_path")]

                if path_projects and len(items) > min(DETAIL_THRESHOLD, max(1, len(path_projects) * 2)):
                    attribute_with_path_queries(
                        events, newest, repo, branch, since, items, root_projects, path_projects
                    )
                else:
                    attribute_with_details(
                        events, newest, repo, branch, items, root_projects, path_projects
                    )

                bs["tip_sha"] = tip
                bs["last_scan_at"] = NOW_ISO
                if items:
                    bs["last_commit_at"] = commit_date(items[0])
        except RateStop as exc:
            stopped = str(exc)
            full_success = False
            print(f"RATE STOP during {repo}: {exc}", file=sys.stderr)
        except Exception as exc:
            full_success = False
            rs["last_error"] = str(exc)[:400]
            print(f"WARNING: activity {repo}: {exc}", file=sys.stderr)

        if full_success:
            rs["last_deep_scan"] = NOW_ISO
            rs["last_deep_scan_project_ids"] = sorted(p["id"] for p in repo_projects)
            rs["scan_requested"] = False
            rs.pop("scan_reason", None)
            rs.pop("last_error", None)
            scanned += 1
        if stopped:
            break

    for project_id, item in newest.items():
        project = project_by_id.get(project_id)
        if project:
            update_project_latest(project, item)

    advance_probe_deadlines(by_repo, state)

    if repair_latest_ids:
        latest_valid = {}
        for event in events.values():
            project_id = event.get("project_id")
            if project_id not in repair_latest_ids:
                continue
            when = parse_time(event.get("date"))
            old = latest_valid.get(project_id)
            if when and (old is None or when > parse_time(old.get("date"))):
                latest_valid[project_id] = event
        for project_id, event in latest_valid.items():
            project = project_by_id.get(project_id)
            if project:
                repair_project_latest(project, event)

    items_by_project = {}
    for event in events.values():
        when = parse_time(event.get("date"))
        if when and when >= baseline - timedelta(days=1):
            fake = {
                "sha": event.get("sha"),
                "commit": {"message": event.get("message") or ""},
            }
            items_by_project.setdefault(event.get("project_id"), []).append(fake)
    for project_id, items in items_by_project.items():
        # The rolling baseline moves on every refresh. Recomputing evidence
        # when no commits were fetched changes counts/examples on an idle run.
        if project_id not in newest:
            continue
        project = project_by_id.get(project_id)
        if project:
            detect_ai(project, items)

    output = compact_history(list(events.values()) + summaries + project_events, NOW)
    for event in output:
        event["branches"] = sorted(set(event.get("branches") or []))

    freeze_addition_context(output, projects, state["repositories"], NOW)

    payload = {
        "generated_at": NOW_ISO,
        "window_days": DAYS,
        "events": output,
    }
    write_activity(ACTIVITY, payload)
    projects.sort(key=lambda r: ((r.get("title") or "").casefold(), r.get("id") or ""))
    PROJECTS.write_text(json.dumps(projects, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    state.setdefault("rate", {})["activity"] = rate_snapshot()
    save_state(state)
    append_summary("GitHub incremental activity phase")

    pending = sum(1 for rs in state["repositories"].values() if rs.get("scan_requested"))
    print(
        f"Deep-scanned {scanned} repositories; saw {commits_seen} branch commits; "
        f"pruned {pruned_branches} stale branch-state entries; "
        f"{pending} repositories remain queued; retained {len(output)} activity events; "
        f"made {REQUESTS} activity HTTP requests; primary remaining "
        f"{RATE_REMAINING if RATE_REMAINING is not None else '?'}/"
        f"{RATE_LIMIT if RATE_LIMIT is not None else '?'}; reserve {effective_reserve()}."
    )
    if stopped:
        print(f"Stopped early to preserve API quota: {stopped}")

if __name__ == "__main__":
    main()
