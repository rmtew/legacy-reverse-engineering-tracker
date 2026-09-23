#!/usr/bin/env python3
"""Merge newly verified discovery records into the canonical project catalogue.

`data/pending-projects.json` is an intentionally small staging queue so discovery
runs can add verified records without rewriting the large catalogue through the
GitHub contents API. Existing project IDs always win; the queue is cleared after
a successful merge. The normal metadata refresher then enriches new GitHub
records before validation/commit.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = ROOT / "data" / "projects.json"
PENDING = ROOT / "data" / "pending-projects.json"


def main() -> None:
    projects = json.loads(PROJECTS.read_text(encoding="utf-8"))
    if not PENDING.exists():
        print("No pending project queue present.")
        return

    pending = json.loads(PENDING.read_text(encoding="utf-8"))
    if not pending:
        print("No pending projects to merge.")
        return

    known = {record.get("id") for record in projects if record.get("id")}
    added = []
    skipped = []
    for record in pending:
        project_id = record.get("id")
        if not project_id:
            raise SystemExit("Pending project is missing id")
        if project_id in known:
            skipped.append(project_id)
            continue
        projects.append(record)
        known.add(project_id)
        added.append(project_id)

    projects.sort(key=lambda record: ((record.get("title") or "").casefold(), record.get("id") or ""))
    PROJECTS.write_text(json.dumps(projects, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    PENDING.write_text("[]\n", encoding="utf-8")

    print(f"Merged {len(added)} pending projects; skipped {len(skipped)} existing IDs.")
    if added:
        print("Added: " + ", ".join(added))
    if skipped:
        print("Skipped: " + ", ".join(skipped))


if __name__ == "__main__":
    main()
