# Sharp MZ, Thomson, DAAD/DOS and Apple Lisa discovery

Review thirteen queue/search candidates; promote nine projects and close three old discovery tasks

Date: 2026-10-31 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- mz-basictoqd-sharp-mz-transfer-tool / Build (reviewed): Primary documentation review only; no generated image was loaded into an emulator.
- mz-basictoqd-sharp-mz-transfer-tool / Runtime profiles (no-evidence-found): No minimum browser, host CPU, RAM, or physical Sharp MZ hardware requirement is stated.
- mz-basictoqd-sharp-mz-transfer-tool / AI (no-evidence-found): No explicit development-AI attribution was found in the reviewed primary documentation; this does not establish non-use.
- arem-mzf-parser-sharp-mz800 / Build (reviewed): Static source review only; Ruby dependencies and parser execution were not run.
- arem-mzf-parser-sharp-mz800 / AI (no-evidence-found): No explicit development-AI attribution was found in the README or inspected parser; this does not establish non-use.
- theodore-thomson-libretro-debugger / Target CPU (no-evidence-found): No native host/output CPU is specified; a portable libretro target is not evidence for a particular host architecture.
- theodore-thomson-libretro-debugger / Build (reviewed): Upstream-documented build and runtime only; no compilation, ROM loading, or debugger session was performed.
- theodore-thomson-libretro-debugger / AI (no-evidence-found): No explicit development-AI attribution was found in the reviewed primary documentation; this does not establish non-use.
- crayon-thomson-mo5-emulator-debugger / Target CPU (no-evidence-found): No native host CPU is specified; supported compiler/OS families do not establish a target architecture.
- crayon-thomson-mo5-emulator-debugger / Build (reviewed): Static documentation review only; no compiler, test, ROM, cassette, emulator or debugger was run.
- crayon-thomson-mo5-emulator-debugger / AI (no-evidence-found): Kiro configuration/specification files exist in the repository, but inspected primary documentation does not establish an actual AI-authored contribution.
- lisa-utilities-monitor-image-extractor / Build (reviewed): Read-only review; no disk image or extracted file was processed.
- lisa-utilities-monitor-image-extractor / AI (no-evidence-found): No explicit development-AI attribution was found in the reviewed primary documentation; this does not establish non-use.
- lisafilemover-native-lisa-utility / Target CPU (no-evidence-found): No explicit target CPU statement was found; Apple Lisa and Lisa Pascal alone are not used to infer Motorola 68000 output metadata.
- lisafilemover-native-lisa-utility / Build (reviewed): Upstream source/build/release evidence only; no Lisa Workshop, disk image, emulator or physical Lisa was run.
- daad-reborn-compiler-drc / Build (reviewed): Primary documentation/source-tree review only; compiler and generated media were not built or run.
- daad-reborn-compiler-drc / AI (no-evidence-found): No explicit development-AI attribution was found in the reviewed primary documentation; this does not establish non-use.
- dsbxida-dosbox-x-ida-debugger / Target CPU (no-evidence-found): No native host/output CPU requirement was found; DOSBox-X lineage and IDA support do not establish a host architecture.
- dsbxida-dosbox-x-ida-debugger / Build (reviewed): Static source review only; no IDA installation, plugin build, DOS program or emulator process was run.
- dsbxida-dosbox-x-ida-debugger / Runtime profiles (no-evidence-found): No minimum IDA, host OS, CPU or RAM requirement was established from the inspected primary files.
- dsbxida-dosbox-x-ida-debugger / AI (no-evidence-found): No explicit development-AI attribution was found in the reviewed primary documentation or plugin source; this does not establish non-use.
- neowidex-apple-lisa-widget-utility / Build (reviewed): Read-only documentation review; destructive drive operations, assembly, boot image generation and hardware/emulator execution were not performed.
- neowidex-apple-lisa-widget-utility / AI (no-evidence-found): No explicit development-AI attribution was found in the reviewed README/build documentation; this does not establish non-use.
- 180-spectrum / Build (reviewed): No SkoolKit command, original-game extraction, assembly, executable or emulator was run.
- 180-spectrum / Runtime profiles (no-evidence-found): No reconstructed runnable build or minimum hardware requirement is documented; the original game is required as disassembly input.
- 180-spectrum / AI (no-evidence-found): No explicit development-AI attribution was found in the reviewed primary files; this does not establish non-use.

## BASIC to QD — Sharp MZ BASIC transfer and listing tools

Project ID: mz-basictoqd-sharp-mz-transfer-tool · Overall audit: reviewed

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
  "display_title": "BASIC to QD — Sharp MZ BASIC transfer and listing tools",
  "id": "mz-basictoqd-sharp-mz-transfer-tool",
  "last_activity": "2019-10-15",
  "last_checked": "2026-10-31",
  "re_started": null,
  "reconstructed_languages": [
    "JavaScript",
    "HTML"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/lukq/mz-basictoqd",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [
    "Sharp MZ BASIC text and binary files"
  ],
  "source_platforms": [
    "Sharp MZ-700",
    "Sharp MZ-800"
  ],
  "status": "Browser transfer/listing utility documented upstream; not independently executed",
  "subjects": [
    "Sharp MZ BASIC transfer tools"
  ],
  "tags": [
    "sharp-mz",
    "basic",
    "quick-disk"
  ],
  "target_cpu": [],
  "target_kinds": [],
  "target_platforms": [
    "Web",
    "Sharp MZ-700",
    "Sharp MZ-800"
  ],
  "techniques": [
    "Quick Disk image generation",
    "MZF BASIC listing"
  ],
  "title": "BASIC to QD — Sharp MZ BASIC transfer and listing tools",
  "tool_kinds": [
    "disk-filesystem-tool",
    "language-tooling"
  ],
  "types": [
    "original retro-development tool",
    "media conversion"
  ],
  "upstream_name": "mz-basictoqd",
  "work_kinds": []
}
```

### Identity (reviewed)

The repository documents a browser application that turns Sharp MZ-800 BASIC text into Quick Disk or cassette data and includes a reverse listing utility for MZF BASIC files.
- https://github.com/lukq/mz-basictoqd/blob/455203562a112b14d0411dc49dee0a780686e5c2/Readme.md

### Classification (reviewed)

This is original retro-development and transfer tooling, not a reverse-engineered program or RE-derived port.
- https://github.com/lukq/mz-basictoqd/blob/455203562a112b14d0411dc49dee0a780686e5c2/Readme.md

### Source CPU (not-applicable)

Source CPU is not applicable: the tool transforms BASIC text and binary media records rather than analysing an original machine-code program.
- https://github.com/lukq/mz-basictoqd/blob/455203562a112b14d0411dc49dee0a780686e5c2/Readme.md

### Target CPU (not-applicable)

Target CPU is not applicable: the outputs are BASIC/media data, not native machine code.
- https://github.com/lukq/mz-basictoqd/blob/455203562a112b14d0411dc49dee0a780686e5c2/Readme.md

### Build (reviewed)

The README gives an end-to-end browser workflow and names supported BASIC versions and emulators; the application was not executed in this review. Limitations: Primary documentation review only; no generated image was loaded into an emulator.
- https://github.com/lukq/mz-basictoqd/blob/455203562a112b14d0411dc49dee0a780686e5c2/Readme.md

### Runtime profiles (no-evidence-found)

No minimum browser, host CPU, RAM, or physical Sharp MZ hardware requirement is stated.
- https://github.com/lukq/mz-basictoqd/blob/455203562a112b14d0411dc49dee0a780686e5c2/Readme.md

### AI (no-evidence-found)

No explicit development-AI attribution was found in the reviewed primary documentation; this does not establish non-use.
- https://github.com/lukq/mz-basictoqd/blob/455203562a112b14d0411dc49dee0a780686e5c2/Readme.md

### Relationships (reviewed)

The README names EmuZ-800/mz800emu usage and separate Quick Disk and cassette output paths; this entry tracks the converter/listing tool rather than those emulators.
- https://github.com/lukq/mz-basictoqd/blob/455203562a112b14d0411dc49dee0a780686e5c2/Readme.md

## AREM MZF Parser — Sharp MZ-800 assembler-source recovery

Project ID: arem-mzf-parser-sharp-mz800 · Overall audit: reviewed

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
  "display_title": "AREM MZF Parser — Sharp MZ-800 assembler-source recovery",
  "id": "arem-mzf-parser-sharp-mz800",
  "last_activity": "2021-08-21",
  "last_checked": "2026-10-31",
  "re_started": null,
  "reconstructed_languages": [
    "Ruby",
    "Z80 assembly text"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/bver/arem-mzf-parser",
  "runtime_profiles": [
    {
      "evidence": [
        "https://github.com/bver/arem-mzf-parser/blob/7d798c1431f05c99fb4fa20415aa730b0b00075c/README.md"
      ],
      "name": "arem_src_parse.rb",
      "notes": "README documents bundle install and command-line invocation.",
      "os": "Ruby with Bundler and BinData",
      "platform": "Modern host"
    }
  ],
  "source_cpu": [
    "Z80"
  ],
  "source_language": [
    "AREM binary source format",
    "Z80 assembly"
  ],
  "source_platforms": [
    "Sharp MZ-800"
  ],
  "status": "Documented AREM source parser; not independently executed",
  "subjects": [
    "AREM MZF assembler sources"
  ],
  "tags": [
    "sharp-mz",
    "z80",
    "arem"
  ],
  "target_cpu": [],
  "target_kinds": [],
  "target_platforms": [
    "Modern host"
  ],
  "techniques": [
    "BinData parsing",
    "MZF type 0x41 decoding"
  ],
  "title": "AREM MZF Parser — Sharp MZ-800 assembler-source recovery",
  "tool_kinds": [
    "binary-analysis",
    "language-tooling"
  ],
  "types": [
    "source recovery tool",
    "binary parser"
  ],
  "upstream_name": "arem-mzf-parser",
  "work_kinds": [
    "data-format-analysis"
  ]
}
```

### Identity (reviewed)

The repository identifies a Ruby parser for assembler source stored in AREM-format MZF type 0x41 files from the Sharp MZ-800.
- https://github.com/bver/arem-mzf-parser/blob/7d798c1431f05c99fb4fa20415aa730b0b00075c/README.md

### Classification (reviewed)

This is binary-format and language tooling for recovering historical assembler text, not a reconstructed game or emulator.
- https://github.com/bver/arem-mzf-parser/blob/7d798c1431f05c99fb4fa20415aa730b0b00075c/README.md
- https://github.com/bver/arem-mzf-parser/blob/7d798c1431f05c99fb4fa20415aa730b0b00075c/arem_src_parse.rb

### Source CPU (reviewed)

The README explicitly identifies Z80 assembler input and the implementation decodes AREM records and Z80 instruction/register forms.
- https://github.com/bver/arem-mzf-parser/blob/7d798c1431f05c99fb4fa20415aa730b0b00075c/README.md
- https://github.com/bver/arem-mzf-parser/blob/7d798c1431f05c99fb4fa20415aa730b0b00075c/arem_src_parse.rb

### Target CPU (not-applicable)

Target CPU is not applicable because the tool emits assembler text rather than a compiled executable.
- https://github.com/bver/arem-mzf-parser/blob/7d798c1431f05c99fb4fa20415aa730b0b00075c/README.md

### Build (reviewed)

The README documents bundle install and a command that emits my_source.asm.txt; no sample file was parsed here. Limitations: Static source review only; Ruby dependencies and parser execution were not run.
- https://github.com/bver/arem-mzf-parser/blob/7d798c1431f05c99fb4fa20415aa730b0b00075c/README.md

### Runtime profiles (reviewed)

The documented Ruby/Bundler/BinData host requirement is captured, with no minimum CPU or RAM inferred.
- https://github.com/bver/arem-mzf-parser/blob/7d798c1431f05c99fb4fa20415aa730b0b00075c/README.md

### AI (no-evidence-found)

No explicit development-AI attribution was found in the README or inspected parser; this does not establish non-use.
- https://github.com/bver/arem-mzf-parser/blob/7d798c1431f05c99fb4fa20415aa730b0b00075c/README.md

### Relationships (reviewed)

The input is the AREM assembler-source container used on Sharp MZ-800; the project is distinct from general MZF disk/tape emulators.
- https://github.com/bver/arem-mzf-parser/blob/7d798c1431f05c99fb4fa20415aa730b0b00075c/README.md
- https://github.com/bver/arem-mzf-parser/blob/7d798c1431f05c99fb4fa20415aa730b0b00075c/arem_src_parse.rb

## Theodore — Thomson MO/TO emulator and debugger

Project ID: theodore-thomson-libretro-debugger · Overall audit: reviewed

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
  "display_title": "Theodore — Thomson MO/TO emulator and debugger",
  "id": "theodore-thomson-libretro-debugger",
  "last_activity": "2026-08-17",
  "last_checked": "2026-10-31",
  "re_started": null,
  "reconstructed_languages": [
    "C"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/Zlika/theodore",
  "runtime_profiles": [
    {
      "evidence": [
        "https://github.com/Zlika/theodore/blob/4d469ce0f71ee046ceb78cdbf8e9f18364aaa918/README.md"
      ],
      "name": "Theodore libretro core",
      "notes": "README lists RetroArch and multiple libretro distributions; no hardware minimum is stated.",
      "os": "RetroArch-compatible environment",
      "platform": "Libretro"
    }
  ],
  "source_cpu": [
    "Motorola 6809"
  ],
  "source_language": [
    "6809 machine code"
  ],
  "source_platforms": [
    "Thomson MO5",
    "Thomson MO6",
    "Thomson TO7",
    "Thomson TO8",
    "Thomson TO9"
  ],
  "status": "Maintained libretro emulator with interactive debugger; not independently built",
  "subjects": [
    "Thomson MO/TO computers"
  ],
  "tags": [
    "thomson",
    "6809",
    "libretro"
  ],
  "target_cpu": [],
  "target_kinds": [],
  "target_platforms": [
    "Libretro"
  ],
  "techniques": [
    "6809 emulation",
    "interactive disassembly",
    "breakpoints"
  ],
  "title": "Theodore — Thomson MO/TO emulator and debugger",
  "tool_kinds": [
    "emulator",
    "debugger",
    "disassembler"
  ],
  "types": [
    "libretro core",
    "software archaeology tool"
  ],
  "upstream_name": "theodore",
  "work_kinds": []
}
```

### Identity (reviewed)

Theodore is a libretro core for Thomson TO7/TO8/TO9 and MO5/MO6 families, with documented media support and installation routes.
- https://github.com/zlika/theodore/blob/4d469ce0f71ee046ceb78cdbf8e9f18364aaa918/README.md

### Classification (reviewed)

It qualifies as core emulator/debugger/disassembler tooling directly useful to retro development and software archaeology.
- https://github.com/zlika/theodore/blob/4d469ce0f71ee046ceb78cdbf8e9f18364aaa918/README.md

### Source CPU (reviewed)

The emulated Thomson family uses the Motorola 6809 lineage and the project documents 6809 CPU emulation and disassembly.
- https://github.com/zlika/theodore/blob/4d469ce0f71ee046ceb78cdbf8e9f18364aaa918/README.md

### Target CPU (no-evidence-found)

No native host/output CPU is specified; a portable libretro target is not evidence for a particular host architecture.
- https://github.com/zlika/theodore/blob/4d469ce0f71ee046ceb78cdbf8e9f18364aaa918/README.md

### Build (reviewed)

The README documents make-based and Android NDK builds plus installation through libretro distributions; no build was run here. Limitations: Upstream-documented build and runtime only; no compilation, ROM loading, or debugger session was performed.
- https://github.com/zlika/theodore/blob/4d469ce0f71ee046ceb78cdbf8e9f18364aaa918/README.md

### Runtime profiles (reviewed)

A libretro runtime route is documented, but no minimum CPU, RAM, chipset, or OS version is stated.
- https://github.com/zlika/theodore/blob/4d469ce0f71ee046ceb78cdbf8e9f18364aaa918/README.md

### AI (no-evidence-found)

No explicit development-AI attribution was found in the reviewed primary documentation; this does not establish non-use.
- https://github.com/zlika/theodore/blob/4d469ce0f71ee046ceb78cdbf8e9f18364aaa918/README.md

### Relationships (reviewed)

The README explicitly traces Theodore to Daniel Coulom's DCTO8D, DCTO9P and DCMO5 emulators; this is the maintained libretro descendant.
- https://github.com/zlika/theodore/blob/4d469ce0f71ee046ceb78cdbf8e9f18364aaa918/README.md

## Crayon — Thomson MO5 emulator and debugger

Project ID: crayon-thomson-mo5-emulator-debugger · Overall audit: reviewed

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
  "display_title": "Crayon — Thomson MO5 emulator and debugger",
  "id": "crayon-thomson-mo5-emulator-debugger",
  "last_activity": "2026-06-30",
  "last_checked": "2026-10-31",
  "re_started": null,
  "reconstructed_languages": [
    "C++"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/qam4/crayon",
  "runtime_profiles": [
    {
      "evidence": [
        "https://github.com/qam4/crayon/blob/136d6b9c49076485abc48e1d9fed62293231f36d/README.md"
      ],
      "name": "Crayon emulator",
      "notes": "Requires separately supplied 12 KiB MO5 BASIC 1.0 ROM and 4 KiB Monitor ROM; no host hardware minimum is stated.",
      "os": "CMake 3.15+, C++17 compiler and SDL2; presets cover Linux, macOS, Windows and Android",
      "platform": "Modern host"
    }
  ],
  "source_cpu": [
    "Motorola 6809"
  ],
  "source_language": [
    "Motorola 6809 machine code"
  ],
  "source_platforms": [
    "Thomson MO5"
  ],
  "status": "C++17 MO5 emulator with standalone, headless and libretro routes; not independently built",
  "subjects": [
    "Thomson MO5"
  ],
  "tags": [
    "thomson",
    "mo5",
    "6809"
  ],
  "target_cpu": [],
  "target_kinds": [],
  "target_platforms": [
    "Windows",
    "Linux",
    "macOS",
    "Android",
    "Libretro"
  ],
  "techniques": [
    "6809E emulation",
    "ImGui debugger",
    "save states"
  ],
  "title": "Crayon — Thomson MO5 emulator and debugger",
  "tool_kinds": [
    "emulator",
    "debugger",
    "disassembler"
  ],
  "types": [
    "standalone emulator",
    "libretro core"
  ],
  "upstream_name": "crayon",
  "work_kinds": []
}
```

### Identity (reviewed)

Crayon is a C++17 Thomson MO5 emulator with standalone SDL2, headless CLI and libretro execution paths.
- https://github.com/qam4/crayon/blob/136d6b9c49076485abc48e1d9fed62293231f36d/README.md

### Classification (reviewed)

Its debugger, disassembler, tests and hardware documentation make it directly relevant development and archaeology tooling.
- https://github.com/qam4/crayon/blob/136d6b9c49076485abc48e1d9fed62293231f36d/README.md

### Source CPU (reviewed)

The README explicitly states full Motorola 6809E CPU emulation for the MO5.
- https://github.com/qam4/crayon/blob/136d6b9c49076485abc48e1d9fed62293231f36d/README.md

### Target CPU (no-evidence-found)

No native host CPU is specified; supported compiler/OS families do not establish a target architecture.
- https://github.com/qam4/crayon/blob/136d6b9c49076485abc48e1d9fed62293231f36d/README.md

### Build (reviewed)

CMake presets, compiler/SDL2 requirements, tests and launcher examples are documented; none was executed in this review. Limitations: Static documentation review only; no compiler, test, ROM, cassette, emulator or debugger was run.
- https://github.com/qam4/crayon/blob/136d6b9c49076485abc48e1d9fed62293231f36d/README.md

### Runtime profiles (reviewed)

The explicit ROM requirements are captured without converting the historical MO5's 48 KiB RAM description into a host minimum.
- https://github.com/qam4/crayon/blob/136d6b9c49076485abc48e1d9fed62293231f36d/README.md

### AI (no-evidence-found)

Kiro configuration/specification files exist in the repository, but inspected primary documentation does not establish an actual AI-authored contribution.
- https://github.com/qam4/crayon/blob/136d6b9c49076485abc48e1d9fed62293231f36d/README.md

### Relationships (reviewed)

Crayon is a distinct new MO5 emulator rather than a fork of the already indexed Maurice or Theodore lineages.
- https://github.com/qam4/crayon/blob/136d6b9c49076485abc48e1d9fed62293231f36d/README.md

## Lisa Utilities — Lisa Monitor image extractor

Project ID: lisa-utilities-monitor-image-extractor · Overall audit: reviewed

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
  "display_title": "Lisa Utilities — Lisa Monitor image extractor",
  "id": "lisa-utilities-monitor-image-extractor",
  "last_activity": "2016-05-05",
  "last_checked": "2026-10-31",
  "re_started": null,
  "reconstructed_languages": [
    "Python"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/d235j/lisa-utilities",
  "runtime_profiles": [
    {
      "evidence": [
        "https://github.com/d235j/lisa-utilities/blob/d79ac35fdc366c49ed16c6a9d3948809862c7f68/README.md"
      ],
      "name": "extract_lisamonitor_image.py",
      "notes": "Primary README states the supported Python generations; no CPU/RAM minimum is given.",
      "os": "Python 2.7 or 3.x",
      "platform": "Modern host"
    }
  ],
  "source_cpu": [],
  "source_language": [
    "Apple Pascal/Lisa Monitor disk images"
  ],
  "source_platforms": [
    "Apple Lisa"
  ],
  "status": "Python Lisa Monitor image extractor documented upstream; not independently executed",
  "subjects": [
    "Apple Lisa Monitor disk images"
  ],
  "tags": [
    "apple-lisa",
    "disk-image",
    "preservation"
  ],
  "target_cpu": [],
  "target_kinds": [],
  "target_platforms": [
    "Modern host"
  ],
  "techniques": [
    "DC42/raw/PO parsing",
    "Twiggy track ordering"
  ],
  "title": "Lisa Utilities — Lisa Monitor image extractor",
  "tool_kinds": [
    "disk-filesystem-tool"
  ],
  "types": [
    "preservation utility",
    "disk image extractor"
  ],
  "upstream_name": "lisa-utilities",
  "work_kinds": [
    "data-format-analysis"
  ]
}
```

### Identity (reviewed)

The repository provides Python utilities for extracting files from Apple Pascal/Lisa Monitor images used in early Lisa and Macintosh development.
- https://github.com/d235j/lisa-utilities/blob/d79ac35fdc366c49ed16c6a9d3948809862c7f68/README.md

### Classification (reviewed)

This is preservation and disk-format tooling, not a recovered Lisa application or emulator.
- https://github.com/d235j/lisa-utilities/blob/d79ac35fdc366c49ed16c6a9d3948809862c7f68/README.md

### Source CPU (not-applicable)

Source CPU is not applicable because the inspected subject is a disk-image format and file extractor, not original executable code.
- https://github.com/d235j/lisa-utilities/blob/d79ac35fdc366c49ed16c6a9d3948809862c7f68/README.md

### Target CPU (not-applicable)

Target CPU is not applicable because extraction produces host files rather than native machine code.
- https://github.com/d235j/lisa-utilities/blob/d79ac35fdc366c49ed16c6a9d3948809862c7f68/README.md

### Build (reviewed)

The README documents the extractor's purpose and Python invocation context; it was not run against an image here. Limitations: Read-only review; no disk image or extracted file was processed.
- https://github.com/d235j/lisa-utilities/blob/d79ac35fdc366c49ed16c6a9d3948809862c7f68/README.md

### Runtime profiles (reviewed)

Python 2.7 or 3.x is explicitly documented and captured; no minimum host CPU or RAM is stated.
- https://github.com/d235j/lisa-utilities/blob/d79ac35fdc366c49ed16c6a9d3948809862c7f68/README.md

### AI (no-evidence-found)

No explicit development-AI attribution was found in the reviewed primary documentation; this does not establish non-use.
- https://github.com/d235j/lisa-utilities/blob/d79ac35fdc366c49ed16c6a9d3948809862c7f68/README.md

### Relationships (reviewed)

Lisa Monitor is identified as a development image format used by Apple and others; the entry is scoped to the extractor rather than those historical tools.
- https://github.com/d235j/lisa-utilities/blob/d79ac35fdc366c49ed16c6a9d3948809862c7f68/README.md

## LisaFileMover — native Lisa Office System file utility

Project ID: lisafilemover-native-lisa-utility · Overall audit: reviewed

### Typed catalogue values

```json
{
  "ai": {
    "tools": [
      "Claude"
    ],
    "usage": true
  },
  "build": {
    "byte_exact": null,
    "compilable": true,
    "playable": null,
    "runnable": true
  },
  "display_title": "LisaFileMover — native Lisa Office System file utility",
  "id": "lisafilemover-native-lisa-utility",
  "last_activity": "2026-09-16",
  "last_checked": "2026-10-31",
  "re_started": null,
  "reconstructed_languages": [
    "Lisa Pascal"
  ],
  "record_class": "subject",
  "repo": "https://github.com/GyroPilot/Apple-LisaFileMover",
  "runtime_profiles": [
    {
      "evidence": [
        "https://github.com/GyroPilot/Apple-LisaFileMover/blob/5fe3ce40f6e3d744a2966f0c08b603ca249e302b/README.md"
      ],
      "name": "LisaFileMover 1.1",
      "notes": "README states every 1.1 feature ran on LisaFPGA and 1.0 was verified on a Lisa 2/10; no minimum CPU/RAM is inferred.",
      "os": "Lisa Office System 3.1",
      "platform": "Apple Lisa"
    }
  ],
  "source_cpu": [],
  "source_language": [
    "Lisa Pascal"
  ],
  "source_platforms": [
    "Apple Lisa"
  ],
  "status": "Released native Lisa Office System utility with documented Workshop build",
  "subjects": [
    "LisaFileMover"
  ],
  "tags": [
    "apple-lisa",
    "lisa-office-system",
    "original-homebrew"
  ],
  "target_cpu": [],
  "target_kinds": [
    "application",
    "development-tool"
  ],
  "target_platforms": [
    "Apple Lisa"
  ],
  "techniques": [
    "Lisa Office System desktop integration",
    "Workshop exec build scripts"
  ],
  "title": "LisaFileMover — native Lisa Office System file utility",
  "tool_kinds": [],
  "types": [
    "original homebrew",
    "native file utility"
  ],
  "upstream_name": "LisaFileMover",
  "work_kinds": []
}
```

### Identity (reviewed)

LisaFileMover is a native Lisa Office System desktop utility for listing, copying, renaming and deleting invisible files and tool sets.
- https://github.com/gyropilot/apple-lisafilemover/blob/5fe3ce40f6e3d744a2966f0c08b603ca249e302b/README.md

### Classification (reviewed)

It is substantial original homebrew/native application development, not reverse-engineered or RE-derived software.
- https://github.com/gyropilot/apple-lisafilemover/blob/5fe3ce40f6e3d744a2966f0c08b603ca249e302b/README.md

### Source CPU (not-applicable)

Source CPU is not applicable: this is original source development rather than analysis of a historical binary.
- https://github.com/gyropilot/apple-lisafilemover/blob/5fe3ce40f6e3d744a2966f0c08b603ca249e302b/README.md

### Target CPU (no-evidence-found)

No explicit target CPU statement was found; Apple Lisa and Lisa Pascal alone are not used to infer Motorola 68000 output metadata.
- https://github.com/gyropilot/apple-lisafilemover/blob/5fe3ce40f6e3d744a2966f0c08b603ca249e302b/README.md

### Build (reviewed)

The repository includes Lisa Pascal Workshop 3.0 compile/link/install scripts, released DC42 images and a documented Lisa-side build route. Limitations: Upstream source/build/release evidence only; no Lisa Workshop, disk image, emulator or physical Lisa was run.
- https://github.com/gyropilot/apple-lisafilemover/blob/5fe3ce40f6e3d744a2966f0c08b603ca249e302b/README.md

### Runtime profiles (reviewed)

Lisa Office System 3.1 and upstream hardware/emulator verification are captured without inventing CPU or RAM minima.
- https://github.com/gyropilot/apple-lisafilemover/blob/5fe3ce40f6e3d744a2966f0c08b603ca249e302b/README.md

### AI (reviewed)

A primary icon-format analysis note explicitly credits Claude; this supports limited AI-use metadata for that documentation work, not a claim that the application code was AI-generated.
- https://github.com/gyropilot/apple-lisafilemover/blob/5fe3ce40f6e3d744a2966f0c08b603ca249e302b/README.md
- https://github.com/gyropilot/apple-lisafilemover/blob/5fe3ce40f6e3d744a2966f0c08b603ca249e302b/icon/LOS_ICON_FORMAT.txt

### Relationships (reviewed)

The README places LisaFileMover in the GyroPilot Lisa utility series and says its working-volume model derives from LISACom 1.6.
- https://github.com/gyropilot/apple-lisafilemover/blob/5fe3ce40f6e3d744a2966f0c08b603ca249e302b/README.md

## DAAD Reborn Compiler — modern DAAD compiler and media tools

Project ID: daad-reborn-compiler-drc · Overall audit: reviewed

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
  "display_title": "DAAD Reborn Compiler — modern DAAD compiler and media tools",
  "id": "daad-reborn-compiler-drc",
  "last_activity": "2026-09-26",
  "last_checked": "2026-10-31",
  "re_started": null,
  "reconstructed_languages": [
    "Pascal",
    "PHP"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/Utodev/DRC",
  "runtime_profiles": [
    {
      "evidence": [
        "https://github.com/Utodev/DRC/blob/71df4e54b7db39b5e7ceeb3b7e5d7dea1cebda95/README"
      ],
      "name": "DAAD Reborn Compiler",
      "notes": "README explicitly states these host OS families; no version, CPU or RAM floor is stated.",
      "os": "Windows, Linux or macOS",
      "platform": "Modern host"
    }
  ],
  "source_cpu": [],
  "source_language": [
    "DAAD source"
  ],
  "source_platforms": [
    "DAAD adventure source"
  ],
  "status": "Modern DAAD replacement compiler and CPC/Spectrum media tooling",
  "subjects": [
    "DAAD Reborn Compiler"
  ],
  "tags": [
    "daad",
    "adventure-authoring",
    "compiler"
  ],
  "target_cpu": [],
  "target_kinds": [],
  "target_platforms": [
    "ZX Spectrum",
    "Amstrad CPC",
    "Modern host"
  ],
  "techniques": [
    "DAAD compilation",
    "CPC MCRF replacement",
    "Spectrum tape/disk generation"
  ],
  "title": "DAAD Reborn Compiler — modern DAAD compiler and media tools",
  "tool_kinds": [
    "compiler-toolchain",
    "disk-filesystem-tool",
    "language-tooling"
  ],
  "types": [
    "retro adventure compiler",
    "media builder"
  ],
  "upstream_name": "DRC",
  "work_kinds": []
}
```

### Identity (reviewed)

DRC is the DAAD Reborn Compiler, a modern replacement for the historical DAAD compiler with companion CPC and Spectrum media tools.
- https://github.com/utodev/drc/blob/71df4e54b7db39b5e7ceeb3b7e5d7dea1cebda95/README

### Classification (reviewed)

It is maintained retro-development compiler/media tooling; the separate canonical DAAD archive remains a historical distribution source, not an interpreter-source project.
- https://github.com/utodev/drc/blob/71df4e54b7db39b5e7ceeb3b7e5d7dea1cebda95/README

### Source CPU (not-applicable)

Source CPU is not applicable because the reviewed input is DAAD adventure source/data rather than an original machine-code binary.
- https://github.com/utodev/drc/blob/71df4e54b7db39b5e7ceeb3b7e5d7dea1cebda95/README

### Target CPU (not-applicable)

Target CPU is not applicable: the documented compiler/media outputs are DAAD databases and tape/disk media, not evidence of native generated instruction sets.
- https://github.com/utodev/drc/blob/71df4e54b7db39b5e7ceeb3b7e5d7dea1cebda95/README

### Build (reviewed)

The README points to usage/build wiki material and downloads and states the compiler runs on modern desktop OSes; no local build or execution was performed. Limitations: Primary documentation/source-tree review only; compiler and generated media were not built or run.
- https://github.com/utodev/drc/blob/71df4e54b7db39b5e7ceeb3b7e5d7dea1cebda95/README

### Runtime profiles (reviewed)

Windows, Linux and macOS are captured as documented host families; no CPU, RAM or OS-version minimum is stated.
- https://github.com/utodev/drc/blob/71df4e54b7db39b5e7ceeb3b7e5d7dea1cebda95/README

### AI (no-evidence-found)

No explicit development-AI attribution was found in the reviewed primary documentation; this does not establish non-use.
- https://github.com/utodev/drc/blob/71df4e54b7db39b5e7ceeb3b7e5d7dea1cebda95/README

### Relationships (reviewed)

DRC replaces the historical DAAD compiler and includes a modern MCRF replacement and DAADMAKER; already tracked DAAD ecosystem tools remain separate projects.
- https://github.com/utodev/drc/blob/71df4e54b7db39b5e7ceeb3b7e5d7dea1cebda95/README

## DoSBoXIDA — DOSBox-X–based IDA debugger

Project ID: dsbxida-dosbox-x-ida-debugger · Overall audit: reviewed

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
  "display_title": "DoSBoXIDA — DOSBox-X–based IDA debugger",
  "id": "dsbxida-dosbox-x-ida-debugger",
  "last_activity": "2021-04-29",
  "last_checked": "2026-10-31",
  "re_started": null,
  "reconstructed_languages": [
    "C++"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/lab313ru/dsbxida",
  "runtime_profiles": [],
  "source_cpu": [
    "x86"
  ],
  "source_language": [
    "DOS x86 machine code"
  ],
  "source_platforms": [
    "DOS"
  ],
  "status": "DOSBox-X fork with independent IDA debugger plugin; not independently built",
  "subjects": [
    "MS-DOS programs"
  ],
  "tags": [
    "dos",
    "ida",
    "dosbox-x"
  ],
  "target_cpu": [],
  "target_kinds": [],
  "target_platforms": [
    "IDA",
    "Modern host"
  ],
  "techniques": [
    "IDA debugger API",
    "DOSBox callbacks",
    "segmented address translation"
  ],
  "title": "DoSBoXIDA — DOSBox-X–based IDA debugger",
  "tool_kinds": [
    "emulator",
    "debugger",
    "binary-analysis"
  ],
  "types": [
    "DOSBox-X fork",
    "IDA debugger plugin"
  ],
  "upstream_name": "dsbxida",
  "work_kinds": [
    "binary-analysis"
  ]
}
```

### Identity (reviewed)

DoSBoXIDA is a DOSBox-X-based project that connects MS-DOS program execution to IDA debugging.
- https://github.com/lab313ru/dsbxida/blob/eb452362a6bd188743df8524fb0b12cd4526babe/README.md

### Classification (reviewed)

Although it is a fork, the inspected dsbxida plugin implements its own IDA debugger integration and DOSBox callback handling, so it is a distinct archaeology tool rather than an ordinary mirror.
- https://github.com/lab313ru/dsbxida/blob/eb452362a6bd188743df8524fb0b12cd4526babe/README.md
- https://github.com/lab313ru/dsbxida/blob/eb452362a6bd188743df8524fb0b12cd4526babe/dsbxida/ida_plugin.cpp

### Source CPU (reviewed)

The README identifies MS-DOS programs and the plugin accepts DOS executable contexts through IDA's PC processor/debugger interfaces, supporting x86 source-program metadata.
- https://github.com/lab313ru/dsbxida/blob/eb452362a6bd188743df8524fb0b12cd4526babe/README.md
- https://github.com/lab313ru/dsbxida/blob/eb452362a6bd188743df8524fb0b12cd4526babe/dsbxida/ida_plugin.cpp

### Target CPU (no-evidence-found)

No native host/output CPU requirement was found; DOSBox-X lineage and IDA support do not establish a host architecture.
- https://github.com/lab313ru/dsbxida/blob/eb452362a6bd188743df8524fb0b12cd4526babe/README.md

### Build (reviewed)

The repository includes plugin and Visual Studio integration, but the README does not provide a complete reproducible build procedure and no build was run. Limitations: Static source review only; no IDA installation, plugin build, DOS program or emulator process was run.
- https://github.com/lab313ru/dsbxida/blob/eb452362a6bd188743df8524fb0b12cd4526babe/README.md
- https://github.com/lab313ru/dsbxida/blob/eb452362a6bd188743df8524fb0b12cd4526babe/dsbxida/ida_plugin.cpp

### Runtime profiles (no-evidence-found)

No minimum IDA, host OS, CPU or RAM requirement was established from the inspected primary files.
- https://github.com/lab313ru/dsbxida/blob/eb452362a6bd188743df8524fb0b12cd4526babe/README.md

### AI (no-evidence-found)

No explicit development-AI attribution was found in the reviewed primary documentation or plugin source; this does not establish non-use.
- https://github.com/lab313ru/dsbxida/blob/eb452362a6bd188743df8524fb0b12cd4526babe/README.md

### Relationships (reviewed)

The older idados_dosbox README names dsbxida as its successor; dsbxida is based on DOSBox-X and carries the current independent plugin implementation.
- https://github.com/lab313ru/dsbxida/blob/eb452362a6bd188743df8524fb0b12cd4526babe/README.md
- https://github.com/lab313ru/dsbxida/blob/eb452362a6bd188743df8524fb0b12cd4526babe/dsbxida/ida_plugin.cpp

## NeoWidEx — Apple Lisa Widget diagnostics and formatter

Project ID: neowidex-apple-lisa-widget-utility · Overall audit: reviewed

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
  "display_title": "NeoWidEx — Apple Lisa Widget diagnostics and formatter",
  "id": "neowidex-apple-lisa-widget-utility",
  "last_activity": "2020-04-18",
  "last_checked": "2026-10-31",
  "re_started": null,
  "reconstructed_languages": [
    "Motorola 68000 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/stepleton/NeoWidEx",
  "runtime_profiles": [
    {
      "evidence": [
        "https://github.com/stepleton/NeoWidEx/blob/5e41885791b56299c3944c273e0b08dc93e13116/README.md"
      ],
      "name": "NeoWidEx 0.4",
      "notes": "Requires a working floppy drive or emulator; Lisa 2/5 can access only external-port drives and most options require a Widget.",
      "os": "Lisa 2 ROM version H",
      "platform": "Apple Lisa 2"
    }
  ],
  "source_cpu": [],
  "source_language": [
    "Widget commands and disk structures"
  ],
  "source_platforms": [
    "Apple Lisa Widget drive"
  ],
  "status": "Original Lisa Widget diagnostic/formatter with documented 68000 build and hardware requirements",
  "subjects": [
    "NeoWidEx"
  ],
  "tags": [
    "apple-lisa",
    "widget",
    "original-homebrew"
  ],
  "target_cpu": [
    "Motorola 68000"
  ],
  "target_kinds": [
    "application",
    "development-tool"
  ],
  "target_platforms": [
    "Apple Lisa 2/10",
    "Apple Lisa 2/5"
  ],
  "techniques": [
    "low-level Widget commands",
    "EASy68K assembly",
    "bootable DC42 generation"
  ],
  "title": "NeoWidEx — Apple Lisa Widget diagnostics and formatter",
  "tool_kinds": [],
  "types": [
    "original homebrew",
    "drive diagnostic",
    "low-level formatter"
  ],
  "upstream_name": "NeoWidEx",
  "work_kinds": []
}
```

### Identity (reviewed)

NeoWidEx is a low-level formatting and diagnostic utility for Apple's 10 MB Widget hard drive on Lisa 2 systems.
- https://github.com/stepleton/neowidex/blob/5e41885791b56299c3944c273e0b08dc93e13116/README.md

### Classification (reviewed)

It is substantial original homebrew and hardware-development software, not a reverse-engineered application or RE-derived port.
- https://github.com/stepleton/neowidex/blob/5e41885791b56299c3944c273e0b08dc93e13116/README.md

### Source CPU (not-applicable)

Source CPU is not applicable because NeoWidEx is original software rather than analysis of a pre-existing binary.
- https://github.com/stepleton/neowidex/blob/5e41885791b56299c3944c273e0b08dc93e13116/README.md

### Target CPU (reviewed)

The repository explicitly describes roughly 10,000 lines of 68000 macro assembly and a native Lisa boot image, supporting Motorola 68000 target metadata.
- https://github.com/stepleton/neowidex/blob/5e41885791b56299c3944c273e0b08dc93e13116/README.md
- https://github.com/stepleton/neowidex/blob/5e41885791b56299c3944c273e0b08dc93e13116/BUILDING.md

### Build (reviewed)

BUILDING documents EASy68K assembly, srec_cat conversion at address $800 and bootable DC42 generation with the Stepleton bootloader; no step was executed here. Limitations: Read-only documentation review; destructive drive operations, assembly, boot image generation and hardware/emulator execution were not performed.
- https://github.com/stepleton/neowidex/blob/5e41885791b56299c3944c273e0b08dc93e13116/README.md
- https://github.com/stepleton/neowidex/blob/5e41885791b56299c3944c273e0b08dc93e13116/BUILDING.md

### Runtime profiles (reviewed)

The README's ROM, floppy/emulator and Widget access requirements are captured exactly; no CPU or RAM minimum is inferred.
- https://github.com/stepleton/neowidex/blob/5e41885791b56299c3944c273e0b08dc93e13116/README.md

### AI (no-evidence-found)

No explicit development-AI attribution was found in the reviewed README/build documentation; this does not establish non-use.
- https://github.com/stepleton/neowidex/blob/5e41885791b56299c3944c273e0b08dc93e13116/README.md

### Relationships (reviewed)

The README distinguishes NeoWidEx from Apple's Widex and credits related BLU/UsbWidEx work without claiming shared source.
- https://github.com/stepleton/neowidex/blob/5e41885791b56299c3944c273e0b08dc93e13116/README.md
- https://github.com/stepleton/neowidex/blob/5e41885791b56299c3944c273e0b08dc93e13116/BUILDING.md

## 180-spectrum

Project ID: 180-spectrum · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "build": {
    "byte_exact": null,
    "compilable": null,
    "playable": null,
    "runnable": null
  },
  "id": "180-spectrum",
  "last_checked": "2026-10-31",
  "runtime_profiles": [],
  "status": "Primary source documents a SkoolKit HTML disassembly build; no reconstructed binary/runtime claim"
}
```

Expected existing project SHA256: 6db545363b88addc9ff5d735d39b7b369760c0add744238fb113af14a5a161e9

### Identity (reviewed)

Pobtastic's 180 repository remains the canonical SkoolKit disassembly of the 1986 ZX Spectrum game.
- https://github.com/pobtastic/180/blob/b59f6d00c1afa39c1cafe3ce2649c3d33c41b3d5/README.md

### Classification (reviewed)

The record remains a subject disassembly, not original homebrew and not a native modern port.
- https://github.com/pobtastic/180/blob/b59f6d00c1afa39c1cafe3ce2649c3d33c41b3d5/README.md

### Source CPU (reviewed)

The original/source architecture remains Z80, as established by the ZX Spectrum machine-code disassembly context.
- https://github.com/pobtastic/180/blob/b59f6d00c1afa39c1cafe3ce2649c3d33c41b3d5/README.md

### Target CPU (not-applicable)

Target CPU is not applicable: the documented output is browsable HTML disassembly, not a rebuilt native executable.
- https://github.com/pobtastic/180/blob/b59f6d00c1afa39c1cafe3ce2649c3d33c41b3d5/README.md

### Build (reviewed)

The README documents installing/cloning SkoolKit and running utils/mkhtml.py to build the current HTML development version; the Makefile delegates to SkoolKit's disassembly framework. It does not claim a rebuilt runnable binary or byte identity. Limitations: No SkoolKit command, original-game extraction, assembly, executable or emulator was run.
- https://github.com/pobtastic/180/blob/b59f6d00c1afa39c1cafe3ce2649c3d33c41b3d5/README.md
- https://github.com/pobtastic/180/blob/b59f6d00c1afa39c1cafe3ce2649c3d33c41b3d5/Makefile

### Runtime profiles (no-evidence-found)

No reconstructed runnable build or minimum hardware requirement is documented; the original game is required as disassembly input.
- https://github.com/pobtastic/180/blob/b59f6d00c1afa39c1cafe3ce2649c3d33c41b3d5/README.md

### AI (no-evidence-found)

No explicit development-AI attribution was found in the reviewed primary files; this does not establish non-use.
- https://github.com/pobtastic/180/blob/b59f6d00c1afa39c1cafe3ce2649c3d33c41b3d5/README.md

### Relationships (reviewed)

The README links SkoolKit, the hosted disassembly and an external mirror; these are tool/output relationships, not separate reconstruction projects.
- https://github.com/pobtastic/180/blob/b59f6d00c1afa39c1cafe3ce2649c3d33c41b3d5/README.md
- https://github.com/pobtastic/180/blob/b59f6d00c1afa39c1cafe3ce2649c3d33c41b3d5/Makefile

## Pinned evidence manifest

- arem_code: https://github.com/bver/arem-mzf-parser/blob/7d798c1431f05c99fb4fa20415aa730b0b00075c/arem_src_parse.rb (Git blob 7296ea0ca7a5673dde89a1666ec62341348e20e7)
- arem_readme: https://github.com/bver/arem-mzf-parser/blob/7d798c1431f05c99fb4fa20415aa730b0b00075c/README.md (Git blob 530998c4b3891cb2937132f83aa6c3ac763aa39d)
- crayon_readme: https://github.com/qam4/crayon/blob/136d6b9c49076485abc48e1d9fed62293231f36d/README.md (Git blob cf8f0dd4afa36375364a0d25ace2bf34eb0e3864)
- drc_readme: https://github.com/utodev/drc/blob/71df4e54b7db39b5e7ceeb3b7e5d7dea1cebda95/README (Git blob a66ae356e69b406209de1c5842bf316b0ad19291)
- dsbxida_plugin: https://github.com/lab313ru/dsbxida/blob/eb452362a6bd188743df8524fb0b12cd4526babe/dsbxida/ida_plugin.cpp (Git blob 45066376ec26024bc14709115b1e75d89558f71c)
- dsbxida_readme: https://github.com/lab313ru/dsbxida/blob/eb452362a6bd188743df8524fb0b12cd4526babe/README.md (Git blob 86c4a6e282879048e8dd8252a1d2c4b3ec655c2c)
- lisa_utils_readme: https://github.com/d235j/lisa-utilities/blob/d79ac35fdc366c49ed16c6a9d3948809862c7f68/README.md (Git blob 6a4b3e4659b7c568c4a08940c34c7eb0f5ac34b1)
- lisamover_icon: https://github.com/gyropilot/apple-lisafilemover/blob/5fe3ce40f6e3d744a2966f0c08b603ca249e302b/icon/LOS_ICON_FORMAT.txt (Git blob b8b01ba28ad9cab8dce0a8ed9abb7448a0bff307)
- lisamover_readme: https://github.com/gyropilot/apple-lisafilemover/blob/5fe3ce40f6e3d744a2966f0c08b603ca249e302b/README.md (Git blob a248bd9f13d6d95e16c142ad71528d854a7a4853)
- mz_readme: https://github.com/lukq/mz-basictoqd/blob/455203562a112b14d0411dc49dee0a780686e5c2/Readme.md (Git blob 773417cdc60a90164373e9a3f202844a7e441b43)
- neowidex_building: https://github.com/stepleton/neowidex/blob/5e41885791b56299c3944c273e0b08dc93e13116/BUILDING.md (Git blob 2497b3895f3f5b6aeac8895976f7679e44b76e05)
- neowidex_readme: https://github.com/stepleton/neowidex/blob/5e41885791b56299c3944c273e0b08dc93e13116/README.md (Git blob ee40ba0529c767e3a55e36f51c19ca50cf64e96c)
- pobtastic_makefile: https://github.com/pobtastic/180/blob/b59f6d00c1afa39c1cafe3ce2649c3d33c41b3d5/Makefile (Git blob 5f74017fb7820f8541d473c322dff02a8fb322e7)
- pobtastic_readme: https://github.com/pobtastic/180/blob/b59f6d00c1afa39c1cafe3ce2649c3d33c41b3d5/README.md (Git blob fd595c7c09359ead438b1e9d9bb68637061fbf08)
- theodore_readme: https://github.com/zlika/theodore/blob/4d469ce0f71ee046ceb78cdbf8e9f18364aaa918/README.md (Git blob e2e27dd90e70906c93cdbf504388f3a05a1f30b9)

## Sources

```json
[
  {
    "id": "github-lukq-mz-basictoqd",
    "kind": "github-repository",
    "reason": "Sharp MZ BASIC text/media converter and listing utility reviewed from README.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/lukq/mz-basictoqd"
  },
  {
    "id": "github-bver-arem-mzf-parser",
    "kind": "github-repository",
    "reason": "Sharp MZ-800 AREM binary source parser reviewed from README and implementation.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/bver/arem-mzf-parser"
  },
  {
    "id": "github-zlika-theodore",
    "kind": "github-repository",
    "reason": "Maintained Thomson MO/TO libretro emulator and debugger reviewed from primary documentation.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/Zlika/theodore"
  },
  {
    "id": "github-qam4-crayon",
    "kind": "github-repository",
    "reason": "Thomson MO5 emulator/debugger reviewed with explicit build and ROM requirements.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/qam4/crayon"
  },
  {
    "id": "github-d235j-lisa-utilities",
    "kind": "github-repository",
    "reason": "Apple Lisa Monitor disk-image extraction utility reviewed from primary documentation.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/d235j/lisa-utilities"
  },
  {
    "id": "github-gyropilot-apple-lisafilemover",
    "kind": "github-repository",
    "reason": "Native Lisa Office System file utility reviewed with build, runtime and AI evidence.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/GyroPilot/Apple-LisaFileMover"
  },
  {
    "id": "github-lab313ru-dsbxida",
    "kind": "github-repository",
    "reason": "DOSBox-X/IDA debugger successor reviewed from README and independent plugin implementation.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/lab313ru/dsbxida"
  }
]
```

## Source updates

```json
[
  {
    "id": "github-utodev-drc",
    "last_reviewed": "2026-10-31",
    "reason": "DRC implementation and primary README reviewed as a modern DAAD compiler plus CPC/Spectrum media tooling; promoted as a coherent toolchain root.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-daad-adventure-writer-daad",
    "last_reviewed": "2026-10-31",
    "reason": "Canonical DAAD archive retained as historical distribution/discovery context; its README says interpreter source is absent, while maintained compiler work is tracked under DRC.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-stepleton-neowidex",
    "last_reviewed": "2026-10-31",
    "reason": "Implementation, 68000 build path and exact Lisa ROM/floppy/Widget requirements reviewed; promoted as original native Lisa development software.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-lab313ru",
    "last_reviewed": "2026-10-31",
    "reason": "DoSBoXIDA successor follow-up completed and promoted; other profile-adjacent retro tooling remains open for later review.",
    "review_state": "partial"
  },
  {
    "id": "github-idados-dosbox",
    "last_reviewed": "2026-10-31",
    "reason": "Historical idados_dosbox predecessor retained as reference; its named successor lab313ru/dsbxida has now been reviewed and promoted.",
    "review_state": "substantially-reviewed"
  }
]
```

## Task updates

```json
[
  {
    "id": "task-review-daad-drc-toolchain-graph",
    "last_reviewed": "2026-10-31",
    "notes_append": "Reviewed canonical DAAD and DRC roots. DAAD remains a historical distribution source whose README says interpreter source is absent; DRC is promoted as the maintained replacement compiler and media-tool root.",
    "state": "done"
  },
  {
    "id": "research-dsbxida-successor",
    "last_reviewed": "2026-10-31",
    "notes_append": "Reviewed dsbxida at eb452362, verified DOSBox-X lineage and an independent IDA debugger plugin implementation, and promoted the successor.",
    "state": "done"
  },
  {
    "id": "task-review-neowidex-lisa-widget-utility",
    "last_reviewed": "2026-10-31",
    "notes_append": "Reviewed README and BUILDING at 5e418857; promoted as original native Lisa homebrew with explicit 68000 build and ROM/floppy/Widget requirements.",
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
      "https://github.com/lukq/mz-basictoqd/blob/455203562a112b14d0411dc49dee0a780686e5c2/Readme.md"
    ],
    "id": "discovery-2026-10-31-mz-basictoqd-promoted",
    "project_ids": [
      "mz-basictoqd-sharp-mz-transfer-tool"
    ],
    "reason": "Verified Sharp MZ BASIC media-transfer and listing tooling.",
    "source_ids": [
      "github-lukq-mz-basictoqd"
    ],
    "title": "BASIC to QD",
    "url": "https://github.com/lukq/mz-basictoqd"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/bver/arem-mzf-parser/blob/7d798c1431f05c99fb4fa20415aa730b0b00075c/README.md"
    ],
    "id": "discovery-2026-10-31-arem-mzf-parser-promoted",
    "project_ids": [
      "arem-mzf-parser-sharp-mz800"
    ],
    "reason": "Verified AREM/MZF source-recovery parser with Z80-aware implementation.",
    "source_ids": [
      "github-bver-arem-mzf-parser"
    ],
    "title": "AREM MZF Parser",
    "url": "https://github.com/bver/arem-mzf-parser"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/Zlika/theodore/blob/4d469ce0f71ee046ceb78cdbf8e9f18364aaa918/README.md"
    ],
    "id": "discovery-2026-10-31-theodore-promoted",
    "project_ids": [
      "theodore-thomson-libretro-debugger"
    ],
    "reason": "Verified maintained Thomson emulator with debugger/disassembler capabilities.",
    "source_ids": [
      "github-zlika-theodore"
    ],
    "title": "Theodore",
    "url": "https://github.com/Zlika/theodore"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/qam4/crayon/blob/136d6b9c49076485abc48e1d9fed62293231f36d/README.md"
    ],
    "id": "discovery-2026-10-31-crayon-promoted",
    "project_ids": [
      "crayon-thomson-mo5-emulator-debugger"
    ],
    "reason": "Verified distinct MO5 emulator/debugger with explicit build and ROM documentation.",
    "source_ids": [
      "github-qam4-crayon"
    ],
    "title": "Crayon",
    "url": "https://github.com/qam4/crayon"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/d235j/lisa-utilities/blob/d79ac35fdc366c49ed16c6a9d3948809862c7f68/README.md"
    ],
    "id": "discovery-2026-10-31-lisa-utilities-promoted",
    "project_ids": [
      "lisa-utilities-monitor-image-extractor"
    ],
    "reason": "Verified Lisa Monitor disk-image preservation utility.",
    "source_ids": [
      "github-d235j-lisa-utilities"
    ],
    "title": "Lisa Utilities",
    "url": "https://github.com/d235j/lisa-utilities"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/GyroPilot/Apple-LisaFileMover/blob/5fe3ce40f6e3d744a2966f0c08b603ca249e302b/README.md"
    ],
    "id": "discovery-2026-10-31-lisafilemover-promoted",
    "project_ids": [
      "lisafilemover-native-lisa-utility"
    ],
    "reason": "Verified substantial original native Lisa Office System application.",
    "source_ids": [
      "github-gyropilot-apple-lisafilemover"
    ],
    "title": "LisaFileMover",
    "url": "https://github.com/GyroPilot/Apple-LisaFileMover"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/Utodev/DRC/blob/71df4e54b7db39b5e7ceeb3b7e5d7dea1cebda95/README"
    ],
    "id": "discovery-2026-10-31-drc-promoted",
    "project_ids": [
      "daad-reborn-compiler-drc"
    ],
    "reason": "Verified modern DAAD compiler and media-tool root; historical interpreter archive kept separate.",
    "source_ids": [
      "github-utodev-drc"
    ],
    "title": "DAAD Reborn Compiler",
    "url": "https://github.com/Utodev/DRC"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/lab313ru/dsbxida/blob/eb452362a6bd188743df8524fb0b12cd4526babe/README.md"
    ],
    "id": "discovery-2026-10-31-dsbxida-promoted",
    "project_ids": [
      "dsbxida-dosbox-x-ida-debugger"
    ],
    "reason": "Verified successor fork with an independent IDA debugger plugin.",
    "source_ids": [
      "github-lab313ru-dsbxida"
    ],
    "title": "DoSBoXIDA",
    "url": "https://github.com/lab313ru/dsbxida"
  }
]
```

## Research event notes

CPU queue returned zero unresolved source/target areas, so no CPU value was inferred merely to satisfy a quota. Fresh GitHub repository/README searches were: '"Sharp MZ" disassembly source reconstruction', '"Thomson MO5" source homebrew tooling', '"Enterprise 128" source port Z80', '"Apple Lisa" assembly source utility', then broadened to 'Sharp MZ source', 'Thomson MO5 emulator', 'Enterprise 128 homebrew', and 'Apple Lisa utility'. Reviewed/promoted: lukq/mz-basictoqd, bver/arem-mzf-parser, Zlika/theodore, qam4/crayon, d235j/lisa-utilities, GyroPilot/Apple-LisaFileMover, Utodev/DRC, lab313ru/dsbxida and stepleton/NeoWidEx. Known results michalhucik/mz800emu and kpouer/Maurice were duplicates of indexed projects; the Enterprise searches returned no promotable candidate. NeoWidEx supersedes its 2026-10-10 deferred review without erasing that historical decision. Pobtastic 180 was re-audited after upstream activity. Read-only review: no upstream code, compiler, emulator, ROM, image, device or destructive utility was run.
