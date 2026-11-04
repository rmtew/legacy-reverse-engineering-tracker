# Retro game and application discovery

Screen focused retro repository searches: add 11 projects.

Date: 2026-11-04 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- oldcompcz-hisoft-c / Runtime profiles (no-evidence-found): Documented dependencies and bounds are recorded in build notes; no independently verified complete runtime profile.
- oldcompcz-hisoft-c / AI (no-evidence-found): No actual development-AI contribution established in the inspected evidence. Missing attribution is not evidence of non-use.
- programandala-net-abersoft-forth / Runtime profiles (no-evidence-found): Documented dependencies and bounds are recorded in build notes; no independently verified complete runtime profile.
- programandala-net-abersoft-forth / AI (no-evidence-found): No actual development-AI contribution established in the inspected evidence. Missing attribution is not evidence of non-use.
- escoman-zx-disasm / Runtime profiles (no-evidence-found): Documented dependencies and bounds are recorded in build notes; no independently verified complete runtime profile.
- escoman-zx-disasm / AI (no-evidence-found): No actual development-AI contribution established in the inspected evidence. Missing attribution is not evidence of non-use.
- cookertron-chuckie-egg-2-js / Target CPU (no-evidence-found): No physical target CPU minimum established; portability or a managed runtime is not a hardware requirement.
- cookertron-chuckie-egg-2-js / Runtime profiles (no-evidence-found): Documented dependencies and bounds are recorded in build notes; no independently verified complete runtime profile.
- cookertron-chuckie-egg-2-js / AI (no-evidence-found): No actual development-AI contribution established in the inspected evidence. Missing attribution is not evidence of non-use.
- wdominik-motionvm / Target CPU (no-evidence-found): No physical target CPU minimum established; portability or a managed runtime is not a hardware requirement.
- wdominik-motionvm / Runtime profiles (no-evidence-found): Documented dependencies and bounds are recorded in build notes; no independently verified complete runtime profile.
- wdominik-motionvm / AI (no-evidence-found): No actual development-AI contribution established in the inspected evidence. Missing attribution is not evidence of non-use.
- dagrigorev-openblood / Target CPU (no-evidence-found): No physical target CPU minimum established; portability or a managed runtime is not a hardware requirement.
- dagrigorev-openblood / Runtime profiles (no-evidence-found): Documented dependencies and bounds are recorded in build notes; no independently verified complete runtime profile.
- dagrigorev-openblood / AI (no-evidence-found): No actual development-AI contribution established in the inspected evidence. Missing attribution is not evidence of non-use.
- lostartefacts-tr01 / Runtime profiles (no-evidence-found): Documented dependencies and bounds are recorded in build notes; no independently verified complete runtime profile.
- lostartefacts-tr01 / AI (no-evidence-found): No actual development-AI contribution established in the inspected evidence. Missing attribution is not evidence of non-use.
- geert-jan77-disassembler6510 / Target CPU (no-evidence-found): No physical target CPU minimum established; portability or a managed runtime is not a hardware requirement.
- geert-jan77-disassembler6510 / Runtime profiles (no-evidence-found): Documented dependencies and bounds are recorded in build notes; no independently verified complete runtime profile.
- geert-jan77-disassembler6510 / AI (no-evidence-found): No actual development-AI contribution established in the inspected evidence. Missing attribution is not evidence of non-use.
- mitigd-dos-hle-kit / Runtime profiles (no-evidence-found): Documented dependencies and bounds are recorded in build notes; no independently verified complete runtime profile.
- mitigd-dos-hle-kit / AI (no-evidence-found): No actual development-AI contribution established in the inspected evidence. Missing attribution is not evidence of non-use.
- virtualaaron09-oss-thefifthaxis-remaster / Target CPU (no-evidence-found): No physical target CPU minimum established; portability or a managed runtime is not a hardware requirement.
- virtualaaron09-oss-thefifthaxis-remaster / Runtime profiles (no-evidence-found): Documented dependencies and bounds are recorded in build notes; no independently verified complete runtime profile.
- virtualaaron09-oss-thefifthaxis-remaster / AI (no-evidence-found): No actual development-AI contribution established in the inspected evidence. Missing attribution is not evidence of non-use.
- pbakota-tisland / Runtime profiles (no-evidence-found): Documented dependencies and bounds are recorded in build notes; no independently verified complete runtime profile.
- pbakota-tisland / AI (no-evidence-found): No actual development-AI contribution established in the inspected evidence. Missing attribution is not evidence of non-use.

## HiSoft C 1.3 — ZX Spectrum compiler reconstruction

Project ID: oldcompcz-hisoft-c · Overall audit: partial

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
  "display_title": "HiSoft C 1.3 — ZX Spectrum compiler reconstruction",
  "id": "oldcompcz-hisoft-c",
  "last_activity": null,
  "last_checked": "2026-11-04",
  "re_started": null,
  "reconstructed_languages": [
    "Z80 assembly",
    "C"
  ],
  "record_class": "subject",
  "repo": "https://github.com/oldcompcz/HiSoft-C",
  "runtime_profiles": [],
  "source_cpu": [
    "Z80"
  ],
  "source_language": [],
  "source_platforms": [
    "ZX Spectrum"
  ],
  "status": "Source inspected; no independent build or execution",
  "subjects": [
    "HiSoft C 1.3"
  ],
  "tags": [],
  "target_cpu": [
    "Z80"
  ],
  "target_kinds": [
    "development-tool"
  ],
  "target_platforms": [
    "ZX Spectrum"
  ],
  "techniques": [],
  "title": "HiSoft C 1.3 — ZX Spectrum compiler reconstruction",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "HiSoft-C",
  "work_kinds": [
    "disassembly",
    "source-reconstruction"
  ]
}
```

### Identity (reviewed)

HiSoft C 1.3 — ZX Spectrum compiler reconstruction. Pinned repository, documentation and selected implementation inspected.
- https://github.com/oldcompcz/HiSoft-C/blob/a056f4eb2d36e846c173b2302560c91fb5c9093d/README.md

### Classification (reviewed)

Annotated Z80 reconstruction of the HiSoft C 1.3 compiler. The author describes byte-parity checks for the 25,600-byte compiler image and rebuilt tape; a separate explanatory C model omits the editor, media interface and resident runtime.
- https://github.com/oldcompcz/HiSoft-C/blob/a056f4eb2d36e846c173b2302560c91fb5c9093d/README.md

### Source CPU (reviewed)

Source architecture: Z80. No minimum CPU inferred.
- https://github.com/oldcompcz/HiSoft-C/blob/a056f4eb2d36e846c173b2302560c91fb5c9093d/README.md

### Target CPU (reviewed)

Target architecture: Z80. This is not a verified minimum CPU for every frontend.
- https://github.com/oldcompcz/HiSoft-C/blob/a056f4eb2d36e846c173b2302560c91fb5c9093d/README.md

### Build (reviewed)

The repository documents make verify and z80asm; author-reported parity has not been independently reproduced. Source-only review: no independent compilation, execution, gameplay or byte comparison.
- https://github.com/oldcompcz/HiSoft-C/blob/a056f4eb2d36e846c173b2302560c91fb5c9093d/README.md

### Runtime profiles (no-evidence-found)

Documented dependencies and bounds are recorded in build notes; no independently verified complete runtime profile.
- https://github.com/oldcompcz/HiSoft-C/blob/a056f4eb2d36e846c173b2302560c91fb5c9093d/README.md

### AI (no-evidence-found)

No actual development-AI contribution established in the inspected evidence. Missing attribution is not evidence of non-use.
- https://github.com/oldcompcz/HiSoft-C/blob/a056f4eb2d36e846c173b2302560c91fb5c9093d/README.md

### Relationships (reviewed)

The C model is explanatory, not a byte-exact replacement for the Z80 compiler.
- https://github.com/oldcompcz/HiSoft-C/blob/a056f4eb2d36e846c173b2302560c91fb5c9093d/README.md

## Abersoft Forth — ZX Spectrum disassembly

Project ID: programandala-net-abersoft-forth · Overall audit: partial

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
  "display_title": "Abersoft Forth — ZX Spectrum disassembly",
  "id": "programandala-net-abersoft-forth",
  "last_activity": null,
  "last_checked": "2026-11-04",
  "re_started": null,
  "reconstructed_languages": [
    "Z80 assembly",
    "Forth"
  ],
  "record_class": "subject",
  "repo": "https://github.com/programandala-net/abersoft-forth",
  "runtime_profiles": [],
  "source_cpu": [
    "Z80"
  ],
  "source_language": [],
  "source_platforms": [
    "ZX Spectrum"
  ],
  "status": "Source inspected; no independent build or execution",
  "subjects": [
    "Abersoft Forth"
  ],
  "tags": [],
  "target_cpu": [
    "Z80"
  ],
  "target_kinds": [
    "development-tool"
  ],
  "target_platforms": [
    "ZX Spectrum"
  ],
  "techniques": [],
  "title": "Abersoft Forth — ZX Spectrum disassembly",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "abersoft-forth",
  "work_kinds": [
    "disassembly",
    "source-reconstruction"
  ]
}
```

### Identity (reviewed)

Abersoft Forth — ZX Spectrum disassembly. Pinned repository, documentation and selected implementation inspected.
- https://github.com/programandala-net/abersoft-forth/blob/36af6cb80bbb69b0d25c10f77d3a5345763bd9d2/README.adoc

### Classification (reviewed)

Annotated Z80 disassembly of Abersoft Forth with generated symbols and tools written in the Forth system itself. Repository contains a rebuild pipeline and tape artefacts.
- https://github.com/programandala-net/abersoft-forth/blob/36af6cb80bbb69b0d25c10f77d3a5345763bd9d2/README.adoc

### Source CPU (reviewed)

Source architecture: Z80. No minimum CPU inferred.
- https://github.com/programandala-net/abersoft-forth/blob/36af6cb80bbb69b0d25c10f77d3a5345763bd9d2/README.adoc

### Target CPU (reviewed)

Target architecture: Z80. This is not a verified minimum CPU for every frontend.
- https://github.com/programandala-net/abersoft-forth/blob/36af6cb80bbb69b0d25c10f77d3a5345763bd9d2/README.adoc

### Build (reviewed)

Pasmo, z80dasm, Make and related tools are documented; no independent build or byte comparison. Source-only review: no independent compilation, execution, gameplay or byte comparison.
- https://github.com/programandala-net/abersoft-forth/blob/36af6cb80bbb69b0d25c10f77d3a5345763bd9d2/README.adoc

### Runtime profiles (no-evidence-found)

Documented dependencies and bounds are recorded in build notes; no independently verified complete runtime profile.
- https://github.com/programandala-net/abersoft-forth/blob/36af6cb80bbb69b0d25c10f77d3a5345763bd9d2/README.adoc

### AI (no-evidence-found)

No actual development-AI contribution established in the inspected evidence. Missing attribution is not evidence of non-use.
- https://github.com/programandala-net/abersoft-forth/blob/36af6cb80bbb69b0d25c10f77d3a5345763bd9d2/README.adoc

### Relationships (reviewed)

Preserves a historic Forth implementation, rather than being a new language interpreter.
- https://github.com/programandala-net/abersoft-forth/blob/36af6cb80bbb69b0d25c10f77d3a5345763bd9d2/README.adoc

## H.A.T.E. — ZX Spectrum disassembly and analysis

Project ID: escoman-zx-disasm · Overall audit: partial

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
  "display_title": "H.A.T.E. — ZX Spectrum disassembly and analysis",
  "id": "escoman-zx-disasm",
  "last_activity": null,
  "last_checked": "2026-11-04",
  "re_started": null,
  "reconstructed_languages": [
    "Z80 assembly",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/escoman/zx-disasm",
  "runtime_profiles": [],
  "source_cpu": [
    "Z80"
  ],
  "source_language": [],
  "source_platforms": [
    "ZX Spectrum"
  ],
  "status": "Source inspected; no independent build or execution",
  "subjects": [
    "H.A.T.E."
  ],
  "tags": [],
  "target_cpu": [
    "Z80"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "ZX Spectrum"
  ],
  "techniques": [],
  "title": "H.A.T.E. — ZX Spectrum disassembly and analysis",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "zx-disasm",
  "work_kinds": [
    "disassembly",
    "binary-analysis",
    "data-format-analysis"
  ]
}
```

### Identity (reviewed)

H.A.T.E. — ZX Spectrum disassembly and analysis. Pinned repository, documentation and selected implementation inspected.
- https://github.com/escoman/zx-disasm/blob/50bf75f25bc88862beb3b789a00a0841fa30d814/README.md
- https://github.com/escoman/zx-disasm/blob/50bf75f25bc88862beb3b789a00a0841fa30d814/games/hate/README.md

### Classification (reviewed)

Repository-wide Spectrum reverse engineering effort currently centered on H.A.T.E. (1989), with separate title and resident-engine listings, coverage traces and notes on input, graphics and game data. A Vector-06C port is a stated goal, not an established finished target.
- https://github.com/escoman/zx-disasm/blob/50bf75f25bc88862beb3b789a00a0841fa30d814/README.md
- https://github.com/escoman/zx-disasm/blob/50bf75f25bc88862beb3b789a00a0841fa30d814/games/hate/README.md

### Source CPU (reviewed)

Source architecture: Z80. No minimum CPU inferred.
- https://github.com/escoman/zx-disasm/blob/50bf75f25bc88862beb3b789a00a0841fa30d814/README.md
- https://github.com/escoman/zx-disasm/blob/50bf75f25bc88862beb3b789a00a0841fa30d814/games/hate/README.md

### Target CPU (reviewed)

Target architecture: Z80. This is not a verified minimum CPU for every frontend.
- https://github.com/escoman/zx-disasm/blob/50bf75f25bc88862beb3b789a00a0841fa30d814/README.md
- https://github.com/escoman/zx-disasm/blob/50bf75f25bc88862beb3b789a00a0841fa30d814/games/hate/README.md

### Build (reviewed)

Project documents SkoolKit-generated listings and simulated execution traces; no independent rebuild, gameplay test or completeness verification. Source-only review: no independent compilation, execution, gameplay or byte comparison.
- https://github.com/escoman/zx-disasm/blob/50bf75f25bc88862beb3b789a00a0841fa30d814/README.md
- https://github.com/escoman/zx-disasm/blob/50bf75f25bc88862beb3b789a00a0841fa30d814/games/hate/README.md

### Runtime profiles (no-evidence-found)

Documented dependencies and bounds are recorded in build notes; no independently verified complete runtime profile.
- https://github.com/escoman/zx-disasm/blob/50bf75f25bc88862beb3b789a00a0841fa30d814/README.md
- https://github.com/escoman/zx-disasm/blob/50bf75f25bc88862beb3b789a00a0841fa30d814/games/hate/README.md

### AI (no-evidence-found)

No actual development-AI contribution established in the inspected evidence. Missing attribution is not evidence of non-use.
- https://github.com/escoman/zx-disasm/blob/50bf75f25bc88862beb3b789a00a0841fa30d814/README.md
- https://github.com/escoman/zx-disasm/blob/50bf75f25bc88862beb3b789a00a0841fa30d814/games/hate/README.md

### Relationships (reviewed)

Repository root represents the overall multi-game analysis project, currently centered on H.A.T.E.
- https://github.com/escoman/zx-disasm/blob/50bf75f25bc88862beb3b789a00a0841fa30d814/README.md
- https://github.com/escoman/zx-disasm/blob/50bf75f25bc88862beb3b789a00a0841fa30d814/games/hate/README.md

## Chuckie Egg 2 — Spectrum-derived browser reimplementation

Project ID: cookertron-chuckie-egg-2-js · Overall audit: partial

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
  "display_title": "Chuckie Egg 2 — Spectrum-derived browser reimplementation",
  "id": "cookertron-chuckie-egg-2-js",
  "last_activity": null,
  "last_checked": "2026-11-04",
  "re_started": null,
  "reconstructed_languages": [
    "JavaScript"
  ],
  "record_class": "subject",
  "repo": "https://github.com/cookertron/Chuckie-Egg-2-JS",
  "runtime_profiles": [],
  "source_cpu": [
    "Z80"
  ],
  "source_language": [],
  "source_platforms": [
    "ZX Spectrum"
  ],
  "status": "Source inspected; no independent build or execution",
  "subjects": [
    "Chuckie Egg 2"
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
  "title": "Chuckie Egg 2 — Spectrum-derived browser reimplementation",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "Chuckie-Egg-2-JS",
  "work_kinds": [
    "reimplementation",
    "reverse-engineering-derived-port"
  ]
}
```

### Identity (reviewed)

Chuckie Egg 2 — Spectrum-derived browser reimplementation. Pinned repository, documentation and selected implementation inspected.
- https://github.com/cookertron/Chuckie-Egg-2-JS/blob/33b30b90372341a776004b211e77473e40d1c99f/README.md

### Classification (reviewed)

Browser engine written from disassembly of the Spectrum game, with reported differential test vectors. Author documents missing Spectrum ROM font, original front end, and a complete end-to-end playthrough. The current repository tree provides generated HTML and an archive rather than the source/build tree described in the README.
- https://github.com/cookertron/Chuckie-Egg-2-JS/blob/33b30b90372341a776004b211e77473e40d1c99f/README.md

### Source CPU (reviewed)

Source architecture: Z80. No minimum CPU inferred.
- https://github.com/cookertron/Chuckie-Egg-2-JS/blob/33b30b90372341a776004b211e77473e40d1c99f/README.md

### Target CPU (no-evidence-found)

No physical target CPU minimum established; portability or a managed runtime is not a hardware requirement.
- https://github.com/cookertron/Chuckie-Egg-2-JS/blob/33b30b90372341a776004b211e77473e40d1c99f/README.md

### Build (reviewed)

The present tree does not expose the referenced build/test scripts; no independent execution or comparison. Source-only review: no independent compilation, execution, gameplay or byte comparison.
- https://github.com/cookertron/Chuckie-Egg-2-JS/blob/33b30b90372341a776004b211e77473e40d1c99f/README.md

### Runtime profiles (no-evidence-found)

Documented dependencies and bounds are recorded in build notes; no independently verified complete runtime profile.
- https://github.com/cookertron/Chuckie-Egg-2-JS/blob/33b30b90372341a776004b211e77473e40d1c99f/README.md

### AI (no-evidence-found)

No actual development-AI contribution established in the inspected evidence. Missing attribution is not evidence of non-use.
- https://github.com/cookertron/Chuckie-Egg-2-JS/blob/33b30b90372341a776004b211e77473e40d1c99f/README.md

### Relationships (reviewed)

A browser rewrite without original Z80 execution; do not conflate it with separate Chuckie Egg 2 platform ports.
- https://github.com/cookertron/Chuckie-Egg-2-JS/blob/33b30b90372341a776004b211e77473e40d1c99f/README.md

## MOTION VM — DOS adventure engine reconstruction

Project ID: wdominik-motionvm · Overall audit: partial

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
  "display_title": "MOTION VM — DOS adventure engine reconstruction",
  "id": "wdominik-motionvm",
  "last_activity": null,
  "last_checked": "2026-11-04",
  "re_started": null,
  "reconstructed_languages": [
    "Rust"
  ],
  "record_class": "subject",
  "repo": "https://github.com/wdominik/motionvm",
  "runtime_profiles": [],
  "source_cpu": [
    "x86"
  ],
  "source_language": [],
  "source_platforms": [
    "DOS"
  ],
  "status": "Source inspected; no independent build or execution",
  "subjects": [
    "MOTION VM"
  ],
  "tags": [],
  "target_cpu": [],
  "target_kinds": [
    "game-engine"
  ],
  "target_platforms": [
    "Windows",
    "macOS",
    "Linux"
  ],
  "techniques": [],
  "title": "MOTION VM — DOS adventure engine reconstruction",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "motionvm",
  "work_kinds": [
    "reimplementation",
    "data-format-analysis"
  ]
}
```

### Identity (reviewed)

MOTION VM — DOS adventure engine reconstruction. Pinned repository, documentation and selected implementation inspected.
- https://github.com/wdominik/motionvm/blob/a05e7a5400633b3f18de3efb3d583d056e1e7fdb/README.md

### Classification (reviewed)

From-scratch Rust implementation of both MOTION engine generations for several German DOS adventures; reads user-provided game data. The author documents compatibility and testing per title.
- https://github.com/wdominik/motionvm/blob/a05e7a5400633b3f18de3efb3d583d056e1e7fdb/README.md

### Source CPU (reviewed)

Source architecture: x86. No minimum CPU inferred.
- https://github.com/wdominik/motionvm/blob/a05e7a5400633b3f18de3efb3d583d056e1e7fdb/README.md

### Target CPU (no-evidence-found)

No physical target CPU minimum established; portability or a managed runtime is not a hardware requirement.
- https://github.com/wdominik/motionvm/blob/a05e7a5400633b3f18de3efb3d583d056e1e7fdb/README.md

### Build (reviewed)

Cargo build and game-data requirement documented; compatibility claims are author reports, not independently verified. Source-only review: no independent compilation, execution, gameplay or byte comparison.
- https://github.com/wdominik/motionvm/blob/a05e7a5400633b3f18de3efb3d583d056e1e7fdb/README.md

### Runtime profiles (no-evidence-found)

Documented dependencies and bounds are recorded in build notes; no independently verified complete runtime profile.
- https://github.com/wdominik/motionvm/blob/a05e7a5400633b3f18de3efb3d583d056e1e7fdb/README.md

### AI (no-evidence-found)

No actual development-AI contribution established in the inspected evidence. Missing attribution is not evidence of non-use.
- https://github.com/wdominik/motionvm/blob/a05e7a5400633b3f18de3efb3d583d056e1e7fdb/README.md

### Relationships (reviewed)

A multi-game engine replacement, not original MOTION source.
- https://github.com/wdominik/motionvm/blob/a05e7a5400633b3f18de3efb3d583d056e1e7fdb/README.md

## OpenBlood — Blood DOS engine reimplementation

Project ID: dagrigorev-openblood · Overall audit: partial

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
  "display_title": "OpenBlood — Blood DOS engine reimplementation",
  "id": "dagrigorev-openblood",
  "last_activity": null,
  "last_checked": "2026-11-04",
  "re_started": null,
  "reconstructed_languages": [
    "Rust"
  ],
  "record_class": "subject",
  "repo": "https://github.com/dagrigorev/OpenBlood",
  "runtime_profiles": [],
  "source_cpu": [
    "x86"
  ],
  "source_language": [],
  "source_platforms": [
    "DOS"
  ],
  "status": "Source inspected; no independent build or execution",
  "subjects": [
    "OpenBlood"
  ],
  "tags": [],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Windows",
    "macOS",
    "Linux"
  ],
  "techniques": [],
  "title": "OpenBlood — Blood DOS engine reimplementation",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "OpenBlood",
  "work_kinds": [
    "reimplementation",
    "data-format-analysis"
  ]
}
```

### Identity (reviewed)

OpenBlood — Blood DOS engine reimplementation. Pinned repository, documentation and selected implementation inspected.
- https://github.com/dagrigorev/OpenBlood/blob/a6d6e8cd55413e6c21625fd6f46c9ec8dd573e81/README.md

### Classification (reviewed)

Independent Rust implementation of Blood (1997), including data readers, rendering and gameplay. The author says multiplayer and portions of enemy behaviour remain unfinished; original game assets are required.
- https://github.com/dagrigorev/OpenBlood/blob/a6d6e8cd55413e6c21625fd6f46c9ec8dd573e81/README.md

### Source CPU (reviewed)

Source architecture: x86. No minimum CPU inferred.
- https://github.com/dagrigorev/OpenBlood/blob/a6d6e8cd55413e6c21625fd6f46c9ec8dd573e81/README.md

### Target CPU (no-evidence-found)

No physical target CPU minimum established; portability or a managed runtime is not a hardware requirement.
- https://github.com/dagrigorev/OpenBlood/blob/a6d6e8cd55413e6c21625fd6f46c9ec8dd573e81/README.md

### Build (reviewed)

Cargo-based engine and asset dependency documented; no independent build or gameplay test. Source-only review: no independent compilation, execution, gameplay or byte comparison.
- https://github.com/dagrigorev/OpenBlood/blob/a6d6e8cd55413e6c21625fd6f46c9ec8dd573e81/README.md

### Runtime profiles (no-evidence-found)

Documented dependencies and bounds are recorded in build notes; no independently verified complete runtime profile.
- https://github.com/dagrigorev/OpenBlood/blob/a6d6e8cd55413e6c21625fd6f46c9ec8dd573e81/README.md

### AI (no-evidence-found)

No actual development-AI contribution established in the inspected evidence. Missing attribution is not evidence of non-use.
- https://github.com/dagrigorev/OpenBlood/blob/a6d6e8cd55413e6c21625fd6f46c9ec8dd573e81/README.md

### Relationships (reviewed)

Distinct from other Blood source ports; not a claim of recovered original source.
- https://github.com/dagrigorev/OpenBlood/blob/a6d6e8cd55413e6c21625fd6f46c9ec8dd573e81/README.md

## Tomb Raider — matching DOS decompilation

Project ID: lostartefacts-tr01 · Overall audit: partial

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
  "display_title": "Tomb Raider — matching DOS decompilation",
  "id": "lostartefacts-tr01",
  "last_activity": null,
  "last_checked": "2026-11-04",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "x86 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/LostArtefacts/tr01",
  "runtime_profiles": [],
  "source_cpu": [
    "x86"
  ],
  "source_language": [],
  "source_platforms": [
    "DOS"
  ],
  "status": "Source inspected; no independent build or execution",
  "subjects": [
    "Tomb Raider"
  ],
  "tags": [],
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
  "title": "Tomb Raider — matching DOS decompilation",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "tr01",
  "work_kinds": [
    "decompilation",
    "source-reconstruction"
  ]
}
```

### Identity (reviewed)

Tomb Raider — matching DOS decompilation. Pinned repository, documentation and selected implementation inspected.
- https://github.com/LostArtefacts/tr01/blob/779857045b193475bf6cd494f9c545d25656d8df/README.md

### Classification (reviewed)

Matching reconstruction of the 1996 DOS executable, informed by later Windows game source and Ghidra analysis. Unrecovered code is taken from the original during development; the project does not claim all functions already match.
- https://github.com/LostArtefacts/tr01/blob/779857045b193475bf6cd494f9c545d25656d8df/README.md

### Source CPU (reviewed)

Source architecture: x86. No minimum CPU inferred.
- https://github.com/LostArtefacts/tr01/blob/779857045b193475bf6cd494f9c545d25656d8df/README.md

### Target CPU (reviewed)

Target architecture: x86. This is not a verified minimum CPU for every frontend.
- https://github.com/LostArtefacts/tr01/blob/779857045b193475bf6cd494f9c545d25656d8df/README.md

### Build (reviewed)

Documents Watcom and MASM toolchain, per-function byte comparisons and user-supplied game files. No independent build or byte verification. Source-only review: no independent compilation, execution, gameplay or byte comparison.
- https://github.com/LostArtefacts/tr01/blob/779857045b193475bf6cd494f9c545d25656d8df/README.md

### Runtime profiles (no-evidence-found)

Documented dependencies and bounds are recorded in build notes; no independently verified complete runtime profile.
- https://github.com/LostArtefacts/tr01/blob/779857045b193475bf6cd494f9c545d25656d8df/README.md

### AI (no-evidence-found)

No actual development-AI contribution established in the inspected evidence. Missing attribution is not evidence of non-use.
- https://github.com/LostArtefacts/tr01/blob/779857045b193475bf6cd494f9c545d25656d8df/README.md

### Relationships (reviewed)

Related to other Lost Artefacts projects, but specifically targets the DOS executable and is not clean-room.
- https://github.com/LostArtefacts/tr01/blob/779857045b193475bf6cd494f9c545d25656d8df/README.md

## Disassembler6510 — C64 disassembly toolkit

Project ID: geert-jan77-disassembler6510 · Overall audit: partial

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
  "display_title": "Disassembler6510 — C64 disassembly toolkit",
  "id": "geert-jan77-disassembler6510",
  "last_activity": null,
  "last_checked": "2026-11-04",
  "re_started": null,
  "reconstructed_languages": [
    "C"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/Geert-Jan77/Disassembler6510",
  "runtime_profiles": [],
  "source_cpu": [
    "6502"
  ],
  "source_language": [],
  "source_platforms": [
    "Commodore 64"
  ],
  "status": "Source inspected; no independent build or execution",
  "subjects": [
    "Disassembler6510"
  ],
  "tags": [],
  "target_cpu": [],
  "target_kinds": [],
  "target_platforms": [
    "Commodore 64",
    "Windows"
  ],
  "techniques": [],
  "title": "Disassembler6510 — C64 disassembly toolkit",
  "tool_kinds": [
    "disassembler",
    "assembler-toolchain"
  ],
  "types": [
    "tooling"
  ],
  "upstream_name": "Disassembler6510",
  "work_kinds": [
    "binary-analysis"
  ]
}
```

### Identity (reviewed)

Disassembler6510 — C64 disassembly toolkit. Pinned repository, documentation and selected implementation inspected.
- https://github.com/Geert-Jan77/Disassembler6510/blob/be69f273f92950142b1301ed55b7611d8b963257/README.md

### Classification (reviewed)

Small 6510 disassembler with a companion assembler and help/data utilities, targeting C64 machine code and documented C64/Windows workflows.
- https://github.com/Geert-Jan77/Disassembler6510/blob/be69f273f92950142b1301ed55b7611d8b963257/README.md

### Source CPU (reviewed)

Source architecture: 6502. No minimum CPU inferred.
- https://github.com/Geert-Jan77/Disassembler6510/blob/be69f273f92950142b1301ed55b7611d8b963257/README.md

### Target CPU (no-evidence-found)

No physical target CPU minimum established; portability or a managed runtime is not a hardware requirement.
- https://github.com/Geert-Jan77/Disassembler6510/blob/be69f273f92950142b1301ed55b7611d8b963257/README.md

### Build (reviewed)

Source and Windows/C64 build instructions present; no independent compilation or reconstruction test. Source-only review: no independent compilation, execution, gameplay or byte comparison.
- https://github.com/Geert-Jan77/Disassembler6510/blob/be69f273f92950142b1301ed55b7611d8b963257/README.md

### Runtime profiles (no-evidence-found)

Documented dependencies and bounds are recorded in build notes; no independently verified complete runtime profile.
- https://github.com/Geert-Jan77/Disassembler6510/blob/be69f273f92950142b1301ed55b7611d8b963257/README.md

### AI (no-evidence-found)

No actual development-AI contribution established in the inspected evidence. Missing attribution is not evidence of non-use.
- https://github.com/Geert-Jan77/Disassembler6510/blob/be69f273f92950142b1301ed55b7611d8b963257/README.md

### Relationships (reviewed)

General archaeology tooling, not the reconstruction of a specific game.
- https://github.com/Geert-Jan77/Disassembler6510/blob/be69f273f92950142b1301ed55b7611d8b963257/README.md

## DOS HLE Kit — executable analysis framework

Project ID: mitigd-dos-hle-kit · Overall audit: partial

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
  "display_title": "DOS HLE Kit — executable analysis framework",
  "id": "mitigd-dos-hle-kit",
  "last_activity": null,
  "last_checked": "2026-11-04",
  "re_started": null,
  "reconstructed_languages": [
    "C++",
    "Python"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/mitigd/dos-hle-kit",
  "runtime_profiles": [],
  "source_cpu": [
    "x86"
  ],
  "source_language": [],
  "source_platforms": [
    "DOS"
  ],
  "status": "Source inspected; no independent build or execution",
  "subjects": [
    "DOS HLE Kit"
  ],
  "tags": [],
  "target_cpu": [
    "x86"
  ],
  "target_kinds": [],
  "target_platforms": [
    "Linux"
  ],
  "techniques": [],
  "title": "DOS HLE Kit — executable analysis framework",
  "tool_kinds": [
    "binary-analysis",
    "emulator",
    "static-analysis"
  ],
  "types": [
    "tooling"
  ],
  "upstream_name": "dos-hle-kit",
  "work_kinds": [
    "binary-analysis"
  ]
}
```

### Identity (reviewed)

DOS HLE Kit — executable analysis framework. Pinned repository, documentation and selected implementation inspected.
- https://github.com/mitigd/dos-hle-kit/blob/81da44189d735e75e7598d686454515540f7e158/README.md

### Classification (reviewed)

General-purpose DOS executable research and function-level high-level-emulation toolkit. It runs remaining original x86 code via KVM or a JIT while replacing selected hardware-facing routines; it is not a recovered game engine.
- https://github.com/mitigd/dos-hle-kit/blob/81da44189d735e75e7598d686454515540f7e158/README.md

### Source CPU (reviewed)

Source architecture: x86. No minimum CPU inferred.
- https://github.com/mitigd/dos-hle-kit/blob/81da44189d735e75e7598d686454515540f7e158/README.md

### Target CPU (reviewed)

Target architecture: x86. This is not a verified minimum CPU for every frontend.
- https://github.com/mitigd/dos-hle-kit/blob/81da44189d735e75e7598d686454515540f7e158/README.md

### Build (reviewed)

Meson/Ninja, SDL and x86-64 host requirements documented; no independent build or execution. Source-only review: no independent compilation, execution, gameplay or byte comparison.
- https://github.com/mitigd/dos-hle-kit/blob/81da44189d735e75e7598d686454515540f7e158/README.md

### Runtime profiles (no-evidence-found)

Documented dependencies and bounds are recorded in build notes; no independently verified complete runtime profile.
- https://github.com/mitigd/dos-hle-kit/blob/81da44189d735e75e7598d686454515540f7e158/README.md

### AI (no-evidence-found)

No actual development-AI contribution established in the inspected evidence. Missing attribution is not evidence of non-use.
- https://github.com/mitigd/dos-hle-kit/blob/81da44189d735e75e7598d686454515540f7e158/README.md

### Relationships (reviewed)

Generic reusable framework, distinguished from its separate game-specific baked-emulation examples.
- https://github.com/mitigd/dos-hle-kit/blob/81da44189d735e75e7598d686454515540f7e158/README.md

## The 5th Axis — C64-derived remaster

Project ID: virtualaaron09-oss-thefifthaxis-remaster · Overall audit: partial

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
  "display_title": "The 5th Axis — C64-derived remaster",
  "id": "virtualaaron09-oss-thefifthaxis-remaster",
  "last_activity": null,
  "last_checked": "2026-11-04",
  "re_started": null,
  "reconstructed_languages": [
    "C#"
  ],
  "record_class": "subject",
  "repo": "https://github.com/virtualaaron09-oss/TheFifthAxis-Remaster",
  "runtime_profiles": [],
  "source_cpu": [
    "6502"
  ],
  "source_language": [],
  "source_platforms": [
    "Commodore 64"
  ],
  "status": "Source inspected; no independent build or execution",
  "subjects": [
    "The 5th Axis"
  ],
  "tags": [],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [],
  "techniques": [],
  "title": "The 5th Axis — C64-derived remaster",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "TheFifthAxis-Remaster",
  "work_kinds": [
    "reimplementation",
    "data-format-analysis"
  ]
}
```

### Identity (reviewed)

The 5th Axis — C64-derived remaster. Pinned repository, documentation and selected implementation inspected.
- https://github.com/virtualaaron09-oss/TheFifthAxis-Remaster/blob/073b951090f00aec09a9aa855dbaaba131f1e270/README.md

### Classification (reviewed)

C# remaster whose author reports reverse engineering a C64 snapshot and extracting sprites, sound and game state. It deliberately changes rendering, timing, physics and audio; faithfulness and claimed completeness have not been verified.
- https://github.com/virtualaaron09-oss/TheFifthAxis-Remaster/blob/073b951090f00aec09a9aa855dbaaba131f1e270/README.md

### Source CPU (reviewed)

Source architecture: 6502. No minimum CPU inferred.
- https://github.com/virtualaaron09-oss/TheFifthAxis-Remaster/blob/073b951090f00aec09a9aa855dbaaba131f1e270/README.md

### Target CPU (no-evidence-found)

No physical target CPU minimum established; portability or a managed runtime is not a hardware requirement.
- https://github.com/virtualaaron09-oss/TheFifthAxis-Remaster/blob/073b951090f00aec09a9aa855dbaaba131f1e270/README.md

### Build (reviewed)

Source and .NET 10/Raylib project present; no independent build or game comparison. Source-only review: no independent compilation, execution, gameplay or byte comparison.
- https://github.com/virtualaaron09-oss/TheFifthAxis-Remaster/blob/073b951090f00aec09a9aa855dbaaba131f1e270/README.md

### Runtime profiles (no-evidence-found)

Documented dependencies and bounds are recorded in build notes; no independently verified complete runtime profile.
- https://github.com/virtualaaron09-oss/TheFifthAxis-Remaster/blob/073b951090f00aec09a9aa855dbaaba131f1e270/README.md

### AI (no-evidence-found)

No actual development-AI contribution established in the inspected evidence. Missing attribution is not evidence of non-use.
- https://github.com/virtualaaron09-oss/TheFifthAxis-Remaster/blob/073b951090f00aec09a9aa855dbaaba131f1e270/README.md

### Relationships (reviewed)

A modern reinterpretation, not a byte-exact C64 reconstruction.
- https://github.com/virtualaaron09-oss/TheFifthAxis-Remaster/blob/073b951090f00aec09a9aa855dbaaba131f1e270/README.md

## Treasure Island — Commodore Plus/4 reconstruction

Project ID: pbakota-tisland · Overall audit: partial

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
  "display_title": "Treasure Island — Commodore Plus/4 reconstruction",
  "id": "pbakota-tisland",
  "last_activity": null,
  "last_checked": "2026-11-04",
  "re_started": null,
  "reconstructed_languages": [
    "6502 assembly",
    "JavaScript"
  ],
  "record_class": "subject",
  "repo": "https://github.com/pbakota/tisland",
  "runtime_profiles": [],
  "source_cpu": [
    "6502"
  ],
  "source_language": [],
  "source_platforms": [
    "Commodore Plus/4"
  ],
  "status": "Source inspected; no independent build or execution",
  "subjects": [
    "Treasure Island"
  ],
  "tags": [],
  "target_cpu": [
    "6502"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Commodore Plus/4",
    "Web"
  ],
  "techniques": [],
  "title": "Treasure Island — Commodore Plus/4 reconstruction",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "tisland",
  "work_kinds": [
    "disassembly",
    "source-reconstruction",
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Treasure Island — Commodore Plus/4 reconstruction. Pinned repository, documentation and selected implementation inspected.
- https://github.com/pbakota/tisland/blob/788114485c2f7b4207bead0c89ac317de68ab5fe/README.md

### Classification (reviewed)

Reverse-engineered Plus/4 Treasure Island with reassemblable assembly, extracted graphics tooling and a separate JavaScript browser implementation. The enhanced version adds navigation and gameplay options.
- https://github.com/pbakota/tisland/blob/788114485c2f7b4207bead0c89ac317de68ab5fe/README.md

### Source CPU (reviewed)

Source architecture: 6502. No minimum CPU inferred.
- https://github.com/pbakota/tisland/blob/788114485c2f7b4207bead0c89ac317de68ab5fe/README.md

### Target CPU (reviewed)

Target architecture: 6502. This is not a verified minimum CPU for every frontend.
- https://github.com/pbakota/tisland/blob/788114485c2f7b4207bead0c89ac317de68ab5fe/README.md

### Build (reviewed)

KickAssembler and Make build documented; no independent assembly, gameplay or byte comparison. Source-only review: no independent compilation, execution, gameplay or byte comparison.
- https://github.com/pbakota/tisland/blob/788114485c2f7b4207bead0c89ac317de68ab5fe/README.md

### Runtime profiles (no-evidence-found)

Documented dependencies and bounds are recorded in build notes; no independently verified complete runtime profile.
- https://github.com/pbakota/tisland/blob/788114485c2f7b4207bead0c89ac317de68ab5fe/README.md

### AI (no-evidence-found)

No actual development-AI contribution established in the inspected evidence. Missing attribution is not evidence of non-use.
- https://github.com/pbakota/tisland/blob/788114485c2f7b4207bead0c89ac317de68ab5fe/README.md

### Relationships (reviewed)

Tracks the complete repository, including both original-platform disassembly and browser rewrite.
- https://github.com/pbakota/tisland/blob/788114485c2f7b4207bead0c89ac317de68ab5fe/README.md

## Pinned evidence manifest

- cookertron-chuckie-egg-2-js-readme-md: https://github.com/cookertron/chuckie-egg-2-js/blob/33b30b90372341a776004b211e77473e40d1c99f/README.md (Git blob cb75bc1c5b2c72898c066d3cc3ca5a0a91cfe132)
- dagrigorev-openblood-readme-md: https://github.com/dagrigorev/openblood/blob/a6d6e8cd55413e6c21625fd6f46c9ec8dd573e81/README.md (Git blob e8625287e62508f1068f80858f2fd243d151fca6)
- escoman-zx-disasm-games-hate-readme-md: https://github.com/escoman/zx-disasm/blob/50bf75f25bc88862beb3b789a00a0841fa30d814/games/hate/README.md (Git blob c193d1709f099418a7132133eefa209ad6dabfaf)
- escoman-zx-disasm-readme-md: https://github.com/escoman/zx-disasm/blob/50bf75f25bc88862beb3b789a00a0841fa30d814/README.md (Git blob 4f230e1fc72e7a854a88d6e8f9a9444b83775978)
- geert-jan77-disassembler6510-readme-md: https://github.com/geert-jan77/disassembler6510/blob/be69f273f92950142b1301ed55b7611d8b963257/README.md (Git blob f7f65543a2f91cc406733f32507de5ece6f04748)
- lostartefacts-tr01-readme-md: https://github.com/lostartefacts/tr01/blob/779857045b193475bf6cd494f9c545d25656d8df/README.md (Git blob 3c6a3d89f588a3a66499c02fa66cdf94b2f45edb)
- mitigd-dos-hle-kit-readme-md: https://github.com/mitigd/dos-hle-kit/blob/81da44189d735e75e7598d686454515540f7e158/README.md (Git blob b7b546e293978812d01cd3b35806d3604283e73e)
- oldcompcz-hisoft-c-readme-md: https://github.com/oldcompcz/hisoft-c/blob/a056f4eb2d36e846c173b2302560c91fb5c9093d/README.md (Git blob 315769f483d0ff3ff891a2d1a34d4897c136391b)
- pbakota-tisland-readme-md: https://github.com/pbakota/tisland/blob/788114485c2f7b4207bead0c89ac317de68ab5fe/README.md (Git blob 97c89cb02feaf84c6de6fc9b34f8ba2190ebd884)
- programandala-net-abersoft-forth-readme-adoc: https://github.com/programandala-net/abersoft-forth/blob/36af6cb80bbb69b0d25c10f77d3a5345763bd9d2/README.adoc (Git blob ff6e3b01b7b05bdfe31bfeb18db7f74b35125546)
- virtualaaron09-oss-thefifthaxis-remaster-readme-md: https://github.com/virtualaaron09-oss/thefifthaxis-remaster/blob/073b951090f00aec09a9aa855dbaaba131f1e270/README.md (Git blob 7f1c68e126d4db0cf8139fc6dbf99400bd419449)
- wdominik-motionvm-readme-md: https://github.com/wdominik/motionvm/blob/a05e7a5400633b3f18de3efb3d583d056e1e7fdb/README.md (Git blob a9a591ae6532c99e66d5065ab99d5fce9ad0c1ec)

## Sources

```json
[
  {
    "first_indexed": "2026-11-04",
    "id": "github-oldcompcz-hisoft-c",
    "kind": "github-repository",
    "last_reviewed": "2026-11-04",
    "open_task_ids": [],
    "projects_promoted": [
      "oldcompcz-hisoft-c"
    ],
    "reason": "Annotated Z80 reconstruction of the HiSoft C 1.3 compiler. The author describes byte-parity checks for the 25,600-byte compiler image and rebuilt tape; a separate explanatory C model omits the editor, media interface and resident runtime.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/oldcompcz/HiSoft-C"
  },
  {
    "first_indexed": "2026-11-04",
    "id": "github-programandala-net-abersoft-forth",
    "kind": "github-repository",
    "last_reviewed": "2026-11-04",
    "open_task_ids": [],
    "projects_promoted": [
      "programandala-net-abersoft-forth"
    ],
    "reason": "Annotated Z80 disassembly of Abersoft Forth with generated symbols and tools written in the Forth system itself. Repository contains a rebuild pipeline and tape artefacts.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/programandala-net/abersoft-forth"
  },
  {
    "first_indexed": "2026-11-04",
    "id": "github-escoman-zx-disasm",
    "kind": "github-repository",
    "last_reviewed": "2026-11-04",
    "open_task_ids": [],
    "projects_promoted": [
      "escoman-zx-disasm"
    ],
    "reason": "Repository-wide Spectrum reverse engineering effort currently centered on H.A.T.E. (1989), with separate title and resident-engine listings, coverage traces and notes on input, graphics and game data. A Vector-06C port is a stated goal, not an established finished target.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/escoman/zx-disasm"
  },
  {
    "first_indexed": "2026-11-04",
    "id": "github-cookertron-chuckie-egg-2-js",
    "kind": "github-repository",
    "last_reviewed": "2026-11-04",
    "open_task_ids": [],
    "projects_promoted": [
      "cookertron-chuckie-egg-2-js"
    ],
    "reason": "Browser engine written from disassembly of the Spectrum game, with reported differential test vectors. Author documents missing Spectrum ROM font, original front end, and a complete end-to-end playthrough. The current repository tree provides generated HTML and an archive rather than the source/build tree described in the README.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/cookertron/Chuckie-Egg-2-JS"
  },
  {
    "first_indexed": "2026-11-04",
    "id": "github-wdominik-motionvm",
    "kind": "github-repository",
    "last_reviewed": "2026-11-04",
    "open_task_ids": [],
    "projects_promoted": [
      "wdominik-motionvm"
    ],
    "reason": "From-scratch Rust implementation of both MOTION engine generations for several German DOS adventures; reads user-provided game data. The author documents compatibility and testing per title.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/wdominik/motionvm"
  },
  {
    "first_indexed": "2026-11-04",
    "id": "github-dagrigorev-openblood",
    "kind": "github-repository",
    "last_reviewed": "2026-11-04",
    "open_task_ids": [],
    "projects_promoted": [
      "dagrigorev-openblood"
    ],
    "reason": "Independent Rust implementation of Blood (1997), including data readers, rendering and gameplay. The author says multiplayer and portions of enemy behaviour remain unfinished; original game assets are required.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/dagrigorev/OpenBlood"
  },
  {
    "first_indexed": "2026-11-04",
    "id": "github-lostartefacts-tr01",
    "kind": "github-repository",
    "last_reviewed": "2026-11-04",
    "open_task_ids": [],
    "projects_promoted": [
      "lostartefacts-tr01"
    ],
    "reason": "Matching reconstruction of the 1996 DOS executable, informed by later Windows game source and Ghidra analysis. Unrecovered code is taken from the original during development; the project does not claim all functions already match.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/LostArtefacts/tr01"
  },
  {
    "first_indexed": "2026-11-04",
    "id": "github-geert-jan77-disassembler6510",
    "kind": "github-repository",
    "last_reviewed": "2026-11-04",
    "open_task_ids": [],
    "projects_promoted": [
      "geert-jan77-disassembler6510"
    ],
    "reason": "Small 6510 disassembler with a companion assembler and help/data utilities, targeting C64 machine code and documented C64/Windows workflows.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/Geert-Jan77/Disassembler6510"
  },
  {
    "first_indexed": "2026-11-04",
    "id": "github-mitigd-dos-hle-kit",
    "kind": "github-repository",
    "last_reviewed": "2026-11-04",
    "open_task_ids": [],
    "projects_promoted": [
      "mitigd-dos-hle-kit"
    ],
    "reason": "General-purpose DOS executable research and function-level high-level-emulation toolkit. It runs remaining original x86 code via KVM or a JIT while replacing selected hardware-facing routines; it is not a recovered game engine.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/mitigd/dos-hle-kit"
  },
  {
    "first_indexed": "2026-11-04",
    "id": "github-virtualaaron09-oss-thefifthaxis-remaster",
    "kind": "github-repository",
    "last_reviewed": "2026-11-04",
    "open_task_ids": [],
    "projects_promoted": [
      "virtualaaron09-oss-thefifthaxis-remaster"
    ],
    "reason": "C# remaster whose author reports reverse engineering a C64 snapshot and extracting sprites, sound and game state. It deliberately changes rendering, timing, physics and audio; faithfulness and claimed completeness have not been verified.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/virtualaaron09-oss/TheFifthAxis-Remaster"
  },
  {
    "first_indexed": "2026-11-04",
    "id": "github-pbakota-tisland",
    "kind": "github-repository",
    "last_reviewed": "2026-11-04",
    "open_task_ids": [],
    "projects_promoted": [
      "pbakota-tisland"
    ],
    "reason": "Reverse-engineered Plus/4 Treasure Island with reassemblable assembly, extracted graphics tooling and a separate JavaScript browser implementation. The enhanced version adds navigation and gameplay options.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/pbakota/tisland"
  }
]
```

## Research event notes

Personally screened hundreds of repository search results against the catalogue, concentrating on C64, ZX Spectrum, Amiga, Atari ST, CPC and DOS/Windows. Reviewed pinned repository trees, documentation and selected source. Original source releases, reverse-engineered reimplementations and independent remakes are identified separately. No binaries or installers executed. No worker, branch or PR used.
