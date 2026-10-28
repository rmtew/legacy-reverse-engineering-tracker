# Dizzy series discovery: source, ports and reconstruction evidence

Review 24 Dizzy-related roots: add ten source/reconstruction projects; hold or exclude fourteen insufficient, derivative or unrelated candidates.

Date: 2026-10-28 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- ryanmallon-dizzy / Target CPU (no-evidence-found): No host CPU minimum established from inspected source.
- ryanmallon-dizzy / Build (reviewed): Source inspection only; no upstream game, installer, emulator, assembler or asset pipeline was run.
- ryanmallon-dizzy / Runtime profiles (no-evidence-found): Dependencies and limits are qualified in build notes; no independently verified runtime floor.
- ryanmallon-dizzy / AI (no-evidence-found): No actual development-AI contribution established in inspected evidence; missing attribution is not evidence of non-use.
- primo-malvado-dizzy-magicland-disassemble / Build (reviewed): Source inspection only; no upstream game, installer, emulator, assembler or asset pipeline was run.
- primo-malvado-dizzy-magicland-disassemble / Runtime profiles (no-evidence-found): Dependencies and limits are qualified in build notes; no independently verified runtime floor.
- primo-malvado-dizzy-magicland-disassemble / AI (no-evidence-found): No actual development-AI contribution established in inspected evidence; missing attribution is not evidence of non-use.
- picosonic-d3 / Build (reviewed): Source inspection only; no upstream game, installer, emulator, assembler or asset pipeline was run.
- picosonic-d3 / AI (no-evidence-found): No actual development-AI contribution established in inspected evidence; missing attribution is not evidence of non-use.
- nzeemin-bk0011m-dizzy1td-rev / Build (reviewed): Source inspection only; no upstream game, installer, emulator, assembler or asset pipeline was run.
- nzeemin-bk0011m-dizzy1td-rev / AI (no-evidence-found): No actual development-AI contribution established in inspected evidence; missing attribution is not evidence of non-use.
- chegleyev-dizzy3remake / Target CPU (no-evidence-found): No host CPU minimum established from inspected source.
- chegleyev-dizzy3remake / Build (reviewed): Source inspection only; no upstream game, installer, emulator, assembler or asset pipeline was run.
- chegleyev-dizzy3remake / Runtime profiles (no-evidence-found): Dependencies and limits are qualified in build notes; no independently verified runtime floor.
- chegleyev-dizzy3remake / AI (no-evidence-found): No actual development-AI contribution established in inspected evidence; missing attribution is not evidence of non-use.
- dev-vpa-dizzy-adventures-remake / Source CPU (no-evidence-found): No single original binary architecture established for this format/engine or multi-version recreation.
- dev-vpa-dizzy-adventures-remake / Target CPU (no-evidence-found): No host CPU minimum established from inspected source.
- dev-vpa-dizzy-adventures-remake / Build (reviewed): Source inspection only; no upstream game, installer, emulator, assembler or asset pipeline was run.
- dev-vpa-dizzy-adventures-remake / Runtime profiles (no-evidence-found): Dependencies and limits are qualified in build notes; no independently verified runtime floor.
- dev-vpa-dizzy-adventures-remake / AI (no-evidence-found): No actual development-AI contribution established in inspected evidence; missing attribution is not evidence of non-use.
- n0t4r0b0t-game-port-factory / Build (reviewed): Source inspection only; no upstream game, installer, emulator, assembler or asset pipeline was run.
- nzeemin-uknc-dizzylogcabin / Build (reviewed): Source inspection only; no upstream game, installer, emulator, assembler or asset pipeline was run.
- nzeemin-uknc-dizzylogcabin / Runtime profiles (no-evidence-found): Dependencies and limits are qualified in build notes; no independently verified runtime floor.
- nzeemin-uknc-dizzylogcabin / AI (no-evidence-found): No actual development-AI contribution established in inspected evidence; missing attribution is not evidence of non-use.
- verm-v-ghastly-getaway-dizzy / Source CPU (no-evidence-found): No single original binary architecture established for this format/engine or multi-version recreation.
- verm-v-ghastly-getaway-dizzy / Build (reviewed): Source inspection only; no upstream game, installer, emulator, assembler or asset pipeline was run.
- verm-v-ghastly-getaway-dizzy / Runtime profiles (no-evidence-found): Dependencies and limits are qualified in build notes; no independently verified runtime floor.
- verm-v-ghastly-getaway-dizzy / AI (no-evidence-found): No actual development-AI contribution established in inspected evidence; missing attribution is not evidence of non-use.
- leprosarium-prolozzy / Source CPU (no-evidence-found): No single original binary architecture established for this format/engine or multi-version recreation.
- leprosarium-prolozzy / Target CPU (no-evidence-found): No host CPU minimum established from inspected source.
- leprosarium-prolozzy / Build (reviewed): Source inspection only; no upstream game, installer, emulator, assembler or asset pipeline was run.
- leprosarium-prolozzy / Runtime profiles (no-evidence-found): Dependencies and limits are qualified in build notes; no independently verified runtime floor.
- leprosarium-prolozzy / AI (no-evidence-found): No actual development-AI contribution established in inspected evidence; missing attribution is not evidence of non-use.

## Fantastic Dizzy — DOS resource reversing tools

Project ID: ryanmallon-dizzy · Overall audit: partial

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
  "display_title": "Fantastic Dizzy — DOS resource reversing tools",
  "id": "ryanmallon-dizzy",
  "last_activity": null,
  "last_checked": "2026-10-28",
  "re_started": null,
  "reconstructed_languages": [
    "Python"
  ],
  "record_class": "hybrid",
  "repo": "https://github.com/RyanMallon/dizzy",
  "runtime_profiles": [],
  "source_cpu": [
    "x86"
  ],
  "source_language": [
    "Python"
  ],
  "source_platforms": [
    "DOS"
  ],
  "status": "Source inspected; no independent build or execution",
  "subjects": [
    "Fantastic Dizzy"
  ],
  "tags": [
    "Dizzy"
  ],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [],
  "techniques": [],
  "title": "Fantastic Dizzy — DOS resource reversing tools",
  "tool_kinds": [
    "asset-tool"
  ],
  "types": [
    "hybrid"
  ],
  "upstream_name": "dizzy",
  "work_kinds": [
    "data-format-analysis"
  ]
}
```

### Identity (reviewed)

Fantastic Dizzy — DOS resource reversing tools. Repository root and implementation inspected.
- https://github.com/RyanMallon/dizzy/blob/3e28cfbdcda36b5ae8b36d0c2a5b90dc849705d2/README.md
- https://github.com/RyanMallon/dizzy/blob/3e28cfbdcda36b5ae8b36d0c2a5b90dc849705d2/dizzy_pack.py
- https://github.com/RyanMallon/dizzy/blob/3e28cfbdcda36b5ae8b36d0c2a5b90dc849705d2/stage_view.py

### Classification (reviewed)

Documented NDX/RES chunk indexes and variable-bit dictionary decompression, unpack/repack scripts, sprite and layered-stage viewers. This is original game resource analysis, not a reconstructed playable engine.
- https://github.com/RyanMallon/dizzy/blob/3e28cfbdcda36b5ae8b36d0c2a5b90dc849705d2/README.md
- https://github.com/RyanMallon/dizzy/blob/3e28cfbdcda36b5ae8b36d0c2a5b90dc849705d2/dizzy_pack.py
- https://github.com/RyanMallon/dizzy/blob/3e28cfbdcda36b5ae8b36d0c2a5b90dc849705d2/stage_view.py

### Source CPU (reviewed)

Original/source architecture: x86.
- https://github.com/RyanMallon/dizzy/blob/3e28cfbdcda36b5ae8b36d0c2a5b90dc849705d2/README.md
- https://github.com/RyanMallon/dizzy/blob/3e28cfbdcda36b5ae8b36d0c2a5b90dc849705d2/dizzy_pack.py
- https://github.com/RyanMallon/dizzy/blob/3e28cfbdcda36b5ae8b36d0c2a5b90dc849705d2/stage_view.py

### Target CPU (no-evidence-found)

No host CPU minimum established from inspected source.
- https://github.com/RyanMallon/dizzy/blob/3e28cfbdcda36b5ae8b36d0c2a5b90dc849705d2/README.md
- https://github.com/RyanMallon/dizzy/blob/3e28cfbdcda36b5ae8b36d0c2a5b90dc849705d2/dizzy_pack.py
- https://github.com/RyanMallon/dizzy/blob/3e28cfbdcda36b5ae8b36d0c2a5b90dc849705d2/stage_view.py

### Build (reviewed)

Legacy Python byte/string conventions and pygame viewers; requires original DOS NDX/RES files. Some tile palette encoding remains unknown and sprite colours may differ by stage. No independent execution. Limitations: Source inspection only; no upstream game, installer, emulator, assembler or asset pipeline was run.
- https://github.com/RyanMallon/dizzy/blob/3e28cfbdcda36b5ae8b36d0c2a5b90dc849705d2/README.md
- https://github.com/RyanMallon/dizzy/blob/3e28cfbdcda36b5ae8b36d0c2a5b90dc849705d2/dizzy_pack.py
- https://github.com/RyanMallon/dizzy/blob/3e28cfbdcda36b5ae8b36d0c2a5b90dc849705d2/stage_view.py

### Runtime profiles (no-evidence-found)

Dependencies and limits are qualified in build notes; no independently verified runtime floor.
- https://github.com/RyanMallon/dizzy/blob/3e28cfbdcda36b5ae8b36d0c2a5b90dc849705d2/README.md
- https://github.com/RyanMallon/dizzy/blob/3e28cfbdcda36b5ae8b36d0c2a5b90dc849705d2/dizzy_pack.py
- https://github.com/RyanMallon/dizzy/blob/3e28cfbdcda36b5ae8b36d0c2a5b90dc849705d2/stage_view.py

### AI (no-evidence-found)

No actual development-AI contribution established in inspected evidence; missing attribution is not evidence of non-use.
- https://github.com/RyanMallon/dizzy/blob/3e28cfbdcda36b5ae8b36d0c2a5b90dc849705d2/README.md
- https://github.com/RyanMallon/dizzy/blob/3e28cfbdcda36b5ae8b36d0c2a5b90dc849705d2/dizzy_pack.py
- https://github.com/RyanMallon/dizzy/blob/3e28cfbdcda36b5ae8b36d0c2a5b90dc849705d2/stage_view.py

### Relationships (reviewed)

Distinct from madmoose/dizzy, the general DOS EXE disassembler. Ryan Mallon describes the resource research separately; repacking writes uncompressed chunks accepted by the original game.
- https://github.com/RyanMallon/dizzy/blob/3e28cfbdcda36b5ae8b36d0c2a5b90dc849705d2/README.md
- https://github.com/RyanMallon/dizzy/blob/3e28cfbdcda36b5ae8b36d0c2a5b90dc849705d2/dizzy_pack.py
- https://github.com/RyanMallon/dizzy/blob/3e28cfbdcda36b5ae8b36d0c2a5b90dc849705d2/stage_view.py

## Magicland Dizzy — annotated Spectrum disassembly

Project ID: primo-malvado-dizzy-magicland-disassemble · Overall audit: partial

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
  "display_title": "Magicland Dizzy — annotated Spectrum disassembly",
  "id": "primo-malvado-dizzy-magicland-disassemble",
  "last_activity": null,
  "last_checked": "2026-10-28",
  "re_started": null,
  "reconstructed_languages": [
    "Z80 assembly",
    "Perl"
  ],
  "record_class": "subject",
  "repo": "https://github.com/primo-malvado/dizzy_magicland_disassemble",
  "runtime_profiles": [],
  "source_cpu": [
    "z80"
  ],
  "source_language": [
    "Z80 assembly",
    "Perl"
  ],
  "source_platforms": [
    "ZX Spectrum"
  ],
  "status": "Source inspected; no independent build or execution",
  "subjects": [
    "Magicland Dizzy"
  ],
  "tags": [
    "Dizzy"
  ],
  "target_cpu": [
    "z80"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "ZX Spectrum"
  ],
  "techniques": [],
  "title": "Magicland Dizzy — annotated Spectrum disassembly",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "dizzy_magicland_disassemble",
  "work_kinds": [
    "disassembly",
    "source-reconstruction"
  ]
}
```

### Identity (reviewed)

Magicland Dizzy — annotated Spectrum disassembly. Repository root and implementation inspected.
- https://github.com/primo-malvado/dizzy_magicland_disassemble/blob/e051974f967681968ca19876ecc5364a5175e01d/README.md
- https://github.com/primo-malvado/dizzy_magicland_disassemble/blob/e051974f967681968ca19876ecc5364a5175e01d/build/build.sh
- https://github.com/primo-malvado/dizzy_magicland_disassemble/blob/e051974f967681968ca19876ecc5364a5175e01d/desenha_sprite.asm
- https://github.com/primo-malvado/dizzy_magicland_disassemble/blob/e051974f967681968ca19876ecc5364a5175e01d/disassemble/disasemble_03_04.pl

### Classification (reviewed)

Game-specific code/data declarations identify map records, function indexes, sprite masks and named drawing operations. Generated and refactored assembly retain generic addresses and unknown regions, so semantic analysis is incomplete.
- https://github.com/primo-malvado/dizzy_magicland_disassemble/blob/e051974f967681968ca19876ecc5364a5175e01d/README.md
- https://github.com/primo-malvado/dizzy_magicland_disassemble/blob/e051974f967681968ca19876ecc5364a5175e01d/build/build.sh
- https://github.com/primo-malvado/dizzy_magicland_disassemble/blob/e051974f967681968ca19876ecc5364a5175e01d/desenha_sprite.asm
- https://github.com/primo-malvado/dizzy_magicland_disassemble/blob/e051974f967681968ca19876ecc5364a5175e01d/disassemble/disasemble_03_04.pl

### Source CPU (reviewed)

Original/source architecture: z80.
- https://github.com/primo-malvado/dizzy_magicland_disassemble/blob/e051974f967681968ca19876ecc5364a5175e01d/README.md
- https://github.com/primo-malvado/dizzy_magicland_disassemble/blob/e051974f967681968ca19876ecc5364a5175e01d/build/build.sh
- https://github.com/primo-malvado/dizzy_magicland_disassemble/blob/e051974f967681968ca19876ecc5364a5175e01d/desenha_sprite.asm
- https://github.com/primo-malvado/dizzy_magicland_disassemble/blob/e051974f967681968ca19876ecc5364a5175e01d/disassemble/disasemble_03_04.pl

### Target CPU (reviewed)

Native target architecture: z80.
- https://github.com/primo-malvado/dizzy_magicland_disassemble/blob/e051974f967681968ca19876ecc5364a5175e01d/README.md
- https://github.com/primo-malvado/dizzy_magicland_disassemble/blob/e051974f967681968ca19876ecc5364a5175e01d/build/build.sh
- https://github.com/primo-malvado/dizzy_magicland_disassemble/blob/e051974f967681968ca19876ecc5364a5175e01d/desenha_sprite.asm
- https://github.com/primo-malvado/dizzy_magicland_disassemble/blob/e051974f967681968ca19876ecc5364a5175e01d/disassemble/disasemble_03_04.pl

### Build (reviewed)

TAPut, Perl CPU::Z80::Disassembler, SJASMPlus and BAS2TAP workflow targets original-shaped TAP. The build script deletes dist binaries but leaves loader assembly commented while consuming dist/01.bin; clean-build success and byte identity are unverified. Limitations: Source inspection only; no upstream game, installer, emulator, assembler or asset pipeline was run.
- https://github.com/primo-malvado/dizzy_magicland_disassemble/blob/e051974f967681968ca19876ecc5364a5175e01d/README.md
- https://github.com/primo-malvado/dizzy_magicland_disassemble/blob/e051974f967681968ca19876ecc5364a5175e01d/build/build.sh
- https://github.com/primo-malvado/dizzy_magicland_disassemble/blob/e051974f967681968ca19876ecc5364a5175e01d/desenha_sprite.asm
- https://github.com/primo-malvado/dizzy_magicland_disassemble/blob/e051974f967681968ca19876ecc5364a5175e01d/disassemble/disasemble_03_04.pl

### Runtime profiles (no-evidence-found)

Dependencies and limits are qualified in build notes; no independently verified runtime floor.
- https://github.com/primo-malvado/dizzy_magicland_disassemble/blob/e051974f967681968ca19876ecc5364a5175e01d/README.md
- https://github.com/primo-malvado/dizzy_magicland_disassemble/blob/e051974f967681968ca19876ecc5364a5175e01d/build/build.sh
- https://github.com/primo-malvado/dizzy_magicland_disassemble/blob/e051974f967681968ca19876ecc5364a5175e01d/desenha_sprite.asm
- https://github.com/primo-malvado/dizzy_magicland_disassemble/blob/e051974f967681968ca19876ecc5364a5175e01d/disassemble/disasemble_03_04.pl

### AI (no-evidence-found)

No actual development-AI contribution established in inspected evidence; missing attribution is not evidence of non-use.
- https://github.com/primo-malvado/dizzy_magicland_disassemble/blob/e051974f967681968ca19876ecc5364a5175e01d/README.md
- https://github.com/primo-malvado/dizzy_magicland_disassemble/blob/e051974f967681968ca19876ecc5364a5175e01d/build/build.sh
- https://github.com/primo-malvado/dizzy_magicland_disassemble/blob/e051974f967681968ca19876ecc5364a5175e01d/desenha_sprite.asm
- https://github.com/primo-malvado/dizzy_magicland_disassemble/blob/e051974f967681968ca19876ecc5364a5175e01d/disassemble/disasemble_03_04.pl

### Relationships (reviewed)

Magicland only, not Treasure Island. A comparison script exists, but its presence is not a passing binary-equivalence result.
- https://github.com/primo-malvado/dizzy_magicland_disassemble/blob/e051974f967681968ca19876ecc5364a5175e01d/README.md
- https://github.com/primo-malvado/dizzy_magicland_disassemble/blob/e051974f967681968ca19876ecc5364a5175e01d/build/build.sh
- https://github.com/primo-malvado/dizzy_magicland_disassemble/blob/e051974f967681968ca19876ecc5364a5175e01d/desenha_sprite.asm
- https://github.com/primo-malvado/dizzy_magicland_disassemble/blob/e051974f967681968ca19876ecc5364a5175e01d/disassemble/disasemble_03_04.pl

## Fantasy World Dizzy — original Z80 source and BBC Micro port

Project ID: picosonic-d3 · Overall audit: partial

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
  "display_title": "Fantasy World Dizzy — original Z80 source and BBC Micro port",
  "id": "picosonic-d3",
  "last_activity": null,
  "last_checked": "2026-10-28",
  "re_started": null,
  "reconstructed_languages": [
    "Z80 assembly",
    "6502 assembly",
    "JavaScript",
    "C"
  ],
  "record_class": "subject",
  "repo": "https://github.com/picosonic/D3",
  "runtime_profiles": [],
  "source_cpu": [
    "z80",
    "6502"
  ],
  "source_language": [
    "Z80 assembly",
    "6502 assembly",
    "JavaScript",
    "C"
  ],
  "source_platforms": [
    "ZX Spectrum",
    "Amstrad CPC",
    "C64"
  ],
  "status": "Source inspected; no independent build or execution",
  "subjects": [
    "Fantasy World Dizzy"
  ],
  "tags": [
    "Dizzy"
  ],
  "target_cpu": [
    "6502"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "BBC Micro",
    "BBC Master"
  ],
  "techniques": [],
  "title": "Fantasy World Dizzy — original Z80 source and BBC Micro port",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "D3",
  "work_kinds": [
    "source-restoration",
    "reverse-engineering-derived-port",
    "disassembly"
  ]
}
```

### Identity (reviewed)

Fantasy World Dizzy — original Z80 source and BBC Micro port. Repository root and implementation inspected.
- https://github.com/picosonic/D3/blob/80a881ebe8dadb60392c92b100e0e74d255a0945/README.md
- https://github.com/picosonic/D3/blob/80a881ebe8dadb60392c92b100e0e74d255a0945/beeb/make.sh
- https://github.com/picosonic/D3/blob/80a881ebe8dadb60392c92b100e0e74d255a0945/beeb/dizzy3.asm
- https://github.com/picosonic/D3/blob/80a881ebe8dadb60392c92b100e0e74d255a0945/original_source/X-ALL.TXT

### Classification (reviewed)

Contains Oliver Twins PDS-era Z80 source with Spectrum/CPC build choices, native 6502 BBC gameplay, and a separately unfinished C64 cartridge disassembly. Main loop, inventory and actor routines are translated into host assembly rather than a Z80 interpreter.
- https://github.com/picosonic/D3/blob/80a881ebe8dadb60392c92b100e0e74d255a0945/README.md
- https://github.com/picosonic/D3/blob/80a881ebe8dadb60392c92b100e0e74d255a0945/beeb/make.sh
- https://github.com/picosonic/D3/blob/80a881ebe8dadb60392c92b100e0e74d255a0945/beeb/dizzy3.asm
- https://github.com/picosonic/D3/blob/80a881ebe8dadb60392c92b100e0e74d255a0945/original_source/X-ALL.TXT

### Source CPU (reviewed)

Original/source architecture: z80, 6502.
- https://github.com/picosonic/D3/blob/80a881ebe8dadb60392c92b100e0e74d255a0945/README.md
- https://github.com/picosonic/D3/blob/80a881ebe8dadb60392c92b100e0e74d255a0945/beeb/make.sh
- https://github.com/picosonic/D3/blob/80a881ebe8dadb60392c92b100e0e74d255a0945/beeb/dizzy3.asm
- https://github.com/picosonic/D3/blob/80a881ebe8dadb60392c92b100e0e74d255a0945/original_source/X-ALL.TXT

### Target CPU (reviewed)

Native target architecture: 6502.
- https://github.com/picosonic/D3/blob/80a881ebe8dadb60392c92b100e0e74d255a0945/README.md
- https://github.com/picosonic/D3/blob/80a881ebe8dadb60392c92b100e0e74d255a0945/beeb/make.sh
- https://github.com/picosonic/D3/blob/80a881ebe8dadb60392c92b100e0e74d255a0945/beeb/dizzy3.asm
- https://github.com/picosonic/D3/blob/80a881ebe8dadb60392c92b100e0e74d255a0945/original_source/X-ALL.TXT

### Build (reviewed)

Linux-oriented build scripts, BeebAsm and image/compression helpers. Requires two 16 KiB sideways-RAM banks: BBC Master or expanded BBC Micro. No assembly or game execution performed. Limitations: Source inspection only; no upstream game, installer, emulator, assembler or asset pipeline was run.
- https://github.com/picosonic/D3/blob/80a881ebe8dadb60392c92b100e0e74d255a0945/README.md
- https://github.com/picosonic/D3/blob/80a881ebe8dadb60392c92b100e0e74d255a0945/beeb/make.sh
- https://github.com/picosonic/D3/blob/80a881ebe8dadb60392c92b100e0e74d255a0945/beeb/dizzy3.asm
- https://github.com/picosonic/D3/blob/80a881ebe8dadb60392c92b100e0e74d255a0945/original_source/X-ALL.TXT

### Runtime profiles (reviewed)

32 KiB sideways RAM in addition to the BBC host memory; inherited Z80-style variable names do not imply a CPU-emulation runtime.
- https://github.com/picosonic/D3/blob/80a881ebe8dadb60392c92b100e0e74d255a0945/README.md
- https://github.com/picosonic/D3/blob/80a881ebe8dadb60392c92b100e0e74d255a0945/beeb/make.sh
- https://github.com/picosonic/D3/blob/80a881ebe8dadb60392c92b100e0e74d255a0945/beeb/dizzy3.asm
- https://github.com/picosonic/D3/blob/80a881ebe8dadb60392c92b100e0e74d255a0945/original_source/X-ALL.TXT

### AI (no-evidence-found)

No actual development-AI contribution established in inspected evidence; missing attribution is not evidence of non-use.
- https://github.com/picosonic/D3/blob/80a881ebe8dadb60392c92b100e0e74d255a0945/README.md
- https://github.com/picosonic/D3/blob/80a881ebe8dadb60392c92b100e0e74d255a0945/beeb/make.sh
- https://github.com/picosonic/D3/blob/80a881ebe8dadb60392c92b100e0e74d255a0945/beeb/dizzy3.asm
- https://github.com/picosonic/D3/blob/80a881ebe8dadb60392c92b100e0e74d255a0945/original_source/X-ALL.TXT

### Relationships (reviewed)

The included Treasure Island painting is a Fantasy World easter egg, not a Treasure Island port. CoCo Game Port Factory uses this source lineage.
- https://github.com/picosonic/D3/blob/80a881ebe8dadb60392c92b100e0e74d255a0945/README.md
- https://github.com/picosonic/D3/blob/80a881ebe8dadb60392c92b100e0e74d255a0945/beeb/make.sh
- https://github.com/picosonic/D3/blob/80a881ebe8dadb60392c92b100e0e74d255a0945/beeb/dizzy3.asm
- https://github.com/picosonic/D3/blob/80a881ebe8dadb60392c92b100e0e74d255a0945/original_source/X-ALL.TXT

## Dizzy 1 on BK-0011M — Fantasy World adaptation disassembly

Project ID: nzeemin-bk0011m-dizzy1td-rev · Overall audit: partial

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
  "display_title": "Dizzy 1 on BK-0011M — Fantasy World adaptation disassembly",
  "id": "nzeemin-bk0011m-dizzy1td-rev",
  "last_activity": null,
  "last_checked": "2026-10-28",
  "re_started": null,
  "reconstructed_languages": [
    "PDP-11 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/nzeemin/bk0011m-dizzy1td-rev",
  "runtime_profiles": [],
  "source_cpu": [
    "pdp-11"
  ],
  "source_language": [
    "PDP-11 assembly"
  ],
  "source_platforms": [
    "BK-0011M"
  ],
  "status": "Source inspected; no independent build or execution",
  "subjects": [
    "Dizzy 1 on BK-0011M"
  ],
  "tags": [
    "Dizzy"
  ],
  "target_cpu": [
    "pdp-11"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "BK-0011M"
  ],
  "techniques": [],
  "title": "Dizzy 1 on BK-0011M — Fantasy World adaptation disassembly",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "bk0011m-dizzy1td-rev",
  "work_kinds": [
    "disassembly",
    "data-format-analysis"
  ]
}
```

### Identity (reviewed)

Dizzy 1 on BK-0011M — Fantasy World adaptation disassembly. Repository root and implementation inspected.
- https://github.com/nzeemin/bk0011m-dizzy1td-rev/blob/e6f154e9f1d5ea8133b5fc98f459cbc016851e04/README.md
- https://github.com/nzeemin/bk0011m-dizzy1td-rev/blob/e6f154e9f1d5ea8133b5fc98f459cbc016851e04/!compilelink.bat
- https://github.com/nzeemin/bk0011m-dizzy1td-rev/blob/e6f154e9f1d5ea8133b5fc98f459cbc016851e04/REVERSE.md
- https://github.com/nzeemin/bk0011m-dizzy1td-rev/blob/e6f154e9f1d5ea8133b5fc98f459cbc016851e04/dizzy.asm

### Classification (reviewed)

Annotated MACRO-11-style reconstruction of the 1994 MBS/TD adaptation, with room, sprite, bank-switching, collision and Russian dialogue analysis. Despite the name Dizzy 1, this is a reworking of Fantasy World Dizzy.
- https://github.com/nzeemin/bk0011m-dizzy1td-rev/blob/e6f154e9f1d5ea8133b5fc98f459cbc016851e04/README.md
- https://github.com/nzeemin/bk0011m-dizzy1td-rev/blob/e6f154e9f1d5ea8133b5fc98f459cbc016851e04/!compilelink.bat
- https://github.com/nzeemin/bk0011m-dizzy1td-rev/blob/e6f154e9f1d5ea8133b5fc98f459cbc016851e04/REVERSE.md
- https://github.com/nzeemin/bk0011m-dizzy1td-rev/blob/e6f154e9f1d5ea8133b5fc98f459cbc016851e04/dizzy.asm

### Source CPU (reviewed)

Original/source architecture: pdp-11.
- https://github.com/nzeemin/bk0011m-dizzy1td-rev/blob/e6f154e9f1d5ea8133b5fc98f459cbc016851e04/README.md
- https://github.com/nzeemin/bk0011m-dizzy1td-rev/blob/e6f154e9f1d5ea8133b5fc98f459cbc016851e04/!compilelink.bat
- https://github.com/nzeemin/bk0011m-dizzy1td-rev/blob/e6f154e9f1d5ea8133b5fc98f459cbc016851e04/REVERSE.md
- https://github.com/nzeemin/bk0011m-dizzy1td-rev/blob/e6f154e9f1d5ea8133b5fc98f459cbc016851e04/dizzy.asm

### Target CPU (reviewed)

Native target architecture: pdp-11.
- https://github.com/nzeemin/bk0011m-dizzy1td-rev/blob/e6f154e9f1d5ea8133b5fc98f459cbc016851e04/README.md
- https://github.com/nzeemin/bk0011m-dizzy1td-rev/blob/e6f154e9f1d5ea8133b5fc98f459cbc016851e04/!compilelink.bat
- https://github.com/nzeemin/bk0011m-dizzy1td-rev/blob/e6f154e9f1d5ea8133b5fc98f459cbc016851e04/REVERSE.md
- https://github.com/nzeemin/bk0011m-dizzy1td-rev/blob/e6f154e9f1d5ea8133b5fc98f459cbc016851e04/dizzy.asm

### Build (reviewed)

Author reports byte-identical BKTurbo8 assembly of DIZZY.DIZ, the 16,186-byte main game file. Not independently reproduced. Loader DIZZY1 is explicitly outside scope; external maze/sprite files are not thereby reconstructed. Limitations: Source inspection only; no upstream game, installer, emulator, assembler or asset pipeline was run.
- https://github.com/nzeemin/bk0011m-dizzy1td-rev/blob/e6f154e9f1d5ea8133b5fc98f459cbc016851e04/README.md
- https://github.com/nzeemin/bk0011m-dizzy1td-rev/blob/e6f154e9f1d5ea8133b5fc98f459cbc016851e04/!compilelink.bat
- https://github.com/nzeemin/bk0011m-dizzy1td-rev/blob/e6f154e9f1d5ea8133b5fc98f459cbc016851e04/REVERSE.md
- https://github.com/nzeemin/bk0011m-dizzy1td-rev/blob/e6f154e9f1d5ea8133b5fc98f459cbc016851e04/dizzy.asm

### Runtime profiles (reviewed)

BK-0011M 128 KiB banked memory and two display buffers; no modern host minimum inferred.
- https://github.com/nzeemin/bk0011m-dizzy1td-rev/blob/e6f154e9f1d5ea8133b5fc98f459cbc016851e04/README.md
- https://github.com/nzeemin/bk0011m-dizzy1td-rev/blob/e6f154e9f1d5ea8133b5fc98f459cbc016851e04/!compilelink.bat
- https://github.com/nzeemin/bk0011m-dizzy1td-rev/blob/e6f154e9f1d5ea8133b5fc98f459cbc016851e04/REVERSE.md
- https://github.com/nzeemin/bk0011m-dizzy1td-rev/blob/e6f154e9f1d5ea8133b5fc98f459cbc016851e04/dizzy.asm

### AI (no-evidence-found)

No actual development-AI contribution established in inspected evidence; missing attribution is not evidence of non-use.
- https://github.com/nzeemin/bk0011m-dizzy1td-rev/blob/e6f154e9f1d5ea8133b5fc98f459cbc016851e04/README.md
- https://github.com/nzeemin/bk0011m-dizzy1td-rev/blob/e6f154e9f1d5ea8133b5fc98f459cbc016851e04/!compilelink.bat
- https://github.com/nzeemin/bk0011m-dizzy1td-rev/blob/e6f154e9f1d5ea8133b5fc98f459cbc016851e04/REVERSE.md
- https://github.com/nzeemin/bk0011m-dizzy1td-rev/blob/e6f154e9f1d5ea8133b5fc98f459cbc016851e04/dizzy.asm

### Relationships (reviewed)

A distinct PDP-11 game adaptation, not the original Dizzy: The Ultimate Cartoon Adventure. Notes distinguish code-file matching from a complete restored disk.
- https://github.com/nzeemin/bk0011m-dizzy1td-rev/blob/e6f154e9f1d5ea8133b5fc98f459cbc016851e04/README.md
- https://github.com/nzeemin/bk0011m-dizzy1td-rev/blob/e6f154e9f1d5ea8133b5fc98f459cbc016851e04/!compilelink.bat
- https://github.com/nzeemin/bk0011m-dizzy1td-rev/blob/e6f154e9f1d5ea8133b5fc98f459cbc016851e04/REVERSE.md
- https://github.com/nzeemin/bk0011m-dizzy1td-rev/blob/e6f154e9f1d5ea8133b5fc98f459cbc016851e04/dizzy.asm

## Fantasy World Dizzy — trace-checked TypeScript remaster

Project ID: chegleyev-dizzy3remake · Overall audit: partial

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
  "display_title": "Fantasy World Dizzy — trace-checked TypeScript remaster",
  "id": "chegleyev-dizzy3remake",
  "last_activity": null,
  "last_checked": "2026-10-28",
  "re_started": null,
  "reconstructed_languages": [
    "TypeScript"
  ],
  "record_class": "subject",
  "repo": "https://github.com/Chegleyev/Dizzy3Remake",
  "runtime_profiles": [],
  "source_cpu": [
    "z80"
  ],
  "source_language": [
    "TypeScript"
  ],
  "source_platforms": [
    "ZX Spectrum"
  ],
  "status": "Source inspected; no independent build or execution",
  "subjects": [
    "Fantasy World Dizzy"
  ],
  "tags": [
    "Dizzy"
  ],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Web"
  ],
  "techniques": [],
  "title": "Fantasy World Dizzy — trace-checked TypeScript remaster",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "Dizzy3Remake",
  "work_kinds": [
    "reverse-engineering-derived-port",
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Fantasy World Dizzy — trace-checked TypeScript remaster. Repository root and implementation inspected.
- https://github.com/Chegleyev/Dizzy3Remake/blob/b05aaeb3db081ee10b8720a8d9d66dd7612729d1/README.md
- https://github.com/Chegleyev/Dizzy3Remake/blob/b05aaeb3db081ee10b8720a8d9d66dd7612729d1/packages/engine/src/collision.ts
- https://github.com/Chegleyev/Dizzy3Remake/blob/b05aaeb3db081ee10b8720a8d9d66dd7612729d1/packages/engine/test/golden.test.ts
- https://github.com/Chegleyev/Dizzy3Remake/blob/b05aaeb3db081ee10b8720a8d9d66dd7612729d1/packages/engine/src/inventory.ts
- https://github.com/Chegleyev/Dizzy3Remake/blob/b05aaeb3db081ee10b8720a8d9d66dd7612729d1/packages/engine/src/engine.ts

### Classification (reviewed)

Semantic port of the 2023 Russian extended 128K version. Named collision and inventory functions identify original addresses; original-derived 12.5 Hz integer logic is tested against captured traces. Rendering interpolation, stable inventory slots, saves and remaster colouring are intentional changes.
- https://github.com/Chegleyev/Dizzy3Remake/blob/b05aaeb3db081ee10b8720a8d9d66dd7612729d1/README.md
- https://github.com/Chegleyev/Dizzy3Remake/blob/b05aaeb3db081ee10b8720a8d9d66dd7612729d1/packages/engine/src/collision.ts
- https://github.com/Chegleyev/Dizzy3Remake/blob/b05aaeb3db081ee10b8720a8d9d66dd7612729d1/packages/engine/test/golden.test.ts
- https://github.com/Chegleyev/Dizzy3Remake/blob/b05aaeb3db081ee10b8720a8d9d66dd7612729d1/packages/engine/src/inventory.ts
- https://github.com/Chegleyev/Dizzy3Remake/blob/b05aaeb3db081ee10b8720a8d9d66dd7612729d1/packages/engine/src/engine.ts

### Source CPU (reviewed)

Original/source architecture: z80.
- https://github.com/Chegleyev/Dizzy3Remake/blob/b05aaeb3db081ee10b8720a8d9d66dd7612729d1/README.md
- https://github.com/Chegleyev/Dizzy3Remake/blob/b05aaeb3db081ee10b8720a8d9d66dd7612729d1/packages/engine/src/collision.ts
- https://github.com/Chegleyev/Dizzy3Remake/blob/b05aaeb3db081ee10b8720a8d9d66dd7612729d1/packages/engine/test/golden.test.ts
- https://github.com/Chegleyev/Dizzy3Remake/blob/b05aaeb3db081ee10b8720a8d9d66dd7612729d1/packages/engine/src/inventory.ts
- https://github.com/Chegleyev/Dizzy3Remake/blob/b05aaeb3db081ee10b8720a8d9d66dd7612729d1/packages/engine/src/engine.ts

### Target CPU (no-evidence-found)

No host CPU minimum established from inspected source.
- https://github.com/Chegleyev/Dizzy3Remake/blob/b05aaeb3db081ee10b8720a8d9d66dd7612729d1/README.md
- https://github.com/Chegleyev/Dizzy3Remake/blob/b05aaeb3db081ee10b8720a8d9d66dd7612729d1/packages/engine/src/collision.ts
- https://github.com/Chegleyev/Dizzy3Remake/blob/b05aaeb3db081ee10b8720a8d9d66dd7612729d1/packages/engine/test/golden.test.ts
- https://github.com/Chegleyev/Dizzy3Remake/blob/b05aaeb3db081ee10b8720a8d9d66dd7612729d1/packages/engine/src/inventory.ts
- https://github.com/Chegleyev/Dizzy3Remake/blob/b05aaeb3db081ee10b8720a8d9d66dd7612729d1/packages/engine/src/engine.ts

### Build (reviewed)

Node/Vite/PixiJS/Vitest build to a single HTML page. Golden tests compare eight bounded movement scenarios and other subsystem tests are present; no independent test run or complete-game equivalence proof. Audio replays captured AY-register streams through a chip implementation, not a runtime Z80 game interpreter. Limitations: Source inspection only; no upstream game, installer, emulator, assembler or asset pipeline was run.
- https://github.com/Chegleyev/Dizzy3Remake/blob/b05aaeb3db081ee10b8720a8d9d66dd7612729d1/README.md
- https://github.com/Chegleyev/Dizzy3Remake/blob/b05aaeb3db081ee10b8720a8d9d66dd7612729d1/packages/engine/src/collision.ts
- https://github.com/Chegleyev/Dizzy3Remake/blob/b05aaeb3db081ee10b8720a8d9d66dd7612729d1/packages/engine/test/golden.test.ts
- https://github.com/Chegleyev/Dizzy3Remake/blob/b05aaeb3db081ee10b8720a8d9d66dd7612729d1/packages/engine/src/inventory.ts
- https://github.com/Chegleyev/Dizzy3Remake/blob/b05aaeb3db081ee10b8720a8d9d66dd7612729d1/packages/engine/src/engine.ts

### Runtime profiles (no-evidence-found)

Dependencies and limits are qualified in build notes; no independently verified runtime floor.
- https://github.com/Chegleyev/Dizzy3Remake/blob/b05aaeb3db081ee10b8720a8d9d66dd7612729d1/README.md
- https://github.com/Chegleyev/Dizzy3Remake/blob/b05aaeb3db081ee10b8720a8d9d66dd7612729d1/packages/engine/src/collision.ts
- https://github.com/Chegleyev/Dizzy3Remake/blob/b05aaeb3db081ee10b8720a8d9d66dd7612729d1/packages/engine/test/golden.test.ts
- https://github.com/Chegleyev/Dizzy3Remake/blob/b05aaeb3db081ee10b8720a8d9d66dd7612729d1/packages/engine/src/inventory.ts
- https://github.com/Chegleyev/Dizzy3Remake/blob/b05aaeb3db081ee10b8720a8d9d66dd7612729d1/packages/engine/src/engine.ts

### AI (no-evidence-found)

No actual development-AI contribution established in inspected evidence; missing attribution is not evidence of non-use.
- https://github.com/Chegleyev/Dizzy3Remake/blob/b05aaeb3db081ee10b8720a8d9d66dd7612729d1/README.md
- https://github.com/Chegleyev/Dizzy3Remake/blob/b05aaeb3db081ee10b8720a8d9d66dd7612729d1/packages/engine/src/collision.ts
- https://github.com/Chegleyev/Dizzy3Remake/blob/b05aaeb3db081ee10b8720a8d9d66dd7612729d1/packages/engine/test/golden.test.ts
- https://github.com/Chegleyev/Dizzy3Remake/blob/b05aaeb3db081ee10b8720a8d9d66dd7612729d1/packages/engine/src/inventory.ts
- https://github.com/Chegleyev/Dizzy3Remake/blob/b05aaeb3db081ee10b8720a8d9d66dd7612729d1/packages/engine/src/engine.ts

### Relationships (reviewed)

The reference is Dr. Titus extended Fantasy World, not unmodified 1989 retail and not Treasure Island. Even ZX rendering deliberately avoids Dizzy colour clash; original data are excluded from the code MIT licence.
- https://github.com/Chegleyev/Dizzy3Remake/blob/b05aaeb3db081ee10b8720a8d9d66dd7612729d1/README.md
- https://github.com/Chegleyev/Dizzy3Remake/blob/b05aaeb3db081ee10b8720a8d9d66dd7612729d1/packages/engine/src/collision.ts
- https://github.com/Chegleyev/Dizzy3Remake/blob/b05aaeb3db081ee10b8720a8d9d66dd7612729d1/packages/engine/test/golden.test.ts
- https://github.com/Chegleyev/Dizzy3Remake/blob/b05aaeb3db081ee10b8720a8d9d66dd7612729d1/packages/engine/src/inventory.ts
- https://github.com/Chegleyev/Dizzy3Remake/blob/b05aaeb3db081ee10b8720a8d9d66dd7612729d1/packages/engine/src/engine.ts

## Treasure Island Dizzy — Godot adventure remake

Project ID: dev-vpa-dizzy-adventures-remake · Overall audit: partial

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
  "display_title": "Treasure Island Dizzy — Godot adventure remake",
  "id": "dev-vpa-dizzy-adventures-remake",
  "last_activity": null,
  "last_checked": "2026-10-28",
  "re_started": null,
  "reconstructed_languages": [
    "GDScript"
  ],
  "record_class": "subject",
  "repo": "https://github.com/dev-vpa/dizzy-adventures-remake",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [
    "GDScript"
  ],
  "source_platforms": [
    "ZX Spectrum",
    "C64"
  ],
  "status": "Source inspected; no independent build or execution",
  "subjects": [
    "Treasure Island Dizzy"
  ],
  "tags": [
    "Dizzy"
  ],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Windows",
    "Linux",
    "Web",
    "Android"
  ],
  "techniques": [],
  "title": "Treasure Island Dizzy — Godot adventure remake",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "dizzy-adventures-remake",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Treasure Island Dizzy — Godot adventure remake. Repository root and implementation inspected.
- https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/README.md
- https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/core/player/player.gd
- https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/tests/integration/test_win_path.gd.uid
- https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/games/treasure-island/data/screen_map.md
- https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/tests/integration/test_win_path.gd

### Classification (reviewed)

Substantial game recreation with 51 claimed level scenes, inventory trades, snorkel/water hazards, thirty coins, boat assembly and taxman ending. Content map cites Spectrum/C64 walkthroughs; Godot gravity and collision implement new mechanics rather than proven recovered original algorithms.
- https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/README.md
- https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/core/player/player.gd
- https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/tests/integration/test_win_path.gd.uid
- https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/games/treasure-island/data/screen_map.md
- https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/tests/integration/test_win_path.gd

### Source CPU (no-evidence-found)

No single original binary architecture established for this format/engine or multi-version recreation.
- https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/README.md
- https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/core/player/player.gd
- https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/tests/integration/test_win_path.gd.uid
- https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/games/treasure-island/data/screen_map.md
- https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/tests/integration/test_win_path.gd

### Target CPU (no-evidence-found)

No host CPU minimum established from inspected source.
- https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/README.md
- https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/core/player/player.gd
- https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/tests/integration/test_win_path.gd.uid
- https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/games/treasure-island/data/screen_map.md
- https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/tests/integration/test_win_path.gd

### Build (reviewed)

Godot 4.4+ compatibility renderer and export presets. Upstream calls it pre-playtest polish awaiting a full playthrough. TestWinPath validates graph reachability and direct scripted state changes, explicitly not physical traversal. Build/playability flags remain unverified. Limitations: Source inspection only; no upstream game, installer, emulator, assembler or asset pipeline was run.
- https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/README.md
- https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/core/player/player.gd
- https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/tests/integration/test_win_path.gd.uid
- https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/games/treasure-island/data/screen_map.md
- https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/tests/integration/test_win_path.gd

### Runtime profiles (no-evidence-found)

Dependencies and limits are qualified in build notes; no independently verified runtime floor.
- https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/README.md
- https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/core/player/player.gd
- https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/tests/integration/test_win_path.gd.uid
- https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/games/treasure-island/data/screen_map.md
- https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/tests/integration/test_win_path.gd

### AI (no-evidence-found)

No actual development-AI contribution established in inspected evidence; missing attribution is not evidence of non-use.
- https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/README.md
- https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/core/player/player.gd
- https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/tests/integration/test_win_path.gd.uid
- https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/games/treasure-island/data/screen_map.md
- https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/tests/integration/test_win_path.gd

### Relationships (reviewed)

A genuine multi-screen recreation but not a byte-exact disassembly or fidelity-verified port. Other Dizzy adventures are planned only. Older slice-map migration notes and screen counts must not be treated as original-game measurements.
- https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/README.md
- https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/core/player/player.gd
- https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/tests/integration/test_win_path.gd.uid
- https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/games/treasure-island/data/screen_map.md
- https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/tests/integration/test_win_path.gd

## Fantasy World Dizzy CoCo 2 — Game Port Factory

Project ID: n0t4r0b0t-game-port-factory · Overall audit: partial

### Typed catalogue values

```json
{
  "ai": {
    "tools": [
      "Claude Code"
    ],
    "usage": true
  },
  "build": {
    "byte_exact": null,
    "compilable": null,
    "playable": null,
    "runnable": null
  },
  "display_title": "Fantasy World Dizzy CoCo 2 — Game Port Factory",
  "id": "n0t4r0b0t-game-port-factory",
  "last_activity": null,
  "last_checked": "2026-10-28",
  "re_started": null,
  "reconstructed_languages": [
    "6809 assembly",
    "Rust",
    "Python",
    "Shell"
  ],
  "record_class": "hybrid",
  "repo": "https://github.com/N0t4R0b0t/game-port-factory",
  "runtime_profiles": [],
  "source_cpu": [
    "z80"
  ],
  "source_language": [
    "6809 assembly",
    "Rust",
    "Python",
    "Shell"
  ],
  "source_platforms": [
    "ZX Spectrum"
  ],
  "status": "Source inspected; no independent build or execution",
  "subjects": [
    "Fantasy World Dizzy CoCo 2"
  ],
  "tags": [
    "Dizzy"
  ],
  "target_cpu": [
    "6809"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Tandy Color Computer 2"
  ],
  "techniques": [],
  "title": "Fantasy World Dizzy CoCo 2 — Game Port Factory",
  "tool_kinds": [
    "automation"
  ],
  "types": [
    "hybrid"
  ],
  "upstream_name": "game-port-factory",
  "work_kinds": [
    "reimplementation",
    "reverse-engineering-derived-port"
  ]
}
```

### Identity (reviewed)

Fantasy World Dizzy CoCo 2 — Game Port Factory. Repository root and implementation inspected.
- https://github.com/N0t4R0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/README.md
- https://github.com/N0t4R0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/ports/dizzy-coco2/README.md
- https://github.com/N0t4R0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/ports/dizzy-coco2/PORT.toml
- https://github.com/N0t4R0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/ports/dizzy-coco2/docs/PROVENANCE.md
- https://github.com/N0t4R0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/ports/dizzy-coco2/target/dragon_code.asm

### Classification (reviewed)

Native 6809 implementation derived from released Fantasy World rules and data, alongside reusable differential-emulator tooling. Current port notes describe full tape/floppy routes, dialogue and thirty coins; the smaller run build has only 31 base rooms.
- https://github.com/N0t4R0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/README.md
- https://github.com/N0t4R0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/ports/dizzy-coco2/README.md
- https://github.com/N0t4R0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/ports/dizzy-coco2/PORT.toml
- https://github.com/N0t4R0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/ports/dizzy-coco2/docs/PROVENANCE.md
- https://github.com/N0t4R0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/ports/dizzy-coco2/target/dragon_code.asm

### Source CPU (reviewed)

Original/source architecture: z80.
- https://github.com/N0t4R0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/README.md
- https://github.com/N0t4R0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/ports/dizzy-coco2/README.md
- https://github.com/N0t4R0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/ports/dizzy-coco2/PORT.toml
- https://github.com/N0t4R0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/ports/dizzy-coco2/docs/PROVENANCE.md
- https://github.com/N0t4R0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/ports/dizzy-coco2/target/dragon_code.asm

### Target CPU (reviewed)

Native target architecture: 6809.
- https://github.com/N0t4R0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/README.md
- https://github.com/N0t4R0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/ports/dizzy-coco2/README.md
- https://github.com/N0t4R0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/ports/dizzy-coco2/PORT.toml
- https://github.com/N0t4R0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/ports/dizzy-coco2/docs/PROVENANCE.md
- https://github.com/N0t4R0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/ports/dizzy-coco2/target/dragon_code.asm

### Build (reviewed)

Requires supplied pinned D3 sources and CoCo ROMs plus lwtools, Rust, Python and emulator tools. Author reports reproducible builds and route bots; no independent runs. Later port notes supersede the root README room-93 blocker but retain taller kill boxes, actor-clock timer differences, different randomness, silent heart sequence and untested physical hardware. Limitations: Source inspection only; no upstream game, installer, emulator, assembler or asset pipeline was run.
- https://github.com/N0t4R0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/README.md
- https://github.com/N0t4R0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/ports/dizzy-coco2/README.md
- https://github.com/N0t4R0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/ports/dizzy-coco2/PORT.toml
- https://github.com/N0t4R0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/ports/dizzy-coco2/docs/PROVENANCE.md
- https://github.com/N0t4R0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/ports/dizzy-coco2/target/dragon_code.asm

### Runtime profiles (reviewed)

64 KiB CoCo 2; floppy requires RS-DOS. Tape omits some negative-x scenery, floppy clips it; floppy joystick is not separately verified.
- https://github.com/N0t4R0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/README.md
- https://github.com/N0t4R0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/ports/dizzy-coco2/README.md
- https://github.com/N0t4R0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/ports/dizzy-coco2/PORT.toml
- https://github.com/N0t4R0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/ports/dizzy-coco2/docs/PROVENANCE.md
- https://github.com/N0t4R0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/ports/dizzy-coco2/target/dragon_code.asm

### AI (reviewed)

README describes the actual end-to-end agent-driven port workflow and completed reference example, not just a speculative AI plan.
- https://github.com/N0t4R0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/README.md
- https://github.com/N0t4R0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/ports/dizzy-coco2/README.md
- https://github.com/N0t4R0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/ports/dizzy-coco2/PORT.toml
- https://github.com/N0t4R0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/ports/dizzy-coco2/docs/PROVENANCE.md
- https://github.com/N0t4R0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/ports/dizzy-coco2/target/dragon_code.asm

### Relationships (reviewed)

Use one repository-root record for its reference game and supporting factory. Original media are absent and generated locally. Cross-platform reproducibility means matching this port build, not identical Spectrum machine code.
- https://github.com/N0t4R0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/README.md
- https://github.com/N0t4R0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/ports/dizzy-coco2/README.md
- https://github.com/N0t4R0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/ports/dizzy-coco2/PORT.toml
- https://github.com/N0t4R0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/ports/dizzy-coco2/docs/PROVENANCE.md
- https://github.com/N0t4R0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/ports/dizzy-coco2/target/dragon_code.asm

## Dizzy Log Cabin — BK to UKNC native port

Project ID: nzeemin-uknc-dizzylogcabin · Overall audit: partial

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
  "display_title": "Dizzy Log Cabin — BK to UKNC native port",
  "id": "nzeemin-uknc-dizzylogcabin",
  "last_activity": null,
  "last_checked": "2026-10-28",
  "re_started": null,
  "reconstructed_languages": [
    "PDP-11 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/nzeemin/uknc-dizzylogcabin",
  "runtime_profiles": [],
  "source_cpu": [
    "pdp-11"
  ],
  "source_language": [
    "PDP-11 assembly"
  ],
  "source_platforms": [
    "BK-0010",
    "BK-0011M"
  ],
  "status": "Source inspected; no independent build or execution",
  "subjects": [
    "Dizzy Log Cabin"
  ],
  "tags": [
    "Dizzy"
  ],
  "target_cpu": [
    "pdp-11"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "UKNC"
  ],
  "techniques": [],
  "title": "Dizzy Log Cabin — BK to UKNC native port",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "uknc-dizzylogcabin",
  "work_kinds": [
    "source-restoration",
    "reverse-engineering-derived-port"
  ]
}
```

### Identity (reviewed)

Dizzy Log Cabin — BK to UKNC native port. Repository root and implementation inspected.
- https://github.com/nzeemin/uknc-dizzylogcabin/blob/8bcd35d8a6ccca71448c86b58490415fa316deb8/README.md
- https://github.com/nzeemin/uknc-dizzylogcabin/blob/8bcd35d8a6ccca71448c86b58490415fa316deb8/!compilelink.bat
- https://github.com/nzeemin/uknc-dizzylogcabin/blob/8bcd35d8a6ccca71448c86b58490415fa316deb8/DIZZYL.ASM

### Classification (reviewed)

Native port of the winter Log Cabin mini-adventure using source supplied by BK author Sergey Shcherbakovsky. Assembly adapts display access and title RLE handling to UKNC hardware.
- https://github.com/nzeemin/uknc-dizzylogcabin/blob/8bcd35d8a6ccca71448c86b58490415fa316deb8/README.md
- https://github.com/nzeemin/uknc-dizzylogcabin/blob/8bcd35d8a6ccca71448c86b58490415fa316deb8/!compilelink.bat
- https://github.com/nzeemin/uknc-dizzylogcabin/blob/8bcd35d8a6ccca71448c86b58490415fa316deb8/DIZZYL.ASM

### Source CPU (reviewed)

Original/source architecture: pdp-11.
- https://github.com/nzeemin/uknc-dizzylogcabin/blob/8bcd35d8a6ccca71448c86b58490415fa316deb8/README.md
- https://github.com/nzeemin/uknc-dizzylogcabin/blob/8bcd35d8a6ccca71448c86b58490415fa316deb8/!compilelink.bat
- https://github.com/nzeemin/uknc-dizzylogcabin/blob/8bcd35d8a6ccca71448c86b58490415fa316deb8/DIZZYL.ASM

### Target CPU (reviewed)

Native target architecture: pdp-11.
- https://github.com/nzeemin/uknc-dizzylogcabin/blob/8bcd35d8a6ccca71448c86b58490415fa316deb8/README.md
- https://github.com/nzeemin/uknc-dizzylogcabin/blob/8bcd35d8a6ccca71448c86b58490415fa316deb8/!compilelink.bat
- https://github.com/nzeemin/uknc-dizzylogcabin/blob/8bcd35d8a6ccca71448c86b58490415fa316deb8/DIZZYL.ASM

### Build (reviewed)

BKTurbo8 plus bkbin2sav/RT-11 disk tooling. Author calls the zero version completable but without music/sound and with awkward controls; independently untested. Limitations: Source inspection only; no upstream game, installer, emulator, assembler or asset pipeline was run.
- https://github.com/nzeemin/uknc-dizzylogcabin/blob/8bcd35d8a6ccca71448c86b58490415fa316deb8/README.md
- https://github.com/nzeemin/uknc-dizzylogcabin/blob/8bcd35d8a6ccca71448c86b58490415fa316deb8/!compilelink.bat
- https://github.com/nzeemin/uknc-dizzylogcabin/blob/8bcd35d8a6ccca71448c86b58490415fa316deb8/DIZZYL.ASM

### Runtime profiles (no-evidence-found)

Dependencies and limits are qualified in build notes; no independently verified runtime floor.
- https://github.com/nzeemin/uknc-dizzylogcabin/blob/8bcd35d8a6ccca71448c86b58490415fa316deb8/README.md
- https://github.com/nzeemin/uknc-dizzylogcabin/blob/8bcd35d8a6ccca71448c86b58490415fa316deb8/!compilelink.bat
- https://github.com/nzeemin/uknc-dizzylogcabin/blob/8bcd35d8a6ccca71448c86b58490415fa316deb8/DIZZYL.ASM

### AI (no-evidence-found)

No actual development-AI contribution established in inspected evidence; missing attribution is not evidence of non-use.
- https://github.com/nzeemin/uknc-dizzylogcabin/blob/8bcd35d8a6ccca71448c86b58490415fa316deb8/README.md
- https://github.com/nzeemin/uknc-dizzylogcabin/blob/8bcd35d8a6ccca71448c86b58490415fa316deb8/!compilelink.bat
- https://github.com/nzeemin/uknc-dizzylogcabin/blob/8bcd35d8a6ccca71448c86b58490415fa316deb8/DIZZYL.ASM

### Relationships (reviewed)

Lineage is Jamie Douglas PC Log Cabin, Verm-V Spectrum version, MDK BK adaptation, then UKNC. It is not an Oliver Twins commercial Dizzy reconstruction.
- https://github.com/nzeemin/uknc-dizzylogcabin/blob/8bcd35d8a6ccca71448c86b58490415fa316deb8/README.md
- https://github.com/nzeemin/uknc-dizzylogcabin/blob/8bcd35d8a6ccca71448c86b58490415fa316deb8/!compilelink.bat
- https://github.com/nzeemin/uknc-dizzylogcabin/blob/8bcd35d8a6ccca71448c86b58490415fa316deb8/DIZZYL.ASM

## Ghastly Getaway Dizzy — Spectrum demake

Project ID: verm-v-ghastly-getaway-dizzy · Overall audit: partial

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
  "display_title": "Ghastly Getaway Dizzy — Spectrum demake",
  "id": "verm-v-ghastly-getaway-dizzy",
  "last_activity": null,
  "last_checked": "2026-10-28",
  "re_started": null,
  "reconstructed_languages": [
    "Dizzy Scripting Engine scripts"
  ],
  "record_class": "subject",
  "repo": "https://github.com/Verm-V/Ghastly-Getaway-Dizzy",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [
    "Dizzy Scripting Engine scripts"
  ],
  "source_platforms": [
    "Windows"
  ],
  "status": "Source inspected; no independent build or execution",
  "subjects": [
    "Ghastly Getaway Dizzy"
  ],
  "tags": [
    "Dizzy"
  ],
  "target_cpu": [
    "z80"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "ZX Spectrum"
  ],
  "techniques": [],
  "title": "Ghastly Getaway Dizzy — Spectrum demake",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "Ghastly-Getaway-Dizzy",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Ghastly Getaway Dizzy — Spectrum demake. Repository root and implementation inspected.
- https://github.com/Verm-V/Ghastly-Getaway-Dizzy/blob/a4a7bf52521716ff0048766cad09542bebf8dee1/readme.txt
- https://github.com/Verm-V/Ghastly-Getaway-Dizzy/blob/a4a7bf52521716ff0048766cad09542bebf8dee1/data/defines.txt
- https://github.com/Verm-V/Ghastly-Getaway-Dizzy/blob/a4a7bf52521716ff0048766cad09542bebf8dee1/ghastly-getaway-gizzy.dseprj
- https://github.com/Verm-V/Ghastly-Getaway-Dizzy/blob/a4a7bf52521716ff0048766cad09542bebf8dee1/data/code1.txt

### Classification (reviewed)

Game-specific demake of the PC DizzyAGE adventure, containing hotel rooms, dialogue, item identifiers and event/puzzle scripts. This is a different fan adventure, not a commercial Dizzy-series decompilation.
- https://github.com/Verm-V/Ghastly-Getaway-Dizzy/blob/a4a7bf52521716ff0048766cad09542bebf8dee1/readme.txt
- https://github.com/Verm-V/Ghastly-Getaway-Dizzy/blob/a4a7bf52521716ff0048766cad09542bebf8dee1/data/defines.txt
- https://github.com/Verm-V/Ghastly-Getaway-Dizzy/blob/a4a7bf52521716ff0048766cad09542bebf8dee1/ghastly-getaway-gizzy.dseprj
- https://github.com/Verm-V/Ghastly-Getaway-Dizzy/blob/a4a7bf52521716ff0048766cad09542bebf8dee1/data/code1.txt

### Source CPU (no-evidence-found)

No single original binary architecture established for this format/engine or multi-version recreation.
- https://github.com/Verm-V/Ghastly-Getaway-Dizzy/blob/a4a7bf52521716ff0048766cad09542bebf8dee1/readme.txt
- https://github.com/Verm-V/Ghastly-Getaway-Dizzy/blob/a4a7bf52521716ff0048766cad09542bebf8dee1/data/defines.txt
- https://github.com/Verm-V/Ghastly-Getaway-Dizzy/blob/a4a7bf52521716ff0048766cad09542bebf8dee1/ghastly-getaway-gizzy.dseprj
- https://github.com/Verm-V/Ghastly-Getaway-Dizzy/blob/a4a7bf52521716ff0048766cad09542bebf8dee1/data/code1.txt

### Target CPU (reviewed)

Native target architecture: z80.
- https://github.com/Verm-V/Ghastly-Getaway-Dizzy/blob/a4a7bf52521716ff0048766cad09542bebf8dee1/readme.txt
- https://github.com/Verm-V/Ghastly-Getaway-Dizzy/blob/a4a7bf52521716ff0048766cad09542bebf8dee1/data/defines.txt
- https://github.com/Verm-V/Ghastly-Getaway-Dizzy/blob/a4a7bf52521716ff0048766cad09542bebf8dee1/ghastly-getaway-gizzy.dseprj
- https://github.com/Verm-V/Ghastly-Getaway-Dizzy/blob/a4a7bf52521716ff0048766cad09542bebf8dee1/data/code1.txt

### Build (reviewed)

Version 0.01; needs external Dizzy Scripting Engine 1.1.0 and DizzyAGE map editor. Project file contains author-specific Windows paths and credits remain incomplete. No build or full playthrough verified. Limitations: Source inspection only; no upstream game, installer, emulator, assembler or asset pipeline was run.
- https://github.com/Verm-V/Ghastly-Getaway-Dizzy/blob/a4a7bf52521716ff0048766cad09542bebf8dee1/readme.txt
- https://github.com/Verm-V/Ghastly-Getaway-Dizzy/blob/a4a7bf52521716ff0048766cad09542bebf8dee1/data/defines.txt
- https://github.com/Verm-V/Ghastly-Getaway-Dizzy/blob/a4a7bf52521716ff0048766cad09542bebf8dee1/ghastly-getaway-gizzy.dseprj
- https://github.com/Verm-V/Ghastly-Getaway-Dizzy/blob/a4a7bf52521716ff0048766cad09542bebf8dee1/data/code1.txt

### Runtime profiles (no-evidence-found)

Dependencies and limits are qualified in build notes; no independently verified runtime floor.
- https://github.com/Verm-V/Ghastly-Getaway-Dizzy/blob/a4a7bf52521716ff0048766cad09542bebf8dee1/readme.txt
- https://github.com/Verm-V/Ghastly-Getaway-Dizzy/blob/a4a7bf52521716ff0048766cad09542bebf8dee1/data/defines.txt
- https://github.com/Verm-V/Ghastly-Getaway-Dizzy/blob/a4a7bf52521716ff0048766cad09542bebf8dee1/ghastly-getaway-gizzy.dseprj
- https://github.com/Verm-V/Ghastly-Getaway-Dizzy/blob/a4a7bf52521716ff0048766cad09542bebf8dee1/data/code1.txt

### AI (no-evidence-found)

No actual development-AI contribution established in inspected evidence; missing attribution is not evidence of non-use.
- https://github.com/Verm-V/Ghastly-Getaway-Dizzy/blob/a4a7bf52521716ff0048766cad09542bebf8dee1/readme.txt
- https://github.com/Verm-V/Ghastly-Getaway-Dizzy/blob/a4a7bf52521716ff0048766cad09542bebf8dee1/data/defines.txt
- https://github.com/Verm-V/Ghastly-Getaway-Dizzy/blob/a4a7bf52521716ff0048766cad09542bebf8dee1/ghastly-getaway-gizzy.dseprj
- https://github.com/Verm-V/Ghastly-Getaway-Dizzy/blob/a4a7bf52521716ff0048766cad09542bebf8dee1/data/code1.txt

### Relationships (reviewed)

Credits Pogie for story/puzzles and Verm-V for code. Target scripting engine is a game-language runtime, not evidence of an emulated source CPU.
- https://github.com/Verm-V/Ghastly-Getaway-Dizzy/blob/a4a7bf52521716ff0048766cad09542bebf8dee1/readme.txt
- https://github.com/Verm-V/Ghastly-Getaway-Dizzy/blob/a4a7bf52521716ff0048766cad09542bebf8dee1/data/defines.txt
- https://github.com/Verm-V/Ghastly-Getaway-Dizzy/blob/a4a7bf52521716ff0048766cad09542bebf8dee1/ghastly-getaway-gizzy.dseprj
- https://github.com/Verm-V/Ghastly-Getaway-Dizzy/blob/a4a7bf52521716ff0048766cad09542bebf8dee1/data/code1.txt

## Prolozzy — DizzyAGE engine adapted to SWI-Prolog

Project ID: leprosarium-prolozzy · Overall audit: partial

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
  "display_title": "Prolozzy — DizzyAGE engine adapted to SWI-Prolog",
  "id": "leprosarium-prolozzy",
  "last_activity": null,
  "last_checked": "2026-10-28",
  "re_started": null,
  "reconstructed_languages": [
    "C++",
    "Prolog"
  ],
  "record_class": "hybrid",
  "repo": "https://github.com/leprosarium/prolozzy",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [
    "C++",
    "Prolog"
  ],
  "source_platforms": [
    "Windows"
  ],
  "status": "Source inspected; no independent build or execution",
  "subjects": [
    "Prolozzy"
  ],
  "tags": [
    "Dizzy"
  ],
  "target_cpu": [],
  "target_kinds": [
    "game-engine"
  ],
  "target_platforms": [
    "Windows"
  ],
  "techniques": [],
  "title": "Prolozzy — DizzyAGE engine adapted to SWI-Prolog",
  "tool_kinds": [
    "language-tooling"
  ],
  "types": [
    "hybrid"
  ],
  "upstream_name": "prolozzy",
  "work_kinds": [
    "source-restoration",
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Prolozzy — DizzyAGE engine adapted to SWI-Prolog. Repository root and implementation inspected.
- https://github.com/leprosarium/prolozzy/blob/0049a5b7f7c47fad451c11ff21eb0868da4c7404/README.md
- https://github.com/leprosarium/prolozzy/blob/0049a5b7f7c47fad451c11ff21eb0868da4c7404/Game/DizPlayer.cpp
- https://github.com/leprosarium/prolozzy/blob/0049a5b7f7c47fad451c11ff21eb0868da4c7404/Game/DizScript.cpp

### Classification (reviewed)

DizzyAGE-derived native engine replaces scripting integration with SWI-Prolog. C++ player accessors and material/collision predicates expose actual engine state to Prolog, beyond a README-only proposal.
- https://github.com/leprosarium/prolozzy/blob/0049a5b7f7c47fad451c11ff21eb0868da4c7404/README.md
- https://github.com/leprosarium/prolozzy/blob/0049a5b7f7c47fad451c11ff21eb0868da4c7404/Game/DizPlayer.cpp
- https://github.com/leprosarium/prolozzy/blob/0049a5b7f7c47fad451c11ff21eb0868da4c7404/Game/DizScript.cpp

### Source CPU (no-evidence-found)

No single original binary architecture established for this format/engine or multi-version recreation.
- https://github.com/leprosarium/prolozzy/blob/0049a5b7f7c47fad451c11ff21eb0868da4c7404/README.md
- https://github.com/leprosarium/prolozzy/blob/0049a5b7f7c47fad451c11ff21eb0868da4c7404/Game/DizPlayer.cpp
- https://github.com/leprosarium/prolozzy/blob/0049a5b7f7c47fad451c11ff21eb0868da4c7404/Game/DizScript.cpp

### Target CPU (no-evidence-found)

No host CPU minimum established from inspected source.
- https://github.com/leprosarium/prolozzy/blob/0049a5b7f7c47fad451c11ff21eb0868da4c7404/README.md
- https://github.com/leprosarium/prolozzy/blob/0049a5b7f7c47fad451c11ff21eb0868da4c7404/Game/DizPlayer.cpp
- https://github.com/leprosarium/prolozzy/blob/0049a5b7f7c47fad451c11ff21eb0868da4c7404/Game/DizScript.cpp

### Build (reviewed)

Windows-oriented source uses SWI-Prolog headers and Win32 stream integration with inherited renderer/audio libraries. No independent build, compatibility suite or finished adventure established. Limitations: Source inspection only; no upstream game, installer, emulator, assembler or asset pipeline was run.
- https://github.com/leprosarium/prolozzy/blob/0049a5b7f7c47fad451c11ff21eb0868da4c7404/README.md
- https://github.com/leprosarium/prolozzy/blob/0049a5b7f7c47fad451c11ff21eb0868da4c7404/Game/DizPlayer.cpp
- https://github.com/leprosarium/prolozzy/blob/0049a5b7f7c47fad451c11ff21eb0868da4c7404/Game/DizScript.cpp

### Runtime profiles (no-evidence-found)

Dependencies and limits are qualified in build notes; no independently verified runtime floor.
- https://github.com/leprosarium/prolozzy/blob/0049a5b7f7c47fad451c11ff21eb0868da4c7404/README.md
- https://github.com/leprosarium/prolozzy/blob/0049a5b7f7c47fad451c11ff21eb0868da4c7404/Game/DizPlayer.cpp
- https://github.com/leprosarium/prolozzy/blob/0049a5b7f7c47fad451c11ff21eb0868da4c7404/Game/DizScript.cpp

### AI (no-evidence-found)

No actual development-AI contribution established in inspected evidence; missing attribution is not evidence of non-use.
- https://github.com/leprosarium/prolozzy/blob/0049a5b7f7c47fad451c11ff21eb0868da4c7404/README.md
- https://github.com/leprosarium/prolozzy/blob/0049a5b7f7c47fad451c11ff21eb0868da4c7404/Game/DizPlayer.cpp
- https://github.com/leprosarium/prolozzy/blob/0049a5b7f7c47fad451c11ff21eb0868da4c7404/Game/DizScript.cpp

### Relationships (reviewed)

Source-engine adaptation and game-authoring support, not recovered commercial Dizzy source. Do not count bundled third-party libraries as independent reconstructions.
- https://github.com/leprosarium/prolozzy/blob/0049a5b7f7c47fad451c11ff21eb0868da4c7404/README.md
- https://github.com/leprosarium/prolozzy/blob/0049a5b7f7c47fad451c11ff21eb0868da4c7404/Game/DizPlayer.cpp
- https://github.com/leprosarium/prolozzy/blob/0049a5b7f7c47fad451c11ff21eb0868da4c7404/Game/DizScript.cpp

## Pinned evidence manifest

- aevri-kwik-snax-readme-md: https://github.com/aevri/kwik_snax/blob/1adbb9a286c6a3f9ae6763886f011677207b515d/README.md (Git blob a1e4d9c1df8c76616dfffa7bb1a3179ecf88cdd1)
- chegleyev-dizzy3remake-packages-engine-src-collision-ts: https://github.com/chegleyev/dizzy3remake/blob/b05aaeb3db081ee10b8720a8d9d66dd7612729d1/packages/engine/src/collision.ts (Git blob d281e00898eb349a225b5ff8136a67f292df530d)
- chegleyev-dizzy3remake-packages-engine-src-inventory-ts: https://github.com/chegleyev/dizzy3remake/blob/b05aaeb3db081ee10b8720a8d9d66dd7612729d1/packages/engine/src/inventory.ts (Git blob a69e1e2d532cdb0fb19a9a17f51c4d067f430c3c)
- chegleyev-dizzy3remake-packages-engine-test-golden-test-ts: https://github.com/chegleyev/dizzy3remake/blob/b05aaeb3db081ee10b8720a8d9d66dd7612729d1/packages/engine/test/golden.test.ts (Git blob 122af603fb44748b72d40c689f33ebb7998d2c0d)
- chegleyev-dizzy3remake-readme-md: https://github.com/chegleyev/dizzy3remake/blob/b05aaeb3db081ee10b8720a8d9d66dd7612729d1/README.md (Git blob 76d9a73f853804654072fbd5e54e0f3ffa1faf62)
- danadrianmirea-dizzyage-dizzyage-readme-txt: https://github.com/danadrianmirea/dizzyage/blob/8e52d238cca482321a37f1d4a297100ccaf2eb33/dizzyage/readme.txt (Git blob 057fd66ef2bef8943ea4edf719143d236b6bebd2)
- danadrianmirea-dizzyage-readme-md: https://github.com/danadrianmirea/dizzyage/blob/8e52d238cca482321a37f1d4a297100ccaf2eb33/README.md (Git blob c07134446ad41987935f39c6897ec84f291ec637)
- dev-vpa-dizzy-adventures-remake-core-player-player-gd: https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/core/player/player.gd (Git blob d1caf9cc84a00af44afc48c5ee0cf28412a2e902)
- dev-vpa-dizzy-adventures-remake-games-treasure-island-data-screen-map-md: https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/games/treasure-island/data/screen_map.md (Git blob dc10f377b261fd9f03fd61de12ad4610375528a8)
- dev-vpa-dizzy-adventures-remake-readme-md: https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/README.md (Git blob b059aef1609bb926d17819d7e4c7002c5c1ef117)
- dev-vpa-dizzy-adventures-remake-tests-integration-test-win-path-gd: https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/tests/integration/test_win_path.gd (Git blob 03620f598752e8702749ce2a3d449464718cbf8d)
- dev-vpa-dizzy-adventures-remake-tests-integration-test-win-path-gd-uid: https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/tests/integration/test_win_path.gd.uid (Git blob 48b25c9b3192af5dbfb6f8f11252b76a41af7e87)
- dizzyage-custom-code-readme-md: https://github.com/dizzyage/custom_code/blob/332a1f3a2dfc1afbf3b3968cda00f96b48c79266/README.md (Git blob cde40e9ee08f58dbfdfabdb1a446599d4774edab)
- dkrutskikh-dizzy-kwik-snax-redux-game-game-cpp: https://github.com/dkrutskikh/dizzy-kwik-snax-redux/blob/e98affa9c4a58dcbea21d8bee5ec25a9ae92cfb7/game/game.cpp (Git blob 60c670d778278777391bbd9ef017fea727f04f64)
- dkrutskikh-dizzy-kwik-snax-redux-readme-md: https://github.com/dkrutskikh/dizzy-kwik-snax-redux/blob/e98affa9c4a58dcbea21d8bee5ec25a9ae92cfb7/README.md (Git blob a71b69b5d2af90e4b7555b4e2f4416c4488ab9ee)
- dkrutskikh-yolkfolk-legacy-readme-md: https://github.com/dkrutskikh/yolkfolk-legacy/blob/7d182f6e560f44e5984a8e75c704b80528f2f3b3/README.md (Git blob 48b5c3e0d852f6c23d145b5784ea7f14715f2f22)
- dkrutskikh-yolkfolk-legacy-source-template-cpp: https://github.com/dkrutskikh/yolkfolk-legacy/blob/7d182f6e560f44e5984a8e75c704b80528f2f3b3/source/template.cpp (Git blob 5b2eb16778a99f2405c5db99f7a1429a5cb9bbcb)
- fwmakc-dizzygame-readme-md: https://github.com/fwmakc/dizzygame/blob/d08909a4b41ae1ba277b540f85e123c49a08c996/README.md (Git blob 094d8e682f111e9fdcdff1dafa8a93865650a6fa)
- iratahack-dizzyviii-dizzy-viii-wonderful-dizzy-2020-v1-5-pok: https://github.com/iratahack/dizzyviii/blob/1e1bf44176d7eb4a0aad42bc2fd6c519dfcdc2e2/Dizzy%20VIII%20-%20Wonderful%20Dizzy%20%282020%29%20v1.5.pok (Git blob cb060b6477ec604bdc9f687806d1f066ceac53bf)
- iratahack-dizzyviii-readme-md: https://github.com/iratahack/dizzyviii/blob/1e1bf44176d7eb4a0aad42bc2fd6c519dfcdc2e2/README.md (Git blob 427a64b434f1ee34d77c300e2d7d829f5d931a94)
- jane-alesi-game-demo-js-game-js: https://github.com/jane-alesi/game-demo/blob/c88a733e177d2677a6f56997b9cc0f04cbbbc6f9/js/game.js (Git blob 42b44ed22681cf7100e7bbb5528f120558844b8e)
- jane-alesi-game-demo-readme-md: https://github.com/jane-alesi/game-demo/blob/c88a733e177d2677a6f56997b9cc0f04cbbbc6f9/README.md (Git blob 7f246a508f24d365977c959e9189eb2db7563334)
- leprosarium-prolozzy-game-dizplayer-cpp: https://github.com/leprosarium/prolozzy/blob/0049a5b7f7c47fad451c11ff21eb0868da4c7404/Game/DizPlayer.cpp (Git blob 8a67c15c2cf50f1c9aff48e9ec14b3c56d67f51a)
- leprosarium-prolozzy-game-dizscript-cpp: https://github.com/leprosarium/prolozzy/blob/0049a5b7f7c47fad451c11ff21eb0868da4c7404/Game/DizScript.cpp (Git blob c061c92befddfb000de3643fa859476df5868d84)
- leprosarium-prolozzy-readme-md: https://github.com/leprosarium/prolozzy/blob/0049a5b7f7c47fad451c11ff21eb0868da4c7404/README.md (Git blob 0733cd20c132935ac7a8759eb3dc0e4f810e11c2)
- n0t4r0b0t-game-port-factory-ports-dizzy-coco2-docs-provenance-md: https://github.com/n0t4r0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/ports/dizzy-coco2/docs/PROVENANCE.md (Git blob fc5c656f7cada3e234e6cb7f6ff30a7eda5a7861)
- n0t4r0b0t-game-port-factory-ports-dizzy-coco2-port-toml: https://github.com/n0t4r0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/ports/dizzy-coco2/PORT.toml (Git blob 4231f47ad539fc1c9fbdfe99616be3edafbf8ac4)
- n0t4r0b0t-game-port-factory-ports-dizzy-coco2-readme-md: https://github.com/n0t4r0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/ports/dizzy-coco2/README.md (Git blob 382d366be63f9fb8f706533ab46c437676e87551)
- n0t4r0b0t-game-port-factory-ports-dizzy-coco2-target-dragon-code-asm: https://github.com/n0t4r0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/ports/dizzy-coco2/target/dragon_code.asm (Git blob d12a2496914c4edb0ae5175f8bc346754fcddf03)
- n0t4r0b0t-game-port-factory-readme-md: https://github.com/n0t4r0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/README.md (Git blob 174049c357c87218e74b245d865be638a8717aaa)
- nzeemin-bk0011m-dizzy1td-rev-readme-md: https://github.com/nzeemin/bk0011m-dizzy1td-rev/blob/e6f154e9f1d5ea8133b5fc98f459cbc016851e04/README.md (Git blob 18cf4dd1e74bad915cd2305c8fc010716e026fee)
- nzeemin-bk0011m-dizzy1td-rev-reverse-md: https://github.com/nzeemin/bk0011m-dizzy1td-rev/blob/e6f154e9f1d5ea8133b5fc98f459cbc016851e04/REVERSE.md (Git blob e3eef8c1c462db377a146e17220dd53cfea37fa1)
- nzeemin-uknc-dizzylogcabin-readme-md: https://github.com/nzeemin/uknc-dizzylogcabin/blob/8bcd35d8a6ccca71448c86b58490415fa316deb8/README.md (Git blob 6b1d0742aadf8049e0db6e4a2c424e93d0a6841e)
- picosonic-d3-beeb-dizzy3-asm: https://github.com/picosonic/d3/blob/80a881ebe8dadb60392c92b100e0e74d255a0945/beeb/dizzy3.asm (Git blob 0538a1610aea76ba48d0f4582fd92e31d798f0e0)
- picosonic-d3-beeb-make-sh: https://github.com/picosonic/d3/blob/80a881ebe8dadb60392c92b100e0e74d255a0945/beeb/make.sh (Git blob 263912f293dd4302a12e6132200afe4038a4d378)
- picosonic-d3-readme-md: https://github.com/picosonic/d3/blob/80a881ebe8dadb60392c92b100e0e74d255a0945/README.md (Git blob a49153967e0f7bc37e79f35a82085e78bc37eef6)
- primo-malvado-dizzy-magicland-disassemble-build-build-sh: https://github.com/primo-malvado/dizzy_magicland_disassemble/blob/e051974f967681968ca19876ecc5364a5175e01d/build/build.sh (Git blob d0353ab9f6b270686852284d56ac01c82229ebee)
- primo-malvado-dizzy-magicland-disassemble-desenha-sprite-asm: https://github.com/primo-malvado/dizzy_magicland_disassemble/blob/e051974f967681968ca19876ecc5364a5175e01d/desenha_sprite.asm (Git blob 5edbb3844a1366e875c4c3bb0ff77658b5d6f3ee)
- primo-malvado-dizzy-magicland-disassemble-disassemble-disasemble-03-04-pl: https://github.com/primo-malvado/dizzy_magicland_disassemble/blob/e051974f967681968ca19876ecc5364a5175e01d/disassemble/disasemble_03_04.pl (Git blob b586d5742634abb3f5d4bd27ab493718f3eff36c)
- primo-malvado-dizzy-magicland-disassemble-readme-md: https://github.com/primo-malvado/dizzy_magicland_disassemble/blob/e051974f967681968ca19876ecc5364a5175e01d/README.md (Git blob 3e4698f3d62031a199340ab26122b39879f86071)
- ryanmallon-dizzy-dizzy-pack-py: https://github.com/ryanmallon/dizzy/blob/3e28cfbdcda36b5ae8b36d0c2a5b90dc849705d2/dizzy_pack.py (Git blob 386fc574ac362e9d10bbc8eb00d93e42d2961fd7)
- ryanmallon-dizzy-readme-md: https://github.com/ryanmallon/dizzy/blob/3e28cfbdcda36b5ae8b36d0c2a5b90dc849705d2/README.md (Git blob 93f251f9f59f7b6f0a128cde02e62a669a2593e5)
- ryanmallon-dizzy-stage-view-py: https://github.com/ryanmallon/dizzy/blob/3e28cfbdcda36b5ae8b36d0c2a5b90dc849705d2/stage_view.py (Git blob 39599d583096e65870852a38ddf4c627877f7865)
- sau412-dizzy-sandbox-readme-md: https://github.com/sau412/dizzy_sandbox/blob/c1fb0c3b1d4b505582eb54d783a86c1738c0a3bf/README.md (Git blob 2a3c22250797619fe484540eea6cbe090e00c8ab)
- verm-v-ghastly-getaway-dizzy-data-defines-txt: https://github.com/verm-v/ghastly-getaway-dizzy/blob/a4a7bf52521716ff0048766cad09542bebf8dee1/data/defines.txt (Git blob f73b804f51337ecd095cca471cb5076db0620fb4)
- verm-v-ghastly-getaway-dizzy-ghastly-getaway-gizzy-dseprj: https://github.com/verm-v/ghastly-getaway-dizzy/blob/a4a7bf52521716ff0048766cad09542bebf8dee1/ghastly-getaway-gizzy.dseprj (Git blob 8a78600c1aa412491089d6d79dc47cf2ae824758)
- verm-v-ghastly-getaway-dizzy-readme-txt: https://github.com/verm-v/ghastly-getaway-dizzy/blob/a4a7bf52521716ff0048766cad09542bebf8dee1/readme.txt (Git blob c59a80479c9b92ec9762b39c02365a044d2d2c42)

## Sources

```json
[
  {
    "first_indexed": "2026-10-28",
    "id": "github-ryanmallon-dizzy",
    "kind": "github-repository",
    "last_reviewed": "2026-10-28",
    "open_task_ids": [],
    "projects_promoted": [
      "ryanmallon-dizzy"
    ],
    "reason": "Documented NDX/RES chunk indexes and variable-bit dictionary decompression, unpack/repack scripts, sprite and layered-stage viewers. This is original game resource analysis, not a reconstructed playable engine.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/RyanMallon/dizzy"
  },
  {
    "first_indexed": "2026-10-28",
    "id": "github-primo-malvado-dizzy-magicland-disassemble",
    "kind": "github-repository",
    "last_reviewed": "2026-10-28",
    "open_task_ids": [],
    "projects_promoted": [
      "primo-malvado-dizzy-magicland-disassemble"
    ],
    "reason": "Game-specific code/data declarations identify map records, function indexes, sprite masks and named drawing operations. Generated and refactored assembly retain generic addresses and unknown regions, so semantic analysis is incomplete.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/primo-malvado/dizzy_magicland_disassemble"
  },
  {
    "first_indexed": "2026-10-28",
    "id": "github-picosonic-d3",
    "kind": "github-repository",
    "last_reviewed": "2026-10-28",
    "open_task_ids": [],
    "projects_promoted": [
      "picosonic-d3"
    ],
    "reason": "Contains Oliver Twins PDS-era Z80 source with Spectrum/CPC build choices, native 6502 BBC gameplay, and a separately unfinished C64 cartridge disassembly. Main loop, inventory and actor routines are translated into host assembly rather than a Z80 interpreter.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/picosonic/D3"
  },
  {
    "first_indexed": "2026-10-28",
    "id": "github-nzeemin-bk0011m-dizzy1td-rev",
    "kind": "github-repository",
    "last_reviewed": "2026-10-28",
    "open_task_ids": [],
    "projects_promoted": [
      "nzeemin-bk0011m-dizzy1td-rev"
    ],
    "reason": "Annotated MACRO-11-style reconstruction of the 1994 MBS/TD adaptation, with room, sprite, bank-switching, collision and Russian dialogue analysis. Despite the name Dizzy 1, this is a reworking of Fantasy World Dizzy.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/nzeemin/bk0011m-dizzy1td-rev"
  },
  {
    "first_indexed": "2026-10-28",
    "id": "github-chegleyev-dizzy3remake",
    "kind": "github-repository",
    "last_reviewed": "2026-10-28",
    "open_task_ids": [],
    "projects_promoted": [
      "chegleyev-dizzy3remake"
    ],
    "reason": "Semantic port of the 2023 Russian extended 128K version. Named collision and inventory functions identify original addresses; original-derived 12.5 Hz integer logic is tested against captured traces. Rendering interpolation, stable inventory slots, saves and remaster colouring are intentional changes.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/Chegleyev/Dizzy3Remake"
  },
  {
    "first_indexed": "2026-10-28",
    "id": "github-dev-vpa-dizzy-adventures-remake",
    "kind": "github-repository",
    "last_reviewed": "2026-10-28",
    "open_task_ids": [],
    "projects_promoted": [
      "dev-vpa-dizzy-adventures-remake"
    ],
    "reason": "Substantial game recreation with 51 claimed level scenes, inventory trades, snorkel/water hazards, thirty coins, boat assembly and taxman ending. Content map cites Spectrum/C64 walkthroughs; Godot gravity and collision implement new mechanics rather than proven recovered original algorithms.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/dev-vpa/dizzy-adventures-remake"
  },
  {
    "first_indexed": "2026-10-28",
    "id": "github-n0t4r0b0t-game-port-factory",
    "kind": "github-repository",
    "last_reviewed": "2026-10-28",
    "open_task_ids": [],
    "projects_promoted": [
      "n0t4r0b0t-game-port-factory"
    ],
    "reason": "Native 6809 implementation derived from released Fantasy World rules and data, alongside reusable differential-emulator tooling. Current port notes describe full tape/floppy routes, dialogue and thirty coins; the smaller run build has only 31 base rooms.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/N0t4R0b0t/game-port-factory"
  },
  {
    "first_indexed": "2026-10-28",
    "id": "github-nzeemin-uknc-dizzylogcabin",
    "kind": "github-repository",
    "last_reviewed": "2026-10-28",
    "open_task_ids": [],
    "projects_promoted": [
      "nzeemin-uknc-dizzylogcabin"
    ],
    "reason": "Native port of the winter Log Cabin mini-adventure using source supplied by BK author Sergey Shcherbakovsky. Assembly adapts display access and title RLE handling to UKNC hardware.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/nzeemin/uknc-dizzylogcabin"
  },
  {
    "first_indexed": "2026-10-28",
    "id": "github-verm-v-ghastly-getaway-dizzy",
    "kind": "github-repository",
    "last_reviewed": "2026-10-28",
    "open_task_ids": [],
    "projects_promoted": [
      "verm-v-ghastly-getaway-dizzy"
    ],
    "reason": "Game-specific demake of the PC DizzyAGE adventure, containing hotel rooms, dialogue, item identifiers and event/puzzle scripts. This is a different fan adventure, not a commercial Dizzy-series decompilation.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/Verm-V/Ghastly-Getaway-Dizzy"
  },
  {
    "first_indexed": "2026-10-28",
    "id": "github-leprosarium-prolozzy",
    "kind": "github-repository",
    "last_reviewed": "2026-10-28",
    "open_task_ids": [],
    "projects_promoted": [
      "leprosarium-prolozzy"
    ],
    "reason": "DizzyAGE-derived native engine replaces scripting integration with SWI-Prolog. C++ player accessors and material/collision predicates expose actual engine state to Prolog, beyond a README-only proposal.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/leprosarium/prolozzy"
  },
  {
    "first_indexed": "2026-10-28",
    "id": "github-dkrutskikh-dizzy-kwik-snax-redux",
    "kind": "github-repository",
    "last_reviewed": "2026-10-28",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Design documentation and multi-platform build skeleton are present, but game/game.cpp only displays a title and waits for VBlank (or immediately returns on desktop). No Kwik Snax gameplay implemented at this revision.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/dkrutskikh/dizzy-kwik-snax-redux"
  },
  {
    "first_indexed": "2026-10-28",
    "id": "github-dkrutskikh-yolkfolk-legacy",
    "kind": "github-repository",
    "last_reviewed": "2026-10-28",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Source is the GBA Hello World template, not a reconstructed Dizzy game.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/dkrutskikh/yolkfolk-legacy"
  },
  {
    "first_indexed": "2026-10-28",
    "id": "github-jane-alesi-game-demo",
    "kind": "github-repository",
    "last_reviewed": "2026-10-28",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Treasure Island-labelled Canvas demo has four simple treasures, procedural scenery and a collect-all win condition; inventory and multiple levels are future work. It does not reconstruct the original puzzle adventure. Explicit AI authorship does not change this scope finding.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/jane-alesi/game-demo"
  },
  {
    "first_indexed": "2026-10-28",
    "id": "github-fwmakc-dizzygame",
    "kind": "github-repository",
    "last_reviewed": "2026-10-28",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Construct 2 runtime export and packaged event/assets are present, but no original project source or evidence of original-game algorithm recovery established. Keep as a fan-demo lead rather than count a completed reconstruction.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/fwmakc/dizzygame"
  },
  {
    "first_indexed": "2026-10-28",
    "id": "github-sau412-dizzy-sandbox",
    "kind": "github-repository",
    "last_reviewed": "2026-10-28",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Seven-file animation/experiment sandbox, not a recovered full Dizzy game.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/sau412/Dizzy_sandbox"
  },
  {
    "first_indexed": "2026-10-28",
    "id": "github-iratahack-dizzyviii",
    "kind": "github-repository",
    "last_reviewed": "2026-10-28",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Only a short Wonderful Dizzy cheat POK file and README; insufficient standalone reconstruction/analysis project.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/iratahack/DizzyVIII"
  },
  {
    "first_indexed": "2026-10-28",
    "id": "github-danadrianmirea-dizzyage",
    "kind": "github-repository",
    "last_reviewed": "2026-10-28",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Learning collection bundles DizzyAGE 2.4 engine/editor source and fan-game examples. Original Simion authorship is preserved in bundled documentation; do not promote this mirror as an independent reconstruction or confuse it with commercial Dizzy source.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/danadrianmirea/dizzyage"
  },
  {
    "first_indexed": "2026-10-28",
    "id": "github-da-nie-dizzy-game",
    "kind": "github-repository",
    "last_reviewed": "2026-10-28",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Author identifies a prototype of their own Dizzy game using official graphics, not a reconstruction of a specified original adventure. Source tree has custom action classes.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/da-nie/Dizzy-game-"
  },
  {
    "first_indexed": "2026-10-28",
    "id": "github-da-nie-dizzy-psp-game",
    "kind": "github-repository",
    "last_reviewed": "2026-10-28",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "PSP adaptation of the same author-created fan prototype; reused official artwork is not recovered original mechanics. No separate original-game reconstruction identity established.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/da-nie/Dizzy-PSP-Game"
  },
  {
    "first_indexed": "2026-10-28",
    "id": "github-da-nie-dizzygame-qt",
    "kind": "github-repository",
    "last_reviewed": "2026-10-28",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Qt Windows adaptation of the same fan prototype, with documented screen judder/no vertical synchronization; not an independently recovered Dizzy title.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/da-nie/DizzyGame-Qt-"
  },
  {
    "first_indexed": "2026-10-28",
    "id": "github-da-nie-dizzy-game-linux",
    "kind": "github-repository",
    "last_reviewed": "2026-10-28",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Linux Qt 5 adaptation of the same fan prototype. Do not multiply project counts for equivalent platform forks lacking a recovered original-game basis.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/da-nie/Dizzy-game-Linux"
  },
  {
    "first_indexed": "2026-10-28",
    "id": "github-dizzyage-custom-code",
    "kind": "github-repository",
    "last_reviewed": "2026-10-28",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Small authoring tutorial collection, including dragon/climbing/jetpack examples, not a specific game reconstruction. Relevant support material but outside this game-first addition batch.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/DizzyAGE/custom_code"
  },
  {
    "first_indexed": "2026-10-28",
    "id": "github-salazkin-dizzy-canvas",
    "kind": "github-repository",
    "last_reviewed": "2026-10-28",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Generic WebGL 2D renderer; Dizzy name is a keyword collision, no connection to the Oliver Twins game series established.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/salazkin/dizzy-canvas"
  },
  {
    "first_indexed": "2026-10-28",
    "id": "github-aevri-kwik-snax",
    "kind": "github-repository",
    "last_reviewed": "2026-10-28",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Food recipes, not the Codemasters game; exact-name keyword collision.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/aevri/kwik_snax"
  }
]
```

## Decisions

```json
[
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/RyanMallon/dizzy/blob/3e28cfbdcda36b5ae8b36d0c2a5b90dc849705d2/README.md",
      "https://github.com/RyanMallon/dizzy/blob/3e28cfbdcda36b5ae8b36d0c2a5b90dc849705d2/dizzy_pack.py",
      "https://github.com/RyanMallon/dizzy/blob/3e28cfbdcda36b5ae8b36d0c2a5b90dc849705d2/stage_view.py"
    ],
    "id": "discovery-2026-10-28-p91-ryanmallon-dizzy",
    "project_ids": [
      "ryanmallon-dizzy"
    ],
    "reason": "Documented NDX/RES chunk indexes and variable-bit dictionary decompression, unpack/repack scripts, sprite and layered-stage viewers. This is original game resource analysis, not a reconstructed playable engine.",
    "reviewed_at": "2026-10-28",
    "source_ids": [
      "github-ryanmallon-dizzy"
    ],
    "title": "RyanMallon/dizzy",
    "url": "https://github.com/RyanMallon/dizzy"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/primo-malvado/dizzy_magicland_disassemble/blob/e051974f967681968ca19876ecc5364a5175e01d/README.md",
      "https://github.com/primo-malvado/dizzy_magicland_disassemble/blob/e051974f967681968ca19876ecc5364a5175e01d/build/build.sh",
      "https://github.com/primo-malvado/dizzy_magicland_disassemble/blob/e051974f967681968ca19876ecc5364a5175e01d/desenha_sprite.asm",
      "https://github.com/primo-malvado/dizzy_magicland_disassemble/blob/e051974f967681968ca19876ecc5364a5175e01d/disassemble/disasemble_03_04.pl"
    ],
    "id": "discovery-2026-10-28-p91-primo-malvado-dizzy-magicland-disassemble",
    "project_ids": [
      "primo-malvado-dizzy-magicland-disassemble"
    ],
    "reason": "Game-specific code/data declarations identify map records, function indexes, sprite masks and named drawing operations. Generated and refactored assembly retain generic addresses and unknown regions, so semantic analysis is incomplete.",
    "reviewed_at": "2026-10-28",
    "source_ids": [
      "github-primo-malvado-dizzy-magicland-disassemble"
    ],
    "title": "primo-malvado/dizzy_magicland_disassemble",
    "url": "https://github.com/primo-malvado/dizzy_magicland_disassemble"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/picosonic/D3/blob/80a881ebe8dadb60392c92b100e0e74d255a0945/README.md",
      "https://github.com/picosonic/D3/blob/80a881ebe8dadb60392c92b100e0e74d255a0945/beeb/make.sh",
      "https://github.com/picosonic/D3/blob/80a881ebe8dadb60392c92b100e0e74d255a0945/beeb/dizzy3.asm",
      "https://github.com/picosonic/D3/blob/80a881ebe8dadb60392c92b100e0e74d255a0945/original_source/X-ALL.TXT"
    ],
    "id": "discovery-2026-10-28-p91-picosonic-d3",
    "project_ids": [
      "picosonic-d3"
    ],
    "reason": "Contains Oliver Twins PDS-era Z80 source with Spectrum/CPC build choices, native 6502 BBC gameplay, and a separately unfinished C64 cartridge disassembly. Main loop, inventory and actor routines are translated into host assembly rather than a Z80 interpreter.",
    "reviewed_at": "2026-10-28",
    "source_ids": [
      "github-picosonic-d3"
    ],
    "title": "picosonic/D3",
    "url": "https://github.com/picosonic/D3"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/nzeemin/bk0011m-dizzy1td-rev/blob/e6f154e9f1d5ea8133b5fc98f459cbc016851e04/README.md",
      "https://github.com/nzeemin/bk0011m-dizzy1td-rev/blob/e6f154e9f1d5ea8133b5fc98f459cbc016851e04/!compilelink.bat",
      "https://github.com/nzeemin/bk0011m-dizzy1td-rev/blob/e6f154e9f1d5ea8133b5fc98f459cbc016851e04/REVERSE.md",
      "https://github.com/nzeemin/bk0011m-dizzy1td-rev/blob/e6f154e9f1d5ea8133b5fc98f459cbc016851e04/dizzy.asm"
    ],
    "id": "discovery-2026-10-28-p91-nzeemin-bk0011m-dizzy1td-rev",
    "project_ids": [
      "nzeemin-bk0011m-dizzy1td-rev"
    ],
    "reason": "Annotated MACRO-11-style reconstruction of the 1994 MBS/TD adaptation, with room, sprite, bank-switching, collision and Russian dialogue analysis. Despite the name Dizzy 1, this is a reworking of Fantasy World Dizzy.",
    "reviewed_at": "2026-10-28",
    "source_ids": [
      "github-nzeemin-bk0011m-dizzy1td-rev"
    ],
    "title": "nzeemin/bk0011m-dizzy1td-rev",
    "url": "https://github.com/nzeemin/bk0011m-dizzy1td-rev"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/Chegleyev/Dizzy3Remake/blob/b05aaeb3db081ee10b8720a8d9d66dd7612729d1/README.md",
      "https://github.com/Chegleyev/Dizzy3Remake/blob/b05aaeb3db081ee10b8720a8d9d66dd7612729d1/packages/engine/src/collision.ts",
      "https://github.com/Chegleyev/Dizzy3Remake/blob/b05aaeb3db081ee10b8720a8d9d66dd7612729d1/packages/engine/test/golden.test.ts",
      "https://github.com/Chegleyev/Dizzy3Remake/blob/b05aaeb3db081ee10b8720a8d9d66dd7612729d1/packages/engine/src/inventory.ts",
      "https://github.com/Chegleyev/Dizzy3Remake/blob/b05aaeb3db081ee10b8720a8d9d66dd7612729d1/packages/engine/src/engine.ts"
    ],
    "id": "discovery-2026-10-28-p91-chegleyev-dizzy3remake",
    "project_ids": [
      "chegleyev-dizzy3remake"
    ],
    "reason": "Semantic port of the 2023 Russian extended 128K version. Named collision and inventory functions identify original addresses; original-derived 12.5 Hz integer logic is tested against captured traces. Rendering interpolation, stable inventory slots, saves and remaster colouring are intentional changes.",
    "reviewed_at": "2026-10-28",
    "source_ids": [
      "github-chegleyev-dizzy3remake"
    ],
    "title": "Chegleyev/Dizzy3Remake",
    "url": "https://github.com/Chegleyev/Dizzy3Remake"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/README.md",
      "https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/core/player/player.gd",
      "https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/tests/integration/test_win_path.gd.uid",
      "https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/games/treasure-island/data/screen_map.md",
      "https://github.com/dev-vpa/dizzy-adventures-remake/blob/8c44f675350a0294b00f8ad5d9daaa2e36b0444e/tests/integration/test_win_path.gd"
    ],
    "id": "discovery-2026-10-28-p91-dev-vpa-dizzy-adventures-remake",
    "project_ids": [
      "dev-vpa-dizzy-adventures-remake"
    ],
    "reason": "Substantial game recreation with 51 claimed level scenes, inventory trades, snorkel/water hazards, thirty coins, boat assembly and taxman ending. Content map cites Spectrum/C64 walkthroughs; Godot gravity and collision implement new mechanics rather than proven recovered original algorithms.",
    "reviewed_at": "2026-10-28",
    "source_ids": [
      "github-dev-vpa-dizzy-adventures-remake"
    ],
    "title": "dev-vpa/dizzy-adventures-remake",
    "url": "https://github.com/dev-vpa/dizzy-adventures-remake"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/N0t4R0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/README.md",
      "https://github.com/N0t4R0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/ports/dizzy-coco2/README.md",
      "https://github.com/N0t4R0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/ports/dizzy-coco2/PORT.toml",
      "https://github.com/N0t4R0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/ports/dizzy-coco2/docs/PROVENANCE.md",
      "https://github.com/N0t4R0b0t/game-port-factory/blob/86bb9bf98f9837c12378781d8f678cabbd15f2b0/ports/dizzy-coco2/target/dragon_code.asm"
    ],
    "id": "discovery-2026-10-28-p91-n0t4r0b0t-game-port-factory",
    "project_ids": [
      "n0t4r0b0t-game-port-factory"
    ],
    "reason": "Native 6809 implementation derived from released Fantasy World rules and data, alongside reusable differential-emulator tooling. Current port notes describe full tape/floppy routes, dialogue and thirty coins; the smaller run build has only 31 base rooms.",
    "reviewed_at": "2026-10-28",
    "source_ids": [
      "github-n0t4r0b0t-game-port-factory"
    ],
    "title": "N0t4R0b0t/game-port-factory",
    "url": "https://github.com/N0t4R0b0t/game-port-factory"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/nzeemin/uknc-dizzylogcabin/blob/8bcd35d8a6ccca71448c86b58490415fa316deb8/README.md",
      "https://github.com/nzeemin/uknc-dizzylogcabin/blob/8bcd35d8a6ccca71448c86b58490415fa316deb8/!compilelink.bat",
      "https://github.com/nzeemin/uknc-dizzylogcabin/blob/8bcd35d8a6ccca71448c86b58490415fa316deb8/DIZZYL.ASM"
    ],
    "id": "discovery-2026-10-28-p91-nzeemin-uknc-dizzylogcabin",
    "project_ids": [
      "nzeemin-uknc-dizzylogcabin"
    ],
    "reason": "Native port of the winter Log Cabin mini-adventure using source supplied by BK author Sergey Shcherbakovsky. Assembly adapts display access and title RLE handling to UKNC hardware.",
    "reviewed_at": "2026-10-28",
    "source_ids": [
      "github-nzeemin-uknc-dizzylogcabin"
    ],
    "title": "nzeemin/uknc-dizzylogcabin",
    "url": "https://github.com/nzeemin/uknc-dizzylogcabin"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/Verm-V/Ghastly-Getaway-Dizzy/blob/a4a7bf52521716ff0048766cad09542bebf8dee1/readme.txt",
      "https://github.com/Verm-V/Ghastly-Getaway-Dizzy/blob/a4a7bf52521716ff0048766cad09542bebf8dee1/data/defines.txt",
      "https://github.com/Verm-V/Ghastly-Getaway-Dizzy/blob/a4a7bf52521716ff0048766cad09542bebf8dee1/ghastly-getaway-gizzy.dseprj",
      "https://github.com/Verm-V/Ghastly-Getaway-Dizzy/blob/a4a7bf52521716ff0048766cad09542bebf8dee1/data/code1.txt"
    ],
    "id": "discovery-2026-10-28-p91-verm-v-ghastly-getaway-dizzy",
    "project_ids": [
      "verm-v-ghastly-getaway-dizzy"
    ],
    "reason": "Game-specific demake of the PC DizzyAGE adventure, containing hotel rooms, dialogue, item identifiers and event/puzzle scripts. This is a different fan adventure, not a commercial Dizzy-series decompilation.",
    "reviewed_at": "2026-10-28",
    "source_ids": [
      "github-verm-v-ghastly-getaway-dizzy"
    ],
    "title": "Verm-V/Ghastly-Getaway-Dizzy",
    "url": "https://github.com/Verm-V/Ghastly-Getaway-Dizzy"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/leprosarium/prolozzy/blob/0049a5b7f7c47fad451c11ff21eb0868da4c7404/README.md",
      "https://github.com/leprosarium/prolozzy/blob/0049a5b7f7c47fad451c11ff21eb0868da4c7404/Game/DizPlayer.cpp",
      "https://github.com/leprosarium/prolozzy/blob/0049a5b7f7c47fad451c11ff21eb0868da4c7404/Game/DizScript.cpp"
    ],
    "id": "discovery-2026-10-28-p91-leprosarium-prolozzy",
    "project_ids": [
      "leprosarium-prolozzy"
    ],
    "reason": "DizzyAGE-derived native engine replaces scripting integration with SWI-Prolog. C++ player accessors and material/collision predicates expose actual engine state to Prolog, beyond a README-only proposal.",
    "reviewed_at": "2026-10-28",
    "source_ids": [
      "github-leprosarium-prolozzy"
    ],
    "title": "leprosarium/prolozzy",
    "url": "https://github.com/leprosarium/prolozzy"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/dkrutskikh/dizzy-kwik-snax-redux/blob/e98affa9c4a58dcbea21d8bee5ec25a9ae92cfb7/README.md",
      "https://github.com/dkrutskikh/dizzy-kwik-snax-redux/blob/e98affa9c4a58dcbea21d8bee5ec25a9ae92cfb7/game/game.cpp"
    ],
    "id": "discovery-2026-10-28-p91-dkrutskikh-dizzy-kwik-snax-redux",
    "project_ids": [],
    "reason": "Design documentation and multi-platform build skeleton are present, but game/game.cpp only displays a title and waits for VBlank (or immediately returns on desktop). No Kwik Snax gameplay implemented at this revision.",
    "reviewed_at": "2026-10-28",
    "source_ids": [
      "github-dkrutskikh-dizzy-kwik-snax-redux"
    ],
    "title": "dkrutskikh/dizzy-kwik-snax-redux",
    "url": "https://github.com/dkrutskikh/dizzy-kwik-snax-redux"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/dkrutskikh/yolkfolk-legacy/blob/7d182f6e560f44e5984a8e75c704b80528f2f3b3/README.md",
      "https://github.com/dkrutskikh/yolkfolk-legacy/blob/7d182f6e560f44e5984a8e75c704b80528f2f3b3/source/template.cpp"
    ],
    "id": "discovery-2026-10-28-p91-dkrutskikh-yolkfolk-legacy",
    "project_ids": [],
    "reason": "Source is the GBA Hello World template, not a reconstructed Dizzy game.",
    "reviewed_at": "2026-10-28",
    "source_ids": [
      "github-dkrutskikh-yolkfolk-legacy"
    ],
    "title": "dkrutskikh/yolkfolk-legacy",
    "url": "https://github.com/dkrutskikh/yolkfolk-legacy"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/jane-alesi/game-demo/blob/c88a733e177d2677a6f56997b9cc0f04cbbbc6f9/README.md",
      "https://github.com/jane-alesi/game-demo/blob/c88a733e177d2677a6f56997b9cc0f04cbbbc6f9/js/game.js"
    ],
    "id": "discovery-2026-10-28-p91-jane-alesi-game-demo",
    "project_ids": [],
    "reason": "Treasure Island-labelled Canvas demo has four simple treasures, procedural scenery and a collect-all win condition; inventory and multiple levels are future work. It does not reconstruct the original puzzle adventure. Explicit AI authorship does not change this scope finding.",
    "reviewed_at": "2026-10-28",
    "source_ids": [
      "github-jane-alesi-game-demo"
    ],
    "title": "jane-alesi/game-demo",
    "url": "https://github.com/jane-alesi/game-demo"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/fwmakc/dizzygame/blob/d08909a4b41ae1ba277b540f85e123c49a08c996/README.md"
    ],
    "id": "discovery-2026-10-28-p91-fwmakc-dizzygame",
    "project_ids": [],
    "reason": "Construct 2 runtime export and packaged event/assets are present, but no original project source or evidence of original-game algorithm recovery established. Keep as a fan-demo lead rather than count a completed reconstruction.",
    "reviewed_at": "2026-10-28",
    "source_ids": [
      "github-fwmakc-dizzygame"
    ],
    "title": "fwmakc/dizzygame",
    "url": "https://github.com/fwmakc/dizzygame"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/sau412/Dizzy_sandbox/blob/c1fb0c3b1d4b505582eb54d783a86c1738c0a3bf/README.md"
    ],
    "id": "discovery-2026-10-28-p91-sau412-dizzy-sandbox",
    "project_ids": [],
    "reason": "Seven-file animation/experiment sandbox, not a recovered full Dizzy game.",
    "reviewed_at": "2026-10-28",
    "source_ids": [
      "github-sau412-dizzy-sandbox"
    ],
    "title": "sau412/Dizzy_sandbox",
    "url": "https://github.com/sau412/Dizzy_sandbox"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/iratahack/DizzyVIII/blob/1e1bf44176d7eb4a0aad42bc2fd6c519dfcdc2e2/README.md",
      "https://github.com/iratahack/DizzyVIII/blob/1e1bf44176d7eb4a0aad42bc2fd6c519dfcdc2e2/Dizzy VIII - Wonderful Dizzy (2020) v1.5.pok"
    ],
    "id": "discovery-2026-10-28-p91-iratahack-dizzyviii",
    "project_ids": [],
    "reason": "Only a short Wonderful Dizzy cheat POK file and README; insufficient standalone reconstruction/analysis project.",
    "reviewed_at": "2026-10-28",
    "source_ids": [
      "github-iratahack-dizzyviii"
    ],
    "title": "iratahack/DizzyVIII",
    "url": "https://github.com/iratahack/DizzyVIII"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/danadrianmirea/dizzyage/blob/8e52d238cca482321a37f1d4a297100ccaf2eb33/README.md",
      "https://github.com/danadrianmirea/dizzyage/blob/8e52d238cca482321a37f1d4a297100ccaf2eb33/dizzyage/readme.txt"
    ],
    "id": "discovery-2026-10-28-p91-danadrianmirea-dizzyage",
    "project_ids": [],
    "reason": "Learning collection bundles DizzyAGE 2.4 engine/editor source and fan-game examples. Original Simion authorship is preserved in bundled documentation; do not promote this mirror as an independent reconstruction or confuse it with commercial Dizzy source.",
    "reviewed_at": "2026-10-28",
    "source_ids": [
      "github-danadrianmirea-dizzyage"
    ],
    "title": "danadrianmirea/dizzyage",
    "url": "https://github.com/danadrianmirea/dizzyage"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/da-nie/Dizzy-game-/tree/7e80ec4fb9f07a3ed2998ca43497405d16bc713a"
    ],
    "id": "discovery-2026-10-28-p91-da-nie-dizzy-game",
    "project_ids": [],
    "reason": "Author identifies a prototype of their own Dizzy game using official graphics, not a reconstruction of a specified original adventure. Source tree has custom action classes.",
    "reviewed_at": "2026-10-28",
    "source_ids": [
      "github-da-nie-dizzy-game"
    ],
    "title": "da-nie/Dizzy-game-",
    "url": "https://github.com/da-nie/Dizzy-game-"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/da-nie/Dizzy-PSP-Game/tree/7468e4dfde3c8927ab64d45e32b3a27d068963b6"
    ],
    "id": "discovery-2026-10-28-p91-da-nie-dizzy-psp-game",
    "project_ids": [],
    "reason": "PSP adaptation of the same author-created fan prototype; reused official artwork is not recovered original mechanics. No separate original-game reconstruction identity established.",
    "reviewed_at": "2026-10-28",
    "source_ids": [
      "github-da-nie-dizzy-psp-game"
    ],
    "title": "da-nie/Dizzy-PSP-Game",
    "url": "https://github.com/da-nie/Dizzy-PSP-Game"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/da-nie/DizzyGame-Qt-/tree/d61b4da82e64560752b404f41e1aca53042d982e"
    ],
    "id": "discovery-2026-10-28-p91-da-nie-dizzygame-qt",
    "project_ids": [],
    "reason": "Qt Windows adaptation of the same fan prototype, with documented screen judder/no vertical synchronization; not an independently recovered Dizzy title.",
    "reviewed_at": "2026-10-28",
    "source_ids": [
      "github-da-nie-dizzygame-qt"
    ],
    "title": "da-nie/DizzyGame-Qt-",
    "url": "https://github.com/da-nie/DizzyGame-Qt-"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/da-nie/Dizzy-game-Linux/tree/462a1ccd47c6ed8d6ee82d4f2e3e5fe7480a2536"
    ],
    "id": "discovery-2026-10-28-p91-da-nie-dizzy-game-linux",
    "project_ids": [],
    "reason": "Linux Qt 5 adaptation of the same fan prototype. Do not multiply project counts for equivalent platform forks lacking a recovered original-game basis.",
    "reviewed_at": "2026-10-28",
    "source_ids": [
      "github-da-nie-dizzy-game-linux"
    ],
    "title": "da-nie/Dizzy-game-Linux",
    "url": "https://github.com/da-nie/Dizzy-game-Linux"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/DizzyAGE/custom_code/blob/332a1f3a2dfc1afbf3b3968cda00f96b48c79266/README.md"
    ],
    "id": "discovery-2026-10-28-p91-dizzyage-custom-code",
    "project_ids": [],
    "reason": "Small authoring tutorial collection, including dragon/climbing/jetpack examples, not a specific game reconstruction. Relevant support material but outside this game-first addition batch.",
    "reviewed_at": "2026-10-28",
    "source_ids": [
      "github-dizzyage-custom-code"
    ],
    "title": "DizzyAGE/custom_code",
    "url": "https://github.com/DizzyAGE/custom_code"
  },
  {
    "decision": "excluded",
    "evidence_urls": [
      "https://github.com/salazkin/dizzy-canvas/tree/4c2297066d662ab3094e4f4491ff0c7795adcceb"
    ],
    "id": "discovery-2026-10-28-p91-salazkin-dizzy-canvas",
    "project_ids": [],
    "reason": "Generic WebGL 2D renderer; Dizzy name is a keyword collision, no connection to the Oliver Twins game series established.",
    "reviewed_at": "2026-10-28",
    "source_ids": [
      "github-salazkin-dizzy-canvas"
    ],
    "title": "salazkin/dizzy-canvas",
    "url": "https://github.com/salazkin/dizzy-canvas"
  },
  {
    "decision": "excluded",
    "evidence_urls": [
      "https://github.com/aevri/kwik_snax/blob/1adbb9a286c6a3f9ae6763886f011677207b515d/README.md"
    ],
    "id": "discovery-2026-10-28-p91-aevri-kwik-snax",
    "project_ids": [],
    "reason": "Food recipes, not the Codemasters game; exact-name keyword collision.",
    "reviewed_at": "2026-10-28",
    "source_ids": [
      "github-aevri-kwik-snax"
    ],
    "title": "aevri/kwik_snax",
    "url": "https://github.com/aevri/kwik_snax"
  }
]
```

## Research event notes

Root personally searched the Dizzy series, individual titles, source/disassembly/remake terms, language-specific repositories and linked authors. Reviewed 24 pinned repository roots: ten additions and fourteen held/excluded candidates. No worker performed discovery. Existing catalogue contains the unrelated madmoose DOS disassembler and Mushroom Pie engine; neither is duplicated. Treasure Island remake is explicitly distinguished from original-algorithm recovery; the stronger Fantasy World ports and Magicland disassembly retain edition, timing, build and fidelity limitations. No upstream code was executed. Separately fetched HEAD commits match pinned tree references. Cached proof texts are included only when their Git blob hashes match; large or encoding-converted sources remain linked rather than presented as byte-verified cached proofs. Dr. Titus describes independently disassembling Treasure Island in a primary-author forum post, but a public source deliverable was not established in this pass; do not turn that anecdote into a source-reconstruction repository entry. This is a broad series-focused pass, not a claim of exhaustive discovery.
