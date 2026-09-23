# Project data schema

The canonical database is `data/projects.json`, a JSON array of project records. The static HTML tracker reads this file directly; there is no generated-data layer.

## Evidence rules

- Use `null` when a fact has not been verified. Missing evidence is not the same as `false`.
- `source_platforms` are the original platforms/binaries being analysed.
- `target_platforms` are platforms produced or supported by the reconstruction/reimplementation.
- `source_cpu` describes the original CPU architecture(s).
- `source_language` describes the material being reverse engineered, usually machine code.
- `reconstructed_languages` describes the human-maintained source/output produced by the project.
- `re_started` is when the reverse-engineering effort began; a year is acceptable when the exact date is unknown.
- `last_activity` is upstream activity; `last_checked` is when this tracker last verified the record.
- `build.byte_exact` means a produced original-platform binary is verified to match the original. A stated goal of byte matching is not enough.
- `ai.usage` is `true` only with explicit evidence, `false` only when non-use is established, otherwise `null`.
- Fuzzy descriptors belong in `tags`; filterable facts belong in typed fields.

## Record fields

`id`, `title`, `repo`, optional `project_url`, `source_platforms`, `target_platforms`, `source_cpu`, `source_language`, `reconstructed_languages`, `types`, `re_started`, `last_activity`, `last_checked`, `status`, `build`, `ai`, `techniques`, `tags`, `notes`.

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

The workflow also refreshes top-level `last_activity` from the latest default-branch commit.

Repository creation is **not** treated as the true reverse-engineering start date. The UI may show it with an asterisk as a fallback while `re_started` is unknown.

AI automation is evidence-only: explicit AI instruction files or AI co-author commit trailers can set `ai.usage=true` and record evidence. Absence of those signals never sets AI usage to false.


## Adaptive repository polling

Persistent generated state lives in `state/github-poll-state.json`. Every daily run conditionally probes each unique GitHub repository using its stored ETag. Unchanged repositories can return `304 Not Modified`; expensive branch/commit work is performed only when scheduled or when a push is detected.

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

The probe phase has a 250-request hard budget and activity collection a 450-request hard budget. Both stop before GitHub's reported primary quota falls below a 250-request reserve. Anything left unfinished remains queued rather than being recorded as successfully checked.

Activity collection is incremental. Poll state stores each observed branch tip SHA and last successful branch scan. Unchanged branch tips require no commit-history request. Changed tips fetch only commits since the previous scan, with a one-day overlap for safety; those commits are merged into the locally retained 180-day `data/activity.json` history.

For multi-project repositories the collector normally fetches new commits once and attributes them using the files touched by each commit. For larger bursts it switches to incremental path-filtered queries when that requires fewer API calls. Deleted upstream branches are pruned from poll-state branch metadata on the next deep scan; historical activity already collected from them remains in the rolling feed until it ages out.


## Shared GitHub repositories

Some repositories contain several independently tracked reverse-engineering projects.

- `repo` always points to the GitHub repository root when GitHub automation is desired.
- `project_url` may point to a project-specific directory/page and is preferred by the UI for the project-title link.
- `github_path` limits automated commit activity to a subdirectory, so one game's commits do not make every game in a monorepo appear active.
- `github_branch` overrides the default branch when the relevant reconstruction lives on another branch (for example, an original-game disassembly branch beside a modified version).


## Activity data

`data/activity.json` is a generated rolling commit feed, currently covering 180 days. It is not hand-edited.

Each event contains:

- `type` (currently `commit`)
- timestamp and commit SHA
- `project_id` linking back to `data/projects.json`
- repository
- commit title/full message and URL
- author
- every active branch on which the collector observed that commit

The collector checks non-default branches when a repository's deep scan is due. Stored branch-tip SHAs avoid re-querying unchanged branches. Commits reachable from several branches are deduplicated per project/SHA and retain all matching branch names.

For shared repositories, `github_path` is used to attribute commits to the relevant tracked subproject. Repository-wide/shared-tooling commits outside a project's configured path are intentionally not attributed to that project.

The Activity UI groups events by UTC calendar day and then project, while displaying the viewer's local event time. It augments stored commit activity with each project's latest known GitHub release and can filter by activity type (commit/release). Filters reuse project metadata, so platform/language/AI filters apply consistently between the catalogue and activity feed. The site header and Activity result bar expose `data/activity.json.generated_at` as the data-refresh time.


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

The RSS 2.0 feed contains up to the 200 most recent commit/release events. Commit items use a stable GUID composed from project ID and commit SHA; release items use project ID plus release tag. Items link directly to the upstream commit or release when available and include project/platform context plus branch, author and commit-message context where relevant.

The feed is derived entirely from already-collected tracker data, so generating it makes no additional GitHub API requests. The website advertises it through a standard RSS autodiscovery `<link>` element and a visible RSS icon in the site header.


## Site integrity validation

`tools/validate_site_data.py` checks that project IDs are unique, every stored activity event references a known project, commit activity keys are unique and newest-first, timestamps are parseable, and generated RSS is valid RSS 2.0 with unique GUIDs and required item fields. The metadata workflow validates JSON before committing generated refresh data, and the Pages workflow validates both JSON and RSS before deployment.
