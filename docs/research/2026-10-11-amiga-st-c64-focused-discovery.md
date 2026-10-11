# Amiga-first discovery: native reconstructions, preserved source and development tools

Add eleven reviewed Amiga, Atari ST and C64 projects; retain deduplicated and deferred leads

Date: 2026-10-11 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- no-cpu-amiga-demo-framework / AI (no-evidence-found): No explicit AI-development disclosure was found in the inspected README, main.dart, copper/memory samples and ten latest default-branch commit messages. The runner's separate non-use declaration does not establish this repository's authorship, so AI usage remains unknown.
- moonstone-ace-amiga-reconstruction / Identity (reviewed): Original game data must be supplied by the player. No repository-root license file was present in the inspected listing; source availability is not a claim of unrestricted reuse.
- moonstone-ace-amiga-reconstruction / Build (reviewed): No independent build, boot, playthrough, hardware test or original-binary comparison was performed. Some oracle tests need developer-only IRA listings; public-checkout tests can skip those. A few setup paths remain developer-specific.
- moonstone-ace-amiga-reconstruction / Relationships (reviewed): The wider moonshard lineage was not exhaustively mapped; the source identifies its role as reference material.
- goodsoup-comi-amiga-native-interpreter / Build (reviewed): No compilation, execution, game completion or binary comparison was performed. The detailed runtime report is dated 2022-08-04 and the repository's latest inspected commit is 2023-10-01; do not present it as a recent playtest.
- goodsoup-comi-amiga-native-interpreter / AI (no-evidence-found): README, implementation/build files and five latest default-branch commits were checked; no explicit development-AI usage attribution was found. AI usage remains unknown, not false.
- sevgi-amiga-game-engine-editor / Build (reviewed): No independent build or editor/template execution was performed. MorphOS and AmigaOS4 targets are explicitly untested. Performance statements framed as aims are not treated as measurements.
- sevgi-amiga-game-engine-editor / AI (no-evidence-found): README, tilemap source, makefile and five recent default-branch commits contain no explicit development-AI disclosure. Preserve unknown usage.
- sevgi-amiga-game-engine-editor / Relationships (reviewed): Lineage is established from the author's README; linked package contents were inaccessible in this pass.
- idopus-directory-opus-modern-port / Build (reviewed): No dependency installation, compilation, launch, filesystem operation or binary comparison was performed. Feature claims are upstream descriptions; README matrix may lag more recent implementation commits.
- idopus-directory-opus-modern-port / Relationships (reviewed): The author's clean-room wording is reported as source-guided porting, not independently certified legal provenance. APL source licensing and trademark restrictions are documented upstream.
- directory-opus-582-original-amiga-source / Build (reviewed): No compilation, execution, installer validation or comparison to the commercial binary was performed. The original development environment uses Amiga assigns and libraries that were not provisioned.
- directory-opus-582-original-amiga-source / Runtime profiles (no-evidence-found): The reviewed release note and source/build files establish Amiga/68000 development but do not state verified minimum runtime RAM, CPU variant or OS version for this archived output. No runtime profile is inferred from the compiler or the platform.
- directory-opus-582-original-amiga-source / AI (no-evidence-found): The README, source/build files and sole initial commit were reviewed without explicit AI-development evidence. Usage remains null; historical dates alone are not used to infer a false value.
- smonson-libtos-atari-st / Build (reviewed): No compile, linked test-program execution or byte comparison was performed.
- smonson-libtos-atari-st / AI (no-evidence-found): Bounded review, not proof of non-use.
- atari-libs-hildenborg / Build (reviewed): Build, runnable and byte-exact facts stay unknown; source-generation and test instructions are not a reproduced pass.
- atari-libs-hildenborg / AI (no-evidence-found): Automatic testing and mechanical XML code generation are not evidence of generative AI.
- c64-misc-ricardoquesada / Build (reviewed): The test README retains stale eight-test claims/sample results while the current Makefile names 13 targets. Its production-grade/cycle-exact wording was not independently validated, so no blanket build or runtime success is asserted.
- c64-misc-ricardoquesada / Runtime profiles (no-evidence-found): Do not infer collection-wide NTSC compatibility or RAM requirements from the platform. No emulator or physical hardware testing occurred.
- c64-misc-ricardoquesada / AI (no-evidence-found): Writing style and project references do not establish AI usage.
- 5plusbuttonsjoystick-c64-software / Build (reviewed): All build flags stay unknown. The payload is binary machine code rather than editable assembly source. Compatible input has CRC32 0x19176BAB; successful patching would intentionally change bytes, not establish original-byte identity.
- 5plusbuttonsjoystick-c64-software / Runtime profiles (no-evidence-found): C64/VIC20/Amiga are mentioned for the physical joystick; that does not establish VIC20 or Amiga software targets for the inspected C64 patches.
- 5plusbuttonsjoystick-c64-software / AI (no-evidence-found): Bounded inspection, not proof of non-use.

## No-CPU Amiga demo runner and platform specification

Project ID: no-cpu-amiga-demo-runner · Overall audit: reviewed

### Typed catalogue values

```json
{
  "ai": {
    "evidence": [
      "Runner README explicitly states that the runner code was written without AI-based code-generation tools: https://github.com/askeksa/NoCpuChallenge/blob/c9a143fb8d31eff53d386ee51a46c96c71e983e5/runner/README.md"
    ],
    "tools": [],
    "usage": false
  },
  "build": {
    "byte_exact": null,
    "compilable": null,
    "playable": null,
    "runnable": null
  },
  "display_title": "No-CPU Amiga demo runner and platform specification",
  "id": "no-cpu-amiga-demo-runner",
  "last_activity": null,
  "last_checked": "2026-10-11",
  "re_started": null,
  "reconstructed_languages": [
    "m68k assembly"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/askeksa/NoCpuChallenge",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Source reviewed; no independent build or runtime test",
  "subjects": [],
  "tags": [
    "amiga",
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "m68k"
  ],
  "target_kinds": [],
  "target_platforms": [
    "Amiga"
  ],
  "techniques": [],
  "title": "No-CPU Amiga Demo Challenge",
  "tool_kinds": [
    "development-environment",
    "automation"
  ],
  "types": [
    "native demo runner",
    "hardware demo development tool"
  ],
  "upstream_name": "No-CPU Amiga Demo Challenge",
  "work_kinds": []
}
```

### Identity (reviewed)

The challenge repository supplies a standard initial Amiga chipset state and the actual no-CPU demo launcher. Runner.S loads chip.dat or chip.zx0, preserves/restores chip memory when possible, configures custom registers and supports exit/reload controls. A runner executable is included.
- https://github.com/askeksa/NoCpuChallenge/blob/c9a143fb8d31eff53d386ee51a46c96c71e983e5/README.md
- https://github.com/askeksa/NoCpuChallenge/blob/c9a143fb8d31eff53d386ee51a46c96c71e983e5/runner/README.md
- https://github.com/askeksa/NoCpuChallenge/blob/c9a143fb8d31eff53d386ee51a46c96c71e983e5/runner/Runner.S

### Classification (reviewed)

Substantive native demo-development tooling, not rules alone: the launcher initializes hardware, loads/decompresses memory images and implements restart/restore behavior. The specification and launcher form one coherent root-scoped work.
- https://github.com/askeksa/NoCpuChallenge/blob/c9a143fb8d31eff53d386ee51a46c96c71e983e5/runner/README.md
- https://github.com/askeksa/NoCpuChallenge/blob/c9a143fb8d31eff53d386ee51a46c96c71e983e5/runner/Runner.S

### Source CPU (not-applicable)

The runner is original development infrastructure, not a reconstructed historical binary. No source CPU or original-platform fact is inferred from the hardware it supports.
- https://github.com/askeksa/NoCpuChallenge/blob/c9a143fb8d31eff53d386ee51a46c96c71e983e5/README.md
- https://github.com/askeksa/NoCpuChallenge/blob/c9a143fb8d31eff53d386ee51a46c96c71e983e5/runner/Runner.S

### Target CPU (reviewed)

Runner.S uses m68k address/data registers, Exec/DOS library calls and supervisor-mode setup. The runner itself is native m68k code; the loaded demo then uses custom-chip DMA/Copper execution without CPU participation. No exact minimum CPU is asserted from the instruction sample.
- https://github.com/askeksa/NoCpuChallenge/blob/c9a143fb8d31eff53d386ee51a46c96c71e983e5/runner/Runner.S
- https://github.com/askeksa/NoCpuChallenge/blob/c9a143fb8d31eff53d386ee51a46c96c71e983e5/runner/README.md

### Build (reviewed)

Assembly source, included ZX0 routine and a runner executable are present. The source uses Amiga include files and an NC: include path, so the complete assembler environment remains untested. No independent assembly, execution or byte-match check was performed.
- https://github.com/askeksa/NoCpuChallenge/blob/c9a143fb8d31eff53d386ee51a46c96c71e983e5/runner/Runner.S
- https://github.com/askeksa/NoCpuChallenge/blob/c9a143fb8d31eff53d386ee51a46c96c71e983e5/runner/README.md

### Runtime profiles (reviewed)

The specification sets memory-image ceilings by OCS/ECS/AGA chipset, not a universal minimum for the runner or each demo. The runner can work with chip-only memory but cannot then reliably exit or restart; extra non-chip memory enables preservation/restoration. These conditions are described without manufacturing a numeric minimum profile.
- https://github.com/askeksa/NoCpuChallenge/blob/c9a143fb8d31eff53d386ee51a46c96c71e983e5/README.md
- https://github.com/askeksa/NoCpuChallenge/blob/c9a143fb8d31eff53d386ee51a46c96c71e983e5/runner/README.md

### AI (reviewed)

Runner README explicitly declares that its code was written without AI-based code-generation tools. The false value is grounded in that author declaration and scoped to the tracked runner; it is not inferred from repository age and is not transferred to the separate invitation-demo repository.
- https://github.com/askeksa/NoCpuChallenge/blob/c9a143fb8d31eff53d386ee51a46c96c71e983e5/runner/README.md

### Relationships (reviewed)

NoCpuDemo is a separate authored demo/framework consuming this runner, not a mirrored runner. The included unzx0_68000 routine is a dependency. The root LICENSE grants zlib-style redistribution terms; third-party routine provenance should still be honored when redistributing.
- https://github.com/askeksa/NoCpuChallenge/blob/c9a143fb8d31eff53d386ee51a46c96c71e983e5/README.md
- https://github.com/askeksa/NoCpuChallenge/blob/c9a143fb8d31eff53d386ee51a46c96c71e983e5/runner/README.md
- https://github.com/askeksa/NoCpuChallenge/blob/c9a143fb8d31eff53d386ee51a46c96c71e983e5/LICENSE.txt

## No-CPU Amiga invitation demo and Dart authoring framework

Project ID: no-cpu-amiga-demo-framework · Overall audit: reviewed

### Typed catalogue values

```json
{
  "ai": {
    "tools": [],
    "usage": null
  },
  "build": {
    "byte_exact": null,
    "compilable": null,
    "playable": null,
    "runnable": null
  },
  "display_title": "No-CPU Amiga invitation demo and Dart authoring framework",
  "id": "no-cpu-amiga-demo-framework",
  "last_activity": null,
  "last_checked": "2026-10-11",
  "re_started": null,
  "reconstructed_languages": [
    "Dart"
  ],
  "record_class": "hybrid",
  "repo": "https://github.com/askeksa/NoCpuDemo",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Source reviewed; no independent build or runtime test",
  "subjects": [
    "No-CPU Challenge invitation demo"
  ],
  "tags": [
    "amiga",
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [],
  "target_kinds": [
    "demo"
  ],
  "target_platforms": [
    "Amiga"
  ],
  "techniques": [],
  "title": "No-CPU demo and framework",
  "tool_kinds": [
    "asset-tool",
    "development-environment"
  ],
  "types": [
    "native homebrew demo source",
    "Copper demo authoring framework"
  ],
  "upstream_name": "No-CPU demo and framework",
  "work_kinds": []
}
```

### Identity (reviewed)

The author identifies this as the Evoke 2025 invitation demo source including its reusable framework, ProTracker music converter, graphics and music. main.dart composes the opening, text, checkerboard, credits and Game of Life parts into a generated chip-memory image.
- https://github.com/askeksa/NoCpuDemo/blob/15c2b8d63677b861701b50f30f57f5f4529ee95a/README.md
- https://github.com/askeksa/NoCpuDemo/blob/15c2b8d63677b861701b50f30f57f5f4529ee95a/no_cpu/bin/main.dart

### Classification (reviewed)

A substantial original Amiga demo and reusable authoring package form a coherent hybrid root entry. Dart code builds copperlists, display/blitter/sprite structures, music data and memory placement; it is not an emulator wrapper for an old game and is not a binary-only collection.
- https://github.com/askeksa/NoCpuDemo/blob/15c2b8d63677b861701b50f30f57f5f4529ee95a/README.md
- https://github.com/askeksa/NoCpuDemo/blob/15c2b8d63677b861701b50f30f57f5f4529ee95a/no_cpu/bin/main.dart
- https://github.com/askeksa/NoCpuDemo/blob/15c2b8d63677b861701b50f30f57f5f4529ee95a/no_cpu/lib/copper.dart
- https://github.com/askeksa/NoCpuDemo/blob/15c2b8d63677b861701b50f30f57f5f4529ee95a/no_cpu/lib/memory.dart

### Source CPU (not-applicable)

This is newly authored demo/framework source, not a historical executable recovery. Empty source-platform/CPU fields distinguish the original work from reverse engineering.
- https://github.com/askeksa/NoCpuDemo/blob/15c2b8d63677b861701b50f30f57f5f4529ee95a/README.md
- https://github.com/askeksa/NoCpuDemo/blob/15c2b8d63677b861701b50f30f57f5f4529ee95a/no_cpu/bin/main.dart

### Target CPU (not-applicable)

The output is chip.dat for direct Amiga custom-chip execution. Copper.dart emits hardware-register command words and memory.dart lays out chip-memory blocks. No conventional target CPU is assigned to that data path, and neither the host Dart runtime nor the separate m68k launcher is relabeled as this demo's execution CPU.
- https://github.com/askeksa/NoCpuDemo/blob/15c2b8d63677b861701b50f30f57f5f4529ee95a/README.md
- https://github.com/askeksa/NoCpuDemo/blob/15c2b8d63677b861701b50f30f57f5f4529ee95a/no_cpu/lib/copper.dart
- https://github.com/askeksa/NoCpuDemo/blob/15c2b8d63677b861701b50f30f57f5f4529ee95a/no_cpu/lib/memory.dart

### Build (reviewed)

README documents Dart package resolution and running main.dart with assertions, alongside a NoCpuChallenge checkout receiving chip.dat. The source and effect modules are present, but dependencies were not installed and the image was not generated or launched here. Compilation, runtime, gameplay and byte matching remain unknown.
- https://github.com/askeksa/NoCpuDemo/blob/15c2b8d63677b861701b50f30f57f5f4529ee95a/README.md
- https://github.com/askeksa/NoCpuDemo/blob/15c2b8d63677b861701b50f30f57f5f4529ee95a/no_cpu/bin/main.dart

### Runtime profiles (reviewed)

README says the general framework is mainly geared toward AGA; OCS adaptation is a possibility, not an established compatible build. The no-CPU launcher is an external requirement. No numeric minimum CPU/RAM or broader chipset compatibility is inferred, so runtime_profiles stays empty.
- https://github.com/askeksa/NoCpuDemo/blob/15c2b8d63677b861701b50f30f57f5f4529ee95a/README.md

### AI (no-evidence-found)

No explicit AI-development disclosure was found in the inspected README, main.dart, copper/memory samples and ten latest default-branch commit messages. The runner's separate non-use declaration does not establish this repository's authorship, so AI usage remains unknown.
- https://github.com/askeksa/NoCpuDemo/blob/15c2b8d63677b861701b50f30f57f5f4529ee95a/README.md
- https://github.com/askeksa/NoCpuDemo/commits/15c2b8d63677b861701b50f30f57f5f4529ee95a

### Relationships (reviewed)

NoCpuChallenge supplies the separately maintained launcher and execution contract; this repository supplies the concrete invitation production, assets and reusable Dart framework. The distinction is implementation versus runner, not a split of one directory into several entries. README states zlib for code and CC BY-NC 4.0 for graphics/music; asset rights differ from the framework license.
- https://github.com/askeksa/NoCpuDemo/blob/15c2b8d63677b861701b50f30f57f5f4529ee95a/README.md

## Moonstone — native C++ reconstruction for Amiga 1200

Project ID: moonstone-ace-amiga-reconstruction · Overall audit: reviewed

### Typed catalogue values

```json
{
  "ai": {
    "evidence": [
      "First public commit 55332f6f8cde577cb8ac3e96bb07d5f27f42448d explicitly credits Claude Opus 5.5; CLAUDE.md documents Claude Code project guidance."
    ],
    "tools": [
      "Claude"
    ],
    "usage": true
  },
  "build": {
    "byte_exact": null,
    "compilable": true,
    "playable": true,
    "runnable": true
  },
  "display_title": "Moonstone — native C++ reconstruction for Amiga 1200",
  "execution_paths": [
    {
      "evidence": [
        "https://github.com/Jarskih/moonstone-ace-public/blob/2bc43a2e673819cc9c71a50a800e5676edcacfb3/CLAUDE.md",
        "https://github.com/Jarskih/moonstone-ace-public/blob/2bc43a2e673819cc9c71a50a800e5676edcacfb3/docs/ARCHITECTURE.md",
        "https://github.com/Jarskih/moonstone-ace-public/blob/2bc43a2e673819cc9c71a50a800e5676edcacfb3/docs/PUBLISHING.md",
        "https://github.com/Jarskih/moonstone-ace-public/blob/2bc43a2e673819cc9c71a50a800e5676edcacfb3/src/engine/scenes.cpp"
      ],
      "method": "native-translation",
      "name": "Native A1200 reconstruction",
      "notes": "Game logic rebuilt as C++ on ACE; original executables supply data at startup. Unicorn executes original code only in comparison tests, not the shipped gameplay path.",
      "status": "playable"
    }
  ],
  "id": "moonstone-ace-amiga-reconstruction",
  "last_activity": "2026-10-10",
  "last_checked": "2026-10-11",
  "re_started": null,
  "reconstructed_languages": [
    "C++",
    "C",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/Jarskih/moonstone-ace-public",
  "runtime_profiles": [
    {
      "chipsets": [
        "AGA"
      ],
      "cpu_family": "m68k",
      "evidence": [
        "https://github.com/Jarskih/moonstone-ace-public/blob/2bc43a2e673819cc9c71a50a800e5676edcacfb3/README.md",
        "https://github.com/Jarskih/moonstone-ace-public/blob/2bc43a2e673819cc9c71a50a800e5676edcacfb3/CLAUDE.md"
      ],
      "min_chip_ram_kib": 2048,
      "min_cpu": "m68020",
      "name": "A1200 release",
      "notes": "Author specifies Amiga 1200 or WinUAE configured as one. Fast RAM recommended but not required for release; debug executable requires fast RAM. Three original game disks required.",
      "os": "Kickstart 3.x",
      "platform": "Amiga"
    }
  ],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [
    "m68k machine code"
  ],
  "source_platforms": [
    "Amiga"
  ],
  "status": "Upstream-reported playable A1200 reconstruction; original disks required; public-build proof documented.",
  "subjects": [
    "Moonstone: A Hard Days Knight"
  ],
  "tags": [
    "Amiga"
  ],
  "target_cpu": [
    "m68020"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Amiga"
  ],
  "techniques": [
    "decompilation",
    "source-reconstruction",
    "reimplementation"
  ],
  "title": "moonstone-ace",
  "tool_kinds": [],
  "types": [
    "native Amiga reconstruction"
  ],
  "upstream_name": "moonstone-ace",
  "work_kinds": [
    "decompilation",
    "source-reconstruction",
    "reimplementation"
  ]
}
```

### Identity (reviewed)

The repository contains one coherent reconstruction of Moonstone: A Hard Days Knight (Mindscape, 1991), including C++ gameplay, ACE runtime, original-data loaders and comparison tooling. README identifies original Amiga disks and the A1200 output. Keep one repository-root record. Limitations: Original game data must be supplied by the player. No repository-root license file was present in the inspected listing; source availability is not a claim of unrestricted reuse.
- https://github.com/Jarskih/moonstone-ace-public/blob/2bc43a2e673819cc9c71a50a800e5676edcacfb3/README.md
- https://github.com/Jarskih/moonstone-ace-public/blob/2bc43a2e673819cc9c71a50a800e5676edcacfb3/src/engine/scenes.cpp
- https://github.com/Jarskih/moonstone-ace-public/blob/2bc43a2e673819cc9c71a50a800e5676edcacfb3/docs/PUBLISHING.md

### Classification (reviewed)

README and CLAUDE.md document a 68k-disassembly-to-C++ reconstruction. src/engine/scenes.cpp implements frame loops and scene bodies with explicit original program.asm label/line references. Architecture separates native runtime, engine services, game API and rules. The game has been all C++ since milestone 7.1r; the original ASM is not linked. The fight-script VM is game bytecode interpretation, and Unicorn is confined to testing.
- https://github.com/Jarskih/moonstone-ace-public/blob/2bc43a2e673819cc9c71a50a800e5676edcacfb3/README.md
- https://github.com/Jarskih/moonstone-ace-public/blob/2bc43a2e673819cc9c71a50a800e5676edcacfb3/CLAUDE.md
- https://github.com/Jarskih/moonstone-ace-public/blob/2bc43a2e673819cc9c71a50a800e5676edcacfb3/src/engine/scenes.cpp
- https://github.com/Jarskih/moonstone-ace-public/blob/2bc43a2e673819cc9c71a50a800e5676edcacfb3/docs/ARCHITECTURE.md
- https://github.com/Jarskih/moonstone-ace-public/blob/2bc43a2e673819cc9c71a50a800e5676edcacfb3/docs/PUBLISHING.md

### Source CPU (reviewed)

README explicitly identifies original 68k machine code, and the source transcribes original program.asm operations and register-oriented interfaces. Store broad m68k; no minimum original CPU is inferred from Amiga branding.
- https://github.com/Jarskih/moonstone-ace-public/blob/2bc43a2e673819cc9c71a50a800e5676edcacfb3/README.md
- https://github.com/Jarskih/moonstone-ace-public/blob/2bc43a2e673819cc9c71a50a800e5676edcacfb3/src/engine/scenes.cpp

### Target CPU (reviewed)

BUILD.md specifies Bartman GCC with M68K_CPU=68020 and vasm -m68020; the README names the A1200/68020 target.
- https://github.com/Jarskih/moonstone-ace-public/blob/2bc43a2e673819cc9c71a50a800e5676edcacfb3/BUILD.md
- https://github.com/Jarskih/moonstone-ace-public/blob/2bc43a2e673819cc9c71a50a800e5676edcacfb3/README.md

### Build (reviewed)

docs/PUBLISHING.md section 7 reports a public-tree export built in Release and Debug with original-dependent reference material absent, then staged to a hard disk. It also records successful boot regression. README reports playable game flow and controls. These explicit upstream reports support compilable/runnable/playable=true. Original-data parity checks and same-project build comparisons do not establish equality to the original game's executable, so byte_exact remains null. Limitations: No independent build, boot, playthrough, hardware test or original-binary comparison was performed. Some oracle tests need developer-only IRA listings; public-checkout tests can skip those. A few setup paths remain developer-specific.
- https://github.com/Jarskih/moonstone-ace-public/blob/2bc43a2e673819cc9c71a50a800e5676edcacfb3/docs/PUBLISHING.md
- https://github.com/Jarskih/moonstone-ace-public/blob/2bc43a2e673819cc9c71a50a800e5676edcacfb3/README.md
- https://github.com/Jarskih/moonstone-ace-public/blob/2bc43a2e673819cc9c71a50a800e5676edcacfb3/BUILD.md

### Runtime profiles (reviewed)

README specifies A1200 or equivalent WinUAE: 68020, AGA, Kickstart 3.x, 2 MB chip RAM; fast RAM is recommended but not required for the release. CLAUDE.md separately says debug requires fast RAM. Profile describes the author's stated release requirements, not an independent hardware validation.
- https://github.com/Jarskih/moonstone-ace-public/blob/2bc43a2e673819cc9c71a50a800e5676edcacfb3/README.md
- https://github.com/Jarskih/moonstone-ace-public/blob/2bc43a2e673819cc9c71a50a800e5676edcacfb3/CLAUDE.md

### AI (reviewed)

The first public commit explicitly includes Co-Authored-By: Claude Opus 5.5. This is direct usage attribution, independently of the CLAUDE.md filename. CLAUDE.md contents describe guidance for Claude Code; the typed tool label is conservatively Claude and preserves the model in evidence.
- https://github.com/Jarskih/moonstone-ace-public/commit/55332f6f8cde577cb8ac3e96bb07d5f27f42448d
- https://github.com/Jarskih/moonstone-ace-public/blob/2bc43a2e673819cc9c71a50a800e5676edcacfb3/CLAUDE.md

### Relationships (reviewed)

ACE is the pinned engine dependency. CLAUDE.md says the moonshard C ports are cross-checks and identifies the original IRA listing as behavior reference. This repository's native A1200 gameplay implementation is distinct from the catalogue's Undine1/Moonstone-A-Hard-Days-Knight-2026 Windows game-specific-emulation record. No independent tracked equivalent was found by root and Moonstone subject checks. Limitations: The wider moonshard lineage was not exhaustively mapped; the source identifies its role as reference material.
- https://github.com/Jarskih/moonstone-ace-public/blob/2bc43a2e673819cc9c71a50a800e5676edcacfb3/CLAUDE.md
- https://github.com/Jarskih/moonstone-ace-public/blob/2bc43a2e673819cc9c71a50a800e5676edcacfb3/docs/PUBLISHING.md
- https://github.com/Jarskih/moonstone-ace-public/blob/2bc43a2e673819cc9c71a50a800e5676edcacfb3/README.md
- https://github.com/AmigaPorts/ACE

## Goodsoup — Curse of Monkey Island native Amiga interpreter

Project ID: goodsoup-comi-amiga-native-interpreter · Overall audit: reviewed

### Typed catalogue values

```json
{
  "ai": {
    "tools": [],
    "usage": null
  },
  "build": {
    "byte_exact": null,
    "compilable": null,
    "playable": null,
    "runnable": true
  },
  "display_title": "Goodsoup — Curse of Monkey Island native Amiga interpreter",
  "execution_paths": [
    {
      "evidence": [
        "https://github.com/betajaen/goodsoup/blob/c2f3a202fa599eed6f85c0cfa906bed7e9126f00/README",
        "https://github.com/betajaen/goodsoup/blob/c2f3a202fa599eed6f85c0cfa906bed7e9126f00/source/goodsoup/script.cpp",
        "https://github.com/betajaen/goodsoup/blob/c2f3a202fa599eed6f85c0cfa906bed7e9126f00/source/goodsoup/makefile"
      ],
      "method": "native-translation",
      "name": "Native SCUMM v8 engine",
      "notes": "C++ interprets SCUMM script bytecode and COMI resources; this is game-engine interpretation rather than x86 CPU emulation. Intro/video and limited room scripts are implemented.",
      "status": "partial"
    }
  ],
  "id": "goodsoup-comi-amiga-native-interpreter",
  "last_activity": "2023-10-01",
  "last_checked": "2026-10-11",
  "re_started": null,
  "reconstructed_languages": [
    "C++"
  ],
  "record_class": "subject",
  "repo": "https://github.com/betajaen/goodsoup",
  "runtime_profiles": [
    {
      "cpu_family": "m68k",
      "evidence": [
        "https://github.com/betajaen/goodsoup/blob/c2f3a202fa599eed6f85c0cfa906bed7e9126f00/README"
      ],
      "min_cpu": "m68020",
      "min_ram_kib": 2048,
      "name": "Native Amiga RTG interpreter",
      "notes": "Author requirements: 940 MiB free disk, P96-compatible graphics capable of 640x480 8-bit at 25 fps, and AHI with compatible audio hardware. These describe the partial RTG runtime, not completed gameplay; AGA remains planned.",
      "os": "Workbench 3.1 or higher",
      "platform": "Amiga"
    }
  ],
  "source_cpu": [],
  "source_language": [
    "SCUMM v8 bytecode",
    "game resource data"
  ],
  "source_platforms": [
    "PC"
  ],
  "status": "Partial native interpreter: opening video and chapter-one room/scripts documented; major gameplay features remain incomplete.",
  "subjects": [
    "The Curse of Monkey Island"
  ],
  "tags": [
    "PC",
    "Amiga",
    "Linux"
  ],
  "target_cpu": [
    "m68020"
  ],
  "target_kinds": [
    "game",
    "game-engine"
  ],
  "target_platforms": [
    "Amiga",
    "Linux"
  ],
  "techniques": [
    "reimplementation",
    "data-format-analysis",
    "reverse-engineering-derived-port"
  ],
  "title": "Goodsoup",
  "tool_kinds": [],
  "types": [
    "partial native game interpreter"
  ],
  "upstream_name": "Goodsoup",
  "work_kinds": [
    "reimplementation",
    "data-format-analysis",
    "reverse-engineering-derived-port"
  ]
}
```

### Identity (reviewed)

Robin Southern's Goodsoup is a single native Amiga interpreter/player project for The Curse of Monkey Island. README names the English GOG PC data and version 0.5; the repository has substantive C++ resource, VM, rendering and platform code. Link the repository root.
- https://github.com/betajaen/goodsoup/blob/c2f3a202fa599eed6f85c0cfa906bed7e9126f00/README
- https://github.com/betajaen/goodsoup/blob/c2f3a202fa599eed6f85c0cfa906bed7e9126f00/source/goodsoup/script.cpp

### Classification (reviewed)

The author identifies a partial fork and reimplementation of ScummVM 0.9.1 SCUMM v8 and NScumm. Reviewed script.cpp reads global/local/object-verb script resources with SCRP, LSCR, ENCD, EXCD and VERB handling; the makefile links dedicated VM, room, codec and SMUSH components. This qualifies at the demonstrated incomplete interpreter scope and does not emulate the original PC CPU.
- https://github.com/betajaen/goodsoup/blob/c2f3a202fa599eed6f85c0cfa906bed7e9126f00/README
- https://github.com/betajaen/goodsoup/blob/c2f3a202fa599eed6f85c0cfa906bed7e9126f00/source/goodsoup/script.cpp
- https://github.com/betajaen/goodsoup/blob/c2f3a202fa599eed6f85c0cfa906bed7e9126f00/source/goodsoup/makefile

### Source CPU (not-applicable)

The input established by README and script.cpp is the original PC game's resource containers and SCUMM v8 bytecode, not an analyzed x86 executable. Source platform stays PC exactly as documented; a physical original CPU is not assigned to these data/script inputs.
- https://github.com/betajaen/goodsoup/blob/c2f3a202fa599eed6f85c0cfa906bed7e9126f00/README
- https://github.com/betajaen/goodsoup/blob/c2f3a202fa599eed6f85c0cfa906bed7e9126f00/source/goodsoup/script.cpp

### Target CPU (reviewed)

The Amiga makefile invokes m68k-amigaos-gcc with -m68020, matching the README's explicit 68020 requirement. The Linux SDL alternative uses gcc -m32, but no specific Linux host architecture was established; target_cpu records only the positively identified Amiga m68020.
- https://github.com/betajaen/goodsoup/blob/c2f3a202fa599eed6f85c0cfa906bed7e9126f00/README
- https://github.com/betajaen/goodsoup/blob/c2f3a202fa599eed6f85c0cfa906bed7e9126f00/source/goodsoup/makefile

### Build (reviewed)

README's dated status describes a working boot script, difficulty dialog, opening SAN movie and chapter-one room with scripts executing, supporting runnable=true only for that partial output. Actors and inventory are placeholders, gameplay is described as little, and AGA waits on RTG completion. The C++98 makefile and build commands are present, but no current successful clean rebuild was verified; compilable/playable/byte_exact remain null. Limitations: No compilation, execution, game completion or binary comparison was performed. The detailed runtime report is dated 2022-08-04 and the repository's latest inspected commit is 2023-10-01; do not present it as a recent playtest.
- https://github.com/betajaen/goodsoup/blob/c2f3a202fa599eed6f85c0cfa906bed7e9126f00/README
- https://github.com/betajaen/goodsoup/blob/c2f3a202fa599eed6f85c0cfa906bed7e9126f00/source/goodsoup/makefile

### Runtime profiles (reviewed)

README explicitly gives Workbench 3.1+, Motorola 68020+, 2 MiB RAM, 940 MiB disk, RTG/P96 graphics at 640x480x8 and AHI. Those requirements are retained as author-reported requirements for the partial native runtime. No minimum Linux runtime is inferred from its make target.
- https://github.com/betajaen/goodsoup/blob/c2f3a202fa599eed6f85c0cfa906bed7e9126f00/README

### AI (no-evidence-found)

README, implementation/build files and five latest default-branch commits were checked; no explicit development-AI usage attribution was found. AI usage remains unknown, not false.
- https://github.com/betajaen/goodsoup/blob/c2f3a202fa599eed6f85c0cfa906bed7e9126f00/README
- https://github.com/betajaen/goodsoup/blob/c2f3a202fa599eed6f85c0cfa906bed7e9126f00/source/goodsoup/script.cpp
- https://github.com/betajaen/goodsoup/blob/c2f3a202fa599eed6f85c0cfa906bed7e9126f00/source/goodsoup/makefile
- https://github.com/betajaen/goodsoup/commit/c2f3a202fa599eed6f85c0cfa906bed7e9126f00

### Relationships (reviewed)

README explicitly credits ScummVM 0.9.1's SCUMM v8 engine and Valery Sablonniere's NScumm as partial code/implementation ancestors. Goodsoup adds native Amiga APIs and its own resource/VM implementation; it is not an unchanged mirror or CPU-emulator wrapper. GitHub metadata reports fork=false, which does not negate the documented source lineage.
- https://github.com/betajaen/goodsoup/blob/c2f3a202fa599eed6f85c0cfa906bed7e9126f00/README
- https://github.com/betajaen/goodsoup/blob/c2f3a202fa599eed6f85c0cfa906bed7e9126f00/source/goodsoup/script.cpp
- https://github.com/betajaen/goodsoup/blob/c2f3a202fa599eed6f85c0cfa906bed7e9126f00/source/goodsoup/makefile

## Sevgi Engine — native Amiga game engine and asset editor

Project ID: sevgi-amiga-game-engine-editor · Overall audit: reviewed

### Typed catalogue values

```json
{
  "ai": {
    "tools": [],
    "usage": null
  },
  "build": {
    "byte_exact": null,
    "compilable": true,
    "playable": null,
    "runnable": true
  },
  "display_title": "Sevgi Engine — native Amiga game engine and asset editor",
  "id": "sevgi-amiga-game-engine-editor",
  "last_activity": "2026-07-26",
  "last_checked": "2026-10-11",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Python"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/alpyre/Sevgi_Engine",
  "runtime_profiles": [
    {
      "chipsets": [
        "ECS",
        "AGA"
      ],
      "evidence": [
        "https://github.com/alpyre/Sevgi_Engine/blob/fcf1b2166351911d49baa6641cf7a359075721a2/README.md",
        "https://github.com/alpyre/Sevgi_Engine/blob/fcf1b2166351911d49baa6641cf7a359075721a2/makefile"
      ],
      "name": "Sevgi Editor and classic engine",
      "notes": "README requires ECS or AGA and MUI 3.8 for the editor. No minimum RAM or CPU model is documented in requirements; the editor's 68k makefile selects -m68020. PowerPC targets remain untested.",
      "os": "Kickstart 2.0+",
      "platform": "Amiga"
    }
  ],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Usable 68k engine/editor with tested compiler templates; PowerPC build targets exist but are explicitly untested.",
  "subjects": [],
  "tags": [
    "Amiga",
    "AmigaOS 4",
    "MorphOS"
  ],
  "target_cpu": [
    "m68020",
    "PowerPC"
  ],
  "target_kinds": [],
  "target_platforms": [
    "Amiga",
    "AmigaOS 4",
    "MorphOS"
  ],
  "techniques": [],
  "title": "Sevgi Engine",
  "tool_kinds": [
    "asset-tool",
    "development-environment"
  ],
  "types": [
    "native game engine and editor"
  ],
  "upstream_name": "Sevgi Engine",
  "work_kinds": []
}
```

### Identity (reviewed)

Sevgi Engine is a coherent original Amiga development toolkit comprising the native Sevgi Editor, generated game engine code, asset-conversion tools and genre templates. README and tilemap_creator.c establish substantive editor functionality; retain one repository-root record rather than splitting every generator.
- https://github.com/alpyre/Sevgi_Engine/blob/fcf1b2166351911d49baa6641cf7a359075721a2/README.md
- https://github.com/alpyre/Sevgi_Engine/blob/fcf1b2166351911d49baa6641cf7a359075721a2/tilemap_creator.c

### Classification (reviewed)

This is directly relevant retro-development tooling, with native game-engine boilerplate generation, asset management, palette/sprite/BOB/tile tools and template game projects. The inspected tilemap creator validates Tiled JSON and invokes the dedicated ConvertMap pipeline with project-specific game-object headers. No binary-derived reconstruction claim is made.
- https://github.com/alpyre/Sevgi_Engine/blob/fcf1b2166351911d49baa6641cf7a359075721a2/README.md
- https://github.com/alpyre/Sevgi_Engine/blob/fcf1b2166351911d49baa6641cf7a359075721a2/tilemap_creator.c

### Source CPU (not-applicable)

This is newly authored development tooling and engine code rather than recovery of one original machine-code program. No historical source CPU is assigned. The target Amiga CPUs are kept separately.
- https://github.com/alpyre/Sevgi_Engine/blob/fcf1b2166351911d49baa6641cf7a359075721a2/README.md
- https://github.com/alpyre/Sevgi_Engine/blob/fcf1b2166351911d49baa6641cf7a359075721a2/tilemap_creator.c
- https://github.com/alpyre/Sevgi_Engine/blob/fcf1b2166351911d49baa6641cf7a359075721a2/makefile

### Target CPU (reviewed)

The editor makefile uses m68k-amigaos-gcc -m68020 for its default OS3 target and -mcpu=powerpc with ppc-amigaos-gcc or ppc-morphos-gcc for OS4/MorphOS. README explicitly says the PowerPC targets have not been tested, so these are build targets rather than verified runtime profiles.
- https://github.com/alpyre/Sevgi_Engine/blob/fcf1b2166351911d49baa6641cf7a359075721a2/makefile
- https://github.com/alpyre/Sevgi_Engine/blob/fcf1b2166351911d49baa6641cf7a359075721a2/README.md

### Build (reviewed)

README states gcc, vbcc and SAS/C engine makefiles have been tested, provides a 68k editor make command, links compiled editor binaries and documents ready-to-compile-and-run templates. This supports upstream-reported compilable/runnable=true for the classic Amiga toolkit. It does not establish completed-game playability or byte matching; those remain null. Limitations: No independent build or editor/template execution was performed. MorphOS and AmigaOS4 targets are explicitly untested. Performance statements framed as aims are not treated as measurements.
- https://github.com/alpyre/Sevgi_Engine/blob/fcf1b2166351911d49baa6641cf7a359075721a2/README.md
- https://github.com/alpyre/Sevgi_Engine/blob/fcf1b2166351911d49baa6641cf7a359075721a2/makefile

### Runtime profiles (reviewed)

README's requirements specify ECS or AGA, Kickstart 2.0+ and MUI 3.8 for the editor. It does not state a runtime minimum CPU or RAM, so the runtime profile leaves both absent; -m68020 remains an explicit compile target rather than inferred tested hardware compatibility.
- https://github.com/alpyre/Sevgi_Engine/blob/fcf1b2166351911d49baa6641cf7a359075721a2/README.md
- https://github.com/alpyre/Sevgi_Engine/blob/fcf1b2166351911d49baa6641cf7a359075721a2/makefile

### AI (no-evidence-found)

README, tilemap source, makefile and five recent default-branch commits contain no explicit development-AI disclosure. Preserve unknown usage.
- https://github.com/alpyre/Sevgi_Engine/blob/fcf1b2166351911d49baa6641cf7a359075721a2/README.md
- https://github.com/alpyre/Sevgi_Engine/blob/fcf1b2166351911d49baa6641cf7a359075721a2/tilemap_creator.c
- https://github.com/alpyre/Sevgi_Engine/blob/fcf1b2166351911d49baa6641cf7a359075721a2/makefile
- https://github.com/alpyre/Sevgi_Engine/commit/fcf1b2166351911d49baa6641cf7a359075721a2

### Relationships (reviewed)

README identifies Georg Steger's ScrollingTricks, specifically Scroller_XYUnlimited2_64, as the engine's foundation, and Frank Wille's ptplayer as the sound component. This repository adds a substantial editor/generator/asset suite. Links to those Aminet packages were screened locally but returned HTTP 403 via the web reader, so their independent project scope was not adjudicated. Limitations: Lineage is established from the author's README; linked package contents were inaccessible in this pass.
- https://github.com/alpyre/Sevgi_Engine/blob/fcf1b2166351911d49baa6641cf7a359075721a2/README.md
- https://aminet.net/package/dev/src/ScrollingTrick
- https://aminet.net/package/mus/play/ptplayer

## iDOpus — Directory Opus 5 Magellan modern desktop port

Project ID: idopus-directory-opus-modern-port · Overall audit: reviewed

### Typed catalogue values

```json
{
  "ai": {
    "evidence": [
      "README Credits explicitly names Claude Code (AI agent) as assisting with the porting process.",
      "Thirteen of the 30 most recent default-branch commits explicitly credit Claude Opus 4.7 (1M context); for example 4a77ae3fc58cbbddcbf14ad35bfc49df05f16953 and 04eb08d43bba453e1664ff0dadc33c346b7edd52. Claude is the normalized tool label; exact upstream wording is preserved here."
    ],
    "tools": [
      "Claude"
    ],
    "usage": true
  },
  "build": {
    "byte_exact": null,
    "compilable": null,
    "playable": null,
    "runnable": true
  },
  "display_title": "iDOpus — Directory Opus 5 Magellan modern desktop port",
  "id": "idopus-directory-opus-modern-port",
  "last_activity": "2026-04-27",
  "last_checked": "2026-10-11",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "C++",
    "Objective-C"
  ],
  "record_class": "subject",
  "repo": "https://github.com/bamsejon/idopus",
  "runtime_profiles": [
    {
      "cpu_family": "ARM",
      "evidence": [
        "https://github.com/bamsejon/idopus/blob/7ce1459a11c656f94c62dd8abe51b0bdfebca9ad/README.md",
        "https://github.com/bamsejon/idopus/blob/7ce1459a11c656f94c62dd8abe51b0bdfebca9ad/CMakeLists.txt"
      ],
      "min_cpu": "AArch64",
      "name": "Apple Silicon build",
      "notes": "README explicitly requires Apple Silicon (M1/M2/M3/M4). No minimum RAM stated.",
      "os": "macOS 13 Ventura or later",
      "platform": "macOS"
    },
    {
      "cpu_family": "x86",
      "evidence": [
        "https://github.com/bamsejon/idopus/blob/7ce1459a11c656f94c62dd8abe51b0bdfebca9ad/README.md"
      ],
      "min_cpu": "x86-64",
      "name": "Windows Qt build",
      "notes": "README documents x64 installer and MSVC/Qt build; no minimum RAM stated.",
      "os": "Windows 10 or 11",
      "platform": "Windows"
    }
  ],
  "source_cpu": [
    "m68000"
  ],
  "source_language": [
    "C",
    "m68000 assembly"
  ],
  "source_platforms": [
    "Amiga"
  ],
  "status": "Upstream-described daily-driver macOS file manager; Linux/Windows Qt builds implemented with feature parity still in progress.",
  "subjects": [
    "Directory Opus 5 Magellan"
  ],
  "tags": [
    "Amiga",
    "macOS",
    "Linux",
    "Windows"
  ],
  "target_cpu": [
    "AArch64",
    "x86-64"
  ],
  "target_kinds": [
    "application"
  ],
  "target_platforms": [
    "macOS",
    "Linux",
    "Windows"
  ],
  "techniques": [
    "reimplementation"
  ],
  "title": "iDOpus",
  "tool_kinds": [],
  "types": [
    "original-source-guided native port"
  ],
  "upstream_name": "iDOpus",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

iDOpus is a distinct modern source-guided implementation of Directory Opus 5 Magellan. It contains portable C core/PAL code, macOS AppKit UI and Linux/Windows Qt UI. src/core/dir_buffer.c concretely reproduces the original directory-buffer architecture, sorting and separation behavior. Keep the repository root.
- https://github.com/bamsejon/idopus/blob/7ce1459a11c656f94c62dd8abe51b0bdfebca9ad/README.md
- https://github.com/bamsejon/idopus/blob/7ce1459a11c656f94c62dd8abe51b0bdfebca9ad/src/core/dir_buffer.c
- https://github.com/bamsejon/idopus/blob/7ce1459a11c656f94c62dd8abe51b0bdfebca9ad/CMakeLists.txt

### Classification (reviewed)

This is a native, original-source-guided port/reimplementation, not binary decompilation or CPU emulation. README says Amiga subsystems are replaced with modern APIs; inspected CMake targets build portable libraries plus native platform UIs. The directory-buffer implementation explicitly follows the original buffers_sort.c shell-sort model.
- https://github.com/bamsejon/idopus/blob/7ce1459a11c656f94c62dd8abe51b0bdfebca9ad/README.md
- https://github.com/bamsejon/idopus/blob/7ce1459a11c656f94c62dd8abe51b0bdfebca9ad/src/core/dir_buffer.c
- https://github.com/bamsejon/idopus/blob/7ce1459a11c656f94c62dd8abe51b0bdfebca9ad/CMakeLists.txt

### Source CPU (reviewed)

The original source release README explicitly says Directory Opus 5.82 contains 68000 assembly alongside SAS/C source. iDOpus's README describes those 68K fragments being removed or rewritten in C. Store m68000 for that original Amiga codebase.
- https://github.com/MrZammler/opus_magellan/blob/ea0352c5573f1af748891f19f2b67be0b3c6d9a3/README.md
- https://github.com/bamsejon/idopus/blob/7ce1459a11c656f94c62dd8abe51b0bdfebca9ad/README.md

### Target CPU (reviewed)

CMake explicitly sets CMAKE_OSX_ARCHITECTURES=arm64 and the README specifies Apple Silicon. Windows instructions and installer target x64. Linux support is documented but its CPU is not pinned, so the target list contains only AArch64 and x86-64.
- https://github.com/bamsejon/idopus/blob/7ce1459a11c656f94c62dd8abe51b0bdfebca9ad/README.md
- https://github.com/bamsejon/idopus/blob/7ce1459a11c656f94c62dd8abe51b0bdfebca9ad/CMakeLists.txt

### Build (reviewed)

README describes the macOS output as a daily-driver file manager and supplies macOS/Windows release installation and launch instructions; Linux/Windows Qt feature parity is partial. This supports author-reported runnable=true. CMake source and commands alone were not used to claim a successful current clean rebuild, and compilable remains null; game playability and original-binary equality also remain null. Limitations: No dependency installation, compilation, launch, filesystem operation or binary comparison was performed. Feature claims are upstream descriptions; README matrix may lag more recent implementation commits.
- https://github.com/bamsejon/idopus/blob/7ce1459a11c656f94c62dd8abe51b0bdfebca9ad/README.md
- https://github.com/bamsejon/idopus/blob/7ce1459a11c656f94c62dd8abe51b0bdfebca9ad/CMakeLists.txt

### Runtime profiles (reviewed)

README specifies macOS 13+ on Apple Silicon and Windows 10/11 x64. Linux Qt 6.5+ is described without a CPU or OS-version minimum; no precise Linux hardware profile is invented. Neither documented desktop target has a stated minimum RAM.
- https://github.com/bamsejon/idopus/blob/7ce1459a11c656f94c62dd8abe51b0bdfebca9ad/README.md
- https://github.com/bamsejon/idopus/blob/7ce1459a11c656f94c62dd8abe51b0bdfebca9ad/CMakeLists.txt

### AI (reviewed)

README Credits explicitly identifies Claude Code (AI agent) as assisting with porting. Thirteen of the 30 latest default-branch commits also contain Co-Authored-By: Claude Opus 4.7 (1M context), including the Qt drag-and-drop implementation and Linux build documentation commits. The normalized Claude label is supported by actual named attribution; exact Claude Code and model wording are preserved in evidence. No tool label is inferred solely from an instruction-file name or provider email domain.
- https://github.com/bamsejon/idopus/blob/7ce1459a11c656f94c62dd8abe51b0bdfebca9ad/README.md
- https://github.com/bamsejon/idopus/commit/4a77ae3fc58cbbddcbf14ad35bfc49df05f16953
- https://github.com/bamsejon/idopus/commit/04eb08d43bba453e1664ff0dadc33c346b7edd52

### Relationships (reviewed)

README names MrZammler/opus_magellan's Directory Opus 5.82 APL release as the source lineage and keeps reference code under original-amiga-source. The ancestor README confirms Jonathan Potter/GP Software's 2012 release and SAS/C/68000 provenance. This modern implementation is independently scoped and differs materially from the source archive. It is unrelated to GP Software's separate commercial Directory Opus for Windows. Limitations: The author's clean-room wording is reported as source-guided porting, not independently certified legal provenance. APL source licensing and trademark restrictions are documented upstream.
- https://github.com/bamsejon/idopus/blob/7ce1459a11c656f94c62dd8abe51b0bdfebca9ad/README.md
- https://github.com/MrZammler/opus_magellan/blob/ea0352c5573f1af748891f19f2b67be0b3c6d9a3/README.md
- https://github.com/bamsejon/idopus/blob/7ce1459a11c656f94c62dd8abe51b0bdfebca9ad/src/core/dir_buffer.c

## Directory Opus 5.82 — original Amiga source archive

Project ID: directory-opus-582-original-amiga-source · Overall audit: reviewed

### Typed catalogue values

```json
{
  "ai": {
    "tools": [],
    "usage": null
  },
  "build": {
    "byte_exact": null,
    "compilable": null,
    "playable": null,
    "runnable": null
  },
  "display_title": "Directory Opus 5.82 — original Amiga source archive",
  "id": "directory-opus-582-original-amiga-source",
  "last_activity": "2013-08-05",
  "last_checked": "2026-10-11",
  "re_started": null,
  "reconstructed_languages": [],
  "record_class": "subject",
  "repo": "https://github.com/MrZammler/opus_magellan",
  "runtime_profiles": [],
  "source_cpu": [
    "m68000"
  ],
  "source_language": [
    "C",
    "m68000 assembly"
  ],
  "source_platforms": [
    "Amiga"
  ],
  "status": "Original 5.82 APL source archive with SAS/C makefiles; contemporary rebuild and runtime unverified.",
  "subjects": [
    "Directory Opus 5 Magellan"
  ],
  "tags": [
    "Amiga"
  ],
  "target_cpu": [
    "m68000"
  ],
  "target_kinds": [
    "application",
    "system-software"
  ],
  "target_platforms": [
    "Amiga"
  ],
  "techniques": [
    "source-restoration"
  ],
  "title": "Directory Opus 5.82",
  "tool_kinds": [],
  "types": [
    "original-source preservation"
  ],
  "upstream_name": "Directory Opus 5.82",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

README preserves Jonathan Potter/GP Software's release announcement dated 2012-11-29, identifying the last commercial release as Directory Opus 5.82. Program/main.c labels itself Original APL release version 5.82 and credits the original authors. Program, Library, Config and modules form one coherent period application/system archive, not independently split projects.
- https://github.com/MrZammler/opus_magellan/blob/ea0352c5573f1af748891f19f2b67be0b3c6d9a3/README.md
- https://github.com/MrZammler/opus_magellan/blob/ea0352c5573f1af748891f19f2b67be0b3c6d9a3/Program/main.c
- https://github.com/MrZammler/opus_magellan/blob/ea0352c5573f1af748891f19f2b67be0b3c6d9a3/Program/makefile

### Classification (reviewed)

This is original-source preservation/restoration of the substantial Amiga file-manager/desktop system. The reviewed startup implementation, 68000 routine and SAS/C link recipe are concrete original source artifacts. There is no evidence of binary-derived reconstruction, so it is not classified as decompilation.
- https://github.com/MrZammler/opus_magellan/blob/ea0352c5573f1af748891f19f2b67be0b3c6d9a3/README.md
- https://github.com/MrZammler/opus_magellan/blob/ea0352c5573f1af748891f19f2b67be0b3c6d9a3/Program/main.c
- https://github.com/MrZammler/opus_magellan/blob/ea0352c5573f1af748891f19f2b67be0b3c6d9a3/Program/rotate.asm
- https://github.com/MrZammler/opus_magellan/blob/ea0352c5573f1af748891f19f2b67be0b3c6d9a3/Program/makefile

### Source CPU (reviewed)

README explicitly states 68000 assembly is used, and Program/rotate.asm contains matching data/address registers and rotate/loop instructions. Source C includes SAS/C register annotations and Amiga ExecBase access. These establish the original m68000 codebase.
- https://github.com/MrZammler/opus_magellan/blob/ea0352c5573f1af748891f19f2b67be0b3c6d9a3/README.md
- https://github.com/MrZammler/opus_magellan/blob/ea0352c5573f1af748891f19f2b67be0b3c6d9a3/Program/rotate.asm
- https://github.com/MrZammler/opus_magellan/blob/ea0352c5573f1af748891f19f2b67be0b3c6d9a3/Program/main.c

### Target CPU (reviewed)

The preserved source and Program/makefile retain native Amiga SAS/C compilation, assembler invocation and slink output. README says non-68000 compilation would require converting the assembly. Thus the preserved build target is m68000; this is not a verified minimum runnable CPU.
- https://github.com/MrZammler/opus_magellan/blob/ea0352c5573f1af748891f19f2b67be0b3c6d9a3/README.md
- https://github.com/MrZammler/opus_magellan/blob/ea0352c5573f1af748891f19f2b67be0b3c6d9a3/Program/makefile
- https://github.com/MrZammler/opus_magellan/blob/ea0352c5573f1af748891f19f2b67be0b3c6d9a3/Program/rotate.asm

### Build (reviewed)

README reports that the historical commercial program was compiled with SAS/C 6. Program/makefile and scoptions preserve its compilation/link workflow for DOpus, DOpusRT5, LoadWB and dopusmsg. This does not prove that the current public snapshot can be cleanly rebuilt or run today, so all build flags remain null. Limitations: No compilation, execution, installer validation or comparison to the commercial binary was performed. The original development environment uses Amiga assigns and libraries that were not provisioned.
- https://github.com/MrZammler/opus_magellan/blob/ea0352c5573f1af748891f19f2b67be0b3c6d9a3/README.md
- https://github.com/MrZammler/opus_magellan/blob/ea0352c5573f1af748891f19f2b67be0b3c6d9a3/Program/makefile
- https://github.com/MrZammler/opus_magellan/blob/ea0352c5573f1af748891f19f2b67be0b3c6d9a3/Program/scoptions

### Runtime profiles (no-evidence-found)

The reviewed release note and source/build files establish Amiga/68000 development but do not state verified minimum runtime RAM, CPU variant or OS version for this archived output. No runtime profile is inferred from the compiler or the platform.
- https://github.com/MrZammler/opus_magellan/blob/ea0352c5573f1af748891f19f2b67be0b3c6d9a3/README.md
- https://github.com/MrZammler/opus_magellan/blob/ea0352c5573f1af748891f19f2b67be0b3c6d9a3/Program/makefile
- https://github.com/MrZammler/opus_magellan/blob/ea0352c5573f1af748891f19f2b67be0b3c6d9a3/Program/main.c

### AI (no-evidence-found)

The README, source/build files and sole initial commit were reviewed without explicit AI-development evidence. Usage remains null; historical dates alone are not used to infer a false value.
- https://github.com/MrZammler/opus_magellan/blob/ea0352c5573f1af748891f19f2b67be0b3c6d9a3/README.md
- https://github.com/MrZammler/opus_magellan/blob/ea0352c5573f1af748891f19f2b67be0b3c6d9a3/Program/main.c
- https://github.com/MrZammler/opus_magellan/blob/ea0352c5573f1af748891f19f2b67be0b3c6d9a3/Program/makefile
- https://github.com/MrZammler/opus_magellan/commit/ea0352c5573f1af748891f19f2b67be0b3c6d9a3

### Relationships (reviewed)

This is the original 5.82 APL source archive credited by the separately reviewed iDOpus modern port. The original release was enabled by the power2people bounty and names Jonathan Potter/GP Software. Catalogue root and Directory Opus/Magellan subject checks found no existing equivalent. The archive and modern native reimplementation warrant separate records with that lineage preserved.
- https://github.com/MrZammler/opus_magellan/blob/ea0352c5573f1af748891f19f2b67be0b3c6d9a3/README.md
- https://github.com/bamsejon/idopus/blob/7ce1459a11c656f94c62dd8abe51b0bdfebca9ad/README.md

## smonson-libtos: Atari ST TOS bindings and runtime library

Project ID: smonson-libtos-atari-st · Overall audit: partial

### Typed catalogue values

```json
{
  "ai": {
    "tools": [],
    "usage": null
  },
  "build": {
    "byte_exact": null,
    "compilable": null,
    "playable": null,
    "runnable": null
  },
  "display_title": "smonson-libtos: Atari ST TOS bindings and runtime library",
  "id": "smonson-libtos-atari-st",
  "last_activity": "2026-10-06",
  "last_checked": "2026-10-11",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "m68k assembly"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/smonson78/smonson-libtos",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Source reviewed; build and execution not independently verified",
  "subjects": [],
  "tags": [
    "Atari ST",
    "Atari TOS",
    "native development",
    "experimental"
  ],
  "target_cpu": [
    "m68000"
  ],
  "target_kinds": [],
  "target_platforms": [
    "Atari ST",
    "Atari TOS"
  ],
  "techniques": [],
  "title": "smonson-libtos: Atari ST TOS bindings and runtime library",
  "tool_kinds": [
    "compiler-toolchain",
    "development-environment"
  ],
  "types": [
    "native runtime library"
  ],
  "upstream_name": "smonson-libtos",
  "work_kinds": []
}
```

### Identity (reviewed)

The author's README identifies this as his own libtos for Atari ST projects and explicitly warns that it is incomplete and educational. The root forms a coherent C runtime and TOS/AES/BIOS/XBIOS/Line-A binding library; no recovered historical source provenance is claimed.
- https://github.com/smonson78/smonson-libtos/blob/01c5fda36202e3c5cfa71088fed4124629aa5cf7/README.md
- https://github.com/smonson78/smonson-libtos/blob/01c5fda36202e3c5cfa71088fed4124629aa5cf7/Makefile

### Classification (reviewed)

Retro-development infrastructure: tos.c implements native trap wrappers, and the Makefile collects system bindings, startup support and libc into libtos.a and optional libtos-dlmalloc.a. This is a library implementation, not a TOS ROM reconstruction or emulator.
- https://github.com/smonson78/smonson-libtos/blob/01c5fda36202e3c5cfa71088fed4124629aa5cf7/tos.c
- https://github.com/smonson78/smonson-libtos/blob/01c5fda36202e3c5cfa71088fed4124629aa5cf7/Makefile

### Source CPU (not-applicable)

No original executable is being analyzed or reconstructed in the inspected library; this is newly written system-call and runtime support, so an original-source CPU is not assigned.
- https://github.com/smonson78/smonson-libtos/blob/01c5fda36202e3c5cfa71088fed4124629aa5cf7/README.md
- https://github.com/smonson78/smonson-libtos/blob/01c5fda36202e3c5cfa71088fed4124629aa5cf7/tos.c

### Target CPU (reviewed)

Makefile explicitly passes -m68000 to m68k-elf-gcc. tos.c uses d0, a0-a2, the stack pointer and trap #1/#13/#14, independently corroborating native Motorola 68000-family output.
- https://github.com/smonson78/smonson-libtos/blob/01c5fda36202e3c5cfa71088fed4124629aa5cf7/Makefile
- https://github.com/smonson78/smonson-libtos/blob/01c5fda36202e3c5cfa71088fed4124629aa5cf7/tos.c

### Build (reviewed)

Makefile supplies builds for libtos.a and libtos-dlmalloc.a using m68k-elf-gcc/ar. The source is present, but the README's breakage warning and lack of a reproduced build leave all four build flags unknown. Limitations: No compile, linked test-program execution or byte comparison was performed.
- https://github.com/smonson78/smonson-libtos/blob/01c5fda36202e3c5cfa71088fed4124629aa5cf7/README.md
- https://github.com/smonson78/smonson-libtos/blob/01c5fda36202e3c5cfa71088fed4124629aa5cf7/Makefile

### Runtime profiles (not-applicable)

The inspected outputs are linkable archives rather than standalone runnable programs. The -m68000 compilation target does not establish RAM, TOS-version or minimum hardware requirements for applications that link this library.
- https://github.com/smonson78/smonson-libtos/blob/01c5fda36202e3c5cfa71088fed4124629aa5cf7/Makefile

### AI (no-evidence-found)

The root inventory, selected README/source/build files and latest ten commit messages were checked. No explicit generative-AI tool attribution was found; usage remains unknown. Limitations: Bounded review, not proof of non-use.
- https://github.com/smonson78/smonson-libtos/blob/01c5fda36202e3c5cfa71088fed4124629aa5cf7/README.md
- https://github.com/smonson78/smonson-libtos/commits/01c5fda36202e3c5cfa71088fed4124629aa5cf7

### Relationships (reviewed)

This library is distinct from the already tracked author's TOS 1.4 ROM disassembly. The earlier ataricc repository contains overlapping runtime/binding filenames plus a C++ GEM application/window/menu framework. That sibling was not counted as a second library record; its framework independence is retained for a separate lineage check.
- https://github.com/smonson78/smonson-libtos/blob/01c5fda36202e3c5cfa71088fed4124629aa5cf7/README.md
- https://github.com/smonson78/smonson-libtos/blob/01c5fda36202e3c5cfa71088fed4124629aa5cf7/Makefile
- https://github.com/smonson78/ataricc/blob/5aec0cb0409428616715eeb8097cb4f6f13f130f/app.cpp
- https://github.com/smonson78/ataricc/blob/5aec0cb0409428616715eeb8097cb4f6f13f130f/Makefile

## atari-libs: generated Atari TOS, AES and VDI C libraries

Project ID: atari-libs-hildenborg · Overall audit: partial

### Typed catalogue values

```json
{
  "ai": {
    "tools": [],
    "usage": null
  },
  "build": {
    "byte_exact": null,
    "compilable": null,
    "playable": null,
    "runnable": null
  },
  "display_title": "atari-libs: generated Atari TOS, AES and VDI C libraries",
  "id": "atari-libs-hildenborg",
  "last_activity": "2026-05-25",
  "last_checked": "2026-10-11",
  "re_started": null,
  "reconstructed_languages": [
    "Python",
    "C",
    "m68k assembly",
    "Shell"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/hildenborg/atari-libs",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Source reviewed; build and execution not independently verified",
  "subjects": [],
  "tags": [
    "Atari ST",
    "Atari TOS",
    "GEM",
    "native development"
  ],
  "target_cpu": [
    "m68k"
  ],
  "target_kinds": [],
  "target_platforms": [
    "Atari TOS",
    "Atari ST"
  ],
  "techniques": [
    "XML-driven binding generation"
  ],
  "title": "atari-libs: generated Atari TOS, AES and VDI C libraries",
  "tool_kinds": [
    "compiler-toolchain",
    "language-tooling"
  ],
  "types": [
    "generated native system libraries"
  ],
  "upstream_name": "atari-libs",
  "work_kinds": []
}
```

### Identity (reviewed)

README identifies system-specific C libraries for Atari 16/32-bit computers, generated from XML interface descriptions. The repository owns the specifications, Python generators, custom C implementations and library/test build scripts.
- https://github.com/hildenborg/atari-libs/blob/ceb9c530afb17d42fde71182e2797906b4db8674/README.md
- https://github.com/hildenborg/atari-libs/blob/ceb9c530afb17d42fde71182e2797906b4db8674/tos_gen.py
- https://github.com/hildenborg/atari-libs/blob/ceb9c530afb17d42fde71182e2797906b4db8674/build.sh

### Classification (reviewed)

Reusable native development tooling rather than binary-derived restoration: the generator emits TOS/AES/VDI declarations and wrappers, and makefile builds libtos.a, libaes.a and libvdi.a. tos_gen.py emits register/stack argument handling and native system traps.
- https://github.com/hildenborg/atari-libs/blob/ceb9c530afb17d42fde71182e2797906b4db8674/README.md
- https://github.com/hildenborg/atari-libs/blob/ceb9c530afb17d42fde71182e2797906b4db8674/makefile
- https://github.com/hildenborg/atari-libs/blob/ceb9c530afb17d42fde71182e2797906b4db8674/tos_gen.py

### Source CPU (not-applicable)

The reviewed material generates new library implementations from XML API definitions; no original historical executable or ROM is the analysis input.
- https://github.com/hildenborg/atari-libs/blob/ceb9c530afb17d42fde71182e2797906b4db8674/README.md
- https://github.com/hildenborg/atari-libs/blob/ceb9c530afb17d42fde71182e2797906b4db8674/tos_gen.py

### Target CPU (reviewed)

makefile selects m68k-atari-elf-gcc; tos_gen.py emits d0/a7 register operations, move.w/move.l and trap instructions. build.sh builds the toolchain's reported multilib variants, so only the evidenced m68k family is recorded, without claiming a specific minimum model.
- https://github.com/hildenborg/atari-libs/blob/ceb9c530afb17d42fde71182e2797906b4db8674/makefile
- https://github.com/hildenborg/atari-libs/blob/ceb9c530afb17d42fde71182e2797906b4db8674/tos_gen.py
- https://github.com/hildenborg/atari-libs/blob/ceb9c530afb17d42fde71182e2797906b4db8674/build.sh

### Build (reviewed)

README documents ./build.sh and python3 gen.py gen m68k-atari-elf, and reports extensive testing of common functions while warning that rarely used functions may be buggy. The scripts generate, compile and install three libraries, but no local build or tests were run. Limitations: Build, runnable and byte-exact facts stay unknown; source-generation and test instructions are not a reproduced pass.
- https://github.com/hildenborg/atari-libs/blob/ceb9c530afb17d42fde71182e2797906b4db8674/README.md
- https://github.com/hildenborg/atari-libs/blob/ceb9c530afb17d42fde71182e2797906b4db8674/build.sh
- https://github.com/hildenborg/atari-libs/blob/ceb9c530afb17d42fde71182e2797906b4db8674/makefile

### Runtime profiles (not-applicable)

These are libraries and a host-side generator, not a standalone Atari application. Target architecture and multilib flags do not establish a runtime minimum or required RAM for downstream programs.
- https://github.com/hildenborg/atari-libs/blob/ceb9c530afb17d42fde71182e2797906b4db8674/README.md
- https://github.com/hildenborg/atari-libs/blob/ceb9c530afb17d42fde71182e2797906b4db8674/build.sh

### AI (no-evidence-found)

Root/tree inventory, selected documentation, generators and build scripts plus latest ten commit messages contain no explicit generative-AI attribution. Usage remains unknown. Limitations: Automatic testing and mechanical XML code generation are not evidence of generative AI.
- https://github.com/hildenborg/atari-libs/blob/ceb9c530afb17d42fde71182e2797906b4db8674/README.md
- https://github.com/hildenborg/atari-libs/commits/ceb9c530afb17d42fde71182e2797906b4db8674

### Relationships (reviewed)

README explicitly states that the already tracked m68k-atari-dev builds and installs these libraries. This repository is a distinct reusable dependency with its own XML specification and generator source, not a mirror or second record of that compiler/debugger distribution.
- https://github.com/hildenborg/atari-libs/blob/ceb9c530afb17d42fde71182e2797906b4db8674/README.md
- https://github.com/hildenborg/m68k-atari-dev

## c64-misc: C64 raster tests, graphics routines and recovery tools

Project ID: c64-misc-ricardoquesada · Overall audit: partial

### Typed catalogue values

```json
{
  "ai": {
    "tools": [],
    "usage": null
  },
  "build": {
    "byte_exact": null,
    "compilable": null,
    "playable": null,
    "runnable": null
  },
  "display_title": "c64-misc: C64 raster tests, graphics routines and recovery tools",
  "id": "c64-misc-ricardoquesada",
  "last_activity": "2026-08-27",
  "last_checked": "2026-10-11",
  "re_started": null,
  "reconstructed_languages": [
    "6502 assembly",
    "Python"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/ricardoquesada/c64-misc",
  "runtime_profiles": [],
  "source_cpu": [
    "6502"
  ],
  "source_language": [
    "6502 machine code",
    "SID and Koala data"
  ],
  "source_platforms": [
    "Commodore 64"
  ],
  "status": "Source reviewed; build and execution not independently verified",
  "subjects": [],
  "tags": [
    "Commodore 64",
    "VIC-II",
    "SID",
    "PAL",
    "development routines"
  ],
  "target_cpu": [
    "MOS 6510"
  ],
  "target_kinds": [],
  "target_platforms": [
    "Commodore 64"
  ],
  "techniques": [
    "cycle-timed VIC-II test programs",
    "SID header and player analysis",
    "legacy disk file recovery"
  ],
  "title": "c64-misc: C64 raster tests, graphics routines and recovery tools",
  "tool_kinds": [
    "cycle-analysis",
    "binary-analysis",
    "asset-tool",
    "disk-filesystem-tool"
  ],
  "types": [
    "retro development and analysis toolkit"
  ],
  "upstream_name": "C= 64 misc",
  "work_kinds": [
    "binary-analysis",
    "data-format-analysis"
  ]
}
```

### Identity (reviewed)

The root README describes the author's reusable C64 tools and routines. Inspected source spans a VIC-II raster-test suite, native Koala graphics viewer, SID metadata/player inspection and a CBM2040 disk-file copier. The root is retained as one development/analysis collection rather than splitting each routine into a project.
- https://github.com/ricardoquesada/c64-misc/blob/8bd2e595400e80629dd0d380de798bafaffd8bbb/README.md
- https://github.com/ricardoquesada/c64-misc/blob/8bd2e595400e80629dd0d380de798bafaffd8bbb/vic_tricks/README.md
- https://github.com/ricardoquesada/c64-misc/blob/8bd2e595400e80629dd0d380de798bafaffd8bbb/viewers/koala.s
- https://github.com/ricardoquesada/c64-misc/blob/8bd2e595400e80629dd0d380de798bafaffd8bbb/tools/cbm2040_to_d64.py
- https://github.com/ricardoquesada/c64-misc/blob/8bd2e595400e80629dd0d380de798bafaffd8bbb/tools/sid_info.py

### Classification (reviewed)

The collection supplies actual native raster/video tests and graphics routines plus host-side analysis/recovery scripts. sid_info.py parses SID headers and recognizes SidTracker64 player instruction/variable layout; cbm2040_to_d64.py uses cbmctrl/cbmread/c1541 to copy legacy disk files into D64/D71 images. This is development and analysis tooling, not reconstruction of a complete historical game.
- https://github.com/ricardoquesada/c64-misc/blob/8bd2e595400e80629dd0d380de798bafaffd8bbb/tools/sid_info.py
- https://github.com/ricardoquesada/c64-misc/blob/8bd2e595400e80629dd0d380de798bafaffd8bbb/tools/cbm2040_to_d64.py
- https://github.com/ricardoquesada/c64-misc/blob/8bd2e595400e80629dd0d380de798bafaffd8bbb/vic_tricks/test_double_irq.asm

### Source CPU (reviewed)

The SID player analyzer explicitly describes and inspects JMP, LDX, JSR, LDA and STA sequences and little-endian instruction operands in a C64 SidTracker64 music payload. This supports a 6502-family analysis input; the disk and graphics data themselves are CPU-independent.
- https://github.com/ricardoquesada/c64-misc/blob/8bd2e595400e80629dd0d380de798bafaffd8bbb/tools/sid_info.py

### Target CPU (reviewed)

test_double_irq.asm explicitly names target Commodore 64 (MOS 6510 / 6569 PAL-B) and implements processor-port banking, raster interrupts and native 6502 instructions. The suite Makefile assembles PRGs with 64tass and selects the PAL C64/VIC-II 6569 model for x64sc.
- https://github.com/ricardoquesada/c64-misc/blob/8bd2e595400e80629dd0d380de798bafaffd8bbb/vic_tricks/test_double_irq.asm
- https://github.com/ricardoquesada/c64-misc/blob/8bd2e595400e80629dd0d380de798bafaffd8bbb/vic_tricks/Makefile

### Build (reviewed)

Root README names cc65 for the older routines; the VIC-II Makefile has 13 concrete 64tass PRG targets and a header/symbol-presence integrity check. Source and build recipes were inspected but not executed. Limitations: The test README retains stale eight-test claims/sample results while the current Makefile names 13 targets. Its production-grade/cycle-exact wording was not independently validated, so no blanket build or runtime success is asserted.
- https://github.com/ricardoquesada/c64-misc/blob/8bd2e595400e80629dd0d380de798bafaffd8bbb/README.md
- https://github.com/ricardoquesada/c64-misc/blob/8bd2e595400e80629dd0d380de798bafaffd8bbb/vic_tricks/Makefile
- https://github.com/ricardoquesada/c64-misc/blob/8bd2e595400e80629dd0d380de798bafaffd8bbb/vic_tricks/README.md

### Runtime profiles (no-evidence-found)

The inspected VIC-II sources document PAL/63-cycle timing and give a VICE launch command, but the collection mixes test programs, older routines and host Python tools. No verified minimum-hardware profile covering a named successfully reproduced output was established. Limitations: Do not infer collection-wide NTSC compatibility or RAM requirements from the platform. No emulator or physical hardware testing occurred.
- https://github.com/ricardoquesada/c64-misc/blob/8bd2e595400e80629dd0d380de798bafaffd8bbb/vic_tricks/test_double_irq.asm
- https://github.com/ricardoquesada/c64-misc/blob/8bd2e595400e80629dd0d380de798bafaffd8bbb/vic_tricks/README.md
- https://github.com/ricardoquesada/c64-misc/blob/8bd2e595400e80629dd0d380de798bafaffd8bbb/vic_tricks/Makefile

### AI (no-evidence-found)

Root/tree inventory, selected assembly/Python/documentation files and latest ten commit messages were inspected. None explicitly attributes development to a named generative-AI tool; usage remains unknown. Limitations: Writing style and project references do not establish AI usage.
- https://github.com/ricardoquesada/c64-misc/blob/8bd2e595400e80629dd0d380de798bafaffd8bbb/README.md
- https://github.com/ricardoquesada/c64-misc/blob/8bd2e595400e80629dd0d380de798bafaffd8bbb/vic_tricks/README.md
- https://github.com/ricardoquesada/c64-misc/commits/8bd2e595400e80629dd0d380de798bafaffd8bbb

### Relationships (reviewed)

The VIC-II README states that these tests support emulation accuracy and disassembly-pattern analysis for the already tracked Regenerator 2000. The repository also contains older independent reusable routines and recovery scripts; it is a separate supporting toolkit, not a mirror of that disassembler or of the author's tracked game disassemblies.
- https://github.com/ricardoquesada/c64-misc/blob/8bd2e595400e80629dd0d380de798bafaffd8bbb/README.md
- https://github.com/ricardoquesada/c64-misc/blob/8bd2e595400e80629dd0d380de798bafaffd8bbb/vic_tricks/README.md
- https://github.com/ricardoquesada/c64-misc/blob/8bd2e595400e80629dd0d380de798bafaffd8bbb/tools/cbm2040_to_d64.py

## 5plusbuttonsJoystick: C64 multibutton game patches and tester

Project ID: 5plusbuttonsjoystick-c64-software · Overall audit: partial

### Typed catalogue values

```json
{
  "ai": {
    "tools": [],
    "usage": null
  },
  "build": {
    "byte_exact": null,
    "compilable": null,
    "playable": null,
    "runnable": null
  },
  "display_title": "5plusbuttonsJoystick: C64 multibutton game patches and tester",
  "id": "5plusbuttonsjoystick-c64-software",
  "last_activity": "2026-08-08",
  "last_checked": "2026-10-11",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Python",
    "6502 machine code"
  ],
  "record_class": "hybrid",
  "repo": "https://github.com/crystalct/5plusbuttonsJoystick",
  "runtime_profiles": [],
  "source_cpu": [
    "6502"
  ],
  "source_language": [
    "6502 machine code"
  ],
  "source_platforms": [
    "Commodore 64"
  ],
  "status": "Source reviewed; build and execution not independently verified",
  "subjects": [
    "Impossible Mission 3",
    "Commando",
    "Wizball",
    "Turrican",
    "Turrican II"
  ],
  "tags": [
    "Commodore 64",
    "joystick",
    "native patches",
    "hardware companion software"
  ],
  "target_cpu": [
    "6502"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Commodore 64"
  ],
  "techniques": [
    "CRC32-guarded binary patching",
    "native control-input patching"
  ],
  "title": "5plusbuttonsJoystick: C64 multibutton game patches and tester",
  "tool_kinds": [
    "binary-analysis"
  ],
  "types": [
    "native game-control patches and hardware test utility"
  ],
  "upstream_name": "5plusbuttonsJoystick",
  "work_kinds": [
    "patching"
  ]
}
```

### Identity (reviewed)

The root hardware project includes creator-attributed C64 game-control modifications and an editable Joystick5plus1Test.c tester. Its Impossible Mission 3 component includes instructions, a Python patcher and a 170-byte native payload. This record covers the coherent software companion and authored patch work, not bare PCB fabrication files.
- https://github.com/crystalct/5plusbuttonsJoystick/blob/af9ab6661352acc4354a9adfe042991473c07eed/README.md
- https://github.com/crystalct/5plusbuttonsJoystick/blob/af9ab6661352acc4354a9adfe042991473c07eed/Joystick5plus1Test.c
- https://github.com/crystalct/5plusbuttonsJoystick/blob/af9ab6661352acc4354a9adfe042991473c07eed/IM3_2ndfirePatch/README.md
- https://github.com/crystalct/5plusbuttonsJoystick/blob/af9ab6661352acc4354a9adfe042991473c07eed/IM3_2ndfirePatch/patch.py

### Classification (reviewed)

Native C64 control patches and a development tester. The Impossible Mission 3 patcher checks input/payload CRC32 values, verifies three expected byte sequences, writes jump replacements and injects the payload. The root README separately attributes Commando, Wizball, Turrican and other patches to this author. No complete disassembly or source reconstruction is claimed.
- https://github.com/crystalct/5plusbuttonsJoystick/blob/af9ab6661352acc4354a9adfe042991473c07eed/README.md
- https://github.com/crystalct/5plusbuttonsJoystick/blob/af9ab6661352acc4354a9adfe042991473c07eed/IM3_2ndfirePatch/patch.py
- https://github.com/crystalct/5plusbuttonsJoystick/blob/af9ab6661352acc4354a9adfe042991473c07eed/Joystick5plus1Test.c

### Source CPU (reviewed)

The targeted C64 image patches use 6502 instructions: patch.py replaces 20 50 FD (JSR $FD50) with 4C 50 81 (JMP $8150), and other hooks use 4C and EA (JMP/NOP). The payload was statically inspected as bytes and begins 20 50 FD A2 99 BD 61 81 9D 3F 03 CA D0 F7, consistent with native 6502 code. A specific silicon revision is not inferred.
- https://github.com/crystalct/5plusbuttonsJoystick/blob/af9ab6661352acc4354a9adfe042991473c07eed/IM3_2ndfirePatch/patch.py
- https://github.com/crystalct/5plusbuttonsJoystick/blob/af9ab6661352acc4354a9adfe042991473c07eed/IM3_2ndfirePatch/IM3.patch

### Target CPU (reviewed)

The injected payload and replacement hook bytes are native 6502 instructions for the original C64 game image, rather than a host CPU emulator. The Python patcher and C tester do not establish any additional host CPU target.
- https://github.com/crystalct/5plusbuttonsJoystick/blob/af9ab6661352acc4354a9adfe042991473c07eed/IM3_2ndfirePatch/patch.py
- https://github.com/crystalct/5plusbuttonsJoystick/blob/af9ab6661352acc4354a9adfe042991473c07eed/IM3_2ndfirePatch/IM3.patch

### Build (reviewed)

The root distributes patched PRG/CRT/D64 artifacts and tester source/binary. Impossible Mission 3 instructions run VICE cartconv, python patch.py, then cartconv again against the user's own game image. Source and payload were inspected without compiling the tester, executing the patcher or playing patched binaries. Limitations: All build flags stay unknown. The payload is binary machine code rather than editable assembly source. Compatible input has CRC32 0x19176BAB; successful patching would intentionally change bytes, not establish original-byte identity.
- https://github.com/crystalct/5plusbuttonsJoystick/blob/af9ab6661352acc4354a9adfe042991473c07eed/README.md
- https://github.com/crystalct/5plusbuttonsJoystick/blob/af9ab6661352acc4354a9adfe042991473c07eed/IM3_2ndfirePatch/README.md
- https://github.com/crystalct/5plusbuttonsJoystick/blob/af9ab6661352acc4354a9adfe042991473c07eed/IM3_2ndfirePatch/patch.py

### Runtime profiles (no-evidence-found)

The documentation specifies C64 joystick-button behavior and warns that replacement SID devices with incompatible POTX/POTY behavior can cause unwanted jumping. It does not establish a tested minimum CPU/RAM or complete hardware-compatibility profile. Limitations: C64/VIC20/Amiga are mentioned for the physical joystick; that does not establish VIC20 or Amiga software targets for the inspected C64 patches.
- https://github.com/crystalct/5plusbuttonsJoystick/blob/af9ab6661352acc4354a9adfe042991473c07eed/README.md
- https://github.com/crystalct/5plusbuttonsJoystick/blob/af9ab6661352acc4354a9adfe042991473c07eed/IM3_2ndfirePatch/README.md

### AI (no-evidence-found)

Root/tree inventory, selected READMEs, C tester and Python patcher plus latest ten commit messages contain no explicit generative-AI attribution. Usage remains unknown. Limitations: Bounded inspection, not proof of non-use.
- https://github.com/crystalct/5plusbuttonsJoystick/blob/af9ab6661352acc4354a9adfe042991473c07eed/README.md
- https://github.com/crystalct/5plusbuttonsJoystick/blob/af9ab6661352acc4354a9adfe042991473c07eed/IM3_2ndfirePatch/patch.py
- https://github.com/crystalct/5plusbuttonsJoystick/commits/af9ab6661352acc4354a9adfe042991473c07eed

### Relationships (reviewed)

ricardoquesada/c64-games-unijoysticle links this repository as one source of its mixed patch collection. Here the creator specifically identifies his own modifications and supplies a concrete guarded patcher, so this is distinct authored software work; the downstream aggregation is not promoted. The nested Impossible Mission 3 patch remains evidence for this root control-modification project rather than a second record.
- https://github.com/crystalct/5plusbuttonsJoystick/blob/af9ab6661352acc4354a9adfe042991473c07eed/README.md
- https://github.com/crystalct/5plusbuttonsJoystick/blob/af9ab6661352acc4354a9adfe042991473c07eed/IM3_2ndfirePatch/README.md
- https://github.com/ricardoquesada/c64-games-unijoysticle/blob/main/README.md

## Sources

```json
[
  {
    "id": "github-codebase-amiga-game-kit",
    "kind": "github-repository",
    "reason": "Amiga Game Kit: native C game build pipeline, deterministic headless emulator tests, profiling and graphics/audio asset tools, with original examples.",
    "review_state": "partial",
    "source": "https://github.com/codebase/amiga-game-kit"
  },
  {
    "id": "github-askeksa-nocpuchallenge",
    "kind": "github-repository",
    "reason": "No-CPU Amiga challenge specification and native chip-memory demo runner, with source, executable and ZX0 decompression.",
    "review_state": "partial",
    "source": "https://github.com/askeksa/NoCpuChallenge"
  },
  {
    "id": "github-askeksa-nocpudemo",
    "kind": "github-repository",
    "reason": "No-CPU invitation demo, Dart framework, copper-list generation and ProTracker-to-custom-chip music conversion.",
    "review_state": "partial",
    "source": "https://github.com/askeksa/NoCpuDemo"
  },
  {
    "id": "github-futureretrofusion-mame106rgb",
    "kind": "github-repository",
    "reason": "MAME 0.106 Amiga display branch naming krabobmkd/amigamame as predecessor; compare implementation before assigning independent lineage.",
    "review_state": "partial",
    "source": "https://github.com/futureretrofusion/Mame106RGB"
  },
  {
    "first_indexed": "2026-10-11",
    "id": "github-jarskih-moonstone-ace-public",
    "kind": "github-repository",
    "last_reviewed": "2026-10-11",
    "open_task_ids": [],
    "projects_promoted": [
      "moonstone-ace-amiga-reconstruction"
    ],
    "reason": "Moonstone — native C++ reconstruction for Amiga 1200",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/Jarskih/moonstone-ace-public"
  },
  {
    "first_indexed": "2026-10-11",
    "id": "github-betajaen-goodsoup",
    "kind": "github-repository",
    "last_reviewed": "2026-10-11",
    "open_task_ids": [],
    "projects_promoted": [
      "goodsoup-comi-amiga-native-interpreter"
    ],
    "reason": "Goodsoup — Curse of Monkey Island native Amiga interpreter",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/betajaen/goodsoup"
  },
  {
    "first_indexed": "2026-10-11",
    "id": "github-alpyre-sevgi-engine",
    "kind": "github-repository",
    "last_reviewed": "2026-10-11",
    "open_task_ids": [],
    "projects_promoted": [
      "sevgi-amiga-game-engine-editor"
    ],
    "reason": "Sevgi Engine — native Amiga game engine and asset editor",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/alpyre/Sevgi_Engine"
  },
  {
    "first_indexed": "2026-10-11",
    "id": "github-bamsejon-idopus",
    "kind": "github-repository",
    "last_reviewed": "2026-10-11",
    "open_task_ids": [],
    "projects_promoted": [
      "idopus-directory-opus-modern-port"
    ],
    "reason": "iDOpus — Directory Opus 5 Magellan modern desktop port",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/bamsejon/idopus"
  },
  {
    "first_indexed": "2026-10-11",
    "id": "github-mrzammler-opus-magellan",
    "kind": "github-repository",
    "last_reviewed": "2026-10-11",
    "open_task_ids": [],
    "projects_promoted": [
      "directory-opus-582-original-amiga-source"
    ],
    "reason": "Directory Opus 5.82 — original Amiga source archive",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/MrZammler/opus_magellan"
  },
  {
    "first_indexed": "2026-10-11",
    "id": "github-smonson78-smonson-libtos",
    "kind": "github-repository",
    "last_reviewed": "2026-10-11",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "The author's README identifies this as his own libtos for Atari ST projects and explicitly warns that it is incomplete and educational. The root forms a coherent C runtime and TOS/AES/BIOS/XBIOS/Line-A binding library; no recovered historical source provenance is claimed.",
    "review_state": "partial",
    "source": "https://github.com/smonson78/smonson-libtos"
  },
  {
    "first_indexed": "2026-10-11",
    "id": "github-hildenborg-atari-libs",
    "kind": "github-repository",
    "last_reviewed": "2026-10-11",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "README identifies system-specific C libraries for Atari 16/32-bit computers, generated from XML interface descriptions. The repository owns the specifications, Python generators, custom C implementations and library/test build scripts.",
    "review_state": "partial",
    "source": "https://github.com/hildenborg/atari-libs"
  },
  {
    "first_indexed": "2026-10-11",
    "id": "github-ricardoquesada-c64-misc",
    "kind": "github-repository",
    "last_reviewed": "2026-10-11",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "The root README describes the author's reusable C64 tools and routines. Inspected source spans a VIC-II raster-test suite, native Koala graphics viewer, SID metadata/player inspection and a CBM2040 disk-file copier. The root is retained as one development/analysis collection rather than splitting each routine into a project.",
    "review_state": "partial",
    "source": "https://github.com/ricardoquesada/c64-misc"
  },
  {
    "first_indexed": "2026-10-11",
    "id": "github-crystalct-5plusbuttonsjoystick",
    "kind": "github-repository",
    "last_reviewed": "2026-10-11",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "The root hardware project includes creator-attributed C64 game-control modifications and an editable Joystick5plus1Test.c tester. Its Impossible Mission 3 component includes instructions, a Python patcher and a 170-byte native payload. This record covers the coherent software companion and authored patch work, not bare PCB fabrication files.",
    "review_state": "partial",
    "source": "https://github.com/crystalct/5plusbuttonsJoystick"
  }
]
```

## Tasks

```json
[
  {
    "description": "Compare Mame106RGB native display implementation and revision lineage with tracked MAME106 MiniMix before deciding whether a distinct branch record is warranted.",
    "id": "task-mame106rgb-compare-native-display-lineage",
    "notes": "Review amiga_video_ham6.cpp, five-mode switching and FRF91C3 changes against krabobmkd/amigamame; primary README and milestone reviewed 2026-10-11.",
    "priority": "normal",
    "source_ids": [
      "github-futureretrofusion-mame106rgb"
    ],
    "state": "open"
  },
  {
    "description": "Publish the evidence-reviewed Amiga Game Kit after separately resolving unsupported coding-agent attribution in the metadata updater.",
    "id": "task-agk-evidence-safe-ai-publication",
    "notes": "Native 68000 C/ACE output verified in tools/build; deterministic headless test, profiler and asset pipeline qualify. AI use is explicit for examples and Retro Diffusion assets, but CLAUDE.md only points to AGENTS.md and all 55 reviewed commit messages lack named coding-agent attribution. Current updater adds Claude by filename alone. Do not suppress all AI use or infer named authorship from integration support.",
    "priority": "normal",
    "source_ids": [
      "github-codebase-amiga-game-kit"
    ],
    "state": "open"
  },
  {
    "description": "Compare ataricc C++ GEM application/window/menu framework with smonson-libtos before deciding whether it warrants an independent project.",
    "id": "task-ataricc-gem-framework-lineage",
    "notes": "Inspected app.cpp and Makefile establish native 68000 work. Next inspect app_window.cpp and MenuBar.cpp plus historical relationship; overlapping TOS/runtime filenames must not produce a duplicate runtime record.",
    "priority": "normal",
    "source_ids": [
      "github-smonson78"
    ],
    "state": "open"
  }
]
```

## Decisions

```json
[
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/codebase/amiga-game-kit/blob/6acced96fd328458e074f6e303633866ce5dc5aa/README.md",
      "https://github.com/codebase/amiga-game-kit/blob/6acced96fd328458e074f6e303633866ce5dc5aa/templates/game/CMakeLists.txt",
      "https://github.com/codebase/amiga-game-kit/blob/6acced96fd328458e074f6e303633866ce5dc5aa/tools/build",
      "https://github.com/codebase/amiga-game-kit/blob/6acced96fd328458e074f6e303633866ce5dc5aa/harness/agk/profiles.py",
      "https://github.com/codebase/amiga-game-kit/blob/6acced96fd328458e074f6e303633866ce5dc5aa/CLAUDE.md",
      "https://github.com/codebase/amiga-game-kit/blob/6acced96fd328458e074f6e303633866ce5dc5aa/AGENTS.md",
      "https://github.com/rmtew/legacy-reverse-engineering-tracker/blob/c1613cac54ca1c39f1e567e76cfd30174dfd3cf1/tools/refresh_github.py#L330-L351"
    ],
    "id": "2026-10-11-focused-promote-amiga-game-kit-codebase",
    "project_ids": [],
    "reason": "Qualified native Amiga development toolkit, but catalogue promotion is deferred to preserve accurate AI attribution: primary README and commit 6acced96fd328458e074f6e303633866ce5dc5aa explicitly establish agent-built examples and Retro Diffusion art; all 55 available commit messages identify no specific coding-agent author. CLAUDE.md is only an @AGENTS.md pointer, and AGENTS.md documents generic workflow. The current tracker refresh_github.py update_ai_config would nevertheless append Claude solely from the filename. Review/fix that heuristic separately, then publish the researched toolkit with only supported AI labels. This is a publication-integrity blocker, not lack of project substance.",
    "source_ids": [
      "github-codebase-amiga-game-kit"
    ],
    "title": "Amiga Game Kit: native game build, test and asset pipeline",
    "url": "https://github.com/codebase/amiga-game-kit"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/askeksa/NoCpuChallenge/blob/c9a143fb8d31eff53d386ee51a46c96c71e983e5/README.md",
      "https://github.com/askeksa/NoCpuChallenge/blob/c9a143fb8d31eff53d386ee51a46c96c71e983e5/runner/README.md",
      "https://github.com/askeksa/NoCpuChallenge/blob/c9a143fb8d31eff53d386ee51a46c96c71e983e5/runner/Runner.S"
    ],
    "id": "2026-10-11-focused-promote-no-cpu-amiga-demo-runner",
    "project_ids": [
      "no-cpu-amiga-demo-runner"
    ],
    "reason": "Substantive native demo-development tooling, not rules alone: the launcher initializes hardware, loads/decompresses memory images and implements restart/restore behavior. The specification and launcher form one coherent root-scoped work.",
    "source_ids": [
      "github-askeksa-nocpuchallenge"
    ],
    "title": "No-CPU Amiga demo runner and platform specification",
    "url": "https://github.com/askeksa/NoCpuChallenge"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/askeksa/NoCpuDemo/blob/15c2b8d63677b861701b50f30f57f5f4529ee95a/README.md",
      "https://github.com/askeksa/NoCpuDemo/blob/15c2b8d63677b861701b50f30f57f5f4529ee95a/no_cpu/bin/main.dart"
    ],
    "id": "2026-10-11-focused-promote-no-cpu-amiga-demo-framework",
    "project_ids": [
      "no-cpu-amiga-demo-framework"
    ],
    "reason": "A substantial original Amiga demo and reusable authoring package form a coherent hybrid root entry. Dart code builds copperlists, display/blitter/sprite structures, music data and memory placement; it is not an emulator wrapper for an old game and is not a binary-only collection.",
    "source_ids": [
      "github-askeksa-nocpudemo"
    ],
    "title": "No-CPU Amiga invitation demo and Dart authoring framework",
    "url": "https://github.com/askeksa/NoCpuDemo"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/futureretrofusion/Mame106RGB/blob/4acbcfe213ff28d0065c7dbbe57efdd46a493b8c/README.md",
      "https://github.com/futureretrofusion/Mame106RGB/blob/4acbcfe213ff28d0065c7dbbe57efdd46a493b8c/docs/ORIGINAL_PROJECT_README.md",
      "https://github.com/futureretrofusion/Mame106RGB/blob/4acbcfe213ff28d0065c7dbbe57efdd46a493b8c/docs/KNOWN_GOOD_V91C3.md"
    ],
    "id": "2026-10-11-mame106rgb-lineage-review",
    "project_ids": [
      "mame106-minimix-amiga"
    ],
    "reason": "README and ORIGINAL_PROJECT_README identify a branch derived from the already tracked krabobmkd/amigamame. KNOWN_GOOD_V91C3 describes five-mode native screen handover work, but this pass has not compared amiga_video_ham6.cpp and mode-switch changes to the tracked predecessor to establish distinct contribution versus a source snapshot. Compare those implementation paths and revision lineage before promoting a second entry. This is a general emulator port, not a game-specific-wrapper exclusion.",
    "source_ids": [
      "github-futureretrofusion-mame106rgb"
    ],
    "title": "Mame106RGB native display branch",
    "url": "https://github.com/futureretrofusion/Mame106RGB"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/Jarskih/moonstone-ace-public/blob/2bc43a2e673819cc9c71a50a800e5676edcacfb3/README.md",
      "https://github.com/Jarskih/moonstone-ace-public/blob/2bc43a2e673819cc9c71a50a800e5676edcacfb3/src/engine/scenes.cpp",
      "https://github.com/Jarskih/moonstone-ace-public/blob/2bc43a2e673819cc9c71a50a800e5676edcacfb3/docs/PUBLISHING.md"
    ],
    "id": "2026-10-11-promote-moonstone-ace-amiga-reconstruction",
    "project_ids": [
      "moonstone-ace-amiga-reconstruction"
    ],
    "reason": "The repository contains one coherent reconstruction of Moonstone: A Hard Days Knight (Mindscape, 1991), including C++ gameplay, ACE runtime, original-data loaders and comparison tooling. README identifies original Amiga disks and the A1200 output. Keep one repository-root record. README and CLAUDE.md document a 68k-disassembly-to-C++ reconstruction. src/engine/scenes.cpp implements frame loops and scene bodies with explicit original program.asm label/line references. Architecture separates native runtime, engine services, game API and rules. The game has been all C++ since milestone 7.1r; the original ASM is not linked. The fight-script VM is game bytecode interpretation, and Unicorn is confined to testing.",
    "reviewed_at": "2026-10-11",
    "source_ids": [
      "github-jarskih-moonstone-ace-public"
    ],
    "title": "Moonstone — native C++ reconstruction for Amiga 1200",
    "url": "https://github.com/Jarskih/moonstone-ace-public"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/betajaen/goodsoup/blob/c2f3a202fa599eed6f85c0cfa906bed7e9126f00/README",
      "https://github.com/betajaen/goodsoup/blob/c2f3a202fa599eed6f85c0cfa906bed7e9126f00/source/goodsoup/script.cpp"
    ],
    "id": "2026-10-11-promote-goodsoup-comi-amiga-native-interpreter",
    "project_ids": [
      "goodsoup-comi-amiga-native-interpreter"
    ],
    "reason": "Robin Southern's Goodsoup is a single native Amiga interpreter/player project for The Curse of Monkey Island. README names the English GOG PC data and version 0.5; the repository has substantive C++ resource, VM, rendering and platform code. Link the repository root. The author identifies a partial fork and reimplementation of ScummVM 0.9.1 SCUMM v8 and NScumm. Reviewed script.cpp reads global/local/object-verb script resources with SCRP, LSCR, ENCD, EXCD and VERB handling; the makefile links dedicated VM, room, codec and SMUSH components. This qualifies at the demonstrated incomplete interpreter scope and does not emulate the original PC CPU.",
    "reviewed_at": "2026-10-11",
    "source_ids": [
      "github-betajaen-goodsoup"
    ],
    "title": "Goodsoup — Curse of Monkey Island native Amiga interpreter",
    "url": "https://github.com/betajaen/goodsoup"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/alpyre/Sevgi_Engine/blob/fcf1b2166351911d49baa6641cf7a359075721a2/README.md",
      "https://github.com/alpyre/Sevgi_Engine/blob/fcf1b2166351911d49baa6641cf7a359075721a2/tilemap_creator.c"
    ],
    "id": "2026-10-11-promote-sevgi-amiga-game-engine-editor",
    "project_ids": [
      "sevgi-amiga-game-engine-editor"
    ],
    "reason": "Sevgi Engine is a coherent original Amiga development toolkit comprising the native Sevgi Editor, generated game engine code, asset-conversion tools and genre templates. README and tilemap_creator.c establish substantive editor functionality; retain one repository-root record rather than splitting every generator. This is directly relevant retro-development tooling, with native game-engine boilerplate generation, asset management, palette/sprite/BOB/tile tools and template game projects. The inspected tilemap creator validates Tiled JSON and invokes the dedicated ConvertMap pipeline with project-specific game-object headers. No binary-derived reconstruction claim is made.",
    "reviewed_at": "2026-10-11",
    "source_ids": [
      "github-alpyre-sevgi-engine"
    ],
    "title": "Sevgi Engine — native Amiga game engine and asset editor",
    "url": "https://github.com/alpyre/Sevgi_Engine"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/bamsejon/idopus/blob/7ce1459a11c656f94c62dd8abe51b0bdfebca9ad/README.md",
      "https://github.com/bamsejon/idopus/blob/7ce1459a11c656f94c62dd8abe51b0bdfebca9ad/src/core/dir_buffer.c",
      "https://github.com/bamsejon/idopus/blob/7ce1459a11c656f94c62dd8abe51b0bdfebca9ad/CMakeLists.txt"
    ],
    "id": "2026-10-11-promote-idopus-directory-opus-modern-port",
    "project_ids": [
      "idopus-directory-opus-modern-port"
    ],
    "reason": "iDOpus is a distinct modern source-guided implementation of Directory Opus 5 Magellan. It contains portable C core/PAL code, macOS AppKit UI and Linux/Windows Qt UI. src/core/dir_buffer.c concretely reproduces the original directory-buffer architecture, sorting and separation behavior. Keep the repository root. This is a native, original-source-guided port/reimplementation, not binary decompilation or CPU emulation. README says Amiga subsystems are replaced with modern APIs; inspected CMake targets build portable libraries plus native platform UIs. The directory-buffer implementation explicitly follows the original buffers_sort.c shell-sort model.",
    "reviewed_at": "2026-10-11",
    "source_ids": [
      "github-bamsejon-idopus"
    ],
    "title": "iDOpus — Directory Opus 5 Magellan modern desktop port",
    "url": "https://github.com/bamsejon/idopus"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/MrZammler/opus_magellan/blob/ea0352c5573f1af748891f19f2b67be0b3c6d9a3/README.md",
      "https://github.com/MrZammler/opus_magellan/blob/ea0352c5573f1af748891f19f2b67be0b3c6d9a3/Program/main.c",
      "https://github.com/MrZammler/opus_magellan/blob/ea0352c5573f1af748891f19f2b67be0b3c6d9a3/Program/makefile"
    ],
    "id": "2026-10-11-promote-directory-opus-582-original-amiga-source",
    "project_ids": [
      "directory-opus-582-original-amiga-source"
    ],
    "reason": "README preserves Jonathan Potter/GP Software's release announcement dated 2012-11-29, identifying the last commercial release as Directory Opus 5.82. Program/main.c labels itself Original APL release version 5.82 and credits the original authors. Program, Library, Config and modules form one coherent period application/system archive, not independently split projects. This is original-source preservation/restoration of the substantial Amiga file-manager/desktop system. The reviewed startup implementation, 68000 routine and SAS/C link recipe are concrete original source artifacts. There is no evidence of binary-derived reconstruction, so it is not classified as decompilation.",
    "reviewed_at": "2026-10-11",
    "source_ids": [
      "github-mrzammler-opus-magellan"
    ],
    "title": "Directory Opus 5.82 — original Amiga source archive",
    "url": "https://github.com/MrZammler/opus_magellan"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/smonson78/smonson-libtos/blob/01c5fda36202e3c5cfa71088fed4124629aa5cf7/README.md",
      "https://github.com/smonson78/smonson-libtos/blob/01c5fda36202e3c5cfa71088fed4124629aa5cf7/Makefile"
    ],
    "id": "2026-10-11-promote-smonson-libtos-atari-st",
    "project_ids": [
      "smonson-libtos-atari-st"
    ],
    "reason": "The author's README identifies this as his own libtos for Atari ST projects and explicitly warns that it is incomplete and educational. The root forms a coherent C runtime and TOS/AES/BIOS/XBIOS/Line-A binding library; no recovered historical source provenance is claimed.",
    "reviewed_at": "2026-10-11",
    "source_ids": [
      "github-smonson78-smonson-libtos",
      "github-smonson78"
    ],
    "title": "smonson-libtos: Atari ST TOS bindings and runtime library",
    "url": "https://github.com/smonson78/smonson-libtos"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/hildenborg/atari-libs/blob/ceb9c530afb17d42fde71182e2797906b4db8674/README.md",
      "https://github.com/hildenborg/atari-libs/blob/ceb9c530afb17d42fde71182e2797906b4db8674/tos_gen.py",
      "https://github.com/hildenborg/atari-libs/blob/ceb9c530afb17d42fde71182e2797906b4db8674/build.sh"
    ],
    "id": "2026-10-11-promote-atari-libs-hildenborg",
    "project_ids": [
      "atari-libs-hildenborg"
    ],
    "reason": "README identifies system-specific C libraries for Atari 16/32-bit computers, generated from XML interface descriptions. The repository owns the specifications, Python generators, custom C implementations and library/test build scripts.",
    "reviewed_at": "2026-10-11",
    "source_ids": [
      "github-hildenborg-atari-libs",
      "fresh-m68k-atari-dev-hildenborg"
    ],
    "title": "atari-libs: generated Atari TOS, AES and VDI C libraries",
    "url": "https://github.com/hildenborg/atari-libs"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/ricardoquesada/c64-misc/blob/8bd2e595400e80629dd0d380de798bafaffd8bbb/README.md",
      "https://github.com/ricardoquesada/c64-misc/blob/8bd2e595400e80629dd0d380de798bafaffd8bbb/vic_tricks/README.md",
      "https://github.com/ricardoquesada/c64-misc/blob/8bd2e595400e80629dd0d380de798bafaffd8bbb/viewers/koala.s",
      "https://github.com/ricardoquesada/c64-misc/blob/8bd2e595400e80629dd0d380de798bafaffd8bbb/tools/cbm2040_to_d64.py",
      "https://github.com/ricardoquesada/c64-misc/blob/8bd2e595400e80629dd0d380de798bafaffd8bbb/tools/sid_info.py"
    ],
    "id": "2026-10-11-promote-c64-misc-ricardoquesada",
    "project_ids": [
      "c64-misc-ricardoquesada"
    ],
    "reason": "The root README describes the author's reusable C64 tools and routines. Inspected source spans a VIC-II raster-test suite, native Koala graphics viewer, SID metadata/player inspection and a CBM2040 disk-file copier. The root is retained as one development/analysis collection rather than splitting each routine into a project.",
    "reviewed_at": "2026-10-11",
    "source_ids": [
      "github-ricardoquesada-c64-misc",
      "github-ricardoquesada"
    ],
    "title": "c64-misc: C64 raster tests, graphics routines and recovery tools",
    "url": "https://github.com/ricardoquesada/c64-misc"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/crystalct/5plusbuttonsJoystick/blob/af9ab6661352acc4354a9adfe042991473c07eed/README.md",
      "https://github.com/crystalct/5plusbuttonsJoystick/blob/af9ab6661352acc4354a9adfe042991473c07eed/Joystick5plus1Test.c",
      "https://github.com/crystalct/5plusbuttonsJoystick/blob/af9ab6661352acc4354a9adfe042991473c07eed/IM3_2ndfirePatch/README.md",
      "https://github.com/crystalct/5plusbuttonsJoystick/blob/af9ab6661352acc4354a9adfe042991473c07eed/IM3_2ndfirePatch/patch.py"
    ],
    "id": "2026-10-11-promote-5plusbuttonsjoystick-c64-software",
    "project_ids": [
      "5plusbuttonsjoystick-c64-software"
    ],
    "reason": "The root hardware project includes creator-attributed C64 game-control modifications and an editable Joystick5plus1Test.c tester. Its Impossible Mission 3 component includes instructions, a Python patcher and a 170-byte native payload. This record covers the coherent software companion and authored patch work, not bare PCB fabrication files.",
    "reviewed_at": "2026-10-11",
    "source_ids": [
      "github-crystalct-5plusbuttonsjoystick"
    ],
    "title": "5plusbuttonsJoystick: C64 multibutton game patches and tester",
    "url": "https://github.com/crystalct/5plusbuttonsJoystick"
  },
  {
    "decision": "excluded",
    "evidence_urls": [
      "https://github.com/smonson78/atari-st-256k-rom/tree/main/H4"
    ],
    "id": "2026-10-11-exclude-st-256k-rom-hardware",
    "project_ids": [],
    "reason": "The complete recursive tree contains KiCad schematic/board/library files and fabrication outputs only. No ROM listing, firmware implementation or software recovery/development tool was found; the ROM wording refers to the physical board.",
    "reviewed_at": "2026-10-11",
    "source_ids": [
      "github-smonson78"
    ],
    "title": "Atari ST 256K ROM adapter board",
    "url": "https://github.com/smonson78/atari-st-256k-rom"
  },
  {
    "decision": "excluded",
    "evidence_urls": [
      "https://github.com/OldSkoolCoder/SpriteMateX/blob/main/README.md"
    ],
    "id": "2026-10-11-exclude-spritematex-c64-mismatch",
    "project_ids": [
      "github-esshahn-spritemate"
    ],
    "reason": "The README defines a Commander X16-specific editor derived from the already tracked Spritemate, says C64-specific code was commented out and SpritePad C64 import removed. A C64 palette option and ancestry do not establish C64 data-analysis/tool support. This specific lead is outside the historical-platform software scope; the C64 predecessor is already represented.",
    "reviewed_at": "2026-10-11",
    "source_ids": [
      "github-oldskoolcoder-c64-re"
    ],
    "title": "SpriteMateX Commander X16 editor",
    "url": "https://github.com/OldSkoolCoder/SpriteMateX"
  },
  {
    "decision": "excluded",
    "evidence_urls": [
      "https://github.com/ricardoquesada/c64-games-unijoysticle/blob/main/README.md",
      "https://github.com/ricardoquesada/c64-games-unijoysticle"
    ],
    "id": "2026-10-11-exclude-unijoysticle-game-aggregation",
    "project_ids": [
      "commando-c64",
      "lemans-c64-ricardoquesada",
      "rambo-c64-ricardoquesada",
      "5plusbuttonsjoystick-c64-software"
    ],
    "reason": "Root README and tree establish a binary collection mixing original C64GS games, CrystalCT modifications, Ricardo Quesada modifications and unidentified third parties, without component-specific source or analysis. The author's tracked Commando/Le Mans/Rambo work and newly reviewed CrystalCT control-patch root retain the demonstrated lineages; this aggregation adds no distinct reconstruction/tool contribution.",
    "reviewed_at": "2026-10-11",
    "source_ids": [
      "github-ricardoquesada"
    ],
    "title": "Unijoysticle enhanced C64 game aggregation",
    "url": "https://github.com/ricardoquesada/c64-games-unijoysticle"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/smonson78/ataricc/blob/5aec0cb0409428616715eeb8097cb4f6f13f130f/Makefile",
      "https://github.com/smonson78/ataricc/blob/5aec0cb0409428616715eeb8097cb4f6f13f130f/app.cpp",
      "https://github.com/smonson78/smonson-libtos"
    ],
    "id": "2026-10-11-defer-ataricc-framework-lineage",
    "project_ids": [
      "smonson-libtos-atari-st"
    ],
    "reason": "Makefile and app.cpp establish a native 68000 C++ GEM application/window/menu framework with bundled TOS/runtime files overlapping smonson-libtos. Do not add a second runtime-library record from filenames alone. Next check: compare app_window.cpp, MenuBar.cpp and full historical relationship to the newer standalone library, then decide whether the independent C++ framework warrants a separate record.",
    "reviewed_at": "2026-10-11",
    "source_ids": [
      "github-smonson78"
    ],
    "title": "ataricc native GEM application framework",
    "url": "https://github.com/smonson78/ataricc"
  },
  {
    "decision": "excluded",
    "evidence_urls": [
      "https://github.com/ricardoquesada/c64-pc-intro-amor-para-dos/blob/018e0b3fe8d5336dd656b5870256689898a8466d/README.md",
      "https://github.com/ricardoquesada/c64-pc-intro-amor-para-dos/blob/018e0b3fe8d5336dd656b5870256689898a8466d/c64/main.asm",
      "https://github.com/ricardoquesada/c64-pc-intro-amor-para-dos/blob/018e0b3fe8d5336dd656b5870256689898a8466d/dos/main.asm"
    ],
    "id": "2026-10-11-exclude-amor-para-dos-small-intro",
    "project_ids": [],
    "reason": "Primary README and assembly establish an original 256-byte intro whose same binary runs natively on C64 and 80386+ DOS; this is explicitly not an emulator wrapper. It is a very small one-effect demonstration rather than substantial homebrew, a reconstructed legacy title or reusable development tool, consistent with existing small-competition-demo exclusions. Its native polyglot technique remains a useful documented source lead.",
    "reviewed_at": "2026-10-11",
    "source_ids": [
      "github-ricardoquesada"
    ],
    "title": "Amor para Dos native C64/DOS polyglot intro",
    "url": "https://github.com/ricardoquesada/c64-pc-intro-amor-para-dos"
  },
  {
    "decision": "duplicate",
    "evidence_urls": [
      "https://github.com/8bitworkshop/8bitworkshop",
      "https://api.github.com/repos/sehugg/8bitworkshop",
      "https://github.com/8bitworkshop/8bitworkshop/blob/master/README.md"
    ],
    "id": "2026-10-11-duplicate-8bitworkshop-canonical-owner",
    "project_ids": [
      "8bitworkshop-retro-browser-ide"
    ],
    "reason": "GitHub repository lookup for the tracked sehugg/8bitworkshop URL resolves to repository ID 76608522 with canonical owner 8bitworkshop. This is the already tracked browser IDE moved to its organization, not a new project.",
    "reviewed_at": "2026-10-11",
    "source_ids": [
      "intake-sehugg-8bitworkshop"
    ],
    "title": "8bitworkshop canonical organization repository",
    "url": "https://github.com/8bitworkshop/8bitworkshop"
  },
  {
    "decision": "excluded",
    "evidence_urls": [
      "https://github.com/OldSkoolCoder/VSCode.C64.BackToBasic",
      "https://github.com/OldSkoolCoder/VSCode.C64.BackToBasic/blob/main/Sprites02.asm"
    ],
    "id": "2026-10-11-exclude-backtobasic-sprite-exercises",
    "project_ids": [],
    "reason": "Root inventory contains two sprite exercises, VIC-II constants, a memory diagram and VSCode workspace. Inspected Sprites02.asm shows a BASIC bootstrap and sprite data/example code, not a reconstructed historical subject or substantial reusable development-tool implementation. Retained as educational source rather than an independent project record.",
    "reviewed_at": "2026-10-11",
    "source_ids": [
      "github-oldskoolcoder-c64-re"
    ],
    "title": "C64 BackToBasic sprite examples",
    "url": "https://github.com/OldSkoolCoder/VSCode.C64.BackToBasic"
  }
]
```

## Research event notes

Amiga-first user-requested discovery pass. All candidate URLs screened against the 1,928-project baseline before detailed primary-source review. One coherent root entry per project; no game-specific CPU-emulation wrapper added. Build/runtime true values, where present, are explicitly attributed to upstream reports; no candidate was independently compiled or played. Current toolkit source, source/target CPU, runtime and lineage were inspected separately. Already-tracked Copperline, LegionGame, ACE, unsui, UNO and Spritemate were not duplicated; existing decisions were left intact. AGK qualifies but is held in reviewed backlog because the current metadata updater would add an unsupported Claude label from a filename alone. No schedules, tooling or unrelated code are changed.
