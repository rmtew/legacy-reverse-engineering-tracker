# Review nine material post-pass changes across reconstruction fidelity, emulated protocol/runtime tests, format tooling and explicit AI evidence; add the newly surfaced Spider-claude research archive.

Review nine material post-pass changes across reconstruction fidelity, emulated protocol/runtime tests, format tooling and explicit AI evidence; add the newly surfaced Spider-claude research archive.

Date: 2026-10-22 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- wing-commander-kilrathi-saga-reconstruction / Target CPU (no-evidence-found): The current README documents Windows, Linux and macOS port packages but no fixed output CPU. Supported architectures are not inferred from C/C++ portability or operating-system names.
- wing-commander-kilrathi-saga-reconstruction / Build (reviewed): The tracker reviewed the commit and upstream verification report but did not compile, execute, byte-compare or gameplay-test this revision.
- wing-commander-kilrathi-saga-reconstruction / Runtime profiles (no-evidence-found): Needs user-supplied Kilrathi Saga data; partial DOS-data compatibility and Mac SuperWingCommander demo mode documented. Modern native host CPU minimum not established.
- symphony-of-night-decompilation / Build (reviewed): No candidate code was compiled or executed by the tracker; matching, runtime fidelity and project-wide completeness remain upstream claims.
- symphony-of-night-decompilation / Runtime profiles (no-evidence-found): No independently verified minimum hardware profile established.
- symphony-of-night-decompilation / AI (no-evidence-found): No explicit completed-work AI disclosure established in inspected evidence. Config files, workflow instructions and algorithmic neural features alone are not proof of authorship.
- firestaff-dungeon-master-engine / Build (reviewed): The upstream note explicitly limits this to listed startup routes: SDL dummy video/audio does not prove native display, physical input, audible output or full gameplay, and only the Atari STX CSB case carries the menu label.
- firestaff-dungeon-master-engine / Relationships (needs-research): The current status material establishes original-media and cross-edition provenance, but the wider predecessor/successor/fork graph remains unreviewed. Next check: Check predecessor/successor/fork and credited-source relationships. Next check: Check predecessor/successor/fork and credited-source relationships.
- ghidra-retro-machines / Build (reviewed): These are upstream test results reviewed from the commit; the tracker did not run Ghidra, the unit suite or the ROM corpus.
- ghidra-retro-machines / Runtime profiles (no-evidence-found): The new analyzers add no minimum host CPU or RAM evidence; existing Ghidra/JDK software prerequisites remain distinct from hardware minima.
- cpc-speaking-vector-head-z80 / Build (reviewed): The stub deliberately does not implement the letter-to-sound rules. This proves the emulated protocol path only, not the physical LambdaSpeak card, native audio, display, input or full program behavior; the tracker did not run the script.
- cpc-speaking-vector-head-z80 / Runtime profiles (no-evidence-found): The reviewed commit adds an emulated LambdaSpeak protocol stub but states no minimum CPC model, RAM or physical-card configuration. Existing speech-hardware and separately obtained NRL-driver requirements remain, so no hardware minimum is inferred.
- fadden-ciderpress2 / Target CPU (no-evidence-found): No minimum host instruction set established; a retro input platform is not a host CPU requirement.
- fadden-ciderpress2 / Build (reviewed): The tracker inspected the source diff and upstream tests but did not build CiderPress II, open a StuffIt archive or validate extracted bytes independently.
- fadden-ciderpress2 / Runtime profiles (no-evidence-found): No verified minimum CPU/RAM/OS profile established beyond the qualified dependency and format notes; no runtime test was performed.
- fadden-ciderpress2 / AI (no-evidence-found): No explicit development-AI contribution disclosure was established in the inspected material; absence does not establish non-use. Agent configuration or MCP integration alone does not establish authorship.
- magnarharestad-magsid-xplatform / Target CPU (no-evidence-found): No minimum host instruction set established; a retro input platform is not a host CPU requirement.
- magnarharestad-magsid-xplatform / Build (reviewed): These are upstream source and test assertions. The tracker did not run .NET tests, execute the 6502 player or verify SID output independently.
- magnarharestad-magsid-xplatform / Runtime profiles (no-evidence-found): No verified minimum CPU/RAM/OS profile established beyond the qualified dependency and format notes; no runtime test was performed.
- moria8-6502-multiplatform / Source CPU (no-evidence-found): The documented source lineages are VMS Pascal and C Umoria; no original executable ISA is established by the reviewed material, so source_cpu remains empty.
- moria8-6502-multiplatform / Build (reviewed): The tracker reviewed the assembly, harness and Makefile changes but did not build any platform, run VICE/MAME/x16emu or reproduce the AI playtester findings.
- amazing-spiderman-rooms-editor / Target CPU (no-evidence-found): The inspected portable/high-level build material does not establish a fixed output CPU or minimum hardware requirement; the target CPU stays unknown.
- amazing-spiderman-rooms-editor / Build (reviewed): No branch was built or executed by the tracker, and the branch pointer does not establish cross-platform data compatibility or a minimum host configuration.
- amazing-spiderman-rooms-editor / Runtime profiles (no-evidence-found): No independently verified runtime profile was established for The Amazing Spider-Man — ROOMS.SPL editor. Upstream platform or test claims are recorded as claims rather than verified hardware requirements.
- spider-claude-amazing-spiderman-research / Source CPU (no-evidence-found): The reviewed README names a DOS executable, EXEPACK, radare2 and DOSBox but does not explicitly identify the original instruction-set architecture. No CPU is inferred from the DOS platform or executable format.
- spider-claude-amazing-spiderman-research / Build (reviewed): The tracker did not run the decoders or tests, provide game files, compare images or validate the partially understood movement table.
- spider-claude-amazing-spiderman-research / Runtime profiles (no-evidence-found): Python 3.9+ and Pillow are explicit software prerequisites, but the inspected documentation gives no minimum host CPU, RAM or operating-system requirement; no runtime profile is fabricated.

## Spider-claude — AI-assisted Amazing Spider-Man asset research

Project ID: spider-claude-amazing-spiderman-research · Overall audit: reviewed

### Typed catalogue values

```json
{
  "ai": {
    "evidence": [
      "README explicitly describes an early Claude-assisted reverse-engineering experiment and latest commit is coauthored by Claude"
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
  "display_title": "Spider-claude — AI-assisted Amazing Spider-Man asset research",
  "github": {
    "activity_state": "active",
    "archived": true,
    "checked_at": "2026-10-22",
    "created_at": "2026-10-21",
    "default_branch": "main",
    "fork": false,
    "languages": [
      "Python"
    ],
    "latest_commit": {
      "date": "2026-10-21",
      "message": "docs: note README is an early LLM RE experiment; editor is current",
      "sha": "75fbe2df49aa77bace7e272f69bc0e4af1a725c2",
      "url": "https://github.com/hughdavenport/Spider-claude/commit/75fbe2df49aa77bace7e272f69bc0e4af1a725c2"
    },
    "primary_language": "Python",
    "pushed_at": "2026-10-21",
    "repository": "hughdavenport/Spider-claude",
    "tracking_branch": "main",
    "tracking_path": null,
    "updated_at": "2026-10-21"
  },
  "id": "spider-claude-amazing-spiderman-research",
  "last_activity": "2026-10-21",
  "last_checked": "2026-10-22",
  "re_started": null,
  "reconstructed_languages": [
    "Python",
    "Markdown"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/hughdavenport/Spider-claude",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [
    "DOS"
  ],
  "status": "Archived record of Claude-assisted DOS asset reverse engineering and Python decoders; superseded by spidey-editor; independent execution not performed",
  "subjects": [
    "Spider-claude",
    "The Amazing Spider-Man (1990 DOS)"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build",
    "archived"
  ],
  "target_cpu": [],
  "target_kinds": [],
  "target_platforms": [],
  "techniques": [
    "radare2-assisted analysis",
    "DOSBox investigation",
    "EXEPACK unpacking",
    "asset decoding"
  ],
  "title": "Spider-claude",
  "tool_kinds": [
    "binary-analysis",
    "asset-tool"
  ],
  "types": [
    "archived reverse-engineering research",
    "game asset decoder"
  ],
  "upstream_name": "Spider-claude",
  "work_kinds": [
    "binary-analysis",
    "data-format-analysis"
  ]
}
```

### Identity (reviewed)

The author identifies Spider-claude as archived reverse-engineering notes and Python decoders for The Amazing Spider-Man's DOS assets, including EGA/CGA graphics, EXEPACK handling, palettes and partial movement-table research.
- https://github.com/hughdavenport/Spider-claude/blob/75fbe2df49aa77bace7e272f69bc0e4af1a725c2/README.md

### Classification (reviewed)

This is substantive game-specific binary/data-format research and asset-decoder tooling, not a game port or ordinary mirror. The repository is archived and explicitly preserved as a process record.
- https://github.com/hughdavenport/Spider-claude/blob/75fbe2df49aa77bace7e272f69bc0e4af1a725c2/README.md

### Source CPU (no-evidence-found)

The reviewed README names a DOS executable, EXEPACK, radare2 and DOSBox but does not explicitly identify the original instruction-set architecture. No CPU is inferred from the DOS platform or executable format.
- https://github.com/hughdavenport/Spider-claude/blob/75fbe2df49aa77bace7e272f69bc0e4af1a725c2/README.md

### Target CPU (not-applicable)

The outputs are host-side Python decoders, notes and extracted images rather than a translated native retro executable, so a retro output CPU is not applicable.
- https://github.com/hughdavenport/Spider-claude/blob/75fbe2df49aa77bace7e272f69bc0e4af1a725c2/README.md

### Build (reviewed)

README usage runs decode_sprites.py on user-supplied files and documents pytest; Python 3.9+ and Pillow are required. No game files or decoded assets are included. Limitations: The tracker did not run the decoders or tests, provide game files, compare images or validate the partially understood movement table.
- https://github.com/hughdavenport/Spider-claude/blob/75fbe2df49aa77bace7e272f69bc0e4af1a725c2/README.md

### Runtime profiles (no-evidence-found)

Python 3.9+ and Pillow are explicit software prerequisites, but the inspected documentation gives no minimum host CPU, RAM or operating-system requirement; no runtime profile is fabricated.
- https://github.com/hughdavenport/Spider-claude/blob/75fbe2df49aa77bace7e272f69bc0e4af1a725c2/README.md

### AI (reviewed)

The author explicitly calls the work an early reverse-engineering experiment with Claude driving radare2 and DOSBox; the latest documentation commit is also coauthored by Claude.
- https://github.com/hughdavenport/Spider-claude/blob/75fbe2df49aa77bace7e272f69bc0e4af1a725c2/README.md
- https://github.com/hughdavenport/Spider-claude/commit/75fbe2df49aa77bace7e272f69bc0e4af1a725c2

### Relationships (reviewed)

The README names spidey-editor as the maintained companion and says it implements every format worked out here. Spider-claude remains a distinct archived research/process record rather than a second current editor.
- https://github.com/hughdavenport/Spider-claude/blob/75fbe2df49aa77bace7e272f69bc0e4af1a725c2/README.md
- https://github.com/hughdavenport/spidey-editor/commit/c62a683551abcd56c012c92cff2c66089e5d82af

## wing-commander-kilrathi-saga-reconstruction

Project ID: wing-commander-kilrathi-saga-reconstruction · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "wing-commander-kilrathi-saga-reconstruction",
  "last_checked": "2026-10-22",
  "status": "working Win32 reconstruction and SDL2 port; upstream reports 95.6796% strict whole-file matching and 1,380/1,550 normalized exact functions after save-loader and mouse-register recovery, while byte identity and gameplay completeness remain explicitly incomplete"
}
```

Expected existing project SHA256: 1e6d8b771f69da581f5c2a9f099c03e502e2ff0ac834e31d11ca3af959b34e53

### Identity (reviewed)

Recovered native C/C++ game source for1996 Win32 Wing Commander, plus SDL2 port and annotated original-binary comparison workflow.
- https://github.com/neuromancer/wc1-re/blob/f2afbcd542e60fa039a52b0b58518a11a0069f11/README.md
- https://github.com/neuromancer/wc1-re/blob/f2afbcd542e60fa039a52b0b58518a11a0069f11/Makefile

### Classification (reviewed)

Byte-for-byte reconstruction explicitly incomplete; annotated per-function report can miss unreconstructed routines between functions and is not gameplay completeness. Native recovered gameplay logic exists; not a generic CPU wrapper. GPL3 root LICENSE; proprietary data not distributed.
- https://github.com/neuromancer/wc1-re/blob/f2afbcd542e60fa039a52b0b58518a11a0069f11/README.md
- https://github.com/neuromancer/wc1-re/blob/f2afbcd542e60fa039a52b0b58518a11a0069f11/Makefile

### Source CPU (reviewed)

Documented source/input platforms: Windows, DOS. Processor scope: x86.
- https://github.com/neuromancer/wc1-re/blob/f2afbcd542e60fa039a52b0b58518a11a0069f11/README.md
- https://github.com/neuromancer/wc1-re/blob/f2afbcd542e60fa039a52b0b58518a11a0069f11/Makefile

### Target CPU (no-evidence-found)

The current README documents Windows, Linux and macOS port packages but no fixed output CPU. Supported architectures are not inferred from C/C++ portability or operating-system names.
- https://github.com/neuromancer/wc1-re/blob/3708d5f616feb26ed5256bec027f812dc26e1a09/README.md

### Build (reviewed)

The post-review commit changes LoadGame transfer qualifiers/order and MainWindowProc local order, raising strict whole-file matching by 112 positions to 496,248 of 518,656 (95.6796%) and normalized exact functions to 1,380 of 1,550. Upstream reports clean native and modern builds plus value checks over all 1,550 functions; the remaining 22,408 differing positions and five size-different functions keep byte identity explicitly incomplete. Limitations: The tracker reviewed the commit and upstream verification report but did not compile, execute, byte-compare or gameplay-test this revision.
- https://github.com/neuromancer/wc1-re/commit/3708d5f616feb26ed5256bec027f812dc26e1a09
- https://github.com/neuromancer/wc1-re/commit/97fb25240329fe35151030f9bee29d30856dd1eb
- https://github.com/neuromancer/wc1-re/blob/3708d5f616feb26ed5256bec027f812dc26e1a09/README.md
- https://github.com/neuromancer/wc1-re/commit/d1e0fdee262380446ac72f617e408831ea7273be

### Runtime profiles (no-evidence-found)

Needs user-supplied Kilrathi Saga data; partial DOS-data compatibility and Mac SuperWingCommander demo mode documented. Modern native host CPU minimum not established.
- https://github.com/neuromancer/wc1-re/blob/f2afbcd542e60fa039a52b0b58518a11a0069f11/README.md
- https://github.com/neuromancer/wc1-re/blob/f2afbcd542e60fa039a52b0b58518a11a0069f11/Makefile

### AI (reviewed)

README explicitly states Codex and Claude were used during reconstruction; actual contribution evidence rather than AGENTS presence.
- https://github.com/neuromancer/wc1-re/blob/f2afbcd542e60fa039a52b0b58518a11a0069f11/README.md
- https://github.com/neuromancer/wc1-re/blob/f2afbcd542e60fa039a52b0b58518a11a0069f11/Makefile

### Relationships (reviewed)

Acknowledged historical compatibility fixes/research reference. https://github.com/Bekenn/wcdx Optional comparison/verification dependency. https://github.com/gg-sl-oss/binary-comp
- https://github.com/neuromancer/wc1-re/blob/f2afbcd542e60fa039a52b0b58518a11a0069f11/README.md
- https://github.com/neuromancer/wc1-re/blob/f2afbcd542e60fa039a52b0b58518a11a0069f11/Makefile

## symphony-of-night-decompilation

Project ID: symphony-of-night-decompilation · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "symphony-of-night-decompilation",
  "last_checked": "2026-10-22",
  "status": "Multi-platform/version reconstruction; upstream finished RLIB data extraction for US and PSP/EU so both RLIB symbol files are empty, without establishing equal source completeness across the wider PS1/PSP/Saturn project"
}
```

Expected existing project SHA256: 8fe2c0a27d785bf66ecc1f5f3da1e44d677907175e652bfde148862d739eadcd

### Identity (reviewed)

Multi-platform/version reconstruction with actual palette-state C alongside remaining INCLUDE_ASM stubs. Own game assets required; matching builds do not mean equal source completeness across PS1/PSP/Saturn targets.
- https://github.com/Xeeynamo/sotn-decomp
- https://github.com/Xeeynamo/sotn-decomp/blob/66a337e30f839a9c724ae008190d3dc60a6b5392/src/dra/4A538.c
- https://github.com/Xeeynamo/sotn-decomp/blob/66a337e30f839a9c724ae008190d3dc60a6b5392/README.md

### Classification (reviewed)

Inspected source supports game / decompilation. Multi-platform/version reconstruction with actual palette-state C alongside remaining INCLUDE_ASM stubs. Own game assets required; matching builds do not mean equal source completeness across PS1/PSP/Saturn targets.
- https://github.com/Xeeynamo/sotn-decomp
- https://github.com/Xeeynamo/sotn-decomp/blob/66a337e30f839a9c724ae008190d3dc60a6b5392/src/dra/4A538.c
- https://github.com/Xeeynamo/sotn-decomp/blob/66a337e30f839a9c724ae008190d3dc60a6b5392/README.md

### Source CPU (reviewed)

Source architecture: MIPS, SH-2.
- https://github.com/Xeeynamo/sotn-decomp
- https://github.com/Xeeynamo/sotn-decomp/blob/66a337e30f839a9c724ae008190d3dc60a6b5392/src/dra/4A538.c
- https://github.com/Xeeynamo/sotn-decomp/blob/66a337e30f839a9c724ae008190d3dc60a6b5392/README.md

### Target CPU (reviewed)

Target architecture: MIPS, SH-2.
- https://github.com/Xeeynamo/sotn-decomp
- https://github.com/Xeeynamo/sotn-decomp/blob/66a337e30f839a9c724ae008190d3dc60a6b5392/src/dra/4A538.c
- https://github.com/Xeeynamo/sotn-decomp/blob/66a337e30f839a9c724ae008190d3dc60a6b5392/README.md

### Build (reviewed)

Upstream's RLIB completion commit adds US and PSP/EU room, sprite, palette, graphics-bank, stage-data and tilemap segments and leaves both RLIB symbol files empty. This closes that library's data-extraction slice; it is not evidence that every version or component is fully decompiled. Limitations: No candidate code was compiled or executed by the tracker; matching, runtime fidelity and project-wide completeness remain upstream claims.
- https://github.com/Xeeynamo/sotn-decomp
- https://github.com/Xeeynamo/sotn-decomp/blob/66a337e30f839a9c724ae008190d3dc60a6b5392/src/dra/4A538.c
- https://github.com/Xeeynamo/sotn-decomp/blob/66a337e30f839a9c724ae008190d3dc60a6b5392/README.md
- https://github.com/Xeeynamo/sotn-decomp/commit/2be55ee17221ee306e330edf2df2d49d48ba47ae

### Runtime profiles (no-evidence-found)

No independently verified minimum hardware profile established.
- https://github.com/Xeeynamo/sotn-decomp
- https://github.com/Xeeynamo/sotn-decomp/blob/66a337e30f839a9c724ae008190d3dc60a6b5392/src/dra/4A538.c
- https://github.com/Xeeynamo/sotn-decomp/blob/66a337e30f839a9c724ae008190d3dc60a6b5392/README.md

### AI (no-evidence-found)

No explicit completed-work AI disclosure established in inspected evidence. Config files, workflow instructions and algorithmic neural features alone are not proof of authorship.
- https://github.com/Xeeynamo/sotn-decomp
- https://github.com/Xeeynamo/sotn-decomp/blob/66a337e30f839a9c724ae008190d3dc60a6b5392/src/dra/4A538.c
- https://github.com/Xeeynamo/sotn-decomp/blob/66a337e30f839a9c724ae008190d3dc60a6b5392/README.md

### Relationships (reviewed)

Screened URL, title and prior decisions. GitHub fork flag is not treated as conclusive lineage evidence.
- https://github.com/Xeeynamo/sotn-decomp
- https://github.com/Xeeynamo/sotn-decomp/blob/66a337e30f839a9c724ae008190d3dc60a6b5392/src/dra/4A538.c
- https://github.com/Xeeynamo/sotn-decomp/blob/66a337e30f839a9c724ae008190d3dc60a6b5392/README.md

## firestaff-dungeon-master-engine

Project ID: firestaff-dungeon-master-engine · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "firestaff-dungeon-master-engine",
  "last_checked": "2026-10-22",
  "status": "v3.0.402 published; subsequent upstream retest passes 11/11 authenticated CSB/DM2 CLI startup routes, while native presentation, input, audio and full-game parity remain explicitly unproven"
}
```

Expected existing project SHA256: 356c41ae3f41625c1acc19d2b0f952976b74fc66ab2eb699f2f4e26796fb726f

### Identity (reviewed)

Clean-room Dungeon Master-family engine using authenticated original media. Current primary documentation records bounded startup/runtime coverage for DM1 on DOS, Atari ST, Amiga and FM Towns; CSB on Amiga, Atari ST and FM Towns; and DM2 on DOS, Amiga, FM Towns and Macintosh. The latest receipts correct DM1 Amiga HD and DM2 FM Towns boot assertions and expand the cross-game startup matrix and diagnostics. These source-owned handoffs do not establish full campaign, save, display or audio parity; Nexus and Theron's Quest remain explicitly bounded, with authentic level/campaign consumers still incomplete. Evidence: https://github.com/yeager/firestaff/blob/main/README.md https://github.com/yeager/firestaff/blob/main/docs/PROJECT_STATUS.md https://github.com/yeager/firestaff/commit/7791b08de76e https://github.com/yeager/firestaff/commit/17a20bdb465e The newest authenticated-media pass discovers the DM1 Amiga 3.6 archive from configured data roots, covers its root-menu scan, records an Amiga startup-media matrix and wires DM1 PC34 soundtrack selection to WAV playback. These remain bounded startup/audio receipts rather than full-game parity. Evidence: https://github.com/yeager/firestaff/commit/d3b50c77c364455674d783c6bf4d4755777dbc44 https://github.com/yeager/firestaff/commit/ec51d5c1b2f58b51b235fc2145abb384d55b597c https://github.com/yeager/firestaff/commit/da1e85756e618dd321ec42257cb31afbb2b341d1 v3.0.376 receipts now cover DM1 Amiga 2.0 resume, the published Linux x86-64 AppImage under QEMU on an ARM64 VM, and the DM2 FM Towns selected-hero HUD icon sourced from authenticated interface data. They do not establish native x86-64 hardware, physical input, aura/panel completion or full visual parity. The release also publishes Android and iOS arm64 artifacts; publication alone is not runtime verification. Evidence: https://github.com/yeager/firestaff/releases/tag/v3.0.376 https://github.com/yeager/firestaff/commit/e0cf778c39b039918d6b1ae1ebf18e23ec423b1a https://github.com/yeager/firestaff/commit/f0c58017d243551f9dbf30ae5b28fb25172bd10e https://github.com/yeager/firestaff/commit/1be613b14f3cef9e2323a3e2b6ed840e13f6c480 Current-main receipts add native Mac mini M4 DM1 title/door pacing into runtime and authenticated FM Towns startup checks for DM1, CSB and DM2. A four-run French Atari ST test also narrowed an earlier no-output incident to a plausible uninitialized-menu fallback, while explicitly leaving historical causation, physical input, display/palette and audible-speaker parity open. Evidence: https://github.com/yeager/firestaff/commit/7256c2f693a8f2a609ebccfcb687f5e1f8c00868 https://github.com/yeager/firestaff/commit/47bc75ce1f897306e74d2e79a0c053209684edd9 https://github.com/yeager/firestaff/commit/3b729320e80658a8eae965f11c1b5f1bd880f5a3 Current-main Amiga work now paces DM1 A20 palette fades and title zooms against absolute 20 ms source deadlines rather than adding host VSync latency. An authentic Amiga v2.0 native Cocoa run on a Mac mini M4 completed the five-fade title in 1,698 ms (366 ms zoom, 500 ms hold, 166 ms final fade); this does not establish HiDPI/pixel parity or beam-line 152 timing. The authenticated Japanese FM Towns CSB save regression now asserts restored map 0, party position 13,13, direction 1 and four champions through direct launch and the live menu-resume route. Evidence: https://github.com/yeager/firestaff/commit/1538eeab7f46d6318be1c6cd89a55a9edc6d5d87 https://github.com/yeager/firestaff/commit/1d3f8e34d62d0cd9b95d74d9fd33b1bb35eb1a6e https://github.com/yeager/firestaff/commit/087aed4bf4b977cb30805152519c82860ff2ed20 Current-main receipts add an authenticated DM2 Amiga viewport gate, bounded DOS viewport/HUD checks and a locked three-draw fresh-weather RNG bootstrap. Separate native Mac M4 tests keep live Retina input unresolved despite controlled 2x/mixed-geometry tests, and real-media startup reruns use dummy video/audio, so they do not establish physical display, input or speaker parity. Evidence: https://github.com/yeager/firestaff/commit/a3740b43a7bce6f783a003c0dacc312cb2430809 https://github.com/yeager/firestaff/commit/2420045a10244b0431932352c07b5de7328dfe33 https://github.com/yeager/firestaff/commit/b9989304f0e931fc9350ee4b7ac01fa861f2c882 https://github.com/yeager/firestaff/commit/f8465d8e0131e982e296b388e7f66ca62d77e48a https://github.com/yeager/firestaff/commit/a8ff9e734b4ff2837a62e5d2a426455770ee2b0a The newest DM1 pass ports FM Towns title shrink sampling from the documented 6-bit fixed-point source path, flips floor/ceiling graphics at their loaded native heights, and restores the entrance-door step to three 60 Hz VBlank intervals. A separate authenticated PC 3.4 path decodes the LZEXE-packed DOS selector preview. Targeted source-lock/native-build checks pass upstream, but the author explicitly retains original-frame comparison and full cross-platform visual parity as open. Evidence: https://github.com/yeager/firestaff/commit/9a2b86019bfcd6bd513213bc21cd402a4f5adaf0 https://github.com/yeager/firestaff/commit/2a85ec7e1801b58d22232fa11ccc5f18a0e9bd0d https://github.com/yeager/firestaff/commit/41b103f29b4d7439d7445fb4e3578f9985e5cfab https://github.com/yeager/firestaff/commit/3085c2f6d56e8088279b5207bfd46744a1dbbd24 The Apple IIGS path now decodes original dungeon worlds, graphics, startup/font, creature/effect metadata and sound, launches authenticated worlds through the CLI/M12 path, and connects native IIGS mirror recruitment. Primary recovered documentation explicitly identifies hidden Apple IIGS graphics.dat code as 65C816 code, supporting the added source architecture. Current changelog receipts also cover stereo DOC effects, Hall progression, inventory transfer, food use and carrying capacity; wall damage, sensors and full sound/presentation parity remain open. No Apple IIGS minimum RAM or host profile is inferred. Evidence: https://github.com/yeager/firestaff/commit/26f1361e5b3d18512db35b7b0791b84f4e4385da https://github.com/yeager/firestaff/commit/9a7458e5fc0b0f019cbe4284bd9d68384050a56b https://github.com/yeager/firestaff/blob/439213c5ba9fbd79d0753d6143a3b86ff9f0d90f/reference/dmweb-community-docs/html/community/documentation/dungeon-master-and-chaos-strikes-back/graphics.dat-hidden-code.html The DM1 PC34 path now preserves the original status-box priority over overlapping ready-hand zones, verifies consecutive champion switches with authenticated data and prevents held-key selector skips. Debug traces separately measure queue, source-outcome and present-return timing while explicitly marking physical scanout unmeasured. Evidence: https://github.com/yeager/firestaff/commit/449d2322fcf641e88cf876a032ee2cc58ca96373 https://github.com/yeager/firestaff/commit/e5b732073270bbb500d10919239185d212ad6d44 The authenticated DM1 Apple IIGS G20E/G21E editions now reach the first world through both direct CLI and M12 menu launch; the CLI route also accepts a native keyboard turn, and the original media archive is hash-checked before and after the run. The upstream check uses SDL dummy output, so original title/entrance presentation, audible DOC playback and complete-campaign parity remain open. A v3.0.387 preparation change is not represented as a published release because no corresponding release was available when checked. Evidence: https://github.com/yeager/firestaff/commit/c9d9b0e0097242ea1a6f1e5fa29183c3e09bfabb Firestaff v3.0.391 is a published release. Its primary notes record DM1 PC34 selected-save restoration, authenticated English/Japanese CSB FM Towns loose-file startup, and Amiga 3.6 French/German graphic selection. Only seven of ten localized bitmap records are decoded for comparison, and upstream explicitly says these checks do not establish complete visual or gameplay parity. Evidence: https://github.com/yeager/firestaff/releases/tag/v3.0.391 https://github.com/yeager/firestaff/commit/ebb10387f277af76683e3aadd27f97dab963d599 https://github.com/yeager/firestaff/commit/d15a674ba936133e9b74b43af982051927f51207 Firestaff v3.0.397 reuses verified hashes for nested archive members while retaining archive freshness checks. On the tested Mac mini M4, the authentic five-game scan took 27.90 seconds cold and 12.35 seconds warm; other platforms and cold-cache performance remain explicitly unverified, and SDL dummy checks do not establish native display, physical input, audible output or complete parity. Evidence: https://github.com/yeager/firestaff/releases/tag/v3.0.397
- https://github.com/yeager/firestaff

### Classification (reviewed)

Current documentation continues to describe source-faithful clean-room runtime/reimplementation plus platform-specific binary/data analysis.
- https://github.com/yeager/firestaff

### Source CPU (reviewed)

Recovered primary Apple IIGS documentation explicitly identifies code embedded in graphics.dat as 65C816 code. The project record adds 65C816 without inferring any host or minimum runtime architecture.
- https://github.com/yeager/firestaff/blob/439213c5ba9fbd79d0753d6143a3b86ff9f0d90f/reference/dmweb-community-docs/html/community/documentation/dungeon-master-and-chaos-strikes-back/graphics.dat-hidden-code.html

### Target CPU (reviewed)

v3.0.371 publishes explicit x86-64 and arm64 host artifacts; the record uses the existing x86 family label plus arm64 without inferring older x86 minima.
- https://github.com/yeager/firestaff/releases/tag/v3.0.371

### Build (reviewed)

A post-release authenticated-media retest passes 11 of 11 current-source CSB and DM2 native CLI startup cases across Atari STX, Amiga, FM Towns, DOS and Macintosh editions, including Amiga 3.5 CTRaw and Hint Oracle. The separate DM1 menu/combat gates also remain passing. Limitations: The upstream note explicitly limits this to listed startup routes: SDL dummy video/audio does not prove native display, physical input, audible output or full gameplay, and only the Atari STX CSB case carries the menu label.
- https://github.com/yeager/firestaff/releases/tag/v3.0.402
- https://github.com/yeager/firestaff/commit/12e3ceb91a790ee5eaa4014688ea3210544b5938
- https://github.com/yeager/firestaff/commit/6c7d90c739b29e4f7d7f8a2020916fbf357554c0
- https://github.com/yeager/firestaff/commit/b05de38e1747d20a33a730e2ecc99472c829716a

### Runtime profiles (reviewed)

The existing Apple Silicon profile now records v3.0.397 scan timings on the same Mac mini M4. They are not CPU/RAM minima or evidence for other hosts.
- https://github.com/yeager/firestaff/releases/tag/v3.0.397

### AI (reviewed)

Existing explicit Claude project-agent evidence remains valid; no weaker inference was substituted.
- https://github.com/yeager/firestaff

### Relationships (needs-research)

The current status material establishes original-media and cross-edition provenance, but the wider predecessor/successor/fork graph remains unreviewed. Next check: Check predecessor/successor/fork and credited-source relationships. Next check: Check predecessor/successor/fork and credited-source relationships.
- https://github.com/yeager/firestaff

## ghidra-retro-machines

Project ID: ghidra-retro-machines · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "ghidra-retro-machines",
  "last_checked": "2026-10-22",
  "status": "Active; 6502 keyed-linear-search dispatch recovery now accepts coherent X- or Y-index loops and rejects mixed-register cases, with unit/build checks and a 35-ROM NES corpus gate reported passing"
}
```

Expected existing project SHA256: ad0475a2ca7a4d9fb4a027ed10ca44922680494e14e4c8f4803016ea439098ad

### Identity (reviewed)

Current README documents C64/C128/PET/NES machine loaders plus bundled SPC700 and 65C816 language variants; the display title now reflects both parts of the scope.
- https://github.com/CBongo/ghidra-retro-machines

### Classification (reviewed)

Current machine-aware static-analysis work makes switch overrides independent of first-reference ordering and verifies deterministic unpinned corpus output; the record remains tooling rather than a reconstructed game.
- https://github.com/CBongo/ghidra-retro-machines/commit/475eeadd4fb50ad045bd8e01dd428243279bfe2d
- https://github.com/CBongo/ghidra-retro-machines/commit/1251af61b1d65c8849bc90795d186ee274938db4
- https://github.com/CBongo/ghidra-retro-machines/commit/2a15e0df8abeeccc0842b212a00e1d08d2316e41
- https://github.com/CBongo/ghidra-retro-machines/commit/48c66e952687ddaa24979626263f9b24dbd6b11d

### Source CPU (reviewed)

Machine descriptors explicitly cover 6502/6510/8502 inputs; README separately documents bundled SPC700 and 65C816 language variants for SNES code, with their current semantic limits preserved.
- https://github.com/CBongo/ghidra-retro-machines

### Target CPU (not-applicable)

Ghidra analysis output is not a translated native retro binary.
- https://github.com/CBongo/ghidra-retro-machines

### Build (reviewed)

The changed analyzer generalizes keyed-linear-search jump-table recovery from Y-only to coherent X or Y loops and adds a guard that rejects mixed-register comparisons. Upstream reports SearchLoopDispatchProgramTest 6/6, build-and-test check OK and the NES real-ROM gate 35/35 passing; the broader 1,132-ROM scan is used only to explain why InlineJumpTableDispatch remains Y-specific. Limitations: These are upstream test results reviewed from the commit; the tracker did not run Ghidra, the unit suite or the ROM corpus.
- https://github.com/CBongo/ghidra-retro-machines/commit/8a20c6bb65074bd911008cffccff587ffc8083d4
- https://github.com/CBongo/ghidra-retro-machines/commit/95ee768b7a25e0646f3237fcc5688a88c1c8c411
- https://github.com/CBongo/ghidra-retro-machines/commit/30539debbfef0bdebf15d754ee86dd73c7a1aae1

### Runtime profiles (no-evidence-found)

The new analyzers add no minimum host CPU or RAM evidence; existing Ghidra/JDK software prerequisites remain distinct from hardware minima.
- https://github.com/CBongo/ghidra-retro-machines/commit/8a20c6bb65074bd911008cffccff587ffc8083d4
- https://github.com/CBongo/ghidra-retro-machines/commit/95ee768b7a25e0646f3237fcc5688a88c1c8c411

### AI (reviewed)

The implementation commit explicitly credits Claude Opus 5.5 and links a Claude session; attribution is scoped to this analyzer/test change rather than generalized to every project component.
- https://github.com/CBongo/ghidra-retro-machines/commit/8a20c6bb65074bd911008cffccff587ffc8083d4
- https://github.com/CBongo/ghidra-retro-machines/commit/95ee768b7a25e0646f3237fcc5688a88c1c8c411
- https://github.com/CBongo/ghidra-retro-machines/commit/30539debbfef0bdebf15d754ee86dd73c7a1aae1

### Relationships (reviewed)

README says the extension was incubated in and serves CBongo/game-music-extraction; that adjacent multi-system extraction repository is queued for independent-scope review.
- https://github.com/CBongo/ghidra-retro-machines

## cpc-speaking-vector-head-z80

Project ID: cpc-speaking-vector-head-z80 · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "cpc-speaking-vector-head-z80",
  "last_checked": "2026-10-22",
  "status": "Upstream now exercises VHLSAI.ROM's LambdaSpeak &E9 protocol end to end in MAME with a stub card; speech rules, physical hardware, audio output and minimum hardware remain unverified"
}
```

Expected existing project SHA256: b5cb4dc536677b604291bb1630755e65321a30dfa6afa4e13c5e675a1b2615ce

### Identity (reviewed)

Z80 revival of a historical BASIC vector head, with viseme animation, speech synchronization and typed-text speech integration.
- https://github.com/lambdamikel/animated-speaking-cpc-vector-head/blob/54b4a9feb0d6bf64f48d4932daecd90c1e0c0c5c/LICENSE-NOTE.md
- https://github.com/lambdamikel/animated-speaking-cpc-vector-head/blob/54b4a9feb0d6bf64f48d4932daecd90c1e0c0c5c/README.md

### Classification (reviewed)

head.asm replaces BASIC coordinate conversion and firmware drawing with precomputed screen coordinates, direct line drawing and double-buffered mouth/eye states. Separate routines hook an optional NRL speech engine. GPL-3 root licence; LICENSE-NOTE.md explicitly excludes proprietary 1985 Amstrad driver from all repository/disc files. User-supplied extracted driver remains outside project licence.
- https://github.com/lambdamikel/animated-speaking-cpc-vector-head/blob/54b4a9feb0d6bf64f48d4932daecd90c1e0c0c5c/LICENSE-NOTE.md
- https://github.com/lambdamikel/animated-speaking-cpc-vector-head/blob/54b4a9feb0d6bf64f48d4932daecd90c1e0c0c5c/README.md

### Source CPU (reviewed)

Architecture of historical host/guest or source-platform program, not a minimum runtime-machine claim.
- https://github.com/lambdamikel/animated-speaking-cpc-vector-head/blob/54b4a9feb0d6bf64f48d4932daecd90c1e0c0c5c/LICENSE-NOTE.md
- https://github.com/lambdamikel/animated-speaking-cpc-vector-head/blob/54b4a9feb0d6bf64f48d4932daecd90c1e0c0c5c/README.md

### Target CPU (reviewed)

Architecture follows inspected native code/toolchain; host-side tools leave CPU unspecified. Peripheral firmware uses its microcontroller architecture. Full minimum runtime configurations were not independently verified.
- https://github.com/lambdamikel/animated-speaking-cpc-vector-head/blob/54b4a9feb0d6bf64f48d4932daecd90c1e0c0c5c/LICENSE-NOTE.md
- https://github.com/lambdamikel/animated-speaking-cpc-vector-head/blob/54b4a9feb0d6bf64f48d4932daecd90c1e0c0c5c/README.md

### Build (reviewed)

A new MAME Lua stub and runner exercise VHLSAI.ROM's &E9 exchange end to end: the ROM sends text, the stub returns a sync byte, count and five allophones, and the test verifies those bytes reach the head's speech buffer. The commit also fixes callback lifetime by retaining MAME subscription tokens. Limitations: The stub deliberately does not implement the letter-to-sound rules. This proves the emulated protocol path only, not the physical LambdaSpeak card, native audio, display, input or full program behavior; the tracker did not run the script.
- https://github.com/lambdamikel/animated-speaking-cpc-vector-head/blob/54b4a9feb0d6bf64f48d4932daecd90c1e0c0c5c/LICENSE-NOTE.md
- https://github.com/lambdamikel/animated-speaking-cpc-vector-head/blob/54b4a9feb0d6bf64f48d4932daecd90c1e0c0c5c/README.md
- https://github.com/lambdamikel/animated-speaking-cpc-vector-head/commit/afe55fa34e144dc2d8151996245db7ab3c92913b

### Runtime profiles (no-evidence-found)

The reviewed commit adds an emulated LambdaSpeak protocol stub but states no minimum CPC model, RAM or physical-card configuration. Existing speech-hardware and separately obtained NRL-driver requirements remain, so no hardware minimum is inferred.
- https://github.com/lambdamikel/animated-speaking-cpc-vector-head/blob/54b4a9feb0d6bf64f48d4932daecd90c1e0c0c5c/LICENSE-NOTE.md
- https://github.com/lambdamikel/animated-speaking-cpc-vector-head/blob/54b4a9feb0d6bf64f48d4932daecd90c1e0c0c5c/README.md
- https://github.com/lambdamikel/animated-speaking-cpc-vector-head/commit/afe55fa34e144dc2d8151996245db7ab3c92913b

### AI (reviewed)

README credits Claude Code (Claude Opus 5) for Z80 port, animation, speech integration and documentation; assembly source credits LAMBDAMIKEL + CLAUDE. Pinned latest commit credits Claude Opus 5.5 for README link update.
- https://github.com/lambdamikel/animated-speaking-cpc-vector-head/blob/54b4a9feb0d6bf64f48d4932daecd90c1e0c0c5c/LICENSE-NOTE.md
- https://github.com/lambdamikel/animated-speaking-cpc-vector-head/blob/54b4a9feb0d6bf64f48d4932daecd90c1e0c0c5c/README.md

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/lambdamikel/animated-speaking-cpc-vector-head/blob/54b4a9feb0d6bf64f48d4932daecd90c1e0c0c5c/LICENSE-NOTE.md
- https://github.com/lambdamikel/animated-speaking-cpc-vector-head/blob/54b4a9feb0d6bf64f48d4932daecd90c1e0c0c5c/README.md

## fadden-ciderpress2

Project ID: fadden-ciderpress2 · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "fadden-ciderpress2",
  "last_checked": "2026-10-22",
  "status": "Source inspected; current upstream adds StuffIt 1.5 HMF-entry extraction and headerless LZC/LZW handling with tests, without an independent tracker build or execution"
}
```

Expected existing project SHA256: c6907983f2a6d87450020f8a3dc8acdd0814f90f85ad7d8d8ea3f5558ab3db9d

### Identity (reviewed)

CiderPress II — Apple II and vintage Macintosh media tools. Repository root and implementation inspected at pinned revisions.
- https://github.com/fadden/CiderPress2/blob/9c57f7a21d302ca9e7f49612f4a687bb6da83471/README.md
- https://github.com/fadden/CiderPress2/blob/9c57f7a21d302ca9e7f49612f4a687bb6da83471/AppCommon/FileIdentifier.cs

### Classification (reviewed)

Archive/disk inspection, extraction and conversion with format-identification and nested-container handling. CLI and Windows GUI have different host support; format recognition is not universal read/write support.
- https://github.com/fadden/CiderPress2/blob/9c57f7a21d302ca9e7f49612f4a687bb6da83471/README.md
- https://github.com/fadden/CiderPress2/blob/9c57f7a21d302ca9e7f49612f4a687bb6da83471/AppCommon/FileIdentifier.cs

### Source CPU (not-applicable)

No instruction-set dependency is established for the input format or host-side implementation. Source and target roles are recorded separately.
- https://github.com/fadden/CiderPress2/blob/9c57f7a21d302ca9e7f49612f4a687bb6da83471/README.md
- https://github.com/fadden/CiderPress2/blob/9c57f7a21d302ca9e7f49612f4a687bb6da83471/AppCommon/FileIdentifier.cs

### Target CPU (no-evidence-found)

No minimum host instruction set established; a retro input platform is not a host CPU requirement.
- https://github.com/fadden/CiderPress2/blob/9c57f7a21d302ca9e7f49612f4a687bb6da83471/README.md
- https://github.com/fadden/CiderPress2/blob/9c57f7a21d302ca9e7f49612f4a687bb6da83471/AppCommon/FileIdentifier.cs

### Build (reviewed)

The StuffIt part-two commit improves HMF-entry extraction, adds a StuffIt mode for headerless LZC/LZW streams, exposes StuffIt labels, and adds compression/sample coverage. This materially broadens the vintage-Mac archive tool rather than changing an unrelated dependency. Limitations: The tracker inspected the source diff and upstream tests but did not build CiderPress II, open a StuffIt archive or validate extracted bytes independently.
- https://github.com/fadden/CiderPress2/blob/9c57f7a21d302ca9e7f49612f4a687bb6da83471/README.md
- https://github.com/fadden/CiderPress2/blob/9c57f7a21d302ca9e7f49612f4a687bb6da83471/AppCommon/FileIdentifier.cs
- https://github.com/fadden/CiderPress2/commit/18d74168c924bdde042c43f0ca600cb477ddb694

### Runtime profiles (no-evidence-found)

No verified minimum CPU/RAM/OS profile established beyond the qualified dependency and format notes; no runtime test was performed.
- https://github.com/fadden/CiderPress2/blob/9c57f7a21d302ca9e7f49612f4a687bb6da83471/README.md
- https://github.com/fadden/CiderPress2/blob/9c57f7a21d302ca9e7f49612f4a687bb6da83471/AppCommon/FileIdentifier.cs

### AI (no-evidence-found)

No explicit development-AI contribution disclosure was established in the inspected material; absence does not establish non-use. Agent configuration or MCP integration alone does not establish authorship.
- https://github.com/fadden/CiderPress2/blob/9c57f7a21d302ca9e7f49612f4a687bb6da83471/README.md
- https://github.com/fadden/CiderPress2/blob/9c57f7a21d302ca9e7f49612f4a687bb6da83471/AppCommon/FileIdentifier.cs

### Relationships (reviewed)

CiderPress successor, with reusable DiskArc and format libraries kept under the coherent root.
- https://github.com/fadden/CiderPress2/blob/9c57f7a21d302ca9e7f49612f4a687bb6da83471/README.md
- https://github.com/fadden/CiderPress2/blob/9c57f7a21d302ca9e7f49612f4a687bb6da83471/AppCommon/FileIdentifier.cs

## magnarharestad-magsid-xplatform

Project ID: magnarharestad-magsid-xplatform · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "magnarharestad-magsid-xplatform",
  "last_checked": "2026-10-22",
  "status": "Source inspected; upstream now builds a real PSID test image and checks imported-song export against the 6502 player frame by frame, without independent tracker execution"
}
```

Expected existing project SHA256: f38dc24db34246175e36f6adfaf7d5b6c0f160763556884738e6656a51c09b9b

### Identity (reviewed)

MagSID Xplatform — cross-platform C64 tracker continuation. Repository root and implementation inspected at pinned revisions.
- https://github.com/MagnarHarestad/MagSID-Xplatform/blob/fd4b06087b53112218fa12094d533512041b25d5/README.md
- https://github.com/MagnarHarestad/MagSID-Xplatform/blob/fd4b06087b53112218fa12094d533512041b25d5/src/MagSid.Assembler/SongImageBuilder.cs
- https://github.com/MagnarHarestad/MagSID-Xplatform/blob/fd4b06087b53112218fa12094d533512041b25d5/THIRD-PARTY-NOTICES.md
- https://github.com/MagnarHarestad/MagSID-Xplatform

### Classification (reviewed)

Avalonia adaptation shares tracker/DAW code, emulated playback and a native SID exporter. Retro sound bank is still incomplete; MP3/FLAC export remains Windows-only while WAV is cross-platform.
- https://github.com/MagnarHarestad/MagSID-Xplatform/blob/fd4b06087b53112218fa12094d533512041b25d5/README.md
- https://github.com/MagnarHarestad/MagSID-Xplatform/blob/fd4b06087b53112218fa12094d533512041b25d5/src/MagSid.Assembler/SongImageBuilder.cs
- https://github.com/MagnarHarestad/MagSID-Xplatform/blob/fd4b06087b53112218fa12094d533512041b25d5/THIRD-PARTY-NOTICES.md
- https://github.com/MagnarHarestad/MagSID-Xplatform

### Source CPU (reviewed)

Architecture context: 6502. Source and target roles are recorded separately.
- https://github.com/MagnarHarestad/MagSID-Xplatform/blob/fd4b06087b53112218fa12094d533512041b25d5/README.md
- https://github.com/MagnarHarestad/MagSID-Xplatform/blob/fd4b06087b53112218fa12094d533512041b25d5/src/MagSid.Assembler/SongImageBuilder.cs
- https://github.com/MagnarHarestad/MagSID-Xplatform/blob/fd4b06087b53112218fa12094d533512041b25d5/THIRD-PARTY-NOTICES.md
- https://github.com/MagnarHarestad/MagSID-Xplatform

### Target CPU (no-evidence-found)

No minimum host instruction set established; a retro input platform is not a host CPU requirement.
- https://github.com/MagnarHarestad/MagSID-Xplatform/blob/fd4b06087b53112218fa12094d533512041b25d5/README.md
- https://github.com/MagnarHarestad/MagSID-Xplatform/blob/fd4b06087b53112218fa12094d533512041b25d5/src/MagSid.Assembler/SongImageBuilder.cs
- https://github.com/MagnarHarestad/MagSID-Xplatform/blob/fd4b06087b53112218fa12094d533512041b25d5/THIRD-PARTY-NOTICES.md
- https://github.com/MagnarHarestad/MagSID-Xplatform

### Build (reviewed)

The updated tests replace a missing external Outlaws.sid fixture by building a PSID from the repository's demo song, then import it through the 6502 path. Three additional tests export imported songs and compare the generated 6502 player with the editor sequencer frame by frame. Limitations: These are upstream source and test assertions. The tracker did not run .NET tests, execute the 6502 player or verify SID output independently.
- https://github.com/MagnarHarestad/MagSID-Xplatform/blob/fd4b06087b53112218fa12094d533512041b25d5/README.md
- https://github.com/MagnarHarestad/MagSID-Xplatform/blob/fd4b06087b53112218fa12094d533512041b25d5/src/MagSid.Assembler/SongImageBuilder.cs
- https://github.com/MagnarHarestad/MagSID-Xplatform/blob/fd4b06087b53112218fa12094d533512041b25d5/THIRD-PARTY-NOTICES.md
- https://github.com/MagnarHarestad/MagSID-Xplatform
- https://github.com/MagnarHarestad/MagSID-Xplatform/commit/99c2bf7a0da29c652a7d38d5a1fb0863fae81cf6

### Runtime profiles (no-evidence-found)

No verified minimum CPU/RAM/OS profile established beyond the qualified dependency and format notes; no runtime test was performed.
- https://github.com/MagnarHarestad/MagSID-Xplatform/blob/fd4b06087b53112218fa12094d533512041b25d5/README.md
- https://github.com/MagnarHarestad/MagSID-Xplatform/blob/fd4b06087b53112218fa12094d533512041b25d5/src/MagSid.Assembler/SongImageBuilder.cs
- https://github.com/MagnarHarestad/MagSID-Xplatform/blob/fd4b06087b53112218fa12094d533512041b25d5/THIRD-PARTY-NOTICES.md
- https://github.com/MagnarHarestad/MagSID-Xplatform

### AI (reviewed)

The SID import/export test commit explicitly credits Claude Opus 5.5. This establishes AI-assisted development for the tested pipeline change without quantifying the contribution or extending it to all project history.
- https://github.com/MagnarHarestad/MagSID-Xplatform/blob/fd4b06087b53112218fa12094d533512041b25d5/README.md
- https://github.com/MagnarHarestad/MagSID-Xplatform/blob/fd4b06087b53112218fa12094d533512041b25d5/src/MagSid.Assembler/SongImageBuilder.cs
- https://github.com/MagnarHarestad/MagSID-Xplatform/blob/fd4b06087b53112218fa12094d533512041b25d5/THIRD-PARTY-NOTICES.md
- https://github.com/MagnarHarestad/MagSID-Xplatform
- https://github.com/MagnarHarestad/MagSID-Xplatform/commit/99c2bf7a0da29c652a7d38d5a1fb0863fae81cf6

### Relationships (reviewed)

Preserves MagSID and GoatTracker-style player ancestry; C# reSID port only implements the single-cycle clock path, not all reSID resamplers.
- https://github.com/MagnarHarestad/MagSID-Xplatform/blob/fd4b06087b53112218fa12094d533512041b25d5/README.md
- https://github.com/MagnarHarestad/MagSID-Xplatform/blob/fd4b06087b53112218fa12094d533512041b25d5/src/MagSid.Assembler/SongImageBuilder.cs
- https://github.com/MagnarHarestad/MagSID-Xplatform/blob/fd4b06087b53112218fa12094d533512041b25d5/THIRD-PARTY-NOTICES.md
- https://github.com/MagnarHarestad/MagSID-Xplatform

## moria8-6502-multiplatform

Project ID: moria8-6502-multiplatform · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "moria8-6502-multiplatform",
  "last_checked": "2026-10-22",
  "status": "Released Apple II and Commodore ports plus buildable/testable Commander X16 target; current upstream fixes three gameplay regressions and wires Apple II MAME scenarios into the runtime target, without independent tracker execution"
}
```

Expected existing project SHA256: 0433efba7c1940908ed39f14ccfa527957cebf7bbf4d5d2f156f1ebc0170cefb

### Identity (reviewed)

Moria8 is a single multi-platform assembly reimplementation of Moria. Current main contains released C64, C128, Plus/4 and Apple II outputs plus a new buildable/testable Commander X16 target; the README's status table still calls X16 planned, so it is not represented as a published release.
- https://github.com/dcgibbons/moria8/blob/60286809eafbd9e804f750d92c07ec2261c0827e/README.md
- https://github.com/dcgibbons/moria8/commit/60286809eafbd9e804f750d92c07ec2261c0827e

### Classification (reviewed)

This remains a native, platform-specific assembly reimplementation derived from the credited VMS Moria and Umoria lineages, not a reverse-engineered binary port.
- https://github.com/dcgibbons/moria8/blob/60286809eafbd9e804f750d92c07ec2261c0827e/README.md

### Source CPU (no-evidence-found)

The documented source lineages are VMS Pascal and C Umoria; no original executable ISA is established by the reviewed material, so source_cpu remains empty.
- https://github.com/dcgibbons/moria8/blob/60286809eafbd9e804f750d92c07ec2261c0827e/README.md

### Target CPU (reviewed)

Existing Apple II and Commodore assembly supports the 6502 output. The Commander X16 makefile explicitly labels its new target 65C02/VERA, supporting the additional 65C02 output without inferring it from the platform name.
- https://github.com/dcgibbons/moria8/blob/60286809eafbd9e804f750d92c07ec2261c0827e/platforms/cx16/Makefile

### Build (reviewed)

The changed 6502 sources stop double monster attacks, make corner-adjacent attackers visible and interrupt auto-rest on damage or worsening hunger, with new C64 regression cases. Build hygiene changes route symbols and Python caches out of source trees, and make testapple2-runtime now runs the MAME scenario suite after the memory-contract gate. Limitations: The tracker reviewed the assembly, harness and Makefile changes but did not build any platform, run VICE/MAME/x16emu or reproduce the AI playtester findings.
- https://github.com/dcgibbons/moria8/commit/60286809eafbd9e804f750d92c07ec2261c0827e
- https://github.com/dcgibbons/moria8/blob/60286809eafbd9e804f750d92c07ec2261c0827e/platforms/cx16/Makefile
- https://github.com/dcgibbons/moria8/commit/dea5d1ae681c36ab858dd3ef7ddc22ef42f8ab80

### Runtime profiles (reviewed)

The existing Apple II 128 KiB/80-column/ProDOS profile remains sourced. The Commander X16 material states x16emu build/run/test requirements but no minimum physical X16 RAM or hardware revision, so no new minimum runtime profile is inferred.
- https://github.com/dcgibbons/moria8/blob/feed714990ae616dd075b66ff0238b60ee2da0ed/docs/release_notes/release_notes-v1.5.0.md
- https://github.com/dcgibbons/moria8/blob/60286809eafbd9e804f750d92c07ec2261c0827e/README.md

### AI (reviewed)

The commit explicitly identifies the three gameplay regressions as findings from the AI playtester. Existing Claude coauthor evidence remains the basis for project-level AI usage; the new statement adds a concrete testing role but does not quantify authorship.
- https://github.com/dcgibbons/moria8/blob/feed714990ae616dd075b66ff0238b60ee2da0ed/README.md
- https://github.com/dcgibbons/moria8/blob/feed714990ae616dd075b66ff0238b60ee2da0ed/docs/release_notes/release_notes-v1.5.0.md
- https://github.com/dcgibbons/moria8/blob/feed714990ae616dd075b66ff0238b60ee2da0ed/platforms/apple2/main.s
- https://github.com/dcgibbons/moria8/blob/feed714990ae616dd075b66ff0238b60ee2da0ed/platforms/apple2/boot.s
- https://github.com/dcgibbons/moria8/blob/feed714990ae616dd075b66ff0238b60ee2da0ed/core/game_loop.s
- https://github.com/dcgibbons/moria8/blob/feed714990ae616dd075b66ff0238b60ee2da0ed/docs/APPLE2_MEMORY_POLICY.md
- https://github.com/dcgibbons/moria8/blob/feed714990ae616dd075b66ff0238b60ee2da0ed/platforms/apple2/Makefile
- https://github.com/dcgibbons/moria8/blob/feed714990ae616dd075b66ff0238b60ee2da0ed/LICENSE
- https://github.com/dcgibbons/moria8/blob/feed714990ae616dd075b66ff0238b60ee2da0ed/data/LICENSE
- https://github.com/dcgibbons/moria8/blob/feed714990ae616dd075b66ff0238b60ee2da0ed/data/SOURCE-OFFER
- https://github.com/dcgibbons/moria8/blob/feed714990ae616dd075b66ff0238b60ee2da0ed/artwork/CREDITS.md
- https://github.com/dcgibbons/moria8/commit/fdfdcfba7e91f9c4b34a8a82ed3774da577aac48
- https://github.com/dcgibbons/moria8/commit/34aac8b6f1b4ecdabe9a88f39500f68a790c43a3
- https://github.com/dcgibbons/moria8/commit/4cf93a96986bcd23fc103650434fbbd9e21774e7
- https://github.com/dcgibbons/moria8/commits/feed714990ae616dd075b66ff0238b60ee2da0ed
- https://github.com/dcgibbons/moria8/commit/dea5d1ae681c36ab858dd3ef7ddc22ef42f8ab80

### Relationships (reviewed)

The shared Commodore and Apple II ports remain one Moria8 project, distinct from its explicitly credited VMS Moria/Umoria ancestors. README/root license specify GPLv3, with disk data/LICENSE and source-offer material; artwork has separate creator credits. Future platform rows and unrelated Moria titles are not additional discoveries. The normalized root, title/alias and lineage screen found no same-code project in the 1,833-project baseline or expanded 2,249-root prior-review union.
- https://github.com/dcgibbons/moria8/blob/feed714990ae616dd075b66ff0238b60ee2da0ed/README.md
- https://github.com/dcgibbons/moria8/blob/feed714990ae616dd075b66ff0238b60ee2da0ed/docs/release_notes/release_notes-v1.5.0.md
- https://github.com/dcgibbons/moria8/blob/feed714990ae616dd075b66ff0238b60ee2da0ed/LICENSE
- https://github.com/dcgibbons/moria8/blob/feed714990ae616dd075b66ff0238b60ee2da0ed/data/LICENSE
- https://github.com/dcgibbons/moria8/blob/feed714990ae616dd075b66ff0238b60ee2da0ed/data/SOURCE-OFFER
- https://github.com/dcgibbons/moria8/blob/feed714990ae616dd075b66ff0238b60ee2da0ed/artwork/CREDITS.md
- https://github.com/dcgibbons/moria8/blob/feed714990ae616dd075b66ff0238b60ee2da0ed/platforms/apple2/main.s
- https://github.com/dcgibbons/moria8/blob/feed714990ae616dd075b66ff0238b60ee2da0ed/platforms/apple2/boot.s
- https://github.com/dcgibbons/moria8/blob/feed714990ae616dd075b66ff0238b60ee2da0ed/core/game_loop.s
- https://github.com/dcgibbons/moria8/blob/feed714990ae616dd075b66ff0238b60ee2da0ed/docs/APPLE2_MEMORY_POLICY.md

## amazing-spiderman-rooms-editor

Project ID: amazing-spiderman-rooms-editor · Overall audit: partial

### Typed catalogue changes

```json
{
  "ai": {
    "evidence": [
      "README explicitly credits Spider-claude as an early Claude-assisted reverse-engineering experiment",
      "README update carries a Claude co-author trailer"
    ],
    "tools": [
      "Claude"
    ],
    "usage": true
  },
  "id": "amazing-spiderman-rooms-editor",
  "last_checked": "2026-10-22",
  "status": "Maintained editor; README now directs newer graphical, graphics/background and documentation work to the new-features branch and identifies Spider-claude as its earlier AI-assisted format-research predecessor"
}
```

Expected existing project SHA256: 450f4d4a08fb9cd0fc5eb020f152a15ec427c788363cb2c31a025eed4f1ed4e1

### Identity (reviewed)

C map/room parser and interactive editor for the 1990 game, including compressed room structures, tiles, objects, switches and file patching rather than just format notes.
- https://github.com/hughdavenport/spidey-editor/blob/696dd2e48219614b01c3c5ac2793ebabc123d863/README.md
- https://github.com/hughdavenport/spidey-editor/blob/696dd2e48219614b01c3c5ac2793ebabc123d863/room.c
- https://github.com/hughdavenport/spidey-editor/blob/696dd2e48219614b01c3c5ac2793ebabc123d863/editor.c
- https://github.com/hughdavenport/spidey-editor/blob/696dd2e48219614b01c3c5ac2793ebabc123d863/Makefile
- https://github.com/hughdavenport/spidey-editor/commit/696dd2e48219614b01c3c5ac2793ebabc123d863

### Classification (reviewed)

The reviewed implementation establishes the stated scope; no independent compilation, execution, gameplay or byte comparison was performed. MIT-licensed editor code does not license original game data.
- https://github.com/hughdavenport/spidey-editor/blob/696dd2e48219614b01c3c5ac2793ebabc123d863/README.md
- https://github.com/hughdavenport/spidey-editor/blob/696dd2e48219614b01c3c5ac2793ebabc123d863/room.c
- https://github.com/hughdavenport/spidey-editor/blob/696dd2e48219614b01c3c5ac2793ebabc123d863/editor.c
- https://github.com/hughdavenport/spidey-editor/blob/696dd2e48219614b01c3c5ac2793ebabc123d863/Makefile
- https://github.com/hughdavenport/spidey-editor/commit/696dd2e48219614b01c3c5ac2793ebabc123d863

### Source CPU (not-applicable)

No predecessor binary CPU is assigned: this is native work or format/language tooling. A platform name or gameplay inspiration is not treated as proof of recovered code lineage.
- https://github.com/hughdavenport/spidey-editor/blob/696dd2e48219614b01c3c5ac2793ebabc123d863/README.md
- https://github.com/hughdavenport/spidey-editor/blob/696dd2e48219614b01c3c5ac2793ebabc123d863/room.c
- https://github.com/hughdavenport/spidey-editor/blob/696dd2e48219614b01c3c5ac2793ebabc123d863/editor.c
- https://github.com/hughdavenport/spidey-editor/blob/696dd2e48219614b01c3c5ac2793ebabc123d863/Makefile
- https://github.com/hughdavenport/spidey-editor/commit/696dd2e48219614b01c3c5ac2793ebabc123d863

### Target CPU (no-evidence-found)

The inspected portable/high-level build material does not establish a fixed output CPU or minimum hardware requirement; the target CPU stays unknown.
- https://github.com/hughdavenport/spidey-editor/blob/696dd2e48219614b01c3c5ac2793ebabc123d863/README.md
- https://github.com/hughdavenport/spidey-editor/blob/696dd2e48219614b01c3c5ac2793ebabc123d863/room.c
- https://github.com/hughdavenport/spidey-editor/blob/696dd2e48219614b01c3c5ac2793ebabc123d863/editor.c
- https://github.com/hughdavenport/spidey-editor/blob/696dd2e48219614b01c3c5ac2793ebabc123d863/Makefile
- https://github.com/hughdavenport/spidey-editor/commit/696dd2e48219614b01c3c5ac2793ebabc123d863

### Build (reviewed)

The author now identifies the new-features branch as the location for the graphical editor, game graphics/background editing, documentation and newer work. Existing Linux build and DOS-data test claims remain author reports; Amiga/C64 data compatibility remains theoretical. Limitations: No branch was built or executed by the tracker, and the branch pointer does not establish cross-platform data compatibility or a minimum host configuration.
- https://github.com/hughdavenport/spidey-editor/blob/696dd2e48219614b01c3c5ac2793ebabc123d863/README.md
- https://github.com/hughdavenport/spidey-editor/blob/696dd2e48219614b01c3c5ac2793ebabc123d863/room.c
- https://github.com/hughdavenport/spidey-editor/blob/696dd2e48219614b01c3c5ac2793ebabc123d863/editor.c
- https://github.com/hughdavenport/spidey-editor/blob/696dd2e48219614b01c3c5ac2793ebabc123d863/Makefile
- https://github.com/hughdavenport/spidey-editor/commit/696dd2e48219614b01c3c5ac2793ebabc123d863
- https://github.com/hughdavenport/spidey-editor/commit/c62a683551abcd56c012c92cff2c66089e5d82af

### Runtime profiles (no-evidence-found)

No independently verified runtime profile was established for The Amazing Spider-Man — ROOMS.SPL editor. Upstream platform or test claims are recorded as claims rather than verified hardware requirements.
- https://github.com/hughdavenport/spidey-editor/blob/696dd2e48219614b01c3c5ac2793ebabc123d863/README.md
- https://github.com/hughdavenport/spidey-editor/blob/696dd2e48219614b01c3c5ac2793ebabc123d863/room.c
- https://github.com/hughdavenport/spidey-editor/blob/696dd2e48219614b01c3c5ac2793ebabc123d863/editor.c
- https://github.com/hughdavenport/spidey-editor/blob/696dd2e48219614b01c3c5ac2793ebabc123d863/Makefile
- https://github.com/hughdavenport/spidey-editor/commit/696dd2e48219614b01c3c5ac2793ebabc123d863

### AI (reviewed)

The README explicitly says Spider-claude was an early experiment using Claude to reverse engineer the game's file formats, and the README change is itself coauthored by Claude. This replaces the previous no-evidence-found state with direct author disclosure.
- https://github.com/hughdavenport/spidey-editor/blob/696dd2e48219614b01c3c5ac2793ebabc123d863/README.md
- https://github.com/hughdavenport/spidey-editor/blob/696dd2e48219614b01c3c5ac2793ebabc123d863/room.c
- https://github.com/hughdavenport/spidey-editor/blob/696dd2e48219614b01c3c5ac2793ebabc123d863/editor.c
- https://github.com/hughdavenport/spidey-editor/blob/696dd2e48219614b01c3c5ac2793ebabc123d863/Makefile
- https://github.com/hughdavenport/spidey-editor/commit/696dd2e48219614b01c3c5ac2793ebabc123d863
- https://github.com/hughdavenport/spidey-editor/commit/c62a683551abcd56c012c92cff2c66089e5d82af
- https://github.com/hughdavenport/Spider-claude/blob/75fbe2df49aa77bace7e272f69bc0e4af1a725c2/README.md

### Relationships (reviewed)

The maintained editor explicitly identifies Spider-claude as the earlier format-research experiment and says spidey-editor is the current implementation of every format worked out there. They are distinct repositories and records with a predecessor/successor relationship, not duplicate live implementations.
- https://github.com/hughdavenport/spidey-editor/blob/696dd2e48219614b01c3c5ac2793ebabc123d863/README.md
- https://github.com/hughdavenport/spidey-editor/blob/696dd2e48219614b01c3c5ac2793ebabc123d863/room.c
- https://github.com/hughdavenport/spidey-editor/blob/696dd2e48219614b01c3c5ac2793ebabc123d863/editor.c
- https://github.com/hughdavenport/spidey-editor/blob/696dd2e48219614b01c3c5ac2793ebabc123d863/Makefile
- https://github.com/hughdavenport/spidey-editor/commit/696dd2e48219614b01c3c5ac2793ebabc123d863
- https://github.com/hughdavenport/spidey-editor/commit/c62a683551abcd56c012c92cff2c66089e5d82af
- https://github.com/hughdavenport/Spider-claude/blob/75fbe2df49aa77bace7e272f69bc0e4af1a725c2/README.md

## Sources

```json
[
  {
    "first_indexed": "2026-10-22",
    "id": "github-hughdavenport-spider-claude",
    "kind": "github-repository",
    "last_reviewed": "2026-10-22",
    "open_task_ids": [],
    "projects_promoted": [
      "spider-claude-amazing-spiderman-research"
    ],
    "reason": "Archived Claude-assisted Amazing Spider-Man DOS asset research and decoder repository explicitly linked as the predecessor to spidey-editor.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/hughdavenport/Spider-claude"
  }
]
```

## Source updates

```json
[
  {
    "id": "wide-20261018b-wing-commander-kilrathi-saga-reconstruction",
    "last_reviewed": "2026-10-22"
  },
  {
    "id": "pass33-symphony-of-night-decompilation",
    "last_reviewed": "2026-10-22"
  },
  {
    "id": "github-yeager-firestaff",
    "last_reviewed": "2026-10-22"
  },
  {
    "id": "github-cbongo-ghidra-retro-machines",
    "last_reviewed": "2026-10-22"
  },
  {
    "id": "wide-20261018j-cpc-speaking-vector-head-z80",
    "last_reviewed": "2026-10-22"
  },
  {
    "id": "github-fadden-ciderpress2",
    "last_reviewed": "2026-10-22"
  },
  {
    "id": "github-magnarharestad-magsid-xplatform",
    "last_reviewed": "2026-10-22"
  },
  {
    "id": "github-dcgibbons-moria8",
    "last_reviewed": "2026-10-22"
  },
  {
    "id": "wide-20261019u-amazing-spiderman-rooms-editor",
    "last_reviewed": "2026-10-22"
  }
]
```

## Source ids

```json
[
  "wide-20261018b-wing-commander-kilrathi-saga-reconstruction",
  "pass33-symphony-of-night-decompilation",
  "github-yeager-firestaff",
  "github-cbongo-ghidra-retro-machines",
  "wide-20261018j-cpc-speaking-vector-head-z80",
  "github-fadden-ciderpress2",
  "github-magnarharestad-magsid-xplatform",
  "github-dcgibbons-moria8",
  "wide-20261019u-amazing-spiderman-rooms-editor",
  "github-hughdavenport-spider-claude"
]
```

## Research event notes

The CPU audit queue returned zero unresolved source/target CPU areas. The new Spider-claude record therefore makes explicit no-evidence-found and not-applicable CPU decisions from primary documentation; no architecture or minimum hardware was inferred. The tracker did not compile or execute candidate projects.
