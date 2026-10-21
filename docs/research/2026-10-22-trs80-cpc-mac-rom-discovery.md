# Review a queue-led preservation task and three rotated fresh searches; add six source-backed projects, retain one curated index and close the Follin component-splitting task.

Review a queue-led preservation task and three rotated fresh searches; add six source-backed projects, retain one curated index and close the Follin component-splitting task.

Date: 2026-10-22 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- sharp-pc1500-rom-disassembly / Build (reviewed): The tracker did not execute TASM or compare the generated binaries with Original_ROMs; runtime and byte identity remain unknown.
- sharp-pc1500-rom-disassembly / Runtime profiles (no-evidence-found): The reviewed README, assembly and build script establish ROM targets but do not state minimum machine, RAM or peripheral requirements beyond product identity.
- sharp-pc1500-rom-disassembly / AI (no-evidence-found): The inspected README, source and build script contain no development-AI disclosure; absence does not establish non-use.
- calvados-genie-iiis-reconstruction / Build (reviewed): One known defect remains open, and the tracker did not independently assemble or boot the system.
- calvados-genie-iiis-reconstruction / AI (no-evidence-found): The reviewed README describes the manual tools and sources used but contains no development-AI disclosure; absence does not establish non-use.
- paket-adventure-game-compiler / Build (reviewed): The tracker did not compile the Java tool or execute a generated game.
- paket-adventure-game-compiler / Runtime profiles (no-evidence-found): The reviewed documentation names CPC 464 and MSX targets but gives no explicit minimum RAM, model revision or OS/ROM requirements suitable for a compatibility profile.
- paket-adventure-game-compiler / AI (no-evidence-found): The inspected README and target sources contain no development-AI disclosure; absence does not establish non-use.
- rom-fiend-macintosh-rom-template / Build (reviewed): The tracker did not install the template or parse a ROM.
- rom-fiend-macintosh-rom-template / Runtime profiles (no-evidence-found): The README requires Hex Fiend but gives no explicit host OS version, CPU or memory minimum; target Macintosh hardware requirements do not apply to the analysis template.
- rom-fiend-macintosh-rom-template / AI (no-evidence-found): The inspected README and template contain no development-AI disclosure; absence does not establish non-use.
- df80-cpm-fortran80-disassembly / Build (reviewed): Byte identity is an author claim; the tracker did not run M80/L80 or compare binaries.
- df80-cpm-fortran80-disassembly / Runtime profiles (no-evidence-found): The project identifies CP/M executables but gives no minimum CP/M version, RAM, machine model or operating environment.
- df80-cpm-fortran80-disassembly / AI (no-evidence-found): The inspected README and recovered source contain no development-AI disclosure; absence does not establish non-use.
- computer-archeology-disassemblies-toolchain / Build (reviewed): The tracker did not execute the renderer or validate individual title binaries.
- computer-archeology-disassemblies-toolchain / Runtime profiles (no-evidence-found): The reviewed root documentation does not provide host CPU, RAM or Python-version minima for the analysis/rendering toolchain.
- computer-archeology-disassemblies-toolchain / AI (no-evidence-found): The inspected root documentation and tooling source contain no development-AI disclosure; absence does not establish non-use.
- follin-music-source-archive / Build (reviewed): The tracker did not build the examples, and no compile claim is generalized to every disk or title.
- follin-music-source-archive / AI (no-evidence-found): The README and reviewed archive structure contain no development-AI disclosure; absence does not establish non-use.

## Sharp PC-1500 / TRS-80 PC-2 ROM disassembly

Project ID: sharp-pc1500-rom-disassembly · Overall audit: reviewed

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
  "display_title": "Sharp PC-1500 / TRS-80 PC-2 ROM disassembly",
  "id": "sharp-pc1500-rom-disassembly",
  "last_activity": "2024-12-25",
  "last_checked": "2026-10-22",
  "re_started": null,
  "reconstructed_languages": [
    "LH5801 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/Jeff-Birt/Sharp_PC-1500_ROM_Disassembly",
  "runtime_profiles": [],
  "source_cpu": [
    "LH5801"
  ],
  "source_language": [],
  "source_platforms": [
    "Sharp PC-1500",
    "TRS-80 PC-2"
  ],
  "status": "Documented TASM rebuild; not independently built",
  "subjects": [
    "Sharp PC-1500 A01/A03/A04 ROMs",
    "TRS-80 PC-2 ROMs"
  ],
  "tags": [
    "Sharp PC-1500",
    "TRS-80 PC-2",
    "LH5801",
    "ROM"
  ],
  "target_cpu": [
    "LH5801"
  ],
  "target_kinds": [
    "firmware-rom"
  ],
  "target_platforms": [
    "Sharp PC-1500",
    "TRS-80 PC-2"
  ],
  "techniques": [
    "multi-revision conditional assembly",
    "cross-assembly"
  ],
  "title": "Sharp PC-1500 ROM Disassembly",
  "tool_kinds": [],
  "types": [
    "ROM disassembly"
  ],
  "upstream_name": "Sharp PC-1500 ROM Disassembly",
  "work_kinds": [
    "disassembly",
    "source-reconstruction"
  ]
}
```

### Identity (reviewed)

The README identifies one LH5801 assembly reconstruction covering the A01, A03 and A04 Sharp PC-1500 ROM revisions, also applicable to the Radio Shack TRS-80 PC-2 lineage.
- https://github.com/Jeff-Birt/Sharp_PC-1500_ROM_Disassembly/blob/5a5f8aa9ba52e239cc224c3a2e48bde9299b4f3e/README.md
- https://github.com/Jeff-Birt/Sharp_PC-1500_ROM_Disassembly/blob/5a5f8aa9ba52e239cc224c3a2e48bde9299b4f3e/PC-1500_ROM-A0x.lh5801.asm

### Classification (reviewed)

This is a ROM disassembly/reconstruction with revision-selectable source and generated binaries; it is not presented as recovered original Sharp source.
- https://github.com/Jeff-Birt/Sharp_PC-1500_ROM_Disassembly/blob/5a5f8aa9ba52e239cc224c3a2e48bde9299b4f3e/README.md
- https://github.com/Jeff-Birt/Sharp_PC-1500_ROM_Disassembly/blob/5a5f8aa9ba52e239cc224c3a2e48bde9299b4f3e/PC-1500_ROM-A0x.lh5801.asm

### Source CPU (reviewed)

The primary assembly filename, source comments and TASM build switch explicitly identify the historical ROM instruction set as Sharp LH5801.
- https://github.com/Jeff-Birt/Sharp_PC-1500_ROM_Disassembly/blob/5a5f8aa9ba52e239cc224c3a2e48bde9299b4f3e/PC-1500_ROM-A0x.lh5801.asm
- https://github.com/Jeff-Birt/Sharp_PC-1500_ROM_Disassembly/blob/5a5f8aa9ba52e239cc224c3a2e48bde9299b4f3e/build.bat

### Target CPU (reviewed)

The documented build invokes TASM's 5801 table and emits PC-1500 ROM binaries, explicitly retaining LH5801 as the output architecture.
- https://github.com/Jeff-Birt/Sharp_PC-1500_ROM_Disassembly/blob/5a5f8aa9ba52e239cc224c3a2e48bde9299b4f3e/README.md
- https://github.com/Jeff-Birt/Sharp_PC-1500_ROM_Disassembly/blob/5a5f8aa9ba52e239cc224c3a2e48bde9299b4f3e/build.bat

### Build (reviewed)

The README and batch script document TASM commands for A01, A03 and A04 outputs and the repository contains generated BIN/LST files. Limitations: The tracker did not execute TASM or compare the generated binaries with Original_ROMs; runtime and byte identity remain unknown.
- https://github.com/Jeff-Birt/Sharp_PC-1500_ROM_Disassembly/blob/5a5f8aa9ba52e239cc224c3a2e48bde9299b4f3e/README.md
- https://github.com/Jeff-Birt/Sharp_PC-1500_ROM_Disassembly/blob/5a5f8aa9ba52e239cc224c3a2e48bde9299b4f3e/build.bat

### Runtime profiles (no-evidence-found)

The reviewed README, assembly and build script establish ROM targets but do not state minimum machine, RAM or peripheral requirements beyond product identity.
- https://github.com/Jeff-Birt/Sharp_PC-1500_ROM_Disassembly/blob/5a5f8aa9ba52e239cc224c3a2e48bde9299b4f3e/README.md
- https://github.com/Jeff-Birt/Sharp_PC-1500_ROM_Disassembly/blob/5a5f8aa9ba52e239cc224c3a2e48bde9299b4f3e/PC-1500_ROM-A0x.lh5801.asm
- https://github.com/Jeff-Birt/Sharp_PC-1500_ROM_Disassembly/blob/5a5f8aa9ba52e239cc224c3a2e48bde9299b4f3e/build.bat

### AI (no-evidence-found)

The inspected README, source and build script contain no development-AI disclosure; absence does not establish non-use.
- https://github.com/Jeff-Birt/Sharp_PC-1500_ROM_Disassembly/blob/5a5f8aa9ba52e239cc224c3a2e48bde9299b4f3e/README.md
- https://github.com/Jeff-Birt/Sharp_PC-1500_ROM_Disassembly/blob/5a5f8aa9ba52e239cc224c3a2e48bde9299b4f3e/PC-1500_ROM-A0x.lh5801.asm
- https://github.com/Jeff-Birt/Sharp_PC-1500_ROM_Disassembly/blob/5a5f8aa9ba52e239cc224c3a2e48bde9299b4f3e/build.bat

### Relationships (reviewed)

The repository treats Sharp PC-1500 and Radio Shack TRS-80 PC-2 as the same ROM-family subject and keeps the three published ROM revisions in one coherent source file.
- https://github.com/Jeff-Birt/Sharp_PC-1500_ROM_Disassembly/blob/5a5f8aa9ba52e239cc224c3a2e48bde9299b4f3e/README.md
- https://github.com/Jeff-Birt/Sharp_PC-1500_ROM_Disassembly/blob/5a5f8aa9ba52e239cc224c3a2e48bde9299b4f3e/PC-1500_ROM-A0x.lh5801.asm

## CalvaDOS — Genie IIIs hard-disk OS reconstruction

Project ID: calvados-genie-iiis-reconstruction · Overall audit: reviewed

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
  "display_title": "CalvaDOS — Genie IIIs hard-disk OS reconstruction",
  "id": "calvados-genie-iiis-reconstruction",
  "last_activity": "2026-09-03",
  "last_checked": "2026-10-22",
  "re_started": null,
  "reconstructed_languages": [
    "Z80 assembly",
    "shell"
  ],
  "record_class": "subject",
  "repo": "https://github.com/Egbert-Azure/TCS-Trommeschlaeger-Genie-IIIs-CalvaDOS",
  "runtime_profiles": [
    {
      "cpu_family": "Z80",
      "evidence": [
        "https://github.com/Egbert-Azure/TCS-Trommeschlaeger-Genie-IIIs-CalvaDOS/blob/52fb7c1ff3135a177ec54e182a2676f35608128b/README.md"
      ],
      "name": "Stage B reconstruction",
      "notes": "Documented boot path uses the reconstructed Stage B OMTI hard-disk system; it runs on a physical Genie IIIs via the patch disk or under sdltrs-MultiHDC. No RAM floor is stated.",
      "os": "CalvaDOS / G-DOS 2.4",
      "platform": "TCS Genie IIIs"
    }
  ],
  "source_cpu": [
    "Z80"
  ],
  "source_language": [
    "surviving Z80 assembly",
    "historical binaries"
  ],
  "source_platforms": [
    "TCS Genie IIIs"
  ],
  "status": "Stage B boots and reads a real hard-disk directory according to the author",
  "subjects": [
    "CalvaDOS",
    "G-DOS 2.4 hard-disk extensions"
  ],
  "tags": [
    "Genie IIIs",
    "G-DOS",
    "Z80",
    "preservation"
  ],
  "target_cpu": [
    "Z80"
  ],
  "target_kinds": [
    "system-software",
    "firmware-rom"
  ],
  "target_platforms": [
    "TCS Genie IIIs"
  ],
  "techniques": [
    "artifact comparison",
    "disassembly",
    "byte diffing",
    "emulator debugging"
  ],
  "title": "CalvaDOS",
  "tool_kinds": [],
  "types": [
    "operating-system reconstruction",
    "software preservation"
  ],
  "upstream_name": "CalvaDOS",
  "work_kinds": [
    "source-reconstruction",
    "source-restoration",
    "binary-analysis"
  ]
}
```

### Identity (reviewed)

The project explicitly reconstructs the lost Stage B CalvaDOS modification for the TCS Genie IIIs from surviving GDOS material, an OMTI boot EPROM, work disks and period documentation.
- https://github.com/Egbert-Azure/TCS-Trommeschlaeger-Genie-IIIs-CalvaDOS/blob/52fb7c1ff3135a177ec54e182a2676f35608128b/README.md

### Classification (reviewed)

The README repeatedly distinguishes this reconstruction from the unrecovered 1986 binaries and separates new BSD-licensed code from preserved third-party G-DOS-derived material.
- https://github.com/Egbert-Azure/TCS-Trommeschlaeger-Genie-IIIs-CalvaDOS/blob/52fb7c1ff3135a177ec54e182a2676f35608128b/README.md

### Source CPU (reviewed)

The README identifies the Genie IIIs as a Z80 machine and documents Z80 disassembly/assembly as the reconstruction basis.
- https://github.com/Egbert-Azure/TCS-Trommeschlaeger-Genie-IIIs-CalvaDOS/blob/52fb7c1ff3135a177ec54e182a2676f35608128b/README.md

### Target CPU (reviewed)

The reconstructed Stage B system and boot EPROM target the same Z80-based Genie IIIs hardware; no host CPU is substituted.
- https://github.com/Egbert-Azure/TCS-Trommeschlaeger-Genie-IIIs-CalvaDOS/blob/52fb7c1ff3135a177ec54e182a2676f35608128b/README.md

### Build (reviewed)

The author reports that the reconstruction boots from hard disk, reaches a command prompt, reads volume 5 and creates RAMDISK; source, disk images and build tools are present. Limitations: One known defect remains open, and the tracker did not independently assemble or boot the system.
- https://github.com/Egbert-Azure/TCS-Trommeschlaeger-Genie-IIIs-CalvaDOS/blob/52fb7c1ff3135a177ec54e182a2676f35608128b/README.md

### Runtime profiles (reviewed)

The README documents physical Genie IIIs and sdltrs-MultiHDC execution paths for the Stage B OMTI reconstruction, but states no minimum RAM.
- https://github.com/Egbert-Azure/TCS-Trommeschlaeger-Genie-IIIs-CalvaDOS/blob/52fb7c1ff3135a177ec54e182a2676f35608128b/README.md

### AI (no-evidence-found)

The reviewed README describes the manual tools and sources used but contains no development-AI disclosure; absence does not establish non-use.
- https://github.com/Egbert-Azure/TCS-Trommeschlaeger-Genie-IIIs-CalvaDOS/blob/52fb7c1ff3135a177ec54e182a2676f35608128b/README.md

### Relationships (reviewed)

CalvaDOS is reconstructed from stock G-DOS 2.4 plus surviving Club80-era hard-disk modifications; related emulator, stock-GDOS and disk-extraction repositories are explicitly named without being collapsed into this record.
- https://github.com/Egbert-Azure/TCS-Trommeschlaeger-Genie-IIIs-CalvaDOS/blob/52fb7c1ff3135a177ec54e182a2676f35608128b/README.md

## PAKET — CPC/MSX point-and-click adventure compiler

Project ID: paket-adventure-game-compiler · Overall audit: reviewed

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
  "display_title": "PAKET — CPC/MSX point-and-click adventure compiler",
  "id": "paket-adventure-game-compiler",
  "last_activity": "2026-10-17",
  "last_checked": "2026-10-22",
  "re_started": null,
  "reconstructed_languages": [
    "Java",
    "Z80 assembly"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/santiontanon/paket",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Version 1.0 compiler with documented CPC 464 and MSX outputs",
  "subjects": [
    "PAKET game definition language and compiler"
  ],
  "tags": [
    "Amstrad CPC",
    "MSX",
    "Z80",
    "adventure engine"
  ],
  "target_cpu": [
    "Z80"
  ],
  "target_kinds": [
    "game-engine"
  ],
  "target_platforms": [
    "Amstrad CPC 464",
    "MSX"
  ],
  "techniques": [
    "domain-specific language",
    "cross-compilation",
    "firmware-derived tape routines"
  ],
  "title": "PAKET",
  "tool_kinds": [
    "compiler-toolchain",
    "language-tooling",
    "asset-tool"
  ],
  "types": [
    "retro game-development toolkit"
  ],
  "upstream_name": "PAKET",
  "work_kinds": []
}
```

### Identity (reviewed)

The README identifies PAKET 1.0 as a game-definition language and compiler for point-and-click adventures targeting Amstrad CPC 464 and MSX.
- https://github.com/santiontanon/paket/blob/1be8adb2fd549e06afeca11fdcf7f8821de78c05/README.md

### Classification (reviewed)

This is substantial original retro-development tooling, not a reverse-engineered game; one CPC tape library explicitly derives and simplifies required routines from firmware disassembly.
- https://github.com/santiontanon/paket/blob/1be8adb2fd549e06afeca11fdcf7f8821de78c05/README.md
- https://github.com/santiontanon/paket/blob/1be8adb2fd549e06afeca11fdcf7f8821de78c05/src/paket/templates/cpc/tape.asm

### Source CPU (not-applicable)

PAKET is a modern Java-authored compiler/game engine rather than reconstruction of one original machine-code subject, so an original source CPU is not applicable.
- https://github.com/santiontanon/paket/blob/1be8adb2fd549e06afeca11fdcf7f8821de78c05/README.md

### Target CPU (reviewed)

The emitted CPC/MSX templates explicitly use Zilog Z80 notation and the compiler includes a Z80 assembler-output utility, directly evidencing the output architecture.
- https://github.com/santiontanon/paket/blob/1be8adb2fd549e06afeca11fdcf7f8821de78c05/src/paket/templates/cpc/paketdsk.asm
- https://github.com/santiontanon/paket/blob/1be8adb2fd549e06afeca11fdcf7f8821de78c05/src/paket/templates/cpc/tape.asm

### Build (reviewed)

The repository supplies a build script, Java compiler sources, examples and target templates; the README states that the compiler generates game binaries. Limitations: The tracker did not compile the Java tool or execute a generated game.
- https://github.com/santiontanon/paket/blob/1be8adb2fd549e06afeca11fdcf7f8821de78c05/README.md
- https://github.com/santiontanon/paket/blob/1be8adb2fd549e06afeca11fdcf7f8821de78c05/build.sh

### Runtime profiles (no-evidence-found)

The reviewed documentation names CPC 464 and MSX targets but gives no explicit minimum RAM, model revision or OS/ROM requirements suitable for a compatibility profile.
- https://github.com/santiontanon/paket/blob/1be8adb2fd549e06afeca11fdcf7f8821de78c05/README.md

### AI (no-evidence-found)

The inspected README and target sources contain no development-AI disclosure; absence does not establish non-use.
- https://github.com/santiontanon/paket/blob/1be8adb2fd549e06afeca11fdcf7f8821de78c05/README.md
- https://github.com/santiontanon/paket/blob/1be8adb2fd549e06afeca11fdcf7f8821de78c05/src/paket/templates/cpc/paketdsk.asm

### Relationships (reviewed)

PAKET incorporates credited WYZTracker player material and a CPC cassette layer derived from firmware disassembly, while the compiler and game-definition system remain the repository's coherent original project.
- https://github.com/santiontanon/paket/blob/1be8adb2fd549e06afeca11fdcf7f8821de78c05/README.md
- https://github.com/santiontanon/paket/blob/1be8adb2fd549e06afeca11fdcf7f8821de78c05/src/paket/templates/cpc/tape.asm

## ROM Fiend — Macintosh ROM structure template for Hex Fiend

Project ID: rom-fiend-macintosh-rom-template · Overall audit: reviewed

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
  "display_title": "ROM Fiend — Macintosh ROM structure template for Hex Fiend",
  "id": "rom-fiend-macintosh-rom-template",
  "last_activity": "2025-02-25",
  "last_checked": "2026-10-22",
  "re_started": null,
  "reconstructed_languages": [
    "Tcl",
    "shell"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/eharmon/rom_fiend",
  "runtime_profiles": [],
  "source_cpu": [
    "68000 family",
    "PowerPC"
  ],
  "source_language": [],
  "source_platforms": [
    "Classic Macintosh"
  ],
  "status": "Parses common 68k and Old World PowerPC Macintosh ROM structures",
  "subjects": [
    "Classic Macintosh System ROMs",
    "Macintosh Declaration ROMs"
  ],
  "tags": [
    "Macintosh",
    "ROM",
    "Hex Fiend",
    "68000",
    "PowerPC"
  ],
  "target_cpu": [],
  "target_kinds": [
    "firmware-rom"
  ],
  "target_platforms": [],
  "techniques": [
    "structured binary parsing",
    "symbol-map integration",
    "byte-order recovery"
  ],
  "title": "ROM Fiend",
  "tool_kinds": [
    "binary-analysis",
    "rom-tool"
  ],
  "types": [
    "ROM analysis tool"
  ],
  "upstream_name": "ROM Fiend",
  "work_kinds": [
    "data-format-analysis"
  ]
}
```

### Identity (reviewed)

The README identifies a Hex Fiend file template for inspecting and modifying classic Macintosh Declaration and System ROMs.
- https://github.com/eharmon/rom_fiend/blob/a06c9baee765ae49fdbc1f04a0da7600d700594e/README.md
- https://github.com/eharmon/rom_fiend/blob/a06c9baee765ae49fdbc1f04a0da7600d700594e/Mac%20ROM.tcl

### Classification (reviewed)

This is reusable ROM structure-analysis tooling with explicit parsing and error handling, not a ROM collection or emulator.
- https://github.com/eharmon/rom_fiend/blob/a06c9baee765ae49fdbc1f04a0da7600d700594e/README.md
- https://github.com/eharmon/rom_fiend/blob/a06c9baee765ae49fdbc1f04a0da7600d700594e/Mac%20ROM.tcl

### Source CPU (reviewed)

The README explicitly covers ROMs for 68k and Old World PowerPC Macs, and the template names PowerPC CPU resource variants.
- https://github.com/eharmon/rom_fiend/blob/a06c9baee765ae49fdbc1f04a0da7600d700594e/README.md
- https://github.com/eharmon/rom_fiend/blob/a06c9baee765ae49fdbc1f04a0da7600d700594e/Mac%20ROM.tcl

### Target CPU (not-applicable)

ROM Fiend emits a structured Hex Fiend view rather than a port or reconstructed machine-code binary, so no output CPU applies.
- https://github.com/eharmon/rom_fiend/blob/a06c9baee765ae49fdbc1f04a0da7600d700594e/README.md

### Build (reviewed)

Installation copies or symlinks the Tcl template and optional symbol maps into Hex Fiend; there is no compiled target build. Limitations: The tracker did not install the template or parse a ROM.
- https://github.com/eharmon/rom_fiend/blob/a06c9baee765ae49fdbc1f04a0da7600d700594e/README.md

### Runtime profiles (no-evidence-found)

The README requires Hex Fiend but gives no explicit host OS version, CPU or memory minimum; target Macintosh hardware requirements do not apply to the analysis template.
- https://github.com/eharmon/rom_fiend/blob/a06c9baee765ae49fdbc1f04a0da7600d700594e/README.md

### AI (no-evidence-found)

The inspected README and template contain no development-AI disclosure; absence does not establish non-use.
- https://github.com/eharmon/rom_fiend/blob/a06c9baee765ae49fdbc1f04a0da7600d700594e/README.md
- https://github.com/eharmon/rom_fiend/blob/a06c9baee765ae49fdbc1f04a0da7600d700594e/Mac%20ROM.tcl

### Relationships (reviewed)

ROM Fiend extends Hex Fiend through its template mechanism and optionally installs external Macintosh ROM symbol maps; those dependencies are not represented as reconstructed subjects here.
- https://github.com/eharmon/rom_fiend/blob/a06c9baee765ae49fdbc1f04a0da7600d700594e/README.md

## dF80 — byte-identical CP/M FORTRAN-80 reconstruction

Project ID: df80-cpm-fortran80-disassembly · Overall audit: reviewed

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
  "display_title": "dF80 — byte-identical CP/M FORTRAN-80 reconstruction",
  "id": "df80-cpm-fortran80-disassembly",
  "last_activity": "2022-02-14",
  "last_checked": "2026-10-22",
  "re_started": null,
  "reconstructed_languages": [
    "Z80 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/nikitinprior/dF80",
  "runtime_profiles": [],
  "source_cpu": [
    "Z80"
  ],
  "source_language": [],
  "source_platforms": [
    "CP/M"
  ],
  "status": "Documented M80/L80 rebuild is byte-identical to F80.COM",
  "subjects": [
    "Microsoft FORTRAN-80 3.4 for CP/M"
  ],
  "tags": [
    "CP/M",
    "FORTRAN-80",
    "Z80",
    "byte-exact"
  ],
  "target_cpu": [
    "Z80"
  ],
  "target_kinds": [
    "development-tool",
    "system-software"
  ],
  "target_platforms": [
    "CP/M"
  ],
  "techniques": [
    "multi-binary comparison",
    "module-boundary recovery",
    "symbol-table analysis"
  ],
  "title": "dF80",
  "tool_kinds": [],
  "types": [
    "compiler reconstruction"
  ],
  "upstream_name": "dF80",
  "work_kinds": [
    "disassembly",
    "source-reconstruction"
  ]
}
```

### Identity (reviewed)

The author identifies a partly commented reconstruction of Microsoft FORTRAN-80 3.4 for CP/M, including both 1985 F80 and 3.44 source variants.
- https://github.com/nikitinprior/dF80/blob/e7f7c3dff284286d52d795d5cdc806b776b3d71a/README.md
- https://github.com/nikitinprior/dF80/blob/e7f7c3dff284286d52d795d5cdc806b776b3d71a/f8.mac

### Classification (reviewed)

This is binary-derived compiler reconstruction; module boundaries were recovered by comparing multiple executables rather than from original Microsoft source.
- https://github.com/nikitinprior/dF80/blob/e7f7c3dff284286d52d795d5cdc806b776b3d71a/README.md

### Source CPU (reviewed)

The README states that the compiler produces Z80 assembler listings and that the recovered source is assembled with Microsoft's M80/L80 toolchain.
- https://github.com/nikitinprior/dF80/blob/e7f7c3dff284286d52d795d5cdc806b776b3d71a/README.md
- https://github.com/nikitinprior/dF80/blob/e7f7c3dff284286d52d795d5cdc806b776b3d71a/f8.mac

### Target CPU (reviewed)

The reconstructed Z80 assembly emits CP/M F80.COM executables, explicitly preserving the Z80 output architecture.
- https://github.com/nikitinprior/dF80/blob/e7f7c3dff284286d52d795d5cdc806b776b3d71a/README.md
- https://github.com/nikitinprior/dF80/blob/e7f7c3dff284286d52d795d5cdc806b776b3d71a/f8.mac

### Build (reviewed)

The README gives M80 and L80 commands and claims the resulting F80.COM and F.COM executables are completely identical to their originals. Limitations: Byte identity is an author claim; the tracker did not run M80/L80 or compare binaries.
- https://github.com/nikitinprior/dF80/blob/e7f7c3dff284286d52d795d5cdc806b776b3d71a/README.md

### Runtime profiles (no-evidence-found)

The project identifies CP/M executables but gives no minimum CP/M version, RAM, machine model or operating environment.
- https://github.com/nikitinprior/dF80/blob/e7f7c3dff284286d52d795d5cdc806b776b3d71a/README.md

### AI (no-evidence-found)

The inspected README and recovered source contain no development-AI disclosure; absence does not establish non-use.
- https://github.com/nikitinprior/dF80/blob/e7f7c3dff284286d52d795d5cdc806b776b3d71a/README.md
- https://github.com/nikitinprior/dF80/blob/e7f7c3dff284286d52d795d5cdc806b776b3d71a/f8.mac

### Relationships (reviewed)

The author distinguishes the selected CP/M compiler from a likely earlier TRS-80 lineage and from W. Cirsovius's separate M80/L80 disassemblies; neither is collapsed into this record.
- https://github.com/nikitinprior/dF80/blob/e7f7c3dff284286d52d795d5cdc806b776b3d71a/README.md

## Computer Archeology — annotated disassemblies and rendering toolchain

Project ID: computer-archeology-disassemblies-toolchain · Overall audit: reviewed

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
  "display_title": "Computer Archeology — annotated disassemblies and rendering toolchain",
  "id": "computer-archeology-disassemblies-toolchain",
  "last_activity": "2026-10-06",
  "last_checked": "2026-10-22",
  "re_started": null,
  "reconstructed_languages": [
    "assembly",
    "Python",
    "JavaScript",
    "Markdown"
  ],
  "record_class": "hybrid",
  "repo": "https://github.com/topherCantrell/computerarcheology",
  "runtime_profiles": [],
  "source_cpu": [
    "6502",
    "Z80",
    "6809",
    "8080"
  ],
  "source_language": [],
  "source_platforms": [
    "Arcade",
    "Atari 2600",
    "TRS-80",
    "TRS-80 Color Computer",
    "Amiga",
    "Game Boy",
    "NES"
  ],
  "status": "Large maintained corpus of annotated analyses with dedicated rendering and consistency tools",
  "subjects": [
    "Computer Archeology annotated program analyses",
    "names_in_code and site-rendering tools"
  ],
  "tags": [
    "software archaeology",
    "disassembly",
    "6502",
    "Z80",
    "6809",
    "8080"
  ],
  "target_cpu": [],
  "target_kinds": [
    "game",
    "firmware-rom"
  ],
  "target_platforms": [],
  "techniques": [
    "cross-linked memory maps",
    "binary consistency checks",
    "ROM graphics extraction"
  ],
  "title": "Computer Archeology",
  "tool_kinds": [
    "binary-analysis",
    "static-analysis",
    "rom-tool",
    "automation"
  ],
  "types": [
    "software-archaeology corpus",
    "analysis toolchain"
  ],
  "upstream_name": "Computer Archeology",
  "work_kinds": [
    "disassembly",
    "binary-analysis",
    "data-format-analysis"
  ]
}
```

### Identity (reviewed)

The root repository contains the source analyses and Python toolchain behind computerarcheology.com, spanning many individually documented games and machines under one coherent publication system.
- https://github.com/topherCantrell/computerarcheology/blob/1adc2a7f3ae30f9efceed3f6b22bf5541c1f584c/README.md
- https://github.com/topherCantrell/computerarcheology/blob/1adc2a7f3ae30f9efceed3f6b22bf5541c1f584c/content/README.md

### Classification (reviewed)

This is both a maintained corpus of annotated binary disassemblies and reusable archaeology tooling; tracking the root preserves the shared renderer, memory-map conventions and analysis identity without splitting every title directory.
- https://github.com/topherCantrell/computerarcheology/blob/1adc2a7f3ae30f9efceed3f6b22bf5541c1f584c/README.md
- https://github.com/topherCantrell/computerarcheology/blob/1adc2a7f3ae30f9efceed3f6b22bf5541c1f584c/content/README.md
- https://github.com/topherCantrell/computerarcheology/blob/1adc2a7f3ae30f9efceed3f6b22bf5541c1f584c/computerarcheology/carender/names_in_code.py

### Source CPU (reviewed)

Reviewed content includes 6502, Z80, 6809 and 8080 program analyses; only those directly represented instruction sets are recorded, not every platform suggested by directory names.
- https://github.com/topherCantrell/computerarcheology/blob/1adc2a7f3ae30f9efceed3f6b22bf5541c1f584c/content/Atari2600/Combat/Code.md
- https://github.com/topherCantrell/computerarcheology/blob/1adc2a7f3ae30f9efceed3f6b22bf5541c1f584c/content/Arcade/Frogger/Code.md
- https://github.com/topherCantrell/computerarcheology/blob/1adc2a7f3ae30f9efceed3f6b22bf5541c1f584c/content/Arcade/Defender/BankFixed.md
- https://github.com/topherCantrell/computerarcheology/blob/1adc2a7f3ae30f9efceed3f6b22bf5541c1f584c/content/Arcade/SpaceInvaders/Code.md

### Target CPU (not-applicable)

The common project output is linked documentation, analysis data and web tooling rather than reconstructed machine-code binaries with one target CPU.
- https://github.com/topherCantrell/computerarcheology/blob/1adc2a7f3ae30f9efceed3f6b22bf5541c1f584c/README.md

### Build (reviewed)

The README documents Python commands for generating and serving the site and describes automated name/link maintenance across disassembly and memory-map files. Limitations: The tracker did not execute the renderer or validate individual title binaries.
- https://github.com/topherCantrell/computerarcheology/blob/1adc2a7f3ae30f9efceed3f6b22bf5541c1f584c/README.md
- https://github.com/topherCantrell/computerarcheology/blob/1adc2a7f3ae30f9efceed3f6b22bf5541c1f584c/computerarcheology/carender/names_in_code.py

### Runtime profiles (no-evidence-found)

The reviewed root documentation does not provide host CPU, RAM or Python-version minima for the analysis/rendering toolchain.
- https://github.com/topherCantrell/computerarcheology/blob/1adc2a7f3ae30f9efceed3f6b22bf5541c1f584c/README.md

### AI (no-evidence-found)

The inspected root documentation and tooling source contain no development-AI disclosure; absence does not establish non-use.
- https://github.com/topherCantrell/computerarcheology/blob/1adc2a7f3ae30f9efceed3f6b22bf5541c1f584c/README.md
- https://github.com/topherCantrell/computerarcheology/blob/1adc2a7f3ae30f9efceed3f6b22bf5541c1f584c/computerarcheology/carender/names_in_code.py

### Relationships (reviewed)

The title directories share one rendering/annotation architecture and publication site, so the repository is represented as one broad analysis project rather than speculative directory-scoped records.
- https://github.com/topherCantrell/computerarcheology/blob/1adc2a7f3ae30f9efceed3f6b22bf5541c1f584c/README.md
- https://github.com/topherCantrell/computerarcheology/blob/1adc2a7f3ae30f9efceed3f6b22bf5541c1f584c/content/README.md

## follin-music-source-archive

Project ID: follin-music-source-archive · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "follin-music-source-archive",
  "last_checked": "2026-10-22",
  "runtime_profiles": [
    {
      "cpu_family": "Z80",
      "evidence": [
        "https://github.com/breakintoprogram/archive-follin/blob/ba0e22578a1af16d1e4d234309b44692ca991c12/README.md",
        "https://github.com/breakintoprogram/archive-follin/tree/ba0e22578a1af16d1e4d234309b44692ca991c12/Examples"
      ],
      "name": "Modern AY example snapshots",
      "notes": "README documents sjasmplus builds of exec_ examples to .sna snapshots and execution in ZEsarUX. No minimum model or RAM is stated.",
      "platform": "ZX Spectrum / Amstrad CPC AY workflow"
    }
  ],
  "status": "Recovered multi-title source archive; documented Z80 AY example rebuilds",
  "target_cpu": [
    "Z80"
  ]
}
```

Expected existing project SHA256: 2b256a2f8d7f09e6ee4c37548584b04a2bad334f17f64241665dd8e0750ddb0b

### Identity (reviewed)

This remains one coherent preservation archive of Tim and Geoff Follin music data and drivers recovered from Tatung Einstein disks; individual game-named folders are archival components, not independently published projects.
- https://github.com/breakintoprogram/archive-follin/blob/ba0e22578a1af16d1e4d234309b44692ca991c12/README.md
- https://github.com/breakintoprogram/archive-follin/tree/ba0e22578a1af16d1e4d234309b44692ca991c12/Examples

### Classification (reviewed)

The archive combines original period 6502/Z80 source recovery, a reverse-engineered token detokenizer and modern example rebuild work; it is not a game disassembly collection.
- https://github.com/breakintoprogram/archive-follin/blob/ba0e22578a1af16d1e4d234309b44692ca991c12/README.md
- https://github.com/breakintoprogram/archive-follin/tree/ba0e22578a1af16d1e4d234309b44692ca991c12/Examples

### Source CPU (reviewed)

The README explicitly identifies original C64 6502 and CPC/Spectrum Z80 source material recovered from the disks.
- https://github.com/breakintoprogram/archive-follin/blob/ba0e22578a1af16d1e4d234309b44692ca991c12/README.md

### Target CPU (reviewed)

The documented modern build lane assembles selected Z80 AY examples with sjasmplus into snapshots; no rebuilt 6502 output is claimed.
- https://github.com/breakintoprogram/archive-follin/blob/ba0e22578a1af16d1e4d234309b44692ca991c12/README.md
- https://github.com/breakintoprogram/archive-follin/tree/ba0e22578a1af16d1e4d234309b44692ca991c12/Examples

### Build (reviewed)

The README documents VS Code build tasks for exec_ files, producing .sna snapshots for ZEsarUX; other recovered files remain source material without blanket rebuild claims. Limitations: The tracker did not build the examples, and no compile claim is generalized to every disk or title.
- https://github.com/breakintoprogram/archive-follin/blob/ba0e22578a1af16d1e4d234309b44692ca991c12/README.md
- https://github.com/breakintoprogram/archive-follin/tree/ba0e22578a1af16d1e4d234309b44692ca991c12/Examples

### Runtime profiles (reviewed)

A bounded Z80 AY snapshot workflow is explicit; no minimum Spectrum/CPC model, RAM or ROM revision is given.
- https://github.com/breakintoprogram/archive-follin/blob/ba0e22578a1af16d1e4d234309b44692ca991c12/README.md
- https://github.com/breakintoprogram/archive-follin/tree/ba0e22578a1af16d1e4d234309b44692ca991c12/Examples

### AI (no-evidence-found)

The README and reviewed archive structure contain no development-AI disclosure; absence does not establish non-use.
- https://github.com/breakintoprogram/archive-follin/blob/ba0e22578a1af16d1e4d234309b44692ca991c12/README.md
- https://github.com/breakintoprogram/archive-follin/tree/ba0e22578a1af16d1e4d234309b44692ca991c12/Examples

### Relationships (reviewed)

The per-game and per-disk materials share the same donor provenance, recovery process, drivers and detokenization workflow; repository-root scope is the accurate catalogue identity.
- https://github.com/breakintoprogram/archive-follin/blob/ba0e22578a1af16d1e4d234309b44692ca991c12/README.md
- https://github.com/breakintoprogram/archive-follin/tree/ba0e22578a1af16d1e4d234309b44692ca991c12/Examples

## Sources

```json
[
  {
    "first_indexed": "2026-10-22",
    "id": "github-jeff-birt-sharp-pc1500-rom-disassembly",
    "kind": "github-repository",
    "last_reviewed": "2026-10-22",
    "open_task_ids": [],
    "projects_promoted": [
      "sharp-pc1500-rom-disassembly"
    ],
    "reason": "Primary repository for a buildable A01/A03/A04 LH5801 ROM disassembly.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/Jeff-Birt/Sharp_PC-1500_ROM_Disassembly"
  },
  {
    "first_indexed": "2026-10-22",
    "id": "github-egbert-azure-calvados",
    "kind": "github-repository",
    "last_reviewed": "2026-10-22",
    "open_task_ids": [],
    "projects_promoted": [
      "calvados-genie-iiis-reconstruction"
    ],
    "reason": "Primary repository for the Stage B CalvaDOS/G-DOS hard-disk reconstruction.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/Egbert-Azure/TCS-Trommeschlaeger-Genie-IIIs-CalvaDOS"
  },
  {
    "first_indexed": "2026-10-22",
    "id": "github-santiontanon-paket",
    "kind": "github-repository",
    "last_reviewed": "2026-10-22",
    "open_task_ids": [],
    "projects_promoted": [
      "paket-adventure-game-compiler"
    ],
    "reason": "Primary repository for the PAKET CPC/MSX point-and-click compiler and engine.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/santiontanon/paket"
  },
  {
    "first_indexed": "2026-10-22",
    "id": "github-eharmon-rom-fiend",
    "kind": "github-repository",
    "last_reviewed": "2026-10-22",
    "open_task_ids": [],
    "projects_promoted": [
      "rom-fiend-macintosh-rom-template"
    ],
    "reason": "Primary repository for the Macintosh ROM Hex Fiend template.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/eharmon/rom_fiend"
  },
  {
    "first_indexed": "2026-10-22",
    "id": "github-nikitinprior-df80",
    "kind": "github-repository",
    "last_reviewed": "2026-10-22",
    "open_task_ids": [],
    "projects_promoted": [
      "df80-cpm-fortran80-disassembly"
    ],
    "reason": "Primary repository for the CP/M FORTRAN-80 compiler reconstruction.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/nikitinprior/dF80"
  },
  {
    "first_indexed": "2026-10-22",
    "id": "github-tophercantrell-computerarcheology",
    "kind": "github-repository",
    "last_reviewed": "2026-10-22",
    "open_task_ids": [],
    "projects_promoted": [
      "computer-archeology-disassemblies-toolchain"
    ],
    "reason": "Primary repository for the Computer Archeology analysis corpus and renderer.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/topherCantrell/computerarcheology"
  },
  {
    "first_indexed": "2026-10-22",
    "id": "github-dougmasten-awesome-coco",
    "kind": "github-repository",
    "last_reviewed": "2026-10-22",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Curated Color Computer development and archaeology index retained for outbound-lead review, not promoted as an independent implementation.",
    "review_state": "partial",
    "source": "https://github.com/dougmasten/awesome-coco"
  },
  {
    "first_indexed": "2026-10-22",
    "id": "search-2026-10-22-trs80-disassembly",
    "kind": "github-code-search",
    "last_reviewed": "2026-10-22",
    "open_task_ids": [],
    "projects_promoted": [
      "sharp-pc1500-rom-disassembly",
      "calvados-genie-iiis-reconstruction",
      "df80-cpm-fortran80-disassembly",
      "computer-archeology-disassemblies-toolchain"
    ],
    "reason": "Fresh-search slice. Exact repository query `\"TRS-80\" disassembly source reconstruction` returned no repositories. Exact code query `TRS-80 disassembly` reviewed kiwisincebirth/TRS-80-ROMS (existing), Jeff-Birt/Sharp_PC-1500_ROM_Disassembly, Egbert-Azure/TCS-Trommeschlaeger-Genie-IIIs-CalvaDOS, nikitinprior/dF80, topherCantrell/computerarcheology and dougmasten/awesome-coco; four new projects were promoted and the curated index was retained as a source.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/search?q=TRS-80+disassembly&type=code"
  },
  {
    "first_indexed": "2026-10-22",
    "id": "search-2026-10-22-amstrad-cpc-disassembly",
    "kind": "github-code-search",
    "last_reviewed": "2026-10-22",
    "open_task_ids": [],
    "projects_promoted": [
      "paket-adventure-game-compiler"
    ],
    "reason": "Fresh-search slice. Exact repository query `\"Amstrad CPC\" reassembly disassembly` returned no repositories. Exact code query `Amstrad CPC disassembly` led to santiontanon/paket; its README and Z80 templates were reviewed and promoted. Other returned emulator/framework matches did not establish a new candidate.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/search?q=Amstrad+CPC+disassembly&type=code"
  },
  {
    "first_indexed": "2026-10-22",
    "id": "search-2026-10-22-macintosh-rom-disassembly",
    "kind": "github-code-search",
    "last_reviewed": "2026-10-22",
    "open_task_ids": [],
    "projects_promoted": [
      "rom-fiend-macintosh-rom-template"
    ],
    "reason": "Fresh-search slice. Exact repository query `\"Macintosh\" 68k ROM disassembly` returned no repositories. Exact code query `Macintosh 68k ROM` reviewed eharmon/rom_fiend and promoted its structured Macintosh ROM parser; generic emulator/configuration and ROM-collection hits were not candidates.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/search?q=Macintosh+68k+ROM&type=code"
  }
]
```

## Source updates

```json
[
  {
    "id": "github-breakintoprogram-archive-follin",
    "last_reviewed": "2026-10-22",
    "reason": "Repository-wide review confirms one coherent recovered-source archive. Modern build documentation is limited to selected Z80 AY examples; individual game folders remain components rather than separate projects.",
    "review_state": "substantially-reviewed"
  }
]
```

## Tasks

```json
[
  {
    "created_at": "2026-10-22",
    "description": "Screen the attributed CoCo disassembly, original-source and development-tool links against current projects and decisions; review only new roots individually.",
    "id": "task-mine-awesome-coco-analysis-links",
    "last_reviewed": "2026-10-22",
    "priority": "normal",
    "source_ids": [
      "github-dougmasten-awesome-coco"
    ],
    "state": "open"
  }
]
```

## Task updates

```json
[
  {
    "id": "task-review-follin-archive-game-music-components",
    "last_reviewed": "2026-10-22",
    "notes_append": "Reviewed the per-disk and example structure. Title-named sources share one donor/recovery/driver workflow and do not warrant directory-scoped records. The explicit sjasmplus rebuild lane is limited to selected Z80 AY examples and is now captured in the root project's target CPU and runtime profile.",
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
      "https://github.com/Jeff-Birt/Sharp_PC-1500_ROM_Disassembly/blob/5a5f8aa9ba52e239cc224c3a2e48bde9299b4f3e/README.md",
      "https://github.com/Jeff-Birt/Sharp_PC-1500_ROM_Disassembly/blob/5a5f8aa9ba52e239cc224c3a2e48bde9299b4f3e/PC-1500_ROM-A0x.lh5801.asm",
      "https://github.com/Jeff-Birt/Sharp_PC-1500_ROM_Disassembly/blob/5a5f8aa9ba52e239cc224c3a2e48bde9299b4f3e/build.bat"
    ],
    "id": "2026-10-22-promote-sharp-pc1500-rom-disassembly",
    "project_ids": [
      "sharp-pc1500-rom-disassembly"
    ],
    "reason": "Primary sources establish a distinct buildable LH5801 ROM disassembly covering three Sharp PC-1500 revisions.",
    "reviewed_at": "2026-10-22",
    "source_ids": [
      "github-jeff-birt-sharp-pc1500-rom-disassembly",
      "search-2026-10-22-trs80-disassembly"
    ],
    "title": "Sharp PC-1500 / TRS-80 PC-2 ROM disassembly",
    "url": "https://github.com/Jeff-Birt/Sharp_PC-1500_ROM_Disassembly"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/Egbert-Azure/TCS-Trommeschlaeger-Genie-IIIs-CalvaDOS/blob/52fb7c1ff3135a177ec54e182a2676f35608128b/README.md"
    ],
    "id": "2026-10-22-promote-calvados-genie-iiis-reconstruction",
    "project_ids": [
      "calvados-genie-iiis-reconstruction"
    ],
    "reason": "Primary documentation establishes a functioning but explicitly reconstructed Genie IIIs hard-disk operating-system lineage.",
    "reviewed_at": "2026-10-22",
    "source_ids": [
      "github-egbert-azure-calvados",
      "search-2026-10-22-trs80-disassembly"
    ],
    "title": "CalvaDOS — Genie IIIs hard-disk OS reconstruction",
    "url": "https://github.com/Egbert-Azure/TCS-Trommeschlaeger-Genie-IIIs-CalvaDOS"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/santiontanon/paket/blob/1be8adb2fd549e06afeca11fdcf7f8821de78c05/README.md",
      "https://github.com/santiontanon/paket/blob/1be8adb2fd549e06afeca11fdcf7f8821de78c05/src/paket/templates/cpc/paketdsk.asm"
    ],
    "id": "2026-10-22-promote-paket-adventure-game-compiler",
    "project_ids": [
      "paket-adventure-game-compiler"
    ],
    "reason": "Primary sources establish substantial original CPC/MSX game-development tooling with explicit Z80 outputs.",
    "reviewed_at": "2026-10-22",
    "source_ids": [
      "github-santiontanon-paket",
      "search-2026-10-22-amstrad-cpc-disassembly"
    ],
    "title": "PAKET — CPC/MSX point-and-click adventure compiler",
    "url": "https://github.com/santiontanon/paket"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/eharmon/rom_fiend/blob/a06c9baee765ae49fdbc1f04a0da7600d700594e/README.md",
      "https://github.com/eharmon/rom_fiend/blob/a06c9baee765ae49fdbc1f04a0da7600d700594e/Mac%20ROM.tcl"
    ],
    "id": "2026-10-22-promote-rom-fiend-macintosh-rom-template",
    "project_ids": [
      "rom-fiend-macintosh-rom-template"
    ],
    "reason": "Primary sources establish reusable structured analysis tooling for classic Macintosh ROMs.",
    "reviewed_at": "2026-10-22",
    "source_ids": [
      "github-eharmon-rom-fiend",
      "search-2026-10-22-macintosh-rom-disassembly"
    ],
    "title": "ROM Fiend — Macintosh ROM structure template for Hex Fiend",
    "url": "https://github.com/eharmon/rom_fiend"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/nikitinprior/dF80/blob/e7f7c3dff284286d52d795d5cdc806b776b3d71a/README.md",
      "https://github.com/nikitinprior/dF80/blob/e7f7c3dff284286d52d795d5cdc806b776b3d71a/f8.mac"
    ],
    "id": "2026-10-22-promote-df80-cpm-fortran80-disassembly",
    "project_ids": [
      "df80-cpm-fortran80-disassembly"
    ],
    "reason": "Primary documentation and source establish a byte-identical CP/M FORTRAN-80 compiler reconstruction.",
    "reviewed_at": "2026-10-22",
    "source_ids": [
      "github-nikitinprior-df80",
      "search-2026-10-22-trs80-disassembly"
    ],
    "title": "dF80 — byte-identical CP/M FORTRAN-80 reconstruction",
    "url": "https://github.com/nikitinprior/dF80"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/topherCantrell/computerarcheology/blob/1adc2a7f3ae30f9efceed3f6b22bf5541c1f584c/README.md",
      "https://github.com/topherCantrell/computerarcheology/blob/1adc2a7f3ae30f9efceed3f6b22bf5541c1f584c/content/README.md",
      "https://github.com/topherCantrell/computerarcheology/blob/1adc2a7f3ae30f9efceed3f6b22bf5541c1f584c/computerarcheology/carender/names_in_code.py"
    ],
    "id": "2026-10-22-promote-computer-archeology-disassemblies-toolchain",
    "project_ids": [
      "computer-archeology-disassemblies-toolchain"
    ],
    "reason": "The repository is a coherent, substantial cross-platform analysis corpus and archaeology toolchain; root scope preserves that identity.",
    "reviewed_at": "2026-10-22",
    "source_ids": [
      "github-tophercantrell-computerarcheology",
      "search-2026-10-22-trs80-disassembly"
    ],
    "title": "Computer Archeology — annotated disassemblies and rendering toolchain",
    "url": "https://github.com/topherCantrell/computerarcheology"
  },
  {
    "decision": "excluded",
    "evidence_urls": [
      "https://github.com/dougmasten/awesome-coco/blob/38f9e4e9ba88a9e5f57cc0f48e43d1204e850b8a/README.md"
    ],
    "id": "2026-10-22-exclude-awesome-coco-as-project",
    "project_ids": [],
    "reason": "The reviewed repository is a curated outbound-resource index rather than its own retro-development implementation. It is retained as a discovery source for individually attributed leads.",
    "reviewed_at": "2026-10-22",
    "source_ids": [
      "github-dougmasten-awesome-coco",
      "search-2026-10-22-trs80-disassembly"
    ],
    "title": "dougmasten/awesome-coco",
    "url": "https://github.com/dougmasten/awesome-coco"
  }
]
```

## Source ids

```json
[
  "github-breakintoprogram-archive-follin"
]
```

## Research event notes

The CPU audit queue returned zero unresolved source/target CPU areas before selection. Six new records and the updated Follin record therefore use only explicit primary CPU evidence. No project was independently compiled or executed.
