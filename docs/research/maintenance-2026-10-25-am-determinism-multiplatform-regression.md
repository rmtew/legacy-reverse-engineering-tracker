# Review eight material upstream changes across emulator determinism, disassembly-derived distribution builds, reconstruction validation, native Apple II probes, gameplay progress and retro-analysis tooling.

Review eight material upstream changes across emulator determinism, disassembly-derived distribution builds, reconstruction validation, native Apple II probes, gameplay progress and retro-analysis tooling.

Date: 2026-10-25 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- snow-classic-mac-emulator / Runtime profiles (no-evidence-found): The deterministic floppy-noise control adds no minimum host CPU, RAM or OS evidence, so no runtime profile is inferred.
- snow-classic-mac-emulator / AI (no-evidence-found): Bounded README and current commit inspection found no explicit development-AI attribution. This does not establish non-use.
- simcity-spectrum-z80-suborb / Target CPU (no-evidence-found): The reviewed distribution and per-machine documentation establish output platforms but do not explicitly establish a processor architecture for every produced variant. No target CPU is inferred from platform names, z88dk or shared source.
- simcity-spectrum-z80-suborb / Runtime profiles (no-evidence-found): Per-platform documentation records media, display, audio and file-system behavior, but the reviewed change does not state verified minimum CPU, RAM, ROM or machine revisions. No runtime minimum is inferred.
- simcity-spectrum-z80-suborb / AI (no-evidence-found): No explicit development-AI disclosure was found in the reviewed commit and distribution documentation; non-use is not established.
- touhou3-pc98-reconstruction / Runtime profiles (no-evidence-found): The cold-product and guest-model checks are reconstruction evidence, not a verified minimum PC-98 runtime profile.
- pom2games-native-apple-ii-collection / Source CPU (no-evidence-found): The README and Snake header identify POM1 Apple-1/GEN2 versions as predecessors, and Chess documents reused POM1 rules code. Those predecessor files were not independently inspected, so no source CPU is inferred from the target assembly or Apple-1 label.
- amberstar-amber-framework / Source CPU (no-evidence-found): Reviewed project documentation identifies legacy Atari ST, Amiga, DOS data or game heritage, but does not establish analyzed original CPU instructions; architecture is not inferred from the platform alone.
- amberstar-amber-framework / Target CPU (no-evidence-found): Reviewed source/build documentation names platforms or language/runtime but no explicit output CPU architecture; no target CPU is inferred from Java, C#, C/C++, or a portable framework.
- amberstar-amber-framework / Runtime profiles (no-evidence-found): The gameplay slice adds no explicit minimum host CPU, RAM, OS or mobile-device profile.
- moria8-6502-multiplatform / Source CPU (no-evidence-found): The documented source lineages are VMS Pascal and C Umoria; no original executable ISA is established by the reviewed material, so source_cpu remains empty.
- neost-atari-emulator / Relationships (needs-research): The current change does not resolve the existing predecessor, successor, fork and credited-source relationship gap. Next check: Check predecessor, successor, fork and credited-source relationships.
- ghidra-retro-machines / Runtime profiles (no-evidence-found): The analyzer change adds no minimum host CPU, RAM or OS evidence; Ghidra/JDK software prerequisites remain distinct from hardware minima.

## snow-classic-mac-emulator

Project ID: snow-classic-mac-emulator · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "snow-classic-mac-emulator",
  "last_checked": "2026-10-25",
  "status": "Primary source now includes seedable deterministic weak-bit and not-ready-drive noise for reproducible floppy-controller tests; independent build/run not performed.",
  "techniques": [
    "deterministic weak-bit and drive-noise replay"
  ]
}
```

Expected existing project SHA256: 3583cce0ee445e15312ed3086926e3cd78e409c2c1bc5a3840016f8011076861

### Identity (reviewed)

Hardware-level Rust Macintosh emulator with integrated disassembly, breakpoints, watchpoints, trap/history viewers and flux/bitstream disk support.
- https://github.com/twvd/snow/blob/f2b2e3c48251641ed317b5799d9d159141dd06bc/README.md
- https://github.com/twvd/snow/blob/f2b2e3c48251641ed317b5799d9d159141dd06bc/docs/BUILDING.md
- https://github.com/twvd/snow/commit/e2cdbb9904b7bb0f7b546ccfc762de55dee11723

### Classification (reviewed)

Inspected IWM register/edge-driven controller code and compact-Mac bus implementation. README lists 128K through IIx/SE30/Portable/PowerBook models, 68000/68020/68030 and PMMU/FPU support. Peripherals and debugging establish a general research tool, not an application-specific wrapper. MIT licence for Snow; README acknowledges Musashi/MAME as reference and separately attributed components including Fluxfox and BlueSCSI Toolbox.
- https://github.com/twvd/snow/blob/f2b2e3c48251641ed317b5799d9d159141dd06bc/README.md
- https://github.com/twvd/snow/blob/f2b2e3c48251641ed317b5799d9d159141dd06bc/docs/BUILDING.md
- https://github.com/twvd/snow/commit/e2cdbb9904b7bb0f7b546ccfc762de55dee11723

### Source CPU (reviewed)

Documented source/input platforms: Macintosh. Processor scope: m68k.
- https://github.com/twvd/snow/blob/f2b2e3c48251641ed317b5799d9d159141dd06bc/README.md
- https://github.com/twvd/snow/blob/f2b2e3c48251641ed317b5799d9d159141dd06bc/docs/BUILDING.md
- https://github.com/twvd/snow/commit/e2cdbb9904b7bb0f7b546ccfc762de55dee11723

### Target CPU (reviewed)

No fixed target CPU is established; portability of the implementation language is not proof of supported architectures.
- https://github.com/twvd/snow/blob/f2b2e3c48251641ed317b5799d9d159141dd06bc/README.md
- https://github.com/twvd/snow/blob/f2b2e3c48251641ed317b5799d9d159141dd06bc/docs/BUILDING.md
- https://github.com/twvd/snow/commit/e2cdbb9904b7bb0f7b546ccfc762de55dee11723

### Build (reviewed)

Upstream adds SetFloppyWeakBitsSeed and a serializable SplitMix64 path covering SWIM/IWM weak-bit zero sequences and per-drive not-ready garbage; clearing the seed restores nondeterministic behavior. This is a deterministic test-control feature, not an independent compatibility result. The tracker did not compile or run Snow.
- https://github.com/twvd/snow/blob/f2b2e3c48251641ed317b5799d9d159141dd06bc/README.md
- https://github.com/twvd/snow/blob/f2b2e3c48251641ed317b5799d9d159141dd06bc/docs/BUILDING.md
- https://github.com/twvd/snow/commit/e2cdbb9904b7bb0f7b546ccfc762de55dee11723

### Runtime profiles (no-evidence-found)

The deterministic floppy-noise control adds no minimum host CPU, RAM or OS evidence, so no runtime profile is inferred.
- https://github.com/twvd/snow/blob/f2b2e3c48251641ed317b5799d9d159141dd06bc/README.md
- https://github.com/twvd/snow/blob/f2b2e3c48251641ed317b5799d9d159141dd06bc/docs/BUILDING.md
- https://github.com/twvd/snow/commit/e2cdbb9904b7bb0f7b546ccfc762de55dee11723

### AI (no-evidence-found)

Bounded README and current commit inspection found no explicit development-AI attribution. This does not establish non-use.
- https://github.com/twvd/snow/blob/f2b2e3c48251641ed317b5799d9d159141dd06bc/README.md
- https://github.com/twvd/snow/blob/f2b2e3c48251641ed317b5799d9d159141dd06bc/docs/BUILDING.md
- https://github.com/twvd/snow/commit/e2cdbb9904b7bb0f7b546ccfc762de55dee11723

### Relationships (reviewed)

New implementation with own hardware-level model and debugger; bounded screen found no tracked Snow equivalent. Source references are not a claim that Snow is a fork of MAME or Musashi.
- https://github.com/twvd/snow/blob/f2b2e3c48251641ed317b5799d9d159141dd06bc/README.md
- https://github.com/twvd/snow/blob/f2b2e3c48251641ed317b5799d9d159141dd06bc/docs/BUILDING.md
- https://github.com/twvd/snow/commit/e2cdbb9904b7bb0f7b546ccfc762de55dee11723

## simcity-spectrum-z80-suborb

Project ID: simcity-spectrum-z80-suborb · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "build": {
    "byte_exact": null,
    "compilable": true,
    "playable": null,
    "runnable": true
  },
  "id": "simcity-spectrum-z80-suborb",
  "last_checked": "2026-10-25",
  "status": "ZX Spectrum disassembly now underpins v1.1.0 distribution builds for Aquarius+, Z88, Mitsubishi Multi 8, PC-8801 and SAM Coupé; tracker-side build/run not performed.",
  "tags": [
    "ZX Spectrum",
    "Aquarius+",
    "Cambridge Z88",
    "Mitsubishi Multi 8",
    "PC-8801",
    "SAM Coupé"
  ],
  "target_platforms": [
    "ZX Spectrum",
    "Aquarius+",
    "Cambridge Z88",
    "Mitsubishi Multi 8",
    "PC-8801",
    "SAM Coupé"
  ],
  "techniques": [
    "shared simulation with platform-specific display, input, sound and file layers",
    "multi-target distribution packaging"
  ],
  "types": [
    "game disassembly",
    "multi-platform port"
  ],
  "work_kinds": [
    "disassembly",
    "reverse-engineering-derived-port"
  ]
}
```

Expected existing project SHA256: c4beb69e9b031b471bf4bea9a7cf9a3bdfb72c07645033d8050f76ab38f92a79

### Identity (reviewed)

The repository is now a multi-platform Sim City port rooted in the ZX Spectrum disassembly. The v1.1.0 distribution target packages separately documented Aquarius+, Z88, Mitsubishi Multi 8, PC-8801 and SAM Coupé outputs; these are one shared implementation, not separate projects.
- https://github.com/suborb/simcity_z80/commit/3409dc87b3a117a79378c93c2388ff6c3be27d25

### Classification (reviewed)

README documentation says the original simulation is retained while each machine rewrites screen, keyboard, sound and file handling. This is a disassembly-derived multi-platform port rather than analysis-only work.
- https://github.com/suborb/simcity_z80/commit/3409dc87b3a117a79378c93c2388ff6c3be27d25

### Source CPU (reviewed)

The existing Z80 source-CPU decision remains tied to the inspected ZX Spectrum disassembly; the new ports do not change that historical input architecture.
- https://github.com/suborb/simcity_z80/commit/3409dc87b3a117a79378c93c2388ff6c3be27d25

### Target CPU (no-evidence-found)

The reviewed distribution and per-machine documentation establish output platforms but do not explicitly establish a processor architecture for every produced variant. No target CPU is inferred from platform names, z88dk or shared source.
- https://github.com/suborb/simcity_z80/commit/3409dc87b3a117a79378c93c2388ff6c3be27d25

### Build (reviewed)

The new Make dist target and make_dist.py create runnable distribution archives with machine-specific launch files and README material for Aquarius+, Z88, Mitsubishi Multi 8, PC-8801 and SAM Coupé; GitHub also publishes v1.1.0 as a multi-platform release. compilable/runnable are upstream-supported claims only: the tracker did not build, launch or play any package.
- https://github.com/suborb/simcity_z80/commit/3409dc87b3a117a79378c93c2388ff6c3be27d25

### Runtime profiles (no-evidence-found)

Per-platform documentation records media, display, audio and file-system behavior, but the reviewed change does not state verified minimum CPU, RAM, ROM or machine revisions. No runtime minimum is inferred.
- https://github.com/suborb/simcity_z80/commit/3409dc87b3a117a79378c93c2388ff6c3be27d25

### AI (no-evidence-found)

No explicit development-AI disclosure was found in the reviewed commit and distribution documentation; non-use is not established.
- https://github.com/suborb/simcity_z80/commit/3409dc87b3a117a79378c93c2388ff6c3be27d25

### Relationships (reviewed)

The five new output packages share the same repository, retained simulation and disassembly lineage. They remain one catalogue project rather than five inflated records.
- https://github.com/suborb/simcity_z80/commit/3409dc87b3a117a79378c93c2388ff6c3be27d25

## touhou3-pc98-reconstruction

Project ID: touhou3-pc98-reconstruction · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "touhou3-pc98-reconstruction",
  "last_checked": "2026-10-25",
  "status": "403 exact MAIN functions / 65,198 exact owned bytes and 97.54% reviewed MAIN CODE; shared OP/MAINL input producers now have separately bounded cold-product and guest-model validation without changing whole-game exactness.",
  "techniques": [
    "cold-build exact ownership accounting",
    "guarded native-byte semantic mutation controls",
    "controlled far-call group experiments",
    "non-fixup raw-byte comparison",
    "shared-source cold-product ownership validation"
  ]
}
```

Expected existing project SHA256: c9bef207beb8f700d894b9f005b03ef8b2defde09fb0d1958e7c701d66455022

### Identity (reviewed)

Scoped source recovery of MAIN, OP, MAINL and ZUN artifacts. README separates exact owned functions from source-present work and says whole-game reconstruction remains unfinished. The new candidates remain within the same scoped MAIN/OP/MAINL/ZUN recovery; neither controlled layout experiments nor candidate bodies expand the exact-function ledger.
- https://github.com/N0zoM1z0/th03
- https://github.com/N0zoM1z0/th03/blob/HEAD/README.md
- https://github.com/N0zoM1z0/th03/commit/0285623896adc8ecc5bf4ba8359b345a4a01cd84
- https://github.com/N0zoM1z0/th03/commit/9f950dacbc46e65649f90ded29e494c8a5c3b253
- https://github.com/N0zoM1z0/th03/commit/df4b1071c1e8312d85f1b0c978c1c99cc8396967

### Classification (reviewed)

Scope: source-reconstruction / game. Primary README, repository file layout and selected implementation files were reviewed.
- https://github.com/N0zoM1z0/th03
- https://github.com/N0zoM1z0/th03/blob/HEAD/README.md
- https://github.com/N0zoM1z0/th03/commit/df4b1071c1e8312d85f1b0c978c1c99cc8396967

### Source CPU (reviewed)

Documented input architecture: x86.
- https://github.com/N0zoM1z0/th03
- https://github.com/N0zoM1z0/th03/blob/HEAD/README.md
- https://github.com/N0zoM1z0/th03/commit/df4b1071c1e8312d85f1b0c978c1c99cc8396967

### Target CPU (reviewed)

Target architecture x86. Host ports and minimum variants are not inferred from source CPU.
- https://github.com/N0zoM1z0/th03
- https://github.com/N0zoM1z0/th03/blob/HEAD/README.md
- https://github.com/N0zoM1z0/th03/commit/df4b1071c1e8312d85f1b0c978c1c99cc8396967

### Build (reviewed)

The new shared input source owns nine functions / 367 CODE bytes in each of OP and MAINL. Upstream reports two-source cold products reproducing 32 OP and 938 MAINL outputs plus independent 2,218-case-per-image guest models at two loads, with 19 mutations rejected per product. The author explicitly scopes this within each product and does not add whole-game byte percentage, canonical packed-file unit offsets or whole-product acceptance. The tracker did not compile, execute or byte-compare the revision.
- https://github.com/N0zoM1z0/th03/blob/2582551ae27692e93cd6652656cf771da7da1084/README.md
- https://github.com/N0zoM1z0/th03/commit/2582551ae27692e93cd6652656cf771da7da1084
- https://github.com/N0zoM1z0/th03/commit/0285623896adc8ecc5bf4ba8359b345a4a01cd84
- https://github.com/N0zoM1z0/th03/commit/9f950dacbc46e65649f90ded29e494c8a5c3b253
- https://github.com/N0zoM1z0/th03/commit/df4b1071c1e8312d85f1b0c978c1c99cc8396967

### Runtime profiles (no-evidence-found)

The cold-product and guest-model checks are reconstruction evidence, not a verified minimum PC-98 runtime profile.
- https://github.com/N0zoM1z0/th03
- https://github.com/N0zoM1z0/th03/blob/HEAD/README.md
- https://github.com/N0zoM1z0/th03/commit/df4b1071c1e8312d85f1b0c978c1c99cc8396967

### AI (reviewed)

Project-scoped agent instructions/configuration provide an AI-use signal; the particular agent is not inferred.
- https://github.com/N0zoM1z0/th03
- https://github.com/N0zoM1z0/th03/blob/HEAD/README.md
- https://github.com/N0zoM1z0/th03/commit/df4b1071c1e8312d85f1b0c978c1c99cc8396967

### Relationships (reviewed)

Checked current catalogue, source and decision URLs and related titles. Scoped source recovery of MAIN, OP, MAINL and ZUN artifacts. README separates exact owned functions from source-present work and says whole-game reconstruction remains unfinished.
- https://github.com/N0zoM1z0/th03
- https://github.com/N0zoM1z0/th03/blob/HEAD/README.md
- https://github.com/N0zoM1z0/th03/commit/df4b1071c1e8312d85f1b0c978c1c99cc8396967

## pom2games-native-apple-ii-collection

Project ID: pom2games-native-apple-ii-collection · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "pom2games-native-apple-ii-collection",
  "last_checked": "2026-10-25",
  "status": "Native Apple II collection; POM2 facade tests now exercise Apple //c and AppleMouse II firmware paths plus register, go and call control across game probes.",
  "techniques": [
    "SMALLDOS format analysis",
    "WOZ/A2R flux decoding",
    "6502 voxel ray casting",
    "reference-model differential testing",
    "ROM-probed crafting reconstruction",
    "resident ProDOS module architecture",
    "DHGR interface reconstruction",
    "joystick UI navigation",
    "ProDOS pre-game map program",
    "POM2 real-firmware integration testing"
  ]
}
```

Expected existing project SHA256: 4d792d290ea2a654357eb752323a49db509d3ae29406b18253b7da4b26b275f2

### Identity (reviewed)

The repository-level collection now includes the separately titled Wilderness reconstruction; it is retained within the established collection record rather than counted as a duplicate repository project.
- https://github.com/habib256/pom2games/blob/main/README.md
- https://github.com/habib256/pom2games/commit/996971397f77a62c49aef92890dac1d69b5cc338
- https://github.com/habib256/pom2games/commit/107307a5fdc74f02af41676785524443929d7e6f

### Classification (reviewed)

Neowilderness remains a reconstruction-informed subject inside the established mixed POM2 collection; its original-homebrew siblings are not relabelled as reverse-engineered.
- https://github.com/habib256/pom2games/commit/f07e562562ab46127de6b99f2b3bc2cd8edca605
- https://github.com/habib256/pom2games/blob/main/neowilderness/README.md
- https://github.com/habib256/pom2games/commit/107307a5fdc74f02af41676785524443929d7e6f

### Source CPU (no-evidence-found)

The README and Snake header identify POM1 Apple-1/GEN2 versions as predecessors, and Chess documents reused POM1 rules code. Those predecessor files were not independently inspected, so no source CPU is inferred from the target assembly or Apple-1 label.
- https://github.com/habib256/pom2games/blob/29909a924977e84636b4000d7341beafb6e3d288/README.md
- https://github.com/habib256/pom2games/blob/29909a924977e84636b4000d7341beafb6e3d288/arkabreakout/src/game.s
- https://github.com/habib256/pom2games/blob/29909a924977e84636b4000d7341beafb6e3d288/arkabreakout/Makefile
- https://github.com/habib256/pom2games/blob/29909a924977e84636b4000d7341beafb6e3d288/chess/README.md
- https://github.com/habib256/pom2games/blob/29909a924977e84636b4000d7341beafb6e3d288/snake/src/snake.c
- https://github.com/habib256/pom2games/blob/29909a924977e84636b4000d7341beafb6e3d288/chromabreak/src/boot.s
- https://github.com/habib256/pom2games/blob/29909a924977e84636b4000d7341beafb6e3d288/chromabreak/Makefile
- https://github.com/habib256/pom2games/blob/29909a924977e84636b4000d7341beafb6e3d288/LICENSE
- https://github.com/habib256/pom2games/commit/107307a5fdc74f02af41676785524443929d7e6f

### Target CPU (reviewed)

Arkabreakout’s game.s explicitly specifies NMOS 6502 and contains native gameplay assembly. ChromaBreak’s Makefile passes --cpu 65c02; boot.s starts with a 6502 CPU probe and then selects .setcpu "65C02", rejecting an NMOS IIe. These establish separate 6502 and 65C02 outputs, not a single machine minimum.
- https://github.com/habib256/pom2games/blob/29909a924977e84636b4000d7341beafb6e3d288/README.md
- https://github.com/habib256/pom2games/blob/29909a924977e84636b4000d7341beafb6e3d288/arkabreakout/src/game.s
- https://github.com/habib256/pom2games/blob/29909a924977e84636b4000d7341beafb6e3d288/arkabreakout/Makefile
- https://github.com/habib256/pom2games/blob/29909a924977e84636b4000d7341beafb6e3d288/chess/README.md
- https://github.com/habib256/pom2games/blob/29909a924977e84636b4000d7341beafb6e3d288/snake/src/snake.c
- https://github.com/habib256/pom2games/blob/29909a924977e84636b4000d7341beafb6e3d288/chromabreak/src/boot.s
- https://github.com/habib256/pom2games/blob/29909a924977e84636b4000d7341beafb6e3d288/chromabreak/Makefile
- https://github.com/habib256/pom2games/blob/29909a924977e84636b4000d7341beafb6e3d288/LICENSE
- https://github.com/habib256/pom2games/commit/107307a5fdc74f02af41676785524443929d7e6f

### Build (reviewed)

The POM2 facade delivery adds register/go/call controls and wires make test probes across Arkabreakout, Pinball and Wargalaga II. Arkabreakout's probe exercises Apple //c and card variants against AppleMouse II firmware, including detection, coordinates, launch/laser/menu input, suppression, DOS exit and display-mode invariants after each CPU instruction. These are upstream tests; the tracker did not build or run them.
- https://github.com/habib256/pom2games/commit/d1b369198dbeb50be199be735d1831ca4d417f71
- https://github.com/habib256/pom2games/commit/107307a5fdc74f02af41676785524443929d7e6f

### Runtime profiles (reviewed)

The new real-firmware and //c probes strengthen test coverage but do not change the existing author-stated Apple II memory/storage profiles or establish a lower minimum.
- https://github.com/habib256/pom2games/blob/main/neowilderness/README.md
- https://github.com/habib256/pom2games/commit/f07e562562ab46127de6b99f2b3bc2cd8edca605
- https://github.com/habib256/pom2games/commit/d1b369198dbeb50be199be735d1831ca4d417f71
- https://github.com/habib256/pom2games/commit/107307a5fdc74f02af41676785524443929d7e6f

### AI (reviewed)

The facade merge is explicitly co-authored by Claude Opus 5.5, consistent with the existing project-level Claude attribution; this remains development evidence, separate from any in-game AI.
- https://github.com/habib256/pom2games/commit/f07e562562ab46127de6b99f2b3bc2cd8edca605
- https://github.com/habib256/pom2games/commit/107307a5fdc74f02af41676785524443929d7e6f

### Relationships (reviewed)

The Wilderness subtree documents reconstruction from external woz-a-day WOZ/A2R images kept out of git; this is a subject inside the tracked POM2 collection, not an original-homebrew relabel.
- https://github.com/habib256/pom2games/blob/main/wilderness/docs/ANALYSE.md
- https://github.com/habib256/pom2games/commit/996971397f77a62c49aef92890dac1d69b5cc338
- https://github.com/habib256/pom2games/commit/107307a5fdc74f02af41676785524443929d7e6f

## amberstar-amber-framework

Project ID: amberstar-amber-framework · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "amberstar-amber-framework",
  "last_checked": "2026-10-25",
  "status": "Early Amberstar reimplementation now integrates fight-or-flee choice, encounter triggering, battle outcomes, loot, defeated-monster removal and rescue/game-over handling; no complete-game claim.",
  "techniques": [
    "direct gameplay implementation",
    "scenario-driven battle regression"
  ]
}
```

Expected existing project SHA256: f62f91745df5692f49516389ad2b4ec5675b87f918fab1cb1b46ad6d28758f19

### Identity (reviewed)

The shared Amber framework and Amberstar implementation remain one early reimplementation project. Current work adds an integrated encounter/battle/loot/defeat slice without claiming game completion.
- https://github.com/Pyrdacor/Amber/blob/main/README.md
- https://github.com/Pyrdacor/Amber/blob/main/Amberstar.Game/Game.cs
- https://github.com/Pyrdacor/Amber/commit/09fa24f211431f201d0bf66e81e0fcef5fedc2d8

### Classification (reviewed)

This remains direct C# gameplay and data-framework reimplementation, not recovered source or a binary-derived port claim.
- https://github.com/Pyrdacor/Amber/blob/main/README.md
- https://github.com/Pyrdacor/Amber/blob/main/Amberstar.Game/Game.cs
- https://github.com/Pyrdacor/Amber/commit/09fa24f211431f201d0bf66e81e0fcef5fedc2d8

### Source CPU (no-evidence-found)

Reviewed project documentation identifies legacy Atari ST, Amiga, DOS data or game heritage, but does not establish analyzed original CPU instructions; architecture is not inferred from the platform alone.
- https://github.com/Pyrdacor/Amber/blob/main/README.md
- https://github.com/Pyrdacor/Amber/blob/main/Amberstar.Game/Game.cs
- https://github.com/Pyrdacor/Amber/commit/09fa24f211431f201d0bf66e81e0fcef5fedc2d8

### Target CPU (no-evidence-found)

Reviewed source/build documentation names platforms or language/runtime but no explicit output CPU architecture; no target CPU is inferred from Java, C#, C/C++, or a portable framework.
- https://github.com/Pyrdacor/Amber/blob/main/README.md
- https://github.com/Pyrdacor/Amber/blob/main/Amberstar.net/Amberstar.net.csproj
- https://github.com/Pyrdacor/Amber/commit/09fa24f211431f201d0bf66e81e0fcef5fedc2d8

### Build (reviewed)

Upstream adds fight-or-flee confirmation, chance-based fleeing, monster advantage, encounter activation when the party is reached, loot display, monster removal after victory, and Shandra rescue or game-over after defeat, with scenario tests and scripting commands. The tracker did not compile or play the project; build/run/play flags remain unknown.
- https://github.com/Pyrdacor/Amber/blob/main/README.md
- https://github.com/Pyrdacor/Amber/blob/main/Amberstar.net/Amberstar.net.csproj
- https://github.com/Pyrdacor/Amber/commit/09fa24f211431f201d0bf66e81e0fcef5fedc2d8

### Runtime profiles (no-evidence-found)

The gameplay slice adds no explicit minimum host CPU, RAM, OS or mobile-device profile.
- https://github.com/Pyrdacor/Amber/blob/main/README.md
- https://github.com/Pyrdacor/Amber/blob/main/Amberstar.net/Amberstar.net.csproj
- https://github.com/Pyrdacor/Amber/commit/09fa24f211431f201d0bf66e81e0fcef5fedc2d8

### AI (reviewed)

The inspected commit explicitly credits Claude Opus 5.5, supporting the existing Claude development attribution.
- https://github.com/Pyrdacor/Amber/blob/main/README.md
- https://github.com/Pyrdacor/Amber/blob/main/Amberstar.Game/Game.cs
- https://github.com/Pyrdacor/Amber/blob/main/Amberstar.net/Amberstar.net.csproj
- https://github.com/Pyrdacor/Amber/commit/09fa24f211431f201d0bf66e81e0fcef5fedc2d8

### Relationships (reviewed)

Exact root absent; related Ambermoon projects known, but Amberstar game and Amber framework are distinct work. Keep the shared framework and Amberstar under one root, separate from Ambermoon.net.
- https://github.com/Pyrdacor/Amber/blob/main/README.md
- https://github.com/Pyrdacor/Amber/blob/main/Amberstar.Game/Game.cs
- https://github.com/Pyrdacor/Amber/commit/09fa24f211431f201d0bf66e81e0fcef5fedc2d8

## moria8-6502-multiplatform

Project ID: moria8-6502-multiplatform · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "moria8-6502-multiplatform",
  "last_checked": "2026-10-25",
  "status": "Released Apple II and Commodore ports plus buildable/testable Commander X16 target; current main adds AI playtesting infrastructure with seven isolated platform stages and a broad set of gameplay-parity fixes, without tracker-side execution.",
  "techniques": [
    "five-platform HAL boundary validation",
    "Commander X16 memory-contract testing",
    "x16emu runtime scenarios",
    "VICE binary-monitor AI playtesting",
    "isolated multi-platform emulator regression",
    "deterministic finding replay"
  ]
}
```

Expected existing project SHA256: fe2b885eea1b8d47c01a4b3152d8ae2877d17fd215c79fe58f835c887ff76594

### Identity (reviewed)

Moria8 is a single multi-platform assembly reimplementation of Moria. Current main contains released C64, C128, Plus/4 and Apple II outputs plus a new buildable/testable Commander X16 target; the README's status table still calls X16 planned, so it is not represented as a published release.
- https://github.com/dcgibbons/moria8/blob/60286809eafbd9e804f750d92c07ec2261c0827e/README.md
- https://github.com/dcgibbons/moria8/commit/60286809eafbd9e804f750d92c07ec2261c0827e
- https://github.com/dcgibbons/moria8/commit/a16fd0f87a4a473782990d8255edbd2f99ce54fe

### Classification (reviewed)

This remains a native, platform-specific assembly reimplementation derived from the credited VMS Moria and Umoria lineages, not a reverse-engineered binary port.
- https://github.com/dcgibbons/moria8/blob/60286809eafbd9e804f750d92c07ec2261c0827e/README.md
- https://github.com/dcgibbons/moria8/commit/a16fd0f87a4a473782990d8255edbd2f99ce54fe

### Source CPU (no-evidence-found)

The documented source lineages are VMS Pascal and C Umoria; no original executable ISA is established by the reviewed material, so source_cpu remains empty.
- https://github.com/dcgibbons/moria8/blob/60286809eafbd9e804f750d92c07ec2261c0827e/README.md
- https://github.com/dcgibbons/moria8/commit/a16fd0f87a4a473782990d8255edbd2f99ce54fe

### Target CPU (reviewed)

Existing Apple II and Commodore assembly supports the 6502 output. The Commander X16 makefile explicitly labels its new target 65C02/VERA, supporting the additional 65C02 output without inferring it from the platform name.
- https://github.com/dcgibbons/moria8/blob/60286809eafbd9e804f750d92c07ec2261c0827e/platforms/cx16/Makefile
- https://github.com/dcgibbons/moria8/commit/a16fd0f87a4a473782990d8255edbd2f99ce54fe

### Build (reviewed)

The merged playtesting work adds VICE binary-monitor sessions, goals, deterministic replay and a dashboard, then isolates fixed emulator ports with private network namespaces so seven platform stages (C64, C128, Plus/4, Apple II, Commander X16, Atari 8-bit and BBC Master) can run in parallel after one shared build. The same merge carries combat, item, monster and spell-effect fixes. These are upstream infrastructure and regression results; the tracker did not build or run any platform.
- https://github.com/dcgibbons/moria8/commit/60286809eafbd9e804f750d92c07ec2261c0827e
- https://github.com/dcgibbons/moria8/blob/60286809eafbd9e804f750d92c07ec2261c0827e/platforms/cx16/Makefile
- https://github.com/dcgibbons/moria8/commit/dea5d1ae681c36ab858dd3ef7ddc22ef42f8ab80
- https://github.com/dcgibbons/moria8/commit/a16fd0f87a4a473782990d8255edbd2f99ce54fe

### Runtime profiles (reviewed)

The existing Apple II 128 KiB/80-column/ProDOS profile remains sourced. Emulator-stage configuration and command timeouts are development-test requirements, not minimum physical hardware evidence, so no new runtime profile is added.
- https://github.com/dcgibbons/moria8/blob/feed714990ae616dd075b66ff0238b60ee2da0ed/docs/release_notes/release_notes-v1.5.0.md
- https://github.com/dcgibbons/moria8/blob/60286809eafbd9e804f750d92c07ec2261c0827e/README.md
- https://github.com/dcgibbons/moria8/commit/a16fd0f87a4a473782990d8255edbd2f99ce54fe

### AI (reviewed)

The repository now documents an operational AI playtester using structured goals, sessions and deterministic replay. Existing Claude evidence remains the project-level development attribution; the infrastructure does not imply that every gameplay change was authored by a model.
- https://github.com/dcgibbons/moria8/blob/feed714990ae616dd075b66ff0238b60ee2da0ed/README.md
- https://github.com/dcgibbons/moria8/blob/feed714990ae616dd075b66ff0238b60ee2da0ed/docs/release_notes/release_notes-v1.5.0.md
- https://github.com/dcgibbons/moria8/blob/feed714990ae616dd075b66ff0238b60ee2da0ed/platforms/apple2/main.s
- https://github.com/dcgibbons/moria8/blob/feed714990ae616dd075b66ff0238b60ee2da0ed/platforms/apple2/boot.s
- https://github.com/dcgibbons/moria8/blob/feed714990ae616dd075b66ff0238b60ee2da0ed/core/game_loop.s
- https://github.com/dcgibbons/moria8/blob/feed714990ae616dd075b66ff0238b60ee2da0ed/docs/APPLE2_MEMORY_POLICY.md
- https://github.com/dcgibbons/moria8/blob/feed714990ae616dd075b66ff0238b60ee2da0ed/platforms/apple2/Makefile
- https://github.com/dcgibbons/moria8/blob/feed714990ae616dd075b66ff0238b60ee2da0ed/LICENSE
- https://github.com/dcgibbons/moria8/blob/feed714990ae616dd075b66ff0238b60ee2da0ed/data/LICENSE
- https://github.com/dcgibbons/moria8/blob/feed714990ae616dd075b66ff0238b60ee2da0ed/data/SOURCE-OFFER
- https://github.com/dcgibbons/moria8/blob/feed714990ae616dd075b66ff0238b60ee2da0ed/artwork/CREDITS.md
- https://github.com/dcgibbons/moria8/commit/fdfdcfba7e91f9c4b34a8a82ed3774da577aac48
- https://github.com/dcgibbons/moria8/commit/34aac8b6f1b4ecdabe9a88f39500f68a790c43a3
- https://github.com/dcgibbons/moria8/commit/4cf93a96986bcd23fc103650434fbbd9e21774e7
- https://github.com/dcgibbons/moria8/commits/feed714990ae616dd075b66ff0238b60ee2da0ed
- https://github.com/dcgibbons/moria8/commit/dea5d1ae681c36ab858dd3ef7ddc22ef42f8ab80
- https://github.com/dcgibbons/moria8/commit/a16fd0f87a4a473782990d8255edbd2f99ce54fe

### Relationships (reviewed)

The shared Commodore and Apple II ports remain one Moria8 project, distinct from its explicitly credited VMS Moria/Umoria ancestors. README/root license specify GPLv3, with disk data/LICENSE and source-offer material; artwork has separate creator credits. Future platform rows and unrelated Moria titles are not additional discoveries. The normalized root, title/alias and lineage screen found no same-code project in the 1,833-project baseline or expanded 2,249-root prior-review union.
- https://github.com/dcgibbons/moria8/blob/feed714990ae616dd075b66ff0238b60ee2da0ed/README.md
- https://github.com/dcgibbons/moria8/blob/feed714990ae616dd075b66ff0238b60ee2da0ed/docs/release_notes/release_notes-v1.5.0.md
- https://github.com/dcgibbons/moria8/blob/feed714990ae616dd075b66ff0238b60ee2da0ed/LICENSE
- https://github.com/dcgibbons/moria8/blob/feed714990ae616dd075b66ff0238b60ee2da0ed/data/LICENSE
- https://github.com/dcgibbons/moria8/blob/feed714990ae616dd075b66ff0238b60ee2da0ed/data/SOURCE-OFFER
- https://github.com/dcgibbons/moria8/blob/feed714990ae616dd075b66ff0238b60ee2da0ed/artwork/CREDITS.md
- https://github.com/dcgibbons/moria8/blob/feed714990ae616dd075b66ff0238b60ee2da0ed/platforms/apple2/main.s
- https://github.com/dcgibbons/moria8/blob/feed714990ae616dd075b66ff0238b60ee2da0ed/platforms/apple2/boot.s
- https://github.com/dcgibbons/moria8/blob/feed714990ae616dd075b66ff0238b60ee2da0ed/core/game_loop.s
- https://github.com/dcgibbons/moria8/blob/feed714990ae616dd075b66ff0238b60ee2da0ed/docs/APPLE2_MEMORY_POLICY.md
- https://github.com/dcgibbons/moria8/commit/a16fd0f87a4a473782990d8255edbd2f99ce54fe

## neost-atari-emulator

Project ID: neost-atari-emulator · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "neost-atari-emulator",
  "last_checked": "2026-10-25",
  "status": "v0.6.2 emulator/debugger; current main adds virtual-INF PRG autostart and fixes duplicate-sector FDC behavior, 16 MHz IPL timing, IKBD mouse-joystick drift, scripted mouse release and save-state safety.",
  "techniques": [
    "hardware emulation",
    "Hatari differential testing",
    "disassembly",
    "watchpoints",
    "deterministic headless debugging",
    "serial-peripheral timing regression",
    "FDC live-media regression",
    "machine self-test cartridges",
    "cycle-deterministic external-control replay",
    "bit-exact 68881 transcendental functions",
    "Hatari differential-oracle regression",
    "virtual-INF autostart regression",
    "duplicate-sector-ID FDC regression",
    "IKBD timing regression"
  ]
}
```

Expected existing project SHA256: 65025c56f20bcbbfc8ca6872b75006c61051f9ad12896c148bd90681aa56b247

### Identity (reviewed)

NeoST remains a chip-oriented ST/Mega ST/STE/Mega STE emulator and debugger. Current main adds --auto PRG launch through generated desktop INF data for TOS 1.04+, TOS 2.06 and EmuTOS; the author reports EMail 1.56 testing on an emulated 1 MiB monochrome ST, not a universal guest-compatibility claim.
- https://github.com/habib256/neost
- https://github.com/habib256/neost/commit/312ac1a9a36b62b1441649c75c6bd38c56501cca

### Classification (reviewed)

Reviewed the current primary source for classification.
- https://github.com/habib256/neost
- https://github.com/habib256/neost/commit/312ac1a9a36b62b1441649c75c6bd38c56501cca

### Source CPU (reviewed)

Reviewed the current primary source for source_cpu.
- https://github.com/habib256/neost
- https://github.com/habib256/neost/commit/312ac1a9a36b62b1441649c75c6bd38c56501cca

### Target CPU (reviewed)

The v0.6.2 release publishes explicit x86-64, ARM64 and WebAssembly output variants; these are host/output architectures, not minimum CPU generations.
- https://github.com/habib256/neost/releases/tag/0.6.2
- https://github.com/habib256/neost/commit/312ac1a9a36b62b1441649c75c6bd38c56501cca

### Build (reviewed)

The current change adds virtual-INF autostart and fixes FDC duplicate sector IDs, READ ADDRESS size/CRC placement, 16 MHz IPL-delay scaling and load-state consistency, IKBD $18 mouse-joystick drift, scripted mouse release timing and save-state refusal during virtual-INF reads. This is upstream test evidence only; the tracker did not build or run NeoST.
- https://github.com/habib256/neost/commit/699e69680c3ec480ea6fd5c384c3c6266dda0295
- https://github.com/habib256/neost/releases/tag/0.6.2
- https://github.com/habib256/neost/commit/312ac1a9a36b62b1441649c75c6bd38c56501cca

### Runtime profiles (reviewed)

The reported 1 MiB monochrome ST configuration for EMail 1.56 is an emulated guest test case, not a host minimum or a proven lowest compatible Atari configuration. Existing release-asset profiles remain unchanged.
- https://github.com/habib256/neost/commit/699e69680c3ec480ea6fd5c384c3c6266dda0295
- https://github.com/habib256/neost/releases/tag/0.6.2
- https://github.com/habib256/neost/commit/312ac1a9a36b62b1441649c75c6bd38c56501cca

### AI (reviewed)

The inspected commit explicitly credits Claude Opus 5.5, supporting the existing project-level development-AI attribution.
- https://github.com/habib256/neost
- https://github.com/habib256/neost/commit/312ac1a9a36b62b1441649c75c6bd38c56501cca

### Relationships (needs-research)

The current change does not resolve the existing predecessor, successor, fork and credited-source relationship gap. Next check: Check predecessor, successor, fork and credited-source relationships.
- https://github.com/habib256/neost
- https://github.com/habib256/neost/commit/312ac1a9a36b62b1441649c75c6bd38c56501cca

## ghidra-retro-machines

Project ID: ghidra-retro-machines · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "ghidra-retro-machines",
  "last_checked": "2026-10-25",
  "status": "Development head now recovers 65C816 JMP/JSR (abs,X) jump tables, stamps dispatch E/M/X width state on new targets and bounds or shrinks tables conservatively against real-ROM conflicts.",
  "techniques": [
    "machine descriptors",
    "bank-state analysis",
    "hardware register symbols",
    "constant-pointer indirect-jump resolution",
    "jump-table bound analysis",
    "single-case oracle defect quarantine",
    "exhaustive CPU-vector verification",
    "planar split jump-table bounding",
    "cross-function predecessor analysis",
    "save-slot dataflow proofs",
    "analysis provenance tracking",
    "dead-code reachability cleanup",
    "analysis-order determinism",
    "parallel corpus reproducibility",
    "cross-function dataflow joins",
    "overlay occupancy invariants",
    "flaky corpus isolation",
    "effective-address decoding under address masks",
    "SPC700 IPL-handshake emulation",
    "byte-verified sound-driver upload recovery",
    "descriptor comment provenance",
    "6502 skip-idiom recognition",
    "one-shot instruction repair",
    "candidate bookmark provenance",
    "65C816 dispatch-width jump-table recovery",
    "conservative table over-read repair"
  ]
}
```

Expected existing project SHA256: bccadda0624a866db92413cdd4f72decf9786b9f7b431e901a54f4d36128805b

### Identity (reviewed)

Current README documents C64/C128/PET/NES machine loaders plus bundled SPC700 and 65C816 language variants; the display title now reflects both parts of the scope.
- https://github.com/CBongo/ghidra-retro-machines
- https://github.com/CBongo/ghidra-retro-machines/commit/7bd479add48fa9e895f60c622281a52dc49b425b
- https://github.com/CBongo/ghidra-retro-machines/commit/abcbbfd3079699a7fc0cd51ece3c1407523b4b43

### Classification (reviewed)

The new 65816 Jump Tables analyzer remains core reverse-engineering tooling: it recovers computed-flow targets and disassembles handlers at the dispatch width without producing translated native output.
- https://github.com/CBongo/ghidra-retro-machines/commit/475eeadd4fb50ad045bd8e01dd428243279bfe2d
- https://github.com/CBongo/ghidra-retro-machines/commit/1251af61b1d65c8849bc90795d186ee274938db4
- https://github.com/CBongo/ghidra-retro-machines/commit/2a15e0df8abeeccc0842b212a00e1d08d2316e41
- https://github.com/CBongo/ghidra-retro-machines/commit/48c66e952687ddaa24979626263f9b24dbd6b11d
- https://github.com/CBongo/ghidra-retro-machines/commit/7bd479add48fa9e895f60c622281a52dc49b425b
- https://github.com/CBongo/ghidra-retro-machines/commit/abcbbfd3079699a7fc0cd51ece3c1407523b4b43

### Source CPU (reviewed)

Machine descriptors explicitly cover 6502/6510/8502 inputs; README separately documents bundled SPC700 and 65C816 language variants for SNES code, with their current semantic limits preserved.
- https://github.com/CBongo/ghidra-retro-machines
- https://github.com/CBongo/ghidra-retro-machines/commit/7bd479add48fa9e895f60c622281a52dc49b425b
- https://github.com/CBongo/ghidra-retro-machines/commit/abcbbfd3079699a7fc0cd51ece3c1407523b4b43

### Target CPU (not-applicable)

Ghidra analysis output is not a translated native retro binary.
- https://github.com/CBongo/ghidra-retro-machines
- https://github.com/CBongo/ghidra-retro-machines/commit/7bd479add48fa9e895f60c622281a52dc49b425b
- https://github.com/CBongo/ghidra-retro-machines/commit/abcbbfd3079699a7fc0cd51ece3c1407523b4b43

### Build (reviewed)

Upstream adds a default-enabled analyzer for 65C816 JMP/JSR (abs,X) tables. It bounds tables using index masks, code/data occupancy, lowest targets and width-aware 16-instruction plausibility; shared tables are reused and later code conflicts shrink or withdraw over-read entries. Reported real-ROM rows increase decoded instructions and recover targets while reducing desync rate, with build-and-test and NES 35/35 gates passing. The tracker did not build Ghidra or run the corpora.
- https://github.com/CBongo/ghidra-retro-machines/commit/8a20c6bb65074bd911008cffccff587ffc8083d4
- https://github.com/CBongo/ghidra-retro-machines/commit/95ee768b7a25e0646f3237fcc5688a88c1c8c411
- https://github.com/CBongo/ghidra-retro-machines/commit/30539debbfef0bdebf15d754ee86dd73c7a1aae1
- https://github.com/CBongo/ghidra-retro-machines/commit/7bd479add48fa9e895f60c622281a52dc49b425b
- https://github.com/CBongo/ghidra-retro-machines/commit/abcbbfd3079699a7fc0cd51ece3c1407523b4b43

### Runtime profiles (no-evidence-found)

The analyzer change adds no minimum host CPU, RAM or OS evidence; Ghidra/JDK software prerequisites remain distinct from hardware minima.
- https://github.com/CBongo/ghidra-retro-machines/commit/8a20c6bb65074bd911008cffccff587ffc8083d4
- https://github.com/CBongo/ghidra-retro-machines/commit/95ee768b7a25e0646f3237fcc5688a88c1c8c411
- https://github.com/CBongo/ghidra-retro-machines/commit/7bd479add48fa9e895f60c622281a52dc49b425b
- https://github.com/CBongo/ghidra-retro-machines/commit/abcbbfd3079699a7fc0cd51ece3c1407523b4b43

### AI (reviewed)

The implementation commit explicitly credits Claude Opus 5.5 and links a Claude session; attribution is scoped to this analyzer change.
- https://github.com/CBongo/ghidra-retro-machines/commit/8a20c6bb65074bd911008cffccff587ffc8083d4
- https://github.com/CBongo/ghidra-retro-machines/commit/95ee768b7a25e0646f3237fcc5688a88c1c8c411
- https://github.com/CBongo/ghidra-retro-machines/commit/30539debbfef0bdebf15d754ee86dd73c7a1aae1
- https://github.com/CBongo/ghidra-retro-machines/commit/7bd479add48fa9e895f60c622281a52dc49b425b
- https://github.com/CBongo/ghidra-retro-machines/commit/abcbbfd3079699a7fc0cd51ece3c1407523b4b43

### Relationships (reviewed)

README says the extension was incubated in and serves CBongo/game-music-extraction; that adjacent multi-system extraction repository is queued for independent-scope review.
- https://github.com/CBongo/ghidra-retro-machines
- https://github.com/CBongo/ghidra-retro-machines/commit/7bd479add48fa9e895f60c622281a52dc49b425b
- https://github.com/CBongo/ghidra-retro-machines/commit/abcbbfd3079699a7fc0cd51ece3c1407523b4b43

## Research event notes

The CPU audit queue contained zero unresolved source/target CPU areas. This pass therefore made no speculative CPU additions: Sim City output CPUs and all new minimum-hardware claims remain unknown where primary evidence was absent. No upstream software, disk image or emulator was built, launched or played by the tracker.
