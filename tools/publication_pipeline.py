#!/usr/bin/env python3
"""Prepare a reviewed delta once, then verify the exact remote and served results.

No network writes. The paired publish_discovery.mjs driver uses the GitHub
connector's atomic blob/tree/commit/expected-SHA ref operations.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path
import re
import shutil
import tempfile
import time
import xml.etree.ElementTree as ET

from apply_discovery_batch import FILES, apply_batch
from validate_site_data import validate


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def encoded(value):
    return (json.dumps(value, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def blob_sha(content):
    return hashlib.sha1(b"blob " + str(len(content)).encode() + b"\0" + content).hexdigest()


def safe_path(value):
    path = Path(value)
    if path.is_absolute() or not path.parts or any(p in {"..", ".git"} for p in path.parts):
        raise ValueError(f"Unsafe publication path: {value}")
    return path


def file_entry(path, content):
    return {"path": str(path), "bytes": len(content), "chars": len(content.decode("utf-8")),
            "sha": blob_sha(content), "sha256": hashlib.sha256(content).hexdigest()}


def verify_files(root, manifest):
    for entry in manifest["files"]:
        content = (Path(root) / safe_path(entry["path"])).read_bytes()
        if file_entry(entry["path"], content) != entry:
            raise ValueError(f"Publication file changed after preparation: {entry['path']}")


def verify_remote(manifest, tree):
    if tree.get("truncated"):
        raise ValueError("Cannot verify a truncated remote tree")
    actual = {x["path"]: x["sha"] for x in tree["tree"] if x["type"] == "blob"}
    for entry in manifest["files"]:
        if actual.get(entry["path"]) != entry["sha"]:
            raise ValueError(f"Remote publication mismatch: {entry['path']}")
    return {"authored_files_verified": len(manifest["files"])}


def verify_live(bundle, live, tree):
    """Check downloaded served data against the deployed commit and authored delta.

    The caller fetches the public site and successful Pages deployment tree.
    This proves bytes and first-scan context; it does not prove builds/playability.
    """
    bundle, live = Path(bundle), Path(live)
    manifest = load(bundle / "manifest.json")
    if tree.get("truncated"):
        raise ValueError("Cannot verify truncated deployed tree")
    blobs = {x["path"]: x["sha"] for x in tree["tree"] if x["type"] == "blob"}
    for name in (*FILES, "activity.json"):
        path = "data/" + name
        if blob_sha((live / path).read_bytes()) != blobs.get(path):
            raise ValueError(f"Served file differs from deployed commit: {path}")
    validate(live / "data/projects.json", live / "data/activity.json", live / "activity.xml")
    for filename, groups in (("discovery-sources.json", ("sources", "backlog")),
                             ("discovery-decisions.json", ("decisions",)),
                             ("research-activity.json", ("events",))):
        wanted = load(bundle / "payload/data" / filename)
        served = load(live / "data" / filename)
        for group in groups:
            present = {item["id"]: item for item in served[group]}
            for item in wanted[group]:
                if present.get(item["id"]) != item:
                    raise ValueError(f"Published research record missing or changed: {filename}/{item['id']}")
    expected = {p["id"]: p for p in load(bundle / "payload/data/projects.json")}
    actual = {p["id"]: p for p in load(live / "data/projects.json")}
    expected_audits = {p["project_id"]: p for p in load(bundle / "payload/data/project-audits.json")["projects"]}
    actual_audits = {p["project_id"]: p for p in load(live / "data/project-audits.json")["projects"]}
    for pid, project in expected.items():
        if pid not in actual:
            raise ValueError(f"Missing published project: {pid}")
        for key in project:
            if key not in {"github", "last_activity", "last_checked", "ai"} and actual[pid].get(key) != project[key]:
                raise ValueError(f"Authored field changed during enrichment: {pid}.{key}")
        if actual_audits.get(pid) != expected_audits.get(pid):
            raise ValueError(f"Authored audit changed during enrichment: {pid}")
        for key in ("usage", "tools"):
            if (actual[pid].get("ai") or {}).get(key) != (project.get("ai") or {}).get(key):
                raise ValueError(f"AI evidence changed during enrichment; review {pid}.{key}")
    events = load(live / "data/activity.json")["events"]
    addition_types = {"project_added", "project_restored"}
    additions = {e["project_id"]: e for e in events if e.get("type") in addition_types}
    windows = {days: {e["project_id"] for e in load(live / f"data/activity-{days}d.json")["events"] if e.get("type") in addition_types} for days in (30, 180)}
    guids = [item.text or "" for item in ET.parse(live / "activity.xml").findall(".//item/guid")]
    added = manifest["summary"]["projects"]
    for pid in added:
        if pid not in additions or any(pid not in values for values in windows.values()):
            raise ValueError(f"Missing publication activity/window event: {pid}")
        if not any(g.startswith(f"legacy-re:{pid}:{kind}:") for g in guids for kind in addition_types):
            raise ValueError(f"Missing publication RSS event: {pid}")
        if "github.com/" not in (actual[pid].get("repo") or ""):
            continue
        gh = actual[pid].get("github") or {}
        for key in ("repository", "default_branch", "tracking_branch", "checked_at", "archived", "fork", "languages"):
            if key not in gh:
                raise ValueError(f"Missing initial metadata: {pid}.{key}")
        context = additions[pid].get("activity_context") or {}
        for key in ("as_of", "last_commit", "last_activity", "commits_90d", "active_days_90d"):
            if key not in context:
                raise ValueError(f"Missing initial activity context: {pid}.{key}")
    return {"served_hashes_verified": True, "authored_projects_preserved": len(expected),
            "initial_context_activity_windows_rss_verified": len(added)}


def legacy_report(batch):
    """Render existing authored audit judgments; never infer research decisions."""
    lines = ["# " + batch["summary"], "", batch.get("notes", ""), ""]
    for entry in batch.get("projects", []) + batch.get("project_updates", []):
        project = entry.get("project", entry.get("changes", {}))
        lines.extend(["## " + str(project.get("display_title") or project.get("title") or entry.get("project_id") or project["id"]), ""])
        for name, area in entry["audit"].get("areas", {}).items():
            lines.extend([f"### {name} ({area['state']})", "", area.get("note", ""), ""])
            lines.extend("- " + url for url in area.get("evidence_urls", []))
            lines.append("")
        lines.extend("- " + action for action in entry["audit"].get("next_actions", []))
        lines.append("")
    for decision in batch.get("decisions", []):
        lines.extend(["## " + decision.get("title", decision["id"]), "", decision["reason"], ""])
    return "\n".join(lines).rstrip() + "\n"


def prepare(document, root, out, baseline, tree, *, evidence_cache=None, expected_commits=None):
    """Write an isolated, repeatable bundle. Never edit the baseline checkout."""
    start = time.perf_counter()
    root, out = Path(root), Path(out)
    if not re.fullmatch(r"[0-9a-f]{40}", baseline):
        raise ValueError("baseline must be the exact 40-character commit SHA")
    if out.resolve() == root.resolve() or root.resolve() in out.resolve().parents:
        raise ValueError("Output must be outside the source checkout")
    if tree.get("truncated"):
        raise ValueError("Baseline tree must be complete")
    tracked = {x["path"]: x for x in tree["tree"] if x["type"] == "blob"}
    consumed = ["data/" + name for name in (*FILES, "activity.json")] + ["sources.md", "log.md"]
    baseline_files = []
    for path in consumed:
        content = (root / path).read_bytes()
        if path not in tracked or blob_sha(content) != tracked[path]["sha"]:
            raise ValueError(f"Baseline file does not match the reviewed tree: {path}")
        baseline_files.append(file_entry(path, content))
    loaded = time.perf_counter()
    if document.get("format") == "research-records/v1":
        from research_record import compile_records, render_report
        batch = compile_records(document, evidence_cache=evidence_cache, expected_commits=expected_commits)
        report = render_report(document, evidence_cache=evidence_cache, expected_commits=expected_commits)
    else:
        batch = copy.deepcopy(document)
        report = legacy_report(batch)
    event = batch["event_id"]
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]*", event):
        raise ValueError("event_id must be a safe filename component")
    fingerprint = digest({"document": document, "baseline": baseline, "baseline_files": baseline_files,
                          "expected_commits": expected_commits})
    if out.exists():
        if not (out / "manifest.json").exists():
            raise ValueError("Output exists without a completed manifest; use a fresh output directory")
        manifest = load(out / "manifest.json")
        if manifest.get("input_digest") != fingerprint:
            raise ValueError("Output belongs to a different input or baseline; prepare a new bundle")
        verify_files(out / "payload", manifest)
        return manifest
    before = {name: load(root / "data" / name) for name in FILES}
    after = copy.deepcopy(before)
    summary = apply_batch(after, batch)
    changed_ids = set(summary["projects"] + summary["updated_projects"])
    existing = {p["id"]: p for p in before["projects.json"]}
    proposed = {p["id"]: p for p in after["projects.json"]}
    old_audits = {p["project_id"]: p for p in before["project-audits.json"]["projects"]}
    new_audits = {p["project_id"]: p for p in after["project-audits.json"]["projects"]}
    for pid, project in existing.items():
        if pid not in changed_ids and (proposed.get(pid) != project or new_audits.get(pid) != old_audits.get(pid)):
            raise ValueError(f"Unrequested project or audit mutation: {pid}")
    review = {"added_ids": summary["projects"], "updated_ids": summary["updated_projects"],
              "preserved_projects": len(existing) - len(summary["updated_projects"]),
              "changes": {pid: {key: {"before": existing.get(pid, {}).get(key), "after": proposed[pid].get(key)}
                                  for key in sorted(set(existing.get(pid, {})) | set(proposed[pid]))
                                  if existing.get(pid, {}).get(key) != proposed[pid].get(key)} for pid in sorted(changed_ids)},
              "uncertain_areas": {pid: [key for key, area in new_audits[pid].get("areas", {}).items()
                                         if area["state"] in {"needs-research", "no-evidence-found", "unreviewed"}]
                                  for pid in sorted(changed_ids)}}
    applied = time.perf_counter()
    out.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".publication-", dir=out.parent) as tmp:
        stage = Path(tmp)
        payload = stage / "payload"
        (payload / "data").mkdir(parents=True)
        files = []
        for name in FILES:
            content = encoded(after[name])
            (payload / "data" / name).write_bytes(content)
            if content != (root / "data" / name).read_bytes():
                files.append(file_entry("data/" + name, content))
        shutil.copy2(root / "data/activity.json", payload / "data/activity.json")
        validate(payload / "data/projects.json", payload / "data/activity.json")
        report_path = f"docs/research/{event}.md"
        if report_path in tracked:
            raise ValueError("Research report already exists; event IDs must be unique")
        (payload / "docs/research").mkdir(parents=True)
        (payload / report_path).write_text(report, encoding="utf-8")
        files.append(file_entry(report_path, report.encode("utf-8")))
        for path in ("sources.md", "log.md"):
            content = (root / path).read_text(encoding="utf-8").rstrip() + f"\n\n## {batch['date']} — {batch['summary']}\n\n[Research record]({report_path}).\n"
            (payload / path).write_text(content, encoding="utf-8")
            files.append(file_entry(path, content.encode("utf-8")))
        validated = time.perf_counter()
        manifest = {"version": 1, "baseline_commit": baseline, "input_digest": fingerprint,
                    "event_id": event, "files": sorted(files, key=lambda x: x["path"]),
                    "baseline_files": baseline_files, "summary": summary,
                    "timings_seconds": {"baseline_read_verify": loaded - start,
                                        "compile_apply_preservation": applied - loaded,
                                        "serialize_validate_render": validated - applied,
                                        "total_prepare": validated - start}}
        (stage / "batch.json").write_bytes(encoded(batch))
        (stage / "review.json").write_bytes(encoded(review))
        (stage / "manifest.json").write_bytes(encoded(manifest))
        stage.rename(out)
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    stage = sub.add_parser("prepare")
    stage.add_argument("input", type=Path)
    stage.add_argument("--root", type=Path, required=True)
    stage.add_argument("--out", type=Path, required=True)
    stage.add_argument("--baseline", required=True)
    stage.add_argument("--baseline-tree", type=Path, required=True)
    stage.add_argument("--evidence-cache", type=Path)
    stage.add_argument("--expected-commits", type=Path)
    check = sub.add_parser("verify-files")
    check.add_argument("bundle", type=Path)
    remote = sub.add_parser("verify-remote")
    remote.add_argument("bundle", type=Path)
    remote.add_argument("tree", type=Path)
    live = sub.add_parser("verify-live")
    live.add_argument("bundle", type=Path)
    live.add_argument("root", type=Path)
    live.add_argument("tree", type=Path)
    args = parser.parse_args()
    if args.command == "prepare":
        result = prepare(load(args.input), args.root, args.out, args.baseline, load(args.baseline_tree),
                         evidence_cache=args.evidence_cache,
                         expected_commits=load(args.expected_commits) if args.expected_commits else None)
        print(json.dumps({"event_id": result["event_id"], "summary": result["summary"], "files": result["files"], "timings_seconds": result["timings_seconds"]}, indent=2))
    elif args.command == "verify-files":
        verify_files(args.bundle / "payload", load(args.bundle / "manifest.json"))
        print("All publication file hashes verified")
    elif args.command == "verify-remote":
        print(json.dumps(verify_remote(load(args.bundle / "manifest.json"), load(args.tree))))
    else:
        print(json.dumps(verify_live(args.bundle, args.root, load(args.tree))))


if __name__ == "__main__":
    main()
