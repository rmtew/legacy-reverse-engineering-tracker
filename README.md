# Retro Development Project Tracker

A structured catalogue of retro-development projects across legacy computers and consoles: reverse engineering, source reconstruction, preservation, homebrew, native ports and directly relevant tooling. The platform list is intentionally open-ended; current coverage includes Amiga, Atari ST, ZX Spectrum, Commodore 64, Amstrad CPC, BBC Micro/Master, Acorn Electron/Archimedes, NES, PMD 85 and others.

**Live tracker:** https://rmtew.github.io/legacy-reverse-engineering-tracker/  
**Activity RSS:** https://rmtew.github.io/legacy-reverse-engineering-tracker/activity.xml

The tracker has two views:

- **Projects** — filterable catalogue using additive facet chips for **Project type / Platform / CPU / Software type / Work / Development tool**, plus compact single-choice controls for AI/build/playability state. The internal subject/tooling/hybrid enum is presented as the clearer **Retro software / Development tools** distinction; hybrid records simply belong to both.
- **Activity** — the default view: day-by-day recent commits, releases and catalogue changes, with the same topical additive facets including CPU family. Branch, author, project and output-language dropdowns are intentionally omitted.

## Repository structure

- `data/projects.json` — canonical structured project data
- `data/activity.json` — rolling 180-day activity; individual commits for 14 days, then compact project/day summaries retaining SHAs for safe incremental collection
- `data/discovery-sources.json` — persistent discovery-node index and explicit research backlog
- `data/discovery-decisions.json` — searchable reviewed candidate decisions, including exclusions and duplicates
- `data/project-audits.json` — field-by-field research coverage for every tracked project
- `data/research-activity.json` — append-only history of discovery/audit work and when it was performed
- `tools/apply_discovery_batch.py` — preview and apply one validated cross-file research batch
- `state/github-poll-state.json` — persistent per-repository polling and branch state
- `index.html`, `web/tracker.js`, `web/tracker.css` — framework-free interactive UI
- `tools/refresh_github.py` — adaptive conditional repository probes, metadata refresh and scan scheduling
- `tools/enrich_evidence.py` — conservative README/status evidence enrichment for build/playability/byte-exact/start fields
- `tools/collect_activity.py` — incremental multi-branch commit collection and project attribution
- `tools/generate_rss.py` — generates the public RSS feed from the activity/project JSON
- `tools/validate_site_data.py` — validates project/activity relationships and generated RSS
- `.github/workflows/refresh-github.yml` — adaptive metadata/activity refresh in fifteen-minute slots
- `.github/workflows/enrich-evidence.yml` — weekly evidence enrichment
- `.github/workflows/pages.yml` — GitHub Pages deployment
- `schema.md` — field definitions and evidence rules
- `sources.md` — human-readable discovery map and search strategy; canonical queue/state lives in `data/discovery-sources.json`
- `log.md` — historical search/discovery notes

There is no rendering framework or build step. The browser reads the JSON data directly. A GitHub Action runs in fifteen-minute slots: projects with commits in the last 14 days are probed every slot, those last active 15–60 days hourly, 61–180 days every four hours, and older or archived projects every twelve hours. Deep activity scans retain their separate adaptive daily to 56-day cadence; any detected push queues an immediate scan. Activity collection is incremental, retaining 180 days locally instead of re-downloading that history. ETags can save primary quota when GitHub actually returns 304, but the probe loop respects the live `X-RateLimit-*` headers and a capped reserve even when ETags miss. A 4,000-request HTTP safety cap plus 0.10 s request pacing protects against runaway or secondary-limit behaviour. Unfinished deep scans remain queued. Repository probes are ordered oldest-first, and queued deep scans prioritize detected changes then least-recently scanned repositories. Empty language metadata is retried after 30 days or a push; release metadata is checked at least every six hours for active projects and daily for others. Only material changes to public data trigger a Pages deployment. A separate weekly enrichment pass scans project documentation for explicit evidence about build/playability/byte-exact/start fields and records CI signals when GitHub's API quota permits. The [polling capacity study](docs/github-polling-capacity-2026-09-26.md) documents the measurements behind this schedule.

Project identity is separated from catalogue presentation: `upstream_name` preserves the project's own name, `display_title` gives the UI a concise human-readable subject/purpose label, and `subjects` records the actual legacy software names so opaque project brands remain searchable. For example, Firestaff is displayed as a Dungeon Master / Chaos Strikes Back engine reconstruction while retaining `Firestaff` as its upstream name.

CPU discovery and runtime compatibility are deliberately separate. The visible **CPU** facet groups exact source/target CPUs into useful families (for example **68000 family**), while optional verified `runtime_profiles` power the separate **Runs on** filter for minimum CPU, RAM and chipset. This avoids presenting a 68020-only build as 68000-compatible merely because both are m68k.

Project classification is deliberately multi-axis rather than a flat tag pile: `record_class` distinguishes subject/tooling/hybrid records, `target_kinds` says what legacy software is being studied, `work_kinds` says what kind of reconstruction/analysis is being done, and `tool_kinds` says what a modern aid actually does. Existing `types` and free-form `tags` remain available for nuance and search.

Unknown facts stay **unknown**. In particular, absence of evidence does not become “No” for AI use, byte exactness, buildability or dates.

## Discovery passes

Prepare one JSON batch containing a date, unique research-event ID, summary and the reviewed additions/updates. Use `python tools/apply_discovery_batch.py batch.json` to preview; add `--write` only after reviewing the summary. The tool links projects to source nodes, creates an unreviewed audit when an explicit audit is not supplied, inserts a newest-first research event and validates the complete proposed tracker before writing any file. It rejects duplicate IDs and repeated project URLs unless a shared URL is explicitly acknowledged. Batch format and a runnable example are in [the discovery workflow guide](docs/discovery-workflow.md).

Commit all changed data files together after `python tools/validate_site_data.py data/projects.json data/activity.json` and `git diff --check`. Publish one commit against the current `main` ref. Catalogue changes trigger a metadata refresh and then Pages; research-index-only changes deploy directly through Pages. Check the relevant runs before finishing. In Codex Work, use the linked GitHub connector for the atomic tree/commit/ref update; the workspace shell may not have authenticated Git credentials. The existing `automation/discovery-*` workflow can also validate, fast-forward and remove a temporary discovery branch. Do not publish intermediate project/audit/source changes separately.


The site header shows the activity-data refresh time. With no saved preference, the site follows the browser/operating-system light/dark preference. Manually using the Light/Dark toggle creates a local override stored in `localStorage` under `retro-development-tracker.theme`; merely following the browser default does not write anything. No other UI settings are persisted yet. The Activity view loads slim 30-day and 180-day browser feeds, showing individual recent commits and older daily summaries. Project additions show a frozen latest commit/release and 90-day activity count after their first completed repository scan. RSS publishes completed UTC-day commit digests, releases and meaningful catalogue changes; pre-tracking backfills and pre-rollout catalogue additions do not become new feed items. Pages deployment validates the JSON relationships and generated RSS before publishing.


The maintenance workflow writes rate-limit diagnostics to its GitHub Actions step summary, including actual limit, remaining quota, reset time, HTTP request counts and conditional 304 counts.


Conditional ETags are treated as an optimization, not as assumed savings: if GitHub returns `304 Not Modified` they are recorded separately, but scheduling decisions still use the actual remaining quota reported by GitHub.


The workflow schedules both NZST and NZDT UTC equivalents and selects the correct pair from the current `Pacific/Auckland` offset, so the 6:30 AM/PM refresh times remain stable across daylight-saving changes.
