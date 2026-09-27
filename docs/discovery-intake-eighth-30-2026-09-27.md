# Eighth discovery intake: next 30 leads

Reviewed the fixed next 30 ranked URLs on 2026-09-27. Existing project matches were checked locally; accessible candidates received repository metadata, directory, README and selective source/lineage inspection. Build/run claims are attributed to upstream documentation.

**Result:** 14 projects from nine candidate URLs, seven retained reference sources, nine exclusions, two already tracked duplicates and three deferred unavailable URLs. Twenty-seven URLs leave the queue; the three 404s remain deferred with follow-up tasks.

| Rank | Candidate | Outcome | Evidence and scope |
| ---: | --- | --- | --- |
| 1–5 | fschuhi/pdf-annotations, rob-burbea-expert, scurry, stencil, yt-transcript-summarizer | Excluded | PDF/Obsidian, dharma RAG, macOS office automation, template rendering and YouTube summaries; no retro analysis or tooling. |
| 6 | ataribaby42/hlipa-source-code-amiga | Duplicate | Exact existing Hlípa native Amiga port; README confirms the same Atari ST-derived work. |
| 7 | sehugg/awesome-8bitgamedev | Source | Curated platform and tooling links for screening future leads. |
| 8 | fschuhi/a2-lode-runner | Duplicate | Exact existing Apple II 6502 Lode Runner research. |
| 9 | horsicq/Detect-It-Easy | Excluded | General malware and PE file inspection; inspected evidence does not establish a focused historical-platform tool. |
| 10 | radek-sprta/awesome-game-remakes | Source | Index of remake leads, not itself a reconstruction. |
| 11 | bobeff/programming-math-science | Excluded | Broad education links. |
| 12 | GerbilSoft/rom-properties | Project | ROM and CBM media metadata parser; inspected CBMCart and CBMDOS source, not a reconstructed game. |
| 13 | mamedev/mame | Source | Broad emulator and hardware-behavior reference for platform-specific audits. |
| 14 | markmoxon/elite-source-code-library | Source | Buildable shared source for already tracked Elite versions. BBC cassette and Apple II version links screened as two new leads for follow-up; no second record for duplicated generated version code. |
| 15 | rejunity/tt05-psg-ay8913 | Source | Hardware AY-3-8913 recreation drawing on reverse-engineered chip diagrams; useful chip-behavior reference, beyond software scope. |
| 16 | sehugg/8bitworkshop | Project | In-browser multi-platform toolchains, emulators and source-level debugging including C64/CPC. |
| 17 | SnowflakePowered/opengood | Source | Historical ROM identification DATs including CPC; README says they were assembled from public data, not extracted from GoodTools executables. |
| 18 | tzubertowski/TreeFrogUI | Excluded | Frontend for modern MIPS emulation handhelds. |
| 19–20 | ArqueologiaDigital/another-world-archive; another-world-hacks | Deferred | Both now return GitHub API 404, while the live sibling reconstruction README still links them. No absence or equivalence claim without accessible artifacts. |
| 21 | GINNOV/littlethings/tree/master/Amiga/Tools | Six projects | ADFinder ADF/HDF manager, AmigaROMExplorer firmware checksum catalog, AuDeluxe module player, IFFViewer Quick Look extensions, PixDeluxe IFF manager, and send2adf OFS image builder. Each has its own project directory and distinct output; decorative amigaLoginScreen excluded from promotion. The sibling aMiLa/AmigaPlayground link is a new lead for a later pass. |
| 22 | pbakota/amigadx | Project | Total Commander plugin for ADF/HDF read/write, ADZ/DMS reading, with old MinGW64 source. |
| 23 | pepijn-devries/adfExplorer | Project | R library for ADF file analysis and transfer; explicitly excludes extended flux/MFM images. |
| 24 | tamus-cyber/pyadf | Deferred | GitHub API 404 and scoped search found no current repository; needs accessible source before classification. |
| 25 | vschwaberow/adflib | Project | Pure Rust ADF parser distinct from tracked C ADFlib, with inspected DMS/Hunk code; planned write support unverified. |
| 26 | ashang/unar | Excluded | Maintenance mirror of upstream archive unpacker and libxad; no distinct retro work demonstrated. |
| 27 | bisqwit/password_codecs | Project | NES game-specific password encoders/decoders and analysis, with credited prior research. |
| 28 | hukkax/Propulse | Project | MOD-compatible editor and player; README credits 8bitbubsy's disassembly-derived ProTracker playback predecessor. |
| 29 | libretro/hatari | Project | Distinct libretro core adaptation of tracked upstream Hatari: inspected src/retro has main, audio, disk control, VFS, video and timing integration. |
| 30 | mbtaylor1982/ReSDMAC | Source | Reverse-engineered Amiga 3000 SDMAC hardware replacement, retained as a hardware-interface reference outside software scope. |

## Programmatic observations

| Finding | Applied or next procedure | Limit |
| --- | --- | --- |
| A queued GitHub tree URL led to six distinct products; root-only preflight and source revisits missed its directory. | Preflight now inventories a tree directory and its README in at most two branch-pinned requests. Scheduled source intake lists its direct child directories and linked repositories in the same bounded pass. | A directory name alone cannot establish an independent project. |
| Multiple formats and parsers overlap ADFlib while their implementations and user-facing outputs differ. | Inspect actual parsers, credit the dependency/predecessor and use directory-specific project URLs; group GitHub metadata probing by repository while retaining per-directory activity. | Shared input formats do not prove a fork or equivalent behavior. |
| A shared Elite source library generates already tracked per-version repos. | Screen README links locally and queue missing versions; retain the library as the source-of-truth reference. | Whether a version has distinct research still needs individual review. |
| Three URLs became inaccessible after collection. | Record deferred decisions and specific lookup tasks; retain queue entries at reduced priority, without classifying absent source. | A 404 does not establish deletion, relocation, or duplicate lineage. |
| AmigaROMExplorer combines deterministic checksum lookup with an optional Ollama research path. | Identify ROMs from local manifests/checksums before requesting LLM summaries; keep model output separately attributed. | LLM prose cannot establish ROM identity or compatibility. |

The 14 projects include CPU, build, AI and relationship audits. None was independently built or exercised in this review.
