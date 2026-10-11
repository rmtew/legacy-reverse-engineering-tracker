# Third Amiga, Atari ST and C64 discovery pass

Add fourteen verified Amiga, Atari ST-family and C64/C128 projects

Date: 2026-10-11 · Review: ready

Snapshot check: all pinned proofs match the supplied expected commits.

## Uncertainty and next checks

- krypton-egg-native-go-reconstruction / Build (reviewed): No local compilation, tests, asset extraction, gameplay or Android-device run was performed. Upstream campaign completion is not independent verification or frame-exact equivalence; byte-exact remains unknown.
- krypton-egg-native-go-reconstruction / Runtime profiles (no-evidence-found): The reviewed README requires Go 1.26+ and a desktop graphics environment for development, while Android scripts configure an arm64/API-23 binding and the status describes an earlier Pixel 10a test. These build settings and one prior device observation do not establish a complete current runnable-hardware minimum; no RAM/CPU/chipset profile is asserted.
- krypton-egg-native-go-reconstruction / AI (no-evidence-found): The complete tree, five available recent commit messages, README, port-status/fidelity documents and selected Go/build files contain no explicit development-AI attribution. The deterministic expert player is game-testing logic and is not evidence of AI-assisted development; usage remains unknown.
- stunt-car-racer-amiga-track-toolkit / Build (reviewed): No project commands were run locally. Upstream CI cannot establish correctness for all proprietary disks, and full native geometry still depends on external table provenance.
- stunt-car-racer-amiga-track-toolkit / AI (no-evidence-found): The complete tree, all three available commit messages, README, package metadata, codec and inspected provenance/status documents disclose no actual development-AI assistance. Unknown is preserved; generated-looking documentation or tooling terminology is not evidence of AI use.
- symphonie-amiga-tracker-source-restoration / Build (reviewed): No local compilation, application execution, DSP test or binary comparison was performed; runnable, playable and byte-exact remain null.
- symphonie-amiga-tracker-source-restoration / Runtime profiles (no-evidence-found): The bundled English guide specifies MC680EC20+, 4 MB and OS 3.0+ for its documented Symphonie 2.4h release, with larger recommended memory for variants. The inspected main source is 3.3d. No evidence establishes that the older guide's minimum applies unchanged to this restored output, so no current runtime profile is copied from it.
- symphonie-amiga-tracker-source-restoration / AI (no-evidence-found): The complete tree, README, build script, original source/manual portions and five recent commit messages were checked. No explicit development-AI attribution was found; the 2015 activity date is not used to infer non-use.
- dbwrender-windows-source-port / Build (reviewed): No local Visual Studio build, render, viewer test or original-output comparison was performed. The published Windows release predates the latest project-file update.
- dbwrender-windows-source-port / Runtime profiles (no-evidence-found): The reviewed README, solution and project files establish Windows/x86 and a Visual Studio build path, but no supported minimum CPU generation, RAM or runtime Windows release. SDK/toolset settings are build dependencies and are not promoted into minimum hardware claims.
- dbwrender-windows-source-port / AI (no-evidence-found): The complete tree, five recent commit messages, README, source header/implementation and build project files reveal no explicit development-AI attribution. The latest commit changes the Visual Studio toolset, which alone establishes no AI involvement.
- super-methane-brothers-canonical-conversion / Build (reviewed): No local build, gameplay, input-recording validation or device test was performed. The native conversion and its replay checksums do not establish an original-Amiga byte-exact binary.
- super-methane-brothers-canonical-conversion / AI (no-evidence-found): The complete tree, five recent commit messages, README, authors/history, selected game source and build configuration were inspected without finding an explicit actual development-AI disclosure. Native input replay and automated state checksums are application/testing functionality, not AI-attribution evidence.
- godlib-atari-development-library / Build (reviewed): No compilation, linked application, unit test or byte comparison was run. Declared build targets and test files are not successful test results.
- godlib-atari-development-library / AI (no-evidence-found): The two root READMEs, complete tree, selected hardware/profiling/build source and latest 20 commit messages disclose no generative-AI use. Usage remains null.
- pack-ice-atari-compression-library / Target CPU (no-evidence-found): The Makefile uses ordinary gcc and ar without architecture selection, and the reviewed C codec is not an embedded CPU core. No specific output CPU or named host OS support matrix is established, so target_cpu and target_platforms are left empty.
- pack-ice-atari-compression-library / Build (reviewed): No build or fixture execution was performed. Fixture equality would validate selected codec cases, not byte-exact reconstruction of a historical executable; byte_exact remains null.
- pack-ice-atari-compression-library / Runtime profiles (no-evidence-found): The inspected README, build file and codec source supply no supported host CPU, RAM minimum or operating-system version. Portable-looking C and the Atari association are not used to invent runnable hardware requirements.
- pack-ice-atari-compression-library / AI (no-evidence-found): The complete tree, README/AUTHORS/HACKING, codec/build/test sources and latest 20 commits contain no explicit generative-AI attribution. The algorithmic look-ahead analysis is not AI-development evidence.
- udump-atari-tos-rom-preservation / Build (reviewed): No cross-compilation, execution, real-machine ROM capture or binary comparison was performed.
- udump-atari-tos-rom-preservation / Runtime profiles (no-evidence-found): README names ST/STE/TT/Falcon and the source selects TOS ROM sizes and CT60/EmuTOS variants, but it does not specify a complete minimum-memory or OS-version configuration. The 16 KiB transfer buffer and -m68000 flag do not establish a runtime minimum.
- udump-atari-tos-rom-preservation / AI (no-evidence-found): The full five-file inventory, README, C implementation, Makefile and all 12 returned commits show no explicit generative-AI development disclosure. Usage is unknown, including later maintenance of the historical code.
- rabenstein-daad-original-adventure / Target CPU (no-evidence-found): Target scripts compile a DAAD game database and combine it with external machine-specific interpreters. No interpreter assembly source or explicit CPU selection was verified in this game checkout. The platform targets are established, but target_cpu remains empty rather than inferring processor models from machine names.
- rabenstein-daad-original-adventure / Build (reviewed): No compilation, emulator launch, gameplay or byte comparison was performed. Released binaries are not proof that this archived source snapshot rebuilds without modification.
- rabenstein-daad-original-adventure / Runtime profiles (no-evidence-found): The source README and reviewed ST/Amiga scripts specify target machines and media but no verified minimum CPU, RAM or OS version. The creator page gives disk-loading instructions rather than complete ST/Amiga hardware minima; no runtime profile is inferred.
- rabenstein-daad-original-adventure / AI (no-evidence-found): The complete repository tree, creator README, game-source header and selected logic, three target scripts and both available commit messages contain no explicit AI-development disclosure. Usage remains null; historical dates alone do not prove non-use.
- jc64dis-java-retro-disassembler / Build (reviewed): No local compilation, native/JVM launch, emulator compatibility test or byte comparison was performed. Successful CI builds do not prove GUI/runtime correctness.
- jc64dis-java-retro-disassembler / Runtime profiles (no-evidence-found): The workflow and README establish Java/native host variants and qualitative performance cautions, but no verified minimum RAM, OS version or CPU generation for a runnable distribution. Guest 6510/Z80/8048 support is not a host minimum; no runtime profile is inferred.
- jc64dis-java-retro-disassembler / AI (no-evidence-found): The inspected DisassemblerAgent.java implements an OpenAI-compatible AI annotation feature and current release notes advertise AI labeling. This establishes a tool capability, not actual AI use in developing JC64dis. No explicit development-use disclosure or AI co-author attribution was found in README, inspected source/build files or the 30 reviewed commit messages; usage stays null.
- negentropy-c64-html-disassembler / Build (reviewed): No package installation, CLI execution, ACME build or output comparison was performed. The README still calls non-HTML templates incomplete.
- negentropy-c64-html-disassembler / Runtime profiles (no-evidence-found): Python 3 and named dependencies are documented. The inspected README, package metadata and CLI do not establish a minimum host CPU/RAM or an OS-specific runnable profile; none is inferred from the C64 input format.
- negentropy-c64-html-disassembler / AI (no-evidence-found): No explicit development-AI disclosure was found in the README, package metadata, inspected decoder/CLI files, complete tree inventory or the 30 reviewed commit messages. Python code and a missing disclosure do not establish non-use; usage stays null.
- nsshaft-native-c128-prototype / Source CPU (no-evidence-found): NS-Shaft is named as gameplay inspiration, but the inspected project does not identify an original binary or recovered source listing being translated. The original subject’s machine architecture and language are therefore left unknown rather than guessed from the new C128 target.
- nsshaft-native-c128-prototype / Build (reviewed): No assembly, Python regression suite, VICE execution, gameplay test or hardware test was run. README’s byte-identical macro-refactoring discussion does not establish identity with an original NS-Shaft binary.
- nsshaft-native-c128-prototype / Runtime profiles (reviewed): The documented hardware configuration was not independently exercised.
- nsshaft-native-c128-prototype / AI (no-evidence-found): README, inspected assembly/build/test/font files and the 13 visible default-branch commits contain no explicit development-AI attribution. Merged PR 4 uses a codex/docs-source-sync branch but has no description; a branch label alone does not establish actual Codex use. Usage remains null.
- nsshaft-native-c128-prototype / Relationships (reviewed): Original game/platform lineage and asset reuse permissions are not fully documented; no source-restoration or clean-room claim is made.
- the-race-c128-reconstruction / Build (reviewed): No compilation, resource export, emulator launch, gameplay or original-binary comparison was performed. The Makefile references resource-copy inputs not all present under res; corresponding generated .bin assets are committed under src, but the rebuild path was not exercised.
- the-race-c128-reconstruction / Runtime profiles (no-evidence-found): C128/C64 build targets and VIC/CIA usage are explicit, but the inspected README/build/source files do not specify a verified minimum RAM, PAL/NTSC compatibility or hardware configuration. No runtime profile is inferred from target names or packaged disk images.
- the-race-c128-reconstruction / AI (no-evidence-found): No explicit AI-development disclosure or AI co-author attribution was found in README, inspected assembly/Makefile or the 29 returned history entries. Historical dates alone are not proof of non-use; usage remains null.
- gorilla-cpm-modula2-port / Target CPU (no-evidence-found): The README specifies compiled CP/M-80 .COM output and names a Z80 emulator in the development credits, but the inspected Modula-2 modules do not establish a precise 8080-versus-Z80 output instruction requirement. Target CPU stays empty instead of inferring it solely from the C128 or CP/M platform labels.
- gorilla-cpm-modula2-port / Build (reviewed): No compiler invocation, boot, gameplay session or binary comparison was performed here. True flags describe documented upstream distribution/playability, not an independent test; byte_exact remains null.
- gorilla-cpm-modula2-port / Runtime profiles (no-evidence-found): The repository documents CP/M-80, named terminal variants and bootable C128/MTX/CPC distributions. xterm.mod implements C128 color and cursor sequences and fixed 80-column UI assumptions, but no verified minimum CPU/RAM or OS revision is given. No machine-minimum profile is inferred.
- gorilla-cpm-modula2-port / AI (no-evidence-found): No explicit development-AI disclosure was found in README, inspected Modula-2 modules, tree inventory or the 30 reviewed commit messages. Their historical dates do not establish non-use; usage stays null.

## Krypton Egg — native Go reconstruction

Project ID: krypton-egg-native-go-reconstruction · Overall audit: reviewed

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
    "playable": true,
    "runnable": true
  },
  "display_title": "Krypton Egg — native Go reconstruction",
  "execution_paths": [
    {
      "evidence": [
        "https://github.com/olivierh59500/krytonegg/blob/efe9ae43b29f77b8e6445f59dccab2a29f71801e/docs/port-status.md",
        "https://github.com/olivierh59500/krytonegg/blob/efe9ae43b29f77b8e6445f59dccab2a29f71801e/internal/game/physics.go"
      ],
      "method": "native-translation",
      "name": "Go/Ebitengine desktop and Android",
      "notes": "Upstream-reported native rewrite; original 68000 instructions are used for offline analysis only. Local ADF-derived assets required. No independent run in this review.",
      "status": "playable"
    }
  ],
  "id": "krypton-egg-native-go-reconstruction",
  "last_activity": "2026-10-07",
  "last_checked": "2026-10-11",
  "re_started": null,
  "reconstructed_languages": [
    "Go",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/olivierh59500/krytonegg",
  "runtime_profiles": [],
  "source_cpu": [
    "m68000"
  ],
  "source_language": [
    "68000 machine code",
    "game data"
  ],
  "source_platforms": [
    "Amiga"
  ],
  "status": "Native desktop and Android rewrite; upstream reports complete campaign; local ADF required",
  "subjects": [
    "Krypton Egg"
  ],
  "tags": [
    "Amiga",
    "source-reviewed",
    "native rewrite",
    "Ebitengine"
  ],
  "target_cpu": [
    "arm64"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Desktop",
    "Android"
  ],
  "techniques": [],
  "title": "Krypton Egg — Go / Ebitengine",
  "tool_kinds": [],
  "types": [
    "native game reconstruction",
    "original-data extraction"
  ],
  "upstream_name": "Krypton Egg — Go / Ebitengine",
  "work_kinds": [
    "reimplementation",
    "reverse-engineering-derived-port",
    "data-format-analysis"
  ]
}
```

### Identity (reviewed)

One coherent repository reconstructs HitSoft's Krypton Egg from a specified Amiga ADF, retaining 60 level layouts, six combats, recovered graphics and audio, and original-format custom levels. The original executable is used for offline investigation only.
- https://github.com/olivierh59500/krytonegg/blob/efe9ae43b29f77b8e6445f59dccab2a29f71801e/README.md
- https://github.com/olivierh59500/krytonegg/blob/efe9ae43b29f77b8e6445f59dccab2a29f71801e/docs/port-status.md

### Classification (reviewed)

This is a native Go/Ebitengine game rewrite derived from original-code and data analysis. The inspected physics.go implements ball motion and collision directly in Go. Port status explicitly says original instructions are neither executed nor interpreted at runtime; FS-UAE and Ghidra are offline reference tools, so this is not a game-specific CPU-emulation wrapper.
- https://github.com/olivierh59500/krytonegg/blob/efe9ae43b29f77b8e6445f59dccab2a29f71801e/docs/port-status.md
- https://github.com/olivierh59500/krytonegg/blob/efe9ae43b29f77b8e6445f59dccab2a29f71801e/internal/game/physics.go
- https://github.com/olivierh59500/krytonegg/blob/efe9ae43b29f77b8e6445f59dccab2a29f71801e/docs/fidelity-audit.md

### Source CPU (reviewed)

The fidelity audit identifies an Amiga 500 reference session and an extracted code hunk imported in Ghidra as 68000:BE:32:default. This establishes the original Motorola 68000 source architecture independently of the Go output.
- https://github.com/olivierh59500/krytonegg/blob/efe9ae43b29f77b8e6445f59dccab2a29f71801e/docs/fidelity-audit.md

### Target CPU (reviewed)

The Android environment script defaults to android/arm64 and the build script passes that value to ebitenmobile bind. Record arm64 for that concrete output; the generic desktop build does not establish an exhaustive host CPU list.
- https://github.com/olivierh59500/krytonegg/blob/efe9ae43b29f77b8e6445f59dccab2a29f71801e/scripts/android-env.sh
- https://github.com/olivierh59500/krytonegg/blob/efe9ae43b29f77b8e6445f59dccab2a29f71801e/scripts/build-android.sh

### Build (reviewed)

The README supplies asset-reconstruction, build, test, vet and native smoke commands, and the maintained status describes a complete input-driven 60-round/six-combat campaign. These explicit upstream reports support compilable/runnable/playable capability. A compatible user-owned ADF must regenerate ignored assets before building. The Android physical-device test predates the latest fidelity corrections. Limitations: No local compilation, tests, asset extraction, gameplay or Android-device run was performed. Upstream campaign completion is not independent verification or frame-exact equivalence; byte-exact remains unknown.
- https://github.com/olivierh59500/krytonegg/blob/efe9ae43b29f77b8e6445f59dccab2a29f71801e/README.md
- https://github.com/olivierh59500/krytonegg/blob/efe9ae43b29f77b8e6445f59dccab2a29f71801e/docs/port-status.md
- https://github.com/olivierh59500/krytonegg/blob/efe9ae43b29f77b8e6445f59dccab2a29f71801e/docs/validation.json
- https://github.com/olivierh59500/krytonegg/blob/efe9ae43b29f77b8e6445f59dccab2a29f71801e/Makefile

### Runtime profiles (no-evidence-found)

The reviewed README requires Go 1.26+ and a desktop graphics environment for development, while Android scripts configure an arm64/API-23 binding and the status describes an earlier Pixel 10a test. These build settings and one prior device observation do not establish a complete current runnable-hardware minimum; no RAM/CPU/chipset profile is asserted.
- https://github.com/olivierh59500/krytonegg/blob/efe9ae43b29f77b8e6445f59dccab2a29f71801e/README.md
- https://github.com/olivierh59500/krytonegg/blob/efe9ae43b29f77b8e6445f59dccab2a29f71801e/docs/port-status.md
- https://github.com/olivierh59500/krytonegg/blob/efe9ae43b29f77b8e6445f59dccab2a29f71801e/scripts/android-env.sh

### AI (no-evidence-found)

The complete tree, five available recent commit messages, README, port-status/fidelity documents and selected Go/build files contain no explicit development-AI attribution. The deterministic expert player is game-testing logic and is not evidence of AI-assisted development; usage remains unknown.
- https://github.com/olivierh59500/krytonegg/blob/efe9ae43b29f77b8e6445f59dccab2a29f71801e/README.md
- https://github.com/olivierh59500/krytonegg/blob/efe9ae43b29f77b8e6445f59dccab2a29f71801e/docs/port-status.md
- https://github.com/olivierh59500/krytonegg/commit/efe9ae43b29f77b8e6445f59dccab2a29f71801e
- https://github.com/olivierh59500/krytonegg/commit/1a7b6343f8e07a06832d7220c5be44b6729824f0
- https://github.com/olivierh59500/krytonegg/commit/4e03673c6501370f5682177baba3cbe1ff73dcab

### Relationships (reviewed)

The README credits HitSoft and the original Kral/Vidos/Deneyer team, Ebitengine for host presentation, and go-zikmu for module replay. It keeps the reference ADF and reconstructed assets out of Git; original asset ownership is retained. The modern collision solver and host audio deliberately adapt original behavior, and this reconstruction is distinct from later PC/mobile releases.
- https://github.com/olivierh59500/krytonegg/blob/efe9ae43b29f77b8e6445f59dccab2a29f71801e/README.md
- https://github.com/olivierh59500/krytonegg/blob/efe9ae43b29f77b8e6445f59dccab2a29f71801e/go.mod
- https://github.com/olivierh59500/krytonegg/blob/efe9ae43b29f77b8e6445f59dccab2a29f71801e/docs/fidelity-audit.md
- https://github.com/olivierh59500/krytonegg/blob/efe9ae43b29f77b8e6445f59dccab2a29f71801e/docs/port-status.md

## Stunt Car Racer — Amiga track analysis and editing toolkit

Project ID: stunt-car-racer-amiga-track-toolkit · Overall audit: reviewed

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
  "display_title": "Stunt Car Racer — Amiga track analysis and editing toolkit",
  "id": "stunt-car-racer-amiga-track-toolkit",
  "last_activity": "2026-10-01",
  "last_checked": "2026-10-11",
  "re_started": null,
  "reconstructed_languages": [
    "Python",
    "JavaScript"
  ],
  "record_class": "hybrid",
  "repo": "https://github.com/djayuffe/Amiga-stunt-car-racer-track-toolkit",
  "runtime_profiles": [],
  "source_cpu": [
    "m68000"
  ],
  "source_language": [
    "game data",
    "68000 machine code"
  ],
  "source_platforms": [
    "Amiga"
  ],
  "status": "804-byte track codec and guarded editing tools; exact mesh reconstruction remains bounded",
  "subjects": [
    "Stunt Car Racer"
  ],
  "tags": [
    "Amiga",
    "source-reviewed",
    "804-byte track format",
    "guarded patching"
  ],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Python hosts",
    "Web browser"
  ],
  "techniques": [],
  "title": "Amiga Stunt Car Racer Track Toolkit",
  "tool_kinds": [
    "asset-tool",
    "disk-filesystem-tool",
    "binary-analysis"
  ],
  "types": [
    "game-specific reverse-engineering toolkit"
  ],
  "upstream_name": "Amiga Stunt Car Racer Track Toolkit",
  "work_kinds": [
    "data-format-analysis",
    "binary-analysis",
    "patching"
  ]
}
```

### Identity (reviewed)

The root is an independent Stunt Car Racer Amiga research/toolkit project by Ulf Bertilsson. It combines installable Python commands, disk-evidence inspection, track codecs, guarded patch transactions, Blender import and a standalone browser inspector as one coherent project.
- https://github.com/djayuffe/amiga-stunt-car-racer-track-toolkit/blob/687701205d83b5e800a94549add1306ca9a5b30f/README.md
- https://github.com/djayuffe/amiga-stunt-car-racer-track-toolkit/blob/687701205d83b5e800a94549add1306ca9a5b30f/pyproject.toml

### Classification (reviewed)

The inspected track.py implements an 804-byte big-endian native track decoder/encoder with preservation of all 100 slots and an editor-native backing record. This materially combines game-data reconstruction with useful asset and disk-analysis tooling; it does not implement a playable game engine.
- https://github.com/djayuffe/amiga-stunt-car-racer-track-toolkit/blob/687701205d83b5e800a94549add1306ca9a5b30f/scrtool/track.py
- https://github.com/djayuffe/amiga-stunt-car-racer-track-toolkit/blob/687701205d83b5e800a94549add1306ca9a5b30f/docs/TRACK804_VERIFIED.md
- https://github.com/djayuffe/amiga-stunt-car-racer-track-toolkit/blob/687701205d83b5e800a94549add1306ca9a5b30f/README.md

### Source CPU (reviewed)

The README explicitly identifies the Amiga/Motorola 68000 source-game context. CPU metadata describes the investigated game, not the CPU on which the Python tools execute.
- https://github.com/djayuffe/amiga-stunt-car-racer-track-toolkit/blob/687701205d83b5e800a94549add1306ca9a5b30f/README.md
- https://github.com/djayuffe/amiga-stunt-car-racer-track-toolkit/blob/687701205d83b5e800a94549add1306ca9a5b30f/pyproject.toml

### Target CPU (not-applicable)

The inspected package targets Python 3.9+ hosts, with browser/Blender inspection helpers. No native CPU-specific game executable is generated; an empty target-CPU list avoids turning Python or the 68000 source-data format into a host architecture claim.
- https://github.com/djayuffe/amiga-stunt-car-racer-track-toolkit/blob/687701205d83b5e800a94549add1306ca9a5b30f/pyproject.toml
- https://github.com/djayuffe/amiga-stunt-car-racer-track-toolkit/blob/687701205d83b5e800a94549add1306ca9a5b30f/README.md
- https://github.com/djayuffe/amiga-stunt-car-racer-track-toolkit/blob/687701205d83b5e800a94549add1306ca9a5b30f/scrtool/track.py

### Build (reviewed)

The pinned head's GitHub CI completed successfully: it compiles Python sources, runs every tests/*.py script and installs the package under Python 3.12. The README documents CLI installation and use. Compilable/runnable describe this tested toolkit; playable is inapplicable and remains null. The no-op codec round-trip claim concerns an expanded resource, not byte-exact rebuilding of the original game binary. Limitations: No project commands were run locally. Upstream CI cannot establish correctness for all proprietary disks, and full native geometry still depends on external table provenance.
- https://github.com/djayuffe/amiga-stunt-car-racer-track-toolkit/blob/687701205d83b5e800a94549add1306ca9a5b30f/.github/workflows/ci.yml
- https://github.com/djayuffe/amiga-stunt-car-racer-track-toolkit/blob/687701205d83b5e800a94549add1306ca9a5b30f/pyproject.toml
- https://github.com/djayuffe/amiga-stunt-car-racer-track-toolkit/blob/687701205d83b5e800a94549add1306ca9a5b30f/docs/TRACK804_VERIFIED.md
- https://github.com/djayuffe/Amiga-stunt-car-racer-track-toolkit/actions/runs/36896180023

### Runtime profiles (not-applicable)

This is host-side analysis and editing software rather than a runnable Amiga reconstruction. Python >=3.9 is an interpreter dependency, not a verified legacy-machine minimum; no retro CPU/RAM/chipset profile applies.
- https://github.com/djayuffe/amiga-stunt-car-racer-track-toolkit/blob/687701205d83b5e800a94549add1306ca9a5b30f/pyproject.toml
- https://github.com/djayuffe/amiga-stunt-car-racer-track-toolkit/blob/687701205d83b5e800a94549add1306ca9a5b30f/README.md

### AI (no-evidence-found)

The complete tree, all three available commit messages, README, package metadata, codec and inspected provenance/status documents disclose no actual development-AI assistance. Unknown is preserved; generated-looking documentation or tooling terminology is not evidence of AI use.
- https://github.com/djayuffe/amiga-stunt-car-racer-track-toolkit/blob/687701205d83b5e800a94549add1306ca9a5b30f/README.md
- https://github.com/djayuffe/amiga-stunt-car-racer-track-toolkit/blob/687701205d83b5e800a94549add1306ca9a5b30f/docs/PROVENANCE_V4.md
- https://github.com/djayuffe/amiga-stunt-car-racer-track-toolkit/blob/687701205d83b5e800a94549add1306ca9a5b30f/scrtool/track.py
- https://github.com/djayuffe/Amiga-stunt-car-racer-track-toolkit/commit/687701205d83b5e800a94549add1306ca9a5b30f
- https://github.com/djayuffe/Amiga-stunt-car-racer-track-toolkit/commit/80bcc4a01e8e7c7cd2d1ec0976e18064c7b1185c
- https://github.com/djayuffe/Amiga-stunt-car-racer-track-toolkit/commit/36ce37f571281a07876a3948e947f52b4182157f

### Relationships (reviewed)

Provenance credits public Multi Stunt Car Track.cpp, a continuation of Stunt Car Remake, and Vesuri's labelled Amiga disassembly. The toolkit requires users to supply compatible source tables and legally obtained game media. Its current codec explicitly distinguishes the 804-byte expanded interchange format from compressed protected-disk streams; preview meshes are analysis aids, not a claim of fully exact native geometry.
- https://github.com/djayuffe/amiga-stunt-car-racer-track-toolkit/blob/687701205d83b5e800a94549add1306ca9a5b30f/docs/PROVENANCE_V4.md
- https://github.com/djayuffe/amiga-stunt-car-racer-track-toolkit/blob/687701205d83b5e800a94549add1306ca9a5b30f/docs/TRACK804_VERIFIED.md
- https://github.com/djayuffe/amiga-stunt-car-racer-track-toolkit/blob/687701205d83b5e800a94549add1306ca9a5b30f/README.md
- https://github.com/djayuffe/amiga-stunt-car-racer-track-toolkit/blob/687701205d83b5e800a94549add1306ca9a5b30f/docs/RE_STATUS.md

## Symphonie — Amiga music-tracker source restoration

Project ID: symphonie-amiga-tracker-source-restoration · Overall audit: reviewed

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
    "runnable": null
  },
  "display_title": "Symphonie — Amiga music-tracker source restoration",
  "id": "symphonie-amiga-tracker-source-restoration",
  "last_activity": "2015-10-03",
  "last_checked": "2026-10-11",
  "re_started": null,
  "reconstructed_languages": [
    "68020 assembly",
    "C"
  ],
  "record_class": "subject",
  "repo": "https://github.com/MastaTabs/Symphonie",
  "runtime_profiles": [],
  "source_cpu": [
    "m68020"
  ],
  "source_language": [
    "68020 assembly"
  ],
  "source_platforms": [
    "Amiga"
  ],
  "status": "Original tracker source made compilable upstream; current rebuild not independently tested",
  "subjects": [
    "Symphonie"
  ],
  "tags": [
    "Amiga",
    "source-reviewed",
    "music tracker",
    "68020"
  ],
  "target_cpu": [
    "m68020"
  ],
  "target_kinds": [
    "application"
  ],
  "target_platforms": [
    "Amiga"
  ],
  "techniques": [],
  "title": "Symphonie",
  "tool_kinds": [],
  "types": [
    "restored original application source"
  ],
  "upstream_name": "Symphonie",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

MastaTabs preserves and reorganizes Patrick Meng's Symphonie Amiga music-tracker source, plugin sources, manuals and historical binaries. The main assembly identifies version 3.3d, and the README describes the 256-channel tracker source as made compilable.
- https://github.com/mastatabs/symphonie/blob/c7d8854f9c9dafa9f74cb339838009072a20a404/README.md
- https://github.com/MastaTabs/Symphonie/blob/c7d8854f9c9dafa9f74cb339838009072a20a404/Symphonie%20Source.Assembler
- https://github.com/MastaTabs/Symphonie/blob/c7d8854f9c9dafa9f74cb339838009072a20a404/doc/Symphonie_E.guide

### Classification (reviewed)

This is restoration/preservation of original tracker application source with a modern assembler/linker build, rather than a decompilation. The main application, DSP plugins and old binaries belong to the same project root and are not split into separate catalogue records.
- https://github.com/mastatabs/symphonie/blob/c7d8854f9c9dafa9f74cb339838009072a20a404/build.sh
- https://github.com/MastaTabs/Symphonie/blob/c7d8854f9c9dafa9f74cb339838009072a20a404/Symphonie%20Source.Assembler
- https://github.com/MastaTabs/Symphonie/blob/c7d8854f9c9dafa9f74cb339838009072a20a404/doc/Symphonie_E.guide

### Source CPU (reviewed)

The original main source explicitly selects MC68020, and the English guide says Symphonie was written in modular 68020 assembler. The exact 68020 family member is therefore source-backed.
- https://github.com/MastaTabs/Symphonie/blob/c7d8854f9c9dafa9f74cb339838009072a20a404/Symphonie%20Source.Assembler
- https://github.com/MastaTabs/Symphonie/blob/c7d8854f9c9dafa9f74cb339838009072a20a404/doc/Symphonie_E.guide

### Target CPU (reviewed)

build.sh invokes vasmm68k_mot with -m68020 and links an Amiga Hunk output using vlink and the m68k-amigaos libraries. Its C helper is built with the vbcc aos68k target. This establishes a native 68020 output target independently of any runtime minimum.
- https://github.com/mastatabs/symphonie/blob/c7d8854f9c9dafa9f74cb339838009072a20a404/build.sh
- https://github.com/MastaTabs/Symphonie/blob/c7d8854f9c9dafa9f74cb339838009072a20a404/Symphonie%20Source.Assembler

### Build (reviewed)

The README explicitly claims the source was made compilable, supported by the checked-in vbcc/vasm/vlink build script and application source. Compilable records that upstream capability. The script assumes local NDK39 and VBCC paths, and merely storing historical executable files does not independently establish the current reconstruction as runnable or equivalent. Limitations: No local compilation, application execution, DSP test or binary comparison was performed; runnable, playable and byte-exact remain null.
- https://github.com/mastatabs/symphonie/blob/c7d8854f9c9dafa9f74cb339838009072a20a404/README.md
- https://github.com/mastatabs/symphonie/blob/c7d8854f9c9dafa9f74cb339838009072a20a404/build.sh
- https://github.com/MastaTabs/Symphonie/blob/c7d8854f9c9dafa9f74cb339838009072a20a404/Symphonie%20Source.Assembler

### Runtime profiles (no-evidence-found)

The bundled English guide specifies MC680EC20+, 4 MB and OS 3.0+ for its documented Symphonie 2.4h release, with larger recommended memory for variants. The inspected main source is 3.3d. No evidence establishes that the older guide's minimum applies unchanged to this restored output, so no current runtime profile is copied from it.
- https://github.com/mastatabs/symphonie/blob/c7d8854f9c9dafa9f74cb339838009072a20a404/build.sh
- https://github.com/MastaTabs/Symphonie/blob/c7d8854f9c9dafa9f74cb339838009072a20a404/doc/Symphonie_E.guide
- https://github.com/MastaTabs/Symphonie/blob/c7d8854f9c9dafa9f74cb339838009072a20a404/Symphonie%20Source.Assembler

### AI (no-evidence-found)

The complete tree, README, build script, original source/manual portions and five recent commit messages were checked. No explicit development-AI attribution was found; the 2015 activity date is not used to infer non-use.
- https://github.com/mastatabs/symphonie/blob/c7d8854f9c9dafa9f74cb339838009072a20a404/README.md
- https://github.com/mastatabs/symphonie/blob/c7d8854f9c9dafa9f74cb339838009072a20a404/build.sh
- https://github.com/MastaTabs/Symphonie/blob/c7d8854f9c9dafa9f74cb339838009072a20a404/Symphonie%20Source.Assembler
- https://github.com/MastaTabs/Symphonie/commit/c7d8854f9c9dafa9f74cb339838009072a20a404
- https://github.com/MastaTabs/Symphonie/commit/9476677effcb532c1ec0650476963d1730f0faf3

### Relationships (reviewed)

The guide credits Patrick Meng and manual contributor Michel Vissers and retains historical proprietary/shareware variant notices. The repository README links the Aminet Symphonie package; this is a third-party restoration rather than a claim that the maintainer authored the original tracker. No blanket open-source licence for the complete archive was established.
- https://github.com/mastatabs/symphonie/blob/c7d8854f9c9dafa9f74cb339838009072a20a404/README.md
- https://github.com/MastaTabs/Symphonie/blob/c7d8854f9c9dafa9f74cb339838009072a20a404/doc/Symphonie_E.guide
- https://github.com/MastaTabs/Symphonie/blob/c7d8854f9c9dafa9f74cb339838009072a20a404/Symphonie%20Source.Assembler

## DBW-Render — preserved Amiga ray-tracer Windows port

Project ID: dbwrender-windows-source-port · Overall audit: reviewed

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
  "display_title": "DBW-Render — preserved Amiga ray-tracer Windows port",
  "id": "dbwrender-windows-source-port",
  "last_activity": "2026-02-08",
  "last_checked": "2026-10-11",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "C++"
  ],
  "record_class": "subject",
  "repo": "https://github.com/DavidKinder/DBWRender",
  "runtime_profiles": [],
  "source_cpu": [
    "m68k",
    "x86"
  ],
  "source_language": [
    "C"
  ],
  "source_platforms": [
    "Amiga",
    "MS-DOS"
  ],
  "status": "Win32 ray tracer and rewritten image viewer; original Amiga lineage preserved",
  "subjects": [
    "DBW-Render"
  ],
  "tags": [
    "Amiga",
    "source-reviewed",
    "ray tracer",
    "source-derived port"
  ],
  "target_cpu": [
    "x86"
  ],
  "target_kinds": [
    "application"
  ],
  "target_platforms": [
    "Windows"
  ],
  "techniques": [],
  "title": "DBW-Render",
  "tool_kinds": [],
  "types": [
    "source-derived native application port"
  ],
  "upstream_name": "DBW-Render",
  "work_kinds": []
}
```

### Identity (reviewed)

David Kinder maintains a Windows port of David Wecker's DBW-Render, through John H. Lowery's MS-DOS adaptation. The root contains the C ray tracer, a rewritten C++ display application, scene files and build projects. The author traces the earlier history to DEC VAX and Amiga.
- https://github.com/davidkinder/dbwrender/blob/748886b74441d6734ec4ae21f1c81a06968ca369/README.md
- https://github.com/davidkinder/dbwrender/blob/748886b74441d6734ec4ae21f1c81a06968ca369/src/ray.c

### Classification (reviewed)

This is a source-derived native application port and preservation of a legacy ray tracer. The C source retains original 1987 attribution and the IBM-PC port history. No binary-derived decompilation or reverse-engineering methodology is asserted, so the work-kind list is left empty rather than mislabelling a source port.
- https://github.com/davidkinder/dbwrender/blob/748886b74441d6734ec4ae21f1c81a06968ca369/README.md
- https://github.com/davidkinder/dbwrender/blob/748886b74441d6734ec4ae21f1c81a06968ca369/src/ray.c

### Source CPU (reviewed)

The author identifies the Amiga A500 edition and the intervening MS-DOS port, while the C source header names the IBM-PC/VGA/MCGA adaptation. The catalogue records their broad m68k and x86 families; it does not invent an exact DOS CPU or a verified runtime minimum. Earlier DEC VAX history is contextual rather than another analysed binary target.
- https://github.com/davidkinder/dbwrender/blob/748886b74441d6734ec4ae21f1c81a06968ca369/README.md
- https://github.com/davidkinder/dbwrender/blob/748886b74441d6734ec4ae21f1c81a06968ca369/src/ray.c

### Target CPU (reviewed)

The Visual Studio solution explicitly defines Debug and Release x86 configurations mapped to Win32 projects. This establishes the produced Windows x86 architecture rather than assuming it from C/C++.
- https://github.com/davidkinder/dbwrender/blob/748886b74441d6734ec4ae21f1c81a06968ca369/src/DBWRender.sln
- https://github.com/davidkinder/dbwrender/blob/748886b74441d6734ec4ae21f1c81a06968ca369/src/ray.vcxproj
- https://github.com/davidkinder/dbwrender/blob/748886b74441d6734ec4ae21f1c81a06968ca369/src/display.vcxproj

### Build (reviewed)

The README gives Visual Studio build instructions and reports completed renders with timing comparisons; release r1 publishes the Windows renderer/viewer. These primary statements support compilable and runnable capability. The maintained source changes resolution and color depth and adds a new viewer, so an original-Amiga binary match is not claimed. Limitations: No local Visual Studio build, render, viewer test or original-output comparison was performed. The published Windows release predates the latest project-file update.
- https://github.com/davidkinder/dbwrender/blob/748886b74441d6734ec4ae21f1c81a06968ca369/README.md
- https://github.com/davidkinder/dbwrender/blob/748886b74441d6734ec4ae21f1c81a06968ca369/src/DBWRender.sln
- https://github.com/DavidKinder/DBWRender/releases/tag/r1

### Runtime profiles (no-evidence-found)

The reviewed README, solution and project files establish Windows/x86 and a Visual Studio build path, but no supported minimum CPU generation, RAM or runtime Windows release. SDK/toolset settings are build dependencies and are not promoted into minimum hardware claims.
- https://github.com/davidkinder/dbwrender/blob/748886b74441d6734ec4ae21f1c81a06968ca369/README.md
- https://github.com/davidkinder/dbwrender/blob/748886b74441d6734ec4ae21f1c81a06968ca369/src/DBWRender.sln
- https://github.com/davidkinder/dbwrender/blob/748886b74441d6734ec4ae21f1c81a06968ca369/src/ray.vcxproj

### AI (no-evidence-found)

The complete tree, five recent commit messages, README, source header/implementation and build project files reveal no explicit development-AI attribution. The latest commit changes the Visual Studio toolset, which alone establishes no AI involvement.
- https://github.com/davidkinder/dbwrender/blob/748886b74441d6734ec4ae21f1c81a06968ca369/README.md
- https://github.com/davidkinder/dbwrender/blob/748886b74441d6734ec4ae21f1c81a06968ca369/src/ray.c
- https://github.com/DavidKinder/DBWRender/commit/748886b74441d6734ec4ae21f1c81a06968ca369
- https://github.com/DavidKinder/DBWRender/commit/888be9dee0a31f6c10e316a24e25aded71aa66ba

### Relationships (reviewed)

The source header credits David Wecker and John H. Lowery, and the README explains Kinder's limited core changes and independently rewritten display utility. Release r1 also supplies the original Amiga disk image for historical context. All components remain one DBW-Render lineage; the source header refers to the bundled DBW_Render licence rather than asserting modern GPL terms.
- https://github.com/davidkinder/dbwrender/blob/748886b74441d6734ec4ae21f1c81a06968ca369/README.md
- https://github.com/davidkinder/dbwrender/blob/748886b74441d6734ec4ae21f1c81a06968ca369/src/ray.c
- https://github.com/DavidKinder/DBWRender/releases/tag/r1

## Super Methane Brothers — original-author native conversion

Project ID: super-methane-brothers-canonical-conversion · Overall audit: reviewed

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
    "playable": true,
    "runnable": true
  },
  "display_title": "Super Methane Brothers — original-author native conversion",
  "id": "super-methane-brothers-canonical-conversion",
  "last_activity": "2026-09-16",
  "last_checked": "2026-10-11",
  "re_started": null,
  "reconstructed_languages": [
    "C++",
    "C"
  ],
  "record_class": "subject",
  "repo": "https://github.com/rombust/Methane",
  "runtime_profiles": [
    {
      "evidence": [
        "https://github.com/rombust/Methane/blob/c1694b0e5cac5be4d9002984ac1a722691c47580/README.md",
        "https://github.com/rombust/Methane/blob/c1694b0e5cac5be4d9002984ac1a722691c47580/android/app/build.gradle.kts"
      ],
      "name": "Documented Android build",
      "notes": "README and Gradle declare arm64-v8a and x86_64 builds and Vulkan 1.1 rendering. No RAM minimum or device validation was established in this review.",
      "os": "Android 8.0 / API 26 or newer",
      "platform": "Android"
    }
  ],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [],
  "source_platforms": [
    "Amiga",
    "Amiga CD32"
  ],
  "status": "Canonical C++/Vulkan conversion for desktop and Android; v3.0.3 released",
  "subjects": [
    "Super Methane Brothers"
  ],
  "tags": [
    "Amiga",
    "source-reviewed",
    "original-author conversion",
    "Vulkan"
  ],
  "target_cpu": [
    "x86_64",
    "arm64"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Windows",
    "Linux",
    "Android"
  ],
  "techniques": [],
  "title": "Super Methane Brothers",
  "tool_kinds": [],
  "types": [
    "original-author native game conversion"
  ],
  "upstream_name": "Super Methane Brothers",
  "work_kinds": []
}
```

### Identity (reviewed)

The canonical repository publishes Super Methane Brothers for Linux, Windows and Android; authors.txt identifies maintainer Mark Page as the original Amiga game's programmer. The old SourceForge developer page links this GitHub root. Current source identifies v3.0.3, matching the October 2026 release.
- https://github.com/rombust/methane/blob/c1694b0e5cac5be4d9002984ac1a722691c47580/README.md
- https://github.com/rombust/methane/blob/c1694b0e5cac5be4d9002984ac1a722691c47580/authors.txt
- https://github.com/rombust/methane/blob/c1694b0e5cac5be4d9002984ac1a722691c47580/Sources/Game/game.cpp
- https://methane.sourceforge.net/develop.html
- https://github.com/rombust/Methane/releases/tag/v3.0.3

### Classification (reviewed)

This is the original programmer's native C++ game conversion, not evidence of a newly discovered assembly decompilation. The inspected game.cpp implements game state directly, and the CMake build links native game, platform and Vulkan sources. Keep all supported outputs under the canonical root and leave reconstruction-method enums empty rather than claiming unproven RE provenance.
- https://github.com/rombust/methane/blob/c1694b0e5cac5be4d9002984ac1a722691c47580/README.md
- https://github.com/rombust/methane/blob/c1694b0e5cac5be4d9002984ac1a722691c47580/Sources/Game/game.cpp
- https://github.com/rombust/methane/blob/c1694b0e5cac5be4d9002984ac1a722691c47580/CMakeLists.txt
- https://github.com/rombust/methane/blob/c1694b0e5cac5be4d9002984ac1a722691c47580/authors.txt

### Source CPU (reviewed)

Primary identity and history name the original Commodore Amiga game and later incorporation of CD32 animation/audio. Record the broad historical m68k family only; no exact original CPU minimum or original-source programming language is claimed from the C++ conversion.
- https://github.com/rombust/methane/blob/c1694b0e5cac5be4d9002984ac1a722691c47580/README.md
- https://github.com/rombust/methane/blob/c1694b0e5cac5be4d9002984ac1a722691c47580/history.txt
- https://github.com/rombust/methane/blob/c1694b0e5cac5be4d9002984ac1a722691c47580/authors.txt

### Target CPU (reviewed)

Windows presets explicitly select x64, and Android Gradle ABI filters select arm64-v8a and x86_64. Record x86_64 and arm64 for these documented outputs. The generic Linux architecture-handling code is not treated as proof that every detected architecture was tested.
- https://github.com/rombust/methane/blob/c1694b0e5cac5be4d9002984ac1a722691c47580/CMakePresets.json
- https://github.com/rombust/methane/blob/c1694b0e5cac5be4d9002984ac1a722691c47580/android/app/build.gradle.kts
- https://github.com/rombust/methane/blob/c1694b0e5cac5be4d9002984ac1a722691c47580/CMakeLists.txt

### Build (reviewed)

The current README documents Linux CMake, Visual Studio and Android Gradle builds plus keyboard, gamepad and touch play. Release v3.0.3 explicitly adds Android, while maintained source and release history establish an existing playable conversion. Compilable/runnable/playable reflect these upstream capabilities, not a local test result. Limitations: No local build, gameplay, input-recording validation or device test was performed. The native conversion and its replay checksums do not establish an original-Amiga byte-exact binary.
- https://github.com/rombust/methane/blob/c1694b0e5cac5be4d9002984ac1a722691c47580/README.md
- https://github.com/rombust/methane/blob/c1694b0e5cac5be4d9002984ac1a722691c47580/CMakeLists.txt
- https://github.com/rombust/methane/blob/c1694b0e5cac5be4d9002984ac1a722691c47580/Sources/Game/game.cpp
- https://github.com/rombust/Methane/releases/tag/v3.0.3

### Runtime profiles (reviewed)

The current README and Gradle configuration explicitly set Android 8.0/API 26 minimum and arm64-v8a/x86_64 ABIs, with Vulkan 1.1 rendering. One Android profile records those declared requirements. No RAM minimum or Windows/Linux minimum CPU/OS is established.
- https://github.com/rombust/methane/blob/c1694b0e5cac5be4d9002984ac1a722691c47580/README.md
- https://github.com/rombust/methane/blob/c1694b0e5cac5be4d9002984ac1a722691c47580/android/app/build.gradle.kts

### AI (no-evidence-found)

The complete tree, five recent commit messages, README, authors/history, selected game source and build configuration were inspected without finding an explicit actual development-AI disclosure. Native input replay and automated state checksums are application/testing functionality, not AI-attribution evidence.
- https://github.com/rombust/methane/blob/c1694b0e5cac5be4d9002984ac1a722691c47580/README.md
- https://github.com/rombust/methane/blob/c1694b0e5cac5be4d9002984ac1a722691c47580/authors.txt
- https://github.com/rombust/methane/blob/c1694b0e5cac5be4d9002984ac1a722691c47580/Sources/Game/game.cpp
- https://github.com/rombust/Methane/commit/c1694b0e5cac5be4d9002984ac1a722691c47580
- https://github.com/rombust/Methane/commit/5ee918169b7f63d5ea92593f47776d40882da738
- https://github.com/rombust/Methane/commit/e376262bb96e7e1f8e8f411bf790d956c84f25d9

### Relationships (reviewed)

The original programmer maintains this canonical conversion with original team credits and explicit Apache Software permission to license this conversion under GPL-2.0-or-later; the original Amiga release retains its separate commercial licence. ClanLib-derived portions have their own zlib-style licence. The separately reviewed carstene1ns homebrew tree is an older derivative with distinct console ports; it is not substituted for this canonical record or counted as a second independent reconstruction.
- https://github.com/rombust/methane/blob/c1694b0e5cac5be4d9002984ac1a722691c47580/README.md
- https://github.com/rombust/methane/blob/c1694b0e5cac5be4d9002984ac1a722691c47580/authors.txt
- https://github.com/carstene1ns/super-methane-brothers/blob/52d931fae033186d791331ad20fd1eb443421f6a/README.md
- https://github.com/carstene1ns/super-methane-brothers/blob/52d931fae033186d791331ad20fd1eb443421f6a/README
- https://methane.sourceforge.net/develop.html

## GODLIB — Atari ST native development and profiling library

Project ID: godlib-atari-development-library · Overall audit: reviewed

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
  "display_title": "GODLIB — Atari ST native development and profiling library",
  "github": {
    "archived": false,
    "checked_at": "2026-10-11",
    "created_at": "2015-02-01",
    "default_branch": "master",
    "fork": false,
    "latest_commit": {
      "date": "2025-07-01",
      "message": "Fast build bff build files for visual studio 2019 and 2022",
      "sha": "ae600aae192f35c8fe8a7e8164ec0e4caaa7e6e9",
      "url": "https://github.com/ReservoirGods/GODLIB/commit/ae600aae192f35c8fe8a7e8164ec0e4caaa7e6e9"
    },
    "primary_language": "C",
    "pushed_at": "2025-07-01",
    "repository": "ReservoirGods/GODLIB",
    "tracking_branch": "master",
    "tracking_path": null,
    "updated_at": "2026-07-09"
  },
  "id": "godlib-atari-development-library",
  "last_activity": "2025-07-01",
  "last_checked": "2026-10-11",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "m68k assembly"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/ReservoirGods/GODLIB",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Substantial C/68k library source; build configurations reviewed but untested",
  "subjects": [],
  "tags": [
    "Atari ST",
    "native development",
    "graphics",
    "audio",
    "profiling"
  ],
  "target_cpu": [
    "m68000"
  ],
  "target_kinds": [],
  "target_platforms": [
    "Atari ST",
    "Windows"
  ],
  "techniques": [
    "hardware-register integration",
    "interrupt-driven profiling"
  ],
  "title": "GODLIB",
  "tool_kinds": [
    "development-environment",
    "profiler",
    "asset-tool"
  ],
  "types": [
    "native development library"
  ],
  "upstream_name": "GODLIB",
  "work_kinds": []
}
```

### Identity (reviewed)

The root identifies GODLIB as an Atari ST development library. README.TXT credits Pink/RG as main coder and Evil/DHS, GGN, Sage and Scy/tSCc as contributors. The complete untruncated tree contains one coherent library covering graphics, audio, sprites, assets, storage, system bindings and profiling; its components are not counted as separate projects.
- https://github.com/ReservoirGods/GODLIB/blob/ae600aae192f35c8fe8a7e8164ec0e4caaa7e6e9/README.md
- https://github.com/ReservoirGods/GODLIB/blob/ae600aae192f35c8fe8a7e8164ec0e4caaa7e6e9/README.TXT
- https://github.com/ReservoirGods/GODLIB/blob/ae600aae192f35c8fe8a7e8164ec0e4caaa7e6e9/GODLIB.MAK

### Classification (reviewed)

Original native development infrastructure, rather than a recovered game or emulator. SYSTEM_S.S saves and restores hardware vectors and accesses Atari registers; PROFILER.C installs interrupt-based function profiling and records samples to PROFILE.PRO. This establishes concrete native development and profiling scope beyond the short README.
- https://github.com/ReservoirGods/GODLIB/blob/ae600aae192f35c8fe8a7e8164ec0e4caaa7e6e9/SYSTEM/SYSTEM_S.S
- https://github.com/ReservoirGods/GODLIB/blob/ae600aae192f35c8fe8a7e8164ec0e4caaa7e6e9/PROFILER/PROFILER.C
- https://github.com/ReservoirGods/GODLIB/blob/ae600aae192f35c8fe8a7e8164ec0e4caaa7e6e9/GODLIB.MAK

### Source CPU (not-applicable)

No historical input binary is being reconstructed in the inspected library. Its original C and assembly implementations are maintained development code; source_cpu remains empty rather than treating its native output architecture as an analysis input.
- https://github.com/ReservoirGods/GODLIB/blob/ae600aae192f35c8fe8a7e8164ec0e4caaa7e6e9/README.TXT
- https://github.com/ReservoirGods/GODLIB/blob/ae600aae192f35c8fe8a7e8164ec0e4caaa7e6e9/SYSTEM/SYSTEM_S.S

### Target CPU (reviewed)

The Atari build selects vasmm68k_mot/vlinkm68k and explicitly passes -m68000 to the assembler and -cpu=68000 to VBCC. The native source independently contains Motorola data/address registers and 68k instructions. Only m68000 is assigned: the Win32/SDL build is evidenced, but its host CPU is not inferred from Windows or general endianness macros.
- https://github.com/ReservoirGods/GODLIB/blob/ae600aae192f35c8fe8a7e8164ec0e4caaa7e6e9/MAKEFILE/PLATFORM/GODLIB_ST.MF
- https://github.com/ReservoirGods/GODLIB/blob/ae600aae192f35c8fe8a7e8164ec0e4caaa7e6e9/SYSTEM/SYSTEM_S.S
- https://github.com/ReservoirGods/GODLIB/blob/ae600aae192f35c8fe8a7e8164ec0e4caaa7e6e9/BASE/BASE.H
- https://github.com/ReservoirGods/GODLIB/blob/ae600aae192f35c8fe8a7e8164ec0e4caaa7e6e9/GODLIB.MAK

### Build (reviewed)

README.TXT documents installation into Pure C. The Atari make configuration provides VBCC/VASM/VLINK TOS output, while GODLIB.MAK builds a Win32/SDL static archive. Both contain environment-specific tool/include locations; the root has unit-test source but no inspected successful current build or test report. All build flags remain unknown. Limitations: No compilation, linked application, unit test or byte comparison was run. Declared build targets and test files are not successful test results.
- https://github.com/ReservoirGods/GODLIB/blob/ae600aae192f35c8fe8a7e8164ec0e4caaa7e6e9/README.TXT
- https://github.com/ReservoirGods/GODLIB/blob/ae600aae192f35c8fe8a7e8164ec0e4caaa7e6e9/MAKEFILE/PLATFORM/GODLIB_ST.MF
- https://github.com/ReservoirGods/GODLIB/blob/ae600aae192f35c8fe8a7e8164ec0e4caaa7e6e9/GODLIB.MAK

### Runtime profiles (not-applicable)

GODLIB is a library integrated into downstream programs. Its 68000 build setting is not a verified CPU/RAM minimum for every possible client, and the reviewed documentation does not define a standalone runtime profile.
- https://github.com/ReservoirGods/GODLIB/blob/ae600aae192f35c8fe8a7e8164ec0e4caaa7e6e9/README.TXT
- https://github.com/ReservoirGods/GODLIB/blob/ae600aae192f35c8fe8a7e8164ec0e4caaa7e6e9/MAKEFILE/PLATFORM/GODLIB_ST.MF

### AI (no-evidence-found)

The two root READMEs, complete tree, selected hardware/profiling/build source and latest 20 commit messages disclose no generative-AI use. Usage remains null.
- https://github.com/ReservoirGods/GODLIB/blob/ae600aae192f35c8fe8a7e8164ec0e4caaa7e6e9/README.md
- https://github.com/ReservoirGods/GODLIB/blob/ae600aae192f35c8fe8a7e8164ec0e4caaa7e6e9/README.TXT
- https://github.com/ReservoirGods/GODLIB/blob/ae600aae192f35c8fe8a7e8164ec0e4caaa7e6e9/SYSTEM/SYSTEM_S.S
- https://github.com/ReservoirGods/GODLIB/blob/ae600aae192f35c8fe8a7e8164ec0e4caaa7e6e9/PROFILER/PROFILER.C
- https://github.com/ReservoirGods/GODLIB/commits/ae600aae192f35c8fe8a7e8164ec0e4caaa7e6e9

### Relationships (reviewed)

Author credits and self-contained source identify the Reservoir Gods library as a distinct implementation from the separately tracked smonson-libtos and hildenborg atari-libs. Pure C, VBCC, VASM, VLINK and SDL are development dependencies or host backends, not additional GODLIB subjects. No separate record is proposed for each graphics, packer or profiler directory.
- https://github.com/ReservoirGods/GODLIB/blob/ae600aae192f35c8fe8a7e8164ec0e4caaa7e6e9/README.TXT
- https://github.com/ReservoirGods/GODLIB/blob/ae600aae192f35c8fe8a7e8164ec0e4caaa7e6e9/MAKEFILE/PLATFORM/GODLIB_ST.MF
- https://github.com/ReservoirGods/GODLIB/blob/ae600aae192f35c8fe8a7e8164ec0e4caaa7e6e9/GODLIB.MAK

## pack-ice — Atari ICE compression library and utilities

Project ID: pack-ice-atari-compression-library · Overall audit: reviewed

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
  "display_title": "pack-ice — Atari ICE compression library and utilities",
  "github": {
    "archived": false,
    "checked_at": "2026-10-11",
    "created_at": "2016-01-06",
    "default_branch": "master",
    "fork": false,
    "latest_commit": {
      "date": "2025-01-05",
      "message": "Fix error: implicit declaration of function ‘exit’",
      "sha": "1f7da1fe22aeada06770356ac70cc67b00256122",
      "url": "https://github.com/larsbrinkhoff/pack-ice/commit/1f7da1fe22aeada06770356ac70cc67b00256122"
    },
    "primary_language": "C",
    "pushed_at": "2025-01-05",
    "repository": "larsbrinkhoff/pack-ice",
    "tracking_branch": "master",
    "tracking_path": null,
    "updated_at": "2025-03-14"
  },
  "id": "pack-ice-atari-compression-library",
  "last_activity": "2025-01-05",
  "last_checked": "2026-10-11",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Shell"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/larsbrinkhoff/pack-ice",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [
    "ICE compressed data"
  ],
  "source_platforms": [
    "Atari ST"
  ],
  "status": "C encoder/decoder with algorithm notes and regression fixtures; tests not run",
  "subjects": [],
  "tags": [
    "Atari ST",
    "ICE",
    "compression",
    "file formats"
  ],
  "target_cpu": [],
  "target_kinds": [],
  "target_platforms": [],
  "techniques": [
    "bitstream decoding",
    "look-ahead compression analysis"
  ],
  "title": "pack-ice",
  "tool_kinds": [
    "asset-tool"
  ],
  "types": [
    "legacy-format compression tooling"
  ],
  "upstream_name": "pack-ice",
  "work_kinds": []
}
```

### Identity (reviewed)

README identifies pack-ice as an Atari ST compression utility and AUTHORS names Lars Brinkhoff. The root contains libice encoder/decoder source and the icecat, freeze and melt front ends, plus format analysis and six fixture pairs. These form a single codec/tool project.
- https://github.com/larsbrinkhoff/pack-ice/blob/1f7da1fe22aeada06770356ac70cc67b00256122/README
- https://github.com/larsbrinkhoff/pack-ice/blob/1f7da1fe22aeada06770356ac70cc67b00256122/AUTHORS
- https://github.com/larsbrinkhoff/pack-ice/blob/1f7da1fe22aeada06770356ac70cc67b00256122/Makefile
- https://github.com/larsbrinkhoff/pack-ice/blob/1f7da1fe22aeada06770356ac70cc67b00256122/HACKING
- https://github.com/larsbrinkhoff/pack-ice/blob/1f7da1fe22aeada06770356ac70cc67b00256122/testcases/README

### Classification (reviewed)

Directly useful legacy-format tooling: ice_crunch.c and ice_decrunch.c implement variable-length copy/back-reference bitstreams, while HACKING analyzes encoding costs and competing compression choices. It is a C implementation of the ICE format; the inspected material does not establish binary-derived decompilation or original Pack-Ice source provenance, so no such work kind is asserted.
- https://github.com/larsbrinkhoff/pack-ice/blob/1f7da1fe22aeada06770356ac70cc67b00256122/ice_crunch.c
- https://github.com/larsbrinkhoff/pack-ice/blob/1f7da1fe22aeada06770356ac70cc67b00256122/ice_decrunch.c
- https://github.com/larsbrinkhoff/pack-ice/blob/1f7da1fe22aeada06770356ac70cc67b00256122/HACKING

### Source CPU (not-applicable)

The input is an ICE-compressed byte stream, not a CPU instruction stream. Historical Atari ST use establishes platform relevance but does not establish an original CPU under analysis; source_cpu remains empty.
- https://github.com/larsbrinkhoff/pack-ice/blob/1f7da1fe22aeada06770356ac70cc67b00256122/README
- https://github.com/larsbrinkhoff/pack-ice/blob/1f7da1fe22aeada06770356ac70cc67b00256122/ice_decrunch.c
- https://github.com/larsbrinkhoff/pack-ice/blob/1f7da1fe22aeada06770356ac70cc67b00256122/HACKING

### Target CPU (no-evidence-found)

The Makefile uses ordinary gcc and ar without architecture selection, and the reviewed C codec is not an embedded CPU core. No specific output CPU or named host OS support matrix is established, so target_cpu and target_platforms are left empty.
- https://github.com/larsbrinkhoff/pack-ice/blob/1f7da1fe22aeada06770356ac70cc67b00256122/Makefile
- https://github.com/larsbrinkhoff/pack-ice/blob/1f7da1fe22aeada06770356ac70cc67b00256122/ice_crunch.c
- https://github.com/larsbrinkhoff/pack-ice/blob/1f7da1fe22aeada06770356ac70cc67b00256122/ice_decrunch.c

### Build (reviewed)

The Makefile builds libice.a and three command-line tools and provides make check. testcases/check compares generated compressed fixtures and decompressed round trips, but prints failures without an aggregate nonzero exit status. testcases/README flags fixture 005 as problematic for the current compressor; the optional new algorithm is disabled in ice_crunch.c. No current pass is claimed. Limitations: No build or fixture execution was performed. Fixture equality would validate selected codec cases, not byte-exact reconstruction of a historical executable; byte_exact remains null.
- https://github.com/larsbrinkhoff/pack-ice/blob/1f7da1fe22aeada06770356ac70cc67b00256122/Makefile
- https://github.com/larsbrinkhoff/pack-ice/blob/1f7da1fe22aeada06770356ac70cc67b00256122/testcases/check
- https://github.com/larsbrinkhoff/pack-ice/blob/1f7da1fe22aeada06770356ac70cc67b00256122/testcases/README
- https://github.com/larsbrinkhoff/pack-ice/blob/1f7da1fe22aeada06770356ac70cc67b00256122/ice_crunch.c

### Runtime profiles (no-evidence-found)

The inspected README, build file and codec source supply no supported host CPU, RAM minimum or operating-system version. Portable-looking C and the Atari association are not used to invent runnable hardware requirements.
- https://github.com/larsbrinkhoff/pack-ice/blob/1f7da1fe22aeada06770356ac70cc67b00256122/README
- https://github.com/larsbrinkhoff/pack-ice/blob/1f7da1fe22aeada06770356ac70cc67b00256122/Makefile
- https://github.com/larsbrinkhoff/pack-ice/blob/1f7da1fe22aeada06770356ac70cc67b00256122/ice_decrunch.c

### AI (no-evidence-found)

The complete tree, README/AUTHORS/HACKING, codec/build/test sources and latest 20 commits contain no explicit generative-AI attribution. The algorithmic look-ahead analysis is not AI-development evidence.
- https://github.com/larsbrinkhoff/pack-ice/blob/1f7da1fe22aeada06770356ac70cc67b00256122/AUTHORS
- https://github.com/larsbrinkhoff/pack-ice/blob/1f7da1fe22aeada06770356ac70cc67b00256122/HACKING
- https://github.com/larsbrinkhoff/pack-ice/blob/1f7da1fe22aeada06770356ac70cc67b00256122/ice_crunch.c
- https://github.com/larsbrinkhoff/pack-ice/commits/1f7da1fe22aeada06770356ac70cc67b00256122

### Relationships (reviewed)

The inspected repository is its own Lars Brinkhoff codec implementation, not a fork according to repository metadata. It is distinct from the already catalogued multi-format Ancient decompressor and L-Packer executable tool. Encoder, decoder, front ends and fixture suite stay together under the root; no unverified claim is made about derivation from Axel Brok/Pack-Ice assembly source.
- https://github.com/larsbrinkhoff/pack-ice/blob/1f7da1fe22aeada06770356ac70cc67b00256122/AUTHORS
- https://github.com/larsbrinkhoff/pack-ice/blob/1f7da1fe22aeada06770356ac70cc67b00256122/README
- https://github.com/larsbrinkhoff/pack-ice/blob/1f7da1fe22aeada06770356ac70cc67b00256122/Makefile
- https://github.com/larsbrinkhoff/pack-ice/blob/1f7da1fe22aeada06770356ac70cc67b00256122/ice_decrunch.c

## uDump — native Atari TOS ROM dumper

Project ID: udump-atari-tos-rom-preservation · Overall audit: reviewed

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
  "display_title": "uDump — native Atari TOS ROM dumper",
  "github": {
    "archived": false,
    "checked_at": "2026-10-11",
    "created_at": "2018-07-05",
    "default_branch": "master",
    "fork": false,
    "latest_commit": {
      "date": "2025-05-19",
      "message": "This is 1.03 release",
      "sha": "11c7ff9492f51918d07251b000133bf9bd12d6bf",
      "url": "https://github.com/mikrosk/uDump/commit/11c7ff9492f51918d07251b000133bf9bd12d6bf"
    },
    "latest_release": {
      "name": "uDump 1.03",
      "published_at": "2025-05-19",
      "tag": "1.03",
      "url": "https://github.com/mikrosk/uDump/releases/tag/1.03"
    },
    "primary_language": "C",
    "pushed_at": "2025-05-19",
    "repository": "mikrosk/uDump",
    "tracking_branch": "master",
    "tracking_path": null,
    "updated_at": "2025-12-16"
  },
  "id": "udump-atari-tos-rom-preservation",
  "last_activity": "2025-05-19",
  "last_checked": "2026-10-11",
  "re_started": null,
  "reconstructed_languages": [
    "C"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/mikrosk/uDump",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [
    "TOS ROM images"
  ],
  "source_platforms": [
    "Atari ST",
    "Atari STE",
    "Atari TT",
    "Atari Falcon"
  ],
  "status": "Creator-released TOS ROM dumper v1.03; native build untested",
  "subjects": [],
  "tags": [
    "Atari ST",
    "Atari TOS",
    "ROM preservation",
    "EmuTOS"
  ],
  "target_cpu": [
    "m68000"
  ],
  "target_kinds": [],
  "target_platforms": [
    "Atari ST",
    "Atari STE",
    "Atari TT",
    "Atari Falcon"
  ],
  "techniques": [],
  "title": "uDump",
  "tool_kinds": [
    "rom-tool"
  ],
  "types": [
    "ROM preservation utility"
  ],
  "upstream_name": "uDump",
  "work_kinds": []
}
```

### Identity (reviewed)

Miro Kropacek/MiKRO identifies uDump 1.03 as a TOS ROM dumping utility for ST, STE, TT and Falcon. The entire five-file tree contains its C implementation, build recipe, author README and license; this is the canonical non-fork repository.
- https://github.com/mikrosk/uDump/blob/11c7ff9492f51918d07251b000133bf9bd12d6bf/README.txt
- https://github.com/mikrosk/uDump/blob/11c7ff9492f51918d07251b000133bf9bd12d6bf/udump.c

### Classification (reviewed)

A native preservation tool that obtains the TOS header, identifies version/country and machine cookies, selects ROM size and writes a named image. It handles EmuTOS and CT60 cases and copies ROM through a bounded buffer to avoid a documented extra-read bus error. It does not reconstruct or emulate TOS execution.
- https://github.com/mikrosk/uDump/blob/11c7ff9492f51918d07251b000133bf9bd12d6bf/udump.c

### Source CPU (not-applicable)

uDump copies ROM bytes and parses header/cookie metadata rather than disassembling or interpreting the captured instructions. The ROM platform is recorded, but no original CPU analysis is claimed.
- https://github.com/mikrosk/uDump/blob/11c7ff9492f51918d07251b000133bf9bd12d6bf/udump.c

### Target CPU (reviewed)

Makefile uses m68k-atari-mint-gcc with explicit -m68000 and links libcmini startup/runtime into udump.tos. This establishes a native Motorola 68000 target without implying that all supported Atari models have the same minimum RAM or firmware.
- https://github.com/mikrosk/uDump/blob/11c7ff9492f51918d07251b000133bf9bd12d6bf/Makefile

### Build (reviewed)

The Makefile declares a libcmini-based native .tos build. The creator publishes a uDump 1.03 binary archive and earlier release notes explicitly discuss the distributed executable; runnable=true records that released utility, not a local run. The current source build was not reproduced, so compilable remains null and no gameplay or historical byte-match claim is made. Limitations: No cross-compilation, execution, real-machine ROM capture or binary comparison was performed.
- https://github.com/mikrosk/uDump/blob/11c7ff9492f51918d07251b000133bf9bd12d6bf/README.txt
- https://github.com/mikrosk/uDump/blob/11c7ff9492f51918d07251b000133bf9bd12d6bf/Makefile
- https://github.com/mikrosk/uDump/releases/tag/1.03
- https://github.com/mikrosk/uDump/releases/tag/1.01

### Runtime profiles (no-evidence-found)

README names ST/STE/TT/Falcon and the source selects TOS ROM sizes and CT60/EmuTOS variants, but it does not specify a complete minimum-memory or OS-version configuration. The 16 KiB transfer buffer and -m68000 flag do not establish a runtime minimum.
- https://github.com/mikrosk/uDump/blob/11c7ff9492f51918d07251b000133bf9bd12d6bf/README.txt
- https://github.com/mikrosk/uDump/blob/11c7ff9492f51918d07251b000133bf9bd12d6bf/Makefile
- https://github.com/mikrosk/uDump/blob/11c7ff9492f51918d07251b000133bf9bd12d6bf/udump.c

### AI (no-evidence-found)

The full five-file inventory, README, C implementation, Makefile and all 12 returned commits show no explicit generative-AI development disclosure. Usage is unknown, including later maintenance of the historical code.
- https://github.com/mikrosk/uDump/blob/11c7ff9492f51918d07251b000133bf9bd12d6bf/README.txt
- https://github.com/mikrosk/uDump/blob/11c7ff9492f51918d07251b000133bf9bd12d6bf/udump.c
- https://github.com/mikrosk/uDump/commits/11c7ff9492f51918d07251b000133bf9bd12d6bf

### Relationships (reviewed)

uDump depends on libcmini and m68k-atari-mint system bindings; it is a separate focused application, not a duplicate runtime-library or TOS-reconstruction record. Its TOS/EmuTOS/CT60 support describes the data captured and machine handling, not ownership or reimplementation of those systems.
- https://github.com/mikrosk/uDump/blob/11c7ff9492f51918d07251b000133bf9bd12d6bf/Makefile
- https://github.com/mikrosk/uDump/blob/11c7ff9492f51918d07251b000133bf9bd12d6bf/udump.c

## The Curse of Rabenstein — original multi-platform DAAD adventure

Project ID: rabenstein-daad-original-adventure · Overall audit: reviewed

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
    "playable": true,
    "runnable": true
  },
  "display_title": "The Curse of Rabenstein — original multi-platform DAAD adventure",
  "github": {
    "archived": false,
    "checked_at": "2026-10-11",
    "created_at": "2020-06-02",
    "default_branch": "master",
    "fork": false,
    "latest_commit": {
      "date": "2020-06-02",
      "message": "fixing readme file",
      "sha": "8fec1f400bbfcb317dbdc8c7a77789fb781492dc",
      "url": "https://github.com/ByteProject/Rabenstein/commit/8fec1f400bbfcb317dbdc8c7a77789fb781492dc"
    },
    "primary_language": "Shell",
    "pushed_at": "2020-06-02",
    "repository": "ByteProject/Rabenstein",
    "tracking_branch": "master",
    "tracking_path": null,
    "updated_at": "2026-05-23"
  },
  "id": "rabenstein-daad-original-adventure",
  "last_activity": "2020-06-02",
  "last_checked": "2026-10-11",
  "re_started": null,
  "reconstructed_languages": [
    "DAAD source",
    "Shell"
  ],
  "record_class": "subject",
  "repo": "https://github.com/ByteProject/Rabenstein",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Released adventure with creator-published DAAD source; archived build needs external setup",
  "subjects": [
    "The Curse of Rabenstein"
  ],
  "tags": [
    "Atari ST",
    "Amiga",
    "Commodore 64",
    "homebrew",
    "interactive fiction"
  ],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Commodore 64",
    "Commodore Plus/4",
    "Amstrad CPC",
    "ZX Spectrum",
    "ZX Spectrum Next",
    "Amiga",
    "Atari ST",
    "DOS"
  ],
  "techniques": [
    "DAAD database compilation",
    "platform-specific disk packaging"
  ],
  "title": "The Curse of Rabenstein",
  "tool_kinds": [],
  "types": [
    "native homebrew",
    "original-source release"
  ],
  "upstream_name": "The Curse of Rabenstein",
  "work_kinds": []
}
```

### Identity (reviewed)

Stefan Vogt/Puddle Software publishes the original source of The Curse of Rabenstein. The 3,187-line rabenstein.dsf contains the game vocabulary, locations, objects and command logic; accompanying artwork and target scripts form one multi-platform game repository. The release page is linked by the creator README.
- https://github.com/ByteProject/Rabenstein/blob/8fec1f400bbfcb317dbdc8c7a77789fb781492dc/README.md
- https://github.com/ByteProject/Rabenstein/blob/8fec1f400bbfcb317dbdc8c7a77789fb781492dc/rabenstein.dsf

### Classification (reviewed)

Substantial original homebrew/adventure source, not reverse engineering of an older commercial game. The repository uses DAAD with the DRC compiler and Maluva extensions, and its scripts package platform-specific interpreter/data disk releases. The game root is retained as one project rather than separate ST, Amiga and C64 records.
- https://github.com/ByteProject/Rabenstein/blob/8fec1f400bbfcb317dbdc8c7a77789fb781492dc/README.md
- https://github.com/ByteProject/Rabenstein/blob/8fec1f400bbfcb317dbdc8c7a77789fb781492dc/rabenstein.dsf
- https://github.com/ByteProject/Rabenstein/blob/8fec1f400bbfcb317dbdc8c7a77789fb781492dc/atari_st.sh
- https://github.com/ByteProject/Rabenstein/blob/8fec1f400bbfcb317dbdc8c7a77789fb781492dc/amiga.sh
- https://github.com/ByteProject/Rabenstein/blob/8fec1f400bbfcb317dbdc8c7a77789fb781492dc/64.sh

### Source CPU (not-applicable)

The inspected work is a newly authored DAAD adventure, not a reconstruction from a historical machine-code binary. source_platforms, source_language and source_cpu therefore remain empty.
- https://github.com/ByteProject/Rabenstein/blob/8fec1f400bbfcb317dbdc8c7a77789fb781492dc/README.md
- https://github.com/ByteProject/Rabenstein/blob/8fec1f400bbfcb317dbdc8c7a77789fb781492dc/rabenstein.dsf

### Target CPU (no-evidence-found)

Target scripts compile a DAAD game database and combine it with external machine-specific interpreters. No interpreter assembly source or explicit CPU selection was verified in this game checkout. The platform targets are established, but target_cpu remains empty rather than inferring processor models from machine names.
- https://github.com/ByteProject/Rabenstein/blob/8fec1f400bbfcb317dbdc8c7a77789fb781492dc/atari_st.sh
- https://github.com/ByteProject/Rabenstein/blob/8fec1f400bbfcb317dbdc8c7a77789fb781492dc/amiga.sh
- https://github.com/ByteProject/Rabenstein/blob/8fec1f400bbfcb317dbdc8c7a77789fb781492dc/64.sh
- https://github.com/ByteProject/Rabenstein/blob/8fec1f400bbfcb317dbdc8c7a77789fb781492dc/rabenstein.dsf

### Build (reviewed)

The creator distributes playable releases and supplies launch instructions for Atari ST, Amiga and other targets, supporting creator-reported runnable/playable=true. The source README expressly warns that external tools are omitted and paths are hardcoded; the inspected ST/Amiga/C64 scripts confirm those dependencies. Current checkout compilability remains unknown. Limitations: No compilation, emulator launch, gameplay or byte comparison was performed. Released binaries are not proof that this archived source snapshot rebuilds without modification.
- https://github.com/ByteProject/Rabenstein/blob/8fec1f400bbfcb317dbdc8c7a77789fb781492dc/README.md
- https://github.com/ByteProject/Rabenstein/blob/8fec1f400bbfcb317dbdc8c7a77789fb781492dc/atari_st.sh
- https://github.com/ByteProject/Rabenstein/blob/8fec1f400bbfcb317dbdc8c7a77789fb781492dc/amiga.sh
- https://github.com/ByteProject/Rabenstein/blob/8fec1f400bbfcb317dbdc8c7a77789fb781492dc/64.sh
- https://8bitgames.itch.io/rabenstein

### Runtime profiles (no-evidence-found)

The source README and reviewed ST/Amiga scripts specify target machines and media but no verified minimum CPU, RAM or OS version. The creator page gives disk-loading instructions rather than complete ST/Amiga hardware minima; no runtime profile is inferred.
- https://github.com/ByteProject/Rabenstein/blob/8fec1f400bbfcb317dbdc8c7a77789fb781492dc/README.md
- https://github.com/ByteProject/Rabenstein/blob/8fec1f400bbfcb317dbdc8c7a77789fb781492dc/atari_st.sh
- https://github.com/ByteProject/Rabenstein/blob/8fec1f400bbfcb317dbdc8c7a77789fb781492dc/amiga.sh
- https://8bitgames.itch.io/rabenstein

### AI (no-evidence-found)

The complete repository tree, creator README, game-source header and selected logic, three target scripts and both available commit messages contain no explicit AI-development disclosure. Usage remains null; historical dates alone do not prove non-use.
- https://github.com/ByteProject/Rabenstein/blob/8fec1f400bbfcb317dbdc8c7a77789fb781492dc/README.md
- https://github.com/ByteProject/Rabenstein/blob/8fec1f400bbfcb317dbdc8c7a77789fb781492dc/rabenstein.dsf
- https://github.com/ByteProject/Rabenstein/commits/8fec1f400bbfcb317dbdc8c7a77789fb781492dc

### Relationships (reviewed)

The README credits Tim Gilberts for DAAD and Uto for Maluva; DRC is a separate compiler. The public source license allows personal educational use but forbids derivative games, so this is not described as permissively licensed. The official release page also lists later MSX/QL ports, a D42 C64 point-and-click edition and a browser edition; those uninspected implementations are not added to this DAAD source record.
- https://github.com/ByteProject/Rabenstein/blob/8fec1f400bbfcb317dbdc8c7a77789fb781492dc/README.md
- https://github.com/ByteProject/Rabenstein/blob/8fec1f400bbfcb317dbdc8c7a77789fb781492dc/rabenstein.dsf
- https://8bitgames.itch.io/rabenstein

## JC64dis — interactive Commodore disassembler and analysis workbench

Project ID: jc64dis-java-retro-disassembler · Overall audit: reviewed

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
    "runnable": null
  },
  "display_title": "JC64dis — interactive Commodore disassembler and analysis workbench",
  "id": "jc64dis-java-retro-disassembler",
  "last_activity": "2026-07-29",
  "last_checked": "2026-10-11",
  "re_started": null,
  "reconstructed_languages": [
    "Java"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/ice00/jc64",
  "runtime_profiles": [],
  "source_cpu": [
    "6510",
    "6502",
    "Z80",
    "8048"
  ],
  "source_language": [
    "machine code"
  ],
  "source_platforms": [
    "Commodore 64",
    "Commodore 128",
    "Commodore 1541",
    "VIC-20",
    "Commodore Plus/4",
    "Atari 8-bit",
    "Odyssey 2"
  ],
  "status": "Current disassembler with observed successful upstream JAR/native CI; experimental emulator retained in the same root.",
  "subjects": [],
  "tags": [
    "Commodore 64",
    "Commodore 128",
    "6502",
    "disassembly",
    "AI-assisted analysis"
  ],
  "target_cpu": [
    "x86-64"
  ],
  "target_kinds": [],
  "target_platforms": [
    "Windows",
    "Linux",
    "macOS"
  ],
  "techniques": [
    "interactive labels and comments",
    "undocumented opcode decoding",
    "machine memory maps",
    "AI-generated analysis annotations"
  ],
  "title": "JC64dis",
  "tool_kinds": [
    "disassembler",
    "reassembler",
    "binary-analysis",
    "emulator"
  ],
  "types": [
    "interactive disassembler",
    "software emulator"
  ],
  "upstream_name": "JC64dis",
  "work_kinds": []
}
```

### Identity (reviewed)

Ice Team/Stefano Tognon’s coherent Java root contains the historical JC64 emulator and the maintained JC64dis graphical disassembler. The old emulator warning in README does not describe the availability of the later JC64dis releases. Repository metadata identifies the root as non-fork; source headers state GPL-2.0-or-later.
- https://github.com/ice00/jc64/blob/59988b819768e8c48f01664ed2ff082ee428de77/README.md
- https://github.com/ice00/jc64/blob/59988b819768e8c48f01664ed2ff082ee428de77/src/sw_emulator/software/cpu/M6510Dasm.java
- https://github.com/ice00/jc64/releases/tag/3.2

### Classification (reviewed)

Reusable software-archaeology tooling, not a reconstructed game. The inspected 6510 disassembler decodes legal and undocumented opcodes; TargetType dispatches machine-specific disassembly; the integrated agent can request listings and assign labels/comments. The emulator and disassembler remain one root record. Compiler.java dispatches assembler calls to DASM, ACME, ca65, 64tass, KickAssembler, Glass and AS, substantiating the integrated reassembly capability.
- https://github.com/ice00/jc64/blob/59988b819768e8c48f01664ed2ff082ee428de77/README.md
- https://github.com/ice00/jc64/blob/59988b819768e8c48f01664ed2ff082ee428de77/src/sw_emulator/software/cpu/M6510Dasm.java
- https://github.com/ice00/jc64/blob/59988b819768e8c48f01664ed2ff082ee428de77/src/sw_emulator/swing/main/TargetType.java
- https://github.com/ice00/jc64/blob/59988b819768e8c48f01664ed2ff082ee428de77/src/sw_emulator/software/ai/DisassemblerAgent.java
- https://github.com/ice00/jc64/blob/59988b819768e8c48f01664ed2ff082ee428de77/src/sw_emulator/software/asm/Compiler.java

### Source CPU (reviewed)

M6510Dasm implements 6510 instruction decoding. TargetType explicitly dispatches M6502-family Commodore/Atari targets, C128Z to Z80Dasm and Odyssey to the I8048-family decoder. These are analysed guest architectures, not the Java host CPU. AtariDasm’s inspected memory-map dispatch names GTIA/POKEY/ANTIC, establishing Atari 8-bit rather than Atari ST; OdysseyDasm identifies the Odyssey/Videopac BIOS.
- https://github.com/ice00/jc64/blob/59988b819768e8c48f01664ed2ff082ee428de77/src/sw_emulator/software/cpu/M6510Dasm.java
- https://github.com/ice00/jc64/blob/59988b819768e8c48f01664ed2ff082ee428de77/src/sw_emulator/swing/main/TargetType.java
- https://github.com/ice00/jc64/blob/59988b819768e8c48f01664ed2ff082ee428de77/src/sw_emulator/software/machine/AtariDasm.java
- https://github.com/ice00/jc64/blob/59988b819768e8c48f01664ed2ff082ee428de77/src/sw_emulator/software/machine/OdysseyDasm.java

### Target CPU (reviewed)

The inspected native-image workflow explicitly downloads amd64 Liberica toolchains for Linux, Windows and macOS and produces native JC64dis binaries. x86-64 records those documented native output variants; the separately built JVM JAR is not assigned an inferred hardware CPU.
- https://github.com/ice00/jc64/blob/59988b819768e8c48f01664ed2ff082ee428de77/.github/workflows/native.yml
- https://github.com/ice00/jc64/blob/59988b819768e8c48f01664ed2ff082ee428de77/build-github.xml

### Build (reviewed)

Observed upstream CI at the pinned commit: run 30475925046 completed successfully. Its job records show successful Ant JAR compilation and native-image build steps for Windows/macOS, the combined Linux compilation/native-image step, and artifact uploads. Ant’s manifest selects JC64Dis. This is concrete upstream build-step evidence for compilable=true, not merely a generic green workflow. Published 3.2 and latest releases contain JAR/native packages; runnable/playable and byte exactness remain unknown. Limitations: No local compilation, native/JVM launch, emulator compatibility test or byte comparison was performed. Successful CI builds do not prove GUI/runtime correctness.
- https://github.com/ice00/jc64/blob/59988b819768e8c48f01664ed2ff082ee428de77/build-github.xml
- https://github.com/ice00/jc64/blob/59988b819768e8c48f01664ed2ff082ee428de77/.github/workflows/native.yml
- https://github.com/ice00/jc64/actions/runs/30475925046
- https://github.com/ice00/jc64/actions/runs/30475925046/job/90657478818
- https://github.com/ice00/jc64/actions/runs/30475925046/job/90657478864
- https://github.com/ice00/jc64/actions/runs/30475925046/job/90657478865
- https://github.com/ice00/jc64/releases/tag/3.2

### Runtime profiles (no-evidence-found)

The workflow and README establish Java/native host variants and qualitative performance cautions, but no verified minimum RAM, OS version or CPU generation for a runnable distribution. Guest 6510/Z80/8048 support is not a host minimum; no runtime profile is inferred.
- https://github.com/ice00/jc64/blob/59988b819768e8c48f01664ed2ff082ee428de77/README.md
- https://github.com/ice00/jc64/blob/59988b819768e8c48f01664ed2ff082ee428de77/.github/workflows/native.yml

### AI (no-evidence-found)

The inspected DisassemblerAgent.java implements an OpenAI-compatible AI annotation feature and current release notes advertise AI labeling. This establishes a tool capability, not actual AI use in developing JC64dis. No explicit development-use disclosure or AI co-author attribution was found in README, inspected source/build files or the 30 reviewed commit messages; usage stays null.
- https://github.com/ice00/jc64/blob/59988b819768e8c48f01664ed2ff082ee428de77/README.md
- https://github.com/ice00/jc64/blob/59988b819768e8c48f01664ed2ff082ee428de77/src/sw_emulator/software/ai/DisassemblerAgent.java
- https://github.com/ice00/jc64/commits/59988b819768e8c48f01664ed2ff082ee428de77
- https://github.com/ice00/jc64/releases/tag/3.2

### Relationships (reviewed)

README credits VICE for CPU instruction-emulation foundations and other hardware references. JC64dis is an integrated subsystem of this same repository, not a separate game or project-per-example. The release notes describe Regenerator2000 project import as interoperability; that is not evidence of duplicate identity.
- https://github.com/ice00/jc64/blob/59988b819768e8c48f01664ed2ff082ee428de77/README.md
- https://github.com/ice00/jc64/releases/tag/3.2

## Negentropy — annotated C64 disassembly and linked HTML generator

Project ID: negentropy-c64-html-disassembler · Overall audit: reviewed

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
  "display_title": "Negentropy — annotated C64 disassembly and linked HTML generator",
  "id": "negentropy-c64-html-disassembler",
  "last_activity": "2025-10-12",
  "last_checked": "2026-10-11",
  "re_started": null,
  "reconstructed_languages": [
    "Python"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/shewitt-au/negentropy",
  "runtime_profiles": [],
  "source_cpu": [
    "6502",
    "6510"
  ],
  "source_language": [
    "6502 machine code",
    "Commodore BASIC"
  ],
  "source_platforms": [
    "Commodore 64"
  ],
  "status": "Python beta disassembler; author reports a successful ACME round-trip example, with current execution untested.",
  "subjects": [],
  "tags": [
    "Commodore 64",
    "HTML",
    "BASIC",
    "6502"
  ],
  "target_cpu": [],
  "target_kinds": [],
  "target_platforms": [],
  "techniques": [
    "configuration-driven labels and comments",
    "linked disassembly",
    "BASIC SYS cross-references",
    "character-set rendering"
  ],
  "title": "Negentropy",
  "tool_kinds": [
    "disassembler",
    "binary-analysis",
    "asset-tool"
  ],
  "types": [
    "annotated disassembly generator"
  ],
  "upstream_name": "Negentropy",
  "work_kinds": []
}
```

### Identity (reviewed)

Stephen Hewitt’s Negentropy is a Python 3 console C64 disassembler. setup.py names the same canonical repository, beta version 0.2, author and MIT license; repository metadata marks it non-fork.
- https://github.com/shewitt-au/negentropy/blob/04b86f701decad4912dc50cf32c906b9644d4f6f/README.md
- https://github.com/shewitt-au/negentropy/blob/04b86f701decad4912dc50cf32c906b9644d4f6f/setup.py

### Classification (reviewed)

One reusable analysis/generation tool, rather than a game reconstruction: README describes linked HTML, BASIC listings and charset images. The inspected M6502 decoder emits structured instructions/labels/comments and the CLI delegates output generation to templates.
- https://github.com/shewitt-au/negentropy/blob/04b86f701decad4912dc50cf32c906b9644d4f6f/README.md
- https://github.com/shewitt-au/negentropy/blob/04b86f701decad4912dc50cf32c906b9644d4f6f/negentropy/M6502decoder.py
- https://github.com/shewitt-au/negentropy/blob/04b86f701decad4912dc50cf32c906b9644d4f6f/negentropy/negentropy.py

### Source CPU (reviewed)

README explicitly specifies 6502 machine-code disassembly and setup.py names both 6502 and 6510. M6502Decoder interprets instruction operand sizes and addressing modes, resolves branch targets and emits instruction records. The C64-specific symbol map belongs to this analysed architecture.
- https://github.com/shewitt-au/negentropy/blob/04b86f701decad4912dc50cf32c906b9644d4f6f/README.md
- https://github.com/shewitt-au/negentropy/blob/04b86f701decad4912dc50cf32c906b9644d4f6f/setup.py
- https://github.com/shewitt-au/negentropy/blob/04b86f701decad4912dc50cf32c906b9644d4f6f/negentropy/M6502decoder.py

### Target CPU (not-applicable)

The maintained program runs under Python and primarily produces linked HTML/text analysis; its host processor is not specified. An optional ACME source template is not a separate compiled modern-host or native retro game output, so no target CPU is assigned.
- https://github.com/shewitt-au/negentropy/blob/04b86f701decad4912dc50cf32c906b9644d4f6f/README.md
- https://github.com/shewitt-au/negentropy/blob/04b86f701decad4912dc50cf32c906b9644d4f6f/negentropy/negentropy.py

### Build (reviewed)

setup.py declares Python 3, a negentropy console entry point, and Jinja2/Pillow/Lark dependencies. Historical upstream commit ae5712aa9b1e47b9974286929671deccd61cf001 explicitly reports successfully assembling one disassembled file with ACME and playing that test. That is a dated example round-trip claim, not proof of current package installation, arbitrary output rebuilding or byte identity; current build flags remain unknown. Limitations: No package installation, CLI execution, ACME build or output comparison was performed. The README still calls non-HTML templates incomplete.
- https://github.com/shewitt-au/negentropy/blob/04b86f701decad4912dc50cf32c906b9644d4f6f/README.md
- https://github.com/shewitt-au/negentropy/blob/04b86f701decad4912dc50cf32c906b9644d4f6f/setup.py
- https://github.com/shewitt-au/negentropy/commit/ae5712aa9b1e47b9974286929671deccd61cf001

### Runtime profiles (no-evidence-found)

Python 3 and named dependencies are documented. The inspected README, package metadata and CLI do not establish a minimum host CPU/RAM or an OS-specific runnable profile; none is inferred from the C64 input format.
- https://github.com/shewitt-au/negentropy/blob/04b86f701decad4912dc50cf32c906b9644d4f6f/README.md
- https://github.com/shewitt-au/negentropy/blob/04b86f701decad4912dc50cf32c906b9644d4f6f/setup.py
- https://github.com/shewitt-au/negentropy/blob/04b86f701decad4912dc50cf32c906b9644d4f6f/negentropy/negentropy.py

### AI (no-evidence-found)

No explicit development-AI disclosure was found in the README, package metadata, inspected decoder/CLI files, complete tree inventory or the 30 reviewed commit messages. Python code and a missing disclosure do not establish non-use; usage stays null.
- https://github.com/shewitt-au/negentropy/blob/04b86f701decad4912dc50cf32c906b9644d4f6f/README.md
- https://github.com/shewitt-au/negentropy/blob/04b86f701decad4912dc50cf32c906b9644d4f6f/setup.py
- https://github.com/shewitt-au/negentropy/blob/04b86f701decad4912dc50cf32c906b9644d4f6f/negentropy/M6502decoder.py
- https://github.com/shewitt-au/negentropy/commits/04b86f701decad4912dc50cf32c906b9644d4f6f
- https://github.com/shewitt-au/negentropy/tree/04b86f701decad4912dc50cf32c906b9644d4f6f

### Relationships (reviewed)

The canonical non-fork root and setup metadata agree on identity. Jinja2, Pillow and Lark are external dependencies, while BASIC/6502 decoders, image generation and output templates are internal components of the same tool. No separate title-level subjects are created.
- https://github.com/shewitt-au/negentropy/blob/04b86f701decad4912dc50cf32c906b9644d4f6f/README.md
- https://github.com/shewitt-au/negentropy/blob/04b86f701decad4912dc50cf32c906b9644d4f6f/setup.py
- https://github.com/shewitt-au/negentropy/blob/04b86f701decad4912dc50cf32c906b9644d4f6f/negentropy/negentropy.py

## NS-Shaft — native C128 descent-game prototype

Project ID: nsshaft-native-c128-prototype · Overall audit: reviewed

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
  "display_title": "NS-Shaft — native C128 descent-game prototype",
  "id": "nsshaft-native-c128-prototype",
  "last_activity": "2026-09-28",
  "last_checked": "2026-10-11",
  "re_started": null,
  "reconstructed_languages": [
    "6502 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/Mankind-dvk/nsshaft-c128",
  "runtime_profiles": [
    {
      "chipsets": [
        "VIC-IIe"
      ],
      "cpu_family": "6502",
      "evidence": [
        "https://github.com/Mankind-dvk/nsshaft-c128/blob/e4e58a56b72ec04256a7f72b6d09eb41e93f9623/README.md",
        "https://github.com/Mankind-dvk/nsshaft-c128/blob/e4e58a56b72ec04256a7f72b6d09eb41e93f9623/src/main.s"
      ],
      "min_cpu": "8502",
      "name": "Native C128 VIC-IIe prototype",
      "notes": "Author specifies native 8502 mode at 1 MHz, RAM bank 0, 40-column output and paddle input on control port 1. PAL-oriented frame timing; writable disk needed for persistent scores. No minimum RAM quantity or NTSC compatibility claim is inferred.",
      "os": "C128 native mode / BASIC 7 loader",
      "platform": "Commodore 128"
    }
  ],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Substantial native C128 gameplay implementation; documented ca65/ld65 build and VICE launcher, untested in this pass.",
  "subjects": [
    "NS-Shaft"
  ],
  "tags": [
    "Commodore 128",
    "8502",
    "VIC-IIe",
    "prototype"
  ],
  "target_cpu": [
    "8502"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Commodore 128"
  ],
  "techniques": [
    "native 8502 execution",
    "character-tile scrolling",
    "SID raster interrupt",
    "dual-slot high-score persistence"
  ],
  "title": "Native Commodore 128 NS-Shaft prototype",
  "tool_kinds": [],
  "types": [
    "native game prototype"
  ],
  "upstream_name": "Native Commodore 128 NS-Shaft prototype",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

The repository identifies an NS-Shaft-style native Commodore 128 prototype, with detailed platform/hazard/character/scoring documentation and a complete subsystem-oriented assembly tree. Its metadata marks it non-fork. No LICENSE file is present in the pinned tree; the included uppercase font has separate classroom-example provenance.
- https://github.com/mankind-dvk/nsshaft-c128/blob/e4e58a56b72ec04256a7f72b6d09eb41e93f9623/README.md
- https://github.com/mankind-dvk/nsshaft-c128/blob/e4e58a56b72ec04256a7f72b6d09eb41e93f9623/src/main.s
- https://github.com/mankind-dvk/nsshaft-c128/blob/e4e58a56b72ec04256a7f72b6d09eb41e93f9623/assets/fonts/README.md

### Classification (reviewed)

This is a native game reimplementation/prototype, not a game-specific emulator wrapper. The inspected main.s directly initializes C128 MMU/VIC/CIA state, calls gameplay modules and coordinates character selection, physics, scrolling and high-score screens. The README explicitly says it never enters C64 compatibility mode.
- https://github.com/mankind-dvk/nsshaft-c128/blob/e4e58a56b72ec04256a7f72b6d09eb41e93f9623/README.md
- https://github.com/mankind-dvk/nsshaft-c128/blob/e4e58a56b72ec04256a7f72b6d09eb41e93f9623/src/main.s

### Source CPU (no-evidence-found)

NS-Shaft is named as gameplay inspiration, but the inspected project does not identify an original binary or recovered source listing being translated. The original subject’s machine architecture and language are therefore left unknown rather than guessed from the new C128 target.
- https://github.com/mankind-dvk/nsshaft-c128/blob/e4e58a56b72ec04256a7f72b6d09eb41e93f9623/README.md
- https://github.com/mankind-dvk/nsshaft-c128/blob/e4e58a56b72ec04256a7f72b6d09eb41e93f9623/src/main.s

### Target CPU (reviewed)

README explicitly specifies native C128/8502 execution at 1 MHz. main.s sets ca65’s 6502 instruction subset, starts from a BASIC 7 SYS loader and manipulates C128 MMU registers; 8502 is the evidenced native output CPU, despite the shared 6502 instruction syntax.
- https://github.com/mankind-dvk/nsshaft-c128/blob/e4e58a56b72ec04256a7f72b6d09eb41e93f9623/README.md
- https://github.com/mankind-dvk/nsshaft-c128/blob/e4e58a56b72ec04256a7f72b6d09eb41e93f9623/src/main.s
- https://github.com/mankind-dvk/nsshaft-c128/blob/e4e58a56b72ec04256a7f72b6d09eb41e93f9623/build.ps1

### Build (reviewed)

The PowerShell recipe invokes ca65 and ld65 with c128-prg.cfg to create build/nsshaft-c128.prg; README supplies VICE x128 and real-machine loading instructions. Optional regression sources exist for charset, platforms and leaderboard behavior, including a py65-based high-score harness. These are source/build/test declarations, not observed passing tests. All four build flags remain unknown. Limitations: No assembly, Python regression suite, VICE execution, gameplay test or hardware test was run. README’s byte-identical macro-refactoring discussion does not establish identity with an original NS-Shaft binary.
- https://github.com/mankind-dvk/nsshaft-c128/blob/e4e58a56b72ec04256a7f72b6d09eb41e93f9623/README.md
- https://github.com/mankind-dvk/nsshaft-c128/blob/e4e58a56b72ec04256a7f72b6d09eb41e93f9623/build.ps1
- https://github.com/mankind-dvk/nsshaft-c128/blob/e4e58a56b72ec04256a7f72b6d09eb41e93f9623/tests/test_highscores.py

### Runtime profiles (reviewed)

A documented native C128 profile is recorded from explicit 8502, 1 MHz, bank-0 and VIC-IIe 40-column statements. README requires paddle input on port 1 and writable disk for saved scores, and describes PAL-oriented timing. The profile records these documented requirements only; no RAM minimum or NTSC compatibility is inferred. Limitations: The documented hardware configuration was not independently exercised.
- https://github.com/mankind-dvk/nsshaft-c128/blob/e4e58a56b72ec04256a7f72b6d09eb41e93f9623/README.md
- https://github.com/mankind-dvk/nsshaft-c128/blob/e4e58a56b72ec04256a7f72b6d09eb41e93f9623/src/main.s

### AI (no-evidence-found)

README, inspected assembly/build/test/font files and the 13 visible default-branch commits contain no explicit development-AI attribution. Merged PR 4 uses a codex/docs-source-sync branch but has no description; a branch label alone does not establish actual Codex use. Usage remains null.
- https://github.com/mankind-dvk/nsshaft-c128/blob/e4e58a56b72ec04256a7f72b6d09eb41e93f9623/README.md
- https://github.com/mankind-dvk/nsshaft-c128/blob/e4e58a56b72ec04256a7f72b6d09eb41e93f9623/src/main.s
- https://github.com/mankind-dvk/nsshaft-c128/blob/e4e58a56b72ec04256a7f72b6d09eb41e93f9623/build.ps1
- https://github.com/Mankind-dvk/nsshaft-c128/pull/4
- https://github.com/Mankind-dvk/nsshaft-c128/commits/e4e58a56b72ec04256a7f72b6d09eb41e93f9623

### Relationships (reviewed)

The README describes a native NS-Shaft-style port with newly structured assembly subsystems rather than preserved historical source. Font documentation identifies an unchanged 2048-byte slice of a teacher-provided C64 charset example embedded locally, so that asset has a separate provenance from game logic. No duplicate tracked implementation or independent subproject was established. Limitations: Original game/platform lineage and asset reuse permissions are not fully documented; no source-restoration or clean-room claim is made.
- https://github.com/mankind-dvk/nsshaft-c128/blob/e4e58a56b72ec04256a7f72b6d09eb41e93f9623/README.md
- https://github.com/mankind-dvk/nsshaft-c128/blob/e4e58a56b72ec04256a7f72b6d09eb41e93f9623/src/main.s
- https://github.com/mankind-dvk/nsshaft-c128/blob/e4e58a56b72ec04256a7f72b6d09eb41e93f9623/assets/fonts/README.md

## The Race — C128 binary reconstruction and C64 adaptation

Project ID: the-race-c128-reconstruction · Overall audit: reviewed

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
  "display_title": "The Race — C128 binary reconstruction and C64 adaptation",
  "id": "the-race-c128-reconstruction",
  "last_activity": "2016-12-12",
  "last_checked": "2026-10-11",
  "re_started": null,
  "reconstructed_languages": [
    "6502 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/ricardoquesada/c128-the-race",
  "runtime_profiles": [],
  "source_cpu": [
    "6502"
  ],
  "source_language": [
    "6502 machine code"
  ],
  "source_platforms": [
    "Commodore 128"
  ],
  "status": "Annotated reconstruction with C128 and C64 build targets and packaged disks; no current build or gameplay verification.",
  "subjects": [
    "The Race"
  ],
  "tags": [
    "Commodore 128",
    "Commodore 64",
    "6502"
  ],
  "target_cpu": [
    "6502"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Commodore 128",
    "Commodore 64"
  ],
  "techniques": [
    "ca65/cl65 assembly",
    "binary-derived reconstruction",
    "conditional machine initialization",
    "VIC raster interrupts"
  ],
  "title": "The Race",
  "tool_kinds": [],
  "types": [
    "binary-derived game reconstruction",
    "native port"
  ],
  "upstream_name": "The Race",
  "work_kinds": [
    "disassembly",
    "source-reconstruction",
    "reverse-engineering-derived-port"
  ]
}
```

### Identity (reviewed)

Ricardo Quesada’s README states that The Race for C128 is being regenerated from its binary files. The root contains orig PRG/D71 inputs, substantial annotated game/intro/music assembly, editable graphics resources and separate C64/C128 packaged disks. The pinned repository is non-fork; no LICENSE file appears in its tree.
- https://github.com/ricardoquesada/c128-the-race/blob/4db38ff7adcce1b70794a5468128a0a812fd7ae5/README.md
- https://github.com/ricardoquesada/c128-the-race/blob/4db38ff7adcce1b70794a5468128a0a812fd7ae5/src/main.s
- https://github.com/ricardoquesada/c128-the-race/blob/4db38ff7adcce1b70794a5468128a0a812fd7ae5/src/game.s
- https://github.com/ricardoquesada/c128-the-race/tree/4db38ff7adcce1b70794a5468128a0a812fd7ae5

### Classification (reviewed)

The one-line README establishes binary-derived reconstruction rather than recovered original source. Substantial labelled game logic handles two players, collisions, scrolling, timers and raster IRQs. Conditional initialization and the Makefile extend the same recovered game to native C64, so this is one coherent reconstruction/adaptation lineage.
- https://github.com/ricardoquesada/c128-the-race/blob/4db38ff7adcce1b70794a5468128a0a812fd7ae5/README.md
- https://github.com/ricardoquesada/c128-the-race/blob/4db38ff7adcce1b70794a5468128a0a812fd7ae5/src/game.s
- https://github.com/ricardoquesada/c128-the-race/blob/4db38ff7adcce1b70794a5468128a0a812fd7ae5/src/main.s
- https://github.com/ricardoquesada/c128-the-race/blob/4db38ff7adcce1b70794a5468128a0a812fd7ae5/Makefile

### Source CPU (reviewed)

The reconstructed C128 game listing uses the 6502-family instruction set, accumulator/X/Y registers, zero-page state and indirect accesses; only the evidenced 6502 instruction architecture is recorded. No Z80/CP/M game path is present in the inspected assembly.
- https://github.com/ricardoquesada/c128-the-race/blob/4db38ff7adcce1b70794a5468128a0a812fd7ae5/src/main.s
- https://github.com/ricardoquesada/c128-the-race/blob/4db38ff7adcce1b70794a5468128a0a812fd7ae5/src/game.s

### Target CPU (reviewed)

Makefile assembles the same sources with cl65 -t c128 and -t c64. main.s conditionally selects C128 MMU or C64 $01 banking initialization. Both outputs remain native 6502-family code; VICE is merely the external launch/test environment.
- https://github.com/ricardoquesada/c128-the-race/blob/4db38ff7adcce1b70794a5468128a0a812fd7ae5/Makefile
- https://github.com/ricardoquesada/c128-the-race/blob/4db38ff7adcce1b70794a5468128a0a812fd7ae5/src/main.s

### Build (reviewed)

The root declares cl65, Exomizer and VICE c1541/x128/x64 steps and includes D71/D64 binaries. Historical commits describe working intermediate reconstruction and later C64 support, but do not certify the current two-target build or complete gameplay. The default all target also launches emulators. All build/byte-match flags remain unknown. Limitations: No compilation, resource export, emulator launch, gameplay or original-binary comparison was performed. The Makefile references resource-copy inputs not all present under res; corresponding generated .bin assets are committed under src, but the rebuild path was not exercised.
- https://github.com/ricardoquesada/c128-the-race/blob/4db38ff7adcce1b70794a5468128a0a812fd7ae5/README.md
- https://github.com/ricardoquesada/c128-the-race/blob/4db38ff7adcce1b70794a5468128a0a812fd7ae5/Makefile
- https://github.com/ricardoquesada/c128-the-race/blob/4db38ff7adcce1b70794a5468128a0a812fd7ae5/src/main.s
- https://github.com/ricardoquesada/c128-the-race/commit/4ec60078ccbbdd051e8d4e24f4a5aace10e0a600
- https://github.com/ricardoquesada/c128-the-race/commit/d6c3980efa1b181d7cf7dd8ae5e13dcea72b71a9

### Runtime profiles (no-evidence-found)

C128/C64 build targets and VIC/CIA usage are explicit, but the inspected README/build/source files do not specify a verified minimum RAM, PAL/NTSC compatibility or hardware configuration. No runtime profile is inferred from target names or packaged disk images.
- https://github.com/ricardoquesada/c128-the-race/blob/4db38ff7adcce1b70794a5468128a0a812fd7ae5/README.md
- https://github.com/ricardoquesada/c128-the-race/blob/4db38ff7adcce1b70794a5468128a0a812fd7ae5/Makefile
- https://github.com/ricardoquesada/c128-the-race/blob/4db38ff7adcce1b70794a5468128a0a812fd7ae5/src/main.s
- https://github.com/ricardoquesada/c128-the-race/blob/4db38ff7adcce1b70794a5468128a0a812fd7ae5/src/game.s

### AI (no-evidence-found)

No explicit AI-development disclosure or AI co-author attribution was found in README, inspected assembly/Makefile or the 29 returned history entries. Historical dates alone are not proof of non-use; usage remains null.
- https://github.com/ricardoquesada/c128-the-race/blob/4db38ff7adcce1b70794a5468128a0a812fd7ae5/README.md
- https://github.com/ricardoquesada/c128-the-race/blob/4db38ff7adcce1b70794a5468128a0a812fd7ae5/Makefile
- https://github.com/ricardoquesada/c128-the-race/blob/4db38ff7adcce1b70794a5468128a0a812fd7ae5/src/game.s
- https://github.com/ricardoquesada/c128-the-race/commits/4db38ff7adcce1b70794a5468128a0a812fd7ae5

### Relationships (reviewed)

The C64 adaptation, C128 reconstruction, intro, cracktro and music modules form the same game repository and are retained as one project. orig contains reconstruction inputs and bin contains outputs; these are not extra project records. The author’s separately reviewed binary-only Erasoft archive is not being counted again.
- https://github.com/ricardoquesada/c128-the-race/blob/4db38ff7adcce1b70794a5468128a0a812fd7ae5/README.md
- https://github.com/ricardoquesada/c128-the-race/blob/4db38ff7adcce1b70794a5468128a0a812fd7ae5/Makefile
- https://github.com/ricardoquesada/c128-the-race/blob/4db38ff7adcce1b70794a5468128a0a812fd7ae5/src/main.s
- https://github.com/ricardoquesada/c128-the-race/tree/4db38ff7adcce1b70794a5468128a0a812fd7ae5

## Gorillas — Turbo Modula-2 port for C128 and CP/M systems

Project ID: gorilla-cpm-modula2-port · Overall audit: reviewed

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
    "playable": true,
    "runnable": true
  },
  "display_title": "Gorillas — Turbo Modula-2 port for C128 and CP/M systems",
  "id": "gorilla-cpm-modula2-port",
  "last_activity": "2019-11-07",
  "last_checked": "2026-10-11",
  "re_started": null,
  "reconstructed_languages": [
    "Modula-2"
  ],
  "record_class": "subject",
  "repo": "https://github.com/sblendorio/gorilla-cpm",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [
    "QBasic"
  ],
  "source_platforms": [
    "DOS"
  ],
  "status": "Author-distributed compiled CP/M game with platform disks and in-game examples; current rebuild and playthrough untested.",
  "subjects": [
    "Gorillas",
    "GORILLA.BAS"
  ],
  "tags": [
    "Commodore 128",
    "CP/M",
    "Modula-2",
    "Gorillas",
    "Amstrad CPC",
    "Memotech MTX"
  ],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "CP/M-80",
    "Commodore 128",
    "Memotech MTX",
    "Amstrad CPC",
    "MSX-DOS"
  ],
  "techniques": [
    "terminal abstraction",
    "ballistic projectile simulation",
    "native CP/M port"
  ],
  "title": "Gorilla.BAS - CP/M version",
  "tool_kinds": [],
  "types": [
    "native game port"
  ],
  "upstream_name": "Gorilla.BAS - CP/M version",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Francesco Sblendorio’s repository identifies a Turbo Modula-2 reimplementation of Microsoft’s DOS 5.0 GORILLA.BAS. main.mod credits the 1991 QBasic version and the 2015 CP/M version. The non-fork root contains the game, terminal library, compiled .COM and platform disk images; repository metadata identifies GPL-2.0 licensing.
- https://github.com/sblendorio/gorilla-cpm/blob/0de936a27ff514c70b43362b5fae6ce3fbdbbf6d/README.md
- https://github.com/sblendorio/gorilla-cpm/blob/0de936a27ff514c70b43362b5fae6ce3fbdbbf6d/source/main.mod

### Classification (reviewed)

A substantial source-level native game port, not binary-derived decompilation or an embedded CPU-emulation wrapper. The inspected game.mod implements projectile movement, buildings/collisions, alternating players and scoring; xterm.mod provides concrete CP/M terminal behavior. Multiple platform disks distribute the same coherent game.
- https://github.com/sblendorio/gorilla-cpm/blob/0de936a27ff514c70b43362b5fae6ce3fbdbbf6d/README.md
- https://github.com/sblendorio/gorilla-cpm/blob/0de936a27ff514c70b43362b5fae6ce3fbdbbf6d/source/game.mod
- https://github.com/sblendorio/gorilla-cpm/blob/0de936a27ff514c70b43362b5fae6ce3fbdbbf6d/source/xterm.mod

### Source CPU (not-applicable)

The documented input is the DOS QBasic game at language/game-design level, not an x86 binary disassembly. Original binary CPU does not apply to this source-level port, so source_cpu is empty.
- https://github.com/sblendorio/gorilla-cpm/blob/0de936a27ff514c70b43362b5fae6ce3fbdbbf6d/README.md
- https://github.com/sblendorio/gorilla-cpm/blob/0de936a27ff514c70b43362b5fae6ce3fbdbbf6d/source/main.mod

### Target CPU (no-evidence-found)

The README specifies compiled CP/M-80 .COM output and names a Z80 emulator in the development credits, but the inspected Modula-2 modules do not establish a precise 8080-versus-Z80 output instruction requirement. Target CPU stays empty instead of inferring it solely from the C128 or CP/M platform labels.
- https://github.com/sblendorio/gorilla-cpm/blob/0de936a27ff514c70b43362b5fae6ce3fbdbbf6d/README.md
- https://github.com/sblendorio/gorilla-cpm/blob/0de936a27ff514c70b43362b5fae6ce3fbdbbf6d/source/main.mod
- https://github.com/sblendorio/gorilla-cpm/blob/0de936a27ff514c70b43362b5fae6ce3fbdbbf6d/source/xterm.mod

### Build (reviewed)

The author explicitly distributes compiled gorilla.com and bootable C128/MTX/CPC/MSX disk images, with named in-game and intro examples on C128 and CPC. This supports author-reported compilability/runnable/playable status for the distributed game, corroborated by the substantial inspected game loop. The exact fresh-build procedure is not supplied in a build script; Turbo Modula-2 is identified as the compiler. Limitations: No compiler invocation, boot, gameplay session or binary comparison was performed here. True flags describe documented upstream distribution/playability, not an independent test; byte_exact remains null.
- https://github.com/sblendorio/gorilla-cpm/blob/0de936a27ff514c70b43362b5fae6ce3fbdbbf6d/README.md
- https://github.com/sblendorio/gorilla-cpm/blob/0de936a27ff514c70b43362b5fae6ce3fbdbbf6d/source/main.mod
- https://github.com/sblendorio/gorilla-cpm/blob/0de936a27ff514c70b43362b5fae6ce3fbdbbf6d/source/game.mod
- https://github.com/sblendorio/gorilla-cpm/tree/0de936a27ff514c70b43362b5fae6ce3fbdbbf6d

### Runtime profiles (no-evidence-found)

The repository documents CP/M-80, named terminal variants and bootable C128/MTX/CPC distributions. xterm.mod implements C128 color and cursor sequences and fixed 80-column UI assumptions, but no verified minimum CPU/RAM or OS revision is given. No machine-minimum profile is inferred.
- https://github.com/sblendorio/gorilla-cpm/blob/0de936a27ff514c70b43362b5fae6ce3fbdbbf6d/README.md
- https://github.com/sblendorio/gorilla-cpm/blob/0de936a27ff514c70b43362b5fae6ce3fbdbbf6d/source/main.mod
- https://github.com/sblendorio/gorilla-cpm/blob/0de936a27ff514c70b43362b5fae6ce3fbdbbf6d/source/xterm.mod

### AI (no-evidence-found)

No explicit development-AI disclosure was found in README, inspected Modula-2 modules, tree inventory or the 30 reviewed commit messages. Their historical dates do not establish non-use; usage stays null.
- https://github.com/sblendorio/gorilla-cpm/blob/0de936a27ff514c70b43362b5fae6ce3fbdbbf6d/README.md
- https://github.com/sblendorio/gorilla-cpm/blob/0de936a27ff514c70b43362b5fae6ce3fbdbbf6d/source/main.mod
- https://github.com/sblendorio/gorilla-cpm/blob/0de936a27ff514c70b43362b5fae6ce3fbdbbf6d/source/game.mod
- https://github.com/sblendorio/gorilla-cpm/commits/0de936a27ff514c70b43362b5fae6ce3fbdbbf6d

### Relationships (reviewed)

The README identifies the original Microsoft QBasic game and this distinct CP/M Modula-2 implementation. The tracked albank1/Commodore-64-Gorillas is a separate C64 BASIC rewrite; shared Gorillas subject alone does not make the CP/M codebase a duplicate. All terminal/platform variants here remain one project.
- https://github.com/sblendorio/gorilla-cpm/blob/0de936a27ff514c70b43362b5fae6ce3fbdbbf6d/README.md
- https://github.com/sblendorio/gorilla-cpm/blob/0de936a27ff514c70b43362b5fae6ce3fbdbbf6d/source/main.mod
- https://github.com/sblendorio/gorilla-cpm/blob/0de936a27ff514c70b43362b5fae6ce3fbdbbf6d/source/xterm.mod

## Pinned evidence manifest

- amiga3-carstene1ns-super-methane-brothers-readme: https://github.com/carstene1ns/super-methane-brothers/blob/52d931fae033186d791331ad20fd1eb443421f6a/README (Git blob 3a45fb209d7648cb71952ee3c908f9d8a77f303b)
- amiga3-carstene1ns-super-methane-brothers-readme-md: https://github.com/carstene1ns/super-methane-brothers/blob/52d931fae033186d791331ad20fd1eb443421f6a/README.md (Git blob 39e82a118005e872ba720698bd1cee303a905f45)
- amiga3-davidkinder-dbwrender-readme-md: https://github.com/davidkinder/dbwrender/blob/748886b74441d6734ec4ae21f1c81a06968ca369/README.md (Git blob f3a1804061165dd3640d4cdb63bbf46660d4ea45)
- amiga3-davidkinder-dbwrender-src-dbwrender-sln: https://github.com/davidkinder/dbwrender/blob/748886b74441d6734ec4ae21f1c81a06968ca369/src/DBWRender.sln (Git blob fe24056c2f0b4c1e318a7efb444ae0642d027123)
- amiga3-davidkinder-dbwrender-src-display-vcxproj: https://github.com/davidkinder/dbwrender/blob/748886b74441d6734ec4ae21f1c81a06968ca369/src/display.vcxproj (Git blob 0c30697bf274e277f28b07fbcd1c1b856f3eda1b)
- amiga3-davidkinder-dbwrender-src-ray-c: https://github.com/davidkinder/dbwrender/blob/748886b74441d6734ec4ae21f1c81a06968ca369/src/ray.c (Git blob 222aab6f656443060edd29def913622268521c71)
- amiga3-davidkinder-dbwrender-src-ray-vcxproj: https://github.com/davidkinder/dbwrender/blob/748886b74441d6734ec4ae21f1c81a06968ca369/src/ray.vcxproj (Git blob abfaf810324883c58949581a6fdf91dfbd845354)
- amiga3-djayuffe-amiga-stunt-car-racer-track-toolkit-docs-provenance-v4-md: https://github.com/djayuffe/amiga-stunt-car-racer-track-toolkit/blob/687701205d83b5e800a94549add1306ca9a5b30f/docs/PROVENANCE_V4.md (Git blob c24fd9dda35b4ff07ab18e7631e6b07445950ad9)
- amiga3-djayuffe-amiga-stunt-car-racer-track-toolkit-docs-re-status-md: https://github.com/djayuffe/amiga-stunt-car-racer-track-toolkit/blob/687701205d83b5e800a94549add1306ca9a5b30f/docs/RE_STATUS.md (Git blob a71b0544e05ea2cb6a8a13d037072306bd5b71a6)
- amiga3-djayuffe-amiga-stunt-car-racer-track-toolkit-docs-track804-verified-md: https://github.com/djayuffe/amiga-stunt-car-racer-track-toolkit/blob/687701205d83b5e800a94549add1306ca9a5b30f/docs/TRACK804_VERIFIED.md (Git blob 0158f2202407ba3e8368d2f7a9aec6b3774b917f)
- amiga3-djayuffe-amiga-stunt-car-racer-track-toolkit-github-workflows-ci-yml: https://github.com/djayuffe/amiga-stunt-car-racer-track-toolkit/blob/687701205d83b5e800a94549add1306ca9a5b30f/.github/workflows/ci.yml (Git blob a99c6f92ea7642b5b828140c3989ff1af123e9f8)
- amiga3-djayuffe-amiga-stunt-car-racer-track-toolkit-pyproject-toml: https://github.com/djayuffe/amiga-stunt-car-racer-track-toolkit/blob/687701205d83b5e800a94549add1306ca9a5b30f/pyproject.toml (Git blob 6a4d92ad5a694d97a427a7aaa17020ea6713c695)
- amiga3-djayuffe-amiga-stunt-car-racer-track-toolkit-readme-md: https://github.com/djayuffe/amiga-stunt-car-racer-track-toolkit/blob/687701205d83b5e800a94549add1306ca9a5b30f/README.md (Git blob f79b72ee2bdd52dc405c7ced8f19075a0ea6483f)
- amiga3-djayuffe-amiga-stunt-car-racer-track-toolkit-scrtool-track-py: https://github.com/djayuffe/amiga-stunt-car-racer-track-toolkit/blob/687701205d83b5e800a94549add1306ca9a5b30f/scrtool/track.py (Git blob 7cfa912b94a434c2e0e26e4b0b10d825502bd1ec)
- amiga3-mastatabs-symphonie-build-sh: https://github.com/mastatabs/symphonie/blob/c7d8854f9c9dafa9f74cb339838009072a20a404/build.sh (Git blob dc23d94c3f31ab79440c1fdba5fd75b27926e238)
- amiga3-mastatabs-symphonie-readme-md: https://github.com/mastatabs/symphonie/blob/c7d8854f9c9dafa9f74cb339838009072a20a404/README.md (Git blob 02ba7ac43ded2d0d227fb23f10d14ab9834105da)
- amiga3-olivierh59500-krytonegg-docs-fidelity-audit-md: https://github.com/olivierh59500/krytonegg/blob/efe9ae43b29f77b8e6445f59dccab2a29f71801e/docs/fidelity-audit.md (Git blob 6dbfbd7eff7753251873b5cdce9f96b6588e9a75)
- amiga3-olivierh59500-krytonegg-docs-port-status-md: https://github.com/olivierh59500/krytonegg/blob/efe9ae43b29f77b8e6445f59dccab2a29f71801e/docs/port-status.md (Git blob 222e114bc0a3d131430fd590a572d56979d89171)
- amiga3-olivierh59500-krytonegg-docs-validation-json: https://github.com/olivierh59500/krytonegg/blob/efe9ae43b29f77b8e6445f59dccab2a29f71801e/docs/validation.json (Git blob 6076ec5122aa375e0642ac1db7ba66e0b2c1fa56)
- amiga3-olivierh59500-krytonegg-go-mod: https://github.com/olivierh59500/krytonegg/blob/efe9ae43b29f77b8e6445f59dccab2a29f71801e/go.mod (Git blob 31aa82ca04c1e0b389b2615ba4a942476a3b436e)
- amiga3-olivierh59500-krytonegg-internal-game-physics-go: https://github.com/olivierh59500/krytonegg/blob/efe9ae43b29f77b8e6445f59dccab2a29f71801e/internal/game/physics.go (Git blob bb604924ee96cb5dccc54800ed47674f6eae6351)
- amiga3-olivierh59500-krytonegg-makefile: https://github.com/olivierh59500/krytonegg/blob/efe9ae43b29f77b8e6445f59dccab2a29f71801e/Makefile (Git blob 3e2669a0297ccd06cfb2554cee00809daff9f0c7)
- amiga3-olivierh59500-krytonegg-readme-md: https://github.com/olivierh59500/krytonegg/blob/efe9ae43b29f77b8e6445f59dccab2a29f71801e/README.md (Git blob e97c3c5420d21182ef173fb10bd9dc72e62466ae)
- amiga3-olivierh59500-krytonegg-scripts-android-env-sh: https://github.com/olivierh59500/krytonegg/blob/efe9ae43b29f77b8e6445f59dccab2a29f71801e/scripts/android-env.sh (Git blob 69a881573d5bd9c3078a0505a576da78f93df5c0)
- amiga3-olivierh59500-krytonegg-scripts-build-android-sh: https://github.com/olivierh59500/krytonegg/blob/efe9ae43b29f77b8e6445f59dccab2a29f71801e/scripts/build-android.sh (Git blob 9484f7f0973ba0080c5a4bb16d3568ddc7c39cf6)
- amiga3-rombust-methane-android-app-build-gradle-kts: https://github.com/rombust/methane/blob/c1694b0e5cac5be4d9002984ac1a722691c47580/android/app/build.gradle.kts (Git blob 15e1644772a111b4be36445a42a6ef3e523f875d)
- amiga3-rombust-methane-authors-txt: https://github.com/rombust/methane/blob/c1694b0e5cac5be4d9002984ac1a722691c47580/authors.txt (Git blob 390cb0a2a8c85ae112a94baab2431a6779d91c56)
- amiga3-rombust-methane-cmakelists-txt: https://github.com/rombust/methane/blob/c1694b0e5cac5be4d9002984ac1a722691c47580/CMakeLists.txt (Git blob b3b7b2403dbaa43689d6c1554c42846328100955)
- amiga3-rombust-methane-cmakepresets-json: https://github.com/rombust/methane/blob/c1694b0e5cac5be4d9002984ac1a722691c47580/CMakePresets.json (Git blob 115fb30eeb9ec0668260c395b2898f8e9b8a19af)
- amiga3-rombust-methane-history-txt: https://github.com/rombust/methane/blob/c1694b0e5cac5be4d9002984ac1a722691c47580/history.txt (Git blob 1d9a9f559edcbc4c9ed4a0c727a217636e8dd75e)
- amiga3-rombust-methane-readme-md: https://github.com/rombust/methane/blob/c1694b0e5cac5be4d9002984ac1a722691c47580/README.md (Git blob b6d9a09b23b899674b02aac7ba3a786f9c4216ff)
- amiga3-rombust-methane-sources-game-game-cpp: https://github.com/rombust/methane/blob/c1694b0e5cac5be4d9002984ac1a722691c47580/Sources/Game/game.cpp (Git blob 089ba76de2c147e25cf6b6ec753b982a860b804b)
- godlib-base-base-h: https://github.com/reservoirgods/godlib/blob/ae600aae192f35c8fe8a7e8164ec0e4caaa7e6e9/BASE/BASE.H (Git blob 6b5edf7ceb3ec2dceded39a7a8e50caeaa1b7159)
- godlib-godlib-mak: https://github.com/reservoirgods/godlib/blob/ae600aae192f35c8fe8a7e8164ec0e4caaa7e6e9/GODLIB.MAK (Git blob f181fc9dcf575f65f5f4ead1c02a5b97d7a3875c)
- godlib-makefile-platform-godlib_st-mf: https://github.com/reservoirgods/godlib/blob/ae600aae192f35c8fe8a7e8164ec0e4caaa7e6e9/MAKEFILE/PLATFORM/GODLIB_ST.MF (Git blob 5131cf0f895098e32997279d2a0f1f8613ad42bb)
- godlib-profiler-profiler-c: https://github.com/reservoirgods/godlib/blob/ae600aae192f35c8fe8a7e8164ec0e4caaa7e6e9/PROFILER/PROFILER.C (Git blob bce9b98583a917a9a685834252972339e736f4e0)
- godlib-readme-md: https://github.com/reservoirgods/godlib/blob/ae600aae192f35c8fe8a7e8164ec0e4caaa7e6e9/README.md (Git blob 60d06029aea601b034b567bc328b41d063783c0f)
- godlib-readme-txt: https://github.com/reservoirgods/godlib/blob/ae600aae192f35c8fe8a7e8164ec0e4caaa7e6e9/README.TXT (Git blob b7155c154f6b9bd4745eb84fbca16305937d82bc)
- godlib-system-system_s-s: https://github.com/reservoirgods/godlib/blob/ae600aae192f35c8fe8a7e8164ec0e4caaa7e6e9/SYSTEM/SYSTEM_S.S (Git blob f5b863dfe89832986be27db6a1d29ae77b657976)
- ice00-jc64--github-workflows-native-yml: https://github.com/ice00/jc64/blob/59988b819768e8c48f01664ed2ff082ee428de77/.github/workflows/native.yml (Git blob 5538c1b90726f92c7f0bd89735308bb6aa809221)
- ice00-jc64-build-github-xml: https://github.com/ice00/jc64/blob/59988b819768e8c48f01664ed2ff082ee428de77/build-github.xml (Git blob f0b3b874bedd7a8b0fc22c31571e4762d66f0892)
- ice00-jc64-readme-md: https://github.com/ice00/jc64/blob/59988b819768e8c48f01664ed2ff082ee428de77/README.md (Git blob 0bd9016b3d852e03ff65a30c312f9dfa4f8a3681)
- ice00-jc64-src-sw_emulator-software-ai-disassembleragent-java: https://github.com/ice00/jc64/blob/59988b819768e8c48f01664ed2ff082ee428de77/src/sw_emulator/software/ai/DisassemblerAgent.java (Git blob c84e1737228dc9084840b799064403fcf2342c34)
- ice00-jc64-src-sw_emulator-software-cpu-m6510dasm-java: https://github.com/ice00/jc64/blob/59988b819768e8c48f01664ed2ff082ee428de77/src/sw_emulator/software/cpu/M6510Dasm.java (Git blob 28f17b23b0c06441f5d540e69c4e446c5bd9bdda)
- ice00-jc64-src-sw_emulator-swing-main-targettype-java: https://github.com/ice00/jc64/blob/59988b819768e8c48f01664ed2ff082ee428de77/src/sw_emulator/swing/main/TargetType.java (Git blob f7eaae6e027dc2ae3694d944b5b5c9970c7207c2)
- mankind-dvk-nsshaft-c128-assets-fonts-readme-md: https://github.com/mankind-dvk/nsshaft-c128/blob/e4e58a56b72ec04256a7f72b6d09eb41e93f9623/assets/fonts/README.md (Git blob 486fefbbe9c9438f70ff30df61420e3b672eb74a)
- mankind-dvk-nsshaft-c128-build-ps1: https://github.com/mankind-dvk/nsshaft-c128/blob/e4e58a56b72ec04256a7f72b6d09eb41e93f9623/build.ps1 (Git blob 0b5a859be10d2645e075be0d59b5d05a157027dc)
- mankind-dvk-nsshaft-c128-readme-md: https://github.com/mankind-dvk/nsshaft-c128/blob/e4e58a56b72ec04256a7f72b6d09eb41e93f9623/README.md (Git blob a4c4293ec15d5d1ac67ebf3b64ef05ce2d62a1b2)
- mankind-dvk-nsshaft-c128-src-main-s: https://github.com/mankind-dvk/nsshaft-c128/blob/e4e58a56b72ec04256a7f72b6d09eb41e93f9623/src/main.s (Git blob 5abc8a7d707e469ba239a60cdb4689b8acf457fe)
- mankind-dvk-nsshaft-c128-tests-test_highscores-py: https://github.com/mankind-dvk/nsshaft-c128/blob/e4e58a56b72ec04256a7f72b6d09eb41e93f9623/tests/test_highscores.py (Git blob b54630a8e0a1388bbe565290f361cdfa4d6295a9)
- pack-ice-authors: https://github.com/larsbrinkhoff/pack-ice/blob/1f7da1fe22aeada06770356ac70cc67b00256122/AUTHORS (Git blob b57327342f85f42a90158333b22015c15d051ed1)
- pack-ice-hacking: https://github.com/larsbrinkhoff/pack-ice/blob/1f7da1fe22aeada06770356ac70cc67b00256122/HACKING (Git blob 522547b5b520175ccb553ba2096163194d0190db)
- pack-ice-ice_crunch-c: https://github.com/larsbrinkhoff/pack-ice/blob/1f7da1fe22aeada06770356ac70cc67b00256122/ice_crunch.c (Git blob 040dc7c31f1fdc5bcdb98ee9c45755dfada51417)
- pack-ice-ice_decrunch-c: https://github.com/larsbrinkhoff/pack-ice/blob/1f7da1fe22aeada06770356ac70cc67b00256122/ice_decrunch.c (Git blob d3f2af99568d95d0da7617ced97b6d34917a3a68)
- pack-ice-makefile: https://github.com/larsbrinkhoff/pack-ice/blob/1f7da1fe22aeada06770356ac70cc67b00256122/Makefile (Git blob b0aeb57137646f34905cd4c9b47f1703718fe156)
- pack-ice-readme: https://github.com/larsbrinkhoff/pack-ice/blob/1f7da1fe22aeada06770356ac70cc67b00256122/README (Git blob 0b184f71f1c10b179e6fd2087a3bd693d3b44cb4)
- pack-ice-testcases-check: https://github.com/larsbrinkhoff/pack-ice/blob/1f7da1fe22aeada06770356ac70cc67b00256122/testcases/check (Git blob 69292ccde1eaf4cf05189d86cdc26297b57e7f5c)
- pack-ice-testcases-readme: https://github.com/larsbrinkhoff/pack-ice/blob/1f7da1fe22aeada06770356ac70cc67b00256122/testcases/README (Git blob 038ff31a138408debdc726e0a7cf6979e6ca00d4)
- rabenstein-64-sh: https://github.com/byteproject/rabenstein/blob/8fec1f400bbfcb317dbdc8c7a77789fb781492dc/64.sh (Git blob 55b177edf825032d003bd4fa35c282ce90ec3afd)
- rabenstein-amiga-sh: https://github.com/byteproject/rabenstein/blob/8fec1f400bbfcb317dbdc8c7a77789fb781492dc/amiga.sh (Git blob 93836844f5f454a2665eb036fb7786efe978e650)
- rabenstein-atari_st-sh: https://github.com/byteproject/rabenstein/blob/8fec1f400bbfcb317dbdc8c7a77789fb781492dc/atari_st.sh (Git blob 8546c79061d29c9b88246c610ab60d620df0cf70)
- rabenstein-rabenstein-dsf: https://github.com/byteproject/rabenstein/blob/8fec1f400bbfcb317dbdc8c7a77789fb781492dc/rabenstein.dsf (Git blob d74aa26adc8b3f5b4459a0badd2c64d06edb3c4b)
- rabenstein-rabenstein-json: https://github.com/byteproject/rabenstein/blob/8fec1f400bbfcb317dbdc8c7a77789fb781492dc/rabenstein.json (Git blob ae222655aeb8b364a1e2edced7796e8479357b25)
- rabenstein-readme-md: https://github.com/byteproject/rabenstein/blob/8fec1f400bbfcb317dbdc8c7a77789fb781492dc/README.md (Git blob 6a044d89bd061600b1536fcb6bcb82d255070ab7)
- ricardoquesada-c128-the-race-makefile: https://github.com/ricardoquesada/c128-the-race/blob/4db38ff7adcce1b70794a5468128a0a812fd7ae5/Makefile (Git blob 2068ae2d1536b4c2a71e90f94d89882adf54b9d5)
- ricardoquesada-c128-the-race-readme-md: https://github.com/ricardoquesada/c128-the-race/blob/4db38ff7adcce1b70794a5468128a0a812fd7ae5/README.md (Git blob bef03d3badf80e74a8eabc6857b2582cc7ff0acf)
- ricardoquesada-c128-the-race-src-game-s: https://github.com/ricardoquesada/c128-the-race/blob/4db38ff7adcce1b70794a5468128a0a812fd7ae5/src/game.s (Git blob efaed656e1b7cbc22098010014fa5ea1c345c6f1)
- ricardoquesada-c128-the-race-src-main-s: https://github.com/ricardoquesada/c128-the-race/blob/4db38ff7adcce1b70794a5468128a0a812fd7ae5/src/main.s (Git blob 079ab9d70b5ad59f6fae8c6ee793aaeb4fe95c0f)
- sblendorio-gorilla-cpm-readme-md: https://github.com/sblendorio/gorilla-cpm/blob/0de936a27ff514c70b43362b5fae6ce3fbdbbf6d/README.md (Git blob 79959886ad25bce2253829f4f1297667e6e3ec48)
- sblendorio-gorilla-cpm-source-game-mod: https://github.com/sblendorio/gorilla-cpm/blob/0de936a27ff514c70b43362b5fae6ce3fbdbbf6d/source/game.mod (Git blob ac69d43eb314f28e6f6742860ff70958bec0d301)
- sblendorio-gorilla-cpm-source-main-mod: https://github.com/sblendorio/gorilla-cpm/blob/0de936a27ff514c70b43362b5fae6ce3fbdbbf6d/source/main.mod (Git blob 10ce50e697aa9e596c7016209d4c9efeb5e5c44a)
- sblendorio-gorilla-cpm-source-xterm-mod: https://github.com/sblendorio/gorilla-cpm/blob/0de936a27ff514c70b43362b5fae6ce3fbdbbf6d/source/xterm.mod (Git blob bc8cbbe8b9f3d5614db29fd09c9dd3bfc5d416c0)
- shewitt-au-negentropy-negentropy-m6502decoder-py: https://github.com/shewitt-au/negentropy/blob/04b86f701decad4912dc50cf32c906b9644d4f6f/negentropy/M6502decoder.py (Git blob f02f63c7c359e1d838888ae7ffff267bee325a87)
- shewitt-au-negentropy-negentropy-negentropy-py: https://github.com/shewitt-au/negentropy/blob/04b86f701decad4912dc50cf32c906b9644d4f6f/negentropy/negentropy.py (Git blob d05fbadc899617e169a66e8c138d556fcc4a2693)
- shewitt-au-negentropy-readme-md: https://github.com/shewitt-au/negentropy/blob/04b86f701decad4912dc50cf32c906b9644d4f6f/README.md (Git blob 991fae7a19e158f4e8996f4d37daa6ce8442e5f5)
- shewitt-au-negentropy-setup-py: https://github.com/shewitt-au/negentropy/blob/04b86f701decad4912dc50cf32c906b9644d4f6f/setup.py (Git blob 3df0967cab4423a6f747cc5b1d2f016b4751f0c7)
- udump-makefile: https://github.com/mikrosk/udump/blob/11c7ff9492f51918d07251b000133bf9bd12d6bf/Makefile (Git blob 7cdcbf1f996bf8d92a2a353ebabdc7d6ddfcd8a4)
- udump-readme-txt: https://github.com/mikrosk/udump/blob/11c7ff9492f51918d07251b000133bf9bd12d6bf/README.txt (Git blob 8335b585a15a310610be147fb0b8d6b48a7a0845)
- udump-udump-c: https://github.com/mikrosk/udump/blob/11c7ff9492f51918d07251b000133bf9bd12d6bf/udump.c (Git blob ca08bcf5883316ae07876a31c356a2dc15d04d4b)

## Sources

```json
[
  {
    "first_indexed": "2026-10-11",
    "id": "third-amiga-krypton-egg-native-go-reconstruction",
    "kind": "github-repository",
    "last_reviewed": "2026-10-11",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "One coherent repository reconstructs HitSoft's Krypton Egg from a specified Amiga ADF, retaining 60 level layouts, six combats, recovered graphics and audio, and original-format custom levels. The original executable is used for offline investigation only. Inspected pinned snapshot efe9ae43b29f77b8e6445f59dccab2a29f71801e.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/olivierh59500/krytonegg"
  },
  {
    "first_indexed": "2026-10-11",
    "id": "third-amiga-stunt-car-racer-amiga-track-toolkit",
    "kind": "github-repository",
    "last_reviewed": "2026-10-11",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "The root is an independent Stunt Car Racer Amiga research/toolkit project by Ulf Bertilsson. It combines installable Python commands, disk-evidence inspection, track codecs, guarded patch transactions, Blender import and a standalone browser inspector as one coherent project. Inspected pinned snapshot 687701205d83b5e800a94549add1306ca9a5b30f.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/djayuffe/Amiga-stunt-car-racer-track-toolkit"
  },
  {
    "first_indexed": "2026-10-11",
    "id": "third-amiga-symphonie-amiga-tracker-source-restoration",
    "kind": "github-repository",
    "last_reviewed": "2026-10-11",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "MastaTabs preserves and reorganizes Patrick Meng's Symphonie Amiga music-tracker source, plugin sources, manuals and historical binaries. The main assembly identifies version 3.3d, and the README describes the 256-channel tracker source as made compilable. Inspected pinned snapshot c7d8854f9c9dafa9f74cb339838009072a20a404.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/MastaTabs/Symphonie"
  },
  {
    "first_indexed": "2026-10-11",
    "id": "third-amiga-dbwrender-windows-source-port",
    "kind": "github-repository",
    "last_reviewed": "2026-10-11",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "David Kinder maintains a Windows port of David Wecker's DBW-Render, through John H. Lowery's MS-DOS adaptation. The root contains the C ray tracer, a rewritten C++ display application, scene files and build projects. The author traces the earlier history to DEC VAX and Amiga. Inspected pinned snapshot 748886b74441d6734ec4ae21f1c81a06968ca369.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/DavidKinder/DBWRender"
  },
  {
    "first_indexed": "2026-10-11",
    "id": "third-amiga-super-methane-brothers-canonical-conversion",
    "kind": "github-repository",
    "last_reviewed": "2026-10-11",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "The canonical repository publishes Super Methane Brothers for Linux, Windows and Android; authors.txt identifies maintainer Mark Page as the original Amiga game's programmer. The old SourceForge developer page links this GitHub root. Current source identifies v3.0.3, matching the October 2026 release. Inspected pinned snapshot c1694b0e5cac5be4d9002984ac1a722691c47580.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/rombust/Methane"
  },
  {
    "first_indexed": "2026-10-11",
    "id": "github-reservoirgods-godlib",
    "kind": "github-repository",
    "last_reviewed": "2026-10-11",
    "open_task_ids": [],
    "projects_promoted": [
      "godlib-atari-development-library"
    ],
    "reason": "A coherent Reservoir Gods C/68k development library with concrete Atari system integration, graphics/audio/asset support and interrupt-driven profiling; one root-level tooling record.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/ReservoirGods/GODLIB"
  },
  {
    "first_indexed": "2026-10-11",
    "id": "github-larsbrinkhoff-pack-ice",
    "kind": "github-repository",
    "last_reviewed": "2026-10-11",
    "open_task_ids": [],
    "projects_promoted": [
      "pack-ice-atari-compression-library"
    ],
    "reason": "A substantive C ICE encoder/decoder with command-line tools, format-analysis notes and regression fixtures, directly relevant to Atari ST assets; CPU claims and unrun tests remain conservative.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/larsbrinkhoff/pack-ice"
  },
  {
    "first_indexed": "2026-10-11",
    "id": "github-mikrosk-udump",
    "kind": "github-repository",
    "last_reviewed": "2026-10-11",
    "open_task_ids": [],
    "projects_promoted": [
      "udump-atari-tos-rom-preservation"
    ],
    "reason": "Maintained native TOS ROM preservation utility with version/machine detection, EmuTOS and CT60 handling, a current binary release and explicit 68000 build target.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/mikrosk/uDump"
  },
  {
    "first_indexed": "2026-10-11",
    "id": "github-byteproject-rabenstein",
    "kind": "github-repository",
    "last_reviewed": "2026-10-11",
    "open_task_ids": [],
    "projects_promoted": [
      "rabenstein-daad-original-adventure"
    ],
    "reason": "Creator-published substantial DAAD game source and platform packaging for a released original adventure; one coherent root, with missing build tools and restricted educational source license explicitly disclosed.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/ByteProject/Rabenstein"
  },
  {
    "first_indexed": "2026-10-11",
    "id": "github-daad-adventure-writer-daad",
    "kind": "github-repository",
    "last_reviewed": "2026-10-11",
    "open_task_ids": [
      "task-review-daad-drc-toolchain-graph"
    ],
    "projects_promoted": [],
    "reason": "DAAD original multi-machine adventure-writing system; the primary README says interpreter source is not provided. Inspect the actual distributed tools and scope before adding a coherent root record.",
    "review_state": "partial",
    "source": "https://github.com/daad-adventure-writer/daad"
  },
  {
    "first_indexed": "2026-10-11",
    "id": "github-utodev-drc",
    "kind": "github-repository",
    "last_reviewed": "2026-10-11",
    "open_task_ids": [
      "task-review-daad-drc-toolchain-graph"
    ],
    "projects_promoted": [],
    "reason": "The canonical DRC README identifies a modern replacement compiler for DAAD, plus MCRF replacement and DAADMAKER media tooling. Source implementation and build/CPU output need a full audit.",
    "review_state": "partial",
    "source": "https://github.com/Utodev/DRC"
  },
  {
    "first_indexed": "2026-10-11",
    "id": "github-freemint-libcmini",
    "kind": "github-repository",
    "last_reviewed": "2026-10-11",
    "open_task_ids": [
      "task-review-libcmini-native-runtime"
    ],
    "projects_promoted": [],
    "reason": "uDump build dependency. Primary README describes an independent small-footprint m68k-atari-mint C library with released binaries and multiple ABI/CPU variants. Review source and lineage before adding it.",
    "review_state": "partial",
    "source": "https://github.com/freemint/libcmini"
  },
  {
    "first_indexed": "2026-10-11",
    "id": "github-ice00-jc64",
    "kind": "github-repository",
    "last_reviewed": "2026-10-11",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Substantial interactive disassembly/annotation/reassembly infrastructure with multi-machine decoders and inspected successful upstream JAR/native build steps. Preserve the coherent emulator/disassembler root, not its many sample analyses as separate projects.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/ice00/jc64"
  },
  {
    "first_indexed": "2026-10-11",
    "id": "github-shewitt-au-negentropy",
    "kind": "github-repository",
    "last_reviewed": "2026-10-11",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "A distinct, substantive C64 disassembly publishing tool combines configured machine-code/BASIC analysis, linked HTML and charset rendering. Canonical package identity and non-fork repository verified; no splitting of decoder/template components.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/shewitt-au/negentropy"
  },
  {
    "first_indexed": "2026-10-11",
    "id": "github-mankind-dvk-nsshaft-c128",
    "kind": "github-repository",
    "last_reviewed": "2026-10-11",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Substantial native C128/8502 game implementation with physics, multiple platform hazards, SID music and persistent scores. Direct hardware assembly proves a native execution path; retain as a qualified prototype with unrun build/tests and unknown development-AI use.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/Mankind-dvk/nsshaft-c128"
  },
  {
    "first_indexed": "2026-10-11",
    "id": "github-ricardoquesada-c128-the-race",
    "kind": "github-repository",
    "last_reviewed": "2026-10-11",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "A previously untracked substantive C128 game reconstruction regenerates The Race from binary inputs, with labelled gameplay/music/intro code and a same-lineage native C64 adaptation. One root covers both outputs; recipes and committed disks are not promoted to test claims.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/ricardoquesada/c128-the-race"
  },
  {
    "first_indexed": "2026-10-11",
    "id": "github-sblendorio-gorilla-cpm",
    "kind": "github-repository",
    "last_reviewed": "2026-10-11",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Distinct substantial Modula-2 implementation of Gorillas with concrete C128 CP/M terminal support and distributed platform disks. It is separate from the tracked C64 BASIC rewrite; count the coherent port once across its multiple terminal/platform variants.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/sblendorio/gorilla-cpm"
  }
]
```

## Tasks

```json
[
  {
    "created_at": "2026-10-11",
    "description": "Audit canonical DAAD and DRC toolchain roots linked by Rabenstein; distinguish distributed historical interpreters, modern compiler implementation and already tracked MALUVA.",
    "id": "task-review-daad-drc-toolchain-graph",
    "last_reviewed": "2026-10-11",
    "notes": "DAAD README says interpreter source is absent; DRC has its own src tree and compiler/media tools. Inspect implementations and actual build evidence, keeping coherent roots rather than every target interpreter. Rabenstein’s historical DRC URL redirects to Utodev/DRC. Primary README snapshots: https://github.com/daad-adventure-writer/daad/blob/4a7e745235a12af5b397902dbd9214bc930c7680/README.md and https://github.com/Utodev/DRC/blob/71df4e54b7db39b5e7ceeb3b7e5d7dea1cebda95/README.",
    "priority": "normal",
    "source_ids": [
      "github-daad-adventure-writer-daad",
      "github-utodev-drc"
    ],
    "state": "open"
  },
  {
    "created_at": "2026-10-11",
    "description": "Review libcmini source, multilib output and relationship to Atari runtime/toolchain records.",
    "id": "task-review-libcmini-native-runtime",
    "last_reviewed": "2026-10-11",
    "notes": "Follow uDump’s concrete libcmini dependency. Verify current Makefile, startup and selected C implementations; README declares 68000 and ColdFire/ABI variants but no independent build was run. Primary README snapshot: https://github.com/freemint/libcmini/blob/77eb5e1e0129c5dad932e08e50d893cf792a5347/README.md.",
    "priority": "normal",
    "source_ids": [
      "github-freemint-libcmini"
    ],
    "state": "open"
  }
]
```

## Decisions

```json
[
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/olivierh59500/krytonegg/blob/efe9ae43b29f77b8e6445f59dccab2a29f71801e/docs/port-status.md",
      "https://github.com/olivierh59500/krytonegg/blob/efe9ae43b29f77b8e6445f59dccab2a29f71801e/internal/game/physics.go",
      "https://github.com/olivierh59500/krytonegg/blob/efe9ae43b29f77b8e6445f59dccab2a29f71801e/docs/fidelity-audit.md"
    ],
    "id": "promote-krypton-egg-native-go-reconstruction",
    "project_ids": [
      "krypton-egg-native-go-reconstruction"
    ],
    "reason": "This is a native Go/Ebitengine game rewrite derived from original-code and data analysis. The inspected physics.go implements ball motion and collision directly in Go. Port status explicitly says original instructions are neither executed nor interpreted at runtime; FS-UAE and Ghidra are offline reference tools, so this is not a game-specific CPU-emulation wrapper.",
    "reviewed_at": "2026-10-11",
    "source_ids": [
      "third-amiga-krypton-egg-native-go-reconstruction"
    ],
    "title": "Krypton Egg — native Go reconstruction",
    "url": "https://github.com/olivierh59500/krytonegg"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/djayuffe/Amiga-stunt-car-racer-track-toolkit/blob/687701205d83b5e800a94549add1306ca9a5b30f/scrtool/track.py",
      "https://github.com/djayuffe/Amiga-stunt-car-racer-track-toolkit/blob/687701205d83b5e800a94549add1306ca9a5b30f/docs/TRACK804_VERIFIED.md",
      "https://github.com/djayuffe/Amiga-stunt-car-racer-track-toolkit/blob/687701205d83b5e800a94549add1306ca9a5b30f/README.md"
    ],
    "id": "promote-stunt-car-racer-amiga-track-toolkit",
    "project_ids": [
      "stunt-car-racer-amiga-track-toolkit"
    ],
    "reason": "The inspected track.py implements an 804-byte big-endian native track decoder/encoder with preservation of all 100 slots and an editor-native backing record. This materially combines game-data reconstruction with useful asset and disk-analysis tooling; it does not implement a playable game engine.",
    "reviewed_at": "2026-10-11",
    "source_ids": [
      "third-amiga-stunt-car-racer-amiga-track-toolkit"
    ],
    "title": "Stunt Car Racer — Amiga track analysis and editing toolkit",
    "url": "https://github.com/djayuffe/Amiga-stunt-car-racer-track-toolkit"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/MastaTabs/Symphonie/blob/c7d8854f9c9dafa9f74cb339838009072a20a404/Symphonie%20Source.Assembler",
      "https://github.com/MastaTabs/Symphonie/blob/c7d8854f9c9dafa9f74cb339838009072a20a404/build.sh",
      "https://github.com/MastaTabs/Symphonie/blob/c7d8854f9c9dafa9f74cb339838009072a20a404/doc/Symphonie_E.guide"
    ],
    "id": "promote-symphonie-amiga-tracker-source-restoration",
    "project_ids": [
      "symphonie-amiga-tracker-source-restoration"
    ],
    "reason": "This is restoration/preservation of original tracker application source with a modern assembler/linker build, rather than a decompilation. The main application, DSP plugins and old binaries belong to the same project root and are not split into separate catalogue records.",
    "reviewed_at": "2026-10-11",
    "source_ids": [
      "third-amiga-symphonie-amiga-tracker-source-restoration"
    ],
    "title": "Symphonie — Amiga music-tracker source restoration",
    "url": "https://github.com/MastaTabs/Symphonie"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/DavidKinder/DBWRender/blob/748886b74441d6734ec4ae21f1c81a06968ca369/README.md",
      "https://github.com/DavidKinder/DBWRender/blob/748886b74441d6734ec4ae21f1c81a06968ca369/src/ray.c"
    ],
    "id": "promote-dbwrender-windows-source-port",
    "project_ids": [
      "dbwrender-windows-source-port"
    ],
    "reason": "This is a source-derived native application port and preservation of a legacy ray tracer. The C source retains original 1987 attribution and the IBM-PC port history. No binary-derived decompilation or reverse-engineering methodology is asserted, so the work-kind list is left empty rather than mislabelling a source port.",
    "reviewed_at": "2026-10-11",
    "source_ids": [
      "third-amiga-dbwrender-windows-source-port"
    ],
    "title": "DBW-Render — preserved Amiga ray-tracer Windows port",
    "url": "https://github.com/DavidKinder/DBWRender"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/rombust/Methane/blob/c1694b0e5cac5be4d9002984ac1a722691c47580/README.md",
      "https://github.com/rombust/Methane/blob/c1694b0e5cac5be4d9002984ac1a722691c47580/Sources/Game/game.cpp",
      "https://github.com/rombust/Methane/blob/c1694b0e5cac5be4d9002984ac1a722691c47580/CMakeLists.txt",
      "https://github.com/rombust/Methane/blob/c1694b0e5cac5be4d9002984ac1a722691c47580/authors.txt"
    ],
    "id": "promote-super-methane-brothers-canonical-conversion",
    "project_ids": [
      "super-methane-brothers-canonical-conversion"
    ],
    "reason": "This is the original programmer's native C++ game conversion, not evidence of a newly discovered assembly decompilation. The inspected game.cpp implements game state directly, and the CMake build links native game, platform and Vulkan sources. Keep all supported outputs under the canonical root and leave reconstruction-method enums empty rather than claiming unproven RE provenance.",
    "reviewed_at": "2026-10-11",
    "source_ids": [
      "third-amiga-super-methane-brothers-canonical-conversion"
    ],
    "title": "Super Methane Brothers — original-author native conversion",
    "url": "https://github.com/rombust/Methane"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/ReservoirGods/GODLIB/blob/ae600aae192f35c8fe8a7e8164ec0e4caaa7e6e9/README.md",
      "https://github.com/ReservoirGods/GODLIB/blob/ae600aae192f35c8fe8a7e8164ec0e4caaa7e6e9/README.TXT",
      "https://github.com/ReservoirGods/GODLIB/blob/ae600aae192f35c8fe8a7e8164ec0e4caaa7e6e9/GODLIB.MAK",
      "https://github.com/ReservoirGods/GODLIB/blob/ae600aae192f35c8fe8a7e8164ec0e4caaa7e6e9/SYSTEM/SYSTEM_S.S",
      "https://github.com/ReservoirGods/GODLIB/blob/ae600aae192f35c8fe8a7e8164ec0e4caaa7e6e9/PROFILER/PROFILER.C",
      "https://github.com/ReservoirGods/GODLIB/blob/ae600aae192f35c8fe8a7e8164ec0e4caaa7e6e9/MAKEFILE/PLATFORM/GODLIB_ST.MF",
      "https://github.com/ReservoirGods/GODLIB/blob/ae600aae192f35c8fe8a7e8164ec0e4caaa7e6e9/BASE/BASE.H",
      "https://github.com/ReservoirGods/GODLIB/commits/ae600aae192f35c8fe8a7e8164ec0e4caaa7e6e9"
    ],
    "id": "2026-10-11-third-promote-godlib-atari-development-library",
    "project_ids": [
      "godlib-atari-development-library"
    ],
    "reason": "A coherent Reservoir Gods C/68k development library with concrete Atari system integration, graphics/audio/asset support and interrupt-driven profiling; one root-level tooling record.",
    "reviewed_at": "2026-10-11",
    "source_ids": [
      "github-reservoirgods-godlib"
    ],
    "title": "GODLIB — Atari ST native development and profiling library",
    "url": "https://github.com/ReservoirGods/GODLIB"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/larsbrinkhoff/pack-ice/blob/1f7da1fe22aeada06770356ac70cc67b00256122/README",
      "https://github.com/larsbrinkhoff/pack-ice/blob/1f7da1fe22aeada06770356ac70cc67b00256122/AUTHORS",
      "https://github.com/larsbrinkhoff/pack-ice/blob/1f7da1fe22aeada06770356ac70cc67b00256122/Makefile",
      "https://github.com/larsbrinkhoff/pack-ice/blob/1f7da1fe22aeada06770356ac70cc67b00256122/HACKING",
      "https://github.com/larsbrinkhoff/pack-ice/blob/1f7da1fe22aeada06770356ac70cc67b00256122/testcases/README",
      "https://github.com/larsbrinkhoff/pack-ice/blob/1f7da1fe22aeada06770356ac70cc67b00256122/ice_crunch.c",
      "https://github.com/larsbrinkhoff/pack-ice/blob/1f7da1fe22aeada06770356ac70cc67b00256122/ice_decrunch.c",
      "https://github.com/larsbrinkhoff/pack-ice/blob/1f7da1fe22aeada06770356ac70cc67b00256122/testcases/check",
      "https://github.com/larsbrinkhoff/pack-ice/commits/1f7da1fe22aeada06770356ac70cc67b00256122"
    ],
    "id": "2026-10-11-third-promote-pack-ice-atari-compression-library",
    "project_ids": [
      "pack-ice-atari-compression-library"
    ],
    "reason": "A substantive C ICE encoder/decoder with command-line tools, format-analysis notes and regression fixtures, directly relevant to Atari ST assets; CPU claims and unrun tests remain conservative.",
    "reviewed_at": "2026-10-11",
    "source_ids": [
      "github-larsbrinkhoff-pack-ice"
    ],
    "title": "pack-ice — Atari ICE compression library and utilities",
    "url": "https://github.com/larsbrinkhoff/pack-ice"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/mikrosk/uDump/blob/11c7ff9492f51918d07251b000133bf9bd12d6bf/README.txt",
      "https://github.com/mikrosk/uDump/blob/11c7ff9492f51918d07251b000133bf9bd12d6bf/udump.c",
      "https://github.com/mikrosk/uDump/blob/11c7ff9492f51918d07251b000133bf9bd12d6bf/Makefile",
      "https://github.com/mikrosk/uDump/releases/tag/1.03",
      "https://github.com/mikrosk/uDump/releases/tag/1.01",
      "https://github.com/mikrosk/uDump/commits/11c7ff9492f51918d07251b000133bf9bd12d6bf"
    ],
    "id": "2026-10-11-third-promote-udump-atari-tos-rom-preservation",
    "project_ids": [
      "udump-atari-tos-rom-preservation"
    ],
    "reason": "Maintained native TOS ROM preservation utility with version/machine detection, EmuTOS and CT60 handling, a current binary release and explicit 68000 build target.",
    "reviewed_at": "2026-10-11",
    "source_ids": [
      "github-mikrosk-udump"
    ],
    "title": "uDump — native Atari TOS ROM dumper",
    "url": "https://github.com/mikrosk/uDump"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/ByteProject/Rabenstein/blob/8fec1f400bbfcb317dbdc8c7a77789fb781492dc/README.md",
      "https://github.com/ByteProject/Rabenstein/blob/8fec1f400bbfcb317dbdc8c7a77789fb781492dc/rabenstein.dsf",
      "https://github.com/ByteProject/Rabenstein/blob/8fec1f400bbfcb317dbdc8c7a77789fb781492dc/atari_st.sh",
      "https://github.com/ByteProject/Rabenstein/blob/8fec1f400bbfcb317dbdc8c7a77789fb781492dc/amiga.sh",
      "https://github.com/ByteProject/Rabenstein/blob/8fec1f400bbfcb317dbdc8c7a77789fb781492dc/64.sh",
      "https://8bitgames.itch.io/rabenstein",
      "https://github.com/ByteProject/Rabenstein/commits/8fec1f400bbfcb317dbdc8c7a77789fb781492dc"
    ],
    "id": "2026-10-11-third-promote-rabenstein-daad-original-adventure",
    "project_ids": [
      "rabenstein-daad-original-adventure"
    ],
    "reason": "Creator-published substantial DAAD game source and platform packaging for a released original adventure; one coherent root, with missing build tools and restricted educational source license explicitly disclosed.",
    "reviewed_at": "2026-10-11",
    "source_ids": [
      "github-byteproject-rabenstein"
    ],
    "title": "The Curse of Rabenstein — original multi-platform DAAD adventure",
    "url": "https://github.com/ByteProject/Rabenstein"
  },
  {
    "decision": "duplicate",
    "evidence_urls": [
      "https://api.github.com/repos/daad-adventure-writer/MALUVA",
      "https://github.com/Utodev/MALUVA",
      "https://github.com/ByteProject/Rabenstein/blob/8fec1f400bbfcb317dbdc8c7a77789fb781492dc/README.md"
    ],
    "id": "2026-10-11-third-maluva-owner-alias",
    "project_ids": [
      "maluva-daad-native-storage-extension"
    ],
    "reason": "GitHub returned a permanent redirect to repository ID 129590533; get_repo resolved that same ID to Utodev/MALUVA, already tracked. The historical Rabenstein dependency link is an alias, not another extension project.",
    "reviewed_at": "2026-10-11",
    "source_ids": [
      "github-utodev-maluva"
    ],
    "title": "MALUVA former daad-adventure-writer repository URL",
    "url": "https://github.com/daad-adventure-writer/MALUVA"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/ice00/jc64/blob/59988b819768e8c48f01664ed2ff082ee428de77/README.md",
      "https://github.com/ice00/jc64/tree/59988b819768e8c48f01664ed2ff082ee428de77"
    ],
    "id": "2026-10-11-third-pass-promote-jc64dis-java-retro-disassembler",
    "project_ids": [
      "jc64dis-java-retro-disassembler"
    ],
    "reason": "Substantial interactive disassembly/annotation/reassembly infrastructure with multi-machine decoders and inspected successful upstream JAR/native build steps. Preserve the coherent emulator/disassembler root, not its many sample analyses as separate projects.",
    "reviewed_at": "2026-10-11",
    "source_ids": [
      "github-ice00-jc64"
    ],
    "title": "JC64dis — interactive Commodore disassembler and analysis workbench",
    "url": "https://github.com/ice00/jc64"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/shewitt-au/negentropy/blob/04b86f701decad4912dc50cf32c906b9644d4f6f/README.md",
      "https://github.com/shewitt-au/negentropy/tree/04b86f701decad4912dc50cf32c906b9644d4f6f"
    ],
    "id": "2026-10-11-third-pass-promote-negentropy-c64-html-disassembler",
    "project_ids": [
      "negentropy-c64-html-disassembler"
    ],
    "reason": "A distinct, substantive C64 disassembly publishing tool combines configured machine-code/BASIC analysis, linked HTML and charset rendering. Canonical package identity and non-fork repository verified; no splitting of decoder/template components.",
    "reviewed_at": "2026-10-11",
    "source_ids": [
      "github-shewitt-au-negentropy"
    ],
    "title": "Negentropy — annotated C64 disassembly and linked HTML generator",
    "url": "https://github.com/shewitt-au/negentropy"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/Mankind-dvk/nsshaft-c128/blob/e4e58a56b72ec04256a7f72b6d09eb41e93f9623/README.md",
      "https://github.com/Mankind-dvk/nsshaft-c128/tree/e4e58a56b72ec04256a7f72b6d09eb41e93f9623"
    ],
    "id": "2026-10-11-third-pass-promote-nsshaft-native-c128-prototype",
    "project_ids": [
      "nsshaft-native-c128-prototype"
    ],
    "reason": "Substantial native C128/8502 game implementation with physics, multiple platform hazards, SID music and persistent scores. Direct hardware assembly proves a native execution path; retain as a qualified prototype with unrun build/tests and unknown development-AI use.",
    "reviewed_at": "2026-10-11",
    "source_ids": [
      "github-mankind-dvk-nsshaft-c128"
    ],
    "title": "NS-Shaft — native C128 descent-game prototype",
    "url": "https://github.com/Mankind-dvk/nsshaft-c128"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/ricardoquesada/c128-the-race/blob/4db38ff7adcce1b70794a5468128a0a812fd7ae5/README.md",
      "https://github.com/ricardoquesada/c128-the-race/tree/4db38ff7adcce1b70794a5468128a0a812fd7ae5"
    ],
    "id": "2026-10-11-third-pass-promote-the-race-c128-reconstruction",
    "project_ids": [
      "the-race-c128-reconstruction"
    ],
    "reason": "A previously untracked substantive C128 game reconstruction regenerates The Race from binary inputs, with labelled gameplay/music/intro code and a same-lineage native C64 adaptation. One root covers both outputs; recipes and committed disks are not promoted to test claims.",
    "reviewed_at": "2026-10-11",
    "source_ids": [
      "github-ricardoquesada-c128-the-race"
    ],
    "title": "The Race — C128 binary reconstruction and C64 adaptation",
    "url": "https://github.com/ricardoquesada/c128-the-race"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/sblendorio/gorilla-cpm/blob/0de936a27ff514c70b43362b5fae6ce3fbdbbf6d/README.md",
      "https://github.com/sblendorio/gorilla-cpm/tree/0de936a27ff514c70b43362b5fae6ce3fbdbbf6d"
    ],
    "id": "2026-10-11-third-pass-promote-gorilla-cpm-modula2-port",
    "project_ids": [
      "gorilla-cpm-modula2-port"
    ],
    "reason": "Distinct substantial Modula-2 implementation of Gorillas with concrete C128 CP/M terminal support and distributed platform disks. It is separate from the tracked C64 BASIC rewrite; count the coherent port once across its multiple terminal/platform variants.",
    "reviewed_at": "2026-10-11",
    "source_ids": [
      "github-sblendorio-gorilla-cpm"
    ],
    "title": "Gorillas — Turbo Modula-2 port for C128 and CP/M systems",
    "url": "https://github.com/sblendorio/gorilla-cpm"
  }
]
```

## Research event notes

User-requested third discovery pass screened against the 1,951-project catalogue at d52199e5345045fb8a00bcfc13ffc595f1fbd28b. Fourteen coherent repository roots qualify: five Amiga-focused, four Atari ST-family including cross-platform Rabenstein, and five C64/C128-focused. Original-source restoration, native ports/homebrew, binary-derived reconstruction and directly useful analysis/development tools are distinguished. No game-specific CPU-emulation wrapper is promoted. Candidate builds, tests, gameplay, hardware and byte comparisons were not run locally: observed upstream CI and explicit author reports are identified separately from declared recipes. Unknown AI use and byte matching remain null. Agent instruction files, branch names, analysis-AI features and automated game players are not evidence of actual development-AI use. Canonical original-author Super Methane Brothers is preferred over a derivative console-port root. Rabenstein is counted once across platforms and its restrictive source licence is retained. Exact source/output CPUs and runnable hardware minima are assessed independently. Existing projects, including separately corrected AI attribution and AGK, are not edited by this pass. No schedules or unrelated code are changed.
