# Discovery batch workflow

Keep a research pass together. Review primary project pages first, then create one JSON batch. Do not mark unknown build, AI, CPU or runtime facts false. Record non-promotions in `data/discovery-decisions.json` so the same lead need not be reassessed from scratch.

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

Assign the source platform from the binary, media, or data actually analyzed. A historical release on another platform, a palette setting, or a new port's target platform does not establish analysis of that platform's original version. When a repository mixes copied templates and project-specific work, inspect the files and promote the verified part at its actual platform and stage. Do not infer a working port from a ROM listing or a copied makefile.

Use `duplicate` for a continuation or mirror already represented by the same research lineage; link the existing project. Use `excluded` when a candidate contains only unanalysed binaries/assets, merely converts somebody else's analysis, or is an ordinary port unrelated to the catalogue's recovery and tooling scope. Use `deferred` only when a specific unresolved fact would change whether or how a distinct record can be made. Name the file or missing evidence and the next check in the reason. For collections, decide separately for each reviewed component and defer only the components still unexamined. Lack of a complete README or playability by itself is not a deferral reason.

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
