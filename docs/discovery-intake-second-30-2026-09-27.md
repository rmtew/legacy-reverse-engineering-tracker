# Second automated discovery intake: next 30 leads

Reviewed the next 30 ranked entries in a fixed snapshot of `state/discovery-intake.json` on 2026-09-27, after the first batch and a subsequent intake run. Screened exact URLs first, read primary repository READMEs and root inventories, then inspected specific hardware, source and documentation directories when scope or provenance was unclear. This is a ranked sample, not a population estimate or a verified build audit.

**Result:** 20 project records, four retained review sources with three open tasks, and six exclusions. The open queue fell from 201 to 171 immediately after review. Each URL has a source record, evidence-linked outcome and conservative audit where promoted. Related original and derivative implementations remain independently visible when the derivative adds a distinct codebase or board integration.

| Rank | Candidate | Outcome | Evidence and scope |
| ---: | --- | --- | --- |
| 1 | ikari-pl/konCePCja | Project | CPC/Plus emulator with IPC debugger and flux media support. |
| 2 | Bread80/CPCForRC2014 | Project | Adapted CPC firmware for RC2014; assembler sources and ROM images. |
| 3 | markmoxon/elite-source-code-commodore-64 | Project | Documented *original* C64 source and reference-matching variant builds. |
| 4 | Bread80/Amstrad-CPC-Kicad-Symbols | Excluded | Hardware pinout symbols, no implemented software analysis. |
| 5 | Bread80/Arduino-Hosted-Z80-Disassembler | Project | Arduino Z80 opcode disassembler; no hardware interface included. |
| 6–7 | cadaver/oldschoolengine2 and oldschoolengine2-emscripten | Sources | Two versions of a game-specific C64 emulator; grouped in one execution-path audit task. |
| 8 | cyxx/infernal_js | Project | CPC disk/Z80/bytecode investigation and JavaScript reimplementation. |
| 9 | amigavision/TopazDouble | Excluded | Hand-made font; README says font format was not reverse engineered. |
| 10 | benbaker76/stspeech | Project | Atari ST speech binary study and portable C reconstruction. |
| 11 | frno7/psgplay | Project | Atari SNDH playback with trace, disassembly and reassembly support. |
| 12 | jbilander/SimpleDevice | Excluded | Driver example/template with generated disassembly; no standalone analysis tool. |
| 13 | mntmn/amiga2000-gfxcard | Project | Scoped to authored Picasso96-compatible Amiga driver derived from interface investigation; the repo also hosts new graphics hardware. |
| 14 | na103/ar3 | Excluded | Rebuilt cartridge hardware with ROM/GAL binaries; no debugger source reconstruction. |
| 15 | pararaum/amigaexamples | Source | Example code and useful external links; mine attributed research/tool links. |
| 16 | prb28/vscode-amiga-assembly | Project | Amiga cross-build, emulator debug and disassembly extension. |
| 17 | schlae/amiga-hddlw | Excluded | Reverse-engineered floppy adapter hardware and PAL logic, outside software/tooling records. |
| 18 | donnchawp/DolphinDOS2 | Project | C64 KERNAL assembly and modification; 1541 source and binary equality not established. |
| 19 | gyurco/MiSTery | Project | Original Atari ST/STE FPGA machine core based in part on recovered hardware documentation. |
| 20 | MiSTer-devel/AtariST_MiSTer | Project | Adapted MiSTery core with MiSTer top-level, video and peripheral integration. |
| 21 | AmstradGameDevChallenge/rpg-adventure | Excluded | Original CPC homebrew; its cited BASIC disassembly is a third-party reference. |
| 22 | benchmarko/CPCBasic | Project | Original JavaScript CPC BASIC compiler/runtime, still receiving bug fixes. |
| 23 | benchmarko/CPCBasicTS | Project | TypeScript continuation with independent feature development and import formats. |
| 24 | cormacj/AmstradCPCRomHacks | Project | CPC ROM command, string/XOR and accessory patch scripts. |
| 25 | cpcsdk/cpctools | Project | CPC media, snapshot and debugging/cross-development tools. |
| 26 | hww/Aleste520EX | Project | Scoped to `Documentation/VDP Emulator`: original/patched MSX2 Vampire Killer listings and Aleste VDP adaptation diffs. |
| 27 | markmoxon/elite-a-source-code-bbc-micro | Project | Documented original BBC source, modern build and reference checks. |
| 28 | markmoxon/elite-source-code-6502-second-processor | Project | Documented original BBC second-processor source and reference checks. |
| 29 | muckypaws/AmstradCPC | Source | Mixed period CPC archive; separate review of tools, game source and cracking work queued. |
| 30 | laullon/b2t80s | Project | Multi-system Z80/6502 emulator with debugger; README notes incomplete systems. |

## Programmatic findings

| Repeated pattern | Immediate technique | Boundary for research |
| --- | --- | --- |
| Root files distinguished ROM-only, schematics, source listings and build scripts quickly; `ReadMe.md`/`Readme.md` casing defeated fixed-path reads. | Added `tools/discovery_triage.py`, a read-only, ordered preflight capped at two GitHub API requests per repository. It reports root names, case-insensitive README intro and explicit root-only file signals. Verified against two live repositories in four requests. | Nested source may exist when no root `.s`/`.c` file does; filenames do not prove authorship, byte matching or qualification. |
| GitHub README search matched citations to another project's disassembly, alongside genuine work on the same platform. | Keep exact URL screening and store reviewed exclusions; use root inventory and README context before promotion. | A reference to code is not evidence that this repository authored the referenced work. |
| Two pairs were related by explicit README lineage: MiSTery/MiSTer and CPCBasic/CPCBasicTS. | Present README links and same-owner similar names together; compare the original and derivative root files and named capabilities. Both pairs keep separate records with explicit relationships and differences. | Shared ancestry alone does not settle whether the derivative has distinct code, targets or research; do not merge by name. |
| Three Elite repos state they restore original source discs and show checksum comparisons. | Search README and root names for `original-sources`, `reference-binaries`, build and verification files, then surface those passages. | Do not call original-source restoration a disassembly; byte-exact claims require explicit variant evidence. |
| Mixed archives and game-specific engines require component scope. | Keep sources and targeted tasks for archive subdirectories and engine execution paths. | A large archive is not one uniform project; emulation of one game is not automatically a source port. |

For subsequent reviews run `python tools/discovery_triage.py --limit 30 --output /tmp/discovery-triage.json` before deeper inspection. It does not mutate the queue or decide acceptance, and the root-only inventory is intentionally shallow. The saved search result origin and score remain available for every lead.
