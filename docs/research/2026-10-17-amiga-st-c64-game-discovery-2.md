# Add eight source-available Amiga, Atari ST and C64 games and in-game editors; defer binary-only Ashheart.

Add eight source-available Amiga, Atari ST and C64 games and in-game editors; defer binary-only Ashheart.

Date: 2026-10-17 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- modsurfer-amiga / AI (no-evidence-found): No explicit development-AI attribution was found in the inspected README, selected source/build files and head commit; non-use is not inferred.
- yast3-atari-st / Runtime profiles (no-evidence-found): No complete minimum hardware profile was established in the inspected material; platform support is recorded separately.
- yast3-atari-st / AI (no-evidence-found): No explicit development-AI attribution was found in the inspected README, selected source/build files and head commit; non-use is not inferred.
- fruit-basket-atari-st / Runtime profiles (no-evidence-found): No complete minimum hardware profile was established in the inspected material; platform support is recorded separately.
- fruit-basket-atari-st / AI (no-evidence-found): No explicit development-AI attribution was found in the inspected README, selected source/build files and head commit; non-use is not inferred.
- grand-theft-pacman-c64 / Runtime profiles (no-evidence-found): No complete minimum hardware profile was established in the inspected material; platform support is recorded separately.
- petscii-panic-c64 / Runtime profiles (no-evidence-found): No complete minimum hardware profile was established in the inspected material; platform support is recorded separately.
- petscii-panic-c64 / AI (no-evidence-found): No explicit development-AI attribution was found in the inspected README, selected source/build files and head commit; non-use is not inferred.
- cannon-fodder-ingame-editor-amiga / AI (no-evidence-found): No explicit development-AI attribution was found in the inspected README, selected source/build files and head commit; non-use is not inferred.
- lemmings2-ingame-editor-amiga / AI (no-evidence-found): No explicit development-AI attribution was found in the inspected README, selected source/build files and head commit; non-use is not inferred.

## ModSurfer

Project ID: modsurfer-amiga · Overall audit: reviewed

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
  "display_title": "ModSurfer",
  "id": "modsurfer-amiga",
  "last_activity": "2019-11-09",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "m68k assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/amigageek/modsurfer",
  "runtime_profiles": [
    {
      "chipsets": [
        "OCS"
      ],
      "cpu_family": "m68k",
      "evidence": [
        "https://github.com/amigageek/modsurfer/blob/ca8e741696d1084c796f73b37f046d2d9affa325/extra/ReadMe"
      ],
      "min_cpu": "68000",
      "min_ram_kib": 512,
      "name": "ModSurfer documented baseline",
      "notes": "Upstream distribution ReadMe explicitly requires PAL OCS, 68000 and 512K or better; not independently tested.",
      "os": "AmigaOS 1.2+",
      "platform": "Amiga"
    }
  ],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/play test not performed",
  "subjects": [
    "ModSurfer"
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
  "title": "ModSurfer",
  "tool_kinds": [],
  "types": [
    "native homebrew game"
  ],
  "upstream_name": "ModSurfer",
  "work_kinds": []
}
```

### Identity (reviewed)

Rhythm game that generates a three-dimensional course from the player's MOD music, inspired by AudioSurf.
- https://github.com/amigageek/modsurfer/blob/ca8e741696d1084c796f73b37f046d2d9affa325/ReadMe
- https://github.com/amigageek/modsurfer/blob/ca8e741696d1084c796f73b37f046d2d9affa325/Makefile
- https://github.com/amigageek/modsurfer/blob/ca8e741696d1084c796f73b37f046d2d9affa325/game.c
- https://github.com/amigageek/modsurfer/blob/ca8e741696d1084c796f73b37f046d2d9affa325/extra/ReadMe
- https://github.com/amigageek/modsurfer/commit/ca8e741696d1084c796f73b37f046d2d9affa325

### Classification (reviewed)

Native homebrew/board-game clone; not original-binary restoration.
- https://github.com/amigageek/modsurfer/blob/ca8e741696d1084c796f73b37f046d2d9affa325/ReadMe
- https://github.com/amigageek/modsurfer/blob/ca8e741696d1084c796f73b37f046d2d9affa325/Makefile
- https://github.com/amigageek/modsurfer/blob/ca8e741696d1084c796f73b37f046d2d9affa325/game.c
- https://github.com/amigageek/modsurfer/blob/ca8e741696d1084c796f73b37f046d2d9affa325/extra/ReadMe
- https://github.com/amigageek/modsurfer/commit/ca8e741696d1084c796f73b37f046d2d9affa325

### Source CPU (not-applicable)

New authored game, not a reconstruction of an identified predecessor binary; source CPU/platform remain empty.
- https://github.com/amigageek/modsurfer/blob/ca8e741696d1084c796f73b37f046d2d9affa325/ReadMe
- https://github.com/amigageek/modsurfer/blob/ca8e741696d1084c796f73b37f046d2d9affa325/Makefile
- https://github.com/amigageek/modsurfer/blob/ca8e741696d1084c796f73b37f046d2d9affa325/game.c
- https://github.com/amigageek/modsurfer/blob/ca8e741696d1084c796f73b37f046d2d9affa325/extra/ReadMe
- https://github.com/amigageek/modsurfer/commit/ca8e741696d1084c796f73b37f046d2d9affa325

### Target CPU (reviewed)

Makefile explicitly selects m68k-amigaos-gcc with -m68000 and vasm; includes game, graphics and ProTracker playback sources.
- https://github.com/amigageek/modsurfer/blob/ca8e741696d1084c796f73b37f046d2d9affa325/ReadMe
- https://github.com/amigageek/modsurfer/blob/ca8e741696d1084c796f73b37f046d2d9affa325/Makefile
- https://github.com/amigageek/modsurfer/blob/ca8e741696d1084c796f73b37f046d2d9affa325/game.c
- https://github.com/amigageek/modsurfer/blob/ca8e741696d1084c796f73b37f046d2d9affa325/extra/ReadMe
- https://github.com/amigageek/modsurfer/commit/ca8e741696d1084c796f73b37f046d2d9affa325

### Build (reviewed)

GNU make cross-builds the native executable and ADF using Amiga GCC, vasm, a host C compiler and xdftool. No independent compilation or gameplay test was performed.
- https://github.com/amigageek/modsurfer/blob/ca8e741696d1084c796f73b37f046d2d9affa325/ReadMe
- https://github.com/amigageek/modsurfer/blob/ca8e741696d1084c796f73b37f046d2d9affa325/Makefile
- https://github.com/amigageek/modsurfer/blob/ca8e741696d1084c796f73b37f046d2d9affa325/game.c
- https://github.com/amigageek/modsurfer/blob/ca8e741696d1084c796f73b37f046d2d9affa325/extra/ReadMe
- https://github.com/amigageek/modsurfer/commit/ca8e741696d1084c796f73b37f046d2d9affa325

### Runtime profiles (reviewed)

Upstream distribution ReadMe explicitly requires PAL OCS, 68000 and 512K or better; not independently tested.
- https://github.com/amigageek/modsurfer/blob/ca8e741696d1084c796f73b37f046d2d9affa325/ReadMe
- https://github.com/amigageek/modsurfer/blob/ca8e741696d1084c796f73b37f046d2d9affa325/Makefile
- https://github.com/amigageek/modsurfer/blob/ca8e741696d1084c796f73b37f046d2d9affa325/game.c
- https://github.com/amigageek/modsurfer/blob/ca8e741696d1084c796f73b37f046d2d9affa325/extra/ReadMe
- https://github.com/amigageek/modsurfer/commit/ca8e741696d1084c796f73b37f046d2d9affa325

### AI (no-evidence-found)

No explicit development-AI attribution was found in the inspected README, selected source/build files and head commit; non-use is not inferred.
- https://github.com/amigageek/modsurfer/blob/ca8e741696d1084c796f73b37f046d2d9affa325/ReadMe
- https://github.com/amigageek/modsurfer/blob/ca8e741696d1084c796f73b37f046d2d9affa325/Makefile
- https://github.com/amigageek/modsurfer/blob/ca8e741696d1084c796f73b37f046d2d9affa325/game.c
- https://github.com/amigageek/modsurfer/blob/ca8e741696d1084c796f73b37f046d2d9affa325/extra/ReadMe
- https://github.com/amigageek/modsurfer/commit/ca8e741696d1084c796f73b37f046d2d9affa325

### Relationships (reviewed)

Original Amiga game, not a binary reconstruction of AudioSurf. Bundled module-player code and assets remain part of the coherent game repository.
- https://github.com/amigageek/modsurfer/blob/ca8e741696d1084c796f73b37f046d2d9affa325/ReadMe
- https://github.com/amigageek/modsurfer/blob/ca8e741696d1084c796f73b37f046d2d9affa325/Makefile
- https://github.com/amigageek/modsurfer/blob/ca8e741696d1084c796f73b37f046d2d9affa325/game.c
- https://github.com/amigageek/modsurfer/blob/ca8e741696d1084c796f73b37f046d2d9affa325/extra/ReadMe
- https://github.com/amigageek/modsurfer/commit/ca8e741696d1084c796f73b37f046d2d9affa325

## Can't Stop

Project ID: cantstop-hollywood-amiga · Overall audit: reviewed

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
    "compilable": null,
    "playable": null,
    "runnable": null
  },
  "display_title": "Can't Stop",
  "id": "cantstop-hollywood-amiga",
  "last_activity": "2026-08-24",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "Hollywood"
  ],
  "record_class": "subject",
  "repo": "https://github.com/phipslk/cantstop",
  "runtime_profiles": [
    {
      "cpu_family": "m68k",
      "evidence": [
        "https://github.com/phipslk/cantstop/blob/b15c965965a1a1a042334f9b4c920c773a01fb79/README.md"
      ],
      "min_cpu": "68020",
      "name": "Amiga 68k release",
      "notes": "README requires RTG and describes AHI audio; RAM minimum is not specified.",
      "os": "AmigaOS 3.x",
      "platform": "Amiga"
    }
  ],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/play test not performed",
  "subjects": [
    "Can't Stop"
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
    "Amiga",
    "Windows"
  ],
  "techniques": [],
  "title": "Can't Stop",
  "tool_kinds": [],
  "types": [
    "native homebrew game"
  ],
  "upstream_name": "Can't Stop",
  "work_kinds": []
}
```

### Identity (reviewed)

Push-your-luck dice-board game clone with hotseat and computer players, English/German UI, risk indicator and sound.
- https://github.com/phipslk/cantstop/blob/b15c965965a1a1a042334f9b4c920c773a01fb79/README.md
- https://github.com/phipslk/cantstop/blob/b15c965965a1a1a042334f9b4c920c773a01fb79/cantstop.hws
- https://github.com/phipslk/cantstop/commit/b15c965965a1a1a042334f9b4c920c773a01fb79

### Classification (reviewed)

Native homebrew/board-game clone; not original-binary restoration.
- https://github.com/phipslk/cantstop/blob/b15c965965a1a1a042334f9b4c920c773a01fb79/README.md
- https://github.com/phipslk/cantstop/blob/b15c965965a1a1a042334f9b4c920c773a01fb79/cantstop.hws
- https://github.com/phipslk/cantstop/commit/b15c965965a1a1a042334f9b4c920c773a01fb79

### Source CPU (not-applicable)

New authored game, not a reconstruction of an identified predecessor binary; source CPU/platform remain empty.
- https://github.com/phipslk/cantstop/blob/b15c965965a1a1a042334f9b4c920c773a01fb79/README.md
- https://github.com/phipslk/cantstop/blob/b15c965965a1a1a042334f9b4c920c773a01fb79/cantstop.hws
- https://github.com/phipslk/cantstop/commit/b15c965965a1a1a042334f9b4c920c773a01fb79

### Target CPU (reviewed)

README explicitly offers Amiga 68k output for 68020+ and Windows output; Hollywood source has separate Amiga audio paths. Windows executable CPU is not established and is not inferred.
- https://github.com/phipslk/cantstop/blob/b15c965965a1a1a042334f9b4c920c773a01fb79/README.md
- https://github.com/phipslk/cantstop/blob/b15c965965a1a1a042334f9b4c920c773a01fb79/cantstop.hws
- https://github.com/phipslk/cantstop/commit/b15c965965a1a1a042334f9b4c920c773a01fb79

### Build (reviewed)

Hollywood source and build assets are provided; releases offer Windows and Amiga executables. No independent compilation or gameplay test was performed.
- https://github.com/phipslk/cantstop/blob/b15c965965a1a1a042334f9b4c920c773a01fb79/README.md
- https://github.com/phipslk/cantstop/blob/b15c965965a1a1a042334f9b4c920c773a01fb79/cantstop.hws
- https://github.com/phipslk/cantstop/commit/b15c965965a1a1a042334f9b4c920c773a01fb79

### Runtime profiles (reviewed)

README requires RTG and describes AHI audio; RAM minimum is not specified.
- https://github.com/phipslk/cantstop/blob/b15c965965a1a1a042334f9b4c920c773a01fb79/README.md
- https://github.com/phipslk/cantstop/blob/b15c965965a1a1a042334f9b4c920c773a01fb79/cantstop.hws
- https://github.com/phipslk/cantstop/commit/b15c965965a1a1a042334f9b4c920c773a01fb79

### AI (reviewed)

Pinned commit explicitly credits Claude as co-author; computer opponents are separate from development-AI attribution.
- https://github.com/phipslk/cantstop/blob/b15c965965a1a1a042334f9b4c920c773a01fb79/README.md
- https://github.com/phipslk/cantstop/blob/b15c965965a1a1a042334f9b4c920c773a01fb79/cantstop.hws
- https://github.com/phipslk/cantstop/commit/b15c965965a1a1a042334f9b4c920c773a01fb79

### Relationships (reviewed)

Unofficial clone of Sid Sackson's board game, not a reverse-engineered predecessor binary. GPL-3.0 applies to repository code/assets, not the original game name/design.
- https://github.com/phipslk/cantstop/blob/b15c965965a1a1a042334f9b4c920c773a01fb79/README.md
- https://github.com/phipslk/cantstop/blob/b15c965965a1a1a042334f9b4c920c773a01fb79/cantstop.hws
- https://github.com/phipslk/cantstop/commit/b15c965965a1a1a042334f9b4c920c773a01fb79

## YAST3

Project ID: yast3-atari-st · Overall audit: reviewed

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
  "display_title": "YAST3",
  "id": "yast3-atari-st",
  "last_activity": "2025-08-11",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "m68k assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/jbqueru/yast3",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/play test not performed",
  "subjects": [
    "YAST3"
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
  "title": "YAST3",
  "tool_kinds": [],
  "types": [
    "native homebrew game"
  ],
  "upstream_name": "YAST3",
  "work_kinds": []
}
```

### Identity (reviewed)

Native dice-combination game by MegaBuSTers collaborators, targeting STE with reduced plain-ST experience and documented TT/Falcon compatibility.
- https://github.com/jbqueru/yast3/blob/078a0568eb7ae910cf210600c7a72433eb4693ff/README.md
- https://github.com/jbqueru/yast3/blob/078a0568eb7ae910cf210600c7a72433eb4693ff/main.s
- https://github.com/jbqueru/yast3/blob/078a0568eb7ae910cf210600c7a72433eb4693ff/build.sh
- https://github.com/jbqueru/yast3/commit/078a0568eb7ae910cf210600c7a72433eb4693ff

### Classification (reviewed)

Native homebrew/board-game clone; not original-binary restoration.
- https://github.com/jbqueru/yast3/blob/078a0568eb7ae910cf210600c7a72433eb4693ff/README.md
- https://github.com/jbqueru/yast3/blob/078a0568eb7ae910cf210600c7a72433eb4693ff/main.s
- https://github.com/jbqueru/yast3/blob/078a0568eb7ae910cf210600c7a72433eb4693ff/build.sh
- https://github.com/jbqueru/yast3/commit/078a0568eb7ae910cf210600c7a72433eb4693ff

### Source CPU (not-applicable)

New authored game, not a reconstruction of an identified predecessor binary; source CPU/platform remain empty.
- https://github.com/jbqueru/yast3/blob/078a0568eb7ae910cf210600c7a72433eb4693ff/README.md
- https://github.com/jbqueru/yast3/blob/078a0568eb7ae910cf210600c7a72433eb4693ff/main.s
- https://github.com/jbqueru/yast3/blob/078a0568eb7ae910cf210600c7a72433eb4693ff/build.sh
- https://github.com/jbqueru/yast3/commit/078a0568eb7ae910cf210600c7a72433eb4693ff

### Target CPU (reviewed)

RMAC assembly source uses 68k code; README identifies STE as primary target with plain ST fallback.
- https://github.com/jbqueru/yast3/blob/078a0568eb7ae910cf210600c7a72433eb4693ff/README.md
- https://github.com/jbqueru/yast3/blob/078a0568eb7ae910cf210600c7a72433eb4693ff/main.s
- https://github.com/jbqueru/yast3/blob/078a0568eb7ae910cf210600c7a72433eb4693ff/build.sh
- https://github.com/jbqueru/yast3/commit/078a0568eb7ae910cf210600c7a72433eb4693ff

### Build (reviewed)

build.sh packages PRG, ST/MSA disk images, source ZIP and Git bundle; README reports Hatari/EmuTOS testing. No independent rebuild or gameplay test.
- https://github.com/jbqueru/yast3/blob/078a0568eb7ae910cf210600c7a72433eb4693ff/README.md
- https://github.com/jbqueru/yast3/blob/078a0568eb7ae910cf210600c7a72433eb4693ff/main.s
- https://github.com/jbqueru/yast3/blob/078a0568eb7ae910cf210600c7a72433eb4693ff/build.sh
- https://github.com/jbqueru/yast3/commit/078a0568eb7ae910cf210600c7a72433eb4693ff

### Runtime profiles (no-evidence-found)

No complete minimum hardware profile was established in the inspected material; platform support is recorded separately.
- https://github.com/jbqueru/yast3/blob/078a0568eb7ae910cf210600c7a72433eb4693ff/README.md
- https://github.com/jbqueru/yast3/blob/078a0568eb7ae910cf210600c7a72433eb4693ff/main.s
- https://github.com/jbqueru/yast3/blob/078a0568eb7ae910cf210600c7a72433eb4693ff/build.sh
- https://github.com/jbqueru/yast3/commit/078a0568eb7ae910cf210600c7a72433eb4693ff

### AI (no-evidence-found)

No explicit development-AI attribution was found in the inspected README, selected source/build files and head commit; non-use is not inferred.
- https://github.com/jbqueru/yast3/blob/078a0568eb7ae910cf210600c7a72433eb4693ff/README.md
- https://github.com/jbqueru/yast3/blob/078a0568eb7ae910cf210600c7a72433eb4693ff/main.s
- https://github.com/jbqueru/yast3/blob/078a0568eb7ae910cf210600c7a72433eb4693ff/build.sh
- https://github.com/jbqueru/yast3/commit/078a0568eb7ae910cf210600c7a72433eb4693ff

### Relationships (reviewed)

Original native dice game; GitHub and Codeberg are mirrors of the same project, not separate additions. AGPL-3.0-or-later with a distinct optional CC BY-SA asset licence.
- https://github.com/jbqueru/yast3/blob/078a0568eb7ae910cf210600c7a72433eb4693ff/README.md
- https://github.com/jbqueru/yast3/blob/078a0568eb7ae910cf210600c7a72433eb4693ff/main.s
- https://github.com/jbqueru/yast3/blob/078a0568eb7ae910cf210600c7a72433eb4693ff/build.sh
- https://github.com/jbqueru/yast3/commit/078a0568eb7ae910cf210600c7a72433eb4693ff

## Atari ST Fruit Basket

Project ID: fruit-basket-atari-st · Overall audit: reviewed

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
  "display_title": "Atari ST Fruit Basket",
  "id": "fruit-basket-atari-st",
  "last_activity": "2026-03-25",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "m68k assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/Tameema23/atari-st-fruit-basket",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/play test not performed",
  "subjects": [
    "Atari ST Fruit Basket"
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
  "title": "Atari ST Fruit Basket",
  "tool_kinds": [],
  "types": [
    "native homebrew game"
  ],
  "upstream_name": "Atari ST Fruit Basket",
  "work_kinds": []
}
```

### Identity (reviewed)

Native catch-the-fruit and avoid-the-bombs arcade game with increasing difficulty, custom framebuffer rendering and PSG audio.
- https://github.com/Tameema23/atari-st-fruit-basket/blob/0009c4750f2efbf881751fabfd8ab29dca0844c9/README.md
- https://github.com/Tameema23/atari-st-fruit-basket/blob/0009c4750f2efbf881751fabfd8ab29dca0844c9/main.c
- https://github.com/Tameema23/atari-st-fruit-basket/blob/0009c4750f2efbf881751fabfd8ab29dca0844c9/MAKEFILE
- https://github.com/Tameema23/atari-st-fruit-basket/blob/0009c4750f2efbf881751fabfd8ab29dca0844c9/v_base.s
- https://github.com/Tameema23/atari-st-fruit-basket/commit/0009c4750f2efbf881751fabfd8ab29dca0844c9

### Classification (reviewed)

Native homebrew/board-game clone; not original-binary restoration.
- https://github.com/Tameema23/atari-st-fruit-basket/blob/0009c4750f2efbf881751fabfd8ab29dca0844c9/README.md
- https://github.com/Tameema23/atari-st-fruit-basket/blob/0009c4750f2efbf881751fabfd8ab29dca0844c9/main.c
- https://github.com/Tameema23/atari-st-fruit-basket/blob/0009c4750f2efbf881751fabfd8ab29dca0844c9/MAKEFILE
- https://github.com/Tameema23/atari-st-fruit-basket/blob/0009c4750f2efbf881751fabfd8ab29dca0844c9/v_base.s
- https://github.com/Tameema23/atari-st-fruit-basket/commit/0009c4750f2efbf881751fabfd8ab29dca0844c9

### Source CPU (not-applicable)

New authored game, not a reconstruction of an identified predecessor binary; source CPU/platform remain empty.
- https://github.com/Tameema23/atari-st-fruit-basket/blob/0009c4750f2efbf881751fabfd8ab29dca0844c9/README.md
- https://github.com/Tameema23/atari-st-fruit-basket/blob/0009c4750f2efbf881751fabfd8ab29dca0844c9/main.c
- https://github.com/Tameema23/atari-st-fruit-basket/blob/0009c4750f2efbf881751fabfd8ab29dca0844c9/MAKEFILE
- https://github.com/Tameema23/atari-st-fruit-basket/blob/0009c4750f2efbf881751fabfd8ab29dca0844c9/v_base.s
- https://github.com/Tameema23/atari-st-fruit-basket/commit/0009c4750f2efbf881751fabfd8ab29dca0844c9

### Target CPU (reviewed)

README specifies cc68x targeting Motorola 68000; v_base.s accesses ST video-base registers using native 68k instructions.
- https://github.com/Tameema23/atari-st-fruit-basket/blob/0009c4750f2efbf881751fabfd8ab29dca0844c9/README.md
- https://github.com/Tameema23/atari-st-fruit-basket/blob/0009c4750f2efbf881751fabfd8ab29dca0844c9/main.c
- https://github.com/Tameema23/atari-st-fruit-basket/blob/0009c4750f2efbf881751fabfd8ab29dca0844c9/MAKEFILE
- https://github.com/Tameema23/atari-st-fruit-basket/blob/0009c4750f2efbf881751fabfd8ab29dca0844c9/v_base.s
- https://github.com/Tameema23/atari-st-fruit-basket/commit/0009c4750f2efbf881751fabfd8ab29dca0844c9

### Build (reviewed)

C/assembly game and MAKEFILE are present. README claims working Atari hardware output; timing/tearing claims were not independently audited, and no build or execution was performed.
- https://github.com/Tameema23/atari-st-fruit-basket/blob/0009c4750f2efbf881751fabfd8ab29dca0844c9/README.md
- https://github.com/Tameema23/atari-st-fruit-basket/blob/0009c4750f2efbf881751fabfd8ab29dca0844c9/main.c
- https://github.com/Tameema23/atari-st-fruit-basket/blob/0009c4750f2efbf881751fabfd8ab29dca0844c9/MAKEFILE
- https://github.com/Tameema23/atari-st-fruit-basket/blob/0009c4750f2efbf881751fabfd8ab29dca0844c9/v_base.s
- https://github.com/Tameema23/atari-st-fruit-basket/commit/0009c4750f2efbf881751fabfd8ab29dca0844c9

### Runtime profiles (no-evidence-found)

No complete minimum hardware profile was established in the inspected material; platform support is recorded separately.
- https://github.com/Tameema23/atari-st-fruit-basket/blob/0009c4750f2efbf881751fabfd8ab29dca0844c9/README.md
- https://github.com/Tameema23/atari-st-fruit-basket/blob/0009c4750f2efbf881751fabfd8ab29dca0844c9/main.c
- https://github.com/Tameema23/atari-st-fruit-basket/blob/0009c4750f2efbf881751fabfd8ab29dca0844c9/MAKEFILE
- https://github.com/Tameema23/atari-st-fruit-basket/blob/0009c4750f2efbf881751fabfd8ab29dca0844c9/v_base.s
- https://github.com/Tameema23/atari-st-fruit-basket/commit/0009c4750f2efbf881751fabfd8ab29dca0844c9

### AI (no-evidence-found)

No explicit development-AI attribution was found in the inspected README, selected source/build files and head commit; non-use is not inferred.
- https://github.com/Tameema23/atari-st-fruit-basket/blob/0009c4750f2efbf881751fabfd8ab29dca0844c9/README.md
- https://github.com/Tameema23/atari-st-fruit-basket/blob/0009c4750f2efbf881751fabfd8ab29dca0844c9/main.c
- https://github.com/Tameema23/atari-st-fruit-basket/blob/0009c4750f2efbf881751fabfd8ab29dca0844c9/MAKEFILE
- https://github.com/Tameema23/atari-st-fruit-basket/blob/0009c4750f2efbf881751fabfd8ab29dca0844c9/v_base.s
- https://github.com/Tameema23/atari-st-fruit-basket/commit/0009c4750f2efbf881751fabfd8ab29dca0844c9

### Relationships (reviewed)

Original homebrew project rather than disassembly or a port of a named commercial game. No duplicate project identity found in the current catalogue.
- https://github.com/Tameema23/atari-st-fruit-basket/blob/0009c4750f2efbf881751fabfd8ab29dca0844c9/README.md
- https://github.com/Tameema23/atari-st-fruit-basket/blob/0009c4750f2efbf881751fabfd8ab29dca0844c9/main.c
- https://github.com/Tameema23/atari-st-fruit-basket/blob/0009c4750f2efbf881751fabfd8ab29dca0844c9/MAKEFILE
- https://github.com/Tameema23/atari-st-fruit-basket/blob/0009c4750f2efbf881751fabfd8ab29dca0844c9/v_base.s
- https://github.com/Tameema23/atari-st-fruit-basket/commit/0009c4750f2efbf881751fabfd8ab29dca0844c9

## PACMAN – Grand Theft Edition

Project ID: grand-theft-pacman-c64 · Overall audit: reviewed

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
    "compilable": null,
    "playable": null,
    "runnable": null
  },
  "display_title": "PACMAN – Grand Theft Edition",
  "id": "grand-theft-pacman-c64",
  "last_activity": "2026-10-09",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "6502 assembly",
    "JavaScript"
  ],
  "record_class": "subject",
  "repo": "https://github.com/rINanDO/c64-bbtg-grandtheftpacman",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/play test not performed",
  "subjects": [
    "PACMAN – Grand Theft Edition"
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
  "title": "PACMAN – Grand Theft Edition",
  "tool_kinds": [],
  "types": [
    "native homebrew game"
  ],
  "upstream_name": "PACMAN – Grand Theft Edition",
  "work_kinds": []
}
```

### Identity (reviewed)

Native Pac-Man-inspired game replacing ghosts with a wanted-list theme, with SID music, intro scenes and original themed sprites.
- https://github.com/rINanDO/c64-bbtg-grandtheftpacman/blob/fb122ac71529616740454c2c934071ad3768882c/README.md
- https://github.com/rINanDO/c64-bbtg-grandtheftpacman/blob/fb122ac71529616740454c2c934071ad3768882c/src/pacman.asm
- https://github.com/rINanDO/c64-bbtg-grandtheftpacman/blob/fb122ac71529616740454c2c934071ad3768882c/Claude%20notes.txt
- https://github.com/rINanDO/c64-bbtg-grandtheftpacman/commit/fb122ac71529616740454c2c934071ad3768882c

### Classification (reviewed)

Native homebrew/board-game clone; not original-binary restoration.
- https://github.com/rINanDO/c64-bbtg-grandtheftpacman/blob/fb122ac71529616740454c2c934071ad3768882c/README.md
- https://github.com/rINanDO/c64-bbtg-grandtheftpacman/blob/fb122ac71529616740454c2c934071ad3768882c/src/pacman.asm
- https://github.com/rINanDO/c64-bbtg-grandtheftpacman/blob/fb122ac71529616740454c2c934071ad3768882c/Claude%20notes.txt
- https://github.com/rINanDO/c64-bbtg-grandtheftpacman/commit/fb122ac71529616740454c2c934071ad3768882c

### Source CPU (not-applicable)

New authored game, not a reconstruction of an identified predecessor binary; source CPU/platform remain empty.
- https://github.com/rINanDO/c64-bbtg-grandtheftpacman/blob/fb122ac71529616740454c2c934071ad3768882c/README.md
- https://github.com/rINanDO/c64-bbtg-grandtheftpacman/blob/fb122ac71529616740454c2c934071ad3768882c/src/pacman.asm
- https://github.com/rINanDO/c64-bbtg-grandtheftpacman/blob/fb122ac71529616740454c2c934071ad3768882c/Claude%20notes.txt
- https://github.com/rINanDO/c64-bbtg-grandtheftpacman/commit/fb122ac71529616740454c2c934071ad3768882c

### Target CPU (reviewed)

src/pacman.asm directly uses C64 screen, colour RAM and hardware state; Node.js host tools assemble 6502 code and write PRG/D64 output.
- https://github.com/rINanDO/c64-bbtg-grandtheftpacman/blob/fb122ac71529616740454c2c934071ad3768882c/README.md
- https://github.com/rINanDO/c64-bbtg-grandtheftpacman/blob/fb122ac71529616740454c2c934071ad3768882c/src/pacman.asm
- https://github.com/rINanDO/c64-bbtg-grandtheftpacman/blob/fb122ac71529616740454c2c934071ad3768882c/Claude%20notes.txt
- https://github.com/rINanDO/c64-bbtg-grandtheftpacman/commit/fb122ac71529616740454c2c934071ad3768882c

### Build (reviewed)

Source and PRG/D64 are present. Published development notes explicitly say initial tests used a limited 6502 harness without VICE, leaving visuals/audio unchecked then. Current end-to-end playability was not independently verified.
- https://github.com/rINanDO/c64-bbtg-grandtheftpacman/blob/fb122ac71529616740454c2c934071ad3768882c/README.md
- https://github.com/rINanDO/c64-bbtg-grandtheftpacman/blob/fb122ac71529616740454c2c934071ad3768882c/src/pacman.asm
- https://github.com/rINanDO/c64-bbtg-grandtheftpacman/blob/fb122ac71529616740454c2c934071ad3768882c/Claude%20notes.txt
- https://github.com/rINanDO/c64-bbtg-grandtheftpacman/commit/fb122ac71529616740454c2c934071ad3768882c

### Runtime profiles (no-evidence-found)

No complete minimum hardware profile was established in the inspected material; platform support is recorded separately.
- https://github.com/rINanDO/c64-bbtg-grandtheftpacman/blob/fb122ac71529616740454c2c934071ad3768882c/README.md
- https://github.com/rINanDO/c64-bbtg-grandtheftpacman/blob/fb122ac71529616740454c2c934071ad3768882c/src/pacman.asm
- https://github.com/rINanDO/c64-bbtg-grandtheftpacman/blob/fb122ac71529616740454c2c934071ad3768882c/Claude%20notes.txt
- https://github.com/rINanDO/c64-bbtg-grandtheftpacman/commit/fb122ac71529616740454c2c934071ad3768882c

### AI (reviewed)

Repository explicitly calls the project vibecoded and supplies Claude development notes.
- https://github.com/rINanDO/c64-bbtg-grandtheftpacman/blob/fb122ac71529616740454c2c934071ad3768882c/README.md
- https://github.com/rINanDO/c64-bbtg-grandtheftpacman/blob/fb122ac71529616740454c2c934071ad3768882c/src/pacman.asm
- https://github.com/rINanDO/c64-bbtg-grandtheftpacman/blob/fb122ac71529616740454c2c934071ad3768882c/Claude%20notes.txt
- https://github.com/rINanDO/c64-bbtg-grandtheftpacman/commit/fb122ac71529616740454c2c934071ad3768882c

### Relationships (reviewed)

Original themed implementation, not original Pac-Man/GTA source restoration. Repository description explicitly calls it vibecoded and publishes Claude development notes. Bundled emulator is a test harness, not the game runtime.
- https://github.com/rINanDO/c64-bbtg-grandtheftpacman/blob/fb122ac71529616740454c2c934071ad3768882c/README.md
- https://github.com/rINanDO/c64-bbtg-grandtheftpacman/blob/fb122ac71529616740454c2c934071ad3768882c/src/pacman.asm
- https://github.com/rINanDO/c64-bbtg-grandtheftpacman/blob/fb122ac71529616740454c2c934071ad3768882c/Claude%20notes.txt
- https://github.com/rINanDO/c64-bbtg-grandtheftpacman/commit/fb122ac71529616740454c2c934071ad3768882c

## PETSCII Panic

Project ID: petscii-panic-c64 · Overall audit: reviewed

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
  "display_title": "PETSCII Panic",
  "id": "petscii-panic-c64",
  "last_activity": "2026-10-12",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "Commodore BASIC V2"
  ],
  "record_class": "subject",
  "repo": "https://github.com/sidchoudhuri/petscii-panic",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/play test not performed",
  "subjects": [
    "PETSCII Panic"
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
  "title": "PETSCII Panic",
  "tool_kinds": [],
  "types": [
    "native homebrew game"
  ],
  "upstream_name": "PETSCII Panic",
  "work_kinds": []
}
```

### Identity (reviewed)

Plants-vs-Zombies-style lawn-defense game in stock C64 BASIC V2 and PETSCII, with six waves and joystick/keyboard control.
- https://github.com/sidchoudhuri/petscii-panic/blob/973c1e41b70681a356e4ea9185d5aa33c8fa0866/README.md
- https://github.com/sidchoudhuri/petscii-panic/blob/973c1e41b70681a356e4ea9185d5aa33c8fa0866/petsciipanic.bas
- https://github.com/sidchoudhuri/petscii-panic/blob/973c1e41b70681a356e4ea9185d5aa33c8fa0866/devlog.md
- https://github.com/sidchoudhuri/petscii-panic/commit/973c1e41b70681a356e4ea9185d5aa33c8fa0866

### Classification (reviewed)

Native homebrew/board-game clone; not original-binary restoration.
- https://github.com/sidchoudhuri/petscii-panic/blob/973c1e41b70681a356e4ea9185d5aa33c8fa0866/README.md
- https://github.com/sidchoudhuri/petscii-panic/blob/973c1e41b70681a356e4ea9185d5aa33c8fa0866/petsciipanic.bas
- https://github.com/sidchoudhuri/petscii-panic/blob/973c1e41b70681a356e4ea9185d5aa33c8fa0866/devlog.md
- https://github.com/sidchoudhuri/petscii-panic/commit/973c1e41b70681a356e4ea9185d5aa33c8fa0866

### Source CPU (not-applicable)

New authored game, not a reconstruction of an identified predecessor binary; source CPU/platform remain empty.
- https://github.com/sidchoudhuri/petscii-panic/blob/973c1e41b70681a356e4ea9185d5aa33c8fa0866/README.md
- https://github.com/sidchoudhuri/petscii-panic/blob/973c1e41b70681a356e4ea9185d5aa33c8fa0866/petsciipanic.bas
- https://github.com/sidchoudhuri/petscii-panic/blob/973c1e41b70681a356e4ea9185d5aa33c8fa0866/devlog.md
- https://github.com/sidchoudhuri/petscii-panic/commit/973c1e41b70681a356e4ea9185d5aa33c8fa0866

### Target CPU (reviewed)

BASIC listing uses C64 PEEK/POKE screen and hardware addresses; it runs through the C64 BASIC interpreter on its 6502-family platform rather than a modern-host game engine.
- https://github.com/sidchoudhuri/petscii-panic/blob/973c1e41b70681a356e4ea9185d5aa33c8fa0866/README.md
- https://github.com/sidchoudhuri/petscii-panic/blob/973c1e41b70681a356e4ea9185d5aa33c8fa0866/petsciipanic.bas
- https://github.com/sidchoudhuri/petscii-panic/blob/973c1e41b70681a356e4ea9185d5aa33c8fa0866/devlog.md
- https://github.com/sidchoudhuri/petscii-panic/commit/973c1e41b70681a356e4ea9185d5aa33c8fa0866

### Build (reviewed)

Editable BASIC listing and ready-to-load PRG are supplied. README gives LOAD/RUN instructions and devlog explains lane scheduling. No independent execution or gameplay test.
- https://github.com/sidchoudhuri/petscii-panic/blob/973c1e41b70681a356e4ea9185d5aa33c8fa0866/README.md
- https://github.com/sidchoudhuri/petscii-panic/blob/973c1e41b70681a356e4ea9185d5aa33c8fa0866/petsciipanic.bas
- https://github.com/sidchoudhuri/petscii-panic/blob/973c1e41b70681a356e4ea9185d5aa33c8fa0866/devlog.md
- https://github.com/sidchoudhuri/petscii-panic/commit/973c1e41b70681a356e4ea9185d5aa33c8fa0866

### Runtime profiles (no-evidence-found)

No complete minimum hardware profile was established in the inspected material; platform support is recorded separately.
- https://github.com/sidchoudhuri/petscii-panic/blob/973c1e41b70681a356e4ea9185d5aa33c8fa0866/README.md
- https://github.com/sidchoudhuri/petscii-panic/blob/973c1e41b70681a356e4ea9185d5aa33c8fa0866/petsciipanic.bas
- https://github.com/sidchoudhuri/petscii-panic/blob/973c1e41b70681a356e4ea9185d5aa33c8fa0866/devlog.md
- https://github.com/sidchoudhuri/petscii-panic/commit/973c1e41b70681a356e4ea9185d5aa33c8fa0866

### AI (no-evidence-found)

No explicit development-AI attribution was found in the inspected README, selected source/build files and head commit; non-use is not inferred.
- https://github.com/sidchoudhuri/petscii-panic/blob/973c1e41b70681a356e4ea9185d5aa33c8fa0866/README.md
- https://github.com/sidchoudhuri/petscii-panic/blob/973c1e41b70681a356e4ea9185d5aa33c8fa0866/petsciipanic.bas
- https://github.com/sidchoudhuri/petscii-panic/blob/973c1e41b70681a356e4ea9185d5aa33c8fa0866/devlog.md
- https://github.com/sidchoudhuri/petscii-panic/commit/973c1e41b70681a356e4ea9185d5aa33c8fa0866

### Relationships (reviewed)

Original C64 homebrew inspired by tower-defense mechanics; no original Plants vs Zombies binary or asset reconstruction is claimed.
- https://github.com/sidchoudhuri/petscii-panic/blob/973c1e41b70681a356e4ea9185d5aa33c8fa0866/README.md
- https://github.com/sidchoudhuri/petscii-panic/blob/973c1e41b70681a356e4ea9185d5aa33c8fa0866/petsciipanic.bas
- https://github.com/sidchoudhuri/petscii-panic/blob/973c1e41b70681a356e4ea9185d5aa33c8fa0866/devlog.md
- https://github.com/sidchoudhuri/petscii-panic/commit/973c1e41b70681a356e4ea9185d5aa33c8fa0866

## Cannon Fodder In-Game Level Editor

Project ID: cannon-fodder-ingame-editor-amiga · Overall audit: reviewed

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
  "display_title": "Cannon Fodder In-Game Level Editor",
  "id": "cannon-fodder-ingame-editor-amiga",
  "last_activity": "2026-10-16",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "m68k assembly",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/timoheimonen/amiga-cannon-fodder-editor",
  "runtime_profiles": [
    {
      "cpu_family": "m68k",
      "evidence": [
        "https://github.com/timoheimonen/amiga-cannon-fodder-editor/blob/83eb35f0c5a0d2e78e6dc5969fed1664becc7c64/README.md"
      ],
      "min_chip_ram_kib": 2048,
      "min_cpu": "68020",
      "min_fast_ram_kib": 4096,
      "name": "Editor documented requirement",
      "notes": "README requires A1200-compatible machine; reported test configuration is emulated A1200/AGA, not real hardware.",
      "os": "Kickstart 3.1; WHDLoad 17+",
      "platform": "Amiga"
    }
  ],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [
    "m68k machine code"
  ],
  "source_platforms": [
    "Amiga"
  ],
  "status": "Primary source reviewed; independent build/play test not performed",
  "subjects": [
    "Cannon Fodder"
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
  "title": "Cannon Fodder In-Game Level Editor",
  "tool_kinds": [],
  "types": [
    "game enhancement and in-game editor"
  ],
  "upstream_name": "Cannon Fodder In-Game Level Editor",
  "work_kinds": [
    "patching",
    "data-format-analysis"
  ]
}
```

### Identity (reviewed)

In-game mission editor and WHDLoad integration for Cannon Fodder, supporting terrain/object editing, multi-phase missions and immediate test play.
- https://github.com/timoheimonen/amiga-cannon-fodder-editor/blob/83eb35f0c5a0d2e78e6dc5969fed1664becc7c64/README.md
- https://github.com/timoheimonen/amiga-cannon-fodder-editor/blob/83eb35f0c5a0d2e78e6dc5969fed1664becc7c64/build.py
- https://github.com/timoheimonen/amiga-cannon-fodder-editor/blob/83eb35f0c5a0d2e78e6dc5969fed1664becc7c64/docs/architecture.md
- https://github.com/timoheimonen/amiga-cannon-fodder-editor/commit/83eb35f0c5a0d2e78e6dc5969fed1664becc7c64

### Classification (reviewed)

Native 68k game enhancement and editor integrated with the original game.
- https://github.com/timoheimonen/amiga-cannon-fodder-editor/blob/83eb35f0c5a0d2e78e6dc5969fed1664becc7c64/README.md
- https://github.com/timoheimonen/amiga-cannon-fodder-editor/blob/83eb35f0c5a0d2e78e6dc5969fed1664becc7c64/build.py
- https://github.com/timoheimonen/amiga-cannon-fodder-editor/blob/83eb35f0c5a0d2e78e6dc5969fed1664becc7c64/docs/architecture.md
- https://github.com/timoheimonen/amiga-cannon-fodder-editor/commit/83eb35f0c5a0d2e78e6dc5969fed1664becc7c64

### Source CPU (reviewed)

Original Amiga game is patched through native 68k assembly and documented game data contracts.
- https://github.com/timoheimonen/amiga-cannon-fodder-editor/blob/83eb35f0c5a0d2e78e6dc5969fed1664becc7c64/README.md
- https://github.com/timoheimonen/amiga-cannon-fodder-editor/blob/83eb35f0c5a0d2e78e6dc5969fed1664becc7c64/build.py
- https://github.com/timoheimonen/amiga-cannon-fodder-editor/blob/83eb35f0c5a0d2e78e6dc5969fed1664becc7c64/docs/architecture.md
- https://github.com/timoheimonen/amiga-cannon-fodder-editor/commit/83eb35f0c5a0d2e78e6dc5969fed1664becc7c64

### Target CPU (reviewed)

vasmm68k_mot/vlink build native editor modules and a WHDLoad slave; README explicitly requires A1200-compatible 68020.
- https://github.com/timoheimonen/amiga-cannon-fodder-editor/blob/83eb35f0c5a0d2e78e6dc5969fed1664becc7c64/README.md
- https://github.com/timoheimonen/amiga-cannon-fodder-editor/blob/83eb35f0c5a0d2e78e6dc5969fed1664becc7c64/build.py
- https://github.com/timoheimonen/amiga-cannon-fodder-editor/blob/83eb35f0c5a0d2e78e6dc5969fed1664becc7c64/docs/architecture.md
- https://github.com/timoheimonen/amiga-cannon-fodder-editor/commit/83eb35f0c5a0d2e78e6dc5969fed1664becc7c64

### Build (reviewed)

Python patcher accepts checksum-matched user-supplied disks and builds a hard-disk install. Upstream testing is on an emulated A1200, explicitly not real hardware. No independent build or gameplay test.
- https://github.com/timoheimonen/amiga-cannon-fodder-editor/blob/83eb35f0c5a0d2e78e6dc5969fed1664becc7c64/README.md
- https://github.com/timoheimonen/amiga-cannon-fodder-editor/blob/83eb35f0c5a0d2e78e6dc5969fed1664becc7c64/build.py
- https://github.com/timoheimonen/amiga-cannon-fodder-editor/blob/83eb35f0c5a0d2e78e6dc5969fed1664becc7c64/docs/architecture.md
- https://github.com/timoheimonen/amiga-cannon-fodder-editor/commit/83eb35f0c5a0d2e78e6dc5969fed1664becc7c64

### Runtime profiles (reviewed)

README requires A1200-compatible machine; reported test configuration is emulated A1200/AGA, not real hardware.
- https://github.com/timoheimonen/amiga-cannon-fodder-editor/blob/83eb35f0c5a0d2e78e6dc5969fed1664becc7c64/README.md
- https://github.com/timoheimonen/amiga-cannon-fodder-editor/blob/83eb35f0c5a0d2e78e6dc5969fed1664becc7c64/build.py
- https://github.com/timoheimonen/amiga-cannon-fodder-editor/blob/83eb35f0c5a0d2e78e6dc5969fed1664becc7c64/docs/architecture.md
- https://github.com/timoheimonen/amiga-cannon-fodder-editor/commit/83eb35f0c5a0d2e78e6dc5969fed1664becc7c64

### AI (no-evidence-found)

No explicit development-AI attribution was found in the inspected README, selected source/build files and head commit; non-use is not inferred.
- https://github.com/timoheimonen/amiga-cannon-fodder-editor/blob/83eb35f0c5a0d2e78e6dc5969fed1664becc7c64/README.md
- https://github.com/timoheimonen/amiga-cannon-fodder-editor/blob/83eb35f0c5a0d2e78e6dc5969fed1664becc7c64/build.py
- https://github.com/timoheimonen/amiga-cannon-fodder-editor/blob/83eb35f0c5a0d2e78e6dc5969fed1664becc7c64/docs/architecture.md
- https://github.com/timoheimonen/amiga-cannon-fodder-editor/commit/83eb35f0c5a0d2e78e6dc5969fed1664becc7c64

### Relationships (reviewed)

Game-specific enhancement and mission-format tooling. Repository contains original editor/slave code, not the original game files or code.
- https://github.com/timoheimonen/amiga-cannon-fodder-editor/blob/83eb35f0c5a0d2e78e6dc5969fed1664becc7c64/README.md
- https://github.com/timoheimonen/amiga-cannon-fodder-editor/blob/83eb35f0c5a0d2e78e6dc5969fed1664becc7c64/build.py
- https://github.com/timoheimonen/amiga-cannon-fodder-editor/blob/83eb35f0c5a0d2e78e6dc5969fed1664becc7c64/docs/architecture.md
- https://github.com/timoheimonen/amiga-cannon-fodder-editor/commit/83eb35f0c5a0d2e78e6dc5969fed1664becc7c64

## Lemmings 2: The Tribes In-Game Level Editor

Project ID: lemmings2-ingame-editor-amiga · Overall audit: reviewed

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
  "display_title": "Lemmings 2: The Tribes In-Game Level Editor",
  "id": "lemmings2-ingame-editor-amiga",
  "last_activity": "2026-10-16",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "m68k assembly",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/timoheimonen/amiga-lemmings2-editor-patch",
  "runtime_profiles": [
    {
      "cpu_family": "m68k",
      "evidence": [
        "https://github.com/timoheimonen/amiga-lemmings2-editor-patch/blob/daea68589addc0d9edfc6f4953d65a52948642f7/README.md"
      ],
      "min_fast_ram_kib": 2048,
      "name": "Editor documented requirement",
      "notes": "PAL display required. Upstream tested emulated A1200/68020/AGA with 2 MiB Chip and 4 MiB Fast; that tested configuration is not asserted as the minimum.",
      "os": "Kickstart 3.1; WHDLoad 17+",
      "platform": "Amiga"
    }
  ],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [
    "m68k machine code"
  ],
  "source_platforms": [
    "Amiga"
  ],
  "status": "Primary source reviewed; independent build/play test not performed",
  "subjects": [
    "Lemmings 2: The Tribes"
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
  "title": "Lemmings 2: The Tribes In-Game Level Editor",
  "tool_kinds": [],
  "types": [
    "game enhancement and in-game editor"
  ],
  "upstream_name": "Lemmings 2: The Tribes In-Game Level Editor",
  "work_kinds": [
    "patching",
    "data-format-analysis"
  ]
}
```

### Identity (reviewed)

In-game terrain/object/skill editor for Lemmings 2 with test play, undo/redo and shareable native level files, packaged as a WHDLoad install.
- https://github.com/timoheimonen/amiga-lemmings2-editor-patch/blob/daea68589addc0d9edfc6f4953d65a52948642f7/README.md
- https://github.com/timoheimonen/amiga-lemmings2-editor-patch/blob/daea68589addc0d9edfc6f4953d65a52948642f7/src/editor/editor.s
- https://github.com/timoheimonen/amiga-lemmings2-editor-patch/blob/daea68589addc0d9edfc6f4953d65a52948642f7/build.py
- https://github.com/timoheimonen/amiga-lemmings2-editor-patch/commit/daea68589addc0d9edfc6f4953d65a52948642f7

### Classification (reviewed)

Native 68k game enhancement and editor integrated with the original game.
- https://github.com/timoheimonen/amiga-lemmings2-editor-patch/blob/daea68589addc0d9edfc6f4953d65a52948642f7/README.md
- https://github.com/timoheimonen/amiga-lemmings2-editor-patch/blob/daea68589addc0d9edfc6f4953d65a52948642f7/src/editor/editor.s
- https://github.com/timoheimonen/amiga-lemmings2-editor-patch/blob/daea68589addc0d9edfc6f4953d65a52948642f7/build.py
- https://github.com/timoheimonen/amiga-lemmings2-editor-patch/commit/daea68589addc0d9edfc6f4953d65a52948642f7

### Source CPU (reviewed)

Original Amiga game is patched through native 68k assembly and documented game data contracts.
- https://github.com/timoheimonen/amiga-lemmings2-editor-patch/blob/daea68589addc0d9edfc6f4953d65a52948642f7/README.md
- https://github.com/timoheimonen/amiga-lemmings2-editor-patch/blob/daea68589addc0d9edfc6f4953d65a52948642f7/src/editor/editor.s
- https://github.com/timoheimonen/amiga-lemmings2-editor-patch/blob/daea68589addc0d9edfc6f4953d65a52948642f7/build.py
- https://github.com/timoheimonen/amiga-lemmings2-editor-patch/commit/daea68589addc0d9edfc6f4953d65a52948642f7

### Target CPU (reviewed)

Native 68k editor assembly is built with vasmm68k_mot. README reports emulated A1200/68020 testing, which is not treated as proof of the minimum CPU.
- https://github.com/timoheimonen/amiga-lemmings2-editor-patch/blob/daea68589addc0d9edfc6f4953d65a52948642f7/README.md
- https://github.com/timoheimonen/amiga-lemmings2-editor-patch/blob/daea68589addc0d9edfc6f4953d65a52948642f7/src/editor/editor.s
- https://github.com/timoheimonen/amiga-lemmings2-editor-patch/blob/daea68589addc0d9edfc6f4953d65a52948642f7/build.py
- https://github.com/timoheimonen/amiga-lemmings2-editor-patch/commit/daea68589addc0d9edfc6f4953d65a52948642f7

### Build (reviewed)

Patcher supports checksum-matched user-owned US or PAL three-disk sets; the editor itself requires a PAL display. No independent build or gameplay test.
- https://github.com/timoheimonen/amiga-lemmings2-editor-patch/blob/daea68589addc0d9edfc6f4953d65a52948642f7/README.md
- https://github.com/timoheimonen/amiga-lemmings2-editor-patch/blob/daea68589addc0d9edfc6f4953d65a52948642f7/src/editor/editor.s
- https://github.com/timoheimonen/amiga-lemmings2-editor-patch/blob/daea68589addc0d9edfc6f4953d65a52948642f7/build.py
- https://github.com/timoheimonen/amiga-lemmings2-editor-patch/commit/daea68589addc0d9edfc6f4953d65a52948642f7

### Runtime profiles (reviewed)

PAL display required. Upstream tested emulated A1200/68020/AGA with 2 MiB Chip and 4 MiB Fast; that tested configuration is not asserted as the minimum.
- https://github.com/timoheimonen/amiga-lemmings2-editor-patch/blob/daea68589addc0d9edfc6f4953d65a52948642f7/README.md
- https://github.com/timoheimonen/amiga-lemmings2-editor-patch/blob/daea68589addc0d9edfc6f4953d65a52948642f7/src/editor/editor.s
- https://github.com/timoheimonen/amiga-lemmings2-editor-patch/blob/daea68589addc0d9edfc6f4953d65a52948642f7/build.py
- https://github.com/timoheimonen/amiga-lemmings2-editor-patch/commit/daea68589addc0d9edfc6f4953d65a52948642f7

### AI (no-evidence-found)

No explicit development-AI attribution was found in the inspected README, selected source/build files and head commit; non-use is not inferred.
- https://github.com/timoheimonen/amiga-lemmings2-editor-patch/blob/daea68589addc0d9edfc6f4953d65a52948642f7/README.md
- https://github.com/timoheimonen/amiga-lemmings2-editor-patch/blob/daea68589addc0d9edfc6f4953d65a52948642f7/src/editor/editor.s
- https://github.com/timoheimonen/amiga-lemmings2-editor-patch/blob/daea68589addc0d9edfc6f4953d65a52948642f7/build.py
- https://github.com/timoheimonen/amiga-lemmings2-editor-patch/commit/daea68589addc0d9edfc6f4953d65a52948642f7

### Relationships (reviewed)

Game-specific editor and format/patch work; original game assets are supplied by the user. Original game physics are reused rather than reimplemented.
- https://github.com/timoheimonen/amiga-lemmings2-editor-patch/blob/daea68589addc0d9edfc6f4953d65a52948642f7/README.md
- https://github.com/timoheimonen/amiga-lemmings2-editor-patch/blob/daea68589addc0d9edfc6f4953d65a52948642f7/src/editor/editor.s
- https://github.com/timoheimonen/amiga-lemmings2-editor-patch/blob/daea68589addc0d9edfc6f4953d65a52948642f7/build.py
- https://github.com/timoheimonen/amiga-lemmings2-editor-patch/commit/daea68589addc0d9edfc6f4953d65a52948642f7

## Sources

```json
[
  {
    "id": "github-amigageek-modsurfer",
    "kind": "github-repository",
    "reason": "Rhythm game that generates a three-dimensional course from the player's MOD music, inspired by AudioSurf.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/amigageek/modsurfer"
  },
  {
    "id": "github-phipslk-cantstop",
    "kind": "github-repository",
    "reason": "Push-your-luck dice-board game clone with hotseat and computer players, English/German UI, risk indicator and sound.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/phipslk/cantstop"
  },
  {
    "id": "github-jbqueru-yast3",
    "kind": "github-repository",
    "reason": "Native dice-combination game by MegaBuSTers collaborators, targeting STE with reduced plain-ST experience and documented TT/Falcon compatibility.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/jbqueru/yast3"
  },
  {
    "id": "github-tameema23-atari-st-fruit-basket",
    "kind": "github-repository",
    "reason": "Native catch-the-fruit and avoid-the-bombs arcade game with increasing difficulty, custom framebuffer rendering and PSG audio.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/Tameema23/atari-st-fruit-basket"
  },
  {
    "id": "github-rinando-c64-bbtg-grandtheftpacman",
    "kind": "github-repository",
    "reason": "Native Pac-Man-inspired game replacing ghosts with a wanted-list theme, with SID music, intro scenes and original themed sprites.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/rINanDO/c64-bbtg-grandtheftpacman"
  },
  {
    "id": "github-sidchoudhuri-petscii-panic",
    "kind": "github-repository",
    "reason": "Plants-vs-Zombies-style lawn-defense game in stock C64 BASIC V2 and PETSCII, with six waves and joystick/keyboard control.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/sidchoudhuri/petscii-panic"
  },
  {
    "id": "github-timoheimonen-amiga-cannon-fodder-editor",
    "kind": "github-repository",
    "reason": "In-game mission editor and WHDLoad integration for Cannon Fodder, supporting terrain/object editing, multi-phase missions and immediate test play.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/timoheimonen/amiga-cannon-fodder-editor"
  },
  {
    "id": "github-timoheimonen-amiga-lemmings2-editor-patch",
    "kind": "github-repository",
    "reason": "In-game terrain/object/skill editor for Lemmings 2 with test play, undo/redo and shareable native level files, packaged as a WHDLoad install.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/timoheimonen/amiga-lemmings2-editor-patch"
  },
  {
    "id": "github-rblackwood224-ashheart",
    "kind": "github-repository",
    "reason": "Inspected repository contains README and PRG/D64 binaries only; no editable game source. Defer pending a source release rather than present it as a source-development project.",
    "review_state": "partial",
    "source": "https://github.com/RBlackwood224/AshHeart"
  }
]
```

## Decisions

```json
[
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/amigageek/modsurfer/blob/ca8e741696d1084c796f73b37f046d2d9affa325/ReadMe",
      "https://github.com/amigageek/modsurfer/blob/ca8e741696d1084c796f73b37f046d2d9affa325/Makefile",
      "https://github.com/amigageek/modsurfer/blob/ca8e741696d1084c796f73b37f046d2d9affa325/game.c",
      "https://github.com/amigageek/modsurfer/blob/ca8e741696d1084c796f73b37f046d2d9affa325/extra/ReadMe",
      "https://github.com/amigageek/modsurfer/commit/ca8e741696d1084c796f73b37f046d2d9affa325"
    ],
    "id": "2026-10-17-promote-modsurfer-amiga",
    "project_ids": [
      "modsurfer-amiga"
    ],
    "reason": "Rhythm game that generates a three-dimensional course from the player's MOD music, inspired by AudioSurf.",
    "source_ids": [
      "github-amigageek-modsurfer"
    ],
    "title": "ModSurfer",
    "url": "https://github.com/amigageek/modsurfer"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/phipslk/cantstop/blob/b15c965965a1a1a042334f9b4c920c773a01fb79/README.md",
      "https://github.com/phipslk/cantstop/blob/b15c965965a1a1a042334f9b4c920c773a01fb79/cantstop.hws",
      "https://github.com/phipslk/cantstop/commit/b15c965965a1a1a042334f9b4c920c773a01fb79"
    ],
    "id": "2026-10-17-promote-cantstop-hollywood-amiga",
    "project_ids": [
      "cantstop-hollywood-amiga"
    ],
    "reason": "Push-your-luck dice-board game clone with hotseat and computer players, English/German UI, risk indicator and sound.",
    "source_ids": [
      "github-phipslk-cantstop"
    ],
    "title": "Can't Stop",
    "url": "https://github.com/phipslk/cantstop"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/jbqueru/yast3/blob/078a0568eb7ae910cf210600c7a72433eb4693ff/README.md",
      "https://github.com/jbqueru/yast3/blob/078a0568eb7ae910cf210600c7a72433eb4693ff/main.s",
      "https://github.com/jbqueru/yast3/blob/078a0568eb7ae910cf210600c7a72433eb4693ff/build.sh",
      "https://github.com/jbqueru/yast3/commit/078a0568eb7ae910cf210600c7a72433eb4693ff"
    ],
    "id": "2026-10-17-promote-yast3-atari-st",
    "project_ids": [
      "yast3-atari-st"
    ],
    "reason": "Native dice-combination game by MegaBuSTers collaborators, targeting STE with reduced plain-ST experience and documented TT/Falcon compatibility.",
    "source_ids": [
      "github-jbqueru-yast3"
    ],
    "title": "YAST3",
    "url": "https://github.com/jbqueru/yast3"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/Tameema23/atari-st-fruit-basket/blob/0009c4750f2efbf881751fabfd8ab29dca0844c9/README.md",
      "https://github.com/Tameema23/atari-st-fruit-basket/blob/0009c4750f2efbf881751fabfd8ab29dca0844c9/main.c",
      "https://github.com/Tameema23/atari-st-fruit-basket/blob/0009c4750f2efbf881751fabfd8ab29dca0844c9/MAKEFILE",
      "https://github.com/Tameema23/atari-st-fruit-basket/blob/0009c4750f2efbf881751fabfd8ab29dca0844c9/v_base.s",
      "https://github.com/Tameema23/atari-st-fruit-basket/commit/0009c4750f2efbf881751fabfd8ab29dca0844c9"
    ],
    "id": "2026-10-17-promote-fruit-basket-atari-st",
    "project_ids": [
      "fruit-basket-atari-st"
    ],
    "reason": "Native catch-the-fruit and avoid-the-bombs arcade game with increasing difficulty, custom framebuffer rendering and PSG audio.",
    "source_ids": [
      "github-tameema23-atari-st-fruit-basket"
    ],
    "title": "Atari ST Fruit Basket",
    "url": "https://github.com/Tameema23/atari-st-fruit-basket"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/rINanDO/c64-bbtg-grandtheftpacman/blob/fb122ac71529616740454c2c934071ad3768882c/README.md",
      "https://github.com/rINanDO/c64-bbtg-grandtheftpacman/blob/fb122ac71529616740454c2c934071ad3768882c/src/pacman.asm",
      "https://github.com/rINanDO/c64-bbtg-grandtheftpacman/blob/fb122ac71529616740454c2c934071ad3768882c/Claude%20notes.txt",
      "https://github.com/rINanDO/c64-bbtg-grandtheftpacman/commit/fb122ac71529616740454c2c934071ad3768882c"
    ],
    "id": "2026-10-17-promote-grand-theft-pacman-c64",
    "project_ids": [
      "grand-theft-pacman-c64"
    ],
    "reason": "Native Pac-Man-inspired game replacing ghosts with a wanted-list theme, with SID music, intro scenes and original themed sprites.",
    "source_ids": [
      "github-rinando-c64-bbtg-grandtheftpacman"
    ],
    "title": "PACMAN – Grand Theft Edition",
    "url": "https://github.com/rINanDO/c64-bbtg-grandtheftpacman"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/sidchoudhuri/petscii-panic/blob/973c1e41b70681a356e4ea9185d5aa33c8fa0866/README.md",
      "https://github.com/sidchoudhuri/petscii-panic/blob/973c1e41b70681a356e4ea9185d5aa33c8fa0866/petsciipanic.bas",
      "https://github.com/sidchoudhuri/petscii-panic/blob/973c1e41b70681a356e4ea9185d5aa33c8fa0866/devlog.md",
      "https://github.com/sidchoudhuri/petscii-panic/commit/973c1e41b70681a356e4ea9185d5aa33c8fa0866"
    ],
    "id": "2026-10-17-promote-petscii-panic-c64",
    "project_ids": [
      "petscii-panic-c64"
    ],
    "reason": "Plants-vs-Zombies-style lawn-defense game in stock C64 BASIC V2 and PETSCII, with six waves and joystick/keyboard control.",
    "source_ids": [
      "github-sidchoudhuri-petscii-panic"
    ],
    "title": "PETSCII Panic",
    "url": "https://github.com/sidchoudhuri/petscii-panic"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/timoheimonen/amiga-cannon-fodder-editor/blob/83eb35f0c5a0d2e78e6dc5969fed1664becc7c64/README.md",
      "https://github.com/timoheimonen/amiga-cannon-fodder-editor/blob/83eb35f0c5a0d2e78e6dc5969fed1664becc7c64/build.py",
      "https://github.com/timoheimonen/amiga-cannon-fodder-editor/blob/83eb35f0c5a0d2e78e6dc5969fed1664becc7c64/docs/architecture.md",
      "https://github.com/timoheimonen/amiga-cannon-fodder-editor/commit/83eb35f0c5a0d2e78e6dc5969fed1664becc7c64"
    ],
    "id": "2026-10-17-promote-cannon-fodder-ingame-editor-amiga",
    "project_ids": [
      "cannon-fodder-ingame-editor-amiga"
    ],
    "reason": "In-game mission editor and WHDLoad integration for Cannon Fodder, supporting terrain/object editing, multi-phase missions and immediate test play.",
    "source_ids": [
      "github-timoheimonen-amiga-cannon-fodder-editor"
    ],
    "title": "Cannon Fodder In-Game Level Editor",
    "url": "https://github.com/timoheimonen/amiga-cannon-fodder-editor"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/timoheimonen/amiga-lemmings2-editor-patch/blob/daea68589addc0d9edfc6f4953d65a52948642f7/README.md",
      "https://github.com/timoheimonen/amiga-lemmings2-editor-patch/blob/daea68589addc0d9edfc6f4953d65a52948642f7/src/editor/editor.s",
      "https://github.com/timoheimonen/amiga-lemmings2-editor-patch/blob/daea68589addc0d9edfc6f4953d65a52948642f7/build.py",
      "https://github.com/timoheimonen/amiga-lemmings2-editor-patch/commit/daea68589addc0d9edfc6f4953d65a52948642f7"
    ],
    "id": "2026-10-17-promote-lemmings2-ingame-editor-amiga",
    "project_ids": [
      "lemmings2-ingame-editor-amiga"
    ],
    "reason": "In-game terrain/object/skill editor for Lemmings 2 with test play, undo/redo and shareable native level files, packaged as a WHDLoad install.",
    "source_ids": [
      "github-timoheimonen-amiga-lemmings2-editor-patch"
    ],
    "title": "Lemmings 2: The Tribes In-Game Level Editor",
    "url": "https://github.com/timoheimonen/amiga-lemmings2-editor-patch"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/RBlackwood224/AshHeart"
    ],
    "id": "2026-10-17-defer-ashheart-source",
    "project_ids": [],
    "reason": "Inspected repository contains README and PRG/D64 binaries only; no editable game source. Defer pending a source release rather than present it as a source-development project.",
    "source_ids": [
      "github-rblackwood224-ashheart"
    ],
    "title": "ASHHEART – The Silent Deep",
    "url": "https://github.com/RBlackwood224/AshHeart"
  }
]
```
