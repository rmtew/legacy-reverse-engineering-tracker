# Game reversing and reconstruction discovery

Review eight game research and reconstruction projects.

Date: 2026-11-05 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- peterkelly-captain-bible-re / Target CPU (no-evidence-found): No independently established minimum target CPU.
- peterkelly-captain-bible-re / Runtime profiles (no-evidence-found): No independently verified hardware profile.
- peterkelly-captain-bible-re / AI (no-evidence-found): No actual AI use established from inspected evidence; absence does not prove non-use.
- s-macke-weltendaemmerung / Target CPU (no-evidence-found): No independently established minimum target CPU.
- s-macke-weltendaemmerung / Runtime profiles (no-evidence-found): No independently verified hardware profile.
- kforestland-lands-of-lore-2-re / Target CPU (no-evidence-found): No independently established minimum target CPU.
- kforestland-lands-of-lore-2-re / Runtime profiles (no-evidence-found): No independently verified hardware profile.
- kforestland-lands-of-lore-2-re / AI (no-evidence-found): No actual AI use established from inspected evidence; absence does not prove non-use.
- i-zhirov-screamer-re / Target CPU (no-evidence-found): No independently established minimum target CPU.
- i-zhirov-screamer-re / Runtime profiles (no-evidence-found): No independently verified hardware profile.
- i-zhirov-screamer-re / AI (no-evidence-found): No actual AI use established from inspected evidence; absence does not prove non-use.
- tcottrill-tempest-full-disassembly-and-c-port / Target CPU (no-evidence-found): No independently established minimum target CPU.
- tcottrill-tempest-full-disassembly-and-c-port / Runtime profiles (no-evidence-found): No independently verified hardware profile.
- correo415415-mslug-decompiled / Target CPU (no-evidence-found): No independently established minimum target CPU.
- correo415415-mslug-decompiled / Runtime profiles (no-evidence-found): No independently verified hardware profile.
- correo415415-mslug-decompiled / AI (no-evidence-found): No actual AI use established from inspected evidence; absence does not prove non-use.
- archawk-deepcrawlerforge / Target CPU (no-evidence-found): No independently established minimum target CPU.
- archawk-deepcrawlerforge / Runtime profiles (no-evidence-found): No independently verified hardware profile.
- archawk-deepcrawlerforge / AI (no-evidence-found): No actual AI use established from inspected evidence; absence does not prove non-use.
- retro-ware-por-go / Target CPU (no-evidence-found): No independently established minimum target CPU.
- retro-ware-por-go / Runtime profiles (no-evidence-found): No independently verified hardware profile.
- retro-ware-por-go / AI (no-evidence-found): No actual AI use established from inspected evidence; absence does not prove non-use.

## Captain Bible — DOS research and Rust engine

Project ID: peterkelly-captain-bible-re · Overall audit: partial

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
  "display_title": "Captain Bible — DOS research and Rust engine",
  "id": "peterkelly-captain-bible-re",
  "last_activity": null,
  "last_checked": "2026-11-05",
  "re_started": null,
  "reconstructed_languages": [
    "Rust",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/peterkelly/captain-bible-re",
  "runtime_profiles": [],
  "source_cpu": [
    "x86"
  ],
  "source_language": [],
  "source_platforms": [
    "DOS"
  ],
  "status": "Source reviewed; no independent build or execution",
  "subjects": [
    "Captain Bible in the Dome of Darkness"
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
  "title": "Captain Bible — DOS research and Rust engine",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "captain-bible-re",
  "work_kinds": [
    "binary-analysis",
    "data-format-analysis",
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Captain Bible — DOS research and Rust engine. Repository and pinned documentation inspected.
- https://github.com/peterkelly/captain-bible-re/blob/084eae89ce9be745ea3ce1376399a82ad4a6f7fe/README.md
- https://github.com/peterkelly/captain-bible-re/blob/084eae89ce9be745ea3ce1376399a82ad4a6f7fe/rust-engine/README.md

### Classification (reviewed)

Research, file format analysis and a Rust clean-room engine using original game data. The author describes DOS/Rust comparisons; no independent build or parity test.
- https://github.com/peterkelly/captain-bible-re/blob/084eae89ce9be745ea3ce1376399a82ad4a6f7fe/README.md
- https://github.com/peterkelly/captain-bible-re/blob/084eae89ce9be745ea3ce1376399a82ad4a6f7fe/rust-engine/README.md

### Source CPU (reviewed)

Source architecture is identified in project documentation.
- https://github.com/peterkelly/captain-bible-re/blob/084eae89ce9be745ea3ce1376399a82ad4a6f7fe/README.md
- https://github.com/peterkelly/captain-bible-re/blob/084eae89ce9be745ea3ce1376399a82ad4a6f7fe/rust-engine/README.md

### Target CPU (no-evidence-found)

No independently established minimum target CPU.
- https://github.com/peterkelly/captain-bible-re/blob/084eae89ce9be745ea3ce1376399a82ad4a6f7fe/README.md
- https://github.com/peterkelly/captain-bible-re/blob/084eae89ce9be745ea3ce1376399a82ad4a6f7fe/rust-engine/README.md

### Build (reviewed)

No independent build, run, gameplay or byte comparison was performed.
- https://github.com/peterkelly/captain-bible-re/blob/084eae89ce9be745ea3ce1376399a82ad4a6f7fe/README.md
- https://github.com/peterkelly/captain-bible-re/blob/084eae89ce9be745ea3ce1376399a82ad4a6f7fe/rust-engine/README.md

### Runtime profiles (no-evidence-found)

No independently verified hardware profile.
- https://github.com/peterkelly/captain-bible-re/blob/084eae89ce9be745ea3ce1376399a82ad4a6f7fe/README.md
- https://github.com/peterkelly/captain-bible-re/blob/084eae89ce9be745ea3ce1376399a82ad4a6f7fe/rust-engine/README.md

### AI (no-evidence-found)

No actual AI use established from inspected evidence; absence does not prove non-use.
- https://github.com/peterkelly/captain-bible-re/blob/084eae89ce9be745ea3ce1376399a82ad4a6f7fe/README.md
- https://github.com/peterkelly/captain-bible-re/blob/084eae89ce9be745ea3ce1376399a82ad4a6f7fe/rust-engine/README.md

### Relationships (reviewed)

Distinct repository and work product; same-game efforts are not assumed identical.
- https://github.com/peterkelly/captain-bible-re/blob/084eae89ce9be745ea3ce1376399a82ad4a6f7fe/README.md
- https://github.com/peterkelly/captain-bible-re/blob/084eae89ce9be745ea3ce1376399a82ad4a6f7fe/rust-engine/README.md

## Weltendämmerung — C64 disassembly and browser port

Project ID: s-macke-weltendaemmerung · Overall audit: partial

### Typed catalogue values

```json
{
  "ai": {
    "evidence": [
      "Author explicitly credits Claude: https://github.com/s-macke/weltendaemmerung/blob/692b6b88dd83b77e8704a757f3314f021084d61c/README.md"
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
  "display_title": "Weltendämmerung — C64 disassembly and browser port",
  "id": "s-macke-weltendaemmerung",
  "last_activity": null,
  "last_checked": "2026-11-05",
  "re_started": null,
  "reconstructed_languages": [
    "6502 assembly",
    "TypeScript",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/s-macke/weltendaemmerung",
  "runtime_profiles": [],
  "source_cpu": [
    "6502"
  ],
  "source_language": [],
  "source_platforms": [
    "C64"
  ],
  "status": "Source reviewed; no independent build or execution",
  "subjects": [
    "Weltendämmerung"
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
  "title": "Weltendämmerung — C64 disassembly and browser port",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "weltendaemmerung",
  "work_kinds": [
    "disassembly",
    "data-format-analysis",
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Weltendämmerung — C64 disassembly and browser port. Repository and pinned documentation inspected.
- https://github.com/s-macke/weltendaemmerung/blob/692b6b88dd83b77e8704a757f3314f021084d61c/README.md
- https://github.com/s-macke/weltendaemmerung/blob/692b6b88dd83b77e8704a757f3314f021084d61c/PORTING.md

### Classification (reviewed)

C64 binary disassembly, documented mechanics and TypeScript browser implementation. Author credits Claude Code. The porting guide lists omitted sound and save/load, so it is not a complete equivalence claim.
- https://github.com/s-macke/weltendaemmerung/blob/692b6b88dd83b77e8704a757f3314f021084d61c/README.md
- https://github.com/s-macke/weltendaemmerung/blob/692b6b88dd83b77e8704a757f3314f021084d61c/PORTING.md

### Source CPU (reviewed)

Source architecture is identified in project documentation.
- https://github.com/s-macke/weltendaemmerung/blob/692b6b88dd83b77e8704a757f3314f021084d61c/README.md
- https://github.com/s-macke/weltendaemmerung/blob/692b6b88dd83b77e8704a757f3314f021084d61c/PORTING.md

### Target CPU (no-evidence-found)

No independently established minimum target CPU.
- https://github.com/s-macke/weltendaemmerung/blob/692b6b88dd83b77e8704a757f3314f021084d61c/README.md
- https://github.com/s-macke/weltendaemmerung/blob/692b6b88dd83b77e8704a757f3314f021084d61c/PORTING.md

### Build (reviewed)

No independent build, run, gameplay or byte comparison was performed.
- https://github.com/s-macke/weltendaemmerung/blob/692b6b88dd83b77e8704a757f3314f021084d61c/README.md
- https://github.com/s-macke/weltendaemmerung/blob/692b6b88dd83b77e8704a757f3314f021084d61c/PORTING.md

### Runtime profiles (no-evidence-found)

No independently verified hardware profile.
- https://github.com/s-macke/weltendaemmerung/blob/692b6b88dd83b77e8704a757f3314f021084d61c/README.md
- https://github.com/s-macke/weltendaemmerung/blob/692b6b88dd83b77e8704a757f3314f021084d61c/PORTING.md

### AI (reviewed)

Author credits Claude for development.
- https://github.com/s-macke/weltendaemmerung/blob/692b6b88dd83b77e8704a757f3314f021084d61c/README.md
- https://github.com/s-macke/weltendaemmerung/blob/692b6b88dd83b77e8704a757f3314f021084d61c/PORTING.md

### Relationships (reviewed)

Distinct repository and work product; same-game efforts are not assumed identical.
- https://github.com/s-macke/weltendaemmerung/blob/692b6b88dd83b77e8704a757f3314f021084d61c/README.md
- https://github.com/s-macke/weltendaemmerung/blob/692b6b88dd83b77e8704a757f3314f021084d61c/PORTING.md

## Lands of Lore II — DOS engine and format research

Project ID: kforestland-lands-of-lore-2-re · Overall audit: partial

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
  "display_title": "Lands of Lore II — DOS engine and format research",
  "id": "kforestland-lands-of-lore-2-re",
  "last_activity": null,
  "last_checked": "2026-11-05",
  "re_started": null,
  "reconstructed_languages": [
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/KForestland/lands-of-lore-2-re",
  "runtime_profiles": [],
  "source_cpu": [
    "x86"
  ],
  "source_language": [],
  "source_platforms": [
    "DOS"
  ],
  "status": "Source reviewed; no independent build or execution",
  "subjects": [
    "Lands of Lore: Guardians of Destiny"
  ],
  "tags": [],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [],
  "techniques": [],
  "title": "Lands of Lore II — DOS engine and format research",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "lands-of-lore-2-re",
  "work_kinds": [
    "binary-analysis",
    "data-format-analysis"
  ]
}
```

### Identity (reviewed)

Lands of Lore II — DOS engine and format research. Repository and pinned documentation inspected.
- https://github.com/KForestland/lands-of-lore-2-re/blob/fe134c268f9c5e0e89e3b8a11148a84fef982f1b/README.md
- https://github.com/KForestland/lands-of-lore-2-re/blob/fe134c268f9c5e0e89e3b8a11148a84fef982f1b/docs/lol2-level-script-format.md

### Classification (reviewed)

DOS executable, scripting, data formats and cave geometry research. Experimental Godot view is a separate repository; the author explicitly notes remaining geometry and gameplay work.
- https://github.com/KForestland/lands-of-lore-2-re/blob/fe134c268f9c5e0e89e3b8a11148a84fef982f1b/README.md
- https://github.com/KForestland/lands-of-lore-2-re/blob/fe134c268f9c5e0e89e3b8a11148a84fef982f1b/docs/lol2-level-script-format.md

### Source CPU (reviewed)

Source architecture is identified in project documentation.
- https://github.com/KForestland/lands-of-lore-2-re/blob/fe134c268f9c5e0e89e3b8a11148a84fef982f1b/README.md
- https://github.com/KForestland/lands-of-lore-2-re/blob/fe134c268f9c5e0e89e3b8a11148a84fef982f1b/docs/lol2-level-script-format.md

### Target CPU (no-evidence-found)

No independently established minimum target CPU.
- https://github.com/KForestland/lands-of-lore-2-re/blob/fe134c268f9c5e0e89e3b8a11148a84fef982f1b/README.md
- https://github.com/KForestland/lands-of-lore-2-re/blob/fe134c268f9c5e0e89e3b8a11148a84fef982f1b/docs/lol2-level-script-format.md

### Build (reviewed)

No independent build, run, gameplay or byte comparison was performed.
- https://github.com/KForestland/lands-of-lore-2-re/blob/fe134c268f9c5e0e89e3b8a11148a84fef982f1b/README.md
- https://github.com/KForestland/lands-of-lore-2-re/blob/fe134c268f9c5e0e89e3b8a11148a84fef982f1b/docs/lol2-level-script-format.md

### Runtime profiles (no-evidence-found)

No independently verified hardware profile.
- https://github.com/KForestland/lands-of-lore-2-re/blob/fe134c268f9c5e0e89e3b8a11148a84fef982f1b/README.md
- https://github.com/KForestland/lands-of-lore-2-re/blob/fe134c268f9c5e0e89e3b8a11148a84fef982f1b/docs/lol2-level-script-format.md

### AI (no-evidence-found)

No actual AI use established from inspected evidence; absence does not prove non-use.
- https://github.com/KForestland/lands-of-lore-2-re/blob/fe134c268f9c5e0e89e3b8a11148a84fef982f1b/README.md
- https://github.com/KForestland/lands-of-lore-2-re/blob/fe134c268f9c5e0e89e3b8a11148a84fef982f1b/docs/lol2-level-script-format.md

### Relationships (reviewed)

Distinct repository and work product; same-game efforts are not assumed identical.
- https://github.com/KForestland/lands-of-lore-2-re/blob/fe134c268f9c5e0e89e3b8a11148a84fef982f1b/README.md
- https://github.com/KForestland/lands-of-lore-2-re/blob/fe134c268f9c5e0e89e3b8a11148a84fef982f1b/docs/lol2-level-script-format.md

## Screamer — DOS executable research and source recovery

Project ID: i-zhirov-screamer-re · Overall audit: partial

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
  "display_title": "Screamer — DOS executable research and source recovery",
  "id": "i-zhirov-screamer-re",
  "last_activity": null,
  "last_checked": "2026-11-05",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/i-zhirov/screamer_re",
  "runtime_profiles": [],
  "source_cpu": [
    "x86"
  ],
  "source_language": [],
  "source_platforms": [
    "DOS"
  ],
  "status": "Source reviewed; no independent build or execution",
  "subjects": [
    "Screamer"
  ],
  "tags": [],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "DOS"
  ],
  "techniques": [],
  "title": "Screamer — DOS executable research and source recovery",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "screamer_re",
  "work_kinds": [
    "disassembly",
    "data-format-analysis",
    "source-reconstruction"
  ]
}
```

### Identity (reviewed)

Screamer — DOS executable research and source recovery. Repository and pinned documentation inspected.
- https://github.com/i-zhirov/screamer_re/blob/75b976f8aaf8adee5f240810d8611a985c0298b0/README.md
- https://github.com/i-zhirov/screamer_re/blob/75b976f8aaf8adee5f240810d8611a985c0298b0/tools/le.py

### Classification (reviewed)

Early DOS/4GW executable analysis with reconstruction and comparison tooling. The author reports one function matching exactly, while other modules differ or only match shape; no full game reconstruction claimed.
- https://github.com/i-zhirov/screamer_re/blob/75b976f8aaf8adee5f240810d8611a985c0298b0/README.md
- https://github.com/i-zhirov/screamer_re/blob/75b976f8aaf8adee5f240810d8611a985c0298b0/tools/le.py

### Source CPU (reviewed)

Source architecture is identified in project documentation.
- https://github.com/i-zhirov/screamer_re/blob/75b976f8aaf8adee5f240810d8611a985c0298b0/README.md
- https://github.com/i-zhirov/screamer_re/blob/75b976f8aaf8adee5f240810d8611a985c0298b0/tools/le.py

### Target CPU (no-evidence-found)

No independently established minimum target CPU.
- https://github.com/i-zhirov/screamer_re/blob/75b976f8aaf8adee5f240810d8611a985c0298b0/README.md
- https://github.com/i-zhirov/screamer_re/blob/75b976f8aaf8adee5f240810d8611a985c0298b0/tools/le.py

### Build (reviewed)

No independent build, run, gameplay or byte comparison was performed.
- https://github.com/i-zhirov/screamer_re/blob/75b976f8aaf8adee5f240810d8611a985c0298b0/README.md
- https://github.com/i-zhirov/screamer_re/blob/75b976f8aaf8adee5f240810d8611a985c0298b0/tools/le.py

### Runtime profiles (no-evidence-found)

No independently verified hardware profile.
- https://github.com/i-zhirov/screamer_re/blob/75b976f8aaf8adee5f240810d8611a985c0298b0/README.md
- https://github.com/i-zhirov/screamer_re/blob/75b976f8aaf8adee5f240810d8611a985c0298b0/tools/le.py

### AI (no-evidence-found)

No actual AI use established from inspected evidence; absence does not prove non-use.
- https://github.com/i-zhirov/screamer_re/blob/75b976f8aaf8adee5f240810d8611a985c0298b0/README.md
- https://github.com/i-zhirov/screamer_re/blob/75b976f8aaf8adee5f240810d8611a985c0298b0/tools/le.py

### Relationships (reviewed)

Distinct repository and work product; same-game efforts are not assumed identical.
- https://github.com/i-zhirov/screamer_re/blob/75b976f8aaf8adee5f240810d8611a985c0298b0/README.md
- https://github.com/i-zhirov/screamer_re/blob/75b976f8aaf8adee5f240810d8611a985c0298b0/tools/le.py

## Tempest — arcade disassembly and C translation

Project ID: tcottrill-tempest-full-disassembly-and-c-port · Overall audit: partial

### Typed catalogue values

```json
{
  "ai": {
    "evidence": [
      "Author explicitly credits Claude: https://github.com/tcottrill/Tempest-Full-Disassembly-and-C-Port/blob/da0fa4d6324f8cac22da2f488b1617a839a79fb0/README.md"
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
  "display_title": "Tempest — arcade disassembly and C translation",
  "id": "tcottrill-tempest-full-disassembly-and-c-port",
  "last_activity": null,
  "last_checked": "2026-11-05",
  "re_started": null,
  "reconstructed_languages": [
    "6502 assembly",
    "C"
  ],
  "record_class": "subject",
  "repo": "https://github.com/tcottrill/Tempest-Full-Disassembly-and-C-Port",
  "runtime_profiles": [],
  "source_cpu": [
    "6502"
  ],
  "source_language": [],
  "source_platforms": [
    "Arcade"
  ],
  "status": "Source reviewed; no independent build or execution",
  "subjects": [
    "Tempest"
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
  "title": "Tempest — arcade disassembly and C translation",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "Tempest-Full-Disassembly-and-C-Port",
  "work_kinds": [
    "disassembly",
    "source-reconstruction",
    "reverse-engineering-derived-port"
  ]
}
```

### Identity (reviewed)

Tempest — arcade disassembly and C translation. Repository and pinned documentation inspected.
- https://github.com/tcottrill/Tempest-Full-Disassembly-and-C-Port/blob/da0fa4d6324f8cac22da2f488b1617a839a79fb0/README.md
- https://github.com/tcottrill/Tempest-Full-Disassembly-and-C-Port/blob/da0fa4d6324f8cac22da2f488b1617a839a79fb0/c_src/README.md

### Classification (reviewed)

Arcade ROM disassembly and C translation with a separate 6502 emulator reference. Author credits Atari original source and an earlier disassembly as naming references, and reports comparison results; those claims were not independently reproduced.
- https://github.com/tcottrill/Tempest-Full-Disassembly-and-C-Port/blob/da0fa4d6324f8cac22da2f488b1617a839a79fb0/README.md
- https://github.com/tcottrill/Tempest-Full-Disassembly-and-C-Port/blob/da0fa4d6324f8cac22da2f488b1617a839a79fb0/c_src/README.md

### Source CPU (reviewed)

Source architecture is identified in project documentation.
- https://github.com/tcottrill/Tempest-Full-Disassembly-and-C-Port/blob/da0fa4d6324f8cac22da2f488b1617a839a79fb0/README.md
- https://github.com/tcottrill/Tempest-Full-Disassembly-and-C-Port/blob/da0fa4d6324f8cac22da2f488b1617a839a79fb0/c_src/README.md

### Target CPU (no-evidence-found)

No independently established minimum target CPU.
- https://github.com/tcottrill/Tempest-Full-Disassembly-and-C-Port/blob/da0fa4d6324f8cac22da2f488b1617a839a79fb0/README.md
- https://github.com/tcottrill/Tempest-Full-Disassembly-and-C-Port/blob/da0fa4d6324f8cac22da2f488b1617a839a79fb0/c_src/README.md

### Build (reviewed)

No independent build, run, gameplay or byte comparison was performed.
- https://github.com/tcottrill/Tempest-Full-Disassembly-and-C-Port/blob/da0fa4d6324f8cac22da2f488b1617a839a79fb0/README.md
- https://github.com/tcottrill/Tempest-Full-Disassembly-and-C-Port/blob/da0fa4d6324f8cac22da2f488b1617a839a79fb0/c_src/README.md

### Runtime profiles (no-evidence-found)

No independently verified hardware profile.
- https://github.com/tcottrill/Tempest-Full-Disassembly-and-C-Port/blob/da0fa4d6324f8cac22da2f488b1617a839a79fb0/README.md
- https://github.com/tcottrill/Tempest-Full-Disassembly-and-C-Port/blob/da0fa4d6324f8cac22da2f488b1617a839a79fb0/c_src/README.md

### AI (reviewed)

Author credits Claude for development.
- https://github.com/tcottrill/Tempest-Full-Disassembly-and-C-Port/blob/da0fa4d6324f8cac22da2f488b1617a839a79fb0/README.md
- https://github.com/tcottrill/Tempest-Full-Disassembly-and-C-Port/blob/da0fa4d6324f8cac22da2f488b1617a839a79fb0/c_src/README.md

### Relationships (reviewed)

Distinct repository and work product; same-game efforts are not assumed identical.
- https://github.com/tcottrill/Tempest-Full-Disassembly-and-C-Port/blob/da0fa4d6324f8cac22da2f488b1617a839a79fb0/README.md
- https://github.com/tcottrill/Tempest-Full-Disassembly-and-C-Port/blob/da0fa4d6324f8cac22da2f488b1617a839a79fb0/c_src/README.md

## Metal Slug — Neo Geo ROM reconstruction

Project ID: correo415415-mslug-decompiled · Overall audit: partial

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
  "display_title": "Metal Slug — Neo Geo ROM reconstruction",
  "id": "correo415415-mslug-decompiled",
  "last_activity": null,
  "last_checked": "2026-11-05",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "68000 assembly",
    "Z80 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/correo415415/mslug-decompiled",
  "runtime_profiles": [],
  "source_cpu": [
    "68000",
    "Z80"
  ],
  "source_language": [],
  "source_platforms": [
    "Neo Geo"
  ],
  "status": "Source reviewed; no independent build or execution",
  "subjects": [
    "Metal Slug"
  ],
  "tags": [],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Neo Geo"
  ],
  "techniques": [],
  "title": "Metal Slug — Neo Geo ROM reconstruction",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "mslug-decompiled",
  "work_kinds": [
    "disassembly",
    "decompilation",
    "source-reconstruction",
    "data-format-analysis"
  ]
}
```

### Identity (reviewed)

Metal Slug — Neo Geo ROM reconstruction. Repository and pinned documentation inspected.
- https://github.com/correo415415/mslug-decompiled/blob/1cacf0e4e0550f77b37fed9d5448ae560a0371ac/README.md
- https://github.com/correo415415/mslug-decompiled/blob/1cacf0e4e0550f77b37fed9d5448ae560a0371ac/mrom/README.md

### Classification (reviewed)

Matching 68000 program ROM and Z80 sound-driver source work, with data extraction and rebuild tools. README reports byte-identical ROMs using a mix of assembly, C and data; the report was not independently tested.
- https://github.com/correo415415/mslug-decompiled/blob/1cacf0e4e0550f77b37fed9d5448ae560a0371ac/README.md
- https://github.com/correo415415/mslug-decompiled/blob/1cacf0e4e0550f77b37fed9d5448ae560a0371ac/mrom/README.md

### Source CPU (reviewed)

Source architecture is identified in project documentation.
- https://github.com/correo415415/mslug-decompiled/blob/1cacf0e4e0550f77b37fed9d5448ae560a0371ac/README.md
- https://github.com/correo415415/mslug-decompiled/blob/1cacf0e4e0550f77b37fed9d5448ae560a0371ac/mrom/README.md

### Target CPU (no-evidence-found)

No independently established minimum target CPU.
- https://github.com/correo415415/mslug-decompiled/blob/1cacf0e4e0550f77b37fed9d5448ae560a0371ac/README.md
- https://github.com/correo415415/mslug-decompiled/blob/1cacf0e4e0550f77b37fed9d5448ae560a0371ac/mrom/README.md

### Build (reviewed)

No independent build, run, gameplay or byte comparison was performed.
- https://github.com/correo415415/mslug-decompiled/blob/1cacf0e4e0550f77b37fed9d5448ae560a0371ac/README.md
- https://github.com/correo415415/mslug-decompiled/blob/1cacf0e4e0550f77b37fed9d5448ae560a0371ac/mrom/README.md

### Runtime profiles (no-evidence-found)

No independently verified hardware profile.
- https://github.com/correo415415/mslug-decompiled/blob/1cacf0e4e0550f77b37fed9d5448ae560a0371ac/README.md
- https://github.com/correo415415/mslug-decompiled/blob/1cacf0e4e0550f77b37fed9d5448ae560a0371ac/mrom/README.md

### AI (no-evidence-found)

No actual AI use established from inspected evidence; absence does not prove non-use.
- https://github.com/correo415415/mslug-decompiled/blob/1cacf0e4e0550f77b37fed9d5448ae560a0371ac/README.md
- https://github.com/correo415415/mslug-decompiled/blob/1cacf0e4e0550f77b37fed9d5448ae560a0371ac/mrom/README.md

### Relationships (reviewed)

Distinct repository and work product; same-game efforts are not assumed identical.
- https://github.com/correo415415/mslug-decompiled/blob/1cacf0e4e0550f77b37fed9d5448ae560a0371ac/README.md
- https://github.com/correo415415/mslug-decompiled/blob/1cacf0e4e0550f77b37fed9d5448ae560a0371ac/mrom/README.md

## Eye of the Beholder — browser engine reconstruction

Project ID: archawk-deepcrawlerforge · Overall audit: partial

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
  "display_title": "Eye of the Beholder — browser engine reconstruction",
  "id": "archawk-deepcrawlerforge",
  "last_activity": null,
  "last_checked": "2026-11-05",
  "re_started": null,
  "reconstructed_languages": [
    "JavaScript"
  ],
  "record_class": "subject",
  "repo": "https://github.com/Archawk/DeepCrawlerForge",
  "runtime_profiles": [],
  "source_cpu": [
    "x86"
  ],
  "source_language": [],
  "source_platforms": [
    "DOS"
  ],
  "status": "Source reviewed; no independent build or execution",
  "subjects": [
    "Eye of the Beholder"
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
  "title": "Eye of the Beholder — browser engine reconstruction",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "DeepCrawlerForge",
  "work_kinds": [
    "data-format-analysis",
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Eye of the Beholder — browser engine reconstruction. Repository and pinned documentation inspected.
- https://github.com/Archawk/DeepCrawlerForge/blob/9aee21bad282ede81bdd9fa161e5b80b11099604/README.md
- https://github.com/Archawk/DeepCrawlerForge/blob/9aee21bad282ede81bdd9fa161e5b80b11099604/docs/CERTIFICATION.md

### Classification (reviewed)

Independent browser implementation reading original DOS resources. The DOS game is described as a comparison oracle; certification and playability reports are author claims, not independently reproduced.
- https://github.com/Archawk/DeepCrawlerForge/blob/9aee21bad282ede81bdd9fa161e5b80b11099604/README.md
- https://github.com/Archawk/DeepCrawlerForge/blob/9aee21bad282ede81bdd9fa161e5b80b11099604/docs/CERTIFICATION.md

### Source CPU (reviewed)

Source architecture is identified in project documentation.
- https://github.com/Archawk/DeepCrawlerForge/blob/9aee21bad282ede81bdd9fa161e5b80b11099604/README.md
- https://github.com/Archawk/DeepCrawlerForge/blob/9aee21bad282ede81bdd9fa161e5b80b11099604/docs/CERTIFICATION.md

### Target CPU (no-evidence-found)

No independently established minimum target CPU.
- https://github.com/Archawk/DeepCrawlerForge/blob/9aee21bad282ede81bdd9fa161e5b80b11099604/README.md
- https://github.com/Archawk/DeepCrawlerForge/blob/9aee21bad282ede81bdd9fa161e5b80b11099604/docs/CERTIFICATION.md

### Build (reviewed)

No independent build, run, gameplay or byte comparison was performed.
- https://github.com/Archawk/DeepCrawlerForge/blob/9aee21bad282ede81bdd9fa161e5b80b11099604/README.md
- https://github.com/Archawk/DeepCrawlerForge/blob/9aee21bad282ede81bdd9fa161e5b80b11099604/docs/CERTIFICATION.md

### Runtime profiles (no-evidence-found)

No independently verified hardware profile.
- https://github.com/Archawk/DeepCrawlerForge/blob/9aee21bad282ede81bdd9fa161e5b80b11099604/README.md
- https://github.com/Archawk/DeepCrawlerForge/blob/9aee21bad282ede81bdd9fa161e5b80b11099604/docs/CERTIFICATION.md

### AI (no-evidence-found)

No actual AI use established from inspected evidence; absence does not prove non-use.
- https://github.com/Archawk/DeepCrawlerForge/blob/9aee21bad282ede81bdd9fa161e5b80b11099604/README.md
- https://github.com/Archawk/DeepCrawlerForge/blob/9aee21bad282ede81bdd9fa161e5b80b11099604/docs/CERTIFICATION.md

### Relationships (reviewed)

Distinct repository and work product; same-game efforts are not assumed identical.
- https://github.com/Archawk/DeepCrawlerForge/blob/9aee21bad282ede81bdd9fa161e5b80b11099604/README.md
- https://github.com/Archawk/DeepCrawlerForge/blob/9aee21bad282ede81bdd9fa161e5b80b11099604/docs/CERTIFICATION.md

## Pool of Radiance — modernized Go port

Project ID: retro-ware-por-go · Overall audit: partial

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
  "display_title": "Pool of Radiance — modernized Go port",
  "id": "retro-ware-por-go",
  "last_activity": null,
  "last_checked": "2026-11-05",
  "re_started": null,
  "reconstructed_languages": [
    "Go"
  ],
  "record_class": "subject",
  "repo": "https://github.com/retro-ware/por-go",
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
  "status": "Source reviewed; no independent build or execution",
  "subjects": [
    "Pool of Radiance"
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
  "title": "Pool of Radiance — modernized Go port",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "por-go",
  "work_kinds": [
    "reverse-engineering-derived-port",
    "data-format-analysis"
  ]
}
```

### Identity (reviewed)

Pool of Radiance — modernized Go port. Repository and pinned documentation inspected.
- https://github.com/retro-ware/por-go/blob/c82552db827160a2153d72d2d5534cba0a7f3f0a/README.md
- https://github.com/retro-ware/por-go/blob/c82552db827160a2153d72d2d5534cba0a7f3f0a/MODERNIZED.md

### Classification (reviewed)

Go game engine using original data and related to the separately tracked DOS analysis workspace. It deliberately modernizes interface, presentation and several rules; do not label it original-identical.
- https://github.com/retro-ware/por-go/blob/c82552db827160a2153d72d2d5534cba0a7f3f0a/README.md
- https://github.com/retro-ware/por-go/blob/c82552db827160a2153d72d2d5534cba0a7f3f0a/MODERNIZED.md

### Source CPU (reviewed)

Source architecture is identified in project documentation.
- https://github.com/retro-ware/por-go/blob/c82552db827160a2153d72d2d5534cba0a7f3f0a/README.md
- https://github.com/retro-ware/por-go/blob/c82552db827160a2153d72d2d5534cba0a7f3f0a/MODERNIZED.md

### Target CPU (no-evidence-found)

No independently established minimum target CPU.
- https://github.com/retro-ware/por-go/blob/c82552db827160a2153d72d2d5534cba0a7f3f0a/README.md
- https://github.com/retro-ware/por-go/blob/c82552db827160a2153d72d2d5534cba0a7f3f0a/MODERNIZED.md

### Build (reviewed)

No independent build, run, gameplay or byte comparison was performed.
- https://github.com/retro-ware/por-go/blob/c82552db827160a2153d72d2d5534cba0a7f3f0a/README.md
- https://github.com/retro-ware/por-go/blob/c82552db827160a2153d72d2d5534cba0a7f3f0a/MODERNIZED.md

### Runtime profiles (no-evidence-found)

No independently verified hardware profile.
- https://github.com/retro-ware/por-go/blob/c82552db827160a2153d72d2d5534cba0a7f3f0a/README.md
- https://github.com/retro-ware/por-go/blob/c82552db827160a2153d72d2d5534cba0a7f3f0a/MODERNIZED.md

### AI (no-evidence-found)

No actual AI use established from inspected evidence; absence does not prove non-use.
- https://github.com/retro-ware/por-go/blob/c82552db827160a2153d72d2d5534cba0a7f3f0a/README.md
- https://github.com/retro-ware/por-go/blob/c82552db827160a2153d72d2d5534cba0a7f3f0a/MODERNIZED.md

### Relationships (reviewed)

Distinct repository and work product; same-game efforts are not assumed identical.
- https://github.com/retro-ware/por-go/blob/c82552db827160a2153d72d2d5534cba0a7f3f0a/README.md
- https://github.com/retro-ware/por-go/blob/c82552db827160a2153d72d2d5534cba0a7f3f0a/MODERNIZED.md

## Pinned evidence manifest

- archawk-deepcrawlerforge-docs-certification-md: https://github.com/archawk/deepcrawlerforge/blob/9aee21bad282ede81bdd9fa161e5b80b11099604/docs/CERTIFICATION.md (Git blob b00ccba1e61d4afb42a0b19b6f22f136efa1d66c)
- archawk-deepcrawlerforge-readme-md: https://github.com/archawk/deepcrawlerforge/blob/9aee21bad282ede81bdd9fa161e5b80b11099604/README.md (Git blob 65d17fa33c13af09685ec385f447960e78cad295)
- correo415415-mslug-decompiled-mrom-readme-md: https://github.com/correo415415/mslug-decompiled/blob/1cacf0e4e0550f77b37fed9d5448ae560a0371ac/mrom/README.md (Git blob b59c444b64e15e38ea0690e88219a9ea033c50b3)
- correo415415-mslug-decompiled-readme-md: https://github.com/correo415415/mslug-decompiled/blob/1cacf0e4e0550f77b37fed9d5448ae560a0371ac/README.md (Git blob 8636fb88ed365c8f7ff0a9f58ce65f03e16562b5)
- i-zhirov-screamer-re-readme-md: https://github.com/i-zhirov/screamer_re/blob/75b976f8aaf8adee5f240810d8611a985c0298b0/README.md (Git blob 039445f244511597fc4933842824d842c88ef3d3)
- i-zhirov-screamer-re-tools-le-py: https://github.com/i-zhirov/screamer_re/blob/75b976f8aaf8adee5f240810d8611a985c0298b0/tools/le.py (Git blob bcb86e86de1df19901a84cb436ec5b7100cdd626)
- kforestland-lands-of-lore-2-re-docs-lol2-level-script-format-md: https://github.com/kforestland/lands-of-lore-2-re/blob/fe134c268f9c5e0e89e3b8a11148a84fef982f1b/docs/lol2-level-script-format.md (Git blob c285559e26c950d0eb275cdb1c4cba77573e2718)
- kforestland-lands-of-lore-2-re-readme-md: https://github.com/kforestland/lands-of-lore-2-re/blob/fe134c268f9c5e0e89e3b8a11148a84fef982f1b/README.md (Git blob 7028d7500db812c28c36a02803873c387e432412)
- peterkelly-captain-bible-re-readme-md: https://github.com/peterkelly/captain-bible-re/blob/084eae89ce9be745ea3ce1376399a82ad4a6f7fe/README.md (Git blob fd1f942c0ab650a3dfbccb85a22854b19fb2dc09)
- peterkelly-captain-bible-re-rust-engine-readme-md: https://github.com/peterkelly/captain-bible-re/blob/084eae89ce9be745ea3ce1376399a82ad4a6f7fe/rust-engine/README.md (Git blob 67226fe845132b520aa56419a8f0983e5a8a4471)
- retro-ware-por-go-modernized-md: https://github.com/retro-ware/por-go/blob/c82552db827160a2153d72d2d5534cba0a7f3f0a/MODERNIZED.md (Git blob 8c517c2d2d342d81f5592fb40e2bf0c083fa9fdd)
- retro-ware-por-go-readme-md: https://github.com/retro-ware/por-go/blob/c82552db827160a2153d72d2d5534cba0a7f3f0a/README.md (Git blob 1fc5f581411d0cfa5633c7ee67d086b41c26b8e6)
- s-macke-weltendaemmerung-porting-md: https://github.com/s-macke/weltendaemmerung/blob/692b6b88dd83b77e8704a757f3314f021084d61c/PORTING.md (Git blob 9a30e74c6afc5f77bff8bb4791ec10eed1bf4d88)
- s-macke-weltendaemmerung-readme-md: https://github.com/s-macke/weltendaemmerung/blob/692b6b88dd83b77e8704a757f3314f021084d61c/README.md (Git blob 9134bb4be0dfe0593b67f241c2e84b660d93bc4a)
- tcottrill-tempest-full-disassembly-and-c-port-c-src-readme-md: https://github.com/tcottrill/tempest-full-disassembly-and-c-port/blob/da0fa4d6324f8cac22da2f488b1617a839a79fb0/c_src/README.md (Git blob 4dae43ffeb85fc019293b0351526f5501adf6beb)
- tcottrill-tempest-full-disassembly-and-c-port-readme-md: https://github.com/tcottrill/tempest-full-disassembly-and-c-port/blob/da0fa4d6324f8cac22da2f488b1617a839a79fb0/README.md (Git blob 6766788608de2b8669b6752131401fde0bd5f48b)

## Sources

```json
[
  {
    "first_indexed": "2026-11-05",
    "id": "github-peterkelly-captain-bible-re",
    "kind": "github-repository",
    "last_reviewed": "2026-11-05",
    "open_task_ids": [],
    "projects_promoted": [
      "peterkelly-captain-bible-re"
    ],
    "reason": "Research, file format analysis and a Rust clean-room engine using original game data. The author describes DOS/Rust comparisons; no independent build or parity test.",
    "review_state": "partial",
    "source": "https://github.com/peterkelly/captain-bible-re"
  },
  {
    "first_indexed": "2026-11-05",
    "id": "github-s-macke-weltendaemmerung",
    "kind": "github-repository",
    "last_reviewed": "2026-11-05",
    "open_task_ids": [],
    "projects_promoted": [
      "s-macke-weltendaemmerung"
    ],
    "reason": "C64 binary disassembly, documented mechanics and TypeScript browser implementation. Author credits Claude Code. The porting guide lists omitted sound and save/load, so it is not a complete equivalence claim.",
    "review_state": "partial",
    "source": "https://github.com/s-macke/weltendaemmerung"
  },
  {
    "first_indexed": "2026-11-05",
    "id": "github-kforestland-lands-of-lore-2-re",
    "kind": "github-repository",
    "last_reviewed": "2026-11-05",
    "open_task_ids": [],
    "projects_promoted": [
      "kforestland-lands-of-lore-2-re"
    ],
    "reason": "DOS executable, scripting, data formats and cave geometry research. Experimental Godot view is a separate repository; the author explicitly notes remaining geometry and gameplay work.",
    "review_state": "partial",
    "source": "https://github.com/KForestland/lands-of-lore-2-re"
  },
  {
    "first_indexed": "2026-11-05",
    "id": "github-i-zhirov-screamer-re",
    "kind": "github-repository",
    "last_reviewed": "2026-11-05",
    "open_task_ids": [],
    "projects_promoted": [
      "i-zhirov-screamer-re"
    ],
    "reason": "Early DOS/4GW executable analysis with reconstruction and comparison tooling. The author reports one function matching exactly, while other modules differ or only match shape; no full game reconstruction claimed.",
    "review_state": "partial",
    "source": "https://github.com/i-zhirov/screamer_re"
  },
  {
    "first_indexed": "2026-11-05",
    "id": "github-tcottrill-tempest-full-disassembly-and-c-port",
    "kind": "github-repository",
    "last_reviewed": "2026-11-05",
    "open_task_ids": [],
    "projects_promoted": [
      "tcottrill-tempest-full-disassembly-and-c-port"
    ],
    "reason": "Arcade ROM disassembly and C translation with a separate 6502 emulator reference. Author credits Atari original source and an earlier disassembly as naming references, and reports comparison results; those claims were not independently reproduced.",
    "review_state": "partial",
    "source": "https://github.com/tcottrill/Tempest-Full-Disassembly-and-C-Port"
  },
  {
    "first_indexed": "2026-11-05",
    "id": "github-correo415415-mslug-decompiled",
    "kind": "github-repository",
    "last_reviewed": "2026-11-05",
    "open_task_ids": [],
    "projects_promoted": [
      "correo415415-mslug-decompiled"
    ],
    "reason": "Matching 68000 program ROM and Z80 sound-driver source work, with data extraction and rebuild tools. README reports byte-identical ROMs using a mix of assembly, C and data; the report was not independently tested.",
    "review_state": "partial",
    "source": "https://github.com/correo415415/mslug-decompiled"
  },
  {
    "first_indexed": "2026-11-05",
    "id": "github-archawk-deepcrawlerforge",
    "kind": "github-repository",
    "last_reviewed": "2026-11-05",
    "open_task_ids": [],
    "projects_promoted": [
      "archawk-deepcrawlerforge"
    ],
    "reason": "Independent browser implementation reading original DOS resources. The DOS game is described as a comparison oracle; certification and playability reports are author claims, not independently reproduced.",
    "review_state": "partial",
    "source": "https://github.com/Archawk/DeepCrawlerForge"
  },
  {
    "first_indexed": "2026-11-05",
    "id": "github-retro-ware-por-go",
    "kind": "github-repository",
    "last_reviewed": "2026-11-05",
    "open_task_ids": [],
    "projects_promoted": [
      "retro-ware-por-go"
    ],
    "reason": "Go game engine using original data and related to the separately tracked DOS analysis workspace. It deliberately modernizes interface, presentation and several rules; do not label it original-identical.",
    "review_state": "partial",
    "source": "https://github.com/retro-ware/por-go"
  }
]
```

## Research event notes

Personally screened repository search, existing projects and decisions, pinned primary documentation and selected supporting sources. No independent builds, gameplay or binary comparisons.
