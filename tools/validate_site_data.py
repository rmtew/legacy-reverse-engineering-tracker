#!/usr/bin/env python3
"""Validate tracker JSON relationships and an optional generated RSS feed."""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
import xml.etree.ElementTree as ET


def parse_time(value):
    if not value:
        raise ValueError("missing timestamp")
    return datetime.fromisoformat(str(value).replace("Z", "+00:00"))


def fail(message, errors):
    errors.append(message)


def validate(projects_path, activity_path, rss_path=None):
    errors = []
    projects = json.loads(projects_path.read_text(encoding="utf-8"))
    activity = json.loads(activity_path.read_text(encoding="utf-8"))

    ids = [project.get("id") for project in projects]
    missing_ids = [i for i, value in enumerate(ids) if not value]
    if missing_ids:
        fail("projects missing id at indexes: " + ", ".join(map(str, missing_ids[:10])), errors)
    duplicates = sorted({value for value in ids if value and ids.count(value) > 1})
    if duplicates:
        fail("duplicate project ids: " + ", ".join(duplicates), errors)

    project_ids = {value for value in ids if value}

    allowed_record_classes = {"subject", "tooling", "hybrid"}
    allowed_target_kinds = {
        "game", "application", "demo", "operating-system", "firmware-rom",
        "system-software", "game-engine", "game-subsystem", "development-tool",
    }
    allowed_work_kinds = {
        "disassembly", "decompilation", "source-reconstruction", "source-restoration",
        "binary-analysis", "data-format-analysis", "copy-protection-analysis",
        "reimplementation", "reverse-engineering-derived-port", "patching",
        "translation", "subsystem-reconstruction",
    }
    allowed_tool_kinds = {
        "emulator", "debugger", "profiler", "graphics-debugger", "binary-analysis",
        "disassembler", "reassembler", "ide", "compiler-toolchain",
        "assembler-toolchain", "static-analysis", "language-tooling", "cycle-analysis",
        "rom-tool", "disk-filesystem-tool", "asset-tool", "automation",
        "development-environment",
    }
    for index, project in enumerate(projects):
        record_class = project.get("record_class")
        if record_class not in allowed_record_classes:
            fail(f"project {index} has invalid record_class {record_class!r}", errors)
        for field, allowed in (
            ("target_kinds", allowed_target_kinds),
            ("work_kinds", allowed_work_kinds),
            ("tool_kinds", allowed_tool_kinds),
        ):
            values = project.get(field)
            if not isinstance(values, list):
                fail(f"project {index} field {field} must be an array", errors)
                continue
            invalid = sorted(set(values) - allowed)
            if invalid:
                fail(f"project {index} field {field} has invalid values: {', '.join(invalid)}", errors)
        if record_class in {"subject", "hybrid"} and not project.get("target_kinds"):
            fail(f"project {index} subject/hybrid record has no target_kinds", errors)
        if record_class in {"tooling", "hybrid"} and not project.get("tool_kinds"):
            fail(f"project {index} tooling/hybrid record has no tool_kinds", errors)

    project_event_types = {
        "project_added",
        "project_removed",
        "project_restored",
        "project_renamed",
        "project_moved",
        "project_updated",
    }
    seen_commits = set()
    previous = None
    for index, event in enumerate(activity.get("events", [])):
        project_id = event.get("project_id")
        event_type = event.get("type")
        snapshot = event.get("project") or {}

        if event_type == "commit":
            if project_id not in project_ids:
                fail(f"activity event {index} references unknown project {project_id!r}", errors)
            if not event.get("sha"):
                fail(f"activity event {index} is missing sha", errors)
            key = (project_id, event.get("repository"), event.get("sha"))
            if key in seen_commits:
                fail(f"duplicate activity event key {key!r}", errors)
            seen_commits.add(key)
        elif event_type in project_event_types:
            if not project_id:
                fail(f"project activity event {index} is missing project_id", errors)
            if snapshot.get("id") != project_id:
                fail(f"project activity event {index} snapshot id does not match project_id", errors)
            if not event.get("title"):
                fail(f"project activity event {index} is missing title", errors)
        else:
            fail(f"activity event {index} has unsupported stored type {event_type!r}", errors)

        try:
            when = parse_time(event.get("date"))
        except ValueError:
            fail(f"activity event {index} has invalid date {event.get('date')!r}", errors)
            when = None
        if when and previous and when > previous:
            fail(f"activity events are not newest-first around index {index}", errors)
        if when:
            previous = when

    try:
        parse_time(activity.get("generated_at"))
    except ValueError:
        fail("activity.generated_at is missing or invalid", errors)

    if rss_path:
        try:
            tree = ET.parse(rss_path)
            root = tree.getroot()
            if root.tag != "rss" or root.attrib.get("version") != "2.0":
                fail("RSS root must be <rss version='2.0'>", errors)
            channel = root.find("channel")
            if channel is None:
                fail("RSS channel missing", errors)
            else:
                items = channel.findall("item")
                if len(items) > 200:
                    fail(f"RSS has {len(items)} items; maximum is 200", errors)
                guids = set()
                for index, item in enumerate(items):
                    for field in ("title", "link", "guid", "pubDate"):
                        node = item.find(field)
                        if node is None or not (node.text or "").strip():
                            fail(f"RSS item {index} missing {field}", errors)
                    guid = item.findtext("guid")
                    if guid in guids:
                        fail(f"duplicate RSS guid {guid!r}", errors)
                    guids.add(guid)
        except ET.ParseError as exc:
            fail(f"RSS XML parse error: {exc}", errors)

    if errors:
        for error in errors:
            print("ERROR:", error, file=sys.stderr)
        raise SystemExit(1)

    print(
        f"Validated {len(projects)} projects, {len(activity.get('events', []))} stored activity events"
        + (f" and RSS {rss_path}" if rss_path else "")
        + "."
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("projects", type=Path)
    parser.add_argument("activity", type=Path)
    parser.add_argument("rss", type=Path, nargs="?")
    args = parser.parse_args()
    validate(args.projects, args.activity, args.rss)


if __name__ == "__main__":
    main()
