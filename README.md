# Legacy Reverse Engineering Tracker

A structured catalogue of reverse-engineering and source-reconstruction projects for **Amiga, Atari ST, ZX Spectrum, Commodore 64 and Amstrad CPC** software.

**Live tracker:** https://rmtew.github.io/legacy-reverse-engineering-tracker/

The tracker has two views:

- **Projects** — filterable catalogue of tracked reverse-engineering projects.
- **Activity** — day-by-day recent commit history across tracked projects, including active non-default branches.

## Repository structure

- `data/projects.json` — canonical structured project data
- `data/activity.json` — rolling 180-day attributed commit feed
- `index.html`, `web/tracker.js`, `web/tracker.css` — framework-free interactive UI
- `tools/refresh_github.py` — objective GitHub metadata and AI-evidence refresh
- `tools/enrich_evidence.py` — conservative README/status evidence enrichment for build/playability/byte-exact/start fields
- `tools/collect_activity.py` — recent multi-branch commit collection and project attribution
- `.github/workflows/refresh-github.yml` — daily metadata/activity refresh
- `.github/workflows/enrich-evidence.yml` — weekly evidence enrichment
- `.github/workflows/pages.yml` — GitHub Pages deployment
- `schema.md` — field definitions and evidence rules
- `sources.md` — discovery nodes, search strategy and open discovery priorities
- `log.md` — historical search/discovery notes

There is no rendering framework or build step. The browser reads the JSON data directly. A daily GitHub Action refreshes repository metadata and the rolling activity feed. A separate weekly enrichment pass scans project documentation for explicit evidence about build/playability/byte-exact/start fields and records CI signals when GitHub's API quota permits.

Unknown facts stay **unknown**. In particular, absence of evidence does not become “No” for AI use, byte exactness, buildability or dates.
