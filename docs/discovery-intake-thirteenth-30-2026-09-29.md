# Thirteenth discovery intake: next 30 leads

Reviewed the fixed next 30 ranked URLs from the saved queue on 2026-09-29. Inspected repository metadata, READMEs, selected files and release directories; compared the MEGA65 debugger fork with its parent and checked the PET core succession. Repository roots represent coherent projects, including the Electron releases with documented changes or conversions. Builds, binary identity and hardware compatibility were not independently repeated.

**Result:** 14 queued project leads, one additional maintained successor project, two duplicates, 14 exclusions, and one audit task. All 30 queued URLs are resolved; nine remain in the saved queue. Four historical search-origin labels were materialized as named discovery sources to preserve attribution, and the successor has its own source record.

| Rank | Lead | Outcome | Evidence and boundary |
| ---: | --- | --- | --- |
| 1 | [MEGA65/m65dbg](https://github.com/MEGA65/m65dbg) | Project | Debugger fork with 206 commits ahead of its parent and concrete C debugger changes; credit upstream. |
| 2 | [Rhialto/PET_MEGA65](https://github.com/Rhialto/PET_MEGA65) | Duplicate → [MegaPET](https://github.com/Rhialto/MegaPET) | Archived predecessor explicitly says development continues in the merged PET/SuperPET core; record the maintained successor once. |
| 3 | [sho3string/GaplusMEGA65_R3_R6](https://github.com/sho3string/GaplusMEGA65_R3_R6) | Excluded; audit task | Specific Gaplus FPGA emulation core built from MiSTer2MEGA65 template; examine for separable software analysis if needed. |
| 4 | [slajerek/RetroDebugger](https://github.com/slajerek/RetroDebugger) | Project | C64, Atari 8-bit and NES real-time debugger frontends embedding credited emulator engines. |
| 5 | [The8BitTheory/qr128](https://github.com/The8BitTheory/qr128) | Project | C128/C64/VIC-20 QR routines and assembly; claimed MEGA65/X16 assembly support remains unfinished. |
| 6–8 | [C-libraries](https://github.com/ambynotcoder/C-libraries), [KhaozEngine](https://github.com/APKiwiOrg/KhaozEngine), [awesome-c](https://github.com/IMCG/awesome-c) | Excluded | Generic C links, a modern game engine, and a general C library directory respectively. |
| 9–10 | [iTantra](https://github.com/sasvanthu/iTantra), [Test](https://github.com/dpt/Test) | Excluded | Android mesh voice project with a misleading RetroSpeechCodec name; unrelated Xcode integer analyser. |
| 11–12 | [Chuckulus](https://github.com/Snuggsy187/Chuckulus), [Attack on Alpha Centauri](https://github.com/Snuggsy187/Electron-Attack-on-Alpha-Centauri) | Excluded | Original game and unexplained disk/tape release respectively; no concrete recovery, modification or reusable technique established. |
| 13 | [Blagger Mod](https://github.com/Snuggsy187/Electron-Blagger-Mod) | Project | Documented speed and obstacle changes in distributed Electron media; no patch source published. |
| 14 | [Crypt Capers](https://github.com/Snuggsy187/Electron-Crypt-Capers) | Project | Credited Electron adaptation and unfinished prerelease, distributed as media only. |
| 15 | [Exile Helper](https://github.com/Snuggsy187/Electron-Exile-Helper) | Project | Original Exile display modified to show live object/weapon statistics; binary only. |
| 16 | [Jetpac](https://github.com/Snuggsy187/Electron-Jetpac) | Project | Electron conversion with upstream physical-hardware and emulator test claims; release media, not full conversion source. |
| 17 | [Knight Lore](https://github.com/Snuggsy187/Electron-KnightLore) | Project | Incomplete Electron prerelease; limited emulator compatibility per author, binary only. |
| 18 | [Lunar Jetman](https://github.com/Snuggsy187/Electron-Lunar-Jetman) | Project | BBC-to-Electron port with partial interrupt assembly and author development account of sprite, memory, timing and sound work; no independent hardware test. |
| 19 | [Repton 2 Expansion](https://github.com/Snuggsy187/Electron-Repton-2-Expansion) | Project | Documented map, counters, play-area and rewind modifications in Electron media; binary only. |
| 20–23 | [clip-tools](https://github.com/fschuhi/clip-tools), [belkirk-jekyll-demo](https://github.com/Jondalar/belkirk-jekyll-demo), [iPHN](https://github.com/Jondalar/iPHN), [Nederland-24.bundle](https://github.com/Jondalar/Nederland-24.bundle) | Excluded | General clipboard utility, website demos, and Plex channel bundle. |
| 24 | [skoolkid/skoolkit](https://github.com/skoolkid/skoolkit) | Project | Spectrum snapshot/ROM disassembly, annotated documentation and reassembly tools; track the toolkit at root. |
| 25–26 | [arc-check](https://github.com/kieranhj/arc-check), [pyadf-releases](https://github.com/chjacob-tubs/pyadf-releases) | Excluded | Original Archimedes checkerboard demo; unrelated quantum-chemistry ADF package. |
| 27 | [Lanthorn](https://github.com/sharkusk/lanthorn) | Project | Interactive-fiction interpreter with loaders for historical disk formats; data/format support, not recovered game source. |
| 28 | [Commander X16 ROM](https://github.com/commanderx16/x16-rom) | Project | Open source BASIC/KERNAL/DOS/GEOS continuation from credited Commodore source; do not imply binary-derived reconstruction. |
| 29 | [Shaid/claude-agents](https://github.com/Shaid/claude-agents) | Project | Game reverse-engineering agent/skill toolkit with concrete tracing, decoding and documentation procedures. |
| 30 | [Another World `tree/master/issues`](https://github.com/arqueologiadigital/another-world-archaeology/tree/master/issues) | Duplicate | Tracked project has this research directory on `main`; stale `master` path is not a separate project. |

## Programmatic observations

| Observation | Procedure applied or opportunity | Limit |
| --- | --- | --- |
| A queued directory URL used `master`, but its already tracked repository uses `main`. | On a nested-path 404, preflight now looks up the single known default branch in the local catalogue and supplies a candidate alternative URL without another request. | The directory must still be inspected; a branch hint alone does not prove that the path exists. |
| PET_MEGA65 is archived and its README points to a merged maintained successor. | Reconcile explicit successor references and archive flags against known project identity before promoting another record; one predecessor duplicate can point to the successor. | A README continuation claim still warrants checking successor artifacts and scope. |
| Electron binary releases range from original games to named patches and ports. | Extract concrete change/port verbs, credited original and available source/media from README and file inventory, then route to review; distinguish release media from source reconstruction in records. | These signals cannot validate binaries or establish modified bytes without deeper analysis. |
| The debugger fork has real changes, while a game FPGA core derives from a common wrapper. | Inspect bounded upstream comparison and changed paths; keep game-specific emulation in an audit task under the standing scope instruction. | Commit counts and common templates alone cannot measure useful divergence. |
| Broad terms `ADF`, `Retro` and `reassembly tools` surface chemistry, modern voice code and general C links. | Cheap metadata and root-file filters can suppress many obvious mismatches, while retaining uncertain historical-format interpreters for inspection. | Acronyms and language alone are unsafe exclusion criteria: Lanthorn actually reads old disk media. |
| Several queue origin labels are search trails, not source IDs. | Preserve those four origins as named source records when saving researched results; future intake can normalize origin IDs when capturing leads. | Do not silently replace a specific provenance with a generic source. |
