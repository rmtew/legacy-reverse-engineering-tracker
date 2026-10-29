# Jaguar, ZX Spectrum and retro-video preservation discovery pass

Promoted four primary-source-reviewed retro-development projects and closed two deferred queue reviews

Date: 2026-10-29 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- mortal-kombat-atari-jaguar-fan-demo / Build (reviewed): The build, emulator launch and hardware behavior were not independently tested in this review, so runnable/playable remain unknown.
- mortal-kombat-atari-jaguar-fan-demo / Runtime profiles (no-evidence-found): The reviewed documentation names Atari Jaguar and a Virtual Jaguar development launch but does not state a minimum Jaguar revision, RAM, ROM, cartridge device or other runnable hardware requirement; none was inferred.
- mortal-kombat-atari-jaguar-fan-demo / AI (no-evidence-found): The reviewed readme, assembly, build script and complete three-commit history contain no explicit development-AI attribution; this does not establish non-use.
- horace-goes-skiing-skoolkit-disassembly / Build (reviewed): No game reassembly, binary comparison or generated HTML run was performed, and the repository does not document a reconstructed game executable.
- horace-goes-skiing-skoolkit-disassembly / AI (no-evidence-found): The complete small tree, nested metadata and four commit messages contain no explicit development-AI attribution; this does not establish non-use.
- particle-man-atari-jaguar / Build (reviewed): No local compilation or hardware test was performed. Runnable/playable reflect upstream real-hardware reports, not independent verification of the current revision.
- particle-man-atari-jaguar / Runtime profiles (no-evidence-found): The README documents real-Jaguar testing and a current 128-byte GameDrive save configuration, but it does not state a minimum Jaguar revision, RAM floor, ROM requirement or generally supported cartridge device. These test details were not converted into a minimum profile.
- retrocastx-rgb-capture-stack / Target CPU (no-evidence-found): The client is documented for Mac, Windows and Linux and the capture device uses ECP5 FPGA logic, but the reviewed material does not constrain the host program to a specific CPU architecture. No host ISA was inferred from Rust, Python or operating-system names.
- retrocastx-rgb-capture-stack / Build (reviewed): The same status list says physical gateware, board manufacture and real X68000/PC-98 capture remain unfinished. No local test or hardware operation was performed.

## Mortal Kombat — Atari Jaguar character-select fan conversion

Project ID: mortal-kombat-atari-jaguar-fan-demo · Overall audit: reviewed

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
  "display_title": "Mortal Kombat — Atari Jaguar character-select fan conversion",
  "id": "mortal-kombat-atari-jaguar-fan-demo",
  "last_activity": "2023-02-24",
  "last_checked": "2026-10-29",
  "re_started": null,
  "reconstructed_languages": [
    "Motorola 68000 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/trufungames/Mortal-Kombat-Atari-Jaguar",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [
    "Arcade"
  ],
  "status": "Jaguar character-select proof of concept with source and documented RAPTOR build path; independent build/run unverified",
  "subjects": [
    "Mortal Kombat"
  ],
  "tags": [
    "Atari Jaguar",
    "Mortal Kombat",
    "RAPTOR",
    "fan conversion",
    "original homebrew"
  ],
  "target_cpu": [
    "Motorola 68000"
  ],
  "target_kinds": [
    "demo"
  ],
  "target_platforms": [
    "Atari Jaguar"
  ],
  "techniques": [
    "RAPTOR sprite animation",
    "sampled-audio playback",
    "Jaguar controller input"
  ],
  "title": "Mortal Kombat Atari Jaguar",
  "tool_kinds": [],
  "types": [
    "original fan conversion",
    "character-select proof of concept"
  ],
  "upstream_name": "Mortal-Kombat-Atari-Jaguar",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Chris Bryant's readme identifies the repository as a Mortal Kombat character-select proof of concept for Atari Jaguar and the assembly header names the same example and author.
- https://github.com/trufungames/Mortal-Kombat-Atari-Jaguar/blob/58d3f11016ad147c233fb81a5a52acdb5dcf5f2f/readme.txt
- https://github.com/trufungames/Mortal-Kombat-Atari-Jaguar/blob/58d3f11016ad147c233fb81a5a52acdb5dcf5f2f/_RAPAPP.S

### Classification (reviewed)

This is an original fan conversion/demo that reuses credited arcade graphics, music and sound effects to implement the selection screen. The project does not claim disassembly, decompilation or recovered original program code, so it is not labelled RE-derived.
- https://github.com/trufungames/Mortal-Kombat-Atari-Jaguar/blob/58d3f11016ad147c233fb81a5a52acdb5dcf5f2f/readme.txt
- https://github.com/trufungames/Mortal-Kombat-Atari-Jaguar/blob/58d3f11016ad147c233fb81a5a52acdb5dcf5f2f/_RAPAPP.S

### Source CPU (not-applicable)

The project imports original arcade audiovisual assets but does not analyse or translate an original executable, so assigning the arcade program's CPU as a source architecture would be misleading.
- https://github.com/trufungames/Mortal-Kombat-Atari-Jaguar/blob/58d3f11016ad147c233fb81a5a52acdb5dcf5f2f/readme.txt

### Target CPU (reviewed)

The application source is Motorola 68000 assembly using data/address registers, Jaguar hardware includes and RAPTOR calls, and the build invokes RMAC/RLN for the native Jaguar executable.
- https://github.com/trufungames/Mortal-Kombat-Atari-Jaguar/blob/58d3f11016ad147c233fb81a5a52acdb5dcf5f2f/_RAPAPP.S
- https://github.com/trufungames/Mortal-Kombat-Atari-Jaguar/blob/58d3f11016ad147c233fb81a5a52acdb5dcf5f2f/BUILD.bat

### Build (reviewed)

The readme directs users to copy the project into RAPTOR's examples directory and execute BUILD.bat; that script assembles, links an ABS image and launches Virtual Jaguar. Limitations: The build, emulator launch and hardware behavior were not independently tested in this review, so runnable/playable remain unknown.
- https://github.com/trufungames/Mortal-Kombat-Atari-Jaguar/blob/58d3f11016ad147c233fb81a5a52acdb5dcf5f2f/readme.txt
- https://github.com/trufungames/Mortal-Kombat-Atari-Jaguar/blob/58d3f11016ad147c233fb81a5a52acdb5dcf5f2f/BUILD.bat

### Runtime profiles (no-evidence-found)

The reviewed documentation names Atari Jaguar and a Virtual Jaguar development launch but does not state a minimum Jaguar revision, RAM, ROM, cartridge device or other runnable hardware requirement; none was inferred.
- https://github.com/trufungames/Mortal-Kombat-Atari-Jaguar/blob/58d3f11016ad147c233fb81a5a52acdb5dcf5f2f/readme.txt
- https://github.com/trufungames/Mortal-Kombat-Atari-Jaguar/blob/58d3f11016ad147c233fb81a5a52acdb5dcf5f2f/BUILD.bat

### AI (no-evidence-found)

The reviewed readme, assembly, build script and complete three-commit history contain no explicit development-AI attribution; this does not establish non-use.
- https://github.com/trufungames/Mortal-Kombat-Atari-Jaguar/blob/58d3f11016ad147c233fb81a5a52acdb5dcf5f2f/readme.txt
- https://github.com/trufungames/Mortal-Kombat-Atari-Jaguar/commits/main

### Relationships (reviewed)

The readme credits RAPTOR as the development API and separately credits the Mortal Kombat sprite, module-music and sound-conversion sources. Those assets and dependencies are not claimed as original code recovered by this project.
- https://github.com/trufungames/Mortal-Kombat-Atari-Jaguar/blob/58d3f11016ad147c233fb81a5a52acdb5dcf5f2f/readme.txt

## Horace Goes Skiing — annotated ZX Spectrum SkoolKit disassembly

Project ID: horace-goes-skiing-skoolkit-disassembly · Overall audit: partial

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
  "display_title": "Horace Goes Skiing — annotated ZX Spectrum SkoolKit disassembly",
  "id": "horace-goes-skiing-skoolkit-disassembly",
  "last_activity": "2024-12-29",
  "last_checked": "2026-10-29",
  "re_started": null,
  "reconstructed_languages": [
    "SkoolKit skool format",
    "Python",
    "Shell"
  ],
  "record_class": "subject",
  "repo": "https://github.com/Ritchie333/skiing",
  "runtime_profiles": [],
  "source_cpu": [
    "Z80"
  ],
  "source_language": [
    "Z80 machine code"
  ],
  "source_platforms": [
    "ZX Spectrum"
  ],
  "status": "Annotated SkoolKit disassembly and generated HTML analysis; no rebuilt game binary established",
  "subjects": [
    "Horace Goes Skiing"
  ],
  "tags": [
    "ZX Spectrum",
    "Horace Goes Skiing",
    "SkoolKit",
    "Z80"
  ],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [],
  "techniques": [
    "SkoolKit control-file annotation",
    "memory-map documentation",
    "graphics extraction"
  ],
  "title": "Horace Goes Skiing",
  "tool_kinds": [],
  "types": [
    "annotated game disassembly",
    "interactive HTML analysis"
  ],
  "upstream_name": "skiing",
  "work_kinds": [
    "disassembly",
    "binary-analysis"
  ]
}
```

### Identity (reviewed)

Repository metadata says it is a disassembly of Horace Goes Skiing, while skiing.ref identifies the game and credits William Tang/Beam Software for the 1982 code and Ritchie Swann for the 2024 disassembly.
- https://github.com/Ritchie333/skiing
- https://github.com/Ritchie333/skiing/blob/166945789eacfcd640aaea9c16501cff9338d70a/src/skiing.ref

### Classification (reviewed)

The repository contains a Z80 snapshot, annotated SkoolKit control/skool material, graphics metadata and a custom HTML writer. It is an analysis/disassembly project, not a source-faithful rebuild or modern game port.
- https://github.com/Ritchie333/skiing/tree/166945789eacfcd640aaea9c16501cff9338d70a/src
- https://github.com/Ritchie333/skiing/blob/166945789eacfcd640aaea9c16501cff9338d70a/build.sh

### Source CPU (reviewed)

The source artifact is a .z80 snapshot and the skool/control files decode its address space and Z80 instruction/data layout for the ZX Spectrum game.
- https://github.com/Ritchie333/skiing/blob/166945789eacfcd640aaea9c16501cff9338d70a/src/skiing.z80
- https://github.com/Ritchie333/skiing/blob/166945789eacfcd640aaea9c16501cff9338d70a/src/skiing.skool
- https://github.com/Ritchie333/skiing/blob/166945789eacfcd640aaea9c16501cff9338d70a/src/skiing.ctl

### Target CPU (not-applicable)

The documented output is SkoolKit-generated HTML analysis, not a rebuilt or ported executable, so no target output CPU applies.
- https://github.com/Ritchie333/skiing/blob/166945789eacfcd640aaea9c16501cff9338d70a/build.sh

### Build (reviewed)

build.sh invokes skool2html.py with the custom SkiingHtmlWriter to generate the analysis site from skiing.skool. Limitations: No game reassembly, binary comparison or generated HTML run was performed, and the repository does not document a reconstructed game executable.
- https://github.com/Ritchie333/skiing/blob/166945789eacfcd640aaea9c16501cff9338d70a/build.sh
- https://github.com/Ritchie333/skiing/blob/166945789eacfcd640aaea9c16501cff9338d70a/src/skiing.py

### Runtime profiles (not-applicable)

The reviewed project publishes analysis source and an HTML-generation command rather than a runnable legacy-hardware build, so a minimum retro runtime profile does not sensibly apply.
- https://github.com/Ritchie333/skiing/blob/166945789eacfcd640aaea9c16501cff9338d70a/build.sh

### AI (no-evidence-found)

The complete small tree, nested metadata and four commit messages contain no explicit development-AI attribution; this does not establish non-use.
- https://github.com/Ritchie333/skiing/tree/166945789eacfcd640aaea9c16501cff9338d70a
- https://github.com/Ritchie333/skiing/commits/main

### Relationships (reviewed)

skiing.ref distinguishes the original 1982 William Tang/Beam Software game from Ritchie Swann's 2024 disassembly, and the project depends on SkoolKit for presentation rather than claiming SkoolKit itself as part of the recovered game.
- https://github.com/Ritchie333/skiing/blob/166945789eacfcd640aaea9c16501cff9338d70a/src/skiing.ref
- https://github.com/Ritchie333/skiing/blob/166945789eacfcd640aaea9c16501cff9338d70a/build.sh

## Particle-Man — original Atari Jaguar procedural maze game

Project ID: particle-man-atari-jaguar · Overall audit: partial

### Typed catalogue values

```json
{
  "ai": {
    "evidence": [
      "README explicitly describes a human/Codex testing agreement and limits Codex to non-compiling work while the user performs real-hardware compilation and testing."
    ],
    "tools": [
      "OpenAI Codex"
    ],
    "usage": true
  },
  "build": {
    "byte_exact": null,
    "compilable": null,
    "playable": true,
    "runnable": true
  },
  "display_title": "Particle-Man — original Atari Jaguar procedural maze game",
  "id": "particle-man-atari-jaguar",
  "last_activity": "2026-09-20",
  "last_checked": "2026-10-29",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Motorola 68000 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/Tolbat/Particle-man",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Public release-candidate source with upstream-reported real-Jaguar gameplay; final current-build persistence acceptance remains pending",
  "subjects": [
    "Particle-Man"
  ],
  "tags": [
    "Atari Jaguar",
    "JagStudio",
    "RAPTOR",
    "original homebrew",
    "maze game"
  ],
  "target_cpu": [
    "Motorola 68000"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Atari Jaguar"
  ],
  "techniques": [
    "procedural point-cloud graphics",
    "RAPTOR Object Processor integration",
    "GPU particle effects",
    "cartridge EEPROM persistence"
  ],
  "title": "Particle-Man",
  "tool_kinds": [],
  "types": [
    "original homebrew game",
    "native Atari Jaguar game"
  ],
  "upstream_name": "Particle-Man",
  "work_kinds": []
}
```

### Identity (reviewed)

The primary README identifies Particle-Man as a procedural neon maze-chase game for Atari Jaguar with a fifty-level campaign, eight-enemy roster, generated graphics and persistent progression.
- https://github.com/Tolbat/Particle-man/blob/066a5e07fae40e2400e1e87fb82c5b509a91f33f/README.md
- https://github.com/Tolbat/Particle-man/blob/066a5e07fae40e2400e1e87fb82c5b509a91f33f/ParticlePac.c

### Classification (reviewed)

This is substantial original Jaguar homebrew. Its maze-chase design is genre-inspired, but the repository does not claim recovered Pac-Man code, binary analysis or an RE-derived port; procedural game logic and audiovisual generation are implemented locally.
- https://github.com/Tolbat/Particle-man/blob/066a5e07fae40e2400e1e87fb82c5b509a91f33f/README.md
- https://github.com/Tolbat/Particle-man/blob/066a5e07fae40e2400e1e87fb82c5b509a91f33f/ParticlePac.c

### Source CPU (not-applicable)

Particle-Man is original homebrew rather than a reconstruction or port of an original binary, so an original source CPU does not apply.
- https://github.com/Tolbat/Particle-man/blob/066a5e07fae40e2400e1e87fb82c5b509a91f33f/README.md

### Target CPU (reviewed)

The native Jaguar wrapper is Motorola 68000 assembly and transfers control into the compiled C game, while the README separately describes Object Processor/GPU work; the CPU record is limited to the evidenced 68000 execution path.
- https://github.com/Tolbat/Particle-man/blob/066a5e07fae40e2400e1e87fb82c5b509a91f33f/rapapp.s
- https://github.com/Tolbat/Particle-man/blob/066a5e07fae40e2400e1e87fb82c5b509a91f33f/README.md

### Build (reviewed)

The README instructs users to build the normal JagStudio C project `particlepac` and reports C13 as an accepted smooth real-Jaguar gameplay baseline; the current C19f source still awaits its final hardware acceptance run and EEPROM power-cycle retention check. Limitations: No local compilation or hardware test was performed. Runnable/playable reflect upstream real-hardware reports, not independent verification of the current revision.
- https://github.com/Tolbat/Particle-man/blob/066a5e07fae40e2400e1e87fb82c5b509a91f33f/README.md
- https://github.com/Tolbat/Particle-man/blob/066a5e07fae40e2400e1e87fb82c5b509a91f33f/ParticlePac.c

### Runtime profiles (no-evidence-found)

The README documents real-Jaguar testing and a current 128-byte GameDrive save configuration, but it does not state a minimum Jaguar revision, RAM floor, ROM requirement or generally supported cartridge device. These test details were not converted into a minimum profile.
- https://github.com/Tolbat/Particle-man/blob/066a5e07fae40e2400e1e87fb82c5b509a91f33f/README.md
- https://github.com/Tolbat/Particle-man/blob/066a5e07fae40e2400e1e87fb82c5b509a91f33f/rapapp.s

### AI (reviewed)

The README explicitly describes the project's current testing agreement with Codex: the user compiles and tests on real Jaguar hardware, while Codex does not compile or launch the game. This establishes Codex involvement but not independent build verification.
- https://github.com/Tolbat/Particle-man/blob/066a5e07fae40e2400e1e87fb82c5b509a91f33f/README.md

### Relationships (reviewed)

JagStudio and RAPTOR are the documented native development/runtime framework. Genre resemblance does not make Particle-Man a Pac-Man code port, and no external original-game binary is an input to the reviewed build.
- https://github.com/Tolbat/Particle-man/blob/066a5e07fae40e2400e1e87fb82c5b509a91f33f/README.md
- https://github.com/Tolbat/Particle-man/blob/066a5e07fae40e2400e1e87fb82c5b509a91f33f/rapapp.s

## RetroCastX — framebuffer-less retro-PC RGB capture and host reconstruction stack

Project ID: retrocastx-rgb-capture-stack · Overall audit: partial

### Typed catalogue values

```json
{
  "ai": {
    "evidence": [
      "Viewer 0.10.0 and related commits contain explicit Claude Opus 5.5 co-author trailers and Claude session links."
    ],
    "tools": [
      "Claude Opus 5.5"
    ],
    "usage": true
  },
  "build": {
    "byte_exact": null,
    "compilable": true,
    "playable": null,
    "runnable": true
  },
  "display_title": "RetroCastX — framebuffer-less retro-PC RGB capture and host reconstruction stack",
  "id": "retrocastx-rgb-capture-stack",
  "last_activity": "2026-10-25",
  "last_checked": "2026-10-29",
  "re_started": null,
  "reconstructed_languages": [
    "Python",
    "Rust",
    "LiteX",
    "Atopile"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/kunichiko/RetroCastX",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Host loopback/client and simulated FPGA path reported working; physical FPGA/ADC capture remains unverified",
  "subjects": [],
  "tags": [
    "Sharp X68000",
    "NEC PC-98",
    "video preservation",
    "FPGA",
    "analog RGB"
  ],
  "target_cpu": [],
  "target_kinds": [],
  "target_platforms": [
    "Sharp X68000",
    "NEC PC-98",
    "macOS",
    "Windows",
    "Linux"
  ],
  "techniques": [
    "raw line-oriented UDP transport",
    "analog RGB timing preservation",
    "host-side frame reconstruction",
    "palette snapping",
    "FPGA simulation"
  ],
  "title": "RetroCastX",
  "tool_kinds": [
    "asset-tool",
    "automation"
  ],
  "types": [
    "analog RGB capture hardware",
    "FPGA line transport",
    "host video reconstruction client"
  ],
  "upstream_name": "RetroCastX",
  "work_kinds": []
}
```

### Identity (reviewed)

The README identifies RetroCastX as a framebuffer-less analog-RGB capture system for retro PCs such as X68000 and PC-98, spanning an ADC, ECP5 FPGA UDP transport and PC/Mac reconstruction client.
- https://github.com/kunichiko/RetroCastX/blob/01c2b5cdf0227ca12a563020126a55dca0ddcc23/README.md

### Classification (reviewed)

This is original preservation/capture tooling, not a reverse-engineered X68000 or PC-98 software subject. Its relevant contribution is lossless timing-aware acquisition and host reconstruction of legacy video output.
- https://github.com/kunichiko/RetroCastX/blob/01c2b5cdf0227ca12a563020126a55dca0ddcc23/README.md

### Source CPU (not-applicable)

RetroCastX samples analog video signals rather than analysing a particular original executable, so no original source CPU applies.
- https://github.com/kunichiko/RetroCastX/blob/01c2b5cdf0227ca12a563020126a55dca0ddcc23/README.md

### Target CPU (no-evidence-found)

The client is documented for Mac, Windows and Linux and the capture device uses ECP5 FPGA logic, but the reviewed material does not constrain the host program to a specific CPU architecture. No host ISA was inferred from Rust, Python or operating-system names.
- https://github.com/kunichiko/RetroCastX/blob/01c2b5cdf0227ca12a563020126a55dca0ddcc23/README.md

### Build (reviewed)

The README provides Python loopback, waveform and NTSC tests plus simulator/receiver commands; it reports generated FPGA bitstreams, simulation-verified gateware and an end-to-end viewer test against sender_sim. Limitations: The same status list says physical gateware, board manufacture and real X68000/PC-98 capture remain unfinished. No local test or hardware operation was performed.
- https://github.com/kunichiko/RetroCastX/blob/01c2b5cdf0227ca12a563020126a55dca0ddcc23/README.md

### Runtime profiles (not-applicable)

The documented runtime is a modern host/capture stack rather than a runnable build for legacy hardware, and the README states no minimum host CPU/RAM/OS versions suitable for a tracker runtime profile.
- https://github.com/kunichiko/RetroCastX/blob/01c2b5cdf0227ca12a563020126a55dca0ddcc23/README.md

### AI (reviewed)

Viewer 0.10.0 and its preceding implementation commit explicitly credit Claude Opus 5.5 as co-author and include Claude session URLs.
- https://github.com/kunichiko/RetroCastX/commit/5e235dd12fcd5008b247dfee4efae59de12cebd9
- https://github.com/kunichiko/RetroCastX/commit/8b6c980fbaa34721800ddd51f4d1b05be5e0ca5b

### Relationships (reviewed)

The README credits OSSC hardware as the TVP7002 analog-front-end reference. RetroCastX remains a separate design whose FPGA side retains only line buffering while frame reconstruction is performed by its host client.
- https://github.com/kunichiko/RetroCastX/blob/01c2b5cdf0227ca12a563020126a55dca0ddcc23/README.md

## Sources

```json
[
  {
    "first_indexed": "2026-10-29",
    "id": "github-tolbat-particle-man",
    "kind": "github-repository",
    "last_reviewed": "2026-10-29",
    "reason": "Primary repository for the original Atari Jaguar Particle-Man game and its JagStudio/RAPTOR source.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/Tolbat/Particle-man"
  },
  {
    "first_indexed": "2026-10-29",
    "id": "github-kunichiko-retrocastx",
    "kind": "github-repository",
    "last_reviewed": "2026-10-29",
    "reason": "Primary repository for the X68000/PC-98 analog-RGB capture, FPGA transport and host reconstruction stack.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/kunichiko/RetroCastX"
  }
]
```

## Source updates

```json
[
  {
    "id": "github-trufungames-mortal-kombat-atari-jaguar",
    "last_reviewed": "2026-10-29",
    "reason": "Bounded review verified a RAPTOR-based original fan conversion/proof-of-concept implementing the Mortal Kombat character-select screen from arcade assets; it is not described as reverse-engineered code.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-ritchie333-skiing",
    "last_reviewed": "2026-10-29",
    "reason": "Nested SkoolKit metadata and annotated control/skool files establish Horace Goes Skiing identity, Ritchie Swann's 2024 disassembly and Z80 analysis scope.",
    "review_state": "substantially-reviewed"
  }
]
```

## Task updates

```json
[
  {
    "id": "task-review-mortal-kombat-atari-jaguar-fan-conversion",
    "last_reviewed": "2026-10-29",
    "notes_append": "Reviewed readme.txt, _RAPAPP.S and BUILD.bat at commit 58d3f11016ad147c233fb81a5a52acdb5dcf5f2f. The repository explicitly calls the work a proof-of-concept built from original arcade graphics, music and sound effects, while the source implements Jaguar-native RAPTOR input, sprites and sampled audio. Classified as a fan conversion/demo, not RE-derived source.",
    "state": "done"
  },
  {
    "id": "task-review-ritchie333-skiing-nested-skoolkit-project",
    "last_reviewed": "2026-10-29",
    "notes_append": "Reviewed the complete eight-entry tree and nested skiing.ref, skiing.ctl, skiing.skool and build.sh at commit 166945789eacfcd640aaea9c16501cff9338d70a. The project identifies Horace Goes Skiing, credits William Tang/Beam Software code and Ritchie Swann's 2024 disassembly, and generates annotated SkoolKit HTML rather than a rebuilt game binary.",
    "state": "done"
  }
]
```

## Decisions

```json
[
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/Tolbat/Particle-man/blob/066a5e07fae40e2400e1e87fb82c5b509a91f33f/README.md",
      "https://github.com/Tolbat/Particle-man/blob/066a5e07fae40e2400e1e87fb82c5b509a91f33f/ParticlePac.c",
      "https://github.com/Tolbat/Particle-man/blob/066a5e07fae40e2400e1e87fb82c5b509a91f33f/rapapp.s"
    ],
    "id": "particle-man-atari-jaguar-promoted",
    "project_ids": [
      "particle-man-atari-jaguar"
    ],
    "reason": "The primary README and implementation establish a substantial original Jaguar maze game with a fifty-level campaign, procedural graphics, RAPTOR/JagStudio integration, persistent scores and upstream-reported real-hardware gameplay. It is original homebrew, not an RE-derived Pac-Man port.",
    "reviewed_at": "2026-10-29",
    "source_ids": [
      "github-tolbat-particle-man"
    ],
    "title": "Particle-Man",
    "url": "https://github.com/Tolbat/Particle-man"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/kunichiko/RetroCastX/blob/01c2b5cdf0227ca12a563020126a55dca0ddcc23/README.md",
      "https://github.com/kunichiko/RetroCastX/commit/5e235dd12fcd5008b247dfee4efae59de12cebd9"
    ],
    "id": "retrocastx-promoted",
    "project_ids": [
      "retrocastx-rgb-capture-stack"
    ],
    "reason": "The repository documents and implements a distinct preservation/capture stack that samples legacy analog RGB, transports raw timing over FPGA/Gigabit Ethernet and reconstructs frames in a host client; simulation and host loopback are reported working while real capture hardware remains unverified.",
    "reviewed_at": "2026-10-29",
    "source_ids": [
      "github-kunichiko-retrocastx"
    ],
    "title": "RetroCastX",
    "url": "https://github.com/kunichiko/RetroCastX"
  }
]
```

## Research event notes

The CPU audit queue reported zero unresolved source/target CPU areas, so no quota-driven CPU edits were invented. Four fresh-search routes were rotated away from the immediately preceding Oric, BBC Micro and Apple IIgs pass: GitHub repository queries `"Atari Jaguar" disassembly OR reconstruction OR homebrew RAPTOR`, `"X68000" disassembly OR decompilation OR source reconstruction`, and `"Commodore PET" ROM disassembly OR source reconstruction`, plus the scoped GitHub code query `"Commodore PET" disassembly`. The Jaguar route promoted Particle-Man and also completed the older Mortal Kombat fan-conversion review. The X68000 route promoted RetroCastX at its demonstrated capture/preservation scope, not as an X68000 software reconstruction. The PET repository query returned no candidates; the code search resolved its substantive hits to already tracked Regenerator 2000, SSE SoftBox and PEDISK II records, while the remaining hits were references or unrelated monitor-ROM work. The saved queue also closed Ritchie333/skiing after nested SkoolKit files established Horace Goes Skiing identity, Z80 analysis scope and authorship. Earlier deferred decisions for Mortal Kombat and skiing remain historical research state and are superseded for inclusion by this bounded source review. No upstream project was compiled, executed, played or tested on hardware during this pass.
