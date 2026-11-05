#!/usr/bin/env python3
"""Cache linkable Wikidata games and conservatively resolve catalogue subjects.

Network refresh is all-or-nothing. Matching is offline and never changes project
records. Missing/ambiguous evidence is review work, not a guessed association.
"""
from __future__ import annotations

import argparse
import hashlib
from collections import defaultdict
from datetime import datetime, timezone, timedelta
import json
import os
from pathlib import Path
import re
import sys
import tempfile
import time
import unicodedata
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from catalogue_storage import load_projects

ENDPOINT = "https://query.wikidata.org/sparql"
USER_AGENT = "LegacyReverseEngineeringTracker/1.0 (https://github.com/rmtew/legacy-reverse-engineering-tracker)"
INDEX_FORMAT = "tracker-wikidata-index/v1"
LINK_FORMAT = "tracker-game-links/v1"
REVIEW_FORMAT = "tracker-wikidata-review/v1"
OVERRIDE_FORMAT = "tracker-wikidata-overrides/v1"
PROPERTIES = {"lemon_amiga": "P4846", "lemon64": "P4816", "moby": "P11688"}
QID = re.compile(r"Q[1-9][0-9]*\Z")
IDENTIFIER = re.compile(r"[0-9]+\Z")
PREFIXES = """PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
"""


def now_text():
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def parse_time(value):
    if not isinstance(value, str):
        raise ValueError("Expected an ISO UTC timestamp")
    result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if result.tzinfo is None:
        raise ValueError("Timestamp must have a timezone")
    return result


def atomic_json(path, value):
    """Never expose half-written JSON or replace good data on serialization errors."""
    raw = (json.dumps(value, ensure_ascii=False, separators=(",", ":"), allow_nan=False) + "\n").encode()
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix="." + path.name + ".", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(raw)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def item_id(uri):
    prefix = "http://www.wikidata.org/entity/"
    if not isinstance(uri, str) or not uri.startswith(prefix) or not QID.fullmatch(uri[len(prefix):]):
        raise ValueError("Invalid Wikidata entity URI")
    return uri[len(prefix):]


def subject_names(subjects):
    names = set()
    for subject in subjects:
        if not isinstance(subject, str) or not subject.strip():
            raise ValueError("Invalid catalogue subject")
        title = re.sub(r"\s+\(\d{4}(?: video game)?\)$", "", subject)
        for name in (title, title.title(), title.replace("’", "'")):
            names.add(unicodedata.normalize("NFKC", name))
    return sorted(names)


def subjects_fingerprint(subjects):
    return hashlib.sha256(json.dumps(sorted(set(subjects)), ensure_ascii=False).encode()).hexdigest()


def eligible_projects(projects):
    return [project for project in projects if project.get("record_class") in {"subject", "hybrid"}
            and "game" in project.get("target_kinds", [])]


def item_query(names):
    if not names or any(not isinstance(name, str) or not name for name in names):
        raise ValueError("Name query requires nonempty strings")
    literals = " ".join(json.dumps(name, ensure_ascii=False) + "@" + language for name in names for language in ("en", "mul"))
    branches = " UNION ".join("{ ?item wdt:" + property_id + " ?external }" for property_id in PROPERTIES.values())
    # Bound label/alias lookups avoid a whole-graph scan and OFFSET pagination.
    # All same-name candidates are retained; a safety limit fails closed.
    return PREFIXES + "SELECT DISTINCT ?item WHERE { VALUES ?name { " + literals + " } { { ?item rdfs:label ?name } UNION { ?item skos:altLabel ?name } } { " + branches + " } } LIMIT 1001"


def detail_query(qids):
    if not qids or any(not isinstance(qid, str) or not QID.fullmatch(qid) for qid in qids):
        raise ValueError("Invalid detail IDs")
    # Tall rows, not optional-property Cartesian products. One row is one fact.
    branches = [
        '{ ?item rdfs:label ?value . FILTER(LANG(?value) IN ("en", "mul")) BIND(IF(LANG(?value) = "en", "label", "label-mul") AS ?kind) }',
        '{ ?item skos:altLabel ?value . FILTER(LANG(?value) IN ("en", "mul")) BIND("alias" AS ?kind) }',
        '{ ?item wdt:P577 ?value . BIND("released" AS ?kind) }',
        '{ ?item wdt:P400 ?platform . OPTIONAL { ?platform rdfs:label ?platformLabel . FILTER(LANG(?platformLabel) IN ("en", "mul")) } BIND(COALESCE(?platformLabel, STR(?platform)) AS ?value) BIND("platform" AS ?kind) }',
    ]
    branches += ['{ ?item wdt:' + prop + ' ?value . BIND("' + key + '" AS ?kind) }' for key, prop in PROPERTIES.items()]
    return PREFIXES + "SELECT ?item ?kind ?value ?platform WHERE { VALUES ?item { " + " ".join("wd:" + q for q in qids) + " } " + " UNION ".join(branches) + " }"


class SparqlClient:
    def __init__(self, timeout=60, delay=1.0, deadline=None):
        self.timeout, self.delay, self.deadline = timeout, delay, deadline
        self.requests = 0

    def __call__(self, query):
        for attempt in range(3):
            remaining = self.deadline - time.monotonic() if self.deadline else self.timeout
            if remaining <= 0:
                raise TimeoutError("Wikidata refresh time budget exhausted")
            request = Request(ENDPOINT + "?" + urlencode({"query": query, "format": "json"}),
                              headers={"Accept": "application/sparql-results+json", "User-Agent": USER_AGENT})
            try:
                self.requests += 1
                with urlopen(request, timeout=min(self.timeout, remaining)) as response:
                    # Bounded fact pages should be small. Reject unexpected bulk/error responses.
                    raw = response.read(16 * 1024 * 1024 + 1)
                if len(raw) > 16 * 1024 * 1024:
                    raise ValueError("Oversized Wikidata response")
                data = json.loads(raw)
                bindings = data.get("results", {}).get("bindings")
                if not isinstance(bindings, list):
                    raise ValueError("Wikidata response is not SPARQL JSON")
                time.sleep(self.delay)
                return bindings
            except HTTPError as error:
                if error.code not in {429, 500, 502, 503, 504} or attempt == 2:
                    raise
                retry_after = error.headers.get("Retry-After", "")
                delay = min(60, int(retry_after)) if retry_after.isdigit() else 5 * (attempt + 1)
                if self.deadline and time.monotonic() + delay >= self.deadline:
                    raise TimeoutError("Wikidata retry would exceed time budget") from error
                time.sleep(delay)
        raise RuntimeError("Unreachable retry state")


def binding_value(row, key):
    value = row.get(key)
    if not isinstance(value, dict) or not isinstance(value.get("value"), str):
        raise ValueError("Malformed SPARQL binding: " + key)
    return value["value"]


def collect_index(query, subjects, *, explicit_qids=(), page_size=40, max_pages=500, generated_at=None, deadline=None):
    if not 1 <= page_size <= 100 or max_pages < 1:
        raise ValueError("Subject query batch size must be 1–100; batch limit must be positive")
    if any(not isinstance(qid, str) or not QID.fullmatch(qid) for qid in explicit_qids):
        raise ValueError("Invalid explicit QID")
    games, names, request_count = {}, subject_names(subjects), 0

    def bounded_query(build_query, values):
        nonlocal request_count
        if deadline and time.monotonic() >= deadline:
            raise TimeoutError("Wikidata refresh time budget exhausted")
        if request_count >= max_pages * 4:
            raise ValueError("Wikidata request limit reached; refusing partial index")
        request_count += 1
        try:
            return query(build_query(values))
        except HTTPError as error:
            if error.code not in {500, 502, 503, 504} or len(values) <= 1:
                raise
            # A WDQS timeout on a batch can be retried at smaller scope, never
            # silently treated as an empty result or a finished refresh.
            middle = len(values) // 2
            return bounded_query(build_query, values[:middle]) + bounded_query(build_query, values[middle:])

    batches = [names[start:start + page_size] for start in range(0, len(names), page_size)]
    if len(batches) > max_pages:
        raise ValueError("Wikidata subject batch limit reached; refusing partial index")
    if explicit_qids:
        batches.append(None)
    for batch in batches:
        rows = bounded_query(item_query, batch) if batch else [{"item": {"value": "http://www.wikidata.org/entity/" + qid}} for qid in explicit_qids]
        if len(rows) >= 1001:
            raise ValueError("Wikidata candidate limit reached; refusing partial index")
        qids = sorted({item_id(binding_value(row, "item")) for row in rows} - games.keys())
        for start in range(0, len(qids), 100):
            selected = qids[start:start + 100]
            page = {qid: {"qid": qid, "label": "", "aliases": [], "platforms": [], "release_dates": [],
                           **{key: [] for key in PROPERTIES}} for qid in selected}
            for row in bounded_query(detail_query, selected):
                qid = item_id(binding_value(row, "item"))
                if qid not in page:
                    raise ValueError("Wikidata details escaped the requested page")
                kind, value = binding_value(row, "kind"), binding_value(row, "value")
                game = page[qid]
                if kind == "label":
                    if game.get("_english_label") and game["_english_label"] != value:
                        raise ValueError("Conflicting English label for " + qid)
                    game["label"] = game["_english_label"] = value
                elif kind == "label-mul":
                    if not game["label"]:
                        game["label"] = value
                    game["aliases"].append(value)
                elif kind == "alias":
                    game["aliases"].append(value)
                elif kind == "released":
                    if re.fullmatch(r"\+?[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9:]+Z", value):
                        game["release_dates"].append(value)
                elif kind == "platform":
                    game["platforms"].append({"qid": item_id(binding_value(row, "platform")), "label": value})
                elif kind in PROPERTIES:
                    # Invalid third-party IDs remain absent, never become URLs.
                    if IDENTIFIER.fullmatch(value):
                        game[kind].append(value)
                else:
                    raise ValueError("Unexpected Wikidata detail kind: " + kind)
            for game in page.values():
                game.pop("_english_label", None)
                for key in ("aliases", "release_dates", *PROPERTIES):
                    game[key] = sorted(set(game[key]))
                game["platforms"] = sorted({(p["qid"], p["label"]) for p in game["platforms"]})
                game["platforms"] = [{"qid": q, "label": label} for q, label in game["platforms"]]
                if not any(game[key] for key in PROPERTIES) and not (game["qid"] in explicit_qids and game["label"]):
                    raise ValueError("No valid external identifiers returned for " + game["qid"])
            games.update(page)
    result = {"format": INDEX_FORMAT, "complete": True, "generated_at": generated_at or now_text(),
              "source": {"endpoint": ENDPOINT, "properties": PROPERTIES,
                         "scope": "Exact English/multilingual catalogue subject names/aliases with external game identifiers; full returned aliases, platforms and dates",
                         "subjects_sha256": subjects_fingerprint(subjects), "subjects": sorted(set(subjects)), "subject_count": len(set(subjects)),
                         "manual_qids": sorted(set(explicit_qids)), "query_version": 1},
              "games": [games[qid] for qid in sorted(games)]}
    validate_index(result)
    return result


def validate_index(index):
    if not isinstance(index, dict) or index.get("format") != INDEX_FORMAT or index.get("complete") is not True:
        raise ValueError("Expected a complete Wikidata index")
    parse_time(index.get("generated_at"))
    source = index.get("source")
    if not isinstance(source, dict) or not isinstance(source.get("subjects"), list) or any(not isinstance(subject, str) or not subject for subject in source["subjects"]):
        raise ValueError("Wikidata index needs its exact queried subjects")
    if source.get("subjects_sha256") != subjects_fingerprint(source["subjects"]):
        raise ValueError("Wikidata subject fingerprint mismatch")
    games = index.get("games")
    if not isinstance(games, list):
        raise ValueError("Wikidata index games must be an array")
    seen = set()
    for game in games:
        if not isinstance(game, dict) or not isinstance(game.get("qid"), str) or not QID.fullmatch(game["qid"]) or game["qid"] in seen:
            raise ValueError("Invalid/duplicate Wikidata game ID")
        seen.add(game["qid"])
        if not isinstance(game.get("label"), str):
            raise ValueError("Invalid Wikidata label")
        for key in ("aliases", "release_dates", *PROPERTIES):
            if not isinstance(game.get(key), list) or any(not isinstance(v, str) or not v for v in game[key]):
                raise ValueError("Invalid Wikidata list: " + key)
            if len(game[key]) != len(set(game[key])):
                raise ValueError("Duplicate Wikidata values: " + key)
        for key in PROPERTIES:
            if any(not IDENTIFIER.fullmatch(v) for v in game[key]):
                raise ValueError("Invalid external identifier")
        if not isinstance(game.get("platforms"), list):
            raise ValueError("Invalid platform list")
        for platform in game["platforms"]:
            if not isinstance(platform, dict) or not isinstance(platform.get("qid"), str) or not QID.fullmatch(platform["qid"]) or not isinstance(platform.get("label"), str):
                raise ValueError("Invalid Wikidata platform")
    return index


def normalized(value):
    return " ".join("".join(character if character.isalnum() else " " for character in unicodedata.normalize("NFKC", value).casefold()).split())


# Only equivalent platform names, not families/compatible successors. Canonical
# platform QIDs and labels are retained from Wikidata, never guessed here.
PLATFORM_ALIASES = {
    "commodore amiga": "amiga", "amiga computer": "amiga",
    "c64": "commodore 64", "commodore c64": "commodore 64",
    "dos": "ms dos", "msdos": "ms dos", "ibm pc dos": "ms dos",
    "nes": "nintendo entertainment system", "famicom": "nintendo entertainment system",
    "snes": "super nintendo entertainment system", "super famicom": "super nintendo entertainment system",
    "spectrum": "zx spectrum", "sinclair zx spectrum": "zx spectrum",
    "windows": "microsoft windows", "apple macintosh": "macintosh",
    "sega genesis": "sega mega drive", "genesis": "sega mega drive", "mega drive": "sega mega drive",
    "arcade": "arcade video game", "arcade game": "arcade video game",
    "bbc microcomputer": "bbc micro", "acorn bbc micro": "bbc micro",
}


def platform_name(value):
    value = normalized(value)
    return PLATFORM_ALIASES.get(value, value)


def validate_overrides(value):
    if not isinstance(value, dict) or value.get("format") != OVERRIDE_FORMAT or not isinstance(value.get("projects"), dict):
        raise ValueError("Invalid Wikidata overrides document")
    for pid, subjects in value["projects"].items():
        if not isinstance(pid, str) or not pid or not isinstance(subjects, dict):
            raise ValueError("Invalid override project")
        for subject, override in subjects.items():
            if not isinstance(subject, str) or not subject or not isinstance(override, dict) or set(override) != {"qid", "reason"}:
                raise ValueError("Overrides need exact subject names, qid and reason")
            if override["qid"] is not None and (not isinstance(override["qid"], str) or not QID.fullmatch(override["qid"])):
                raise ValueError("Invalid override QID")
            if not isinstance(override["reason"], str) or not override["reason"].strip():
                raise ValueError("Manual overrides need a reason")
    return value["projects"]


def project_game_links(projects, index, overrides=None, *, generated_at=None):
    validate_index(index)
    override_projects = validate_overrides(overrides or {"format": OVERRIDE_FORMAT, "projects": {}})
    games = {game["qid"]: game for game in index["games"]}
    names = defaultdict(set)
    for game in games.values():
        for name in [game["label"], *game["aliases"]]:
            if normalized(name):
                names[normalized(name)].add(game["qid"])
    accepted, review, used = {}, [], set()
    counts = defaultdict(int)
    for project in eligible_projects(projects):
        platforms = {platform_name(p) for p in project.get("source_platforms", [])}
        for subject in project.get("subjects", []):
            if not isinstance(subject, str) or not subject.strip():
                continue
            pid = project["id"]
            record = {"project_id": pid, "subject": subject}
            override = override_projects.get(pid, {}).get(subject)
            qid = None
            if override is not None:
                used.add((pid, subject))
                qid = override["qid"]
                status = "manual" if qid else "excluded"
                record["reason"] = override["reason"]
                if qid and qid not in games:
                    record["warning"] = "Manual QID is absent from current index; no external IDs inferred"
            elif subject not in index["source"]["subjects"]:
                status = "not-indexed"
                record["reason"] = "Subject added after index collection; await the next refresh"
            else:
                # Explicit subject release annotations are usable; re_started and
                # repository dates are never interpreted as the game's release.
                year_match = re.fullmatch(r"(.+?)\s+\((\d{4})(?: video game)?\)", subject)
                title = year_match[1] if year_match else subject
                year = year_match[2] if year_match else None
                candidates = sorted(names.get(normalized(title), set()))
                eligible, corroborated = [], {}
                details = []
                for candidate in candidates:
                    game = games[candidate]
                    game_platforms = {platform_name(p["label"]) for p in game["platforms"]}
                    years = {date.lstrip("+")[:4] for date in game["release_dates"]}
                    platform_match = bool(platforms & game_platforms)
                    platform_conflict = bool(platforms and game_platforms and not platform_match)
                    year_match = bool(year and year in years)
                    year_conflict = bool(year and years and year not in years)
                    reason = "platform-mismatch" if platform_conflict else "release-year-mismatch" if year_conflict else "corroborated" if platform_match else "missing-platform-evidence"
                    # Platform corroboration is mandatory, even when the name or
                    # release year alone looks unique. Unknown candidates remain
                    # in contention rather than being silently discarded.
                    if not platform_conflict and not year_conflict:
                        eligible.append(candidate)
                        corroborated[candidate] = platform_match
                    details.append({"qid": candidate, "label": game["label"], "platforms": game["platforms"], "release_dates": game["release_dates"], "reason": reason})
                if len(eligible) == 1 and corroborated[eligible[0]]:
                    qid, status = eligible[0], "exact-title-platform"
                elif len(eligible) > 1:
                    status = "ambiguous"
                elif eligible:
                    status = "missing-platform-evidence"
                elif candidates:
                    status = "conflicting-evidence"
                else:
                    status = "unmatched"
                record["candidates"] = details[:20]
                record["candidate_count"] = len(details)
            record["status"] = status
            counts[status] += 1
            if qid:
                game = games.get(qid, {})
                link = {"subject": subject, "qid": qid, "match": status,
                        "evidence": "https://www.wikidata.org/wiki/" + qid,
                        **{key: game.get(key, [])[0] if len(game.get(key, [])) == 1 else None for key in PROPERTIES}}
                if status == "manual":
                    link["reason"] = override["reason"]
                accepted.setdefault(pid, []).append(link)
                conflicts = [key for key in PROPERTIES if len(game.get(key, [])) > 1]
                if conflicts:
                    record["warning"] = "Multiple external IDs omitted: " + ", ".join(conflicts)
                if "warning" in record:
                    review.append(record)
            else:
                review.append(record)
    for pid, subjects in override_projects.items():
        for subject in subjects:
            if (pid, subject) not in used:
                review.append({"project_id": pid, "subject": subject, "status": "stale-override", "reason": "Project/subject is missing or not a game record; override retained unchanged"})
                counts["stale-override"] += 1
    stamp = generated_at or now_text()
    base = {"generated_at": stamp, "index_generated_at": index["generated_at"]}
    return ({"format": LINK_FORMAT, **base, "projects": accepted},
            {"format": REVIEW_FORMAT, **base, "counts": dict(sorted(counts.items())), "subjects": review})


def refresh(root, *, force=False, max_age_days=30, page_size=40, max_pages=500, timeout=60, max_runtime=900, query=None):
    root = Path(root)
    path = root / "state/wikidata-index.json"
    previous = validate_index(read_json(path)) if path.exists() else None
    projects = eligible_projects(load_projects(root / "data/projects.json"))
    subjects = sorted({subject for project in projects for subject in project.get("subjects", [])})
    overrides_path = root / "config/wikidata-overrides.json"
    overrides = validate_overrides(read_json(overrides_path)) if overrides_path.exists() else {}
    manual_qids = sorted({override["qid"] for values in overrides.values() for override in values.values() if override["qid"]})
    source = previous.get("source", {}) if previous else {}
    same_subjects = previous and source.get("subjects_sha256") == subjects_fingerprint(subjects)
    same_overrides = previous and source.get("manual_qids", []) == manual_qids
    # An incremental addition must not postpone the next complete refresh.
    full_refresh_at = source.get("full_refresh_at", previous["generated_at"] if previous else None)
    fresh = previous and datetime.now(timezone.utc) - parse_time(full_refresh_at) < timedelta(days=max_age_days)
    if fresh and same_subjects and same_overrides and not force:
        return {"status": "cached", "games": len(previous["games"])}
    incremental = bool(fresh and not force)
    query_subjects = sorted(set(subjects) - set(source.get("subjects", []))) if incremental else subjects
    query_qids = sorted(set(manual_qids) - set(source.get("manual_qids", []))) if incremental else manual_qids
    deadline = time.monotonic() + max_runtime
    client = query or SparqlClient(timeout=timeout, deadline=deadline)
    index = collect_index(client, query_subjects, explicit_qids=query_qids, page_size=page_size, max_pages=max_pages, deadline=deadline)
    if incremental:
        merged = {game["qid"]: game for game in previous["games"]}
        merged.update({game["qid"]: game for game in index["games"]})
        index["games"] = [merged[qid] for qid in sorted(merged)]
    elif previous and same_subjects and len(index["games"]) < len(previous["games"]) * 0.8:
        raise ValueError("Wikidata index unexpectedly shrank by over 20%; retaining previous data")
    index["source"].update(subjects=subjects, subjects_sha256=subjects_fingerprint(subjects),
                           subject_count=len(subjects), manual_qids=manual_qids,
                           full_refresh_at=full_refresh_at if incremental else index["generated_at"])
    validate_index(index)
    atomic_json(path, index)
    return {"status": "incremental" if incremental else "refreshed", "games": len(index["games"]),
            "queried_subjects": len(query_subjects), "queried_manual_qids": len(query_qids)}


def match(root):
    root = Path(root)
    index = validate_index(read_json(root / "state/wikidata-index.json"))
    overrides_path = root / "config/wikidata-overrides.json"
    overrides = read_json(overrides_path) if overrides_path.exists() else None
    links, review = project_game_links(load_projects(root / "data/projects.json"), index, overrides)
    # No-op runs do not cause commits/deployments solely due to generated_at.
    existing = root / "data/game-links.json"
    old = read_json(existing) if existing.exists() else None
    if old and {k: v for k, v in old.items() if k not in {"generated_at", "index_generated_at"}} == {k: v for k, v in links.items() if k not in {"generated_at", "index_generated_at"}}:
        links["generated_at"] = old["generated_at"]
        links["index_generated_at"] = old["index_generated_at"]
    old_review_path = root / "state/wikidata-review.json"
    old_review = read_json(old_review_path) if old_review_path.exists() else None
    if old_review and {k: v for k, v in old_review.items() if k not in {"generated_at", "index_generated_at"}} == {k: v for k, v in review.items() if k not in {"generated_at", "index_generated_at"}}:
        review["generated_at"] = old_review["generated_at"]
        review["index_generated_at"] = old_review["index_generated_at"]
    atomic_json(old_review_path, review)
    atomic_json(existing, links)
    return {"projects": len(links["projects"]), "links": sum(map(len, links["projects"].values())), "review": len(review["subjects"]), "counts": review["counts"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    refresh_parser = subparsers.add_parser("refresh", help="Refresh complete cached Wikidata index; preserve existing cache on failure")
    refresh_parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    refresh_parser.add_argument("--force", action="store_true")
    refresh_parser.add_argument("--max-age-days", type=int, default=30)
    refresh_parser.add_argument("--page-size", type=int, default=40)
    refresh_parser.add_argument("--max-pages", type=int, default=500)
    refresh_parser.add_argument("--timeout", type=int, default=60)
    refresh_parser.add_argument("--max-runtime", type=int, default=900)
    match_parser = subparsers.add_parser("match", help="Resolve game subjects offline and write accepted links plus review report")
    match_parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = vars(parser.parse_args())
    command = args.pop("command")
    try:
        if any(value <= 0 for key, value in args.items() if key in {"max_age_days", "page_size", "max_pages", "timeout", "max_runtime"}):
            raise ValueError("Numeric refresh limits must be positive")
        print(json.dumps(refresh(**args) if command == "refresh" else match(**args), sort_keys=True))
    except (ValueError, OSError, TimeoutError, URLError, KeyError, TypeError) as error:
        print("Wikidata " + command + " failed; existing complete cache/links retained: " + str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
