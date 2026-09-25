# Fresh-search pilot — 26 September 2026

This pass tested searches that start outside the existing discovery backlog. It was a bounded trial, not a claim to have exhausted any platform or every search result. Project additions and one resolved duplicate were applied as research event `2026-09-26-fresh-search-pilot`; source links, audits and the event are in the structured research indexes.

## Searches run

| Route | Queries / starting points | Observation |
| --- | --- | --- |
| GitHub repository/README search | `"atari st" "disassembly" in:readme`; `"amiga" "reverse engineering" in:readme`; `"commodore 64" "disassembly" in:readme`; `"amstrad cpc" "reverse engineering" in:readme`; `"zx spectrum" "disassembly" in:readme`; `"bbc micro" "reassemblable" in:readme`; `"nes" "byte exact" in:readme`; `topic:atari-st topic:reverse-engineering` | Eight first-page queries gave broad coverage, but many results were already tracked or had matching words in unrelated README sections. Exact jargon such as “reassemblable” underperformed on BBC Micro. |
| Global code search | `"byte-for-byte" "Atari ST"`; `"reassembled" "Amiga"`; `"C64" "Ghidra"`; `"Amstrad CPC" "disassembly"` | Four searches found useful format/tooling leads, including GFA Detokenizer and ghidra-retro-machines. Generic two-word searches also matched copied code, newsletters and unrelated occurrences in one file. Code searches need path/content scoping and selective README follow-up. |
| Web search outside GitHub repository search | Atari ST GFA format recovery; Amiga game disassembly; C64 game reconstruction; CPC reverse-engineering tools | Four themed queries found the CPC Z80 tool and the Mixup project, but also rediscovered tracked Batman, Bubble Bobble, Head Over Heels and TOS work. Results need canonical project checks. |
| Independent citation trail | [Dan Sanderson's Crossroads machine-code article](https://dansanderson.com/mega65/crossroads-part-2/) → its cited Crossroads II disassembly | The old `hyphz/crossroads-2-disassembly` GitHub path resolves to the already tracked `MarkRdgOx/crossroads-2-disassembly`. The article is indexed as a discovery node for its original Crossroads investigation, and the duplicate link is recorded explicitly. |

We screened the visible first-page hits and read sixteen candidate or related project READMEs, plus the Crossroads article and title-specific Mixup manifests. The ten new records represent eight distinct repositories; that count is **not** a success rate for all GitHub search results because the results were sampled, not fully adjudicated.

## Promoted work

| Discovery path | Project records | Primary evidence and boundary |
| --- | --- | --- |
| Code search → format project → companion repository | [GFA Detokenizer](https://github.com/NeHeGL/GFA-Detokenizer), [GFA Tokenizer](https://github.com/NeHeGL/GFA-Tokenizer) | Separate decode and encode tools, both checked against historical GFA-BASIC behavior; credit the earlier gfalist format research. Neither is a disassembly of the editor. |
| Code search | [ghidra-retro-machines](https://github.com/CBongo/ghidra-retro-machines) | Machine descriptors and implemented C64/C128/PET/NES loaders, with mapper coverage still evolving. |
| Repository README search | [Action Replay 5](https://github.com/dmcoles/ActionReplay5) | Amiga debugger reconstruction from Action Replay III/IV/ARIV sources with additional new code and 68000 assembler build variants. No historical byte-matching claim. |
| Web search | [z80-smart-disassembler](https://github.com/cormacj/z80-smart-disassembler) | CPC-ROM-motivated Z80 code/data disassembler with templates and assembler output. |
| Repository search → author's framework link | [MetroidNESRecomp](https://github.com/mstan/MetroidNESRecomp), [NESRecomp](https://github.com/mstan/nesrecomp) | Metroid targets the USA ROM and has incomplete game coverage; the framework is a separate reusable 6502-to-C tool. More linked title projects remain to review. |
| Web search → title-specific directories | [Batman: Return of the Joker](https://github.com/Fabulu/Mixup/tree/main/games/batman), [Gradius](https://github.com/Fabulu/Mixup/tree/main/games/gradius), [DoDonPachi DaiOuJou](https://github.com/Fabulu/Mixup/tree/main/games/ddpdoj) | The same Mixup repository contains three distinct original platforms and different completion states. The root README has newer progress than some title manifests. Frame/behavior parity does not mean a byte-identical rebuilt original ROM. |

The apparent Batman: The Movie Amiga, Head Over Heels CPC, TOS 1.4 UK, C64 Bubble Bobble rebb64 and C64 Archon hits were already in `data/projects.json`. The Faery Tale Adventure original-source repository already has an explicit exclusion decision. Other search hits remain unreviewed; a search appearance alone does not become a deferred candidate or a claim of exclusion.

## Improvements from the trial

1. Rotate **platform × work** combinations, including data formats and development tools, instead of repeating broad platform/disassembly terms. Search old and newly published work: creation date, last push and stars are optional sorting aids, not qualification requirements.
2. Screen normalized repository URLs, redirects, tracked `project_url` values and prior decisions before opening every README. Check the actual project files and upstream claims before promotion.
3. Use repository/README searches for broad recall. Use code search for a specific marker with `path:` or `content:` scoping; generic words in a large code corpus have low precision. Pace code queries and handle secondary search limits: a burst of duplicate-check requests in this pass returned HTTP 429.
4. Follow one or two *new* citation trails from promising hits. Record the trail even when it ends in an existing project, as the Crossroads redirect did.
5. Review monorepo components separately when their platform, work or completion state differs. Keep one shared source node, but give qualifying titles their own project URL and `github_path`.
6. Record each future pass's exact queries, date, route, inspected candidates, canonical matches, decisions, promotions and unexamined leads. Compare unique qualifying additions per *actually reviewed* candidate, not per raw search hit. Preserve follow-up tasks for mstan's other NES game projects and the original Crossroads research.

## Publication check

The discovery commit passed the full local data validator and deployed through Pages. During the ensuing push-triggered metadata refresh, a daylight-saving alternate scheduled run took the same concurrency group. Although that scheduled run intentionally skipped its refresh steps, its `cancel-in-progress: true` setting cancelled the active push refresh. The workflow now uses `cancel-in-progress: false` so an alternate schedule cannot discard an active catalogue refresh; queued work still uses the same single concurrency group. Verify the follow-up refresh completes and publishes its activity/catalogue metadata before treating this as resolved.

This pilot changed the catalogue and research indexes using the existing validated discovery batch workflow. It did not change the schedule or add an unattended search scraper.
