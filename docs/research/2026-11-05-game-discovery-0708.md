# Retro game reconstruction discovery

Screen retro game research across BBC, UK101, Spectrum, C64, DOS and Windows; add seven projects and defer one architecture review.

Date: 2026-11-05 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- dmcr45-arendarvon-castle / Target CPU (no-evidence-found): No target CPU minimum established.
- dmcr45-arendarvon-castle / Runtime profiles (no-evidence-found): No independently verified complete runtime profile.
- ahope1-galactic-hitchhiker / Runtime profiles (no-evidence-found): No independently verified complete runtime profile.
- ahope1-galactic-hitchhiker / AI (no-evidence-found): No AI contribution established from inspected evidence; absence does not prove non-use.
- suborb-lemmings-z88 / Runtime profiles (no-evidence-found): No independently verified complete runtime profile.
- suborb-lemmings-z88 / AI (no-evidence-found): No AI contribution established from inspected evidence; absence does not prove non-use.
- wbovela-michaelplet / Target CPU (no-evidence-found): No target CPU minimum established.
- wbovela-michaelplet / Runtime profiles (no-evidence-found): No independently verified complete runtime profile.
- wbovela-michaelplet / AI (no-evidence-found): No AI contribution established from inspected evidence; absence does not prove non-use.
- filasfilas-f-mm1 / Target CPU (no-evidence-found): No target CPU minimum established.
- filasfilas-f-mm1 / Runtime profiles (no-evidence-found): No independently verified complete runtime profile.
- filasfilas-f-mm1 / AI (no-evidence-found): No AI contribution established from inspected evidence; absence does not prove non-use.
- diegoami-imperial-conquest-2 / Target CPU (no-evidence-found): No target CPU minimum established.
- diegoami-imperial-conquest-2 / Runtime profiles (no-evidence-found): No independently verified complete runtime profile.
- diegoami-imperial-conquest-2 / AI (no-evidence-found): No AI contribution established from inspected evidence; absence does not prove non-use.
- ajgbarnes-level9 / Target CPU (no-evidence-found): No target CPU minimum established.
- ajgbarnes-level9 / Runtime profiles (no-evidence-found): No independently verified complete runtime profile.
- ajgbarnes-level9 / AI (no-evidence-found): No AI contribution established from inspected evidence; absence does not prove non-use.

## The Secret of Arendarvon Castle — BBC adventure reconstruction

Project ID: dmcr45-arendarvon-castle · Overall audit: partial

### Typed catalogue values

```json
{
  "ai": {
    "evidence": [
      "Author explicitly credits Claude: https://github.com/dmcr45/arendarvon-castle/blob/06733d2b4f057322e3cbb8aa77ffd73daf5adb4d/README.md"
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
  "display_title": "The Secret of Arendarvon Castle — BBC adventure reconstruction",
  "id": "dmcr45-arendarvon-castle",
  "last_activity": null,
  "last_checked": "2026-11-05",
  "re_started": null,
  "reconstructed_languages": [
    "JavaScript"
  ],
  "record_class": "subject",
  "repo": "https://github.com/dmcr45/arendarvon-castle",
  "runtime_profiles": [],
  "source_cpu": [
    "6502"
  ],
  "source_language": [],
  "source_platforms": [
    "BBC Micro"
  ],
  "status": "Research and source inspected; no independent build or execution",
  "subjects": [
    "The Secret of Arendarvon Castle"
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
  "title": "The Secret of Arendarvon Castle — BBC adventure reconstruction",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "arendarvon-castle",
  "work_kinds": [
    "disassembly",
    "reimplementation"
  ]
}
```

### Identity (reviewed)

The Secret of Arendarvon Castle — BBC adventure reconstruction. Pinned repository material inspected.
- https://github.com/dmcr45/arendarvon-castle/blob/06733d2b4f057322e3cbb8aa77ffd73daf5adb4d/README.md
- https://github.com/dmcr45/arendarvon-castle/blob/06733d2b4f057322e3cbb8aa77ffd73daf5adb4d/arendarvon-engine.js

### Classification (reviewed)

Original ALADIN adventure bytecode translated into native JavaScript with traceable bytecode offsets. Author reports large differential comparisons against the patched original, and explicitly describes deliberate fixes; these tests were not independently repeated.
- https://github.com/dmcr45/arendarvon-castle/blob/06733d2b4f057322e3cbb8aa77ffd73daf5adb4d/README.md
- https://github.com/dmcr45/arendarvon-castle/blob/06733d2b4f057322e3cbb8aa77ffd73daf5adb4d/arendarvon-engine.js

### Source CPU (reviewed)

Source architectures follow the platforms explicitly examined; no exact variant inferred.
- https://github.com/dmcr45/arendarvon-castle/blob/06733d2b4f057322e3cbb8aa77ffd73daf5adb4d/README.md
- https://github.com/dmcr45/arendarvon-castle/blob/06733d2b4f057322e3cbb8aa77ffd73daf5adb4d/arendarvon-engine.js

### Target CPU (no-evidence-found)

No target CPU minimum established.
- https://github.com/dmcr45/arendarvon-castle/blob/06733d2b4f057322e3cbb8aa77ffd73daf5adb4d/README.md
- https://github.com/dmcr45/arendarvon-castle/blob/06733d2b4f057322e3cbb8aa77ffd73daf5adb4d/arendarvon-engine.js

### Build (reviewed)

Repository documents source or research and build procedures where applicable; no independent build, execution, or byte comparison.
- https://github.com/dmcr45/arendarvon-castle/blob/06733d2b4f057322e3cbb8aa77ffd73daf5adb4d/README.md
- https://github.com/dmcr45/arendarvon-castle/blob/06733d2b4f057322e3cbb8aa77ffd73daf5adb4d/arendarvon-engine.js

### Runtime profiles (no-evidence-found)

No independently verified complete runtime profile.
- https://github.com/dmcr45/arendarvon-castle/blob/06733d2b4f057322e3cbb8aa77ffd73daf5adb4d/README.md
- https://github.com/dmcr45/arendarvon-castle/blob/06733d2b4f057322e3cbb8aa77ffd73daf5adb4d/arendarvon-engine.js

### AI (reviewed)

The author credits Claude for code or research.
- https://github.com/dmcr45/arendarvon-castle/blob/06733d2b4f057322e3cbb8aa77ffd73daf5adb4d/README.md
- https://github.com/dmcr45/arendarvon-castle/blob/06733d2b4f057322e3cbb8aa77ffd73daf5adb4d/arendarvon-engine.js

### Relationships (reviewed)

Distinct research repository; related same-title work is not automatically treated as identical.
- https://github.com/dmcr45/arendarvon-castle/blob/06733d2b4f057322e3cbb8aa77ffd73daf5adb4d/README.md
- https://github.com/dmcr45/arendarvon-castle/blob/06733d2b4f057322e3cbb8aa77ffd73daf5adb4d/arendarvon-engine.js

## Galactic Hitchhiker — UK101 disassembly and BBC conversion

Project ID: ahope1-galactic-hitchhiker · Overall audit: partial

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
  "display_title": "Galactic Hitchhiker — UK101 disassembly and BBC conversion",
  "id": "ahope1-galactic-hitchhiker",
  "last_activity": null,
  "last_checked": "2026-11-05",
  "re_started": null,
  "reconstructed_languages": [
    "6502 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/ahope1/Galactic-Hitchhiker",
  "runtime_profiles": [],
  "source_cpu": [
    "6502"
  ],
  "source_language": [],
  "source_platforms": [
    "Compukit UK101"
  ],
  "status": "Research and source inspected; no independent build or execution",
  "subjects": [
    "Galactic Hitchhiker"
  ],
  "tags": [],
  "target_cpu": [
    "6502"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "BBC Micro"
  ],
  "techniques": [],
  "title": "Galactic Hitchhiker — UK101 disassembly and BBC conversion",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "Galactic-Hitchhiker",
  "work_kinds": [
    "disassembly",
    "reverse-engineering-derived-port"
  ]
}
```

### Identity (reviewed)

Galactic Hitchhiker — UK101 disassembly and BBC conversion. Pinned repository material inspected.
- https://github.com/ahope1/Galactic-Hitchhiker/blob/76d42b8f2921a4c38bb580a863fc26fce3c8edab/README.md
- https://github.com/ahope1/Galactic-Hitchhiker/blob/76d42b8f2921a4c38bb580a863fc26fce3c8edab/disassembly/README.md
- https://github.com/ahope1/Galactic-Hitchhiker/blob/76d42b8f2921a4c38bb580a863fc26fce3c8edab/beebify/README.md

### Classification (reviewed)

Annotated UK101 6502 disassembly and modified BBC Micro conversion. Author states the unmodified source reassembles identically to the original hex with binary includes; that claim and BBC execution were not independently tested.
- https://github.com/ahope1/Galactic-Hitchhiker/blob/76d42b8f2921a4c38bb580a863fc26fce3c8edab/README.md
- https://github.com/ahope1/Galactic-Hitchhiker/blob/76d42b8f2921a4c38bb580a863fc26fce3c8edab/disassembly/README.md
- https://github.com/ahope1/Galactic-Hitchhiker/blob/76d42b8f2921a4c38bb580a863fc26fce3c8edab/beebify/README.md

### Source CPU (reviewed)

Source architectures follow the platforms explicitly examined; no exact variant inferred.
- https://github.com/ahope1/Galactic-Hitchhiker/blob/76d42b8f2921a4c38bb580a863fc26fce3c8edab/README.md
- https://github.com/ahope1/Galactic-Hitchhiker/blob/76d42b8f2921a4c38bb580a863fc26fce3c8edab/disassembly/README.md
- https://github.com/ahope1/Galactic-Hitchhiker/blob/76d42b8f2921a4c38bb580a863fc26fce3c8edab/beebify/README.md

### Target CPU (reviewed)

BBC Micro uses a 6502.
- https://github.com/ahope1/Galactic-Hitchhiker/blob/76d42b8f2921a4c38bb580a863fc26fce3c8edab/README.md
- https://github.com/ahope1/Galactic-Hitchhiker/blob/76d42b8f2921a4c38bb580a863fc26fce3c8edab/disassembly/README.md
- https://github.com/ahope1/Galactic-Hitchhiker/blob/76d42b8f2921a4c38bb580a863fc26fce3c8edab/beebify/README.md

### Build (reviewed)

Repository documents source or research and build procedures where applicable; no independent build, execution, or byte comparison.
- https://github.com/ahope1/Galactic-Hitchhiker/blob/76d42b8f2921a4c38bb580a863fc26fce3c8edab/README.md
- https://github.com/ahope1/Galactic-Hitchhiker/blob/76d42b8f2921a4c38bb580a863fc26fce3c8edab/disassembly/README.md
- https://github.com/ahope1/Galactic-Hitchhiker/blob/76d42b8f2921a4c38bb580a863fc26fce3c8edab/beebify/README.md

### Runtime profiles (no-evidence-found)

No independently verified complete runtime profile.
- https://github.com/ahope1/Galactic-Hitchhiker/blob/76d42b8f2921a4c38bb580a863fc26fce3c8edab/README.md
- https://github.com/ahope1/Galactic-Hitchhiker/blob/76d42b8f2921a4c38bb580a863fc26fce3c8edab/disassembly/README.md
- https://github.com/ahope1/Galactic-Hitchhiker/blob/76d42b8f2921a4c38bb580a863fc26fce3c8edab/beebify/README.md

### AI (no-evidence-found)

No AI contribution established from inspected evidence; absence does not prove non-use.
- https://github.com/ahope1/Galactic-Hitchhiker/blob/76d42b8f2921a4c38bb580a863fc26fce3c8edab/README.md
- https://github.com/ahope1/Galactic-Hitchhiker/blob/76d42b8f2921a4c38bb580a863fc26fce3c8edab/disassembly/README.md
- https://github.com/ahope1/Galactic-Hitchhiker/blob/76d42b8f2921a4c38bb580a863fc26fce3c8edab/beebify/README.md

### Relationships (reviewed)

Distinct research repository; related same-title work is not automatically treated as identical.
- https://github.com/ahope1/Galactic-Hitchhiker/blob/76d42b8f2921a4c38bb580a863fc26fce3c8edab/README.md
- https://github.com/ahope1/Galactic-Hitchhiker/blob/76d42b8f2921a4c38bb580a863fc26fce3c8edab/disassembly/README.md
- https://github.com/ahope1/Galactic-Hitchhiker/blob/76d42b8f2921a4c38bb580a863fc26fce3c8edab/beebify/README.md

## Lemmings — Spectrum-derived Cambridge Z88 port

Project ID: suborb-lemmings-z88 · Overall audit: partial

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
  "display_title": "Lemmings — Spectrum-derived Cambridge Z88 port",
  "id": "suborb-lemmings-z88",
  "last_activity": null,
  "last_checked": "2026-11-05",
  "re_started": null,
  "reconstructed_languages": [
    "Z80 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/suborb/lemmings_z88",
  "runtime_profiles": [],
  "source_cpu": [
    "Z80"
  ],
  "source_language": [],
  "source_platforms": [
    "ZX Spectrum"
  ],
  "status": "Research and source inspected; no independent build or execution",
  "subjects": [
    "Lemmings"
  ],
  "tags": [],
  "target_cpu": [
    "Z80"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Cambridge Z88"
  ],
  "techniques": [],
  "title": "Lemmings — Spectrum-derived Cambridge Z88 port",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "lemmings_z88",
  "work_kinds": [
    "disassembly",
    "reverse-engineering-derived-port"
  ]
}
```

### Identity (reviewed)

Lemmings — Spectrum-derived Cambridge Z88 port. Pinned repository material inspected.
- https://github.com/suborb/lemmings_z88/blob/cc5f29545c4acd9c1fe96608575495f64b1e7278/README.md
- https://github.com/suborb/lemmings_z88/blob/cc5f29545c4acd9c1fe96608575495f64b1e7278/game.asm

### Classification (reviewed)

Historical Z88 port based on a disassembly of the Spectrum version. Source contains game code, build files and levels; README says it preserves circa-2000 source with changes for modern z88dk. No independent build or gameplay check.
- https://github.com/suborb/lemmings_z88/blob/cc5f29545c4acd9c1fe96608575495f64b1e7278/README.md
- https://github.com/suborb/lemmings_z88/blob/cc5f29545c4acd9c1fe96608575495f64b1e7278/game.asm

### Source CPU (reviewed)

Source architectures follow the platforms explicitly examined; no exact variant inferred.
- https://github.com/suborb/lemmings_z88/blob/cc5f29545c4acd9c1fe96608575495f64b1e7278/README.md
- https://github.com/suborb/lemmings_z88/blob/cc5f29545c4acd9c1fe96608575495f64b1e7278/game.asm

### Target CPU (reviewed)

Target is a Z80-based Cambridge Z88.
- https://github.com/suborb/lemmings_z88/blob/cc5f29545c4acd9c1fe96608575495f64b1e7278/README.md
- https://github.com/suborb/lemmings_z88/blob/cc5f29545c4acd9c1fe96608575495f64b1e7278/game.asm

### Build (reviewed)

Repository documents source or research and build procedures where applicable; no independent build, execution, or byte comparison.
- https://github.com/suborb/lemmings_z88/blob/cc5f29545c4acd9c1fe96608575495f64b1e7278/README.md
- https://github.com/suborb/lemmings_z88/blob/cc5f29545c4acd9c1fe96608575495f64b1e7278/game.asm

### Runtime profiles (no-evidence-found)

No independently verified complete runtime profile.
- https://github.com/suborb/lemmings_z88/blob/cc5f29545c4acd9c1fe96608575495f64b1e7278/README.md
- https://github.com/suborb/lemmings_z88/blob/cc5f29545c4acd9c1fe96608575495f64b1e7278/game.asm

### AI (no-evidence-found)

No AI contribution established from inspected evidence; absence does not prove non-use.
- https://github.com/suborb/lemmings_z88/blob/cc5f29545c4acd9c1fe96608575495f64b1e7278/README.md
- https://github.com/suborb/lemmings_z88/blob/cc5f29545c4acd9c1fe96608575495f64b1e7278/game.asm

### Relationships (reviewed)

Distinct research repository; related same-title work is not automatically treated as identical.
- https://github.com/suborb/lemmings_z88/blob/cc5f29545c4acd9c1fe96608575495f64b1e7278/README.md
- https://github.com/suborb/lemmings_z88/blob/cc5f29545c4acd9c1fe96608575495f64b1e7278/game.asm

## Michael Plet — C64 game disassembly archive

Project ID: wbovela-michaelplet · Overall audit: partial

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
  "display_title": "Michael Plet — C64 game disassembly archive",
  "id": "wbovela-michaelplet",
  "last_activity": null,
  "last_checked": "2026-11-05",
  "re_started": null,
  "reconstructed_languages": [
    "6502 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/wbovela/MichaelPlet",
  "runtime_profiles": [],
  "source_cpu": [
    "6502"
  ],
  "source_language": [],
  "source_platforms": [
    "C64"
  ],
  "status": "Research and source inspected; no independent build or execution",
  "subjects": [
    "Caverns of Khafka",
    "Dead Zone",
    "Doctor Who and the Mines of Terror"
  ],
  "tags": [],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [],
  "techniques": [],
  "title": "Michael Plet — C64 game disassembly archive",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "MichaelPlet",
  "work_kinds": [
    "disassembly",
    "data-format-analysis"
  ]
}
```

### Identity (reviewed)

Michael Plet — C64 game disassembly archive. Pinned repository material inspected.
- https://github.com/wbovela/MichaelPlet/blob/f8c66d8011848a321cf02111626127134d66e29d/README.md
- https://github.com/wbovela/MichaelPlet/blob/f8c66d8011848a321cf02111626127134d66e29d/Dead%20Zone%20v1/Findings.txt

### Classification (reviewed)

Repository-level collection preserving Michael Plet’s game disassemblies and analysis. Inspected Dead Zone notes identify maps, sprites and memory addresses; the collection includes other games and tools. Completeness and reassembly are not established.
- https://github.com/wbovela/MichaelPlet/blob/f8c66d8011848a321cf02111626127134d66e29d/README.md
- https://github.com/wbovela/MichaelPlet/blob/f8c66d8011848a321cf02111626127134d66e29d/Dead%20Zone%20v1/Findings.txt

### Source CPU (reviewed)

Source architectures follow the platforms explicitly examined; no exact variant inferred.
- https://github.com/wbovela/MichaelPlet/blob/f8c66d8011848a321cf02111626127134d66e29d/README.md
- https://github.com/wbovela/MichaelPlet/blob/f8c66d8011848a321cf02111626127134d66e29d/Dead%20Zone%20v1/Findings.txt

### Target CPU (no-evidence-found)

No target CPU minimum established.
- https://github.com/wbovela/MichaelPlet/blob/f8c66d8011848a321cf02111626127134d66e29d/README.md
- https://github.com/wbovela/MichaelPlet/blob/f8c66d8011848a321cf02111626127134d66e29d/Dead%20Zone%20v1/Findings.txt

### Build (reviewed)

Repository documents source or research and build procedures where applicable; no independent build, execution, or byte comparison.
- https://github.com/wbovela/MichaelPlet/blob/f8c66d8011848a321cf02111626127134d66e29d/README.md
- https://github.com/wbovela/MichaelPlet/blob/f8c66d8011848a321cf02111626127134d66e29d/Dead%20Zone%20v1/Findings.txt

### Runtime profiles (no-evidence-found)

No independently verified complete runtime profile.
- https://github.com/wbovela/MichaelPlet/blob/f8c66d8011848a321cf02111626127134d66e29d/README.md
- https://github.com/wbovela/MichaelPlet/blob/f8c66d8011848a321cf02111626127134d66e29d/Dead%20Zone%20v1/Findings.txt

### AI (no-evidence-found)

No AI contribution established from inspected evidence; absence does not prove non-use.
- https://github.com/wbovela/MichaelPlet/blob/f8c66d8011848a321cf02111626127134d66e29d/README.md
- https://github.com/wbovela/MichaelPlet/blob/f8c66d8011848a321cf02111626127134d66e29d/Dead%20Zone%20v1/Findings.txt

### Relationships (reviewed)

Distinct research repository; related same-title work is not automatically treated as identical.
- https://github.com/wbovela/MichaelPlet/blob/f8c66d8011848a321cf02111626127134d66e29d/README.md
- https://github.com/wbovela/MichaelPlet/blob/f8c66d8011848a321cf02111626127134d66e29d/Dead%20Zone%20v1/Findings.txt

## Might and Magic I — DOS format research and partial C++ remake

Project ID: filasfilas-f-mm1 · Overall audit: partial

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
  "display_title": "Might and Magic I — DOS format research and partial C++ remake",
  "id": "filasfilas-f-mm1",
  "last_activity": null,
  "last_checked": "2026-11-05",
  "re_started": null,
  "reconstructed_languages": [
    "C++"
  ],
  "record_class": "subject",
  "repo": "https://github.com/filasfilas/F-MM1",
  "runtime_profiles": [],
  "source_cpu": [
    "x86"
  ],
  "source_language": [],
  "source_platforms": [
    "DOS"
  ],
  "status": "Research and source inspected; no independent build or execution",
  "subjects": [
    "Might and Magic: Book One"
  ],
  "tags": [],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [],
  "techniques": [],
  "title": "Might and Magic I — DOS format research and partial C++ remake",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "F-MM1",
  "work_kinds": [
    "data-format-analysis",
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Might and Magic I — DOS format research and partial C++ remake. Pinned repository material inspected.
- https://github.com/filasfilas/F-MM1/blob/7074e062e7f0cccc3b7fa34c5be63f6a416e7f84/README.md
- https://github.com/filasfilas/F-MM1/blob/7074e062e7f0cccc3b7fa34c5be63f6a416e7f84/Docs/reverse%20engineering%20info/mazedata-file-struct.txt
- https://github.com/filasfilas/F-MM1/blob/7074e062e7f0cccc3b7fa34c5be63f6a416e7f84/model/maps/map.cpp

### Classification (reviewed)

Early SFML remake and DOS data-format research. The inspected map loader reads 55 original MAZEDATA records, while several maps remain unimplemented; README says it is not yet a playable game. No independent test.
- https://github.com/filasfilas/F-MM1/blob/7074e062e7f0cccc3b7fa34c5be63f6a416e7f84/README.md
- https://github.com/filasfilas/F-MM1/blob/7074e062e7f0cccc3b7fa34c5be63f6a416e7f84/Docs/reverse%20engineering%20info/mazedata-file-struct.txt
- https://github.com/filasfilas/F-MM1/blob/7074e062e7f0cccc3b7fa34c5be63f6a416e7f84/model/maps/map.cpp

### Source CPU (reviewed)

Source architectures follow the platforms explicitly examined; no exact variant inferred.
- https://github.com/filasfilas/F-MM1/blob/7074e062e7f0cccc3b7fa34c5be63f6a416e7f84/README.md
- https://github.com/filasfilas/F-MM1/blob/7074e062e7f0cccc3b7fa34c5be63f6a416e7f84/Docs/reverse%20engineering%20info/mazedata-file-struct.txt
- https://github.com/filasfilas/F-MM1/blob/7074e062e7f0cccc3b7fa34c5be63f6a416e7f84/model/maps/map.cpp

### Target CPU (no-evidence-found)

No target CPU minimum established.
- https://github.com/filasfilas/F-MM1/blob/7074e062e7f0cccc3b7fa34c5be63f6a416e7f84/README.md
- https://github.com/filasfilas/F-MM1/blob/7074e062e7f0cccc3b7fa34c5be63f6a416e7f84/Docs/reverse%20engineering%20info/mazedata-file-struct.txt
- https://github.com/filasfilas/F-MM1/blob/7074e062e7f0cccc3b7fa34c5be63f6a416e7f84/model/maps/map.cpp

### Build (reviewed)

Repository documents source or research and build procedures where applicable; no independent build, execution, or byte comparison.
- https://github.com/filasfilas/F-MM1/blob/7074e062e7f0cccc3b7fa34c5be63f6a416e7f84/README.md
- https://github.com/filasfilas/F-MM1/blob/7074e062e7f0cccc3b7fa34c5be63f6a416e7f84/Docs/reverse%20engineering%20info/mazedata-file-struct.txt
- https://github.com/filasfilas/F-MM1/blob/7074e062e7f0cccc3b7fa34c5be63f6a416e7f84/model/maps/map.cpp

### Runtime profiles (no-evidence-found)

No independently verified complete runtime profile.
- https://github.com/filasfilas/F-MM1/blob/7074e062e7f0cccc3b7fa34c5be63f6a416e7f84/README.md
- https://github.com/filasfilas/F-MM1/blob/7074e062e7f0cccc3b7fa34c5be63f6a416e7f84/Docs/reverse%20engineering%20info/mazedata-file-struct.txt
- https://github.com/filasfilas/F-MM1/blob/7074e062e7f0cccc3b7fa34c5be63f6a416e7f84/model/maps/map.cpp

### AI (no-evidence-found)

No AI contribution established from inspected evidence; absence does not prove non-use.
- https://github.com/filasfilas/F-MM1/blob/7074e062e7f0cccc3b7fa34c5be63f6a416e7f84/README.md
- https://github.com/filasfilas/F-MM1/blob/7074e062e7f0cccc3b7fa34c5be63f6a416e7f84/Docs/reverse%20engineering%20info/mazedata-file-struct.txt
- https://github.com/filasfilas/F-MM1/blob/7074e062e7f0cccc3b7fa34c5be63f6a416e7f84/model/maps/map.cpp

### Relationships (reviewed)

Distinct research repository; related same-title work is not automatically treated as identical.
- https://github.com/filasfilas/F-MM1/blob/7074e062e7f0cccc3b7fa34c5be63f6a416e7f84/README.md
- https://github.com/filasfilas/F-MM1/blob/7074e062e7f0cccc3b7fa34c5be63f6a416e7f84/Docs/reverse%20engineering%20info/mazedata-file-struct.txt
- https://github.com/filasfilas/F-MM1/blob/7074e062e7f0cccc3b7fa34c5be63f6a416e7f84/model/maps/map.cpp

## Imperial Conquest 2 — reimplementation and related research

Project ID: diegoami-imperial-conquest-2 · Overall audit: partial

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
  "display_title": "Imperial Conquest 2 — reimplementation and related research",
  "id": "diegoami-imperial-conquest-2",
  "last_activity": null,
  "last_checked": "2026-11-05",
  "re_started": null,
  "reconstructed_languages": [
    "C#"
  ],
  "record_class": "subject",
  "repo": "https://github.com/diegoami/imperial_conquest_2",
  "runtime_profiles": [],
  "source_cpu": [
    "x86"
  ],
  "source_language": [],
  "source_platforms": [
    "Windows"
  ],
  "status": "Research and source inspected; no independent build or execution",
  "subjects": [
    "Imperial Conquest 2"
  ],
  "tags": [],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Windows"
  ],
  "techniques": [],
  "title": "Imperial Conquest 2 — reimplementation and related research",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "imperial_conquest_2",
  "work_kinds": [
    "disassembly",
    "data-format-analysis",
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Imperial Conquest 2 — reimplementation and related research. Pinned repository material inspected.
- https://github.com/diegoami/imperial_conquest_2/blob/7883775498db79638f81656cc7c630faecec9109/README.md
- https://github.com/diegoami/imperial_conquest_2/blob/7883775498db79638f81656cc7c630faecec9109/src/IC2.Engine/Ai/AiCapitalDefence.cs
- https://github.com/diegoami/imperial-conquest-2-research/blob/2d6a496d1eb32b72129814316532247e98e36846/README.md

### Classification (reviewed)

C#/Godot strategy reimplementation paired with a separate research repository documenting the 1996 Win32 game’s formats and recovered rules. Inspected native strategy code cites an original routine and research report. Upstream describes both faithful and changed rulesets; original parity and playability were not independently established.
- https://github.com/diegoami/imperial_conquest_2/blob/7883775498db79638f81656cc7c630faecec9109/README.md
- https://github.com/diegoami/imperial_conquest_2/blob/7883775498db79638f81656cc7c630faecec9109/src/IC2.Engine/Ai/AiCapitalDefence.cs
- https://github.com/diegoami/imperial-conquest-2-research/blob/2d6a496d1eb32b72129814316532247e98e36846/README.md

### Source CPU (reviewed)

Source architectures follow the platforms explicitly examined; no exact variant inferred.
- https://github.com/diegoami/imperial_conquest_2/blob/7883775498db79638f81656cc7c630faecec9109/README.md
- https://github.com/diegoami/imperial_conquest_2/blob/7883775498db79638f81656cc7c630faecec9109/src/IC2.Engine/Ai/AiCapitalDefence.cs
- https://github.com/diegoami/imperial-conquest-2-research/blob/2d6a496d1eb32b72129814316532247e98e36846/README.md

### Target CPU (no-evidence-found)

No target CPU minimum established.
- https://github.com/diegoami/imperial_conquest_2/blob/7883775498db79638f81656cc7c630faecec9109/README.md
- https://github.com/diegoami/imperial_conquest_2/blob/7883775498db79638f81656cc7c630faecec9109/src/IC2.Engine/Ai/AiCapitalDefence.cs
- https://github.com/diegoami/imperial-conquest-2-research/blob/2d6a496d1eb32b72129814316532247e98e36846/README.md

### Build (reviewed)

Repository documents source or research and build procedures where applicable; no independent build, execution, or byte comparison.
- https://github.com/diegoami/imperial_conquest_2/blob/7883775498db79638f81656cc7c630faecec9109/README.md
- https://github.com/diegoami/imperial_conquest_2/blob/7883775498db79638f81656cc7c630faecec9109/src/IC2.Engine/Ai/AiCapitalDefence.cs
- https://github.com/diegoami/imperial-conquest-2-research/blob/2d6a496d1eb32b72129814316532247e98e36846/README.md

### Runtime profiles (no-evidence-found)

No independently verified complete runtime profile.
- https://github.com/diegoami/imperial_conquest_2/blob/7883775498db79638f81656cc7c630faecec9109/README.md
- https://github.com/diegoami/imperial_conquest_2/blob/7883775498db79638f81656cc7c630faecec9109/src/IC2.Engine/Ai/AiCapitalDefence.cs
- https://github.com/diegoami/imperial-conquest-2-research/blob/2d6a496d1eb32b72129814316532247e98e36846/README.md

### AI (no-evidence-found)

No AI contribution established from inspected evidence; absence does not prove non-use.
- https://github.com/diegoami/imperial_conquest_2/blob/7883775498db79638f81656cc7c630faecec9109/README.md
- https://github.com/diegoami/imperial_conquest_2/blob/7883775498db79638f81656cc7c630faecec9109/src/IC2.Engine/Ai/AiCapitalDefence.cs
- https://github.com/diegoami/imperial-conquest-2-research/blob/2d6a496d1eb32b72129814316532247e98e36846/README.md

### Relationships (reviewed)

Distinct research repository; related same-title work is not automatically treated as identical.
- https://github.com/diegoami/imperial_conquest_2/blob/7883775498db79638f81656cc7c630faecec9109/README.md
- https://github.com/diegoami/imperial_conquest_2/blob/7883775498db79638f81656cc7c630faecec9109/src/IC2.Engine/Ai/AiCapitalDefence.cs
- https://github.com/diegoami/imperial-conquest-2-research/blob/2d6a496d1eb32b72129814316532247e98e36846/README.md

## Level 9 — Python interpreter and adventure bytecode research

Project ID: ajgbarnes-level9 · Overall audit: partial

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
  "display_title": "Level 9 — Python interpreter and adventure bytecode research",
  "id": "ajgbarnes-level9",
  "last_activity": null,
  "last_checked": "2026-11-05",
  "re_started": null,
  "reconstructed_languages": [
    "Python"
  ],
  "record_class": "hybrid",
  "repo": "https://github.com/ajgbarnes/level9",
  "runtime_profiles": [],
  "source_cpu": [
    "6502",
    "Z80"
  ],
  "source_language": [],
  "source_platforms": [
    "BBC Micro",
    "ZX Spectrum"
  ],
  "status": "Research and source inspected; no independent build or execution",
  "subjects": [
    "Colossal Adventure",
    "Adventure Quest",
    "Dungeon Adventure",
    "Lords of Time",
    "Snowball"
  ],
  "tags": [],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [],
  "techniques": [],
  "title": "Level 9 — Python interpreter and adventure bytecode research",
  "tool_kinds": [
    "disassembler"
  ],
  "types": [
    "subject",
    "tool"
  ],
  "upstream_name": "level9",
  "work_kinds": [
    "data-format-analysis",
    "disassembly",
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Level 9 — Python interpreter and adventure bytecode research. Pinned repository material inspected.
- https://github.com/ajgbarnes/level9/blob/35522eea68062433b4014e49d008b2112e78eaaf/README.md
- https://github.com/ajgbarnes/level9/blob/35522eea68062433b4014e49d008b2112e78eaaf/decompiler.py

### Classification (reviewed)

Python A-Code tools and interpreter with annotated game bytecode decompilations, data extractors and a v1 format specification. README reports broad v1 support and nascent v2 support; inspected decoder implements opcode listing. No independent game or extraction test.
- https://github.com/ajgbarnes/level9/blob/35522eea68062433b4014e49d008b2112e78eaaf/README.md
- https://github.com/ajgbarnes/level9/blob/35522eea68062433b4014e49d008b2112e78eaaf/decompiler.py

### Source CPU (reviewed)

Source architectures follow the platforms explicitly examined; no exact variant inferred.
- https://github.com/ajgbarnes/level9/blob/35522eea68062433b4014e49d008b2112e78eaaf/README.md
- https://github.com/ajgbarnes/level9/blob/35522eea68062433b4014e49d008b2112e78eaaf/decompiler.py

### Target CPU (no-evidence-found)

No target CPU minimum established.
- https://github.com/ajgbarnes/level9/blob/35522eea68062433b4014e49d008b2112e78eaaf/README.md
- https://github.com/ajgbarnes/level9/blob/35522eea68062433b4014e49d008b2112e78eaaf/decompiler.py

### Build (reviewed)

Repository documents source or research and build procedures where applicable; no independent build, execution, or byte comparison.
- https://github.com/ajgbarnes/level9/blob/35522eea68062433b4014e49d008b2112e78eaaf/README.md
- https://github.com/ajgbarnes/level9/blob/35522eea68062433b4014e49d008b2112e78eaaf/decompiler.py

### Runtime profiles (no-evidence-found)

No independently verified complete runtime profile.
- https://github.com/ajgbarnes/level9/blob/35522eea68062433b4014e49d008b2112e78eaaf/README.md
- https://github.com/ajgbarnes/level9/blob/35522eea68062433b4014e49d008b2112e78eaaf/decompiler.py

### AI (no-evidence-found)

No AI contribution established from inspected evidence; absence does not prove non-use.
- https://github.com/ajgbarnes/level9/blob/35522eea68062433b4014e49d008b2112e78eaaf/README.md
- https://github.com/ajgbarnes/level9/blob/35522eea68062433b4014e49d008b2112e78eaaf/decompiler.py

### Relationships (reviewed)

Distinct research repository; related same-title work is not automatically treated as identical.
- https://github.com/ajgbarnes/level9/blob/35522eea68062433b4014e49d008b2112e78eaaf/README.md
- https://github.com/ajgbarnes/level9/blob/35522eea68062433b4014e49d008b2112e78eaaf/decompiler.py

## Pinned evidence manifest

- ahope1-galactic-hitchhiker-beebify-readme-md: https://github.com/ahope1/galactic-hitchhiker/blob/76d42b8f2921a4c38bb580a863fc26fce3c8edab/beebify/README.md (Git blob a028d80f1276047a773917488701a44250805e8c)
- ahope1-galactic-hitchhiker-disassembly-readme-md: https://github.com/ahope1/galactic-hitchhiker/blob/76d42b8f2921a4c38bb580a863fc26fce3c8edab/disassembly/README.md (Git blob 51ebf2615982f699b12595619cdeff3371c4f25a)
- ahope1-galactic-hitchhiker-readme-md: https://github.com/ahope1/galactic-hitchhiker/blob/76d42b8f2921a4c38bb580a863fc26fce3c8edab/README.md (Git blob 758ff67db332de76c793f8fdb29593bc9da95266)
- ajgbarnes-level9-decompiler-py: https://github.com/ajgbarnes/level9/blob/35522eea68062433b4014e49d008b2112e78eaaf/decompiler.py (Git blob 93e0e283250b8659b930bbbc3340f4f6e4ebb0b3)
- ajgbarnes-level9-readme-md: https://github.com/ajgbarnes/level9/blob/35522eea68062433b4014e49d008b2112e78eaaf/README.md (Git blob b502994ec7c8ffe42eab19e24cd13e50070c26ed)
- diegoami-imperial-conquest-2-readme-md: https://github.com/diegoami/imperial_conquest_2/blob/7883775498db79638f81656cc7c630faecec9109/README.md (Git blob acf55bfe489c10397841f2ab545e277d6db03de0)
- diegoami-imperial-conquest-2-research-readme-md: https://github.com/diegoami/imperial-conquest-2-research/blob/2d6a496d1eb32b72129814316532247e98e36846/README.md (Git blob 75eaf34ca7edf7b8c0bd477481b4fd057ba43c0f)
- diegoami-imperial-conquest-2-src-ic2-engine-ai-aicapitaldefence-cs: https://github.com/diegoami/imperial_conquest_2/blob/7883775498db79638f81656cc7c630faecec9109/src/IC2.Engine/Ai/AiCapitalDefence.cs (Git blob 1813cb1f363e4a5545d2576e50ff683bcc143904)
- dmcr45-arendarvon-castle-arendarvon-engine-js: https://github.com/dmcr45/arendarvon-castle/blob/06733d2b4f057322e3cbb8aa77ffd73daf5adb4d/arendarvon-engine.js (Git blob 41cc2449e68fae418727796d69bd7c1ba1b33028)
- dmcr45-arendarvon-castle-readme-md: https://github.com/dmcr45/arendarvon-castle/blob/06733d2b4f057322e3cbb8aa77ffd73daf5adb4d/README.md (Git blob ac2d4a5a92579aef1d9c590a87dc9a951645785d)
- filasfilas-f-mm1-docs-reverse-engineering-info-mazedata-file-struct-txt: https://github.com/filasfilas/f-mm1/blob/7074e062e7f0cccc3b7fa34c5be63f6a416e7f84/Docs/reverse%20engineering%20info/mazedata-file-struct.txt (Git blob 948c30aec91e6200f8e1ac47b9f734e8b3f63ab9)
- filasfilas-f-mm1-model-maps-map-cpp: https://github.com/filasfilas/f-mm1/blob/7074e062e7f0cccc3b7fa34c5be63f6a416e7f84/model/maps/map.cpp (Git blob 0b1b39bf8e86b76de58eb30b8449b44393ca6702)
- filasfilas-f-mm1-readme-md: https://github.com/filasfilas/f-mm1/blob/7074e062e7f0cccc3b7fa34c5be63f6a416e7f84/README.md (Git blob 57232883a2f9afa29a48c790d534b609356d60cb)
- hyperbog-rloft-code1-code1-cpp: https://github.com/hyperbog/rloft/blob/2d73a40006541bbed56f352e60e806c0a111e070/Code1/Code1.cpp (Git blob 85a25d5298d6b88314fd571985f15cf8b7be0af5)
- hyperbog-rloft-code1-readme-md: https://github.com/hyperbog/rloft/blob/2d73a40006541bbed56f352e60e806c0a111e070/Code1/README.md (Git blob 01cf94a32ed22226ff3702ec1660ff856bbb1f92)
- hyperbog-rloft-readme-md: https://github.com/hyperbog/rloft/blob/2d73a40006541bbed56f352e60e806c0a111e070/README.md (Git blob 513a133f139af3d379909ff7cd6b0558556ce30f)
- suborb-lemmings-z88-game-asm: https://github.com/suborb/lemmings_z88/blob/cc5f29545c4acd9c1fe96608575495f64b1e7278/game.asm (Git blob 03d2131295973149c1516836fb80bc3bf8e09bc0)
- suborb-lemmings-z88-readme-md: https://github.com/suborb/lemmings_z88/blob/cc5f29545c4acd9c1fe96608575495f64b1e7278/README.md (Git blob 7dcaeb50429af013bc4d37f7a34f5447bd7295a7)
- wbovela-michaelplet-dead-zone-v1-findings-txt: https://github.com/wbovela/michaelplet/blob/f8c66d8011848a321cf02111626127134d66e29d/Dead%20Zone%20v1/Findings.txt (Git blob c95cc3e56fdaa0482bbc493be2bd6429fc16f493)
- wbovela-michaelplet-readme-md: https://github.com/wbovela/michaelplet/blob/f8c66d8011848a321cf02111626127134d66e29d/README.md (Git blob 24ad870fa9218799dc67fa1259a7dbfe462efdc9)

## Sources

```json
[
  {
    "first_indexed": "2026-11-05",
    "id": "github-dmcr45-arendarvon-castle",
    "kind": "github-repository",
    "last_reviewed": "2026-11-05",
    "open_task_ids": [],
    "projects_promoted": [
      "dmcr45-arendarvon-castle"
    ],
    "reason": "Original ALADIN adventure bytecode translated into native JavaScript with traceable bytecode offsets. Author reports large differential comparisons against the patched original, and explicitly describes deliberate fixes; these tests were not independently repeated.",
    "review_state": "partial",
    "source": "https://github.com/dmcr45/arendarvon-castle"
  },
  {
    "first_indexed": "2026-11-05",
    "id": "github-ahope1-galactic-hitchhiker",
    "kind": "github-repository",
    "last_reviewed": "2026-11-05",
    "open_task_ids": [],
    "projects_promoted": [
      "ahope1-galactic-hitchhiker"
    ],
    "reason": "Annotated UK101 6502 disassembly and modified BBC Micro conversion. Author states the unmodified source reassembles identically to the original hex with binary includes; that claim and BBC execution were not independently tested.",
    "review_state": "partial",
    "source": "https://github.com/ahope1/Galactic-Hitchhiker"
  },
  {
    "first_indexed": "2026-11-05",
    "id": "github-suborb-lemmings-z88",
    "kind": "github-repository",
    "last_reviewed": "2026-11-05",
    "open_task_ids": [],
    "projects_promoted": [
      "suborb-lemmings-z88"
    ],
    "reason": "Historical Z88 port based on a disassembly of the Spectrum version. Source contains game code, build files and levels; README says it preserves circa-2000 source with changes for modern z88dk. No independent build or gameplay check.",
    "review_state": "partial",
    "source": "https://github.com/suborb/lemmings_z88"
  },
  {
    "first_indexed": "2026-11-05",
    "id": "github-wbovela-michaelplet",
    "kind": "github-repository",
    "last_reviewed": "2026-11-05",
    "open_task_ids": [],
    "projects_promoted": [
      "wbovela-michaelplet"
    ],
    "reason": "Repository-level collection preserving Michael Plet’s game disassemblies and analysis. Inspected Dead Zone notes identify maps, sprites and memory addresses; the collection includes other games and tools. Completeness and reassembly are not established.",
    "review_state": "partial",
    "source": "https://github.com/wbovela/MichaelPlet"
  },
  {
    "first_indexed": "2026-11-05",
    "id": "github-filasfilas-f-mm1",
    "kind": "github-repository",
    "last_reviewed": "2026-11-05",
    "open_task_ids": [],
    "projects_promoted": [
      "filasfilas-f-mm1"
    ],
    "reason": "Early SFML remake and DOS data-format research. The inspected map loader reads 55 original MAZEDATA records, while several maps remain unimplemented; README says it is not yet a playable game. No independent test.",
    "review_state": "partial",
    "source": "https://github.com/filasfilas/F-MM1"
  },
  {
    "first_indexed": "2026-11-05",
    "id": "github-diegoami-imperial-conquest-2",
    "kind": "github-repository",
    "last_reviewed": "2026-11-05",
    "open_task_ids": [],
    "projects_promoted": [
      "diegoami-imperial-conquest-2"
    ],
    "reason": "C#/Godot strategy reimplementation paired with a separate research repository documenting the 1996 Win32 game’s formats and recovered rules. Inspected native strategy code cites an original routine and research report. Upstream describes both faithful and changed rulesets; original parity and playability were not independently established.",
    "review_state": "partial",
    "source": "https://github.com/diegoami/imperial_conquest_2"
  },
  {
    "first_indexed": "2026-11-05",
    "id": "github-diegoami-imperial-conquest-2-research",
    "kind": "github-repository",
    "last_reviewed": "2026-11-05",
    "open_task_ids": [],
    "projects_promoted": [
      "diegoami-imperial-conquest-2"
    ],
    "reason": "Separate research repository for this same reimplementation.",
    "review_state": "partial",
    "source": "https://github.com/diegoami/imperial-conquest-2-research"
  },
  {
    "first_indexed": "2026-11-05",
    "id": "github-ajgbarnes-level9",
    "kind": "github-repository",
    "last_reviewed": "2026-11-05",
    "open_task_ids": [],
    "projects_promoted": [
      "ajgbarnes-level9"
    ],
    "reason": "Python A-Code tools and interpreter with annotated game bytecode decompilations, data extractors and a v1 format specification. README reports broad v1 support and nascent v2 support; inspected decoder implements opcode listing. No independent game or extraction test.",
    "review_state": "partial",
    "source": "https://github.com/ajgbarnes/level9"
  },
  {
    "first_indexed": "2026-11-05",
    "id": "github-hyperbog-rloft",
    "kind": "github-repository",
    "last_reviewed": "2026-11-05",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Ravenloft C++ source is substantial but represents explicit x86 register and machine state; its execution architecture needs review against the game-specific BAKED EMULATION boundary. Repository itself distinguishes byte accounting from semantic parity and a finished player-facing game.",
    "review_state": "partial",
    "source": "https://github.com/Hyperbog/RLOFT"
  }
]
```

## Decisions

```json
[
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/Hyperbog/RLOFT/blob/2d73a40006541bbed56f352e60e806c0a111e070/README.md",
      "https://github.com/Hyperbog/RLOFT/blob/2d73a40006541bbed56f352e60e806c0a111e070/Code1/README.md",
      "https://github.com/Hyperbog/RLOFT/blob/2d73a40006541bbed56f352e60e806c0a111e070/Code1/Code1.cpp"
    ],
    "id": "pass119-hyperbog-rloft",
    "project_ids": [],
    "reason": "Ravenloft C++ source is substantial but represents explicit x86 register and machine state; its execution architecture needs review against the game-specific BAKED EMULATION boundary. Repository itself distinguishes byte accounting from semantic parity and a finished player-facing game.",
    "reviewed_at": "2026-11-05",
    "source_ids": [
      "github-hyperbog-rloft"
    ],
    "title": "Hyperbog/RLOFT",
    "url": "https://github.com/Hyperbog/RLOFT"
  }
]
```

## Research event notes

Personally screened repository search and primary source against the current catalogue and prior decisions. Inspected pinned documentation and selected code. No independent builds, gameplay or byte comparisons. Game-specific CPU execution leads deferred for the existing BAKED EMULATION audit.
