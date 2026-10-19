#!/usr/bin/env python3
"""One material-publication decision shared by collectors and serialized Pages.

The deployment environment is the successful-publication receipt, not a second
writable catalogue. Requests are wake-ups: every admission reads latest main.
https://docs.github.com/en/rest/deployments/deployments#list-deployments
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import time

from catalogue_storage import load_git_dataset, load_git_projects
from refresh_scope import check_publishable

COLLECTORS = {
    ".github/workflows/apply-research.yml": "Publish reviewed research atomically",
    ".github/workflows/refresh-github.yml": "Publish results and refresh progress atomically",
    ".github/workflows/publish-enrichment.yml": "Publish retained evidence and progress together",
}
GENERATORS = (
    "tools/build_site.py",
    "tools/generate_rss.py",
    "tools/generate_recent_activity.py",
    "tools/activity_history.py",
    "tools/catalogue_storage.py",
)


def git(root, *args):
    return subprocess.check_output(["git", *args], cwd=root, timeout=60).decode().strip()


def revision(root, ref):
    sha = git(root, "rev-parse", "--verify", ref + "^{commit}")
    if not re.fullmatch("[0-9a-f]{40}", sha):
        raise ValueError("Invalid publication revision")
    return sha


def blob(root, sha, name):
    return subprocess.check_output(["git", "show", f"{sha}:{name}"], cwd=root, timeout=30)


def document(root, sha, name):
    return json.loads(blob(root, sha, name))


def fingerprint(root, sha):
    """Hash public facts/assets/build inputs, excluding collection-only clocks.

    Logical partition reads ignore byte formatting, shard routing and digest
    changes caused solely by checked_at. All other tracked public files count.
    """
    projects = load_git_projects(sha, cwd=root)
    for project in projects:
        (project.get("github") or {}).pop("checked_at", None)
    activity = document(root, sha, "data/activity.json")
    activity.pop("generated_at", None)
    value = {
        "projects": projects,
        "activity": activity,
        "audits": load_git_dataset(sha, "project-audits.json", cwd=root),
        "files": {},
    }
    names = git(
        root, "ls-tree", "-r", "--name-only", sha, "--", "index.html", "web", "data", *GENERATORS
    ).splitlines()
    for name in names:
        if name in {
            "data/activity.json",
            "data/projects.json",
            "data/projects.index.json",
            "data/project-audits.json",
            "data/project-audits.index.json",
        } or name.startswith(("data/projects/", "data/project-audits/")):
            continue
        content = blob(root, sha, name)
        # JSON key ordering/indentation is not a new public fact.
        value["files"][name] = (
            json.loads(content)
            if name.startswith("data/") and name.endswith(".json")
            else hashlib.sha256(content).hexdigest()
        )
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"), allow_nan=False).encode()
    ).hexdigest()


def publishable(root, sha):
    try:
        if document(root, sha, "data/pending-projects.json"):
            return False
        check_publishable(
            document(root, sha, "state/github-poll-state.json"),
            load_git_projects(sha, cwd=root),
            document(root, sha, "state/project-catalog-state.json"),
        )
    except SystemExit:
        return False
    return True


class GitHub:
    def __init__(self, repo=None):
        self.repo = repo or os.environ["GITHUB_REPOSITORY"]
        if not re.fullmatch(r"[\w.-]+/[\w.-]+", self.repo):
            raise ValueError("Invalid repository")

    def get(self, endpoint):
        value = subprocess.check_output(
            ["gh", "api", "-X", "GET", f"repos/{self.repo}/{endpoint}"], timeout=30
        )
        return json.loads(value)

    def deployed(self):
        # An unsuccessful newer attempt must never become the baseline.
        # Gate/reconcile jobs have no environment, so no-op requests create no
        # successful environment deployment rows of their own.
        for page in range(1, 21):
            rows = self.get(f"deployments?environment=github-pages&per_page=100&page={page}")
            for row in sorted(rows, key=lambda r: r["id"], reverse=True):
                statuses = self.get(f"deployments/{row['id']}/statuses?per_page=1")
                if statuses and statuses[0]["state"] == "success":
                    sha = row["sha"]
                    if not re.fullmatch("[0-9a-f]{40}", sha):
                        raise ValueError("Invalid successful deployment SHA")
                    return sha
            if len(rows) < 100:
                return None
        raise RuntimeError("No successful deployment in bounded history; investigate before publishing")

    def collecting(self, snapshot):
        rows = self.get("actions/runs?status=in_progress&branch=main&per_page=100")["workflow_runs"]
        current = os.environ.get("GITHUB_RUN_ID")
        for run in rows:
            path = run.get("path", "").split("@", 1)[0]
            if path not in COLLECTORS or str(run["id"]) == current or run.get("head_sha") == snapshot:
                continue
            jobs = self.get(f"actions/runs/{run['id']}/jobs?per_page=100")["jobs"]
            for job in jobs:
                if job["name"] not in {"refresh", "enrich", "ingest", "publish"} or job["status"] == "completed":
                    continue
                publication = next((s for s in job.get("steps", []) if s["name"] == COLLECTORS[path]), None)
                # Ignore post-publication notification/continuation steps, so
                # simultaneous finalizers cannot wait on one another forever.
                if publication is None or publication["status"] != "completed":
                    return True
        return False

    def dispatch(self, attempt):
        for retry in range(3):
            result = subprocess.run(
                ["gh", "workflow", "run", "pages.yml", "--ref", "main", "-f", f"attempt={attempt}"],
                timeout=30,
            )
            if result.returncode == 0:
                return
            if retry < 2:
                time.sleep(2 * (retry + 1))
        raise RuntimeError("Pages request failed; hourly reconciliation retains the follow-up")


def decide(*, snapshot, event_sha, digest, deployed_digest, complete, busy):
    result = {"snapshot": snapshot, "fingerprint": digest, "deploy": False, "request": False}
    if not complete:
        result["reason"] = "publication-incomplete"
    elif digest == deployed_digest:
        result["reason"] = "already-deployed"
    elif busy:
        result["reason"] = "collector-publishing"
    elif event_sha and event_sha != snapshot:
        result.update(reason="superseded-request", request=True)
    else:
        result.update(reason="material-publication", deploy=True, request=True)
    return result


def inspect(root, api, event_sha=""):
    git(root, "fetch", "origin", "main")
    snapshot = revision(root, "origin/main")
    complete = publishable(root, snapshot)
    if not complete:
        return decide(
            snapshot=snapshot,
            event_sha=event_sha,
            digest="",
            deployed_digest=None,
            complete=False,
            busy=False,
        )
    digest = fingerprint(root, snapshot)
    deployed = api.deployed()
    old_digest = fingerprint(root, revision(root, deployed)) if deployed else None
    return decide(
        snapshot=snapshot,
        event_sha=event_sha,
        digest=digest,
        deployed_digest=old_digest,
        complete=True,
        busy=False if old_digest == digest else api.collecting(snapshot),
    )


def request(root, api, *, failure=False, attempt=0, failed_digest=""):
    result = inspect(root, api)
    result["requested"] = False
    if result["request"]:
        next_attempt = (
            attempt + 1 if failure and (not failed_digest or result["fingerprint"] == failed_digest) else 0
        )
        if next_attempt > 2:
            result.update(request=False, reason="retry-limit")
        else:
            api.dispatch(next_attempt)
            result.update(requested=True, attempt=next_attempt)
    return result


def output(result):
    print(json.dumps(result, separators=(",", ":")), flush=True)
    if filename := os.environ.get("GITHUB_OUTPUT"):
        with open(filename, "a") as handle:
            for key in ("deploy", "snapshot", "fingerprint"):
                handle.write(
                    f'{key}={str(result.get(key, "")).lower() if key == "deploy" else result.get(key, "")}\n'
                )
    if filename := os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(filename, "a") as handle:
            handle.write("Pages publication: `" + json.dumps(result, separators=(",", ":")) + "`\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("gate", "request", "verify"))
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--snapshot", default="")
    parser.add_argument("--attempt", type=int, choices=range(3), default=0)
    parser.add_argument("--failure", action="store_true")
    parser.add_argument("--failed-digest", default="")
    args = parser.parse_args()
    if args.command == "verify":
        if (
            args.snapshot != os.environ.get("GITHUB_SHA")
            or revision(args.root, "HEAD") != args.snapshot
            or not publishable(args.root, args.snapshot)
        ):
            raise SystemExit("Refusing mismatched or incomplete deployment snapshot")
        return
    api = GitHub()
    if args.command == "gate":
        result = inspect(args.root, api, os.environ["GITHUB_SHA"])
    else:
        result = request(
            args.root, api, failure=args.failure, attempt=args.attempt, failed_digest=args.failed_digest
        )
    output(result)


if __name__ == "__main__":
    main()
