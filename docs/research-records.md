# Author research once

`tools/research_record.py` is an optional authoring layer over the existing
[discovery batch](discovery-workflow.md). It does not change the catalogue schema,
migrate existing records, fetch evidence, or make substantive judgments.

Keep typed project values in `project`, and write each audit area's narrative
once. The compiler generates `project.notes`, the corresponding audit `note`, and
a review report from those same narratives. Do not copy prose into all three
places. CPU, build, runtime, AI, identity and relationship judgments remain
independent and author-owned. `null` stays `null`; neither a cache hit nor a
sentence in an evidence file changes a project fact or audit state.

## Shape

A document has:

- `format`: `research-records/v1`
- The existing batch `date`, `event_id`, `summary`, and optional `notes`, `kind`,
  `sources`, `source_updates`, `tasks`, `task_updates`, `decisions`, `source_ids`
- Optional `title` for the report; otherwise `summary` is used
- `review`: `{"status": "draft"}` or `{"status": "ready"}`; optional `digest`
- `records`: the projects researched in this pass
- Optional `proofs`: an object indexed by author-chosen evidence IDs

Each new record contains `project` (the full existing typed project schema,
without `notes`), nonempty `source_ids`, explicit `overall_state`, and `areas`.
The overall state is `unreviewed`, `partial`, or `reviewed`, as decided by the
author. A shared project URL requires `allow_shared_url: true`, just as in the
existing batch format.

All eight areas are explicit: `identity`, `classification`, `source_cpu`,
`target_cpu`, `build`, `runtime_profiles`, `ai`, and `relationships`. Each has:

- `state`: one of the existing audit states
- `narrative`: the evidence-based judgment, including the actual scope inspected
- Optional `limitations`: a distinct uncertainty or boundary worth highlighting
- Optional `next_action`: a concrete follow-up; required for `needs-research`
- `evidence_urls` and/or `evidence_ids`: primary URLs or references to pinned proofs

Reviewed, not-applicable, and no-evidence-found areas need at least one evidence
URL or proof reference. An unreviewed area's generated `checked_at` stays `null`.
CPU areas cannot remain unreviewed when compiling a ready batch. The compiler
checks structure, not whether the research justifies a judgment: the author must
still inspect the evidence. `no-evidence-found` never sets a fact to `false`.

### Small fictional example

This illustrates authoring, not research about a real project. Replace the
example facts, URLs and source ID with primary-source findings before using it.
The source ID must exist in the tracker or in this document's `sources` array.

```json
{
  "format": "research-records/v1",
  "date": "2026-10-06",
  "event_id": "2026-10-06-example-source-review",
  "summary": "Review Example Game's source archive",
  "review": {"status": "draft"},
  "records": [{
    "source_ids": ["your-reviewed-source-id"],
    "overall_state": "partial",
    "project": {
      "id": "example-source-archive",
      "title": "Example Game",
      "upstream_name": "Example Game",
      "display_title": "Example Game source archive",
      "subjects": ["Example Game"],
      "repo": "https://example.org/game",
      "source_platforms": ["Amiga"],
      "target_platforms": [],
      "source_cpu": ["m68k"],
      "target_cpu": [],
      "runtime_profiles": [],
      "source_language": ["m68k assembly"],
      "reconstructed_languages": [],
      "record_class": "subject",
      "target_kinds": ["game"],
      "work_kinds": ["source-restoration"],
      "tool_kinds": [],
      "types": ["original-source archive"],
      "re_started": null,
      "last_activity": null,
      "last_checked": "2026-10-06",
      "status": "Source archive; build untested",
      "build": {"compilable": null, "runnable": null, "playable": null, "byte_exact": null},
      "ai": {"usage": null, "tools": []},
      "techniques": [],
      "tags": []
    },
    "areas": {
      "identity": {
        "state": "reviewed",
        "narrative": "The author page identifies the archive as the original Example Game source release.",
        "evidence_urls": ["https://example.org/game"]
      },
      "classification": {
        "state": "reviewed",
        "narrative": "This is original-source preservation; no binary-derived reconstruction is claimed.",
        "evidence_urls": ["https://example.org/game"]
      },
      "source_cpu": {
        "state": "reviewed",
        "narrative": "The reviewed listing uses Motorola data/address registers and 68k instructions.",
        "evidence_urls": ["https://example.org/game/source"]
      },
      "target_cpu": {
        "state": "no-evidence-found",
        "narrative": "The reviewed material does not establish a reconstruction output architecture.",
        "evidence_urls": ["https://example.org/game"]
      },
      "build": {
        "state": "reviewed",
        "narrative": "Source is preserved; the page does not establish a successful rebuild.",
        "limitations": "No compilation, execution, gameplay or byte comparison was performed.",
        "evidence_urls": ["https://example.org/game"]
      },
      "runtime_profiles": {
        "state": "no-evidence-found",
        "narrative": "No minimum runnable hardware was established by the inspected source and page.",
        "evidence_urls": ["https://example.org/game"]
      },
      "ai": {
        "state": "no-evidence-found",
        "narrative": "The inspected page contains no development-AI disclosure; absence does not establish non-use.",
        "evidence_urls": ["https://example.org/game"]
      },
      "relationships": {
        "state": "needs-research",
        "narrative": "A predecessor link is present, but its relationship has not been checked.",
        "next_action": "Inspect the linked predecessor's author and history.",
        "evidence_urls": ["https://example.org/game"]
      }
    }
  }]
}
```

There is no generated classification or boilerplate fallback for a missing area.
Write the distinct judgment, including the reason for `not-applicable`, rather
than cloning another area's narrative. Additional typed project evidence blocks
are passed through intact. Existing source/task/decision entries use their
existing schemas and are included in the report without reinterpretation.

## Preview, review and compile

```sh
python tools/research_record.py research.json --report /tmp/research-review.md
# Inspect the report, especially uncertainties, exact typed values and evidence.
# Then explicitly mark review.status ready, or record a ready digest:
python tools/research_record.py research.json --seal /tmp/research-ready.json
python tools/research_record.py /tmp/research-ready.json --output /tmp/legacy-batch.json
python tools/apply_discovery_batch.py /tmp/legacy-batch.json
```

The report highlights unknowns, limitations and next checks before the project
views. The legacy helper still runs full cross-file validation and checks
collisions against the existing catalogue. Its dry run changes no catalogue data.
Use the publication pipeline's exact data diff and snapshot checks before writing
or publishing. The report supplements that diff; it does not replace it.

`compile_records(document, *, evidence_cache=None, expected_commits=None)` returns
a compatible batch dictionary. `render_report` takes the same arguments and
returns reproducible Markdown, allowing drafts. Both leave the input unchanged.
Audit areas have stable order; dictionary insertion order does not affect the
report or digest. No clock, network request, current directory or live metadata
is used to infer facts.

`review.status = ready` is the author's explicit declaration. The optional
`seal_review(document)` helper and `--seal` copy the document with ready status
and a SHA256 digest of its authored contents. They do not approve the research.
When a digest exists, changed project facts, narratives, limitations, source
updates or proof identities produce a stale-review error. After reviewing a
change, explicitly reseal it. Do not auto-seal merely because validation passed.
The publication pipeline separately binds the generated files and exact diff to
its preview receipt.

## Existing project updates

A record can instead have:

```json
"update": {
  "project_id": "existing-project-id",
  "expected_sha256": "SHA256_OF_THE_COMPLETE_EXISTING_PROJECT_RECORD"
}
```

For an update, `project` contains only the explicit top-level changes, without
`notes`; `id` can be omitted or must match. Use the batch helper's canonical
project digest from the exact reviewed baseline. Omitted fields survive; supplied
nested objects replace that entire top-level value, so include every child field
that must remain. The compiler creates `project_updates` with `changes`, a full
explicit replacement audit, and optional `source_ids`. Generated notes replace
the prior note, so carry forward relevant existing narrative when researching an
update. There is no automatic interpretation of prior notes or audit judgments.

## Immutable evidence cache

Plain `evidence_urls` are retained verbatim as author citations. For reusable
GitHub UTF-8 file evidence, use a proof with an exact repository root, full commit
SHA, relative file path and full Git blob SHA:

```json
"proofs": {
  "readme": {
    "repository": "https://github.com/OWNER/REPO",
    "commit": "FULL_40_CHARACTER_COMMIT_SHA",
    "path": "README.md",
    "blob": "FULL_40_CHARACTER_GIT_BLOB_SHA"
  }
}
```

Reference it with `"evidence_ids": ["readme"]` in any relevant area. The cache is
local working data, not a new catalogue field. Populate it from the primary file
bytes and the GitHub response's observed commit/path/blob identity:

```python
from pathlib import Path
from research_record import EvidenceCache

# proof contains the repository, commit, path and observed Git blob SHA above.
# Preserve exact UTF-8 bytes, including CRLF if present.
text = Path("/tmp/reviewed-README.md").read_bytes().decode("utf-8")
EvidenceCache("/tmp/research-evidence").put(proof, text)
```

A proof can alternatively include `text` to seed the cache using `--cache`.
Large source bodies should stay in the local cache. Neither compiled batches nor
reports include cached source bodies. Omit inline text after caching; this does
not change the review digest because the Git blob SHA already binds the bytes.
Binary evidence remains a normal citation rather than being decoded as text.

```sh
python tools/research_record.py research-ready.json \
  --cache /tmp/research-evidence \
  --expected-commits /tmp/observed-heads.json \
  --report /tmp/research-review.md --output /tmp/legacy-batch.json
```

`observed-heads.json` maps repository root URLs to full commit SHAs independently
observed by the collector/reviewer. When supplied, every proof's repository must
be present and its pinned commit must match. A changed head is a deliberate stop
for inspection, not permission to silently relabel old evidence as current. A
new commit, path, repository or blob has a different cache key, even when some
file contents happen to remain the same. Corrupt contents, conflicting blobs at
the same immutable path, wrong cache identity and missing pinned files all fail.

Without `expected_commits`, only pinned-snapshot integrity is checked. The report
says upstream heads were not checked. Providing a stale mapping cannot establish
current freshness: this module does not contact GitHub. Git blob verification
proves the bytes match the declared blob, not that the commit actually contains
that file or that a source made a claim. Establish commit/tree membership and
provenance when collecting it. Reusing verified bytes saves retrieval work; it
never carries forward substantive approval or changes review states.

Run the focused checks with:

```sh
python -m unittest discover -s tools -p 'test_research_record.py' -v
```
