#!/usr/bin/env python3
"""Rank unresolved CPU research from the persistent project-audit index.

This reports research work; it never guesses a CPU from a platform or edits data.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UNRESOLVED = {"unreviewed", "needs-research"}
MACHINE_MATERIAL = ("machine code", "executable", "rom", "binary", "disassembly", "assembly")


def queue(projects: list[dict], audits: list[dict]) -> list[dict]:
    by_id = {item["project_id"]: item for item in audits}
    result = []
    for project in projects:
        audit = by_id.get(project["id"])
        if audit is None:
            raise ValueError(f"Missing audit for {project['id']}")
        areas = audit.get("areas") or {}
        source = (areas.get("source_cpu") or {}).get("state")
        target = (areas.get("target_cpu") or {}).get("state")
        source_pending = source in UNRESOLVED
        target_pending = target in UNRESOLVED
        if not (source_pending or target_pending):
            continue
        material = " ".join(project.get("source_language") or []).lower()
        targets = project.get("target_platforms") or []
        sources = project.get("source_platforms") or []
        score = (50 if source_pending and not project.get("source_cpu") else
                 20 if source_pending else 0)
        score += 20 if target_pending and not project.get("target_cpu") else 0
        score += 25 if any(word in material for word in MACHINE_MATERIAL) else 0
        score += 10 if project.get("record_class") in {"subject", "hybrid"} else 0
        score += 10 if len(set(sources + targets)) > 1 else 0
        if audit.get("last_reviewed") is None:
            score += 5
        result.append({
            "id": project["id"],
            "priority": score,
            "source_cpu_state": source,
            "target_cpu_state": target,
            "source_cpu": project.get("source_cpu") or [],
            "target_cpu": project.get("target_cpu") or [],
            "source_platforms": sources,
            "target_platforms": targets,
            "source_language": project.get("source_language") or [],
            "repo": project.get("repo"),
        })
    return sorted(result, key=lambda item: (-item["priority"], item["id"]))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--json", action="store_true", help="Machine-readable ranked results")
    args = parser.parse_args()
    projects = json.loads((ROOT / "data/projects.json").read_text(encoding="utf-8"))
    audits = json.loads((ROOT / "data/project-audits.json").read_text(encoding="utf-8"))["projects"]
    ranked = queue(projects, audits)
    shown = ranked[:max(0, args.limit)]
    if args.json:
        print(json.dumps({"total": len(ranked), "candidates": shown}, indent=2))
        return
    print(f"{len(ranked)} projects have unresolved source or target CPU audit areas.")
    for item in shown:
        print(f"{item['priority']:3}  {item['id']}: source={item['source_cpu_state']} "
              f"target={item['target_cpu_state']}  {item['repo']}")


if __name__ == "__main__":
    main()
