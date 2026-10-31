# Upstream analysis, runtime and collection maintenance

Review ten material upstream changes across reconstruction, emulation, runtime tooling and multi-project retro collections.

Date: 2026-10-31 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- firestaff-dungeon-master-engine / Build (needs-research): The tracker did not repeat the tests. Launcher admission and menu startup do not establish complete native display, input or gameplay. Next check: Continue bounded native runtime and Nexus gates without converting startup coverage into a complete-playability claim.
- m68k-reversing-toolkit-rmtew / Build (needs-research): The tracker did not regenerate the output. The fixtures are post-filter continuations and do not certify contact geometry, global alias safety, unique release or later reuse validity. Next check: Follow the connected contact-eligibility and special-player response consumers while preserving the stated lifetime and scanout boundaries.
- m68k-reversing-toolkit-rmtew / Runtime profiles (needs-research): The reviewed analysis run states no minimum Amiga CPU, RAM, chipset or ROM requirement. Next check: Add a runtime profile only after primary documentation or qualified hardware/emulator testing states a concrete minimum.
- m68k-reversing-toolkit-rmtew / Relationships (needs-research): The restoration remains within Starglider 2 and does not resolve the wider credited-source or predecessor graph. Next check: Revisit project relationships after the bounded restoration stabilizes.
- zapple-ii-bpm-prodos-softcard-environment / Build (reviewed): The tracker did not build or run the system or repeat a remote-login session.
- zapple-ii-bpm-prodos-softcard-environment / Runtime profiles (no-evidence-found): The reviewed commits provide no new minimum Apple II model, SoftCard, RAM, W5100 firmware or network profile.
- zapple-ii-bpm-prodos-softcard-environment / AI (no-evidence-found): The reviewed full commit messages and implementation diff contain no explicit development-AI attribution; absence does not establish non-use.
- moria8-6502-multiplatform / Source CPU (no-evidence-found): The documented source lineages are VMS Pascal and C Umoria; the reviewed storage commits do not establish an original executable ISA, so source_cpu remains empty.
- moria8-6502-multiplatform / Build (reviewed): The tracker did not build the ports, run VICE or reproduce the disk faults.
- ase-atari-system-emulator / Build (reviewed): The tracker did not build or run ASE, validate RTC edge cases or test older snapshot files.
- ase-atari-system-emulator / Runtime profiles (no-evidence-found): The change documents device timing behavior but no verified host CPU/RAM minimum or newly qualified guest machine configuration.
- ase-atari-system-emulator / AI (no-evidence-found): The reviewed full commit message and diff contain no explicit AI-contribution attribution; usage remains unknown rather than false.
- koncepcja-cpc-emulator-debugger / Build (reviewed): The tracker did not build the emulator or run the cross-platform frame-ring tests.
- koncepcja-cpc-emulator-debugger / Runtime profiles (no-evidence-found): Cross-platform CI coverage is evidenced, but no minimum host CPU, RAM or OS version is stated.
- spice86-real-mode-pc-reverse-engineering-emulator / Build (reviewed): The tracker did not build Spice86 or run the analyzer fixtures. The commit explicitly says behavior can remain correct while recovered method structure is imperfect.
- spice86-real-mode-pc-reverse-engineering-emulator / Runtime profiles (no-evidence-found): The reviewed analyzer changes state no minimum host CPU, RAM or operating-system version.
- regenerator2000-commodore-disassembler / Build (reviewed): The tracker did not run cargo tests, VICE or the TUI.
- pom2games-native-apple-ii-collection / Source CPU (no-evidence-found): The reviewed changes concern native target memory maps and do not establish a distinct original binary CPU for either title; source_cpu remains empty rather than inferred from Apple II output.
- pom2games-native-apple-ii-collection / Build (reviewed): The tracker did not build the disk images, run the tests or verify the measured free-space figures.
- amy-studio-colecovision-development-environment / Build (reviewed): The tracker did not compile or run the ten example ROMs on GearColeco or physical hardware.
- amy-studio-colecovision-development-environment / Runtime profiles (no-evidence-found): The named ColecoVision memory profile is a build profile, but the reviewed commits state no new verified minimum console RAM/peripheral configuration or host CPU/RAM floor.

## firestaff-dungeon-master-engine

Project ID: firestaff-dungeon-master-engine · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "firestaff-dungeon-master-engine",
  "last_activity": "2026-10-31",
  "last_checked": "2026-10-31",
  "status": "Firestaff now binds authenticated Atari ST Chaos Strikes Back archive members to the same original image and covers Atari ST 1.1 menu startup; broader native playability and Nexus completion remain open.",
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
    "startup source-frame tracing",
    "authenticated SNES media classification",
    "bounded H03 ROMDUNGEON decoding",
    "same-archive authenticated file pairing",
    "Atari ST menu-route regression"
  ]
}
```

Expected existing project SHA256: d87d7ecd8a33ee9082ad0ef0942f8be66d2dc62786e81e4d69b1d072dcdcb7cd

### Identity (reviewed)

Firestaff remains one clean-room Dungeon Master-family engine and evidence framework; the Atari ST archive and menu routes are variants inside the same project.
- https://github.com/yeager/firestaff/commit/f1065c673fca0c8586f58fe5883c7abb9011aaac
- https://github.com/yeager/firestaff/commit/aa3732f4a30aac7a0b320c6c9b16adaa795849fc

### Classification (reviewed)

The changes are authenticated-media reconstruction and regression evidence, not proof of a complete native Atari ST port.
- https://github.com/yeager/firestaff/commit/f1065c673fca0c8586f58fe5883c7abb9011aaac

### Source CPU (reviewed)

Existing x86, m68k, HuC6280, SH-2 and 65C816 source-family decisions remain; this Atari ST path introduces no new original CPU family.
- https://github.com/yeager/firestaff/blob/bcdd94bd06d4fe442e2429870111419e0ca57bae/README.md
- https://github.com/yeager/firestaff/commit/f1065c673fca0c8586f58fe5883c7abb9011aaac

### Target CPU (reviewed)

Existing x86-64 and arm64 modern outputs remain; archive admission and Atari menu testing do not establish a new output architecture.
- https://github.com/yeager/firestaff/releases/tag/v3.0.416
- https://github.com/yeager/firestaff/commit/f1065c673fca0c8586f58fe5883c7abb9011aaac

### Build (needs-research)

Upstream added same-image GRAPHICS.DAT/DUNGEON.DAT digest binding for Atari ST CSB and expanded real-media route coverage, including Atari ST 1.1 menu startup. Limitations: The tracker did not repeat the tests. Launcher admission and menu startup do not establish complete native display, input or gameplay. Next check: Continue bounded native runtime and Nexus gates without converting startup coverage into a complete-playability claim.
- https://github.com/yeager/firestaff/commit/f1065c673fca0c8586f58fe5883c7abb9011aaac
- https://github.com/yeager/firestaff/commit/aa3732f4a30aac7a0b320c6c9b16adaa795849fc

### Runtime profiles (reviewed)

Existing measured Mac mini M4 and QEMU-hosted Linux x86-64 profiles remain; the reviewed Atari changes state no additional minimum CPU, RAM or OS floor.
- https://github.com/yeager/firestaff/releases/tag/v3.0.416
- https://github.com/yeager/firestaff/commit/f1065c673fca0c8586f58fe5883c7abb9011aaac

### AI (reviewed)

Existing explicit Claude commit attribution remains scoped to evidenced contributions; no broader inference is made from these commits.
- https://github.com/yeager/firestaff/commit/bcdd94bd06d4fe442e2429870111419e0ca57bae

### Relationships (reviewed)

The additional Atari editions and archive routes remain Firestaff variants, not newly titled nested projects.
- https://github.com/yeager/firestaff/commit/f1065c673fca0c8586f58fe5883c7abb9011aaac

## m68k-reversing-toolkit-rmtew

Project ID: m68k-reversing-toolkit-rmtew · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "m68k-reversing-toolkit-rmtew",
  "last_activity": "2026-10-31",
  "last_checked": "2026-10-31",
  "status": "Starglider 2 remains byte-exact across 412,736 bytes while connected homing, HUD, collision-retirement and world-record recycling continuations gain original-CPU fixtures; global alias safety and complete gameplay remain unproved.",
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
    "orphan layout-element rejection",
    "producer-phase launch-state contract recovery",
    "guarded actor-field ownership",
    "disk/media helper role recovery",
    "shared disk/audio service-state modeling",
    "loop-wide sparse-memory preservation",
    "canonical pointer-producer validation",
    "operand-role projection correction",
    "original-CPU collision-response fixtures",
    "record-pool retirement reconstruction",
    "homing and HUD continuation recovery"
  ]
}
```

Expected existing project SHA256: 18023f279ecd5ff8846d5f695f8a4d10da8390a066f200489b339fb8e03639dd

### Identity (reviewed)

M68k Reversing Toolkit remains the generated Amiga analysis and reconstruction framework; this pass advances its existing Starglider 2 target.
- https://github.com/rmtew/amiga-reversing/commit/5ba1042639e3f736d9cca7531f2360a80bfbac18

### Classification (reviewed)

The new collision, retirement, homing and HUD continuations are bounded semantic restoration with explicit non-certification of global lifetime, DMA, scanout and gameplay behavior.
- https://github.com/rmtew/amiga-reversing/commit/5ba1042639e3f736d9cca7531f2360a80bfbac18

### Source CPU (reviewed)

The tracked Starglider 2 input remains Motorola 68000 code, with the reviewed batch explicitly covered by original-CPU cases.
- https://github.com/rmtew/amiga-reversing/blob/9c8cdbfd2a4fca323e3fcc37031a32f7d4c72780/README.md
- https://github.com/rmtew/amiga-reversing/commit/5ba1042639e3f736d9cca7531f2360a80bfbac18

### Target CPU (reviewed)

The output remains native Motorola 68000 assembly verified upstream through exact C/vasm and standalone rebuild paths.
- https://github.com/rmtew/amiga-reversing/commit/5ba1042639e3f736d9cca7531f2360a80bfbac18

### Build (needs-research)

Upstream reports 175 original-CPU collision/recycling cases, exact C/vasm output and clean standalone output across the unchanged 412,736-byte target. Limitations: The tracker did not regenerate the output. The fixtures are post-filter continuations and do not certify contact geometry, global alias safety, unique release or later reuse validity. Next check: Follow the connected contact-eligibility and special-player response consumers while preserving the stated lifetime and scanout boundaries.
- https://github.com/rmtew/amiga-reversing/commit/5ba1042639e3f736d9cca7531f2360a80bfbac18

### Runtime profiles (needs-research)

The reviewed analysis run states no minimum Amiga CPU, RAM, chipset or ROM requirement. Next check: Add a runtime profile only after primary documentation or qualified hardware/emulator testing states a concrete minimum.
- https://github.com/rmtew/amiga-reversing/commit/5ba1042639e3f736d9cca7531f2360a80bfbac18

### AI (reviewed)

Existing explicit Claude contribution evidence remains valid and scoped to tracked commits.
- https://github.com/rmtew/amiga-reversing/commit/0806d08b49d8d7f1aa6826c40385317bbb81154c

### Relationships (needs-research)

The restoration remains within Starglider 2 and does not resolve the wider credited-source or predecessor graph. Next check: Revisit project relationships after the bounded restoration stabilizes.
- https://github.com/rmtew/amiga-reversing/blob/9c8cdbfd2a4fca323e3fcc37031a32f7d4c72780/README.md

## zapple-ii-bpm-prodos-softcard-environment

Project ID: zapple-ii-bpm-prodos-softcard-environment · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "zapple-ii-bpm-prodos-softcard-environment",
  "last_activity": "2026-10-31",
  "last_checked": "2026-10-31",
  "status": "Zapple-II / BP/M now supports a configurable SoftCard slot, remappable O:/P: drives and a kernel-owned multiuser Telnet service; execution remains upstream-reported.",
  "techniques": [
    "terminal personality caching",
    "CP/M file-semantics regression",
    "virtualized directory search",
    "bank-safe W5100 socket API integration",
    "CP/M Telnet and WGET client integration",
    "CP/M-compatible remote-login service",
    "Telnet option negotiation",
    "ProDOS boot configuration staging",
    "multiuser Telnet service"
  ]
}
```

Expected existing project SHA256: a25092555b087d52596384c1c1227c806ccb8ac842cf8815cc606cb7438b6cf0

### Identity (reviewed)

Configurable drives, SoftCard placement and NETCCP remain parts of the same Apple IIe/SoftCard Zapple-II and BP/M environment.
- https://github.com/bobbimanners/Zapple-II/commit/9bbcb2c550f6441f55d4dc3374aa1dcbfc07d50c
- https://github.com/bobbimanners/Zapple-II/commit/8ff106bb30072b3d805699eebfc1caf89706b558

### Classification (reviewed)

This is original CP/M-compatible system and networking development for legacy Apple II/SoftCard hardware, not reverse-engineered game code.
- https://github.com/bobbimanners/Zapple-II/commit/9bbcb2c550f6441f55d4dc3374aa1dcbfc07d50c

### Source CPU (reviewed)

The inspected boot driver and BP/M implementation continue to establish 6502 and Z80 source architectures; this is not a minimum-machine inference.
- https://github.com/bobbimanners/Zapple-II/commit/9bbcb2c550f6441f55d4dc3374aa1dcbfc07d50c

### Target CPU (reviewed)

The staged 6502 driver and Z80 kernel remain the evidenced output architectures; configuration flexibility adds no new target CPU.
- https://github.com/bobbimanners/Zapple-II/commit/9bbcb2c550f6441f55d4dc3374aa1dcbfc07d50c

### Build (reviewed)

Upstream stages ZAPPLE2.CNF below the Z80 load, copies O:/P: mounts and DNS into the kernel, separates SoftCard slot configuration from Uthernet, and registers a persistent NETCCP listener. Limitations: The tracker did not build or run the system or repeat a remote-login session.
- https://github.com/bobbimanners/Zapple-II/commit/9bbcb2c550f6441f55d4dc3374aa1dcbfc07d50c
- https://github.com/bobbimanners/Zapple-II/commit/8ff106bb30072b3d805699eebfc1caf89706b558

### Runtime profiles (no-evidence-found)

The reviewed commits provide no new minimum Apple II model, SoftCard, RAM, W5100 firmware or network profile.
- https://github.com/bobbimanners/Zapple-II/commit/9bbcb2c550f6441f55d4dc3374aa1dcbfc07d50c

### AI (no-evidence-found)

The reviewed full commit messages and implementation diff contain no explicit development-AI attribution; absence does not establish non-use.
- https://github.com/bobbimanners/Zapple-II/commit/9bbcb2c550f6441f55d4dc3374aa1dcbfc07d50c
- https://github.com/bobbimanners/Zapple-II/commit/8ff106bb30072b3d805699eebfc1caf89706b558

### Relationships (reviewed)

The NETCCP client, resident service and drive configuration are components of Zapple-II/BP/M rather than independently titled repository projects.
- https://github.com/bobbimanners/Zapple-II/commit/8ff106bb30072b3d805699eebfc1caf89706b558

## moria8-6502-multiplatform

Project ID: moria8-6502-multiplatform · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "moria8-6502-multiplatform",
  "last_activity": "2026-10-31",
  "last_checked": "2026-10-31",
  "status": "Moria8 adds disk save/load playtests, retry paths and deterministic failed-run capture across its 6502/65C02 ports; released/platform status is unchanged and tracker-side execution was not performed.",
  "techniques": [
    "five-platform HAL boundary validation",
    "Commander X16 memory-contract testing",
    "x16emu runtime scenarios",
    "VICE binary-monitor AI playtesting",
    "isolated multi-platform emulator regression",
    "deterministic finding replay",
    "disk save/load scenario replay",
    "drive-status retry validation"
  ]
}
```

Expected existing project SHA256: d220a9cfc44f8b09edac9710005e0ac5c7b80c79807a3ff2e51d75696b94ccb6

### Identity (reviewed)

The C64, C128, Plus/4, Apple II, Commander X16 and other platform paths remain one Moria8 reimplementation.
- https://github.com/dcgibbons/moria8/commit/297ae351fa8af5a6ea33bfcf6787b3bb3857104f
- https://github.com/dcgibbons/moria8/commit/d654ee133b53716b7291b10d25ce5d19f6f3b3ab

### Classification (reviewed)

Moria8 remains a native platform-specific assembly reimplementation from credited VMS Moria and Umoria source lineages, not a reverse-engineered binary port.
- https://github.com/dcgibbons/moria8

### Source CPU (no-evidence-found)

The documented source lineages are VMS Pascal and C Umoria; the reviewed storage commits do not establish an original executable ISA, so source_cpu remains empty.
- https://github.com/dcgibbons/moria8
- https://github.com/dcgibbons/moria8/commit/d654ee133b53716b7291b10d25ce5d19f6f3b3ab

### Target CPU (reviewed)

Existing 6502 and 65C02 outputs remain evidenced; disk retry and REU-init changes add no new output CPU.
- https://github.com/dcgibbons/moria8/commit/297ae351fa8af5a6ea33bfcf6787b3bb3857104f
- https://github.com/dcgibbons/moria8/commit/d654ee133b53716b7291b10d25ce5d19f6f3b3ab

### Build (reviewed)

Upstream adds save/load scenario playtests, retains failed-run inputs and VICE seeds, retries failed asset loads, and retries Plus/4 command-channel reads up to three times after JiffyDOS read timeouts. Limitations: The tracker did not build the ports, run VICE or reproduce the disk faults.
- https://github.com/dcgibbons/moria8/commit/d654ee133b53716b7291b10d25ce5d19f6f3b3ab
- https://github.com/dcgibbons/moria8/commit/a7421bb2b6b5fcfec8a8c4ba912df7127ee1914e

### Runtime profiles (reviewed)

The existing Apple II 128 KiB/80-column/ProDOS profile remains sourced. Emulator harness settings and JiffyDOS retry behavior are test/runtime behavior, not new minimum hardware evidence.
- https://github.com/dcgibbons/moria8
- https://github.com/dcgibbons/moria8/commit/d654ee133b53716b7291b10d25ce5d19f6f3b3ab

### AI (reviewed)

The repository's operational AI playtester remains documented; the reviewed storage commits do not imply that every change was model-authored.
- https://github.com/dcgibbons/moria8
- https://github.com/dcgibbons/moria8/commit/a7421bb2b6b5fcfec8a8c4ba912df7127ee1914e

### Relationships (reviewed)

The platform storage implementations remain one Moria8 project distinct from its credited VMS Moria/Umoria ancestors.
- https://github.com/dcgibbons/moria8

## ase-atari-system-emulator

Project ID: ase-atari-system-emulator · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "ase-atari-system-emulator",
  "last_activity": "2026-10-31",
  "last_checked": "2026-10-31",
  "status": "ASE now emulates the Mega ST RP5C15 and IKBD clocks with emulated-time advancement and snapshot state; Linux remains described upstream as untested.",
  "techniques": [
    "IKBD input emulation",
    "hard-drive game-library integration",
    "RP5C15 real-time-clock emulation",
    "snapshot-deterministic clock state"
  ]
}
```

Expected existing project SHA256: 5ced6a7e40b03fa17f7c23b3531d07c92f4decbbbecc20228d071b8152925165

### Identity (reviewed)

RP5C15 and IKBD clock support extend the same generic Atari ST-family emulator.
- https://github.com/thebitculture/ase/commit/5d12334eb5b3a6aa3ee9725848ac73c911b6a684

### Classification (reviewed)

ASE remains a generic ST/Mega ST/STE emulator using Moira, not a game-specific reconstruction.
- https://github.com/thebitculture/ase
- https://github.com/thebitculture/ase/commit/5d12334eb5b3a6aa3ee9725848ac73c911b6a684

### Source CPU (reviewed)

The emulated guest remains Motorola 68000; clock-device emulation adds no source CPU family.
- https://github.com/thebitculture/ase
- https://github.com/thebitculture/ase/commit/5d12334eb5b3a6aa3ee9725848ac73c911b6a684

### Target CPU (reviewed)

Existing x86-64 and arm64 host outputs remain; the reviewed device work adds no host architecture.
- https://github.com/thebitculture/ase

### Build (reviewed)

Upstream advances both clocks by emulated cycles, initializes them from host local time only at the external session boundary, and appends clock state to backward-compatible snapshots. Limitations: The tracker did not build or run ASE, validate RTC edge cases or test older snapshot files.
- https://github.com/thebitculture/ase/commit/5d12334eb5b3a6aa3ee9725848ac73c911b6a684

### Runtime profiles (no-evidence-found)

The change documents device timing behavior but no verified host CPU/RAM minimum or newly qualified guest machine configuration.
- https://github.com/thebitculture/ase/commit/5d12334eb5b3a6aa3ee9725848ac73c911b6a684

### AI (no-evidence-found)

The reviewed full commit message and diff contain no explicit AI-contribution attribution; usage remains unknown rather than false.
- https://github.com/thebitculture/ase/commit/5d12334eb5b3a6aa3ee9725848ac73c911b6a684

### Relationships (reviewed)

The RP5C15 and IKBD implementations are emulator subsystems; Moira and Munt remain dependencies rather than newly split projects.
- https://github.com/thebitculture/ase
- https://github.com/thebitculture/ase/commit/5d12334eb5b3a6aa3ee9725848ac73c911b6a684

## koncepcja-cpc-emulator-debugger

Project ID: koncepcja-cpc-emulator-debugger · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "koncepcja-cpc-emulator-debugger",
  "last_activity": "2026-10-31",
  "last_checked": "2026-10-31",
  "status": "konCePCja's KCPC debugger now publishes every frame through a documented shared-memory ring with sequence-numbered events and an independent fb_dump reader tested across Linux, macOS and Windows CI.",
  "techniques": [
    "sub-cycle pin-level hardware simulation",
    "flux-image decoding",
    "deterministic record/replay",
    "headless TCP debugger automation",
    "integrated Z80 assembly and disassembly",
    "binary debugger protocol",
    "controller leases and event subscriptions",
    "IDE and disk-image writeback regression",
    "lease-bound atomic debugger mutation",
    "frame-boundary IPC writes",
    "shared-memory frame-ring protocol",
    "independent frame-reader conformance testing"
  ]
}
```

Expected existing project SHA256: 420a94be643caf7e0a62799da052ce60fa1b3a4abf0a35db4795b1fe43b4b21a

### Identity (reviewed)

The frame ring and fb_dump tool extend konCePCja's existing KCPC emulator/debugger interface.
- https://github.com/ikari-pl/konCePCja/commit/0ccb93bf3a2acee3bc84c0863ab3fc7eea45cff7

### Classification (reviewed)

This remains a CPC/Plus emulator and debugger; the standalone frame reader is a directly related tool within the same repository.
- https://github.com/ikari-pl/konCePCja/commit/0ccb93bf3a2acee3bc84c0863ab3fc7eea45cff7

### Source CPU (reviewed)

The emulated guest architecture remains Z80; frame transport adds no source CPU.
- https://github.com/ikari-pl/konCePCja

### Target CPU (not-applicable)

The emulator/debugger does not emit a reconstructed subject binary with a fixed output CPU.
- https://github.com/ikari-pl/konCePCja/commit/0ccb93bf3a2acee3bc84c0863ab3fc7eea45cff7

### Build (reviewed)

FB_INFO names the ring, EVT_FRAME carries its sequence, fb_dump reads only the published protocol, and integrated tests require the text IPC, Python reader and C reader to agree on a paused firmware frame and CRC32 across Linux, macOS and MSVC jobs. Limitations: The tracker did not build the emulator or run the cross-platform frame-ring tests.
- https://github.com/ikari-pl/konCePCja/commit/0ccb93bf3a2acee3bc84c0863ab3fc7eea45cff7

### Runtime profiles (no-evidence-found)

Cross-platform CI coverage is evidenced, but no minimum host CPU, RAM or OS version is stated.
- https://github.com/ikari-pl/konCePCja/commit/0ccb93bf3a2acee3bc84c0863ab3fc7eea45cff7

### AI (reviewed)

Existing explicit Claude Opus co-author evidence remains scoped to evidenced commits; no broader attribution is inferred.
- https://github.com/ikari-pl/konCePCja

### Relationships (reviewed)

fb_dump is a protocol-conformance utility delivered with konCePCja, not an independently promoted project; vendored components remain dependencies.
- https://github.com/ikari-pl/konCePCja/commit/0ccb93bf3a2acee3bc84c0863ab3fc7eea45cff7

## spice86-real-mode-pc-reverse-engineering-emulator

Project ID: spice86-real-mode-pc-reverse-engineering-emulator · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "spice86-real-mode-pc-reverse-engineering-emulator",
  "last_activity": "2026-10-31",
  "last_checked": "2026-10-31",
  "status": "Spice86 now distinguishes redirected returns by stack level and carries SSA/data-flow through one IR pipeline, improving generated-method ownership without claiming perfect structure recovery.",
  "techniques": [
    "real-mode execution tracing",
    "control-flow graph reconstruction",
    "C# override generation",
    "stack-level redirected-return classification",
    "SSA data-flow analysis",
    "intermediate-representation lowering"
  ]
}
```

Expected existing project SHA256: 99633ee997b2095e873ea04b97506426764a9b2ff6f788d9e32c6c43eefd0944

### Identity (reviewed)

The redirected-return and SSA work extends the maintained C# Spice86 emulator/reverse-engineering environment.
- https://github.com/OpenRakis/Spice86/commit/f59486b7b8efc062bda0aa55f1d60e45a76845e6
- https://github.com/OpenRakis/Spice86/commit/0a81e014b0e7a484c01be074872ef3ea7a5d9b90

### Classification (reviewed)

Spice86 remains reusable real-mode PC analysis and code-generation tooling rather than a game-specific wrapper.
- https://github.com/OpenRakis/Spice86
- https://github.com/OpenRakis/Spice86/commit/f59486b7b8efc062bda0aa55f1d60e45a76845e6

### Source CPU (reviewed)

The analyzed input architecture remains 16-bit x86 real mode.
- https://github.com/OpenRakis/Spice86

### Target CPU (reviewed)

No fixed native subject CPU is emitted; generated C# and emulated execution remain portable analysis outputs rather than a target-ISA claim.
- https://github.com/OpenRakis/Spice86/commit/f59486b7b8efc062bda0aa55f1d60e45a76845e6

### Build (reviewed)

Upstream adds RedirectedCallContinuation only when a return consumes the matching call frame, carries external-code may-write effects through SSA, and documents the case where same-stack redirection can still pull another routine into the caller partition. Limitations: The tracker did not build Spice86 or run the analyzer fixtures. The commit explicitly says behavior can remain correct while recovered method structure is imperfect.
- https://github.com/OpenRakis/Spice86/commit/f59486b7b8efc062bda0aa55f1d60e45a76845e6
- https://github.com/OpenRakis/Spice86/commit/0a81e014b0e7a484c01be074872ef3ea7a5d9b90

### Runtime profiles (no-evidence-found)

The reviewed analyzer changes state no minimum host CPU, RAM or operating-system version.
- https://github.com/OpenRakis/Spice86/commit/f59486b7b8efc062bda0aa55f1d60e45a76845e6

### AI (reviewed)

Existing full commits with Copilot co-author trailers establish scoped AI contribution; no repository-wide authorship inference is made.
- https://github.com/OpenRakis/Spice86

### Relationships (reviewed)

This remains the maintained C# continuation of kevinferrare/spice86; the new partition edges do not create a separate project.
- https://github.com/OpenRakis/Spice86

## regenerator2000-commodore-disassembler

Project ID: regenerator2000-commodore-disassembler · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "regenerator2000-commodore-disassembler",
  "last_activity": "2026-10-31",
  "last_checked": "2026-10-31",
  "status": "Regenerator 2000 now indexes shared lexical-scope boundaries and performs monotonic block-range rendering while documenting the state and rendering invariants; upstream buildability remains established by the repository, not re-tested here.",
  "techniques": [
    "interactive manual analysis",
    "VICE binary monitor",
    "cycle-accurate unpacking sandbox",
    "assembly round-trip verification",
    "MCP server",
    "cross-reference analysis",
    "lexical-scope indexing",
    "range-indexed disassembly rendering"
  ]
}
```

Expected existing project SHA256: c22232e786f8ae5df9f0dc36831db474eeb68fd080408459fdbd6b51451834b4

### Identity (reviewed)

Scope indexing and BlocksView changes extend the same Regenerator 2000 Commodore reverse-engineering workbench.
- https://github.com/ricardoquesada/regenerator2000/commit/577c6eeb0e272907d9af851a489aab6831e356be

### Classification (reviewed)

This remains interactive 6502 disassembly/debugging and automated analysis tooling, not a reconstructed game.
- https://github.com/ricardoquesada/regenerator2000

### Source CPU (reviewed)

The workbench continues to analyze Commodore 6502-family binaries; UI indexing adds no source CPU family.
- https://github.com/ricardoquesada/regenerator2000

### Target CPU (not-applicable)

The workbench analyzes and exports source but does not define one native reconstructed output CPU.
- https://github.com/ricardoquesada/regenerator2000

### Build (reviewed)

Upstream documents deterministic sparse annotation serialization, O(log S) scope boundaries, monotonic block scans and off-screen scope tracking, following implementation and regression work on the same paths. Limitations: The tracker did not run cargo tests, VICE or the TUI.
- https://github.com/ricardoquesada/regenerator2000/commit/577c6eeb0e272907d9af851a489aab6831e356be
- https://github.com/ricardoquesada/regenerator2000/commit/1929fdb2943ce33901a5d239132af42410bca018

### Runtime profiles (not-applicable)

The reviewed UI/data-structure work does not establish a legacy target's minimum runnable CPU, RAM or ROM profile.
- https://github.com/ricardoquesada/regenerator2000/commit/577c6eeb0e272907d9af851a489aab6831e356be

### AI (reviewed)

Explicit upstream Claude Opus co-author attribution remains independently verified and scoped to the evidenced commit.
- https://github.com/ricardoquesada/regenerator2000/commit/c2fcbcfe8d1a88c3baefde8e566bccf226ec870d

### Relationships (reviewed)

The MCP server, VICE integration and TUI remain components of one workbench rather than separate promoted projects.
- https://github.com/ricardoquesada/regenerator2000

## pom2games-native-apple-ii-collection

Project ID: pom2games-native-apple-ii-collection · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "pom2games-native-apple-ii-collection",
  "last_activity": "2026-10-31",
  "last_checked": "2026-10-31",
  "status": "POM2 Games' native Apple II collection now records WARGALAGA II's 1.9 KiB memory recovery and Robot Space Station's tested DHGR-page code overlays; both remain named subjects within the collection.",
  "subjects": [
    "Arkabreakout",
    "ChromaBreak",
    "MICRO-SOKOBAN",
    "Chess",
    "Maze 3D",
    "Snake",
    "Pinball Construction Set",
    "MCS",
    "Wilderness",
    "WARGALAGA II",
    "Robot Space Station"
  ],
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
    "POM2 real-firmware integration testing",
    "auxiliary-memory code overlays",
    "frame-timed music regression"
  ]
}
```

Expected existing project SHA256: f17767ff15efff24eaa85dacc6eaad3b108738366d228ef20ec0a4f41ba4898b

### Identity (reviewed)

WARGALAGA II and Robot Space Station are separately titled native Apple II works inside the established POM2 Games repository-level collection record.
- https://github.com/habib256/pom2games/commit/2d4bea4314e1bf7bcf3a1c70dfcfb50436a2752a
- https://github.com/habib256/pom2games/commit/301f1b56a8c0135ac023670b903735f38247c134

### Classification (reviewed)

These are native Apple II homebrew/adaptation works in a mixed collection; the commits do not relabel them as binary-derived reconstructions.
- https://github.com/habib256/pom2games/commit/2d4bea4314e1bf7bcf3a1c70dfcfb50436a2752a
- https://github.com/habib256/pom2games/commit/301f1b56a8c0135ac023670b903735f38247c134

### Source CPU (no-evidence-found)

The reviewed changes concern native target memory maps and do not establish a distinct original binary CPU for either title; source_cpu remains empty rather than inferred from Apple II output.
- https://github.com/habib256/pom2games/commit/2d4bea4314e1bf7bcf3a1c70dfcfb50436a2752a
- https://github.com/habib256/pom2games/commit/301f1b56a8c0135ac023670b903735f38247c134

### Target CPU (reviewed)

Existing 6502 and 65C02 collection outputs remain; the reviewed ca65/cc65 memory reorganizations add no new target CPU.
- https://github.com/habib256/pom2games/commit/2d4bea4314e1bf7bcf3a1c70dfcfb50436a2752a
- https://github.com/habib256/pom2games/commit/301f1b56a8c0135ac023670b903735f38247c134

### Build (reviewed)

WARGALAGA II moves PT3 music and sprite packs in auxiliary memory, recovers about 1.9 KiB main RAM and adds a steady-music IRQ test. Robot Space Station swaps PLAY/FRONT overlays through hidden DHGR page 2, recovers about 1.7 KiB and tests five screen transitions against RSS.OVL. Limitations: The tracker did not build the disk images, run the tests or verify the measured free-space figures.
- https://github.com/habib256/pom2games/commit/2d4bea4314e1bf7bcf3a1c70dfcfb50436a2752a
- https://github.com/habib256/pom2games/commit/301f1b56a8c0135ac023670b903735f38247c134

### Runtime profiles (reviewed)

The memory maps strengthen implementation evidence but do not establish a lower Apple II minimum than the collection's existing author-stated profiles.
- https://github.com/habib256/pom2games/commit/2d4bea4314e1bf7bcf3a1c70dfcfb50436a2752a
- https://github.com/habib256/pom2games/commit/301f1b56a8c0135ac023670b903735f38247c134

### AI (reviewed)

Both reviewed feature commits explicitly credit Claude Opus 5.5; this is development attribution, separate from any in-game AI.
- https://github.com/habib256/pom2games/commit/2d4bea4314e1bf7bcf3a1c70dfcfb50436a2752a
- https://github.com/habib256/pom2games/commit/301f1b56a8c0135ac023670b903735f38247c134

### Relationships (reviewed)

WARGALAGA II and Robot Space Station are now named collection subjects, not duplicate repository records; existing Wilderness reconstruction provenance remains distinct from these native works.
- https://github.com/habib256/pom2games/commit/2d4bea4314e1bf7bcf3a1c70dfcfb50436a2752a
- https://github.com/habib256/pom2games/commit/301f1b56a8c0135ac023670b903735f38247c134

## amy-studio-colecovision-development-environment

Project ID: amy-studio-colecovision-development-environment · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "amy-studio-colecovision-development-environment",
  "last_activity": "2026-10-31",
  "last_checked": "2026-10-31",
  "status": "Amy Studio adds ten explicitly labelled faithful COMPUTE! adaptations as ColecoVision examples, preserving source-game rules and quirks while remaining an original browser development environment.",
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
    "Chutes"
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
    "manual-canon example manifests"
  ]
}
```

Expected existing project SHA256: 321e0742631c27116ff3c2cc0abb29aa6dc171841c9b6bc0244e237bc831cf40

### Identity (reviewed)

Amy Studio remains the original browser-based ColecoVision/ADAM development environment; the ten newly named COMPUTE! adaptations are bundled examples and subjects inside it.
- https://github.com/amypurple/AmyStudio/commit/d64559d2bf0258defcb1f093344e3fd200f48f22
- https://github.com/amypurple/AmyStudio/commit/26ac8be8c0002395adbb1cb622cb250a936f8076

### Classification (reviewed)

The manifest labels each new work a faithful adaptation. They are source-listing ports for the original toolchain, not reverse-engineered binaries and not independent repository projects.
- https://github.com/amypurple/AmyStudio/commit/d64559d2bf0258defcb1f093344e3fd200f48f22
- https://github.com/amypurple/AmyStudio/commit/26ac8be8c0002395adbb1cb622cb250a936f8076

### Source CPU (not-applicable)

Amy Studio is original development tooling and the adaptations derive from published BASIC listings rather than analyzed original executables; no source binary CPU is assigned.
- https://github.com/amypurple/AmyStudio/commit/26ac8be8c0002395adbb1cb622cb250a936f8076

### Target CPU (reviewed)

The examples use Amy's existing ColecoVision legacy memory profile and Z80 output; no new target CPU is introduced.
- https://github.com/amypurple/AmyStudio/commit/d64559d2bf0258defcb1f093344e3fd200f48f22
- https://github.com/amypurple/AmyStudio/commit/26ac8be8c0002395adbb1cb622cb250a936f8076

### Build (reviewed)

The manifest adds eight February/March 1983 and two April 1983 ports with preserved mechanics, provenance and the colecovision_legacy_sdcc profile; the Chutes source documents coordinate, sprite, timing and collision adaptations from the Atari listing. Limitations: The tracker did not compile or run the ten example ROMs on GearColeco or physical hardware.
- https://github.com/amypurple/AmyStudio/commit/d64559d2bf0258defcb1f093344e3fd200f48f22
- https://github.com/amypurple/AmyStudio/commit/26ac8be8c0002395adbb1cb622cb250a936f8076

### Runtime profiles (no-evidence-found)

The named ColecoVision memory profile is a build profile, but the reviewed commits state no new verified minimum console RAM/peripheral configuration or host CPU/RAM floor.
- https://github.com/amypurple/AmyStudio/commit/d64559d2bf0258defcb1f093344e3fd200f48f22
- https://github.com/amypurple/AmyStudio/commit/26ac8be8c0002395adbb1cb622cb250a936f8076

### AI (reviewed)

The Chutes source explicitly says Claude ported it for Amy Studio, consistent with the README's Claude/OpenAI Codex disclosure; attribution remains scoped to documented work.
- https://github.com/amypurple/AmyStudio/commit/26ac8be8c0002395adbb1cb622cb250a936f8076
- https://github.com/amypurple/AmyStudio

### Relationships (reviewed)

The ten adaptations are now named subjects within Amy Studio's example corpus. Their original COMPUTE! authors and source machines remain credited, while the self-hosted GearColeco core remains a test dependency.
- https://github.com/amypurple/AmyStudio/commit/d64559d2bf0258defcb1f093344e3fd200f48f22
- https://github.com/amypurple/AmyStudio/commit/26ac8be8c0002395adbb1cb622cb250a936f8076

## Source updates

```json
[
  {
    "id": "github-yeager-firestaff",
    "last_reviewed": "2026-10-31",
    "reason": "Reviewed authenticated Atari ST same-archive admission and menu-route regression while retaining playability limits.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-rmtew",
    "last_reviewed": "2026-10-31",
    "reason": "Reviewed Starglider 2 collision, retirement, homing and HUD continuations with original-CPU and byte-exact boundaries.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "wide-20261018h-zapple-ii-bpm-prodos-softcard-environment",
    "last_reviewed": "2026-10-31",
    "reason": "Reviewed SoftCard/drive configuration staging and persistent NETCCP service without inferring hardware minima.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-dcgibbons-moria8",
    "last_reviewed": "2026-10-31",
    "reason": "Reviewed disk save/load playtests, deterministic failure capture and drive-status retry paths.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-thebitculture-ase",
    "last_reviewed": "2026-10-31",
    "reason": "Reviewed RP5C15 and IKBD clock emulation plus snapshot-deterministic state.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "intake-ikari-pl-koncepcja",
    "last_reviewed": "2026-10-31",
    "reason": "Reviewed the documented shared-memory frame ring, independent reader and cross-platform conformance tests.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "wide-20261018n-spice86-real-mode-pc-reverse-engineering-emulator",
    "last_reviewed": "2026-10-31",
    "reason": "Reviewed stack-level redirected returns and SSA/IR data-flow boundaries.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-ricardoquesada",
    "last_reviewed": "2026-10-31",
    "reason": "Reviewed lexical-scope indexing, range rendering and documented invariants.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-habib256-pom2games",
    "last_reviewed": "2026-10-31",
    "reason": "Reviewed WARGALAGA II and Robot Space Station memory reorganizations and added both as collection subjects.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-amypurple-amystudio",
    "last_reviewed": "2026-10-31",
    "reason": "Reviewed ten new faithful COMPUTE! adaptations and retained them as Amy Studio example subjects.",
    "review_state": "substantially-reviewed"
  }
]
```

## Research event notes

The CPU audit queue contained zero unresolved source or target CPU areas, so no architecture value was invented for this pass. Ten materially changed projects were reviewed from primary commits. WARGALAGA II, Robot Space Station and ten COMPUTE! adaptations are retained as named subjects inside their established repository-level collection or development-environment records rather than being misclassified as reverse-engineered standalone projects. The tracker did not compile or execute upstream software.
