# Legacy Reverse Engineering Tracker

A structured catalogue of reverse-engineering and source-reconstruction projects for **Amiga, Atari ST, ZX Spectrum, Commodore 64 and Amstrad CPC** software.

The primary interface is the static [interactive tracker](index.html): one table, all projects by default, sortable columns, full-text search, and combinable filters for platforms, CPU, output language, reverse-engineering type, tags, status, compilability, playability, byte exactness and AI usage.

## Repository structure

- `projects/**/*.yml` — canonical project records
- `web/projects.json` — generated browser data
- `index.html`, `web/tracker.js`, `web/tracker.css` — framework-free UI
- `tools/build_data.py` — dependency-free YAML-subset → JSON builder
- `schema.md` — field definitions and evidence rules
- `sources.md` — people, collections and repositories used for graph-style discovery
- `log.md` — dated discovery/search notes
- `projects.md` — legacy discovery backlog retained until migration is complete

A GitHub Action rebuilds `web/projects.json` whenever canonical YAML records change.

Unknown facts stay **unknown**. In particular, absence of evidence does not become “No” for AI use, byte exactness, buildability or dates.
