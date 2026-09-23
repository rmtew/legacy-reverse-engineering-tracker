#!/usr/bin/env python3
"""Enrich unknown project facts from explicit, reviewable GitHub evidence.

This collector is deliberately conservative. It scans project README/status/build
notes and records excerpts for compilability, playability, byte exactness and
explicit project-start dates. It only promotes an unknown field when all strong
matches agree. Generic CI results are recorded as supporting signals but never
used by themselves to claim that a reconstruction compiles or plays.
"""
from __future__ import annotations

import base64
import json
import os
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "projects.json"
API = "https://api.github.com"
TOKEN = os.environ.get("GITHUB_TOKEN", "")
TODAY = datetime.now(timezone.utc).date().isoformat()
COLLECTOR = "github-docs-v1"
MAX_FILE_BYTES = 600_000

CACHE = {}

DOC_NAMES = {
    "readme.md", "readme", "status.md", "status.txt", "build.md",
    "building.md", "build.txt", "notes.md",
}

COMPILE_POSITIVE = [
    re.compile(r"\b(?:the\s+)?(?:game|source|code|disassembly|listing|rom|firmware)\s+(?:now\s+)?(?:compiles|assembles|reassembles)\b", re.I),
    re.compile(r"\b(?:game|project|program|source|code|disassembly|listing|rom|firmware|levels?)\s+(?:can|may)\s+(?:be\s+)?(?:compiled|built|assembled|reassembled)\b", re.I),
    re.compile(r"\b(?:game|program|source|code)\s+to compile and run\b", re.I),
    re.compile(r"\byou can (?:compile|build|assemble|reassemble)(?:\s+and\s+run)?\b", re.I),
    re.compile(r"\b(?:compile|build|assemble|reassemble) and run\b", re.I),
    re.compile(r"\bbuild(?:ing)? the disassembly\b", re.I),
    re.compile(r"\bassemble the game back to a binary\b", re.I),
    re.compile(r"\bre-assemble this code\b", re.I),
]
COMPILE_NEGATIVE = [
    re.compile(r"\b(?:does not|doesn't|cannot|can't)\s+(?:compile|build|assemble|reassemble)\b", re.I),
    re.compile(r"\bnot compilable\b", re.I),
]

PLAYABLE_POSITIVE = [
    re.compile(r"\b(?:build|reconstruction|reconstructed version|prg|binary)\s+(?:is\s+)?playable\b", re.I),
    re.compile(r"\b(?:build|reconstruction|reconstructed version|prg|binary)\s+(?:now\s+)?plays(?:\s+well)?\b", re.I),
    re.compile(r"\b(?:game|source|code)\s+compiles and plays\b", re.I),
    re.compile(r"\bplayable\s+(?:prg|binary|build|reconstruction)\b", re.I),
    re.compile(r"\b(?:reconstructed|rebuilt)\s+(?:game|version|prg|binary)\b[^.\n]{0,80}\bplays\b", re.I),
]
PLAYABLE_NEGATIVE = [
    re.compile(r"\bnot playable\b", re.I),
    re.compile(r"\b(?:game|build|reconstruction|version)\s+(?:does not|doesn't) play\b", re.I),
]

BYTE_POSITIVE = [
    re.compile(r"\b(?:source|disassembly|listing|file)\b[^.\n]{0,100}\breassembl(?:e|es|ed|ing)\b[^.\n]{0,100}\b(?:byte[- ]for[- ]byte identical|byte[- ]identical|byte[- ]exact)\b", re.I),
    re.compile(r"\breassembl(?:e|es|ed|ing)\b[^.\n]{0,100}\b(?:byte[- ]for[- ]byte identical|byte[- ]identical|byte[- ]exact)\b[^.\n]{0,100}\b(?:original|cartridge|rom|binary|executable)\b", re.I),
    re.compile(r"\b(?:rebuilt|reassembled|compiled|generated)\s+(?:binary|rom|snapshot|executable|cartridge)\b[^.\n]{0,100}\b(?:byte[- ]identical|byte[- ]exact|bit[- ]for[- ]bit identical|exactly the same)\b", re.I),
    re.compile(r"\b(?:binary|rom|snapshot|executable|cartridge)\b[^.\n]{0,100}\b(?:byte[- ]identical|byte[- ]exact|bit[- ]for[- ]bit identical)\b[^.\n]{0,100}\boriginal\b", re.I),
    re.compile(r"\bgenerates? (?:the )?exactly same binary as (?:the )?original\b", re.I),
    re.compile(r"\bcmp\b[^.\n]{0,120}\b(?:no output|byte[- ]identical|identical)\b", re.I),
    re.compile(r"\ba byte[- ]exact[^.\n]{0,80}\b(?:reconstruction|reverse engineer|disassembly)\b", re.I),
]
BYTE_NEGATIVE = [
    re.compile(r"\bnot byte[- ](?:exact|identical)\b", re.I),
    re.compile(r"\bnot bit[- ]for[- ]bit\b", re.I),
    re.compile(r"\bdoes not (?:match|reproduce)[^.\n]{0,80}\bexactly\b", re.I),
]
BYTE_GOAL_WORDS = re.compile(
    r"\b(?:goal|aim|target|intended|intention|trying|attempt|want|must|should|planned|plans?)\b",
    re.I,
)

START_PATTERNS = [
    re.compile(r"\b(?:project|work|reverse[- ]engineering|disassembly)\s+(?:was\s+)?(?:started|began|commenced)\s+(?:in\s+)?((?:19|20)\d{2})\b", re.I),
    re.compile(r"\bi started (?:this|the) (?:project|work|reverse[- ]engineering|disassembly)[^0-9\n]{0,40}((?:19|20)\d{2})\b", re.I),
]

CI_NAME = re.compile(r"\b(?:build|test|tests|ci|compile|assemble|verify|verification)\b", re.I)
CI_EXCLUDE = re.compile(r"\b(?:pages?|deploy|deployment|docs?|documentation|website|site|lint|format)\b", re.I)

def api(path, allow_404=False):
    key = (path, allow_404)
    if key in CACHE:
        return CACHE[key]
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "legacy-reverse-engineering-tracker",
        "X-GitHub-Api-Version": "2026-03-10",
    }
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    try:
        with urlopen(Request(API + path, headers=headers), timeout=30) as response:
            value = json.load(response)
    except HTTPError as exc:
        if allow_404 and exc.code in (403, 404):
            value = None
        else:
            body = exc.read().decode("utf-8", "replace")
            raise RuntimeError(f"GitHub API {exc.code} for {path}: {body[:300]}") from exc
    CACHE[key] = value
    return value

def github_repo(url):
    match = re.fullmatch(r"https?://github\.com/([^/]+)/([^/#?]+?)(?:\.git)?/?", url or "")
    return f"{match.group(1)}/{match.group(2)}" if match else None

def contents(repo, path, branch):
    encoded = quote(path, safe="/")
    suffix = f"/{encoded}" if encoded else ""
    return api(f"/repos/{repo}/contents{suffix}?ref={quote(branch)}", allow_404=True)

def read_file(repo, entry, branch):
    if not entry or entry.get("type") != "file" or (entry.get("size") or 0) > MAX_FILE_BYTES:
        return None
    item = contents(repo, entry["path"], branch)
    if not isinstance(item, dict):
        return None
    if item.get("encoding") == "base64" and item.get("content"):
        raw = base64.b64decode(item["content"])
        return raw.decode("utf-8", "replace")
    return None

def clean_excerpt(line):
    line = re.sub(r"<[^>]+>", " ", line)
    line = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", line)
    line = re.sub(r"[#*_\x60>|]", " ", line)
    line = re.sub(r"\s+", " ", line).strip()
    return line[:260]

def matched_excerpt(line, match):
    start = max(0, match.start() - 110)
    end = min(len(line), match.end() + 130)
    prefix = "…" if start else ""
    suffix = "…" if end < len(line) else ""
    return prefix + line[start:end] + suffix

def evidence_entry(value, entry, excerpt, strength="strong"):
    return {
        "value": value,
        "strength": strength,
        "source": entry.get("path"),
        "url": entry.get("html_url"),
        "excerpt": clean_excerpt(excerpt),
        "checked_at": TODAY,
        "collector": COLLECTOR,
    }

def scan_boolean(text, entry, positive, negative, reject_positive=None):
    found = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or len(line) > 1500:
            continue
        for pattern in negative:
            if pattern.search(line):
                found.append(evidence_entry(False, entry, matched_excerpt(line, pattern.search(line))))
                break
        else:
            for pattern in positive:
                if pattern.search(line):
                    if reject_positive and reject_positive.search(line):
                        continue
                    found.append(evidence_entry(True, entry, matched_excerpt(line, pattern.search(line))))
                    break
    return dedupe(found)

def scan_start(text, entry):
    found = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or len(line) > 1500:
            continue
        for pattern in START_PATTERNS:
            match = pattern.search(line)
            if match:
                year = int(match.group(1))
                if 1980 <= year <= datetime.now(timezone.utc).year:
                    found.append(evidence_entry(year, entry, matched_excerpt(line, match)))
                break
    return dedupe(found)

def dedupe(entries):
    seen = set()
    output = []
    for item in entries:
        key = (item["value"], item["source"], item["excerpt"])
        if key not in seen:
            seen.add(key)
            output.append(item)
    return output[:8]

def project_docs(record, repo, branch):
    base = (record.get("github_path") or "").rstrip("/")
    listing = contents(repo, base, branch)
    candidates = []
    if isinstance(listing, list):
        for entry in listing:
            if entry.get("type") == "file" and entry.get("name", "").lower() in DOC_NAMES:
                candidates.append(entry)

    if not base:
        docs_listing = contents(repo, "docs", branch)
        if isinstance(docs_listing, list):
            for entry in docs_listing:
                if entry.get("type") == "file" and entry.get("name", "").lower() in {"readme.md", "status.md", "build.md"}:
                    candidates.append(entry)

    result = []
    for entry in candidates[:6]:
        text = read_file(repo, entry, branch)
        if text:
            result.append((entry, text))
    return result

def resolve_boolean(record, field, evidence):
    values = {item["value"] for item in evidence if item.get("strength") == "strong"}
    if len(values) != 1:
        return False
    build = record.setdefault("build", {})
    if build.get(field) is None:
        build[field] = values.pop()
        return True
    return False

def resolve_start(record, evidence):
    years = {item["value"] for item in evidence if item.get("strength") == "strong"}
    if len(years) == 1 and record.get("re_started") is None:
        record["re_started"] = years.pop()
        return True
    return False

def ci_signals(repo, branch):
    params = urlencode({"branch": branch, "status": "completed", "per_page": 30})
    payload = api(f"/repos/{repo}/actions/runs?{params}", allow_404=True)
    if not isinstance(payload, dict):
        return []
    latest_by_name = {}
    for run in payload.get("workflow_runs", []):
        name = run.get("name") or ""
        if not CI_NAME.search(name) or CI_EXCLUDE.search(name):
            continue
        if name in latest_by_name:
            continue
        latest_by_name[name] = {
            "workflow": name,
            "conclusion": run.get("conclusion"),
            "event": run.get("event"),
            "branch": run.get("head_branch"),
            "url": run.get("html_url"),
            "completed_at": (run.get("updated_at") or "")[:10] or None,
            "checked_at": TODAY,
            "collector": COLLECTOR,
        }
        if len(latest_by_name) >= 5:
            break
    return list(latest_by_name.values())

def enrich(record):
    repo = github_repo(record.get("repo"))
    if not repo:
        return False

    previous_auto = (record.get("evidence") or {}).get("automated") or {}
    previous_applied = previous_auto.get("applied") or {}
    build = record.setdefault("build", {})
    for field, value in previous_applied.items():
        if field == "re_started":
            if record.get("re_started") == value:
                record["re_started"] = None
        elif field in build and build.get(field) == value:
            build[field] = None

    info = api(f"/repos/{repo}")
    default_branch = info.get("default_branch") or "main"
    branch = record.get("github_branch") or default_branch
    docs = project_docs(record, repo, branch)

    auto = {
        "collector": COLLECTOR,
        "checked_at": TODAY,
        "compilable": [],
        "playable": [],
        "byte_exact": [],
        "re_started": [],
        "ci": ci_signals(repo, branch) if not record.get("github_path") else [],
    }

    for entry, text in docs:
        auto["compilable"].extend(scan_boolean(text, entry, COMPILE_POSITIVE, COMPILE_NEGATIVE))
        auto["playable"].extend(scan_boolean(text, entry, PLAYABLE_POSITIVE, PLAYABLE_NEGATIVE))
        auto["byte_exact"].extend(scan_boolean(text, entry, BYTE_POSITIVE, BYTE_NEGATIVE, BYTE_GOAL_WORDS))
        auto["re_started"].extend(scan_start(text, entry))

    for key in ("compilable", "playable", "byte_exact", "re_started"):
        auto[key] = dedupe(auto[key])

    promoted = False
    applied = {}
    if resolve_boolean(record, "compilable", auto["compilable"]):
        promoted = True
        applied["compilable"] = record["build"]["compilable"]
    if resolve_boolean(record, "playable", auto["playable"]):
        promoted = True
        applied["playable"] = record["build"]["playable"]
    if record.setdefault("build", {}).get("playable") is True and record["build"].get("runnable") is None:
        record["build"]["runnable"] = True
        promoted = True
        applied["runnable"] = True
    if resolve_boolean(record, "byte_exact", auto["byte_exact"]):
        promoted = True
        applied["byte_exact"] = record["build"]["byte_exact"]
    if resolve_start(record, auto["re_started"]):
        promoted = True
        applied["re_started"] = record["re_started"]

    if applied:
        auto["applied"] = applied

    has_evidence = any(auto[key] for key in ("compilable", "playable", "byte_exact", "re_started", "ci"))
    evidence = record.setdefault("evidence", {})
    if has_evidence:
        evidence["automated"] = auto
    else:
        evidence.pop("automated", None)
        if not evidence:
            record.pop("evidence", None)
    return promoted

def main():
    records = json.loads(DATA.read_text(encoding="utf-8"))
    processed = 0
    promoted = 0
    failures = []

    for index, record in enumerate(records, 1):
        if not github_repo(record.get("repo")):
            continue
        try:
            changed = enrich(record)
            processed += 1
            if changed:
                promoted += 1
            print(f"[{index}/{len(records)}] evidence {record['title']}")
        except Exception as exc:
            failures.append((record.get("title", record.get("id")), str(exc)))
            print(f"WARNING: {record.get('title')}: {exc}")
        time.sleep(0.02)

    records.sort(key=lambda r: ((r.get("title") or "").casefold(), r.get("id") or ""))
    DATA.write_text(json.dumps(records, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Evidence checked for {processed} GitHub-backed records; promoted fields on {promoted} records; {len(failures)} failures.")

if __name__ == "__main__":
    main()
