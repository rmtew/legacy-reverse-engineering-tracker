# Fourth automated discovery intake: next 30 leads

Reviewed a fixed snapshot of the next 30 ranked open URLs on 2026-09-27. Screened against known URLs, inspected repository roots and primary READMEs, and checked the two Acorn Electron source examples. This is a discovery pass, not a build or byte-comparison audit.

**Result:** 16 distinct project records, one retained collection with a targeted follow-up task, and 13 exclusions. Every reviewed URL has a source record and leaves the open queue.

| Rank | Candidate | Outcome | Evidence and scope |
| ---: | --- | --- | --- |
| 1 | davidrg/ckwin | Excluded | Kermit 95 application source; no specific recovery/development analysis. |
| 2 | ksherlock/ample | Project | Apple II/Mac MAME front end with custom emulator build. |
| 3 | libretro/virtualjaguar-libretro | Project | Atari Jaguar/CD emulator with documented hardware tests. |
| 4 | MarcoPon/SeqBox | Excluded | Generic resilient archive; incidental Amiga search hit. |
| 5 | RetroReversing/retroReversing | Source | Curated RE articles and tool links; follow specific outbound projects. |
| 6 | Sakura-IT/SonnetAmiga | Project | WarpOS API/ABI reimplementation for Amiga PPC cards; CVS mirror. |
| 7 | adtools/clib2 | Project | Amiga-specific C runtime and headers for GNU C development. |
| 8 | EmberHeavyIndustries/HID2AMI | Excluded | HID hardware adapter and firmware. |
| 9 | MW0MWZ/AmiTCP_NG | Project | AmiTCP-derived 68k stack plus independent Roadshow SDK ABI implementation. |
| 10 | thomas-luebker/amimcp | Project | MCP remote shell/files/GUI agent for real Amiga; runtime evidence in README. |
| 11 | ytmytm/c64-GEOS2000 | Project | C64 GEOS KERNAL disassembly and modified buildable source; Amiga search hit was incidental. |
| 12 | cyxx/bermuda | Project | Bermuda Syndrome engine rewritten from original Windows executable. |
| 13 | cyxx/f2bgl | Project | Fade to Black engine reimplementation using original PC files. |
| 14 | cyxx/linyaga | Project | Partial Yaga engine wrapper using original game executable/data. |
| 15 | mandraga/upernes | Project | NES 6502 to SNES 65C816 analysis/recompiler; manual indirect-target step. |
| 16 | rejunity/z80-open-silicon | Excluded | Hardware Z80 silicon clone. |
| 17 | TobyLobster/multiply_test | Project | Reproducible cycle and memory tests of 120+ credited 6502 routines. |
| 18 | angree/sf2000-basilisk-ii-macintosh-emulator | Project | Distinct Basilisk II Macintosh emulator port to SF2000/GB300. |
| 19–23 | 0xC0DE6502/electrobots-going-underground-releases, electrobots-releases, elementum-releases, flappy-bird-releases, lode-runner-2021-releases | Excluded | Playable Electron/BBC game release packages; no independently documented recovered source or tooling. |
| 24 | 0xC0DE6502/machine-auto-detect-releases | Project | Distributed Electron real-machine/emulator timing-detection routine and assembly example. |
| 25 | 0xC0DE6502/manic-miner-2021-releases | Excluded | Electron game images derived from credited BBC game, no authored analysis here. |
| 26 | 0xC0DE6502/max65-syntax-highlighting-releases | Project | Distributed VS Code assembly syntax extension, even though source is not shown here. |
| 27 | 0xC0DE6502/meteors-enhanced-releases | Excluded | Playable enhanced game image only. |
| 28–29 | 0xC0DE6502/python-releases, soko-ban-releases | Excluded | Playable game packages; Python is the game title, not the language interpreter. |
| 30 | 0xC0DE6502/speed-tricks-releases | Project | Annotated BASIC/6502 source measuring Electron display and MOS timing techniques. |

## Programmatic observations

| Observed pattern | Applied or proposed procedure | Boundary |
| --- | --- | --- |
| Eleven GitHub code-search hits included SeqBox, GEOS and Jaguar, whose titles/descriptions do not identify the queried Amiga or Atari ST platform. | Ranking now rewards code-search hits with an independently described platform match and demotes mismatches, retaining every URL for review. | README/code evidence can still establish relevance despite a mismatch. |
| Twelve `-releases` repos appeared consecutively from one profile; three offered developer tools or annotated source. | Preflight now lists `.ssd`, `.uef`, `.exe`, `.vsix` artifacts and recognizes `.6502` source. Use `--max-per-profile 4` for a varied review slice. | Release suffix and root inventory never decide qualification. |
| The two game-engine rewrites say they were derived from original executables; the Yaga wrapper documents data/executable use without the same lineage claim. | Capture source-versus-target platform and explicit provenance at intake, then audit build and predecessor details later. | A README alone does not establish binary equality or recovered code coverage. |
| `AmiTCP_NG` explicitly separates inherited AmiTCP code from independent Roadshow SDK ABI implementation. | Record both lineage and the distinct API work in one project, without labelling it a Roadshow disassembly. | Fork metadata cannot supply the actual divergence description. |

The top 30 is a ranked slice; these proportions do not estimate yield across the entire queue. All new project audits leave unverified build, AI authorship and runtime claims open. A later targeted inspection of RetroReversing links should screen exact URLs before fetching files.
