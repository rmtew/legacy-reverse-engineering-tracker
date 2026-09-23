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
