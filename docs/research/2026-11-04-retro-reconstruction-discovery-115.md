# Amiga and Atari ST game discovery

Screen Amiga and Atari ST game research: add 6 projects and defer 4 for source or architecture review.

Date: 2026-11-04 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- vairn-mm2 / Target CPU (no-evidence-found): No target CPU minimum independently established.
- vairn-mm2 / Runtime profiles (no-evidence-found): No independently verified complete runtime profile.
- vairn-mm2 / AI (no-evidence-found): No actual AI contribution established from inspected evidence; absence does not establish non-use.
- czeskij-silk-worm-revisited / Target CPU (no-evidence-found): No target CPU minimum independently established.
- czeskij-silk-worm-revisited / Runtime profiles (no-evidence-found): No independently verified complete runtime profile.
- czeskij-silk-worm-revisited / AI (no-evidence-found): No actual AI contribution established from inspected evidence; absence does not establish non-use.
- amigarecomp-skrecomp / Target CPU (no-evidence-found): No target CPU minimum independently established.
- amigarecomp-skrecomp / Runtime profiles (no-evidence-found): No independently verified complete runtime profile.
- shaid-sorcery / Target CPU (no-evidence-found): No target CPU minimum independently established.
- shaid-sorcery / Runtime profiles (no-evidence-found): No independently verified complete runtime profile.
- shaid-sorcery / AI (no-evidence-found): No actual AI contribution established from inspected evidence; absence does not establish non-use.
- capusto-into-the-eagle-s-nest / Target CPU (no-evidence-found): No target CPU minimum independently established.
- capusto-into-the-eagle-s-nest / Runtime profiles (no-evidence-found): No independently verified complete runtime profile.
- capusto-into-the-eagle-s-nest / AI (no-evidence-found): No actual AI contribution established from inspected evidence; absence does not establish non-use.
- yuryyudin-bouncingbubbles / Target CPU (no-evidence-found): No target CPU minimum independently established.
- yuryyudin-bouncingbubbles / Runtime profiles (no-evidence-found): No independently verified complete runtime profile.

## Might & Magic II — Amiga source analysis and remake

Project ID: vairn-mm2 · Overall audit: partial

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
  "display_title": "Might & Magic II — Amiga source analysis and remake",
  "id": "vairn-mm2",
  "last_activity": null,
  "last_checked": "2026-11-04",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "C++"
  ],
  "record_class": "subject",
  "repo": "https://github.com/Vairn/MM2",
  "runtime_profiles": [],
  "source_cpu": [
    "68000"
  ],
  "source_language": [],
  "source_platforms": [
    "Amiga"
  ],
  "status": "Source inspected; no independent build or execution",
  "subjects": [
    "Might & Magic II"
  ],
  "tags": [],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Amiga",
    "Windows",
    "Linux",
    "macOS"
  ],
  "techniques": [],
  "title": "Might & Magic II — Amiga source analysis and remake",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "MM2",
  "work_kinds": [
    "disassembly",
    "data-format-analysis",
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Might & Magic II — Amiga source analysis and remake. Repository and pinned source reviewed.
- https://github.com/Vairn/MM2/blob/e67409c4cd8a34858e2b25e6b41600092c238c0f/README.md
- https://github.com/Vairn/MM2/blob/e67409c4cd8a34858e2b25e6b41600092c238c0f/EXTRACTED/decomp/mm2_create_character.c

### Classification (reviewed)

Original Amiga 68k analysis and data codecs feed a C++ remake; the character creation code explicitly marks its RNG as not byte-perfect. The remake remains in progress.
- https://github.com/Vairn/MM2/blob/e67409c4cd8a34858e2b25e6b41600092c238c0f/README.md
- https://github.com/Vairn/MM2/blob/e67409c4cd8a34858e2b25e6b41600092c238c0f/EXTRACTED/decomp/mm2_create_character.c

### Source CPU (reviewed)

Original Amiga game uses 68000 architecture; exact minimum not inferred.
- https://github.com/Vairn/MM2/blob/e67409c4cd8a34858e2b25e6b41600092c238c0f/README.md
- https://github.com/Vairn/MM2/blob/e67409c4cd8a34858e2b25e6b41600092c238c0f/EXTRACTED/decomp/mm2_create_character.c

### Target CPU (no-evidence-found)

No target CPU minimum independently established.
- https://github.com/Vairn/MM2/blob/e67409c4cd8a34858e2b25e6b41600092c238c0f/README.md
- https://github.com/Vairn/MM2/blob/e67409c4cd8a34858e2b25e6b41600092c238c0f/EXTRACTED/decomp/mm2_create_character.c

### Build (reviewed)

Project provides source and describes build steps or a browser frontend. No independent compilation, execution, gameplay or byte comparison.
- https://github.com/Vairn/MM2/blob/e67409c4cd8a34858e2b25e6b41600092c238c0f/README.md
- https://github.com/Vairn/MM2/blob/e67409c4cd8a34858e2b25e6b41600092c238c0f/EXTRACTED/decomp/mm2_create_character.c

### Runtime profiles (no-evidence-found)

No independently verified complete runtime profile.
- https://github.com/Vairn/MM2/blob/e67409c4cd8a34858e2b25e6b41600092c238c0f/README.md
- https://github.com/Vairn/MM2/blob/e67409c4cd8a34858e2b25e6b41600092c238c0f/EXTRACTED/decomp/mm2_create_character.c

### AI (no-evidence-found)

No actual AI contribution established from inspected evidence; absence does not establish non-use.
- https://github.com/Vairn/MM2/blob/e67409c4cd8a34858e2b25e6b41600092c238c0f/README.md
- https://github.com/Vairn/MM2/blob/e67409c4cd8a34858e2b25e6b41600092c238c0f/EXTRACTED/decomp/mm2_create_character.c

### Relationships (reviewed)

Distinct project repository; same-title projects remain separate and no equivalence or completeness is inferred.
- https://github.com/Vairn/MM2/blob/e67409c4cd8a34858e2b25e6b41600092c238c0f/README.md
- https://github.com/Vairn/MM2/blob/e67409c4cd8a34858e2b25e6b41600092c238c0f/EXTRACTED/decomp/mm2_create_character.c

## Silkworm — Amiga analysis and browser remake

Project ID: czeskij-silk-worm-revisited · Overall audit: partial

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
  "display_title": "Silkworm — Amiga analysis and browser remake",
  "id": "czeskij-silk-worm-revisited",
  "last_activity": null,
  "last_checked": "2026-11-04",
  "re_started": null,
  "reconstructed_languages": [
    "JavaScript"
  ],
  "record_class": "subject",
  "repo": "https://github.com/czeskij/silk-worm-revisited",
  "runtime_profiles": [],
  "source_cpu": [
    "68000"
  ],
  "source_language": [],
  "source_platforms": [
    "Amiga"
  ],
  "status": "Source inspected; no independent build or execution",
  "subjects": [
    "Silkworm"
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
  "title": "Silkworm — Amiga analysis and browser remake",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "silk-worm-revisited",
  "work_kinds": [
    "disassembly",
    "data-format-analysis",
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Silkworm — Amiga analysis and browser remake. Repository and pinned source reviewed.
- https://github.com/czeskij/silk-worm-revisited/blob/42e4355342efe55abcc1b41611c2a92badcdf04e/README.md
- https://github.com/czeskij/silk-worm-revisited/blob/42e4355342efe55abcc1b41611c2a92badcdf04e/remake/README.md

### Classification (reviewed)

Disk, memory, level and enemy-wave analysis supports a browser remake from the user-supplied disk. Disassemblies are regenerated locally; the author identifies gameplay approximations.
- https://github.com/czeskij/silk-worm-revisited/blob/42e4355342efe55abcc1b41611c2a92badcdf04e/README.md
- https://github.com/czeskij/silk-worm-revisited/blob/42e4355342efe55abcc1b41611c2a92badcdf04e/remake/README.md

### Source CPU (reviewed)

Original Amiga game uses 68000 architecture; exact minimum not inferred.
- https://github.com/czeskij/silk-worm-revisited/blob/42e4355342efe55abcc1b41611c2a92badcdf04e/README.md
- https://github.com/czeskij/silk-worm-revisited/blob/42e4355342efe55abcc1b41611c2a92badcdf04e/remake/README.md

### Target CPU (no-evidence-found)

No target CPU minimum independently established.
- https://github.com/czeskij/silk-worm-revisited/blob/42e4355342efe55abcc1b41611c2a92badcdf04e/README.md
- https://github.com/czeskij/silk-worm-revisited/blob/42e4355342efe55abcc1b41611c2a92badcdf04e/remake/README.md

### Build (reviewed)

Project provides source and describes build steps or a browser frontend. No independent compilation, execution, gameplay or byte comparison.
- https://github.com/czeskij/silk-worm-revisited/blob/42e4355342efe55abcc1b41611c2a92badcdf04e/README.md
- https://github.com/czeskij/silk-worm-revisited/blob/42e4355342efe55abcc1b41611c2a92badcdf04e/remake/README.md

### Runtime profiles (no-evidence-found)

No independently verified complete runtime profile.
- https://github.com/czeskij/silk-worm-revisited/blob/42e4355342efe55abcc1b41611c2a92badcdf04e/README.md
- https://github.com/czeskij/silk-worm-revisited/blob/42e4355342efe55abcc1b41611c2a92badcdf04e/remake/README.md

### AI (no-evidence-found)

No actual AI contribution established from inspected evidence; absence does not establish non-use.
- https://github.com/czeskij/silk-worm-revisited/blob/42e4355342efe55abcc1b41611c2a92badcdf04e/README.md
- https://github.com/czeskij/silk-worm-revisited/blob/42e4355342efe55abcc1b41611c2a92badcdf04e/remake/README.md

### Relationships (reviewed)

Distinct project repository; same-title projects remain separate and no equivalence or completeness is inferred.
- https://github.com/czeskij/silk-worm-revisited/blob/42e4355342efe55abcc1b41611c2a92badcdf04e/README.md
- https://github.com/czeskij/silk-worm-revisited/blob/42e4355342efe55abcc1b41611c2a92badcdf04e/remake/README.md

## Soccer Kid — Amiga game logic reimplementation

Project ID: amigarecomp-skrecomp · Overall audit: partial

### Typed catalogue values

```json
{
  "ai": {
    "evidence": [
      "README explicitly credits Claude Opus for reverse engineering, C code and tests: https://github.com/AmigaRecomp/skrecomp/blob/8241bed158a73d5031f953f30f455a3541ee3272/README.md"
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
  "display_title": "Soccer Kid — Amiga game logic reimplementation",
  "id": "amigarecomp-skrecomp",
  "last_activity": null,
  "last_checked": "2026-11-04",
  "re_started": null,
  "reconstructed_languages": [
    "C"
  ],
  "record_class": "subject",
  "repo": "https://github.com/AmigaRecomp/skrecomp",
  "runtime_profiles": [],
  "source_cpu": [
    "68000"
  ],
  "source_language": [],
  "source_platforms": [
    "Amiga"
  ],
  "status": "Source inspected; no independent build or execution",
  "subjects": [
    "Soccer Kid"
  ],
  "tags": [],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Windows",
    "Linux",
    "macOS"
  ],
  "techniques": [],
  "title": "Soccer Kid — Amiga game logic reimplementation",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "skrecomp",
  "work_kinds": [
    "disassembly",
    "reverse-engineering-derived-port"
  ]
}
```

### Identity (reviewed)

Soccer Kid — Amiga game logic reimplementation. Repository and pinned source reviewed.
- https://github.com/AmigaRecomp/skrecomp/blob/8241bed158a73d5031f953f30f455a3541ee3272/README.md
- https://github.com/AmigaRecomp/skrecomp/blob/8241bed158a73d5031f953f30f455a3541ee3272/src/game/attr_country_london.c

### Classification (reviewed)

Author describes rewriting 68000 game routines in C using original disk data; includes a level editor. Mac build tested by author; other platforms not independently verified.
- https://github.com/AmigaRecomp/skrecomp/blob/8241bed158a73d5031f953f30f455a3541ee3272/README.md
- https://github.com/AmigaRecomp/skrecomp/blob/8241bed158a73d5031f953f30f455a3541ee3272/src/game/attr_country_london.c

### Source CPU (reviewed)

Original Amiga game uses 68000 architecture; exact minimum not inferred.
- https://github.com/AmigaRecomp/skrecomp/blob/8241bed158a73d5031f953f30f455a3541ee3272/README.md
- https://github.com/AmigaRecomp/skrecomp/blob/8241bed158a73d5031f953f30f455a3541ee3272/src/game/attr_country_london.c

### Target CPU (no-evidence-found)

No target CPU minimum independently established.
- https://github.com/AmigaRecomp/skrecomp/blob/8241bed158a73d5031f953f30f455a3541ee3272/README.md
- https://github.com/AmigaRecomp/skrecomp/blob/8241bed158a73d5031f953f30f455a3541ee3272/src/game/attr_country_london.c

### Build (reviewed)

Project provides source and describes build steps or a browser frontend. No independent compilation, execution, gameplay or byte comparison.
- https://github.com/AmigaRecomp/skrecomp/blob/8241bed158a73d5031f953f30f455a3541ee3272/README.md
- https://github.com/AmigaRecomp/skrecomp/blob/8241bed158a73d5031f953f30f455a3541ee3272/src/game/attr_country_london.c

### Runtime profiles (no-evidence-found)

No independently verified complete runtime profile.
- https://github.com/AmigaRecomp/skrecomp/blob/8241bed158a73d5031f953f30f455a3541ee3272/README.md
- https://github.com/AmigaRecomp/skrecomp/blob/8241bed158a73d5031f953f30f455a3541ee3272/src/game/attr_country_london.c

### AI (reviewed)

AI involvement explicitly disclosed.
- https://github.com/AmigaRecomp/skrecomp/blob/8241bed158a73d5031f953f30f455a3541ee3272/README.md
- https://github.com/AmigaRecomp/skrecomp/blob/8241bed158a73d5031f953f30f455a3541ee3272/src/game/attr_country_london.c

### Relationships (reviewed)

Distinct project repository; same-title projects remain separate and no equivalence or completeness is inferred.
- https://github.com/AmigaRecomp/skrecomp/blob/8241bed158a73d5031f953f30f455a3541ee3272/README.md
- https://github.com/AmigaRecomp/skrecomp/blob/8241bed158a73d5031f953f30f455a3541ee3272/src/game/attr_country_london.c

## Wizardry 6 — Amiga data and executable analysis

Project ID: shaid-sorcery · Overall audit: partial

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
  "display_title": "Wizardry 6 — Amiga data and executable analysis",
  "id": "shaid-sorcery",
  "last_activity": null,
  "last_checked": "2026-11-04",
  "re_started": null,
  "reconstructed_languages": [
    "TypeScript"
  ],
  "record_class": "subject",
  "repo": "https://github.com/Shaid/sorcery",
  "runtime_profiles": [],
  "source_cpu": [
    "68000"
  ],
  "source_language": [],
  "source_platforms": [
    "Amiga"
  ],
  "status": "Source inspected; no independent build or execution",
  "subjects": [
    "Wizardry 6"
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
  "title": "Wizardry 6 — Amiga data and executable analysis",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "sorcery",
  "work_kinds": [
    "disassembly",
    "data-format-analysis",
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Wizardry 6 — Amiga data and executable analysis. Repository and pinned source reviewed.
- https://github.com/Shaid/sorcery/blob/1036800ee6394252672e36dea7ddceab91555e5f/README.md
- https://github.com/Shaid/sorcery/blob/1036800ee6394252672e36dea7ddceab91555e5f/docs/wizardry6/amiga/data-structure.md

### Classification (reviewed)

Wizardry 6 executable and asset formats analysed from Amiga data; a browser implementation and asset pipeline are in progress. Research distinguishes verified format facts from hypotheses.
- https://github.com/Shaid/sorcery/blob/1036800ee6394252672e36dea7ddceab91555e5f/README.md
- https://github.com/Shaid/sorcery/blob/1036800ee6394252672e36dea7ddceab91555e5f/docs/wizardry6/amiga/data-structure.md

### Source CPU (reviewed)

Original Amiga game uses 68000 architecture; exact minimum not inferred.
- https://github.com/Shaid/sorcery/blob/1036800ee6394252672e36dea7ddceab91555e5f/README.md
- https://github.com/Shaid/sorcery/blob/1036800ee6394252672e36dea7ddceab91555e5f/docs/wizardry6/amiga/data-structure.md

### Target CPU (no-evidence-found)

No target CPU minimum independently established.
- https://github.com/Shaid/sorcery/blob/1036800ee6394252672e36dea7ddceab91555e5f/README.md
- https://github.com/Shaid/sorcery/blob/1036800ee6394252672e36dea7ddceab91555e5f/docs/wizardry6/amiga/data-structure.md

### Build (reviewed)

Project provides source and describes build steps or a browser frontend. No independent compilation, execution, gameplay or byte comparison.
- https://github.com/Shaid/sorcery/blob/1036800ee6394252672e36dea7ddceab91555e5f/README.md
- https://github.com/Shaid/sorcery/blob/1036800ee6394252672e36dea7ddceab91555e5f/docs/wizardry6/amiga/data-structure.md

### Runtime profiles (no-evidence-found)

No independently verified complete runtime profile.
- https://github.com/Shaid/sorcery/blob/1036800ee6394252672e36dea7ddceab91555e5f/README.md
- https://github.com/Shaid/sorcery/blob/1036800ee6394252672e36dea7ddceab91555e5f/docs/wizardry6/amiga/data-structure.md

### AI (no-evidence-found)

No actual AI contribution established from inspected evidence; absence does not establish non-use.
- https://github.com/Shaid/sorcery/blob/1036800ee6394252672e36dea7ddceab91555e5f/README.md
- https://github.com/Shaid/sorcery/blob/1036800ee6394252672e36dea7ddceab91555e5f/docs/wizardry6/amiga/data-structure.md

### Relationships (reviewed)

Distinct project repository; same-title projects remain separate and no equivalence or completeness is inferred.
- https://github.com/Shaid/sorcery/blob/1036800ee6394252672e36dea7ddceab91555e5f/README.md
- https://github.com/Shaid/sorcery/blob/1036800ee6394252672e36dea7ddceab91555e5f/docs/wizardry6/amiga/data-structure.md

## Into the Eagle's Nest — Amiga C recreation

Project ID: capusto-into-the-eagle-s-nest · Overall audit: partial

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
  "display_title": "Into the Eagle's Nest — Amiga C recreation",
  "id": "capusto-into-the-eagle-s-nest",
  "last_activity": null,
  "last_checked": "2026-11-04",
  "re_started": null,
  "reconstructed_languages": [
    "C"
  ],
  "record_class": "subject",
  "repo": "https://github.com/CaPusto/Into-the-Eagle-s-Nest",
  "runtime_profiles": [],
  "source_cpu": [
    "68000"
  ],
  "source_language": [],
  "source_platforms": [
    "Amiga"
  ],
  "status": "Source inspected; no independent build or execution",
  "subjects": [
    "Into the Eagle's Nest"
  ],
  "tags": [],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Windows",
    "Linux",
    "macOS"
  ],
  "techniques": [],
  "title": "Into the Eagle's Nest — Amiga C recreation",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "Into-the-Eagle-s-Nest",
  "work_kinds": [
    "reverse-engineering-derived-port",
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Into the Eagle's Nest — Amiga C recreation. Repository and pinned source reviewed.
- https://github.com/CaPusto/Into-the-Eagle-s-Nest/blob/81b1fd0d2c73f1f92ca64e2a26691c1eaff4a893/README.md
- https://github.com/CaPusto/Into-the-Eagle-s-Nest/blob/81b1fd0d2c73f1f92ca64e2a26691c1eaff4a893/src/game/enemies.c

### Classification (reviewed)

C/SDL3 gameplay recreation using converted Amiga assets; enemy source refers to original assembly. README describes a coming-soon project, so fidelity and completeness are not independently established.
- https://github.com/CaPusto/Into-the-Eagle-s-Nest/blob/81b1fd0d2c73f1f92ca64e2a26691c1eaff4a893/README.md
- https://github.com/CaPusto/Into-the-Eagle-s-Nest/blob/81b1fd0d2c73f1f92ca64e2a26691c1eaff4a893/src/game/enemies.c

### Source CPU (reviewed)

Original Amiga game uses 68000 architecture; exact minimum not inferred.
- https://github.com/CaPusto/Into-the-Eagle-s-Nest/blob/81b1fd0d2c73f1f92ca64e2a26691c1eaff4a893/README.md
- https://github.com/CaPusto/Into-the-Eagle-s-Nest/blob/81b1fd0d2c73f1f92ca64e2a26691c1eaff4a893/src/game/enemies.c

### Target CPU (no-evidence-found)

No target CPU minimum independently established.
- https://github.com/CaPusto/Into-the-Eagle-s-Nest/blob/81b1fd0d2c73f1f92ca64e2a26691c1eaff4a893/README.md
- https://github.com/CaPusto/Into-the-Eagle-s-Nest/blob/81b1fd0d2c73f1f92ca64e2a26691c1eaff4a893/src/game/enemies.c

### Build (reviewed)

Project provides source and describes build steps or a browser frontend. No independent compilation, execution, gameplay or byte comparison.
- https://github.com/CaPusto/Into-the-Eagle-s-Nest/blob/81b1fd0d2c73f1f92ca64e2a26691c1eaff4a893/README.md
- https://github.com/CaPusto/Into-the-Eagle-s-Nest/blob/81b1fd0d2c73f1f92ca64e2a26691c1eaff4a893/src/game/enemies.c

### Runtime profiles (no-evidence-found)

No independently verified complete runtime profile.
- https://github.com/CaPusto/Into-the-Eagle-s-Nest/blob/81b1fd0d2c73f1f92ca64e2a26691c1eaff4a893/README.md
- https://github.com/CaPusto/Into-the-Eagle-s-Nest/blob/81b1fd0d2c73f1f92ca64e2a26691c1eaff4a893/src/game/enemies.c

### AI (no-evidence-found)

No actual AI contribution established from inspected evidence; absence does not establish non-use.
- https://github.com/CaPusto/Into-the-Eagle-s-Nest/blob/81b1fd0d2c73f1f92ca64e2a26691c1eaff4a893/README.md
- https://github.com/CaPusto/Into-the-Eagle-s-Nest/blob/81b1fd0d2c73f1f92ca64e2a26691c1eaff4a893/src/game/enemies.c

### Relationships (reviewed)

Distinct project repository; same-title projects remain separate and no equivalence or completeness is inferred.
- https://github.com/CaPusto/Into-the-Eagle-s-Nest/blob/81b1fd0d2c73f1f92ca64e2a26691c1eaff4a893/README.md
- https://github.com/CaPusto/Into-the-Eagle-s-Nest/blob/81b1fd0d2c73f1f92ca64e2a26691c1eaff4a893/src/game/enemies.c

## Bouncing Boubles — Atari ST analysis and browser recreation

Project ID: yuryyudin-bouncingbubbles · Overall audit: partial

### Typed catalogue values

```json
{
  "ai": {
    "evidence": [
      "GitHub repository description explicitly describes a one-prompt AI remake."
    ],
    "tools": [],
    "usage": true
  },
  "build": {
    "byte_exact": null,
    "compilable": null,
    "playable": null,
    "runnable": null
  },
  "display_title": "Bouncing Boubles — Atari ST analysis and browser recreation",
  "id": "yuryyudin-bouncingbubbles",
  "last_activity": null,
  "last_checked": "2026-11-04",
  "re_started": null,
  "reconstructed_languages": [
    "JavaScript"
  ],
  "record_class": "subject",
  "repo": "https://github.com/YuryYudin/BouncingBubbles",
  "runtime_profiles": [],
  "source_cpu": [
    "68000"
  ],
  "source_language": [],
  "source_platforms": [
    "Atari ST"
  ],
  "status": "Source inspected; no independent build or execution",
  "subjects": [
    "Bouncing Boubles"
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
  "title": "Bouncing Boubles — Atari ST analysis and browser recreation",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "BouncingBubbles",
  "work_kinds": [
    "disassembly",
    "data-format-analysis",
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Bouncing Boubles — Atari ST analysis and browser recreation. Repository and pinned source reviewed.
- https://github.com/YuryYudin/BouncingBubbles/blob/03123217cf40cd8ba8d3fc56a775653b1cdb225d/README.md
- https://github.com/YuryYudin/BouncingBubbles/blob/03123217cf40cd8ba8d3fc56a775653b1cdb225d/research/game_logic_report.md

### Classification (reviewed)

Browser recreation informed by a compiled GFA-BASIC executable, emulator memory observations and disassembly; detailed game logic report records addresses and recovered behavior.
- https://github.com/YuryYudin/BouncingBubbles/blob/03123217cf40cd8ba8d3fc56a775653b1cdb225d/README.md
- https://github.com/YuryYudin/BouncingBubbles/blob/03123217cf40cd8ba8d3fc56a775653b1cdb225d/research/game_logic_report.md

### Source CPU (reviewed)

Original Atari ST game uses 68000 architecture; exact minimum not inferred.
- https://github.com/YuryYudin/BouncingBubbles/blob/03123217cf40cd8ba8d3fc56a775653b1cdb225d/README.md
- https://github.com/YuryYudin/BouncingBubbles/blob/03123217cf40cd8ba8d3fc56a775653b1cdb225d/research/game_logic_report.md

### Target CPU (no-evidence-found)

No target CPU minimum independently established.
- https://github.com/YuryYudin/BouncingBubbles/blob/03123217cf40cd8ba8d3fc56a775653b1cdb225d/README.md
- https://github.com/YuryYudin/BouncingBubbles/blob/03123217cf40cd8ba8d3fc56a775653b1cdb225d/research/game_logic_report.md

### Build (reviewed)

Project provides source and describes build steps or a browser frontend. No independent compilation, execution, gameplay or byte comparison.
- https://github.com/YuryYudin/BouncingBubbles/blob/03123217cf40cd8ba8d3fc56a775653b1cdb225d/README.md
- https://github.com/YuryYudin/BouncingBubbles/blob/03123217cf40cd8ba8d3fc56a775653b1cdb225d/research/game_logic_report.md

### Runtime profiles (no-evidence-found)

No independently verified complete runtime profile.
- https://github.com/YuryYudin/BouncingBubbles/blob/03123217cf40cd8ba8d3fc56a775653b1cdb225d/README.md
- https://github.com/YuryYudin/BouncingBubbles/blob/03123217cf40cd8ba8d3fc56a775653b1cdb225d/research/game_logic_report.md

### AI (reviewed)

AI involvement explicitly disclosed.
- https://github.com/YuryYudin/BouncingBubbles/blob/03123217cf40cd8ba8d3fc56a775653b1cdb225d/README.md
- https://github.com/YuryYudin/BouncingBubbles/blob/03123217cf40cd8ba8d3fc56a775653b1cdb225d/research/game_logic_report.md

### Relationships (reviewed)

Distinct project repository; same-title projects remain separate and no equivalence or completeness is inferred.
- https://github.com/YuryYudin/BouncingBubbles/blob/03123217cf40cd8ba8d3fc56a775653b1cdb225d/README.md
- https://github.com/YuryYudin/BouncingBubbles/blob/03123217cf40cd8ba8d3fc56a775653b1cdb225d/research/game_logic_report.md

## Pinned evidence manifest

- amigarecomp-skrecomp-readme-md: https://github.com/amigarecomp/skrecomp/blob/8241bed158a73d5031f953f30f455a3541ee3272/README.md (Git blob cb7106e89c6fca69255bf82226d5427899f530cd)
- amigarecomp-skrecomp-src-game-attr-country-london-c: https://github.com/amigarecomp/skrecomp/blob/8241bed158a73d5031f953f30f455a3541ee3272/src/game/attr_country_london.c (Git blob f2a99146aebca156396a701d218f71b2510b5b5e)
- capusto-into-the-eagle-s-nest-readme-md: https://github.com/capusto/into-the-eagle-s-nest/blob/81b1fd0d2c73f1f92ca64e2a26691c1eaff4a893/README.md (Git blob d37405898162af78507c6542596379bcbd11b945)
- capusto-into-the-eagle-s-nest-src-game-enemies-c: https://github.com/capusto/into-the-eagle-s-nest/blob/81b1fd0d2c73f1f92ca64e2a26691c1eaff4a893/src/game/enemies.c (Git blob 3a35bf84f7a43047b22e8de19cc18c82fb9398e3)
- czeskij-silk-worm-revisited-readme-md: https://github.com/czeskij/silk-worm-revisited/blob/42e4355342efe55abcc1b41611c2a92badcdf04e/README.md (Git blob eb2a16bcc6933af83dce149554be7671762a30a2)
- czeskij-silk-worm-revisited-remake-readme-md: https://github.com/czeskij/silk-worm-revisited/blob/42e4355342efe55abcc1b41611c2a92badcdf04e/remake/README.md (Git blob 814e1e34e048951b61f3693cc8e83fc74d217d7e)
- grumbel-turrican-port-readme-md: https://github.com/grumbel/turrican-port/blob/8009806a95bfc8fe4d9c8ca0a34ed5c1838bd236/README.md (Git blob 056b1ac3bcd3ac45238c3b0257342f84f2a6555a)
- josteintopland-jumpingjackson-readme-md: https://github.com/josteintopland/jumpingjackson/blob/9e8986d0a16fa98956752ca0c4a2d455a53d18f9/README.md (Git blob 247f9280ee738e997711415cf650d60e386466f0)
- jungjozef-swiv-internal-actor-lifted-go: https://github.com/jungjozef/swiv/blob/e752dfd6cfcc880514066b92b6454a6834d02f24/internal/actor/lifted.go (Git blob 541a987e9977fd86caebc5cd780a23c27eb0e762)
- jungjozef-swiv-readme-md: https://github.com/jungjozef/swiv/blob/e752dfd6cfcc880514066b92b6454a6834d02f24/README.md (Git blob 4262d29e4520e43579ae4d4b23ddd73de937782d)
- shaid-sorcery-docs-wizardry6-amiga-data-structure-md: https://github.com/shaid/sorcery/blob/1036800ee6394252672e36dea7ddceab91555e5f/docs/wizardry6/amiga/data-structure.md (Git blob 453ece0ee387e8b1e23f9dabfb2e393b3e2cb0b4)
- shaid-sorcery-readme-md: https://github.com/shaid/sorcery/blob/1036800ee6394252672e36dea7ddceab91555e5f/README.md (Git blob d91aba4e247f4680c4e70c55ecd34231b7dc4dbf)
- tombonator3000-moonstone-readme-md: https://github.com/tombonator3000/moonstone/blob/69d9f8200c3244df0d5073f8e64f50cb479a5916/README.md (Git blob 6c6375d45279c51ca39dc1e2c40fb6dcebcc45e8)
- vairn-mm2-extracted-decomp-mm2-create-character-c: https://github.com/vairn/mm2/blob/e67409c4cd8a34858e2b25e6b41600092c238c0f/EXTRACTED/decomp/mm2_create_character.c (Git blob dfb9b07eec22c5c0a70c55e20f41137c82756f62)
- vairn-mm2-readme-md: https://github.com/vairn/mm2/blob/e67409c4cd8a34858e2b25e6b41600092c238c0f/README.md (Git blob 2aec37bec43ee98040dd3e09a12bdfd9acca8ce8)
- yuryyudin-bouncingbubbles-readme-md: https://github.com/yuryyudin/bouncingbubbles/blob/03123217cf40cd8ba8d3fc56a775653b1cdb225d/README.md (Git blob a4802c0e6a4f865e4847d92ba06720264453c5a8)
- yuryyudin-bouncingbubbles-research-game-logic-report-md: https://github.com/yuryyudin/bouncingbubbles/blob/03123217cf40cd8ba8d3fc56a775653b1cdb225d/research/game_logic_report.md (Git blob e021cce5b02c3e81f9485160653ce5c518c283f8)

## Sources

```json
[
  {
    "first_indexed": "2026-11-04",
    "id": "github-vairn-mm2",
    "kind": "github-repository",
    "last_reviewed": "2026-11-04",
    "open_task_ids": [],
    "projects_promoted": [
      "vairn-mm2"
    ],
    "reason": "Original Amiga 68k analysis and data codecs feed a C++ remake; the character creation code explicitly marks its RNG as not byte-perfect. The remake remains in progress.",
    "review_state": "partial",
    "source": "https://github.com/Vairn/MM2"
  },
  {
    "first_indexed": "2026-11-04",
    "id": "github-czeskij-silk-worm-revisited",
    "kind": "github-repository",
    "last_reviewed": "2026-11-04",
    "open_task_ids": [],
    "projects_promoted": [
      "czeskij-silk-worm-revisited"
    ],
    "reason": "Disk, memory, level and enemy-wave analysis supports a browser remake from the user-supplied disk. Disassemblies are regenerated locally; the author identifies gameplay approximations.",
    "review_state": "partial",
    "source": "https://github.com/czeskij/silk-worm-revisited"
  },
  {
    "first_indexed": "2026-11-04",
    "id": "github-amigarecomp-skrecomp",
    "kind": "github-repository",
    "last_reviewed": "2026-11-04",
    "open_task_ids": [],
    "projects_promoted": [
      "amigarecomp-skrecomp"
    ],
    "reason": "Author describes rewriting 68000 game routines in C using original disk data; includes a level editor. Mac build tested by author; other platforms not independently verified.",
    "review_state": "partial",
    "source": "https://github.com/AmigaRecomp/skrecomp"
  },
  {
    "first_indexed": "2026-11-04",
    "id": "github-shaid-sorcery",
    "kind": "github-repository",
    "last_reviewed": "2026-11-04",
    "open_task_ids": [],
    "projects_promoted": [
      "shaid-sorcery"
    ],
    "reason": "Wizardry 6 executable and asset formats analysed from Amiga data; a browser implementation and asset pipeline are in progress. Research distinguishes verified format facts from hypotheses.",
    "review_state": "partial",
    "source": "https://github.com/Shaid/sorcery"
  },
  {
    "first_indexed": "2026-11-04",
    "id": "github-capusto-into-the-eagle-s-nest",
    "kind": "github-repository",
    "last_reviewed": "2026-11-04",
    "open_task_ids": [],
    "projects_promoted": [
      "capusto-into-the-eagle-s-nest"
    ],
    "reason": "C/SDL3 gameplay recreation using converted Amiga assets; enemy source refers to original assembly. README describes a coming-soon project, so fidelity and completeness are not independently established.",
    "review_state": "partial",
    "source": "https://github.com/CaPusto/Into-the-Eagle-s-Nest"
  },
  {
    "first_indexed": "2026-11-04",
    "id": "github-yuryyudin-bouncingbubbles",
    "kind": "github-repository",
    "last_reviewed": "2026-11-04",
    "open_task_ids": [],
    "projects_promoted": [
      "yuryyudin-bouncingbubbles"
    ],
    "reason": "Browser recreation informed by a compiled GFA-BASIC executable, emulator memory observations and disassembly; detailed game logic report records addresses and recovered behavior.",
    "review_state": "partial",
    "source": "https://github.com/YuryYudin/BouncingBubbles"
  },
  {
    "first_indexed": "2026-11-04",
    "id": "github-jungjozef-swiv",
    "kind": "github-repository",
    "last_reviewed": "2026-11-04",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "SWIV Go reconstruction contains both semantically modelled game objects and generated routines retaining 68000 register and flag state; defer for BAKED EMULATION architecture audit rather than classify the complete runtime from one file.",
    "review_state": "partial",
    "source": "https://github.com/jungjozef/swiv"
  },
  {
    "first_indexed": "2026-11-04",
    "id": "github-grumbel-turrican-port",
    "kind": "github-repository",
    "last_reviewed": "2026-11-04",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "BAKED EMULATION audit: README describes original 68000 code running with Amiga chip models; static recompilation and native reimplementation are planned, not yet demonstrated.",
    "review_state": "partial",
    "source": "https://github.com/Grumbel/turrican-port"
  },
  {
    "first_indexed": "2026-11-04",
    "id": "github-tombonator3000-moonstone",
    "kind": "github-repository",
    "last_reviewed": "2026-11-04",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "BAKED EMULATION audit: README describes original game running on an emulated Amiga with incremental replacements planned; do not conflate with the separate Moonstone ACE reconstruction.",
    "review_state": "partial",
    "source": "https://github.com/Tombonator3000/MOONSTONE"
  },
  {
    "first_indexed": "2026-11-04",
    "id": "github-josteintopland-jumpingjackson",
    "kind": "github-repository",
    "last_reviewed": "2026-11-04",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "README claims a C game clone reverse-engineered from Amiga, but the pinned repository contains only README and licence, not the claimed implementation. Recheck if source appears.",
    "review_state": "partial",
    "source": "https://github.com/JosteinTopland/jumpingjackson"
  }
]
```

## Decisions

```json
[
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/jungjozef/swiv/blob/e752dfd6cfcc880514066b92b6454a6834d02f24/README.md",
      "https://github.com/jungjozef/swiv/blob/e752dfd6cfcc880514066b92b6454a6834d02f24/internal/actor/lifted.go"
    ],
    "id": "pass115-jungjozef-swiv",
    "project_ids": [],
    "reason": "SWIV Go reconstruction contains both semantically modelled game objects and generated routines retaining 68000 register and flag state; defer for BAKED EMULATION architecture audit rather than classify the complete runtime from one file.",
    "reviewed_at": "2026-11-04",
    "source_ids": [
      "github-jungjozef-swiv"
    ],
    "title": "jungjozef/swiv",
    "url": "https://github.com/jungjozef/swiv"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/Grumbel/turrican-port/blob/8009806a95bfc8fe4d9c8ca0a34ed5c1838bd236/README.md"
    ],
    "id": "pass115-grumbel-turrican-port",
    "project_ids": [],
    "reason": "BAKED EMULATION audit: README describes original 68000 code running with Amiga chip models; static recompilation and native reimplementation are planned, not yet demonstrated.",
    "reviewed_at": "2026-11-04",
    "source_ids": [
      "github-grumbel-turrican-port"
    ],
    "title": "Grumbel/turrican-port",
    "url": "https://github.com/Grumbel/turrican-port"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/Tombonator3000/MOONSTONE/blob/69d9f8200c3244df0d5073f8e64f50cb479a5916/README.md"
    ],
    "id": "pass115-tombonator3000-moonstone",
    "project_ids": [],
    "reason": "BAKED EMULATION audit: README describes original game running on an emulated Amiga with incremental replacements planned; do not conflate with the separate Moonstone ACE reconstruction.",
    "reviewed_at": "2026-11-04",
    "source_ids": [
      "github-tombonator3000-moonstone"
    ],
    "title": "Tombonator3000/MOONSTONE",
    "url": "https://github.com/Tombonator3000/MOONSTONE"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/JosteinTopland/jumpingjackson/blob/9e8986d0a16fa98956752ca0c4a2d455a53d18f9/README.md"
    ],
    "id": "pass115-josteintopland-jumpingjackson",
    "project_ids": [],
    "reason": "README claims a C game clone reverse-engineered from Amiga, but the pinned repository contains only README and licence, not the claimed implementation. Recheck if source appears.",
    "reviewed_at": "2026-11-04",
    "source_ids": [
      "github-josteintopland-jumpingjackson"
    ],
    "title": "JosteinTopland/jumpingjackson",
    "url": "https://github.com/JosteinTopland/jumpingjackson"
  }
]
```

## Research event notes

Personally screened GitHub and web results against the current catalogue, prior sources and decisions. Inspected pinned documentation and selected source; no independent builds, runs or byte comparisons. Game-specific retained machine runtimes are deferred for architecture review.
