# Third automated discovery intake: next 30 leads

Reviewed a fixed snapshot of the next 30 ranked open URLs on 2026-09-27. Screened their URLs, inspected primary READMEs and root inventories, and followed project-specific documentation and source directories where a root README was absent or the repository mixed subjects. This is a scoped evidence pass rather than a build or runtime test.

**Result:** 17 project records from 16 URLs, five retained sources with three targeted tasks, and nine exclusions. The PROBOS repository has two independently described outputs, so 30 URLs produce 31 distinct outcomes/records. Each promoted project has a conservative audit, and every reviewed URL leaves the open queue.

| Rank | Candidate | Outcome | Evidence and scope |
| ---: | --- | --- | --- |
| 1 | albank1/ZX-spectrum-512K-cartridge-Jose-Leandro | Project | Authored Python ROM/menu utilities, with original cartridge/ROM credit preserved. |
| 2 | angree/Amiga-68K-BobrHopper | Excluded | Native port of author's recent game; no historical binary analysis. |
| 3 | angree/openttd_amiga_68k | Excluded | Substantial Amiga port of available OpenTTD source, outside recovery scope. |
| 4 | ataribaby42/probos2000 | Two projects | C64 PRG analysis to native Spectrum 48K TAP; separate direct JavaScript reimplementation of the Spectrum version. |
| 5 | Bread80/Couch-To-64k---Breadboard-Z80-Computer | Excluded | New breadboard computer/tutorial. |
| 6 | Bread80/CPC_Keyboards | Excluded | Keyboard hardware designs. |
| 7 | Bread80/CPC_ZERO | Excluded | Hypothetical new 6502 CPC-like hardware. |
| 8 | Bread80/CPCModular | Excluded | CPC-compatible hardware modules and test snippets. |
| 9 | Bread80/GreenHAL | Excluded | Untested HAL/PAL replacement hardware, despite behavior-test notes. |
| 10 | Bread80/Quiche | Project | Pascal-like Z80 cross compiler, explicitly early work in progress. |
| 11 | Bread80/Soft968-Amstrad-Firmware-Manual | Source | Hyperlinked CPC firmware reference for specific ROM audits. |
| 12 | Bread80/z80-character-lcd | Excluded | Z80 LCD hardware tutorial and test code. |
| 13 | cadaver/c64gameframework | Project | Reusable C64 game engine, sprite and build tooling. |
| 14 | cadaver/cadaver.github.io | Source | Author website and hosted tool releases; compare with GitHub sources. |
| 15 | cadaver/hessian | Source | Original game source to check against game-specific emulator support. |
| 16–17 | cadaver/miniplayer, miniplayer2 | Two projects | Distinct music-player implementations; v2 README details effects, hard restart and performance changes. |
| 18 | cadaver/mw4 | Source | Original Metal Warrior 4 code to scope the game-specific emulator lineage. |
| 19–20 | cadaver/siddump, sidid | Two projects | SID execution/profile dump and signature-based playroutine identification. |
| 21 | cadaver/steelranger-demo | Source | Original demo source for the specific emulator audit. |
| 22 | 0xC0DE6502/CHIP-8-releases | Excluded | Binary-only Electron CHIP-8 consumer emulator without developer analysis function shown. |
| 23 | TheJare/stardust-48k | Project | Spectrum snapshot-based partial reconstruction; README says not yet fully reassemblable. |
| 24 | ultrabolido/abadia | Project | Distinct Web game implementation using CPC assets and credited prior disassembly. |
| 25 | rolandshacks/vs64 | Project | C64 IDE, emulation and debugger; Atari ST search origin was incidental. |
| 26 | travisgoodspeed/goodasm | Project | Retargetable assembler/disassembler with 6502 and Game Boy support. |
| 27 | unbibium/dcpu-cbmbasic | Project | BASIC/KERNAL translation from C64 disassemblies to DCPU-16. |
| 28 | dhansel/smon6502 | Project | Adapted 1984 C64 monitor for homebrew 6502, with assembler/debugger. |
| 29 | KallDrexx/Dotnet6502 | Project | JIT decompiler of 6502 to .NET IL; different architecture from highbyte/dotnet-6502. |
| 30 | chelsea6502/BeebEater | Project | BBC BASIC port from credited ROM disassemblies to 6502 breadboard computer. |

## Programmatic observations

| Observation | Improvement | Limit |
| --- | --- | --- |
| Profile mining supplied **22 of 30** leads, including nine Cadaver and eight Bread80 siblings; six Bread80 hardware leads were outside software scope. | `discovery_intake.py --list 30 --max-per-profile 4` now offers a diversified review slice. It caps siblings in the displayed first pass, fills spare slots from them, and leaves the stored ranking untouched. A deterministic test checks cap, fill and nonmutation. | Diversification changes review order, never inclusion; some authors have several genuinely distinct tools. |
| A root-only inventory saw directories in `probos2000` but no root README; the distinct native and Web work was under `PROBOS_48K/` and `PROBOS_WEB/`. | A future bounded one-level README inventory for no-root-README or multi-component repositories would expose candidate project paths. | Directory names alone do not prove independent work; inspect README and implementation before splitting. |
| `miniplayer`/`miniplayer2` share lineage, while `KallDrexx/Dotnet6502` and `highbyte/dotnet-6502` only share a descriptive name. | Surface similar repo names and README predecessor links to reviewers, then compare architecture and supported behavior. | Neither name similarity nor a fork relationship is an automatic duplicate. |
| Search queries returned relevant tools on the wrong platform: VS64 from an Atari ST query, Stardust from a CPC query. | Preserve the title/description platform ranking adjustment; inspect actual source/binary platform before writing catalogue fields. | A mismatch lowers priority but must not discard a cross-platform or poorly described project. |
| Source repositories for Hessian, MW4 and Steel Ranger give direct evidence for last batch's game-specific emulator audit. | One targeted task links these three originals to the prior engine-review task rather than adding three unsupported reverse-engineering records. | Original game source is valuable evidence but does not imply the engine runs every version of the game. |

The next programmatic preflight should retain a strict request budget while adding optional one-level README discovery. No automated signal here establishes runtime, binary equality, or whether source is original versus reconstructed.
