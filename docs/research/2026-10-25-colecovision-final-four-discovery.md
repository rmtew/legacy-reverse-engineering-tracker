# Complete the ColecoVision title-source review and rotate fresh platform searches

Reviewed the final four title directories in tony-cruise/colecovision-games-source, promoted four compilable Z80 disassemblies, completed the 24-title queue task, and screened fresh Atari 8-bit, Apple II, MSX, TI-99 and BBC Micro repository searches against existing catalogue state.

Date: 2026-10-25 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- space-panic-colecovision-disassembly / Build (reviewed): This pass did not run the assembler, execute the ROM or perform a byte comparison. The author's 'same code' statement was not treated as an independently established byte-exact build.
- space-panic-colecovision-disassembly / Runtime profiles (no-evidence-found): README and source header were checked; they discuss emulator-specific behavior but state no separate minimum CPU, RAM, chipset or ROM requirement.
- space-panic-colecovision-disassembly / AI (no-evidence-found): The inspected README and assembly header contain no development-AI attribution; absence does not establish non-use.
- squish-em-featuring-sam-colecovision-disassembly / Build (reviewed): This pass did not run the assembler, execute the ROM or perform a byte comparison.
- squish-em-featuring-sam-colecovision-disassembly / Runtime profiles (no-evidence-found): README and source header were checked; they identify a ColecoVision ROM but state no separate minimum CPU, RAM, chipset or ROM requirement.
- squish-em-featuring-sam-colecovision-disassembly / AI (no-evidence-found): The inspected README and assembly header contain no development-AI attribution; absence does not establish non-use.
- star-wars-arcade-colecovision-disassembly / Build (reviewed): This pass did not run the assembler, execute the ROM or perform a byte comparison.
- star-wars-arcade-colecovision-disassembly / Runtime profiles (no-evidence-found): README and source header were checked; the 16 KB ROM layout and ColecoVision devices are documented, but no separate minimum CPU, RAM, chipset or ROM requirement is stated.
- the-heist-colecovision-disassembly / Build (reviewed): This pass did not run the assembler, execute the ROM or perform a byte comparison.
- the-heist-colecovision-disassembly / Runtime profiles (no-evidence-found): README and source header were checked; the 16 KB ROM layout and ColecoVision devices are documented, but no separate minimum CPU, RAM, chipset or ROM requirement is stated.

## Space Panic — ColecoVision compilable disassembly

Project ID: space-panic-colecovision-disassembly · Overall audit: reviewed

### Typed catalogue values

```json
{
  "ai": {
    "tools": [],
    "usage": null
  },
  "build": {
    "byte_exact": null,
    "compilable": true,
    "playable": null,
    "runnable": null
  },
  "display_title": "Space Panic — ColecoVision compilable disassembly",
  "execution_paths": null,
  "github_branch": null,
  "github_path": "games/Space-Panic",
  "id": "space-panic-colecovision-disassembly",
  "last_activity": null,
  "last_checked": "2026-10-25",
  "project_url": "https://github.com/tony-cruise/colecovision-games-source/tree/main/games/Space-Panic",
  "re_started": null,
  "reconstructed_languages": [
    "Z80 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/tony-cruise/colecovision-games-source",
  "runtime_profiles": [],
  "source_cpu": [
    "Z80"
  ],
  "source_language": [
    "Z80 machine code"
  ],
  "source_platforms": [
    "ColecoVision"
  ],
  "status": "compilable disassembly",
  "subjects": [
    "Space Panic"
  ],
  "tags": [
    "ColecoVision",
    "Z80",
    "Space Panic"
  ],
  "target_cpu": [
    "Z80"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "ColecoVision"
  ],
  "techniques": [
    "Z80 disassembly",
    "control-flow annotation",
    "ROM reconstruction"
  ],
  "title": "Space Panic",
  "tool_kinds": [],
  "types": [
    "compilable game disassembly"
  ],
  "upstream_name": "Space Panic",
  "work_kinds": [
    "disassembly",
    "source-reconstruction"
  ]
}
```

### Identity (reviewed)

The title README and assembly header identify Space Panic as a distinct reconstruction by Captain Cozmos inside the shared game-source repository.
- https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/Space-Panic/README.md
- https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/Space-Panic/space-panic.asm

### Classification (reviewed)

The README calls it a compilable disassembly and the annotated source reconstructs the ColecoVision game ROM; it is not presented as original homebrew.
- https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/Space-Panic/README.md
- https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/Space-Panic/space-panic.asm

### Source CPU (reviewed)

The assembly source explicitly selects CPU Z80 for the original ColecoVision program.
- https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/Space-Panic/space-panic.asm

### Target CPU (reviewed)

The same Z80 assembly source emits the reconstructed ColecoVision ROM.
- https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/Space-Panic/space-panic.asm

### Build (reviewed)

The README calls the listing compilable and the source contains an explicit ROM output directive. Limitations: This pass did not run the assembler, execute the ROM or perform a byte comparison. The author's 'same code' statement was not treated as an independently established byte-exact build.
- https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/Space-Panic/README.md
- https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/Space-Panic/space-panic.asm

### Runtime profiles (no-evidence-found)

README and source header were checked; they discuss emulator-specific behavior but state no separate minimum CPU, RAM, chipset or ROM requirement.
- https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/Space-Panic/README.md
- https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/Space-Panic/space-panic.asm

### AI (no-evidence-found)

The inspected README and assembly header contain no development-AI attribution; absence does not establish non-use.
- https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/Space-Panic/README.md
- https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/Space-Panic/space-panic.asm

### Relationships (reviewed)

Space Panic is one separately titled directory in the 24-game collection and is retained as an independent subject record; the shared repository does not collapse the title-level work into one game.
- https://github.com/tony-cruise/colecovision-games-source/tree/main/games/Space-Panic
- https://github.com/tony-cruise/colecovision-games-source

## Squish-em Featuring Sam — ColecoVision compilable disassembly

Project ID: squish-em-featuring-sam-colecovision-disassembly · Overall audit: reviewed

### Typed catalogue values

```json
{
  "ai": {
    "tools": [],
    "usage": null
  },
  "build": {
    "byte_exact": null,
    "compilable": true,
    "playable": null,
    "runnable": null
  },
  "display_title": "Squish-em Featuring Sam — ColecoVision compilable disassembly",
  "execution_paths": null,
  "github_branch": null,
  "github_path": "games/Squish-em-Featuring-Sam",
  "id": "squish-em-featuring-sam-colecovision-disassembly",
  "last_activity": null,
  "last_checked": "2026-10-25",
  "project_url": "https://github.com/tony-cruise/colecovision-games-source/tree/main/games/Squish-em-Featuring-Sam",
  "re_started": null,
  "reconstructed_languages": [
    "Z80 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/tony-cruise/colecovision-games-source",
  "runtime_profiles": [],
  "source_cpu": [
    "Z80"
  ],
  "source_language": [
    "Z80 machine code"
  ],
  "source_platforms": [
    "ColecoVision"
  ],
  "status": "compilable disassembly",
  "subjects": [
    "Squish-em Featuring Sam"
  ],
  "tags": [
    "ColecoVision",
    "Z80",
    "Squish-em Featuring Sam"
  ],
  "target_cpu": [
    "Z80"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "ColecoVision"
  ],
  "techniques": [
    "Z80 disassembly",
    "control-flow annotation",
    "ROM reconstruction"
  ],
  "title": "Squish-em Featuring Sam",
  "tool_kinds": [],
  "types": [
    "compilable game disassembly"
  ],
  "upstream_name": "Squish-em Featuring Sam",
  "work_kinds": [
    "disassembly",
    "source-reconstruction"
  ]
}
```

### Identity (reviewed)

The title README and assembly header identify Squish-em Featuring Sam as a distinct reconstruction by Captain Cozmos inside the shared repository.
- https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/Squish-em-Featuring-Sam/README.md
- https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/Squish-em-Featuring-Sam/squish-em-featuring-sam.asm

### Classification (reviewed)

The README calls it a compilable disassembly and the annotated source reconstructs the ColecoVision game ROM; it is not presented as original homebrew.
- https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/Squish-em-Featuring-Sam/README.md
- https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/Squish-em-Featuring-Sam/squish-em-featuring-sam.asm

### Source CPU (reviewed)

The assembly source explicitly selects CPU Z80 for the original ColecoVision program.
- https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/Squish-em-Featuring-Sam/squish-em-featuring-sam.asm

### Target CPU (reviewed)

The same Z80 assembly source emits the reconstructed ColecoVision ROM.
- https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/Squish-em-Featuring-Sam/squish-em-featuring-sam.asm

### Build (reviewed)

The README calls the listing compilable and the source contains explicit ROM output and CPU directives. Limitations: This pass did not run the assembler, execute the ROM or perform a byte comparison.
- https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/Squish-em-Featuring-Sam/README.md
- https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/Squish-em-Featuring-Sam/squish-em-featuring-sam.asm

### Runtime profiles (no-evidence-found)

README and source header were checked; they identify a ColecoVision ROM but state no separate minimum CPU, RAM, chipset or ROM requirement.
- https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/Squish-em-Featuring-Sam/README.md
- https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/Squish-em-Featuring-Sam/squish-em-featuring-sam.asm

### AI (no-evidence-found)

The inspected README and assembly header contain no development-AI attribution; absence does not establish non-use.
- https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/Squish-em-Featuring-Sam/README.md
- https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/Squish-em-Featuring-Sam/squish-em-featuring-sam.asm

### Relationships (reviewed)

Squish-em Featuring Sam is one separately titled directory in the 24-game collection and is retained as an independent subject record.
- https://github.com/tony-cruise/colecovision-games-source/tree/main/games/Squish-em-Featuring-Sam
- https://github.com/tony-cruise/colecovision-games-source

## Star Wars Arcade — ColecoVision compilable disassembly

Project ID: star-wars-arcade-colecovision-disassembly · Overall audit: reviewed

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
    "compilable": true,
    "playable": null,
    "runnable": null
  },
  "display_title": "Star Wars Arcade — ColecoVision compilable disassembly",
  "execution_paths": null,
  "github_branch": null,
  "github_path": "games/Star Wars Arcade",
  "id": "star-wars-arcade-colecovision-disassembly",
  "last_activity": null,
  "last_checked": "2026-10-25",
  "project_url": "https://github.com/tony-cruise/colecovision-games-source/tree/main/games/Star%20Wars%20Arcade",
  "re_started": null,
  "reconstructed_languages": [
    "Z80 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/tony-cruise/colecovision-games-source",
  "runtime_profiles": [],
  "source_cpu": [
    "Z80"
  ],
  "source_language": [
    "Z80 machine code"
  ],
  "source_platforms": [
    "ColecoVision"
  ],
  "status": "compilable disassembly",
  "subjects": [
    "Star Wars: The Arcade Game"
  ],
  "tags": [
    "ColecoVision",
    "Z80",
    "Star Wars: The Arcade Game",
    "Claude Code"
  ],
  "target_cpu": [
    "Z80"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "ColecoVision"
  ],
  "techniques": [
    "Z80 disassembly",
    "control-flow annotation",
    "ROM reconstruction"
  ],
  "title": "Star Wars Arcade",
  "tool_kinds": [],
  "types": [
    "compilable game disassembly"
  ],
  "upstream_name": "Star Wars Arcade",
  "work_kinds": [
    "disassembly",
    "source-reconstruction"
  ]
}
```

### Identity (reviewed)

The title README and annotated assembly identify the ColecoVision Star Wars arcade conversion as a distinct reconstruction inside the shared repository.
- https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/Star%20Wars%20Arcade/README.md
- https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/Star%20Wars%20Arcade/star-wars-arcade.asm

### Classification (reviewed)

The README calls it a compilable disassembly and the source reconstructs a 16 KB ColecoVision game ROM with annotated VDP, sound, RAM and control-flow structure.
- https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/Star%20Wars%20Arcade/README.md
- https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/Star%20Wars%20Arcade/star-wars-arcade.asm

### Source CPU (reviewed)

The assembly source explicitly selects CPU Z80 for the original ColecoVision program.
- https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/Star%20Wars%20Arcade/star-wars-arcade.asm

### Target CPU (reviewed)

The same Z80 assembly source emits the reconstructed ColecoVision ROM.
- https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/Star%20Wars%20Arcade/star-wars-arcade.asm

### Build (reviewed)

The README calls the listing compilable and the source contains explicit ROM output, CPU and origin directives. Limitations: This pass did not run the assembler, execute the ROM or perform a byte comparison.
- https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/Star%20Wars%20Arcade/README.md
- https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/Star%20Wars%20Arcade/star-wars-arcade.asm

### Runtime profiles (no-evidence-found)

README and source header were checked; the 16 KB ROM layout and ColecoVision devices are documented, but no separate minimum CPU, RAM, chipset or ROM requirement is stated.
- https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/Star%20Wars%20Arcade/README.md
- https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/Star%20Wars%20Arcade/star-wars-arcade.asm

### AI (reviewed)

The title README explicitly credits Kamshaft and Claude Code for this compilable disassembly; the attribution is recorded only for this title.
- https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/Star%20Wars%20Arcade/README.md

### Relationships (reviewed)

Star Wars Arcade is one separately titled directory in the 24-game collection and is retained as an independent subject record.
- https://github.com/tony-cruise/colecovision-games-source/tree/main/games/Star%20Wars%20Arcade
- https://github.com/tony-cruise/colecovision-games-source

## The Heist — ColecoVision compilable disassembly

Project ID: the-heist-colecovision-disassembly · Overall audit: reviewed

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
    "compilable": true,
    "playable": null,
    "runnable": null
  },
  "display_title": "The Heist — ColecoVision compilable disassembly",
  "execution_paths": null,
  "github_branch": null,
  "github_path": "games/The Heist",
  "id": "the-heist-colecovision-disassembly",
  "last_activity": null,
  "last_checked": "2026-10-25",
  "project_url": "https://github.com/tony-cruise/colecovision-games-source/tree/main/games/The%20Heist",
  "re_started": null,
  "reconstructed_languages": [
    "Z80 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/tony-cruise/colecovision-games-source",
  "runtime_profiles": [],
  "source_cpu": [
    "Z80"
  ],
  "source_language": [
    "Z80 machine code"
  ],
  "source_platforms": [
    "ColecoVision"
  ],
  "status": "compilable disassembly",
  "subjects": [
    "The Heist"
  ],
  "tags": [
    "ColecoVision",
    "Z80",
    "The Heist",
    "Claude Code"
  ],
  "target_cpu": [
    "Z80"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "ColecoVision"
  ],
  "techniques": [
    "Z80 disassembly",
    "control-flow annotation",
    "ROM reconstruction"
  ],
  "title": "The Heist",
  "tool_kinds": [],
  "types": [
    "compilable game disassembly"
  ],
  "upstream_name": "The Heist",
  "work_kinds": [
    "disassembly",
    "source-reconstruction"
  ]
}
```

### Identity (reviewed)

The title README and annotated assembly identify The Heist as a distinct ColecoVision reconstruction inside the shared repository.
- https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/The%20Heist/README.md
- https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/The%20Heist/the-heist.asm

### Classification (reviewed)

The README calls it a compilable disassembly and the source reconstructs a 16 KB ColecoVision game ROM with annotated VDP, sound, controller and game-logic structure.
- https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/The%20Heist/README.md
- https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/The%20Heist/the-heist.asm

### Source CPU (reviewed)

The assembly source explicitly selects CPU Z80 for the original ColecoVision program.
- https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/The%20Heist/the-heist.asm

### Target CPU (reviewed)

The same Z80 assembly source emits the reconstructed ColecoVision ROM.
- https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/The%20Heist/the-heist.asm

### Build (reviewed)

The README calls the listing compilable and the source contains explicit ROM output, CPU and origin directives. Limitations: This pass did not run the assembler, execute the ROM or perform a byte comparison.
- https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/The%20Heist/README.md
- https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/The%20Heist/the-heist.asm

### Runtime profiles (no-evidence-found)

README and source header were checked; the 16 KB ROM layout and ColecoVision devices are documented, but no separate minimum CPU, RAM, chipset or ROM requirement is stated.
- https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/The%20Heist/README.md
- https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/The%20Heist/the-heist.asm

### AI (reviewed)

The title README explicitly credits Kamshaft and Claude Code for this compilable disassembly; the attribution is recorded only for this title.
- https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/The%20Heist/README.md

### Relationships (reviewed)

The Heist is one separately titled directory in the 24-game collection and is retained as an independent subject record.
- https://github.com/tony-cruise/colecovision-games-source/tree/main/games/The%20Heist
- https://github.com/tony-cruise/colecovision-games-source

## Sources

```json
[
  {
    "first_indexed": "2026-10-25",
    "id": "search-2026-10-25-atari8-source-reconstruction",
    "kind": "github-repository-search",
    "last_reviewed": "2026-10-25",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Fresh-search slice; exact query `Atari 8-bit source reconstruction` returned no repositories in the reviewed result page.",
    "review_state": "exhausted",
    "source": "https://github.com/search?q=Atari+8-bit+source+reconstruction&type=repositories"
  },
  {
    "first_indexed": "2026-10-25",
    "id": "search-2026-10-25-apple2-decompiler",
    "kind": "github-repository-search",
    "last_reviewed": "2026-10-25",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Fresh-search slice; exact query `Apple II decompiler` returned moralrecordings/applesoft-basic-decompiler and stjeanp/applesoft-basic-decompiler. Both canonical URLs already resolve through the catalogue and reviewed duplicate/lineage decisions, so they were not re-reviewed or promoted again.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/search?q=Apple+II+decompiler&type=repositories"
  },
  {
    "first_indexed": "2026-10-25",
    "id": "search-2026-10-25-msx-disassembly",
    "kind": "github-repository-search",
    "last_reviewed": "2026-10-25",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Fresh-search slice; exact query `MSX disassembly` returned Booga-Boo, Pyramid Warp, Arkanoid, Elite, Antarctic Adventure, Road Fighter, Stardust, Topo Soft Logo, Youkai Yashiki, Ale Hop, Temptations, Demonia, Colt 36 and Sky Jaguar repositories. Every canonical URL was already represented by a project or reviewed source/decision; no material changed source was found and no duplicate was added.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/search?q=MSX+disassembly&type=repositories"
  },
  {
    "first_indexed": "2026-10-25",
    "id": "search-2026-10-25-ti99-disassembly",
    "kind": "github-repository-search",
    "last_reviewed": "2026-10-25",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Fresh-search slice; exact query `TI-99 disassembly` returned no repositories in the reviewed result page.",
    "review_state": "exhausted",
    "source": "https://github.com/search?q=TI-99+disassembly&type=repositories"
  },
  {
    "first_indexed": "2026-10-25",
    "id": "search-2026-10-25-bbc-source-reconstruction",
    "kind": "github-repository-search",
    "last_reviewed": "2026-10-25",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Fresh-search verification; exact query `\"BBC Micro\" source reconstruction` returned no repositories in the reviewed result page.",
    "review_state": "exhausted",
    "source": "https://github.com/search?q=%22BBC+Micro%22+source+reconstruction&type=repositories"
  }
]
```

## Source updates

```json
[
  {
    "id": "github-tony-cruise-colecovision-games-source",
    "last_reviewed": "2026-10-25",
    "reason": "All 24 titled game directories now have title-level primary-source reviews. Space Panic, Squish-em Featuring Sam, Star Wars Arcade and The Heist were the final four and were promoted as separate compilable Z80 disassemblies. The repository remains a useful watched collection for newly appearing titles.",
    "review_state": "substantially-reviewed"
  }
]
```

## Task updates

```json
[
  {
    "id": "task-review-colecovision-games-source-titles",
    "last_reviewed": "2026-10-25",
    "notes_append": "Reviewed the final four directories on 2026-10-25 and promoted Space Panic, Squish-em Featuring Sam, Star Wars Arcade and The Heist. All 24 titled directories now have separate title-level reviews.",
    "state": "done"
  }
]
```

## Decisions

```json
[
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/Space-Panic/README.md",
      "https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/Space-Panic/space-panic.asm"
    ],
    "id": "discovery-2026-10-25-promote-space-panic-colecovision",
    "project_ids": [
      "space-panic-colecovision-disassembly"
    ],
    "reason": "The title README explicitly calls the work a compilable disassembly, while the assembly header identifies Captain Cozmos's resolved-link reconstruction and selects Z80 ROM output. A title-scoped record preserves the independent work inside the 24-game collection.",
    "reviewed_at": "2026-10-25",
    "source_ids": [
      "github-tony-cruise-colecovision-games-source"
    ],
    "title": "Space Panic — ColecoVision compilable disassembly",
    "url": "https://github.com/tony-cruise/colecovision-games-source/tree/main/games/Space-Panic"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/Squish-em-Featuring-Sam/README.md",
      "https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/Squish-em-Featuring-Sam/squish-em-featuring-sam.asm"
    ],
    "id": "discovery-2026-10-25-promote-squish-em-colecovision",
    "project_ids": [
      "squish-em-featuring-sam-colecovision-disassembly"
    ],
    "reason": "The title README explicitly calls the work a compilable disassembly and the source identifies Captain Cozmos's Z80 ROM reconstruction. It is independently titled and scoped within the collection.",
    "reviewed_at": "2026-10-25",
    "source_ids": [
      "github-tony-cruise-colecovision-games-source"
    ],
    "title": "Squish-em Featuring Sam — ColecoVision compilable disassembly",
    "url": "https://github.com/tony-cruise/colecovision-games-source/tree/main/games/Squish-em-Featuring-Sam"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/Star%20Wars%20Arcade/README.md",
      "https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/Star%20Wars%20Arcade/star-wars-arcade.asm"
    ],
    "id": "discovery-2026-10-25-promote-star-wars-arcade-colecovision",
    "project_ids": [
      "star-wars-arcade-colecovision-disassembly"
    ],
    "reason": "The title README explicitly calls this a compilable disassembly by Kamshaft and Claude Code; the annotated Z80 source documents the 16 KB ColecoVision ROM, VDP, sound and reconstruction structure. AI attribution is scoped to this title only.",
    "reviewed_at": "2026-10-25",
    "source_ids": [
      "github-tony-cruise-colecovision-games-source"
    ],
    "title": "Star Wars Arcade — ColecoVision compilable disassembly",
    "url": "https://github.com/tony-cruise/colecovision-games-source/tree/main/games/Star%20Wars%20Arcade"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/The%20Heist/README.md",
      "https://github.com/tony-cruise/colecovision-games-source/blob/41ab5dac371b2cb84cfdf58aa323989308ad9748/games/The%20Heist/the-heist.asm"
    ],
    "id": "discovery-2026-10-25-promote-the-heist-colecovision",
    "project_ids": [
      "the-heist-colecovision-disassembly"
    ],
    "reason": "The title README explicitly calls this a compilable disassembly by Kamshaft and Claude Code; the annotated Z80 source documents the 16 KB ColecoVision ROM, VDP, sound and reconstruction structure. AI attribution is scoped to this title only.",
    "reviewed_at": "2026-10-25",
    "source_ids": [
      "github-tony-cruise-colecovision-games-source"
    ],
    "title": "The Heist — ColecoVision compilable disassembly",
    "url": "https://github.com/tony-cruise/colecovision-games-source/tree/main/games/The%20Heist"
  }
]
```

## Source ids

```json
[
  "github-tony-cruise-colecovision-games-source",
  "search-2026-10-25-atari8-source-reconstruction",
  "search-2026-10-25-apple2-decompiler",
  "search-2026-10-25-msx-disassembly",
  "search-2026-10-25-ti99-disassembly",
  "search-2026-10-25-bbc-source-reconstruction"
]
```

## Research event notes

The CPU audit queue returned zero unresolved source/target CPU areas. Fresh-search results were either already tracked/reviewed or empty; no duplicate project records were created. No minimum runtime hardware was inferred from the ColecoVision platform.
