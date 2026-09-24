# Search / Report Log

## 2026-09-23 — baseline

Scope expanded to **Amiga, Atari ST, ZX Spectrum, C64 and Amstrad CPC**.

State rules:
- An old/dormant project newly found by us counts as a discovery.
- Known projects are reported again only for substantive milestones.
- Routine commits and trivial progress changes are noise.
- Follow references outward from known authors/projects.

Latest expansion identified:
- Spectrum: Chase H.Q., The Great Escape, nzeemin SkoolKit collection, JETPAC, River Raid, Nether Earth, Alien, plus Paul Maddern/Ritchie Swann leads.
- C64: Iridis Alpha, Matrix, Ancipital, Spy Hunter, Commando and Attack of the Mutant Camels leads, Pitfall II.
- CPC: Head Over Heels and CPC BASIC 1.1.
- Existing discovery nodes include Tetracorp, Pyrdacor, Llamasource/mwenge, Sarnau and geogeo28/atari_reverse.

### Next search priorities

1. Resolve canonical sources for historical Spectrum/C64 leads.
2. Mine SkoolKit authors and credits outward.
3. Enumerate remaining Llamasource work.
4. Revisit Tetracorp external RE links.
5. Mine Pyrdacor/Amber credits and predecessor research.
6. Search CPC communities more deeply; CPC has the thinnest baseline.


## 2026-09-23 — reference-mining follow-up

Followed links/credits already present in known project data rather than relying primarily on generic search.

### Newly promoted into catalogue

- **The Lords of Midnight (ZX Spectrum/DOS)** — Michael Cook's parallel disassembly. Ghidra was used for the DOS binary and SkoolKit for Spectrum; surviving partial DOS source and Icemark data research help annotate/reconstruct the rest.
- **Head Over Heels (ZX Spectrum)** — Simon Frankau's work surfaced directly from the CPC Head Over Heels README, which credits it because the CPC port is closely related to the Spectrum version.
- **SkoolKit maintained disassemblies** — Skool Daze, Back to Skool, Contact Sam Cruise, Manic Miner, Jet Set Willy and Hungry Horace are explicit complete disassembly lines and should be tracked as projects, not merely as examples of the tool.
- **Piddewitt C64 cluster** — Lode Runner, Championship Lode Runner and The Castles of Dr. Creep. The first two explicitly target bit-for-bit-identical reconstructed assembler source.

### Strong discovery leads retained

SkoolKit's curated links substantially expands the Spectrum queue. Paul Maddern alone is linked to 180, Atic Atac, Battlezone, Batty, Booty, Jason's Gem, Jetpac, Lunar Jetman, PSSST, Rampage and Splitting Images. Michael Cook's collection additionally identifies Philip Anderson (Knight Tyme, Spellbound, Stormbringer, Through The Trap Door), BadBeard (Dynamite Dan 2), Lunysoft (Tir Na Nog, Dun Darach), tcdev (Alien8, Knight Lore), Simon Owen (Atic Atac) and multiple Chaos disassemblies.

The ArcadeGeek SkoolKit archive reported 29 Spectrum disassemblies during this pass and is now a discovery node.

### Method result

Cross-references continue to outperform generic searches. The CPC Head Over Heels project led directly to the Spectrum Head Over Heels work; Gridrunner's write-up exposes predecessor C64 disassemblies; and SkoolKit's own link/index pages expose a much larger historical Spectrum RE graph.

### Next priorities

1. Resolve Paul Maddern's GitHub projects individually and record canonical URLs/status.
2. Enumerate all 29 ArcadeGeek entries and deduplicate against known projects.
3. Inspect Piddewitt's C64 repositories and their documentation for further adjacent authors/projects.
4. Follow Simon Frankau beyond Speedball 2 and Head Over Heels.
5. Continue CPC-specific graph discovery, which remains much thinner than Spectrum/C64.


## 2026-09-23 — historical Spectrum + CPC resolution pass

Resolved the named Spectrum backlog into canonical/current sources and expanded CPC substantially.

### ZX Spectrum

- Enumerated the current Pobtastic/ArcadeGeek index and mapped its disassemblies to current GitHub repositories/subdirectories.
- Promoted all previously listed Paul Maddern/Pobtastic leads and additional current catalogue entries, while keeping genuinely independent disassemblies separate (for example Michael Cook's JETPAC vs Pobtastic's JETPAC).
- Resolved Ritchie Swann's Deathchase, Everyone's A Wally and Starquake repositories.
- Promoted Philip M. Anderson's four complete SkoolKit disassemblies from the preserved source in `mrcook/zx-spectrum-games`, with links to the rendered Wolfe-Lyon versions.
- Promoted BadBeard's Dynamite Dan II, Lunysoft's Tir Na Nog/Dun Darach, tcdev's Alien 8/Knight Lore/Pentagram and both the historical Guesser/szeliga and modern Lewis Lane Chaos projects.

### Amstrad CPC

Added new qualifying projects/sources:

- Bread80 CPC6128 firmware reconstruction
- Richard Lloyd CPC464 ROM disassembly
- Sarnau HiSoft DEVPAC reverse engineering
- La Abadía del Crimen preservation/disassembly/remake work
- The Abbey of Crime English patching project
- Into the Eagle's Nest CPC analysis
- Laserwarp full cassette-derived disassembly with byte-exact round trip and explicit Claude assistance
- Oh Mummy Resurrected
- Harrier Attack Reloaded

CPC discovery sources now include CPC Analyser, CPCWiki, Bread80, BrettHallen, moqucu and Sarnau's CPC work.

### Result

Structured project count increased from 69 to 121. `projects.md` now contains only open-ended discovery directions rather than the previously named Spectrum/CPC source-resolution queue.


## 2026-09-23 — BBC/Acorn expansion and new Amiga/Atari leads

User-supplied leads expanded the tracker beyond its original five platform families.

### Mark Moxon / bbcelite.com

Promoted binary-derived reconstructions for:

- Elite (BBC Micro disc)
- Elite Demonstration Disc (BBC Micro)
- Elite (Acorn Electron)
- Elite (BBC Master)
- Elite (NES)
- Aviator (BBC Micro)
- Revs (BBC Micro)
- The Sentinel (BBC Micro)
- Lander (Acorn Archimedes)

These repositories explicitly describe hand reconstruction from disassembly and provide build/reference verification. Mark Moxon's BBC Micro cassette Elite, 6502 Second Processor Elite, Commodore 64 Elite and Apple II Elite repositories are intentionally not promoted in this pass because their READMEs describe them as documented/preserved original source rather than source reconstructed from binaries. Elite-A is also left for later assessment because the surviving source is original source from a historically reverse-engineered derivative rather than a fresh binary reconstruction by the current repository.

### ataribaby42

Promoted:

- independent byte-exact ZX Spectrum Elite 128K-compatible reconstruction
- independently buildable Atari ST Elite source reconstruction from historical source material
- native Amiga Elite port derived from the corrected Atari source tree
- Hlípa Atari ST → Amiga reconstruction/port
- Hlípa PMD 85 → ZX Spectrum reconstruction/port

The Hlípa work adds PMD 85 as a source platform as well as another independent cross-platform reconstruction path.

### angree

Promoted:

- AmiGTA — clean-room/native Amiga reimplementation of Grand Theft Auto
- AmiSC — playable native Amiga StarCraft port using original game data; source is currently unpublished, so implementation provenance is noted as non-auditable
- AmiXcom — native classic-Amiga port of the OpenXcom reimplementation, explicitly developed with Claude Code
- Master of Magic ReMoM Amiga port — native port of a reconstructed C codebase

OpenSWOS was already tracked. Other angree repositories that are ordinary ports of open-source software or unrelated original projects were not promoted.

### Result

Structured project count increased from 121 to 139. Newly represented source/target families now include BBC Micro, BBC Master, Acorn Electron, Acorn Archimedes, NES and PMD 85. The public site description should remain platform-neutral so further additions do not require maintaining a hard-coded platform list.


## 2026-09-23 — jotd666 arcade-to-Amiga cluster

Audited the large `jotd666` GitHub profile and promoted 33 qualifying arcade-to-Amiga reverse-engineering/transcode projects with project-specific README evidence.

The promoted set includes Bagman, Ms. Pac-Man, Elevator Action, Galaga, Moon Patrol, Scramble, Atari Tetris, Pac-Man, Donkey Kong, Bad Dudes vs. DragonNinja, Phoenix, BurgerTime, Hyper Sports, Rally-X, Commando, Lock 'n' Chase, Karate Champ, Track & Field, Jail Break, Gyruss, Pengo, Dig Dug II, Ghosts 'n Goblins, Mappy, Pooyan, Super Bagman, Gravitar, U.S. Championship V'Ball, Roc'n Rope, Amidar, Double Dragon, Nibbler and Vulgus.

Common technique pattern: reverse engineer original arcade machine code (often Z80/6502/6809), transcode or adapt it to 68000 assembly, then replace arcade graphics/sound hardware access with native Amiga implementations. Some projects instead patch original 68000 arcade code directly (for example Bad Dudes).

Not yet promoted from this profile: repositories whose README was missing, minimal, or apparently copied from another project (including several names such as Xevious, Galaxian500, Jungle King, Jr. Pac-Man, Bosconian, Super Pac-Man, Dig Dug, Rolling Thunder, Tiger-Heli, Mr. Do, Berzerk and Marble Madness II). These remain discovery candidates for a project-specific evidence pass rather than being guessed into the database.

Structured project count increased from 139 to 172.


## 2026-09-23 — adjacent tooling and ROM/toolchain reconstruction pass

Reviewed seven user-supplied retro-development/tooling leads and broadened the catalogue carefully to include directly relevant reverse-engineering infrastructure.

Promoted six records: WinUAE as adjacent Amiga emulation/debugging tooling; th-otto/tos3x as Atari TOS ROM/source reconstruction; jonathanschilling/mac_rom as a five-ROM bit-identical Macintosh reconstruction; Level 9 l9dev as a C recoding of Atari ST 68000 authoring tools; wepl/ReSource as an Amiga reassembler/disassembler maintained from a self-resourced reconstruction; and Copperline as an active cycle-driven Amiga emulator/debugger with explicit AI-agent development guidance.

BlitterStudio/dopus5 was reviewed but not promoted as a catalogue record because its documentation identifies it as an active continuation of the 2012 released Directory Opus 5 source, not a reverse-engineering/source-reconstruction project. It remains a discovery node because it is strongly topical to the Amiga development ecosystem.

The broader promotion rule now explicitly admits core emulators, debuggers, reassemblers, reconstructed toolchains and archival development tooling when directly relevant to software archaeology, while ordinary source releases/maintenance remain excluded by default.

Structured project count increased from 172 to 178.


## 2026-09-23 — Copperline history backfill and 8-Bit Analysers

Investigated why Copperline showed its release but not its recent commit activity. The project was added on 23 September and the collector's first deep scan used the repository's first_seen timestamp as the lower bound, so commits from 19–20 September were outside the initial incremental fetch. Releases were populated separately from repository metadata, which is why v0.21.0 still appeared.

Fixed the collector so a repository's first branch scan backfills from the full retained 180-day activity window. Existing repositories remain incremental after their first successful scan.

Added TheGoodDoktor/8BitAnalysers as adjacent reverse-engineering tooling. Its README describes Spectrum, C64 and CPC analysis/annotation tools; recent history includes assembler export, MCP analysis tools, Copilot branches/commits and explicit Claude-related repository work.


## 2026-09-24 — hitchhikr Amiga disassemblies, analyser projects and activity fallback

Followed the Amiga/tooling graph and promoted eight buildable `hitchhikr` disassembly/reconstruction projects: **Alien Breed**, **Driller**, **Feud**, **Into The Eagle's Nest** (Amiga/Atari ST), **Spy vs Spy II**, **Spy vs Spy III**, **Thexder** and **Zool 2 AGA**.

Their common pattern is original disk/executable extraction, IRA/ReSource/Capstone-assisted disassembly where appropriate, vasm reconstruction and emulator validation. Byte exactness remains Unknown unless project-specific evidence supports it: Into The Eagle's Nest is explicitly non-identical because Atari ST-specific code was reconstructed, while Feud reports exact output for some versions but not others.

Audited `TheGoodDoktor/8BitAnalysers` and confirmed its tracker record is current through 23 September, including the current commit, weekly release, assembler export/MCP tooling and explicit Claude/Copilot evidence. Its neighboring `SpectrumAnalyserProjects` and `C64AnalyserProjects` repositories contain large title-specific analysis datasets, so both were added as discovery nodes for per-title review rather than promoting every directory without sufficient project-specific evidence.

Rechecked the Copperline discrepancy. The canonical project record already contains the 20 September main-branch commit `c79d6f46…`, which is newer than the 19 September `v0.21.0` release. The Activity view could nevertheless show the release while omitting that commit because it synthesized missing release events from project metadata but had no equivalent latest-commit fallback. Added a commit fallback so a known latest commit is shown even before the detailed activity collector has reached that repository.

Added a small pending-discovery merge queue used by the refresh workflow, allowing verified scheduled-discovery records to be merged into the canonical catalogue before GitHub metadata enrichment and validation.

Structured project count increased from 178 to 186.


## 2026-09-24 — HoraceAndTheSpider Amiga project audit

Audited the user-supplied HoraceAndTheSpider repository cluster and promoted four qualifying projects: **Cybernoid-68k**, **Legend-68k**, **Indy-Heat-WHD** and **Dalek-Attack-WHD**.

Cybernoid provides a lossless byte-identical GAME→project→GAME extraction/repack path plus decoded maps, graphics and tables; Legend reconstructs the PAC compression/resource format from Amiga resources and traced 68000 loader behaviour; Indy Heat contains active runtime-tested race/track/AI reverse engineering and editor tooling; Dalek Attack documents and patches character/resource structures through WHDLoad while decoding Pack-Ice assets.

**From-Lights-to-Flag** was reviewed but not promoted: its own documentation describes an original Amiga racer that uses findings from the separate Indy Heat reverse-engineering project as design reference and explicitly avoids transplanting original code/assets. It remains useful as a discovery node around the Indy Heat work.

HoraceAndTheSpider was added to recurring discovery sources for future profile/adjacent-repository passes.


## 2026-09-24 — PiST Atari ST development tooling

Promoted **PiST** as qualifying adjacent retro-development/software-archaeology tooling. PiST is a cross-platform Atari ST/STE 68000 IDE that integrates vasm/vlink with Hatari and provides source-line debugging, labelled disassembly, register/memory/hardware inspection, profiling, floppy-image and sprite/bitplane tooling, plus remote/MCP automation. The current README describes the write→assemble→run→debug loop as usable, and release v0.8.3 was published on 23 September 2026.

PiST was also added as a discovery node because its documentation links directly into the modern Atari development stack, including Hatari/hrdb, vasm/vlink, EmuTOS and legacy disk/graphics formats.


## 2026-09-24 — Atari Ghidra reverse-engineering tooling

Promoted **czietz/ghidraScripts_for_Atari** as qualifying Atari reverse-engineering tooling. The repository is explicitly intended to simplify analysis of Atari TOS code in Ghidra: it imports Atari executables with TEXT/DATA/BSS layout and relocations, imports TOS ROMs at their header-derived addresses, imports Atari a.out objects and symbols, and provides MiNTLib Function ID data plus TOS system-variable symbols for identifying otherwise unknown code.

The project remains maintained enough to support current tooling: its latest commit on 18 January 2026 adapts the scripts for Ghidra 12's runtime changes. The repository was also added as an Atari tooling discovery node.


## 2026-09-24 — amitools Amiga archaeology tooling

Promoted **cnvogelg/amitools** as qualifying Amiga software-archaeology and retro-development infrastructure. Its host-side toolset works directly with classic 68k AmigaOS binaries and storage formats: the Hunk library/hunktool loads executable, library and object-file hunks and relocations; romtool inspects, dissects and builds Kickstart ROM images; filesystem tooling handles ADF/HDF, RDB, OFS and FFS structures; and vamos executes Amiga CLI binaries through an API-level AmigaOS environment with detailed library-call, structure, code-fetch and memory tracing.

The current latest release is **v0.8.1** from 30 December 2025, with repository commits continuing through the same date. Added amitools as a recurring Amiga tooling/discovery node; its links to machine68k and historical Amiga development-tool execution are useful outward discovery paths.


## 2026-09-24 — Hatari, EmuTOS and modern Amiga debugger/toolchain cluster

Audited six user-supplied Atari/Amiga infrastructure repositories and promoted all six under the tracker’s tooling/reimplementation rules.

- **Hatari** — foundational ST/STE/TT/Falcon emulator with debugger, conditional breakpoints, symbol/disassembly support, CPU/DSP profiling and remote control.
- **EmuTOS** — free TOS-compatible OS/ROM implementation. Catalogued as reproducible Atari development/emulation infrastructure and a behavioral compatibility project, not as a reconstruction of proprietary Atari ROM binaries.
- **PUAE Debugger** — WinUAE-derived in-editor Amiga debugger/profiler with Hunk/ELF symbols, reverse execution, watchpoints, DMA/Copper/blitter analysis, memory reconstruction and MCP/DAP automation.
- **vAmiga Debugger** — integrated source debugger with fast-load, symbol-aware state/memory visualization, CPU/Copper disassembly and reverse stepping; recent profiler work includes explicit Claude-assisted commits.
- **m68k-tools** — reusable 68000 parser, formatter, cycle counter, linter/static-analysis and language-server suite.
- **BartmanAbyss vscode-amiga-debug** — self-contained GCC/GDB + WinUAE/FS-UAE Amiga development environment with source debugging, frame/DMA profiling, graphics debugging and source-correlated disassembly.

All six were also added as recurring discovery nodes because their dependency and attribution graphs connect to emulator cores, cross-compilers, debug formats, ROM replacements and other directly relevant software-archaeology tooling.


## 2026-09-24 — structured subject/tool classification

Reworked catalogue classification now that the tracker spans both reconstructed legacy software and substantial modern archaeology/development infrastructure.

Added four typed facets to every current project: **record class** (`subject`, `tooling`, `hybrid`), **target kinds**, **work kinds**, and **tool kinds**. The initial migration classifies 186 records as subjects, 12 as modern tooling and 2 as hybrids. Existing `types` and free-form tags remain intact for project-specific nuance rather than carrying the primary classification burden.

The Projects UI now exposes separate Class, Target kind, Work and Tool filters and renders prefixed badges such as **Target: Game**, **Work: Source reconstruction** and **Tool: Emulator**. Project details and Activity project headers show the same facets, and future material classification changes participate in catalogue-change activity.

The catalogue-state baseline was migrated together with the records so this one-time taxonomy introduction does not fabricate 200 metadata-update events. Site validation now enforces the controlled classification vocabulary and requires subject/hybrid records to have a target kind and tooling/hybrid records to have a tool kind.


## 2026-09-24 — compact classification presentation

Reduced the visual weight of the new structured classification badges after seeing them in the Activity feed. Repeated `Class:`, `Target:`, `Work:` and `Tool:` text was removed from badge bodies (the semantic prefix remains in the tooltip), saturated category colours were replaced with quiet neutral pills, and padding/gap/font sizes were reduced.

Activity now uses a deliberately compact classification summary. Subject records show the primary target plus at most two work kinds; tooling records show Tooling plus at most three high-value capabilities. Generic analysis/automation/toolchain capabilities are suppressed there when a more informative debugger/emulator/profiler/development-environment description is already present. The Projects table continues to expose the full classification, and the detail dialog retains the explicit labelled classification rows.


## 2026-09-24 — Firestaff, Starflight, CD32 disc archaeology and Llamasoft expansion

Audited the user-supplied Firestaff, Starflight, vs-sr-dev and mwenge discovery graph.

Promoted **Firestaff** as a clean-room/source-faithful Dungeon Master-family engine spanning DOS, Atari ST, Amiga, FM Towns, Macintosh, Saturn and PC Engine/TurboGrafx source families, and **Starflight Reverse** as a DOS/Forth reverse-engineering project that recovers threaded words, overlays and C representations from the original binaries.

Promoted **19 title-specific vs-sr-dev Amiga CD32 archaeology repositories**: Alfred Chicken, Banshee, Dragonstone, Fire & Ice, Gloom, Guardian, Gunship 2000, HeroQuest II, James Pond 2, Legends, Liberation: Captive II, Marvin's Marvellous Adventure, Microcosm, Myth, Power Drive, Prey, Superfrog, The Speris Legacy and Universe. These are documentation-first projects, but each performs substantive executable/disc/data-format reverse engineering with reproducible tools; the shared `cd32-platformnotes-doc` and `cd32-gamelist-doc` remain discovery nodes rather than catalogue subjects.

Expanded **mwenge/Llamasoft** beyond the already tracked Gridrunner, Matrix, Iridis Alpha and Ancipital records. Added Virtual Light Machine, Psychedelia/Colourspace, Hellgate, the C64/Atari 8-bit Attack of the Mutant Camels reconstructions, Voidrunner, Metagalactic Llamas, Batalyx, Sheep in Space, Revenge of the Mutant Camels, Hover Bovver, Mama Llama, Return of the Mutant Camels and an independent Uridium reconstruction. Tempest 2000 remains excluded as a catalogue subject because that repository primarily preserves/builds surviving original source; Psychedelia II is an original tribute/adaptation rather than a reconstruction.

Structured project count increased from 200 to **234**. The vs-sr-dev profile and its CD32 indexes were added as recurring discovery nodes for later auditing beyond CD32.


## 2026-09-24 — Apple II reconstruction graph and new C64/NES/Genesis static-recomp projects

Audited the user-supplied fschuhi profile plus Alien, Seven Cities of Gold, Solomon's Key, Shadowrun Defragged, Archon and BattleTech repositories.

Promoted all six named repositories: **Alien** (complete C64 disassembly plus faithful Python reimplementation and disk-analysis toolkit), **Seven Cities of Gold** (C64-to-Swift reconstruction with emulator-verified routines), **Solomon's Key** (byte-identical USA/Europe NES reconstruction), **Shadowrun Defragged** (Genesis bug-fix project backed by substantial ROM disassembly/analysis), **Archon** (relocatable C64 source-logic reconstruction), and **BattleTech: The Crescent Hawk's Inception** (native Windows static recompilation driven by a fixed 21,637-block analysis catalogue).

The fschuhi profile yielded three independent records: **a2-lode-runner** as a title-specific research/specification layer, **Robotron 2084** as an Apple II disassembly/research workbench, and **papple2** as purpose-built Apple II reverse-engineering/debugger infrastructure. The narrower **a2-hires-lab** remains a discovery aid under the profile rather than a separate catalogue record; generic/forked assembler/emulator repositories were not promoted merely for being useful dependencies.

Following a2-lode-runner's credited predecessor chain exposed **XekriRedmane** as a major Apple II reconstruction node. Promoted its byte-perfect **Lode Runner**, **Ultima I**, **Ali Baba and the Forty Thieves**, and **Drol** literate reconstructions. The profile is now a recurring discovery source for future Apple II audits.

AI evidence was recorded only where explicit: Seven Cities documents heavy Claude assistance; Solomon's Key carries Codex co-author trailers; Shadowrun Defragged explicitly documents GPT-5.6 Sol/Codex use; and the XekriRedmane reconstructions have explicit Claude project/commit evidence.

Catalogue count increased from 234 to **247**.


## 2026-09-24 — Starflight remastered successor

Audited **canadacow/starflight-reverse** against the already tracked **s-macke/starflight-reverse**. The new repository explicitly identifies the s-macke project as its background/origin, but it is not merely another copy of the recovery tree: it has become a playable remastered runtime that fully emulates Starflight's recovered Forth and assembly execution while adding a real-time Vulkan/rotoscoped/PBR presentation layer and switchable classic EGA/CGA output.

Promoted it as a separate **RE-derived reimplementation/remaster** record rather than merging the two projects. The s-macke record now notes this successor relationship, and canadacow's repository was added as a discovery node. The README explicitly describes the remaster as AI-generated, so AI usage is marked true while the tool name remains unknown rather than guessed.


## 2026-09-24 — curated display titles and subject names

Separated upstream project identity from catalogue presentation. Every current record now carries **upstream_name**, **display_title**, and **subjects**. The existing `title` field remains for compatibility/history, while Projects, Activity and RSS prefer `display_title`.

Opaque or awkward names now receive concise tracker labels that answer what the project actually is without relying on tags. Examples include **Firestaff — Dungeon Master / Chaos Strikes Back engine reconstruction**, **VS Code Amiga C/C++ debugger & profiler**, **amitools — Amiga binary, ROM & filesystem toolkit**, **PiST — Atari ST assembly IDE & debugger**, and **papple2 — Apple II reverse-engineering emulator/debugger**. Multi-subject projects such as Firestaff also carry explicit subject arrays for search.

The one-time migration updated the catalogue-state baseline in lockstep so it does not fabricate hundreds of project metadata events. Future changes to upstream/display names or subjects are material catalogue changes and will appear normally in Activity. Validation now requires non-empty upstream/display names and subjects for subject/hybrid records.


## 2026-09-24 — 0xC0DE6502, RetroRE and BBC Exile audit

Audited the 0xC0DE6502 profile, realdmx/retrore and chriskillpack/exile-beebasm.

Promoted five projects from **0xC0DE6502**: **Lode Runner — BBC Micro disassembly**, **Repton — Acorn Electron tape-protection disassembly**, **The Way of the Exploding Fist — Acorn Electron tape-loader disassembly**, **Electroniq — Acorn Electron browser emulator**, and **Electroniq — VS Code source-level Acorn Electron debugger**. The profile's Electron Elite repository was not duplicated because it is a fork of the already represented Mark Moxon Electron Elite reconstruction.

Promoted **Exile — BBC Micro disassembly** from chriskillpack. **RetroRE 6502** itself remains a discovery node rather than a project record because it is a curated index mixing original source and reverse-engineered projects. Its explicit Original/RE columns make it particularly useful for triage.

Following RetroRE immediately yielded **Choplifter — Apple II clean-room source reconstruction** by blondie7575. It is a full binary-led reconstruction whose game code is described as binary-identical, but the original custom floppy loader was intentionally replaced by a ProDOS loader, so the tracker does not mark the complete build byte-exact.

The RetroRE index exposes a much larger backlog of untracked full/partial 6502 reconstructions across Apple II, Atari 2600/8-bit, BBC Micro, C64 and NES; this has been added as an explicit discovery priority rather than bulk-promoting entries without primary-source verification.

Catalogue count increased from 248 to **255**.


## 2026-09-24 — public site renamed Retro Development Project Tracker

Renamed the public-facing site and RSS branding to **Retro Development Project Tracker** with the subtitle **Reverse engineering · reconstruction · preservation · homebrew · tooling**. The GitHub repository name and Pages URL remain unchanged to avoid unnecessary URL/repository churn.


## 2026-09-24 — additive facet filtering

Replaced the dropdown-heavy Projects and Activity filters with additive facet chips. Multiple choices inside one facet are ORed (for example Amiga + Atari ST + Amstrad CPC), while different facets combine to narrow results (for example those platforms + Game + Source reconstruction).

The internal `subject/tooling/hybrid` classification is no longer exposed as UI jargon. **Project type** presents **Retro software** and **Development tools**; hybrid records belong to both. Projects now expose additive Platform, Software type, Work and Development tool facets, with CPU/output language under More filters, while AI/Compiles/Playable/Byte exact use compact mutually exclusive Any/Yes/No/Unknown controls.

Activity was simplified to Search, Period, additive Activity type / Project type / Platform / Software type / Work / Development tool facets, and AI state. Dedicated project, author, branch and output-language filters were removed. The activity text search remains for project/subject and activity text, but no longer indexes authors or branch names.


## 2026-09-24 — CPU-family and verified runtime compatibility filtering

Moved **CPU** into the primary additive filters and normalized closely related stored variants into discovery families such as **6502 family**, **68000 family**, **x86**, Z80 and ARM. Platform filtering now considers both source and target platforms, and CPU discovery can consider source CPU, optional target CPU and verified runtime profiles, making same-architecture ports easier to find.

Added an optional **Runs on** compatibility section, deliberately separate from the broad CPU facet. It is driven only by verified `runtime_profiles` and supports minimum CPU, RAM budget and chipset compatibility. Selecting a 68020-class CPU can include a build whose documented minimum is 68000; selecting 68000 excludes a 68020-minimum build. The controls remain explicitly empty until requirements have been verified rather than inferring compatibility from source architecture.

The schema now supports optional `target_cpu` and `runtime_profiles`, validation enforces their shape, and catalogue activity treats changes to these fields as material. Activity filtering also gained the normalized CPU-family facet.


## 2026-09-24 — instant view switching

Removed unconditional Activity-feed reconstruction from Activity/Projects tab switching. The rendered Activity DOM is now retained and only marked dirty when Activity data/filter state changes; switching back to an unchanged Activity view is therefore a visibility toggle rather than a full regroup/sort/HTML rebuild. Off-screen activity-day layout is also deferred with CSS `content-visibility` to reduce the cost of showing long feeds.


## 2026-09-24 — persistent light/dark theme toggle

Added an explicit **Light/Dark** theme toggle in the site header. Light mode is now the default regardless of operating-system preference. The selected theme is restored before the stylesheet loads to avoid a theme flash and is persisted locally in the browser with `localStorage` key `retro-development-tracker.theme`. No other settings are persisted yet.


## 2026-09-24 — browser-default theme behaviour

Adjusted theme handling so an unset tracker preference follows the browser/OS `prefers-color-scheme` value. Nothing is written to storage merely by loading the site. Only an explicit user click on the Light/Dark toggle creates a persistent `localStorage` override; once present, that manual override takes precedence over browser defaults.


## 2026-09-24 — Zippy Race OCS Amiga fan conversion

Promoted **Zippy Race — OCS Amiga fan conversion** from `lantus/ZippyRace-OCS`. This is intentionally a broader-scope retro-development/homebrew record rather than a reverse-engineering record: the project's own README explicitly says **no reverse engineering or transcoding was performed** and that the game was written by hand to recreate the 1983 Irem arcade game.

The repository contains the complete C/m68k-assembly Amiga implementation, assets and build system. Its Makefile targets **68000** explicitly, while the README states that it runs at **50/60 fps on any Amiga with 1 MB**, so the record includes a verified OCS runtime profile of 68000 + 1 MB rather than inferring compatibility from the Amiga target alone. The `lantus` profile was added as a recurring Amiga/68k retro-development discovery node.

Catalogue count increased from 255 to **256**.


## 2026-09-25 — deeper cross-platform discovery pass

Read the canonical catalogue, discovery-source graph and current 180-day activity feed before searching, then expanded outward through RetroRE 6502, author profiles and primary project documentation. This pass followed the represented-platform graph rather than a fixed platform list and introduced **Atari 2600** as a first-class source platform where primary project evidence supported it.

Promoted **14 verified projects** across Atari 2600, Atari 8-bit, Commodore 64, BBC Micro and NES, together with two directly relevant BBC/6502 development tools. The additions include source reconstructions, disassemblies, binary/data analysis, a preservation-oriented emulator/debugger and a programmable tracing disassembler.

Hardware requirements remain evidence-only. **Fighter Pilot** is the only new record in this pass with a `runtime_profiles` entry because its README explicitly requires at least **48K** on named Atari 8-bit machines; no CPU minimum or other runnable requirement was inferred from platform or architecture alone.

Discovery sources were expanded for Dennis Debro, ZornsLemma, TobyLobster, nmikstas, cadaver and Crossroads 2, and the existing sarnau node now reflects the substantial Atari 8-bit archaeology cluster. Strong unpromoted follow-ups remain in the same graph, including additional sarnau Atari 8-bit analyses, Zelda/NES work and further BBC Micro disassemblies.

Catalogue count increased from 272 to **286**.


## 2026-09-25 — discovery automation landing verification

Verified the repository-side discovery landing path by pushing this commit to an `automation/discovery-*` branch and allowing `.github/workflows/land-discovery.yml` to fast-forward `main` only after confirming the branch is non-empty, zero commits behind, and based directly on the current `main`.


## 2026-09-25 — runtime-profile and status maintenance

Reviewed repository activity since the previous maintenance pass and rechecked current primary documentation for the materially changed projects.

Added evidence-backed runtime metadata for **Master of Magic — ReMoM Amiga port**: the native binary requires a 68020 or better, Kickstart/Workbench 3.1+, and 8 MB Fast RAM; AGA additionally requires 2 MB Chip RAM. AGA and 8-bit RTG are now separate runtime profiles so the RTG record does not invent an unstated Chip-RAM minimum.

Added verified runtime profiles for **Elite — native Amiga port (ataribaby42)**. The default OCS build is documented for MC68000, Kickstart 1.3, 512 KB Chip RAM plus 512 KB expansion RAM, while the explicit `cpu=68020` build is recorded separately without inferring a RAM minimum that the README does not state.

Refined **Firestaff — Dungeon Master / Chaos Strikes Back engine reconstruction** to reflect the project's own current status boundary: Dungeon Master 1 on PC DOS 3.4 is playable/source-locked, while the other named games remain verified bounded routes or active bring-up rather than being promoted to complete playability.

Updated **ZX Spectrum game disassemblies — reproducible SkoolKit archaeology** to include its new patching work: The Hobbit's optional fast-draw patch is applied on top of verified source and validated by rendering all 22 pictures and comparing whole memory afterwards.


## 2026-09-25 — persistent research indexes and queues

Converted the implicit research backlog into persistent machine-readable state.

`data/discovery-sources.json` now indexes every discovery node from `sources.md`, links already promoted projects, records review dates where the existing research log/catalogue establishes them, and turns the human Open discovery priorities into explicit stateful backlog tasks.

`data/project-audits.json` now contains one audit record for every catalogue project, separating factual unknowns from research-state unknowns across identity, classification, source/target CPU, build evidence, runtime profiles, AI evidence and project relationships. Missing evidence is still not treated as false; `needs-research`, `not-applicable` and `no-evidence-found` are distinct states.

`data/research-activity.json` provides append-only research history and is seeded from the research-oriented entries already present in this log. Validation now enforces source/task references and exact project-audit coverage. The pending-project merge tool creates an unreviewed audit placeholder for every newly added project so the index cannot silently fall behind the catalogue.


## 2026-09-25 — analyser queues and RetroRE batch

Continued preemptive discovery from the persistent research queues rather than a broad search.

Completed the title-level audit of **TheGoodDoktor/C64AnalyserProjects**, promoting the nine remaining per-game analysis states after verifying their dedicated annotation databases, saved analysis/emulator state and configuration. The C64 analyser backlog task is now complete.

Advanced **TheGoodDoktor/SpectrumAnalyserProjects** with ten especially substantive title records: Batman, Bobby Bearing, Cybernoid, Dan Dare, Everyone's A Wally, Exolon, Jack the Nipper II, Manic Miner, Ranarama and Starquake. These were selected for deep per-title analysis data and, where present, exported Z80/Skool source, Lua viewers/exporters, maps, flow graphs and decoded graphics. The broader Spectrum analyser queue remains in progress.

Advanced the **RetroRE 6502** backlog with primary-source verification of The Legend of Zelda, Final Fantasy, Contra, Balloon Fight, Jackal, Pharaoh's Curse, Rambo and Planetoid. Following Contra's own project graph also yielded **Super C**. Byte-exact status was recorded only where the primary project documentation explicitly states matching reconstruction output.

The discovery index's task-to-source links were also normalized. The initial migration's keyword-derived links were too broad; active backlog tasks now point at the actual source nodes that should drive future queue selection.

This pass adds **28 projects**, taking the catalogue from 293 to **321**.


## 2026-09-25 — Spectrum, RetroRE, Ricardo and jotd queue pass

Continued preemptive discovery from four explicit research queues.

Promoted ten more substantial **SpectrumAnalyserProjects** title states: Cobra, Auf Wiedersehen Monty, Elite, Livingstone I Presume, Thrust, Firelord, Zub, Spellbound 128K, Chase H.Q. and Cybernoid II. The pass prioritised large per-title annotation databases and, where present, custom Lua analysis/viewer tooling. The Spectrum analyser queue remains in progress.

Advanced **RetroRE 6502** with two primary-source NES reconstructions: **Super Mario Bros. 3**, whose NESASM source explicitly rebuilds the US PRG1 ROM byte-for-byte, and **Tecmo Super Bowl**, whose repository describes an exhaustive fully labelled/commented reverse engineering and byte-for-byte rebuild.

Completed the **Ricardo Quesada C64** source audit. Added **Le Mans** as a fully disassembled/patched C64 reconstruction, **Regenerator 2000** as a modern Commodore 6502 disassembler/debugger/MCP reverse-engineering workbench, and **VChar64** as substantive C64/128 asset-development tooling. Other inspected repositories were original homebrew, small misc/demo collections or mirrors; **UNP64** explicitly identifies itself as an official mirror and was not duplicated as a separate project.

Advanced the **jotd666** audit with **Xevious** and **Galaxian**, both backed by project-specific documentation explicitly describing Z80 reverse engineering and 68000 transcoding. Several other candidate repositories currently contain copied or mismatched READMEs for other games, so they remain unpromoted pending project-specific evidence rather than inheriting claims from those templates.

This pass adds **17 projects**, taking the catalogue from 321 to **338**.
