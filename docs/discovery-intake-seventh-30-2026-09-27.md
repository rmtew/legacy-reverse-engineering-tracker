# Seventh discovery intake: next 30 leads

Reviewed a fixed snapshot of the next 30 ranked URLs on 2026-09-27. Each URL was screened locally before GitHub metadata, root, README and selected source/lineage reads. This is a research pass; build and run statements below are attributed to upstream documentation.

**Result:** nine projects, two retained reference sources and 19 exclusions. All 30 reviewed URLs are represented in the research index and removed from the open queue.

| Rank | Candidate | Outcome | Evidence and scope |
| ---: | --- | --- | --- |
| 1 | cyxx/dpoly_js | Project | Flashback polygon cutscene player on Web canvas/audio, derived from the already tracked REminiscence engine; no full-game reconstruction claim. The exact source data edition remains unverified. |
| 2 | cyxx/extract_android_ota_payload | Excluded | Android OTA firmware utility, outside retro software. |
| 3 | cyxx/extract_fb_genesis | Project | Flashback Genesis ROM data extraction, with four named ROM variants; game assets rather than executable disassembly. |
| 4 | cyxx/hugo_js | Project | Hugo Délire train mini-game browser player and C animation/resource tools, with narrowly documented scope. |
| 5 | cyxx/hulabee | Project | SDL2 Sauce VM rewrite, .pan/.gg decoders and opcode-trace DLL; VM README names two supported games and missing features. |
| 6 | cyxx/igor | Project | Spanish-CD Igor x86 executable decoder and game-specific interpreter; author calls it a proof of concept and lists missing original save/load screen. |
| 7–8 | disastos/.github; lushtree-cn-honeyzhao/awesome-c | Excluded | Organization profile metadata and broad C links list, respectively. |
| 9 | dpt/Aha | Project | Henry Warren's superoptimiser adapted for ARM/Thumb BIC/RSB; original source retained on `distrib` branch. |
| 10 | dpt/Containers | Excluded | General C associative-array structures, without a retro target. |
| 11 | dpt/davespace.co.uk | Source | Author site source contains RISC OS/ARM and Great Escape project material; retain as a reference, no second application record. |
| 12–16 | dpt/DPTLib, DPTSteppedProgressBar, Explosion, LEGOKit, MarbleRunKit | Excluded | Portable library, SwiftUI widget, SDL3 particles and Blender assets with no demonstrated retro recovery function. |
| 17 | dpt/MotionMasks | Excluded | Generic RLE mask compositing research, with no historical-software lineage shown. |
| 18 | dpt/PatchedPRMs | Source | Patches for the RISC OS Programmer's Reference Manuals CD; useful reference material, not reconstructed executable code. |
| 19 | dpt/PhotoFiler | Excluded | Ordinary RISC OS image thumbnailing application. |
| 20 | dpt/PrivateEye | Project | `libs/appengine` is a separate reusable RISC OS desktop C library within the image-viewer repository. The viewer itself is not labelled a reconstruction. |
| 21 | dpt/SinclairLogo | Excluded | Interactive logo/typography generator, unrelated to Spectrum program analysis. |
| 22 | dpt/SlopAY | Project | Z80/AY player and audio export for Spectrum/CPC files; companion macOS MIDIAY in same project. README explicitly says much of the new code was vibe-coded. |
| 23–25 | dpt/StableDiffusionWorkflows, Toolbar, Utils | Excluded | Image-generation presets, ordinary RISC OS launcher and generic file scripts. |
| 26 | dpt/zerotape | Project | Generic C serializer explicitly built to save/load reconstructed state in the already tracked Great Escape in C project; not a Spectrum tape decoder. |
| 27–30 | fschuhi/anima and three digital-garden repositories | Excluded | Modern PDF annotation and religious-text publishing tools/content. |

## Programmatic observations

| Finding | Applied or proposed procedure | Limit |
| --- | --- | --- |
| Flashback appeared in three Cyxx repositories, with a full engine already tracked elsewhere. | Preflight now reports up to 20 distinct external GitHub repository roots mentioned in a README, without another request. This surfaces lineage leads before expensive inspection. | An outbound link may be a dependency or citation; it cannot prove duplicate lineage or divergence. |
| Some relevant work is below `vm/`, `tools/` or `libs/appengine/` while the root names a different product. | Keep the root/README preflight cheap, then use a bounded one-level inventory for promising mixed repositories. | Directory names do not justify splitting a project until code and scope are inspected. |
| Title words such as `tape`, `retro` and `Sinclair` misidentified a generic serializer, particle demo and logo generator. | Screen metadata and primary README for a concrete original artifact or development use before classification; keep `zerotape`'s Great Escape relationship explicit. | Positive or negative keywords alone cannot decide scope. |
| Six Cyxx and 18 DPT profile siblings dominate this fixed slice. | The existing `--max-per-profile 4` view provides a more diverse future review slice without changing saved rank order. | Siblings include real work; the cap affects scheduling, never eligibility. |
| Multiple game interpreters have partial runtime support and ambiguous original media variants. | Record platform and CPU unknowns at creation and give each audit a specific verification action. | A README's supported-game list is not an independently verified playable or byte-exact claim. |

The nine projects have explicit CPU audits. No new project was built or tested during this intake pass.
