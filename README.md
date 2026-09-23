# Legacy Reverse Engineering Tracker

A structured catalogue of reverse-engineering and source-reconstruction projects for **Amiga, Atari ST, ZX Spectrum, Commodore 64 and Amstrad CPC** software.

**Live tracker:** https://rmtew.github.io/legacy-reverse-engineering-tracker/

The tracker has two views: **Projects** is the filterable catalogue; **Activity** is a day-by-day changelog of recent commits across tracked projects, including active non-default branches. Activity can be filtered by period, source platform, project, output language, branch, AI usage and free text.

## Repository structure

- `data/projects.json` — canonical structured project data\n- `data/activity.json` — rolling 180-day attributed commit feed
- `index.html`, `web/tracker.js`, `web/tracker.css` — framework-free interactive UI
- `tools/refresh_github.py` — objective GitHub metadata/AI-evidence refresh\n- `tools/collect_activity.py` — recent multi-branch commit collection and project attribution
- `.github/workflows/refresh-github.yml` — scheduled metadata refresh
- `.github/workflows/pages.yml` — GitHub Pages deployment
- `schema.md` — field definitions and evidence rules
- `sources.md` — discovery nodes used for graph-style searches
- `projects.md` — unresolved discovery backlog
- `log.md` — historical search/discovery notes

There is no rendering framework or build step. The browser reads the canonical JSON directly. A daily GitHub Action enriches GitHub-backed records with repository metadata and explicit AI-use signals, then rebuilds the rolling activity feed from recent commits on active branches.

Unknown facts stay **unknown**. In particular, absence of evidence does not become “No” for AI use, byte exactness, buildability or dates.
