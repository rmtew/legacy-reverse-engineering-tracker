# Twelfth discovery intake: next 30 leads

Reviewed the fixed next 30 ranked URLs after reconciling with the latest `main`. The 2026-09-29 metadata refresh put a large Acorn/BBC profile cluster ahead of the older remaining candidates. Checked GitHub repository metadata, root inventories, READMEs, selected source and fork commits. Projects are linked at repository roots when code, documentation and tooling form one coherent work.

**Result:** 19 projects, one technical reference source, eight exclusions and two duplicates. All 30 reviewed URLs leave the saved queue; 39 leads remain. No project was independently built or run.

| Rank | Lead | Outcome | Evidence and boundary |
| ---: | --- | --- | --- |
| 1 | kieranhj/arc-django-2 | Excluded | Original Archimedes musicdisk, without a demonstrated independent recovery or reusable tool. |
| 2 | kieranhj/archieklang | Project | ARM Archimedes port of AmigaKlang with sample-generation code, imported references and QTM harness; credit original synth. |
| 3 | kieranhj/arkos-player-bbc | Project | 6502 AKL/AKM/AKY players and AY-to-SN76489 conversion for a stock Model B. README explicitly credits Claude for new code, with human direction and review. |
| 4 | kieranhj/beeb-port-kit | Project | C64-to-BBC porting playbook and reusable 6502/Python code distilled from two shipped game ports; kit is separate from the tracked Paradroid work and new Edge Grinder port. |
| 5 | kieranhj/image2mode1 | Project | Image optimizer and BBC Master raster-timed MODE 1 display engine; repository root contains the converter and display code. |
| 6 | kieranhj/line-test | Project | BBC line-routine comparison harness with switchable routines, frame/raster controls and an Elite line-routine excerpt; not a new Elite disassembly. |
| 7 | kieranhj/llm-beeb-wiki | Source | Cited BBC performance knowledge base, authored with LLM support; useful reference, not a reconstructed program. |
| 8 | kieranhj/vgmplay | Project | Early BBC VGM player source and disk; README says later simondotm tools superseded it. |
| 9–10 | kermitfrog/inputmangler; kbddisplay | Excluded | General Linux input remapper and keyboard cheat sheet. Mentioning DOSBox or FS-UAE does not confer project scope. |
| 11 | kieranhj/archie-face | Project | Archimedes C environment with video banks, interrupts, debug and rendering helpers. |
| 12 | kieranhj/archie-verse | Project | ARM2/ARM250 trackmo framework, integrated music/video/debug parts. |
| 13 | kieranhj/edge-beeb | Project | Source-led C64 Edge Grinder port to BBC Master 128 with documented hardware changes, disk and browser run links; CPC tune credited. |
| 14 | kieranhj/fight-or-flight | Excluded | Aircraft-noise web app. |
| 15 | kieranhj/funky-fresh | Project | Reusable BBC demo framework with banked effects, timing and Rocket sync. |
| 16 | kieranhj/globe | Project | BeebAsm globe demo translated to Archimedes ARM assembly; no byte-match assertion. |
| 17 | kieranhj/image2mode7 | Project | Teletext image optimization, preview and DFS export; README credits original algorithm and Claude co-writing. |
| 18 | kieranhj/img2ans | Project | CP437 half-block and CGA palette converter to DOS-style ANSI art. |
| 19 | kieranhj/proto-arc | Project | Reduced Archimedes prototype framework with triple buffering, music and debugger controls. |
| 20 | kieranhj/qtm-vasm | Project | QTM v1.49b source translated from tokenized BBC BASIC V assembler to vasm. Upstream reports byte-identical output for four variants and Arculator playback; not reproduced in this pass. |
| 21 | kieranhj/raster-fx | Project | Generic BBC palette timing/interrupt framework, separate from image2mode1's integrated display path. |
| 22 | kieranhj/rocket-podule | Project | Rocket Sync Tracker podule integration for Arculator, with author commits for input callbacks. |
| 23 | kieranhj/stipple-256 | Excluded | Original BBC Master intro and bespoke asset scripts supporting it; no separately reusable tooling established. |
| 24 | angree/QLOOP--Any-Video-To-Looped-Animated-Repeatable-Texture | Excluded | General modern video texture loop/tiling processor. |
| 25 | ataribaby42/elite-source-code-nes | Duplicate with divergence | Copy of tracked Mark Moxon NES Elite source. Local commits add build conveniences and options to omit planet detail and scanner lettering; record changes, credit predecessor, avoid another reconstruction entry. |
| 26 | Attackwave/gimle-os | Excluded | Repository URL returns 404; the owner's separate m68k assembler is already tracked. |
| 27 | dansanderson/mega65-symbols | Project | I/O symbol generator from VHDL-derived MEGA65 register map; includes checked-in assembler/C definitions. |
| 28 | gcastel/mega65-cal | Excluded | Original MEGA65 calendar program, outside focused recovery/tooling scope. |
| 29 | grue74/ghidra-c64helpers | Project | Ghidra fork has actual PETSCII/C64 byte-viewer formats and 6510 processor changes relative to NSA parent; upstream README alone obscures them. |
| 30 | hyphz/crossroads-2-disassembly | Duplicate redirect | Old owner URL resolves to already tracked MarkRdgOx/Crossroads 2 disassembly. |

## Programmatic observations

| Observation | Applied procedure or next opportunity | Limit |
| --- | --- | --- |
| Renamed repository #30 looked locally new despite its canonical URL already being tracked. | Preflight now extracts the canonical repository root from the existing contents listing and screens it locally; no extra API request. Record the old URL as a duplicate/redirect for future queue reconciliation. | Empty or inaccessible repositories need a metadata/redirect request; canonical identity says nothing about project merit. |
| Twenty-three URLs came from the same profile in the top ranked slice, combining reusable frameworks with original demos and a web application. | Use existing optional `--max-per-source` view for variety during early reviews; preserve the fixed ranked queue for accountable batches. Metadata and root-file signals route inspection. | A cap must not silently discard siblings; simple platform or language heuristics would misclassify the meaningful port and frameworks. |
| The NES Elite copy is not a GitHub fork, yet three local commits alter build outputs and add two game presentation switches. | Compare author commits and changed paths against known upstream before deciding duplicate vs a separately tracked implementation. Document the options in the duplicate decision. | A `fork: false` flag does not prove originality; two presentation toggles here did not justify a second reconstruction. |
| The Ghidra fork's README repeats upstream, while changed files reveal PETSCII viewers and a 6510 specification. | Prefer bounded parent comparison and targeted source paths to README-only decisions for broad forks. | An ahead count can be inflated by merges and cannot establish relevance by itself. |
| Several README claims include AI authorship, hardware requirements and byte-identical builds. | Preserve explicit provenance and tested scope in project notes and audit fields; keep upstream test reports distinct from independent verification. | Builds, byte matching and minimum hardware were not repeated here. |
