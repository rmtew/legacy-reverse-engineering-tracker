# Sixth discovery intake: next 30 leads

Reviewed a fixed snapshot of the next 30 ranked URLs on 2026-09-27. Screened local project and decision indexes first, then read repository metadata, roots, primary READMEs and selective source or lineage files. No new project was independently built or run.

**Result:** four projects and 26 exclusions. Every reviewed URL has a source or decision record and leaves the open queue on the next intake reconciliation.

| Rank | Candidate | Outcome | Evidence and scope |
| ---: | --- | --- | --- |
| 1 | fschuhi/a2-hires-lab | Project | Excel/VBA lab analyzing Apple II Lode Runner sprites, shift tables, NTSC colors and HGR memory, based on XekriRedmane's disassembly. Distinct from the author's tracked Lode Runner research. HISTORY explicitly documents LLM sessions and corrections to Gemini-authored assembly explanations. |
| 2 | angree/sf2000-frogui-modded | Excluded | FrogUI firmware interface fork for modern handhelds; no original-game analysis shown. |
| 3 | angree/vr-tbc-243-patch | Excluded | World of Warcraft 2.4.3 VR Direct3D proxy adapted from WoVR, without demonstrated historical-game binary reconstruction. |
| 4–7 | angree/WoW panic button and three WoW 2.4.3 addons | Excluded | Hotkey, chat filtering, audio announcements and translation, not legacy recovery or retro developer tools. |
| 8–14 | ataribaby42/DayZ mods | Excluded | Backpacks, creatures, weather, rally and hazard zones for DayZ; no historical-game analysis. |
| 15–17 | ataribaby42/SchneiderTrophy1927, Siege-of-Athira, WarthogChart | Excluded | Current flight-sim tool, ArmA mission and controller chart application. |
| 18–23 | Attackwave/caid, glasir, glasir-control, homebrew-glasir, mcrataway, scoop-glasir | Excluded | General KiCad, code-intelligence, packaging and Minecraft security tools. The two package repositories are release distribution for Glasir, not separate software analysis. |
| 24 | Bread80/BenPrommer-SDP | Excluded | Arduino breadboard EEPROM programmer with no identified historical-software target. |
| 25 | Bread80/Datapoint2200 | Project | `Software/OS` contains six assembly modules, binaries and assembly-order notes transcribed from the 1971 Programmer's Manual. The hardware schematics are separate and expressly unverified; no binary-derived disassembly claim. |
| 26 | Bread80/Keyboard-FPC10 | Excluded | CPC keyboard connector PCB, hardware only. |
| 27 | Bread80/RC2014-512K-ROM-512K-RAM-Board | Project | Z80 ROM-writing routines for RC2014's SST39SF040 module, RASM source and sample outputs. |
| 28 | cadaver/c64loader | Project | Standalone, smaller-runtime C64 fastloader v3 derived from `c64gameframework`/MW ULTRA, with distinct DASM source, drive support and restricted configuration. |
| 29 | cadaver/turso3d | Excluded | SDL3/OpenGL engine derived partly from Urho3D, with no retro-software target. |
| 30 | Crystal-Bell/Earth-2.0 | Excluded | Lunar infrastructure concept text; no retro-software artifact. |

## Programmatic observations

| Observation | Procedure or improvement | Boundary |
| --- | --- | --- |
| Twenty-two hits from three profiles were adjacent modern projects. | Use the existing `--max-per-profile 4` review view for variety when choosing a future *slice*; preserve the original queue and this fixed batch's order. | Profile membership and descriptions cannot automatically exclude siblings; the Cadaver loader was a worthwhile exception. |
| The Excel/VBA lab exposes analysis work primarily as an `.xlsm` workbook. | Preflight now lists `analysis_workbooks`, separate from binary game artifacts. | Presence of a workbook does not establish its purpose or correctness. |
| The KiCad repository contains both `README.de.md` and English `README.md`; other SDKs may have only `README.en.md`. | Preflight recognizes two-suffix README names and prefers the plain or English README. | English preference is a read path choice, not evidence that translations agree. |
| The Datapoint repository's root looks hardware focused, while original OS assembly lives two levels down. | A future bounded manifest or one-level source-directory inventory could surface `Software/OS` and its own README. | Root filenames, language labels and inherited published listings do not prove a new disassembly. |
| Similar development nouns covered generic EEPROM programming, a target-specific RC2014 writer and a distinct C64 loader. | Screen exact URLs, read the target and implementation, then record the specific relationship to a prior project. | Keywords, forks and root language alone cannot decide scope or lineage. |

The four audits keep unverified builds, hardware behavior and runtime details open where applicable. The Apple II record's Gemini attribution is from its own HISTORY; published README claims and supplied artifacts were not independently exercised.
