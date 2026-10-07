# 9 further Macintosh 68k game projects: source and implementation review

Review 9 further Macintosh 68k game projects and documented holds

Date: 2026-10-07 · Review: ready

Snapshot check: all pinned proofs match the supplied expected commits.

## Uncertainty and next checks

- beast-mac-pascal-swift-reconstruction / Build (reviewed): No game was compiled, launched, played, hardware-tested or byte-compared. All independent verification flags remain unknown.
- megaroids-mac-swift-source-reconstruction / Build (reviewed): No game was compiled, launched, played, hardware-tested or byte-compared. All independent verification flags remain unknown.
- missile-macintosh-munafo-original-source / Build (reviewed): No game was compiled, launched, played, hardware-tested or byte-compared. All independent verification flags remain unknown.
- missile-macintosh-munafo-original-source / AI (no-evidence-found): No development-AI attribution found on the inspected source page; non-use is not established.
- multipong-native-mac68k-jcgraybill / Build (reviewed): No dependency installation, game compilation, tests, launch, gameplay, hardware check or binary comparison was performed. All build-verification flags remain null.
- multipong-native-mac68k-jcgraybill / Runtime profiles (no-evidence-found): No exact minimum Macintosh model, OS release, RAM budget or CPU speed is stated in the inspected README/source. WaitNextEvent, menu/resource lookups and QuickDraw region behavior are required by the code, but they are not converted into an unsupported numeric hardware or OS floor.
- multipong-native-mac68k-jcgraybill / AI (no-evidence-found): The inspected README and complete available 13-commit message history contain no explicit development-AI disclosure or assistant co-author trailer. This does not establish non-use; age, coding style and filenames are not AI evidence.
- battlechess-macintosh-native-recompilation / Build (reviewed): No dependency installation, game compilation, tests, launch, gameplay, hardware check or binary comparison was performed. All build-verification flags remain null. Original idle-animation triggering, timing/audio, computer choices, save exchange and modem interoperability remain incomplete or unverified upstream.
- battlechess-macintosh-native-recompilation / Runtime profiles (no-evidence-found): The application needs a desktop video/audio environment supported by SDL3 and the matching external data pack. No exact minimum CPU, RAM, macOS version or Linux distribution is established. Original Macintosh source architecture and dummy-driver smoke tests are not host runtime minima.
- battlechess-macintosh-native-recompilation / AI (no-evidence-found): NOTICE describes the icon as generated artwork but does not name an AI system; its linked resources/ICON.md is absent from the pinned tree. Neither that wording nor a filename establishes development-AI usage.
- 3tris-html5-francescom / Build (reviewed): No dependency installation, game compilation, tests, launch, gameplay, hardware check or binary comparison was performed. All build-verification flags remain null.
- 3tris-html5-francescom / AI (no-evidence-found): The inspected README and complete available 7-commit message history contain no explicit development-AI disclosure or assistant co-author trailer. This does not establish non-use; age, coding style and filenames are not AI evidence.
- wolf3d-mac-original-source-archive / Build (reviewed): No dependency installation, game compilation, tests, launch, gameplay, hardware check or binary comparison was performed. All build-verification flags remain null. README’s original author build claim is historical and does not verify this mirror.
- wolf3d-mac-original-source-archive / AI (no-evidence-found): The inspected README and complete available 1-commit message history contain no explicit development-AI disclosure or assistant co-author trailer. This does not establish non-use; age, coding style and filenames are not AI evidence.
- sparks-classic-mac-restoration-depp / Build (reviewed): No compilation, tests, execution, gameplay or binary comparison was performed. All build booleans remain null.
- sparks-classic-mac-restoration-depp / Runtime profiles (no-evidence-found): Main.cpp tests Color QuickDraw availability and an 8-bit display mode, then allocates a GWorld backbuffer. These are implementation requirements, but the inspected material supplies no authoritative minimum CPU model or RAM for a usable game; no runnable hardware profile is asserted.
- sparks-classic-mac-restoration-depp / AI (no-evidence-found): The inspected README and original-code/bootstrap material contain no explicit development-AI disclosure. This is a bounded negative search, not evidence of non-use; usage remains unknown.
- sparks-classic-mac-restoration-depp / Relationships (reviewed): The other copy’s provenance and current location remain unresolved.
- galactic-empire-minimicro-joestrout / Source CPU (reviewed): The original help is MacRoman and was retrieved as exact base64 bytes, decoded only for static reading and Git-blob verified against the pinned tree. It is cited as a binary/non-UTF-8 file instead of falsely re-encoding it in the UTF-8 proof cache.
- galactic-empire-minimicro-joestrout / Target CPU (no-evidence-found): The README targets the Mini Micro interpreter and the author distributes an HTML5 build. Neither the MiniScript game nor the inspected instructions declares a game-specific CPU output; no CPU family is inferred from Mini Micro’s host implementations.
- galactic-empire-minimicro-joestrout / Build (reviewed): No interpreter launch, execution, gameplay, dependency verification or byte comparison was performed. The author’s released browser build is not treated as local runtime verification.
- galactic-empire-minimicro-joestrout / Runtime profiles (no-evidence-found): The README requires Mini Micro but does not establish a minimum Mini Micro version, host CPU or RAM. Original Macintosh memory requirements belong to the historical source game, not a runtime minimum for this recreation, so runtime_profiles stays empty.
- galactic-empire-minimicro-joestrout / AI (no-evidence-found): The inspected README and MiniScript gameplay modules contain no explicit development-AI attribution. AI usage remains unknown; computational game rules and automated opponents would not themselves establish development assistance.

## Beast 1.0: 68000-to-Pascal reconstruction and native Swift port

Project ID: beast-mac-pascal-swift-reconstruction · Overall audit: partial

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
  "display_title": "Beast 1.0: 68000-to-Pascal reconstruction and native Swift port",
  "id": "beast-mac-pascal-swift-reconstruction",
  "last_activity": null,
  "last_checked": "2026-10-07",
  "re_started": null,
  "reconstructed_languages": [
    "Pascal",
    "Swift"
  ],
  "record_class": "subject",
  "repo": "https://github.com/RoyTinker/beasties-macos-port",
  "runtime_profiles": [
    {
      "evidence": [
        "https://github.com/RoyTinker/beasties-macos-port/blob/14b329202f25e01181c8d51b3ecb9d22682f0a17/port/Package.swift",
        "https://github.com/RoyTinker/beasties-macos-port/blob/14b329202f25e01181c8d51b3ecb9d22682f0a17/port/build-app.sh"
      ],
      "name": "Declared modern native output",
      "notes": "Swift tools 5.9 manifest; arm64 and x86_64 universal build. No independent run or numeric RAM floor established.",
      "os": "macOS 14 or later",
      "platform": "macOS"
    }
  ],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [
    "Pascal",
    "m68k assembly"
  ],
  "source_platforms": [
    "Macintosh"
  ],
  "status": "Annotated 68000 disassembly, reconstructed Pascal and Swift/AppKit game; port fidelity unverified",
  "subjects": [
    "Beast 1.0"
  ],
  "tags": [
    "source-reviewed",
    "macintosh-68k-discovery"
  ],
  "target_cpu": [
    "ARM64",
    "x86-64"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "macOS"
  ],
  "techniques": [],
  "title": "Beast 1.0",
  "tool_kinds": [],
  "types": [
    "Pascal reconstruction and Swift native port"
  ],
  "upstream_name": "beasties-macos-port",
  "work_kinds": [
    "disassembly",
    "decompilation",
    "reverse-engineering-derived-port"
  ]
}
```

### Identity (reviewed)

Preserves and reconstructs Chuck Shotton/BIAP Systems’ 1989 Beast 1.0. The game’s CODE resources, Pascal routines and Swift board logic are present, with movement, block pushing, enemy pursuit, win/loss and settings.
- https://github.com/roytinker/beasties-macos-port/blob/14b329202f25e01181c8d51b3ecb9d22682f0a17/README.md
- https://github.com/roytinker/beasties-macos-port/blob/14b329202f25e01181c8d51b3ecb9d22682f0a17/src/Beast.p
- https://github.com/roytinker/beasties-macos-port/blob/14b329202f25e01181c8d51b3ecb9d22682f0a17/port/Sources/BeastCore/BeastGame.swift

### Classification (reviewed)

Annotated 68000 disassembly was lifted into Pascal and translated routine by routine into Swift. The AppKit shell calls native game logic; its PICT interpreter decodes graphics commands, not CPU instructions or Macintosh hardware. Treat as binary-derived reconstruction and native port, not original-author source.
- https://github.com/roytinker/beasties-macos-port/blob/14b329202f25e01181c8d51b3ecb9d22682f0a17/disasm/CODE_2.s
- https://github.com/roytinker/beasties-macos-port/blob/14b329202f25e01181c8d51b3ecb9d22682f0a17/src/Beast.p
- https://github.com/roytinker/beasties-macos-port/blob/14b329202f25e01181c8d51b3ecb9d22682f0a17/port/Sources/BeastCore/BeastGame.swift
- https://github.com/roytinker/beasties-macos-port/blob/14b329202f25e01181c8d51b3ecb9d22682f0a17/port/Sources/Beast/PICT.swift
- https://github.com/roytinker/beasties-macos-port/blob/14b329202f25e01181c8d51b3ecb9d22682f0a17/port/Sources/Beast/AppDelegate.swift

### Source CPU (reviewed)

The CODE 2 listing contains Motorola address/data registers, 68000 opcodes and Macintosh A-line Toolbox traps. Reconstructed Pascal preserves CODE offsets and A5 globals. This establishes m68k input independently of a generic classic-Mac label.
- https://github.com/roytinker/beasties-macos-port/blob/14b329202f25e01181c8d51b3ecb9d22682f0a17/disasm/CODE_2.s
- https://github.com/roytinker/beasties-macos-port/blob/14b329202f25e01181c8d51b3ecb9d22682f0a17/src/Beast.p

### Target CPU (reviewed)

build-app.sh explicitly requests arm64 and x86_64 Swift builds. These are native modern Mac outputs; retained 68000 disassembly is an input artifact and does not imply a rebuilt classic-Mac target.
- https://github.com/roytinker/beasties-macos-port/blob/14b329202f25e01181c8d51b3ecb9d22682f0a17/port/build-app.sh
- https://github.com/roytinker/beasties-macos-port/blob/14b329202f25e01181c8d51b3ecb9d22682f0a17/port/Package.swift

### Build (reviewed)

SwiftPM defines BeastCore, the AppKit executable and a test target; the shell script packages resources and applies an ad-hoc signature. Original resource data and generated artwork are included. No Pascal rebuild recipe or complete-game equivalence test was established. Limitations: No game was compiled, launched, played, hardware-tested or byte-compared. All independent verification flags remain unknown.
- https://github.com/roytinker/beasties-macos-port/blob/14b329202f25e01181c8d51b3ecb9d22682f0a17/port/Package.swift
- https://github.com/roytinker/beasties-macos-port/blob/14b329202f25e01181c8d51b3ecb9d22682f0a17/port/build-app.sh
- https://github.com/roytinker/beasties-macos-port/blob/14b329202f25e01181c8d51b3ecb9d22682f0a17/src/Beast.p

### Runtime profiles (reviewed)

Package.swift declares macOS 14 and Swift tools 5.9. The native shell uses a 60 Hz timer and original-sized board coordinates. QDRandom explicitly has not been checked against a real ROM; documentation lists deliberate menu, storage, input, zoom and safety changes. No precise historic OS/RAM minimum is claimed.
- https://github.com/roytinker/beasties-macos-port/blob/14b329202f25e01181c8d51b3ecb9d22682f0a17/port/Package.swift
- https://github.com/roytinker/beasties-macos-port/blob/14b329202f25e01181c8d51b3ecb9d22682f0a17/port/Sources/Beast/AppDelegate.swift
- https://github.com/roytinker/beasties-macos-port/blob/14b329202f25e01181c8d51b3ecb9d22682f0a17/port/Sources/BeastCore/QDRandom.swift
- https://github.com/roytinker/beasties-macos-port/blob/14b329202f25e01181c8d51b3ecb9d22682f0a17/README.md

### AI (reviewed)

Actual implementation commit 8729de48 adds the Swift game, shell and build files and includes an explicit Claude coauthor trailer. Its model label is recorded only as an upstream attribution, not independent model-version verification. Nine available commit messages were inspected.
- https://github.com/roytinker/beasties-macos-port/blob/14b329202f25e01181c8d51b3ecb9d22682f0a17/README.md
- https://github.com/RoyTinker/beasties-macos-port/commit/8729de48e467dc2ac9460a11deca0911f4b8b752

### Relationships (reviewed)

One reconstruction lineage covers its disassembly, Pascal and Swift stages. No matching Beast lineage appears in the catalogue or prior-review union. The Swift port is MIT licensed, except original-derived Artwork.swift and AppIcon.icns; the original application, disassembly and art retain Chuck Shotton/BIAP rights.
- https://github.com/roytinker/beasties-macos-port/blob/14b329202f25e01181c8d51b3ecb9d22682f0a17/README.md
- https://github.com/roytinker/beasties-macos-port/blob/14b329202f25e01181c8d51b3ecb9d22682f0a17/port/LICENSE

## Megaroids: recovered Macintosh C and Swift remake

Project ID: megaroids-mac-swift-source-reconstruction · Overall audit: partial

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
  "display_title": "Megaroids: recovered Macintosh C and Swift remake",
  "id": "megaroids-mac-swift-source-reconstruction",
  "last_activity": null,
  "last_checked": "2026-10-07",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Swift"
  ],
  "record_class": "subject",
  "repo": "https://github.com/jraymonds86/Megaroids",
  "runtime_profiles": [
    {
      "evidence": [
        "https://github.com/jraymonds86/Megaroids/blob/79fa383912ee58aad8ee3d96d3a1bc6c8ef21a4d/Megaroids.xcodeproj/project.pbxproj",
        "https://github.com/jraymonds86/Megaroids/blob/79fa383912ee58aad8ee3d96d3a1bc6c8ef21a4d/README.md"
      ],
      "name": "Inspected modern application target",
      "notes": "Target settings override project-level 26.4 values. README gives inconsistent Xcode 16+ and 26.4.1+ guidance. No fixed output ISA or tested hardware minimum established.",
      "os": "macOS 26.0 target setting",
      "platform": "macOS"
    }
  ],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [
    "C",
    "m68k assembly"
  ],
  "source_platforms": [
    "Macintosh"
  ],
  "status": "Recovered source/data and Swift game implementation; deliberate gameplay/audio changes; build untested",
  "subjects": [
    "Megaroids"
  ],
  "tags": [
    "source-reviewed",
    "macintosh-68k-discovery"
  ],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "macOS"
  ],
  "techniques": [],
  "title": "Megaroids",
  "tool_kinds": [],
  "types": [
    "Historical C source recovery and Swift remake"
  ],
  "upstream_name": "Megaroids",
  "work_kinds": [
    "source-reconstruction",
    "translation"
  ]
}
```

### Identity (reviewed)

Reconstructs the Bunnells’ Megaroids from a historical book listing, corrected OCR and binary-extracted sprite data, then implements a modern Swift game. The README gives both 1984 and 1985 original dates; no exact original release date is selected here.
- https://github.com/jraymonds86/megaroids/blob/79fa383912ee58aad8ee3d96d3a1bc6c8ef21a4d/README.md
- https://github.com/jraymonds86/megaroids/blob/79fa383912ee58aad8ee3d96d3a1bc6c8ef21a4d/Megaroids.c
- https://github.com/jraymonds86/megaroids/blob/79fa383912ee58aad8ee3d96d3a1bc6c8ef21a4d/Megaroids/Game/GameEngine.swift

### Classification (reviewed)

Source-led recovery and translation rather than a general emulator. The recovered C contains Toolbox calls and hardware-oriented code; Swift GameEngine, Ship and SoundEngine implement game-state progression, motion and audio directly. Recovered Megaroids.c is an assembled reference, not an untouched original archive.
- https://github.com/jraymonds86/megaroids/blob/79fa383912ee58aad8ee3d96d3a1bc6c8ef21a4d/Megaroids.c
- https://github.com/jraymonds86/megaroids/blob/79fa383912ee58aad8ee3d96d3a1bc6c8ef21a4d/Megaroids/Game/GameEngine.swift
- https://github.com/jraymonds86/megaroids/blob/79fa383912ee58aad8ee3d96d3a1bc6c8ef21a4d/Megaroids/Game/Ship.swift
- https://github.com/jraymonds86/megaroids/blob/79fa383912ee58aad8ee3d96d3a1bc6c8ef21a4d/Megaroids/Audio/SoundEngine.swift

### Source CPU (reviewed)

The preserved C includes a 68000 compiler string, inline 68k operations, low-memory globals and original Macintosh framebuffer addresses. These establish the m68k Macintosh implementation, separate from the Swift host architecture.
- https://github.com/jraymonds86/megaroids/blob/79fa383912ee58aad8ee3d96d3a1bc6c8ef21a4d/Megaroids.c

### Target CPU (reviewed)

The Xcode project builds a macOS Swift application but does not pin an explicit output ISA in the inspected settings. Do not infer Apple silicon or Intel support from modern macOS alone; target_cpu is intentionally empty.
- https://github.com/jraymonds86/megaroids/blob/79fa383912ee58aad8ee3d96d3a1bc6c8ef21a4d/Megaroids.xcodeproj/project.pbxproj
- https://github.com/jraymonds86/megaroids/blob/79fa383912ee58aad8ee3d96d3a1bc6c8ef21a4d/Megaroids/Game/GameEngine.swift

### Build (reviewed)

An Xcode project and source/assets are present. A git-ignored project.xcconfig is a required base configuration and contains user-supplied signing/bundle settings; it must be supplied locally. The README’s Xcode 16+ heading conflicts with its later 26.4.1+ instruction. No exact compiler minimum is asserted. Limitations: No game was compiled, launched, played, hardware-tested or byte-compared. All independent verification flags remain unknown.
- https://github.com/jraymonds86/megaroids/blob/79fa383912ee58aad8ee3d96d3a1bc6c8ef21a4d/Megaroids.xcodeproj/project.pbxproj
- https://github.com/jraymonds86/megaroids/blob/79fa383912ee58aad8ee3d96d3a1bc6c8ef21a4d/.gitignore
- https://github.com/jraymonds86/megaroids/blob/79fa383912ee58aad8ee3d96d3a1bc6c8ef21a4d/README.md

### Runtime profiles (reviewed)

Application target deployment settings are macOS 26.0, overriding project-level 26.4 settings. The source runs a 60 Hz timer and original-resolution game model. It deliberately changes audio mixing, hyperspace behavior, friction and presentation, so advertised pixel fidelity is not treated as verified equivalence.
- https://github.com/jraymonds86/megaroids/blob/79fa383912ee58aad8ee3d96d3a1bc6c8ef21a4d/Megaroids.xcodeproj/project.pbxproj
- https://github.com/jraymonds86/megaroids/blob/79fa383912ee58aad8ee3d96d3a1bc6c8ef21a4d/Megaroids/Game/GameEngine.swift
- https://github.com/jraymonds86/megaroids/blob/79fa383912ee58aad8ee3d96d3a1bc6c8ef21a4d/Megaroids/Game/Ship.swift
- https://github.com/jraymonds86/megaroids/blob/79fa383912ee58aad8ee3d96d3a1bc6c8ef21a4d/Megaroids/Audio/SoundEngine.swift
- https://github.com/jraymonds86/megaroids/blob/79fa383912ee58aad8ee3d96d3a1bc6c8ef21a4d/README.md

### AI (reviewed)

README explicitly credits Claude Code for the Swift implementation and overall porting approach. That direct development disclosure supports AI usage; the .claude ignore entry is not used as evidence. Both available commit messages were also inspected.
- https://github.com/jraymonds86/megaroids/blob/79fa383912ee58aad8ee3d96d3a1bc6c8ef21a4d/README.md

### Relationships (reviewed)

Recovered C and Swift are one project lineage, with no Megaroids project found in the current catalogue/prior union. This does not duplicate other independent Asteroids-like games. No repository-wide license was found in the complete tree; the author reserves original game rights to the Bunnell family, so availability is not a blanket reuse grant.
- https://github.com/jraymonds86/megaroids/blob/79fa383912ee58aad8ee3d96d3a1bc6c8ef21a4d/README.md
- https://github.com/jraymonds86/megaroids/blob/79fa383912ee58aad8ee3d96d3a1bc6c8ef21a4d/Megaroids.c

## Missile: Robert Munafo’s original Macintosh Pascal source

Project ID: missile-macintosh-munafo-original-source · Overall audit: partial

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
  "display_title": "Missile: Robert Munafo’s original Macintosh Pascal source",
  "id": "missile-macintosh-munafo-original-source",
  "last_activity": null,
  "last_checked": "2026-10-07",
  "re_started": null,
  "reconstructed_languages": [],
  "record_class": "subject",
  "repo": "https://mrob.com/pub/source/missile.html",
  "runtime_profiles": [],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [
    "Pascal"
  ],
  "source_platforms": [
    "Macintosh"
  ],
  "status": "Author-published Pascal and resource listings; rebuild untested",
  "subjects": [
    "Missile",
    "Missile Command"
  ],
  "tags": [
    "source-reviewed",
    "macintosh-68k-discovery"
  ],
  "target_cpu": [
    "m68k"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Macintosh"
  ],
  "techniques": [],
  "title": "Missile",
  "tool_kinds": [],
  "types": [
    "Original-author Macintosh game source"
  ],
  "upstream_name": "Missile",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

Robert Munafo publishes his June 1984 Macintosh Missile Command implementation, with later revisions.
- https://mrob.com/pub/source/missile.html

### Classification (reviewed)

Original-author Pascal preservation: missile movement, fireballs, rounds, scoring and Toolbox UI are implemented.
- https://mrob.com/pub/source/missile.html

### Source CPU (reviewed)

Author identifies the original 128K Macintosh; m68k is inferred from that explicit machine target.
- https://mrob.com/pub/source/missile.html

### Target CPU (reviewed)

Historical Macintosh output remains m68k. Later PowerPC compatibility claims do not establish native PowerPC recompilation.
- https://mrob.com/pub/source/missile.html

### Build (reviewed)

Lisa Pascal source and resource definitions are published. Historical interface units and resource compilation remain required. Limitations: No game was compiled, launched, played, hardware-tested or byte-compared. All independent verification flags remain unknown.
- https://mrob.com/pub/source/missile.html

### Runtime profiles (reviewed)

Original 128K Macintosh compatibility is author-reported. Exact OS/RAM minima remain unspecified; source comments disclose missing sound and other features.
- https://mrob.com/pub/source/missile.html

### AI (no-evidence-found)

No development-AI attribution found on the inspected source page; non-use is not established.
- https://mrob.com/pub/source/missile.html

### Relationships (reviewed)

Independent Macintosh implementation, distinct from indexed Atari arcade disassembly. Source-specific GPL-2.0 notice applies; generic website footer licensing is separate.
- https://mrob.com/pub/source/missile.html

## Multi Pong: native Macintosh multi-window Pong

Project ID: multipong-native-mac68k-jcgraybill · Overall audit: partial

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
  "display_title": "Multi Pong: native Macintosh multi-window Pong",
  "id": "multipong-native-mac68k-jcgraybill",
  "last_activity": "2025-04-15",
  "last_checked": "2026-10-07",
  "re_started": null,
  "reconstructed_languages": [
    "C"
  ],
  "record_class": "subject",
  "repo": "https://github.com/jcgraybill/multipong",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Source reviewed; independent build and gameplay untested",
  "subjects": [
    "Multi Pong"
  ],
  "tags": [
    "source-reviewed",
    "macintosh-68k-discovery"
  ],
  "target_cpu": [
    "m68k"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Macintosh"
  ],
  "techniques": [],
  "title": "Multi Pong",
  "tool_kinds": [],
  "types": [
    "native homebrew game",
    "Pong-style game"
  ],
  "upstream_name": "multipong",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

The maintainer’s Multi Pong is a native multi-window Pong variant developed in a 68k Macintosh programming study group. The reviewed implementation contains moving balls, an opponent paddle, collision against visible regions of draggable windows, five difficulty choices, scoring and an end condition at seven points.
- https://github.com/jcgraybill/multipong/blob/5c69a8bfce75a7b62482ac622520fb882918c805/README.md
- https://github.com/jcgraybill/multipong/blob/5c69a8bfce75a7b62482ac622520fb882918c805/multipong.c

### Classification (reviewed)

Original source-level homebrew in C using Macintosh Toolbox windows, QuickDraw regions, menus and event handling. The user changes the playfield through actual Mac windows; this is an implemented game rather than a generic window shell. The linked browser edition is a delivery option, not evidence of a separate browser reimplementation.
- https://github.com/jcgraybill/multipong/blob/5c69a8bfce75a7b62482ac622520fb882918c805/multipong.c
- https://github.com/jcgraybill/multipong/blob/5c69a8bfce75a7b62482ac622520fb882918c805/README.md

### Source CPU (not-applicable)

No historical binary, machine-code input or recovered original Pong source is identified. This is new homebrew and does not establish a historical source CPU or source platform; those arrays are empty.
- https://github.com/jcgraybill/multipong/blob/5c69a8bfce75a7b62482ac622520fb882918c805/README.md
- https://github.com/jcgraybill/multipong/blob/5c69a8bfce75a7b62482ac622520fb882918c805/multipong.c

### Target CPU (reviewed)

README situates development specifically in the 68k Macintosh programming group and instructs building with THINK C 6.0; the source uses direct classic Toolbox/QuickDraw calls. Together these establish the intended m68k output. The generic Performa reference is not treated as proof of native PowerPC code generation.
- https://github.com/jcgraybill/multipong/blob/5c69a8bfce75a7b62482ac622520fb882918c805/README.md
- https://github.com/jcgraybill/multipong/blob/5c69a8bfce75a7b62482ac622520fb882918c805/multipong.c

### Build (reviewed)

README requires THINK C 6.0 and decoding/decompressing the supplied project and resource archives with StuffIt Expander. The complete tree includes the C implementation plus separate BinHex/StuffIt project and resource files. Those encoded artifacts were not unpacked, so project settings and resource-fork completeness remain unverified. Limitations: No dependency installation, game compilation, tests, launch, gameplay, hardware check or binary comparison was performed. All build-verification flags remain null.
- https://github.com/jcgraybill/multipong/blob/5c69a8bfce75a7b62482ac622520fb882918c805/README.md
- https://github.com/jcgraybill/multipong/blob/5c69a8bfce75a7b62482ac622520fb882918c805/multipong.c
- https://github.com/jcgraybill/multipong/blob/5c69a8bfce75a7b62482ac622520fb882918c805/Multi%20Pong.π.rsrc.sit.hqx
- https://github.com/jcgraybill/multipong/blob/5c69a8bfce75a7b62482ac622520fb882918c805/Multi%20Pong.π.sit.hqx

### Runtime profiles (no-evidence-found)

No exact minimum Macintosh model, OS release, RAM budget or CPU speed is stated in the inspected README/source. WaitNextEvent, menu/resource lookups and QuickDraw region behavior are required by the code, but they are not converted into an unsupported numeric hardware or OS floor.
- https://github.com/jcgraybill/multipong/blob/5c69a8bfce75a7b62482ac622520fb882918c805/README.md
- https://github.com/jcgraybill/multipong/blob/5c69a8bfce75a7b62482ac622520fb882918c805/multipong.c

### AI (no-evidence-found)

The inspected README and complete available 13-commit message history contain no explicit development-AI disclosure or assistant co-author trailer. This does not establish non-use; age, coding style and filenames are not AI evidence.
- https://github.com/jcgraybill/multipong/blob/5c69a8bfce75a7b62482ac622520fb882918c805/README.md
- https://github.com/jcgraybill/multipong/commit/5c69a8bfce75a7b62482ac622520fb882918c805

### Relationships (reviewed)

One coherent homebrew game, with its source and encoded project/resources retained at one root. The repository has an Apache-2.0 license. No matching Multi Pong source lineage was found in the catalogue or prior-review root union; the linked study group is development context, not another game identity.
- https://github.com/jcgraybill/multipong/blob/5c69a8bfce75a7b62482ac622520fb882918c805/README.md
- https://github.com/jcgraybill/multipong/blob/5c69a8bfce75a7b62482ac622520fb882918c805/LICENSE
- https://github.com/jcgraybill/multipong/blob/5c69a8bfce75a7b62482ac622520fb882918c805/multipong.c

## Battle Chess: Macintosh 68k recovery to native C/C++

Project ID: battlechess-macintosh-native-recompilation · Overall audit: partial

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
  "display_title": "Battle Chess: Macintosh 68k recovery to native C/C++",
  "id": "battlechess-macintosh-native-recompilation",
  "last_activity": "2026-10-06",
  "last_checked": "2026-10-07",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "C++"
  ],
  "record_class": "subject",
  "repo": "https://github.com/myaumura/BattleChess",
  "runtime_profiles": [],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [
    "m68k machine code"
  ],
  "source_platforms": [
    "Macintosh"
  ],
  "status": "Substantial native game recovery; external data/extraction tooling required and original parity incomplete",
  "subjects": [
    "Battle Chess"
  ],
  "tags": [
    "source-reviewed",
    "macintosh-68k-discovery"
  ],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "macOS",
    "Linux"
  ],
  "techniques": [],
  "title": "Battle Chess",
  "tool_kinds": [],
  "types": [
    "native recompilation",
    "game reconstruction"
  ],
  "upstream_name": "BattleChess",
  "work_kinds": [
    "binary-analysis",
    "reverse-engineering-derived-port"
  ]
}
```

### Identity (reviewed)

Unofficial native recompilation of Macintosh Battle Chess. docs/DATA.md identifies the exact recovery baseline as MacPlay Battle Chess 1.0.2, with an embedded 1988–93 Interplay notice; the general 1991 release label does not date that exact binary. Reviewed code includes legal moves, piece lists, saves, animation sequencing, game sessions and native UI.
- https://github.com/myaumura/battlechess/blob/fc9211d7e6a5409f8d01d35cd018494d76ca9d0d/README.md
- https://github.com/myaumura/battlechess/blob/fc9211d7e6a5409f8d01d35cd018494d76ca9d0d/docs/DATA.md
- https://github.com/myaumura/battlechess/blob/fc9211d7e6a5409f8d01d35cd018494d76ca9d0d/lib/recovered_core.c
- https://github.com/myaumura/battlechess/blob/fc9211d7e6a5409f8d01d35cd018494d76ca9d0d/lib/Game.c

### Classification (reviewed)

Binary-derived recovery into a C11 engine and C++17/SDL3 host, explicitly not a clean-room project. recovered_core.c translates original file-offset routines into host-valued structs rather than a mapped 68k memory image; animation.c retains original routine provenance beside native helpers, while QuickDrawControl.cpp recreates controls through SDL. No guest-CPU interpreter is in these inspected game/host paths.
- https://github.com/myaumura/battlechess/blob/fc9211d7e6a5409f8d01d35cd018494d76ca9d0d/README.md
- https://github.com/myaumura/battlechess/blob/fc9211d7e6a5409f8d01d35cd018494d76ca9d0d/lib/recovered_core.c
- https://github.com/myaumura/battlechess/blob/fc9211d7e6a5409f8d01d35cd018494d76ca9d0d/lib/animation.c
- https://github.com/myaumura/battlechess/blob/fc9211d7e6a5409f8d01d35cd018494d76ca9d0d/src/QuickDrawControl.cpp
- https://github.com/myaumura/battlechess/blob/fc9211d7e6a5409f8d01d35cd018494d76ca9d0d/config/build.cmake

### Source CPU (reviewed)

README and the data contract explicitly identify Motorola 68k Macintosh as the original recovered executable. The source preserves A5-global and original file-offset provenance. No later PowerPC source release is claimed or inferred.
- https://github.com/myaumura/battlechess/blob/fc9211d7e6a5409f8d01d35cd018494d76ca9d0d/README.md
- https://github.com/myaumura/battlechess/blob/fc9211d7e6a5409f8d01d35cd018494d76ca9d0d/docs/DATA.md
- https://github.com/myaumura/battlechess/blob/fc9211d7e6a5409f8d01d35cd018494d76ca9d0d/lib/recovered_core.c

### Target CPU (reviewed)

Build instructions use the compiler’s normal host architecture on modern macOS/Linux; CMake declares C11/C++17 and SDL3 without a fixed ISA. The modern native output is therefore not recorded as m68k or as a guessed x86/ARM family.
- https://github.com/myaumura/battlechess/blob/fc9211d7e6a5409f8d01d35cd018494d76ca9d0d/docs/BUILD.md
- https://github.com/myaumura/battlechess/blob/fc9211d7e6a5409f8d01d35cd018494d76ca9d0d/config/build.cmake

### Build (reviewed)

CMake 3.20 and C11/C++17 build a source-only core by default; the application additionally needs SDL3 3.4 and a matching external prepared data pack. CMake checks for generated catalogs, animation pixels, a 32,000-byte opening book and assets. The repository intentionally omits original resources and the extraction scripts needed to create the pack. Upstream dated test and playability claims are reported separately from verification here. Limitations: No dependency installation, game compilation, tests, launch, gameplay, hardware check or binary comparison was performed. All build-verification flags remain null. Original idle-animation triggering, timing/audio, computer choices, save exchange and modem interoperability remain incomplete or unverified upstream.
- https://github.com/myaumura/battlechess/blob/fc9211d7e6a5409f8d01d35cd018494d76ca9d0d/README.md
- https://github.com/myaumura/battlechess/blob/fc9211d7e6a5409f8d01d35cd018494d76ca9d0d/docs/DATA.md
- https://github.com/myaumura/battlechess/blob/fc9211d7e6a5409f8d01d35cd018494d76ca9d0d/docs/BUILD.md
- https://github.com/myaumura/battlechess/blob/fc9211d7e6a5409f8d01d35cd018494d76ca9d0d/config/build.cmake

### Runtime profiles (no-evidence-found)

The application needs a desktop video/audio environment supported by SDL3 and the matching external data pack. No exact minimum CPU, RAM, macOS version or Linux distribution is established. Original Macintosh source architecture and dummy-driver smoke tests are not host runtime minima.
- https://github.com/myaumura/battlechess/blob/fc9211d7e6a5409f8d01d35cd018494d76ca9d0d/docs/BUILD.md
- https://github.com/myaumura/battlechess/blob/fc9211d7e6a5409f8d01d35cd018494d76ca9d0d/docs/ROADMAP.md

### AI (no-evidence-found)

The inspected README and complete available 11-commit message history contain no explicit development-AI disclosure or assistant co-author trailer. This does not establish non-use; age, coding style and filenames are not AI evidence. Limitations: NOTICE describes the icon as generated artwork but does not name an AI system; its linked resources/ICON.md is absent from the pinned tree. Neither that wording nor a filename establishes development-AI usage.
- https://github.com/myaumura/battlechess/blob/fc9211d7e6a5409f8d01d35cd018494d76ca9d0d/README.md
- https://github.com/myaumura/BattleChess/commit/fc9211d7e6a5409f8d01d35cd018494d76ca9d0d

### Relationships (reviewed)

The inspected root is a distinct Macintosh recovery, not a clone of an existing Battle Chess catalogue record. MIT covers contributions only to the extent contributors can license them; NOTICE excludes original code/data, Apple fonts and other third-party material. Screenshots contain original artwork, while required data and the separate recovery workspace are not distributed. No public URL for the omitted extraction toolchain is supplied in the inspected data contract.
- https://github.com/myaumura/battlechess/blob/fc9211d7e6a5409f8d01d35cd018494d76ca9d0d/README.md
- https://github.com/myaumura/battlechess/blob/fc9211d7e6a5409f8d01d35cd018494d76ca9d0d/NOTICE
- https://github.com/myaumura/battlechess/blob/fc9211d7e6a5409f8d01d35cd018494d76ca9d0d/LICENSE
- https://github.com/myaumura/battlechess/blob/fc9211d7e6a5409f8d01d35cd018494d76ca9d0d/docs/DATA.md

## 3Tris: HTML5 recreation of the Macintosh 68k puzzle game

Project ID: 3tris-html5-francescom · Overall audit: partial

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
  "display_title": "3Tris: HTML5 recreation of the Macintosh 68k puzzle game",
  "id": "3tris-html5-francescom",
  "last_activity": "2022-02-24",
  "last_checked": "2026-10-07",
  "re_started": null,
  "reconstructed_languages": [
    "JavaScript"
  ],
  "record_class": "subject",
  "repo": "https://github.com/francescom/3Tris",
  "runtime_profiles": [
    {
      "evidence": [
        "https://github.com/francescom/3Tris/blob/3b991a89dcb435d5333ec842e01f107424686a28/README.md",
        "https://github.com/francescom/3Tris/blob/3b991a89dcb435d5333ec842e01f107424686a28/index.html"
      ],
      "name": "Documented HTML5 browser edition",
      "notes": "Historical author claims include IE9+, Firefox, Chrome, Safari and iOS devices; Android explicitly untested. No current browser or hardware minimum independently verified.",
      "platform": "Web browser"
    }
  ],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [],
  "source_platforms": [
    "Macintosh"
  ],
  "status": "HTML5/JavaScript game source and media; documented polygon-depth bug; runtime untested",
  "subjects": [
    "3Tris"
  ],
  "tags": [
    "source-reviewed",
    "macintosh-68k-discovery"
  ],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Web browser"
  ],
  "techniques": [],
  "title": "3Tris",
  "tool_kinds": [],
  "types": [
    "browser remake",
    "3D puzzle-game reimplementation"
  ],
  "upstream_name": "3Tris",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

The maintainer identifies this as HTML5 3Tris and explicitly links its original Macintosh 68K predecessor. The implemented JavaScript game includes a 3D block grid, eight shape types, timed descent, rotations, placement collision, filled-plane clearing, score/level progression and game over, with separate device-oriented pages.
- https://github.com/francescom/3tris/blob/3b991a89dcb435d5333ec842e01f107424686a28/README.md
- https://github.com/francescom/3tris/blob/3b991a89dcb435d5333ec842e01f107424686a28/jsinc/3tris.js
- https://github.com/francescom/3tris/blob/3b991a89dcb435d5333ec842e01f107424686a28/index.html

### Classification (reviewed)

A browser JavaScript recreation with its own Canvas/3D rendering and input code. The inspected gameplay uses direct grid and shape logic, not emulation of Macintosh CPU or Toolbox calls. No binary-derived recovery method or original source translation is asserted.
- https://github.com/francescom/3tris/blob/3b991a89dcb435d5333ec842e01f107424686a28/jsinc/3tris.js
- https://github.com/francescom/3tris/blob/3b991a89dcb435d5333ec842e01f107424686a28/jsinc/3tris_draw.js
- https://github.com/francescom/3tris/blob/3b991a89dcb435d5333ec842e01f107424686a28/jsinc/js_3d_engine.js
- https://github.com/francescom/3tris/blob/3b991a89dcb435d5333ec842e01f107424686a28/fast.html

### Source CPU (reviewed)

README explicitly calls the predecessor a Macintosh 68K game, establishing m68k historical ancestry. No original binary was inspected and no more precise 680x0 minimum or PowerPC edition is inferred. The README’s broad decade wording is not used as an exact release date.
- https://github.com/francescom/3tris/blob/3b991a89dcb435d5333ec842e01f107424686a28/README.md

### Target CPU (reviewed)

The output is HTML5/JavaScript executed by a browser. The inspected pages load local scripts and media; they do not establish a native output ISA. The historical m68k ancestry is not copied into target_cpu.
- https://github.com/francescom/3tris/blob/3b991a89dcb435d5333ec842e01f107424686a28/index.html
- https://github.com/francescom/3tris/blob/3b991a89dcb435d5333ec842e01f107424686a28/fast.html
- https://github.com/francescom/3tris/blob/3b991a89dcb435d5333ec842e01f107424686a28/jsinc/3tris.js

### Build (reviewed)

The tree provides directly served HTML/JavaScript, Canvas support code, audio in Ogg/MP3, image assets and a PHP endpoint serving the application-cache manifest; no transpiler or package-managed build is specified. README explicitly notes an unresolved polygon-distance visualization bug and says Android was untested. The current behavior of obsolete app-cache/browser paths has not been checked. Limitations: No dependency installation, game compilation, tests, launch, gameplay, hardware check or binary comparison was performed. All build-verification flags remain null.
- https://github.com/francescom/3tris/blob/3b991a89dcb435d5333ec842e01f107424686a28/README.md
- https://github.com/francescom/3tris/blob/3b991a89dcb435d5333ec842e01f107424686a28/index.html
- https://github.com/francescom/3tris/blob/3b991a89dcb435d5333ec842e01f107424686a28/fast.html
- https://github.com/francescom/3tris/blob/3b991a89dcb435d5333ec842e01f107424686a28/manifest.php
- https://github.com/francescom/3tris/blob/3b991a89dcb435d5333ec842e01f107424686a28/jsinc/scoresaver.js

### Runtime profiles (reviewed)

README lists iPhone/iPod/iPad, IE9, Firefox, Chrome and Safari compatibility, while index.html requires an HTML5-capable browser and excludes Internet Explorer below 9. These are historical author claims, with no current-version test, hardware floor or numeric RAM minimum.
- https://github.com/francescom/3tris/blob/3b991a89dcb435d5333ec842e01f107424686a28/README.md
- https://github.com/francescom/3tris/blob/3b991a89dcb435d5333ec842e01f107424686a28/index.html

### AI (no-evidence-found)

The inspected README and complete available 7-commit message history contain no explicit development-AI disclosure or assistant co-author trailer. This does not establish non-use; age, coding style and filenames are not AI evidence.
- https://github.com/francescom/3tris/blob/3b991a89dcb435d5333ec842e01f107424686a28/README.md
- https://github.com/francescom/3Tris/commit/3b991a89dcb435d5333ec842e01f107424686a28

### Relationships (reviewed)

A single browser game with fast/slow/iOS layouts, not separate implementations per page. It has no root LICENSE; index.html says source may be used by anyone, which is an informal source-use statement rather than a standard license or established grant for every bundled sound/image. No matching root or 3Tris lineage was found in the current catalogue/prior-review union. The original-author website link could not be fetched, so authorship beyond the repository’s primary description is not assumed.
- https://github.com/francescom/3tris/blob/3b991a89dcb435d5333ec842e01f107424686a28/README.md
- https://github.com/francescom/3tris/blob/3b991a89dcb435d5333ec842e01f107424686a28/index.html

## Wolfenstein 3D: original Macintosh 68k/PowerPC source archive

Project ID: wolf3d-mac-original-source-archive · Overall audit: partial

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
  "display_title": "Wolfenstein 3D: original Macintosh 68k/PowerPC source archive",
  "id": "wolf3d-mac-original-source-archive",
  "last_activity": "2013-12-20",
  "last_checked": "2026-10-07",
  "re_started": null,
  "reconstructed_languages": [],
  "record_class": "subject",
  "repo": "https://github.com/Blzut3/Wolf3D-Mac",
  "runtime_profiles": [
    {
      "cpu_family": "m68k",
      "evidence": [
        "https://github.com/Blzut3/Wolf3D-Mac/blob/4ff692cf2a71f10cefc467e83c910399890747a4/Mac.c",
        "https://github.com/Blzut3/Wolf3D-Mac/blob/4ff692cf2a71f10cefc467e83c910399890747a4/Wolf.h"
      ],
      "name": "Preserved Macintosh 68k initialization requirements",
      "notes": "Source requires 32-bit Color QuickDraw and 8-bit display at least 512×384; no minimum CPU model or RAM inferred from architecture or warning cases. Requirements are code-derived, not runtime-tested.",
      "os": "System 6.0.7 or later",
      "platform": "Macintosh"
    }
  ],
  "source_cpu": [
    "m68k",
    "PowerPC"
  ],
  "source_language": [
    "C",
    "m68k assembly",
    "PowerPC assembly"
  ],
  "source_platforms": [
    "Macintosh"
  ],
  "status": "Archived original Macintosh source release; legacy project/resources and rebuild unverified",
  "subjects": [
    "Wolfenstein 3D"
  ],
  "tags": [
    "source-reviewed",
    "macintosh-68k-discovery"
  ],
  "target_cpu": [
    "m68k",
    "PowerPC"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Macintosh"
  ],
  "techniques": [],
  "title": "Wolfenstein 3D",
  "tool_kinds": [],
  "types": [
    "original-source archive"
  ],
  "upstream_name": "Wolf3D-Mac",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

Preservation mirror of the original Macintosh Wolfenstein 3D First/Second Encounter source release, attributed in the preserved release note to Bill Heineman and Chris DeSalvo. The note dates the Macintosh commercial release to October 1994 and the source-release account to January 2000; the GitHub root itself is a later third-party archive. WolfMain.c implements the level/game loop, player/enemy/projectile movement and game progression.
- https://github.com/blzut3/wolf3d-mac/blob/4ff692cf2a71f10cefc467e83c910399890747a4/ReadMe.txt
- https://github.com/blzut3/wolf3d-mac/blob/4ff692cf2a71f10cefc467e83c910399890747a4/WolfMain.c
- https://github.com/blzut3/wolf3d-mac/blob/4ff692cf2a71f10cefc467e83c910399890747a4/PlMove.c

### Classification (reviewed)

Historical original-source preservation with native Macintosh Toolbox support, C gameplay and separate 68k/PPC assembly renderers. The preserved note says this Mac version descends from the SNES adaptation and uses BSP rendering, so it is not collapsed into the tracker’s DOS-derived Wolf ports merely by title. No new decompilation is claimed.
- https://github.com/blzut3/wolf3d-mac/blob/4ff692cf2a71f10cefc467e83c910399890747a4/ReadMe.txt
- https://github.com/blzut3/wolf3d-mac/blob/4ff692cf2a71f10cefc467e83c910399890747a4/WolfMain.c
- https://github.com/blzut3/wolf3d-mac/blob/4ff692cf2a71f10cefc467e83c910399890747a4/RefBsp.c
- https://github.com/blzut3/wolf3d-mac/blob/4ff692cf2a71f10cefc467e83c910399890747a4/Wolf.68k
- https://github.com/blzut3/wolf3d-mac/blob/4ff692cf2a71f10cefc467e83c910399890747a4/Wolf.ppc
- https://github.com/Blzut3/Wolf3D-Mac/blob/4ff692cf2a71f10cefc467e83c910399890747a4/Mac.c

### Source CPU (reviewed)

The release note explicitly distinguishes Macintosh 68000 and PowerPC editions. Wolf.68k contains D/A registers, MOVEM/MOVE/ADDX/DBF instructions, and Wolf.ppc contains PowerPC register, TOC and code-section conventions. These independently establish both source families; the SNES ancestry does not become a claimed source binary platform for this Mac archive.
- https://github.com/blzut3/wolf3d-mac/blob/4ff692cf2a71f10cefc467e83c910399890747a4/ReadMe.txt
- https://github.com/blzut3/wolf3d-mac/blob/4ff692cf2a71f10cefc467e83c910399890747a4/Wolf.68k
- https://github.com/blzut3/wolf3d-mac/blob/4ff692cf2a71f10cefc467e83c910399890747a4/Wolf.ppc

### Target CPU (reviewed)

The archive retains distinct native 68k and PowerPC renderer paths and a CodeWarrior project. Both architectures describe preserved original outputs, not modern host targets or verified successful rebuilds. README’s historical runtime-generated-scaler description is not copied as current behavior: Wolf.68k explicitly records a revision to tight loops, and current SetupScalers68k.c builds a reciprocal table with a disabled older ScaleGlue call path.
- https://github.com/blzut3/wolf3d-mac/blob/4ff692cf2a71f10cefc467e83c910399890747a4/Wolf.68k
- https://github.com/blzut3/wolf3d-mac/blob/4ff692cf2a71f10cefc467e83c910399890747a4/Wolf.ppc
- https://github.com/blzut3/wolf3d-mac/blob/4ff692cf2a71f10cefc467e83c910399890747a4/SetupScalers68k.c
- https://github.com/blzut3/wolf3d-mac/blob/4ff692cf2a71f10cefc467e83c910399890747a4/SetupScalersPPC.c
- https://github.com/blzut3/wolf3d-mac/blob/4ff692cf2a71f10cefc467e83c910399890747a4/ReadMe.txt

### Build (reviewed)

The source-release note says the project was updated from CodeWarrior DR/4 to Pro 5. The tree contains Wolf3D.mcp, assembly/object artifacts and separate proprietary music libraries, but no complete game resource/asset pack or reproducible modern recipe. Source still uses resource IDs and GetResource/LoadAResource calls. Project-file strings name both MacOS 68K/PPC linkers and legacy libraries; they do not prove all dependencies are present. Limitations: No dependency installation, game compilation, tests, launch, gameplay, hardware check or binary comparison was performed. All build-verification flags remain null. README’s original author build claim is historical and does not verify this mirror.
- https://github.com/blzut3/wolf3d-mac/blob/4ff692cf2a71f10cefc467e83c910399890747a4/ReadMe.txt
- https://github.com/blzut3/wolf3d-mac/blob/4ff692cf2a71f10cefc467e83c910399890747a4/Wolf.h
- https://github.com/blzut3/wolf3d-mac/blob/4ff692cf2a71f10cefc467e83c910399890747a4/SetupScalers68k.c
- https://github.com/Blzut3/Wolf3D-Mac/blob/4ff692cf2a71f10cefc467e83c910399890747a4/Wolf3D.mcp
- https://github.com/Blzut3/Wolf3D-Mac/blob/4ff692cf2a71f10cefc467e83c910399890747a4/Mac.c

### Runtime profiles (reviewed)

Mac.c’s 68k initialization explicitly rejects systems before 6.0.7, requires 32-bit Color QuickDraw, and selects an 8-bit monitor at least 512×384. Its 68000/68020/68030 cases display speed warnings rather than a reliable universal minimum-CPU rule. The PowerPC branch skips the OS gate with a 7.1 comment; no independently established PPC minimum or numeric RAM requirement is asserted.
- https://github.com/blzut3/wolf3d-mac/blob/4ff692cf2a71f10cefc467e83c910399890747a4/Wolf.h
- https://github.com/Blzut3/Wolf3D-Mac/blob/4ff692cf2a71f10cefc467e83c910399890747a4/Mac.c

### AI (no-evidence-found)

The inspected README and complete available 1-commit message history contain no explicit development-AI disclosure or assistant co-author trailer. This does not establish non-use; age, coding style and filenames are not AI evidence.
- https://github.com/blzut3/wolf3d-mac/blob/4ff692cf2a71f10cefc467e83c910399890747a4/ReadMe.txt
- https://github.com/Blzut3/Wolf3D-Mac/commit/4ff692cf2a71f10cefc467e83c910399890747a4

### Relationships (reviewed)

One archived mirror of the original Mac source lineage, counted once. Existing records were compared without re-researching their roots: earok/AkikoWolf credits AWolf/PSP/id DOS source, agranlund/wolf derives from Wolf4SDL/id, and kweepa/wolf64 is a C64 assembly raycaster. In contrast, this preserved author note explicitly identifies a SNES-derived implementation rather than the PC version, with BSP visibility; RefBsp.c and separate Mac renderer paths corroborate material implementation differences, not merely a new target platform. No matching Blzut3/Heineman/Burger Mac source root appears in the complete prior-review union. No general root license is supplied; the release note expressly reserves Steve Hales/Jim Nitchals music-driver rights and requires separate permission for reuse. Public source availability is not treated as an unrestricted redistribution grant.
- https://github.com/blzut3/wolf3d-mac/blob/4ff692cf2a71f10cefc467e83c910399890747a4/ReadMe.txt
- https://github.com/blzut3/wolf3d-mac/blob/4ff692cf2a71f10cefc467e83c910399890747a4/WolfMain.c
- https://github.com/blzut3/wolf3d-mac/blob/4ff692cf2a71f10cefc467e83c910399890747a4/Wolf.68k
- https://github.com/blzut3/wolf3d-mac/blob/4ff692cf2a71f10cefc467e83c910399890747a4/RefBsp.c

## Sparks — original classic Macintosh game restoration

Project ID: sparks-classic-mac-restoration-depp · Overall audit: partial

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
  "display_title": "Sparks — original classic Macintosh game restoration",
  "id": "sparks-classic-mac-restoration-depp",
  "last_activity": "2021-03-25",
  "last_checked": "2026-10-07",
  "re_started": null,
  "reconstructed_languages": [
    "C++"
  ],
  "record_class": "subject",
  "repo": "https://github.com/depp/sparks",
  "runtime_profiles": [],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [
    "C++"
  ],
  "source_platforms": [
    "Macintosh"
  ],
  "status": "Unfinished original game restoration; static review only",
  "subjects": [
    "Sparks"
  ],
  "tags": [
    "Macintosh",
    "68k ancestry",
    "static review"
  ],
  "target_cpu": [
    "m68k",
    "PowerPC"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Macintosh"
  ],
  "techniques": [],
  "title": "Sparks — original classic Macintosh game restoration",
  "tool_kinds": [],
  "types": [
    "original-source restoration",
    "unfinished game prototype"
  ],
  "upstream_name": "Sparks",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

The author identifies Sparks as the beginnings of a Macintosh game written around 2000 and this repository as an attempt to get its original classic Macintosh code running. The pinned tree contains the game loop, entity, player, star-field, renderer and resource source, rather than only an announcement.
- https://github.com/depp/sparks/blob/61a6865733af34949fd912217d7a5441ccce93cd/README.md
- https://github.com/depp/sparks/blob/61a6865733af34949fd912217d7a5441ccce93cd/Main.cpp

### Classification (reviewed)

Original-source restoration of an unfinished game prototype. Main.cpp initializes the classic Toolbox and drives Game_RunFrame; this is neither a binary decompilation nor a modern independent remake. The README explicitly declines to characterize the historical work as a finished game.
- https://github.com/depp/sparks/blob/61a6865733af34949fd912217d7a5441ccce93cd/README.md
- https://github.com/depp/sparks/blob/61a6865733af34949fd912217d7a5441ccce93cd/Main.cpp

### Source CPU (reviewed)

The preserved original Macintosh C++ tree has separate 68K object rules, CPlusOptions-68K with the near model, 68K runtime libraries and a Sparks.68k link target. Together with the author’s original-code statement, this directly establishes m68k source provenance rather than inferring it from the approximate date.
- https://github.com/depp/sparks/blob/61a6865733af34949fd912217d7a5441ccce93cd/README.md
- https://github.com/depp/sparks/blob/61a6865733af34949fd912217d7a5441ccce93cd/Makefile

### Target CPU (reviewed)

The MPW makefile explicitly targets both Sparks.68k through ILink and Sparks.ppc through PPCLink. These are documented build targets; successful output was not established.
- https://github.com/depp/sparks/blob/61a6865733af34949fd912217d7a5441ccce93cd/Makefile

### Build (reviewed)

Inspected the MPW makefile, classic Toolbox bootstrap and complete tree inventory. The build requires the historical CPlus/PPCCPlus, ILink/PPCLink and Rez tools and classic Macintosh libraries; Resources.r and Resources.rsrc are present. No root license grant was found in the tree or README. The project remains explicitly unfinished. Limitations: No compilation, tests, execution, gameplay or binary comparison was performed. All build booleans remain null.
- https://github.com/depp/sparks/blob/61a6865733af34949fd912217d7a5441ccce93cd/Makefile
- https://github.com/depp/sparks/blob/61a6865733af34949fd912217d7a5441ccce93cd/Main.cpp
- https://github.com/depp/sparks/blob/61a6865733af34949fd912217d7a5441ccce93cd/README.md

### Runtime profiles (no-evidence-found)

Main.cpp tests Color QuickDraw availability and an 8-bit display mode, then allocates a GWorld backbuffer. These are implementation requirements, but the inspected material supplies no authoritative minimum CPU model or RAM for a usable game; no runnable hardware profile is asserted.
- https://github.com/depp/sparks/blob/61a6865733af34949fd912217d7a5441ccce93cd/Main.cpp

### AI (no-evidence-found)

The inspected README and original-code/bootstrap material contain no explicit development-AI disclosure. This is a bounded negative search, not evidence of non-use; usage remains unknown.
- https://github.com/depp/sparks/blob/61a6865733af34949fd912217d7a5441ccce93cd/README.md
- https://github.com/depp/sparks/blob/61a6865733af34949fd912217d7a5441ccce93cd/Main.cpp

### Relationships (reviewed)

The README mentions another copy in /game/space without identifying a repository. This record covers the author’s Sparks restoration root once; that undeclared copy is not promoted separately. The root was absent from the current catalogue and prior-review/source/decision root index. Limitations: The other copy’s provenance and current location remain unresolved.
- https://github.com/depp/sparks/blob/61a6865733af34949fd912217d7a5441ccce93cd/README.md

## Galactic Empire — Mini Micro recreation

Project ID: galactic-empire-minimicro-joestrout · Overall audit: partial

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
  "display_title": "Galactic Empire — Mini Micro recreation",
  "id": "galactic-empire-minimicro-joestrout",
  "last_activity": "2025-05-27",
  "last_checked": "2026-10-07",
  "re_started": null,
  "reconstructed_languages": [
    "MiniScript"
  ],
  "record_class": "subject",
  "repo": "https://github.com/JoeStrout/galactic-empire",
  "runtime_profiles": [],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [],
  "source_platforms": [
    "Macintosh"
  ],
  "status": "Recreation and extension with source and assets; static review only",
  "subjects": [
    "Galactic Empire (Cary Torkelson)"
  ],
  "tags": [
    "Macintosh",
    "68k ancestry",
    "static review"
  ],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Mini Micro",
    "Web browser"
  ],
  "techniques": [],
  "title": "Galactic Empire — Mini Micro recreation",
  "tool_kinds": [],
  "types": [
    "game remake"
  ],
  "upstream_name": "Galactic Empire",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

README identifies an open-source recreation/extension of Cary Torkelson’s Mac shareware game, with explicit instructions for playing the original. The repository preserves reference screenshots and original help alongside a separate MiniScript implementation.
- https://github.com/joestrout/galactic-empire/blob/1517e2a827e4889f2e86a7ffa1c35e39fcc19452/README.md
- https://github.com/joestrout/galactic-empire/blob/1517e2a827e4889f2e86a7ffa1c35e39fcc19452/main.ms
- https://github.com/JoeStrout/galactic-empire/blob/1517e2a827e4889f2e86a7ffa1c35e39fcc19452/reference/GE-Help.text

### Classification (reviewed)

Independent MiniScript recreation/extension. main.ms implements the 20-planet galaxy, fleet travel, spying, combat/occupation, resources and the 1200-year win/loss deadline; gameRules.ms provides technology-dependent combat and force-generation rules. This is concrete gameplay source, not a description-only or emulator-wrapper listing.
- https://github.com/joestrout/galactic-empire/blob/1517e2a827e4889f2e86a7ffa1c35e39fcc19452/main.ms
- https://github.com/joestrout/galactic-empire/blob/1517e2a827e4889f2e86a7ffa1c35e39fcc19452/gameRules.ms

### Source CPU (reviewed)

The preserved original GE-Help.text explicitly supports digitized sound on System 6.0.2 and later and color graphics on System 6.0.4 with Color QuickDraw, plus a 320K monochrome allocation. m68k ancestry is inferred from those original System 6 execution requirements, which predate PowerPC support, rather than from a generic classic-Mac label. Limitations: The original help is MacRoman and was retrieved as exact base64 bytes, decoded only for static reading and Git-blob verified against the pinned tree. It is cited as a binary/non-UTF-8 file instead of falsely re-encoding it in the UTF-8 proof cache.
- https://github.com/joestrout/galactic-empire/blob/1517e2a827e4889f2e86a7ffa1c35e39fcc19452/README.md
- https://github.com/JoeStrout/galactic-empire/blob/1517e2a827e4889f2e86a7ffa1c35e39fcc19452/reference/GE-Help.text

### Target CPU (no-evidence-found)

The README targets the Mini Micro interpreter and the author distributes an HTML5 build. Neither the MiniScript game nor the inspected instructions declares a game-specific CPU output; no CPU family is inferred from Mini Micro’s host implementations.
- https://github.com/joestrout/galactic-empire/blob/1517e2a827e4889f2e86a7ffa1c35e39fcc19452/README.md
- https://github.com/joestrout/galactic-empire/blob/1517e2a827e4889f2e86a7ffa1c35e39fcc19452/main.ms
- https://joestrout.itch.io/galactic-empire

### Build (reviewed)

The documented path mounts the repository in Mini Micro and loads/runs main. Source, PNG artwork, resource/sound modules and original-reference material are present. main.ms imports Mini Micro/system helper modules; the project is not standalone without that environment. The pinned LICENSE is the Unlicense/public-domain dedication for the remake; original reference-game rights are separate. Inspected game source; some actions deliberately use simplified fixed quantities, consistent with recreation/extension rather than binary fidelity. Limitations: No interpreter launch, execution, gameplay, dependency verification or byte comparison was performed. The author’s released browser build is not treated as local runtime verification.
- https://github.com/joestrout/galactic-empire/blob/1517e2a827e4889f2e86a7ffa1c35e39fcc19452/README.md
- https://github.com/joestrout/galactic-empire/blob/1517e2a827e4889f2e86a7ffa1c35e39fcc19452/LICENSE
- https://github.com/joestrout/galactic-empire/blob/1517e2a827e4889f2e86a7ffa1c35e39fcc19452/main.ms
- https://github.com/joestrout/galactic-empire/blob/1517e2a827e4889f2e86a7ffa1c35e39fcc19452/gameRules.ms

### Runtime profiles (no-evidence-found)

The README requires Mini Micro but does not establish a minimum Mini Micro version, host CPU or RAM. Original Macintosh memory requirements belong to the historical source game, not a runtime minimum for this recreation, so runtime_profiles stays empty.
- https://github.com/joestrout/galactic-empire/blob/1517e2a827e4889f2e86a7ffa1c35e39fcc19452/README.md
- https://github.com/JoeStrout/galactic-empire/blob/1517e2a827e4889f2e86a7ffa1c35e39fcc19452/reference/GE-Help.text

### AI (no-evidence-found)

The inspected README and MiniScript gameplay modules contain no explicit development-AI attribution. AI usage remains unknown; computational game rules and automated opponents would not themselves establish development assistance.
- https://github.com/joestrout/galactic-empire/blob/1517e2a827e4889f2e86a7ffa1c35e39fcc19452/README.md
- https://github.com/joestrout/galactic-empire/blob/1517e2a827e4889f2e86a7ffa1c35e39fcc19452/main.ms
- https://github.com/joestrout/galactic-empire/blob/1517e2a827e4889f2e86a7ffa1c35e39fcc19452/gameRules.ms

### Relationships (reviewed)

The README explicitly ties this independent recreation to Cary Torkelson’s game and includes a route to the original Mac distribution. Reference material is kept separate from the new MiniScript code. No same-code port or mirror relationship to an already-reviewed root was found in the screened registers.
- https://github.com/joestrout/galactic-empire/blob/1517e2a827e4889f2e86a7ffa1c35e39fcc19452/README.md
- https://github.com/joestrout/galactic-empire/blob/1517e2a827e4889f2e86a7ffa1c35e39fcc19452/main.ms

## Pinned evidence manifest

- jraymonds86--megaroids--.gitignore: https://github.com/jraymonds86/megaroids/blob/79fa383912ee58aad8ee3d96d3a1bc6c8ef21a4d/.gitignore (Git blob fa11b022fc20f5c1849154c789354c1612dc57cc)
- jraymonds86--megaroids--megaroids--audio--soundengine.swift: https://github.com/jraymonds86/megaroids/blob/79fa383912ee58aad8ee3d96d3a1bc6c8ef21a4d/Megaroids/Audio/SoundEngine.swift (Git blob fd552ccb4dc0be8c0395c95222cce716f36f3b70)
- jraymonds86--megaroids--megaroids--game--gameengine.swift: https://github.com/jraymonds86/megaroids/blob/79fa383912ee58aad8ee3d96d3a1bc6c8ef21a4d/Megaroids/Game/GameEngine.swift (Git blob 023c9feee291d80491258949324a15106941e116)
- jraymonds86--megaroids--megaroids--game--ship.swift: https://github.com/jraymonds86/megaroids/blob/79fa383912ee58aad8ee3d96d3a1bc6c8ef21a4d/Megaroids/Game/Ship.swift (Git blob 4c44a19cac1eb46024a3e8fad751e2e666e3c4ba)
- jraymonds86--megaroids--megaroids.c: https://github.com/jraymonds86/megaroids/blob/79fa383912ee58aad8ee3d96d3a1bc6c8ef21a4d/Megaroids.c (Git blob a7703c556adb209bca8450fee0d7246a0882a5a4)
- jraymonds86--megaroids--megaroids.xcodeproj--project.pbxproj: https://github.com/jraymonds86/megaroids/blob/79fa383912ee58aad8ee3d96d3a1bc6c8ef21a4d/Megaroids.xcodeproj/project.pbxproj (Git blob 14916417a758df9af96ec35672909a2a7d7c13c5)
- jraymonds86--megaroids--readme.md: https://github.com/jraymonds86/megaroids/blob/79fa383912ee58aad8ee3d96d3a1bc6c8ef21a4d/README.md (Git blob 3a4f0ec87e26dd47231e474f3fcc9284d019a997)
- native-blzut3--wolf3d-mac--plmove.c: https://github.com/blzut3/wolf3d-mac/blob/4ff692cf2a71f10cefc467e83c910399890747a4/PlMove.c (Git blob e55633652e88d7d16ba49df3d19e21103f61078b)
- native-blzut3--wolf3d-mac--readme.txt: https://github.com/blzut3/wolf3d-mac/blob/4ff692cf2a71f10cefc467e83c910399890747a4/ReadMe.txt (Git blob f3eaff127b85ad4694603865ba208838a93ddf30)
- native-blzut3--wolf3d-mac--refbsp.c: https://github.com/blzut3/wolf3d-mac/blob/4ff692cf2a71f10cefc467e83c910399890747a4/RefBsp.c (Git blob f589f6cf525a0390a97e676699d4183a38ea8124)
- native-blzut3--wolf3d-mac--setupscalers68k.c: https://github.com/blzut3/wolf3d-mac/blob/4ff692cf2a71f10cefc467e83c910399890747a4/SetupScalers68k.c (Git blob 1c64bbf691c556fe479580e6a49f690a66c29572)
- native-blzut3--wolf3d-mac--setupscalersppc.c: https://github.com/blzut3/wolf3d-mac/blob/4ff692cf2a71f10cefc467e83c910399890747a4/SetupScalersPPC.c (Git blob 9336eae2bc409d561cbecc2a1ae3d6b25b9ac70f)
- native-blzut3--wolf3d-mac--wolf.68k: https://github.com/blzut3/wolf3d-mac/blob/4ff692cf2a71f10cefc467e83c910399890747a4/Wolf.68k (Git blob 5426bb64a625c93d96634a1f5c310197b9d8f268)
- native-blzut3--wolf3d-mac--wolf.h: https://github.com/blzut3/wolf3d-mac/blob/4ff692cf2a71f10cefc467e83c910399890747a4/Wolf.h (Git blob cc76549ad2906bf83cce6be5ac6136e12672e93e)
- native-blzut3--wolf3d-mac--wolf.ppc: https://github.com/blzut3/wolf3d-mac/blob/4ff692cf2a71f10cefc467e83c910399890747a4/Wolf.ppc (Git blob 18c6f69c4c451b0791bb00862ac630ec75b192a4)
- native-blzut3--wolf3d-mac--wolfmain.c: https://github.com/blzut3/wolf3d-mac/blob/4ff692cf2a71f10cefc467e83c910399890747a4/WolfMain.c (Git blob a33ecb6352d7ed6c8f0efd6cdf9fef67c3a9e064)
- native-francescom--3tris--fast.html: https://github.com/francescom/3tris/blob/3b991a89dcb435d5333ec842e01f107424686a28/fast.html (Git blob 91fb5f92f834ab025d8a4276d96d183399e609e8)
- native-francescom--3tris--index.html: https://github.com/francescom/3tris/blob/3b991a89dcb435d5333ec842e01f107424686a28/index.html (Git blob e93fa3752b40ddde9d3e5d474b619046b43e63ac)
- native-francescom--3tris--jsinc--3tris.js: https://github.com/francescom/3tris/blob/3b991a89dcb435d5333ec842e01f107424686a28/jsinc/3tris.js (Git blob 0f0121b86d2a3c888ef85ad5c45cdb426712b92f)
- native-francescom--3tris--jsinc--3tris_draw.js: https://github.com/francescom/3tris/blob/3b991a89dcb435d5333ec842e01f107424686a28/jsinc/3tris_draw.js (Git blob c15d19ae6e430ef7fcf7e95b216fa47d83a66c41)
- native-francescom--3tris--jsinc--js_3d_engine.js: https://github.com/francescom/3tris/blob/3b991a89dcb435d5333ec842e01f107424686a28/jsinc/js_3d_engine.js (Git blob fcd6b6f097aaf8aa0fccc53e05dd5d55c4e5298c)
- native-francescom--3tris--jsinc--scoresaver.js: https://github.com/francescom/3tris/blob/3b991a89dcb435d5333ec842e01f107424686a28/jsinc/scoresaver.js (Git blob b2ed5cf4d667f24c12df8829eda62cf761765bec)
- native-francescom--3tris--manifest.php: https://github.com/francescom/3tris/blob/3b991a89dcb435d5333ec842e01f107424686a28/manifest.php (Git blob db4850cfdf2655ce1b5644a829929233b9cc79f8)
- native-francescom--3tris--readme.md: https://github.com/francescom/3tris/blob/3b991a89dcb435d5333ec842e01f107424686a28/README.md (Git blob 160258355af8a5f4413a944bb7c7c537b9808d5b)
- native-jcgraybill--multipong--license: https://github.com/jcgraybill/multipong/blob/5c69a8bfce75a7b62482ac622520fb882918c805/LICENSE (Git blob 261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64)
- native-jcgraybill--multipong--multipong.c: https://github.com/jcgraybill/multipong/blob/5c69a8bfce75a7b62482ac622520fb882918c805/multipong.c (Git blob 09201720405dfbdedbb4864c078c68d123401631)
- native-jcgraybill--multipong--readme.md: https://github.com/jcgraybill/multipong/blob/5c69a8bfce75a7b62482ac622520fb882918c805/README.md (Git blob bbff20cdea4bf4698c89e9b786958d35155bff34)
- native-myaumura--battlechess--config--build.cmake: https://github.com/myaumura/battlechess/blob/fc9211d7e6a5409f8d01d35cd018494d76ca9d0d/config/build.cmake (Git blob 7eae08cd243a831df0d7034568e6a48708149a35)
- native-myaumura--battlechess--docs--build.md: https://github.com/myaumura/battlechess/blob/fc9211d7e6a5409f8d01d35cd018494d76ca9d0d/docs/BUILD.md (Git blob 479c4dd3f2f31db6f3d0272508934b5d76200308)
- native-myaumura--battlechess--docs--data.md: https://github.com/myaumura/battlechess/blob/fc9211d7e6a5409f8d01d35cd018494d76ca9d0d/docs/DATA.md (Git blob 1268a7db622c4a1f5212bbfb142f1701e6968012)
- native-myaumura--battlechess--docs--roadmap.md: https://github.com/myaumura/battlechess/blob/fc9211d7e6a5409f8d01d35cd018494d76ca9d0d/docs/ROADMAP.md (Git blob c5f2977c2b71c746a70ee6f1425b7ad09b0fa851)
- native-myaumura--battlechess--lib--animation.c: https://github.com/myaumura/battlechess/blob/fc9211d7e6a5409f8d01d35cd018494d76ca9d0d/lib/animation.c (Git blob a3646cd72a269f816fc324a68e793c6d8748ff34)
- native-myaumura--battlechess--lib--game.c: https://github.com/myaumura/battlechess/blob/fc9211d7e6a5409f8d01d35cd018494d76ca9d0d/lib/Game.c (Git blob 70e28273f74371d50c2552e8f19b222ef5b78dfe)
- native-myaumura--battlechess--lib--recovered_core.c: https://github.com/myaumura/battlechess/blob/fc9211d7e6a5409f8d01d35cd018494d76ca9d0d/lib/recovered_core.c (Git blob 5025a1c49eff1491ef17d7562803e97b7d8a4feb)
- native-myaumura--battlechess--license: https://github.com/myaumura/battlechess/blob/fc9211d7e6a5409f8d01d35cd018494d76ca9d0d/LICENSE (Git blob c1db1c5562da620effbfd3e2749aa59102940e85)
- native-myaumura--battlechess--notice: https://github.com/myaumura/battlechess/blob/fc9211d7e6a5409f8d01d35cd018494d76ca9d0d/NOTICE (Git blob 4d1719589c7d8b932e8f03431f0718e2d5cb3cca)
- native-myaumura--battlechess--readme.md: https://github.com/myaumura/battlechess/blob/fc9211d7e6a5409f8d01d35cd018494d76ca9d0d/README.md (Git blob 1d3c62f602118254dd6e5f32d4ebaef6813e56fa)
- native-myaumura--battlechess--src--quickdrawcontrol.cpp: https://github.com/myaumura/battlechess/blob/fc9211d7e6a5409f8d01d35cd018494d76ca9d0d/src/QuickDrawControl.cpp (Git blob aa56b42d4f8634df85148c212f7dcda0ccff2af5)
- remakes-depp-sparks-main-cpp: https://github.com/depp/sparks/blob/61a6865733af34949fd912217d7a5441ccce93cd/Main.cpp (Git blob c4801215f134d2bb68771037d9cab48763e3f33f)
- remakes-depp-sparks-makefile: https://github.com/depp/sparks/blob/61a6865733af34949fd912217d7a5441ccce93cd/Makefile (Git blob 2a7b7431d95f7ba931fbae018ce811ce2a9d8758)
- remakes-depp-sparks-readme-md: https://github.com/depp/sparks/blob/61a6865733af34949fd912217d7a5441ccce93cd/README.md (Git blob aa2425d0cb1598a5c764f0d34fc5d6388129514e)
- remakes-joestrout-galactic-empire-gamerules-ms: https://github.com/joestrout/galactic-empire/blob/1517e2a827e4889f2e86a7ffa1c35e39fcc19452/gameRules.ms (Git blob 81ed0dda846d9e1a11a8acbea86294c879ae32d5)
- remakes-joestrout-galactic-empire-license: https://github.com/joestrout/galactic-empire/blob/1517e2a827e4889f2e86a7ffa1c35e39fcc19452/LICENSE (Git blob fdddb29aa445bf3d6a5d843d6dd77e10a9f99657)
- remakes-joestrout-galactic-empire-main-ms: https://github.com/joestrout/galactic-empire/blob/1517e2a827e4889f2e86a7ffa1c35e39fcc19452/main.ms (Git blob e1edfeb6582e0f39651c58281280be55754ab647)
- remakes-joestrout-galactic-empire-readme-md: https://github.com/joestrout/galactic-empire/blob/1517e2a827e4889f2e86a7ffa1c35e39fcc19452/README.md (Git blob 7fdae2762ee6b12338d24c54b143f807ee93a38f)
- roytinker--beasties-macos-port--disasm--code_2.s: https://github.com/roytinker/beasties-macos-port/blob/14b329202f25e01181c8d51b3ecb9d22682f0a17/disasm/CODE_2.s (Git blob c9398def6ad3881372cee4b241a326c2fd09b8ab)
- roytinker--beasties-macos-port--port--build-app.sh: https://github.com/roytinker/beasties-macos-port/blob/14b329202f25e01181c8d51b3ecb9d22682f0a17/port/build-app.sh (Git blob 3141dd8e681beada958b007f5981b79a6b0a0272)
- roytinker--beasties-macos-port--port--license: https://github.com/roytinker/beasties-macos-port/blob/14b329202f25e01181c8d51b3ecb9d22682f0a17/port/LICENSE (Git blob 2781bab7e83e817e00af0fe8378b20cac2c408e7)
- roytinker--beasties-macos-port--port--package.swift: https://github.com/roytinker/beasties-macos-port/blob/14b329202f25e01181c8d51b3ecb9d22682f0a17/port/Package.swift (Git blob 888c8d726b9c9dd67ca68362e45160e0294aa4cb)
- roytinker--beasties-macos-port--port--sources--beast--appdelegate.swift: https://github.com/roytinker/beasties-macos-port/blob/14b329202f25e01181c8d51b3ecb9d22682f0a17/port/Sources/Beast/AppDelegate.swift (Git blob 86bebeb2b3213f1d8773cc0b280c5124526dec87)
- roytinker--beasties-macos-port--port--sources--beast--pict.swift: https://github.com/roytinker/beasties-macos-port/blob/14b329202f25e01181c8d51b3ecb9d22682f0a17/port/Sources/Beast/PICT.swift (Git blob 6965f074a04be7f17ff0c7bd26038f0c380e4ee1)
- roytinker--beasties-macos-port--port--sources--beastcore--beastgame.swift: https://github.com/roytinker/beasties-macos-port/blob/14b329202f25e01181c8d51b3ecb9d22682f0a17/port/Sources/BeastCore/BeastGame.swift (Git blob b0c19fdd55898fc1f5daf74b759847f7d5a5553d)
- roytinker--beasties-macos-port--port--sources--beastcore--qdrandom.swift: https://github.com/roytinker/beasties-macos-port/blob/14b329202f25e01181c8d51b3ecb9d22682f0a17/port/Sources/BeastCore/QDRandom.swift (Git blob c66055d79a2a15bcf14f90035e1095e218ca699c)
- roytinker--beasties-macos-port--readme.md: https://github.com/roytinker/beasties-macos-port/blob/14b329202f25e01181c8d51b3ecb9d22682f0a17/README.md (Git blob aacc4ca38eadedea73bdeebe951fd8a5f56a6df3)
- roytinker--beasties-macos-port--src--beast.p: https://github.com/roytinker/beasties-macos-port/blob/14b329202f25e01181c8d51b3ecb9d22682f0a17/src/Beast.p (Git blob 99fcfa2c75a70738df7a7c47abee277cb70ff79c)

## Sources

```json
[
  {
    "first_indexed": "2026-10-07",
    "id": "github-roytinker-beasties-macos-port",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [
      "beast-mac-pascal-swift-reconstruction"
    ],
    "reason": "Game-specific source and architecture reviewed for classic Macintosh 68k discovery.",
    "review_state": "partial",
    "source": "https://github.com/RoyTinker/beasties-macos-port"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-jraymonds86-megaroids",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [
      "megaroids-mac-swift-source-reconstruction"
    ],
    "reason": "Game-specific source and architecture reviewed for classic Macintosh 68k discovery.",
    "review_state": "partial",
    "source": "https://github.com/jraymonds86/Megaroids"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "web-mrob-missile-source",
    "kind": "website",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [
      "missile-macintosh-munafo-original-source"
    ],
    "reason": "Game-specific source and architecture reviewed for classic Macintosh 68k discovery.",
    "review_state": "partial",
    "source": "https://mrob.com/pub/source/missile.html"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-apmcpherson-videomacpachack",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Hardware clone and control-panel disk image for a Macintosh Portable video card; not a game. README and complete tree inspected.",
    "review_state": "partial",
    "source": "https://github.com/apmcpherson/VideoMacPacHack"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-baptistem-greeblestales",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Python/Pygame game remake identified; repository README names Mac OS 9 only. External archive metadata claims 68k/PPC, but primary original 68k support and full implementation/rights review remain incomplete. Not excluded solely for targeting a modern host.",
    "review_state": "partial",
    "source": "https://github.com/baptistem/GreeblesTales"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-saturn597-stuntcopter",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "README explicitly derives from gamache/blehm source already published in the tracker. Turbo Pascal conversion and difficulty options do not create a new independent implementation lineage.",
    "review_state": "partial",
    "source": "https://github.com/saturn597/StuntCopter"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-metatermin8r-pid-re",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Substantive game-specific 68020 format research and companion Unity engine identified. Held as a research/support source in this game-focused pass rather than padding a second game entry. Actual Cursor-coauthored parser commits found; no inference from assistant-context filenames.",
    "review_state": "partial",
    "source": "https://github.com/metatermin8r/pid-re"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-metatermin8r-pathways-into-darkness-unity",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Source implements level geometry, doors, transitions and partial player state, so README claims of no functionality are stale. Later companion notes describe inventory/combat beyond this pinned public Unity tree, whose head explicitly says no enemy logic. Hold for reconciliation of publicly present game scope, missing user-supplied data and output target evidence.",
    "review_state": "partial",
    "source": "https://github.com/metatermin8r/pathways-into-darkness-unity"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-jcgraybill-multipong",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Multi Pong: native Macintosh multi-window Pong; pinned source, architecture, build, runtime and lineage review.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/jcgraybill/multipong"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-myaumura-battlechess",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Battle Chess: Macintosh 68k recovery to native C/C++; pinned source, architecture, build, runtime and lineage review.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/myaumura/BattleChess"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-francescom-3tris",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "3Tris: HTML5 recreation of the Macintosh 68k puzzle game; pinned source, architecture, build, runtime and lineage review.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/francescom/3Tris"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-blzut3-wolf3d-mac",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Wolfenstein 3D: original Macintosh 68k/PowerPC source archive; pinned source, architecture, build, runtime and lineage review.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/Blzut3/Wolf3D-Mac"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-p-z-l-games-from-1984",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Modern Swift/SpriteKit remakes named Breaklet and Asteroids with real source exist, but the README and per-game descriptions do not identify the specific historical Macintosh editions or provide exact 68k ancestry. Breaklet additionally calls itself a classic Atari Breakout recreation. Resolve the intended Macintosh original and its architecture before promotion; do not infer m68k solely from the 1984 repository name.",
    "review_state": "partial",
    "source": "https://github.com/p-z-l/games-from-1984"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-samuel-cooper-darkwood",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "README only calls this a recreation of an old Macintosh game. Inspected Java battle code is incomplete, with placeholder/syntax-level issues, and no exact original release, 68k evidence, resource provenance or root license is supplied. Identify the original Darkwood and inspect an authoritative architecture source before deciding eligibility.",
    "review_state": "partial",
    "source": "https://github.com/samuel-cooper/darkwood"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-mlaux-gray-brick",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Game Boy/Game Boy Color emulator and JIT toolkit targeting 68k Macintosh, not an independently implemented Macintosh game. Its game compatibility list does not create new game records. README explicitly discloses Claude Code assistance, but the tool remains outside this game-only pass.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/mlaux/gray-brick"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-vaelen-clarus",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Compiled language, compiler and runtime for System 6/7 native 68k applications. README and tree establish a development toolchain; a bouncing-ball code sample does not establish an independent game. No game promotion in this pass.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/vaelen/clarus"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-rdrmic-think-columns",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "README identifies an unrelated 2006 Python 2.4/Pygame Columns-style game. It surfaced through an imprecise THINK C repository query; no classic Macintosh 68k association is established.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/rdrmic/think-columns"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-depp-sparks",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [
      "sparks-classic-mac-restoration-depp"
    ],
    "reason": "Macintosh 68k games, bounded static implementation and ancestry review",
    "review_state": "partial",
    "source": "https://github.com/depp/sparks"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-arfeo-balderdoush",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Substantive game implementation reviewed, but held pending primary-source confirmation of the historical Macintosh 68k edition.",
    "review_state": "partial",
    "source": "https://github.com/arfeo/Balderdoush"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-joestrout-galactic-empire",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [
      "galactic-empire-minimicro-joestrout"
    ],
    "reason": "Macintosh 68k games, bounded static implementation and ancestry review",
    "review_state": "partial",
    "source": "https://github.com/JoeStrout/galactic-empire"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-sefk-daleks",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Substantive game implementation reviewed, but held pending primary-source confirmation of the historical Macintosh 68k edition.",
    "review_state": "partial",
    "source": "https://github.com/sefk/daleks"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-aaronsaikovski-godaleks",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Substantive game implementation reviewed, but held pending primary-source confirmation of the historical Macintosh 68k edition.",
    "review_state": "partial",
    "source": "https://github.com/AaronSaikovski/godaleks"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-dobromirmontauk-spectre-remake",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Substantive game implementation reviewed, but held pending primary-source confirmation of the historical Macintosh 68k edition.",
    "review_state": "partial",
    "source": "https://github.com/dobromirmontauk/spectre-remake"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-rezmason-scourge",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Macintosh 68k games, bounded static implementation and ancestry review",
    "review_state": "partial",
    "source": "https://github.com/Rezmason/Scourge"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-arfeo-deadend",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Macintosh 68k games, bounded static implementation and ancestry review",
    "review_state": "partial",
    "source": "https://github.com/arfeo/DeadEnd"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-thefakemontyontherun-space-trashman-blues",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Macintosh 68k games, bounded static implementation and ancestry review",
    "review_state": "partial",
    "source": "https://github.com/TheFakeMontyOnTheRun/space-trashman-blues"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-tristanstcyr-macfungus-2.0",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Macintosh 68k games, bounded static implementation and ancestry review",
    "review_state": "partial",
    "source": "https://github.com/tristanstcyr/MacFungus-2.0"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-jegger-factory-industrial-devolution",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Macintosh 68k games, bounded static implementation and ancestry review",
    "review_state": "partial",
    "source": "https://github.com/jegger/factory-industrial-devolution"
  }
]
```

## Decisions

```json
[
  {
    "decision": "excluded",
    "evidence_urls": [
      "https://github.com/apmcpherson/VideoMacPacHack/blob/ffc5633452705cae010b3777d0807670c4eed379/README.md"
    ],
    "id": "discovery-2026-10-07-mac68k-round2-apmcpherson-videomacpachack",
    "project_ids": [],
    "reason": "Hardware clone and control-panel disk image for a Macintosh Portable video card; not a game. README and complete tree inspected.",
    "reviewed_at": "2026-10-07",
    "source_ids": [
      "github-apmcpherson-videomacpachack"
    ],
    "title": "apmcpherson/VideoMacPacHack",
    "url": "https://github.com/apmcpherson/VideoMacPacHack"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/baptistem/GreeblesTales/blob/7458b218e1ce14bc5c1896e5ce8c782741fe1cb8/readme.md"
    ],
    "id": "discovery-2026-10-07-mac68k-round2-baptistem-greeblestales",
    "project_ids": [],
    "reason": "Python/Pygame game remake identified; repository README names Mac OS 9 only. External archive metadata claims 68k/PPC, but primary original 68k support and full implementation/rights review remain incomplete. Not excluded solely for targeting a modern host.",
    "reviewed_at": "2026-10-07",
    "source_ids": [
      "github-baptistem-greeblestales"
    ],
    "title": "baptistem/GreeblesTales",
    "url": "https://github.com/baptistem/GreeblesTales"
  },
  {
    "decision": "duplicate",
    "evidence_urls": [
      "https://github.com/saturn597/StuntCopter/blob/d2b860ef24a2e10b1f18c48c5c338d826e296d0f/README.md"
    ],
    "id": "discovery-2026-10-07-mac68k-round2-saturn597-stuntcopter",
    "project_ids": [],
    "reason": "README explicitly derives from gamache/blehm source already published in the tracker. Turbo Pascal conversion and difficulty options do not create a new independent implementation lineage.",
    "reviewed_at": "2026-10-07",
    "source_ids": [
      "github-saturn597-stuntcopter"
    ],
    "title": "saturn597/StuntCopter",
    "url": "https://github.com/saturn597/StuntCopter"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/metatermin8r/pid-re/blob/fb010dfe68bbbc58db5c145bed75a68d66d7c193/README.md"
    ],
    "id": "discovery-2026-10-07-mac68k-round2-metatermin8r-pid-re",
    "project_ids": [],
    "reason": "Substantive game-specific 68020 format research and companion Unity engine identified. Held as a research/support source in this game-focused pass rather than padding a second game entry. Actual Cursor-coauthored parser commits found; no inference from assistant-context filenames.",
    "reviewed_at": "2026-10-07",
    "source_ids": [
      "github-metatermin8r-pid-re"
    ],
    "title": "metatermin8r/pid-re",
    "url": "https://github.com/metatermin8r/pid-re"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/metatermin8r/pathways-into-darkness-unity/blob/db3124148e5fede849debece10ce627debea8a1d/README.md"
    ],
    "id": "discovery-2026-10-07-mac68k-round2-metatermin8r-pathways-into-darkness-unity",
    "project_ids": [],
    "reason": "Source implements level geometry, doors, transitions and partial player state, so README claims of no functionality are stale. Later companion notes describe inventory/combat beyond this pinned public Unity tree, whose head explicitly says no enemy logic. Hold for reconciliation of publicly present game scope, missing user-supplied data and output target evidence.",
    "reviewed_at": "2026-10-07",
    "source_ids": [
      "github-metatermin8r-pathways-into-darkness-unity"
    ],
    "title": "metatermin8r/pathways-into-darkness-unity",
    "url": "https://github.com/metatermin8r/pathways-into-darkness-unity"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/p-z-l/games-from-1984/blob/57d04b264a76aabb8d240bd40e3d689461120494/README.md",
      "https://github.com/p-z-l/games-from-1984/blob/57d04b264a76aabb8d240bd40e3d689461120494/Asteroids/README.md",
      "https://github.com/p-z-l/games-from-1984/blob/57d04b264a76aabb8d240bd40e3d689461120494/Breaklet/README.md",
      "https://github.com/p-z-l/games-from-1984/blob/57d04b264a76aabb8d240bd40e3d689461120494/Asteroids/Asteroids/GameScene.swift",
      "https://github.com/p-z-l/games-from-1984/blob/57d04b264a76aabb8d240bd40e3d689461120494/Breaklet/Breaklet/GameScene.swift"
    ],
    "id": "discovery-2026-10-07-mac68k-round2-p-z-l-games-from-1984",
    "project_ids": [],
    "reason": "Modern Swift/SpriteKit remakes named Breaklet and Asteroids with real source exist, but the README and per-game descriptions do not identify the specific historical Macintosh editions or provide exact 68k ancestry. Breaklet additionally calls itself a classic Atari Breakout recreation. Resolve the intended Macintosh original and its architecture before promotion; do not infer m68k solely from the 1984 repository name.",
    "reviewed_at": "2026-10-07",
    "source_ids": [
      "github-p-z-l-games-from-1984"
    ],
    "title": "p-z-l/games-from-1984",
    "url": "https://github.com/p-z-l/games-from-1984"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/samuel-cooper/darkwood/blob/efe504eea2de0e724ca1894bca1d4bd6cbd78654/README.md",
      "https://github.com/samuel-cooper/darkwood/blob/efe504eea2de0e724ca1894bca1d4bd6cbd78654/src/Battle.java",
      "https://github.com/samuel-cooper/darkwood/blob/efe504eea2de0e724ca1894bca1d4bd6cbd78654/src/Player.java"
    ],
    "id": "discovery-2026-10-07-mac68k-round2-samuel-cooper-darkwood",
    "project_ids": [],
    "reason": "README only calls this a recreation of an old Macintosh game. Inspected Java battle code is incomplete, with placeholder/syntax-level issues, and no exact original release, 68k evidence, resource provenance or root license is supplied. Identify the original Darkwood and inspect an authoritative architecture source before deciding eligibility.",
    "reviewed_at": "2026-10-07",
    "source_ids": [
      "github-samuel-cooper-darkwood"
    ],
    "title": "samuel-cooper/darkwood",
    "url": "https://github.com/samuel-cooper/darkwood"
  },
  {
    "decision": "excluded",
    "evidence_urls": [
      "https://github.com/mlaux/gray-brick/blob/b7542faae806af2fafab94ed3fc5c70efa0fcb98/README.md",
      "https://github.com/mlaux/gray-brick/blob/b7542faae806af2fafab94ed3fc5c70efa0fcb98/compiler/compiler.c",
      "https://github.com/mlaux/gray-brick/blob/b7542faae806af2fafab94ed3fc5c70efa0fcb98/system6/emulator.c"
    ],
    "id": "discovery-2026-10-07-mac68k-round2-mlaux-gray-brick",
    "project_ids": [],
    "reason": "Game Boy/Game Boy Color emulator and JIT toolkit targeting 68k Macintosh, not an independently implemented Macintosh game. Its game compatibility list does not create new game records. README explicitly discloses Claude Code assistance, but the tool remains outside this game-only pass.",
    "reviewed_at": "2026-10-07",
    "source_ids": [
      "github-mlaux-gray-brick"
    ],
    "title": "mlaux/gray-brick",
    "url": "https://github.com/mlaux/gray-brick"
  },
  {
    "decision": "excluded",
    "evidence_urls": [
      "https://github.com/vaelen/clarus/blob/9121955a8d656ce877c4fe9a0c0d3ecd188bde92/README.md"
    ],
    "id": "discovery-2026-10-07-mac68k-round2-vaelen-clarus",
    "project_ids": [],
    "reason": "Compiled language, compiler and runtime for System 6/7 native 68k applications. README and tree establish a development toolchain; a bouncing-ball code sample does not establish an independent game. No game promotion in this pass.",
    "reviewed_at": "2026-10-07",
    "source_ids": [
      "github-vaelen-clarus"
    ],
    "title": "vaelen/clarus",
    "url": "https://github.com/vaelen/clarus"
  },
  {
    "decision": "excluded",
    "evidence_urls": [
      "https://github.com/rdrmic/think-columns/blob/ffce412de37d864387f0abfaa36767b8f6cfdaa1/README.md"
    ],
    "id": "discovery-2026-10-07-mac68k-round2-rdrmic-think-columns",
    "project_ids": [],
    "reason": "README identifies an unrelated 2006 Python 2.4/Pygame Columns-style game. It surfaced through an imprecise THINK C repository query; no classic Macintosh 68k association is established.",
    "reviewed_at": "2026-10-07",
    "source_ids": [
      "github-rdrmic-think-columns"
    ],
    "title": "rdrmic/think-columns",
    "url": "https://github.com/rdrmic/think-columns"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/depp/sparks/blob/61a6865733af34949fd912217d7a5441ccce93cd/README.md"
    ],
    "id": "discovery-2026-10-07-remakes-depp-sparks",
    "project_ids": [
      "sparks-classic-mac-restoration-depp"
    ],
    "reason": "Static gameplay/source and specific Macintosh 68k ancestry reviewed; build/run/playable/byte-exact remain unknown.",
    "reviewed_at": "2026-10-07",
    "source_ids": [
      "github-depp-sparks"
    ],
    "title": "depp/sparks",
    "url": "https://github.com/depp/sparks"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/arfeo/Balderdoush/blob/dab61c46dcf005fe85420deb780a096ea95b3c3d/README.md"
    ],
    "id": "discovery-2026-10-07-remakes-arfeo-balderdoush",
    "project_ids": [],
    "reason": "Primary-evidence admission hold: the specific Macintosh remake and actual gameplay implementation are established, but historical 68k CPU evidence rests on archive metadata/transcribed requirements. Original binary/header or original author documentation explicitly confirming the 68k edition was not verified. Preserve the reviewed source facts without promoting the project in this batch.",
    "reviewed_at": "2026-10-07",
    "source_ids": [
      "github-arfeo-balderdoush"
    ],
    "title": "arfeo/Balderdoush",
    "url": "https://github.com/arfeo/Balderdoush"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/JoeStrout/galactic-empire/blob/1517e2a827e4889f2e86a7ffa1c35e39fcc19452/README.md"
    ],
    "id": "discovery-2026-10-07-remakes-joestrout-galactic-empire",
    "project_ids": [
      "galactic-empire-minimicro-joestrout"
    ],
    "reason": "Static gameplay/source and specific Macintosh 68k ancestry reviewed; build/run/playable/byte-exact remain unknown.",
    "reviewed_at": "2026-10-07",
    "source_ids": [
      "github-joestrout-galactic-empire"
    ],
    "title": "JoeStrout/galactic-empire",
    "url": "https://github.com/JoeStrout/galactic-empire"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/sefk/daleks/blob/49b19f64acc0574f6678c59d713dc2b2a0192714/README.md"
    ],
    "id": "discovery-2026-10-07-remakes-sefk-daleks",
    "project_ids": [],
    "reason": "Primary-evidence admission hold: the specific Macintosh remake and actual gameplay implementation are established, but historical 68k CPU evidence rests on archive metadata/transcribed requirements. Original binary/header or original author documentation explicitly confirming the 68k edition was not verified. Preserve the reviewed source facts without promoting the project in this batch.",
    "reviewed_at": "2026-10-07",
    "source_ids": [
      "github-sefk-daleks"
    ],
    "title": "sefk/daleks",
    "url": "https://github.com/sefk/daleks"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/AaronSaikovski/godaleks/blob/04ab86addd9fbd3fa77b58c2b204d3b8eb0e4310/README.md"
    ],
    "id": "discovery-2026-10-07-remakes-aaronsaikovski-godaleks",
    "project_ids": [],
    "reason": "Primary-evidence admission hold: the specific Macintosh remake and actual gameplay implementation are established, but historical 68k CPU evidence rests on archive metadata/transcribed requirements. Original binary/header or original author documentation explicitly confirming the 68k edition was not verified. Preserve the reviewed source facts without promoting the project in this batch.",
    "reviewed_at": "2026-10-07",
    "source_ids": [
      "github-aaronsaikovski-godaleks"
    ],
    "title": "AaronSaikovski/godaleks",
    "url": "https://github.com/AaronSaikovski/godaleks"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/dobromirmontauk/spectre-remake/blob/29e128a8b1c71df3b0bb9161f14c11d87ec179ad/GOAL.md"
    ],
    "id": "discovery-2026-10-07-remakes-dobromirmontauk-spectre-remake",
    "project_ids": [],
    "reason": "Primary-evidence admission hold: the specific Macintosh remake and actual gameplay implementation are established, but historical 68k CPU evidence rests on archive metadata/transcribed requirements. Original binary/header or original author documentation explicitly confirming the 68k edition was not verified. Preserve the reviewed source facts without promoting the project in this batch.",
    "reviewed_at": "2026-10-07",
    "source_ids": [
      "github-dobromirmontauk-spectre-remake"
    ],
    "title": "dobromirmontauk/spectre-remake",
    "url": "https://github.com/dobromirmontauk/spectre-remake"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/Rezmason/Scourge/blob/0d5bd435851f3058ef40de2d25d786af3e185c45/README.md"
    ],
    "id": "discovery-2026-10-07-remakes-rezmason-scourge",
    "project_ids": [],
    "reason": "Substantive Haxe/Praxis Fungus derivative with source, gameplay rules, assets and GPL-3.0-or-later disclosure; held because the inspected primary README and Info-Mac original-game announcement do not state original 68k execution requirements. The 1992 date alone is not used as CPU evidence.",
    "reviewed_at": "2026-10-07",
    "source_ids": [
      "github-rezmason-scourge"
    ],
    "title": "Rezmason/Scourge",
    "url": "https://github.com/Rezmason/Scourge"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/arfeo/DeadEnd/blob/bfb53a0d294fda94f32f255a8978122cfcbd11d1/README.md"
    ],
    "id": "discovery-2026-10-07-remakes-arfeo-deadend",
    "project_ids": [],
    "reason": "Substantive MIT TypeScript/Canvas remake of the specifically named DeadEnd II with levels and build scripts; held because this 1998 variant’s 68k versus PPC status was not established. Evidence for the earlier 1993 DeadEnd is insufficient to silently assign the sequel’s CPU.",
    "reviewed_at": "2026-10-07",
    "source_ids": [
      "github-arfeo-deadend"
    ],
    "title": "arfeo/DeadEnd",
    "url": "https://github.com/arfeo/DeadEnd"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/TheFakeMontyOnTheRun/space-trashman-blues/blob/f94e0c3ac75d0a40bc25514f5c80b7bcf1f418e2/README.md"
    ],
    "id": "discovery-2026-10-07-remakes-thefakemontyontherun-space-trashman-blues",
    "project_ids": [],
    "reason": "Sub Mare Imperium: Derelict has multiple modern/retro frontends and mentions Macintosh classic as an output. The inspected README/core/frontend docs do not establish a historical Macintosh 68k game ancestor; modern host/output availability alone does not meet this lane’s ancestry rule.",
    "reviewed_at": "2026-10-07",
    "source_ids": [
      "github-thefakemontyontherun-space-trashman-blues"
    ],
    "title": "TheFakeMontyOnTheRun/space-trashman-blues",
    "url": "https://github.com/TheFakeMontyOnTheRun/space-trashman-blues"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/tristanstcyr/MacFungus-2.0/blob/8f1f7e384f478828dc9b992f1d69f88e93b591bc/README"
    ],
    "id": "discovery-2026-10-07-remakes-tristanstcyr-macfungus-2.0",
    "project_ids": [],
    "reason": "Unreleased 2006-era MacFungus next-version source with Cocoa/Objective-C++/C++ gameplay and BSD license; held because the inspected README does not establish the chain to the 68k Fungus original or distinguish source inheritance from earlier MacFungus implementations.",
    "reviewed_at": "2026-10-07",
    "source_ids": [
      "github-tristanstcyr-macfungus-2.0"
    ],
    "title": "tristanstcyr/MacFungus-2.0",
    "url": "https://github.com/tristanstcyr/MacFungus-2.0"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/jegger/factory-industrial-devolution/blob/9a17f55d659c0fbf563ee477b9dade3acb98f47c/main.py"
    ],
    "id": "discovery-2026-10-07-remakes-jegger-factory-industrial-devolution",
    "project_ids": [],
    "reason": "Actual Python/Kivy game source, KV UI, sprite assets and two map JSON files are present, but the remake description is the only inspected identity link to Factory. No README, license or exact original 68k provenance was established; retain for research rather than description-only promotion.",
    "reviewed_at": "2026-10-07",
    "source_ids": [
      "github-jegger-factory-industrial-devolution"
    ],
    "title": "jegger/factory-industrial-devolution",
    "url": "https://github.com/jegger/factory-industrial-devolution"
  }
]
```

## Research event notes

User-approved publication following static review of 9 further game projects connected to classic Macintosh 68k source or native outputs. The user approved publishing these nine to main on 2026-10-07; 19 held, excluded or duplicate leads remain unpromoted. Facts and eight audit areas were authored once; report and payload are generated. Exact baseline 96bf999c862ca1a41d6752977f350d501935b019 has 1,789 projects and 99 Git-blob-verified files. The exclusion union contains 2,171 normalized current catalogue, source/decision and all-prior-reviewed GitHub roots; non-GitHub candidate identity and URL were checked separately. Search-only leads are not misrepresented as previously reviewed. Distinct independent implementations may share titles; mirrors and same-code ports remain duplicates. Modern host ISA is never inferred from historical 68k input or generic compiler support. No game was built, tested, launched, played or byte-compared; all independent build/runtime flags remain unknown. AI attribution requires an explicit developer statement or actual implementation commit. Where legacy source bytes are not UTF-8, original-byte integrity is kept separately and pinned URLs are cited rather than fabricating UTF-8 cache identities. Web-source snapshots are mutable-source observations with separately retained hashes, not Git proofs. All pre-existing catalogue objects, audit snapshots, activity and polling state are preserved. Coverage is bounded; holds and unreviewed leads are recorded without an exhaustiveness claim.
