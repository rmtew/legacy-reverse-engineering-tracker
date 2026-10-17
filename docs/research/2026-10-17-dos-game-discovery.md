# Add twelve DOS-related game projects covering original sources, a matching reconstruction, native homebrew and an original-source Linux port.

Add twelve DOS-related game projects covering original sources, a matching reconstruction, native homebrew and an original-source Linux port.

Date: 2026-10-17 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- dosraptor-original / Runtime profiles (no-evidence-found): Native 32-bit DOS protected-mode executable,386 flat DOS/4G. No complete minimum CPU/RAM/OS configuration was established. Compiler architecture and recommended emulator are not proof of hardware compatibility.
- dosraptor-original / AI (no-evidence-found): No explicit AI-development claim found in inspected project documentation. This is unknown, not a negative determination.
- kens-labyrinth-original-dos / Runtime profiles (no-evidence-found): Native 16-bit DOS; LAB3D.C contains main game loop and inline _asm blocks. No complete minimum CPU/RAM/OS configuration was established. Compiler architecture and recommended emulator are not proof of hardware compatibility.
- kens-labyrinth-original-dos / AI (no-evidence-found): No explicit AI-development claim found in inspected project documentation. This is unknown, not a negative determination.
- dos-defender / AI (no-evidence-found): No explicit AI-development claim found in inspected project documentation. This is unknown, not a negative determination.
- dungeons-of-noudar / AI (no-evidence-found): No explicit AI-development claim found in inspected project documentation. This is unknown, not a negative determination.
- plutonium-caverns / Runtime profiles (no-evidence-found): graphics.c uses dos.h/conio.h/graph.h,320x200 framebuffer, VGA memory/palette ports. README recommends DOSBox. No complete minimum CPU/RAM/OS configuration was established. Compiler architecture and recommended emulator are not proof of hardware compatibility.
- plutonium-caverns / AI (no-evidence-found): No explicit AI-development claim found in inspected project documentation. This is unknown, not a negative determination.
- gridfighter-3d / Runtime profiles (no-evidence-found): Native DOS plus QB64 source for Linux/Windows/macOS; modern builds described as untested. No complete minimum CPU/RAM/OS configuration was established. Compiler architecture and recommended emulator are not proof of hardware compatibility.
- gridfighter-3d / AI (no-evidence-found): No explicit AI-development claim found in inspected project documentation. This is unknown, not a negative determination.
- biomenace-decomp / Runtime profiles (no-evidence-found): Native DOS matching BMENACE1.EXE, original data required. No complete minimum CPU/RAM/OS configuration was established. Compiler architecture and recommended emulator are not proof of hardware compatibility.
- biomenace-decomp / AI (no-evidence-found): No explicit AI-development claim found in inspected project documentation. This is unknown, not a negative determination.
- catacomb-original-dos / Runtime profiles (no-evidence-found): Native DOS, CGA/EGA modules; CATACOMB.PAS is program Catacombs, uses DOS/CGA/EGA and gameplay object records. No complete minimum CPU/RAM/OS configuration was established. Compiler architecture and recommended emulator are not proof of hardware compatibility.
- catacomb-original-dos / AI (no-evidence-found): No explicit AI-development claim found in inspected project documentation. This is unknown, not a negative determination.
- catacomb-3d-original-dos / Runtime profiles (no-evidence-found): Native DOS; C3_MAIN.C implements original game state/memory pointers; assembly files present. No complete minimum CPU/RAM/OS configuration was established. Compiler architecture and recommended emulator are not proof of hardware compatibility.
- catacomb-3d-original-dos / AI (no-evidence-found): No explicit AI-development claim found in inspected project documentation. This is unknown, not a negative determination.
- keen-dreams-original-dos / Runtime profiles (no-evidence-found): Native DOS EGA/CGA versions; GRMODE and static dictionary/header objects select variant. kd_main.c identifies Keen Dreams / native game state. No complete minimum CPU/RAM/OS configuration was established. Compiler architecture and recommended emulator are not proof of hardware compatibility.
- keen-dreams-original-dos / AI (no-evidence-found): No explicit AI-development claim found in inspected project documentation. This is unknown, not a negative determination.
- hovertank-3d-original-dos / Runtime profiles (no-evidence-found): Native DOS. HOVMAIN.C contains sound/keyboard interrupt state and graphics segment structures. No complete minimum CPU/RAM/OS configuration was established. Compiler architecture and recommended emulator are not proof of hardware compatibility.
- hovertank-3d-original-dos / AI (no-evidence-found): No explicit AI-development claim found in inspected project documentation. This is unknown, not a negative determination.
- iron-seed-fpc / Runtime profiles (no-evidence-found): Upstream tested x86_64/i386 Linux. is.pas retains original 1994 Channel 7 and port contributor copyrights. No complete minimum CPU/RAM/OS configuration was established. Compiler architecture and recommended emulator are not proof of hardware compatibility.
- iron-seed-fpc / AI (no-evidence-found): No explicit AI-development claim found in inspected project documentation. This is unknown, not a negative determination.

## Raptor: Call of the Shadows — original DOS v1.2 sources

Project ID: dosraptor-original · Overall audit: reviewed

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
  "display_title": "Raptor: Call of the Shadows — original DOS v1.2 sources",
  "id": "dosraptor-original",
  "last_activity": "2024-03-22",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "x86 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/skynettx/dosraptor",
  "runtime_profiles": [],
  "source_cpu": [
    "x86"
  ],
  "source_language": [
    "C",
    "x86 assembly"
  ],
  "source_platforms": [
    "DOS"
  ],
  "status": "Source reviewed; independent build/play test not performed",
  "subjects": [
    "Raptor: Call of the Shadows"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "x86"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "DOS"
  ],
  "techniques": [],
  "title": "Raptor: Call of the Shadows — original DOS v1.2 sources",
  "tool_kinds": [],
  "types": [
    "original DOS source release"
  ],
  "upstream_name": "Raptor: Call of the Shadows — original DOS v1.2 sources",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

Original released game source with replacement sound integration.
- https://github.com/skynettx/dosraptor/blob/4403569505c215c6cebe02cc3344e670499def1d/README.md
- https://github.com/skynettx/dosraptor/blob/4403569505c215c6cebe02cc3344e670499def1d/SOURCE/RAP.C

### Classification (reviewed)

Preserved/released original DOS game source, not a newly inferred decompilation. Proprietary DMX replaced by Apogee Sound System plus APODMX; not pristine original or byte-identical. GPL 2+. Original game data needed.
- https://github.com/skynettx/dosraptor/blob/4403569505c215c6cebe02cc3344e670499def1d/README.md
- https://github.com/skynettx/dosraptor/blob/4403569505c215c6cebe02cc3344e670499def1d/SOURCE/RAP.C

### Source CPU (reviewed)

Original DOS x86 input lineage is established by the source release and build documentation.
- https://github.com/skynettx/dosraptor/blob/4403569505c215c6cebe02cc3344e670499def1d/README.md
- https://github.com/skynettx/dosraptor/blob/4403569505c215c6cebe02cc3344e670499def1d/SOURCE/RAP.C

### Target CPU (reviewed)

Native DOS x86 output is documented by the reviewed compiler/build and game source. DOSBox/browser packaging does not change the native game target.
- https://github.com/skynettx/dosraptor/blob/4403569505c215c6cebe02cc3344e670499def1d/README.md
- https://github.com/skynettx/dosraptor/blob/4403569505c215c6cebe02cc3344e670499def1d/SOURCE/RAP.C

### Build (reviewed)

DOS builds need Watcom C 10.0 and TASM 3.1; closer-match build uses Watcom C 9.5b for GFX and compatible C32 for APODMX. SOURCE/MAKEFILE uses wcc386, PROCESSOR=386, flat model, SYSTEM dos4g. Documentation/source inspection only; no toolchain build performed. Build/play/byte-exact flags remain unknown. 
- https://github.com/skynettx/dosraptor/blob/4403569505c215c6cebe02cc3344e670499def1d/README.md
- https://github.com/skynettx/dosraptor/blob/4403569505c215c6cebe02cc3344e670499def1d/SOURCE/RAP.C

### Runtime profiles (no-evidence-found)

Native 32-bit DOS protected-mode executable,386 flat DOS/4G. No complete minimum CPU/RAM/OS configuration was established. Compiler architecture and recommended emulator are not proof of hardware compatibility.
- https://github.com/skynettx/dosraptor/blob/4403569505c215c6cebe02cc3344e670499def1d/README.md
- https://github.com/skynettx/dosraptor/blob/4403569505c215c6cebe02cc3344e670499def1d/SOURCE/RAP.C

### AI (no-evidence-found)

No explicit AI-development claim found in inspected project documentation. This is unknown, not a negative determination.
- https://github.com/skynettx/dosraptor/blob/4403569505c215c6cebe02cc3344e670499def1d/README.md
- https://github.com/skynettx/dosraptor/blob/4403569505c215c6cebe02cc3344e670499def1d/SOURCE/RAP.C

### Relationships (reviewed)

Distinct from tracked RaybeezPL/raptor-amiga-port: original DOS code versus downstream Amiga platform port.
- https://github.com/skynettx/dosraptor/blob/4403569505c215c6cebe02cc3344e670499def1d/README.md
- https://github.com/skynettx/dosraptor/blob/4403569505c215c6cebe02cc3344e670499def1d/SOURCE/RAP.C

## Ken’s Labyrinth — preserved original DOS sources

Project ID: kens-labyrinth-original-dos · Overall audit: reviewed

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
  "display_title": "Ken’s Labyrinth — preserved original DOS sources",
  "id": "kens-labyrinth-original-dos",
  "last_activity": "2022-08-23",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "x86 inline assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/commercial-game-sources/kens_labyrinth",
  "runtime_profiles": [],
  "source_cpu": [
    "x86"
  ],
  "source_language": [
    "C",
    "x86 inline assembly"
  ],
  "source_platforms": [
    "DOS"
  ],
  "status": "Source reviewed; independent build/play test not performed",
  "subjects": [
    "Ken’s Labyrinth"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "x86"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "DOS"
  ],
  "techniques": [],
  "title": "Ken’s Labyrinth — preserved original DOS sources",
  "tool_kinds": [],
  "types": [
    "original DOS source release"
  ],
  "upstream_name": "Ken’s Labyrinth — preserved original DOS sources",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

Mirror of author-released Ken’s Labyrinth v2.1 full-version source.
- https://github.com/commercial-game-sources/kens_labyrinth/blob/452b72a5f2b88ffd856a2f4c320f25f7c4caab6c/README.md
- https://github.com/commercial-game-sources/kens_labyrinth/blob/452b72a5f2b88ffd856a2f4c320f25f7c4caab6c/README.TXT

### Classification (reviewed)

Preserved/released original DOS game source, not a newly inferred decompilation. Archived mirror. Noncommercial source license, not OSI open source. README warns digitized sound playback crashes machine.
- https://github.com/commercial-game-sources/kens_labyrinth/blob/452b72a5f2b88ffd856a2f4c320f25f7c4caab6c/README.md
- https://github.com/commercial-game-sources/kens_labyrinth/blob/452b72a5f2b88ffd856a2f4c320f25f7c4caab6c/README.TXT

### Source CPU (reviewed)

Original DOS x86 input lineage is established by the source release and build documentation.
- https://github.com/commercial-game-sources/kens_labyrinth/blob/452b72a5f2b88ffd856a2f4c320f25f7c4caab6c/README.md
- https://github.com/commercial-game-sources/kens_labyrinth/blob/452b72a5f2b88ffd856a2f4c320f25f7c4caab6c/README.TXT

### Target CPU (reviewed)

Native DOS x86 output is documented by the reviewed compiler/build and game source. DOSBox/browser packaging does not change the native game target.
- https://github.com/commercial-game-sources/kens_labyrinth/blob/452b72a5f2b88ffd856a2f4c320f25f7c4caab6c/README.md
- https://github.com/commercial-game-sources/kens_labyrinth/blob/452b72a5f2b88ffd856a2f4c320f25f7c4caab6c/README.TXT

### Build (reviewed)

README.TXT: Microsoft C 6.00A, the 1990 DOS compiler. MAKEFILE invokes cl /c /AM and link. Documentation/source inspection only; no toolchain build performed. Build/play/byte-exact flags remain unknown. 
- https://github.com/commercial-game-sources/kens_labyrinth/blob/452b72a5f2b88ffd856a2f4c320f25f7c4caab6c/README.md
- https://github.com/commercial-game-sources/kens_labyrinth/blob/452b72a5f2b88ffd856a2f4c320f25f7c4caab6c/README.TXT

### Runtime profiles (no-evidence-found)

Native 16-bit DOS; LAB3D.C contains main game loop and inline _asm blocks. No complete minimum CPU/RAM/OS configuration was established. Compiler architecture and recommended emulator are not proof of hardware compatibility.
- https://github.com/commercial-game-sources/kens_labyrinth/blob/452b72a5f2b88ffd856a2f4c320f25f7c4caab6c/README.md
- https://github.com/commercial-game-sources/kens_labyrinth/blob/452b72a5f2b88ffd856a2f4c320f25f7c4caab6c/README.TXT

### AI (no-evidence-found)

No explicit AI-development claim found in inspected project documentation. This is unknown, not a negative determination.
- https://github.com/commercial-game-sources/kens_labyrinth/blob/452b72a5f2b88ffd856a2f4c320f25f7c4caab6c/README.md
- https://github.com/commercial-game-sources/kens_labyrinth/blob/452b72a5f2b88ffd856a2f4c320f25f7c4caab6c/README.TXT

### Relationships (reviewed)

Preserved DOS original, distinct from lab3d-sdl source ports.
- https://github.com/commercial-game-sources/kens_labyrinth/blob/452b72a5f2b88ffd856a2f4c320f25f7c4caab6c/README.md
- https://github.com/commercial-game-sources/kens_labyrinth/blob/452b72a5f2b88ffd856a2f4c320f25f7c4caab6c/README.TXT

## DOS Defender — native DOS Ludum Dare shooter

Project ID: dos-defender · Overall audit: reviewed

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
  "display_title": "DOS Defender — native DOS Ludum Dare shooter",
  "id": "dos-defender",
  "last_activity": "2020-06-24",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "GNU C",
    "x86 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/skeeto/dosdefender-ld31",
  "runtime_profiles": [
    {
      "cpu_family": "x86",
      "evidence": [
        "https://github.com/skeeto/dosdefender-ld31/blob/f6242450425c530dcbba54d7937b6b1e23e29cd2/README.md",
        "https://github.com/skeeto/dosdefender-ld31/blob/f6242450425c530dcbba54d7937b6b1e23e29cd2/Makefile"
      ],
      "min_cpu": "80386",
      "name": "Documented DOS target",
      "notes": "Build uses -march=i386. Author describes real-mode COM requiring 64 KiB RAM and 64 KiB video memory, with DOSBox preferred; physical-PC compatibility was not independently tested.",
      "platform": "DOS"
    }
  ],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Source reviewed; independent build/play test not performed",
  "subjects": [
    "DOS Defender"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "x86"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "DOS"
  ],
  "techniques": [],
  "title": "DOS Defender — native DOS Ludum Dare shooter",
  "tool_kinds": [],
  "types": [
    "native DOS homebrew game"
  ],
  "upstream_name": "DOS Defender — native DOS Ludum Dare shooter",
  "work_kinds": []
}
```

### Identity (reviewed)

Original 2014 Ludum Dare 31 DOS homebrew.
- https://github.com/skeeto/dosdefender-ld31/blob/f6242450425c530dcbba54d7937b6b1e23e29cd2/README.md
- https://github.com/skeeto/dosdefender-ld31/blob/f6242450425c530dcbba54d7937b6b1e23e29cd2/Makefile

### Classification (reviewed)

New native DOS game, not reconstruction of an older executable. Not 8086: build requires i386 instruction set. No external assets. Unlicense.
- https://github.com/skeeto/dosdefender-ld31/blob/f6242450425c530dcbba54d7937b6b1e23e29cd2/README.md
- https://github.com/skeeto/dosdefender-ld31/blob/f6242450425c530dcbba54d7937b6b1e23e29cd2/Makefile

### Source CPU (not-applicable)

No predecessor executable is reconstructed; source platform/CPU are empty for this authored game.
- https://github.com/skeeto/dosdefender-ld31/blob/f6242450425c530dcbba54d7937b6b1e23e29cd2/README.md
- https://github.com/skeeto/dosdefender-ld31/blob/f6242450425c530dcbba54d7937b6b1e23e29cd2/Makefile

### Target CPU (reviewed)

Native DOS x86 output is documented by the reviewed compiler/build and game source. DOSBox/browser packaging does not change the native game target.
- https://github.com/skeeto/dosdefender-ld31/blob/f6242450425c530dcbba54d7937b6b1e23e29cd2/README.md
- https://github.com/skeeto/dosdefender-ld31/blob/f6242450425c530dcbba54d7937b6b1e23e29cd2/Makefile

### Build (reviewed)

README/Makefile: GCC i386 freestanding -m32 -march=i386; com.ld creates DOSDEF.COM. Documentation/source inspection only; no toolchain build performed. Build/play/byte-exact flags remain unknown. 
- https://github.com/skeeto/dosdefender-ld31/blob/f6242450425c530dcbba54d7937b6b1e23e29cd2/README.md
- https://github.com/skeeto/dosdefender-ld31/blob/f6242450425c530dcbba54d7937b6b1e23e29cd2/Makefile

### Runtime profiles (reviewed)

x86 real-mode; README64 kB RAM,64 kB video memory,10 kB executable. Preferred runtime DOSBox, should work to some extent on DOS. See documented configuration above; it is not an independently measured minimum.
- https://github.com/skeeto/dosdefender-ld31/blob/f6242450425c530dcbba54d7937b6b1e23e29cd2/README.md
- https://github.com/skeeto/dosdefender-ld31/blob/f6242450425c530dcbba54d7937b6b1e23e29cd2/Makefile

### AI (no-evidence-found)

No explicit AI-development claim found in inspected project documentation. This is unknown, not a negative determination.
- https://github.com/skeeto/dosdefender-ld31/blob/f6242450425c530dcbba54d7937b6b1e23e29cd2/README.md
- https://github.com/skeeto/dosdefender-ld31/blob/f6242450425c530dcbba54d7937b6b1e23e29cd2/Makefile

### Relationships (reviewed)

Original game, not an emulation wrapper.
- https://github.com/skeeto/dosdefender-ld31/blob/f6242450425c530dcbba54d7937b6b1e23e29cd2/README.md
- https://github.com/skeeto/dosdefender-ld31/blob/f6242450425c530dcbba54d7937b6b1e23e29cd2/Makefile

## Dungeons of Noudar — native DOS dungeon crawler

Project ID: dungeons-of-noudar · Overall audit: reviewed

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
  "display_title": "Dungeons of Noudar — native DOS dungeon crawler",
  "id": "dungeons-of-noudar",
  "last_activity": "2026-08-25",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "C++14",
    "C"
  ],
  "record_class": "subject",
  "repo": "https://github.com/TheFakeMontyOnTheRun/dungeons-of-noudar",
  "runtime_profiles": [
    {
      "cpu_family": "x86",
      "evidence": [
        "https://github.com/TheFakeMontyOnTheRun/dungeons-of-noudar/blob/03e94de322613c80fca748e8eb5426de59b993d4/README.md",
        "https://github.com/TheFakeMontyOnTheRun/dungeons-of-noudar/blob/03e94de322613c80fca748e8eb5426de59b993d4/DungeonsOfNoudar486/Makefile"
      ],
      "name": "Author-tested configuration",
      "notes": "Author tested 486SX-33 with 8 MiB RAM; current Makefile selects -march=i486. Reports of 386 execution are not established compatibility. VGA and AdLib/PC-speaker/OPL2LPT are documented.",
      "platform": "DOS"
    }
  ],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Source reviewed; independent build/play test not performed",
  "subjects": [
    "Dungeons of Noudar"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "x86"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "DOS"
  ],
  "techniques": [],
  "title": "Dungeons of Noudar — native DOS dungeon crawler",
  "tool_kinds": [],
  "types": [
    "native DOS homebrew game"
  ],
  "upstream_name": "Dungeons of Noudar — native DOS dungeon crawler",
  "work_kinds": []
}
```

### Identity (reviewed)

New 2.5D first-person dungeon crawler for MS-DOS/FreeDOS.
- https://github.com/TheFakeMontyOnTheRun/dungeons-of-noudar/blob/03e94de322613c80fca748e8eb5426de59b993d4/README.md
- https://github.com/TheFakeMontyOnTheRun/dungeons-of-noudar/blob/03e94de322613c80fca748e8eb5426de59b993d4/DungeonsOfNoudar486/Makefile

### Classification (reviewed)

New native DOS game, not reconstruction of an older executable. Fetch submodules. Historical V2 Android/iOS/macOS/LibRetro not current supported mainline. BSD 2.
- https://github.com/TheFakeMontyOnTheRun/dungeons-of-noudar/blob/03e94de322613c80fca748e8eb5426de59b993d4/README.md
- https://github.com/TheFakeMontyOnTheRun/dungeons-of-noudar/blob/03e94de322613c80fca748e8eb5426de59b993d4/DungeonsOfNoudar486/Makefile

### Source CPU (not-applicable)

No predecessor executable is reconstructed; source platform/CPU are empty for this authored game.
- https://github.com/TheFakeMontyOnTheRun/dungeons-of-noudar/blob/03e94de322613c80fca748e8eb5426de59b993d4/README.md
- https://github.com/TheFakeMontyOnTheRun/dungeons-of-noudar/blob/03e94de322613c80fca748e8eb5426de59b993d4/DungeonsOfNoudar486/Makefile

### Target CPU (reviewed)

Native DOS x86 output is documented by the reviewed compiler/build and game source. DOSBox/browser packaging does not change the native game target.
- https://github.com/TheFakeMontyOnTheRun/dungeons-of-noudar/blob/03e94de322613c80fca748e8eb5426de59b993d4/README.md
- https://github.com/TheFakeMontyOnTheRun/dungeons-of-noudar/blob/03e94de322613c80fca748e8eb5426de59b993d4/DungeonsOfNoudar486/Makefile

### Build (reviewed)

Recursive submodules and modern DJGPP; cd DungeonsOfNoudar486 && make builds DOS executable/data. Makefile invokes i386-pc-msdosdjgpp-g++. Documentation/source inspection only; no toolchain build performed. Build/play/byte-exact flags remain unknown. 
- https://github.com/TheFakeMontyOnTheRun/dungeons-of-noudar/blob/03e94de322613c80fca748e8eb5426de59b993d4/README.md
- https://github.com/TheFakeMontyOnTheRun/dungeons-of-noudar/blob/03e94de322613c80fca748e8eb5426de59b993d4/DungeonsOfNoudar486/Makefile

### Runtime profiles (reviewed)

Protected-mode VGA; author tested 486SX-33 MHz with 8 MB.386 reports unverified. AdLib, PC speaker, OPL2LPT. main.cpp uses DJGPP dpmi/go32/pc/bios headers. See documented configuration above; it is not an independently measured minimum.
- https://github.com/TheFakeMontyOnTheRun/dungeons-of-noudar/blob/03e94de322613c80fca748e8eb5426de59b993d4/README.md
- https://github.com/TheFakeMontyOnTheRun/dungeons-of-noudar/blob/03e94de322613c80fca748e8eb5426de59b993d4/DungeonsOfNoudar486/Makefile

### AI (no-evidence-found)

No explicit AI-development claim found in inspected project documentation. This is unknown, not a negative determination.
- https://github.com/TheFakeMontyOnTheRun/dungeons-of-noudar/blob/03e94de322613c80fca748e8eb5426de59b993d4/README.md
- https://github.com/TheFakeMontyOnTheRun/dungeons-of-noudar/blob/03e94de322613c80fca748e8eb5426de59b993d4/DungeonsOfNoudar486/Makefile

### Relationships (reviewed)

Started as AndroidVR game; mainline is native DOS, internal SDL2 version for testing/development.
- https://github.com/TheFakeMontyOnTheRun/dungeons-of-noudar/blob/03e94de322613c80fca748e8eb5426de59b993d4/README.md
- https://github.com/TheFakeMontyOnTheRun/dungeons-of-noudar/blob/03e94de322613c80fca748e8eb5426de59b993d4/DungeonsOfNoudar486/Makefile

## Plutonium Caverns — native DOS puzzle game

Project ID: plutonium-caverns · Overall audit: reviewed

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
  "display_title": "Plutonium Caverns — native DOS puzzle game",
  "id": "plutonium-caverns",
  "last_activity": "2019-06-08",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "C"
  ],
  "record_class": "subject",
  "repo": "https://github.com/jani-nykanen/plutonium-caverns",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Source reviewed; independent build/play test not performed",
  "subjects": [
    "Plutonium Caverns"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "x86"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "DOS"
  ],
  "techniques": [],
  "title": "Plutonium Caverns — native DOS puzzle game",
  "tool_kinds": [],
  "types": [
    "native DOS homebrew game"
  ],
  "upstream_name": "Plutonium Caverns — native DOS puzzle game",
  "work_kinds": []
}
```

### Identity (reviewed)

Original 2019 MS-DOS puzzle homebrew.
- https://github.com/jani-nykanen/plutonium-caverns/blob/7fb3ffec8a32502688b2b52429cbe2da8e90435c/README.md
- https://github.com/jani-nykanen/plutonium-caverns/blob/7fb3ffec8a32502688b2b52429cbe2da8e90435c/src/core/graphics.c

### Classification (reviewed)

New native DOS game, not reconstruction of an older executable. README informally specifies LGPL code; assets reserved for author except font. No complete scripted build instructions.
- https://github.com/jani-nykanen/plutonium-caverns/blob/7fb3ffec8a32502688b2b52429cbe2da8e90435c/README.md
- https://github.com/jani-nykanen/plutonium-caverns/blob/7fb3ffec8a32502688b2b52429cbe2da8e90435c/src/core/graphics.c

### Source CPU (not-applicable)

No predecessor executable is reconstructed; source platform/CPU are empty for this authored game.
- https://github.com/jani-nykanen/plutonium-caverns/blob/7fb3ffec8a32502688b2b52429cbe2da8e90435c/README.md
- https://github.com/jani-nykanen/plutonium-caverns/blob/7fb3ffec8a32502688b2b52429cbe2da8e90435c/src/core/graphics.c

### Target CPU (reviewed)

Native DOS x86 output is documented by the reviewed compiler/build and game source. DOSBox/browser packaging does not change the native game target.
- https://github.com/jani-nykanen/plutonium-caverns/blob/7fb3ffec8a32502688b2b52429cbe2da8e90435c/README.md
- https://github.com/jani-nykanen/plutonium-caverns/blob/7fb3ffec8a32502688b2b52429cbe2da8e90435c/src/core/graphics.c

### Build (reviewed)

README: OpenWatcom, add all .c files to project and build. Documentation/source inspection only; no toolchain build performed. Build/play/byte-exact flags remain unknown. 
- https://github.com/jani-nykanen/plutonium-caverns/blob/7fb3ffec8a32502688b2b52429cbe2da8e90435c/README.md
- https://github.com/jani-nykanen/plutonium-caverns/blob/7fb3ffec8a32502688b2b52429cbe2da8e90435c/src/core/graphics.c

### Runtime profiles (no-evidence-found)

graphics.c uses dos.h/conio.h/graph.h,320x200 framebuffer, VGA memory/palette ports. README recommends DOSBox. No complete minimum CPU/RAM/OS configuration was established. Compiler architecture and recommended emulator are not proof of hardware compatibility.
- https://github.com/jani-nykanen/plutonium-caverns/blob/7fb3ffec8a32502688b2b52429cbe2da8e90435c/README.md
- https://github.com/jani-nykanen/plutonium-caverns/blob/7fb3ffec8a32502688b2b52429cbe2da8e90435c/src/core/graphics.c

### AI (no-evidence-found)

No explicit AI-development claim found in inspected project documentation. This is unknown, not a negative determination.
- https://github.com/jani-nykanen/plutonium-caverns/blob/7fb3ffec8a32502688b2b52429cbe2da8e90435c/README.md
- https://github.com/jani-nykanen/plutonium-caverns/blob/7fb3ffec8a32502688b2b52429cbe2da8e90435c/src/core/graphics.c

### Relationships (reviewed)

html5 directory packages DOSBox; main source compiles native DOS.
- https://github.com/jani-nykanen/plutonium-caverns/blob/7fb3ffec8a32502688b2b52429cbe2da8e90435c/README.md
- https://github.com/jani-nykanen/plutonium-caverns/blob/7fb3ffec8a32502688b2b52429cbe2da8e90435c/src/core/graphics.c

## Gridfighter 3D — QuickBASIC DOS arcade game

Project ID: gridfighter-3d · Overall audit: reviewed

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
  "display_title": "Gridfighter 3D — QuickBASIC DOS arcade game",
  "id": "gridfighter-3d",
  "last_activity": "2019-01-19",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "QuickBASIC",
    "QB64 BASIC"
  ],
  "record_class": "subject",
  "repo": "https://github.com/porta2note/gridfighter3d",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Source reviewed; independent build/play test not performed",
  "subjects": [
    "Gridfighter 3D"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "x86"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "DOS",
    "Linux",
    "Windows",
    "macOS"
  ],
  "techniques": [],
  "title": "Gridfighter 3D — QuickBASIC DOS arcade game",
  "tool_kinds": [],
  "types": [
    "native DOS homebrew game"
  ],
  "upstream_name": "Gridfighter 3D — QuickBASIC DOS arcade game",
  "work_kinds": []
}
```

### Identity (reviewed)

Official source release of Jay Hammer’s2017-onward arcade/VR game.
- https://github.com/porta2note/gridfighter3d/blob/155596b21c3eff30738f3be3081ff33d70658701/README.md
- https://github.com/porta2note/gridfighter3d/blob/155596b21c3eff30738f3be3081ff33d70658701/GRID3D24.BAS

### Classification (reviewed)

New native DOS game, not reconstruction of an older executable. Source 0x24 corresponds game v1.3. GPL 3 source; source header separately labels author-prebuilt binaries CC-BY-NC.
- https://github.com/porta2note/gridfighter3d/blob/155596b21c3eff30738f3be3081ff33d70658701/README.md
- https://github.com/porta2note/gridfighter3d/blob/155596b21c3eff30738f3be3081ff33d70658701/GRID3D24.BAS

### Source CPU (not-applicable)

No predecessor executable is reconstructed; source platform/CPU are empty for this authored game.
- https://github.com/porta2note/gridfighter3d/blob/155596b21c3eff30738f3be3081ff33d70658701/README.md
- https://github.com/porta2note/gridfighter3d/blob/155596b21c3eff30738f3be3081ff33d70658701/GRID3D24.BAS

### Target CPU (reviewed)

Native DOS x86 output is documented by the reviewed compiler/build and game source. Separate QB64 modern desktop sources are documented as untested; no additional CPU architecture is inferred.
- https://github.com/porta2note/gridfighter3d/blob/155596b21c3eff30738f3be3081ff33d70658701/README.md
- https://github.com/porta2note/gridfighter3d/blob/155596b21c3eff30738f3be3081ff33d70658701/GRID3D24.BAS

### Build (reviewed)

Microsoft QuickBASIC 4.5 for DOS, no extra libraries; separate QB64 source for modern OSes. Documentation/source inspection only; no toolchain build performed. Build/play/byte-exact flags remain unknown. 
- https://github.com/porta2note/gridfighter3d/blob/155596b21c3eff30738f3be3081ff33d70658701/README.md
- https://github.com/porta2note/gridfighter3d/blob/155596b21c3eff30738f3be3081ff33d70658701/GRID3D24.BAS

### Runtime profiles (no-evidence-found)

Native DOS plus QB64 source for Linux/Windows/macOS; modern builds described as untested. No complete minimum CPU/RAM/OS configuration was established. Compiler architecture and recommended emulator are not proof of hardware compatibility.
- https://github.com/porta2note/gridfighter3d/blob/155596b21c3eff30738f3be3081ff33d70658701/README.md
- https://github.com/porta2note/gridfighter3d/blob/155596b21c3eff30738f3be3081ff33d70658701/GRID3D24.BAS

### AI (no-evidence-found)

No explicit AI-development claim found in inspected project documentation. This is unknown, not a negative determination.
- https://github.com/porta2note/gridfighter3d/blob/155596b21c3eff30738f3be3081ff33d70658701/README.md
- https://github.com/porta2note/gridfighter3d/blob/155596b21c3eff30738f3be3081ff33d70658701/GRID3D24.BAS

### Relationships (reviewed)

DOS/QB64 variants differ timing/vsync/file I/O, not emulation wrapper.
- https://github.com/porta2note/gridfighter3d/blob/155596b21c3eff30738f3be3081ff33d70658701/README.md
- https://github.com/porta2note/gridfighter3d/blob/155596b21c3eff30738f3be3081ff33d70658701/GRID3D24.BAS

## BioMenace — matching DOS episode-one reconstruction

Project ID: biomenace-decomp · Overall audit: reviewed

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
  "display_title": "BioMenace — matching DOS episode-one reconstruction",
  "id": "biomenace-decomp",
  "last_activity": "2024-12-27",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "x86 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/lethal-guitar/BioMenaceDecomp",
  "runtime_profiles": [],
  "source_cpu": [
    "x86"
  ],
  "source_language": [
    "x86 machine code"
  ],
  "source_platforms": [
    "DOS"
  ],
  "status": "Source reviewed; independent build/play test not performed",
  "subjects": [
    "BioMenace"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "x86"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "DOS"
  ],
  "techniques": [],
  "title": "BioMenace — matching DOS episode-one reconstruction",
  "tool_kinds": [],
  "types": [
    "DOS game reconstruction"
  ],
  "upstream_name": "BioMenace — matching DOS episode-one reconstruction",
  "work_kinds": [
    "decompilation",
    "source-reconstruction"
  ]
}
```

### Identity (reviewed)

Decompilation/source reconstruction of Bio Menace episode 1.
- https://github.com/lethal-guitar/BioMenaceDecomp/blob/4471bcfc03ff2ebe10620011fa45e9a1d086c841/README.md
- https://github.com/lethal-guitar/BioMenaceDecomp/blob/4471bcfc03ff2ebe10620011fa45e9a1d086c841/SRC/BM_MAIN.C

### Classification (reviewed)

Binary-derived reconstruction. Only episode 1 here; matching is upstream claim, not reproduced locally. GPL 2.
- https://github.com/lethal-guitar/BioMenaceDecomp/blob/4471bcfc03ff2ebe10620011fa45e9a1d086c841/README.md
- https://github.com/lethal-guitar/BioMenaceDecomp/blob/4471bcfc03ff2ebe10620011fa45e9a1d086c841/SRC/BM_MAIN.C

### Source CPU (reviewed)

Original DOS x86 input lineage is established by the source release and build documentation.
- https://github.com/lethal-guitar/BioMenaceDecomp/blob/4471bcfc03ff2ebe10620011fa45e9a1d086c841/README.md
- https://github.com/lethal-guitar/BioMenaceDecomp/blob/4471bcfc03ff2ebe10620011fa45e9a1d086c841/SRC/BM_MAIN.C

### Target CPU (reviewed)

Native DOS x86 output is documented by the reviewed compiler/build and game source. DOSBox/browser packaging does not change the native game target.
- https://github.com/lethal-guitar/BioMenaceDecomp/blob/4471bcfc03ff2ebe10620011fa45e9a1d086c841/README.md
- https://github.com/lethal-guitar/BioMenaceDecomp/blob/4471bcfc03ff2ebe10620011fa45e9a1d086c841/SRC/BM_MAIN.C

### Build (reviewed)

Borland C++ 2.0 in DOS, make, then LZEXE compression. README claims identical freeware/shareware v1.1 binaries. SRC/MAKEFILE invokes BCC/TLINK/TASM, targets BMENACE1.EXE. Documentation/source inspection only; no toolchain build performed. Build/play/byte-exact flags remain unknown. The identical-binary result is an upstream claim for episode one only, not reproduced in this pass.
- https://github.com/lethal-guitar/BioMenaceDecomp/blob/4471bcfc03ff2ebe10620011fa45e9a1d086c841/README.md
- https://github.com/lethal-guitar/BioMenaceDecomp/blob/4471bcfc03ff2ebe10620011fa45e9a1d086c841/SRC/BM_MAIN.C

### Runtime profiles (no-evidence-found)

Native DOS matching BMENACE1.EXE, original data required. No complete minimum CPU/RAM/OS configuration was established. Compiler architecture and recommended emulator are not proof of hardware compatibility.
- https://github.com/lethal-guitar/BioMenaceDecomp/blob/4471bcfc03ff2ebe10620011fa45e9a1d086c841/README.md
- https://github.com/lethal-guitar/BioMenaceDecomp/blob/4471bcfc03ff2ebe10620011fa45e9a1d086c841/SRC/BM_MAIN.C

### AI (no-evidence-found)

No explicit AI-development claim found in inspected project documentation. This is unknown, not a negative determination.
- https://github.com/lethal-guitar/BioMenaceDecomp/blob/4471bcfc03ff2ebe10620011fa45e9a1d086c841/README.md
- https://github.com/lethal-guitar/BioMenaceDecomp/blob/4471bcfc03ff2ebe10620011fa45e9a1d086c841/SRC/BM_MAIN.C

### Relationships (reviewed)

Based on K1n9_Duk3 Keen 4 reconstruction; README points to separate K1n9_Duk3 all 3 episodes reconstruction.
- https://github.com/lethal-guitar/BioMenaceDecomp/blob/4471bcfc03ff2ebe10620011fa45e9a1d086c841/README.md
- https://github.com/lethal-guitar/BioMenaceDecomp/blob/4471bcfc03ff2ebe10620011fa45e9a1d086c841/SRC/BM_MAIN.C

## Catacomb — original Turbo Pascal DOS sources

Project ID: catacomb-original-dos · Overall audit: reviewed

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
  "display_title": "Catacomb — original Turbo Pascal DOS sources",
  "id": "catacomb-original-dos",
  "last_activity": "2014-06-05",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "Turbo Pascal",
    "x86 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/CatacombGames/Catacomb",
  "runtime_profiles": [],
  "source_cpu": [
    "x86"
  ],
  "source_language": [
    "Turbo Pascal",
    "x86 assembly"
  ],
  "source_platforms": [
    "DOS"
  ],
  "status": "Source reviewed; independent build/play test not performed",
  "subjects": [
    "Catacomb"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "x86"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "DOS"
  ],
  "techniques": [],
  "title": "Catacomb — original Turbo Pascal DOS sources",
  "tool_kinds": [],
  "types": [
    "original DOS source release"
  ],
  "upstream_name": "Catacomb — original Turbo Pascal DOS sources",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

Original released source for 2D Catacomb.
- https://github.com/CatacombGames/Catacomb/blob/e657bc3aa8fef0d89bd09aa8fa0e051941c66518/README.md
- https://github.com/CatacombGames/Catacomb/blob/e657bc3aa8fef0d89bd09aa8fa0e051941c66518/MAKECAT.BAT

### Classification (reviewed)

Preserved/released original DOS game source, not a newly inferred decompilation. GPL 2 code; data/embedded OBJ retain nonfree terms with linking exception. Editor requires uncompressed levels.
- https://github.com/CatacombGames/Catacomb/blob/e657bc3aa8fef0d89bd09aa8fa0e051941c66518/README.md
- https://github.com/CatacombGames/Catacomb/blob/e657bc3aa8fef0d89bd09aa8fa0e051941c66518/MAKECAT.BAT

### Source CPU (reviewed)

Original DOS x86 input lineage is established by the source release and build documentation.
- https://github.com/CatacombGames/Catacomb/blob/e657bc3aa8fef0d89bd09aa8fa0e051941c66518/README.md
- https://github.com/CatacombGames/Catacomb/blob/e657bc3aa8fef0d89bd09aa8fa0e051941c66518/MAKECAT.BAT

### Target CPU (reviewed)

Native DOS x86 output is documented by the reviewed compiler/build and game source. DOSBox/browser packaging does not change the native game target.
- https://github.com/CatacombGames/Catacomb/blob/e657bc3aa8fef0d89bd09aa8fa0e051941c66518/README.md
- https://github.com/CatacombGames/Catacomb/blob/e657bc3aa8fef0d89bd09aa8fa0e051941c66518/MAKECAT.BAT

### Build (reviewed)

Turbo Pascal 5.5; MAKECAT.BAT invokes tasm catasm, tasm soundlib, tpc -b catacomb. Documentation/source inspection only; no toolchain build performed. Build/play/byte-exact flags remain unknown. 
- https://github.com/CatacombGames/Catacomb/blob/e657bc3aa8fef0d89bd09aa8fa0e051941c66518/README.md
- https://github.com/CatacombGames/Catacomb/blob/e657bc3aa8fef0d89bd09aa8fa0e051941c66518/MAKECAT.BAT

### Runtime profiles (no-evidence-found)

Native DOS, CGA/EGA modules; CATACOMB.PAS is program Catacombs, uses DOS/CGA/EGA and gameplay object records. No complete minimum CPU/RAM/OS configuration was established. Compiler architecture and recommended emulator are not proof of hardware compatibility.
- https://github.com/CatacombGames/Catacomb/blob/e657bc3aa8fef0d89bd09aa8fa0e051941c66518/README.md
- https://github.com/CatacombGames/Catacomb/blob/e657bc3aa8fef0d89bd09aa8fa0e051941c66518/MAKECAT.BAT

### AI (no-evidence-found)

No explicit AI-development claim found in inspected project documentation. This is unknown, not a negative determination.
- https://github.com/CatacombGames/Catacomb/blob/e657bc3aa8fef0d89bd09aa8fa0e051941c66518/README.md
- https://github.com/CatacombGames/Catacomb/blob/e657bc3aa8fef0d89bd09aa8fa0e051941c66518/MAKECAT.BAT

### Relationships (reviewed)

Distinct 2D game from Catacomb3D and The Catacomb/CatacombII.
- https://github.com/CatacombGames/Catacomb/blob/e657bc3aa8fef0d89bd09aa8fa0e051941c66518/README.md
- https://github.com/CatacombGames/Catacomb/blob/e657bc3aa8fef0d89bd09aa8fa0e051941c66518/MAKECAT.BAT

## Catacomb 3-D: The Descent — original DOS sources

Project ID: catacomb-3d-original-dos · Overall audit: reviewed

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
  "display_title": "Catacomb 3-D: The Descent — original DOS sources",
  "id": "catacomb-3d-original-dos",
  "last_activity": "2014-06-05",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "x86 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/CatacombGames/Catacomb3D",
  "runtime_profiles": [],
  "source_cpu": [
    "x86"
  ],
  "source_language": [
    "C",
    "x86 assembly"
  ],
  "source_platforms": [
    "DOS"
  ],
  "status": "Source reviewed; independent build/play test not performed",
  "subjects": [
    "Catacomb 3-D: The Descent"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "x86"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "DOS"
  ],
  "techniques": [],
  "title": "Catacomb 3-D: The Descent — original DOS sources",
  "tool_kinds": [],
  "types": [
    "original DOS source release"
  ],
  "upstream_name": "Catacomb 3-D: The Descent — original DOS sources",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

Original released source for Catacomb3-D aka Catacombs 3/A New Dimension.
- https://github.com/CatacombGames/Catacomb3D/blob/aa97f4995dc7dbea3ecc1794a2d4d4354839cad4/README.md
- https://github.com/CatacombGames/Catacomb3D/blob/aa97f4995dc7dbea3ecc1794a2d4d4354839cad4/CAT3D.PRJ

### Classification (reviewed)

Preserved/released original DOS game source, not a newly inferred decompilation. GPL 2 source; legally acquired game data required. GitHub language classifier C++ does not accurately distinguish historical C.
- https://github.com/CatacombGames/Catacomb3D/blob/aa97f4995dc7dbea3ecc1794a2d4d4354839cad4/README.md
- https://github.com/CatacombGames/Catacomb3D/blob/aa97f4995dc7dbea3ecc1794a2d4d4354839cad4/CAT3D.PRJ

### Source CPU (reviewed)

Original DOS x86 input lineage is established by the source release and build documentation.
- https://github.com/CatacombGames/Catacomb3D/blob/aa97f4995dc7dbea3ecc1794a2d4d4354839cad4/README.md
- https://github.com/CatacombGames/Catacomb3D/blob/aa97f4995dc7dbea3ecc1794a2d4d4354839cad4/CAT3D.PRJ

### Target CPU (reviewed)

Native DOS x86 output is documented by the reviewed compiler/build and game source. DOSBox/browser packaging does not change the native game target.
- https://github.com/CatacombGames/Catacomb3D/blob/aa97f4995dc7dbea3ecc1794a2d4d4354839cad4/README.md
- https://github.com/CatacombGames/Catacomb3D/blob/aa97f4995dc7dbea3ecc1794a2d4d4354839cad4/CAT3D.PRJ

### Build (reviewed)

Designed Borland C++ 2.0, compiled with 3.1 at release. CAT3D.PRJ present. Documentation/source inspection only; no toolchain build performed. Build/play/byte-exact flags remain unknown. 
- https://github.com/CatacombGames/Catacomb3D/blob/aa97f4995dc7dbea3ecc1794a2d4d4354839cad4/README.md
- https://github.com/CatacombGames/Catacomb3D/blob/aa97f4995dc7dbea3ecc1794a2d4d4354839cad4/CAT3D.PRJ

### Runtime profiles (no-evidence-found)

Native DOS; C3_MAIN.C implements original game state/memory pointers; assembly files present. No complete minimum CPU/RAM/OS configuration was established. Compiler architecture and recommended emulator are not proof of hardware compatibility.
- https://github.com/CatacombGames/Catacomb3D/blob/aa97f4995dc7dbea3ecc1794a2d4d4354839cad4/README.md
- https://github.com/CatacombGames/Catacomb3D/blob/aa97f4995dc7dbea3ecc1794a2d4d4354839cad4/CAT3D.PRJ

### AI (no-evidence-found)

No explicit AI-development claim found in inspected project documentation. This is unknown, not a negative determination.
- https://github.com/CatacombGames/Catacomb3D/blob/aa97f4995dc7dbea3ecc1794a2d4d4354839cad4/README.md
- https://github.com/CatacombGames/Catacomb3D/blob/aa97f4995dc7dbea3ecc1794a2d4d4354839cad4/CAT3D.PRJ

### Relationships (reviewed)

Distinct from 2D Catacomb and later Catacomb Adventure trilogy.
- https://github.com/CatacombGames/Catacomb3D/blob/aa97f4995dc7dbea3ecc1794a2d4d4354839cad4/README.md
- https://github.com/CatacombGames/Catacomb3D/blob/aa97f4995dc7dbea3ecc1794a2d4d4354839cad4/CAT3D.PRJ

## Commander Keen in Keen Dreams — original DOS source release

Project ID: keen-dreams-original-dos · Overall audit: reviewed

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
  "display_title": "Commander Keen in Keen Dreams — original DOS source release",
  "id": "keen-dreams-original-dos",
  "last_activity": "2014-11-12",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "x86 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/keendreams/keen",
  "runtime_profiles": [],
  "source_cpu": [
    "x86"
  ],
  "source_language": [
    "C",
    "x86 assembly"
  ],
  "source_platforms": [
    "DOS"
  ],
  "status": "Source reviewed; independent build/play test not performed",
  "subjects": [
    "Commander Keen in Keen Dreams"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "x86"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "DOS"
  ],
  "techniques": [],
  "title": "Commander Keen in Keen Dreams — original DOS source release",
  "tool_kinds": [],
  "types": [
    "original DOS source release"
  ],
  "upstream_name": "Commander Keen in Keen Dreams — original DOS source release",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

Crowdfunding-enabled original game source release.
- https://github.com/keendreams/keen/blob/4348b4719be87a0b873f5f4f77b4de82ddf7050c/README.md
- https://github.com/keendreams/keen/blob/4348b4719be87a0b873f5f4f77b4de82ddf7050c/kdreams.prj

### Classification (reviewed)

Preserved/released original DOS game source, not a newly inferred decompilation. GPL 2+ source; game/static data retain original license and must be legally acquired.
- https://github.com/keendreams/keen/blob/4348b4719be87a0b873f5f4f77b4de82ddf7050c/README.md
- https://github.com/keendreams/keen/blob/4348b4719be87a0b873f5f4f77b4de82ddf7050c/kdreams.prj

### Source CPU (reviewed)

Original DOS x86 input lineage is established by the source release and build documentation.
- https://github.com/keendreams/keen/blob/4348b4719be87a0b873f5f4f77b4de82ddf7050c/README.md
- https://github.com/keendreams/keen/blob/4348b4719be87a0b873f5f4f77b4de82ddf7050c/kdreams.prj

### Target CPU (reviewed)

Native DOS x86 output is documented by the reviewed compiler/build and game source. DOSBox/browser packaging does not change the native game target.
- https://github.com/keendreams/keen/blob/4348b4719be87a0b873f5f4f77b4de82ddf7050c/README.md
- https://github.com/keendreams/keen/blob/4348b4719be87a0b873f5f4f77b4de82ddf7050c/kdreams.prj

### Build (reviewed)

Borland C++ 2.0, revisions built with 3.1; static/make.bat invokes bcc makeobj.c and converts static data to OBJ, then root project opened in bc. Documentation/source inspection only; no toolchain build performed. Build/play/byte-exact flags remain unknown. 
- https://github.com/keendreams/keen/blob/4348b4719be87a0b873f5f4f77b4de82ddf7050c/README.md
- https://github.com/keendreams/keen/blob/4348b4719be87a0b873f5f4f77b4de82ddf7050c/kdreams.prj

### Runtime profiles (no-evidence-found)

Native DOS EGA/CGA versions; GRMODE and static dictionary/header objects select variant. kd_main.c identifies Keen Dreams / native game state. No complete minimum CPU/RAM/OS configuration was established. Compiler architecture and recommended emulator are not proof of hardware compatibility.
- https://github.com/keendreams/keen/blob/4348b4719be87a0b873f5f4f77b4de82ddf7050c/README.md
- https://github.com/keendreams/keen/blob/4348b4719be87a0b873f5f4f77b4de82ddf7050c/kdreams.prj

### AI (no-evidence-found)

No explicit AI-development claim found in inspected project documentation. This is unknown, not a negative determination.
- https://github.com/keendreams/keen/blob/4348b4719be87a0b873f5f4f77b4de82ddf7050c/README.md
- https://github.com/keendreams/keen/blob/4348b4719be87a0b873f5f4f77b4de82ddf7050c/kdreams.prj

### Relationships (reviewed)

Distinct from tracked Omnispeak, Keen 4–6. Original native game, not source port.
- https://github.com/keendreams/keen/blob/4348b4719be87a0b873f5f4f77b4de82ddf7050c/README.md
- https://github.com/keendreams/keen/blob/4348b4719be87a0b873f5f4f77b4de82ddf7050c/kdreams.prj

## Hovertank 3-D — original DOS source release

Project ID: hovertank-3d-original-dos · Overall audit: reviewed

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
  "display_title": "Hovertank 3-D — original DOS source release",
  "id": "hovertank-3d-original-dos",
  "last_activity": "2014-06-04",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "x86 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/FlatRockSoft/Hovertank3D",
  "runtime_profiles": [],
  "source_cpu": [
    "x86"
  ],
  "source_language": [
    "C",
    "x86 assembly"
  ],
  "source_platforms": [
    "DOS"
  ],
  "status": "Source reviewed; independent build/play test not performed",
  "subjects": [
    "Hovertank 3-D"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "x86"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "DOS"
  ],
  "techniques": [],
  "title": "Hovertank 3-D — original DOS source release",
  "tool_kinds": [],
  "types": [
    "original DOS source release"
  ],
  "upstream_name": "Hovertank 3-D — original DOS source release",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

Original GPL release of Hovertank3D source.
- https://github.com/FlatRockSoft/Hovertank3D/blob/86f6b5ed34c52d2ca8acbb26391ebd5b2542f1fa/README
- https://github.com/FlatRockSoft/Hovertank3D/blob/86f6b5ed34c52d2ca8acbb26391ebd5b2542f1fa/HOVER.PRJ

### Classification (reviewed)

Preserved/released original DOS game source, not a newly inferred decompilation. GPL 2 source; original game data required. GitHub labels historical C sources as C++.
- https://github.com/FlatRockSoft/Hovertank3D/blob/86f6b5ed34c52d2ca8acbb26391ebd5b2542f1fa/README
- https://github.com/FlatRockSoft/Hovertank3D/blob/86f6b5ed34c52d2ca8acbb26391ebd5b2542f1fa/HOVER.PRJ

### Source CPU (reviewed)

Original DOS x86 input lineage is established by the source release and build documentation.
- https://github.com/FlatRockSoft/Hovertank3D/blob/86f6b5ed34c52d2ca8acbb26391ebd5b2542f1fa/README
- https://github.com/FlatRockSoft/Hovertank3D/blob/86f6b5ed34c52d2ca8acbb26391ebd5b2542f1fa/HOVER.PRJ

### Target CPU (reviewed)

Native DOS x86 output is documented by the reviewed compiler/build and game source. DOSBox/browser packaging does not change the native game target.
- https://github.com/FlatRockSoft/Hovertank3D/blob/86f6b5ed34c52d2ca8acbb26391ebd5b2542f1fa/README
- https://github.com/FlatRockSoft/Hovertank3D/blob/86f6b5ed34c52d2ca8acbb26391ebd5b2542f1fa/HOVER.PRJ

### Build (reviewed)

Borland C++ 2.0 design, compiled under 3.1 at release; HOVER.PRJ present. Documentation/source inspection only; no toolchain build performed. Build/play/byte-exact flags remain unknown. 
- https://github.com/FlatRockSoft/Hovertank3D/blob/86f6b5ed34c52d2ca8acbb26391ebd5b2542f1fa/README
- https://github.com/FlatRockSoft/Hovertank3D/blob/86f6b5ed34c52d2ca8acbb26391ebd5b2542f1fa/HOVER.PRJ

### Runtime profiles (no-evidence-found)

Native DOS. HOVMAIN.C contains sound/keyboard interrupt state and graphics segment structures. No complete minimum CPU/RAM/OS configuration was established. Compiler architecture and recommended emulator are not proof of hardware compatibility.
- https://github.com/FlatRockSoft/Hovertank3D/blob/86f6b5ed34c52d2ca8acbb26391ebd5b2542f1fa/README
- https://github.com/FlatRockSoft/Hovertank3D/blob/86f6b5ed34c52d2ca8acbb26391ebd5b2542f1fa/HOVER.PRJ

### AI (no-evidence-found)

No explicit AI-development claim found in inspected project documentation. This is unknown, not a negative determination.
- https://github.com/FlatRockSoft/Hovertank3D/blob/86f6b5ed34c52d2ca8acbb26391ebd5b2542f1fa/README
- https://github.com/FlatRockSoft/Hovertank3D/blob/86f6b5ed34c52d2ca8acbb26391ebd5b2542f1fa/HOVER.PRJ

### Relationships (reviewed)

Separate original from later Hovertank source ports.
- https://github.com/FlatRockSoft/Hovertank3D/blob/86f6b5ed34c52d2ca8acbb26391ebd5b2542f1fa/README
- https://github.com/FlatRockSoft/Hovertank3D/blob/86f6b5ed34c52d2ca8acbb26391ebd5b2542f1fa/HOVER.PRJ

## Iron Seed — original-source Free Pascal SDL2 port

Project ID: iron-seed-fpc · Overall audit: reviewed

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
  "display_title": "Iron Seed — original-source Free Pascal SDL2 port",
  "id": "iron-seed-fpc",
  "last_activity": "2024-09-07",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "Pascal",
    "C",
    "D"
  ],
  "record_class": "subject",
  "repo": "https://github.com/mnalis/ironseed_fpc",
  "runtime_profiles": [],
  "source_cpu": [
    "x86"
  ],
  "source_language": [
    "Pascal"
  ],
  "source_platforms": [
    "DOS"
  ],
  "status": "Source reviewed; independent build/play test not performed",
  "subjects": [
    "Iron Seed"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "x86",
    "x86-64"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Linux"
  ],
  "techniques": [],
  "title": "Iron Seed — original-source Free Pascal SDL2 port",
  "tool_kinds": [],
  "types": [
    "original-source Linux port"
  ],
  "upstream_name": "Iron Seed — original-source Free Pascal SDL2 port",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

Native GNU/Linux port of 1994 Channel 7 DOS original released sources.
- https://github.com/mnalis/ironseed_fpc/blob/9fbb093ddcb3a62f98482e39d7416f2da32cf464/README.md
- https://github.com/mnalis/ironseed_fpc/blob/9fbb093ddcb3a62f98482e39d7416f2da32cf464/Makefile

### Classification (reviewed)

Original-source port to Linux. Current native Linux target, not DOS build. release_sdl lacks anti-corruption checks; debug_sdl recommended. GPL 3+. Big-endian datafiles explicitly do not work, per upstream code/history.
- https://github.com/mnalis/ironseed_fpc/blob/9fbb093ddcb3a62f98482e39d7416f2da32cf464/README.md
- https://github.com/mnalis/ironseed_fpc/blob/9fbb093ddcb3a62f98482e39d7416f2da32cf464/Makefile

### Source CPU (reviewed)

Original DOS x86 input lineage is established by the source release and build documentation.
- https://github.com/mnalis/ironseed_fpc/blob/9fbb093ddcb3a62f98482e39d7416f2da32cf464/README.md
- https://github.com/mnalis/ironseed_fpc/blob/9fbb093ddcb3a62f98482e39d7416f2da32cf464/Makefile

### Target CPU (reviewed)

FPC Linux port reports upstream tests on i386 and x86_64; other architectures are potential, not verified outputs.
- https://github.com/mnalis/ironseed_fpc/blob/9fbb093ddcb3a62f98482e39d7416f2da32cf464/README.md
- https://github.com/mnalis/ironseed_fpc/blob/9fbb093ddcb3a62f98482e39d7416f2da32cf464/Makefile

### Build (reviewed)

FPC, GCC, SDL2/SDL2_mixer; make or make debug_sdl then ./is. Makefile builds Pascal programs plus optional D data converters. Documentation/source inspection only; no toolchain build performed. Build/play/byte-exact flags remain unknown. 
- https://github.com/mnalis/ironseed_fpc/blob/9fbb093ddcb3a62f98482e39d7416f2da32cf464/README.md
- https://github.com/mnalis/ironseed_fpc/blob/9fbb093ddcb3a62f98482e39d7416f2da32cf464/Makefile

### Runtime profiles (no-evidence-found)

Upstream tested x86_64/i386 Linux. is.pas retains original 1994 Channel 7 and port contributor copyrights. No complete minimum CPU/RAM/OS configuration was established. Compiler architecture and recommended emulator are not proof of hardware compatibility.
- https://github.com/mnalis/ironseed_fpc/blob/9fbb093ddcb3a62f98482e39d7416f2da32cf464/README.md
- https://github.com/mnalis/ironseed_fpc/blob/9fbb093ddcb3a62f98482e39d7416f2da32cf464/Makefile

### AI (no-evidence-found)

No explicit AI-development claim found in inspected project documentation. This is unknown, not a negative determination.
- https://github.com/mnalis/ironseed_fpc/blob/9fbb093ddcb3a62f98482e39d7416f2da32cf464/README.md
- https://github.com/mnalis/ironseed_fpc/blob/9fbb093ddcb3a62f98482e39d7416f2da32cf464/Makefile

### Relationships (reviewed)

Fork of nukebloodaxe/ironseed_fpc. Verified 69 commits ahead / 0 behind parent master, including SDL2 migration, mouse-boundary crash fixes, PIC support; original-source lineage, not executable emulation.
- https://github.com/mnalis/ironseed_fpc/blob/9fbb093ddcb3a62f98482e39d7416f2da32cf464/README.md
- https://github.com/mnalis/ironseed_fpc/blob/9fbb093ddcb3a62f98482e39d7416f2da32cf464/Makefile

## Sources

```json
[
  {
    "id": "github-skynettx-dosraptor",
    "kind": "github-repository",
    "reason": "Original released game source with replacement sound integration",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/skynettx/dosraptor"
  },
  {
    "id": "github-commercial-game-sources-kens_labyrinth",
    "kind": "github-repository",
    "reason": "Mirror of author-released Ken’s Labyrinth v2.1 full-version source",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/commercial-game-sources/kens_labyrinth"
  },
  {
    "id": "github-skeeto-dosdefender-ld31",
    "kind": "github-repository",
    "reason": "Original 2014 Ludum Dare 31 DOS homebrew",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/skeeto/dosdefender-ld31"
  },
  {
    "id": "github-thefakemontyontherun-dungeons-of-noudar",
    "kind": "github-repository",
    "reason": "New 2.5D first-person dungeon crawler for MS-DOS/FreeDOS",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/TheFakeMontyOnTheRun/dungeons-of-noudar"
  },
  {
    "id": "github-jani-nykanen-plutonium-caverns",
    "kind": "github-repository",
    "reason": "Original 2019 MS-DOS puzzle homebrew",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/jani-nykanen/plutonium-caverns"
  },
  {
    "id": "github-porta2note-gridfighter3d",
    "kind": "github-repository",
    "reason": "Official source release of Jay Hammer’s2017-onward arcade/VR game",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/porta2note/gridfighter3d"
  },
  {
    "id": "github-lethal-guitar-biomenacedecomp",
    "kind": "github-repository",
    "reason": "Decompilation/source reconstruction of Bio Menace episode 1",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/lethal-guitar/BioMenaceDecomp"
  },
  {
    "id": "github-catacombgames-catacomb",
    "kind": "github-repository",
    "reason": "Original released source for 2D Catacomb",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/CatacombGames/Catacomb"
  },
  {
    "id": "github-catacombgames-catacomb3d",
    "kind": "github-repository",
    "reason": "Original released source for Catacomb3-D aka Catacombs 3/A New Dimension",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/CatacombGames/Catacomb3D"
  },
  {
    "id": "github-keendreams-keen",
    "kind": "github-repository",
    "reason": "Crowdfunding-enabled original game source release",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/keendreams/keen"
  },
  {
    "id": "github-flatrocksoft-hovertank3d",
    "kind": "github-repository",
    "reason": "Original GPL release of Hovertank3D source",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/FlatRockSoft/Hovertank3D"
  },
  {
    "id": "github-mnalis-ironseed_fpc",
    "kind": "github-repository",
    "reason": "Native GNU/Linux port of 1994 Channel 7 DOS original released sources",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/mnalis/ironseed_fpc"
  }
]
```

## Decisions

```json
[
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/skynettx/dosraptor/blob/4403569505c215c6cebe02cc3344e670499def1d/README.md",
      "https://github.com/skynettx/dosraptor/blob/4403569505c215c6cebe02cc3344e670499def1d/SOURCE/RAP.C",
      "https://github.com/skynettx/dosraptor/blob/4403569505c215c6cebe02cc3344e670499def1d/SOURCE/MAKEFILE",
      "https://github.com/skynettx/dosraptor/tree/4403569505c215c6cebe02cc3344e670499def1d/GFX",
      "https://github.com/skynettx/dosraptor/tree/4403569505c215c6cebe02cc3344e670499def1d/apodmx",
      "https://github.com/skynettx/dosraptor/tree/4403569505c215c6cebe02cc3344e670499def1d/audiolib",
      "https://github.com/skynettx/dosraptor/commit/4403569505c215c6cebe02cc3344e670499def1d"
    ],
    "id": "2026-10-17-promote-dosraptor-original",
    "project_ids": [
      "dosraptor-original"
    ],
    "reason": "Original released game source with replacement sound integration",
    "source_ids": [
      "github-skynettx-dosraptor"
    ],
    "title": "Raptor: Call of the Shadows — original DOS v1.2 sources",
    "url": "https://github.com/skynettx/dosraptor"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/commercial-game-sources/kens_labyrinth/blob/452b72a5f2b88ffd856a2f4c320f25f7c4caab6c/README.md",
      "https://github.com/commercial-game-sources/kens_labyrinth/blob/452b72a5f2b88ffd856a2f4c320f25f7c4caab6c/README.TXT",
      "https://github.com/commercial-game-sources/kens_labyrinth/blob/452b72a5f2b88ffd856a2f4c320f25f7c4caab6c/MAKEFILE",
      "https://github.com/commercial-game-sources/kens_labyrinth/blob/452b72a5f2b88ffd856a2f4c320f25f7c4caab6c/LAB3D.C",
      "https://github.com/commercial-game-sources/kens_labyrinth/blob/452b72a5f2b88ffd856a2f4c320f25f7c4caab6c/GRAPHX.C",
      "https://github.com/commercial-game-sources/kens_labyrinth/commit/452b72a5f2b88ffd856a2f4c320f25f7c4caab6c"
    ],
    "id": "2026-10-17-promote-kens-labyrinth-original-dos",
    "project_ids": [
      "kens-labyrinth-original-dos"
    ],
    "reason": "Mirror of author-released Ken’s Labyrinth v2.1 full-version source",
    "source_ids": [
      "github-commercial-game-sources-kens_labyrinth"
    ],
    "title": "Ken’s Labyrinth — preserved original DOS sources",
    "url": "https://github.com/commercial-game-sources/kens_labyrinth"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/skeeto/dosdefender-ld31/blob/f6242450425c530dcbba54d7937b6b1e23e29cd2/README.md",
      "https://github.com/skeeto/dosdefender-ld31/blob/f6242450425c530dcbba54d7937b6b1e23e29cd2/Makefile",
      "https://github.com/skeeto/dosdefender-ld31/blob/f6242450425c530dcbba54d7937b6b1e23e29cd2/com.ld",
      "https://github.com/skeeto/dosdefender-ld31/blob/f6242450425c530dcbba54d7937b6b1e23e29cd2/dosdef.c",
      "https://github.com/skeeto/dosdefender-ld31/commit/f6242450425c530dcbba54d7937b6b1e23e29cd2"
    ],
    "id": "2026-10-17-promote-dos-defender",
    "project_ids": [
      "dos-defender"
    ],
    "reason": "Original 2014 Ludum Dare 31 DOS homebrew",
    "source_ids": [
      "github-skeeto-dosdefender-ld31"
    ],
    "title": "DOS Defender — native DOS Ludum Dare shooter",
    "url": "https://github.com/skeeto/dosdefender-ld31"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/TheFakeMontyOnTheRun/dungeons-of-noudar/blob/03e94de322613c80fca748e8eb5426de59b993d4/README.md",
      "https://github.com/TheFakeMontyOnTheRun/dungeons-of-noudar/blob/03e94de322613c80fca748e8eb5426de59b993d4/DungeonsOfNoudar486/Makefile",
      "https://github.com/TheFakeMontyOnTheRun/dungeons-of-noudar/blob/03e94de322613c80fca748e8eb5426de59b993d4/DungeonsOfNoudar486/main.cpp",
      "https://github.com/TheFakeMontyOnTheRun/dungeons-of-noudar/blob/03e94de322613c80fca748e8eb5426de59b993d4/.gitmodules",
      "https://github.com/TheFakeMontyOnTheRun/dungeons-of-noudar/commit/03e94de322613c80fca748e8eb5426de59b993d4"
    ],
    "id": "2026-10-17-promote-dungeons-of-noudar",
    "project_ids": [
      "dungeons-of-noudar"
    ],
    "reason": "New 2.5D first-person dungeon crawler for MS-DOS/FreeDOS",
    "source_ids": [
      "github-thefakemontyontherun-dungeons-of-noudar"
    ],
    "title": "Dungeons of Noudar — native DOS dungeon crawler",
    "url": "https://github.com/TheFakeMontyOnTheRun/dungeons-of-noudar"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/jani-nykanen/plutonium-caverns/blob/7fb3ffec8a32502688b2b52429cbe2da8e90435c/README.md",
      "https://github.com/jani-nykanen/plutonium-caverns/blob/7fb3ffec8a32502688b2b52429cbe2da8e90435c/src/core/graphics.c",
      "https://github.com/jani-nykanen/plutonium-caverns/tree/7fb3ffec8a32502688b2b52429cbe2da8e90435c/src",
      "https://github.com/jani-nykanen/plutonium-caverns/commit/7fb3ffec8a32502688b2b52429cbe2da8e90435c"
    ],
    "id": "2026-10-17-promote-plutonium-caverns",
    "project_ids": [
      "plutonium-caverns"
    ],
    "reason": "Original 2019 MS-DOS puzzle homebrew",
    "source_ids": [
      "github-jani-nykanen-plutonium-caverns"
    ],
    "title": "Plutonium Caverns — native DOS puzzle game",
    "url": "https://github.com/jani-nykanen/plutonium-caverns"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/porta2note/gridfighter3d/blob/155596b21c3eff30738f3be3081ff33d70658701/README.md",
      "https://github.com/porta2note/gridfighter3d/blob/155596b21c3eff30738f3be3081ff33d70658701/GRID3D24.BAS",
      "https://github.com/porta2note/gridfighter3d/blob/155596b21c3eff30738f3be3081ff33d70658701/GRID3D24_64_LINUX.BAS",
      "https://github.com/porta2note/gridfighter3d/commit/155596b21c3eff30738f3be3081ff33d70658701"
    ],
    "id": "2026-10-17-promote-gridfighter-3d",
    "project_ids": [
      "gridfighter-3d"
    ],
    "reason": "Official source release of Jay Hammer’s2017-onward arcade/VR game",
    "source_ids": [
      "github-porta2note-gridfighter3d"
    ],
    "title": "Gridfighter 3D — QuickBASIC DOS arcade game",
    "url": "https://github.com/porta2note/gridfighter3d"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/lethal-guitar/BioMenaceDecomp/blob/4471bcfc03ff2ebe10620011fa45e9a1d086c841/README.md",
      "https://github.com/lethal-guitar/BioMenaceDecomp/blob/4471bcfc03ff2ebe10620011fa45e9a1d086c841/SRC/BM_MAIN.C",
      "https://github.com/lethal-guitar/BioMenaceDecomp/blob/4471bcfc03ff2ebe10620011fa45e9a1d086c841/SRC/MAKEFILE",
      "https://github.com/lethal-guitar/BioMenaceDecomp/tree/4471bcfc03ff2ebe10620011fa45e9a1d086c841/SRC",
      "https://github.com/lethal-guitar/BioMenaceDecomp/commit/4471bcfc03ff2ebe10620011fa45e9a1d086c841"
    ],
    "id": "2026-10-17-promote-biomenace-decomp",
    "project_ids": [
      "biomenace-decomp"
    ],
    "reason": "Decompilation/source reconstruction of Bio Menace episode 1",
    "source_ids": [
      "github-lethal-guitar-biomenacedecomp"
    ],
    "title": "BioMenace — matching DOS episode-one reconstruction",
    "url": "https://github.com/lethal-guitar/BioMenaceDecomp"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/CatacombGames/Catacomb/blob/e657bc3aa8fef0d89bd09aa8fa0e051941c66518/README.md",
      "https://github.com/CatacombGames/Catacomb/blob/e657bc3aa8fef0d89bd09aa8fa0e051941c66518/MAKECAT.BAT",
      "https://github.com/CatacombGames/Catacomb/blob/e657bc3aa8fef0d89bd09aa8fa0e051941c66518/CATACOMB.PAS",
      "https://github.com/CatacombGames/Catacomb/blob/e657bc3aa8fef0d89bd09aa8fa0e051941c66518/CATASM.ASM",
      "https://github.com/CatacombGames/Catacomb/blob/e657bc3aa8fef0d89bd09aa8fa0e051941c66518/CGADATA.PAS",
      "https://github.com/CatacombGames/Catacomb/blob/e657bc3aa8fef0d89bd09aa8fa0e051941c66518/EGADATA.PAS",
      "https://github.com/CatacombGames/Catacomb/commit/e657bc3aa8fef0d89bd09aa8fa0e051941c66518"
    ],
    "id": "2026-10-17-promote-catacomb-original-dos",
    "project_ids": [
      "catacomb-original-dos"
    ],
    "reason": "Original released source for 2D Catacomb",
    "source_ids": [
      "github-catacombgames-catacomb"
    ],
    "title": "Catacomb — original Turbo Pascal DOS sources",
    "url": "https://github.com/CatacombGames/Catacomb"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/CatacombGames/Catacomb3D/blob/aa97f4995dc7dbea3ecc1794a2d4d4354839cad4/README.md",
      "https://github.com/CatacombGames/Catacomb3D/blob/aa97f4995dc7dbea3ecc1794a2d4d4354839cad4/CAT3D.PRJ",
      "https://github.com/CatacombGames/Catacomb3D/blob/aa97f4995dc7dbea3ecc1794a2d4d4354839cad4/C3_ASM.ASM",
      "https://github.com/CatacombGames/Catacomb3D/blob/aa97f4995dc7dbea3ecc1794a2d4d4354839cad4/C3_MAIN.C",
      "https://github.com/CatacombGames/Catacomb3D/commit/aa97f4995dc7dbea3ecc1794a2d4d4354839cad4"
    ],
    "id": "2026-10-17-promote-catacomb-3d-original-dos",
    "project_ids": [
      "catacomb-3d-original-dos"
    ],
    "reason": "Original released source for Catacomb3-D aka Catacombs 3/A New Dimension",
    "source_ids": [
      "github-catacombgames-catacomb3d"
    ],
    "title": "Catacomb 3-D: The Descent — original DOS sources",
    "url": "https://github.com/CatacombGames/Catacomb3D"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/keendreams/keen/blob/4348b4719be87a0b873f5f4f77b4de82ddf7050c/README.md",
      "https://github.com/keendreams/keen/blob/4348b4719be87a0b873f5f4f77b4de82ddf7050c/kdreams.prj",
      "https://github.com/keendreams/keen/blob/4348b4719be87a0b873f5f4f77b4de82ddf7050c/kd_main.c",
      "https://github.com/keendreams/keen/blob/4348b4719be87a0b873f5f4f77b4de82ddf7050c/id_vw_a.asm",
      "https://github.com/keendreams/keen/blob/4348b4719be87a0b873f5f4f77b4de82ddf7050c/static/make.bat",
      "https://github.com/keendreams/keen/commit/4348b4719be87a0b873f5f4f77b4de82ddf7050c"
    ],
    "id": "2026-10-17-promote-keen-dreams-original-dos",
    "project_ids": [
      "keen-dreams-original-dos"
    ],
    "reason": "Crowdfunding-enabled original game source release",
    "source_ids": [
      "github-keendreams-keen"
    ],
    "title": "Commander Keen in Keen Dreams — original DOS source release",
    "url": "https://github.com/keendreams/keen"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/FlatRockSoft/Hovertank3D/blob/86f6b5ed34c52d2ca8acbb26391ebd5b2542f1fa/README",
      "https://github.com/FlatRockSoft/Hovertank3D/blob/86f6b5ed34c52d2ca8acbb26391ebd5b2542f1fa/HOVER.PRJ",
      "https://github.com/FlatRockSoft/Hovertank3D/blob/86f6b5ed34c52d2ca8acbb26391ebd5b2542f1fa/IDASM.ASM",
      "https://github.com/FlatRockSoft/Hovertank3D/blob/86f6b5ed34c52d2ca8acbb26391ebd5b2542f1fa/HOVMAIN.C",
      "https://github.com/FlatRockSoft/Hovertank3D/commit/86f6b5ed34c52d2ca8acbb26391ebd5b2542f1fa"
    ],
    "id": "2026-10-17-promote-hovertank-3d-original-dos",
    "project_ids": [
      "hovertank-3d-original-dos"
    ],
    "reason": "Original GPL release of Hovertank3D source",
    "source_ids": [
      "github-flatrocksoft-hovertank3d"
    ],
    "title": "Hovertank 3-D — original DOS source release",
    "url": "https://github.com/FlatRockSoft/Hovertank3D"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/mnalis/ironseed_fpc/blob/9fbb093ddcb3a62f98482e39d7416f2da32cf464/README.md",
      "https://github.com/mnalis/ironseed_fpc/blob/9fbb093ddcb3a62f98482e39d7416f2da32cf464/Makefile",
      "https://github.com/mnalis/ironseed_fpc/blob/9fbb093ddcb3a62f98482e39d7416f2da32cf464/is.pas",
      "https://github.com/mnalis/ironseed_fpc/blob/9fbb093ddcb3a62f98482e39d7416f2da32cf464/c_utils.c",
      "https://github.com/nukebloodaxe/ironseed_fpc/commit/99feae1c70a2784c691669d50a5999fb5f503b45",
      "https://github.com/mnalis/ironseed_fpc/commit/9fbb093ddcb3a62f98482e39d7416f2da32cf464"
    ],
    "id": "2026-10-17-promote-iron-seed-fpc",
    "project_ids": [
      "iron-seed-fpc"
    ],
    "reason": "Native GNU/Linux port of 1994 Channel 7 DOS original released sources",
    "source_ids": [
      "github-mnalis-ironseed_fpc"
    ],
    "title": "Iron Seed — original-source Free Pascal SDL2 port",
    "url": "https://github.com/mnalis/ironseed_fpc"
  }
]
```

## Research event notes

DOS catalogue and developer/source links were screened against existing projects, sources and decisions. All prior records are preserved. Game assets and original source licensing are distinguished; no upstream game code was executed. BioMenace episode-one matching is an attributed upstream claim. Native DOS programs are distinguished from optional DOSBox web packaging, and Iron Seed is explicitly a Linux port of a DOS original.
