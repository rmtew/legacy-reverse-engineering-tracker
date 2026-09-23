#!/usr/bin/env python3
"""Incrementally collect GitHub commit activity for repositories due to scan.

The collector consumes state/github-poll-state.json written by refresh_github.py.
It keeps 180 days of local history but only requests commits since each branch's
last successful scan, with a one-day overlap for safety.
"""
from __future__ import annotations

import json
import os
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen

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
RESERVE = int(os.environ.get("GITHUB_RATE_RESERVE", "250"))
MAX_REQUESTS = int(os.environ.get("GITHUB_ACTIVITY_REQUEST_BUDGET", "450"))
REQUESTS = 0
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
    if REQUESTS >= MAX_REQUESTS:
        raise RateStop(f"activity request budget reached ({MAX_REQUESTS})")
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
            remaining = response.headers.get("X-RateLimit-Remaining")
            if remaining is not None and int(remaining) <= RESERVE:
                raise RateStop(f"GitHub primary rate limit reserve reached ({remaining} remaining)")
            return json.load(response)
    except HTTPError as exc:
        body = exc.read().decode("utf-8", "replace")
        remaining = exc.headers.get("X-RateLimit-Remaining") if exc.headers else None
        if allow_404 and exc.code == 404:
            return None
        if exc.code in (403, 429) and ("rate limit" in body.lower() or "secondary" in body.lower()):
            raise RateStop(f"GitHub rate limit response {exc.code}: {body[:180]}")
        if remaining is not None and int(remaining) <= RESERVE:
            raise RateStop(f"GitHub primary rate limit reserve reached ({remaining} remaining)")
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
    return not explicit or explicit == branch

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
    reason_rank = {"changed": 0, "new": 1, "scheduled": 2}
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

def main():
    projects = load_json(PROJECTS, [])
    payload = load_json(ACTIVITY, {"generated_at": None, "window_days": DAYS, "events": []})
    state = load_json(STATE, {"version": 1, "repositories": {}})
    state.setdefault("repositories", {})

    by_repo = {}
    project_by_id = {p["id"]: p for p in projects}
    for project in projects:
        repo = github_repo(project.get("repo"))
        if repo:
            by_repo.setdefault(repo, []).append(project)

    events = {}
    for old in payload.get("events", []):
        when = parse_time(old.get("date"))
        if not when or when < CUTOFF or old.get("project_id") not in project_by_id:
            continue
        key = (old.get("project_id"), old.get("repository"), old.get("sha"))
        old["branches"] = sorted(set(old.get("branches") or []))
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
                if tip and tip == bs.get("tip_sha"):
                    continue

                last_scan = (
                    parse_time(bs.get("last_scan_at"))
                    or parse_time(rs.get("last_deep_scan"))
                    or parse_time(rs.get("first_seen_at"))
                    or baseline
                )
                since = max(CUTOFF, last_scan - timedelta(days=1))
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
        project = project_by_id.get(project_id)
        if project:
            detect_ai(project, items)

    output = sorted(
        events.values(),
        key=lambda e: (e.get("date") or "", e.get("repository") or "", e.get("sha") or ""),
        reverse=True,
    )
    for event in output:
        event["branches"] = sorted(set(event.get("branches") or []))

    payload = {
        "generated_at": NOW_ISO,
        "window_days": DAYS,
        "events": output,
    }
    ACTIVITY.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    projects.sort(key=lambda r: ((r.get("title") or "").casefold(), r.get("id") or ""))
    PROJECTS.write_text(json.dumps(projects, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    save_state(state)

    pending = sum(1 for rs in state["repositories"].values() if rs.get("scan_requested"))
    print(
        f"Deep-scanned {scanned} repositories; saw {commits_seen} branch commits; "
        f"pruned {pruned_branches} stale branch-state entries; "
        f"{pending} repositories remain queued; retained {len(output)} activity events; "
        f"used {REQUESTS}/{MAX_REQUESTS} activity requests."
    )
    if stopped:
        print(f"Stopped early to preserve API quota: {stopped}")

if __name__ == "__main__":
    main()
