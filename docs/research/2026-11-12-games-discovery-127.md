# Retro game discovery and supplied projects

Review two Atari ST game port projects.

Date: 2026-11-12 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- kings-quest-v-amiga-to-atari-st-shim / Runtime profiles (no-evidence-found): No independently verified minimum hardware profile.
- dogs-of-war-atari-st-static-recomp-voodatari / Runtime profiles (no-evidence-found): No independently verified minimum hardware profile.

## King's Quest V — Atari ST shim port

Project ID: kings-quest-v-amiga-to-atari-st-shim · Overall audit: partial

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
  "display_title": "King's Quest V — Atari ST shim port",
  "id": "kings-quest-v-amiga-to-atari-st-shim",
  "last_activity": null,
  "last_checked": "2026-11-12",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "m68k assembly",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/jarnalyrkar/KQ5ST",
  "runtime_profiles": [],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [],
  "source_platforms": [
    "Amiga",
    "DOS"
  ],
  "status": "Upstream source reviewed; no independent execution",
  "subjects": [
    "King's Quest V"
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
  "title": "King's Quest V — Atari ST shim port",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "King's Quest V",
  "work_kinds": [
    "reverse-engineering-derived-port",
    "binary-analysis",
    "data-format-analysis"
  ]
}
```

### Identity (reviewed)

Pinned README identifies King's Quest V and this project.
- https://github.com/jarnalyrkar/kq5st/blob/06c2f9c103dba76a156c03d947ff882f7adf7986/README.md

### Classification (reviewed)

Converts and patches the original Amiga SCI interpreter into an Atari ST program with an AmigaOS/hardware shim and PC EGA art. Compatibility rehosting, not restored interpreter source.
- https://github.com/jarnalyrkar/kq5st/blob/06c2f9c103dba76a156c03d947ff882f7adf7986/README.md

### Source CPU (reviewed)

Documented source platform or executable uses m68k.
- https://github.com/jarnalyrkar/kq5st/blob/06c2f9c103dba76a156c03d947ff882f7adf7986/README.md

### Target CPU (reviewed)

Documented output uses m68k.
- https://github.com/jarnalyrkar/kq5st/blob/06c2f9c103dba76a156c03d947ff882f7adf7986/README.md

### Build (reviewed)

The author reports Hatari playtesting through early areas; original Amiga and DOS game data are required. No independent build, execution, gameplay or byte comparison was performed.
- https://github.com/jarnalyrkar/kq5st/blob/06c2f9c103dba76a156c03d947ff882f7adf7986/README.md

### Runtime profiles (no-evidence-found)

No independently verified minimum hardware profile.
- https://github.com/jarnalyrkar/kq5st/blob/06c2f9c103dba76a156c03d947ff882f7adf7986/README.md

### AI (reviewed)

Claude collaboration is disclosed in the upstream README or commit.
- https://github.com/jarnalyrkar/kq5st/blob/06c2f9c103dba76a156c03d947ff882f7adf7986/README.md

### Relationships (reviewed)

Distinct from the tracked King's Quest VI AGI demake repair; this uses the King's Quest V Amiga interpreter and PC artwork. Previous deferral resolved as compatibility rehosting, not restored interpreter source.
- https://github.com/jarnalyrkar/kq5st/blob/06c2f9c103dba76a156c03d947ff882f7adf7986/README.md

## Dogs of War — Atari ST static recompilation

Project ID: dogs-of-war-atari-st-static-recomp-voodatari · Overall audit: partial

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
  "display_title": "Dogs of War — Atari ST static recompilation",
  "execution_paths": [
    {
      "evidence": [
        "https://github.com/voodatari/Dogs-of-War-Atari-ST-Recomp/blob/6116729d389d254c5f17042598ef79d3176f736e/README.md"
      ],
      "method": "baked-emulation",
      "name": "Documented port",
      "notes": "Translates the Atari ST program to C and links it to a retained small STE machine runtime. This is baked emulation despite not interpreting 68000 instructions.",
      "status": "partial"
    }
  ],
  "id": "dogs-of-war-atari-st-static-recomp-voodatari",
  "last_activity": null,
  "last_checked": "2026-11-12",
  "re_started": null,
  "reconstructed_languages": [
    "C"
  ],
  "record_class": "subject",
  "repo": "https://github.com/voodatari/Dogs-of-War-Atari-ST-Recomp",
  "runtime_profiles": [],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [],
  "source_platforms": [
    "Atari ST"
  ],
  "status": "Upstream source reviewed; no independent execution",
  "subjects": [
    "Dogs of War"
  ],
  "tags": [],
  "target_cpu": [
    "x86-64"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Windows",
    "Linux"
  ],
  "techniques": [],
  "title": "Dogs of War — Atari ST static recompilation",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "Dogs of War",
  "work_kinds": [
    "reverse-engineering-derived-port",
    "binary-analysis"
  ]
}
```

### Identity (reviewed)

Pinned README identifies Dogs of War and this project.
- https://github.com/voodatari/dogs-of-war-atari-st-recomp/blob/6116729d389d254c5f17042598ef79d3176f736e/README.md

### Classification (reviewed)

Translates the Atari ST program to C and links it to a retained small STE machine runtime. This is baked emulation despite not interpreting 68000 instructions.
- https://github.com/voodatari/dogs-of-war-atari-st-recomp/blob/6116729d389d254c5f17042598ef79d3176f736e/README.md

### Source CPU (reviewed)

Documented source platform or executable uses m68k.
- https://github.com/voodatari/dogs-of-war-atari-st-recomp/blob/6116729d389d254c5f17042598ef79d3176f736e/README.md

### Target CPU (reviewed)

Documented output uses x86-64.
- https://github.com/voodatari/dogs-of-war-atari-st-recomp/blob/6116729d389d254c5f17042598ef79d3176f736e/README.md

### Build (reviewed)

Author describes Windows and Linux builds requiring original game data. No independent build, execution, gameplay or byte comparison was performed.
- https://github.com/voodatari/dogs-of-war-atari-st-recomp/blob/6116729d389d254c5f17042598ef79d3176f736e/README.md

### Runtime profiles (no-evidence-found)

No independently verified minimum hardware profile.
- https://github.com/voodatari/dogs-of-war-atari-st-recomp/blob/6116729d389d254c5f17042598ef79d3176f736e/README.md

### AI (reviewed)

Claude collaboration is disclosed in the upstream README or commit.
- https://github.com/voodatari/dogs-of-war-atari-st-recomp/blob/6116729d389d254c5f17042598ef79d3176f736e/README.md

### Relationships (reviewed)

Distinct repository; not assumed equivalent to other tracked work.
- https://github.com/voodatari/dogs-of-war-atari-st-recomp/blob/6116729d389d254c5f17042598ef79d3176f736e/README.md

## Pinned evidence manifest

- dogs-of-war-atari-st-static-recomp-voodatari-readme: https://github.com/voodatari/dogs-of-war-atari-st-recomp/blob/6116729d389d254c5f17042598ef79d3176f736e/README.md (Git blob b929511cb978e274fcf3a68697b7fd377a3c3e3f)
- kings-quest-v-amiga-to-atari-st-shim-readme: https://github.com/jarnalyrkar/kq5st/blob/06c2f9c103dba76a156c03d947ff882f7adf7986/README.md (Git blob fdb9245a77c6298985bb3721b7cc6db90c715e82)

## Sources

```json
[
  {
    "first_indexed": "2026-11-12",
    "id": "github-dogs-of-war-atari-st-static-recomp-voodatari",
    "kind": "github-repository",
    "last_reviewed": "2026-11-12",
    "open_task_ids": [],
    "projects_promoted": [
      "dogs-of-war-atari-st-static-recomp-voodatari"
    ],
    "reason": "Translates the Atari ST program to C and links it to a retained small STE machine runtime. This is baked emulation despite not interpreting 68000 instructions.",
    "review_state": "partial",
    "source": "https://github.com/voodatari/Dogs-of-War-Atari-ST-Recomp"
  }
]
```

## Research event notes

Personally reviewed upstream pinned READMEs. No independent build, gameplay or byte comparison. Screamer and RedCat were removed after current main showed they are already tracked.
