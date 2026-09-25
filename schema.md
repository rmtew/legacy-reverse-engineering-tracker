# Project data schema

The canonical database is `data/projects.json`, a JSON array of project records. The static HTML tracker reads this file directly; there is no generated-data layer.

## Evidence rules

- Use `null` when a fact has not been verified. Missing evidence is not the same as `false`.
- `upstream_name` is the project's own or best-known upstream name. It preserves identity even when that name is opaque in a catalogue.
- `display_title` is a tracker-curated explanatory label used prominently by the UI. When the upstream name is opaque, identify the legacy subject/platform plus the project's primary purpose (for example, `Firestaff — Dungeon Master / Chaos Strikes Back engine reconstruction`). Do not turn it into a list of every capability.
- `subjects` names the actual legacy software subjects being studied or reconstructed. It is searchable and may contain several titles for a multi-game engine/project. Pure generic tooling can leave it empty; subject/hybrid records must name at least one subject.
- `source_platforms` are the original platforms/binaries being analysed.
- `target_platforms` are platforms produced or supported by the reconstruction/reimplementation.
- `source_cpu` describes the original CPU architecture(s). The UI groups related variants into broad discovery families such as **6502 family** and **68000 family** without discarding the exact stored CPU.
- `target_cpu` optionally records CPU architecture(s) produced or directly targeted by a port/reimplementation. Do not infer this merely from a host language or modern build environment.
- `runtime_profiles` optionally records verified minimum hardware requirements for runnable outputs/build variants. A profile may contain `name`, required `platform`, optional `cpu_family`, `min_cpu`, `min_ram_kib`, `min_chip_ram_kib`, `min_fast_ram_kib`, `chipsets`, `os`, `notes`, and source `evidence`. Only populate these from explicit primary evidence; never infer a runnable minimum from source CPU or platform alone.
- `source_language` describes the material being reverse engineered, usually machine code.
- `reconstructed_languages` describes the human-maintained source/output produced by the project.
- `record_class` separates reverse-engineered/reimplemented **subjects** from modern supporting **tooling**; `hybrid` is reserved for projects that are materially both (for example a reconstructed historical tool that is also actively useful for archaeology).
- `target_kinds` describes what kind of legacy subject is being reconstructed or analysed, independently of platform: game, application, demo, operating system/ROM, development tool, engine/subsystem, etc. Pure tooling records normally leave this empty.
- `work_kinds` describes the reverse-engineering/reconstruction method: disassembly, decompilation, source reconstruction, binary/data analysis, reimplementation, RE-derived port, and so on.
- `tool_kinds` describes concrete capabilities of tooling/hybrid records: emulator, debugger, profiler, disassembler, IDE, toolchain, static analysis, ROM/filesystem tooling, etc.
- `types` is retained as a legacy/free-form descriptor field for project-specific nuance; the UI's primary classification and filters use the structured fields above.
- `re_started` is when the reverse-engineering effort began; a year is acceptable when the exact date is unknown.
- `last_activity` is upstream activity; `last_checked` is when this tracker last verified the record.
- `build.byte_exact` means a produced original-platform binary is verified to match the original. A stated goal of byte matching is not enough.
- `ai.usage` is `true` only with explicit evidence, `false` only when non-use is established, otherwise `null`.
- Fuzzy descriptors belong in `tags`; filterable facts belong in typed fields.

## Record fields

`id`, legacy `title`, `upstream_name`, `display_title`, `subjects`, `repo`, optional `project_url`, `source_platforms`, `target_platforms`, `source_cpu`, optional `target_cpu`, optional `runtime_profiles`, `source_language`, `reconstructed_languages`, `record_class`, `target_kinds`, `work_kinds`, `tool_kinds`, `types`, `re_started`, `last_activity`, `last_checked`, `status`, `build`, `ai`, `techniques`, `tags`, `notes`.

### Structured classification vocabulary

`record_class` is one of:

- `subject` — the record primarily represents legacy software being reverse engineered, reconstructed, restored or reimplemented.
- `tooling` — the record primarily represents modern infrastructure useful to software archaeology or reproducible retro development.
- `hybrid` — materially both a reverse-engineered subject and a useful tool.

`target_kinds` uses: `game`, `application`, `demo`, `operating-system`, `firmware-rom`, `system-software`, `game-engine`, `game-subsystem`, `development-tool`.

`work_kinds` uses: `disassembly`, `decompilation`, `source-reconstruction`, `source-restoration`, `binary-analysis`, `data-format-analysis`, `copy-protection-analysis`, `reimplementation`, `reverse-engineering-derived-port`, `patching`, `translation`, `subsystem-reconstruction`.

`tool_kinds` uses: `emulator`, `debugger`, `profiler`, `graphics-debugger`, `binary-analysis`, `disassembler`, `reassembler`, `ide`, `compiler-toolchain`, `assembler-toolchain`, `static-analysis`, `language-tooling`, `cycle-analysis`, `rom-tool`, `disk-filesystem-tool`, `asset-tool`, `automation`, `development-environment`.

The UI's **CPU** facet is a broad discovery facet: source, target and verified-runtime CPUs are grouped into architecture families. **Runs on** is deliberately separate and only uses verified `runtime_profiles`. A selected CPU or RAM amount there means a documented output must fit that hardware; for example, a 68020 choice may include a 68000-minimum build, while a 68000 choice must exclude a 68020-minimum build.

The UI renders structured classification independently of the display title. `display_title` answers “what is this project?” at a glance; classification answers “what kind of record/work/tool is it?”; `subjects` makes opaque project names searchable by the actual software being studied.

`build` contains `compilable`, `runnable`, `playable`, and `byte_exact`, each represented by `true`, `false`, or `null`.

`ai` contains `usage` (`true`, `false`, or `null`) and a `tools` array containing only explicitly evidenced tools.


## Automated GitHub metadata

For records whose `repo` is a GitHub repository, the daily workflow refreshes a `github` object containing objective repository data:

- `repository`
- `created_at`, `pushed_at`, `updated_at`, `checked_at`
- `default_branch`, `archived`, `fork`
- `primary_language` and the ordered `languages` list
- `activity_state` derived from latest commit age
- `latest_commit`
- `latest_release` when present

The workflow also refreshes top-level `last_activity` from the latest commit on the tracked branch/path. Its 180-day activity scan may find no recent commits for an older repository, so a separate one-result historical lookup supplies the actual latest date without inserting that old commit into the activity timeline. Empty branch/path results are cached for 30 days (or until the repository's pushed timestamp changes); the UI then says no commit was found rather than inventing a date.

Repository creation is **not** treated as the true reverse-engineering start date. The UI may show it with an asterisk as a fallback while `re_started` is unknown.

AI automation is evidence-only: explicit AI instruction files or AI co-author commit trailers can set `ai.usage=true` and record evidence. Absence of those signals never sets AI usage to false.


## Adaptive repository polling

Persistent generated state lives in `state/github-poll-state.json`. Scheduled refreshes run at about 06:30 and 18:30 `Pacific/Auckland`, immediately before the 07:00 and 19:00 maintenance passes. Each refresh conditionally probes every unique GitHub repository using its stored ETag. Unchanged repositories can return `304 Not Modified`; expensive branch/commit work is performed only when scheduled or when a push is detected.

The workflow keeps those local refresh times DST-stable by scheduling both NZST and NZDT UTC equivalents and allowing only the pair matching the current Auckland UTC offset to proceed.

Deep-scan cadence is based on the most recent tracked activity in the repository:

| Activity age | Deep-scan cadence |
|---|---:|
| 0–14 days | daily |
| 15–60 days | every 3 days |
| 61–180 days | every 7 days |
| 181–730 days | every 14 days |
| over 730 days | every 30 days |
| archived repository | every 56 days |

Longer cadences are deterministically staggered by repository name so weekly/monthly work is spread across days. A changed `pushed_at` value overrides the cadence and queues an immediate deep scan. Newly tracked repositories are queued immediately after the initial state bootstrap. Probe execution itself is oldest-first using `last_probe_at`, so if the request budget cuts a run short, skipped repositories automatically move to the front on the next run. Deep-scan execution similarly prioritizes detected changes/new repositories, then the least-recently deep-scanned queued repositories.

Primary-rate throttling is based on GitHub's response headers (`X-RateLimit-Limit`, `X-RateLimit-Remaining`, and `X-RateLimit-Reset`) rather than fixed probe/activity quotas. Conditional ETag probes are allowed to continue even when the remaining primary quota is near the reserve because a valid authenticated `304 Not Modified` response does not consume primary quota. ETag savings are opportunistic: the workflow records the actual `304` count but does not assume GitHub will return one.

For requests that do consume primary quota, the reserve is calculated from the reported limit: 15% of the limit, with a normal floor of 100 and a cap of 250 requests. Thus a 1,000-request allowance reserves 150, while the currently observed 5,000-request allowance reserves 250 rather than 750. Low-limit/unauthenticated cases scale the floor down instead of reserving more than a practical fraction of the limit.

Both phases have a separate 4,000-HTTP-request safety cap and a 0.10 s request delay. At most about 600 sequential requests/minute can therefore be attempted by a phase, keeping the cap from becoming the normal bottleneck while still providing runaway/secondary-limit protection. Primary quota remains the real limiter. Anything left unfinished remains queued rather than being recorded as successfully checked. The workflow records the observed limit, remaining quota, reset timestamp, HTTP request count and conditional-304 count in generated poll state and the Actions step summary.

Activity collection is incremental. A newly tracked repository is first backfilled across the retained 180-day activity window; adding a new tracked project to an already-known repository also queues a one-time repository backfill so recent pre-existing commits are not missed. Poll state stores the tracked project IDs, each observed branch tip SHA and last successful branch scan. After the initial/backfill scan, unchanged branch tips require no commit-history request. Changed tips fetch only commits since the previous scan, with a one-day overlap for safety; those commits are merged into the locally retained 180-day `data/activity.json` history.

For multi-project repositories the collector normally fetches new commits once and attributes them using the files touched by each commit. For larger bursts it switches to incremental path-filtered queries when that requires fewer API calls. Deleted upstream branches are pruned from poll-state branch metadata on the next deep scan; historical activity already collected from them remains in the rolling feed until it ages out.


## Shared GitHub repositories

Some repositories contain several independently tracked reverse-engineering projects.

- `repo` always points to the GitHub repository root when GitHub automation is desired.
- `project_url` may point to a project-specific directory/page and is preferred by the UI for the project-title link.
- `github_path` limits automated commit activity to a subdirectory, so one game's commits do not make every game in a monorepo appear active.
- `github_branch` overrides the default branch when the relevant reconstruction lives on another branch (for example, an original-game disassembly branch beside a modified version).



## Research-state indexes

Research coverage is persistent state rather than being inferred from null project fields.

### `data/discovery-sources.json`

This is the canonical discovery-node/work-queue index. Each source has a stable `id`, human/source URL, source `kind`, rationale, `review_state`, indexing/review dates, promoted project IDs and linked open tasks.

Source review states are:

- `unreviewed` — known lead, not yet investigated.
- `partial` — investigated enough to yield context/projects, but meaningful graph work remains.
- `substantially-reviewed` — the current source graph has been worked through; revisit mainly for changes/new links.
- `exhausted` — reviewed and no remaining useful leads are currently known.

The top-level `backlog` is the explicit source-research queue. Task states are `open`, `in-progress`, `done`, or `deferred`. A deferred task is retained so a consciously excluded lead is not repeatedly rediscovered.

### `data/discovery-decisions.json`

This is an index of specific reviewed candidate URLs, especially leads deliberately not promoted. Each decision has a stable `id`, descriptive `title`, canonical `url`, `decision` (`excluded`, `duplicate`, `deferred`, or `promoted`), concise `reason`, one or more primary `evidence_urls`, linked `source_ids`, optional `project_ids`, and `reviewed_at`. `promoted` decisions require a project reference; an excluded conversion can point to a tracked predecessor when appropriate. URLs and IDs must be unique within this index. A decision records what was reviewed; it does not assert that every other work on the subject is excluded.

The batch helper can add these records alongside projects and research history. See [discovery workflow](docs/discovery-workflow.md).

### `data/project-audits.json`

There must be exactly one audit record for every `data/projects.json` project ID. It tracks research coverage independently from the factual project record.

Audit areas are `identity`, `classification`, `source_cpu`, `target_cpu`, `build`, `runtime_profiles`, `ai`, and `relationships`.

Area states are:

- `unreviewed` — no meaningful check has yet been made.
- `needs-research` — the project has been reviewed generally, but this area still needs primary-source work.
- `reviewed` — the area has been checked and the catalogue reflects the established result.
- `not-applicable` — the field does not sensibly apply to this project.
- `no-evidence-found` — a check was performed but found no positive evidence; this never means the underlying fact is false.

This distinction is important: an absent `target_cpu` or `runtime_profiles` value no longer implies either “not researched” or “no evidence exists”. The audit index records which case applies.

### `data/research-activity.json`

Append-only research history. Events record when discovery/audit work occurred and may reference source IDs or project IDs. The initial migration seeds this history from research-oriented `log.md` sections; subsequent research passes should append a concise event as they update source/task/audit state.

`sources.md` and `log.md` remain useful human-readable context, but these JSON files are the canonical current research queue and coverage state.


## Activity data

`data/activity.json` is a generated rolling activity feed covering 180 days. It is not hand-edited. The first 14 days retain individual commits. Older commits are compacted into `daily_commits` events per project, repository and Pacific/Auckland calendar day. Each summary retains sorted SHA identities for deduplication during later scans, plus the newest commit date/title/link. The Pages build creates slim 30- and 180-day browser feeds without full commit messages or summary SHA arrays. RSS uses the canonical file.

Stored commit events contain:

- `type: "commit"`
- timestamp and commit SHA
- `project_id` linking back to `data/projects.json`
- repository
- commit title/full message and URL
- author
- every active branch on which the collector observed that commit

The collector checks non-default branches when a repository's deep scan is due. Stored branch-tip SHAs avoid re-querying unchanged branches. Commits reachable from several branches are deduplicated per project/SHA and retain all matching branch names.

For shared repositories, `github_path` is used to attribute commits to the relevant tracked subproject. Repository-wide/shared-tooling commits outside a project's configured path are intentionally not attributed to that project.

The feed also persists meaningful catalogue-change events:

- `project_added`
- `project_removed`
- `project_restored`
- `project_renamed`
- `project_moved`
- `project_updated`

`state/project-catalog-state.json` stores the previous material catalogue snapshot used to detect those changes. The initial state is a baseline only, so existing projects do not receive fabricated historical addition events. Volatile fields such as `last_checked`, `last_activity`, generated GitHub metadata and automated evidence excerpts are excluded from the comparison. Material facts such as upstream/display names, subjects, platforms, languages, structured classification, legacy type descriptors, status, build flags, AI usage/tools, tags, techniques, notes and project location are compared.

Project-change events carry a compact `project` snapshot. Metadata-change events also carry structured `change_details` entries containing the field plus its before/after values; the Activity UI turns these into field-aware descriptions such as `AI usage detected · Claude`, `Target platform added · Windows`, or `Byte-exact build confirmed` rather than exposing JSON diffs. Older events that predate `change_details` are humanised from their retained legacy transition text when possible. The project snapshot lets removal events remain displayable and filterable after the canonical project record has been deleted. Removed snapshots are retained as tombstones in catalogue state so a later reappearance can be emitted as `project_restored`. Addition/restoration events gain frozen `activity_context` (last known commit, last activity, latest release, 90-day commit and active-day counts) once a completed deep scan has covered the project. Previously missing historical commit dates may subsequently be filled without changing the original 90-day counts; until a scan completes the page reports a pending scan.

The Activity UI groups events by the viewer's local calendar day and then project, and displays each event in the viewer's local time. It augments stored activity with each current project's latest known GitHub release and can filter by activity type (commit/daily summary, release, project changes). Filters use either the current project record or the event's persisted project snapshot, so removed projects remain usable in the feed. The site header and Activity result bar expose `data/activity.json.generated_at` as the data-refresh time.


## Evidence enrichment

`tools/enrich_evidence.py` performs a conservative weekly pass over GitHub-backed project documentation.

It scans project-local README/status/build notes for explicit claims about:

- compilability
- playability
- byte exactness
- project/reverse-engineering start year

The collector writes reviewable provenance under:

`evidence.automated`

Each evidence item records the inferred value, source file/link, a short source excerpt, check date, collector ID and strength.

Rules:

- Unknown fields are promoted only when all **strong** evidence found for that field agrees.
- Existing non-null curated values are never overwritten automatically.
- Playable=true may imply runnable=true when runnable is still unknown.
- Statements framed as goals/targets/plans are not accepted as proof of byte exactness.
- Generic CI success is recorded as a supporting signal only; it does not by itself prove the reconstruction compiles or plays.
- Documentation is fetched from raw GitHub content so evidence collection does not compete heavily with metadata/activity collection for the GitHub API quota. CI signals are best-effort and may be absent when the API quota is exhausted.
- Monorepo projects scan their configured `github_path` only, so one project's README cannot supply evidence for another.
- Repository creation dates remain separate GitHub metadata and are not promoted to `re_started`.

The automated evidence block contains only records with actual evidence/signals. It may contain `compilable`, `playable`, `byte_exact`, `re_started`, and `ci` arrays plus collector/check metadata. When automation promotes a previously unknown field it records that change in `evidence.automated.applied`; on later runs it may retract only its own prior promotion if the supporting evidence no longer qualifies. Curated non-null values are not automatically replaced.


## RSS feed

GitHub Pages generates `activity.xml` from `data/activity.json` and `data/projects.json` at deployment time using `tools/generate_rss.py`.

The RSS 2.0 feed contains up to 200 items. Commit activity is published after its UTC calendar day closes, one item per project/day listing its commits with links, authors, hashes and branches. Pre-tracking historical backfills are excluded from RSS but remain visible on the site. Daily GUIDs remain project ID plus UTC date, preserving existing subscriptions. Releases remain separate items linking upstream. Catalogue additions, restorations, removals, moves, renames and material metadata changes after `CATALOG_FEED_START` are separate items; that cutoff prevents the initial deployment from notifying subscribers of hundreds of earlier additions. Addition descriptions include frozen upstream dates and 90-day activity after a completed scan, or indicate a pending scan.

The feed is derived entirely from already-collected tracker data, so generating it makes no additional GitHub API requests. The website advertises it through a standard RSS autodiscovery `<link>` element and a visible RSS icon in the site header.


## Site integrity validation

`tools/validate_site_data.py` checks that project IDs are unique, every stored activity event references a known project, commit activity keys are unique and newest-first, timestamps are parseable, and generated RSS is valid RSS 2.0 with unique GUIDs and required item fields. The metadata workflow validates JSON before committing generated refresh data, and the Pages workflow validates both JSON and RSS before deployment.
