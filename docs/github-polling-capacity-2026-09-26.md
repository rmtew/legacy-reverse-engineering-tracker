# GitHub polling capacity study (26 September 2026)

**Implementation update:** The configured 15-minute/1-hour/4-hour/12-hour probe tiers, live-quota reserve for all probes, bounded request history, negative language cache, independent release checks, and material-change Pages gate have now been implemented. The measurements and whole-catalogue estimates below describe the previous twice-daily baseline. Newly added projects bypass the tier deadline in both direct catalogue pushes and dispatched discovery landings; manual dispatch can request a full sweep explicitly. Monitor actual quota and publication latency after the new schedule has run for a day before shortening a tier.

## Schedule verification (26 September 2026)

**The configured quarter-hour CI cadence is not verified and the previous GitHub schedule had multi-hour delivery delays.** The original `7,22,37,52 * * * *` cron was committed at 03:48 UTC and rewritten as four separate valid entries at 05:42 UTC. Both syntaxes are valid under GitHub's documented POSIX cron rules. Through 06:15 UTC, every refresh run after 03:48 was a `push` run; no new `schedule` run was created. The 04:09 UTC refresh completed at 04:11 UTC but was triggered by a push. A temporary diagnostic workflow succeeded on push and queried GitHub's workflow API using `GITHUB_TOKEN`: the refresh workflow state is **active**, with workflow ID 364772732. The diagnostic file was removed afterward.

The earlier twice-daily schedule's own logs contain `github.event.schedule`. Comparing that intended cron slot with the Actions run creation time exposes substantial delays (UTC throughout):

| Intended cron slot | Actual run created | Delay | Result |
| --- | --- | --- | --- |
| Sep 25 05:30 | [Sep 25 10:21](https://github.com/rmtew/legacy-reverse-engineering-tracker/actions/runs/36123547329) | 4h 51m | DST alternate skipped as designed |
| Sep 25 06:30 | [Sep 25 12:03](https://github.com/rmtew/legacy-reverse-engineering-tracker/actions/runs/36132779704) | 5h 33m | Selected NZST refresh |
| Sep 25 17:30 | [Sep 25 20:38](https://github.com/rmtew/legacy-reverse-engineering-tracker/actions/runs/36186977455) | 3h 08m | DST alternate skipped as designed |
| Sep 25 18:30 | [Sep 25 21:44](https://github.com/rmtew/legacy-reverse-engineering-tracker/actions/runs/36193139730) | 3h 14m | Selected NZST refresh |

The queue delay occurred **before** a runner started, not in the Python poller or the site's date display. A scheduled event's creation is missing altogether for the new cron as of this check, but earlier delays prevent us from concluding those particular events were dropped rather than still pending. GitHub documents that schedule events can be delayed or dropped. The project currently has no measured 15-minute timer, even though the per-project due logic, manual dispatch, human catalogue pushes, and explicitly dispatched discovery landings are functional. A 15-minute detection objective needs an independent clock calling the existing `workflow_dispatch` endpoint, plus an age-of-last-run check; an external scheduler and its GitHub credential have not been provisioned. Keep native cron as a fallback until the independent trigger is observed working. Do not estimate publication latency from configured cron alone.

Evidence: [refresh runs](https://github.com/rmtew/legacy-reverse-engineering-tracker/actions/workflows/refresh-github.yml), [04:09 push run](https://github.com/rmtew/legacy-reverse-engineering-tracker/actions/runs/36216994071), [05:42 push run](https://github.com/rmtew/legacy-reverse-engineering-tracker/actions/runs/36221605073), [diagnostic workflow-state run](https://github.com/rmtew/legacy-reverse-engineering-tracker/actions/runs/36222990024), [GitHub's schedule documentation](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule).

Initial live run (03:49–03:52 UTC): 272 of 592 repositories probed; 320 deferred; 557 HTTP requests (272 conditional probes, zero 304s, 200 HTTP 404 responses, mostly expected release lookups); three changed repositories deep-scanned. The first response reported 4,999/5,000 remaining and the final probe response 4,734/5,000, a 265-unit observed delta across the phase, smaller than the HTTP-call count. This is a measured delta, not a promise of a stable discount: other API activity and response behaviour can change it. The following refresh had no repositories due and made zero HTTP requests. Its moving activity window still changed AI evidence counts, which incorrectly triggered a Pages deployment; the collector now updates that evidence only when it fetched commits for the project. An idle run also retains the last quota header snapshot until reset instead of replacing it with unknown values.

Discovery integration: direct chat-authored catalogue commits trigger the push refresh and defer Pages until it completes. When the new adaptive probe has no further metadata to write, Pages still recognizes the original catalogue push and deploys it. Scheduled discovery branches use the landing workflow's explicit refresh dispatch; the refresh merges pending projects, probes new IDs immediately, records additions, and dispatches Pages when done. A first scan that finds a recent commit immediately promotes a newly added project to the 15-minute probe tier, even if the catalogue initially had no activity date. Normal scheduled polling does not spend quota on an unnecessary full sweep after each discovery landing.

## Present behaviour

The `Refresh GitHub metadata` workflow selects two runs per Auckland day, around 06:30 and 18:30. It also runs on certain human-authored catalogue pushes and explicit dispatch. Every run probes **every distinct tracked repository** with `GET /repos/{owner}/{repo}`. The adaptive 1/3/7/14/30/56-day intervals apply to *deep branch/commit scans*, not to these repository probes. A changed `pushed_at` queues an immediate deep scan. The collector skips commit queries on branches whose tip SHA has not changed. Each refresh persists probe timestamps/ETags, and a successful workflow run triggers a Pages deployment.

In the state last updated 2026-09-26 02:17 UTC there are 592 distinct repositories, including 86 in the daily deep-scan tier, 113 in the three-day tier, 104 seven-day, 109 fourteen-day, 171 thirty-day, and 9 archived at 56 days. All 592 have an ETag, but every sampled completed run reports **zero 304 responses**. Accordingly, budget one quota unit per probe until we understand or fix the ETag behaviour. GitHub says properly authenticated conditional requests that actually return 304 do not count against the primary quota; sending an ETag is not itself a saving.

## Measured requests

These are the workflow's own logs and persisted `X-RateLimit-*` header snapshots; the rows are *individual runs*, not independent hourly allowances. The last column includes both phases.

| Run start (UTC) | Repos probed | Probe HTTP | Activity HTTP | Total | Final reported quota | Notes |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| Sep 26 02:13 | 592 | 663 | 13 | 676 | 3,708 / 5,000 | 2 pushed changes; 6 deep scans |
| Sep 26 01:21 | 588 | 645 | 5 | 650 | 4,367 / 5,000 | 1 pushed change; 2 deep scans |
| Sep 26 00:13 | 579 | 641 | 169 | 810 | 4,208 / 5,000 | 140 deep scans |
| Sep 26 00:49 | 587 | 678 | 34 | 712 | 3,520 / 5,000 | 10 deep scans |
| Sep 25 22:44 | 579 | 936 | 3 | 939 | 4,156 / 5,000 | 304 missing historical-head lookups |

The 02:13 probe phase made 663 calls, including 592 repository probes and 4 historical-head lookups; the remaining 67 are primarily enrichment of repos with absent language metadata and changed metadata. A local catalogue count finds about 21 repositories with empty/missing `github.languages`; the code retries language, root contents, and sometimes release endpoints whenever the repository GET returns 200. Empty metadata currently has no negative cache. Two runs in the *same* quota window moved reported remaining from 4,367 (01:25) to 3,708 (02:17), confirming substantial charged usage. Other jobs can consume quota in that interval, so this difference is not a precise attribution of all 659 units to refresh.

The workflow response headers report a 5,000-per-hour limit during these runs, despite GitHub's general documentation saying the normal `GITHUB_TOKEN` limit is 1,000/hour per repository (15,000 for applicable Enterprise Cloud resources). Do not assume the observed 5,000 applies to every future token or environment. The scripts already read live limits and hold a 250-request reserve at 5,000. The probe phase deliberately allows conditional probes even after reaching that reserve, assuming they may be free; with zero observed 304s this safeguard is ineffective until fixed.

## Capacity estimates

Using **676 charged requests per full-catalogue run** as a recent example, and no benefit from ETags:

| Full-catalogue cadence | Approximate requests/hour | Approximate requests/day | Assessment at observed 5,000/hour |
| --- | ---: | ---: | --- |
| Current twice a day | about 56 averaged across a day | 1,352 | Comfortable, though runs can cluster after catalogue changes |
| Hourly | 676 | 16,224 | Comfortable |
| Every 30 minutes | 1,352 | 32,448 | Comfortable |
| Every 15 minutes | 2,704 | 64,896 | Plausible, but 96 refreshes and up to 96 Pages deployments per day |
| Every 10 minutes | 4,056 | 97,344 | Little headroom for deeper scans, weekly enrichment, or other API users |
| Every 5 minutes | 8,112 | 194,688 | Beyond the observed hourly limit |

The first row averages the two daily runs over 24 hours; each individual refresh still uses hundreds of calls in a few minutes. Actual work varies: sampled runs were 650–939 requests, and 140 deep scans cost another 169 calls. The current full sweep takes roughly four minutes. A full sweep every five minutes would almost continuously occupy a runner; GitHub also documents that scheduled jobs may be delayed or dropped. These are planning estimates, not a promise of detection latency or API capacity.

### Preferred staged approach

1. **Fix accounting first.** Record *start and end* `X-RateLimit-Remaining`, limit, reset, per-phase 200/304/error counts, GET versus enrichment/commit calls, and run duration in a rolling compact diagnostic; alert when fewer than 25% of runs return 304 or the run starts below a chosen reserve. Check why persisted ETags never get a 304 before counting on free probes. Cache stable negative language/release results or retry them on an infrequent timer, not on every unchanged repository GET.
2. **Add per-repository probe cadence**, separate from deep scan cadence: currently active (last tracked commit within 14 days) every 15 minutes; 15–60 days hourly; 61–180 days every four hours; older or archived every twelve hours. Use oldest-probed first and persistent timestamps, stagger each tier across slots, and force prompt probing of newly added projects. Keep the current changed-`pushed_at` immediate scan and the existing deep-scan intervals. Preserve an explicit 12-hour maximum age for quiet repositories. With the current distribution this produces roughly `86 × 4 + 113 + 104 / 4 + 289 / 12 ≈ 507` repository probes/hour before extras, versus `592 × 4 = 2,368`/hour for full sweeps every 15 minutes. Recompute after each catalogue change; these are averages, not peak-slot guarantees.
3. **Avoid a deploy on each probe-only run.** Store poll-state changes without committing/publishing per pass where possible (or separate probe state from public data), and deploy only when visible metadata or activity changes. Otherwise frequent probes cause commits and Pages rebuilds even when nothing upstream changed. Note that pushing with `GITHUB_TOKEN` will not itself start the normal push-triggered Pages workflow; maintain an explicit dispatch or equivalent for meaningful changes.
4. **Pilot 15-minute hot-tier polling** with limits derived from response headers, at least a conservative 250-unit reserve when the measured limit is 5,000, and slow down automatically when remaining quota or secondary-limit responses demand it. Evaluate 24 hours of quota minima, delays, API errors, 304 rate, changed projects, and Pages runs before shortening another tier. At the documented 1,000/hour `GITHUB_TOKEN` limit, the estimated 507 baseline leaves much less headroom, so live-header gating is essential.

Expected detection for a hot project would become about **7.5 minutes average / 15 minutes schedule bound**, plus runner queue time, scan time, commit, and Pages deploy. It is not real-time. The workflow currently refreshes `latest_release` only on a changed `pushed_at` or missing languages; a release created against an existing tag with no new push can be missed. Add a separately budgeted release check or consider GitHub webhook/dispatch integration if that latency matters.

Sources: [workflow](../.github/workflows/refresh-github.yml), [probe code](../tools/refresh_github.py), [collector](../tools/collect_activity.py), [state](../state/github-poll-state.json), [02:13 run](https://github.com/rmtew/legacy-reverse-engineering-tracker/actions/runs/36210984634), [01:21 run](https://github.com/rmtew/legacy-reverse-engineering-tracker/actions/runs/36208167636), [00:13 run](https://github.com/rmtew/legacy-reverse-engineering-tracker/actions/runs/36204045706), [GitHub rate limits](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api), [conditional requests](https://docs.github.com/en/rest/using-the-rest-api/best-practices-for-using-the-rest-api), [Actions schedules](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows).
