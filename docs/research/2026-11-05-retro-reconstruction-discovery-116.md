# Amiga and Atari ST reconstruction discovery

Review targeted game research, add four projects, reconcile two merged project lineages, and defer four leads.

Date: 2026-11-05 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- stupidcoder-retroreverse / Target CPU (no-evidence-found): No target CPU minimum established.
- stupidcoder-retroreverse / Runtime profiles (no-evidence-found): No independently verified complete runtime profile.
- wroniasty-aftertouch / Target CPU (no-evidence-found): No target CPU minimum established.
- wroniasty-aftertouch / Runtime profiles (no-evidence-found): No independently verified complete runtime profile.
- wroniasty-aftertouch / AI (no-evidence-found): No AI contribution established from inspected evidence; absence does not prove non-use.
- dbhq-uk-rockford-engine / Target CPU (no-evidence-found): No target CPU minimum established.
- dbhq-uk-rockford-engine / Runtime profiles (no-evidence-found): No independently verified complete runtime profile.
- dbhq-uk-rockford-engine / AI (no-evidence-found): No AI contribution established from inspected evidence; absence does not prove non-use.
- georgeflower-zelda1-atarist / Runtime profiles (no-evidence-found): No independently verified complete runtime profile.
- battle-squadron-amiga-recomp-crownpark / Target CPU (no-evidence-found): No target CPU minimum established.
- battle-squadron-amiga-recomp-crownpark / Runtime profiles (no-evidence-found): No independently verified complete runtime profile.
- battle-squadron-amiga-recomp-crownpark / AI (no-evidence-found): No AI contribution established from inspected evidence; absence does not prove non-use.
- shaid-sorcery / Target CPU (no-evidence-found): No target CPU minimum established.
- shaid-sorcery / Runtime profiles (no-evidence-found): No independently verified complete runtime profile.
- shaid-sorcery / AI (no-evidence-found): No AI contribution established from inspected evidence; absence does not prove non-use.

## RetroReverse — multi-game binary research

Project ID: stupidcoder-retroreverse · Overall audit: partial

### Typed catalogue values

```json
{
  "ai": {
    "evidence": [
      "Author explicitly credits Claude: https://github.com/StupidCoder/RetroReverse/blob/4260a49c3099ff3a5beac10d776a57cb5fc9e529/README.md"
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
  "display_title": "RetroReverse — multi-game binary research",
  "id": "stupidcoder-retroreverse",
  "last_activity": null,
  "last_checked": "2026-11-05",
  "re_started": null,
  "reconstructed_languages": [
    "Go"
  ],
  "record_class": "subject",
  "repo": "https://github.com/StupidCoder/RetroReverse",
  "runtime_profiles": [],
  "source_cpu": [
    "68000",
    "6502",
    "x86"
  ],
  "source_language": [],
  "source_platforms": [
    "Amiga",
    "C64",
    "DOS"
  ],
  "status": "Research and source inspected; no independent build or execution",
  "subjects": [
    "Stunt Car Racer",
    "Marble Madness",
    "Turrican"
  ],
  "tags": [],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [],
  "techniques": [],
  "title": "RetroReverse — multi-game binary research",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "RetroReverse",
  "work_kinds": [
    "disassembly",
    "data-format-analysis",
    "reimplementation"
  ]
}
```

### Identity (reviewed)

RetroReverse — multi-game binary research. Pinned repository material inspected.
- https://github.com/StupidCoder/RetroReverse/blob/4260a49c3099ff3a5beac10d776a57cb5fc9e529/README.md
- https://github.com/StupidCoder/RetroReverse/blob/4260a49c3099ff3a5beac10d776a57cb5fc9e529/games/stunt-car-racer-amiga/stunt-car-racer-amiga.md
- https://github.com/StupidCoder/RetroReverse/blob/4260a49c3099ff3a5beac10d776a57cb5fc9e529/games/turrican-amiga/turrican-amiga.md

### Classification (reviewed)

A shared toolkit and per-game investigations. The Amiga Stunt Car Racer work documents track formats and a Go physics reconstruction, Marble Madness documents disk and executable layout, and Turrican research is earlier-stage. Author describes reported tests and AI authorship; claims have not been independently verified.
- https://github.com/StupidCoder/RetroReverse/blob/4260a49c3099ff3a5beac10d776a57cb5fc9e529/README.md
- https://github.com/StupidCoder/RetroReverse/blob/4260a49c3099ff3a5beac10d776a57cb5fc9e529/games/stunt-car-racer-amiga/stunt-car-racer-amiga.md
- https://github.com/StupidCoder/RetroReverse/blob/4260a49c3099ff3a5beac10d776a57cb5fc9e529/games/turrican-amiga/turrican-amiga.md

### Source CPU (reviewed)

Source architectures follow the platforms explicitly examined; no exact variant inferred.
- https://github.com/StupidCoder/RetroReverse/blob/4260a49c3099ff3a5beac10d776a57cb5fc9e529/README.md
- https://github.com/StupidCoder/RetroReverse/blob/4260a49c3099ff3a5beac10d776a57cb5fc9e529/games/stunt-car-racer-amiga/stunt-car-racer-amiga.md
- https://github.com/StupidCoder/RetroReverse/blob/4260a49c3099ff3a5beac10d776a57cb5fc9e529/games/turrican-amiga/turrican-amiga.md

### Target CPU (no-evidence-found)

No target CPU minimum established.
- https://github.com/StupidCoder/RetroReverse/blob/4260a49c3099ff3a5beac10d776a57cb5fc9e529/README.md
- https://github.com/StupidCoder/RetroReverse/blob/4260a49c3099ff3a5beac10d776a57cb5fc9e529/games/stunt-car-racer-amiga/stunt-car-racer-amiga.md
- https://github.com/StupidCoder/RetroReverse/blob/4260a49c3099ff3a5beac10d776a57cb5fc9e529/games/turrican-amiga/turrican-amiga.md

### Build (reviewed)

Repository documents source or research and build procedures where applicable; no independent build, execution, or byte comparison.
- https://github.com/StupidCoder/RetroReverse/blob/4260a49c3099ff3a5beac10d776a57cb5fc9e529/README.md
- https://github.com/StupidCoder/RetroReverse/blob/4260a49c3099ff3a5beac10d776a57cb5fc9e529/games/stunt-car-racer-amiga/stunt-car-racer-amiga.md
- https://github.com/StupidCoder/RetroReverse/blob/4260a49c3099ff3a5beac10d776a57cb5fc9e529/games/turrican-amiga/turrican-amiga.md

### Runtime profiles (no-evidence-found)

No independently verified complete runtime profile.
- https://github.com/StupidCoder/RetroReverse/blob/4260a49c3099ff3a5beac10d776a57cb5fc9e529/README.md
- https://github.com/StupidCoder/RetroReverse/blob/4260a49c3099ff3a5beac10d776a57cb5fc9e529/games/stunt-car-racer-amiga/stunt-car-racer-amiga.md
- https://github.com/StupidCoder/RetroReverse/blob/4260a49c3099ff3a5beac10d776a57cb5fc9e529/games/turrican-amiga/turrican-amiga.md

### AI (reviewed)

The author credits Claude for code or research.
- https://github.com/StupidCoder/RetroReverse/blob/4260a49c3099ff3a5beac10d776a57cb5fc9e529/README.md
- https://github.com/StupidCoder/RetroReverse/blob/4260a49c3099ff3a5beac10d776a57cb5fc9e529/games/stunt-car-racer-amiga/stunt-car-racer-amiga.md
- https://github.com/StupidCoder/RetroReverse/blob/4260a49c3099ff3a5beac10d776a57cb5fc9e529/games/turrican-amiga/turrican-amiga.md

### Relationships (reviewed)

Distinct research repository; related same-title work is not automatically treated as identical.
- https://github.com/StupidCoder/RetroReverse/blob/4260a49c3099ff3a5beac10d776a57cb5fc9e529/README.md
- https://github.com/StupidCoder/RetroReverse/blob/4260a49c3099ff3a5beac10d776a57cb5fc9e529/games/stunt-car-racer-amiga/stunt-car-racer-amiga.md
- https://github.com/StupidCoder/RetroReverse/blob/4260a49c3099ff3a5beac10d776a57cb5fc9e529/games/turrican-amiga/turrican-amiga.md

## Aftertouch — SWOS match engine research

Project ID: wroniasty-aftertouch · Overall audit: partial

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
  "display_title": "Aftertouch — SWOS match engine research",
  "id": "wroniasty-aftertouch",
  "last_activity": null,
  "last_checked": "2026-11-05",
  "re_started": null,
  "reconstructed_languages": [
    "C++"
  ],
  "record_class": "subject",
  "repo": "https://github.com/wroniasty/aftertouch",
  "runtime_profiles": [],
  "source_cpu": [
    "68000",
    "x86"
  ],
  "source_language": [],
  "source_platforms": [
    "Amiga",
    "DOS"
  ],
  "status": "Research and source inspected; no independent build or execution",
  "subjects": [
    "Sensible World of Soccer"
  ],
  "tags": [],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [],
  "techniques": [],
  "title": "Aftertouch — SWOS match engine research",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "aftertouch",
  "work_kinds": [
    "disassembly",
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Aftertouch — SWOS match engine research. Pinned repository material inspected.
- https://github.com/wroniasty/aftertouch/blob/164c0c3b96d28672fa68307bd0f3914d595d86f0/doc/README.md
- https://github.com/wroniasty/aftertouch/blob/164c0c3b96d28672fa68307bd0f3914d595d86f0/doc/AMIGA_CHANGES.md
- https://github.com/wroniasty/aftertouch/blob/164c0c3b96d28672fa68307bd0f3914d595d86f0/src/core/src/match_engine.cpp

### Classification (reviewed)

An independent match engine informed by DOS disassembly and an Amiga SWOS 96/97 match-module cross-check. Detailed notes distinguish corrections and unresolved behavioural disagreements; implementation contains a match tick. Completeness is not established.
- https://github.com/wroniasty/aftertouch/blob/164c0c3b96d28672fa68307bd0f3914d595d86f0/doc/README.md
- https://github.com/wroniasty/aftertouch/blob/164c0c3b96d28672fa68307bd0f3914d595d86f0/doc/AMIGA_CHANGES.md
- https://github.com/wroniasty/aftertouch/blob/164c0c3b96d28672fa68307bd0f3914d595d86f0/src/core/src/match_engine.cpp

### Source CPU (reviewed)

Source architectures follow the platforms explicitly examined; no exact variant inferred.
- https://github.com/wroniasty/aftertouch/blob/164c0c3b96d28672fa68307bd0f3914d595d86f0/doc/README.md
- https://github.com/wroniasty/aftertouch/blob/164c0c3b96d28672fa68307bd0f3914d595d86f0/doc/AMIGA_CHANGES.md
- https://github.com/wroniasty/aftertouch/blob/164c0c3b96d28672fa68307bd0f3914d595d86f0/src/core/src/match_engine.cpp

### Target CPU (no-evidence-found)

No target CPU minimum established.
- https://github.com/wroniasty/aftertouch/blob/164c0c3b96d28672fa68307bd0f3914d595d86f0/doc/README.md
- https://github.com/wroniasty/aftertouch/blob/164c0c3b96d28672fa68307bd0f3914d595d86f0/doc/AMIGA_CHANGES.md
- https://github.com/wroniasty/aftertouch/blob/164c0c3b96d28672fa68307bd0f3914d595d86f0/src/core/src/match_engine.cpp

### Build (reviewed)

Repository documents source or research and build procedures where applicable; no independent build, execution, or byte comparison.
- https://github.com/wroniasty/aftertouch/blob/164c0c3b96d28672fa68307bd0f3914d595d86f0/doc/README.md
- https://github.com/wroniasty/aftertouch/blob/164c0c3b96d28672fa68307bd0f3914d595d86f0/doc/AMIGA_CHANGES.md
- https://github.com/wroniasty/aftertouch/blob/164c0c3b96d28672fa68307bd0f3914d595d86f0/src/core/src/match_engine.cpp

### Runtime profiles (no-evidence-found)

No independently verified complete runtime profile.
- https://github.com/wroniasty/aftertouch/blob/164c0c3b96d28672fa68307bd0f3914d595d86f0/doc/README.md
- https://github.com/wroniasty/aftertouch/blob/164c0c3b96d28672fa68307bd0f3914d595d86f0/doc/AMIGA_CHANGES.md
- https://github.com/wroniasty/aftertouch/blob/164c0c3b96d28672fa68307bd0f3914d595d86f0/src/core/src/match_engine.cpp

### AI (no-evidence-found)

No AI contribution established from inspected evidence; absence does not prove non-use.
- https://github.com/wroniasty/aftertouch/blob/164c0c3b96d28672fa68307bd0f3914d595d86f0/doc/README.md
- https://github.com/wroniasty/aftertouch/blob/164c0c3b96d28672fa68307bd0f3914d595d86f0/doc/AMIGA_CHANGES.md
- https://github.com/wroniasty/aftertouch/blob/164c0c3b96d28672fa68307bd0f3914d595d86f0/src/core/src/match_engine.cpp

### Relationships (reviewed)

Distinct research repository; related same-title work is not automatically treated as identical.
- https://github.com/wroniasty/aftertouch/blob/164c0c3b96d28672fa68307bd0f3914d595d86f0/doc/README.md
- https://github.com/wroniasty/aftertouch/blob/164c0c3b96d28672fa68307bd0f3914d595d86f0/doc/AMIGA_CHANGES.md
- https://github.com/wroniasty/aftertouch/blob/164c0c3b96d28672fa68307bd0f3914d595d86f0/src/core/src/match_engine.cpp

## Rockford — DOS engine reconstruction and Amiga analysis

Project ID: dbhq-uk-rockford-engine · Overall audit: partial

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
  "display_title": "Rockford — DOS engine reconstruction and Amiga analysis",
  "id": "dbhq-uk-rockford-engine",
  "last_activity": null,
  "last_checked": "2026-11-05",
  "re_started": null,
  "reconstructed_languages": [
    "C#",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/dbhq-uk/rockford-engine",
  "runtime_profiles": [],
  "source_cpu": [
    "x86",
    "68000"
  ],
  "source_language": [],
  "source_platforms": [
    "DOS",
    "Amiga"
  ],
  "status": "Research and source inspected; no independent build or execution",
  "subjects": [
    "Rockford: The Arcade Game"
  ],
  "tags": [],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Web"
  ],
  "techniques": [],
  "title": "Rockford — DOS engine reconstruction and Amiga analysis",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "rockford-engine",
  "work_kinds": [
    "disassembly",
    "data-format-analysis",
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Rockford — DOS engine reconstruction and Amiga analysis. Pinned repository material inspected.
- https://github.com/dbhq-uk/rockford-engine/blob/a51701c13023e75abe1fd7778703035e9bd7877f/README.md
- https://github.com/dbhq-uk/rockford-engine/blob/a51701c13023e75abe1fd7778703035e9bd7877f/tools/amigahunk.py

### Classification (reviewed)

DOS engine reimplementation derived from executable disassembly, with Amiga hunk inspection tooling. The author reports partial no-input comparison with the DOS original and explicitly says real play with input has not been compared. The Amiga evidence supports binary analysis, not an Amiga engine port.
- https://github.com/dbhq-uk/rockford-engine/blob/a51701c13023e75abe1fd7778703035e9bd7877f/README.md
- https://github.com/dbhq-uk/rockford-engine/blob/a51701c13023e75abe1fd7778703035e9bd7877f/tools/amigahunk.py

### Source CPU (reviewed)

Source architectures follow the platforms explicitly examined; no exact variant inferred.
- https://github.com/dbhq-uk/rockford-engine/blob/a51701c13023e75abe1fd7778703035e9bd7877f/README.md
- https://github.com/dbhq-uk/rockford-engine/blob/a51701c13023e75abe1fd7778703035e9bd7877f/tools/amigahunk.py

### Target CPU (no-evidence-found)

No target CPU minimum established.
- https://github.com/dbhq-uk/rockford-engine/blob/a51701c13023e75abe1fd7778703035e9bd7877f/README.md
- https://github.com/dbhq-uk/rockford-engine/blob/a51701c13023e75abe1fd7778703035e9bd7877f/tools/amigahunk.py

### Build (reviewed)

Repository documents source or research and build procedures where applicable; no independent build, execution, or byte comparison.
- https://github.com/dbhq-uk/rockford-engine/blob/a51701c13023e75abe1fd7778703035e9bd7877f/README.md
- https://github.com/dbhq-uk/rockford-engine/blob/a51701c13023e75abe1fd7778703035e9bd7877f/tools/amigahunk.py

### Runtime profiles (no-evidence-found)

No independently verified complete runtime profile.
- https://github.com/dbhq-uk/rockford-engine/blob/a51701c13023e75abe1fd7778703035e9bd7877f/README.md
- https://github.com/dbhq-uk/rockford-engine/blob/a51701c13023e75abe1fd7778703035e9bd7877f/tools/amigahunk.py

### AI (no-evidence-found)

No AI contribution established from inspected evidence; absence does not prove non-use.
- https://github.com/dbhq-uk/rockford-engine/blob/a51701c13023e75abe1fd7778703035e9bd7877f/README.md
- https://github.com/dbhq-uk/rockford-engine/blob/a51701c13023e75abe1fd7778703035e9bd7877f/tools/amigahunk.py

### Relationships (reviewed)

Distinct research repository; related same-title work is not automatically treated as identical.
- https://github.com/dbhq-uk/rockford-engine/blob/a51701c13023e75abe1fd7778703035e9bd7877f/README.md
- https://github.com/dbhq-uk/rockford-engine/blob/a51701c13023e75abe1fd7778703035e9bd7877f/tools/amigahunk.py

## The Legend of Zelda — Atari ST port

Project ID: georgeflower-zelda1-atarist · Overall audit: partial

### Typed catalogue values

```json
{
  "ai": {
    "evidence": [
      "Author explicitly credits Claude: https://github.com/georgeflower/zelda1-atarist/blob/53121014c497ff29ed8ce80859b3a3018fdf10fc/README.md"
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
  "display_title": "The Legend of Zelda — Atari ST port",
  "id": "georgeflower-zelda1-atarist",
  "last_activity": null,
  "last_checked": "2026-11-05",
  "re_started": null,
  "reconstructed_languages": [
    "68000 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/georgeflower/zelda1-atarist",
  "runtime_profiles": [],
  "source_cpu": [
    "6502"
  ],
  "source_language": [],
  "source_platforms": [
    "NES"
  ],
  "status": "Research and source inspected; no independent build or execution",
  "subjects": [
    "The Legend of Zelda"
  ],
  "tags": [],
  "target_cpu": [
    "68000"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Atari ST"
  ],
  "techniques": [],
  "title": "The Legend of Zelda — Atari ST port",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "zelda1-atarist",
  "work_kinds": [
    "reverse-engineering-derived-port"
  ]
}
```

### Identity (reviewed)

The Legend of Zelda — Atari ST port. Pinned repository material inspected.
- https://github.com/georgeflower/zelda1-atarist/blob/53121014c497ff29ed8ce80859b3a3018fdf10fc/README.md
- https://github.com/georgeflower/zelda1-atarist/blob/53121014c497ff29ed8ce80859b3a3018fdf10fc/atari_st/src/main.s

### Classification (reviewed)

Atari ST 68000 port informed by the NES disassembly and user-supplied ROM data. The author reports a 512 KB ST target and a work-in-progress game; Claude is explicitly credited with most code and tools. No independent build or play test.
- https://github.com/georgeflower/zelda1-atarist/blob/53121014c497ff29ed8ce80859b3a3018fdf10fc/README.md
- https://github.com/georgeflower/zelda1-atarist/blob/53121014c497ff29ed8ce80859b3a3018fdf10fc/atari_st/src/main.s

### Source CPU (reviewed)

Source architectures follow the platforms explicitly examined; no exact variant inferred.
- https://github.com/georgeflower/zelda1-atarist/blob/53121014c497ff29ed8ce80859b3a3018fdf10fc/README.md
- https://github.com/georgeflower/zelda1-atarist/blob/53121014c497ff29ed8ce80859b3a3018fdf10fc/atari_st/src/main.s

### Target CPU (reviewed)

Author states Atari ST 68000 target and 512 KB memory.
- https://github.com/georgeflower/zelda1-atarist/blob/53121014c497ff29ed8ce80859b3a3018fdf10fc/README.md
- https://github.com/georgeflower/zelda1-atarist/blob/53121014c497ff29ed8ce80859b3a3018fdf10fc/atari_st/src/main.s

### Build (reviewed)

Repository documents source or research and build procedures where applicable; no independent build, execution, or byte comparison.
- https://github.com/georgeflower/zelda1-atarist/blob/53121014c497ff29ed8ce80859b3a3018fdf10fc/README.md
- https://github.com/georgeflower/zelda1-atarist/blob/53121014c497ff29ed8ce80859b3a3018fdf10fc/atari_st/src/main.s

### Runtime profiles (no-evidence-found)

No independently verified complete runtime profile.
- https://github.com/georgeflower/zelda1-atarist/blob/53121014c497ff29ed8ce80859b3a3018fdf10fc/README.md
- https://github.com/georgeflower/zelda1-atarist/blob/53121014c497ff29ed8ce80859b3a3018fdf10fc/atari_st/src/main.s

### AI (reviewed)

The author credits Claude for code or research.
- https://github.com/georgeflower/zelda1-atarist/blob/53121014c497ff29ed8ce80859b3a3018fdf10fc/README.md
- https://github.com/georgeflower/zelda1-atarist/blob/53121014c497ff29ed8ce80859b3a3018fdf10fc/atari_st/src/main.s

### Relationships (reviewed)

Distinct research repository; related same-title work is not automatically treated as identical.
- https://github.com/georgeflower/zelda1-atarist/blob/53121014c497ff29ed8ce80859b3a3018fdf10fc/README.md
- https://github.com/georgeflower/zelda1-atarist/blob/53121014c497ff29ed8ce80859b3a3018fdf10fc/atari_st/src/main.s

## Battle Squadron — Amiga disassembly and native reconstruction

Project ID: battle-squadron-amiga-recomp-crownpark · Overall audit: partial

### Typed catalogue changes

```json
{
  "display_title": "Battle Squadron — Amiga disassembly and native reconstruction",
  "execution_paths": [
    {
      "evidence": [
        "https://github.com/CrownParkComputing/BattleSquadron2026/blob/3f5a29f32c9269d675ff879e6d07cc5ba4903998/README.md"
      ],
      "method": "native-translation",
      "name": "Native game",
      "notes": "Root describes native C game logic and native renderer; claimed lockstep tests not independently reproduced.",
      "status": "partial"
    },
    {
      "evidence": [
        "https://github.com/CrownParkComputing/BattleSquadron2026/blob/3f5a29f32c9269d675ff879e6d07cc5ba4903998/amiga/README.md"
      ],
      "method": "baked-emulation",
      "name": "Amiga reference runner",
      "notes": "Separate reference runner executes original code in Musashi with OCS host; author-reported.",
      "status": "playable"
    }
  ],
  "github": {},
  "id": "battle-squadron-amiga-recomp-crownpark",
  "reconstructed_languages": [
    "68000 assembly",
    "C"
  ],
  "repo": "https://github.com/CrownParkComputing/BattleSquadron2026",
  "status": "Upstream reports native reconstruction and verification; not independently tested",
  "target_platforms": [
    "Amiga",
    "Windows",
    "Linux",
    "macOS",
    "Android"
  ],
  "title": "Battle Squadron",
  "upstream_name": "BattleSquadron2026",
  "work_kinds": [
    "disassembly",
    "source-reconstruction",
    "data-format-analysis",
    "reimplementation"
  ]
}
```

Expected existing project SHA256: b4f0bf3ae8b8cbc6cf02cddb790dbd52fd45026537a70c85aa953a2af4fccb1a

### Identity (reviewed)

Battle Squadron — Amiga disassembly and native reconstruction. Pinned repository material inspected.
- https://github.com/CrownParkComputing/BattleSquadron2026/blob/3f5a29f32c9269d675ff879e6d07cc5ba4903998/README.md
- https://github.com/CrownParkComputing/BattleSquadron2026/blob/3f5a29f32c9269d675ff879e6d07cc5ba4903998/amiga/README.md

### Classification (reviewed)

Combined repository explicitly incorporates the prior BattleSquadron-Amiga work. Root describes a native C game, while the included Amiga research retains a separate Musashi/OCS reference runner; upstream reports lockstep tests but these were not independently reproduced.
- https://github.com/CrownParkComputing/BattleSquadron2026/blob/3f5a29f32c9269d675ff879e6d07cc5ba4903998/README.md
- https://github.com/CrownParkComputing/BattleSquadron2026/blob/3f5a29f32c9269d675ff879e6d07cc5ba4903998/amiga/README.md

### Source CPU (reviewed)

Source architectures follow the platforms explicitly examined; no exact variant inferred.
- https://github.com/CrownParkComputing/BattleSquadron2026/blob/3f5a29f32c9269d675ff879e6d07cc5ba4903998/README.md
- https://github.com/CrownParkComputing/BattleSquadron2026/blob/3f5a29f32c9269d675ff879e6d07cc5ba4903998/amiga/README.md

### Target CPU (no-evidence-found)

No target CPU minimum established.
- https://github.com/CrownParkComputing/BattleSquadron2026/blob/3f5a29f32c9269d675ff879e6d07cc5ba4903998/README.md
- https://github.com/CrownParkComputing/BattleSquadron2026/blob/3f5a29f32c9269d675ff879e6d07cc5ba4903998/amiga/README.md

### Build (reviewed)

Repository documents source or research and build procedures where applicable; no independent build, execution, or byte comparison.
- https://github.com/CrownParkComputing/BattleSquadron2026/blob/3f5a29f32c9269d675ff879e6d07cc5ba4903998/README.md
- https://github.com/CrownParkComputing/BattleSquadron2026/blob/3f5a29f32c9269d675ff879e6d07cc5ba4903998/amiga/README.md

### Runtime profiles (no-evidence-found)

No independently verified complete runtime profile.
- https://github.com/CrownParkComputing/BattleSquadron2026/blob/3f5a29f32c9269d675ff879e6d07cc5ba4903998/README.md
- https://github.com/CrownParkComputing/BattleSquadron2026/blob/3f5a29f32c9269d675ff879e6d07cc5ba4903998/amiga/README.md

### AI (no-evidence-found)

No AI contribution established from inspected evidence; absence does not prove non-use.
- https://github.com/CrownParkComputing/BattleSquadron2026/blob/3f5a29f32c9269d675ff879e6d07cc5ba4903998/README.md
- https://github.com/CrownParkComputing/BattleSquadron2026/blob/3f5a29f32c9269d675ff879e6d07cc5ba4903998/amiga/README.md

### Relationships (reviewed)

README identifies the prior BattleSquadron-Amiga repository as incorporated into this root; update the existing record instead of creating a duplicate.
- https://github.com/CrownParkComputing/BattleSquadron2026/blob/3f5a29f32c9269d675ff879e6d07cc5ba4903998/README.md
- https://github.com/CrownParkComputing/BattleSquadron2026/blob/3f5a29f32c9269d675ff879e6d07cc5ba4903998/amiga/README.md

## Black Crypt, Wizardry 6 and dungeon-game research

Project ID: shaid-sorcery · Overall audit: partial

### Typed catalogue changes

```json
{
  "display_title": "Black Crypt, Wizardry 6 and dungeon-game research",
  "github": {},
  "id": "shaid-sorcery",
  "reconstructed_languages": [
    "TypeScript",
    "Python"
  ],
  "repo": "https://github.com/Shaid/crawl",
  "source_cpu": [
    "68000",
    "x86"
  ],
  "source_platforms": [
    "Amiga",
    "DOS",
    "SNES"
  ],
  "status": "Research collection; implementation varies by title and was not independently tested",
  "subjects": [
    "Black Crypt",
    "Wizardry 6",
    "Might & Magic III"
  ],
  "target_platforms": [
    "Web"
  ],
  "title": "Black Crypt, Wizardry 6 and dungeon-game research",
  "upstream_name": "crawl",
  "work_kinds": [
    "disassembly",
    "data-format-analysis",
    "reimplementation"
  ]
}
```

Expected existing project SHA256: a91a0ffea82cadbfb0670909da329441445c89d64bdfc2c7eb65ab90b0b7bf92

### Identity (reviewed)

Black Crypt, Wizardry 6 and dungeon-game research. Pinned repository material inspected.
- https://github.com/Shaid/crawl/blob/c5b2ec7b9aa4a10ded5d7ce83b406e3835a37d60/README.md
- https://github.com/Shaid/crawl/blob/c5b2ec7b9aa4a10ded5d7ce83b406e3835a37d60/docs/blackcrypt/amiga/data-structure.md
- https://github.com/Shaid/crawl/blob/c5b2ec7b9aa4a10ded5d7ce83b406e3835a37d60/docs/mm3/amiga/data-structure.md

### Classification (reviewed)

Crawl root documents Black Crypt and explicitly says Wizardry 6 was merged from sorcery; separate pinned documentation analyses the Amiga Might & Magic III formats. Actual browser implementation and completeness vary by title; no independent tests.
- https://github.com/Shaid/crawl/blob/c5b2ec7b9aa4a10ded5d7ce83b406e3835a37d60/README.md
- https://github.com/Shaid/crawl/blob/c5b2ec7b9aa4a10ded5d7ce83b406e3835a37d60/docs/blackcrypt/amiga/data-structure.md
- https://github.com/Shaid/crawl/blob/c5b2ec7b9aa4a10ded5d7ce83b406e3835a37d60/docs/mm3/amiga/data-structure.md

### Source CPU (reviewed)

Source architectures follow the platforms explicitly examined; no exact variant inferred.
- https://github.com/Shaid/crawl/blob/c5b2ec7b9aa4a10ded5d7ce83b406e3835a37d60/README.md
- https://github.com/Shaid/crawl/blob/c5b2ec7b9aa4a10ded5d7ce83b406e3835a37d60/docs/blackcrypt/amiga/data-structure.md
- https://github.com/Shaid/crawl/blob/c5b2ec7b9aa4a10ded5d7ce83b406e3835a37d60/docs/mm3/amiga/data-structure.md

### Target CPU (no-evidence-found)

No target CPU minimum established.
- https://github.com/Shaid/crawl/blob/c5b2ec7b9aa4a10ded5d7ce83b406e3835a37d60/README.md
- https://github.com/Shaid/crawl/blob/c5b2ec7b9aa4a10ded5d7ce83b406e3835a37d60/docs/blackcrypt/amiga/data-structure.md
- https://github.com/Shaid/crawl/blob/c5b2ec7b9aa4a10ded5d7ce83b406e3835a37d60/docs/mm3/amiga/data-structure.md

### Build (reviewed)

Repository documents source or research and build procedures where applicable; no independent build, execution, or byte comparison.
- https://github.com/Shaid/crawl/blob/c5b2ec7b9aa4a10ded5d7ce83b406e3835a37d60/README.md
- https://github.com/Shaid/crawl/blob/c5b2ec7b9aa4a10ded5d7ce83b406e3835a37d60/docs/blackcrypt/amiga/data-structure.md
- https://github.com/Shaid/crawl/blob/c5b2ec7b9aa4a10ded5d7ce83b406e3835a37d60/docs/mm3/amiga/data-structure.md

### Runtime profiles (no-evidence-found)

No independently verified complete runtime profile.
- https://github.com/Shaid/crawl/blob/c5b2ec7b9aa4a10ded5d7ce83b406e3835a37d60/README.md
- https://github.com/Shaid/crawl/blob/c5b2ec7b9aa4a10ded5d7ce83b406e3835a37d60/docs/blackcrypt/amiga/data-structure.md
- https://github.com/Shaid/crawl/blob/c5b2ec7b9aa4a10ded5d7ce83b406e3835a37d60/docs/mm3/amiga/data-structure.md

### AI (no-evidence-found)

No AI contribution established from inspected evidence; absence does not prove non-use.
- https://github.com/Shaid/crawl/blob/c5b2ec7b9aa4a10ded5d7ce83b406e3835a37d60/README.md
- https://github.com/Shaid/crawl/blob/c5b2ec7b9aa4a10ded5d7ce83b406e3835a37d60/docs/blackcrypt/amiga/data-structure.md
- https://github.com/Shaid/crawl/blob/c5b2ec7b9aa4a10ded5d7ce83b406e3835a37d60/docs/mm3/amiga/data-structure.md

### Relationships (reviewed)

Root README identifies Wizardry 6 work formerly in sorcery as merged into this shared repository; consolidate the existing record rather than duplicate the same lineage.
- https://github.com/Shaid/crawl/blob/c5b2ec7b9aa4a10ded5d7ce83b406e3835a37d60/README.md
- https://github.com/Shaid/crawl/blob/c5b2ec7b9aa4a10ded5d7ce83b406e3835a37d60/docs/blackcrypt/amiga/data-structure.md
- https://github.com/Shaid/crawl/blob/c5b2ec7b9aa4a10ded5d7ce83b406e3835a37d60/docs/mm3/amiga/data-structure.md

## Pinned evidence manifest

- crownparkcomputing-battlesquadron2026-amiga-readme-md: https://github.com/crownparkcomputing/battlesquadron2026/blob/3f5a29f32c9269d675ff879e6d07cc5ba4903998/amiga/README.md (Git blob d2634e8f20edfa4505b3deef8b6a401411553607)
- crownparkcomputing-battlesquadron2026-readme-md: https://github.com/crownparkcomputing/battlesquadron2026/blob/3f5a29f32c9269d675ff879e6d07cc5ba4903998/README.md (Git blob 64575922a786e94f5a6d2ce4dfa5ba7bf39de263)
- crownparkcomputing-hybris-readme-md: https://github.com/crownparkcomputing/hybris/blob/e0c9b17a442e9580a71f61d2ce578f0e96118df4/README.md (Git blob 94ab76be72233956e3753fa18f0d8935865cb928)
- crownparkcomputing-swiv-amiga-readme-md: https://github.com/crownparkcomputing/swiv-amiga/blob/e804a8a7c1005632ec6e2468b0ed200dfdc202b3/README.md (Git blob f17b7c097570f7260d5cfc0bc53b099c4338edb4)
- dbhq-uk-rockford-engine-readme-md: https://github.com/dbhq-uk/rockford-engine/blob/a51701c13023e75abe1fd7778703035e9bd7877f/README.md (Git blob d9128b930d07b51ab95706de2014d10c7dd4f80a)
- dbhq-uk-rockford-engine-tools-amigahunk-py: https://github.com/dbhq-uk/rockford-engine/blob/a51701c13023e75abe1fd7778703035e9bd7877f/tools/amigahunk.py (Git blob 83e72115f65bb4ae41fce424931052202d53e328)
- georgeflower-zelda1-atarist-atari-st-src-main-s: https://github.com/georgeflower/zelda1-atarist/blob/53121014c497ff29ed8ce80859b3a3018fdf10fc/atari_st/src/main.s (Git blob bddb42725d185a1520ada206cddf895dd329f2c1)
- georgeflower-zelda1-atarist-readme-md: https://github.com/georgeflower/zelda1-atarist/blob/53121014c497ff29ed8ce80859b3a3018fdf10fc/README.md (Git blob 1abc0e011a82bda731300c315a5f9dd577376e0b)
- jedeyesniv-art-llamatron-pc-recomp-readme-md: https://github.com/jedeyesniv-art/llamatron-pc-recomp/blob/e1dd7b0197b00fb76975081efc20d7545e2d17ad/README.md (Git blob 933fa0cabd4683a8c29fed30707a0378729d22bd)
- philjf-fcg-portandstarboard-porting-notes-md: https://github.com/philjf-fcg/portandstarboard/blob/fa33187ba4fd6106d1438f29ecb0c88f522b6690/PORTING_NOTES.md (Git blob b93170c9de7f726a8143e0e0b5336536291442a6)
- philjf-fcg-portandstarboard-xenon2modern-gameworld-cs: https://github.com/philjf-fcg/portandstarboard/blob/fa33187ba4fd6106d1438f29ecb0c88f522b6690/Xenon2Modern/GameWorld.cs (Git blob 87feb34f440c038bf8f813a42acf09dc10714b52)
- shaid-crawl-docs-mm3-amiga-data-structure-md: https://github.com/shaid/crawl/blob/c5b2ec7b9aa4a10ded5d7ce83b406e3835a37d60/docs/mm3/amiga/data-structure.md (Git blob 271745fe8b2c7658308b315d486ff3dbc15ab5b8)
- shaid-crawl-readme-md: https://github.com/shaid/crawl/blob/c5b2ec7b9aa4a10ded5d7ce83b406e3835a37d60/README.md (Git blob 67bb2d00023c6fe942cb43b996022bf7068d5231)
- stupidcoder-retroreverse-games-stunt-car-racer-amiga-stunt-car-racer-amiga-md: https://github.com/stupidcoder/retroreverse/blob/4260a49c3099ff3a5beac10d776a57cb5fc9e529/games/stunt-car-racer-amiga/stunt-car-racer-amiga.md (Git blob 7467727a2bfac80ab5d7c97fe09c1e3f33109cc4)
- stupidcoder-retroreverse-games-turrican-amiga-turrican-amiga-md: https://github.com/stupidcoder/retroreverse/blob/4260a49c3099ff3a5beac10d776a57cb5fc9e529/games/turrican-amiga/turrican-amiga.md (Git blob 6e27c350beba761dd36e2c66be1720556e7553ce)
- stupidcoder-retroreverse-readme-md: https://github.com/stupidcoder/retroreverse/blob/4260a49c3099ff3a5beac10d776a57cb5fc9e529/README.md (Git blob d27dce5c1335cb24e420c828966725900c150b79)
- wroniasty-aftertouch-doc-amiga-changes-md: https://github.com/wroniasty/aftertouch/blob/164c0c3b96d28672fa68307bd0f3914d595d86f0/doc/AMIGA_CHANGES.md (Git blob 4aabaffccf77745925c3022355eb2e89dc08ce71)
- wroniasty-aftertouch-doc-readme-md: https://github.com/wroniasty/aftertouch/blob/164c0c3b96d28672fa68307bd0f3914d595d86f0/doc/README.md (Git blob 7d39051ba4c5341061bc1e4135f077170fcb1ea9)
- wroniasty-aftertouch-src-core-src-match-engine-cpp: https://github.com/wroniasty/aftertouch/blob/164c0c3b96d28672fa68307bd0f3914d595d86f0/src/core/src/match_engine.cpp (Git blob d1987ee764af65f2e4912894b79989c22b2cd55c)

## Sources

```json
[
  {
    "first_indexed": "2026-11-05",
    "id": "github-stupidcoder-retroreverse",
    "kind": "github-repository",
    "last_reviewed": "2026-11-05",
    "open_task_ids": [],
    "projects_promoted": [
      "stupidcoder-retroreverse"
    ],
    "reason": "A shared toolkit and per-game investigations. The Amiga Stunt Car Racer work documents track formats and a Go physics reconstruction, Marble Madness documents disk and executable layout, and Turrican research is earlier-stage. Author describes reported tests and AI authorship; claims have not been independently verified.",
    "review_state": "partial",
    "source": "https://github.com/StupidCoder/RetroReverse"
  },
  {
    "first_indexed": "2026-11-05",
    "id": "github-wroniasty-aftertouch",
    "kind": "github-repository",
    "last_reviewed": "2026-11-05",
    "open_task_ids": [],
    "projects_promoted": [
      "wroniasty-aftertouch"
    ],
    "reason": "An independent match engine informed by DOS disassembly and an Amiga SWOS 96/97 match-module cross-check. Detailed notes distinguish corrections and unresolved behavioural disagreements; implementation contains a match tick. Completeness is not established.",
    "review_state": "partial",
    "source": "https://github.com/wroniasty/aftertouch"
  },
  {
    "first_indexed": "2026-11-05",
    "id": "github-dbhq-uk-rockford-engine",
    "kind": "github-repository",
    "last_reviewed": "2026-11-05",
    "open_task_ids": [],
    "projects_promoted": [
      "dbhq-uk-rockford-engine"
    ],
    "reason": "DOS engine reimplementation derived from executable disassembly, with Amiga hunk inspection tooling. The author reports partial no-input comparison with the DOS original and explicitly says real play with input has not been compared. The Amiga evidence supports binary analysis, not an Amiga engine port.",
    "review_state": "partial",
    "source": "https://github.com/dbhq-uk/rockford-engine"
  },
  {
    "first_indexed": "2026-11-05",
    "id": "github-georgeflower-zelda1-atarist",
    "kind": "github-repository",
    "last_reviewed": "2026-11-05",
    "open_task_ids": [],
    "projects_promoted": [
      "georgeflower-zelda1-atarist"
    ],
    "reason": "Atari ST 68000 port informed by the NES disassembly and user-supplied ROM data. The author reports a 512 KB ST target and a work-in-progress game; Claude is explicitly credited with most code and tools. No independent build or play test.",
    "review_state": "partial",
    "source": "https://github.com/georgeflower/zelda1-atarist"
  },
  {
    "first_indexed": "2026-11-05",
    "id": "github-philjf-fcg-portandstarboard",
    "kind": "github-repository",
    "last_reviewed": "2026-11-05",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Xenon II investigation includes Amiga extraction and DOS graphics formats, but the inspected C# loop is a simplified shooter with timed generic stages; the notes call it a base for future gameplay porting, so original game fidelity is not established. Defer for deeper source-specific analysis.",
    "review_state": "partial",
    "source": "https://github.com/Philjf-FCG/PortandStarboard"
  },
  {
    "first_indexed": "2026-11-05",
    "id": "github-crownparkcomputing-swiv-amiga",
    "kind": "github-repository",
    "last_reviewed": "2026-11-05",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "The described playable game executes original 68000 code under Musashi with OCS chipset models. Defer to the game-specific BAKED EMULATION audit rather than add as native reconstruction.",
    "review_state": "partial",
    "source": "https://github.com/CrownParkComputing/SWIV-Amiga"
  },
  {
    "first_indexed": "2026-11-05",
    "id": "github-crownparkcomputing-hybris",
    "kind": "github-repository",
    "last_reviewed": "2026-11-05",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "The Hybris runner loads the original game executable with Musashi and game-focused OCS hardware models. Defer for BAKED EMULATION audit; disk extraction research is distinct from evidence of a native game rewrite.",
    "review_state": "partial",
    "source": "https://github.com/CrownParkComputing/Hybris"
  },
  {
    "first_indexed": "2026-11-05",
    "id": "github-jedeyesniv-art-llamatron-pc-recomp",
    "kind": "github-repository",
    "last_reviewed": "2026-11-05",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "The README says original Atari ST 68000 game code runs in Musashi with ST hardware/TOS emulation. Defer for BAKED EMULATION review despite the repository name.",
    "review_state": "partial",
    "source": "https://github.com/jedeyesniv-art/Llamatron-PC-Recomp"
  },
  {
    "first_indexed": "2026-11-05",
    "id": "github-crownparkcomputing-battlesquadron2026",
    "kind": "github-repository",
    "last_reviewed": "2026-11-05",
    "open_task_ids": [],
    "projects_promoted": [
      "battle-squadron-amiga-recomp-crownpark"
    ],
    "reason": "Combined repository explicitly incorporates the prior BattleSquadron-Amiga work. Root describes a native C game, while the included Amiga research retains a separate Musashi/OCS reference runner; upstream reports lockstep tests but these were not independently reproduced.",
    "review_state": "partial",
    "source": "https://github.com/CrownParkComputing/BattleSquadron2026"
  },
  {
    "first_indexed": "2026-11-05",
    "id": "github-shaid-crawl",
    "kind": "github-repository",
    "last_reviewed": "2026-11-05",
    "open_task_ids": [],
    "projects_promoted": [
      "shaid-sorcery"
    ],
    "reason": "Crawl root documents Black Crypt and explicitly says Wizardry 6 was merged from sorcery; separate pinned documentation analyses the Amiga Might & Magic III formats. Actual browser implementation and completeness vary by title; no independent tests.",
    "review_state": "partial",
    "source": "https://github.com/Shaid/crawl"
  }
]
```

## Decisions

```json
[
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/Philjf-FCG/PortandStarboard/blob/fa33187ba4fd6106d1438f29ecb0c88f522b6690/PORTING_NOTES.md",
      "https://github.com/Philjf-FCG/PortandStarboard/blob/fa33187ba4fd6106d1438f29ecb0c88f522b6690/Xenon2Modern/GameWorld.cs"
    ],
    "id": "pass116-philjf-fcg-portandstarboard",
    "project_ids": [],
    "reason": "Xenon II investigation includes Amiga extraction and DOS graphics formats, but the inspected C# loop is a simplified shooter with timed generic stages; the notes call it a base for future gameplay porting, so original game fidelity is not established. Defer for deeper source-specific analysis.",
    "reviewed_at": "2026-11-05",
    "source_ids": [
      "github-philjf-fcg-portandstarboard"
    ],
    "title": "Philjf-FCG/PortandStarboard",
    "url": "https://github.com/Philjf-FCG/PortandStarboard"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/CrownParkComputing/SWIV-Amiga/blob/e804a8a7c1005632ec6e2468b0ed200dfdc202b3/README.md"
    ],
    "id": "pass116-crownparkcomputing-swiv-amiga",
    "project_ids": [],
    "reason": "The described playable game executes original 68000 code under Musashi with OCS chipset models. Defer to the game-specific BAKED EMULATION audit rather than add as native reconstruction.",
    "reviewed_at": "2026-11-05",
    "source_ids": [
      "github-crownparkcomputing-swiv-amiga"
    ],
    "title": "CrownParkComputing/SWIV-Amiga",
    "url": "https://github.com/CrownParkComputing/SWIV-Amiga"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/CrownParkComputing/Hybris/blob/e0c9b17a442e9580a71f61d2ce578f0e96118df4/README.md"
    ],
    "id": "pass116-crownparkcomputing-hybris",
    "project_ids": [],
    "reason": "The Hybris runner loads the original game executable with Musashi and game-focused OCS hardware models. Defer for BAKED EMULATION audit; disk extraction research is distinct from evidence of a native game rewrite.",
    "reviewed_at": "2026-11-05",
    "source_ids": [
      "github-crownparkcomputing-hybris"
    ],
    "title": "CrownParkComputing/Hybris",
    "url": "https://github.com/CrownParkComputing/Hybris"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/jedeyesniv-art/Llamatron-PC-Recomp/blob/e1dd7b0197b00fb76975081efc20d7545e2d17ad/README.md"
    ],
    "id": "pass116-jedeyesniv-art-llamatron-pc-recomp",
    "project_ids": [],
    "reason": "The README says original Atari ST 68000 game code runs in Musashi with ST hardware/TOS emulation. Defer for BAKED EMULATION review despite the repository name.",
    "reviewed_at": "2026-11-05",
    "source_ids": [
      "github-jedeyesniv-art-llamatron-pc-recomp"
    ],
    "title": "jedeyesniv-art/Llamatron-PC-Recomp",
    "url": "https://github.com/jedeyesniv-art/Llamatron-PC-Recomp"
  }
]
```

## Research event notes

Personally screened repository search and primary source against the current catalogue and prior decisions. Inspected pinned documentation and selected code. No independent builds, gameplay or byte comparisons. Game-specific CPU execution leads deferred for the existing BAKED EMULATION audit.
