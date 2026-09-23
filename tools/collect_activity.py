#!/usr/bin/env python3
"""Collect recent commit activity for tracked GitHub projects.

The activity feed is a rolling 180-day snapshot. Commits are collected from
all branches with activity inside that window, plus explicitly tracked/default
branches. Shared repositories use each project's github_path for attribution.
"""
from __future__ import annotations

import json
import os
import re
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = ROOT / "data" / "projects.json"
ACTIVITY = ROOT / "data" / "activity.json"
API = "https://api.github.com"
TOKEN = os.environ.get("GITHUB_TOKEN", "")
NOW = datetime.now(timezone.utc)
DAYS = 180
SINCE = NOW - timedelta(days=DAYS)
SINCE_ISO = SINCE.isoformat(timespec="seconds").replace("+00:00", "Z")
MAX_BRANCHES_PER_REPO = 40

def api(path, allow_404=False):
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "legacy-reverse-engineering-tracker",
        "X-GitHub-Api-Version": "2026-03-10",
    }
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    try:
        with urlopen(Request(API + path, headers=headers), timeout=30) as response:
            return json.load(response)
    except HTTPError as exc:
        if allow_404 and exc.code == 404:
            return None
        body = exc.read().decode("utf-8", "replace")
        raise RuntimeError(f"GitHub API {exc.code} for {path}: {body[:300]}") from exc

def github_repo(url):
    match = re.fullmatch(r"https?://github\.com/([^/]+)/([^/#?]+?)(?:\.git)?/?", url or "")
    return f"{match.group(1)}/{match.group(2)}" if match else None

def commit_date(item):
    commit = item.get("commit") or {}
    return ((commit.get("committer") or {}).get("date")
            or (commit.get("author") or {}).get("date"))

def list_branches(repo):
    branches = []
    for page in range(1, 4):
        chunk = api(f"/repos/{repo}/branches?per_page=100&page={page}") or []
        branches.extend(chunk)
        if len(chunk) < 100:
            break
    return [b.get("name") for b in branches if b.get("name")][:MAX_BRANCHES_PER_REPO]

def commits(repo, branch, path=None, per_page=100):
    params = {"sha": branch, "since": SINCE_ISO, "per_page": per_page}
    if path:
        params["path"] = path
    result = []
    for page in range(1, 4):
        params["page"] = page
        chunk = api(f"/repos/{repo}/commits?{urlencode(params)}", allow_404=True) or []
        result.extend(chunk)
        if len(chunk) < per_page:
            break
    return result

def main():
    projects = json.loads(PROJECTS.read_text(encoding="utf-8"))
    by_repo = {}
    for project in projects:
        repo = github_repo(project.get("repo"))
        if repo:
            by_repo.setdefault(repo, []).append(project)

    events = {}
    failures = []

    for repo_index, (repo, repo_projects) in enumerate(sorted(by_repo.items()), 1):
        try:
            info = api(f"/repos/{repo}")
            default = info.get("default_branch") or "main"
            explicit = {p.get("github_branch") for p in repo_projects if p.get("github_branch")}
            branch_names = list_branches(repo)
            for required in {default, *explicit}:
                if required and required not in branch_names:
                    branch_names.append(required)

            active_branches = []
            repo_commits = {}
            for branch in branch_names:
                recent = commits(repo, branch)
                repo_commits[branch] = recent
                if recent or branch == default or branch in explicit:
                    active_branches.append(branch)
                time.sleep(0.02)

            print(f"[{repo_index}/{len(by_repo)}] {repo}: {len(active_branches)} active branches")

            for project in repo_projects:
                path = project.get("github_path")
                tracked_branch = project.get("github_branch")
                candidate_branches = active_branches
                if tracked_branch:
                    candidate_branches = [b for b in active_branches if b == tracked_branch]

                for branch in candidate_branches:
                    items = commits(repo, branch, path) if path else repo_commits.get(branch, [])
                    for item in items:
                        sha = item.get("sha")
                        date = commit_date(item)
                        if not sha or not date:
                            continue
                        key = (project["id"], repo, sha)
                        commit = item.get("commit") or {}
                        author = item.get("author") or {}
                        commit_author = commit.get("author") or {}
                        event = events.get(key)
                        if not event:
                            message = commit.get("message") or ""
                            event = {
                                "type": "commit",
                                "date": date,
                                "project_id": project["id"],
                                "repository": repo,
                                "sha": sha,
                                "title": message.splitlines()[0] if message else sha[:12],
                                "message": message,
                                "url": item.get("html_url"),
                                "author": author.get("login") or commit_author.get("name"),
                                "branches": [],
                            }
                            events[key] = event
                        if branch not in event["branches"]:
                            event["branches"].append(branch)
                    time.sleep(0.02)
        except Exception as exc:
            failures.append((repo, str(exc)))
            print(f"WARNING: {repo}: {exc}")

    output = sorted(events.values(), key=lambda e: (e["date"], e["repository"], e["sha"]), reverse=True)
    for event in output:
        event["branches"].sort()

    payload = {
        "generated_at": NOW.isoformat(timespec="seconds").replace("+00:00", "Z"),
        "window_days": DAYS,
        "events": output,
    }
    ACTIVITY.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(output)} attributed commit events from {len(by_repo)} repositories.")
    if failures:
        print(f"{len(failures)} repositories failed; retained activity is partial.")

if __name__ == "__main__":
    main()
