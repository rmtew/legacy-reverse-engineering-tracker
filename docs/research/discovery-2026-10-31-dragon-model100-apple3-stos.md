# Dragon/CoCo, Model 100, Apple III and STOS discovery

Review thirteen fresh candidates, promote seven projects, and deepen the STOS component/runtime audit

Date: 2026-10-31 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- dragon-dos-utils-unix / Build (reviewed): Static documentation review only.
- dragon-dos-utils-unix / AI (no-evidence-found): No explicit development-AI attribution was found in the reviewed README; this does not establish non-use.
- dragon32-dev-devcontainer / Build (reviewed): Upstream-documented workflow only.
- dragon32-dev-devcontainer / AI (no-evidence-found): No explicit development-AI attribution was found in the inspected README or Makefile; this does not establish non-use.
- dragon-mpagd-suite / Build (reviewed): Primary documentation review only.
- dragon-mpagd-suite / AI (no-evidence-found): No explicit development-AI attribution was found in the reviewed README; this does not establish non-use.
- casromutils-dragon-coco / Build (reviewed): Implementation and comments reviewed statically.
- casromutils-dragon-coco / AI (no-evidence-found): No explicit development-AI attribution was found in the inspected Pascal sources; this does not establish non-use.
- apple-iii-custom-rom / Build (reviewed): Static source/documentation review only; output identity was not compared.
- apple-iii-custom-rom / AI (no-evidence-found): No explicit development-AI attribution was found in the inspected README/source; this does not establish non-use.
- apple-iii-rom-drive-driver / Target CPU (no-evidence-found): The inspected README and driver source do not explicitly identify the output CPU; Apple III platform and assembly syntax alone were not used to infer it.
- apple-iii-rom-drive-driver / Build (reviewed): Upstream-documented build only.
- apple-iii-rom-drive-driver / AI (no-evidence-found): No explicit development-AI attribution was found in the inspected README/source; this does not establish non-use.
- soshdboot-apple-iii / Build (reviewed): Primary documentation/source review only; claimed boot compatibility was not reproduced.
- soshdboot-apple-iii / AI (no-evidence-found): No explicit development-AI attribution was found in the inspected README/source; this does not establish non-use.
- stos-atari-basic-source / Build (needs-research): The inspected extension materials provide source and historical usage context, including full GBP interpreter/compiler source, but do not establish a complete reproducible modern build for the core STOS compiler/interpreter. Next check: Trace the root/core build procedure and tool versions, then attempt a non-destructive build or locate an upstream reproducibility statement.
- stos-atari-basic-source / AI (no-evidence-found): No explicit development-AI attribution was found in the inspected historical documentation/source materials; this does not establish non-use in later maintenance.
- stos-atari-basic-source / Relationships (needs-research): The Falcon suite and GBP Extension are now identified as titled components in the STOS repository, but the provenance boundary between original historical core sources and later adapted/system-interface trees remains incompletely documented. Next check: Map the repository's orig and adapted source trees against named historical releases and extension authors before splitting or linking further component records.

## Dragon DOS Utils — VDK and DragonDOS extraction tools

Project ID: dragon-dos-utils-unix · Overall audit: reviewed

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
  "display_title": "Dragon DOS Utils — VDK and DragonDOS extraction tools",
  "id": "dragon-dos-utils-unix",
  "last_activity": "2021-12-12",
  "last_checked": "2026-10-31",
  "re_started": null,
  "reconstructed_languages": [
    "C"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/pulkomandy/ddosutils",
  "runtime_profiles": [
    {
      "evidence": [
        "https://github.com/pulkomandy/ddosutils/blob/24029d98649b351edded672f51537dbd02fc9145/README.md"
      ],
      "name": "ddosutils",
      "notes": "README documents make -f makefile.gcc; no host CPU or RAM minimum is stated.",
      "os": "GNU make and GCC",
      "platform": "Unix-like host"
    }
  ],
  "source_cpu": [],
  "source_language": [
    "VDK disk images",
    "Dragon BASIC",
    "DosDream database files"
  ],
  "source_platforms": [
    "Dragon 32",
    "Dragon 64",
    "DragonDOS"
  ],
  "status": "Unix port of Dragon DOS Utils with documented VDK extraction and conversion routes; not independently built",
  "subjects": [
    "DragonDOS disk images",
    "DosDream databases"
  ],
  "tags": [
    "dragon-32",
    "dragondos",
    "vdk"
  ],
  "target_cpu": [],
  "target_kinds": [],
  "target_platforms": [
    "Unix-like host"
  ],
  "techniques": [
    "DragonDOS filesystem parsing",
    "BASIC listing conversion",
    "DosDream text conversion"
  ],
  "title": "Dragon DOS Utils — VDK and DragonDOS extraction tools",
  "tool_kinds": [
    "disk-filesystem-tool"
  ],
  "types": [
    "disk image utility",
    "data conversion tool"
  ],
  "upstream_name": "ddosutils",
  "work_kinds": [
    "data-format-analysis"
  ]
}
```

### Identity (reviewed)

The repository is a Unix port of Graham E. Kinns' Dragon DOS Utils for listing and extracting VDK/DragonDOS images and converting BASIC and DosDream data.
- https://github.com/pulkomandy/ddosutils/blob/24029d98649b351edded672f51537dbd02fc9145/README.md

### Classification (reviewed)

This is host-side disk-filesystem and data-format tooling, not a reconstructed Dragon program or native port.
- https://github.com/pulkomandy/ddosutils/blob/24029d98649b351edded672f51537dbd02fc9145/README.md

### Source CPU (not-applicable)

Source CPU is not applicable because the reviewed inputs are disk images, BASIC records and database data rather than an original machine-code program.
- https://github.com/pulkomandy/ddosutils/blob/24029d98649b351edded672f51537dbd02fc9145/README.md

### Target CPU (not-applicable)

Target CPU is not applicable because the utility extracts and converts data rather than emitting native executable code.
- https://github.com/pulkomandy/ddosutils/blob/24029d98649b351edded672f51537dbd02fc9145/README.md

### Build (reviewed)

The README gives the GCC makefile command and names the command-line utilities; no build or sample-image extraction was run. Limitations: Static documentation review only.
- https://github.com/pulkomandy/ddosutils/blob/24029d98649b351edded672f51537dbd02fc9145/README.md

### Runtime profiles (reviewed)

GNU make/GCC on a Unix-like host is documented; no CPU, RAM or OS-version minimum is stated.
- https://github.com/pulkomandy/ddosutils/blob/24029d98649b351edded672f51537dbd02fc9145/README.md

### AI (no-evidence-found)

No explicit development-AI attribution was found in the reviewed README; this does not establish non-use.
- https://github.com/pulkomandy/ddosutils/blob/24029d98649b351edded672f51537dbd02fc9145/README.md

### Relationships (reviewed)

The README explicitly identifies this as a Unix port of Graham E. Kinns' Dragon DOS Utils and retains the upstream utility lineage.
- https://github.com/pulkomandy/ddosutils/blob/24029d98649b351edded672f51537dbd02fc9145/README.md

## Dragon 32 DevContainer — reproducible 6809 ROM starter

Project ID: dragon32-dev-devcontainer · Overall audit: reviewed

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
  "display_title": "Dragon 32 DevContainer — reproducible 6809 ROM starter",
  "id": "dragon32-dev-devcontainer",
  "last_activity": "2026-01-08",
  "last_checked": "2026-10-31",
  "re_started": null,
  "reconstructed_languages": [
    "Motorola 6809 assembly"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/computamike/dragon32-dev",
  "runtime_profiles": [
    {
      "evidence": [
        "https://github.com/computamike/dragon32-dev/blob/babf1b56f5e745e9da732a1522b681467e69767d/Readme.md"
      ],
      "name": "VS Code DevContainer",
      "notes": "README documents the container and XRoar workflow; no host hardware minimum is stated.",
      "os": "VS Code Dev Containers and Docker",
      "platform": "Modern host"
    }
  ],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [
    "Dragon 32"
  ],
  "status": "Containerized Dragon 32 assembly starter with ROM build and XRoar run targets",
  "subjects": [
    "Dragon 32 ROM development"
  ],
  "tags": [
    "dragon-32",
    "6809",
    "devcontainer"
  ],
  "target_cpu": [
    "Motorola 6809"
  ],
  "target_kinds": [],
  "target_platforms": [
    "Dragon 32"
  ],
  "techniques": [
    "6809 ROM assembly",
    "containerized toolchain",
    "XRoar launch automation"
  ],
  "title": "Dragon 32 DevContainer — reproducible 6809 ROM starter",
  "tool_kinds": [
    "development-environment",
    "assembler-toolchain"
  ],
  "types": [
    "original retro-development environment",
    "ROM starter"
  ],
  "upstream_name": "dragon32-dev",
  "work_kinds": []
}
```

### Identity (reviewed)

The repository presents a VS Code DevContainer and Hello World ROM starter for Dragon 32 assembly development.
- https://github.com/computamike/dragon32-dev/blob/babf1b56f5e745e9da732a1522b681467e69767d/Readme.md

### Classification (reviewed)

This is original retro-development environment/toolchain work, not reverse engineering or an RE-derived port.
- https://github.com/computamike/dragon32-dev/blob/babf1b56f5e745e9da732a1522b681467e69767d/Readme.md
- https://github.com/computamike/dragon32-dev/blob/babf1b56f5e745e9da732a1522b681467e69767d/Makefile

### Source CPU (not-applicable)

Source CPU is not applicable because this is an original development starter rather than analysis of a pre-existing binary.
- https://github.com/computamike/dragon32-dev/blob/babf1b56f5e745e9da732a1522b681467e69767d/Readme.md

### Target CPU (reviewed)

The Makefile explicitly selects asm6809 or a09 and builds a Dragon 32 ROM, establishing Motorola 6809 output.
- https://github.com/computamike/dragon32-dev/blob/babf1b56f5e745e9da732a1522b681467e69767d/Makefile

### Build (reviewed)

README and Makefile document container startup, make, ROM output and an XRoar run target; no container, assembler or emulator was run. Limitations: Upstream-documented workflow only.
- https://github.com/computamike/dragon32-dev/blob/babf1b56f5e745e9da732a1522b681467e69767d/Readme.md
- https://github.com/computamike/dragon32-dev/blob/babf1b56f5e745e9da732a1522b681467e69767d/Makefile

### Runtime profiles (reviewed)

The documented host route requires VS Code Dev Containers and Docker; no CPU, RAM or version floor is stated.
- https://github.com/computamike/dragon32-dev/blob/babf1b56f5e745e9da732a1522b681467e69767d/Readme.md

### AI (no-evidence-found)

No explicit development-AI attribution was found in the inspected README or Makefile; this does not establish non-use.
- https://github.com/computamike/dragon32-dev/blob/babf1b56f5e745e9da732a1522b681467e69767d/Readme.md
- https://github.com/computamike/dragon32-dev/blob/babf1b56f5e745e9da732a1522b681467e69767d/Makefile

### Relationships (reviewed)

The starter integrates the asm6809/a09 assembler choices with XRoar but is a distinct project rather than a bundled copy of those tools.
- https://github.com/computamike/dragon32-dev/blob/babf1b56f5e745e9da732a1522b681467e69767d/Readme.md
- https://github.com/computamike/dragon32-dev/blob/babf1b56f5e745e9da732a1522b681467e69767d/Makefile

## Dragon AGD Suite — Spectrum AGD conversion toolchain for Dragon/CoCo

Project ID: dragon-mpagd-suite · Overall audit: reviewed

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
  "display_title": "Dragon AGD Suite — Spectrum AGD conversion toolchain for Dragon/CoCo",
  "id": "dragon-mpagd-suite",
  "last_activity": "2019-09-07",
  "last_checked": "2026-10-31",
  "re_started": null,
  "reconstructed_languages": [
    "Motorola 6809 assembly"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/oss003/Dragon-MPAGD-Suite",
  "runtime_profiles": [
    {
      "evidence": [
        "https://github.com/oss003/Dragon-MPAGD-Suite/blob/3d7c60d82b8f237bfc518127cd71674175e69978/README.md"
      ],
      "name": "Dragon AGD Suite",
      "notes": "README lists these tools and DSK/VDK output; no host CPU or RAM minimum is stated.",
      "os": "MinGW, ASM6809 and XRoar",
      "platform": "Windows host"
    }
  ],
  "source_cpu": [],
  "source_language": [
    "AGD game data",
    "ZX Spectrum snapshots"
  ],
  "source_platforms": [
    "ZX Spectrum",
    "Arcade Game Designer"
  ],
  "status": "Documented AGD conversion/build suite for Dragon and CoCo targets; not independently run",
  "subjects": [
    "Arcade Game Designer games"
  ],
  "tags": [
    "dragon-32",
    "coco",
    "agd",
    "6809"
  ],
  "target_cpu": [
    "Motorola 6809"
  ],
  "target_kinds": [],
  "target_platforms": [
    "Dragon 32",
    "Dragon 64",
    "TRS-80 Color Computer"
  ],
  "techniques": [
    "AGD extraction",
    "6809 code generation",
    "DSK/VDK image generation"
  ],
  "title": "Dragon AGD Suite — Spectrum AGD conversion toolchain for Dragon/CoCo",
  "tool_kinds": [
    "compiler-toolchain",
    "disk-filesystem-tool",
    "asset-tool"
  ],
  "types": [
    "cross-platform game conversion toolchain",
    "media builder"
  ],
  "upstream_name": "Dragon-MPAGD-Suite",
  "work_kinds": []
}
```

### Identity (reviewed)

The repository documents a suite that extracts AGD games from Spectrum snapshots, compiles them for Dragon/CoCo and emits runnable disk images.
- https://github.com/oss003/dragon-mpagd-suite/blob/3d7c60d82b8f237bfc518127cd71674175e69978/README.md

### Classification (reviewed)

This is a cross-platform retro game-authoring/conversion toolchain; it should not be labeled as a reverse-engineered game or blanket RE-derived port.
- https://github.com/oss003/dragon-mpagd-suite/blob/3d7c60d82b8f237bfc518127cd71674175e69978/README.md

### Source CPU (not-applicable)

Source CPU is not applicable because the reviewed input is AGD game data extracted from snapshots, not an original machine-code program under analysis.
- https://github.com/oss003/dragon-mpagd-suite/blob/3d7c60d82b8f237bfc518127cd71674175e69978/README.md

### Target CPU (reviewed)

The README explicitly says the suite converts game data into 6809 format and uses ASM6809 for Dragon/CoCo output.
- https://github.com/oss003/dragon-mpagd-suite/blob/3d7c60d82b8f237bfc518127cd71674175e69978/README.md

### Build (reviewed)

The README enumerates MinGW, ASM6809 and XRoar plus compiler and disk-image steps; no conversion, compilation or emulation was run. Limitations: Primary documentation review only.
- https://github.com/oss003/dragon-mpagd-suite/blob/3d7c60d82b8f237bfc518127cd71674175e69978/README.md

### Runtime profiles (reviewed)

The documented Windows-host toolchain is captured without inferring host CPU/RAM or minimum target hardware.
- https://github.com/oss003/dragon-mpagd-suite/blob/3d7c60d82b8f237bfc518127cd71674175e69978/README.md

### AI (no-evidence-found)

No explicit development-AI attribution was found in the reviewed README; this does not establish non-use.
- https://github.com/oss003/dragon-mpagd-suite/blob/3d7c60d82b8f237bfc518127cd71674175e69978/README.md

### Relationships (reviewed)

The suite depends on AGD-format source material, ASM6809 and XRoar and targets both Dragon and CoCo media; those dependencies are not separate components of this record.
- https://github.com/oss003/dragon-mpagd-suite/blob/3d7c60d82b8f237bfc518127cd71674175e69978/README.md

## CasROMUtils — Dragon/CoCo cassette and multicart tooling

Project ID: casromutils-dragon-coco · Overall audit: reviewed

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
  "display_title": "CasROMUtils — Dragon/CoCo cassette and multicart tooling",
  "id": "casromutils-dragon-coco",
  "last_activity": "2021-11-21",
  "last_checked": "2026-10-31",
  "re_started": null,
  "reconstructed_languages": [
    "Pascal"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/prime6809/CasROMUtils",
  "runtime_profiles": [
    {
      "evidence": [
        "https://github.com/prime6809/CasROMUtils/blob/99bc7ae86921153583cda4a9f6d75619cbb787de/CasUtils/CasFix.pas",
        "https://github.com/prime6809/CasROMUtils/blob/99bc7ae86921153583cda4a9f6d75619cbb787de/RomLink/RomLink.pas"
      ],
      "name": "CasFix and RomLink",
      "notes": "Source comments document the compiler/host families; no CPU or RAM minimum is stated.",
      "os": "Windows or Linux; FreePascal 2.0.4 or later",
      "platform": "Modern host"
    }
  ],
  "source_cpu": [],
  "source_language": [
    "Dragon/CoCo cassette images",
    "ROM images"
  ],
  "source_platforms": [
    "Dragon 32",
    "Dragon 64",
    "Dragon Alpha",
    "TRS-80 Color Computer"
  ],
  "status": "FreePascal cassette repair and MegaCart image utilities reviewed from implementation; not independently compiled",
  "subjects": [
    "Dragon/CoCo cassette images",
    "Dragon/CoCo MegaCart images"
  ],
  "tags": [
    "dragon-32",
    "coco",
    "cassette",
    "megacart"
  ],
  "target_cpu": [],
  "target_kinds": [],
  "target_platforms": [
    "Windows",
    "Linux"
  ],
  "techniques": [
    "cassette checksum repair",
    "leader/sync reconstruction",
    "paged ROM packaging"
  ],
  "title": "CasROMUtils — Dragon/CoCo cassette and multicart tooling",
  "tool_kinds": [
    "disk-filesystem-tool",
    "rom-tool"
  ],
  "types": [
    "cassette image repair tool",
    "multicart image builder"
  ],
  "upstream_name": "CasROMUtils",
  "work_kinds": [
    "data-format-analysis"
  ]
}
```

### Identity (reviewed)

The inspected CasFix and RomLink sources implement Dragon/CoCo cassette repair/conversion and MegaCart paged-ROM construction.
- https://github.com/prime6809/casromutils/blob/99bc7ae86921153583cda4a9f6d75619cbb787de/CasUtils/CasFix.pas
- https://github.com/prime6809/casromutils/blob/99bc7ae86921153583cda4a9f6d75619cbb787de/RomLink/RomLink.pas

### Classification (reviewed)

This is host-side media analysis/repair and ROM packaging tooling, not a reconstructed title or native game port.
- https://github.com/prime6809/casromutils/blob/99bc7ae86921153583cda4a9f6d75619cbb787de/CasUtils/CasFix.pas
- https://github.com/prime6809/casromutils/blob/99bc7ae86921153583cda4a9f6d75619cbb787de/RomLink/RomLink.pas

### Source CPU (not-applicable)

Source CPU is not applicable because the tools inspect cassette and ROM-image data rather than a particular original executable.
- https://github.com/prime6809/casromutils/blob/99bc7ae86921153583cda4a9f6d75619cbb787de/CasUtils/CasFix.pas
- https://github.com/prime6809/casromutils/blob/99bc7ae86921153583cda4a9f6d75619cbb787de/RomLink/RomLink.pas

### Target CPU (not-applicable)

Target CPU is not applicable because the outputs are repaired cassette/media containers and packaged ROM pages, not generated native code.
- https://github.com/prime6809/casromutils/blob/99bc7ae86921153583cda4a9f6d75619cbb787de/CasUtils/CasFix.pas
- https://github.com/prime6809/casromutils/blob/99bc7ae86921153583cda4a9f6d75619cbb787de/RomLink/RomLink.pas

### Build (reviewed)

Source headers identify FreePascal 2.0.4+ and Windows/Linux builds; no compiler, cassette or ROM image was run. Limitations: Implementation and comments reviewed statically.
- https://github.com/prime6809/casromutils/blob/99bc7ae86921153583cda4a9f6d75619cbb787de/CasUtils/CasFix.pas
- https://github.com/prime6809/casromutils/blob/99bc7ae86921153583cda4a9f6d75619cbb787de/RomLink/RomLink.pas

### Runtime profiles (reviewed)

The explicit FreePascal and Windows/Linux host requirements are captured; no CPU/RAM minimum is stated.
- https://github.com/prime6809/casromutils/blob/99bc7ae86921153583cda4a9f6d75619cbb787de/CasUtils/CasFix.pas
- https://github.com/prime6809/casromutils/blob/99bc7ae86921153583cda4a9f6d75619cbb787de/RomLink/RomLink.pas

### AI (no-evidence-found)

No explicit development-AI attribution was found in the inspected Pascal sources; this does not establish non-use.
- https://github.com/prime6809/casromutils/blob/99bc7ae86921153583cda4a9f6d75619cbb787de/CasUtils/CasFix.pas
- https://github.com/prime6809/casromutils/blob/99bc7ae86921153583cda4a9f6d75619cbb787de/RomLink/RomLink.pas

### Relationships (reviewed)

CasFix and RomLink are complementary utilities in one coherent repository: cassette-image repair/conversion and Dragon/CoCo MegaCart image assembly.
- https://github.com/prime6809/casromutils/blob/99bc7ae86921153583cda4a9f6d75619cbb787de/CasUtils/CasFix.pas
- https://github.com/prime6809/casromutils/blob/99bc7ae86921153583cda4a9f6d75619cbb787de/RomLink/RomLink.pas

## Apple III Custom ROM — DAN II boot and monitor extension

Project ID: apple-iii-custom-rom · Overall audit: reviewed

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
  "display_title": "Apple III Custom ROM — DAN II boot and monitor extension",
  "id": "apple-iii-custom-rom",
  "last_activity": "2023-11-29",
  "last_checked": "2026-10-31",
  "re_started": null,
  "reconstructed_languages": [
    "6502 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/ThorstenBr/Apple_III_Custom_ROM",
  "runtime_profiles": [
    {
      "cpu_family": "6502",
      "evidence": [
        "https://github.com/ThorstenBr/Apple_III_Custom_ROM/blob/5fa8e6aa9891b70cb26e900b636b36b2d8c98163/README.md"
      ],
      "name": "Custom 4K/8K ROM",
      "notes": "README documents DAN II autoboot and extended monitor variants; no RAM minimum is stated.",
      "os": "Replacement 4 KiB ROM or banked 8 KiB ROM adapter",
      "platform": "Apple III"
    }
  ],
  "source_cpu": [
    "6502"
  ],
  "source_language": [
    "6502 assembly"
  ],
  "source_platforms": [
    "Apple III",
    "Apple II"
  ],
  "status": "Modified Apple III ROM sources for DAN II boot and extended monitor/disassembler variants",
  "subjects": [
    "Apple III system ROM",
    "DAN II Controller"
  ],
  "tags": [
    "apple-iii",
    "6502",
    "rom",
    "monitor"
  ],
  "target_cpu": [
    "6502"
  ],
  "target_kinds": [
    "firmware-rom",
    "development-tool"
  ],
  "target_platforms": [
    "Apple III"
  ],
  "techniques": [
    "ROM bank switching",
    "monitor extension",
    "6502 disassembler adaptation"
  ],
  "title": "Apple III Custom ROM — DAN II boot and monitor extension",
  "tool_kinds": [],
  "types": [
    "system ROM adaptation",
    "monitor extension"
  ],
  "upstream_name": "Apple_III_Custom_ROM",
  "work_kinds": [
    "source-restoration",
    "patching"
  ]
}
```

### Identity (reviewed)

The repository provides Apple III custom 4 KiB and banked 8 KiB ROM variants for DAN II boot and an extended monitor/disassembler.
- https://github.com/thorstenbr/apple_iii_custom_rom/blob/5fa8e6aa9891b70cb26e900b636b36b2d8c98163/README.md

### Classification (reviewed)

This is a source adaptation of the original Apple III ROM, with an Apple II disassembler routine incorporated; it is not wholly original homebrew or a binary-derived clean-room reconstruction.
- https://github.com/thorstenbr/apple_iii_custom_rom/blob/5fa8e6aa9891b70cb26e900b636b36b2d8c98163/README.md
- https://github.com/thorstenbr/apple_iii_custom_rom/blob/5fa8e6aa9891b70cb26e900b636b36b2d8c98163/source/ROM/monitor.s

### Source CPU (reviewed)

The monitor source explicitly selects the 6502 CPU, establishing the source firmware architecture.
- https://github.com/thorstenbr/apple_iii_custom_rom/blob/5fa8e6aa9891b70cb26e900b636b36b2d8c98163/source/ROM/monitor.s

### Target CPU (reviewed)

The custom Apple III ROM remains 6502 firmware and the assembled source explicitly targets 6502.
- https://github.com/thorstenbr/apple_iii_custom_rom/blob/5fa8e6aa9891b70cb26e900b636b36b2d8c98163/README.md
- https://github.com/thorstenbr/apple_iii_custom_rom/blob/5fa8e6aa9891b70cb26e900b636b36b2d8c98163/source/ROM/monitor.s

### Build (reviewed)

The repository provides buildable ROM source and documents the 4 KiB/8 KiB variants; no assembler, ROM image, adapter or Apple III was run. Limitations: Static source/documentation review only; output identity was not compared.
- https://github.com/thorstenbr/apple_iii_custom_rom/blob/5fa8e6aa9891b70cb26e900b636b36b2d8c98163/README.md
- https://github.com/thorstenbr/apple_iii_custom_rom/blob/5fa8e6aa9891b70cb26e900b636b36b2d8c98163/source/ROM/monitor.s

### Runtime profiles (reviewed)

The documented Apple III replacement-ROM and 8 KiB banked-adapter requirements are captured without inferring RAM or machine revision requirements.
- https://github.com/thorstenbr/apple_iii_custom_rom/blob/5fa8e6aa9891b70cb26e900b636b36b2d8c98163/README.md

### AI (no-evidence-found)

No explicit development-AI attribution was found in the inspected README/source; this does not establish non-use.
- https://github.com/thorstenbr/apple_iii_custom_rom/blob/5fa8e6aa9891b70cb26e900b636b36b2d8c98163/README.md
- https://github.com/thorstenbr/apple_iii_custom_rom/blob/5fa8e6aa9891b70cb26e900b636b36b2d8c98163/source/ROM/monitor.s

### Relationships (reviewed)

The README identifies the original Apple III ROM as the base, adds DAN II autoboot, and credits an Apple II ROM disassembler routine for the monitor extension.
- https://github.com/thorstenbr/apple_iii_custom_rom/blob/5fa8e6aa9891b70cb26e900b636b36b2d8c98163/README.md

## Apple III ROM-Drive Driver — SOS support for ProDOS ROM-Drive

Project ID: apple-iii-rom-drive-driver · Overall audit: partial

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
  "display_title": "Apple III ROM-Drive Driver — SOS support for ProDOS ROM-Drive",
  "id": "apple-iii-rom-drive-driver",
  "last_activity": "2026-10-11",
  "last_checked": "2026-10-31",
  "re_started": null,
  "reconstructed_languages": [
    "assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/david-schmidt/apple-iii-rom-drive-driver",
  "runtime_profiles": [
    {
      "evidence": [
        "https://github.com/david-schmidt/apple-iii-rom-drive-driver/blob/d28d588f1a99b904246b3844282cf54a28781e3a/README.md"
      ],
      "name": "A3ROMDRIVE.DRIVER",
      "notes": "Primary documentation describes read-only driver operation; no CPU, RAM or SOS-version floor is stated.",
      "os": "SOS with Terence Boldt ProDOS ROM-Drive card",
      "platform": "Apple III"
    }
  ],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Original read-only Apple III SOS driver for the ProDOS ROM-Drive card",
  "subjects": [
    "ProDOS ROM-Drive",
    "Apple III SOS"
  ],
  "tags": [
    "apple-iii",
    "sos",
    "device-driver",
    "original-homebrew"
  ],
  "target_cpu": [],
  "target_kinds": [
    "system-software",
    "development-tool"
  ],
  "target_platforms": [
    "Apple III"
  ],
  "techniques": [
    "SOS device driver",
    "ROM-drive block access"
  ],
  "title": "Apple III ROM-Drive Driver — SOS support for ProDOS ROM-Drive",
  "tool_kinds": [],
  "types": [
    "original homebrew",
    "SOS device driver"
  ],
  "upstream_name": "apple-iii-rom-drive-driver",
  "work_kinds": []
}
```

### Identity (reviewed)

The repository implements a read-only Apple III SOS driver for Terence Boldt's ProDOS ROM-Drive card.
- https://github.com/david-schmidt/apple-iii-rom-drive-driver/blob/d28d588f1a99b904246b3844282cf54a28781e3a/README.md
- https://github.com/david-schmidt/apple-iii-rom-drive-driver/blob/d28d588f1a99b904246b3844282cf54a28781e3a/a3romdrive.s

### Classification (reviewed)

This is explicitly original native driver/homebrew work, not a reverse-engineered or RE-derived project.
- https://github.com/david-schmidt/apple-iii-rom-drive-driver/blob/d28d588f1a99b904246b3844282cf54a28781e3a/README.md
- https://github.com/david-schmidt/apple-iii-rom-drive-driver/blob/d28d588f1a99b904246b3844282cf54a28781e3a/a3romdrive.s

### Source CPU (not-applicable)

Source CPU is not applicable because the project is original software rather than analysis of a pre-existing binary.
- https://github.com/david-schmidt/apple-iii-rom-drive-driver/blob/d28d588f1a99b904246b3844282cf54a28781e3a/README.md
- https://github.com/david-schmidt/apple-iii-rom-drive-driver/blob/d28d588f1a99b904246b3844282cf54a28781e3a/a3romdrive.s

### Target CPU (no-evidence-found)

The inspected README and driver source do not explicitly identify the output CPU; Apple III platform and assembly syntax alone were not used to infer it.
- https://github.com/david-schmidt/apple-iii-rom-drive-driver/blob/d28d588f1a99b904246b3844282cf54a28781e3a/README.md
- https://github.com/david-schmidt/apple-iii-rom-drive-driver/blob/d28d588f1a99b904246b3844282cf54a28781e3a/a3romdrive.s

### Build (reviewed)

The README gives the Python/a3driverutil and ca65 build dependencies; no assembly, packaging, card access or SOS boot was run. Limitations: Upstream-documented build only.
- https://github.com/david-schmidt/apple-iii-rom-drive-driver/blob/d28d588f1a99b904246b3844282cf54a28781e3a/README.md
- https://github.com/david-schmidt/apple-iii-rom-drive-driver/blob/d28d588f1a99b904246b3844282cf54a28781e3a/a3romdrive.s

### Runtime profiles (reviewed)

The explicit Apple III, SOS and ProDOS ROM-Drive card requirements are captured; no CPU, RAM or OS-version minimum is stated.
- https://github.com/david-schmidt/apple-iii-rom-drive-driver/blob/d28d588f1a99b904246b3844282cf54a28781e3a/README.md

### AI (no-evidence-found)

No explicit development-AI attribution was found in the inspected README/source; this does not establish non-use.
- https://github.com/david-schmidt/apple-iii-rom-drive-driver/blob/d28d588f1a99b904246b3844282cf54a28781e3a/README.md
- https://github.com/david-schmidt/apple-iii-rom-drive-driver/blob/d28d588f1a99b904246b3844282cf54a28781e3a/a3romdrive.s

### Relationships (reviewed)

The driver targets Terence Boldt's separate ProDOS ROM-Drive hardware and uses a3driverutil for SOS driver packaging; those dependencies remain distinct.
- https://github.com/david-schmidt/apple-iii-rom-drive-driver/blob/d28d588f1a99b904246b3844282cf54a28781e3a/README.md

## SOS HD Boot — Apple III ROM and kernel hard-disk boot adaptation

Project ID: soshdboot-apple-iii · Overall audit: reviewed

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
  "display_title": "SOS HD Boot — Apple III ROM and kernel hard-disk boot adaptation",
  "id": "soshdboot-apple-iii",
  "last_activity": "2025-03-24",
  "last_checked": "2026-10-31",
  "re_started": null,
  "reconstructed_languages": [
    "6502 assembly",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/robjustice/soshdboot",
  "runtime_profiles": [
    {
      "cpu_family": "6502",
      "evidence": [
        "https://github.com/robjustice/soshdboot/blob/154107c3dcf2e2084a60a1de1ade033d00fffb51/README.md"
      ],
      "min_ram_kib": 128,
      "name": "SOS HD Boot",
      "notes": "README states the boot loader supports 128K, 256K and 512K systems and reports testing on 256K/512K machines.",
      "os": "Modified SOS.KERNEL and ROM; ProDOS-compatible block card",
      "platform": "Apple III"
    }
  ],
  "source_cpu": [
    "6502"
  ],
  "source_language": [
    "6502 assembly"
  ],
  "source_platforms": [
    "Apple III"
  ],
  "status": "Source-built Apple III ROM/kernel/driver adaptation for booting from ProDOS block cards",
  "subjects": [
    "Apple III system ROM",
    "Apple III SOS"
  ],
  "tags": [
    "apple-iii",
    "6502",
    "sos",
    "boot-rom"
  ],
  "target_cpu": [
    "6502"
  ],
  "target_kinds": [
    "firmware-rom",
    "operating-system"
  ],
  "target_platforms": [
    "Apple III"
  ],
  "techniques": [
    "ROM boot adaptation",
    "SOS kernel patching",
    "block-device driver integration"
  ],
  "title": "SOS HD Boot — Apple III ROM and kernel hard-disk boot adaptation",
  "tool_kinds": [],
  "types": [
    "system ROM adaptation",
    "SOS kernel adaptation",
    "boot loader"
  ],
  "upstream_name": "soshdboot",
  "work_kinds": [
    "source-restoration",
    "patching"
  ]
}
```

### Identity (reviewed)

The repository supplies an updated Apple III ROM, modified SOS kernel, boot loaders and Disk3 driver for direct boot from ProDOS-compatible block cards.
- https://github.com/robjustice/soshdboot/blob/154107c3dcf2e2084a60a1de1ade033d00fffb51/README.md
- https://github.com/robjustice/soshdboot/blob/154107c3dcf2e2084a60a1de1ade033d00fffb51/src/rom/diskio.s

### Classification (reviewed)

This is an Apple III firmware/system-software source adaptation with original integration work, not a clean-room reconstruction or ordinary binary distribution.
- https://github.com/robjustice/soshdboot/blob/154107c3dcf2e2084a60a1de1ade033d00fffb51/README.md
- https://github.com/robjustice/soshdboot/blob/154107c3dcf2e2084a60a1de1ade033d00fffb51/src/rom/diskio.s

### Source CPU (reviewed)

The inspected ROM disk I/O source explicitly selects the 6502 CPU, establishing the source firmware architecture.
- https://github.com/robjustice/soshdboot/blob/154107c3dcf2e2084a60a1de1ade033d00fffb51/src/rom/diskio.s

### Target CPU (reviewed)

The built ROM/kernel components run on Apple III and the inspected source explicitly targets 6502.
- https://github.com/robjustice/soshdboot/blob/154107c3dcf2e2084a60a1de1ade033d00fffb51/README.md
- https://github.com/robjustice/soshdboot/blob/154107c3dcf2e2084a60a1de1ade033d00fffb51/src/rom/diskio.s

### Build (reviewed)

README documents ca65/ld65, Python 2.7, ROM/kernel build targets and MAME commands; no build, ROM installation, image mutation or emulator/hardware boot was run. Limitations: Primary documentation/source review only; claimed boot compatibility was not reproduced.
- https://github.com/robjustice/soshdboot/blob/154107c3dcf2e2084a60a1de1ade033d00fffb51/README.md
- https://github.com/robjustice/soshdboot/blob/154107c3dcf2e2084a60a1de1ade033d00fffb51/src/rom/diskio.s

### Runtime profiles (reviewed)

The README explicitly states 128K/256K/512K support, testing on 256K/512K, and the required modified ROM/SOS plus block card; 128 KiB is recorded as the documented floor.
- https://github.com/robjustice/soshdboot/blob/154107c3dcf2e2084a60a1de1ade033d00fffb51/README.md

### AI (no-evidence-found)

No explicit development-AI attribution was found in the inspected README/source; this does not establish non-use.
- https://github.com/robjustice/soshdboot/blob/154107c3dcf2e2084a60a1de1ade033d00fffb51/README.md
- https://github.com/robjustice/soshdboot/blob/154107c3dcf2e2084a60a1de1ade033d00fffb51/src/rom/diskio.s

### Relationships (reviewed)

The project integrates modified Apple III ROM/SOS components with ProDOS block cards and documents its Disk3 driver/boot-loader variants as one coherent boot stack.
- https://github.com/robjustice/soshdboot/blob/154107c3dcf2e2084a60a1de1ade033d00fffb51/README.md

## stos-atari-basic-source

Project ID: stos-atari-basic-source · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "stos-atari-basic-source",
  "last_checked": "2026-10-31",
  "runtime_profiles": [
    {
      "chipsets": [
        "Falcon DMA sound"
      ],
      "cpu_family": "Motorola 68000",
      "evidence": [
        "https://github.com/th-otto/STOS/blob/d11672715dce04d7ab30c5f4758d3b56ca63e421/extens/falc_snd/doc/falc_snd.txt"
      ],
      "min_cpu": "Motorola 68030",
      "min_ram_kib": 1024,
      "name": "Falcon 030 DMA Sound Extension v2.2",
      "notes": "Primary manual states Falcon 030 only, 1/4/14 MB RAM and RGB/VGA/TV monitor.",
      "os": "STOS Basic with STOSFIX3",
      "platform": "Atari Falcon 030"
    }
  ],
  "status": "Preserved STOS BASIC compiler/interpreter and extension sources; Falcon DMA Sound runtime requirements verified",
  "subjects": [
    "STOS BASIC",
    "GBP Extension",
    "Falcon 030 DMA Sound Extension",
    "Falcon Extension Suite"
  ]
}
```

Expected existing project SHA256: c20c5e152ff925311e4b76f413170b7782f7363c00e41fef6ad70713be07ec0d

### Identity (reviewed)

The repository remains the canonical STOS BASIC source collection and also preserves titled interpreter/compiler extensions, including GBP and the documented Falcon extension suite.
- https://github.com/th-otto/stos/blob/d11672715dce04d7ab30c5f4758d3b56ca63e421/doc/info.txt
- https://github.com/th-otto/stos/blob/d11672715dce04d7ab30c5f4758d3b56ca63e421/extens/gbp/README.md

### Classification (reviewed)

This is recovered/preserved historical development-system source plus extension sources; it is not a binary-derived reimplementation or ordinary mirror.
- https://github.com/th-otto/stos/blob/d11672715dce04d7ab30c5f4758d3b56ca63e421/doc/info.txt
- https://github.com/th-otto/stos/blob/d11672715dce04d7ab30c5f4758d3b56ca63e421/extens/gbp/README.md

### Source CPU (reviewed)

The existing Motorola 68000 source CPU remains appropriate for the Atari ST core; the Falcon sound manual separately documents 68030 execution for that extension and does not replace the project-wide original architecture.
- https://github.com/th-otto/stos/blob/d11672715dce04d7ab30c5f4758d3b56ca63e421/doc/info.txt
- https://github.com/th-otto/stos/blob/d11672715dce04d7ab30c5f4758d3b56ca63e421/extens/falc_snd/doc/falc_snd.txt

### Target CPU (reviewed)

The preserved compiler/interpreter target remains Motorola 68000-family ST software; the verified Falcon extension runtime is recorded as a variant requirement rather than broadening the canonical output CPU without evidence.
- https://github.com/th-otto/stos/blob/d11672715dce04d7ab30c5f4758d3b56ca63e421/doc/info.txt
- https://github.com/th-otto/stos/blob/d11672715dce04d7ab30c5f4758d3b56ca63e421/extens/falc_snd/doc/falc_snd.txt

### Build (needs-research)

The inspected extension materials provide source and historical usage context, including full GBP interpreter/compiler source, but do not establish a complete reproducible modern build for the core STOS compiler/interpreter. Next check: Trace the root/core build procedure and tool versions, then attempt a non-destructive build or locate an upstream reproducibility statement.
- https://github.com/th-otto/stos/blob/d11672715dce04d7ab30c5f4758d3b56ca63e421/doc/info.txt
- https://github.com/th-otto/stos/blob/d11672715dce04d7ab30c5f4758d3b56ca63e421/extens/gbp/README.md

### Runtime profiles (reviewed)

The Falcon DMA Sound manual explicitly requires an Atari Falcon 030, 1/4/14 MB RAM, RGB/VGA/TV display, STOS Basic and STOSFIX3; the lowest stated RAM value is captured without extrapolating to other STOS components.
- https://github.com/th-otto/stos/blob/d11672715dce04d7ab30c5f4758d3b56ca63e421/extens/falc_snd/doc/falc_snd.txt

### AI (no-evidence-found)

No explicit development-AI attribution was found in the inspected historical documentation/source materials; this does not establish non-use in later maintenance.
- https://github.com/th-otto/stos/blob/d11672715dce04d7ab30c5f4758d3b56ca63e421/doc/info.txt
- https://github.com/th-otto/stos/blob/d11672715dce04d7ab30c5f4758d3b56ca63e421/extens/gbp/README.md
- https://github.com/th-otto/stos/blob/d11672715dce04d7ab30c5f4758d3b56ca63e421/extens/falc_snd/doc/falc_snd.txt

### Relationships (needs-research)

The Falcon suite and GBP Extension are now identified as titled components in the STOS repository, but the provenance boundary between original historical core sources and later adapted/system-interface trees remains incompletely documented. Next check: Map the repository's orig and adapted source trees against named historical releases and extension authors before splitting or linking further component records.
- https://github.com/th-otto/stos/blob/d11672715dce04d7ab30c5f4758d3b56ca63e421/doc/info.txt
- https://github.com/th-otto/stos/blob/d11672715dce04d7ab30c5f4758d3b56ca63e421/extens/gbp/README.md

## Pinned evidence manifest

- apple3rom_monitor: https://github.com/thorstenbr/apple_iii_custom_rom/blob/5fa8e6aa9891b70cb26e900b636b36b2d8c98163/source/ROM/monitor.s (Git blob 86f7d89fe5bf150f03b23abd9bb004140ea93530)
- apple3rom_readme: https://github.com/thorstenbr/apple_iii_custom_rom/blob/5fa8e6aa9891b70cb26e900b636b36b2d8c98163/README.md (Git blob 03e6fd997added0b4b6c08c23583ece47cd8a4be)
- casfix_source: https://github.com/prime6809/casromutils/blob/99bc7ae86921153583cda4a9f6d75619cbb787de/CasUtils/CasFix.pas (Git blob 3621ee35fa0c79b8511937d7732ea20e62459806)
- ddos_readme: https://github.com/pulkomandy/ddosutils/blob/24029d98649b351edded672f51537dbd02fc9145/README.md (Git blob 4e5b04a708d4b0441411fa9048089afc23990313)
- dragondev_makefile: https://github.com/computamike/dragon32-dev/blob/babf1b56f5e745e9da732a1522b681467e69767d/Makefile (Git blob 4847938ab4059d93723f70e443cd96b2feb59e6a)
- dragondev_readme: https://github.com/computamike/dragon32-dev/blob/babf1b56f5e745e9da732a1522b681467e69767d/Readme.md (Git blob dbf01da122be31ddb076fa09fc9124e7add39e52)
- mpagd_readme: https://github.com/oss003/dragon-mpagd-suite/blob/3d7c60d82b8f237bfc518127cd71674175e69978/README.md (Git blob ed84581fd8cf125b81fb924b91c01f7f95b00042)
- romdrive_readme: https://github.com/david-schmidt/apple-iii-rom-drive-driver/blob/d28d588f1a99b904246b3844282cf54a28781e3a/README.md (Git blob 4d3d643b604e9dc2646b2da27dcdd84f0d4692f3)
- romdrive_source: https://github.com/david-schmidt/apple-iii-rom-drive-driver/blob/d28d588f1a99b904246b3844282cf54a28781e3a/a3romdrive.s (Git blob 4cd568313e68ea3a2a0c0feb5c5f5e99a31a0df7)
- romlink_source: https://github.com/prime6809/casromutils/blob/99bc7ae86921153583cda4a9f6d75619cbb787de/RomLink/RomLink.pas (Git blob 288c8b246efef7246c5734446cfef17e750955c8)
- soshd_diskio: https://github.com/robjustice/soshdboot/blob/154107c3dcf2e2084a60a1de1ade033d00fffb51/src/rom/diskio.s (Git blob 44253fff53f5766aecdd6de6995cd16879fdeeb8)
- soshd_readme: https://github.com/robjustice/soshdboot/blob/154107c3dcf2e2084a60a1de1ade033d00fffb51/README.md (Git blob 4a07688ede40db8b776c501f2f89d6d72aa031bc)
- stos_falcon_sound: https://github.com/th-otto/stos/blob/d11672715dce04d7ab30c5f4758d3b56ca63e421/extens/falc_snd/doc/falc_snd.txt (Git blob 807971c8774233cd596aebc506606628dc65dbd0)
- stos_gbp: https://github.com/th-otto/stos/blob/d11672715dce04d7ab30c5f4758d3b56ca63e421/extens/gbp/README.md (Git blob e0e8ab93fd0115f8ae451c5378ee5674a39dcad8)
- stos_info: https://github.com/th-otto/stos/blob/d11672715dce04d7ab30c5f4758d3b56ca63e421/doc/info.txt (Git blob ed490f861c2238669c9bc76f03dfff5f9bcd4236)

## Sources

```json
[
  {
    "id": "github-pulkomandy-ddosutils",
    "kind": "github-repository",
    "reason": "DragonDOS/VDK extraction and data conversion utilities reviewed from primary README.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/pulkomandy/ddosutils"
  },
  {
    "id": "github-computamike-dragon32-dev",
    "kind": "github-repository",
    "reason": "Dragon 32 containerized 6809 ROM development starter reviewed from README and Makefile.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/computamike/dragon32-dev"
  },
  {
    "id": "github-oss003-dragon-mpagd-suite",
    "kind": "github-repository",
    "reason": "AGD-to-Dragon/CoCo conversion and media toolchain reviewed from primary documentation.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/oss003/Dragon-MPAGD-Suite"
  },
  {
    "id": "github-prime6809-casromutils",
    "kind": "github-repository",
    "reason": "Dragon/CoCo cassette repair and MegaCart packaging tools reviewed from implementations.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/prime6809/CasROMUtils"
  },
  {
    "id": "github-osresearch-model100",
    "kind": "github-repository",
    "reason": "Model 100 replacement-mainboard candidate reviewed and excluded as hardware-focused without a distinct tracker-qualifying software project.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/osresearch/model100"
  },
  {
    "id": "github-kethku-model100-firmware",
    "kind": "github-repository",
    "reason": "Search false positive reviewed; repository is Keyboardio Model 01 firmware, not TRS-80 Model 100 work.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/Kethku/Model100-Firmware"
  },
  {
    "id": "github-mew-cx-trs80m100-forth",
    "kind": "github-repository",
    "reason": "Historical 1986 fig-FORTH source archive reviewed; no distinct active preservation or reconstruction contribution established.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/mew-cx/trs80m100_forth"
  },
  {
    "id": "github-sboger-virtualt-devterm",
    "kind": "github-repository",
    "reason": "VirtualT DevTerm repackaging/maintenance candidate reviewed without a distinct archaeology contribution.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/sboger/VirtualT-DevTerm"
  },
  {
    "id": "github-thorstenbr-apple-iii-custom-rom",
    "kind": "github-repository",
    "reason": "Apple III custom system ROM source adaptation reviewed with explicit 6502 evidence.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/ThorstenBr/Apple_III_Custom_ROM"
  },
  {
    "id": "github-thorstenbr-appleiii-diskii",
    "kind": "github-repository",
    "reason": "Apple III Disk II candidate reviewed and excluded as a hardware adapter/PCB project.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/ThorstenBr/AppleIII_diskII"
  },
  {
    "id": "github-david-schmidt-apple-iii-rom-drive-driver",
    "kind": "github-repository",
    "reason": "Original Apple III SOS ROM-Drive driver reviewed from README and assembly source.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/david-schmidt/apple-iii-rom-drive-driver"
  },
  {
    "id": "github-robjustice-soshdboot",
    "kind": "github-repository",
    "reason": "Apple III ROM/SOS hard-disk boot adaptation reviewed with build, CPU and runtime evidence.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/robjustice/soshdboot"
  },
  {
    "id": "github-datajerk-apple3rtr",
    "kind": "github-repository",
    "reason": "Apple III MAME runtime/distribution package reviewed without a distinct development or recovery contribution.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/datajerk/apple3rtr"
  }
]
```

## Source updates

```json
[
  {
    "id": "github-th-otto-stos",
    "last_reviewed": "2026-10-31",
    "reason": "Component-level review verified GBP and Falcon extension identities plus explicit Falcon 030 DMA Sound runtime requirements; core build reproducibility and orig/adapted provenance still need research.",
    "review_state": "partial"
  }
]
```

## Task updates

```json
[
  {
    "id": "task-th-otto-stos-component-review",
    "last_reviewed": "2026-10-31",
    "notes_append": "Reviewed doc/info.txt, GBP Extension README and Falcon DMA Sound manual at d116727. Verified titled extension components and captured Falcon 030/1 MB/STOSFIX3 runtime requirements. Remaining work is narrowed to core build reproducibility and mapping original versus adapted source-tree provenance.",
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
      "https://github.com/pulkomandy/ddosutils/blob/24029d98649b351edded672f51537dbd02fc9145/README.md"
    ],
    "id": "discovery-2026-10-31-ddosutils-promoted",
    "project_ids": [
      "dragon-dos-utils-unix"
    ],
    "reason": "Verified DragonDOS/VDK filesystem extraction and BASIC/DosDream conversion tooling.",
    "source_ids": [
      "github-pulkomandy-ddosutils"
    ],
    "title": "Dragon DOS Utils",
    "url": "https://github.com/pulkomandy/ddosutils"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/computamike/dragon32-dev/blob/babf1b56f5e745e9da732a1522b681467e69767d/Readme.md"
    ],
    "id": "discovery-2026-10-31-dragon32-dev-promoted",
    "project_ids": [
      "dragon32-dev-devcontainer"
    ],
    "reason": "Verified reproducible Dragon 32 6809 ROM starter with assembler and XRoar workflow.",
    "source_ids": [
      "github-computamike-dragon32-dev"
    ],
    "title": "Dragon 32 DevContainer",
    "url": "https://github.com/computamike/dragon32-dev"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/oss003/Dragon-MPAGD-Suite/blob/3d7c60d82b8f237bfc518127cd71674175e69978/README.md"
    ],
    "id": "discovery-2026-10-31-dragon-mpagd-promoted",
    "project_ids": [
      "dragon-mpagd-suite"
    ],
    "reason": "Verified AGD extraction, 6809 compilation and Dragon/CoCo disk-image toolchain.",
    "source_ids": [
      "github-oss003-dragon-mpagd-suite"
    ],
    "title": "Dragon AGD Suite",
    "url": "https://github.com/oss003/Dragon-MPAGD-Suite"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/prime6809/CasROMUtils/blob/99bc7ae86921153583cda4a9f6d75619cbb787de/CasUtils/CasFix.pas",
      "https://github.com/prime6809/CasROMUtils/blob/99bc7ae86921153583cda4a9f6d75619cbb787de/RomLink/RomLink.pas"
    ],
    "id": "discovery-2026-10-31-casromutils-promoted",
    "project_ids": [
      "casromutils-dragon-coco"
    ],
    "reason": "Verified distinct cassette-image repair/conversion and Dragon/CoCo MegaCart packaging utilities.",
    "source_ids": [
      "github-prime6809-casromutils"
    ],
    "title": "CasROMUtils",
    "url": "https://github.com/prime6809/CasROMUtils"
  },
  {
    "decision": "excluded",
    "evidence_urls": [
      "https://github.com/osresearch/model100"
    ],
    "id": "discovery-2026-10-31-model100-mainboard-excluded",
    "reason": "Primary README describes an iCE40/Teensy replacement-mainboard hardware project; no distinct retro-development or software-archaeology tool was established.",
    "source_ids": [
      "github-osresearch-model100"
    ],
    "title": "Model 100 modern mainboard",
    "url": "https://github.com/osresearch/model100"
  },
  {
    "decision": "excluded",
    "evidence_urls": [
      "https://github.com/Kethku/Model100-Firmware"
    ],
    "id": "discovery-2026-10-31-kethku-model100-excluded",
    "reason": "Search false positive: the primary README identifies Keyboardio Model 01 keyboard firmware, not TRS-80 Model 100 work.",
    "source_ids": [
      "github-kethku-model100-firmware"
    ],
    "title": "Model100-Firmware",
    "url": "https://github.com/Kethku/Model100-Firmware"
  },
  {
    "decision": "excluded",
    "evidence_urls": [
      "https://github.com/mew-cx/trs80m100_forth"
    ],
    "id": "discovery-2026-10-31-trs80m100-forth-excluded",
    "reason": "The reviewed repository is a bare archive of a 1986 fig-FORTH source listing; no distinct active preservation, reconstruction or tooling contribution was established.",
    "source_ids": [
      "github-mew-cx-trs80m100-forth"
    ],
    "title": "TRS-80 Model 100 fig-FORTH source",
    "url": "https://github.com/mew-cx/trs80m100_forth"
  },
  {
    "decision": "excluded",
    "evidence_urls": [
      "https://github.com/sboger/VirtualT-DevTerm"
    ],
    "id": "discovery-2026-10-31-virtualt-devterm-excluded",
    "reason": "Primary README presents a repurposed port of defunct VirtualT for DevTerm; the reviewed changes do not establish a distinct archaeology contribution beyond platform packaging/maintenance.",
    "source_ids": [
      "github-sboger-virtualt-devterm"
    ],
    "title": "VirtualT DevTerm",
    "url": "https://github.com/sboger/VirtualT-DevTerm"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/ThorstenBr/Apple_III_Custom_ROM/blob/5fa8e6aa9891b70cb26e900b636b36b2d8c98163/README.md"
    ],
    "id": "discovery-2026-10-31-apple-iii-custom-rom-promoted",
    "project_ids": [
      "apple-iii-custom-rom"
    ],
    "reason": "Verified Apple III ROM source adaptation with DAN II boot, monitor extensions and explicit 6502 target evidence.",
    "source_ids": [
      "github-thorstenbr-apple-iii-custom-rom"
    ],
    "title": "Apple III Custom ROM",
    "url": "https://github.com/ThorstenBr/Apple_III_Custom_ROM"
  },
  {
    "decision": "excluded",
    "evidence_urls": [
      "https://github.com/ThorstenBr/AppleIII_diskII"
    ],
    "id": "discovery-2026-10-31-appleiii-diskii-excluded",
    "reason": "The reviewed candidate is a hardware adapter/PCB project without a distinct tracker-qualifying software component.",
    "source_ids": [
      "github-thorstenbr-appleiii-diskii"
    ],
    "title": "Apple III Disk II adapter",
    "url": "https://github.com/ThorstenBr/AppleIII_diskII"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/david-schmidt/apple-iii-rom-drive-driver/blob/d28d588f1a99b904246b3844282cf54a28781e3a/README.md"
    ],
    "id": "discovery-2026-10-31-apple-iii-rom-drive-driver-promoted",
    "project_ids": [
      "apple-iii-rom-drive-driver"
    ],
    "reason": "Verified original read-only SOS device driver and documented ca65 build path for ProDOS ROM-Drive hardware.",
    "source_ids": [
      "github-david-schmidt-apple-iii-rom-drive-driver"
    ],
    "title": "Apple III ROM-Drive Driver",
    "url": "https://github.com/david-schmidt/apple-iii-rom-drive-driver"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/robjustice/soshdboot/blob/154107c3dcf2e2084a60a1de1ade033d00fffb51/README.md"
    ],
    "id": "discovery-2026-10-31-soshdboot-promoted",
    "project_ids": [
      "soshdboot-apple-iii"
    ],
    "reason": "Verified Apple III ROM/SOS hard-disk boot adaptation with explicit 6502 source, build and memory support evidence.",
    "source_ids": [
      "github-robjustice-soshdboot"
    ],
    "title": "SOS HD Boot",
    "url": "https://github.com/robjustice/soshdboot"
  },
  {
    "decision": "excluded",
    "evidence_urls": [
      "https://github.com/datajerk/apple3rtr"
    ],
    "id": "discovery-2026-10-31-apple3rtr-excluded",
    "reason": "The reviewed repository is an Apple III MAME runtime/distribution package with bundled images and scripts; no distinct development, reconstruction or recovery contribution was established.",
    "source_ids": [
      "github-datajerk-apple3rtr"
    ],
    "title": "apple3rtr",
    "url": "https://github.com/datajerk/apple3rtr"
  }
]
```

## Research event notes

The CPU audit queue returned zero unresolved source/target CPU areas, so no CPU value was inferred merely to satisfy a quota. Fresh GitHub repository/README searches were '"Dragon 32" disassembly source reconstruction', '"TRS-80 Model 100" disassembly development tooling', and '"Apple III" source disassembly homebrew tooling'; each narrow query returned no promotable candidate, so the repository route was broadened to 'dragon32', 'model100', and 'apple iii' without star, age, or recent-push filters. Thirteen canonical candidate URLs were screened and reviewed: seven promoted and six excluded. The STOS source/task queue was selected as an old partial component review and advanced with Falcon extension/runtime evidence. Read-only review: no compiler, assembler, ROM, disk/cassette image, emulator, hardware, firmware, driver, or destructive utility was run.
