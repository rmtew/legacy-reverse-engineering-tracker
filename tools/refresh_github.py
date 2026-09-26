#!/usr/bin/env python3
"""Adaptive GitHub repository polling and metadata refresh.

Repository probes have a separate cadence from deep activity scans. Recently
active projects are probed frequently; quiet projects are checked less often.
A changed pushed_at timestamp always requests an immediate deep activity scan.
"""
from __future__ import annotations

import hashlib
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

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = ROOT / "data" / "projects.json"
STATE = ROOT / "state" / "github-poll-state.json"
API = "https://api.github.com"
TOKEN = os.environ.get("GITHUB_TOKEN", "")
RUN_AT = datetime.now(timezone.utc)
TODAY = RUN_AT.date()
MIN_RESERVE = int(os.environ.get("GITHUB_MIN_RATE_RESERVE", "100"))
MAX_RESERVE = int(os.environ.get("GITHUB_MAX_RATE_RESERVE", "250"))
RESERVE_FRACTION = float(os.environ.get("GITHUB_RATE_RESERVE_FRACTION", "0.15"))
MAX_HTTP_REQUESTS = int(os.environ.get("GITHUB_HTTP_SAFETY_CAP", "4000"))
REQUEST_DELAY = float(os.environ.get("GITHUB_REQUEST_DELAY", "0.10"))
REQUESTS = 0
NOT_MODIFIED = 0
CONDITIONAL_REQUESTS = 0
STATUS_COUNTS = {}
RATE_LIMIT = None
RATE_REMAINING = None
RATE_RESET = None
RATE_START_REMAINING = None
FORCE_FULL_PROBE = os.environ.get("GITHUB_FORCE_FULL_PROBE", "").lower() == "true"

AI_CONFIG = {
    "claude.md": "Claude",
    ".claude": "Claude",
    "codex.md": "OpenAI Codex",
}

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
    global RATE_LIMIT, RATE_REMAINING, RATE_RESET, RATE_START_REMAINING
    if not headers:
        return
    try:
        if headers.get("X-RateLimit-Limit") is not None:
            RATE_LIMIT = int(headers["X-RateLimit-Limit"])
        if headers.get("X-RateLimit-Remaining") is not None:
            RATE_REMAINING = int(headers["X-RateLimit-Remaining"])
            if RATE_START_REMAINING is None:
                RATE_START_REMAINING = RATE_REMAINING
        if headers.get("X-RateLimit-Reset") is not None:
            RATE_RESET = int(headers["X-RateLimit-Reset"])
    except (TypeError, ValueError):
        pass

def rate_snapshot():
    reset_at = None
    if RATE_RESET:
        reset_at = datetime.fromtimestamp(RATE_RESET, timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
    return {
        "checked_at": datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
        "http_requests": REQUESTS,
        "not_modified": NOT_MODIFIED,
        "conditional_requests": CONDITIONAL_REQUESTS,
        "statuses": dict(STATUS_COUNTS),
        "limit": RATE_LIMIT,
        "remaining_after_first_request": RATE_START_REMAINING,
        "remaining": RATE_REMAINING,
        "quota_delta_after_first_request": (
            RATE_START_REMAINING - RATE_REMAINING
            if RATE_START_REMAINING is not None and RATE_REMAINING is not None else None
        ),
        "duration_seconds": round((datetime.now(timezone.utc) - RUN_AT).total_seconds()),
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
            f"- HTTP requests: **{snap['http_requests']}**"
            f" ({snap['not_modified']} / {snap['conditional_requests']} conditional 304 responses)\n"
            f"- Primary REST quota: **{snap['remaining'] if snap['remaining'] is not None else '?'}"
            f" / {snap['limit'] if snap['limit'] is not None else '?'}** remaining"
            f"; dynamic reserve **{snap['reserve']}**\n"
            f"- Quota after first response: **{snap['remaining_after_first_request']}**;"
            f" change since then: **{snap['quota_delta_after_first_request']}**;"
            f" statuses: **{snap['statuses']}**; elapsed: **{snap['duration_seconds']} s**\n"
            f"- Rate reset: **{snap['reset_at'] or '?'}**\n\n"
        )
        if CONDITIONAL_REQUESTS >= 20 and NOT_MODIFIED / CONDITIONAL_REQUESTS < 0.25:
            handle.write("- ETag diagnostic: fewer than 25% of conditional probes returned 304; do not budget probes as free.\n\n")

def load_state():
    if not STATE.exists():
        return {"version": 1, "repositories": {}}
    try:
        data = json.loads(STATE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        data = {}
    data.setdefault("version", 1)
    data.setdefault("repositories", {})
    return data

def save_state(state):
    STATE.parent.mkdir(parents=True, exist_ok=True)
    state["updated_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
    STATE.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def github_repo(url):
    match = re.fullmatch(r"https?://github\.com/([^/]+)/([^/#?]+?)(?:\.git)?/?", url or "")
    return f"{match.group(1)}/{match.group(2)}" if match else None

def iso_date(value):
    return value[:10] if value else None

def parse_day(value):
    try:
        return datetime.strptime(value[:10], "%Y-%m-%d").date() if value else None
    except (TypeError, ValueError):
        return None

def parse_time(value):
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")) if value else None
    except (TypeError, ValueError):
        return None

def activity_state(value):
    day = parse_day(value)
    if not day:
        return None
    age = (TODAY - day).days
    if age <= 90:
        return "active"
    if age <= 365:
        return "recent"
    if age <= 730:
        return "quiet"
    return "dormant"

def interval_days(last_activity, archived=False):
    if archived:
        return 56
    day = parse_day(last_activity)
    if not day:
        return 14
    age = max(0, (TODAY - day).days)
    if age <= 14:
        return 1
    if age <= 60:
        return 3
    if age <= 180:
        return 7
    if age <= 730:
        return 14
    return 30

def probe_interval_minutes(last_activity, archived=False):
    if archived:
        return 720
    day = parse_day(last_activity)
    if not day:
        return 720
    age = max(0, (TODAY - day).days)
    if age <= 14:
        return 15
    if age <= 60:
        return 60
    if age <= 180:
        return 240
    return 720

def probe_due(repo, rs, interval):
    """Spread the first migration pass across slots, then honour actual elapsed time."""
    next_due = parse_time(rs.get("next_probe_due_at"))
    if next_due:
        return RUN_AT >= next_due
    last = parse_time(rs.get("last_probe_at"))
    if not last:
        last_day = parse_day(rs.get("last_probe"))
        last = datetime.combine(last_day, datetime.min.time(), timezone.utc) if last_day else None
    if not last:
        return True
    slots = max(1, interval // 15)
    # A one-time transition from the old whole-catalogue schedule. Every repo
    # is first revisited within its maximum interval, with stable stagger.
    first_offset = min(interval, 15 * (1 + bucket(repo, slots)))
    return RUN_AT >= last + timedelta(minutes=first_offset)

def bucket(repo, interval):
    digest = hashlib.sha256(repo.encode("utf-8")).digest()
    return int.from_bytes(digest[:4], "big") % interval

def scheduled_today(repo, interval):
    return interval <= 1 or TODAY.toordinal() % interval == bucket(repo, interval)

def probe_order(repositories, state):
    """Oldest/never-probed repositories go first so budget limits are fair."""
    repo_state = state.get("repositories", {})
    def key(repo):
        rs = repo_state.get(repo, {})
        last = rs.get("last_probe_at") or rs.get("last_probe") or ""
        return (last, repo.casefold())
    return sorted(repositories, key=key)

def api(path, *, etag=None, allow_404=False, allow_empty_repo=False):
    global REQUESTS, NOT_MODIFIED, CONDITIONAL_REQUESTS
    if REQUESTS >= MAX_HTTP_REQUESTS:
        raise RateStop(f"HTTP safety cap reached ({MAX_HTTP_REQUESTS})")
    # A conditional request only saves quota when it actually returns 304.
    # Repository probes have returned 200 in every sampled production run.
    if not primary_available():
        raise PrimaryReserve(
            f"primary rate reserve reached ({RATE_REMAINING} remaining; reserve {effective_reserve()})"
        )

    REQUESTS += 1
    if etag:
        CONDITIONAL_REQUESTS += 1
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "legacy-reverse-engineering-tracker",
        "X-GitHub-Api-Version": "2026-03-10",
    }
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    if etag:
        headers["If-None-Match"] = etag

    try:
        with urlopen(Request(API + path, headers=headers), timeout=30) as response:
            response_headers = dict(response.headers)
            update_rate(response_headers)
            STATUS_COUNTS[response.status] = STATUS_COUNTS.get(response.status, 0) + 1
            body = json.load(response)
            time.sleep(REQUEST_DELAY)
            return response.status, body, response_headers
    except HTTPError as exc:
        response_headers = dict(exc.headers) if exc.headers else {}
        update_rate(response_headers)
        STATUS_COUNTS[exc.code] = STATUS_COUNTS.get(exc.code, 0) + 1
        if exc.code == 304:
            NOT_MODIFIED += 1
            time.sleep(REQUEST_DELAY)
            return 304, None, response_headers

        body = exc.read().decode("utf-8", "replace")
        time.sleep(REQUEST_DELAY)
        if allow_404 and exc.code == 404:
            return 404, None, response_headers
        if allow_empty_repo and exc.code == 409:
            return 409, None, response_headers
        if exc.code in (403, 429) and (
            "rate limit" in body.lower() or "secondary" in body.lower()
        ):
            raise RateStop(f"GitHub rate limit response {exc.code}: {body[:180]}")
        raise RuntimeError(f"GitHub API {exc.code} for {path}: {body[:300]}") from exc

def get_json(path, **kwargs):
    status, body, headers = api(path, **kwargs)
    return body, headers, status

def update_ai_config(projects, root_entries, github_entries):
    root_names = {e.get("name", "").lower() for e in root_entries if isinstance(e, dict)}
    gh_names = {e.get("name", "").lower() for e in github_entries if isinstance(e, dict)}
    for record in projects:
        ai = record.setdefault("ai", {"usage": None, "tools": []})
        tools = set(ai.get("tools") or [])
        evidence = list(ai.get("evidence") or [])
        for filename, tool in AI_CONFIG.items():
            if filename in root_names:
                tools.add(tool)
                phrase = f"{tool} project instructions/configuration present"
                if phrase not in evidence:
                    evidence.append(phrase)
        if "copilot-instructions.md" in gh_names:
            tools.add("GitHub Copilot")
            phrase = ".github/copilot-instructions.md present"
            if phrase not in evidence:
                evidence.append(phrase)
        if tools:
            ai["usage"] = True
            ai["tools"] = sorted(tools)
            ai["evidence"] = evidence

def update_basic_info(repo, info, repo_projects):
    branch = info.get("default_branch") or "main"
    for record in repo_projects:
        gh = record.setdefault("github", {})
        gh.update({
            "repository": repo,
            "created_at": iso_date(info.get("created_at")),
            "pushed_at": iso_date(info.get("pushed_at")),
            "updated_at": iso_date(info.get("updated_at")),
            "checked_at": TODAY.isoformat(),
            "default_branch": branch,
            "tracking_branch": record.get("github_branch") or branch,
            "tracking_path": record.get("github_path"),
            "archived": bool(info.get("archived")),
            "fork": bool(info.get("fork")),
            "primary_language": info.get("language"),
            "activity_state": activity_state(record.get("last_activity")),
        })

def update_latest_release(repo_projects, release):
    for record in repo_projects:
        if record.get("github_path"):
            continue
        gh = record.setdefault("github", {})
        if release:
            gh["latest_release"] = {
                "tag": release.get("tag_name"),
                "name": release.get("name"),
                "published_at": iso_date(release.get("published_at")),
                "url": release.get("html_url"),
            }
        else:
            gh.pop("latest_release", None)

def check_latest_release(repo, repo_projects):
    release, _, _ = get_json(f"/repos/{repo}/releases/latest", allow_404=True)
    update_latest_release(repo_projects, release)

def enrich_changed_repo(repo, info, repo_projects):
    branch = info.get("default_branch") or "main"
    languages, _, _ = get_json(f"/repos/{repo}/languages")
    root_entries, _, _ = get_json(f"/repos/{repo}/contents?ref={quote(branch)}", allow_404=True)
    root_entries = root_entries or []
    github_entries = []
    if any(isinstance(e, dict) and e.get("name") == ".github" and e.get("type") == "dir" for e in root_entries):
        github_entries, _, _ = get_json(
            f"/repos/{repo}/contents/.github?ref={quote(branch)}", allow_404=True
        )
        github_entries = github_entries or []

    update_ai_config(repo_projects, root_entries, github_entries)

    if any(not p.get("github_path") for p in repo_projects):
        check_latest_release(repo, repo_projects)

    ordered_languages = [
        name for name, _ in sorted((languages or {}).items(), key=lambda item: item[1], reverse=True)
    ]
    for record in repo_projects:
        gh = record.setdefault("github", {})
        gh["languages"] = ordered_languages
    return not bool(languages)


def fill_missing_latest_commits(repos, state, request=get_json):
    """Fetch one historical commit per tracked branch/path missing a latest date.

    The rolling activity collector intentionally fetches only 180 days. A
    repository older than that still needs its most recent upstream date for
    the project record and the addition card, without adding an old commit to
    the current activity timeline.
    """
    groups = {}
    for repo, projects in repos.items():
        rs = state["repositories"].get(repo) or {}
        for project in projects:
            if (project.get("github") or {}).get("latest_commit"):
                continue
            branch = (project.get("github_branch") or (project.get("github") or {}).get("tracking_branch")
                      or rs.get("default_branch") or "main")
            groups.setdefault((repo, branch, project.get("github_path") or ""), []).append(project)

    found = unavailable = checked = 0
    for (repo, branch, path), projects in sorted(groups.items()):
        rs = state["repositories"][repo]
        key = json.dumps([branch, path], separators=(",", ":"))
        empty_checks = rs.setdefault("empty_commit_lookups", {})
        prior = empty_checks.get(key) or {}
        prior_day = parse_day(prior.get("checked_at"))
        if (prior_day and TODAY - prior_day < timedelta(days=30)
                and prior.get("pushed_at") == rs.get("last_seen_pushed_at")):
            for project in projects:
                project.setdefault("github", {})["latest_commit_lookup"] = "unavailable"
            continue

        params = {"sha": branch, "per_page": 1}
        if path:
            params["path"] = path
        try:
            items, _, status = request(f"/repos/{repo}/commits?{urlencode(params)}",
                                       allow_404=True, allow_empty_repo=True)
        except RateStop as exc:
            print(f"RATE STOP during latest-commit lookup: {exc}", file=sys.stderr)
            break
        except Exception as exc:
            print(f"WARNING: latest commit {repo} {branch} {path}: {exc}", file=sys.stderr)
            continue
        checked += 1
        item = items[0] if isinstance(items, list) and items else None
        commit = (item or {}).get("commit") or {}
        when = (commit.get("committer") or {}).get("date") or (commit.get("author") or {}).get("date")
        if not item or not when or not item.get("sha"):
            empty_checks[key] = {"checked_at": TODAY.isoformat(),
                                 "pushed_at": rs.get("last_seen_pushed_at")}
            for project in projects:
                project.setdefault("github", {})["latest_commit_lookup"] = "unavailable"
            unavailable += len(projects)
            continue

        empty_checks.pop(key, None)
        day = iso_date(when)
        for project in projects:
            gh = project.setdefault("github", {})
            gh["latest_commit"] = {
                "sha": item["sha"], "date": day,
                "message": (commit.get("message") or "").splitlines()[0],
                "url": item.get("html_url"),
            }
            gh.pop("latest_commit_lookup", None)
            if not parse_day(project.get("last_activity")) or parse_day(project["last_activity"]) < parse_day(day):
                project["last_activity"] = day
            gh["activity_state"] = activity_state(project["last_activity"])
            found += 1
    return checked, found, unavailable

def main():
    records = json.loads(PROJECTS.read_text(encoding="utf-8"))
    state = load_state()
    repos = {}
    for record in records:
        repo = github_repo(record.get("repo"))
        if repo:
            repos.setdefault(repo, []).append(record)

    probed = changed_count = requested = skipped = 0
    stopped = None
    bootstrap_state = not bool(state["repositories"])

    for repo in probe_order(repos, state):
        repo_projects = repos[repo]
        project_ids = sorted(p["id"] for p in repo_projects if p.get("id"))
        new_repo = repo not in state["repositories"]
        rs = state["repositories"].setdefault(repo, {})
        rs.setdefault("first_seen_at", RUN_AT.isoformat(timespec="seconds").replace("+00:00", "Z"))
        if new_repo and not bootstrap_state:
            rs["scan_requested"] = True
            rs["scan_reason"] = "new"

        previous_project_ids = rs.get("project_ids")
        added_projects = []
        rs["project_ids"] = project_ids
        if previous_project_ids is not None:
            added_projects = sorted(set(project_ids) - set(previous_project_ids))
            if added_projects:
                rs["scan_requested"] = True
                if rs.get("scan_reason") != "changed":
                    rs["scan_reason"] = "new-project"
        latest = max(
            (parse_day(p.get("last_activity")) for p in repo_projects if parse_day(p.get("last_activity"))),
            default=None,
        )
        latest_day = latest.isoformat() if latest else None
        archived = bool(next((p.get("github", {}).get("archived") for p in repo_projects if p.get("github")), False))
        probe_minutes = probe_interval_minutes(latest_day, archived)
        rs["probe_interval_minutes"] = probe_minutes
        if not (FORCE_FULL_PROBE or new_repo or added_projects or probe_due(repo, rs, probe_minutes)):
            skipped += 1
            continue
        prior_pushed = rs.get("last_seen_pushed_at")
        if not prior_pushed:
            prior_pushed = next(
                (p.get("github", {}).get("pushed_at") for p in repo_projects if p.get("github", {}).get("pushed_at")),
                None,
            )

        try:
            info, headers, status = get_json(f"/repos/{repo}", etag=rs.get("etag"))
        except RateStop as exc:
            stopped = str(exc)
            print(f"RATE STOP before {repo}: {exc}", file=sys.stderr)
            break
        except Exception as exc:
            rs["last_error"] = str(exc)[:400]
            rs["last_probe"] = TODAY.isoformat()
            rs["last_probe_at"] = RUN_AT.isoformat(timespec="seconds").replace("+00:00", "Z")
            rs["next_probe_due_at"] = (RUN_AT + timedelta(minutes=probe_minutes)).isoformat(timespec="seconds").replace("+00:00", "Z")
            print(f"WARNING: probe {repo}: {exc}", file=sys.stderr)
            continue

        probed += 1
        rs["last_probe"] = TODAY.isoformat()
        rs["last_probe_at"] = RUN_AT.isoformat(timespec="seconds").replace("+00:00", "Z")
        rs["next_probe_due_at"] = (RUN_AT + timedelta(minutes=probe_minutes)).isoformat(timespec="seconds").replace("+00:00", "Z")
        rs.pop("last_error", None)
        if headers.get("ETag"):
            rs["etag"] = headers["ETag"]

        info_changed = status == 200
        pushed_changed = False
        default_branch = next((p.get("github", {}).get("default_branch") for p in repo_projects if p.get("github")), "main")
        enriched = False

        if info_changed and info:
            current_pushed = info.get("pushed_at")
            if prior_pushed and current_pushed:
                pushed_changed = (
                    current_pushed != prior_pushed
                    if "T" in str(prior_pushed)
                    else iso_date(current_pushed) != iso_date(prior_pushed)
                )
            rs["last_seen_pushed_at"] = current_pushed
            rs["last_repo_updated_at"] = info.get("updated_at")
            archived = bool(info.get("archived"))
            default_branch = info.get("default_branch") or "main"
            update_basic_info(repo, info, repo_projects)
            if pushed_changed:
                rs["last_change_detected"] = TODAY.isoformat()
                rs["last_change_detected_at"] = RUN_AT.isoformat(timespec="seconds").replace("+00:00", "Z")
                changed_count += 1
            empty_checked = parse_day(rs.get("empty_languages_checked_at"))
            retry_empty = not empty_checked or TODAY - empty_checked >= timedelta(days=30)
            missing_heavy = any(not p.get("github", {}).get("languages") for p in repo_projects) and (
                new_repo or bool(added_projects) or retry_empty
            )
            if pushed_changed or missing_heavy:
                try:
                    empty_languages = enrich_changed_repo(repo, info, repo_projects)
                    enriched = True
                    if empty_languages:
                        rs["empty_languages_checked_at"] = TODAY.isoformat()
                    else:
                        rs.pop("empty_languages_checked_at", None)
                    if any(not p.get("github_path") for p in repo_projects):
                        rs["last_release_check_at"] = RUN_AT.isoformat(timespec="seconds").replace("+00:00", "Z")
                except PrimaryReserve as exc:
                    print(f"RATE RESERVE: skipping optional metadata for {repo}: {exc}", file=sys.stderr)
                except RateStop as exc:
                    stopped = str(exc)
                    print(f"RATE STOP while enriching {repo}: {exc}", file=sys.stderr)
                except Exception as exc:
                    print(f"WARNING: metadata {repo}: {exc}", file=sys.stderr)

        if not enriched and any(not p.get("github_path") for p in repo_projects):
            checked = parse_time(rs.get("last_release_check_at"))
            release_hours = 6 if probe_minutes == 15 else 24
            if not checked or RUN_AT - checked >= timedelta(hours=release_hours):
                try:
                    check_latest_release(repo, repo_projects)
                    rs["last_release_check_at"] = RUN_AT.isoformat(timespec="seconds").replace("+00:00", "Z")
                except PrimaryReserve as exc:
                    print(f"RATE RESERVE: skipping release for {repo}: {exc}", file=sys.stderr)
                except RateStop as exc:
                    stopped = str(exc)
                    print(f"RATE STOP while checking release for {repo}: {exc}", file=sys.stderr)
                except Exception as exc:
                    print(f"WARNING: release {repo}: {exc}", file=sys.stderr)

        interval = interval_days(latest.isoformat() if latest else None, archived)
        rs["probe_interval_minutes"] = probe_interval_minutes(latest_day, archived)
        rs["next_probe_due_at"] = (RUN_AT + timedelta(minutes=rs["probe_interval_minutes"])).isoformat(timespec="seconds").replace("+00:00", "Z")
        rs["interval_days"] = interval
        rs["default_branch"] = default_branch
        due = scheduled_today(repo, interval)
        last_deep_scan = rs.get("last_deep_scan") or ""
        already_scanned = last_deep_scan[:10] == TODAY.isoformat()
        should_queue = pushed_changed or ((due or rs.get("scan_requested")) and not already_scanned)
        if should_queue:
            if not rs.get("scan_requested"):
                requested += 1
            rs["scan_requested"] = True
            rs["scan_reason"] = "changed" if pushed_changed else rs.get("scan_reason", "scheduled")

        if stopped:
            break

    history_checked, history_found, history_unavailable = fill_missing_latest_commits(repos, state)
    snapshot = rate_snapshot()
    snapshot.update({"probed": probed, "skipped_not_due": skipped})
    rate_state = state.setdefault("rate", {})
    rate_state["probe"] = snapshot
    rate_state["probe_history"] = (rate_state.get("probe_history") or [])[-95:] + [snapshot]
    save_state(state)
    append_summary("GitHub repository probe phase")
    records.sort(key=lambda r: ((r.get("title") or "").casefold(), r.get("id") or ""))
    PROJECTS.write_text(json.dumps(records, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(
        f"Probed {probed}/{len(repos)} repositories ({skipped} deferred by cadence); "
        f"detected {changed_count} pushed changes; "
        f"requested {requested} deep scans; made {REQUESTS} HTTP requests "
        f"({NOT_MODIFIED} returned 304); checked {history_checked} missing historical heads "
        f"({history_found} project dates found, {history_unavailable} unavailable); primary remaining "
        f"{RATE_REMAINING if RATE_REMAINING is not None else '?'}/"
        f"{RATE_LIMIT if RATE_LIMIT is not None else '?'}; reserve {effective_reserve()}."
    )
    if stopped:
        print(f"Stopped early to preserve API quota: {stopped}")

if __name__ == "__main__":
    main()
