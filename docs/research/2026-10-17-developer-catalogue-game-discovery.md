# Add fourteen game projects from developer-following and catalogue-to-source routes, including Populous creature fixes, native games and editors.

Add fourteen game projects from developer-following and catalogue-to-source routes, including Populous creature fixes, native games and editors.

Date: 2026-10-17 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- robo-gems-c64 / Runtime profiles (no-evidence-found): No full minimum hardware profile was established in the inspected material; platform does not imply an exact minimum configuration.
- robo-gems-c64 / AI (no-evidence-found): No explicit development-AI attribution found in inspected README, selected source/build files and head commit; non-use is not inferred.
- fatman-amiga-gus0650 / Runtime profiles (no-evidence-found): No full minimum hardware profile was established in the inspected material; platform does not imply an exact minimum configuration.
- fatman-amiga-gus0650 / AI (no-evidence-found): No explicit development-AI attribution found in inspected README, selected source/build files and head commit; non-use is not inferred.
- gusgames64-basic-archive / Runtime profiles (no-evidence-found): No full minimum hardware profile was established in the inspected material; platform does not imply an exact minimum configuration.
- gusgames64-basic-archive / AI (no-evidence-found): No explicit development-AI attribution found in inspected README, selected source/build files and head commit; non-use is not inferred.
- sg-invaders-c64 / Runtime profiles (no-evidence-found): No full minimum hardware profile was established in the inspected material; platform does not imply an exact minimum configuration.
- sg-invaders-c64 / AI (no-evidence-found): Release page declares no generative AI, while repository contains Copilot guidance. Configuration alone proves neither use nor non-use in development; leave development-AI usage unknown.
- light-cycle-duel-c64 / Runtime profiles (no-evidence-found): No full minimum hardware profile was established in the inspected material; platform does not imply an exact minimum configuration.
- light-cycle-duel-c64 / AI (no-evidence-found): No explicit development-AI attribution found in inspected README, selected source/build files and head commit; non-use is not inferred.
- populous-amiga-creature-fix / Runtime profiles (no-evidence-found): No full minimum hardware profile was established in the inspected material; platform does not imply an exact minimum configuration.
- populous-amiga-creature-fix / AI (no-evidence-found): No explicit development-AI attribution found in inspected README, selected source/build files and head commit; non-use is not inferred.
- populous-atari-st-creature-fix / Runtime profiles (no-evidence-found): No full minimum hardware profile was established in the inspected material; platform does not imply an exact minimum configuration.
- populous-atari-st-creature-fix / AI (no-evidence-found): No explicit development-AI attribution found in inspected README, selected source/build files and head commit; non-use is not inferred.
- ultima-v-atari-st-inn-fix / Runtime profiles (no-evidence-found): No full minimum hardware profile was established in the inspected material; platform does not imply an exact minimum configuration.
- ultima-v-atari-st-inn-fix / AI (no-evidence-found): No explicit development-AI attribution found in inspected README, selected source/build files and head commit; non-use is not inferred.
- hunter-amiga-68060-performance / AI (no-evidence-found): No explicit development-AI attribution found in inspected README, selected source/build files and head commit; non-use is not inferred.
- lemmings-amiga-ingame-editor / AI (no-evidence-found): No explicit development-AI attribution found in inspected README, selected source/build files and head commit; non-use is not inferred.
- street-rod-2-amiga-68060-patch / AI (no-evidence-found): No explicit development-AI attribution found in inspected README, selected source/build files and head commit; non-use is not inferred.
- swos-9697-amiga-ingame-editors / AI (no-evidence-found): No explicit development-AI attribution found in inspected README, selected source/build files and head commit; non-use is not inferred.
- caveman-lionel-commodore-ports / Runtime profiles (no-evidence-found): No full minimum hardware profile was established in the inspected material; platform does not imply an exact minimum configuration.
- caveman-lionel-commodore-ports / AI (no-evidence-found): No explicit development-AI attribution found in inspected README, selected source/build files and head commit; non-use is not inferred.

## Robo Gems

Project ID: robo-gems-c64 · Overall audit: reviewed

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
  "display_title": "Robo Gems",
  "id": "robo-gems-c64",
  "last_activity": "2026-05-18",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "KickC",
    "6502 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/kdebczynski/c64-robo-gems",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/play test not performed",
  "subjects": [
    "Robo Gems"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build",
    "catalogue-to-source"
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
  "title": "Robo Gems",
  "tool_kinds": [],
  "types": [
    "source-available game"
  ],
  "upstream_name": "Robo Gems",
  "work_kinds": []
}
```

### Identity (reviewed)

Two-player competitive platform game with twelve maps, released as a learning project with its complete KickC code.
- https://github.com/kdebczynski/c64-robo-gems/blob/915a566b9c9df0dfe9be51e4fd173b65da3f3381/README.md
- https://github.com/kdebczynski/c64-robo-gems/blob/915a566b9c9df0dfe9be51e4fd173b65da3f3381/robo-gems.c
- https://github.com/kdebczynski/c64-robo-gems/commit/915a566b9c9df0dfe9be51e4fd173b65da3f3381
- https://kdebczynski.itch.io/robo-gems

### Classification (reviewed)

Source-available native game or authored port; no byte-exact binary reconstruction claim.
- https://github.com/kdebczynski/c64-robo-gems/blob/915a566b9c9df0dfe9be51e4fd173b65da3f3381/README.md
- https://github.com/kdebczynski/c64-robo-gems/blob/915a566b9c9df0dfe9be51e4fd173b65da3f3381/robo-gems.c
- https://github.com/kdebczynski/c64-robo-gems/commit/915a566b9c9df0dfe9be51e4fd173b65da3f3381
- https://kdebczynski.itch.io/robo-gems

### Source CPU (not-applicable)

No identified predecessor binary is reconstructed; original source platform and CPU are left empty.
- https://github.com/kdebczynski/c64-robo-gems/blob/915a566b9c9df0dfe9be51e4fd173b65da3f3381/README.md
- https://github.com/kdebczynski/c64-robo-gems/blob/915a566b9c9df0dfe9be51e4fd173b65da3f3381/robo-gems.c
- https://github.com/kdebczynski/c64-robo-gems/commit/915a566b9c9df0dfe9be51e4fd173b65da3f3381
- https://kdebczynski.itch.io/robo-gems

### Target CPU (reviewed)

Native Commodore 64 output on the 6502 family is established by the README and reviewed source; Python/Java build tools are host-side.
- https://github.com/kdebczynski/c64-robo-gems/blob/915a566b9c9df0dfe9be51e4fd173b65da3f3381/README.md
- https://github.com/kdebczynski/c64-robo-gems/blob/915a566b9c9df0dfe9be51e4fd173b65da3f3381/robo-gems.c
- https://github.com/kdebczynski/c64-robo-gems/commit/915a566b9c9df0dfe9be51e4fd173b65da3f3381
- https://kdebczynski.itch.io/robo-gems

### Build (reviewed)

README identifies KickC 0.8.6 beta plus KickAssembler and Java. Entry source includes C64 hardware, joystick, sprite, SID and screen modules. No independent rebuild, gameplay test or byte-exact comparison was performed.
- https://github.com/kdebczynski/c64-robo-gems/blob/915a566b9c9df0dfe9be51e4fd173b65da3f3381/README.md
- https://github.com/kdebczynski/c64-robo-gems/blob/915a566b9c9df0dfe9be51e4fd173b65da3f3381/robo-gems.c
- https://github.com/kdebczynski/c64-robo-gems/commit/915a566b9c9df0dfe9be51e4fd173b65da3f3381
- https://kdebczynski.itch.io/robo-gems

### Runtime profiles (no-evidence-found)

No full minimum hardware profile was established in the inspected material; platform does not imply an exact minimum configuration.
- https://github.com/kdebczynski/c64-robo-gems/blob/915a566b9c9df0dfe9be51e4fd173b65da3f3381/README.md
- https://github.com/kdebczynski/c64-robo-gems/blob/915a566b9c9df0dfe9be51e4fd173b65da3f3381/robo-gems.c
- https://github.com/kdebczynski/c64-robo-gems/commit/915a566b9c9df0dfe9be51e4fd173b65da3f3381
- https://kdebczynski.itch.io/robo-gems

### AI (no-evidence-found)

No explicit development-AI attribution found in inspected README, selected source/build files and head commit; non-use is not inferred.
- https://github.com/kdebczynski/c64-robo-gems/blob/915a566b9c9df0dfe9be51e4fd173b65da3f3381/README.md
- https://github.com/kdebczynski/c64-robo-gems/blob/915a566b9c9df0dfe9be51e4fd173b65da3f3381/robo-gems.c
- https://github.com/kdebczynski/c64-robo-gems/commit/915a566b9c9df0dfe9be51e4fd173b65da3f3381
- https://kdebczynski.itch.io/robo-gems

### Relationships (reviewed)

Distinct source-available game; current catalogue and prior decision URLs were screened before addition.
- https://github.com/kdebczynski/c64-robo-gems/blob/915a566b9c9df0dfe9be51e4fd173b65da3f3381/README.md
- https://github.com/kdebczynski/c64-robo-gems/blob/915a566b9c9df0dfe9be51e4fd173b65da3f3381/robo-gems.c
- https://github.com/kdebczynski/c64-robo-gems/commit/915a566b9c9df0dfe9be51e4fd173b65da3f3381
- https://kdebczynski.itch.io/robo-gems

## Fatman

Project ID: fatman-amiga-gus0650 · Overall audit: reviewed

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
  "display_title": "Fatman",
  "id": "fatman-amiga-gus0650",
  "last_activity": "2025-06-20",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "Blitz Basic"
  ],
  "record_class": "subject",
  "repo": "https://github.com/gus0650/Fatman",
  "runtime_profiles": [],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [
    "AmigaBASIC"
  ],
  "source_platforms": [
    "Amiga"
  ],
  "status": "Primary source reviewed; independent build/play test not performed",
  "subjects": [
    "Fatman"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build",
    "developer-following"
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
  "title": "Fatman",
  "tool_kinds": [],
  "types": [
    "source-available game"
  ],
  "upstream_name": "Fatman",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

Amiga game originally written in AmigaBASIC in 1990 and later converted to Blitz Basic.
- https://github.com/gus0650/Fatman/blob/85849f70fc72489e7ac86cb35df6fe2e34dd03f6/README.md
- https://github.com/gus0650/Fatman/blob/85849f70fc72489e7ac86cb35df6fe2e34dd03f6/fatman.bba
- https://github.com/gus0650/Fatman/commit/85849f70fc72489e7ac86cb35df6fe2e34dd03f6
- https://gus0650.itch.io/

### Classification (reviewed)

Source-available native game or authored port; no byte-exact binary reconstruction claim.
- https://github.com/gus0650/Fatman/blob/85849f70fc72489e7ac86cb35df6fe2e34dd03f6/README.md
- https://github.com/gus0650/Fatman/blob/85849f70fc72489e7ac86cb35df6fe2e34dd03f6/fatman.bba
- https://github.com/gus0650/Fatman/commit/85849f70fc72489e7ac86cb35df6fe2e34dd03f6
- https://gus0650.itch.io/

### Source CPU (reviewed)

Source lineage/platform is documented in the linked README and reviewed source; source CPU is distinct from host-side tooling.
- https://github.com/gus0650/Fatman/blob/85849f70fc72489e7ac86cb35df6fe2e34dd03f6/README.md
- https://github.com/gus0650/Fatman/blob/85849f70fc72489e7ac86cb35df6fe2e34dd03f6/fatman.bba
- https://github.com/gus0650/Fatman/commit/85849f70fc72489e7ac86cb35df6fe2e34dd03f6
- https://gus0650.itch.io/

### Target CPU (reviewed)

Native Amiga output on the m68k family is established by the README and reviewed source; Python/Java build tools are host-side.
- https://github.com/gus0650/Fatman/blob/85849f70fc72489e7ac86cb35df6fe2e34dd03f6/README.md
- https://github.com/gus0650/Fatman/blob/85849f70fc72489e7ac86cb35df6fe2e34dd03f6/fatman.bba
- https://github.com/gus0650/Fatman/commit/85849f70fc72489e7ac86cb35df6fe2e34dd03f6
- https://gus0650.itch.io/

### Build (reviewed)

Readable fatman.bba and tokenized BB2 source, assets, executable and ADF are supplied. Source header identifies Blitz Basic 2.1; display code directly uses Amiga bitmaps, blits and audio. No independent rebuild, gameplay test or byte-exact comparison was performed.
- https://github.com/gus0650/Fatman/blob/85849f70fc72489e7ac86cb35df6fe2e34dd03f6/README.md
- https://github.com/gus0650/Fatman/blob/85849f70fc72489e7ac86cb35df6fe2e34dd03f6/fatman.bba
- https://github.com/gus0650/Fatman/commit/85849f70fc72489e7ac86cb35df6fe2e34dd03f6
- https://gus0650.itch.io/

### Runtime profiles (no-evidence-found)

No full minimum hardware profile was established in the inspected material; platform does not imply an exact minimum configuration.
- https://github.com/gus0650/Fatman/blob/85849f70fc72489e7ac86cb35df6fe2e34dd03f6/README.md
- https://github.com/gus0650/Fatman/blob/85849f70fc72489e7ac86cb35df6fe2e34dd03f6/fatman.bba
- https://github.com/gus0650/Fatman/commit/85849f70fc72489e7ac86cb35df6fe2e34dd03f6
- https://gus0650.itch.io/

### AI (no-evidence-found)

No explicit development-AI attribution found in inspected README, selected source/build files and head commit; non-use is not inferred.
- https://github.com/gus0650/Fatman/blob/85849f70fc72489e7ac86cb35df6fe2e34dd03f6/README.md
- https://github.com/gus0650/Fatman/blob/85849f70fc72489e7ac86cb35df6fe2e34dd03f6/fatman.bba
- https://github.com/gus0650/Fatman/commit/85849f70fc72489e7ac86cb35df6fe2e34dd03f6
- https://gus0650.itch.io/

### Relationships (reviewed)

Distinct source-available game; current catalogue and prior decision URLs were screened before addition.
- https://github.com/gus0650/Fatman/blob/85849f70fc72489e7ac86cb35df6fe2e34dd03f6/README.md
- https://github.com/gus0650/Fatman/blob/85849f70fc72489e7ac86cb35df6fe2e34dd03f6/fatman.bba
- https://github.com/gus0650/Fatman/commit/85849f70fc72489e7ac86cb35df6fe2e34dd03f6
- https://gus0650.itch.io/

## GusGames64

Project ID: gusgames64-basic-archive · Overall audit: reviewed

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
  "display_title": "GusGames64",
  "id": "gusgames64-basic-archive",
  "last_activity": "2025-04-25",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "Commodore BASIC"
  ],
  "record_class": "subject",
  "repo": "https://github.com/gus0650/GusGames64",
  "runtime_profiles": [],
  "source_cpu": [
    "6502"
  ],
  "source_language": [
    "Commodore BASIC"
  ],
  "source_platforms": [
    "Commodore 64"
  ],
  "status": "Primary source reviewed; independent build/play test not performed",
  "subjects": [
    "GusGames64"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build",
    "developer-following"
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
  "title": "GusGames64",
  "tool_kinds": [],
  "types": [
    "source-available game"
  ],
  "upstream_name": "GusGames64",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

Coherent collection of small C64 games written by Gustaf Stechmann during 1984–1985.
- https://github.com/gus0650/GusGames64/blob/734a310c88060b9200606c5ff1bf5b21253ef374/README.md
- https://github.com/gus0650/GusGames64/blob/734a310c88060b9200606c5ff1bf5b21253ef374/src/moonlander.prg
- https://github.com/gus0650/GusGames64/commit/734a310c88060b9200606c5ff1bf5b21253ef374

### Classification (reviewed)

Source-available native game or authored port; no byte-exact binary reconstruction claim.
- https://github.com/gus0650/GusGames64/blob/734a310c88060b9200606c5ff1bf5b21253ef374/README.md
- https://github.com/gus0650/GusGames64/blob/734a310c88060b9200606c5ff1bf5b21253ef374/src/moonlander.prg
- https://github.com/gus0650/GusGames64/commit/734a310c88060b9200606c5ff1bf5b21253ef374

### Source CPU (reviewed)

Source lineage/platform is documented in the linked README and reviewed source; source CPU is distinct from host-side tooling.
- https://github.com/gus0650/GusGames64/blob/734a310c88060b9200606c5ff1bf5b21253ef374/README.md
- https://github.com/gus0650/GusGames64/blob/734a310c88060b9200606c5ff1bf5b21253ef374/src/moonlander.prg
- https://github.com/gus0650/GusGames64/commit/734a310c88060b9200606c5ff1bf5b21253ef374

### Target CPU (reviewed)

Native Commodore 64 output on the 6502 family is established by the README and reviewed source; Python/Java build tools are host-side.
- https://github.com/gus0650/GusGames64/blob/734a310c88060b9200606c5ff1bf5b21253ef374/README.md
- https://github.com/gus0650/GusGames64/blob/734a310c88060b9200606c5ff1bf5b21253ef374/src/moonlander.prg
- https://github.com/gus0650/GusGames64/commit/734a310c88060b9200606c5ff1bf5b21253ef374

### Build (reviewed)

The src/*.prg files are tokenized BASIC source, not automatically dismissed as opaque binaries: inspected Moonlander starts at $0801 with linked BASIC lines and REM title/author text. Other entries include Antares, Hangman, Planetoids and Skyhawk. D64 releases are also supplied. No independent rebuild, gameplay test or byte-exact comparison was performed.
- https://github.com/gus0650/GusGames64/blob/734a310c88060b9200606c5ff1bf5b21253ef374/README.md
- https://github.com/gus0650/GusGames64/blob/734a310c88060b9200606c5ff1bf5b21253ef374/src/moonlander.prg
- https://github.com/gus0650/GusGames64/commit/734a310c88060b9200606c5ff1bf5b21253ef374

### Runtime profiles (no-evidence-found)

No full minimum hardware profile was established in the inspected material; platform does not imply an exact minimum configuration.
- https://github.com/gus0650/GusGames64/blob/734a310c88060b9200606c5ff1bf5b21253ef374/README.md
- https://github.com/gus0650/GusGames64/blob/734a310c88060b9200606c5ff1bf5b21253ef374/src/moonlander.prg
- https://github.com/gus0650/GusGames64/commit/734a310c88060b9200606c5ff1bf5b21253ef374

### AI (no-evidence-found)

No explicit development-AI attribution found in inspected README, selected source/build files and head commit; non-use is not inferred.
- https://github.com/gus0650/GusGames64/blob/734a310c88060b9200606c5ff1bf5b21253ef374/README.md
- https://github.com/gus0650/GusGames64/blob/734a310c88060b9200606c5ff1bf5b21253ef374/src/moonlander.prg
- https://github.com/gus0650/GusGames64/commit/734a310c88060b9200606c5ff1bf5b21253ef374

### Relationships (reviewed)

One authored game collection, retained at repository root rather than creating a separate entry for every BASIC file. No independent restoration from machine code is claimed.
- https://github.com/gus0650/GusGames64/blob/734a310c88060b9200606c5ff1bf5b21253ef374/README.md
- https://github.com/gus0650/GusGames64/blob/734a310c88060b9200606c5ff1bf5b21253ef374/src/moonlander.prg
- https://github.com/gus0650/GusGames64/commit/734a310c88060b9200606c5ff1bf5b21253ef374

## Blower

Project ID: blower-amiga-port · Overall audit: reviewed

### Typed catalogue values

```json
{
  "ai": {
    "tools": [
      "Midjourney"
    ],
    "usage": true
  },
  "build": {
    "byte_exact": null,
    "compilable": null,
    "playable": null,
    "runnable": null
  },
  "display_title": "Blower",
  "id": "blower-amiga-port",
  "last_activity": "2022-11-07",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "Blitz Basic"
  ],
  "record_class": "subject",
  "repo": "https://github.com/youenchene/blower",
  "runtime_profiles": [
    {
      "cpu_family": "m68k",
      "evidence": [
        "https://github.com/youenchene/blower/blob/03a91c4201e093e5a31c7fc55cf1b7638ce5dce4/README.md"
      ],
      "min_chip_ram_kib": 1024,
      "name": "Documented Amiga requirement",
      "notes": "README says compatible with all Amigas with 1 MiB Chip RAM and reports A500/A1200/CDTV tests; not independently tested.",
      "platform": "Amiga"
    }
  ],
  "source_cpu": [
    "x86"
  ],
  "source_language": [
    "Pascal",
    "x86 assembly"
  ],
  "source_platforms": [
    "DOS"
  ],
  "status": "Primary source reviewed; independent build/play test not performed",
  "subjects": [
    "Blower"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build",
    "catalogue-to-source"
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
  "title": "Blower",
  "tool_kinds": [],
  "types": [
    "source-available game"
  ],
  "upstream_name": "Blower",
  "work_kinds": []
}
```

### Identity (reviewed)

Four-player local combat game ported from the author’s 1996–1997 DOS Pascal/x86 game for the Amiga Blitz Basic Game Jam.
- https://github.com/youenchene/blower/blob/03a91c4201e093e5a31c7fc55cf1b7638ce5dce4/README.md
- https://github.com/youenchene/blower/blob/03a91c4201e093e5a31c7fc55cf1b7638ce5dce4/blower.bba
- https://github.com/youenchene/blower/commit/03a91c4201e093e5a31c7fc55cf1b7638ce5dce4
- https://youenchene.itch.io/blower

### Classification (reviewed)

Source-available native game or authored port; no byte-exact binary reconstruction claim.
- https://github.com/youenchene/blower/blob/03a91c4201e093e5a31c7fc55cf1b7638ce5dce4/README.md
- https://github.com/youenchene/blower/blob/03a91c4201e093e5a31c7fc55cf1b7638ce5dce4/blower.bba
- https://github.com/youenchene/blower/commit/03a91c4201e093e5a31c7fc55cf1b7638ce5dce4
- https://youenchene.itch.io/blower

### Source CPU (reviewed)

Source lineage/platform is documented in the linked README and reviewed source; source CPU is distinct from host-side tooling.
- https://github.com/youenchene/blower/blob/03a91c4201e093e5a31c7fc55cf1b7638ce5dce4/README.md
- https://github.com/youenchene/blower/blob/03a91c4201e093e5a31c7fc55cf1b7638ce5dce4/blower.bba
- https://github.com/youenchene/blower/commit/03a91c4201e093e5a31c7fc55cf1b7638ce5dce4
- https://youenchene.itch.io/blower

### Target CPU (reviewed)

Native Amiga output on the m68k family is established by the README and reviewed source; Python/Java build tools are host-side.
- https://github.com/youenchene/blower/blob/03a91c4201e093e5a31c7fc55cf1b7638ce5dce4/README.md
- https://github.com/youenchene/blower/blob/03a91c4201e093e5a31c7fc55cf1b7638ce5dce4/blower.bba
- https://github.com/youenchene/blower/commit/03a91c4201e093e5a31c7fc55cf1b7638ce5dce4
- https://youenchene.itch.io/blower

### Build (reviewed)

Readable blower.bba and assets accompany ADF, hard-disk, CDTV and CD32 releases. README documents Ultimate Blitz Basic 2.1 and testing on A500/A1200/CDTV. No independent rebuild, gameplay test or byte-exact comparison was performed.
- https://github.com/youenchene/blower/blob/03a91c4201e093e5a31c7fc55cf1b7638ce5dce4/README.md
- https://github.com/youenchene/blower/blob/03a91c4201e093e5a31c7fc55cf1b7638ce5dce4/blower.bba
- https://github.com/youenchene/blower/commit/03a91c4201e093e5a31c7fc55cf1b7638ce5dce4
- https://youenchene.itch.io/blower

### Runtime profiles (reviewed)

README says compatible with all Amigas with 1 MiB Chip RAM and reports A500/A1200/CDTV tests; not independently tested.
- https://github.com/youenchene/blower/blob/03a91c4201e093e5a31c7fc55cf1b7638ce5dce4/README.md
- https://github.com/youenchene/blower/blob/03a91c4201e093e5a31c7fc55cf1b7638ce5dce4/blower.bba
- https://github.com/youenchene/blower/commit/03a91c4201e093e5a31c7fc55cf1b7638ce5dce4
- https://youenchene.itch.io/blower

### AI (reviewed)

README explicitly credits Midjourney for the title screen alongside Grafx2; this does not establish AI-generated game code.
- https://github.com/youenchene/blower/blob/03a91c4201e093e5a31c7fc55cf1b7638ce5dce4/README.md
- https://github.com/youenchene/blower/blob/03a91c4201e093e5a31c7fc55cf1b7638ce5dce4/blower.bba
- https://github.com/youenchene/blower/commit/03a91c4201e093e5a31c7fc55cf1b7638ce5dce4
- https://youenchene.itch.io/blower

### Relationships (reviewed)

Distinct source-available game; current catalogue and prior decision URLs were screened before addition.
- https://github.com/youenchene/blower/blob/03a91c4201e093e5a31c7fc55cf1b7638ce5dce4/README.md
- https://github.com/youenchene/blower/blob/03a91c4201e093e5a31c7fc55cf1b7638ce5dce4/blower.bba
- https://github.com/youenchene/blower/commit/03a91c4201e093e5a31c7fc55cf1b7638ce5dce4
- https://youenchene.itch.io/blower

## SG Invaders MMXXVI

Project ID: sg-invaders-c64 · Overall audit: reviewed

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
  "display_title": "SG Invaders MMXXVI",
  "id": "sg-invaders-c64",
  "last_activity": "2026-03-26",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "Turbo Rascal",
    "6502 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/sveinjo/Space-Invaders-64",
  "runtime_profiles": [],
  "source_cpu": [
    "8080"
  ],
  "source_language": [
    "8080 assembly"
  ],
  "source_platforms": [
    "Arcade"
  ],
  "status": "Primary source reviewed; independent build/play test not performed",
  "subjects": [
    "SG Invaders MMXXVI"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build",
    "catalogue-to-source"
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
  "title": "SG Invaders MMXXVI",
  "tool_kinds": [],
  "types": [
    "source-available game"
  ],
  "upstream_name": "SG Invaders MMXXVI",
  "work_kinds": [
    "reimplementation",
    "binary-analysis"
  ]
}
```

### Identity (reviewed)

Native C64 Space Invaders adaptation using raster-driven sprite multiplexing, with Intel 8080 disassembly/analysis material in the repository.
- https://github.com/sveinjo/Space-Invaders-64/blob/2a729bebdd6fbaeb4b75c57f577dc3ae5aa066a3/README.md
- https://github.com/sveinjo/Space-Invaders-64/blob/2a729bebdd6fbaeb4b75c57f577dc3ae5aa066a3/SpaceInvaders64.ras
- https://github.com/sveinjo/Space-Invaders-64/blob/2a729bebdd6fbaeb4b75c57f577dc3ae5aa066a3/.github/copilot-instructions.md
- https://github.com/sveinjo/Space-Invaders-64/commit/2a729bebdd6fbaeb4b75c57f577dc3ae5aa066a3
- https://sveinacious-g.itch.io/invaders

### Classification (reviewed)

Source-available native game or authored port; no byte-exact binary reconstruction claim.
- https://github.com/sveinjo/Space-Invaders-64/blob/2a729bebdd6fbaeb4b75c57f577dc3ae5aa066a3/README.md
- https://github.com/sveinjo/Space-Invaders-64/blob/2a729bebdd6fbaeb4b75c57f577dc3ae5aa066a3/SpaceInvaders64.ras
- https://github.com/sveinjo/Space-Invaders-64/blob/2a729bebdd6fbaeb4b75c57f577dc3ae5aa066a3/.github/copilot-instructions.md
- https://github.com/sveinjo/Space-Invaders-64/commit/2a729bebdd6fbaeb4b75c57f577dc3ae5aa066a3
- https://sveinacious-g.itch.io/invaders

### Source CPU (reviewed)

Source lineage/platform is documented in the linked README and reviewed source; source CPU is distinct from host-side tooling.
- https://github.com/sveinjo/Space-Invaders-64/blob/2a729bebdd6fbaeb4b75c57f577dc3ae5aa066a3/README.md
- https://github.com/sveinjo/Space-Invaders-64/blob/2a729bebdd6fbaeb4b75c57f577dc3ae5aa066a3/SpaceInvaders64.ras
- https://github.com/sveinjo/Space-Invaders-64/blob/2a729bebdd6fbaeb4b75c57f577dc3ae5aa066a3/.github/copilot-instructions.md
- https://github.com/sveinjo/Space-Invaders-64/commit/2a729bebdd6fbaeb4b75c57f577dc3ae5aa066a3
- https://sveinacious-g.itch.io/invaders

### Target CPU (reviewed)

Native Commodore 64 output on the 6502 family is established by the README and reviewed source; Python/Java build tools are host-side.
- https://github.com/sveinjo/Space-Invaders-64/blob/2a729bebdd6fbaeb4b75c57f577dc3ae5aa066a3/README.md
- https://github.com/sveinjo/Space-Invaders-64/blob/2a729bebdd6fbaeb4b75c57f577dc3ae5aa066a3/SpaceInvaders64.ras
- https://github.com/sveinjo/Space-Invaders-64/blob/2a729bebdd6fbaeb4b75c57f577dc3ae5aa066a3/.github/copilot-instructions.md
- https://github.com/sveinjo/Space-Invaders-64/commit/2a729bebdd6fbaeb4b75c57f577dc3ae5aa066a3
- https://sveinacious-g.itch.io/invaders

### Build (reviewed)

TRSE project, Turbo Rascal source and generated assembly plus PRG releases are present. README still describes an early engine stage; linked release page describes a released PAL/NTSC game. Those differing descriptions do not establish independently tested playability. No independent rebuild, gameplay test or byte-exact comparison was performed.
- https://github.com/sveinjo/Space-Invaders-64/blob/2a729bebdd6fbaeb4b75c57f577dc3ae5aa066a3/README.md
- https://github.com/sveinjo/Space-Invaders-64/blob/2a729bebdd6fbaeb4b75c57f577dc3ae5aa066a3/SpaceInvaders64.ras
- https://github.com/sveinjo/Space-Invaders-64/blob/2a729bebdd6fbaeb4b75c57f577dc3ae5aa066a3/.github/copilot-instructions.md
- https://github.com/sveinjo/Space-Invaders-64/commit/2a729bebdd6fbaeb4b75c57f577dc3ae5aa066a3
- https://sveinacious-g.itch.io/invaders

### Runtime profiles (no-evidence-found)

No full minimum hardware profile was established in the inspected material; platform does not imply an exact minimum configuration.
- https://github.com/sveinjo/Space-Invaders-64/blob/2a729bebdd6fbaeb4b75c57f577dc3ae5aa066a3/README.md
- https://github.com/sveinjo/Space-Invaders-64/blob/2a729bebdd6fbaeb4b75c57f577dc3ae5aa066a3/SpaceInvaders64.ras
- https://github.com/sveinjo/Space-Invaders-64/blob/2a729bebdd6fbaeb4b75c57f577dc3ae5aa066a3/.github/copilot-instructions.md
- https://github.com/sveinjo/Space-Invaders-64/commit/2a729bebdd6fbaeb4b75c57f577dc3ae5aa066a3
- https://sveinacious-g.itch.io/invaders

### AI (no-evidence-found)

Release page declares no generative AI, while repository contains Copilot guidance. Configuration alone proves neither use nor non-use in development; leave development-AI usage unknown.
- https://github.com/sveinjo/Space-Invaders-64/blob/2a729bebdd6fbaeb4b75c57f577dc3ae5aa066a3/README.md
- https://github.com/sveinjo/Space-Invaders-64/blob/2a729bebdd6fbaeb4b75c57f577dc3ae5aa066a3/SpaceInvaders64.ras
- https://github.com/sveinjo/Space-Invaders-64/blob/2a729bebdd6fbaeb4b75c57f577dc3ae5aa066a3/.github/copilot-instructions.md
- https://github.com/sveinjo/Space-Invaders-64/commit/2a729bebdd6fbaeb4b75c57f577dc3ae5aa066a3
- https://sveinacious-g.itch.io/invaders

### Relationships (reviewed)

Native C64 adaptation, not a browser-only remake: bundled browser emulator is a distribution wrapper. Original arcade analysis is separate from the authored C64 runtime.
- https://github.com/sveinjo/Space-Invaders-64/blob/2a729bebdd6fbaeb4b75c57f577dc3ae5aa066a3/README.md
- https://github.com/sveinjo/Space-Invaders-64/blob/2a729bebdd6fbaeb4b75c57f577dc3ae5aa066a3/SpaceInvaders64.ras
- https://github.com/sveinjo/Space-Invaders-64/blob/2a729bebdd6fbaeb4b75c57f577dc3ae5aa066a3/.github/copilot-instructions.md
- https://github.com/sveinjo/Space-Invaders-64/commit/2a729bebdd6fbaeb4b75c57f577dc3ae5aa066a3
- https://sveinacious-g.itch.io/invaders

## Light Cycle Duel

Project ID: light-cycle-duel-c64 · Overall audit: reviewed

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
  "display_title": "Light Cycle Duel",
  "id": "light-cycle-duel-c64",
  "last_activity": "2026-09-18",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "Turbo Rascal"
  ],
  "record_class": "subject",
  "repo": "https://github.com/fuzzybad/trse/tree/main/c64/LightCycles",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/play test not performed",
  "subjects": [
    "Light Cycle Duel"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build",
    "catalogue-to-source"
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
  "title": "Light Cycle Duel",
  "tool_kinds": [],
  "types": [
    "source-available game"
  ],
  "upstream_name": "Light Cycle Duel",
  "work_kinds": []
}
```

### Identity (reviewed)

One- or two-player C64 light-cycle game with a computer opponent, published with editable TRSE sources.
- https://github.com/fuzzybad/trse/blob/1ef444209650bfa15e73e1ea88a15803fcb182ad/README.md
- https://github.com/fuzzybad/trse/blob/1ef444209650bfa15e73e1ea88a15803fcb182ad/c64/LightCycles/main.ras
- https://github.com/fuzzybad/trse/commit/1ef444209650bfa15e73e1ea88a15803fcb182ad
- https://fuzzybad.itch.io/c64-light-cycle-duel

### Classification (reviewed)

Source-available native game or authored port; no byte-exact binary reconstruction claim.
- https://github.com/fuzzybad/trse/blob/1ef444209650bfa15e73e1ea88a15803fcb182ad/README.md
- https://github.com/fuzzybad/trse/blob/1ef444209650bfa15e73e1ea88a15803fcb182ad/c64/LightCycles/main.ras
- https://github.com/fuzzybad/trse/commit/1ef444209650bfa15e73e1ea88a15803fcb182ad
- https://fuzzybad.itch.io/c64-light-cycle-duel

### Source CPU (not-applicable)

No identified predecessor binary is reconstructed; original source platform and CPU are left empty.
- https://github.com/fuzzybad/trse/blob/1ef444209650bfa15e73e1ea88a15803fcb182ad/README.md
- https://github.com/fuzzybad/trse/blob/1ef444209650bfa15e73e1ea88a15803fcb182ad/c64/LightCycles/main.ras
- https://github.com/fuzzybad/trse/commit/1ef444209650bfa15e73e1ea88a15803fcb182ad
- https://fuzzybad.itch.io/c64-light-cycle-duel

### Target CPU (reviewed)

Native Commodore 64 output on the 6502 family is established by the README and reviewed source; Python/Java build tools are host-side.
- https://github.com/fuzzybad/trse/blob/1ef444209650bfa15e73e1ea88a15803fcb182ad/README.md
- https://github.com/fuzzybad/trse/blob/1ef444209650bfa15e73e1ea88a15803fcb182ad/c64/LightCycles/main.ras
- https://github.com/fuzzybad/trse/commit/1ef444209650bfa15e73e1ea88a15803fcb182ad
- https://fuzzybad.itch.io/c64-light-cycle-duel

### Build (reviewed)

Inspected main.ras implements input, positions, collision, game state and drawing; supporting .ras files and PRGs are supplied. No independent rebuild, gameplay test or byte-exact comparison was performed.
- https://github.com/fuzzybad/trse/blob/1ef444209650bfa15e73e1ea88a15803fcb182ad/README.md
- https://github.com/fuzzybad/trse/blob/1ef444209650bfa15e73e1ea88a15803fcb182ad/c64/LightCycles/main.ras
- https://github.com/fuzzybad/trse/commit/1ef444209650bfa15e73e1ea88a15803fcb182ad
- https://fuzzybad.itch.io/c64-light-cycle-duel

### Runtime profiles (no-evidence-found)

No full minimum hardware profile was established in the inspected material; platform does not imply an exact minimum configuration.
- https://github.com/fuzzybad/trse/blob/1ef444209650bfa15e73e1ea88a15803fcb182ad/README.md
- https://github.com/fuzzybad/trse/blob/1ef444209650bfa15e73e1ea88a15803fcb182ad/c64/LightCycles/main.ras
- https://github.com/fuzzybad/trse/commit/1ef444209650bfa15e73e1ea88a15803fcb182ad
- https://fuzzybad.itch.io/c64-light-cycle-duel

### AI (no-evidence-found)

No explicit development-AI attribution found in inspected README, selected source/build files and head commit; non-use is not inferred.
- https://github.com/fuzzybad/trse/blob/1ef444209650bfa15e73e1ea88a15803fcb182ad/README.md
- https://github.com/fuzzybad/trse/blob/1ef444209650bfa15e73e1ea88a15803fcb182ad/c64/LightCycles/main.ras
- https://github.com/fuzzybad/trse/commit/1ef444209650bfa15e73e1ea88a15803fcb182ad
- https://fuzzybad.itch.io/c64-light-cycle-duel

### Relationships (reviewed)

Use the game-specific subdirectory because repository root is a mixed collection of PET/C128 demos, utilities and experiments. This entry covers original Light Cycle Duel, not the separately advertised Deluxe edition.
- https://github.com/fuzzybad/trse/blob/1ef444209650bfa15e73e1ea88a15803fcb182ad/README.md
- https://github.com/fuzzybad/trse/blob/1ef444209650bfa15e73e1ea88a15803fcb182ad/c64/LightCycles/main.ras
- https://github.com/fuzzybad/trse/commit/1ef444209650bfa15e73e1ea88a15803fcb182ad
- https://fuzzybad.itch.io/c64-light-cycle-duel

## Populous Amiga Creature Fix

Project ID: populous-amiga-creature-fix · Overall audit: reviewed

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
  "display_title": "Populous Amiga Creature Fix",
  "id": "populous-amiga-creature-fix",
  "last_activity": "2026-10-03",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "m68k assembly",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/timoheimonen/Populous-Amiga-funny-creature-fix",
  "runtime_profiles": [],
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
    "Populous Amiga Creature Fix"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build",
    "developer-following"
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
  "title": "Populous Amiga Creature Fix",
  "tool_kinds": [],
  "types": [
    "game enhancement"
  ],
  "upstream_name": "Populous Amiga Creature Fix",
  "work_kinds": [
    "patching"
  ]
}
```

### Identity (reviewed)

Game-specific restoration of wizard, swamp-monster and rock-monster spawning; documents missing stack argument, off-map position, repeated paused spawning and invalid table-full check.
- https://github.com/timoheimonen/Populous-Amiga-funny-creature-fix/blob/beed7c79a5762dde63daef53ea1f79df5fc0fc94/README.md
- https://github.com/timoheimonen/Populous-Amiga-funny-creature-fix/blob/beed7c79a5762dde63daef53ea1f79df5fc0fc94/src/funny_fix.s
- https://github.com/timoheimonen/Populous-Amiga-funny-creature-fix/commit/beed7c79a5762dde63daef53ea1f79df5fc0fc94

### Classification (reviewed)

Native game-specific enhancement, not a complete original-binary restoration.
- https://github.com/timoheimonen/Populous-Amiga-funny-creature-fix/blob/beed7c79a5762dde63daef53ea1f79df5fc0fc94/README.md
- https://github.com/timoheimonen/Populous-Amiga-funny-creature-fix/blob/beed7c79a5762dde63daef53ea1f79df5fc0fc94/src/funny_fix.s
- https://github.com/timoheimonen/Populous-Amiga-funny-creature-fix/commit/beed7c79a5762dde63daef53ea1f79df5fc0fc94

### Source CPU (reviewed)

Source lineage/platform is documented in the linked README and reviewed source; source CPU is distinct from host-side tooling.
- https://github.com/timoheimonen/Populous-Amiga-funny-creature-fix/blob/beed7c79a5762dde63daef53ea1f79df5fc0fc94/README.md
- https://github.com/timoheimonen/Populous-Amiga-funny-creature-fix/blob/beed7c79a5762dde63daef53ea1f79df5fc0fc94/src/funny_fix.s
- https://github.com/timoheimonen/Populous-Amiga-funny-creature-fix/commit/beed7c79a5762dde63daef53ea1f79df5fc0fc94

### Target CPU (reviewed)

Native Amiga output on the m68k family is established by the README and reviewed source; Python/Java build tools are host-side.
- https://github.com/timoheimonen/Populous-Amiga-funny-creature-fix/blob/beed7c79a5762dde63daef53ea1f79df5fc0fc94/README.md
- https://github.com/timoheimonen/Populous-Amiga-funny-creature-fix/blob/beed7c79a5762dde63daef53ea1f79df5fc0fc94/src/funny_fix.s
- https://github.com/timoheimonen/Populous-Amiga-funny-creature-fix/commit/beed7c79a5762dde63daef53ea1f79df5fc0fc94

### Build (reviewed)

Readable 68000 patch source and Python disk patcher; optional vasm comparison verifies embedded patch bytes. User must supply the exact supported disk image. Upstream behavioral measurements are reported, not independently reproduced. No independent rebuild, gameplay test or byte-exact comparison was performed.
- https://github.com/timoheimonen/Populous-Amiga-funny-creature-fix/blob/beed7c79a5762dde63daef53ea1f79df5fc0fc94/README.md
- https://github.com/timoheimonen/Populous-Amiga-funny-creature-fix/blob/beed7c79a5762dde63daef53ea1f79df5fc0fc94/src/funny_fix.s
- https://github.com/timoheimonen/Populous-Amiga-funny-creature-fix/commit/beed7c79a5762dde63daef53ea1f79df5fc0fc94

### Runtime profiles (no-evidence-found)

No full minimum hardware profile was established in the inspected material; platform does not imply an exact minimum configuration.
- https://github.com/timoheimonen/Populous-Amiga-funny-creature-fix/blob/beed7c79a5762dde63daef53ea1f79df5fc0fc94/README.md
- https://github.com/timoheimonen/Populous-Amiga-funny-creature-fix/blob/beed7c79a5762dde63daef53ea1f79df5fc0fc94/src/funny_fix.s
- https://github.com/timoheimonen/Populous-Amiga-funny-creature-fix/commit/beed7c79a5762dde63daef53ea1f79df5fc0fc94

### AI (no-evidence-found)

No explicit development-AI attribution found in inspected README, selected source/build files and head commit; non-use is not inferred.
- https://github.com/timoheimonen/Populous-Amiga-funny-creature-fix/blob/beed7c79a5762dde63daef53ea1f79df5fc0fc94/README.md
- https://github.com/timoheimonen/Populous-Amiga-funny-creature-fix/blob/beed7c79a5762dde63daef53ea1f79df5fc0fc94/src/funny_fix.s
- https://github.com/timoheimonen/Populous-Amiga-funny-creature-fix/commit/beed7c79a5762dde63daef53ea1f79df5fc0fc94

### Relationships (reviewed)

Separate platform-specific patch implementation, not a mirror of the other platform or the existing tetracorp/populous disassembly. No original game files supplied; linked two-player games require matching versions.
- https://github.com/timoheimonen/Populous-Amiga-funny-creature-fix/blob/beed7c79a5762dde63daef53ea1f79df5fc0fc94/README.md
- https://github.com/timoheimonen/Populous-Amiga-funny-creature-fix/blob/beed7c79a5762dde63daef53ea1f79df5fc0fc94/src/funny_fix.s
- https://github.com/timoheimonen/Populous-Amiga-funny-creature-fix/commit/beed7c79a5762dde63daef53ea1f79df5fc0fc94

## Populous Atari ST Creature Fix

Project ID: populous-atari-st-creature-fix · Overall audit: reviewed

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
  "display_title": "Populous Atari ST Creature Fix",
  "id": "populous-atari-st-creature-fix",
  "last_activity": "2026-10-04",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "m68k assembly",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/timoheimonen/Populous-Atari-funny-creature-fix",
  "runtime_profiles": [],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [
    "m68k machine code"
  ],
  "source_platforms": [
    "Atari ST"
  ],
  "status": "Primary source reviewed; independent build/play test not performed",
  "subjects": [
    "Populous Atari ST Creature Fix"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build",
    "developer-following"
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
  "title": "Populous Atari ST Creature Fix",
  "tool_kinds": [],
  "types": [
    "game enhancement"
  ],
  "upstream_name": "Populous Atari ST Creature Fix",
  "work_kinds": [
    "patching"
  ]
}
```

### Identity (reviewed)

Game-specific restoration of wizard, swamp-monster and rock-monster spawning; documents missing stack argument, off-map position, repeated paused spawning and invalid table-full check.
- https://github.com/timoheimonen/Populous-Atari-funny-creature-fix/blob/88ddd56c2629f67c56112bc5e4265c1258625ead/README.md
- https://github.com/timoheimonen/Populous-Atari-funny-creature-fix/blob/88ddd56c2629f67c56112bc5e4265c1258625ead/src/funny_fix.s
- https://github.com/timoheimonen/Populous-Atari-funny-creature-fix/commit/88ddd56c2629f67c56112bc5e4265c1258625ead

### Classification (reviewed)

Native game-specific enhancement, not a complete original-binary restoration.
- https://github.com/timoheimonen/Populous-Atari-funny-creature-fix/blob/88ddd56c2629f67c56112bc5e4265c1258625ead/README.md
- https://github.com/timoheimonen/Populous-Atari-funny-creature-fix/blob/88ddd56c2629f67c56112bc5e4265c1258625ead/src/funny_fix.s
- https://github.com/timoheimonen/Populous-Atari-funny-creature-fix/commit/88ddd56c2629f67c56112bc5e4265c1258625ead

### Source CPU (reviewed)

Source lineage/platform is documented in the linked README and reviewed source; source CPU is distinct from host-side tooling.
- https://github.com/timoheimonen/Populous-Atari-funny-creature-fix/blob/88ddd56c2629f67c56112bc5e4265c1258625ead/README.md
- https://github.com/timoheimonen/Populous-Atari-funny-creature-fix/blob/88ddd56c2629f67c56112bc5e4265c1258625ead/src/funny_fix.s
- https://github.com/timoheimonen/Populous-Atari-funny-creature-fix/commit/88ddd56c2629f67c56112bc5e4265c1258625ead

### Target CPU (reviewed)

Native Atari ST output on the m68k family is established by the README and reviewed source; Python/Java build tools are host-side.
- https://github.com/timoheimonen/Populous-Atari-funny-creature-fix/blob/88ddd56c2629f67c56112bc5e4265c1258625ead/README.md
- https://github.com/timoheimonen/Populous-Atari-funny-creature-fix/blob/88ddd56c2629f67c56112bc5e4265c1258625ead/src/funny_fix.s
- https://github.com/timoheimonen/Populous-Atari-funny-creature-fix/commit/88ddd56c2629f67c56112bc5e4265c1258625ead

### Build (reviewed)

Readable 68000 patch source and Python disk patcher; optional vasm comparison verifies embedded patch bytes. User must supply the exact supported disk image. Upstream behavioral measurements are reported, not independently reproduced. No independent rebuild, gameplay test or byte-exact comparison was performed.
- https://github.com/timoheimonen/Populous-Atari-funny-creature-fix/blob/88ddd56c2629f67c56112bc5e4265c1258625ead/README.md
- https://github.com/timoheimonen/Populous-Atari-funny-creature-fix/blob/88ddd56c2629f67c56112bc5e4265c1258625ead/src/funny_fix.s
- https://github.com/timoheimonen/Populous-Atari-funny-creature-fix/commit/88ddd56c2629f67c56112bc5e4265c1258625ead

### Runtime profiles (no-evidence-found)

No full minimum hardware profile was established in the inspected material; platform does not imply an exact minimum configuration.
- https://github.com/timoheimonen/Populous-Atari-funny-creature-fix/blob/88ddd56c2629f67c56112bc5e4265c1258625ead/README.md
- https://github.com/timoheimonen/Populous-Atari-funny-creature-fix/blob/88ddd56c2629f67c56112bc5e4265c1258625ead/src/funny_fix.s
- https://github.com/timoheimonen/Populous-Atari-funny-creature-fix/commit/88ddd56c2629f67c56112bc5e4265c1258625ead

### AI (no-evidence-found)

No explicit development-AI attribution found in inspected README, selected source/build files and head commit; non-use is not inferred.
- https://github.com/timoheimonen/Populous-Atari-funny-creature-fix/blob/88ddd56c2629f67c56112bc5e4265c1258625ead/README.md
- https://github.com/timoheimonen/Populous-Atari-funny-creature-fix/blob/88ddd56c2629f67c56112bc5e4265c1258625ead/src/funny_fix.s
- https://github.com/timoheimonen/Populous-Atari-funny-creature-fix/commit/88ddd56c2629f67c56112bc5e4265c1258625ead

### Relationships (reviewed)

Separate platform-specific patch implementation, not a mirror of the other platform or the existing tetracorp/populous disassembly. No original game files supplied; linked two-player games require matching versions.
- https://github.com/timoheimonen/Populous-Atari-funny-creature-fix/blob/88ddd56c2629f67c56112bc5e4265c1258625ead/README.md
- https://github.com/timoheimonen/Populous-Atari-funny-creature-fix/blob/88ddd56c2629f67c56112bc5e4265c1258625ead/src/funny_fix.s
- https://github.com/timoheimonen/Populous-Atari-funny-creature-fix/commit/88ddd56c2629f67c56112bc5e4265c1258625ead

## Ultima V Atari ST Inn Fix

Project ID: ultima-v-atari-st-inn-fix · Overall audit: reviewed

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
  "display_title": "Ultima V Atari ST Inn Fix",
  "id": "ultima-v-atari-st-inn-fix",
  "last_activity": "2026-10-04",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "m68k assembly",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/timoheimonen/atari-st-ultima-5-inn-fix",
  "runtime_profiles": [],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [
    "m68k machine code"
  ],
  "source_platforms": [
    "Atari ST"
  ],
  "status": "Primary source reviewed; independent build/play test not performed",
  "subjects": [
    "Ultima V Atari ST Inn Fix"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build",
    "developer-following"
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
  "title": "Ultima V Atari ST Inn Fix",
  "tool_kinds": [],
  "types": [
    "game enhancement"
  ],
  "upstream_name": "Ultima V Atari ST Inn Fix",
  "work_kinds": [
    "patching"
  ]
}
```

### Identity (reviewed)

Fixes active-party-member index corruption when leaving a companion at an inn, which causes merchants to read an invalid buyer and charge maximum prices.
- https://github.com/timoheimonen/atari-st-ultima-5-inn-fix/blob/0914000555cf78b029007d2819d5d4e83ffeff66/README.md
- https://github.com/timoheimonen/atari-st-ultima-5-inn-fix/blob/0914000555cf78b029007d2819d5d4e83ffeff66/src/inn_fix.s
- https://github.com/timoheimonen/atari-st-ultima-5-inn-fix/commit/0914000555cf78b029007d2819d5d4e83ffeff66

### Classification (reviewed)

Native game-specific enhancement, not a complete original-binary restoration.
- https://github.com/timoheimonen/atari-st-ultima-5-inn-fix/blob/0914000555cf78b029007d2819d5d4e83ffeff66/README.md
- https://github.com/timoheimonen/atari-st-ultima-5-inn-fix/blob/0914000555cf78b029007d2819d5d4e83ffeff66/src/inn_fix.s
- https://github.com/timoheimonen/atari-st-ultima-5-inn-fix/commit/0914000555cf78b029007d2819d5d4e83ffeff66

### Source CPU (reviewed)

Source lineage/platform is documented in the linked README and reviewed source; source CPU is distinct from host-side tooling.
- https://github.com/timoheimonen/atari-st-ultima-5-inn-fix/blob/0914000555cf78b029007d2819d5d4e83ffeff66/README.md
- https://github.com/timoheimonen/atari-st-ultima-5-inn-fix/blob/0914000555cf78b029007d2819d5d4e83ffeff66/src/inn_fix.s
- https://github.com/timoheimonen/atari-st-ultima-5-inn-fix/commit/0914000555cf78b029007d2819d5d4e83ffeff66

### Target CPU (reviewed)

Native Atari ST output on the m68k family is established by the README and reviewed source; Python/Java build tools are host-side.
- https://github.com/timoheimonen/atari-st-ultima-5-inn-fix/blob/0914000555cf78b029007d2819d5d4e83ffeff66/README.md
- https://github.com/timoheimonen/atari-st-ultima-5-inn-fix/blob/0914000555cf78b029007d2819d5d4e83ffeff66/src/inn_fix.s
- https://github.com/timoheimonen/atari-st-ultima-5-inn-fix/commit/0914000555cf78b029007d2819d5d4e83ffeff66

### Build (reviewed)

Six-byte replacement described in readable 68000 source and applied by Python to a checksum-matched user disk. README reports before/after Hatari measurements; original game and emulator not run in this review. No independent rebuild, gameplay test or byte-exact comparison was performed.
- https://github.com/timoheimonen/atari-st-ultima-5-inn-fix/blob/0914000555cf78b029007d2819d5d4e83ffeff66/README.md
- https://github.com/timoheimonen/atari-st-ultima-5-inn-fix/blob/0914000555cf78b029007d2819d5d4e83ffeff66/src/inn_fix.s
- https://github.com/timoheimonen/atari-st-ultima-5-inn-fix/commit/0914000555cf78b029007d2819d5d4e83ffeff66

### Runtime profiles (no-evidence-found)

No full minimum hardware profile was established in the inspected material; platform does not imply an exact minimum configuration.
- https://github.com/timoheimonen/atari-st-ultima-5-inn-fix/blob/0914000555cf78b029007d2819d5d4e83ffeff66/README.md
- https://github.com/timoheimonen/atari-st-ultima-5-inn-fix/blob/0914000555cf78b029007d2819d5d4e83ffeff66/src/inn_fix.s
- https://github.com/timoheimonen/atari-st-ultima-5-inn-fix/commit/0914000555cf78b029007d2819d5d4e83ffeff66

### AI (no-evidence-found)

No explicit development-AI attribution found in inspected README, selected source/build files and head commit; non-use is not inferred.
- https://github.com/timoheimonen/atari-st-ultima-5-inn-fix/blob/0914000555cf78b029007d2819d5d4e83ffeff66/README.md
- https://github.com/timoheimonen/atari-st-ultima-5-inn-fix/blob/0914000555cf78b029007d2819d5d4e83ffeff66/src/inn_fix.s
- https://github.com/timoheimonen/atari-st-ultima-5-inn-fix/commit/0914000555cf78b029007d2819d5d4e83ffeff66

### Relationships (reviewed)

Distinct game-specific project; current catalogue and prior decision URLs were screened before addition. Original game files are not included in these patch repositories.
- https://github.com/timoheimonen/atari-st-ultima-5-inn-fix/blob/0914000555cf78b029007d2819d5d4e83ffeff66/README.md
- https://github.com/timoheimonen/atari-st-ultima-5-inn-fix/blob/0914000555cf78b029007d2819d5d4e83ffeff66/src/inn_fix.s
- https://github.com/timoheimonen/atari-st-ultima-5-inn-fix/commit/0914000555cf78b029007d2819d5d4e83ffeff66

## Hunter 68060 Performance Patch

Project ID: hunter-amiga-68060-performance · Overall audit: reviewed

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
  "display_title": "Hunter 68060 Performance Patch",
  "id": "hunter-amiga-68060-performance",
  "last_activity": "2026-09-11",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "m68k assembly",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/timoheimonen/amiga-hunter-performance-68060",
  "runtime_profiles": [
    {
      "cpu_family": "m68k",
      "evidence": [
        "https://github.com/timoheimonen/amiga-hunter-performance-68060/blob/4114ba01fa99f3f4ee0dd50a121bbc223d6f39c9/README.md"
      ],
      "min_cpu": "68060",
      "name": "Upstream documented emulator configuration",
      "notes": "README specifies FS-UAE, 2 MiB Chip RAM and emulated Blizzard 1260 with default 32 MiB accelerator RAM. Treat this as documented configuration, not an independently measured RAM minimum.",
      "os": "Kickstart 3.1",
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
    "Hunter 68060 Performance Patch"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build",
    "developer-following"
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
  "title": "Hunter 68060 Performance Patch",
  "tool_kinds": [],
  "types": [
    "game enhancement"
  ],
  "upstream_name": "Hunter 68060 Performance Patch",
  "work_kinds": [
    "patching"
  ]
}
```

### Identity (reviewed)

Accelerator-targeted Hunter patch with instruction-cache support, Fast RAM allocations, terrain/polygon optimizations and an expanded terrain depth window.
- https://github.com/timoheimonen/amiga-hunter-performance-68060/blob/4114ba01fa99f3f4ee0dd50a121bbc223d6f39c9/README.md
- https://github.com/timoheimonen/amiga-hunter-performance-68060/blob/4114ba01fa99f3f4ee0dd50a121bbc223d6f39c9/PATCH.md
- https://github.com/timoheimonen/amiga-hunter-performance-68060/commit/4114ba01fa99f3f4ee0dd50a121bbc223d6f39c9

### Classification (reviewed)

Native game-specific enhancement, not a complete original-binary restoration.
- https://github.com/timoheimonen/amiga-hunter-performance-68060/blob/4114ba01fa99f3f4ee0dd50a121bbc223d6f39c9/README.md
- https://github.com/timoheimonen/amiga-hunter-performance-68060/blob/4114ba01fa99f3f4ee0dd50a121bbc223d6f39c9/PATCH.md
- https://github.com/timoheimonen/amiga-hunter-performance-68060/commit/4114ba01fa99f3f4ee0dd50a121bbc223d6f39c9

### Source CPU (reviewed)

Source lineage/platform is documented in the linked README and reviewed source; source CPU is distinct from host-side tooling.
- https://github.com/timoheimonen/amiga-hunter-performance-68060/blob/4114ba01fa99f3f4ee0dd50a121bbc223d6f39c9/README.md
- https://github.com/timoheimonen/amiga-hunter-performance-68060/blob/4114ba01fa99f3f4ee0dd50a121bbc223d6f39c9/PATCH.md
- https://github.com/timoheimonen/amiga-hunter-performance-68060/commit/4114ba01fa99f3f4ee0dd50a121bbc223d6f39c9

### Target CPU (reviewed)

Native Amiga output on the m68k family is established by the README and reviewed source; Python/Java build tools are host-side.
- https://github.com/timoheimonen/amiga-hunter-performance-68060/blob/4114ba01fa99f3f4ee0dd50a121bbc223d6f39c9/README.md
- https://github.com/timoheimonen/amiga-hunter-performance-68060/blob/4114ba01fa99f3f4ee0dd50a121bbc223d6f39c9/PATCH.md
- https://github.com/timoheimonen/amiga-hunter-performance-68060/commit/4114ba01fa99f3f4ee0dd50a121bbc223d6f39c9

### Build (reviewed)

Python applies embedded patches to a matching user ADF; source and patch details are supplied. README documents FS-UAE/Blizzard 1260 setup rather than proving broad real-hardware compatibility. No independent rebuild, gameplay test or byte-exact comparison was performed.
- https://github.com/timoheimonen/amiga-hunter-performance-68060/blob/4114ba01fa99f3f4ee0dd50a121bbc223d6f39c9/README.md
- https://github.com/timoheimonen/amiga-hunter-performance-68060/blob/4114ba01fa99f3f4ee0dd50a121bbc223d6f39c9/PATCH.md
- https://github.com/timoheimonen/amiga-hunter-performance-68060/commit/4114ba01fa99f3f4ee0dd50a121bbc223d6f39c9

### Runtime profiles (reviewed)

README specifies FS-UAE, 2 MiB Chip RAM and emulated Blizzard 1260 with default 32 MiB accelerator RAM. Treat this as documented configuration, not an independently measured RAM minimum.
- https://github.com/timoheimonen/amiga-hunter-performance-68060/blob/4114ba01fa99f3f4ee0dd50a121bbc223d6f39c9/README.md
- https://github.com/timoheimonen/amiga-hunter-performance-68060/blob/4114ba01fa99f3f4ee0dd50a121bbc223d6f39c9/PATCH.md
- https://github.com/timoheimonen/amiga-hunter-performance-68060/commit/4114ba01fa99f3f4ee0dd50a121bbc223d6f39c9

### AI (no-evidence-found)

No explicit development-AI attribution found in inspected README, selected source/build files and head commit; non-use is not inferred.
- https://github.com/timoheimonen/amiga-hunter-performance-68060/blob/4114ba01fa99f3f4ee0dd50a121bbc223d6f39c9/README.md
- https://github.com/timoheimonen/amiga-hunter-performance-68060/blob/4114ba01fa99f3f4ee0dd50a121bbc223d6f39c9/PATCH.md
- https://github.com/timoheimonen/amiga-hunter-performance-68060/commit/4114ba01fa99f3f4ee0dd50a121bbc223d6f39c9

### Relationships (reviewed)

Distinct game-specific project; current catalogue and prior decision URLs were screened before addition. Original game files are not included in these patch repositories.
- https://github.com/timoheimonen/amiga-hunter-performance-68060/blob/4114ba01fa99f3f4ee0dd50a121bbc223d6f39c9/README.md
- https://github.com/timoheimonen/amiga-hunter-performance-68060/blob/4114ba01fa99f3f4ee0dd50a121bbc223d6f39c9/PATCH.md
- https://github.com/timoheimonen/amiga-hunter-performance-68060/commit/4114ba01fa99f3f4ee0dd50a121bbc223d6f39c9

## Lemmings and Holiday Lemmings In-Game Editor

Project ID: lemmings-amiga-ingame-editor · Overall audit: reviewed

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
  "display_title": "Lemmings and Holiday Lemmings In-Game Editor",
  "id": "lemmings-amiga-ingame-editor",
  "last_activity": "2026-10-08",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "m68k assembly",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/timoheimonen/Amiga-Lemmings-Editor",
  "runtime_profiles": [
    {
      "cpu_family": "m68k",
      "evidence": [
        "https://github.com/timoheimonen/Amiga-Lemmings-Editor/blob/1e64e68957fb5bb5ad44af5da968896846971d50/README.md"
      ],
      "min_chip_ram_kib": 512,
      "name": "Lemmings floppy editor baseline",
      "notes": "README requires PAL A500 with 512 KiB Chip plus 512 KiB slow RAM; Holiday Lemmings requires 512 KiB Chip plus 512 KiB other memory. Upstream supplies real-A500 photographs; not independently tested.",
      "os": "Kickstart 1.3",
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
    "Lemmings and Holiday Lemmings In-Game Editor"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build",
    "developer-following"
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
  "title": "Lemmings and Holiday Lemmings In-Game Editor",
  "tool_kinds": [],
  "types": [
    "game enhancement"
  ],
  "upstream_name": "Lemmings and Holiday Lemmings In-Game Editor",
  "work_kinds": [
    "patching",
    "data-format-analysis"
  ]
}
```

### Identity (reviewed)

Adds custom levels and an in-game level editor to original Lemmings and Holiday Lemmings 1994, with floppy and WHDLoad installations.
- https://github.com/timoheimonen/Amiga-Lemmings-Editor/blob/1e64e68957fb5bb5ad44af5da968896846971d50/README.md
- https://github.com/timoheimonen/Amiga-Lemmings-Editor/blob/1e64e68957fb5bb5ad44af5da968896846971d50/build.py
- https://github.com/timoheimonen/Amiga-Lemmings-Editor/commit/1e64e68957fb5bb5ad44af5da968896846971d50

### Classification (reviewed)

Native game-specific enhancement, not a complete original-binary restoration.
- https://github.com/timoheimonen/Amiga-Lemmings-Editor/blob/1e64e68957fb5bb5ad44af5da968896846971d50/README.md
- https://github.com/timoheimonen/Amiga-Lemmings-Editor/blob/1e64e68957fb5bb5ad44af5da968896846971d50/build.py
- https://github.com/timoheimonen/Amiga-Lemmings-Editor/commit/1e64e68957fb5bb5ad44af5da968896846971d50

### Source CPU (reviewed)

Source lineage/platform is documented in the linked README and reviewed source; source CPU is distinct from host-side tooling.
- https://github.com/timoheimonen/Amiga-Lemmings-Editor/blob/1e64e68957fb5bb5ad44af5da968896846971d50/README.md
- https://github.com/timoheimonen/Amiga-Lemmings-Editor/blob/1e64e68957fb5bb5ad44af5da968896846971d50/build.py
- https://github.com/timoheimonen/Amiga-Lemmings-Editor/commit/1e64e68957fb5bb5ad44af5da968896846971d50

### Target CPU (reviewed)

Native Amiga output on the m68k family is established by the README and reviewed source; Python/Java build tools are host-side.
- https://github.com/timoheimonen/Amiga-Lemmings-Editor/blob/1e64e68957fb5bb5ad44af5da968896846971d50/README.md
- https://github.com/timoheimonen/Amiga-Lemmings-Editor/blob/1e64e68957fb5bb5ad44af5da968896846971d50/build.py
- https://github.com/timoheimonen/Amiga-Lemmings-Editor/commit/1e64e68957fb5bb5ad44af5da968896846971d50

### Build (reviewed)

build.py assembles native editor variants with vasm and embeds outputs into patch.py. User-supplied checksum-matched disks are required; source documents native level files and disk exchange. No independent rebuild, gameplay test or byte-exact comparison was performed.
- https://github.com/timoheimonen/Amiga-Lemmings-Editor/blob/1e64e68957fb5bb5ad44af5da968896846971d50/README.md
- https://github.com/timoheimonen/Amiga-Lemmings-Editor/blob/1e64e68957fb5bb5ad44af5da968896846971d50/build.py
- https://github.com/timoheimonen/Amiga-Lemmings-Editor/commit/1e64e68957fb5bb5ad44af5da968896846971d50

### Runtime profiles (reviewed)

README requires PAL A500 with 512 KiB Chip plus 512 KiB slow RAM; Holiday Lemmings requires 512 KiB Chip plus 512 KiB other memory. Upstream supplies real-A500 photographs; not independently tested.
- https://github.com/timoheimonen/Amiga-Lemmings-Editor/blob/1e64e68957fb5bb5ad44af5da968896846971d50/README.md
- https://github.com/timoheimonen/Amiga-Lemmings-Editor/blob/1e64e68957fb5bb5ad44af5da968896846971d50/build.py
- https://github.com/timoheimonen/Amiga-Lemmings-Editor/commit/1e64e68957fb5bb5ad44af5da968896846971d50

### AI (no-evidence-found)

No explicit development-AI attribution found in inspected README, selected source/build files and head commit; non-use is not inferred.
- https://github.com/timoheimonen/Amiga-Lemmings-Editor/blob/1e64e68957fb5bb5ad44af5da968896846971d50/README.md
- https://github.com/timoheimonen/Amiga-Lemmings-Editor/blob/1e64e68957fb5bb5ad44af5da968896846971d50/build.py
- https://github.com/timoheimonen/Amiga-Lemmings-Editor/commit/1e64e68957fb5bb5ad44af5da968896846971d50

### Relationships (reviewed)

Distinct from the already tracked Lemmings 2 editor. Lemmings and Holiday Lemmings share this coherent repository and are kept as one entry.
- https://github.com/timoheimonen/Amiga-Lemmings-Editor/blob/1e64e68957fb5bb5ad44af5da968896846971d50/README.md
- https://github.com/timoheimonen/Amiga-Lemmings-Editor/blob/1e64e68957fb5bb5ad44af5da968896846971d50/build.py
- https://github.com/timoheimonen/Amiga-Lemmings-Editor/commit/1e64e68957fb5bb5ad44af5da968896846971d50

## Street Rod 2 68060 Performance Patch

Project ID: street-rod-2-amiga-68060-patch · Overall audit: reviewed

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
  "display_title": "Street Rod 2 68060 Performance Patch",
  "id": "street-rod-2-amiga-68060-patch",
  "last_activity": "2026-09-26",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "m68k assembly",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/timoheimonen/amiga-sr2-060-performance-patch",
  "runtime_profiles": [
    {
      "chipsets": [
        "AGA"
      ],
      "cpu_family": "m68k",
      "evidence": [
        "https://github.com/timoheimonen/amiga-sr2-060-performance-patch/blob/1f1ff97e31a5627f5253fe8cf9ce60bbe3d779c5/README.md"
      ],
      "min_chip_ram_kib": 2048,
      "min_cpu": "68060",
      "min_fast_ram_kib": 2048,
      "name": "Documented patch requirement",
      "notes": "README explicitly requires PAL A1200/AGA and MC68060; primarily intended for emulation.",
      "os": "Kickstart 3.1 A1200 rev 40.68",
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
    "Street Rod 2 68060 Performance Patch"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build",
    "developer-following"
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
  "title": "Street Rod 2 68060 Performance Patch",
  "tool_kinds": [],
  "types": [
    "game enhancement"
  ],
  "upstream_name": "Street Rod 2 68060 Performance Patch",
  "work_kinds": [
    "patching"
  ]
}
```

### Identity (reviewed)

Accelerator-focused Street Rod 2 update covering audio timing, road-buffer timing/frame cap, drawing optimizations and instruction-cache handling.
- https://github.com/timoheimonen/amiga-sr2-060-performance-patch/blob/1f1ff97e31a5627f5253fe8cf9ce60bbe3d779c5/README.md
- https://github.com/timoheimonen/amiga-sr2-060-performance-patch/blob/1f1ff97e31a5627f5253fe8cf9ce60bbe3d779c5/PATCH.md
- https://github.com/timoheimonen/amiga-sr2-060-performance-patch/commit/1f1ff97e31a5627f5253fe8cf9ce60bbe3d779c5

### Classification (reviewed)

Native game-specific enhancement, not a complete original-binary restoration.
- https://github.com/timoheimonen/amiga-sr2-060-performance-patch/blob/1f1ff97e31a5627f5253fe8cf9ce60bbe3d779c5/README.md
- https://github.com/timoheimonen/amiga-sr2-060-performance-patch/blob/1f1ff97e31a5627f5253fe8cf9ce60bbe3d779c5/PATCH.md
- https://github.com/timoheimonen/amiga-sr2-060-performance-patch/commit/1f1ff97e31a5627f5253fe8cf9ce60bbe3d779c5

### Source CPU (reviewed)

Source lineage/platform is documented in the linked README and reviewed source; source CPU is distinct from host-side tooling.
- https://github.com/timoheimonen/amiga-sr2-060-performance-patch/blob/1f1ff97e31a5627f5253fe8cf9ce60bbe3d779c5/README.md
- https://github.com/timoheimonen/amiga-sr2-060-performance-patch/blob/1f1ff97e31a5627f5253fe8cf9ce60bbe3d779c5/PATCH.md
- https://github.com/timoheimonen/amiga-sr2-060-performance-patch/commit/1f1ff97e31a5627f5253fe8cf9ce60bbe3d779c5

### Target CPU (reviewed)

Native Amiga output on the m68k family is established by the README and reviewed source; Python/Java build tools are host-side.
- https://github.com/timoheimonen/amiga-sr2-060-performance-patch/blob/1f1ff97e31a5627f5253fe8cf9ce60bbe3d779c5/README.md
- https://github.com/timoheimonen/amiga-sr2-060-performance-patch/blob/1f1ff97e31a5627f5253fe8cf9ce60bbe3d779c5/PATCH.md
- https://github.com/timoheimonen/amiga-sr2-060-performance-patch/commit/1f1ff97e31a5627f5253fe8cf9ce60bbe3d779c5

### Build (reviewed)

Python patcher embeds native HUNK payloads; PATCH.md describes assembly helpers and expected/replacement byte manifest. Author primarily targets emulator play. No independent rebuild, gameplay test or byte-exact comparison was performed.
- https://github.com/timoheimonen/amiga-sr2-060-performance-patch/blob/1f1ff97e31a5627f5253fe8cf9ce60bbe3d779c5/README.md
- https://github.com/timoheimonen/amiga-sr2-060-performance-patch/blob/1f1ff97e31a5627f5253fe8cf9ce60bbe3d779c5/PATCH.md
- https://github.com/timoheimonen/amiga-sr2-060-performance-patch/commit/1f1ff97e31a5627f5253fe8cf9ce60bbe3d779c5

### Runtime profiles (reviewed)

README explicitly requires PAL A1200/AGA and MC68060; primarily intended for emulation.
- https://github.com/timoheimonen/amiga-sr2-060-performance-patch/blob/1f1ff97e31a5627f5253fe8cf9ce60bbe3d779c5/README.md
- https://github.com/timoheimonen/amiga-sr2-060-performance-patch/blob/1f1ff97e31a5627f5253fe8cf9ce60bbe3d779c5/PATCH.md
- https://github.com/timoheimonen/amiga-sr2-060-performance-patch/commit/1f1ff97e31a5627f5253fe8cf9ce60bbe3d779c5

### AI (no-evidence-found)

No explicit development-AI attribution found in inspected README, selected source/build files and head commit; non-use is not inferred.
- https://github.com/timoheimonen/amiga-sr2-060-performance-patch/blob/1f1ff97e31a5627f5253fe8cf9ce60bbe3d779c5/README.md
- https://github.com/timoheimonen/amiga-sr2-060-performance-patch/blob/1f1ff97e31a5627f5253fe8cf9ce60bbe3d779c5/PATCH.md
- https://github.com/timoheimonen/amiga-sr2-060-performance-patch/commit/1f1ff97e31a5627f5253fe8cf9ce60bbe3d779c5

### Relationships (reviewed)

Distinct game-specific project; current catalogue and prior decision URLs were screened before addition. Original game files are not included in these patch repositories.
- https://github.com/timoheimonen/amiga-sr2-060-performance-patch/blob/1f1ff97e31a5627f5253fe8cf9ce60bbe3d779c5/README.md
- https://github.com/timoheimonen/amiga-sr2-060-performance-patch/blob/1f1ff97e31a5627f5253fe8cf9ce60bbe3d779c5/PATCH.md
- https://github.com/timoheimonen/amiga-sr2-060-performance-patch/commit/1f1ff97e31a5627f5253fe8cf9ce60bbe3d779c5

## SWOS 96–97 In-Game Editors

Project ID: swos-9697-amiga-ingame-editors · Overall audit: reviewed

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
  "display_title": "SWOS 96–97 In-Game Editors",
  "id": "swos-9697-amiga-ingame-editors",
  "last_activity": "2026-10-16",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "m68k assembly",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/timoheimonen/amiga-swos-9697-editor",
  "runtime_profiles": [
    {
      "chipsets": [
        "AGA"
      ],
      "cpu_family": "m68k",
      "evidence": [
        "https://github.com/timoheimonen/amiga-swos-9697-editor/blob/fbf093b808683dc3f7089686ce2b3330bc7cdf23/README.md"
      ],
      "min_chip_ram_kib": 2048,
      "min_cpu": "68020",
      "min_fast_ram_kib": 2048,
      "name": "Documented editor baseline",
      "notes": "README requires A1200-compatible system; tested in emulation with 4 MiB Fast RAM, not on real hardware.",
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
    "SWOS 96–97 In-Game Editors"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build",
    "developer-following"
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
  "title": "SWOS 96–97 In-Game Editors",
  "tool_kinds": [],
  "types": [
    "game enhancement"
  ],
  "upstream_name": "SWOS 96–97 In-Game Editors",
  "work_kinds": [
    "patching",
    "data-format-analysis"
  ]
}
```

### Identity (reviewed)

Integrated editors for teams, players, tactics, tournaments and the game database, with CSV/JSON exchange and match logs.
- https://github.com/timoheimonen/amiga-swos-9697-editor/blob/fbf093b808683dc3f7089686ce2b3330bc7cdf23/README.md
- https://github.com/timoheimonen/amiga-swos-9697-editor/blob/fbf093b808683dc3f7089686ce2b3330bc7cdf23/build.py
- https://github.com/timoheimonen/amiga-swos-9697-editor/commit/fbf093b808683dc3f7089686ce2b3330bc7cdf23

### Classification (reviewed)

Native game-specific enhancement, not a complete original-binary restoration.
- https://github.com/timoheimonen/amiga-swos-9697-editor/blob/fbf093b808683dc3f7089686ce2b3330bc7cdf23/README.md
- https://github.com/timoheimonen/amiga-swos-9697-editor/blob/fbf093b808683dc3f7089686ce2b3330bc7cdf23/build.py
- https://github.com/timoheimonen/amiga-swos-9697-editor/commit/fbf093b808683dc3f7089686ce2b3330bc7cdf23

### Source CPU (reviewed)

Source lineage/platform is documented in the linked README and reviewed source; source CPU is distinct from host-side tooling.
- https://github.com/timoheimonen/amiga-swos-9697-editor/blob/fbf093b808683dc3f7089686ce2b3330bc7cdf23/README.md
- https://github.com/timoheimonen/amiga-swos-9697-editor/blob/fbf093b808683dc3f7089686ce2b3330bc7cdf23/build.py
- https://github.com/timoheimonen/amiga-swos-9697-editor/commit/fbf093b808683dc3f7089686ce2b3330bc7cdf23

### Target CPU (reviewed)

Native Amiga output on the m68k family is established by the README and reviewed source; Python/Java build tools are host-side.
- https://github.com/timoheimonen/amiga-swos-9697-editor/blob/fbf093b808683dc3f7089686ce2b3330bc7cdf23/README.md
- https://github.com/timoheimonen/amiga-swos-9697-editor/blob/fbf093b808683dc3f7089686ce2b3330bc7cdf23/build.py
- https://github.com/timoheimonen/amiga-swos-9697-editor/commit/fbf093b808683dc3f7089686ce2b3330bc7cdf23

### Build (reviewed)

build.py assembles/links native editor modules and WHDLoad slave using vasm/vlink and validates locations against user-supplied game data. README reports emulated A1200 testing only. No independent rebuild, gameplay test or byte-exact comparison was performed.
- https://github.com/timoheimonen/amiga-swos-9697-editor/blob/fbf093b808683dc3f7089686ce2b3330bc7cdf23/README.md
- https://github.com/timoheimonen/amiga-swos-9697-editor/blob/fbf093b808683dc3f7089686ce2b3330bc7cdf23/build.py
- https://github.com/timoheimonen/amiga-swos-9697-editor/commit/fbf093b808683dc3f7089686ce2b3330bc7cdf23

### Runtime profiles (reviewed)

README requires A1200-compatible system; tested in emulation with 4 MiB Fast RAM, not on real hardware.
- https://github.com/timoheimonen/amiga-swos-9697-editor/blob/fbf093b808683dc3f7089686ce2b3330bc7cdf23/README.md
- https://github.com/timoheimonen/amiga-swos-9697-editor/blob/fbf093b808683dc3f7089686ce2b3330bc7cdf23/build.py
- https://github.com/timoheimonen/amiga-swos-9697-editor/commit/fbf093b808683dc3f7089686ce2b3330bc7cdf23

### AI (no-evidence-found)

No explicit development-AI attribution found in inspected README, selected source/build files and head commit; non-use is not inferred.
- https://github.com/timoheimonen/amiga-swos-9697-editor/blob/fbf093b808683dc3f7089686ce2b3330bc7cdf23/README.md
- https://github.com/timoheimonen/amiga-swos-9697-editor/blob/fbf093b808683dc3f7089686ce2b3330bc7cdf23/build.py
- https://github.com/timoheimonen/amiga-swos-9697-editor/commit/fbf093b808683dc3f7089686ce2b3330bc7cdf23

### Relationships (reviewed)

Distinct game-specific project; current catalogue and prior decision URLs were screened before addition. Original game files are not included in these patch repositories.
- https://github.com/timoheimonen/amiga-swos-9697-editor/blob/fbf093b808683dc3f7089686ce2b3330bc7cdf23/README.md
- https://github.com/timoheimonen/amiga-swos-9697-editor/blob/fbf093b808683dc3f7089686ce2b3330bc7cdf23/build.py
- https://github.com/timoheimonen/amiga-swos-9697-editor/commit/fbf093b808683dc3f7089686ce2b3330bc7cdf23

## Caveman – Lionel Cross-Platform Versions

Project ID: caveman-lionel-commodore-ports · Overall audit: reviewed

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
  "display_title": "Caveman – Lionel Cross-Platform Versions",
  "id": "caveman-lionel-commodore-ports",
  "last_activity": "2020-01-09",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "6502 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/1888games/Caveman-C64VIC20Plus4PET",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/play test not performed",
  "subjects": [
    "Caveman – Lionel Cross-Platform Versions"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build",
    "developer-following"
  ],
  "target_cpu": [
    "6502"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Commodore 64",
    "Commodore VIC-20",
    "Commodore Plus/4",
    "Commodore PET"
  ],
  "techniques": [],
  "title": "Caveman – Lionel Cross-Platform Versions",
  "tool_kinds": [],
  "types": [
    "source-available game"
  ],
  "upstream_name": "Caveman – Lionel Cross-Platform Versions",
  "work_kinds": []
}
```

### Identity (reviewed)

Cross-platform Caveman implementation using the author’s Lionel library for C64, VIC-20, Plus/4 and PET.
- https://github.com/1888games/Caveman-C64VIC20Plus4PET/blob/343f6f0420f12bd53a7dd17659802a54b0850768/README.md
- https://github.com/1888games/Caveman-C64VIC20Plus4PET/blob/343f6f0420f12bd53a7dd17659802a54b0850768/scripts/main.asm
- https://github.com/1888games/Caveman-C64VIC20Plus4PET/commit/343f6f0420f12bd53a7dd17659802a54b0850768

### Classification (reviewed)

Source-available native game or authored port; no byte-exact binary reconstruction claim.
- https://github.com/1888games/Caveman-C64VIC20Plus4PET/blob/343f6f0420f12bd53a7dd17659802a54b0850768/README.md
- https://github.com/1888games/Caveman-C64VIC20Plus4PET/blob/343f6f0420f12bd53a7dd17659802a54b0850768/scripts/main.asm
- https://github.com/1888games/Caveman-C64VIC20Plus4PET/commit/343f6f0420f12bd53a7dd17659802a54b0850768

### Source CPU (not-applicable)

No identified predecessor binary is reconstructed; original source platform and CPU are left empty.
- https://github.com/1888games/Caveman-C64VIC20Plus4PET/blob/343f6f0420f12bd53a7dd17659802a54b0850768/README.md
- https://github.com/1888games/Caveman-C64VIC20Plus4PET/blob/343f6f0420f12bd53a7dd17659802a54b0850768/scripts/main.asm
- https://github.com/1888games/Caveman-C64VIC20Plus4PET/commit/343f6f0420f12bd53a7dd17659802a54b0850768

### Target CPU (reviewed)

Native Commodore 64 output on the 6502 family is established by the README and reviewed source; Python/Java build tools are host-side.
- https://github.com/1888games/Caveman-C64VIC20Plus4PET/blob/343f6f0420f12bd53a7dd17659802a54b0850768/README.md
- https://github.com/1888games/Caveman-C64VIC20Plus4PET/blob/343f6f0420f12bd53a7dd17659802a54b0850768/scripts/main.asm
- https://github.com/1888games/Caveman-C64VIC20Plus4PET/commit/343f6f0420f12bd53a7dd17659802a54b0850768

### Build (reviewed)

KickAssembler source selects the machine in scripts/main.asm. README says VIC-20 and Plus/4 are complete and C64 should run but lacks sound; the later pinned head commit explicitly reports PET version complete. These are upstream claims, not independently reproduced build/play results.
- https://github.com/1888games/Caveman-C64VIC20Plus4PET/blob/343f6f0420f12bd53a7dd17659802a54b0850768/README.md
- https://github.com/1888games/Caveman-C64VIC20Plus4PET/blob/343f6f0420f12bd53a7dd17659802a54b0850768/scripts/main.asm
- https://github.com/1888games/Caveman-C64VIC20Plus4PET/commit/343f6f0420f12bd53a7dd17659802a54b0850768

### Runtime profiles (no-evidence-found)

No full minimum hardware profile was established in the inspected material; platform does not imply an exact minimum configuration.
- https://github.com/1888games/Caveman-C64VIC20Plus4PET/blob/343f6f0420f12bd53a7dd17659802a54b0850768/README.md
- https://github.com/1888games/Caveman-C64VIC20Plus4PET/blob/343f6f0420f12bd53a7dd17659802a54b0850768/scripts/main.asm
- https://github.com/1888games/Caveman-C64VIC20Plus4PET/commit/343f6f0420f12bd53a7dd17659802a54b0850768

### AI (no-evidence-found)

No explicit development-AI attribution found in inspected README, selected source/build files and head commit; non-use is not inferred.
- https://github.com/1888games/Caveman-C64VIC20Plus4PET/blob/343f6f0420f12bd53a7dd17659802a54b0850768/README.md
- https://github.com/1888games/Caveman-C64VIC20Plus4PET/blob/343f6f0420f12bd53a7dd17659802a54b0850768/scripts/main.asm
- https://github.com/1888games/Caveman-C64VIC20Plus4PET/commit/343f6f0420f12bd53a7dd17659802a54b0850768

### Relationships (reviewed)

Related to already tracked 1888games/Caveman-C64 but this is a distinct cross-platform source tree/library experiment, not a URL alias or fork. Preserve differing completeness for each machine.
- https://github.com/1888games/Caveman-C64VIC20Plus4PET/blob/343f6f0420f12bd53a7dd17659802a54b0850768/README.md
- https://github.com/1888games/Caveman-C64VIC20Plus4PET/blob/343f6f0420f12bd53a7dd17659802a54b0850768/scripts/main.asm
- https://github.com/1888games/Caveman-C64VIC20Plus4PET/commit/343f6f0420f12bd53a7dd17659802a54b0850768

## Sources

```json
[
  {
    "id": "github-kdebczynski-c64-robo-gems",
    "kind": "github-repository",
    "reason": "catalogue-to-source: Two-player competitive platform game with twelve maps, released as a learning project with its complete KickC code.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/kdebczynski/c64-robo-gems"
  },
  {
    "id": "github-gus0650-fatman",
    "kind": "github-repository",
    "reason": "developer-following: Amiga game originally written in AmigaBASIC in 1990 and later converted to Blitz Basic.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/gus0650/Fatman"
  },
  {
    "id": "github-gus0650-gusgames64",
    "kind": "github-repository",
    "reason": "developer-following: Coherent collection of small C64 games written by Gustaf Stechmann during 1984–1985.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/gus0650/GusGames64"
  },
  {
    "id": "github-youenchene-blower",
    "kind": "github-repository",
    "reason": "catalogue-to-source: Four-player local combat game ported from the author’s 1996–1997 DOS Pascal/x86 game for the Amiga Blitz Basic Game Jam.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/youenchene/blower"
  },
  {
    "id": "github-sveinjo-space-invaders-64",
    "kind": "github-repository",
    "reason": "catalogue-to-source: Native C64 Space Invaders adaptation using raster-driven sprite multiplexing, with Intel 8080 disassembly/analysis material in the repository.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/sveinjo/Space-Invaders-64"
  },
  {
    "id": "github-fuzzybad-trse",
    "kind": "github-repository",
    "reason": "catalogue-to-source: One- or two-player C64 light-cycle game with a computer opponent, published with editable TRSE sources.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/fuzzybad/trse"
  },
  {
    "id": "github-timoheimonen-populous-amiga-funny-creature-fix",
    "kind": "github-repository",
    "reason": "developer-following: Game-specific restoration of wizard, swamp-monster and rock-monster spawning; documents missing stack argument, off-map position, repeated paused spawning and invalid table-full check.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/timoheimonen/Populous-Amiga-funny-creature-fix"
  },
  {
    "id": "github-timoheimonen-populous-atari-funny-creature-fix",
    "kind": "github-repository",
    "reason": "developer-following: Game-specific restoration of wizard, swamp-monster and rock-monster spawning; documents missing stack argument, off-map position, repeated paused spawning and invalid table-full check.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/timoheimonen/Populous-Atari-funny-creature-fix"
  },
  {
    "id": "github-timoheimonen-atari-st-ultima-5-inn-fix",
    "kind": "github-repository",
    "reason": "developer-following: Fixes active-party-member index corruption when leaving a companion at an inn, which causes merchants to read an invalid buyer and charge maximum prices.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/timoheimonen/atari-st-ultima-5-inn-fix"
  },
  {
    "id": "github-timoheimonen-amiga-hunter-performance-68060",
    "kind": "github-repository",
    "reason": "developer-following: Accelerator-targeted Hunter patch with instruction-cache support, Fast RAM allocations, terrain/polygon optimizations and an expanded terrain depth window.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/timoheimonen/amiga-hunter-performance-68060"
  },
  {
    "id": "github-timoheimonen-amiga-lemmings-editor",
    "kind": "github-repository",
    "reason": "developer-following: Adds custom levels and an in-game level editor to original Lemmings and Holiday Lemmings 1994, with floppy and WHDLoad installations.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/timoheimonen/Amiga-Lemmings-Editor"
  },
  {
    "id": "github-timoheimonen-amiga-sr2-060-performance-patch",
    "kind": "github-repository",
    "reason": "developer-following: Accelerator-focused Street Rod 2 update covering audio timing, road-buffer timing/frame cap, drawing optimizations and instruction-cache handling.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/timoheimonen/amiga-sr2-060-performance-patch"
  },
  {
    "id": "github-timoheimonen-amiga-swos-9697-editor",
    "kind": "github-repository",
    "reason": "developer-following: Integrated editors for teams, players, tactics, tournaments and the game database, with CSV/JSON exchange and match logs.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/timoheimonen/amiga-swos-9697-editor"
  },
  {
    "id": "github-1888games-caveman-c64vic20plus4pet",
    "kind": "github-repository",
    "reason": "developer-following: Cross-platform Caveman implementation using the author’s Lionel library for C64, VIC-20, Plus/4 and PET.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/1888games/Caveman-C64VIC20Plus4PET"
  },
  {
    "id": "archive-blade-source",
    "kind": "website",
    "reason": "Author lists original assembler archive under CC BY-NC 4.0, currently behind a $10 source tier. Source not purchased or inspected; track as a lead, not freely available verified source.",
    "review_state": "partial",
    "source": "https://marksheeky.itch.io/blade"
  },
  {
    "id": "archive-hilt-ii-source",
    "kind": "website",
    "reason": "Author lists original assembler archive under CC BY-NC 4.0, currently behind a $10 source tier. Source not purchased or inspected.",
    "review_state": "partial",
    "source": "https://marksheeky.itch.io/hilt-ii"
  },
  {
    "id": "archive-andy-green-stos-source",
    "kind": "website",
    "reason": "Archive announced by STOS Coders. Its approximately 423 MB ZIP was indexed using HTTP byte ranges: 9,620 entries, including STOS source and supporting data. Individual game identities and source completeness still require review.",
    "review_state": "partial",
    "source": "https://stoscoders.com/andy-green-source-code"
  }
]
```

## Decisions

```json
[
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/kdebczynski/c64-robo-gems/blob/915a566b9c9df0dfe9be51e4fd173b65da3f3381/README.md",
      "https://github.com/kdebczynski/c64-robo-gems/blob/915a566b9c9df0dfe9be51e4fd173b65da3f3381/robo-gems.c",
      "https://github.com/kdebczynski/c64-robo-gems/commit/915a566b9c9df0dfe9be51e4fd173b65da3f3381",
      "https://kdebczynski.itch.io/robo-gems"
    ],
    "id": "2026-10-17-promote-robo-gems-c64",
    "project_ids": [
      "robo-gems-c64"
    ],
    "reason": "catalogue-to-source: Two-player competitive platform game with twelve maps, released as a learning project with its complete KickC code.",
    "source_ids": [
      "github-kdebczynski-c64-robo-gems"
    ],
    "title": "Robo Gems",
    "url": "https://github.com/kdebczynski/c64-robo-gems"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/gus0650/Fatman/blob/85849f70fc72489e7ac86cb35df6fe2e34dd03f6/README.md",
      "https://github.com/gus0650/Fatman/blob/85849f70fc72489e7ac86cb35df6fe2e34dd03f6/fatman.bba",
      "https://github.com/gus0650/Fatman/commit/85849f70fc72489e7ac86cb35df6fe2e34dd03f6",
      "https://gus0650.itch.io/"
    ],
    "id": "2026-10-17-promote-fatman-amiga-gus0650",
    "project_ids": [
      "fatman-amiga-gus0650"
    ],
    "reason": "developer-following: Amiga game originally written in AmigaBASIC in 1990 and later converted to Blitz Basic.",
    "source_ids": [
      "github-gus0650-fatman"
    ],
    "title": "Fatman",
    "url": "https://github.com/gus0650/Fatman"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/gus0650/GusGames64/blob/734a310c88060b9200606c5ff1bf5b21253ef374/README.md",
      "https://github.com/gus0650/GusGames64/blob/734a310c88060b9200606c5ff1bf5b21253ef374/src/moonlander.prg",
      "https://github.com/gus0650/GusGames64/commit/734a310c88060b9200606c5ff1bf5b21253ef374"
    ],
    "id": "2026-10-17-promote-gusgames64-basic-archive",
    "project_ids": [
      "gusgames64-basic-archive"
    ],
    "reason": "developer-following: Coherent collection of small C64 games written by Gustaf Stechmann during 1984–1985.",
    "source_ids": [
      "github-gus0650-gusgames64"
    ],
    "title": "GusGames64",
    "url": "https://github.com/gus0650/GusGames64"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/youenchene/blower/blob/03a91c4201e093e5a31c7fc55cf1b7638ce5dce4/README.md",
      "https://github.com/youenchene/blower/blob/03a91c4201e093e5a31c7fc55cf1b7638ce5dce4/blower.bba",
      "https://github.com/youenchene/blower/commit/03a91c4201e093e5a31c7fc55cf1b7638ce5dce4",
      "https://youenchene.itch.io/blower"
    ],
    "id": "2026-10-17-promote-blower-amiga-port",
    "project_ids": [
      "blower-amiga-port"
    ],
    "reason": "catalogue-to-source: Four-player local combat game ported from the author’s 1996–1997 DOS Pascal/x86 game for the Amiga Blitz Basic Game Jam.",
    "source_ids": [
      "github-youenchene-blower"
    ],
    "title": "Blower",
    "url": "https://github.com/youenchene/blower"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/sveinjo/Space-Invaders-64/blob/2a729bebdd6fbaeb4b75c57f577dc3ae5aa066a3/README.md",
      "https://github.com/sveinjo/Space-Invaders-64/blob/2a729bebdd6fbaeb4b75c57f577dc3ae5aa066a3/SpaceInvaders64.ras",
      "https://github.com/sveinjo/Space-Invaders-64/blob/2a729bebdd6fbaeb4b75c57f577dc3ae5aa066a3/.github/copilot-instructions.md",
      "https://github.com/sveinjo/Space-Invaders-64/commit/2a729bebdd6fbaeb4b75c57f577dc3ae5aa066a3",
      "https://sveinacious-g.itch.io/invaders"
    ],
    "id": "2026-10-17-promote-sg-invaders-c64",
    "project_ids": [
      "sg-invaders-c64"
    ],
    "reason": "catalogue-to-source: Native C64 Space Invaders adaptation using raster-driven sprite multiplexing, with Intel 8080 disassembly/analysis material in the repository.",
    "source_ids": [
      "github-sveinjo-space-invaders-64"
    ],
    "title": "SG Invaders MMXXVI",
    "url": "https://github.com/sveinjo/Space-Invaders-64"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/fuzzybad/trse/blob/1ef444209650bfa15e73e1ea88a15803fcb182ad/README.md",
      "https://github.com/fuzzybad/trse/blob/1ef444209650bfa15e73e1ea88a15803fcb182ad/c64/LightCycles/main.ras",
      "https://github.com/fuzzybad/trse/commit/1ef444209650bfa15e73e1ea88a15803fcb182ad",
      "https://fuzzybad.itch.io/c64-light-cycle-duel"
    ],
    "id": "2026-10-17-promote-light-cycle-duel-c64",
    "project_ids": [
      "light-cycle-duel-c64"
    ],
    "reason": "catalogue-to-source: One- or two-player C64 light-cycle game with a computer opponent, published with editable TRSE sources.",
    "source_ids": [
      "github-fuzzybad-trse"
    ],
    "title": "Light Cycle Duel",
    "url": "https://github.com/fuzzybad/trse/tree/main/c64/LightCycles"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/timoheimonen/Populous-Amiga-funny-creature-fix/blob/beed7c79a5762dde63daef53ea1f79df5fc0fc94/README.md",
      "https://github.com/timoheimonen/Populous-Amiga-funny-creature-fix/blob/beed7c79a5762dde63daef53ea1f79df5fc0fc94/src/funny_fix.s",
      "https://github.com/timoheimonen/Populous-Amiga-funny-creature-fix/commit/beed7c79a5762dde63daef53ea1f79df5fc0fc94"
    ],
    "id": "2026-10-17-promote-populous-amiga-creature-fix",
    "project_ids": [
      "populous-amiga-creature-fix"
    ],
    "reason": "developer-following: Game-specific restoration of wizard, swamp-monster and rock-monster spawning; documents missing stack argument, off-map position, repeated paused spawning and invalid table-full check.",
    "source_ids": [
      "github-timoheimonen-populous-amiga-funny-creature-fix"
    ],
    "title": "Populous Amiga Creature Fix",
    "url": "https://github.com/timoheimonen/Populous-Amiga-funny-creature-fix"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/timoheimonen/Populous-Atari-funny-creature-fix/blob/88ddd56c2629f67c56112bc5e4265c1258625ead/README.md",
      "https://github.com/timoheimonen/Populous-Atari-funny-creature-fix/blob/88ddd56c2629f67c56112bc5e4265c1258625ead/src/funny_fix.s",
      "https://github.com/timoheimonen/Populous-Atari-funny-creature-fix/commit/88ddd56c2629f67c56112bc5e4265c1258625ead"
    ],
    "id": "2026-10-17-promote-populous-atari-st-creature-fix",
    "project_ids": [
      "populous-atari-st-creature-fix"
    ],
    "reason": "developer-following: Game-specific restoration of wizard, swamp-monster and rock-monster spawning; documents missing stack argument, off-map position, repeated paused spawning and invalid table-full check.",
    "source_ids": [
      "github-timoheimonen-populous-atari-funny-creature-fix"
    ],
    "title": "Populous Atari ST Creature Fix",
    "url": "https://github.com/timoheimonen/Populous-Atari-funny-creature-fix"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/timoheimonen/atari-st-ultima-5-inn-fix/blob/0914000555cf78b029007d2819d5d4e83ffeff66/README.md",
      "https://github.com/timoheimonen/atari-st-ultima-5-inn-fix/blob/0914000555cf78b029007d2819d5d4e83ffeff66/src/inn_fix.s",
      "https://github.com/timoheimonen/atari-st-ultima-5-inn-fix/commit/0914000555cf78b029007d2819d5d4e83ffeff66"
    ],
    "id": "2026-10-17-promote-ultima-v-atari-st-inn-fix",
    "project_ids": [
      "ultima-v-atari-st-inn-fix"
    ],
    "reason": "developer-following: Fixes active-party-member index corruption when leaving a companion at an inn, which causes merchants to read an invalid buyer and charge maximum prices.",
    "source_ids": [
      "github-timoheimonen-atari-st-ultima-5-inn-fix"
    ],
    "title": "Ultima V Atari ST Inn Fix",
    "url": "https://github.com/timoheimonen/atari-st-ultima-5-inn-fix"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/timoheimonen/amiga-hunter-performance-68060/blob/4114ba01fa99f3f4ee0dd50a121bbc223d6f39c9/README.md",
      "https://github.com/timoheimonen/amiga-hunter-performance-68060/blob/4114ba01fa99f3f4ee0dd50a121bbc223d6f39c9/PATCH.md",
      "https://github.com/timoheimonen/amiga-hunter-performance-68060/commit/4114ba01fa99f3f4ee0dd50a121bbc223d6f39c9"
    ],
    "id": "2026-10-17-promote-hunter-amiga-68060-performance",
    "project_ids": [
      "hunter-amiga-68060-performance"
    ],
    "reason": "developer-following: Accelerator-targeted Hunter patch with instruction-cache support, Fast RAM allocations, terrain/polygon optimizations and an expanded terrain depth window.",
    "source_ids": [
      "github-timoheimonen-amiga-hunter-performance-68060"
    ],
    "title": "Hunter 68060 Performance Patch",
    "url": "https://github.com/timoheimonen/amiga-hunter-performance-68060"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/timoheimonen/Amiga-Lemmings-Editor/blob/1e64e68957fb5bb5ad44af5da968896846971d50/README.md",
      "https://github.com/timoheimonen/Amiga-Lemmings-Editor/blob/1e64e68957fb5bb5ad44af5da968896846971d50/build.py",
      "https://github.com/timoheimonen/Amiga-Lemmings-Editor/commit/1e64e68957fb5bb5ad44af5da968896846971d50"
    ],
    "id": "2026-10-17-promote-lemmings-amiga-ingame-editor",
    "project_ids": [
      "lemmings-amiga-ingame-editor"
    ],
    "reason": "developer-following: Adds custom levels and an in-game level editor to original Lemmings and Holiday Lemmings 1994, with floppy and WHDLoad installations.",
    "source_ids": [
      "github-timoheimonen-amiga-lemmings-editor"
    ],
    "title": "Lemmings and Holiday Lemmings In-Game Editor",
    "url": "https://github.com/timoheimonen/Amiga-Lemmings-Editor"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/timoheimonen/amiga-sr2-060-performance-patch/blob/1f1ff97e31a5627f5253fe8cf9ce60bbe3d779c5/README.md",
      "https://github.com/timoheimonen/amiga-sr2-060-performance-patch/blob/1f1ff97e31a5627f5253fe8cf9ce60bbe3d779c5/PATCH.md",
      "https://github.com/timoheimonen/amiga-sr2-060-performance-patch/commit/1f1ff97e31a5627f5253fe8cf9ce60bbe3d779c5"
    ],
    "id": "2026-10-17-promote-street-rod-2-amiga-68060-patch",
    "project_ids": [
      "street-rod-2-amiga-68060-patch"
    ],
    "reason": "developer-following: Accelerator-focused Street Rod 2 update covering audio timing, road-buffer timing/frame cap, drawing optimizations and instruction-cache handling.",
    "source_ids": [
      "github-timoheimonen-amiga-sr2-060-performance-patch"
    ],
    "title": "Street Rod 2 68060 Performance Patch",
    "url": "https://github.com/timoheimonen/amiga-sr2-060-performance-patch"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/timoheimonen/amiga-swos-9697-editor/blob/fbf093b808683dc3f7089686ce2b3330bc7cdf23/README.md",
      "https://github.com/timoheimonen/amiga-swos-9697-editor/blob/fbf093b808683dc3f7089686ce2b3330bc7cdf23/build.py",
      "https://github.com/timoheimonen/amiga-swos-9697-editor/commit/fbf093b808683dc3f7089686ce2b3330bc7cdf23"
    ],
    "id": "2026-10-17-promote-swos-9697-amiga-ingame-editors",
    "project_ids": [
      "swos-9697-amiga-ingame-editors"
    ],
    "reason": "developer-following: Integrated editors for teams, players, tactics, tournaments and the game database, with CSV/JSON exchange and match logs.",
    "source_ids": [
      "github-timoheimonen-amiga-swos-9697-editor"
    ],
    "title": "SWOS 96–97 In-Game Editors",
    "url": "https://github.com/timoheimonen/amiga-swos-9697-editor"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/1888games/Caveman-C64VIC20Plus4PET/blob/343f6f0420f12bd53a7dd17659802a54b0850768/README.md",
      "https://github.com/1888games/Caveman-C64VIC20Plus4PET/blob/343f6f0420f12bd53a7dd17659802a54b0850768/scripts/main.asm",
      "https://github.com/1888games/Caveman-C64VIC20Plus4PET/commit/343f6f0420f12bd53a7dd17659802a54b0850768"
    ],
    "id": "2026-10-17-promote-caveman-lionel-commodore-ports",
    "project_ids": [
      "caveman-lionel-commodore-ports"
    ],
    "reason": "developer-following: Cross-platform Caveman implementation using the author’s Lionel library for C64, VIC-20, Plus/4 and PET.",
    "source_ids": [
      "github-1888games-caveman-c64vic20plus4pet"
    ],
    "title": "Caveman – Lionel Cross-Platform Versions",
    "url": "https://github.com/1888games/Caveman-C64VIC20Plus4PET"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://marksheeky.itch.io/blade"
    ],
    "id": "2026-10-17-defer-blade-source",
    "project_ids": [],
    "reason": "Author lists original assembler archive under CC BY-NC 4.0, currently behind a $10 source tier. Source not purchased or inspected; track as a lead, not freely available verified source.",
    "source_ids": [
      "archive-blade-source"
    ],
    "title": "Blade original Amiga source",
    "url": "https://marksheeky.itch.io/blade"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://marksheeky.itch.io/hilt-ii"
    ],
    "id": "2026-10-17-defer-hilt-ii-source",
    "project_ids": [],
    "reason": "Author lists original assembler archive under CC BY-NC 4.0, currently behind a $10 source tier. Source not purchased or inspected.",
    "source_ids": [
      "archive-hilt-ii-source"
    ],
    "title": "Hilt II original Amiga source",
    "url": "https://marksheeky.itch.io/hilt-ii"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://stoscoders.com/andy-green-source-code"
    ],
    "id": "2026-10-17-defer-andy-green-stos-source",
    "project_ids": [],
    "reason": "Archive announced by STOS Coders. Its approximately 423 MB ZIP was indexed using HTTP byte ranges: 9,620 entries, including STOS source and supporting data. Individual game identities and source completeness still require review.",
    "source_ids": [
      "archive-andy-green-stos-source"
    ],
    "title": "Andy Green STOS source collection",
    "url": "https://stoscoders.com/andy-green-source-code"
  }
]
```

## Research event notes

Discovery experiment: 195 repository URLs from 12 requested developer profiles were batch-screened; 41 matched prior decisions or tracked projects and 154 were URL-new, many unrelated to games/platform scope. This is not 154 verified leads. Fourteen relevant projects were selected and source-reviewed.
Four accepted projects were reached through game release/source links; ten through developer follow-through. These are first attribution routes, not proof that keyword search could never find them. Prior two keyword-led passes added seven and eight projects. This pass is broader, so counts do not prove a per-hour efficiency improvement.
Source archival routes exposed paid source archives and a large Atari ST collection; those limitations are recorded separately. No software from candidate repositories was executed.
