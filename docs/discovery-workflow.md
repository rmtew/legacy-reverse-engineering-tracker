# Discovery batch workflow

Keep a research pass together. Review primary project pages first, then create one JSON batch. Do not mark unknown build, AI, CPU or runtime facts false. Record non-promotions in `data/discovery-decisions.json` so the same lead need not be reassessed from scratch.

## Batch input

The root object requires `date` (ISO calendar date), a unique `event_id`, and `summary`. Optional `notes` and `kind` describe the research event. Supported arrays:

| Field | Contents |
| --- | --- |
| `projects` | `{ "project": <full project record>, "source_ids": ["existing-or-new-source-id"], "audit": <optional full audit>, "allow_shared_url": true|false }` |
| `sources` | New source records in the discovery-source schema. Missing index/review dates, review state, and link arrays receive conservative defaults. |
| `source_updates` | Existing source `id`, plus `review_state`, `reason`, or `last_reviewed`. Project links are added automatically from `projects`. |
| `tasks` | New backlog records. Open tasks are linked to their `source_ids`. |
| `task_updates` | Existing task `id`, plus `state`, `notes_append`, or `last_reviewed`. Completed/deferred tasks are removed from sources' open-task lists. |
| `decisions` | Candidate decisions in the [schema](../schema.md), with `reviewed_at` and `project_ids` optional when not applicable. |
| `source_ids` | Additional existing sources reviewed in the pass; included in the research event. |

`project` follows the full `data/projects.json` schema. The helper creates an **unreviewed** audit if the entry omits `audit`; supply an explicit audited record when fields have actually been checked. Each project needs at least one source ID. URLs shared by independent projects require `allow_shared_url: true` in that entry. The helper refuses an existing project ID, decision ID, event ID, or decision URL. It checks each new project's `project_url` (falling back to `repo`) for collisions; a shared repository with distinct project pages is fine.

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
