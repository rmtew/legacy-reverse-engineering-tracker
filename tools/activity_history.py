"""Compact older commit detail while retaining identities for incremental scans."""

import json
from copy import deepcopy
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo


DETAIL_DAYS = 14
LOCAL_ZONE = ZoneInfo("Pacific/Auckland")


def write_activity(path, payload):
    """Write valid JSON with one event per line for useful Git history diffs."""
    event_lines = ["    " + json.dumps(event, ensure_ascii=False, separators=(",", ":"))
                   for event in payload["events"]]
    header = ("{\n  \"generated_at\": " + json.dumps(payload["generated_at"]) +
              ",\n  \"window_days\": " + str(payload["window_days"]) + ",\n  \"events\": [\n")
    path.write_text(header + ",\n".join(event_lines) + "\n  ]\n}\n", encoding="utf-8")


def parse_time(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def local_day(value):
    return parse_time(value).astimezone(LOCAL_ZONE).date().isoformat()


def compact_history(events, now):
    """Return newest-first events, merging old commits into project/day summaries.

    SHA identities remain in the summary so a later backfill or overlapping scan
    cannot count a previously observed commit twice.
    """
    cutoff = now - timedelta(days=DETAIL_DAYS)
    summaries = {}
    detailed = []
    for event in events:
        if event.get("type") not in ("commit", "daily_commits"):
            detailed.append(event)
            continue
        if event["type"] == "commit" and parse_time(event["date"]) >= cutoff:
            detailed.append(event)
            continue
        key = (event["project_id"], event.get("repository"),
               event.get("day") or local_day(event["date"]))
        summary = summaries.setdefault(key, {
            "type": "daily_commits", "date": event["date"], "day": key[2],
            "project_id": key[0], "repository": key[1], "shas": set(),
            "latest_title": event.get("latest_title") or event.get("title"),
            "latest_url": event.get("latest_url") or event.get("url"),
        })
        summary["shas"].update(event.get("shas") or [event.get("sha")])
        if event["date"] > summary["date"]:
            summary["date"] = event["date"]
            summary["latest_title"] = event.get("latest_title") or event.get("title")
            summary["latest_url"] = event.get("latest_url") or event.get("url")
    for summary in summaries.values():
        summary["shas"] = sorted(sha for sha in summary["shas"] if sha)
        summary["count"] = len(summary["shas"])
        detailed.append(summary)
    return sorted(detailed, key=lambda event: (
        event.get("date") or "", event.get("repository") or "",
        event.get("sha") or "", event.get("type") or "",
        event.get("project_id") or "",
    ), reverse=True)


def freeze_addition_context(events, projects, repositories, now):
    """Capture upstream facts once the first post-addition scan has completed."""
    by_id = {project["id"]: project for project in projects}
    recent_cutoff = now - timedelta(days=90)
    counts, days = {}, {}
    for event in events:
        if event["type"] not in ("commit", "daily_commits") or parse_time(event["date"]) < recent_cutoff:
            continue
        project_id = event["project_id"]
        counts[project_id] = counts.get(project_id, 0) + (event.get("count", 1) if event["type"] == "daily_commits" else 1)
        days.setdefault(project_id, set()).add(event.get("day") or local_day(event["date"]))
    for event in events:
        if event.get("type") not in ("project_added", "project_restored"):
            continue
        project = by_id.get(event["project_id"])
        if not project:
            continue
        github = project.get("github") or {}
        if "activity_context" in event:
            context = event["activity_context"]
            # A 180-day scan may have completed before the older repository's
            # true latest commit was looked up. Fill only previously unknown
            # fields; keep the original 90-day counts and known dates frozen.
            if not context.get("last_commit") and github.get("latest_commit"):
                context["last_commit"] = deepcopy(github["latest_commit"])
                context["last_activity"] = project.get("last_activity")
                context.pop("last_commit_lookup", None)
            if not context.get("latest_release") and github.get("latest_release"):
                context["latest_release"] = deepcopy(github["latest_release"])
            if not context.get("last_commit") and github.get("latest_commit_lookup") == "unavailable":
                context["last_commit_lookup"] = "unavailable"
            continue
        repository = (project.get("github") or {}).get("repository") if project else None
        state = repositories.get(repository) or {}
        scanned_at = state.get("last_deep_scan") if repository else None
        if not project or not scanned_at:
            continue
        if parse_time(scanned_at) < parse_time(event["date"]):
            scanned_ids = state.get("last_deep_scan_project_ids") or []
            # One-time migration for additions recorded just after their scan,
            # before the collector began recording scanned project IDs.
            legacy_same_run = (event["date"] <= "2026-09-25T21:57:35Z"
                               and event["project_id"] in (state.get("project_ids") or [])
                               and parse_time(event["date"]) - parse_time(scanned_at) <= timedelta(minutes=10))
            if event["project_id"] not in scanned_ids and not legacy_same_run:
                continue
        event["activity_context"] = {
            "as_of": now.isoformat(timespec="seconds").replace("+00:00", "Z"),
            "last_commit": deepcopy(github.get("latest_commit")),
            "last_activity": project.get("last_activity"),
            "latest_release": deepcopy(github.get("latest_release")),
            "last_commit_lookup": github.get("latest_commit_lookup"),
            "commits_90d": counts.get(project["id"], 0),
            "active_days_90d": len(days.get(project["id"], ())),
        }
