# Add ten verified Amiga, Atari ST, C64 and BBC Micro projects

Add ten verified Amiga, Atari ST, C64 and BBC Micro projects

Date: 2026-10-15 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- amiga-mcp-zz9000-debugger / Runtime profiles (no-evidence-found): The inspected documentation and build/implementation samples do not establish a complete minimum runnable hardware profile. No RAM or minimum CPU is inferred from platform or compiler target.
- amiga-mcp-zz9000-debugger / AI (no-evidence-found): No explicit development-AI contribution attribution was found in the inspected documentation, implementation/build samples and latest default-branch commit. This bounded review does not prove non-use; integration/configuration files are not contribution evidence.
- dctelnet-amiga-maintained-source / AI (no-evidence-found): No explicit development-AI contribution attribution was found in the inspected documentation, implementation/build samples and latest default-branch commit. This bounded review does not prove non-use; integration/configuration files are not contribution evidence.
- libcmini-atari-runtime / Runtime profiles (no-evidence-found): The inspected documentation and build/implementation samples do not establish a complete minimum runnable hardware profile. No RAM or minimum CPU is inferred from platform or compiler target.
- libcmini-atari-runtime / AI (no-evidence-found): No explicit development-AI contribution attribution was found in the inspected documentation, implementation/build samples and latest default-branch commit. This bounded review does not prove non-use; integration/configuration files are not contribution evidence.
- adpcm-68k-codec-replayer / AI (no-evidence-found): No explicit development-AI contribution attribution was found in the inspected documentation, implementation/build samples and latest default-branch commit. This bounded review does not prove non-use; integration/configuration files are not contribution evidence.
- sndh-ym-archive-player / Runtime profiles (no-evidence-found): The inspected documentation and build/implementation samples do not establish a complete minimum runnable hardware profile. No RAM or minimum CPU is inferred from platform or compiler target.
- sndh-ym-archive-player / AI (no-evidence-found): No explicit development-AI contribution attribution was found in the inspected documentation, implementation/build samples and latest default-branch commit. This bounded review does not prove non-use; integration/configuration files are not contribution evidence.
- rvncd-amiga-vnc-server / Runtime profiles (no-evidence-found): The inspected documentation and build/implementation samples do not establish a complete minimum runnable hardware profile. No RAM or minimum CPU is inferred from platform or compiler target.
- rvncd-amiga-vnc-server / AI (no-evidence-found): No explicit development-AI contribution attribution was found in the inspected documentation, implementation/build samples and latest default-branch commit. This bounded review does not prove non-use; integration/configuration files are not contribution evidence.
- c64-monster-attack / Runtime profiles (no-evidence-found): The inspected documentation and build/implementation samples do not establish a complete minimum runnable hardware profile. No RAM or minimum CPU is inferred from platform or compiler target.
- c64-monster-attack / AI (no-evidence-found): No explicit development-AI contribution attribution was found in the inspected documentation, implementation/build samples and latest default-branch commit. This bounded review does not prove non-use; integration/configuration files are not contribution evidence.
- storm-chase-c64-source / Runtime profiles (no-evidence-found): The inspected documentation and build/implementation samples do not establish a complete minimum runnable hardware profile. No RAM or minimum CPU is inferred from platform or compiler target.
- storm-chase-c64-source / AI (no-evidence-found): No explicit development-AI contribution attribution was found in the inspected documentation, implementation/build samples and latest default-branch commit. This bounded review does not prove non-use; integration/configuration files are not contribution evidence.
- tigermoth-c64-source / Runtime profiles (no-evidence-found): The inspected documentation and build/implementation samples do not establish a complete minimum runnable hardware profile. No RAM or minimum CPU is inferred from platform or compiler target.
- tigermoth-c64-source / AI (no-evidence-found): No explicit development-AI contribution attribution was found in the inspected documentation, implementation/build samples and latest default-branch commit. This bounded review does not prove non-use; integration/configuration files are not contribution evidence.

## Lander: BBC Micro port of the Archimedes demo

Project ID: lander-bbc-micro-ebenupton · Overall audit: partial

### Typed catalogue values

```json
{
  "ai": {
    "evidence": [
      {
        "detail": "Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>",
        "type": "commit",
        "url": "https://github.com/ebenupton/lander/commit/8f2f11833d28254719264e496bd2f74bec02700c"
      }
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
  "display_title": "Lander: BBC Micro port of the Archimedes demo",
  "id": "lander-bbc-micro-ebenupton",
  "last_activity": null,
  "last_checked": "2026-10-15",
  "re_started": null,
  "reconstructed_languages": [
    "6502 assembly",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/ebenupton/lander",
  "runtime_profiles": [
    {
      "cpu_family": "6502",
      "evidence": [
        "https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/README.md"
      ],
      "min_cpu": "6502",
      "name": "Upstream Model B requirements",
      "notes": "Model B with 64 KB sideways RAM: four writable 16 KB banks, ROMSEL or Watford/Solidisk write-select. This is additional banked RAM, not a claimed total RAM minimum. README recommends BBC B with 8271 (DFS 1.2) in jsbeeb.",
      "os": "DFS",
      "platform": "BBC Micro"
    }
  ],
  "source_cpu": [
    "ARM"
  ],
  "source_language": [
    "ARM assembly"
  ],
  "source_platforms": [
    "Acorn Archimedes"
  ],
  "status": "Primary source and build workflow reviewed; independent execution unverified",
  "subjects": [
    "Lander for the BBC Micro"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
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
  "title": "Lander for the BBC Micro",
  "tool_kinds": [],
  "types": [
    "native port"
  ],
  "upstream_name": "Lander for the BBC Micro",
  "work_kinds": [
    "reverse-engineering-derived-port"
  ]
}
```

### Identity (reviewed)

Eben Upton ports David Braben's 1987 Lander demo, including landscape, ship, flight model, landing, fuel, map and sound.
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/README.md
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/src/land.s
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/ref/lander/NOTES.md
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/ref/lander/flight.py
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/build.sh

### Classification (reviewed)

Native 6502 implementation informed by Mark Moxon's annotated ARM reconstruction; not an original-source release or an embedded ARM emulation host.
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/README.md
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/src/land.s
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/ref/lander/NOTES.md
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/ref/lander/flight.py
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/build.sh

### Source CPU (reviewed)

ref/lander/NOTES.md identifies Lander.arm as the reconstructed Archimedes source, and flight.py explicitly transcribes its routines and 32-bit arithmetic. ARM source and 6502 output are distinct.
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/README.md
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/src/land.s
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/ref/lander/NOTES.md
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/ref/lander/flight.py
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/build.sh

### Target CPU (reviewed)

README explicitly targets a 2 MHz 6502; src/land.s implements the native renderer and sideways-RAM loader.
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/README.md
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/src/land.s
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/ref/lander/NOTES.md
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/ref/lander/flight.py
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/build.sh

### Build (reviewed)

README supplies lander.ssd and cc65/Python/numpy build instructions, with py65 reference comparisons. Its deterministic match is to the port's checked-in disk, not the original Archimedes executable. No independent compilation, execution, gameplay or byte comparison was performed; all four build flags remain unknown.
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/README.md
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/src/land.s
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/ref/lander/NOTES.md
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/ref/lander/flight.py
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/build.sh

### Runtime profiles (reviewed)

README requires BBC Micro Model B, four writable 16 KB sideways-RAM banks and DFS. No independent hardware validation.
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/README.md

### AI (reviewed)

The inspected head commit explicitly credits Claude Fable 5.1. This applies to Upton's port, independently of the predecessor's AI policy.
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/README.md
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/src/land.s
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/ref/lander/NOTES.md
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/ref/lander/flight.py
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/build.sh
- https://github.com/ebenupton/lander/commit/8f2f11833d28254719264e496bd2f74bec02700c

### Relationships (reviewed)

README and ref/lander/NOTES.md credit Mark Moxon's lander-source-code-acorn-archimedes and lander.bbcelite.com; loader and disk builder derive from ebenupton/beebgame. No blanket licensing claim is made. The repository URL and title were compared with the current catalogue; no equivalent project record was found.
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/README.md
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/src/land.s
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/ref/lander/NOTES.md
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/ref/lander/flight.py
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/build.sh

## Amiga MCP Debugger: cooperative ZZ9000 ARM debugging

Project ID: amiga-mcp-zz9000-debugger · Overall audit: partial

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
  "display_title": "Amiga MCP Debugger: cooperative ZZ9000 ARM debugging",
  "id": "amiga-mcp-zz9000-debugger",
  "last_activity": null,
  "last_checked": "2026-10-15",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Python"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/SkiltonUSA/Amiga-MCP-Debugger",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source and build workflow reviewed; independent execution unverified",
  "subjects": [],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "m68k",
    "ARM Cortex-A9"
  ],
  "target_kinds": [],
  "target_platforms": [
    "Amiga",
    "macOS"
  ],
  "techniques": [],
  "title": "Amiga MCP Debugger",
  "tool_kinds": [
    "debugger",
    "automation",
    "development-environment"
  ],
  "types": [
    "debugger extension"
  ],
  "upstream_name": "Amiga MCP Debugger",
  "work_kinds": []
}
```

### Identity (reviewed)

Extends Amiga DevBench with instrumented ZZ9000 ARM debugging, shared-memory computation and integrated fractal demonstrations.
- https://github.com/SkiltonUSA/Amiga-MCP-Debugger/blob/3acafebba8951f60e85a941b4c8cfb60be611002/README.md
- https://github.com/SkiltonUSA/Amiga-MCP-Debugger/blob/3acafebba8951f60e85a941b4c8cfb60be611002/scripts/build_arm_debug.py
- https://github.com/SkiltonUSA/Amiga-MCP-Debugger/blob/3acafebba8951f60e85a941b4c8cfb60be611002/scripts/build_zz9000_debug.py
- https://github.com/SkiltonUSA/Amiga-MCP-Debugger/blob/3acafebba8951f60e85a941b4c8cfb60be611002/docs/amiga-arm-debugging.md

### Classification (reviewed)

Tooling with cooperative checkpoints, watched memory and logs; does not attach to arbitrary ARM code or provide instruction-level stepping.
- https://github.com/SkiltonUSA/Amiga-MCP-Debugger/blob/3acafebba8951f60e85a941b4c8cfb60be611002/README.md
- https://github.com/SkiltonUSA/Amiga-MCP-Debugger/blob/3acafebba8951f60e85a941b4c8cfb60be611002/scripts/build_arm_debug.py
- https://github.com/SkiltonUSA/Amiga-MCP-Debugger/blob/3acafebba8951f60e85a941b4c8cfb60be611002/scripts/build_zz9000_debug.py
- https://github.com/SkiltonUSA/Amiga-MCP-Debugger/blob/3acafebba8951f60e85a941b4c8cfb60be611002/docs/amiga-arm-debugging.md

### Source CPU (not-applicable)

This is newly authored native software or development tooling, not analysis of a predecessor binary. Source platform/CPU/language are intentionally empty; output architecture is recorded separately.
- https://github.com/SkiltonUSA/Amiga-MCP-Debugger/blob/3acafebba8951f60e85a941b4c8cfb60be611002/README.md
- https://github.com/SkiltonUSA/Amiga-MCP-Debugger/blob/3acafebba8951f60e85a941b4c8cfb60be611002/scripts/build_arm_debug.py
- https://github.com/SkiltonUSA/Amiga-MCP-Debugger/blob/3acafebba8951f60e85a941b4c8cfb60be611002/scripts/build_zz9000_debug.py
- https://github.com/SkiltonUSA/Amiga-MCP-Debugger/blob/3acafebba8951f60e85a941b4c8cfb60be611002/docs/amiga-arm-debugging.md

### Target CPU (reviewed)

Build scripts explicitly target ARM Cortex-A9 and m68k-amigaos-gcc with 68020/68030 flags. Tested 68060 hardware is not inferred as a universal minimum.
- https://github.com/SkiltonUSA/Amiga-MCP-Debugger/blob/3acafebba8951f60e85a941b4c8cfb60be611002/README.md
- https://github.com/SkiltonUSA/Amiga-MCP-Debugger/blob/3acafebba8951f60e85a941b4c8cfb60be611002/scripts/build_arm_debug.py
- https://github.com/SkiltonUSA/Amiga-MCP-Debugger/blob/3acafebba8951f60e85a941b4c8cfb60be611002/scripts/build_zz9000_debug.py
- https://github.com/SkiltonUSA/Amiga-MCP-Debugger/blob/3acafebba8951f60e85a941b4c8cfb60be611002/docs/amiga-arm-debugging.md

### Build (reviewed)

Upstream reports physical A4000TX/TF4060/ZZ9000 acceptance, release artifacts and native tests; developer builds require the pinned bridge/SDK and firmware environment. No independent compilation, execution, gameplay or byte comparison was performed; all four build flags remain unknown.
- https://github.com/SkiltonUSA/Amiga-MCP-Debugger/blob/3acafebba8951f60e85a941b4c8cfb60be611002/README.md
- https://github.com/SkiltonUSA/Amiga-MCP-Debugger/blob/3acafebba8951f60e85a941b4c8cfb60be611002/scripts/build_arm_debug.py
- https://github.com/SkiltonUSA/Amiga-MCP-Debugger/blob/3acafebba8951f60e85a941b4c8cfb60be611002/scripts/build_zz9000_debug.py
- https://github.com/SkiltonUSA/Amiga-MCP-Debugger/blob/3acafebba8951f60e85a941b4c8cfb60be611002/docs/amiga-arm-debugging.md

### Runtime profiles (no-evidence-found)

The inspected documentation and build/implementation samples do not establish a complete minimum runnable hardware profile. No RAM or minimum CPU is inferred from platform or compiler target.
- https://github.com/SkiltonUSA/Amiga-MCP-Debugger/blob/3acafebba8951f60e85a941b4c8cfb60be611002/README.md
- https://github.com/SkiltonUSA/Amiga-MCP-Debugger/blob/3acafebba8951f60e85a941b4c8cfb60be611002/scripts/build_arm_debug.py
- https://github.com/SkiltonUSA/Amiga-MCP-Debugger/blob/3acafebba8951f60e85a941b4c8cfb60be611002/scripts/build_zz9000_debug.py
- https://github.com/SkiltonUSA/Amiga-MCP-Debugger/blob/3acafebba8951f60e85a941b4c8cfb60be611002/docs/amiga-arm-debugging.md

### AI (no-evidence-found)

No explicit development-AI contribution attribution was found in the inspected documentation, implementation/build samples and latest default-branch commit. This bounded review does not prove non-use; integration/configuration files are not contribution evidence.
- https://github.com/SkiltonUSA/Amiga-MCP-Debugger/blob/3acafebba8951f60e85a941b4c8cfb60be611002/README.md
- https://github.com/SkiltonUSA/Amiga-MCP-Debugger/blob/3acafebba8951f60e85a941b4c8cfb60be611002/scripts/build_arm_debug.py
- https://github.com/SkiltonUSA/Amiga-MCP-Debugger/blob/3acafebba8951f60e85a941b4c8cfb60be611002/scripts/build_zz9000_debug.py
- https://github.com/SkiltonUSA/Amiga-MCP-Debugger/blob/3acafebba8951f60e85a941b4c8cfb60be611002/docs/amiga-arm-debugging.md
- https://github.com/SkiltonUSA/Amiga-MCP-Debugger/commit/3acafebba8951f60e85a941b4c8cfb60be611002

### Relationships (reviewed)

Distinct cooperative debugging/compute implementation extends tracked geekychris/amiga_mcp; XANI XACP supplies firmware interfaces, not this debugger protocol. SDL2 fixes live separately. Vendor licences remain separate. The repository URL and title were compared with the current catalogue; no equivalent project record was found.
- https://github.com/SkiltonUSA/Amiga-MCP-Debugger/blob/3acafebba8951f60e85a941b4c8cfb60be611002/README.md
- https://github.com/SkiltonUSA/Amiga-MCP-Debugger/blob/3acafebba8951f60e85a941b4c8cfb60be611002/scripts/build_arm_debug.py
- https://github.com/SkiltonUSA/Amiga-MCP-Debugger/blob/3acafebba8951f60e85a941b4c8cfb60be611002/scripts/build_zz9000_debug.py
- https://github.com/SkiltonUSA/Amiga-MCP-Debugger/blob/3acafebba8951f60e85a941b4c8cfb60be611002/docs/amiga-arm-debugging.md

## DCTelnet: maintained Amiga Telnet and BBS client

Project ID: dctelnet-amiga-maintained-source · Overall audit: partial

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
  "display_title": "DCTelnet: maintained Amiga Telnet and BBS client",
  "id": "dctelnet-amiga-maintained-source",
  "last_activity": null,
  "last_checked": "2026-10-15",
  "re_started": null,
  "reconstructed_languages": [
    "C"
  ],
  "record_class": "subject",
  "repo": "https://github.com/bruno-frederic/dctelnet",
  "runtime_profiles": [
    {
      "cpu_family": "m68k",
      "evidence": [
        "https://github.com/bruno-frederic/dctelnet/blob/90f8615ce4ee4b67f1122a4761f9ee65ab90ac94/README.md"
      ],
      "min_cpu": "68000",
      "name": "Upstream classic requirements",
      "notes": "Requires compatible TCP/IP stack; Kickstart 2.00/2.02 require supplied compatible library variants. Separate optimized 68020 output exists.",
      "os": "AmigaOS 2.0+",
      "platform": "Amiga"
    }
  ],
  "source_cpu": [
    "68020"
  ],
  "source_language": [
    "C"
  ],
  "source_platforms": [
    "Amiga"
  ],
  "status": "Primary source and build workflow reviewed; independent execution unverified",
  "subjects": [
    "DCTelnet"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "68000",
    "68020"
  ],
  "target_kinds": [
    "application"
  ],
  "target_platforms": [
    "Amiga"
  ],
  "techniques": [],
  "title": "DCTelnet",
  "tool_kinds": [],
  "types": [
    "source maintenance"
  ],
  "upstream_name": "DCTelnet",
  "work_kinds": [
    "source-restoration",
    "patching"
  ]
}
```

### Identity (reviewed)

Maintained version of Zed's DCTelnet with BBS terminal support, ZModem and a restored 68000-compatible build.
- https://github.com/bruno-frederic/dctelnet/blob/90f8615ce4ee4b67f1122a4761f9ee65ab90ac94/README.md
- https://github.com/bruno-frederic/dctelnet/blob/90f8615ce4ee4b67f1122a4761f9ee65ab90ac94/src/Makefile
- https://github.com/bruno-frederic/dctelnet/blob/90f8615ce4ee4b67f1122a4761f9ee65ab90ac94/src/DCTelnet.c
- https://github.com/bruno-frederic/dctelnet/blob/90f8615ce4ee4b67f1122a4761f9ee65ab90ac94/LICENSE

### Classification (reviewed)

Source maintenance and portability fixes based on published DCTelnet 1.5/1.6 sources; not a binary-derived reconstruction.
- https://github.com/bruno-frederic/dctelnet/blob/90f8615ce4ee4b67f1122a4761f9ee65ab90ac94/README.md
- https://github.com/bruno-frederic/dctelnet/blob/90f8615ce4ee4b67f1122a4761f9ee65ab90ac94/src/Makefile
- https://github.com/bruno-frederic/dctelnet/blob/90f8615ce4ee4b67f1122a4761f9ee65ab90ac94/src/DCTelnet.c
- https://github.com/bruno-frederic/dctelnet/blob/90f8615ce4ee4b67f1122a4761f9ee65ab90ac94/LICENSE

### Source CPU (reviewed)

README explicitly says the original 1.5/1.6 releases were compiled for 68020+; this source-maintenance lineage is distinguished from the new 68000 output.
- https://github.com/bruno-frederic/dctelnet/blob/90f8615ce4ee4b67f1122a4761f9ee65ab90ac94/README.md
- https://github.com/bruno-frederic/dctelnet/blob/90f8615ce4ee4b67f1122a4761f9ee65ab90ac94/src/Makefile
- https://github.com/bruno-frederic/dctelnet/blob/90f8615ce4ee4b67f1122a4761f9ee65ab90ac94/src/DCTelnet.c
- https://github.com/bruno-frederic/dctelnet/blob/90f8615ce4ee4b67f1122a4761f9ee65ab90ac94/LICENSE

### Target CPU (reviewed)

src/Makefile explicitly builds separate 68000 and 68020 variants using VBCC or GCC.
- https://github.com/bruno-frederic/dctelnet/blob/90f8615ce4ee4b67f1122a4761f9ee65ab90ac94/README.md
- https://github.com/bruno-frederic/dctelnet/blob/90f8615ce4ee4b67f1122a4761f9ee65ab90ac94/src/Makefile
- https://github.com/bruno-frederic/dctelnet/blob/90f8615ce4ee4b67f1122a4761f9ee65ab90ac94/src/DCTelnet.c
- https://github.com/bruno-frederic/dctelnet/blob/90f8615ce4ee4b67f1122a4761f9ee65ab90ac94/LICENSE

### Build (reviewed)

README describes recompiled releases since 1.7 and src/Makefile implements both CPU builds. Current C99 versions cannot be built with historical SAS/C. No independent compilation, execution, gameplay or byte comparison was performed; all four build flags remain unknown.
- https://github.com/bruno-frederic/dctelnet/blob/90f8615ce4ee4b67f1122a4761f9ee65ab90ac94/README.md
- https://github.com/bruno-frederic/dctelnet/blob/90f8615ce4ee4b67f1122a4761f9ee65ab90ac94/src/Makefile
- https://github.com/bruno-frederic/dctelnet/blob/90f8615ce4ee4b67f1122a4761f9ee65ab90ac94/src/DCTelnet.c
- https://github.com/bruno-frederic/dctelnet/blob/90f8615ce4ee4b67f1122a4761f9ee65ab90ac94/LICENSE

### Runtime profiles (reviewed)

The runtime profile records the documented requirement, not an independent hardware test.
- https://github.com/bruno-frederic/dctelnet/blob/90f8615ce4ee4b67f1122a4761f9ee65ab90ac94/README.md
- https://github.com/bruno-frederic/dctelnet/blob/90f8615ce4ee4b67f1122a4761f9ee65ab90ac94/src/Makefile
- https://github.com/bruno-frederic/dctelnet/blob/90f8615ce4ee4b67f1122a4761f9ee65ab90ac94/src/DCTelnet.c
- https://github.com/bruno-frederic/dctelnet/blob/90f8615ce4ee4b67f1122a4761f9ee65ab90ac94/LICENSE

### AI (no-evidence-found)

No explicit development-AI contribution attribution was found in the inspected documentation, implementation/build samples and latest default-branch commit. This bounded review does not prove non-use; integration/configuration files are not contribution evidence.
- https://github.com/bruno-frederic/dctelnet/blob/90f8615ce4ee4b67f1122a4761f9ee65ab90ac94/README.md
- https://github.com/bruno-frederic/dctelnet/blob/90f8615ce4ee4b67f1122a4761f9ee65ab90ac94/src/Makefile
- https://github.com/bruno-frederic/dctelnet/blob/90f8615ce4ee4b67f1122a4761f9ee65ab90ac94/src/DCTelnet.c
- https://github.com/bruno-frederic/dctelnet/blob/90f8615ce4ee4b67f1122a4761f9ee65ab90ac94/LICENSE
- https://github.com/bruno-frederic/dctelnet/commit/90f8615ce4ee4b67f1122a4761f9ee65ab90ac94

### Relationships (reviewed)

Credits Zed's Aminet sources, Bruno Frederic and spotUP improvements, and third-party ReqTools/XPR/XEM sources. LICENSE states original code remains all rights reserved. The repository URL and title were compared with the current catalogue; no equivalent project record was found.
- https://github.com/bruno-frederic/dctelnet/blob/90f8615ce4ee4b67f1122a4761f9ee65ab90ac94/README.md
- https://github.com/bruno-frederic/dctelnet/blob/90f8615ce4ee4b67f1122a4761f9ee65ab90ac94/src/Makefile
- https://github.com/bruno-frederic/dctelnet/blob/90f8615ce4ee4b67f1122a4761f9ee65ab90ac94/src/DCTelnet.c
- https://github.com/bruno-frederic/dctelnet/blob/90f8615ce4ee4b67f1122a4761f9ee65ab90ac94/LICENSE

## libcmini: small-footprint Atari C runtime

Project ID: libcmini-atari-runtime · Overall audit: partial

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
  "display_title": "libcmini: small-footprint Atari C runtime",
  "id": "libcmini-atari-runtime",
  "last_activity": null,
  "last_checked": "2026-10-15",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "m68k assembly"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/freemint/libcmini",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source and build workflow reviewed; independent execution unverified",
  "subjects": [],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "68000",
    "ColdFire"
  ],
  "target_kinds": [],
  "target_platforms": [
    "Atari ST"
  ],
  "techniques": [],
  "title": "libcmini",
  "tool_kinds": [
    "compiler-toolchain",
    "development-environment"
  ],
  "types": [
    "C runtime library"
  ],
  "upstream_name": "libcmini",
  "work_kinds": []
}
```

### Identity (reviewed)

Small-footprint C runtime and startup code for m68k-atari-mint/mintelf programs.
- https://github.com/freemint/libcmini/blob/77eb5e1e0129c5dad932e08e50d893cf792a5347/README.md
- https://github.com/freemint/libcmini/blob/77eb5e1e0129c5dad932e08e50d893cf792a5347/Makefile
- https://github.com/freemint/libcmini/blob/77eb5e1e0129c5dad932e08e50d893cf792a5347/sources/crt0.S
- https://github.com/freemint/libcmini/blob/77eb5e1e0129c5dad932e08e50d893cf792a5347/sources/puts.c
- https://github.com/freemint/libcmini/blob/77eb5e1e0129c5dad932e08e50d893cf792a5347/LICENSE.txt

### Classification (reviewed)

Development runtime for small GEM programs; not an independent reconstruction of TOS or a duplicate compiler.
- https://github.com/freemint/libcmini/blob/77eb5e1e0129c5dad932e08e50d893cf792a5347/README.md
- https://github.com/freemint/libcmini/blob/77eb5e1e0129c5dad932e08e50d893cf792a5347/Makefile
- https://github.com/freemint/libcmini/blob/77eb5e1e0129c5dad932e08e50d893cf792a5347/sources/crt0.S
- https://github.com/freemint/libcmini/blob/77eb5e1e0129c5dad932e08e50d893cf792a5347/sources/puts.c
- https://github.com/freemint/libcmini/blob/77eb5e1e0129c5dad932e08e50d893cf792a5347/LICENSE.txt

### Source CPU (not-applicable)

This is newly authored native software or development tooling, not analysis of a predecessor binary. Source platform/CPU/language are intentionally empty; output architecture is recorded separately.
- https://github.com/freemint/libcmini/blob/77eb5e1e0129c5dad932e08e50d893cf792a5347/README.md
- https://github.com/freemint/libcmini/blob/77eb5e1e0129c5dad932e08e50d893cf792a5347/Makefile
- https://github.com/freemint/libcmini/blob/77eb5e1e0129c5dad932e08e50d893cf792a5347/sources/crt0.S
- https://github.com/freemint/libcmini/blob/77eb5e1e0129c5dad932e08e50d893cf792a5347/sources/puts.c
- https://github.com/freemint/libcmini/blob/77eb5e1e0129c5dad932e08e50d893cf792a5347/LICENSE.txt

### Target CPU (reviewed)

Makefile explicitly supports ONLY_68K and ColdFire multilib; crt0.S handles 680x0/ColdFire startup and sources/puts.c supplies C library implementation.
- https://github.com/freemint/libcmini/blob/77eb5e1e0129c5dad932e08e50d893cf792a5347/README.md
- https://github.com/freemint/libcmini/blob/77eb5e1e0129c5dad932e08e50d893cf792a5347/Makefile
- https://github.com/freemint/libcmini/blob/77eb5e1e0129c5dad932e08e50d893cf792a5347/sources/crt0.S
- https://github.com/freemint/libcmini/blob/77eb5e1e0129c5dad932e08e50d893cf792a5347/sources/puts.c
- https://github.com/freemint/libcmini/blob/77eb5e1e0129c5dad932e08e50d893cf792a5347/LICENSE.txt

### Build (reviewed)

README gives make/install and explicit linkage with crt0.o, libcmini and libgcc, plus release/snapshot links. No independent compilation, execution, gameplay or byte comparison was performed; all four build flags remain unknown.
- https://github.com/freemint/libcmini/blob/77eb5e1e0129c5dad932e08e50d893cf792a5347/README.md
- https://github.com/freemint/libcmini/blob/77eb5e1e0129c5dad932e08e50d893cf792a5347/Makefile
- https://github.com/freemint/libcmini/blob/77eb5e1e0129c5dad932e08e50d893cf792a5347/sources/crt0.S
- https://github.com/freemint/libcmini/blob/77eb5e1e0129c5dad932e08e50d893cf792a5347/sources/puts.c
- https://github.com/freemint/libcmini/blob/77eb5e1e0129c5dad932e08e50d893cf792a5347/LICENSE.txt

### Runtime profiles (no-evidence-found)

The inspected documentation and build/implementation samples do not establish a complete minimum runnable hardware profile. No RAM or minimum CPU is inferred from platform or compiler target.
- https://github.com/freemint/libcmini/blob/77eb5e1e0129c5dad932e08e50d893cf792a5347/README.md
- https://github.com/freemint/libcmini/blob/77eb5e1e0129c5dad932e08e50d893cf792a5347/Makefile
- https://github.com/freemint/libcmini/blob/77eb5e1e0129c5dad932e08e50d893cf792a5347/sources/crt0.S
- https://github.com/freemint/libcmini/blob/77eb5e1e0129c5dad932e08e50d893cf792a5347/sources/puts.c
- https://github.com/freemint/libcmini/blob/77eb5e1e0129c5dad932e08e50d893cf792a5347/LICENSE.txt

### AI (no-evidence-found)

No explicit development-AI contribution attribution was found in the inspected documentation, implementation/build samples and latest default-branch commit. This bounded review does not prove non-use; integration/configuration files are not contribution evidence.
- https://github.com/freemint/libcmini/blob/77eb5e1e0129c5dad932e08e50d893cf792a5347/README.md
- https://github.com/freemint/libcmini/blob/77eb5e1e0129c5dad932e08e50d893cf792a5347/Makefile
- https://github.com/freemint/libcmini/blob/77eb5e1e0129c5dad932e08e50d893cf792a5347/sources/crt0.S
- https://github.com/freemint/libcmini/blob/77eb5e1e0129c5dad932e08e50d893cf792a5347/sources/puts.c
- https://github.com/freemint/libcmini/blob/77eb5e1e0129c5dad932e08e50d893cf792a5347/LICENSE.txt
- https://github.com/freemint/libcmini/commit/77eb5e1e0129c5dad932e08e50d893cf792a5347

### Relationships (reviewed)

Alternative to mintlib for smaller GEM programs. sources/puts.c retains GNU C Library attribution and LGPL terms; repository LICENSE.txt is LGPL 2.1. Resolves the open libcmini runtime backlog check. The repository URL and title were compared with the current catalogue; no equivalent project record was found.
- https://github.com/freemint/libcmini/blob/77eb5e1e0129c5dad932e08e50d893cf792a5347/README.md
- https://github.com/freemint/libcmini/blob/77eb5e1e0129c5dad932e08e50d893cf792a5347/Makefile
- https://github.com/freemint/libcmini/blob/77eb5e1e0129c5dad932e08e50d893cf792a5347/sources/crt0.S
- https://github.com/freemint/libcmini/blob/77eb5e1e0129c5dad932e08e50d893cf792a5347/sources/puts.c
- https://github.com/freemint/libcmini/blob/77eb5e1e0129c5dad932e08e50d893cf792a5347/LICENSE.txt

## IMA ADPCM: Amiga/ST decoder and Paula replay library

Project ID: adpcm-68k-codec-replayer · Overall audit: partial

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
  "display_title": "IMA ADPCM: Amiga/ST decoder and Paula replay library",
  "id": "adpcm-68k-codec-replayer",
  "last_activity": null,
  "last_checked": "2026-10-15",
  "re_started": null,
  "reconstructed_languages": [
    "m68k assembly",
    "C++"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/Kalmalyzer/adpcm-68k",
  "runtime_profiles": [
    {
      "evidence": [
        "https://github.com/Kalmalyzer/adpcm-68k/blob/69361d82f03fed8cf667a46a98344f26fca790d9/AmigaReplay/PaulaOutput.s"
      ],
      "name": "Paula replay screen-mode constraint",
      "notes": "PaulaOutput.s requires standard PAL interlaced or noninterlaced modes; NTSC and DBLPAL are unsupported by its playback-position calculation. No application RAM/CPU minimum established.",
      "platform": "Amiga"
    }
  ],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source and build workflow reviewed; independent execution unverified",
  "subjects": [],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "68000"
  ],
  "target_kinds": [],
  "target_platforms": [
    "Amiga",
    "Atari ST",
    "Windows"
  ],
  "techniques": [],
  "title": "IMA ADPCM codec and 68k decoder",
  "tool_kinds": [
    "asset-tool"
  ],
  "types": [
    "audio codec and replay library"
  ],
  "upstream_name": "IMA ADPCM codec and 68k decoder",
  "work_kinds": []
}
```

### Identity (reviewed)

Mikael Kalms' 68000 ADPCM decoder, Amiga Paula replay code and host WAV/ADPCM conversion utility.
- https://github.com/Kalmalyzer/adpcm-68k/blob/69361d82f03fed8cf667a46a98344f26fca790d9/README.md
- https://github.com/Kalmalyzer/adpcm-68k/blob/69361d82f03fed8cf667a46a98344f26fca790d9/Decode68k/ADPCMDecoder68000.s
- https://github.com/Kalmalyzer/adpcm-68k/blob/69361d82f03fed8cf667a46a98344f26fca790d9/AmigaReplay/PaulaOutput.s
- https://github.com/Kalmalyzer/adpcm-68k/blob/69361d82f03fed8cf667a46a98344f26fca790d9/Codec/codec.cpp
- https://github.com/Kalmalyzer/adpcm-68k/blob/69361d82f03fed8cf667a46a98344f26fca790d9/LICENSE.md

### Classification (reviewed)

Reusable audio development tools and decoder library; no historical game or game-specific emulation host.
- https://github.com/Kalmalyzer/adpcm-68k/blob/69361d82f03fed8cf667a46a98344f26fca790d9/README.md
- https://github.com/Kalmalyzer/adpcm-68k/blob/69361d82f03fed8cf667a46a98344f26fca790d9/Decode68k/ADPCMDecoder68000.s
- https://github.com/Kalmalyzer/adpcm-68k/blob/69361d82f03fed8cf667a46a98344f26fca790d9/AmigaReplay/PaulaOutput.s
- https://github.com/Kalmalyzer/adpcm-68k/blob/69361d82f03fed8cf667a46a98344f26fca790d9/Codec/codec.cpp
- https://github.com/Kalmalyzer/adpcm-68k/blob/69361d82f03fed8cf667a46a98344f26fca790d9/LICENSE.md

### Source CPU (not-applicable)

This is newly authored native software or development tooling, not analysis of a predecessor binary. Source platform/CPU/language are intentionally empty; output architecture is recorded separately.
- https://github.com/Kalmalyzer/adpcm-68k/blob/69361d82f03fed8cf667a46a98344f26fca790d9/README.md
- https://github.com/Kalmalyzer/adpcm-68k/blob/69361d82f03fed8cf667a46a98344f26fca790d9/Decode68k/ADPCMDecoder68000.s
- https://github.com/Kalmalyzer/adpcm-68k/blob/69361d82f03fed8cf667a46a98344f26fca790d9/AmigaReplay/PaulaOutput.s
- https://github.com/Kalmalyzer/adpcm-68k/blob/69361d82f03fed8cf667a46a98344f26fca790d9/Codec/codec.cpp
- https://github.com/Kalmalyzer/adpcm-68k/blob/69361d82f03fed8cf667a46a98344f26fca790d9/LICENSE.md

### Target CPU (reviewed)

Decoder header explicitly targets 68000 and documents A500/ST timings; no host CPU inferred from the Windows executable.
- https://github.com/Kalmalyzer/adpcm-68k/blob/69361d82f03fed8cf667a46a98344f26fca790d9/README.md
- https://github.com/Kalmalyzer/adpcm-68k/blob/69361d82f03fed8cf667a46a98344f26fca790d9/Decode68k/ADPCMDecoder68000.s
- https://github.com/Kalmalyzer/adpcm-68k/blob/69361d82f03fed8cf667a46a98344f26fca790d9/AmigaReplay/PaulaOutput.s
- https://github.com/Kalmalyzer/adpcm-68k/blob/69361d82f03fed8cf667a46a98344f26fca790d9/Codec/codec.cpp
- https://github.com/Kalmalyzer/adpcm-68k/blob/69361d82f03fed8cf667a46a98344f26fca790d9/LICENSE.md

### Build (reviewed)

Native assembly decoder/replay source and a Visual Studio codec project/executable are included; upstream reports measured throughput. No independent compilation, execution, gameplay or byte comparison was performed; all four build flags remain unknown.
- https://github.com/Kalmalyzer/adpcm-68k/blob/69361d82f03fed8cf667a46a98344f26fca790d9/README.md
- https://github.com/Kalmalyzer/adpcm-68k/blob/69361d82f03fed8cf667a46a98344f26fca790d9/Decode68k/ADPCMDecoder68000.s
- https://github.com/Kalmalyzer/adpcm-68k/blob/69361d82f03fed8cf667a46a98344f26fca790d9/AmigaReplay/PaulaOutput.s
- https://github.com/Kalmalyzer/adpcm-68k/blob/69361d82f03fed8cf667a46a98344f26fca790d9/Codec/codec.cpp
- https://github.com/Kalmalyzer/adpcm-68k/blob/69361d82f03fed8cf667a46a98344f26fca790d9/LICENSE.md

### Runtime profiles (reviewed)

PaulaOutput.s requires PAL interlaced or noninterlaced screen modes and explicitly excludes NTSC/DBLPAL for its playback-position calculation. No complete CPU/RAM minimum for the replay application was established.
- https://github.com/Kalmalyzer/adpcm-68k/blob/69361d82f03fed8cf667a46a98344f26fca790d9/README.md
- https://github.com/Kalmalyzer/adpcm-68k/blob/69361d82f03fed8cf667a46a98344f26fca790d9/Decode68k/ADPCMDecoder68000.s
- https://github.com/Kalmalyzer/adpcm-68k/blob/69361d82f03fed8cf667a46a98344f26fca790d9/AmigaReplay/PaulaOutput.s
- https://github.com/Kalmalyzer/adpcm-68k/blob/69361d82f03fed8cf667a46a98344f26fca790d9/Codec/codec.cpp
- https://github.com/Kalmalyzer/adpcm-68k/blob/69361d82f03fed8cf667a46a98344f26fca790d9/LICENSE.md

### AI (no-evidence-found)

No explicit development-AI contribution attribution was found in the inspected documentation, implementation/build samples and latest default-branch commit. This bounded review does not prove non-use; integration/configuration files are not contribution evidence.
- https://github.com/Kalmalyzer/adpcm-68k/blob/69361d82f03fed8cf667a46a98344f26fca790d9/README.md
- https://github.com/Kalmalyzer/adpcm-68k/blob/69361d82f03fed8cf667a46a98344f26fca790d9/Decode68k/ADPCMDecoder68000.s
- https://github.com/Kalmalyzer/adpcm-68k/blob/69361d82f03fed8cf667a46a98344f26fca790d9/AmigaReplay/PaulaOutput.s
- https://github.com/Kalmalyzer/adpcm-68k/blob/69361d82f03fed8cf667a46a98344f26fca790d9/Codec/codec.cpp
- https://github.com/Kalmalyzer/adpcm-68k/blob/69361d82f03fed8cf667a46a98344f26fca790d9/LICENSE.md
- https://github.com/Kalmalyzer/adpcm-68k/commit/69361d82f03fed8cf667a46a98344f26fca790d9

### Relationships (reviewed)

68k code is credited to Mikael Kalms and MIT licensed; reference codec provenance is Stichting Mathematisch Centrum with its own notices. Keep the coherent codec/replay system together. The repository URL and title were compared with the current catalogue; no equivalent project record was found.
- https://github.com/Kalmalyzer/adpcm-68k/blob/69361d82f03fed8cf667a46a98344f26fca790d9/README.md
- https://github.com/Kalmalyzer/adpcm-68k/blob/69361d82f03fed8cf667a46a98344f26fca790d9/Decode68k/ADPCMDecoder68000.s
- https://github.com/Kalmalyzer/adpcm-68k/blob/69361d82f03fed8cf667a46a98344f26fca790d9/AmigaReplay/PaulaOutput.s
- https://github.com/Kalmalyzer/adpcm-68k/blob/69361d82f03fed8cf667a46a98344f26fca790d9/Codec/codec.cpp
- https://github.com/Kalmalyzer/adpcm-68k/blob/69361d82f03fed8cf667a46a98344f26fca790d9/LICENSE.md

## SNDH/YM Archive Player: Atari music inspection and WAV export

Project ID: sndh-ym-archive-player · Overall audit: partial

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
  "display_title": "SNDH/YM Archive Player: Atari music inspection and WAV export",
  "id": "sndh-ym-archive-player",
  "last_activity": null,
  "last_checked": "2026-10-15",
  "re_started": null,
  "reconstructed_languages": [
    "C++"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/arnaud-carre/sndh-player",
  "runtime_profiles": [],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [
    "m68k machine code"
  ],
  "source_platforms": [
    "Atari ST"
  ],
  "status": "Primary source and build workflow reviewed; independent execution unverified",
  "subjects": [],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "ARM64"
  ],
  "target_kinds": [],
  "target_platforms": [
    "Windows",
    "macOS"
  ],
  "techniques": [],
  "title": "SNDH and YM Archive Player",
  "tool_kinds": [
    "asset-tool"
  ],
  "types": [
    "music inspection and export tool"
  ],
  "upstream_name": "SNDH and YM Archive Player",
  "work_kinds": []
}
```

### Identity (reviewed)

Leonard/Oxygene's SNDH/YM archive browser/player with per-voice visualization, seeking and WAV export.
- https://github.com/arnaud-carre/sndh-player/blob/8f1b0ca6d28088743725628d19db180f62cb1202/README.md
- https://github.com/arnaud-carre/sndh-player/blob/8f1b0ca6d28088743725628d19db180f62cb1202/CMakeLists.txt
- https://github.com/arnaud-carre/sndh-player/blob/8f1b0ca6d28088743725628d19db180f62cb1202/SndhArchivePlayer/WavWriter.cpp
- https://github.com/arnaud-carre/sndh-player/blob/8f1b0ca6d28088743725628d19db180f62cb1202/SndhArchivePlayer/AsyncSndhStream.cpp
- https://github.com/arnaud-carre/sndh-player/blob/8f1b0ca6d28088743725628d19db180f62cb1202/LICENSE

### Classification (reviewed)

Tool for inspecting and exporting historical Atari music using the separate AtariAudio library; not a game-specific host.
- https://github.com/arnaud-carre/sndh-player/blob/8f1b0ca6d28088743725628d19db180f62cb1202/README.md
- https://github.com/arnaud-carre/sndh-player/blob/8f1b0ca6d28088743725628d19db180f62cb1202/CMakeLists.txt
- https://github.com/arnaud-carre/sndh-player/blob/8f1b0ca6d28088743725628d19db180f62cb1202/SndhArchivePlayer/WavWriter.cpp
- https://github.com/arnaud-carre/sndh-player/blob/8f1b0ca6d28088743725628d19db180f62cb1202/SndhArchivePlayer/AsyncSndhStream.cpp
- https://github.com/arnaud-carre/sndh-player/blob/8f1b0ca6d28088743725628d19db180f62cb1202/LICENSE

### Source CPU (reviewed)

README describes execution of Atari SNDH music through Musashi 68k and AtariAudio. YM register-dump data itself is not executable CPU code.
- https://github.com/arnaud-carre/sndh-player/blob/8f1b0ca6d28088743725628d19db180f62cb1202/README.md
- https://github.com/arnaud-carre/sndh-player/blob/8f1b0ca6d28088743725628d19db180f62cb1202/CMakeLists.txt
- https://github.com/arnaud-carre/sndh-player/blob/8f1b0ca6d28088743725628d19db180f62cb1202/SndhArchivePlayer/WavWriter.cpp
- https://github.com/arnaud-carre/sndh-player/blob/8f1b0ca6d28088743725628d19db180f62cb1202/SndhArchivePlayer/AsyncSndhStream.cpp
- https://github.com/arnaud-carre/sndh-player/blob/8f1b0ca6d28088743725628d19db180f62cb1202/LICENSE

### Target CPU (reviewed)

README explicitly identifies macOS Arm prebuilt output. Windows architecture is not inferred from the C++ source.
- https://github.com/arnaud-carre/sndh-player/blob/8f1b0ca6d28088743725628d19db180f62cb1202/README.md
- https://github.com/arnaud-carre/sndh-player/blob/8f1b0ca6d28088743725628d19db180f62cb1202/CMakeLists.txt
- https://github.com/arnaud-carre/sndh-player/blob/8f1b0ca6d28088743725628d19db180f62cb1202/SndhArchivePlayer/WavWriter.cpp
- https://github.com/arnaud-carre/sndh-player/blob/8f1b0ca6d28088743725628d19db180f62cb1202/SndhArchivePlayer/AsyncSndhStream.cpp
- https://github.com/arnaud-carre/sndh-player/blob/8f1b0ca6d28088743725628d19db180f62cb1202/LICENSE

### Build (reviewed)

README documents prebuilt Windows/macOS players and CMake compilation; WavWriter.cpp implements export. No independent compilation, execution, gameplay or byte comparison was performed; all four build flags remain unknown.
- https://github.com/arnaud-carre/sndh-player/blob/8f1b0ca6d28088743725628d19db180f62cb1202/README.md
- https://github.com/arnaud-carre/sndh-player/blob/8f1b0ca6d28088743725628d19db180f62cb1202/CMakeLists.txt
- https://github.com/arnaud-carre/sndh-player/blob/8f1b0ca6d28088743725628d19db180f62cb1202/SndhArchivePlayer/WavWriter.cpp
- https://github.com/arnaud-carre/sndh-player/blob/8f1b0ca6d28088743725628d19db180f62cb1202/SndhArchivePlayer/AsyncSndhStream.cpp
- https://github.com/arnaud-carre/sndh-player/blob/8f1b0ca6d28088743725628d19db180f62cb1202/LICENSE

### Runtime profiles (no-evidence-found)

The inspected documentation and build/implementation samples do not establish a complete minimum runnable hardware profile. No RAM or minimum CPU is inferred from platform or compiler target.
- https://github.com/arnaud-carre/sndh-player/blob/8f1b0ca6d28088743725628d19db180f62cb1202/README.md
- https://github.com/arnaud-carre/sndh-player/blob/8f1b0ca6d28088743725628d19db180f62cb1202/CMakeLists.txt
- https://github.com/arnaud-carre/sndh-player/blob/8f1b0ca6d28088743725628d19db180f62cb1202/SndhArchivePlayer/WavWriter.cpp
- https://github.com/arnaud-carre/sndh-player/blob/8f1b0ca6d28088743725628d19db180f62cb1202/SndhArchivePlayer/AsyncSndhStream.cpp
- https://github.com/arnaud-carre/sndh-player/blob/8f1b0ca6d28088743725628d19db180f62cb1202/LICENSE

### AI (no-evidence-found)

No explicit development-AI contribution attribution was found in the inspected documentation, implementation/build samples and latest default-branch commit. This bounded review does not prove non-use; integration/configuration files are not contribution evidence.
- https://github.com/arnaud-carre/sndh-player/blob/8f1b0ca6d28088743725628d19db180f62cb1202/README.md
- https://github.com/arnaud-carre/sndh-player/blob/8f1b0ca6d28088743725628d19db180f62cb1202/CMakeLists.txt
- https://github.com/arnaud-carre/sndh-player/blob/8f1b0ca6d28088743725628d19db180f62cb1202/SndhArchivePlayer/WavWriter.cpp
- https://github.com/arnaud-carre/sndh-player/blob/8f1b0ca6d28088743725628d19db180f62cb1202/SndhArchivePlayer/AsyncSndhStream.cpp
- https://github.com/arnaud-carre/sndh-player/blob/8f1b0ca6d28088743725628d19db180f62cb1202/LICENSE
- https://github.com/arnaud-carre/sndh-player/commit/8f1b0ca6d28088743725628d19db180f62cb1202

### Relationships (reviewed)

AtariAudio is an explicit separate dependency; README describes Musashi 68k and YM/MFP/STE DAC emulation lineage. This record is the archive inspection application, not another record for its core. MIT licence. The repository URL and title were compared with the current catalogue; no equivalent project record was found.
- https://github.com/arnaud-carre/sndh-player/blob/8f1b0ca6d28088743725628d19db180f62cb1202/README.md
- https://github.com/arnaud-carre/sndh-player/blob/8f1b0ca6d28088743725628d19db180f62cb1202/CMakeLists.txt
- https://github.com/arnaud-carre/sndh-player/blob/8f1b0ca6d28088743725628d19db180f62cb1202/SndhArchivePlayer/WavWriter.cpp
- https://github.com/arnaud-carre/sndh-player/blob/8f1b0ca6d28088743725628d19db180f62cb1202/SndhArchivePlayer/AsyncSndhStream.cpp
- https://github.com/arnaud-carre/sndh-player/blob/8f1b0ca6d28088743725628d19db180f62cb1202/LICENSE

## rVNCd: native Amiga VNC server

Project ID: rvncd-amiga-vnc-server · Overall audit: partial

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
  "display_title": "rVNCd: native Amiga VNC server",
  "id": "rvncd-amiga-vnc-server",
  "last_activity": null,
  "last_checked": "2026-10-15",
  "re_started": null,
  "reconstructed_languages": [
    "C"
  ],
  "record_class": "subject",
  "repo": "https://github.com/rolsen74/rvncd",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source and build workflow reviewed; independent execution unverified",
  "subjects": [
    "rVNCd"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "m68k",
    "PowerPC"
  ],
  "target_kinds": [
    "application"
  ],
  "target_platforms": [
    "Amiga",
    "AmigaOS 4"
  ],
  "techniques": [],
  "title": "rVNCd",
  "tool_kinds": [],
  "types": [
    "native application source"
  ],
  "upstream_name": "rVNCd",
  "work_kinds": []
}
```

### Identity (reviewed)

Native Amiga VNC server with screen, input, clipboard and ARexx integration.
- https://github.com/rolsen74/rvncd/blob/6a433c0216357c61abdf6fa95686aab229cdb09a/README.md
- https://github.com/rolsen74/rvncd/blob/6a433c0216357c61abdf6fa95686aab229cdb09a/makefile
- https://github.com/rolsen74/rvncd/blob/6a433c0216357c61abdf6fa95686aab229cdb09a/src/rVNCd.c
- https://github.com/rolsen74/rvncd/blob/6a433c0216357c61abdf6fa95686aab229cdb09a/LICENSE

### Classification (reviewed)

Original native application; AmigaOS 4 support is documented, while AmigaOS 3 remains work in progress.
- https://github.com/rolsen74/rvncd/blob/6a433c0216357c61abdf6fa95686aab229cdb09a/README.md
- https://github.com/rolsen74/rvncd/blob/6a433c0216357c61abdf6fa95686aab229cdb09a/makefile
- https://github.com/rolsen74/rvncd/blob/6a433c0216357c61abdf6fa95686aab229cdb09a/src/rVNCd.c
- https://github.com/rolsen74/rvncd/blob/6a433c0216357c61abdf6fa95686aab229cdb09a/LICENSE

### Source CPU (not-applicable)

This is newly authored native software or development tooling, not analysis of a predecessor binary. Source platform/CPU/language are intentionally empty; output architecture is recorded separately.
- https://github.com/rolsen74/rvncd/blob/6a433c0216357c61abdf6fa95686aab229cdb09a/README.md
- https://github.com/rolsen74/rvncd/blob/6a433c0216357c61abdf6fa95686aab229cdb09a/makefile
- https://github.com/rolsen74/rvncd/blob/6a433c0216357c61abdf6fa95686aab229cdb09a/src/rVNCd.c
- https://github.com/rolsen74/rvncd/blob/6a433c0216357c61abdf6fa95686aab229cdb09a/LICENSE

### Target CPU (reviewed)

makefile selects vbcc/vasmm68k_mot for AOS3 and ppc-amigaos-gcc for AOS4. These targets do not establish a working AOS3 build.
- https://github.com/rolsen74/rvncd/blob/6a433c0216357c61abdf6fa95686aab229cdb09a/README.md
- https://github.com/rolsen74/rvncd/blob/6a433c0216357c61abdf6fa95686aab229cdb09a/makefile
- https://github.com/rolsen74/rvncd/blob/6a433c0216357c61abdf6fa95686aab229cdb09a/src/rVNCd.c
- https://github.com/rolsen74/rvncd/blob/6a433c0216357c61abdf6fa95686aab229cdb09a/LICENSE

### Build (reviewed)

Makefile provides AOS3/AOS4, graphics and GUI variants; README describes native AOS4 operation and ongoing AOS3 support. No independent compilation, execution, gameplay or byte comparison was performed; all four build flags remain unknown.
- https://github.com/rolsen74/rvncd/blob/6a433c0216357c61abdf6fa95686aab229cdb09a/README.md
- https://github.com/rolsen74/rvncd/blob/6a433c0216357c61abdf6fa95686aab229cdb09a/makefile
- https://github.com/rolsen74/rvncd/blob/6a433c0216357c61abdf6fa95686aab229cdb09a/src/rVNCd.c
- https://github.com/rolsen74/rvncd/blob/6a433c0216357c61abdf6fa95686aab229cdb09a/LICENSE

### Runtime profiles (no-evidence-found)

The inspected documentation and build/implementation samples do not establish a complete minimum runnable hardware profile. No RAM or minimum CPU is inferred from platform or compiler target.
- https://github.com/rolsen74/rvncd/blob/6a433c0216357c61abdf6fa95686aab229cdb09a/README.md
- https://github.com/rolsen74/rvncd/blob/6a433c0216357c61abdf6fa95686aab229cdb09a/makefile
- https://github.com/rolsen74/rvncd/blob/6a433c0216357c61abdf6fa95686aab229cdb09a/src/rVNCd.c
- https://github.com/rolsen74/rvncd/blob/6a433c0216357c61abdf6fa95686aab229cdb09a/LICENSE

### AI (no-evidence-found)

No explicit development-AI contribution attribution was found in the inspected documentation, implementation/build samples and latest default-branch commit. This bounded review does not prove non-use; integration/configuration files are not contribution evidence.
- https://github.com/rolsen74/rvncd/blob/6a433c0216357c61abdf6fa95686aab229cdb09a/README.md
- https://github.com/rolsen74/rvncd/blob/6a433c0216357c61abdf6fa95686aab229cdb09a/makefile
- https://github.com/rolsen74/rvncd/blob/6a433c0216357c61abdf6fa95686aab229cdb09a/src/rVNCd.c
- https://github.com/rolsen74/rvncd/blob/6a433c0216357c61abdf6fa95686aab229cdb09a/LICENSE
- https://github.com/rolsen74/rvncd/commit/6a433c0216357c61abdf6fa95686aab229cdb09a

### Relationships (reviewed)

One server with platform/backend variants; retain at repository root. GPLv3 repository licence; no predecessor-binary derivation claimed. The repository URL and title were compared with the current catalogue; no equivalent project record was found.
- https://github.com/rolsen74/rvncd/blob/6a433c0216357c61abdf6fa95686aab229cdb09a/README.md
- https://github.com/rolsen74/rvncd/blob/6a433c0216357c61abdf6fa95686aab229cdb09a/makefile
- https://github.com/rolsen74/rvncd/blob/6a433c0216357c61abdf6fa95686aab229cdb09a/src/rVNCd.c
- https://github.com/rolsen74/rvncd/blob/6a433c0216357c61abdf6fa95686aab229cdb09a/LICENSE

## Monster Attack: C64 adventure-engine game

Project ID: c64-monster-attack · Overall audit: partial

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
  "display_title": "Monster Attack: C64 adventure-engine game",
  "id": "c64-monster-attack",
  "last_activity": null,
  "last_checked": "2026-10-15",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "6502 assembly",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/JPEWdev/c64-monster-attack",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source and build workflow reviewed; independent execution unverified",
  "subjects": [
    "Commodore 64 Monster Attack"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "6502"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Commodore 64"
  ],
  "techniques": [],
  "title": "Commodore 64 Monster Attack",
  "tool_kinds": [],
  "types": [
    "native homebrew game"
  ],
  "upstream_name": "Commodore 64 Monster Attack",
  "work_kinds": []
}
```

### Identity (reviewed)

Joshua Watt's monster-fighting game with weapons, coins, store and an adventure-engine demonstration.
- https://github.com/JPEWdev/c64-monster-attack/blob/29ef2d84e2a20b4ef8e4af20a2037b3fd6accb1b/README.md
- https://github.com/JPEWdev/c64-monster-attack/blob/29ef2d84e2a20b4ef8e4af20a2037b3fd6accb1b/CMakeLists.txt
- https://github.com/JPEWdev/c64-monster-attack/blob/29ef2d84e2a20b4ef8e4af20a2037b3fd6accb1b/src/main.c
- https://github.com/JPEWdev/c64-monster-attack/blob/29ef2d84e2a20b4ef8e4af20a2037b3fd6accb1b/src/screen.S
- https://github.com/JPEWdev/c64-monster-attack/blob/29ef2d84e2a20b4ef8e4af20a2037b3fd6accb1b/LICENSE

### Classification (reviewed)

Substantive native homebrew; upstream calls it a playable technology demo rather than a completed adventure.
- https://github.com/JPEWdev/c64-monster-attack/blob/29ef2d84e2a20b4ef8e4af20a2037b3fd6accb1b/README.md
- https://github.com/JPEWdev/c64-monster-attack/blob/29ef2d84e2a20b4ef8e4af20a2037b3fd6accb1b/CMakeLists.txt
- https://github.com/JPEWdev/c64-monster-attack/blob/29ef2d84e2a20b4ef8e4af20a2037b3fd6accb1b/src/main.c
- https://github.com/JPEWdev/c64-monster-attack/blob/29ef2d84e2a20b4ef8e4af20a2037b3fd6accb1b/src/screen.S
- https://github.com/JPEWdev/c64-monster-attack/blob/29ef2d84e2a20b4ef8e4af20a2037b3fd6accb1b/LICENSE

### Source CPU (not-applicable)

This is newly authored native software or development tooling, not analysis of a predecessor binary. Source platform/CPU/language are intentionally empty; output architecture is recorded separately.
- https://github.com/JPEWdev/c64-monster-attack/blob/29ef2d84e2a20b4ef8e4af20a2037b3fd6accb1b/README.md
- https://github.com/JPEWdev/c64-monster-attack/blob/29ef2d84e2a20b4ef8e4af20a2037b3fd6accb1b/CMakeLists.txt
- https://github.com/JPEWdev/c64-monster-attack/blob/29ef2d84e2a20b4ef8e4af20a2037b3fd6accb1b/src/main.c
- https://github.com/JPEWdev/c64-monster-attack/blob/29ef2d84e2a20b4ef8e4af20a2037b3fd6accb1b/src/screen.S
- https://github.com/JPEWdev/c64-monster-attack/blob/29ef2d84e2a20b4ef8e4af20a2037b3fd6accb1b/LICENSE

### Target CPU (reviewed)

README explicitly names the 6502 compiler family and handwritten interrupts; CMake selects llvm-mos-sdk platform c64.
- https://github.com/JPEWdev/c64-monster-attack/blob/29ef2d84e2a20b4ef8e4af20a2037b3fd6accb1b/README.md
- https://github.com/JPEWdev/c64-monster-attack/blob/29ef2d84e2a20b4ef8e4af20a2037b3fd6accb1b/CMakeLists.txt
- https://github.com/JPEWdev/c64-monster-attack/blob/29ef2d84e2a20b4ef8e4af20a2037b3fd6accb1b/src/main.c
- https://github.com/JPEWdev/c64-monster-attack/blob/29ef2d84e2a20b4ef8e4af20a2037b3fd6accb1b/src/screen.S
- https://github.com/JPEWdev/c64-monster-attack/blob/29ef2d84e2a20b4ef8e4af20a2037b3fd6accb1b/LICENSE

### Build (reviewed)

CMake/Ninja builds PRG/D64 and VICE debug targets; README offers releases and explicitly says the game is playable, with more progression/enemies planned. No independent compilation, execution, gameplay or byte comparison was performed; all four build flags remain unknown.
- https://github.com/JPEWdev/c64-monster-attack/blob/29ef2d84e2a20b4ef8e4af20a2037b3fd6accb1b/README.md
- https://github.com/JPEWdev/c64-monster-attack/blob/29ef2d84e2a20b4ef8e4af20a2037b3fd6accb1b/CMakeLists.txt
- https://github.com/JPEWdev/c64-monster-attack/blob/29ef2d84e2a20b4ef8e4af20a2037b3fd6accb1b/src/main.c
- https://github.com/JPEWdev/c64-monster-attack/blob/29ef2d84e2a20b4ef8e4af20a2037b3fd6accb1b/src/screen.S
- https://github.com/JPEWdev/c64-monster-attack/blob/29ef2d84e2a20b4ef8e4af20a2037b3fd6accb1b/LICENSE

### Runtime profiles (no-evidence-found)

The inspected documentation and build/implementation samples do not establish a complete minimum runnable hardware profile. No RAM or minimum CPU is inferred from platform or compiler target.
- https://github.com/JPEWdev/c64-monster-attack/blob/29ef2d84e2a20b4ef8e4af20a2037b3fd6accb1b/README.md
- https://github.com/JPEWdev/c64-monster-attack/blob/29ef2d84e2a20b4ef8e4af20a2037b3fd6accb1b/CMakeLists.txt
- https://github.com/JPEWdev/c64-monster-attack/blob/29ef2d84e2a20b4ef8e4af20a2037b3fd6accb1b/src/main.c
- https://github.com/JPEWdev/c64-monster-attack/blob/29ef2d84e2a20b4ef8e4af20a2037b3fd6accb1b/src/screen.S
- https://github.com/JPEWdev/c64-monster-attack/blob/29ef2d84e2a20b4ef8e4af20a2037b3fd6accb1b/LICENSE

### AI (no-evidence-found)

No explicit development-AI contribution attribution was found in the inspected documentation, implementation/build samples and latest default-branch commit. This bounded review does not prove non-use; integration/configuration files are not contribution evidence.
- https://github.com/JPEWdev/c64-monster-attack/blob/29ef2d84e2a20b4ef8e4af20a2037b3fd6accb1b/README.md
- https://github.com/JPEWdev/c64-monster-attack/blob/29ef2d84e2a20b4ef8e4af20a2037b3fd6accb1b/CMakeLists.txt
- https://github.com/JPEWdev/c64-monster-attack/blob/29ef2d84e2a20b4ef8e4af20a2037b3fd6accb1b/src/main.c
- https://github.com/JPEWdev/c64-monster-attack/blob/29ef2d84e2a20b4ef8e4af20a2037b3fd6accb1b/src/screen.S
- https://github.com/JPEWdev/c64-monster-attack/blob/29ef2d84e2a20b4ef8e4af20a2037b3fd6accb1b/LICENSE
- https://github.com/JPEWdev/c64-monster-attack/commit/29ef2d84e2a20b4ef8e4af20a2037b3fd6accb1b

### Relationships (reviewed)

Original coherent game/engine project; llvm-mos, VICE and PETSCII Editor are dependencies, not predecessor games. MIT licensed. The repository URL and title were compared with the current catalogue; no equivalent project record was found.
- https://github.com/JPEWdev/c64-monster-attack/blob/29ef2d84e2a20b4ef8e4af20a2037b3fd6accb1b/README.md
- https://github.com/JPEWdev/c64-monster-attack/blob/29ef2d84e2a20b4ef8e4af20a2037b3fd6accb1b/CMakeLists.txt
- https://github.com/JPEWdev/c64-monster-attack/blob/29ef2d84e2a20b4ef8e4af20a2037b3fd6accb1b/src/main.c
- https://github.com/JPEWdev/c64-monster-attack/blob/29ef2d84e2a20b4ef8e4af20a2037b3fd6accb1b/src/screen.S
- https://github.com/JPEWdev/c64-monster-attack/blob/29ef2d84e2a20b4ef8e4af20a2037b3fd6accb1b/LICENSE

## Storm Chase: C64 source and 64tass conversion

Project ID: storm-chase-c64-source · Overall audit: partial

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
  "display_title": "Storm Chase: C64 source and 64tass conversion",
  "id": "storm-chase-c64-source",
  "last_activity": null,
  "last_checked": "2026-10-15",
  "re_started": null,
  "reconstructed_languages": [
    "6502 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/RichardTND/Storm-Chase",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source and build workflow reviewed; independent execution unverified",
  "subjects": [
    "Storm Chase"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "6502"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Commodore 64"
  ],
  "techniques": [],
  "title": "Storm Chase",
  "tool_kinds": [],
  "types": [
    "native homebrew game source"
  ],
  "upstream_name": "Storm Chase",
  "work_kinds": []
}
```

### Identity (reviewed)

Richard/TND's 2020 rain-catching game, built originally using native C64 tools and published with assets and source.
- https://github.com/RichardTND/Storm-Chase/blob/620e3e02faaf27050a89519b954135a74b5ba405/README.md
- https://github.com/RichardTND/Storm-Chase/blob/620e3e02faaf27050a89519b954135a74b5ba405/StormChase/stormchase.asm
- https://github.com/RichardTND/Storm-Chase/blob/620e3e02faaf27050a89519b954135a74b5ba405/StormChase/buildit.bat

### Classification (reviewed)

Author source release converted from Turbo Assembler to 64tass; no binary-derived disassembly claim.
- https://github.com/RichardTND/Storm-Chase/blob/620e3e02faaf27050a89519b954135a74b5ba405/README.md
- https://github.com/RichardTND/Storm-Chase/blob/620e3e02faaf27050a89519b954135a74b5ba405/StormChase/stormchase.asm
- https://github.com/RichardTND/Storm-Chase/blob/620e3e02faaf27050a89519b954135a74b5ba405/StormChase/buildit.bat

### Source CPU (not-applicable)

This is newly authored native software or development tooling, not analysis of a predecessor binary. Source platform/CPU/language are intentionally empty; output architecture is recorded separately.
- https://github.com/RichardTND/Storm-Chase/blob/620e3e02faaf27050a89519b954135a74b5ba405/README.md
- https://github.com/RichardTND/Storm-Chase/blob/620e3e02faaf27050a89519b954135a74b5ba405/StormChase/stormchase.asm
- https://github.com/RichardTND/Storm-Chase/blob/620e3e02faaf27050a89519b954135a74b5ba405/StormChase/buildit.bat

### Target CPU (reviewed)

stormchase.asm implements 6502 instructions and C64 VIC/SID accesses; buildit.bat invokes 64tass for the native PRG.
- https://github.com/RichardTND/Storm-Chase/blob/620e3e02faaf27050a89519b954135a74b5ba405/README.md
- https://github.com/RichardTND/Storm-Chase/blob/620e3e02faaf27050a89519b954135a74b5ba405/StormChase/stormchase.asm
- https://github.com/RichardTND/Storm-Chase/blob/620e3e02faaf27050a89519b954135a74b5ba405/StormChase/buildit.bat

### Build (reviewed)

Committed PRG/assets and a Windows-specific 64tass/Exomizer/VICE batch workflow exist; the script contains local paths and is not independently validated. No independent compilation, execution, gameplay or byte comparison was performed; all four build flags remain unknown.
- https://github.com/RichardTND/Storm-Chase/blob/620e3e02faaf27050a89519b954135a74b5ba405/README.md
- https://github.com/RichardTND/Storm-Chase/blob/620e3e02faaf27050a89519b954135a74b5ba405/StormChase/stormchase.asm
- https://github.com/RichardTND/Storm-Chase/blob/620e3e02faaf27050a89519b954135a74b5ba405/StormChase/buildit.bat

### Runtime profiles (no-evidence-found)

The inspected documentation and build/implementation samples do not establish a complete minimum runnable hardware profile. No RAM or minimum CPU is inferred from platform or compiler target.
- https://github.com/RichardTND/Storm-Chase/blob/620e3e02faaf27050a89519b954135a74b5ba405/README.md
- https://github.com/RichardTND/Storm-Chase/blob/620e3e02faaf27050a89519b954135a74b5ba405/StormChase/stormchase.asm
- https://github.com/RichardTND/Storm-Chase/blob/620e3e02faaf27050a89519b954135a74b5ba405/StormChase/buildit.bat

### AI (no-evidence-found)

No explicit development-AI contribution attribution was found in the inspected documentation, implementation/build samples and latest default-branch commit. This bounded review does not prove non-use; integration/configuration files are not contribution evidence.
- https://github.com/RichardTND/Storm-Chase/blob/620e3e02faaf27050a89519b954135a74b5ba405/README.md
- https://github.com/RichardTND/Storm-Chase/blob/620e3e02faaf27050a89519b954135a74b5ba405/StormChase/stormchase.asm
- https://github.com/RichardTND/Storm-Chase/blob/620e3e02faaf27050a89519b954135a74b5ba405/StormChase/buildit.bat
- https://github.com/RichardTND/Storm-Chase/commit/620e3e02faaf27050a89519b954135a74b5ba405

### Relationships (reviewed)

README credits Richard/TND and permits exploration/modification with credit, describing it as freeware; no generic OSI licence is inferred. The repository URL and title were compared with the current catalogue; no equivalent project record was found.
- https://github.com/RichardTND/Storm-Chase/blob/620e3e02faaf27050a89519b954135a74b5ba405/README.md
- https://github.com/RichardTND/Storm-Chase/blob/620e3e02faaf27050a89519b954135a74b5ba405/StormChase/stormchase.asm
- https://github.com/RichardTND/Storm-Chase/blob/620e3e02faaf27050a89519b954135a74b5ba405/StormChase/buildit.bat

## Tiger Moth: C64 assembly game source

Project ID: tigermoth-c64-source · Overall audit: partial

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
  "display_title": "Tiger Moth: C64 assembly game source",
  "id": "tigermoth-c64-source",
  "last_activity": null,
  "last_checked": "2026-10-15",
  "re_started": null,
  "reconstructed_languages": [
    "6502 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/pmprog/TigerMothC64",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source and build workflow reviewed; independent execution unverified",
  "subjects": [
    "Tiger Moth"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "6502"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Commodore 64"
  ],
  "techniques": [],
  "title": "Tiger Moth",
  "tool_kinds": [],
  "types": [
    "native homebrew game source"
  ],
  "upstream_name": "Tiger Moth",
  "work_kinds": []
}
```

### Identity (reviewed)

Marq Watkin/Polymath's C64 game source snapshot includes title/game loops, levels, player health, bullets, sprites and scoring.
- https://github.com/pmprog/TigerMothC64/blob/1acaeb7d5faf069f3406cfd68dbdb6c6a88344df/tigermoth.asm
- https://github.com/pmprog/TigerMothC64/blob/1acaeb7d5faf069f3406cfd68dbdb6c6a88344df/screen_game.inc
- https://github.com/pmprog/TigerMothC64/blob/1acaeb7d5faf069f3406cfd68dbdb6c6a88344df/Compile.bat
- https://github.com/pmprog/TigerMothC64/blob/1acaeb7d5faf069f3406cfd68dbdb6c6a88344df/LICENSE

### Classification (reviewed)

Substantive native game implementation; no README or completion claim is required for inclusion.
- https://github.com/pmprog/TigerMothC64/blob/1acaeb7d5faf069f3406cfd68dbdb6c6a88344df/tigermoth.asm
- https://github.com/pmprog/TigerMothC64/blob/1acaeb7d5faf069f3406cfd68dbdb6c6a88344df/screen_game.inc
- https://github.com/pmprog/TigerMothC64/blob/1acaeb7d5faf069f3406cfd68dbdb6c6a88344df/Compile.bat
- https://github.com/pmprog/TigerMothC64/blob/1acaeb7d5faf069f3406cfd68dbdb6c6a88344df/LICENSE

### Source CPU (not-applicable)

This is newly authored native software or development tooling, not analysis of a predecessor binary. Source platform/CPU/language are intentionally empty; output architecture is recorded separately.
- https://github.com/pmprog/TigerMothC64/blob/1acaeb7d5faf069f3406cfd68dbdb6c6a88344df/tigermoth.asm
- https://github.com/pmprog/TigerMothC64/blob/1acaeb7d5faf069f3406cfd68dbdb6c6a88344df/screen_game.inc
- https://github.com/pmprog/TigerMothC64/blob/1acaeb7d5faf069f3406cfd68dbdb6c6a88344df/Compile.bat
- https://github.com/pmprog/TigerMothC64/blob/1acaeb7d5faf069f3406cfd68dbdb6c6a88344df/LICENSE

### Target CPU (reviewed)

Compile.bat selects TASM -65; tigermoth.asm uses 6502 instructions, VIC address $D000 and a C64 BASIC startup stub.
- https://github.com/pmprog/TigerMothC64/blob/1acaeb7d5faf069f3406cfd68dbdb6c6a88344df/tigermoth.asm
- https://github.com/pmprog/TigerMothC64/blob/1acaeb7d5faf069f3406cfd68dbdb6c6a88344df/screen_game.inc
- https://github.com/pmprog/TigerMothC64/blob/1acaeb7d5faf069f3406cfd68dbdb6c6a88344df/Compile.bat
- https://github.com/pmprog/TigerMothC64/blob/1acaeb7d5faf069f3406cfd68dbdb6c6a88344df/LICENSE

### Build (reviewed)

Compile.bat builds a PRG then launches WinVICE using local relative tool paths; no compiled release or successful independent run was established. No independent compilation, execution, gameplay or byte comparison was performed; all four build flags remain unknown.
- https://github.com/pmprog/TigerMothC64/blob/1acaeb7d5faf069f3406cfd68dbdb6c6a88344df/tigermoth.asm
- https://github.com/pmprog/TigerMothC64/blob/1acaeb7d5faf069f3406cfd68dbdb6c6a88344df/screen_game.inc
- https://github.com/pmprog/TigerMothC64/blob/1acaeb7d5faf069f3406cfd68dbdb6c6a88344df/Compile.bat
- https://github.com/pmprog/TigerMothC64/blob/1acaeb7d5faf069f3406cfd68dbdb6c6a88344df/LICENSE

### Runtime profiles (no-evidence-found)

The inspected documentation and build/implementation samples do not establish a complete minimum runnable hardware profile. No RAM or minimum CPU is inferred from platform or compiler target.
- https://github.com/pmprog/TigerMothC64/blob/1acaeb7d5faf069f3406cfd68dbdb6c6a88344df/tigermoth.asm
- https://github.com/pmprog/TigerMothC64/blob/1acaeb7d5faf069f3406cfd68dbdb6c6a88344df/screen_game.inc
- https://github.com/pmprog/TigerMothC64/blob/1acaeb7d5faf069f3406cfd68dbdb6c6a88344df/Compile.bat
- https://github.com/pmprog/TigerMothC64/blob/1acaeb7d5faf069f3406cfd68dbdb6c6a88344df/LICENSE

### AI (no-evidence-found)

No explicit development-AI contribution attribution was found in the inspected documentation, implementation/build samples and latest default-branch commit. This bounded review does not prove non-use; integration/configuration files are not contribution evidence.
- https://github.com/pmprog/TigerMothC64/blob/1acaeb7d5faf069f3406cfd68dbdb6c6a88344df/tigermoth.asm
- https://github.com/pmprog/TigerMothC64/blob/1acaeb7d5faf069f3406cfd68dbdb6c6a88344df/screen_game.inc
- https://github.com/pmprog/TigerMothC64/blob/1acaeb7d5faf069f3406cfd68dbdb6c6a88344df/Compile.bat
- https://github.com/pmprog/TigerMothC64/blob/1acaeb7d5faf069f3406cfd68dbdb6c6a88344df/LICENSE
- https://github.com/pmprog/TigerMothC64/commit/1acaeb7d5faf069f3406cfd68dbdb6c6a88344df

### Relationships (reviewed)

Coherent author game source with shared local routines, MIT copyright 2017 Marq Watkin. No predecessor or copied game lineage identified in the inspected source. The repository URL and title were compared with the current catalogue; no equivalent project record was found.
- https://github.com/pmprog/TigerMothC64/blob/1acaeb7d5faf069f3406cfd68dbdb6c6a88344df/tigermoth.asm
- https://github.com/pmprog/TigerMothC64/blob/1acaeb7d5faf069f3406cfd68dbdb6c6a88344df/screen_game.inc
- https://github.com/pmprog/TigerMothC64/blob/1acaeb7d5faf069f3406cfd68dbdb6c6a88344df/Compile.bat
- https://github.com/pmprog/TigerMothC64/blob/1acaeb7d5faf069f3406cfd68dbdb6c6a88344df/LICENSE

## Sources

```json
[
  {
    "first_indexed": "2026-10-15",
    "id": "github-ebenupton-lander",
    "kind": "github-repository",
    "last_reviewed": "2026-10-15",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Lander: BBC Micro port of the Archimedes demo; primary README/build/implementation and latest commit inspected.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/ebenupton/lander"
  },
  {
    "first_indexed": "2026-10-15",
    "id": "github-skiltonusa-amiga-mcp-debugger",
    "kind": "github-repository",
    "last_reviewed": "2026-10-15",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Amiga MCP Debugger: cooperative ZZ9000 ARM debugging; primary README/build/implementation and latest commit inspected.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/SkiltonUSA/Amiga-MCP-Debugger"
  },
  {
    "first_indexed": "2026-10-15",
    "id": "github-bruno-frederic-dctelnet",
    "kind": "github-repository",
    "last_reviewed": "2026-10-15",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "DCTelnet: maintained Amiga Telnet and BBS client; primary README/build/implementation and latest commit inspected.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/bruno-frederic/dctelnet"
  },
  {
    "first_indexed": "2026-10-15",
    "id": "github-kalmalyzer-adpcm-68k",
    "kind": "github-repository",
    "last_reviewed": "2026-10-15",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "IMA ADPCM: Amiga/ST decoder and Paula replay library; primary README/build/implementation and latest commit inspected.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/Kalmalyzer/adpcm-68k"
  },
  {
    "first_indexed": "2026-10-15",
    "id": "github-arnaud-carre-sndh-player",
    "kind": "github-repository",
    "last_reviewed": "2026-10-15",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "SNDH/YM Archive Player: Atari music inspection and WAV export; primary README/build/implementation and latest commit inspected.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/arnaud-carre/sndh-player"
  },
  {
    "first_indexed": "2026-10-15",
    "id": "github-rolsen74-rvncd",
    "kind": "github-repository",
    "last_reviewed": "2026-10-15",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "rVNCd: native Amiga VNC server; primary README/build/implementation and latest commit inspected.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/rolsen74/rvncd"
  },
  {
    "first_indexed": "2026-10-15",
    "id": "github-jpewdev-c64-monster-attack",
    "kind": "github-repository",
    "last_reviewed": "2026-10-15",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Monster Attack: C64 adventure-engine game; primary README/build/implementation and latest commit inspected.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/JPEWdev/c64-monster-attack"
  },
  {
    "first_indexed": "2026-10-15",
    "id": "github-richardtnd-storm-chase",
    "kind": "github-repository",
    "last_reviewed": "2026-10-15",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Storm Chase: C64 source and 64tass conversion; primary README/build/implementation and latest commit inspected.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/RichardTND/Storm-Chase"
  },
  {
    "first_indexed": "2026-10-15",
    "id": "github-pmprog-tigermothc64",
    "kind": "github-repository",
    "last_reviewed": "2026-10-15",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Tiger Moth: C64 assembly game source; primary README/build/implementation and latest commit inspected.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/pmprog/TigerMothC64"
  }
]
```

## Source updates

```json
[
  {
    "id": "github-freemint-libcmini",
    "last_reviewed": "2026-10-15",
    "review_state": "substantially-reviewed"
  }
]
```

## Task updates

```json
[
  {
    "id": "task-review-libcmini-native-runtime",
    "last_reviewed": "2026-10-15",
    "notes_append": "Reviewed current Makefile, sources/crt0.S and sources/puts.c; promoted libcmini with verified 68000/ColdFire output scope and upstream LGPL provenance. No independent build or runtime test.",
    "state": "done"
  }
]
```

## Research event notes

Screened 80 repository-search results plus explicit/saved-queue leads locally before evidence review. Skipped existing AtariST MiSTer, MiSTery, SunDog, GODLIB, Atari ST ROM listings, Geneva, PSGPlay, Monty on the Run, Ninja Carnage, Snout About, The Race C128, Burger Time, Soulless, FoodTruck, Silk Dust and other resolved hits. Commando 2084 matches commando-c64. Existing Skramble and Erasoft deferrals remain unresolved; no repeated decision rows added. Game-specific-emulation backlog policy preserved; no game-specific hosts promoted. Broader newly seen search hits remain unreviewed, not excluded.
