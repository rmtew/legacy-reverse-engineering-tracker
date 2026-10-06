#!/usr/bin/env python3
"""Compile author-reviewed research records into the existing discovery batch.

This module performs structural checks and rendering only. It never derives a
classification, audit judgment, build flag or AI claim from evidence text.
"""
from __future__ import annotations

import argparse
import copy
from datetime import date
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import quote, urlsplit

FORMAT = "research-records/v1"
AREAS = ("identity", "classification", "source_cpu", "target_cpu", "build",
         "runtime_profiles", "ai", "relationships")
LABELS = {"identity": "Identity", "classification": "Classification",
          "source_cpu": "Source CPU", "target_cpu": "Target CPU", "build": "Build",
          "runtime_profiles": "Runtime profiles", "ai": "AI", "relationships": "Relationships"}
AREA_STATES = {"unreviewed", "needs-research", "reviewed", "not-applicable", "no-evidence-found"}
BATCH_FIELDS = ("date", "event_id", "summary", "notes", "kind", "sources",
                "source_updates", "tasks", "task_updates", "decisions", "source_ids")
_SHA = re.compile(r"[0-9a-fA-F]{40}\Z")


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def _text(value, label: str) -> str:
    _require(isinstance(value, str) and bool(value.strip()), f"{label} must be nonempty text")
    return value


def _strings(value, label: str) -> list[str]:
    _require(isinstance(value, list), f"{label} must be an array")
    for item in value:
        _text(item, label)
    _require(len(value) == len(set(value)), f"{label} contains duplicates")
    return value


def _url(value, label: str) -> str:
    _text(value, label)
    parsed = urlsplit(value)
    _require(parsed.scheme in {"http", "https"} and bool(parsed.netloc)
             and parsed.username is None and parsed.password is None,
             f"{label} must be an HTTP(S) URL without credentials")
    return value


def _canonical(value) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False, allow_nan=False).encode("utf-8")


def _repository(value) -> str:
    _text(value, "Proof repository")
    _require(re.fullmatch(r"https://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+/?", value)
             is not None, "Proof repository must be a GitHub repository root URL")
    return value.rstrip("/").casefold()


def _sha(value, label: str) -> str:
    _require(isinstance(value, str) and _SHA.fullmatch(value) is not None,
             f"{label} must be a full 40-character Git SHA")
    return value.lower()


def proof_identity(proof: dict) -> dict:
    """Return the immutable cache identity; paths cannot escape the repository."""
    _require(isinstance(proof, dict) and not set(proof) - {"repository", "commit", "path", "blob", "text"},
             "Proof has unknown fields or is not an object")
    path = _text(proof.get("path"), "Proof path")
    _require(not any(part in {"", ".", ".."} for part in path.split("/"))
             and "\\" not in path and not any(ord(c) < 32 for c in path),
             "Proof path must be a repository-relative file path")
    return {"repository": _repository(proof.get("repository")),
            "commit": _sha(proof.get("commit"), "Proof commit"), "path": path,
            "blob": _sha(proof.get("blob"), "Proof blob")}


def proof_url(proof: dict) -> str:
    identity = proof_identity(proof)
    return f"{identity['repository']}/blob/{identity['commit']}/{quote(identity['path'], safe='/')}"


def git_blob_sha(text: str) -> str:
    """Hash the exact UTF-8 bytes as a Git blob (including preserved newlines)."""
    _require(isinstance(text, str), "Proof text must be a string")
    content = text.encode("utf-8")
    return hashlib.sha1(b"blob " + str(len(content)).encode("ascii") + b"\0" + content).hexdigest()


class EvidenceCache:
    """Local immutable text cache keyed by repository, commit, path AND blob.

    A matching blob establishes byte integrity, not that a server returned it or
    that a commit contains it. Collectors/reviewers must establish that provenance.
    """
    def __init__(self, directory: Path | str):
        self.directory = Path(directory)

    def path_for(self, proof: dict) -> Path:
        key = hashlib.sha256(_canonical(proof_identity(proof))).hexdigest()
        return self.directory / (key + ".json")

    def get(self, proof: dict) -> str:
        identity = proof_identity(proof)
        path = self.path_for(proof)
        _require(path.is_file(), f"Missing pinned proof cache entry for {proof_url(proof)}")
        try:
            entry = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, ValueError) as exc:
            raise ValueError(f"Unreadable proof cache entry: {path.name}") from exc
        _require(isinstance(entry, dict) and set(entry) == {"identity", "text"}
                 and entry.get("identity") == identity, "Mismatched proof cache identity")
        _require(git_blob_sha(entry.get("text")) == identity["blob"], "Mismatched proof cache blob")
        return entry["text"]

    def put(self, proof: dict, text: str) -> Path:
        identity = proof_identity(proof)
        _require(git_blob_sha(text) == identity["blob"], "Mismatched proof text/blob")
        self.directory.mkdir(parents=True, exist_ok=True)
        path = self.path_for(proof)
        if path.exists():
            _require(self.get(proof) == text, "Conflicting immutable proof cache entry")
            return path
        # Exclusive creation protects existing entries from accidental overwrite.
        try:
            with path.open("x", encoding="utf-8") as handle:
                json.dump({"identity": identity, "text": text}, handle, ensure_ascii=False, indent=2)
                handle.write("\n")
        except FileExistsError:
            _require(self.get(proof) == text, "Conflicting immutable proof cache entry")
        return path


def review_digest(document: dict) -> str:
    """Bind the authored payload, excluding review metadata and cached text.

    The proof blob SHA already binds its exact bytes. Switching between inline
    text and the same verified cache entry does not invalidate the review.
    """
    _require(isinstance(document, dict), "Research document must be an object")
    payload = copy.deepcopy(document)
    payload.pop("review", None)
    _require(isinstance(payload.get("proofs", {}), dict), "proofs must be an object indexed by proof ID")
    for proof in payload.get("proofs", {}).values():
        _require(isinstance(proof, dict), "Proof must be an object")
        proof.pop("text", None)
    return hashlib.sha256(_canonical(payload)).hexdigest()


def seal_review(document: dict) -> dict:
    """Explicit author action after review; makes no substantive judgment."""
    result = copy.deepcopy(document)
    result["review"] = {"status": "ready", "digest": review_digest(document)}
    return result


def _normalize(document: dict, *, evidence_cache=None, expected_commits=None, require_ready=False) -> tuple[dict, dict]:
    _require(isinstance(document, dict), "Research document must be an object")
    allowed = set(BATCH_FIELDS) | {"format", "title", "records", "proofs", "review"}
    _require(not set(document) - allowed, "Unknown research document fields")
    _require(document.get("format") == FORMAT, f"Research format must be {FORMAT}")
    day = _text(document.get("date"), "Research date")
    _require(re.fullmatch(r"\d{4}-\d{2}-\d{2}", day) is not None, "Research date must be YYYY-MM-DD")
    date.fromisoformat(day)
    for field in ("event_id", "summary"):
        _text(document.get(field), field)
    if "notes" in document:
        _require(isinstance(document["notes"], str), "Research notes must be text")
    if "kind" in document:
        _text(document["kind"], "Research kind")
    if "title" in document:
        _text(document["title"], "Report title")
    for field in ("sources", "source_updates", "tasks", "task_updates", "decisions", "source_ids"):
        _require(isinstance(document.get(field, []), list), f"{field} must be an array")
    review = document.get("review")
    _require(isinstance(review, dict) and not set(review) - {"status", "digest"}, "Research needs an explicit review object")
    _require(isinstance(review.get("status"), str) and review["status"] in {"draft", "ready"}, "Review status must be draft or ready")
    if require_ready:
        _require(review["status"] == "ready", "Research review is not ready; finish the author review before compiling")
    if "digest" in review:
        _require(review["digest"] == review_digest(document), "Stale research review digest; review the changed record/proofs again")

    cache = evidence_cache if isinstance(evidence_cache, EvidenceCache) or evidence_cache is None else EvidenceCache(evidence_cache)
    heads = None
    if expected_commits is not None:
        _require(isinstance(expected_commits, dict), "expected_commits must map repository URLs to commit SHAs")
        heads = {}
        for repository, commit in expected_commits.items():
            repository = _repository(repository)
            _require(repository not in heads, "Duplicate expected repository after normalization")
            heads[repository] = _sha(commit, "Expected commit")
    proofs = document.get("proofs", {})
    _require(isinstance(proofs, dict), "proofs must be an object indexed by proof ID")
    proof_urls, locations = {}, {}
    # Validate the full manifest before filling the cache.
    for proof_id, proof in proofs.items():
        _text(proof_id, "Proof ID")
        identity = proof_identity(proof)
        location = (identity["repository"], identity["commit"], identity["path"])
        _require(location not in locations or locations[location] == identity["blob"],
                 "Conflicting blobs for the same pinned repository/commit/path")
        locations[location] = identity["blob"]
        if heads is not None:
            _require(identity["repository"] in heads, f"No expected commit supplied for {identity['repository']}")
            _require(heads[identity["repository"]] == identity["commit"], f"Stale proof commit for {proof_id}; inspect the new upstream snapshot")
        if "text" in proof:
            _require(git_blob_sha(proof["text"]) == identity["blob"], f"Mismatched proof text/blob for {proof_id}")
        else:
            _require(cache is not None, f"Proof {proof_id} needs inline text or a pinned evidence cache")
            cache.get(proof)
        proof_urls[proof_id] = proof_url(proof)

    records = document.get("records", [])
    _require(isinstance(records, list), "records must be an array")
    batch = {field: copy.deepcopy(document[field]) for field in BATCH_FIELDS if field in document}
    batch["projects"] = []
    ids, urls = set(), {}
    for record in records:
        _require(isinstance(record, dict) and not set(record) - {"project", "source_ids", "allow_shared_url", "overall_state", "areas", "update"},
                 "Record has unknown fields or is not an object")
        project = copy.deepcopy(record.get("project"))
        _require(isinstance(project, dict), "Record needs a project object")
        update = record.get("update")
        if update is not None:
            _require(isinstance(update, dict) and set(update) == {"project_id", "expected_sha256"},
                     "update needs project_id and expected_sha256")
            project_id = _text(update["project_id"], "Update project ID")
            _require(isinstance(update["expected_sha256"], str)
                     and re.fullmatch(r"[0-9a-f]{64}", update["expected_sha256"]) is not None,
                     "Update expected_sha256 must be a canonical project SHA256")
            _require(project.get("id", project_id) == project_id, "Update may not change project ID")
            project.pop("id", None)
        else:
            project_id = _text(project.get("id"), "Project ID")
        _require(project_id not in ids, f"Duplicate project ID {project_id}")
        ids.add(project_id)
        _require("notes" not in project, f"Project {project_id}: author area narratives instead of duplicated project.notes")
        source_ids = _strings(record.get("source_ids", []), f"{project_id} source_ids")
        _require(update is not None or bool(source_ids), f"Project {project_id} needs source_ids")
        url = project.get("project_url") or project.get("repo")
        if update is None or url:
            _url(url, f"{project_id} URL")
        key = url.rstrip("/").casefold() if url else None
        if "allow_shared_url" in record:
            _require(type(record["allow_shared_url"]) is bool, "allow_shared_url must be boolean")
        _require(key is None or key not in urls or record.get("allow_shared_url") is True,
                 f"Project {project_id} shares URL with {urls.get(key)}; use distinct project_url or allow_shared_url")
        if key is not None:
            urls[key] = project_id
        _require(isinstance(record.get("overall_state"), str) and record["overall_state"] in {"unreviewed", "partial", "reviewed"}, f"Project {project_id} needs explicit overall_state")
        areas = record.get("areas")
        _require(isinstance(areas, dict) and set(areas) == set(AREAS), f"Project {project_id} needs exactly these areas: {', '.join(AREAS)}")
        audit = {"project_id": project_id, "last_reviewed": day, "overall_state": record["overall_state"],
                 "areas": {}, "next_actions": []}
        note_parts, all_links = [], []
        for name in AREAS:
            area = areas[name]
            label = f"{project_id}.{name}"
            _require(isinstance(area, dict) and not set(area) - {"state", "narrative", "limitations", "next_action", "evidence_ids", "evidence_urls"},
                     f"{label} has unknown fields or is not an object")
            state = area.get("state")
            _require(isinstance(state, str) and state in AREA_STATES, f"{label} needs an explicit audit state")
            if require_ready and name in {"source_cpu", "target_cpu"}:
                _require(state != "unreviewed", f"{label} needs an explicit CPU audit decision")
            narrative = _text(area.get("narrative"), f"{label} narrative")
            links = []
            for proof_id in _strings(area.get("evidence_ids", []), f"{label} evidence_ids"):
                _require(proof_id in proof_urls, f"{label} references unknown proof {proof_id}")
                links.append(proof_urls[proof_id])
            for link in _strings(area.get("evidence_urls", []), f"{label} evidence_urls"):
                links.append(_url(link, f"{label} evidence URL"))
            links = list(dict.fromkeys(links))
            if state in {"reviewed", "not-applicable", "no-evidence-found"}:
                _require(bool(links), f"{label} needs evidence URLs or pinned proof references for its reviewed judgment")
            if "limitations" in area:
                narrative += " Limitations: " + _text(area["limitations"], f"{label} limitations")
            if "next_action" in area:
                action = _text(area["next_action"], f"{label} next_action")
                narrative += " Next check: " + action
                if action not in audit["next_actions"]:
                    audit["next_actions"].append(action)
            if state == "needs-research":
                _require("next_action" in area, f"{label} needs a concrete next_action")
            audit["areas"][name] = {"state": state, "checked_at": None if state == "unreviewed" else day,
                                      "note": narrative, "evidence_urls": links}
            note_parts.append(LABELS[name] + ": " + narrative)
            all_links.extend(links)
        project["notes"] = " ".join(note_parts)
        if all_links:
            project["notes"] += " Evidence: " + " ".join(dict.fromkeys(all_links))
        if update is not None:
            entry = {"project_id": project_id, "expected_sha256": update["expected_sha256"],
                     "changes": project, "audit": audit}
            if source_ids:
                entry["source_ids"] = copy.deepcopy(source_ids)
            if "allow_shared_url" in record:
                entry["allow_shared_url"] = record["allow_shared_url"]
            batch.setdefault("project_updates", []).append(entry)
        else:
            entry = {"project": project, "source_ids": copy.deepcopy(source_ids), "audit": audit}
            if "allow_shared_url" in record:
                entry["allow_shared_url"] = record["allow_shared_url"]
            batch["projects"].append(entry)
    _require(any(batch.get(field) for field in ("projects", "project_updates", "sources", "source_updates", "tasks", "task_updates", "decisions")),
             "Research document has no changes")
    # Cache only checked content. A cache hit never changes review or audit state.
    if cache is not None:
        for proof in proofs.values():
            if "text" in proof:
                cache.put(proof, proof["text"])
    return batch, proof_urls


def compile_records(document: dict, *, evidence_cache=None, expected_commits=None) -> dict:
    """Produce the unchanged legacy batch schema from an explicitly ready record.

    Full catalogue validation and collision checks against existing records remain
    the responsibility of apply_discovery_batch / the publication pipeline.
    """
    return _normalize(document, evidence_cache=evidence_cache,
                      expected_commits=expected_commits, require_ready=True)[0]


def render_report(document: dict, *, evidence_cache=None, expected_commits=None) -> str:
    """Render a draft or ready review, with unresolved areas first and exact values."""
    batch, proof_urls = _normalize(document, evidence_cache=evidence_cache, expected_commits=expected_commits)
    lines = ["# " + document.get("title", document["summary"]), "", document["summary"], "",
             f"Date: {document['date']} · Review: {document['review']['status']}", "",
             "Snapshot check: " + ("all pinned proofs match the supplied expected commits."
                                    if expected_commits is not None else "upstream heads were not checked; pinned evidence is a historical snapshot."), "",
             "## Uncertainty and next checks", ""]
    uncertainties = []
    for record in document.get("records", []):
        for name in AREAS:
            area = record["areas"][name]
            if area["state"] in {"unreviewed", "needs-research", "no-evidence-found"} or area.get("limitations") or area.get("next_action"):
                detail = area.get("limitations") or area["narrative"]
                if area.get("next_action"):
                    detail += " Next check: " + area["next_action"]
                project_id = record.get("update", {}).get("project_id") or record["project"]["id"]
                uncertainties.append(f"- {project_id} / {LABELS[name]} ({area['state']}): {detail}")
    lines.extend(uncertainties or ["No unresolved areas were flagged by the author."])
    report_entries = list(batch["projects"]) + [
        {"project": {"id": entry["project_id"], **entry["changes"]}, "audit": entry["audit"],
         "expected_sha256": entry["expected_sha256"]} for entry in batch.get("project_updates", [])]
    for entry in report_entries:
        project, audit = entry["project"], entry["audit"]
        lines.extend(["", "## " + project.get("display_title", project.get("title", project["id"])), "",
                      f"Project ID: {project['id']} · Overall audit: {audit['overall_state']}", "",
                      "### Typed catalogue changes" if "expected_sha256" in entry else "### Typed catalogue values", "", "```json",
                      json.dumps({key: value for key, value in project.items() if key != "notes"},
                                 indent=2, ensure_ascii=False, sort_keys=True, allow_nan=False), "```"])
        if "expected_sha256" in entry:
            lines.extend(["", "Expected existing project SHA256: " + entry["expected_sha256"]])
        for name in AREAS:
            area = audit["areas"][name]
            lines.extend(["", f"### {LABELS[name]} ({area['state']})", "", area["note"]])
            lines.extend("- " + url for url in area["evidence_urls"])
    if proof_urls:
        lines.extend(["", "## Pinned evidence manifest", ""])
        for proof_id in sorted(proof_urls):
            proof = proof_identity(document["proofs"][proof_id])
            lines.append(f"- {proof_id}: {proof_urls[proof_id]} (Git blob {proof['blob']})")
    for field in ("sources", "source_updates", "tasks", "task_updates", "decisions", "source_ids"):
        if batch.get(field):
            lines.extend(["", "## " + field.replace("_", " ").capitalize(), "", "```json",
                          json.dumps(batch[field], indent=2, ensure_ascii=False, sort_keys=True, allow_nan=False), "```"])
    if document.get("notes"):
        lines.extend(["", "## Research event notes", "", document["notes"]])
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path, help="Write the compatible legacy batch")
    parser.add_argument("--report", type=Path, help="Write a Markdown report (drafts allowed)")
    parser.add_argument("--cache", type=Path, help="Local pinned UTF-8 evidence cache")
    parser.add_argument("--expected-commits", type=Path, help="JSON map of repository URLs to separately observed current commit SHAs")
    parser.add_argument("--seal", type=Path, help="Explicitly record ready review/digest in a new research document after reviewing it")
    args = parser.parse_args()
    try:
        document = json.loads(args.input.read_text(encoding="utf-8"))
        kwargs = {"evidence_cache": args.cache, "expected_commits":
                  json.loads(args.expected_commits.read_text(encoding="utf-8")) if args.expected_commits else None}
        # Validate everything requested before creating output artifacts.
        sealed = seal_review(document) if args.seal else None
        report = render_report(sealed or document, **kwargs) if args.report or args.seal else None
        output = compile_records(sealed or document, **kwargs) if args.output or not (args.report or args.seal) else None
        if args.report:
            args.report.write_text(report, encoding="utf-8")
        if args.seal:
            args.seal.write_text(json.dumps(sealed, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        if args.output:
            args.output.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        elif output is not None:
            print(json.dumps(output, indent=2, ensure_ascii=False))
    except (OSError, ValueError, TypeError, KeyError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
