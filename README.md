# Legacy Reverse Engineering Tracker

Structured tracking for reverse-engineering/source-reconstruction projects targeting **Amiga, Atari ST, ZX Spectrum, Commodore 64 and Amstrad CPC**.

## Interactive tracker

The repository now includes a framework-free static browser at [index.html](index.html). When served through GitHub Pages it provides:

- all projects in one table by default
- combined filtering by source platform, reconstructed language, type, status, compilability, playability, byte exactness and AI usage
- free-text search over titles, notes, tags, techniques and platforms
- sortable columns
- expandable project details
- explicit **Unknown** state rather than treating missing evidence as “No”

Canonical records remain YAML under `projects/`. `tools/generate_views.py` converts those records into `web/projects.json`; the browser is plain HTML/CSS/JavaScript with no rendering framework or runtime dependencies.

See [schema.md](schema.md), [sources.md](sources.md), [log.md](log.md), and the legacy [projects.md](projects.md) migration/backlog view.
