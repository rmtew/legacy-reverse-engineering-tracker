# Upstream fidelity and runtime-evidence maintenance

Review ten material upstream changes across reconstruction fidelity, decompilation, ports, networking and original-hardware evidence.

Date: 2026-10-29 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- marek177-nitemare3d-reversed / Target CPU (no-evidence-found): No explicit minimum host ISA established; do not infer one from the host operating system.
- marek177-nitemare3d-reversed / Build (needs-research): The caller-contract run intercepts the original blitter, the viewport run mocks two downstream dependencies, and neither establishes full DOS/VGA reachability, save/load parity or playable-game fidelity. Next check: Connect the bounded save, viewport and blitter findings to original runtime execution, framebuffer output and end-to-end save/load checks.
- marek177-nitemare3d-reversed / Runtime profiles (no-evidence-found): No independent hardware compatibility or minimum memory/CPU testing; dependencies and limits are recorded in build notes.
- virtua-tennis-dreamcast-analysis / Build (reviewed): These are upstream counters and per-function equivalence results. Some newly proven functions have explicitly thin instruction coverage, and the tracker did not run the suite or boot a reconstructed disc. Next check: Track the remaining 18 C-capable functions and require the project to keep function proof, eligible-byte completion and aggregate coverage separate.
- virtua-tennis-dreamcast-analysis / Runtime profiles (no-evidence-found): No minimum Dreamcast accessory/model profile or host runtime minimum is stated in the inspected decompilation documentation.
- firestaff-dungeon-master-engine / Build (needs-research): The Nexus replay verifies a retail reference flow in Ymir, not Firestaff's Continue implementation or input parity. The source-frame trace is diagnostic and does not establish native FM Towns presentation parity. Next check: Bind the cold-boot BKR scan/load path and compare Firestaff Continue, HUD, viewport and startup presentation against the authenticated references.
- openrac-rac1-decomp / Build (reviewed): The tracker did not compile with the period toolchains or independently compare the result; type consolidation is not a whole-project matching or playability claim. Next check: Follow matching reports and toolchain reproducibility evidence independently of structural typing progress.
- openrac-rac1-decomp / Runtime profiles (no-evidence-found): No verified minimum CPU/RAM/OS profile established beyond the qualified dependency and format notes; no runtime test was performed.
- kharn27-esp32-locomotive-basic / Build (reviewed): The size and ABI readings are build/ELF evidence, not hardware measurements. The report remains ON_DEVICE_UNVERIFIED, and the pre-B C99 implementation still classifies all 14 STRING cases as unsupported. Next check: Repeat the final-head CI and perform the explicitly requested flash/monitor hardware run before recording any runnable-device profile.
- kharn27-esp32-locomotive-basic / Runtime profiles (no-evidence-found): No independent hardware compatibility or minimum memory/CPU testing; dependencies and limits are recorded in build notes.
- zapple-ii-bpm-prodos-softcard-environment / Build (reviewed): The tracker reviewed source changes only; it did not assemble the image, exercise W5100 hardware or verify Telnet/WGET interoperability. Next check: Retain kernel/socket ownership boundaries and seek reproducible Apple IIe/SoftCard network execution evidence.
- zapple-ii-bpm-prodos-softcard-environment / Runtime profiles (no-evidence-found): The reviewed terminal and CP/M changes do not state a minimum Apple IIe revision, RAM, SoftCard model, ROM or display requirement. No minimum is inferred from the 6502/Z80 code.
- zapple-ii-bpm-prodos-softcard-environment / AI (no-evidence-found): Unknown: bounded primary documentation, sampled implementation/build/licence files and up to three latest full commit messages contain no explicit AI-contribution attribution. Absence is not evidence of non-use.
- ambermoon / Build (reviewed): Acceptance is upstream listening/conversion evidence. The tracker did not rebuild the port, compare generated player bytes or audit audible parity for each song. Next check: Follow reproducible port builds and retain per-song acceptance separately from complete music or game parity.
- amberstar-amber-framework / Source CPU (no-evidence-found): Reviewed project documentation identifies legacy Atari ST, Amiga, DOS data or game heritage, but does not establish analyzed original CPU instructions; architecture is not inferred from the platform alone.
- amberstar-amber-framework / Target CPU (no-evidence-found): Reviewed source/build documentation names platforms or language/runtime but no explicit output CPU architecture; no target CPU is inferred from Java, C#, C/C++, or a portable framework.
- amberstar-amber-framework / Build (reviewed): The tracker did not run the game or compare audio/video output to original Amiga hardware; these bounded data, outro and player paths do not establish complete-game parity. Next check: Track scenario tests and original-output comparisons for the expanded Amiga-specific paths.
- amberstar-amber-framework / Runtime profiles (no-evidence-found): The gameplay slice adds no explicit minimum host CPU, RAM, OS or mobile-device profile.
- simcity-spectrum-z80-suborb / Target CPU (no-evidence-found): The reviewed distribution and per-machine documentation establish output platforms but do not explicitly establish a processor architecture for every produced variant. No target CPU is inferred from platform names, z88dk or shared source.
- simcity-spectrum-z80-suborb / Build (reviewed): The Aquarius+ commit explicitly leaves text transparency, popup colour and border remapping unverified on hardware. The tracker did not build or run any target. Next check: Seek hardware evidence for the Aquarius+ layer composition while keeping platform-specific UI verification separate.
- simcity-spectrum-z80-suborb / Runtime profiles (no-evidence-found): Per-platform documentation records media, display, audio and file-system behavior, but the reviewed change does not state verified minimum CPU, RAM, ROM or machine revisions. No runtime minimum is inferred.
- simcity-spectrum-z80-suborb / AI (no-evidence-found): No explicit development-AI disclosure was found in the reviewed commit and distribution documentation; non-use is not established.
- aminetxduo-classic-amiga-ip-stack / Build (reviewed): The reviewed top-level commits pin dependency revisions; the tracker did not run TCP fault-injection tests or repeat the physical Amiga network test. Next check: Retain the physical A3000/A2065 profile and seek end-to-end recovery evidence before broadening runtime or interoperability claims.

## marek177-nitemare3d-reversed

Project ID: marek177-nitemare3d-reversed · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "marek177-nitemare3d-reversed",
  "last_activity": "2026-10-28",
  "last_checked": "2026-10-29",
  "status": "Six-image DOS analysis now fixes the 55,015-byte save-slot layout, exercises caller/blitter contracts in 4,536 cases, and traces the default viewport split chain in 492 cases; runtime reachability, VGA output and whole-game parity remain open.",
  "techniques": [
    "scoped real-mode p-code modelling",
    "cross-version renderer ownership verification",
    "save-slot layout verification",
    "blitter caller-contract verification",
    "viewport split-chain provenance"
  ]
}
```

Expected existing project SHA256: 316e3c7138893d05c72dcfd54f59a69429db266b6318f44d778f1dffa3b747de

### Identity (reviewed)

Nitemare 3D — DOS/Win16 research and partial C++ engine. Repository identity, pinned tree and available implementation inspected.
- https://github.com/marek177/Nitemare3d-reversed/blob/f5c37abbbdc3ff8bd806af10fb1eb6dd01e9df68/README.md
- https://github.com/marek177/Nitemare3d-reversed/blob/f5c37abbbdc3ff8bd806af10fb1eb6dd01e9df68/src/game/LevelState.cpp

### Classification (reviewed)

Detailed original runtime/static findings integrated into partial C++/SDL3 components. Inspected structured map/player/level state; DOS and Win16 evidence are separately bounded.
- https://github.com/marek177/Nitemare3d-reversed/blob/f5c37abbbdc3ff8bd806af10fb1eb6dd01e9df68/README.md
- https://github.com/marek177/Nitemare3d-reversed/blob/f5c37abbbdc3ff8bd806af10fb1eb6dd01e9df68/src/game/LevelState.cpp

### Source CPU (reviewed)

Documented original ISA: x86.
- https://github.com/marek177/Nitemare3d-reversed/blob/f5c37abbbdc3ff8bd806af10fb1eb6dd01e9df68/README.md
- https://github.com/marek177/Nitemare3d-reversed/blob/f5c37abbbdc3ff8bd806af10fb1eb6dd01e9df68/src/game/LevelState.cpp

### Target CPU (no-evidence-found)

No explicit minimum host ISA established; do not infer one from the host operating system.
- https://github.com/marek177/Nitemare3d-reversed/blob/f5c37abbbdc3ff8bd806af10fb1eb6dd01e9df68/README.md
- https://github.com/marek177/Nitemare3d-reversed/blob/f5c37abbbdc3ff8bd806af10fb1eb6dd01e9df68/src/game/LevelState.cpp

### Build (needs-research)

The reviewed pass 21, 25 and 26 reports account for the fixed 55,015-byte Win16 save slot, exercise signed page-gate and split-boundary caller contracts in 4,536 cases, and verify 492 default viewport setter-to-blitter chains across six DOS images. Limitations: The caller-contract run intercepts the original blitter, the viewport run mocks two downstream dependencies, and neither establishes full DOS/VGA reachability, save/load parity or playable-game fidelity. Next check: Connect the bounded save, viewport and blitter findings to original runtime execution, framebuffer output and end-to-end save/load checks.
- https://github.com/marek177/Nitemare3d-reversed/commit/154f6539cc8fa48edf88ef9dbf5d489895bc69bf
- https://github.com/marek177/Nitemare3d-reversed/commit/c5bd56d950c3d829ac6c647797219ed919829f87
- https://github.com/marek177/Nitemare3d-reversed/commit/b743f999a2eb30876467dcc39b091719a5438b65

### Runtime profiles (no-evidence-found)

No independent hardware compatibility or minimum memory/CPU testing; dependencies and limits are recorded in build notes.
- https://github.com/marek177/Nitemare3d-reversed/blob/f5c37abbbdc3ff8bd806af10fb1eb6dd01e9df68/README.md
- https://github.com/marek177/Nitemare3d-reversed/blob/f5c37abbbdc3ff8bd806af10fb1eb6dd01e9df68/src/game/LevelState.cpp

### AI (reviewed)

README identifies AI-assisted reverse-engineering project; specific development AI not established in inspected evidence.
- https://github.com/marek177/Nitemare3d-reversed/blob/f5c37abbbdc3ff8bd806af10fb1eb6dd01e9df68/README.md
- https://github.com/marek177/Nitemare3d-reversed/blob/f5c37abbbdc3ff8bd806af10fb1eb6dd01e9df68/src/game/LevelState.cpp

### Relationships (reviewed)

Distinct from directory-format-only Nitemare research. AI assistance explicit but tool identity not established here.
- https://github.com/marek177/Nitemare3d-reversed/blob/f5c37abbbdc3ff8bd806af10fb1eb6dd01e9df68/README.md
- https://github.com/marek177/Nitemare3d-reversed/blob/f5c37abbbdc3ff8bd806af10fb1eb6dd01e9df68/src/game/LevelState.cpp

## virtua-tennis-dreamcast-analysis

Project ID: virtua-tennis-dreamcast-analysis · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "virtua-tennis-dreamcast-analysis",
  "last_activity": "2026-10-28",
  "last_checked": "2026-10-29",
  "status": "Dreamcast SH-4 decompilation now reports 99.5% of C-capable functions, 97.8% of eligible code bytes and 70.6% aggregate test coverage, with 18 of 3,299 C-capable functions and 17,086 eligible bytes left.",
  "techniques": [
    "directed function-equivalence testing",
    "holdout-tested function equivalence",
    "SH-4 call-argument recovery",
    "development/holdout function equivalence testing",
    "instruction-coverage accounting"
  ]
}
```

Expected existing project SHA256: 63d75990366be53b0f454c07ca7a4a4849e77c06d27be82d1d268f69a1b8a2b5

### Identity (reviewed)

Virtua Tennis Dreamcast decompilation with disc-derived executable reconstruction, symbol/asset maps, generated C and side-by-side Shuriken Explorer presentation.
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/blob/d82fc50aa7af487a308c5ceac87b4f7a2b01a14d/README.md
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/commit/5c3062a3ebc613061ea8e5a94ac01ec92fac299d

### Classification (reviewed)

Original-platform game decompilation. Byte-identical executable assembly fallback, C-capable function completion, eligible-byte completion and test coverage are separate measures and are not collapsed into one completeness claim.
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/blob/d82fc50aa7af487a308c5ceac87b4f7a2b01a14d/README.md
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/commit/5c3062a3ebc613061ea8e5a94ac01ec92fac299d

### Source CPU (reviewed)

The source executable remains Dreamcast SH-4 machine code.
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/blob/d82fc50aa7af487a308c5ceac87b4f7a2b01a14d/README.md
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/commit/5c3062a3ebc613061ea8e5a94ac01ec92fac299d

### Target CPU (reviewed)

The reconstruction targets SH-4 for the original Dreamcast executable; no modern host port output is established.
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/blob/d82fc50aa7af487a308c5ceac87b4f7a2b01a14d/README.md
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/commit/5c3062a3ebc613061ea8e5a94ac01ec92fac299d

### Build (reviewed)

The pinned progress commits report playerStartReactions, ADXF_AddPartition, latticeBind, FBCompQueue, entryCharaSelExec, rankNameEntryExec and entryPickRandomChara as proven and update the project to 99.5% of C-capable functions, 97.8% of eligible bytes and 70.6% aggregate test coverage. Limitations: These are upstream counters and per-function equivalence results. Some newly proven functions have explicitly thin instruction coverage, and the tracker did not run the suite or boot a reconstructed disc. Next check: Track the remaining 18 C-capable functions and require the project to keep function proof, eligible-byte completion and aggregate coverage separate.
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/commit/f701c9450c307dda7fc45205213440b3c0b61803
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/commit/832f5eddc4f7b6fe62bc354fff534528df5081d6

### Runtime profiles (no-evidence-found)

No minimum Dreamcast accessory/model profile or host runtime minimum is stated in the inspected decompilation documentation.
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/blob/d82fc50aa7af487a308c5ceac87b4f7a2b01a14d/README.md
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/commit/5c3062a3ebc613061ea8e5a94ac01ec92fac299d

### AI (reviewed)

The reviewed equivalence and reader commits explicitly credit Claude Opus 5.5 as co-author; attribution is limited to those evidenced changes.
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/commit/ffa09820ec2427a759d2bba61c6303152cc73880
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/commit/86aa92ad3d86b6b6187d630c71bb5c720075c89a

### Relationships (reviewed)

SDK-identical library functions are explicitly tracked separately from game-derived C recovery. The repository remains a title-specific project sharing tooling and the Shuriken Explorer presentation with related Dreamcast decomps.
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/blob/d82fc50aa7af487a308c5ceac87b4f7a2b01a14d/sdk-identical.txt
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/blob/d82fc50aa7af487a308c5ceac87b4f7a2b01a14d/README.md
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/commit/5c3062a3ebc613061ea8e5a94ac01ec92fac299d

## firestaff-dungeon-master-engine

Project ID: firestaff-dungeon-master-engine · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "firestaff-dungeon-master-engine",
  "last_activity": "2026-10-28",
  "last_checked": "2026-10-29",
  "status": "Authenticated Nexus evidence now carries a retained retail BKR through Continue into a four-champion dungeon view, while FM Towns DM2 traces cover startup source frames; Firestaff-side Continue loading, HUD/viewport and presentation parity remain unimplemented or unverified.",
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
    "launcher/runtime access-owner separation",
    "authenticated save-image replay",
    "VDP source-span verification",
    "startup source-frame tracing"
  ]
}
```

Expected existing project SHA256: d329b1070649e3053b0368b9c72157e09d12376015659fb630a3937832bb463f

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

A hash-retained Japanese retail BKR was replayed in Ymir 0.4.2-dev from cold boot through Continue to a four-champion dungeon view, and a paired Up-input replay changed the rendered view. Separate FM Towns DM2 work records every startup source frame used during Timer-A catch-up. Limitations: The Nexus replay verifies a retail reference flow in Ymir, not Firestaff's Continue implementation or input parity. The source-frame trace is diagnostic and does not establish native FM Towns presentation parity. Next check: Bind the cold-boot BKR scan/load path and compare Firestaff Continue, HUD, viewport and startup presentation against the authenticated references.
- https://github.com/yeager/firestaff/commit/07f371b437cc0e2ed02082beaec2598d58eab80e
- https://github.com/yeager/firestaff/commit/6bd8bddac9ed6c82befa3a3f2949ee5540816105

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

## openrac-rac1-decomp

Project ID: openrac-rac1-decomp · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "openrac-rac1-decomp",
  "last_activity": "2026-10-28",
  "last_checked": "2026-10-29",
  "status": "PAL 2.00 PS2 reconstruction now shares typed LevelState/camera, render, pause, particle, puzzle and memory-card structures across overlays; these structural refactors do not by themselves establish additional matching or playability.",
  "techniques": [
    "shared-structure recovery across overlays",
    "typed sound-slot and draw-queue recovery",
    "cross-overlay shared-structure recovery",
    "typed memory-card state recovery"
  ]
}
```

Expected existing project SHA256: 9cbcc3bf63f9eece7cb18aea1a6ced6824b2edffc74c227500d8de9983240813

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

Eleven reviewed refactors replace duplicate and raw-offset overlay structures with shared hero, LevelState, camera, render, pause, particle, Trespasser-puzzle and memory-card types while preserving the original-address reconstruction model. Limitations: The tracker did not compile with the period toolchains or independently compare the result; type consolidation is not a whole-project matching or playability claim. Next check: Follow matching reports and toolchain reproducibility evidence independently of structural typing progress.
- https://github.com/OpenRAC/rac1-decomp/commit/e02169335967d5e090eee47fd50ce3824c63e11a
- https://github.com/OpenRAC/rac1-decomp/commit/0f0bfcfe98553a7a0ea9a26db94ff00deecf8be5

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

## kharn27-esp32-locomotive-basic

Project ID: kharn27-esp32-locomotive-basic · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "kharn27-esp32-locomotive-basic",
  "last_activity": "2026-10-28",
  "last_checked": "2026-10-29",
  "status": "The reconstruction now records three passing Xtensa firmware profiles with exact size budgets and an original-ROM oracle with 14/14 scalar STRING cases observed twice; device execution and broad BASIC compatibility remain explicitly unverified.",
  "target_cpu": [
    "Xtensa"
  ],
  "techniques": [
    "three-profile Xtensa size and ABI verification",
    "independent original-ROM oracle capture"
  ]
}
```

Expected existing project SHA256: 3362b6130f22e5efa2f0b6213e1a8957ca601fb12d6e6fe3ef64f29a57b63e8b

### Identity (reviewed)

Locomotive BASIC — native C compatibility reconstruction. Repository identity, pinned tree and available implementation inspected.
- https://github.com/Kharn27/ESP32-Locomotive-Basic/blob/2ca96fde8e50251b4bcdfaf642e8052f3c828e5d/README.md
- https://github.com/Kharn27/ESP32-Locomotive-Basic/blob/2ca96fde8e50251b4bcdfaf642e8052f3c828e5d/core/basic_tokenizer.c
- https://github.com/Kharn27/ESP32-Locomotive-Basic/blob/2ca96fde8e50251b4bcdfaf642e8052f3c828e5d/docs/PROJECT_STATUS.md

### Classification (reviewed)

Reconstructs CPC 6128 BASIC 1.1 tokens, expression and execution semantics using original disassembly as behavioral reference. Inspected original-address-backed token catalogue and emitter.
- https://github.com/Kharn27/ESP32-Locomotive-Basic/blob/2ca96fde8e50251b4bcdfaf642e8052f3c828e5d/README.md
- https://github.com/Kharn27/ESP32-Locomotive-Basic/blob/2ca96fde8e50251b4bcdfaf642e8052f3c828e5d/core/basic_tokenizer.c
- https://github.com/Kharn27/ESP32-Locomotive-Basic/blob/2ca96fde8e50251b4bcdfaf642e8052f3c828e5d/docs/PROJECT_STATUS.md

### Source CPU (reviewed)

Documented original ISA: Z80.
- https://github.com/Kharn27/ESP32-Locomotive-Basic/blob/2ca96fde8e50251b4bcdfaf642e8052f3c828e5d/README.md
- https://github.com/Kharn27/ESP32-Locomotive-Basic/blob/2ca96fde8e50251b4bcdfaf642e8052f3c828e5d/core/basic_tokenizer.c
- https://github.com/Kharn27/ESP32-Locomotive-Basic/blob/2ca96fde8e50251b4bcdfaf642e8052f3c828e5d/docs/PROJECT_STATUS.md

### Target CPU (reviewed)

ESP-IDF 5.5.6 CI explicitly builds three Xtensa firmware profiles (CONSOLE, HW3 and BASIC_PROBE), establishing Xtensa as an output CPU architecture without implying a minimum CPU model.
- https://github.com/Kharn27/ESP32-Locomotive-Basic/commit/1e0459e1fb9e3f78d786f073ec7be6403dce0630

### Build (reviewed)

Upstream records ESP-IDF 5.5.6 Xtensa CI passing CONSOLE, HW3 and BASIC_PROBE profiles with exact Flash/IRAM/DRAM/image budgets, 16/16 ABI fields and 83/83 CTest results per C99 matrix cell. A separate original-ROM acquisition records two exact RAM/printer observations for each of 14 scalar STRING cases. Limitations: The size and ABI readings are build/ELF evidence, not hardware measurements. The report remains ON_DEVICE_UNVERIFIED, and the pre-B C99 implementation still classifies all 14 STRING cases as unsupported. Next check: Repeat the final-head CI and perform the explicitly requested flash/monitor hardware run before recording any runnable-device profile.
- https://github.com/Kharn27/ESP32-Locomotive-Basic/commit/1e0459e1fb9e3f78d786f073ec7be6403dce0630
- https://github.com/Kharn27/ESP32-Locomotive-Basic/commit/6723ff0d51f23ada0a6913c6006db68ea51595eb

### Runtime profiles (no-evidence-found)

No independent hardware compatibility or minimum memory/CPU testing; dependencies and limits are recorded in build notes.
- https://github.com/Kharn27/ESP32-Locomotive-Basic/blob/2ca96fde8e50251b4bcdfaf642e8052f3c828e5d/README.md
- https://github.com/Kharn27/ESP32-Locomotive-Basic/blob/2ca96fde8e50251b4bcdfaf642e8052f3c828e5d/core/basic_tokenizer.c
- https://github.com/Kharn27/ESP32-Locomotive-Basic/blob/2ca96fde8e50251b4bcdfaf642e8052f3c828e5d/docs/PROJECT_STATUS.md

### AI (reviewed)

README explicitly assigns design/review and implementation roles to ChatGPT assistants.
- https://github.com/Kharn27/ESP32-Locomotive-Basic/blob/2ca96fde8e50251b4bcdfaf642e8052f3c828e5d/README.md
- https://github.com/Kharn27/ESP32-Locomotive-Basic/blob/2ca96fde8e50251b4bcdfaf642e8052f3c828e5d/core/basic_tokenizer.c
- https://github.com/Kharn27/ESP32-Locomotive-Basic/blob/2ca96fde8e50251b4bcdfaf642e8052f3c828e5d/docs/PROJECT_STATUS.md

### Relationships (reviewed)

The native C runtime does not embed or execute the CPC ROM. The newly pinned original-ROM runs are an external behavior oracle, kept distinct from internal tests and target firmware execution.
- https://github.com/Kharn27/ESP32-Locomotive-Basic/commit/6723ff0d51f23ada0a6913c6006db68ea51595eb

## zapple-ii-bpm-prodos-softcard-environment

Project ID: zapple-ii-bpm-prodos-softcard-environment · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "zapple-ii-bpm-prodos-softcard-environment",
  "last_activity": "2026-10-28",
  "last_checked": "2026-10-29",
  "status": "The Apple IIe/SoftCard environment now exposes kernel-managed W5100 socket and packetless TX/RX APIs, migrates Telnet to the kernel interface and adds a first working WGET client; network execution was not independently repeated.",
  "techniques": [
    "terminal personality caching",
    "CP/M file-semantics regression",
    "virtualized directory search",
    "bank-safe W5100 socket API integration",
    "CP/M Telnet and WGET client integration"
  ]
}
```

Expected existing project SHA256: cbad82e15563de3bdcd277edb4f17878cdbe4f8c3180bf4e3b7ccf5897e5c2ef

### Identity (reviewed)

Native dual-CPU CP/M-compatible CCP/BDOS/BIOS environment translating Z80 program file operations into Apple II ProDOS services.
- https://github.com/bobbimanners/Zapple-II/blob/770b60f998a9f28ebd7e5ea6a99dc7d2b6e7ac03/README.md
- https://github.com/bobbimanners/Zapple-II/blob/770b60f998a9f28ebd7e5ea6a99dc7d2b6e7ac03/softcard65.asm
- https://github.com/bobbimanners/Zapple-II/commit/4f5f5c6ac0768c8e205be90740684679030e2345

### Classification (reviewed)

Substantial 6502 loader/terminal/ProDOS backend and Z80 BDOS/BIOS/CCP code with bank gateway and FCB/DMA transfers. Real SoftCard Z80 executes applications; this is not a CPU emulator. Newly updated default branch inspected at pinned commit. BSD-2-Clause for project code. Bundled assemblers have separate notices; CP/M programs including WordStar/Turbo Pascal/dBase are third-party content and not automatically relicensed by root BSD grant.
- https://github.com/bobbimanners/Zapple-II/blob/770b60f998a9f28ebd7e5ea6a99dc7d2b6e7ac03/README.md
- https://github.com/bobbimanners/Zapple-II/blob/770b60f998a9f28ebd7e5ea6a99dc7d2b6e7ac03/softcard65.asm
- https://github.com/bobbimanners/Zapple-II/commit/4f5f5c6ac0768c8e205be90740684679030e2345

### Source CPU (reviewed)

Original/inspected source architecture is 6502, Z80. This is not an inferred minimum runnable machine.
- https://github.com/bobbimanners/Zapple-II/blob/770b60f998a9f28ebd7e5ea6a99dc7d2b6e7ac03/README.md
- https://github.com/bobbimanners/Zapple-II/blob/770b60f998a9f28ebd7e5ea6a99dc7d2b6e7ac03/softcard65.asm
- https://github.com/bobbimanners/Zapple-II/commit/4f5f5c6ac0768c8e205be90740684679030e2345

### Target CPU (reviewed)

Inspected implementation/build establishes 6502, Z80 output architecture; a complete minimum runtime configuration was not independently verified.
- https://github.com/bobbimanners/Zapple-II/blob/770b60f998a9f28ebd7e5ea6a99dc7d2b6e7ac03/README.md
- https://github.com/bobbimanners/Zapple-II/blob/770b60f998a9f28ebd7e5ea6a99dc7d2b6e7ac03/softcard65.asm
- https://github.com/bobbimanners/Zapple-II/commit/4f5f5c6ac0768c8e205be90740684679030e2345

### Build (reviewed)

The reviewed changes add ownership-checked BDOS socket management and a bounded 16-byte packetless W5100 TX/RX path, migrate Telnet to dynamic kernel sockets, and introduce the upstream-described first working WGET.COM. Limitations: The tracker reviewed source changes only; it did not assemble the image, exercise W5100 hardware or verify Telnet/WGET interoperability. Next check: Retain kernel/socket ownership boundaries and seek reproducible Apple IIe/SoftCard network execution evidence.
- https://github.com/bobbimanners/Zapple-II/commit/65b215c64ed9b74b7b81596f7fa61c883ef91666
- https://github.com/bobbimanners/Zapple-II/commit/4398794c9a3e36383e2559ff39414e1d2e8cfb03

### Runtime profiles (no-evidence-found)

The reviewed terminal and CP/M changes do not state a minimum Apple IIe revision, RAM, SoftCard model, ROM or display requirement. No minimum is inferred from the 6502/Z80 code.
- https://github.com/bobbimanners/Zapple-II/commit/4f5f5c6ac0768c8e205be90740684679030e2345

### AI (no-evidence-found)

Unknown: bounded primary documentation, sampled implementation/build/licence files and up to three latest full commit messages contain no explicit AI-contribution attribution. Absence is not evidence of non-use.
- https://github.com/bobbimanners/Zapple-II/blob/770b60f998a9f28ebd7e5ea6a99dc7d2b6e7ac03/README.md
- https://github.com/bobbimanners/Zapple-II/blob/770b60f998a9f28ebd7e5ea6a99dc7d2b6e7ac03/softcard65.asm
- https://github.com/bobbimanners/Zapple-II/commit/4f5f5c6ac0768c8e205be90740684679030e2345

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/bobbimanners/Zapple-II/blob/770b60f998a9f28ebd7e5ea6a99dc7d2b6e7ac03/README.md
- https://github.com/bobbimanners/Zapple-II/blob/770b60f998a9f28ebd7e5ea6a99dc7d2b6e7ac03/softcard65.asm
- https://github.com/bobbimanners/Zapple-II/commit/4f5f5c6ac0768c8e205be90740684679030e2345

## ambermoon

Project ID: ambermoon · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "ambermoon",
  "last_activity": "2026-10-28",
  "last_checked": "2026-10-29",
  "runtime_profiles": [
    {
      "cpu_family": "m68k",
      "evidence": [
        "https://github.com/Pyrdacor/Ambermoon/commit/9eae91ea17f4e5a0fa4b78f5921c2dee8aac5b05"
      ],
      "min_ram_kib": 2048,
      "name": "Atari ST port",
      "notes": "Primary port documentation states that Hatari configured as an STE works, a plain ST also works, and at least 2 MB RAM is required. This is an upstream documented minimum, not tracker-side physical-hardware validation.",
      "platform": "Atari ST"
    }
  ],
  "status": "The Atari ST port now carries its unpacked original player/song data in-tree, no longer needs ORIGINAL at build time, and has accepted conversions for the documented Amiga song set through song 32; tracker-side build and listening tests were not performed.",
  "target_cpu": [
    "m68k"
  ],
  "techniques": [
    "binary analysis",
    "format decoding",
    "source restoration",
    "recovered-source build",
    "native asset painting and palette editing",
    "Pack-Ice music extraction",
    "Amiga-to-Atari-ST music conversion",
    "song-specific conversion overrides"
  ]
}
```

Expected existing project SHA256: fbc993f9f2db9f7cc3246cc19521e5cdd4c270a3eaab39c43a4a5588afb4e004

### Identity (reviewed)

Seeded from curated upstream_name/display_title/subjects.
- https://github.com/Pyrdacor/Ambermoon/blob/master/README.md

### Classification (reviewed)

Seeded from record_class and structured kind fields.
- https://github.com/Pyrdacor/Ambermoon/blob/master/README.md

### Source CPU (reviewed)

The v1.21 changelog explicitly identifies a plain-68000 decompression fault and source-built Amiga program, reinforcing the existing m68000 source-architecture record without asserting a RAM minimum.
- https://github.com/Pyrdacor/Ambermoon/commit/faca6448dea37b24d59a161d4680583822812d7b

### Target CPU (reviewed)

The Atari ST port documentation explicitly identifies its retained player as 68000 code and builds a runnable ST output, establishing an m68k output architecture without broadening compatibility beyond the documented port.
- https://github.com/Pyrdacor/Ambermoon/commit/9eae91ea17f4e5a0fa4b78f5921c2dee8aac5b05

### Build (reviewed)

The port stores the unchanged 8,314-byte ST player and split song data in port/MUSIC, removes the build-time ORIGINAL dependency, and records accepted conversions across the subsequently reviewed song commits through Game Over (song 32). Limitations: Acceptance is upstream listening/conversion evidence. The tracker did not rebuild the port, compare generated player bytes or audit audible parity for each song. Next check: Follow reproducible port builds and retain per-song acceptance separately from complete music or game parity.
- https://github.com/Pyrdacor/Ambermoon/commit/9eae91ea17f4e5a0fa4b78f5921c2dee8aac5b05
- https://github.com/Pyrdacor/Ambermoon/commit/620c782ee1c8bc89621f9bdbe03a8e9a6c856d9e

### Runtime profiles (reviewed)

The Atari ST port documentation explicitly states that an STE or plain ST works with at least 2 MB RAM; no narrower CPU model, ROM revision or physical-hardware test is inferred.
- https://github.com/Pyrdacor/Ambermoon/commit/9eae91ea17f4e5a0fa4b78f5921c2dee8aac5b05

### AI (reviewed)

The v1.21 changelog/source-build commit has an explicit Claude Opus 5.5 co-author trailer; AI usage is affirmative but its extent is not inferred.
- https://github.com/Pyrdacor/Ambermoon/commit/faca6448dea37b24d59a161d4680583822812d7b

### Relationships (reviewed)

AmbermoonImageEditor was reviewed as a separately titled repository component, but it is documented, built and versioned inside the Ambermoon Tools suite rather than released as an independent project. Existing separate records for Ambermoon source restoration and Ambermoon.net remain distinct.
- https://github.com/Pyrdacor/Ambermoon/commit/ebaf2d63b05ee718b97a61f531a2c6c00857b399
- https://github.com/Pyrdacor/Ambermoon/blob/master/Tools/README.md

## amberstar-amber-framework

Project ID: amberstar-amber-framework · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "amberstar-amber-framework",
  "last_activity": "2026-10-28",
  "last_checked": "2026-10-29",
  "status": "Amberstar framework now loads English Amiga data, reproduces Amiga outro pictures/copper gradients and handles Amiga COSO/TFMX music and samples, including the seven-voice outro path; complete-game parity is not claimed.",
  "techniques": [
    "direct gameplay implementation",
    "scenario-driven battle regression",
    "Amiga copper-gradient reconstruction",
    "COSO and TFMX module playback",
    "legacy outro data decoding"
  ]
}
```

Expected existing project SHA256: 82d31b3b10a92e7d51260ef2d2b9e0a128d74192d84da4362bd61547ffdb3c0a

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

The reviewed series adds English Amiga data, original-style map-song selection, sampled Amiga music, EXTRO.UDO pictures with 15-step copper-gradient fades, and COSO/TFMX playback including the seven-voice Amiga outro. Limitations: The tracker did not run the game or compare audio/video output to original Amiga hardware; these bounded data, outro and player paths do not establish complete-game parity. Next check: Track scenario tests and original-output comparisons for the expanded Amiga-specific paths.
- https://github.com/Pyrdacor/Amber/commit/79fc7499ac2df1f6152c995f1484057846edf939
- https://github.com/Pyrdacor/Amber/commit/15b236abf172a4beb9acda6fb087fdf05c51a4f4
- https://github.com/Pyrdacor/Amber/commit/cc7aaa9d93cca43793d72b05f6053e0576ba008f

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

## simcity-spectrum-z80-suborb

Project ID: simcity-spectrum-z80-suborb · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "simcity-spectrum-z80-suborb",
  "last_activity": "2026-10-28",
  "last_checked": "2026-10-29",
  "status": "The shared Z80 reconstruction adds scenario disasters, square minimaps for PC-88 and Multi 8, and Aquarius+ 4bpp minimap plus text-layer menus, dialogs, budget and evaluation screens; Aquarius+ display details remain hardware-unverified.",
  "techniques": [
    "shared simulation with platform-specific display, input, sound and file layers",
    "multi-target distribution packaging",
    "shared multi-platform Z80 UI adaptation",
    "Aquarius+ bitmap/text-layer integration",
    "scenario disaster reconstruction"
  ]
}
```

Expected existing project SHA256: 2c73dde8bbcf53cf5e8147ba5dd31ce6c9f55aa5407cdb2eb4dd34032c935eea

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

The reviewed commits implement scenario-triggered animated disasters, share square minimaps across PC-88 and Multi 8, and move Aquarius+ menus, dialogs, budget, evaluation and title screens to its text layer over the bitmap display. Limitations: The Aquarius+ commit explicitly leaves text transparency, popup colour and border remapping unverified on hardware. The tracker did not build or run any target. Next check: Seek hardware evidence for the Aquarius+ layer composition while keeping platform-specific UI verification separate.
- https://github.com/suborb/simcity_z80/commit/97f40874c6562127070f51a221ce85f34d835c51
- https://github.com/suborb/simcity_z80/commit/db283d373fc1b10ed7aa0a4bc97c21d8b78ae959
- https://github.com/suborb/simcity_z80/commit/904f6309b70d00024c1a159ee6afd23a951f949b

### Runtime profiles (no-evidence-found)

Per-platform documentation records media, display, audio and file-system behavior, but the reviewed change does not state verified minimum CPU, RAM, ROM or machine revisions. No runtime minimum is inferred.
- https://github.com/suborb/simcity_z80/commit/3409dc87b3a117a79378c93c2388ff6c3be27d25

### AI (no-evidence-found)

No explicit development-AI disclosure was found in the reviewed commit and distribution documentation; non-use is not established.
- https://github.com/suborb/simcity_z80/commit/3409dc87b3a117a79378c93c2388ff6c3be27d25

### Relationships (reviewed)

The five new output packages share the same repository, retained simulation and disassembly lineage. They remain one catalogue project rather than five inflated records.
- https://github.com/suborb/simcity_z80/commit/3409dc87b3a117a79378c93c2388ff6c3be27d25

## aminetxduo-classic-amiga-ip-stack

Project ID: aminetxduo-classic-amiga-ip-stack · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "aminetxduo-classic-amiga-ip-stack",
  "last_activity": "2026-10-28",
  "last_checked": "2026-10-29",
  "status": "AmiNetXDuo now pins reviewed NetX Duo TCP corrections for FIN acknowledgement, recovery boundaries/timers and DATA/FIN SACK recovery; the existing physical A3000/A2065 profile remains the only measured tracker runtime profile.",
  "techniques": [
    "pinned upstream TCP recovery integration",
    "SACK DATA/FIN recovery"
  ]
}
```

Expected existing project SHA256: be9449af9c10534beed9cf91f02e1343fbb1b3e983eeec0a5b6479626e408834

### Identity (reviewed)

Independent bsdsocket.library implementation for classic AmigaOS backed by hosted ThreadX/NetX Duo, SANA-II network drivers and command-line networking clients.
- https://github.com/tinic/AmiNetXDuo/blob/511dc69ecf77cac9379ed6fd730b7aa439b87dd6/README.md
- https://github.com/tinic/AmiNetXDuo/blob/511dc69ecf77cac9379ed6fd730b7aa439b87dd6/docs/DEVELOPMENT.md

### Classification (reviewed)

Substantial native socket lifecycle/descriptor handling and cooperative Exec/ThreadX integration; code-level original ABI implementation rather than redistributed Roadshow/AmiTCP code. Current1.0.0-rc1; Pi Wi-Fi driver experimental and hardware coverage varies. MIT main stack and ThreadX/NetX; exceptions include BSD-2 NE2000 code, Dropbear MIT-style, separate Commodore/Sylvan Installer notices, MPL2 CA roots/WiFiPi and BSD WirelessManager. README licence table pins their scopes.
- https://github.com/tinic/AmiNetXDuo/blob/511dc69ecf77cac9379ed6fd730b7aa439b87dd6/README.md
- https://github.com/tinic/AmiNetXDuo/blob/511dc69ecf77cac9379ed6fd730b7aa439b87dd6/docs/DEVELOPMENT.md

### Source CPU (not-applicable)

No predecessor machine-code input or processor-specific source architecture is established; no CPU is inferred from the host language.
- https://github.com/tinic/AmiNetXDuo/blob/511dc69ecf77cac9379ed6fd730b7aa439b87dd6/README.md
- https://github.com/tinic/AmiNetXDuo/blob/511dc69ecf77cac9379ed6fd730b7aa439b87dd6/docs/DEVELOPMENT.md

### Target CPU (reviewed)

Documented output/support targets: Amiga. Processor scope: m68k.
- https://github.com/tinic/AmiNetXDuo/blob/511dc69ecf77cac9379ed6fd730b7aa439b87dd6/README.md
- https://github.com/tinic/AmiNetXDuo/blob/511dc69ecf77cac9379ed6fd730b7aa439b87dd6/docs/DEVELOPMENT.md

### Build (reviewed)

The project advances its pinned NetX Duo dependency through reviewed FIN acknowledgement, retransmission-boundary/timer and DATA/FIN SACK recovery corrections. Limitations: The reviewed top-level commits pin dependency revisions; the tracker did not run TCP fault-injection tests or repeat the physical Amiga network test. Next check: Retain the physical A3000/A2065 profile and seek end-to-end recovery evidence before broadening runtime or interoperability claims.
- https://github.com/tinic/AmiNetXDuo/commit/2c24ac1f4950fed9c9c5c1ff19f399f8abede33b
- https://github.com/tinic/AmiNetXDuo/commit/73055cf88246d8d97e54d7269f48e89cf705849e
- https://github.com/tinic/AmiNetXDuo/commit/d3734d57e5a0198b6294682f82a1d3c8adb7c651

### Runtime profiles (reviewed)

A physical Amiga 3000 with an Ameristar A2065 is now an upstream-tested configuration. No CPU generation or RAM floor is inferred from the machine model.
- https://github.com/tinic/AmiNetXDuo/commit/fce3575311d97f0bb13414cef3b97bbd026c6640

### AI (reviewed)

Pinned HEAD commit explicitly carries Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>; Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>; Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>; Co-authored-by: Claude Opus 5.5 <noreply@anthropic.com>. This supports AI-assisted contribution to that commit; extent across the complete implementation is not established.
- https://github.com/tinic/AmiNetXDuo/blob/511dc69ecf77cac9379ed6fd730b7aa439b87dd6/README.md
- https://github.com/tinic/AmiNetXDuo/blob/511dc69ecf77cac9379ed6fd730b7aa439b87dd6/docs/DEVELOPMENT.md

### Relationships (reviewed)

Original published-ABI implementation atop maintained ThreadX/NetX Duo forks; not a fork of proprietary Roadshow, Miami or AmiTCP.
- https://github.com/tinic/AmiNetXDuo/blob/511dc69ecf77cac9379ed6fd730b7aa439b87dd6/README.md
- https://github.com/tinic/AmiNetXDuo/blob/511dc69ecf77cac9379ed6fd730b7aa439b87dd6/docs/DEVELOPMENT.md

## Source updates

```json
[
  {
    "id": "github-marek177-nitemare3d-reversed",
    "last_reviewed": "2026-10-29",
    "reason": "Reviewed the new save-layout, blitter-contract and viewport-provenance evidence across the six DOS images; retained the explicit reachability and whole-game limits.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "pass23-virtua-tennis-dreamcast-analysis",
    "last_reviewed": "2026-10-29",
    "reason": "Reviewed the two progress commits and their updated README counters, per-function development/holdout evidence and explicitly thin coverage limits.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-yeager-firestaff",
    "last_reviewed": "2026-10-29",
    "reason": "Reviewed the authentic Nexus BKR Continue replay and FM Towns startup trace work; preserved the distinction between retail-reference capture and Firestaff implementation.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-openrac-rac1-decomp",
    "last_reviewed": "2026-10-29",
    "reason": "Reviewed the shared LevelState, render, pause, particle, puzzle and memory-card typing refactors; no separate nested project appeared.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-kharn27-esp32-locomotive-basic",
    "last_reviewed": "2026-10-29",
    "reason": "Reviewed the exact three-profile Xtensa build evidence and the independent original-CPC scalar STRING oracle package; no second project root appeared.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "wide-20261018h-zapple-ii-bpm-prodos-softcard-environment",
    "last_reviewed": "2026-10-29",
    "reason": "Reviewed the kernel socket-manager, packetless W5100 TX/RX, Telnet and first WGET integration; no separate utility project was promoted.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-pyrdacor",
    "last_reviewed": "2026-10-29",
    "reason": "Reviewed the Atari ST music extraction and Amiga-to-ST conversion series; the port remains part of Ambermoon rather than a newly titled project.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-pyrdacor-amber",
    "last_reviewed": "2026-10-29",
    "reason": "Reviewed the English Amiga data, map-music, sample, outro graphics and COSO/TFMX playback additions; all remain within the existing Amber framework project.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "intake-fourteenth-search-zx-disassembly",
    "last_reviewed": "2026-10-29",
    "reason": "Reviewed the disaster, multi-platform minimap and Aquarius+ text-layer work; the ports remain one shared reconstruction project.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "wide-20261018i-aminetxduo-classic-amiga-ip-stack",
    "last_reviewed": "2026-10-29",
    "reason": "Reviewed the pinned NetX Duo FIN, recovery-boundary and DATA/FIN SACK updates; the vendor submodule remains part of AmiNetXDuo.",
    "review_state": "substantially-reviewed"
  }
]
```

## Research event notes

The CPU audit queue contained zero unresolved source/target CPU areas. This pass nevertheless captured newly explicit Xtensa output evidence for ESP32 Locomotive BASIC and the Atari ST port's documented 2 MB runtime floor; it did not infer a minimum from a platform or language. Primary commits were reviewed, and no upstream project was compiled or executed by the tracker.
