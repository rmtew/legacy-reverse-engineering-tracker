# Tenth discovery intake: next 30 leads

Reviewed the fixed next 30 ranked URLs on 2026-09-28. Existing project coverage was screened locally; repository metadata, READMEs, source paths and lineage statements were checked for the selected scope. Upstream build and byte-identity claims were not independently tested.

**Result:** 13 distinct projects, two reference sources, two distribution duplicates, 13 exclusions. All 30 reviewed URLs left the saved queue; six linked projects entered follow-up. The previous Tempest 2000 follow-up task is complete.

| Rank | Candidate | Outcome | Evidence and scope |
| ---: | --- | --- | --- |
| 1 | WacKEDmaN/CPCSyntaxError | Project | CPC/Plus/GX4000 Windows emulator with Z80, model-specific CRTC and Gate Array, debugger and assembler; hardware/test compatibility claims remain upstream. |
| 2 | Jondalar/homebrew-ue2emu | Duplicate | Homebrew formula distributes the UE2 binaries at rank 3. |
| 3 | Jondalar/UE2-C64U-Emulator | Project | Runs C64 Ultimate firmware application unmodified while modeling board I/O, delegates C64 to tracked TRX64 and exposes MCP test control; FPGA part does not execute. |
| 4 | Jondalar/homebrew-trx64 | Duplicate | Homebrew formula installs the already tracked TRX64 runtime. |
| 5 | mwenge/tempest2k | Project | Jeff Minter's **original** Jaguar assembler source, modern build files, and upstream byte-identical cartridge claim. No independent build or match test. |
| 6–10 | Jondalar/CCVoiceOverHelpers; imapfilter-icloud-hey-screener; mailscreener; robotv-vdr-headless; VDR_Zapper_Reloaded | Excluded | iOS accessibility, modern email and television software from the same profile. |
| 11 | Jondalar/vice-cartconv | Project | VICE cartconv adaptation that extracts individual CRT banks; VICE authors remain credited. |
| 12 | OldSkoolCoder/Tutorials | Source | C64/PET 6502 tutorial code and a link index. Four separate source/tool leads entered follow-up. |
| 13 | richgel999/miniz | Excluded | General Deflate library reached through a dependency link. |
| 14 | s-macke/SAM | Project | C adaptation of the C64 Software Automatic Mouth speech engine and reciter, with WAV/SDL output; no original binary rebuild claim. |
| 15 | segrax/DrCreep | Project | C++ Castles of Dr. Creep reimplementation explicitly based on reverse engineering C64 6502 object code; uses user-provided D64 data. |
| 16–17 | tree-sitter/tree-sitter; Zeyad-Azima/Offensive-Resources | Excluded | General parser framework and offensive-security directory; no specific historical software work demonstrated. |
| 18 | floooh/vscode-kcide | Project | CPC/C64/KC85 VS Code assembler IDE with embedded debugging, disassembly and emulators. Its ASMX-derived assembler is a follow-up lead. |
| 19 | ivop/bbc-basic | Project | Annotated BBC BASIC II/III 6502 listing with BBC, Atom, System and C64 build variants. Credits Harston's source reconstruction and Ivo's conversion/fixes; distinct from the tracked Acornaeology listing. |
| 20 | markmoxon/elite-compendium-bbc-master | Project | BBC Master Elite disc integration, menu and DSD/SSD build around branch-pinned program submodules; individual Elite versions remain separately represented. |
| 21 | oisee/antique-toy | Source | ZX Spectrum/Z80 technique book and examples. README discloses LLM assistance; descriptions are reference leads, not independently verified hardware claims. |
| 22 | AmiBlitz/AmiBlitz3 | Project | Native Amiga compiler and IDE with source, libraries and examples. README states the **IDE** requires 68020 and 8 MB; compiled programs have separate requirements. |
| 23 | ifilot/greaseweazle | Project | GreaseGUI Qt application for Greaseweazle disk imaging, including Amiga ADF and Atari ST, with distinct GUI source; original Keir Fraser hardware and firmware credited. |
| 24 | johnjoeallen/bascal | Project | Structured BASIC compiler emitting classic BASIC, C and JVM code. |
| 25–26 | KermitProject/ckermit; OpenKermit/ckermit | Excluded | Portable Unix/VMS communications software; the newer version is a continuation, but neither review established focused historical-software recovery scope. |
| 27–29 | ravikiranj/twitter-sentiment-analyzer; sergev/LiteBSD; wireshark/wireshark | Excluded | Twitter API scripts, PIC32MZ OS and general network analyzer surfaced by broad code searches. |
| 30 | asahala/Bitcrush | Project | Python C64/Amiga/PC screenmode image effects. The output is retro **lookalike** imagery; no native machine graphics or recovered assets claimed. |

## Programmatic observations

| Finding | Applied or next procedure | Limit |
| --- | --- | --- |
| README indexes mix many tracked, reviewed and new links. The Elite Compendium names 31 related repositories; 29 belong to Mark Moxon, of which nine are tracked projects, five reviewed decisions, four known repositories, one known source and ten still new. | The bounded preflight now screens **all** README and landing-page repository links against the local index and returns status counts plus up to 20 new roots, even when a display list clips at 20. No extra GitHub requests. | A local `new` result means unseen URL, not a qualified project; queued status is separate from catalogue coverage. |
| Two Homebrew taps are package aliases for actual emulator repositories. | Screen README links against known projects before an additional source review and record duplicate decisions linked to the original project. | Packaging can be independently interesting, but these formulae install the same executables. |
| One GitHub profile yielded several unrelated mail and TV repositories amid C64 emulators. | Use the existing per-profile display cap for varied passes and README/metadata scope checks before opening code. | A repository description is triage evidence only; do not hard-exclude on query mismatch. |
| Tempest original source, Dr. Creep object-code reimplementation and BBC BASIC derivative listings have different provenance. | Preserve source type and predecessor credits in distinct records and audit areas. | Upstream byte identity, emulator behavior and ROM matching still require independent tests. |
| The AmiBlitz README separates minimum IDE CPU from generated-program requirements. | Record m68020 as the IDE's minimum and leave compiled-output CPU requirements open. | Platform name alone cannot establish a minimum runnable CPU. |

Six linked follow-ups are queued: PET Frogger, CIDOS, OSKMon, OSKBasic, the ASMX-derived assembler, and the BBC Micro Elite Compendium. None of the 13 promoted projects was independently built or exercised.

