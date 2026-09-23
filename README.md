# Legacy Reverse Engineering Tracker

A structured catalogue of reverse-engineering and source-reconstruction projects for **Amiga, Atari ST, ZX Spectrum, Commodore 64 and Amstrad CPC** software.

The primary interface is the static [interactive tracker](index.html): one table, all projects by default, sortable columns, full-text search, and combinable filters for source/target platform, CPU, output language, reverse-engineering type, tags, status, compilability, playability, byte exactness and AI usage.

## Repository structure

- `data/projects.json` — canonical structured project data
- `index.html`, `web/tracker.js`, `web/tracker.css` — framework-free interactive UI
- `schema.md` — field definitions and evidence rules
- `sources.md` — people, collections and repositories used for graph-style discovery
- `log.md` — dated discovery/search notes
- `projects.md` — legacy discovery backlog retained until all leads are migrated

There is no rendering framework or build step. The browser reads the canonical JSON directly. A daily GitHub Action enriches GitHub-backed records with repository creation/activity dates, latest commit/release information, language metadata, archive state and explicit AI-use signals.

Unknown facts stay **unknown**. In particular, absence of evidence does not become “No” for AI use, byte exactness, buildability or dates.
