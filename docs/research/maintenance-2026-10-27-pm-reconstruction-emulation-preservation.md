# Reconstruction, emulation and preservation maintenance

Review ten materially changed projects spanning exact reconstruction, original-platform enhancements, emulator compatibility, filesystem preservation and source-restored CP/M utilities.

Date: 2026-10-27 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- m68k-reversing-toolkit-rmtew / Build (needs-research): The tracker did not run the generator, assembler or tests. Three angle reads remain honest field gaps and substantial game semantics remain unresolved. Next check: Continue classifying the 271 unresolved record accesses and qualify behavior without promoting local exactness to complete reconstruction.
- m68k-reversing-toolkit-rmtew / Runtime profiles (needs-research): The byte-exact generation receipt does not establish a minimum Amiga CPU, RAM, chipset or ROM profile for running the original game. Next check: Add a runtime profile only when primary documentation or qualified hardware/emulator testing states a concrete minimum configuration.
- m68k-reversing-toolkit-rmtew / Relationships (needs-research): The current restoration remains within the Starglider 2 target and does not resolve the wider predecessor, successor or credited-source graph. Next check: Revisit project relationships after the bounded restoration stabilizes.
- wing-commander-kilrathi-saga-reconstruction / Target CPU (no-evidence-found): The README documents modern host operating systems but does not establish a fixed supported output CPU; none is inferred from C/C++ portability.
- wing-commander-kilrathi-saga-reconstruction / Build (needs-research): The tracker did not compile, compare or run the project. Declaration order is a matching device, not recovered original source spelling, and 1,631 strict differences remain. Next check: Track closure of the remaining strict-byte runs and require a complete build/runtime claim before promoting whole-project exactness.
- wing-commander-kilrathi-saga-reconstruction / Runtime profiles (no-evidence-found): The inspected change provides no minimum host CPU, RAM or OS profile; user-supplied game data remains required.
- firestaff-dungeon-master-engine / Build (needs-research): Coverage depends on available authenticated media and explicitly does not establish native CD boot, movement transactions or full campaign/display parity. The tracker did not run any build or media. Next check: Continue authenticated campaign and presentation validation while preserving platform- and checkpoint-specific limits.
- systemless-classic-mac-runtime / Build (reviewed): The tracker did not build or run Systemless, and the focused import test does not establish universal application compatibility.
- systemless-classic-mac-runtime / Runtime profiles (no-evidence-found): Release assets identify native architectures, but the inspected release and commit do not state minimum host CPU generation, RAM or OS versions suitable for a verified profile.
- gaberealb-parasite-eve-2-decomp / Build (reviewed): The tracker did not extract media, run the generators, compile or compare the output; one clean-build claim does not establish full decompilation completeness.
- gaberealb-parasite-eve-2-decomp / Runtime profiles (no-evidence-found): The reviewed material states no minimum PlayStation revision/accessory profile or verified host runtime minimum.
- markyturtle-newzealandstory-amiga / Build (reviewed): The tracker did not build or run the disk. Real hardware remains untested and the 50 Hz mode may fall back to 25 Hz on a busy pass.
- markyturtle-newzealandstory-amiga / Runtime profiles (no-evidence-found): The mirror cache explicitly targets 512 KiB machines, but the reviewed documentation does not state a complete minimum CPU, chip/fast RAM, chipset and Kickstart profile for the enhanced variant; no composite minimum is inferred.
- pool-of-radiance-dos-c-reconstruction / Target CPU (no-evidence-found): Portable C is the intended deliverable, but the inspected material does not establish a fixed supported output CPU architecture.
- pool-of-radiance-dos-c-reconstruction / Build (needs-research): The resolved binary was not the pinned build; the receipt explicitly is not certification, full RAM, natural route, whole-game or new recovery credit. The tracker did not run it. Next check: Continue strict routine recovery and require pinned or otherwise qualified oracle provenance before widening native-validation claims.
- pool-of-radiance-dos-c-reconstruction / Runtime profiles (no-evidence-found): The fixture names one Linux DOSBox-X executable but does not state minimum host or original-machine CPU/RAM requirements suitable for a runtime profile.
- amiga-disk-engine-darian-frey / Build (reviewed): These are upstream corpus and fuzz results. The tracker did not compile the Rust/Qt workspace, supply the corpus or execute either decoder.
- amiga-disk-engine-darian-frey / Runtime profiles (no-evidence-found): The inspected change states no minimum host CPU, RAM or OS profile for CLI or Qt operation.
- cpm86-kernel-source-reconstruction / Build (needs-research): The tracker did not build the kernel or commands. Historical GENDEF source presence does not prove exact correspondence with the patched shipped binary. Next check: Identify the shipped GENDEF revision and patch 03, then compare representative generated LIB files before claiming source restoration.
- cpm86-kernel-source-reconstruction / Runtime profiles (no-evidence-found): PC XT and V20 MBC targets are documented, but the inspected change does not establish complete minimum RAM, firmware, storage or host-emulator profiles.
- cpm86-kernel-source-reconstruction / AI (no-evidence-found): The inspected current README, GENDEF analysis commit and commit metadata contain no explicit AI contribution attribution; this bounded absence is not proof of non-use.
- gearsf7000-sega-machine-emulator / Target CPU (no-evidence-found): Windows, macOS, Linux and BSD hosts are documented, but the inspected files do not establish a supported host CPU architecture or minimum; none is inferred from C++20 or SDL3.
- gearsf7000-sega-machine-emulator / Build (reviewed): Konami, Konami SCC and ASCII 8 MegaROMs are explicitly refused; the tracker did not compile or run the emulator or validate commercial software.
- gearsf7000-sega-machine-emulator / Runtime profiles (no-evidence-found): Guest RAM layouts are not host requirements. The inspected README still does not state minimum host CPU, RAM or OS versions.
- gearsf7000-sega-machine-emulator / AI (no-evidence-found): The inspected current README and three reviewed commits contain no explicit development-AI attribution; this is a bounded evidence check, not proof of non-use.

## m68k-reversing-toolkit-rmtew

Project ID: m68k-reversing-toolkit-rmtew · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "m68k-reversing-toolkit-rmtew",
  "last_checked": "2026-10-27",
  "status": "Starglider 2 output remains byte-exact while a canonical common-prefix join restores six typed XYZ projections, reducing unresolved record accesses from 277 to 271; broader semantics remain incomplete.",
  "techniques": [
    "canonical memory-layout modeling",
    "relocation adapter qualification",
    "instruction-boundary timing probes",
    "cold-start differential analysis",
    "high-mask allocation qualification",
    "external source-package reproduction",
    "lease-lifetime instrumentation",
    "reversible range-backed semantic restoration",
    "binary-layout contract accounting",
    "operand provenance admission",
    "native reference catalogue consistency",
    "canonical custom-type prefix joining"
  ]
}
```

Expected existing project SHA256: 14f59fb8745caafbe7d00d2162d3e8aba7c880bed59075a819fed5eb791d526b

### Identity (reviewed)

M68k Reversing Toolkit remains the same generated Amiga analysis and reconstruction framework; the reviewed change advances its Starglider 2 restoration rather than creating a separate project.
- https://github.com/rmtew/amiga-reversing/commit/9c8cdbfd2a4fca323e3fcc37031a32f7d4c72780

### Classification (reviewed)

The change is bounded reconstruction/tooling work: canonical ancestry is used to retain a safe common custom pointer prefix without treating that prefix as proof of equal values, subtype, lifetime or complete semantics.
- https://github.com/rmtew/amiga-reversing/commit/9c8cdbfd2a4fca323e3fcc37031a32f7d4c72780

### Source CPU (reviewed)

The tracked Starglider 2 input remains Motorola 68000 code; no new architecture is inferred from the analysis implementation.
- https://github.com/rmtew/amiga-reversing/blob/9c8cdbfd2a4fca323e3fcc37031a32f7d4c72780/README.md

### Target CPU (reviewed)

The retained output is native Motorola 68000 assembly, verified upstream against the original binary through the existing C/vasm route.
- https://github.com/rmtew/amiga-reversing/commit/9c8cdbfd2a4fca323e3fcc37031a32f7d4c72780

### Build (needs-research)

Upstream reports 103 focused checks and 832 native tests passing. Six XYZ projections return, type conflicts in this inventory fall from nine to zero, typed accesses rise from 436 to 442, and unresolved accesses fall from 277 to 271 while the rebuilt 412,736-byte output remains exact. Limitations: The tracker did not run the generator, assembler or tests. Three angle reads remain honest field gaps and substantial game semantics remain unresolved. Next check: Continue classifying the 271 unresolved record accesses and qualify behavior without promoting local exactness to complete reconstruction.
- https://github.com/rmtew/amiga-reversing/commit/9c8cdbfd2a4fca323e3fcc37031a32f7d4c72780

### Runtime profiles (needs-research)

The byte-exact generation receipt does not establish a minimum Amiga CPU, RAM, chipset or ROM profile for running the original game. Next check: Add a runtime profile only when primary documentation or qualified hardware/emulator testing states a concrete minimum configuration.
- https://github.com/rmtew/amiga-reversing/commit/9c8cdbfd2a4fca323e3fcc37031a32f7d4c72780

### AI (reviewed)

Existing explicit Claude contribution evidence remains valid; the reviewed commit does not add a new attribution category.
- https://github.com/rmtew/amiga-reversing/commit/0806d08b49d8d7f1aa6826c40385317bbb81154c
- https://github.com/rmtew/amiga-reversing/commit/9c8cdbfd2a4fca323e3fcc37031a32f7d4c72780

### Relationships (needs-research)

The current restoration remains within the Starglider 2 target and does not resolve the wider predecessor, successor or credited-source graph. Next check: Revisit project relationships after the bounded restoration stabilizes.
- https://github.com/rmtew/amiga-reversing/commit/9c8cdbfd2a4fca323e3fcc37031a32f7d4c72780

## wing-commander-kilrathi-saga-reconstruction

Project ID: wing-commander-kilrathi-saga-reconstruction · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "wing-commander-kilrathi-saga-reconstruction",
  "last_checked": "2026-10-27",
  "status": "Working Win32 reconstruction and SDL2 port; upstream now reports 517,025 of 518,656 strict-matching bytes (99.6855%), leaving 1,631 differences in 264 runs while all 1,539 mapped functions retain their addresses."
}
```

Expected existing project SHA256: f2d89bb73140ca92f2fb4f9e686e1ed78ff4c5e37c9f9a5a6b643be9233b4acd

### Identity (reviewed)

Recovered native Win32 Wing Commander source plus SDL2 port and original-binary comparison workflow; the current work refines matching in the same reconstruction.
- https://github.com/neuromancer/wc1-re/commit/e4f4f7085ca5f06c18e20f3d0c71b1022b505ed0

### Classification (reviewed)

Incomplete byte-oriented reconstruction with a modern SDL2 port. Per-function similarity and strict byte coverage remain separate from gameplay-completeness claims.
- https://github.com/neuromancer/wc1-re/commit/e4f4f7085ca5f06c18e20f3d0c71b1022b505ed0

### Source CPU (reviewed)

The reconstructed Kilrathi Saga executable remains x86 input.
- https://github.com/neuromancer/wc1-re/blob/e4f4f7085ca5f06c18e20f3d0c71b1022b505ed0/README.md

### Target CPU (no-evidence-found)

The README documents modern host operating systems but does not establish a fixed supported output CPU; none is inferred from C/C++ portability.
- https://github.com/neuromancer/wc1-re/blob/e4f4f7085ca5f06c18e20f3d0c71b1022b505ed0/README.md

### Build (needs-research)

Upstream reorders existing locals in RestoreSpriteBackground, preserving its body and 40-byte frame while reducing differing instruction encodings from 23 to 12. The complete report reaches 517,025/518,656 strict bytes (99.6855%), 1,532/1,550 normalized exact matches and 1,519 byte-identical complete spans; make verify passes upstream. Limitations: The tracker did not compile, compare or run the project. Declaration order is a matching device, not recovered original source spelling, and 1,631 strict differences remain. Next check: Track closure of the remaining strict-byte runs and require a complete build/runtime claim before promoting whole-project exactness.
- https://github.com/neuromancer/wc1-re/commit/e4f4f7085ca5f06c18e20f3d0c71b1022b505ed0

### Runtime profiles (no-evidence-found)

The inspected change provides no minimum host CPU, RAM or OS profile; user-supplied game data remains required.
- https://github.com/neuromancer/wc1-re/blob/e4f4f7085ca5f06c18e20f3d0c71b1022b505ed0/README.md

### AI (reviewed)

The repository explicitly documents Codex and Claude use; the current matching commit does not broaden that attribution beyond evidenced work.
- https://github.com/neuromancer/wc1-re/blob/e4f4f7085ca5f06c18e20f3d0c71b1022b505ed0/README.md
- https://github.com/neuromancer/wc1-re/commit/e4f4f7085ca5f06c18e20f3d0c71b1022b505ed0

### Relationships (reviewed)

The project continues to use binary-comp for verification and retains its documented historical compatibility references; the reviewed change creates no separate component.
- https://github.com/neuromancer/wc1-re/blob/e4f4f7085ca5f06c18e20f3d0c71b1022b505ed0/README.md

## firestaff-dungeon-master-engine

Project ID: firestaff-dungeon-master-engine · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "firestaff-dungeon-master-engine",
  "last_checked": "2026-10-27",
  "status": "Firestaff v3.0.416 and current head add bounded authenticated launcher, Theron and cross-platform startup evidence while explicitly limiting picker coverage to available media and leaving full campaign/display parity open."
}
```

Expected existing project SHA256: 5b640104a931839a6823e2a3e56eb855866830dc3bb6b5d84ee469def27b4722

### Identity (reviewed)

Firestaff remains a clean-room Dungeon Master-family engine using authenticated original media across documented platform variants.
- https://github.com/yeager/firestaff/releases/tag/v3.0.416
- https://github.com/yeager/firestaff/commit/bcdd94bd06d4fe442e2429870111419e0ca57bae

### Classification (reviewed)

Clean-room cross-platform engine reconstruction. Launcher and source-trace receipts are bounded verification evidence, not proof of full campaign, display, audio or save parity.
- https://github.com/yeager/firestaff/releases/tag/v3.0.416
- https://github.com/yeager/firestaff/commit/bcdd94bd06d4fe442e2429870111419e0ca57bae

### Source CPU (reviewed)

Existing x86, m68k, HuC6280, SH-2 and 65C816 source-family decisions remain supported by the documented original-platform scope; no new CPU is established by this pass.
- https://github.com/yeager/firestaff/blob/bcdd94bd06d4fe442e2429870111419e0ca57bae/README.md

### Target CPU (reviewed)

Published v3.0.416 assets retain x86-64 and arm64 modern outputs. Asset publication is not converted into an unstated minimum CPU generation.
- https://github.com/yeager/firestaff/releases/tag/v3.0.416

### Build (needs-research)

The release and current documentation cover available authenticated alternate PC, Atari ST, Amiga and Macintosh selections from the no-game menu, original-archive immutability checks, Japanese Theron input/source-pointer evidence and qualified startup checkpoints. Limitations: Coverage depends on available authenticated media and explicitly does not establish native CD boot, movement transactions or full campaign/display parity. The tracker did not run any build or media. Next check: Continue authenticated campaign and presentation validation while preserving platform- and checkpoint-specific limits.
- https://github.com/yeager/firestaff/releases/tag/v3.0.416
- https://github.com/yeager/firestaff/commit/bcdd94bd06d4fe442e2429870111419e0ca57bae

### Runtime profiles (reviewed)

Existing evidenced Mac mini M4 and QEMU-hosted Linux x86-64 profiles remain valid. v3.0.416 publishes additional assets but does not establish a new measured minimum CPU, RAM or OS floor.
- https://github.com/yeager/firestaff/releases/tag/v3.0.416
- https://github.com/yeager/firestaff/commit/bcdd94bd06d4fe442e2429870111419e0ca57bae

### AI (reviewed)

Existing explicit Claude contribution evidence remains scoped to evidenced commits; the reviewed release metadata does not justify broadening the project-level claim.
- https://github.com/yeager/firestaff/commit/bcdd94bd06d4fe442e2429870111419e0ca57bae

### Relationships (reviewed)

DM1, Chaos Strikes Back, DM2, Nexus and Theron's Quest remain variants within the same source-faithful engine effort, with their evidence limits kept distinct.
- https://github.com/yeager/firestaff/blob/bcdd94bd06d4fe442e2429870111419e0ca57bae/README.md

## systemless-classic-mac-runtime

Project ID: systemless-classic-mac-runtime · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "systemless-classic-mac-runtime",
  "last_checked": "2026-10-27",
  "status": "Systemless 0.100.0 remains the published baseline; development head now implements QuickDraw AngleFromSlope for PowerPC applications with signed fixed-point edge-case tests through the PEF import path."
}
```

Expected existing project SHA256: 3e9abda534becc0ee16879c9a05d509da0730bc117c6c10b7b00f6b32a3fd70c

### Identity (reviewed)

Systemless remains a modern runtime for classic Macintosh APIs and m68k/PowerPC applications; the current change extends its PowerPC import dispatcher.
- https://github.com/benletchford/systemless/releases/tag/v0.100.0
- https://github.com/benletchford/systemless/commit/90ccf23aa169d90d9dec8b4b2a64b37e133dca4e

### Classification (reviewed)

Source-faithful compatibility runtime and API reimplementation, not a Macintosh system-ROM reconstruction or generic emulator snapshot.
- https://github.com/benletchford/systemless/commit/90ccf23aa169d90d9dec8b4b2a64b37e133dca4e

### Source CPU (reviewed)

The runtime continues to execute classic Macintosh m68k and PowerPC application code; the new import is specifically exercised through a synthetic PowerPC PEF application.
- https://github.com/benletchford/systemless/commit/90ccf23aa169d90d9dec8b4b2a64b37e133dca4e

### Target CPU (reviewed)

The v0.100.0 release publishes ARM64 and x86-64 native variants while WebAssembly remains part of the project scope; no new architecture is inferred from the API change.
- https://github.com/benletchford/systemless/releases/tag/v0.100.0

### Build (reviewed)

The new PEF import dispatch implements QuickDraw AngleFromSlope and tests zero, positive, negative and extreme signed 16.16 slopes while checking return-register and stack behavior. Limitations: The tracker did not build or run Systemless, and the focused import test does not establish universal application compatibility.
- https://github.com/benletchford/systemless/commit/90ccf23aa169d90d9dec8b4b2a64b37e133dca4e

### Runtime profiles (no-evidence-found)

Release assets identify native architectures, but the inspected release and commit do not state minimum host CPU generation, RAM or OS versions suitable for a verified profile.
- https://github.com/benletchford/systemless/releases/tag/v0.100.0
- https://github.com/benletchford/systemless/commit/90ccf23aa169d90d9dec8b4b2a64b37e133dca4e

### AI (reviewed)

Existing direct Claude co-author evidence remains valid; the reviewed QuickDraw commit contains no new co-author trailer.
- https://github.com/benletchford/systemless/commit/90ccf23aa169d90d9dec8b4b2a64b37e133dca4e

### Relationships (reviewed)

The QuickDraw implementation is part of the same InterfaceLib compatibility layer and does not represent a newly titled subproject.
- https://github.com/benletchford/systemless/commit/90ccf23aa169d90d9dec8b4b2a64b37e133dca4e

## gaberealb-parasite-eve-2-decomp

Project ID: gaberealb-parasite-eve-2-decomp · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "gaberealb-parasite-eve-2-decomp",
  "last_checked": "2026-10-27",
  "status": "USA PlayStation matching reconstruction; stage data now delegates per-area map, image, music and object rows to room instances while upstream reports a clean matching build."
}
```

Expected existing project SHA256: f6b17c075d6785a73df0d784835fe7f5ac80a2ec72f232de6c60bc123cbb2449

### Identity (reviewed)

Parasite Eve II USA matching reconstruction for PlayStation. The current stage/room data ownership change remains within the same title and region.
- https://github.com/GabeRealB/parasite-eve-2-decomp/commit/b6f071e3562678f1ddf84c2771d3d56ab08fbac7

### Classification (reviewed)

Original-platform matching decompilation and asset/package reconstruction, not a host port. Stage-wide and room-owned data are now represented separately without changing that classification.
- https://github.com/GabeRealB/parasite-eve-2-decomp/commit/b6f071e3562678f1ddf84c2771d3d56ab08fbac7

### Source CPU (reviewed)

The reconstructed PlayStation executable remains MIPS input.
- https://github.com/GabeRealB/parasite-eve-2-decomp/blob/b6f071e3562678f1ddf84c2771d3d56ab08fbac7/README.md

### Target CPU (reviewed)

The matching rebuild remains MIPS output for the original PlayStation target; no modern host port is established.
- https://github.com/GabeRealB/parasite-eve-2-decomp/blob/b6f071e3562678f1ddf84c2771d3d56ab08fbac7/README.md

### Build (reviewed)

Current tooling moves each room's row of stage per-area tables into that room instance, reconstructs the flattened tables when reading a stage and reports a clean matching build upstream. Limitations: The tracker did not extract media, run the generators, compile or compare the output; one clean-build claim does not establish full decompilation completeness.
- https://github.com/GabeRealB/parasite-eve-2-decomp/commit/b6f071e3562678f1ddf84c2771d3d56ab08fbac7

### Runtime profiles (no-evidence-found)

The reviewed material states no minimum PlayStation revision/accessory profile or verified host runtime minimum.
- https://github.com/GabeRealB/parasite-eve-2-decomp/blob/b6f071e3562678f1ddf84c2771d3d56ab08fbac7/README.md

### AI (reviewed)

Existing explicit Claude involvement remains scoped to evidenced project work; the current commit adds no new attribution beyond that record.
- https://github.com/GabeRealB/parasite-eve-2-decomp/commit/b6f071e3562678f1ddf84c2771d3d56ab08fbac7

### Relationships (reviewed)

Rooms and stage packages remain internal components of the same Parasite Eve II reconstruction, not separately promoted projects.
- https://github.com/GabeRealB/parasite-eve-2-decomp/commit/b6f071e3562678f1ddf84c2771d3d56ab08fbac7

## markyturtle-newzealandstory-amiga

Project ID: markyturtle-newzealandstory-amiga · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "markyturtle-newzealandstory-amiga",
  "last_checked": "2026-10-27",
  "status": "Byte-exact Amiga disassembly/rebuild plus enhanced branch; upstream now reports WinUAE tests for the corkscrew scroller, 48 KiB mirror cache and 50 Hz presentation, while real-hardware validation remains open.",
  "techniques": [
    "byte-exact disassembly rebuild",
    "frame-by-frame emulator comparison",
    "double-buffered corkscrew scrolling",
    "on-demand mirrored-frame caching",
    "interpolated 50 Hz presentation"
  ]
}
```

Expected existing project SHA256: 6c9e267a487bbed2eb245210aea0f2e1f7a810303cbd12299aa25c868adb2719

### Identity (reviewed)

The New Zealand Story Amiga disassembly and disk rebuild now also carries an enhanced hand-edited branch for optional display and memory improvements.
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/commit/98a83e1b98c61d80bdf6608c2e71124036b7583f

### Classification (reviewed)

Original-platform disassembly/reassembly with a clearly separated enhanced Amiga variant. The optional enhancements do not relabel the work as a modern host port.
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/commit/98a83e1b98c61d80bdf6608c2e71124036b7583f

### Source CPU (reviewed)

The original and enhanced Amiga assembly remain Motorola 68000-family source.
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/blob/98a83e1b98c61d80bdf6608c2e71124036b7583f/BUILDING.md

### Target CPU (reviewed)

The project continues to emit native m68k Amiga disk output; no other CPU target is introduced.
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/commit/98a83e1b98c61d80bdf6608c2e71124036b7583f

### Build (reviewed)

Upstream reports the enhanced scroller, 48 KiB mirror cache and interpolated 50 Hz play tested in WinUAE, including progress screens and return to title. The frame comparison reports identical displays for sampled frames across all 20 levels with four joystick inputs until timer phase divergence. Limitations: The tracker did not build or run the disk. Real hardware remains untested and the 50 Hz mode may fall back to 25 Hz on a busy pass.
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/commit/98a83e1b98c61d80bdf6608c2e71124036b7583f

### Runtime profiles (no-evidence-found)

The mirror cache explicitly targets 512 KiB machines, but the reviewed documentation does not state a complete minimum CPU, chip/fast RAM, chipset and Kickstart profile for the enhanced variant; no composite minimum is inferred.
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/commit/98a83e1b98c61d80bdf6608c2e71124036b7583f

### AI (reviewed)

The reviewed documentation commit explicitly carries a Claude Opus 5.5 co-author trailer and session reference; attribution remains scoped to evidenced work.
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/commit/98a83e1b98c61d80bdf6608c2e71124036b7583f

### Relationships (reviewed)

The exact rebuild and enhanced branch are variants of the same Amiga title project; proposed menu/input work remains a TODO rather than a separately promoted project.
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/commit/96983457501d34c21112f768a2cf3b6784699283

## pool-of-radiance-dos-c-reconstruction

Project ID: pool-of-radiance-dos-c-reconstruction · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "pool-of-radiance-dos-c-reconstruction",
  "last_checked": "2026-10-27",
  "status": "Incremental DOS C reconstruction still reports 286 strict routines among 331 identities; current native fixtures record DOSBox-X executable provenance for bounded 128-case RES03F1/RES0464 comparisons without adding recovery credit."
}
```

Expected existing project SHA256: 24198b391f9a16c52562effcfa145cc5c79ac48f648139a3dff6915741c85795

### Identity (reviewed)

Portable C reconstruction of the DOS v1.3 Pool of Radiance engine, using owner-supplied ignored game resources and scoped comparison oracles.
- https://github.com/huntergdavis/poolrad-decomp/blob/57764669ae521ffd4089e8883fadbd897101a823/README.md

### Classification (reviewed)

Incremental source reconstruction with bounded native-oracle validation. Provider provenance is audit hardening and does not count as an additional recovered routine.
- https://github.com/huntergdavis/poolrad-decomp/commit/57764669ae521ffd4089e8883fadbd897101a823

### Source CPU (reviewed)

The original DOS engine remains x86 input.
- https://github.com/huntergdavis/poolrad-decomp/blob/57764669ae521ffd4089e8883fadbd897101a823/README.md

### Target CPU (no-evidence-found)

Portable C is the intended deliverable, but the inspected material does not establish a fixed supported output CPU architecture.
- https://github.com/huntergdavis/poolrad-decomp/blob/57764669ae521ffd4089e8883fadbd897101a823/README.md

### Build (needs-research)

The RES0464 provenance fixture records a resolved DOSBox-X binary, version, SHA-256 and pin status. Upstream reports both phases passing 128 cases—113 returns and 15 RunError204 stops—with identical bounded CPU/stack/DS/heap captures after excluding only provider metadata. Limitations: The resolved binary was not the pinned build; the receipt explicitly is not certification, full RAM, natural route, whole-game or new recovery credit. The tracker did not run it. Next check: Continue strict routine recovery and require pinned or otherwise qualified oracle provenance before widening native-validation claims.
- https://github.com/huntergdavis/poolrad-decomp/commit/57764669ae521ffd4089e8883fadbd897101a823

### Runtime profiles (no-evidence-found)

The fixture names one Linux DOSBox-X executable but does not state minimum host or original-machine CPU/RAM requirements suitable for a runtime profile.
- https://github.com/huntergdavis/poolrad-decomp/commit/57764669ae521ffd4089e8883fadbd897101a823

### AI (reviewed)

The README explicitly assigns Claude and Codex reconstruction/data-layer work under primary-session review; attribution remains scoped to this documented workflow.
- https://github.com/huntergdavis/poolrad-decomp/blob/57764669ae521ffd4089e8883fadbd897101a823/README.md

### Relationships (reviewed)

The project retains its documented poolrad-macmaps research snapshot and DOSBox-X oracle relationship; current provider hardening creates no separate project.
- https://github.com/huntergdavis/poolrad-decomp/blob/57764669ae521ffd4089e8883fadbd897101a823/README.md

## amiga-disk-engine-darian-frey

Project ID: amiga-disk-engine-darian-frey · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "amiga-disk-engine-darian-frey",
  "last_checked": "2026-10-27",
  "status": "Active Rust/C++ Amiga disk toolkit; decoded views now cover Workbench icons and indexed, EHB, HAM and 24-bit ILBM images with upstream corpus accounting and fuzz-bounded allocation checks.",
  "techniques": [
    "data-format-analysis",
    "reimplementation",
    "whole-corpus differential measurement",
    "format-aware fuzzing",
    "byte-accounting validation"
  ]
}
```

Expected existing project SHA256: 2106d31561f254c9a1a9fd923a2848f42ce3620d2034a0431ac79e6c0e30e41b

### Identity (reviewed)

Amiga Disk Engine is a cross-platform Rust core, CLI, C ABI and Qt GUI for Amiga disks, filesystems, containers and decoded content.
- https://github.com/Darian-Frey/Amiga-Disk-Engine/commit/acdaee96caf1ccac7e2b093f81fc08381655046b

### Classification (reviewed)

Preservation and disk-analysis tooling with independently implemented format decoders; it is not a recovered Amiga application or emulator.
- https://github.com/Darian-Frey/Amiga-Disk-Engine/commit/acdaee96caf1ccac7e2b093f81fc08381655046b

### Source CPU (not-applicable)

The reviewed inputs are disk structures, Workbench icon records and ILBM image data rather than one executable architecture.
- https://github.com/Darian-Frey/Amiga-Disk-Engine/commit/acdaee96caf1ccac7e2b093f81fc08381655046b

### Target CPU (reviewed)

The existing x86-64 host output evidence remains; the decoded-format work does not establish an additional host architecture.
- https://github.com/Darian-Frey/Amiga-Disk-Engine/commit/acdaee96caf1ccac7e2b093f81fc08381655046b

### Build (reviewed)

Upstream reports 12,817/12,826 corpus icons and 4,664 ILBM pictures decoded, with 12,807 icons fully accounting for every file byte and 4,637 images consuming BODY exactly. Indexed, EHB, HAM and 24-bit images, ByteRun1 and masks are covered; two oversized-allocation cases found by fuzzing are rejected early. Limitations: These are upstream corpus and fuzz results. The tracker did not compile the Rust/Qt workspace, supply the corpus or execute either decoder.
- https://github.com/Darian-Frey/Amiga-Disk-Engine/commit/acdaee96caf1ccac7e2b093f81fc08381655046b

### Runtime profiles (no-evidence-found)

The inspected change states no minimum host CPU, RAM or OS profile for CLI or Qt operation.
- https://github.com/Darian-Frey/Amiga-Disk-Engine/commit/acdaee96caf1ccac7e2b093f81fc08381655046b

### AI (reviewed)

The decoder commit explicitly carries a Claude Opus 5.5 co-author trailer; attribution is scoped to evidenced work.
- https://github.com/Darian-Frey/Amiga-Disk-Engine/commit/acdaee96caf1ccac7e2b093f81fc08381655046b

### Relationships (reviewed)

AROS icon.library and ilbm.datatype are documented behavioral references read locally and not copied into the repository; ADFlib remains a black-box differential oracle rather than a linked dependency.
- https://github.com/Darian-Frey/Amiga-Disk-Engine/commit/acdaee96caf1ccac7e2b093f81fc08381655046b

## cpm86-kernel-source-reconstruction

Project ID: cpm86-kernel-source-reconstruction · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "cpm86-kernel-source-reconstruction",
  "last_checked": "2026-10-27",
  "status": "Reconstructed CP/M-86 kernel and command distribution; HDMAINT source has been added, while GENDEF now has an explicit analysis record and remains a shipped binary with source reconstruction deferred.",
  "techniques": [
    "DOS utility source porting",
    "floppy formatter reconstruction",
    "annotated command disassembly",
    "historical source-to-binary provenance analysis"
  ]
}
```

Expected existing project SHA256: 8de6ec8a674ff6a6582f117e61e4d2d27f2b5ab2177d7c306c4f155274af6c0f

### Identity (reviewed)

CP/M-86 1.1 reconstructed kernel and command distribution for IBM PC XT, emulators and V20 MBC, with frozen, annotated and experimental source sets.
- https://github.com/tsupplis/cpm86-kernel/blob/90b7dffba94fdbf0285113182c24e22fe69dce20/README.md
- https://github.com/tsupplis/cpm86-kernel/commit/90b7dffba94fdbf0285113182c24e22fe69dce20

### Classification (reviewed)

Kernel and command source restoration combining disassembly recovery, historical-source adaptation and original binaries. GENDEF is correctly retained as analyzed/deferred rather than claimed reconstructed.
- https://github.com/tsupplis/cpm86-kernel/blob/90b7dffba94fdbf0285113182c24e22fe69dce20/README.md
- https://github.com/tsupplis/cpm86-kernel/commit/90b7dffba94fdbf0285113182c24e22fe69dce20

### Source CPU (reviewed)

The recovered kernel and CP/M-86 command binaries remain 8086-family input; GENDEF's historical archive is explicitly MP/M-86 material whose exact binary correspondence is not yet established.
- https://github.com/tsupplis/cpm86-kernel/blob/90b7dffba94fdbf0285113182c24e22fe69dce20/README.md
- https://github.com/tsupplis/cpm86-kernel/commit/90b7dffba94fdbf0285113182c24e22fe69dce20

### Target CPU (reviewed)

The documented native outputs remain 8086/8088 and NEC V20 variants. GENDEF can emit 8086/8088 or Z80/8080/8085 assembly definitions, but those text outputs are not added as executable target CPUs.
- https://github.com/tsupplis/cpm86-kernel/blob/90b7dffba94fdbf0285113182c24e22fe69dce20/README.md
- https://github.com/tsupplis/cpm86-kernel/commit/90b7dffba94fdbf0285113182c24e22fe69dce20

### Build (needs-research)

README now lists HDMAINT 1.1 as reverse-engineered and source-built. GENDEF analysis documents its .DEF-to-.LIB role, historical PL/M-86 modules and build procedure, but explicitly says reconstruction is deferred, no source build/Makefile exists and no sample input has been run. Limitations: The tracker did not build the kernel or commands. Historical GENDEF source presence does not prove exact correspondence with the patched shipped binary. Next check: Identify the shipped GENDEF revision and patch 03, then compare representative generated LIB files before claiming source restoration.
- https://github.com/tsupplis/cpm86-kernel/blob/90b7dffba94fdbf0285113182c24e22fe69dce20/README.md
- https://github.com/tsupplis/cpm86-kernel/commit/90b7dffba94fdbf0285113182c24e22fe69dce20

### Runtime profiles (no-evidence-found)

PC XT and V20 MBC targets are documented, but the inspected change does not establish complete minimum RAM, firmware, storage or host-emulator profiles.
- https://github.com/tsupplis/cpm86-kernel/blob/90b7dffba94fdbf0285113182c24e22fe69dce20/README.md

### AI (no-evidence-found)

The inspected current README, GENDEF analysis commit and commit metadata contain no explicit AI contribution attribution; this bounded absence is not proof of non-use.
- https://github.com/tsupplis/cpm86-kernel/blob/90b7dffba94fdbf0285113182c24e22fe69dce20/README.md
- https://github.com/tsupplis/cpm86-kernel/commit/90b7dffba94fdbf0285113182c24e22fe69dce20

### Relationships (reviewed)

The project depends on cpm86-crossdev, imports or adapts historical Digital Research/Microsoft tools and records GENDEF's MP/M-86 source archive as evidence rather than a completed new subproject.
- https://github.com/tsupplis/cpm86-kernel/blob/90b7dffba94fdbf0285113182c24e22fe69dce20/README.md
- https://github.com/tsupplis/cpm86-kernel/commit/90b7dffba94fdbf0285113182c24e22fe69dce20

## gearsf7000-sega-machine-emulator

Project ID: gearsf7000-sega-machine-emulator · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "gearsf7000-sega-machine-emulator",
  "last_checked": "2026-10-27",
  "status": "Desktop SG-1000/SC-3000/SF-7000 and related emulator/debugger; MSX1 support now includes two joysticks, logical cartridge breakpoints and ASCII 16 MegaROM banking while other MegaROM mappers remain unsupported.",
  "techniques": [
    "whole-machine emulation",
    "cycle and peripheral modeling",
    "save-state instrumentation",
    "debug-event publication",
    "heuristic cartridge-mapper identification"
  ]
}
```

Expected existing project SHA256: add147e1ee2a832ba3b6fdd9a2949ee70c22b648299faee894e23b96199641be

### Identity (reviewed)

GearSF7000 remains a desktop Sega-family emulator/debugger derived from GearColeco, with expanding MSX1 and Sord M5 coverage in the same application.
- https://github.com/siriokds/GearSF7000-devel/commit/2ce8f97b7c3720c1433b2a97597943e5af6aea5d

### Classification (reviewed)

Substantial whole-machine emulator and debugger, not a game-specific wrapper. MSX1 is another modeled guest family rather than a separately titled project.
- https://github.com/siriokds/GearSF7000-devel/commit/2ce8f97b7c3720c1433b2a97597943e5af6aea5d

### Source CPU (reviewed)

The modeled SG-1000, SC-3000, ColecoVision, MSX1 and Sord M5 machines use the documented Z80 guest core; the new mapper changes cartridge banking rather than CPU scope.
- https://github.com/siriokds/GearSF7000-devel/blob/2ce8f97b7c3720c1433b2a97597943e5af6aea5d/README.md

### Target CPU (no-evidence-found)

Windows, macOS, Linux and BSD hosts are documented, but the inspected files do not establish a supported host CPU architecture or minimum; none is inferred from C++20 or SDL3.
- https://github.com/siriokds/GearSF7000-devel/blob/2ce8f97b7c3720c1433b2a97597943e5af6aea5d/README.md

### Build (reviewed)

MSX1 now models AY-port joysticks, directs host keys to joystick profiles when keyboard mode is off and matches logical cartridge execution breakpoints. ASCII 16 MegaROM support adds two 16 KiB bank windows, manual/MCP selection, save-state banks and bounded auto-detection for 32 KiB–4 MiB images. Limitations: Konami, Konami SCC and ASCII 8 MegaROMs are explicitly refused; the tracker did not compile or run the emulator or validate commercial software.
- https://github.com/siriokds/GearSF7000-devel/commit/2dd56922d35bd690fd6ee3fb85df30c6e217abd0
- https://github.com/siriokds/GearSF7000-devel/commit/a89a9105a6c8158a224505035183fc8bdb93a086
- https://github.com/siriokds/GearSF7000-devel/commit/2ce8f97b7c3720c1433b2a97597943e5af6aea5d

### Runtime profiles (no-evidence-found)

Guest RAM layouts are not host requirements. The inspected README still does not state minimum host CPU, RAM or OS versions.
- https://github.com/siriokds/GearSF7000-devel/blob/2ce8f97b7c3720c1433b2a97597943e5af6aea5d/README.md

### AI (no-evidence-found)

The inspected current README and three reviewed commits contain no explicit development-AI attribution; this is a bounded evidence check, not proof of non-use.
- https://github.com/siriokds/GearSF7000-devel/blob/2ce8f97b7c3720c1433b2a97597943e5af6aea5d/README.md
- https://github.com/siriokds/GearSF7000-devel/commit/2ce8f97b7c3720c1433b2a97597943e5af6aea5d

### Relationships (reviewed)

GearColeco remains the credited foundation; imported Clock Signal Z80 and blueMSX-derived modules retain their separate provenance. MSX additions remain part of GearSF7000 rather than a forked product.
- https://github.com/siriokds/GearSF7000-devel/blob/2ce8f97b7c3720c1433b2a97597943e5af6aea5d/README.md

## Source ids

```json
[
  "github-rmtew",
  "wide-20261018b-wing-commander-kilrathi-saga-reconstruction",
  "github-yeager-firestaff",
  "wide-20261018d-systemless-classic-mac-runtime",
  "github-gaberealb-parasite-eve-2-decomp",
  "github-markyturtle-newzealandstory-amiga",
  "pass25-pool-of-radiance-dos-c-reconstruction",
  "github-darian-frey-amiga-disk-engine",
  "wide-20261018t-cpm86-kernel-source-reconstruction",
  "github-siriokds-gearsf7000-devel"
]
```

## Research event notes

The CPU audit queue returned zero unresolved source or target CPU areas before project selection, so no architecture or minimum-hardware values were invented to meet a quota. Primary commit diffs, pinned documentation and release metadata were inspected. No upstream program, ROM, disk image, compiler, emulator, game or test suite was built or executed by the tracker; exactness, corpus and runtime results remain attributed upstream claims.
