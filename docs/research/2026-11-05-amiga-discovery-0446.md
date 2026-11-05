# Amiga and Atari ST game and tool discovery

Screen Amiga and Atari ST discovery leads; add an early Amiga game investigation, two development tools and two related game reconstructions.

Date: 2026-11-05 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- retroshoppt-lotus2recomp / Target CPU (no-evidence-found): No exact target CPU minimum established.
- retroshoppt-lotus2recomp / Runtime profiles (no-evidence-found): No independently verified complete runtime profile.
- retroshoppt-lotus2recomp / AI (no-evidence-found): No actual AI contribution established from inspected evidence; absence does not prove non-use.
- benbaker76-amigascope / Target CPU (no-evidence-found): No exact target CPU minimum established.
- benbaker76-amigascope / Runtime profiles (no-evidence-found): No independently verified complete runtime profile.
- benbaker76-amigascope / AI (no-evidence-found): No actual AI contribution established from inspected evidence; absence does not prove non-use.
- alphapixel-extract-adf-python / Source CPU (no-evidence-found): No specific source CPU is asserted.
- alphapixel-extract-adf-python / Target CPU (no-evidence-found): No exact target CPU minimum established.
- alphapixel-extract-adf-python / Runtime profiles (no-evidence-found): No independently verified complete runtime profile.
- coolbutuseless-anotherworld / Source CPU (no-evidence-found): No specific source CPU is asserted.
- coolbutuseless-anotherworld / Target CPU (no-evidence-found): No exact target CPU minimum established.
- coolbutuseless-anotherworld / Runtime profiles (no-evidence-found): No independently verified complete runtime profile.
- coolbutuseless-anotherworld / AI (no-evidence-found): No actual AI contribution established from inspected evidence; absence does not prove non-use.
- mbialkowski-lazarus-revibed / Target CPU (no-evidence-found): No exact target CPU minimum established.
- mbialkowski-lazarus-revibed / Runtime profiles (no-evidence-found): No independently verified complete runtime profile.

## Lotus Turbo Challenge II — early Amiga disk investigation

Project ID: retroshoppt-lotus2recomp · Overall audit: partial

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
  "display_title": "Lotus Turbo Challenge II — early Amiga disk investigation",
  "id": "retroshoppt-lotus2recomp",
  "last_activity": null,
  "last_checked": "2026-11-05",
  "re_started": null,
  "reconstructed_languages": [
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/RetroShopPT/Lotus2Recomp",
  "runtime_profiles": [],
  "source_cpu": [
    "68000"
  ],
  "source_language": [],
  "source_platforms": [
    "Amiga"
  ],
  "status": "Source and research inspected; no independent build or execution",
  "subjects": [
    "Lotus Turbo Challenge II"
  ],
  "tags": [],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [],
  "techniques": [],
  "title": "Lotus Turbo Challenge II — early Amiga disk investigation",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "Lotus2Recomp",
  "work_kinds": [
    "data-format-analysis"
  ]
}
```

### Identity (reviewed)

Lotus Turbo Challenge II — early Amiga disk investigation. Pinned primary material reviewed.
- https://github.com/RetroShopPT/Lotus2Recomp/blob/805479d364020e34bca0f7db6a362c46acfe62b3/README.md
- https://github.com/RetroShopPT/Lotus2Recomp/blob/805479d364020e34bca0f7db6a362c46acfe62b3/inspect_adf.py

### Classification (reviewed)

Early disk and boot-loader research: read-only Python inventory checks disk hashes, bootblock checksums, root block and packing signatures; README records first loader read. The game remains packed and neither recompiler nor playable port exists.
- https://github.com/RetroShopPT/Lotus2Recomp/blob/805479d364020e34bca0f7db6a362c46acfe62b3/README.md
- https://github.com/RetroShopPT/Lotus2Recomp/blob/805479d364020e34bca0f7db6a362c46acfe62b3/inspect_adf.py

### Source CPU (reviewed)

Source CPU is listed only where the platform and source evidence establish it.
- https://github.com/RetroShopPT/Lotus2Recomp/blob/805479d364020e34bca0f7db6a362c46acfe62b3/README.md
- https://github.com/RetroShopPT/Lotus2Recomp/blob/805479d364020e34bca0f7db6a362c46acfe62b3/inspect_adf.py

### Target CPU (no-evidence-found)

No exact target CPU minimum established.
- https://github.com/RetroShopPT/Lotus2Recomp/blob/805479d364020e34bca0f7db6a362c46acfe62b3/README.md
- https://github.com/RetroShopPT/Lotus2Recomp/blob/805479d364020e34bca0f7db6a362c46acfe62b3/inspect_adf.py

### Build (reviewed)

Source and author build instructions inspected. No independent build, execution, gameplay or byte comparison.
- https://github.com/RetroShopPT/Lotus2Recomp/blob/805479d364020e34bca0f7db6a362c46acfe62b3/README.md
- https://github.com/RetroShopPT/Lotus2Recomp/blob/805479d364020e34bca0f7db6a362c46acfe62b3/inspect_adf.py

### Runtime profiles (no-evidence-found)

No independently verified complete runtime profile.
- https://github.com/RetroShopPT/Lotus2Recomp/blob/805479d364020e34bca0f7db6a362c46acfe62b3/README.md
- https://github.com/RetroShopPT/Lotus2Recomp/blob/805479d364020e34bca0f7db6a362c46acfe62b3/inspect_adf.py

### AI (no-evidence-found)

No actual AI contribution established from inspected evidence; absence does not prove non-use.
- https://github.com/RetroShopPT/Lotus2Recomp/blob/805479d364020e34bca0f7db6a362c46acfe62b3/README.md
- https://github.com/RetroShopPT/Lotus2Recomp/blob/805479d364020e34bca0f7db6a362c46acfe62b3/inspect_adf.py

### Relationships (reviewed)

Separate investigation of the same game as CrownParkComputing/Lotus2-Native and jonathanopalise/lotus2-ste; independent lineage not established.
- https://github.com/RetroShopPT/Lotus2Recomp/blob/805479d364020e34bca0f7db6a362c46acfe62b3/README.md
- https://github.com/RetroShopPT/Lotus2Recomp/blob/805479d364020e34bca0f7db6a362c46acfe62b3/inspect_adf.py

## AmigaScope — headless Amiga debugging and profiling

Project ID: benbaker76-amigascope · Overall audit: partial

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
  "display_title": "AmigaScope — headless Amiga debugging and profiling",
  "id": "benbaker76-amigascope",
  "last_activity": null,
  "last_checked": "2026-11-05",
  "re_started": null,
  "reconstructed_languages": [
    "Python"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/benbaker76/AmigaScope",
  "runtime_profiles": [],
  "source_cpu": [
    "68000"
  ],
  "source_language": [],
  "source_platforms": [
    "Amiga"
  ],
  "status": "Source and research inspected; no independent build or execution",
  "subjects": [
    "Amiga software"
  ],
  "tags": [],
  "target_cpu": [],
  "target_kinds": [],
  "target_platforms": [
    "Linux"
  ],
  "techniques": [],
  "title": "AmigaScope — headless Amiga debugging and profiling",
  "tool_kinds": [
    "debugger"
  ],
  "types": [
    "tool"
  ],
  "upstream_name": "AmigaScope",
  "work_kinds": [
    "binary-analysis"
  ]
}
```

### Identity (reviewed)

AmigaScope — headless Amiga debugging and profiling. Pinned primary material reviewed.
- https://github.com/benbaker76/AmigaScope/blob/8629fadc925475250a553fb26823a219e53bde3d/README.md
- https://github.com/benbaker76/AmigaScope/blob/8629fadc925475250a553fb26823a219e53bde3d/gdb_proxy.py

### Classification (reviewed)

Headless GDB proxy and MCP interface for FS-UAE and native SDL builds; includes profiling and Amiga copper and display inspection utilities. Author describes emulator and GDB dependencies; inspected proxy source, but did not run the harness.
- https://github.com/benbaker76/AmigaScope/blob/8629fadc925475250a553fb26823a219e53bde3d/README.md
- https://github.com/benbaker76/AmigaScope/blob/8629fadc925475250a553fb26823a219e53bde3d/gdb_proxy.py

### Source CPU (reviewed)

Source CPU is listed only where the platform and source evidence establish it.
- https://github.com/benbaker76/AmigaScope/blob/8629fadc925475250a553fb26823a219e53bde3d/README.md
- https://github.com/benbaker76/AmigaScope/blob/8629fadc925475250a553fb26823a219e53bde3d/gdb_proxy.py

### Target CPU (no-evidence-found)

No exact target CPU minimum established.
- https://github.com/benbaker76/AmigaScope/blob/8629fadc925475250a553fb26823a219e53bde3d/README.md
- https://github.com/benbaker76/AmigaScope/blob/8629fadc925475250a553fb26823a219e53bde3d/gdb_proxy.py

### Build (reviewed)

Source and author build instructions inspected. No independent build, execution, gameplay or byte comparison.
- https://github.com/benbaker76/AmigaScope/blob/8629fadc925475250a553fb26823a219e53bde3d/README.md
- https://github.com/benbaker76/AmigaScope/blob/8629fadc925475250a553fb26823a219e53bde3d/gdb_proxy.py

### Runtime profiles (no-evidence-found)

No independently verified complete runtime profile.
- https://github.com/benbaker76/AmigaScope/blob/8629fadc925475250a553fb26823a219e53bde3d/README.md
- https://github.com/benbaker76/AmigaScope/blob/8629fadc925475250a553fb26823a219e53bde3d/gdb_proxy.py

### AI (no-evidence-found)

No actual AI contribution established from inspected evidence; absence does not prove non-use.
- https://github.com/benbaker76/AmigaScope/blob/8629fadc925475250a553fb26823a219e53bde3d/README.md
- https://github.com/benbaker76/AmigaScope/blob/8629fadc925475250a553fb26823a219e53bde3d/gdb_proxy.py

### Relationships (reviewed)

Distinct repository; related projects and similar subjects are not presumed equivalent.
- https://github.com/benbaker76/AmigaScope/blob/8629fadc925475250a553fb26823a219e53bde3d/README.md
- https://github.com/benbaker76/AmigaScope/blob/8629fadc925475250a553fb26823a219e53bde3d/gdb_proxy.py

## Extract-ADF — Python OFS recovery port

Project ID: alphapixel-extract-adf-python · Overall audit: partial

### Typed catalogue values

```json
{
  "ai": {
    "evidence": [
      "Explicit attribution to Codex: https://github.com/AlphaPixel/Extract-ADF-Python/blob/bb4fbda0a54b99ac96bcb769c4c77a8025eba132/README.md"
    ],
    "tools": [
      "Codex"
    ],
    "usage": true
  },
  "build": {
    "byte_exact": null,
    "compilable": null,
    "playable": null,
    "runnable": null
  },
  "display_title": "Extract-ADF — Python OFS recovery port",
  "id": "alphapixel-extract-adf-python",
  "last_activity": null,
  "last_checked": "2026-11-05",
  "re_started": null,
  "reconstructed_languages": [
    "Python"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/AlphaPixel/Extract-ADF-Python",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [
    "Amiga"
  ],
  "status": "Source and research inspected; no independent build or execution",
  "subjects": [
    "Amiga OFS disk images"
  ],
  "tags": [],
  "target_cpu": [],
  "target_kinds": [],
  "target_platforms": [],
  "techniques": [],
  "title": "Extract-ADF — Python OFS recovery port",
  "tool_kinds": [
    "disk-filesystem-tool"
  ],
  "types": [
    "tool"
  ],
  "upstream_name": "Extract-ADF-Python",
  "work_kinds": [
    "data-format-analysis"
  ]
}
```

### Identity (reviewed)

Extract-ADF — Python OFS recovery port. Pinned primary material reviewed.
- https://github.com/AlphaPixel/Extract-ADF-Python/blob/bb4fbda0a54b99ac96bcb769c4c77a8025eba132/README.md
- https://github.com/AlphaPixel/Extract-ADF-Python/blob/bb4fbda0a54b99ac96bcb769c4c77a8025eba132/extract-adf.py

### Classification (reviewed)

Python port of mist64/extract-adf for extracting Amiga OFS files, including some damaged images. README says FFS is unsupported and DMS is recognized but not implemented; author reports fixture tests, not independently repeated.
- https://github.com/AlphaPixel/Extract-ADF-Python/blob/bb4fbda0a54b99ac96bcb769c4c77a8025eba132/README.md
- https://github.com/AlphaPixel/Extract-ADF-Python/blob/bb4fbda0a54b99ac96bcb769c4c77a8025eba132/extract-adf.py

### Source CPU (no-evidence-found)

No specific source CPU is asserted.
- https://github.com/AlphaPixel/Extract-ADF-Python/blob/bb4fbda0a54b99ac96bcb769c4c77a8025eba132/README.md
- https://github.com/AlphaPixel/Extract-ADF-Python/blob/bb4fbda0a54b99ac96bcb769c4c77a8025eba132/extract-adf.py

### Target CPU (no-evidence-found)

No exact target CPU minimum established.
- https://github.com/AlphaPixel/Extract-ADF-Python/blob/bb4fbda0a54b99ac96bcb769c4c77a8025eba132/README.md
- https://github.com/AlphaPixel/Extract-ADF-Python/blob/bb4fbda0a54b99ac96bcb769c4c77a8025eba132/extract-adf.py

### Build (reviewed)

Source and author build instructions inspected. No independent build, execution, gameplay or byte comparison.
- https://github.com/AlphaPixel/Extract-ADF-Python/blob/bb4fbda0a54b99ac96bcb769c4c77a8025eba132/README.md
- https://github.com/AlphaPixel/Extract-ADF-Python/blob/bb4fbda0a54b99ac96bcb769c4c77a8025eba132/extract-adf.py

### Runtime profiles (no-evidence-found)

No independently verified complete runtime profile.
- https://github.com/AlphaPixel/Extract-ADF-Python/blob/bb4fbda0a54b99ac96bcb769c4c77a8025eba132/README.md
- https://github.com/AlphaPixel/Extract-ADF-Python/blob/bb4fbda0a54b99ac96bcb769c4c77a8025eba132/extract-adf.py

### AI (reviewed)

Actual AI assistance explicitly described in cited source.
- https://github.com/AlphaPixel/Extract-ADF-Python/blob/bb4fbda0a54b99ac96bcb769c4c77a8025eba132/README.md
- https://github.com/AlphaPixel/Extract-ADF-Python/blob/bb4fbda0a54b99ac96bcb769c4c77a8025eba132/extract-adf.py

### Relationships (reviewed)

Python port of mist64/extract-adf, explicitly credited upstream.
- https://github.com/AlphaPixel/Extract-ADF-Python/blob/bb4fbda0a54b99ac96bcb769c4c77a8025eba132/README.md
- https://github.com/AlphaPixel/Extract-ADF-Python/blob/bb4fbda0a54b99ac96bcb769c4c77a8025eba132/extract-adf.py

## Another World — R bytecode interpreter

Project ID: coolbutuseless-anotherworld · Overall audit: partial

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
  "display_title": "Another World — R bytecode interpreter",
  "id": "coolbutuseless-anotherworld",
  "last_activity": null,
  "last_checked": "2026-11-05",
  "re_started": null,
  "reconstructed_languages": [
    "R"
  ],
  "record_class": "subject",
  "repo": "https://github.com/coolbutuseless/anotherworld",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Source and research inspected; no independent build or execution",
  "subjects": [
    "Another World"
  ],
  "tags": [],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [],
  "techniques": [],
  "title": "Another World — R bytecode interpreter",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "anotherworld",
  "work_kinds": [
    "reimplementation",
    "data-format-analysis"
  ]
}
```

### Identity (reviewed)

Another World — R bytecode interpreter. Pinned primary material reviewed.
- https://github.com/coolbutuseless/anotherworld/blob/3a2c77a721171eb7a8f251333ac768b352e7e244/README.md
- https://github.com/coolbutuseless/anotherworld/blob/3a2c77a721171eb7a8f251333ac768b352e7e244/game.R

### Classification (reviewed)

R implementation of the game-specific script virtual machine, derived from cyxx/another_js and Fabien Sanglard’s interpreter. This interprets the game’s own designed bytecode, not a 68000 machine emulator. README describes unfinished music, bitmap rendering and automatic level progression; bundled reference identifies an Out of This World demo, so no Amiga-specific data compatibility is claimed.
- https://github.com/coolbutuseless/anotherworld/blob/3a2c77a721171eb7a8f251333ac768b352e7e244/README.md
- https://github.com/coolbutuseless/anotherworld/blob/3a2c77a721171eb7a8f251333ac768b352e7e244/game.R

### Source CPU (no-evidence-found)

No specific source CPU is asserted.
- https://github.com/coolbutuseless/anotherworld/blob/3a2c77a721171eb7a8f251333ac768b352e7e244/README.md
- https://github.com/coolbutuseless/anotherworld/blob/3a2c77a721171eb7a8f251333ac768b352e7e244/game.R

### Target CPU (no-evidence-found)

No exact target CPU minimum established.
- https://github.com/coolbutuseless/anotherworld/blob/3a2c77a721171eb7a8f251333ac768b352e7e244/README.md
- https://github.com/coolbutuseless/anotherworld/blob/3a2c77a721171eb7a8f251333ac768b352e7e244/game.R

### Build (reviewed)

Source and author build instructions inspected. No independent build, execution, gameplay or byte comparison.
- https://github.com/coolbutuseless/anotherworld/blob/3a2c77a721171eb7a8f251333ac768b352e7e244/README.md
- https://github.com/coolbutuseless/anotherworld/blob/3a2c77a721171eb7a8f251333ac768b352e7e244/game.R

### Runtime profiles (no-evidence-found)

No independently verified complete runtime profile.
- https://github.com/coolbutuseless/anotherworld/blob/3a2c77a721171eb7a8f251333ac768b352e7e244/README.md
- https://github.com/coolbutuseless/anotherworld/blob/3a2c77a721171eb7a8f251333ac768b352e7e244/game.R

### AI (no-evidence-found)

No actual AI contribution established from inspected evidence; absence does not prove non-use.
- https://github.com/coolbutuseless/anotherworld/blob/3a2c77a721171eb7a8f251333ac768b352e7e244/README.md
- https://github.com/coolbutuseless/anotherworld/blob/3a2c77a721171eb7a8f251333ac768b352e7e244/game.R

### Relationships (reviewed)

R implementation explicitly cites cyxx/another_js, which is already tracked; distinct implementation language and runtime.
- https://github.com/coolbutuseless/anotherworld/blob/3a2c77a721171eb7a8f251333ac768b352e7e244/README.md
- https://github.com/coolbutuseless/anotherworld/blob/3a2c77a721171eb7a8f251333ac768b352e7e244/game.R

## Lazarus 97 — DOS reconstruction and Godot remake

Project ID: mbialkowski-lazarus-revibed · Overall audit: partial

### Typed catalogue values

```json
{
  "ai": {
    "evidence": [
      "Explicit attribution to Claude: https://github.com/mbialkowski/lazarus-revibed/blob/3c271f67f37e513e15983c65fc6dd9e5ee42e5df/README.md"
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
  "display_title": "Lazarus 97 — DOS reconstruction and Godot remake",
  "id": "mbialkowski-lazarus-revibed",
  "last_activity": null,
  "last_checked": "2026-11-05",
  "re_started": null,
  "reconstructed_languages": [
    "GDScript",
    "Python",
    "C"
  ],
  "record_class": "subject",
  "repo": "https://github.com/mbialkowski/lazarus-revibed",
  "runtime_profiles": [],
  "source_cpu": [
    "x86"
  ],
  "source_language": [],
  "source_platforms": [
    "DOS"
  ],
  "status": "Source and research inspected; no independent build or execution",
  "subjects": [
    "Lazarus"
  ],
  "tags": [],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Web"
  ],
  "techniques": [],
  "title": "Lazarus 97 — DOS reconstruction and Godot remake",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "lazarus-revibed",
  "work_kinds": [
    "disassembly",
    "data-format-analysis",
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Lazarus 97 — DOS reconstruction and Godot remake. Pinned primary material reviewed.
- https://github.com/mbialkowski/lazarus-revibed/blob/3c271f67f37e513e15983c65fc6dd9e5ee42e5df/README.md
- https://github.com/mbialkowski/lazarus-revibed/blob/3c271f67f37e513e15983c65fc6dd9e5ee42e5df/reference/README.md
- https://github.com/mbialkowski/lazarus-revibed/blob/3c271f67f37e513e15983c65fc6dd9e5ee42e5df/remake/scripts/sim/hero.gd

### Classification (reviewed)

Reverse engineering targets the 1997 DOS port of the 1995 Amiga game, not the Amiga executable. Repository includes annotated Ghidra pseudo-C, format analysis, extraction tools and a Godot remake. Author reports automated comparisons and a winning-route playthrough; none independently reproduced.
- https://github.com/mbialkowski/lazarus-revibed/blob/3c271f67f37e513e15983c65fc6dd9e5ee42e5df/README.md
- https://github.com/mbialkowski/lazarus-revibed/blob/3c271f67f37e513e15983c65fc6dd9e5ee42e5df/reference/README.md
- https://github.com/mbialkowski/lazarus-revibed/blob/3c271f67f37e513e15983c65fc6dd9e5ee42e5df/remake/scripts/sim/hero.gd

### Source CPU (reviewed)

Source CPU is listed only where the platform and source evidence establish it.
- https://github.com/mbialkowski/lazarus-revibed/blob/3c271f67f37e513e15983c65fc6dd9e5ee42e5df/README.md
- https://github.com/mbialkowski/lazarus-revibed/blob/3c271f67f37e513e15983c65fc6dd9e5ee42e5df/reference/README.md
- https://github.com/mbialkowski/lazarus-revibed/blob/3c271f67f37e513e15983c65fc6dd9e5ee42e5df/remake/scripts/sim/hero.gd

### Target CPU (no-evidence-found)

No exact target CPU minimum established.
- https://github.com/mbialkowski/lazarus-revibed/blob/3c271f67f37e513e15983c65fc6dd9e5ee42e5df/README.md
- https://github.com/mbialkowski/lazarus-revibed/blob/3c271f67f37e513e15983c65fc6dd9e5ee42e5df/reference/README.md
- https://github.com/mbialkowski/lazarus-revibed/blob/3c271f67f37e513e15983c65fc6dd9e5ee42e5df/remake/scripts/sim/hero.gd

### Build (reviewed)

Source and author build instructions inspected. No independent build, execution, gameplay or byte comparison.
- https://github.com/mbialkowski/lazarus-revibed/blob/3c271f67f37e513e15983c65fc6dd9e5ee42e5df/README.md
- https://github.com/mbialkowski/lazarus-revibed/blob/3c271f67f37e513e15983c65fc6dd9e5ee42e5df/reference/README.md
- https://github.com/mbialkowski/lazarus-revibed/blob/3c271f67f37e513e15983c65fc6dd9e5ee42e5df/remake/scripts/sim/hero.gd

### Runtime profiles (no-evidence-found)

No independently verified complete runtime profile.
- https://github.com/mbialkowski/lazarus-revibed/blob/3c271f67f37e513e15983c65fc6dd9e5ee42e5df/README.md
- https://github.com/mbialkowski/lazarus-revibed/blob/3c271f67f37e513e15983c65fc6dd9e5ee42e5df/reference/README.md
- https://github.com/mbialkowski/lazarus-revibed/blob/3c271f67f37e513e15983c65fc6dd9e5ee42e5df/remake/scripts/sim/hero.gd

### AI (reviewed)

Actual AI assistance explicitly described in cited source.
- https://github.com/mbialkowski/lazarus-revibed/blob/3c271f67f37e513e15983c65fc6dd9e5ee42e5df/README.md
- https://github.com/mbialkowski/lazarus-revibed/blob/3c271f67f37e513e15983c65fc6dd9e5ee42e5df/reference/README.md
- https://github.com/mbialkowski/lazarus-revibed/blob/3c271f67f37e513e15983c65fc6dd9e5ee42e5df/remake/scripts/sim/hero.gd

### Relationships (reviewed)

Distinct repository; related projects and similar subjects are not presumed equivalent.
- https://github.com/mbialkowski/lazarus-revibed/blob/3c271f67f37e513e15983c65fc6dd9e5ee42e5df/README.md
- https://github.com/mbialkowski/lazarus-revibed/blob/3c271f67f37e513e15983c65fc6dd9e5ee42e5df/reference/README.md
- https://github.com/mbialkowski/lazarus-revibed/blob/3c271f67f37e513e15983c65fc6dd9e5ee42e5df/remake/scripts/sim/hero.gd

## Pinned evidence manifest

- alphapixel-extract-adf-python-extract-adf-py: https://github.com/alphapixel/extract-adf-python/blob/bb4fbda0a54b99ac96bcb769c4c77a8025eba132/extract-adf.py (Git blob ca3fc57d69b97a7683569a523975991977b6b044)
- alphapixel-extract-adf-python-readme-md: https://github.com/alphapixel/extract-adf-python/blob/bb4fbda0a54b99ac96bcb769c4c77a8025eba132/README.md (Git blob 75f3da63d398608fd285cef2dc3e60cc0da1f5d4)
- benbaker76-amigascope-gdb-proxy-py: https://github.com/benbaker76/amigascope/blob/8629fadc925475250a553fb26823a219e53bde3d/gdb_proxy.py (Git blob 7199be10faf0fdf604f51602a8716d48f00306ba)
- benbaker76-amigascope-readme-md: https://github.com/benbaker76/amigascope/blob/8629fadc925475250a553fb26823a219e53bde3d/README.md (Git blob 705d359a984db6f9ab4252ae86ef9852038b4644)
- coolbutuseless-anotherworld-game-r: https://github.com/coolbutuseless/anotherworld/blob/3a2c77a721171eb7a8f251333ac768b352e7e244/game.R (Git blob c2030af027c064a3b93621d186f2225e35b07403)
- coolbutuseless-anotherworld-readme-md: https://github.com/coolbutuseless/anotherworld/blob/3a2c77a721171eb7a8f251333ac768b352e7e244/README.md (Git blob 5926efb2948968e8ecfa42b65f5632cc799e8325)
- mbialkowski-lazarus-revibed-readme-md: https://github.com/mbialkowski/lazarus-revibed/blob/3c271f67f37e513e15983c65fc6dd9e5ee42e5df/README.md (Git blob 3936d1064bf9aa63a2f525f5d26f210a13acc0ef)
- mbialkowski-lazarus-revibed-reference-readme-md: https://github.com/mbialkowski/lazarus-revibed/blob/3c271f67f37e513e15983c65fc6dd9e5ee42e5df/reference/README.md (Git blob 6cf2ad9a590c45c8ae53c562696764e38e09f8df)
- mbialkowski-lazarus-revibed-remake-scripts-sim-hero-gd: https://github.com/mbialkowski/lazarus-revibed/blob/3c271f67f37e513e15983c65fc6dd9e5ee42e5df/remake/scripts/sim/hero.gd (Git blob 41a7ac15a47a4196ad6d513cc9b9322108337a76)
- retroshoppt-lotus2recomp-inspect-adf-py: https://github.com/retroshoppt/lotus2recomp/blob/805479d364020e34bca0f7db6a362c46acfe62b3/inspect_adf.py (Git blob 448c4724a69650ad4220b0652d967cafb5b65de3)
- retroshoppt-lotus2recomp-readme-md: https://github.com/retroshoppt/lotus2recomp/blob/805479d364020e34bca0f7db6a362c46acfe62b3/README.md (Git blob 7e939ed06e0ebcda893bd84595007b2e8e632310)

## Sources

```json
[
  {
    "first_indexed": "2026-11-05",
    "id": "github-retroshoppt-lotus2recomp",
    "kind": "github-repository",
    "last_reviewed": "2026-11-05",
    "open_task_ids": [],
    "projects_promoted": [
      "retroshoppt-lotus2recomp"
    ],
    "reason": "Early disk and boot-loader research: read-only Python inventory checks disk hashes, bootblock checksums, root block and packing signatures; README records first loader read. The game remains packed and neither recompiler nor playable port exists.",
    "review_state": "partial",
    "source": "https://github.com/RetroShopPT/Lotus2Recomp"
  },
  {
    "first_indexed": "2026-11-05",
    "id": "github-benbaker76-amigascope",
    "kind": "github-repository",
    "last_reviewed": "2026-11-05",
    "open_task_ids": [],
    "projects_promoted": [
      "benbaker76-amigascope"
    ],
    "reason": "Headless GDB proxy and MCP interface for FS-UAE and native SDL builds; includes profiling and Amiga copper and display inspection utilities. Author describes emulator and GDB dependencies; inspected proxy source, but did not run the harness.",
    "review_state": "partial",
    "source": "https://github.com/benbaker76/AmigaScope"
  },
  {
    "first_indexed": "2026-11-05",
    "id": "github-alphapixel-extract-adf-python",
    "kind": "github-repository",
    "last_reviewed": "2026-11-05",
    "open_task_ids": [],
    "projects_promoted": [
      "alphapixel-extract-adf-python"
    ],
    "reason": "Python port of mist64/extract-adf for extracting Amiga OFS files, including some damaged images. README says FFS is unsupported and DMS is recognized but not implemented; author reports fixture tests, not independently repeated.",
    "review_state": "partial",
    "source": "https://github.com/AlphaPixel/Extract-ADF-Python"
  },
  {
    "first_indexed": "2026-11-05",
    "id": "github-coolbutuseless-anotherworld",
    "kind": "github-repository",
    "last_reviewed": "2026-11-05",
    "open_task_ids": [],
    "projects_promoted": [
      "coolbutuseless-anotherworld"
    ],
    "reason": "R implementation of the game-specific script virtual machine, derived from cyxx/another_js and Fabien Sanglard’s interpreter. This interprets the game’s own designed bytecode, not a 68000 machine emulator. README describes unfinished music, bitmap rendering and automatic level progression; bundled reference identifies an Out of This World demo, so no Amiga-specific data compatibility is claimed.",
    "review_state": "partial",
    "source": "https://github.com/coolbutuseless/anotherworld"
  },
  {
    "first_indexed": "2026-11-05",
    "id": "github-mbialkowski-lazarus-revibed",
    "kind": "github-repository",
    "last_reviewed": "2026-11-05",
    "open_task_ids": [],
    "projects_promoted": [
      "mbialkowski-lazarus-revibed"
    ],
    "reason": "Reverse engineering targets the 1997 DOS port of the 1995 Amiga game, not the Amiga executable. Repository includes annotated Ghidra pseudo-C, format analysis, extraction tools and a Godot remake. Author reports automated comparisons and a winning-route playthrough; none independently reproduced.",
    "review_state": "partial",
    "source": "https://github.com/mbialkowski/lazarus-revibed"
  }
]
```

## Research event notes

Personally screened search results and source against the current catalogue and prior decisions. Inspected pinned primary documentation and representative source. No independent builds, gameplay, hardware or byte comparisons. Game-specific retained-machine runtimes are deferred for architecture review.
