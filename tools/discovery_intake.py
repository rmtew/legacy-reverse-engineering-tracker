#!/usr/bin/env python3
"""Collect bounded discovery leads and maintain a screened, ranked review queue.

No project or research decision is made here. Scheduled and chat-driven runs
use the same saved recipes and state; --offline --input imports external hits.
"""
from __future__ import annotations

import argparse
import base64
from collections import Counter, defaultdict
from datetime import datetime, timezone
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import sys
import time
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode, urljoin, urlsplit
from urllib.request import Request, urlopen

from screen_discovery_candidates import CandidateIndex, ROOT, canonical_url, github_repository_key, read_candidates

CONFIG = ROOT / "config" / "discovery-intake.json"
STATE = ROOT / "state" / "discovery-intake.json"
WORK_TERMS = re.compile(r"\b(disassembl\w*|decompil\w*|reassembl\w*|reverse.engineer\w*|"
                        r"reconstruct\w*|debugg\w*|emulat\w*|asset.extract\w*|reimplement\w*)\b", re.I)
PLATFORM_TERMS = re.compile(r"\b(amiga|m68k|68k|68000|\.adf|adf|ocs|ecs|aga|atari[ -]st|"
                            r"tos|commodore[ -]64|c64|amstrad|cpc|zx[ -]spectrum|bbc[ -]micro|"
                            r"acorn|electron|6502|z80)\b", re.I)
GH_LINK = re.compile(r"https?://(?:www\.)?github\.com/[\w.-]+/[\w.-]+(?:/[^\s<>\])}\"']*)?", re.I)
DIRECTORIES = {"games", "projects", "disassemblies", "disassembly", "ports", "targets"}


def now_utc() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


class HTTPClient:
    def __init__(self, token: str = "", delay: float = 2.1, max_requests: int = 30):
        self.token, self.delay, self.max_requests = token, delay, max_requests
        self.count = 0
        self.last_request = 0.0
        self.rate = {}

    def get(self, url: str):
        if self.count >= self.max_requests:
            raise RuntimeError("intake request cap reached")
        wait = self.delay - (time.monotonic() - self.last_request)
        if wait > 0:
            time.sleep(wait)
        host = urlsplit(url).hostname
        if host != "api.github.com" and urlsplit(url).scheme != "https":
            raise ValueError("Website source must use HTTPS")
        headers = {"Accept": "application/vnd.github+json", "User-Agent": "retro-dev-tracker-intake"}
        if host == "api.github.com" and self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        self.count += 1
        self.last_request = time.monotonic()
        try:
            with urlopen(Request(url, headers=headers), timeout=15) as response:
                self.rate = {k: response.headers.get(k) for k in
                             ("X-RateLimit-Resource", "X-RateLimit-Remaining", "Retry-After")}
                raw = response.read(1_000_001)
        except HTTPError as exc:
            raise RuntimeError(f"HTTP {exc.code} for {urlsplit(url).path} (rate remaining: "
                               f"{exc.headers.get('X-RateLimit-Remaining', '?')})") from exc
        except URLError as exc:
            raise RuntimeError(f"Request failed for {urlsplit(url).hostname}: {exc.reason}") from exc
        if len(raw) > 1_000_000:
            raise ValueError("Source response exceeds 1 MB")
        return json.loads(raw) if host == "api.github.com" else raw.decode("utf-8", errors="replace")


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            link = dict(attrs).get("href", "")
            if link:
                self.links.append(link)


def collect_query(client, recipe: dict, limit: int) -> list[dict]:
    kind = recipe["kind"]
    if kind not in {"repositories", "code"}:
        raise ValueError(f"Unsupported query kind: {kind}")
    endpoint = "repositories" if kind == "repositories" else "code"
    url = f"https://api.github.com/search/{endpoint}?" + urlencode({"q": recipe["q"], "per_page": limit})
    data = client.get(url)
    hits = []
    for item in data.get("items", []):
        repo = item if kind == "repositories" else item.get("repository", {})
        if repo.get("fork"):
            continue
        link = repo.get("html_url")
        if link:
            hits.append({"url": link, "route": f"github-{kind}", "origin": recipe["id"],
                         "title": repo.get("full_name") or repo.get("name", ""),
                         "description": repo.get("description") or "",
                         "evidence_url": item.get("html_url") if kind == "code" else link})
    return hits


def github_candidate(link: str) -> str | None:
    """Keep directory leads distinct, but treat issue/file links as repo evidence."""
    try:
        normalized = canonical_url(link)
    except ValueError:
        return None
    root = github_repository_key(normalized)
    if root is None:
        return None
    segments = urlsplit(normalized).path.strip("/").split("/")
    return normalized if len(segments) >= 5 and segments[2] == "tree" else root


def collect_source(client, source: dict, max_links: int) -> list[dict]:
    kind, source_url = source["kind"], source["source"]
    parsed = urlsplit(source_url)
    path = parsed.path.strip("/").split("/")
    hits = []
    if kind == "github-profile" and parsed.hostname == "github.com" and len(path) == 1:
        api = f"https://api.github.com/users/{quote(path[0])}/repos?per_page=100&type=owner&sort=pushed"
        for repo in client.get(api):
            if not repo.get("fork") and repo.get("html_url"):
                hits.append({"url": repo["html_url"], "title": repo.get("name", ""),
                             "description": repo.get("description") or ""})
    elif kind == "github-repository" and parsed.hostname == "github.com" and len(path) >= 2:
        owner, repo = path[:2]
        api = f"https://api.github.com/repos/{quote(owner)}/{quote(repo)}/readme"
        try:
            readme = client.get(api)
            body = base64.b64decode(readme["content"]).decode("utf-8", errors="replace")
        except RuntimeError as exc:
            if "HTTP 404" not in str(exc):
                raise
            body = ""  # Repositories without a README still have directories.
        for link in GH_LINK.findall(body):
            candidate = github_candidate(link.rstrip(".,;"))
            if candidate:
                hits.append({"url": candidate, "evidence_url": readme.get("html_url", source_url)})
        # Only inspect title collections; generic src/docs directories are too broad.
        root = client.get(f"https://api.github.com/repos/{quote(owner)}/{quote(repo)}/contents")
        for directory in root if isinstance(root, list) else []:
            if directory.get("type") == "dir" and directory["name"].casefold() in DIRECTORIES:
                children = client.get(directory["url"])
                for child in children if isinstance(children, list) else []:
                    if child.get("type") == "dir" and child.get("html_url"):
                        hits.append({"url": child["html_url"], "title": child["name"],
                                     "evidence_url": directory.get("html_url", source_url)})
    elif kind == "website" and parsed.scheme == "https":
        parser = LinkParser()
        parser.feed(client.get(source_url))
        for link in parser.links:
            resolved = urljoin(source_url, link)
            candidate = github_candidate(resolved)
            if candidate:
                hits.append({"url": candidate, "evidence_url": source_url})
    return [{**hit, "route": f"source-{kind}", "origin": source["id"]} for hit in hits[:max_links]]


def empty_state() -> dict:
    return {"version": 1, "query_cursor": 0, "source_checked": {}, "queue": {}, "runs": []}


def read_state(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else empty_state()


def merge_state(base: dict, incoming: dict) -> dict:
    """Reconcile a finished run with a main branch that advanced during it."""
    result = json.loads(json.dumps(base))
    result["query_cursor"] = incoming["query_cursor"]
    for key, value in incoming["source_checked"].items():
        if value > result["source_checked"].get(key, ""):
            result["source_checked"][key] = value
    for key, value in incoming["queue"].items():
        old = result["queue"].get(key)
        if old is None:
            result["queue"][key] = value
        else:
            old["first_seen"] = min(old["first_seen"], value["first_seen"])
            newer = value["last_seen"] >= old["last_seen"]
            old["last_seen"] = max(old["last_seen"], value["last_seen"])
            old["origins"] = sorted({(x["route"], x["origin"]): x for x in
                                     old["origins"] + value["origins"]}.values(),
                                    key=lambda x: (x["route"], x["origin"]))
            if newer:
                old.update({k: value[k] for k in ("title", "description", "evidence_url") if k in value})
    result["runs"] = sorted({x["id"]: x for x in base["runs"] + incoming["runs"]}.values(),
                            key=lambda x: x["id"])[-30:]
    return result


def add_hits(state: dict, index: CandidateIndex, hits: list[dict], when: str) -> dict:
    counts = defaultdict(Counter)
    for hit in hits:
        screened = index.screen(hit["url"])
        status = screened["status"]
        route = hit.get("route", "manual")
        counts[route][status] += 1
        if status not in {"new", "known_repository", "known_repository_path"} and not (
            status == "reviewed_decision" and any(m.get("decision") == "deferred" for m in screened["matches"])
        ):
            continue
        key = screened["canonical_url"]
        entry = state["queue"].setdefault(key, {"url": hit["url"], "first_seen": when, "origins": []})
        entry["last_seen"] = when
        for field in ("title", "description", "evidence_url"):
            if hit.get(field) and not entry.get(field):
                entry[field] = hit[field][:500]
        origin = {"route": route, "origin": hit.get("origin", "manual")}
        if origin not in entry["origins"]:
            entry["origins"].append(origin)
    return {route: dict(counter) for route, counter in sorted(counts.items())}


def rank_queue(state: dict, index: CandidateIndex) -> dict:
    resolved = []
    for key, entry in state["queue"].items():
        result = index.screen(key)
        status = result["status"]
        if status not in {"new", "known_repository", "known_repository_path"} and not (
            status == "reviewed_decision" and any(m.get("decision") == "deferred" for m in result["matches"])
        ):
            resolved.append(key)
            continue
        entry["status"] = status
        title_and_description = entry.get("title", "") + " " + entry.get("description", "")
        work = bool(WORK_TERMS.search(title_and_description))
        platform = bool(PLATFORM_TERMS.search(title_and_description))
        route_bonus = 12 if any(o["route"] == "github-code" for o in entry["origins"]) else 0
        route_bonus += 8 if any(o["route"] == "source-github-repository" for o in entry["origins"]) else 0
        entry["score"] = ({"new": 100, "known_repository_path": 78,
                           "known_repository": 70, "reviewed_decision": 45}[status]
                          + (12 if work else 0) + (8 if platform else 0)
                          + min(12, 4 * len(entry["origins"])) + route_bonus
                          - (18 if not entry.get("description") else 0)
                          - (20 if not work and not platform else 0)
                          - (15 if urlsplit(key).path.lower().endswith("-releases") else 0))
    for key in resolved:
        del state["queue"][key]
    state["queue"] = dict(sorted(state["queue"].items(),
                                 key=lambda item: (-item[1]["score"], item[1]["first_seen"], item[0])))
    return {"open": len(state["queue"]), "resolved": len(resolved)}


def run(root: Path, client, config: dict, state: dict, *, max_queries: int | None = None,
        input_hits: list[dict] | None = None, offline: bool = False, when: str | None = None) -> dict:
    when = when or now_utc()
    index = CandidateIndex(root / "data")
    hits = list(input_hits or [])
    errors = []
    selected = []
    if not offline:
        recipes = config["queries"]
        count = min(len(recipes), max_queries if max_queries is not None else config["queries_per_run"])
        attempted = 0
        for offset in range(count):
            pos = (state["query_cursor"] + offset) % len(recipes)
            recipe = recipes[pos]
            attempted += 1
            try:
                hits.extend(collect_query(client, recipe, config["results_per_query"]))
                selected.append(recipe["id"])
            except (RuntimeError, ValueError, KeyError) as exc:
                errors.append(f"query {recipe['id']}: {exc}")
                if client.count >= client.max_requests or "HTTP 429" in str(exc) or "HTTP 403" in str(exc):
                    break
        state["query_cursor"] = (state["query_cursor"] + attempted) % len(recipes)
        sources = json.loads((root / "data" / "discovery-sources.json").read_text(encoding="utf-8"))["sources"]
        for kind, limit in config["sources_per_run"].items():
            eligible = [s for s in sources if s["kind"] == kind and s["source"].startswith("https://")]
            eligible.sort(key=lambda s: (state["source_checked"].get(s["id"], ""), s["id"]))
            for source in eligible[:limit]:
                state["source_checked"][source["id"]] = when
                try:
                    hits.extend(collect_source(client, source, config["max_links_per_source"]))
                    selected.append(source["id"])
                except (RuntimeError, ValueError, KeyError, UnicodeError) as exc:
                    errors.append(f"source {source['id']}: {exc}")
                    if client.count >= client.max_requests:
                        break
    counts = add_hits(state, index, hits, when)
    queue_summary = rank_queue(state, index)
    report = {"id": when, "queries_and_sources": selected, "hits": len(hits), "by_route": counts,
              "requests": client.count, "errors": errors, **queue_summary}
    state["runs"].append(report)
    state["runs"] = state["runs"][-30:]
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help=argparse.SUPPRESS)
    parser.add_argument("--input", help="Import candidate URLs or JSON objects; - reads stdin")
    parser.add_argument("--offline", action="store_true", help="Only import input/reconcile state; no network")
    parser.add_argument("--max-queries", type=int, help="Queries to rotate through in this run")
    parser.add_argument("--list", type=int, metavar="N", help="Show N highest-ranked queued leads without collecting")
    parser.add_argument("--merge-state", type=Path, help="Merge a completed run after main advances")
    parser.add_argument("--output", type=Path, help="Write state to this path (default: state/discovery-intake.json)")
    args = parser.parse_args()
    path = args.root / "state" / "discovery-intake.json"
    state = read_state(path)
    index = CandidateIndex(args.root / "data")
    if args.list is not None:
        rank_queue(state, index)
        for key, entry in list(state["queue"].items())[:args.list]:
            print(f"{entry['score']:3} {entry['status']:22} {entry['url']}  "
                  f"[{', '.join(x['origin'] for x in entry['origins'])}]")
        return
    if args.merge_state:
        state = merge_state(state, read_state(args.merge_state))
        report = rank_queue(state, index)
    else:
        if args.offline and not args.input:
            parser.error("--offline requires --input or --merge-state")
        hits = read_candidates(args.input, "manual") if args.input else []
        client = HTTPClient(os.environ.get("GITHUB_TOKEN", ""))
        config = json.loads((args.root / "config" / "discovery-intake.json").read_text(encoding="utf-8"))
        report = run(args.root, client, config, state, max_queries=args.max_queries,
                     input_hits=hits, offline=args.offline)
    output = args.output or path
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
