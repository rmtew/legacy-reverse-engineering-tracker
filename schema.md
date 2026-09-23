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

The collector checks non-default branches that have commits inside the activity window. Commits reachable from several branches are deduplicated per project/SHA and retain all matching branch names.

For shared repositories, `github_path` is used to attribute commits to the relevant tracked subproject. Repository-wide/shared-tooling commits outside a project's configured path are intentionally not attributed to that project.

The Activity UI groups commits by UTC calendar day and then project, while displaying the viewer's local commit time. Filters reuse project metadata, so platform/language/AI filters apply consistently between the catalogue and activity feed.


## Evidence enrichment

`tools/enrich_evidence.py` performs a conservative daily pass over GitHub-backed project documentation.

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
- Monorepo projects scan their configured `github_path` only, so one project's README cannot supply evidence for another.
- Repository creation dates remain separate GitHub metadata and are not promoted to `re_started`.

The automated evidence block currently contains `compilable`, `playable`, `byte_exact`, `re_started`, and `ci` arrays plus collector/check metadata.
