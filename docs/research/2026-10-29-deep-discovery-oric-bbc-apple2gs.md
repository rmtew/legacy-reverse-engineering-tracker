# Oric, BBC Micro and Apple IIgs discovery and audit pass

Promoted six evidence-reviewed retro-development projects and recorded two specific deferred leads

Date: 2026-10-29 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- stop-press-bbc-disassembly / Build (reviewed): No execution test or minimum hardware claim was found in the reviewed files.
- stop-press-bbc-disassembly / Runtime profiles (no-evidence-found): The README and build script identify BBC Micro ROM outputs but do not state a verified minimum machine, RAM, ROM or sideways-ROM configuration; none was inferred.
- stop-press-bbc-disassembly / AI (no-evidence-found): The reviewed README, build script and latest commit metadata contain no explicit development-AI disclosure; this does not establish non-use.
- grime6502-bbc-restoration / Build (reviewed): No independent execution, gameplay or byte comparison was performed; the explicit improvements mean the original binary should not be assumed to match.
- grime6502-bbc-restoration / Runtime profiles (no-evidence-found): The reviewed README names the BBC Micro and SSD output but states no minimum model, RAM or ROM requirements; none were inferred.
- grime6502-bbc-restoration / AI (no-evidence-found): The reviewed README and latest commit metadata contain no explicit development-AI disclosure; this does not establish non-use.
- beeb-6502-timing-tests / Build (reviewed): The reviewed README did not establish a source-build command, so compilability remains unknown.
- beeb-6502-timing-tests / Runtime profiles (no-evidence-found): The author reports tests on BBC B and Master 128 and warns about the 1 MHz bus, but does not claim either machine as a minimum hardware profile; no minimum CPU, RAM or ROM was inferred.
- beeb-6502-timing-tests / AI (no-evidence-found): The reviewed README and latest commit metadata contain no explicit development-AI disclosure; this does not establish non-use.
- lib6502-jit / Target CPU (no-evidence-found): The reviewed documentation says LLVM emits host code but does not restrict or enumerate host output architectures; none was inferred from LLVM or the implementation language.
- lib6502-jit / Build (no-evidence-found): The reviewed project overview and imported lib6502 documentation establish implementation scope and compatibility limits but not a verified current build or runnable artifact.
- lib6502-jit / AI (no-evidence-found): The reviewed README and first public release commit metadata contain no explicit development-AI disclosure; this does not establish non-use.
- vscode-osdk-oric / Build (reviewed): No independent package build was run, so compilability remains unknown.
- edasm-prodos-assembler-tools-disassembly / Build (needs-research): The repository describes the source as for viewing and does not report a verified successful or byte-identical rebuild. Next check: Assemble the five documented source files with the stated Release 1.1 environment and compare each output with the corresponding original program.
- edasm-prodos-assembler-tools-disassembly / Runtime profiles (no-evidence-found): The reviewed material identifies ProDOS 8 and the original Apple II package but states no minimum model, CPU, RAM or ROM requirements; none were inferred.
- edasm-prodos-assembler-tools-disassembly / AI (no-evidence-found): The reviewed README, source headers and latest commit metadata contain no explicit development-AI disclosure; this does not establish non-use.

## Stop Press v1.9 — BBC Micro ROM disassembly and PALPROM rebuild

Project ID: stop-press-bbc-disassembly · Overall audit: reviewed

### Typed catalogue values

```json
{
  "ai": {
    "tools": [],
    "usage": null
  },
  "build": {
    "byte_exact": true,
    "compilable": true,
    "playable": null,
    "runnable": null
  },
  "display_title": "Stop Press v1.9 — BBC Micro ROM disassembly and PALPROM rebuild",
  "id": "stop-press-bbc-disassembly",
  "last_activity": "2024-09-08",
  "last_checked": "2026-10-29",
  "re_started": null,
  "reconstructed_languages": [
    "6502 assembly",
    "Python",
    "Shell"
  ],
  "record_class": "subject",
  "repo": "https://github.com/ZornsLemma/stop-press-disassembly",
  "runtime_profiles": [],
  "source_cpu": [
    "6502"
  ],
  "source_language": [
    "6502 machine code"
  ],
  "source_platforms": [
    "BBC Micro"
  ],
  "status": "Both source ROMs rebuild byte-for-byte; a combined PALPROM image is also produced",
  "subjects": [
    "Stop Press v1.9"
  ],
  "tags": [
    "BBC Micro",
    "Stop Press",
    "Watford Electronics",
    "PALPROM"
  ],
  "target_cpu": [
    "6502"
  ],
  "target_kinds": [
    "application"
  ],
  "target_platforms": [
    "BBC Micro"
  ],
  "techniques": [
    "py8dis-assisted disassembly",
    "beebasm reassembly",
    "binary comparison",
    "ROM combination"
  ],
  "title": "Stop Press v1.9",
  "tool_kinds": [],
  "types": [
    "ROM disassembly",
    "PALPROM reconstruction"
  ],
  "upstream_name": "Stop Press disassembly",
  "work_kinds": [
    "disassembly",
    "source-reconstruction",
    "patching"
  ]
}
```

### Identity (reviewed)

The README identifies the source as the Watford Electronics release of AMS Stop Press v1.9 for the BBC Micro and names the two original ROM images used by the project.
- https://github.com/ZornsLemma/stop-press-disassembly/blob/79d739d3e3a44d869293db3e12b5db845a7323c5/README.md

### Classification (reviewed)

This is a binary-derived ROM disassembly and source reconstruction with an additional combined PALPROM output, not an original homebrew project.
- https://github.com/ZornsLemma/stop-press-disassembly/blob/79d739d3e3a44d869293db3e12b5db845a7323c5/README.md
- https://github.com/ZornsLemma/stop-press-disassembly/blob/79d739d3e3a44d869293db3e12b5db845a7323c5/go.sh

### Source CPU (reviewed)

The project disassembles BBC Micro ROMs as 6502 code through py8dis and beebasm source generation.
- https://github.com/ZornsLemma/stop-press-disassembly/blob/79d739d3e3a44d869293db3e12b5db845a7323c5/go.sh

### Target CPU (reviewed)

The generated assembly is reassembled into BBC Micro ROM images for the same 6502 target.
- https://github.com/ZornsLemma/stop-press-disassembly/blob/79d739d3e3a44d869293db3e12b5db845a7323c5/go.sh

### Build (reviewed)

The build script generates assembly from the disassembly drivers, assembles both original ROM outputs with beebasm, compares each against its original with cmp, and builds the combined PALPROM image. Limitations: No execution test or minimum hardware claim was found in the reviewed files.
- https://github.com/ZornsLemma/stop-press-disassembly/blob/79d739d3e3a44d869293db3e12b5db845a7323c5/go.sh

### Runtime profiles (no-evidence-found)

The README and build script identify BBC Micro ROM outputs but do not state a verified minimum machine, RAM, ROM or sideways-ROM configuration; none was inferred.
- https://github.com/ZornsLemma/stop-press-disassembly/blob/79d739d3e3a44d869293db3e12b5db845a7323c5/README.md
- https://github.com/ZornsLemma/stop-press-disassembly/blob/79d739d3e3a44d869293db3e12b5db845a7323c5/go.sh

### AI (no-evidence-found)

The reviewed README, build script and latest commit metadata contain no explicit development-AI disclosure; this does not establish non-use.
- https://github.com/ZornsLemma/stop-press-disassembly/blob/79d739d3e3a44d869293db3e12b5db845a7323c5/README.md
- https://github.com/ZornsLemma/stop-press-disassembly/commit/79d739d3e3a44d869293db3e12b5db845a7323c5

### Relationships (reviewed)

The README attributes the original application to the Watford Electronics release of AMS Stop Press and explains that this project combines its two ROMs into one Computer Concepts-style PALPROM image.
- https://github.com/ZornsLemma/stop-press-disassembly/blob/79d739d3e3a44d869293db3e12b5db845a7323c5/README.md

## Grime — BBC Micro game recovery and enhanced source version

Project ID: grime6502-bbc-restoration · Overall audit: reviewed

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
  "display_title": "Grime — BBC Micro game recovery and enhanced source version",
  "id": "grime6502-bbc-restoration",
  "last_activity": "2026-03-19",
  "last_checked": "2026-10-29",
  "re_started": null,
  "reconstructed_languages": [
    "6502 assembly",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/TobyLobster/Grime6502",
  "runtime_profiles": [],
  "source_cpu": [
    "6502"
  ],
  "source_language": [
    "6502 machine code",
    "surviving 6502 assembly"
  ],
  "source_platforms": [
    "BBC Micro"
  ],
  "status": "Recovered labelled source builds a BBC Micro SSD with documented controls, fixes and optimizations",
  "subjects": [
    "Grime"
  ],
  "tags": [
    "BBC Micro",
    "Grime",
    "beebasm"
  ],
  "target_cpu": [
    "6502"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "BBC Micro"
  ],
  "techniques": [
    "binary disassembly",
    "surviving-source recovery",
    "video-assisted labelling",
    "original-platform patching"
  ],
  "title": "Grime",
  "tool_kinds": [],
  "types": [
    "game source recovery",
    "enhanced original-platform version"
  ],
  "upstream_name": "Grime6502",
  "work_kinds": [
    "disassembly",
    "source-reconstruction",
    "patching"
  ]
}
```

### Identity (reviewed)

The author README identifies Grime as a BBC Micro game by Mark Bell and describes this repository as its recovery plus improved version.
- https://github.com/TobyLobster/Grime6502/blob/0d63a56a2d7569e29bedff6f13c2ea758dfc33b9/README.md

### Classification (reviewed)

This is a source recovery reconstructed from the original binary and surviving source files, followed by explicitly documented controls, fixes and optimizations on the original platform.
- https://github.com/TobyLobster/Grime6502/blob/0d63a56a2d7569e29bedff6f13c2ea758dfc33b9/README.md

### Source CPU (reviewed)

The README describes disassembly of the BBC Micro binary into beebasm-compatible 6502 assembly source.
- https://github.com/TobyLobster/Grime6502/blob/0d63a56a2d7569e29bedff6f13c2ea758dfc33b9/README.md

### Target CPU (reviewed)

The recovered and enhanced assembly is built back into a BBC Micro SSD, retaining the 6502 target.
- https://github.com/TobyLobster/Grime6502/blob/0d63a56a2d7569e29bedff6f13c2ea758dfc33b9/README.md

### Build (reviewed)

The README requires beebasm and Python 3 and gives `python3 build.py`, which creates an SSD image. Limitations: No independent execution, gameplay or byte comparison was performed; the explicit improvements mean the original binary should not be assumed to match.
- https://github.com/TobyLobster/Grime6502/blob/0d63a56a2d7569e29bedff6f13c2ea758dfc33b9/README.md

### Runtime profiles (no-evidence-found)

The reviewed README names the BBC Micro and SSD output but states no minimum model, RAM or ROM requirements; none were inferred.
- https://github.com/TobyLobster/Grime6502/blob/0d63a56a2d7569e29bedff6f13c2ea758dfc33b9/README.md

### AI (no-evidence-found)

The reviewed README and latest commit metadata contain no explicit development-AI disclosure; this does not establish non-use.
- https://github.com/TobyLobster/Grime6502/blob/0d63a56a2d7569e29bedff6f13c2ea758dfc33b9/README.md
- https://github.com/TobyLobster/Grime6502/commit/0d63a56a2d7569e29bedff6f13c2ea758dfc33b9

### Relationships (reviewed)

The README distinguishes the original Mark Bell game, its surviving source fragments, the recovered labelled disassembly and Toby Lobster's gameplay-preserving enhanced version.
- https://github.com/TobyLobster/Grime6502/blob/0d63a56a2d7569e29bedff6f13c2ea758dfc33b9/README.md

## BBC Micro 6502/65C02 timing tests for emulator validation

Project ID: beeb-6502-timing-tests · Overall audit: reviewed

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
  "display_title": "BBC Micro 6502/65C02 timing tests for emulator validation",
  "id": "beeb-6502-timing-tests",
  "last_activity": "2026-03-22",
  "last_checked": "2026-10-29",
  "re_started": null,
  "reconstructed_languages": [
    "6502 assembly",
    "Python"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/tom-seddon/beeb_6502_timing_tests",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Released SSD tests run on BBC Micro and BBC Master hardware to expose specific 6502/65C02 timing errors",
  "subjects": [],
  "tags": [
    "BBC Micro",
    "BBC Master",
    "6502",
    "65C02"
  ],
  "target_cpu": [
    "6502",
    "65C02"
  ],
  "target_kinds": [],
  "target_platforms": [
    "BBC Micro",
    "BBC Master"
  ],
  "techniques": [
    "cycle-timing edge-case tests",
    "real-hardware validation",
    "emulator conformance testing"
  ],
  "title": "BBC Micro 6502 timing tests",
  "tool_kinds": [
    "cycle-analysis",
    "automation"
  ],
  "types": [
    "native CPU timing test suite",
    "emulator conformance tests"
  ],
  "upstream_name": "beeb_6502_timing_tests",
  "work_kinds": []
}
```

### Identity (reviewed)

The primary README identifies the repository as tests for specific 6502 and 65C02 timing cases on BBC Micro and Master systems.
- https://github.com/tom-seddon/beeb_6502_timing_tests/blob/f3dec4fddd1acce008949551ffbf2c4fea181989/README.md

### Classification (reviewed)

This is original native diagnostic software and emulator-validation tooling, not a reverse-engineered subject or an RE-derived port.
- https://github.com/tom-seddon/beeb_6502_timing_tests/blob/f3dec4fddd1acce008949551ffbf2c4fea181989/README.md

### Source CPU (not-applicable)

No original binary is being analysed or reconstructed; the project authors native timing tests, so an original source CPU does not sensibly apply.
- https://github.com/tom-seddon/beeb_6502_timing_tests/blob/f3dec4fddd1acce008949551ffbf2c4fea181989/README.md

### Target CPU (reviewed)

The README explicitly says the tests exercise 6502 and 65C02 timing cases and can run on BBC B and Master 128 hardware.
- https://github.com/tom-seddon/beeb_6502_timing_tests/blob/f3dec4fddd1acce008949551ffbf2c4fea181989/README.md

### Build (reviewed)

The project publishes an SSD release with documented boot instructions and success/failure output for real BBC hardware. Limitations: The reviewed README did not establish a source-build command, so compilability remains unknown.
- https://github.com/tom-seddon/beeb_6502_timing_tests/blob/f3dec4fddd1acce008949551ffbf2c4fea181989/README.md

### Runtime profiles (no-evidence-found)

The author reports tests on BBC B and Master 128 and warns about the 1 MHz bus, but does not claim either machine as a minimum hardware profile; no minimum CPU, RAM or ROM was inferred.
- https://github.com/tom-seddon/beeb_6502_timing_tests/blob/f3dec4fddd1acce008949551ffbf2c4fea181989/README.md

### AI (no-evidence-found)

The reviewed README and latest commit metadata contain no explicit development-AI disclosure; this does not establish non-use.
- https://github.com/tom-seddon/beeb_6502_timing_tests/blob/f3dec4fddd1acce008949551ffbf2c4fea181989/README.md
- https://github.com/tom-seddon/beeb_6502_timing_tests/commit/f3dec4fddd1acce008949551ffbf2c4fea181989

### Relationships (reviewed)

The README explicitly positions these tests alongside dp111/6502Timing and as a way to validate emulator CPU timing; those are dependencies/context rather than reconstructed subjects in this record.
- https://github.com/tom-seddon/beeb_6502_timing_tests/blob/f3dec4fddd1acce008949551ffbf2c4fea181989/README.md

## lib6502-jit — LLVM JIT implementation of the 6502 emulator API

Project ID: lib6502-jit · Overall audit: reviewed

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
  "display_title": "lib6502-jit — LLVM JIT implementation of the 6502 emulator API",
  "id": "lib6502-jit",
  "last_activity": "2014-06-25",
  "last_checked": "2026-10-29",
  "re_started": null,
  "reconstructed_languages": [
    "C++",
    "LLVM IR"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/ZornsLemma/lib6502-jit",
  "runtime_profiles": [],
  "source_cpu": [
    "6502"
  ],
  "source_language": [
    "6502 machine code"
  ],
  "source_platforms": [],
  "status": "Mostly compatible lib6502 API implementation that JIT-compiles 6502 code with LLVM",
  "subjects": [],
  "tags": [
    "6502",
    "LLVM",
    "lib6502",
    "JIT"
  ],
  "target_cpu": [],
  "target_kinds": [],
  "target_platforms": [],
  "techniques": [
    "LLVM just-in-time compilation",
    "6502 dynamic binary translation",
    "lib6502 API compatibility"
  ],
  "title": "lib6502-jit",
  "tool_kinds": [
    "emulator",
    "binary-analysis"
  ],
  "types": [
    "6502 JIT emulator library",
    "dynamic binary translator"
  ],
  "upstream_name": "lib6502-jit",
  "work_kinds": [
    "translation"
  ]
}
```

### Identity (reviewed)

The repository README identifies lib6502-jit as a mostly compatible implementation of Ian Piumarta's lib6502 API.
- https://github.com/ZornsLemma/lib6502-jit/blob/5d5ddba7f10596fc574fb0639012d720b9d66c62/README.md
- https://github.com/ZornsLemma/lib6502-jit/blob/5d5ddba7f10596fc574fb0639012d720b9d66c62/README.lib6502

### Classification (reviewed)

This is modern emulator/dynamic-translation tooling: it uses LLVM JIT compilation to translate 6502 machine code to host code while exposing the lib6502 API.
- https://github.com/ZornsLemma/lib6502-jit/blob/5d5ddba7f10596fc574fb0639012d720b9d66c62/README.md

### Source CPU (reviewed)

The README explicitly states that the input machine code and emulated API are for the 6502.
- https://github.com/ZornsLemma/lib6502-jit/blob/5d5ddba7f10596fc574fb0639012d720b9d66c62/README.md

### Target CPU (no-evidence-found)

The reviewed documentation says LLVM emits host code but does not restrict or enumerate host output architectures; none was inferred from LLVM or the implementation language.
- https://github.com/ZornsLemma/lib6502-jit/blob/5d5ddba7f10596fc574fb0639012d720b9d66c62/README.md

### Build (no-evidence-found)

The reviewed project overview and imported lib6502 documentation establish implementation scope and compatibility limits but not a verified current build or runnable artifact.
- https://github.com/ZornsLemma/lib6502-jit/blob/5d5ddba7f10596fc574fb0639012d720b9d66c62/README.md
- https://github.com/ZornsLemma/lib6502-jit/blob/5d5ddba7f10596fc574fb0639012d720b9d66c62/README.lib6502

### Runtime profiles (not-applicable)

This is a host library rather than a runnable legacy-hardware output, so the tracker's minimum retro-hardware runtime profile does not sensibly apply.
- https://github.com/ZornsLemma/lib6502-jit/blob/5d5ddba7f10596fc574fb0639012d720b9d66c62/README.md

### AI (no-evidence-found)

The reviewed README and first public release commit metadata contain no explicit development-AI disclosure; this does not establish non-use.
- https://github.com/ZornsLemma/lib6502-jit/blob/5d5ddba7f10596fc574fb0639012d720b9d66c62/README.md
- https://github.com/ZornsLemma/lib6502-jit/commit/5d5ddba7f10596fc574fb0639012d720b9d66c62

### Relationships (reviewed)

The repository explicitly implements Ian Piumarta's lib6502 API and preserves the upstream lib6502 README while documenting deliberate compatibility differences in the JIT implementation.
- https://github.com/ZornsLemma/lib6502-jit/blob/5d5ddba7f10596fc574fb0639012d720b9d66c62/README.md
- https://github.com/ZornsLemma/lib6502-jit/blob/5d5ddba7f10596fc574fb0639012d720b9d66c62/README.lib6502

## VS Code OSDK — Oric development and source-level debugging environment

Project ID: vscode-osdk-oric · Overall audit: reviewed

### Typed catalogue values

```json
{
  "ai": {
    "evidence": [
      "Commit b9edb61078d7759d60bb5244194c5e8a1bd05909 has an explicit Claude Opus 5 (1M context) co-author trailer."
    ],
    "tools": [
      "Claude Opus 5"
    ],
    "usage": true
  },
  "build": {
    "byte_exact": null,
    "compilable": null,
    "playable": null,
    "runnable": true
  },
  "display_title": "VS Code OSDK — Oric development and source-level debugging environment",
  "id": "vscode-osdk-oric",
  "last_activity": "2026-07-28",
  "last_checked": "2026-10-29",
  "re_started": null,
  "reconstructed_languages": [
    "JavaScript"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/Oric-Software-Development-Kit/vscode-osdk",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Released VS Code extension for OSDK editing, building, testing and Oricutron-backed C/assembly debugging",
  "subjects": [],
  "tags": [
    "Oric",
    "OSDK",
    "Oricutron",
    "VS Code"
  ],
  "target_cpu": [
    "6502"
  ],
  "target_kinds": [],
  "target_platforms": [
    "Oric"
  ],
  "techniques": [
    "Oricutron GDB-stub integration",
    "source-map debugging",
    "reverse trace",
    "screen and memory inspection",
    "headless test automation"
  ],
  "title": "VS Code OSDK",
  "tool_kinds": [
    "ide",
    "debugger",
    "graphics-debugger",
    "profiler",
    "automation",
    "development-environment"
  ],
  "types": [
    "VS Code extension",
    "Oric source-level debugger"
  ],
  "upstream_name": "VS Code OSDK",
  "work_kinds": []
}
```

### Identity (reviewed)

The primary README identifies VS Code OSDK as a Visual Studio Code extension for Oric development and debugging with OSDK and Oricutron.
- https://github.com/Oric-Software-Development-Kit/vscode-osdk/blob/b9edb61078d7759d60bb5244194c5e8a1bd05909/README.md

### Classification (reviewed)

This is original development tooling, not a reverse-engineered program: it provides Oric C/assembly language support, source-level debugging, reverse trace, graphics/memory inspection and automated tests.
- https://github.com/Oric-Software-Development-Kit/vscode-osdk/blob/b9edb61078d7759d60bb5244194c5e8a1bd05909/README.md

### Source CPU (not-applicable)

The extension does not analyse a particular original binary, so an original source CPU does not sensibly apply.
- https://github.com/Oric-Software-Development-Kit/vscode-osdk/blob/b9edb61078d7759d60bb5244194c5e8a1bd05909/README.md

### Target CPU (reviewed)

The README explicitly documents 6502/XA references and debugging of Oric assembly/C output through OSDK and Oricutron, establishing the 6502 development target.
- https://github.com/Oric-Software-Development-Kit/vscode-osdk/blob/b9edb61078d7759d60bb5244194c5e8a1bd05909/README.md

### Build (reviewed)

The README documents the released VS Code extension, its requirements and operating features; version 1.0.0 was published as the first Marketplace release. Limitations: No independent package build was run, so compilability remains unknown.
- https://github.com/Oric-Software-Development-Kit/vscode-osdk/blob/b9edb61078d7759d60bb5244194c5e8a1bd05909/README.md
- https://github.com/Oric-Software-Development-Kit/vscode-osdk/commit/b9edb61078d7759d60bb5244194c5e8a1bd05909

### Runtime profiles (not-applicable)

The documented requirements are for the modern VS Code/OSDK/Oricutron host environment, not a minimum runnable retro-hardware build variant, so no runtime profile was added.
- https://github.com/Oric-Software-Development-Kit/vscode-osdk/blob/b9edb61078d7759d60bb5244194c5e8a1bd05909/README.md

### AI (reviewed)

The first Marketplace release commit explicitly credits Claude Opus 5 (1M context) in a co-author trailer. The README's MCP interaction feature is a capability and is not used by itself as authorship evidence.
- https://github.com/Oric-Software-Development-Kit/vscode-osdk/commit/b9edb61078d7759d60bb5244194c5e8a1bd05909
- https://github.com/Oric-Software-Development-Kit/vscode-osdk/blob/b9edb61078d7759d60bb5244194c5e8a1bd05909/README.md

### Relationships (reviewed)

The extension is a distinct front end built around OSDK 2.0+ and the included Oricutron GDB stub; those dependencies remain separate projects rather than subjects reconstructed here.
- https://github.com/Oric-Software-Development-Kit/vscode-osdk/blob/b9edb61078d7759d60bb5244194c5e8a1bd05909/README.md

## EdAsm — ProDOS Assembler Tools Release 1.1 disassembled source

Project ID: edasm-prodos-assembler-tools-disassembly · Overall audit: partial

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
  "display_title": "EdAsm — ProDOS Assembler Tools Release 1.1 disassembled source",
  "id": "edasm-prodos-assembler-tools-disassembly",
  "last_activity": "2022-05-21",
  "last_checked": "2026-10-29",
  "re_started": null,
  "reconstructed_languages": [
    "6502/65C02 assembly"
  ],
  "record_class": "hybrid",
  "repo": "https://github.com/markpmlim/EdAsm",
  "runtime_profiles": [],
  "source_cpu": [
    "6502",
    "65C02"
  ],
  "source_language": [
    "6502/65C02 machine code"
  ],
  "source_platforms": [
    "Apple II"
  ],
  "status": "Disassembled sources for five ProDOS Assembler Tools programs are published with assembly prerequisites and byte-comparison intent",
  "subjects": [
    "ProDOS Assembler Tools Release 1.1",
    "EDASM"
  ],
  "tags": [
    "Apple II",
    "ProDOS 8",
    "EDASM",
    "assembler"
  ],
  "target_cpu": [
    "6502",
    "65C02"
  ],
  "target_kinds": [
    "development-tool"
  ],
  "target_platforms": [
    "Apple II"
  ],
  "techniques": [
    "Flaming Bird Disassembler",
    "manual source reconstruction",
    "byte-comparison preparation",
    "SWEET16 analysis"
  ],
  "title": "EdAsm",
  "tool_kinds": [
    "assembler-toolchain",
    "language-tooling"
  ],
  "types": [
    "historical assembler disassembly",
    "source reconstruction"
  ],
  "upstream_name": "EdAsm",
  "work_kinds": [
    "disassembly",
    "source-reconstruction"
  ]
}
```

### Identity (reviewed)

The repository README identifies the work as disassembled source for five programs in the ProDOS Assembler Tools Release 1.1 package, including EDASM.SYSTEM and its command-line tools.
- https://github.com/markpmlim/EdAsm/blob/05a19d8693a3b511ebdf97a8e8adb3eef886e698/README.MD

### Classification (reviewed)

This is binary-derived source reconstruction of a historical Apple development tool, so it is both a reconstructed subject and preserved development tooling; it is not labelled as original homebrew.
- https://github.com/markpmlim/EdAsm/blob/05a19d8693a3b511ebdf97a8e8adb3eef886e698/README.MD
- https://github.com/markpmlim/EdAsm

### Source CPU (reviewed)

The README says the disassembly requires 6502/65C02 knowledge and SWEET16 understanding, and the published source uses those instruction families for the original ProDOS tools.
- https://github.com/markpmlim/EdAsm/blob/05a19d8693a3b511ebdf97a8e8adb3eef886e698/README.MD
- https://github.com/markpmlim/EdAsm

### Target CPU (reviewed)

The reconstructed assembly is intended to reassemble the same ProDOS 8 programs using 6502/65C02 source, establishing the same output CPU families.
- https://github.com/markpmlim/EdAsm/blob/05a19d8693a3b511ebdf97a8e8adb3eef886e698/README.MD

### Build (needs-research)

The README explains that a copy of ProDOS Assembler Tools Release 1.1 is required to assemble the five programs and that retained DS data permits comparison with the originals. Limitations: The repository describes the source as for viewing and does not report a verified successful or byte-identical rebuild. Next check: Assemble the five documented source files with the stated Release 1.1 environment and compare each output with the corresponding original program.
- https://github.com/markpmlim/EdAsm/blob/05a19d8693a3b511ebdf97a8e8adb3eef886e698/README.MD

### Runtime profiles (no-evidence-found)

The reviewed material identifies ProDOS 8 and the original Apple II package but states no minimum model, CPU, RAM or ROM requirements; none were inferred.
- https://github.com/markpmlim/EdAsm/blob/05a19d8693a3b511ebdf97a8e8adb3eef886e698/README.MD

### AI (no-evidence-found)

The reviewed README, source headers and latest commit metadata contain no explicit development-AI disclosure; this does not establish non-use.
- https://github.com/markpmlim/EdAsm/blob/05a19d8693a3b511ebdf97a8e8adb3eef886e698/README.MD
- https://github.com/markpmlim/EdAsm/commit/05a19d8693a3b511ebdf97a8e8adb3eef886e698

### Relationships (reviewed)

The README ties this repository specifically to ProDOS Assembler Tools Release 1.1 and identifies the original package as both the source artifact and required assembly environment.
- https://github.com/markpmlim/EdAsm/blob/05a19d8693a3b511ebdf97a8e8adb3eef886e698/README.MD

## Sources

```json
[
  {
    "first_indexed": "2026-10-29",
    "id": "github-zornslemma-stop-press-disassembly",
    "kind": "github-repository",
    "last_reviewed": "2026-10-29",
    "reason": "Primary repository for the BBC Micro Stop Press v1.9 ROM disassembly, byte-comparison rebuild and combined PALPROM output.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/ZornsLemma/stop-press-disassembly"
  },
  {
    "first_indexed": "2026-10-29",
    "id": "github-tobylobster-grime6502",
    "kind": "github-repository",
    "last_reviewed": "2026-10-29",
    "reason": "Primary repository for the recovered and enhanced BBC Micro Grime source.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/TobyLobster/Grime6502"
  },
  {
    "first_indexed": "2026-10-29",
    "id": "github-tom-seddon-beeb-6502-timing-tests",
    "kind": "github-repository",
    "last_reviewed": "2026-10-29",
    "reason": "Primary repository for native BBC Micro and BBC Master 6502/65C02 timing tests used to validate emulator CPU timing.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/tom-seddon/beeb_6502_timing_tests"
  },
  {
    "first_indexed": "2026-10-29",
    "id": "github-zornslemma-lib6502-jit",
    "kind": "github-repository",
    "last_reviewed": "2026-10-29",
    "reason": "Primary repository for the LLVM JIT implementation of the lib6502 API.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/ZornsLemma/lib6502-jit"
  },
  {
    "first_indexed": "2026-10-29",
    "id": "github-oric-software-development-kit-vscode-osdk",
    "kind": "github-repository",
    "last_reviewed": "2026-10-29",
    "reason": "Primary repository for the VS Code OSDK development and Oricutron source-level debugging extension.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/Oric-Software-Development-Kit/vscode-osdk"
  },
  {
    "first_indexed": "2026-10-29",
    "id": "github-markpmlim-edasm",
    "kind": "github-repository",
    "last_reviewed": "2026-10-29",
    "reason": "Primary repository for the disassembled source of the ProDOS Assembler Tools Release 1.1 programs.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/markpmlim/EdAsm"
  },
  {
    "first_indexed": "2026-10-29",
    "id": "github-ksherlock-gno-sources",
    "kind": "github-repository",
    "last_reviewed": "2026-10-29",
    "reason": "Apple IIgs GNO/ME source collection whose canonical lineage, build scope and relationship to other GNO repositories remain unresolved.",
    "review_state": "partial",
    "source": "https://github.com/ksherlock/gno-sources"
  },
  {
    "first_indexed": "2026-10-29",
    "id": "github-tobylobster-rom-library",
    "kind": "github-repository",
    "last_reviewed": "2026-10-29",
    "reason": "BBC Micro ROM library with recent component-matching activity but no root README establishing independent analysis-tool scope.",
    "review_state": "partial",
    "source": "https://github.com/TobyLobster/rom_library"
  }
]
```

## Source updates

```json
[
  {
    "id": "github-zornslemma",
    "last_reviewed": "2026-10-29",
    "review_state": "partial"
  },
  {
    "id": "github-tobylobster",
    "last_reviewed": "2026-10-29",
    "review_state": "partial"
  },
  {
    "id": "github-tom-seddon",
    "last_reviewed": "2026-10-29",
    "review_state": "partial"
  },
  {
    "id": "github-seghaxx-nitecrwl",
    "last_reviewed": "2026-10-29",
    "review_state": "partial"
  }
]
```

## Tasks

```json
[
  {
    "created_at": "2026-10-29",
    "description": "Resolve ksherlock/gno-sources lineage and build scope against the current GNO/ME repositories before promotion.",
    "id": "task-gno-sources-lineage-and-build",
    "last_reviewed": "2026-10-29",
    "notes": "Inspect repository history, period release documentation and links to GnoConsortium/gno and tubesnob-apple/gno; establish whether this is an independent maintained source restoration, a predecessor, or a source import. Verify any Apple IIgs build claims from primary files rather than the directory names.",
    "priority": "normal",
    "source_ids": [
      "github-ksherlock-gno-sources"
    ],
    "state": "deferred"
  },
  {
    "created_at": "2026-10-29",
    "description": "Establish whether TobyLobster/rom_library publishes a distinct ROM-component matching or extraction tool.",
    "id": "task-rom-library-analysis-tool-scope",
    "last_reviewed": "2026-10-29",
    "notes": "The current tree has no root README; recent commits mention extracted ROMs and matched component parts. Inspect the generator/index implementation and any project site documentation before deciding whether this is a qualifying analysis tool or only a curated archive.",
    "priority": "normal",
    "source_ids": [
      "github-tobylobster-rom-library"
    ],
    "state": "deferred"
  }
]
```

## Task updates

```json
[
  {
    "id": "task-seghaxx-nitecrwl-provenance",
    "last_reviewed": "2026-10-29",
    "notes_append": "A current repository-name search, file search and canonical URL recheck did not expose the original Atari ST binary or a binary-to-recovered-C++ correspondence record. Keep the promoted project facts unchanged and defer this provenance question until the author publishes or links the original artifact.",
    "state": "deferred"
  }
]
```

## Decisions

```json
[
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/ZornsLemma/stop-press-disassembly/blob/79d739d3e3a44d869293db3e12b5db845a7323c5/README.md",
      "https://github.com/ZornsLemma/stop-press-disassembly/blob/79d739d3e3a44d869293db3e12b5db845a7323c5/go.sh"
    ],
    "id": "stop-press-disassembly-promoted",
    "project_ids": [
      "stop-press-bbc-disassembly"
    ],
    "reason": "The primary README and build script establish a BBC Micro Stop Press v1.9 ROM disassembly, byte-identical rebuilds of both source ROMs and a combined PALPROM build.",
    "reviewed_at": "2026-10-29",
    "source_ids": [
      "github-zornslemma-stop-press-disassembly"
    ],
    "title": "Stop Press disassembly",
    "url": "https://github.com/ZornsLemma/stop-press-disassembly"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/TobyLobster/Grime6502/blob/0d63a56a2d7569e29bedff6f13c2ea758dfc33b9/README.md"
    ],
    "id": "grime6502-promoted",
    "project_ids": [
      "grime6502-bbc-restoration"
    ],
    "reason": "The author documents recovery of the BBC Micro game from its binary and surviving source, a labelled disassembly, conservative gameplay-preserving fixes and a reproducible SSD build command.",
    "reviewed_at": "2026-10-29",
    "source_ids": [
      "github-tobylobster-grime6502"
    ],
    "title": "Grime6502",
    "url": "https://github.com/TobyLobster/Grime6502"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/tom-seddon/beeb_6502_timing_tests/blob/f3dec4fddd1acce008949551ffbf2c4fea181989/README.md"
    ],
    "id": "beeb-6502-timing-tests-promoted",
    "project_ids": [
      "beeb-6502-timing-tests"
    ],
    "reason": "The README establishes runnable native BBC Micro/Master tests for specific 6502 and 65C02 timing cases, explicitly intended to validate emulator CPU timing accuracy.",
    "reviewed_at": "2026-10-29",
    "source_ids": [
      "github-tom-seddon-beeb-6502-timing-tests"
    ],
    "title": "BBC Micro 6502 timing tests",
    "url": "https://github.com/tom-seddon/beeb_6502_timing_tests"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/ZornsLemma/lib6502-jit/blob/5d5ddba7f10596fc574fb0639012d720b9d66c62/README.md",
      "https://github.com/ZornsLemma/lib6502-jit/blob/5d5ddba7f10596fc574fb0639012d720b9d66c62/README.lib6502"
    ],
    "id": "lib6502-jit-promoted",
    "project_ids": [
      "lib6502-jit"
    ],
    "reason": "The project is a concrete LLVM JIT implementation of the lib6502 API for translating 6502 machine code to host code, with documented compatibility limitations.",
    "reviewed_at": "2026-10-29",
    "source_ids": [
      "github-zornslemma-lib6502-jit"
    ],
    "title": "lib6502-jit",
    "url": "https://github.com/ZornsLemma/lib6502-jit"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/Oric-Software-Development-Kit/vscode-osdk/blob/b9edb61078d7759d60bb5244194c5e8a1bd05909/README.md",
      "https://github.com/Oric-Software-Development-Kit/vscode-osdk/commit/b9edb61078d7759d60bb5244194c5e8a1bd05909"
    ],
    "id": "vscode-osdk-promoted",
    "project_ids": [
      "vscode-osdk-oric"
    ],
    "reason": "The primary README documents a released VS Code environment for Oric C/assembly development, source-level debugging through Oricutron, reverse trace, memory/screen inspection and test automation.",
    "reviewed_at": "2026-10-29",
    "source_ids": [
      "github-oric-software-development-kit-vscode-osdk"
    ],
    "title": "VS Code OSDK",
    "url": "https://github.com/Oric-Software-Development-Kit/vscode-osdk"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/markpmlim/EdAsm/blob/05a19d8693a3b511ebdf97a8e8adb3eef886e698/README.MD",
      "https://github.com/markpmlim/EdAsm"
    ],
    "id": "edasm-prodos-tools-promoted",
    "project_ids": [
      "edasm-prodos-assembler-tools-disassembly"
    ],
    "reason": "The repository identifies its sources as disassemblies of five ProDOS Assembler Tools Release 1.1 programs and documents the original package needed to assemble them and compare outputs.",
    "reviewed_at": "2026-10-29",
    "source_ids": [
      "github-markpmlim-edasm"
    ],
    "title": "EdAsm",
    "url": "https://github.com/markpmlim/EdAsm"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/ksherlock/gno-sources",
      "https://github.com/ksherlock/gno-sources/commit/102264454a6cc6847957ee5965743730f26e6307"
    ],
    "id": "ksherlock-gno-sources-deferred",
    "reason": "The reviewed tree contains a broad Apple IIgs GNO/ME source collection and current commits but no root README. Resolve its canonical lineage and distinct build/release scope against the other GNO repositories before deciding whether it warrants an independent record.",
    "reviewed_at": "2026-10-29",
    "source_ids": [
      "github-ksherlock-gno-sources"
    ],
    "title": "gno-sources",
    "url": "https://github.com/ksherlock/gno-sources"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/TobyLobster/rom_library",
      "https://github.com/TobyLobster/rom_library/commit/904f18b56c9518b87624a9ab3ea7c7cd3dd0aaef"
    ],
    "id": "tobylobster-rom-library-deferred",
    "reason": "The repository has no root README. Recent commits mention extracting ROMs from larger images and matching component parts, but the reviewed tree does not yet establish whether a reusable analysis implementation is published or this is only archive curation.",
    "reviewed_at": "2026-10-29",
    "source_ids": [
      "github-tobylobster-rom-library"
    ],
    "title": "rom_library",
    "url": "https://github.com/TobyLobster/rom_library"
  }
]
```

## Source ids

```json
[
  "github-zornslemma",
  "github-tobylobster",
  "github-tom-seddon",
  "github-seghaxx-nitecrwl"
]
```

## Research event notes

The CPU audit queue reported zero unresolved source/target CPU areas, so this pass did not fabricate CPU work. Four fresh-search focuses were rotated independently of the saved queue. Oric routes: web query `site:github.com Oric Atmos disassembly reassembly reverse engineering homebrew tooling` and GitHub repository query `Oric disassembly reverse engineering development toolkit`. PC-98 routes: web query `site:github.com PC-98 disassembly decompilation reverse engineering source reconstruction` and GitHub repository query `PC-98 decompiler disassembly source reconstruction`; reviewed PC98VNResearch, ReC98, th04 and lime-juice/juice results were already represented. Apple IIgs routes: web query `site:github.com Apple IIgs disassembly reconstruction source port homebrew tooling` and GitHub repository query `Apple IIgs disassembly reassembly development tools`; EdAsm was promoted and gno-sources was deferred. Acorn Archimedes routes: web query `site:github.com Acorn Archimedes disassembly reconstruction homebrew development tooling` and GitHub repository query `Acorn Archimedes disassembly reconstruction development`; the Lander reconstruction and its two web ports were already represented. Queue/profile review additionally promoted Stop Press, Grime6502, BBC 6502 timing tests and lib6502-jit. TobyLobster/rom_library remains deferred because the root has no README and the reviewed tree did not establish whether its ROM-component matching is a published analysis tool or only archive curation. SegHaxx/nitecrwl provenance remains deferred after repository/file searches did not expose the original binary or a binary-to-source correspondence record.
