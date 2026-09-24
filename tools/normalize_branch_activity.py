#!/usr/bin/env python3
"""Remove commit activity attributed to the wrong repository branch.

Root project records track their repository's default branch. Records with an
explicit ``github_branch`` track that branch instead. The activity collector
scans every branch to support branch-specific projects, so this post-pass keeps
final activity/project metadata aligned with each record's tracking branch.
"""
from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = ROOT / "data" / "projects.json"
ACTIVITY = ROOT / "data" / "activity.json"
API = "https://api.github.com"
TOKEN = os.environ.get("GITHUB_TOKEN", "")

# These three records were cleared by the first normalizer run before remote
# branch-tip fallback existed. They repair themselves once, then drop out of
# this set because latest_commit is present again.
LEGACY_REPAIRS = {
    "elite-bbc-master-moxon",
    "elite-bbc-micro-disc-moxon",
    "jsbeeb-mcp-kieranhj",
}


def parse_time(value):
    if not value:
        return None
    try:
        if len(value) == 10:
            return datetime.fromisoformat(value + "T00:00:00+00:00")
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (TypeError, ValueError):
        return None


def tracking_branch(project):
    explicit = project.get("github_branch")
    if explicit:
        return explicit
    return (project.get("github") or {}).get("default_branch")


def activity_state(value):
    day = parse_time(value)
    if not day:
        return None
    age = (datetime.now(timezone.utc).date() - day.date()).days
    if age <= 90:
        return "active"
    if age <= 365:
        return "recent"
    if age <= 730:
        return "quiet"
    return "dormant"


def remote_latest(project):
    gh = project.get("github") or {}
    repo = gh.get("repository")
    branch = tracking_branch(project)
    if not repo or not branch:
        return None

    params = {"sha": branch, "per_page": 1}
    if project.get("github_path"):
        params["path"] = project["github_path"]
    url = f"{API}/repos/{repo}/commits?{urlencode(params)}"
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "legacy-reverse-engineering-tracker",
        "X-GitHub-Api-Version": "2026-03-10",
    }
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    with urlopen(Request(url, headers=headers), timeout=30) as response:
        items = json.load(response)
    if not items:
        return None

    item = items[0]
    commit = item.get("commit") or {}
    when = (commit.get("committer") or {}).get("date") or (commit.get("author") or {}).get("date")
    if not when:
        return None
    message = commit.get("message") or ""
    return {
        "date": when,
        "sha": item.get("sha"),
        "message": message,
        "title": message.splitlines()[0] if message else "",
        "url": item.get("html_url"),
    }


def apply_latest(project, event):
    day = event["date"][:10]
    project["last_activity"] = day
    gh = project.setdefault("github", {})
    gh["latest_commit"] = {
        "sha": event.get("sha"),
        "date": day,
        "message": (event.get("message") or event.get("title") or "").splitlines()[0],
        "url": event.get("url"),
    }
    gh["activity_state"] = activity_state(day)


def main():
    projects = json.loads(PROJECTS.read_text(encoding="utf-8"))
    payload = json.loads(ACTIVITY.read_text(encoding="utf-8"))
    by_id = {p.get("id"): p for p in projects if p.get("id")}

    kept = []
    removed = 0
    narrowed = 0
    stale_latest = set()

    for event in payload.get("events", []):
        if event.get("type") != "commit":
            kept.append(event)
            continue

        project = by_id.get(event.get("project_id"))
        expected = tracking_branch(project or {})
        branches = sorted(set(event.get("branches") or []))
        if not project or not expected or not branches:
            kept.append(event)
            continue

        matching = [branch for branch in branches if branch == expected]
        if not matching:
            latest = (project.get("github") or {}).get("latest_commit") or {}
            if latest.get("sha") == event.get("sha"):
                stale_latest.add(project["id"])
            removed += 1
            continue

        if matching != branches:
            event["branches"] = matching
            narrowed += 1
        kept.append(event)

    forced = {
        project_id
        for project_id in LEGACY_REPAIRS
        if project_id in by_id and not ((by_id[project_id].get("github") or {}).get("latest_commit"))
    }
    repair_ids = stale_latest | forced

    newest = {}
    for event in kept:
        if event.get("type") != "commit":
            continue
        project_id = event.get("project_id")
        if project_id not in repair_ids:
            continue
        when = parse_time(event.get("date"))
        if not when:
            continue
        old = newest.get(project_id)
        if old is None or when > parse_time(old.get("date")):
            newest[project_id] = event

    repaired = 0
    cleared = 0
    remote_repairs = 0
    for project_id in repair_ids:
        project = by_id[project_id]
        event = None
        try:
            event = remote_latest(project)
            if event:
                remote_repairs += 1
        except Exception as exc:
            print(f"WARNING: branch-tip repair {project_id}: {exc}")
        if event is None:
            event = newest.get(project_id)

        if event:
            apply_latest(project, event)
            repaired += 1
        else:
            # The retained activity window contains no commit on the branch this
            # record actually tracks, and the remote tip could not be resolved.
            # Unknown is preferable to retaining a demonstrably wrong commit.
            project["last_activity"] = None
            gh = project.setdefault("github", {})
            gh.pop("latest_commit", None)
            gh["activity_state"] = None
            cleared += 1

    if removed or narrowed or repaired or cleared:
        payload["events"] = kept
        ACTIVITY.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        projects.sort(key=lambda p: ((p.get("title") or "").casefold(), p.get("id") or ""))
        PROJECTS.write_text(json.dumps(projects, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(
        f"Branch attribution normalization: removed {removed} events, narrowed {narrowed}, "
        f"repaired {repaired} latest commits ({remote_repairs} from branch tips), "
        f"cleared {cleared} unresolved latest commits."
    )


if __name__ == "__main__":
    main()
