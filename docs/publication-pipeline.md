# Compact reviewed research publication

Research remains human/model-authored and evidence-reviewed. The supported online
route sends one small reviewed delta to trusted main; GitHub Actions expands and
validates it against current main. Canonical partitions, generated reports and
projections stay on the runner instead of crossing the connector.

## Prepare and submit

Author `research-records/v1` using [the research record guide](research-records.md).
Review the typed values, primary evidence and uncertainties, then explicitly seal:

```sh
python tools/research_record.py research.json --seal /tmp/reviewed.json
python tools/research_submission.py prepare /tmp/reviewed.json --out /tmp/research-submit
```

The second command creates an ordinary `publish_discovery.js` bundle containing
only `submissions/research/<event_id>.json`. Use that existing connector publisher
with the bundle, current main baseline and its resumable checkpoint. A native
Git client may instead commit that one payload file to main. Newly prepared
bundles explicitly identify the single sealed compact submission. If main
advances, the connector publisher refreshes only its parent/tree, with at most
three fast-forward attempts per invocation. Reviewed input bytes, digest and the
original manifest stay unchanged; uploaded immutable blobs are reused. Resume
the same bundle/checkpoint after interrupted or exhausted attempts.

An identical existing submission (including equivalent JSON serialization) or
matching applied receipt is success without rewriting it. A conflicting event
ID fails. Uncertain ref-update responses are resolved by reading remote state
before another write; an unchanged ambiguous outcome stops for checkpoint
resume. Authorization denials are never retried automatically. Code, expanded
catalogue bundles and older unmarked bundles retain strict baseline checks.
Never upload expanded catalogue partitions for a new research pass.
`package` can produce a single compact input file for native Git transport.

The route requires a ready review digest, inline pinned proof text (or `--cache`
to embed verified cached text), at most 100 project records / 500 batch entries,
and at most 1 MiB of UTF-8 input. The JSON-escaped connector request must also fit
the shared 4 MiB ceiling. IDs are safe filename components of at most 128
characters. Oversized passes must be split and reviewed explicitly.

A seal records an author review and protects content integrity; it cannot prove
that the judgments are correct. Only writers authorized to commit to main may
submit. An external PR or self-sealed attachment receives no write privileges.

## Atomic apply and stable receipts

`apply-research.yml` runs trusted main code on main pushes, manual runs and an
hourly recovery wake-up. It reads only committed JSON inputs and processes at
most four pending events per run. Missed or coalesced wake-ups remain discoverable
in the inbox; there is no recursive workflow continuation.

For each event, Actions reuses the existing compiler, discovery application,
publication preservation checks and full data validator. It builds and validates
site/RSS projections in isolation, then commits changed canonical partitions,
research provenance/report, an immutable `state/research-receipts/<event_id>.json`
and a small durable outbox entry together. A receipt binds event ID, reviewed
content digest, input blob, baseline, report hash and applied summary. It never
copies the catalogue. Unchanged existing projects/audits must remain exact.

Fast-forward push conflicts retry against latest main up to three times, with
fresh validation. Concurrent metadata is retained. Explicit existing-project
updates still require their authored expected SHA; conflicts need another review.
A concurrent change to publication tools requires rerunning the trusted job.

Same ID and identical reviewed content is a no-op. Conflicting content under an
existing ID fails clearly. IDs already published by the legacy path cannot be
silently adopted. Inputs and receipts retain provenance; do not edit completed
submissions to reuse their IDs.

## Handoff and recovery

Only after a successful commit/push does Actions dispatch the existing durable
metadata/activity refresh for project changes, using a stable request identity.
First scans cover 30 days; historical head/release lookups still recover old
upstream dates without putting expired commits in the timeline. Pages uses the
existing shared completeness/material-change gate, so new catalogue records
cannot deploy before initial enrichment and catalogue events are complete.
Research-only changes use that same Pages gate directly.

The outbox is acknowledged only after handoff succeeds. A crash after publication
or notification failure leaves the receipt and pending outbox intact. Rerun the
job, manually run **Apply reviewed research submissions** with its `event_id`, or
allow the hourly recovery run. Replays do not duplicate projects, research events
or reports. Completed acknowledgements do not dispatch workflows again.
Publication commands reset a dedicated checkout; use them in Actions, not a
shared working tree with uncommitted work.

Check the stable receipt, the metadata workflow when applicable, and the actual
successful Pages deployment. Pages validates canonical data, the 30-day browser
projection and RSS at the pinned exported commit. Existing remote/live bundle
verification commands remain available for already-authored legacy publications.

## Transition

The expanded `publication_pipeline.py prepare` format is retained for native
server-side application, old checkpoints and exceptional catalogue repair.
`publish_discovery.js` also remains the connector transport for code/maintenance
commits. These are not alternative automatic research-ingestion routes.
The old `automation/discovery-*` fast-forward landing workflow is removed;
research submissions cannot replace executable tools/workflows or choose output
paths/commands. Legacy batch input and historical publication verification remain
readable through their existing tools.
