#!/usr/bin/env python3
"""Collect cheap directory inventory, README or landing-page hints for queued GitHub leads.

This read-only preflight makes no qualification, build or provenance decision.
It uses at most two GitHub API calls per candidate and preserves queue order.
"""
from __future__ import annotations

import argparse
import base64
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
from urllib.parse import quote, urlsplit

from discovery_intake import HTTPClient, LinkParser, STATE, github_candidate
from screen_discovery_candidates import github_repository_key


SOURCE_EXT = {".asm", ".s", ".6502", ".c", ".cpp", ".go", ".py", ".ts", ".js", ".v", ".sv", ".vhd"}
BINARY_EXT = {".rom", ".bin", ".adf", ".dsk", ".prg", ".tos", ".jed", ".ssd", ".uef", ".exe", ".vsix"}
RELEASE_EXT = {".ssd", ".uef", ".exe", ".vsix"}
DESIGN_EXT = {".kicad_sch", ".kicad_pcb", ".lib", ".pld"}
WORKBOOK_EXT = {".xlsm", ".xlsx", ".ods"}
BUILD_NAMES = {"makefile", "cmakelists.txt", "build.sh", "build.bat", "package.json"}
GITHUB_REPO_URL = re.compile(r"https?://(?:www\.)?github\.com/[\w.-]+/[\w.-]+", re.I)


def inventory(items: list[dict]) -> dict:
    """Return root-file observations, never an inclusion or exclusion verdict."""
    names = [item["name"] for item in items if item.get("type") in {"file", "dir"} and item.get("name")]
    files = [item["name"] for item in items if item.get("type") == "file" and item.get("name")]
    dirs = [item["name"] for item in items if item.get("type") == "dir" and item.get("name")]
    readmes = [name for name in files if re.match(r"^readme(?:\.[^.]+){0,2}$", name, re.I)]
    # A translated README may sort before the English root README in GitHub's listing.
    readme = min(readmes, key=lambda name: (0 if name.casefold() == "readme.md" else
                                            1 if name.casefold() == "readme.en.md" else 2,
                                            name.casefold())) if readmes else None
    return {
        "root_names": names,
        "readme_path": readme,
        "landing_page_path": next((name for name in files if name.casefold() == "index.html"), None) if not readme else None,
        "root_signals": {
            "source_files": any(Path(name).suffix.casefold() in SOURCE_EXT for name in files),
            "binary_files": any(Path(name).suffix.casefold() in BINARY_EXT for name in files),
            "release_artifacts": [name for name in files if Path(name).suffix.casefold() in RELEASE_EXT],
            "hardware_design_files": any(Path(name).suffix.casefold() in DESIGN_EXT for name in files),
            "analysis_workbooks": [name for name in files if Path(name).suffix.casefold() in WORKBOOK_EXT],
            "build_files": any(name.casefold() in BUILD_NAMES for name in files),
            "source_directories": [name for name in dirs if name.casefold() in
                                   {"src", "source", "sources", "1-source-files", "original-sources"}],
        },
    }


def triage(queue: list, client: HTTPClient, limit: int) -> dict:
    leads = []
    for url, entry in queue[:limit]:
        parsed = urlsplit(url)
        parts = parsed.path.strip("/").split("/")
        row = {"url": url, "score": entry.get("score"), "origins": entry.get("origins", [])}
        nested = len(parts) >= 5 and parts[2] == "tree" and bool(parts[3]) and all(parts[4:])
        if parsed.hostname != "github.com" or not (len(parts) == 2 or nested):
            row["error"] = "Only GitHub repository roots or tree/branch/directory URLs support this preflight"
            leads.append(row)
            continue
        owner, repo = map(quote, parts[:2])
        directory = "/".join(parts[4:]) if nested else ""
        branch = parts[3] if nested else None
        endpoint = f"https://api.github.com/repos/{owner}/{repo}/contents"
        if directory:
            endpoint += "/" + "/".join(map(quote, parts[4:]))
            row["directory_path"] = directory
            row["ref"] = branch
        suffix = "?ref=" + quote(branch) if branch else ""
        try:
            items = client.get(endpoint + suffix)
            if not isinstance(items, list):
                raise ValueError("Repository root is not a directory listing")
            row.update(inventory(items))
            page_path = row["readme_path"] or row["landing_page_path"]
            if page_path:
                page = client.get(endpoint + "/" + quote(page_path) + suffix)
                body = base64.b64decode(page["content"]).decode("utf-8", errors="replace")
            if row["readme_path"]:
                row["readme_intro"] = body.lstrip()[:1000]
                row["readme_url"] = page.get("html_url")
                own_repo = github_repository_key(url)
                related = []
                seen = {own_repo.casefold()}
                for link in GITHUB_REPO_URL.findall(body):
                    root = github_repository_key(github_candidate(link.rstrip(".,;:!?")) or "")
                    if root and root.casefold() not in seen:
                        related.append(root)
                        seen.add(root.casefold())
                row["related_repository_count"] = len(related)
                row["related_repositories"] = related[:20]
            elif row["landing_page_path"]:
                parser = LinkParser()
                parser.feed(body)
                repositories = list(dict.fromkeys(filter(None, (github_repository_key(github_candidate(link) or "")
                                                           for link in parser.links))))
                row["landing_page_url"] = page.get("html_url")
                row["outbound_repository_count"] = len(repositories)
                row["outbound_repositories"] = repositories[:50]
        except (RuntimeError, ValueError, KeyError, UnicodeError) as exc:
            row["error"] = str(exc)
            if client.count >= client.max_requests:
                leads.append(row)
                break
        leads.append(row)
    return {"generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "scope": "Repository root or tree directory; signals are observations, not catalogue decisions",
            "requests": client.count, "leads": leads}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=STATE,
                        help="Intake state or fixed queue snapshot (default: saved state)")
    parser.add_argument("--limit", type=int, default=15, help="1–30 leads (at most two calls each)")
    parser.add_argument("--output", type=Path, help="Write JSON preflight report; default stdout")
    args = parser.parse_args()
    if not 1 <= args.limit <= 30:
        parser.error("--limit must be between 1 and 30")
    data = json.loads(args.input.read_text(encoding="utf-8"))
    queue = list(data["queue"].items()) if isinstance(data, dict) else data
    client = HTTPClient(os.environ.get("GITHUB_TOKEN", ""), delay=0.5, max_requests=2 * args.limit)
    report = triage(queue, client, args.limit)
    content = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(content, encoding="utf-8")
    else:
        print(content, end="")


if __name__ == "__main__":
    main()
