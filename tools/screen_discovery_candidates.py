#!/usr/bin/env python3
"""Screen discovery URLs against the current catalogue and research decisions.

Accept URLs as arguments, one URL per line from --input, or a JSON array of
URLs / {"url": ..., "route": ...} objects. This command makes no network
requests and never changes the research indexes.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import json
from pathlib import Path
import sys
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[1]
TRACKING_PARAMETERS = {"fbclid", "gclid", "mc_cid", "mc_eid"}


def canonical_url(value: str) -> str:
    """Normalize URL syntax without collapsing distinct repository paths."""
    parts = urlsplit(value.strip())
    if parts.scheme.lower() not in {"http", "https"} or not parts.hostname:
        raise ValueError(f"Expected an absolute HTTP(S) URL: {value!r}")
    if parts.username or parts.password:
        raise ValueError(f"Credentials are not allowed in a discovery URL: {value!r}")
    try:
        port = parts.port
    except ValueError as exc:
        raise ValueError(f"Invalid port in discovery URL: {value!r}") from exc
    host = parts.hostname.lower()
    if host == "www.github.com":
        host = "github.com"
    if port and not (parts.scheme.lower() == "http" and port == 80 or
                     parts.scheme.lower() == "https" and port == 443):
        host += f":{port}"
    path = parts.path.rstrip("/")
    if host == "github.com":
        segments = path.split("/")
        if len(segments) >= 3 and segments[1] and segments[2]:
            segments[1] = segments[1].casefold()
            segments[2] = segments[2].removesuffix(".git").casefold()
            path = "/".join(segments)
        elif len(segments) >= 2:
            segments[1] = segments[1].casefold()
            path = "/".join(segments)
    query = urlencode(sorted((k, v) for k, v in parse_qsl(parts.query, keep_blank_values=True)
                             if not k.lower().startswith("utm_") and k.lower() not in TRACKING_PARAMETERS))
    # GitHub serves the same repository over HTTP and HTTPS; other hosts may
    # use scheme-dependent endpoints, so preserve their original scheme.
    scheme = "https" if host == "github.com" else parts.scheme.lower()
    return urlunsplit((scheme, host, path, query, ""))


def github_repository_key(url: str) -> str | None:
    parts = urlsplit(url)
    segments = parts.path.strip("/").split("/")
    if parts.hostname == "github.com" and len(segments) >= 2 and all(segments[:2]):
        return f"https://github.com/{segments[0]}/{segments[1]}"
    return None


class CandidateIndex:
    def __init__(self, data_dir: Path):
        self.exact = defaultdict(list)
        self.repositories = defaultdict(list)
        self.repository_branches = defaultdict(set)
        self.project_urls = {}
        projects = json.loads((data_dir / "projects.json").read_text(encoding="utf-8"))
        discovery = json.loads((data_dir / "discovery-sources.json").read_text(encoding="utf-8"))
        decisions = json.loads((data_dir / "discovery-decisions.json").read_text(encoding="utf-8"))

        for project in projects:
            url = project.get("project_url") or project.get("repo")
            if url:
                self.project_urls[project["id"]] = url
                self.add(url, {"kind": "project", "id": project["id"], "url": url})
            repo = project.get("repo")
            if repo:
                key = github_repository_key(canonical_url(repo))
                if key:
                    self.repositories[key].append({"kind": "project", "id": project["id"], "url": repo})
                    branch = (project.get("github") or {}).get("default_branch")
                    if branch:
                        self.repository_branches[key].add(branch)
        for source in discovery["sources"]:
            url = source["source"]
            # Some source nodes are names or descriptions rather than URLs.
            if url.startswith(("https://", "http://")):
                self.add(url, {"kind": "source", "id": source["id"],
                               "review_state": source["review_state"], "url": url})
        for decision in decisions["decisions"]:
            url = decision["url"]
            self.add(url, {"kind": "decision", "id": decision["id"],
                           "decision": decision["decision"], "project_ids": decision.get("project_ids", []),
                           "url": url})

    def add(self, url: str, match: dict) -> None:
        self.exact[canonical_url(url)].append(match)

    def screen(self, url: str) -> dict:
        try:
            key = canonical_url(url)
        except ValueError as exc:
            return {"url": url, "status": "invalid", "reason": str(exc), "matches": []}
        matches = self.exact.get(key, [])
        kinds = {match["kind"] for match in matches}
        if "decision" in kinds:
            status = "reviewed_decision"
        elif "project" in kinds:
            status = "tracked_project"
        elif "source" in kinds:
            status = "known_source"
        else:
            repo_key = github_repository_key(key)
            matches = self.repositories.get(repo_key, []) if repo_key else []
            status = ("known_repository" if repo_key == key else "known_repository_path") if matches else "new"
        result = {"url": url, "canonical_url": key, "status": status, "matches": matches}
        targets = sorted({self.project_urls[project_id]
                          for match in matches if match["kind"] == "decision"
                          for project_id in match.get("project_ids", [])
                          if project_id in self.project_urls})
        if targets:
            result["target_project_urls"] = targets
        return result


def screen_batch(index: CandidateIndex, candidates: list[dict]) -> dict:
    results = []
    seen = {}
    routes = defaultdict(Counter)
    for candidate in candidates:
        result = index.screen(candidate["url"])
        route = candidate.get("route") or "unspecified"
        result["route"] = route
        key = result.get("canonical_url")
        if key and key in seen:
            result["status"] = "repeat_in_batch"
            result["first_seen_at"] = seen[key]
        elif key:
            seen[key] = len(results)
        routes[route][result["status"]] += 1
        results.append(result)
    return {"summary": {"total": len(results), "unique_urls": len(seen),
                        "by_route": {route: dict(counts) for route, counts in sorted(routes.items())}},
            "results": results}


def read_candidates(path: str, route: str) -> list[dict]:
    content = sys.stdin.read() if path == "-" else Path(path).read_text(encoding="utf-8")
    if content.lstrip().startswith("["):
        raw = json.loads(content)
        if not isinstance(raw, list):
            raise ValueError("Input JSON must be an array")
    else:
        raw = [line.strip() for line in content.splitlines() if line.strip() and not line.lstrip().startswith("#")]
    candidates = [({"url": item, "route": route} if isinstance(item, str) else item) for item in raw]
    if any(not isinstance(item, dict) or not isinstance(item.get("url"), str) or
           not isinstance(item.get("route", route), str) for item in candidates):
        raise ValueError("Candidates must be URLs or objects with string url and route fields")
    return candidates


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("urls", nargs="*", help="Candidate URLs to screen")
    parser.add_argument("--input", metavar="PATH", help="Newline/JSON candidate file, or - for stdin")
    parser.add_argument("--route", default="unspecified", help="Search route for command-line/newline URLs")
    parser.add_argument("--data-dir", type=Path, default=ROOT / "data", help=argparse.SUPPRESS)
    parser.add_argument("--json", action="store_true", help="Machine-readable results and route counts")
    args = parser.parse_args()
    if not args.urls and not args.input:
        parser.error("Provide URLs or --input")
    try:
        candidates = read_candidates(args.input, args.route) if args.input else []
        candidates.extend({"url": url, "route": args.route} for url in args.urls)
        report = screen_batch(CandidateIndex(args.data_dir), candidates)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        parser.error(str(exc))
    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        for result in report["results"]:
            identities = ", ".join(
                f"{m['kind']}:{m.get('decision', m.get('review_state', m['id']))}:{m['id']}"
                if m["kind"] != "project" else f"project:{m['id']}"
                for m in result["matches"])
            targets = ", ".join(result.get("target_project_urls", []))
            print(f"{result['status']:23} {result['url']}" + (f"  [{identities}]" if identities else "") +
                  (f"  -> {targets}" if targets else ""))
        for route, counts in report["summary"]["by_route"].items():
            print(f"{route}: " + ", ".join(f"{name}={count}" for name, count in sorted(counts.items())))


if __name__ == "__main__":
    main()
