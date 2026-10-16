# Add seven game projects across Amiga, Atari ST and C64; defer hardware-emulation port and scaffold-only candidate.

Add seven game projects across Amiga, Atari ST and C64; defer hardware-emulation port and scaffold-only candidate.

Date: 2026-10-17 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- amiwind-morrowind-amiga / Runtime profiles (no-evidence-found): Target and timing/reference configuration are recorded in the target-CPU note. No independently verified minimum runnable profile is asserted.
- amiwind-morrowind-amiga / AI (no-evidence-found): No explicit development-AI attribution found in the inspected README and selected source/build documents; absence is not evidence of non-use.
- stunt-car-racer-performance-patch / Runtime profiles (no-evidence-found): Target and timing/reference configuration are recorded in the target-CPU note. No independently verified minimum runnable profile is asserted.
- stunt-car-racer-performance-patch / AI (no-evidence-found): No explicit development-AI attribution found in the inspected README and selected source/build documents; absence is not evidence of non-use.
- core-atari-st-flindholm / Runtime profiles (no-evidence-found): Target and timing/reference configuration are recorded in the target-CPU note. No independently verified minimum runnable profile is asserted.
- core-atari-st-flindholm / AI (no-evidence-found): No explicit development-AI attribution found in the inspected README and selected source/build documents; absence is not evidence of non-use.
- super-sprint-reforged-st / Runtime profiles (no-evidence-found): Target and timing/reference configuration are recorded in the target-CPU note. No independently verified minimum runnable profile is asserted.
- super-sprint-reforged-st / AI (no-evidence-found): No explicit development-AI attribution found in the inspected README and selected source/build documents; absence is not evidence of non-use.
- lest-c64-needlestack / Runtime profiles (no-evidence-found): Target and timing/reference configuration are recorded in the target-CPU note. No independently verified minimum runnable profile is asserted.
- smashy-smashy-c64 / Runtime profiles (no-evidence-found): Target and timing/reference configuration are recorded in the target-CPU note. No independently verified minimum runnable profile is asserted.
- are-type-c64-jaredevans / Runtime profiles (no-evidence-found): Target and timing/reference configuration are recorded in the target-CPU note. No independently verified minimum runnable profile is asserted.
- are-type-c64-jaredevans / AI (no-evidence-found): No explicit development-AI attribution found in the inspected README and selected source/build documents; absence is not evidence of non-use.

## Morrowind: experimental native Amiga engine

Project ID: amiwind-morrowind-amiga · Overall audit: reviewed

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
  "display_title": "Morrowind: experimental native Amiga engine",
  "id": "amiwind-morrowind-amiga",
  "last_activity": "2026-10-16",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "m68k assembly",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/FlyingFathead/amiwind",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Source and documentation reviewed; independent build/play test not performed",
  "subjects": [
    "Morrowind"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
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
  "title": "AmiWind",
  "tool_kinds": [],
  "types": [
    "native game reimplementation"
  ],
  "upstream_name": "AmiWind",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Experimental CHIM/AmiQuake-derived RPG engine and asset conversion pipeline for Morrowind; current regional coverage is not a complete playable Morrowind port.
- https://github.com/FlyingFathead/amiwind/blob/27fd410c97ee881ae455acb27708ce63ab7ecd8e/README.md
- https://github.com/FlyingFathead/amiwind/blob/27fd410c97ee881ae455acb27708ce63ab7ecd8e/docs/FAQ.md
- https://github.com/FlyingFathead/amiwind/blob/27fd410c97ee881ae455acb27708ce63ab7ecd8e/docs/LICENSING_AND_CREDITS.md

### Classification (reviewed)

Experimental CHIM/AmiQuake-derived RPG engine and asset conversion pipeline for Morrowind; current regional coverage is not a complete playable Morrowind port.
- https://github.com/FlyingFathead/amiwind/blob/27fd410c97ee881ae455acb27708ce63ab7ecd8e/README.md
- https://github.com/FlyingFathead/amiwind/blob/27fd410c97ee881ae455acb27708ce63ab7ecd8e/docs/FAQ.md
- https://github.com/FlyingFathead/amiwind/blob/27fd410c97ee881ae455acb27708ce63ab7ecd8e/docs/LICENSING_AND_CREDITS.md

### Source CPU (not-applicable)

New native game/engine implementation; no predecessor CPU reconstruction was established in this bounded review. Source CPU remains empty.
- https://github.com/FlyingFathead/amiwind/blob/27fd410c97ee881ae455acb27708ce63ab7ecd8e/README.md
- https://github.com/FlyingFathead/amiwind/blob/27fd410c97ee881ae455acb27708ce63ab7ecd8e/docs/FAQ.md
- https://github.com/FlyingFathead/amiwind/blob/27fd410c97ee881ae455acb27708ce63ab7ecd8e/docs/LICENSING_AND_CREDITS.md

### Target CPU (reviewed)

The FAQ explicitly targets 68040 with FPU and AGA in an emulated reference configuration; physical-hardware performance and stock A1200 support remain unproven.
- https://github.com/FlyingFathead/amiwind/blob/27fd410c97ee881ae455acb27708ce63ab7ecd8e/README.md
- https://github.com/FlyingFathead/amiwind/blob/27fd410c97ee881ae455acb27708ce63ab7ecd8e/docs/FAQ.md
- https://github.com/FlyingFathead/amiwind/blob/27fd410c97ee881ae455acb27708ce63ab7ecd8e/docs/LICENSING_AND_CREDITS.md

### Build (reviewed)

README documents conversion from the user's own game files, build scripts, regional emulator checks and substantial remaining gameplay gaps. No independent build or gameplay test was run.
- https://github.com/FlyingFathead/amiwind/blob/27fd410c97ee881ae455acb27708ce63ab7ecd8e/README.md
- https://github.com/FlyingFathead/amiwind/blob/27fd410c97ee881ae455acb27708ce63ab7ecd8e/docs/FAQ.md
- https://github.com/FlyingFathead/amiwind/blob/27fd410c97ee881ae455acb27708ce63ab7ecd8e/docs/LICENSING_AND_CREDITS.md

### Runtime profiles (no-evidence-found)

Target and timing/reference configuration are recorded in the target-CPU note. No independently verified minimum runnable profile is asserted.
- https://github.com/FlyingFathead/amiwind/blob/27fd410c97ee881ae455acb27708ce63ab7ecd8e/README.md
- https://github.com/FlyingFathead/amiwind/blob/27fd410c97ee881ae455acb27708ce63ab7ecd8e/docs/FAQ.md
- https://github.com/FlyingFathead/amiwind/blob/27fd410c97ee881ae455acb27708ce63ab7ecd8e/docs/LICENSING_AND_CREDITS.md

### AI (no-evidence-found)

No explicit development-AI attribution found in the inspected README and selected source/build documents; absence is not evidence of non-use.
- https://github.com/FlyingFathead/amiwind/blob/27fd410c97ee881ae455acb27708ce63ab7ecd8e/README.md
- https://github.com/FlyingFathead/amiwind/blob/27fd410c97ee881ae455acb27708ce63ab7ecd8e/docs/FAQ.md
- https://github.com/FlyingFathead/amiwind/blob/27fd410c97ee881ae455acb27708ce63ab7ecd8e/docs/LICENSING_AND_CREDITS.md

### Relationships (reviewed)

CHIM derives from AmiQuake with component-specific GPL terms; Morrowind assets are user-supplied and not relicensed. This is a native Amiga engine, not a generic emulator.
- https://github.com/FlyingFathead/amiwind/blob/27fd410c97ee881ae455acb27708ce63ab7ecd8e/README.md
- https://github.com/FlyingFathead/amiwind/blob/27fd410c97ee881ae455acb27708ce63ab7ecd8e/docs/FAQ.md
- https://github.com/FlyingFathead/amiwind/blob/27fd410c97ee881ae455acb27708ce63ab7ecd8e/docs/LICENSING_AND_CREDITS.md

## Stunt Car Racer: Amiga performance and track-editor patch

Project ID: stunt-car-racer-performance-patch · Overall audit: reviewed

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
  "display_title": "Stunt Car Racer: Amiga performance and track-editor patch",
  "id": "stunt-car-racer-performance-patch",
  "last_activity": "2026-10-04",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "m68k assembly",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/timoheimonen/amiga-stunt-car-racer-060-performance-patch",
  "runtime_profiles": [],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [
    "m68k assembly"
  ],
  "source_platforms": [
    "Amiga"
  ],
  "status": "Source and documentation reviewed; independent build/play test not performed",
  "subjects": [
    "Stunt Car Racer"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
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
  "title": "Stunt Car Racer Performance",
  "tool_kinds": [],
  "types": [
    "game patch"
  ],
  "upstream_name": "Stunt Car Racer Performance",
  "work_kinds": [
    "patching",
    "binary-analysis"
  ]
}
```

### Identity (reviewed)

Game-specific source patch adds 50 Hz physics/rendering, a track editor and beta serial multiplayer while retaining the original timer cadence.
- https://github.com/timoheimonen/amiga-stunt-car-racer-060-performance-patch/blob/257d4ec50e82230205dc278d905564f1e945a09f/README.md
- https://github.com/timoheimonen/amiga-stunt-car-racer-060-performance-patch/blob/257d4ec50e82230205dc278d905564f1e945a09f/src/SCR_Player20ms.s
- https://github.com/timoheimonen/amiga-stunt-car-racer-060-performance-patch/blob/257d4ec50e82230205dc278d905564f1e945a09f/patch.py

### Classification (reviewed)

Game-specific source patch adds 50 Hz physics/rendering, a track editor and beta serial multiplayer while retaining the original timer cadence.
- https://github.com/timoheimonen/amiga-stunt-car-racer-060-performance-patch/blob/257d4ec50e82230205dc278d905564f1e945a09f/README.md
- https://github.com/timoheimonen/amiga-stunt-car-racer-060-performance-patch/blob/257d4ec50e82230205dc278d905564f1e945a09f/src/SCR_Player20ms.s
- https://github.com/timoheimonen/amiga-stunt-car-racer-060-performance-patch/blob/257d4ec50e82230205dc278d905564f1e945a09f/patch.py

### Source CPU (reviewed)

Original game and patch use 68k addressing and register conventions documented in the inspected assembly.
- https://github.com/timoheimonen/amiga-stunt-car-racer-060-performance-patch/blob/257d4ec50e82230205dc278d905564f1e945a09f/README.md
- https://github.com/timoheimonen/amiga-stunt-car-racer-060-performance-patch/blob/257d4ec50e82230205dc278d905564f1e945a09f/src/SCR_Player20ms.s
- https://github.com/timoheimonen/amiga-stunt-car-racer-060-performance-patch/blob/257d4ec50e82230205dc278d905564f1e945a09f/patch.py

### Target CPU (reviewed)

The 68000 assembly integration kernel is inspected; the documented overall target is primarily emulated MC68060 Amiga with 2 MiB Chip RAM and additional Fast RAM.
- https://github.com/timoheimonen/amiga-stunt-car-racer-060-performance-patch/blob/257d4ec50e82230205dc278d905564f1e945a09f/README.md
- https://github.com/timoheimonen/amiga-stunt-car-racer-060-performance-patch/blob/257d4ec50e82230205dc278d905564f1e945a09f/src/SCR_Player20ms.s
- https://github.com/timoheimonen/amiga-stunt-car-racer-060-performance-patch/blob/257d4ec50e82230205dc278d905564f1e945a09f/patch.py

### Build (reviewed)

Python patcher accepts a checksum-matched user-owned ADF, includes assembly sources and offers WHDLoad output. Upstream frame-rate and compatibility claims were not independently tested.
- https://github.com/timoheimonen/amiga-stunt-car-racer-060-performance-patch/blob/257d4ec50e82230205dc278d905564f1e945a09f/README.md
- https://github.com/timoheimonen/amiga-stunt-car-racer-060-performance-patch/blob/257d4ec50e82230205dc278d905564f1e945a09f/src/SCR_Player20ms.s
- https://github.com/timoheimonen/amiga-stunt-car-racer-060-performance-patch/blob/257d4ec50e82230205dc278d905564f1e945a09f/patch.py

### Runtime profiles (no-evidence-found)

Target and timing/reference configuration are recorded in the target-CPU note. No independently verified minimum runnable profile is asserted.
- https://github.com/timoheimonen/amiga-stunt-car-racer-060-performance-patch/blob/257d4ec50e82230205dc278d905564f1e945a09f/README.md
- https://github.com/timoheimonen/amiga-stunt-car-racer-060-performance-patch/blob/257d4ec50e82230205dc278d905564f1e945a09f/src/SCR_Player20ms.s
- https://github.com/timoheimonen/amiga-stunt-car-racer-060-performance-patch/blob/257d4ec50e82230205dc278d905564f1e945a09f/patch.py

### AI (no-evidence-found)

No explicit development-AI attribution found in the inspected README and selected source/build documents; absence is not evidence of non-use.
- https://github.com/timoheimonen/amiga-stunt-car-racer-060-performance-patch/blob/257d4ec50e82230205dc278d905564f1e945a09f/README.md
- https://github.com/timoheimonen/amiga-stunt-car-racer-060-performance-patch/blob/257d4ec50e82230205dc278d905564f1e945a09f/src/SCR_Player20ms.s
- https://github.com/timoheimonen/amiga-stunt-car-racer-060-performance-patch/blob/257d4ec50e82230205dc278d905564f1e945a09f/patch.py

### Relationships (reviewed)

MIT covers patch code, not original game or Kickstart assets. Distinct from a complete source restoration.
- https://github.com/timoheimonen/amiga-stunt-car-racer-060-performance-patch/blob/257d4ec50e82230205dc278d905564f1e945a09f/README.md
- https://github.com/timoheimonen/amiga-stunt-car-racer-060-performance-patch/blob/257d4ec50e82230205dc278d905564f1e945a09f/src/SCR_Player20ms.s
- https://github.com/timoheimonen/amiga-stunt-car-racer-060-performance-patch/blob/257d4ec50e82230205dc278d905564f1e945a09f/patch.py

## CORE: Atari ST vector arcade game

Project ID: core-atari-st-flindholm · Overall audit: reviewed

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
  "display_title": "CORE: Atari ST vector arcade game",
  "id": "core-atari-st-flindholm",
  "last_activity": "2026-10-01",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "m68k assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/flindholm-lab/CORE",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Source and documentation reviewed; independent build/play test not performed",
  "subjects": [
    "CORE"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
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
  "title": "CORE",
  "tool_kinds": [],
  "types": [
    "native homebrew game"
  ],
  "upstream_name": "CORE",
  "work_kinds": []
}
```

### Identity (reviewed)

Native arcade game about timing inward jumps through rotating defensive rings; includes source and a PRG.
- https://github.com/flindholm-lab/CORE/blob/9bdd939525c0e7d36e8015164dae0e81365fe2f0/README.md
- https://github.com/flindholm-lab/CORE/blob/9bdd939525c0e7d36e8015164dae0e81365fe2f0/core.c

### Classification (reviewed)

Native homebrew game; not binary-derived reconstruction.
- https://github.com/flindholm-lab/CORE/blob/9bdd939525c0e7d36e8015164dae0e81365fe2f0/README.md
- https://github.com/flindholm-lab/CORE/blob/9bdd939525c0e7d36e8015164dae0e81365fe2f0/core.c

### Source CPU (not-applicable)

New native game/engine implementation; no predecessor CPU reconstruction was established in this bounded review. Source CPU remains empty.
- https://github.com/flindholm-lab/CORE/blob/9bdd939525c0e7d36e8015164dae0e81365fe2f0/README.md
- https://github.com/flindholm-lab/CORE/blob/9bdd939525c0e7d36e8015164dae0e81365fe2f0/core.c

### Target CPU (reviewed)

core.c uses explicit 68000 trap wrappers and ST display hardware; README specifies vbcc m68k-atari/TOS and ST/STE targets.
- https://github.com/flindholm-lab/CORE/blob/9bdd939525c0e7d36e8015164dae0e81365fe2f0/README.md
- https://github.com/flindholm-lab/CORE/blob/9bdd939525c0e7d36e8015164dae0e81365fe2f0/core.c

### Build (reviewed)

README supplies a vbcc build command and claims ST/STE and Hatari testing. It names core2.c/core2.prg, while the inspected tree contains core.c/core.prg and the source header gives the matching core.c command. Build was not independently run.
- https://github.com/flindholm-lab/CORE/blob/9bdd939525c0e7d36e8015164dae0e81365fe2f0/README.md
- https://github.com/flindholm-lab/CORE/blob/9bdd939525c0e7d36e8015164dae0e81365fe2f0/core.c

### Runtime profiles (no-evidence-found)

Target and timing/reference configuration are recorded in the target-CPU note. No independently verified minimum runnable profile is asserted.
- https://github.com/flindholm-lab/CORE/blob/9bdd939525c0e7d36e8015164dae0e81365fe2f0/README.md
- https://github.com/flindholm-lab/CORE/blob/9bdd939525c0e7d36e8015164dae0e81365fe2f0/core.c

### AI (no-evidence-found)

No explicit development-AI attribution found in the inspected README and selected source/build documents; absence is not evidence of non-use.
- https://github.com/flindholm-lab/CORE/blob/9bdd939525c0e7d36e8015164dae0e81365fe2f0/README.md
- https://github.com/flindholm-lab/CORE/blob/9bdd939525c0e7d36e8015164dae0e81365fe2f0/core.c

### Relationships (reviewed)

Original homebrew inspired by vector-arcade aesthetics; no predecessor binary reconstruction is claimed.
- https://github.com/flindholm-lab/CORE/blob/9bdd939525c0e7d36e8015164dae0e81365fe2f0/README.md
- https://github.com/flindholm-lab/CORE/blob/9bdd939525c0e7d36e8015164dae0e81365fe2f0/core.c

## Super Sprint: Atari ST four-player restoration and patches

Project ID: super-sprint-reforged-st · Overall audit: reviewed

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
  "display_title": "Super Sprint: Atari ST four-player restoration and patches",
  "id": "super-sprint-reforged-st",
  "last_activity": "2026-10-04",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "m68k assembly",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/stephane-perez/super-sprint-reforged",
  "runtime_profiles": [],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [
    "m68k assembly"
  ],
  "source_platforms": [
    "Atari ST"
  ],
  "status": "Source and documentation reviewed; independent build/play test not performed",
  "subjects": [
    "Super Sprint"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
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
  "title": "Super Sprint Reforged",
  "tool_kinds": [],
  "types": [
    "game patch"
  ],
  "upstream_name": "Super Sprint Reforged",
  "work_kinds": [
    "disassembly",
    "binary-analysis",
    "patching"
  ]
}
```

### Identity (reviewed)

Reverse-engineering and patch project enabling a human fourth car, additional controller interfaces, hard-disk loading and reset fixes.
- https://github.com/stephane-perez/super-sprint-reforged/blob/7840cfc1eb981768fde9754e9378bb2ab779e69f/README.md
- https://github.com/stephane-perez/super-sprint-reforged/blob/7840cfc1eb981768fde9754e9378bb2ab779e69f/src/p4.s
- https://github.com/stephane-perez/super-sprint-reforged/blob/7840cfc1eb981768fde9754e9378bb2ab779e69f/Makefile

### Classification (reviewed)

Reverse-engineering and patch project enabling a human fourth car, additional controller interfaces, hard-disk loading and reset fixes.
- https://github.com/stephane-perez/super-sprint-reforged/blob/7840cfc1eb981768fde9754e9378bb2ab779e69f/README.md
- https://github.com/stephane-perez/super-sprint-reforged/blob/7840cfc1eb981768fde9754e9378bb2ab779e69f/src/p4.s
- https://github.com/stephane-perez/super-sprint-reforged/blob/7840cfc1eb981768fde9754e9378bb2ab779e69f/Makefile

### Source CPU (reviewed)

Original game and patch use 68k addressing and register conventions documented in the inspected assembly.
- https://github.com/stephane-perez/super-sprint-reforged/blob/7840cfc1eb981768fde9754e9378bb2ab779e69f/README.md
- https://github.com/stephane-perez/super-sprint-reforged/blob/7840cfc1eb981768fde9754e9378bb2ab779e69f/src/p4.s
- https://github.com/stephane-perez/super-sprint-reforged/blob/7840cfc1eb981768fde9754e9378bb2ab779e69f/Makefile

### Target CPU (reviewed)

src/p4.s is PC-relative 68000 code appended to the original TOS TEXT segment, with documented A4/A5 game-state conventions and rewritten relocations.
- https://github.com/stephane-perez/super-sprint-reforged/blob/7840cfc1eb981768fde9754e9378bb2ab779e69f/README.md
- https://github.com/stephane-perez/super-sprint-reforged/blob/7840cfc1eb981768fde9754e9378bb2ab779e69f/src/p4.s
- https://github.com/stephane-perez/super-sprint-reforged/blob/7840cfc1eb981768fde9754e9378bb2ab779e69f/Makefile

### Build (reviewed)

Makefile builds the assembly patch; user-supplied matching game files are required. README reports EmuTOS ST/STE checks and documents fourth-player limitations. No independent build or gameplay test.
- https://github.com/stephane-perez/super-sprint-reforged/blob/7840cfc1eb981768fde9754e9378bb2ab779e69f/README.md
- https://github.com/stephane-perez/super-sprint-reforged/blob/7840cfc1eb981768fde9754e9378bb2ab779e69f/src/p4.s
- https://github.com/stephane-perez/super-sprint-reforged/blob/7840cfc1eb981768fde9754e9378bb2ab779e69f/Makefile

### Runtime profiles (no-evidence-found)

Target and timing/reference configuration are recorded in the target-CPU note. No independently verified minimum runnable profile is asserted.
- https://github.com/stephane-perez/super-sprint-reforged/blob/7840cfc1eb981768fde9754e9378bb2ab779e69f/README.md
- https://github.com/stephane-perez/super-sprint-reforged/blob/7840cfc1eb981768fde9754e9378bb2ab779e69f/src/p4.s
- https://github.com/stephane-perez/super-sprint-reforged/blob/7840cfc1eb981768fde9754e9378bb2ab779e69f/Makefile

### AI (no-evidence-found)

No explicit development-AI attribution found in the inspected README and selected source/build documents; absence is not evidence of non-use.
- https://github.com/stephane-perez/super-sprint-reforged/blob/7840cfc1eb981768fde9754e9378bb2ab779e69f/README.md
- https://github.com/stephane-perez/super-sprint-reforged/blob/7840cfc1eb981768fde9754e9378bb2ab779e69f/src/p4.s
- https://github.com/stephane-perez/super-sprint-reforged/blob/7840cfc1eb981768fde9754e9378bb2ab779e69f/Makefile

### Relationships (reviewed)

Uses methods of the separately tracked IK+ Reforged but targets a distinct game. MIT applies only to the project's original code; game data is not distributed.
- https://github.com/stephane-perez/super-sprint-reforged/blob/7840cfc1eb981768fde9754e9378bb2ab779e69f/README.md
- https://github.com/stephane-perez/super-sprint-reforged/blob/7840cfc1eb981768fde9754e9378bb2ab779e69f/src/p4.s
- https://github.com/stephane-perez/super-sprint-reforged/blob/7840cfc1eb981768fde9754e9378bb2ab779e69f/Makefile

## Lest: native C64 first-person 3D game

Project ID: lest-c64-needlestack · Overall audit: reviewed

### Typed catalogue values

```json
{
  "ai": {
    "tools": [
      "Claude Code"
    ],
    "usage": true
  },
  "build": {
    "byte_exact": null,
    "compilable": null,
    "playable": null,
    "runnable": null
  },
  "display_title": "Lest: native C64 first-person 3D game",
  "id": "lest-c64-needlestack",
  "last_activity": "2026-10-16",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "6502 assembly",
    "JavaScript"
  ],
  "record_class": "subject",
  "repo": "https://github.com/needlestack/lest-c64",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Source and documentation reviewed; independent build/play test not performed",
  "subjects": [
    "Lest"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "6502"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Commodore 64"
  ],
  "techniques": [],
  "title": "Lest",
  "tool_kinds": [],
  "types": [
    "native homebrew game"
  ],
  "upstream_name": "Lest",
  "work_kinds": []
}
```

### Identity (reviewed)

Native first-person homebrew using a fitted character-mode wall renderer, hardware-sprite entities and disk-loaded levels; formerly called c64fps.
- https://github.com/needlestack/lest-c64/blob/8f6c9f688d8bbcd5fd4e48c24d43ed11a42b9738/README.md
- https://github.com/needlestack/lest-c64/blob/8f6c9f688d8bbcd5fd4e48c24d43ed11a42b9738/build/iray.asm

### Classification (reviewed)

Native homebrew game; not binary-derived reconstruction.
- https://github.com/needlestack/lest-c64/blob/8f6c9f688d8bbcd5fd4e48c24d43ed11a42b9738/README.md
- https://github.com/needlestack/lest-c64/blob/8f6c9f688d8bbcd5fd4e48c24d43ed11a42b9738/build/iray.asm

### Source CPU (not-applicable)

New native game/engine implementation; no predecessor CPU reconstruction was established in this bounded review. Source CPU remains empty.
- https://github.com/needlestack/lest-c64/blob/8f6c9f688d8bbcd5fd4e48c24d43ed11a42b9738/README.md
- https://github.com/needlestack/lest-c64/blob/8f6c9f688d8bbcd5fd4e48c24d43ed11a42b9738/build/iray.asm

### Target CPU (reviewed)

README identifies emitted 6502 assembly and a stock C64 target; the inspected generated assembly is build/iray.asm. JavaScript is the host build/generation language, not the runtime CPU.
- https://github.com/needlestack/lest-c64/blob/8f6c9f688d8bbcd5fd4e48c24d43ed11a42b9738/README.md
- https://github.com/needlestack/lest-c64/blob/8f6c9f688d8bbcd5fd4e48c24d43ed11a42b9738/build/iray.asm

### Build (reviewed)

Node.js and ImageMagick build a D64 with an in-repository assembler and disk writer. README documents an NTSC target, Krill loader and VICE true-drive setting; no independent build or play test.
- https://github.com/needlestack/lest-c64/blob/8f6c9f688d8bbcd5fd4e48c24d43ed11a42b9738/README.md
- https://github.com/needlestack/lest-c64/blob/8f6c9f688d8bbcd5fd4e48c24d43ed11a42b9738/build/iray.asm

### Runtime profiles (no-evidence-found)

Target and timing/reference configuration are recorded in the target-CPU note. No independently verified minimum runnable profile is asserted.
- https://github.com/needlestack/lest-c64/blob/8f6c9f688d8bbcd5fd4e48c24d43ed11a42b9738/README.md
- https://github.com/needlestack/lest-c64/blob/8f6c9f688d8bbcd5fd4e48c24d43ed11a42b9738/build/iray.asm

### AI (reviewed)

README explicitly attributes development to Claude Code.
- https://github.com/needlestack/lest-c64/blob/8f6c9f688d8bbcd5fd4e48c24d43ed11a42b9738/README.md
- https://github.com/needlestack/lest-c64/blob/8f6c9f688d8bbcd5fd4e48c24d43ed11a42b9738/build/iray.asm

### Relationships (reviewed)

Original Jonathan Field game with credited Krill loader and Exomizer components; README explicitly credits Claude Code development. MIT project code with separate third-party notices.
- https://github.com/needlestack/lest-c64/blob/8f6c9f688d8bbcd5fd4e48c24d43ed11a42b9738/README.md
- https://github.com/needlestack/lest-c64/blob/8f6c9f688d8bbcd5fd4e48c24d43ed11a42b9738/build/iray.asm

## Smashy Smashy: C64 platform-smashing game

Project ID: smashy-smashy-c64 · Overall audit: reviewed

### Typed catalogue values

```json
{
  "ai": {
    "tools": [
      "Claude Code"
    ],
    "usage": true
  },
  "build": {
    "byte_exact": null,
    "compilable": null,
    "playable": null,
    "runnable": null
  },
  "display_title": "Smashy Smashy: C64 platform-smashing game",
  "id": "smashy-smashy-c64",
  "last_activity": "2026-10-16",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "Prog8",
    "6502 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/revlayle/smashy-smashy",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Source and documentation reviewed; independent build/play test not performed",
  "subjects": [
    "Smashy Smashy"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "6502"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Commodore 64"
  ],
  "techniques": [],
  "title": "Smashy Smashy",
  "tool_kinds": [],
  "types": [
    "native homebrew game"
  ],
  "upstream_name": "Smashy Smashy",
  "work_kinds": []
}
```

### Identity (reviewed)

Native single-screen platform game with procedural levels, treasure collection, enemies and smash-chain scoring.
- https://github.com/revlayle/smashy-smashy/blob/2b190d97a6c77d3d3029492c551ebeee2321bc5c/README.md
- https://github.com/revlayle/smashy-smashy/blob/2b190d97a6c77d3d3029492c551ebeee2321bc5c/src/main.p8

### Classification (reviewed)

Native homebrew game; not binary-derived reconstruction.
- https://github.com/revlayle/smashy-smashy/blob/2b190d97a6c77d3d3029492c551ebeee2321bc5c/README.md
- https://github.com/revlayle/smashy-smashy/blob/2b190d97a6c77d3d3029492c551ebeee2321bc5c/src/main.p8

### Source CPU (not-applicable)

New native game/engine implementation; no predecessor CPU reconstruction was established in this bounded review. Source CPU remains empty.
- https://github.com/revlayle/smashy-smashy/blob/2b190d97a6c77d3d3029492c551ebeee2321bc5c/README.md
- https://github.com/revlayle/smashy-smashy/blob/2b190d97a6c77d3d3029492c551ebeee2321bc5c/src/main.p8

### Target CPU (reviewed)

Prog8 source targets C64 and is compiled through 64tass into native 6502-family code; README describes PAL timing and faster NTSC play.
- https://github.com/revlayle/smashy-smashy/blob/2b190d97a6c77d3d3029492c551ebeee2321bc5c/README.md
- https://github.com/revlayle/smashy-smashy/blob/2b190d97a6c77d3d3029492c551ebeee2321bc5c/src/main.p8

### Build (reviewed)

README supplies build/run scripts and pinned Prog8 toolchain, screenshots and self-test scenarios. No independent build, execution or gameplay verification was performed.
- https://github.com/revlayle/smashy-smashy/blob/2b190d97a6c77d3d3029492c551ebeee2321bc5c/README.md
- https://github.com/revlayle/smashy-smashy/blob/2b190d97a6c77d3d3029492c551ebeee2321bc5c/src/main.p8

### Runtime profiles (no-evidence-found)

Target and timing/reference configuration are recorded in the target-CPU note. No independently verified minimum runnable profile is asserted.
- https://github.com/revlayle/smashy-smashy/blob/2b190d97a6c77d3d3029492c551ebeee2321bc5c/README.md
- https://github.com/revlayle/smashy-smashy/blob/2b190d97a6c77d3d3029492c551ebeee2321bc5c/src/main.p8

### AI (reviewed)

README explicitly attributes development to Claude Code.
- https://github.com/revlayle/smashy-smashy/blob/2b190d97a6c77d3d3029492c551ebeee2321bc5c/README.md
- https://github.com/revlayle/smashy-smashy/blob/2b190d97a6c77d3d3029492c551ebeee2321bc5c/src/main.p8

### Relationships (reviewed)

Designed by Rev. Layle and explicitly written with Claude Code; graphics are disclosed as AI-generated placeholders. MIT game with separately licensed Prog8 guides.
- https://github.com/revlayle/smashy-smashy/blob/2b190d97a6c77d3d3029492c551ebeee2321bc5c/README.md
- https://github.com/revlayle/smashy-smashy/blob/2b190d97a6c77d3d3029492c551ebeee2321bc5c/src/main.p8

## ARE-TYPE: C64 horizontal shoot-em-up

Project ID: are-type-c64-jaredevans · Overall audit: reviewed

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
  "display_title": "ARE-TYPE: C64 horizontal shoot-em-up",
  "id": "are-type-c64-jaredevans",
  "last_activity": "2026-07-26",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "6502 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/jaredevans/c64-shmup",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Source and documentation reviewed; independent build/play test not performed",
  "subjects": [
    "ARE-TYPE"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "6502"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Commodore 64"
  ],
  "techniques": [],
  "title": "ARE-TYPE",
  "tool_kinds": [],
  "types": [
    "native homebrew game"
  ],
  "upstream_name": "ARE-TYPE",
  "work_kinds": []
}
```

### Identity (reviewed)

R-Type-inspired native horizontal shooter with charge beam, bosses, sprite multiplexing and SID soundtrack; not a reconstruction of R-Type.
- https://github.com/jaredevans/c64-shmup/blob/63554e26e83fb209a41ccf1def1ede4c5f0c4a2e/README.md
- https://github.com/jaredevans/c64-shmup/blob/63554e26e83fb209a41ccf1def1ede4c5f0c4a2e/scroll.asm

### Classification (reviewed)

Native homebrew game; not binary-derived reconstruction.
- https://github.com/jaredevans/c64-shmup/blob/63554e26e83fb209a41ccf1def1ede4c5f0c4a2e/README.md
- https://github.com/jaredevans/c64-shmup/blob/63554e26e83fb209a41ccf1def1ede4c5f0c4a2e/scroll.asm

### Source CPU (not-applicable)

New native game/engine implementation; no predecessor CPU reconstruction was established in this bounded review. Source CPU remains empty.
- https://github.com/jaredevans/c64-shmup/blob/63554e26e83fb209a41ccf1def1ede4c5f0c4a2e/README.md
- https://github.com/jaredevans/c64-shmup/blob/63554e26e83fb209a41ccf1def1ede4c5f0c4a2e/scroll.asm

### Target CPU (reviewed)

README and scroll.asm identify 6502 assembly, C64 VIC/SID hardware and the ACME assembler; target is PAL C64.
- https://github.com/jaredevans/c64-shmup/blob/63554e26e83fb209a41ccf1def1ede4c5f0c4a2e/README.md
- https://github.com/jaredevans/c64-shmup/blob/63554e26e83fb209a41ccf1def1ede4c5f0c4a2e/scroll.asm

### Build (reviewed)

README provides ACME/VICE commands and a gameplay demonstration. The annotated source is claimed to match its own source binary, not an original commercial game. No independent build or play test.
- https://github.com/jaredevans/c64-shmup/blob/63554e26e83fb209a41ccf1def1ede4c5f0c4a2e/README.md
- https://github.com/jaredevans/c64-shmup/blob/63554e26e83fb209a41ccf1def1ede4c5f0c4a2e/scroll.asm

### Runtime profiles (no-evidence-found)

Target and timing/reference configuration are recorded in the target-CPU note. No independently verified minimum runnable profile is asserted.
- https://github.com/jaredevans/c64-shmup/blob/63554e26e83fb209a41ccf1def1ede4c5f0c4a2e/README.md
- https://github.com/jaredevans/c64-shmup/blob/63554e26e83fb209a41ccf1def1ede4c5f0c4a2e/scroll.asm

### AI (no-evidence-found)

No explicit development-AI attribution found in the inspected README and selected source/build documents; absence is not evidence of non-use.
- https://github.com/jaredevans/c64-shmup/blob/63554e26e83fb209a41ccf1def1ede4c5f0c4a2e/README.md
- https://github.com/jaredevans/c64-shmup/blob/63554e26e83fb209a41ccf1def1ede4c5f0c4a2e/scroll.asm

### Relationships (reviewed)

Original homebrew inspired by R-Type. A separate Dies Irae SID arrangement is included in the same repository rather than promoted as another game.
- https://github.com/jaredevans/c64-shmup/blob/63554e26e83fb209a41ccf1def1ede4c5f0c4a2e/README.md
- https://github.com/jaredevans/c64-shmup/blob/63554e26e83fb209a41ccf1def1ede4c5f0c4a2e/scroll.asm

## Sources

```json
[
  {
    "id": "github-flyingfathead-amiwind",
    "kind": "github-repository",
    "reason": "Experimental CHIM/AmiQuake-derived RPG engine and asset conversion pipeline for Morrowind; current regional coverage is not a complete playable Morrowind port.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/FlyingFathead/amiwind"
  },
  {
    "id": "github-timoheimonen-amiga-stunt-car-racer-060-performance-patch",
    "kind": "github-repository",
    "reason": "Game-specific source patch adds 50 Hz physics/rendering, a track editor and beta serial multiplayer while retaining the original timer cadence.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/timoheimonen/amiga-stunt-car-racer-060-performance-patch"
  },
  {
    "id": "github-flindholm-lab-core",
    "kind": "github-repository",
    "reason": "Native arcade game about timing inward jumps through rotating defensive rings; includes source and a PRG.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/flindholm-lab/CORE"
  },
  {
    "id": "github-stephane-perez-super-sprint-reforged",
    "kind": "github-repository",
    "reason": "Reverse-engineering and patch project enabling a human fourth car, additional controller interfaces, hard-disk loading and reset fixes.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/stephane-perez/super-sprint-reforged"
  },
  {
    "id": "github-needlestack-lest-c64",
    "kind": "github-repository",
    "reason": "Native first-person homebrew using a fitted character-mode wall renderer, hardware-sprite entities and disk-loaded levels; formerly called c64fps.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/needlestack/lest-c64"
  },
  {
    "id": "github-revlayle-smashy-smashy",
    "kind": "github-repository",
    "reason": "Native single-screen platform game with procedural levels, treasure collection, enemies and smash-chain scoring.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/revlayle/smashy-smashy"
  },
  {
    "id": "github-jaredevans-c64-shmup",
    "kind": "github-repository",
    "reason": "R-Type-inspired native horizontal shooter with charge beam, bosses, sprite multiplexing and SID soundtrack; not a reconstruction of R-Type.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/jaredevans/c64-shmup"
  },
  {
    "id": "github-apolkosnik-chorensha",
    "kind": "github-repository",
    "reason": "README explicitly says original X68000 program runs with X68000 hardware emulated in software. Deferred for game-specific-emulation review under the user's inclusion policy; not added as a native reimplementation.",
    "review_state": "partial",
    "source": "https://github.com/apolkosnik/chorensha"
  },
  {
    "id": "github-kle256-atari-ste-brick-break",
    "kind": "github-repository",
    "reason": "README explicitly labels this scaffolding only with no game behaviour, rendering or tests. Defer until substantive implementation is verified.",
    "review_state": "partial",
    "source": "https://github.com/kle256/Atari-STE-Brick-Break"
  }
]
```

## Tasks

```json
[
  {
    "description": "Review Cho Ren Sha Amiga port under the game-specific hardware-emulation inclusion policy.",
    "id": "review-chorensha-amiga-execution-model",
    "notes": "Original 68000 program executes with X68000 hardware emulated; do not promote as native reimplementation without classification review.",
    "priority": "normal",
    "source_ids": [
      "github-apolkosnik-chorensha"
    ],
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
      "https://github.com/FlyingFathead/amiwind/blob/27fd410c97ee881ae455acb27708ce63ab7ecd8e/README.md",
      "https://github.com/FlyingFathead/amiwind/blob/27fd410c97ee881ae455acb27708ce63ab7ecd8e/docs/FAQ.md",
      "https://github.com/FlyingFathead/amiwind/blob/27fd410c97ee881ae455acb27708ce63ab7ecd8e/docs/LICENSING_AND_CREDITS.md"
    ],
    "id": "2026-10-17-promote-amiwind-morrowind-amiga",
    "project_ids": [
      "amiwind-morrowind-amiga"
    ],
    "reason": "Experimental CHIM/AmiQuake-derived RPG engine and asset conversion pipeline for Morrowind; current regional coverage is not a complete playable Morrowind port.",
    "source_ids": [
      "github-flyingfathead-amiwind"
    ],
    "title": "AmiWind",
    "url": "https://github.com/FlyingFathead/amiwind"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/timoheimonen/amiga-stunt-car-racer-060-performance-patch/blob/257d4ec50e82230205dc278d905564f1e945a09f/README.md",
      "https://github.com/timoheimonen/amiga-stunt-car-racer-060-performance-patch/blob/257d4ec50e82230205dc278d905564f1e945a09f/src/SCR_Player20ms.s",
      "https://github.com/timoheimonen/amiga-stunt-car-racer-060-performance-patch/blob/257d4ec50e82230205dc278d905564f1e945a09f/patch.py"
    ],
    "id": "2026-10-17-promote-stunt-car-racer-performance-patch",
    "project_ids": [
      "stunt-car-racer-performance-patch"
    ],
    "reason": "Game-specific source patch adds 50 Hz physics/rendering, a track editor and beta serial multiplayer while retaining the original timer cadence.",
    "source_ids": [
      "github-timoheimonen-amiga-stunt-car-racer-060-performance-patch"
    ],
    "title": "Stunt Car Racer Performance",
    "url": "https://github.com/timoheimonen/amiga-stunt-car-racer-060-performance-patch"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/flindholm-lab/CORE/blob/9bdd939525c0e7d36e8015164dae0e81365fe2f0/README.md",
      "https://github.com/flindholm-lab/CORE/blob/9bdd939525c0e7d36e8015164dae0e81365fe2f0/core.c"
    ],
    "id": "2026-10-17-promote-core-atari-st-flindholm",
    "project_ids": [
      "core-atari-st-flindholm"
    ],
    "reason": "Native arcade game about timing inward jumps through rotating defensive rings; includes source and a PRG.",
    "source_ids": [
      "github-flindholm-lab-core"
    ],
    "title": "CORE",
    "url": "https://github.com/flindholm-lab/CORE"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/stephane-perez/super-sprint-reforged/blob/7840cfc1eb981768fde9754e9378bb2ab779e69f/README.md",
      "https://github.com/stephane-perez/super-sprint-reforged/blob/7840cfc1eb981768fde9754e9378bb2ab779e69f/src/p4.s",
      "https://github.com/stephane-perez/super-sprint-reforged/blob/7840cfc1eb981768fde9754e9378bb2ab779e69f/Makefile"
    ],
    "id": "2026-10-17-promote-super-sprint-reforged-st",
    "project_ids": [
      "super-sprint-reforged-st"
    ],
    "reason": "Reverse-engineering and patch project enabling a human fourth car, additional controller interfaces, hard-disk loading and reset fixes.",
    "source_ids": [
      "github-stephane-perez-super-sprint-reforged"
    ],
    "title": "Super Sprint Reforged",
    "url": "https://github.com/stephane-perez/super-sprint-reforged"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/needlestack/lest-c64/blob/8f6c9f688d8bbcd5fd4e48c24d43ed11a42b9738/README.md",
      "https://github.com/needlestack/lest-c64/blob/8f6c9f688d8bbcd5fd4e48c24d43ed11a42b9738/build/iray.asm"
    ],
    "id": "2026-10-17-promote-lest-c64-needlestack",
    "project_ids": [
      "lest-c64-needlestack"
    ],
    "reason": "Native first-person homebrew using a fitted character-mode wall renderer, hardware-sprite entities and disk-loaded levels; formerly called c64fps.",
    "source_ids": [
      "github-needlestack-lest-c64"
    ],
    "title": "Lest",
    "url": "https://github.com/needlestack/lest-c64"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/revlayle/smashy-smashy/blob/2b190d97a6c77d3d3029492c551ebeee2321bc5c/README.md",
      "https://github.com/revlayle/smashy-smashy/blob/2b190d97a6c77d3d3029492c551ebeee2321bc5c/src/main.p8"
    ],
    "id": "2026-10-17-promote-smashy-smashy-c64",
    "project_ids": [
      "smashy-smashy-c64"
    ],
    "reason": "Native single-screen platform game with procedural levels, treasure collection, enemies and smash-chain scoring.",
    "source_ids": [
      "github-revlayle-smashy-smashy"
    ],
    "title": "Smashy Smashy",
    "url": "https://github.com/revlayle/smashy-smashy"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/jaredevans/c64-shmup/blob/63554e26e83fb209a41ccf1def1ede4c5f0c4a2e/README.md",
      "https://github.com/jaredevans/c64-shmup/blob/63554e26e83fb209a41ccf1def1ede4c5f0c4a2e/scroll.asm"
    ],
    "id": "2026-10-17-promote-are-type-c64-jaredevans",
    "project_ids": [
      "are-type-c64-jaredevans"
    ],
    "reason": "R-Type-inspired native horizontal shooter with charge beam, bosses, sprite multiplexing and SID soundtrack; not a reconstruction of R-Type.",
    "source_ids": [
      "github-jaredevans-c64-shmup"
    ],
    "title": "ARE-TYPE",
    "url": "https://github.com/jaredevans/c64-shmup"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/apolkosnik/chorensha/blob/amiga-port/README.md"
    ],
    "id": "2026-10-17-defer-apolkosnik-chorensha",
    "project_ids": [],
    "reason": "README explicitly says original X68000 program runs with X68000 hardware emulated in software. Deferred for game-specific-emulation review under the user's inclusion policy; not added as a native reimplementation.",
    "source_ids": [
      "github-apolkosnik-chorensha"
    ],
    "title": "Cho Ren Sha 68k Amiga port",
    "url": "https://github.com/apolkosnik/chorensha"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/kle256/Atari-STE-Brick-Break/blob/main/README.md"
    ],
    "id": "2026-10-17-defer-kle256-atari-ste-brick-break",
    "project_ids": [],
    "reason": "README explicitly labels this scaffolding only with no game behaviour, rendering or tests. Defer until substantive implementation is verified.",
    "source_ids": [
      "github-kle256-atari-ste-brick-break"
    ],
    "title": "Atari STE Brick Break",
    "url": "https://github.com/kle256/Atari-STE-Brick-Break"
  }
]
```
