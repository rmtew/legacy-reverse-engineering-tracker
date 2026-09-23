# Discovery Sources

These are **discovery nodes**, not merely individual tracked projects. Search their READMEs, credits, related repositories, predecessor/successor links, tools, forums and curated lists.

| Source | Reason |
|---|---|
| https://github.com/tetracorp | Multiple Amiga reverse-engineering projects plus external RE references |
| https://github.com/Pyrdacor | Amber ecosystem and links to earlier research |
| https://github.com/kermitfrog | Ambermoon binary-analysis work |
| https://github.com/slaapliedje/OpenUA | Active cross-68K reconstruction |
| https://github.com/HoraceAndTheSpider/Bloodwych-68k | Active Amiga 68K reconstruction/tooling |
| https://github.com/geogeo28/atari_reverse | Reusable Atari ST reconstruction framework; watch for new RE targets |
| https://github.com/sarnau | Atari ST software/protection analysis and CPC application reverse engineering |
| https://github.com/mwenge | Llamasource cluster, especially C64/ST |
| https://github.com/dpt | Spectrum Chase H.Q./Great Escape work |
| https://github.com/nzeemin/skoolkit-game-revs | Multi-title Spectrum reverse-engineering collection |
| https://github.com/mrcook | Spectrum disassemblies and preserved historical source material |
| https://github.com/skoolkid | Maintained SkoolKit disassemblies |
| https://github.com/pobtastic | Large current SkoolKit/ArcadeGeek Spectrum disassembly collection |
| https://www.pobtastic.co.uk/ | Human-maintained index mapping Pobtastic disassemblies to current repositories/rendered sites |
| https://github.com/Ritchie333 | Historical Spectrum disassemblies |
| https://github.com/tcdev42/re | Reassemblable reverse-engineering collection; Spectrum Alien 8, Knight Lore and Pentagram |
| https://github.com/lewster32/chaos-disassembly | Modern Chaos disassembly with explicit Claude Code assistance and historical references |
| https://skoolkit.ca/links/ | Curated Spectrum disassembly index and historical project graph |
| https://skoolkit.ca/disassemblies/ | Maintained complete Spectrum disassemblies and update dates |
| https://skoolkit.arcadegeek.co.uk/ | Large Spectrum disassembly archive |
| https://github.com/ricardoquesada | C64 disassembly trail; Commando and adjacent work |
| https://github.com/Piddewitt | C64 reverse-engineered game-source projects |
| C64 Mark | C64 disassembly trail |
| Simon Frankau | Speedball 2 and Head Over Heels cross-version analysis |
| Senior Dads | Atari ST binary-to-source reconstruction |
| https://github.com/Bread80 | CPC BASIC and firmware unassembly/reconstruction |
| https://github.com/BrettHallen/Amstrad-CPC | CPC project collection; Laserwarp includes byte-exact AI-assisted disassembly |
| https://github.com/moqucu/abadia-del-crimen-amstrad-cpc-disassembly | La Abadía del Crimen disassembly, asset extraction and reimplementation work |
| https://github.com/sarnau/hisoft-devpac-cpc | Byte-verified reverse engineering of HiSoft DEVPAC for CPC |
| https://colourclash.co.uk/cpc-analyser/ | CPC reverse-engineering tool/community node |
| https://www.cpcwiki.eu/ | CPC project/documentation graph and reverse-engineered adaptations |
| https://github.com/markmoxon | Major software-archaeology source: reconstructed Elite variants, Aviator, Revs, The Sentinel and Lander across BBC/Acorn/NES platforms |
| https://www.bbcelite.com/ | Mark Moxon's documentation hub linking reconstructed source projects, deep dives and related archaeology |
| https://github.com/ataribaby42 | Active cross-platform reconstruction/port work including Elite (ZX/ST/Amiga) and Hlípa (Atari ST/Amiga/PMD 85/ZX) |
| https://github.com/angree | Active Amiga 68k reimplementation/port source: OpenSWOS, AmiGTA, AmiSC, AmiXcom and ReMoM-derived work |
| https://github.com/jotd666 | Large arcade-to-Amiga reverse-engineering/transcode collection; many projects explicitly document Z80/6502/6809 reverse engineering and 68k conversion |

| https://github.com/tonioni/WinUAE | Core Amiga emulator/debugging ecosystem; adjacent tooling for compatibility research and reverse engineering |

| https://github.com/th-otto/tos3x | Atari TOS ROM/source reconstruction plus historical Alcyon toolchain and disassembly references |

| https://github.com/jonathanschilling/mac_rom | Bit-identical classic Macintosh ROM source reconstruction and documentation graph |

| https://github.com/BlitterStudio/dopus5 | Active continuation of the released Directory Opus 5 source; adjacent Amiga development ecosystem, not itself an RE reconstruction |

| https://github.com/MikeTheTechie/Level9-Public | Level 9 source archive plus l9dev recoding of Atari ST 68000 authoring tools into C |

| https://github.com/wepl/ReSource | Amiga reassembler/disassembler reconstructed and maintained from its own resourced output |

| https://github.com/CopperlineHQ/Copperline | Active cycle-driven Amiga emulator with reverse stepping, source debugging and automation tooling |

| https://github.com/TheGoodDoktor/8BitAnalysers | Multi-platform 8-bit analysis/annotation toolkit for Spectrum, C64 and CPC; assembler export and MCP-assisted analysis |

## Open discovery priorities

### Amiga / Atari ST

- Continue auditing `jotd666` repositories not yet promoted, especially candidates with missing or template/copied READMEs; require project-specific evidence before adding them.
- Resolve and assess AmberWorlds / Oliver Gantert, Slothsoft / Daniel Schulz and Nico Bendlin's Amber research as possible additional tracked projects.
- Continue mining Tetracorp external references and the Pyrdacor/Amber predecessor graph.
- Continue watching `geogeo28/atari_reverse` for newly added reverse-engineering targets.
- **BLACK ICE remains excluded** because its own documentation identifies it as an original game built from knowledge gained during RE work rather than an RE project itself.

### Commodore 64

- Continue mining Ricardo Quesada's C64 work beyond Commando.
- Continue mining C64 Mark and the wider Llamasource graph.
- Enumerate additional Piddewitt reverse-engineered game-source repositories.
- Treat recovered/original source collections cautiously: original source alone does not qualify unless substantial reverse engineering accompanies it.

### ZX Spectrum

- Continue graph-style discovery through SkoolKit links, author profiles and references from already tracked disassemblies.
- Prefer canonical/current project sources over archive mirrors, while keeping genuinely independent disassemblies as separate records.

### Amstrad CPC

- Continue discovery through CPC Analyser users, CPCWiki/CPCRulez references, firmware/protection research and GitHub project graphs.

### BBC / Acorn / consoles / newly represented platforms

- Mine Mark Moxon's linked archaeology graph beyond the projects already promoted, but keep original-source-only preservation distinct from binary/source reconstruction.
- Follow credited predecessors and related disassemblies around BBC Micro, BBC Master, Acorn Electron, Acorn Archimedes and NES projects.
- Treat newly represented platforms as first-class discovery targets rather than restricting future searches to the original five platform families.

### Tooling / emulation / adjacent infrastructure

- Track core emulators, debuggers, reassemblers, reconstructed toolchains and archival development systems when they are directly useful to software archaeology or reproducible legacy development.
- Keep ordinary open-source continuation/maintenance projects distinct from reverse-engineering records; they may remain discovery nodes without becoming catalogue records.
- Mine WinUAE, Copperline, ReSource, TOS toolchains and the Level 9 archive for referenced formats, tools, historical source drops and adjacent reconstruction projects.

## Search strategy

In addition to direct searches, mine:

- acknowledgements and credits
- linked tools and predecessor projects
- author/organisation repositories
- forks and successors
- documentation bibliographies
- retro-development forums
- curated RE/disassembly lists
- ports that cite reconstructed source

Graph-style discovery is intentional: many of the strongest finds were adjacent references rather than keyword-search hits.

## Promotion rule

A lead becomes a record in `data/projects.json` once there is a concrete source and enough evidence to say what is being reverse engineered or reconstructed. Core emulators, debuggers, reassemblers, reconstructed toolchains and archival development tooling may also qualify when directly useful to software archaeology or reproducible legacy development. Ordinary source releases or open-source maintenance alone normally remain discovery nodes rather than catalogue records. Unknown metadata is acceptable; invented metadata is not.
