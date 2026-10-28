# Reconstruction, emulator and static-recompilation maintenance

Review eleven material upstream changes across reconstruction fidelity, emulator scheduling, static recompilation, enhanced Amiga variants and reverse-engineering tooling.

Date: 2026-10-28 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- m68k-reversing-toolkit-rmtew / Build (needs-research): These are upstream targeted checks and generated-output claims; the tracker did not run the generator or game, and the remaining unresolved accesses still require semantic classification. Next check: Continue classifying the remaining unresolved record accesses and qualify behavior without promoting local exactness to complete reconstruction.
- m68k-reversing-toolkit-rmtew / Runtime profiles (needs-research): The reviewed creator-contract receipt does not state a minimum Amiga CPU, RAM, chipset or ROM configuration. Next check: Add a runtime profile only when primary documentation or qualified hardware/emulator testing states a concrete minimum configuration.
- m68k-reversing-toolkit-rmtew / Relationships (needs-research): The current restoration remains within the Starglider 2 target and does not resolve the wider predecessor, successor or credited-source graph. Next check: Revisit project relationships after the bounded restoration stabilizes.
- wing-commander-kilrathi-saga-reconstruction / Target CPU (no-evidence-found): The README documents modern host operating systems but does not establish a fixed supported output CPU; none is inferred from C/C++ portability.
- wing-commander-kilrathi-saga-reconstruction / Build (needs-research): This is a bounded exact-match result, not proof that every remaining function, executable byte or gameplay route is complete; the tracker did not compile or compare the executable. Next check: Track closure of the remaining strict-byte runs and require a complete build/runtime claim before promoting whole-project exactness.
- wing-commander-kilrathi-saga-reconstruction / Runtime profiles (no-evidence-found): The inspected change provides no minimum host CPU, RAM or OS profile; user-supplied game data remains required.
- firestaff-dungeon-master-engine / Build (needs-research): This upstream test covers launcher recovery and media discovery, not native display, input, audio or complete campaign parity; the tracker did not execute it. Next check: Continue authenticated campaign and presentation validation while preserving platform- and checkpoint-specific limits.
- smikes75-amiga-re-kit / Target CPU (no-evidence-found): No minimum host instruction set established; a retro input platform is not a host CPU requirement.
- smikes75-amiga-re-kit / Build (reviewed): The test total and exactness statements are upstream results; the tracker did not install the package, run pytest, translate a game or compare captures.
- smikes75-amiga-re-kit / Runtime profiles (no-evidence-found): The inspected 0.7.1 material documents tools and test environments but no minimum host CPU, RAM or OS requirement, and no minimum Amiga configuration is inferred from its input formats.
- copperline-amiga-emulator / Build (reviewed): The tracker did not build Copperline or reproduce its benchmark results.
- markyturtle-newzealandstory-amiga / Build (reviewed): The tracker did not assemble or run the disk. Emulator coverage does not establish physical-hardware compatibility or a complete minimum machine profile.
- markyturtle-newzealandstory-amiga / Runtime profiles (no-evidence-found): The documentation gives tested emulator configurations and a 512 KiB mirror-cache design constraint but does not state a complete minimum CPU, chip/fast RAM, chipset and Kickstart profile for the enhanced variant.
- space-station-silicon-valley-decompilation / Build (reviewed): The tracker did not build or hash a ROM. The percentage is an upstream aggregate and does not establish complete source recovery, runtime fidelity or EU parity.
- space-station-silicon-valley-decompilation / Runtime profiles (no-evidence-found): No independently verified minimum hardware profile established.
- space-station-silicon-valley-decompilation / AI (no-evidence-found): No explicit completed-work AI disclosure established in inspected evidence. Config files, workflow instructions and algorithmic neural features alone are not proof of authorship.
- cdlewis-snowboardkids-decomp / Build (reviewed): The exactness claim is bounded to the changed routine; the tracker did not build or compare a ROM and does not extend it to whole-project or other-region completion.
- cdlewis-snowboardkids-decomp / Runtime profiles (no-evidence-found): No verified minimum CPU/RAM/OS profile established beyond the qualified dependency and format notes; no runtime test was performed.
- cdlewis-snowboardkids-decomp / AI (no-evidence-found): No explicit development-AI contribution disclosure was established in the inspected material; absence does not establish non-use. Agent configuration or MCP integration alone does not establish authorship.
- openrac-rac1-decomp / Build (reviewed): The tracker did not compile with the period toolchains or independently compare the result; structural cleanup alone does not establish whole-project matching or playability.
- openrac-rac1-decomp / Runtime profiles (no-evidence-found): No verified minimum CPU/RAM/OS profile established beyond the qualified dependency and format notes; no runtime test was performed.
- gustavocanepa-gt4-decomp / Build (reviewed): These are upstream progress counters. The tracker did not compile, link, boot or play the reconstruction, and the counters do not establish complete data recovery.
- gustavocanepa-gt4-decomp / Runtime profiles (no-evidence-found): No verified minimum CPU/RAM/OS profile established beyond the qualified dependency and format notes; no runtime test was performed.
- faxanadu-nes-mstan-recomp / Build (reviewed): Upstream records preliminary owner playtesting and native/interpreter agreement, but broader progression, bosses and secrets remain open and cross-room combat/projectiles are incomplete; the tracker did not run the release.
- faxanadu-nes-mstan-recomp / Runtime profiles (no-evidence-found): The reviewed release and README do not state a minimum host CPU, RAM or OS version; no runtime floor is inferred from the generated x64 target.
- faxanadu-nes-mstan-recomp / AI (no-evidence-found): A bounded review of the current release commit and project documentation found no explicit development-AI contribution disclosure; absence does not establish non-use.

## m68k-reversing-toolkit-rmtew

Project ID: m68k-reversing-toolkit-rmtew · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "m68k-reversing-toolkit-rmtew",
  "last_activity": "2026-10-27",
  "last_checked": "2026-10-28",
  "status": "Starglider 2 output remains byte-exact while six projectile-creator call contracts and their storage roles are restored; 24 orphan layout coordinates were removed, but broader semantics and minimum runtime requirements remain incomplete.",
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
    "canonical custom-type prefix joining",
    "projectile creator contract recovery",
    "orphan layout-element rejection"
  ]
}
```

Expected existing project SHA256: 6b1095a77f7802f83a5fdd42a47b408205def1352654a3c0fa65cd4e19ba1f39

### Identity (reviewed)

M68k Reversing Toolkit remains the same generated Amiga analysis and reconstruction framework; the reviewed change advances its Starglider 2 restoration rather than creating a separate project.
- https://github.com/rmtew/amiga-reversing/commit/9c8cdbfd2a4fca323e3fcc37031a32f7d4c72780
- https://github.com/rmtew/amiga-reversing/commit/e27b8f71fa9ea49f77d6a5ceb937368f167eda5c

### Classification (reviewed)

The change is bounded reconstruction/tooling work: canonical ancestry is used to retain a safe common custom pointer prefix without treating that prefix as proof of equal values, subtype, lifetime or complete semantics.
- https://github.com/rmtew/amiga-reversing/commit/9c8cdbfd2a4fca323e3fcc37031a32f7d4c72780
- https://github.com/rmtew/amiga-reversing/commit/e27b8f71fa9ea49f77d6a5ceb937368f167eda5c

### Source CPU (reviewed)

The tracked Starglider 2 input remains Motorola 68000 code; no new architecture is inferred from the analysis implementation.
- https://github.com/rmtew/amiga-reversing/blob/9c8cdbfd2a4fca323e3fcc37031a32f7d4c72780/README.md
- https://github.com/rmtew/amiga-reversing/commit/e27b8f71fa9ea49f77d6a5ceb937368f167eda5c

### Target CPU (reviewed)

The retained output is native Motorola 68000 assembly, verified upstream against the original binary through the existing C/vasm route.
- https://github.com/rmtew/amiga-reversing/commit/9c8cdbfd2a4fca323e3fcc37031a32f7d4c72780
- https://github.com/rmtew/amiga-reversing/commit/e27b8f71fa9ea49f77d6a5ceb937368f167eda5c

### Build (needs-research)

The primary change restores six recovered projectile-creator callers, types their storage roles (including type 12/25 writes and the steered-projectile path), and rejects 24 orphan layout coordinates while retaining the existing byte-exact Starglider 2 generation route. Limitations: These are upstream targeted checks and generated-output claims; the tracker did not run the generator or game, and the remaining unresolved accesses still require semantic classification. Next check: Continue classifying the remaining unresolved record accesses and qualify behavior without promoting local exactness to complete reconstruction.
- https://github.com/rmtew/amiga-reversing/commit/e27b8f71fa9ea49f77d6a5ceb937368f167eda5c

### Runtime profiles (needs-research)

The reviewed creator-contract receipt does not state a minimum Amiga CPU, RAM, chipset or ROM configuration. Next check: Add a runtime profile only when primary documentation or qualified hardware/emulator testing states a concrete minimum configuration.
- https://github.com/rmtew/amiga-reversing/commit/e27b8f71fa9ea49f77d6a5ceb937368f167eda5c

### AI (reviewed)

Existing explicit Claude contribution evidence remains valid; the reviewed commit does not add a new attribution category.
- https://github.com/rmtew/amiga-reversing/commit/0806d08b49d8d7f1aa6826c40385317bbb81154c
- https://github.com/rmtew/amiga-reversing/commit/9c8cdbfd2a4fca323e3fcc37031a32f7d4c72780
- https://github.com/rmtew/amiga-reversing/commit/e27b8f71fa9ea49f77d6a5ceb937368f167eda5c

### Relationships (needs-research)

The current restoration remains within the Starglider 2 target and does not resolve the wider predecessor, successor or credited-source graph. Next check: Revisit project relationships after the bounded restoration stabilizes.
- https://github.com/rmtew/amiga-reversing/commit/9c8cdbfd2a4fca323e3fcc37031a32f7d4c72780
- https://github.com/rmtew/amiga-reversing/commit/e27b8f71fa9ea49f77d6a5ceb937368f167eda5c

## wing-commander-kilrathi-saga-reconstruction

Project ID: wing-commander-kilrathi-saga-reconstruction · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "wing-commander-kilrathi-saga-reconstruction",
  "last_activity": "2026-10-27",
  "last_checked": "2026-10-28",
  "status": "Working Win32 reconstruction and SDL2 port; the scramble/cutscene change now matches the original register allocation byte for byte, while the remaining strict-byte runs and whole-project completion stay open.",
  "techniques": [
    "strict whole-file executable comparison",
    "per-function machine-code similarity auditing",
    "discarded-probe recording",
    "register-lifetime probe recording",
    "byte-for-byte function matching",
    "register-allocation matching"
  ]
}
```

Expected existing project SHA256: ce6e7ef12d9349acaa1ec0a0bd386a34222734bafbaf292c2509a2c1d083f86c

### Identity (reviewed)

Recovered native Win32 Wing Commander source plus SDL2 port and original-binary comparison workflow; the current work refines matching in the same reconstruction.
- https://github.com/neuromancer/wc1-re/commit/e4f4f7085ca5f06c18e20f3d0c71b1022b505ed0
- https://github.com/neuromancer/wc1-re/commit/43299bf5742aee892d7159de0f97347ebad1b672

### Classification (reviewed)

Incomplete byte-oriented reconstruction with a modern SDL2 port. Per-function similarity and strict byte coverage remain separate from gameplay-completeness claims.
- https://github.com/neuromancer/wc1-re/commit/e4f4f7085ca5f06c18e20f3d0c71b1022b505ed0
- https://github.com/neuromancer/wc1-re/commit/43299bf5742aee892d7159de0f97347ebad1b672

### Source CPU (reviewed)

The reconstructed Kilrathi Saga executable remains x86 input.
- https://github.com/neuromancer/wc1-re/blob/e4f4f7085ca5f06c18e20f3d0c71b1022b505ed0/README.md
- https://github.com/neuromancer/wc1-re/commit/43299bf5742aee892d7159de0f97347ebad1b672

### Target CPU (no-evidence-found)

The README documents modern host operating systems but does not establish a fixed supported output CPU; none is inferred from C/C++ portability.
- https://github.com/neuromancer/wc1-re/blob/e4f4f7085ca5f06c18e20f3d0c71b1022b505ed0/README.md
- https://github.com/neuromancer/wc1-re/commit/43299bf5742aee892d7159de0f97347ebad1b672

### Build (needs-research)

The primary commit changes the scramble cutscene implementation and associated declarations to reproduce the original register allocation byte for byte. Limitations: This is a bounded exact-match result, not proof that every remaining function, executable byte or gameplay route is complete; the tracker did not compile or compare the executable. Next check: Track closure of the remaining strict-byte runs and require a complete build/runtime claim before promoting whole-project exactness.
- https://github.com/neuromancer/wc1-re/commit/43299bf5742aee892d7159de0f97347ebad1b672

### Runtime profiles (no-evidence-found)

The inspected change provides no minimum host CPU, RAM or OS profile; user-supplied game data remains required.
- https://github.com/neuromancer/wc1-re/blob/e4f4f7085ca5f06c18e20f3d0c71b1022b505ed0/README.md
- https://github.com/neuromancer/wc1-re/commit/43299bf5742aee892d7159de0f97347ebad1b672

### AI (reviewed)

The repository explicitly documents Codex and Claude use; the current matching commit does not broaden that attribution beyond evidenced work.
- https://github.com/neuromancer/wc1-re/blob/e4f4f7085ca5f06c18e20f3d0c71b1022b505ed0/README.md
- https://github.com/neuromancer/wc1-re/commit/e4f4f7085ca5f06c18e20f3d0c71b1022b505ed0
- https://github.com/neuromancer/wc1-re/commit/43299bf5742aee892d7159de0f97347ebad1b672

### Relationships (reviewed)

The project continues to use binary-comp for verification and retains its documented historical compatibility references; the reviewed change creates no separate component.
- https://github.com/neuromancer/wc1-re/blob/e4f4f7085ca5f06c18e20f3d0c71b1022b505ed0/README.md
- https://github.com/neuromancer/wc1-re/commit/43299bf5742aee892d7159de0f97347ebad1b672

## firestaff-dungeon-master-engine

Project ID: firestaff-dungeon-master-engine · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "firestaff-dungeon-master-engine",
  "last_activity": "2026-10-27",
  "last_checked": "2026-10-28",
  "status": "Firestaff now rescans authenticated game data after folder access is granted or repaired, keeping launcher access ownership separate from the runtime; full campaign and presentation parity remain open.",
  "techniques": [
    "clean-room reimplementation",
    "original-media hashing",
    "binary analysis",
    "format decoding",
    "cross-version comparison",
    "real-media verification",
    "source-locked runtime verification",
    "instrumented Mednafen capture",
    "Backup RAM format analysis",
    "CD track provenance verification",
    "source-frame byte comparison",
    "native save-format analysis",
    "bounded in-memory media decoding",
    "cross-platform startup matrix testing",
    "source-clock timing calibration",
    "authenticated viewport-region gates",
    "deterministic RNG bootstrap verification",
    "source-locked fixed-point sampling",
    "authenticated packed-selector decoding",
    "source-timed VBlank cadence",
    "Apple IIGS resource decoding",
    "65C816 hidden-code analysis",
    "DOC sound reconstruction",
    "authenticated mouse-route regression",
    "input-to-present latency tracing",
    "authenticated Apple IIGS startup-route verification",
    "original-media immutability hashing",
    "source-timed selector animation/audio separation",
    "overlapped authenticated-media scanning",
    "authenticated cross-game startup matrix",
    "bounded original-media weather/RNG verification",
    "authenticated alcove interaction regression",
    "authenticated first-combat verification",
    "authenticated five-game main-menu selection",
    "authenticated Amiga 3.6 combat-route verification",
    "source-ordered indoor draw interleaving",
    "bounded missile-chain traversal",
    "retail keyboard-capture reconstruction",
    "mouse-to-pad route validation",
    "Nexus event-44 dispatch tracing",
    "authenticated mixed-media AUTO launcher regression",
    "Saturn BKR save-card decoding",
    "native FM Towns RLE decoding",
    "authenticated graphics regression",
    "post-permission authenticated-media rescan",
    "launcher/runtime access-owner separation"
  ]
}
```

Expected existing project SHA256: 1d1f0e8f28be8480bd0be9db7c9bb5e48cf263c0ce1f4cd2cad647534612af50

### Identity (reviewed)

Firestaff remains a clean-room Dungeon Master-family engine using authenticated original media across documented platform variants.
- https://github.com/yeager/firestaff/releases/tag/v3.0.416
- https://github.com/yeager/firestaff/commit/bcdd94bd06d4fe442e2429870111419e0ca57bae
- https://github.com/yeager/firestaff/commit/8d0c71d73d994eda534e90b66ccf4922bc3698db

### Classification (reviewed)

Clean-room cross-platform engine reconstruction. Launcher and source-trace receipts are bounded verification evidence, not proof of full campaign, display, audio or save parity.
- https://github.com/yeager/firestaff/releases/tag/v3.0.416
- https://github.com/yeager/firestaff/commit/bcdd94bd06d4fe442e2429870111419e0ca57bae
- https://github.com/yeager/firestaff/commit/8d0c71d73d994eda534e90b66ccf4922bc3698db

### Source CPU (reviewed)

Existing x86, m68k, HuC6280, SH-2 and 65C816 source-family decisions remain supported by the documented original-platform scope; no new CPU is established by this pass.
- https://github.com/yeager/firestaff/blob/bcdd94bd06d4fe442e2429870111419e0ca57bae/README.md
- https://github.com/yeager/firestaff/commit/8d0c71d73d994eda534e90b66ccf4922bc3698db

### Target CPU (reviewed)

Published v3.0.416 assets retain x86-64 and arm64 modern outputs. Asset publication is not converted into an unstated minimum CPU generation.
- https://github.com/yeager/firestaff/releases/tag/v3.0.416
- https://github.com/yeager/firestaff/commit/8d0c71d73d994eda534e90b66ccf4922bc3698db

### Build (needs-research)

The primary change adds a regression for selecting an inaccessible data folder, granting access, rescanning it and discovering Dungeon Master media while preserving a separate runtime access owner. Limitations: This upstream test covers launcher recovery and media discovery, not native display, input, audio or complete campaign parity; the tracker did not execute it. Next check: Continue authenticated campaign and presentation validation while preserving platform- and checkpoint-specific limits.
- https://github.com/yeager/firestaff/commit/8d0c71d73d994eda534e90b66ccf4922bc3698db

### Runtime profiles (reviewed)

Existing evidenced Mac mini M4 and QEMU-hosted Linux x86-64 profiles remain valid. v3.0.416 publishes additional assets but does not establish a new measured minimum CPU, RAM or OS floor.
- https://github.com/yeager/firestaff/releases/tag/v3.0.416
- https://github.com/yeager/firestaff/commit/bcdd94bd06d4fe442e2429870111419e0ca57bae
- https://github.com/yeager/firestaff/commit/8d0c71d73d994eda534e90b66ccf4922bc3698db

### AI (reviewed)

Existing explicit Claude contribution evidence remains scoped to evidenced commits; the reviewed release metadata does not justify broadening the project-level claim.
- https://github.com/yeager/firestaff/commit/bcdd94bd06d4fe442e2429870111419e0ca57bae
- https://github.com/yeager/firestaff/commit/8d0c71d73d994eda534e90b66ccf4922bc3698db

### Relationships (reviewed)

DM1, Chaos Strikes Back, DM2, Nexus and Theron's Quest remain variants within the same source-faithful engine effort, with their evidence limits kept distinct.
- https://github.com/yeager/firestaff/blob/bcdd94bd06d4fe442e2429870111419e0ca57bae/README.md
- https://github.com/yeager/firestaff/commit/8d0c71d73d994eda534e90b66ccf4922bc3698db

## smikes75-amiga-re-kit

Project ID: smikes75-amiga-re-kit · Overall audit: partial

### Typed catalogue changes

```json
{
  "ai": {
    "evidence": [
      "Claude co-author trailer observed in recent tracked commits: 11 in this scan (example 445674974d9f; Claude Fable 5.1)",
      "Explicit upstream commit attribution: Co-Authored-By: Claude Fable 5.1. https://github.com/smikes75/amiga-re-kit/commit/445674974d9f346bb42d3f85b1599a6bc973709c"
    ],
    "tools": [
      "Claude"
    ],
    "usage": true
  },
  "id": "smikes75-amiga-re-kit",
  "last_activity": "2026-10-27",
  "last_checked": "2026-10-28",
  "status": "Version 0.7.1 adds whole-game m68k-to-C translation roots and overlays, exact display-gap comparison, a web engine and an interrupt-aware Paula state model; upstream reports 2,376 tests, but the tracker did not run them.",
  "techniques": [
    "whole-game m68k-to-C translation",
    "display differential validation",
    "interrupt-aware Paula state modelling",
    "Emscripten web-engine validation"
  ]
}
```

Expected existing project SHA256: 6700efbd8b09618a84135ad2a2650aea54e7ce7d454254a2407c5eaea01290a0

### Identity (reviewed)

amiga-re-kit — measured Amiga reverse-engineering toolkit. Repository root and implementation inspected at pinned revisions.
- https://github.com/smikes75/amiga-re-kit/blob/34fe20cfd007b5737b601af6fb374c62e030b19c/README.md
- https://github.com/smikes75/amiga-re-kit/blob/34fe20cfd007b5737b601af6fb374c62e030b19c/src/arek/m68k/recomp.py
- https://github.com/smikes75/amiga-re-kit/commit/445674974d9f346bb42d3f85b1599a6bc973709c

### Classification (reviewed)

Game-agnostic extraction of instruments from SWIV, Turrican II and Superfrog projects. ADF/HUNK readers, checksum-aware unpackers, conservative 68000 walking, MCP and capture comparison are implemented. Recompiler is explicitly a prototype with a restricted blitter/custom-chip model; unmodelled accesses are logged, not proof of a complete native game port.
- https://github.com/smikes75/amiga-re-kit/blob/34fe20cfd007b5737b601af6fb374c62e030b19c/README.md
- https://github.com/smikes75/amiga-re-kit/blob/34fe20cfd007b5737b601af6fb374c62e030b19c/src/arek/m68k/recomp.py
- https://github.com/smikes75/amiga-re-kit/commit/445674974d9f346bb42d3f85b1599a6bc973709c

### Source CPU (reviewed)

Architecture context: m68k. Source and target roles are recorded separately.
- https://github.com/smikes75/amiga-re-kit/blob/34fe20cfd007b5737b601af6fb374c62e030b19c/README.md
- https://github.com/smikes75/amiga-re-kit/blob/34fe20cfd007b5737b601af6fb374c62e030b19c/src/arek/m68k/recomp.py
- https://github.com/smikes75/amiga-re-kit/commit/445674974d9f346bb42d3f85b1599a6bc973709c

### Target CPU (no-evidence-found)

No minimum host instruction set established; a retro input platform is not a host CPU requirement.
- https://github.com/smikes75/amiga-re-kit/blob/34fe20cfd007b5737b601af6fb374c62e030b19c/README.md
- https://github.com/smikes75/amiga-re-kit/blob/34fe20cfd007b5737b601af6fb374c62e030b19c/src/arek/m68k/recomp.py
- https://github.com/smikes75/amiga-re-kit/commit/445674974d9f346bb42d3f85b1599a6bc973709c

### Build (reviewed)

The pinned 0.7.1 documentation describes whole-game translation roots and overlays, a web engine, exact display comparison against vAmiga, an interrupt-aware Paula model and 2,376 passing pytest tests without bundling game data. Limitations: The test total and exactness statements are upstream results; the tracker did not install the package, run pytest, translate a game or compare captures.
- https://github.com/smikes75/amiga-re-kit/commit/445674974d9f346bb42d3f85b1599a6bc973709c

### Runtime profiles (no-evidence-found)

The inspected 0.7.1 material documents tools and test environments but no minimum host CPU, RAM or OS requirement, and no minimum Amiga configuration is inferred from its input formats.
- https://github.com/smikes75/amiga-re-kit/commit/445674974d9f346bb42d3f85b1599a6bc973709c

### AI (reviewed)

The reviewed 0.7.1 commit explicitly credits Claude Fable 5.1 as co-author; attribution is limited to evidenced work.
- https://github.com/smikes75/amiga-re-kit/commit/445674974d9f346bb42d3f85b1599a6bc973709c

### Relationships (reviewed)

Related game projects are extraction provenance, not extra projects created from the toolkit directories.
- https://github.com/smikes75/amiga-re-kit/blob/34fe20cfd007b5737b601af6fb374c62e030b19c/README.md
- https://github.com/smikes75/amiga-re-kit/blob/34fe20cfd007b5737b601af6fb374c62e030b19c/src/arek/m68k/recomp.py
- https://github.com/smikes75/amiga-re-kit/commit/445674974d9f346bb42d3f85b1599a6bc973709c

## copperline-amiga-emulator

Project ID: copperline-amiga-emulator · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "copperline-amiga-emulator",
  "last_activity": "2026-10-27",
  "last_checked": "2026-10-28",
  "status": "Copperline improves JIT memory access and fastest-mode CPU scheduling, with documented benchmark recipes separating deterministic fixed-frequency emulation from host-dependent fastest mode.",
  "techniques": [
    "WinUAE-compatible debug output",
    "cycle-driven hardware emulation",
    "headless deterministic testing",
    "native-resolution screenshot capture",
    "capability-gated WASM expansion plugins",
    "persistent media write-through",
    "reverse stepping",
    "source debugging",
    "state import",
    "interlaced field weaving",
    "drive-mechanism event serialization",
    "WinUAE/FS-UAE sample-set compatibility",
    "power-on versus warm-reset modelling",
    "Kickstart boot-menu regression testing",
    "MMU-less 68EC CPU modelling",
    "68EC030 access-control-unit emulation",
    "guest CPU boot regression",
    "JIT memory-access optimization",
    "fixed-versus-fastest scheduling benchmarks"
  ]
}
```

Expected existing project SHA256: 1e53c84cf88e2835aacc4afe98e24a9667ed3debb40cf79c50dd22c1460e1f30

### Identity (reviewed)

Seeded from curated upstream_name/display_title/subjects.
- https://github.com/CopperlineHQ/Copperline/commit/49c36005e9974b427096fe045d7fc849e4f1cd54

### Classification (reviewed)

Seeded from record_class and structured kind fields.
- https://github.com/CopperlineHQ/Copperline/commit/49c36005e9974b427096fe045d7fc849e4f1cd54

### Source CPU (reviewed)

The source cpu decision remains unchanged after reviewing the current primary commit.
- https://github.com/CopperlineHQ/Copperline/commit/49c36005e9974b427096fe045d7fc849e4f1cd54

### Target CPU (not-applicable)

The target cpu decision remains unchanged after reviewing the current primary commit.
- https://github.com/CopperlineHQ/Copperline/commit/49c36005e9974b427096fe045d7fc849e4f1cd54

### Build (reviewed)

The merged primary change improves JIT memory access and fastest-mode CPU scheduling and documents the benchmark configurations used to compare fixed deterministic and host-dependent fastest modes. Limitations: The tracker did not build Copperline or reproduce its benchmark results.
- https://github.com/CopperlineHQ/Copperline/commit/49c36005e9974b427096fe045d7fc849e4f1cd54

### Runtime profiles (not-applicable)

The documented A1200/68040 and A500-style configurations are guest benchmark recipes, not minimum host hardware requirements or verified minimum runnable Amiga profiles; no runtime minimum is inferred from them.
- https://github.com/CopperlineHQ/Copperline/commit/49c36005e9974b427096fe045d7fc849e4f1cd54

### AI (reviewed)

Existing affirmative Claude/Copilot/Codex evidence remains valid. The floppy-sound change also received an explicit Copilot-review follow-up; attribution remains scoped to evidenced work.
- https://github.com/CopperlineHQ/Copperline/commit/272e6f779f0d7afdbdf273ab5ca478596301840a
- https://github.com/CopperlineHQ/Copperline/commit/c3220bc325d68f85a5730b50627ef419879b19a2
- https://github.com/CopperlineHQ/Copperline/commit/49c36005e9974b427096fe045d7fc849e4f1cd54

### Relationships (reviewed)

Copperline is an independent emulator/debugger with WinUAE state/configuration interoperability and a maintained public fork of the Bartman VS Code Amiga debugger extension.
- https://github.com/CopperlineHQ/Copperline/blob/main/README.md
- https://github.com/CopperlineHQ/Copperline/blob/main/docs/debugger/vscode-bartman.md
- https://github.com/CopperlineHQ/Copperline/commit/49c36005e9974b427096fe045d7fc849e4f1cd54

## markyturtle-newzealandstory-amiga

Project ID: markyturtle-newzealandstory-amiga · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "ai": {
    "evidence": [
      "Claude co-author trailer observed in recent tracked commits: 31 in this scan (example 013f2a91c765; Claude Opus 5.5)",
      "Explicit upstream commit attribution and session reference: Claude Opus 5.5. https://github.com/MarkyTurtle/NewzealandStory--Amiga/commit/013f2a91c7651546f50c04c17ff22ed3d69bcf93"
    ],
    "tools": [
      "Claude"
    ],
    "usage": true
  },
  "id": "markyturtle-newzealandstory-amiga",
  "last_activity": "2026-10-27",
  "last_checked": "2026-10-28",
  "status": "Byte-exact Amiga disassembly/rebuild plus enhanced variant; the enhanced branch now adds a title/options menu, two-button joystick controls, sound test, cheat fly mode and F2 level skip alongside its existing smooth-scroller work.",
  "techniques": [
    "byte-exact disassembly rebuild",
    "frame-by-frame emulator comparison",
    "double-buffered corkscrew scrolling",
    "on-demand mirrored-frame caching",
    "interpolated 50 Hz presentation",
    "enhanced-variant menu regression testing",
    "all-level cheat-route testing"
  ]
}
```

Expected existing project SHA256: 3adef42988b313da7c4ccbc53b5c1166852c11803618d15184a58696434cc251

### Identity (reviewed)

The New Zealand Story Amiga disassembly and disk rebuild now also carries an enhanced hand-edited branch for optional display and memory improvements.
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/commit/98a83e1b98c61d80bdf6608c2e71124036b7583f
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/commit/013f2a91c7651546f50c04c17ff22ed3d69bcf93

### Classification (reviewed)

The exact disk rebuild and optional enhanced variant remain one Amiga disassembly project; the menu, input and cheat additions are original enhancements and are not mislabelled as recovered original behavior.
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/commit/013f2a91c7651546f50c04c17ff22ed3d69bcf93

### Source CPU (reviewed)

The original and enhanced Amiga assembly remain Motorola 68000-family source.
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/blob/98a83e1b98c61d80bdf6608c2e71124036b7583f/BUILDING.md
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/commit/013f2a91c7651546f50c04c17ff22ed3d69bcf93

### Target CPU (reviewed)

The project continues to emit native m68k Amiga disk output; no other CPU target is introduced.
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/commit/98a83e1b98c61d80bdf6608c2e71124036b7583f
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/commit/013f2a91c7651546f50c04c17ff22ed3d69bcf93

### Build (reviewed)

The primary merge adds a title/options menu, two-button joystick controls, sound test, cheat fly mode and F2 level skip, with upstream menu, fly-mode and smooth-scroll tests across the enhanced branch. Limitations: The tracker did not assemble or run the disk. Emulator coverage does not establish physical-hardware compatibility or a complete minimum machine profile.
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/commit/013f2a91c7651546f50c04c17ff22ed3d69bcf93

### Runtime profiles (no-evidence-found)

The documentation gives tested emulator configurations and a 512 KiB mirror-cache design constraint but does not state a complete minimum CPU, chip/fast RAM, chipset and Kickstart profile for the enhanced variant.
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/commit/013f2a91c7651546f50c04c17ff22ed3d69bcf93

### AI (reviewed)

The reviewed merge explicitly credits Claude Opus 5.5 and links its session; attribution is limited to that evidenced work.
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/commit/013f2a91c7651546f50c04c17ff22ed3d69bcf93

### Relationships (reviewed)

The exact rebuild and enhanced branch are variants of the same Amiga title project; proposed menu/input work remains a TODO rather than a separately promoted project.
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/commit/96983457501d34c21112f768a2cf3b6784699283
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/commit/013f2a91c7651546f50c04c17ff22ed3d69bcf93

## space-station-silicon-valley-decompilation

Project ID: space-station-silicon-valley-decompilation · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "space-station-silicon-valley-decompilation",
  "last_activity": "2026-10-27",
  "last_checked": "2026-10-28",
  "status": "Work-in-progress Nintendo 64 decompilation; upstream now reports 93% matching for the US build, while EU support and NON_MATCHING functional paths remain distinct from completed source recovery.",
  "techniques": [
    "region-separated matching progress accounting"
  ]
}
```

Expected existing project SHA256: cb1040bc922a8abe538e4cad205d89265353475689aaaaf06b9417f79916bb09

### Identity (reviewed)

US/EU source with actual C routines. EU assembly support is not equal to US decompilation progress; NON_MATCHING functional paths are distinct from byte-perfect matching. Own ROM required.
- https://github.com/mkst/sssv
- https://github.com/mkst/sssv/blob/8bff37d73ce5909737f35f1abf2b5f1d1094e76f/src.us/core/controller.c
- https://github.com/mkst/sssv/blob/8bff37d73ce5909737f35f1abf2b5f1d1094e76f/README.md
- https://github.com/mkst/sssv/commit/27c472eb01d2990a832a1a12c0b083c7fd240e14

### Classification (reviewed)

Inspected source supports game / decompilation. US/EU source with actual C routines. EU assembly support is not equal to US decompilation progress; NON_MATCHING functional paths are distinct from byte-perfect matching. Own ROM required.
- https://github.com/mkst/sssv
- https://github.com/mkst/sssv/blob/8bff37d73ce5909737f35f1abf2b5f1d1094e76f/src.us/core/controller.c
- https://github.com/mkst/sssv/blob/8bff37d73ce5909737f35f1abf2b5f1d1094e76f/README.md
- https://github.com/mkst/sssv/commit/27c472eb01d2990a832a1a12c0b083c7fd240e14

### Source CPU (reviewed)

Source architecture: MIPS.
- https://github.com/mkst/sssv
- https://github.com/mkst/sssv/blob/8bff37d73ce5909737f35f1abf2b5f1d1094e76f/src.us/core/controller.c
- https://github.com/mkst/sssv/blob/8bff37d73ce5909737f35f1abf2b5f1d1094e76f/README.md
- https://github.com/mkst/sssv/commit/27c472eb01d2990a832a1a12c0b083c7fd240e14

### Target CPU (reviewed)

Target architecture: MIPS.
- https://github.com/mkst/sssv
- https://github.com/mkst/sssv/blob/8bff37d73ce5909737f35f1abf2b5f1d1094e76f/src.us/core/controller.c
- https://github.com/mkst/sssv/blob/8bff37d73ce5909737f35f1abf2b5f1d1094e76f/README.md
- https://github.com/mkst/sssv/commit/27c472eb01d2990a832a1a12c0b083c7fd240e14

### Build (reviewed)

The primary 93% update changes multiple US source units and reports 93% matching progress for the US build; the README continues to distinguish EU support and NON_MATCHING functional paths from matching reconstruction. Limitations: The tracker did not build or hash a ROM. The percentage is an upstream aggregate and does not establish complete source recovery, runtime fidelity or EU parity.
- https://github.com/mkst/sssv/commit/27c472eb01d2990a832a1a12c0b083c7fd240e14

### Runtime profiles (no-evidence-found)

No independently verified minimum hardware profile established.
- https://github.com/mkst/sssv
- https://github.com/mkst/sssv/blob/8bff37d73ce5909737f35f1abf2b5f1d1094e76f/src.us/core/controller.c
- https://github.com/mkst/sssv/blob/8bff37d73ce5909737f35f1abf2b5f1d1094e76f/README.md
- https://github.com/mkst/sssv/commit/27c472eb01d2990a832a1a12c0b083c7fd240e14

### AI (no-evidence-found)

No explicit completed-work AI disclosure established in inspected evidence. Config files, workflow instructions and algorithmic neural features alone are not proof of authorship.
- https://github.com/mkst/sssv
- https://github.com/mkst/sssv/blob/8bff37d73ce5909737f35f1abf2b5f1d1094e76f/src.us/core/controller.c
- https://github.com/mkst/sssv/blob/8bff37d73ce5909737f35f1abf2b5f1d1094e76f/README.md
- https://github.com/mkst/sssv/commit/27c472eb01d2990a832a1a12c0b083c7fd240e14

### Relationships (reviewed)

Screened URL, title and prior decisions. GitHub fork flag is not treated as conclusive lineage evidence.
- https://github.com/mkst/sssv
- https://github.com/mkst/sssv/blob/8bff37d73ce5909737f35f1abf2b5f1d1094e76f/src.us/core/controller.c
- https://github.com/mkst/sssv/blob/8bff37d73ce5909737f35f1abf2b5f1d1094e76f/README.md
- https://github.com/mkst/sssv/commit/27c472eb01d2990a832a1a12c0b083c7fd240e14

## cdlewis-snowboardkids-decomp

Project ID: cdlewis-snowboardkids-decomp · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "cdlewis-snowboardkids-decomp",
  "last_activity": "2026-10-27",
  "last_checked": "2026-10-28",
  "status": "Nintendo 64 matching reconstruction; the US course-select player-panel update was simplified while preserving its exact match, without implying whole-project or regional completion.",
  "techniques": [
    "source simplification under exact-match constraints"
  ]
}
```

Expected existing project SHA256: cbce81c2fc6f5ecc6bd01a0c31f4f535fec8c90d07b1c8a59ba64074e63f0192

### Identity (reviewed)

Snowboard Kids — N64 matching reconstruction. Repository root and implementation inspected at pinned revisions.
- https://github.com/cdlewis/snowboardkids-decomp/blob/a9a845ba9747edb3124daf1c8d9ee5951af3c924/README.md
- https://github.com/cdlewis/snowboardkids-decomp/blob/a9a845ba9747edb3124daf1c8d9ee5951af3c924/src.jp/audio/scheduler.c
- https://github.com/cdlewis/snowboardkids-decomp
- https://github.com/cdlewis/snowboardkids-decomp/commit/2cc5a236faeb9ae67db6efd9f1123200a033bbd9

### Classification (reviewed)

Matching original-target reconstruction with region-specific code/data progress and recovered scheduler/audio structures. Not a PC port; original asset extraction remains required.
- https://github.com/cdlewis/snowboardkids-decomp/blob/a9a845ba9747edb3124daf1c8d9ee5951af3c924/README.md
- https://github.com/cdlewis/snowboardkids-decomp/blob/a9a845ba9747edb3124daf1c8d9ee5951af3c924/src.jp/audio/scheduler.c
- https://github.com/cdlewis/snowboardkids-decomp
- https://github.com/cdlewis/snowboardkids-decomp/commit/2cc5a236faeb9ae67db6efd9f1123200a033bbd9

### Source CPU (reviewed)

Architecture context: mips. Source and target roles are recorded separately.
- https://github.com/cdlewis/snowboardkids-decomp/blob/a9a845ba9747edb3124daf1c8d9ee5951af3c924/README.md
- https://github.com/cdlewis/snowboardkids-decomp/blob/a9a845ba9747edb3124daf1c8d9ee5951af3c924/src.jp/audio/scheduler.c
- https://github.com/cdlewis/snowboardkids-decomp
- https://github.com/cdlewis/snowboardkids-decomp/commit/2cc5a236faeb9ae67db6efd9f1123200a033bbd9

### Target CPU (reviewed)

Explicit output/execution architecture: mips.
- https://github.com/cdlewis/snowboardkids-decomp/blob/a9a845ba9747edb3124daf1c8d9ee5951af3c924/README.md
- https://github.com/cdlewis/snowboardkids-decomp/blob/a9a845ba9747edb3124daf1c8d9ee5951af3c924/src.jp/audio/scheduler.c
- https://github.com/cdlewis/snowboardkids-decomp
- https://github.com/cdlewis/snowboardkids-decomp/commit/2cc5a236faeb9ae67db6efd9f1123200a033bbd9

### Build (reviewed)

The primary commit simplifies the US course-select player-panel update while preserving the function's exact match against the original target. Limitations: The exactness claim is bounded to the changed routine; the tracker did not build or compare a ROM and does not extend it to whole-project or other-region completion.
- https://github.com/cdlewis/snowboardkids-decomp/commit/2cc5a236faeb9ae67db6efd9f1123200a033bbd9

### Runtime profiles (no-evidence-found)

No verified minimum CPU/RAM/OS profile established beyond the qualified dependency and format notes; no runtime test was performed.
- https://github.com/cdlewis/snowboardkids-decomp/blob/a9a845ba9747edb3124daf1c8d9ee5951af3c924/README.md
- https://github.com/cdlewis/snowboardkids-decomp/blob/a9a845ba9747edb3124daf1c8d9ee5951af3c924/src.jp/audio/scheduler.c
- https://github.com/cdlewis/snowboardkids-decomp
- https://github.com/cdlewis/snowboardkids-decomp/commit/2cc5a236faeb9ae67db6efd9f1123200a033bbd9

### AI (no-evidence-found)

No explicit development-AI contribution disclosure was established in the inspected material; absence does not establish non-use. Agent configuration or MCP integration alone does not establish authorship.
- https://github.com/cdlewis/snowboardkids-decomp/blob/a9a845ba9747edb3124daf1c8d9ee5951af3c924/README.md
- https://github.com/cdlewis/snowboardkids-decomp/blob/a9a845ba9747edb3124daf1c8d9ee5951af3c924/src.jp/audio/scheduler.c
- https://github.com/cdlewis/snowboardkids-decomp
- https://github.com/cdlewis/snowboardkids-decomp/commit/2cc5a236faeb9ae67db6efd9f1123200a033bbd9

### Relationships (reviewed)

Distinct from the already tracked sequel Snowboard Kids2; avoid title-family deduplication that merges separate games.
- https://github.com/cdlewis/snowboardkids-decomp/blob/a9a845ba9747edb3124daf1c8d9ee5951af3c924/README.md
- https://github.com/cdlewis/snowboardkids-decomp/blob/a9a845ba9747edb3124daf1c8d9ee5951af3c924/src.jp/audio/scheduler.c
- https://github.com/cdlewis/snowboardkids-decomp
- https://github.com/cdlewis/snowboardkids-decomp/commit/2cc5a236faeb9ae67db6efd9f1123200a033bbd9

## openrac-rac1-decomp

Project ID: openrac-rac1-decomp · Overall audit: partial

### Typed catalogue changes

```json
{
  "ai": {
    "evidence": [
      "Claude project instructions/configuration present (configuration only; does not establish AI contribution)",
      "Codex co-author trailer observed in recent tracked commits: 8 in this scan (example 3af68fae6f9b; Codex (GPT-6))",
      "Claude co-author trailer observed in recent tracked commits: 24 in this scan (example 04f012c1f4ca; Claude Opus 5.5)"
    ],
    "tools": [
      "Claude",
      "Codex"
    ],
    "usage": true
  },
  "id": "openrac-rac1-decomp",
  "last_activity": "2026-10-27",
  "last_checked": "2026-10-28",
  "status": "PAL 2.00 PlayStation 2 matching reconstruction; the hero refactor types sound slots and draw queues and removes overlay-private hero structures, while matching and playability remain upstream work in progress.",
  "techniques": [
    "shared-structure recovery across overlays",
    "typed sound-slot and draw-queue recovery"
  ]
}
```

Expected existing project SHA256: 21c6edbff90a9498ae1baf78ce8b39f9a6aaa489e6e4de137259217c05ad3cea

### Identity (reviewed)

Ratchet and Clank — PS2 matching reconstruction. Repository root and implementation inspected at pinned revisions.
- https://github.com/OpenRAC/rac1-decomp/blob/813090403fe822acd929616da0fee2081131f92e/README.md
- https://github.com/OpenRAC/rac1-decomp/blob/813090403fe822acd929616da0fee2081131f92e/Makefile.sn
- https://github.com/OpenRAC/rac1-decomp
- https://github.com/OpenRAC/rac1-decomp/commit/209d3381ebaa8c06d5df98eeabad4adad45bdfb7

### Classification (reviewed)

PAL2.00 reconstruction links recovered functions at original addresses and fills gaps from local disassembly. Readability refinement and future PC reimplementation remain separate work.
- https://github.com/OpenRAC/rac1-decomp/blob/813090403fe822acd929616da0fee2081131f92e/README.md
- https://github.com/OpenRAC/rac1-decomp/blob/813090403fe822acd929616da0fee2081131f92e/Makefile.sn
- https://github.com/OpenRAC/rac1-decomp
- https://github.com/OpenRAC/rac1-decomp/commit/209d3381ebaa8c06d5df98eeabad4adad45bdfb7

### Source CPU (reviewed)

Architecture context: mips. Source and target roles are recorded separately.
- https://github.com/OpenRAC/rac1-decomp/blob/813090403fe822acd929616da0fee2081131f92e/README.md
- https://github.com/OpenRAC/rac1-decomp/blob/813090403fe822acd929616da0fee2081131f92e/Makefile.sn
- https://github.com/OpenRAC/rac1-decomp
- https://github.com/OpenRAC/rac1-decomp/commit/209d3381ebaa8c06d5df98eeabad4adad45bdfb7

### Target CPU (reviewed)

Explicit output/execution architecture: mips.
- https://github.com/OpenRAC/rac1-decomp/blob/813090403fe822acd929616da0fee2081131f92e/README.md
- https://github.com/OpenRAC/rac1-decomp/blob/813090403fe822acd929616da0fee2081131f92e/Makefile.sn
- https://github.com/OpenRAC/rac1-decomp
- https://github.com/OpenRAC/rac1-decomp/commit/209d3381ebaa8c06d5df98eeabad4adad45bdfb7

### Build (reviewed)

The primary refactor introduces shared typed hero sound-slot and draw-queue structures and removes private overlay copies while retaining the project's original-address reconstruction model. Limitations: The tracker did not compile with the period toolchains or independently compare the result; structural cleanup alone does not establish whole-project matching or playability.
- https://github.com/OpenRAC/rac1-decomp/commit/209d3381ebaa8c06d5df98eeabad4adad45bdfb7

### Runtime profiles (no-evidence-found)

No verified minimum CPU/RAM/OS profile established beyond the qualified dependency and format notes; no runtime test was performed.
- https://github.com/OpenRAC/rac1-decomp/blob/813090403fe822acd929616da0fee2081131f92e/README.md
- https://github.com/OpenRAC/rac1-decomp/blob/813090403fe822acd929616da0fee2081131f92e/Makefile.sn
- https://github.com/OpenRAC/rac1-decomp
- https://github.com/OpenRAC/rac1-decomp/commit/209d3381ebaa8c06d5df98eeabad4adad45bdfb7

### AI (reviewed)

Recent primary commit trailers explicitly credit both Codex and Claude on this repository; project-level attribution remains limited to those evidenced commits and is not inferred from configuration files.
- https://github.com/OpenRAC/rac1-decomp/commit/3af68fae6f9b
- https://github.com/OpenRAC/rac1-decomp/commit/04f012c1f4ca
- https://github.com/OpenRAC/rac1-decomp/commit/209d3381ebaa8c06d5df98eeabad4adad45bdfb7

### Relationships (reviewed)

Two original code segments use different compiler sub-builds; one toolchain label is insufficient for reproducibility.
- https://github.com/OpenRAC/rac1-decomp/blob/813090403fe822acd929616da0fee2081131f92e/README.md
- https://github.com/OpenRAC/rac1-decomp/blob/813090403fe822acd929616da0fee2081131f92e/Makefile.sn
- https://github.com/OpenRAC/rac1-decomp
- https://github.com/OpenRAC/rac1-decomp/commit/209d3381ebaa8c06d5df98eeabad4adad45bdfb7

## gustavocanepa-gt4-decomp

Project ID: gustavocanepa-gt4-decomp · Overall audit: partial

### Typed catalogue changes

```json
{
  "ai": {
    "evidence": [
      "Claude project instructions/configuration present (configuration only; does not establish AI contribution)",
      "Agent project instructions/configuration present (configuration only; does not establish AI contribution)",
      "Explicit Claude involvement in tracked commit d47be0938ec5: \"Large function with Claude Fable: 1 of 3; knowledge: argument arrays, widget-event stack layout, early-return constants\"",
      "Explicit Claude involvement in tracked commit be220f08a1ca: \"Large functions with Claude Fable: 3 of 3; knowledge: padded string unions, byte-offset matrix loops, 64-bit field masks\"",
      "Explicit Claude involvement in tracked commit 803abafd7acb: \"Large functions with Claude Fable: 2 of 3; knowledge: branch-scoped pointers, overlapping-branch unions, two-callback registration\"",
      "Explicit Claude involvement in tracked commit d3fe19020ab5: \"Large functions with Claude Fable: 3 of 3; knowledge: stack layouts with gaps, per-block results, string pointer lifetime\"",
      "Explicit Claude involvement in tracked commit dfdb0f88c15d: \"Large functions with Claude Fable: 2 more of 3; knowledge: ctor results, union-typed vectors and members\"",
      "Explicit Claude involvement in tracked commit 97b8ee3879ce: \"Large functions with Claude Fable: 3 of 3; knowledge: union slots, hidden-pointer returns, inline accessors, string triple\"",
      "Explicit Claude involvement in tracked commit 01e0ca47b25f: \"Large functions with Claude Fable: 2 more of 3; knowledge: vptr aliasing, partial struct addressing, handle-assign idiom\"",
      "Explicit Claude involvement in tracked commit 78bcc3284164: \"First large functions matched with Claude Fable (2 of 3); knowledge: bitfields, vec-init loops, handle temporaries\"",
      "Explicit Claude Sonnet 5.5 co-author trailer in reviewed commit 0bb9c22e24a6",
      "Claude co-author trailer observed in recent tracked commits: 6 in this scan (example ca851d2a956b; Claude Sonnet 5.5)",
      "Explicit upstream commit attribution: Co-Authored-By: Claude Sonnet 5.5. https://github.com/gustavocanepa/gt4-decomp/commit/ca851d2a956beb28917f8d00cbc26cf71a455b8d"
    ],
    "tools": [
      "Claude"
    ],
    "usage": true
  },
  "id": "gustavocanepa-gt4-decomp",
  "last_activity": "2026-10-27",
  "last_checked": "2026-10-28",
  "status": "Gran Turismo 4 PS2 reconstruction now reports 30,157 of 30,875 matching functions (97.7%), 89.0% matching code bytes and 87.3% clean source; the separate experimental native port is not represented as playable.",
  "techniques": [
    "cross-game function matching",
    "objdiff progress accounting",
    "source-cleanliness reporting",
    "data-source reconstruction accounting",
    "function/code/data progress separation"
  ]
}
```

Expected existing project SHA256: c093cd136e21ecd3d14efbff7f783683f70fb98905441b5434eaff0b4e05ac58

### Identity (reviewed)

Gran Turismo 4 — PS2 engine reconstruction. Repository root and implementation inspected at pinned revisions.
- https://github.com/gustavocanepa/gt4-decomp/blob/0d055fc01f5c9fa53bdef69a9967845ba28a15cd/README.md
- https://github.com/gustavocanepa/gt4-decomp/blob/0d055fc01f5c9fa53bdef69a9967845ba28a15cd/tools/clean_report.py
- https://github.com/gustavocanepa/gt4-decomp/blob/0d055fc01f5c9fa53bdef69a9967845ba28a15cd/src/startup/CarIconMaker/GranTurismo4__GameObjectPS2__internal_render.c
- https://github.com/gustavocanepa/gt4-decomp
- https://github.com/gustavocanepa/gt4-decomp/commit/0bb9c22e24a65ab3b9938cee6e1afb06f5bf7856
- https://github.com/gustavocanepa/gt4-decomp/commit/ca851d2a956beb28917f8d00cbc26cf71a455b8d

### Classification (reviewed)

The reviewed repository remains the matching PS2 CORE.GT4 reconstruction for NTSC-U SCUS-97328 v1.01. Its separately linked gt4-native experiment is not conflated with this record or represented as a playable PC port.
- https://github.com/gustavocanepa/gt4-decomp/commit/ca851d2a956beb28917f8d00cbc26cf71a455b8d

### Source CPU (reviewed)

Architecture context: mips. Source and target roles are recorded separately.
- https://github.com/gustavocanepa/gt4-decomp/blob/0d055fc01f5c9fa53bdef69a9967845ba28a15cd/README.md
- https://github.com/gustavocanepa/gt4-decomp/blob/0d055fc01f5c9fa53bdef69a9967845ba28a15cd/tools/clean_report.py
- https://github.com/gustavocanepa/gt4-decomp/blob/0d055fc01f5c9fa53bdef69a9967845ba28a15cd/src/startup/CarIconMaker/GranTurismo4__GameObjectPS2__internal_render.c
- https://github.com/gustavocanepa/gt4-decomp
- https://github.com/gustavocanepa/gt4-decomp/commit/0bb9c22e24a65ab3b9938cee6e1afb06f5bf7856
- https://github.com/gustavocanepa/gt4-decomp/commit/ca851d2a956beb28917f8d00cbc26cf71a455b8d

### Target CPU (reviewed)

Explicit output/execution architecture: mips.
- https://github.com/gustavocanepa/gt4-decomp/blob/0d055fc01f5c9fa53bdef69a9967845ba28a15cd/README.md
- https://github.com/gustavocanepa/gt4-decomp/blob/0d055fc01f5c9fa53bdef69a9967845ba28a15cd/tools/clean_report.py
- https://github.com/gustavocanepa/gt4-decomp/blob/0d055fc01f5c9fa53bdef69a9967845ba28a15cd/src/startup/CarIconMaker/GranTurismo4__GameObjectPS2__internal_render.c
- https://github.com/gustavocanepa/gt4-decomp
- https://github.com/gustavocanepa/gt4-decomp/commit/0bb9c22e24a65ab3b9938cee6e1afb06f5bf7856
- https://github.com/gustavocanepa/gt4-decomp/commit/ca851d2a956beb28917f8d00cbc26cf71a455b8d

### Build (reviewed)

The pinned README reports 30,157 of 30,875 matching functions (97.7%), 89.0% matching code bytes, 87.3% clean source, 30,128 functions linked from C/C++, and 68,346 of 2,664,152 data bytes reconstructed. Limitations: These are upstream progress counters. The tracker did not compile, link, boot or play the reconstruction, and the counters do not establish complete data recovery.
- https://github.com/gustavocanepa/gt4-decomp/commit/ca851d2a956beb28917f8d00cbc26cf71a455b8d

### Runtime profiles (no-evidence-found)

No verified minimum CPU/RAM/OS profile established beyond the qualified dependency and format notes; no runtime test was performed.
- https://github.com/gustavocanepa/gt4-decomp/blob/0d055fc01f5c9fa53bdef69a9967845ba28a15cd/README.md
- https://github.com/gustavocanepa/gt4-decomp/blob/0d055fc01f5c9fa53bdef69a9967845ba28a15cd/tools/clean_report.py
- https://github.com/gustavocanepa/gt4-decomp/blob/0d055fc01f5c9fa53bdef69a9967845ba28a15cd/src/startup/CarIconMaker/GranTurismo4__GameObjectPS2__internal_render.c
- https://github.com/gustavocanepa/gt4-decomp
- https://github.com/gustavocanepa/gt4-decomp/commit/0bb9c22e24a65ab3b9938cee6e1afb06f5bf7856
- https://github.com/gustavocanepa/gt4-decomp/commit/ca851d2a956beb28917f8d00cbc26cf71a455b8d

### AI (reviewed)

The reviewed progress commit explicitly credits Claude Sonnet 5.5 as co-author; attribution is limited to evidenced work.
- https://github.com/gustavocanepa/gt4-decomp/commit/ca851d2a956beb28917f8d00cbc26cf71a455b8d

### Relationships (reviewed)

Tourist Trophy sharing and duplicate functions can inflate function counts relative to unique logic; clean-report filters are not semantic proof.
- https://github.com/gustavocanepa/gt4-decomp/blob/0d055fc01f5c9fa53bdef69a9967845ba28a15cd/README.md
- https://github.com/gustavocanepa/gt4-decomp/blob/0d055fc01f5c9fa53bdef69a9967845ba28a15cd/tools/clean_report.py
- https://github.com/gustavocanepa/gt4-decomp/blob/0d055fc01f5c9fa53bdef69a9967845ba28a15cd/src/startup/CarIconMaker/GranTurismo4__GameObjectPS2__internal_render.c
- https://github.com/gustavocanepa/gt4-decomp
- https://github.com/gustavocanepa/gt4-decomp/commit/0bb9c22e24a65ab3b9938cee6e1afb06f5bf7856
- https://github.com/gustavocanepa/gt4-decomp/commit/ca851d2a956beb28917f8d00cbc26cf71a455b8d

## faxanadu-nes-mstan-recomp

Project ID: faxanadu-nes-mstan-recomp · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "faxanadu-nes-mstan-recomp",
  "last_activity": "2026-10-27",
  "last_checked": "2026-10-28",
  "status": "Playable NES-to-PC static recompilation; v2.5.0 adds an experimental Seamless mod, disabled by default, while cross-room combat/projectile behavior and broad progression testing remain incomplete.",
  "techniques": [
    "NESRecomp",
    "6502-to-C static recompilation",
    "ROM checksum gating",
    "Nestopia oracle comparison",
    "generated native code",
    "native/interpreter agreement testing",
    "experimental cross-room actor continuity"
  ]
}
```

Expected existing project SHA256: f3d03bd674e3710c65733341240a59763d89d4f1eeb637e2ab659e7bbaba1287

### Identity (reviewed)

The identity decision remains unchanged after reviewing the current primary commit.
- https://github.com/mstan/FaxanaduRecomp/commit/f743ae4c87406947de7a6a61cacd2cc036ca631c

### Classification (reviewed)

The classification decision remains unchanged after reviewing the current primary commit.
- https://github.com/mstan/FaxanaduRecomp/commit/f743ae4c87406947de7a6a61cacd2cc036ca631c

### Source CPU (reviewed)

Primary README explicitly identifies original NES 6502 ROM machine code as the recompilation input.
- https://github.com/mstan/FaxanaduRecomp/commit/f743ae4c87406947de7a6a61cacd2cc036ca631c

### Target CPU (reviewed)

Primary README explicitly says generated C is compiled to native x64.
- https://github.com/mstan/FaxanaduRecomp/commit/f743ae4c87406947de7a6a61cacd2cc036ca631c

### Build (reviewed)

The v2.5.0 primary release commit puts the experimental Seamless mod first in the Mods menu, disabled by default, with moving neighboring actors and adaptive fit-to-screen behavior; it is mutually exclusive with Play as Link. Limitations: Upstream records preliminary owner playtesting and native/interpreter agreement, but broader progression, bosses and secrets remain open and cross-room combat/projectiles are incomplete; the tracker did not run the release.
- https://github.com/mstan/FaxanaduRecomp/commit/f743ae4c87406947de7a6a61cacd2cc036ca631c

### Runtime profiles (no-evidence-found)

The reviewed release and README do not state a minimum host CPU, RAM or OS version; no runtime floor is inferred from the generated x64 target.
- https://github.com/mstan/FaxanaduRecomp/commit/f743ae4c87406947de7a6a61cacd2cc036ca631c

### AI (no-evidence-found)

A bounded review of the current release commit and project documentation found no explicit development-AI contribution disclosure; absence does not establish non-use.
- https://github.com/mstan/FaxanaduRecomp/commit/f743ae4c87406947de7a6a61cacd2cc036ca631c

### Relationships (reviewed)

Primary README identifies NESRecomp as the shared framework; this repository has an independent title-specific configuration, generated output and status boundary.
- https://github.com/mstan/FaxanaduRecomp/commit/f743ae4c87406947de7a6a61cacd2cc036ca631c

## Research event notes

The CPU audit queue contained zero unresolved source/target CPU areas, so this pass resolved zero CPU audit areas rather than inventing work. Primary commits and pinned documentation were reviewed; no upstream project was compiled or executed, and no runtime minimum was inferred from platform, source language, guest benchmark recipes or broad architecture family.
