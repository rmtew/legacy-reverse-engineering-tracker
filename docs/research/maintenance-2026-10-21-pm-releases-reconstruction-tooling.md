# Review nine material upstream changes spanning published releases, reconstruction evidence, emulator fidelity and retro-development tooling.

Review nine material upstream changes spanning published releases, reconstruction evidence, emulator fidelity and retro-development tooling.

Date: 2026-10-21 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- pool-of-radiance-dos-c-reconstruction / Target CPU (no-evidence-found): No fixed output CPU established; modern host CPU is not inferred.
- pool-of-radiance-dos-c-reconstruction / Build (reviewed): No strict/identity/manifest/member-table credit is claimed upstream, and neither whole-game completeness nor playability is established.
- pool-of-radiance-dos-c-reconstruction / Runtime profiles (no-evidence-found): No independently verified runtime profile. Explicit limitations retained in identity.
- firestaff-dungeon-master-engine / Relationships (needs-research): The current status material establishes original-media and cross-edition provenance, but the wider predecessor/successor/fork graph remains unreviewed. Next check: Check predecessor/successor/fork and credited-source relationships. Next check: Check predecessor/successor/fork and credited-source relationships.
- retroio-filesystem-libraries / Source CPU (no-evidence-found): No fixed source CPU assigned for this host-side tooling.
- retroio-filesystem-libraries / Target CPU (no-evidence-found): No fixed target CPU inferred from modern host or asset format.
- retroio-filesystem-libraries / Runtime profiles (no-evidence-found): No independently verified minimum hardware profile established.
- github-henols-c64-re-tools / Target CPU (no-evidence-found): TypeScript runs under Node.js/tsx on the host. No host CPU architecture was established; VICE, ACME and Ghidra are separate dependencies, not a reason to infer a modern CPU target.
- github-henols-c64-re-tools / Runtime profiles (no-evidence-found): v2.1.1 publishes a devcontainer feature and states Node.js/VICE software prerequisites, but no host CPU family, RAM floor or minimum machine. No runtime profile is inferred.
- amy-studio-colecovision-development-environment / Runtime profiles (no-evidence-found): Current README and reviewed ADAM commits state no minimum ColecoVision/ADAM RAM profile or host CPU/RAM floor.
- virtualjaguar-libretro / Build (reviewed): Stable runtime profiles remain pinned to v3.9.1; release-candidate artifacts do not replace them.
- applem-apple-ii-emulator-debugger / Runtime profiles (no-evidence-found): Historical machine RAM configurations are emulated profiles, not host minimum requirements.
- pist-atari-st-ide / AI (no-evidence-found): The reviewed v0.10.4 release notes provide no explicit development-AI attribution; configuration files are not treated as proof of contribution.
- pist-atari-st-ide / Relationships (needs-research): The bundled Hatari fork and upstream Hatari/vasm/vlink relationships are identified but the fork's independent catalogue scope has not been fully reconciled. Next check: Check the bundled Hatari fork and credited toolchain relationships against existing catalogue records.
- moria8-6502-multiplatform / Source CPU (no-evidence-found): The documented source lineages are VMS Pascal and C Umoria; no original executable ISA is established by the reviewed material, so source_cpu remains empty.

## pool-of-radiance-dos-c-reconstruction

Project ID: pool-of-radiance-dos-c-reconstruction · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "pool-of-radiance-dos-c-reconstruction",
  "last_checked": "2026-10-21",
  "status": "incremental DOS C reconstruction; the latest driver-internal timer-hook translation has a 318-case original-byte differential with zero mismatches plus bounded native frame-mechanics corroboration, while whole-game denominators and full gameplay remain unknown",
  "techniques": [
    "original-byte differential testing",
    "fail-closed environment modeling",
    "DOSBox-X native frame-mechanics corroboration"
  ]
}
```

Expected existing project SHA256: c54c15c8fb2e21d0eb572d31ebb1de2e4ab65e2a7e91361578ad444bad052b78

### Identity (reviewed)

Early portable C engine reconstruction; actual ECL/data-format parsers and recovered modules are present. Claude/Codex workflow disclosed. Full gameplay and later platform ports are goals, not verified achievements.
- https://github.com/huntergdavis/poolrad-decomp
- https://github.com/huntergdavis/poolrad-decomp/blob/08c46cb32836220b153a9465b568a016d75edbac/README.md

### Classification (reviewed)

Scoped as game; source-reconstruction. Repository layout and selected source inspected.
- https://github.com/huntergdavis/poolrad-decomp
- https://github.com/huntergdavis/poolrad-decomp/blob/08c46cb32836220b153a9465b568a016d75edbac/README.md

### Source CPU (reviewed)

Source architecture: x86
- https://github.com/huntergdavis/poolrad-decomp
- https://github.com/huntergdavis/poolrad-decomp/blob/08c46cb32836220b153a9465b568a016d75edbac/README.md

### Target CPU (no-evidence-found)

No fixed output CPU established; modern host CPU is not inferred.
- https://github.com/huntergdavis/poolrad-decomp
- https://github.com/huntergdavis/poolrad-decomp/blob/08c46cb32836220b153a9465b568a016d75edbac/README.md

### Build (reviewed)

Current main translates the 53-byte RES_08AE +137C timer-hook installer and reports 318 original-byte Unicorn differential cases with zero mismatches, full 1 MiB RAM comparison and a declared fail-closed DOS-vector/port environment. Thirty-two DOSBox-X native calls corroborate only frame mechanics through a shadow vector table; they do not verify real DOS, PIT behavior, the installed handler, natural reachability or full gameplay. The tracker did not run the harness. Limitations: No strict/identity/manifest/member-table credit is claimed upstream, and neither whole-game completeness nor playability is established.
- https://github.com/huntergdavis/poolrad-decomp/commit/9f1d6b1e0520d2a36759179cb856f5e67c0218ed

### Runtime profiles (no-evidence-found)

No independently verified runtime profile. Explicit limitations retained in identity.
- https://github.com/huntergdavis/poolrad-decomp
- https://github.com/huntergdavis/poolrad-decomp/blob/08c46cb32836220b153a9465b568a016d75edbac/README.md

### AI (reviewed)

README explicitly describes Claude and Codex work lanes.
- https://github.com/huntergdavis/poolrad-decomp
- https://github.com/huntergdavis/poolrad-decomp/blob/08c46cb32836220b153a9465b568a016d75edbac/README.md

### Relationships (reviewed)

Current catalogue URL and related-title screening performed. No unmodified fork promoted as a separate project.
- https://github.com/huntergdavis/poolrad-decomp
- https://github.com/huntergdavis/poolrad-decomp/blob/08c46cb32836220b153a9465b568a016d75edbac/README.md

## firestaff-dungeon-master-engine

Project ID: firestaff-dungeon-master-engine · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "firestaff-dungeon-master-engine",
  "last_checked": "2026-10-21",
  "status": "v3.0.401 published with expanded authentic-media startup matrices and a bounded DM2 DOS EN weather-zone/RNG gate; native presentation, input, audio and full gameplay parity remain open",
  "techniques": [
    "clean-room reimplementation",
    "original-media hashing",
    "binary analysis",
    "format decoding",
    "cross-version comparison",
    "real-media verification",
    "source-locked runtime verification",
    "instrumented Mednafen capture",
    "Backup RAM format analysis",
    "CD track provenance verification",
    "source-frame byte comparison",
    "native save-format analysis",
    "bounded in-memory media decoding",
    "cross-platform startup matrix testing",
    "source-clock timing calibration",
    "authenticated viewport-region gates",
    "deterministic RNG bootstrap verification",
    "source-locked fixed-point sampling",
    "authenticated packed-selector decoding",
    "source-timed VBlank cadence",
    "Apple IIGS resource decoding",
    "65C816 hidden-code analysis",
    "DOC sound reconstruction",
    "authenticated mouse-route regression",
    "input-to-present latency tracing",
    "authenticated Apple IIGS startup-route verification",
    "original-media immutability hashing",
    "source-timed selector animation/audio separation",
    "overlapped authenticated-media scanning",
    "authenticated cross-game startup matrix",
    "bounded original-media weather/RNG verification"
  ]
}
```

Expected existing project SHA256: 91a62d7c99bcae4b296ba1120930b6bb92b70543cc18dbfe6c44999f3f02aa58

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

Firestaff v3.0.401 is published. Its release notes expand original-media startup matrices across DM1, CSB and DM2 and add a DOS EN gate for weather zone 2 plus a separate cold-weather/RNG receipt. Upstream explicitly says the SDL-dummy checks do not establish native display, physical input, audible playback or full gameplay parity; equivalent weather checks for other editions remain open. The tracker did not execute the release.
- https://github.com/yeager/firestaff/releases/tag/v3.0.401
- https://github.com/yeager/firestaff/commit/0e1619635a0ba499f60abf3fdca0409dc1182cd6

### Runtime profiles (reviewed)

The existing Apple Silicon profile now records v3.0.397 scan timings on the same Mac mini M4. They are not CPU/RAM minima or evidence for other hosts.
- https://github.com/yeager/firestaff/releases/tag/v3.0.397

### AI (reviewed)

Existing explicit Claude project-agent evidence remains valid; no weaker inference was substituted.
- https://github.com/yeager/firestaff

### Relationships (needs-research)

The current status material establishes original-media and cross-edition provenance, but the wider predecessor/successor/fork graph remains unreviewed. Next check: Check predecessor/successor/fork and credited-source relationships. Next check: Check predecessor/successor/fork and credited-source relationships.
- https://github.com/yeager/firestaff

## retroio-filesystem-libraries

Project ID: retroio-filesystem-libraries · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "retroio-filesystem-libraries",
  "last_checked": "2026-10-21",
  "status": "active; Econet attributes now use recoverable .xat sidecars, DragonDOS recognition has real-image accept/reject gates, and NDFS/TNFS/XMSG protocol contracts remain mutation-backed",
  "techniques": [
    "SINTRAN M allocation modeling",
    "mutation-tested protocol boundary contracts",
    "Acorn attribute sidecar recovery",
    "real-image filesystem acceptance and rejection testing"
  ]
}
```

Expected existing project SHA256: 047ffa66c89d51e19963338f3d80de3efb942069231fe1de8e1417e07417cf91

### Identity (reviewed)

Identity: Reusable storage/network packages with actual Commodore image factory and filesystem implementations. Explicit Claude-assisted code disclosure; broad package list is not uniform independently verified format coverage. Classification: Inspected source supports development tooling. Reusable storage/network packages with actual Commodore image factory and filesystem implementations. Explicit Claude-assisted code disclosure; broad package list is not uniform independently verified format coverage. Source CPU: No fixed source CPU assigned for this host-side tooling. Target CPU: No fixed target CPU inferred from modern host or asset format. Build: No candidate code compiled or executed. Rebuild hashes, runtime fidelity and completeness remain upstream claims; matching with original binary/assembly fallback is not full source recovery. Runtime profiles: No independently verified minimum hardware profile established. AI: Explicit README disclosure establishes AI use; no additional tool/model inferred beyond the recorded disclosure. Relationships: Screened URL, title and prior decisions. GitHub fork flag is not treated as conclusive lineage evidence. Evidence: https://github.com/RetroCoreLabs/RetroIO https://github.com/RetroCoreLabs/RetroIO/blob/e6231b40c15d1de8c43ee924378802e695902955/src/RetroIO.Storage.Local/src/CbmImageFactory.cs https://github.com/RetroCoreLabs/RetroIO/blob/e6231b40c15d1de8c43ee924378802e695902955/README.md
- https://github.com/RetroCoreLabs/RetroIO
- https://github.com/RetroCoreLabs/RetroIO/blob/e6231b40c15d1de8c43ee924378802e695902955/src/RetroIO.Storage.Local/src/CbmImageFactory.cs
- https://github.com/RetroCoreLabs/RetroIO/blob/e6231b40c15d1de8c43ee924378802e695902955/README.md

### Classification (reviewed)

Inspected source supports development tooling. Reusable storage/network packages with actual Commodore image factory and filesystem implementations. Explicit Claude-assisted code disclosure; broad package list is not uniform independently verified format coverage.
- https://github.com/RetroCoreLabs/RetroIO
- https://github.com/RetroCoreLabs/RetroIO/blob/e6231b40c15d1de8c43ee924378802e695902955/src/RetroIO.Storage.Local/src/CbmImageFactory.cs
- https://github.com/RetroCoreLabs/RetroIO/blob/e6231b40c15d1de8c43ee924378802e695902955/README.md

### Source CPU (no-evidence-found)

No fixed source CPU assigned for this host-side tooling.
- https://github.com/RetroCoreLabs/RetroIO
- https://github.com/RetroCoreLabs/RetroIO/blob/e6231b40c15d1de8c43ee924378802e695902955/src/RetroIO.Storage.Local/src/CbmImageFactory.cs
- https://github.com/RetroCoreLabs/RetroIO/blob/e6231b40c15d1de8c43ee924378802e695902955/README.md

### Target CPU (no-evidence-found)

No fixed target CPU inferred from modern host or asset format.
- https://github.com/RetroCoreLabs/RetroIO
- https://github.com/RetroCoreLabs/RetroIO/blob/e6231b40c15d1de8c43ee924378802e695902955/src/RetroIO.Storage.Local/src/CbmImageFactory.cs
- https://github.com/RetroCoreLabs/RetroIO/blob/e6231b40c15d1de8c43ee924378802e695902955/README.md

### Build (reviewed)

Current main removes legacy Econet ',inf' attribute handling, derives length from the file, moves damaged or empty .xat sidecars to .xat.bad before rebuilding metadata, and adds real-image DragonDOS acceptance/rejection tests. These are upstream tests and implementation claims; no tracker-side build, disk mount or protocol execution was performed.
- https://github.com/RetroCoreLabs/RetroIO/commit/753adabd534c75f6fb726cdecd30f2eb1d0e0df9
- https://github.com/RetroCoreLabs/RetroIO/commit/369d262f71f09add33c96e7621d02d10da7faee9

### Runtime profiles (no-evidence-found)

No independently verified minimum hardware profile established.
- https://github.com/RetroCoreLabs/RetroIO
- https://github.com/RetroCoreLabs/RetroIO/blob/e6231b40c15d1de8c43ee924378802e695902955/src/RetroIO.Storage.Local/src/CbmImageFactory.cs
- https://github.com/RetroCoreLabs/RetroIO/blob/e6231b40c15d1de8c43ee924378802e695902955/README.md

### AI (reviewed)

Explicit README disclosure establishes AI use; no additional tool/model inferred beyond the recorded disclosure.
- https://github.com/RetroCoreLabs/RetroIO
- https://github.com/RetroCoreLabs/RetroIO/blob/e6231b40c15d1de8c43ee924378802e695902955/src/RetroIO.Storage.Local/src/CbmImageFactory.cs
- https://github.com/RetroCoreLabs/RetroIO/blob/e6231b40c15d1de8c43ee924378802e695902955/README.md

### Relationships (reviewed)

Screened URL, title and prior decisions. GitHub fork flag is not treated as conclusive lineage evidence.
- https://github.com/RetroCoreLabs/RetroIO
- https://github.com/RetroCoreLabs/RetroIO/blob/e6231b40c15d1de8c43ee924378802e695902955/src/RetroIO.Storage.Local/src/CbmImageFactory.cs
- https://github.com/RetroCoreLabs/RetroIO/blob/e6231b40c15d1de8c43ee924378802e695902955/README.md

## github-henols-c64-re-tools

Project ID: github-henols-c64-re-tools · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "github-henols-c64-re-tools",
  "last_checked": "2026-10-21",
  "status": "active; recording coverage origins, bounded large-trace transport, protocol-version handshakes, false-code reference suppression and unreferenced disk-sector extraction now strengthen agent-facing reconstruction evidence",
  "techniques": [
    "binary-analysis",
    "data-format-analysis",
    "MCP",
    "field tracing",
    "byte-identical source generation",
    "scripted rebuild validation",
    "runtime provenance comparison",
    "one-release provenance separation",
    "platform-symbol export",
    "CIA entry-state capture and restoration",
    "bounded host request logging",
    "source-map generation",
    "linked reference documentation",
    "non-stopping execution tracing",
    "parallel-agent evidence ownership",
    "media signature validation",
    "JAM and snapshot failure hardening",
    "multi-release provenance grouping",
    "in-program crack-trace analysis",
    "coverage-origin recording",
    "bounded attachment transport",
    "versioned host handshake",
    "data-region false-code suppression",
    "unreferenced-sector extraction"
  ]
}
```

Expected existing project SHA256: 7ef55921948c85917cd060f1a82fe1d74def229177e49d95ef8422cbb2cecc3c

### Identity (reviewed)

General-purpose TypeScript C64 reverse-engineering toolkit controlling stock VICE and integrating disk/BASIC/static-analysis/assembly/equivalence workflows. package.json now declares 2.0.0 and publishable CLI/MCP/host bins, while the primary roadmap explicitly leaves npm trusted-publisher setup, the v2.0.0 tag and verification of the published package open. C64RT_TRACE adds per-process JSONL field traces for host requests, VICE lifecycle, MCP calls, native tool runs and stderr without exposing the trace to the agent. Node.js 24+, VICE 3.9+ and user-supplied ROMs remain prerequisites; no host CPU/RAM minimum or independent execution is established. Evidence: https://github.com/henols/c64-re-tools/blob/main/README.md https://github.com/henols/c64-re-tools/blob/main/package.json https://github.com/henols/c64-re-tools/commit/11987768d056 https://github.com/henols/c64-re-tools/commit/5ceac29bb61b Current M14 work now generates byte-identical ACME source from an unpacked image or PRG, curated knowledge and Ghidra instructions; an optional loader is run in VICE and checked at the recovered entry state. The documented ten-stage workflow adds explicit acceptance criteria, exit checks, deliverables and coverage reporting. Release comparison can attach first-access/runtime-change evidence to differing bytes, single-release separation reports unpack/access/reachability provenance, and platform symbols can be exported as an ACME include. These are upstream live-tool checks rather than an independent tracker run, and they do not close the separate npm publication gate. Evidence: https://github.com/henols/c64-re-tools/commit/8e2bbb5a106c2fe339bc2f1aaaa8d02b414a1341 https://github.com/henols/c64-re-tools/commit/18bc1327744db353667cabf39d81ed373effe078 https://github.com/henols/c64-re-tools/commit/b80796c63719f7eeb4fd694afd689fe5a926cd8b https://github.com/henols/c64-re-tools/commit/1c0070e068b719314a4ee47b56de189916b0a6d6 https://github.com/henols/c64-re-tools/commit/ad164faf2354087ee3c0f7bd8d9e52c36a367fbc M17 now captures CIA timer latches and interrupt masks that ordinary register reads cannot recover, programs generated loaders to restore the reachable timer state, and compares counters, latches, controls and masks at the entry jump. An upstream live test distinguishes the repaired loader from one without CIA restoration. The host also records each skill-script operation and outcome while keeping verbose MCP/VICE tracing opt-in. These are upstream tests; no local VICE run was performed, SID voice 3, TOD phase and interrupt flags remain documented limits, and the npm publication gate remains open. Evidence: https://github.com/henols/c64-re-tools/commit/5cdc74d5226db7d8123ca782cfb6e9a36a11ee8b https://github.com/henols/c64-re-tools/commit/15a3bb8f331d0fe8d81976400c04a4e632813b06 M23/M24 now let execution traces continue while recording observations/history, generate linked source maps and program reference pages, and route evidence-producing agent run files into owned run directories. The Bruce Lee acceptance reports 70 reference pages, 1,227 entries, 21 decoded tables and deterministic second-pass linking; these are upstream field-run receipts and do not close the separate npm publication gate. Evidence: https://github.com/henols/c64-re-tools/commit/4c209ab6e79cbb0a34e3b818bf33d8b6fb92f0ba https://github.com/henols/c64-re-tools/commit/7a45b671dc7b6efc1f0c6b905e57ae1839a8ce3a https://github.com/henols/c64-re-tools/commit/9caaff4bf206b429d389fcdf5e94d42919600cd9 v2.1.1 closes the previously open publication gate and reports a real-project field pass covering every script command and MCP tool on VICE 3.10. It hardens JAM state, snapshot failures, drive-side stops, static/provenance analysis and preflight validation; current main additionally rejects malformed media before VICE can reinterpret it, stops an in-flight autostart before snapshot restore and exposes the documented $A000-$BFFF VICE memory-map flaw. These are upstream field and regression receipts, not a tracker-side VICE run. Evidence: https://github.com/henols/c64-re-tools/releases/tag/v2.1.1 https://github.com/henols/c64-re-tools/commit/eb69c523cc34f88e9c2aa5e23f3139306ed6bb5b
- https://github.com/henols/c64-re-tools/blob/main/README.md
- https://github.com/henols/c64-re-tools/blob/main/package.json
- https://github.com/henols/c64-re-tools/blob/main/src/c64.ts
- https://github.com/henols/c64-re-tools/blob/main/src/mcp/server.ts
- https://github.com/henols/c64-re-tools/commit/46993b6ff6617fab2ca93e300c8d37e80da02bc9

### Classification (reviewed)

M17 extends the general-purpose C64 reconstruction toolkit with CIA entry-state restoration and bounded host-operation logging; it remains tooling rather than a title-specific reconstruction.
- https://github.com/henols/c64-re-tools/commit/5cdc74d5226db7d8123ca782cfb6e9a36a11ee8b
- https://github.com/henols/c64-re-tools/commit/15a3bb8f331d0fe8d81976400c04a4e632813b06

### Source CPU (reviewed)

README explicitly supplies a Ghidra NMOS 6510 language with all 256 opcodes and C64 BASIC/disk analysis. The 6510 is the analyzed guest CPU.
- https://github.com/henols/c64-re-tools/blob/main/README.md
- https://github.com/henols/c64-re-tools/blob/main/package.json
- https://github.com/henols/c64-re-tools/blob/main/src/c64.ts
- https://github.com/henols/c64-re-tools/blob/main/src/mcp/server.ts

### Target CPU (no-evidence-found)

TypeScript runs under Node.js/tsx on the host. No host CPU architecture was established; VICE, ACME and Ghidra are separate dependencies, not a reason to infer a modern CPU target.
- https://github.com/henols/c64-re-tools/blob/main/README.md
- https://github.com/henols/c64-re-tools/blob/main/package.json
- https://github.com/henols/c64-re-tools/blob/main/src/c64.ts
- https://github.com/henols/c64-re-tools/blob/main/src/mcp/server.ts

### Build (reviewed)

Current main lets recordings state where coverage begins, transports very large trace hits as bounded attachments, rejects client/host version mismatches, suppresses analyzer references originating in classified data, and can extract used-but-unreferenced disk sectors. Upstream tests are present for these contracts; the tracker did not run VICE, the MCP host or reconstruction workflows.
- https://github.com/henols/c64-re-tools/commit/e475418a03b5cb9c6c071103918d6459b956f425
- https://github.com/henols/c64-re-tools/commit/a585eb84eadf92a5ed75521f686620e9460f775b
- https://github.com/henols/c64-re-tools/commit/c9a5f6376536465a3644c1c5d59d0ca03c40ba03
- https://github.com/henols/c64-re-tools/commit/fffae9ef0b

### Runtime profiles (no-evidence-found)

v2.1.1 publishes a devcontainer feature and states Node.js/VICE software prerequisites, but no host CPU family, RAM floor or minimum machine. No runtime profile is inferred.
- https://github.com/henols/c64-re-tools/releases/tag/v2.1.1
- https://github.com/henols/c64-re-tools/blob/main/README.md

### AI (reviewed)

The new field-test plan explicitly documents a Claude session exercising the toolkit from its packed artifact. This establishes AI use in the project workflow but is not represented as source-code authorship or a co-author claim.
- https://github.com/henols/c64-re-tools/commit/5ceac29bb61b
- https://github.com/henols/c64-re-tools/blob/main/README.md

### Relationships (reviewed)

Toolkit project with its own implementation; VICE/Ghidra/ACME are external dependencies. GitHub reports fork=false; that metadata alone does not establish independent authorship. Canonical root was screened against the approved 1,320-project catalogue plus discovery-source/decision indexes; no root collision was found. Rights: MIT for toolkit; separately supplied VICE/ROMs and external tools retain their rights.
- https://github.com/henols/c64-re-tools/blob/main/README.md
- https://github.com/henols/c64-re-tools/blob/main/package.json
- https://github.com/henols/c64-re-tools/blob/main/src/c64.ts
- https://github.com/henols/c64-re-tools/blob/main/src/mcp/server.ts
- https://github.com/henols/c64-re-tools

## amy-studio-colecovision-development-environment

Project ID: amy-studio-colecovision-development-environment · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "amy-studio-colecovision-development-environment",
  "last_checked": "2026-10-21",
  "status": "active; Goblin, Speed Ski, Paratrooper and Things in the Dark source ports have deterministic upstream compile/runtime gates",
  "techniques": [
    "Amy-to-Z80 compilation",
    "in-browser assembly",
    "ROM generation",
    "source breakpoints",
    "instruction stepping",
    "CPU/VDP/RAM/VRAM inspection",
    "cycle profiling",
    "gasm80-compatible Z80 assembly",
    "ADAM EOS project support",
    "ADAM serial/debug input",
    "screen-mode dataflow analysis",
    "deterministic source-port runtime validation"
  ]
}
```

Expected existing project SHA256: 571662f5aec229f45c02f6b7034ce858474591ae77f30c77f51afcfdecff9edd

### Identity (reviewed)

Amy Studio remains an original browser-based ColecoVision/ADAM development environment, not a reverse-engineered game project. Current main adds substantial source ports as examples and validation fixtures.
- https://github.com/amypurple/AmyStudio
- https://github.com/amypurple/AmyStudio/commit/e757e40ee2101544ccbb0236ea5c246e18a63144

### Classification (reviewed)

Current primary commits extend the original browser toolchain from ColecoVision into native Coleco ADAM development/debug support without changing its original-tooling classification.
- https://github.com/amypurple/AmyStudio

### Source CPU (not-applicable)

Original development tooling has no analyzed source binary CPU.
- https://github.com/amypurple/AmyStudio

### Target CPU (reviewed)

README and current assembler commit explicitly target Z80 code; ADAM support does not introduce a separately inferred CPU family.
- https://github.com/amypurple/AmyStudio

### Build (reviewed)

Upstream adds Goblin, Speed Ski, Paratrooper and Things in the Dark ports with deterministic compiler and Gearcoleco test-core gates. The Goblin/Speed Ski harness compiles balanced ROMs, uses a fixed seed and scripted inputs, then checks game-specific screen, tile and sprite outcomes. This is upstream validation only; the tracker did not compile or run the examples on an emulator or physical ColecoVision.
- https://github.com/amypurple/AmyStudio/commit/e757e40ee2101544ccbb0236ea5c246e18a63144
- https://github.com/amypurple/AmyStudio/commit/e974dfa79761159a2e7af5b0e2534a2b3d3fee37
- https://github.com/amypurple/AmyStudio/commit/a39c66c20342154d51b9be74e73cbdda5bfb053a

### Runtime profiles (no-evidence-found)

Current README and reviewed ADAM commits state no minimum ColecoVision/ADAM RAM profile or host CPU/RAM floor.
- https://github.com/amypurple/AmyStudio

### AI (reviewed)

Primary README explicitly credits Claude and OpenAI Codex while preserving human ownership and testing responsibility.
- https://github.com/amypurple/AmyStudio

### Relationships (reviewed)

Primary README identifies the bundled self-hosted GearColeco WebAssembly test core and older ColecoVision toolchain heritage.
- https://github.com/amypurple/AmyStudio

## virtualjaguar-libretro

Project ID: virtualjaguar-libretro · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "virtualjaguar-libretro",
  "last_checked": "2026-10-21",
  "status": "v3.10.0 release candidate compiled across 24 targets but is explicitly untested and without manual QA; current work adds DSTA2 computed-Z lane fidelity, revision-guarded community cheats and stricter Neuro profile validation",
  "techniques": [
    "hardware emulation",
    "headless regression corpus",
    "savestate compatibility",
    "SIMD acceleration",
    "per-title compatibility presets",
    "netlist-derived hardware validation",
    "GDB remote debugging",
    "executable and cartridge loader analysis",
    "revision-guarded community cheat conversion",
    "release-candidate cross-compilation matrix"
  ]
}
```

Expected existing project SHA256: 55b2c1994ca537e1843d9888b07de1aea57042baf2427d4de0a33fabb7538603

### Identity (reviewed)

README identifies the maintained Jaguar/Jaguar CD libretro core and v3.8.0 release; display title and subject are normalized to the continuing Virtual Jaguar identity.
- https://github.com/libretro/virtualjaguar-libretro/blob/master/README.md
- https://github.com/libretro/virtualjaguar-libretro/releases/tag/v3.8.0

### Classification (reviewed)

Core emulates Jaguar 68000, GPU, DSP, Object Processor, CD, link, Memory Track and GameDrive behavior; it is platform tooling, not a game reconstruction.
- https://github.com/libretro/virtualjaguar-libretro/blob/master/README.md

### Source CPU (reviewed)

README explicitly names the emulated 68000 alongside Jaguar custom processors; the existing source_cpu=m68000 is retained without inventing canonical labels for the custom GPU/DSP.
- https://github.com/libretro/virtualjaguar-libretro/blob/master/README.md

### Target CPU (reviewed)

README/release matrix explicitly names Linux x86_64/aarch64/i686, macOS Apple Silicon/Intel, Windows x64/x86, Android arm64/armeabi-v7a/x86_64/x86, iOS/tvOS arm64 and WebAssembly. These establish x86, x86-64, ARM, arm64 and WebAssembly outputs without inferring console ISAs from platform names.
- https://github.com/libretro/virtualjaguar-libretro/blob/master/README.md
- https://github.com/libretro/virtualjaguar-libretro/blob/master/.github/workflows/c-cpp.yml

### Build (reviewed)

The rolling v3.10.0 release candidate reports successful compilation on 24 targets and adds a DSTA2 computed-Z destination-lane correction, revision-guarded community cheat conversion and stricter Neuro profile checks. Its own release page explicitly says the candidate has not passed the test suite or manual QA, so it is not recorded as a stable v3.10.0 release or playability proof. Limitations: Stable runtime profiles remain pinned to v3.9.1; release-candidate artifacts do not replace them.
- https://github.com/libretro/virtualjaguar-libretro/releases/tag/prerelease
- https://github.com/libretro/virtualjaguar-libretro/commit/338e2b65

### Runtime profiles (reviewed)

Updated the explicit desktop architecture profiles to v3.9.1 and added the published Windows ARM64 package. The release does not state a minimum CPU generation or RAM, so none is inferred.
- https://github.com/libretro/virtualjaguar-libretro/releases/tag/v3.9.1

### AI (reviewed)

v3.8.0 release-notes commit explicitly credits Claude Opus 5.5. Copilot instruction/configuration files are retained as configuration-only evidence rather than independent proof of contribution.
- https://github.com/libretro/virtualjaguar-libretro/commit/e166e0e1fd36d87d85cf16a81db119bb14c0225b

### Relationships (reviewed)

README explicitly documents lineage from David Raingeard's original Virtual Jaguar through SDL/Qt maintenance into the libretro port; the mirror is lineage context, not a second project.
- https://github.com/libretro/virtualjaguar-libretro/blob/master/README.md

## applem-apple-ii-emulator-debugger

Project ID: applem-apple-ii-emulator-debugger · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "applem-apple-ii-emulator-debugger",
  "last_checked": "2026-10-21",
  "status": "v1.9.0 source milestone adds soft-switch breakpoints, a YM2149F Mockingboard option, faster IIgs 6502 execution and IIgs sound/timing fixes; the latest published GitHub release remains v1.6.0",
  "target_cpu": [
    "WebAssembly"
  ],
  "techniques": [
    "WebAssembly emulation",
    "recorded-silicon CPU verification",
    "built-in debugger",
    "disk exploration",
    "MCP/AG-UI control",
    "soft-switch breakpoints"
  ]
}
```

Expected existing project SHA256: ccac2d206ac705dc352c2ce08ece356e13d370296e0d20eb6ba25b683f95a3ee

### Identity (reviewed)

The existing project identity was rechecked against the primary repository.
- https://github.com/mikedaley/web-a2e/blob/main/README.md

### Classification (reviewed)

The existing catalogue classification remains supported by the primary repository.
- https://github.com/mikedaley/web-a2e/blob/main/README.md

### Source CPU (reviewed)

Machine table explicitly identifies NMOS 6502, 65C02 and 65C816; Z80 SoftCard is also implemented.
- https://github.com/mikedaley/web-a2e

### Target CPU (reviewed)

Primary documentation identifies the emulator core as a WebAssembly output; WebAssembly is recorded without inferring a physical host CPU.
- https://github.com/mikedaley/web-a2e/blob/2396c76c3ae306e352bd9783c1a950d1420273f8/README.md

### Build (reviewed)

The v1.9.0 source milestone adds soft-switch change/on/off breakpoints, a YM2149F Mockingboard option, roughly doubled IIgs execution speed for 6502 code and IIgs Ensoniq/vblank fixes. No v1.9.0 GitHub release was published when checked; the latest published release remains v1.6.0. The tracker did not run the web application.
- https://github.com/mikedaley/web-a2e/commit/2396c76c3ae306e352bd9783c1a950d1420273f8
- https://github.com/mikedaley/web-a2e/blob/2396c76c3ae306e352bd9783c1a950d1420273f8/src/js/help/release-notes.js
- https://github.com/mikedaley/web-a2e/commit/3fcca30ab152a5f4c08d97b7cf5512fffe685c92

### Runtime profiles (no-evidence-found)

Historical machine RAM configurations are emulated profiles, not host minimum requirements.
- https://github.com/mikedaley/web-a2e

### AI (reviewed)

The v1.9.0 version commit and IIgs core-update commit explicitly credit Claude Opus 5.5. This establishes assistance on those changes only, not a quantified project-wide contribution.
- https://github.com/mikedaley/web-a2e/commit/2396c76c3ae306e352bd9783c1a950d1420273f8
- https://github.com/mikedaley/web-a2e/commit/3fcca30ab152a5f4c08d97b7cf5512fffe685c92

### Relationships (reviewed)

One coherent emulator supports four Apple II family machines and their shared tooling.
- https://github.com/mikedaley/web-a2e

## pist-atari-st-ide

Project ID: pist-atari-st-ide · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "pist-atari-st-ide",
  "last_checked": "2026-10-21",
  "runtime_profiles": [
    {
      "cpu_family": "x86-64",
      "evidence": [
        "https://github.com/idontwantyourspamthanks/PiST/releases/tag/v0.10.4"
      ],
      "name": "v0.10.4 Linux x86-64 packages",
      "notes": "Published AppImage, Debian and RPM packages bundle PiST, Hatari, vasm and vlink. Release notes map the software floor to Ubuntu 22.04+, Debian 12+ or Fedora 36+. No minimum CPU generation or RAM is stated.",
      "os": "glibc 2.35 or newer",
      "platform": "Linux"
    },
    {
      "cpu_family": "x86-64",
      "evidence": [
        "https://github.com/idontwantyourspamthanks/PiST/releases/tag/v0.10.4"
      ],
      "name": "v0.10.4 Windows x86-64",
      "notes": "Published ZIP/MSI includes the emulator and Visual C++ runtime. Emulator integration is explicitly experimental on Windows; no minimum Windows version, CPU generation or RAM is stated.",
      "platform": "Windows"
    },
    {
      "cpu_family": "arm64",
      "evidence": [
        "https://github.com/idontwantyourspamthanks/PiST/releases/tag/v0.10.4"
      ],
      "name": "v0.10.4 macOS arm64",
      "notes": "Published DMG and tar.gz bundle the emulator and libraries. No minimum macOS version or RAM is stated.",
      "platform": "macOS"
    }
  ],
  "status": "v0.10.4 published; packaged demos now open from writable per-user copies, while Windows emulator integration remains explicitly experimental",
  "target_cpu": [
    "x86-64",
    "arm64"
  ]
}
```

Expected existing project SHA256: a48e5ed621950c7da64bf8fa20ccb6d11571fcfc6c2a904b0177586e4d8aac61

### Identity (reviewed)

PiST is a cross-platform Atari ST/STE 68000 assembly IDE and debugger integrating vasm, vlink and Hatari, with MCP control as adjacent retro-development tooling.
- https://github.com/idontwantyourspamthanks/PiST/releases/tag/v0.10.4

### Classification (reviewed)

The release remains original development/debugging tooling rather than a reconstructed game or emulator-derived port.
- https://github.com/idontwantyourspamthanks/PiST/releases/tag/v0.10.4

### Source CPU (reviewed)

PiST targets Atari ST/STE source projects written for Motorola 68000; this source architecture is retained independently of host package architectures.
- https://github.com/idontwantyourspamthanks/PiST/releases/tag/v0.10.4

### Target CPU (reviewed)

v0.10.4 publishes Linux and Windows x86-64 packages plus macOS arm64 packages. These establish host outputs without implying minimum CPU generations.
- https://github.com/idontwantyourspamthanks/PiST/releases/tag/v0.10.4

### Build (reviewed)

v0.10.4 fixes packaged first-run demos by copying the read-only installed tree into writable per-user storage, migrates saved installed-demo paths and scopes stop-hook trust to files PiST copied. Linux/macOS integration is exercised upstream; Windows emulator integration remains explicitly experimental. The tracker did not run a package.
- https://github.com/idontwantyourspamthanks/PiST/releases/tag/v0.10.4

### Runtime profiles (reviewed)

Release assets explicitly support Linux x86-64, Windows x86-64 and macOS arm64. Linux packages require glibc 2.35 or newer; no minimum CPU generation or RAM is stated. Windows emulator integration is experimental.
- https://github.com/idontwantyourspamthanks/PiST/releases/tag/v0.10.4

### AI (no-evidence-found)

The reviewed v0.10.4 release notes provide no explicit development-AI attribution; configuration files are not treated as proof of contribution.
- https://github.com/idontwantyourspamthanks/PiST/releases/tag/v0.10.4

### Relationships (needs-research)

The bundled Hatari fork and upstream Hatari/vasm/vlink relationships are identified but the fork's independent catalogue scope has not been fully reconciled. Next check: Check the bundled Hatari fork and credited toolchain relationships against existing catalogue records.
- https://github.com/idontwantyourspamthanks/PiST/releases/tag/v0.10.4

## Moria8 — multi-platform 6502 roguelike reimplementation

Project ID: moria8-6502-multiplatform · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "display_title": "Moria8 — multi-platform 6502 roguelike reimplementation",
  "id": "moria8-6502-multiplatform",
  "last_checked": "2026-10-21",
  "status": "released Apple II and Commodore ports plus a buildable/testable Commander X16 65C02/VERA target on current main; independent build and runtime remain unverified",
  "target_cpu": [
    "6502",
    "65C02"
  ],
  "target_platforms": [
    "Apple II",
    "Commodore 64",
    "Commodore 128",
    "Commodore Plus/4",
    "Commander X16"
  ],
  "techniques": [
    "five-platform HAL boundary validation",
    "Commander X16 memory-contract testing",
    "x16emu runtime scenarios"
  ]
}
```

Expected existing project SHA256: b65e47a3984e9cb38110289d6dd56eda43b1bce2be708d89512001988c35a61a

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

Current main builds a Commander X16 ZIP with main, data, overlays, monster tiers, title, licence and source offer; it adds static memory-contract checks and x16emu testbench scenarios alongside five-platform HAL-boundary validation. These are source and upstream test claims only; the tracker did not build or run the target.
- https://github.com/dcgibbons/moria8/commit/60286809eafbd9e804f750d92c07ec2261c0827e
- https://github.com/dcgibbons/moria8/blob/60286809eafbd9e804f750d92c07ec2261c0827e/platforms/cx16/Makefile

### Runtime profiles (reviewed)

The existing Apple II 128 KiB/80-column/ProDOS profile remains sourced. The Commander X16 material states x16emu build/run/test requirements but no minimum physical X16 RAM or hardware revision, so no new minimum runtime profile is inferred.
- https://github.com/dcgibbons/moria8/blob/feed714990ae616dd075b66ff0238b60ee2da0ed/docs/release_notes/release_notes-v1.5.0.md
- https://github.com/dcgibbons/moria8/blob/60286809eafbd9e804f750d92c07ec2261c0827e/README.md

### AI (reviewed)

A bounded history audit inspected the latest 20 commits and two repository-scoped ten-result searches for Claude and AI. Real implementation commits for monster spawning/movement and confusion/stun fixes explicitly carry Claude coauthor trailers. This establishes AI-assisted development in this project, not a quantified contribution or proof every Apple II module was AI-written. Assistant filenames and game monster AI are not used as attribution evidence.
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

## Source ids

```json
[
  "pass25-pool-of-radiance-dos-c-reconstruction",
  "github-yeager-firestaff",
  "pass35-retroio-filesystem-libraries",
  "github-henols-c64-re-tools",
  "github-amypurple-amystudio",
  "intake-libretro-virtualjaguar-libretro",
  "github-mikedaley-web-a2e",
  "github-idontwantyourspamthanks-pist",
  "github-dcgibbons-moria8"
]
```

## Research event notes

The CPU audit queue returned zero unresolved source/target CPU areas. This pass therefore made no speculative CPU assignments; new output architectures are limited to explicit package or source evidence. No candidate project was independently compiled or executed by the tracker.
