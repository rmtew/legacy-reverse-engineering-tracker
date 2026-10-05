# Search / Report Log

## 2026-10-05 — GitHub pagination and platform-alias batch

Added **51 source-reviewed projects**, increasing the catalogue from 1,269 to **1,320**. The bounded follow-on pass used 53 GitHub search calls, including eight page-two continuations and spelling/term variants, plus direct author/source links. Result lists contain 1,581 unique roots; 58 selected roots received primary review and exactly the approved 51 were promoted. Sixteen pages still hit the 100-result cap.

Highlights include SWIV-Native, two independent Dungeon Master reimplementations, C64 Defender, VIC-20 JETPAC, Air/Sea Attack CVBasic, SG-1000/SC-3000 Akalabeth and Softporn Adventure, CPC Booty/Nibbler/Transversion, and ChipWits original-source restoration. Tools, native homebrew, demos and generic emulators remain distinctly typed. Retired c64m and predecessor SIDBlaster URLs alias the approved current projects without adding duplicates.

All 51 have complete eight-area research audits. Primary source/build/release evidence supports bounded flags; incomplete/non-buildable projects, original-asset requirements, rights caveats and uncertain hardware remain explicit. No candidate compilation/playtest, byte-exact verification, application/workflow edit or unreviewed-lead promotion was performed.

See [the complete review and exact query coverage](docs/github-pagination-aliases-51-2026-10-05.md). Existing metadata and Pages workflows generate catalogue Activity and RSS.

## 2026-10-05 — Platform-matrix and curated-remake batch

Added **65 source-reviewed projects**, taking the catalogue from 1,204 to **1,269**. The approved batch includes 64 unique GitHub roots and F.L’s Barbarian author-site remake family. Three old RustyPixelsUK URLs are preserved as canonical redirect aliases, without adding projects. All new records have complete eight-area research audits and primary evidence.

Discovery combined a bounded 78-query platform/term GitHub matrix with creator/competition sources and the user-supplied Awesome Game Remakes list. The list yielded twenty primary-reviewed additions; unmatched search/list links remain unqualified. New projects include OpenFodder, OpenDUNE (including Atari builds), freeserf.net, Lionheart Remake, Geneva, NeoDesk, AWeb, CPC RetroDev source releases, Yawi, Notator Online and partial Midwinter/Neuromancer/Dork’s Dilemma reconstructions.

Buildability, runtime compatibility, original-source CPU and AI claims remain evidence-scoped. No independent candidate build/play test was performed; incomplete gameplay, missing build/assets, data-only equivalence and platform-specific limitations are retained. No code/workflow changes or unrelated old-exclusion reconsideration is included.

See [the full review](docs/platform-matrix-remakes-65-2026-10-05.md). Existing refresh and Pages workflows generate catalogue addition activity and RSS.

## 2026-10-05 — Big retro-development discovery batch

Reviewed 47 new candidates from fresh, locally deduplicated platform searches and four explicit project leads. Added **44 projects**, taking the catalogue from 1,160 to **1,204**; recorded **one retired-predecessor duplicate**, **two exclusions**, and **zero deferrals**.

The explicit leads are **Black Tiger MD**, **Side Arms MD**, **volamos** and **Raptor: Call of the Shadows for Amiga**. New coverage also includes native **Lotus Turbo Challenge 2** and **Platoon** reconstructions, **ScummST**, Amiga porting/runtime libraries, **Test Drive I–III**, **Street Rod**, **Aces of the Pacific**, **Batty for DOS**, **FROGMAN**, **The Shaft**, **Desolate**, **TrailBlazer**, and Lynx development/recompilation projects.

Every addition has identity/classification, CPU, build/runtime, AI and relationship audits. Browser output is not assigned a hardware CPU; native game paths are distinguished from general emulators and separate differential oracles. Chip's Challenge/Crystal Mines II Lynx reference ports are runnable experiments with unfinished input, not playable games. FROGMAN's code-region equality and other frame/asset comparisons are not generalized to whole-release byte identity. Build/playability claims retain their upstream scope; no independent game build or play test was performed.

See [the complete review](docs/big-retro-development-batch-2026-10-05.md). Existing metadata/activity and Pages/RSS workflows generate public addition events after publication.

## 2026-10-05 — Final CPU queue item and explicit AI evidence

Resolved the last queued CPU audit for **IRA — Amiga 68k reassembler**. Primary maintainer documentation establishes 68000/010/020/030/040/060 input coverage, portable build routes and a source-regeneration/binary-comparison workflow; its assembler-text output makes target CPU not applicable, while exact host CPU and RAM minima remain unasserted.

The upstream lane reviewed **Copperline — Amiga emulator & reverse debugger** and **Gearlynx — Atari Lynx emulator and MCP debugger**. Copperline now records capability-gated WASM resource writes, persistent write-through tests, public Bartman-extension lineage and explicit Codex attribution. Gearlynx now records Timer 2 VBlank profiling and missed-VBlank trace events. Ten stale AI audit states were reconciled with explicit repository instructions or co-author evidence already present in project records.


## 2026-10-05 — Oric/Lynx/DOS discovery and target-CPU audit

Rotated fresh discovery through exact FM Towns, Oric/Atmos and Atari Lynx searches. Added **Oric Explorer — media browser and 6502 analysis tool**, **OSDK — Oric cross-development system**, **Blake's 7 — original Oric fan adventure**, **Gearlynx — Atari Lynx emulator and MCP debugger**, **Super Mario Bros. — RE-derived native Atari Lynx port**, **ALYNXDJ — original Atari Lynx music tracker**, **Ultima V — u5d decompilation and playable reconstruction**, and **Stunts 1.1 — restunts2 executable reconstruction**. The records distinguish OSDK's official-project identity from its Git mirror, and keep Blake's 7 and ALYNXDJ explicitly classified as original fan/homebrew work rather than reverse-engineered derivatives.

The independent CPU lane resolved ten queued target areas. Primary READMEs, assembler source and build scripts establish ARM2/ARM250, 6502 and m68000/m68020 outputs where explicit. **dis68k**, **Ghidra Amiga hunks loader** and **MEGA65 I/O symbol generator** are target-CPU not applicable because they produce text, analysis state or symbol definitions rather than runnable CPU-native output. No hardware minimum was inferred from platform or source language.


## 2026-10-04 — MSX/BBC/Amiga output audit and active toolchain review

Resolved ten queued target-CPU areas with primary READMEs, repository trees and build scripts. **Stardust MSX annotated tape reconstruction** now records its verified Z80 reassembly output; **MNT VA2000 — reverse-engineered Picasso96 driver** records the driver's explicit `-m68020` build; **AmigaAsm** records m68000 assembly export; and **vasm m68k MOT — Amiga debugging variant** records its documented 68000-family selectors. **Archie-FACE — Archimedes C demo environment** now explicitly records that its primary build files do not name a specific ARM CPU output. Analysis archives, host tools and unsupported listings are `not-applicable` or `no-evidence-found` rather than inheriting CPUs from platform labels.

The upstream lane reviewed **IK+ — Atari ST compatibility and three-player patches**, **lxa — Linux Amiga executable runtime**, **Amy Studio — browser-based ColecoVision development environment** and **Dotnet6502 — 6502 JIT decompiler to .NET MSIL**. The records now preserve IK+ version 7's exact input/build/runtime bounds, lxa's AmigaOS 3.1 probe corrections, Amy Studio's gasm80-compatible assembler and Coleco ADAM support, and Dotnet6502's documented runnable JIT paths without inventing unstated host minima.


## 2026-10-04 — Apollo/BBC/Z80 output audit and active upstream review

Resolved twelve queued target-CPU areas using primary READMEs, makefiles, assembly sources and verification scripts. Explicit outputs now cover **MasterVamp**, **PackFire**, **PtvPack**, **Plan B BBC disassembly**, **qr128**, **QTM v1.49b**, **sjasmplus**, **ZX Spectrum 48K ROM** and **Star Raiders Atari 8-bit source analysis**. **Peasauce**, **Planetoid BBC disassembly** and **Sim City Spectrum Z80 disassembly** are explicitly target-CPU not applicable. No hardware minimum was inferred from a platform or instruction set.

The upstream lane reviewed **Firestaff — Dungeon Master / Chaos Strikes Back engine reconstruction**, **Copperline — Amiga emulator & reverse debugger**, **lxa — Linux Amiga executable runtime**, **Rolling Thunder — Amiga 68k translation**, **C64RE — MCP-assisted C64 software analysis workbench** and **TRX64 — C64 reverse-debugging emulator/runtime**. Records preserve the exact boundaries of the new evidence rather than promoting bounded tests to complete compatibility.


## 2026-10-04 — Saturn, Apple IIgs and MSX discovery plus target-CPU audit

Reviewed saved NES, arcade, Atari ST, C64 and Amiga leads and rotated fresh searches through Sega Saturn, Apple IIgs and MSX code results. Added **Ultima III: Exodus — NES disassembly**, **Star Wars arcade — audio firmware disassembly**, **Matrix — Atari ST source reconstruction**, **RetroIO — 8-bit disk and tape image inspector**, **Ghidra Sega Saturn Loader**, **Panzer Dragoon Saga — SH-2 reverse-engineering corpus**, **ApplEm — Apple II/IIgs emulator and debugger**, **MSXDAW — byte-exact MSX disassembly workbench**, **Vampire Killer — byte-exact MSX2 disassembly**, **King's Valley II — byte-exact MSX2 disassembly**, **Booga-Boo — byte-checked MSX1 disassembly**, **Zanac — MSX clean-room AI reconstruction and disassembly**, and **Metal Gear — MSX2 disassembly-derived browser port**.

The same review records six non-promotions rather than leaving them to be rediscovered: three small C64 charity-competition games fall below the substantial-homebrew threshold, **erings** explicitly disclaims a game-development-tool role, **Duke68k** still lacks primary provenance/build documentation, and the **MazeOfGalious** repository was unavailable.

The independent CPU lane resolved eight queued target-CPU areas. Primary source establishes 68000–68060 outputs for **m68k assembler/disassembler — Amiga Hunk aware**, m68000 for **M68k Reversing Toolkit — generated Amiga analysis**, 6502/65C02 for **max65 — Acorn 65xx assembler**, 45GS02 for **m65dbg — MEGA65 remote debugger**, Z80 for **Wanted: Monty Mole — Spectrum disassembly**, and 6502 for **OSKBasic — C64 graphics BASIC extension** and **OSKMon — C64 and VIC-20 machine-code monitor**. **MegaPET — Commodore PET/SuperPET core on MEGA65** is explicitly target-CPU not applicable because its output is an FPGA core. No runtime minimum was inferred from those output architectures.


## 2026-10-03 — Spectrum/BBC target CPUs, Firestaff and Moonstone

Resolved ten queued target-CPU areas with primary READMEs, repository trees and build files. **Exolon Spectrum disassembly**, **Head Over Heels Spectrum annotated reconstruction**, **The Hobbit Spectrum v1.0 annotated disassembly**, **Hunchback Spectrum disassembly** and **Lode Runner Spectrum reconstructed source** now record explicit Z80 native outputs; **image2mode1 — BBC raster palette converter** records its 6502 display-engine output. Four analysis or binary-only projects are explicitly target-CPU not applicable rather than receiving architectures inferred from their platform.

The upstream-change lane reviewed **Firestaff — Dungeon Master / Chaos Strikes Back engine reconstruction** and **Moonstone — Amiga game-specific Windows adaptation**. Firestaff v3.0.358 now records its bounded authenticated Atari ST sound queue, persisted-root handoff for three original-media editions and retail JP Theron Akutuba capture while retaining the stated audio, gameplay and save-restoration limits. Moonstone now reflects the published v1.4.0 local multiplayer release, the tested but unreleased v1.4.1 fullscreen commit, and explicit Codex attribution. No new hardware minimum was inferred.


## 2026-10-03 — Mixed-output CPU audit and Elite over Econet RTC review

Resolved thirteen CPU audit areas across twelve queued projects. **Chronos — Spectrum beeper engine disassembly** and **Chuckie Egg Spectrum SkoolKit disassembly** now record explicit Z80 build outputs; **CIDOS — Commodore disk BASIC commands** records its checked 6502 PRG build; and **easmx — embeddable ASMX fork** records its implemented multi-CPU output families while marking an original source CPU not applicable.

Pure listing/analysis projects are explicitly target-CPU not applicable, and mixed C64 type-ins plus binary-only Electron releases retain no-evidence-found rather than receiving CPUs inferred from their platforms. The same primary review corrects **CDTV U75 controller ROM disassembly** to record its explicit Claude-assisted emulator harness and final code review. The upstream-change lane also updated **Elite over Econet — network-loading & multiplayer scoreboard modification** for its 6502 assembled outputs and new selectable Acorn Econet RTC !BOOT build path. No unstated CPU, RAM or minimum-hardware requirement was added.

## 2026-10-03 — RetroRE residuals, rotated discovery and target-CPU audit

Reviewed the remaining RetroRE Zelda lead and rotated fresh searches across Atari Lynx, TRS-80/CP/M and Apple Lisa routes. Added **MBASIC 5.21 — byte-identical CP/M source reconstruction**, **sdltrs-MultiHDC — TRS-80 hard-disk archaeology emulator**, **Apple Lisa — MiSTer FPGA core**, **romdev — multi-platform ROM development and analysis environment**, and **The Legend of Zelda — early NES WIP disassembly**. The records preserve the distinction between reconstructed historical software, original development tooling, hardware emulation and an incomplete independent disassembly.

The separate CPU lane resolved ten queued target-CPU areas. Primary build/source evidence establishes 6502 outputs for **ANFS 4.18 bare disassembly**, **Arkos Tracker players for BBC Micro**, **Attack on Alpha Centauri BBC disassembly** and **Boulder Dash BBC disassembly**; ARM for **ArchieKlang — Archimedes synth port**; Z80 for **Bandersnatch Spectrum code disassembly**; and m68000 compatibility for **Shrinkler — Amiga executable compressor**. **Audio Sculpture 1.5 — IPL protection analysis** and **C64 character ROM glyph listing** are explicitly not CPU-targeted outputs, while **elf2hunk — ELF to Amiga Hunk converter** records no fixed host CPU. Only the documented stock BBC Model B and all-Amiga-CPU runtime statements were added; unstated RAM floors remain unknown.


## 2026-10-02 — Native ROMs, browser outputs and Firestaff original-media review

Resolved ten queued target-CPU areas. **Epyx Fastload cartridge load routines** and **EXMON II BBC/Electron annotated ROM update** now record explicit 6502 native outputs; **Globe — 6502 demo translated to ARM** now correctly separates its original 6502 source from its ARM port output. **Exile BBC 6502-to-C++ study port** records only its explicitly configured x86-64 Visual Studio output, while **OpenCaptive** records its published x86-64 and arm64 package architectures. Browser JavaScript outputs and music/data-analysis tools are explicitly target-CPU not applicable; no host architecture was inferred from their language or platform.

The upstream-change lane reviewed **Firestaff — Dungeon Master / Chaos Strikes Back engine reconstruction**. Its PC 3.4 route now defeats the first original-media group and traverses the cleared square; authenticated Atari ST source-order reads correct the fresh-start sensor chain across six editions. DM2 Macintosh work now binds more CHARSHEET control evidence, corrects big-endian wall-actuator interpretation and aligns hitboxes to source RECT_7. XP/RNG parity, complete Mac inventory dispatch, a normal later-map route and a successful live switch interaction remain open.


## 2026-10-02 — Portable outputs, native 6502 targets and active upstream review

Resolved twelve queued target-CPU areas with primary READMEs, repository trees, build files and source directives. **Commander X16 ROM — Commodore-derived system software** now records its explicit 65C02 output; **Edge Grinder — BBC Master 128 port** records the README's plain 2 MHz 6502 target and bounded Master hardware profile. Seven portable Go, .NET, Python, C++, Rust or SCI-VM outputs are explicitly not applicable to a fixed target CPU. **Jetpac — Acorn Electron conversion**, **Knight Lore — Acorn Electron prerelease** and **Lunar Jetman — BBC to Electron conversion** retain empty CPU metadata with `no-evidence-found` audits because their binary-only repositories do not state an output instruction set.

The upstream-change lane reviewed **Project Eon**, **papple2 — Apple II reverse-engineering emulator/debugger** and **Rolling Thunder — Amiga 68k translation**. Project Eon's record now bounds its recovered Deuteros title/bootstrap rendering and CIA continuation without promoting that to complete opening or gameplay parity. papple2 now reflects its `core-complete` rebuilt instrumentation and explicit ApplePy/oracle/sibling relationships. Rolling Thunder records the new default hardware-tester build and MCU input path while preserving the remaining scrolling, sprite, timing and lockup gaps.


## 2026-10-02 — Spectrum source graph, CPC/Atari tooling and output CPU audit

Reviewed the old `mrcook`/SkoolKit graph plus fresh CPC, Archimedes and SG-1000 search routes. Added **Manic Miner: Retro! — Z80-to-C++ source-faithful port**, **Rebelstar Raiders — recovered Spectrum BASIC/Z80 source**, **scrconv — ZX Spectrum SCR image converter**, **Earth Shaker — byte-exact ZX Spectrum disassembly**, **Eric & the Floaters — ZX Spectrum disassembly**, **iDSK — Amstrad CPC disk-image editor**, **SugarboxV2 — CPC emulator and source debugger**, and **Atari ST development toolkit — reproducible cross-build container**. The search record retains exact queries and the already-indexed Acorn/SG-1000 duplicate outcomes.

The separate CPU lane resolved eight queued areas across eight projects, reducing the unresolved queue from 103 to 95. Three reconstructed Amiga components now record evidenced m68000 outputs; AppEngine's original-library input CPU is explicitly not applicable; the two original 2.5vibe SDKs now distinguish source-CPU non-applicability from their explicit 6502 output; **StarCraft — AmiSC 68K** records its 68020/AmigaOS 3.0+/AGA-or-RTG floor without inventing a RAM minimum; and **Athena — Spectrum 128K to Next reconstructed port** now cleanly separates original Z80 input from Z80N output and records only the arcade variant's explicit 2 MiB requirement.


## 2026-10-01 — Reconstructed output CPUs, amimcp variants and unavailable Starflight source

Resolved ten queued CPU areas across nine projects, reducing the unresolved-project queue from 112 to 103. **Supaplex — assembly-level DOS binary patches** now records its explicit x86 patched-executable output without turning a reported 386DX/40 working result into a minimum. **PET Frogger — recovered original source** records its checked-in 6502 PRG output, while its exact PET model and RAM floor remain open.

Five reconstructed Amiga components now record m68000 output from their reviewed source rather than leaving the target architecture unresearched: **Emetic Skimmer — The Movers cracktro reconstruction**, **The King of Chicago — HQC intro reconstruction**, **Rick Dangerous — Oracle trainer menu reconstruction**, **Robocod — TRSI trainer menu reconstruction**, and **RSI Cruncher v1.4 — reconstructed Amiga source**. Their assembly, binary comparison and full hardware compatibility remain separate unresolved areas.

**Tempest 2000 — Jaguar original-source restoration** now records both its 68000 main program and linked Jaguar GPU modules. The documented hash-checked ROM build remains an upstream claim pending independent reproduction. **Starflight — Atari ST binary and asset analysis** was corrected in the opposite direction: its canonical repository now returns 404, so an inferred m68000 field was removed, native output marked not applicable and identity/relocation research left open.

The active-upstream review corrects **amimcp** from a historical-source model to original development tooling with explicit 68000, 68020+ and Apollo 68080 agent outputs. Its AmigaOS 2.04+/`bsdsocket.library` baseline and three exact build variants are now represented without inventing RAM requirements. **SNES IDA loader and processor** now has a reviewed AI audit matching its two explicit Claude-attributed commits.


## 2026-10-01 — Firmware, CPC/DOS output CPU audit and Firestaff Macintosh review

Resolved eleven CPU audit areas across ten projects. **SidecarTridge — Atari ST disk image browser** now distinguishes its CPU-independent ST/MSA inputs from its explicit m68000 Atari-side image and separately identified RP2040 firmware, without inferring another CPU family from the board name. **ST Recover — floppy imaging** and **SuperDiskIndex — Amiga/Atari flux-image analyzer** now mark sector/flux input CPUs not applicable, while **xPack — Amiga XPK unpacker for Linux** records no original-CPU evidence rather than inferring one from AmigaOS provenance.

Primary build/source evidence now records Z80 output and the explicit 128 KiB floor for **The Abbey of Crime (English translation)**; m68000 output for **Beneath a Steel Sky — Delirium cracktro reconstruction**; and x86 DOS output for **Cosmo's Cosmic Adventure — source reconstruction**, **Duke Nukem II — byte-exact DOS source reconstruction**, **F-15 Strike Eagle II — DOS executable reconstruction**, and **Pacwars — debug-symbol-assisted DOS C decompilation**. Runtime profiles are limited to exact statements: Cosmore and Duke II have documented 80286 instruction floors, while F-15 and Pacwars retain unknown minimum hardware.

Active review of **Firestaff — Dungeon Master / Chaos Strikes Back engine reconstruction** captures v3.0.353's authenticated Macintosh-retail AUTO selection, source-owned viewport/HUD and bounded movement/audio regressions. The record preserves upstream's limits: audible native output, physical Retina presentation and same-state visual comparison with the original remain unverified.


## 2026-10-01 — Successor reviews, Apple IIGS/Jaguar/Mega Drive search and CPU audit

Closed both previously unreviewed successor tasks. **Tube64 — 64-bit Bullfrog Tube reconstruction port** is now represented separately from the pointer-sensitive 32-bit DOS reconstruction, while **xrick-kb — Rick Dangerous reverse-engineering knowledge base** records the independent Atari ST/DOS Ghidra, RAM-capture, format and Hatari-validation corpus rather than folding it into the runnable xrick port.

Three rotated fresh searches added **6502bench SourceGen — interactive 6502-family disassembly workbench**, **TransWarp GS ROM 1.8s — byte-identical Apple IIgs disassembly**, **Jaguar SDK — restored Atari development toolchain**, **jagfx — Atari Jaguar graphics extractor and ROM searcher**, **Flicky — byte-identical Mega Drive source reconstruction**, and **Alien Soldier — byte-identical Mega Drive source reconstruction**. Exact queries and reviewed URLs are retained in research state; Apple II DeskTop and SAM were recorded as exact catalogue duplicates. The Mega Drive records distinguish their 68000 program and Z80 sound components and preserve their explicit byte-identity/runtime evidence.

The separate CPU lane resolved ten queued source-CPU areas for **Floppy Disk Workbench — Amiga/Atari flux recovery**, **iff2bpl — Amiga bitplane converter**, **IFFshow — Amiga ILBM inspector**, **Kick Off 2 — tactic file editor**, **AmigaIFFConverter — ILBM writer**, **rscview — GEM resource renderer**, **Rusty Backup — Amiga RDB and Atari AHDI image tooling**, **SCI Companion — Sierra game IDE**, **ScummVM Tools — Amiga/ST extractors**, and **SCI Tools — decompiler and parsers**. Their documented inputs are flux, disk, graphics, resource, tactic or virtual-machine data; source CPU is therefore explicitly not applicable rather than inferred from a platform label.


## 2026-10-01 — BBC/Acorn graph, HuC6280/Mac/Atari searches and CPU audit

Added eight primary-source-backed projects. The changing Mark Moxon graph yielded **Elite Compendium — Acorn Electron 16K sideways-RAM collection**, **Elite Compendium — BBC Micro B+ / B+128 collection**, and **!EliteNet — Archimedes Elite Econet scoreboard application**. !EliteNet is explicitly recorded as original RISC OS homebrew/application work that leaves Archimedes Elite untouched, not as a reverse-engineered game. The two platform-specific Universe Editor repositories were deduplicated against the existing multi-platform editor record.

Three rotated fresh-search slices added **huc6280disasm — code-flow-aware PC Engine disassembler**, **dis6280 — PCEAS-style HuC6280 disassembler**, **Etripator — PC Engine ROM/CD disassembler**, **resource_dasm — classic Mac resource and machine-code archaeology suite**, and **Alternate Reality: The Dungeon — Atari 8-bit byte-checked disassembly**. The search record preserves the exact GitHub/web queries and exact duplicates for the already tracked Macintosh ROM and Star Raiders projects. resource_dasm remains one coherent repository-root project rather than being over-split into its many related utilities.

The separate CPU lane resolved ten queued source-CPU areas. AmigaFFH, amigainfo, atari-hd, CHZPART and Crunch-Mania now explicitly treat their file/disk/stream inputs as CPU-not-applicable. Atari ST Floppy Image Toolkit records the bundled m68000 emulator core, while Gearboy, Gearcoleco, Geargrafx and Gearsystem now record SM83, Z80, HuC6280 and Z80 guest CPUs from primary debugger/core documentation. No host CPU or minimum hardware was inferred from platform or language.


## 2026-09-30 — Cross-platform output and ADF-input CPU audit

Resolved ten queued CPU areas across **Harrier Attack Reloaded**, **Oh Mummy Resurrected**, **Seven Cities of Gold — reverse-engineered macOS remaster**, **Starflight — Vulkan remaster from recovered Forth/x86 runtime**, **Atari STBook/STylus diagnostic cartridge analysis**, **SunDog — Atari ST p-system runtime reconstruction**, **Sensible World of Soccer / OpenSWOS**, **ADF Opus 2025 — Amiga disk image workbench**, **ADF reader/writer — Amiga OFS/FFS image inspector**, and **ADFlib — Amiga OFS/FFS filesystem library**. Primary documentation establishes Starflight's x86-64 builds and OpenSWOS's explicit ARM-handheld target, while undocumented CPC, Swift/macOS and portable-C host architectures remain **no evidence found** rather than inferred from platform or language.

The three ADF/OFS/FFS tools now classify their disk and filesystem inputs as CPU-not-applicable; ADFlib's historical MC68EC020 development machine is retained only as provenance. Exact Plus-emulation, macOS 14+/Swift 6, SDL/OpenGL and diagnostic-board execution contexts are recorded without inventing RAM or processor minima. OpenSWOS is also corrected to match its current primary README: a clean-room C#/Godot reimplementation informed by Amiga 68k source, DOS Ghidra analysis and `swos-port`, not a C++/assembly reconstruction output.


## 2026-09-30 — Amiga/Z80/MIDI CPU audit and active upstream review

Resolved eleven queued CPU areas across **XFDMaster — Amiga packed file decruncher**, **Roc'n Rope — Amiga arcade transcode**, **Super Bagman — Amiga arcade transcode**, **Track & Field — Amiga arcade transcode**, **Vulgus — Amiga arcade transcode**, **Mercenary (ZX Spectrum disassembly / Next port)**, **MIDI-MAZE II — Atari ST title music and player reconstruction**, **MIDI Maze — browser port from reconstructed ST source**, and **MIDImaze — Atari ST reverse-compiled C**. Primary package metadata, assembly and build files establish m68k, m68000/m68020, Z80N and Intel x86-64 outputs. Packed/data inputs, browser bundles and music exports are explicitly CPU-not-applicable where appropriate; runtime notes preserve exact Node/Python/macOS and hardware evidence without inferring host CPUs or RAM from platform names.

Active review records **NESRecomp — 6502-to-C static recompilation framework** adding opt-in cycle-backend game-mod hooks, isolated guest calls, mod save-state records and custom-width rendering; **UnifiedFloppyTool — Amiga/Atari disk preservation** wiring sector-ID verification, retry count and clock correction into measured conversion paths; **Project Eon** reaching bounded MCGA/EGA return paths and publishing recurring Deuteros Original frames without claiming capture parity; and **Firestaff — Dungeon Master / Chaos Strikes Back engine reconstruction** narrowing Theron status to its current 53/53 labeled test boundary while keeping original presentation and gameplay consumers open.


## 2026-09-30 — Portable/native CPU audit and active upstream review

Resolved eleven queued source/output CPU areas across **Carmageddon — incremental DOS executable reconstruction**, **Duke Nukem II — RigelEngine modern reimplementation**, **Prince of Persia — DOS-disassembly-derived SDL port**, **Zeliard — independent DOS analysis and SDL port**, **Frontier: Elite II — Atari ST VM/reimplementation**, **FujiBoink! — Atari ST demo converted to Amiga**, **The Great Escape**, both **Hlípa** ports and **Project Eon — multi-game preservation and native reimplementation**. Primary workflows and build files establish only exact x86/x86-64/arm64, ARMv6, WebAssembly, 68000 and Z80 outputs; Zeliard and FrontierVM remain explicitly **no evidence found** for portable-host CPU. Exact Hlípa, RigelEngine and Great Escape runtime statements are retained without converting vague usage or platform labels into invented minima.

Active review records **Fairlight II — ZX Spectrum completion-bug reverse engineering** explicitly attributing its E1–E6 room-flag interpretation to ChatGPT, **Hlípa — PMD 85 to ZX Spectrum reconstruction/port** v1.3 producing Czech and English TAP/SNA variants, **Elite — BBC Master reconstruction** adding byte-matching Master Compact ADFS output, **Project Eon** connecting a bounded Millennium DOS video-driver load session, and **Master of Magic — ReMoM Amiga port** 0.5.3 fixing movement-mode byte ordering and stale Build-button state. Project Eon's synthetic selector/DOS observations and absent INT 91h dispatch remain stated boundaries, not gameplay-parity claims.


## 2026-09-30 — NESRecomp title graph, multi-system archaeology and CPU audit

Promoted thirteen primary-source-backed projects from two queued graph reviews and a rotated SG-1000/SC-3000/ColecoVision search. **game-music-extraction — multi-system music sequence archaeology** is retained as one coherent cross-system extractor and analysis project. The NESRecomp root yielded nine independently runnable title projects: **Super Mario Bros. — NES-to-PC static recompilation**, **Duck Hunt — NES-to-PC static recompilation**, **Dr. Mario — NES-to-PC static recompilation**, **The Legend of Zelda — NES-to-PC static recompilation**, **Faxanadu — NES-to-PC static recompilation**, **Yoshi — NES-to-PC static recompilation**, **Yoshi's Cookie — NES-to-PC static recompilation**, **Mega Man 3 — NES-to-PC static recompilation**, and **Gumshoe — NES-to-PC static recompilation**. Their status claims remain title-specific and bounded to each repository's documented testing rather than inherited from the framework.

The fresh-search slice added **morepork — multi-system emulator trace capture and comparison**, **Amy Studio — browser-based ColecoVision development environment**, and **Mr. Do! — arcade-style ColecoVision fan conversion**. The exact repository/code searches and reviewed outcomes are retained in research state; Gearsystem, Gearcoleco and MEKA were deduplicated against existing records. Amy Studio is classified as original development tooling, and Mr. Do! as a disassembly-based fan conversion rather than reverse-engineering work in its own right.

Separately resolved eight queued target-CPU areas across **Jail Break — Amiga arcade transcode**, **Karate Champ — Amiga arcade transcode**, **Lock 'n' Chase — Amiga arcade transcode**, **Nibbler — Amiga arcade transcode**, **Pengo — Amiga arcade transcode**, **Phoenix — Amiga arcade transcode**, **Pooyan — Amiga arcade transcode**, and **Rally-X — Amiga arcade transcode**. Checked-in build files distinguish m68000 and m68020 variants; stated Chip-RAM floors are captured only for Jail Break and Karate Champ, Pengo's Neo Geo output is now explicit, and Nibbler's aspirational 512 KB goal is not presented as current compatibility.


## 2026-09-29 — Amiga arcade output CPUs and bounded runtime evidence

Resolved ten queued target-CPU areas from project READMEs and checked-in build files. **Bad Dudes vs. DragonNinja — Amiga arcade port**, **Bagman — Amiga arcade transcode**, **BurgerTime — Amiga arcade transcode**, **Dig Dug II — Amiga arcade transcode**, **Donkey Kong — Amiga arcade transcode**, **Elevator Action — Amiga arcade port**, **Galaga — Amiga arcade transcode**, **Gravitar — Amiga arcade transcode**, **Gyruss — Amiga arcade transcode**, and **Hyper Sports — Amiga arcade transcode** now distinguish explicit 68000, 68020 or broad m68k output evidence. Variant-specific OCS/ECS/AGA, Chip-RAM, total-RAM and WHDLoad statements are recorded only where primary documentation states them; model names and vague Fast-RAM requirements were not converted into invented numeric minima.

Material upstream review records **Firestaff — Dungeon Master / Chaos Strikes Back engine reconstruction** requiring authenticated Atari ST, Amiga and FM Towns CSB routes to produce a nonzero source-rendered viewport hash and promoting DM2 Amiga from a fail-closed frame to a real-GDAT launcher-to-runtime receipt, while retaining its input/save/display/audio/dungeon limits. **Ghidra Retro Machines — bank-aware loaders and retro CPU languages** now includes its explicit SNES SPC700/65C816 language scope and records the single named 65C816 E1.E oracle defect, the 500 PASS / 8 N/A / 4 FAIL baseline and tripwires that fail if the excluded case starts passing or disappears. Its credited **game-music-extraction** parent is indexed as a separate lead for coherent-scope review rather than prematurely split into directory records.


## 2026-09-29 — Native-output CPU audit and active upstream review

Resolved ten queued CPU areas from primary READMEs, source declarations and build scripts. **xrick — Rick Dangerous reimplementation** now records its explicit IBM PC x86 and Atari ST 68k inputs plus current Windows x64/WebAssembly outputs. **Atari ST BIOS ROM comparative listings**, **Elite Compendium — BBC Master disc integration**, **Fuzzy's Space Golf — partial DOS resource decoding**, **ShortLine v1.1 — offset-annotated reconstructed port**, **Tube — reconstructed DOS Bullfrog game port**, **Zeliard — bit-perfect MASM reconstruction and web port**, and **Frontier: Elite II — Amiga renderer/audio reconstruction** now distinguish directly evidenced native/wasm outputs from undocumented portable-host architectures. Clyde and Rayman remain analysis/disassembly outputs, so their native target CPU is explicitly not applicable rather than guessed. Fuzzy's mixed original-game and planned-port hardware discussion remains a bounded needs-research item.

Primary Amiga package documentation also establishes Frontier's 68040+, 8 MB, RTG and AmigaOS 3.x/AROS floor. **NESRecomp — 6502-to-C static recompilation framework** now records merged Famicom Disk System LLE/HLE support and its bounded synthetic-BIOS, multi-side and owner-ROM testing. **ZX Spectrum game disassemblies — reproducible SkoolKit archaeology** now spans nine subjects; Pentagram, Alien 8 and Nightshade bring the documented fully covered, byte-exact set to seven. xrick's linked knowledge base and Tube's linked Tube64 successor are retained as explicit discovery tasks pending independent-scope review.


## 2026-09-29 — Elite version graph, TRS-80/X68000 search and CPU audit

Completed the queued Elite library-version review and added three distinct source-backed projects: **Elite — Apple II documented original sources**, **Elite — BBC Micro cassette documented original sources**, and **Elite Compendium — BBC Micro 16K sideways-RAM collection**. Each has an independent primary repository and build scope; the BBC Micro collection is kept separate from the already tracked BBC Master Compendium.

The rotated TRS-80, Apple IIgs and X68000 searches added **TRS-80 Level I ROM — annotated Z80 disassembly**, **TRS-80 Model 102 ROM — documented source reconstruction**, **Akumajou Dracula — X68000 15 kHz display hack**, **Sharp X68000 XVI IPL — Ghidra analysis**, and **Extractors and Decoders — multi-platform game archive tools**. Two Model 102 forks were recorded as duplicates and a README-only TRSDOS repository was excluded. Apple IIgs and X68000 source-reconstruction searches yielded no further candidates. The Dracula work is explicitly a disassembly-derived fan hack, while the Model 102 identity build remains a goal rather than a claimed verified result.

Separately resolved eight queued target-CPU audit areas across **Alien (1984) — Python remake and disassembly**, **Ambermoon Advanced**, **Ambermoon.net — Ambermoon engine reimplementation**, **Grand Theft Auto — AmiGTA**, **BattleTech: The Crescent Hawk's Inception — C64 static recompilation**, **CDTV OS 2.35 — reconstructed firmware patch**, **Chase H.Q.**, and **DolphinDOS 2 — C64 KERNAL ROM source and modification**. Exact native targets and runtime floors follow primary assembly/build documentation; portable Python and undocumented host minima remain not-applicable or no-evidence-found rather than inferred.


## 2026-09-28 — VM/data CPU boundaries and active upstream review

Resolved twelve queued CPU audit areas across **Amber Remix — Amiga Amberstar data decoder**, **Amberworld — Amber trilogy format & code reverse engineering**, **Flashback — Atari ST REminiscence port**, **Gorillas — DOS QBasic to C64 BASIC port**, **Hulabee Sauce — VM and asset tools**, the two Lab 313 IDA Amiga tools, **SAM — C port of C64 speech synthesizer**, **Sierra SCI scripts — decompiled corpus**, and **Tokimeki Memorial: Forever With You — PlayStation Ghidra analysis**. Data containers, language-level ports and SCI/Sauce bytecode are now explicitly CPU-not-applicable or no-evidence-found. Source declarations establish only the IDA tools' m68k/68040 analysis selections, SAM's 6502 reverse-source lineage and Tokimeki's MIPS R3000 input. Flashback also gains the README's exact 2.5 MB RAM floor, 4 MB recommendation and 3.5 MB disk requirement without inventing a minimum CPU.

Material upstream review records **UnifiedFloppyTool** raising A2R to T1 with both real container layouts and fixing Apple GCR seam/checksum handling; **Firestaff — Dungeon Master / Chaos Strikes Back engine reconstruction** passing 71 registered Theron tests and covering all type-zero inventory records while retaining its T900/campaign caveats; and **Ghidra Retro Machines — bank-aware C64, C128, PET and NES loaders** adding constant-pointer and table-after-code analysis while leaving three NES rows explicitly held for owner review.


## 2026-09-28 — Format-tool CPU audit and active upstream review

Resolved twelve queued CPU audit areas across **AmbermoonSourceror — Ghidra-to-Amiga assembly converter**, both **AmigaHunkParser** implementations, **Amiga Imploder — decompiled compressor**, **MapTapper — Amiga graphics and map ripper**, **raw2iff — Amiga/ST graphics converter**, **STTRANS — Atari STBook transfer protocol research**, and **UnifiedFloppyTool — Amiga/Atari disk preservation**. Generic HUNK containers, savestates, raw graphics, disk images and flux streams are now explicitly CPU-not-applicable instead of inheriting architecture from their platform label. AmbermoonSourceror's output is tied to its explicit `-m68000` assembler flag while the original input CPU remains no-evidence-found; the checked-in STTRANS.PRG primary artifact identifies as Atari ST M68K. The C HUNK parser also built cleanly with GCC and ran its usage path locally.

Material upstream review records **UnifiedFloppyTool**'s 570/570-tested ring-position validation and the still-unresolved G71 bridge gap, **Rolling Thunder — Amiga 68k translation** reaching working 16x16 tiles/mirroring while multi-CPU synchronisation remains explicitly broken, and **Firestaff — Dungeon Master / Chaos Strikes Back engine reconstruction** adding bounded authentic-media door and inventory regressions. Firestaff's new checks remain narrowly described: they verify fail-closed doors and source-record-preserving item transactions, not original door, T900/UI, quest-item or complete campaign semantics.


## 2026-09-28 — Atari VCS homebrew graph, DOS tooling and CPU audit

Completed the canonical `milnak/atari-vcs-disassembly` submodule review. Added five distinct, source-backed Atari 2600 homebrew projects at their demonstrated scope: **Grizzards — Atari 2600 turn-based RPG**, **Climber 5 — Atari 2600 homebrew adaptation**, **Pacman4K — 4 KiB Atari 2600 Pac-Man homebrew**, **2048 — Atari 2600 homebrew port**, and **Atomchess — 1 KiB Atari 2600 chess port**. These are explicitly classified as original homebrew, behavioral adaptations or source ports—not reverse-engineered binaries. The book, lesson-code and small-demo aggregate repositories remain discovery references rather than single project records.

The rotated CPC, DOS and Intellivision searches also added **wcdatool — Watcom DOS executable disassembly workbench**. Existing CPC results deduplicated to tracked records; Intellivision searches produced no new qualifying candidate. A sparse but implemented DOSBox Staging VS Code extension remains deferred for source-level capability verification.

Separately resolved twelve queued CPU audit areas across **Jr. Pac-Man — Amiga maze and sprite conversion script**, **Rockford — DOS hidden-level recovery and patcher**, **Tearaway Thomas — Amiga DHp2 unpacking research**, **lxa — Linux Amiga executable runtime**, **NiteCrawl — Atari ST C++ decompilation**, and **image-rider — exploratory Atari ST STX parser**. Data/media-only inputs are now explicitly CPU-not-applicable, undocumented executable architectures are recorded as no evidence found, lxa's 68000 guest is primary-source verified, and NiteCrawl's m68k output follows its actual cross-toolchain rather than the platform label.


## 2026-09-27 — Firmware/arcade CPU audit and active upstream maintenance

Resolved ten queued CPU audit areas across six projects. **FlashFloppy** now records its explicit ARM Cortex-M3/M4 Gotek firmware variants and documented MCU RAM floors without assigning CPUs to disk-image inputs. **RetroGhidra** records the processor IDs selected by its loaders. **RExtract** is explicitly CPU-not-applicable on both sides because it converts disk/music data rather than native code. **Jungle King** and **Tiger Heli** now have reviewed Z80 source evidence and no invented native output; Tiger Heli's copied/mismatched Amiga scaffold remains outside the tracked arcade-disassembly claim. **AmiXcom** closes its target-CPU gap with the documented 68020+/AGA, Kickstart 3.0+ and approximately 50 MB Fast-RAM profile.

Material upstream review records **AmiXcom 0.9.14** and its AdLib/AmiXcomPrefs work, **NESRecomp**'s generated catalog of 57 supported mapper IDs covering 6,682 known dumps with bounded validation language, and **ZX Spectrum game disassemblies** reaching complete 40,696-byte Knight Lore coverage with original-table room editing and game-code-driven animation, sound and behavior pages.


## 2026-09-27 — Arcade, VM and media CPU audit plus active upstream review

Resolved twelve queued CPU audit areas from primary source. **Berzerk** is confirmed as a Z80 disassembly with no native output target; its source header also explicitly discloses Deepseek V4 AI. **Marble Madness II** now records the M68000 arcade original and the unfinished Amiga loader's explicit 68020/AGA target without presenting its declared memory as a verified runnable profile. **Super Pac-Man** now records its actual in-progress Amiga m68000/m68020 outputs and explicit Claude-assisted reverse-engineering commit while retaining open build/runtime questions. Another World's analysed VM bytecode and DrawBridge/STM32 floppy media are no longer treated as architecture-bearing inputs; STM32 USB Floppy Tracer records the explicit ARM Cortex-M firmware target, while DrawBridge's unnamed Arduino MCU remains **no evidence found**.

Active-upstream review also recorded **Copperline 1.0.0-rc.1** and its supported release/build paths, **Firestaff**'s bounded authenticated-media Atari ST, Amiga and FM Towns menu/runtime handoffs, and **Bosconian**'s explicit Claude-assisted Z80 reverse-engineering pass. None of the bounded startup tests or unfinished translations were promoted to complete gameplay claims.


## 2026-09-26 — Arcade CPU evidence and active upstream maintenance

Resolved ten queued CPU audit areas with primary evidence. MAME's current hardware drivers establish Z80 originals for Amidar, Pac-Man, Ms. Pac-Man and Scramble, HD6309 for Double Dragon, and 6502 for U.S. Championship V'Ball. BeerMon's source documents the m68k family and explicitly selects `mc68030` for the reconstruction output; this does not claim a minimum runnable Amiga. Prehistorik's reviewed tree does not name its original executable CPU, while REminiscence consumes multi-platform resource data rather than native executable code, so those cases now record **no evidence found** and **not applicable** instead of platform-derived guesses.

Material upstream work was also incorporated. **NESRecomp** now records its opt-in cycle-accurate compiler/runtime, bounded interpreter fallback, validation boundaries and rollback netplay. **STDL** now records its documented cross-build, runnable TOS examples, target byte-comparison tests, per-step YM effects and 50/60 Hz timing fix; no universal minimum hardware profile is inferred. **Firestaff** now distinguishes authenticated US/JP Theron Track 02 early-runtime boots and a bounded fresh-start DM1 save round-trip from still-unverified campaign parity and Atari v1.0 save resume.


## 2026-09-26 — Amiga/Atari format audit and Elite root scope

Read primary repository READMEs for sixteen tracked disk-image, archive, graphics, level-data and recovery tools. Their source and target CPU audit areas now say **not applicable** to the data-format operation; host language and an Amiga/Atari input format are not a minimum CPU claim. Initial identity/classification checks were recorded where previously unreviewed, while build, AI and relationship areas remain open when not verified. Relevant READMEs document boundaries such as Adf7z's extraction-only behavior, retro-io's planned Atari XL support, fluxfox's initial Amiga/ST support, and xdms-rs's mode-specific test coverage.

The `vschwaberow/amiga_reconstructed` inventory was also completed: all fourteen present component directories and their source headers were checked. Three were already catalogued; eleven distinct historical intros, trainer menus and tools were added with original author attribution and build/runtime/byte-match status left unverified. The corresponding discovery task is closed, and the source index preserves the qualification scope.

Two Atari ST demo audits were also tightened. **Mono Mental** has an explicit 68000, 1 MB, TOS 1.04+, hard-drive and high-resolution monochrome requirement; its unsupported negative AI usage field was reset to unknown. **TCB Star-Wars Scroller** documents vasm reassembly but leaves one effect partly unanalysed and changes the extracted quit path, so neither byte identity nor a runtime floor is inferred.

The ataribaby42 Elite root README and `src_atari`/`src_orig` documentation identify independent enhanced Atari ST, native Amiga, and preserved-original Atari ST builds. The formerly Amiga-only enhanced entry now points to the repository root and covers both enhanced targets and their separate runtime profiles. The preserved `src_orig` catalogue entry stays at its distinct source tree. Its stable existing ID preserves research and activity references; visible classification, title and tracking path reflect the new scope.

## 2026-09-23 — baseline

Scope expanded to **Amiga, Atari ST, ZX Spectrum, C64 and Amstrad CPC**.

State rules:
- An old/dormant project newly found by us counts as a discovery.
- Known projects are reported again only for substantive milestones.
- Routine commits and trivial progress changes are noise.
- Follow references outward from known authors/projects.

Latest expansion identified:
- Spectrum: Chase H.Q., The Great Escape, nzeemin SkoolKit collection, JETPAC, River Raid, Nether Earth, Alien, plus Paul Maddern/Ritchie Swann leads.
- C64: Iridis Alpha, Matrix, Ancipital, Spy Hunter, Commando and Attack of the Mutant Camels leads, Pitfall II.
- CPC: Head Over Heels and CPC BASIC 1.1.
- Existing discovery nodes include Tetracorp, Pyrdacor, Llamasource/mwenge, Sarnau and geogeo28/atari_reverse.

### Next search priorities

1. Resolve canonical sources for historical Spectrum/C64 leads.
2. Mine SkoolKit authors and credits outward.
3. Enumerate remaining Llamasource work.
4. Revisit Tetracorp external RE links.
5. Mine Pyrdacor/Amber credits and predecessor research.
6. Search CPC communities more deeply; CPC has the thinnest baseline.


## 2026-09-23 — reference-mining follow-up

Followed links/credits already present in known project data rather than relying primarily on generic search.

### Newly promoted into catalogue

- **The Lords of Midnight (ZX Spectrum/DOS)** — Michael Cook's parallel disassembly. Ghidra was used for the DOS binary and SkoolKit for Spectrum; surviving partial DOS source and Icemark data research help annotate/reconstruct the rest.
- **Head Over Heels (ZX Spectrum)** — Simon Frankau's work surfaced directly from the CPC Head Over Heels README, which credits it because the CPC port is closely related to the Spectrum version.
- **SkoolKit maintained disassemblies** — Skool Daze, Back to Skool, Contact Sam Cruise, Manic Miner, Jet Set Willy and Hungry Horace are explicit complete disassembly lines and should be tracked as projects, not merely as examples of the tool.
- **Piddewitt C64 cluster** — Lode Runner, Championship Lode Runner and The Castles of Dr. Creep. The first two explicitly target bit-for-bit-identical reconstructed assembler source.

### Strong discovery leads retained

SkoolKit's curated links substantially expands the Spectrum queue. Paul Maddern alone is linked to 180, Atic Atac, Battlezone, Batty, Booty, Jason's Gem, Jetpac, Lunar Jetman, PSSST, Rampage and Splitting Images. Michael Cook's collection additionally identifies Philip Anderson (Knight Tyme, Spellbound, Stormbringer, Through The Trap Door), BadBeard (Dynamite Dan 2), Lunysoft (Tir Na Nog, Dun Darach), tcdev (Alien8, Knight Lore), Simon Owen (Atic Atac) and multiple Chaos disassemblies.

The ArcadeGeek SkoolKit archive reported 29 Spectrum disassemblies during this pass and is now a discovery node.

### Method result

Cross-references continue to outperform generic searches. The CPC Head Over Heels project led directly to the Spectrum Head Over Heels work; Gridrunner's write-up exposes predecessor C64 disassemblies; and SkoolKit's own link/index pages expose a much larger historical Spectrum RE graph.

### Next priorities

1. Resolve Paul Maddern's GitHub projects individually and record canonical URLs/status.
2. Enumerate all 29 ArcadeGeek entries and deduplicate against known projects.
3. Inspect Piddewitt's C64 repositories and their documentation for further adjacent authors/projects.
4. Follow Simon Frankau beyond Speedball 2 and Head Over Heels.
5. Continue CPC-specific graph discovery, which remains much thinner than Spectrum/C64.


## 2026-09-23 — historical Spectrum + CPC resolution pass

Resolved the named Spectrum backlog into canonical/current sources and expanded CPC substantially.

### ZX Spectrum

- Enumerated the current Pobtastic/ArcadeGeek index and mapped its disassemblies to current GitHub repositories/subdirectories.
- Promoted all previously listed Paul Maddern/Pobtastic leads and additional current catalogue entries, while keeping genuinely independent disassemblies separate (for example Michael Cook's JETPAC vs Pobtastic's JETPAC).
- Resolved Ritchie Swann's Deathchase, Everyone's A Wally and Starquake repositories.
- Promoted Philip M. Anderson's four complete SkoolKit disassemblies from the preserved source in `mrcook/zx-spectrum-games`, with links to the rendered Wolfe-Lyon versions.
- Promoted BadBeard's Dynamite Dan II, Lunysoft's Tir Na Nog/Dun Darach, tcdev's Alien 8/Knight Lore/Pentagram and both the historical Guesser/szeliga and modern Lewis Lane Chaos projects.

### Amstrad CPC

Added new qualifying projects/sources:

- Bread80 CPC6128 firmware reconstruction
- Richard Lloyd CPC464 ROM disassembly
- Sarnau HiSoft DEVPAC reverse engineering
- La Abadía del Crimen preservation/disassembly/remake work
- The Abbey of Crime English patching project
- Into the Eagle's Nest CPC analysis
- Laserwarp full cassette-derived disassembly with byte-exact round trip and explicit Claude assistance
- Oh Mummy Resurrected
- Harrier Attack Reloaded

CPC discovery sources now include CPC Analyser, CPCWiki, Bread80, BrettHallen, moqucu and Sarnau's CPC work.

### Result

Structured project count increased from 69 to 121. `projects.md` now contains only open-ended discovery directions rather than the previously named Spectrum/CPC source-resolution queue.


## 2026-09-23 — BBC/Acorn expansion and new Amiga/Atari leads

User-supplied leads expanded the tracker beyond its original five platform families.

### Mark Moxon / bbcelite.com

Promoted binary-derived reconstructions for:

- Elite (BBC Micro disc)
- Elite Demonstration Disc (BBC Micro)
- Elite (Acorn Electron)
- Elite (BBC Master)
- Elite (NES)
- Aviator (BBC Micro)
- Revs (BBC Micro)
- The Sentinel (BBC Micro)
- Lander (Acorn Archimedes)

These repositories explicitly describe hand reconstruction from disassembly and provide build/reference verification. Mark Moxon's BBC Micro cassette Elite, 6502 Second Processor Elite, Commodore 64 Elite and Apple II Elite repositories are intentionally not promoted in this pass because their READMEs describe them as documented/preserved original source rather than source reconstructed from binaries. Elite-A is also left for later assessment because the surviving source is original source from a historically reverse-engineered derivative rather than a fresh binary reconstruction by the current repository.

### ataribaby42

Promoted:

- independent byte-exact ZX Spectrum Elite 128K-compatible reconstruction
- independently buildable Atari ST Elite source reconstruction from historical source material
- native Amiga Elite port derived from the corrected Atari source tree
- Hlípa Atari ST → Amiga reconstruction/port
- Hlípa PMD 85 → ZX Spectrum reconstruction/port

The Hlípa work adds PMD 85 as a source platform as well as another independent cross-platform reconstruction path.

### angree

Promoted:

- AmiGTA — clean-room/native Amiga reimplementation of Grand Theft Auto
- AmiSC — playable native Amiga StarCraft port using original game data; source is currently unpublished, so implementation provenance is noted as non-auditable
- AmiXcom — native classic-Amiga port of the OpenXcom reimplementation, explicitly developed with Claude Code
- Master of Magic ReMoM Amiga port — native port of a reconstructed C codebase

OpenSWOS was already tracked. Other angree repositories that are ordinary ports of open-source software or unrelated original projects were not promoted.

### Result

Structured project count increased from 121 to 139. Newly represented source/target families now include BBC Micro, BBC Master, Acorn Electron, Acorn Archimedes, NES and PMD 85. The public site description should remain platform-neutral so further additions do not require maintaining a hard-coded platform list.


## 2026-09-23 — jotd666 arcade-to-Amiga cluster

Audited the large `jotd666` GitHub profile and promoted 33 qualifying arcade-to-Amiga reverse-engineering/transcode projects with project-specific README evidence.

The promoted set includes Bagman, Ms. Pac-Man, Elevator Action, Galaga, Moon Patrol, Scramble, Atari Tetris, Pac-Man, Donkey Kong, Bad Dudes vs. DragonNinja, Phoenix, BurgerTime, Hyper Sports, Rally-X, Commando, Lock 'n' Chase, Karate Champ, Track & Field, Jail Break, Gyruss, Pengo, Dig Dug II, Ghosts 'n Goblins, Mappy, Pooyan, Super Bagman, Gravitar, U.S. Championship V'Ball, Roc'n Rope, Amidar, Double Dragon, Nibbler and Vulgus.

Common technique pattern: reverse engineer original arcade machine code (often Z80/6502/6809), transcode or adapt it to 68000 assembly, then replace arcade graphics/sound hardware access with native Amiga implementations. Some projects instead patch original 68000 arcade code directly (for example Bad Dudes).

Not yet promoted from this profile: repositories whose README was missing, minimal, or apparently copied from another project (including several names such as Xevious, Galaxian500, Jungle King, Jr. Pac-Man, Bosconian, Super Pac-Man, Dig Dug, Rolling Thunder, Tiger-Heli, Mr. Do, Berzerk and Marble Madness II). These remain discovery candidates for a project-specific evidence pass rather than being guessed into the database.

Structured project count increased from 139 to 172.


## 2026-09-23 — adjacent tooling and ROM/toolchain reconstruction pass

Reviewed seven user-supplied retro-development/tooling leads and broadened the catalogue carefully to include directly relevant reverse-engineering infrastructure.

Promoted six records: WinUAE as adjacent Amiga emulation/debugging tooling; th-otto/tos3x as Atari TOS ROM/source reconstruction; jonathanschilling/mac_rom as a five-ROM bit-identical Macintosh reconstruction; Level 9 l9dev as a C recoding of Atari ST 68000 authoring tools; wepl/ReSource as an Amiga reassembler/disassembler maintained from a self-resourced reconstruction; and Copperline as an active cycle-driven Amiga emulator/debugger with explicit AI-agent development guidance.

BlitterStudio/dopus5 was reviewed but not promoted as a catalogue record because its documentation identifies it as an active continuation of the 2012 released Directory Opus 5 source, not a reverse-engineering/source-reconstruction project. It remains a discovery node because it is strongly topical to the Amiga development ecosystem.

The broader promotion rule now explicitly admits core emulators, debuggers, reassemblers, reconstructed toolchains and archival development tooling when directly relevant to software archaeology, while ordinary source releases/maintenance remain excluded by default.

Structured project count increased from 172 to 178.


## 2026-09-23 — Copperline history backfill and 8-Bit Analysers

Investigated why Copperline showed its release but not its recent commit activity. The project was added on 23 September and the collector's first deep scan used the repository's first_seen timestamp as the lower bound, so commits from 19–20 September were outside the initial incremental fetch. Releases were populated separately from repository metadata, which is why v0.21.0 still appeared.

Fixed the collector so a repository's first branch scan backfills from the full retained 180-day activity window. Existing repositories remain incremental after their first successful scan.

Added TheGoodDoktor/8BitAnalysers as adjacent reverse-engineering tooling. Its README describes Spectrum, C64 and CPC analysis/annotation tools; recent history includes assembler export, MCP analysis tools, Copilot branches/commits and explicit Claude-related repository work.


## 2026-09-24 — hitchhikr Amiga disassemblies, analyser projects and activity fallback

Followed the Amiga/tooling graph and promoted eight buildable `hitchhikr` disassembly/reconstruction projects: **Alien Breed**, **Driller**, **Feud**, **Into The Eagle's Nest** (Amiga/Atari ST), **Spy vs Spy II**, **Spy vs Spy III**, **Thexder** and **Zool 2 AGA**.

Their common pattern is original disk/executable extraction, IRA/ReSource/Capstone-assisted disassembly where appropriate, vasm reconstruction and emulator validation. Byte exactness remains Unknown unless project-specific evidence supports it: Into The Eagle's Nest is explicitly non-identical because Atari ST-specific code was reconstructed, while Feud reports exact output for some versions but not others.

Audited `TheGoodDoktor/8BitAnalysers` and confirmed its tracker record is current through 23 September, including the current commit, weekly release, assembler export/MCP tooling and explicit Claude/Copilot evidence. Its neighboring `SpectrumAnalyserProjects` and `C64AnalyserProjects` repositories contain large title-specific analysis datasets, so both were added as discovery nodes for per-title review rather than promoting every directory without sufficient project-specific evidence.

Rechecked the Copperline discrepancy. The canonical project record already contains the 20 September main-branch commit `c79d6f46…`, which is newer than the 19 September `v0.21.0` release. The Activity view could nevertheless show the release while omitting that commit because it synthesized missing release events from project metadata but had no equivalent latest-commit fallback. Added a commit fallback so a known latest commit is shown even before the detailed activity collector has reached that repository.

Added a small pending-discovery merge queue used by the refresh workflow, allowing verified scheduled-discovery records to be merged into the canonical catalogue before GitHub metadata enrichment and validation.

Structured project count increased from 178 to 186.


## 2026-09-24 — HoraceAndTheSpider Amiga project audit

Audited the user-supplied HoraceAndTheSpider repository cluster and promoted four qualifying projects: **Cybernoid-68k**, **Legend-68k**, **Indy-Heat-WHD** and **Dalek-Attack-WHD**.

Cybernoid provides a lossless byte-identical GAME→project→GAME extraction/repack path plus decoded maps, graphics and tables; Legend reconstructs the PAC compression/resource format from Amiga resources and traced 68000 loader behaviour; Indy Heat contains active runtime-tested race/track/AI reverse engineering and editor tooling; Dalek Attack documents and patches character/resource structures through WHDLoad while decoding Pack-Ice assets.

**From-Lights-to-Flag** was reviewed but not promoted: its own documentation describes an original Amiga racer that uses findings from the separate Indy Heat reverse-engineering project as design reference and explicitly avoids transplanting original code/assets. It remains useful as a discovery node around the Indy Heat work.

HoraceAndTheSpider was added to recurring discovery sources for future profile/adjacent-repository passes.


## 2026-09-24 — PiST Atari ST development tooling

Promoted **PiST** as qualifying adjacent retro-development/software-archaeology tooling. PiST is a cross-platform Atari ST/STE 68000 IDE that integrates vasm/vlink with Hatari and provides source-line debugging, labelled disassembly, register/memory/hardware inspection, profiling, floppy-image and sprite/bitplane tooling, plus remote/MCP automation. The current README describes the write→assemble→run→debug loop as usable, and release v0.8.3 was published on 23 September 2026.

PiST was also added as a discovery node because its documentation links directly into the modern Atari development stack, including Hatari/hrdb, vasm/vlink, EmuTOS and legacy disk/graphics formats.


## 2026-09-24 — Atari Ghidra reverse-engineering tooling

Promoted **czietz/ghidraScripts_for_Atari** as qualifying Atari reverse-engineering tooling. The repository is explicitly intended to simplify analysis of Atari TOS code in Ghidra: it imports Atari executables with TEXT/DATA/BSS layout and relocations, imports TOS ROMs at their header-derived addresses, imports Atari a.out objects and symbols, and provides MiNTLib Function ID data plus TOS system-variable symbols for identifying otherwise unknown code.

The project remains maintained enough to support current tooling: its latest commit on 18 January 2026 adapts the scripts for Ghidra 12's runtime changes. The repository was also added as an Atari tooling discovery node.


## 2026-09-24 — amitools Amiga archaeology tooling

Promoted **cnvogelg/amitools** as qualifying Amiga software-archaeology and retro-development infrastructure. Its host-side toolset works directly with classic 68k AmigaOS binaries and storage formats: the Hunk library/hunktool loads executable, library and object-file hunks and relocations; romtool inspects, dissects and builds Kickstart ROM images; filesystem tooling handles ADF/HDF, RDB, OFS and FFS structures; and vamos executes Amiga CLI binaries through an API-level AmigaOS environment with detailed library-call, structure, code-fetch and memory tracing.

The current latest release is **v0.8.1** from 30 December 2025, with repository commits continuing through the same date. Added amitools as a recurring Amiga tooling/discovery node; its links to machine68k and historical Amiga development-tool execution are useful outward discovery paths.


## 2026-09-24 — Hatari, EmuTOS and modern Amiga debugger/toolchain cluster

Audited six user-supplied Atari/Amiga infrastructure repositories and promoted all six under the tracker’s tooling/reimplementation rules.

- **Hatari** — foundational ST/STE/TT/Falcon emulator with debugger, conditional breakpoints, symbol/disassembly support, CPU/DSP profiling and remote control.
- **EmuTOS** — free TOS-compatible OS/ROM implementation. Catalogued as reproducible Atari development/emulation infrastructure and a behavioral compatibility project, not as a reconstruction of proprietary Atari ROM binaries.
- **PUAE Debugger** — WinUAE-derived in-editor Amiga debugger/profiler with Hunk/ELF symbols, reverse execution, watchpoints, DMA/Copper/blitter analysis, memory reconstruction and MCP/DAP automation.
- **vAmiga Debugger** — integrated source debugger with fast-load, symbol-aware state/memory visualization, CPU/Copper disassembly and reverse stepping; recent profiler work includes explicit Claude-assisted commits.
- **m68k-tools** — reusable 68000 parser, formatter, cycle counter, linter/static-analysis and language-server suite.
- **BartmanAbyss vscode-amiga-debug** — self-contained GCC/GDB + WinUAE/FS-UAE Amiga development environment with source debugging, frame/DMA profiling, graphics debugging and source-correlated disassembly.

All six were also added as recurring discovery nodes because their dependency and attribution graphs connect to emulator cores, cross-compilers, debug formats, ROM replacements and other directly relevant software-archaeology tooling.


## 2026-09-24 — structured subject/tool classification

Reworked catalogue classification now that the tracker spans both reconstructed legacy software and substantial modern archaeology/development infrastructure.

Added four typed facets to every current project: **record class** (`subject`, `tooling`, `hybrid`), **target kinds**, **work kinds**, and **tool kinds**. The initial migration classifies 186 records as subjects, 12 as modern tooling and 2 as hybrids. Existing `types` and free-form tags remain intact for project-specific nuance rather than carrying the primary classification burden.

The Projects UI now exposes separate Class, Target kind, Work and Tool filters and renders prefixed badges such as **Target: Game**, **Work: Source reconstruction** and **Tool: Emulator**. Project details and Activity project headers show the same facets, and future material classification changes participate in catalogue-change activity.

The catalogue-state baseline was migrated together with the records so this one-time taxonomy introduction does not fabricate 200 metadata-update events. Site validation now enforces the controlled classification vocabulary and requires subject/hybrid records to have a target kind and tooling/hybrid records to have a tool kind.


## 2026-09-24 — compact classification presentation

Reduced the visual weight of the new structured classification badges after seeing them in the Activity feed. Repeated `Class:`, `Target:`, `Work:` and `Tool:` text was removed from badge bodies (the semantic prefix remains in the tooltip), saturated category colours were replaced with quiet neutral pills, and padding/gap/font sizes were reduced.

Activity now uses a deliberately compact classification summary. Subject records show the primary target plus at most two work kinds; tooling records show Tooling plus at most three high-value capabilities. Generic analysis/automation/toolchain capabilities are suppressed there when a more informative debugger/emulator/profiler/development-environment description is already present. The Projects table continues to expose the full classification, and the detail dialog retains the explicit labelled classification rows.


## 2026-09-24 — Firestaff, Starflight, CD32 disc archaeology and Llamasoft expansion

Audited the user-supplied Firestaff, Starflight, vs-sr-dev and mwenge discovery graph.

Promoted **Firestaff** as a clean-room/source-faithful Dungeon Master-family engine spanning DOS, Atari ST, Amiga, FM Towns, Macintosh, Saturn and PC Engine/TurboGrafx source families, and **Starflight Reverse** as a DOS/Forth reverse-engineering project that recovers threaded words, overlays and C representations from the original binaries.

Promoted **19 title-specific vs-sr-dev Amiga CD32 archaeology repositories**: Alfred Chicken, Banshee, Dragonstone, Fire & Ice, Gloom, Guardian, Gunship 2000, HeroQuest II, James Pond 2, Legends, Liberation: Captive II, Marvin's Marvellous Adventure, Microcosm, Myth, Power Drive, Prey, Superfrog, The Speris Legacy and Universe. These are documentation-first projects, but each performs substantive executable/disc/data-format reverse engineering with reproducible tools; the shared `cd32-platformnotes-doc` and `cd32-gamelist-doc` remain discovery nodes rather than catalogue subjects.

Expanded **mwenge/Llamasoft** beyond the already tracked Gridrunner, Matrix, Iridis Alpha and Ancipital records. Added Virtual Light Machine, Psychedelia/Colourspace, Hellgate, the C64/Atari 8-bit Attack of the Mutant Camels reconstructions, Voidrunner, Metagalactic Llamas, Batalyx, Sheep in Space, Revenge of the Mutant Camels, Hover Bovver, Mama Llama, Return of the Mutant Camels and an independent Uridium reconstruction. Tempest 2000 remains excluded as a catalogue subject because that repository primarily preserves/builds surviving original source; Psychedelia II is an original tribute/adaptation rather than a reconstruction.

Structured project count increased from 200 to **234**. The vs-sr-dev profile and its CD32 indexes were added as recurring discovery nodes for later auditing beyond CD32.


## 2026-09-24 — Apple II reconstruction graph and new C64/NES/Genesis static-recomp projects

Audited the user-supplied fschuhi profile plus Alien, Seven Cities of Gold, Solomon's Key, Shadowrun Defragged, Archon and BattleTech repositories.

Promoted all six named repositories: **Alien** (complete C64 disassembly plus faithful Python reimplementation and disk-analysis toolkit), **Seven Cities of Gold** (C64-to-Swift reconstruction with emulator-verified routines), **Solomon's Key** (byte-identical USA/Europe NES reconstruction), **Shadowrun Defragged** (Genesis bug-fix project backed by substantial ROM disassembly/analysis), **Archon** (relocatable C64 source-logic reconstruction), and **BattleTech: The Crescent Hawk's Inception** (native Windows static recompilation driven by a fixed 21,637-block analysis catalogue).

The fschuhi profile yielded three independent records: **a2-lode-runner** as a title-specific research/specification layer, **Robotron 2084** as an Apple II disassembly/research workbench, and **papple2** as purpose-built Apple II reverse-engineering/debugger infrastructure. The narrower **a2-hires-lab** remains a discovery aid under the profile rather than a separate catalogue record; generic/forked assembler/emulator repositories were not promoted merely for being useful dependencies.

Following a2-lode-runner's credited predecessor chain exposed **XekriRedmane** as a major Apple II reconstruction node. Promoted its byte-perfect **Lode Runner**, **Ultima I**, **Ali Baba and the Forty Thieves**, and **Drol** literate reconstructions. The profile is now a recurring discovery source for future Apple II audits.

AI evidence was recorded only where explicit: Seven Cities documents heavy Claude assistance; Solomon's Key carries Codex co-author trailers; Shadowrun Defragged explicitly documents GPT-5.6 Sol/Codex use; and the XekriRedmane reconstructions have explicit Claude project/commit evidence.

Catalogue count increased from 234 to **247**.


## 2026-09-24 — Starflight remastered successor

Audited **canadacow/starflight-reverse** against the already tracked **s-macke/starflight-reverse**. The new repository explicitly identifies the s-macke project as its background/origin, but it is not merely another copy of the recovery tree: it has become a playable remastered runtime that fully emulates Starflight's recovered Forth and assembly execution while adding a real-time Vulkan/rotoscoped/PBR presentation layer and switchable classic EGA/CGA output.

Promoted it as a separate **RE-derived reimplementation/remaster** record rather than merging the two projects. The s-macke record now notes this successor relationship, and canadacow's repository was added as a discovery node. The README explicitly describes the remaster as AI-generated, so AI usage is marked true while the tool name remains unknown rather than guessed.


## 2026-09-24 — curated display titles and subject names

Separated upstream project identity from catalogue presentation. Every current record now carries **upstream_name**, **display_title**, and **subjects**. The existing `title` field remains for compatibility/history, while Projects, Activity and RSS prefer `display_title`.

Opaque or awkward names now receive concise tracker labels that answer what the project actually is without relying on tags. Examples include **Firestaff — Dungeon Master / Chaos Strikes Back engine reconstruction**, **VS Code Amiga C/C++ debugger & profiler**, **amitools — Amiga binary, ROM & filesystem toolkit**, **PiST — Atari ST assembly IDE & debugger**, and **papple2 — Apple II reverse-engineering emulator/debugger**. Multi-subject projects such as Firestaff also carry explicit subject arrays for search.

The one-time migration updated the catalogue-state baseline in lockstep so it does not fabricate hundreds of project metadata events. Future changes to upstream/display names or subjects are material catalogue changes and will appear normally in Activity. Validation now requires non-empty upstream/display names and subjects for subject/hybrid records.


## 2026-09-24 — 0xC0DE6502, RetroRE and BBC Exile audit

Audited the 0xC0DE6502 profile, realdmx/retrore and chriskillpack/exile-beebasm.

Promoted five projects from **0xC0DE6502**: **Lode Runner — BBC Micro disassembly**, **Repton — Acorn Electron tape-protection disassembly**, **The Way of the Exploding Fist — Acorn Electron tape-loader disassembly**, **Electroniq — Acorn Electron browser emulator**, and **Electroniq — VS Code source-level Acorn Electron debugger**. The profile's Electron Elite repository was not duplicated because it is a fork of the already represented Mark Moxon Electron Elite reconstruction.

Promoted **Exile — BBC Micro disassembly** from chriskillpack. **RetroRE 6502** itself remains a discovery node rather than a project record because it is a curated index mixing original source and reverse-engineered projects. Its explicit Original/RE columns make it particularly useful for triage.

Following RetroRE immediately yielded **Choplifter — Apple II clean-room source reconstruction** by blondie7575. It is a full binary-led reconstruction whose game code is described as binary-identical, but the original custom floppy loader was intentionally replaced by a ProDOS loader, so the tracker does not mark the complete build byte-exact.

The RetroRE index exposes a much larger backlog of untracked full/partial 6502 reconstructions across Apple II, Atari 2600/8-bit, BBC Micro, C64 and NES; this has been added as an explicit discovery priority rather than bulk-promoting entries without primary-source verification.

Catalogue count increased from 248 to **255**.


## 2026-09-24 — public site renamed Retro Development Project Tracker

Renamed the public-facing site and RSS branding to **Retro Development Project Tracker** with the subtitle **Reverse engineering · reconstruction · preservation · homebrew · tooling**. The GitHub repository name and Pages URL remain unchanged to avoid unnecessary URL/repository churn.


## 2026-09-24 — additive facet filtering

Replaced the dropdown-heavy Projects and Activity filters with additive facet chips. Multiple choices inside one facet are ORed (for example Amiga + Atari ST + Amstrad CPC), while different facets combine to narrow results (for example those platforms + Game + Source reconstruction).

The internal `subject/tooling/hybrid` classification is no longer exposed as UI jargon. **Project type** presents **Retro software** and **Development tools**; hybrid records belong to both. Projects now expose additive Platform, Software type, Work and Development tool facets, with CPU/output language under More filters, while AI/Compiles/Playable/Byte exact use compact mutually exclusive Any/Yes/No/Unknown controls.

Activity was simplified to Search, Period, additive Activity type / Project type / Platform / Software type / Work / Development tool facets, and AI state. Dedicated project, author, branch and output-language filters were removed. The activity text search remains for project/subject and activity text, but no longer indexes authors or branch names.


## 2026-09-24 — CPU-family and verified runtime compatibility filtering

Moved **CPU** into the primary additive filters and normalized closely related stored variants into discovery families such as **6502 family**, **68000 family**, **x86**, Z80 and ARM. Platform filtering now considers both source and target platforms, and CPU discovery can consider source CPU, optional target CPU and verified runtime profiles, making same-architecture ports easier to find.

Added an optional **Runs on** compatibility section, deliberately separate from the broad CPU facet. It is driven only by verified `runtime_profiles` and supports minimum CPU, RAM budget and chipset compatibility. Selecting a 68020-class CPU can include a build whose documented minimum is 68000; selecting 68000 excludes a 68020-minimum build. The controls remain explicitly empty until requirements have been verified rather than inferring compatibility from source architecture.

The schema now supports optional `target_cpu` and `runtime_profiles`, validation enforces their shape, and catalogue activity treats changes to these fields as material. Activity filtering also gained the normalized CPU-family facet.


## 2026-09-24 — instant view switching

Removed unconditional Activity-feed reconstruction from Activity/Projects tab switching. The rendered Activity DOM is now retained and only marked dirty when Activity data/filter state changes; switching back to an unchanged Activity view is therefore a visibility toggle rather than a full regroup/sort/HTML rebuild. Off-screen activity-day layout is also deferred with CSS `content-visibility` to reduce the cost of showing long feeds.


## 2026-09-24 — persistent light/dark theme toggle

Added an explicit **Light/Dark** theme toggle in the site header. Light mode is now the default regardless of operating-system preference. The selected theme is restored before the stylesheet loads to avoid a theme flash and is persisted locally in the browser with `localStorage` key `retro-development-tracker.theme`. No other settings are persisted yet.


## 2026-09-24 — browser-default theme behaviour

Adjusted theme handling so an unset tracker preference follows the browser/OS `prefers-color-scheme` value. Nothing is written to storage merely by loading the site. Only an explicit user click on the Light/Dark toggle creates a persistent `localStorage` override; once present, that manual override takes precedence over browser defaults.


## 2026-09-24 — Zippy Race OCS Amiga fan conversion

Promoted **Zippy Race — OCS Amiga fan conversion** from `lantus/ZippyRace-OCS`. This is intentionally a broader-scope retro-development/homebrew record rather than a reverse-engineering record: the project's own README explicitly says **no reverse engineering or transcoding was performed** and that the game was written by hand to recreate the 1983 Irem arcade game.

The repository contains the complete C/m68k-assembly Amiga implementation, assets and build system. Its Makefile targets **68000** explicitly, while the README states that it runs at **50/60 fps on any Amiga with 1 MB**, so the record includes a verified OCS runtime profile of 68000 + 1 MB rather than inferring compatibility from the Amiga target alone. The `lantus` profile was added as a recurring Amiga/68k retro-development discovery node.

Catalogue count increased from 255 to **256**.


## 2026-09-25 — deeper cross-platform discovery pass

Read the canonical catalogue, discovery-source graph and current 180-day activity feed before searching, then expanded outward through RetroRE 6502, author profiles and primary project documentation. This pass followed the represented-platform graph rather than a fixed platform list and introduced **Atari 2600** as a first-class source platform where primary project evidence supported it.

Promoted **14 verified projects** across Atari 2600, Atari 8-bit, Commodore 64, BBC Micro and NES, together with two directly relevant BBC/6502 development tools. The additions include source reconstructions, disassemblies, binary/data analysis, a preservation-oriented emulator/debugger and a programmable tracing disassembler.

Hardware requirements remain evidence-only. **Fighter Pilot** is the only new record in this pass with a `runtime_profiles` entry because its README explicitly requires at least **48K** on named Atari 8-bit machines; no CPU minimum or other runnable requirement was inferred from platform or architecture alone.

Discovery sources were expanded for Dennis Debro, ZornsLemma, TobyLobster, nmikstas, cadaver and Crossroads 2, and the existing sarnau node now reflects the substantial Atari 8-bit archaeology cluster. Strong unpromoted follow-ups remain in the same graph, including additional sarnau Atari 8-bit analyses, Zelda/NES work and further BBC Micro disassemblies.

Catalogue count increased from 272 to **286**.


## 2026-09-25 — discovery automation landing verification

Verified the repository-side discovery landing path by pushing this commit to an `automation/discovery-*` branch and allowing `.github/workflows/land-discovery.yml` to fast-forward `main` only after confirming the branch is non-empty, zero commits behind, and based directly on the current `main`.


## 2026-09-25 — runtime-profile and status maintenance

Reviewed repository activity since the previous maintenance pass and rechecked current primary documentation for the materially changed projects.

Added evidence-backed runtime metadata for **Master of Magic — ReMoM Amiga port**: the native binary requires a 68020 or better, Kickstart/Workbench 3.1+, and 8 MB Fast RAM; AGA additionally requires 2 MB Chip RAM. AGA and 8-bit RTG are now separate runtime profiles so the RTG record does not invent an unstated Chip-RAM minimum.

Added verified runtime profiles for **Elite — native Amiga port (ataribaby42)**. The default OCS build is documented for MC68000, Kickstart 1.3, 512 KB Chip RAM plus 512 KB expansion RAM, while the explicit `cpu=68020` build is recorded separately without inferring a RAM minimum that the README does not state.

Refined **Firestaff — Dungeon Master / Chaos Strikes Back engine reconstruction** to reflect the project's own current status boundary: Dungeon Master 1 on PC DOS 3.4 is playable/source-locked, while the other named games remain verified bounded routes or active bring-up rather than being promoted to complete playability.

Updated **ZX Spectrum game disassemblies — reproducible SkoolKit archaeology** to include its new patching work: The Hobbit's optional fast-draw patch is applied on top of verified source and validated by rendering all 22 pictures and comparing whole memory afterwards.


## 2026-09-25 — persistent research indexes and queues

Converted the implicit research backlog into persistent machine-readable state.

`data/discovery-sources.json` now indexes every discovery node from `sources.md`, links already promoted projects, records review dates where the existing research log/catalogue establishes them, and turns the human Open discovery priorities into explicit stateful backlog tasks.

`data/project-audits.json` now contains one audit record for every catalogue project, separating factual unknowns from research-state unknowns across identity, classification, source/target CPU, build evidence, runtime profiles, AI evidence and project relationships. Missing evidence is still not treated as false; `needs-research`, `not-applicable` and `no-evidence-found` are distinct states.

`data/research-activity.json` provides append-only research history and is seeded from the research-oriented entries already present in this log. Validation now enforces source/task references and exact project-audit coverage. The pending-project merge tool creates an unreviewed audit placeholder for every newly added project so the index cannot silently fall behind the catalogue.


## 2026-09-25 — analyser queues and RetroRE batch

Continued preemptive discovery from the persistent research queues rather than a broad search.

Completed the title-level audit of **TheGoodDoktor/C64AnalyserProjects**, promoting the nine remaining per-game analysis states after verifying their dedicated annotation databases, saved analysis/emulator state and configuration. The C64 analyser backlog task is now complete.

Advanced **TheGoodDoktor/SpectrumAnalyserProjects** with ten especially substantive title records: Batman, Bobby Bearing, Cybernoid, Dan Dare, Everyone's A Wally, Exolon, Jack the Nipper II, Manic Miner, Ranarama and Starquake. These were selected for deep per-title analysis data and, where present, exported Z80/Skool source, Lua viewers/exporters, maps, flow graphs and decoded graphics. The broader Spectrum analyser queue remains in progress.

Advanced the **RetroRE 6502** backlog with primary-source verification of The Legend of Zelda, Final Fantasy, Contra, Balloon Fight, Jackal, Pharaoh's Curse, Rambo and Planetoid. Following Contra's own project graph also yielded **Super C**. Byte-exact status was recorded only where the primary project documentation explicitly states matching reconstruction output.

The discovery index's task-to-source links were also normalized. The initial migration's keyword-derived links were too broad; active backlog tasks now point at the actual source nodes that should drive future queue selection.

This pass adds **28 projects**, taking the catalogue from 293 to **321**.


## 2026-09-25 — Spectrum, RetroRE, Ricardo and jotd queue pass

Continued preemptive discovery from four explicit research queues.

Promoted ten more substantial **SpectrumAnalyserProjects** title states: Cobra, Auf Wiedersehen Monty, Elite, Livingstone I Presume, Thrust, Firelord, Zub, Spellbound 128K, Chase H.Q. and Cybernoid II. The pass prioritised large per-title annotation databases and, where present, custom Lua analysis/viewer tooling. The Spectrum analyser queue remains in progress.

Advanced **RetroRE 6502** with two primary-source NES reconstructions: **Super Mario Bros. 3**, whose NESASM source explicitly rebuilds the US PRG1 ROM byte-for-byte, and **Tecmo Super Bowl**, whose repository describes an exhaustive fully labelled/commented reverse engineering and byte-for-byte rebuild.

Completed the **Ricardo Quesada C64** source audit. Added **Le Mans** as a fully disassembled/patched C64 reconstruction, **Regenerator 2000** as a modern Commodore 6502 disassembler/debugger/MCP reverse-engineering workbench, and **VChar64** as substantive C64/128 asset-development tooling. Other inspected repositories were original homebrew, small misc/demo collections or mirrors; **UNP64** explicitly identifies itself as an official mirror and was not duplicated as a separate project.

Advanced the **jotd666** audit with **Xevious** and **Galaxian**, both backed by project-specific documentation explicitly describing Z80 reverse engineering and 68000 transcoding. Several other candidate repositories currently contain copied or mismatched READMEs for other games, so they remain unpromoted pending project-specific evidence rather than inheriting claims from those templates.

This pass adds **17 projects**, taking the catalogue from 321 to **338**.


## 2026-09-25 — Spectrum analyser completion and RetroRE C64/BBC/Atari batch

Finished the systematic **TheGoodDoktor/SpectrumAnalyserProjects** title audit. Promoted the final eighteen substantive game-analysis directories: Saboteur, Head Over Heels, Amaurote 128, Zynaps, Hyper Sports, Universal Hero, Target Renegade, Light Force, Wizball, Athena, Robocop, Rastan, Feud, Octan, Turrican II, Monty Is Innocent, Daley Thompson's Supertest and Tai-Pan. The remaining `ZXBasic` directory was explicitly reviewed but not promoted: it has no snapshot/established legacy subject and is largely generic baseline analysis state. The dedicated Spectrum analyser queue is now complete.

Advanced the **RetroRE 6502** backlog with nine independent primary-source projects:
- Haunted House — Atari 2600 commented disassembly;
- A View to a Kill, Chiller, Squirm, Hunchback, Wizard of Wor and Ghostbusters — C64 reverse-engineering/disassembly projects;
- Imogen and Night World — BBC Micro py8dis/BeebAsm reconstruction projects.

The Imogen and Night World repositories have no conventional README, so their build scripts were used as primary evidence: both generate reconstructed source and compare rebuilt components against original binaries. Existing canonical tracker records were preferred over alternate/older RetroRE links, so Aviator, Revs and Electron Elite were not duplicated.

Also sampled the **Mark Moxon** archaeology graph. Apple II Elite, BBC Micro cassette Elite and Elite-A are current repositories centered on original-source preservation/documentation (Elite-A's historical creation itself involved disassembly), so they remain discovery context rather than being added as new reverse-engineering records in this pass. The Mark Moxon graph task remains in progress for genuinely distinct hacks, tools and ports.

This pass adds **27 projects**, taking the catalogue from 338 to **365**.


## 2026-09-25 — Mark Moxon and Amber predecessor graph pass

Completed the main **Mark Moxon Elite hack/tool graph** audit. Added six distinct runnable projects: flicker-free Commodore 64/Plus/4 Elite, Teletext Elite, Elite 3D, Two-player Elite, Elite Universe Editor and Elite over Econet. The current original-source-only repositories and Elite Compendium variants remain discovery context rather than being misclassified as reconstruction work. `!EliteNet` was explicitly reviewed but not promoted because it is a companion Archimedes scoreboard application and the game itself is untouched.

Resolved the named **Amber predecessor** backlog using Pyrdacor's primary Ambermoon documentation. Added **Amberworld** as a historical Amberstar/Ambermoon/Albion reverse-engineering and format-tooling project, and **AmbermoonSourceror** as a Ghidra-export-to-Amiga-assembler tool. Added concrete discovery nodes for Daniel Schulz's Slothsoft Ambermoon tooling and Nico Bendlin's GitLab/Ghidra research rather than leaving them as unresolved names. Confirmed that `kermitfrog/Amberstar` is a fork of the already tracked `Pyrdacor/Amberstar`, so it was not duplicated.

Expanded the **Tetracorp** graph beyond Amiga work with **Tokimeki Memorial: Forever With You**, a documented Ghidra analysis of the 1995 Japanese PlayStation release. This also adds PlayStation as a represented source platform.

This pass adds **9 projects**, taking the catalogue from 365 to **374**.


## 2026-09-25 — Hitchhikr tooling, RetroRE Monty/Punch-Out and BBC predecessor pass

Advanced the **hitchhikr** discovery graph with three independently evidenced projects: **x68k2amiga**, an X68000-to-Amiga executable conversion/depacking utility built specifically to aid subsequent reversing; **crudNES**, a NES emulator whose runtime tracer generates disassembly and ROM-reconstruction files; and **Oktalyzer**, a complete Amiga disassembly being modernized with new replay/mixer and Vampire support.

Advanced **RetroRE 6502** with **Monty on the Run**, which provides both a documented byte-perfect C64 reconstruction and a synchronized refactored source tree, and **Mike Tyson's Punch-Out!!**, an ongoing NES reverse-engineering project whose build script reconstructs banks and checksum-compares them to the originals.

Reviewed a sample of the **BBC/Acorn predecessor graph**. Imogen, Thrust, Manic Miner, the Acorn 6502 coprocessor OS and BBC Lode Runner are already represented. `tom-seddon/exile_disassembly` explicitly describes itself as redundant because its upstream disassembly was later updated, so it was retained as discovery context rather than duplicated as another Exile record.

This pass adds **5 projects**, taking the catalogue from 374 to **379**.


## 2026-09-25 — RetroRE Mega Man 3–6 disassembly pass

Advanced the high-priority RetroRE 6502 backlog by resolving the older Raidenthequick Mega Man links to their current `refreshing-lemonade` repositories.

Promoted four NES projects: **Mega Man 3**, **Mega Man 4**, **Mega Man 5** and **Mega Man 6**. Each primary README states that the code and data disassembly is complete and rebuilds a clean NTSC-U ROM with xkas-plus; the source is complete while code commentary remains unfinished. The catalogue records the projects as complete/compilable disassemblies but deliberately leaves byte-exactness unknown because the documentation does not explicitly claim a byte-for-byte-identical output.

The RetroRE task remains in progress for the remaining Apple II, Atari 2600/8-bit, C64 and NES leads.


## 2026-09-25 — Apple II SourceGen discovery expansion

Advanced the high-priority RetroRE 6502 backlog through Andy McFadden's 6502disassembly.com project pages. Promoted seven Apple II disassembly/analysis projects: **Bomber**, **Deathmaze 5000**, **Elite**, **Phantoms Five**, **Golden Voyage / Scott Adams Adventures**, **Space Eggs** and **Stellar 7**. These provide SourceGen project sets and substantial technical analysis; build, runnable and byte-exact fields remain unknown where the project pages do not establish a verified standalone rebuild.

Then followed the SourceGen index outward beyond RetroRE and promoted nine additional archaeology targets: the **GS/OS DOS 3.3 FST**, **RDOS**, **AppleVision**, **Bill Budge's 3-D Graphics System module**, **Caverns of Freitag**, **Graphics Magician Picture Painter**, **Micro-Painter**, **Sabotage** and **Starship Commander**. This adds operating-system internals, development tooling, mixed BASIC/machine-code applications and games rather than only game disassemblies.

A persistent follow-up task now records the remaining SourceGen index (including Epoch, other Apple II titles, Atari 2600 Adventure, NES Super Mario Bros. and the arcade projects) so the source can be worked systematically and deduplicated against converted/published original listings.


## 2026-09-25 — SourceGen arcade follow-through

Continued the new 6502disassembly.com queue outside the Apple II section. Promoted **Asteroids**, **Battlezone**, **Centipede** and **Missile Command** as substantial arcade 6502 disassembly/analysis projects. Their project pages combine SourceGen project sets with project-specific binary construction and technical analysis of vector/graphics systems, hardware interfaces, revisions and game-state behavior.

Reviewed but did not promote the site's Atari 2600 **Adventure** and NES **Super Mario Bros.** pages as independent catalogue records: both explicitly describe SourceGen conversions of pre-existing disassemblies with little or no new analysis. Keeping those as source-level references avoids inflating the project count with format conversions of already-existing work.


## 2026-09-25 — SourceGen Apple II follow-through

Promoted three further Apple II SourceGen projects after primary-page review: **ABM**, **Penny Arcade** and **Epoch**. Epoch is explicitly recorded as work in progress because its listing notes that some of the mathematics remains unexplained.

The remaining first-party SourceGen item requiring a more careful provenance split is the Apple II system/peripheral ROM collection, which combines independent disassemblies with conversions of published or original listings. The persistent discovery task now records that distinction plus the site's outbound “Other Disassemblies” graph.


## 2026-09-26 — g0me3 completion and cross-platform CPU audit

Completed the 11-repository **g0me3** profile inventory. Added four further game projects: **RoboCop 3 (NES) — Back From Source reconstruction**, **Rambo (NES) — Back From Source reconstruction**, **Green Beret — FDS-to-UNROM NES conversion** and **Backgammon — FDS-to-NES cartridge conversion**. Also added **TileMapper — multi-console ROM tile-map viewer** and **ida_stuff — retro-console IDA loaders and analysis scripts** as reusable tooling. The customized FCEUX fork remains explicitly deferred until project-specific archaeology or debugging work is documented beyond its repository description.

Ran the CPU audit queue before selecting existing records and resolved ten queued CPU audit areas across five projects. Primary technical evidence now records the DOS **Pushover** executable as 16-bit x86, the original **Amiga LZX** compressor as 68000 and its released host builds as x86-64/arm64, and **L-Packer** output depackers as 68000. **Another World JS** and **hode** were explicitly marked CPU-not-applicable where their documented inputs are VM bytecode/data and their outputs are portable browser/host code, rather than inferring CPUs from platform labels.

This pass adds **6 projects**, taking the catalogue from 692 to **698**, completes the g0me3 discovery task, and reduces the unresolved project CPU queue from 189 to **184** while resolving ten individual source/target audit areas.


## 2026-09-26 — VM/toolchain CPU audit and active-project maintenance

Resolved ten further queued CPU audit areas across seven projects. **Another World — cross-port archaeology** and **Another World — cross-port source reconstruction** now explicitly treat their current AW virtual-machine bytecode inputs/outputs as native-CPU-not-applicable; the reconstruction's own PLAN excludes engine binaries and whole-port packaging from current scope. **Blues Brothers — reimplemented Titus game engine** is likewise marked source-CPU-not-applicable because it consumes original data and reimplements behavior rather than translating executable instructions.

The initial **STOS BASIC — Atari ST compiler and interpreter source** audit now records the core historical interpreter/compiler as 68000 source and output, while keeping specialized Falcon/later-CPU extensions and a reproducible modern build as separate open research. Project-local primary listings identify **Commando — Amiga arcade transcode** as Z80-derived and **Ghosts'N'Goblins** plus **Mappy** as 6809-derived.

Reviewed two upstream changes since the preceding maintenance pass. **Firestaff — Dungeon Master / Chaos Strikes Back engine reconstruction** added authentic Amiga and French-DOS DM2 runtime receipts, direct FM Towns CSB save resume, and a byte-identical Theron's Quest US source-frame comparison whose documentation explicitly limits the claim to one captured screen. **Elite — native Amiga port (ataribaby42)** advanced to its 1.81 dual-buffer instrument-reset fix with native transition regression tests; its explicit `AGENTS.md` workflow also corrects the earlier AI evidence state without guessing a particular agent product.


## 2026-09-27 — MSX, PC-98 and Atari fresh-search pass

Ran the rotating fresh-search slice across Atari 8-bit, MSX and PC-98 using repository/README search, scoped source search and web GitHub-index queries, while continuing the high-priority RetroRE queue.

Promoted eight independently evidenced projects: **Metal Gear — annotated MSX2 ROM reconstruction**, **Arkanoid — byte-exact annotated MSX disassembly**, **PC-98 Visual Novel Research — engine disassembly and format toolkit**, **lime-juice — PC-98 MES compiler/decompiler and image toolkit**, **ReC98 — bit-perfect Touhou PC-98 source reconstruction**, **Neko Project II Debug Edition — PC-98 binary debugger**, **Atari OS-B NTSC — paper-source restoration and verified ROM build**, and **Bruce Lee — annotated Atari 8-bit disassembly**.

Recorded the original Racket `tomyun/juice` as the predecessor lineage represented by lime-juice. The `milnak/atari-vcs-disassembly` root remains a discovery node because it aggregates credited sources and submodules; a new task will review its canonical components individually. `MSXDUMPTOOLS` remains a redistribution/ecosystem node rather than an independently authored project.

The separate CPU lane resolved eleven queued areas across seven existing records. DoDonPachi DaiOuJou now records its README's explicit 68000 evidence; Batman, Gradius, ALIS, PowerPacker and RNC ProPack retain empty CPU fields with precise no-evidence-found audit states instead of platform guesses; AmigaQB_extract is explicitly CPU-not-applicable as backup-data recovery tooling. The unresolved CPU queue falls from 164 to 157 projects.

This pass adds **8 projects**, taking the catalogue from 755 to **763**.
