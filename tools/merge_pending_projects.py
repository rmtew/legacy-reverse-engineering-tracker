#!/usr/bin/env python3
"""Merge verified discoveries and small curated updates into the catalogue.

`data/pending-projects.json` is an intentionally small staging queue so discovery
and maintenance runs can update the large catalogue without rewriting it through
the GitHub contents API. Normal entries add new projects; existing project IDs
still win by default. An existing record may be deliberately patched only with
an explicit `_update` object containing top-level `set` and/or `remove` fields.
The queue is cleared after a successful merge.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = ROOT / "data" / "projects.json"
PENDING = ROOT / "data" / "pending-projects.json"


def apply_update(record: dict, update: dict, project_id: str) -> None:
    if not isinstance(update, dict):
        raise SystemExit(f"Pending update for {project_id} must be an object")
    fields = update.get("set") or {}
    remove = update.get("remove") or []
    if not isinstance(fields, dict) or not isinstance(remove, list):
        raise SystemExit(f"Pending update for {project_id} has invalid set/remove values")
    if "id" in fields or "id" in remove:
        raise SystemExit(f"Pending update for {project_id} may not change or remove id")
    for key, value in fields.items():
        record[key] = value
    for key in remove:
        record.pop(key, None)


def main() -> None:
    projects = json.loads(PROJECTS.read_text(encoding="utf-8"))
    if not PENDING.exists():
        print("No pending project queue present.")
        return

    pending = json.loads(PENDING.read_text(encoding="utf-8"))
    if not pending:
        print("No pending projects to merge.")
        return

    by_id = {record.get("id"): record for record in projects if record.get("id")}
    added = []
    updated = []
    skipped = []
    for record in pending:
        project_id = record.get("id")
        if not project_id:
            raise SystemExit("Pending project is missing id")

        update = record.get("_update")
        if update is not None:
            current = by_id.get(project_id)
            if current is None:
                raise SystemExit(f"Pending update references unknown project id: {project_id}")
            apply_update(current, update, project_id)
            updated.append(project_id)
            continue

        if project_id in by_id:
            skipped.append(project_id)
            continue
        projects.append(record)
        by_id[project_id] = record
        added.append(project_id)

    projects.sort(key=lambda record: ((record.get("title") or "").casefold(), record.get("id") or ""))
    PROJECTS.write_text(json.dumps(projects, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    PENDING.write_text("[]\n", encoding="utf-8")

    print(
        f"Merged {len(added)} pending projects; applied {len(updated)} curated updates; "
        f"skipped {len(skipped)} existing IDs."
    )
    if added:
        print("Added: " + ", ".join(added))
    if updated:
        print("Updated: " + ", ".join(updated))
    if skipped:
        print("Skipped: " + ", ".join(skipped))


if __name__ == "__main__":
    main()
