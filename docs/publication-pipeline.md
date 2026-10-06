# Repeatable research publication

The research decisions remain human/model-authored and evidence-reviewed. The
pipeline removes repeated formatting, staging and verification scripts. It does
not invent CPU/platform corrections, decide that an untested game works, or
turn an unknown AI claim into a negative answer.

## 1. Research and review

Prefer the [single-authoring record](research-records.md): write each area's
judgment once and generate the project note, audit and report. Existing legacy
batches are still accepted without migration. Reuse pinned repository/commit/
blob evidence when its upstream snapshot is unchanged. Verify current upstream
heads before supplying `--expected-commits`; the compiler cannot establish
freshness or source provenance by itself.

Review uncertain claims and the exact typed changes. Ready status or an optional
review digest records that decision; passing a structural validator does not
make research approved. Keep distinct reasoning for original-platform/CPU,
output-platform/CPU, runtime, source lineage and licensing.

## 2. Prepare once against an exact baseline

Obtain the current main SHA and complete recursive tree through GitHub. Use a
checkout or connector-materialized snapshot whose input bytes match that tree.
The output must be a separate directory:

```sh
python tools/publication_pipeline.py prepare research.json \
  --root /path/to/reviewed-checkout --out /tmp/reviewed-publication \
  --baseline FULL_MAIN_COMMIT_SHA --baseline-tree /tmp/main-tree.json
```

Optional structured-record arguments are `--evidence-cache` and
`--expected-commits`. This performs one whole-data validation, preserves all
unmodified project/audit objects, and emits:

- `payload/`: staged catalogue files and generated report/index entries
- `manifest.json`: baseline, exact file hashes, counts and stage timings
- `review.json`: exact field before/after values and uncertain audit areas
- `batch.json`: the compiled compatible delta

The source checkout is untouched. Repeating the same preparation checks and
reuses its output. Changed inputs, stale baseline bytes, modified output or an
incomplete bundle require a fresh output directory. Duplicate event IDs remain
an error; they never silently append another research event.

Legacy batches support `project_updates` as well as additions. Each update has
`project_id`, `expected_sha256`, `changes`, and a full explicit replacement
`audit`; optional source links and `allow_shared_url` follow addition rules.
Calculate the expected digest using `publication_pipeline.digest(project)` on
the exact reviewed record. Changes are shallow: omitted fields survive, supplied
nested objects replace that top-level value. IDs cannot be renamed through this
helper. A stale or duplicate update fails before any source file is written.

## 3. Publish the reviewed manifest

Review `review.json`, the generated report and manifest. Run repository tests
once against the final code/data, not once per formatting pass:

```sh
python -m unittest discover -s tools -p 'test_*.py'
node --test tools/test_cpu_filters.js tools/test_publish_discovery.js
python tools/publication_pipeline.py verify-files /tmp/reviewed-publication
git diff --check
```

For an authorized connector publication, load `tools/publish_discovery.js` into
`functions.exec` without printing its payload and invoke:

```js
await publishDiscovery(tools, {
  repository: "rmtew/legacy-reverse-engineering-tracker",
  branch: "EXISTING_AUTHORIZED_BRANCH",
  bundle: "/tmp/reviewed-publication",
  message: "Publish reviewed research batch"
});
```

The adapter takes the real available connector tools; it does not require a
token, invent a local-file upload API, create a branch, approve a review or open
a PR. It uploads only changed manifest files, verifies returned blob hashes,
creates one tree and commit, advances the chosen ref with `expected_sha` and
`force: false`, then verifies the remote ref and complete file tree. Its local
checkpoint reuses already-verified blobs. A lost ref-update response is resolved
by reading the ref on resume; an advanced head requires preparation/review
against the new baseline, never a blind force or replay over another commit.

The connector currently accepts text. Bounded shell reads keep multi-megabyte
payloads out of model context, but they are still transfer overhead. This driver
automates that bridge; it does not claim to eliminate it. Keep its checkpoint
with the bundle until publication verification finishes.

Do not use an `automation/discovery-*` branch for a draft code PR: that existing
workflow fast-forwards main. Use that route only for an authorized, reviewed data
publication. Code/tool/workflow changes should have their normal review first.

## 4. Complete enrichment, deployment and served verification

A main push scopes metadata and history to repositories whose authored catalogue
records changed. Shared repositories are fetched once. The scoped path forces
complete first-scan metadata, historical head/release context and a full 180-day
branch/path backfill, subject to existing rate/request/time safety limits.
Incomplete work remains pending and cannot be described as a completed addition.
Normal schedules and manual dispatches without publication inputs retain broad
adaptive polling. They can recover pending first scans.

Recovery work in each adaptive metadata/history phase has a shared request slice
(at most 25% of usable capacity, capped at 1,000 calls), leaving capacity for
ordinary maintenance. Every refresh reconciles still-unrecorded catalogue changes,
including when a previous publication run was replaced by a later code-only push. A first scan too large for existing safety limits
stays pending with a diagnostic; there is no unsafe partial-completion shortcut.
This change does not introduce resumable page cursors or increase quota limits.

For a bot landing, `land-discovery.yml` dispatches immutable `publication_base`
and `publication_head` SHAs. Manual publication retries should pass both:

```sh
gh workflow run refresh-github.yml --ref main \
  -f publication_base=FULL_BASE_SHA -f publication_head=FULL_AUTHORED_SHA
```

Wait for successful metadata and Pages runs for the expected publication. For
authored commit verification, fetch its complete tree and run:

```sh
python tools/publication_pipeline.py verify-remote /tmp/reviewed-publication authored-tree.json
```

Download served `data/{projects,activity,project-audits,discovery-sources,
discovery-decisions,research-activity,activity-30d,activity-180d}.json` and
`activity.xml` into a local directory. Obtain the actual successful Pages
deployment commit's complete tree, then run:

```sh
python tools/publication_pipeline.py verify-live /tmp/reviewed-publication /tmp/served-site deployed-tree.json
```

This checks served canonical hashes, full data/RSS validity, unchanged authored
fields/audits, addition events in both windows/RSS, and initial GitHub/context
fields. Changes to AI usage/tools require explicit review. Run soon after
publication: rolling-feed expiry is not a failed historical publication. An
empty repository can legitimately have null last-commit context. Metadata and
successful Pages are necessary evidence, not proof of compilation or gameplay.

## Measured offline replay

Replayed the recorded 17-game batch against its original 1,715-project baseline,
without network writes or fake live additions. The original end-to-end audit
measured 31m29s: preparation 13m08s, review 4m21s, commit about 48s of tool runtime,
metadata roughly 10m03s, and Pages roughly 46s. Some phases overlapped and blob
transfer wall time was not fully measured, so these are not additive CPU times.

On the same local recorded data:

- Existing apply/validate dry run: 0.84s
- New complete preparation: 1.20s (baseline verification 0.11s, compilation/
  application/preservation 0.27s, serialization/validation/reporting 0.83s)
- Idempotent prepared-bundle recheck: 0.15s
- Offline served-data verification: 1.44s; all 1,732 typed records/audits and all
  17 addition contexts, activity windows and RSS events checked
- Eight changed files, 15,260,275 bytes with the generated compact index/report

The JSON merge was already cheap; it is not claimed as a speedup. The gain is
reusable scaffolding and single-authored research. Actual future authoring-time
savings and live network timing are unmeasured. The recorded old probe touched
1,154 repositories and made 1,405 requests; the same catalogue delta selects
only the 17 changed repositories. Actual new request counts depend on branches,
paths/history, quota and retries. No projected wall-clock estimate replaces a
future measured publication.
