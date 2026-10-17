# Add ten native Amiga game, source-preservation and enhancement projects from release pages, developer links and the Amiga Sources catalogue.

Add ten native Amiga game, source-preservation and enhancement projects from release pages, developer links and the Amiga Sources catalogue.

Date: 2026-10-17 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- neonnoir-amiga / AI (no-evidence-found): No explicit development-AI attribution found in inspected documentation, selected source/build files and head commit. Non-use is not inferred.
- acid-software-pd-game-sources / Runtime profiles (no-evidence-found): No complete minimum CPU/RAM/OS profile established from inspected material. Build tool settings and author performance recommendations are not automatically runtime minima.
- acid-software-pd-game-sources / AI (no-evidence-found): No explicit development-AI attribution found in inspected documentation, selected source/build files and head commit. Non-use is not inferred.
- lazymines-amiga / Runtime profiles (no-evidence-found): No complete minimum CPU/RAM/OS profile established from inspected material. Build tool settings and author performance recommendations are not automatically runtime minima.
- lazymines-amiga / AI (no-evidence-found): No explicit development-AI attribution found in inspected documentation, selected source/build files and head commit. Non-use is not inferred.
- neonworld-amiga / AI (no-evidence-found): No explicit development-AI attribution found in inspected documentation, selected source/build files and head commit. Non-use is not inferred.
- breathless-native-amiga-source / Runtime profiles (no-evidence-found): No complete minimum CPU/RAM/OS profile established from inspected material. Build tool settings and author performance recommendations are not automatically runtime minima.
- breathless-native-amiga-source / AI (no-evidence-found): No explicit development-AI attribution found in inspected documentation, selected source/build files and head commit. Non-use is not inferred.
- alien-breed-3d-rtg-amiga / Runtime profiles (no-evidence-found): No complete minimum CPU/RAM/OS profile established from inspected material. Build tool settings and author performance recommendations are not automatically runtime minima.
- alien-breed-3d-rtg-amiga / AI (no-evidence-found): No explicit development-AI attribution found in inspected documentation, selected source/build files and head commit. Non-use is not inferred.
- alien-breed-3d2-rebuilt-amiga / AI (no-evidence-found): No explicit development-AI attribution found in inspected documentation, selected source/build files and head commit. Non-use is not inferred.
- high-octane-original-amiga / Runtime profiles (no-evidence-found): No complete minimum CPU/RAM/OS profile established from inspected material. Build tool settings and author performance recommendations are not automatically runtime minima.
- high-octane-original-amiga / AI (no-evidence-found): No explicit development-AI attribution found in inspected documentation, selected source/build files and head commit. Non-use is not inferred.
- alien-breed-3d2-redux / Runtime profiles (no-evidence-found): No complete minimum CPU/RAM/OS profile established from inspected material. Build tool settings and author performance recommendations are not automatically runtime minima.
- alien-breed-3d2-redux / AI (no-evidence-found): No explicit development-AI attribution found in inspected documentation, selected source/build files and head commit. Non-use is not inferred.

## NEONnoir

Project ID: neonnoir-amiga · Overall audit: reviewed

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
  "display_title": "NEONnoir",
  "id": "neonnoir-amiga",
  "last_activity": "2025-04-06",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "Blitz Basic"
  ],
  "record_class": "subject",
  "repo": "https://github.com/steamknight/NEONnoir",
  "runtime_profiles": [
    {
      "cpu_family": "m68k",
      "evidence": [
        "https://github.com/steamknight/NEONnoir/blob/3a702ba85105169f61196a7a924533dc3fba667e/README.md"
      ],
      "name": "Author-stated target",
      "notes": "README targets Amiga 1200; a complete RAM/OS minimum was not established.",
      "platform": "Amiga"
    }
  ],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Source reviewed; independent build/play test not performed",
  "subjects": [
    "NEONnoir"
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
  "title": "NEONnoir",
  "tool_kinds": [],
  "types": [
    "native homebrew game"
  ],
  "upstream_name": "NEONnoir",
  "work_kinds": []
}
```

### Identity (reviewed)

Cyberpunk point-and-click adventure/visual novel for Amiga 1200, created for the Amiga Blitz Basic Game Jam.
- https://github.com/steamknight/NEONnoir/blob/3a702ba85105169f61196a7a924533dc3fba667e/README.md
- https://github.com/steamknight/NEONnoir/blob/3a702ba85105169f61196a7a924533dc3fba667e/src/NN_main.bb2
- https://github.com/steamknight/NEONnoir/blob/3a702ba85105169f61196a7a924533dc3fba667e/build.ps1
- https://github.com/steamknight/NEONnoir/commit/3a702ba85105169f61196a7a924533dc3fba667e
- https://steamknight.itch.io/neonnoir

### Classification (reviewed)

Authored native Amiga game, not original-binary reconstruction.
- https://github.com/steamknight/NEONnoir/blob/3a702ba85105169f61196a7a924533dc3fba667e/README.md
- https://github.com/steamknight/NEONnoir/blob/3a702ba85105169f61196a7a924533dc3fba667e/src/NN_main.bb2
- https://github.com/steamknight/NEONnoir/blob/3a702ba85105169f61196a7a924533dc3fba667e/build.ps1
- https://github.com/steamknight/NEONnoir/commit/3a702ba85105169f61196a7a924533dc3fba667e
- https://steamknight.itch.io/neonnoir

### Source CPU (not-applicable)

No predecessor machine-code input is reconstructed; source platform/CPU are left empty.
- https://github.com/steamknight/NEONnoir/blob/3a702ba85105169f61196a7a924533dc3fba667e/README.md
- https://github.com/steamknight/NEONnoir/blob/3a702ba85105169f61196a7a924533dc3fba667e/src/NN_main.bb2
- https://github.com/steamknight/NEONnoir/blob/3a702ba85105169f61196a7a924533dc3fba667e/build.ps1
- https://github.com/steamknight/NEONnoir/commit/3a702ba85105169f61196a7a924533dc3fba667e
- https://steamknight.itch.io/neonnoir

### Target CPU (reviewed)

Native classic Amiga/m68k output is established by reviewed source/build declarations.
- https://github.com/steamknight/NEONnoir/blob/3a702ba85105169f61196a7a924533dc3fba667e/README.md
- https://github.com/steamknight/NEONnoir/blob/3a702ba85105169f61196a7a924533dc3fba667e/src/NN_main.bb2
- https://github.com/steamknight/NEONnoir/blob/3a702ba85105169f61196a7a924533dc3fba667e/build.ps1
- https://github.com/steamknight/NEONnoir/commit/3a702ba85105169f61196a7a924533dc3fba667e
- https://steamknight.itch.io/neonnoir

### Build (reviewed)

Readable Blitz Basic modules, editor sources, assets and a PowerShell assembly/packaging script are supplied. NN_main.bb2 contains native Amiga display and timing setup. Build/play/byte-exact flags remain unknown; no candidate software was executed.
- https://github.com/steamknight/NEONnoir/blob/3a702ba85105169f61196a7a924533dc3fba667e/README.md
- https://github.com/steamknight/NEONnoir/blob/3a702ba85105169f61196a7a924533dc3fba667e/src/NN_main.bb2
- https://github.com/steamknight/NEONnoir/blob/3a702ba85105169f61196a7a924533dc3fba667e/build.ps1
- https://github.com/steamknight/NEONnoir/commit/3a702ba85105169f61196a7a924533dc3fba667e
- https://steamknight.itch.io/neonnoir

### Runtime profiles (reviewed)

README targets Amiga 1200; a complete RAM/OS minimum was not established.
- https://github.com/steamknight/NEONnoir/blob/3a702ba85105169f61196a7a924533dc3fba667e/README.md
- https://github.com/steamknight/NEONnoir/blob/3a702ba85105169f61196a7a924533dc3fba667e/src/NN_main.bb2
- https://github.com/steamknight/NEONnoir/blob/3a702ba85105169f61196a7a924533dc3fba667e/build.ps1
- https://github.com/steamknight/NEONnoir/commit/3a702ba85105169f61196a7a924533dc3fba667e
- https://steamknight.itch.io/neonnoir

### AI (no-evidence-found)

No explicit development-AI attribution found in inspected documentation, selected source/build files and head commit. Non-use is not inferred.
- https://github.com/steamknight/NEONnoir/blob/3a702ba85105169f61196a7a924533dc3fba667e/README.md
- https://github.com/steamknight/NEONnoir/blob/3a702ba85105169f61196a7a924533dc3fba667e/src/NN_main.bb2
- https://github.com/steamknight/NEONnoir/blob/3a702ba85105169f61196a7a924533dc3fba667e/build.ps1
- https://github.com/steamknight/NEONnoir/commit/3a702ba85105169f61196a7a924533dc3fba667e
- https://steamknight.itch.io/neonnoir

### Relationships (reviewed)

New native game, separate from NeonWorld. Code is CC BY 4.0, while other content/assets use CC BY-NC-ND 4.0; do not present all assets as freely modifiable.
- https://github.com/steamknight/NEONnoir/blob/3a702ba85105169f61196a7a924533dc3fba667e/README.md
- https://github.com/steamknight/NEONnoir/blob/3a702ba85105169f61196a7a924533dc3fba667e/src/NN_main.bb2
- https://github.com/steamknight/NEONnoir/blob/3a702ba85105169f61196a7a924533dc3fba667e/build.ps1
- https://github.com/steamknight/NEONnoir/commit/3a702ba85105169f61196a7a924533dc3fba667e
- https://steamknight.itch.io/neonnoir

## Acid Software Public Domain Game Sources

Project ID: acid-software-pd-game-sources · Overall audit: reviewed

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
  "display_title": "Acid Software Public Domain Game Sources",
  "id": "acid-software-pd-game-sources",
  "last_activity": "2018-03-17",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "Blitz Basic"
  ],
  "record_class": "subject",
  "repo": "https://github.com/nitrologic/acidpd",
  "runtime_profiles": [],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [
    "Blitz Basic"
  ],
  "source_platforms": [
    "Amiga"
  ],
  "status": "Source reviewed; independent build/play test not performed",
  "subjects": [
    "Acid Software Public Domain Game Sources"
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
  "title": "Acid Software Public Domain Game Sources",
  "tool_kinds": [],
  "types": [
    "original-source restoration/enhancement"
  ],
  "upstream_name": "Acid Software Public Domain Game Sources",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

Acid Software collection of Amiga public-domain games, containing untokenized Blitz2 sources in many cases.
- https://github.com/nitrologic/acidpd/blob/87a024d4f32938093e519191588ff0a29228f7af/README.md
- https://github.com/nitrologic/acidpd/blob/87a024d4f32938093e519191588ff0a29228f7af/defender/defender.src
- https://github.com/nitrologic/acidpd/blob/87a024d4f32938093e519191588ff0a29228f7af/AboutBlitz2.txt
- https://github.com/nitrologic/acidpd/commit/87a024d4f32938093e519191588ff0a29228f7af

### Classification (reviewed)

Original Amiga source preservation or a distinct native enhancement of it.
- https://github.com/nitrologic/acidpd/blob/87a024d4f32938093e519191588ff0a29228f7af/README.md
- https://github.com/nitrologic/acidpd/blob/87a024d4f32938093e519191588ff0a29228f7af/defender/defender.src
- https://github.com/nitrologic/acidpd/blob/87a024d4f32938093e519191588ff0a29228f7af/AboutBlitz2.txt
- https://github.com/nitrologic/acidpd/commit/87a024d4f32938093e519191588ff0a29228f7af

### Source CPU (reviewed)

Inspected original source/build material identifies a classic Amiga m68k game lineage.
- https://github.com/nitrologic/acidpd/blob/87a024d4f32938093e519191588ff0a29228f7af/README.md
- https://github.com/nitrologic/acidpd/blob/87a024d4f32938093e519191588ff0a29228f7af/defender/defender.src
- https://github.com/nitrologic/acidpd/blob/87a024d4f32938093e519191588ff0a29228f7af/AboutBlitz2.txt
- https://github.com/nitrologic/acidpd/commit/87a024d4f32938093e519191588ff0a29228f7af

### Target CPU (reviewed)

Native classic Amiga/m68k output is established by reviewed source/build declarations.
- https://github.com/nitrologic/acidpd/blob/87a024d4f32938093e519191588ff0a29228f7af/README.md
- https://github.com/nitrologic/acidpd/blob/87a024d4f32938093e519191588ff0a29228f7af/defender/defender.src
- https://github.com/nitrologic/acidpd/blob/87a024d4f32938093e519191588ff0a29228f7af/AboutBlitz2.txt
- https://github.com/nitrologic/acidpd/commit/87a024d4f32938093e519191588ff0a29228f7af

### Build (reviewed)

Inspected Defender text source loads Amiga sprites, shapes, sound and bitmaps. Archive also contains game directories, magazines/examples and binary assets; source completeness varies across its contents. Build/play/byte-exact flags remain unknown; no candidate software was executed.
- https://github.com/nitrologic/acidpd/blob/87a024d4f32938093e519191588ff0a29228f7af/README.md
- https://github.com/nitrologic/acidpd/blob/87a024d4f32938093e519191588ff0a29228f7af/defender/defender.src
- https://github.com/nitrologic/acidpd/blob/87a024d4f32938093e519191588ff0a29228f7af/AboutBlitz2.txt
- https://github.com/nitrologic/acidpd/commit/87a024d4f32938093e519191588ff0a29228f7af

### Runtime profiles (no-evidence-found)

No complete minimum CPU/RAM/OS profile established from inspected material. Build tool settings and author performance recommendations are not automatically runtime minima.
- https://github.com/nitrologic/acidpd/blob/87a024d4f32938093e519191588ff0a29228f7af/README.md
- https://github.com/nitrologic/acidpd/blob/87a024d4f32938093e519191588ff0a29228f7af/defender/defender.src
- https://github.com/nitrologic/acidpd/blob/87a024d4f32938093e519191588ff0a29228f7af/AboutBlitz2.txt
- https://github.com/nitrologic/acidpd/commit/87a024d4f32938093e519191588ff0a29228f7af

### AI (no-evidence-found)

No explicit development-AI attribution found in inspected documentation, selected source/build files and head commit. Non-use is not inferred.
- https://github.com/nitrologic/acidpd/blob/87a024d4f32938093e519191588ff0a29228f7af/README.md
- https://github.com/nitrologic/acidpd/blob/87a024d4f32938093e519191588ff0a29228f7af/defender/defender.src
- https://github.com/nitrologic/acidpd/blob/87a024d4f32938093e519191588ff0a29228f7af/AboutBlitz2.txt
- https://github.com/nitrologic/acidpd/commit/87a024d4f32938093e519191588ff0a29228f7af

### Relationships (reviewed)

Track this coherent publisher collection once at repository root. Do not count every example or packaged copy as a separate restored game, or assume every included title has full source.
- https://github.com/nitrologic/acidpd/blob/87a024d4f32938093e519191588ff0a29228f7af/README.md
- https://github.com/nitrologic/acidpd/blob/87a024d4f32938093e519191588ff0a29228f7af/defender/defender.src
- https://github.com/nitrologic/acidpd/blob/87a024d4f32938093e519191588ff0a29228f7af/AboutBlitz2.txt
- https://github.com/nitrologic/acidpd/commit/87a024d4f32938093e519191588ff0a29228f7af

## LazyMines

Project ID: lazymines-amiga · Overall audit: reviewed

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
  "display_title": "LazyMines",
  "id": "lazymines-amiga",
  "last_activity": "2026-08-02",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "C"
  ],
  "record_class": "subject",
  "repo": "https://github.com/hlsyounes/lazymines",
  "runtime_profiles": [],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [
    "C"
  ],
  "source_platforms": [
    "Amiga"
  ],
  "status": "Source reviewed; independent build/play test not performed",
  "subjects": [
    "LazyMines"
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
  "title": "LazyMines",
  "tool_kinds": [],
  "types": [
    "original-source restoration/enhancement"
  ],
  "upstream_name": "LazyMines",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

Native Amiga Minesweeper game with preserved source headers dating to 1993–1994.
- https://github.com/hlsyounes/lazymines/blob/0553ded221a62c012934f5f6a322a5293637b121/Minesweeper.c
- https://github.com/hlsyounes/lazymines/blob/0553ded221a62c012934f5f6a322a5293637b121/field.c
- https://github.com/hlsyounes/lazymines/blob/0553ded221a62c012934f5f6a322a5293637b121/Smakefile
- https://github.com/hlsyounes/lazymines/commit/0553ded221a62c012934f5f6a322a5293637b121

### Classification (reviewed)

Original Amiga source preservation or a distinct native enhancement of it.
- https://github.com/hlsyounes/lazymines/blob/0553ded221a62c012934f5f6a322a5293637b121/Minesweeper.c
- https://github.com/hlsyounes/lazymines/blob/0553ded221a62c012934f5f6a322a5293637b121/field.c
- https://github.com/hlsyounes/lazymines/blob/0553ded221a62c012934f5f6a322a5293637b121/Smakefile
- https://github.com/hlsyounes/lazymines/commit/0553ded221a62c012934f5f6a322a5293637b121

### Source CPU (reviewed)

Inspected original source/build material identifies a classic Amiga m68k game lineage.
- https://github.com/hlsyounes/lazymines/blob/0553ded221a62c012934f5f6a322a5293637b121/Minesweeper.c
- https://github.com/hlsyounes/lazymines/blob/0553ded221a62c012934f5f6a322a5293637b121/field.c
- https://github.com/hlsyounes/lazymines/blob/0553ded221a62c012934f5f6a322a5293637b121/Smakefile
- https://github.com/hlsyounes/lazymines/commit/0553ded221a62c012934f5f6a322a5293637b121

### Target CPU (reviewed)

Native classic Amiga/m68k output is established by reviewed source/build declarations.
- https://github.com/hlsyounes/lazymines/blob/0553ded221a62c012934f5f6a322a5293637b121/Minesweeper.c
- https://github.com/hlsyounes/lazymines/blob/0553ded221a62c012934f5f6a322a5293637b121/field.c
- https://github.com/hlsyounes/lazymines/blob/0553ded221a62c012934f5f6a322a5293637b121/Smakefile
- https://github.com/hlsyounes/lazymines/commit/0553ded221a62c012934f5f6a322a5293637b121

### Build (reviewed)

C source implements Intuition/GadTools UI and minefield logic. Smakefile links with SAS/C libraries and Amiga libraries; no README or modern portable build is assumed. Build/play/byte-exact flags remain unknown; no candidate software was executed.
- https://github.com/hlsyounes/lazymines/blob/0553ded221a62c012934f5f6a322a5293637b121/Minesweeper.c
- https://github.com/hlsyounes/lazymines/blob/0553ded221a62c012934f5f6a322a5293637b121/field.c
- https://github.com/hlsyounes/lazymines/blob/0553ded221a62c012934f5f6a322a5293637b121/Smakefile
- https://github.com/hlsyounes/lazymines/commit/0553ded221a62c012934f5f6a322a5293637b121

### Runtime profiles (no-evidence-found)

No complete minimum CPU/RAM/OS profile established from inspected material. Build tool settings and author performance recommendations are not automatically runtime minima.
- https://github.com/hlsyounes/lazymines/blob/0553ded221a62c012934f5f6a322a5293637b121/Minesweeper.c
- https://github.com/hlsyounes/lazymines/blob/0553ded221a62c012934f5f6a322a5293637b121/field.c
- https://github.com/hlsyounes/lazymines/blob/0553ded221a62c012934f5f6a322a5293637b121/Smakefile
- https://github.com/hlsyounes/lazymines/commit/0553ded221a62c012934f5f6a322a5293637b121

### AI (no-evidence-found)

No explicit development-AI attribution found in inspected documentation, selected source/build files and head commit. Non-use is not inferred.
- https://github.com/hlsyounes/lazymines/blob/0553ded221a62c012934f5f6a322a5293637b121/Minesweeper.c
- https://github.com/hlsyounes/lazymines/blob/0553ded221a62c012934f5f6a322a5293637b121/field.c
- https://github.com/hlsyounes/lazymines/blob/0553ded221a62c012934f5f6a322a5293637b121/Smakefile
- https://github.com/hlsyounes/lazymines/commit/0553ded221a62c012934f5f6a322a5293637b121

### Relationships (reviewed)

Original Amiga source project, not a browser recreation. CPU attribution comes from the classic Amiga build and APIs, not the development host.
- https://github.com/hlsyounes/lazymines/blob/0553ded221a62c012934f5f6a322a5293637b121/Minesweeper.c
- https://github.com/hlsyounes/lazymines/blob/0553ded221a62c012934f5f6a322a5293637b121/field.c
- https://github.com/hlsyounes/lazymines/blob/0553ded221a62c012934f5f6a322a5293637b121/Smakefile
- https://github.com/hlsyounes/lazymines/commit/0553ded221a62c012934f5f6a322a5293637b121

## NeonWorld

Project ID: neonworld-amiga · Overall audit: reviewed

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
  "display_title": "NeonWorld",
  "id": "neonworld-amiga",
  "last_activity": "2025-03-06",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "m68k assembly",
    "Java"
  ],
  "record_class": "subject",
  "repo": "https://github.com/cobour/neon-world",
  "runtime_profiles": [
    {
      "cpu_family": "m68k",
      "evidence": [
        "https://github.com/cobour/neon-world/blob/53a4ab5d39f62bbd39b116e8effa03e6ea0fa22c/readme.md"
      ],
      "min_chip_ram_kib": 512,
      "min_cpu": "68000",
      "min_ram_kib": 1024,
      "name": "Documented PAL baseline",
      "notes": "README says PAL Amiga with 512 KiB Chip plus another 512 KiB of any type. Reported test machine had 1 MiB Chip and 1.5 MiB Slow, which is not the claimed minimum.",
      "platform": "Amiga"
    }
  ],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Source reviewed; independent build/play test not performed",
  "subjects": [
    "NeonWorld"
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
  "title": "NeonWorld",
  "tool_kinds": [],
  "types": [
    "native homebrew game"
  ],
  "upstream_name": "NeonWorld",
  "work_kinds": []
}
```

### Identity (reviewed)

PAL Amiga horizontal shooter developed as an A500 assembly project, with level/enemy tooling and public game sources.
- https://github.com/cobour/neon-world/blob/53a4ab5d39f62bbd39b116e8effa03e6ea0fa22c/readme.md
- https://github.com/cobour/neon-world/blob/53a4ab5d39f62bbd39b116e8effa03e6ea0fa22c/_main.asm
- https://github.com/cobour/neon-world/blob/53a4ab5d39f62bbd39b116e8effa03e6ea0fa22c/.vscode/tasks.json
- https://github.com/cobour/neon-world/commit/53a4ab5d39f62bbd39b116e8effa03e6ea0fa22c
- https://cobour.itch.io/neonworld

### Classification (reviewed)

Authored native Amiga game, not original-binary reconstruction.
- https://github.com/cobour/neon-world/blob/53a4ab5d39f62bbd39b116e8effa03e6ea0fa22c/readme.md
- https://github.com/cobour/neon-world/blob/53a4ab5d39f62bbd39b116e8effa03e6ea0fa22c/_main.asm
- https://github.com/cobour/neon-world/blob/53a4ab5d39f62bbd39b116e8effa03e6ea0fa22c/.vscode/tasks.json
- https://github.com/cobour/neon-world/commit/53a4ab5d39f62bbd39b116e8effa03e6ea0fa22c
- https://cobour.itch.io/neonworld

### Source CPU (not-applicable)

No predecessor machine-code input is reconstructed; source platform/CPU are left empty.
- https://github.com/cobour/neon-world/blob/53a4ab5d39f62bbd39b116e8effa03e6ea0fa22c/readme.md
- https://github.com/cobour/neon-world/blob/53a4ab5d39f62bbd39b116e8effa03e6ea0fa22c/_main.asm
- https://github.com/cobour/neon-world/blob/53a4ab5d39f62bbd39b116e8effa03e6ea0fa22c/.vscode/tasks.json
- https://github.com/cobour/neon-world/commit/53a4ab5d39f62bbd39b116e8effa03e6ea0fa22c
- https://cobour.itch.io/neonworld

### Target CPU (reviewed)

Native classic Amiga/m68k output is established by reviewed source/build declarations.
- https://github.com/cobour/neon-world/blob/53a4ab5d39f62bbd39b116e8effa03e6ea0fa22c/readme.md
- https://github.com/cobour/neon-world/blob/53a4ab5d39f62bbd39b116e8effa03e6ea0fa22c/_main.asm
- https://github.com/cobour/neon-world/blob/53a4ab5d39f62bbd39b116e8effa03e6ea0fa22c/.vscode/tasks.json
- https://github.com/cobour/neon-world/commit/53a4ab5d39f62bbd39b116e8effa03e6ea0fa22c
- https://cobour.itch.io/neonworld

### Build (reviewed)

Build tasks explicitly use vasm -m68000 and vlink. Java/JDK 21+ asset generation must run before assembly. Author reports real-A500 and FS-UAE testing; not independently reproduced. Build/play/byte-exact flags remain unknown; no candidate software was executed.
- https://github.com/cobour/neon-world/blob/53a4ab5d39f62bbd39b116e8effa03e6ea0fa22c/readme.md
- https://github.com/cobour/neon-world/blob/53a4ab5d39f62bbd39b116e8effa03e6ea0fa22c/_main.asm
- https://github.com/cobour/neon-world/blob/53a4ab5d39f62bbd39b116e8effa03e6ea0fa22c/.vscode/tasks.json
- https://github.com/cobour/neon-world/commit/53a4ab5d39f62bbd39b116e8effa03e6ea0fa22c
- https://cobour.itch.io/neonworld

### Runtime profiles (reviewed)

README says PAL Amiga with 512 KiB Chip plus another 512 KiB of any type. Reported test machine had 1 MiB Chip and 1.5 MiB Slow, which is not the claimed minimum.
- https://github.com/cobour/neon-world/blob/53a4ab5d39f62bbd39b116e8effa03e6ea0fa22c/readme.md
- https://github.com/cobour/neon-world/blob/53a4ab5d39f62bbd39b116e8effa03e6ea0fa22c/_main.asm
- https://github.com/cobour/neon-world/blob/53a4ab5d39f62bbd39b116e8effa03e6ea0fa22c/.vscode/tasks.json
- https://github.com/cobour/neon-world/commit/53a4ab5d39f62bbd39b116e8effa03e6ea0fa22c
- https://cobour.itch.io/neonworld

### AI (no-evidence-found)

No explicit development-AI attribution found in inspected documentation, selected source/build files and head commit. Non-use is not inferred.
- https://github.com/cobour/neon-world/blob/53a4ab5d39f62bbd39b116e8effa03e6ea0fa22c/readme.md
- https://github.com/cobour/neon-world/blob/53a4ab5d39f62bbd39b116e8effa03e6ea0fa22c/_main.asm
- https://github.com/cobour/neon-world/blob/53a4ab5d39f62bbd39b116e8effa03e6ea0fa22c/.vscode/tasks.json
- https://github.com/cobour/neon-world/commit/53a4ab5d39f62bbd39b116e8effa03e6ea0fa22c
- https://cobour.itch.io/neonworld

### Relationships (reviewed)

Separate game from NEONnoir and from the author’s later Mutant Monty conversion. Third-party music, graphics, module player and inflater credits are retained upstream.
- https://github.com/cobour/neon-world/blob/53a4ab5d39f62bbd39b116e8effa03e6ea0fa22c/readme.md
- https://github.com/cobour/neon-world/blob/53a4ab5d39f62bbd39b116e8effa03e6ea0fa22c/_main.asm
- https://github.com/cobour/neon-world/blob/53a4ab5d39f62bbd39b116e8effa03e6ea0fa22c/.vscode/tasks.json
- https://github.com/cobour/neon-world/commit/53a4ab5d39f62bbd39b116e8effa03e6ea0fa22c
- https://cobour.itch.io/neonworld

## Gloom Reforged

Project ID: gloom-reforged-amiga · Overall audit: reviewed

### Typed catalogue values

```json
{
  "ai": {
    "tools": [],
    "usage": true
  },
  "build": {
    "byte_exact": null,
    "compilable": null,
    "playable": null,
    "runnable": null
  },
  "display_title": "Gloom Reforged",
  "id": "gloom-reforged-amiga",
  "last_activity": "2026-10-15",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "m68k assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/Andiweli/Gloom-Reforged",
  "runtime_profiles": [
    {
      "chipsets": [
        "ECS",
        "AGA"
      ],
      "cpu_family": "m68k",
      "evidence": [
        "https://github.com/Andiweli/Gloom-Reforged/blob/60c58f1fa901dff9235b2e05ad24c218bcc9d2d6/README.md"
      ],
      "name": "Documented display/OS family",
      "notes": "README supports ECS, AGA and P96. PiStorm or 68060 at 100 MHz is recommended for performance, not asserted as a minimum.",
      "os": "AmigaOS 3+",
      "platform": "Amiga"
    }
  ],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [
    "m68k assembly"
  ],
  "source_platforms": [
    "Amiga"
  ],
  "status": "Source reviewed; independent build/play test not performed",
  "subjects": [
    "Gloom Reforged"
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
  "title": "Gloom Reforged",
  "tool_kinds": [],
  "types": [
    "original-source restoration/enhancement"
  ],
  "upstream_name": "Gloom Reforged",
  "work_kinds": [
    "source-restoration",
    "patching"
  ]
}
```

### Identity (reviewed)

Enhanced native Amiga Gloom derived from released original source, with ECS/AGA/Picasso96 support, controls, rendering changes and bug fixes.
- https://github.com/Andiweli/Gloom-Reforged/blob/60c58f1fa901dff9235b2e05ad24c218bcc9d2d6/README.md
- https://github.com/Andiweli/Gloom-Reforged/blob/60c58f1fa901dff9235b2e05ad24c218bcc9d2d6/source/GloomReforged.s
- https://github.com/Andiweli/Gloom-Reforged/blob/60c58f1fa901dff9235b2e05ad24c218bcc9d2d6/LICENSE.md
- https://github.com/Andiweli/Gloom-Reforged/commit/60c58f1fa901dff9235b2e05ad24c218bcc9d2d6

### Classification (reviewed)

Original Amiga source preservation or a distinct native enhancement of it.
- https://github.com/Andiweli/Gloom-Reforged/blob/60c58f1fa901dff9235b2e05ad24c218bcc9d2d6/README.md
- https://github.com/Andiweli/Gloom-Reforged/blob/60c58f1fa901dff9235b2e05ad24c218bcc9d2d6/source/GloomReforged.s
- https://github.com/Andiweli/Gloom-Reforged/blob/60c58f1fa901dff9235b2e05ad24c218bcc9d2d6/LICENSE.md
- https://github.com/Andiweli/Gloom-Reforged/commit/60c58f1fa901dff9235b2e05ad24c218bcc9d2d6

### Source CPU (reviewed)

Inspected original source/build material identifies a classic Amiga m68k game lineage.
- https://github.com/Andiweli/Gloom-Reforged/blob/60c58f1fa901dff9235b2e05ad24c218bcc9d2d6/README.md
- https://github.com/Andiweli/Gloom-Reforged/blob/60c58f1fa901dff9235b2e05ad24c218bcc9d2d6/source/GloomReforged.s
- https://github.com/Andiweli/Gloom-Reforged/blob/60c58f1fa901dff9235b2e05ad24c218bcc9d2d6/LICENSE.md
- https://github.com/Andiweli/Gloom-Reforged/commit/60c58f1fa901dff9235b2e05ad24c218bcc9d2d6

### Target CPU (reviewed)

Native classic Amiga/m68k output is established by reviewed source/build declarations.
- https://github.com/Andiweli/Gloom-Reforged/blob/60c58f1fa901dff9235b2e05ad24c218bcc9d2d6/README.md
- https://github.com/Andiweli/Gloom-Reforged/blob/60c58f1fa901dff9235b2e05ad24c218bcc9d2d6/source/GloomReforged.s
- https://github.com/Andiweli/Gloom-Reforged/blob/60c58f1fa901dff9235b2e05ad24c218bcc9d2d6/LICENSE.md
- https://github.com/Andiweli/Gloom-Reforged/commit/60c58f1fa901dff9235b2e05ad24c218bcc9d2d6

### Build (reviewed)

Public repository contains native GloomReforged assembly and tools. README explicitly warns of increased CPU demand and recommends PiStorm or fast 68060; recommendation is not a measured minimum. Build/play/byte-exact flags remain unknown; no candidate software was executed.
- https://github.com/Andiweli/Gloom-Reforged/blob/60c58f1fa901dff9235b2e05ad24c218bcc9d2d6/README.md
- https://github.com/Andiweli/Gloom-Reforged/blob/60c58f1fa901dff9235b2e05ad24c218bcc9d2d6/source/GloomReforged.s
- https://github.com/Andiweli/Gloom-Reforged/blob/60c58f1fa901dff9235b2e05ad24c218bcc9d2d6/LICENSE.md
- https://github.com/Andiweli/Gloom-Reforged/commit/60c58f1fa901dff9235b2e05ad24c218bcc9d2d6

### Runtime profiles (reviewed)

README supports ECS, AGA and P96. PiStorm or 68060 at 100 MHz is recommended for performance, not asserted as a minimum.
- https://github.com/Andiweli/Gloom-Reforged/blob/60c58f1fa901dff9235b2e05ad24c218bcc9d2d6/README.md
- https://github.com/Andiweli/Gloom-Reforged/blob/60c58f1fa901dff9235b2e05ad24c218bcc9d2d6/source/GloomReforged.s
- https://github.com/Andiweli/Gloom-Reforged/blob/60c58f1fa901dff9235b2e05ad24c218bcc9d2d6/LICENSE.md
- https://github.com/Andiweli/Gloom-Reforged/commit/60c58f1fa901dff9235b2e05ad24c218bcc9d2d6

### AI (reviewed)

README explicitly displays an AI-Assisted Coding badge. No particular assistant/model is established by that badge.
- https://github.com/Andiweli/Gloom-Reforged/blob/60c58f1fa901dff9235b2e05ad24c218bcc9d2d6/README.md
- https://github.com/Andiweli/Gloom-Reforged/blob/60c58f1fa901dff9235b2e05ad24c218bcc9d2d6/source/GloomReforged.s
- https://github.com/Andiweli/Gloom-Reforged/blob/60c58f1fa901dff9235b2e05ad24c218bcc9d2d6/LICENSE.md
- https://github.com/Andiweli/Gloom-Reforged/commit/60c58f1fa901dff9235b2e05ad24c218bcc9d2d6

### Relationships (reviewed)

Distinct enhancement of already tracked earok/GloomAmiga, not its mirror. README announces paid itch.io distribution for v3 onward while v2.4.0 remains on Aminet; public repository inspection does not promise future paid releases will include source.
- https://github.com/Andiweli/Gloom-Reforged/blob/60c58f1fa901dff9235b2e05ad24c218bcc9d2d6/README.md
- https://github.com/Andiweli/Gloom-Reforged/blob/60c58f1fa901dff9235b2e05ad24c218bcc9d2d6/source/GloomReforged.s
- https://github.com/Andiweli/Gloom-Reforged/blob/60c58f1fa901dff9235b2e05ad24c218bcc9d2d6/LICENSE.md
- https://github.com/Andiweli/Gloom-Reforged/commit/60c58f1fa901dff9235b2e05ad24c218bcc9d2d6

## Breathless – Native Amiga Source Builds

Project ID: breathless-native-amiga-source · Overall audit: reviewed

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
  "display_title": "Breathless – Native Amiga Source Builds",
  "id": "breathless-native-amiga-source",
  "last_activity": "2023-11-09",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "m68k assembly",
    "C"
  ],
  "record_class": "subject",
  "repo": "https://github.com/mheyer32/Breathless",
  "runtime_profiles": [],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [
    "m68k assembly",
    "C"
  ],
  "source_platforms": [
    "Amiga"
  ],
  "status": "Source reviewed; independent build/play test not performed",
  "subjects": [
    "Breathless – Native Amiga Source Builds"
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
  "title": "Breathless – Native Amiga Source Builds",
  "tool_kinds": [],
  "types": [
    "original-source restoration/enhancement"
  ],
  "upstream_name": "Breathless – Native Amiga Source Builds",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

Native Amiga Breathless source tree with game/map-editor material and maintained assembler build variants.
- https://github.com/mheyer32/Breathless/blob/c82abc3d29486e62c717942899966a5759dcb434/Leggimi.txt
- https://github.com/mheyer32/Breathless/blob/c82abc3d29486e62c717942899966a5759dcb434/Sorgenti/Makefile
- https://github.com/mheyer32/Breathless/blob/c82abc3d29486e62c717942899966a5759dcb434/Sorgenti/Loader.asm
- https://github.com/mheyer32/Breathless/commit/c82abc3d29486e62c717942899966a5759dcb434

### Classification (reviewed)

Original Amiga source preservation or a distinct native enhancement of it.
- https://github.com/mheyer32/Breathless/blob/c82abc3d29486e62c717942899966a5759dcb434/Leggimi.txt
- https://github.com/mheyer32/Breathless/blob/c82abc3d29486e62c717942899966a5759dcb434/Sorgenti/Makefile
- https://github.com/mheyer32/Breathless/blob/c82abc3d29486e62c717942899966a5759dcb434/Sorgenti/Loader.asm
- https://github.com/mheyer32/Breathless/commit/c82abc3d29486e62c717942899966a5759dcb434

### Source CPU (reviewed)

Inspected original source/build material identifies a classic Amiga m68k game lineage.
- https://github.com/mheyer32/Breathless/blob/c82abc3d29486e62c717942899966a5759dcb434/Leggimi.txt
- https://github.com/mheyer32/Breathless/blob/c82abc3d29486e62c717942899966a5759dcb434/Sorgenti/Makefile
- https://github.com/mheyer32/Breathless/blob/c82abc3d29486e62c717942899966a5759dcb434/Sorgenti/Loader.asm
- https://github.com/mheyer32/Breathless/commit/c82abc3d29486e62c717942899966a5759dcb434

### Target CPU (reviewed)

Native classic Amiga/m68k output is established by reviewed source/build declarations.
- https://github.com/mheyer32/Breathless/blob/c82abc3d29486e62c717942899966a5759dcb434/Leggimi.txt
- https://github.com/mheyer32/Breathless/blob/c82abc3d29486e62c717942899966a5759dcb434/Sorgenti/Makefile
- https://github.com/mheyer32/Breathless/blob/c82abc3d29486e62c717942899966a5759dcb434/Sorgenti/Loader.asm
- https://github.com/mheyer32/Breathless/commit/c82abc3d29486e62c717942899966a5759dcb434

### Build (reviewed)

Reviewed Makefile uses vasm/vlink and m68k tools, with Breathless, Breathless060 and BreathlessLC060 outputs. Loader assembly and source layouts are present; no independent rebuild. Build/play/byte-exact flags remain unknown; no candidate software was executed.
- https://github.com/mheyer32/Breathless/blob/c82abc3d29486e62c717942899966a5759dcb434/Leggimi.txt
- https://github.com/mheyer32/Breathless/blob/c82abc3d29486e62c717942899966a5759dcb434/Sorgenti/Makefile
- https://github.com/mheyer32/Breathless/blob/c82abc3d29486e62c717942899966a5759dcb434/Sorgenti/Loader.asm
- https://github.com/mheyer32/Breathless/commit/c82abc3d29486e62c717942899966a5759dcb434

### Runtime profiles (no-evidence-found)

No complete minimum CPU/RAM/OS profile established from inspected material. Build tool settings and author performance recommendations are not automatically runtime minima.
- https://github.com/mheyer32/Breathless/blob/c82abc3d29486e62c717942899966a5759dcb434/Leggimi.txt
- https://github.com/mheyer32/Breathless/blob/c82abc3d29486e62c717942899966a5759dcb434/Sorgenti/Makefile
- https://github.com/mheyer32/Breathless/blob/c82abc3d29486e62c717942899966a5759dcb434/Sorgenti/Loader.asm
- https://github.com/mheyer32/Breathless/commit/c82abc3d29486e62c717942899966a5759dcb434

### AI (no-evidence-found)

No explicit development-AI attribution found in inspected documentation, selected source/build files and head commit. Non-use is not inferred.
- https://github.com/mheyer32/Breathless/blob/c82abc3d29486e62c717942899966a5759dcb434/Leggimi.txt
- https://github.com/mheyer32/Breathless/blob/c82abc3d29486e62c717942899966a5759dcb434/Sorgenti/Makefile
- https://github.com/mheyer32/Breathless/blob/c82abc3d29486e62c717942899966a5759dcb434/Sorgenti/Loader.asm
- https://github.com/mheyer32/Breathless/commit/c82abc3d29486e62c717942899966a5759dcb434

### Relationships (reviewed)

Separate from already tracked Fido666/Breathless SDL2/C port. Leggimi.txt carries restrictive historical distribution, noncommercial-use and player-component notices; source availability must not be equated with a permissive open-source licence.
- https://github.com/mheyer32/Breathless/blob/c82abc3d29486e62c717942899966a5759dcb434/Leggimi.txt
- https://github.com/mheyer32/Breathless/blob/c82abc3d29486e62c717942899966a5759dcb434/Sorgenti/Makefile
- https://github.com/mheyer32/Breathless/blob/c82abc3d29486e62c717942899966a5759dcb434/Sorgenti/Loader.asm
- https://github.com/mheyer32/Breathless/commit/c82abc3d29486e62c717942899966a5759dcb434

## Alien Breed 3D RTG

Project ID: alien-breed-3d-rtg-amiga · Overall audit: reviewed

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
  "display_title": "Alien Breed 3D RTG",
  "id": "alien-breed-3d-rtg-amiga",
  "last_activity": "2022-08-06",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "m68k assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/mheyer32/ab3d-rtg",
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
  "status": "Source reviewed; independent build/play test not performed",
  "subjects": [
    "Alien Breed 3D RTG"
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
  "title": "Alien Breed 3D RTG",
  "tool_kinds": [],
  "types": [
    "original-source restoration/enhancement"
  ],
  "upstream_name": "Alien Breed 3D RTG",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

Native Amiga RTG adaptation of Alien Breed 3D based on John Girvin’s earlier source work.
- https://github.com/mheyer32/ab3d-rtg/blob/c135c175a55d26238efebcc52e9382c61bcd6fe8/readme.md
- https://github.com/mheyer32/ab3d-rtg/blob/c135c175a55d26238efebcc52e9382c61bcd6fe8/newsource/Makefile
- https://github.com/mheyer32/ab3d-rtg/blob/c135c175a55d26238efebcc52e9382c61bcd6fe8/newsource/main.s
- https://github.com/mheyer32/ab3d-rtg/commit/c135c175a55d26238efebcc52e9382c61bcd6fe8

### Classification (reviewed)

Original Amiga source preservation or a distinct native enhancement of it.
- https://github.com/mheyer32/ab3d-rtg/blob/c135c175a55d26238efebcc52e9382c61bcd6fe8/readme.md
- https://github.com/mheyer32/ab3d-rtg/blob/c135c175a55d26238efebcc52e9382c61bcd6fe8/newsource/Makefile
- https://github.com/mheyer32/ab3d-rtg/blob/c135c175a55d26238efebcc52e9382c61bcd6fe8/newsource/main.s
- https://github.com/mheyer32/ab3d-rtg/commit/c135c175a55d26238efebcc52e9382c61bcd6fe8

### Source CPU (reviewed)

Inspected original source/build material identifies a classic Amiga m68k game lineage.
- https://github.com/mheyer32/ab3d-rtg/blob/c135c175a55d26238efebcc52e9382c61bcd6fe8/readme.md
- https://github.com/mheyer32/ab3d-rtg/blob/c135c175a55d26238efebcc52e9382c61bcd6fe8/newsource/Makefile
- https://github.com/mheyer32/ab3d-rtg/blob/c135c175a55d26238efebcc52e9382c61bcd6fe8/newsource/main.s
- https://github.com/mheyer32/ab3d-rtg/commit/c135c175a55d26238efebcc52e9382c61bcd6fe8

### Target CPU (reviewed)

Native classic Amiga/m68k output is established by reviewed source/build declarations.
- https://github.com/mheyer32/ab3d-rtg/blob/c135c175a55d26238efebcc52e9382c61bcd6fe8/readme.md
- https://github.com/mheyer32/ab3d-rtg/blob/c135c175a55d26238efebcc52e9382c61bcd6fe8/newsource/Makefile
- https://github.com/mheyer32/ab3d-rtg/blob/c135c175a55d26238efebcc52e9382c61bcd6fe8/newsource/main.s
- https://github.com/mheyer32/ab3d-rtg/commit/c135c175a55d26238efebcc52e9382c61bcd6fe8

### Build (reviewed)

newsource Makefile uses vasm/vlink, rtgmaster headers and Amiga includes. Native main.s retains 68020-era source settings while the build enables 68060 instructions; exact minimum compatibility is not inferred. Build/play/byte-exact flags remain unknown; no candidate software was executed.
- https://github.com/mheyer32/ab3d-rtg/blob/c135c175a55d26238efebcc52e9382c61bcd6fe8/readme.md
- https://github.com/mheyer32/ab3d-rtg/blob/c135c175a55d26238efebcc52e9382c61bcd6fe8/newsource/Makefile
- https://github.com/mheyer32/ab3d-rtg/blob/c135c175a55d26238efebcc52e9382c61bcd6fe8/newsource/main.s
- https://github.com/mheyer32/ab3d-rtg/commit/c135c175a55d26238efebcc52e9382c61bcd6fe8

### Runtime profiles (no-evidence-found)

No complete minimum CPU/RAM/OS profile established from inspected material. Build tool settings and author performance recommendations are not automatically runtime minima.
- https://github.com/mheyer32/ab3d-rtg/blob/c135c175a55d26238efebcc52e9382c61bcd6fe8/readme.md
- https://github.com/mheyer32/ab3d-rtg/blob/c135c175a55d26238efebcc52e9382c61bcd6fe8/newsource/Makefile
- https://github.com/mheyer32/ab3d-rtg/blob/c135c175a55d26238efebcc52e9382c61bcd6fe8/newsource/main.s
- https://github.com/mheyer32/ab3d-rtg/commit/c135c175a55d26238efebcc52e9382c61bcd6fe8

### AI (no-evidence-found)

No explicit development-AI attribution found in inspected documentation, selected source/build files and head commit. Non-use is not inferred.
- https://github.com/mheyer32/ab3d-rtg/blob/c135c175a55d26238efebcc52e9382c61bcd6fe8/readme.md
- https://github.com/mheyer32/ab3d-rtg/blob/c135c175a55d26238efebcc52e9382c61bcd6fe8/newsource/Makefile
- https://github.com/mheyer32/ab3d-rtg/blob/c135c175a55d26238efebcc52e9382c61bcd6fe8/newsource/main.s
- https://github.com/mheyer32/ab3d-rtg/commit/c135c175a55d26238efebcc52e9382c61bcd6fe8

### Relationships (reviewed)

Alien Breed 3D I RTG project is distinct from the original source bundled with AB3D2 and from already tracked retro-foundry/Alien-Breed-HD PC output.
- https://github.com/mheyer32/ab3d-rtg/blob/c135c175a55d26238efebcc52e9382c61bcd6fe8/readme.md
- https://github.com/mheyer32/ab3d-rtg/blob/c135c175a55d26238efebcc52e9382c61bcd6fe8/newsource/Makefile
- https://github.com/mheyer32/ab3d-rtg/blob/c135c175a55d26238efebcc52e9382c61bcd6fe8/newsource/main.s
- https://github.com/mheyer32/ab3d-rtg/commit/c135c175a55d26238efebcc52e9382c61bcd6fe8

## Alien Breed 3D II Rebuilt

Project ID: alien-breed-3d2-rebuilt-amiga · Overall audit: reviewed

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
  "display_title": "Alien Breed 3D II Rebuilt",
  "id": "alien-breed-3d2-rebuilt-amiga",
  "last_activity": "2026-09-13",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "m68k assembly",
    "C"
  ],
  "record_class": "subject",
  "repo": "https://github.com/mheyer32/alienbreed3d2",
  "runtime_profiles": [
    {
      "chipsets": [
        "ECS",
        "AGA"
      ],
      "cpu_family": "m68k",
      "evidence": [
        "https://github.com/mheyer32/alienbreed3d2/blob/86abb5c5b28cbab874e46b96c94b93b51bff56ec/README.md"
      ],
      "name": "Documented graphics support",
      "notes": "README reports ECS/AGA and RTG support with 256-colour 320x240 or 320x256 screenmode; native chipset is still used by menus. Build flavours are 030/040/060, not proof of a minimum RAM configuration.",
      "platform": "Amiga"
    }
  ],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [
    "m68k assembly",
    "C"
  ],
  "source_platforms": [
    "Amiga"
  ],
  "status": "Source reviewed; independent build/play test not performed",
  "subjects": [
    "Alien Breed 3D II Rebuilt"
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
  "title": "Alien Breed 3D II Rebuilt",
  "tool_kinds": [],
  "types": [
    "original-source restoration/enhancement"
  ],
  "upstream_name": "Alien Breed 3D II Rebuilt",
  "work_kinds": [
    "source-restoration",
    "patching"
  ]
}
```

### Identity (reviewed)

Maintained native Amiga engine reconstruction from released Alien Breed 3D II source, with bug/performance fixes, Workbench return, RTG and mod support.
- https://github.com/mheyer32/alienbreed3d2/blob/86abb5c5b28cbab874e46b96c94b93b51bff56ec/README.md
- https://github.com/mheyer32/alienbreed3d2/blob/86abb5c5b28cbab874e46b96c94b93b51bff56ec/ab3d2_source/Makefile
- https://github.com/mheyer32/alienbreed3d2/blob/86abb5c5b28cbab874e46b96c94b93b51bff56ec/ab3d2_source/c/main.c
- https://github.com/mheyer32/alienbreed3d2/blob/86abb5c5b28cbab874e46b96c94b93b51bff56ec/ab3d2_source/docs/README.md
- https://github.com/mheyer32/alienbreed3d2/commit/86abb5c5b28cbab874e46b96c94b93b51bff56ec

### Classification (reviewed)

Original Amiga source preservation or a distinct native enhancement of it.
- https://github.com/mheyer32/alienbreed3d2/blob/86abb5c5b28cbab874e46b96c94b93b51bff56ec/README.md
- https://github.com/mheyer32/alienbreed3d2/blob/86abb5c5b28cbab874e46b96c94b93b51bff56ec/ab3d2_source/Makefile
- https://github.com/mheyer32/alienbreed3d2/blob/86abb5c5b28cbab874e46b96c94b93b51bff56ec/ab3d2_source/c/main.c
- https://github.com/mheyer32/alienbreed3d2/blob/86abb5c5b28cbab874e46b96c94b93b51bff56ec/ab3d2_source/docs/README.md
- https://github.com/mheyer32/alienbreed3d2/commit/86abb5c5b28cbab874e46b96c94b93b51bff56ec

### Source CPU (reviewed)

Inspected original source/build material identifies a classic Amiga m68k game lineage.
- https://github.com/mheyer32/alienbreed3d2/blob/86abb5c5b28cbab874e46b96c94b93b51bff56ec/README.md
- https://github.com/mheyer32/alienbreed3d2/blob/86abb5c5b28cbab874e46b96c94b93b51bff56ec/ab3d2_source/Makefile
- https://github.com/mheyer32/alienbreed3d2/blob/86abb5c5b28cbab874e46b96c94b93b51bff56ec/ab3d2_source/c/main.c
- https://github.com/mheyer32/alienbreed3d2/blob/86abb5c5b28cbab874e46b96c94b93b51bff56ec/ab3d2_source/docs/README.md
- https://github.com/mheyer32/alienbreed3d2/commit/86abb5c5b28cbab874e46b96c94b93b51bff56ec

### Target CPU (reviewed)

Native classic Amiga/m68k output is established by reviewed source/build declarations.
- https://github.com/mheyer32/alienbreed3d2/blob/86abb5c5b28cbab874e46b96c94b93b51bff56ec/README.md
- https://github.com/mheyer32/alienbreed3d2/blob/86abb5c5b28cbab874e46b96c94b93b51bff56ec/ab3d2_source/Makefile
- https://github.com/mheyer32/alienbreed3d2/blob/86abb5c5b28cbab874e46b96c94b93b51bff56ec/ab3d2_source/c/main.c
- https://github.com/mheyer32/alienbreed3d2/blob/86abb5c5b28cbab874e46b96c94b93b51bff56ec/ab3d2_source/docs/README.md
- https://github.com/mheyer32/alienbreed3d2/commit/86abb5c5b28cbab874e46b96c94b93b51bff56ec

### Build (reviewed)

Makefile provides 030/040/060 build flavours using m68k GCC and vasm; native C/assembly and development docs are present. README describes release packages for original game data and compatible mods; independently unbuilt. Build/play/byte-exact flags remain unknown; no candidate software was executed.
- https://github.com/mheyer32/alienbreed3d2/blob/86abb5c5b28cbab874e46b96c94b93b51bff56ec/README.md
- https://github.com/mheyer32/alienbreed3d2/blob/86abb5c5b28cbab874e46b96c94b93b51bff56ec/ab3d2_source/Makefile
- https://github.com/mheyer32/alienbreed3d2/blob/86abb5c5b28cbab874e46b96c94b93b51bff56ec/ab3d2_source/c/main.c
- https://github.com/mheyer32/alienbreed3d2/blob/86abb5c5b28cbab874e46b96c94b93b51bff56ec/ab3d2_source/docs/README.md
- https://github.com/mheyer32/alienbreed3d2/commit/86abb5c5b28cbab874e46b96c94b93b51bff56ec

### Runtime profiles (reviewed)

README reports ECS/AGA and RTG support with 256-colour 320x240 or 320x256 screenmode; native chipset is still used by menus. Build flavours are 030/040/060, not proof of a minimum RAM configuration.
- https://github.com/mheyer32/alienbreed3d2/blob/86abb5c5b28cbab874e46b96c94b93b51bff56ec/README.md
- https://github.com/mheyer32/alienbreed3d2/blob/86abb5c5b28cbab874e46b96c94b93b51bff56ec/ab3d2_source/Makefile
- https://github.com/mheyer32/alienbreed3d2/blob/86abb5c5b28cbab874e46b96c94b93b51bff56ec/ab3d2_source/c/main.c
- https://github.com/mheyer32/alienbreed3d2/blob/86abb5c5b28cbab874e46b96c94b93b51bff56ec/ab3d2_source/docs/README.md
- https://github.com/mheyer32/alienbreed3d2/commit/86abb5c5b28cbab874e46b96c94b93b51bff56ec

### AI (no-evidence-found)

No explicit development-AI attribution found in inspected documentation, selected source/build files and head commit. Non-use is not inferred.
- https://github.com/mheyer32/alienbreed3d2/blob/86abb5c5b28cbab874e46b96c94b93b51bff56ec/README.md
- https://github.com/mheyer32/alienbreed3d2/blob/86abb5c5b28cbab874e46b96c94b93b51bff56ec/ab3d2_source/Makefile
- https://github.com/mheyer32/alienbreed3d2/blob/86abb5c5b28cbab874e46b96c94b93b51bff56ec/ab3d2_source/c/main.c
- https://github.com/mheyer32/alienbreed3d2/blob/86abb5c5b28cbab874e46b96c94b93b51bff56ec/ab3d2_source/docs/README.md
- https://github.com/mheyer32/alienbreed3d2/commit/86abb5c5b28cbab874e46b96c94b93b51bff56ec

### Relationships (reviewed)

Rebuilt is the engine project; Redux/Karlos TKG is a separate content modification that uses it. Native chipset remains needed for menus even with RTG, according to README.
- https://github.com/mheyer32/alienbreed3d2/blob/86abb5c5b28cbab874e46b96c94b93b51bff56ec/README.md
- https://github.com/mheyer32/alienbreed3d2/blob/86abb5c5b28cbab874e46b96c94b93b51bff56ec/ab3d2_source/Makefile
- https://github.com/mheyer32/alienbreed3d2/blob/86abb5c5b28cbab874e46b96c94b93b51bff56ec/ab3d2_source/c/main.c
- https://github.com/mheyer32/alienbreed3d2/blob/86abb5c5b28cbab874e46b96c94b93b51bff56ec/ab3d2_source/docs/README.md
- https://github.com/mheyer32/alienbreed3d2/commit/86abb5c5b28cbab874e46b96c94b93b51bff56ec

## High Octane – Original Amiga Sources

Project ID: high-octane-original-amiga · Overall audit: reviewed

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
  "display_title": "High Octane – Original Amiga Sources",
  "id": "high-octane-original-amiga",
  "last_activity": "2026-01-15",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "AMOS BASIC"
  ],
  "record_class": "subject",
  "repo": "https://github.com/titmouse001/Amiga-Archive-For-My-Old-Stuff",
  "runtime_profiles": [],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [
    "AMOS BASIC"
  ],
  "source_platforms": [
    "Amiga"
  ],
  "status": "Source reviewed; independent build/play test not performed",
  "subjects": [
    "High Octane – Original Amiga Sources"
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
  "title": "High Octane – Original Amiga Sources",
  "tool_kinds": [],
  "types": [
    "original-source restoration/enhancement"
  ],
  "upstream_name": "High Octane – Original Amiga Sources",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

Author’s recovered AMOS sources for the original High Octane driving game, with map editor, assets and contemporary publication material.
- https://github.com/titmouse001/Amiga-Archive-For-My-Old-Stuff/blob/fc2524969bc7da5f76aef9fd13bba956c063d843/README.md
- https://github.com/titmouse001/Amiga-Archive-For-My-Old-Stuff/blob/fc2524969bc7da5f76aef9fd13bba956c063d843/HO_Source/High_Octane/high_octane.amos
- https://github.com/titmouse001/Amiga-Archive-For-My-Old-Stuff/commit/fc2524969bc7da5f76aef9fd13bba956c063d843

### Classification (reviewed)

Original Amiga source preservation or a distinct native enhancement of it.
- https://github.com/titmouse001/Amiga-Archive-For-My-Old-Stuff/blob/fc2524969bc7da5f76aef9fd13bba956c063d843/README.md
- https://github.com/titmouse001/Amiga-Archive-For-My-Old-Stuff/blob/fc2524969bc7da5f76aef9fd13bba956c063d843/HO_Source/High_Octane/high_octane.amos
- https://github.com/titmouse001/Amiga-Archive-For-My-Old-Stuff/commit/fc2524969bc7da5f76aef9fd13bba956c063d843

### Source CPU (reviewed)

Inspected original source/build material identifies a classic Amiga m68k game lineage.
- https://github.com/titmouse001/Amiga-Archive-For-My-Old-Stuff/blob/fc2524969bc7da5f76aef9fd13bba956c063d843/README.md
- https://github.com/titmouse001/Amiga-Archive-For-My-Old-Stuff/blob/fc2524969bc7da5f76aef9fd13bba956c063d843/HO_Source/High_Octane/high_octane.amos
- https://github.com/titmouse001/Amiga-Archive-For-My-Old-Stuff/commit/fc2524969bc7da5f76aef9fd13bba956c063d843

### Target CPU (reviewed)

Native classic Amiga/m68k output is established by reviewed source/build declarations.
- https://github.com/titmouse001/Amiga-Archive-For-My-Old-Stuff/blob/fc2524969bc7da5f76aef9fd13bba956c063d843/README.md
- https://github.com/titmouse001/Amiga-Archive-For-My-Old-Stuff/blob/fc2524969bc7da5f76aef9fd13bba956c063d843/HO_Source/High_Octane/high_octane.amos
- https://github.com/titmouse001/Amiga-Archive-For-My-Old-Stuff/commit/fc2524969bc7da5f76aef9fd13bba956c063d843

### Build (reviewed)

The .amos game source has an AMOS Basic V1.3 header; tokenized source is not an opaque machine-code executable. Map-editor and compatibility sources accompany it. No rebuild performed. Build/play/byte-exact flags remain unknown; no candidate software was executed.
- https://github.com/titmouse001/Amiga-Archive-For-My-Old-Stuff/blob/fc2524969bc7da5f76aef9fd13bba956c063d843/README.md
- https://github.com/titmouse001/Amiga-Archive-For-My-Old-Stuff/blob/fc2524969bc7da5f76aef9fd13bba956c063d843/HO_Source/High_Octane/high_octane.amos
- https://github.com/titmouse001/Amiga-Archive-For-My-Old-Stuff/commit/fc2524969bc7da5f76aef9fd13bba956c063d843

### Runtime profiles (no-evidence-found)

No complete minimum CPU/RAM/OS profile established from inspected material. Build tool settings and author performance recommendations are not automatically runtime minima.
- https://github.com/titmouse001/Amiga-Archive-For-My-Old-Stuff/blob/fc2524969bc7da5f76aef9fd13bba956c063d843/README.md
- https://github.com/titmouse001/Amiga-Archive-For-My-Old-Stuff/blob/fc2524969bc7da5f76aef9fd13bba956c063d843/HO_Source/High_Octane/high_octane.amos
- https://github.com/titmouse001/Amiga-Archive-For-My-Old-Stuff/commit/fc2524969bc7da5f76aef9fd13bba956c063d843

### AI (no-evidence-found)

No explicit development-AI attribution found in inspected documentation, selected source/build files and head commit. Non-use is not inferred.
- https://github.com/titmouse001/Amiga-Archive-For-My-Old-Stuff/blob/fc2524969bc7da5f76aef9fd13bba956c063d843/README.md
- https://github.com/titmouse001/Amiga-Archive-For-My-Old-Stuff/blob/fc2524969bc7da5f76aef9fd13bba956c063d843/HO_Source/High_Octane/high_octane.amos
- https://github.com/titmouse001/Amiga-Archive-For-My-Old-Stuff/commit/fc2524969bc7da5f76aef9fd13bba956c063d843

### Relationships (reviewed)

Original High Octane, distinct from already tracked Amiga-HighOctane2/UltimateOctane. Repository root is mainly this coherent recovered project, so no unnecessary sub-path entry.
- https://github.com/titmouse001/Amiga-Archive-For-My-Old-Stuff/blob/fc2524969bc7da5f76aef9fd13bba956c063d843/README.md
- https://github.com/titmouse001/Amiga-Archive-For-My-Old-Stuff/blob/fc2524969bc7da5f76aef9fd13bba956c063d843/HO_Source/High_Octane/high_octane.amos
- https://github.com/titmouse001/Amiga-Archive-For-My-Old-Stuff/commit/fc2524969bc7da5f76aef9fd13bba956c063d843

## Alien Breed 3D II Redux (Karlos TKG)

Project ID: alien-breed-3d2-redux · Overall audit: reviewed

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
  "display_title": "Alien Breed 3D II Redux (Karlos TKG)",
  "id": "alien-breed-3d2-redux",
  "last_activity": "2026-06-21",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "Game/editor data"
  ],
  "record_class": "subject",
  "repo": "https://github.com/0xABADCAFE/karlos-tkg",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [
    "Amiga"
  ],
  "status": "Source reviewed; independent build/play test not performed",
  "subjects": [
    "Alien Breed 3D II Redux (Karlos TKG)"
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
  "title": "Alien Breed 3D II Redux (Karlos TKG)",
  "tool_kinds": [],
  "types": [
    "game-content modification"
  ],
  "upstream_name": "Alien Breed 3D II Redux (Karlos TKG)",
  "work_kinds": []
}
```

### Identity (reviewed)

Work-in-progress reimagining of Alien Breed 3D II with expanded textures, lighting, enemies, sounds, weapons and inventory rules.
- https://github.com/0xABADCAFE/karlos-tkg/blob/09d84a05f6811ff055279c50e6a70dacbf4825b8/README.md
- https://github.com/0xABADCAFE/karlos-tkg/blob/09d84a05f6811ff055279c50e6a70dacbf4825b8/Editor/Assets/TKGD/Make.sh
- https://github.com/0xABADCAFE/karlos-tkg/commit/09d84a05f6811ff055279c50e6a70dacbf4825b8

### Classification (reviewed)

Game/editor content modification for a separately maintained engine.
- https://github.com/0xABADCAFE/karlos-tkg/blob/09d84a05f6811ff055279c50e6a70dacbf4825b8/README.md
- https://github.com/0xABADCAFE/karlos-tkg/blob/09d84a05f6811ff055279c50e6a70dacbf4825b8/Editor/Assets/TKGD/Make.sh
- https://github.com/0xABADCAFE/karlos-tkg/commit/09d84a05f6811ff055279c50e6a70dacbf4825b8

### Source CPU (not-applicable)

Content entry consists of game/editor data rather than recovered CPU-specific code; source CPU stays empty.
- https://github.com/0xABADCAFE/karlos-tkg/blob/09d84a05f6811ff055279c50e6a70dacbf4825b8/README.md
- https://github.com/0xABADCAFE/karlos-tkg/blob/09d84a05f6811ff055279c50e6a70dacbf4825b8/Editor/Assets/TKGD/Make.sh
- https://github.com/0xABADCAFE/karlos-tkg/commit/09d84a05f6811ff055279c50e6a70dacbf4825b8

### Target CPU (reviewed)

Mod runs on the native Amiga/m68k Rebuilt engine documented by the author, not on a host-side editor.
- https://github.com/0xABADCAFE/karlos-tkg/blob/09d84a05f6811ff055279c50e6a70dacbf4825b8/README.md
- https://github.com/0xABADCAFE/karlos-tkg/blob/09d84a05f6811ff055279c50e6a70dacbf4825b8/Editor/Assets/TKGD/Make.sh
- https://github.com/0xABADCAFE/karlos-tkg/commit/09d84a05f6811ff055279c50e6a70dacbf4825b8

### Build (reviewed)

Repository supplies editable game/editor assets and ships the separately maintained Rebuilt engine. README documents Amiga/UAE startup and use of an improved LevelEd; this is not a second independent engine implementation. Build/play/byte-exact flags remain unknown; no candidate software was executed.
- https://github.com/0xABADCAFE/karlos-tkg/blob/09d84a05f6811ff055279c50e6a70dacbf4825b8/README.md
- https://github.com/0xABADCAFE/karlos-tkg/blob/09d84a05f6811ff055279c50e6a70dacbf4825b8/Editor/Assets/TKGD/Make.sh
- https://github.com/0xABADCAFE/karlos-tkg/commit/09d84a05f6811ff055279c50e6a70dacbf4825b8

### Runtime profiles (no-evidence-found)

No complete minimum CPU/RAM/OS profile established from inspected material. Build tool settings and author performance recommendations are not automatically runtime minima.
- https://github.com/0xABADCAFE/karlos-tkg/blob/09d84a05f6811ff055279c50e6a70dacbf4825b8/README.md
- https://github.com/0xABADCAFE/karlos-tkg/blob/09d84a05f6811ff055279c50e6a70dacbf4825b8/Editor/Assets/TKGD/Make.sh
- https://github.com/0xABADCAFE/karlos-tkg/commit/09d84a05f6811ff055279c50e6a70dacbf4825b8

### AI (no-evidence-found)

No explicit development-AI attribution found in inspected documentation, selected source/build files and head commit. Non-use is not inferred.
- https://github.com/0xABADCAFE/karlos-tkg/blob/09d84a05f6811ff055279c50e6a70dacbf4825b8/README.md
- https://github.com/0xABADCAFE/karlos-tkg/blob/09d84a05f6811ff055279c50e6a70dacbf4825b8/Editor/Assets/TKGD/Make.sh
- https://github.com/0xABADCAFE/karlos-tkg/commit/09d84a05f6811ff055279c50e6a70dacbf4825b8

### Relationships (reviewed)

Distinct game-content modification using mheyer32/alienbreed3d2. Keep mod and engine identities separate; no new machine-code reconstruction is claimed by this content entry.
- https://github.com/0xABADCAFE/karlos-tkg/blob/09d84a05f6811ff055279c50e6a70dacbf4825b8/README.md
- https://github.com/0xABADCAFE/karlos-tkg/blob/09d84a05f6811ff055279c50e6a70dacbf4825b8/Editor/Assets/TKGD/Make.sh
- https://github.com/0xABADCAFE/karlos-tkg/commit/09d84a05f6811ff055279c50e6a70dacbf4825b8

## Sources

```json
[
  {
    "id": "github-steamknight-neonnoir",
    "kind": "github-repository",
    "reason": "Cyberpunk point-and-click adventure/visual novel for Amiga 1200, created for the Amiga Blitz Basic Game Jam.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/steamknight/NEONnoir"
  },
  {
    "id": "github-nitrologic-acidpd",
    "kind": "github-repository",
    "reason": "Acid Software collection of Amiga public-domain games, containing untokenized Blitz2 sources in many cases.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/nitrologic/acidpd"
  },
  {
    "id": "github-hlsyounes-lazymines",
    "kind": "github-repository",
    "reason": "Native Amiga Minesweeper game with preserved source headers dating to 1993–1994.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/hlsyounes/lazymines"
  },
  {
    "id": "github-cobour-neon-world",
    "kind": "github-repository",
    "reason": "PAL Amiga horizontal shooter developed as an A500 assembly project, with level/enemy tooling and public game sources.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/cobour/neon-world"
  },
  {
    "id": "github-andiweli-gloom-reforged",
    "kind": "github-repository",
    "reason": "Enhanced native Amiga Gloom derived from released original source, with ECS/AGA/Picasso96 support, controls, rendering changes and bug fixes.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/Andiweli/Gloom-Reforged"
  },
  {
    "id": "github-mheyer32-breathless",
    "kind": "github-repository",
    "reason": "Native Amiga Breathless source tree with game/map-editor material and maintained assembler build variants.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/mheyer32/Breathless"
  },
  {
    "id": "github-mheyer32-ab3d-rtg",
    "kind": "github-repository",
    "reason": "Native Amiga RTG adaptation of Alien Breed 3D based on John Girvin’s earlier source work.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/mheyer32/ab3d-rtg"
  },
  {
    "id": "github-mheyer32-alienbreed3d2",
    "kind": "github-repository",
    "reason": "Maintained native Amiga engine reconstruction from released Alien Breed 3D II source, with bug/performance fixes, Workbench return, RTG and mod support.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/mheyer32/alienbreed3d2"
  },
  {
    "id": "github-titmouse001-amiga-archive-for-my-old-stuff",
    "kind": "github-repository",
    "reason": "Author’s recovered AMOS sources for the original High Octane driving game, with map editor, assets and contemporary publication material.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/titmouse001/Amiga-Archive-For-My-Old-Stuff"
  },
  {
    "id": "github-0xabadcafe-karlos-tkg",
    "kind": "github-repository",
    "reason": "Work-in-progress reimagining of Alien Breed 3D II with expanded textures, lighting, enemies, sounds, weapons and inventory rules.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/0xABADCAFE/karlos-tkg"
  }
]
```

## Decisions

```json
[
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/steamknight/NEONnoir/blob/3a702ba85105169f61196a7a924533dc3fba667e/README.md",
      "https://github.com/steamknight/NEONnoir/blob/3a702ba85105169f61196a7a924533dc3fba667e/src/NN_main.bb2",
      "https://github.com/steamknight/NEONnoir/blob/3a702ba85105169f61196a7a924533dc3fba667e/build.ps1",
      "https://github.com/steamknight/NEONnoir/commit/3a702ba85105169f61196a7a924533dc3fba667e",
      "https://steamknight.itch.io/neonnoir"
    ],
    "id": "2026-10-17-promote-neonnoir-amiga",
    "project_ids": [
      "neonnoir-amiga"
    ],
    "reason": "Cyberpunk point-and-click adventure/visual novel for Amiga 1200, created for the Amiga Blitz Basic Game Jam.",
    "source_ids": [
      "github-steamknight-neonnoir"
    ],
    "title": "NEONnoir",
    "url": "https://github.com/steamknight/NEONnoir"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/nitrologic/acidpd/blob/87a024d4f32938093e519191588ff0a29228f7af/README.md",
      "https://github.com/nitrologic/acidpd/blob/87a024d4f32938093e519191588ff0a29228f7af/defender/defender.src",
      "https://github.com/nitrologic/acidpd/blob/87a024d4f32938093e519191588ff0a29228f7af/AboutBlitz2.txt",
      "https://github.com/nitrologic/acidpd/commit/87a024d4f32938093e519191588ff0a29228f7af"
    ],
    "id": "2026-10-17-promote-acid-software-pd-game-sources",
    "project_ids": [
      "acid-software-pd-game-sources"
    ],
    "reason": "Acid Software collection of Amiga public-domain games, containing untokenized Blitz2 sources in many cases.",
    "source_ids": [
      "github-nitrologic-acidpd"
    ],
    "title": "Acid Software Public Domain Game Sources",
    "url": "https://github.com/nitrologic/acidpd"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/hlsyounes/lazymines/blob/0553ded221a62c012934f5f6a322a5293637b121/Minesweeper.c",
      "https://github.com/hlsyounes/lazymines/blob/0553ded221a62c012934f5f6a322a5293637b121/field.c",
      "https://github.com/hlsyounes/lazymines/blob/0553ded221a62c012934f5f6a322a5293637b121/Smakefile",
      "https://github.com/hlsyounes/lazymines/commit/0553ded221a62c012934f5f6a322a5293637b121"
    ],
    "id": "2026-10-17-promote-lazymines-amiga",
    "project_ids": [
      "lazymines-amiga"
    ],
    "reason": "Native Amiga Minesweeper game with preserved source headers dating to 1993–1994.",
    "source_ids": [
      "github-hlsyounes-lazymines"
    ],
    "title": "LazyMines",
    "url": "https://github.com/hlsyounes/lazymines"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/cobour/neon-world/blob/53a4ab5d39f62bbd39b116e8effa03e6ea0fa22c/readme.md",
      "https://github.com/cobour/neon-world/blob/53a4ab5d39f62bbd39b116e8effa03e6ea0fa22c/_main.asm",
      "https://github.com/cobour/neon-world/blob/53a4ab5d39f62bbd39b116e8effa03e6ea0fa22c/.vscode/tasks.json",
      "https://github.com/cobour/neon-world/commit/53a4ab5d39f62bbd39b116e8effa03e6ea0fa22c",
      "https://cobour.itch.io/neonworld"
    ],
    "id": "2026-10-17-promote-neonworld-amiga",
    "project_ids": [
      "neonworld-amiga"
    ],
    "reason": "PAL Amiga horizontal shooter developed as an A500 assembly project, with level/enemy tooling and public game sources.",
    "source_ids": [
      "github-cobour-neon-world"
    ],
    "title": "NeonWorld",
    "url": "https://github.com/cobour/neon-world"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/Andiweli/Gloom-Reforged/blob/60c58f1fa901dff9235b2e05ad24c218bcc9d2d6/README.md",
      "https://github.com/Andiweli/Gloom-Reforged/blob/60c58f1fa901dff9235b2e05ad24c218bcc9d2d6/source/GloomReforged.s",
      "https://github.com/Andiweli/Gloom-Reforged/blob/60c58f1fa901dff9235b2e05ad24c218bcc9d2d6/LICENSE.md",
      "https://github.com/Andiweli/Gloom-Reforged/commit/60c58f1fa901dff9235b2e05ad24c218bcc9d2d6"
    ],
    "id": "2026-10-17-promote-gloom-reforged-amiga",
    "project_ids": [
      "gloom-reforged-amiga"
    ],
    "reason": "Enhanced native Amiga Gloom derived from released original source, with ECS/AGA/Picasso96 support, controls, rendering changes and bug fixes.",
    "source_ids": [
      "github-andiweli-gloom-reforged"
    ],
    "title": "Gloom Reforged",
    "url": "https://github.com/Andiweli/Gloom-Reforged"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/mheyer32/Breathless/blob/c82abc3d29486e62c717942899966a5759dcb434/Leggimi.txt",
      "https://github.com/mheyer32/Breathless/blob/c82abc3d29486e62c717942899966a5759dcb434/Sorgenti/Makefile",
      "https://github.com/mheyer32/Breathless/blob/c82abc3d29486e62c717942899966a5759dcb434/Sorgenti/Loader.asm",
      "https://github.com/mheyer32/Breathless/commit/c82abc3d29486e62c717942899966a5759dcb434"
    ],
    "id": "2026-10-17-promote-breathless-native-amiga-source",
    "project_ids": [
      "breathless-native-amiga-source"
    ],
    "reason": "Native Amiga Breathless source tree with game/map-editor material and maintained assembler build variants.",
    "source_ids": [
      "github-mheyer32-breathless"
    ],
    "title": "Breathless – Native Amiga Source Builds",
    "url": "https://github.com/mheyer32/Breathless"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/mheyer32/ab3d-rtg/blob/c135c175a55d26238efebcc52e9382c61bcd6fe8/readme.md",
      "https://github.com/mheyer32/ab3d-rtg/blob/c135c175a55d26238efebcc52e9382c61bcd6fe8/newsource/Makefile",
      "https://github.com/mheyer32/ab3d-rtg/blob/c135c175a55d26238efebcc52e9382c61bcd6fe8/newsource/main.s",
      "https://github.com/mheyer32/ab3d-rtg/commit/c135c175a55d26238efebcc52e9382c61bcd6fe8"
    ],
    "id": "2026-10-17-promote-alien-breed-3d-rtg-amiga",
    "project_ids": [
      "alien-breed-3d-rtg-amiga"
    ],
    "reason": "Native Amiga RTG adaptation of Alien Breed 3D based on John Girvin’s earlier source work.",
    "source_ids": [
      "github-mheyer32-ab3d-rtg"
    ],
    "title": "Alien Breed 3D RTG",
    "url": "https://github.com/mheyer32/ab3d-rtg"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/mheyer32/alienbreed3d2/blob/86abb5c5b28cbab874e46b96c94b93b51bff56ec/README.md",
      "https://github.com/mheyer32/alienbreed3d2/blob/86abb5c5b28cbab874e46b96c94b93b51bff56ec/ab3d2_source/Makefile",
      "https://github.com/mheyer32/alienbreed3d2/blob/86abb5c5b28cbab874e46b96c94b93b51bff56ec/ab3d2_source/c/main.c",
      "https://github.com/mheyer32/alienbreed3d2/blob/86abb5c5b28cbab874e46b96c94b93b51bff56ec/ab3d2_source/docs/README.md",
      "https://github.com/mheyer32/alienbreed3d2/commit/86abb5c5b28cbab874e46b96c94b93b51bff56ec"
    ],
    "id": "2026-10-17-promote-alien-breed-3d2-rebuilt-amiga",
    "project_ids": [
      "alien-breed-3d2-rebuilt-amiga"
    ],
    "reason": "Maintained native Amiga engine reconstruction from released Alien Breed 3D II source, with bug/performance fixes, Workbench return, RTG and mod support.",
    "source_ids": [
      "github-mheyer32-alienbreed3d2"
    ],
    "title": "Alien Breed 3D II Rebuilt",
    "url": "https://github.com/mheyer32/alienbreed3d2"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/titmouse001/Amiga-Archive-For-My-Old-Stuff/blob/fc2524969bc7da5f76aef9fd13bba956c063d843/README.md",
      "https://github.com/titmouse001/Amiga-Archive-For-My-Old-Stuff/blob/fc2524969bc7da5f76aef9fd13bba956c063d843/HO_Source/High_Octane/high_octane.amos",
      "https://github.com/titmouse001/Amiga-Archive-For-My-Old-Stuff/commit/fc2524969bc7da5f76aef9fd13bba956c063d843"
    ],
    "id": "2026-10-17-promote-high-octane-original-amiga",
    "project_ids": [
      "high-octane-original-amiga"
    ],
    "reason": "Author’s recovered AMOS sources for the original High Octane driving game, with map editor, assets and contemporary publication material.",
    "source_ids": [
      "github-titmouse001-amiga-archive-for-my-old-stuff"
    ],
    "title": "High Octane – Original Amiga Sources",
    "url": "https://github.com/titmouse001/Amiga-Archive-For-My-Old-Stuff"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/0xABADCAFE/karlos-tkg/blob/09d84a05f6811ff055279c50e6a70dacbf4825b8/README.md",
      "https://github.com/0xABADCAFE/karlos-tkg/blob/09d84a05f6811ff055279c50e6a70dacbf4825b8/Editor/Assets/TKGD/Make.sh",
      "https://github.com/0xABADCAFE/karlos-tkg/commit/09d84a05f6811ff055279c50e6a70dacbf4825b8"
    ],
    "id": "2026-10-17-promote-alien-breed-3d2-redux",
    "project_ids": [
      "alien-breed-3d2-redux"
    ],
    "reason": "Work-in-progress reimagining of Alien Breed 3D II with expanded textures, lighting, enemies, sounds, weapons and inventory rules.",
    "source_ids": [
      "github-0xabadcafe-karlos-tkg"
    ],
    "title": "Alien Breed 3D II Redux (Karlos TKG)",
    "url": "https://github.com/0xABADCAFE/karlos-tkg"
  }
]
```

## Research event notes

Catalogue URLs were screened programmatically, then source/build/identity and lineage reviewed. Distinguish High Octane from High Octane II; native Breathless from its tracked SDL2 port; Alien Breed 3D RTG from the PC port; Rebuilt engine from Redux content; and NEONnoir from NeonWorld. AMOS tokenized source was recognized by its file header. Collection coverage, non-permissive asset/source notices and paid-release announcements remain explicit. All prior projects are preserved; no candidate code was executed.
