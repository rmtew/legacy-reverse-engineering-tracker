# Reconstruction, emulation and port maintenance

Review eleven materially changed reconstruction, emulation and source-derived port projects against current primary commits.

Date: 2026-10-28 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- smalltalk80-by-the-book-pharo-vm / Build (reviewed): The tracker did not install Pharo, launch the VM, benchmark text display, or exercise the fallback.
- smalltalk80-by-the-book-pharo-vm / Runtime profiles (no-evidence-found): Pharo 11 or newer remains the documented host requirement, but the current change states no minimum CPU, RAM or operating-system version.
- smalltalk80-by-the-book-pharo-vm / AI (no-evidence-found): The reviewed commit contains no development-AI attribution; absence in this bounded evidence is not proof of non-use.
- snow-classic-mac-emulator / Build (reviewed): The tracker did not compile Snow or run its test suite; compatibility remains an upstream result.
- snow-classic-mac-emulator / Runtime profiles (no-evidence-found): The reviewed CPU-core and test changes state no minimum host CPU, RAM or operating-system requirement, so no runtime profile is inferred.
- snow-classic-mac-emulator / AI (no-evidence-found): Bounded README and current commit inspection found no explicit development-AI attribution. This does not establish non-use.
- th04-lotus-land-story-reconstruction / Build (reviewed): These are bounded upstream functional checks. The tracker did not download the preview, supply game assets, build either branch, or compare DOS pixel/timing or physical audio.
- th04-lotus-land-story-reconstruction / Runtime profiles (no-evidence-found): The reviewed guide establishes a Windows x64 build and a Linux SDL2 route but gives no minimum CPU, RAM, Windows version or Linux distribution. No minimum runtime profile is inferred.
- black-tiger-megadrive-native-port / Build (reviewed): The tracker did not build the ROM or run the tests. Upstream explicitly says physical hardware remains untested and does not claim a complete natural playthrough.
- black-tiger-megadrive-native-port / Runtime profiles (no-evidence-found): The release cites emulator checks and an earlier user report involving a Mega Drive Model 2 VA0 and EverGenesis V3, but explicitly says those physical configurations were unavailable for retest. No minimum hardware profile is recorded.
- black-tiger-megadrive-native-port / AI (no-evidence-found): The reviewed release commit contains no development-AI attribution; absence in this bounded evidence is not proof of non-use.
- virtua-tennis-dreamcast-analysis / Build (reviewed): These are upstream generator and test-ledger results. The tracker did not supply a disc/SDK, run the equivalence cases, or rebuild the executable.
- virtua-tennis-dreamcast-analysis / Runtime profiles (no-evidence-found): No minimum Dreamcast accessory/model profile or host runtime minimum is stated in the inspected decompilation documentation.
- zombie-revenge-dc-decompilation / Build (reviewed): These are upstream equivalence and progress results. The tracker did not supply a disc/SDK, execute the cases, or rebuild and run the game.
- zombie-revenge-dc-decompilation / Runtime profiles (no-evidence-found): The reviewed material does not state a minimum Dreamcast model/accessory profile or a verified host runtime profile beyond the original-platform SH-4 reconstruction context.
- shdecompilations-silent-hill-decomp / Build (reviewed): The tracker did not extract a supported game version, compile, execute, or byte-compare the project; the change is not evidence of whole-game completion.
- shdecompilations-silent-hill-decomp / Runtime profiles (no-evidence-found): The inspected README and collision change do not state a minimum original or host CPU, RAM, ROM/OS or chipset profile suitable for a verified runtime record.
- alien-breed-3d-source-derived-pc-port / Build (reviewed): The focused tests use synthetic states; upstream explicitly says an original-game emulator comparison has not been performed, and the tracker did not build or run the port.
- alien-breed-3d-source-derived-pc-port / Runtime profiles (needs-research): The reviewed combat repair gives no minimum host CPU, RAM, GPU or OS version for the desktop or web builds. Next check: Check primary build documentation and qualified releases for concrete minimum desktop/web requirements before adding a runtime profile.
- alien-breed-3d-source-derived-pc-port / AI (no-evidence-found): The reviewed documentation and commit contain no explicit development-AI attribution; absence in this bounded evidence is not proof of non-use.
- snepulator-sega-coleco-emulator / Build (reviewed): The tracker did not build Snepulator, load a ROM, or verify save interoperability and corruption handling.
- snepulator-sega-coleco-emulator / Runtime profiles (no-evidence-found): SDL2/OpenGL and zlib are software dependencies. No supported Linux hardware minimum was found; the explicit Windows cross-compiler architecture is not a minimum CPU profile.
- snepulator-sega-coleco-emulator / AI (no-evidence-found): No explicit AI-development evidence observed in the README, tree and selected source/build/license files reviewed. This is not evidence of no AI use.
- new-super-mario-bros-ds-decomp / Build (reviewed): The tracker did not build or execute the actor; this bounded recovery does not establish a compilable or playable full ROM.
- new-super-mario-bros-ds-decomp / Runtime profiles (no-evidence-found): No independently verified minimum runnable hardware profile established.
- new-super-mario-bros-ds-decomp / AI (no-evidence-found): No explicit AI-use disclosure established in inspected evidence. Agent/configuration presence alone is not proof of use; absence is not non-use.
- caesar0007-nfshs-psx-decomp / Build (needs-research): This is a source-contract cleanup, not a new whole-project exactness result. The tracker did not compile, test, run or byte-compare it. Next check: Follow the remaining source/SYM/SLD contracts and only promote whole-project byte exactness after upstream closes the explicit gaps.
- caesar0007-nfshs-psx-decomp / Runtime profiles (no-evidence-found): The reviewed source-contract change establishes no minimum PlayStation model, host CPU, RAM, OS or emulator requirement. Repository licensing terms are not a runtime profile.

## smalltalk80-by-the-book-pharo-vm

Project ID: smalltalk80-by-the-book-pharo-vm · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "smalltalk80-by-the-book-pharo-vm",
  "last_checked": "2026-10-28",
  "status": "Pharo-hosted Smalltalk-80 VM now implements and documents native primitive 103 text scanning with a guarded guest-code fallback; independent execution was not performed.",
  "techniques": [
    "snapshot serialization",
    "garbage-collection root preservation",
    "host filesystem bridging",
    "native guest-primitive acceleration"
  ]
}
```

Expected existing project SHA256: 7c072a62f2b9f8751d36977aef638f2eb03acae7b9a1869f925d42a20d989a25

### Identity (reviewed)

Independent implementation of the complete Bluebook Smalltalk-80 VM and environment in Smalltalk itself, with Tonel-format interpreter, object memory, BitBlt, display and filesystem adapters for Pharo.
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/README.md
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/src/Smalltalk-80%20VM/Interpreter.class.st
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/src/Smalltalk-80%20VM/ObjectMemory.class.st
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/LICENSE
- https://github.com/ljulliar/smalltalk-80-sources/commit/888028e157c272dcb49ffa04367de598bbd305bf
- https://github.com/ljulliar/smalltalk-80-sources/commit/aff99612b8b850bc844b9d930f8e6be59509e90d

### Classification (reviewed)

The project remains a Pharo-hosted implementation of the Bluebook Smalltalk-80 VM. The current commit deepens VM implementation rather than preserving or decompiling a native historical binary.
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/README.md
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/src/Smalltalk-80%20VM/Interpreter.class.st
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/src/Smalltalk-80%20VM/ObjectMemory.class.st
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/LICENSE
- https://github.com/ljulliar/smalltalk-80-sources/commit/888028e157c272dcb49ffa04367de598bbd305bf
- https://github.com/ljulliar/smalltalk-80-sources/commit/ac41c5a6699a040dcfb8a9f10499a2f7afb4ff10
- https://github.com/ljulliar/smalltalk-80-sources/commit/aff99612b8b850bc844b9d930f8e6be59509e90d

### Source CPU (not-applicable)

No physical predecessor input architecture established; compiler/VM host CPU is not treated as recovered input.
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/README.md
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/src/Smalltalk-80%20VM/Interpreter.class.st
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/src/Smalltalk-80%20VM/ObjectMemory.class.st
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/LICENSE
- https://github.com/ljulliar/smalltalk-80-sources/commit/888028e157c272dcb49ffa04367de598bbd305bf
- https://github.com/ljulliar/smalltalk-80-sources/commit/aff99612b8b850bc844b9d930f8e6be59509e90d

### Target CPU (reviewed)

No particular physical output CPU established; implementation-language portability does not prove host support.
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/README.md
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/src/Smalltalk-80%20VM/Interpreter.class.st
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/src/Smalltalk-80%20VM/ObjectMemory.class.st
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/LICENSE
- https://github.com/ljulliar/smalltalk-80-sources/commit/888028e157c272dcb49ffa04367de598bbd305bf
- https://github.com/ljulliar/smalltalk-80-sources/commit/aff99612b8b850bc844b9d930f8e6be59509e90d

### Build (reviewed)

Upstream documents primitive 103 as a host-side CharacterScanner implementation that validates all arguments before drawing, refreshes once per character run, and falls back to guest Smalltalk when disabled or invalid. The TODO now marks the accelerated scanner complete. Limitations: The tracker did not install Pharo, launch the VM, benchmark text display, or exercise the fallback.
- https://github.com/ljulliar/smalltalk-80-sources/commit/aff99612b8b850bc844b9d930f8e6be59509e90d

### Runtime profiles (no-evidence-found)

Pharo 11 or newer remains the documented host requirement, but the current change states no minimum CPU, RAM or operating-system version.
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/README.md
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/src/Smalltalk-80%20VM/Interpreter.class.st
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/src/Smalltalk-80%20VM/ObjectMemory.class.st
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/LICENSE
- https://github.com/ljulliar/smalltalk-80-sources/commit/888028e157c272dcb49ffa04367de598bbd305bf
- https://github.com/ljulliar/smalltalk-80-sources/commit/ac41c5a6699a040dcfb8a9f10499a2f7afb4ff10
- https://github.com/ljulliar/smalltalk-80-sources/commit/aff99612b8b850bc844b9d930f8e6be59509e90d

### AI (no-evidence-found)

The reviewed commit contains no development-AI attribution; absence in this bounded evidence is not proof of non-use.
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/README.md
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/src/Smalltalk-80%20VM/Interpreter.class.st
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/src/Smalltalk-80%20VM/ObjectMemory.class.st
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/LICENSE
- https://github.com/ljulliar/smalltalk-80-sources/commit/888028e157c272dcb49ffa04367de598bbd305bf
- https://github.com/ljulliar/smalltalk-80-sources/commit/ac41c5a6699a040dcfb8a9f10499a2f7afb4ff10
- https://github.com/ljulliar/smalltalk-80-sources/commit/aff99612b8b850bc844b9d930f8e6be59509e90d

### Relationships (reviewed)

Credits Banay implementation for debugging reference, Bluebook chapters, and Mario Wolczko image archive.
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/README.md
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/src/Smalltalk-80%20VM/Interpreter.class.st
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/src/Smalltalk-80%20VM/ObjectMemory.class.st
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/LICENSE
- https://github.com/ljulliar/smalltalk-80-sources/commit/888028e157c272dcb49ffa04367de598bbd305bf
- https://github.com/ljulliar/smalltalk-80-sources/commit/aff99612b8b850bc844b9d930f8e6be59509e90d

## snow-classic-mac-emulator

Project ID: snow-classic-mac-emulator · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "snow-classic-mac-emulator",
  "last_checked": "2026-10-28",
  "status": "Active classic-Mac emulator/debugger; current M68k work corrects exception-frame PCs for long divide-by-zero and FTRAPcc and adds focused format-2 frame tests.",
  "techniques": [
    "deterministic weak-bit and drive-noise replay",
    "exception-frame conformance tests"
  ]
}
```

Expected existing project SHA256: 7c92d0f3baa0fa454412a4c6337b7f8ce66147c03c177131fe7fd347322681f0

### Identity (reviewed)

Hardware-level Rust Macintosh emulator with integrated disassembly, breakpoints, watchpoints, trap/history viewers and flux/bitstream disk support.
- https://github.com/twvd/snow/blob/f2b2e3c48251641ed317b5799d9d159141dd06bc/README.md
- https://github.com/twvd/snow/blob/f2b2e3c48251641ed317b5799d9d159141dd06bc/docs/BUILDING.md
- https://github.com/twvd/snow/commit/e2cdbb9904b7bb0f7b546ccfc762de55dee11723
- https://github.com/twvd/snow/commit/690a13d453a33c196f34326a586f6bd33f67ce58

### Classification (reviewed)

Inspected IWM register/edge-driven controller code and compact-Mac bus implementation. README lists 128K through IIx/SE30/Portable/PowerBook models, 68000/68020/68030 and PMMU/FPU support. Peripherals and debugging establish a general research tool, not an application-specific wrapper. MIT licence for Snow; README acknowledges Musashi/MAME as reference and separately attributed components including Fluxfox and BlueSCSI Toolbox.
- https://github.com/twvd/snow/blob/f2b2e3c48251641ed317b5799d9d159141dd06bc/README.md
- https://github.com/twvd/snow/blob/f2b2e3c48251641ed317b5799d9d159141dd06bc/docs/BUILDING.md
- https://github.com/twvd/snow/commit/e2cdbb9904b7bb0f7b546ccfc762de55dee11723
- https://github.com/twvd/snow/commit/690a13d453a33c196f34326a586f6bd33f67ce58

### Source CPU (reviewed)

Documented source/input platforms: Macintosh. Processor scope: m68k.
- https://github.com/twvd/snow/blob/f2b2e3c48251641ed317b5799d9d159141dd06bc/README.md
- https://github.com/twvd/snow/blob/f2b2e3c48251641ed317b5799d9d159141dd06bc/docs/BUILDING.md
- https://github.com/twvd/snow/commit/e2cdbb9904b7bb0f7b546ccfc762de55dee11723
- https://github.com/twvd/snow/commit/690a13d453a33c196f34326a586f6bd33f67ce58

### Target CPU (reviewed)

No fixed target CPU is established; portability of the implementation language is not proof of supported architectures.
- https://github.com/twvd/snow/blob/f2b2e3c48251641ed317b5799d9d159141dd06bc/README.md
- https://github.com/twvd/snow/blob/f2b2e3c48251641ed317b5799d9d159141dd06bc/docs/BUILDING.md
- https://github.com/twvd/snow/commit/e2cdbb9904b7bb0f7b546ccfc762de55dee11723
- https://github.com/twvd/snow/commit/690a13d453a33c196f34326a586f6bd33f67ce58

### Build (reviewed)

The reviewed diff advances the emulated 68k core by correcting the saved PC after DIVS/DIVU and using the pumped prefetch path for FTRAPcc. New tests cover long register and indexed-memory division plus word, long and no-immediate FTRAPT forms. Limitations: The tracker did not compile Snow or run its test suite; compatibility remains an upstream result.
- https://github.com/twvd/snow/commit/690a13d453a33c196f34326a586f6bd33f67ce58

### Runtime profiles (no-evidence-found)

The reviewed CPU-core and test changes state no minimum host CPU, RAM or operating-system requirement, so no runtime profile is inferred.
- https://github.com/twvd/snow/commit/690a13d453a33c196f34326a586f6bd33f67ce58

### AI (no-evidence-found)

Bounded README and current commit inspection found no explicit development-AI attribution. This does not establish non-use.
- https://github.com/twvd/snow/blob/f2b2e3c48251641ed317b5799d9d159141dd06bc/README.md
- https://github.com/twvd/snow/blob/f2b2e3c48251641ed317b5799d9d159141dd06bc/docs/BUILDING.md
- https://github.com/twvd/snow/commit/e2cdbb9904b7bb0f7b546ccfc762de55dee11723
- https://github.com/twvd/snow/commit/690a13d453a33c196f34326a586f6bd33f67ce58

### Relationships (reviewed)

New implementation with own hardware-level model and debugger; bounded screen found no tracked Snow equivalent. Source references are not a claim that Snow is a fork of MAME or Musashi.
- https://github.com/twvd/snow/blob/f2b2e3c48251641ed317b5799d9d159141dd06bc/README.md
- https://github.com/twvd/snow/blob/f2b2e3c48251641ed317b5799d9d159141dd06bc/docs/BUILDING.md
- https://github.com/twvd/snow/commit/e2cdbb9904b7bb0f7b546ccfc762de55dee11723
- https://github.com/twvd/snow/commit/690a13d453a33c196f34326a586f6bd33f67ce58

## th04-lotus-land-story-reconstruction

Project ID: th04-lotus-land-story-reconstruction · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "ai": {
    "evidence": [
      "Recent primary commit subjects explicitly identify gpt-6.1-sol, including 55cf73e966cacc453a73953bf4f4fa69fb96a9fc.",
      "Agent project instructions/configuration present (configuration only; does not establish AI contribution)",
      "Primary commit subject explicitly identifies GPT-6.1 work: https://github.com/N0zoM1z0/th04/commit/09e80fdfabe5f0be8f19969a9f97adf9dec40707"
    ],
    "tools": [
      "GPT-6.1"
    ],
    "usage": true
  },
  "id": "th04-lotus-land-story-reconstruction",
  "last_checked": "2026-10-28",
  "status": "PC-98 reconstruction plus a downloadable Windows x64 preview; upstream documents Normal/Extra, ending/name/save and Music Room checks while complete DOS pixel/timing and physical-sound identity remain open.",
  "techniques": [
    "Ghidra",
    "function-level reconstruction",
    "differential execution",
    "binary matching",
    "DOSBox-X runtime validation",
    "native porting",
    "original/reconstructed replay comparison",
    "state-pool comparison",
    "cadence calibration",
    "instruction-vector comparison",
    "undefined-behavior sanitizer contracts",
    "registration-route parity testing",
    "continue-route differential execution",
    "title/GRCG differential validation",
    "negative-replay preservation",
    "PC-98 keyboard and UART oracle comparison",
    "Windows x64 functional smoke validation"
  ]
}
```

Expected existing project SHA256: 3aaaceef679cf9dbc710473d89ab518e2a4822a477ab0206790892609af47835

### Identity (reviewed)

Primary README continues to identify the original Japanese Touhou 4 and its MAIN.EXE, OP.EXE, MAINE.EXE and ZUN.COM reconstructions.
- https://github.com/N0zoM1z0/th04/blob/main/README.md
- https://github.com/N0zoM1z0/th04/commit/09e80fdfabe5f0be8f19969a9f97adf9dec40707

### Classification (reviewed)

The repository remains a PC-98 source reconstruction with a separate unfinished native x64 port; the new work expands bounded native recovery rather than changing that classification.
- https://github.com/N0zoM1z0/th04/commit/5e04432eb943c8155c7525cbe93f6211a5ca7414
- https://github.com/N0zoM1z0/th04/commit/09e80fdfabe5f0be8f19969a9f97adf9dec40707

### Source CPU (reviewed)

Maintained source and existing primary documentation continue to establish 16-bit x86 PC-98 executables; the new instruction-vector work does not change the source architecture.
- https://github.com/N0zoM1z0/th04/blob/main/README.md
- https://github.com/N0zoM1z0/th04/commit/09e80fdfabe5f0be8f19969a9f97adf9dec40707

### Target CPU (reviewed)

The project still produces 16-bit x86 DOS targets and maintains a Linux/Windows x64 native port. No additional architecture is introduced by the reviewed commits.
- https://github.com/N0zoM1z0/th04/blob/main/README.md
- https://github.com/N0zoM1z0/th04/commit/09e80fdfabe5f0be8f19969a9f97adf9dec40707

### Build (reviewed)

The root documentation now gives a release/download path and an exact MinGW-w64/CMake/Ninja source-build route for the port/modern-64 branch. Upstream reports hooked-window clears for Normal Reimu A, Normal Marisa B and earned Extra Reimu A plus ending, save and audio checks. Limitations: These are bounded upstream functional checks. The tracker did not download the preview, supply game assets, build either branch, or compare DOS pixel/timing or physical audio.
- https://github.com/N0zoM1z0/th04/commit/09e80fdfabe5f0be8f19969a9f97adf9dec40707

### Runtime profiles (no-evidence-found)

The reviewed guide establishes a Windows x64 build and a Linux SDL2 route but gives no minimum CPU, RAM, Windows version or Linux distribution. No minimum runtime profile is inferred.
- https://github.com/N0zoM1z0/th04/commit/09e80fdfabe5f0be8f19969a9f97adf9dec40707

### AI (reviewed)

The reviewed commits explicitly identify gpt-6.1-sol; attribution remains scoped to the evidenced title-work commits.
- https://github.com/N0zoM1z0/th04/commit/566c2049f20cfc49d975e907392f68abe162b11a
- https://github.com/N0zoM1z0/th04/commit/ef35bc527f93564f0547a617a79435317e74bbd3
- https://github.com/N0zoM1z0/th04/commit/09e80fdfabe5f0be8f19969a9f97adf9dec40707

### Relationships (reviewed)

ReC98 remains a pinned source-routing and migration input while this repository maintains its own standalone product source and native-port verification history.
- https://github.com/N0zoM1z0/th04/blob/main/README.md
- https://github.com/N0zoM1z0/th04/commit/09e80fdfabe5f0be8f19969a9f97adf9dec40707

## black-tiger-megadrive-native-port

Project ID: black-tiger-megadrive-native-port · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "black-tiger-megadrive-native-port",
  "last_checked": "2026-10-28",
  "status": "Source-only v1.9.5 native Mega Drive port; restores Round 5/7 dialogue scenery, snake poison, falling-rock sound and used bonus-door persistence, with physical hardware still untested.",
  "techniques": [
    "ROM disassembly and behavioral analysis",
    "MAME observation oracles",
    "native 68000 reimplementation",
    "build-time asset conversion",
    "source-versus-port regression comparisons",
    "controlled encounter fixtures",
    "cross-emulator smoke testing",
    "fixture-based runtime regression testing"
  ]
}
```

Expected existing project SHA256: 1e38a8f631168b7bcc7c434d03bec1aa31fcd69bd86f137264a41fb79b74fd25

### Identity (reviewed)

Root README, manifest and repository metadata identify a source-only Black Tiger arcade-to-Mega Drive port. The manifest says the exact revision is unknown despite hash-locked files; do not silently claim an independently verified arcade revision.
- https://github.com/rester159/blacktiger_MD/blob/main/README.md
- https://github.com/rester159/blacktiger_MD/blob/main/STATUS.md
- https://github.com/rester159/blacktiger_MD/blob/main/Makefile
- https://github.com/rester159/blacktiger_MD/blob/main/docs/source-only.md
- https://github.com/rester159/blacktiger_MD/blob/main/reference/player_audit.md
- https://github.com/rester159/blacktiger_MD/blob/main/reference/audio_audit.md
- https://github.com/rester159/blacktiger_MD/blob/main/src/main.c
- https://github.com/rester159/blacktiger_MD/blob/main/src/game.c
- https://github.com/rester159/blacktiger_MD/blob/main/assets/rom_manifest.json
- https://github.com/mamedev/mame/blob/master/src/mame/capcom/blktiger.cpp
- https://github.com/rester159/blacktiger_MD/commit/2809c483235e6808d5f82eb72aa30471815aeacf

### Classification (reviewed)

v1.9.2 remains a native SGDK/Mega Drive behavioral port. The release text explicitly says the cartridge does not execute the arcade CPU, so the update is not relabelled as embedded emulation or original-source recovery.
- https://github.com/rester159/blacktiger_MD/blob/main/README.md
- https://github.com/rester159/blacktiger_MD/blob/main/STATUS.md
- https://github.com/rester159/blacktiger_MD/blob/main/Makefile
- https://github.com/rester159/blacktiger_MD/blob/main/docs/source-only.md
- https://github.com/rester159/blacktiger_MD/blob/main/reference/player_audit.md
- https://github.com/rester159/blacktiger_MD/blob/main/reference/audio_audit.md
- https://github.com/rester159/blacktiger_MD/blob/main/src/main.c
- https://github.com/rester159/blacktiger_MD/blob/main/src/game.c
- https://github.com/rester159/blacktiger_MD/blob/main/assets/rom_manifest.json
- https://github.com/mamedev/mame/blob/master/src/mame/capcom/blktiger.cpp
- https://github.com/rester159/blacktiger_MD/commit/11d356548eb0b5683b498e8a16a2efd674b4e202
- https://github.com/rester159/blacktiger_MD/commit/2809c483235e6808d5f82eb72aa30471815aeacf

### Source CPU (reviewed)

Z80 established by player audit and MAME primary driver, which identifies main and audio Z80 CPUs. Driver also describes an 8751 protection MCU; the reviewed port scope reconstructs Z80 gameplay/audio behavior, not that MCU's program.
- https://github.com/rester159/blacktiger_MD/blob/main/README.md
- https://github.com/rester159/blacktiger_MD/blob/main/STATUS.md
- https://github.com/rester159/blacktiger_MD/blob/main/Makefile
- https://github.com/rester159/blacktiger_MD/blob/main/docs/source-only.md
- https://github.com/rester159/blacktiger_MD/blob/main/reference/player_audit.md
- https://github.com/rester159/blacktiger_MD/blob/main/reference/audio_audit.md
- https://github.com/rester159/blacktiger_MD/blob/main/src/main.c
- https://github.com/rester159/blacktiger_MD/blob/main/src/game.c
- https://github.com/rester159/blacktiger_MD/blob/main/assets/rom_manifest.json
- https://github.com/mamedev/mame/blob/master/src/mame/capcom/blktiger.cpp
- https://github.com/rester159/blacktiger_MD/commit/2809c483235e6808d5f82eb72aa30471815aeacf

### Target CPU (reviewed)

README explicitly states native 68000 game logic; Makefile invokes m68k-elf-gcc -m68000. No inferred host CPU.
- https://github.com/rester159/blacktiger_MD/blob/main/README.md
- https://github.com/rester159/blacktiger_MD/blob/main/STATUS.md
- https://github.com/rester159/blacktiger_MD/blob/main/Makefile
- https://github.com/rester159/blacktiger_MD/blob/main/docs/source-only.md
- https://github.com/rester159/blacktiger_MD/blob/main/reference/player_audit.md
- https://github.com/rester159/blacktiger_MD/blob/main/reference/audio_audit.md
- https://github.com/rester159/blacktiger_MD/blob/main/src/main.c
- https://github.com/rester159/blacktiger_MD/blob/main/src/game.c
- https://github.com/rester159/blacktiger_MD/blob/main/assets/rom_manifest.json
- https://github.com/mamedev/mame/blob/master/src/mame/capcom/blktiger.cpp
- https://github.com/rester159/blacktiger_MD/commit/2809c483235e6808d5f82eb72aa30471815aeacf

### Build (reviewed)

Upstream's v1.9.5 status reports 194 test recipes and strict packaging passing for a hash-identified ROM after dialogue, snake, rock and bonus-door fixes. Limitations: The tracker did not build the ROM or run the tests. Upstream explicitly says physical hardware remains untested and does not claim a complete natural playthrough.
- https://github.com/rester159/blacktiger_MD/commit/2809c483235e6808d5f82eb72aa30471815aeacf

### Runtime profiles (no-evidence-found)

The release cites emulator checks and an earlier user report involving a Mega Drive Model 2 VA0 and EverGenesis V3, but explicitly says those physical configurations were unavailable for retest. No minimum hardware profile is recorded.
- https://github.com/rester159/blacktiger_MD/blob/main/README.md
- https://github.com/rester159/blacktiger_MD/blob/main/STATUS.md
- https://github.com/rester159/blacktiger_MD/blob/main/Makefile
- https://github.com/rester159/blacktiger_MD/blob/main/docs/source-only.md
- https://github.com/rester159/blacktiger_MD/blob/main/reference/player_audit.md
- https://github.com/rester159/blacktiger_MD/blob/main/reference/audio_audit.md
- https://github.com/rester159/blacktiger_MD/blob/main/src/main.c
- https://github.com/rester159/blacktiger_MD/blob/main/src/game.c
- https://github.com/rester159/blacktiger_MD/blob/main/assets/rom_manifest.json
- https://github.com/mamedev/mame/blob/master/src/mame/capcom/blktiger.cpp
- https://github.com/rester159/blacktiger_MD/commit/11d356548eb0b5683b498e8a16a2efd674b4e202
- https://github.com/rester159/blacktiger_MD/commit/2809c483235e6808d5f82eb72aa30471815aeacf

### AI (no-evidence-found)

The reviewed release commit contains no development-AI attribution; absence in this bounded evidence is not proof of non-use.
- https://github.com/rester159/blacktiger_MD/blob/main/README.md
- https://github.com/rester159/blacktiger_MD/blob/main/STATUS.md
- https://github.com/rester159/blacktiger_MD/blob/main/Makefile
- https://github.com/rester159/blacktiger_MD/blob/main/docs/source-only.md
- https://github.com/rester159/blacktiger_MD/blob/main/reference/player_audit.md
- https://github.com/rester159/blacktiger_MD/blob/main/reference/audio_audit.md
- https://github.com/rester159/blacktiger_MD/blob/main/src/main.c
- https://github.com/rester159/blacktiger_MD/blob/main/src/game.c
- https://github.com/rester159/blacktiger_MD/blob/main/assets/rom_manifest.json
- https://github.com/mamedev/mame/blob/master/src/mame/capcom/blktiger.cpp
- https://github.com/rester159/blacktiger_MD/commit/11d356548eb0b5683b498e8a16a2efd674b4e202
- https://github.com/rester159/blacktiger_MD/commit/2809c483235e6808d5f82eb72aa30471815aeacf

### Relationships (reviewed)

Distinct from Side Arms MD; shares author/SGDK/native-port approach. MAME is an offline reference/oracle, not runtime. No canonical or subject duplicate in catalogue.
- https://github.com/rester159/blacktiger_MD/blob/main/README.md
- https://github.com/rester159/blacktiger_MD/blob/main/STATUS.md
- https://github.com/rester159/blacktiger_MD/blob/main/Makefile
- https://github.com/rester159/blacktiger_MD/blob/main/docs/source-only.md
- https://github.com/rester159/blacktiger_MD/blob/main/reference/player_audit.md
- https://github.com/rester159/blacktiger_MD/blob/main/reference/audio_audit.md
- https://github.com/rester159/blacktiger_MD/blob/main/src/main.c
- https://github.com/rester159/blacktiger_MD/blob/main/src/game.c
- https://github.com/rester159/blacktiger_MD/blob/main/assets/rom_manifest.json
- https://github.com/mamedev/mame/blob/master/src/mame/capcom/blktiger.cpp
- https://github.com/rester159/blacktiger_MD/commit/2809c483235e6808d5f82eb72aa30471815aeacf

## virtua-tennis-dreamcast-analysis

Project ID: virtua-tennis-dreamcast-analysis · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "virtua-tennis-dreamcast-analysis",
  "last_checked": "2026-10-28",
  "status": "Dreamcast SH-4 decompilation; upstream reports 96.5% of C-capable functions, 77.3% of eligible code bytes and 54.8% aggregate instruction coverage, while retaining 114 functions left.",
  "techniques": [
    "directed function-equivalence testing"
  ]
}
```

Expected existing project SHA256: 5de77b3f805ab18a26d2c601d590bc231c9c3a1298b42b4194c488fde1ac9d83

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

The reviewed commit proves 13 more functions and removes six equivalence entries whose cases did not hold after stricter call-boundary checking. The pinned README reports 3,186 of 3,300 C-capable functions complete, 613,996 of 794,572 eligible bytes complete, and 54.8% aggregate instruction coverage; the assembly baseline still rebuilds byte for byte. Limitations: These are upstream generator and test-ledger results. The tracker did not supply a disc/SDK, run the equivalence cases, or rebuild the executable.
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/commit/5c3062a3ebc613061ea8e5a94ac01ec92fac299d

### Runtime profiles (no-evidence-found)

No minimum Dreamcast accessory/model profile or host runtime minimum is stated in the inspected decompilation documentation.
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/blob/d82fc50aa7af487a308c5ceac87b4f7a2b01a14d/README.md
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/commit/5c3062a3ebc613061ea8e5a94ac01ec92fac299d

### AI (reviewed)

The reviewed generator/progress commit explicitly carries a Claude Opus 5.5 co-author trailer. Attribution is scoped to evidenced work, not generalized to every recovered function.
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/commit/d82fc50aa7af487a308c5ceac87b4f7a2b01a14d
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/commit/5c3062a3ebc613061ea8e5a94ac01ec92fac299d

### Relationships (reviewed)

SDK-identical library functions are explicitly tracked separately from game-derived C recovery. The repository remains a title-specific project sharing tooling and the Shuriken Explorer presentation with related Dreamcast decomps.
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/blob/d82fc50aa7af487a308c5ceac87b4f7a2b01a14d/sdk-identical.txt
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/blob/d82fc50aa7af487a308c5ceac87b4f7a2b01a14d/README.md
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/commit/5c3062a3ebc613061ea8e5a94ac01ec92fac299d

## zombie-revenge-dc-decompilation

Project ID: zombie-revenge-dc-decompilation · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "zombie-revenge-dc-decompilation",
  "last_checked": "2026-10-28",
  "status": "Dreamcast SH-4 decompilation; upstream reports 95.7% of C-capable functions, 87.6% of eligible code bytes and 65.5% aggregate instruction coverage, with 176 functions left.",
  "techniques": [
    "directed function-equivalence testing"
  ]
}
```

Expected existing project SHA256: 484be9b0b623a5026dfaab081a9928f8838c36b274894531f9b728676e91e6db

### Identity (reviewed)

Zombie Revenge Dreamcast decompilation with disc-derived local extraction, generated C, assembly fallback and an interactive Shuriken Explorer view.
- https://github.com/consolesplayingconsoles/zombie-revenge-decomp/blob/ed22b044680a2b7e513470e99ff16e3e2f7fefeb/README.md
- https://github.com/consolesplayingconsoles/zombie-revenge-decomp/commit/9560f436a7721932ff474030d72453676b258b7e

### Classification (reviewed)

Original-platform game decompilation and source reconstruction. Whole-executable matching with assembly fallback is kept distinct from complete C recovery and from per-function behavioral equivalence.
- https://github.com/consolesplayingconsoles/zombie-revenge-decomp/blob/ed22b044680a2b7e513470e99ff16e3e2f7fefeb/README.md
- https://github.com/consolesplayingconsoles/zombie-revenge-decomp/blob/ed22b044680a2b7e513470e99ff16e3e2f7fefeb/docs/equivalent.md
- https://github.com/consolesplayingconsoles/zombie-revenge-decomp/commit/9560f436a7721932ff474030d72453676b258b7e

### Source CPU (reviewed)

The reconstructed Dreamcast executable remains SH-4 input.
- https://github.com/consolesplayingconsoles/zombie-revenge-decomp/blob/ed22b044680a2b7e513470e99ff16e3e2f7fefeb/README.md
- https://github.com/consolesplayingconsoles/zombie-revenge-decomp/commit/9560f436a7721932ff474030d72453676b258b7e

### Target CPU (reviewed)

The matching rebuild remains SH-4 output for the original Dreamcast executable; no host port CPU is claimed.
- https://github.com/consolesplayingconsoles/zombie-revenge-decomp/blob/ed22b044680a2b7e513470e99ff16e3e2f7fefeb/README.md
- https://github.com/consolesplayingconsoles/zombie-revenge-decomp/commit/9560f436a7721932ff474030d72453676b258b7e

### Build (reviewed)

The reviewed commit proves three more functions, including one previously timing out only under a ten-worker run and two admitted after comparing calls against registers the callee actually reads. The pinned README reports 3,883 of 4,059 C-capable functions complete, 595,552 of 679,764 eligible bytes complete, and 65.5% aggregate instruction coverage. Limitations: These are upstream equivalence and progress results. The tracker did not supply a disc/SDK, execute the cases, or rebuild and run the game.
- https://github.com/consolesplayingconsoles/zombie-revenge-decomp/commit/9560f436a7721932ff474030d72453676b258b7e

### Runtime profiles (no-evidence-found)

The reviewed material does not state a minimum Dreamcast model/accessory profile or a verified host runtime profile beyond the original-platform SH-4 reconstruction context.
- https://github.com/consolesplayingconsoles/zombie-revenge-decomp/blob/ed22b044680a2b7e513470e99ff16e3e2f7fefeb/README.md
- https://github.com/consolesplayingconsoles/zombie-revenge-decomp/commit/9560f436a7721932ff474030d72453676b258b7e

### AI (reviewed)

The reviewed progress commit explicitly carries a Claude Opus 5.5 co-author trailer. Attribution is limited to evidenced work rather than treating the full decompilation as AI-generated.
- https://github.com/consolesplayingconsoles/zombie-revenge-decomp/commit/ed22b044680a2b7e513470e99ff16e3e2f7fefeb
- https://github.com/consolesplayingconsoles/zombie-revenge-decomp/commit/9560f436a7721932ff474030d72453676b258b7e

### Relationships (reviewed)

SDK-identical functions are now explicitly separated from game-derived recovery. The repository remains one title-specific decompilation in the consolesplayingconsoles tool/explorer ecosystem.
- https://github.com/consolesplayingconsoles/zombie-revenge-decomp/blob/ed22b044680a2b7e513470e99ff16e3e2f7fefeb/sdk-identical.txt
- https://github.com/consolesplayingconsoles/zombie-revenge-decomp/blob/ed22b044680a2b7e513470e99ff16e3e2f7fefeb/README.md
- https://github.com/consolesplayingconsoles/zombie-revenge-decomp/commit/9560f436a7721932ff474030d72453676b258b7e

## shdecompilations-silent-hill-decomp

Project ID: shdecompilations-silent-hill-decomp · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "shdecompilations-silent-hill-decomp",
  "last_checked": "2026-10-28",
  "status": "In-progress PlayStation matching decompilation; current work deobfuscates collision triggers across all supported regional symbol maps without establishing a complete playable reconstruction.",
  "techniques": [
    "collision-trigger deobfuscation"
  ]
}
```

Expected existing project SHA256: 456d8a43504ee26983f7b559c030cb513b5647983df054d06255ee46c5424979

### Identity (reviewed)

Silent Hill PlayStation matching decompilation. Current head materially refines the body-program collision subsystem rather than introducing a separate project.
- https://github.com/shdecompilations/silent-hill-decomp
- https://github.com/shdecompilations/silent-hill-decomp/commit/59fd80f8180f18d9d90c3442cc04ed1293786973
- https://github.com/shdecompilations/silent-hill-decomp/commit/3b9a686c490abdf2b771ef064a241c3434c1ee90

### Classification (reviewed)

Original-platform source reconstruction with executable and overlay matching. The collision commit turns previously opaque layout and control flow into typed polygon/cylinder attributes and named pass-state behavior; it is not a PC port.
- https://github.com/shdecompilations/silent-hill-decomp/commit/59fd80f8180f18d9d90c3442cc04ed1293786973
- https://github.com/shdecompilations/silent-hill-decomp/commit/3b9a686c490abdf2b771ef064a241c3434c1ee90

### Source CPU (reviewed)

The reviewed project remains a PlayStation MIPS executable reconstruction; the collision refactor does not change that source architecture.
- https://github.com/shdecompilations/silent-hill-decomp/blob/59fd80f8180f18d9d90c3442cc04ed1293786973/README.md
- https://github.com/shdecompilations/silent-hill-decomp/commit/3b9a686c490abdf2b771ef064a241c3434c1ee90

### Target CPU (reviewed)

Matching output remains original-target MIPS code; no additional port architecture is established by the reviewed change.
- https://github.com/shdecompilations/silent-hill-decomp/blob/59fd80f8180f18d9d90c3442cc04ed1293786973/README.md
- https://github.com/shdecompilations/silent-hill-decomp/commit/3b9a686c490abdf2b771ef064a241c3434c1ee90

### Build (reviewed)

The reviewed change introduces a dedicated collision-trigger interface and rewrites affected collision, title-event, water and enemy code while updating USA, EUR and both Japanese symbol maps. Limitations: The tracker did not extract a supported game version, compile, execute, or byte-compare the project; the change is not evidence of whole-game completion.
- https://github.com/shdecompilations/silent-hill-decomp/commit/3b9a686c490abdf2b771ef064a241c3434c1ee90

### Runtime profiles (no-evidence-found)

The inspected README and collision change do not state a minimum original or host CPU, RAM, ROM/OS or chipset profile suitable for a verified runtime record.
- https://github.com/shdecompilations/silent-hill-decomp/blob/59fd80f8180f18d9d90c3442cc04ed1293786973/README.md
- https://github.com/shdecompilations/silent-hill-decomp/commit/59fd80f8180f18d9d90c3442cc04ed1293786973
- https://github.com/shdecompilations/silent-hill-decomp/commit/3b9a686c490abdf2b771ef064a241c3434c1ee90

### AI (reviewed)

The repository's existing bounded disclosure remains: game code is not knowingly AI-generated, while some throwaway decompilation helpers used AI. The reviewed collision commit carries no additional AI attribution.
- https://github.com/shdecompilations/silent-hill-decomp/blob/59fd80f8180f18d9d90c3442cc04ed1293786973/README.md
- https://github.com/shdecompilations/silent-hill-decomp/commit/59fd80f8180f18d9d90c3442cc04ed1293786973
- https://github.com/shdecompilations/silent-hill-decomp/commit/3b9a686c490abdf2b771ef064a241c3434c1ee90

### Relationships (reviewed)

The README's Vatuu references remain project lineage. The collision subsystem is part of the same body-program reconstruction, not a separately promoted component.
- https://github.com/shdecompilations/silent-hill-decomp/blob/59fd80f8180f18d9d90c3442cc04ed1293786973/README.md
- https://github.com/shdecompilations/silent-hill-decomp/commit/3b9a686c490abdf2b771ef064a241c3434c1ee90

## alien-breed-3d-source-derived-pc-port

Project ID: alien-breed-3d-source-derived-pc-port · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "alien-breed-3d-source-derived-pc-port",
  "last_checked": "2026-10-28",
  "status": "Amiga-source-derived SDL2 PC/web port; restores the shotgun soldier's original five-pellet instant-hit attack with 16 focused production-handler cases, while natural and original-emulator comparison remain open.",
  "techniques": [
    "assembly-to-C translation",
    "Amiga asset format reuse",
    "SDL2 rendering",
    "source-derived combat-behavior restoration"
  ]
}
```

Expected existing project SHA256: cf56c4d035f82cd860ca7fc7307cd8613457eba155f460c84cf5cef49ca6645a

### Identity (reviewed)

Alien Breed 3D source-derived PC/web port built from released Amiga source and retaining the original game's data formats.
- https://github.com/retro-foundry/Alien-Breed-HD/commit/61a13bc47a22bae885b44de2ed03b4ba1246d420

### Classification (reviewed)

This remains a source-derived SDL2 port rather than a decompilation or an emulator-hosted original binary.
- https://github.com/retro-foundry/Alien-Breed-HD/commit/61a13bc47a22bae885b44de2ed03b4ba1246d420

### Source CPU (reviewed)

The preserved original Amiga source is Motorola 68000 assembly; the source architecture is not inferred from the modern port language.
- https://github.com/retro-foundry/Alien-Breed-HD/commit/61a13bc47a22bae885b44de2ed03b4ba1246d420

### Target CPU (not-applicable)

No fixed output CPU is established for the portable desktop/web builds, so a host architecture is not inferred.
- https://github.com/retro-foundry/Alien-Breed-HD/commit/61a13bc47a22bae885b44de2ed03b4ba1246d420

### Build (reviewed)

The reviewed documentation traces the shotgun behavior to FlameMarine.s and replaces an unreachable flamer branch with five instant-hit pellets, original sample/volume and recovery timing. Sixteen focused cases cover both players, option values, range, tick batching, windup, sound, recovery and pool behavior. Limitations: The focused tests use synthetic states; upstream explicitly says an original-game emulator comparison has not been performed, and the tracker did not build or run the port.
- https://github.com/retro-foundry/Alien-Breed-HD/commit/61a13bc47a22bae885b44de2ed03b4ba1246d420

### Runtime profiles (needs-research)

The reviewed combat repair gives no minimum host CPU, RAM, GPU or OS version for the desktop or web builds. Next check: Check primary build documentation and qualified releases for concrete minimum desktop/web requirements before adding a runtime profile.
- https://github.com/retro-foundry/Alien-Breed-HD/commit/61a13bc47a22bae885b44de2ed03b4ba1246d420

### AI (no-evidence-found)

The reviewed documentation and commit contain no explicit development-AI attribution; absence in this bounded evidence is not proof of non-use.
- https://github.com/retro-foundry/Alien-Breed-HD/commit/61a13bc47a22bae885b44de2ed03b4ba1246d420

### Relationships (reviewed)

The port is derived from the released Alien Breed 3D Amiga source; the reviewed change remains within the same project.
- https://github.com/retro-foundry/Alien-Breed-HD/commit/61a13bc47a22bae885b44de2ed03b4ba1246d420

## snepulator-sega-coleco-emulator

Project ID: snepulator-sega-coleco-emulator · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "snepulator-sega-coleco-emulator",
  "last_checked": "2026-10-28",
  "status": "Multi-system emulator with default Mega Drive support; current code parses ROM headers and adds battery-backed SRAM load, mapping, access control and save-file synchronization.",
  "techniques": [
    "ROM-header parsing",
    "battery-backed SRAM persistence"
  ]
}
```

Expected existing project SHA256: 96500a9baa03785e76699e3461683a92152ede48f8710897bdaab356ff5ed9e8

### Identity (reviewed)

Canonical repository metadata and inspected primary files establish Snepulator. Reviewed tree 5ef72fde6b11cbbdb9acd555317cfddfd170baab. Upstream push date supplies provisional last_activity; repository creation is not used as the project start date. Active multi-system emulator with source and build recipe. Primary-source inspection only; no independent build or runtime test.
- https://github.com/JoppyFurr/Snepulator
- https://github.com/JoppyFurr/Snepulator/blob/main/README.md
- https://api.github.com/repos/JoppyFurr/Snepulator
- https://github.com/JoppyFurr/Snepulator/commit/47eff3cfe274bd5b88d14a2f8ddf4f6cdaaae655

### Classification (reviewed)

The current default build includes the previously developer-gated Mega Drive core and upstream reports a number of games playable. The README machine list still trails this change, so the record preserves that documentation boundary.
- https://github.com/JoppyFurr/Snepulator/commit/2a6523d20e1b
- https://github.com/JoppyFurr/Snepulator/blob/main/build.sh
- https://github.com/JoppyFurr/Snepulator/blob/main/README.md
- https://github.com/JoppyFurr/Snepulator/commit/47eff3cfe274bd5b88d14a2f8ddf4f6cdaaae655

### Source CPU (reviewed)

build.sh explicitly compiles source/cpu/m68k.c together with the default Mega Drive machine and VDP sources. m68000 is therefore recorded alongside the existing Z80 guest CPU; it is not inferred merely from the platform name.
- https://github.com/JoppyFurr/Snepulator/blob/main/build.sh
- https://github.com/JoppyFurr/Snepulator/commit/2a6523d20e1b
- https://github.com/JoppyFurr/Snepulator/commit/47eff3cfe274bd5b88d14a2f8ddf4f6cdaaae655

### Target CPU (reviewed)

build.sh explicitly includes a Windows x86_64-w64-mingw32 cross-build branch. Record x86-64 as that documented build target only; README-supported Linux has no specified CPU. Windows is not promoted into the supported-platform list solely from that recipe.
- https://github.com/JoppyFurr/Snepulator/blob/main/README.md
- https://github.com/JoppyFurr/Snepulator/blob/main/build.sh
- https://github.com/JoppyFurr/Snepulator/blob/main/source/sg-1000.c
- https://github.com/JoppyFurr/Snepulator/commit/47eff3cfe274bd5b88d14a2f8ddf4f6cdaaae655

### Build (reviewed)

The reviewed Mega Drive diff recognizes the SEGA header, normalizes and reports the game title, decodes SRAM location/size, gates overlapping SRAM through the control register, loads saves during initialization and writes them during synchronization. Limitations: The tracker did not build Snepulator, load a ROM, or verify save interoperability and corruption handling.
- https://github.com/JoppyFurr/Snepulator/commit/47eff3cfe274bd5b88d14a2f8ddf4f6cdaaae655

### Runtime profiles (no-evidence-found)

SDL2/OpenGL and zlib are software dependencies. No supported Linux hardware minimum was found; the explicit Windows cross-compiler architecture is not a minimum CPU profile.
- https://github.com/JoppyFurr/Snepulator/blob/main/README.md
- https://github.com/JoppyFurr/Snepulator/blob/main/build.sh
- https://github.com/JoppyFurr/Snepulator/commit/47eff3cfe274bd5b88d14a2f8ddf4f6cdaaae655

### AI (no-evidence-found)

No explicit AI-development evidence observed in the README, tree and selected source/build/license files reviewed. This is not evidence of no AI use.
- https://github.com/JoppyFurr/Snepulator/blob/main/README.md
- https://github.com/JoppyFurr/Snepulator/blob/main/source/sg-1000.c
- https://github.com/JoppyFurr/Snepulator/blob/main/build.sh
- https://github.com/JoppyFurr/Snepulator/commit/47eff3cfe274bd5b88d14a2f8ddf4f6cdaaae655

### Relationships (reviewed)

Canonical root is absent from the 1,380-project baseline and prior-decision ledger; GitHub metadata records a non-fork. Generic machine emulator developed since 2017 according to README. MIT project license coexists with separate bundled library licenses; user ROMs are required. Under-development Mega Drive support is excluded from confirmed machine labels. Related/dependency graphs were not exhaustively traversed, so source review stays partial.
- https://github.com/JoppyFurr/Snepulator
- https://github.com/JoppyFurr/Snepulator/blob/main/README.md
- https://github.com/JoppyFurr/Snepulator/blob/main/LICENSE.txt
- https://github.com/JoppyFurr/Snepulator/blob/main/source/sg-1000.c
- https://github.com/JoppyFurr/Snepulator/commit/47eff3cfe274bd5b88d14a2f8ddf4f6cdaaae655

## new-super-mario-bros-ds-decomp

Project ID: new-super-mario-bros-ds-decomp · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "new-super-mario-bros-ds-decomp",
  "last_checked": "2026-10-28",
  "status": "Early Nintendo DS matching project that still does not build a full ROM; current Object317 recovery adds resource loading, selection state, input handling and an actor profile but retains an incomplete render path.",
  "techniques": [
    "actor state-machine reconstruction"
  ]
}
```

Expected existing project SHA256: b4076303adcd4459f9bbb415f149542da976427a22b8a87b53ecb3a4b15c3b51

### Identity (reviewed)

Early matching project with actor/base sources. README explicitly says it cannot compile to a full ROM yet; do not imply a playable reconstruction.
- https://github.com/NSMB-Decomp/nsmb
- https://github.com/NSMB-Decomp/nsmb/blob/9c7c0b341ae87f860df090e1e35d720f06c70bfa/src/Bases/Actor.cpp
- https://github.com/NSMB-Decomp/nsmb/blob/9c7c0b341ae87f860df090e1e35d720f06c70bfa/readme.md
- https://github.com/NSMB-Decomp/nsmb/commit/b967b56a2a6ff115f45195292e57c298d277bdd8

### Classification (reviewed)

Classified as game / decompilation based on the inspected primary source; limitations in identity are retained.
- https://github.com/NSMB-Decomp/nsmb
- https://github.com/NSMB-Decomp/nsmb/blob/9c7c0b341ae87f860df090e1e35d720f06c70bfa/src/Bases/Actor.cpp
- https://github.com/NSMB-Decomp/nsmb/blob/9c7c0b341ae87f860df090e1e35d720f06c70bfa/readme.md
- https://github.com/NSMB-Decomp/nsmb/commit/b967b56a2a6ff115f45195292e57c298d277bdd8

### Source CPU (reviewed)

Inspected platform and source identify ARM9.
- https://github.com/NSMB-Decomp/nsmb
- https://github.com/NSMB-Decomp/nsmb/blob/9c7c0b341ae87f860df090e1e35d720f06c70bfa/src/Bases/Actor.cpp
- https://github.com/NSMB-Decomp/nsmb/blob/9c7c0b341ae87f860df090e1e35d720f06c70bfa/readme.md
- https://github.com/NSMB-Decomp/nsmb/commit/b967b56a2a6ff115f45195292e57c298d277bdd8

### Target CPU (reviewed)

Output architecture: ARM9.
- https://github.com/NSMB-Decomp/nsmb
- https://github.com/NSMB-Decomp/nsmb/blob/9c7c0b341ae87f860df090e1e35d720f06c70bfa/src/Bases/Actor.cpp
- https://github.com/NSMB-Decomp/nsmb/blob/9c7c0b341ae87f860df090e1e35d720f06c70bfa/readme.md
- https://github.com/NSMB-Decomp/nsmb/commit/b967b56a2a6ff115f45195292e57c298d277bdd8

### Build (reviewed)

The pinned Object317 source now loads eight model resources, initializes transform and selection state, handles left/right/A input through member-function state tables, and defines the actor profile. Rendering still contains a commented matrix operation and the project README's full-ROM limitation remains in force. Limitations: The tracker did not build or execute the actor; this bounded recovery does not establish a compilable or playable full ROM.
- https://github.com/NSMB-Decomp/nsmb/commit/b967b56a2a6ff115f45195292e57c298d277bdd8

### Runtime profiles (no-evidence-found)

No independently verified minimum runnable hardware profile established.
- https://github.com/NSMB-Decomp/nsmb
- https://github.com/NSMB-Decomp/nsmb/blob/9c7c0b341ae87f860df090e1e35d720f06c70bfa/src/Bases/Actor.cpp
- https://github.com/NSMB-Decomp/nsmb/blob/9c7c0b341ae87f860df090e1e35d720f06c70bfa/readme.md
- https://github.com/NSMB-Decomp/nsmb/commit/b967b56a2a6ff115f45195292e57c298d277bdd8

### AI (no-evidence-found)

No explicit AI-use disclosure established in inspected evidence. Agent/configuration presence alone is not proof of use; absence is not non-use.
- https://github.com/NSMB-Decomp/nsmb
- https://github.com/NSMB-Decomp/nsmb/blob/9c7c0b341ae87f860df090e1e35d720f06c70bfa/src/Bases/Actor.cpp
- https://github.com/NSMB-Decomp/nsmb/blob/9c7c0b341ae87f860df090e1e35d720f06c70bfa/readme.md
- https://github.com/NSMB-Decomp/nsmb/commit/b967b56a2a6ff115f45195292e57c298d277bdd8

### Relationships (reviewed)

Current catalogue URL, title and known alias screening performed; repository not a GitHub fork.
- https://github.com/NSMB-Decomp/nsmb
- https://github.com/NSMB-Decomp/nsmb/blob/9c7c0b341ae87f860df090e1e35d720f06c70bfa/src/Bases/Actor.cpp
- https://github.com/NSMB-Decomp/nsmb/blob/9c7c0b341ae87f860df090e1e35d720f06c70bfa/readme.md
- https://github.com/NSMB-Decomp/nsmb/commit/b967b56a2a6ff115f45195292e57c298d277bdd8

## caesar0007-nfshs-psx-decomp

Project ID: caesar0007-nfshs-psx-decomp · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "caesar0007-nfshs-psx-decomp",
  "last_checked": "2026-10-28",
  "status": "Active PlayStation matching reconstruction; current work replaces ad-hoc EACPSXZ declarations with canonical library headers while wider source/SYM/SLD recovery remains incomplete.",
  "techniques": [
    "SYM/SLD ownership-contract validation",
    "source-only build gates",
    "whole-image byte comparison",
    "canonical library-header contract restoration"
  ]
}
```

Expected existing project SHA256: aea4ebef59cacae4fdea5367d4f2735bd6581073da907719b917f56a224a16c5

### Identity (reviewed)

Need for Speed High Stakes — PSX matching reconstruction. Repository root and implementation inspected at pinned revisions.
- https://github.com/caesar0007/nfshs-psx-decomp/blob/fa6a3a2ecc09a90abbcdc241af4e491be0c383b9/README.md
- https://github.com/Caesar0007/NFSHS-PSX-decomp/blob/fa6a3a2ecc09a90abbcdc241af4e491be0c383b9/README.md
- https://github.com/Caesar0007/NFSHS-PSX-decomp/blob/fa6a3a2ecc09a90abbcdc241af4e491be0c383b9/src/aiinit.c
- https://github.com/Caesar0007/NFSHS-PSX-decomp/commit/e811441133ea7118cc834772343e105bd4ff158e
- https://github.com/Caesar0007/NFSHS-PSX-decomp/commit/0ca9a756e603185b9bfa72bc7a9c1a8f595af929

### Classification (reviewed)

Matching and reconstruction tracks coexist. Inspected aiinit.c is INCLUDE_ASM wrappers, not recovered C bodies; README percentages are dated author reports, not a current semantic completeness measure.
- https://github.com/caesar0007/nfshs-psx-decomp/blob/fa6a3a2ecc09a90abbcdc241af4e491be0c383b9/README.md
- https://github.com/Caesar0007/NFSHS-PSX-decomp/blob/fa6a3a2ecc09a90abbcdc241af4e491be0c383b9/README.md
- https://github.com/Caesar0007/NFSHS-PSX-decomp/blob/fa6a3a2ecc09a90abbcdc241af4e491be0c383b9/src/aiinit.c
- https://github.com/Caesar0007/NFSHS-PSX-decomp/commit/e811441133ea7118cc834772343e105bd4ff158e
- https://github.com/Caesar0007/NFSHS-PSX-decomp/commit/0ca9a756e603185b9bfa72bc7a9c1a8f595af929

### Source CPU (reviewed)

Architecture context: mips. Source and target roles are recorded separately.
- https://github.com/caesar0007/nfshs-psx-decomp/blob/fa6a3a2ecc09a90abbcdc241af4e491be0c383b9/README.md
- https://github.com/Caesar0007/NFSHS-PSX-decomp/blob/fa6a3a2ecc09a90abbcdc241af4e491be0c383b9/README.md
- https://github.com/Caesar0007/NFSHS-PSX-decomp/blob/fa6a3a2ecc09a90abbcdc241af4e491be0c383b9/src/aiinit.c
- https://github.com/Caesar0007/NFSHS-PSX-decomp/commit/e811441133ea7118cc834772343e105bd4ff158e
- https://github.com/Caesar0007/NFSHS-PSX-decomp/commit/0ca9a756e603185b9bfa72bc7a9c1a8f595af929

### Target CPU (reviewed)

Explicit output/execution architecture: mips.
- https://github.com/caesar0007/nfshs-psx-decomp/blob/fa6a3a2ecc09a90abbcdc241af4e491be0c383b9/README.md
- https://github.com/Caesar0007/NFSHS-PSX-decomp/blob/fa6a3a2ecc09a90abbcdc241af4e491be0c383b9/README.md
- https://github.com/Caesar0007/NFSHS-PSX-decomp/blob/fa6a3a2ecc09a90abbcdc241af4e491be0c383b9/src/aiinit.c
- https://github.com/Caesar0007/NFSHS-PSX-decomp/commit/e811441133ea7118cc834772343e105bd4ff158e
- https://github.com/Caesar0007/NFSHS-PSX-decomp/commit/0ca9a756e603185b9bfa72bc7a9c1a8f595af929

### Build (needs-research)

The reviewed diff migrates game and track-stream code from hand-written extern declarations to canonical EACPSXZ headers for memory, file, task, fixed-math, text and exit APIs; stripped-reference stubs receive explicit signatures and arguments. Limitations: This is a source-contract cleanup, not a new whole-project exactness result. The tracker did not compile, test, run or byte-compare it. Next check: Follow the remaining source/SYM/SLD contracts and only promote whole-project byte exactness after upstream closes the explicit gaps.
- https://github.com/Caesar0007/NFSHS-PSX-decomp/commit/0ca9a756e603185b9bfa72bc7a9c1a8f595af929

### Runtime profiles (no-evidence-found)

The reviewed source-contract change establishes no minimum PlayStation model, host CPU, RAM, OS or emulator requirement. Repository licensing terms are not a runtime profile.
- https://github.com/Caesar0007/NFSHS-PSX-decomp/commit/0ca9a756e603185b9bfa72bc7a9c1a8f595af929

### AI (reviewed)

An inspected reconstruction commit explicitly credits Claude Opus 5.5, supporting the project-level Claude attribution; the latest contract-restoration commit itself contains no co-author trailer.
- https://github.com/Caesar0007/NFSHS-PSX-decomp/commit/b3a6e2d4b7dbe4cab0fbff28819566187651780b
- https://github.com/Caesar0007/NFSHS-PSX-decomp/commit/e811441133ea7118cc834772343e105bd4ff158e
- https://github.com/Caesar0007/NFSHS-PSX-decomp/commit/0ca9a756e603185b9bfa72bc7a9c1a8f595af929

### Relationships (reviewed)

README links XProger as separately authorized port; do not conflate matching project and port.
- https://github.com/caesar0007/nfshs-psx-decomp/blob/fa6a3a2ecc09a90abbcdc241af4e491be0c383b9/README.md
- https://github.com/Caesar0007/NFSHS-PSX-decomp/blob/fa6a3a2ecc09a90abbcdc241af4e491be0c383b9/README.md
- https://github.com/Caesar0007/NFSHS-PSX-decomp/blob/fa6a3a2ecc09a90abbcdc241af4e491be0c383b9/src/aiinit.c
- https://github.com/Caesar0007/NFSHS-PSX-decomp/commit/e811441133ea7118cc834772343e105bd4ff158e
- https://github.com/Caesar0007/NFSHS-PSX-decomp/commit/0ca9a756e603185b9bfa72bc7a9c1a8f595af929

## Source ids

```json
[
  "wide-20261018q-smalltalk80-by-the-book-pharo-vm",
  "wide-20261018d-snow-classic-mac-emulator",
  "github-n0zom1z0-th04",
  "bigbatch-rester159-blacktiger-md",
  "pass23-virtua-tennis-dreamcast-analysis",
  "pass32-zombie-revenge-dc-decompilation",
  "github-shdecompilations-silent-hill-decomp",
  "github-retro-foundry-alien-breed-hd",
  "github-joppyfurr-snepulator",
  "pass30-new-super-mario-bros-ds-decomp",
  "github-caesar0007-nfshs-psx-decomp"
]
```

## Research event notes

The CPU audit queue returned zero unresolved source or target CPU areas before selection, so no architecture or minimum-hardware fields were invented to satisfy a quota. Primary commit diffs and pinned files were inspected. The tracker did not compile, execute or independently benchmark the reviewed software; upstream build, equivalence and runtime claims remain attributed.
