# Jaguar ports, cartridge analysis and CPC listing-tool discovery

Reviewed an older CPC collection and a rotated Jaguar/TRS-80/X68000/Vectrex search slice

Date: 2026-10-27 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- typer-inner-checker-locomotive-basic / Runtime profiles (no-evidence-found): The reviewed material says the page opens in a browser but gives no minimum CPU, RAM, browser or operating-system requirement suitable for a runtime profile.
- atari-jaguar-240p-test-suite-port / Runtime profiles (no-evidence-found): Native Atari Jaguar execution and cartridge/emulator loading routes are documented, but no variant-specific minimum CPU/RAM profile beyond the target console was established.
- atari-jaguar-240p-test-suite-port / AI (no-evidence-found): The repository contains agent-configuration files, but those are not contribution evidence; the reviewed README and primary project material do not explicitly attribute implementation to an AI tool, so usage remains unknown.
- jaglba-atari-jaguar-port / Runtime profiles (no-evidence-found): The documentation establishes Atari Jaguar and BigPEmu execution paths and a 6 MB cartridge image, but it does not provide a variant minimum CPU/RAM profile beyond the console target.
- jaglba-atari-jaguar-port / AI (no-evidence-found): No explicit development-AI attribution was established in the reviewed README and provenance document; absence is recorded as unknown rather than non-use.
- tolbat-jaguar-cartridge-reader / Target CPU (no-evidence-found): The reviewed fork documents Arduino IDE and library dependencies but does not explicitly identify a processor model in its own primary material; no firmware CPU is inferred from the hardware family.
- tolbat-jaguar-cartridge-reader / Runtime profiles (no-evidence-found): The reviewed fork does not provide a complete minimum hardware profile for the standalone reader, so no CPU/RAM/chipset runtime profile is recorded.
- tolbat-jaguar-cartridge-reader / AI (no-evidence-found): No explicit development-AI attribution was found in the reviewed README or firmware header; usage remains unknown.

## Typer Inner Checker — Locomotive BASIC listing validator

Project ID: typer-inner-checker-locomotive-basic · Overall audit: reviewed

### Typed catalogue values

```json
{
  "ai": {
    "evidence": [
      "The checked-in Claude-discussion.txt transcript records Brett's requests and Claude's implementation, extension and test descriptions for the tool."
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
    "runnable": null
  },
  "display_title": "Typer Inner Checker — Locomotive BASIC listing validator",
  "github_path": "Typer-Inner-Checker",
  "id": "typer-inner-checker-locomotive-basic",
  "last_activity": null,
  "last_checked": "2026-10-27",
  "project_url": "https://github.com/BrettHallen/Amstrad-CPC/tree/main/Typer-Inner-Checker",
  "re_started": null,
  "reconstructed_languages": [
    "HTML",
    "JavaScript",
    "CSS"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/BrettHallen/Amstrad-CPC",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [
    "Locomotive BASIC source listings"
  ],
  "source_platforms": [
    "Amstrad CPC"
  ],
  "status": "Primary source and development transcript reviewed; independent browser execution not performed",
  "subjects": [],
  "tags": [
    "Amstrad CPC",
    "Locomotive BASIC",
    "AI-assisted"
  ],
  "target_cpu": [],
  "target_kinds": [],
  "target_platforms": [],
  "techniques": [
    "keyword recognition",
    "syntax validation",
    "jump-target analysis",
    "BAS text normalization"
  ],
  "title": "Typer Inner Checker",
  "tool_kinds": [
    "static-analysis",
    "language-tooling"
  ],
  "types": [
    "Locomotive BASIC listing checker"
  ],
  "upstream_name": "Typer Inner Checker",
  "work_kinds": []
}
```

### Identity (reviewed)

The monorepo root identifies Typer Inner Checker as a browser page for checking Locomotive BASIC program listings, and the directory contains the self-contained implementation.
- https://github.com/BrettHallen/Amstrad-CPC/blob/5570544eeb983c5a58893272335011cf44615521/README.md
- https://github.com/BrettHallen/Amstrad-CPC/blob/5570544eeb983c5a58893272335011cf44615521/Typer-Inner-Checker/Typer-Inner-Checker.html

### Classification (reviewed)

This is modern retro-development tooling: it validates source listings, recognizes BASIC vocabulary, checks line structure and references, and supports listing load/save; it is not an emulator and does not execute programs.
- https://github.com/BrettHallen/Amstrad-CPC/blob/5570544eeb983c5a58893272335011cf44615521/Typer-Inner-Checker/Typer-Inner-Checker.html

### Source CPU (not-applicable)

The tool analyzes textual Locomotive BASIC listings rather than an original machine-code binary, so assigning the CPC's processor as a recovered source CPU would be misleading.
- https://github.com/BrettHallen/Amstrad-CPC/blob/5570544eeb983c5a58893272335011cf44615521/README.md

### Target CPU (not-applicable)

The output is normalized BASIC text and saved BAS files, not a native CPU-targeted port or reconstructed binary.
- https://github.com/BrettHallen/Amstrad-CPC/blob/5570544eeb983c5a58893272335011cf44615521/Typer-Inner-Checker/Typer-Inner-Checker.html

### Build (reviewed)

The inspected artifact is a self-contained HTML/CSS/JavaScript page. No browser execution or functional test was performed in this pass, so build and runnable flags remain unknown.
- https://github.com/BrettHallen/Amstrad-CPC/blob/5570544eeb983c5a58893272335011cf44615521/Typer-Inner-Checker/Typer-Inner-Checker.html

### Runtime profiles (no-evidence-found)

The reviewed material says the page opens in a browser but gives no minimum CPU, RAM, browser or operating-system requirement suitable for a runtime profile.
- https://github.com/BrettHallen/Amstrad-CPC/blob/5570544eeb983c5a58893272335011cf44615521/Typer-Inner-Checker/Claude-discussion.txt

### AI (reviewed)

The repository preserves a detailed Brett/Claude development transcript in which Claude states that it built, extended and tested the checker; this is explicit project-specific AI contribution evidence.
- https://github.com/BrettHallen/Amstrad-CPC/blob/5570544eeb983c5a58893272335011cf44615521/Typer-Inner-Checker/Claude-discussion.txt

### Relationships (reviewed)

Typer Inner Checker is a separate titled tool inside BrettHallen/Amstrad-CPC. It supports transcribing CPC listings and is distinct from the repository's Laserwarp analysis and hardware subprojects.
- https://github.com/BrettHallen/Amstrad-CPC/blob/5570544eeb983c5a58893272335011cf44615521/README.md

## 240p Test Suite — Atari Jaguar native diagnostics

Project ID: atari-jaguar-240p-test-suite-port · Overall audit: reviewed

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
  "display_title": "240p Test Suite — Atari Jaguar native diagnostics",
  "id": "atari-jaguar-240p-test-suite-port",
  "last_activity": "2026-04-28",
  "last_checked": "2026-10-27",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "assembly",
    "Make"
  ],
  "record_class": "subject",
  "repo": "https://github.com/JoeMatt/atari_jaguar_240p_test_suite",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Active Jaguar fork with v0.x releases; primary source reviewed, independent build/run not performed",
  "subjects": [
    "240p Test Suite"
  ],
  "tags": [
    "Atari Jaguar",
    "homebrew",
    "diagnostics"
  ],
  "target_cpu": [
    "m68k"
  ],
  "target_kinds": [
    "application"
  ],
  "target_platforms": [
    "Atari Jaguar"
  ],
  "techniques": [
    "bare-metal console port",
    "display calibration patterns",
    "hardware diagnostics"
  ],
  "title": "Atari Jaguar 240p Test Suite",
  "tool_kinds": [],
  "types": [
    "Native homebrew diagnostic port"
  ],
  "upstream_name": "Atari Jaguar 240p Test Suite",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

The project identifies itself as the Atari Jaguar 240p Test Suite, a bare-metal port of Artemio Urbina's diagnostic suite with Jaguar-specific tests and tagged pre-1.0 releases.
- https://github.com/JoeMatt/atari_jaguar_240p_test_suite/blob/1649ab0f539fbcb81c95eff1054b0264d41557c7/README.md

### Classification (reviewed)

This is substantial original homebrew porting work, not reverse engineering: it implements calibration patterns, lag/audio tests and Jaguar hardware probes as native console software.
- https://github.com/JoeMatt/atari_jaguar_240p_test_suite/blob/1649ab0f539fbcb81c95eff1054b0264d41557c7/README.md

### Source CPU (not-applicable)

The port is derived from the high-level 240p Test Suite project rather than recovery of an original machine-code binary, so no predecessor CPU is assigned.
- https://github.com/JoeMatt/atari_jaguar_240p_test_suite/blob/1649ab0f539fbcb81c95eff1054b0264d41557c7/README.md

### Target CPU (reviewed)

The build documentation explicitly requires m68k-atari-mint cross tools and produces Atari Jaguar ROM formats, establishing the native m68k output architecture without asserting a minimum runtime CPU.
- https://github.com/JoeMatt/atari_jaguar_240p_test_suite/blob/1649ab0f539fbcb81c95eff1054b0264d41557c7/README.md

### Build (reviewed)

The README documents Docker and native toolchain paths, multiple ROM formats, releases and emulator smoke tests. No build, ROM execution or real-hardware test was independently performed, so boolean build/run flags remain unknown.
- https://github.com/JoeMatt/atari_jaguar_240p_test_suite/blob/1649ab0f539fbcb81c95eff1054b0264d41557c7/README.md

### Runtime profiles (no-evidence-found)

Native Atari Jaguar execution and cartridge/emulator loading routes are documented, but no variant-specific minimum CPU/RAM profile beyond the target console was established.
- https://github.com/JoeMatt/atari_jaguar_240p_test_suite/blob/1649ab0f539fbcb81c95eff1054b0264d41557c7/README.md

### AI (no-evidence-found)

The repository contains agent-configuration files, but those are not contribution evidence; the reviewed README and primary project material do not explicitly attribute implementation to an AI tool, so usage remains unknown.
- https://github.com/JoeMatt/atari_jaguar_240p_test_suite/tree/1649ab0f539fbcb81c95eff1054b0264d41557c7

### Relationships (reviewed)

The README identifies JoeMatt's project as an active fork of BitJag's original Jaguar port and as a port of Artemio Urbina's broader 240p Test Suite. BitJag and ArtemioUrbina Jaguar repositories are recorded as lineage duplicates, not independent projects.
- https://github.com/JoeMatt/atari_jaguar_240p_test_suite/blob/1649ab0f539fbcb81c95eff1054b0264d41557c7/README.md
- https://github.com/BitJag/atari_jaguar_240p_test_suite/blob/a65a646df41e2ca2f343d864b749875a3674b1ec/README.md

## JagLBA — Little Big Adventure source port for Atari Jaguar

Project ID: jaglba-atari-jaguar-port · Overall audit: reviewed

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
  "display_title": "JagLBA — Little Big Adventure source port for Atari Jaguar",
  "id": "jaglba-atari-jaguar-port",
  "last_activity": "2026-10-02",
  "last_checked": "2026-10-27",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "m68k assembly",
    "Jaguar GPU/DSP assembly",
    "Python",
    "Batch"
  ],
  "record_class": "subject",
  "repo": "https://github.com/vs-sr-dev/jag-lba",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Work in progress; first room and scripts run in BigPEmu, earlier renderer tested on real Jaguar; far from playable",
  "subjects": [
    "Little Big Adventure"
  ],
  "tags": [
    "Atari Jaguar",
    "Little Big Adventure",
    "source port",
    "work in progress"
  ],
  "target_cpu": [
    "m68k",
    "Jaguar GPU/DSP"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Atari Jaguar"
  ],
  "techniques": [
    "GPL source transplant",
    "Jaguar GPU rendering",
    "Jaguar DSP audio synthesis",
    "cartridge asset packing"
  ],
  "title": "JagLBA",
  "tool_kinds": [],
  "types": [
    "Source-derived native port"
  ],
  "upstream_name": "JagLBA",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

JagLBA identifies itself as a 6 MB Atari Jaguar cartridge port of Little Big Adventure, built from the released GPL engine source and requiring user-supplied game data.
- https://github.com/vs-sr-dev/jag-lba/blob/c8708485ca8baef78a1f1a05743008c80bc9534d/README.md

### Classification (reviewed)

This is a source-derived native port, not a binary-derived reconstruction. The current project is explicitly far from playable; the first room, scripts and interaction run in BigPEmu, while an earlier renderer-only build was tested on real hardware.
- https://github.com/vs-sr-dev/jag-lba/blob/c8708485ca8baef78a1f1a05743008c80bc9534d/README.md

### Source CPU (not-applicable)

The input is a released C engine lineage with formerly x86 assembly modules translated to C, not recovery from a specific original executable, so an original binary CPU is not assigned.
- https://github.com/vs-sr-dev/jag-lba/blob/c8708485ca8baef78a1f1a05743008c80bc9534d/engine_c/fork/PROVENANCE.md

### Target CPU (reviewed)

The README explicitly says the engine runs on the Jaguar's 68000 and describes GPU rendering plus DSP audio work; the repository contains 68000 boot/interrupt code and GPU/DSP kernels.
- https://github.com/vs-sr-dev/jag-lba/blob/c8708485ca8baef78a1f1a05743008c80bc9534d/README.md

### Build (reviewed)

The Windows build path requires owned LBA data, Python, Docker with a documented m68k toolchain image, RMAC and Jaguar SDK headers, and writes separate emulator and hardware ROMs. No build or execution was independently performed.
- https://github.com/vs-sr-dev/jag-lba/blob/c8708485ca8baef78a1f1a05743008c80bc9534d/README.md

### Runtime profiles (no-evidence-found)

The documentation establishes Atari Jaguar and BigPEmu execution paths and a 6 MB cartridge image, but it does not provide a variant minimum CPU/RAM profile beyond the console target.
- https://github.com/vs-sr-dev/jag-lba/blob/c8708485ca8baef78a1f1a05743008c80bc9534d/README.md

### AI (no-evidence-found)

No explicit development-AI attribution was established in the reviewed README and provenance document; absence is recorded as unknown rather than non-use.
- https://github.com/vs-sr-dev/jag-lba/blob/c8708485ca8baef78a1f1a05743008c80bc9534d/README.md
- https://github.com/vs-sr-dev/jag-lba/blob/c8708485ca8baef78a1f1a05743008c80bc9534d/engine_c/fork/PROVENANCE.md

### Relationships (reviewed)

The provenance file records a direct chain from lba1-classic-community through PSX-LBA and DS-LBA, with selected HS-LBA fixes. These are source-port predecessors, not evidence of Jaguar binary reverse engineering.
- https://github.com/vs-sr-dev/jag-lba/blob/c8708485ca8baef78a1f1a05743008c80bc9534d/engine_c/fork/PROVENANCE.md

## Jaguar Cartridge Reader — 16-bit dump and bus-analysis firmware

Project ID: tolbat-jaguar-cartridge-reader · Overall audit: reviewed

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
  "display_title": "Jaguar Cartridge Reader — 16-bit dump and bus-analysis firmware",
  "id": "tolbat-jaguar-cartridge-reader",
  "last_activity": "2026-08-24",
  "last_checked": "2026-10-27",
  "re_started": null,
  "reconstructed_languages": [
    "Arduino C++"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/Tolbat/jaguarcartreader",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [
    "Atari Jaguar cartridge ROM and bus data"
  ],
  "source_platforms": [
    "Atari Jaguar"
  ],
  "status": "Primary firmware and documentation reviewed; independent hardware execution not performed",
  "subjects": [],
  "tags": [
    "Atari Jaguar",
    "cartridge preservation",
    "firmware"
  ],
  "target_cpu": [],
  "target_kinds": [],
  "target_platforms": [],
  "techniques": [
    "non-destructive cartridge probing",
    "data-bus characterization",
    "big-endian ROM dumping",
    "repeated-read stability checks"
  ],
  "title": "jaguarcartreader",
  "tool_kinds": [
    "rom-tool",
    "binary-analysis"
  ],
  "types": [
    "Cartridge dumping and analysis firmware"
  ],
  "upstream_name": "jaguarcartreader",
  "work_kinds": [
    "binary-analysis"
  ]
}
```

### Identity (reviewed)

Tolbat's jaguarcartreader is a modified standalone Atari Jaguar cartridge-reader firmware with 4 MB and 6 MB 16-bit dump modes and a read-only cartridge analyzer.
- https://github.com/Tolbat/jaguarcartreader/blob/809541c8dd76e81df1fe3ff424188d4fd879288a/README.md

### Classification (reviewed)

This qualifies as preservation and binary-analysis tooling: it measures cartridge bus behavior, samples address ranges and output-enable states, checks read stability, and writes standard J64 images. It is not a reverse-engineered game or a general hardware project record.
- https://github.com/Tolbat/jaguarcartreader/blob/809541c8dd76e81df1fe3ff424188d4fd879288a/README.md
- https://github.com/Tolbat/jaguarcartreader/blob/809541c8dd76e81df1fe3ff424188d4fd879288a/Cart_Reader/JAG/jag.ino

### Source CPU (not-applicable)

The tool dumps cartridge ROM bytes and characterizes the physical data-bus layout without interpreting a specific game's executable CPU instructions, so no original CPU is assigned.
- https://github.com/Tolbat/jaguarcartreader/blob/809541c8dd76e81df1fe3ff424188d4fd879288a/README.md

### Target CPU (no-evidence-found)

The reviewed fork documents Arduino IDE and library dependencies but does not explicitly identify a processor model in its own primary material; no firmware CPU is inferred from the hardware family.
- https://github.com/Tolbat/jaguarcartreader/blob/809541c8dd76e81df1fe3ff424188d4fd879288a/README.md
- https://github.com/Tolbat/jaguarcartreader/blob/809541c8dd76e81df1fe3ff424188d4fd879288a/Cart_Reader/JAG/jag.ino

### Build (reviewed)

The README lists Arduino IDE 1.8.19 and pinned display/storage libraries, and the repository contains the Arduino firmware. The firmware was not compiled, flashed or run on reader hardware in this pass.
- https://github.com/Tolbat/jaguarcartreader/blob/809541c8dd76e81df1fe3ff424188d4fd879288a/README.md
- https://github.com/Tolbat/jaguarcartreader/blob/809541c8dd76e81df1fe3ff424188d4fd879288a/Cart_Reader/JAG/jag.ino

### Runtime profiles (no-evidence-found)

The reviewed fork does not provide a complete minimum hardware profile for the standalone reader, so no CPU/RAM/chipset runtime profile is recorded.
- https://github.com/Tolbat/jaguarcartreader/blob/809541c8dd76e81df1fe3ff424188d4fd879288a/README.md

### AI (no-evidence-found)

No explicit development-AI attribution was found in the reviewed README or firmware header; usage remains unknown.
- https://github.com/Tolbat/jaguarcartreader/blob/809541c8dd76e81df1fe3ff424188d4fd879288a/README.md
- https://github.com/Tolbat/jaguarcartreader/blob/809541c8dd76e81df1fe3ff424188d4fd879288a/Cart_Reader/JAG/jag.ino

### Relationships (reviewed)

The README identifies Tolbat's work as a modification of PsychoFox11/GrumpyGopher/sakman55 reader lineage. The OSCR User Group fork carries the same analyzer and 16-bit modes with build/release automation, so it is recorded as a duplicate successor rather than a separate project.
- https://github.com/Tolbat/jaguarcartreader/blob/809541c8dd76e81df1fe3ff424188d4fd879288a/README.md
- https://github.com/oscrusergroup/firmware-jaguar-standalone/blob/debf9a3cadc281f82efbc1a804b53c0b8e079550/README.md

## Sources

```json
[
  {
    "first_indexed": "2026-10-27",
    "id": "search-2026-10-27-vectrex-disassembly",
    "kind": "github-repository-search",
    "last_reviewed": "2026-10-27",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Fresh-search query `vectrex disassembly`; the repository search returned no candidates in this pass.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/search?q=vectrex+disassembly&type=repositories"
  },
  {
    "first_indexed": "2026-10-27",
    "id": "search-2026-10-27-x68000-disassembly",
    "kind": "github-repository-search",
    "last_reviewed": "2026-10-27",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Fresh-search query `x68000 disassembly`; the sole reviewed hit, vampirefrog/x68kd11s, was already promoted as x68kd11s-system-disassemblies.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/search?q=x68000+disassembly&type=repositories"
  },
  {
    "first_indexed": "2026-10-27",
    "id": "search-2026-10-27-trs80-disassembly",
    "kind": "github-repository-search",
    "last_reviewed": "2026-10-27",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Fresh-search query `trs-80 disassembly`; reviewed andyv/level1, eriktier/RomT102Disassembly, gummieinars/trsdos, mccabet/RomT102Disassembly and pockemul/RomT102Disassembly, all already promoted, excluded or recorded as duplicates.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/search?q=trs-80+disassembly&type=repositories"
  },
  {
    "first_indexed": "2026-10-27",
    "id": "search-2026-10-27-atari-jaguar-homebrew",
    "kind": "github-repository-search",
    "last_reviewed": "2026-10-27",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Fresh-search query `atari jaguar homebrew`; six candidates were screened and reviewed, producing three promoted lineages plus duplicate-fork decisions.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/search?q=atari+jaguar+homebrew&type=repositories"
  },
  {
    "first_indexed": "2026-10-27",
    "id": "github-joematt-atari-jaguar-240p-test-suite",
    "kind": "github-repository",
    "last_reviewed": "2026-10-27",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Active Atari Jaguar continuation of BitJag's native 240p Test Suite port, with substantial additional diagnostics and release/build documentation.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/JoeMatt/atari_jaguar_240p_test_suite"
  },
  {
    "first_indexed": "2026-10-27",
    "id": "github-bitjag-atari-jaguar-240p-test-suite",
    "kind": "github-repository",
    "last_reviewed": "2026-10-27",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Original Atari Jaguar port lineage now represented by the materially extended JoeMatt continuation.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/BitJag/atari_jaguar_240p_test_suite"
  },
  {
    "first_indexed": "2026-10-27",
    "id": "github-artemiourbina-atari-jaguar-240p-test-suite",
    "kind": "github-repository",
    "last_reviewed": "2026-10-27",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Unmodified fork of the BitJag Atari Jaguar port at the same reviewed commit; recorded as a duplicate lineage node.",
    "review_state": "exhausted",
    "source": "https://github.com/ArtemioUrbina/atari_jaguar_240p_test_suite"
  },
  {
    "first_indexed": "2026-10-27",
    "id": "github-vs-sr-dev-jag-lba",
    "kind": "github-repository",
    "last_reviewed": "2026-10-27",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Source-derived Little Big Adventure port for Atari Jaguar, with documented engine provenance and native 68000/GPU/DSP implementation.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/vs-sr-dev/jag-lba"
  },
  {
    "first_indexed": "2026-10-27",
    "id": "github-tolbat-jaguarcartreader",
    "kind": "github-repository",
    "last_reviewed": "2026-10-27",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Atari Jaguar cartridge-dumping firmware with non-destructive bus-layout analysis and 16-bit cartridge modes.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/Tolbat/jaguarcartreader"
  },
  {
    "first_indexed": "2026-10-27",
    "id": "github-oscrusergroup-firmware-jaguar-standalone",
    "kind": "github-repository",
    "last_reviewed": "2026-10-27",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Downstream fork of Tolbat's Jaguar cartridge reader; reviewed changes are build/release automation rather than a separate software-archaeology project.",
    "review_state": "exhausted",
    "source": "https://github.com/oscrusergroup/firmware-jaguar-standalone"
  }
]
```

## Source updates

```json
[
  {
    "id": "github-bretthallen-amstrad-cpc",
    "last_reviewed": "2026-10-27",
    "reason": "CPC project collection; Laserwarp and the Claude-assisted Typer Inner Checker are promoted, while root hardware projects and typed-listing material were screened without being misclassified as reverse-engineered software. Broader CPC graph work remains.",
    "review_state": "partial"
  }
]
```

## Task updates

```json
[
  {
    "id": "task-continue-discovery-through-cpc-analyser-users-cpcwiki-cpcrulez-reference",
    "last_reviewed": "2026-10-27",
    "notes_append": "Reviewed BrettHallen/Amstrad-CPC root and nested Typer Inner Checker; promoted the listing-analysis tool, retained hardware-only entries as discovery context, and left the wider CPCWiki/CPCRulez/analyser-user graph open.",
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
      "https://github.com/BrettHallen/Amstrad-CPC/blob/5570544eeb983c5a58893272335011cf44615521/README.md",
      "https://github.com/BrettHallen/Amstrad-CPC/blob/5570544eeb983c5a58893272335011cf44615521/Typer-Inner-Checker/Claude-discussion.txt",
      "https://github.com/BrettHallen/Amstrad-CPC/blob/5570544eeb983c5a58893272335011cf44615521/Typer-Inner-Checker/Typer-Inner-Checker.html"
    ],
    "id": "promote-typer-inner-checker",
    "project_ids": [
      "typer-inner-checker-locomotive-basic"
    ],
    "reason": "A concrete self-contained Locomotive BASIC listing-analysis tool with keyword recognition, syntax checks, jump-target validation and BAS load/save support; the preserved transcript explicitly documents Claude-assisted development.",
    "source_ids": [
      "github-bretthallen-amstrad-cpc"
    ],
    "title": "Typer Inner Checker",
    "url": "https://github.com/BrettHallen/Amstrad-CPC/tree/main/Typer-Inner-Checker"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/JoeMatt/atari_jaguar_240p_test_suite/blob/1649ab0f539fbcb81c95eff1054b0264d41557c7/README.md"
    ],
    "id": "promote-atari-jaguar-240p-test-suite",
    "project_ids": [
      "atari-jaguar-240p-test-suite-port"
    ],
    "reason": "A substantial native Jaguar diagnostic port and active continuation of BitJag's original port, with added calibration patterns, hardware tests, releases and reproducible build paths.",
    "source_ids": [
      "search-2026-10-27-atari-jaguar-homebrew",
      "github-joematt-atari-jaguar-240p-test-suite"
    ],
    "title": "Atari Jaguar 240p Test Suite",
    "url": "https://github.com/JoeMatt/atari_jaguar_240p_test_suite"
  },
  {
    "decision": "duplicate",
    "evidence_urls": [
      "https://github.com/BitJag/atari_jaguar_240p_test_suite/blob/a65a646df41e2ca2f343d864b749875a3674b1ec/README.md",
      "https://github.com/JoeMatt/atari_jaguar_240p_test_suite/blob/1649ab0f539fbcb81c95eff1054b0264d41557c7/README.md"
    ],
    "id": "duplicate-bitjag-atari-jaguar-240p-test-suite",
    "project_ids": [
      "atari-jaguar-240p-test-suite-port"
    ],
    "reason": "This is the original Jaguar port lineage; the catalogue record uses JoeMatt's explicitly identified active fork because it materially extends the same project rather than representing an independent title.",
    "source_ids": [
      "search-2026-10-27-atari-jaguar-homebrew",
      "github-bitjag-atari-jaguar-240p-test-suite"
    ],
    "title": "BitJag Atari Jaguar 240p Test Suite",
    "url": "https://github.com/BitJag/atari_jaguar_240p_test_suite"
  },
  {
    "decision": "duplicate",
    "evidence_urls": [
      "https://github.com/ArtemioUrbina/atari_jaguar_240p_test_suite/blob/a65a646df41e2ca2f343d864b749875a3674b1ec/README.md",
      "https://github.com/BitJag/atari_jaguar_240p_test_suite/commit/a65a646df41e2ca2f343d864b749875a3674b1ec"
    ],
    "id": "duplicate-artemiourbina-atari-jaguar-240p-test-suite",
    "project_ids": [
      "atari-jaguar-240p-test-suite-port"
    ],
    "reason": "GitHub identifies this as a BitJag fork and its reviewed head is the same BitJag commit; it does not establish a separate Jaguar implementation.",
    "source_ids": [
      "search-2026-10-27-atari-jaguar-homebrew",
      "github-artemiourbina-atari-jaguar-240p-test-suite"
    ],
    "title": "ArtemioUrbina Atari Jaguar 240p Test Suite fork",
    "url": "https://github.com/ArtemioUrbina/atari_jaguar_240p_test_suite"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/vs-sr-dev/jag-lba/blob/c8708485ca8baef78a1f1a05743008c80bc9534d/README.md",
      "https://github.com/vs-sr-dev/jag-lba/blob/c8708485ca8baef78a1f1a05743008c80bc9534d/engine_c/fork/PROVENANCE.md"
    ],
    "id": "promote-jag-lba-atari-jaguar-port",
    "project_ids": [
      "jaglba-atari-jaguar-port"
    ],
    "reason": "A substantial source-derived native Atari Jaguar port of Little Big Adventure with documented GPL engine lineage, 68000 execution, Jaguar GPU/DSP rendering work and an explicit work-in-progress boundary.",
    "source_ids": [
      "search-2026-10-27-atari-jaguar-homebrew",
      "github-vs-sr-dev-jag-lba"
    ],
    "title": "JagLBA",
    "url": "https://github.com/vs-sr-dev/jag-lba"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/Tolbat/jaguarcartreader/blob/809541c8dd76e81df1fe3ff424188d4fd879288a/README.md",
      "https://github.com/Tolbat/jaguarcartreader/blob/809541c8dd76e81df1fe3ff424188d4fd879288a/Cart_Reader/JAG/jag.ino"
    ],
    "id": "promote-tolbat-jaguar-cartridge-reader",
    "project_ids": [
      "tolbat-jaguar-cartridge-reader"
    ],
    "reason": "Preservation firmware that dumps Jaguar cartridges and adds a non-destructive cartridge-bus analyzer plus evidence-based 16-bit read modes for newer cartridge layouts.",
    "source_ids": [
      "search-2026-10-27-atari-jaguar-homebrew",
      "github-tolbat-jaguarcartreader"
    ],
    "title": "Jaguar Cartridge Reader",
    "url": "https://github.com/Tolbat/jaguarcartreader"
  },
  {
    "decision": "duplicate",
    "evidence_urls": [
      "https://github.com/oscrusergroup/firmware-jaguar-standalone/blob/debf9a3cadc281f82efbc1a804b53c0b8e079550/README.md",
      "https://github.com/Tolbat/jaguarcartreader/blob/809541c8dd76e81df1fe3ff424188d4fd879288a/README.md"
    ],
    "id": "duplicate-oscrusergroup-jaguar-reader-firmware",
    "project_ids": [
      "tolbat-jaguar-cartridge-reader"
    ],
    "reason": "GitHub identifies this as a downstream fork of Tolbat's reader; the reviewed README carries the same analyzer/16-bit functionality and adds routine build/release automation rather than a distinct preservation project.",
    "source_ids": [
      "search-2026-10-27-atari-jaguar-homebrew",
      "github-oscrusergroup-firmware-jaguar-standalone"
    ],
    "title": "OSCR Jaguar standalone firmware",
    "url": "https://github.com/oscrusergroup/firmware-jaguar-standalone"
  }
]
```

## Research event notes

CPU audit queue returned zero unresolved source/target CPU areas. Fresh repository searches were: `vectrex disassembly` (no results), `x68000 disassembly` (x68kd11s already promoted), `trs-80 disassembly` (five results already promoted, excluded or duplicate), and `atari jaguar homebrew` (six candidates reviewed: three promoted lineages and three duplicate forks). The BrettHallen/Amstrad-CPC root was revisited from the older queue; Typer Inner Checker was promoted, hardware-only entries were not treated as software projects, and the broader CPC source task remains open.
