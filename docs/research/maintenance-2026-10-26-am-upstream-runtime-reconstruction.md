# Review ten material upstream changes spanning reconstruction exactness, measured FPGA runtime variants, original-homebrew rendering, emulator failure paths and multi-platform build claims.

Review ten material upstream changes spanning reconstruction exactness, measured FPGA runtime variants, original-homebrew rendering, emulator failure paths and multi-platform build claims.

Date: 2026-10-26 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- github-patrickvonmassow-heart-of-africa-remake / Source CPU (no-evidence-found): Primary identity evidence establishes the historical C64 game subject and the remake lineage. It does not explicitly establish the original executable CPU or show a verified original-binary CPU analysis. source_cpu remains empty; no 6510/Z80 value is inferred from platform names or the new implementation language.
- github-patrickvonmassow-heart-of-africa-remake / Target CPU (no-evidence-found): React/Three.js/Vite and browser scripts establish a browser output, but neither TypeScript nor WebGPU identifies a host CPU architecture; target_cpu remains empty.
- github-patrickvonmassow-heart-of-africa-remake / Build (reviewed): The project remains incomplete, and no tracker-side runtime or visual comparison was performed.
- github-patrickvonmassow-heart-of-africa-remake / Runtime profiles (no-evidence-found): README requires Node.js 20+ for development and describes WebGPU rendering with WebGL 2 fallback and lazy-loaded Kokoro TTS. These software/graphics capabilities establish no minimum CPU or RAM; no hardware runtime profile is asserted.
- firestaff-dungeon-master-engine / Build (reviewed): The checks are bounded to the documented routes and do not establish complete native-input, gameplay or timing parity.
- firestaff-dungeon-master-engine / Relationships (needs-research): The reviewed launcher/input/save evidence does not resolve the wider predecessor, successor, fork or credited-source graph. Next check: Check predecessor, successor, fork and credited-source relationships.
- astralbound-amiga-space-trading / Runtime profiles (no-evidence-found): README requires Kickstart 3.0+ for native prototype and expansion RAM; ECS/AGA native modes and CGX/Picasso96-compatible RTG. No independent runtime check.
- caesar0007-nfshs-psx-decomp / Build (needs-research): Reported exact outputs are bounded checkpoints and do not establish complete recovered source or gameplay completeness. Next check: Follow the remaining source/SYM/SLD contracts and only promote whole-project byte-exactness if upstream closes the explicitly retained gaps.
- einstein-newtonos-device-emulator / Runtime profiles (no-evidence-found): The Windows fixes establish supported failure paths, not a minimum host CPU, RAM, Windows version or Newton ROM requirement. No runtime minimum is inferred.
- wing-commander-kilrathi-saga-reconstruction / Target CPU (no-evidence-found): The current README documents Windows, Linux and macOS port packages but no fixed output CPU. Supported architectures are not inferred from C/C++ portability or operating-system names.
- wing-commander-kilrathi-saga-reconstruction / Build (needs-research): The figures are upstream checkpoints, not a complete executable identity or gameplay-completeness result. Next check: Track closure of the remaining strict-byte runs and verify a complete build/runtime claim before promoting whole-project exactness.
- wing-commander-kilrathi-saga-reconstruction / Runtime profiles (no-evidence-found): Needs user-supplied Kilrathi Saga data; partial DOS-data compatibility and Mac SuperWingCommander demo mode documented. Modern native host CPU minimum not established.
- nd120-reconstructed-verilog-cpu / Runtime profiles (reviewed): These are verified FPGA board/build combinations, not proof of a lowest compatible FPGA, RAM minimum or universal timing margin.
- nd120-reconstructed-verilog-cpu / AI (no-evidence-found): Pinned full latest commit message and trailers plus available documentation reviewed. No explicit AI contribution attribution established; usage remains unknown.
- zapple-ii-bpm-prodos-softcard-environment / Runtime profiles (no-evidence-found): The reviewed terminal and CP/M changes do not state a minimum Apple IIe revision, RAM, SoftCard model, ROM or display requirement. No minimum is inferred from the 6502/Z80 code.
- zapple-ii-bpm-prodos-softcard-environment / AI (no-evidence-found): Unknown: bounded primary documentation, sampled implementation/build/licence files and up to three latest full commit messages contain no explicit AI-contribution attribution. Absence is not evidence of non-use.
- m68k-reversing-toolkit-rmtew / Build (needs-research): The tracker did not regenerate or execute the output; the primary source explicitly retains unresolved semantics. Next check: Continue classifying the remaining 22,445 bytes and qualify reconstructed behavior without converting bounded byte equality into a whole-game completeness claim.
- m68k-reversing-toolkit-rmtew / Runtime profiles (needs-research): The restored data and byte-equality checks do not establish a verified minimum Amiga CPU, RAM, chipset or ROM configuration. Next check: Establish explicit minimum runnable hardware only from primary runtime documentation or qualified physical/emulated hardware tests.
- m68k-reversing-toolkit-rmtew / Relationships (needs-research): The Starglider 2 restoration slice does not resolve the remaining predecessor, successor, fork or credited-source graph. Next check: Research remaining predecessor, successor, fork and credited-source relationships after the bounded restoration work stabilizes.
- mega-man-x4-ps1-decompilation / Build (reviewed): Byte identity is scoped to the documented PlayStation executables and does not apply to Linux or Saturn runtime behavior.
- mega-man-x4-ps1-decompilation / Runtime profiles (no-evidence-found): The new README documents toolchains and outputs but no minimum Linux host, PlayStation model, Saturn revision, RAM or OS profile. No hardware minimum is inferred.
- mega-man-x4-ps1-decompilation / AI (no-evidence-found): The reviewed commit contains no development-AI attribution; absence in this bounded commit is not proof of non-use.

## github-patrickvonmassow-heart-of-africa-remake

Project ID: github-patrickvonmassow-heart-of-africa-remake · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "github-patrickvonmassow-heart-of-africa-remake",
  "last_checked": "2026-10-26",
  "status": "Active incomplete browser remake; current work adds measured cross-backend villager load and grip checks and fixes a truncated WebGPU regression signature. The tracker did not run the browser build.",
  "techniques": [
    "reimplementation",
    "runtime-pose export and round-trip validation",
    "measured garment penetration analysis",
    "cross-model review workflow",
    "cross-backend visual regression gates",
    "measurement-led WebGPU failure triage"
  ]
}
```

Expected existing project SHA256: c129e4497ff37fe52bca16ca06a3588d111fda7ae5394f7e9cfa11730b3c8ae2

### Identity (reviewed)

README identifies a from-scratch 3D remake of the 1985 Ozark Softscape game. TypeScript economy implementation calculates treasures, regional trading and ferry passages; the tree includes world, movement, settlement, survival, state and test modules. Vite/React/Three.js package provides build, unit-test and browser-verification scripts. Scope/status: active proof of concept; explicitly incomplete. Metadata and selected file blobs were reviewed; this is not an exhaustive source audit.
- https://github.com/PatrickVonMassow/Heart-of-Africa-Remake/blob/main/README.md
- https://api.github.com/repos/patrickvonmassow/heart-of-africa-remake
- https://github.com/PatrickVonMassow/Heart-of-Africa-Remake/blob/main/src/systems/economy.ts
- https://github.com/patrickvonmassow/heart-of-africa-remake/blob/main/src/state/store.ts
- https://github.com/PatrickVonMassow/Heart-of-Africa-Remake/commit/8cb3aef06d2f10cde6db8133ea796e42a53c64eb

### Classification (reviewed)

The repository remains an incomplete browser reimplementation of The Heart of Africa. The measured villager and renderer work does not establish binary-derived source recovery or relabel this project as a decompilation.
- https://github.com/PatrickVonMassow/Heart-of-Africa-Remake/commit/8cb3aef06d2f10cde6db8133ea796e42a53c64eb

### Source CPU (no-evidence-found)

Primary identity evidence establishes the historical C64 game subject and the remake lineage. It does not explicitly establish the original executable CPU or show a verified original-binary CPU analysis. source_cpu remains empty; no 6510/Z80 value is inferred from platform names or the new implementation language.
- https://github.com/PatrickVonMassow/Heart-of-Africa-Remake/blob/main/README.md
- https://github.com/PatrickVonMassow/Heart-of-Africa-Remake/blob/main/src/systems/economy.ts
- https://github.com/patrickvonmassow/heart-of-africa-remake/blob/main/src/state/store.ts
- https://github.com/PatrickVonMassow/Heart-of-Africa-Remake/blob/main/package.json
- https://github.com/PatrickVonMassow/Heart-of-Africa-Remake/commit/8cb3aef06d2f10cde6db8133ea796e42a53c64eb

### Target CPU (no-evidence-found)

React/Three.js/Vite and browser scripts establish a browser output, but neither TypeScript nor WebGPU identifies a host CPU architecture; target_cpu remains empty.
- https://github.com/PatrickVonMassow/Heart-of-Africa-Remake/blob/main/README.md
- https://github.com/PatrickVonMassow/Heart-of-Africa-Remake/blob/main/src/systems/economy.ts
- https://github.com/patrickvonmassow/heart-of-africa-remake/blob/main/src/state/store.ts
- https://github.com/PatrickVonMassow/Heart-of-Africa-Remake/blob/main/package.json
- https://github.com/PatrickVonMassow/Heart-of-Africa-Remake/commit/8cb3aef06d2f10cde6db8133ea796e42a53c64eb

### Build (reviewed)

Upstream's bounded WebGPU charge fix now reads the preserved prefix of a 200-character-truncated measurement so the known 180-second water-stand failure remains charged. Other commits in the reviewed window add cross-backend villager dress, basket and head-load checks. These are upstream regression results; the tracker did not build, launch or play the remake. Limitations: The project remains incomplete, and no tracker-side runtime or visual comparison was performed.
- https://github.com/PatrickVonMassow/Heart-of-Africa-Remake/commit/8cb3aef06d2f10cde6db8133ea796e42a53c64eb

### Runtime profiles (no-evidence-found)

README requires Node.js 20+ for development and describes WebGPU rendering with WebGL 2 fallback and lazy-loaded Kokoro TTS. These software/graphics capabilities establish no minimum CPU or RAM; no hardware runtime profile is asserted.
- https://github.com/PatrickVonMassow/Heart-of-Africa-Remake/blob/main/README.md
- https://github.com/PatrickVonMassow/Heart-of-Africa-Remake/blob/main/package.json
- https://github.com/PatrickVonMassow/Heart-of-Africa-Remake/blob/main/src/systems/economy.ts
- https://github.com/patrickvonmassow/heart-of-africa-remake/blob/main/src/state/store.ts
- https://github.com/PatrickVonMassow/Heart-of-Africa-Remake/commit/8cb3aef06d2f10cde6db8133ea796e42a53c64eb

### AI (reviewed)

The inspected commit explicitly credits Claude Opus 5.5 (1M context), supporting the existing Claude-family development attribution without implying that every change is model-authored.
- https://github.com/PatrickVonMassow/Heart-of-Africa-Remake/commit/8cb3aef06d2f10cde6db8133ea796e42a53c64eb

### Relationships (reviewed)

No current same-title/alias project found in title, subjects, upstream name, repository and notes comparison; metadata reports non-fork. This is a bounded comparison, not an exhaustive code-provenance audit. The canonical repository root was compared with the hash-verified 1,380-project baseline and discovery indexes at 44558101462cd67db1951803eaeea07aafdff930; no canonical-root collision was found. GitHub fork=false is metadata, not proof of independent authorship. Rights: MIT for original project work. README says original game assets are not used; MIT applies to the project's own work, with third-party data/libraries separately licensed.
- https://github.com/patrickvonmassow/heart-of-africa-remake
- https://github.com/PatrickVonMassow/Heart-of-Africa-Remake/blob/main/README.md
- https://github.com/PatrickVonMassow/Heart-of-Africa-Remake/blob/main/LICENSE
- https://api.github.com/repos/patrickvonmassow/heart-of-africa-remake/git/trees/HEAD?recursive=1
- https://github.com/PatrickVonMassow/Heart-of-Africa-Remake/blob/main/src/systems/economy.ts
- https://github.com/patrickvonmassow/heart-of-africa-remake/blob/main/src/state/store.ts
- https://github.com/PatrickVonMassow/Heart-of-Africa-Remake/commit/8cb3aef06d2f10cde6db8133ea796e42a53c64eb

## firestaff-dungeon-master-engine

Project ID: firestaff-dungeon-master-engine · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "firestaff-dungeon-master-engine",
  "last_checked": "2026-10-26",
  "status": "Development head verifies mixed-media DM1 AUTO selection from the no-game launcher through FM Towns and PC media handoff, alongside new Theron SDL input and Saturn BKR evidence; complete cross-game parity remains open.",
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
    "bounded original-media weather/RNG verification",
    "authenticated alcove interaction regression",
    "authenticated first-combat verification",
    "authenticated five-game main-menu selection",
    "authenticated Amiga 3.6 combat-route verification",
    "source-ordered indoor draw interleaving",
    "bounded missile-chain traversal",
    "retail keyboard-capture reconstruction",
    "mouse-to-pad route validation",
    "Nexus event-44 dispatch tracing",
    "authenticated mixed-media AUTO launcher regression",
    "Saturn BKR save-card decoding"
  ]
}
```

Expected existing project SHA256: 4f19f3e9de5e845f16771c167661621cdfabc54f6a8b35bc2157cec91238edd1

### Identity (reviewed)

Clean-room Dungeon Master-family engine using authenticated original media. Current primary documentation records bounded startup/runtime coverage for DM1 on DOS, Atari ST, Amiga and FM Towns; CSB on Amiga, Atari ST and FM Towns; and DM2 on DOS, Amiga, FM Towns and Macintosh. The latest receipts correct DM1 Amiga HD and DM2 FM Towns boot assertions and expand the cross-game startup matrix and diagnostics. These source-owned handoffs do not establish full campaign, save, display or audio parity; Nexus and Theron's Quest remain explicitly bounded, with authentic level/campaign consumers still incomplete. Evidence: https://github.com/yeager/firestaff/blob/main/README.md https://github.com/yeager/firestaff/blob/main/docs/PROJECT_STATUS.md https://github.com/yeager/firestaff/commit/7791b08de76e https://github.com/yeager/firestaff/commit/17a20bdb465e The newest authenticated-media pass discovers the DM1 Amiga 3.6 archive from configured data roots, covers its root-menu scan, records an Amiga startup-media matrix and wires DM1 PC34 soundtrack selection to WAV playback. These remain bounded startup/audio receipts rather than full-game parity. Evidence: https://github.com/yeager/firestaff/commit/d3b50c77c364455674d783c6bf4d4755777dbc44 https://github.com/yeager/firestaff/commit/ec51d5c1b2f58b51b235fc2145abb384d55b597c https://github.com/yeager/firestaff/commit/da1e85756e618dd321ec42257cb31afbb2b341d1 v3.0.376 receipts now cover DM1 Amiga 2.0 resume, the published Linux x86-64 AppImage under QEMU on an ARM64 VM, and the DM2 FM Towns selected-hero HUD icon sourced from authenticated interface data. They do not establish native x86-64 hardware, physical input, aura/panel completion or full visual parity. The release also publishes Android and iOS arm64 artifacts; publication alone is not runtime verification. Evidence: https://github.com/yeager/firestaff/releases/tag/v3.0.376 https://github.com/yeager/firestaff/commit/e0cf778c39b039918d6b1ae1ebf18e23ec423b1a https://github.com/yeager/firestaff/commit/f0c58017d243551f9dbf30ae5b28fb25172bd10e https://github.com/yeager/firestaff/commit/1be613b14f3cef9e2323a3e2b6ed840e13f6c480 Current-main receipts add native Mac mini M4 DM1 title/door pacing into runtime and authenticated FM Towns startup checks for DM1, CSB and DM2. A four-run French Atari ST test also narrowed an earlier no-output incident to a plausible uninitialized-menu fallback, while explicitly leaving historical causation, physical input, display/palette and audible-speaker parity open. Evidence: https://github.com/yeager/firestaff/commit/7256c2f693a8f2a609ebccfcb687f5e1f8c00868 https://github.com/yeager/firestaff/commit/47bc75ce1f897306e74d2e79a0c053209684edd9 https://github.com/yeager/firestaff/commit/3b729320e80658a8eae965f11c1b5f1bd880f5a3 Current-main Amiga work now paces DM1 A20 palette fades and title zooms against absolute 20 ms source deadlines rather than adding host VSync latency. An authentic Amiga v2.0 native Cocoa run on a Mac mini M4 completed the five-fade title in 1,698 ms (366 ms zoom, 500 ms hold, 166 ms final fade); this does not establish HiDPI/pixel parity or beam-line 152 timing. The authenticated Japanese FM Towns CSB save regression now asserts restored map 0, party position 13,13, direction 1 and four champions through direct launch and the live menu-resume route. Evidence: https://github.com/yeager/firestaff/commit/1538eeab7f46d6318be1c6cd89a55a9edc6d5d87 https://github.com/yeager/firestaff/commit/1d3f8e34d62d0cd9b95d74d9fd33b1bb35eb1a6e https://github.com/yeager/firestaff/commit/087aed4bf4b977cb30805152519c82860ff2ed20 Current-main receipts add an authenticated DM2 Amiga viewport gate, bounded DOS viewport/HUD checks and a locked three-draw fresh-weather RNG bootstrap. Separate native Mac M4 tests keep live Retina input unresolved despite controlled 2x/mixed-geometry tests, and real-media startup reruns use dummy video/audio, so they do not establish physical display, input or speaker parity. Evidence: https://github.com/yeager/firestaff/commit/a3740b43a7bce6f783a003c0dacc312cb2430809 https://github.com/yeager/firestaff/commit/2420045a10244b0431932352c07b5de7328dfe33 https://github.com/yeager/firestaff/commit/b9989304f0e931fc9350ee4b7ac01fa861f2c882 https://github.com/yeager/firestaff/commit/f8465d8e0131e982e296b388e7f66ca62d77e48a https://github.com/yeager/firestaff/commit/a8ff9e734b4ff2837a62e5d2a426455770ee2b0a The newest DM1 pass ports FM Towns title shrink sampling from the documented 6-bit fixed-point source path, flips floor/ceiling graphics at their loaded native heights, and restores the entrance-door step to three 60 Hz VBlank intervals. A separate authenticated PC 3.4 path decodes the LZEXE-packed DOS selector preview. Targeted source-lock/native-build checks pass upstream, but the author explicitly retains original-frame comparison and full cross-platform visual parity as open. Evidence: https://github.com/yeager/firestaff/commit/9a2b86019bfcd6bd513213bc21cd402a4f5adaf0 https://github.com/yeager/firestaff/commit/2a85ec7e1801b58d22232fa11ccc5f18a0e9bd0d https://github.com/yeager/firestaff/commit/41b103f29b4d7439d7445fb4e3578f9985e5cfab https://github.com/yeager/firestaff/commit/3085c2f6d56e8088279b5207bfd46744a1dbbd24 The Apple IIGS path now decodes original dungeon worlds, graphics, startup/font, creature/effect metadata and sound, launches authenticated worlds through the CLI/M12 path, and connects native IIGS mirror recruitment. Primary recovered documentation explicitly identifies hidden Apple IIGS graphics.dat code as 65C816 code, supporting the added source architecture. Current changelog receipts also cover stereo DOC effects, Hall progression, inventory transfer, food use and carrying capacity; wall damage, sensors and full sound/presentation parity remain open. No Apple IIGS minimum RAM or host profile is inferred. Evidence: https://github.com/yeager/firestaff/commit/26f1361e5b3d18512db35b7b0791b84f4e4385da https://github.com/yeager/firestaff/commit/9a7458e5fc0b0f019cbe4284bd9d68384050a56b https://github.com/yeager/firestaff/blob/439213c5ba9fbd79d0753d6143a3b86ff9f0d90f/reference/dmweb-community-docs/html/community/documentation/dungeon-master-and-chaos-strikes-back/graphics.dat-hidden-code.html The DM1 PC34 path now preserves the original status-box priority over overlapping ready-hand zones, verifies consecutive champion switches with authenticated data and prevents held-key selector skips. Debug traces separately measure queue, source-outcome and present-return timing while explicitly marking physical scanout unmeasured. Evidence: https://github.com/yeager/firestaff/commit/449d2322fcf641e88cf876a032ee2cc58ca96373 https://github.com/yeager/firestaff/commit/e5b732073270bbb500d10919239185d212ad6d44 The authenticated DM1 Apple IIGS G20E/G21E editions now reach the first world through both direct CLI and M12 menu launch; the CLI route also accepts a native keyboard turn, and the original media archive is hash-checked before and after the run. The upstream check uses SDL dummy output, so original title/entrance presentation, audible DOC playback and complete-campaign parity remain open. A v3.0.387 preparation change is not represented as a published release because no corresponding release was available when checked. Evidence: https://github.com/yeager/firestaff/commit/c9d9b0e0097242ea1a6f1e5fa29183c3e09bfabb Firestaff v3.0.391 is a published release. Its primary notes record DM1 PC34 selected-save restoration, authenticated English/Japanese CSB FM Towns loose-file startup, and Amiga 3.6 French/German graphic selection. Only seven of ten localized bitmap records are decoded for comparison, and upstream explicitly says these checks do not establish complete visual or gameplay parity. Evidence: https://github.com/yeager/firestaff/releases/tag/v3.0.391 https://github.com/yeager/firestaff/commit/ebb10387f277af76683e3aadd27f97dab963d599 https://github.com/yeager/firestaff/commit/d15a674ba936133e9b74b43af982051927f51207 Firestaff v3.0.397 reuses verified hashes for nested archive members while retaining archive freshness checks. On the tested Mac mini M4, the authentic five-game scan took 27.90 seconds cold and 12.35 seconds warm; other platforms and cold-cache performance remain explicitly unverified, and SDL dummy checks do not establish native display, physical input, audible output or complete parity. Evidence: https://github.com/yeager/firestaff/releases/tag/v3.0.397 A current primary-source test now exercises five explicitly named Dungeon Master-family selections without broadening the project beyond its documented clean-room reconstruction scope.
- https://github.com/yeager/firestaff
- https://github.com/yeager/firestaff/commit/034ff0ab6fb9bac543f756207f608ca143e3778e
- https://github.com/yeager/firestaff/commit/2d511dd960811309f78d6720d3e7c68014676de1
- https://github.com/yeager/firestaff/commit/fb04a6a8485dcffe9f668a9e0aa32d5a58842ef1
- https://github.com/yeager/firestaff/commit/9857d924c8501b0d2b7928756183d3d1c6eec56f
- https://github.com/yeager/firestaff/commit/860b47b315cb62ee1a1ed316689cdf3dc0408650
- https://github.com/yeager/firestaff/commit/14a084
- https://github.com/yeager/firestaff/commit/cce374
- https://github.com/yeager/firestaff/commit/1f33af
- https://github.com/yeager/firestaff/commit/3e3ec633f0a61c5f17358567e086a5343e39be1d

### Classification (reviewed)

The new work remains a clean-room Dungeon Master-family reconstruction: authenticated media drives a bounded Amiga 3.6 combat route, while DM2 rendering and missile behavior follow inspected source order.
- https://github.com/yeager/firestaff
- https://github.com/yeager/firestaff/commit/2d511dd960811309f78d6720d3e7c68014676de1
- https://github.com/yeager/firestaff/commit/fb04a6a8485dcffe9f668a9e0aa32d5a58842ef1
- https://github.com/yeager/firestaff/commit/9857d924c8501b0d2b7928756183d3d1c6eec56f
- https://github.com/yeager/firestaff/commit/860b47b315cb62ee1a1ed316689cdf3dc0408650
- https://github.com/yeager/firestaff/commit/14a084
- https://github.com/yeager/firestaff/commit/cce374
- https://github.com/yeager/firestaff/commit/1f33af
- https://github.com/yeager/firestaff/commit/3e3ec633f0a61c5f17358567e086a5343e39be1d

### Source CPU (reviewed)

Recovered primary Apple IIGS documentation explicitly identifies code embedded in graphics.dat as 65C816 code. The project record adds 65C816 without inferring any host or minimum runtime architecture.
- https://github.com/yeager/firestaff/blob/439213c5ba9fbd79d0753d6143a3b86ff9f0d90f/reference/dmweb-community-docs/html/community/documentation/dungeon-master-and-chaos-strikes-back/graphics.dat-hidden-code.html
- https://github.com/yeager/firestaff/commit/2d511dd960811309f78d6720d3e7c68014676de1
- https://github.com/yeager/firestaff/commit/fb04a6a8485dcffe9f668a9e0aa32d5a58842ef1
- https://github.com/yeager/firestaff/commit/9857d924c8501b0d2b7928756183d3d1c6eec56f
- https://github.com/yeager/firestaff/commit/860b47b315cb62ee1a1ed316689cdf3dc0408650
- https://github.com/yeager/firestaff/commit/14a084
- https://github.com/yeager/firestaff/commit/cce374
- https://github.com/yeager/firestaff/commit/1f33af
- https://github.com/yeager/firestaff/commit/3e3ec633f0a61c5f17358567e086a5343e39be1d

### Target CPU (reviewed)

v3.0.371 publishes explicit x86-64 and arm64 host artifacts; the record uses the existing x86 family label plus arm64 without inferring older x86 minima.
- https://github.com/yeager/firestaff/releases/tag/v3.0.371
- https://github.com/yeager/firestaff/commit/2d511dd960811309f78d6720d3e7c68014676de1
- https://github.com/yeager/firestaff/commit/fb04a6a8485dcffe9f668a9e0aa32d5a58842ef1
- https://github.com/yeager/firestaff/commit/9857d924c8501b0d2b7928756183d3d1c6eec56f
- https://github.com/yeager/firestaff/commit/860b47b315cb62ee1a1ed316689cdf3dc0408650
- https://github.com/yeager/firestaff/commit/14a084
- https://github.com/yeager/firestaff/commit/cce374
- https://github.com/yeager/firestaff/commit/1f33af
- https://github.com/yeager/firestaff/commit/3e3ec633f0a61c5f17358567e086a5343e39be1d

### Build (reviewed)

The merged regression now starts without --game, --data-dir or FIRESTAFF_DATA, waits for the scan, drives the no-game menu, and checks FM Towns and PC 3.4 media discovery plus FM Towns handoff. The wider reviewed window also carries Theron SDL input routes and Saturn BKR parsing. These are upstream authenticated-media tests; the tracker did not build or run Firestaff. Limitations: The checks are bounded to the documented routes and do not establish complete native-input, gameplay or timing parity.
- https://github.com/yeager/firestaff/commit/3e3ec633f0a61c5f17358567e086a5343e39be1d

### Runtime profiles (reviewed)

Input reconstruction adds no minimum host CPU, RAM or OS evidence. Existing explicit artifact and Apple Silicon test profiles remain unchanged.
- https://github.com/yeager/firestaff/releases/tag/v3.0.397
- https://github.com/yeager/firestaff/commit/2d511dd960811309f78d6720d3e7c68014676de1
- https://github.com/yeager/firestaff/commit/fb04a6a8485dcffe9f668a9e0aa32d5a58842ef1
- https://github.com/yeager/firestaff/commit/9857d924c8501b0d2b7928756183d3d1c6eec56f
- https://github.com/yeager/firestaff/commit/860b47b315cb62ee1a1ed316689cdf3dc0408650
- https://github.com/yeager/firestaff/commit/14a084
- https://github.com/yeager/firestaff/commit/cce374
- https://github.com/yeager/firestaff/commit/1f33af
- https://github.com/yeager/firestaff/commit/3e3ec633f0a61c5f17358567e086a5343e39be1d

### AI (reviewed)

Existing explicit Claude project-agent evidence remains valid; no weaker inference was substituted.
- https://github.com/yeager/firestaff
- https://github.com/yeager/firestaff/commit/2d511dd960811309f78d6720d3e7c68014676de1
- https://github.com/yeager/firestaff/commit/fb04a6a8485dcffe9f668a9e0aa32d5a58842ef1
- https://github.com/yeager/firestaff/commit/9857d924c8501b0d2b7928756183d3d1c6eec56f
- https://github.com/yeager/firestaff/commit/860b47b315cb62ee1a1ed316689cdf3dc0408650
- https://github.com/yeager/firestaff/commit/14a084
- https://github.com/yeager/firestaff/commit/cce374
- https://github.com/yeager/firestaff/commit/1f33af
- https://github.com/yeager/firestaff/commit/3e3ec633f0a61c5f17358567e086a5343e39be1d

### Relationships (needs-research)

The reviewed launcher/input/save evidence does not resolve the wider predecessor, successor, fork or credited-source graph. Next check: Check predecessor, successor, fork and credited-source relationships.
- https://github.com/yeager/firestaff/commit/3e3ec633f0a61c5f17358567e086a5343e39be1d

## astralbound-amiga-space-trading

Project ID: astralbound-amiga-space-trading · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "astralbound-amiga-space-trading",
  "last_checked": "2026-10-26",
  "status": "Original native Amiga space-trading game; current source adds Enhanced Bezier rings and fixes Classic planet occlusion and orbital terrain-colour parity. Independent build/run not performed.",
  "techniques": [
    "great-circle contour parity validation",
    "renderer regression testing"
  ]
}
```

Expected existing project SHA256: 0845744c94b937187c3bb7673443c9241edfd57264d2bf72ceb067738ffb1d39

### Identity (reviewed)

Original solid-polygon space-trading/combat prototype inspired by Frontier: Elite II. Contains substantial original universe generation, terrain renderer, physics, ports, contracts, combat, save state and ECS/AGA/RTG Amiga backends, rather than an emulated original game.
- https://github.com/sacredbanana/astralbound/blob/07829b8c78f1ece3b75ab4460115ca3f351d0cc5/README.md
- https://github.com/sacredbanana/astralbound/blob/07829b8c78f1ece3b75ab4460115ca3f351d0cc5/src/game.c
- https://github.com/sacredbanana/astralbound/blob/07829b8c78f1ece3b75ab4460115ca3f351d0cc5/src/render.c
- https://github.com/sacredbanana/astralbound/blob/07829b8c78f1ece3b75ab4460115ca3f351d0cc5/src/platform/amiga.c
- https://github.com/sacredbanana/astralbound/blob/07829b8c78f1ece3b75ab4460115ca3f351d0cc5/Makefile.Amiga
- https://github.com/sacredbanana/astralbound/blob/07829b8c78f1ece3b75ab4460115ca3f351d0cc5/LICENSE
- https://github.com/sacredbanana/astralbound/blob/07829b8c78f1ece3b75ab4460115ca3f351d0cc5/THIRD_PARTY.txt
- https://github.com/sacredbanana/astralbound/blob/07829b8c78f1ece3b75ab4460115ca3f351d0cc5/data/README.md
- https://github.com/sacredbanana/astralbound/commit/07829b8c78f1ece3b75ab4460115ca3f351d0cc5
- https://github.com/sacredbanana/astralbound/commit/17083aa560002c54ca8a190447ec6fc5bb0b10fb

### Classification (reviewed)

Astralbound remains substantial original homebrew for Amiga. The renderer changes are native game development and are not evidence of reverse engineering or an RE-derived port.
- https://github.com/sacredbanana/astralbound/commit/17083aa560002c54ca8a190447ec6fc5bb0b10fb

### Source CPU (not-applicable)

No recovered binary/source predecessor architecture is asserted.
- https://github.com/sacredbanana/astralbound/blob/07829b8c78f1ece3b75ab4460115ca3f351d0cc5/README.md
- https://github.com/sacredbanana/astralbound/blob/07829b8c78f1ece3b75ab4460115ca3f351d0cc5/src/game.c
- https://github.com/sacredbanana/astralbound/blob/07829b8c78f1ece3b75ab4460115ca3f351d0cc5/src/render.c
- https://github.com/sacredbanana/astralbound/blob/07829b8c78f1ece3b75ab4460115ca3f351d0cc5/src/platform/amiga.c
- https://github.com/sacredbanana/astralbound/blob/07829b8c78f1ece3b75ab4460115ca3f351d0cc5/Makefile.Amiga
- https://github.com/sacredbanana/astralbound/blob/07829b8c78f1ece3b75ab4460115ca3f351d0cc5/LICENSE
- https://github.com/sacredbanana/astralbound/blob/07829b8c78f1ece3b75ab4460115ca3f351d0cc5/THIRD_PARTY.txt
- https://github.com/sacredbanana/astralbound/blob/07829b8c78f1ece3b75ab4460115ca3f351d0cc5/data/README.md
- https://github.com/sacredbanana/astralbound/commit/07829b8c78f1ece3b75ab4460115ca3f351d0cc5
- https://github.com/sacredbanana/astralbound/commit/17083aa560002c54ca8a190447ec6fc5bb0b10fb

### Target CPU (reviewed)

Architectures describe native outputs, not build-machine CPUs.
- https://github.com/sacredbanana/astralbound/blob/07829b8c78f1ece3b75ab4460115ca3f351d0cc5/README.md
- https://github.com/sacredbanana/astralbound/blob/07829b8c78f1ece3b75ab4460115ca3f351d0cc5/src/game.c
- https://github.com/sacredbanana/astralbound/blob/07829b8c78f1ece3b75ab4460115ca3f351d0cc5/src/render.c
- https://github.com/sacredbanana/astralbound/blob/07829b8c78f1ece3b75ab4460115ca3f351d0cc5/src/platform/amiga.c
- https://github.com/sacredbanana/astralbound/blob/07829b8c78f1ece3b75ab4460115ca3f351d0cc5/Makefile.Amiga
- https://github.com/sacredbanana/astralbound/blob/07829b8c78f1ece3b75ab4460115ca3f351d0cc5/LICENSE
- https://github.com/sacredbanana/astralbound/blob/07829b8c78f1ece3b75ab4460115ca3f351d0cc5/THIRD_PARTY.txt
- https://github.com/sacredbanana/astralbound/blob/07829b8c78f1ece3b75ab4460115ca3f351d0cc5/data/README.md
- https://github.com/sacredbanana/astralbound/commit/07829b8c78f1ece3b75ab4460115ca3f351d0cc5
- https://github.com/sacredbanana/astralbound/commit/17083aa560002c54ca8a190447ec6fc5bb0b10fb

### Build (reviewed)

Upstream replaces direct noise sampling with contour-loop parity anchored at cube corners, adds seam/LOD parity tests, and adds an orbital renderer regression to prevent whole-region colour flicker. The tracker did not compile or run either Classic or Enhanced rendering.
- https://github.com/sacredbanana/astralbound/commit/17083aa560002c54ca8a190447ec6fc5bb0b10fb

### Runtime profiles (no-evidence-found)

README requires Kickstart 3.0+ for native prototype and expansion RAM; ECS/AGA native modes and CGX/Picasso96-compatible RTG. No independent runtime check.
- https://github.com/sacredbanana/astralbound/blob/07829b8c78f1ece3b75ab4460115ca3f351d0cc5/README.md
- https://github.com/sacredbanana/astralbound/blob/07829b8c78f1ece3b75ab4460115ca3f351d0cc5/src/game.c
- https://github.com/sacredbanana/astralbound/blob/07829b8c78f1ece3b75ab4460115ca3f351d0cc5/src/render.c
- https://github.com/sacredbanana/astralbound/blob/07829b8c78f1ece3b75ab4460115ca3f351d0cc5/src/platform/amiga.c
- https://github.com/sacredbanana/astralbound/blob/07829b8c78f1ece3b75ab4460115ca3f351d0cc5/Makefile.Amiga
- https://github.com/sacredbanana/astralbound/blob/07829b8c78f1ece3b75ab4460115ca3f351d0cc5/LICENSE
- https://github.com/sacredbanana/astralbound/blob/07829b8c78f1ece3b75ab4460115ca3f351d0cc5/THIRD_PARTY.txt
- https://github.com/sacredbanana/astralbound/blob/07829b8c78f1ece3b75ab4460115ca3f351d0cc5/data/README.md
- https://github.com/sacredbanana/astralbound/commit/07829b8c78f1ece3b75ab4460115ca3f351d0cc5
- https://github.com/sacredbanana/astralbound/commit/17083aa560002c54ca8a190447ec6fc5bb0b10fb

### AI (reviewed)

Pinned full latest commit explicitly credits Claude Opus 5.5 via Co-Authored-By trailer.
- https://github.com/sacredbanana/astralbound/blob/07829b8c78f1ece3b75ab4460115ca3f351d0cc5/README.md
- https://github.com/sacredbanana/astralbound/blob/07829b8c78f1ece3b75ab4460115ca3f351d0cc5/src/game.c
- https://github.com/sacredbanana/astralbound/blob/07829b8c78f1ece3b75ab4460115ca3f351d0cc5/src/render.c
- https://github.com/sacredbanana/astralbound/blob/07829b8c78f1ece3b75ab4460115ca3f351d0cc5/src/platform/amiga.c
- https://github.com/sacredbanana/astralbound/blob/07829b8c78f1ece3b75ab4460115ca3f351d0cc5/Makefile.Amiga
- https://github.com/sacredbanana/astralbound/blob/07829b8c78f1ece3b75ab4460115ca3f351d0cc5/LICENSE
- https://github.com/sacredbanana/astralbound/blob/07829b8c78f1ece3b75ab4460115ca3f351d0cc5/THIRD_PARTY.txt
- https://github.com/sacredbanana/astralbound/blob/07829b8c78f1ece3b75ab4460115ca3f351d0cc5/data/README.md
- https://github.com/sacredbanana/astralbound/commit/07829b8c78f1ece3b75ab4460115ca3f351d0cc5
- https://github.com/sacredbanana/astralbound/commit/17083aa560002c54ca8a190447ec6fc5bb0b10fb

### Relationships (reviewed)

Inspired by Frontier: Elite II; explicitly original source and assets, not its decompilation.
- https://github.com/sacredbanana/astralbound/blob/07829b8c78f1ece3b75ab4460115ca3f351d0cc5/README.md
- https://github.com/sacredbanana/astralbound/blob/07829b8c78f1ece3b75ab4460115ca3f351d0cc5/src/game.c
- https://github.com/sacredbanana/astralbound/blob/07829b8c78f1ece3b75ab4460115ca3f351d0cc5/src/render.c
- https://github.com/sacredbanana/astralbound/blob/07829b8c78f1ece3b75ab4460115ca3f351d0cc5/src/platform/amiga.c
- https://github.com/sacredbanana/astralbound/blob/07829b8c78f1ece3b75ab4460115ca3f351d0cc5/Makefile.Amiga
- https://github.com/sacredbanana/astralbound/blob/07829b8c78f1ece3b75ab4460115ca3f351d0cc5/LICENSE
- https://github.com/sacredbanana/astralbound/blob/07829b8c78f1ece3b75ab4460115ca3f351d0cc5/THIRD_PARTY.txt
- https://github.com/sacredbanana/astralbound/blob/07829b8c78f1ece3b75ab4460115ca3f351d0cc5/data/README.md
- https://github.com/sacredbanana/astralbound/commit/07829b8c78f1ece3b75ab4460115ca3f351d0cc5
- https://github.com/sacredbanana/astralbound/commit/17083aa560002c54ca8a190447ec6fc5bb0b10fb

## caesar0007-nfshs-psx-decomp

Project ID: caesar0007-nfshs-psx-decomp · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "caesar0007-nfshs-psx-decomp",
  "last_checked": "2026-10-26",
  "status": "Active PlayStation source reconstruction: upstream reports 246 complete function contracts, 119 unchanged normal ELFs, and a 299,819/299,819 reconstructed-image comparison while explicitly retaining unresolved source/SYM/SLD work.",
  "techniques": [
    "SYM/SLD ownership-contract validation",
    "source-only build gates",
    "whole-image byte comparison"
  ]
}
```

Expected existing project SHA256: 1828f3e5dc888e02a8672cbfc441ff4f8881aa70ab0fc725d5b8308e86b4d3b0

### Identity (reviewed)

Need for Speed High Stakes — PSX matching reconstruction. Repository root and implementation inspected at pinned revisions.
- https://github.com/caesar0007/nfshs-psx-decomp/blob/fa6a3a2ecc09a90abbcdc241af4e491be0c383b9/README.md
- https://github.com/Caesar0007/NFSHS-PSX-decomp/blob/fa6a3a2ecc09a90abbcdc241af4e491be0c383b9/README.md
- https://github.com/Caesar0007/NFSHS-PSX-decomp/blob/fa6a3a2ecc09a90abbcdc241af4e491be0c383b9/src/aiinit.c
- https://github.com/Caesar0007/NFSHS-PSX-decomp/commit/e811441133ea7118cc834772343e105bd4ff158e

### Classification (reviewed)

Matching and reconstruction tracks coexist. Inspected aiinit.c is INCLUDE_ASM wrappers, not recovered C bodies; README percentages are dated author reports, not a current semantic completeness measure.
- https://github.com/caesar0007/nfshs-psx-decomp/blob/fa6a3a2ecc09a90abbcdc241af4e491be0c383b9/README.md
- https://github.com/Caesar0007/NFSHS-PSX-decomp/blob/fa6a3a2ecc09a90abbcdc241af4e491be0c383b9/README.md
- https://github.com/Caesar0007/NFSHS-PSX-decomp/blob/fa6a3a2ecc09a90abbcdc241af4e491be0c383b9/src/aiinit.c
- https://github.com/Caesar0007/NFSHS-PSX-decomp/commit/e811441133ea7118cc834772343e105bd4ff158e

### Source CPU (reviewed)

Architecture context: mips. Source and target roles are recorded separately.
- https://github.com/caesar0007/nfshs-psx-decomp/blob/fa6a3a2ecc09a90abbcdc241af4e491be0c383b9/README.md
- https://github.com/Caesar0007/NFSHS-PSX-decomp/blob/fa6a3a2ecc09a90abbcdc241af4e491be0c383b9/README.md
- https://github.com/Caesar0007/NFSHS-PSX-decomp/blob/fa6a3a2ecc09a90abbcdc241af4e491be0c383b9/src/aiinit.c
- https://github.com/Caesar0007/NFSHS-PSX-decomp/commit/e811441133ea7118cc834772343e105bd4ff158e

### Target CPU (reviewed)

Explicit output/execution architecture: mips.
- https://github.com/caesar0007/nfshs-psx-decomp/blob/fa6a3a2ecc09a90abbcdc241af4e491be0c383b9/README.md
- https://github.com/Caesar0007/NFSHS-PSX-decomp/blob/fa6a3a2ecc09a90abbcdc241af4e491be0c383b9/README.md
- https://github.com/Caesar0007/NFSHS-PSX-decomp/blob/fa6a3a2ecc09a90abbcdc241af4e491be0c383b9/src/aiinit.c
- https://github.com/Caesar0007/NFSHS-PSX-decomp/commit/e811441133ea7118cc834772343e105bd4ff158e

### Build (needs-research)

The reviewed commit reports one additional complete Track function contract (246 total), 119 unchanged normal ELFs, 117 tests, and a 299,819/299,819 reconstructed-image comparison. It separately records unresolved block/source contracts and says the wider source/SYM/SLD goal remains incomplete. The tracker did not build, run or byte-compare the project. Limitations: Reported exact outputs are bounded checkpoints and do not establish complete recovered source or gameplay completeness. Next check: Follow the remaining source/SYM/SLD contracts and only promote whole-project byte-exactness if upstream closes the explicitly retained gaps.
- https://github.com/Caesar0007/NFSHS-PSX-decomp/commit/e811441133ea7118cc834772343e105bd4ff158e

### Runtime profiles (reviewed)

Author publishes restrictive licensing; viewing source is not a grant to build or redistribute ports.
- https://github.com/caesar0007/nfshs-psx-decomp/blob/fa6a3a2ecc09a90abbcdc241af4e491be0c383b9/README.md
- https://github.com/Caesar0007/NFSHS-PSX-decomp/blob/fa6a3a2ecc09a90abbcdc241af4e491be0c383b9/README.md
- https://github.com/Caesar0007/NFSHS-PSX-decomp/blob/fa6a3a2ecc09a90abbcdc241af4e491be0c383b9/src/aiinit.c
- https://github.com/Caesar0007/NFSHS-PSX-decomp/commit/e811441133ea7118cc834772343e105bd4ff158e

### AI (reviewed)

An inspected reconstruction commit explicitly credits Claude Opus 5.5, supporting the project-level Claude attribution; the latest contract-restoration commit itself contains no co-author trailer.
- https://github.com/Caesar0007/NFSHS-PSX-decomp/commit/b3a6e2d4b7dbe4cab0fbff28819566187651780b
- https://github.com/Caesar0007/NFSHS-PSX-decomp/commit/e811441133ea7118cc834772343e105bd4ff158e

### Relationships (reviewed)

README links XProger as separately authorized port; do not conflate matching project and port.
- https://github.com/caesar0007/nfshs-psx-decomp/blob/fa6a3a2ecc09a90abbcdc241af4e491be0c383b9/README.md
- https://github.com/Caesar0007/NFSHS-PSX-decomp/blob/fa6a3a2ecc09a90abbcdc241af4e491be0c383b9/README.md
- https://github.com/Caesar0007/NFSHS-PSX-decomp/blob/fa6a3a2ecc09a90abbcdc241af4e491be0c383b9/src/aiinit.c
- https://github.com/Caesar0007/NFSHS-PSX-decomp/commit/e811441133ea7118cc834772343e105bd4ff158e

## einstein-newtonos-device-emulator

Project ID: einstein-newtonos-device-emulator · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "einstein-newtonos-device-emulator",
  "last_checked": "2026-10-26",
  "status": "NewtonOS device emulator; current release notes document Windows fast-start shutdown, waveOut deadlock and unresponsive-download fixes. Independent build/run not performed.",
  "techniques": [
    "Windows waveOut concurrency repair",
    "failure-path regression handling"
  ]
}
```

Expected existing project SHA256: f3b490123461898a39ec6f35b1b329b958a6ee18f7f52f6cf1f20016a3272771

### Identity (reviewed)

Long-running Apple Newton emulator with ARM processor/JIT, memory/MMU, display, interrupt, serial/network and PCMCIA emulation plus debugger and cross-platform frontends.
- https://github.com/pguyot/Einstein/blob/a152dfa1c06d6ec2de09b4e4febebdab1c1df749/README.md
- https://github.com/pguyot/Einstein/blob/a152dfa1c06d6ec2de09b4e4febebdab1c1df749/LICENSE
- https://github.com/pguyot/Einstein/commit/15feb0494700888cef086291ad18bf40ba29b36e

### Classification (reviewed)

Requires separately supplied Newton ROM; README says project cannot distribute it. Guest operating system is original ROM software executed by emulator, not a source reconstruction. Supported and partial host claims kept separate. GPL-2.0-or-later in processor header with GPLv2 root text; bundled libraries have their own terms. Newton ROM rights are not granted by emulator licence.
- https://github.com/pguyot/Einstein/blob/a152dfa1c06d6ec2de09b4e4febebdab1c1df749/README.md
- https://github.com/pguyot/Einstein/blob/a152dfa1c06d6ec2de09b4e4febebdab1c1df749/LICENSE
- https://github.com/pguyot/Einstein/commit/15feb0494700888cef086291ad18bf40ba29b36e

### Source CPU (reviewed)

Documented source/input platforms: Apple Newton MessagePad, NewtonOS. Processor scope: ARM.
- https://github.com/pguyot/Einstein/blob/a152dfa1c06d6ec2de09b4e4febebdab1c1df749/README.md
- https://github.com/pguyot/Einstein/blob/a152dfa1c06d6ec2de09b4e4febebdab1c1df749/LICENSE
- https://github.com/pguyot/Einstein/commit/15feb0494700888cef086291ad18bf40ba29b36e

### Target CPU (reviewed)

No fixed target CPU is established; portability of the implementation language is not proof of supported architectures.
- https://github.com/pguyot/Einstein/blob/a152dfa1c06d6ec2de09b4e4febebdab1c1df749/README.md
- https://github.com/pguyot/Einstein/blob/a152dfa1c06d6ec2de09b4e4febebdab1c1df749/LICENSE
- https://github.com/pguyot/Einstein/commit/15feb0494700888cef086291ad18bf40ba29b36e

### Build (reviewed)

Upstream release notes document three repaired failure paths: Windows close with fast start, a waveOut callback deadlock when NewtonOS stops audio, and Install Essentials handling of a non-responsive server. The tracker did not build or run Einstein on Windows or another host.
- https://github.com/pguyot/Einstein/commit/15feb0494700888cef086291ad18bf40ba29b36e

### Runtime profiles (no-evidence-found)

The Windows fixes establish supported failure paths, not a minimum host CPU, RAM, Windows version or Newton ROM requirement. No runtime minimum is inferred.
- https://github.com/pguyot/Einstein/commit/15feb0494700888cef086291ad18bf40ba29b36e

### AI (reviewed)

The release-note commit explicitly credits Claude Opus 5.5, confirming the existing Claude-family development attribution.
- https://github.com/pguyot/Einstein/commit/15feb0494700888cef086291ad18bf40ba29b36e

### Relationships (reviewed)

Separate Newton lineage from tracked Palm emulators.
- https://github.com/pguyot/Einstein/blob/a152dfa1c06d6ec2de09b4e4febebdab1c1df749/README.md
- https://github.com/pguyot/Einstein/blob/a152dfa1c06d6ec2de09b4e4febebdab1c1df749/LICENSE
- https://github.com/pguyot/Einstein/commit/15feb0494700888cef086291ad18bf40ba29b36e

## wing-commander-kilrathi-saga-reconstruction

Project ID: wing-commander-kilrathi-saga-reconstruction · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "wing-commander-kilrathi-saga-reconstruction",
  "last_checked": "2026-10-26",
  "status": "Working Win32 reconstruction and SDL2 port; upstream reports 516,228 of 518,656 strict-matching bytes (99.5319%) with 2,428 differing positions in 565 runs, while current navigation/expression probes remain deliberately unretained.",
  "techniques": [
    "strict whole-file executable comparison",
    "per-function machine-code similarity auditing",
    "discarded-probe recording",
    "register-lifetime probe recording",
    "byte-for-byte function matching"
  ]
}
```

Expected existing project SHA256: b8db090e58e6aa00037e637f396521e334412c61646b958a4fc6649611a30619

### Identity (reviewed)

Recovered native C/C++ game source for1996 Win32 Wing Commander, plus SDL2 port and annotated original-binary comparison workflow. The current source remains the same recovered native Win32 game reconstruction and SDL2 port; the new work is a bounded recovery of inflight-computer byte layout rather than a new port or separate subject.
- https://github.com/neuromancer/wc1-re/blob/f2afbcd542e60fa039a52b0b58518a11a0069f11/README.md
- https://github.com/neuromancer/wc1-re/blob/f2afbcd542e60fa039a52b0b58518a11a0069f11/Makefile
- https://github.com/neuromancer/wc1-re/commit/2bb053685774ff044ca730572bd5777baadfb5e5
- https://github.com/neuromancer/wc1-re/commit/60da3dd5763c9ffbcdc9f3b37887422cf88b3ed7
- https://github.com/neuromancer/wc1-re/commit/b4832d57155e0aa5f6e7a8e410eaaae7b808c8a1

### Classification (reviewed)

Byte-for-byte reconstruction explicitly incomplete; annotated per-function report can miss unreconstructed routines between functions and is not gameplay completeness. Native recovered gameplay logic exists; not a generic CPU wrapper. GPL3 root LICENSE; proprietary data not distributed.
- https://github.com/neuromancer/wc1-re/blob/f2afbcd542e60fa039a52b0b58518a11a0069f11/README.md
- https://github.com/neuromancer/wc1-re/blob/f2afbcd542e60fa039a52b0b58518a11a0069f11/Makefile
- https://github.com/neuromancer/wc1-re/commit/b4832d57155e0aa5f6e7a8e410eaaae7b808c8a1

### Source CPU (reviewed)

Documented source/input platforms: Windows, DOS. Processor scope: x86.
- https://github.com/neuromancer/wc1-re/blob/f2afbcd542e60fa039a52b0b58518a11a0069f11/README.md
- https://github.com/neuromancer/wc1-re/blob/f2afbcd542e60fa039a52b0b58518a11a0069f11/Makefile
- https://github.com/neuromancer/wc1-re/commit/b4832d57155e0aa5f6e7a8e410eaaae7b808c8a1

### Target CPU (no-evidence-found)

The current README documents Windows, Linux and macOS port packages but no fixed output CPU. Supported architectures are not inferred from C/C++ portability or operating-system names.
- https://github.com/neuromancer/wc1-re/blob/3708d5f616feb26ed5256bec027f812dc26e1a09/README.md
- https://github.com/neuromancer/wc1-re/commit/b4832d57155e0aa5f6e7a8e410eaaae7b808c8a1

### Build (needs-research)

Upstream records 516,228 of 518,656 strictly matching bytes (99.5319%), leaving 2,428 differing positions in 565 runs. The reviewed navigation, mission-reset, formatter and arithmetic experiments are explicitly rejected because they do not improve strict matching or regress another routine. The tracker did not compile or execute the reconstruction. Limitations: The figures are upstream checkpoints, not a complete executable identity or gameplay-completeness result. Next check: Track closure of the remaining strict-byte runs and verify a complete build/runtime claim before promoting whole-project exactness.
- https://github.com/neuromancer/wc1-re/commit/b4832d57155e0aa5f6e7a8e410eaaae7b808c8a1

### Runtime profiles (no-evidence-found)

Needs user-supplied Kilrathi Saga data; partial DOS-data compatibility and Mac SuperWingCommander demo mode documented. Modern native host CPU minimum not established.
- https://github.com/neuromancer/wc1-re/blob/f2afbcd542e60fa039a52b0b58518a11a0069f11/README.md
- https://github.com/neuromancer/wc1-re/blob/f2afbcd542e60fa039a52b0b58518a11a0069f11/Makefile
- https://github.com/neuromancer/wc1-re/commit/b4832d57155e0aa5f6e7a8e410eaaae7b808c8a1

### AI (reviewed)

README explicitly states Codex and Claude were used during reconstruction; actual contribution evidence rather than AGENTS presence.
- https://github.com/neuromancer/wc1-re/blob/f2afbcd542e60fa039a52b0b58518a11a0069f11/README.md
- https://github.com/neuromancer/wc1-re/blob/f2afbcd542e60fa039a52b0b58518a11a0069f11/Makefile
- https://github.com/neuromancer/wc1-re/commit/b4832d57155e0aa5f6e7a8e410eaaae7b808c8a1

### Relationships (reviewed)

Acknowledged historical compatibility fixes/research reference. https://github.com/Bekenn/wcdx Optional comparison/verification dependency. https://github.com/gg-sl-oss/binary-comp
- https://github.com/neuromancer/wc1-re/blob/f2afbcd542e60fa039a52b0b58518a11a0069f11/README.md
- https://github.com/neuromancer/wc1-re/blob/f2afbcd542e60fa039a52b0b58518a11a0069f11/Makefile
- https://github.com/neuromancer/wc1-re/commit/b4832d57155e0aa5f6e7a8e410eaaae7b808c8a1

## nd120-reconstructed-verilog-cpu

Project ID: nd120-reconstructed-verilog-cpu · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "build": {
    "byte_exact": null,
    "compilable": true,
    "playable": null,
    "runnable": true
  },
  "id": "nd120-reconstructed-verilog-cpu",
  "last_checked": "2026-10-26",
  "runtime_profiles": [
    {
      "cpu_family": "ND-120",
      "evidence": [
        {
          "excerpt": "SMD + tape reader ... routed; 21540& boots SINTRAN in 26 s",
          "source": "Verilog/TODO.md",
          "url": "https://github.com/RetroCoreLabs/nd-120/commit/284caff64cd83e01e472fc807e402a234069b2f1"
        }
      ],
      "name": "Tang Nano 20K SMD variant",
      "notes": "Upstream's measured fast20 configuration with SMD and tape reader uses 89% logic and 45 of 46 BSRAM blocks, routes successfully, and boots SINTRAN from 21540& in 26 seconds. This is a verified board/build combination, not a minimum FPGA or memory requirement.",
      "platform": "Tang Nano 20K FPGA"
    },
    {
      "cpu_family": "ND-120",
      "evidence": [
        {
          "excerpt": "Winchester + tape reader (the default) ... routed; 20500& boots SINTRAN",
          "source": "Verilog/TODO.md",
          "url": "https://github.com/RetroCoreLabs/nd-120/commit/284caff64cd83e01e472fc807e402a234069b2f1"
        }
      ],
      "name": "Tang Nano 20K Winchester default",
      "notes": "Upstream reports the default Winchester plus tape-reader build at 87% logic and 45 of 46 BSRAM blocks, routed and booting SINTRAN from 20500&. SMD and Winchester together do not route on the tested Tang configuration.",
      "platform": "Tang Nano 20K FPGA"
    }
  ],
  "status": "Reconstructed ND-120 Verilog system with measured FPGA bring-up: tested Tang Nano 20K SMD-only and Winchester variants boot SINTRAN, while combined SMD+Winchester routing fails on Tang; Nexys and MEGA65 work continue.",
  "techniques": [
    "FPGA hardware bring-up",
    "place-and-route capacity testing",
    "storage-controller emulation"
  ]
}
```

Expected existing project SHA256: 9d31d943891d0237c77f8121500c0a95c187043c0679c890e0ae3e740495563e

### Identity (reviewed)

A reconstruction of the 1988 Norsk Data ND-120 3202D CPU board from original design documents, first represented in Logisim and now maintained as Verilog. Includes CPU/decode gate arrays, PAL translations, microcode, MMU and bus devices, simulation harnesses and FPGA board integrations. This is a hardware/firmware reconstruction distinct from the catalogued nd100x and nd500x software emulators.
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/README.md
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/Verilog/ND120_CORE.v
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/Verilog/ND120_TOP.v
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/BUILDING.md
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/Verilog/Makefile
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/LICENSE
- https://github.com/RetroCoreLabs/nd-120/commit/f640113d1db7262b78cc5c8e54dc461a311595a7
- https://github.com/RetroCoreLabs/nd-120/commit/284caff64cd83e01e472fc807e402a234069b2f1

### Classification (reviewed)

Actual board-independent core and CPU/peripheral instantiation inspected. README claims SINTRAN III boots on Tang Nano, Nexys and MiSTer; MEGA65 bitstreams are timing-clean but not yet run on real MEGA65. Treat hardware claims as upstream reports. Root MIT licence inspected. Original 1988 design scans, firmware and other inherited material require their own provenance assessment.
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/README.md
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/Verilog/ND120_CORE.v
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/Verilog/ND120_TOP.v
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/BUILDING.md
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/Verilog/Makefile
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/LICENSE
- https://github.com/RetroCoreLabs/nd-120/commit/f640113d1db7262b78cc5c8e54dc461a311595a7
- https://github.com/RetroCoreLabs/nd-120/commit/284caff64cd83e01e472fc807e402a234069b2f1

### Source CPU (reviewed)

Reconstructed architecture is ND-120 from original schematics, PAL equations and microcode.
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/README.md
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/Verilog/ND120_CORE.v
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/Verilog/ND120_TOP.v
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/BUILDING.md
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/Verilog/Makefile
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/LICENSE
- https://github.com/RetroCoreLabs/nd-120/commit/f640113d1db7262b78cc5c8e54dc461a311595a7
- https://github.com/RetroCoreLabs/nd-120/commit/284caff64cd83e01e472fc807e402a234069b2f1

### Target CPU (reviewed)

Logical CPU in generated FPGA bitstream remains ND-120. FPGA vendor silicon and simulator C++ host are not claimed as native instruction-set output.
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/README.md
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/Verilog/ND120_CORE.v
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/Verilog/ND120_TOP.v
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/BUILDING.md
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/Verilog/Makefile
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/LICENSE
- https://github.com/RetroCoreLabs/nd-120/commit/f640113d1db7262b78cc5c8e54dc461a311595a7
- https://github.com/RetroCoreLabs/nd-120/commit/284caff64cd83e01e472fc807e402a234069b2f1

### Build (reviewed)

Primary documentation records measured Tang fast20 results: SMD plus Winchester fails routing even after removing the tape reader, while SMD-only and default Winchester variants route and boot SINTRAN. These upstream hardware results support compilable/runnable for documented variants; the tracker did not synthesize or boot the core.
- https://github.com/RetroCoreLabs/nd-120/commit/284caff64cd83e01e472fc807e402a234069b2f1

### Runtime profiles (reviewed)

Two Tang Nano 20K runnable variants are captured from measured primary documentation: SMD plus tape reader boots SINTRAN from 21540& in 26 seconds, and Winchester plus tape reader boots from 20500&. The same source explicitly says combined SMD+Winchester does not route on Tang, so that combination is not represented as runnable. Limitations: These are verified FPGA board/build combinations, not proof of a lowest compatible FPGA, RAM minimum or universal timing margin.
- https://github.com/RetroCoreLabs/nd-120/commit/284caff64cd83e01e472fc807e402a234069b2f1

### AI (no-evidence-found)

Pinned full latest commit message and trailers plus available documentation reviewed. No explicit AI contribution attribution established; usage remains unknown.
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/README.md
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/Verilog/ND120_CORE.v
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/Verilog/ND120_TOP.v
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/BUILDING.md
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/Verilog/Makefile
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/LICENSE
- https://github.com/RetroCoreLabs/nd-120/commit/f640113d1db7262b78cc5c8e54dc461a311595a7
- https://github.com/RetroCoreLabs/nd-120/commit/284caff64cd83e01e472fc807e402a234069b2f1

### Relationships (reviewed)

Repository renamed from RonnyA/nd-120 to RetroCoreLabs/nd-120; both URLs screened. Distinct from ND100X and ND500X emulators.
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/README.md
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/Verilog/ND120_CORE.v
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/Verilog/ND120_TOP.v
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/BUILDING.md
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/Verilog/Makefile
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/LICENSE
- https://github.com/RetroCoreLabs/nd-120/commit/f640113d1db7262b78cc5c8e54dc461a311595a7
- https://github.com/RetroCoreLabs/nd-120/commit/284caff64cd83e01e472fc807e402a234069b2f1

## zapple-ii-bpm-prodos-softcard-environment

Project ID: zapple-ii-bpm-prodos-softcard-environment · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "zapple-ii-bpm-prodos-softcard-environment",
  "last_checked": "2026-10-26",
  "status": "Apple IIe 6502/Z80 SoftCard environment; current source fixes CP/M file truncation and directory search, caches terminal personality for faster output, and makes tab switching interrupt DIR/TYPE. Independent build/run not performed.",
  "techniques": [
    "terminal personality caching",
    "CP/M file-semantics regression",
    "virtualized directory search"
  ]
}
```

Expected existing project SHA256: 17d3f18d92802deb65c5481113164da503ae4b9a09c5b336922d1ead8232df49

### Identity (reviewed)

Native dual-CPU CP/M-compatible CCP/BDOS/BIOS environment translating Z80 program file operations into Apple II ProDOS services.
- https://github.com/bobbimanners/Zapple-II/blob/770b60f998a9f28ebd7e5ea6a99dc7d2b6e7ac03/README.md
- https://github.com/bobbimanners/Zapple-II/blob/770b60f998a9f28ebd7e5ea6a99dc7d2b6e7ac03/softcard65.asm
- https://github.com/bobbimanners/Zapple-II/commit/4f5f5c6ac0768c8e205be90740684679030e2345

### Classification (reviewed)

Substantial 6502 loader/terminal/ProDOS backend and Z80 BDOS/BIOS/CCP code with bank gateway and FCB/DMA transfers. Real SoftCard Z80 executes applications; this is not a CPU emulator. Newly updated default branch inspected at pinned commit. BSD-2-Clause for project code. Bundled assemblers have separate notices; CP/M programs including WordStar/Turbo Pascal/dBase are third-party content and not automatically relicensed by root BSD grant.
- https://github.com/bobbimanners/Zapple-II/blob/770b60f998a9f28ebd7e5ea6a99dc7d2b6e7ac03/README.md
- https://github.com/bobbimanners/Zapple-II/blob/770b60f998a9f28ebd7e5ea6a99dc7d2b6e7ac03/softcard65.asm
- https://github.com/bobbimanners/Zapple-II/commit/4f5f5c6ac0768c8e205be90740684679030e2345

### Source CPU (reviewed)

Original/inspected source architecture is 6502, Z80. This is not an inferred minimum runnable machine.
- https://github.com/bobbimanners/Zapple-II/blob/770b60f998a9f28ebd7e5ea6a99dc7d2b6e7ac03/README.md
- https://github.com/bobbimanners/Zapple-II/blob/770b60f998a9f28ebd7e5ea6a99dc7d2b6e7ac03/softcard65.asm
- https://github.com/bobbimanners/Zapple-II/commit/4f5f5c6ac0768c8e205be90740684679030e2345

### Target CPU (reviewed)

Inspected implementation/build establishes 6502, Z80 output architecture; a complete minimum runtime configuration was not independently verified.
- https://github.com/bobbimanners/Zapple-II/blob/770b60f998a9f28ebd7e5ea6a99dc7d2b6e7ac03/README.md
- https://github.com/bobbimanners/Zapple-II/blob/770b60f998a9f28ebd7e5ea6a99dc7d2b6e7ac03/softcard65.asm
- https://github.com/bobbimanners/Zapple-II/commit/4f5f5c6ac0768c8e205be90740684679030e2345

### Build (reviewed)

The reviewed assembly caches the active terminal personality instead of walking each tab context for every character, restores the Soroc default during tab initialization, and makes manual tab switches terminate DIR or TYPE. Adjacent commits repair CP/M close truncation and virtualize directory search. The tracker did not assemble or run the disk image.
- https://github.com/bobbimanners/Zapple-II/commit/4f5f5c6ac0768c8e205be90740684679030e2345

### Runtime profiles (no-evidence-found)

The reviewed terminal and CP/M changes do not state a minimum Apple IIe revision, RAM, SoftCard model, ROM or display requirement. No minimum is inferred from the 6502/Z80 code.
- https://github.com/bobbimanners/Zapple-II/commit/4f5f5c6ac0768c8e205be90740684679030e2345

### AI (no-evidence-found)

Unknown: bounded primary documentation, sampled implementation/build/licence files and up to three latest full commit messages contain no explicit AI-contribution attribution. Absence is not evidence of non-use.
- https://github.com/bobbimanners/Zapple-II/blob/770b60f998a9f28ebd7e5ea6a99dc7d2b6e7ac03/README.md
- https://github.com/bobbimanners/Zapple-II/blob/770b60f998a9f28ebd7e5ea6a99dc7d2b6e7ac03/softcard65.asm
- https://github.com/bobbimanners/Zapple-II/commit/4f5f5c6ac0768c8e205be90740684679030e2345

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/bobbimanners/Zapple-II/blob/770b60f998a9f28ebd7e5ea6a99dc7d2b6e7ac03/README.md
- https://github.com/bobbimanners/Zapple-II/blob/770b60f998a9f28ebd7e5ea6a99dc7d2b6e7ac03/softcard65.asm
- https://github.com/bobbimanners/Zapple-II/commit/4f5f5c6ac0768c8e205be90740684679030e2345

## m68k-reversing-toolkit-rmtew

Project ID: m68k-reversing-toolkit-rmtew · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "m68k-reversing-toolkit-rmtew",
  "last_checked": "2026-10-26",
  "status": "Starglider 2 semantic restoration preserves complete C/vasm byte equality for the mapped output and reduces unclassified bytes from 25,585 to 22,445; substantial function and field meaning remains unresolved.",
  "techniques": [
    "canonical memory-layout modeling",
    "relocation adapter qualification",
    "instruction-boundary timing probes",
    "cold-start differential analysis",
    "high-mask allocation qualification",
    "external source-package reproduction",
    "lease-lifetime instrumentation",
    "reversible range-backed semantic restoration",
    "binary-layout contract accounting"
  ]
}
```

Expected existing project SHA256: 9ee1bf5a1a2400e3bd03a882355dbbdc17c43441f1fa8d417694e2b07de2799b

### Identity (reviewed)

The repository and existing tracker record identify M68k Reversing Toolkit — generated Amiga analysis.
- https://github.com/rmtew/amiga-reversing/commit/9133be6a37cfa7caf5eb25b36dad6ada57a4e47f
- https://github.com/rmtew/amiga-reversing/commit/d15c2cf881aad2c80505dd58fa0e901115ed6eb4
- https://github.com/rmtew/amiga-reversing/commit/9ae1c5cbfe278a9200c8c95fee1ecd46c07ab16d

### Classification (reviewed)

The new Pandora work remains bounded reconstruction qualification: it proves one additional allocation owner and an exported source package without claiming a finished game reconstruction or universal relocated layout.
- https://github.com/rmtew/amiga-reversing/commit/9133be6a37cfa7caf5eb25b36dad6ada57a4e47f
- https://github.com/rmtew/amiga-reversing/commit/d15c2cf881aad2c80505dd58fa0e901115ed6eb4
- https://github.com/rmtew/amiga-reversing/commit/9ae1c5cbfe278a9200c8c95fee1ecd46c07ab16d

### Source CPU (reviewed)

The existing source-CPU decision remains unchanged; no architecture was inferred from platform or language.
- https://github.com/rmtew/amiga-reversing/commit/9133be6a37cfa7caf5eb25b36dad6ada57a4e47f
- https://github.com/rmtew/amiga-reversing/commit/d15c2cf881aad2c80505dd58fa0e901115ed6eb4
- https://github.com/rmtew/amiga-reversing/commit/9ae1c5cbfe278a9200c8c95fee1ecd46c07ab16d

### Target CPU (reviewed)

The toolkit renders and validates native Motorola 68000 assembly for tracked Amiga binaries.
- https://github.com/rmtew/amiga-reversing/blob/main/README.md
- https://github.com/rmtew/amiga-reversing/blob/main/docs/reproduction.md
- https://github.com/rmtew/amiga-reversing/commit/9133be6a37cfa7caf5eb25b36dad6ada57a4e47f
- https://github.com/rmtew/amiga-reversing/commit/d15c2cf881aad2c80505dd58fa0e901115ed6eb4
- https://github.com/rmtew/amiga-reversing/commit/9ae1c5cbfe278a9200c8c95fee1ecd46c07ab16d

### Build (needs-research)

The Starglider 2 restoration plan reports complete C/vasm byte equality preserved for the current mapped output while unclassified bytes fall from 25,585 to 22,445. The new observation set names disk UI strings, ratings storage, Taymar mission state and object-sound records. Substantial function and field meaning remains unresolved, so this is not a completed whole-game source reconstruction. Limitations: The tracker did not regenerate or execute the output; the primary source explicitly retains unresolved semantics. Next check: Continue classifying the remaining 22,445 bytes and qualify reconstructed behavior without converting bounded byte equality into a whole-game completeness claim.
- https://github.com/rmtew/amiga-reversing/commit/9ae1c5cbfe278a9200c8c95fee1ecd46c07ab16d

### Runtime profiles (needs-research)

The restored data and byte-equality checks do not establish a verified minimum Amiga CPU, RAM, chipset or ROM configuration. Next check: Establish explicit minimum runnable hardware only from primary runtime documentation or qualified physical/emulated hardware tests.
- https://github.com/rmtew/amiga-reversing/commit/9ae1c5cbfe278a9200c8c95fee1ecd46c07ab16d

### AI (reviewed)

Attribution independently verified on 2026-10-11: Explicit upstream commit attribution: Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>. https://github.com/rmtew/amiga-reversing/commit/0806d08b49d8d7f1aa6826c40385317bbb81154c This confirms the existing Claude-family label independently of instruction/configuration files.
- https://github.com/rmtew/amiga-reversing/commit/0806d08b49d8d7f1aa6826c40385317bbb81154c
- https://github.com/rmtew/amiga-reversing/commit/9133be6a37cfa7caf5eb25b36dad6ada57a4e47f
- https://github.com/rmtew/amiga-reversing/commit/d15c2cf881aad2c80505dd58fa0e901115ed6eb4
- https://github.com/rmtew/amiga-reversing/commit/9ae1c5cbfe278a9200c8c95fee1ecd46c07ab16d

### Relationships (needs-research)

The Starglider 2 restoration slice does not resolve the remaining predecessor, successor, fork or credited-source graph. Next check: Research remaining predecessor, successor, fork and credited-source relationships after the bounded restoration work stabilizes.
- https://github.com/rmtew/amiga-reversing/commit/9ae1c5cbfe278a9200c8c95fee1ecd46c07ab16d

## mega-man-x4-ps1-decompilation

Project ID: mega-man-x4-ps1-decompilation · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "build": {
    "byte_exact": true,
    "compilable": true,
    "playable": null,
    "runnable": null
  },
  "id": "mega-man-x4-ps1-decompilation",
  "last_checked": "2026-10-26",
  "status": "Matching Mega Man X4 decompilation: the same C source builds byte-matching US, JP and EU PlayStation executables, native Linux ports, and a non-matching Sega Saturn build. Runtime/playability not independently tested.",
  "techniques": [
    "cross-platform native porting",
    "SH-2 assembly integration",
    "scene-oracle regression comparison",
    "multi-region executable checksum verification"
  ]
}
```

Expected existing project SHA256: 692877cd75d8acbebcf188550744faaf4b64b55cb5422b4c2216380458751d7e

### Identity (reviewed)

US executable reconstruction with typed engine/gameplay C and original-file extraction requirements. ROM/executable matching and completeness not independently tested.
- https://github.com/sozud/mmx4
- https://github.com/sozud/mmx4/blob/f57f491299bd6206d16e2ef960e5782673b2b5b5/src/main/102FC.c
- https://github.com/sozud/mmx4/commit/807a01b1b8928811908a33367b964cf22f5ce799

### Classification (reviewed)

The rewritten README explicitly distinguishes byte-matching US/JP/EU PlayStation executables, native Linux ports and a non-matching Sega Saturn build. The Saturn output remains an RE-derived port rather than evidence that the original PlayStation program used SH-2.
- https://github.com/sozud/mmx4/commit/807a01b1b8928811908a33367b964cf22f5ce799

### Source CPU (reviewed)

Source architecture: MIPS.
- https://github.com/sozud/mmx4
- https://github.com/sozud/mmx4/blob/f57f491299bd6206d16e2ef960e5782673b2b5b5/src/main/102FC.c
- https://github.com/sozud/mmx4/commit/807a01b1b8928811908a33367b964cf22f5ce799

### Target CPU (reviewed)

The existing PlayStation output remains MIPS. The new Saturn-native manifest and assembly compile with gcc-sh-elf using -m2, explicitly establishing SH-2 as an additional output CPU.
- https://github.com/sozud/mmx4
- https://github.com/sozud/mmx4/blob/f57f491299bd6206d16e2ef960e5782673b2b5b5/src/main/102FC.c
- https://github.com/sozud/mmx4/commit/6a6b4555e775820b5f4e45c6f50bd5859223a453
- https://github.com/sozud/mmx4/commit/807a01b1b8928811908a33367b964cf22f5ce799

### Build (reviewed)

The primary README now explicitly states that the same C source builds byte-matching PlayStation executables for US, JP and EU, native Linux ports for US and JP, and a non-matching Saturn build. It documents the three retail executable names, GCC versions and checksum files. This supports byte_exact=true for the documented PlayStation outputs; the tracker did not build or run any variant. Limitations: Byte identity is scoped to the documented PlayStation executables and does not apply to Linux or Saturn runtime behavior.
- https://github.com/sozud/mmx4/commit/807a01b1b8928811908a33367b964cf22f5ce799

### Runtime profiles (no-evidence-found)

The new README documents toolchains and outputs but no minimum Linux host, PlayStation model, Saturn revision, RAM or OS profile. No hardware minimum is inferred.
- https://github.com/sozud/mmx4/commit/807a01b1b8928811908a33367b964cf22f5ce799

### AI (no-evidence-found)

The reviewed commit contains no development-AI attribution; absence in this bounded commit is not proof of non-use.
- https://github.com/sozud/mmx4
- https://github.com/sozud/mmx4/blob/f57f491299bd6206d16e2ef960e5782673b2b5b5/src/main/102FC.c
- https://github.com/sozud/mmx4/commit/6a6b4555e775820b5f4e45c6f50bd5859223a453
- https://github.com/sozud/mmx4/commit/807a01b1b8928811908a33367b964cf22f5ce799

### Relationships (reviewed)

Screened URL, title and prior decisions. GitHub fork flag is not treated as conclusive lineage evidence.
- https://github.com/sozud/mmx4
- https://github.com/sozud/mmx4/blob/f57f491299bd6206d16e2ef960e5782673b2b5b5/src/main/102FC.c
- https://github.com/sozud/mmx4/commit/807a01b1b8928811908a33367b964cf22f5ce799

## Research event notes

The CPU audit queue contained zero unresolved source/target CPU areas, so no speculative architecture work was created. This pass adds two measured ND-120 Tang Nano 20K runtime variants and preserves explicit unknowns elsewhere. No upstream software, FPGA core, game or emulator was built, launched or played by the tracker.
