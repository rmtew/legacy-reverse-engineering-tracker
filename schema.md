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

`id`, `title`, `repo`, `source_platforms`, `target_platforms`, `source_cpu`, `source_language`, `reconstructed_languages`, `types`, `re_started`, `last_activity`, `last_checked`, `status`, `build`, `ai`, `techniques`, `tags`, `notes`.

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
