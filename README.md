# Retro Development Project Tracker

A structured catalogue of retro-development projects across legacy computers and consoles: reverse engineering, source reconstruction, preservation, homebrew, native ports and directly relevant tooling. The platform list is intentionally open-ended; current coverage includes Amiga, Atari ST, ZX Spectrum, Commodore 64, Amstrad CPC, BBC Micro/Master, Acorn Electron/Archimedes, NES, PMD 85 and others.

**Live tracker:** https://rmtew.github.io/legacy-reverse-engineering-tracker/  
**Activity RSS:** https://rmtew.github.io/legacy-reverse-engineering-tracker/activity.xml

The tracker has two views:

- **Projects** — filterable catalogue using additive facet chips for **Project type / Platform / CPU / Software type / Work / Development tool**, plus compact single-choice controls for AI/build/playability state. The internal subject/tooling/hybrid enum is presented as the clearer **Retro software / Development tools** distinction; hybrid records simply belong to both.
- **Activity** — the default view: day-by-day recent commits, releases and catalogue changes, with the same topical additive facets including CPU family. Branch, author, project and output-language dropdowns are intentionally omitted.

## Repository structure

- `data/projects.index.json` + `data/projects/*.json` — canonical structured project data
- `data/activity.json` — rolling 180-day activity; individual commits for 14 days, then compact project/day summaries retaining SHAs for safe incremental collection
- `data/discovery-sources.json` — persistent discovery-node index and explicit research backlog
- `data/discovery-decisions.json` — searchable reviewed candidate decisions, including exclusions and duplicates
- `data/project-audits.index.json` + `data/project-audits/*.json` — field-by-field research coverage for every tracked project
- `data/research-activity.json` — append-only history of discovery/audit work and when it was performed
- `tools/apply_discovery_batch.py` — preview and apply one validated cross-file research batch
- `tools/screen_discovery_candidates.py` — local, read-only early URL screening for discovery results
- `tools/discovery_intake.py` — bounded searches, source mining, URL screening and ranked review queue
- `config/discovery-intake.json` — rotating GitHub search recipes and per-run collection limits
- `state/discovery-intake.json` — persistent candidate queue, provenance, source check dates and run statistics
- `state/github-poll-state.json` — persistent per-repository polling and branch state
- `index.html`, `web/tracker.js`, `web/tracker.css` — framework-free interactive UI
- `tools/refresh_github.py` — adaptive conditional repository probes, metadata refresh and scan scheduling
- `tools/enrich_evidence.py` — conservative README/status evidence enrichment for build/playability/byte-exact/start fields
- `tools/collect_activity.py` — incremental multi-branch commit collection and project attribution
- `tools/generate_rss.py` — generates the public RSS feed from the activity/project JSON
- `tools/validate_site_data.py` — validates project/activity relationships and generated RSS
- `.github/workflows/refresh-github.yml` — adaptive metadata/activity refresh in fifteen-minute slots
- `.github/workflows/enrich-evidence.yml` — hourly bounded evidence slices
- `.github/workflows/pages.yml` — GitHub Pages deployment
- `schema.md` — field definitions and evidence rules
- `sources.md` — human-readable discovery map and search strategy; canonical queue/state lives in `data/discovery-sources.json`
- `log.md` — historical search/discovery notes

There is no rendering framework or build step. The browser reads the JSON data directly. A GitHub Action runs in fifteen-minute slots: projects with commits in the last 14 days are probed every slot, those last active 15–60 days hourly, 61–180 days every four hours, and older or archived projects every twelve hours. Deep activity scans retain their separate adaptive daily to 56-day cadence; any detected push queues an immediate scan. Activity collection is incremental, retaining 180 days locally instead of re-downloading that history. ETags can save primary quota when GitHub actually returns 304, but the probe loop respects the live `X-RateLimit-*` headers and a capped reserve even when ETags miss. A 4,000-request HTTP safety cap plus 0.10 s request pacing protects against runaway or secondary-limit behaviour. Unfinished deep scans remain queued. Repository probes are ordered oldest-first, and queued deep scans prioritize detected changes then least-recently scanned repositories. Empty language metadata is retried after 30 days or a push; release metadata is checked at least every six hours for active projects and daily for others. Only material changes to public data trigger a Pages deployment. A separate hourly enrichment slice checks changed or overdue projects for explicit build/playability/byte-exact/start evidence and CI signals. Each slice retains a 300-HTTP-request ceiling and at most 600 seconds of collection, with an additional 80-request GitHub API ceiling and separate caps of 60 CI checks and 64 document checks, leaving room inside the unchanged 20-minute job limit for validation and publication. The [polling capacity study](docs/github-polling-capacity-2026-09-26.md) documents the measurements behind this schedule.

Project identity is separated from catalogue presentation: `upstream_name` preserves the project's own name, `display_title` gives the UI a concise human-readable subject/purpose label, and `subjects` records the actual legacy software names so opaque project brands remain searchable. For example, Firestaff is displayed as a Dungeon Master / Chaos Strikes Back engine reconstruction while retaining `Firestaff` as its upstream name.

CPU discovery and runtime compatibility are deliberately separate. The visible **CPU** facet groups exact source/target CPUs into useful families (for example **68000 family**), while optional verified `runtime_profiles` power the separate **Runs on** filter for minimum CPU, RAM and chipset. This avoids presenting a 68020-only build as 68000-compatible merely because both are m68k.

Project classification is deliberately multi-axis rather than a flat tag pile: `record_class` distinguishes subject/tooling/hybrid records, `target_kinds` says what legacy software is being studied, `work_kinds` says what kind of reconstruction/analysis is being done, and `tool_kinds` says what a modern aid actually does. Existing `types` and free-form `tags` remain available for nuance and search.

Evidence enrichment uses `tools/enrich_evidence.py collect --bundle <outside-checkout-path>` and `apply --bundle <same-path>`. Collection writes a temporary replay bundle without editing the catalogue. Publication replays it against latest main, validates the staged catalogue and commits changed project partitions with `state/enrichment-state.json` in one fast-forward update. Material promotions also use the existing catalogue-event recorder in staging and commit activity/catalogue state with the results; unrecorded changes on latest main defer replay until metadata refresh finishes. A push retry reuses the bundle without refetching; conflicting source versions or evidence/build edits remain due instead of being overwritten. Workflows serialize enrichment runs rather than canceling active collection.

The scheduler keeps one current entry per active project: hashes, timestamps and a bounded retry counter; it stores no duplicate project facts, document bodies or growing history. Canonical automated evidence is reused by immutable repository commit, configured path/candidate paths and collector version. CI refreshes independently after seven days; documents are reverified after 30 days or detected changes. Each work queue prioritizes known changed inputs within a bounded allocation, while reserving oldest-overdue capacity. CI and documents have independent attempt/freshness/retry state so cheap CI cannot move unfinished document work to the back of its queue. Observed-input hashes retain change priority for unfinished components even when the other component publishes newer work; they do not mark either component complete. Failed requests use bounded backoff. Only confirmed missing document paths count as absence; transient failures retain prior evidence. Completed documents can publish while failed CI signals remain unchanged and due. State is pruned for removed projects and checked against the shared 4 MiB escaped-request ceiling. Bump the collector version when extraction semantics change.

Enrichment capacity is explicit, rather than a promise to scan the catalogue every day. CI gets at most 60 one-request checks/hour (20% of the HTTP ceiling), with 15 changed-input slots and at least 45 oldest-overdue slots when both queues are busy. It queries the configured branch directly, without a per-record head request. Documents receive the remaining 240 requests and unused CI allocation, with half reserved for oldest-overdue work; the 64-record cap also bounds cheap cache verification. Priority/overdue shares reserve wall time and API requests as well as HTTP requests, unused priority capacity flows to oldest-overdue work, and unused CI request allocation flows to documents. Total load stays at 300 HTTP requests/hour; API traffic is capped separately at 80/hour. The optional `--records`/dispatch `records` total cap defaults to zero (use the separate caps); `records=1`, `doc_records=1`, `ci_records=1`, `requests=20` gives a small verification run.

At about 3,266 GitHub records / 3,113 roots, cold documents cost up to 17 non-redirected requests (one fallback head + 16 paths), so the conservative normal capacity is 14 cold records/hour: initial document backlog under 10 days. Even continuous changed-input pressure leaves seven cold overdue records/hour, or under 20 days for that population, fitting the 30-day horizon. CI alone costs one request: 60/hour normally, 45/hour reserved under pressure, clearing that root backlog in under three days against a seven-day horizon. Redirect hops consume the same budgets and reduce throughput. These are healthy-service capacity targets, assuming hourly runs and change volume within the priority allocation, not guarantees during failures, rate limits or exhausted time budgets. Per-work backlog, completion and lane counters expose shortfalls instead of marking unfinished work fresh. The earlier full scan averaged about 2.5 seconds/record in flushed progress batches; the ten-minute collection ceiling remains the hard safety bound.

Change detection reuses `github-poll-state.json`'s full repository `last_seen_pushed_at` and branch `tip_sha`. Project-level `pushed_at` is day-only and `latest_commit` may be path-filtered or historical, so neither alone authorizes cache reuse. A document scan reuses an immutable tip only when the matching branch is present, the last successful probe is at most 13 hours old (the existing poller allows up to 12-hour cadence), a successful scan covers the observed push, and there is no pending scan, error or publication. Otherwise it performs a budgeted head lookup. Thus prioritization follows observed metadata changes, with the poller's detection delay; it does not claim instantaneous upstream detection. Warm CI needs no tip at all.

Unknown facts stay **unknown**. In particular, absence of evidence does not become “No” for AI use, byte exactness, buildability or dates.

## Discovery passes

For a publication-ready pass, use the [single-authoring research record](docs/research-records.md)
and [repeatable publication pipeline](docs/publication-pipeline.md). One reviewed
area narrative generates project notes, audits and the report. Preparation emits
an exact-diff review bundle; connector publication preserves expected-SHA leases
and verifies the authored tree. Catalogue publication refreshes only changed
repositories, completing their metadata/history/context before Pages. Scheduled
maintenance continues its normal broad adaptive polling and recovers incomplete
first scans. Existing catalogue records and legacy batches need no migration.

The daily `discovery-intake.yml` workflow rotates GitHub repository/README and code searches, lists repositories under selected source profiles, checks selected repository READMEs and title directories, and mines GitHub links from selected source websites. It screens hits locally and writes a ranked review queue to `state/discovery-intake.json`, retaining query/source provenance and per-route counts. `python tools/discovery_intake.py --list 30` shows its highest-ranked leads; `python tools/discovery_intake.py` runs the same intake locally with `GITHUB_TOKEN`. `workflow_dispatch` runs it on demand and accepts optional newline-separated candidate URLs. External web *search* still needs an interactive search provider; this job follows curated website sources but does not scrape a search engine. The intake queue never changes project or research decisions.

Screen search-result URLs before opening candidate pages: `python tools/screen_discovery_candidates.py --input candidates.txt --route 'web search'`. The input can be one URL per line or a JSON array of URLs / `{ "url": "...", "route": "..." }` objects; use `--input -` for stdin or `--json` for structured results and per-route counts. It combines current projects, source nodes and reviewed decisions without making GitHub API calls. A known profile or repository can still contain new projects; inspect `known_repository_path` hits and unreviewed/deferred matches rather than discarding them. Redirected/renamed URLs can be recorded as duplicate decisions linked to the current project ID, giving future searches an exact alias match.

Prepare one JSON batch containing a date, unique research-event ID, summary and the reviewed additions/updates. Use `python tools/apply_discovery_batch.py batch.json` to preview; add `--write` only after reviewing the summary. The tool links projects to source nodes, creates an unreviewed audit when an explicit audit is not supplied, inserts a newest-first research event and validates the complete proposed tracker before writing any file. It rejects duplicate IDs and repeated project URLs unless a shared URL is explicitly acknowledged. Batch format and a runnable example are in [the discovery workflow guide](docs/discovery-workflow.md).

Projects and audits use `tools/catalogue_storage.py` as their shared loader/writer. Records route by SHA-256 of the ID, initially one hex digit (16 partitions per dataset). Only an overflowing prefix splits further; insertions do not move unrelated records. Indexes preserve record order, audit metadata and shard digests; shards contain records only. Each serialized, JSON-escaped connector request is limited to 4 MiB, with 12 MiB of headroom below the connector limit. An individually oversized record or index fails explicitly before writing; review/split its content rather than bypassing the bound. Only changed partitions and indexes are published. No-op writes preserve bytes, and source-only research leaves audits untouched.

The old `projects.json` and `project-audits.json` names remain logical CLI/input names for compatibility, not writable files. Historical snapshots can be read through the same loader's narrow legacy path; mixed monolith/index layouts are rejected. `python tools/catalogue_storage.py` migrates a legacy checkout and verifies exact logical equality. Commit the generated indexes/partitions and deleted monoliths together. Browser loading reads the project index and project partitions, plus the existing lazy activity windows; audits are not loaded by the browser.

Commit all changed data files together after `python tools/validate_site_data.py data/projects.json data/activity.json` and `git diff --check`. Publish one commit against the current `main` ref. Catalogue changes trigger a metadata refresh and then Pages; research-index-only changes deploy directly through Pages. Check the relevant runs before finishing. In Codex Work, use the linked GitHub connector for the atomic tree/commit/ref update; the workspace shell may not have authenticated Git credentials. The existing `automation/discovery-*` workflow can also validate, fast-forward and remove a temporary discovery branch. Do not publish intermediate project/audit/source changes separately.


The site header shows the activity-data refresh time. With no saved preference, the site follows the browser/operating-system light/dark preference. Manually using the Light/Dark toggle creates a local override stored in `localStorage` under `retro-development-tracker.theme`; merely following the browser default does not write anything. No other UI settings are persisted yet. The Activity view loads slim 30-day and 180-day browser feeds, showing individual recent commits and older daily summaries. Project additions show a frozen latest commit/release and 90-day activity count after their first completed repository scan. RSS publishes completed UTC-day commit digests, releases and meaningful catalogue changes; pre-tracking backfills and pre-rollout catalogue additions do not become new feed items. Pages deployment validates the JSON relationships and generated RSS before publishing.


The maintenance workflow writes rate-limit diagnostics to its GitHub Actions step summary, including actual limit, remaining quota, reset time, HTTP request counts and conditional 304 counts.


Conditional ETags are treated as an optimization, not as assumed savings: if GitHub returns `304 Not Modified` they are recorded separately, but scheduling decisions still use the actual remaining quota reported by GitHub.


The workflow schedules both NZST and NZDT UTC equivalents and selects the correct pair from the current `Pacific/Auckland` offset, so the 6:30 AM/PM refresh times remain stable across daylight-saving changes.
