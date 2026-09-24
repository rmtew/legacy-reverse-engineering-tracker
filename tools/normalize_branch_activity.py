#!/usr/bin/env python3
"""Remove commit activity attributed to the wrong repository branch.

Root project records track their repository's default branch. Records with an
explicit ``github_branch`` track that branch instead. The activity collector
scans every branch to support branch-specific projects, so this post-pass keeps
final activity/project metadata aligned with each record's tracking branch.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = ROOT / "data" / "projects.json"
ACTIVITY = ROOT / "data" / "activity.json"


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

    newest = {}
    for event in kept:
        if event.get("type") != "commit":
            continue
        project_id = event.get("project_id")
        if project_id not in stale_latest:
            continue
        when = parse_time(event.get("date"))
        if not when:
            continue
        old = newest.get(project_id)
        if old is None or when > parse_time(old.get("date")):
            newest[project_id] = event

    repaired = 0
    cleared = 0
    for project_id in stale_latest:
        project = by_id[project_id]
        gh = project.setdefault("github", {})
        event = newest.get(project_id)
        if event:
            day = event["date"][:10]
            project["last_activity"] = day
            gh["latest_commit"] = {
                "sha": event.get("sha"),
                "date": day,
                "message": (event.get("message") or event.get("title") or "").splitlines()[0],
                "url": event.get("url"),
            }
            gh["activity_state"] = activity_state(day)
            repaired += 1
        else:
            # The retained activity window contains no commit on the branch this
            # record actually tracks. Unknown is preferable to retaining a
            # demonstrably wrong commit from another branch.
            project["last_activity"] = None
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
        f"repaired {repaired} latest commits, cleared {cleared} unresolved latest commits."
    )


if __name__ == "__main__":
    main()
