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



RESEARCH_AREAS = {"identity", "classification", "source_cpu", "target_cpu", "build", "runtime_profiles", "ai", "relationships"}
RESEARCH_AREA_STATES = {"unreviewed", "needs-research", "reviewed", "not-applicable", "no-evidence-found"}
RESEARCH_OVERALL_STATES = {"unreviewed", "partial", "reviewed"}
DISCOVERY_REVIEW_STATES = {"unreviewed", "partial", "substantially-reviewed", "exhausted"}
DISCOVERY_TASK_STATES = {"open", "in-progress", "done", "deferred"}
DISCOVERY_DECISIONS = {"excluded", "duplicate", "deferred", "promoted"}


def validate_date(value, label, errors, allow_none=True):
    if value is None and allow_none:
        return
    if not isinstance(value, str):
        fail(f"{label} must be a date string" + (" or null" if allow_none else ""), errors)
        return
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        fail(f"{label} has invalid date {value!r}", errors)


def validate_research_state(projects_path, project_ids, errors):
    data_dir = projects_path.parent
    discovery_path = data_dir / "discovery-sources.json"
    audits_path = data_dir / "project-audits.json"
    research_path = data_dir / "research-activity.json"
    decisions_path = data_dir / "discovery-decisions.json"

    missing_files = [str(path) for path in (discovery_path, audits_path, research_path, decisions_path) if not path.exists()]
    if missing_files:
        fail("research state files missing: " + ", ".join(missing_files), errors)
        return 0, 0, 0, 0

    discovery = json.loads(discovery_path.read_text(encoding="utf-8"))
    audits = json.loads(audits_path.read_text(encoding="utf-8"))
    research = json.loads(research_path.read_text(encoding="utf-8"))
    decisions = json.loads(decisions_path.read_text(encoding="utf-8"))
    validate_date(decisions.get("indexed_at"), "discovery decisions indexed_at", errors, allow_none=False)

    source_ids = []
    for index, source in enumerate(discovery.get("sources", [])):
        source_id = source.get("id")
        if not isinstance(source_id, str) or not source_id:
            fail(f"discovery source {index} is missing id", errors)
            continue
        source_ids.append(source_id)
        if not isinstance(source.get("source"), str) or not source.get("source", "").strip():
            fail(f"discovery source {source_id} is missing source", errors)
        if source.get("review_state") not in DISCOVERY_REVIEW_STATES:
            fail(f"discovery source {source_id} has invalid review_state {source.get('review_state')!r}", errors)
        validate_date(source.get("first_indexed"), f"discovery source {source_id} first_indexed", errors, allow_none=False)
        validate_date(source.get("last_reviewed"), f"discovery source {source_id} last_reviewed", errors)

    duplicate_sources = sorted({value for value in source_ids if source_ids.count(value) > 1})
    if duplicate_sources:
        fail("duplicate discovery source ids: " + ", ".join(duplicate_sources), errors)
    source_id_set = set(source_ids)

    task_ids = []
    for index, task in enumerate(discovery.get("backlog", [])):
        task_id = task.get("id")
        if not isinstance(task_id, str) or not task_id:
            fail(f"discovery backlog task {index} is missing id", errors)
            continue
        task_ids.append(task_id)
        if task.get("state") not in DISCOVERY_TASK_STATES:
            fail(f"discovery task {task_id} has invalid state {task.get('state')!r}", errors)
        refs = task.get("source_ids")
        if not isinstance(refs, list):
            fail(f"discovery task {task_id} source_ids must be an array", errors)
        else:
            unknown = sorted(set(refs) - source_id_set)
            if unknown:
                fail(f"discovery task {task_id} references unknown source ids: {', '.join(unknown)}", errors)
        validate_date(task.get("created_at"), f"discovery task {task_id} created_at", errors, allow_none=False)
        validate_date(task.get("last_reviewed"), f"discovery task {task_id} last_reviewed", errors)

    duplicate_tasks = sorted({value for value in task_ids if task_ids.count(value) > 1})
    if duplicate_tasks:
        fail("duplicate discovery task ids: " + ", ".join(duplicate_tasks), errors)
    task_id_set = set(task_ids)
    for source in discovery.get("sources", []):
        promoted = source.get("projects_promoted")
        if not isinstance(promoted, list):
            fail(f"discovery source {source.get('id')} projects_promoted must be an array", errors)
        else:
            unknown_projects = sorted(set(promoted) - project_ids)
            if unknown_projects:
                fail(f"discovery source {source.get('id')} references unknown promoted projects: {', '.join(unknown_projects)}", errors)
        unknown = sorted(set(source.get("open_task_ids") or []) - task_id_set)
        if unknown:
            fail(f"discovery source {source.get('id')} references unknown open tasks: {', '.join(unknown)}", errors)

    decision_ids = set()
    decision_urls = set()
    if not isinstance(decisions.get("decisions"), list):
        fail("discovery decisions must be an array", errors)
    else:
        for index, decision in enumerate(decisions["decisions"]):
            if not isinstance(decision, dict):
                fail(f"discovery decision {index} must be an object", errors)
                continue
            decision_id = decision.get("id")
            url = decision.get("url")
            if not isinstance(decision_id, str) or not decision_id.strip():
                fail(f"discovery decision {index} is missing id", errors)
            elif decision_id in decision_ids:
                fail(f"duplicate discovery decision id {decision_id}", errors)
            else:
                decision_ids.add(decision_id)
            if not isinstance(url, str) or not url.startswith(("https://", "http://")):
                fail(f"discovery decision {index} has invalid url", errors)
            elif url.rstrip("/").casefold() in decision_urls:
                fail(f"duplicate discovery decision url {url}", errors)
            else:
                decision_urls.add(url.rstrip("/").casefold())
            for field in ("title", "reason"):
                if not isinstance(decision.get(field), str) or not decision[field].strip():
                    fail(f"discovery decision {index} is missing {field}", errors)
            if decision.get("decision") not in DISCOVERY_DECISIONS:
                fail(f"discovery decision {index} has invalid decision {decision.get('decision')!r}", errors)
            validate_date(decision.get("reviewed_at"), f"discovery decision {index} reviewed_at", errors, allow_none=False)
            for field, allowed in (("source_ids", source_id_set), ("project_ids", project_ids)):
                values = decision.get(field)
                if not isinstance(values, list) or any(not isinstance(value, str) for value in values):
                    fail(f"discovery decision {index} {field} must be an array of IDs", errors)
                else:
                    unknown = sorted(set(values) - allowed)
                    if unknown:
                        fail(f"discovery decision {index} has unknown {field}: {', '.join(unknown)}", errors)
                    if field == "source_ids" and not values:
                        fail(f"discovery decision {index} needs source_ids", errors)
            evidence = decision.get("evidence_urls")
            if not isinstance(evidence, list) or not evidence or any(not isinstance(link, str) or not link.startswith(("https://", "http://")) for link in evidence):
                fail(f"discovery decision {index} needs evidence_urls", errors)
            if decision.get("decision") == "promoted" and not decision.get("project_ids"):
                fail(f"promoted discovery decision {index} needs project_ids", errors)

    audit_ids = []
    for index, audit in enumerate(audits.get("projects", [])):
        project_id = audit.get("project_id")
        if not isinstance(project_id, str) or not project_id:
            fail(f"project audit {index} is missing project_id", errors)
            continue
        audit_ids.append(project_id)
        if audit.get("overall_state") not in RESEARCH_OVERALL_STATES:
            fail(f"project audit {project_id} has invalid overall_state {audit.get('overall_state')!r}", errors)
        validate_date(audit.get("last_reviewed"), f"project audit {project_id} last_reviewed", errors)
        areas = audit.get("areas")
        if not isinstance(areas, dict):
            fail(f"project audit {project_id} areas must be an object", errors)
            continue
        missing = RESEARCH_AREAS - set(areas)
        extra = set(areas) - RESEARCH_AREAS
        if missing:
            fail(f"project audit {project_id} missing areas: {', '.join(sorted(missing))}", errors)
        if extra:
            fail(f"project audit {project_id} has unknown areas: {', '.join(sorted(extra))}", errors)
        for area_name, area in areas.items():
            if not isinstance(area, dict):
                fail(f"project audit {project_id} area {area_name} must be an object", errors)
                continue
            if area.get("state") not in RESEARCH_AREA_STATES:
                fail(f"project audit {project_id} area {area_name} has invalid state {area.get('state')!r}", errors)
            validate_date(area.get("checked_at"), f"project audit {project_id} area {area_name} checked_at", errors)
        if not isinstance(audit.get("next_actions"), list):
            fail(f"project audit {project_id} next_actions must be an array", errors)

    duplicate_audits = sorted({value for value in audit_ids if audit_ids.count(value) > 1})
    if duplicate_audits:
        fail("duplicate project audit ids: " + ", ".join(duplicate_audits), errors)
    audit_id_set = set(audit_ids)
    missing_audits = sorted(project_ids - audit_id_set)
    stale_audits = sorted(audit_id_set - project_ids)
    if missing_audits:
        fail("projects missing audit records: " + ", ".join(missing_audits[:20]), errors)
    if stale_audits:
        fail("project audits reference missing projects: " + ", ".join(stale_audits[:20]), errors)

    event_ids = []
    previous_date = None
    for index, event in enumerate(research.get("events", [])):
        event_id = event.get("id")
        if not isinstance(event_id, str) or not event_id:
            fail(f"research event {index} is missing id", errors)
            continue
        event_ids.append(event_id)
        validate_date(event.get("date"), f"research event {event_id} date", errors, allow_none=False)
        if not isinstance(event.get("kind"), str) or not event.get("kind", "").strip():
            fail(f"research event {event_id} is missing kind", errors)
        if not isinstance(event.get("summary"), str) or not event.get("summary", "").strip():
            fail(f"research event {event_id} is missing summary", errors)
        unknown_projects = sorted(set(event.get("project_ids") or []) - project_ids)
        if unknown_projects:
            fail(f"research event {event_id} references unknown projects: {', '.join(unknown_projects)}", errors)
        unknown_sources = sorted(set(event.get("source_ids") or []) - source_id_set)
        if unknown_sources:
            fail(f"research event {event_id} references unknown sources: {', '.join(unknown_sources)}", errors)
        date = event.get("date")
        if isinstance(date, str) and previous_date and date > previous_date:
            fail(f"research events are not newest-first around index {index}", errors)
        if isinstance(date, str):
            previous_date = date

    duplicate_events = sorted({value for value in event_ids if event_ids.count(value) > 1})
    if duplicate_events:
        fail("duplicate research event ids: " + ", ".join(duplicate_events), errors)

    return len(source_ids), len(audit_ids), len(event_ids), len(decisions.get("decisions", []))


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

    source_count, audit_count, research_event_count, decision_count = validate_research_state(projects_path, project_ids, errors)

    for index, project in enumerate(projects):
        for field in ("upstream_name", "display_title"):
            value = project.get(field)
            if not isinstance(value, str) or not value.strip():
                fail(f"project {index} field {field} must be a non-empty string", errors)
        subjects = project.get("subjects")
        target_cpu = project.get("target_cpu")
        if target_cpu is not None:
            if not isinstance(target_cpu, list):
                fail(f"project {index} field target_cpu must be an array when present", errors)
            elif any(not isinstance(value, str) or not value.strip() for value in target_cpu):
                fail(f"project {index} target_cpu must contain only non-empty strings", errors)
        runtime_profiles = project.get("runtime_profiles")
        if runtime_profiles is not None:
            if not isinstance(runtime_profiles, list):
                fail(f"project {index} field runtime_profiles must be an array when present", errors)
            else:
                for profile_index, profile in enumerate(runtime_profiles):
                    if not isinstance(profile, dict):
                        fail(f"project {index} runtime profile {profile_index} must be an object", errors)
                        continue
                    if not isinstance(profile.get("platform"), str) or not profile.get("platform", "").strip():
                        fail(f"project {index} runtime profile {profile_index} must have a non-empty platform", errors)
                    for field in ("name", "cpu_family", "min_cpu", "os", "notes"):
                        value = profile.get(field)
                        if value is not None and (not isinstance(value, str) or not value.strip()):
                            fail(f"project {index} runtime profile {profile_index} field {field} must be a non-empty string when present", errors)
                    for field in ("min_ram_kib", "min_chip_ram_kib", "min_fast_ram_kib"):
                        value = profile.get(field)
                        if value is not None and (not isinstance(value, int) or isinstance(value, bool) or value < 0):
                            fail(f"project {index} runtime profile {profile_index} field {field} must be a non-negative integer when present", errors)
                    chipsets = profile.get("chipsets")
                    if chipsets is not None and (not isinstance(chipsets, list) or any(not isinstance(value, str) or not value.strip() for value in chipsets)):
                        fail(f"project {index} runtime profile {profile_index} chipsets must be an array of non-empty strings", errors)
                    evidence = profile.get("evidence")
                    if evidence is not None and not isinstance(evidence, list):
                        fail(f"project {index} runtime profile {profile_index} evidence must be an array when present", errors)
        if not isinstance(subjects, list):
            fail(f"project {index} field subjects must be an array", errors)
        elif any(not isinstance(value, str) or not value.strip() for value in subjects):
            fail(f"project {index} subjects must contain only non-empty strings", errors)

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
        if record_class in {"subject", "hybrid"} and not project.get("subjects"):
            fail(f"project {index} subject/hybrid record has no subjects", errors)
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
        elif event_type == "daily_commits":
            if project_id not in project_ids:
                fail(f"activity summary {index} references unknown project {project_id!r}", errors)
            if not event.get("day") or not event.get("shas") or event.get("count") != len(set(event["shas"])):
                fail(f"activity summary {index} has invalid day or commit identities", errors)
            for sha in event.get("shas") or []:
                key = (project_id, event.get("repository"), sha)
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
        + f", {source_count} discovery sources, {decision_count} discovery decisions, {audit_count} project audits, {research_event_count} research events"
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
