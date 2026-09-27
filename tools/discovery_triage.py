#!/usr/bin/env python3
"""Collect cheap root inventory and README hints for queued GitHub leads.

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

from discovery_intake import HTTPClient, STATE


SOURCE_EXT = {".asm", ".s", ".6502", ".c", ".cpp", ".go", ".py", ".ts", ".js", ".v", ".sv", ".vhd"}
BINARY_EXT = {".rom", ".bin", ".adf", ".dsk", ".prg", ".tos", ".jed", ".ssd", ".uef", ".exe", ".vsix"}
RELEASE_EXT = {".ssd", ".uef", ".exe", ".vsix"}
DESIGN_EXT = {".kicad_sch", ".kicad_pcb", ".lib", ".pld"}
BUILD_NAMES = {"makefile", "cmakelists.txt", "build.sh", "build.bat", "package.json"}


def inventory(items: list[dict]) -> dict:
    """Return root-file observations, never an inclusion or exclusion verdict."""
    names = [item["name"] for item in items if item.get("type") in {"file", "dir"} and item.get("name")]
    files = [item["name"] for item in items if item.get("type") == "file" and item.get("name")]
    dirs = [item["name"] for item in items if item.get("type") == "dir" and item.get("name")]
    readme = next((name for name in files if re.match(r"^readme(?:\.[^.]+)?$", name, re.I)), None)
    return {
        "root_names": names,
        "readme_path": readme,
        "root_signals": {
            "source_files": any(Path(name).suffix.casefold() in SOURCE_EXT for name in files),
            "binary_files": any(Path(name).suffix.casefold() in BINARY_EXT for name in files),
            "release_artifacts": [name for name in files if Path(name).suffix.casefold() in RELEASE_EXT],
            "hardware_design_files": any(Path(name).suffix.casefold() in DESIGN_EXT for name in files),
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
        if parsed.hostname != "github.com" or len(parts) != 2:
            row["error"] = "Only GitHub repository root URLs support this preflight"
            leads.append(row)
            continue
        owner, repo = map(quote, parts)
        endpoint = f"https://api.github.com/repos/{owner}/{repo}/contents"
        try:
            items = client.get(endpoint)
            if not isinstance(items, list):
                raise ValueError("Repository root is not a directory listing")
            row.update(inventory(items))
            if row["readme_path"]:
                readme = client.get(endpoint + "/" + quote(row["readme_path"]))
                body = base64.b64decode(readme["content"]).decode("utf-8", errors="replace")
                row["readme_intro"] = body.lstrip()[:1000]
                row["readme_url"] = readme.get("html_url")
        except (RuntimeError, ValueError, KeyError, UnicodeError) as exc:
            row["error"] = str(exc)
            if client.count >= client.max_requests:
                leads.append(row)
                break
        leads.append(row)
    return {"generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "scope": "Repository root only; signals are observations, not catalogue decisions",
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
