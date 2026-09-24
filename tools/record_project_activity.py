#!/usr/bin/env python3
"""Record meaningful catalogue changes as persisted activity events.

The state file is a compact material snapshot of the canonical catalogue. It is
used only to identify changes between maintenance runs; volatile GitHub refresh
metadata is intentionally excluded so routine probes do not become activity.
"""
from __future__ import annotations

import json
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = ROOT / "data" / "projects.json"
ACTIVITY = ROOT / "data" / "activity.json"
STATE = ROOT / "state" / "project-catalog-state.json"

DAYS = 180
NOW = datetime.now(timezone.utc)
NOW_ISO = NOW.isoformat(timespec="seconds").replace("+00:00", "Z")
CUTOFF = NOW - timedelta(days=DAYS)

MATERIAL_FIELDS = (
    "title",
    "upstream_name",
    "display_title",
    "subjects",
    "repo",
    "project_url",
    "github_path",
    "github_branch",
    "source_platforms",
    "target_platforms",
    "source_cpu",
    "target_cpu",
    "runtime_profiles",
    "source_language",
    "reconstructed_languages",
    "record_class",
    "target_kinds",
    "work_kinds",
    "tool_kinds",
    "types",
    "re_started",
    "status",
    "build",
    "techniques",
    "tags",
    "notes",
)
MOVE_FIELDS = {"repo", "project_url", "github_path", "github_branch"}

# Co-author trailers/config files are handled by the GitHub collectors. These
# patterns cover unusually explicit human commit subjects such as
# "Claude fixed vector display!" without treating a bare tool-name mention as
# evidence of use.
EXPLICIT_AI_PATTERNS = (
    (
        "Claude",
        re.compile(
            r"^(?:claude)\b.*\b(?:fix(?:ed)?|implement(?:ed)?|generat(?:ed|e)|wrote|write|add(?:ed)?|creat(?:ed|e)|refactor(?:ed)?|help(?:ed)?|assist(?:ed)?|port(?:ed)?|convert(?:ed)?)\b"
            r"|\b(?:fix(?:ed)?|implement(?:ed)?|generat(?:ed|e)|wrote|write|add(?:ed)?|creat(?:ed|e)|refactor(?:ed)?|help(?:ed)?|assist(?:ed)?|port(?:ed)?|convert(?:ed)?)\b.*\bby\s+claude\b"
            r"|\b(?:with|using|via)\s+claude\b",
            re.I,
        ),
    ),
    (
        "ChatGPT",
        re.compile(
            r"^(?:chatgpt)\b.*\b(?:fix(?:ed)?|implement(?:ed)?|generat(?:ed|e)|wrote|write|add(?:ed)?|creat(?:ed|e)|refactor(?:ed)?|help(?:ed)?|assist(?:ed)?)\b"
            r"|\b(?:fix(?:ed)?|implement(?:ed)?|generat(?:ed|e)|wrote|write|add(?:ed)?|creat(?:ed|e)|refactor(?:ed)?|help(?:ed)?|assist(?:ed)?)\b.*\bby\s+chatgpt\b"
            r"|\b(?:with|using|via)\s+chatgpt\b",
            re.I,
        ),
    ),
    (
        "OpenAI Codex",
        re.compile(
            r"^(?:codex|openai codex)\b.*\b(?:fix(?:ed)?|implement(?:ed)?|generat(?:ed|e)|wrote|write|add(?:ed)?|creat(?:ed|e)|refactor(?:ed)?|help(?:ed)?|assist(?:ed)?)\b"
            r"|\b(?:fix(?:ed)?|implement(?:ed)?|generat(?:ed|e)|wrote|write|add(?:ed)?|creat(?:ed|e)|refactor(?:ed)?|help(?:ed)?|assist(?:ed)?)\b.*\bby\s+(?:codex|openai codex)\b"
            r"|\b(?:with|using|via)\s+(?:codex|openai codex)\b",
            re.I,
        ),
    ),
    (
        "GitHub Copilot",
        re.compile(
            r"^(?:github copilot|copilot)\b.*\b(?:fix(?:ed)?|implement(?:ed)?|generat(?:ed|e)|wrote|write|add(?:ed)?|creat(?:ed|e)|refactor(?:ed)?|help(?:ed)?|assist(?:ed)?)\b"
            r"|\b(?:fix(?:ed)?|implement(?:ed)?|generat(?:ed|e)|wrote|write|add(?:ed)?|creat(?:ed|e)|refactor(?:ed)?|help(?:ed)?|assist(?:ed)?)\b.*\bby\s+(?:github copilot|copilot)\b"
            r"|\b(?:with|using|via)\s+(?:github copilot|copilot)\b",
            re.I,
        ),
    ),
    (
        "Gemini",
        re.compile(
            r"^(?:gemini)\b.*\b(?:fix(?:ed)?|implement(?:ed)?|generat(?:ed|e)|wrote|write|add(?:ed)?|creat(?:ed|e)|refactor(?:ed)?|help(?:ed)?|assist(?:ed)?)\b"
            r"|\b(?:fix(?:ed)?|implement(?:ed)?|generat(?:ed|e)|wrote|write|add(?:ed)?|creat(?:ed|e)|refactor(?:ed)?|help(?:ed)?|assist(?:ed)?)\b.*\bby\s+gemini\b"
            r"|\b(?:with|using|via)\s+gemini\b",
            re.I,
        ),
    ),
)


def parse_time(value):
    if not value:
        return None
    try:
        return datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except ValueError:
        return None


def compact_ai(value):
    value = value or {}
    return {
        "usage": value.get("usage"),
        "tools": value.get("tools") or [],
    }


def enrich_explicit_ai(projects, activity):
    by_id = {project.get("id"): project for project in projects if project.get("id")}
    enriched = 0
    for event in activity.get("events", []):
        if event.get("type") != "commit":
            continue
        when = parse_time(event.get("date"))
        if when and when < CUTOFF:
            continue
        project = by_id.get(event.get("project_id"))
        if not project:
            continue
        subject = (event.get("title") or (event.get("message") or "").splitlines()[0]).strip()
        if not subject:
            continue
        for tool, pattern in EXPLICIT_AI_PATTERNS:
            if not pattern.search(subject):
                continue
            ai = project.setdefault("ai", {"usage": None, "tools": []})
            tools = set(ai.get("tools") or [])
            evidence = list(ai.get("evidence") or [])
            sha = (event.get("sha") or "")[:12]
            marker = f"Explicit {tool} involvement in tracked commit {sha}"
            if not any(str(item).startswith(marker) for item in evidence):
                evidence.append(f'{marker}: "{subject[:180]}"')
            before = (ai.get("usage"), tuple(ai.get("tools") or []))
            tools.add(tool)
            ai["usage"] = True
            ai["tools"] = sorted(tools)
            ai["evidence"] = evidence
            after = (ai.get("usage"), tuple(ai.get("tools") or []))
            if after != before:
                enriched += 1
            break
    return enriched


def snapshot(project):
    out = {"id": project["id"]}
    for field in MATERIAL_FIELDS:
        value = project.get(field)
        out[field] = value
    out["ai"] = compact_ai(project.get("ai"))
    return out


def changed_fields(before, after):
    keys = set(before) | set(after)
    keys.discard("id")
    return sorted(key for key in keys if before.get(key) != after.get(key))


def display_value(value):
    if isinstance(value, list):
        return ", ".join(str(item) for item in value) or "none"
    if isinstance(value, dict):
        return json.dumps(value, sort_keys=True, ensure_ascii=False)
    if value is None or value == "":
        return "unknown"
    return str(value)


def change_message(before, after, fields):
    pieces = []
    for field in fields[:4]:
        pieces.append(
            f"{field.replace('_', ' ')}: {display_value(before.get(field))} → {display_value(after.get(field))}"
        )
    if len(fields) > 4:
        pieces.append(f"+{len(fields) - 4} more field{'s' if len(fields) - 4 != 1 else ''}")
    return "; ".join(pieces)


def project_url(project):
    return project.get("project_url") or project.get("repo")


def change_details(before, after, fields):
    return [
        {
            "field": field,
            "before": before.get(field),
            "after": after.get(field),
        }
        for field in fields
    ]


def make_event(
    event_type,
    project_id,
    project,
    title,
    message="",
    changes=None,
    details=None,
):
    return {
        "type": event_type,
        "date": NOW_ISO,
        "project_id": project_id,
        "project": project,
        "title": title,
        "message": message,
        "url": project_url(project),
        "changes": changes or [],
        "change_details": details or [],
        "branches": [],
    }


def main():
    projects = json.loads(PROJECTS.read_text(encoding="utf-8"))
    activity = json.loads(ACTIVITY.read_text(encoding="utf-8"))
    explicit_ai = enrich_explicit_ai(projects, activity)
    state = json.loads(STATE.read_text(encoding="utf-8")) if STATE.exists() else {
        "version": 1,
        "updated_at": None,
        "projects": {},
        "removed": {},
    }

    current = {project["id"]: snapshot(project) for project in projects if project.get("id")}
    previous = state.get("projects") or {}
    removed = state.get("removed") or {}

    events = []
    for project_id in sorted(current):
        now = current[project_id]
        before = previous.get(project_id)
        if before is None:
            if project_id in removed:
                events.append(make_event(
                    "project_restored", project_id, now, "Project restored",
                    "Returned to the tracked catalogue."
                ))
                removed.pop(project_id, None)
            else:
                events.append(make_event(
                    "project_added", project_id, now, "Project added",
                    "Added to the tracked catalogue."
                ))
            continue

        fields = changed_fields(before, now)
        if not fields:
            continue

        if fields == ["title"]:
            event_type = "project_renamed"
            title = "Project renamed"
        elif any(field in MOVE_FIELDS for field in fields):
            event_type = "project_moved"
            title = "Project location changed"
        else:
            event_type = "project_updated"
            title = "Project metadata updated"

        events.append(make_event(
            event_type,
            project_id,
            now,
            title,
            change_message(before, now, fields),
            fields,
            change_details(before, now, fields),
        ))

    for project_id in sorted(set(previous) - set(current)):
        before = previous[project_id]
        removed[project_id] = before
        events.append(make_event(
            "project_removed",
            project_id,
            before,
            "Project removed",
            "Removed from the tracked catalogue.",
        ))

    retained = []
    for event in activity.get("events", []):
        when = parse_time(event.get("date"))
        if when and when >= CUTOFF:
            retained.append(event)

    retained.extend(events)
    retained.sort(
        key=lambda event: (
            event.get("date") or "",
            event.get("repository") or "",
            event.get("sha") or "",
            event.get("type") or "",
            event.get("project_id") or "",
        ),
        reverse=True,
    )

    activity["generated_at"] = NOW_ISO
    activity["window_days"] = DAYS
    activity["events"] = retained
    PROJECTS.write_text(json.dumps(projects, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    ACTIVITY.write_text(json.dumps(activity, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    state = {
        "version": 1,
        "updated_at": NOW_ISO,
        "projects": current,
        "removed": removed,
    }
    STATE.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(
        f"Recorded {len(events)} catalogue activity event{'s' if len(events) != 1 else ''}; "
        f"tracking {len(current)} current projects and {len(removed)} removed-project tombstones; "
        f"enriched {explicit_ai} project{'s' if explicit_ai != 1 else ''} from explicit AI commit subjects."
    )


if __name__ == "__main__":
    main()
