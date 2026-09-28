# Eleventh discovery intake: next 30 leads

Reviewed a fixed snapshot of the next 30 ranked URLs. Screened against the local index, then checked primary GitHub metadata, README files, root files and selected author/fork commits. This pass follows the repository-root scope rule: hardware, software and documentation that form one project stay at the root.

**Result:** 20 distinct projects, one source with an open branch comparison, nine exclusions. All 30 reviewed URLs leave the queue; reconciliation also removed four older entries that had been covered by intervening catalogue work, leaving 45 queued URLs. The FS-UAE source is recorded and its follow-up is tracked separately. Five prior linked-review tasks are complete; a sixth was already promoted between batches.

| Rank | Lead | Outcome | Evidence and boundary |
| ---: | --- | --- | --- |
| 1 | OldSkoolCoder/OSKBasic | Project | C64 BASIC graphics extension; README describes 1985 program, while checked assembly header records a 2020 onward implementation. No binary equivalence claim. |
| 2 | OldSkoolCoder/OSKMon | Project | Common-code C64/VIC-20 assembler and disassembler monitor. |
| 3 | axewater/winuae | Project | Direct child of tracked BartmanAbyss/WinUAE; parent comparison isolates one 94-line GDB server change for screenshot/disassembly monitor commands. Credit Bartman and tonioni. |
| 4 | davidgiven/fluxengine | Project | Cohesive flux hardware and Java imaging client; Amiga, Macintosh and other floppy formats. README dates a Java client rewrite to September 2026. |
| 5 | jfdelnero/Pauline | Project | FPGA floppy dumper, drive emulator and Linux control software in one repository; HxC is a credited submodule. |
| 6 | keirf/greaseweazle | Project | Original Greaseweazle host tools, distinct from tracked GreaseGUI derivative; firmware linked separately. |
| 7 | lipro-cpm4l/libdsk | Project | Unofficial continuation of John Elliott’s floppy image library; README credits original authors and additional formats. |
| 8 | maxim-zhao/sega8bitheaderreader | Project | Sega/Codemasters/SDSC ROM header inspection, without disassembly claim. |
| 9 | opencbm/opencbm | Project | Commodore IEC host drivers and disk-copy tools, one coherent suite. |
| 10 | simonowen/samdisk | Project | Copy-protected PC floppy imaging; upstream says v4 rewrite remains incomplete. |
| 11 | bartmanabyss/binutils-gdb | Project | Amiga-specific GNU debugger fork: checked author commits for m68k syntax, branch info and section offsets. Broad upstream changes are not credited to fork author. |
| 12 | bartmanabyss/elf2hunk | Project | Separate ELF-to-Amiga Hunk converter, including 68k relocation fixes in history. |
| 13 | bartmanabyss/shrinkler | Project | Seven commits ahead of the original Shrinkler: JSON compression statistics, relocation and symbol-hunk fixes, progress and VS build changes. |
| 14 | bebbo/amiga-gcc | Excluded | Linked GitHub repository returns 404. Existing tracked AmigaPorts GCC continuation credits bebbo; no new content verified. |
| 15 | davidcanadas/vasm-m68k-mot-win32 | Project | Unofficial vasm mirror with m68k section-name changes for Amiga debugging; original vasm credited. |
| 16 | grahambates/fs-uae | Source + task | Default branch has upstream-authored FS-UAE content; two `remote_debugger_*` branches need branch-specific comparison before assigning an independent derivative record. |
| 17–20 | libexpat/libexpat; marus/cortex-debug; microsoft/vscode-js-profile-visualizer; preactjs/preact-devtools | Excluded | General XML, Cortex-M, JavaScript-profile and Preact editor dependencies; no reviewed legacy-computer work. |
| 21 | z00m128/sjasmplus | Project | SourceForge-derived Z80 assembler with Spectrum/CPC output modes and scripting. |
| 22 | hansbonini/sega2asm | Project | Mega Drive ROM splitter with 68000/Z80 disassembly and asset extraction; credits predecessor algorithms and tools. |
| 23 | floooh/easmx | Project | ASMX fork adapted as embeddable/WASI assembler for KC IDE, with map and include-root outputs. |
| 24 | OldSkoolCoder/CIDOS | Project | C64 and 1541/SD2IEC assembly disk-command extension. |
| 25 | OldSkoolCoder/PET-Frogger | Project | Author’s recovered school-era PET 6502 source and PRG; original source, not a binary-derived reconstruction. |
| 26 | 0xC0DE6502/max65-releases | Project | Documented BBC/Electron 65xx cross assembler distributed as a binary release; public implementation source was not established. |
| 27–30 | albank1/albank1; Arduino-Network-Tester; Extract-encapsulated-PDF-from-DICOM-and-save-file; Python-DICOM-tools | Excluded | Personal profile, unrelated electronics and medical-imaging scripts. |

## Programmatic observations

| Observation | Applied or proposed procedure | Limit |
| --- | --- | --- |
| A single linked tool README supplied seven disk dependencies, and an Amiga debugger README supplied ten more links, four of them ordinary editor/runtime dependencies. | Added optional `--max-per-source N` review display cap. It selects other origins after the cap and fills remaining slots in rank order; queue contents and default rank order remain unchanged. Screen all links locally before fetching metadata. | A dependency link is context, not qualification or authorship. The cap is an optional view and must not silently drop projects. |
| Fork metadata alone concealed both a small genuine GDB change and copied upstream READMEs. | Use parent metadata plus a bounded compare summary and author-commit inspection. An ahead count, changed path and commit subject help route deeper review. | A huge upstream merge can swamp comparison; branch/ref selection and authorship require human review. |
| FS-UAE’s default branch did not demonstrate the named remote debugger while two branch names suggest it exists. | Queue branch-specific comparison of `remote_debugger_barto` and `remote_debugger_prb28`; retain as a source until an implementation is checked. | A branch name is a review hint, not proof of a working debugger. |
| Release-only max65 has substantive documentation but no verified source; original PET Frogger source has a different provenance than disassembly. | Separate distribution, source and provenance fields in records; leave builds, byte identity and CPU minima unresolved when untested. | Repository language and build files alone do not establish a runnable historical target. |

No new project was independently compiled or exercised. CPU and runtime audit notes indicate the evidence inspected, not measured compatibility.
