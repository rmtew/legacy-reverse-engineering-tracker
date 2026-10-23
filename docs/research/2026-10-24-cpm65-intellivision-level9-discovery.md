# CP/M-65, pkIntvMCP and Level 9 discovery review

Review an old Level 9 source and four rotated GitHub code-search routes; add CP/M-65 and pkIntvMCP, and refresh the reconstructed Level 9 toolchain.

Date: 2026-10-24 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- pkintvmcp-cp1600-debugger / Build (reviewed): The tracker did not install dependencies, build, run tests, execute ROMs or compare behavior with jzIntv. The README's earlier planning prose is partly stale relative to the implemented MCP server.
- cpm65-native-6502-os / Build (reviewed): The tracker did not build the aggregate dependency graph, download ROMs, run MAME, write media or boot any image. Peripheral and emulator limitations differ by platform.
- cpm65-native-6502-os / AI (no-evidence-found): The inspected primary README, root tree and pinned head commit contain no explicit development-AI contribution disclosure. This bounded absence does not establish non-use.
- level9-l9dev-toolchain-reconstruction / Build (reviewed): No local compilation or regression run was performed. The README explicitly leaves graphics, v1-v2 messaging/input and broader packaging incomplete, and lists missing or corrupted historical inputs.
- level9-l9dev-toolchain-reconstruction / AI (no-evidence-found): The inspected l9dev README, Makefile and current head commit provide no explicit development-AI contribution disclosure. This does not establish non-use.

## pkIntvMCP — AI-assisted CP-1600 emulator and debugger

Project ID: pkintvmcp-cp1600-debugger · Overall audit: reviewed

### Typed catalogue values

```json
{
  "ai": {
    "evidence": [
      "Latest reviewed commit explicitly says it was generated with Claude Code and carries a Claude Sonnet 4.5 co-author trailer: f518a181e9c6abe51661471de495a2009290de13"
    ],
    "tools": [
      "Claude Code"
    ],
    "usage": true
  },
  "build": {
    "byte_exact": null,
    "compilable": true,
    "playable": null,
    "runnable": true
  },
  "display_title": "pkIntvMCP — AI-assisted CP-1600 emulator and debugger",
  "id": "pkintvmcp-cp1600-debugger",
  "last_activity": "2025-12-17",
  "last_checked": "2026-10-24",
  "re_started": null,
  "reconstructed_languages": [
    "TypeScript"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/peterkaminski/pkintvmcp",
  "runtime_profiles": [
    {
      "evidence": [
        "https://github.com/peterkaminski/pkintvmcp/blob/f518a181e9c6abe51661471de495a2009290de13/package.json"
      ],
      "name": "Node.js MCP server and CLI",
      "notes": "The root package manifest states the host runtime versions. No host CPU or RAM minimum is documented or inferred.",
      "os": "Node.js >=18; npm >=9",
      "platform": "Node.js"
    }
  ],
  "source_cpu": [
    "General Instrument CP1610"
  ],
  "source_language": [
    "CP-1600 machine code"
  ],
  "source_platforms": [
    "Intellivision"
  ],
  "status": "Alpha CP-1600 emulator and MCP debugger; full Intellivision system integration and external jzIntv validation remain incomplete",
  "subjects": [
    "pkIntvMCP",
    "Intellivision",
    "CP-1600"
  ],
  "tags": [
    "Intellivision",
    "CP-1600",
    "MCP",
    "alpha"
  ],
  "target_cpu": [],
  "target_kinds": [],
  "target_platforms": [
    "Node.js"
  ],
  "techniques": [
    "instruction-set emulation",
    "execution tracing",
    "breakpoints and watchpoints",
    "memory inspection",
    "MCP tool interface"
  ],
  "title": "pkIntvMCP",
  "tool_kinds": [
    "emulator",
    "debugger",
    "disassembler",
    "automation"
  ],
  "types": [
    "CPU emulator",
    "MCP debugging server",
    "ROM analysis tool"
  ],
  "upstream_name": "pkIntvMCP",
  "work_kinds": [
    "binary-analysis"
  ]
}
```

### Identity (reviewed)

The repository identifies pkIntvMCP as Peter Kaminski's CP-1600/Intellivision emulator and debugging tool, with a TypeScript workspace containing core, CLI and MCP-server packages.
- https://github.com/peterkaminski/pkintvmcp
- https://github.com/peterkaminski/pkintvmcp/blob/f518a181e9c6abe51661471de495a2009290de13/README.md

### Classification (reviewed)

This is modern retro-development tooling: it emulates and disassembles CP-1600 instructions, exposes execution and inspection through MCP, and is designed for debugging or reverse-engineering Intellivision ROMs. It is not a game reconstruction or full gameplay emulator.
- https://github.com/peterkaminski/pkintvmcp/blob/f518a181e9c6abe51661471de495a2009290de13/README.md
- https://github.com/peterkaminski/pkintvmcp/blob/f518a181e9c6abe51661471de495a2009290de13/packages/mcp-cpu/src/server.ts

### Source CPU (reviewed)

The reviewed implementation and documentation explicitly target CP-1600/Intellivision machine code; the tracker uses the established General Instrument CP1610 catalogue label for that source architecture.
- https://github.com/peterkaminski/pkintvmcp/blob/f518a181e9c6abe51661471de495a2009290de13/README.md
- https://github.com/peterkaminski/pkintvmcp/tree/f518a181e9c6abe51661471de495a2009290de13/packages/core/src

### Target CPU (not-applicable)

The output is host-side TypeScript tooling rather than a generated retro-machine binary. No fixed host instruction set is assigned from Node.js or the development language.
- https://github.com/peterkaminski/pkintvmcp/blob/f518a181e9c6abe51661471de495a2009290de13/package.json

### Build (reviewed)

The workspace provides build and test scripts, a runnable CLI and an implemented stdio MCP server. The README reports 348 passing tests and a complete 79-instruction CPU core, while also marking the project alpha and external jzIntv validation incomplete. Limitations: The tracker did not install dependencies, build, run tests, execute ROMs or compare behavior with jzIntv. The README's earlier planning prose is partly stale relative to the implemented MCP server.
- https://github.com/peterkaminski/pkintvmcp/blob/f518a181e9c6abe51661471de495a2009290de13/README.md
- https://github.com/peterkaminski/pkintvmcp/blob/f518a181e9c6abe51661471de495a2009290de13/package.json
- https://github.com/peterkaminski/pkintvmcp/blob/f518a181e9c6abe51661471de495a2009290de13/packages/mcp-cpu/src/server.ts

### Runtime profiles (reviewed)

The root package manifest explicitly requires Node.js 18 or newer and npm 9 or newer for the host tools. No CPU, RAM or operating-system minimum is stated.
- https://github.com/peterkaminski/pkintvmcp/blob/f518a181e9c6abe51661471de495a2009290de13/package.json

### AI (reviewed)

The latest reviewed commit explicitly says it was generated with Claude Code and includes a Claude Sonnet 4.5 co-author trailer. Claude is also the intended conversational debugging client, but that integration alone is kept separate from the contribution evidence.
- https://github.com/peterkaminski/pkintvmcp/commit/f518a181e9c6abe51661471de495a2009290de13
- https://github.com/peterkaminski/pkintvmcp/blob/f518a181e9c6abe51661471de495a2009290de13/README.md

### Relationships (reviewed)

The README explicitly positions jzIntv as the reference emulator and says pkIntvMCP is a debugging/analysis companion rather than a replacement. External validation against jzIntv is still pending.
- https://github.com/peterkaminski/pkintvmcp/blob/f518a181e9c6abe51661471de495a2009290de13/README.md

## CP/M-65 — native CP/M port for 6502-family systems

Project ID: cpm65-native-6502-os · Overall audit: reviewed

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
  "display_title": "CP/M-65 — native CP/M port for 6502-family systems",
  "id": "cpm65-native-6502-os",
  "last_activity": "2026-04-05",
  "last_checked": "2026-10-24",
  "re_started": null,
  "reconstructed_languages": [
    "6502 assembly",
    "65C02 assembly",
    "65816 assembly",
    "C",
    "C++",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/davidgiven/cpm65",
  "runtime_profiles": [
    {
      "cpu_family": "6502 family",
      "evidence": [
        "https://github.com/davidgiven/cpm65/blob/ff7f5f938607195c562e53f0a4558086aab4663a/README.md"
      ],
      "min_ram_kib": 16,
      "name": "Atari 400/800 XL/XE disk build",
      "notes": "The standard disk and hard-disk builds run with at least 16 KiB; the XL/XE-specific xlhd build requires at least 64 KiB.",
      "platform": "Atari 8-bit"
    },
    {
      "cpu_family": "6502 family",
      "evidence": [
        "https://github.com/davidgiven/cpm65/blob/ff7f5f938607195c562e53f0a4558086aab4663a/README.md"
      ],
      "min_ram_kib": 64,
      "name": "Oric 1 / Oric Atmos Microdisc build",
      "notes": "Oric 1 requires the full 64 KiB upgrade including overlay RAM; only the Microdisc interface currently works reliably.",
      "platform": "Oric"
    },
    {
      "cpu_family": "6502 family",
      "evidence": [
        "https://github.com/davidgiven/cpm65/blob/ff7f5f938607195c562e53f0a4558086aab4663a/README.md"
      ],
      "min_ram_kib": 35,
      "name": "Fully expanded VIC-20 build",
      "notes": "README requires a fully expanded VIC-20 with all memory banks populated for the full 35 KiB configuration; several drive/loader image variants have different peripheral requirements.",
      "platform": "Commodore VIC-20"
    },
    {
      "cpu_family": "6502 family",
      "evidence": [
        "https://github.com/davidgiven/cpm65/blob/ff7f5f938607195c562e53f0a4558086aab4663a/README.md"
      ],
      "min_ram_kib": 16,
      "name": "Ohio Scientific build",
      "notes": "README states support for Ohio Scientific systems with at least 16 KiB and a floppy drive.",
      "platform": "Ohio Scientific"
    },
    {
      "cpu_family": "6502 family",
      "evidence": [
        "https://github.com/davidgiven/cpm65/blob/ff7f5f938607195c562e53f0a4558086aab4663a/README.md"
      ],
      "name": "Apple IIe build",
      "notes": "Requires an 80-column card but explicitly does not require auxiliary memory; two slot-6 drives are supported.",
      "platform": "Apple IIe"
    }
  ],
  "source_cpu": [
    "Intel 8080"
  ],
  "source_language": [
    "CP/M system interfaces",
    "8080 machine code"
  ],
  "source_platforms": [
    "CP/M"
  ],
  "status": "Native 6502-family CP/M port with binary releases, cross/native development tools and broad hardware support",
  "subjects": [
    "CP/M-65",
    "CP/M"
  ],
  "tags": [
    "CP/M",
    "6502",
    "65C02",
    "65816",
    "cross-platform"
  ],
  "target_cpu": [
    "6502",
    "65C02",
    "65816"
  ],
  "target_kinds": [
    "operating-system"
  ],
  "target_platforms": [
    "BBC Micro",
    "Acorn Electron",
    "Commodore 64",
    "Commodore VIC-20",
    "Commodore PET",
    "Commander X16",
    "Apple IIe",
    "Atari 8-bit",
    "Oric",
    "Super Nintendo",
    "KIM-1",
    "Ohio Scientific",
    "Sorbus",
    "neo6502",
    "nano6502"
  ],
  "techniques": [
    "native operating-system porting",
    "relocatable binaries",
    "platform BIOS implementations",
    "cross compilation",
    "MAME regression testing"
  ],
  "title": "CP/M-65",
  "tool_kinds": [],
  "types": [
    "native operating-system port",
    "retro development environment"
  ],
  "upstream_name": "CP/M-65",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

David Given's repository identifies CP/M-65 as a native port of Digital Research's CP/M to the 6502, with a coherent operating system, applications, libraries, build system, disk images and tests.
- https://github.com/davidgiven/cpm65
- https://github.com/davidgiven/cpm65/blob/ff7f5f938607195c562e53f0a4558086aab4663a/README.md

### Classification (reviewed)

This is a native reimplementation/port of the CP/M operating environment for 6502-family machines, with relocatable application binaries and both cross-hosted and native development tools. It is not labelled binary-derived reverse engineering.
- https://github.com/davidgiven/cpm65/blob/ff7f5f938607195c562e53f0a4558086aab4663a/README.md

### Source CPU (reviewed)

The README contrasts CP/M-65 with original 8080 CP/M programs and explicitly says it does not run 8080 binaries; Intel 8080 is recorded as the source architecture of the operating-system subject, not as an emulated CPU.
- https://github.com/davidgiven/cpm65/blob/ff7f5f938607195c562e53f0a4558086aab4663a/README.md

### Target CPU (reviewed)

The repository documents native 6502 and 65C02 machines and a Super Nintendo build using 65816 code; these are explicit output architectures, not inferred from platform names alone.
- https://github.com/davidgiven/cpm65/blob/ff7f5f938607195c562e53f0a4558086aab4663a/README.md

### Build (reviewed)

README supplies binary releases and an llvm-mos-based Makefile workflow that builds bootable images for supported targets. It also documents automated MAME tests for a subset of platforms and native/cross development tools. Limitations: The tracker did not build the aggregate dependency graph, download ROMs, run MAME, write media or boot any image. Peripheral and emulator limitations differ by platform.
- https://github.com/davidgiven/cpm65/blob/ff7f5f938607195c562e53f0a4558086aab4663a/README.md
- https://github.com/davidgiven/cpm65/blob/ff7f5f938607195c562e53f0a4558086aab4663a/Makefile

### Runtime profiles (reviewed)

The reviewed README provides explicit memory or hardware requirements for Atari, Oric, fully expanded VIC-20, Ohio Scientific and Apple IIe variants. Only those stated requirements are captured; other platform model names are not converted into guessed CPU or RAM minima.
- https://github.com/davidgiven/cpm65/blob/ff7f5f938607195c562e53f0a4558086aab4663a/README.md

### AI (no-evidence-found)

The inspected primary README, root tree and pinned head commit contain no explicit development-AI contribution disclosure. This bounded absence does not establish non-use.
- https://github.com/davidgiven/cpm65/blob/ff7f5f938607195c562e53f0a4558086aab4663a/README.md
- https://github.com/davidgiven/cpm65/commit/ff7f5f938607195c562e53f0a4558086aab4663a

### Relationships (reviewed)

The project is explicitly related to Digital Research CP/M but produces native relocatable 6502-family applications rather than emulating or translating existing 8080 binaries. Its many machine ports are one coherent repository-level operating-system project.
- https://github.com/davidgiven/cpm65/blob/ff7f5f938607195c562e53f0a4558086aab4663a/README.md

## level9-l9dev-toolchain-reconstruction

Project ID: level9-l9dev-toolchain-reconstruction · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "level9-l9dev-toolchain-reconstruction",
  "last_checked": "2026-10-24",
  "runtime_profiles": [
    {
      "evidence": [
        "https://github.com/MikeTheTechie/Level9-Public/blob/02aaab0a9326292b01b213c727528e39b0d7e2a5/l9dev/README.md"
      ],
      "name": "Linux l9dev tools and interpreters",
      "notes": "The README provides make/install instructions and Ubuntu 24.04 binaries. No host CPU or RAM minimum is stated or inferred.",
      "os": "Ubuntu 24.04 prebuilt executables provided",
      "platform": "Linux"
    }
  ],
  "status": "Reconstructed Linux toolchain with ST/PC interpreters, HUGE text-only support and regression fixtures; graphics and v1-v2 support remain incomplete",
  "techniques": [
    "manual source recoding",
    "behavioral regression testing",
    "binary-compatibility testing",
    "ST and PC machine-code interpretation",
    "address-sanitizer verification"
  ]
}
```

Expected existing project SHA256: 6b8a1b9f043851aa9a80da3369ca476b1f6b68009d4ce94e9a2ad64edd3f20e8

### Identity (reviewed)

The l9dev directory remains one coherent reconstruction of Level 9's development tools, recoded in C from Atari ST 68000 assembler. The current source now includes compiler, finisher, squasher, menu and interpreter programs.
- https://github.com/MikeTheTechie/Level9-Public/tree/02aaab0a9326292b01b213c727528e39b0d7e2a5/l9dev
- https://github.com/MikeTheTechie/Level9-Public/blob/02aaab0a9326292b01b213c727528e39b0d7e2a5/l9dev/README.md

### Classification (reviewed)

The project is both a source reconstruction of historical Level 9 authoring tools and an active Linux compiler/interpreter environment useful for preserved game sources. New interpreters expand the same toolchain rather than constituting a separate project.
- https://github.com/MikeTheTechie/Level9-Public/blob/02aaab0a9326292b01b213c727528e39b0d7e2a5/l9dev/README.md
- https://github.com/MikeTheTechie/Level9-Public/blob/02aaab0a9326292b01b213c727528e39b0d7e2a5/l9dev/Makefile

### Source CPU (reviewed)

The primary README explicitly says the C tools were recoded from Atari ST 68000 assembler, establishing m68000 as the historical source architecture.
- https://github.com/MikeTheTechie/Level9-Public/blob/02aaab0a9326292b01b213c727528e39b0d7e2a5/l9dev/README.md

### Target CPU (not-applicable)

The reconstructed tools are host C programs for Linux; no fixed Linux host CPU is documented. Their optional generation or interpretation of ST/PC machine code is a tool capability, not a minimum host CPU.
- https://github.com/MikeTheTechie/Level9-Public/blob/02aaab0a9326292b01b213c727528e39b0d7e2a5/l9dev/README.md
- https://github.com/MikeTheTechie/Level9-Public/blob/02aaab0a9326292b01b213c727528e39b0d7e2a5/l9dev/Makefile

### Build (reviewed)

The current Makefile builds l9comp, l9finish, l9int, l9menu and l9squash with GCC, while scripts drive game generation and table assembly. The README documents ST/PC interpreter modes, text-only HUGE support and compile/run regression suites. Limitations: No local compilation or regression run was performed. The README explicitly leaves graphics, v1-v2 messaging/input and broader packaging incomplete, and lists missing or corrupted historical inputs.
- https://github.com/MikeTheTechie/Level9-Public/blob/02aaab0a9326292b01b213c727528e39b0d7e2a5/l9dev/README.md
- https://github.com/MikeTheTechie/Level9-Public/blob/02aaab0a9326292b01b213c727528e39b0d7e2a5/l9dev/Makefile

### Runtime profiles (reviewed)

The README provides Ubuntu 24.04 executables and a generic Linux make/install route. No minimum host processor or RAM is stated, so none is inferred.
- https://github.com/MikeTheTechie/Level9-Public/blob/02aaab0a9326292b01b213c727528e39b0d7e2a5/l9dev/README.md

### AI (no-evidence-found)

The inspected l9dev README, Makefile and current head commit provide no explicit development-AI contribution disclosure. This does not establish non-use.
- https://github.com/MikeTheTechie/Level9-Public/blob/02aaab0a9326292b01b213c727528e39b0d7e2a5/l9dev/README.md
- https://github.com/MikeTheTechie/Level9-Public/commit/02aaab0a9326292b01b213c727528e39b0d7e2a5

### Relationships (reviewed)

The toolchain is derived from Level 9's Atari ST 68000 authoring programs, incorporates observed v1.5 behavior, and credits the GS/DK interpreter for verification. Preserved game sources and regression fixtures are inputs/tests, not separate l9dev implementations.
- https://github.com/MikeTheTechie/Level9-Public/blob/02aaab0a9326292b01b213c727528e39b0d7e2a5/l9dev/README.md

## Sources

```json
[
  {
    "first_indexed": "2026-10-24",
    "id": "github-peterkaminski-pkintvmcp",
    "kind": "github-repository",
    "last_reviewed": "2026-10-24",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Primary repository for the TypeScript CP-1600 emulator, disassembler and MCP debugging server.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/peterkaminski/pkintvmcp"
  },
  {
    "first_indexed": "2026-10-24",
    "id": "github-davidgiven-cpm65",
    "kind": "github-repository",
    "last_reviewed": "2026-10-24",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Primary repository for CP/M-65, a native CP/M port and development environment for 6502-family retro systems.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/davidgiven/cpm65"
  },
  {
    "first_indexed": "2026-10-24",
    "id": "search-2026-10-24-intellivision-disassembly",
    "kind": "github-code-search",
    "last_reviewed": "2026-10-24",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Fresh-search slice. Exact query `Intellivision disassembly` surfaced peterkaminski/pkintvmcp, whose pinned README, MCP server, package manifest and current commit attribution were reviewed and promoted. Other returned roots were already tracked, generic emulators, curated indexes or unrelated keyword co-occurrences.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/search?q=Intellivision+disassembly&type=code"
  },
  {
    "first_indexed": "2026-10-24",
    "id": "search-2026-10-24-oric-atmos-homebrew",
    "kind": "github-code-search",
    "last_reviewed": "2026-10-24",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Fresh-search slice. Exact query `Oric Atmos homebrew` surfaced davidgiven/cpm65. Its pinned README and repository implementation tree were reviewed; the Oric port is one of many coherent CP/M-65 targets, so one repository-root project was promoted rather than a platform-fragment record.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/search?q=Oric+Atmos+homebrew&type=code"
  },
  {
    "first_indexed": "2026-10-24",
    "id": "search-2026-10-24-coco-disassembly",
    "kind": "github-code-search",
    "last_reviewed": "2026-10-24",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Fresh-search slice. Exact query `TRS-80 Color Computer disassembly` returned the already tracked Computer Archeology collection as its material candidate. Other results were indexes, broad emulators, unrelated repositories or documentation-only matches; no new candidate was promoted.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/search?q=TRS-80+Color+Computer+disassembly&type=code"
  },
  {
    "first_indexed": "2026-10-24",
    "id": "search-2026-10-24-sharp-mz-reconstruction",
    "kind": "github-code-search",
    "last_reviewed": "2026-10-24",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Fresh-search slice. Exact query `Sharp MZ source reconstruction` produced only modern machine-learning and incidental text matches in the reviewed result page; no Sharp MZ retro-development candidate URL was identified.",
    "review_state": "exhausted",
    "source": "https://github.com/search?q=Sharp+MZ+source+reconstruction&type=code"
  }
]
```

## Source updates

```json
[
  {
    "id": "github-mikethetechie-level9-public",
    "last_reviewed": "2026-10-24",
    "reason": "Rechecked the current repository root and l9dev at commit 02aaab0a9326292b01b213c727528e39b0d7e2a5. The reconstructed C toolchain now includes ST and PC machine-code interpreters, debug/autorun modes, text-only HUGE support, game selection and expanded regression fixtures; missing v1-v2 messaging/input and graphics remain explicit limitations. The root game/sys/floppy archive graph is now substantially reviewed, while its broad ecosystem tracking task remains open.",
    "review_state": "substantially-reviewed"
  }
]
```

## Task updates

```json
[
  {
    "id": "task-mine-winuae-copperline-resource-tos-toolchains-the-level-9-archive-and-t",
    "last_reviewed": "2026-10-24",
    "notes_append": "Reviewed the current Level9-Public root and l9dev expansion at 02aaab0a9326292b01b213c727528e39b0d7e2a5. The existing l9dev project now covers the added ST/PC interpreter and regression scope; no separate title was split from the coherent toolchain. Other sources named by this broad task remain open.",
    "state": "in-progress"
  }
]
```

## Decisions

```json
[
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/peterkaminski/pkintvmcp/blob/f518a181e9c6abe51661471de495a2009290de13/README.md",
      "https://github.com/peterkaminski/pkintvmcp/blob/f518a181e9c6abe51661471de495a2009290de13/packages/mcp-cpu/src/server.ts",
      "https://github.com/peterkaminski/pkintvmcp/blob/f518a181e9c6abe51661471de495a2009290de13/package.json"
    ],
    "id": "discovery-2026-10-24-promote-pkintvmcp-cp1600-debugger",
    "project_ids": [
      "pkintvmcp-cp1600-debugger"
    ],
    "reason": "Implemented TypeScript CP-1600 core, disassembler, execution controls and MCP inspection server form a substantive Intellivision debugging and binary-analysis environment. Full-system emulation and external jzIntv validation remain incomplete.",
    "reviewed_at": "2026-10-24",
    "source_ids": [
      "github-peterkaminski-pkintvmcp",
      "search-2026-10-24-intellivision-disassembly"
    ],
    "title": "pkIntvMCP — AI-assisted CP-1600 emulator and debugger",
    "url": "https://github.com/peterkaminski/pkintvmcp"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/davidgiven/cpm65/blob/ff7f5f938607195c562e53f0a4558086aab4663a/README.md",
      "https://github.com/davidgiven/cpm65/blob/ff7f5f938607195c562e53f0a4558086aab4663a/Makefile"
    ],
    "id": "discovery-2026-10-24-promote-cpm65-native-6502-os",
    "project_ids": [
      "cpm65-native-6502-os"
    ],
    "reason": "Coherent native CP/M reimplementation targets many 6502, 65C02 and 65816 machines, provides relocatable applications and development tools, and documents build, release, test and hardware-specific runtime requirements. It does not emulate 8080 binaries.",
    "reviewed_at": "2026-10-24",
    "source_ids": [
      "github-davidgiven-cpm65",
      "search-2026-10-24-oric-atmos-homebrew"
    ],
    "title": "CP/M-65 — native CP/M port for 6502-family systems",
    "url": "https://github.com/davidgiven/cpm65"
  }
]
```

## Source ids

```json
[
  "github-mikethetechie-level9-public",
  "github-peterkaminski-pkintvmcp",
  "github-davidgiven-cpm65",
  "search-2026-10-24-intellivision-disassembly",
  "search-2026-10-24-oric-atmos-homebrew",
  "search-2026-10-24-coco-disassembly",
  "search-2026-10-24-sharp-mz-reconstruction"
]
```

## Research event notes

The CPU audit queue returned zero unresolved source or target CPU areas before candidate selection. Exact GitHub code-search queries were `Intellivision disassembly`, `Oric Atmos homebrew`, `TRS-80 Color Computer disassembly`, and `Sharp MZ source reconstruction`. Primary repository evidence was reviewed for two new candidates. The TRS-80/CoCo route resolved to the already tracked Computer Archeology project; the Sharp MZ route returned no relevant retro-development candidate. No upstream software, ROM, image, test suite, compiler or emulator was executed. Build and runtime flags reflect bounded primary-source claims only.
