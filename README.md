# Legacy Reverse Engineering Tracker

A structured catalogue of reverse-engineering, source-reconstruction and closely related native-port projects across legacy computers and consoles. The platform list is intentionally open-ended; current coverage includes Amiga, Atari ST, ZX Spectrum, Commodore 64, Amstrad CPC, BBC Micro/Master, Acorn Electron/Archimedes, NES, PMD 85 and others.

**Live tracker:** https://rmtew.github.io/legacy-reverse-engineering-tracker/  
**Activity RSS:** https://rmtew.github.io/legacy-reverse-engineering-tracker/activity.xml

The tracker has two views:

- **Projects** — filterable catalogue of tracked reverse-engineering projects.
- **Activity** — the default view: day-by-day recent commits and latest releases across tracked projects, including active non-default branches.

## Repository structure

- `data/projects.json` — canonical structured project data
- `data/activity.json` — rolling 180-day attributed commit feed
- `state/github-poll-state.json` — persistent per-repository polling and branch state
- `index.html`, `web/tracker.js`, `web/tracker.css` — framework-free interactive UI
- `tools/refresh_github.py` — adaptive conditional repository probes, metadata refresh and scan scheduling
- `tools/enrich_evidence.py` — conservative README/status evidence enrichment for build/playability/byte-exact/start fields
- `tools/collect_activity.py` — incremental multi-branch commit collection and project attribution
- `tools/generate_rss.py` — generates the public RSS feed from the activity/project JSON
- `tools/validate_site_data.py` — validates project/activity relationships and generated RSS
- `.github/workflows/refresh-github.yml` — daily metadata/activity refresh
- `.github/workflows/enrich-evidence.yml` — weekly evidence enrichment
- `.github/workflows/pages.yml` — GitHub Pages deployment
- `schema.md` — field definitions and evidence rules
- `sources.md` — discovery nodes, search strategy and open discovery priorities
- `log.md` — historical search/discovery notes

There is no rendering framework or build step. The browser reads the JSON data directly. A daily GitHub Action uses conditional repository probes and adaptive, staggered deep scans: recently active repositories are checked frequently, dormant ones less often, while any detected push queues an immediate scan. Activity collection is incremental, retaining 180 days locally instead of re-downloading that history. Conditional repository probes are allowed across the whole catalogue and primary throttling follows GitHub's actual `X-RateLimit-*` response headers rather than a fixed per-phase request budget. A small capped reserve is kept for deployment/other work, while a 4,000-request HTTP safety cap plus 0.10 s request pacing protects against runaway/secondary-limit behaviour without becoming the normal limiting factor. Unfinished deep scans remain queued. Repository probes are ordered oldest-first, and queued deep scans prioritize detected changes then least-recently scanned repositories, so budget limits cannot permanently starve later repositories. A separate weekly enrichment pass scans project documentation for explicit evidence about build/playability/byte-exact/start fields and records CI signals when GitHub's API quota permits.

Unknown facts stay **unknown**. In particular, absence of evidence does not become “No” for AI use, byte exactness, buildability or dates.


The site header shows the activity-data refresh time. The Activity view can filter commits versus releases. The RSS feed is deliberately lower-noise: commits are grouped into one item per project per UTC day, while releases remain separate items. Pages deployment validates the JSON relationships and generated RSS before publishing.


The maintenance workflow writes rate-limit diagnostics to its GitHub Actions step summary, including actual limit, remaining quota, reset time, HTTP request counts and conditional 304 counts.


Conditional ETags are treated as an optimization, not as assumed savings: if GitHub returns `304 Not Modified` they are recorded separately, but scheduling decisions still use the actual remaining quota reported by GitHub.
