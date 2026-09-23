# Project record schema

Canonical project records live under `projects/<platform>/*.yml`. The browser never reads YAML directly; `tools/build_data.py` validates the records and generates `web/projects.json`.

## Rules

- Use `unknown` when a fact has not been verified. Missing evidence is not the same as `no`.
- `source_platforms` are the original platforms/binaries being analysed.
- `target_platforms` are platforms produced or supported by the reconstruction/reimplementation.
- `source_cpu` describes the original machine-code CPU(s).
- `source_language` describes the material being reverse engineered, usually machine code.
- `reconstructed_languages` describes the human-maintained output/source produced by the project.
- `re_started` is when the reverse-engineering effort began. A year is acceptable when the exact date is unknown.
- `last_activity` is upstream project activity; `last_checked` is when this tracker last verified it.
- `build.byte_exact` means the generated original-platform binary matches the original. Behavioural equivalence alone is not byte exact.
- `ai.usage` is `yes` only with explicit evidence. Otherwise use `unknown`.
- Keep fuzzy descriptors in `tags`; keep filterable facts in typed fields.

## Core fields

`id`, `title`, `repo`, `source_platforms`, `target_platforms`, `source_cpu`, `source_language`, `reconstructed_languages`, `types`, `re_started`, `last_activity`, `last_checked`, `status`, `build`, `ai`, `techniques`, `tags`, `notes`.

## Build fields

`compilable`, `runnable`, `playable`, `byte_exact` each use `yes`, `no`, or `unknown`.

## AI fields

`usage` uses `yes`, `no`, or `unknown`; `tools` lists explicitly evidenced tools only.
