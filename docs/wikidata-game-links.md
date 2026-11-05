# Wikidata game links

`tools/wikidata_games.py` maintains an offline, subject-scoped Wikidata index.
It does not edit canonical project records, audits, repository metadata or
discovery judgments. The existing site build copies the resulting public JSON.

## Refresh and match

Run from a complete checkout of current main:

```
python tools/wikidata_games.py refresh --root . --max-age-days 30
python tools/wikidata_games.py match --root .
python -m unittest discover -s tools -p 'test_wikidata_games.py'
```

The first command queries Wikidata when the cache is missing or its full refresh
is 30 days old. A new catalogue subject or manual override QID triggers only the
new lookups while the cache is fresh. Incremental updates retain the original
full-refresh date, so repeated discoveries cannot postpone periodic rebuilding.
`--force` performs a complete scoped refresh. Matching performs no network work.

The source scope is subject/hybrid records explicitly tagged `game`. Every
queried subject is recorded in the cache. A subject added after collection is
reported as `not-indexed` until a refresh covers it; matching an old alias alone
cannot promote a newly added subject. Applications, pure tooling and engine-only
records are excluded even if their names collide with games.

## Bounded acquisition

The index covers candidate items with Lemon Amiga `P4846`, Lemon64 `P4816`, or
MobyGames `P11688`. It is not a copy of all Wikidata video games. Exact labels and
aliases in English (`en`) and language-independent/multilingual (`mul`) are
queried in batches. Subject variants include their original spelling, title case
and normalized apostrophes; an explicit trailing release-year annotation is
removed for candidate lookup. This deliberately does not claim fuzzy or
exhaustive matching of every spelling.

Every returned candidate retains its QID, names/aliases, platform QIDs and labels,
release dates, and all valid numeric IDs for the three databases. Tall fact rows
avoid cross-products between optional aliases, platforms, dates and identifiers.
All same-name candidates are retained. The candidate safety ceiling fails the
refresh rather than silently discarding possibilities. HTTP 429/5xx responses get
bounded retries; persistent query timeouts split batches into smaller requests.
There is no OFFSET scan of the complete Wikidata graph.

Defaults are 40 name variants per batch, 60 seconds per request, a 900-second
overall budget and 500 subject batches. `--page-size`, `--timeout`,
`--max-runtime` and `--max-pages` are available for operational tuning. Ordinary
fresh-cache runs make no network requests. A full run with about 2,500 distinct
subjects is expected to need roughly 125–250 requests, depending on spelling
variants, candidate reuse and timeout splitting. Actual WDQS latency varies.

## Matching and review

Automatic acceptance requires an exact normalized title/alias and independently
matching **source** platform evidence, with one remaining candidate. Normalizing
case, spacing and punctuation is not fuzzy title matching. Target platforms,
repository dates and `re_started` are never treated as original-game evidence.
An explicit subject release year can reject contradictory candidates but cannot
replace the platform requirement. An unknown platform does not eliminate a
competing candidate. Missing evidence, conflicting evidence and ambiguity remain
separate review states.

`state/wikidata-review.json` records unresolved subjects, candidate identities,
platform/date evidence and reasons. At most 20 candidates are displayed per
subject, accompanied by the complete count; matching always considers all of
them. Items with several IDs for one external database retain all of them in the
index, but the public link is omitted rather than choosing one arbitrarily.

`config/wikidata-overrides.json` is hand-maintained and never rewritten. Its
`projects` object maps a project ID to exact subject strings. Each value has
`qid` and a nonempty `reason`. A QID explicitly selects a game, while `null`
suppresses automatic linking. Override QIDs are fetched independently of title
search, and changes invalidate a fresh cache. A QID absent from the cache can
still retain the explicit manual Wikidata reference, with no invented external
IDs and a review warning. Stale overrides remain intact and are reported.

## Files and contract

- `state/wikidata-index.json`: complete cached candidates and scope/provenance.
- `state/wikidata-review.json`: unresolved subjects and warnings.
- `data/game-links.json`: accepted links only, keyed by project ID.
- `config/wikidata-overrides.json`: reviewed manual selections/exclusions.

The public document has `format: tracker-game-links/v1`, `generated_at`,
`index_generated_at`, and `projects`. Each project has an array of objects with
`subject`, `qid`, `lemon_amiga`, `lemon64`, `moby`, `match` and `evidence`.
Database IDs are numeric strings or `null`; `match` is `exact-title-platform` or
`manual`; `evidence` is the canonical Wikidata item URL. Manual entries also have
the authored `reason`. The UI should construct external URLs from validated IDs.
Missing documents/project keys mean that no accepted links are available.

Public/review timestamps retain the last material resolution when a repeat
match or an otherwise identical index refresh changes no contents. This avoids
deployments caused only by freshness timestamps. The index itself retains the
actual collection/full-refresh times and source properties.

## Actions and failure handling

No scheduled refresh workflow is enabled yet. Refresh and match can be run manually
when Wikidata access is available. Run matching after new research as well when practical. On the
first deployment, an Actions run can bootstrap the index if the editing
environment cannot reach Wikidata; ordinary PR tests are completely offline and
must not depend on the service.

A failed/incomplete refresh exits nonzero and does not replace the old complete
index. A failed match preserves existing public links. There is no fallback to
fuzzy or title-only matching. Do not commit partial or missing collected outputs.
If refresh fails and a verified old cache exists, matching may explicitly run
against that cache; new subjects stay `not-indexed`. Publish against latest main
so concurrent project additions/removals cannot be lost. Stage only the generated
index/review/link files, not unrelated catalogue or automation state.

Wikidata structured data is CC0. The cache identifies its source endpoint and
properties; every accepted link preserves the item URL as provenance.

The initial index is a limited live-tested seed covering Dungeon Master, Elite and Lemmings. Other subjects remain explicitly not indexed until a complete refresh succeeds.
