# Acorn emulation, Gold Box archaeology and legacy-disk discovery

Review eight canonical candidates, promote seven projects, and advance the Acorn/BBC relationship graph

Date: 2026-11-02 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- jsbeeb-bbc-micro-emulator / Build (reviewed): The tracker did not install dependencies, compile, package or run the emulator.
- beebjit-libretro-bbc-micro-core / Build (reviewed): The tracker did not compile the core, connect to a handheld, run RetroArch or reproduce performance figures.
- beeblink-bbc-file-server / Target CPU (no-evidence-found): The reviewed README and ROM build document name BBC/Electron targets and 64tass but do not explicitly state the ROM output CPU; the value is not inferred from platform.
- beeblink-bbc-file-server / Build (reviewed): The tracker did not build the ROM/server or connect physical hardware.
- beeblink-bbc-file-server / AI (no-evidence-found): No explicit development-AI attribution was found in the reviewed README or build documents; this does not establish non-use.
- wish-gold-box-save-editor-automapper / Build (reviewed): The tracker did not install Wish, open copyrighted media or attach to an emulator.
- stnicc-beeb-bbc-demo-recreation / Build (reviewed): The tracker did not assemble the demo, generate media or run an emulator.
- stnicc-beeb-bbc-demo-recreation / Runtime profiles (no-evidence-found): BBC and Master emulator configurations are named, but the reviewed primary files do not state a minimum model, RAM amount or chipset requirement.
- legacy89diskkit-japanese-disk-toolkit / Build (reviewed): The tracker did not build either implementation or open a disk image.
- legacy89diskkit-japanese-disk-toolkit / AI (no-evidence-found): No explicit development-AI attribution was found in the reviewed README or platform support document; agent-oriented planning filenames alone are not treated as contribution evidence.
- nectaris-javascript-remake / Source CPU (no-evidence-found): The reviewed primary documents name the PC Engine target but do not state an original CPU architecture; no CPU is inferred from platform.
- nectaris-javascript-remake / Build (reviewed): The tracker did not host, run or test the remake and did not execute original game binaries.
- nectaris-javascript-remake / Runtime profiles (no-evidence-found): A static-browser route is documented, but no minimum browser version, host CPU or RAM is stated.

## jsbeeb — JavaScript BBC Micro-family emulator

Project ID: jsbeeb-bbc-micro-emulator · Overall audit: reviewed

### Typed catalogue values

```json
{
  "ai": {
    "evidence": [
      "Latest reviewed upstream commit explicitly says it was generated with Claude Code and credits Claude Opus 5.5: https://github.com/mattgodbolt/jsbeeb/commit/178031ec9e7420a0965981f7f7877df35886fe0c"
    ],
    "tools": [
      "Claude Code"
    ],
    "usage": true
  },
  "build": {
    "byte_exact": null,
    "compilable": true,
    "playable": true,
    "runnable": true
  },
  "display_title": "jsbeeb — JavaScript BBC Micro-family emulator",
  "id": "jsbeeb-bbc-micro-emulator",
  "last_activity": "2026-11-01",
  "last_checked": "2026-11-02",
  "re_started": null,
  "reconstructed_languages": [
    "JavaScript"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/mattgodbolt/jsbeeb",
  "runtime_profiles": [
    {
      "evidence": [
        "https://github.com/mattgodbolt/jsbeeb/blob/178031ec9e7420a0965981f7f7877df35886fe0c/package.json"
      ],
      "name": "Browser build",
      "notes": "The package browserslist states these browser floors; no host CPU or RAM minimum is stated.",
      "os": "Chrome 111+, Edge 111+, Firefox 115+, Safari 16.4+ or iOS Safari 16.4+",
      "platform": "Web browser"
    },
    {
      "evidence": [
        "https://github.com/mattgodbolt/jsbeeb/blob/178031ec9e7420a0965981f7f7877df35886fe0c/package.json"
      ],
      "name": "Source and desktop build",
      "notes": "The package manifest states the Node floor and documents optional Electron packaging; no host CPU or RAM minimum is stated.",
      "os": "Node.js 24.15.0 or later",
      "platform": "Windows, Linux or macOS"
    }
  ],
  "source_cpu": [
    "6502",
    "65C02",
    "65C12"
  ],
  "source_language": [
    "6502 machine behavior",
    "65C02 machine behavior",
    "65C12 machine behavior"
  ],
  "source_platforms": [
    "BBC Micro",
    "BBC Master 128",
    "Acorn Atom"
  ],
  "status": "Active browser and Electron emulator with debugger, rewind, media inspection and automated CPU tests; not independently built or run in this review.",
  "subjects": [
    "BBC Micro",
    "BBC Master 128",
    "Acorn Atom"
  ],
  "tags": [
    "BBC Micro",
    "BBC Master",
    "Acorn Atom",
    "6502",
    "65C02",
    "65C12",
    "emulator",
    "debugger"
  ],
  "target_cpu": [],
  "target_kinds": [],
  "target_platforms": [
    "Web browser",
    "Windows",
    "Linux",
    "macOS"
  ],
  "techniques": [
    "cycle-aware 6502-family emulation",
    "integrated debugging",
    "save-state rewind",
    "disc surface inspection",
    "CPU regression testing"
  ],
  "title": "jsbeeb — JavaScript BBC Micro-family emulator",
  "tool_kinds": [
    "emulator",
    "debugger",
    "binary-analysis"
  ],
  "types": [
    "browser emulator",
    "desktop emulator",
    "integrated debugger"
  ],
  "upstream_name": "jsbeeb",
  "work_kinds": []
}
```

### Identity (reviewed)

jsbeeb is the canonical JavaScript BBC Micro-family emulator maintained by Matt Godbolt.
- https://github.com/mattgodbolt/jsbeeb/blob/178031ec9e7420a0965981f7f7877df35886fe0c/README.md

### Classification (reviewed)

It qualifies as a core emulator, debugger and media-analysis environment directly useful to BBC development and archaeology.
- https://github.com/mattgodbolt/jsbeeb/blob/178031ec9e7420a0965981f7f7877df35886fe0c/README.md

### Source CPU (reviewed)

The model implementation explicitly selects MOS 6502, CMOS 65C02 and CMOS 65C12 opcode families.
- https://github.com/mattgodbolt/jsbeeb/blob/178031ec9e7420a0965981f7f7877df35886fe0c/src/models.js

### Target CPU (not-applicable)

Browser and Electron builds do not establish one fixed native output CPU; no host architecture is inferred.
- https://github.com/mattgodbolt/jsbeeb/blob/178031ec9e7420a0965981f7f7877df35886fe0c/package.json

### Build (reviewed)

The README and package manifest document npm development, test, web build and Electron packaging paths. Limitations: The tracker did not install dependencies, compile, package or run the emulator.
- https://github.com/mattgodbolt/jsbeeb/blob/178031ec9e7420a0965981f7f7877df35886fe0c/README.md
- https://github.com/mattgodbolt/jsbeeb/blob/178031ec9e7420a0965981f7f7877df35886fe0c/package.json

### Runtime profiles (reviewed)

The package manifest gives exact supported browser floors and Node.js 24.15.0+ for source/desktop builds; no CPU or RAM minimum is stated.
- https://github.com/mattgodbolt/jsbeeb/blob/178031ec9e7420a0965981f7f7877df35886fe0c/package.json

### AI (reviewed)

The reviewed head commit explicitly attributes generation to Claude Code and co-authorship to Claude Opus 5.5.
- https://github.com/mattgodbolt/jsbeeb/commit/178031ec9e7420a0965981f7f7877df35886fe0c

### Relationships (reviewed)

The separately tracked jsbeeb-mcp project exposes this emulator through MCP; that automation layer does not replace the emulator record.
- https://github.com/mattgodbolt/jsbeeb/blob/178031ec9e7420a0965981f7f7877df35886fe0c/README.md
- https://github.com/kieranhj/jsbeeb-mcp

## beebjit-libretro — BBC Micro JIT emulator core for RetroArch

Project ID: beebjit-libretro-bbc-micro-core · Overall audit: partial

### Typed catalogue values

```json
{
  "ai": {
    "evidence": [
      "README states the core was written with Claude Code under Kieran Connell's direction."
    ],
    "tools": [
      "Claude Code"
    ],
    "usage": true
  },
  "build": {
    "byte_exact": null,
    "compilable": true,
    "playable": true,
    "runnable": true
  },
  "display_title": "beebjit-libretro — BBC Micro JIT emulator core for RetroArch",
  "id": "beebjit-libretro-bbc-micro-core",
  "last_activity": "2026-11-01",
  "last_checked": "2026-11-02",
  "re_started": null,
  "reconstructed_languages": [
    "C"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/kieranhj/beebjit-libretro",
  "runtime_profiles": [
    {
      "cpu_family": "ARM64",
      "evidence": [
        "https://github.com/kieranhj/beebjit-libretro/blob/763450c5611d54b71b6bd68077bc7385e62af2bf/README.md"
      ],
      "min_cpu": "Allwinner H700 quad Cortex-A53 is the documented first tested target, not a claimed minimum",
      "name": "RG40XXV muOS tested target",
      "notes": "The README reports full-speed BBC emulation on this device and says the JIT requires a 64-bit host. No RAM minimum is stated.",
      "platform": "muOS / RetroArch"
    }
  ],
  "source_cpu": [
    "6502"
  ],
  "source_language": [
    "6502 machine behavior"
  ],
  "source_platforms": [
    "BBC Micro",
    "BBC Master 128"
  ],
  "status": "Linux-only libretro wrapper around beebjit with ARM64/x64 JIT support and documented RG40XXV measurements; not independently built or benchmarked.",
  "subjects": [
    "BBC Model B",
    "BBC Master 128",
    "beebjit"
  ],
  "tags": [
    "BBC Micro",
    "BBC Master",
    "6502",
    "ARM64",
    "x86-64",
    "libretro",
    "emulator",
    "Claude Code"
  ],
  "target_cpu": [
    "x86-64",
    "ARM64"
  ],
  "target_kinds": [],
  "target_platforms": [
    "Linux",
    "Libretro",
    "muOS"
  ],
  "techniques": [
    "JIT CPU emulation",
    "libretro integration",
    "vertical-sync lockstep",
    "headless benchmarking",
    "cross-building with Zig"
  ],
  "title": "beebjit-libretro — BBC Micro JIT emulator core for RetroArch",
  "tool_kinds": [
    "emulator",
    "debugger"
  ],
  "types": [
    "libretro core",
    "JIT emulator integration"
  ],
  "upstream_name": "beebjit-libretro",
  "work_kinds": []
}
```

### Identity (reviewed)

This repository is the distinct libretro glue layer around Chris Evans' beebjit emulator.
- https://github.com/kieranhj/beebjit-libretro/blob/763450c5611d54b71b6bd68077bc7385e62af2bf/README.md

### Classification (reviewed)

It qualifies as a BBC emulator integration and debugging/benchmark environment rather than a new independent CPU core.
- https://github.com/kieranhj/beebjit-libretro/blob/763450c5611d54b71b6bd68077bc7385e62af2bf/README.md

### Source CPU (reviewed)

The README explicitly describes beebjit's JIT as 6502-only and the interpreter option as the 6502 core.
- https://github.com/kieranhj/beebjit-libretro/blob/763450c5611d54b71b6bd68077bc7385e62af2bf/README.md

### Target CPU (reviewed)

The README explicitly limits the JIT to ARM64 and x64 64-bit Linux hosts and documents an aarch64 cross-build.
- https://github.com/kieranhj/beebjit-libretro/blob/763450c5611d54b71b6bd68077bc7385e62af2bf/README.md

### Build (reviewed)

Native Linux make and Zig-based aarch64 cross-build commands are documented along with headless test and benchmark scripts. Limitations: The tracker did not compile the core, connect to a handheld, run RetroArch or reproduce performance figures.
- https://github.com/kieranhj/beebjit-libretro/blob/763450c5611d54b71b6bd68077bc7385e62af2bf/README.md

### Runtime profiles (reviewed)

An RG40XXV with Allwinner H700 quad Cortex-A53 running muOS is an explicitly measured target; this is retained as a tested profile, not generalized into a minimum.
- https://github.com/kieranhj/beebjit-libretro/blob/763450c5611d54b71b6bd68077bc7385e62af2bf/README.md

### AI (reviewed)

The README explicitly says Claude Code wrote the core from Kieran Connell's direction; the reviewed head commit also credits Claude Opus 5.5.
- https://github.com/kieranhj/beebjit-libretro/blob/763450c5611d54b71b6bd68077bc7385e62af2bf/README.md
- https://github.com/kieranhj/beebjit-libretro/commit/763450c5611d54b71b6bd68077bc7385e62af2bf

### Relationships (reviewed)

The core wraps beebjit as a submodule and says its repository adds only libretro glue and two OS substitutions.
- https://github.com/kieranhj/beebjit-libretro/blob/763450c5611d54b71b6bd68077bc7385e62af2bf/README.md

## BeebLink — BBC Micro and Electron host file server

Project ID: beeblink-bbc-file-server · Overall audit: partial

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
    "runnable": true
  },
  "display_title": "BeebLink — BBC Micro and Electron host file server",
  "id": "beeblink-bbc-file-server",
  "last_activity": "2026-06-03",
  "last_checked": "2026-11-02",
  "re_started": null,
  "reconstructed_languages": [
    "JavaScript",
    "C++",
    "assembly"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/tom-seddon/beeblink",
  "runtime_profiles": [
    {
      "evidence": [
        "https://github.com/tom-seddon/beeblink/blob/58776b038d1fe7494a2c15564b0a5e1b7860a928/docs/build-server.md"
      ],
      "name": "Host server",
      "notes": "Windows additionally needs Visual Studio to build; macOS needs Xcode; Ubuntu needs libusb-dev and libudev-dev. No CPU or RAM minimum is stated.",
      "os": "Node.js 18.20 or later",
      "platform": "Windows, Linux or macOS"
    },
    {
      "evidence": [
        "https://github.com/tom-seddon/beeblink/blob/58776b038d1fe7494a2c15564b0a5e1b7860a928/README.md"
      ],
      "name": "BBC Micro link",
      "notes": "README recommends EEPROM or battery-backed write-protectable sideways RAM; no CPU or RAM minimum is stated.",
      "os": "BeebLink ROM plus Tube USB serial adapter or UPURS cable",
      "platform": "BBC Micro / BBC Master 128"
    },
    {
      "chipsets": [
        "Plus 1",
        "Advanced Plus 5",
        "Tube USB serial adapter PLD V3+"
      ],
      "evidence": [
        "https://github.com/tom-seddon/beeblink/blob/58776b038d1fe7494a2c15564b0a5e1b7860a928/README.md"
      ],
      "name": "Acorn Electron link",
      "notes": "README describes this as a DIY configuration; no CPU or RAM minimum is stated.",
      "platform": "Acorn Electron"
    }
  ],
  "source_cpu": [],
  "source_language": [
    "BBC filing-system behavior"
  ],
  "source_platforms": [
    "BBC Micro",
    "BBC Master 128",
    "Acorn Electron"
  ],
  "status": "Active host-server and BBC/Electron ROM system with documented hardware links and reproducible server/ROM build instructions; not independently built.",
  "subjects": [
    "BBC Micro",
    "BBC Master 128",
    "Acorn Electron"
  ],
  "tags": [
    "BBC Micro",
    "BBC Master",
    "Acorn Electron",
    "file server",
    "development tool"
  ],
  "target_cpu": [],
  "target_kinds": [
    "development-tool"
  ],
  "target_platforms": [
    "BBC Micro",
    "Acorn Electron",
    "Windows",
    "Linux",
    "macOS"
  ],
  "techniques": [
    "host-backed filing system",
    "Tube serial transport",
    "UPURS transport",
    "BBC ROM development",
    "multi-machine file sharing"
  ],
  "title": "BeebLink — BBC Micro and Electron host file server",
  "tool_kinds": [
    "development-environment",
    "disk-filesystem-tool"
  ],
  "types": [
    "host file server",
    "BBC filing system ROM",
    "retro-development bridge"
  ],
  "upstream_name": "BeebLink",
  "work_kinds": []
}
```

### Identity (reviewed)

BeebLink is a host file-storage system with a BBC/Electron ROM and transport-specific server components.
- https://github.com/tom-seddon/beeblink/blob/58776b038d1fe7494a2c15564b0a5e1b7860a928/README.md

### Classification (reviewed)

It qualifies as directly relevant retro-development and filing-system tooling, not a game reconstruction.
- https://github.com/tom-seddon/beeblink/blob/58776b038d1fe7494a2c15564b0a5e1b7860a928/README.md

### Source CPU (not-applicable)

There is no original binary subject whose CPU is being reconstructed; the project is a newly authored host/server and ROM tool.
- https://github.com/tom-seddon/beeblink/blob/58776b038d1fe7494a2c15564b0a5e1b7860a928/README.md

### Target CPU (no-evidence-found)

The reviewed README and ROM build document name BBC/Electron targets and 64tass but do not explicitly state the ROM output CPU; the value is not inferred from platform.
- https://github.com/tom-seddon/beeblink/blob/58776b038d1fe7494a2c15564b0a5e1b7860a928/README.md
- https://github.com/tom-seddon/beeblink/blob/58776b038d1fe7494a2c15564b0a5e1b7860a928/docs/build-rom.md

### Build (reviewed)

Primary documentation gives separate ROM and Node server build routes for Windows, macOS and Linux. Limitations: The tracker did not build the ROM/server or connect physical hardware.
- https://github.com/tom-seddon/beeblink/blob/58776b038d1fe7494a2c15564b0a5e1b7860a928/docs/build-rom.md
- https://github.com/tom-seddon/beeblink/blob/58776b038d1fe7494a2c15564b0a5e1b7860a928/docs/build-server.md

### Runtime profiles (reviewed)

Node.js 18.20+ and the distinct BBC, Electron and host prerequisites are explicit; no CPU or RAM minimum is stated.
- https://github.com/tom-seddon/beeblink/blob/58776b038d1fe7494a2c15564b0a5e1b7860a928/README.md
- https://github.com/tom-seddon/beeblink/blob/58776b038d1fe7494a2c15564b0a5e1b7860a928/docs/build-server.md

### AI (no-evidence-found)

No explicit development-AI attribution was found in the reviewed README or build documents; this does not establish non-use.
- https://github.com/tom-seddon/beeblink/blob/58776b038d1fe7494a2c15564b0a5e1b7860a928/README.md

### Relationships (reviewed)

TubeHost integration is documented, while BeebLink remains its own server/ROM project.
- https://github.com/tom-seddon/beeblink/blob/58776b038d1fe7494a2c15564b0a5e1b7860a928/README.md

## Wish — C64 and Amiga Gold Box save editor and automapper

Project ID: wish-gold-box-save-editor-automapper · Overall audit: reviewed

### Typed catalogue values

```json
{
  "ai": {
    "evidence": [
      "README explicitly states the source code was generated by Claude Code under human authorship of art and user-facing text."
    ],
    "tools": [
      "Claude Code"
    ],
    "usage": true
  },
  "build": {
    "byte_exact": null,
    "compilable": true,
    "playable": null,
    "runnable": true
  },
  "display_title": "Wish — C64 and Amiga Gold Box save editor and automapper",
  "id": "wish-gold-box-save-editor-automapper",
  "last_activity": "2026-10-18",
  "last_checked": "2026-11-02",
  "re_started": null,
  "reconstructed_languages": [
    "Python"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/malcyon/wish",
  "runtime_profiles": [
    {
      "evidence": [
        "https://github.com/malcyon/wish/blob/20aff7c9dd484347de64e1e7994380faf25e8af0/README.md"
      ],
      "name": "Linux application",
      "notes": "Gold Box game disks are required; no CPU or RAM minimum is stated.",
      "os": "Python 3.12 or later",
      "platform": "Linux"
    },
    {
      "evidence": [
        "https://github.com/malcyon/wish/blob/20aff7c9dd484347de64e1e7994380faf25e8af0/README.md"
      ],
      "name": "Live automapper",
      "notes": "The README documents the monitor/debugger connections and user-supplied game media; no CPU or RAM minimum is stated.",
      "os": "VICE for C64; WinUAE on Windows or patched FS-UAE on Linux for Amiga",
      "platform": "Windows or Linux host"
    }
  ],
  "source_cpu": [],
  "source_language": [
    "Gold Box save formats",
    "live emulator memory",
    "game resource data"
  ],
  "source_platforms": [
    "Commodore 64",
    "Amiga",
    "DOS"
  ],
  "status": "Active save editor and emulator-linked automapper backed by extensive C64, Amiga and DOS format/runtime research; not independently run.",
  "subjects": [
    "Pool of Radiance",
    "Curse of the Azure Bonds",
    "Secrets of the Silver Blades",
    "Pools of Darkness"
  ],
  "tags": [
    "Commodore 64",
    "Amiga",
    "DOS",
    "Gold Box",
    "save editor",
    "automapper",
    "Claude Code"
  ],
  "target_cpu": [],
  "target_kinds": [
    "development-tool"
  ],
  "target_platforms": [
    "Windows",
    "Linux"
  ],
  "techniques": [
    "save-format reconstruction",
    "live emulator memory inspection",
    "cross-platform save conversion",
    "resource-format analysis",
    "emulator debugger integration"
  ],
  "title": "Wish — C64 and Amiga Gold Box save editor and automapper",
  "tool_kinds": [
    "binary-analysis",
    "debugger"
  ],
  "types": [
    "save editor",
    "live automapper",
    "cross-platform data converter"
  ],
  "upstream_name": "Wish",
  "work_kinds": [
    "data-format-analysis"
  ]
}
```

### Identity (reviewed)

Wish is the canonical save editor and live automapper for four Gold Box titles across C64, Amiga and DOS.
- https://github.com/malcyon/wish/blob/20aff7c9dd484347de64e1e7994380faf25e8af0/README.md

### Classification (reviewed)

It qualifies as substantial binary/data analysis and emulator-linked archaeology tooling, not as a game port or reconstruction.
- https://github.com/malcyon/wish/blob/20aff7c9dd484347de64e1e7994380faf25e8af0/README.md
- https://github.com/malcyon/wish/blob/20aff7c9dd484347de64e1e7994380faf25e8af0/docs/README.md

### Source CPU (not-applicable)

The reviewed subjects are save records, resource data and live emulator memory across several ports rather than one original machine-code binary.
- https://github.com/malcyon/wish/blob/20aff7c9dd484347de64e1e7994380faf25e8af0/README.md

### Target CPU (not-applicable)

Wish edits/converts data and inspects emulator state; it does not emit a native retro executable with a target CPU.
- https://github.com/malcyon/wish/blob/20aff7c9dd484347de64e1e7994380faf25e8af0/README.md

### Build (reviewed)

The README documents pip installation on Linux and a Windows executable, plus emulator-specific live setup. Limitations: The tracker did not install Wish, open copyrighted media or attach to an emulator.
- https://github.com/malcyon/wish/blob/20aff7c9dd484347de64e1e7994380faf25e8af0/README.md

### Runtime profiles (reviewed)

Python 3.12+ on Linux and explicit VICE/WinUAE/patched-FS-UAE automapper routes are documented; no host CPU or RAM minimum is stated.
- https://github.com/malcyon/wish/blob/20aff7c9dd484347de64e1e7994380faf25e8af0/README.md

### AI (reviewed)

The README explicitly says Claude Code generated the source while humans created art and user-facing text.
- https://github.com/malcyon/wish/blob/20aff7c9dd484347de64e1e7994380faf25e8af0/README.md

### Relationships (reviewed)

Wish uses VICE's binary monitor, WinUAE and Graham Bates' patched FS-UAE/uae-dap route; these remain dependencies rather than embedded subprojects.
- https://github.com/malcyon/wish/blob/20aff7c9dd484347de64e1e7994380faf25e8af0/README.md

## beeb-niccc — BBC Micro STNICCC-2000 recreation

Project ID: stnicc-beeb-bbc-demo-recreation · Overall audit: partial

### Typed catalogue values

```json
{
  "ai": {
    "evidence": [
      "The reviewed v1.2 commit explicitly credits Claude Opus 5.5 and links its Claude Code session: https://github.com/kieranhj/stnicc-beeb/commit/9a9cce3a80e71648fe7396552c4531a8b64a4a08"
    ],
    "tools": [
      "Claude Code"
    ],
    "usage": true
  },
  "build": {
    "byte_exact": null,
    "compilable": true,
    "playable": null,
    "runnable": true
  },
  "display_title": "beeb-niccc — BBC Micro STNICCC-2000 recreation",
  "id": "stnicc-beeb-bbc-demo-recreation",
  "last_activity": "2026-10-19",
  "last_checked": "2026-11-02",
  "re_started": null,
  "reconstructed_languages": [
    "6502 assembly",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/kieranhj/stnicc-beeb",
  "runtime_profiles": [
    {
      "evidence": [
        "https://github.com/kieranhj/stnicc-beeb/blob/9a9cce3a80e71648fe7396552c4531a8b64a4a08/Makefile"
      ],
      "name": "BBC disc build",
      "notes": "The Makefile builds DSD images and names B/Acorn 1770 and Master 128 emulator configurations; no minimum CPU, RAM or model is claimed.",
      "os": "DFS-compatible disc environment",
      "platform": "BBC Micro / BBC Master 128"
    }
  ],
  "source_cpu": [],
  "source_language": [
    "STNICCC scene stream"
  ],
  "source_platforms": [
    "Atari ST"
  ],
  "status": "Released BBC Micro recreation of the STNICCC-2000 demo with BeebAsm source, stream encoders and BBC/NuLA/CPC-palette variants; not independently assembled or run.",
  "subjects": [
    "STNICCC-2000"
  ],
  "tags": [
    "BBC Micro",
    "BBC Master",
    "Atari ST",
    "6502",
    "demo",
    "fan conversion"
  ],
  "target_cpu": [
    "6502"
  ],
  "target_kinds": [
    "demo"
  ],
  "target_platforms": [
    "BBC Micro",
    "BBC Master 128"
  ],
  "techniques": [
    "6502 assembly",
    "polygon stream re-encoding",
    "double buffering",
    "disc streaming",
    "NuLA display adaptation"
  ],
  "title": "beeb-niccc — BBC Micro STNICCC-2000 recreation",
  "tool_kinds": [],
  "types": [
    "fan conversion",
    "demo recreation"
  ],
  "upstream_name": "beeb-niccc",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

The repository is the BBC Micro recreation of STNICCC-2000 released as beeb-niccc.
- https://github.com/kieranhj/stnicc-beeb/blob/9a9cce3a80e71648fe7396552c4531a8b64a4a08/README.md

### Classification (reviewed)

This is a substantial native fan recreation/conversion and demo production, not a disassembly or binary-derived source reconstruction.
- https://github.com/kieranhj/stnicc-beeb/blob/9a9cce3a80e71648fe7396552c4531a8b64a4a08/README.md
- https://github.com/kieranhj/stnicc-beeb/blob/9a9cce3a80e71648fe7396552c4531a8b64a4a08/stnicc-beeb.asm

### Source CPU (not-applicable)

The BBC work consumes an STNICCC scene stream rather than reconstructing the original demo executable, so an original-binary source CPU is not assigned.
- https://github.com/kieranhj/stnicc-beeb/blob/9a9cce3a80e71648fe7396552c4531a8b64a4a08/stnicc-beeb.asm

### Target CPU (reviewed)

The build labels the source as BeebAsm/.6502 assembly and assembles the BBC disc output from that code.
- https://github.com/kieranhj/stnicc-beeb/blob/9a9cce3a80e71648fe7396552c4531a8b64a4a08/Makefile
- https://github.com/kieranhj/stnicc-beeb/blob/9a9cce3a80e71648fe7396552c4531a8b64a4a08/stnicc-beeb.asm

### Build (reviewed)

The Makefile documents BeebAsm, Exomizer and Python stages that build SSD/DSD release media and test routes through b2/jsbeeb. Limitations: The tracker did not assemble the demo, generate media or run an emulator.
- https://github.com/kieranhj/stnicc-beeb/blob/9a9cce3a80e71648fe7396552c4531a8b64a4a08/Makefile

### Runtime profiles (no-evidence-found)

BBC and Master emulator configurations are named, but the reviewed primary files do not state a minimum model, RAM amount or chipset requirement.
- https://github.com/kieranhj/stnicc-beeb/blob/9a9cce3a80e71648fe7396552c4531a8b64a4a08/Makefile

### AI (reviewed)

The reviewed v1.2 commit explicitly credits Claude Opus 5.5 and a Claude Code session.
- https://github.com/kieranhj/stnicc-beeb/commit/9a9cce3a80e71648fe7396552c4531a8b64a4a08

### Relationships (reviewed)

The repository adapts the STNICCC-2000 scene for BBC hardware and includes its own encoders/build; it is not a fork or mirror of the original Atari ST binary.
- https://github.com/kieranhj/stnicc-beeb/blob/9a9cce3a80e71648fe7396552c4531a8b64a4a08/README.md
- https://github.com/kieranhj/stnicc-beeb/blob/9a9cce3a80e71648fe7396552c4531a8b64a4a08/Makefile

## Legacy89DiskKit — Japanese retro disk-image toolkit

Project ID: legacy89diskkit-japanese-disk-toolkit · Overall audit: reviewed

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
    "runnable": true
  },
  "display_title": "Legacy89DiskKit — Japanese retro disk-image toolkit",
  "id": "legacy89diskkit-japanese-disk-toolkit",
  "last_activity": "2026-04-10",
  "last_checked": "2026-11-02",
  "re_started": null,
  "reconstructed_languages": [
    "C#",
    "C++"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/medamap/Legacy89DiskKit",
  "runtime_profiles": [
    {
      "evidence": [
        "https://github.com/medamap/Legacy89DiskKit/blob/40bd90edc4109ba8985f135918f9b31d500f8720/README.md"
      ],
      "name": "Legacy89DiskKit CLI",
      "notes": "README documents build/install routes but states no host CPU, RAM or OS-version minimum.",
      "os": "Managed build scripts; CMake optionally enables the native companion",
      "platform": "Windows, Linux or macOS"
    }
  ],
  "source_cpu": [],
  "source_language": [
    "D88 disk images",
    "D77 disk images",
    "2D raw disk images",
    "DSK raw disk images",
    "legacy filesystems"
  ],
  "source_platforms": [
    "Sharp X1",
    "PC-8801",
    "MSX"
  ],
  "status": "Active CLI and library for inspecting, creating, formatting, copying and boot-metadata analysis of Japanese legacy disk formats; not independently built or tested.",
  "subjects": [
    "D88 disk images",
    "D77 disk images",
    "Sharp X1 Hu-BASIC",
    "Sharp X1 X-DOS",
    "PC-8801 N88-BASIC",
    "MSX-DOS"
  ],
  "tags": [
    "Sharp X1",
    "PC-8801",
    "MSX",
    "D88",
    "D77",
    "disk image",
    "filesystem tool"
  ],
  "target_cpu": [],
  "target_kinds": [
    "development-tool"
  ],
  "target_platforms": [
    "Windows",
    "Linux",
    "macOS"
  ],
  "techniques": [
    "disk-container parsing",
    "legacy filesystem reconstruction",
    "boot metadata inspection",
    "sector import/export",
    "managed/native parity testing"
  ],
  "title": "Legacy89DiskKit — Japanese retro disk-image toolkit",
  "tool_kinds": [
    "disk-filesystem-tool"
  ],
  "types": [
    "disk image toolkit",
    "filesystem utility",
    "native bridge"
  ],
  "upstream_name": "Legacy89DiskKit",
  "work_kinds": [
    "data-format-analysis"
  ]
}
```

### Identity (reviewed)

Legacy89DiskKit is the canonical CLI/library for Japanese 8-bit and 16-bit disk container and filesystem workflows.
- https://github.com/medamap/Legacy89DiskKit/blob/40bd90edc4109ba8985f135918f9b31d500f8720/README.md

### Classification (reviewed)

It qualifies as disk/filesystem analysis and development tooling, not as an emulator or reconstructed native application.
- https://github.com/medamap/Legacy89DiskKit/blob/40bd90edc4109ba8985f135918f9b31d500f8720/README.md

### Source CPU (not-applicable)

The reviewed inputs are disk containers, filesystems and boot metadata rather than one original machine-code binary.
- https://github.com/medamap/Legacy89DiskKit/blob/40bd90edc4109ba8985f135918f9b31d500f8720/README.md

### Target CPU (not-applicable)

The toolkit manipulates disk data and does not emit a native retro executable with a target CPU.
- https://github.com/medamap/Legacy89DiskKit/blob/40bd90edc4109ba8985f135918f9b31d500f8720/README.md

### Build (reviewed)

Shell and PowerShell build scripts run managed builds/tests and conditionally build/test the C++ library through CMake. Limitations: The tracker did not build either implementation or open a disk image.
- https://github.com/medamap/Legacy89DiskKit/blob/40bd90edc4109ba8985f135918f9b31d500f8720/README.md

### Runtime profiles (reviewed)

Windows, Linux and macOS install/build routes are documented; no host CPU, RAM or OS-version minimum is stated.
- https://github.com/medamap/Legacy89DiskKit/blob/40bd90edc4109ba8985f135918f9b31d500f8720/README.md

### AI (no-evidence-found)

No explicit development-AI attribution was found in the reviewed README or platform support document; agent-oriented planning filenames alone are not treated as contribution evidence.
- https://github.com/medamap/Legacy89DiskKit/blob/40bd90edc4109ba8985f135918f9b31d500f8720/README.md
- https://github.com/medamap/Legacy89DiskKit/blob/40bd90edc4109ba8985f135918f9b31d500f8720/Documents/guides/Platform_Support_Status.md

### Relationships (reviewed)

The C# CLI/library and documented C++ native bridge are one product family in the same repository, not separate titled projects.
- https://github.com/medamap/Legacy89DiskKit/blob/40bd90edc4109ba8985f135918f9b31d500f8720/README.md

## Nectaris — browser-based mechanics reconstruction and remake

Project ID: nectaris-javascript-remake · Overall audit: partial

### Typed catalogue values

```json
{
  "ai": {
    "evidence": [
      "README explicitly labels fifteen scenarios and three 16-map campaigns as AI-made; no specific generation tool is named."
    ],
    "tools": [],
    "usage": true
  },
  "build": {
    "byte_exact": null,
    "compilable": true,
    "playable": true,
    "runnable": true
  },
  "display_title": "Nectaris — browser-based mechanics reconstruction and remake",
  "id": "nectaris-javascript-remake",
  "last_activity": "2026-10-12",
  "last_checked": "2026-11-02",
  "re_started": null,
  "reconstructed_languages": [
    "JavaScript",
    "HTML",
    "CSS"
  ],
  "record_class": "subject",
  "repo": "https://github.com/ernop/nectaris-remake",
  "runtime_profiles": [
    {
      "evidence": [
        "https://github.com/ernop/nectaris-remake/blob/3a749261455c53f63909b0928b0cd3bc429d9a24/README.md"
      ],
      "name": "Static browser build",
      "notes": "README states there is no build step or dependency; no browser version, CPU or RAM minimum is stated.",
      "os": "Static files served over HTTP/HTTPS or opened locally",
      "platform": "Web browser"
    }
  ],
  "source_cpu": [],
  "source_language": [
    "manuals",
    "community mechanics research",
    "Windows executable observations"
  ],
  "source_platforms": [
    "PC Engine",
    "TurboGrafx-16"
  ],
  "status": "From-scratch browser remake with documented PCE-targeted mechanics research, Windows-executable observations and explicit remaining fidelity gaps; not a source port or decompilation.",
  "subjects": [
    "Nectaris",
    "Military Madness"
  ],
  "tags": [
    "PC Engine",
    "TurboGrafx-16",
    "Nectaris",
    "Military Madness",
    "remake",
    "gameplay reconstruction"
  ],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Web browser"
  ],
  "techniques": [
    "manual-based rule reconstruction",
    "original-executable observation",
    "combat formula reconstruction",
    "deterministic regression fixtures",
    "map format conversion"
  ],
  "title": "Nectaris — browser-based mechanics reconstruction and remake",
  "tool_kinds": [],
  "types": [
    "from-scratch remake",
    "gameplay mechanics reconstruction",
    "browser game"
  ],
  "upstream_name": "Nectaris",
  "work_kinds": [
    "reimplementation",
    "subsystem-reconstruction"
  ]
}
```

### Identity (reviewed)

This is the canonical from-scratch JavaScript remake targeting 1989 Japanese PC Engine Nectaris mechanics.
- https://github.com/ernop/nectaris-remake/blob/3a749261455c53f63909b0928b0cd3bc429d9a24/README.md
- https://github.com/ernop/nectaris-remake/blob/3a749261455c53f63909b0928b0cd3bc429d9a24/MECHANICS.md

### Classification (reviewed)

It qualifies as a substantial researched remake and gameplay reconstruction; the project explicitly says it is from scratch and is not labelled a binary-derived decompilation or port.
- https://github.com/ernop/nectaris-remake/blob/3a749261455c53f63909b0928b0cd3bc429d9a24/README.md

### Source CPU (no-evidence-found)

The reviewed primary documents name the PC Engine target but do not state an original CPU architecture; no CPU is inferred from platform.
- https://github.com/ernop/nectaris-remake/blob/3a749261455c53f63909b0928b0cd3bc429d9a24/MECHANICS.md

### Target CPU (not-applicable)

The portable browser implementation does not establish one native output CPU.
- https://github.com/ernop/nectaris-remake/blob/3a749261455c53f63909b0928b0cd3bc429d9a24/README.md

### Build (reviewed)

The project is documented as dependency-free static files with no build step and a Node test suite. Limitations: The tracker did not host, run or test the remake and did not execute original game binaries.
- https://github.com/ernop/nectaris-remake/blob/3a749261455c53f63909b0928b0cd3bc429d9a24/README.md

### Runtime profiles (no-evidence-found)

A static-browser route is documented, but no minimum browser version, host CPU or RAM is stated.
- https://github.com/ernop/nectaris-remake/blob/3a749261455c53f63909b0928b0cd3bc429d9a24/README.md

### AI (reviewed)

The README explicitly labels fifteen maps and three campaigns as AI-made but does not name the generation tool; this is recorded narrowly as content-development AI evidence.
- https://github.com/ernop/nectaris-remake/blob/3a749261455c53f63909b0928b0cd3bc429d9a24/README.md

### Relationships (reviewed)

The remake uses manuals, community research, Windows-port observations and imported campaign data as references while remaining an independent implementation.
- https://github.com/ernop/nectaris-remake/blob/3a749261455c53f63909b0928b0cd3bc429d9a24/MECHANICS.md

## Sources

```json
[
  {
    "id": "github-mattgodbolt-jsbeeb",
    "kind": "github-repository",
    "reason": "Canonical BBC Micro-family JavaScript emulator, debugger and media-analysis environment.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/mattgodbolt/jsbeeb"
  },
  {
    "id": "github-kieranhj-beebjit-libretro",
    "kind": "github-repository",
    "reason": "beebjit libretro glue, ARM64/x64 JIT runtime evidence and Claude attribution reviewed.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/kieranhj/beebjit-libretro"
  },
  {
    "id": "github-tom-seddon-beeblink",
    "kind": "github-repository",
    "reason": "BBC/Electron host file server, ROM build and hardware transport requirements reviewed.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/tom-seddon/beeblink"
  },
  {
    "id": "github-malcyon-wish",
    "kind": "github-repository",
    "reason": "Gold Box save-format archaeology, live automapping, runtime routes and explicit Claude Code use reviewed.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/malcyon/wish"
  },
  {
    "id": "github-kieranhj-stnicc-beeb",
    "kind": "github-repository",
    "reason": "BBC Micro STNICCC recreation, BeebAsm build and target CPU evidence reviewed.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/kieranhj/stnicc-beeb"
  },
  {
    "id": "github-medamap-legacy89diskkit",
    "kind": "github-repository",
    "reason": "Japanese D88/D77/raw disk and filesystem tooling reviewed across Sharp X1, PC-8801 and MSX support.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/medamap/Legacy89DiskKit"
  },
  {
    "id": "github-ernop-nectaris-remake",
    "kind": "github-repository",
    "reason": "From-scratch Nectaris remake and documented mechanics/executable-observation research reviewed.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/ernop/nectaris-remake"
  },
  {
    "id": "fresh-search-2026-11-02-pc98-lynx-oric",
    "kind": "named-source",
    "reason": "Rotated GitHub code/README search slice. TH04 resolved to an existing promoted record; Legacy89DiskKit and the Nectaris false-positive were reviewed at their demonstrated scopes; Lynx and Oric results yielded no additional deep-review candidate.",
    "review_state": "substantially-reviewed",
    "source": "PC-98 disassembly reconstruction; Atari Lynx toolchain homebrew; Oric disassembly reassembly toolchain"
  }
]
```

## Source updates

```json
[
  {
    "id": "github-kieranhj",
    "last_reviewed": "2026-11-02"
  },
  {
    "id": "github-tom-seddon",
    "last_reviewed": "2026-11-02"
  }
]
```

## Task updates

```json
[
  {
    "id": "task-follow-credited-predecessors-and-related-disassemblies-around-bbc-micro-",
    "last_reviewed": "2026-11-02",
    "notes_append": "Reviewed unrepresented Acorn/BBC graph entries: promoted jsbeeb, beebjit-libretro, BeebLink and beeb-niccc with explicit architecture/runtime/classification boundaries. The wider predecessor and profile graph remains open.",
    "state": "in-progress"
  }
]
```

## Decisions

```json
[
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/mattgodbolt/jsbeeb/blob/178031ec9e7420a0965981f7f7877df35886fe0c/README.md",
      "https://github.com/mattgodbolt/jsbeeb/blob/178031ec9e7420a0965981f7f7877df35886fe0c/src/models.js"
    ],
    "id": "discovery-2026-11-02-jsbeeb-promoted",
    "project_ids": [
      "jsbeeb-bbc-micro-emulator"
    ],
    "reason": "Canonical BBC Micro-family browser/desktop emulator with integrated debugger, media analysis, rewind and explicit 6502-family model coverage.",
    "source_ids": [
      "github-mattgodbolt-jsbeeb",
      "github-kieranhj"
    ],
    "title": "jsbeeb",
    "url": "https://github.com/mattgodbolt/jsbeeb"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/kieranhj/beebjit-libretro/blob/763450c5611d54b71b6bd68077bc7385e62af2bf/README.md"
    ],
    "id": "discovery-2026-11-02-beebjit-libretro-promoted",
    "project_ids": [
      "beebjit-libretro-bbc-micro-core"
    ],
    "reason": "Distinct libretro integration for beebjit with explicit JIT architectures, tested handheld target and Claude-assisted provenance.",
    "source_ids": [
      "github-kieranhj-beebjit-libretro",
      "github-kieranhj"
    ],
    "title": "beebjit-libretro",
    "url": "https://github.com/kieranhj/beebjit-libretro"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/tom-seddon/beeblink/blob/58776b038d1fe7494a2c15564b0a5e1b7860a928/README.md"
    ],
    "id": "discovery-2026-11-02-beeblink-promoted",
    "project_ids": [
      "beeblink-bbc-file-server"
    ],
    "reason": "Substantial BBC/Electron development filing system with host server, native ROM and documented physical transports.",
    "source_ids": [
      "github-tom-seddon-beeblink",
      "github-tom-seddon"
    ],
    "title": "BeebLink",
    "url": "https://github.com/tom-seddon/beeblink"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/malcyon/wish/blob/20aff7c9dd484347de64e1e7994380faf25e8af0/README.md",
      "https://github.com/malcyon/wish/blob/20aff7c9dd484347de64e1e7994380faf25e8af0/docs/README.md"
    ],
    "id": "discovery-2026-11-02-wish-promoted",
    "project_ids": [
      "wish-gold-box-save-editor-automapper"
    ],
    "reason": "Substantial C64/Amiga/DOS Gold Box save-format analysis, cross-port conversion and live emulator-memory automapping tool.",
    "source_ids": [
      "github-malcyon-wish"
    ],
    "title": "Wish",
    "url": "https://github.com/malcyon/wish"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/kieranhj/stnicc-beeb/blob/9a9cce3a80e71648fe7396552c4531a8b64a4a08/README.md",
      "https://github.com/kieranhj/stnicc-beeb/blob/9a9cce3a80e71648fe7396552c4531a8b64a4a08/Makefile"
    ],
    "id": "discovery-2026-11-02-stnicc-beeb-promoted",
    "project_ids": [
      "stnicc-beeb-bbc-demo-recreation"
    ],
    "reason": "Released and source-backed BBC Micro fan recreation of STNICCC-2000 with native BeebAsm renderer and stream tooling.",
    "source_ids": [
      "github-kieranhj-stnicc-beeb",
      "github-kieranhj"
    ],
    "title": "beeb-niccc",
    "url": "https://github.com/kieranhj/stnicc-beeb"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/medamap/Legacy89DiskKit/blob/40bd90edc4109ba8985f135918f9b31d500f8720/README.md",
      "https://github.com/medamap/Legacy89DiskKit/blob/40bd90edc4109ba8985f135918f9b31d500f8720/Documents/guides/Platform_Support_Status.md"
    ],
    "id": "discovery-2026-11-02-legacy89diskkit-promoted",
    "project_ids": [
      "legacy89diskkit-japanese-disk-toolkit"
    ],
    "reason": "Japanese legacy-disk container/filesystem toolkit with tested Sharp X1, PC-8801 and MSX workflows.",
    "source_ids": [
      "github-medamap-legacy89diskkit",
      "fresh-search-2026-11-02-pc98-lynx-oric"
    ],
    "title": "Legacy89DiskKit",
    "url": "https://github.com/medamap/Legacy89DiskKit"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/ernop/nectaris-remake/blob/3a749261455c53f63909b0928b0cd3bc429d9a24/README.md",
      "https://github.com/ernop/nectaris-remake/blob/3a749261455c53f63909b0928b0cd3bc429d9a24/MECHANICS.md"
    ],
    "id": "discovery-2026-11-02-nectaris-promoted",
    "project_ids": [
      "nectaris-javascript-remake"
    ],
    "reason": "From-scratch browser remake with extensive manual/community research, Windows-executable observations and explicit remaining fidelity limits.",
    "source_ids": [
      "github-ernop-nectaris-remake",
      "fresh-search-2026-11-02-pc98-lynx-oric"
    ],
    "title": "Nectaris",
    "url": "https://github.com/ernop/nectaris-remake"
  }
]
```

## Source ids

```json
[
  "github-kieranhj",
  "github-tom-seddon"
]
```

## Research event notes

The CPU audit queue returned zero unresolved source/target CPU areas, so no CPU value was inferred merely to satisfy a quota. The older Acorn/BBC profile task was selected from the canonical queue. Reviewed candidate URLs: mattgodbolt/jsbeeb, kieranhj/beebjit-libretro, tom-seddon/beeblink, malcyon/wish, kieranhj/stnicc-beeb, medamap/Legacy89DiskKit and ernop/nectaris-remake were promoted; N0zoM1z0/th04 resolved to the existing promoted TH04 record and was not duplicated. Fresh GitHub code/README searches were exactly 'PC-98 disassembly reconstruction', 'Atari Lynx toolchain homebrew', and 'Oric disassembly reassembly toolchain'. The PC-98 route surfaced the already indexed TH04 and Legacy89DiskKit; the latter qualified on its documented Japanese disk/filesystem support. The Lynx and Oric routes produced only broad indexes, emulator distributions, unrelated modern code or already indexed references, with no additional candidate selected for deep review. STNICCC is recorded as a BBC fan recreation, Nectaris as a from-scratch researched remake, and neither is relabelled as binary-derived reverse engineering. Read-only review: no emulator, ROM, disk image, compiler, game, server or hardware was run.
