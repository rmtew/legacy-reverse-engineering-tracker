# Personal Amiga, Kult, CPC and SC-3000 discovery pass

Personally screen 94 search hits, inspect nine new roots, add six source-backed projects and defer three candidates.

Date: 2026-10-26 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- markyturtle-newzealandstory-amiga / Build (reviewed): Read-only source review; no upstream build, game, image or firmware execution. Upstream success statements remain attributed rather than independently verified.
- markyturtle-newzealandstory-amiga / Runtime profiles (no-evidence-found): No independent minimum CPU/RAM/chipset compatibility test was performed; hardware and format limitations remain qualified in build notes.
- markyturtle-newzealandstory-amiga / AI (no-evidence-found): No actual development-AI contribution or named model established in inspected files. Agent instructions, prose style and missing attribution do not establish use or non-use.
- hunkstalker-kult-atari-st-decomp / Build (reviewed): Read-only source review; no upstream build, game, image or firmware execution. Upstream success statements remain attributed rather than independently verified.
- hunkstalker-kult-atari-st-decomp / Runtime profiles (no-evidence-found): No independent minimum CPU/RAM/chipset compatibility test was performed; hardware and format limitations remain qualified in build notes.
- hunkstalker-kult-atari-st-decomp / AI (no-evidence-found): No actual development-AI contribution or named model established in inspected files. Agent instructions, prose style and missing attribution do not establish use or non-use.
- kaosoverride-capricerpi / Target CPU (no-evidence-found): No explicit host/native minimum ISA established in reviewed build material; board names are kept separately from CPU requirements.
- kaosoverride-capricerpi / Build (reviewed): Read-only source review; no upstream build, game, image or firmware execution. Upstream success statements remain attributed rather than independently verified.
- kaosoverride-capricerpi / Runtime profiles (no-evidence-found): No independent minimum CPU/RAM/chipset compatibility test was performed; hardware and format limitations remain qualified in build notes.
- kaosoverride-capricerpi / AI (no-evidence-found): No actual development-AI contribution or named model established in inspected files. Agent instructions, prose style and missing attribution do not establish use or non-use.
- djopensource-who-ate-rudys-sandwich / Source CPU (no-evidence-found): Interpreted BASIC source identifies CPC 464 but does not itself declare a machine-code instruction set; no CPU value asserted.
- djopensource-who-ate-rudys-sandwich / Target CPU (no-evidence-found): No explicit host/native minimum ISA established in reviewed build material; board names are kept separately from CPU requirements.
- djopensource-who-ate-rudys-sandwich / Build (reviewed): Read-only source review; no upstream build, game, image or firmware execution. Upstream success statements remain attributed rather than independently verified.
- djopensource-who-ate-rudys-sandwich / Runtime profiles (no-evidence-found): No independent minimum CPU/RAM/chipset compatibility test was performed; hardware and format limitations remain qualified in build notes.
- djopensource-who-ate-rudys-sandwich / AI (no-evidence-found): No actual development-AI contribution or named model established in inspected files. Agent instructions, prose style and missing attribution do not establish use or non-use.
- shippoiincho-sc3000emulator / Target CPU (no-evidence-found): No explicit host/native minimum ISA established in reviewed build material; board names are kept separately from CPU requirements.
- shippoiincho-sc3000emulator / Build (reviewed): Read-only source review; no upstream build, game, image or firmware execution. Upstream success statements remain attributed rather than independently verified.
- shippoiincho-sc3000emulator / Runtime profiles (no-evidence-found): No independent minimum CPU/RAM/chipset compatibility test was performed; hardware and format limitations remain qualified in build notes.
- shippoiincho-sc3000emulator / AI (no-evidence-found): No actual development-AI contribution or named model established in inspected files. Agent instructions, prose style and missing attribution do not establish use or non-use.
- siriokds-sc-3000-keyboard-support / Build (reviewed): Read-only source review; no upstream build, game, image or firmware execution. Upstream success statements remain attributed rather than independently verified.
- siriokds-sc-3000-keyboard-support / Runtime profiles (no-evidence-found): No independent minimum CPU/RAM/chipset compatibility test was performed; hardware and format limitations remain qualified in build notes.
- siriokds-sc-3000-keyboard-support / AI (no-evidence-found): No actual development-AI contribution or named model established in inspected files. Agent instructions, prose style and missing attribution do not establish use or non-use.

## The New Zealand Story — Amiga disassembly and disk rebuild

Project ID: markyturtle-newzealandstory-amiga · Overall audit: partial

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
    "playable": true,
    "runnable": true
  },
  "display_title": "The New Zealand Story — Amiga disassembly and disk rebuild",
  "id": "markyturtle-newzealandstory-amiga",
  "last_activity": null,
  "last_checked": "2026-10-26",
  "re_started": null,
  "reconstructed_languages": [
    "m68k assembly",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/MarkyTurtle/NewzealandStory--Amiga",
  "runtime_profiles": [],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [
    "m68k assembly",
    "Python"
  ],
  "source_platforms": [
    "Amiga"
  ],
  "status": "Source reviewed; upstream build claims qualified in notes",
  "subjects": [
    "The New Zealand Story"
  ],
  "tags": [],
  "target_cpu": [
    "m68k"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Amiga"
  ],
  "techniques": [],
  "title": "The New Zealand Story — Amiga disassembly and disk rebuild",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "NewzealandStory--Amiga",
  "work_kinds": [
    "disassembly",
    "source-reconstruction",
    "patching"
  ]
}
```

### Identity (reviewed)

The New Zealand Story — Amiga disassembly and disk rebuild. Immutable root listing and linked source/build material personally reviewed.
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/blob/085eb38546bdae4de6c021ae52d7e62f7cd287f4/README.md
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/blob/085eb38546bdae4de6c021ae52d7e62f7cd287f4/BUILDING.md
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/blob/085eb38546bdae4de6c021ae52d7e62f7cd287f4/original/build.sh
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/blob/085eb38546bdae4de6c021ae52d7e62f7cd287f4/enhanced/src/diskload.s

### Classification (reviewed)

Original main, loader and two boot sources have byte-comparison build gates; a separate enhanced path replaces disk routines and boot chain to build an AmigaDOS-format disk. Extracted graphics/music and tools are included. Keep original-byte matching distinct from the deliberately modified enhanced build.
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/blob/085eb38546bdae4de6c021ae52d7e62f7cd287f4/README.md
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/blob/085eb38546bdae4de6c021ae52d7e62f7cd287f4/BUILDING.md
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/blob/085eb38546bdae4de6c021ae52d7e62f7cd287f4/original/build.sh
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/blob/085eb38546bdae4de6c021ae52d7e62f7cd287f4/enhanced/src/diskload.s

### Source CPU (reviewed)

Architecture established by inspected assembly or named emulator CPU implementation: m68k.
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/blob/085eb38546bdae4de6c021ae52d7e62f7cd287f4/README.md
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/blob/085eb38546bdae4de6c021ae52d7e62f7cd287f4/BUILDING.md
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/blob/085eb38546bdae4de6c021ae52d7e62f7cd287f4/original/build.sh
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/blob/085eb38546bdae4de6c021ae52d7e62f7cd287f4/enhanced/src/diskload.s

### Target CPU (reviewed)

Native assembly output uses m68k.
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/blob/085eb38546bdae4de6c021ae52d7e62f7cd287f4/README.md
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/blob/085eb38546bdae4de6c021ae52d7e62f7cd287f4/BUILDING.md
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/blob/085eb38546bdae4de6c021ae52d7e62f7cd287f4/original/build.sh
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/blob/085eb38546bdae4de6c021ae52d7e62f7cd287f4/enhanced/src/diskload.s

### Build (reviewed)

BUILDING.md and original/build.sh specify vasm -m68000 and hashes for four original binaries plus packed main; README reports enhanced boot/play in FS-UAE, with WinUAE and real hardware still untested. These are upstream claims, not runs performed in this pass. Limitations: Read-only source review; no upstream build, game, image or firmware execution. Upstream success statements remain attributed rather than independently verified.
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/blob/085eb38546bdae4de6c021ae52d7e62f7cd287f4/README.md
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/blob/085eb38546bdae4de6c021ae52d7e62f7cd287f4/BUILDING.md
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/blob/085eb38546bdae4de6c021ae52d7e62f7cd287f4/original/build.sh
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/blob/085eb38546bdae4de6c021ae52d7e62f7cd287f4/enhanced/src/diskload.s

### Runtime profiles (no-evidence-found)

No independent minimum CPU/RAM/chipset compatibility test was performed; hardware and format limitations remain qualified in build notes.
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/blob/085eb38546bdae4de6c021ae52d7e62f7cd287f4/README.md
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/blob/085eb38546bdae4de6c021ae52d7e62f7cd287f4/BUILDING.md
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/blob/085eb38546bdae4de6c021ae52d7e62f7cd287f4/original/build.sh
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/blob/085eb38546bdae4de6c021ae52d7e62f7cd287f4/enhanced/src/diskload.s

### AI (no-evidence-found)

No actual development-AI contribution or named model established in inspected files. Agent instructions, prose style and missing attribution do not establish use or non-use.
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/blob/085eb38546bdae4de6c021ae52d7e62f7cd287f4/README.md
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/blob/085eb38546bdae4de6c021ae52d7e62f7cd287f4/BUILDING.md
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/blob/085eb38546bdae4de6c021ae52d7e62f7cd287f4/original/build.sh
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/blob/085eb38546bdae4de6c021ae52d7e62f7cd287f4/enhanced/src/diskload.s

### Relationships (reviewed)

Uses the author's 4489_byteloader in the enhanced native Amiga game. The study emulator is analysis tooling, not evidence that the shipped Amiga path is baked emulation.
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/blob/085eb38546bdae4de6c021ae52d7e62f7cd287f4/README.md
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/blob/085eb38546bdae4de6c021ae52d7e62f7cd287f4/BUILDING.md
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/blob/085eb38546bdae4de6c021ae52d7e62f7cd287f4/original/build.sh
- https://github.com/MarkyTurtle/NewzealandStory--Amiga/blob/085eb38546bdae4de6c021ae52d7e62f7cd287f4/enhanced/src/diskload.s

## Kult: The Temple of Flying Saucers — Atari ST matching reconstruction

Project ID: hunkstalker-kult-atari-st-decomp · Overall audit: partial

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
  "display_title": "Kult: The Temple of Flying Saucers — Atari ST matching reconstruction",
  "id": "hunkstalker-kult-atari-st-decomp",
  "last_activity": null,
  "last_checked": "2026-10-26",
  "re_started": null,
  "reconstructed_languages": [
    "m68k assembly",
    "C",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/hunkstalker/kult-atari-st-decomp",
  "runtime_profiles": [],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [
    "m68k assembly",
    "C",
    "Python"
  ],
  "source_platforms": [
    "Atari ST"
  ],
  "status": "Source reviewed; upstream build claims qualified in notes",
  "subjects": [
    "Kult: The Temple of Flying Saucers"
  ],
  "tags": [],
  "target_cpu": [
    "m68k"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Atari ST"
  ],
  "techniques": [],
  "title": "Kult: The Temple of Flying Saucers — Atari ST matching reconstruction",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "kult-atari-st-decomp",
  "work_kinds": [
    "disassembly",
    "source-reconstruction"
  ]
}
```

### Identity (reviewed)

Kult: The Temple of Flying Saucers — Atari ST matching reconstruction. Immutable root listing and linked source/build material personally reviewed.
- https://github.com/hunkstalker/kult-atari-st-decomp/blob/5ef7c171dc71760bc9bb1e6abe4b0405319e4f5f/README.md
- https://github.com/hunkstalker/kult-atari-st-decomp/blob/5ef7c171dc71760bc9bb1e6abe4b0405319e4f5f/matching/Makefile
- https://github.com/hunkstalker/kult-atari-st-decomp/blob/5ef7c171dc71760bc9bb1e6abe4b0405319e4f5f/matching/src/auto_011e5e.s

### Classification (reviewed)

Assembly reconstruction of the original Atari ST engine with transcribed tables, Alcyon C startup/music and relocation reconstruction. Concrete assembly and build scripts are present; not merely a decompilation goal.
- https://github.com/hunkstalker/kult-atari-st-decomp/blob/5ef7c171dc71760bc9bb1e6abe4b0405319e4f5f/README.md
- https://github.com/hunkstalker/kult-atari-st-decomp/blob/5ef7c171dc71760bc9bb1e6abe4b0405319e4f5f/matching/Makefile
- https://github.com/hunkstalker/kult-atari-st-decomp/blob/5ef7c171dc71760bc9bb1e6abe4b0405319e4f5f/matching/src/auto_011e5e.s

### Source CPU (reviewed)

Architecture established by inspected assembly or named emulator CPU implementation: m68k.
- https://github.com/hunkstalker/kult-atari-st-decomp/blob/5ef7c171dc71760bc9bb1e6abe4b0405319e4f5f/README.md
- https://github.com/hunkstalker/kult-atari-st-decomp/blob/5ef7c171dc71760bc9bb1e6abe4b0405319e4f5f/matching/Makefile
- https://github.com/hunkstalker/kult-atari-st-decomp/blob/5ef7c171dc71760bc9bb1e6abe4b0405319e4f5f/matching/src/auto_011e5e.s

### Target CPU (reviewed)

Native assembly output uses m68k.
- https://github.com/hunkstalker/kult-atari-st-decomp/blob/5ef7c171dc71760bc9bb1e6abe4b0405319e4f5f/README.md
- https://github.com/hunkstalker/kult-atari-st-decomp/blob/5ef7c171dc71760bc9bb1e6abe4b0405319e4f5f/matching/Makefile
- https://github.com/hunkstalker/kult-atari-st-decomp/blob/5ef7c171dc71760bc9bb1e6abe4b0405319e4f5f/matching/src/auto_011e5e.s

### Build (reviewed)

Upstream reports a byte-identical 184291-byte KULT.PRG and all 2171 relocations. make vasm/check/indep are documented. Initial resource ingestion requires the owner's original PRG; independence means no original PRG at build time after ingestion, not asset-free building. No build run here. Limitations: Read-only source review; no upstream build, game, image or firmware execution. Upstream success statements remain attributed rather than independently verified.
- https://github.com/hunkstalker/kult-atari-st-decomp/blob/5ef7c171dc71760bc9bb1e6abe4b0405319e4f5f/README.md
- https://github.com/hunkstalker/kult-atari-st-decomp/blob/5ef7c171dc71760bc9bb1e6abe4b0405319e4f5f/matching/Makefile
- https://github.com/hunkstalker/kult-atari-st-decomp/blob/5ef7c171dc71760bc9bb1e6abe4b0405319e4f5f/matching/src/auto_011e5e.s

### Runtime profiles (no-evidence-found)

No independent minimum CPU/RAM/chipset compatibility test was performed; hardware and format limitations remain qualified in build notes.
- https://github.com/hunkstalker/kult-atari-st-decomp/blob/5ef7c171dc71760bc9bb1e6abe4b0405319e4f5f/README.md
- https://github.com/hunkstalker/kult-atari-st-decomp/blob/5ef7c171dc71760bc9bb1e6abe4b0405319e4f5f/matching/Makefile
- https://github.com/hunkstalker/kult-atari-st-decomp/blob/5ef7c171dc71760bc9bb1e6abe4b0405319e4f5f/matching/src/auto_011e5e.s

### AI (no-evidence-found)

No actual development-AI contribution or named model established in inspected files. Agent instructions, prose style and missing attribution do not establish use or non-use.
- https://github.com/hunkstalker/kult-atari-st-decomp/blob/5ef7c171dc71760bc9bb1e6abe4b0405319e4f5f/README.md
- https://github.com/hunkstalker/kult-atari-st-decomp/blob/5ef7c171dc71760bc9bb1e6abe4b0405319e4f5f/matching/Makefile
- https://github.com/hunkstalker/kult-atari-st-decomp/blob/5ef7c171dc71760bc9bb1e6abe4b0405319e4f5f/matching/src/auto_011e5e.s

### Relationships (reviewed)

Separate related kult-atari-st-c repository is a C core and differential harness, not the matching ASM deliverable. Reviewed separately and not silently represented as a playable native port.
- https://github.com/hunkstalker/kult-atari-st-decomp/blob/5ef7c171dc71760bc9bb1e6abe4b0405319e4f5f/README.md
- https://github.com/hunkstalker/kult-atari-st-decomp/blob/5ef7c171dc71760bc9bb1e6abe4b0405319e4f5f/matching/Makefile
- https://github.com/hunkstalker/kult-atari-st-decomp/blob/5ef7c171dc71760bc9bb1e6abe4b0405319e4f5f/matching/src/auto_011e5e.s

## CapriceRPI — Raspberry Pi CPC emulator port

Project ID: kaosoverride-capricerpi · Overall audit: partial

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
  "display_title": "CapriceRPI — Raspberry Pi CPC emulator port",
  "id": "kaosoverride-capricerpi",
  "last_activity": null,
  "last_checked": "2026-10-26",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "C++"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/KaosOverride/CapriceRPI",
  "runtime_profiles": [],
  "source_cpu": [
    "Z80"
  ],
  "source_language": [
    "C",
    "C++"
  ],
  "source_platforms": [
    "Amstrad CPC"
  ],
  "status": "Source reviewed; upstream build claims qualified in notes",
  "subjects": [
    "CapriceRPI"
  ],
  "tags": [],
  "target_cpu": [],
  "target_kinds": [],
  "target_platforms": [
    "Raspberry Pi"
  ],
  "techniques": [],
  "title": "CapriceRPI — Raspberry Pi CPC emulator port",
  "tool_kinds": [
    "emulator"
  ],
  "types": [
    "tooling"
  ],
  "upstream_name": "CapriceRPI",
  "work_kinds": []
}
```

### Identity (reviewed)

CapriceRPI — Raspberry Pi CPC emulator port. Immutable root listing and linked source/build material personally reviewed.
- https://github.com/KaosOverride/CapriceRPI/blob/7d86ebdc6a5e645220c6f30cf407ac57c3256054/README%20for%20this%20port.txt
- https://github.com/KaosOverride/CapriceRPI/blob/7d86ebdc6a5e645220c6f30cf407ac57c3256054/src/makefile

### Classification (reviewed)

Substantive Caprice32 4.1.0 adaptation with joystick-driven virtual keyboard, four-controller/ToTo support, autorun, snapshots and Pi-specific display handling. Includes emulator core and source build files rather than only a packaged binary.
- https://github.com/KaosOverride/CapriceRPI/blob/7d86ebdc6a5e645220c6f30cf407ac57c3256054/README%20for%20this%20port.txt
- https://github.com/KaosOverride/CapriceRPI/blob/7d86ebdc6a5e645220c6f30cf407ac57c3256054/src/makefile

### Source CPU (reviewed)

Architecture established by inspected assembly or named emulator CPU implementation: Z80.
- https://github.com/KaosOverride/CapriceRPI/blob/7d86ebdc6a5e645220c6f30cf407ac57c3256054/README%20for%20this%20port.txt
- https://github.com/KaosOverride/CapriceRPI/blob/7d86ebdc6a5e645220c6f30cf407ac57c3256054/src/makefile

### Target CPU (no-evidence-found)

No explicit host/native minimum ISA established in reviewed build material; board names are kept separately from CPU requirements.
- https://github.com/KaosOverride/CapriceRPI/blob/7d86ebdc6a5e645220c6f30cf407ac57c3256054/README%20for%20this%20port.txt
- https://github.com/KaosOverride/CapriceRPI/blob/7d86ebdc6a5e645220c6f30cf407ac57c3256054/src/makefile

### Build (reviewed)

Inspected g++/SDL1 makefile and port release notes; dependencies include SDL_image/SDL_ttf, zlib and older image libraries. No compilation or device run performed; contemporary Pi OS compatibility unverified. Limitations: Read-only source review; no upstream build, game, image or firmware execution. Upstream success statements remain attributed rather than independently verified.
- https://github.com/KaosOverride/CapriceRPI/blob/7d86ebdc6a5e645220c6f30cf407ac57c3256054/README%20for%20this%20port.txt
- https://github.com/KaosOverride/CapriceRPI/blob/7d86ebdc6a5e645220c6f30cf407ac57c3256054/src/makefile

### Runtime profiles (no-evidence-found)

No independent minimum CPU/RAM/chipset compatibility test was performed; hardware and format limitations remain qualified in build notes.
- https://github.com/KaosOverride/CapriceRPI/blob/7d86ebdc6a5e645220c6f30cf407ac57c3256054/README%20for%20this%20port.txt
- https://github.com/KaosOverride/CapriceRPI/blob/7d86ebdc6a5e645220c6f30cf407ac57c3256054/src/makefile

### AI (no-evidence-found)

No actual development-AI contribution or named model established in inspected files. Agent instructions, prose style and missing attribution do not establish use or non-use.
- https://github.com/KaosOverride/CapriceRPI/blob/7d86ebdc6a5e645220c6f30cf407ac57c3256054/README%20for%20this%20port.txt
- https://github.com/KaosOverride/CapriceRPI/blob/7d86ebdc6a5e645220c6f30cf407ac57c3256054/src/makefile

### Relationships (reviewed)

Credits Ulrich Doewich's Caprice32, GP2x port menu lineage, Kevin Thacker/Troels K autotype work. Catalogue this distinct adaptation without treating the shared emulator core as newly authored.
- https://github.com/KaosOverride/CapriceRPI/blob/7d86ebdc6a5e645220c6f30cf407ac57c3256054/README%20for%20this%20port.txt
- https://github.com/KaosOverride/CapriceRPI/blob/7d86ebdc6a5e645220c6f30cf407ac57c3256054/src/makefile

## Who ate Rudy's sandwich? — CPC BASIC game

Project ID: djopensource-who-ate-rudys-sandwich · Overall audit: partial

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
  "display_title": "Who ate Rudy's sandwich? — CPC BASIC game",
  "id": "djopensource-who-ate-rudys-sandwich",
  "last_activity": null,
  "last_checked": "2026-10-26",
  "re_started": null,
  "reconstructed_languages": [
    "BASIC"
  ],
  "record_class": "subject",
  "repo": "https://github.com/djopensource/who-ate-rudys-sandwich",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [
    "BASIC"
  ],
  "source_platforms": [
    "Amstrad CPC"
  ],
  "status": "Source reviewed; upstream build claims qualified in notes",
  "subjects": [
    "Who ate Rudy's sandwich?"
  ],
  "tags": [],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Amstrad CPC"
  ],
  "techniques": [],
  "title": "Who ate Rudy's sandwich? — CPC BASIC game",
  "tool_kinds": [],
  "types": [
    "homebrew"
  ],
  "upstream_name": "who-ate-rudys-sandwich",
  "work_kinds": []
}
```

### Identity (reviewed)

Who ate Rudy's sandwich? — CPC BASIC game. Immutable root listing and linked source/build material personally reviewed.
- https://github.com/djopensource/who-ate-rudys-sandwich/blob/cd4e706cb7bcf031d964dbe1f36800e546e086bd/copyright.txt
- https://github.com/djopensource/who-ate-rudys-sandwich/blob/cd4e706cb7bcf031d964dbe1f36800e546e086bd/rudys.bas

### Classification (reviewed)

Original 2021 CPC game by Angelos Mavros. The substantial readable BASIC listing contains title flow, character drawing, dialogue and game interaction, accompanied by tape/audio distribution files.
- https://github.com/djopensource/who-ate-rudys-sandwich/blob/cd4e706cb7bcf031d964dbe1f36800e546e086bd/copyright.txt
- https://github.com/djopensource/who-ate-rudys-sandwich/blob/cd4e706cb7bcf031d964dbe1f36800e546e086bd/rudys.bas

### Source CPU (no-evidence-found)

Interpreted BASIC source identifies CPC 464 but does not itself declare a machine-code instruction set; no CPU value asserted.
- https://github.com/djopensource/who-ate-rudys-sandwich/blob/cd4e706cb7bcf031d964dbe1f36800e546e086bd/copyright.txt
- https://github.com/djopensource/who-ate-rudys-sandwich/blob/cd4e706cb7bcf031d964dbe1f36800e546e086bd/rudys.bas

### Target CPU (no-evidence-found)

No explicit host/native minimum ISA established in reviewed build material; board names are kept separately from CPU requirements.
- https://github.com/djopensource/who-ate-rudys-sandwich/blob/cd4e706cb7bcf031d964dbe1f36800e546e086bd/copyright.txt
- https://github.com/djopensource/who-ate-rudys-sandwich/blob/cd4e706cb7bcf031d964dbe1f36800e546e086bd/rudys.bas

### Build (reviewed)

Listing identifies CPC 464 and version 1.0 Beta; no build procedure or independent loading/play test was verified. Tape and WAV presence alone is not a proven runnable build. Limitations: Read-only source review; no upstream build, game, image or firmware execution. Upstream success statements remain attributed rather than independently verified.
- https://github.com/djopensource/who-ate-rudys-sandwich/blob/cd4e706cb7bcf031d964dbe1f36800e546e086bd/copyright.txt
- https://github.com/djopensource/who-ate-rudys-sandwich/blob/cd4e706cb7bcf031d964dbe1f36800e546e086bd/rudys.bas

### Runtime profiles (no-evidence-found)

No independent minimum CPU/RAM/chipset compatibility test was performed; hardware and format limitations remain qualified in build notes.
- https://github.com/djopensource/who-ate-rudys-sandwich/blob/cd4e706cb7bcf031d964dbe1f36800e546e086bd/copyright.txt
- https://github.com/djopensource/who-ate-rudys-sandwich/blob/cd4e706cb7bcf031d964dbe1f36800e546e086bd/rudys.bas

### AI (no-evidence-found)

No actual development-AI contribution or named model established in inspected files. Agent instructions, prose style and missing attribution do not establish use or non-use.
- https://github.com/djopensource/who-ate-rudys-sandwich/blob/cd4e706cb7bcf031d964dbe1f36800e546e086bd/copyright.txt
- https://github.com/djopensource/who-ate-rudys-sandwich/blob/cd4e706cb7bcf031d964dbe1f36800e546e086bd/rudys.bas

### Relationships (reviewed)

Author/copyright identity is stated in the source and copyright.txt. No predecessor or reconstruction relationship is established; classify as original homebrew, not reverse engineering.
- https://github.com/djopensource/who-ate-rudys-sandwich/blob/cd4e706cb7bcf031d964dbe1f36800e546e086bd/copyright.txt
- https://github.com/djopensource/who-ate-rudys-sandwich/blob/cd4e706cb7bcf031d964dbe1f36800e546e086bd/rudys.bas

## SC-3000 emulator for Raspberry Pi Pico

Project ID: shippoiincho-sc3000emulator · Overall audit: partial

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
  "display_title": "SC-3000 emulator for Raspberry Pi Pico",
  "id": "shippoiincho-sc3000emulator",
  "last_activity": null,
  "last_checked": "2026-10-26",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "C++"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/shippoiincho/sc3000emulator",
  "runtime_profiles": [],
  "source_cpu": [
    "Z80"
  ],
  "source_language": [
    "C",
    "C++"
  ],
  "source_platforms": [
    "SC-3000"
  ],
  "status": "Source reviewed; upstream build claims qualified in notes",
  "subjects": [
    "SC-3000 emulator for Raspberry Pi Pico"
  ],
  "tags": [],
  "target_cpu": [],
  "target_kinds": [],
  "target_platforms": [
    "Raspberry Pi Pico"
  ],
  "techniques": [],
  "title": "SC-3000 emulator for Raspberry Pi Pico",
  "tool_kinds": [
    "emulator"
  ],
  "types": [
    "tooling"
  ],
  "upstream_name": "sc3000emulator",
  "work_kinds": []
}
```

### Identity (reviewed)

SC-3000 emulator for Raspberry Pi Pico. Immutable root listing and linked source/build material personally reviewed.
- https://github.com/shippoiincho/sc3000emulator/blob/54e614763d61d6e2acfb9d2db5b6143565dc640f/README.md
- https://github.com/shippoiincho/sc3000emulator/blob/54e614763d61d6e2acfb9d2db5b6143565dc640f/sc3000emulator/CMakeLists.txt

### Classification (reviewed)

Pico-hosted SC-3000 emulator implements RAM, TMS9918 video, PSG, cartridge/tape handling and keyboard/gamepad input. CMake lists actual machine, Z80, VGA, filesystem and USB implementation units.
- https://github.com/shippoiincho/sc3000emulator/blob/54e614763d61d6e2acfb9d2db5b6143565dc640f/README.md
- https://github.com/shippoiincho/sc3000emulator/blob/54e614763d61d6e2acfb9d2db5b6143565dc640f/sc3000emulator/CMakeLists.txt

### Source CPU (reviewed)

Architecture established by inspected assembly or named emulator CPU implementation: Z80.
- https://github.com/shippoiincho/sc3000emulator/blob/54e614763d61d6e2acfb9d2db5b6143565dc640f/README.md
- https://github.com/shippoiincho/sc3000emulator/blob/54e614763d61d6e2acfb9d2db5b6143565dc640f/sc3000emulator/CMakeLists.txt

### Target CPU (no-evidence-found)

No explicit host/native minimum ISA established in reviewed build material; board names are kept separately from CPU requirements.
- https://github.com/shippoiincho/sc3000emulator/blob/54e614763d61d6e2acfb9d2db5b6143565dc640f/README.md
- https://github.com/shippoiincho/sc3000emulator/blob/54e614763d61d6e2acfb9d2db5b6143565dc640f/sc3000emulator/CMakeLists.txt

### Build (reviewed)

Pico SDK/CMake build and UF2 distribution are present. README documents 32KiB cartridge limit, excludes 40KiB/mega ROMs and describes LittleFS tape loading. No firmware was built or flashed during review. Limitations: Read-only source review; no upstream build, game, image or firmware execution. Upstream success statements remain attributed rather than independently verified.
- https://github.com/shippoiincho/sc3000emulator/blob/54e614763d61d6e2acfb9d2db5b6143565dc640f/README.md
- https://github.com/shippoiincho/sc3000emulator/blob/54e614763d61d6e2acfb9d2db5b6143565dc640f/sc3000emulator/CMakeLists.txt

### Runtime profiles (no-evidence-found)

No independent minimum CPU/RAM/chipset compatibility test was performed; hardware and format limitations remain qualified in build notes.
- https://github.com/shippoiincho/sc3000emulator/blob/54e614763d61d6e2acfb9d2db5b6143565dc640f/README.md
- https://github.com/shippoiincho/sc3000emulator/blob/54e614763d61d6e2acfb9d2db5b6143565dc640f/sc3000emulator/CMakeLists.txt

### AI (no-evidence-found)

No actual development-AI contribution or named model established in inspected files. Agent instructions, prose style and missing attribution do not establish use or non-use.
- https://github.com/shippoiincho/sc3000emulator/blob/54e614763d61d6e2acfb9d2db5b6143565dc640f/README.md
- https://github.com/shippoiincho/sc3000emulator/blob/54e614763d61d6e2acfb9d2db5b6143565dc640f/sc3000emulator/CMakeLists.txt

### Relationships (reviewed)

Explicitly credits redcode Z80/Zeta, Hunter-Adams VGA, littlefs, vrEmuTms9918, C-BIOS fonts and HID parser lineage; this is an integrated machine emulator, not a new CPU-core claim.
- https://github.com/shippoiincho/sc3000emulator/blob/54e614763d61d6e2acfb9d2db5b6143565dc640f/README.md
- https://github.com/shippoiincho/sc3000emulator/blob/54e614763d61d6e2acfb9d2db5b6143565dc640f/sc3000emulator/CMakeLists.txt

## SC-3000 / SG-1000 keyboard and joystick routines

Project ID: siriokds-sc-3000-keyboard-support · Overall audit: partial

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
  "display_title": "SC-3000 / SG-1000 keyboard and joystick routines",
  "id": "siriokds-sc-3000-keyboard-support",
  "last_activity": null,
  "last_checked": "2026-10-26",
  "re_started": null,
  "reconstructed_languages": [
    "Z80 assembly"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/siriokds/SC-3000-Keyboard-support",
  "runtime_profiles": [],
  "source_cpu": [
    "Z80"
  ],
  "source_language": [
    "Z80 assembly"
  ],
  "source_platforms": [
    "SC-3000",
    "SG-1000"
  ],
  "status": "Source reviewed; upstream build claims qualified in notes",
  "subjects": [
    "SC-3000 / SG-1000 keyboard and joystick routines"
  ],
  "tags": [],
  "target_cpu": [
    "Z80"
  ],
  "target_kinds": [],
  "target_platforms": [
    "SC-3000",
    "SG-1000"
  ],
  "techniques": [],
  "title": "SC-3000 / SG-1000 keyboard and joystick routines",
  "tool_kinds": [
    "development-environment"
  ],
  "types": [
    "tooling"
  ],
  "upstream_name": "SC-3000-Keyboard-support",
  "work_kinds": []
}
```

### Identity (reviewed)

SC-3000 / SG-1000 keyboard and joystick routines. Immutable root listing and linked source/build material personally reviewed.
- https://github.com/siriokds/SC-3000-Keyboard-support/blob/4e4c8c736b22fe5f1d767f5cb978b2534cabaf39/SC3000_SG1000_KeybJoy.asm
- https://github.com/siriokds/SC-3000-Keyboard-support/blob/4e4c8c736b22fe5f1d767f5cb978b2534cabaf39/SG-1000_SC-3000_essentials.asm

### Classification (reviewed)

Reusable Z80 routines detect keyboard/PPI availability and merge cursor/key rows with joystick inputs; companion startup, interrupt and VDP/PSG templates support native game development.
- https://github.com/siriokds/SC-3000-Keyboard-support/blob/4e4c8c736b22fe5f1d767f5cb978b2534cabaf39/SC3000_SG1000_KeybJoy.asm
- https://github.com/siriokds/SC-3000-Keyboard-support/blob/4e4c8c736b22fe5f1d767f5cb978b2534cabaf39/SG-1000_SC-3000_essentials.asm

### Source CPU (reviewed)

Architecture established by inspected assembly or named emulator CPU implementation: Z80.
- https://github.com/siriokds/SC-3000-Keyboard-support/blob/4e4c8c736b22fe5f1d767f5cb978b2534cabaf39/SC3000_SG1000_KeybJoy.asm
- https://github.com/siriokds/SC-3000-Keyboard-support/blob/4e4c8c736b22fe5f1d767f5cb978b2534cabaf39/SG-1000_SC-3000_essentials.asm

### Target CPU (reviewed)

Native assembly output uses Z80.
- https://github.com/siriokds/SC-3000-Keyboard-support/blob/4e4c8c736b22fe5f1d767f5cb978b2534cabaf39/SC3000_SG1000_KeybJoy.asm
- https://github.com/siriokds/SC-3000-Keyboard-support/blob/4e4c8c736b22fe5f1d767f5cb978b2534cabaf39/SG-1000_SC-3000_essentials.asm

### Build (reviewed)

Actual assembly instructions and port definitions inspected. Essentials contains literal unfinished placeholders and unresolved symbolic references; treat it as integration snippets, not a standalone compilable program. No assembler or hardware test performed. Limitations: Read-only source review; no upstream build, game, image or firmware execution. Upstream success statements remain attributed rather than independently verified.
- https://github.com/siriokds/SC-3000-Keyboard-support/blob/4e4c8c736b22fe5f1d767f5cb978b2534cabaf39/SC3000_SG1000_KeybJoy.asm
- https://github.com/siriokds/SC-3000-Keyboard-support/blob/4e4c8c736b22fe5f1d767f5cb978b2534cabaf39/SG-1000_SC-3000_essentials.asm

### Runtime profiles (no-evidence-found)

No independent minimum CPU/RAM/chipset compatibility test was performed; hardware and format limitations remain qualified in build notes.
- https://github.com/siriokds/SC-3000-Keyboard-support/blob/4e4c8c736b22fe5f1d767f5cb978b2534cabaf39/SC3000_SG1000_KeybJoy.asm
- https://github.com/siriokds/SC-3000-Keyboard-support/blob/4e4c8c736b22fe5f1d767f5cb978b2534cabaf39/SG-1000_SC-3000_essentials.asm

### AI (no-evidence-found)

No actual development-AI contribution or named model established in inspected files. Agent instructions, prose style and missing attribution do not establish use or non-use.
- https://github.com/siriokds/SC-3000-Keyboard-support/blob/4e4c8c736b22fe5f1d767f5cb978b2534cabaf39/SC3000_SG1000_KeybJoy.asm
- https://github.com/siriokds/SC-3000-Keyboard-support/blob/4e4c8c736b22fe5f1d767f5cb978b2534cabaf39/SG-1000_SC-3000_essentials.asm

### Relationships (reviewed)

Repository also contains a CVBasic prologue. No claim that this repo originates the broader compiler runtime; inclusion is for its demonstrated SC-3000 input integration routines.
- https://github.com/siriokds/SC-3000-Keyboard-support/blob/4e4c8c736b22fe5f1d767f5cb978b2534cabaf39/SC3000_SG1000_KeybJoy.asm
- https://github.com/siriokds/SC-3000-Keyboard-support/blob/4e4c8c736b22fe5f1d767f5cb978b2534cabaf39/SG-1000_SC-3000_essentials.asm

## Pinned evidence manifest

- chaossource-menace-reverse-engineering-completed-md: https://github.com/chaossource/menace-reverse-engineering/blob/182f2440e01e5734c6d8adef6dde1d48d31826fb/COMPLETED.md (Git blob be9050d0997cca06713a2a5cb56538439e845767)
- chaossource-menace-reverse-engineering-menace-re-readme-md: https://github.com/chaossource/menace-reverse-engineering/blob/182f2440e01e5734c6d8adef6dde1d48d31826fb/menace-re/README.md (Git blob 3638450f6a15cac81986936c2ea14a6c6eccd47e)
- chaossource-menace-reverse-engineering-menace-re-src-game-cpp: https://github.com/chaossource/menace-reverse-engineering/blob/182f2440e01e5734c6d8adef6dde1d48d31826fb/menace-re/src/game.cpp (Git blob 68fd558792a4278b551c79212d936c559b1785bb)
- chaossource-menace-reverse-engineering-menace-re-tools-disassemble-game-py: https://github.com/chaossource/menace-reverse-engineering/blob/182f2440e01e5734c6d8adef6dde1d48d31826fb/menace-re/tools/disassemble_game.py (Git blob 6c40c830c55ba867546f030b54a00af9afb71368)
- djopensource-who-ate-rudys-sandwich-copyright-txt: https://github.com/djopensource/who-ate-rudys-sandwich/blob/cd4e706cb7bcf031d964dbe1f36800e546e086bd/copyright.txt (Git blob 57361395c672c2393ae9bd3817b19f2738b77759)
- djopensource-who-ate-rudys-sandwich-rudys-bas: https://github.com/djopensource/who-ate-rudys-sandwich/blob/cd4e706cb7bcf031d964dbe1f36800e546e086bd/rudys.bas (Git blob 6ba301dfe311cc81721fa07476b6109312aaedb3)
- f1ac0-dual-usb-controller-adapter-cpc-readme-md: https://github.com/f1ac0/dual-usb-controller-adapter-cpc/blob/659a37f512044e07411de67dbf293068632a03ff/README.md (Git blob a73121257b67f2db6243f14acd1e8d2c83ad27db)
- hunkstalker-kult-atari-st-c-agents-md: https://github.com/hunkstalker/kult-atari-st-c/blob/beebb5219f67ae2879a7cddf0b6a85e35aaca164/AGENTS.md (Git blob 2dc2a443129dcf75d9829e2673bfc8ef98b5aaf4)
- hunkstalker-kult-atari-st-c-include-kult-api-h: https://github.com/hunkstalker/kult-atari-st-c/blob/beebb5219f67ae2879a7cddf0b6a85e35aaca164/include/kult_api.h (Git blob 94c60fe335f2b6290892be720390f9529c40e2d1)
- hunkstalker-kult-atari-st-c-include-kult-port-h: https://github.com/hunkstalker/kult-atari-st-c/blob/beebb5219f67ae2879a7cddf0b6a85e35aaca164/include/kult_port.h (Git blob 86a8a7c5aa016bc05157110d358f38aa95ab7d5e)
- hunkstalker-kult-atari-st-c-makefile: https://github.com/hunkstalker/kult-atari-st-c/blob/beebb5219f67ae2879a7cddf0b6a85e35aaca164/Makefile (Git blob bc34661552689bd51959085ccc1a358088fda2a2)
- hunkstalker-kult-atari-st-c-readme-md: https://github.com/hunkstalker/kult-atari-st-c/blob/beebb5219f67ae2879a7cddf0b6a85e35aaca164/README.md (Git blob a935c961166066d0023e07b11809fd87a1e8dd54)
- hunkstalker-kult-atari-st-c-src-input-c: https://github.com/hunkstalker/kult-atari-st-c/blob/beebb5219f67ae2879a7cddf0b6a85e35aaca164/src/input.c (Git blob a80e0f9508ddd057279b54eb8dc9199a25f1af69)
- hunkstalker-kult-atari-st-c-tools-recreate-kit-include-machine-h: https://github.com/hunkstalker/kult-atari-st-c/blob/beebb5219f67ae2879a7cddf0b6a85e35aaca164/tools/recreate_kit/include/machine.h (Git blob 71e2892855b7a610b3d4849878d8e196e604ef7f)
- hunkstalker-kult-atari-st-decomp-matching-makefile: https://github.com/hunkstalker/kult-atari-st-decomp/blob/5ef7c171dc71760bc9bb1e6abe4b0405319e4f5f/matching/Makefile (Git blob 515df454a734528a26766510d14984f1bbb63410)
- hunkstalker-kult-atari-st-decomp-matching-src-auto-011e5e-s: https://github.com/hunkstalker/kult-atari-st-decomp/blob/5ef7c171dc71760bc9bb1e6abe4b0405319e4f5f/matching/src/auto_011e5e.s (Git blob c205c17e2e02cf17d93bb041af8c974b8ff0ae40)
- hunkstalker-kult-atari-st-decomp-readme-md: https://github.com/hunkstalker/kult-atari-st-decomp/blob/5ef7c171dc71760bc9bb1e6abe4b0405319e4f5f/README.md (Git blob d048aebb53539d7c90e9f8ba65a9d6b111b0774d)
- kaosoverride-capricerpi-readme-for-this-port-txt: https://github.com/kaosoverride/capricerpi/blob/7d86ebdc6a5e645220c6f30cf407ac57c3256054/README%20for%20this%20port.txt (Git blob 2d5d10c1369edffe730164782b7667c148cc32cd)
- kaosoverride-capricerpi-src-makefile: https://github.com/kaosoverride/capricerpi/blob/7d86ebdc6a5e645220c6f30cf407ac57c3256054/src/makefile (Git blob 18c7632795a7cb73a0f9be570f287cdbf40faec8)
- markyturtle-newzealandstory-amiga-building-md: https://github.com/markyturtle/newzealandstory--amiga/blob/085eb38546bdae4de6c021ae52d7e62f7cd287f4/BUILDING.md (Git blob 6a3b5db2788cadb1b45264df6d78fca4858627d2)
- markyturtle-newzealandstory-amiga-enhanced-src-diskload-s: https://github.com/markyturtle/newzealandstory--amiga/blob/085eb38546bdae4de6c021ae52d7e62f7cd287f4/enhanced/src/diskload.s (Git blob e811b60593330d79530e78a3608b699a88d4ded5)
- markyturtle-newzealandstory-amiga-original-build-sh: https://github.com/markyturtle/newzealandstory--amiga/blob/085eb38546bdae4de6c021ae52d7e62f7cd287f4/original/build.sh (Git blob d4428d83825035bff89faa25b2222f90532942a0)
- markyturtle-newzealandstory-amiga-readme-md: https://github.com/markyturtle/newzealandstory--amiga/blob/085eb38546bdae4de6c021ae52d7e62f7cd287f4/README.md (Git blob 097384f8d700c92efc6f7e96a350a49355b88052)
- shippoiincho-sc3000emulator-readme-md: https://github.com/shippoiincho/sc3000emulator/blob/54e614763d61d6e2acfb9d2db5b6143565dc640f/README.md (Git blob 37f683cdaf59132f20ac95aedc5ce7a86f5c2077)
- shippoiincho-sc3000emulator-sc3000emulator-cmakelists-txt: https://github.com/shippoiincho/sc3000emulator/blob/54e614763d61d6e2acfb9d2db5b6143565dc640f/sc3000emulator/CMakeLists.txt (Git blob 189320911f7fa98adf7cdadfdd2e8d4fe8d32a50)
- siriokds-sc-3000-keyboard-support-sc3000-sg1000-keybjoy-asm: https://github.com/siriokds/sc-3000-keyboard-support/blob/4e4c8c736b22fe5f1d767f5cb978b2534cabaf39/SC3000_SG1000_KeybJoy.asm (Git blob 3a202e3f941940da5312d7672d3c3f4169788b75)
- siriokds-sc-3000-keyboard-support-sg-1000-sc-3000-essentials-asm: https://github.com/siriokds/sc-3000-keyboard-support/blob/4e4c8c736b22fe5f1d767f5cb978b2534cabaf39/SG-1000_SC-3000_essentials.asm (Git blob a796c0090a7964f530da99b34faccbc1a2554fc7)

## Sources

```json
[
  {
    "first_indexed": "2026-10-26",
    "id": "github-markyturtle-newzealandstory-amiga",
    "kind": "github-repository",
    "last_reviewed": "2026-10-26",
    "open_task_ids": [],
    "projects_promoted": [
      "markyturtle-newzealandstory-amiga"
    ],
    "reason": "Original main, loader and two boot sources have byte-comparison build gates; a separate enhanced path replaces disk routines and boot chain to build an AmigaDOS-format disk. Extracted graphics/music and tools are included. Keep original-byte matching distinct from the deliberately modified enhanced build.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/MarkyTurtle/NewzealandStory--Amiga"
  },
  {
    "first_indexed": "2026-10-26",
    "id": "github-hunkstalker-kult-atari-st-decomp",
    "kind": "github-repository",
    "last_reviewed": "2026-10-26",
    "open_task_ids": [],
    "projects_promoted": [
      "hunkstalker-kult-atari-st-decomp"
    ],
    "reason": "Assembly reconstruction of the original Atari ST engine with transcribed tables, Alcyon C startup/music and relocation reconstruction. Concrete assembly and build scripts are present; not merely a decompilation goal.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/hunkstalker/kult-atari-st-decomp"
  },
  {
    "first_indexed": "2026-10-26",
    "id": "github-kaosoverride-capricerpi",
    "kind": "github-repository",
    "last_reviewed": "2026-10-26",
    "open_task_ids": [],
    "projects_promoted": [
      "kaosoverride-capricerpi"
    ],
    "reason": "Substantive Caprice32 4.1.0 adaptation with joystick-driven virtual keyboard, four-controller/ToTo support, autorun, snapshots and Pi-specific display handling. Includes emulator core and source build files rather than only a packaged binary.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/KaosOverride/CapriceRPI"
  },
  {
    "first_indexed": "2026-10-26",
    "id": "github-djopensource-who-ate-rudys-sandwich",
    "kind": "github-repository",
    "last_reviewed": "2026-10-26",
    "open_task_ids": [],
    "projects_promoted": [
      "djopensource-who-ate-rudys-sandwich"
    ],
    "reason": "Original 2021 CPC game by Angelos Mavros. The substantial readable BASIC listing contains title flow, character drawing, dialogue and game interaction, accompanied by tape/audio distribution files.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/djopensource/who-ate-rudys-sandwich"
  },
  {
    "first_indexed": "2026-10-26",
    "id": "github-shippoiincho-sc3000emulator",
    "kind": "github-repository",
    "last_reviewed": "2026-10-26",
    "open_task_ids": [],
    "projects_promoted": [
      "shippoiincho-sc3000emulator"
    ],
    "reason": "Pico-hosted SC-3000 emulator implements RAM, TMS9918 video, PSG, cartridge/tape handling and keyboard/gamepad input. CMake lists actual machine, Z80, VGA, filesystem and USB implementation units.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/shippoiincho/sc3000emulator"
  },
  {
    "first_indexed": "2026-10-26",
    "id": "github-siriokds-sc-3000-keyboard-support",
    "kind": "github-repository",
    "last_reviewed": "2026-10-26",
    "open_task_ids": [],
    "projects_promoted": [
      "siriokds-sc-3000-keyboard-support"
    ],
    "reason": "Reusable Z80 routines detect keyboard/PPI availability and merge cursor/key rows with joystick inputs; companion startup, interrupt and VDP/PSG templates support native game development.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/siriokds/SC-3000-Keyboard-support"
  },
  {
    "first_indexed": "2026-10-26",
    "id": "github-chaossource-menace-reverse-engineering",
    "kind": "github-repository",
    "last_reviewed": "2026-10-26",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Defer claimed complete Menace port: README and COMPLETED claims conflict with unfinished original logic; actual game.cpp uses generic timed random enemies and placeholder rendering, while disassembly helper slices guessed disk offsets. Concrete tools exist, but faithful reconstruction and reliable extraction claims are not established. Do not promote completion rhetoric as game restoration.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/chaossource/menace-reverse-engineering"
  },
  {
    "first_indexed": "2026-10-26",
    "id": "github-hunkstalker-kult-atari-st-c",
    "kind": "github-repository",
    "last_reviewed": "2026-10-26",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Defer execution-architecture review, not the separate matching ASM project. C core explicitly is not playable and retains a flat 68000 address-space image, machine-width arithmetic and boundary register parameters. Musashi is the reference oracle, which alone is not baked-emulation evidence; determine the deployed core runtime boundary before a native-port or baked-emulation classification.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/hunkstalker/kult-atari-st-c"
  },
  {
    "first_indexed": "2026-10-26",
    "id": "github-f1ac0-dual-usb-controller-adapter-cpc",
    "kind": "github-repository",
    "last_reviewed": "2026-10-26",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Defer software inclusion: this root provides PCB/enclosure design, documentation and compiled STM32 update/bootloader binaries, but no corresponding firmware source tree. Do not describe hardware manufacturing files plus binaries as a source-backed software implementation.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/f1ac0/Dual-USB-Controller-adapter-CPC"
  }
]
```

## Decisions

```json
[
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/MarkyTurtle/NewzealandStory--Amiga/blob/085eb38546bdae4de6c021ae52d7e62f7cd287f4/README.md",
      "https://github.com/MarkyTurtle/NewzealandStory--Amiga/blob/085eb38546bdae4de6c021ae52d7e62f7cd287f4/BUILDING.md",
      "https://github.com/MarkyTurtle/NewzealandStory--Amiga/blob/085eb38546bdae4de6c021ae52d7e62f7cd287f4/original/build.sh",
      "https://github.com/MarkyTurtle/NewzealandStory--Amiga/blob/085eb38546bdae4de6c021ae52d7e62f7cd287f4/enhanced/src/diskload.s"
    ],
    "id": "2026-10-26-amiga-kult-cpc-sc3000-discovery-markyturtle-newzealandstory-amiga",
    "project_ids": [
      "markyturtle-newzealandstory-amiga"
    ],
    "reason": "Original main, loader and two boot sources have byte-comparison build gates; a separate enhanced path replaces disk routines and boot chain to build an AmigaDOS-format disk. Extracted graphics/music and tools are included. Keep original-byte matching distinct from the deliberately modified enhanced build.",
    "reviewed_at": "2026-10-26",
    "source_ids": [
      "github-markyturtle-newzealandstory-amiga"
    ],
    "title": "The New Zealand Story — Amiga disassembly and disk rebuild",
    "url": "https://github.com/MarkyTurtle/NewzealandStory--Amiga"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/hunkstalker/kult-atari-st-decomp/blob/5ef7c171dc71760bc9bb1e6abe4b0405319e4f5f/README.md",
      "https://github.com/hunkstalker/kult-atari-st-decomp/blob/5ef7c171dc71760bc9bb1e6abe4b0405319e4f5f/matching/Makefile",
      "https://github.com/hunkstalker/kult-atari-st-decomp/blob/5ef7c171dc71760bc9bb1e6abe4b0405319e4f5f/matching/src/auto_011e5e.s"
    ],
    "id": "2026-10-26-amiga-kult-cpc-sc3000-discovery-hunkstalker-kult-atari-st-decomp",
    "project_ids": [
      "hunkstalker-kult-atari-st-decomp"
    ],
    "reason": "Assembly reconstruction of the original Atari ST engine with transcribed tables, Alcyon C startup/music and relocation reconstruction. Concrete assembly and build scripts are present; not merely a decompilation goal.",
    "reviewed_at": "2026-10-26",
    "source_ids": [
      "github-hunkstalker-kult-atari-st-decomp"
    ],
    "title": "Kult: The Temple of Flying Saucers — Atari ST matching reconstruction",
    "url": "https://github.com/hunkstalker/kult-atari-st-decomp"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/KaosOverride/CapriceRPI/blob/7d86ebdc6a5e645220c6f30cf407ac57c3256054/README%20for%20this%20port.txt",
      "https://github.com/KaosOverride/CapriceRPI/blob/7d86ebdc6a5e645220c6f30cf407ac57c3256054/src/makefile"
    ],
    "id": "2026-10-26-amiga-kult-cpc-sc3000-discovery-kaosoverride-capricerpi",
    "project_ids": [
      "kaosoverride-capricerpi"
    ],
    "reason": "Substantive Caprice32 4.1.0 adaptation with joystick-driven virtual keyboard, four-controller/ToTo support, autorun, snapshots and Pi-specific display handling. Includes emulator core and source build files rather than only a packaged binary.",
    "reviewed_at": "2026-10-26",
    "source_ids": [
      "github-kaosoverride-capricerpi"
    ],
    "title": "CapriceRPI — Raspberry Pi CPC emulator port",
    "url": "https://github.com/KaosOverride/CapriceRPI"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/djopensource/who-ate-rudys-sandwich/blob/cd4e706cb7bcf031d964dbe1f36800e546e086bd/copyright.txt",
      "https://github.com/djopensource/who-ate-rudys-sandwich/blob/cd4e706cb7bcf031d964dbe1f36800e546e086bd/rudys.bas"
    ],
    "id": "2026-10-26-amiga-kult-cpc-sc3000-discovery-djopensource-who-ate-rudys-sandwich",
    "project_ids": [
      "djopensource-who-ate-rudys-sandwich"
    ],
    "reason": "Original 2021 CPC game by Angelos Mavros. The substantial readable BASIC listing contains title flow, character drawing, dialogue and game interaction, accompanied by tape/audio distribution files.",
    "reviewed_at": "2026-10-26",
    "source_ids": [
      "github-djopensource-who-ate-rudys-sandwich"
    ],
    "title": "Who ate Rudy's sandwich? — CPC BASIC game",
    "url": "https://github.com/djopensource/who-ate-rudys-sandwich"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/shippoiincho/sc3000emulator/blob/54e614763d61d6e2acfb9d2db5b6143565dc640f/README.md",
      "https://github.com/shippoiincho/sc3000emulator/blob/54e614763d61d6e2acfb9d2db5b6143565dc640f/sc3000emulator/CMakeLists.txt"
    ],
    "id": "2026-10-26-amiga-kult-cpc-sc3000-discovery-shippoiincho-sc3000emulator",
    "project_ids": [
      "shippoiincho-sc3000emulator"
    ],
    "reason": "Pico-hosted SC-3000 emulator implements RAM, TMS9918 video, PSG, cartridge/tape handling and keyboard/gamepad input. CMake lists actual machine, Z80, VGA, filesystem and USB implementation units.",
    "reviewed_at": "2026-10-26",
    "source_ids": [
      "github-shippoiincho-sc3000emulator"
    ],
    "title": "SC-3000 emulator for Raspberry Pi Pico",
    "url": "https://github.com/shippoiincho/sc3000emulator"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/siriokds/SC-3000-Keyboard-support/blob/4e4c8c736b22fe5f1d767f5cb978b2534cabaf39/SC3000_SG1000_KeybJoy.asm",
      "https://github.com/siriokds/SC-3000-Keyboard-support/blob/4e4c8c736b22fe5f1d767f5cb978b2534cabaf39/SG-1000_SC-3000_essentials.asm"
    ],
    "id": "2026-10-26-amiga-kult-cpc-sc3000-discovery-siriokds-sc-3000-keyboard-support",
    "project_ids": [
      "siriokds-sc-3000-keyboard-support"
    ],
    "reason": "Reusable Z80 routines detect keyboard/PPI availability and merge cursor/key rows with joystick inputs; companion startup, interrupt and VDP/PSG templates support native game development.",
    "reviewed_at": "2026-10-26",
    "source_ids": [
      "github-siriokds-sc-3000-keyboard-support"
    ],
    "title": "SC-3000 / SG-1000 keyboard and joystick routines",
    "url": "https://github.com/siriokds/SC-3000-Keyboard-support"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/chaossource/menace-reverse-engineering/blob/182f2440e01e5734c6d8adef6dde1d48d31826fb/menace-re/README.md",
      "https://github.com/chaossource/menace-reverse-engineering/blob/182f2440e01e5734c6d8adef6dde1d48d31826fb/COMPLETED.md",
      "https://github.com/chaossource/menace-reverse-engineering/blob/182f2440e01e5734c6d8adef6dde1d48d31826fb/menace-re/src/game.cpp",
      "https://github.com/chaossource/menace-reverse-engineering/blob/182f2440e01e5734c6d8adef6dde1d48d31826fb/menace-re/tools/disassemble_game.py"
    ],
    "id": "2026-10-26-amiga-kult-cpc-sc3000-discovery-chaossource-menace-reverse-engineering",
    "project_ids": [],
    "reason": "Defer claimed complete Menace port: README and COMPLETED claims conflict with unfinished original logic; actual game.cpp uses generic timed random enemies and placeholder rendering, while disassembly helper slices guessed disk offsets. Concrete tools exist, but faithful reconstruction and reliable extraction claims are not established. Do not promote completion rhetoric as game restoration.",
    "reviewed_at": "2026-10-26",
    "source_ids": [
      "github-chaossource-menace-reverse-engineering"
    ],
    "title": "chaossource/menace-reverse-engineering",
    "url": "https://github.com/chaossource/menace-reverse-engineering"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/hunkstalker/kult-atari-st-c/blob/beebb5219f67ae2879a7cddf0b6a85e35aaca164/README.md",
      "https://github.com/hunkstalker/kult-atari-st-c/blob/beebb5219f67ae2879a7cddf0b6a85e35aaca164/AGENTS.md",
      "https://github.com/hunkstalker/kult-atari-st-c/blob/beebb5219f67ae2879a7cddf0b6a85e35aaca164/src/input.c",
      "https://github.com/hunkstalker/kult-atari-st-c/blob/beebb5219f67ae2879a7cddf0b6a85e35aaca164/Makefile",
      "https://github.com/hunkstalker/kult-atari-st-c/blob/beebb5219f67ae2879a7cddf0b6a85e35aaca164/include/kult_port.h",
      "https://github.com/hunkstalker/kult-atari-st-c/blob/beebb5219f67ae2879a7cddf0b6a85e35aaca164/include/kult_api.h",
      "https://github.com/hunkstalker/kult-atari-st-c/blob/beebb5219f67ae2879a7cddf0b6a85e35aaca164/tools/recreate_kit/include/machine.h"
    ],
    "id": "2026-10-26-amiga-kult-cpc-sc3000-discovery-hunkstalker-kult-atari-st-c",
    "project_ids": [],
    "reason": "Defer execution-architecture review, not the separate matching ASM project. C core explicitly is not playable and retains a flat 68000 address-space image, machine-width arithmetic and boundary register parameters. Musashi is the reference oracle, which alone is not baked-emulation evidence; determine the deployed core runtime boundary before a native-port or baked-emulation classification.",
    "reviewed_at": "2026-10-26",
    "source_ids": [
      "github-hunkstalker-kult-atari-st-c"
    ],
    "title": "hunkstalker/kult-atari-st-c",
    "url": "https://github.com/hunkstalker/kult-atari-st-c"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/f1ac0/Dual-USB-Controller-adapter-CPC/blob/659a37f512044e07411de67dbf293068632a03ff/README.md"
    ],
    "id": "2026-10-26-amiga-kult-cpc-sc3000-discovery-f1ac0-dual-usb-controller-adapter-cpc",
    "project_ids": [],
    "reason": "Defer software inclusion: this root provides PCB/enclosure design, documentation and compiled STM32 update/bootloader binaries, but no corresponding firmware source tree. Do not describe hardware manufacturing files plus binaries as a source-backed software implementation.",
    "reviewed_at": "2026-10-26",
    "source_ids": [
      "github-f1ac0-dual-usb-controller-adapter-cpc"
    ],
    "title": "f1ac0/Dual-USB-Controller-adapter-CPC",
    "url": "https://github.com/f1ac0/Dual-USB-Controller-adapter-CPC"
  }
]
```

## Research event notes

Root performed all research and publication directly; no discovery worker. Four fresh repository searches were screened locally against current main before primary-source review. Unrelated SC3000 substring matches were discarded during triage, not described as investigated projects. Nine selected roots were inspected with immutable trees and blob-verified inline source proofs. This is a bounded pass, not exhaustive platform coverage. Distinguish matching originals from patched outputs, source cores from runnable ports, hardware/binary releases from source-backed software, and claimed completion from actual code. No upstream code was executed and no private inputs were downloaded.
