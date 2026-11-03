# Classic platform reconstruction discovery

Review 43 candidate repositories: add 8 projects and record four deferrals.

Date: 2026-11-03 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- akustikrausch-protracker4 / Runtime profiles (no-evidence-found): Documented dependencies and bounds are recorded in build notes; no independently verified complete runtime profile.
- akustikrausch-protracker4 / AI (no-evidence-found): No actual development-AI contribution established in the inspected evidence. Missing attribution is not evidence of non-use.
- markyturtle-stunt-car-racer-amiga / Runtime profiles (no-evidence-found): Documented dependencies and bounds are recorded in build notes; no independently verified complete runtime profile.
- neozeed-qlfrontier / Runtime profiles (no-evidence-found): Documented dependencies and bounds are recorded in build notes; no independently verified complete runtime profile.
- neozeed-qlfrontier / AI (no-evidence-found): No actual development-AI contribution established in the inspected evidence. Missing attribution is not evidence of non-use.
- cambrianminds-the-pack-rat / Target CPU (no-evidence-found): No physical target CPU minimum established; portability or a managed runtime is not a hardware requirement.
- cambrianminds-the-pack-rat / Runtime profiles (no-evidence-found): Documented dependencies and bounds are recorded in build notes; no independently verified complete runtime profile.
- cambrianminds-the-pack-rat / AI (no-evidence-found): No actual development-AI contribution established in the inspected evidence. Missing attribution is not evidence of non-use.
- johnshawler-bump-n-jump-amiga / Runtime profiles (no-evidence-found): Documented dependencies and bounds are recorded in build notes; no independently verified complete runtime profile.
- johnshawler-bump-n-jump-amiga / AI (no-evidence-found): No actual development-AI contribution established in the inspected evidence. Missing attribution is not evidence of non-use.
- johnshawler-do-run-run-amiga / Runtime profiles (no-evidence-found): Documented dependencies and bounds are recorded in build notes; no independently verified complete runtime profile.
- johnshawler-do-run-run-amiga / AI (no-evidence-found): No actual development-AI contribution established in the inspected evidence. Missing attribution is not evidence of non-use.
- johnshawler-skate-or-die-dx-amiga / Runtime profiles (no-evidence-found): Documented dependencies and bounds are recorded in build notes; no independently verified complete runtime profile.
- johnshawler-skate-or-die-dx-amiga / AI (no-evidence-found): No actual development-AI contribution established in the inspected evidence. Missing attribution is not evidence of non-use.
- seamuswaldron-atic-atac / Target CPU (no-evidence-found): No physical target CPU minimum established; portability or a managed runtime is not a hardware requirement.
- seamuswaldron-atic-atac / Runtime profiles (no-evidence-found): Documented dependencies and bounds are recorded in build notes; no independently verified complete runtime profile.

## ProTracker 4.1 — Amiga music tracker

Project ID: akustikrausch-protracker4 · Overall audit: partial

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
  "display_title": "ProTracker 4.1 — Amiga music tracker",
  "id": "akustikrausch-protracker4",
  "last_activity": null,
  "last_checked": "2026-11-03",
  "re_started": null,
  "reconstructed_languages": [
    "68000 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/akustikrausch/protracker4",
  "runtime_profiles": [],
  "source_cpu": [
    "68000"
  ],
  "source_language": [
    "68000 assembly"
  ],
  "source_platforms": [
    "Amiga"
  ],
  "status": "Source inspected; no independent build or execution",
  "subjects": [
    "ProTracker 4.1"
  ],
  "tags": [],
  "target_cpu": [
    "68000"
  ],
  "target_kinds": [
    "application"
  ],
  "target_platforms": [
    "Amiga"
  ],
  "techniques": [],
  "title": "ProTracker 4.1 — Amiga music tracker",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "protracker4",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

ProTracker 4.1 — Amiga music tracker. Pinned repository, documentation and selected implementation inspected.
- https://github.com/akustikrausch/protracker4/blob/e33274565026d9348f326e4b4e75503ff6c2b585/README.md
- https://github.com/akustikrausch/protracker4/blob/e33274565026d9348f326e4b4e75503ff6c2b585/Protracker.asm
- https://github.com/akustikrausch/protracker4/blob/e33274565026d9348f326e4b4e75503ff6c2b585/Makefile
- https://github.com/akustikrausch/protracker4/blob/e33274565026d9348f326e4b4e75503ff6c2b585/src/engine/efx8.asm
- https://github.com/akustikrausch/protracker4/blob/e33274565026d9348f326e4b4e75503ff6c2b585/src/sys/ahi.asm

### Classification (reviewed)

Modern continuation of the released ProTracker 4 source, with 4/8-channel tracker editing, RTG screens and AHI audio. This is a source-based continuation, not a claimed disassembly or byte-exact original reconstruction.
- https://github.com/akustikrausch/protracker4/blob/e33274565026d9348f326e4b4e75503ff6c2b585/README.md
- https://github.com/akustikrausch/protracker4/blob/e33274565026d9348f326e4b4e75503ff6c2b585/Protracker.asm
- https://github.com/akustikrausch/protracker4/blob/e33274565026d9348f326e4b4e75503ff6c2b585/Makefile
- https://github.com/akustikrausch/protracker4/blob/e33274565026d9348f326e4b4e75503ff6c2b585/src/engine/efx8.asm
- https://github.com/akustikrausch/protracker4/blob/e33274565026d9348f326e4b4e75503ff6c2b585/src/sys/ahi.asm

### Source CPU (reviewed)

Source architecture: 68000. No minimum CPU inferred.
- https://github.com/akustikrausch/protracker4/blob/e33274565026d9348f326e4b4e75503ff6c2b585/README.md
- https://github.com/akustikrausch/protracker4/blob/e33274565026d9348f326e4b4e75503ff6c2b585/Protracker.asm
- https://github.com/akustikrausch/protracker4/blob/e33274565026d9348f326e4b4e75503ff6c2b585/Makefile
- https://github.com/akustikrausch/protracker4/blob/e33274565026d9348f326e4b4e75503ff6c2b585/src/engine/efx8.asm
- https://github.com/akustikrausch/protracker4/blob/e33274565026d9348f326e4b4e75503ff6c2b585/src/sys/ahi.asm

### Target CPU (reviewed)

Target architecture: 68000. This is not a verified minimum CPU for every frontend.
- https://github.com/akustikrausch/protracker4/blob/e33274565026d9348f326e4b4e75503ff6c2b585/README.md
- https://github.com/akustikrausch/protracker4/blob/e33274565026d9348f326e4b4e75503ff6c2b585/Protracker.asm
- https://github.com/akustikrausch/protracker4/blob/e33274565026d9348f326e4b4e75503ff6c2b585/Makefile
- https://github.com/akustikrausch/protracker4/blob/e33274565026d9348f326e4b4e75503ff6c2b585/src/engine/efx8.asm
- https://github.com/akustikrausch/protracker4/blob/e33274565026d9348f326e4b4e75503ff6c2b585/src/sys/ahi.asm

### Build (reviewed)

README specifies vasm, Amiga 68000–68060, Kickstart 2.04+ and 1 MB. Source is split into playback, UI, I/O and system modules. No independent build or playback test. Source-only review: no independent compilation, execution, gameplay or byte comparison.
- https://github.com/akustikrausch/protracker4/blob/e33274565026d9348f326e4b4e75503ff6c2b585/README.md
- https://github.com/akustikrausch/protracker4/blob/e33274565026d9348f326e4b4e75503ff6c2b585/Protracker.asm
- https://github.com/akustikrausch/protracker4/blob/e33274565026d9348f326e4b4e75503ff6c2b585/Makefile
- https://github.com/akustikrausch/protracker4/blob/e33274565026d9348f326e4b4e75503ff6c2b585/src/engine/efx8.asm
- https://github.com/akustikrausch/protracker4/blob/e33274565026d9348f326e4b4e75503ff6c2b585/src/sys/ahi.asm

### Runtime profiles (no-evidence-found)

Documented dependencies and bounds are recorded in build notes; no independently verified complete runtime profile.
- https://github.com/akustikrausch/protracker4/blob/e33274565026d9348f326e4b4e75503ff6c2b585/README.md
- https://github.com/akustikrausch/protracker4/blob/e33274565026d9348f326e4b4e75503ff6c2b585/Protracker.asm
- https://github.com/akustikrausch/protracker4/blob/e33274565026d9348f326e4b4e75503ff6c2b585/Makefile
- https://github.com/akustikrausch/protracker4/blob/e33274565026d9348f326e4b4e75503ff6c2b585/src/engine/efx8.asm
- https://github.com/akustikrausch/protracker4/blob/e33274565026d9348f326e4b4e75503ff6c2b585/src/sys/ahi.asm

### AI (no-evidence-found)

No actual development-AI contribution established in the inspected evidence. Missing attribution is not evidence of non-use.
- https://github.com/akustikrausch/protracker4/blob/e33274565026d9348f326e4b4e75503ff6c2b585/README.md
- https://github.com/akustikrausch/protracker4/blob/e33274565026d9348f326e4b4e75503ff6c2b585/Protracker.asm
- https://github.com/akustikrausch/protracker4/blob/e33274565026d9348f326e4b4e75503ff6c2b585/Makefile
- https://github.com/akustikrausch/protracker4/blob/e33274565026d9348f326e4b4e75503ff6c2b585/src/engine/efx8.asm
- https://github.com/akustikrausch/protracker4/blob/e33274565026d9348f326e4b4e75503ff6c2b585/src/sys/ahi.asm

### Relationships (reviewed)

Based on original ProTracker 4 beta source released by Tom Beyer and earlier 3.15 lineage; credit condition and noncommercial licence stated in repository.
- https://github.com/akustikrausch/protracker4/blob/e33274565026d9348f326e4b4e75503ff6c2b585/README.md
- https://github.com/akustikrausch/protracker4/blob/e33274565026d9348f326e4b4e75503ff6c2b585/Protracker.asm
- https://github.com/akustikrausch/protracker4/blob/e33274565026d9348f326e4b4e75503ff6c2b585/Makefile
- https://github.com/akustikrausch/protracker4/blob/e33274565026d9348f326e4b4e75503ff6c2b585/src/engine/efx8.asm
- https://github.com/akustikrausch/protracker4/blob/e33274565026d9348f326e4b4e75503ff6c2b585/src/sys/ahi.asm

## Stunt Car Racer — Amiga Turbo disassembly

Project ID: markyturtle-stunt-car-racer-amiga · Overall audit: partial

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
  "display_title": "Stunt Car Racer — Amiga Turbo disassembly",
  "id": "markyturtle-stunt-car-racer-amiga",
  "last_activity": null,
  "last_checked": "2026-11-03",
  "re_started": null,
  "reconstructed_languages": [
    "68000 assembly",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/MarkyTurtle/Stunt-Car-Racer---Amiga",
  "runtime_profiles": [],
  "source_cpu": [
    "68000"
  ],
  "source_language": [
    "68000 assembly",
    "Python"
  ],
  "source_platforms": [
    "Amiga"
  ],
  "status": "Source inspected; no independent build or execution",
  "subjects": [
    "Stunt Car Racer"
  ],
  "tags": [],
  "target_cpu": [
    "68000"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Amiga"
  ],
  "techniques": [],
  "title": "Stunt Car Racer — Amiga Turbo disassembly",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "Stunt-Car-Racer---Amiga",
  "work_kinds": [
    "disassembly",
    "source-reconstruction",
    "patching"
  ]
}
```

### Identity (reviewed)

Stunt Car Racer — Amiga Turbo disassembly. Pinned repository, documentation and selected implementation inspected.
- https://github.com/MarkyTurtle/Stunt-Car-Racer---Amiga/blob/4d5ef1d7fd6cf2065cdc7210c4691b62362ecdd5/README.md
- https://github.com/MarkyTurtle/Stunt-Car-Racer---Amiga/blob/4d5ef1d7fd6cf2065cdc7210c4691b62362ecdd5/BUILDING.md
- https://github.com/MarkyTurtle/Stunt-Car-Racer---Amiga/blob/4d5ef1d7fd6cf2065cdc7210c4691b62362ecdd5/original/README.md
- https://github.com/MarkyTurtle/Stunt-Car-Racer---Amiga/blob/4d5ef1d7fd6cf2065cdc7210c4691b62362ecdd5/original/docs/CODE.md
- https://github.com/MarkyTurtle/Stunt-Car-Racer---Amiga/blob/4d5ef1d7fd6cf2065cdc7210c4691b62362ecdd5/original/scr_boot.s

### Classification (reviewed)

Disassembled game, bootblock and loader from the Galahad Turbo release, with separately maintained enhanced AmigaDOS disk. Author claims original parts reassemble byte-identically to that release, not necessarily the untouched retail version.
- https://github.com/MarkyTurtle/Stunt-Car-Racer---Amiga/blob/4d5ef1d7fd6cf2065cdc7210c4691b62362ecdd5/README.md
- https://github.com/MarkyTurtle/Stunt-Car-Racer---Amiga/blob/4d5ef1d7fd6cf2065cdc7210c4691b62362ecdd5/BUILDING.md
- https://github.com/MarkyTurtle/Stunt-Car-Racer---Amiga/blob/4d5ef1d7fd6cf2065cdc7210c4691b62362ecdd5/original/README.md
- https://github.com/MarkyTurtle/Stunt-Car-Racer---Amiga/blob/4d5ef1d7fd6cf2065cdc7210c4691b62362ecdd5/original/docs/CODE.md
- https://github.com/MarkyTurtle/Stunt-Car-Racer---Amiga/blob/4d5ef1d7fd6cf2065cdc7210c4691b62362ecdd5/original/scr_boot.s

### Source CPU (reviewed)

Source architecture: 68000. No minimum CPU inferred.
- https://github.com/MarkyTurtle/Stunt-Car-Racer---Amiga/blob/4d5ef1d7fd6cf2065cdc7210c4691b62362ecdd5/README.md
- https://github.com/MarkyTurtle/Stunt-Car-Racer---Amiga/blob/4d5ef1d7fd6cf2065cdc7210c4691b62362ecdd5/BUILDING.md
- https://github.com/MarkyTurtle/Stunt-Car-Racer---Amiga/blob/4d5ef1d7fd6cf2065cdc7210c4691b62362ecdd5/original/README.md
- https://github.com/MarkyTurtle/Stunt-Car-Racer---Amiga/blob/4d5ef1d7fd6cf2065cdc7210c4691b62362ecdd5/original/docs/CODE.md
- https://github.com/MarkyTurtle/Stunt-Car-Racer---Amiga/blob/4d5ef1d7fd6cf2065cdc7210c4691b62362ecdd5/original/scr_boot.s

### Target CPU (reviewed)

Target architecture: 68000. This is not a verified minimum CPU for every frontend.
- https://github.com/MarkyTurtle/Stunt-Car-Racer---Amiga/blob/4d5ef1d7fd6cf2065cdc7210c4691b62362ecdd5/README.md
- https://github.com/MarkyTurtle/Stunt-Car-Racer---Amiga/blob/4d5ef1d7fd6cf2065cdc7210c4691b62362ecdd5/BUILDING.md
- https://github.com/MarkyTurtle/Stunt-Car-Racer---Amiga/blob/4d5ef1d7fd6cf2065cdc7210c4691b62362ecdd5/original/README.md
- https://github.com/MarkyTurtle/Stunt-Car-Racer---Amiga/blob/4d5ef1d7fd6cf2065cdc7210c4691b62362ecdd5/original/docs/CODE.md
- https://github.com/MarkyTurtle/Stunt-Car-Racer---Amiga/blob/4d5ef1d7fd6cf2065cdc7210c4691b62362ecdd5/original/scr_boot.s

### Build (reviewed)

Original and enhanced build scripts, disassembly configuration and CI are present; enhanced boot reaches game entry in author emulator harness, broader gameplay still under investigation. No independent build. Source-only review: no independent compilation, execution, gameplay or byte comparison.
- https://github.com/MarkyTurtle/Stunt-Car-Racer---Amiga/blob/4d5ef1d7fd6cf2065cdc7210c4691b62362ecdd5/README.md
- https://github.com/MarkyTurtle/Stunt-Car-Racer---Amiga/blob/4d5ef1d7fd6cf2065cdc7210c4691b62362ecdd5/BUILDING.md
- https://github.com/MarkyTurtle/Stunt-Car-Racer---Amiga/blob/4d5ef1d7fd6cf2065cdc7210c4691b62362ecdd5/original/README.md
- https://github.com/MarkyTurtle/Stunt-Car-Racer---Amiga/blob/4d5ef1d7fd6cf2065cdc7210c4691b62362ecdd5/original/docs/CODE.md
- https://github.com/MarkyTurtle/Stunt-Car-Racer---Amiga/blob/4d5ef1d7fd6cf2065cdc7210c4691b62362ecdd5/original/scr_boot.s

### Runtime profiles (no-evidence-found)

Documented dependencies and bounds are recorded in build notes; no independently verified complete runtime profile.
- https://github.com/MarkyTurtle/Stunt-Car-Racer---Amiga/blob/4d5ef1d7fd6cf2065cdc7210c4691b62362ecdd5/README.md
- https://github.com/MarkyTurtle/Stunt-Car-Racer---Amiga/blob/4d5ef1d7fd6cf2065cdc7210c4691b62362ecdd5/BUILDING.md
- https://github.com/MarkyTurtle/Stunt-Car-Racer---Amiga/blob/4d5ef1d7fd6cf2065cdc7210c4691b62362ecdd5/original/README.md
- https://github.com/MarkyTurtle/Stunt-Car-Racer---Amiga/blob/4d5ef1d7fd6cf2065cdc7210c4691b62362ecdd5/original/docs/CODE.md
- https://github.com/MarkyTurtle/Stunt-Car-Racer---Amiga/blob/4d5ef1d7fd6cf2065cdc7210c4691b62362ecdd5/original/scr_boot.s

### AI (reviewed)

The repository explicitly discloses AI-assisted development; specific attribution is recorded where stated.
- https://github.com/MarkyTurtle/Stunt-Car-Racer---Amiga/blob/4d5ef1d7fd6cf2065cdc7210c4691b62362ecdd5/README.md
- https://github.com/MarkyTurtle/Stunt-Car-Racer---Amiga/blob/4d5ef1d7fd6cf2065cdc7210c4691b62362ecdd5/BUILDING.md
- https://github.com/MarkyTurtle/Stunt-Car-Racer---Amiga/blob/4d5ef1d7fd6cf2065cdc7210c4691b62362ecdd5/original/README.md
- https://github.com/MarkyTurtle/Stunt-Car-Racer---Amiga/blob/4d5ef1d7fd6cf2065cdc7210c4691b62362ecdd5/original/docs/CODE.md
- https://github.com/MarkyTurtle/Stunt-Car-Racer---Amiga/blob/4d5ef1d7fd6cf2065cdc7210c4691b62362ecdd5/original/scr_boot.s

### Relationships (reviewed)

Turbo release and enhanced disk are distinct from the unmodified retail release.
- https://github.com/MarkyTurtle/Stunt-Car-Racer---Amiga/blob/4d5ef1d7fd6cf2065cdc7210c4691b62362ecdd5/README.md
- https://github.com/MarkyTurtle/Stunt-Car-Racer---Amiga/blob/4d5ef1d7fd6cf2065cdc7210c4691b62362ecdd5/BUILDING.md
- https://github.com/MarkyTurtle/Stunt-Car-Racer---Amiga/blob/4d5ef1d7fd6cf2065cdc7210c4691b62362ecdd5/original/README.md
- https://github.com/MarkyTurtle/Stunt-Car-Racer---Amiga/blob/4d5ef1d7fd6cf2065cdc7210c4691b62362ecdd5/original/docs/CODE.md
- https://github.com/MarkyTurtle/Stunt-Car-Racer---Amiga/blob/4d5ef1d7fd6cf2065cdc7210c4691b62362ecdd5/original/scr_boot.s

## Frontier: Elite II — Sinclair QL port

Project ID: neozeed-qlfrontier · Overall audit: partial

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
  "display_title": "Frontier: Elite II — Sinclair QL port",
  "id": "neozeed-qlfrontier",
  "last_activity": null,
  "last_checked": "2026-11-03",
  "re_started": null,
  "reconstructed_languages": [
    "68000 assembly",
    "C",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/neozeed/QLFrontier",
  "runtime_profiles": [],
  "source_cpu": [
    "68000"
  ],
  "source_language": [
    "68000 assembly",
    "C",
    "Python"
  ],
  "source_platforms": [
    "Atari ST"
  ],
  "status": "Source inspected; no independent build or execution",
  "subjects": [
    "Frontier: Elite II"
  ],
  "tags": [],
  "target_cpu": [
    "68008"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Sinclair QL"
  ],
  "techniques": [],
  "title": "Frontier: Elite II — Sinclair QL port",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "QLFrontier",
  "work_kinds": [
    "reverse-engineering-derived-port"
  ]
}
```

### Identity (reviewed)

Frontier: Elite II — Sinclair QL port. Pinned repository, documentation and selected implementation inspected.
- https://github.com/neozeed/QLFrontier/blob/ac289e2cc7b4e498eacdc38f71f36cb9482a4677/README.md
- https://github.com/neozeed/QLFrontier/blob/ac289e2cc7b4e498eacdc38f71f36cb9482a4677/Makefile
- https://github.com/neozeed/QLFrontier/blob/ac289e2cc7b4e498eacdc38f71f36cb9482a4677/src/start.s

### Classification (reviewed)

Port of the Atari ST disassembly to QDOS with 4-colour and 8-colour display variants, native file services and input adaptation. Original game logic is retained; hardware and rendering differ.
- https://github.com/neozeed/QLFrontier/blob/ac289e2cc7b4e498eacdc38f71f36cb9482a4677/README.md
- https://github.com/neozeed/QLFrontier/blob/ac289e2cc7b4e498eacdc38f71f36cb9482a4677/Makefile
- https://github.com/neozeed/QLFrontier/blob/ac289e2cc7b4e498eacdc38f71f36cb9482a4677/src/start.s

### Source CPU (reviewed)

Source architecture: 68000. No minimum CPU inferred.
- https://github.com/neozeed/QLFrontier/blob/ac289e2cc7b4e498eacdc38f71f36cb9482a4677/README.md
- https://github.com/neozeed/QLFrontier/blob/ac289e2cc7b4e498eacdc38f71f36cb9482a4677/Makefile
- https://github.com/neozeed/QLFrontier/blob/ac289e2cc7b4e498eacdc38f71f36cb9482a4677/src/start.s

### Target CPU (reviewed)

Target architecture: 68008. This is not a verified minimum CPU for every frontend.
- https://github.com/neozeed/QLFrontier/blob/ac289e2cc7b4e498eacdc38f71f36cb9482a4677/README.md
- https://github.com/neozeed/QLFrontier/blob/ac289e2cc7b4e498eacdc38f71f36cb9482a4677/Makefile
- https://github.com/neozeed/QLFrontier/blob/ac289e2cc7b4e498eacdc38f71f36cb9482a4677/src/start.s

### Build (reviewed)

README describes POSIX make, C compiler, Python and included JAS/linker; QLBox tests use Minerva and 1 MB. No physical hardware or stock 68008 performance verified; no independent test. Source-only review: no independent compilation, execution, gameplay or byte comparison.
- https://github.com/neozeed/QLFrontier/blob/ac289e2cc7b4e498eacdc38f71f36cb9482a4677/README.md
- https://github.com/neozeed/QLFrontier/blob/ac289e2cc7b4e498eacdc38f71f36cb9482a4677/Makefile
- https://github.com/neozeed/QLFrontier/blob/ac289e2cc7b4e498eacdc38f71f36cb9482a4677/src/start.s

### Runtime profiles (no-evidence-found)

Documented dependencies and bounds are recorded in build notes; no independently verified complete runtime profile.
- https://github.com/neozeed/QLFrontier/blob/ac289e2cc7b4e498eacdc38f71f36cb9482a4677/README.md
- https://github.com/neozeed/QLFrontier/blob/ac289e2cc7b4e498eacdc38f71f36cb9482a4677/Makefile
- https://github.com/neozeed/QLFrontier/blob/ac289e2cc7b4e498eacdc38f71f36cb9482a4677/src/start.s

### AI (no-evidence-found)

No actual development-AI contribution established in the inspected evidence. Missing attribution is not evidence of non-use.
- https://github.com/neozeed/QLFrontier/blob/ac289e2cc7b4e498eacdc38f71f36cb9482a4677/README.md
- https://github.com/neozeed/QLFrontier/blob/ac289e2cc7b4e498eacdc38f71f36cb9482a4677/Makefile
- https://github.com/neozeed/QLFrontier/blob/ac289e2cc7b4e498eacdc38f71f36cb9482a4677/src/start.s

### Relationships (reviewed)

Based on Atari ST Frontier disassembly, not a new independent disassembly of the original.
- https://github.com/neozeed/QLFrontier/blob/ac289e2cc7b4e498eacdc38f71f36cb9482a4677/README.md
- https://github.com/neozeed/QLFrontier/blob/ac289e2cc7b4e498eacdc38f71f36cb9482a4677/Makefile
- https://github.com/neozeed/QLFrontier/blob/ac289e2cc7b4e498eacdc38f71f36cb9482a4677/src/start.s

## The Pack Rat — DOS reverse-engineered web edition

Project ID: cambrianminds-the-pack-rat · Overall audit: partial

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
  "display_title": "The Pack Rat — DOS reverse-engineered web edition",
  "id": "cambrianminds-the-pack-rat",
  "last_activity": null,
  "last_checked": "2026-11-03",
  "re_started": null,
  "reconstructed_languages": [
    "JavaScript",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/CambrianMinds/the-pack-rat",
  "runtime_profiles": [],
  "source_cpu": [
    "x86"
  ],
  "source_language": [
    "JavaScript",
    "Python"
  ],
  "source_platforms": [
    "DOS"
  ],
  "status": "Source inspected; no independent build or execution",
  "subjects": [
    "The Pack Rat"
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
  "title": "The Pack Rat — DOS reverse-engineered web edition",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "the-pack-rat",
  "work_kinds": [
    "reimplementation",
    "data-format-analysis"
  ]
}
```

### Identity (reviewed)

The Pack Rat — DOS reverse-engineered web edition. Pinned repository, documentation and selected implementation inspected.
- https://github.com/CambrianMinds/the-pack-rat/blob/1a2ab9650c0126e935996ad22d7a2f9641a40323/README.md
- https://github.com/CambrianMinds/the-pack-rat/blob/1a2ab9650c0126e935996ad22d7a2f9641a40323/game.js
- https://github.com/CambrianMinds/the-pack-rat/blob/1a2ab9650c0126e935996ad22d7a2f9641a40323/scripts/extract.py

### Classification (reviewed)

Browser recreation of the 1992 DOS game with gameplay, level data decoding, sound synthesis and tile extraction. README attributes physics and compressed level handling to binary analysis; exact behavioral fidelity is a maintainer claim, not independently established.
- https://github.com/CambrianMinds/the-pack-rat/blob/1a2ab9650c0126e935996ad22d7a2f9641a40323/README.md
- https://github.com/CambrianMinds/the-pack-rat/blob/1a2ab9650c0126e935996ad22d7a2f9641a40323/game.js
- https://github.com/CambrianMinds/the-pack-rat/blob/1a2ab9650c0126e935996ad22d7a2f9641a40323/scripts/extract.py

### Source CPU (reviewed)

Source architecture: x86. No minimum CPU inferred.
- https://github.com/CambrianMinds/the-pack-rat/blob/1a2ab9650c0126e935996ad22d7a2f9641a40323/README.md
- https://github.com/CambrianMinds/the-pack-rat/blob/1a2ab9650c0126e935996ad22d7a2f9641a40323/game.js
- https://github.com/CambrianMinds/the-pack-rat/blob/1a2ab9650c0126e935996ad22d7a2f9641a40323/scripts/extract.py

### Target CPU (no-evidence-found)

No physical target CPU minimum established; portability or a managed runtime is not a hardware requirement.
- https://github.com/CambrianMinds/the-pack-rat/blob/1a2ab9650c0126e935996ad22d7a2f9641a40323/README.md
- https://github.com/CambrianMinds/the-pack-rat/blob/1a2ab9650c0126e935996ad22d7a2f9641a40323/game.js
- https://github.com/CambrianMinds/the-pack-rat/blob/1a2ab9650c0126e935996ad22d7a2f9641a40323/scripts/extract.py

### Build (reviewed)

HTML, JavaScript and assets in repository, with documented browser and automated tests; no code executed or gameplay verified. Source-only review: no independent compilation, execution, gameplay or byte comparison.
- https://github.com/CambrianMinds/the-pack-rat/blob/1a2ab9650c0126e935996ad22d7a2f9641a40323/README.md
- https://github.com/CambrianMinds/the-pack-rat/blob/1a2ab9650c0126e935996ad22d7a2f9641a40323/game.js
- https://github.com/CambrianMinds/the-pack-rat/blob/1a2ab9650c0126e935996ad22d7a2f9641a40323/scripts/extract.py

### Runtime profiles (no-evidence-found)

Documented dependencies and bounds are recorded in build notes; no independently verified complete runtime profile.
- https://github.com/CambrianMinds/the-pack-rat/blob/1a2ab9650c0126e935996ad22d7a2f9641a40323/README.md
- https://github.com/CambrianMinds/the-pack-rat/blob/1a2ab9650c0126e935996ad22d7a2f9641a40323/game.js
- https://github.com/CambrianMinds/the-pack-rat/blob/1a2ab9650c0126e935996ad22d7a2f9641a40323/scripts/extract.py

### AI (no-evidence-found)

No actual development-AI contribution established in the inspected evidence. Missing attribution is not evidence of non-use.
- https://github.com/CambrianMinds/the-pack-rat/blob/1a2ab9650c0126e935996ad22d7a2f9641a40323/README.md
- https://github.com/CambrianMinds/the-pack-rat/blob/1a2ab9650c0126e935996ad22d7a2f9641a40323/game.js
- https://github.com/CambrianMinds/the-pack-rat/blob/1a2ab9650c0126e935996ad22d7a2f9641a40323/scripts/extract.py

### Relationships (reviewed)

Reimplementation for browsers, not a byte-exact DOS binary or original source recovery.
- https://github.com/CambrianMinds/the-pack-rat/blob/1a2ab9650c0126e935996ad22d7a2f9641a40323/README.md
- https://github.com/CambrianMinds/the-pack-rat/blob/1a2ab9650c0126e935996ad22d7a2f9641a40323/game.js
- https://github.com/CambrianMinds/the-pack-rat/blob/1a2ab9650c0126e935996ad22d7a2f9641a40323/scripts/extract.py

## Bump ’n’ Jump — NES to Amiga port archive

Project ID: johnshawler-bump-n-jump-amiga · Overall audit: partial

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
  "display_title": "Bump ’n’ Jump — NES to Amiga port archive",
  "id": "johnshawler-bump-n-jump-amiga",
  "last_activity": null,
  "last_checked": "2026-11-03",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "68000 assembly",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/johnshawler/bump-n-jump-amiga",
  "runtime_profiles": [],
  "source_cpu": [
    "6502"
  ],
  "source_language": [
    "C",
    "68000 assembly",
    "Python"
  ],
  "source_platforms": [
    "NES"
  ],
  "status": "Source inspected; no independent build or execution",
  "subjects": [
    "Bump ’n’ Jump"
  ],
  "tags": [],
  "target_cpu": [
    "68020"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Amiga"
  ],
  "techniques": [],
  "title": "Bump ’n’ Jump — NES to Amiga port archive",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "bump-n-jump-amiga",
  "work_kinds": [
    "reverse-engineering-derived-port"
  ]
}
```

### Identity (reviewed)

Bump ’n’ Jump — NES to Amiga port archive. Pinned repository, documentation and selected implementation inspected.
- https://github.com/johnshawler/bump-n-jump-amiga/blob/1ea49c5be6b0e35db4ccb97c83cf10971e85eac4/README.md
- https://github.com/johnshawler/bump-n-jump-amiga/blob/1ea49c5be6b0e35db4ccb97c83cf10971e85eac4/docs/BUILD.md
- https://github.com/johnshawler/bump-n-jump-amiga/blob/1ea49c5be6b0e35db4ccb97c83cf10971e85eac4/generate_asm.py

### Classification (reviewed)

Experimental NES-derived A1200 port represented by a partial archive of runtime, translators and historical reports. Original cartridge-derived generated code and assets, the later DX work and release files are absent.
- https://github.com/johnshawler/bump-n-jump-amiga/blob/1ea49c5be6b0e35db4ccb97c83cf10971e85eac4/README.md
- https://github.com/johnshawler/bump-n-jump-amiga/blob/1ea49c5be6b0e35db4ccb97c83cf10971e85eac4/docs/BUILD.md
- https://github.com/johnshawler/bump-n-jump-amiga/blob/1ea49c5be6b0e35db4ccb97c83cf10971e85eac4/generate_asm.py

### Source CPU (reviewed)

Source architecture: 6502. No minimum CPU inferred.
- https://github.com/johnshawler/bump-n-jump-amiga/blob/1ea49c5be6b0e35db4ccb97c83cf10971e85eac4/README.md
- https://github.com/johnshawler/bump-n-jump-amiga/blob/1ea49c5be6b0e35db4ccb97c83cf10971e85eac4/docs/BUILD.md
- https://github.com/johnshawler/bump-n-jump-amiga/blob/1ea49c5be6b0e35db4ccb97c83cf10971e85eac4/generate_asm.py

### Target CPU (reviewed)

Target architecture: 68020. This is not a verified minimum CPU for every frontend.
- https://github.com/johnshawler/bump-n-jump-amiga/blob/1ea49c5be6b0e35db4ccb97c83cf10971e85eac4/README.md
- https://github.com/johnshawler/bump-n-jump-amiga/blob/1ea49c5be6b0e35db4ccb97c83cf10971e85eac4/docs/BUILD.md
- https://github.com/johnshawler/bump-n-jump-amiga/blob/1ea49c5be6b0e35db4ccb97c83cf10971e85eac4/generate_asm.py

### Build (reviewed)

Documented target is PAL A1200 68EC020, AGA and 2 MiB chip RAM; build requires user-supplied NES ROM, external tools and generated files. Historical tests do not establish full-game or physical-hardware coverage. Source-only review: no independent compilation, execution, gameplay or byte comparison.
- https://github.com/johnshawler/bump-n-jump-amiga/blob/1ea49c5be6b0e35db4ccb97c83cf10971e85eac4/README.md
- https://github.com/johnshawler/bump-n-jump-amiga/blob/1ea49c5be6b0e35db4ccb97c83cf10971e85eac4/docs/BUILD.md
- https://github.com/johnshawler/bump-n-jump-amiga/blob/1ea49c5be6b0e35db4ccb97c83cf10971e85eac4/generate_asm.py

### Runtime profiles (no-evidence-found)

Documented dependencies and bounds are recorded in build notes; no independently verified complete runtime profile.
- https://github.com/johnshawler/bump-n-jump-amiga/blob/1ea49c5be6b0e35db4ccb97c83cf10971e85eac4/README.md
- https://github.com/johnshawler/bump-n-jump-amiga/blob/1ea49c5be6b0e35db4ccb97c83cf10971e85eac4/docs/BUILD.md
- https://github.com/johnshawler/bump-n-jump-amiga/blob/1ea49c5be6b0e35db4ccb97c83cf10971e85eac4/generate_asm.py

### AI (no-evidence-found)

No actual development-AI contribution established in the inspected evidence. Missing attribution is not evidence of non-use.
- https://github.com/johnshawler/bump-n-jump-amiga/blob/1ea49c5be6b0e35db4ccb97c83cf10971e85eac4/README.md
- https://github.com/johnshawler/bump-n-jump-amiga/blob/1ea49c5be6b0e35db4ccb97c83cf10971e85eac4/docs/BUILD.md
- https://github.com/johnshawler/bump-n-jump-amiga/blob/1ea49c5be6b0e35db4ccb97c83cf10971e85eac4/generate_asm.py

### Relationships (reviewed)

Public archive is not the later DX/WHDLoad release; no full clean public build claimed.
- https://github.com/johnshawler/bump-n-jump-amiga/blob/1ea49c5be6b0e35db4ccb97c83cf10971e85eac4/README.md
- https://github.com/johnshawler/bump-n-jump-amiga/blob/1ea49c5be6b0e35db4ccb97c83cf10971e85eac4/docs/BUILD.md
- https://github.com/johnshawler/bump-n-jump-amiga/blob/1ea49c5be6b0e35db4ccb97c83cf10971e85eac4/generate_asm.py

## Do! Run Run — Amiga development source

Project ID: johnshawler-do-run-run-amiga · Overall audit: partial

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
  "display_title": "Do! Run Run — Amiga development source",
  "id": "johnshawler-do-run-run-amiga",
  "last_activity": null,
  "last_checked": "2026-11-03",
  "re_started": null,
  "reconstructed_languages": [
    "68000 assembly",
    "C",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/johnshawler/do-run-run-amiga",
  "runtime_profiles": [],
  "source_cpu": [
    "Z80"
  ],
  "source_language": [
    "68000 assembly",
    "C",
    "Python"
  ],
  "source_platforms": [
    "Arcade"
  ],
  "status": "Source inspected; no independent build or execution",
  "subjects": [
    "Do! Run Run"
  ],
  "tags": [],
  "target_cpu": [
    "68020"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Amiga"
  ],
  "techniques": [],
  "title": "Do! Run Run — Amiga development source",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "do-run-run-amiga",
  "work_kinds": [
    "reverse-engineering-derived-port"
  ]
}
```

### Identity (reviewed)

Do! Run Run — Amiga development source. Pinned repository, documentation and selected implementation inspected.
- https://github.com/johnshawler/do-run-run-amiga/blob/db6fb68f32c784042cb36340523be8bf4f659dd6/README.md
- https://github.com/johnshawler/do-run-run-amiga/blob/db6fb68f32c784042cb36340523be8bf4f659dd6/BUILDING.md
- https://github.com/johnshawler/do-run-run-amiga/blob/db6fb68f32c784042cb36340523be8bf4f659dd6/PUBLICATION_SCOPE.md
- https://github.com/johnshawler/do-run-run-amiga/blob/db6fb68f32c784042cb36340523be8bf4f659dd6/decode_dorunrun.py

### Classification (reviewed)

Partial authored source archive for an experimental arcade-to-A1200 port, including graphics, bounded input translation, and ROM analysis tools. Public diagnostic is not a complete playable release.
- https://github.com/johnshawler/do-run-run-amiga/blob/db6fb68f32c784042cb36340523be8bf4f659dd6/README.md
- https://github.com/johnshawler/do-run-run-amiga/blob/db6fb68f32c784042cb36340523be8bf4f659dd6/BUILDING.md
- https://github.com/johnshawler/do-run-run-amiga/blob/db6fb68f32c784042cb36340523be8bf4f659dd6/PUBLICATION_SCOPE.md
- https://github.com/johnshawler/do-run-run-amiga/blob/db6fb68f32c784042cb36340523be8bf4f659dd6/decode_dorunrun.py

### Source CPU (reviewed)

Source architecture: Z80. No minimum CPU inferred.
- https://github.com/johnshawler/do-run-run-amiga/blob/db6fb68f32c784042cb36340523be8bf4f659dd6/README.md
- https://github.com/johnshawler/do-run-run-amiga/blob/db6fb68f32c784042cb36340523be8bf4f659dd6/BUILDING.md
- https://github.com/johnshawler/do-run-run-amiga/blob/db6fb68f32c784042cb36340523be8bf4f659dd6/PUBLICATION_SCOPE.md
- https://github.com/johnshawler/do-run-run-amiga/blob/db6fb68f32c784042cb36340523be8bf4f659dd6/decode_dorunrun.py

### Target CPU (reviewed)

Target architecture: 68020. This is not a verified minimum CPU for every frontend.
- https://github.com/johnshawler/do-run-run-amiga/blob/db6fb68f32c784042cb36340523be8bf4f659dd6/README.md
- https://github.com/johnshawler/do-run-run-amiga/blob/db6fb68f32c784042cb36340523be8bf4f659dd6/BUILDING.md
- https://github.com/johnshawler/do-run-run-amiga/blob/db6fb68f32c784042cb36340523be8bf4f659dd6/PUBLICATION_SCOPE.md
- https://github.com/johnshawler/do-run-run-amiga/blob/db6fb68f32c784042cb36340523be8bf4f659dd6/decode_dorunrun.py

### Build (reviewed)

Native diagnostic requires a separately supplied parent arcade ROM and assembler. Later private game candidate has missing dependencies; no fresh build or gameplay test. Source-only review: no independent compilation, execution, gameplay or byte comparison.
- https://github.com/johnshawler/do-run-run-amiga/blob/db6fb68f32c784042cb36340523be8bf4f659dd6/README.md
- https://github.com/johnshawler/do-run-run-amiga/blob/db6fb68f32c784042cb36340523be8bf4f659dd6/BUILDING.md
- https://github.com/johnshawler/do-run-run-amiga/blob/db6fb68f32c784042cb36340523be8bf4f659dd6/PUBLICATION_SCOPE.md
- https://github.com/johnshawler/do-run-run-amiga/blob/db6fb68f32c784042cb36340523be8bf4f659dd6/decode_dorunrun.py

### Runtime profiles (no-evidence-found)

Documented dependencies and bounds are recorded in build notes; no independently verified complete runtime profile.
- https://github.com/johnshawler/do-run-run-amiga/blob/db6fb68f32c784042cb36340523be8bf4f659dd6/README.md
- https://github.com/johnshawler/do-run-run-amiga/blob/db6fb68f32c784042cb36340523be8bf4f659dd6/BUILDING.md
- https://github.com/johnshawler/do-run-run-amiga/blob/db6fb68f32c784042cb36340523be8bf4f659dd6/PUBLICATION_SCOPE.md
- https://github.com/johnshawler/do-run-run-amiga/blob/db6fb68f32c784042cb36340523be8bf4f659dd6/decode_dorunrun.py

### AI (no-evidence-found)

No actual development-AI contribution established in the inspected evidence. Missing attribution is not evidence of non-use.
- https://github.com/johnshawler/do-run-run-amiga/blob/db6fb68f32c784042cb36340523be8bf4f659dd6/README.md
- https://github.com/johnshawler/do-run-run-amiga/blob/db6fb68f32c784042cb36340523be8bf4f659dd6/BUILDING.md
- https://github.com/johnshawler/do-run-run-amiga/blob/db6fb68f32c784042cb36340523be8bf4f659dd6/PUBLICATION_SCOPE.md
- https://github.com/johnshawler/do-run-run-amiga/blob/db6fb68f32c784042cb36340523be8bf4f659dd6/decode_dorunrun.py

### Relationships (reviewed)

Historical milestones describe specific experiments; do not treat as proof the latest private build is reproducible.
- https://github.com/johnshawler/do-run-run-amiga/blob/db6fb68f32c784042cb36340523be8bf4f659dd6/README.md
- https://github.com/johnshawler/do-run-run-amiga/blob/db6fb68f32c784042cb36340523be8bf4f659dd6/BUILDING.md
- https://github.com/johnshawler/do-run-run-amiga/blob/db6fb68f32c784042cb36340523be8bf4f659dd6/PUBLICATION_SCOPE.md
- https://github.com/johnshawler/do-run-run-amiga/blob/db6fb68f32c784042cb36340523be8bf4f659dd6/decode_dorunrun.py

## Skate or Die — Apple IIGS to Amiga DX

Project ID: johnshawler-skate-or-die-dx-amiga · Overall audit: partial

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
  "display_title": "Skate or Die — Apple IIGS to Amiga DX",
  "id": "johnshawler-skate-or-die-dx-amiga",
  "last_activity": null,
  "last_checked": "2026-11-03",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "68000 assembly",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/johnshawler/skate-or-die-dx-amiga",
  "runtime_profiles": [],
  "source_cpu": [
    "65816"
  ],
  "source_language": [
    "C",
    "68000 assembly",
    "Python"
  ],
  "source_platforms": [
    "Apple IIGS"
  ],
  "status": "Source inspected; no independent build or execution",
  "subjects": [
    "Skate or Die"
  ],
  "tags": [],
  "target_cpu": [
    "68020"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Amiga"
  ],
  "techniques": [],
  "title": "Skate or Die — Apple IIGS to Amiga DX",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "skate-or-die-dx-amiga",
  "work_kinds": [
    "reverse-engineering-derived-port"
  ]
}
```

### Identity (reviewed)

Skate or Die — Apple IIGS to Amiga DX. Pinned repository, documentation and selected implementation inspected.
- https://github.com/johnshawler/skate-or-die-dx-amiga/blob/92c18f64ebd79b87230cb626f525dd603b72c747/README.md
- https://github.com/johnshawler/skate-or-die-dx-amiga/blob/92c18f64ebd79b87230cb626f525dd603b72c747/docs/TRANSLATOR.md
- https://github.com/johnshawler/skate-or-die-dx-amiga/blob/92c18f64ebd79b87230cb626f525dd603b72c747/ecs/game/src/evrun.c
- https://github.com/johnshawler/skate-or-die-dx-amiga/blob/92c18f64ebd79b87230cb626f525dd603b72c747/ecs/game/runtime/m816rt.c

### Classification (reviewed)

A1200 port translates original Apple IIGS 65816 game code to C and combines it with an Amiga runtime and native replacements; translator and lockstep machinery are published. Original data and generated game code are omitted.
- https://github.com/johnshawler/skate-or-die-dx-amiga/blob/92c18f64ebd79b87230cb626f525dd603b72c747/README.md
- https://github.com/johnshawler/skate-or-die-dx-amiga/blob/92c18f64ebd79b87230cb626f525dd603b72c747/docs/TRANSLATOR.md
- https://github.com/johnshawler/skate-or-die-dx-amiga/blob/92c18f64ebd79b87230cb626f525dd603b72c747/ecs/game/src/evrun.c
- https://github.com/johnshawler/skate-or-die-dx-amiga/blob/92c18f64ebd79b87230cb626f525dd603b72c747/ecs/game/runtime/m816rt.c

### Source CPU (reviewed)

Source architecture: 65816. No minimum CPU inferred.
- https://github.com/johnshawler/skate-or-die-dx-amiga/blob/92c18f64ebd79b87230cb626f525dd603b72c747/README.md
- https://github.com/johnshawler/skate-or-die-dx-amiga/blob/92c18f64ebd79b87230cb626f525dd603b72c747/docs/TRANSLATOR.md
- https://github.com/johnshawler/skate-or-die-dx-amiga/blob/92c18f64ebd79b87230cb626f525dd603b72c747/ecs/game/src/evrun.c
- https://github.com/johnshawler/skate-or-die-dx-amiga/blob/92c18f64ebd79b87230cb626f525dd603b72c747/ecs/game/runtime/m816rt.c

### Target CPU (reviewed)

Target architecture: 68020. This is not a verified minimum CPU for every frontend.
- https://github.com/johnshawler/skate-or-die-dx-amiga/blob/92c18f64ebd79b87230cb626f525dd603b72c747/README.md
- https://github.com/johnshawler/skate-or-die-dx-amiga/blob/92c18f64ebd79b87230cb626f525dd603b72c747/docs/TRANSLATOR.md
- https://github.com/johnshawler/skate-or-die-dx-amiga/blob/92c18f64ebd79b87230cb626f525dd603b72c747/ecs/game/src/evrun.c
- https://github.com/johnshawler/skate-or-die-dx-amiga/blob/92c18f64ebd79b87230cb626f525dd603b72c747/ecs/game/runtime/m816rt.c

### Build (reviewed)

Requires user-supplied game and Kickstart, extracted assets, generated headers and m68k toolchain; author has not tested a clean build from public checkout alone. Target is 68020, AGA and 2 MB chip RAM. Source-only review: no independent compilation, execution, gameplay or byte comparison.
- https://github.com/johnshawler/skate-or-die-dx-amiga/blob/92c18f64ebd79b87230cb626f525dd603b72c747/README.md
- https://github.com/johnshawler/skate-or-die-dx-amiga/blob/92c18f64ebd79b87230cb626f525dd603b72c747/docs/TRANSLATOR.md
- https://github.com/johnshawler/skate-or-die-dx-amiga/blob/92c18f64ebd79b87230cb626f525dd603b72c747/ecs/game/src/evrun.c
- https://github.com/johnshawler/skate-or-die-dx-amiga/blob/92c18f64ebd79b87230cb626f525dd603b72c747/ecs/game/runtime/m816rt.c

### Runtime profiles (no-evidence-found)

Documented dependencies and bounds are recorded in build notes; no independently verified complete runtime profile.
- https://github.com/johnshawler/skate-or-die-dx-amiga/blob/92c18f64ebd79b87230cb626f525dd603b72c747/README.md
- https://github.com/johnshawler/skate-or-die-dx-amiga/blob/92c18f64ebd79b87230cb626f525dd603b72c747/docs/TRANSLATOR.md
- https://github.com/johnshawler/skate-or-die-dx-amiga/blob/92c18f64ebd79b87230cb626f525dd603b72c747/ecs/game/src/evrun.c
- https://github.com/johnshawler/skate-or-die-dx-amiga/blob/92c18f64ebd79b87230cb626f525dd603b72c747/ecs/game/runtime/m816rt.c

### AI (no-evidence-found)

No actual development-AI contribution established in the inspected evidence. Missing attribution is not evidence of non-use.
- https://github.com/johnshawler/skate-or-die-dx-amiga/blob/92c18f64ebd79b87230cb626f525dd603b72c747/README.md
- https://github.com/johnshawler/skate-or-die-dx-amiga/blob/92c18f64ebd79b87230cb626f525dd603b72c747/docs/TRANSLATOR.md
- https://github.com/johnshawler/skate-or-die-dx-amiga/blob/92c18f64ebd79b87230cb626f525dd603b72c747/ecs/game/src/evrun.c
- https://github.com/johnshawler/skate-or-die-dx-amiga/blob/92c18f64ebd79b87230cb626f525dd603b72c747/ecs/game/runtime/m816rt.c

### Relationships (reviewed)

Original game logic is translated rather than a ground-up remake; source publication excludes copyrighted game material.
- https://github.com/johnshawler/skate-or-die-dx-amiga/blob/92c18f64ebd79b87230cb626f525dd603b72c747/README.md
- https://github.com/johnshawler/skate-or-die-dx-amiga/blob/92c18f64ebd79b87230cb626f525dd603b72c747/docs/TRANSLATOR.md
- https://github.com/johnshawler/skate-or-die-dx-amiga/blob/92c18f64ebd79b87230cb626f525dd603b72c747/ecs/game/src/evrun.c
- https://github.com/johnshawler/skate-or-die-dx-amiga/blob/92c18f64ebd79b87230cb626f525dd603b72c747/ecs/game/runtime/m816rt.c

## Atic Atac — Go reimplementation

Project ID: seamuswaldron-atic-atac · Overall audit: partial

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
  "display_title": "Atic Atac — Go reimplementation",
  "id": "seamuswaldron-atic-atac",
  "last_activity": null,
  "last_checked": "2026-11-03",
  "re_started": null,
  "reconstructed_languages": [
    "Go",
    "Z80 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/SeamusWaldron/atic-atac",
  "runtime_profiles": [],
  "source_cpu": [
    "Z80"
  ],
  "source_language": [
    "Go",
    "Z80 assembly"
  ],
  "source_platforms": [
    "ZX Spectrum"
  ],
  "status": "Source inspected; no independent build or execution",
  "subjects": [
    "Atic Atac"
  ],
  "tags": [],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [],
  "techniques": [],
  "title": "Atic Atac — Go reimplementation",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "atic-atac",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Atic Atac — Go reimplementation. Pinned repository, documentation and selected implementation inspected.
- https://github.com/SeamusWaldron/atic-atac/blob/a7926d1d221746f3392d4191d4ca7b4e0ee1c7da/README.md
- https://github.com/SeamusWaldron/atic-atac/blob/a7926d1d221746f3392d4191d4ca7b4e0ee1c7da/docs/atic-atac-initial-analysis.md
- https://github.com/SeamusWaldron/atic-atac/blob/a7926d1d221746f3392d4191d4ca7b4e0ee1c7da/Makefile

### Classification (reviewed)

Go reimplementation based on Simon Owen’s ZX Spectrum disassembly, with extracted rooms and game entities plus an optional experimental first-person view. README claims the 2D game is playable; 3D is alpha.
- https://github.com/SeamusWaldron/atic-atac/blob/a7926d1d221746f3392d4191d4ca7b4e0ee1c7da/README.md
- https://github.com/SeamusWaldron/atic-atac/blob/a7926d1d221746f3392d4191d4ca7b4e0ee1c7da/docs/atic-atac-initial-analysis.md
- https://github.com/SeamusWaldron/atic-atac/blob/a7926d1d221746f3392d4191d4ca7b4e0ee1c7da/Makefile

### Source CPU (reviewed)

Source architecture: Z80. No minimum CPU inferred.
- https://github.com/SeamusWaldron/atic-atac/blob/a7926d1d221746f3392d4191d4ca7b4e0ee1c7da/README.md
- https://github.com/SeamusWaldron/atic-atac/blob/a7926d1d221746f3392d4191d4ca7b4e0ee1c7da/docs/atic-atac-initial-analysis.md
- https://github.com/SeamusWaldron/atic-atac/blob/a7926d1d221746f3392d4191d4ca7b4e0ee1c7da/Makefile

### Target CPU (no-evidence-found)

No physical target CPU minimum established; portability or a managed runtime is not a hardware requirement.
- https://github.com/SeamusWaldron/atic-atac/blob/a7926d1d221746f3392d4191d4ca7b4e0ee1c7da/README.md
- https://github.com/SeamusWaldron/atic-atac/blob/a7926d1d221746f3392d4191d4ca7b4e0ee1c7da/docs/atic-atac-initial-analysis.md
- https://github.com/SeamusWaldron/atic-atac/blob/a7926d1d221746f3392d4191d4ca7b4e0ee1c7da/Makefile

### Build (reviewed)

Go, Ebitengine and oto source; README provides make run. No independent build, runtime, fidelity or platform-support tests. Source-only review: no independent compilation, execution, gameplay or byte comparison.
- https://github.com/SeamusWaldron/atic-atac/blob/a7926d1d221746f3392d4191d4ca7b4e0ee1c7da/README.md
- https://github.com/SeamusWaldron/atic-atac/blob/a7926d1d221746f3392d4191d4ca7b4e0ee1c7da/docs/atic-atac-initial-analysis.md
- https://github.com/SeamusWaldron/atic-atac/blob/a7926d1d221746f3392d4191d4ca7b4e0ee1c7da/Makefile

### Runtime profiles (no-evidence-found)

Documented dependencies and bounds are recorded in build notes; no independently verified complete runtime profile.
- https://github.com/SeamusWaldron/atic-atac/blob/a7926d1d221746f3392d4191d4ca7b4e0ee1c7da/README.md
- https://github.com/SeamusWaldron/atic-atac/blob/a7926d1d221746f3392d4191d4ca7b4e0ee1c7da/docs/atic-atac-initial-analysis.md
- https://github.com/SeamusWaldron/atic-atac/blob/a7926d1d221746f3392d4191d4ca7b4e0ee1c7da/Makefile

### AI (reviewed)

The repository explicitly discloses AI-assisted development; specific attribution is recorded where stated.
- https://github.com/SeamusWaldron/atic-atac/blob/a7926d1d221746f3392d4191d4ca7b4e0ee1c7da/README.md
- https://github.com/SeamusWaldron/atic-atac/blob/a7926d1d221746f3392d4191d4ca7b4e0ee1c7da/docs/atic-atac-initial-analysis.md
- https://github.com/SeamusWaldron/atic-atac/blob/a7926d1d221746f3392d4191d4ca7b4e0ee1c7da/Makefile

### Relationships (reviewed)

Uses an existing disassembly from mrcook/zx-spectrum-games; separate Go implementation, not a new original disassembly.
- https://github.com/SeamusWaldron/atic-atac/blob/a7926d1d221746f3392d4191d4ca7b4e0ee1c7da/README.md
- https://github.com/SeamusWaldron/atic-atac/blob/a7926d1d221746f3392d4191d4ca7b4e0ee1c7da/docs/atic-atac-initial-analysis.md
- https://github.com/SeamusWaldron/atic-atac/blob/a7926d1d221746f3392d4191d4ca7b4e0ee1c7da/Makefile

## Pinned evidence manifest

- akustikrausch-protracker4-makefile: https://github.com/akustikrausch/protracker4/blob/e33274565026d9348f326e4b4e75503ff6c2b585/Makefile (Git blob a6a3a203e636a533aa949cf0db143a25e8527783)
- akustikrausch-protracker4-protracker-asm: https://github.com/akustikrausch/protracker4/blob/e33274565026d9348f326e4b4e75503ff6c2b585/Protracker.asm (Git blob 59c6b6a97d4f5a3dd6a5c95191c659d277e340c0)
- akustikrausch-protracker4-readme-md: https://github.com/akustikrausch/protracker4/blob/e33274565026d9348f326e4b4e75503ff6c2b585/README.md (Git blob 17ae7d480bce06085a46de5a04d7cb086d2fc24d)
- akustikrausch-protracker4-src-engine-efx8-asm: https://github.com/akustikrausch/protracker4/blob/e33274565026d9348f326e4b4e75503ff6c2b585/src/engine/efx8.asm (Git blob b91b801fc6bff718e0911a800fa6c8523d68cb20)
- akustikrausch-protracker4-src-sys-ahi-asm: https://github.com/akustikrausch/protracker4/blob/e33274565026d9348f326e4b4e75503ff6c2b585/src/sys/ahi.asm (Git blob 855f26da5b1ad07dafeb91ad81b51faf6afe0c0d)
- cambrianminds-the-pack-rat-readme-md: https://github.com/cambrianminds/the-pack-rat/blob/1a2ab9650c0126e935996ad22d7a2f9641a40323/README.md (Git blob dc399dbd22b5c3b454b0a46b06efa41bc4f6eee6)
- cambrianminds-the-pack-rat-scripts-extract-py: https://github.com/cambrianminds/the-pack-rat/blob/1a2ab9650c0126e935996ad22d7a2f9641a40323/scripts/extract.py (Git blob 5787e01d062c4e65f4e9e5a72baf9b3b5cf80489)
- georgeflower-faxanadu-atari-st-atari-st-readme-md: https://github.com/georgeflower/faxanadu-atari-st/blob/6d2ede050368886fb2024a5989601e9ab0eeaad4/atari_st/README.md (Git blob b0fb08012e61d8065e846c68c2a2279e4b919aad)
- georgeflower-faxanadu-atari-st-atari-st-src-main-s: https://github.com/georgeflower/faxanadu-atari-st/blob/6d2ede050368886fb2024a5989601e9ab0eeaad4/atari_st/src/main.s (Git blob 122a962199893867c2ebdabe47ddddfd85d9c082)
- georgeflower-faxanadu-atari-st-readme-md: https://github.com/georgeflower/faxanadu-atari-st/blob/6d2ede050368886fb2024a5989601e9ab0eeaad4/README.md (Git blob cc591e60abf65ead696e2a323fb4724f20b32932)
- johnshawler-alcon-amiga-readme-md: https://github.com/johnshawler/alcon-amiga/blob/3e0f6794235890d7ea4bdba33c352385a76a542a/README.md (Git blob 2d816b2614980f7c269c08268afb9cc725184b29)
- johnshawler-bump-n-jump-amiga-docs-build-md: https://github.com/johnshawler/bump-n-jump-amiga/blob/1ea49c5be6b0e35db4ccb97c83cf10971e85eac4/docs/BUILD.md (Git blob 3ddffc6659745febf0da732f66b2225a25a52fe9)
- johnshawler-bump-n-jump-amiga-generate-asm-py: https://github.com/johnshawler/bump-n-jump-amiga/blob/1ea49c5be6b0e35db4ccb97c83cf10971e85eac4/generate_asm.py (Git blob 1c1800cd0a3fcdd6feabcd945031445c31f4add3)
- johnshawler-bump-n-jump-amiga-readme-md: https://github.com/johnshawler/bump-n-jump-amiga/blob/1ea49c5be6b0e35db4ccb97c83cf10971e85eac4/README.md (Git blob a45ea2d1ad420e59a6a2fe03841d63c0579be443)
- johnshawler-do-run-run-amiga-building-md: https://github.com/johnshawler/do-run-run-amiga/blob/db6fb68f32c784042cb36340523be8bf4f659dd6/BUILDING.md (Git blob 93245460b78e5b09ee614f3a1c1808a116e47d5c)
- johnshawler-do-run-run-amiga-decode-dorunrun-py: https://github.com/johnshawler/do-run-run-amiga/blob/db6fb68f32c784042cb36340523be8bf4f659dd6/decode_dorunrun.py (Git blob 95e857eb05101681e057763346e77726e253659d)
- johnshawler-do-run-run-amiga-publication-scope-md: https://github.com/johnshawler/do-run-run-amiga/blob/db6fb68f32c784042cb36340523be8bf4f659dd6/PUBLICATION_SCOPE.md (Git blob 45f6883fab8fda77b9ceedd6279487591b8f6e7d)
- johnshawler-do-run-run-amiga-readme-md: https://github.com/johnshawler/do-run-run-amiga/blob/db6fb68f32c784042cb36340523be8bf4f659dd6/README.md (Git blob 29b7318ad888a678b03c947cfa0ed577061f3caf)
- johnshawler-skate-or-die-dx-amiga-docs-translator-md: https://github.com/johnshawler/skate-or-die-dx-amiga/blob/92c18f64ebd79b87230cb626f525dd603b72c747/docs/TRANSLATOR.md (Git blob 0155edb6a73741b98a5007d20fa208151b7f5daa)
- johnshawler-skate-or-die-dx-amiga-ecs-game-runtime-m816rt-c: https://github.com/johnshawler/skate-or-die-dx-amiga/blob/92c18f64ebd79b87230cb626f525dd603b72c747/ecs/game/runtime/m816rt.c (Git blob 4d037058afcea2629a6cc3c26194c7c5df050363)
- johnshawler-skate-or-die-dx-amiga-readme-md: https://github.com/johnshawler/skate-or-die-dx-amiga/blob/92c18f64ebd79b87230cb626f525dd603b72c747/README.md (Git blob 379df71cd5832aae586bc1608e598dddfea36e96)
- johnshawler-yie-amiga-readme-md: https://github.com/johnshawler/yie-amiga/blob/2a6f94cb01529a3bcd379c09a5cb45301f74f6ee/README.md (Git blob e5ee6f6bea4e2a97676b97630abdf00b1c4b82e9)
- markyturtle-stunt-car-racer-amiga-building-md: https://github.com/markyturtle/stunt-car-racer---amiga/blob/4d5ef1d7fd6cf2065cdc7210c4691b62362ecdd5/BUILDING.md (Git blob d8276f3388c7a5fca8835e881b4c14030436df48)
- markyturtle-stunt-car-racer-amiga-original-docs-code-md: https://github.com/markyturtle/stunt-car-racer---amiga/blob/4d5ef1d7fd6cf2065cdc7210c4691b62362ecdd5/original/docs/CODE.md (Git blob 63efe59b5331d7de719b47720a22f31c1b141334)
- markyturtle-stunt-car-racer-amiga-original-readme-md: https://github.com/markyturtle/stunt-car-racer---amiga/blob/4d5ef1d7fd6cf2065cdc7210c4691b62362ecdd5/original/README.md (Git blob a042ed7e85e6cbf7d6e35b9eca5a195ba92ce14d)
- markyturtle-stunt-car-racer-amiga-original-scr-boot-s: https://github.com/markyturtle/stunt-car-racer---amiga/blob/4d5ef1d7fd6cf2065cdc7210c4691b62362ecdd5/original/scr_boot.s (Git blob 02bdb6d23f2233459e71c12047650d528108b160)
- markyturtle-stunt-car-racer-amiga-readme-md: https://github.com/markyturtle/stunt-car-racer---amiga/blob/4d5ef1d7fd6cf2065cdc7210c4691b62362ecdd5/README.md (Git blob 7e3dd0f3b013305dfaf41e1d28ff5dd1a15829f2)
- neozeed-qlfrontier-makefile: https://github.com/neozeed/qlfrontier/blob/ac289e2cc7b4e498eacdc38f71f36cb9482a4677/Makefile (Git blob 9cfa3b800b56f820c72af95c219f569e02fd3f9c)
- neozeed-qlfrontier-readme-md: https://github.com/neozeed/qlfrontier/blob/ac289e2cc7b4e498eacdc38f71f36cb9482a4677/README.md (Git blob 5d2dab15ae063e7a9f02b521751e1da69446f5a9)
- neozeed-qlfrontier-src-start-s: https://github.com/neozeed/qlfrontier/blob/ac289e2cc7b4e498eacdc38f71f36cb9482a4677/src/start.s (Git blob 8cec3cb2294dff5186257f5092a2260ffd6c13dd)
- parker-fawcett-rebuild-dossier-readme-md: https://github.com/parker-fawcett/rebuild-dossier/blob/7e67b999e5b99d8d206ea4dae415baa774c95dad/README.md (Git blob a4ffd904c6d888f0839a9710cdfc68a9ce8e30f9)
- seamuswaldron-atic-atac-docs-atic-atac-initial-analysis-md: https://github.com/seamuswaldron/atic-atac/blob/a7926d1d221746f3392d4191d4ca7b4e0ee1c7da/docs/atic-atac-initial-analysis.md (Git blob 69ed8de3fc9c8c3cf5cacc92256e5fbd1490bee5)
- seamuswaldron-atic-atac-makefile: https://github.com/seamuswaldron/atic-atac/blob/a7926d1d221746f3392d4191d4ca7b4e0ee1c7da/Makefile (Git blob bdbe2db6e1bdea85016161d9c0e3198b0501c4df)
- seamuswaldron-atic-atac-readme-md: https://github.com/seamuswaldron/atic-atac/blob/a7926d1d221746f3392d4191d4ca7b4e0ee1c7da/README.md (Git blob 934aabbe47950e40f5c04835b8e34dca4881bb65)

## Sources

```json
[
  {
    "first_indexed": "2026-11-03",
    "id": "github-akustikrausch-protracker4",
    "kind": "github-repository",
    "last_reviewed": "2026-11-03",
    "open_task_ids": [],
    "projects_promoted": [
      "akustikrausch-protracker4"
    ],
    "reason": "Modern continuation of the released ProTracker 4 source, with 4/8-channel tracker editing, RTG screens and AHI audio. This is a source-based continuation, not a claimed disassembly or byte-exact original reconstruction.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/akustikrausch/protracker4"
  },
  {
    "first_indexed": "2026-11-03",
    "id": "github-markyturtle-stunt-car-racer-amiga",
    "kind": "github-repository",
    "last_reviewed": "2026-11-03",
    "open_task_ids": [],
    "projects_promoted": [
      "markyturtle-stunt-car-racer-amiga"
    ],
    "reason": "Disassembled game, bootblock and loader from the Galahad Turbo release, with separately maintained enhanced AmigaDOS disk. Author claims original parts reassemble byte-identically to that release, not necessarily the untouched retail version.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/MarkyTurtle/Stunt-Car-Racer---Amiga"
  },
  {
    "first_indexed": "2026-11-03",
    "id": "github-neozeed-qlfrontier",
    "kind": "github-repository",
    "last_reviewed": "2026-11-03",
    "open_task_ids": [],
    "projects_promoted": [
      "neozeed-qlfrontier"
    ],
    "reason": "Port of the Atari ST disassembly to QDOS with 4-colour and 8-colour display variants, native file services and input adaptation. Original game logic is retained; hardware and rendering differ.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/neozeed/QLFrontier"
  },
  {
    "first_indexed": "2026-11-03",
    "id": "github-cambrianminds-the-pack-rat",
    "kind": "github-repository",
    "last_reviewed": "2026-11-03",
    "open_task_ids": [],
    "projects_promoted": [
      "cambrianminds-the-pack-rat"
    ],
    "reason": "Browser recreation of the 1992 DOS game with gameplay, level data decoding, sound synthesis and tile extraction. README attributes physics and compressed level handling to binary analysis; exact behavioral fidelity is a maintainer claim, not independently established.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/CambrianMinds/the-pack-rat"
  },
  {
    "first_indexed": "2026-11-03",
    "id": "github-johnshawler-bump-n-jump-amiga",
    "kind": "github-repository",
    "last_reviewed": "2026-11-03",
    "open_task_ids": [],
    "projects_promoted": [
      "johnshawler-bump-n-jump-amiga"
    ],
    "reason": "Experimental NES-derived A1200 port represented by a partial archive of runtime, translators and historical reports. Original cartridge-derived generated code and assets, the later DX work and release files are absent.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/johnshawler/bump-n-jump-amiga"
  },
  {
    "first_indexed": "2026-11-03",
    "id": "github-johnshawler-do-run-run-amiga",
    "kind": "github-repository",
    "last_reviewed": "2026-11-03",
    "open_task_ids": [],
    "projects_promoted": [
      "johnshawler-do-run-run-amiga"
    ],
    "reason": "Partial authored source archive for an experimental arcade-to-A1200 port, including graphics, bounded input translation, and ROM analysis tools. Public diagnostic is not a complete playable release.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/johnshawler/do-run-run-amiga"
  },
  {
    "first_indexed": "2026-11-03",
    "id": "github-johnshawler-skate-or-die-dx-amiga",
    "kind": "github-repository",
    "last_reviewed": "2026-11-03",
    "open_task_ids": [],
    "projects_promoted": [
      "johnshawler-skate-or-die-dx-amiga"
    ],
    "reason": "A1200 port translates original Apple IIGS 65816 game code to C and combines it with an Amiga runtime and native replacements; translator and lockstep machinery are published. Original data and generated game code are omitted.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/johnshawler/skate-or-die-dx-amiga"
  },
  {
    "first_indexed": "2026-11-03",
    "id": "github-seamuswaldron-atic-atac",
    "kind": "github-repository",
    "last_reviewed": "2026-11-03",
    "open_task_ids": [],
    "projects_promoted": [
      "seamuswaldron-atic-atac"
    ],
    "reason": "Go reimplementation based on Simon Owen’s ZX Spectrum disassembly, with extracted rooms and game entities plus an optional experimental first-person view. README claims the 2D game is playable; 3D is alpha.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/SeamusWaldron/atic-atac"
  },
  {
    "first_indexed": "2026-11-03",
    "id": "github-georgeflower-faxanadu-atari-st",
    "kind": "github-repository",
    "last_reviewed": "2026-11-03",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Original NES disassembly is copied from chipx86/faxanadu; the separate native Atari ST port README says it has just started and only shows colour bars. Defer as an early port until game behavior is present.",
    "review_state": "partial",
    "source": "https://github.com/georgeflower/faxanadu-atari-st"
  },
  {
    "first_indexed": "2026-11-03",
    "id": "github-johnshawler-yie-amiga",
    "kind": "github-repository",
    "last_reviewed": "2026-11-03",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Reference collection of MAME, FPGA and NES source snapshots. README explicitly says it is research material, not a playable game, merged engine or Amiga port. Defer for actual port implementation.",
    "review_state": "partial",
    "source": "https://github.com/johnshawler/yie-amiga"
  },
  {
    "first_indexed": "2026-11-03",
    "id": "github-johnshawler-alcon-amiga",
    "kind": "github-repository",
    "last_reviewed": "2026-11-03",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Repository contains only a title README with no substantive source or documented reconstruction; defer pending implementation.",
    "review_state": "partial",
    "source": "https://github.com/johnshawler/Alcon-Amiga"
  },
  {
    "first_indexed": "2026-11-03",
    "id": "github-parker-fawcett-rebuild-dossier",
    "kind": "github-repository",
    "last_reviewed": "2026-11-03",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Generic modern web-service specification and test-generation tool, rather than retro binary or platform reconstruction; outside this focused discovery pass.",
    "review_state": "partial",
    "source": "https://github.com/Parker-Fawcett/rebuild-dossier"
  }
]
```

## Decisions

```json
[
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/georgeflower/faxanadu-atari-st/blob/6d2ede050368886fb2024a5989601e9ab0eeaad4/README.md",
      "https://github.com/georgeflower/faxanadu-atari-st/blob/6d2ede050368886fb2024a5989601e9ab0eeaad4/atari_st/README.md",
      "https://github.com/georgeflower/faxanadu-atari-st/blob/6d2ede050368886fb2024a5989601e9ab0eeaad4/atari_st/src/main.s"
    ],
    "id": "pass108-georgeflower-faxanadu-atari-st",
    "project_ids": [],
    "reason": "Original NES disassembly is copied from chipx86/faxanadu; the separate native Atari ST port README says it has just started and only shows colour bars. Defer as an early port until game behavior is present.",
    "reviewed_at": "2026-11-03",
    "source_ids": [
      "github-georgeflower-faxanadu-atari-st"
    ],
    "title": "georgeflower/faxanadu-atari-st",
    "url": "https://github.com/georgeflower/faxanadu-atari-st"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/johnshawler/yie-amiga/blob/2a6f94cb01529a3bcd379c09a5cb45301f74f6ee/README.md"
    ],
    "id": "pass108-johnshawler-yie-amiga",
    "project_ids": [],
    "reason": "Reference collection of MAME, FPGA and NES source snapshots. README explicitly says it is research material, not a playable game, merged engine or Amiga port. Defer for actual port implementation.",
    "reviewed_at": "2026-11-03",
    "source_ids": [
      "github-johnshawler-yie-amiga"
    ],
    "title": "johnshawler/yie-amiga",
    "url": "https://github.com/johnshawler/yie-amiga"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/johnshawler/Alcon-Amiga/blob/3e0f6794235890d7ea4bdba33c352385a76a542a/README.md"
    ],
    "id": "pass108-johnshawler-alcon-amiga",
    "project_ids": [],
    "reason": "Repository contains only a title README with no substantive source or documented reconstruction; defer pending implementation.",
    "reviewed_at": "2026-11-03",
    "source_ids": [
      "github-johnshawler-alcon-amiga"
    ],
    "title": "johnshawler/Alcon-Amiga",
    "url": "https://github.com/johnshawler/Alcon-Amiga"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/Parker-Fawcett/rebuild-dossier/blob/7e67b999e5b99d8d206ea4dae415baa774c95dad/README.md"
    ],
    "id": "pass108-parker-fawcett-rebuild-dossier",
    "project_ids": [],
    "reason": "Generic modern web-service specification and test-generation tool, rather than retro binary or platform reconstruction; outside this focused discovery pass.",
    "reviewed_at": "2026-11-03",
    "source_ids": [
      "github-parker-fawcett-rebuild-dossier"
    ],
    "title": "Parker-Fawcett/rebuild-dossier",
    "url": "https://github.com/Parker-Fawcett/rebuild-dossier"
  }
]
```

## Research event notes

Personally screened 742 repository URLs across C64, ZX Spectrum, Amiga, Atari ST, CPC and DOS/Windows searches against current main; reviewed available pinned repository trees and selected documentation and source. No binaries executed. ProTracker is a source-based continuation, not a disassembly. Claims of exactness and gameplay are attributed to project documentation; no independent runtime verification. No worker, branch or PR used.
