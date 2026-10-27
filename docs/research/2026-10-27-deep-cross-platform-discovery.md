# Reviewed Enterprise, SAM Coupe, Thomson, Oric, CoCo and SourceGen discovery leads

Reviewed Enterprise, SAM Coupe, Thomson, Oric, CoCo and SourceGen discovery leads

Date: 2026-10-27 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- azas-mini-dos-historical-development-system / AI (no-evidence-found): No development-AI attribution was found in the inspected primary README or pinned head commit; non-use is not inferred.
- tile2sam-sam-coupe-graphics-tool / Runtime profiles (no-evidence-found): No minimum host CPU or RAM requirement is stated in the inspected documentation.
- tile2sam-sam-coupe-graphics-tool / AI (no-evidence-found): No explicit development-AI attribution was found in the pinned README or head commit; non-use is not inferred.
- vscode-pyz80-sam-coupe-development-extension / AI (no-evidence-found): No explicit development-AI attribution was found in the inspected README, package manifest or pinned head commit; non-use is not inferred.
- ep128-devel-sdcc-library / Build (no-evidence-found): The inspected primary README establishes scope but not a successful reproducible build; no compilation was performed.
- ep128-devel-sdcc-library / Runtime profiles (no-evidence-found): No explicit minimum Enterprise CPU variant, RAM, ROM or host requirement was found; none is inferred from the platform name.
- ep128-devel-sdcc-library / AI (no-evidence-found): No explicit development-AI attribution was found in the README or pinned head commit; non-use is not inferred.
- sdvideo-thomson-video-toolchain / AI (no-evidence-found): No explicit development-AI attribution was found in the README, Makefile or pinned head commit; non-use is not inferred.

## AZAS / MINI-DOS — preserved Z80 development system

Project ID: azas-mini-dos-historical-development-system · Overall audit: reviewed

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
  "display_title": "AZAS / MINI-DOS — preserved Z80 development system",
  "id": "azas-mini-dos-historical-development-system",
  "last_activity": "2023-06-09",
  "last_checked": "2026-10-27",
  "re_started": null,
  "reconstructed_languages": [
    "Z80 assembly",
    "C",
    "C#"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/autumn009/mini-dos",
  "runtime_profiles": [
    {
      "evidence": [
        "https://github.com/autumn009/mini-dos/blob/cf8761a86ff8efa5899590fd303792e4d92b32ee/README.md"
      ],
      "min_ram_kib": 64,
      "name": "PC-8001 ROM 1.1 with MULTICARD",
      "notes": "The README states this specific PC-8001 configuration; it is not generalized to the PC-8801 or Sharp X1 variants.",
      "os": "PC-8001 ROM 1.1 and MULTICARD",
      "platform": "NEC PC-8001"
    }
  ],
  "source_cpu": [
    "Z80"
  ],
  "source_language": [
    "Z80 assembly",
    "C",
    "yacc"
  ],
  "source_platforms": [
    "NEC PC-8001",
    "NEC PC-8801",
    "Sharp X1"
  ],
  "status": "Historical source and bootable disk images preserved; not independently executed",
  "subjects": [
    "AZAS",
    "MINI-DOS",
    "SOCE",
    "AZA86"
  ],
  "tags": [
    "Z80",
    "PC-8001",
    "PC-8801",
    "Sharp X1",
    "preservation"
  ],
  "target_cpu": [
    "Z80",
    "8086"
  ],
  "target_kinds": [],
  "target_platforms": [
    "NEC PC-8001",
    "NEC PC-8801",
    "Sharp X1",
    "IBM PC compatible"
  ],
  "techniques": [
    "Z80-to-8086 source translation",
    "disk-based native development"
  ],
  "title": "AZAS / MINI-DOS",
  "tool_kinds": [
    "assembler-toolchain",
    "compiler-toolchain",
    "development-environment"
  ],
  "types": [
    "historical development system",
    "original-source preservation"
  ],
  "upstream_name": "AZAS/MINI-DOS",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

The primary README identifies a preserved AZAS assembler, SOCE editor, MINI-DOS and bootable D88 images for PC-8001/8801 and Sharp X1.
- https://github.com/autumn009/mini-dos/blob/cf8761a86ff8efa5899590fd303792e4d92b32ee/README.md

### Classification (reviewed)

This is historical original-source preservation and development tooling, not a binary-derived reconstruction. AZA86 additionally translates AZAS Z80 source for MASM on 8086 systems.
- https://github.com/autumn009/mini-dos/blob/cf8761a86ff8efa5899590fd303792e4d92b32ee/README.md

### Source CPU (reviewed)

The preserved native development system and assembler sources target Z80 programs; this is the original architecture rather than a host minimum.
- https://github.com/autumn009/mini-dos/blob/cf8761a86ff8efa5899590fd303792e4d92b32ee/README.md

### Target CPU (reviewed)

AZAS produces Z80 work, while the documented AZA86 conversion route translates AZAS Z80 source to MASM 8086 form.
- https://github.com/autumn009/mini-dos/blob/cf8761a86ff8efa5899590fd303792e4d92b32ee/README.md

### Build (reviewed)

Source and bootable D88 images are present, but no clean build or execution was performed. Build, run and byte-identity flags remain unknown.
- https://github.com/autumn009/mini-dos/blob/cf8761a86ff8efa5899590fd303792e4d92b32ee/README.md

### Runtime profiles (reviewed)

The README explicitly requires 64 KB, ROM 1.1 and MULTICARD for its PC-8001 configuration. No equivalent minimum was stated for the PC-8801 or Sharp X1 variants.
- https://github.com/autumn009/mini-dos/blob/cf8761a86ff8efa5899590fd303792e4d92b32ee/README.md

### AI (no-evidence-found)

No development-AI attribution was found in the inspected primary README or pinned head commit; non-use is not inferred.
- https://github.com/autumn009/mini-dos/blob/cf8761a86ff8efa5899590fd303792e4d92b32ee/README.md
- https://github.com/autumn009/mini-dos/commit/cf8761a86ff8efa5899590fd303792e4d92b32ee

### Relationships (reviewed)

The README presents AZAS, SOCE, MINI-DOS and AZA86 as components of one period development system, so they are curated as one coherent record.
- https://github.com/autumn009/mini-dos/blob/cf8761a86ff8efa5899590fd303792e4d92b32ee/README.md

## tile2sam — SAM Coupe graphics and Z80 sprite-code generator

Project ID: tile2sam-sam-coupe-graphics-tool · Overall audit: reviewed

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
  "display_title": "tile2sam — SAM Coupe graphics and Z80 sprite-code generator",
  "id": "tile2sam-sam-coupe-graphics-tool",
  "last_activity": "2026-07-30",
  "last_checked": "2026-10-27",
  "re_started": null,
  "reconstructed_languages": [
    "Python",
    "Z80 assembly"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/simonowen/tile2sam",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Install and generation workflow documented; not independently executed",
  "subjects": [],
  "tags": [
    "SAM Coupe",
    "Z80",
    "graphics",
    "sprites"
  ],
  "target_cpu": [
    "Z80"
  ],
  "target_kinds": [],
  "target_platforms": [
    "SAM Coupe"
  ],
  "techniques": [
    "palette conversion",
    "sprite extraction",
    "sprite-specific code generation",
    "timing estimation"
  ],
  "title": "tile2sam",
  "tool_kinds": [
    "asset-tool",
    "assembler-toolchain"
  ],
  "types": [
    "graphics conversion tool",
    "code generator"
  ],
  "upstream_name": "tile2sam",
  "work_kinds": []
}
```

### Identity (reviewed)

The pinned README identifies tile2sam as a Python command that converts images into SAM Coupe graphics data or optimized sprite-specific Z80 routines.
- https://github.com/simonowen/tile2sam/blob/2e3f143a674e479c8ff58695cbbf2794ae4b8ad9/ReadMe.md

### Classification (reviewed)

This is directly useful retro-development asset and code-generation tooling, with SAM screen-mode, palette, tile and timing support.
- https://github.com/simonowen/tile2sam/blob/2e3f143a674e479c8ff58695cbbf2794ae4b8ad9/ReadMe.md

### Source CPU (not-applicable)

Input is modern image data rather than a legacy binary with an original CPU architecture.
- https://github.com/simonowen/tile2sam/blob/2e3f143a674e479c8ff58695cbbf2794ae4b8ad9/ReadMe.md

### Target CPU (reviewed)

The tool explicitly emits Z80 drawing, save, restore, copy and clear routines for SAM Coupe sprites.
- https://github.com/simonowen/tile2sam/blob/2e3f143a674e479c8ff58695cbbf2794ae4b8ad9/ReadMe.md

### Build (reviewed)

The README documents installation through uv and concrete command examples. It was not independently installed or run, so build/run flags remain unknown.
- https://github.com/simonowen/tile2sam/blob/2e3f143a674e479c8ff58695cbbf2794ae4b8ad9/ReadMe.md

### Runtime profiles (no-evidence-found)

No minimum host CPU or RAM requirement is stated in the inspected documentation.
- https://github.com/simonowen/tile2sam/blob/2e3f143a674e479c8ff58695cbbf2794ae4b8ad9/ReadMe.md

### AI (no-evidence-found)

No explicit development-AI attribution was found in the pinned README or head commit; non-use is not inferred.
- https://github.com/simonowen/tile2sam/blob/2e3f143a674e479c8ff58695cbbf2794ae4b8ad9/ReadMe.md
- https://github.com/simonowen/tile2sam/commit/2e3f143a674e479c8ff58695cbbf2794ae4b8ad9

### Relationships (reviewed)

The repository and package describe one tool with bundled demos rather than separate independently titled projects.
- https://github.com/simonowen/tile2sam/blob/2e3f143a674e479c8ff58695cbbf2794ae4b8ad9/ReadMe.md

## vscode-pyz80 — SAM Coupe build, run and deployment extension

Project ID: vscode-pyz80-sam-coupe-development-extension · Overall audit: reviewed

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
  "display_title": "vscode-pyz80 — SAM Coupe build, run and deployment extension",
  "id": "vscode-pyz80-sam-coupe-development-extension",
  "last_activity": "2026-04-20",
  "last_checked": "2026-10-27",
  "re_started": null,
  "reconstructed_languages": [
    "JavaScript",
    "JSON",
    "Z80 assembly"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/simonowen/vscode-pyz80",
  "runtime_profiles": [
    {
      "evidence": [
        "https://github.com/simonowen/vscode-pyz80/blob/f806a5b8565e83542ab2aac22b3687e5b3bde23a/README.md",
        "https://github.com/simonowen/vscode-pyz80/blob/f806a5b8565e83542ab2aac22b3687e5b3bde23a/package.json"
      ],
      "name": "VS Code extension workflow",
      "notes": "These are documented software prerequisites; no host CPU or RAM minimum is stated.",
      "os": "Visual Studio Code 1.75+, Python 3.6+, SimCoupe 1.1+; SAMdisk 4 required for network deployment",
      "platform": "Windows, macOS or Linux"
    }
  ],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Published extension workflow documented; not independently executed",
  "subjects": [],
  "tags": [
    "SAM Coupe",
    "Z80",
    "VS Code",
    "pyz80",
    "SimCoupe"
  ],
  "target_cpu": [
    "Z80"
  ],
  "target_kinds": [],
  "target_platforms": [
    "SAM Coupe"
  ],
  "techniques": [
    "disk-image generation",
    "emulator launch",
    "network deployment",
    "symbol-map integration"
  ],
  "title": "vscode-pyz80",
  "tool_kinds": [
    "ide",
    "assembler-toolchain",
    "automation",
    "development-environment"
  ],
  "types": [
    "Visual Studio Code extension"
  ],
  "upstream_name": "vscode-pyz80",
  "work_kinds": []
}
```

### Identity (reviewed)

The README and package manifest identify a VS Code extension for editing and assembling Z80 code for the SAM Coupe.
- https://github.com/simonowen/vscode-pyz80/blob/f806a5b8565e83542ab2aac22b3687e5b3bde23a/README.md
- https://github.com/simonowen/vscode-pyz80/blob/f806a5b8565e83542ab2aac22b3687e5b3bde23a/package.json

### Classification (reviewed)

It integrates assembly, SAMDOS v2 disk-image creation, SimCoupe launch/symbol maps and optional network delivery to a physical SAM, exceeding syntax highlighting alone.
- https://github.com/simonowen/vscode-pyz80/blob/f806a5b8565e83542ab2aac22b3687e5b3bde23a/README.md

### Source CPU (not-applicable)

The extension is development infrastructure and does not analyze an original legacy binary.
- https://github.com/simonowen/vscode-pyz80/blob/f806a5b8565e83542ab2aac22b3687e5b3bde23a/README.md

### Target CPU (reviewed)

The documented build workflow invokes pyz80 for SAM Coupe Z80 programs.
- https://github.com/simonowen/vscode-pyz80/blob/f806a5b8565e83542ab2aac22b3687e5b3bde23a/README.md

### Build (reviewed)

The package manifest and README document installation and commands; the extension was not independently installed or executed, so flags remain unknown.
- https://github.com/simonowen/vscode-pyz80/blob/f806a5b8565e83542ab2aac22b3687e5b3bde23a/README.md
- https://github.com/simonowen/vscode-pyz80/blob/f806a5b8565e83542ab2aac22b3687e5b3bde23a/package.json

### Runtime profiles (reviewed)

README and package metadata state VS Code 1.75+, Python 3.6+, SimCoupe 1.1+, and SAMdisk 4 for network use. No host CPU or RAM minimum is given.
- https://github.com/simonowen/vscode-pyz80/blob/f806a5b8565e83542ab2aac22b3687e5b3bde23a/README.md
- https://github.com/simonowen/vscode-pyz80/blob/f806a5b8565e83542ab2aac22b3687e5b3bde23a/package.json

### AI (no-evidence-found)

No explicit development-AI attribution was found in the inspected README, package manifest or pinned head commit; non-use is not inferred.
- https://github.com/simonowen/vscode-pyz80/blob/f806a5b8565e83542ab2aac22b3687e5b3bde23a/README.md
- https://github.com/simonowen/vscode-pyz80/commit/f806a5b8565e83542ab2aac22b3687e5b3bde23a

### Relationships (reviewed)

pyz80, SimCoupe and SAMdisk are external dependencies; this record covers the integration extension itself.
- https://github.com/simonowen/vscode-pyz80/blob/f806a5b8565e83542ab2aac22b3687e5b3bde23a/README.md

## ep128-devel — SDCC C library and crt0 for Enterprise 128

Project ID: ep128-devel-sdcc-library · Overall audit: reviewed

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
  "display_title": "ep128-devel — SDCC C library and crt0 for Enterprise 128",
  "id": "ep128-devel-sdcc-library",
  "last_activity": "2016-04-21",
  "last_checked": "2026-10-27",
  "project_url": "https://github.com/lgblgblgb/sdcc-projects/tree/master/ep128-devel",
  "re_started": null,
  "reconstructed_languages": [
    "Z80 assembly",
    "C"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/lgblgblgb/sdcc-projects",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Source reviewed; build and runtime not independently tested",
  "subjects": [],
  "tags": [
    "Enterprise 128",
    "Z80",
    "SDCC",
    "C"
  ],
  "target_cpu": [
    "Z80"
  ],
  "target_kinds": [],
  "target_platforms": [
    "Enterprise 128"
  ],
  "techniques": [
    "crt0 startup",
    "target library wrappers",
    "Z80 library replacement"
  ],
  "title": "ep128-devel",
  "tool_kinds": [
    "compiler-toolchain",
    "language-tooling"
  ],
  "types": [
    "runtime library",
    "C development support"
  ],
  "upstream_name": "ep128-devel",
  "work_kinds": []
}
```

### Identity (reviewed)

The root README and sole project directory identify ep128-devel as an Enterprise 128 library and crt0 for SDCC-based C development.
- https://github.com/lgblgblgb/sdcc-projects/blob/459eb1764bf31aee0d5db493d862bcbe32e277e7/README.md
- https://github.com/lgblgblgb/sdcc-projects/tree/459eb1764bf31aee0d5db493d862bcbe32e277e7/ep128-devel

### Classification (reviewed)

This is target-specific compiler/runtime infrastructure: wrappers and selected replacements around SDCC's generic Z80 library.
- https://github.com/lgblgblgb/sdcc-projects/blob/459eb1764bf31aee0d5db493d862bcbe32e277e7/README.md

### Source CPU (not-applicable)

The library is original development tooling rather than analysis of a legacy binary.
- https://github.com/lgblgblgb/sdcc-projects/blob/459eb1764bf31aee0d5db493d862bcbe32e277e7/README.md

### Target CPU (reviewed)

The README explicitly says the work uses SDCC's Z80 backend and replaces selected generic Z80 routines.
- https://github.com/lgblgblgb/sdcc-projects/blob/459eb1764bf31aee0d5db493d862bcbe32e277e7/README.md

### Build (no-evidence-found)

The inspected primary README establishes scope but not a successful reproducible build; no compilation was performed.
- https://github.com/lgblgblgb/sdcc-projects/blob/459eb1764bf31aee0d5db493d862bcbe32e277e7/README.md

### Runtime profiles (no-evidence-found)

No explicit minimum Enterprise CPU variant, RAM, ROM or host requirement was found; none is inferred from the platform name.
- https://github.com/lgblgblgb/sdcc-projects/blob/459eb1764bf31aee0d5db493d862bcbe32e277e7/README.md

### AI (no-evidence-found)

No explicit development-AI attribution was found in the README or pinned head commit; non-use is not inferred.
- https://github.com/lgblgblgb/sdcc-projects/blob/459eb1764bf31aee0d5db493d862bcbe32e277e7/README.md
- https://github.com/lgblgblgb/sdcc-projects/commit/459eb1764bf31aee0d5db493d862bcbe32e277e7

### Relationships (reviewed)

The repository contains one named target project, ep128-devel, which depends on upstream SDCC but is independently scoped Enterprise-specific work.
- https://github.com/lgblgblgb/sdcc-projects/blob/459eb1764bf31aee0d5db493d862bcbe32e277e7/README.md

## Oric_MiSTer — Oric, Atmos and Pravetz 8D FPGA core

Project ID: oric-mister-fpga-core · Overall audit: reviewed

### Typed catalogue values

```json
{
  "ai": {
    "evidence": [
      "Pinned head commit attributes savestate work to Claude Fable 5"
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
  "display_title": "Oric_MiSTer — Oric, Atmos and Pravetz 8D FPGA core",
  "id": "oric-mister-fpga-core",
  "last_activity": "2026-06-11",
  "last_checked": "2026-10-27",
  "re_started": null,
  "reconstructed_languages": [
    "VHDL",
    "Verilog",
    "SystemVerilog",
    "Python",
    "Shell"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/MiSTer-devel/Oric_MiSTer",
  "runtime_profiles": [
    {
      "evidence": [
        "https://github.com/MiSTer-devel/Oric_MiSTer/blob/c4cf449821b8a3bf2e3538739248ae29d30b8733/README.md"
      ],
      "name": "MiSTer FPGA core",
      "notes": "The repository targets MiSTer and documents deployed game and launcher paths; no host CPU or RAM minimum is stated. The emulated Oric configuration has 64 KiB RAM, which is not recorded as a MiSTer host minimum.",
      "platform": "MiSTer FPGA"
    }
  ],
  "source_cpu": [
    "6502"
  ],
  "source_language": [
    "6502 machine code",
    "Oric media and snapshot formats"
  ],
  "source_platforms": [
    "Oric-1",
    "Oric Atmos",
    "Pravetz 8D"
  ],
  "status": "Maintained core with checked-in releases; not independently built or run",
  "subjects": [
    "Oric-1",
    "Oric Atmos",
    "Pravetz 8D"
  ],
  "tags": [
    "Oric",
    "Atmos",
    "Pravetz 8D",
    "MiSTer",
    "FPGA",
    "6502"
  ],
  "target_cpu": [],
  "target_kinds": [],
  "target_platforms": [
    "MiSTer FPGA"
  ],
  "techniques": [
    "FPGA hardware reimplementation",
    "TAP streaming",
    "snapshot restoration",
    "ROM read-side patching",
    "disk-image support"
  ],
  "title": "Oric_MiSTer",
  "tool_kinds": [
    "emulator",
    "asset-tool",
    "binary-analysis"
  ],
  "types": [
    "FPGA core",
    "media analysis tooling"
  ],
  "upstream_name": "Oric / Oric Atmos for MiSTer",
  "work_kinds": [
    "reimplementation",
    "data-format-analysis"
  ]
}
```

### Identity (reviewed)

The pinned README identifies the current repository as the MiSTer Oric-1, Oric Atmos and Pravetz 8D FPGA core, with releases and support tools in the same tree.
- https://github.com/MiSTer-devel/Oric_MiSTer/blob/c4cf449821b8a3bf2e3538739248ae29d30b8733/README.md

### Classification (reviewed)

The core reimplements ULA video, 6502, VIA, AY sound, keyboard and disk/tape behavior. TAP, SNA and disk tools are supporting parts of the same coherent FPGA project.
- https://github.com/MiSTer-devel/Oric_MiSTer/blob/c4cf449821b8a3bf2e3538739248ae29d30b8733/README.md

### Source CPU (reviewed)

The primary README explicitly identifies the emulated CPU as 6502.
- https://github.com/MiSTer-devel/Oric_MiSTer/blob/c4cf449821b8a3bf2e3538739248ae29d30b8733/README.md

### Target CPU (not-applicable)

The output is FPGA logic for MiSTer rather than a port compiled for a documented target CPU.
- https://github.com/MiSTer-devel/Oric_MiSTer/blob/c4cf449821b8a3bf2e3538739248ae29d30b8733/README.md

### Build (reviewed)

The README documents the oric-build script and checked-in RBF releases while warning that deployment behavior reflects the maintainer's local setup. No build or execution was independently performed.
- https://github.com/MiSTer-devel/Oric_MiSTer/blob/c4cf449821b8a3bf2e3538739248ae29d30b8733/README.md

### Runtime profiles (reviewed)

MiSTer is the explicit runtime platform. The 64 KiB value describes the emulated Oric RAM, not a minimum host requirement; no MiSTer CPU or RAM minimum is stated.
- https://github.com/MiSTer-devel/Oric_MiSTer/blob/c4cf449821b8a3bf2e3538739248ae29d30b8733/README.md

### AI (reviewed)

The pinned head commit explicitly carries Claude Fable 5 co-author attribution for savestate work, establishing Claude-assisted contribution without generalizing beyond that evidence.
- https://github.com/MiSTer-devel/Oric_MiSTer/commit/c4cf449821b8a3bf2e3538739248ae29d30b8733

### Relationships (reviewed)

The README states this MiSTer core descends from earlier MiST/SiDi Oric FPGA work and used Oricutron source to understand snapshots; those are predecessors/references, not duplicates of the maintained MiSTer tree.
- https://github.com/MiSTer-devel/Oric_MiSTer/blob/c4cf449821b8a3bf2e3538739248ae29d30b8733/README.md

## SDVideo — Thomson MO/TO video converter and 6809 player

Project ID: sdvideo-thomson-video-toolchain · Overall audit: reviewed

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
  "display_title": "SDVideo — Thomson MO/TO video converter and 6809 player",
  "id": "sdvideo-thomson-video-toolchain",
  "last_activity": "2023-04-11",
  "last_checked": "2026-10-27",
  "re_started": null,
  "reconstructed_languages": [
    "Lua",
    "6809 assembly",
    "Make"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/Samuel-DEVULDER/SDVideo",
  "runtime_profiles": [
    {
      "cpu_family": "6809",
      "evidence": [
        "https://github.com/Samuel-DEVULDER/SDVideo/blob/d69dcb8b3b065411ad1389c9c47a7386663cc59b/README.md"
      ],
      "min_cpu": "MC6809 at 1 MHz",
      "name": "Native SDDrive video player",
      "notes": "Individual conversion modes have narrower machine compatibility documented in the README; no RAM minimum is stated.",
      "platform": "Thomson MO/TO computers with SDDrive"
    }
  ],
  "source_cpu": [],
  "source_language": [
    "video and audio media"
  ],
  "source_platforms": [],
  "status": "Converter and player sources reviewed; not independently built or run",
  "subjects": [],
  "tags": [
    "Thomson",
    "MO5",
    "TO8",
    "6809",
    "SDDrive",
    "video"
  ],
  "target_cpu": [
    "6809"
  ],
  "target_kinds": [],
  "target_platforms": [
    "Thomson MO5",
    "Thomson MO6",
    "Thomson TO7",
    "Thomson TO7/70",
    "Thomson TO8",
    "Thomson TO9+"
  ],
  "techniques": [
    "video frame conversion",
    "palette quantization",
    "native streaming playback",
    "FFmpeg integration"
  ],
  "title": "SDVideo",
  "tool_kinds": [
    "asset-tool",
    "assembler-toolchain"
  ],
  "types": [
    "media conversion toolchain",
    "native video player"
  ],
  "upstream_name": "SDVideo",
  "work_kinds": []
}
```

### Identity (reviewed)

The pinned README and Makefile establish a Lua/FFmpeg conversion pipeline plus native assembly player for SDDrive-equipped Thomson MO/TO machines.
- https://github.com/Samuel-DEVULDER/SDVideo/blob/d69dcb8b3b065411ad1389c9c47a7386663cc59b/README.md
- https://github.com/Samuel-DEVULDER/SDVideo/blob/d69dcb8b3b065411ad1389c9c47a7386663cc59b/Makefile

### Classification (reviewed)

This is substantial original retro-development tooling: host media conversion and a native player, not reverse engineering of a historical title.
- https://github.com/Samuel-DEVULDER/SDVideo/blob/d69dcb8b3b065411ad1389c9c47a7386663cc59b/README.md

### Source CPU (not-applicable)

Input is modern video/audio media rather than a legacy binary with an original CPU.
- https://github.com/Samuel-DEVULDER/SDVideo/blob/d69dcb8b3b065411ad1389c9c47a7386663cc59b/README.md

### Target CPU (reviewed)

The primary documentation explicitly describes a native MC6809 player running at 1 MHz and the repository contains its assembly sources.
- https://github.com/Samuel-DEVULDER/SDVideo/blob/d69dcb8b3b065411ad1389c9c47a7386663cc59b/README.md
- https://github.com/Samuel-DEVULDER/SDVideo/tree/d69dcb8b3b065411ad1389c9c47a7386663cc59b/asm

### Build (reviewed)

The Makefile invokes c6809 and the Lua/FFmpeg tools, but also downloads dependencies and media for test targets. No clean build or run was performed, so flags remain unknown.
- https://github.com/Samuel-DEVULDER/SDVideo/blob/d69dcb8b3b065411ad1389c9c47a7386663cc59b/Makefile

### Runtime profiles (reviewed)

The player is explicitly MC6809 at 1 MHz with SDDrive; the README gives per-mode model compatibility. No RAM minimum is stated or inferred.
- https://github.com/Samuel-DEVULDER/SDVideo/blob/d69dcb8b3b065411ad1389c9c47a7386663cc59b/README.md

### AI (no-evidence-found)

No explicit development-AI attribution was found in the README, Makefile or pinned head commit; non-use is not inferred.
- https://github.com/Samuel-DEVULDER/SDVideo/blob/d69dcb8b3b065411ad1389c9c47a7386663cc59b/README.md
- https://github.com/Samuel-DEVULDER/SDVideo/commit/d69dcb8b3b065411ad1389c9c47a7386663cc59b

### Relationships (reviewed)

The converter and native player are documented and built as one SDVideo workflow; no separately titled subproject was established.
- https://github.com/Samuel-DEVULDER/SDVideo/blob/d69dcb8b3b065411ad1389c9c47a7386663cc59b/README.md
- https://github.com/Samuel-DEVULDER/SDVideo/blob/d69dcb8b3b065411ad1389c9c47a7386663cc59b/Makefile

## Sources

```json
[
  {
    "first_indexed": "2026-10-27",
    "id": "github-autumn009-mini-dos",
    "kind": "github-repository",
    "last_reviewed": "2026-10-27",
    "reason": "Historical AZAS/MINI-DOS source, bootable disk images and AZA86 conversion tooling for NEC and Sharp Z80 systems.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/autumn009/mini-dos"
  },
  {
    "first_indexed": "2026-10-27",
    "id": "github-simonowen-tile2sam",
    "kind": "github-repository",
    "last_reviewed": "2026-10-27",
    "reason": "SAM Coupe graphics conversion and sprite-specific Z80 code-generation tool.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/simonowen/tile2sam"
  },
  {
    "first_indexed": "2026-10-27",
    "id": "github-simonowen-vscode-pyz80",
    "kind": "github-repository",
    "last_reviewed": "2026-10-27",
    "reason": "VS Code build, run and deployment integration for SAM Coupe Z80 projects.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/simonowen/vscode-pyz80"
  },
  {
    "first_indexed": "2026-10-27",
    "id": "github-lgblgblgb-sdcc-projects",
    "kind": "github-repository",
    "last_reviewed": "2026-10-27",
    "reason": "Enterprise 128 C-development library and crt0 for SDCC's Z80 backend.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/lgblgblgb/sdcc-projects"
  },
  {
    "first_indexed": "2026-10-27",
    "id": "github-mister-devel-oric-mister",
    "kind": "github-repository",
    "last_reviewed": "2026-10-27",
    "reason": "Maintained MiSTer FPGA core and associated Oric media/snapshot analysis tools.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/MiSTer-devel/Oric_MiSTer"
  },
  {
    "first_indexed": "2026-10-27",
    "id": "github-samuel-devulder-sdvideo",
    "kind": "github-repository",
    "last_reviewed": "2026-10-27",
    "reason": "Video conversion pipeline and native 6809 player for Thomson MO/TO computers.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/Samuel-DEVULDER/SDVideo"
  },
  {
    "first_indexed": "2026-10-27",
    "id": "github-debmint-coco-disasm",
    "kind": "github-repository",
    "last_reviewed": "2026-10-27",
    "reason": "Archived GitHub mirror of a CoCo OS-9/BASIC 6809 disassembler now pointing to a GitLab canonical repository.",
    "review_state": "partial",
    "source": "https://github.com/debmint/coco-disasm"
  },
  {
    "first_indexed": "2026-10-27",
    "id": "github-6809-rom-info",
    "kind": "github-repository",
    "last_reviewed": "2026-10-27",
    "reason": "Dragon/6809 ROM-information candidate returned by fresh search but unavailable at review time.",
    "review_state": "unreviewed",
    "source": "https://github.com/6809/rom-info"
  }
]
```

## Source updates

```json
[
  {
    "id": "web-6502disassembly-com",
    "last_reviewed": "2026-10-27",
    "reason": "Rechecked the Apple II ROM, GS/OS FST and RDOS pages; the latter two and the independently qualified ROM components are already tracked, while the broader outbound disassembly graph remains open.",
    "review_state": "partial"
  },
  {
    "id": "github-geogeo28-atari-reverse",
    "last_reviewed": "2026-10-27",
    "reason": "Rechecked the current projects tree: it still contains the six tracked Atari ST reconstruction subjects plus the previously excluded original homebrew BLACK ICE, with no new title directory.",
    "review_state": "substantially-reviewed"
  }
]
```

## Task updates

```json
[
  {
    "id": "task-continue-mining-6502disassembly-sourcegen-project-index",
    "last_reviewed": "2026-10-27",
    "notes_append": "Rechecked the Apple II ROM, GS/OS FST and RDOS landing pages. GS/OS and RDOS are already tracked; the mixed ROM index is already split into its independently qualified projects. No duplicate collection record was added; outbound links remain to review.",
    "state": "in-progress"
  },
  {
    "id": "task-continue-watching-geogeo28-atari-reverse-for-newly-added-reverse-enginee",
    "last_reviewed": "2026-10-27",
    "notes_append": "Rechecked the repository project tree; no new reverse-engineering target has appeared beyond the six tracked Atari ST projects, and BLACK ICE remains original homebrew rather than an RE-derived project.",
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
      "https://github.com/autumn009/mini-dos/blob/cf8761a86ff8efa5899590fd303792e4d92b32ee/README.md"
    ],
    "id": "promote-autumn009-mini-dos",
    "project_ids": [
      "azas-mini-dos-historical-development-system"
    ],
    "reason": "Preserved Z80 development system with bootable images and Z80-to-8086 conversion tooling.",
    "source_ids": [
      "github-autumn009-mini-dos"
    ],
    "title": "AZAS / MINI-DOS historical development system",
    "url": "https://github.com/autumn009/mini-dos"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/simonowen/tile2sam/blob/2e3f143a674e479c8ff58695cbbf2794ae4b8ad9/ReadMe.md"
    ],
    "id": "promote-simonowen-tile2sam",
    "project_ids": [
      "tile2sam-sam-coupe-graphics-tool"
    ],
    "reason": "SAM Coupe graphics extractor and optimized Z80 sprite-code generator.",
    "source_ids": [
      "github-simonowen-tile2sam"
    ],
    "title": "tile2sam",
    "url": "https://github.com/simonowen/tile2sam"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/simonowen/vscode-pyz80/blob/f806a5b8565e83542ab2aac22b3687e5b3bde23a/README.md"
    ],
    "id": "promote-simonowen-vscode-pyz80",
    "project_ids": [
      "vscode-pyz80-sam-coupe-development-extension"
    ],
    "reason": "SAM Coupe Z80 edit, assemble, run and deployment integration.",
    "source_ids": [
      "github-simonowen-vscode-pyz80"
    ],
    "title": "vscode-pyz80",
    "url": "https://github.com/simonowen/vscode-pyz80"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/lgblgblgb/sdcc-projects/blob/459eb1764bf31aee0d5db493d862bcbe32e277e7/README.md"
    ],
    "id": "promote-lgblgblgb-sdcc-projects",
    "project_ids": [
      "ep128-devel-sdcc-library"
    ],
    "reason": "Enterprise 128 crt0, library and C wrappers for SDCC's Z80 backend.",
    "source_ids": [
      "github-lgblgblgb-sdcc-projects"
    ],
    "title": "ep128-devel",
    "url": "https://github.com/lgblgblgb/sdcc-projects"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/MiSTer-devel/Oric_MiSTer/blob/c4cf449821b8a3bf2e3538739248ae29d30b8733/README.md"
    ],
    "id": "promote-mister-oric-core",
    "project_ids": [
      "oric-mister-fpga-core"
    ],
    "reason": "Maintained Oric-1, Atmos and Pravetz 8D FPGA core with media tooling.",
    "source_ids": [
      "github-mister-devel-oric-mister"
    ],
    "title": "Oric_MiSTer",
    "url": "https://github.com/MiSTer-devel/Oric_MiSTer"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/Samuel-DEVULDER/SDVideo/blob/d69dcb8b3b065411ad1389c9c47a7386663cc59b/README.md"
    ],
    "id": "promote-samuel-devulder-sdvideo",
    "project_ids": [
      "sdvideo-thomson-video-toolchain"
    ],
    "reason": "Thomson MO/TO media converter with native MC6809 playback code.",
    "source_ids": [
      "github-samuel-devulder-sdvideo"
    ],
    "title": "SDVideo",
    "url": "https://github.com/Samuel-DEVULDER/SDVideo"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/debmint/coco-disasm/blob/5798a5b8752ae3e4e9b07c595e07598606901bf8/README.md"
    ],
    "id": "defer-debmint-coco-disasm-canonical",
    "reason": "Archived mirror points to GitLab; inspect the canonical history and current build state before promotion.",
    "source_ids": [
      "github-debmint-coco-disasm"
    ],
    "title": "coco-disasm",
    "url": "https://github.com/debmint/coco-disasm"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/6809/rom-info"
    ],
    "id": "defer-6809-rom-info-unavailable",
    "reason": "GitHub candidate was unavailable; recheck primary scope before classification.",
    "source_ids": [
      "github-6809-rom-info"
    ],
    "title": "6809 rom-info",
    "url": "https://github.com/6809/rom-info"
  }
]
```

## Source ids

```json
[
  "web-6502disassembly-com",
  "github-geogeo28-atari-reverse"
]
```

## Research event notes

Queue work rechecked the SourceGen Apple II pages and geogeo28 Atari ST project tree. Fresh-search routes and exact queries: web/GitHub repository search — site:github.com Thomson MO5 TO7 TO8 disassembly reconstruction source; site:github.com Oric Atmos disassembly reassembly source reconstruction; site:github.com Atari Lynx disassembly reassembly decompilation source; site:github.com TRS-80 Color Computer CoCo disassembly reconstruction tooling; site:github.com Enterprise 128 disassembly source reconstruction; site:github.com SAM Coupe disassembly source reconstruction; site:github.com Sharp X1 disassembly source reconstruction; site:github.com Dragon 32 disassembly source reconstruction. Eleven candidate URLs were screened; six were promoted, two deferred, and three SourceGen collection pages resolved to existing tracked projects. The CPU audit queue returned zero unresolved areas before selection, so no existing CPU fields were refreshed merely to satisfy a quota.
