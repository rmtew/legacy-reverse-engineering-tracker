# Reconstruction, runtime and tooling maintenance

Review nine materially changed projects, capture MPX68K runtime requirements, expand ZX84 CPU scope, close the game-music-extraction build audit, and record current reconstruction and emulator fixes.

Date: 2026-10-27 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- shdecompilations-silent-hill-decomp / Build (reviewed): The tracker did not extract the game, compile, run, or byte-compare the result.
- shdecompilations-silent-hill-decomp / Runtime profiles (no-evidence-found): The inspected README and collision change do not state a minimum original or host CPU, RAM, ROM/OS or chipset profile suitable for a verified runtime record.
- zeal8bit-os / Build (reviewed): The tracker did not install dependencies, build the OS, flash hardware or boot an emulator.
- zeal8bit-os / Runtime profiles (no-evidence-found): The README gives configurable kernel-size observations and a four-page MMU design, but requirements vary by target and drivers. Those design values are not promoted to a universal verified minimum hardware profile.
- zeal8bit-os / AI (no-evidence-found): The inspected README and deterministic-build commit contain no explicit development-AI attribution. This bounded absence does not establish non-use.
- amigaports-m68k-amigaos-gcc / Build (reviewed): The tracker did not build the toolchain or run the new boards; test-harness coverage must not be read as universal output compatibility.
- mpx68k-macos-emulator / Build (reviewed): The tracker did not build the Xcode project, supply ROMs, mount an XDF image or run the emulator.
- mpx68k-macos-emulator / Runtime profiles (reviewed): These are author-stated requirements and were not independently runtime-tested.
- amiberry-system-emulator / Build (reviewed): This is upstream source evidence on development head, not a new release or an independent emulator run.
- cbongo-game-music-extraction / Build (reviewed): The new validation uses authored controls, not held-out commercial-game accuracy. The tracker did not install Perl/Python dependencies, render audio, run tests or inspect user-supplied media.
- zx84-z80-emulator-mcp / Build (reviewed): The tracker did not install dependencies, build the web application, run the MCP server, supply ROMs/media or test any emulated machine.
- zx84-z80-emulator-mcp / Runtime profiles (no-evidence-found): The inspected release documentation describes browser and headless use but does not state a minimum host CPU, RAM or OS/browser version suitable for a verified runtime profile.
- zombie-revenge-dc-decompilation / Build (reviewed): Progress percentages are upstream classifications, not independent whole-game correctness. The tracker did not extract media, regenerate sources, compile, compare or execute the game.
- zombie-revenge-dc-decompilation / Runtime profiles (no-evidence-found): The reviewed material does not state a minimum Dreamcast model/accessory profile or a verified host runtime profile beyond the original-platform SH-4 reconstruction context.
- virtua-tennis-dreamcast-analysis / Build (reviewed): These are upstream generator/classifier and test results, not independent full-game correctness. The tracker did not extract, regenerate, compile, compare or execute the game.
- virtua-tennis-dreamcast-analysis / Runtime profiles (no-evidence-found): No minimum Dreamcast accessory/model profile or host runtime minimum is stated in the inspected decompilation documentation.

## shdecompilations-silent-hill-decomp

Project ID: shdecompilations-silent-hill-decomp · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "shdecompilations-silent-hill-decomp",
  "last_checked": "2026-10-27",
  "status": "In-progress PlayStation matching decompilation; current collision work replaces opaque shape handling with typed polygon/cylinder structures and clearer pass-state logic; no independent build or execution"
}
```

Expected existing project SHA256: 1f61e1faea746c555bee0e863172f5308333e2f64c5f1b4d7d5afac366a4113d

### Identity (reviewed)

Silent Hill PlayStation matching decompilation. Current head materially refines the body-program collision subsystem rather than introducing a separate project.
- https://github.com/shdecompilations/silent-hill-decomp
- https://github.com/shdecompilations/silent-hill-decomp/commit/59fd80f8180f18d9d90c3442cc04ed1293786973

### Classification (reviewed)

Original-platform source reconstruction with executable and overlay matching. The collision commit turns previously opaque layout and control flow into typed polygon/cylinder attributes and named pass-state behavior; it is not a PC port.
- https://github.com/shdecompilations/silent-hill-decomp/commit/59fd80f8180f18d9d90c3442cc04ed1293786973

### Source CPU (reviewed)

The reviewed project remains a PlayStation MIPS executable reconstruction; the collision refactor does not change that source architecture.
- https://github.com/shdecompilations/silent-hill-decomp/blob/59fd80f8180f18d9d90c3442cc04ed1293786973/README.md

### Target CPU (reviewed)

Matching output remains original-target MIPS code; no additional port architecture is established by the reviewed change.
- https://github.com/shdecompilations/silent-hill-decomp/blob/59fd80f8180f18d9d90c3442cc04ed1293786973/README.md

### Build (reviewed)

The current diff restructures collision attributes while preserving explicit structure sizes and updates the corresponding C implementation. Upstream matching remains version-specific and dependent on owned game extraction and the documented target toolchain. Limitations: The tracker did not extract the game, compile, run, or byte-compare the result.
- https://github.com/shdecompilations/silent-hill-decomp/commit/59fd80f8180f18d9d90c3442cc04ed1293786973

### Runtime profiles (no-evidence-found)

The inspected README and collision change do not state a minimum original or host CPU, RAM, ROM/OS or chipset profile suitable for a verified runtime record.
- https://github.com/shdecompilations/silent-hill-decomp/blob/59fd80f8180f18d9d90c3442cc04ed1293786973/README.md
- https://github.com/shdecompilations/silent-hill-decomp/commit/59fd80f8180f18d9d90c3442cc04ed1293786973

### AI (reviewed)

The repository's existing bounded disclosure remains: game code is not knowingly AI-generated, while some throwaway decompilation helpers used AI. The reviewed collision commit carries no additional AI attribution.
- https://github.com/shdecompilations/silent-hill-decomp/blob/59fd80f8180f18d9d90c3442cc04ed1293786973/README.md
- https://github.com/shdecompilations/silent-hill-decomp/commit/59fd80f8180f18d9d90c3442cc04ed1293786973

### Relationships (reviewed)

The README's Vatuu references remain project lineage. The collision subsystem is part of the same body-program reconstruction, not a separately promoted component.
- https://github.com/shdecompilations/silent-hill-decomp/blob/59fd80f8180f18d9d90c3442cc04ed1293786973/README.md

## zeal8bit-os

Project ID: zeal8bit-os · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "zeal8bit-os",
  "last_checked": "2026-10-27",
  "status": "Portable native Z80 assembly OS with documented CMake/z88dk builds; generated libraries now use deterministic archive metadata"
}
```

Expected existing project SHA256: ca696f89178f7eae8bfe26da7b25d682cc2e94732855e29ab09e377acb2df9a2

### Identity (reviewed)

Zeal 8-bit OS remains a portable operating system written in Z80 assembly, with kernel, drivers, filesystems, target configurations and SDK examples.
- https://github.com/Zeal8bit/Zeal-8-bit-OS/blob/4d6c869ab57d2417f916258bb813408726b86c6e/README.md

### Classification (reviewed)

Substantial original retro operating-system development, inspired by Linux and CP/M interfaces but not described as binary-derived reconstruction.
- https://github.com/Zeal8bit/Zeal-8-bit-OS/blob/4d6c869ab57d2417f916258bb813408726b86c6e/README.md

### Source CPU (reviewed)

The README explicitly states the OS is written entirely in Z80 assembly for Z80 computers.
- https://github.com/Zeal8bit/Zeal-8-bit-OS/blob/4d6c869ab57d2417f916258bb813408726b86c6e/README.md

### Target CPU (reviewed)

The documented native output architecture is Z80. Broad supported targets are not converted into additional CPU claims.
- https://github.com/Zeal8bit/Zeal-8-bit-OS/blob/4d6c869ab57d2417f916258bb813408726b86c6e/README.md

### Build (reviewed)

The README documents CMake configuration and build commands using z88dk/z80asm. Current CMake compiler modules pass deterministic archive options so generated static libraries zero variable time, UID and GID metadata. Limitations: The tracker did not install dependencies, build the OS, flash hardware or boot an emulator.
- https://github.com/Zeal8bit/Zeal-8-bit-OS/blob/4d6c869ab57d2417f916258bb813408726b86c6e/README.md
- https://github.com/Zeal8bit/Zeal-8-bit-OS/commit/4d6c869ab57d2417f916258bb813408726b86c6e

### Runtime profiles (no-evidence-found)

The README gives configurable kernel-size observations and a four-page MMU design, but requirements vary by target and drivers. Those design values are not promoted to a universal verified minimum hardware profile.
- https://github.com/Zeal8bit/Zeal-8-bit-OS/blob/4d6c869ab57d2417f916258bb813408726b86c6e/README.md

### AI (no-evidence-found)

The inspected README and deterministic-build commit contain no explicit development-AI attribution. This bounded absence does not establish non-use.
- https://github.com/Zeal8bit/Zeal-8-bit-OS/blob/4d6c869ab57d2417f916258bb813408726b86c6e/README.md
- https://github.com/Zeal8bit/Zeal-8-bit-OS/commit/4d6c869ab57d2417f916258bb813408726b86c6e

### Relationships (reviewed)

The OS is part of the wider Zeal 8-bit Computer project and explicitly cites Linux and CP/M as interface inspirations; it remains one coherent OS repository rather than a reconstruction of either predecessor.
- https://github.com/Zeal8bit/Zeal-8-bit-OS/blob/4d6c869ab57d2417f916258bb813408726b86c6e/README.md

## amigaports-m68k-amigaos-gcc

Project ID: amigaports-m68k-amigaos-gcc · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "amigaports-m68k-amigaos-gcc",
  "last_checked": "2026-10-27",
  "status": "Active m68k-AmigaOS cross toolchain; tests now distinguish 68000 boards from 68020/68881 ixemul and newlib -fbaserel32 boards; tracker did not run the suite"
}
```

Expected existing project SHA256: 45ae15d02afee0def1554a1c9e5301e7d4f977fc2d175c79d000efaae63369e6

### Identity (reviewed)

AmigaPorts continuation of the m68k-AmigaOS GCC cross-compiler and associated binutils, libraries, SDK integration and tests.
- https://github.com/AmigaPorts/m68k-amigaos-gcc

### Classification (reviewed)

Retro-development compiler/toolchain infrastructure, not a recovered game, original-machine emulator or binary-derived program reconstruction.
- https://github.com/AmigaPorts/m68k-amigaos-gcc

### Source CPU (not-applicable)

There is no historical input executable whose CPU should be recorded as source_cpu for this compiler toolchain.
- https://github.com/AmigaPorts/m68k-amigaos-gcc

### Target CPU (reviewed)

The cross toolchain emits m68k AmigaOS code. Current tests explicitly cover baseline 68000 and 68020 plus 68881 configurations without implying one universal minimum.
- https://github.com/AmigaPorts/m68k-amigaos-gcc/commit/ec2840b1a549e73ec328dfc3137dbabc915327c7

### Build (reviewed)

New DejaGnu boards exercise ixemul with 68020/68881 libraries and newlib with 68020/68881 plus -fbaserel32. The commit notes these are for PR testing and not run by the ordinary make check target. Limitations: The tracker did not build the toolchain or run the new boards; test-harness coverage must not be read as universal output compatibility.
- https://github.com/AmigaPorts/m68k-amigaos-gcc/commit/ec2840b1a549e73ec328dfc3137dbabc915327c7
- https://github.com/AmigaPorts/m68k-amigaos-gcc/blob/ec2840b1a549e73ec328dfc3137dbabc915327c7/doc/testing.md

### Runtime profiles (not-applicable)

The reviewed 68000 and 68020/68881 DejaGnu boards are compiler test configurations, not minimum runtime requirements for all software produced by the toolchain.
- https://github.com/AmigaPorts/m68k-amigaos-gcc/commit/ec2840b1a549e73ec328dfc3137dbabc915327c7

### AI (reviewed)

The reviewed testsuite commit explicitly carries a Claude Opus 5.5 co-author trailer. Existing Copilot and Claude attribution remains scoped to evidenced commits rather than the entire toolchain.
- https://github.com/AmigaPorts/m68k-amigaos-gcc/commit/ec2840b1a549e73ec328dfc3137dbabc915327c7

### Relationships (reviewed)

The repository remains the AmigaPorts continuation of the established m68k-AmigaOS GCC lineage; ixemul and newlib are alternative runtime/library test configurations inside the same toolchain.
- https://github.com/AmigaPorts/m68k-amigaos-gcc
- https://github.com/AmigaPorts/m68k-amigaos-gcc/commit/ec2840b1a549e73ec328dfc3137dbabc915327c7

## mpx68k-macos-emulator

Project ID: mpx68k-macos-emulator · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "mpx68k-macos-emulator",
  "last_checked": "2026-10-27",
  "runtime_profiles": [
    {
      "cpu_family": "ARM64",
      "evidence": [
        "https://github.com/YosAwed/MPX68K/blob/b7172329f790c8cc0523de02ba8ffcc56e524689/README.md"
      ],
      "min_ram_kib": 4194304,
      "name": "macOS Apple Silicon build",
      "notes": "README also states 1 GB free disk space for ROM and disk images. Required original CGROM.DAT and IPLROM.DAT are not included.",
      "os": "macOS 12.0 Monterey or later",
      "platform": "macOS"
    },
    {
      "cpu_family": "x86-64",
      "evidence": [
        "https://github.com/YosAwed/MPX68K/blob/b7172329f790c8cc0523de02ba8ffcc56e524689/README.md"
      ],
      "min_ram_kib": 4194304,
      "name": "macOS Intel build",
      "notes": "README also states 1 GB free disk space for ROM and disk images. Required original CGROM.DAT and IPLROM.DAT are not included.",
      "os": "macOS 12.0 Monterey or later",
      "platform": "macOS"
    }
  ],
  "status": "macOS X68000 emulator for Apple Silicon and Intel; current head restores the XDF file handle needed by the macOS disk-image path"
}
```

Expected existing project SHA256: 8487da578115be73440e87ff85b2ee0f70777c5f5d25e99ddc87f42ee97d8946

### Identity (reviewed)

MPX68K is a macOS Sharp X68000 emulator using a C68K-based core with native Swift UI, storage, monitor and media integration.
- https://github.com/YosAwed/MPX68K/blob/b7172329f790c8cc0523de02ba8ffcc56e524689/README.md

### Classification (reviewed)

System-emulator port and modern native integration, not original game reconstruction. Mixed upstream component licences and required proprietary ROM/data remain distinct.
- https://github.com/YosAwed/MPX68K/blob/b7172329f790c8cc0523de02ba8ffcc56e524689/README.md
- https://github.com/YosAwed/MPX68K/blob/b7172329f790c8cc0523de02ba8ffcc56e524689/ARCHITECTURE.md

### Source CPU (reviewed)

The README explicitly describes M68000 CPU emulation for the Sharp X68000 guest.
- https://github.com/YosAwed/MPX68K/blob/b7172329f790c8cc0523de02ba8ffcc56e524689/README.md

### Target CPU (reviewed)

README explicitly supports both Apple Silicon and Intel Macs, recorded as ARM64 and x86-64 host architectures.
- https://github.com/YosAwed/MPX68K/blob/b7172329f790c8cc0523de02ba8ffcc56e524689/README.md

### Build (reviewed)

README documents the Xcode project and bundled C68K dependency. Current head restores the local FILEH declaration used by XDF_SetFD on the macOS file-backed path, fixing that build path without changing disk format scope. Limitations: The tracker did not build the Xcode project, supply ROMs, mount an XDF image or run the emulator.
- https://github.com/YosAwed/MPX68K/blob/b7172329f790c8cc0523de02ba8ffcc56e524689/README.md
- https://github.com/YosAwed/MPX68K/commit/b7172329f790c8cc0523de02ba8ffcc56e524689

### Runtime profiles (reviewed)

The README explicitly states macOS 12.0 or later, Apple Silicon or Intel, minimum 4 GB RAM and 1 GB free disk. Two host-CPU variants are captured; mandatory original ROM files remain separate prerequisites. Limitations: These are author-stated requirements and were not independently runtime-tested.
- https://github.com/YosAwed/MPX68K/blob/b7172329f790c8cc0523de02ba8ffcc56e524689/README.md

### AI (reviewed)

Existing direct Claude co-author evidence remains valid and distinct from configuration files. The reviewed merge commit itself carries no new AI attribution.
- https://github.com/YosAwed/MPX68K/commit/5458a6f77047
- https://github.com/YosAwed/MPX68K/commit/b7172329f790c8cc0523de02ba8ffcc56e524689

### Relationships (reviewed)

README explicitly traces the project through hissorii/px68k and GOROman's intervening iOS conversion. The macOS app and its disk/monitor integration remain this project's distinct work.
- https://github.com/YosAwed/MPX68K/blob/b7172329f790c8cc0523de02ba8ffcc56e524689/README.md

## amiberry-system-emulator

Project ID: amiberry-system-emulator · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "amiberry-system-emulator",
  "last_checked": "2026-10-27",
  "status": "v8.4.2 remains the published baseline; development head now hard-resets stale 24/32-bit address-space transitions and adds bounded x86-64 JIT fault diagnostics"
}
```

Expected existing project SHA256: c63798f603b1eaa4488d14af1ccfe0a7c37eb84aa532e361aa8cc656cd5f7cc1

### Identity (reviewed)

General-purpose UAE/WinUAE-derived Amiga system emulator. Current work continues post-v8.4.2 CPU, JIT and configuration correctness rather than creating a separate product.
- https://github.com/BlitterStudio/amiberry
- https://github.com/BlitterStudio/amiberry/releases/tag/v8.4.2
- https://github.com/BlitterStudio/amiberry/commit/a44fb280caa79dafda1e498cde4a6e21c423e30a

### Classification (reviewed)

System emulation and debugging/runtime maintenance. Guest CPU-mode correctness does not change the distinction between Amiga m68k guests and modern host CPU families.
- https://github.com/BlitterStudio/amiberry/commit/a44fb280caa79dafda1e498cde4a6e21c423e30a

### Source CPU (reviewed)

m68k remains the emulated guest family. The reviewed change explicitly handles transitions between 24-bit and 32-bit guest address-space layouts.
- https://github.com/BlitterStudio/amiberry/blob/a44fb280caa79dafda1e498cde4a6e21c423e30a/src/newcpu.cpp
- https://github.com/BlitterStudio/amiberry/commit/a44fb280caa79dafda1e498cde4a6e21c423e30a

### Target CPU (reviewed)

Existing documented ARM, x86, RISC-V and LoongArch64 host families remain unchanged. The new diagnostic path is specifically bounded to supported x86-64 JIT hosts and does not establish a new target.
- https://github.com/BlitterStudio/amiberry/blob/master/README.md
- https://github.com/BlitterStudio/amiberry/commit/a44fb280caa79dafda1e498cde4a6e21c423e30a

### Build (reviewed)

Current head forces a hard reset when a CPU-mode change leaves the bank table laid out for the old 24/32-bit address space. It also logs bounded backtraces, memory-bank data and CPU state for x86-64 faults outside JIT code, guarded to libc platforms that provide backtrace support. Limitations: This is upstream source evidence on development head, not a new release or an independent emulator run.
- https://github.com/BlitterStudio/amiberry/commit/a44fb280caa79dafda1e498cde4a6e21c423e30a

### Runtime profiles (reviewed)

The change states no new host CPU, RAM or OS minimum. Existing published Windows/macOS ARM64/x86-64 variants and v8.4.2 Linux AppImage glibc 2.35 floor remain unchanged.
- https://github.com/BlitterStudio/amiberry/releases/tag/v8.4.0
- https://github.com/BlitterStudio/amiberry/releases/tag/v8.4.2
- https://github.com/BlitterStudio/amiberry/commit/a44fb280caa79dafda1e498cde4a6e21c423e30a

### AI (reviewed)

Existing scoped ChatGPT, Claude and Copilot evidence remains. The reviewed address-space commit contains no additional co-author attribution.
- https://github.com/BlitterStudio/amiberry/commit/831f13e71ee6e872d6d3570f2c23068493d0dd15
- https://github.com/BlitterStudio/amiberry/commit/e28372fec0e9a957bce3cf5e791db3e3931e1724
- https://github.com/BlitterStudio/amiberry/commit/a44fb280caa79dafda1e498cde4a6e21c423e30a

### Relationships (reviewed)

Amiberry remains a UAE/WinUAE-derived Amiga system emulator. External Kickstart ROMs, game media and third-party components retain separate provenance; the current CPU/JIT fix does not alter lineage.
- https://github.com/BlitterStudio/amiberry/blob/master/README.md
- https://github.com/BlitterStudio/amiberry/blob/master/LICENSE

## cbongo-game-music-extraction

Project ID: cbongo-game-music-extraction · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "cbongo-game-music-extraction",
  "last_checked": "2026-10-27",
  "status": "Host-side multi-system music archaeology suite; current analysis conservatively reconstructs baked tracker chords with explicit ambiguity and authored validation controls",
  "techniques": [
    "ROM and disk extraction",
    "MIDI reconstruction",
    "disassembly-style sequence output",
    "game-code analysis notes",
    "AKAO format decoding",
    "baked-chord spectral analysis",
    "tracker-rendered probe validation",
    "ambiguity-preserving reconstruction"
  ]
}
```

Expected existing project SHA256: 586bf3daf4b397504bb2eed6063bc2c1f1b9f05334e4784525ac01b1cbbb7a7d

### Identity (reviewed)

Coherent multi-system collection of extraction and analysis scripts that read user-supplied ROM/disk images and produce MIDI, sequence listings and research notes. Current instrument-analysis modules remain part of the same root project.
- https://github.com/CBongo/game-music-extraction/blob/c26e9fd0744bb8fc8515c5cad335758c3ef0efa9/README.md
- https://github.com/CBongo/game-music-extraction/commit/c26e9fd0744bb8fc8515c5cad335758c3ef0efa9

### Classification (reviewed)

Music-sequence and instrument archaeology tooling spanning arcade, console and home-computer data. It reconstructs musical structure and analysis outputs rather than executable CPU code.
- https://github.com/CBongo/game-music-extraction/blob/c26e9fd0744bb8fc8515c5cad335758c3ef0efa9/README.md
- https://github.com/CBongo/game-music-extraction/blob/c26e9fd0744bb8fc8515c5cad335758c3ef0efa9/docs/instrument-composites.md

### Source CPU (not-applicable)

The reviewed work analyzes sample, tracker and sequence data across systems rather than one original executable architecture; platform names are not converted into source CPU guesses.
- https://github.com/CBongo/game-music-extraction/blob/c26e9fd0744bb8fc8515c5cad335758c3ef0efa9/README.md
- https://github.com/CBongo/game-music-extraction/blob/c26e9fd0744bb8fc8515c5cad335758c3ef0efa9/docs/instrument-composites.md

### Target CPU (not-applicable)

Outputs are MIDI, text, diagnostics and reconstructed event data rather than CPU-targeted binaries.
- https://github.com/CBongo/game-music-extraction/blob/c26e9fd0744bb8fc8515c5cad335758c3ef0efa9/README.md
- https://github.com/CBongo/game-music-extraction/blob/c26e9fd0744bb8fc8515c5cad335758c3ef0efa9/docs/instrument-composites.md

### Build (reviewed)

The repository documents directly runnable Perl extractors and a Python analysis package. Current code adds conservative baked-chord detection, event expansion, fixture generation and validation: upstream reports exact component sets for four priority tracker triads, avoids false composite calls on three single-tone controls, and abstains on ambiguous power/octave material. Limitations: The new validation uses authored controls, not held-out commercial-game accuracy. The tracker did not install Perl/Python dependencies, render audio, run tests or inspect user-supplied media.
- https://github.com/CBongo/game-music-extraction/blob/c26e9fd0744bb8fc8515c5cad335758c3ef0efa9/README.md
- https://github.com/CBongo/game-music-extraction/blob/c26e9fd0744bb8fc8515c5cad335758c3ef0efa9/docs/instrument-composite-validation.md
- https://github.com/CBongo/game-music-extraction/commit/c26e9fd0744bb8fc8515c5cad335758c3ef0efa9

### Runtime profiles (not-applicable)

This is host-side extraction and analysis tooling, not a runnable legacy-hardware output. The reviewed docs state tool/sample-rate choices but no meaningful minimum host CPU or RAM profile.
- https://github.com/CBongo/game-music-extraction/blob/c26e9fd0744bb8fc8515c5cad335758c3ef0efa9/docs/instrument-composites.md

### AI (reviewed)

Claude and Codex project instruction/configuration files remain explicit workflow signals but do not by themselves attribute the new analysis code. The reviewed commit has no co-author trailer, so project AI usage remains scoped to existing evidence.
- https://github.com/CBongo/game-music-extraction
- https://github.com/CBongo/game-music-extraction/commit/c26e9fd0744bb8fc8515c5cad335758c3ef0efa9

### Relationships (reviewed)

Ghidra Retro Machines remains an incubating child/related effort; system directories and the instrument-analysis package form one coherent root project rather than separate promoted titles.
- https://github.com/CBongo/game-music-extraction
- https://github.com/CBongo/game-music-extraction/blob/c26e9fd0744bb8fc8515c5cad335758c3ef0efa9/README.md

## zx84-z80-emulator-mcp

Project ID: zx84-z80-emulator-mcp · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "zx84-z80-emulator-mcp",
  "last_checked": "2026-10-27",
  "source_cpu": [
    "Z80",
    "6502",
    "65C02"
  ],
  "status": "Active browser-based multi-system 8-bit emulator, debugger and MCP automation bench; v0.10.0 adds major Atari, Electron, Enterprise and shared-machine expansion",
  "techniques": [
    "headless emulation",
    "MCP-assisted reverse engineering",
    "interactive debugging",
    "execution tracing",
    "memory and register inspection",
    "OCR",
    "disk and sector inspection",
    "multi-system chip and peripheral emulation"
  ]
}
```

Expected existing project SHA256: 8de712d8122d90326b1d21614c0aa10b12e70c555cca1f88ca471f2328b03ea3

### Identity (reviewed)

ZX84 is a browser-based 8-bit computer emulator with machine-specific hardware models, developer tools and a headless MCP server. Release 0.10.0 substantially broadens the same product rather than splitting platform-specific projects.
- https://github.com/damieng-zx/zx84/blob/a95a85f353c086fe4fdf588bf17539f9a2f9ca4d/README.md
- https://github.com/damieng-zx/zx84/commit/a95a85f353c086fe4fdf588bf17539f9a2f9ca4d

### Classification (reviewed)

Core multi-system emulator, debugger and automated reverse-engineering environment. It is original tooling informed by published hardware behavior and selectively adapted data/code, not a collection of reconstructed games.
- https://github.com/damieng-zx/zx84/blob/a95a85f353c086fe4fdf588bf17539f9a2f9ca4d/README.md
- https://github.com/damieng-zx/zx84/blob/a95a85f353c086fe4fdf588bf17539f9a2f9ca4d/THIRD_PARTY.md

### Source CPU (reviewed)

The supported-machine table explicitly distinguishes Z80, 6502 and 65C02 guests. These are emulated source architectures, not inferred from platform labels.
- https://github.com/damieng-zx/zx84/blob/a95a85f353c086fe4fdf588bf17539f9a2f9ca4d/README.md

### Target CPU (not-applicable)

ZX84 is browser/Node-hosted tooling and does not emit a fixed native CPU-targeted retro binary. No host CPU is inferred from TypeScript or browser execution.
- https://github.com/damieng-zx/zx84/blob/a95a85f353c086fe4fdf588bf17539f9a2f9ca4d/README.md

### Build (reviewed)

Release 0.10.0 merges a very large implementation expansion including Atari 8-bit, Acorn Electron and Enterprise systems plus shared machine/service refactoring. README documents browser execution and the headless MCP server with debugging, media and inspection controls. Limitations: The tracker did not install dependencies, build the web application, run the MCP server, supply ROMs/media or test any emulated machine.
- https://github.com/damieng-zx/zx84/commit/a95a85f353c086fe4fdf588bf17539f9a2f9ca4d
- https://github.com/damieng-zx/zx84/blob/a95a85f353c086fe4fdf588bf17539f9a2f9ca4d/README.md
- https://github.com/damieng-zx/zx84/blob/a95a85f353c086fe4fdf588bf17539f9a2f9ca4d/docs/developer-tools.md

### Runtime profiles (no-evidence-found)

The inspected release documentation describes browser and headless use but does not state a minimum host CPU, RAM or OS/browser version suitable for a verified runtime profile.
- https://github.com/damieng-zx/zx84/blob/a95a85f353c086fe4fdf588bf17539f9a2f9ca4d/README.md

### AI (reviewed)

Existing explicit Claude and unnamed OpenAI co-author evidence remains scoped to evidenced commits. The MCP server's use by AI assistants is a product capability and kept distinct from authorship evidence.
- https://github.com/damieng-zx/zx84/commit/a5d5faf06c84416d51d7b66986c69cec46030560
- https://github.com/damieng-zx/zx84/blob/a95a85f353c086fe4fdf588bf17539f9a2f9ca4d/README.md

### Relationships (reviewed)

README and third-party notices now document lineage precisely: behavior references include MAME, Fuse/libspectrum, openMSX, ep128emu and Clock Signal; selected MAME data, xBR shaders, Bedstead glyphs, ZXDB transforms, dskmanager-rust and retro-render material are adapted or consumed under separately stated terms. The multiple machine implementations remain one shared ZX84 project.
- https://github.com/damieng-zx/zx84/blob/a95a85f353c086fe4fdf588bf17539f9a2f9ca4d/README.md
- https://github.com/damieng-zx/zx84/blob/a95a85f353c086fe4fdf588bf17539f9a2f9ca4d/THIRD_PARTY.md

## zombie-revenge-dc-decompilation

Project ID: zombie-revenge-dc-decompilation · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "zombie-revenge-dc-decompilation",
  "last_checked": "2026-10-27",
  "status": "Dreamcast SH-4 decompilation with region-pinned rebuild and function-equivalence workflow; upstream reports 60.1% of C-capable functions and 23.3% of eligible code bytes complete, with 13.2% aggregate instruction coverage"
}
```

Expected existing project SHA256: 9c652ad8ee13e4512fdb669774ef547b31c676149cf6f68c3b492e86ef3f7597

### Identity (reviewed)

Zombie Revenge Dreamcast decompilation with disc-derived local extraction, generated C, assembly fallback and an interactive Shuriken Explorer view.
- https://github.com/consolesplayingconsoles/zombie-revenge-decomp/blob/ed22b044680a2b7e513470e99ff16e3e2f7fefeb/README.md

### Classification (reviewed)

Original-platform game decompilation and source reconstruction. Whole-executable matching with assembly fallback is kept distinct from complete C recovery and from per-function behavioral equivalence.
- https://github.com/consolesplayingconsoles/zombie-revenge-decomp/blob/ed22b044680a2b7e513470e99ff16e3e2f7fefeb/README.md
- https://github.com/consolesplayingconsoles/zombie-revenge-decomp/blob/ed22b044680a2b7e513470e99ff16e3e2f7fefeb/docs/equivalent.md

### Source CPU (reviewed)

The reconstructed Dreamcast executable remains SH-4 input.
- https://github.com/consolesplayingconsoles/zombie-revenge-decomp/blob/ed22b044680a2b7e513470e99ff16e3e2f7fefeb/README.md

### Target CPU (reviewed)

The matching rebuild remains SH-4 output for the original Dreamcast executable; no host port CPU is claimed.
- https://github.com/consolesplayingconsoles/zombie-revenge-decomp/blob/ed22b044680a2b7e513470e99ff16e3e2f7fefeb/README.md

### Build (reviewed)

Upstream reports 34 newly generated C functions, 384 functions identified as byte-identical SDK library code, 60.1% of 3,998 C-capable functions complete, 23.3% of 655,494 eligible bytes complete and 13.2% total instruction coverage. Individual equivalence records retain development/holdout case scope. Limitations: Progress percentages are upstream classifications, not independent whole-game correctness. The tracker did not extract media, regenerate sources, compile, compare or execute the game.
- https://github.com/consolesplayingconsoles/zombie-revenge-decomp/commit/ed22b044680a2b7e513470e99ff16e3e2f7fefeb
- https://github.com/consolesplayingconsoles/zombie-revenge-decomp/blob/ed22b044680a2b7e513470e99ff16e3e2f7fefeb/README.md
- https://github.com/consolesplayingconsoles/zombie-revenge-decomp/blob/ed22b044680a2b7e513470e99ff16e3e2f7fefeb/sdk-identical.txt

### Runtime profiles (no-evidence-found)

The reviewed material does not state a minimum Dreamcast model/accessory profile or a verified host runtime profile beyond the original-platform SH-4 reconstruction context.
- https://github.com/consolesplayingconsoles/zombie-revenge-decomp/blob/ed22b044680a2b7e513470e99ff16e3e2f7fefeb/README.md

### AI (reviewed)

The reviewed progress commit explicitly carries a Claude Opus 5.5 co-author trailer. Attribution is limited to evidenced work rather than treating the full decompilation as AI-generated.
- https://github.com/consolesplayingconsoles/zombie-revenge-decomp/commit/ed22b044680a2b7e513470e99ff16e3e2f7fefeb

### Relationships (reviewed)

SDK-identical functions are now explicitly separated from game-derived recovery. The repository remains one title-specific decompilation in the consolesplayingconsoles tool/explorer ecosystem.
- https://github.com/consolesplayingconsoles/zombie-revenge-decomp/blob/ed22b044680a2b7e513470e99ff16e3e2f7fefeb/sdk-identical.txt
- https://github.com/consolesplayingconsoles/zombie-revenge-decomp/blob/ed22b044680a2b7e513470e99ff16e3e2f7fefeb/README.md

## virtua-tennis-dreamcast-analysis

Project ID: virtua-tennis-dreamcast-analysis · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "virtua-tennis-dreamcast-analysis",
  "last_checked": "2026-10-27",
  "status": "Dreamcast SH-4 decompilation with disc-driven reconstruction and C-equivalence workflow; upstream reports 93.9% of C-capable functions and 66.4% of eligible code bytes complete, with 45.9% aggregate instruction coverage"
}
```

Expected existing project SHA256: a2fc58ce75f8c8d687f6b1f5dd396a362ea0363e3772b4f5d3b748f639b469dc

### Identity (reviewed)

Virtua Tennis Dreamcast decompilation with disc-derived executable reconstruction, symbol/asset maps, generated C and side-by-side Shuriken Explorer presentation.
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/blob/d82fc50aa7af487a308c5ceac87b4f7a2b01a14d/README.md

### Classification (reviewed)

Original-platform game decompilation. Byte-identical executable assembly fallback, C-capable function completion, eligible-byte completion and test coverage are separate measures and are not collapsed into one completeness claim.
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/blob/d82fc50aa7af487a308c5ceac87b4f7a2b01a14d/README.md

### Source CPU (reviewed)

The source executable remains Dreamcast SH-4 machine code.
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/blob/d82fc50aa7af487a308c5ceac87b4f7a2b01a14d/README.md

### Target CPU (reviewed)

The reconstruction targets SH-4 for the original Dreamcast executable; no modern host port output is established.
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/blob/d82fc50aa7af487a308c5ceac87b4f7a2b01a14d/README.md

### Build (reviewed)

Upstream reports 140 newly generated C functions, 93.9% of 3,281 C-capable functions complete, 66.4% of 787,322 eligible bytes complete, 45.9% total instruction coverage and only 16 remaining FUN-style names. SDK matching was recalculated with updated structure-return, argument-area and block-copy handling. Limitations: These are upstream generator/classifier and test results, not independent full-game correctness. The tracker did not extract, regenerate, compile, compare or execute the game.
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/commit/d82fc50aa7af487a308c5ceac87b4f7a2b01a14d
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/blob/d82fc50aa7af487a308c5ceac87b4f7a2b01a14d/README.md
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/blob/d82fc50aa7af487a308c5ceac87b4f7a2b01a14d/sdk-identical.txt

### Runtime profiles (no-evidence-found)

No minimum Dreamcast accessory/model profile or host runtime minimum is stated in the inspected decompilation documentation.
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/blob/d82fc50aa7af487a308c5ceac87b4f7a2b01a14d/README.md

### AI (reviewed)

The reviewed generator/progress commit explicitly carries a Claude Opus 5.5 co-author trailer. Attribution is scoped to evidenced work, not generalized to every recovered function.
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/commit/d82fc50aa7af487a308c5ceac87b4f7a2b01a14d

### Relationships (reviewed)

SDK-identical library functions are explicitly tracked separately from game-derived C recovery. The repository remains a title-specific project sharing tooling and the Shuriken Explorer presentation with related Dreamcast decomps.
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/blob/d82fc50aa7af487a308c5ceac87b4f7a2b01a14d/sdk-identical.txt
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/blob/d82fc50aa7af487a308c5ceac87b4f7a2b01a14d/README.md

## Source ids

```json
[
  "github-shdecompilations-silent-hill-decomp",
  "pass23-zeal8bit-os",
  "intake-amigaports-m68k-amigaos-gcc",
  "wide-20261018d-mpx68k-macos-emulator",
  "github-blitterstudio-amiberry",
  "github-cbongo-game-music-extraction",
  "github-damieng-zx-zx84",
  "pass32-zombie-revenge-dc-decompilation",
  "pass23-virtua-tennis-dreamcast-analysis"
]
```

## Research event notes

The CPU audit queue returned zero unresolved source or target CPU areas before project selection, so no architecture fields were invented to meet a quota. This pass instead reviewed nine projects with material upstream changes and two stale high-value audit gaps. Primary commit diffs and pinned documentation were inspected. No upstream program, operating system, toolchain, emulator, test suite, ROM, disk image or game was built or executed by the tracker; percentages, tests and fixes remain attributed upstream claims.
