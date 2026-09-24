#!/usr/bin/env python3
"""Stage one researched discovery batch, validate the whole tracker, then write it.

The input format and publishing steps are documented in README.md. This tool
never commits or publishes. Without --write it only previews the proposed state.
"""
from __future__ import annotations

import argparse
import copy
from datetime import date
import json
import os
from pathlib import Path
import shutil
import tempfile

from merge_pending_projects import new_audit
from validate_site_data import validate

ROOT = Path(__file__).resolve().parents[1]
FILES = ("projects.json", "project-audits.json", "discovery-sources.json",
         "discovery-decisions.json", "research-activity.json")


def unique_url(url: str) -> str:
    return url.rstrip("/").casefold()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def apply_batch(data: dict, batch: dict) -> dict:
    allowed = {"date", "event_id", "summary", "notes", "kind", "projects", "sources",
               "source_updates", "tasks", "task_updates", "decisions", "source_ids"}
    require(isinstance(batch, dict) and not (set(batch) - allowed), "Unknown batch fields or invalid batch object")
    day = batch.get("date")
    require(isinstance(day, str), "Batch needs a date (YYYY-MM-DD)")
    date.fromisoformat(day)
    for field in ("event_id", "summary"):
        require(isinstance(batch.get(field), str) and bool(batch[field].strip()), f"Batch needs {field}")
    for field in ("projects", "sources", "source_updates", "tasks", "task_updates", "decisions", "source_ids"):
        require(isinstance(batch.get(field, []), list), f"{field} must be an array")
    require(any(batch.get(field) for field in ("projects", "sources", "source_updates", "tasks", "task_updates", "decisions")), "Batch has no changes")

    projects = data["projects.json"]
    audits = data["project-audits.json"]["projects"]
    discovery = data["discovery-sources.json"]
    decisions = data["discovery-decisions.json"]["decisions"]
    history = data["research-activity.json"]["events"]
    source_by_id = {s["id"]: s for s in discovery["sources"]}
    task_by_id = {t["id"]: t for t in discovery["backlog"]}
    project_ids = {p["id"] for p in projects}
    audit_ids = {a["project_id"] for a in audits}
    event_sources = set(batch.get("source_ids", []))
    added_projects = []

    for source in batch.get("sources", []):
        require(isinstance(source, dict) and source.get("id") not in source_by_id, "Duplicate or invalid source id")
        source = copy.deepcopy(source)
        source.setdefault("first_indexed", day)
        source.setdefault("last_reviewed", day)
        source.setdefault("review_state", "partial")
        source.setdefault("projects_promoted", [])
        source.setdefault("open_task_ids", [])
        discovery["sources"].append(source)
        source_by_id[source["id"]] = source
        event_sources.add(source["id"])

    for task in batch.get("tasks", []):
        require(isinstance(task, dict) and task.get("id") not in task_by_id, "Duplicate or invalid task id")
        task = copy.deepcopy(task)
        task.setdefault("created_at", day)
        task.setdefault("last_reviewed", day)
        task.setdefault("state", "open")
        for source_id in task.get("source_ids", []):
            require(source_id in source_by_id, f"Unknown source {source_id} in task")
            if task["state"] in {"open", "in-progress"}:
                source_by_id[source_id]["open_task_ids"] = sorted(set(source_by_id[source_id]["open_task_ids"]) | {task["id"]})
            event_sources.add(source_id)
        discovery["backlog"].append(task)
        task_by_id[task["id"]] = task

    known_urls = {}
    for project in projects:
        url = project.get("project_url") or project.get("repo")
        if url:
            known_urls.setdefault(unique_url(url), []).append(project["id"])
    for entry in batch.get("projects", []):
        require(isinstance(entry, dict) and isinstance(entry.get("project"), dict), "Each project entry needs a project object")
        project = copy.deepcopy(entry["project"])
        project_id = project.get("id")
        require(isinstance(project_id, str) and project_id and project_id not in project_ids, f"Duplicate or invalid project id {project_id!r}")
        source_ids = entry.get("source_ids")
        require(isinstance(source_ids, list) and source_ids, f"Project {project_id} needs source_ids")
        for source_id in source_ids:
            require(source_id in source_by_id, f"Unknown source {source_id} for {project_id}")
            source = source_by_id[source_id]
            source["projects_promoted"] = sorted(set(source["projects_promoted"]) | {project_id})
            source["last_reviewed"] = day
            event_sources.add(source_id)
        url = project.get("project_url") or project.get("repo")
        require(isinstance(url, str) and bool(url.strip()), f"Project {project_id} needs repo or project_url")
        collision = known_urls.get(unique_url(url), [])
        require(not collision or entry.get("allow_shared_url") is True,
                f"Project {project_id} shares URL with {', '.join(collision)}; use a distinct project_url or explicitly allow_shared_url")
        known_urls.setdefault(unique_url(url), []).append(project_id)
        audit = copy.deepcopy(entry.get("audit", new_audit(project_id)))
        require(audit.get("project_id", project_id) == project_id and project_id not in audit_ids, f"Invalid audit for {project_id}")
        audit["project_id"] = project_id
        projects.append(project)
        audits.append(audit)
        project_ids.add(project_id)
        audit_ids.add(project_id)
        added_projects.append(project_id)

    for update in batch.get("source_updates", []):
        require(isinstance(update, dict) and update.get("id") in source_by_id, "Source update references unknown id")
        require(not (set(update) - {"id", "review_state", "reason", "last_reviewed"}), "Unsupported source update field")
        source = source_by_id[update["id"]]
        source.update({key: value for key, value in update.items() if key != "id"})
        source["last_reviewed"] = update.get("last_reviewed", day)
        event_sources.add(source["id"])

    for update in batch.get("task_updates", []):
        require(isinstance(update, dict) and update.get("id") in task_by_id, "Task update references unknown id")
        require(not (set(update) - {"id", "state", "notes_append", "last_reviewed"}), "Unsupported task update field")
        task = task_by_id[update["id"]]
        if "notes_append" in update:
            require(isinstance(update["notes_append"], str) and bool(update["notes_append"].strip()), "notes_append must be nonempty")
            task["notes"] = (task.get("notes", "").rstrip() + " " + update["notes_append"].strip()).strip()
        task.update({key: value for key, value in update.items() if key in {"state", "last_reviewed"}})
        task["last_reviewed"] = update.get("last_reviewed", day)
        for source_id in task.get("source_ids", []):
            source = source_by_id[source_id]
            linked = set(source["open_task_ids"])
            if task["state"] in {"open", "in-progress"}:
                linked.add(task["id"])
            else:
                linked.discard(task["id"])
            source["open_task_ids"] = sorted(linked)
            event_sources.add(source_id)

    known_decision_ids = {d["id"] for d in decisions}
    known_decision_urls = {unique_url(d["url"]) for d in decisions}
    for decision in batch.get("decisions", []):
        require(isinstance(decision, dict) and isinstance(decision.get("id"), str), "Decision needs id")
        require(decision["id"] not in known_decision_ids, f"Duplicate decision id {decision['id']}")
        require(isinstance(decision.get("url"), str) and unique_url(decision["url"]) not in known_decision_urls,
                f"Duplicate or invalid decision URL for {decision['id']}")
        decision = copy.deepcopy(decision)
        decision.setdefault("reviewed_at", day)
        decision.setdefault("project_ids", [])
        for source_id in decision.get("source_ids", []):
            require(source_id in source_by_id, f"Unknown source {source_id} for decision")
            event_sources.add(source_id)
        decisions.append(decision)
        known_decision_ids.add(decision["id"])
        known_decision_urls.add(unique_url(decision["url"]))

    require(all(source_id in source_by_id for source_id in event_sources), "Event references unknown source")
    require(batch["event_id"] not in {event["id"] for event in history}, "Duplicate research event id")
    event = {"id": batch["event_id"], "date": day, "kind": batch.get("kind", "source-review"),
             "summary": batch["summary"], "source_ids": sorted(event_sources),
             "project_ids": added_projects, "notes": batch.get("notes", "")}
    position = next((i for i, old in enumerate(history) if old["date"] <= day), len(history))
    history.insert(position, event)
    for name in ("discovery-sources.json", "discovery-decisions.json", "project-audits.json", "research-activity.json"):
        data[name]["indexed_at"] = day
    return {"projects": added_projects, "sources": sorted(event_sources), "decisions": len(batch.get("decisions", []))}


def run(root: Path, batch: dict, write: bool) -> dict:
    data_dir = root / "data"
    data = {name: json.loads((data_dir / name).read_text(encoding="utf-8")) for name in FILES}
    original = {name: (data_dir / name).read_bytes() for name in FILES}
    summary = apply_batch(data, batch)
    with tempfile.TemporaryDirectory(prefix=".discovery-batch-", dir=root) as tmp:
        staged = Path(tmp) / "data"
        staged.mkdir()
        shutil.copy2(data_dir / "activity.json", staged / "activity.json")
        changed = {}
        for name in FILES:
            content = (json.dumps(data[name], indent=2, ensure_ascii=False) + "\n").encode("utf-8")
            if content != original[name]:
                (staged / name).write_bytes(content)
                changed[name] = content
            else:
                shutil.copy2(data_dir / name, staged / name)
        validate(staged / "projects.json", staged / "activity.json")
        if write:
            written = []
            try:
                for name, content in changed.items():
                    os.replace(staged / name, data_dir / name)
                    written.append(name)
            except OSError:
                for name in written:
                    (data_dir / name).write_bytes(original[name])
                raise
    summary["changed_files"] = ["data/" + name for name in changed]
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("batch", type=Path, help="JSON research batch")
    parser.add_argument("--write", action="store_true", help="Apply the validated batch; default is dry-run")
    parser.add_argument("--root", type=Path, default=ROOT, help=argparse.SUPPRESS)
    args = parser.parse_args()
    try:
        summary = run(args.root, json.loads(args.batch.read_text(encoding="utf-8")), args.write)
    except (ValueError, KeyError, TypeError) as exc:
        parser.error(str(exc))
    print(("Applied" if args.write else "Dry run:") + f" {len(summary['projects'])} projects, "
          f"{summary['decisions']} decisions; sources: {', '.join(summary['sources']) or 'none'}")
    print("Files: " + ", ".join(summary["changed_files"]))


if __name__ == "__main__":
    main()
