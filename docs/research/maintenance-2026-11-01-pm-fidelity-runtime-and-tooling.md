# Fidelity, runtime and retro-tooling maintenance

Review eight material upstream changes across reconstruction, emulation, ports and preservation tooling

Date: 2026-11-01 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- alien-breed-3d-source-derived-pc-port / Build (reviewed): The tracker did not run the suite. Source animation attachment mapping, portal openings, geometry authoring and playable new-room validation remain open.
- alien-breed-3d-source-derived-pc-port / Runtime profiles (needs-research): The compiler changes state no minimum host CPU, RAM, GPU or OS version for desktop or web builds. Next check: Check primary build documentation and qualified releases for concrete minimum desktop/web requirements before adding a runtime profile.
- alien-breed-3d-source-derived-pc-port / AI (no-evidence-found): The reviewed commits contain no explicit development-AI attribution; absence in this bounded evidence is not proof of non-use.
- wing-commander-kilrathi-saga-reconstruction / Target CPU (no-evidence-found): Native and SDL builds are reported, but the reviewed commits do not establish one fixed output CPU or minimum host ISA.
- wing-commander-kilrathi-saga-reconstruction / Build (needs-research): The tracker did not compile or byte-compare the executable. Remaining ordered cleanup and declaration/qualifier blockers are not closed by these commits. Next check: Continue source-faithful cleanup while retaining mandatory whole-executable hashing and operand checks for every accepted change.
- wing-commander-kilrathi-saga-reconstruction / Runtime profiles (no-evidence-found): The reviewed commits provide no minimum CPU, RAM, Windows version or SDL host requirement, so no runtime profile is added.
- moria8-6502-multiplatform / Source CPU (no-evidence-found): Moria8 is a new implementation rather than a reconstruction of one original executable ISA, so no source CPU is inferred from its target platforms.
- moria8-6502-multiplatform / Build (reviewed): The tracker did not assemble or execute the ports or reproduce the drive IRQ/status scenarios.
- kharn27-esp32-locomotive-basic / Build (reviewed): CPC ESC oracle behavior, device BREAK handling and the native hardware lane remain explicitly unverified or blocked.
- kharn27-esp32-locomotive-basic / Runtime profiles (no-evidence-found): Do not promote a runnable ESP32 profile from host-only C99 tests. Next check: Repeat final-head CI and perform the requested flash/monitor hardware run before recording a runnable-device profile.
- amy-studio-colecovision-development-environment / Build (reviewed): The tracker did not run the browser environment, compiler, ROMs or ColecoVision emulator.
- amy-studio-colecovision-development-environment / Runtime profiles (no-evidence-found): The reviewed commits state no minimum browser, host CPU, RAM or ColecoVision hardware profile, so none is added.
- pcsx-redux-debugging-environment / Target CPU (no-evidence-found): The portable host build has no fixed output CPU established by this commit, so none is inferred.
- pcsx-redux-debugging-environment / Build (reviewed): The tracker did not build PCSX-Redux, run the new test or compare behavior on physical PlayStation hardware.
- pcsx-redux-debugging-environment / Runtime profiles (no-evidence-found): The GPU fix states no minimum host CPU, RAM, GPU or OS requirement.
- pcsx-redux-debugging-environment / AI (no-evidence-found): The reviewed commit contains no explicit development-AI attribution; absence does not establish non-use.
- puzzle-pits-source-modernization / Build (reviewed): The tracker did not run mkpit, round-trip a level or launch its output in any game port.
- puzzle-pits-source-modernization / Runtime profiles (no-evidence-found): The tool commit specifies Node invocation but no minimum host CPU, RAM, Node version or operating system.
- artemiourbina-mdfourier / Target CPU (no-evidence-found): No fixed host output ISA or minimum CPU is established by the C signal-processing change.
- artemiourbina-mdfourier / Build (reviewed): The tracker did not compile MDFourier, rerun captures or quantify numerical differences beyond the upstream description.
- artemiourbina-mdfourier / Runtime profiles (no-evidence-found): The reviewed source and documentation change states no minimum CPU, RAM, audio interface or operating-system requirement.
- artemiourbina-mdfourier / AI (no-evidence-found): The reviewed commit contains no explicit development-AI attribution; absence does not establish non-use.

## alien-breed-3d-source-derived-pc-port

Project ID: alien-breed-3d-source-derived-pc-port · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "alien-breed-3d-source-derived-pc-port",
  "last_checked": "2026-11-01",
  "status": "Amiga-source-derived SDL2 PC/web port; its editor now assembles complete original-map room graphics streams and preserves packed point-lighting animation controls, while new-geometry authoring and playable newly drawn rooms remain unproven.",
  "techniques": [
    "assembly-to-C translation",
    "Amiga asset format reuse",
    "SDL2 rendering",
    "source-derived combat-behavior restoration",
    "transactional editable-source history",
    "portal-topology compilation",
    "original-contract collision reconstruction",
    "complete room-graphics stream assembly",
    "packed point-lighting reconstruction"
  ]
}
```

Expected existing project SHA256: 90a384648fc334a2bdf109e47b4a0c467430b6d1219a781f0e416ae656cf7bea

### Identity (reviewed)

Alien Breed 3D remains the same Amiga-source-derived PC/web port and integrated editor; the new compiler stages are not separate projects.
- https://github.com/retro-foundry/Alien-Breed-HD/commit/1b3c7f240a675535ee95e16907de8517a658e904
- https://github.com/retro-foundry/Alien-Breed-HD/commit/8e869445a4c1628b0d79cedefc372ccdcb275b34

### Classification (reviewed)

This remains source-derived port and editor work grounded in released Amiga source contracts, not a decompilation or emulator-hosted original binary.
- https://github.com/retro-foundry/Alien-Breed-HD/commit/1b3c7f240a675535ee95e16907de8517a658e904
- https://github.com/retro-foundry/Alien-Breed-HD/commit/8e869445a4c1628b0d79cedefc372ccdcb275b34

### Source CPU (reviewed)

The preserved original Amiga source remains Motorola 68000 assembly; TypeScript compiler code does not change that source architecture.
- https://github.com/retro-foundry/Alien-Breed-HD/commit/1b3c7f240a675535ee95e16907de8517a658e904

### Target CPU (not-applicable)

No fixed output CPU is established for the portable desktop/web builds or editor, so no host architecture is inferred.
- https://github.com/retro-foundry/Alien-Breed-HD/commit/8e869445a4c1628b0d79cedefc372ccdcb275b34

### Build (reviewed)

Upstream now assembles complete room graphics streams with explicit record identities and reconstructs packed point-lighting words without corrupting animation-control bytes; the suite reports 522 unit checks plus builds passing. Limitations: The tracker did not run the suite. Source animation attachment mapping, portal openings, geometry authoring and playable new-room validation remain open.
- https://github.com/retro-foundry/Alien-Breed-HD/commit/1b3c7f240a675535ee95e16907de8517a658e904
- https://github.com/retro-foundry/Alien-Breed-HD/commit/8e869445a4c1628b0d79cedefc372ccdcb275b34

### Runtime profiles (needs-research)

The compiler changes state no minimum host CPU, RAM, GPU or OS version for desktop or web builds. Next check: Check primary build documentation and qualified releases for concrete minimum desktop/web requirements before adding a runtime profile.
- https://github.com/retro-foundry/Alien-Breed-HD/commit/1b3c7f240a675535ee95e16907de8517a658e904

### AI (no-evidence-found)

The reviewed commits contain no explicit development-AI attribution; absence in this bounded evidence is not proof of non-use.
- https://github.com/retro-foundry/Alien-Breed-HD/commit/1b3c7f240a675535ee95e16907de8517a658e904
- https://github.com/retro-foundry/Alien-Breed-HD/commit/8e869445a4c1628b0d79cedefc372ccdcb275b34

### Relationships (reviewed)

Generated room streams and lighting remain editor outputs inside Alien Breed HD, not separately titled projects.
- https://github.com/retro-foundry/Alien-Breed-HD/commit/1b3c7f240a675535ee95e16907de8517a658e904
- https://github.com/retro-foundry/Alien-Breed-HD/commit/8e869445a4c1628b0d79cedefc372ccdcb275b34

## wing-commander-kilrathi-saga-reconstruction

Project ID: wing-commander-kilrathi-saga-reconstruction · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "wing-commander-kilrathi-saga-reconstruction",
  "last_checked": "2026-11-01",
  "status": "Kilrathi Saga reconstruction now models Win32 shell byte views separately from the game modules’ integer flags and names more globals from DOS source while retaining an upstream-reported exact 518,656-byte executable match.",
  "techniques": [
    "strict whole-file executable comparison",
    "per-function machine-code similarity auditing",
    "discarded-probe recording",
    "register-lifetime probe recording",
    "byte-for-byte function matching",
    "register-allocation matching",
    "whole-executable hash verification",
    "instruction-operand cross-checking",
    "compiler-input cleanup under exactness constraints",
    "source-declaration alias reconstruction",
    "DOS-source symbol recovery"
  ]
}
```

Expected existing project SHA256: de8268769a25b18c8f45f24cbe74b84240b9480712eff6da65431232654000e3

### Identity (reviewed)

This remains the Wing Commander Kilrathi Saga reconstruction and SDL2 port; shell/header restructuring stays within the same project.
- https://github.com/neuromancer/wc1-re/commit/0d41905313a38b3344c4d204c297563d1cc0f0d9
- https://github.com/neuromancer/wc1-re/commit/d5f115d5f4aec7f553c2e8987a371e44ecfb8823

### Classification (reviewed)

The changes are source-faithful reconstruction work that models original declarations and names recovered globals while preserving executable identity.
- https://github.com/neuromancer/wc1-re/commit/0d41905313a38b3344c4d204c297563d1cc0f0d9
- https://github.com/neuromancer/wc1-re/commit/d5f115d5f4aec7f553c2e8987a371e44ecfb8823

### Source CPU (reviewed)

The original reconstructed executable remains 32-bit x86; header aliasing and symbol naming add no new source CPU.
- https://github.com/neuromancer/wc1-re/commit/0d41905313a38b3344c4d204c297563d1cc0f0d9

### Target CPU (no-evidence-found)

Native and SDL builds are reported, but the reviewed commits do not establish one fixed output CPU or minimum host ISA.
- https://github.com/neuromancer/wc1-re/commit/0d41905313a38b3344c4d204c297563d1cc0f0d9

### Build (needs-research)

Upstream reports native and SDL builds, address audits, full verification, and all 518,656 executable bytes matching after separating shell byte aliases from game-module integer declarations. Limitations: The tracker did not compile or byte-compare the executable. Remaining ordered cleanup and declaration/qualifier blockers are not closed by these commits. Next check: Continue source-faithful cleanup while retaining mandatory whole-executable hashing and operand checks for every accepted change.
- https://github.com/neuromancer/wc1-re/commit/0d41905313a38b3344c4d204c297563d1cc0f0d9
- https://github.com/neuromancer/wc1-re/commit/d5f115d5f4aec7f553c2e8987a371e44ecfb8823

### Runtime profiles (no-evidence-found)

The reviewed commits provide no minimum CPU, RAM, Windows version or SDL host requirement, so no runtime profile is added.
- https://github.com/neuromancer/wc1-re/commit/0d41905313a38b3344c4d204c297563d1cc0f0d9

### AI (reviewed)

Both reviewed commits explicitly credit Claude Opus 5.5; attribution is limited to these changes.
- https://github.com/neuromancer/wc1-re/commit/0d41905313a38b3344c4d204c297563d1cc0f0d9
- https://github.com/neuromancer/wc1-re/commit/d5f115d5f4aec7f553c2e8987a371e44ecfb8823

### Relationships (reviewed)

The Win32 shell, game modules and SDL renderer remain build components of the same reconstruction rather than distinct tracker projects.
- https://github.com/neuromancer/wc1-re/commit/0d41905313a38b3344c4d204c297563d1cc0f0d9

## moria8-6502-multiplatform

Project ID: moria8-6502-multiplatform · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "moria8-6502-multiplatform",
  "last_checked": "2026-11-01",
  "status": "Moria8 now treats truncated Commodore drive-status reads as lost, retries only probes that can issue a fresh OPEN, and fails ambiguous save status rather than reporting success; upstream playtest-disk scenarios pass across C64, Plus/4 and C128.",
  "techniques": [
    "five-platform HAL boundary validation",
    "Commander X16 memory-contract testing",
    "x16emu runtime scenarios",
    "VICE binary-monitor AI playtesting",
    "isolated multi-platform emulator regression",
    "deterministic finding replay",
    "disk save/load scenario replay",
    "drive-status retry validation",
    "lost-status recovery",
    "fresh-OPEN probe retries"
  ]
}
```

Expected existing project SHA256: bbfe9309b8ac8f333b6dec205cd7dd86725e8949eca6a2aeacbc79fc3bcae529

### Identity (reviewed)

Moria8 remains one multi-platform 6502/65C02 roguelike reimplementation with platform-specific HAL and storage policies.
- https://github.com/dcgibbons/moria8/commit/7fb9dd9c90254c3e45d6c2b4ff3a2effd4605af6
- https://github.com/dcgibbons/moria8/commit/a56cde42dfc9e3d5110c72c04ec04a60ee402be2

### Classification (reviewed)

The changes harden original-hardware storage behavior and regression playtests; they do not convert Moria8 into a recovered original binary.
- https://github.com/dcgibbons/moria8/commit/7fb9dd9c90254c3e45d6c2b4ff3a2effd4605af6
- https://github.com/dcgibbons/moria8/commit/a56cde42dfc9e3d5110c72c04ec04a60ee402be2

### Source CPU (no-evidence-found)

Moria8 is a new implementation rather than a reconstruction of one original executable ISA, so no source CPU is inferred from its target platforms.
- https://github.com/dcgibbons/moria8/commit/7fb9dd9c90254c3e45d6c2b4ff3a2effd4605af6

### Target CPU (reviewed)

The existing 6502 and 65C02 output architectures remain explicit in platform sources; storage-policy fixes introduce no new target CPU.
- https://github.com/dcgibbons/moria8/commit/7fb9dd9c90254c3e45d6c2b4ff3a2effd4605af6

### Build (reviewed)

Upstream adds lost-status flags, fresh-OPEN retry rules and save-failure handling, then records playtest-disk results of C64 18/18, Plus/4 19/19 and C128 18/18. Limitations: The tracker did not assemble or execute the ports or reproduce the drive IRQ/status scenarios.
- https://github.com/dcgibbons/moria8/commit/7fb9dd9c90254c3e45d6c2b4ff3a2effd4605af6
- https://github.com/dcgibbons/moria8/commit/a56cde42dfc9e3d5110c72c04ec04a60ee402be2

### Runtime profiles (reviewed)

The existing documented Apple IIe 128K/extended-80-column profile remains; the Commodore storage fixes do not state new minimum CPU, RAM, ROM or drive requirements.
- https://github.com/dcgibbons/moria8/commit/7fb9dd9c90254c3e45d6c2b4ff3a2effd4605af6
- https://github.com/dcgibbons/moria8/commit/a56cde42dfc9e3d5110c72c04ec04a60ee402be2

### AI (reviewed)

Existing AI-assisted playtest design remains explicitly documented; these commits do not justify broader authorship claims beyond current evidence.
- https://github.com/dcgibbons/moria8/commit/a56cde42dfc9e3d5110c72c04ec04a60ee402be2

### Relationships (reviewed)

C64, Plus/4, C128 and Commander X16 paths remain platform ports in one Moria8 project rather than separate titled projects.
- https://github.com/dcgibbons/moria8/commit/7fb9dd9c90254c3e45d6c2b4ff3a2effd4605af6

## kharn27-esp32-locomotive-basic

Project ID: kharn27-esp32-locomotive-basic · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "kharn27-esp32-locomotive-basic",
  "last_checked": "2026-11-01",
  "status": "The reconstruction now has a host-verified bounded C99 ESC/ANSI transport contract with malformed-CSI quarantine; original CPC ESC behavior, BREAK on device and a native hardware run remain explicitly unverified.",
  "techniques": [
    "three-profile Xtensa size and ABI verification",
    "independent original-ROM oracle capture",
    "bounded ESC/CSI framing",
    "malformed-sequence quarantine"
  ]
}
```

Expected existing project SHA256: 79026a4511e3271283a972da936179d115c6f3b78abe7d444a6910c3ba140a3a

### Identity (reviewed)

This remains the native C compatibility reconstruction of Locomotive BASIC for ESP32-class targets.
- https://github.com/Kharn27/ESP32-Locomotive-Basic/commit/4ed2b38657ff27797f0309944e3b21cd7d0a4284
- https://github.com/Kharn27/ESP32-Locomotive-Basic/commit/48b06aac9e80b6e0ce2a50edcca12c30f277d5e7

### Classification (reviewed)

The transport contract reconstructs and tests host-side input framing while preserving explicit gaps against original CPC/device behavior.
- https://github.com/Kharn27/ESP32-Locomotive-Basic/commit/4ed2b38657ff27797f0309944e3b21cd7d0a4284

### Source CPU (reviewed)

The original Locomotive BASIC context remains Z80; the C99 transport harness does not alter that source architecture.
- https://github.com/Kharn27/ESP32-Locomotive-Basic/commit/4ed2b38657ff27797f0309944e3b21cd7d0a4284

### Target CPU (reviewed)

Existing primary build evidence establishes Xtensa firmware outputs; the host transport contract adds no second output CPU.
- https://github.com/Kharn27/ESP32-Locomotive-Basic/commit/4ed2b38657ff27797f0309944e3b21cd7d0a4284

### Build (reviewed)

Upstream marks the bounded C99 ESC/ANSI bench and negative regression host-verified, including quarantine of malformed CSI until an explicit final byte. Limitations: CPC ESC oracle behavior, device BREAK handling and the native hardware lane remain explicitly unverified or blocked.
- https://github.com/Kharn27/ESP32-Locomotive-Basic/commit/4ed2b38657ff27797f0309944e3b21cd7d0a4284
- https://github.com/Kharn27/ESP32-Locomotive-Basic/commit/48b06aac9e80b6e0ce2a50edcca12c30f277d5e7

### Runtime profiles (no-evidence-found)

The transport bench is host verification and supplies no completed flash/monitor hardware run or minimum device profile. Limitations: Do not promote a runnable ESP32 profile from host-only C99 tests. Next check: Repeat final-head CI and perform the requested flash/monitor hardware run before recording a runnable-device profile.
- https://github.com/Kharn27/ESP32-Locomotive-Basic/commit/4ed2b38657ff27797f0309944e3b21cd7d0a4284

### AI (reviewed)

Existing project evidence identifies ChatGPT involvement; the reviewed transport commits add no more specific contribution attribution.
- https://github.com/Kharn27/ESP32-Locomotive-Basic/commit/4ed2b38657ff27797f0309944e3b21cd7d0a4284

### Relationships (reviewed)

The C99 harness is a validation component inside the Locomotive BASIC reconstruction, not a separate emulator or port.
- https://github.com/Kharn27/ESP32-Locomotive-Basic/commit/4ed2b38657ff27797f0309944e3b21cd7d0a4284

## amy-studio-colecovision-development-environment

Project ID: amy-studio-colecovision-development-environment · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "amy-studio-colecovision-development-environment",
  "last_checked": "2026-11-01",
  "status": "Amy Studio adds Shaker and Star Strike as explicitly non-port ColecoVision adaptations built from 1986 Ahoy! article rules, plus compiler support for inline VoxPCM and variable shifts; they remain original adaptations inside the browser development environment.",
  "subjects": [
    "Goblin",
    "Speed Ski",
    "Paratrooper",
    "Things in the Dark",
    "Copy Cat",
    "A Day at the Races",
    "Slalom",
    "Mastermaze",
    "Boggler",
    "Closeout",
    "Fighter Aces",
    "TI Trapshoot",
    "TI-99 Match-Em",
    "Chutes",
    "Shaker",
    "Star Strike"
  ],
  "techniques": [
    "Amy-to-Z80 compilation",
    "in-browser assembly",
    "ROM generation",
    "source breakpoints",
    "instruction stepping",
    "CPU/VDP/RAM/VRAM inspection",
    "cycle profiling",
    "gasm80-compatible Z80 assembly",
    "ADAM EOS project support",
    "ADAM serial/debug input",
    "screen-mode dataflow analysis",
    "deterministic source-port runtime validation",
    "source-listing faithful adaptation",
    "manual-canon example manifests",
    "article-rules original adaptation",
    "inline VoxPCM compilation",
    "variable-shift compilation"
  ]
}
```

Expected existing project SHA256: 286036728c6f5f53b56b30f04abdfe2b7336c27611a7b4478e747d81ca3f24d6

### Identity (reviewed)

Amy Studio remains the browser ColecoVision development environment; Shaker and Star Strike are named example subjects inside the repository.
- https://github.com/amypurple/AmyStudio/commit/a3fea07cdbefe4ed4386777dd8ea3022b0de3d5d
- https://github.com/amypurple/AmyStudio/commit/d46ee553c8843d5a4cda455aa3ab5b7e698c17b1

### Classification (reviewed)

Both sources explicitly describe new ColecoVision games based on Ahoy! article rules and say they are not ports; original visuals, projection and implementation choices prevent mislabelling them as recovered or reverse-engineered originals.
- https://github.com/amypurple/AmyStudio/commit/a3fea07cdbefe4ed4386777dd8ea3022b0de3d5d
- https://github.com/amypurple/AmyStudio/commit/cf1ec80bdcd3bc5f9cf7fc4b382051661845c07a

### Source CPU (not-applicable)

Amy Studio and these examples are newly authored development work; no original binary CPU is assigned from the C64 article context.
- https://github.com/amypurple/AmyStudio/commit/a3fea07cdbefe4ed4386777dd8ea3022b0de3d5d

### Target CPU (reviewed)

Amy compiles its ColecoVision examples to Z80 output; Shaker, Star Strike and compiler features do not add another target architecture.
- https://github.com/amypurple/AmyStudio/commit/a3fea07cdbefe4ed4386777dd8ea3022b0de3d5d
- https://github.com/amypurple/AmyStudio/commit/d46ee553c8843d5a4cda455aa3ab5b7e698c17b1

### Build (reviewed)

Upstream adds and refines both games, then extends the compiler and tests for inline VoxPCM and variable shifts. Limitations: The tracker did not run the browser environment, compiler, ROMs or ColecoVision emulator.
- https://github.com/amypurple/AmyStudio/commit/a3fea07cdbefe4ed4386777dd8ea3022b0de3d5d
- https://github.com/amypurple/AmyStudio/commit/cf1ec80bdcd3bc5f9cf7fc4b382051661845c07a
- https://github.com/amypurple/AmyStudio/commit/d46ee553c8843d5a4cda455aa3ab5b7e698c17b1

### Runtime profiles (no-evidence-found)

The reviewed commits state no minimum browser, host CPU, RAM or ColecoVision hardware profile, so none is added.
- https://github.com/amypurple/AmyStudio/commit/a3fea07cdbefe4ed4386777dd8ea3022b0de3d5d
- https://github.com/amypurple/AmyStudio/commit/d46ee553c8843d5a4cda455aa3ab5b7e698c17b1

### AI (reviewed)

Shaker and Star Strike explicitly credit Claude/Anthropic in their source comments; the existing README also credits Claude and Codex development contributions.
- https://github.com/amypurple/AmyStudio/commit/a3fea07cdbefe4ed4386777dd8ea3022b0de3d5d
- https://github.com/amypurple/AmyStudio/commit/cf1ec80bdcd3bc5f9cf7fc4b382051661845c07a

### Relationships (reviewed)

Shaker and Star Strike remain example subjects within Amy Studio. Their Ahoy! inspirations are provenance, not separate imported source projects.
- https://github.com/amypurple/AmyStudio/commit/a3fea07cdbefe4ed4386777dd8ea3022b0de3d5d
- https://github.com/amypurple/AmyStudio/commit/cf1ec80bdcd3bc5f9cf7fc4b382051661845c07a

## pcsx-redux-debugging-environment

Project ID: pcsx-redux-debugging-environment · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "pcsx-redux-debugging-environment",
  "last_checked": "2026-11-01",
  "status": "PCSX-Redux now clears GPUSTAT bit 26 throughout incomplete multi-word GP0 commands and GP0(C0h) readout until the final word, matching an added silicon-focused regression test; independently unbuilt and unrun.",
  "techniques": [
    "physical console timing calibration",
    "cross-renderer GPU parity",
    "silicon register-state conformance"
  ]
}
```

Expected existing project SHA256: 77031d239f09d4c5b5cda71b0cd4c0b4140d8d87704a381fcfd94cff1718e64f

### Identity (reviewed)

PCSX-Redux remains the same PlayStation emulator and reverse-engineering environment.
- https://github.com/pcsx-redux/pcsx-redux/commit/b723f051beb95e5bf94db2db1352c30a93e172d0

### Classification (reviewed)

The change improves hardware-register emulation fidelity and debugging behavior rather than reconstructing a game.
- https://github.com/pcsx-redux/pcsx-redux/commit/b723f051beb95e5bf94db2db1352c30a93e172d0

### Source CPU (reviewed)

The analyzed/emulated PlayStation architecture remains MIPS; a GPU register-state fix does not add another source CPU.
- https://github.com/pcsx-redux/pcsx-redux/commit/b723f051beb95e5bf94db2db1352c30a93e172d0

### Target CPU (no-evidence-found)

The portable host build has no fixed output CPU established by this commit, so none is inferred.
- https://github.com/pcsx-redux/pcsx-redux/commit/b723f051beb95e5bf94db2db1352c30a93e172d0

### Build (reviewed)

Upstream models GPUSTAT bit 26 as clear from the first through penultimate word of incomplete GP0 commands and readout, with a test checking each word. Limitations: The tracker did not build PCSX-Redux, run the new test or compare behavior on physical PlayStation hardware.
- https://github.com/pcsx-redux/pcsx-redux/commit/b723f051beb95e5bf94db2db1352c30a93e172d0

### Runtime profiles (no-evidence-found)

The GPU fix states no minimum host CPU, RAM, GPU or OS requirement.
- https://github.com/pcsx-redux/pcsx-redux/commit/b723f051beb95e5bf94db2db1352c30a93e172d0

### AI (no-evidence-found)

The reviewed commit contains no explicit development-AI attribution; absence does not establish non-use.
- https://github.com/pcsx-redux/pcsx-redux/commit/b723f051beb95e5bf94db2db1352c30a93e172d0

### Relationships (reviewed)

The gpustat26 MIPS test remains a conformance fixture inside PCSX-Redux, not a separate project.
- https://github.com/pcsx-redux/pcsx-redux/commit/b723f051beb95e5bf94db2db1352c30a93e172d0

## puzzle-pits-source-modernization

Project ID: puzzle-pits-source-modernization · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "puzzle-pits-source-modernization",
  "last_checked": "2026-11-01",
  "status": "The preserved 1995 DOS source and modern ports now include mkpit, which compiles bounded text maps, legends and scripts into compatible PIT level files; playable-port status is unchanged.",
  "techniques": [
    "DOS compatibility-layer preservation",
    "cross-platform Zig/SDL2 porting",
    "differential gameplay-rule fuzzing",
    "byte-exact level-format round trips",
    "text-map-to-binary level compilation"
  ]
}
```

Expected existing project SHA256: abacd8f32f2ef4ae2a7664d150bc18eb7adc05f961c75dfa35806b98a19e3553

### Identity (reviewed)

The Puzzle Pits remains the preserved DOS source plus modern cross-platform ports and compatible editing tools.
- https://github.com/LaPingvino/The-Puzzle-Pits/commit/de2487de85017457e6c199f91c39c13fe576fe2e

### Classification (reviewed)

mkpit is preservation-oriented authoring tooling for the reconstructed PIT format, not a new game or reverse-engineered executable.
- https://github.com/LaPingvino/The-Puzzle-Pits/commit/de2487de85017457e6c199f91c39c13fe576fe2e

### Source CPU (reviewed)

The preserved DOS original remains x86; the Node-based authoring tool does not change source CPU provenance.
- https://github.com/LaPingvino/The-Puzzle-Pits/commit/de2487de85017457e6c199f91c39c13fe576fe2e

### Target CPU (reviewed)

Existing x86-64 output evidence for current native ports remains; the portable authoring script does not justify another target CPU.
- https://github.com/LaPingvino/The-Puzzle-Pits/commit/de2487de85017457e6c199f91c39c13fe576fe2e

### Build (reviewed)

mkpit accepts a bounded textual map, optional legend overrides and script text, requires exactly one player, and writes the established PIT binary through shared serializers. Limitations: The tracker did not run mkpit, round-trip a level or launch its output in any game port.
- https://github.com/LaPingvino/The-Puzzle-Pits/commit/de2487de85017457e6c199f91c39c13fe576fe2e

### Runtime profiles (no-evidence-found)

The tool commit specifies Node invocation but no minimum host CPU, RAM, Node version or operating system.
- https://github.com/LaPingvino/The-Puzzle-Pits/commit/de2487de85017457e6c199f91c39c13fe576fe2e

### AI (reviewed)

The mkpit commit explicitly credits Claude Opus 5.5 and links a Claude session; attribution is limited to this tool change.
- https://github.com/LaPingvino/The-Puzzle-Pits/commit/de2487de85017457e6c199f91c39c13fe576fe2e

### Relationships (reviewed)

mkpit is a repository tool supporting The Puzzle Pits level format, not a separate titled project.
- https://github.com/LaPingvino/The-Puzzle-Pits/commit/de2487de85017457e6c199f91c39c13fe576fe2e

## artemiourbina-mdfourier

Project ID: artemiourbina-mdfourier · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "artemiourbina-mdfourier",
  "last_checked": "2026-11-01",
  "status": "MDFourier now uses amplitude-spectrum scaling in sample units, reports amplitudes relative to the strongest tone, and derives the digital noise floor consistently in dBr; the tracker did not independently build or compare captures.",
  "techniques": [
    "frequency-domain console-audio comparison",
    "amplitude-spectrum normalization",
    "digital noise-floor calibration"
  ]
}
```

Expected existing project SHA256: 2a527177493ccc3e5f034eef2e5382f89133869c10af87b689460c41a13fcfeb

### Identity (reviewed)

MDFourier remains the cross-console audio comparison and analysis suite.
- https://github.com/ArtemioUrbina/MDFourier/commit/495d2372f84b596a3352ed78615bdf80f6e2eba1

### Classification (reviewed)

This is preservation and hardware-comparison tooling that analyzes captured signals; it is not a reconstructed game or emulator.
- https://github.com/ArtemioUrbina/MDFourier/commit/495d2372f84b596a3352ed78615bdf80f6e2eba1

### Source CPU (not-applicable)

The reviewed host-side signal-analysis change has no original binary/source CPU role to record.
- https://github.com/ArtemioUrbina/MDFourier/commit/495d2372f84b596a3352ed78615bdf80f6e2eba1

### Target CPU (no-evidence-found)

No fixed host output ISA or minimum CPU is established by the C signal-processing change.
- https://github.com/ArtemioUrbina/MDFourier/commit/495d2372f84b596a3352ed78615bdf80f6e2eba1

### Build (reviewed)

Upstream replaces the prior magnitude scale with 2|X|/S1 amplitude-spectrum scaling, retains relative dBr output, and recalculates the digital floor as a tone at the bit-depth floor. Limitations: The tracker did not compile MDFourier, rerun captures or quantify numerical differences beyond the upstream description.
- https://github.com/ArtemioUrbina/MDFourier/commit/495d2372f84b596a3352ed78615bdf80f6e2eba1

### Runtime profiles (no-evidence-found)

The reviewed source and documentation change states no minimum CPU, RAM, audio interface or operating-system requirement.
- https://github.com/ArtemioUrbina/MDFourier/commit/495d2372f84b596a3352ed78615bdf80f6e2eba1

### AI (no-evidence-found)

The reviewed commit contains no explicit development-AI attribution; absence does not establish non-use.
- https://github.com/ArtemioUrbina/MDFourier/commit/495d2372f84b596a3352ed78615bdf80f6e2eba1

### Relationships (reviewed)

The analysis executable, wave utilities and documentation remain components of one MDFourier suite.
- https://github.com/ArtemioUrbina/MDFourier/commit/495d2372f84b596a3352ed78615bdf80f6e2eba1

## Source updates

```json
[
  {
    "id": "github-retro-foundry-alien-breed-hd",
    "last_reviewed": "2026-11-01",
    "reason": "Reviewed complete room-stream and point-lighting compiler stages while retaining new-geometry/playability limits.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "wide-20261018b-wing-commander-kilrathi-saga-reconstruction",
    "last_reviewed": "2026-11-01",
    "reason": "Reviewed Win32 shell declaration aliasing and DOS-source symbol recovery under whole-executable exactness.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-dcgibbons-moria8",
    "last_reviewed": "2026-11-01",
    "reason": "Reviewed lost drive-status handling, fresh-OPEN retry rules and cross-Commodore playtest results.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-kharn27-esp32-locomotive-basic",
    "last_reviewed": "2026-11-01",
    "reason": "Reviewed the host-verified ESC/ANSI transport contract and explicit CPC/device verification gaps.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-amypurple-amystudio",
    "last_reviewed": "2026-11-01",
    "reason": "Reviewed Shaker and Star Strike provenance/classification plus compiler support for VoxPCM and variable shifts.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "pass34-pcsx-redux-debugging-environment",
    "last_reviewed": "2026-11-01",
    "reason": "Reviewed GP0 partial-command GPUSTAT bit-26 behavior and the word-by-word regression.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "pass24-puzzle-pits-source-modernization",
    "last_reviewed": "2026-11-01",
    "reason": "Reviewed mkpit text-map/script compilation into the preserved PIT format.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-artemiourbina-mdfourier",
    "last_reviewed": "2026-11-01",
    "reason": "Reviewed amplitude-spectrum scaling and digital noise-floor calibration changes.",
    "review_state": "substantially-reviewed"
  }
]
```

## Research event notes

The CPU audit queue contained zero unresolved source or target CPU areas, so no architecture value was invented for this pass. Eight materially changed projects were reviewed from primary commits after the previous maintenance receipt. Shaker and Star Strike are explicitly recorded as original ColecoVision adaptations based on article rules, not ports or reverse-engineered originals. The tracker did not compile, execute or hardware-test upstream software.
