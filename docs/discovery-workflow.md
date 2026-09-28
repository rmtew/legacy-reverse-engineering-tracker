# Discovery batch workflow

Keep a research pass together. Screen candidate URLs, review primary project pages, then create one JSON batch. Do not mark unknown build, AI, CPU or runtime facts false. Record non-promotions in `data/discovery-decisions.json` so the same lead need not be reassessed from scratch.

## Screen search results

Start with `python tools/discovery_intake.py --list 30` to review the saved queue. Known repository rows include locally matched project IDs so a reviewer can check existing title coverage before requesting repository files. A daily Action and manually dispatched runs collect bounded GitHub searches and revisit known profiles, repositories and website sources. Each queued URL includes its route and query/source of origin, first/last sighting and a cheap relevance score. Platform-focused README and code searches receive a small ranking adjustment when the repository title/description matches or mismatches the query's platform; mismatches stay in the queue. A candidate already promoted or excluded is removed on the next run; deferred decisions remain for follow-up. The ranked queue is a work list, not a project recommendation or a claim of qualification. Search recipes and budgets live in `config/discovery-intake.json`; run outcomes live in `state/discovery-intake.json`. The [first 30 review](discovery-intake-first-30-2026-09-27.md) records outcomes and the next programmatic opportunities.

For a bounded read-only evidence pass, `python tools/discovery_triage.py --limit 30 --output /tmp/discovery-triage.json` reads each repository root or a queued `tree/<branch>/<directory>` path and its README if present (at most 60 requests). A tree path uses a single-segment branch name, keeps directory signals scoped, and pins both requests to that branch. It lists up to 20 distinct external GitHub repository roots from a README as lineage leads. It screens every observed README link against the local catalogue, even past the 20-link display cap, and reports status counts and up to 20 new roots. Landing-page repository links receive the same local screening. These extra checks make no API requests and do not classify a project. If there is no README but there is an `index.html`, it reads the page instead and lists up to 50 distinct outbound GitHub repository roots. It reports filenames, limited file-type signals (including release artifacts, .6502 assembly and analysis workbooks) and the opening README text, recognizing mixed capitalization and two-suffix translations and preferring a plain or English README. It does not change the queue or classify a project. A saved ordered queue snapshot may be supplied with `--input`; see the [second 30 review](discovery-intake-second-30-2026-09-27.md) for examples where signals helped and where they were insufficient. Use a GitHub token for the batch to avoid exhausting unauthenticated API quota.

Directory-name review hints (`root_signals.review_directories`) flag likely nested tools, ROM listings, source and disassembly folders in the same listing response, with no added requests. Inspect the indicated path and its adjacent README before classifying; these names do not establish provenance or project independence.

For a more varied review slice, `python tools/discovery_intake.py --list 30 --max-per-profile 4` limits siblings discovered from one GitHub profile in the displayed first pass and fills any spare slots from the remaining ranked leads. The persisted queue is unchanged. The [third 30 review](discovery-intake-third-30-2026-09-27.md) records the profile-heavy batch that motivated this option and an example where separate projects lived below a repository with no root README. The [fourth 30 review](discovery-intake-fourth-30-2026-09-27.md) documents platform-mismatched code hits and a cluster of releases containing three developer artifacts. The [fifth 30 review](discovery-intake-fifth-30-2026-09-27.md) documents covered repository roots, a site index and a machine-readable manifest. The [sixth 30 review](discovery-intake-sixth-30-2026-09-27.md) documents workbooks, translated READMEs and source nested inside a hardware repository. The [seventh 30 review](discovery-intake-seventh-30-2026-09-27.md) documents predecessor links, game-specific interpreters and misleading repository names. The [eighth 30 review](discovery-intake-eighth-30-2026-09-27.md) covers nested Amiga tools, shared source libraries and unavailable links. The [ninth 30 review](discovery-intake-ninth-30-2026-09-28.md) covers X68000 tooling, fork divergence and nested ROM research. The [tenth 30 review](discovery-intake-tenth-30-2026-09-28.md) covers package aliases, original-source provenance, and local screening of large README indexes.

For a chat-triggered pass, run the intake command locally or dispatch `discovery-intake.yml` from GitHub Actions; `--input candidate_urls.json --offline` adds externally discovered hits without network calls. The Action's optional `candidate_urls` input accepts newline-separated links and also runs the saved recipes. New web search queries still require a search provider or manual search, then URL import. Neither the CI refresh of tracked repositories nor this intake collector evaluates whether a new project belongs in the catalogue.

A reviewed GitHub source at `tree/<branch>/<directory>` revisits that directory directly: one contents request lists child directories as leads, and one optional README request supplies outbound repository links. This is bounded by the existing source-link limit. Preserve branch and directory in follow-up URLs; a root repository read can miss independent tools below a collection directory.

Pass an entire result page to the local index before requesting each README or another GitHub API lookup:

```sh
python tools/screen_discovery_candidates.py --input candidates.txt --route 'repository search'
python tools/screen_discovery_candidates.py --input candidates.json --json
```

Input is one URL per line, or a JSON array of URL strings and/or `{ "url": "...", "route": "web search" }` entries. Positional URLs and `--input -` (stdin) also work. The output identifies exact tracked projects, reviewed decisions (including their decision type and linked project URLs), known sources, known repositories and paths within them, new URLs, and repeated hits in this input. JSON output includes counts by route. Compare new and reviewed hits across search routes before repeating broad queries.

The index removes fragments and tracking parameters, normalizes GitHub owner/repository spelling and routine slash/scheme differences, and keeps paths and meaningful query parameters distinct. It makes no network requests: a previously unseen redirect cannot be detected until investigated. Record confirmed old/redirecting URLs as `duplicate` decisions linked to their current project IDs; subsequent searches then resolve them locally. A known source/profile can point to new repositories. A known repository can contain new title-specific directories. Deferred decisions and unreviewed sources still need follow-up. Only use an exact project or resolved exclusion/duplicate decision to avoid repeating the same research.

## Batch input

The root object requires `date` (ISO calendar date), a unique `event_id`, and `summary`. Optional `notes` and `kind` describe the research event. Supported arrays:

| Field | Contents |
| --- | --- |
| `projects` | `{ "project": <full project record>, "source_ids": ["existing-or-new-source-id"], "audit": <required researched audit>, "allow_shared_url": true|false }` |
| `sources` | New source records in the discovery-source schema. Missing index/review dates, review state, and link arrays receive conservative defaults. |
| `source_updates` | Existing source `id`, plus `review_state`, `reason`, or `last_reviewed`. Project links are added automatically from `projects`. |
| `tasks` | New backlog records. Open tasks are linked to their `source_ids`. |
| `task_updates` | Existing task `id`, plus `state`, `notes_append`, or `last_reviewed`. Completed/deferred tasks are removed from sources' open-task lists. |
| `decisions` | Candidate decisions in the [schema](../schema.md), with `reviewed_at` and `project_ids` optional when not applicable. |
| `source_ids` | Additional existing sources reviewed in the pass; included in the research event. |

`project` follows the full `data/projects.json` schema. Every new project requires an explicit audit reviewed on the batch date. Decide both `source_cpu` and `target_cpu` from primary evidence at creation: use `reviewed` for verified values, `not-applicable` for data-only work where an original/target CPU does not sensibly apply, `no-evidence-found` after an actual search, or `needs-research` with a concrete next action. Do not infer a minimum runnable CPU from a platform or from the source architecture. The helper rejects omitted or wholly unreviewed CPU audits. Run `python tools/cpu_audit_queue.py --limit 20` to select unresolved existing projects for subsequent research. Each project needs at least one source ID. URLs shared by independent projects require `allow_shared_url: true` in that entry. The helper refuses an existing project ID, decision ID, event ID, or decision URL. It checks each new project's `project_url` (falling back to `repo`) for collisions; a shared repository with distinct project pages is fine.

For a decision-only pass, a batch can look like this after replacing the example details with a real reviewed lead:

```json
{
  "date": "2026-09-25",
  "event_id": "2026-09-25-example-review",
  "summary": "Reviewed an unpromoted candidate",
  "source_ids": ["web-6502disassembly-com"],
  "decisions": [
    {
      "id": "example-conversion-decision",
      "title": "Example conversion",
      "url": "https://example.org/project",
      "decision": "excluded",
      "reason": "The primary page says this is only a conversion of an existing listing.",
      "evidence_urls": ["https://example.org/project"],
      "source_ids": ["web-6502disassembly-com"]
    }
  ]
}
```

`excluded` means this specific candidate does not warrant an independent catalogue record. `duplicate` points to a tracked equivalent, `deferred` needs more evidence, and `promoted` references one or more tracked project IDs. Preserve the predecessor's identity in the reason instead of implying that the underlying research has no value.

### Decide at the demonstrated scope

Include a distinct project when its public artifacts establish concrete work on historical software or directly relevant development/recovery tooling. A disassembly, parser, unpacker, patcher, research script, experimental port, or documented distributed tool can qualify without a playable game, complete format support, detailed README, bundled original data, or published source for a binary tool. Describe the part that actually exists and leave build, runtime, provenance, and byte matching unknown unless verified. Historical original-source archives qualify as development tooling when they provide a substantive period system, but do not label them binary-derived reconstructions without evidence.

Link a project to the repository root when its archive, implementation, documentation and tools form one coherent work. Keep a directory URL when the repository contains genuinely separate projects and that directory identifies the independently tracked work. A useful tool or disassembly found in a folder is evidence for the parent project; it does not by itself require a directory-scoped record.

Assign the source platform from the binary, media, or data actually analyzed. A historical release on another platform, a palette setting, or a new port's target platform does not establish analysis of that platform's original version. When a repository mixes copied templates and project-specific work, inspect the files and promote the verified part at its actual platform and stage. Do not infer a working port from a ROM listing or a copied makefile.

Use `duplicate` for a continuation or mirror already represented by the same research lineage; link the existing project. Use `excluded` when a candidate contains only unanalysed binaries/assets, merely converts somebody else's analysis, or is an ordinary port unrelated to the catalogue's recovery and tooling scope. Use `deferred` only when a specific unresolved fact would change whether or how a distinct record can be made. Name the file or missing evidence and the next check in the reason. For collections, decide separately for each reviewed component and defer only the components still unexamined. Lack of a complete README or playability by itself is not a deferral reason.

For linked README dependency lists, `python tools/discovery_intake.py --list 30 --max-per-source 4` caps the number displayed from one source (profile or repository), then fills spare slots in rank order. It keeps every skipped URL in the saved queue and makes no eligibility decision. The [eleventh 30 review](discovery-intake-eleventh-30-2026-09-29.md) records the motivating case.

## Preview and apply

```sh
python tools/apply_discovery_batch.py path/to/batch.json
python tools/apply_discovery_batch.py path/to/batch.json --write
python tools/validate_site_data.py data/projects.json data/activity.json
git diff --check
git diff --stat
```

The first command stages the proposed data in a temporary directory and runs the full validator without changing the repository. `--write` repeats validation and writes the related files only after it succeeds. Review the resulting diff, including the exact source links and candidate reasons. Commit the complete diff **once**, with any required code or documentation changes, so refresh/deployment workflows never see a half-updated catalogue.

## Publish and verify

Fetch current `main` before publishing. In Codex Work, use the linked GitHub connector for repository writes: create blobs for each changed file, create one tree based on the current `main` tree, create one commit with the current `main` commit as its parent, and fast-forward `main` with `force: false`. Compare blob/tree SHAs with the validated local files when possible. If `main` advanced, rebase/revalidate rather than force an update. An authenticated Git client may instead push one validated commit; do not assume this workspace's shell has credentials.

For a batch that merits a branch review, `automation/discovery-*` triggers the existing landing workflow. It validates, fast-forwards `main`, dispatches the refresh, and removes the branch on success. Direct connector commits on `main` trigger the ordinary push refresh when the catalogue changes. After publication, confirm the metadata refresh and subsequent Pages `workflow_run` deployment for catalogue changes; a research-index-only pass deploys through the direct Pages push run. If a workflow fails, inspect its actual failing step before starting another discovery batch.
