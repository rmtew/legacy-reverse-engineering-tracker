# Legacy Reverse Engineering Tracker

A structured catalogue of reverse-engineering and source-reconstruction projects for **Amiga, Atari ST, ZX Spectrum, Commodore 64 and Amstrad CPC** software.

**Live tracker:** https://rmtew.github.io/legacy-reverse-engineering-tracker/

The tracker shows all projects by default, with sortable columns, full-text search, and combinable filters for source/target platform, CPU, output language, reverse-engineering type, tags, status, GitHub activity, compilability, playability, byte exactness and AI usage.

## Repository structure

- `data/projects.json` — canonical structured project data
- `index.html`, `web/tracker.js`, `web/tracker.css` — framework-free interactive UI
- `tools/refresh_github.py` — objective GitHub metadata/AI-evidence refresh
- `.github/workflows/refresh-github.yml` — scheduled metadata refresh
- `.github/workflows/pages.yml` — GitHub Pages deployment
- `schema.md` — field definitions and evidence rules
- `sources.md` — discovery nodes used for graph-style searches
- `projects.md` — unresolved discovery backlog
- `log.md` — historical search/discovery notes

There is no rendering framework or build step. The browser reads the canonical JSON directly. A daily GitHub Action enriches GitHub-backed records with repository creation/activity dates, latest commit/release information, language metadata, archive state and explicit AI-use signals.

Unknown facts stay **unknown**. In particular, absence of evidence does not become “No” for AI use, byte exactness, buildability or dates.
