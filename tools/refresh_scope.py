#!/usr/bin/env python3
"""Select publication work from catalogue deltas, independently of polling cadence.

The manifest lives in RUNNER_TEMP, so resetting to a newer main does not erase
the original comparison base. Persisted per-repository work survives failed
runs and is also consumed by the ordinary scheduled refresh.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
from pathlib import Path

from record_project_activity import snapshot

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = ROOT / "data/projects.json"
STATE = ROOT / "state/github-poll-state.json"
CATALOGUE = ROOT / "state/project-catalog-state.json"


def repository(project):
    match = re.fullmatch(r"https?://github\.com/([^/]+)/([^/#?]+?)(?:\.git)?/?", project.get("repo") or "")
    return f"{match[1]}/{match[2]}" if match else None


def material(project):
    # Match the existing catalogue-event definition of authored/material fields.
    # Poll timestamps, last_activity and changing AI evidence counts are excluded;
    # explicit AI usage/tools and top-level branch/path changes remain material.
    return snapshot(project)


def tracking(project):
    return (repository(project), project.get("github_branch"), project.get("github_path"))


def catalogue_delta(before, after):
    old = {p["id"]: p for p in before}
    new = {p["id"]: p for p in after}
    changed = sorted(pid for pid, p in new.items() if pid not in old or material(old[pid]) != material(p))
    removed = sorted(set(old) - set(new))
    reset = sorted(pid for pid in changed if pid not in old or tracking(old[pid]) != tracking(new[pid]))
    left_github = sorted(pid for pid in changed if pid in old and repository(old[pid]) and not repository(new[pid]))
    repositories = sorted({repository(new[pid]) for pid in changed if repository(new[pid])})
    membership = sorted({repository(p) for pid in changed + removed
                         for p in (old.get(pid, {}), new.get(pid, {})) if repository(p)})
    fingerprints = {}
    for repo in repositories:
        records = sorted((material(p) for p in after if repository(p) == repo), key=lambda p: p["id"])
        fingerprints[repo] = hashlib.sha256(json.dumps(records, sort_keys=True).encode()).hexdigest()
    return {"mode": "publication", "repositories": repositories,
            "changed_project_ids": changed, "reset_project_ids": reset, "left_github_project_ids": left_github,
            "removed_project_ids": removed, "membership_repositories": membership,
            "fingerprints": fingerprints}


def union_catalogue_deltas(*deltas):
    """Retain work missed by earlier triggers, using the same current catalogue."""
    fields = ("repositories", "changed_project_ids", "reset_project_ids", "left_github_project_ids",
              "removed_project_ids", "membership_repositories")
    merged = {"mode": "publication", **{field: sorted({value for delta in deltas
              for value in delta.get(field, [])}) for field in fields}}
    merged["fingerprints"] = {repo: fingerprint for delta in deltas
                              for repo, fingerprint in delta["fingerprints"].items()}
    return merged


def load_scope():
    filename = os.environ.get("GITHUB_REFRESH_SCOPE_FILE")
    if not filename:
        return {"mode": "adaptive"}
    scope = json.loads(Path(filename).read_text(encoding="utf-8"))
    if scope.get("mode") not in {"adaptive", "publication"}:
        raise ValueError("Invalid GitHub refresh scope")
    return scope


def select_repositories(repositories, scope):
    if scope["mode"] != "publication":
        return repositories
    selected = set(scope["repositories"])
    return {repo: projects for repo, projects in repositories.items() if repo in selected}


def prepare_publication(repositories, state, scope, projects=None):
    if scope["mode"] != "publication":
        # An hourly/default-manual run can begin before the publication run.
        # It stays broad, but must not bless new catalogue work as complete.
        if scope.get("publication"):
            prepare_publication(repositories, state, scope["publication"], projects)
        return
    # A move away from GitHub has no selected GitHub repository to visit below.
    for project in projects or []:
        if project["id"] in scope.get("left_github_project_ids", []) and repository(project) is None:
            project.pop("github", None)
            project.pop("last_activity", None)
    states = state.setdefault("repositories", {})
    for repo in scope["membership_repositories"]:
        if repo not in repositories:
            states.pop(repo, None)
        elif repo in states:
            ids = sorted(p["id"] for p in repositories[repo])
            states[repo]["project_ids"] = ids
            if "last_deep_scan_project_ids" in states[repo]:
                states[repo]["last_deep_scan_project_ids"] = sorted(set(states[repo]["last_deep_scan_project_ids"]) & set(ids))
    for repo in scope["repositories"]:
        if repo not in repositories:
            continue
        rs = states.setdefault(repo, {})
        fingerprint = scope["fingerprints"][repo]
        if (rs.get("publication") or {}).get("fingerprint") == fingerprint:
            continue
        reset_ids = sorted(p["id"] for p in repositories[repo] if p["id"] in scope["reset_project_ids"])
        rs["publication"] = {"fingerprint": fingerprint, "metadata_complete": False,
                             "history_complete": False, "reset_project_ids": reset_ids}
        # Do not let an old repository scan freeze context for a new project or
        # changed branch/path before its full history has actually completed.
        rs.pop("last_deep_scan", None)
        rs.pop("last_deep_scan_project_ids", None)
        rs["scan_requested"] = True
        rs["scan_reason"] = "publication"
        for project in repositories[repo]:
            if project["id"] in reset_ids:
                project.pop("github", None)
                project.pop("last_activity", None)


def pending_publication(rs):
    work = rs.get("publication") or {}
    return bool(work) and not (work.get("metadata_complete") and work.get("history_complete"))


def check_complete(scope, state):
    if scope["mode"] != "publication":
        if scope.get("publication"):
            check_complete(scope["publication"], state)
        return
    incomplete = []
    for repo in scope["repositories"]:
        work = (state.get("repositories", {}).get(repo) or {}).get("publication") or {}
        if (work.get("fingerprint") != scope["fingerprints"][repo]
                or not work.get("metadata_complete") or not work.get("history_complete")):
            incomplete.append(repo)
    if incomplete:
        raise SystemExit("Publication enrichment is still pending (retry state retained): " + ", ".join(incomplete))


def check_publishable(state, projects, catalogue=None):
    if catalogue is not None:
        current = {p["id"]: material(p) for p in projects}
        previous = {pid: material(p) for pid, p in catalogue.get("projects", {}).items()}
        if current != previous:
            raise SystemExit("Catalogue changes must be refreshed and recorded before deploying")
    tracked = {repository(project) for project in projects}
    pending = sorted(repo for repo, rs in state.get("repositories", {}).items()
                     if repo in tracked and pending_publication(rs))
    if pending:
        raise SystemExit("Publication enrichment must finish before deploying: " + ", ".join(pending))


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def select_base(event_name, event, base="", head=""):
    if base or head:
        if event_name != "workflow_dispatch" or not base or not head:
            raise ValueError("Publication dispatch requires both publication_base and publication_head")
        return base, head
    if event_name == "push":
        return event["before"], event["after"]
    return None, None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check-complete", action="store_true")
    parser.add_argument("--check-publishable", action="store_true")
    args = parser.parse_args()
    if args.check_publishable:
        check_publishable(json.loads(STATE.read_text(encoding="utf-8")),
                          json.loads(PROJECTS.read_text(encoding="utf-8")),
                          json.loads(CATALOGUE.read_text(encoding="utf-8")))
        return
    filename = os.environ.get("GITHUB_REFRESH_SCOPE_FILE")
    if not filename:
        raise SystemExit("GITHUB_REFRESH_SCOPE_FILE must name a runner-temporary manifest")
    if args.check_complete:
        check_complete(load_scope(), json.loads(STATE.read_text(encoding="utf-8")))
        return
    event_path = os.environ.get("GITHUB_EVENT_PATH")
    event = json.loads(Path(event_path).read_text()) if event_path else {}
    base, head = select_base(os.environ.get("GITHUB_EVENT_NAME", ""), event,
                             os.environ.get("PUBLICATION_BASE", ""), os.environ.get("PUBLICATION_HEAD", ""))
    current = json.loads(PROJECTS.read_text(encoding="utf-8"))
    catalogue = json.loads(CATALOGUE.read_text(encoding="utf-8")) if CATALOGUE.exists() else {"projects": {}}
    outstanding = catalogue_delta(list(catalogue.get("projects", {}).values()), current)
    if base is None:
        scope = {"mode": "adaptive", "publication": outstanding}
    else:
        if not all(re.fullmatch(r"[0-9a-fA-F]{40}", value) for value in (base, head)):
            raise ValueError("Publication revisions must be full commit SHAs")
        git("merge-base", "--is-ancestor", head, "HEAD")
        if set(base) == {"0"}:
            before = []  # The initial push has no previous catalogue.
        else:
            git("merge-base", "--is-ancestor", base, head)
            before = (json.loads(git("show", f"{base}:data/projects.json"))
                      if git("ls-tree", "--name-only", base, "--", "data/projects.json") else [])
        scope = union_catalogue_deltas(catalogue_delta(before, current), outstanding)
        scope.update({"base": base, "head": head})
    Path(filename).write_text(json.dumps(scope, indent=2) + "\n", encoding="utf-8")
    work = scope.get("publication", scope)
    print("Refresh scope: " + scope["mode"] + "; " + str(len(work.get("repositories", []))) + " publication repositories")


if __name__ == "__main__":
    main()
