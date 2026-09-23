#!/usr/bin/env python3
"""Refresh objective GitHub metadata for tracked projects.

Only GitHub-observable facts are automated. Curated reverse-engineering
judgements (true project start date, playability, byte exactness, etc.) are not
inferred from repository metadata.
"""
from __future__ import annotations

import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import quote
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "projects.json"
API = "https://api.github.com"
TOKEN = os.environ.get("GITHUB_TOKEN", "")
TODAY = datetime.now(timezone.utc).date()

AI_PATTERNS = [
    (re.compile(r"co-authored-by:.*\bclaude\b", re.I), "Claude"),
    (re.compile(r"co-authored-by:.*\banthropic\b", re.I), "Claude"),
    (re.compile(r"co-authored-by:.*\bchatgpt\b", re.I), "ChatGPT"),
    (re.compile(r"co-authored-by:.*\bopenai\b", re.I), "ChatGPT"),
    (re.compile(r"co-authored-by:.*\bcopilot\b", re.I), "GitHub Copilot"),
    (re.compile(r"co-authored-by:.*\bgemini\b", re.I), "Gemini"),
]

CACHE = {}

def api(path: str, allow_404: bool = False):
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "legacy-reverse-engineering-tracker",
        "X-GitHub-Api-Version": "2026-03-10",
    }
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    request = Request(API + path, headers=headers)
    try:
        with urlopen(request, timeout=30) as response:
            return json.load(response)
    except HTTPError as exc:
        if allow_404 and exc.code == 404:
            return None
        body = exc.read().decode("utf-8", "replace")
        raise RuntimeError(f"GitHub API {exc.code} for {path}: {body[:500]}") from exc

def cached(key, path, allow_404=False):
    if key not in CACHE:
        CACHE[key] = api(path, allow_404=allow_404)
    return CACHE[key]

def github_repo(url):
    match = re.fullmatch(r"https?://github\.com/([^/]+)/([^/#?]+?)(?:\.git)?/?", url or "")
    return f"{match.group(1)}/{match.group(2)}" if match else None

def iso_date(value):
    return value[:10] if value else None

def activity_state(date_string):
    if not date_string:
        return None
    then = datetime.strptime(date_string[:10], "%Y-%m-%d").date()
    days = (TODAY - then).days
    if days <= 90:
        return "active"
    if days <= 365:
        return "recent"
    if days <= 730:
        return "quiet"
    return "dormant"

def repo_context(full_name, branch):
    info = cached(("repo", full_name), f"/repos/{full_name}")
    languages = cached(("languages", full_name), f"/repos/{full_name}/languages") or {}
    root = cached(
        ("root", full_name, branch),
        f"/repos/{full_name}/contents?ref={quote(branch)}",
        allow_404=True,
    ) or []
    github_entries = []
    if any(
        isinstance(entry, dict)
        and entry.get("name") == ".github"
        and entry.get("type") == "dir"
        for entry in root
    ):
        github_entries = cached(
            ("dotgithub", full_name, branch),
            f"/repos/{full_name}/contents/.github?ref={quote(branch)}",
            allow_404=True,
        ) or []
    return info, languages, root, github_entries

def detect_ai(record, commits, root_entries, github_entries):
    ai = record.setdefault("ai", {"usage": None, "tools": []})
    tools = set(ai.get("tools") or [])
    evidence = []

    root_names = {entry.get("name", "").lower() for entry in root_entries if isinstance(entry, dict)}
    github_names = {entry.get("name", "").lower() for entry in github_entries if isinstance(entry, dict)}

    if "claude.md" in root_names or ".claude" in root_names:
        tools.add("Claude")
        evidence.append("Claude project instructions/configuration present")
    if "copilot-instructions.md" in github_names:
        tools.add("GitHub Copilot")
        evidence.append(".github/copilot-instructions.md present")
    if "codex.md" in root_names:
        tools.add("OpenAI Codex")
        evidence.append("CODEX.md present in repository root")

    hits = {}
    example = {}
    for commit in commits:
        message = ((commit.get("commit") or {}).get("message") or "")
        matched_tools = {tool for pattern, tool in AI_PATTERNS if pattern.search(message)}
        for tool in matched_tools:
            tools.add(tool)
            hits[tool] = hits.get(tool, 0) + 1
            example.setdefault(tool, commit.get("sha", "")[:12])

    for tool, count in sorted(hits.items()):
        evidence.append(
            f"{tool} co-author trailer in {count} of the latest {len(commits)} checked commits"
            f" (example {example[tool]})"
        )

    if tools:
        ai["usage"] = True
        ai["tools"] = sorted(tools)
        ai["evidence"] = evidence
    elif ai.get("usage") is not True:
        ai["tools"] = ai.get("tools") or []
        ai.pop("evidence", None)

def refresh(record):
    full_name = github_repo(record.get("repo"))
    if not full_name:
        return False

    base_info = cached(("repo", full_name), f"/repos/{full_name}")
    default_branch = base_info.get("default_branch") or "main"
    branch = record.get("github_branch") or default_branch
    project_path = record.get("github_path")

    info, languages, root_entries, github_entries = repo_context(full_name, branch)

    commit_query = f"/repos/{full_name}/commits?sha={quote(branch)}&per_page=100"
    if project_path:
        commit_query += f"&path={quote(project_path, safe='/')}"
    commits = api(commit_query) or []

    latest = commits[0] if commits else None
    commit_data = (latest or {}).get("commit") or {}
    commit_date = (
        (commit_data.get("committer") or {}).get("date")
        or (commit_data.get("author") or {}).get("date")
    )
    last_activity = iso_date(commit_date)
    if not last_activity and not project_path:
        last_activity = iso_date(info.get("pushed_at"))

    gh = record.setdefault("github", {})
    gh.update({
        "repository": full_name,
        "created_at": iso_date(info.get("created_at")),
        "pushed_at": iso_date(info.get("pushed_at")),
        "updated_at": iso_date(info.get("updated_at")),
        "checked_at": TODAY.isoformat(),
        "default_branch": default_branch,
        "tracking_branch": branch,
        "tracking_path": project_path,
        "archived": bool(info.get("archived")),
        "fork": bool(info.get("fork")),
        "primary_language": info.get("language"),
        "languages": [
            name for name, _ in sorted(
                languages.items(), key=lambda item: item[1], reverse=True
            )
        ],
        "activity_state": activity_state(last_activity),
    })

    if latest:
        gh["latest_commit"] = {
            "sha": latest.get("sha"),
            "date": iso_date(commit_date),
            "message": (commit_data.get("message") or "").splitlines()[0],
            "url": latest.get("html_url"),
        }
    else:
        gh.pop("latest_commit", None)

    # Releases are repository-wide and may be misleading for subprojects.
    if not project_path:
        release = cached(
            ("release", full_name),
            f"/repos/{full_name}/releases/latest",
            allow_404=True,
        )
        if release:
            gh["latest_release"] = {
                "tag": release.get("tag_name"),
                "name": release.get("name"),
                "published_at": iso_date(release.get("published_at")),
                "url": release.get("html_url"),
            }
        else:
            gh.pop("latest_release", None)
    else:
        gh.pop("latest_release", None)

    if last_activity:
        record["last_activity"] = last_activity

    detect_ai(record, commits, root_entries, github_entries)
    return True

def main():
    records = json.loads(DATA.read_text(encoding="utf-8"))
    refreshed = 0
    failures = []

    for index, record in enumerate(records, 1):
        try:
            if refresh(record):
                refreshed += 1
                print(f"[{index}/{len(records)}] refreshed {record['title']}")
        except Exception as exc:
            failures.append((record.get("title", record.get("id")), str(exc)))
            print(f"WARNING: {record.get('title')}: {exc}", file=sys.stderr)
        time.sleep(0.03)

    records.sort(key=lambda r: ((r.get("title") or "").casefold(), r.get("id") or ""))
    DATA.write_text(
        json.dumps(records, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    print(f"Refreshed {refreshed} GitHub-backed records; {len(failures)} failures.")
    for title, error in failures:
        print(f"  - {title}: {error}", file=sys.stderr)

    if failures and refreshed == 0:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
