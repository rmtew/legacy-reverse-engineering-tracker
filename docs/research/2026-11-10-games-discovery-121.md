# Game reversing and reconstruction discovery

Review eleven game reversing and reconstruction projects.

Date: 2026-11-10 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- indieindie7-scorcher-decomp / Target CPU (no-evidence-found): No minimum output CPU was established; source architecture is not a host requirement.
- indieindie7-scorcher-decomp / Build (reviewed): No independent build, execution, gameplay or byte comparison was performed.
- indieindie7-scorcher-decomp / Runtime profiles (no-evidence-found): No independently verified runtime hardware profile was established from the inspected documentation.
- indieindie7-scorcher-decomp / AI (no-evidence-found): No explicit development-AI disclosure was established from the inspected README; absence does not establish non-use.
- indieindie7-gungriffon-decomp / Target CPU (no-evidence-found): No minimum output CPU was established; source architecture is not a host requirement.
- indieindie7-gungriffon-decomp / Build (reviewed): No independent build, execution, gameplay or byte comparison was performed.
- indieindie7-gungriffon-decomp / Runtime profiles (no-evidence-found): No independently verified runtime hardware profile was established from the inspected documentation.
- indieindie7-deadoralive-decomp / Target CPU (no-evidence-found): No minimum output CPU was established; source architecture is not a host requirement.
- indieindie7-deadoralive-decomp / Build (reviewed): No independent build, execution, gameplay or byte comparison was performed.
- indieindie7-deadoralive-decomp / Runtime profiles (no-evidence-found): No independently verified runtime hardware profile was established from the inspected documentation.
- indieindie7-cyberspeedway-decomp / Target CPU (no-evidence-found): No minimum output CPU was established; source architecture is not a host requirement.
- indieindie7-cyberspeedway-decomp / Build (reviewed): No independent build, execution, gameplay or byte comparison was performed.
- indieindie7-cyberspeedway-decomp / Runtime profiles (no-evidence-found): No independently verified runtime hardware profile was established from the inspected documentation.
- indieindie7-cyberspeedway-decomp / AI (no-evidence-found): No explicit development-AI disclosure was established from the inspected README; absence does not establish non-use.
- indieindie7-clockworkknight-decomp / Target CPU (no-evidence-found): No minimum output CPU was established; source architecture is not a host requirement.
- indieindie7-clockworkknight-decomp / Build (reviewed): No independent build, execution, gameplay or byte comparison was performed.
- indieindie7-clockworkknight-decomp / Runtime profiles (no-evidence-found): No independently verified runtime hardware profile was established from the inspected documentation.
- indieindie7-clockworkknight-decomp / AI (no-evidence-found): No explicit development-AI disclosure was established from the inspected README; absence does not establish non-use.
- indieindie7-robotica-decomp / Target CPU (no-evidence-found): No minimum output CPU was established; source architecture is not a host requirement.
- indieindie7-robotica-decomp / Build (reviewed): No independent build, execution, gameplay or byte comparison was performed.
- indieindie7-robotica-decomp / Runtime profiles (no-evidence-found): No independently verified runtime hardware profile was established from the inspected documentation.
- indieindie7-cybersled-decomp / Target CPU (no-evidence-found): No minimum output CPU was established; source architecture is not a host requirement.
- indieindie7-cybersled-decomp / Build (reviewed): No independent build, execution, gameplay or byte comparison was performed.
- indieindie7-cybersled-decomp / Runtime profiles (no-evidence-found): No independently verified runtime hardware profile was established from the inspected documentation.
- indieindie7-cybersled-decomp / AI (no-evidence-found): No explicit development-AI disclosure was established from the inspected README; absence does not establish non-use.
- georgeflower-faxanadu-atari-st / Build (reviewed): No independent build, execution, gameplay or byte comparison was performed.
- georgeflower-faxanadu-atari-st / Runtime profiles (no-evidence-found): No independently verified runtime hardware profile was established from the inspected documentation.
- kandowontu2-simtower-native-windows-port / Build (reviewed): No independent build, execution, gameplay or byte comparison was performed.
- kandowontu2-simtower-native-windows-port / Runtime profiles (no-evidence-found): No independently verified runtime hardware profile was established from the inspected documentation.
- kandowontu2-simtower-native-windows-port / AI (no-evidence-found): No explicit development-AI disclosure was established from the inspected README; absence does not establish non-use.
- colourclash-lasersquad / Target CPU (no-evidence-found): No minimum output CPU was established; source architecture is not a host requirement.
- colourclash-lasersquad / Build (reviewed): No independent build, execution, gameplay or byte comparison was performed.
- colourclash-lasersquad / Runtime profiles (no-evidence-found): No independently verified runtime hardware profile was established from the inspected documentation.
- colourclash-lasersquad / AI (no-evidence-found): No explicit development-AI disclosure was established from the inspected README; absence does not establish non-use.
- emukp-ganbare / Build (reviewed): No independent build, execution, gameplay or byte comparison was performed.
- emukp-ganbare / Runtime profiles (no-evidence-found): No independently verified runtime hardware profile was established from the inspected documentation.
- emukp-ganbare / AI (no-evidence-found): No explicit development-AI disclosure was established from the inspected README; absence does not establish non-use.

## Scorcher — DOS, Windows and Saturn reversing

Project ID: indieindie7-scorcher-decomp · Overall audit: partial

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
  "display_title": "Scorcher — DOS, Windows and Saturn reversing",
  "id": "indieindie7-scorcher-decomp",
  "last_activity": null,
  "last_checked": "2026-11-10",
  "re_started": null,
  "reconstructed_languages": [],
  "record_class": "subject",
  "repo": "https://github.com/indieindie7/scorcher-decomp",
  "runtime_profiles": [],
  "source_cpu": [
    "x86",
    "sh2"
  ],
  "source_language": [],
  "source_platforms": [
    "DOS",
    "Windows",
    "Sega Saturn"
  ],
  "status": "Source reviewed; no independent build or execution",
  "subjects": [
    "Scorcher"
  ],
  "tags": [],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [],
  "techniques": [],
  "title": "Scorcher — DOS, Windows and Saturn reversing",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "scorcher-decomp",
  "work_kinds": [
    "binary-analysis",
    "data-format-analysis"
  ]
}
```

### Identity (reviewed)

Scorcher is identified in the pinned project README.
- https://github.com/indieindie7/scorcher-decomp/blob/822003c65663bf8fc93d75a50b04d1202d80293b/README.md

### Classification (reviewed)

Function maps, working notes, Ghidra scripts and selected decompiler output across three builds; not a full reconstructed source tree.
- https://github.com/indieindie7/scorcher-decomp/blob/822003c65663bf8fc93d75a50b04d1202d80293b/README.md

### Source CPU (reviewed)

The README identifies the original platform and x86, sh2 architecture; this describes the source, not the host requirement.
- https://github.com/indieindie7/scorcher-decomp/blob/822003c65663bf8fc93d75a50b04d1202d80293b/README.md

### Target CPU (no-evidence-found)

No minimum output CPU was established; source architecture is not a host requirement.
- https://github.com/indieindie7/scorcher-decomp/blob/822003c65663bf8fc93d75a50b04d1202d80293b/README.md

### Build (reviewed)

Research uses owned game files and Ghidra; selected decompiler dumps do not establish buildability. Limitations: No independent build, execution, gameplay or byte comparison was performed.
- https://github.com/indieindie7/scorcher-decomp/blob/822003c65663bf8fc93d75a50b04d1202d80293b/README.md

### Runtime profiles (no-evidence-found)

No independently verified runtime hardware profile was established from the inspected documentation.
- https://github.com/indieindie7/scorcher-decomp/blob/822003c65663bf8fc93d75a50b04d1202d80293b/README.md

### AI (no-evidence-found)

No explicit development-AI disclosure was established from the inspected README; absence does not establish non-use.
- https://github.com/indieindie7/scorcher-decomp/blob/822003c65663bf8fc93d75a50b04d1202d80293b/README.md

### Relationships (reviewed)

Shares tools with the author's AMOK work but analyzes a distinct game.
- https://github.com/indieindie7/scorcher-decomp/blob/822003c65663bf8fc93d75a50b04d1202d80293b/README.md

## Gungriffon — Saturn function maps

Project ID: indieindie7-gungriffon-decomp · Overall audit: partial

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
  "display_title": "Gungriffon — Saturn function maps",
  "id": "indieindie7-gungriffon-decomp",
  "last_activity": null,
  "last_checked": "2026-11-10",
  "re_started": null,
  "reconstructed_languages": [],
  "record_class": "subject",
  "repo": "https://github.com/indieindie7/gungriffon-decomp",
  "runtime_profiles": [],
  "source_cpu": [
    "sh2"
  ],
  "source_language": [],
  "source_platforms": [
    "Sega Saturn"
  ],
  "status": "Source reviewed; no independent build or execution",
  "subjects": [
    "Gungriffon"
  ],
  "tags": [],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [],
  "techniques": [],
  "title": "Gungriffon — Saturn function maps",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "gungriffon-decomp",
  "work_kinds": [
    "binary-analysis"
  ]
}
```

### Identity (reviewed)

Gungriffon is identified in the pinned project README.
- https://github.com/indieindie7/gungriffon-decomp/blob/024d2dc2addbd1bdd977917ad44c5562711224fa/README.md

### Classification (reviewed)

Function maps cover stage, title and briefing programs; most names are explicitly provisional.
- https://github.com/indieindie7/gungriffon-decomp/blob/024d2dc2addbd1bdd977917ad44c5562711224fa/README.md

### Source CPU (reviewed)

The README identifies the original platform and sh2 architecture; this describes the source, not the host requirement.
- https://github.com/indieindie7/gungriffon-decomp/blob/024d2dc2addbd1bdd977917ad44c5562711224fa/README.md

### Target CPU (no-evidence-found)

No minimum output CPU was established; source architecture is not a host requirement.
- https://github.com/indieindie7/gungriffon-decomp/blob/024d2dc2addbd1bdd977917ad44c5562711224fa/README.md

### Build (reviewed)

Original disc and Ghidra required; symbol counts do not establish semantic completeness. Limitations: No independent build, execution, gameplay or byte comparison was performed.
- https://github.com/indieindie7/gungriffon-decomp/blob/024d2dc2addbd1bdd977917ad44c5562711224fa/README.md

### Runtime profiles (no-evidence-found)

No independently verified runtime hardware profile was established from the inspected documentation.
- https://github.com/indieindie7/gungriffon-decomp/blob/024d2dc2addbd1bdd977917ad44c5562711224fa/README.md

### AI (reviewed)

The README explicitly describes local-model review of naming decisions; model identity is not established.
- https://github.com/indieindie7/gungriffon-decomp/blob/024d2dc2addbd1bdd977917ad44c5562711224fa/README.md

### Relationships (reviewed)

Uses related author tooling but covers a distinct game.
- https://github.com/indieindie7/gungriffon-decomp/blob/024d2dc2addbd1bdd977917ad44c5562711224fa/README.md

## Dead or Alive — Saturn and arcade analysis

Project ID: indieindie7-deadoralive-decomp · Overall audit: partial

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
  "display_title": "Dead or Alive — Saturn and arcade analysis",
  "id": "indieindie7-deadoralive-decomp",
  "last_activity": null,
  "last_checked": "2026-11-10",
  "re_started": null,
  "reconstructed_languages": [],
  "record_class": "subject",
  "repo": "https://github.com/indieindie7/deadoralive-decomp",
  "runtime_profiles": [],
  "source_cpu": [
    "sh2",
    "i960"
  ],
  "source_language": [],
  "source_platforms": [
    "Sega Saturn",
    "Arcade"
  ],
  "status": "Source reviewed; no independent build or execution",
  "subjects": [
    "Dead or Alive"
  ],
  "tags": [],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [],
  "techniques": [],
  "title": "Dead or Alive — Saturn and arcade analysis",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "deadoralive-decomp",
  "work_kinds": [
    "binary-analysis"
  ]
}
```

### Identity (reviewed)

Dead or Alive is identified in the pinned project README.
- https://github.com/indieindie7/deadoralive-decomp/blob/558cddc3c51718aa5e9264b045e498e5875e6fc7/README.md

### Classification (reviewed)

Function naming and review records cover the Saturn main program and Model 2 arcade version; no game binaries or reconstructed source are distributed.
- https://github.com/indieindie7/deadoralive-decomp/blob/558cddc3c51718aa5e9264b045e498e5875e6fc7/README.md

### Source CPU (reviewed)

The README identifies the original platform and sh2, i960 architecture; this describes the source, not the host requirement.
- https://github.com/indieindie7/deadoralive-decomp/blob/558cddc3c51718aa5e9264b045e498e5875e6fc7/README.md

### Target CPU (no-evidence-found)

No minimum output CPU was established; source architecture is not a host requirement.
- https://github.com/indieindie7/deadoralive-decomp/blob/558cddc3c51718aa5e9264b045e498e5875e6fc7/README.md

### Build (reviewed)

Owned binaries and Ghidra needed; named functions are not a rebuild. Limitations: No independent build, execution, gameplay or byte comparison was performed.
- https://github.com/indieindie7/deadoralive-decomp/blob/558cddc3c51718aa5e9264b045e498e5875e6fc7/README.md

### Runtime profiles (no-evidence-found)

No independently verified runtime hardware profile was established from the inspected documentation.
- https://github.com/indieindie7/deadoralive-decomp/blob/558cddc3c51718aa5e9264b045e498e5875e6fc7/README.md

### AI (reviewed)

The README explicitly describes local-model review of naming decisions; model identity is not established.
- https://github.com/indieindie7/deadoralive-decomp/blob/558cddc3c51718aa5e9264b045e498e5875e6fc7/README.md

### Relationships (reviewed)

Same methodology as Astal and Clockwork Knight, but a separate game.
- https://github.com/indieindie7/deadoralive-decomp/blob/558cddc3c51718aa5e9264b045e498e5875e6fc7/README.md

## Cyber Speedway — Saturn overlay analysis

Project ID: indieindie7-cyberspeedway-decomp · Overall audit: partial

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
  "display_title": "Cyber Speedway — Saturn overlay analysis",
  "id": "indieindie7-cyberspeedway-decomp",
  "last_activity": null,
  "last_checked": "2026-11-10",
  "re_started": null,
  "reconstructed_languages": [],
  "record_class": "subject",
  "repo": "https://github.com/indieindie7/cyberspeedway-decomp",
  "runtime_profiles": [],
  "source_cpu": [
    "sh2"
  ],
  "source_language": [],
  "source_platforms": [
    "Sega Saturn"
  ],
  "status": "Source reviewed; no independent build or execution",
  "subjects": [
    "Cyber Speedway"
  ],
  "tags": [],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [],
  "techniques": [],
  "title": "Cyber Speedway — Saturn overlay analysis",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "cyberspeedway-decomp",
  "work_kinds": [
    "binary-analysis"
  ]
}
```

### Identity (reviewed)

Cyber Speedway is identified in the pinned project README.
- https://github.com/indieindie7/cyberspeedway-decomp/blob/c6b4ee9213d6a2d3596b8d5703b54974e418874e/README.md

### Classification (reviewed)

Names and review records cover 38 Saturn overlays, with cross-overlay tooling; no game program or decompiled C included.
- https://github.com/indieindie7/cyberspeedway-decomp/blob/c6b4ee9213d6a2d3596b8d5703b54974e418874e/README.md

### Source CPU (reviewed)

The README identifies the original platform and sh2 architecture; this describes the source, not the host requirement.
- https://github.com/indieindie7/cyberspeedway-decomp/blob/c6b4ee9213d6a2d3596b8d5703b54974e418874e/README.md

### Target CPU (no-evidence-found)

No minimum output CPU was established; source architecture is not a host requirement.
- https://github.com/indieindie7/cyberspeedway-decomp/blob/c6b4ee9213d6a2d3596b8d5703b54974e418874e/README.md

### Build (reviewed)

Requires owned program files and Ghidra; symbol coverage does not prove functional correctness. Limitations: No independent build, execution, gameplay or byte comparison was performed.
- https://github.com/indieindie7/cyberspeedway-decomp/blob/c6b4ee9213d6a2d3596b8d5703b54974e418874e/README.md

### Runtime profiles (no-evidence-found)

No independently verified runtime hardware profile was established from the inspected documentation.
- https://github.com/indieindie7/cyberspeedway-decomp/blob/c6b4ee9213d6a2d3596b8d5703b54974e418874e/README.md

### AI (no-evidence-found)

No explicit development-AI disclosure was established from the inspected README; absence does not establish non-use.
- https://github.com/indieindie7/cyberspeedway-decomp/blob/c6b4ee9213d6a2d3596b8d5703b54974e418874e/README.md

### Relationships (reviewed)

Shares tooling with author's Scorcher and AMOK studies but is a distinct game.
- https://github.com/indieindie7/cyberspeedway-decomp/blob/c6b4ee9213d6a2d3596b8d5703b54974e418874e/README.md

## Clockwork Knight — Saturn analysis and symbols

Project ID: indieindie7-clockworkknight-decomp · Overall audit: partial

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
  "display_title": "Clockwork Knight — Saturn analysis and symbols",
  "id": "indieindie7-clockworkknight-decomp",
  "last_activity": null,
  "last_checked": "2026-11-10",
  "re_started": null,
  "reconstructed_languages": [],
  "record_class": "subject",
  "repo": "https://github.com/indieindie7/clockworkknight-decomp",
  "runtime_profiles": [],
  "source_cpu": [
    "sh2"
  ],
  "source_language": [],
  "source_platforms": [
    "Sega Saturn"
  ],
  "status": "Source reviewed; no independent build or execution",
  "subjects": [
    "Clockwork Knight"
  ],
  "tags": [],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [],
  "techniques": [],
  "title": "Clockwork Knight — Saturn analysis and symbols",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "clockworkknight-decomp",
  "work_kinds": [
    "binary-analysis"
  ]
}
```

### Identity (reviewed)

Clockwork Knight is identified in the pinned project README.
- https://github.com/indieindie7/clockworkknight-decomp/blob/0e680dd83e14646ca3bdde8634f07ea3afb00d01/README.md

### Classification (reviewed)

Function maps and review records cover multiple Clockwork Knight titles and compilation programs; provisional labels remain author interpretations.
- https://github.com/indieindie7/clockworkknight-decomp/blob/0e680dd83e14646ca3bdde8634f07ea3afb00d01/README.md

### Source CPU (reviewed)

The README identifies the original platform and sh2 architecture; this describes the source, not the host requirement.
- https://github.com/indieindie7/clockworkknight-decomp/blob/0e680dd83e14646ca3bdde8634f07ea3afb00d01/README.md

### Target CPU (no-evidence-found)

No minimum output CPU was established; source architecture is not a host requirement.
- https://github.com/indieindie7/clockworkknight-decomp/blob/0e680dd83e14646ca3bdde8634f07ea3afb00d01/README.md

### Build (reviewed)

Requires original programs and analysis tools; no complete rebuilt game established. Limitations: No independent build, execution, gameplay or byte comparison was performed.
- https://github.com/indieindie7/clockworkknight-decomp/blob/0e680dd83e14646ca3bdde8634f07ea3afb00d01/README.md

### Runtime profiles (no-evidence-found)

No independently verified runtime hardware profile was established from the inspected documentation.
- https://github.com/indieindie7/clockworkknight-decomp/blob/0e680dd83e14646ca3bdde8634f07ea3afb00d01/README.md

### AI (no-evidence-found)

No explicit development-AI disclosure was established from the inspected README; absence does not establish non-use.
- https://github.com/indieindie7/clockworkknight-decomp/blob/0e680dd83e14646ca3bdde8634f07ea3afb00d01/README.md

### Relationships (reviewed)

Shared tooling with related Saturn studies; this is a separate game series.
- https://github.com/indieindie7/clockworkknight-decomp/blob/0e680dd83e14646ca3bdde8634f07ea3afb00d01/README.md

## Robotica / Daedalus — Saturn function analysis

Project ID: indieindie7-robotica-decomp · Overall audit: partial

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
  "display_title": "Robotica / Daedalus — Saturn function analysis",
  "id": "indieindie7-robotica-decomp",
  "last_activity": null,
  "last_checked": "2026-11-10",
  "re_started": null,
  "reconstructed_languages": [],
  "record_class": "subject",
  "repo": "https://github.com/indieindie7/robotica-decomp",
  "runtime_profiles": [],
  "source_cpu": [
    "sh2"
  ],
  "source_language": [],
  "source_platforms": [
    "Sega Saturn"
  ],
  "status": "Source reviewed; no independent build or execution",
  "subjects": [
    "Robotica"
  ],
  "tags": [],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [],
  "techniques": [],
  "title": "Robotica / Daedalus — Saturn function analysis",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "robotica-decomp",
  "work_kinds": [
    "binary-analysis"
  ]
}
```

### Identity (reviewed)

Robotica is identified in the pinned project README.
- https://github.com/indieindie7/robotica-decomp/blob/677b9343e0a51d0e2c038b3a8c41eb0b3db14533/README.md

### Classification (reviewed)

Function maps and tooling study the Saturn FPS main program; README marks remaining names provisional.
- https://github.com/indieindie7/robotica-decomp/blob/677b9343e0a51d0e2c038b3a8c41eb0b3db14533/README.md

### Source CPU (reviewed)

The README identifies the original platform and sh2 architecture; this describes the source, not the host requirement.
- https://github.com/indieindie7/robotica-decomp/blob/677b9343e0a51d0e2c038b3a8c41eb0b3db14533/README.md

### Target CPU (no-evidence-found)

No minimum output CPU was established; source architecture is not a host requirement.
- https://github.com/indieindie7/robotica-decomp/blob/677b9343e0a51d0e2c038b3a8c41eb0b3db14533/README.md

### Build (reviewed)

Original game image and Ghidra required; names are hypotheses, not source reconstruction. Limitations: No independent build, execution, gameplay or byte comparison was performed.
- https://github.com/indieindie7/robotica-decomp/blob/677b9343e0a51d0e2c038b3a8c41eb0b3db14533/README.md

### Runtime profiles (no-evidence-found)

No independently verified runtime hardware profile was established from the inspected documentation.
- https://github.com/indieindie7/robotica-decomp/blob/677b9343e0a51d0e2c038b3a8c41eb0b3db14533/README.md

### AI (reviewed)

The README explicitly describes local-model review of naming decisions; model identity is not established.
- https://github.com/indieindie7/robotica-decomp/blob/677b9343e0a51d0e2c038b3a8c41eb0b3db14533/README.md

### Relationships (reviewed)

Distinct game from related Gungriffon and Saturn projects.
- https://github.com/indieindie7/robotica-decomp/blob/677b9343e0a51d0e2c038b3a8c41eb0b3db14533/README.md

## Cyber Sled — arcade 68000 analysis

Project ID: indieindie7-cybersled-decomp · Overall audit: partial

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
  "display_title": "Cyber Sled — arcade 68000 analysis",
  "id": "indieindie7-cybersled-decomp",
  "last_activity": null,
  "last_checked": "2026-11-10",
  "re_started": null,
  "reconstructed_languages": [],
  "record_class": "subject",
  "repo": "https://github.com/indieindie7/cybersled-decomp",
  "runtime_profiles": [],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [],
  "source_platforms": [
    "Arcade"
  ],
  "status": "Source reviewed; no independent build or execution",
  "subjects": [
    "Cyber Sled"
  ],
  "tags": [],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [],
  "techniques": [],
  "title": "Cyber Sled — arcade 68000 analysis",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "cybersled-decomp",
  "work_kinds": [
    "binary-analysis"
  ]
}
```

### Identity (reviewed)

Cyber Sled is identified in the pinned project README.
- https://github.com/indieindie7/cybersled-decomp/blob/67d3ca93950ab84d453890b00a0737be883d3243/README.md

### Classification (reviewed)

Function maps and labels study the two 68000 programs of the System 21 arcade game.
- https://github.com/indieindie7/cybersled-decomp/blob/67d3ca93950ab84d453890b00a0737be883d3243/README.md

### Source CPU (reviewed)

The README identifies the original platform and m68k architecture; this describes the source, not the host requirement.
- https://github.com/indieindie7/cybersled-decomp/blob/67d3ca93950ab84d453890b00a0737be883d3243/README.md

### Target CPU (no-evidence-found)

No minimum output CPU was established; source architecture is not a host requirement.
- https://github.com/indieindie7/cybersled-decomp/blob/67d3ca93950ab84d453890b00a0737be883d3243/README.md

### Build (reviewed)

Original game binaries and Ghidra are needed; analysis is not a rebuilt executable. Limitations: No independent build, execution, gameplay or byte comparison was performed.
- https://github.com/indieindie7/cybersled-decomp/blob/67d3ca93950ab84d453890b00a0737be883d3243/README.md

### Runtime profiles (no-evidence-found)

No independently verified runtime hardware profile was established from the inspected documentation.
- https://github.com/indieindie7/cybersled-decomp/blob/67d3ca93950ab84d453890b00a0737be883d3243/README.md

### AI (no-evidence-found)

No explicit development-AI disclosure was established from the inspected README; absence does not establish non-use.
- https://github.com/indieindie7/cybersled-decomp/blob/67d3ca93950ab84d453890b00a0737be883d3243/README.md

### Relationships (reviewed)

Related by tooling to Scorcher and AMOK but studies a separate arcade title.
- https://github.com/indieindie7/cybersled-decomp/blob/67d3ca93950ab84d453890b00a0737be883d3243/README.md

## Faxanadu — Atari ST port

Project ID: georgeflower-faxanadu-atari-st · Overall audit: partial

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
  "display_title": "Faxanadu — Atari ST port",
  "id": "georgeflower-faxanadu-atari-st",
  "last_activity": null,
  "last_checked": "2026-11-10",
  "re_started": null,
  "reconstructed_languages": [
    "m68k assembly",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/georgeflower/faxanadu-atari-st",
  "runtime_profiles": [],
  "source_cpu": [
    "6502"
  ],
  "source_language": [],
  "source_platforms": [
    "NES"
  ],
  "status": "Source reviewed; no independent build or execution",
  "subjects": [
    "Faxanadu"
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
  "title": "Faxanadu — Atari ST port",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "faxanadu-atari-st",
  "work_kinds": [
    "reverse-engineering-derived-port"
  ]
}
```

### Identity (reviewed)

Faxanadu is identified in the pinned project README.
- https://github.com/georgeflower/faxanadu-atari-st/blob/33f26f6a8a3435769d66e09569722371196f60ce/README.md

### Classification (reviewed)

Work-in-progress 68000 Atari ST port based on chipx86's NES disassembly, using assets extracted from a user-supplied ROM. The current plan reports progress beyond the stale colour-bars-only README: screen rendering, scrolling, input, walking and jumping; other systems are unfinished.
- https://github.com/georgeflower/faxanadu-atari-st/blob/33f26f6a8a3435769d66e09569722371196f60ce/README.md
- https://github.com/georgeflower/faxanadu-atari-st/blob/33f26f6a8a3435769d66e09569722371196f60ce/atari_st/PLAN.md

### Source CPU (reviewed)

The README identifies the NES ROM as input and a separate 68000 Atari ST output.
- https://github.com/georgeflower/faxanadu-atari-st/blob/33f26f6a8a3435769d66e09569722371196f60ce/README.md

### Target CPU (reviewed)

The README specifies a 68000 Atari ST build.
- https://github.com/georgeflower/faxanadu-atari-st/blob/33f26f6a8a3435769d66e09569722371196f60ce/README.md

### Build (reviewed)

README claims a TOS PRG build, but this review did not build or run it. Limitations: No independent build, execution, gameplay or byte comparison was performed.
- https://github.com/georgeflower/faxanadu-atari-st/blob/33f26f6a8a3435769d66e09569722371196f60ce/README.md

### Runtime profiles (no-evidence-found)

No independently verified runtime hardware profile was established from the inspected documentation.
- https://github.com/georgeflower/faxanadu-atari-st/blob/33f26f6a8a3435769d66e09569722371196f60ce/README.md

### AI (reviewed)

The README explicitly states the port was built with AI help, without identifying a tool.
- https://github.com/georgeflower/faxanadu-atari-st/blob/33f26f6a8a3435769d66e09569722371196f60ce/README.md

### Relationships (reviewed)

Uses chipx86's NES disassembly; distinct from the tracked NES-to-PC recompilation.
- https://github.com/georgeflower/faxanadu-atari-st/blob/33f26f6a8a3435769d66e09569722371196f60ce/README.md

## SimTower — Win16 to native Windows port

Project ID: kandowontu2-simtower-native-windows-port · Overall audit: partial

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
  "display_title": "SimTower — Win16 to native Windows port",
  "id": "kandowontu2-simtower-native-windows-port",
  "last_activity": null,
  "last_checked": "2026-11-10",
  "re_started": null,
  "reconstructed_languages": [
    "C++"
  ],
  "record_class": "subject",
  "repo": "https://github.com/kandowontu2/simtower-native-windows-port",
  "runtime_profiles": [],
  "source_cpu": [
    "x86"
  ],
  "source_language": [],
  "source_platforms": [
    "Windows"
  ],
  "status": "Source reviewed; no independent build or execution",
  "subjects": [
    "SimTower"
  ],
  "tags": [],
  "target_cpu": [
    "x86-64"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Windows"
  ],
  "techniques": [],
  "title": "SimTower — Win16 to native Windows port",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "simtower-native-windows-port",
  "work_kinds": [
    "binary-analysis",
    "reverse-engineering-derived-port"
  ]
}
```

### Identity (reviewed)

SimTower is identified in the pinned project README.
- https://github.com/kandowontu2/simtower-native-windows-port/blob/b9a8b2849710482d3b6feb31a7af194961f351c6/README.md

### Classification (reviewed)

Function-by-function x86-64 port of the Win16 game with NE analysis and call graph; original resources are not distributed.
- https://github.com/kandowontu2/simtower-native-windows-port/blob/b9a8b2849710482d3b6feb31a7af194961f351c6/README.md

### Source CPU (reviewed)

The README identifies the original platform and x86 architecture; this describes the source, not the host requirement.
- https://github.com/kandowontu2/simtower-native-windows-port/blob/b9a8b2849710482d3b6feb31a7af194961f351c6/README.md

### Target CPU (reviewed)

The README describes an x86-64 Windows port.
- https://github.com/kandowontu2/simtower-native-windows-port/blob/b9a8b2849710482d3b6feb31a7af194961f351c6/README.md

### Build (reviewed)

Author reports tests and limited original/native checks; build requires extracted original resources, and this review did not run it. Limitations: No independent build, execution, gameplay or byte comparison was performed.
- https://github.com/kandowontu2/simtower-native-windows-port/blob/b9a8b2849710482d3b6feb31a7af194961f351c6/README.md

### Runtime profiles (no-evidence-found)

No independently verified runtime hardware profile was established from the inspected documentation.
- https://github.com/kandowontu2/simtower-native-windows-port/blob/b9a8b2849710482d3b6feb31a7af194961f351c6/README.md

### AI (no-evidence-found)

No explicit development-AI disclosure was established from the inspected README; absence does not establish non-use.
- https://github.com/kandowontu2/simtower-native-windows-port/blob/b9a8b2849710482d3b6feb31a7af194961f351c6/README.md

### Relationships (reviewed)

Distinct game project; no identical repository found in current catalogue.
- https://github.com/kandowontu2/simtower-native-windows-port/blob/b9a8b2849710482d3b6feb31a7af194961f351c6/README.md

## Laser Squad — Spectrum Analyser research

Project ID: colourclash-lasersquad · Overall audit: partial

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
  "display_title": "Laser Squad — Spectrum Analyser research",
  "id": "colourclash-lasersquad",
  "last_activity": null,
  "last_checked": "2026-11-10",
  "re_started": null,
  "reconstructed_languages": [],
  "record_class": "subject",
  "repo": "https://github.com/Colourclash/LaserSquad",
  "runtime_profiles": [],
  "source_cpu": [
    "z80"
  ],
  "source_language": [],
  "source_platforms": [
    "ZX Spectrum"
  ],
  "status": "Source reviewed; no independent build or execution",
  "subjects": [
    "Laser Squad"
  ],
  "tags": [],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [],
  "techniques": [],
  "title": "Laser Squad — Spectrum Analyser research",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "LaserSquad",
  "work_kinds": [
    "disassembly",
    "binary-analysis"
  ]
}
```

### Identity (reviewed)

Laser Squad is identified in the pinned project README.
- https://github.com/colourclash/lasersquad/blob/6ea702fef289e8e504cd76e48c1a92d3161ac02a/README.md

### Classification (reviewed)

Partial work-in-progress disassembly for scenario 1, with Lua viewers for maps, commands and graphics in Spectrum Analyser.
- https://github.com/colourclash/lasersquad/blob/6ea702fef289e8e504cd76e48c1a92d3161ac02a/README.md

### Source CPU (reviewed)

The README identifies the ZX Spectrum as the original platform; its processor is Z80.
- https://github.com/colourclash/lasersquad/blob/6ea702fef289e8e504cd76e48c1a92d3161ac02a/README.md

### Target CPU (no-evidence-found)

No minimum output CPU was established; source architecture is not a host requirement.
- https://github.com/colourclash/lasersquad/blob/6ea702fef289e8e504cd76e48c1a92d3161ac02a/README.md

### Build (reviewed)

Requires the Spectrum Analyser workspace and snapshot; no rebuild is claimed. Limitations: No independent build, execution, gameplay or byte comparison was performed.
- https://github.com/colourclash/lasersquad/blob/6ea702fef289e8e504cd76e48c1a92d3161ac02a/README.md

### Runtime profiles (no-evidence-found)

No independently verified runtime hardware profile was established from the inspected documentation.
- https://github.com/colourclash/lasersquad/blob/6ea702fef289e8e504cd76e48c1a92d3161ac02a/README.md

### AI (no-evidence-found)

No explicit development-AI disclosure was established from the inspected README; absence does not establish non-use.
- https://github.com/colourclash/lasersquad/blob/6ea702fef289e8e504cd76e48c1a92d3161ac02a/README.md

### Relationships (reviewed)

Uses TheGoodDoktor's Spectrum Analyser, distinct from the tool project.
- https://github.com/colourclash/lasersquad/blob/6ea702fef289e8e504cd76e48c1a92d3161ac02a/README.md

## Ganbare Goemon — MSX2 translation reconstruction

Project ID: emukp-ganbare · Overall audit: partial

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
  "display_title": "Ganbare Goemon — MSX2 translation reconstruction",
  "id": "emukp-ganbare",
  "last_activity": null,
  "last_checked": "2026-11-10",
  "re_started": null,
  "reconstructed_languages": [
    "Z80 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/emukp/Ganbare",
  "runtime_profiles": [],
  "source_cpu": [
    "z80"
  ],
  "source_language": [],
  "source_platforms": [
    "MSX2"
  ],
  "status": "Source reviewed; no independent build or execution",
  "subjects": [
    "Ganbare Goemon"
  ],
  "tags": [],
  "target_cpu": [
    "z80"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "MSX2"
  ],
  "techniques": [],
  "title": "Ganbare Goemon — MSX2 translation reconstruction",
  "tool_kinds": [],
  "types": [
    "subject"
  ],
  "upstream_name": "Ganbare",
  "work_kinds": [
    "disassembly",
    "source-reconstruction"
  ]
}
```

### Identity (reviewed)

Ganbare Goemon is identified in the pinned project README.
- https://github.com/emukp/ganbare/blob/2ee09eab0d75f7e5c751fcef5e7ba2c7ab1fbec6/README.md

### Classification (reviewed)

Chinese translation of the MSX2 game reorganizes original and expanded banks into Z80 assembly including logic, graphics and sound modules.
- https://github.com/emukp/ganbare/blob/2ee09eab0d75f7e5c751fcef5e7ba2c7ab1fbec6/README.md

### Source CPU (reviewed)

The README identifies MSX2 and Z80 assembly, with original and expanded banks.
- https://github.com/emukp/ganbare/blob/2ee09eab0d75f7e5c751fcef5e7ba2c7ab1fbec6/README.md

### Target CPU (reviewed)

The SjASMPlus source targets MSX2 Z80.
- https://github.com/emukp/ganbare/blob/2ee09eab0d75f7e5c751fcef5e7ba2c7ab1fbec6/README.md

### Build (reviewed)

README gives SjASMPlus build steps; no independent build, byte-identity or gameplay check. Limitations: No independent build, execution, gameplay or byte comparison was performed.
- https://github.com/emukp/ganbare/blob/2ee09eab0d75f7e5c751fcef5e7ba2c7ab1fbec6/README.md

### Runtime profiles (no-evidence-found)

No independently verified runtime hardware profile was established from the inspected documentation.
- https://github.com/emukp/ganbare/blob/2ee09eab0d75f7e5c751fcef5e7ba2c7ab1fbec6/README.md

### AI (no-evidence-found)

No explicit development-AI disclosure was established from the inspected README; absence does not establish non-use.
- https://github.com/emukp/ganbare/blob/2ee09eab0d75f7e5c751fcef5e7ba2c7ab1fbec6/README.md

### Relationships (reviewed)

Distinct MSX2 game and translation work, not the tracked SNES Goemon 3 disassembly.
- https://github.com/emukp/ganbare/blob/2ee09eab0d75f7e5c751fcef5e7ba2c7ab1fbec6/README.md

## Pinned evidence manifest

- colourclash-lasersquad-readme: https://github.com/colourclash/lasersquad/blob/6ea702fef289e8e504cd76e48c1a92d3161ac02a/README.md (Git blob 9e941ce744c651eede4dea98098aafb243505055)
- emukp-ganbare-readme: https://github.com/emukp/ganbare/blob/2ee09eab0d75f7e5c751fcef5e7ba2c7ab1fbec6/README.md (Git blob f9e5ec6ce1c6300b4f2d6916244fa49821664648)
- georgeflower-faxanadu-atari-st-plan: https://github.com/georgeflower/faxanadu-atari-st/blob/33f26f6a8a3435769d66e09569722371196f60ce/atari_st/PLAN.md (Git blob c8892bc022af180071ee6b49e6410b13f23f584c)
- georgeflower-faxanadu-atari-st-readme: https://github.com/georgeflower/faxanadu-atari-st/blob/33f26f6a8a3435769d66e09569722371196f60ce/README.md (Git blob 0df8f3a381692f9098332cbbd782bbf9fb1e8efa)
- indieindie7-clockworkknight-decomp-readme: https://github.com/indieindie7/clockworkknight-decomp/blob/0e680dd83e14646ca3bdde8634f07ea3afb00d01/README.md (Git blob b738d85e0a9cc59d477edfa26c90f882ac7ef172)
- indieindie7-cybersled-decomp-readme: https://github.com/indieindie7/cybersled-decomp/blob/67d3ca93950ab84d453890b00a0737be883d3243/README.md (Git blob 93ee2e1e34cbd699a5da8e999e638e82237a4581)
- indieindie7-cyberspeedway-decomp-readme: https://github.com/indieindie7/cyberspeedway-decomp/blob/c6b4ee9213d6a2d3596b8d5703b54974e418874e/README.md (Git blob 7d90a864a0b4181689559d7a9685e49eab41bc8c)
- indieindie7-deadoralive-decomp-readme: https://github.com/indieindie7/deadoralive-decomp/blob/558cddc3c51718aa5e9264b045e498e5875e6fc7/README.md (Git blob 61cb60eb08b28011f951033dc314e0f3fa2ea0d0)
- indieindie7-gungriffon-decomp-readme: https://github.com/indieindie7/gungriffon-decomp/blob/024d2dc2addbd1bdd977917ad44c5562711224fa/README.md (Git blob 7d1062149fe2f7127dc41a5ffadb0c048dda6cf3)
- indieindie7-robotica-decomp-readme: https://github.com/indieindie7/robotica-decomp/blob/677b9343e0a51d0e2c038b3a8c41eb0b3db14533/README.md (Git blob f58d2bd4d1d14efe8407f1704b9af4bd6f5f3130)
- indieindie7-scorcher-decomp-readme: https://github.com/indieindie7/scorcher-decomp/blob/822003c65663bf8fc93d75a50b04d1202d80293b/README.md (Git blob da1519301df41883fbc389216b57e5a46facdd74)
- kandowontu2-simtower-native-windows-port-readme: https://github.com/kandowontu2/simtower-native-windows-port/blob/b9a8b2849710482d3b6feb31a7af194961f351c6/README.md (Git blob 54355a38ac4e26c2a74fd250ddad2e8d80b961b7)

## Sources

```json
[
  {
    "first_indexed": "2026-11-10",
    "id": "github-indieindie7-scorcher-decomp",
    "kind": "github-repository",
    "last_reviewed": "2026-11-10",
    "open_task_ids": [],
    "projects_promoted": [
      "indieindie7-scorcher-decomp"
    ],
    "reason": "Function maps, working notes, Ghidra scripts and selected decompiler output across three builds; not a full reconstructed source tree.",
    "review_state": "partial",
    "source": "https://github.com/indieindie7/scorcher-decomp"
  },
  {
    "first_indexed": "2026-11-10",
    "id": "github-indieindie7-gungriffon-decomp",
    "kind": "github-repository",
    "last_reviewed": "2026-11-10",
    "open_task_ids": [],
    "projects_promoted": [
      "indieindie7-gungriffon-decomp"
    ],
    "reason": "Function maps cover stage, title and briefing programs; most names are explicitly provisional.",
    "review_state": "partial",
    "source": "https://github.com/indieindie7/gungriffon-decomp"
  },
  {
    "first_indexed": "2026-11-10",
    "id": "github-indieindie7-deadoralive-decomp",
    "kind": "github-repository",
    "last_reviewed": "2026-11-10",
    "open_task_ids": [],
    "projects_promoted": [
      "indieindie7-deadoralive-decomp"
    ],
    "reason": "Function naming and review records cover the Saturn main program and Model 2 arcade version; no game binaries or reconstructed source are distributed.",
    "review_state": "partial",
    "source": "https://github.com/indieindie7/deadoralive-decomp"
  },
  {
    "first_indexed": "2026-11-10",
    "id": "github-indieindie7-cyberspeedway-decomp",
    "kind": "github-repository",
    "last_reviewed": "2026-11-10",
    "open_task_ids": [],
    "projects_promoted": [
      "indieindie7-cyberspeedway-decomp"
    ],
    "reason": "Names and review records cover 38 Saturn overlays, with cross-overlay tooling; no game program or decompiled C included.",
    "review_state": "partial",
    "source": "https://github.com/indieindie7/cyberspeedway-decomp"
  },
  {
    "first_indexed": "2026-11-10",
    "id": "github-indieindie7-clockworkknight-decomp",
    "kind": "github-repository",
    "last_reviewed": "2026-11-10",
    "open_task_ids": [],
    "projects_promoted": [
      "indieindie7-clockworkknight-decomp"
    ],
    "reason": "Function maps and review records cover multiple Clockwork Knight titles and compilation programs; provisional labels remain author interpretations.",
    "review_state": "partial",
    "source": "https://github.com/indieindie7/clockworkknight-decomp"
  },
  {
    "first_indexed": "2026-11-10",
    "id": "github-indieindie7-robotica-decomp",
    "kind": "github-repository",
    "last_reviewed": "2026-11-10",
    "open_task_ids": [],
    "projects_promoted": [
      "indieindie7-robotica-decomp"
    ],
    "reason": "Function maps and tooling study the Saturn FPS main program; README marks remaining names provisional.",
    "review_state": "partial",
    "source": "https://github.com/indieindie7/robotica-decomp"
  },
  {
    "first_indexed": "2026-11-10",
    "id": "github-indieindie7-cybersled-decomp",
    "kind": "github-repository",
    "last_reviewed": "2026-11-10",
    "open_task_ids": [],
    "projects_promoted": [
      "indieindie7-cybersled-decomp"
    ],
    "reason": "Function maps and labels study the two 68000 programs of the System 21 arcade game.",
    "review_state": "partial",
    "source": "https://github.com/indieindie7/cybersled-decomp"
  },
  {
    "first_indexed": "2026-11-10",
    "id": "github-kandowontu2-simtower-native-windows-port",
    "kind": "github-repository",
    "last_reviewed": "2026-11-10",
    "open_task_ids": [],
    "projects_promoted": [
      "kandowontu2-simtower-native-windows-port"
    ],
    "reason": "Function-by-function x86-64 port of the Win16 game with NE analysis and call graph; original resources are not distributed.",
    "review_state": "partial",
    "source": "https://github.com/kandowontu2/simtower-native-windows-port"
  },
  {
    "first_indexed": "2026-11-10",
    "id": "github-colourclash-lasersquad",
    "kind": "github-repository",
    "last_reviewed": "2026-11-10",
    "open_task_ids": [],
    "projects_promoted": [
      "colourclash-lasersquad"
    ],
    "reason": "Partial work-in-progress disassembly for scenario 1, with Lua viewers for maps, commands and graphics in Spectrum Analyser.",
    "review_state": "partial",
    "source": "https://github.com/Colourclash/LaserSquad"
  },
  {
    "first_indexed": "2026-11-10",
    "id": "github-emukp-ganbare",
    "kind": "github-repository",
    "last_reviewed": "2026-11-10",
    "open_task_ids": [],
    "projects_promoted": [
      "emukp-ganbare"
    ],
    "reason": "Chinese translation of the MSX2 game reorganizes original and expanded banks into Z80 assembly including logic, graphics and sound modules.",
    "review_state": "partial",
    "source": "https://github.com/emukp/Ganbare"
  }
]
```

## Source updates

```json
[
  {
    "id": "github-georgeflower-faxanadu-atari-st",
    "last_reviewed": "2026-11-10",
    "reason": "Previously deferred as colour bars only; current plan reports screen rendering, scrolling, input, walking and jumping. Further game systems remain in progress.",
    "review_state": "partial"
  }
]
```

## Research event notes

Personally screened the current catalogue and primary pinned documentation. No independent build, execution, gameplay or binary comparison.
