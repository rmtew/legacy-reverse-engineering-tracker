# Project record schema

Each project is stored as a small YAML record under `projects/<platform>/`.

Important rules:

- Use `unknown` when evidence is absent. Do not convert absence of evidence into `no`.
- `source_platforms` means the original binary/software being analysed.
- `target_platforms` means platforms produced by the reconstruction/reimplementation.
- `last_activity` describes upstream project activity; `last_checked` describes our observation date.
- `byte_exact` describes whether the generated original-platform binary matches the original, not whether behaviour merely appears equivalent.
- AI usage is only `yes` when explicitly evidenced; otherwise use `unknown`.

Core fields: id, title, repo, source_platforms, target_platforms, source_cpu, source_language, reconstructed_languages, types, re_started, last_activity, last_checked, status, build, ai, techniques, tags, notes.
