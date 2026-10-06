# Focused Amiga/C64 discovery, fourth pass: 44 approved projects

Added 44 approved source-reviewed projects, taking the catalogue from 1,621 to 1,665. Nine holds, twelve lineage/component references and two out-of-scope exclusions remain non-promoted.

## Scope and verification

Exactly the approved 44 roots were re-screened against main d654a0c46bb2cf237e81a2d98673cf248c3ed3ad, its catalogue/source/decision indexes and the 1,861-root normalized prior-review union. The batch adds 352 meaningful evidence-backed audit areas covering identity, classification, source CPU, target CPU, build, runtime profiles, AI and relationships. Source/overall audit states remain partial.

No candidate was built, run, emulated, played or byte-compared. All four build flags remain unknown. Recipes, bundled binaries and upstream claims do not establish independently successful outputs. Source, native target and development/data-format roles are separated; source CPU is not inferred from a game inspiration or a platform keyword. Modern host languages do not establish host ISAs. Source visibility is not unrestricted licensing, and original games, music, fonts, graphics, firmware and dependencies retain separate rights concerns.

Highlights include source-derived Stunt Car Racer Remake; original BlitzWays and Notegame; native Amiga TuxPuck and Airstrike ports; Galaga, Galaxian, Megamania, OYUP!, Mario’s Cement Factory and other C64 games; ClassAction source restoration, LZXa, Poseidon USB, ZZ9000 drivers and authentic Amiga/C64 format-development tools.

ClassAction reconstructs missing support code from the old object API but still uses resource objects. LZXa’s clean-room description remains an upstream assertion; its decoder acknowledges UnLZX logic, and compatibility/no-op limitations are retained. BlitzWays has restrictive rights and an asset filename mismatch. The Pouet helper disables upstream TLS checking and exposes an unauthenticated HTTP relay; it is not represented as safe to deploy. Poseidon’s author still requests real OS3 runtime validation. Native C64 source and checked-in PRGs are not represented as independent successful game tests.

ZZ9000 driver code fixes explicitly credit Codex review; this supports that role only, not broad AI generation. Claude evidence is retained on the deferred sid-fixer source but does not create an accepted project. No tool is inferred from a provider email, a model-only name, UI cursor wording or the separate Amiga Codex lint tool. Existing PR4 attribution code and labels remain untouched.

## Bounded discovery coverage

- 24 repository-search attempts: 23 fresh exact query/page pairs and 1 disclosed repeat.
- 4 failed searches are recorded as errors rather than evidence of absence; no requested repository-search page cap was reached.
- 394 result occurrences, 414 screened roots including direct backlog/successor/lineage leads, and 48 previously reviewed/indexed roots excluded.
- 23 primary-fetch/parameter failures retain recovery or limitation notes; one additional bounded exact-name commit search.
- Metadata-only hits were not silently counted as primary source reviews. This is a bounded pass, not ecosystem exhaustion.

### Exact repository-search ledger

- `user:AmigaSourcePreservation fork:false`: page 1, limit 100, 0 results (failed; not absence evidence).
- `user:meistrale amiga fork:false`: page 1, limit 100, 0 results (failed; not absence evidence).
- `user:phx amiga fork:false`: page 1, limit 100, 0 results.
- `user:ptitSeb stuntcarremake`: page 1, limit 100, 1 results.
- `user:ozzyboshi fork:false`: page 1, limit 100, 70 results.
- `user:mequa amiga fork:false`: page 1, limit 100, 0 results (failed; not absence evidence).
- `amiga blitzbasic game fork:false`: page 1, limit 100, 2 results.
- `amiga AMOS game fork:false`: page 1, limit 100, 3 results.
- `user:GraemeCowell fork:false`: page 1, limit 100, 0 results (failed; not absence evidence).
- `user:stefanhaustein amiga fork:false`: page 1, limit 100, 0 results.
- `user:weiju amiga fork:false`: page 1, limit 100, 10 results.
- `user:billynewport fork:false`: page 1, limit 100, 14 results.
- `amiga "source code" "game" fork:false stars:0`: page 1, limit 100, 1 results.
- `amiga "Blitz Basic" fork:false`: page 1, limit 100, 17 results.
- `user:colinvella fork:false`: page 1, limit 100, 8 results.
- `user:meveric amiga fork:false`: page 1, limit 100, 0 results.
- `user:rolandshacks fork:false`: page 1, limit 100, 18 results (prior query/page repeated).
- `user:cadaver fork:false`: page 1, limit 100, 14 results.
- `user:hayesmaker fork:false`: page 1, limit 100, 40 results.
- `user:1888games fork:false`: page 1, limit 100, 65 results.
- `user:alby69 fork:false`: page 1, limit 100, 35 results.
- `user:OldSkoolCoder fork:false`: page 1, limit 100, 37 results.
- `user:ricardoquesada c64 fork:false`: page 1, limit 100, 14 results.
- `user:Esshahn fork:false`: page 1, limit 100, 45 results.

## Approved projects

### Stunt Car Racer Remake — source-derived portable reconstruction

[Repository](https://github.com/ptitSeb/stuntcarremake)

- Source platforms: Amiga
- Target platforms: Windows, Linux, Web
- Source CPU: m68k
- Target CPU: ARM
- Source material/language: m68k assembly, original Amiga track and sound data
- Maintained language: C++
- Classification: subject; game, source-reconstruction, reverse-engineering-derived-port
- Build flags: all unknown (compilable, runnable, playable and byte_exact).
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** C++ reconstruction of Amiga Stunt Car Racer gameplay, extended from the SourceForge Windows conversion to Linux, ARM Linux handhelds and Emscripten; the browser build is one target of this project. Canonical root https://github.com/ptitSeb/stuntcarremake was screened against the fresh 1621-project baseline and 1861-root union including prior sources, decisions and reviews. Source snapshot: commit 9f0f8e6e0aca08b715a0f9291ba21c3dc3cab39d; actual root Git tree 4755d835922532855ab21f4b392d3187fc958352 verified through https://api.github.com/repos/ptitSeb/stuntcarremake/git/commits/9f0f8e6e0aca08b715a0f9291ba21c3dc3cab39d.

Evidence: [source 1](https://github.com/ptitSeb/stuntcarremake/blob/9f0f8e6e0aca08b715a0f9291ba21c3dc3cab39d/README.md) · [source 2](https://github.com/ptitSeb/stuntcarremake/blob/9f0f8e6e0aca08b715a0f9291ba21c3dc3cab39d/Car_Behaviour.cpp) · [source 3](https://github.com/ptitSeb/stuntcarremake/blob/9f0f8e6e0aca08b715a0f9291ba21c3dc3cab39d/StuntCarRacer.cpp) · [source 4](https://github.com/ptitSeb/stuntcarremake/blob/9f0f8e6e0aca08b715a0f9291ba21c3dc3cab39d/dx_linux.cpp) · [source 5](https://github.com/ptitSeb/stuntcarremake/blob/9f0f8e6e0aca08b715a0f9291ba21c3dc3cab39d/Reference%20only/StuntCarRacer.s) · [source 6](https://github.com/ptitSeb/stuntcarremake) · [source 7](https://api.github.com/repos/ptitSeb/stuntcarremake/git/commits/9f0f8e6e0aca08b715a0f9291ba21c3dc3cab39d)

**Classification (reviewed):** Classified as subject with source-derived Amiga game reconstruction and native portability layer. Methods: source-reconstruction, reverse-engineering-derived-port. The README identifies the SourceForge Stunt Car Racer Remake as its original project. That primary upstream explicitly says its partial Windows conversion uses Amiga track data, sound samples and car-physics algorithms.

Evidence: [source 1](https://github.com/ptitSeb/stuntcarremake/blob/9f0f8e6e0aca08b715a0f9291ba21c3dc3cab39d/README.md) · [source 2](https://github.com/ptitSeb/stuntcarremake/blob/9f0f8e6e0aca08b715a0f9291ba21c3dc3cab39d/Car_Behaviour.cpp) · [source 3](https://github.com/ptitSeb/stuntcarremake/blob/9f0f8e6e0aca08b715a0f9291ba21c3dc3cab39d/StuntCarRacer.cpp) · [source 4](https://github.com/ptitSeb/stuntcarremake/blob/9f0f8e6e0aca08b715a0f9291ba21c3dc3cab39d/dx_linux.cpp) · [source 5](https://github.com/ptitSeb/stuntcarremake/blob/9f0f8e6e0aca08b715a0f9291ba21c3dc3cab39d/Reference%20only/StuntCarRacer.s) · [source 6](https://github.com/ptitSeb/stuntcarremake/blob/9f0f8e6e0aca08b715a0f9291ba21c3dc3cab39d/Makefile)

**Source architecture (reviewed):** Reference only/StuntCarRacer.s was directly inspected during publication preparation at the same recorded commit. Its native move.l/moveq/jsr instructions, d0/a6 registers, Amiga library vectors and custom-chip accesses ground source_cpu=m68k in supplied original-platform code. It is a reference listing, not proof of byte-exact recovery or an unmodified original binary.

Evidence: [source 1](https://github.com/ptitSeb/stuntcarremake/blob/9f0f8e6e0aca08b715a0f9291ba21c3dc3cab39d/README.md) · [source 2](https://github.com/ptitSeb/stuntcarremake/blob/9f0f8e6e0aca08b715a0f9291ba21c3dc3cab39d/Car_Behaviour.cpp) · [source 3](https://github.com/ptitSeb/stuntcarremake/blob/9f0f8e6e0aca08b715a0f9291ba21c3dc3cab39d/StuntCarRacer.cpp) · [source 4](https://github.com/ptitSeb/stuntcarremake/blob/9f0f8e6e0aca08b715a0f9291ba21c3dc3cab39d/dx_linux.cpp) · [source 5](https://github.com/ptitSeb/stuntcarremake/blob/9f0f8e6e0aca08b715a0f9291ba21c3dc3cab39d/Reference%20only/StuntCarRacer.s) · [source 6](https://github.com/ptitSeb/stuntcarremake/blob/9f0f8e6e0aca08b715a0f9291ba21c3dc3cab39d/Makefile)

**Target architecture (reviewed):** Makefile directly targets ARM Cortex-A8/A9/A15 and other Cortex variants through -mcpu and ARM flags, supporting ARM as an explicit target. Windows/Linux/browser output does not establish additional host ISAs; no x86/wasm target_cpu is inferred merely from those runtimes.

Evidence: [source 1](https://github.com/ptitSeb/stuntcarremake/blob/9f0f8e6e0aca08b715a0f9291ba21c3dc3cab39d/Makefile) · [source 2](https://github.com/ptitSeb/stuntcarremake/blob/9f0f8e6e0aca08b715a0f9291ba21c3dc3cab39d/README.md) · [source 3](https://github.com/ptitSeb/stuntcarremake/blob/9f0f8e6e0aca08b715a0f9291ba21c3dc3cab39d/Car_Behaviour.cpp) · [source 4](https://github.com/ptitSeb/stuntcarremake/blob/9f0f8e6e0aca08b715a0f9291ba21c3dc3cab39d/StuntCarRacer.cpp) · [source 5](https://github.com/ptitSeb/stuntcarremake/blob/9f0f8e6e0aca08b715a0f9291ba21c3dc3cab39d/dx_linux.cpp) · [source 6](https://github.com/ptitSeb/stuntcarremake/blob/9f0f8e6e0aca08b715a0f9291ba21c3dc3cab39d/Reference%20only/StuntCarRacer.s)

**Build and verification (reviewed):** Makefile supplies native C++ SDL1/SDL2, OpenAL, OpenGL/gl4es and Emscripten routes. Windows Visual Studio projects and DirectX SDK heritage are documented. The reference assembly is not compiled by this host make recipe. Upstream calls its original conversion partial; no build or gameplay/equivalence test was run. All four build flags are null. No independent successful build, execution, gameplay or byte-exact result is claimed.

Evidence: [source 1](https://github.com/ptitSeb/stuntcarremake/blob/9f0f8e6e0aca08b715a0f9291ba21c3dc3cab39d/Makefile) · [source 2](https://github.com/ptitSeb/stuntcarremake/blob/9f0f8e6e0aca08b715a0f9291ba21c3dc3cab39d/README.md)

**Runtime requirements (no-evidence-found):** Selected primary material does not establish a sufficiently explicit output-specific hardware minimum. No profile is populated: build flags, guest models, development machines and historical test anecdotes are not extrapolated into verified CPU/RAM/chipset/OS minima.

Evidence: [source 1](https://github.com/ptitSeb/stuntcarremake/blob/9f0f8e6e0aca08b715a0f9291ba21c3dc3cab39d/README.md) · [source 2](https://github.com/ptitSeb/stuntcarremake/blob/9f0f8e6e0aca08b715a0f9291ba21c3dc3cab39d/Car_Behaviour.cpp) · [source 3](https://github.com/ptitSeb/stuntcarremake/blob/9f0f8e6e0aca08b715a0f9291ba21c3dc3cab39d/StuntCarRacer.cpp) · [source 4](https://github.com/ptitSeb/stuntcarremake/blob/9f0f8e6e0aca08b715a0f9291ba21c3dc3cab39d/dx_linux.cpp) · [source 5](https://github.com/ptitSeb/stuntcarremake/blob/9f0f8e6e0aca08b715a0f9291ba21c3dc3cab39d/Reference%20only/StuntCarRacer.s) · [source 6](https://github.com/ptitSeb/stuntcarremake/blob/9f0f8e6e0aca08b715a0f9291ba21c3dc3cab39d/Makefile)

**AI attribution (no-evidence-found):** No explicit generative-AI attribution found in the selected README, source, build, license evidence or 30 recent commit messages. This bounded review is not proof of non-use. Generic provider domains and gameplay AI are not tool attribution. Generic provider/model mentions, ordinary gameplay AI and future hypothetical uses are not named-tool attribution.

Evidence: [source 1](https://github.com/ptitSeb/stuntcarremake/blob/9f0f8e6e0aca08b715a0f9291ba21c3dc3cab39d/README.md) · [source 2](https://github.com/ptitSeb/stuntcarremake/blob/9f0f8e6e0aca08b715a0f9291ba21c3dc3cab39d/Car_Behaviour.cpp) · [source 3](https://github.com/ptitSeb/stuntcarremake/blob/9f0f8e6e0aca08b715a0f9291ba21c3dc3cab39d/StuntCarRacer.cpp) · [source 4](https://github.com/ptitSeb/stuntcarremake/blob/9f0f8e6e0aca08b715a0f9291ba21c3dc3cab39d/dx_linux.cpp) · [source 5](https://github.com/ptitSeb/stuntcarremake/blob/9f0f8e6e0aca08b715a0f9291ba21c3dc3cab39d/Reference%20only/StuntCarRacer.s) · [source 6](https://github.com/ptitSeb/stuntcarremake/blob/9f0f8e6e0aca08b715a0f9291ba21c3dc3cab39d/Makefile) · [source 7](https://api.github.com/repos/ptitSeb/stuntcarremake/commits?per_page=30&page=1)

**Lineage and rights (reviewed):** The SourceForge Windows original, portable GitHub branch and browser build form one counted project lineage. Existing Vesuri native Amiga framerate-enhancement work is distinct. Original track/audio data and Microsoft SDK code retain separate rights; LICENSE-DejaVu licenses the font only and no clear project-wide game license was found. License/asset review: No clear project-wide license found; font-specific Bitstream/DejaVu terms and Microsoft SDK source notice are separate. Wider author/dependency graphs remain partial.

Evidence: [source 1](https://github.com/ptitSeb/stuntcarremake/blob/9f0f8e6e0aca08b715a0f9291ba21c3dc3cab39d/README.md) · [source 2](https://github.com/ptitSeb/stuntcarremake/blob/9f0f8e6e0aca08b715a0f9291ba21c3dc3cab39d/Car_Behaviour.cpp) · [source 3](https://github.com/ptitSeb/stuntcarremake/blob/9f0f8e6e0aca08b715a0f9291ba21c3dc3cab39d/StuntCarRacer.cpp) · [source 4](https://github.com/ptitSeb/stuntcarremake/blob/9f0f8e6e0aca08b715a0f9291ba21c3dc3cab39d/dx_linux.cpp) · [source 5](https://github.com/ptitSeb/stuntcarremake/blob/9f0f8e6e0aca08b715a0f9291ba21c3dc3cab39d/Reference%20only/StuntCarRacer.s) · [source 6](https://github.com/ptitSeb/stuntcarremake/blob/9f0f8e6e0aca08b715a0f9291ba21c3dc3cab39d/Makefile) · [source 7](https://github.com/ptitSeb/stuntcarremake/blob/9f0f8e6e0aca08b715a0f9291ba21c3dc3cab39d/LICENSE-DejaVu) · [source 8](https://sourceforge.net/projects/stuntcarremake/) · [source 9](https://api.github.com/repos/ptitSeb/stuntcarremake/git/commits/9f0f8e6e0aca08b715a0f9291ba21c3dc3cab39d) · [source 10](https://github.com/Vesuri/stuntcarracer)

### TuxPuck Amiga — native m68k SDL game port

[Repository](https://github.com/Ozzyboshi/tuxpuck-amiga)

- Source platforms: Linux
- Target platforms: Amiga
- Source CPU: Unasserted / not applicable
- Target CPU: m68k
- Source material/language: C
- Maintained language: C
- Classification: subject; game
- Build flags: all unknown (compilable, runnable, playable and byte_exact).
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Jacob Kroon’s TuxPuck SDL game ported to classic Amiga with native m68k-amigaos build recipes. Canonical root https://github.com/Ozzyboshi/tuxpuck-amiga was screened against the fresh 1621-project baseline and 1861-root union including prior sources, decisions and reviews. Source snapshot: commit 2bd2cee2d52e3f99d77b151f4d1774fa9852748f; actual root Git tree 2761dbe65c3c499ec7ed1efc6baf6e772e7cfacc verified through https://api.github.com/repos/Ozzyboshi/tuxpuck-amiga/git/commits/2bd2cee2d52e3f99d77b151f4d1774fa9852748f.

Evidence: [source 1](https://github.com/Ozzyboshi/tuxpuck-amiga/blob/2bd2cee2d52e3f99d77b151f4d1774fa9852748f/readme.txt) · [source 2](https://github.com/Ozzyboshi/tuxpuck-amiga/blob/2bd2cee2d52e3f99d77b151f4d1774fa9852748f/tuxpuck.c) · [source 3](https://github.com/Ozzyboshi/tuxpuck-amiga/blob/2bd2cee2d52e3f99d77b151f4d1774fa9852748f/player.c) · [source 4](https://github.com/Ozzyboshi/tuxpuck-amiga) · [source 5](https://api.github.com/repos/Ozzyboshi/tuxpuck-amiga/git/commits/2bd2cee2d52e3f99d77b151f4d1774fa9852748f)

**Classification (reviewed):** Classified as subject with native m68k source port. No unsupported decompilation, recovery or RE-derived method is assigned. Makefile and data/Makefile explicitly use m68k-amigaos-gcc, m68k-amigaos-ar and Amiga SDL/library paths, establishing an actual native target rather than name-only association.

Evidence: [source 1](https://github.com/Ozzyboshi/tuxpuck-amiga/blob/2bd2cee2d52e3f99d77b151f4d1774fa9852748f/readme.txt) · [source 2](https://github.com/Ozzyboshi/tuxpuck-amiga/blob/2bd2cee2d52e3f99d77b151f4d1774fa9852748f/tuxpuck.c) · [source 3](https://github.com/Ozzyboshi/tuxpuck-amiga/blob/2bd2cee2d52e3f99d77b151f4d1774fa9852748f/player.c) · [source 4](https://github.com/Ozzyboshi/tuxpuck-amiga/blob/2bd2cee2d52e3f99d77b151f4d1774fa9852748f/Makefile) · [source 5](https://github.com/Ozzyboshi/tuxpuck-amiga/blob/2bd2cee2d52e3f99d77b151f4d1774fa9852748f/data/Makefile)

**Source architecture (not-applicable):** This is a port of author-provided portable C source, not recovery of a native original-game binary. No original CPU is established by the Linux/Unix provenance or gameplay AI logic; source_cpu remains empty.

Evidence: [source 1](https://github.com/Ozzyboshi/tuxpuck-amiga/blob/2bd2cee2d52e3f99d77b151f4d1774fa9852748f/readme.txt) · [source 2](https://github.com/Ozzyboshi/tuxpuck-amiga/blob/2bd2cee2d52e3f99d77b151f4d1774fa9852748f/tuxpuck.c) · [source 3](https://github.com/Ozzyboshi/tuxpuck-amiga/blob/2bd2cee2d52e3f99d77b151f4d1774fa9852748f/player.c) · [source 4](https://github.com/Ozzyboshi/tuxpuck-amiga/blob/2bd2cee2d52e3f99d77b151f4d1774fa9852748f/Makefile) · [source 5](https://github.com/Ozzyboshi/tuxpuck-amiga/blob/2bd2cee2d52e3f99d77b151f4d1774fa9852748f/data/Makefile)

**Target architecture (reviewed):** Makefile and data/Makefile explicitly invoke m68k-amigaos-gcc and m68k-amigaos-ar. These establish native m68k output without proving any exact CPU minimum or compatibility with stock hardware.

Evidence: [source 1](https://github.com/Ozzyboshi/tuxpuck-amiga/blob/2bd2cee2d52e3f99d77b151f4d1774fa9852748f/Makefile) · [source 2](https://github.com/Ozzyboshi/tuxpuck-amiga/blob/2bd2cee2d52e3f99d77b151f4d1774fa9852748f/data/Makefile) · [source 3](https://github.com/Ozzyboshi/tuxpuck-amiga/blob/2bd2cee2d52e3f99d77b151f4d1774fa9852748f/readme.txt) · [source 4](https://github.com/Ozzyboshi/tuxpuck-amiga/blob/2bd2cee2d52e3f99d77b151f4d1774fa9852748f/tuxpuck.c) · [source 5](https://github.com/Ozzyboshi/tuxpuck-amiga/blob/2bd2cee2d52e3f99d77b151f4d1774fa9852748f/player.c)

**Build and verification (reviewed):** Amiga build recipes hard-code /opt/amiga and /root/amiga-gcc dependencies, link SDL/SDL_mixer, PNG/JPEG/Vorbis libraries and package generated asset arrays. Upstream generic install instructions are not a verified clean Amiga build; bundled object files are not build evidence. All four build flags are null. No independent successful build, execution, gameplay or byte-exact result is claimed.

Evidence: [source 1](https://github.com/Ozzyboshi/tuxpuck-amiga/blob/2bd2cee2d52e3f99d77b151f4d1774fa9852748f/Makefile) · [source 2](https://github.com/Ozzyboshi/tuxpuck-amiga/blob/2bd2cee2d52e3f99d77b151f4d1774fa9852748f/data/Makefile) · [source 3](https://github.com/Ozzyboshi/tuxpuck-amiga/blob/2bd2cee2d52e3f99d77b151f4d1774fa9852748f/readme.txt)

**Runtime requirements (no-evidence-found):** Selected primary material does not establish a sufficiently explicit output-specific hardware minimum. No profile is populated: build flags, guest models, development machines and historical test anecdotes are not extrapolated into verified CPU/RAM/chipset/OS minima.

Evidence: [source 1](https://github.com/Ozzyboshi/tuxpuck-amiga/blob/2bd2cee2d52e3f99d77b151f4d1774fa9852748f/readme.txt) · [source 2](https://github.com/Ozzyboshi/tuxpuck-amiga/blob/2bd2cee2d52e3f99d77b151f4d1774fa9852748f/tuxpuck.c) · [source 3](https://github.com/Ozzyboshi/tuxpuck-amiga/blob/2bd2cee2d52e3f99d77b151f4d1774fa9852748f/player.c) · [source 4](https://github.com/Ozzyboshi/tuxpuck-amiga/blob/2bd2cee2d52e3f99d77b151f4d1774fa9852748f/Makefile) · [source 5](https://github.com/Ozzyboshi/tuxpuck-amiga/blob/2bd2cee2d52e3f99d77b151f4d1774fa9852748f/data/Makefile)

**AI attribution (no-evidence-found):** No explicit generative-AI attribution found in the selected README, source, build, license evidence or 2 recent commit messages. This bounded review is not proof of non-use. Generic provider domains and gameplay AI are not tool attribution. Generic provider/model mentions, ordinary gameplay AI and future hypothetical uses are not named-tool attribution.

Evidence: [source 1](https://github.com/Ozzyboshi/tuxpuck-amiga/blob/2bd2cee2d52e3f99d77b151f4d1774fa9852748f/readme.txt) · [source 2](https://github.com/Ozzyboshi/tuxpuck-amiga/blob/2bd2cee2d52e3f99d77b151f4d1774fa9852748f/tuxpuck.c) · [source 3](https://github.com/Ozzyboshi/tuxpuck-amiga/blob/2bd2cee2d52e3f99d77b151f4d1774fa9852748f/player.c) · [source 4](https://github.com/Ozzyboshi/tuxpuck-amiga/blob/2bd2cee2d52e3f99d77b151f4d1774fa9852748f/Makefile) · [source 5](https://github.com/Ozzyboshi/tuxpuck-amiga/blob/2bd2cee2d52e3f99d77b151f4d1774fa9852748f/data/Makefile) · [source 6](https://api.github.com/repos/Ozzyboshi/tuxpuck-amiga/commits?per_page=30&page=1)

**Lineage and rights (reviewed):** Jacob Kroon’s TuxPuck source and this Amiga port remain a source-derived port, not a decompilation. COPYING supplies GPLv2 and headers refer to it; bundled asset provenance was not separately audited. No Vampire requirement is borrowed from the author’s Airstrike port. License/asset review: GPL version 2 text in COPYING; original source headers refer to it. Assets retain original upstream provenance and were not separately audited. Wider author/dependency graphs remain partial.

Evidence: [source 1](https://github.com/Ozzyboshi/tuxpuck-amiga/blob/2bd2cee2d52e3f99d77b151f4d1774fa9852748f/readme.txt) · [source 2](https://github.com/Ozzyboshi/tuxpuck-amiga/blob/2bd2cee2d52e3f99d77b151f4d1774fa9852748f/tuxpuck.c) · [source 3](https://github.com/Ozzyboshi/tuxpuck-amiga/blob/2bd2cee2d52e3f99d77b151f4d1774fa9852748f/player.c) · [source 4](https://github.com/Ozzyboshi/tuxpuck-amiga/blob/2bd2cee2d52e3f99d77b151f4d1774fa9852748f/Makefile) · [source 5](https://github.com/Ozzyboshi/tuxpuck-amiga/blob/2bd2cee2d52e3f99d77b151f4d1774fa9852748f/data/Makefile) · [source 6](https://github.com/Ozzyboshi/tuxpuck-amiga/blob/2bd2cee2d52e3f99d77b151f4d1774fa9852748f/COPYING) · [source 7](https://api.github.com/repos/Ozzyboshi/tuxpuck-amiga/git/commits/2bd2cee2d52e3f99d77b151f4d1774fa9852748f)

### Airstrike Amiga — native RTG dogfighting port

[Repository](https://github.com/Ozzyboshi/airstrike-amiga)

- Source platforms: Linux
- Target platforms: Amiga
- Source CPU: Unasserted / not applicable
- Target CPU: m68k
- Source material/language: C
- Maintained language: C
- Classification: subject; game
- Build flags: all unknown (compilable, runnable, playable and byte_exact).
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Amiga m68k/RTG port of the unfinished SDL Airstrike two-dimensional dogfighting game. Canonical root https://github.com/Ozzyboshi/airstrike-amiga was screened against the fresh 1621-project baseline and 1861-root union including prior sources, decisions and reviews. Source snapshot: commit e4e4b0be7216a939ea043ff78c7a28947552799c; actual root Git tree 36b07c5db8d585e701f9426379405e5fc4832612 verified through https://api.github.com/repos/Ozzyboshi/airstrike-amiga/git/commits/e4e4b0be7216a939ea043ff78c7a28947552799c.

Evidence: [source 1](https://github.com/Ozzyboshi/airstrike-amiga/blob/e4e4b0be7216a939ea043ff78c7a28947552799c/Readme.md) · [source 2](https://github.com/Ozzyboshi/airstrike-amiga/blob/e4e4b0be7216a939ea043ff78c7a28947552799c/README) · [source 3](https://github.com/Ozzyboshi/airstrike-amiga/blob/e4e4b0be7216a939ea043ff78c7a28947552799c/src/airstrike.c) · [source 4](https://github.com/Ozzyboshi/airstrike-amiga/blob/e4e4b0be7216a939ea043ff78c7a28947552799c/airstrike-amiga.readme) · [source 5](https://github.com/Ozzyboshi/airstrike-amiga) · [source 6](https://api.github.com/repos/Ozzyboshi/airstrike-amiga/git/commits/e4e4b0be7216a939ea043ff78c7a28947552799c)

**Classification (reviewed):** Classified as subject with native high-end Amiga source port. No unsupported decompilation, recovery or RE-derived method is assigned. Port README explicitly targets high-end RTG Amigas such as Vampire and names bebbo’s GCC plus Amiga SDL 1.2.

Evidence: [source 1](https://github.com/Ozzyboshi/airstrike-amiga/blob/e4e4b0be7216a939ea043ff78c7a28947552799c/Readme.md) · [source 2](https://github.com/Ozzyboshi/airstrike-amiga/blob/e4e4b0be7216a939ea043ff78c7a28947552799c/README) · [source 3](https://github.com/Ozzyboshi/airstrike-amiga/blob/e4e4b0be7216a939ea043ff78c7a28947552799c/src/airstrike.c) · [source 4](https://github.com/Ozzyboshi/airstrike-amiga/blob/e4e4b0be7216a939ea043ff78c7a28947552799c/airstrike-amiga.readme) · [source 5](https://github.com/Ozzyboshi/airstrike-amiga/blob/e4e4b0be7216a939ea043ff78c7a28947552799c/Makefile) · [source 6](https://github.com/Ozzyboshi/airstrike-amiga/blob/e4e4b0be7216a939ea043ff78c7a28947552799c/src/Makefile)

**Source architecture (not-applicable):** The author ports existing C/SDL Airstrike source from Debian; no native original binary or original CPU was analysed. Source CPU is not assigned from the Linux platform.

Evidence: [source 1](https://github.com/Ozzyboshi/airstrike-amiga/blob/e4e4b0be7216a939ea043ff78c7a28947552799c/Readme.md) · [source 2](https://github.com/Ozzyboshi/airstrike-amiga/blob/e4e4b0be7216a939ea043ff78c7a28947552799c/README) · [source 3](https://github.com/Ozzyboshi/airstrike-amiga/blob/e4e4b0be7216a939ea043ff78c7a28947552799c/src/airstrike.c) · [source 4](https://github.com/Ozzyboshi/airstrike-amiga/blob/e4e4b0be7216a939ea043ff78c7a28947552799c/airstrike-amiga.readme) · [source 5](https://github.com/Ozzyboshi/airstrike-amiga/blob/e4e4b0be7216a939ea043ff78c7a28947552799c/Makefile) · [source 6](https://github.com/Ozzyboshi/airstrike-amiga/blob/e4e4b0be7216a939ea043ff78c7a28947552799c/src/Makefile)

**Target architecture (reviewed):** src/Makefile explicitly uses m68k-amigaos-gcc and Amiga SDL libraries. It establishes the m68k target family, but not an exact 680x0 minimum.

Evidence: [source 1](https://github.com/Ozzyboshi/airstrike-amiga/blob/e4e4b0be7216a939ea043ff78c7a28947552799c/Makefile) · [source 2](https://github.com/Ozzyboshi/airstrike-amiga/blob/e4e4b0be7216a939ea043ff78c7a28947552799c/src/Makefile) · [source 3](https://github.com/Ozzyboshi/airstrike-amiga/blob/e4e4b0be7216a939ea043ff78c7a28947552799c/Readme.md) · [source 4](https://github.com/Ozzyboshi/airstrike-amiga/blob/e4e4b0be7216a939ea043ff78c7a28947552799c/README) · [source 5](https://github.com/Ozzyboshi/airstrike-amiga/blob/e4e4b0be7216a939ea043ff78c7a28947552799c/src/airstrike.c) · [source 6](https://github.com/Ozzyboshi/airstrike-amiga/blob/e4e4b0be7216a939ea043ff78c7a28947552799c/airstrike-amiga.readme)

**Build and verification (reviewed):** Makefile delegates to src/Makefile for ordinary and sound-enabled targets. Source forces 800x600 and the author documents a high-end RTG/Vampire setup and bebbo GCC Docker build. No compiler/container/game was run. All four build flags are null. No independent successful build, execution, gameplay or byte-exact result is claimed.

Evidence: [source 1](https://github.com/Ozzyboshi/airstrike-amiga/blob/e4e4b0be7216a939ea043ff78c7a28947552799c/Makefile) · [source 2](https://github.com/Ozzyboshi/airstrike-amiga/blob/e4e4b0be7216a939ea043ff78c7a28947552799c/src/Makefile) · [source 3](https://github.com/Ozzyboshi/airstrike-amiga/blob/e4e4b0be7216a939ea043ff78c7a28947552799c/Readme.md)

**Runtime requirements (reviewed):** Upstream specifically intends a high-end RTG machine such as Vampire; no exact CPU or RAM floor is documented. This is a documented requirement, not an independently tested configuration.

Evidence: [source 1](https://github.com/Ozzyboshi/airstrike-amiga/blob/e4e4b0be7216a939ea043ff78c7a28947552799c/Readme.md) · [source 2](https://github.com/Ozzyboshi/airstrike-amiga/blob/e4e4b0be7216a939ea043ff78c7a28947552799c/README) · [source 3](https://github.com/Ozzyboshi/airstrike-amiga/blob/e4e4b0be7216a939ea043ff78c7a28947552799c/src/airstrike.c) · [source 4](https://github.com/Ozzyboshi/airstrike-amiga/blob/e4e4b0be7216a939ea043ff78c7a28947552799c/airstrike-amiga.readme) · [source 5](https://github.com/Ozzyboshi/airstrike-amiga/blob/e4e4b0be7216a939ea043ff78c7a28947552799c/Makefile) · [source 6](https://github.com/Ozzyboshi/airstrike-amiga/blob/e4e4b0be7216a939ea043ff78c7a28947552799c/src/Makefile)

**AI attribution (no-evidence-found):** No explicit generative-AI attribution found in the selected README, source, build, license evidence or 18 recent commit messages. This bounded review is not proof of non-use. Generic provider domains and gameplay AI are not tool attribution. Generic provider/model mentions, ordinary gameplay AI and future hypothetical uses are not named-tool attribution.

Evidence: [source 1](https://github.com/Ozzyboshi/airstrike-amiga/blob/e4e4b0be7216a939ea043ff78c7a28947552799c/Readme.md) · [source 2](https://github.com/Ozzyboshi/airstrike-amiga/blob/e4e4b0be7216a939ea043ff78c7a28947552799c/README) · [source 3](https://github.com/Ozzyboshi/airstrike-amiga/blob/e4e4b0be7216a939ea043ff78c7a28947552799c/src/airstrike.c) · [source 4](https://github.com/Ozzyboshi/airstrike-amiga/blob/e4e4b0be7216a939ea043ff78c7a28947552799c/airstrike-amiga.readme) · [source 5](https://github.com/Ozzyboshi/airstrike-amiga/blob/e4e4b0be7216a939ea043ff78c7a28947552799c/Makefile) · [source 6](https://github.com/Ozzyboshi/airstrike-amiga/blob/e4e4b0be7216a939ea043ff78c7a28947552799c/src/Makefile) · [source 7](https://api.github.com/repos/Ozzyboshi/airstrike-amiga/commits?per_page=30&page=1)

**Lineage and rights (reviewed):** The inherited Airstrike test-6 README calls the game unfinished. LICENSE covers program and most data under GPL with uncertain public-domain provenance for some Internet-sourced sounds; COPYING contains GPLv2. License/asset review: GPL version 2 text plus LICENSE describing most data as GPL and uncertain public-domain provenance for some sounds. Wider author/dependency graphs remain partial.

Evidence: [source 1](https://github.com/Ozzyboshi/airstrike-amiga/blob/e4e4b0be7216a939ea043ff78c7a28947552799c/Readme.md) · [source 2](https://github.com/Ozzyboshi/airstrike-amiga/blob/e4e4b0be7216a939ea043ff78c7a28947552799c/README) · [source 3](https://github.com/Ozzyboshi/airstrike-amiga/blob/e4e4b0be7216a939ea043ff78c7a28947552799c/src/airstrike.c) · [source 4](https://github.com/Ozzyboshi/airstrike-amiga/blob/e4e4b0be7216a939ea043ff78c7a28947552799c/airstrike-amiga.readme) · [source 5](https://github.com/Ozzyboshi/airstrike-amiga/blob/e4e4b0be7216a939ea043ff78c7a28947552799c/Makefile) · [source 6](https://github.com/Ozzyboshi/airstrike-amiga/blob/e4e4b0be7216a939ea043ff78c7a28947552799c/src/Makefile) · [source 7](https://github.com/Ozzyboshi/airstrike-amiga/blob/e4e4b0be7216a939ea043ff78c7a28947552799c/LICENSE) · [source 8](https://github.com/Ozzyboshi/airstrike-amiga/blob/e4e4b0be7216a939ea043ff78c7a28947552799c/COPYING) · [source 9](https://api.github.com/repos/Ozzyboshi/airstrike-amiga/git/commits/e4e4b0be7216a939ea043ff78c7a28947552799c)

Documented profiles: [{"name": "Amiga RTG port requirements", "platform": "Amiga", "os": "AmigaOS 3.1 or later", "notes": "Upstream specifically intends a high-end RTG machine such as Vampire; no exact CPU or RAM floor is documented. This is a documented requirement, not an independently tested configuration.", "evidence": ["https://github.com/Ozzyboshi/airstrike-amiga/blob/e4e4b0be7216a939ea043ff78c7a28947552799c/Readme.md", "https://github.com/Ozzyboshi/airstrike-amiga/blob/e4e4b0be7216a939ea043ff78c7a28947552799c/airstrike-amiga.readme"]}]

### jzIntv Amiga — native Intellivision emulator port

[Repository](https://github.com/Ozzyboshi/jzintv-amiga)

- Source platforms: Linux
- Target platforms: Amiga
- Source CPU: Unasserted / not applicable
- Target CPU: m68k
- Source material/language: Unasserted / not applicable
- Maintained language: C, C++
- Classification: tooling; emulator
- Build flags: all unknown (compilable, runnable, playable and byte_exact).
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Native classic-Amiga m68k port of Joe Zbiciak’s general Intellivision emulator, with CP1600 core and SDK build. Canonical root https://github.com/Ozzyboshi/jzintv-amiga was screened against the fresh 1621-project baseline and 1861-root union including prior sources, decisions and reviews. Source snapshot: commit 949ef533264b74603f60ceeb5edc76c680f78dbe; actual root Git tree 7c5314c39668e589c6f9ad641be2cc7b81e7cb4f verified through https://api.github.com/repos/Ozzyboshi/jzintv-amiga/git/commits/949ef533264b74603f60ceeb5edc76c680f78dbe.

Evidence: [source 1](https://github.com/Ozzyboshi/jzintv-amiga/blob/949ef533264b74603f60ceeb5edc76c680f78dbe/README.md) · [source 2](https://github.com/Ozzyboshi/jzintv-amiga/blob/949ef533264b74603f60ceeb5edc76c680f78dbe/README.txt) · [source 3](https://github.com/Ozzyboshi/jzintv-amiga/blob/949ef533264b74603f60ceeb5edc76c680f78dbe/jzintv-amiga.readme) · [source 4](https://github.com/Ozzyboshi/jzintv-amiga/blob/949ef533264b74603f60ceeb5edc76c680f78dbe/src/cp1600/cp1600.c) · [source 5](https://github.com/Ozzyboshi/jzintv-amiga) · [source 6](https://api.github.com/repos/Ozzyboshi/jzintv-amiga/git/commits/949ef533264b74603f60ceeb5edc76c680f78dbe)

**Classification (reviewed):** Classified as tooling with native port of a general console emulator. No unsupported decompilation, recovery or RE-derived method is assigned. Tool capabilities: emulator. README and Aminet readme identify RTG as required, m68k-amigaos >= 3.1 and successful upstream use on a Vampire-equipped Amiga.

Evidence: [source 1](https://github.com/Ozzyboshi/jzintv-amiga/blob/949ef533264b74603f60ceeb5edc76c680f78dbe/README.md) · [source 2](https://github.com/Ozzyboshi/jzintv-amiga/blob/949ef533264b74603f60ceeb5edc76c680f78dbe/README.txt) · [source 3](https://github.com/Ozzyboshi/jzintv-amiga/blob/949ef533264b74603f60ceeb5edc76c680f78dbe/jzintv-amiga.readme) · [source 4](https://github.com/Ozzyboshi/jzintv-amiga/blob/949ef533264b74603f60ceeb5edc76c680f78dbe/src/cp1600/cp1600.c) · [source 5](https://github.com/Ozzyboshi/jzintv-amiga/blob/949ef533264b74603f60ceeb5edc76c680f78dbe/src/Makefile.m68k) · [source 6](https://github.com/Ozzyboshi/jzintv-amiga/blob/949ef533264b74603f60ceeb5edc76c680f78dbe/src/Makefile.common)

**Source architecture (not-applicable):** A port of a general console emulator from existing source, not recovered native game code. The CP1600 guest instruction core is documented in notes; it is not a host/source CPU inferred from Linux or a new catalogue CPU label.

Evidence: [source 1](https://github.com/Ozzyboshi/jzintv-amiga/blob/949ef533264b74603f60ceeb5edc76c680f78dbe/README.md) · [source 2](https://github.com/Ozzyboshi/jzintv-amiga/blob/949ef533264b74603f60ceeb5edc76c680f78dbe/README.txt) · [source 3](https://github.com/Ozzyboshi/jzintv-amiga/blob/949ef533264b74603f60ceeb5edc76c680f78dbe/jzintv-amiga.readme) · [source 4](https://github.com/Ozzyboshi/jzintv-amiga/blob/949ef533264b74603f60ceeb5edc76c680f78dbe/src/cp1600/cp1600.c) · [source 5](https://github.com/Ozzyboshi/jzintv-amiga/blob/949ef533264b74603f60ceeb5edc76c680f78dbe/src/Makefile.m68k) · [source 6](https://github.com/Ozzyboshi/jzintv-amiga/blob/949ef533264b74603f60ceeb5edc76c680f78dbe/src/Makefile.common)

**Target architecture (reviewed):** src/Makefile.m68k explicitly invokes m68k-amigaos GCC/G++ and links Amiga SDL. The commented -mtune=68080 is not an active CPU requirement; m68k is the supported family-level output claim.

Evidence: [source 1](https://github.com/Ozzyboshi/jzintv-amiga/blob/949ef533264b74603f60ceeb5edc76c680f78dbe/src/Makefile.m68k) · [source 2](https://github.com/Ozzyboshi/jzintv-amiga/blob/949ef533264b74603f60ceeb5edc76c680f78dbe/src/Makefile.common) · [source 3](https://github.com/Ozzyboshi/jzintv-amiga/blob/949ef533264b74603f60ceeb5edc76c680f78dbe/README.md) · [source 4](https://github.com/Ozzyboshi/jzintv-amiga/blob/949ef533264b74603f60ceeb5edc76c680f78dbe/README.txt) · [source 5](https://github.com/Ozzyboshi/jzintv-amiga/blob/949ef533264b74603f60ceeb5edc76c680f78dbe/jzintv-amiga.readme) · [source 6](https://github.com/Ozzyboshi/jzintv-amiga/blob/949ef533264b74603f60ceeb5edc76c680f78dbe/src/cp1600/cp1600.c)

**Build and verification (reviewed):** Makefile.m68k and Makefile.common build jzIntv plus SDK-1600. Firmware exec.bin/grom.bin and game ROMs must be supplied separately. No build, ROM execution or accuracy check was run; audio performance remains an upstream warning. All four build flags are null. No independent successful build, execution, gameplay or byte-exact result is claimed.

Evidence: [source 1](https://github.com/Ozzyboshi/jzintv-amiga/blob/949ef533264b74603f60ceeb5edc76c680f78dbe/src/Makefile.m68k) · [source 2](https://github.com/Ozzyboshi/jzintv-amiga/blob/949ef533264b74603f60ceeb5edc76c680f78dbe/src/Makefile.common) · [source 3](https://github.com/Ozzyboshi/jzintv-amiga/blob/949ef533264b74603f60ceeb5edc76c680f78dbe/README.md)

**Runtime requirements (reviewed):** Upstream requires RTG and reports testing on a Vampire-equipped Amiga. Audio performance problems are documented; exact CPU/RAM minima remain unspecified and no runtime test was performed.

Evidence: [source 1](https://github.com/Ozzyboshi/jzintv-amiga/blob/949ef533264b74603f60ceeb5edc76c680f78dbe/README.md) · [source 2](https://github.com/Ozzyboshi/jzintv-amiga/blob/949ef533264b74603f60ceeb5edc76c680f78dbe/README.txt) · [source 3](https://github.com/Ozzyboshi/jzintv-amiga/blob/949ef533264b74603f60ceeb5edc76c680f78dbe/jzintv-amiga.readme) · [source 4](https://github.com/Ozzyboshi/jzintv-amiga/blob/949ef533264b74603f60ceeb5edc76c680f78dbe/src/cp1600/cp1600.c) · [source 5](https://github.com/Ozzyboshi/jzintv-amiga/blob/949ef533264b74603f60ceeb5edc76c680f78dbe/src/Makefile.m68k) · [source 6](https://github.com/Ozzyboshi/jzintv-amiga/blob/949ef533264b74603f60ceeb5edc76c680f78dbe/src/Makefile.common)

**AI attribution (no-evidence-found):** No explicit generative-AI attribution found in the selected README, source, build, license evidence or 10 recent commit messages. This bounded review is not proof of non-use. Generic provider domains and gameplay AI are not tool attribution. Generic provider/model mentions, ordinary gameplay AI and future hypothetical uses are not named-tool attribution.

Evidence: [source 1](https://github.com/Ozzyboshi/jzintv-amiga/blob/949ef533264b74603f60ceeb5edc76c680f78dbe/README.md) · [source 2](https://github.com/Ozzyboshi/jzintv-amiga/blob/949ef533264b74603f60ceeb5edc76c680f78dbe/README.txt) · [source 3](https://github.com/Ozzyboshi/jzintv-amiga/blob/949ef533264b74603f60ceeb5edc76c680f78dbe/jzintv-amiga.readme) · [source 4](https://github.com/Ozzyboshi/jzintv-amiga/blob/949ef533264b74603f60ceeb5edc76c680f78dbe/src/cp1600/cp1600.c) · [source 5](https://github.com/Ozzyboshi/jzintv-amiga/blob/949ef533264b74603f60ceeb5edc76c680f78dbe/src/Makefile.m68k) · [source 6](https://github.com/Ozzyboshi/jzintv-amiga/blob/949ef533264b74603f60ceeb5edc76c680f78dbe/src/Makefile.common) · [source 7](https://api.github.com/repos/Ozzyboshi/jzintv-amiga/commits?per_page=30&page=1)

**Lineage and rights (reviewed):** Joe Zbiciak’s general Intellivision emulator is eligible as general tooling, not a game-specific emulation wrapper. GPLv2 text was inspected; firmware/game ROM rights are separate. The -a0 prose versus -ao example discrepancy and A600 keymap issue are retained. License/asset review: GPL version 2 text at repository root; external firmware and game ROM rights remain separate. Wider author/dependency graphs remain partial.

Evidence: [source 1](https://github.com/Ozzyboshi/jzintv-amiga/blob/949ef533264b74603f60ceeb5edc76c680f78dbe/README.md) · [source 2](https://github.com/Ozzyboshi/jzintv-amiga/blob/949ef533264b74603f60ceeb5edc76c680f78dbe/README.txt) · [source 3](https://github.com/Ozzyboshi/jzintv-amiga/blob/949ef533264b74603f60ceeb5edc76c680f78dbe/jzintv-amiga.readme) · [source 4](https://github.com/Ozzyboshi/jzintv-amiga/blob/949ef533264b74603f60ceeb5edc76c680f78dbe/src/cp1600/cp1600.c) · [source 5](https://github.com/Ozzyboshi/jzintv-amiga/blob/949ef533264b74603f60ceeb5edc76c680f78dbe/src/Makefile.m68k) · [source 6](https://github.com/Ozzyboshi/jzintv-amiga/blob/949ef533264b74603f60ceeb5edc76c680f78dbe/src/Makefile.common) · [source 7](https://github.com/Ozzyboshi/jzintv-amiga/blob/949ef533264b74603f60ceeb5edc76c680f78dbe/COPYING.txt) · [source 8](https://api.github.com/repos/Ozzyboshi/jzintv-amiga/git/commits/949ef533264b74603f60ceeb5edc76c680f78dbe)

Documented profiles: [{"name": "Classic Amiga RTG port", "platform": "Amiga", "os": "AmigaOS 3.1 or later", "notes": "Upstream requires RTG and reports testing on a Vampire-equipped Amiga. Audio performance problems are documented; exact CPU/RAM minima remain unspecified and no runtime test was performed.", "evidence": ["https://github.com/Ozzyboshi/jzintv-amiga/blob/949ef533264b74603f60ceeb5edc76c680f78dbe/README.md", "https://github.com/Ozzyboshi/jzintv-amiga/blob/949ef533264b74603f60ceeb5edc76c680f78dbe/jzintv-amiga.readme"]}]

### VControlGUI — Amiga Vampire accelerator control panel

[Repository](https://github.com/Ozzyboshi/VControlGUI)

- Source platforms: Amiga
- Target platforms: Amiga
- Source CPU: Unasserted / not applicable
- Target CPU: m68k
- Source material/language: C, m68k assembly
- Maintained language: C, m68k assembly
- Classification: subject; application
- Build flags: all unknown (compilable, runnable, playable and byte_exact).
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Intuition/GadTools control panel for Vampire cards that calls external VControl and reads CPU control registers. Canonical root https://github.com/Ozzyboshi/VControlGUI was screened against the fresh 1621-project baseline and 1861-root union including prior sources, decisions and reviews. Source snapshot: commit 9debf4c18822e266e618da72381896499223c5ca; actual root Git tree 996305cea8953d1980ec5da349ba0594c535c236 verified through https://api.github.com/repos/Ozzyboshi/VControlGUI/git/commits/9debf4c18822e266e618da72381896499223c5ca.

Evidence: [source 1](https://github.com/Ozzyboshi/VControlGUI/blob/9debf4c18822e266e618da72381896499223c5ca/README.md) · [source 2](https://github.com/Ozzyboshi/VControlGUI/blob/9debf4c18822e266e618da72381896499223c5ca/VControlGUI.c) · [source 3](https://github.com/Ozzyboshi/VControlGUI/blob/9debf4c18822e266e618da72381896499223c5ca/V_CPU_CACR.asm) · [source 4](https://github.com/Ozzyboshi/VControlGUI) · [source 5](https://api.github.com/repos/Ozzyboshi/VControlGUI/git/commits/9debf4c18822e266e618da72381896499223c5ca)

**Classification (reviewed):** Classified as subject with native Amiga accelerator-control application. No unsupported decompilation, recovery or RE-derived method is assigned. README requires a Vampire card, VControl installed in the path and AmigaOS; upstream tested AmigaOS 3.1.4 and Coffin.

Evidence: [source 1](https://github.com/Ozzyboshi/VControlGUI/blob/9debf4c18822e266e618da72381896499223c5ca/README.md) · [source 2](https://github.com/Ozzyboshi/VControlGUI/blob/9debf4c18822e266e618da72381896499223c5ca/VControlGUI.c) · [source 3](https://github.com/Ozzyboshi/VControlGUI/blob/9debf4c18822e266e618da72381896499223c5ca/V_CPU_CACR.asm) · [source 4](https://github.com/Ozzyboshi/VControlGUI/blob/9debf4c18822e266e618da72381896499223c5ca/Makefile)

**Source architecture (not-applicable):** This is original native application source, not reconstruction of a separately identified historical binary. The native helper code is target implementation, so no recovered source CPU is asserted.

Evidence: [source 1](https://github.com/Ozzyboshi/VControlGUI/blob/9debf4c18822e266e618da72381896499223c5ca/README.md) · [source 2](https://github.com/Ozzyboshi/VControlGUI/blob/9debf4c18822e266e618da72381896499223c5ca/VControlGUI.c) · [source 3](https://github.com/Ozzyboshi/VControlGUI/blob/9debf4c18822e266e618da72381896499223c5ca/V_CPU_CACR.asm) · [source 4](https://github.com/Ozzyboshi/VControlGUI/blob/9debf4c18822e266e618da72381896499223c5ca/Makefile)

**Target architecture (reviewed):** V_CPU_CACR.asm declares machine mc68020 and uses MOVEC/CACR in supervisor mode. Together with the vasm and m68k-amigaos-GCC build, this supports native m68k output. Makefile -m68000 must not be misread as whole-program stock-68000 compatibility.

Evidence: [source 1](https://github.com/Ozzyboshi/VControlGUI/blob/9debf4c18822e266e618da72381896499223c5ca/Makefile) · [source 2](https://github.com/Ozzyboshi/VControlGUI/blob/9debf4c18822e266e618da72381896499223c5ca/README.md) · [source 3](https://github.com/Ozzyboshi/VControlGUI/blob/9debf4c18822e266e618da72381896499223c5ca/VControlGUI.c) · [source 4](https://github.com/Ozzyboshi/VControlGUI/blob/9debf4c18822e266e618da72381896499223c5ca/V_CPU_CACR.asm)

**Build and verification (reviewed):** Makefile links C/GadTools UI with vasm Hunk register-access helpers. External VControl must be installed. No settings, Kickstart selection, accelerator registers or hardware were exercised. All four build flags are null. No independent successful build, execution, gameplay or byte-exact result is claimed.

Evidence: [source 1](https://github.com/Ozzyboshi/VControlGUI/blob/9debf4c18822e266e618da72381896499223c5ca/Makefile) · [source 2](https://github.com/Ozzyboshi/VControlGUI/blob/9debf4c18822e266e618da72381896499223c5ca/README.md)

**Runtime requirements (reviewed):** README requires a Vampire card and VControl in PATH. AmigaOS 3.1.4/Coffin are reported test systems, not universal minimum versions. CPU/RAM/chipset minima are not inferred; no hardware control was tested.

Evidence: [source 1](https://github.com/Ozzyboshi/VControlGUI/blob/9debf4c18822e266e618da72381896499223c5ca/README.md) · [source 2](https://github.com/Ozzyboshi/VControlGUI/blob/9debf4c18822e266e618da72381896499223c5ca/VControlGUI.c) · [source 3](https://github.com/Ozzyboshi/VControlGUI/blob/9debf4c18822e266e618da72381896499223c5ca/V_CPU_CACR.asm) · [source 4](https://github.com/Ozzyboshi/VControlGUI/blob/9debf4c18822e266e618da72381896499223c5ca/Makefile)

**AI attribution (no-evidence-found):** No explicit generative-AI attribution found in the selected README, source, build, license evidence or 8 recent commit messages. This bounded review is not proof of non-use. Generic provider domains and gameplay AI are not tool attribution. Generic provider/model mentions, ordinary gameplay AI and future hypothetical uses are not named-tool attribution.

Evidence: [source 1](https://github.com/Ozzyboshi/VControlGUI/blob/9debf4c18822e266e618da72381896499223c5ca/README.md) · [source 2](https://github.com/Ozzyboshi/VControlGUI/blob/9debf4c18822e266e618da72381896499223c5ca/VControlGUI.c) · [source 3](https://github.com/Ozzyboshi/VControlGUI/blob/9debf4c18822e266e618da72381896499223c5ca/V_CPU_CACR.asm) · [source 4](https://github.com/Ozzyboshi/VControlGUI/blob/9debf4c18822e266e618da72381896499223c5ca/Makefile) · [source 5](https://api.github.com/repos/Ozzyboshi/VControlGUI/commits?per_page=30&page=1)

**Lineage and rights (reviewed):** This is a distinct GUI application for the external VControl utility, not an independent reimplementation of its backend. Main C source explicitly licenses GPLv2-or-later although GitHub metadata is null; separate helper provenance remains partial. License/asset review: GPL-2.0-or-later is explicit in the main C source; no root LICENSE file. Preserve third-party/helper provenance separately. Wider author/dependency graphs remain partial.

Evidence: [source 1](https://github.com/Ozzyboshi/VControlGUI/blob/9debf4c18822e266e618da72381896499223c5ca/README.md) · [source 2](https://github.com/Ozzyboshi/VControlGUI/blob/9debf4c18822e266e618da72381896499223c5ca/VControlGUI.c) · [source 3](https://github.com/Ozzyboshi/VControlGUI/blob/9debf4c18822e266e618da72381896499223c5ca/V_CPU_CACR.asm) · [source 4](https://github.com/Ozzyboshi/VControlGUI/blob/9debf4c18822e266e618da72381896499223c5ca/Makefile) · [source 5](https://api.github.com/repos/Ozzyboshi/VControlGUI/git/commits/9debf4c18822e266e618da72381896499223c5ca)

Documented profiles: [{"name": "Vampire control-panel dependency profile", "platform": "Amiga", "notes": "README requires a Vampire card and VControl in PATH. AmigaOS 3.1.4/Coffin are reported test systems, not universal minimum versions. CPU/RAM/chipset minima are not inferred; no hardware control was tested.", "evidence": ["https://github.com/Ozzyboshi/VControlGUI/blob/9debf4c18822e266e618da72381896499223c5ca/README.md", "https://github.com/Ozzyboshi/VControlGUI/blob/9debf4c18822e266e618da72381896499223c5ca/V_CPU_CACR.asm"]}]

### AmigaFontEditor — browser-based Amiga font and asset tools

[Repository](https://github.com/Ozzyboshi/AmigaFontEditor)

- Source platforms: Amiga
- Target platforms: Web
- Source CPU: Unasserted / not applicable
- Target CPU: Unasserted / not applicable
- Source material/language: Unasserted / not applicable
- Maintained language: JavaScript, HTML
- Classification: tooling; asset-tool
- Build flags: all unknown (compilable, runnable, playable and byte_exact).
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Browser-based bitmap font/sprite/palette and custom-register helpers that produce data for Amiga assembly programs. Canonical root https://github.com/Ozzyboshi/AmigaFontEditor was screened against the fresh 1621-project baseline and 1861-root union including prior sources, decisions and reviews. Source snapshot: commit 2e551ed777853d279e999864401371ff12404bb6; actual root Git tree 36a8bfcd3be641bda8ec7a1b16bbe1916c14efab verified through https://api.github.com/repos/Ozzyboshi/AmigaFontEditor/git/commits/2e551ed777853d279e999864401371ff12404bb6.

Evidence: [source 1](https://github.com/Ozzyboshi/AmigaFontEditor/blob/2e551ed777853d279e999864401371ff12404bb6/README.md) · [source 2](https://github.com/Ozzyboshi/AmigaFontEditor/blob/2e551ed777853d279e999864401371ff12404bb6/js/AmigaFontEditor.js) · [source 3](https://github.com/Ozzyboshi/AmigaFontEditor/blob/2e551ed777853d279e999864401371ff12404bb6/index.html) · [source 4](https://github.com/Ozzyboshi/AmigaFontEditor) · [source 5](https://api.github.com/repos/Ozzyboshi/AmigaFontEditor/git/commits/2e551ed777853d279e999864401371ff12404bb6)

**Classification (reviewed):** Classified as tooling with Amiga asset-development web application. No unsupported decompilation, recovery or RE-derived method is assigned. Tool capabilities: asset-tool. README explicitly describes drawing characters and exporting binary data for Amiga assembly INCBIN, with raw import and hexadecimal/binary inspection.

Evidence: [source 1](https://github.com/Ozzyboshi/AmigaFontEditor/blob/2e551ed777853d279e999864401371ff12404bb6/README.md) · [source 2](https://github.com/Ozzyboshi/AmigaFontEditor/blob/2e551ed777853d279e999864401371ff12404bb6/js/AmigaFontEditor.js) · [source 3](https://github.com/Ozzyboshi/AmigaFontEditor/blob/2e551ed777853d279e999864401371ff12404bb6/index.html)

**Source architecture (not-applicable):** The tool works with font, palette, sprite and planar asset formats for Amiga assembly development, not recovered machine instructions. Amiga is a data/development ecosystem here; source_cpu does not apply.

Evidence: [source 1](https://github.com/Ozzyboshi/AmigaFontEditor/blob/2e551ed777853d279e999864401371ff12404bb6/README.md) · [source 2](https://github.com/Ozzyboshi/AmigaFontEditor/blob/2e551ed777853d279e999864401371ff12404bb6/js/AmigaFontEditor.js) · [source 3](https://github.com/Ozzyboshi/AmigaFontEditor/blob/2e551ed777853d279e999864401371ff12404bb6/index.html)

**Target architecture (no-evidence-found):** The application executes as JavaScript/HTML in a browser and emits binary asset data for INCBIN. This establishes neither a native host ISA nor machine-code output; target_cpu remains empty.

Evidence: [source 1](https://github.com/Ozzyboshi/AmigaFontEditor/blob/2e551ed777853d279e999864401371ff12404bb6/index.html) · [source 2](https://github.com/Ozzyboshi/AmigaFontEditor/blob/2e551ed777853d279e999864401371ff12404bb6/README.md) · [source 3](https://github.com/Ozzyboshi/AmigaFontEditor/blob/2e551ed777853d279e999864401371ff12404bb6/js/AmigaFontEditor.js)

**Build and verification (reviewed):** The static index.html entry point includes author JavaScript and bundled UPNG/pako. No package build pipeline was found for this entry point. README says offline-capable; offline operation and export correctness were not tested. All four build flags are null. No independent successful build, execution, gameplay or byte-exact result is claimed.

Evidence: [source 1](https://github.com/Ozzyboshi/AmigaFontEditor/blob/2e551ed777853d279e999864401371ff12404bb6/index.html) · [source 2](https://github.com/Ozzyboshi/AmigaFontEditor/blob/2e551ed777853d279e999864401371ff12404bb6/README.md)

**Runtime requirements (no-evidence-found):** Selected primary material does not establish a sufficiently explicit output-specific hardware minimum. No profile is populated: build flags, guest models, development machines and historical test anecdotes are not extrapolated into verified CPU/RAM/chipset/OS minima.

Evidence: [source 1](https://github.com/Ozzyboshi/AmigaFontEditor/blob/2e551ed777853d279e999864401371ff12404bb6/README.md) · [source 2](https://github.com/Ozzyboshi/AmigaFontEditor/blob/2e551ed777853d279e999864401371ff12404bb6/js/AmigaFontEditor.js) · [source 3](https://github.com/Ozzyboshi/AmigaFontEditor/blob/2e551ed777853d279e999864401371ff12404bb6/index.html)

**AI attribution (no-evidence-found):** No explicit generative-AI attribution found in the selected README, source, build, license evidence or 30 recent commit messages. This bounded review is not proof of non-use. Generic provider domains and gameplay AI are not tool attribution. Generic provider/model mentions, ordinary gameplay AI and future hypothetical uses are not named-tool attribution.

Evidence: [source 1](https://github.com/Ozzyboshi/AmigaFontEditor/blob/2e551ed777853d279e999864401371ff12404bb6/README.md) · [source 2](https://github.com/Ozzyboshi/AmigaFontEditor/blob/2e551ed777853d279e999864401371ff12404bb6/js/AmigaFontEditor.js) · [source 3](https://github.com/Ozzyboshi/AmigaFontEditor/blob/2e551ed777853d279e999864401371ff12404bb6/index.html) · [source 4](https://api.github.com/repos/Ozzyboshi/AmigaFontEditor/commits?per_page=30&page=1)

**Lineage and rights (reviewed):** One tool suite includes font/sprite, Copper/register and raw/planar helpers. MIT is explicit for project code; bundled UPNG/pako provenance/notices remain separate. It is Amiga development tooling, not a browser emulator wrapper. License/asset review: MIT for project code; bundled UPNG/pako libraries are present and require their own notices/provenance. Wider author/dependency graphs remain partial.

Evidence: [source 1](https://github.com/Ozzyboshi/AmigaFontEditor/blob/2e551ed777853d279e999864401371ff12404bb6/README.md) · [source 2](https://github.com/Ozzyboshi/AmigaFontEditor/blob/2e551ed777853d279e999864401371ff12404bb6/js/AmigaFontEditor.js) · [source 3](https://github.com/Ozzyboshi/AmigaFontEditor/blob/2e551ed777853d279e999864401371ff12404bb6/index.html) · [source 4](https://github.com/Ozzyboshi/AmigaFontEditor/blob/2e551ed777853d279e999864401371ff12404bb6/LICENSE) · [source 5](https://api.github.com/repos/Ozzyboshi/AmigaFontEditor/git/commits/2e551ed777853d279e999864401371ff12404bb6)

### AmigaPouetDownloader — ARexx release organizer and relay

[Repository](https://github.com/Ozzyboshi/AmigaPouetDownloader)

- Source platforms: Amiga
- Target platforms: Amiga, Linux
- Source CPU: Unasserted / not applicable
- Target CPU: m68k
- Source material/language: ARexx, C, JavaScript
- Maintained language: ARexx, C, JavaScript
- Classification: subject; application
- Build flags: all unknown (compilable, runnable, playable and byte_exact).
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Classic-Amiga Pouet release downloader/organizer using ARexx, native C parsers and a Node.js HTTP-to-HTTPS relay. Canonical root https://github.com/Ozzyboshi/AmigaPouetDownloader was screened against the fresh 1621-project baseline and 1861-root union including prior sources, decisions and reviews. Source snapshot: commit f6112eb3e97bafe34348f8953d22bdfc5cfe9a92; actual root Git tree 8b35949eb9cec29384ebc6dc383490f3a2885f65 verified through https://api.github.com/repos/Ozzyboshi/AmigaPouetDownloader/git/commits/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92.

Evidence: [source 1](https://github.com/Ozzyboshi/AmigaPouetDownloader/blob/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92/README.md) · [source 2](https://github.com/Ozzyboshi/AmigaPouetDownloader/blob/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92/amiga/pouet.rexx) · [source 3](https://github.com/Ozzyboshi/AmigaPouetDownloader/blob/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92/amiga/parse_prod.c) · [source 4](https://github.com/Ozzyboshi/AmigaPouetDownloader/blob/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92/httpserver/server.js) · [source 5](https://github.com/Ozzyboshi/AmigaPouetDownloader) · [source 6](https://api.github.com/repos/Ozzyboshi/AmigaPouetDownloader/git/commits/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92)

**Classification (reviewed):** Classified as subject with native ARexx application with modern helper service. No unsupported decompilation, recovery or RE-derived method is assigned. README specifies a classic Amiga with 1 MB RAM, hard disk, TCP/IP stack and connectivity to a modern helper machine; it lists tested A500+/A600 accelerator/network configurations.

Evidence: [source 1](https://github.com/Ozzyboshi/AmigaPouetDownloader/blob/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92/README.md) · [source 2](https://github.com/Ozzyboshi/AmigaPouetDownloader/blob/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92/amiga/pouet.rexx) · [source 3](https://github.com/Ozzyboshi/AmigaPouetDownloader/blob/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92/amiga/parse_prod.c) · [source 4](https://github.com/Ozzyboshi/AmigaPouetDownloader/blob/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92/httpserver/server.js) · [source 5](https://github.com/Ozzyboshi/AmigaPouetDownloader/blob/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92/amiga/compilaparseprod.sh) · [source 6](https://github.com/Ozzyboshi/AmigaPouetDownloader/blob/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92/httpserver/package.json)

**Source architecture (not-applicable):** Original ARexx/C/Node application sources are supplied, not recovered instructions from a legacy binary. Source CPU is not applicable; source-platform association describes the native Amiga application.

Evidence: [source 1](https://github.com/Ozzyboshi/AmigaPouetDownloader/blob/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92/README.md) · [source 2](https://github.com/Ozzyboshi/AmigaPouetDownloader/blob/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92/amiga/pouet.rexx) · [source 3](https://github.com/Ozzyboshi/AmigaPouetDownloader/blob/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92/amiga/parse_prod.c) · [source 4](https://github.com/Ozzyboshi/AmigaPouetDownloader/blob/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92/httpserver/server.js) · [source 5](https://github.com/Ozzyboshi/AmigaPouetDownloader/blob/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92/amiga/compilaparseprod.sh) · [source 6](https://github.com/Ozzyboshi/AmigaPouetDownloader/blob/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92/httpserver/package.json)

**Target architecture (reviewed):** amiga/compilaparseprod.sh explicitly invokes m68k-amigaos-gcc for native helpers. m68k describes those executables only. ARexx and Node hosts do not establish additional instruction sets.

Evidence: [source 1](https://github.com/Ozzyboshi/AmigaPouetDownloader/blob/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92/amiga/compilaparseprod.sh) · [source 2](https://github.com/Ozzyboshi/AmigaPouetDownloader/blob/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92/httpserver/package.json) · [source 3](https://github.com/Ozzyboshi/AmigaPouetDownloader/blob/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92/README.md) · [source 4](https://github.com/Ozzyboshi/AmigaPouetDownloader/blob/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92/amiga/pouet.rexx) · [source 5](https://github.com/Ozzyboshi/AmigaPouetDownloader/blob/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92/amiga/parse_prod.c) · [source 6](https://github.com/Ozzyboshi/AmigaPouetDownloader/blob/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92/httpserver/server.js)

**Build and verification (reviewed):** The helper recipe uses -mcrt=nix20; the parser header also sketches a vbcc alternative. Runtime needs ARexx, wget, mkdir, lha/unzip/xdms and helper binaries. A 512 KB parser buffer and upstream RAM-disk recommendation matter. No build, downloads or archive extraction were run. All four build flags are null. No independent successful build, execution, gameplay or byte-exact result is claimed.

Evidence: [source 1](https://github.com/Ozzyboshi/AmigaPouetDownloader/blob/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92/amiga/compilaparseprod.sh) · [source 2](https://github.com/Ozzyboshi/AmigaPouetDownloader/blob/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92/httpserver/package.json) · [source 3](https://github.com/Ozzyboshi/AmigaPouetDownloader/blob/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92/README.md)

**Runtime requirements (reviewed):** README states 1 MB RAM, hard disk, TCP/IP and network access to a modern helper. It separately recommends at least 8 MB Fast RAM when using a RAM disk; that recommendation is not a universal minimum. Auxiliary binaries must match the actual CPU. No runtime test. README specifies an internet-connected modern PC with Docker/Compose, tested on Ubuntu, reachable from the Amiga on the configured port. No CPU/RAM minimum is asserted here; keep relay private because it is unauthenticated and disables upstream certificate validation.

Evidence: [source 1](https://github.com/Ozzyboshi/AmigaPouetDownloader/blob/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92/README.md) · [source 2](https://github.com/Ozzyboshi/AmigaPouetDownloader/blob/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92/amiga/pouet.rexx) · [source 3](https://github.com/Ozzyboshi/AmigaPouetDownloader/blob/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92/amiga/parse_prod.c) · [source 4](https://github.com/Ozzyboshi/AmigaPouetDownloader/blob/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92/httpserver/server.js) · [source 5](https://github.com/Ozzyboshi/AmigaPouetDownloader/blob/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92/amiga/compilaparseprod.sh) · [source 6](https://github.com/Ozzyboshi/AmigaPouetDownloader/blob/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92/httpserver/package.json)

**AI attribution (no-evidence-found):** No explicit generative-AI attribution found in the selected README, source, build, license evidence or 30 recent commit messages. This bounded review is not proof of non-use. Generic provider domains and gameplay AI are not tool attribution. Generic provider/model mentions, ordinary gameplay AI and future hypothetical uses are not named-tool attribution.

Evidence: [source 1](https://github.com/Ozzyboshi/AmigaPouetDownloader/blob/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92/README.md) · [source 2](https://github.com/Ozzyboshi/AmigaPouetDownloader/blob/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92/amiga/pouet.rexx) · [source 3](https://github.com/Ozzyboshi/AmigaPouetDownloader/blob/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92/amiga/parse_prod.c) · [source 4](https://github.com/Ozzyboshi/AmigaPouetDownloader/blob/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92/httpserver/server.js) · [source 5](https://github.com/Ozzyboshi/AmigaPouetDownloader/blob/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92/amiga/compilaparseprod.sh) · [source 6](https://github.com/Ozzyboshi/AmigaPouetDownloader/blob/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92/httpserver/package.json) · [source 7](https://api.github.com/repos/Ozzyboshi/AmigaPouetDownloader/commits?per_page=30&page=1)

**Lineage and rights (reviewed):** Native Amiga organizer plus a Node HTTP-to-HTTPS helper are one application. No explicit project license was found. The relay listens without authentication and sets rejectUnauthorized:false; upstream warns against public exposure. These security limits and separate demo/content rights remain prominent. License/asset review: No project license found in inspected tree/source/README; source availability alone is not an open-source grant. Wider author/dependency graphs remain partial.

Evidence: [source 1](https://github.com/Ozzyboshi/AmigaPouetDownloader/blob/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92/README.md) · [source 2](https://github.com/Ozzyboshi/AmigaPouetDownloader/blob/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92/amiga/pouet.rexx) · [source 3](https://github.com/Ozzyboshi/AmigaPouetDownloader/blob/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92/amiga/parse_prod.c) · [source 4](https://github.com/Ozzyboshi/AmigaPouetDownloader/blob/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92/httpserver/server.js) · [source 5](https://github.com/Ozzyboshi/AmigaPouetDownloader/blob/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92/amiga/compilaparseprod.sh) · [source 6](https://github.com/Ozzyboshi/AmigaPouetDownloader/blob/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92/httpserver/package.json) · [source 7](https://api.github.com/repos/Ozzyboshi/AmigaPouetDownloader/git/commits/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92)

Documented profiles: [{"name": "Documented classic-Amiga downloader setup", "platform": "Amiga", "min_ram_kib": 1024, "notes": "README states 1 MB RAM, hard disk, TCP/IP and network access to a modern helper. It separately recommends at least 8 MB Fast RAM when using a RAM disk; that recommendation is not a universal minimum. Auxiliary binaries must match the actual CPU. No runtime test.", "evidence": ["https://github.com/Ozzyboshi/AmigaPouetDownloader/blob/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92/README.md", "https://github.com/Ozzyboshi/AmigaPouetDownloader/blob/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92/amiga/parse_prod.c"]}, {"name": "Modern helper service", "platform": "Linux", "notes": "README specifies an internet-connected modern PC with Docker/Compose, tested on Ubuntu, reachable from the Amiga on the configured port. No CPU/RAM minimum is asserted here; keep relay private because it is unauthenticated and disables upstream certificate validation.", "evidence": ["https://github.com/Ozzyboshi/AmigaPouetDownloader/blob/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92/README.md", "https://github.com/Ozzyboshi/AmigaPouetDownloader/blob/f6112eb3e97bafe34348f8953d22bdfc5cfe9a92/httpserver/server.js"]}]

### ALSFS — Amiga/Linux serial filesystem suite

[Repository](https://github.com/Ozzyboshi/alsfsAmigaServer)

- Source platforms: Amiga
- Target platforms: Amiga, Linux
- Source CPU: Unasserted / not applicable
- Target CPU: Unasserted / not applicable
- Source material/language: Unasserted / not applicable
- Maintained language: C, JavaScript, ARexx
- Classification: tooling; disk-filesystem-tool
- Build flags: all unknown (compilable, runnable, playable and byte_exact).
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** One multi-repository suite that exposes real Amiga files and floppy images to Linux over a null-modem serial link. Canonical root https://github.com/Ozzyboshi/alsfsAmigaServer was screened against the fresh 1621-project baseline and 1861-root union including prior sources, decisions and reviews. Source snapshot: commit 22e5391e13533659e906763d894c0988abc2d0ae; actual root Git tree fa5529af77361da2e5ff815629186d8e6a5c3fa0 verified through https://api.github.com/repos/Ozzyboshi/alsfsAmigaServer/git/commits/22e5391e13533659e906763d894c0988abc2d0ae.

Evidence: [source 1](https://github.com/Ozzyboshi/alsfsAmigaServer/blob/22e5391e13533659e906763d894c0988abc2d0ae/alsfssrv.c) · [source 2](https://github.com/Ozzyboshi/alsfsAmigaServer/blob/22e5391e13533659e906763d894c0988abc2d0ae/amiga_operations.c) · [source 3](https://github.com/Ozzyboshi/alsfsAmigaServer) · [source 4](https://api.github.com/repos/Ozzyboshi/alsfsAmigaServer/git/commits/22e5391e13533659e906763d894c0988abc2d0ae)

**Classification (reviewed):** Classified as tooling with native Amiga serial filesystem application and host integration. No unsupported decompilation, recovery or RE-derived method is assigned. Tool capabilities: disk-filesystem-tool. alsfssrv.c implements a resident Amiga serial command server for filesystem listing/read/write/delete/rename, ADF floppy operations and keyboard input; amiga_operations.c uses DOS and trackdisk.device APIs.

Evidence: [source 1](https://github.com/Ozzyboshi/alsfsAmigaServer/blob/22e5391e13533659e906763d894c0988abc2d0ae/alsfssrv.c) · [source 2](https://github.com/Ozzyboshi/alsfsAmigaServer/blob/22e5391e13533659e906763d894c0988abc2d0ae/amiga_operations.c) · [source 3](https://github.com/Ozzyboshi/alsfsAmigaServer/blob/22e5391e13533659e906763d894c0988abc2d0ae/Makefile)

**Source architecture (not-applicable):** This original filesystem transfer suite operates on Amiga files and disk images; no historical native binary is reconstructed. Data/filesystem content does not have a single source CPU.

Evidence: [source 1](https://github.com/Ozzyboshi/alsfsAmigaServer/blob/22e5391e13533659e906763d894c0988abc2d0ae/alsfssrv.c) · [source 2](https://github.com/Ozzyboshi/alsfsAmigaServer/blob/22e5391e13533659e906763d894c0988abc2d0ae/amiga_operations.c) · [source 3](https://github.com/Ozzyboshi/alsfsAmigaServer/blob/22e5391e13533659e906763d894c0988abc2d0ae/Makefile)

**Target architecture (needs-research):** The native-server recipe uses vbcc +kick13 and the NDK but no explicit processor-selection argument, native assembly or inspected executable header establishes a target ISA independently in this bounded review. No Linux/Node host ISA is inferred. target_cpu stays empty pending stronger primary evidence.

Evidence: [source 1](https://github.com/Ozzyboshi/alsfsAmigaServer/blob/22e5391e13533659e906763d894c0988abc2d0ae/Makefile) · [source 2](https://github.com/Ozzyboshi/alsfsAmigaServer/blob/22e5391e13533659e906763d894c0988abc2d0ae/alsfssrv.c) · [source 3](https://github.com/Ozzyboshi/alsfsAmigaServer/blob/22e5391e13533659e906763d894c0988abc2d0ae/amiga_operations.c)

**Build and verification (reviewed):** Makefile compiles the Amiga server with vbcc +kick13 and hardcoded /data paths. Linux FUSE client uses autotools and curl/json-c/crypto/zip/magic; Node serial bridge is separate. The documented ARexx bootstrap requires Workbench 2.1 despite +kick13. No filesystem operations or disk writes were performed. All four build flags are null. No independent successful build, execution, gameplay or byte-exact result is claimed.

Evidence: [source 1](https://github.com/Ozzyboshi/alsfsAmigaServer/blob/22e5391e13533659e906763d894c0988abc2d0ae/Makefile) · [source 2](https://github.com/Ozzyboshi/alsfsAmigaServer/blob/22e5391e13533659e906763d894c0988abc2d0ae/alsfssrv.c)

**Runtime requirements (reviewed):** Author reports use on an unexpanded A600 with 1 MB Chip RAM; that successful setup is not converted into an independently verified minimum. Documented serial link uses a null-modem cable at 19200 baud. Workbench 1.3 lacks the required ARexx bootstrap.

Evidence: [source 1](https://github.com/Ozzyboshi/alsfsAmigaServer/blob/22e5391e13533659e906763d894c0988abc2d0ae/alsfssrv.c) · [source 2](https://github.com/Ozzyboshi/alsfsAmigaServer/blob/22e5391e13533659e906763d894c0988abc2d0ae/amiga_operations.c) · [source 3](https://github.com/Ozzyboshi/alsfsAmigaServer/blob/22e5391e13533659e906763d894c0988abc2d0ae/Makefile) · [source 4](https://github.com/Ozzyboshi/alsfsdocumentation/blob/424389ac464ddba14161cd17cd25f6a110e14d4e/docs/index.md) · [source 5](https://github.com/Ozzyboshi/alsfsdocumentation/blob/424389ac464ddba14161cd17cd25f6a110e14d4e/docs/install.md)

**AI attribution (no-evidence-found):** No explicit generative-AI attribution found in the selected README, source, build, license evidence or 22 recent commit messages. This bounded review is not proof of non-use. Generic provider domains and gameplay AI are not tool attribution. Generic provider/model mentions, ordinary gameplay AI and future hypothetical uses are not named-tool attribution.

Evidence: [source 1](https://github.com/Ozzyboshi/alsfsAmigaServer/blob/22e5391e13533659e906763d894c0988abc2d0ae/alsfssrv.c) · [source 2](https://github.com/Ozzyboshi/alsfsAmigaServer/blob/22e5391e13533659e906763d894c0988abc2d0ae/amiga_operations.c) · [source 3](https://github.com/Ozzyboshi/alsfsAmigaServer/blob/22e5391e13533659e906763d894c0988abc2d0ae/Makefile) · [source 4](https://api.github.com/repos/Ozzyboshi/alsfsAmigaServer/commits?per_page=30&page=1)

**Lineage and rights (reviewed):** alsfsAmigaServer, alsfs Linux FUSE client, alsfsNodejsServer and alsfsdocumentation are one counted suite. Amiga server licensing is unclear, Linux client explicitly GPLv3 and Node metadata GPL-2.0. Trusted/private deployment is appropriate given HTTP exposure and destructive file/disk operations; no security assurance is implied. License/asset review: Amiga server: no explicit license found. Related Linux client: GPLv3; Node package: GPL-2.0 metadata. Preserve this mixed/unclear component status. Wider author/dependency graphs remain partial.

Evidence: [source 1](https://github.com/Ozzyboshi/alsfsAmigaServer/blob/22e5391e13533659e906763d894c0988abc2d0ae/alsfssrv.c) · [source 2](https://github.com/Ozzyboshi/alsfsAmigaServer/blob/22e5391e13533659e906763d894c0988abc2d0ae/amiga_operations.c) · [source 3](https://github.com/Ozzyboshi/alsfsAmigaServer/blob/22e5391e13533659e906763d894c0988abc2d0ae/Makefile) · [source 4](https://github.com/Ozzyboshi/alsfsdocumentation/blob/22e5391e13533659e906763d894c0988abc2d0ae/docs/index.md) · [source 5](https://github.com/Ozzyboshi/alsfsdocumentation/blob/22e5391e13533659e906763d894c0988abc2d0ae/docs/alsfssrv.md) · [source 6](https://github.com/Ozzyboshi/alsfs/blob/22e5391e13533659e906763d894c0988abc2d0ae/src/alsfs.c) · [source 7](https://github.com/Ozzyboshi/alsfs/blob/22e5391e13533659e906763d894c0988abc2d0ae/configure.ac) · [source 8](https://github.com/Ozzyboshi/alsfsNodejsServer/blob/22e5391e13533659e906763d894c0988abc2d0ae/package.json) · [source 9](https://api.github.com/repos/Ozzyboshi/alsfsAmigaServer/git/commits/22e5391e13533659e906763d894c0988abc2d0ae) · [source 10](https://github.com/Ozzyboshi/alsfs) · [source 11](https://github.com/Ozzyboshi/alsfsNodejsServer) · [source 12](https://github.com/Ozzyboshi/alsfsdocumentation)

Documented profiles: [{"name": "Documented ALSFS bootstrap workflow", "platform": "Amiga", "os": "Workbench 2.1 with ARexx for documented bootstrap", "notes": "Author reports use on an unexpanded A600 with 1 MB Chip RAM; that successful setup is not converted into an independently verified minimum. Documented serial link uses a null-modem cable at 19200 baud. Workbench 1.3 lacks the required ARexx bootstrap.", "evidence": ["https://github.com/Ozzyboshi/alsfsdocumentation/blob/424389ac464ddba14161cd17cd25f6a110e14d4e/docs/index.md", "https://github.com/Ozzyboshi/alsfsdocumentation/blob/424389ac464ddba14161cd17cd25f6a110e14d4e/docs/install.md"]}]

### Fatma — Amiga keymap Hunk-file editor

[Repository](https://github.com/weiju/fatma)

- Source platforms: Amiga
- Target platforms: Windows, Linux, macOS
- Source CPU: Unasserted / not applicable
- Target CPU: Unasserted / not applicable
- Source material/language: Unasserted / not applicable
- Maintained language: Scala
- Classification: tooling; data-format-analysis, asset-tool
- Build flags: all unknown (compilable, runnable, playable and byte_exact).
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Scala/JVM graphical editor and serializer for real AmigaOS keymap Hunk files. Canonical root https://github.com/weiju/fatma was screened against the fresh 1621-project baseline and 1861-root union including prior sources, decisions and reviews. Source snapshot: commit 063185672474114c67a0505fc87a98193522d783; actual root Git tree 4a2ff0f829e639bcd3384d4c3819bfe50a72be0e verified through https://api.github.com/repos/weiju/fatma/git/commits/063185672474114c67a0505fc87a98193522d783.

Evidence: [source 1](https://github.com/weiju/fatma/blob/063185672474114c67a0505fc87a98193522d783/README.md) · [source 2](https://github.com/weiju/fatma/blob/063185672474114c67a0505fc87a98193522d783/manual) · [source 3](https://github.com/weiju/fatma/blob/063185672474114c67a0505fc87a98193522d783/src/main/scala/org/dmpp/os/devices/KeymapReader.scala) · [source 4](https://github.com/weiju/fatma/blob/063185672474114c67a0505fc87a98193522d783/src/main/scala/org/dmpp/os/devices/KeymapWriter.scala) · [source 5](https://github.com/weiju/fatma) · [source 6](https://api.github.com/repos/weiju/fatma/git/commits/063185672474114c67a0505fc87a98193522d783)

**Classification (reviewed):** Classified as tooling with Amiga keymap reconstruction/editor tooling. Methods: data-format-analysis. Tool capabilities: asset-tool. README describes learning Amiga keymap layout/OS concepts to create a Colemak keymap; the resulting resource is copied to DEVS:keymaps.

Evidence: [source 1](https://github.com/weiju/fatma/blob/063185672474114c67a0505fc87a98193522d783/README.md) · [source 2](https://github.com/weiju/fatma/blob/063185672474114c67a0505fc87a98193522d783/manual) · [source 3](https://github.com/weiju/fatma/blob/063185672474114c67a0505fc87a98193522d783/src/main/scala/org/dmpp/os/devices/KeymapReader.scala) · [source 4](https://github.com/weiju/fatma/blob/063185672474114c67a0505fc87a98193522d783/src/main/scala/org/dmpp/os/devices/KeymapWriter.scala) · [source 5](https://github.com/weiju/fatma/blob/063185672474114c67a0505fc87a98193522d783/build.sbt)

**Source architecture (not-applicable):** KeymapReader/Writer inspect and serialize AmigaOS Hunk keymap structures and relocation data, not executable game code. The format is the Amiga relationship; it does not supply a source CPU.

Evidence: [source 1](https://github.com/weiju/fatma/blob/063185672474114c67a0505fc87a98193522d783/README.md) · [source 2](https://github.com/weiju/fatma/blob/063185672474114c67a0505fc87a98193522d783/manual) · [source 3](https://github.com/weiju/fatma/blob/063185672474114c67a0505fc87a98193522d783/src/main/scala/org/dmpp/os/devices/KeymapReader.scala) · [source 4](https://github.com/weiju/fatma/blob/063185672474114c67a0505fc87a98193522d783/src/main/scala/org/dmpp/os/devices/KeymapWriter.scala) · [source 5](https://github.com/weiju/fatma/blob/063185672474114c67a0505fc87a98193522d783/build.sbt)

**Target architecture (no-evidence-found):** Scala/JVM execution and generated keymap data establish no native host ISA or machine-code target. Windows/Linux/macOS are documented application hosts; Amiga receives data files under DEVS:keymaps.

Evidence: [source 1](https://github.com/weiju/fatma/blob/063185672474114c67a0505fc87a98193522d783/build.sbt) · [source 2](https://github.com/weiju/fatma/blob/063185672474114c67a0505fc87a98193522d783/README.md) · [source 3](https://github.com/weiju/fatma/blob/063185672474114c67a0505fc87a98193522d783/manual) · [source 4](https://github.com/weiju/fatma/blob/063185672474114c67a0505fc87a98193522d783/src/main/scala/org/dmpp/os/devices/KeymapReader.scala) · [source 5](https://github.com/weiju/fatma/blob/063185672474114c67a0505fc87a98193522d783/src/main/scala/org/dmpp/os/devices/KeymapWriter.scala)

**Build and verification (reviewed):** build.sbt selects Scala 2.11.6 and sbt-assembly. The older manual mentions Scala 2.9, Java 6+ and sbt 0.10; those statements do not prove compatibility of the checked build. No keymap was generated, loaded or tested. All four build flags are null. No independent successful build, execution, gameplay or byte-exact result is claimed.

Evidence: [source 1](https://github.com/weiju/fatma/blob/063185672474114c67a0505fc87a98193522d783/build.sbt) · [source 2](https://github.com/weiju/fatma/blob/063185672474114c67a0505fc87a98193522d783/README.md)

**Runtime requirements (no-evidence-found):** Selected primary material does not establish a sufficiently explicit output-specific hardware minimum. No profile is populated: build flags, guest models, development machines and historical test anecdotes are not extrapolated into verified CPU/RAM/chipset/OS minima.

Evidence: [source 1](https://github.com/weiju/fatma/blob/063185672474114c67a0505fc87a98193522d783/README.md) · [source 2](https://github.com/weiju/fatma/blob/063185672474114c67a0505fc87a98193522d783/manual) · [source 3](https://github.com/weiju/fatma/blob/063185672474114c67a0505fc87a98193522d783/src/main/scala/org/dmpp/os/devices/KeymapReader.scala) · [source 4](https://github.com/weiju/fatma/blob/063185672474114c67a0505fc87a98193522d783/src/main/scala/org/dmpp/os/devices/KeymapWriter.scala) · [source 5](https://github.com/weiju/fatma/blob/063185672474114c67a0505fc87a98193522d783/build.sbt)

**AI attribution (no-evidence-found):** No explicit generative-AI attribution found in the selected README, source, build, license evidence or 15 recent commit messages. This bounded review is not proof of non-use. Generic provider domains and gameplay AI are not tool attribution. Generic provider/model mentions, ordinary gameplay AI and future hypothetical uses are not named-tool attribution.

Evidence: [source 1](https://github.com/weiju/fatma/blob/063185672474114c67a0505fc87a98193522d783/README.md) · [source 2](https://github.com/weiju/fatma/blob/063185672474114c67a0505fc87a98193522d783/manual) · [source 3](https://github.com/weiju/fatma/blob/063185672474114c67a0505fc87a98193522d783/src/main/scala/org/dmpp/os/devices/KeymapReader.scala) · [source 4](https://github.com/weiju/fatma/blob/063185672474114c67a0505fc87a98193522d783/src/main/scala/org/dmpp/os/devices/KeymapWriter.scala) · [source 5](https://github.com/weiju/fatma/blob/063185672474114c67a0505fc87a98193522d783/build.sbt) · [source 6](https://api.github.com/repos/weiju/fatma/commits?per_page=30&page=1)

**Lineage and rights (reviewed):** Original purpose-built keymap editor with explicit GPLv3 README and LICENSE. Its relation to Amiga is the documented format/deployment workflow, not a native Amiga executable. Output OS/dead-key compatibility remains unverified. License/asset review: GPL version 3 explicitly named in README and supplied as LICENSE. Wider author/dependency graphs remain partial.

Evidence: [source 1](https://github.com/weiju/fatma/blob/063185672474114c67a0505fc87a98193522d783/README.md) · [source 2](https://github.com/weiju/fatma/blob/063185672474114c67a0505fc87a98193522d783/manual) · [source 3](https://github.com/weiju/fatma/blob/063185672474114c67a0505fc87a98193522d783/src/main/scala/org/dmpp/os/devices/KeymapReader.scala) · [source 4](https://github.com/weiju/fatma/blob/063185672474114c67a0505fc87a98193522d783/src/main/scala/org/dmpp/os/devices/KeymapWriter.scala) · [source 5](https://github.com/weiju/fatma/blob/063185672474114c67a0505fc87a98193522d783/build.sbt) · [source 6](https://github.com/weiju/fatma/blob/063185672474114c67a0505fc87a98193522d783/LICENSE) · [source 7](https://api.github.com/repos/weiju/fatma/git/commits/063185672474114c67a0505fc87a98193522d783)

### amigados-utils — Amiga disk and Hunk development tools

[Repository](https://github.com/weiju/amigados-utils)

- Source platforms: Amiga
- Target platforms: Unix
- Source CPU: m68000
- Target CPU: Unasserted / not applicable
- Source material/language: m68000 machine code, Amiga Hunk binaries, Amiga disk images
- Maintained language: Python
- Classification: tooling; binary-analysis, data-format-analysis, disk-filesystem-tool, binary-analysis, disassembler, asset-tool
- Build flags: all unknown (compilable, runnable, playable and byte_exact).
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Python command-line suite for manipulating Amiga disk images, viewing/disassembling Hunk binaries and preparing native-development inputs. Canonical root https://github.com/weiju/amigados-utils was screened against the fresh 1621-project baseline and 1861-root union including prior sources, decisions and reviews. Source snapshot: commit 67a129228aa545ac2857df34150ffbe1539a8c62; actual root Git tree 02b6e0c0e9489bb478d38ca42a7b9ac41a4dcfba verified through https://api.github.com/repos/weiju/amigados-utils/git/commits/67a129228aa545ac2857df34150ffbe1539a8c62.

Evidence: [source 1](https://github.com/weiju/amigados-utils/blob/67a129228aa545ac2857df34150ffbe1539a8c62/README.md) · [source 2](https://github.com/weiju/amigados-utils/blob/67a129228aa545ac2857df34150ffbe1539a8c62/amigados/adftools/logical.py) · [source 3](https://github.com/weiju/amigados-utils/blob/67a129228aa545ac2857df34150ffbe1539a8c62/amigados/hunktools/dalf.py) · [source 4](https://github.com/weiju/amigados-utils/blob/67a129228aa545ac2857df34150ffbe1539a8c62/amigados/vm/disassemble.py) · [source 5](https://github.com/weiju/amigados-utils) · [source 6](https://api.github.com/repos/weiju/amigados-utils/git/commits/67a129228aa545ac2857df34150ffbe1539a8c62)

**Classification (reviewed):** Classified as tooling with Amiga binary/filesystem development toolkit. Methods: binary-analysis, data-format-analysis. Tool capabilities: disk-filesystem-tool, binary-analysis, disassembler, asset-tool. README names ADF/HDF creation and filesystem commands, FD/BumpRev replacements, Hunk inspection and PNG conversion for Amiga system development.

Evidence: [source 1](https://github.com/weiju/amigados-utils/blob/67a129228aa545ac2857df34150ffbe1539a8c62/README.md) · [source 2](https://github.com/weiju/amigados-utils/blob/67a129228aa545ac2857df34150ffbe1539a8c62/amigados/adftools/logical.py) · [source 3](https://github.com/weiju/amigados-utils/blob/67a129228aa545ac2857df34150ffbe1539a8c62/amigados/hunktools/dalf.py) · [source 4](https://github.com/weiju/amigados-utils/blob/67a129228aa545ac2857df34150ffbe1539a8c62/amigados/vm/disassemble.py) · [source 5](https://github.com/weiju/amigados-utils/blob/67a129228aa545ac2857df34150ffbe1539a8c62/setup.py)

**Source architecture (reviewed):** amigados/vm/disassemble.py explicitly constructs Capstone CS_ARCH_M68K with CS_MODE_M68K_000 for Hunk code. source_cpu=m68000 refers to the native instruction input being analysed, not the Python host or CPU of arbitrary disk-image contents.

Evidence: [source 1](https://github.com/weiju/amigados-utils/blob/67a129228aa545ac2857df34150ffbe1539a8c62/README.md) · [source 2](https://github.com/weiju/amigados-utils/blob/67a129228aa545ac2857df34150ffbe1539a8c62/amigados/adftools/logical.py) · [source 3](https://github.com/weiju/amigados-utils/blob/67a129228aa545ac2857df34150ffbe1539a8c62/amigados/hunktools/dalf.py) · [source 4](https://github.com/weiju/amigados-utils/blob/67a129228aa545ac2857df34150ffbe1539a8c62/amigados/vm/disassemble.py) · [source 5](https://github.com/weiju/amigados-utils/blob/67a129228aa545ac2857df34150ffbe1539a8c62/setup.py)

**Target architecture (no-evidence-found):** Python tools inspect binaries and generate filesystem/asset data; no native host triple or generated machine-code ISA was established. target_cpu is empty rather than inferred from Unix.

Evidence: [source 1](https://github.com/weiju/amigados-utils/blob/67a129228aa545ac2857df34150ffbe1539a8c62/setup.py) · [source 2](https://github.com/weiju/amigados-utils/blob/67a129228aa545ac2857df34150ffbe1539a8c62/README.md) · [source 3](https://github.com/weiju/amigados-utils/blob/67a129228aa545ac2857df34150ffbe1539a8c62/amigados/adftools/logical.py) · [source 4](https://github.com/weiju/amigados-utils/blob/67a129228aa545ac2857df34150ffbe1539a8c62/amigados/hunktools/dalf.py) · [source 5](https://github.com/weiju/amigados-utils/blob/67a129228aa545ac2857df34150ffbe1539a8c62/amigados/vm/disassemble.py)

**Build and verification (reviewed):** setup.py supplies command scripts and Pillow/Jinja2/Capstone dependencies. fdtool is marked just started; recent history records migration to Capstone. No package install, ADF edit, disassembly run or test was performed. All four build flags are null. No independent successful build, execution, gameplay or byte-exact result is claimed.

Evidence: [source 1](https://github.com/weiju/amigados-utils/blob/67a129228aa545ac2857df34150ffbe1539a8c62/setup.py) · [source 2](https://github.com/weiju/amigados-utils/blob/67a129228aa545ac2857df34150ffbe1539a8c62/README.md)

**Runtime requirements (no-evidence-found):** Selected primary material does not establish a sufficiently explicit output-specific hardware minimum. No profile is populated: build flags, guest models, development machines and historical test anecdotes are not extrapolated into verified CPU/RAM/chipset/OS minima.

Evidence: [source 1](https://github.com/weiju/amigados-utils/blob/67a129228aa545ac2857df34150ffbe1539a8c62/README.md) · [source 2](https://github.com/weiju/amigados-utils/blob/67a129228aa545ac2857df34150ffbe1539a8c62/amigados/adftools/logical.py) · [source 3](https://github.com/weiju/amigados-utils/blob/67a129228aa545ac2857df34150ffbe1539a8c62/amigados/hunktools/dalf.py) · [source 4](https://github.com/weiju/amigados-utils/blob/67a129228aa545ac2857df34150ffbe1539a8c62/amigados/vm/disassemble.py) · [source 5](https://github.com/weiju/amigados-utils/blob/67a129228aa545ac2857df34150ffbe1539a8c62/setup.py)

**AI attribution (no-evidence-found):** No explicit generative-AI attribution found in the selected README, source, build, license evidence or 30 recent commit messages. This bounded review is not proof of non-use. Generic provider domains and gameplay AI are not tool attribution. Generic provider/model mentions, ordinary gameplay AI and future hypothetical uses are not named-tool attribution.

Evidence: [source 1](https://github.com/weiju/amigados-utils/blob/67a129228aa545ac2857df34150ffbe1539a8c62/README.md) · [source 2](https://github.com/weiju/amigados-utils/blob/67a129228aa545ac2857df34150ffbe1539a8c62/amigados/adftools/logical.py) · [source 3](https://github.com/weiju/amigados-utils/blob/67a129228aa545ac2857df34150ffbe1539a8c62/amigados/hunktools/dalf.py) · [source 4](https://github.com/weiju/amigados-utils/blob/67a129228aa545ac2857df34150ffbe1539a8c62/amigados/vm/disassemble.py) · [source 5](https://github.com/weiju/amigados-utils/blob/67a129228aa545ac2857df34150ffbe1539a8c62/setup.py) · [source 6](https://api.github.com/repos/weiju/amigados-utils/commits?per_page=30&page=1)

**Lineage and rights (reviewed):** One Python development suite. Related earlier Scala ADF Tools/Arr!Jay is retained as an unpromoted related-tool lead pending deliberate identity/lineage review; no unsupported claim of exact derivation. BSD-3-Clause LICENSE conflicts with a GPLv3 package classifier, and bundled Workbench 1.3 disk-image rights remain separate. License/asset review: BSD-3-Clause LICENSE and BSD setup field, with contradictory GPLv3 classifier; bundled Workbench image rights separate. Wider author/dependency graphs remain partial.

Evidence: [source 1](https://github.com/weiju/amigados-utils/blob/67a129228aa545ac2857df34150ffbe1539a8c62/README.md) · [source 2](https://github.com/weiju/amigados-utils/blob/67a129228aa545ac2857df34150ffbe1539a8c62/amigados/adftools/logical.py) · [source 3](https://github.com/weiju/amigados-utils/blob/67a129228aa545ac2857df34150ffbe1539a8c62/amigados/hunktools/dalf.py) · [source 4](https://github.com/weiju/amigados-utils/blob/67a129228aa545ac2857df34150ffbe1539a8c62/amigados/vm/disassemble.py) · [source 5](https://github.com/weiju/amigados-utils/blob/67a129228aa545ac2857df34150ffbe1539a8c62/setup.py) · [source 6](https://github.com/weiju/amigados-utils/blob/67a129228aa545ac2857df34150ffbe1539a8c62/LICENSE) · [source 7](https://api.github.com/repos/weiju/amigados-utils/git/commits/67a129228aa545ac2857df34150ffbe1539a8c62) · [source 8](https://github.com/weiju/adf-tools)

### DMPP — Amiga hardware research and visual emulator

[Repository](https://github.com/weiju/dmpp)

- Source platforms: Amiga
- Target platforms: Desktop
- Source CPU: Unasserted / not applicable
- Target CPU: Unasserted / not applicable
- Source material/language: Unasserted / not applicable
- Maintained language: Scala
- Classification: tooling; reimplementation, emulator, graphics-debugger, cycle-analysis
- Build flags: all unknown (compilable, runnable, playable and byte_exact).
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Scala Amiga hardware/emulator research with custom-chip/DMA models and visual debugger, independent of a particular game. Canonical root https://github.com/weiju/dmpp was screened against the fresh 1621-project baseline and 1861-root union including prior sources, decisions and reviews. Source snapshot: commit c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1; actual root Git tree 8467fcadc2380e8da9ec975780681b18bf439df9 verified through https://api.github.com/repos/weiju/dmpp/git/commits/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1.

Evidence: [source 1](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/README.md) · [source 2](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/scala/dmpp-board/src/main/scala/org/dmpp/amiga/AmigaBoard.scala) · [source 3](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/scala/dmpp-board/src/main/scala/org/dmpp/amiga/Copper.scala) · [source 4](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/scala/dmpp-debugger/src/main/scala/org/dmpp/debugger/Main.scala) · [source 5](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/scala/dmpp-cpu/README) · [source 6](https://github.com/weiju/dmpp) · [source 7](https://api.github.com/repos/weiju/dmpp/git/commits/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1)

**Classification (reviewed):** Classified as tooling with general Amiga emulator and hardware-research implementation. Methods: reimplementation. Tool capabilities: emulator, graphics-debugger, cycle-analysis. README frames this as a research project that may become a real emulator and claims it can run a significant portion of Kickstart 1.3 code.

Evidence: [source 1](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/README.md) · [source 2](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/scala/dmpp-board/src/main/scala/org/dmpp/amiga/AmigaBoard.scala) · [source 3](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/scala/dmpp-board/src/main/scala/org/dmpp/amiga/Copper.scala) · [source 4](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/scala/dmpp-debugger/src/main/scala/org/dmpp/debugger/Main.scala) · [source 5](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/scala/dmpp-cpu/README) · [source 6](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/scala/build.sbt) · [source 7](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/scala/project/Build.scala) · [source 8](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/scala/project/build.properties)

**Source architecture (not-applicable):** Original general hardware-model research, not a recovered native game/ROM source listing. The emulated 68000 guest and external Kickstart 1.3 subject are explained in notes; source_cpu is not inferred from the Amiga name or claims of partial ROM execution.

Evidence: [source 1](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/README.md) · [source 2](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/scala/dmpp-board/src/main/scala/org/dmpp/amiga/AmigaBoard.scala) · [source 3](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/scala/dmpp-board/src/main/scala/org/dmpp/amiga/Copper.scala) · [source 4](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/scala/dmpp-debugger/src/main/scala/org/dmpp/debugger/Main.scala) · [source 5](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/scala/dmpp-cpu/README) · [source 6](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/scala/build.sbt) · [source 7](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/scala/project/Build.scala) · [source 8](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/scala/project/build.properties)

**Target architecture (no-evidence-found):** Scala/JVM debugger and emulator modules do not establish a native host target ISA. The modeled 68000 is a guest architecture, not target_cpu for the host executable.

Evidence: [source 1](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/scala/build.sbt) · [source 2](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/scala/project/Build.scala) · [source 3](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/scala/project/build.properties) · [source 4](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/README.md) · [source 5](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/scala/dmpp-board/src/main/scala/org/dmpp/amiga/AmigaBoard.scala) · [source 6](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/scala/dmpp-board/src/main/scala/org/dmpp/amiga/Copper.scala) · [source 7](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/scala/dmpp-debugger/src/main/scala/org/dmpp/debugger/Main.scala) · [source 8](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/scala/dmpp-cpu/README)

**Build and verification (reviewed):** Current build uses Scala 2.11.8 and sbt 0.13.13. AmigaBoard imports org.mahatma68k.Cpu while the inspected dependency file lists only tests/Swing, leaving clean-build setup unresolved. Source models 512 KiB Chip RAM; the adjacent 512-megabytes comment is erroneous. No ROM or emulator was executed. All four build flags are null. No independent successful build, execution, gameplay or byte-exact result is claimed.

Evidence: [source 1](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/scala/build.sbt) · [source 2](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/scala/project/Build.scala) · [source 3](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/scala/project/build.properties) · [source 4](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/README.md)

**Runtime requirements (no-evidence-found):** Selected primary material does not establish a sufficiently explicit output-specific hardware minimum. No profile is populated: build flags, guest models, development machines and historical test anecdotes are not extrapolated into verified CPU/RAM/chipset/OS minima.

Evidence: [source 1](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/README.md) · [source 2](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/scala/dmpp-board/src/main/scala/org/dmpp/amiga/AmigaBoard.scala) · [source 3](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/scala/dmpp-board/src/main/scala/org/dmpp/amiga/Copper.scala) · [source 4](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/scala/dmpp-debugger/src/main/scala/org/dmpp/debugger/Main.scala) · [source 5](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/scala/dmpp-cpu/README) · [source 6](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/scala/build.sbt) · [source 7](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/scala/project/Build.scala) · [source 8](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/scala/project/build.properties)

**AI attribution (no-evidence-found):** No explicit generative-AI attribution found in the selected README, source, build, license evidence or 30 recent commit messages. This bounded review is not proof of non-use. Generic provider domains and gameplay AI are not tool attribution. Generic provider/model mentions, ordinary gameplay AI and future hypothetical uses are not named-tool attribution.

Evidence: [source 1](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/README.md) · [source 2](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/scala/dmpp-board/src/main/scala/org/dmpp/amiga/AmigaBoard.scala) · [source 3](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/scala/dmpp-board/src/main/scala/org/dmpp/amiga/Copper.scala) · [source 4](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/scala/dmpp-debugger/src/main/scala/org/dmpp/debugger/Main.scala) · [source 5](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/scala/dmpp-cpu/README) · [source 6](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/scala/build.sbt) · [source 7](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/scala/project/Build.scala) · [source 8](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/scala/project/build.properties) · [source 9](https://api.github.com/repos/weiju/dmpp/commits?per_page=30&page=1)

**Lineage and rights (reviewed):** Generic partial Amiga emulator research is eligible as tooling, unlike excluded game-specific CPU wrappers. BSD-3-Clause-style notices are in inspected board/Copper/debugger code; no root license and no rights to external Kickstart ROMs are inferred. Related spin-off tools are not extra project counts. License/asset review: BSD-3-Clause-style notices explicitly in inspected board/Copper/debugger sources; no root license detected. Wider author/dependency graphs remain partial.

Evidence: [source 1](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/README.md) · [source 2](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/scala/dmpp-board/src/main/scala/org/dmpp/amiga/AmigaBoard.scala) · [source 3](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/scala/dmpp-board/src/main/scala/org/dmpp/amiga/Copper.scala) · [source 4](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/scala/dmpp-debugger/src/main/scala/org/dmpp/debugger/Main.scala) · [source 5](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/scala/dmpp-cpu/README) · [source 6](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/scala/build.sbt) · [source 7](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/scala/project/Build.scala) · [source 8](https://github.com/weiju/dmpp/blob/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1/scala/project/build.properties) · [source 9](https://api.github.com/repos/weiju/dmpp/git/commits/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1)

### BlitzWays — original Amiga tile-puzzle source

[Repository](https://github.com/wertstahl/blitzways)

- Source platforms: Amiga
- Target platforms: Amiga
- Source CPU: Unasserted / not applicable
- Target CPU: Unasserted / not applicable
- Source material/language: Blitz Basic 2
- Maintained language: Blitz Basic 2
- Classification: subject; game
- Build flags: all unknown (compilable, runnable, playable and byte_exact).
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** A substantial native Blitz Basic tile-pair puzzle begun in 1992 and completed in 2020, with editable source, assets and disk/file releases. Canonical root https://github.com/wertstahl/blitzways was screened against the fresh 1621-project baseline and 1861-root union including prior sources, decisions and reviews. Source snapshot: commit 4fa00f788204a6c71983779df0d3bf0b45967af9; actual root Git tree 296689e25cf2702149748a28eae3baef1d9a845a verified through https://api.github.com/repos/wertstahl/blitzways/git/commits/4fa00f788204a6c71983779df0d3bf0b45967af9.

Evidence: [source 1](https://github.com/wertstahl/blitzways/blob/4fa00f788204a6c71983779df0d3bf0b45967af9/README.md) · [source 2](https://github.com/wertstahl/blitzways/blob/4fa00f788204a6c71983779df0d3bf0b45967af9/Manual.readme) · [source 3](https://github.com/wertstahl/blitzways/blob/4fa00f788204a6c71983779df0d3bf0b45967af9/src/VisualStudioCodeSrc/Ways1.30.VSC.bb2) · [source 4](https://github.com/wertstahl/blitzways) · [source 5](https://api.github.com/repos/wertstahl/blitzways/git/commits/4fa00f788204a6c71983779df0d3bf0b45967af9)

**Classification (reviewed):** Classified as subject with original-source Amiga tile-puzzle game. No unsupported decompilation, recovery or RE-derived method is assigned. The 6,446-line editable source implements boot/resource loading, level selection and tutorials, tile validation, pathfinding, tile removal, end-of-level state, score persistence and autoplay; it is a complete game implementation rather than a rendering example.

Evidence: [source 1](https://github.com/wertstahl/blitzways/blob/4fa00f788204a6c71983779df0d3bf0b45967af9/README.md) · [source 2](https://github.com/wertstahl/blitzways/blob/4fa00f788204a6c71983779df0d3bf0b45967af9/Manual.readme) · [source 3](https://github.com/wertstahl/blitzways/blob/4fa00f788204a6c71983779df0d3bf0b45967af9/src/VisualStudioCodeSrc/Ways1.30.VSC.bb2) · [source 4](https://github.com/wertstahl/blitzways/blob/4fa00f788204a6c71983779df0d3bf0b45967af9/Blitz2CompilerOptions.txt)

**Source architecture (needs-research):** Substantial editable original Blitz Basic source is preserved, with 1992 concept and later development history. Neither inspected compiler settings nor high-level source establishes a native ISA independently; source_cpu is not inferred from A500+/A1200 labels.

Evidence: [source 1](https://github.com/wertstahl/blitzways/blob/4fa00f788204a6c71983779df0d3bf0b45967af9/README.md) · [source 2](https://github.com/wertstahl/blitzways/blob/4fa00f788204a6c71983779df0d3bf0b45967af9/Manual.readme) · [source 3](https://github.com/wertstahl/blitzways/blob/4fa00f788204a6c71983779df0d3bf0b45967af9/src/VisualStudioCodeSrc/Ways1.30.VSC.bb2) · [source 4](https://github.com/wertstahl/blitzways/blob/4fa00f788204a6c71983779df0d3bf0b45967af9/Blitz2CompilerOptions.txt)

**Target architecture (needs-research):** Blitz Basic build/environment and Amiga executable releases are documented, but no explicit processor flag or output header was inspected. target_cpu remains empty; A1200 development does not prove an AGA-only or 68020-only minimum.

Evidence: [source 1](https://github.com/wertstahl/blitzways/blob/4fa00f788204a6c71983779df0d3bf0b45967af9/README.md) · [source 2](https://github.com/wertstahl/blitzways/blob/4fa00f788204a6c71983779df0d3bf0b45967af9/Blitz2CompilerOptions.txt) · [source 3](https://github.com/wertstahl/blitzways/blob/4fa00f788204a6c71983779df0d3bf0b45967af9/Manual.readme) · [source 4](https://github.com/wertstahl/blitzways/blob/4fa00f788204a6c71983779df0d3bf0b45967af9/src/VisualStudioCodeSrc/Ways1.30.VSC.bb2)

**Build and verification (reviewed):** Build requires Blitz 2 v2.1, SuperTed 2.24 and CIATrkrLib with supplied compiler limits. Editable source loads gfx/StoneSet.2020 while the tree supplies gfx/Stoneset.2025. Runtime consequences were not tested. OS 3.0 is a development environment, not the game minimum. All four build flags are null. No independent successful build, execution, gameplay or byte-exact result is claimed.

Evidence: [source 1](https://github.com/wertstahl/blitzways/blob/4fa00f788204a6c71983779df0d3bf0b45967af9/README.md) · [source 2](https://github.com/wertstahl/blitzways/blob/4fa00f788204a6c71983779df0d3bf0b45967af9/Blitz2CompilerOptions.txt)

**Runtime requirements (reviewed):** Manual states 1 MB Chip RAM and Kickstart 2.0. A500+ ECS and A1200 are upstream design targets, not a separately tested all-Amiga compatibility matrix. Development OS 3.0 requirement is distinct. No build/runtime test.

Evidence: [source 1](https://github.com/wertstahl/blitzways/blob/4fa00f788204a6c71983779df0d3bf0b45967af9/README.md) · [source 2](https://github.com/wertstahl/blitzways/blob/4fa00f788204a6c71983779df0d3bf0b45967af9/Manual.readme) · [source 3](https://github.com/wertstahl/blitzways/blob/4fa00f788204a6c71983779df0d3bf0b45967af9/src/VisualStudioCodeSrc/Ways1.30.VSC.bb2) · [source 4](https://github.com/wertstahl/blitzways/blob/4fa00f788204a6c71983779df0d3bf0b45967af9/Blitz2CompilerOptions.txt)

**AI attribution (no-evidence-found):** No explicit generative-AI usage attribution found. Manual suggests that someone could use AI for a future remake after 2045; that hypothetical is not evidence that the checked-in game used AI. Latest ten commits and selected source/readmes inspected. Generic provider/model mentions, ordinary gameplay AI and future hypothetical uses are not named-tool attribution.

Evidence: [source 1](https://github.com/wertstahl/blitzways/blob/4fa00f788204a6c71983779df0d3bf0b45967af9/README.md) · [source 2](https://github.com/wertstahl/blitzways/blob/4fa00f788204a6c71983779df0d3bf0b45967af9/Manual.readme) · [source 3](https://github.com/wertstahl/blitzways/blob/4fa00f788204a6c71983779df0d3bf0b45967af9/src/VisualStudioCodeSrc/Ways1.30.VSC.bb2) · [source 4](https://github.com/wertstahl/blitzways/blob/4fa00f788204a6c71983779df0d3bf0b45967af9/Blitz2CompilerOptions.txt) · [source 5](https://api.github.com/repos/wertstahl/blitzways/commits?per_page=10)

**Lineage and rights (reviewed):** Original title based on ISK Stone concept, not another count for its source representations or third-party cracktro. All-rights-reserved/non-redistribution source and asset notices are explicit. Catalogue links/paraphrases only; no broad rights grant or generative-AI usage inferred from a hypothetical future-AI-remake comment. License/asset review: Explicit all-rights-reserved/non-redistribution notices in README and asset readmes; GitHub reports no recognised license. Freeware runtime distribution is not an open-source grant. Wider author/dependency graphs remain partial.

Evidence: [source 1](https://github.com/wertstahl/blitzways/blob/4fa00f788204a6c71983779df0d3bf0b45967af9/README.md) · [source 2](https://github.com/wertstahl/blitzways/blob/4fa00f788204a6c71983779df0d3bf0b45967af9/Manual.readme) · [source 3](https://github.com/wertstahl/blitzways/blob/4fa00f788204a6c71983779df0d3bf0b45967af9/src/VisualStudioCodeSrc/Ways1.30.VSC.bb2) · [source 4](https://github.com/wertstahl/blitzways/blob/4fa00f788204a6c71983779df0d3bf0b45967af9/Blitz2CompilerOptions.txt) · [source 5](https://github.com/wertstahl/blitzways/blob/4fa00f788204a6c71983779df0d3bf0b45967af9/extra/extra.readme) · [source 6](https://github.com/wertstahl/blitzways/blob/4fa00f788204a6c71983779df0d3bf0b45967af9/extra/unused/copyright.readme) · [source 7](https://api.github.com/repos/wertstahl/blitzways) · [source 8](https://github.com/wertstahl/blitzways/commit/4fa00f788204a6c71983779df0d3bf0b45967af9) · [source 9](https://api.github.com/repos/wertstahl/blitzways/git/commits/4fa00f788204a6c71983779df0d3bf0b45967af9)

Documented profiles: [{"name": "Documented BlitzWays game minimum", "platform": "Amiga", "min_chip_ram_kib": 1024, "os": "Kickstart 2.0 or later", "notes": "Manual states 1 MB Chip RAM and Kickstart 2.0. A500+ ECS and A1200 are upstream design targets, not a separately tested all-Amiga compatibility matrix. Development OS 3.0 requirement is distinct. No build/runtime test.", "evidence": ["https://github.com/wertstahl/blitzways/blob/4fa00f788204a6c71983779df0d3bf0b45967af9/Manual.readme", "https://github.com/wertstahl/blitzways/blob/4fa00f788204a6c71983779df0d3bf0b45967af9/README.md"]}]

### Notegame — original Amiga music-symbol game and editor

[Repository](https://github.com/xet7/notegame)

- Source platforms: Amiga
- Target platforms: Amiga
- Source CPU: Unasserted / not applicable
- Target CPU: Unasserted / not applicable
- Source material/language: Blitz Basic 2
- Maintained language: Blitz Basic 2
- Classification: subject; game, source-restoration
- Build flags: all unknown (compilable, runnable, playable and byte_exact).
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** The authors’ preserved 1994–95 Blitz Basic music-note identification game for Amiga, with an executable, original tokenized source, readable text exports and game-definition tooling. Canonical root https://github.com/xet7/notegame was screened against the fresh 1621-project baseline and 1861-root union including prior sources, decisions and reviews. Source snapshot: commit 8b7eb4e57ad4554b49b26a0125a1424df25a2d75; actual root Git tree 50896834cafdc4276472c1e4b5e2982bb44f51a7 verified through https://api.github.com/repos/xet7/notegame/git/commits/8b7eb4e57ad4554b49b26a0125a1424df25a2d75.

Evidence: [source 1](https://github.com/xet7/notegame/blob/8b7eb4e57ad4554b49b26a0125a1424df25a2d75/README.md) · [source 2](https://github.com/xet7/notegame/blob/8b7eb4e57ad4554b49b26a0125a1424df25a2d75/CHANGELOG.md) · [source 3](https://github.com/xet7/notegame/blob/8b7eb4e57ad4554b49b26a0125a1424df25a2d75/Aika/Code/Aikaar_V0.26.txt) · [source 4](https://github.com/xet7/notegame/blob/8b7eb4e57ad4554b49b26a0125a1424df25a2d75/Aika/Code/TeePeliTP.txt) · [source 5](https://github.com/xet7/notegame) · [source 6](https://api.github.com/repos/xet7/notegame/git/commits/8b7eb4e57ad4554b49b26a0125a1424df25a2d75)

**Classification (reviewed):** Classified as subject with original-source Amiga educational music game. Methods: source-restoration. The 1,516-line Aikaar_V0.26.txt contains dated 1994–95 development notes and a v0.26 identifier dated 13 September 1995. Substantive inspected code covers requester-based player input, randomised symbol/question order, correct/incorrect answer handling, elapsed time, result history and score-file persistence.

Evidence: [source 1](https://github.com/xet7/notegame/blob/8b7eb4e57ad4554b49b26a0125a1424df25a2d75/README.md) · [source 2](https://github.com/xet7/notegame/blob/8b7eb4e57ad4554b49b26a0125a1424df25a2d75/CHANGELOG.md) · [source 3](https://github.com/xet7/notegame/blob/8b7eb4e57ad4554b49b26a0125a1424df25a2d75/Aika/Code/Aikaar_V0.26.txt) · [source 4](https://github.com/xet7/notegame/blob/8b7eb4e57ad4554b49b26a0125a1424df25a2d75/Aika/Code/TeePeliTP.txt) · [source 5](https://github.com/xet7/notegame/blob/8b7eb4e57ad4554b49b26a0125a1424df25a2d75/Aika/Code/convert/convert-to-utf8.sh) · [source 6](https://github.com/xet7/notegame/blob/8b7eb4e57ad4554b49b26a0125a1424df25a2d75/Aika/s/startup-sequence)

**Source architecture (needs-research):** Original 1994–95 Blitz Basic game/editor sources are readable text exports, with tokenized originals retained. No native ISA was established from the inspected high-level source; source_cpu is not assigned from A1200 development provenance.

Evidence: [source 1](https://github.com/xet7/notegame/blob/8b7eb4e57ad4554b49b26a0125a1424df25a2d75/README.md) · [source 2](https://github.com/xet7/notegame/blob/8b7eb4e57ad4554b49b26a0125a1424df25a2d75/CHANGELOG.md) · [source 3](https://github.com/xet7/notegame/blob/8b7eb4e57ad4554b49b26a0125a1424df25a2d75/Aika/Code/Aikaar_V0.26.txt) · [source 4](https://github.com/xet7/notegame/blob/8b7eb4e57ad4554b49b26a0125a1424df25a2d75/Aika/Code/TeePeliTP.txt) · [source 5](https://github.com/xet7/notegame/blob/8b7eb4e57ad4554b49b26a0125a1424df25a2d75/Aika/Code/convert/convert-to-utf8.sh) · [source 6](https://github.com/xet7/notegame/blob/8b7eb4e57ad4554b49b26a0125a1424df25a2d75/Aika/s/startup-sequence)

**Target architecture (needs-research):** README names Amiga 1200, Blitz Basic 2 v2.10 and SuperTED v2.52. These are environment descriptions, not explicit output ISA evidence or proof of an AGA/68020 minimum. target_cpu remains empty pending native-output evidence.

Evidence: [source 1](https://github.com/xet7/notegame/blob/8b7eb4e57ad4554b49b26a0125a1424df25a2d75/README.md) · [source 2](https://github.com/xet7/notegame/blob/8b7eb4e57ad4554b49b26a0125a1424df25a2d75/Aika/Code/convert/convert-to-utf8.sh) · [source 3](https://github.com/xet7/notegame/blob/8b7eb4e57ad4554b49b26a0125a1424df25a2d75/Aika/s/startup-sequence) · [source 4](https://github.com/xet7/notegame/blob/8b7eb4e57ad4554b49b26a0125a1424df25a2d75/CHANGELOG.md) · [source 5](https://github.com/xet7/notegame/blob/8b7eb4e57ad4554b49b26a0125a1424df25a2d75/Aika/Code/Aikaar_V0.26.txt) · [source 6](https://github.com/xet7/notegame/blob/8b7eb4e57ad4554b49b26a0125a1424df25a2d75/Aika/Code/TeePeliTP.txt)

**Build and verification (reviewed):** README describes Aika: assignment and launch workflow; source needs ReqTools and data/graphics. Exported text was converted through AmiBlitz3 in 2024. No compile, detokenization-equivalence or packaged runtime check was performed. All four build flags are null. No independent successful build, execution, gameplay or byte-exact result is claimed.

Evidence: [source 1](https://github.com/xet7/notegame/blob/8b7eb4e57ad4554b49b26a0125a1424df25a2d75/README.md) · [source 2](https://github.com/xet7/notegame/blob/8b7eb4e57ad4554b49b26a0125a1424df25a2d75/Aika/Code/convert/convert-to-utf8.sh) · [source 3](https://github.com/xet7/notegame/blob/8b7eb4e57ad4554b49b26a0125a1424df25a2d75/Aika/s/startup-sequence)

**Runtime requirements (no-evidence-found):** Selected primary material does not establish a sufficiently explicit output-specific hardware minimum. No profile is populated: build flags, guest models, development machines and historical test anecdotes are not extrapolated into verified CPU/RAM/chipset/OS minima.

Evidence: [source 1](https://github.com/xet7/notegame/blob/8b7eb4e57ad4554b49b26a0125a1424df25a2d75/README.md) · [source 2](https://github.com/xet7/notegame/blob/8b7eb4e57ad4554b49b26a0125a1424df25a2d75/CHANGELOG.md) · [source 3](https://github.com/xet7/notegame/blob/8b7eb4e57ad4554b49b26a0125a1424df25a2d75/Aika/Code/Aikaar_V0.26.txt) · [source 4](https://github.com/xet7/notegame/blob/8b7eb4e57ad4554b49b26a0125a1424df25a2d75/Aika/Code/TeePeliTP.txt) · [source 5](https://github.com/xet7/notegame/blob/8b7eb4e57ad4554b49b26a0125a1424df25a2d75/Aika/Code/convert/convert-to-utf8.sh) · [source 6](https://github.com/xet7/notegame/blob/8b7eb4e57ad4554b49b26a0125a1424df25a2d75/Aika/s/startup-sequence)

**AI attribution (no-evidence-found):** No explicit generative-AI usage attribution found in the bounded README/source/build/license and latest ten-or-fewer commit-message review. This is not proof of non-use. Generic provider/model mentions, ordinary gameplay AI and future hypothetical uses are not named-tool attribution.

Evidence: [source 1](https://github.com/xet7/notegame/blob/8b7eb4e57ad4554b49b26a0125a1424df25a2d75/README.md) · [source 2](https://github.com/xet7/notegame/blob/8b7eb4e57ad4554b49b26a0125a1424df25a2d75/CHANGELOG.md) · [source 3](https://github.com/xet7/notegame/blob/8b7eb4e57ad4554b49b26a0125a1424df25a2d75/Aika/Code/Aikaar_V0.26.txt) · [source 4](https://github.com/xet7/notegame/blob/8b7eb4e57ad4554b49b26a0125a1424df25a2d75/Aika/Code/TeePeliTP.txt) · [source 5](https://github.com/xet7/notegame/blob/8b7eb4e57ad4554b49b26a0125a1424df25a2d75/Aika/Code/convert/convert-to-utf8.sh) · [source 6](https://github.com/xet7/notegame/blob/8b7eb4e57ad4554b49b26a0125a1424df25a2d75/Aika/s/startup-sequence) · [source 7](https://api.github.com/repos/xet7/notegame/commits?per_page=10)

**Lineage and rights (reviewed):** Lauri Ojansivu and Tapio Pärepalo’s original game and definition editor are one record. MIT LICENSE names both; bundled reqtools/system libraries/fonts have separate unaudited rights. Windows/Linux/Mac Blitz variants mentioned in README are not ports of this Amiga game. Historic 1.3/2.x compatibility is an intent claim, not a verified matrix. License/asset review: MIT LICENSE names Lauri Ojansivu and Tapio Pärepalo (1995–2024). Bundled third-party runtime/system components and fonts have not received a separate rights audit. Wider author/dependency graphs remain partial.

Evidence: [source 1](https://github.com/xet7/notegame/blob/8b7eb4e57ad4554b49b26a0125a1424df25a2d75/README.md) · [source 2](https://github.com/xet7/notegame/blob/8b7eb4e57ad4554b49b26a0125a1424df25a2d75/CHANGELOG.md) · [source 3](https://github.com/xet7/notegame/blob/8b7eb4e57ad4554b49b26a0125a1424df25a2d75/Aika/Code/Aikaar_V0.26.txt) · [source 4](https://github.com/xet7/notegame/blob/8b7eb4e57ad4554b49b26a0125a1424df25a2d75/Aika/Code/TeePeliTP.txt) · [source 5](https://github.com/xet7/notegame/blob/8b7eb4e57ad4554b49b26a0125a1424df25a2d75/Aika/Code/convert/convert-to-utf8.sh) · [source 6](https://github.com/xet7/notegame/blob/8b7eb4e57ad4554b49b26a0125a1424df25a2d75/Aika/s/startup-sequence) · [source 7](https://github.com/xet7/notegame/blob/8b7eb4e57ad4554b49b26a0125a1424df25a2d75/LICENSE) · [source 8](https://api.github.com/repos/xet7/notegame) · [source 9](https://github.com/xet7/notegame/commit/8b7eb4e57ad4554b49b26a0125a1424df25a2d75) · [source 10](https://github.com/xet7/notegame/commit/adb2c89ed419027e792c0a44986d2a001c3d4667) · [source 11](https://api.github.com/repos/xet7/notegame/git/commits/8b7eb4e57ad4554b49b26a0125a1424df25a2d75)

### Galaga: native C64 arcade adaptation source

[Repository](https://github.com/1888games/GalagaC64)

- Source platforms: Unasserted / not applicable
- Target platforms: C64
- Source CPU: Unasserted / not applicable
- Target CPU: 6502
- Source material/language: Unasserted / not applicable
- Maintained language: 6502 assembly (KickAssembler)
- Classification: subject; game, reimplementation
- Build flags: all unknown (compilable, runnable, playable and byte_exact).
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** README names a Commodore 64 arcade port written with KickAssembler, CharPad and SpritePad. main.asm supplies a BASIC entry stub and directly configures VIC-II, interrupts, SID and memory banking. beam.asm implements capture, spinning, recapture and dual-fighter transitions; source modules cover formations, collision, waves, challenge stages, scores and disk persistence. These are game mechanics, not an embedded arcade CPU core. Main entry reads the KERNAL PAL/NTSC flag at $02A6. IRQ code selects raster/multiplexer timing and skips periodic SID updates for NTSC. Historical logs contain PRG memory maps; the reviewed head is V1.06a. Inspected snapshot: branch main, head commit 583f515ab7000d85478948c954463deaf1d7369b, git tree b52109614e94fc8802da68538276acd1da394c75. Head and tree are separate identities; the connector tree response top-level sha was not used as the actual tree identity. Inspection is a bounded sample, not all code/features.

Evidence: [source 1](https://github.com/1888games/GalagaC64/blob/583f515ab7000d85478948c954463deaf1d7369b/Scripts/main.asm) · [source 2](https://github.com/1888games/GalagaC64/blob/583f515ab7000d85478948c954463deaf1d7369b/Scripts/game/gameplay/beam.asm) · [source 3](https://github.com/1888games/GalagaC64/blob/583f515ab7000d85478948c954463deaf1d7369b/Scripts/game/system/irq.asm) · [source 4](https://github.com/1888games/GalagaC64/blob/583f515ab7000d85478948c954463deaf1d7369b/Scripts/data/assets.asm) · [source 5](https://github.com/1888games/GalagaC64/blob/583f515ab7000d85478948c954463deaf1d7369b/README.md) · [source 6](https://github.com/1888games/GalagaC64/blob/583f515ab7000d85478948c954463deaf1d7369b/Scripts/bin/main_BuildLog.txt) · [source 7](https://github.com/1888games/GalagaC64/commit/583f515ab7000d85478948c954463deaf1d7369b)

**Classification (reviewed):** Native C64 authored game source, with direct game logic and VIC-II/SID/CIA interaction rather than a game-specific CPU emulator. README identifies the arcade game as inspiration; no original arcade binary, Z80 disassembly or CPU translation was inspected. Target is C64, while source_platforms/source_cpu/source_language remain empty because no original binary was recovered or analysed. work_kinds=reimplementation describes the evidenced game adaptation, not binary-derived reverse engineering.

Evidence: [source 1](https://github.com/1888games/GalagaC64/blob/583f515ab7000d85478948c954463deaf1d7369b/Scripts/main.asm) · [source 2](https://github.com/1888games/GalagaC64/blob/583f515ab7000d85478948c954463deaf1d7369b/Scripts/game/gameplay/beam.asm) · [source 3](https://github.com/1888games/GalagaC64/blob/583f515ab7000d85478948c954463deaf1d7369b/Scripts/game/system/irq.asm) · [source 4](https://github.com/1888games/GalagaC64/blob/583f515ab7000d85478948c954463deaf1d7369b/Scripts/data/assets.asm) · [source 5](https://github.com/1888games/GalagaC64/blob/583f515ab7000d85478948c954463deaf1d7369b/README.md) · [source 6](https://github.com/1888games/GalagaC64/blob/583f515ab7000d85478948c954463deaf1d7369b/Scripts/bin/main_BuildLog.txt)

**Source architecture (not-applicable):** This is authored or adapted game source, not a disassembled/recovered original executable. Game inspiration does not establish the original binary ISA; source_cpu stays empty/not-applicable.

Evidence: [source 1](https://github.com/1888games/GalagaC64/blob/583f515ab7000d85478948c954463deaf1d7369b/Scripts/main.asm) · [source 2](https://github.com/1888games/GalagaC64/blob/583f515ab7000d85478948c954463deaf1d7369b/Scripts/game/gameplay/beam.asm) · [source 3](https://github.com/1888games/GalagaC64/blob/583f515ab7000d85478948c954463deaf1d7369b/Scripts/game/system/irq.asm) · [source 4](https://github.com/1888games/GalagaC64/blob/583f515ab7000d85478948c954463deaf1d7369b/Scripts/data/assets.asm) · [source 5](https://github.com/1888games/GalagaC64/blob/583f515ab7000d85478948c954463deaf1d7369b/README.md) · [source 6](https://github.com/1888games/GalagaC64/blob/583f515ab7000d85478948c954463deaf1d7369b/Scripts/bin/main_BuildLog.txt)

**Target architecture (reviewed):** Reviewed assembly contains 6502-family LDA/STA/JSR and native hardware-access code, with a C64 assembler/entrypoint. target_cpu=6502 records the observed instruction set; it does not assert an exact 6510 silicon subtype, numerical CPU/RAM minimum, or successfully assembled output.

Evidence: [source 1](https://github.com/1888games/GalagaC64/blob/583f515ab7000d85478948c954463deaf1d7369b/Scripts/main.asm) · [source 2](https://github.com/1888games/GalagaC64/blob/583f515ab7000d85478948c954463deaf1d7369b/Scripts/bin/main_BuildLog.txt) · [source 3](https://github.com/1888games/GalagaC64/blob/583f515ab7000d85478948c954463deaf1d7369b/Scripts/game/gameplay/beam.asm) · [source 4](https://github.com/1888games/GalagaC64/blob/583f515ab7000d85478948c954463deaf1d7369b/Scripts/game/system/irq.asm) · [source 5](https://github.com/1888games/GalagaC64/blob/583f515ab7000d85478948c954463deaf1d7369b/Scripts/data/assets.asm) · [source 6](https://github.com/1888games/GalagaC64/blob/583f515ab7000d85478948c954463deaf1d7369b/README.md)

**Build and verification (needs-research):** Selected main assembly and included assets define the native KickAssembler program; checked-in PRGs, symbols and historical build logs are upstream artifacts, not a current successful build. No portable automated build recipe was established. No independent assembly, runtime, original-ROM equivalence or hardware test was performed. Checked-in PRGs and historical build logs are upstream artifacts only. No explicit license was found in the inspected standalone README/source material or license-named tree entries. Public source visibility does not establish redistribution rights, including rights in game graphics, names and music. Build portability needs review: several imports use lowercase assets while the tree stores Assets, along with historical relative-path conventions. No clean case-sensitive-host rebuild was attempted. PAL/NTSC adjustment code is implementation evidence, not verified timing or full gameplay equivalence. No candidate compilation, execution, emulator/gameplay test, hardware test, round-trip or byte comparison was run. compilable/runnable/playable/byte_exact all remain null.

Evidence: [source 1](https://github.com/1888games/GalagaC64/blob/583f515ab7000d85478948c954463deaf1d7369b/Scripts/main.asm) · [source 2](https://github.com/1888games/GalagaC64/blob/583f515ab7000d85478948c954463deaf1d7369b/Scripts/bin/main_BuildLog.txt) · [source 3](https://github.com/1888games/GalagaC64/blob/583f515ab7000d85478948c954463deaf1d7369b/Scripts/game/gameplay/beam.asm) · [source 4](https://github.com/1888games/GalagaC64/blob/583f515ab7000d85478948c954463deaf1d7369b/Scripts/game/system/irq.asm) · [source 5](https://github.com/1888games/GalagaC64/blob/583f515ab7000d85478948c954463deaf1d7369b/Scripts/data/assets.asm) · [source 6](https://github.com/1888games/GalagaC64/blob/583f515ab7000d85478948c954463deaf1d7369b/README.md)

**Runtime requirements (no-evidence-found):** No sufficiently specific supported minimum hardware configuration was established for a runtime profile. Target C64 and observed native ISA are not evidence of a tested CPU/RAM minimum. Video/timing evidence: MOS 6510/6502-family native C64; VIC-II/SID/CIA direct access. Explicit PAL/NTSC detection and frame/SID scheduling branches; untested. Relevant limits: PAL/NTSC adjustment code is implementation evidence, not verified timing or full gameplay equivalence.

Evidence: [source 1](https://github.com/1888games/GalagaC64/blob/583f515ab7000d85478948c954463deaf1d7369b/Scripts/main.asm) · [source 2](https://github.com/1888games/GalagaC64/blob/583f515ab7000d85478948c954463deaf1d7369b/Scripts/game/gameplay/beam.asm) · [source 3](https://github.com/1888games/GalagaC64/blob/583f515ab7000d85478948c954463deaf1d7369b/Scripts/game/system/irq.asm) · [source 4](https://github.com/1888games/GalagaC64/blob/583f515ab7000d85478948c954463deaf1d7369b/Scripts/data/assets.asm) · [source 5](https://github.com/1888games/GalagaC64/blob/583f515ab7000d85478948c954463deaf1d7369b/README.md) · [source 6](https://github.com/1888games/GalagaC64/blob/583f515ab7000d85478948c954463deaf1d7369b/Scripts/bin/main_BuildLog.txt)

**AI attribution (no-evidence-found):** No explicit generative-AI attribution found in the selected README, implementation, build or license material and the first eight default-branch commit messages/author metadata (or all returned if fewer). One selected commit detail was read where recorded. This bounded review is not proof of non-use. Opponent gameplay AI is not generative-AI tooling evidence. Unknown is not evidence of non-use; named tools are not inferred from provider addresses, ordinary automation or gameplay AI.

Evidence: [source 1](https://api.github.com/repos/1888games/GalagaC64/commits?per_page=8&page=1) · [source 2](https://github.com/1888games/GalagaC64/commit/583f515ab7000d85478948c954463deaf1d7369b) · [source 3](https://github.com/1888games/GalagaC64/blob/583f515ab7000d85478948c954463deaf1d7369b/Scripts/main.asm) · [source 4](https://github.com/1888games/GalagaC64/blob/583f515ab7000d85478948c954463deaf1d7369b/Scripts/game/gameplay/beam.asm) · [source 5](https://github.com/1888games/GalagaC64/blob/583f515ab7000d85478948c954463deaf1d7369b/Scripts/game/system/irq.asm) · [source 6](https://github.com/1888games/GalagaC64/blob/583f515ab7000d85478948c954463deaf1d7369b/Scripts/data/assets.asm) · [source 7](https://github.com/1888games/GalagaC64/blob/583f515ab7000d85478948c954463deaf1d7369b/README.md) · [source 8](https://github.com/1888games/GalagaC64/blob/583f515ab7000d85478948c954463deaf1d7369b/Scripts/bin/main_BuildLog.txt)

**Lineage and rights (reviewed):** overlapping collection; not a second project 1888games/ArlasoftC64 The overlapping Arlasoft Complete folder is supporting provenance, not another project. Blob comparison found 79 matching standalone blobs; main-source match paths: Complete/GalagaC64/Scripts/main.asm. Licensing: No standalone license grant established; metadata license is null and no license-named file occurs in the complete tree. Canonical root was absent from the verified 1,621-project d654a0c publication baseline and 1,861-root normalized reviewed index. Wider lineage/source coverage is still partial.

Evidence: [source 1](https://github.com/1888games/GalagaC64/blob/583f515ab7000d85478948c954463deaf1d7369b/Scripts/main.asm) · [source 2](https://github.com/1888games/GalagaC64/blob/583f515ab7000d85478948c954463deaf1d7369b/Scripts/game/gameplay/beam.asm) · [source 3](https://github.com/1888games/GalagaC64/blob/583f515ab7000d85478948c954463deaf1d7369b/Scripts/game/system/irq.asm) · [source 4](https://github.com/1888games/GalagaC64/blob/583f515ab7000d85478948c954463deaf1d7369b/Scripts/data/assets.asm) · [source 5](https://github.com/1888games/GalagaC64/blob/583f515ab7000d85478948c954463deaf1d7369b/README.md) · [source 6](https://github.com/1888games/GalagaC64/blob/583f515ab7000d85478948c954463deaf1d7369b/Scripts/bin/main_BuildLog.txt) · [source 7](https://github.com/1888games/ArlasoftC64/blob/7f70676ee2166e493e9669370f226813ea1cd5cb/README.md)

### Galaxian: native C64 arcade adaptation source

[Repository](https://github.com/1888games/GalaxianC64)

- Source platforms: Unasserted / not applicable
- Target platforms: C64
- Source CPU: Unasserted / not applicable
- Target CPU: 6502
- Source material/language: Unasserted / not applicable
- Maintained language: 6502 assembly (KickAssembler)
- Classification: subject; game, reimplementation
- Build flags: all unknown (compilable, runnable, playable and byte_exact).
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** main.asm assembles the C64 program and imports Galaxian charger and flight modules alongside the shared graphics/input framework. charger.asm implements flagship escorts, alien flank selection, attack counters, difficulty, shocked swarms and level completion. It is distinct game logic, not simply a renamed Galaga binary or repository mirror. MachineType is read from $02A6; irq.asm includes NTSC-specific star setup and SID scheduling. The inspected history includes a source-changing 1.01 fix and a release V1.0 commit. Inspected snapshot: branch main, head commit b493eb741b87f4f73d359532923b910115e191ff, git tree bf7b225eed3b37d00499c0be188639073a517606. Head and tree are separate identities; the connector tree response top-level sha was not used as the actual tree identity. Inspection is a bounded sample, not all code/features.

Evidence: [source 1](https://github.com/1888games/GalaxianC64/blob/b493eb741b87f4f73d359532923b910115e191ff/Scripts/main.asm) · [source 2](https://github.com/1888games/GalaxianC64/blob/b493eb741b87f4f73d359532923b910115e191ff/Scripts/game/gameplay/charger.asm) · [source 3](https://github.com/1888games/GalaxianC64/blob/b493eb741b87f4f73d359532923b910115e191ff/Scripts/game/system/irq.asm) · [source 4](https://github.com/1888games/GalaxianC64/blob/b493eb741b87f4f73d359532923b910115e191ff/Scripts/data/assets.asm) · [source 5](https://github.com/1888games/GalaxianC64/blob/b493eb741b87f4f73d359532923b910115e191ff/README.md) · [source 6](https://github.com/1888games/GalaxianC64/blob/b493eb741b87f4f73d359532923b910115e191ff/Scripts/bin/main_BuildLog.txt) · [source 7](https://github.com/1888games/GalaxianC64/commit/b493eb741b87f4f73d359532923b910115e191ff)

**Classification (reviewed):** Native C64 authored game source, with direct game logic and VIC-II/SID/CIA interaction rather than a game-specific CPU emulator. Distinct Galaxian gameplay shares an Arlasoft C64 framework with Galaga. Source inspection does not establish original arcade binary recovery, emulation or original-CPU analysis. Target is C64, while source_platforms/source_cpu/source_language remain empty because no original binary was recovered or analysed. work_kinds=reimplementation describes the evidenced game adaptation, not binary-derived reverse engineering.

Evidence: [source 1](https://github.com/1888games/GalaxianC64/blob/b493eb741b87f4f73d359532923b910115e191ff/Scripts/main.asm) · [source 2](https://github.com/1888games/GalaxianC64/blob/b493eb741b87f4f73d359532923b910115e191ff/Scripts/game/gameplay/charger.asm) · [source 3](https://github.com/1888games/GalaxianC64/blob/b493eb741b87f4f73d359532923b910115e191ff/Scripts/game/system/irq.asm) · [source 4](https://github.com/1888games/GalaxianC64/blob/b493eb741b87f4f73d359532923b910115e191ff/Scripts/data/assets.asm) · [source 5](https://github.com/1888games/GalaxianC64/blob/b493eb741b87f4f73d359532923b910115e191ff/README.md) · [source 6](https://github.com/1888games/GalaxianC64/blob/b493eb741b87f4f73d359532923b910115e191ff/Scripts/bin/main_BuildLog.txt)

**Source architecture (not-applicable):** This is authored or adapted game source, not a disassembled/recovered original executable. Game inspiration does not establish the original binary ISA; source_cpu stays empty/not-applicable.

Evidence: [source 1](https://github.com/1888games/GalaxianC64/blob/b493eb741b87f4f73d359532923b910115e191ff/Scripts/main.asm) · [source 2](https://github.com/1888games/GalaxianC64/blob/b493eb741b87f4f73d359532923b910115e191ff/Scripts/game/gameplay/charger.asm) · [source 3](https://github.com/1888games/GalaxianC64/blob/b493eb741b87f4f73d359532923b910115e191ff/Scripts/game/system/irq.asm) · [source 4](https://github.com/1888games/GalaxianC64/blob/b493eb741b87f4f73d359532923b910115e191ff/Scripts/data/assets.asm) · [source 5](https://github.com/1888games/GalaxianC64/blob/b493eb741b87f4f73d359532923b910115e191ff/README.md) · [source 6](https://github.com/1888games/GalaxianC64/blob/b493eb741b87f4f73d359532923b910115e191ff/Scripts/bin/main_BuildLog.txt)

**Target architecture (reviewed):** Reviewed assembly contains 6502-family LDA/STA/JSR and native hardware-access code, with a C64 assembler/entrypoint. target_cpu=6502 records the observed instruction set; it does not assert an exact 6510 silicon subtype, numerical CPU/RAM minimum, or successfully assembled output.

Evidence: [source 1](https://github.com/1888games/GalaxianC64/blob/b493eb741b87f4f73d359532923b910115e191ff/Scripts/main.asm) · [source 2](https://github.com/1888games/GalaxianC64/blob/b493eb741b87f4f73d359532923b910115e191ff/Scripts/bin/main_BuildLog.txt) · [source 3](https://github.com/1888games/GalaxianC64/blob/b493eb741b87f4f73d359532923b910115e191ff/Scripts/game/gameplay/charger.asm) · [source 4](https://github.com/1888games/GalaxianC64/blob/b493eb741b87f4f73d359532923b910115e191ff/Scripts/game/system/irq.asm) · [source 5](https://github.com/1888games/GalaxianC64/blob/b493eb741b87f4f73d359532923b910115e191ff/Scripts/data/assets.asm) · [source 6](https://github.com/1888games/GalaxianC64/blob/b493eb741b87f4f73d359532923b910115e191ff/README.md)

**Build and verification (needs-research):** Selected main assembly and included assets define the native KickAssembler program; checked-in PRGs, symbols and historical build logs are upstream artifacts, not a current successful build. No portable automated build recipe was established. No independent assembly, runtime, original-ROM equivalence or hardware test was performed. Checked-in PRGs and historical build logs are upstream artifacts only. No explicit license was found in the inspected standalone README/source material or license-named tree entries. Public source visibility does not establish redistribution rights, including rights in game graphics, names and music. Build portability needs review: several imports use lowercase assets while the tree stores Assets, along with historical relative-path conventions. No clean case-sensitive-host rebuild was attempted. README is only a title; classification is grounded in source and history. Shared Galaga-named SID/map assets remain in-tree and should not be interpreted as a separate underlying game source recovery. No candidate compilation, execution, emulator/gameplay test, hardware test, round-trip or byte comparison was run. compilable/runnable/playable/byte_exact all remain null.

Evidence: [source 1](https://github.com/1888games/GalaxianC64/blob/b493eb741b87f4f73d359532923b910115e191ff/Scripts/main.asm) · [source 2](https://github.com/1888games/GalaxianC64/blob/b493eb741b87f4f73d359532923b910115e191ff/Scripts/bin/main_BuildLog.txt) · [source 3](https://github.com/1888games/GalaxianC64/blob/b493eb741b87f4f73d359532923b910115e191ff/Scripts/game/gameplay/charger.asm) · [source 4](https://github.com/1888games/GalaxianC64/blob/b493eb741b87f4f73d359532923b910115e191ff/Scripts/game/system/irq.asm) · [source 5](https://github.com/1888games/GalaxianC64/blob/b493eb741b87f4f73d359532923b910115e191ff/Scripts/data/assets.asm) · [source 6](https://github.com/1888games/GalaxianC64/blob/b493eb741b87f4f73d359532923b910115e191ff/README.md)

**Runtime requirements (no-evidence-found):** No sufficiently specific supported minimum hardware configuration was established for a runtime profile. Target C64 and observed native ISA are not evidence of a tested CPU/RAM minimum. Video/timing evidence: Native MOS 6510 C64 assembly with VIC-II/SID/CIA; PAL/NTSC-specific source branches exist, but neither mode was executed. Relevant limits:

Evidence: [source 1](https://github.com/1888games/GalaxianC64/blob/b493eb741b87f4f73d359532923b910115e191ff/Scripts/main.asm) · [source 2](https://github.com/1888games/GalaxianC64/blob/b493eb741b87f4f73d359532923b910115e191ff/Scripts/game/gameplay/charger.asm) · [source 3](https://github.com/1888games/GalaxianC64/blob/b493eb741b87f4f73d359532923b910115e191ff/Scripts/game/system/irq.asm) · [source 4](https://github.com/1888games/GalaxianC64/blob/b493eb741b87f4f73d359532923b910115e191ff/Scripts/data/assets.asm) · [source 5](https://github.com/1888games/GalaxianC64/blob/b493eb741b87f4f73d359532923b910115e191ff/README.md) · [source 6](https://github.com/1888games/GalaxianC64/blob/b493eb741b87f4f73d359532923b910115e191ff/Scripts/bin/main_BuildLog.txt)

**AI attribution (no-evidence-found):** No explicit generative-AI attribution found in the selected README, implementation, build or license material and the first eight default-branch commit messages/author metadata (or all returned if fewer). One selected commit detail was read where recorded. This bounded review is not proof of non-use. Opponent gameplay AI is not generative-AI tooling evidence. Unknown is not evidence of non-use; named tools are not inferred from provider addresses, ordinary automation or gameplay AI.

Evidence: [source 1](https://api.github.com/repos/1888games/GalaxianC64/commits?per_page=8&page=1) · [source 2](https://github.com/1888games/GalaxianC64/commit/b493eb741b87f4f73d359532923b910115e191ff) · [source 3](https://github.com/1888games/GalaxianC64/blob/b493eb741b87f4f73d359532923b910115e191ff/Scripts/main.asm) · [source 4](https://github.com/1888games/GalaxianC64/blob/b493eb741b87f4f73d359532923b910115e191ff/Scripts/game/gameplay/charger.asm) · [source 5](https://github.com/1888games/GalaxianC64/blob/b493eb741b87f4f73d359532923b910115e191ff/Scripts/game/system/irq.asm) · [source 6](https://github.com/1888games/GalaxianC64/blob/b493eb741b87f4f73d359532923b910115e191ff/Scripts/data/assets.asm) · [source 7](https://github.com/1888games/GalaxianC64/blob/b493eb741b87f4f73d359532923b910115e191ff/README.md) · [source 8](https://github.com/1888games/GalaxianC64/blob/b493eb741b87f4f73d359532923b910115e191ff/Scripts/bin/main_BuildLog.txt)

**Lineage and rights (reviewed):** overlapping collection; not a second project 1888games/ArlasoftC64 The overlapping Arlasoft Complete folder is supporting provenance, not another project. Blob comparison found 83 matching standalone blobs; main-source match paths: Complete/Galaxian/Scripts/main.asm. Licensing: No standalone license grant established; metadata license is null and no license-named file occurs in the complete tree. Canonical root was absent from the verified 1,621-project d654a0c publication baseline and 1,861-root normalized reviewed index. Wider lineage/source coverage is still partial.

Evidence: [source 1](https://github.com/1888games/GalaxianC64/blob/b493eb741b87f4f73d359532923b910115e191ff/Scripts/main.asm) · [source 2](https://github.com/1888games/GalaxianC64/blob/b493eb741b87f4f73d359532923b910115e191ff/Scripts/game/gameplay/charger.asm) · [source 3](https://github.com/1888games/GalaxianC64/blob/b493eb741b87f4f73d359532923b910115e191ff/Scripts/game/system/irq.asm) · [source 4](https://github.com/1888games/GalaxianC64/blob/b493eb741b87f4f73d359532923b910115e191ff/Scripts/data/assets.asm) · [source 5](https://github.com/1888games/GalaxianC64/blob/b493eb741b87f4f73d359532923b910115e191ff/README.md) · [source 6](https://github.com/1888games/GalaxianC64/blob/b493eb741b87f4f73d359532923b910115e191ff/Scripts/bin/main_BuildLog.txt) · [source 7](https://github.com/1888games/ArlasoftC64/blob/7f70676ee2166e493e9669370f226813ea1cd5cb/README.md)

### Megamania: native C64 adaptation source

[Repository](https://github.com/1888games/Megamania-C64-)

- Source platforms: Unasserted / not applicable
- Target platforms: C64
- Source CPU: Unasserted / not applicable
- Target CPU: 6502
- Source material/language: Unasserted / not applicable
- Maintained language: 6502 assembly (KickAssembler)
- Classification: subject; game, reimplementation
- Build flags: all unknown (compilable, runnable, playable and byte_exact).
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** README identifies the Atari 2600 original and native C64 KickAssembler workflow. main.asm assembles game state, sound, bullets, ship, energy and enemy modules; enemies.asm contains wave tables, enemy movement, collision and scoring. irq.asm multiplexes enemy sprite rows. The repository includes CharPad/SpritePad source assets, SID/sound data, PRG/symbol files and a historical assembler memory-map log. Latest sampled history contains gameplay fixes. Inspected snapshot: branch master, head commit ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529, git tree 1e7ca2e64f23981ab98b4e4375bb5a06ebeed596. Head and tree are separate identities; the connector tree response top-level sha was not used as the actual tree identity. Inspection is a bounded sample, not all code/features.

Evidence: [source 1](https://github.com/1888games/Megamania-C64-/blob/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529/scripts/main.asm) · [source 2](https://github.com/1888games/Megamania-C64-/blob/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529/scripts/interrupts/enemies.asm) · [source 3](https://github.com/1888games/Megamania-C64-/blob/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529/scripts/interrupts/irq.asm) · [source 4](https://github.com/1888games/Megamania-C64-/blob/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529/scripts/setup/assets.asm) · [source 5](https://github.com/1888games/Megamania-C64-/blob/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529/README.md) · [source 6](https://github.com/1888games/Megamania-C64-/blob/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529/scripts/bin/main_BuildLog.txt) · [source 7](https://github.com/1888games/Megamania-C64-/commit/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529)

**Classification (reviewed):** Native C64 authored game source, with direct game logic and VIC-II/SID/CIA interaction rather than a game-specific CPU emulator. README identifies the Atari 2600 original, but this reviewed material is newly authored C64 assembly. No Atari ROM or original 6507 binary was analysed. Target is C64, while source_platforms/source_cpu/source_language remain empty because no original binary was recovered or analysed. work_kinds=reimplementation describes the evidenced game adaptation, not binary-derived reverse engineering.

Evidence: [source 1](https://github.com/1888games/Megamania-C64-/blob/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529/scripts/main.asm) · [source 2](https://github.com/1888games/Megamania-C64-/blob/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529/scripts/interrupts/enemies.asm) · [source 3](https://github.com/1888games/Megamania-C64-/blob/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529/scripts/interrupts/irq.asm) · [source 4](https://github.com/1888games/Megamania-C64-/blob/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529/scripts/setup/assets.asm) · [source 5](https://github.com/1888games/Megamania-C64-/blob/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529/README.md) · [source 6](https://github.com/1888games/Megamania-C64-/blob/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529/scripts/bin/main_BuildLog.txt)

**Source architecture (not-applicable):** This is authored or adapted game source, not a disassembled/recovered original executable. Game inspiration does not establish the original binary ISA; source_cpu stays empty/not-applicable.

Evidence: [source 1](https://github.com/1888games/Megamania-C64-/blob/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529/scripts/main.asm) · [source 2](https://github.com/1888games/Megamania-C64-/blob/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529/scripts/interrupts/enemies.asm) · [source 3](https://github.com/1888games/Megamania-C64-/blob/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529/scripts/interrupts/irq.asm) · [source 4](https://github.com/1888games/Megamania-C64-/blob/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529/scripts/setup/assets.asm) · [source 5](https://github.com/1888games/Megamania-C64-/blob/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529/README.md) · [source 6](https://github.com/1888games/Megamania-C64-/blob/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529/scripts/bin/main_BuildLog.txt)

**Target architecture (reviewed):** Reviewed assembly contains 6502-family LDA/STA/JSR and native hardware-access code, with a C64 assembler/entrypoint. target_cpu=6502 records the observed instruction set; it does not assert an exact 6510 silicon subtype, numerical CPU/RAM minimum, or successfully assembled output.

Evidence: [source 1](https://github.com/1888games/Megamania-C64-/blob/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529/scripts/main.asm) · [source 2](https://github.com/1888games/Megamania-C64-/blob/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529/scripts/bin/main_BuildLog.txt) · [source 3](https://github.com/1888games/Megamania-C64-/blob/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529/scripts/interrupts/enemies.asm) · [source 4](https://github.com/1888games/Megamania-C64-/blob/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529/scripts/interrupts/irq.asm) · [source 5](https://github.com/1888games/Megamania-C64-/blob/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529/scripts/setup/assets.asm) · [source 6](https://github.com/1888games/Megamania-C64-/blob/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529/README.md)

**Build and verification (needs-research):** Selected main assembly and included assets define the native KickAssembler program; checked-in PRGs, symbols and historical build logs are upstream artifacts, not a current successful build. No portable automated build recipe was established. No independent assembly, runtime, original-ROM equivalence or hardware test was performed. Checked-in PRGs and historical build logs are upstream artifacts only. No explicit license was found in the inspected standalone README/source material or license-named tree entries. Public source visibility does not establish redistribution rights, including rights in game graphics, names and music. Build portability needs review: several imports use lowercase assets while the tree stores Assets, along with historical relative-path conventions. No clean case-sensitive-host rebuild was attempted. DetectMachine stores a PAL/NTSC value, but the reviewed NTSC branch merely jumps to the common finish label; full timing compensation is not established. No candidate compilation, execution, emulator/gameplay test, hardware test, round-trip or byte comparison was run. compilable/runnable/playable/byte_exact all remain null.

Evidence: [source 1](https://github.com/1888games/Megamania-C64-/blob/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529/scripts/main.asm) · [source 2](https://github.com/1888games/Megamania-C64-/blob/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529/scripts/bin/main_BuildLog.txt) · [source 3](https://github.com/1888games/Megamania-C64-/blob/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529/scripts/interrupts/enemies.asm) · [source 4](https://github.com/1888games/Megamania-C64-/blob/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529/scripts/interrupts/irq.asm) · [source 5](https://github.com/1888games/Megamania-C64-/blob/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529/scripts/setup/assets.asm) · [source 6](https://github.com/1888games/Megamania-C64-/blob/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529/README.md)

**Runtime requirements (no-evidence-found):** No sufficiently specific supported minimum hardware configuration was established for a runtime profile. Target C64 and observed native ISA are not evidence of a tested CPU/RAM minimum. Video/timing evidence: Native C64 MOS 6510/6502 assembly; raster-multiplexed sprites and SID. A machine detector alone does not establish equivalent PAL/NTSC timing. Relevant limits: DetectMachine stores a PAL/NTSC value, but the reviewed NTSC branch merely jumps to the common finish label; full timing compensation is not established.

Evidence: [source 1](https://github.com/1888games/Megamania-C64-/blob/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529/scripts/main.asm) · [source 2](https://github.com/1888games/Megamania-C64-/blob/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529/scripts/interrupts/enemies.asm) · [source 3](https://github.com/1888games/Megamania-C64-/blob/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529/scripts/interrupts/irq.asm) · [source 4](https://github.com/1888games/Megamania-C64-/blob/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529/scripts/setup/assets.asm) · [source 5](https://github.com/1888games/Megamania-C64-/blob/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529/README.md) · [source 6](https://github.com/1888games/Megamania-C64-/blob/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529/scripts/bin/main_BuildLog.txt)

**AI attribution (no-evidence-found):** No explicit generative-AI attribution found in the selected README, implementation, build or license material and the first eight default-branch commit messages/author metadata (or all returned if fewer). One selected commit detail was read where recorded. This bounded review is not proof of non-use. Opponent gameplay AI is not generative-AI tooling evidence. Unknown is not evidence of non-use; named tools are not inferred from provider addresses, ordinary automation or gameplay AI.

Evidence: [source 1](https://api.github.com/repos/1888games/Megamania-C64-/commits?per_page=8&page=1) · [source 2](https://github.com/1888games/Megamania-C64-/commit/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529) · [source 3](https://github.com/1888games/Megamania-C64-/blob/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529/scripts/main.asm) · [source 4](https://github.com/1888games/Megamania-C64-/blob/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529/scripts/interrupts/enemies.asm) · [source 5](https://github.com/1888games/Megamania-C64-/blob/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529/scripts/interrupts/irq.asm) · [source 6](https://github.com/1888games/Megamania-C64-/blob/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529/scripts/setup/assets.asm) · [source 7](https://github.com/1888games/Megamania-C64-/blob/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529/README.md) · [source 8](https://github.com/1888games/Megamania-C64-/blob/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529/scripts/bin/main_BuildLog.txt)

**Lineage and rights (reviewed):** overlapping collection; not a second project 1888games/ArlasoftC64 The overlapping Arlasoft Complete folder is supporting provenance, not another project. Blob comparison found 90 matching standalone blobs; main-source match paths: Complete/Megamania/scripts/main.asm. Licensing: No standalone license grant established; metadata license is null and no license-named file occurs in the complete tree. Canonical root was absent from the verified 1,621-project d654a0c publication baseline and 1,861-root normalized reviewed index. Wider lineage/source coverage is still partial.

Evidence: [source 1](https://github.com/1888games/Megamania-C64-/blob/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529/scripts/main.asm) · [source 2](https://github.com/1888games/Megamania-C64-/blob/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529/scripts/interrupts/enemies.asm) · [source 3](https://github.com/1888games/Megamania-C64-/blob/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529/scripts/interrupts/irq.asm) · [source 4](https://github.com/1888games/Megamania-C64-/blob/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529/scripts/setup/assets.asm) · [source 5](https://github.com/1888games/Megamania-C64-/blob/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529/README.md) · [source 6](https://github.com/1888games/Megamania-C64-/blob/ae6458a21a3a8ce7b7c19bf750b7b6d9d004e529/scripts/bin/main_BuildLog.txt) · [source 7](https://github.com/1888games/ArlasoftC64/blob/7f70676ee2166e493e9669370f226813ea1cd5cb/README.md)

### Paper Planes: native C64 port source

[Repository](https://github.com/1888games/PaperPlanesC64)

- Source platforms: Unasserted / not applicable
- Target platforms: C64
- Source CPU: Unasserted / not applicable
- Target CPU: 6502
- Source material/language: Unasserted / not applicable
- Maintained language: 6502 assembly (KickAssembler)
- Classification: subject; game, reimplementation
- Build flags: all unknown (compilable, runnable, playable and byte_exact).
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** README explicitly credits Sam Demaine’s Ludum Dare 47 game and lists KickAssembler, CharPad and SpritePad. player.asm implements fixed-point position, turning-angle lookup, joystick steering, power-up detection and collectible collision. main.asm imports enemy, scoring, power-up and sprite-multiplexer code. Source reads $02A6 and uses a SID timing counter for NTSC. The selected history includes the substantive change from sprite power-ups to character power-ups. Inspected snapshot: branch main, head commit fe2f445a074d159dd499d2a6211af897a5fcc065, git tree 4b9891c82c0f40e8f0c7b51476145ad0e0f3e230. Head and tree are separate identities; the connector tree response top-level sha was not used as the actual tree identity. Inspection is a bounded sample, not all code/features.

Evidence: [source 1](https://github.com/1888games/PaperPlanesC64/blob/fe2f445a074d159dd499d2a6211af897a5fcc065/Scripts/main.asm) · [source 2](https://github.com/1888games/PaperPlanesC64/blob/fe2f445a074d159dd499d2a6211af897a5fcc065/Scripts/game/gameplay/player.asm) · [source 3](https://github.com/1888games/PaperPlanesC64/blob/fe2f445a074d159dd499d2a6211af897a5fcc065/Scripts/game/system/irq.asm) · [source 4](https://github.com/1888games/PaperPlanesC64/blob/fe2f445a074d159dd499d2a6211af897a5fcc065/Scripts/data/assets.asm) · [source 5](https://github.com/1888games/PaperPlanesC64/blob/fe2f445a074d159dd499d2a6211af897a5fcc065/README.md) · [source 6](https://github.com/1888games/PaperPlanesC64/blob/fe2f445a074d159dd499d2a6211af897a5fcc065/Scripts/bin/main_BuildLog.txt) · [source 7](https://github.com/1888games/PaperPlanesC64/commit/fe2f445a074d159dd499d2a6211af897a5fcc065)

**Classification (reviewed):** Native C64 authored game source, with direct game logic and VIC-II/SID/CIA interaction rather than a game-specific CPU emulator. README credits Sam Demaine’s Ludum Dare 47 game. Original host OS and original executable analysis are not established; do not invent original-platform or source-CPU fields. Target is C64, while source_platforms/source_cpu/source_language remain empty because no original binary was recovered or analysed. work_kinds=reimplementation describes the evidenced game adaptation, not binary-derived reverse engineering.

Evidence: [source 1](https://github.com/1888games/PaperPlanesC64/blob/fe2f445a074d159dd499d2a6211af897a5fcc065/Scripts/main.asm) · [source 2](https://github.com/1888games/PaperPlanesC64/blob/fe2f445a074d159dd499d2a6211af897a5fcc065/Scripts/game/gameplay/player.asm) · [source 3](https://github.com/1888games/PaperPlanesC64/blob/fe2f445a074d159dd499d2a6211af897a5fcc065/Scripts/game/system/irq.asm) · [source 4](https://github.com/1888games/PaperPlanesC64/blob/fe2f445a074d159dd499d2a6211af897a5fcc065/Scripts/data/assets.asm) · [source 5](https://github.com/1888games/PaperPlanesC64/blob/fe2f445a074d159dd499d2a6211af897a5fcc065/README.md) · [source 6](https://github.com/1888games/PaperPlanesC64/blob/fe2f445a074d159dd499d2a6211af897a5fcc065/Scripts/bin/main_BuildLog.txt)

**Source architecture (not-applicable):** This is authored or adapted game source, not a disassembled/recovered original executable. Game inspiration does not establish the original binary ISA; source_cpu stays empty/not-applicable.

Evidence: [source 1](https://github.com/1888games/PaperPlanesC64/blob/fe2f445a074d159dd499d2a6211af897a5fcc065/Scripts/main.asm) · [source 2](https://github.com/1888games/PaperPlanesC64/blob/fe2f445a074d159dd499d2a6211af897a5fcc065/Scripts/game/gameplay/player.asm) · [source 3](https://github.com/1888games/PaperPlanesC64/blob/fe2f445a074d159dd499d2a6211af897a5fcc065/Scripts/game/system/irq.asm) · [source 4](https://github.com/1888games/PaperPlanesC64/blob/fe2f445a074d159dd499d2a6211af897a5fcc065/Scripts/data/assets.asm) · [source 5](https://github.com/1888games/PaperPlanesC64/blob/fe2f445a074d159dd499d2a6211af897a5fcc065/README.md) · [source 6](https://github.com/1888games/PaperPlanesC64/blob/fe2f445a074d159dd499d2a6211af897a5fcc065/Scripts/bin/main_BuildLog.txt)

**Target architecture (reviewed):** Reviewed assembly contains 6502-family LDA/STA/JSR and native hardware-access code, with a C64 assembler/entrypoint. target_cpu=6502 records the observed instruction set; it does not assert an exact 6510 silicon subtype, numerical CPU/RAM minimum, or successfully assembled output.

Evidence: [source 1](https://github.com/1888games/PaperPlanesC64/blob/fe2f445a074d159dd499d2a6211af897a5fcc065/Scripts/main.asm) · [source 2](https://github.com/1888games/PaperPlanesC64/blob/fe2f445a074d159dd499d2a6211af897a5fcc065/Scripts/bin/main_BuildLog.txt) · [source 3](https://github.com/1888games/PaperPlanesC64/blob/fe2f445a074d159dd499d2a6211af897a5fcc065/Scripts/game/gameplay/player.asm) · [source 4](https://github.com/1888games/PaperPlanesC64/blob/fe2f445a074d159dd499d2a6211af897a5fcc065/Scripts/game/system/irq.asm) · [source 5](https://github.com/1888games/PaperPlanesC64/blob/fe2f445a074d159dd499d2a6211af897a5fcc065/Scripts/data/assets.asm) · [source 6](https://github.com/1888games/PaperPlanesC64/blob/fe2f445a074d159dd499d2a6211af897a5fcc065/README.md)

**Build and verification (needs-research):** Selected main assembly and included assets define the native KickAssembler program; checked-in PRGs, symbols and historical build logs are upstream artifacts, not a current successful build. No portable automated build recipe was established. No independent assembly, runtime, original-ROM equivalence or hardware test was performed. Checked-in PRGs and historical build logs are upstream artifacts only. No explicit license was found in the inspected standalone README/source material or license-named tree entries. Public source visibility does not establish redistribution rights, including rights in game graphics, names and music. Build portability needs review: several imports use lowercase assets while the tree stores Assets, along with historical relative-path conventions. No clean case-sensitive-host rebuild was attempted. The original game’s precise operating-system/platform target is not evidenced, so no speculative source-platform label is assigned. No candidate compilation, execution, emulator/gameplay test, hardware test, round-trip or byte comparison was run. compilable/runnable/playable/byte_exact all remain null.

Evidence: [source 1](https://github.com/1888games/PaperPlanesC64/blob/fe2f445a074d159dd499d2a6211af897a5fcc065/Scripts/main.asm) · [source 2](https://github.com/1888games/PaperPlanesC64/blob/fe2f445a074d159dd499d2a6211af897a5fcc065/Scripts/bin/main_BuildLog.txt) · [source 3](https://github.com/1888games/PaperPlanesC64/blob/fe2f445a074d159dd499d2a6211af897a5fcc065/Scripts/game/gameplay/player.asm) · [source 4](https://github.com/1888games/PaperPlanesC64/blob/fe2f445a074d159dd499d2a6211af897a5fcc065/Scripts/game/system/irq.asm) · [source 5](https://github.com/1888games/PaperPlanesC64/blob/fe2f445a074d159dd499d2a6211af897a5fcc065/Scripts/data/assets.asm) · [source 6](https://github.com/1888games/PaperPlanesC64/blob/fe2f445a074d159dd499d2a6211af897a5fcc065/README.md)

**Runtime requirements (no-evidence-found):** No sufficiently specific supported minimum hardware configuration was established for a runtime profile. Target C64 and observed native ISA are not evidence of a tested CPU/RAM minimum. Video/timing evidence: Native MOS 6510 C64 target with VIC-II/SID and PAL/NTSC detector/timing branches. Gameplay and timing remain unverified. Relevant limits:

Evidence: [source 1](https://github.com/1888games/PaperPlanesC64/blob/fe2f445a074d159dd499d2a6211af897a5fcc065/Scripts/main.asm) · [source 2](https://github.com/1888games/PaperPlanesC64/blob/fe2f445a074d159dd499d2a6211af897a5fcc065/Scripts/game/gameplay/player.asm) · [source 3](https://github.com/1888games/PaperPlanesC64/blob/fe2f445a074d159dd499d2a6211af897a5fcc065/Scripts/game/system/irq.asm) · [source 4](https://github.com/1888games/PaperPlanesC64/blob/fe2f445a074d159dd499d2a6211af897a5fcc065/Scripts/data/assets.asm) · [source 5](https://github.com/1888games/PaperPlanesC64/blob/fe2f445a074d159dd499d2a6211af897a5fcc065/README.md) · [source 6](https://github.com/1888games/PaperPlanesC64/blob/fe2f445a074d159dd499d2a6211af897a5fcc065/Scripts/bin/main_BuildLog.txt)

**AI attribution (no-evidence-found):** No explicit generative-AI attribution found in the selected README, implementation, build or license material and the first eight default-branch commit messages/author metadata (or all returned if fewer). One selected commit detail was read where recorded. This bounded review is not proof of non-use. Opponent gameplay AI is not generative-AI tooling evidence. Unknown is not evidence of non-use; named tools are not inferred from provider addresses, ordinary automation or gameplay AI.

Evidence: [source 1](https://api.github.com/repos/1888games/PaperPlanesC64/commits?per_page=8&page=1) · [source 2](https://github.com/1888games/PaperPlanesC64/commit/fe2f445a074d159dd499d2a6211af897a5fcc065) · [source 3](https://github.com/1888games/PaperPlanesC64/blob/fe2f445a074d159dd499d2a6211af897a5fcc065/Scripts/main.asm) · [source 4](https://github.com/1888games/PaperPlanesC64/blob/fe2f445a074d159dd499d2a6211af897a5fcc065/Scripts/game/gameplay/player.asm) · [source 5](https://github.com/1888games/PaperPlanesC64/blob/fe2f445a074d159dd499d2a6211af897a5fcc065/Scripts/game/system/irq.asm) · [source 6](https://github.com/1888games/PaperPlanesC64/blob/fe2f445a074d159dd499d2a6211af897a5fcc065/Scripts/data/assets.asm) · [source 7](https://github.com/1888games/PaperPlanesC64/blob/fe2f445a074d159dd499d2a6211af897a5fcc065/README.md) · [source 8](https://github.com/1888games/PaperPlanesC64/blob/fe2f445a074d159dd499d2a6211af897a5fcc065/Scripts/bin/main_BuildLog.txt)

**Lineage and rights (reviewed):** overlapping collection; not a second project 1888games/ArlasoftC64 The overlapping Arlasoft Complete folder is supporting provenance, not another project. Blob comparison found 76 matching standalone blobs; main-source match paths: Complete/PaperPlanesC64/Scripts/main.asm. Licensing: No standalone license grant established; metadata license is null and no license-named file occurs in the complete tree. Canonical root was absent from the verified 1,621-project d654a0c publication baseline and 1,861-root normalized reviewed index. Wider lineage/source coverage is still partial.

Evidence: [source 1](https://github.com/1888games/PaperPlanesC64/blob/fe2f445a074d159dd499d2a6211af897a5fcc065/Scripts/main.asm) · [source 2](https://github.com/1888games/PaperPlanesC64/blob/fe2f445a074d159dd499d2a6211af897a5fcc065/Scripts/game/gameplay/player.asm) · [source 3](https://github.com/1888games/PaperPlanesC64/blob/fe2f445a074d159dd499d2a6211af897a5fcc065/Scripts/game/system/irq.asm) · [source 4](https://github.com/1888games/PaperPlanesC64/blob/fe2f445a074d159dd499d2a6211af897a5fcc065/Scripts/data/assets.asm) · [source 5](https://github.com/1888games/PaperPlanesC64/blob/fe2f445a074d159dd499d2a6211af897a5fcc065/README.md) · [source 6](https://github.com/1888games/PaperPlanesC64/blob/fe2f445a074d159dd499d2a6211af897a5fcc065/Scripts/bin/main_BuildLog.txt) · [source 7](https://github.com/1888games/ArlasoftC64/blob/7f70676ee2166e493e9669370f226813ea1cd5cb/README.md)

### Fire: native C64 Game & Watch adaptation source

[Repository](https://github.com/1888games/Fire-Game-Watch)

- Source platforms: Unasserted / not applicable
- Target platforms: C64
- Source CPU: Unasserted / not applicable
- Target CPU: 6502
- Source material/language: Unasserted / not applicable
- Maintained language: 6502 assembly (KickAssembler)
- Classification: subject; game, reimplementation
- Build flags: all unknown (compilable, runnable, playable and byte_exact).
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** README names the Game & Watch Fire adaptation and 6502/KickAssembler development. scripts/main.asm defaults target to C64 and runs the rescue/game-state loop; jumpers.asm implements jumper positions, saved-jumper progression and bounce state. Lionel/c64.asm accesses SID, CIA and C64 memory-bank hardware. The code also contains conditional PET, VIC and 264 branches and corresponding support modules. Only the default C64 target was substantively inspected; the alternate target comments are not independent compatibility verification. Inspected snapshot: branch master, head commit 565892aeb25dcb0917dd5d53a87a98f48eb925dd, git tree d185c129ed03792929581c6f3a8308876974c06c. Head and tree are separate identities; the connector tree response top-level sha was not used as the actual tree identity. Inspection is a bounded sample, not all code/features.

Evidence: [source 1](https://github.com/1888games/Fire-Game-Watch/blob/565892aeb25dcb0917dd5d53a87a98f48eb925dd/scripts/main.asm) · [source 2](https://github.com/1888games/Fire-Game-Watch/blob/565892aeb25dcb0917dd5d53a87a98f48eb925dd/scripts/interrupts/jumpers.asm) · [source 3](https://github.com/1888games/Fire-Game-Watch/blob/565892aeb25dcb0917dd5d53a87a98f48eb925dd/scripts/setup/loadModules.asm) · [source 4](https://github.com/1888games/Fire-Game-Watch/blob/565892aeb25dcb0917dd5d53a87a98f48eb925dd/Lionel/c64.asm) · [source 5](https://github.com/1888games/Fire-Game-Watch/blob/565892aeb25dcb0917dd5d53a87a98f48eb925dd/README.md) · [source 6](https://github.com/1888games/Fire-Game-Watch/blob/565892aeb25dcb0917dd5d53a87a98f48eb925dd/scripts/bin/main_BuildLog.txt) · [source 7](https://github.com/1888games/Fire-Game-Watch/commit/565892aeb25dcb0917dd5d53a87a98f48eb925dd)

**Classification (reviewed):** Native C64 authored game source, with direct game logic and VIC-II/SID/CIA interaction rather than a game-specific CPU emulator. The Nintendo Game & Watch original is the gameplay inspiration, not an analysed handheld binary. This source defaults target=C64; PET/VIC/264 code branches are not separately reviewed runtime outputs. Target is C64, while source_platforms/source_cpu/source_language remain empty because no original binary was recovered or analysed. work_kinds=reimplementation describes the evidenced game adaptation, not binary-derived reverse engineering.

Evidence: [source 1](https://github.com/1888games/Fire-Game-Watch/blob/565892aeb25dcb0917dd5d53a87a98f48eb925dd/scripts/main.asm) · [source 2](https://github.com/1888games/Fire-Game-Watch/blob/565892aeb25dcb0917dd5d53a87a98f48eb925dd/scripts/interrupts/jumpers.asm) · [source 3](https://github.com/1888games/Fire-Game-Watch/blob/565892aeb25dcb0917dd5d53a87a98f48eb925dd/scripts/setup/loadModules.asm) · [source 4](https://github.com/1888games/Fire-Game-Watch/blob/565892aeb25dcb0917dd5d53a87a98f48eb925dd/Lionel/c64.asm) · [source 5](https://github.com/1888games/Fire-Game-Watch/blob/565892aeb25dcb0917dd5d53a87a98f48eb925dd/README.md) · [source 6](https://github.com/1888games/Fire-Game-Watch/blob/565892aeb25dcb0917dd5d53a87a98f48eb925dd/scripts/bin/main_BuildLog.txt)

**Source architecture (not-applicable):** This is authored or adapted game source, not a disassembled/recovered original executable. Game inspiration does not establish the original binary ISA; source_cpu stays empty/not-applicable.

Evidence: [source 1](https://github.com/1888games/Fire-Game-Watch/blob/565892aeb25dcb0917dd5d53a87a98f48eb925dd/scripts/main.asm) · [source 2](https://github.com/1888games/Fire-Game-Watch/blob/565892aeb25dcb0917dd5d53a87a98f48eb925dd/scripts/interrupts/jumpers.asm) · [source 3](https://github.com/1888games/Fire-Game-Watch/blob/565892aeb25dcb0917dd5d53a87a98f48eb925dd/scripts/setup/loadModules.asm) · [source 4](https://github.com/1888games/Fire-Game-Watch/blob/565892aeb25dcb0917dd5d53a87a98f48eb925dd/Lionel/c64.asm) · [source 5](https://github.com/1888games/Fire-Game-Watch/blob/565892aeb25dcb0917dd5d53a87a98f48eb925dd/README.md) · [source 6](https://github.com/1888games/Fire-Game-Watch/blob/565892aeb25dcb0917dd5d53a87a98f48eb925dd/scripts/bin/main_BuildLog.txt)

**Target architecture (reviewed):** Reviewed assembly contains 6502-family LDA/STA/JSR and native hardware-access code, with a C64 assembler/entrypoint. target_cpu=6502 records the observed instruction set; it does not assert an exact 6510 silicon subtype, numerical CPU/RAM minimum, or successfully assembled output.

Evidence: [source 1](https://github.com/1888games/Fire-Game-Watch/blob/565892aeb25dcb0917dd5d53a87a98f48eb925dd/scripts/main.asm) · [source 2](https://github.com/1888games/Fire-Game-Watch/blob/565892aeb25dcb0917dd5d53a87a98f48eb925dd/scripts/bin/main_BuildLog.txt) · [source 3](https://github.com/1888games/Fire-Game-Watch/blob/565892aeb25dcb0917dd5d53a87a98f48eb925dd/scripts/interrupts/jumpers.asm) · [source 4](https://github.com/1888games/Fire-Game-Watch/blob/565892aeb25dcb0917dd5d53a87a98f48eb925dd/scripts/setup/loadModules.asm) · [source 5](https://github.com/1888games/Fire-Game-Watch/blob/565892aeb25dcb0917dd5d53a87a98f48eb925dd/Lionel/c64.asm) · [source 6](https://github.com/1888games/Fire-Game-Watch/blob/565892aeb25dcb0917dd5d53a87a98f48eb925dd/README.md)

**Build and verification (needs-research):** Selected main assembly and included assets define the native KickAssembler program; checked-in PRGs, symbols and historical build logs are upstream artifacts, not a current successful build. No portable automated build recipe was established. No independent assembly, runtime, original-ROM equivalence or hardware test was performed. Checked-in PRGs and historical build logs are upstream artifacts only. No explicit license was found in the inspected standalone README/source material or license-named tree entries. Public source visibility does not establish redistribution rights, including rights in game graphics, names and music. Source includes fixed raster waits and target-specific memory placements; PAL/NTSC behavior has not been established. The reused BASICStub string still says Caveman; that is a framework residue, not evidence this is the already-tracked Caveman project. No candidate compilation, execution, emulator/gameplay test, hardware test, round-trip or byte comparison was run. compilable/runnable/playable/byte_exact all remain null.

Evidence: [source 1](https://github.com/1888games/Fire-Game-Watch/blob/565892aeb25dcb0917dd5d53a87a98f48eb925dd/scripts/main.asm) · [source 2](https://github.com/1888games/Fire-Game-Watch/blob/565892aeb25dcb0917dd5d53a87a98f48eb925dd/scripts/bin/main_BuildLog.txt) · [source 3](https://github.com/1888games/Fire-Game-Watch/blob/565892aeb25dcb0917dd5d53a87a98f48eb925dd/scripts/interrupts/jumpers.asm) · [source 4](https://github.com/1888games/Fire-Game-Watch/blob/565892aeb25dcb0917dd5d53a87a98f48eb925dd/scripts/setup/loadModules.asm) · [source 5](https://github.com/1888games/Fire-Game-Watch/blob/565892aeb25dcb0917dd5d53a87a98f48eb925dd/Lionel/c64.asm) · [source 6](https://github.com/1888games/Fire-Game-Watch/blob/565892aeb25dcb0917dd5d53a87a98f48eb925dd/README.md)

**Runtime requirements (no-evidence-found):** No sufficiently specific supported minimum hardware configuration was established for a runtime profile. Target C64 and observed native ISA are not evidence of a tested CPU/RAM minimum. Video/timing evidence: Default build selects C64/MOS 6510. Other Commodore selectors exist but are not claimed as reviewed runnable targets; PAL/NTSC support unverified. Relevant limits: Source includes fixed raster waits and target-specific memory placements; PAL/NTSC behavior has not been established.

Evidence: [source 1](https://github.com/1888games/Fire-Game-Watch/blob/565892aeb25dcb0917dd5d53a87a98f48eb925dd/scripts/main.asm) · [source 2](https://github.com/1888games/Fire-Game-Watch/blob/565892aeb25dcb0917dd5d53a87a98f48eb925dd/scripts/interrupts/jumpers.asm) · [source 3](https://github.com/1888games/Fire-Game-Watch/blob/565892aeb25dcb0917dd5d53a87a98f48eb925dd/scripts/setup/loadModules.asm) · [source 4](https://github.com/1888games/Fire-Game-Watch/blob/565892aeb25dcb0917dd5d53a87a98f48eb925dd/Lionel/c64.asm) · [source 5](https://github.com/1888games/Fire-Game-Watch/blob/565892aeb25dcb0917dd5d53a87a98f48eb925dd/README.md) · [source 6](https://github.com/1888games/Fire-Game-Watch/blob/565892aeb25dcb0917dd5d53a87a98f48eb925dd/scripts/bin/main_BuildLog.txt)

**AI attribution (no-evidence-found):** No explicit generative-AI attribution found in the selected README, implementation, build or license material and the first eight default-branch commit messages/author metadata (or all returned if fewer). One selected commit detail was read where recorded. This bounded review is not proof of non-use. Opponent gameplay AI is not generative-AI tooling evidence. Unknown is not evidence of non-use; named tools are not inferred from provider addresses, ordinary automation or gameplay AI.

Evidence: [source 1](https://api.github.com/repos/1888games/Fire-Game-Watch/commits?per_page=8&page=1) · [source 2](https://github.com/1888games/Fire-Game-Watch/commit/565892aeb25dcb0917dd5d53a87a98f48eb925dd) · [source 3](https://github.com/1888games/Fire-Game-Watch/blob/565892aeb25dcb0917dd5d53a87a98f48eb925dd/scripts/main.asm) · [source 4](https://github.com/1888games/Fire-Game-Watch/blob/565892aeb25dcb0917dd5d53a87a98f48eb925dd/scripts/interrupts/jumpers.asm) · [source 5](https://github.com/1888games/Fire-Game-Watch/blob/565892aeb25dcb0917dd5d53a87a98f48eb925dd/scripts/setup/loadModules.asm) · [source 6](https://github.com/1888games/Fire-Game-Watch/blob/565892aeb25dcb0917dd5d53a87a98f48eb925dd/Lionel/c64.asm) · [source 7](https://github.com/1888games/Fire-Game-Watch/blob/565892aeb25dcb0917dd5d53a87a98f48eb925dd/README.md) · [source 8](https://github.com/1888games/Fire-Game-Watch/blob/565892aeb25dcb0917dd5d53a87a98f48eb925dd/scripts/bin/main_BuildLog.txt)

**Lineage and rights (reviewed):** overlapping collection; not a second project 1888games/ArlasoftC64 The overlapping Arlasoft Complete folder is supporting provenance, not another project. Blob comparison found 73 matching standalone blobs; main-source match paths: Complete/Fire/scripts/main.asm. Licensing: No standalone license grant established; metadata license is null and no license-named file occurs in the complete tree. Canonical root was absent from the verified 1,621-project d654a0c publication baseline and 1,861-root normalized reviewed index. Wider lineage/source coverage is still partial.

Evidence: [source 1](https://github.com/1888games/Fire-Game-Watch/blob/565892aeb25dcb0917dd5d53a87a98f48eb925dd/scripts/main.asm) · [source 2](https://github.com/1888games/Fire-Game-Watch/blob/565892aeb25dcb0917dd5d53a87a98f48eb925dd/scripts/interrupts/jumpers.asm) · [source 3](https://github.com/1888games/Fire-Game-Watch/blob/565892aeb25dcb0917dd5d53a87a98f48eb925dd/scripts/setup/loadModules.asm) · [source 4](https://github.com/1888games/Fire-Game-Watch/blob/565892aeb25dcb0917dd5d53a87a98f48eb925dd/Lionel/c64.asm) · [source 5](https://github.com/1888games/Fire-Game-Watch/blob/565892aeb25dcb0917dd5d53a87a98f48eb925dd/README.md) · [source 6](https://github.com/1888games/Fire-Game-Watch/blob/565892aeb25dcb0917dd5d53a87a98f48eb925dd/scripts/bin/main_BuildLog.txt) · [source 7](https://github.com/1888games/ArlasoftC64/blob/7f70676ee2166e493e9669370f226813ea1cd5cb/README.md)

### 10x10: native C64 puzzle-game source

[Repository](https://github.com/1888games/10x10-C64-)

- Source platforms: Unasserted / not applicable
- Target platforms: C64
- Source CPU: Unasserted / not applicable
- Target CPU: 6502
- Source material/language: Unasserted / not applicable
- Maintained language: 6502 assembly (KickAssembler)
- Classification: subject; game, reimplementation
- Build flags: all unknown (compilable, runnable, playable and byte_exact).
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** README names 1010 and the 6502/KickAssembler implementation. grid.asm implements a 10-by-10 board, placement validation, row/column completion, clearing bonuses and game-over searches; main.asm imports input, mouse/pointer, pieces, score and SID support. main.asm detects the machine via raster register changes and sets an NTSC pointer-movement speed. A historical build log records native PRG output and a C64 memory map. Inspected snapshot: branch master, head commit d56a79c7ed6022dd3fee26c470ad8ee4762a1884, git tree 5d091a5185ab5f44eaf5ba9965e33c28d646f136. Head and tree are separate identities; the connector tree response top-level sha was not used as the actual tree identity. Inspection is a bounded sample, not all code/features.

Evidence: [source 1](https://github.com/1888games/10x10-C64-/blob/d56a79c7ed6022dd3fee26c470ad8ee4762a1884/scripts/main.asm) · [source 2](https://github.com/1888games/10x10-C64-/blob/d56a79c7ed6022dd3fee26c470ad8ee4762a1884/scripts/interrupts/grid.asm) · [source 3](https://github.com/1888games/10x10-C64-/blob/d56a79c7ed6022dd3fee26c470ad8ee4762a1884/scripts/interrupts/irq.asm) · [source 4](https://github.com/1888games/10x10-C64-/blob/d56a79c7ed6022dd3fee26c470ad8ee4762a1884/scripts/setup/assets.asm) · [source 5](https://github.com/1888games/10x10-C64-/blob/d56a79c7ed6022dd3fee26c470ad8ee4762a1884/README.md) · [source 6](https://github.com/1888games/10x10-C64-/blob/d56a79c7ed6022dd3fee26c470ad8ee4762a1884/scripts/bin/main_BuildLog.txt) · [source 7](https://github.com/1888games/10x10-C64-/commit/d56a79c7ed6022dd3fee26c470ad8ee4762a1884)

**Classification (reviewed):** Native C64 authored game source, with direct game logic and VIC-II/SID/CIA interaction rather than a game-specific CPU emulator. README identifies the mobile puzzle game 1010. No original mobile OS or binary analysis is evidenced; its conceptual origin is preserved here without adding a source platform or CPU. Target is C64, while source_platforms/source_cpu/source_language remain empty because no original binary was recovered or analysed. work_kinds=reimplementation describes the evidenced game adaptation, not binary-derived reverse engineering.

Evidence: [source 1](https://github.com/1888games/10x10-C64-/blob/d56a79c7ed6022dd3fee26c470ad8ee4762a1884/scripts/main.asm) · [source 2](https://github.com/1888games/10x10-C64-/blob/d56a79c7ed6022dd3fee26c470ad8ee4762a1884/scripts/interrupts/grid.asm) · [source 3](https://github.com/1888games/10x10-C64-/blob/d56a79c7ed6022dd3fee26c470ad8ee4762a1884/scripts/interrupts/irq.asm) · [source 4](https://github.com/1888games/10x10-C64-/blob/d56a79c7ed6022dd3fee26c470ad8ee4762a1884/scripts/setup/assets.asm) · [source 5](https://github.com/1888games/10x10-C64-/blob/d56a79c7ed6022dd3fee26c470ad8ee4762a1884/README.md) · [source 6](https://github.com/1888games/10x10-C64-/blob/d56a79c7ed6022dd3fee26c470ad8ee4762a1884/scripts/bin/main_BuildLog.txt)

**Source architecture (not-applicable):** This is authored or adapted game source, not a disassembled/recovered original executable. Game inspiration does not establish the original binary ISA; source_cpu stays empty/not-applicable.

Evidence: [source 1](https://github.com/1888games/10x10-C64-/blob/d56a79c7ed6022dd3fee26c470ad8ee4762a1884/scripts/main.asm) · [source 2](https://github.com/1888games/10x10-C64-/blob/d56a79c7ed6022dd3fee26c470ad8ee4762a1884/scripts/interrupts/grid.asm) · [source 3](https://github.com/1888games/10x10-C64-/blob/d56a79c7ed6022dd3fee26c470ad8ee4762a1884/scripts/interrupts/irq.asm) · [source 4](https://github.com/1888games/10x10-C64-/blob/d56a79c7ed6022dd3fee26c470ad8ee4762a1884/scripts/setup/assets.asm) · [source 5](https://github.com/1888games/10x10-C64-/blob/d56a79c7ed6022dd3fee26c470ad8ee4762a1884/README.md) · [source 6](https://github.com/1888games/10x10-C64-/blob/d56a79c7ed6022dd3fee26c470ad8ee4762a1884/scripts/bin/main_BuildLog.txt)

**Target architecture (reviewed):** Reviewed assembly contains 6502-family LDA/STA/JSR and native hardware-access code, with a C64 assembler/entrypoint. target_cpu=6502 records the observed instruction set; it does not assert an exact 6510 silicon subtype, numerical CPU/RAM minimum, or successfully assembled output.

Evidence: [source 1](https://github.com/1888games/10x10-C64-/blob/d56a79c7ed6022dd3fee26c470ad8ee4762a1884/scripts/main.asm) · [source 2](https://github.com/1888games/10x10-C64-/blob/d56a79c7ed6022dd3fee26c470ad8ee4762a1884/scripts/bin/main_BuildLog.txt) · [source 3](https://github.com/1888games/10x10-C64-/blob/d56a79c7ed6022dd3fee26c470ad8ee4762a1884/scripts/interrupts/grid.asm) · [source 4](https://github.com/1888games/10x10-C64-/blob/d56a79c7ed6022dd3fee26c470ad8ee4762a1884/scripts/interrupts/irq.asm) · [source 5](https://github.com/1888games/10x10-C64-/blob/d56a79c7ed6022dd3fee26c470ad8ee4762a1884/scripts/setup/assets.asm) · [source 6](https://github.com/1888games/10x10-C64-/blob/d56a79c7ed6022dd3fee26c470ad8ee4762a1884/README.md)

**Build and verification (needs-research):** Selected main assembly and included assets define the native KickAssembler program; checked-in PRGs, symbols and historical build logs are upstream artifacts, not a current successful build. No portable automated build recipe was established. No independent assembly, runtime, original-ROM equivalence or hardware test was performed. Checked-in PRGs and historical build logs are upstream artifacts only. No explicit license was found in the inspected standalone README/source material or license-named tree entries. Public source visibility does not establish redistribution rights, including rights in game graphics, names and music. Build portability needs review: several imports use lowercase assets while the tree stores Assets, along with historical relative-path conventions. No clean case-sensitive-host rebuild was attempted. The detector adjusts pointer movement but does not by itself prove comprehensive PAL/NTSC compensation. Original mobile OS is deliberately left unspecified. No candidate compilation, execution, emulator/gameplay test, hardware test, round-trip or byte comparison was run. compilable/runnable/playable/byte_exact all remain null.

Evidence: [source 1](https://github.com/1888games/10x10-C64-/blob/d56a79c7ed6022dd3fee26c470ad8ee4762a1884/scripts/main.asm) · [source 2](https://github.com/1888games/10x10-C64-/blob/d56a79c7ed6022dd3fee26c470ad8ee4762a1884/scripts/bin/main_BuildLog.txt) · [source 3](https://github.com/1888games/10x10-C64-/blob/d56a79c7ed6022dd3fee26c470ad8ee4762a1884/scripts/interrupts/grid.asm) · [source 4](https://github.com/1888games/10x10-C64-/blob/d56a79c7ed6022dd3fee26c470ad8ee4762a1884/scripts/interrupts/irq.asm) · [source 5](https://github.com/1888games/10x10-C64-/blob/d56a79c7ed6022dd3fee26c470ad8ee4762a1884/scripts/setup/assets.asm) · [source 6](https://github.com/1888games/10x10-C64-/blob/d56a79c7ed6022dd3fee26c470ad8ee4762a1884/README.md)

**Runtime requirements (no-evidence-found):** No sufficiently specific supported minimum hardware configuration was established for a runtime profile. Target C64 and observed native ISA are not evidence of a tested CPU/RAM minimum. Video/timing evidence: Native MOS 6510 C64 target; VIC-II/SID and input routines. Source includes a PAL/NTSC detector and an NTSC pointer-speed adjustment. Relevant limits: The detector adjusts pointer movement but does not by itself prove comprehensive PAL/NTSC compensation. Original mobile OS is deliberately left unspecified.

Evidence: [source 1](https://github.com/1888games/10x10-C64-/blob/d56a79c7ed6022dd3fee26c470ad8ee4762a1884/scripts/main.asm) · [source 2](https://github.com/1888games/10x10-C64-/blob/d56a79c7ed6022dd3fee26c470ad8ee4762a1884/scripts/interrupts/grid.asm) · [source 3](https://github.com/1888games/10x10-C64-/blob/d56a79c7ed6022dd3fee26c470ad8ee4762a1884/scripts/interrupts/irq.asm) · [source 4](https://github.com/1888games/10x10-C64-/blob/d56a79c7ed6022dd3fee26c470ad8ee4762a1884/scripts/setup/assets.asm) · [source 5](https://github.com/1888games/10x10-C64-/blob/d56a79c7ed6022dd3fee26c470ad8ee4762a1884/README.md) · [source 6](https://github.com/1888games/10x10-C64-/blob/d56a79c7ed6022dd3fee26c470ad8ee4762a1884/scripts/bin/main_BuildLog.txt)

**AI attribution (no-evidence-found):** No explicit generative-AI attribution found in the selected README, implementation, build or license material and the first eight default-branch commit messages/author metadata (or all returned if fewer). One selected commit detail was read where recorded. This bounded review is not proof of non-use. Opponent gameplay AI is not generative-AI tooling evidence. Unknown is not evidence of non-use; named tools are not inferred from provider addresses, ordinary automation or gameplay AI.

Evidence: [source 1](https://api.github.com/repos/1888games/10x10-C64-/commits?per_page=8&page=1) · [source 2](https://github.com/1888games/10x10-C64-/commit/d56a79c7ed6022dd3fee26c470ad8ee4762a1884) · [source 3](https://github.com/1888games/10x10-C64-/blob/d56a79c7ed6022dd3fee26c470ad8ee4762a1884/scripts/main.asm) · [source 4](https://github.com/1888games/10x10-C64-/blob/d56a79c7ed6022dd3fee26c470ad8ee4762a1884/scripts/interrupts/grid.asm) · [source 5](https://github.com/1888games/10x10-C64-/blob/d56a79c7ed6022dd3fee26c470ad8ee4762a1884/scripts/interrupts/irq.asm) · [source 6](https://github.com/1888games/10x10-C64-/blob/d56a79c7ed6022dd3fee26c470ad8ee4762a1884/scripts/setup/assets.asm) · [source 7](https://github.com/1888games/10x10-C64-/blob/d56a79c7ed6022dd3fee26c470ad8ee4762a1884/README.md) · [source 8](https://github.com/1888games/10x10-C64-/blob/d56a79c7ed6022dd3fee26c470ad8ee4762a1884/scripts/bin/main_BuildLog.txt)

**Lineage and rights (reviewed):** overlapping collection; not a second project 1888games/ArlasoftC64 The overlapping Arlasoft Complete folder is supporting provenance, not another project. Blob comparison found 61 matching standalone blobs; main-source match paths: Complete/10x10/scripts/main.asm. Licensing: No standalone license grant established; metadata license is null and no license-named file occurs in the complete tree. Canonical root was absent from the verified 1,621-project d654a0c publication baseline and 1,861-root normalized reviewed index. Wider lineage/source coverage is still partial.

Evidence: [source 1](https://github.com/1888games/10x10-C64-/blob/d56a79c7ed6022dd3fee26c470ad8ee4762a1884/scripts/main.asm) · [source 2](https://github.com/1888games/10x10-C64-/blob/d56a79c7ed6022dd3fee26c470ad8ee4762a1884/scripts/interrupts/grid.asm) · [source 3](https://github.com/1888games/10x10-C64-/blob/d56a79c7ed6022dd3fee26c470ad8ee4762a1884/scripts/interrupts/irq.asm) · [source 4](https://github.com/1888games/10x10-C64-/blob/d56a79c7ed6022dd3fee26c470ad8ee4762a1884/scripts/setup/assets.asm) · [source 5](https://github.com/1888games/10x10-C64-/blob/d56a79c7ed6022dd3fee26c470ad8ee4762a1884/README.md) · [source 6](https://github.com/1888games/10x10-C64-/blob/d56a79c7ed6022dd3fee26c470ad8ee4762a1884/scripts/bin/main_BuildLog.txt) · [source 7](https://github.com/1888games/ArlasoftC64/blob/7f70676ee2166e493e9669370f226813ea1cd5cb/README.md)

### Infinite Space: native C64 shooter source

[Repository](https://github.com/1888games/Infinite-Space-C64-)

- Source platforms: Unasserted / not applicable
- Target platforms: C64
- Source CPU: Unasserted / not applicable
- Target CPU: 6502
- Source material/language: Unasserted / not applicable
- Maintained language: 6502 assembly (KickAssembler)
- Classification: subject; game
- Build flags: all unknown (compilable, runnable, playable and byte_exact).
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** README states KickAssembler for C64/Ludum Dare 47; main.asm credits Arlasoft, music by Richard Bayliss and 5 October 2020. ship.asm implements sprite positioning, lives, death and hit tests; the game loop imports enemy, controls, drawing, scoring and stars modules, with raster-driven sprite updates. Checked-in graphics and SID assets are linked from assembly; the tree includes a PRG and historical build log. Inspected snapshot: branch main, head commit 20616d27d409272ca25accc37714fa186434ce1d, git tree 31cdd41e9af45fa8e04a863adadfa88b277fef84. Head and tree are separate identities; the connector tree response top-level sha was not used as the actual tree identity. Inspection is a bounded sample, not all code/features.

Evidence: [source 1](https://github.com/1888games/Infinite-Space-C64-/blob/20616d27d409272ca25accc37714fa186434ce1d/scripts/main.asm) · [source 2](https://github.com/1888games/Infinite-Space-C64-/blob/20616d27d409272ca25accc37714fa186434ce1d/scripts/game/ship.asm) · [source 3](https://github.com/1888games/Infinite-Space-C64-/blob/20616d27d409272ca25accc37714fa186434ce1d/scripts/game/irq.asm) · [source 4](https://github.com/1888games/Infinite-Space-C64-/blob/20616d27d409272ca25accc37714fa186434ce1d/scripts/common/assets.asm) · [source 5](https://github.com/1888games/Infinite-Space-C64-/blob/20616d27d409272ca25accc37714fa186434ce1d/README.md) · [source 6](https://github.com/1888games/Infinite-Space-C64-/blob/20616d27d409272ca25accc37714fa186434ce1d/scripts/bin/main_BuildLog.txt) · [source 7](https://github.com/1888games/Infinite-Space-C64-/commit/20616d27d409272ca25accc37714fa186434ce1d)

**Classification (reviewed):** Native C64 authored game source, with direct game logic and VIC-II/SID/CIA interaction rather than a game-specific CPU emulator. Original C64 homebrew for Ludum Dare 47. There is no separately recovered historical binary; source-platform/CPU/language and reverse-engineering work kinds stay empty. Target is C64, while source_platforms/source_cpu/source_language remain empty because no original binary was recovered or analysed. Original homebrew is not assigned a binary-recovery work kind.

Evidence: [source 1](https://github.com/1888games/Infinite-Space-C64-/blob/20616d27d409272ca25accc37714fa186434ce1d/scripts/main.asm) · [source 2](https://github.com/1888games/Infinite-Space-C64-/blob/20616d27d409272ca25accc37714fa186434ce1d/scripts/game/ship.asm) · [source 3](https://github.com/1888games/Infinite-Space-C64-/blob/20616d27d409272ca25accc37714fa186434ce1d/scripts/game/irq.asm) · [source 4](https://github.com/1888games/Infinite-Space-C64-/blob/20616d27d409272ca25accc37714fa186434ce1d/scripts/common/assets.asm) · [source 5](https://github.com/1888games/Infinite-Space-C64-/blob/20616d27d409272ca25accc37714fa186434ce1d/README.md) · [source 6](https://github.com/1888games/Infinite-Space-C64-/blob/20616d27d409272ca25accc37714fa186434ce1d/scripts/bin/main_BuildLog.txt)

**Source architecture (not-applicable):** This is authored or adapted game source, not a disassembled/recovered original executable. Game inspiration does not establish the original binary ISA; source_cpu stays empty/not-applicable.

Evidence: [source 1](https://github.com/1888games/Infinite-Space-C64-/blob/20616d27d409272ca25accc37714fa186434ce1d/scripts/main.asm) · [source 2](https://github.com/1888games/Infinite-Space-C64-/blob/20616d27d409272ca25accc37714fa186434ce1d/scripts/game/ship.asm) · [source 3](https://github.com/1888games/Infinite-Space-C64-/blob/20616d27d409272ca25accc37714fa186434ce1d/scripts/game/irq.asm) · [source 4](https://github.com/1888games/Infinite-Space-C64-/blob/20616d27d409272ca25accc37714fa186434ce1d/scripts/common/assets.asm) · [source 5](https://github.com/1888games/Infinite-Space-C64-/blob/20616d27d409272ca25accc37714fa186434ce1d/README.md) · [source 6](https://github.com/1888games/Infinite-Space-C64-/blob/20616d27d409272ca25accc37714fa186434ce1d/scripts/bin/main_BuildLog.txt)

**Target architecture (reviewed):** Reviewed assembly contains 6502-family LDA/STA/JSR and native hardware-access code, with a C64 assembler/entrypoint. target_cpu=6502 records the observed instruction set; it does not assert an exact 6510 silicon subtype, numerical CPU/RAM minimum, or successfully assembled output.

Evidence: [source 1](https://github.com/1888games/Infinite-Space-C64-/blob/20616d27d409272ca25accc37714fa186434ce1d/scripts/main.asm) · [source 2](https://github.com/1888games/Infinite-Space-C64-/blob/20616d27d409272ca25accc37714fa186434ce1d/scripts/bin/main_BuildLog.txt) · [source 3](https://github.com/1888games/Infinite-Space-C64-/blob/20616d27d409272ca25accc37714fa186434ce1d/scripts/game/ship.asm) · [source 4](https://github.com/1888games/Infinite-Space-C64-/blob/20616d27d409272ca25accc37714fa186434ce1d/scripts/game/irq.asm) · [source 5](https://github.com/1888games/Infinite-Space-C64-/blob/20616d27d409272ca25accc37714fa186434ce1d/scripts/common/assets.asm) · [source 6](https://github.com/1888games/Infinite-Space-C64-/blob/20616d27d409272ca25accc37714fa186434ce1d/README.md)

**Build and verification (needs-research):** Selected main assembly and included assets define the native KickAssembler program; checked-in PRGs, symbols and historical build logs are upstream artifacts, not a current successful build. No portable automated build recipe was established. No independent assembly, runtime, original-ROM equivalence or hardware test was performed. Checked-in PRGs and historical build logs are upstream artifacts only. No explicit license was found in the inspected standalone README/source material or license-named tree entries. Public source visibility does not establish redistribution rights, including rights in game graphics, names and music. Build portability needs review: several imports use lowercase assets while the tree stores Assets, along with historical relative-path conventions. No clean case-sensitive-host rebuild was attempted. Music has a separately credited creator. No explicit music redistribution license was established. The historical build log contains an older LD46/backburner pathname; treat it as provenance only, not proof that current head assembles or that the documented event is LD46. No candidate compilation, execution, emulator/gameplay test, hardware test, round-trip or byte comparison was run. compilable/runnable/playable/byte_exact all remain null.

Evidence: [source 1](https://github.com/1888games/Infinite-Space-C64-/blob/20616d27d409272ca25accc37714fa186434ce1d/scripts/main.asm) · [source 2](https://github.com/1888games/Infinite-Space-C64-/blob/20616d27d409272ca25accc37714fa186434ce1d/scripts/bin/main_BuildLog.txt) · [source 3](https://github.com/1888games/Infinite-Space-C64-/blob/20616d27d409272ca25accc37714fa186434ce1d/scripts/game/ship.asm) · [source 4](https://github.com/1888games/Infinite-Space-C64-/blob/20616d27d409272ca25accc37714fa186434ce1d/scripts/game/irq.asm) · [source 5](https://github.com/1888games/Infinite-Space-C64-/blob/20616d27d409272ca25accc37714fa186434ce1d/scripts/common/assets.asm) · [source 6](https://github.com/1888games/Infinite-Space-C64-/blob/20616d27d409272ca25accc37714fa186434ce1d/README.md)

**Runtime requirements (no-evidence-found):** No sufficiently specific supported minimum hardware configuration was established for a runtime profile. Target C64 and observed native ISA are not evidence of a tested CPU/RAM minimum. Video/timing evidence: MOS 6510 C64 code with VIC-II/SID/CIA; fixed raster scheduling observed. PAL/NTSC equivalence not established. Relevant limits:

Evidence: [source 1](https://github.com/1888games/Infinite-Space-C64-/blob/20616d27d409272ca25accc37714fa186434ce1d/scripts/main.asm) · [source 2](https://github.com/1888games/Infinite-Space-C64-/blob/20616d27d409272ca25accc37714fa186434ce1d/scripts/game/ship.asm) · [source 3](https://github.com/1888games/Infinite-Space-C64-/blob/20616d27d409272ca25accc37714fa186434ce1d/scripts/game/irq.asm) · [source 4](https://github.com/1888games/Infinite-Space-C64-/blob/20616d27d409272ca25accc37714fa186434ce1d/scripts/common/assets.asm) · [source 5](https://github.com/1888games/Infinite-Space-C64-/blob/20616d27d409272ca25accc37714fa186434ce1d/README.md) · [source 6](https://github.com/1888games/Infinite-Space-C64-/blob/20616d27d409272ca25accc37714fa186434ce1d/scripts/bin/main_BuildLog.txt)

**AI attribution (no-evidence-found):** No explicit generative-AI attribution found in the selected README, implementation, build or license material and the first eight default-branch commit messages/author metadata (or all returned if fewer). One selected commit detail was read where recorded. This bounded review is not proof of non-use. Opponent gameplay AI is not generative-AI tooling evidence. Unknown is not evidence of non-use; named tools are not inferred from provider addresses, ordinary automation or gameplay AI.

Evidence: [source 1](https://api.github.com/repos/1888games/Infinite-Space-C64-/commits?per_page=8&page=1) · [source 2](https://github.com/1888games/Infinite-Space-C64-/commit/20616d27d409272ca25accc37714fa186434ce1d) · [source 3](https://github.com/1888games/Infinite-Space-C64-/blob/20616d27d409272ca25accc37714fa186434ce1d/scripts/main.asm) · [source 4](https://github.com/1888games/Infinite-Space-C64-/blob/20616d27d409272ca25accc37714fa186434ce1d/scripts/game/ship.asm) · [source 5](https://github.com/1888games/Infinite-Space-C64-/blob/20616d27d409272ca25accc37714fa186434ce1d/scripts/game/irq.asm) · [source 6](https://github.com/1888games/Infinite-Space-C64-/blob/20616d27d409272ca25accc37714fa186434ce1d/scripts/common/assets.asm) · [source 7](https://github.com/1888games/Infinite-Space-C64-/blob/20616d27d409272ca25accc37714fa186434ce1d/README.md) · [source 8](https://github.com/1888games/Infinite-Space-C64-/blob/20616d27d409272ca25accc37714fa186434ce1d/scripts/bin/main_BuildLog.txt)

**Lineage and rights (reviewed):** overlapping collection; not a second project 1888games/ArlasoftC64 The overlapping Arlasoft Complete folder is supporting provenance, not another project. Blob comparison found 30 matching standalone blobs; main-source match paths: Complete/Infinite Space/scripts/main.asm. Licensing: No standalone license grant established; metadata license is null and no license-named file occurs in the complete tree. Canonical root was absent from the verified 1,621-project d654a0c publication baseline and 1,861-root normalized reviewed index. Wider lineage/source coverage is still partial.

Evidence: [source 1](https://github.com/1888games/Infinite-Space-C64-/blob/20616d27d409272ca25accc37714fa186434ce1d/scripts/main.asm) · [source 2](https://github.com/1888games/Infinite-Space-C64-/blob/20616d27d409272ca25accc37714fa186434ce1d/scripts/game/ship.asm) · [source 3](https://github.com/1888games/Infinite-Space-C64-/blob/20616d27d409272ca25accc37714fa186434ce1d/scripts/game/irq.asm) · [source 4](https://github.com/1888games/Infinite-Space-C64-/blob/20616d27d409272ca25accc37714fa186434ce1d/scripts/common/assets.asm) · [source 5](https://github.com/1888games/Infinite-Space-C64-/blob/20616d27d409272ca25accc37714fa186434ce1d/README.md) · [source 6](https://github.com/1888games/Infinite-Space-C64-/blob/20616d27d409272ca25accc37714fa186434ce1d/scripts/bin/main_BuildLog.txt) · [source 7](https://github.com/1888games/ArlasoftC64/blob/7f70676ee2166e493e9669370f226813ea1cd5cb/README.md)

### Merge64: native C64 block-merging game source

[Repository](https://github.com/1888games/Merge64)

- Source platforms: Unasserted / not applicable
- Target platforms: C64
- Source CPU: Unasserted / not applicable
- Target CPU: 6502
- Source material/language: Unasserted / not applicable
- Maintained language: 6502 assembly (KickAssembler)
- Classification: subject; game, reimplementation
- Build flags: all unknown (compilable, runnable, playable and byte_exact).
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** README identifies Shoot ’n’ Merge and a weekend development origin. block.asm implements a five-by-eight grid, moving columns, fired blocks, merge queues, merge-chain checks, scoring and rising speed; irq.asm multiplexes five sprite rows. Native main.asm, generated asset inputs, a PRG and a historical assembler memory map are present. The Arlasoft collection contains a related snapshot, but the main-file blob differs from this standalone repository. Inspected snapshot: branch master, head commit d60989b3c8ef776f1a55cbd48a0ebad44411d62a, git tree 99fca58bf4a14d21f51dcc3700ca0f9d07f18695. Head and tree are separate identities; the connector tree response top-level sha was not used as the actual tree identity. Inspection is a bounded sample, not all code/features.

Evidence: [source 1](https://github.com/1888games/Merge64/blob/d60989b3c8ef776f1a55cbd48a0ebad44411d62a/scripts/main.asm) · [source 2](https://github.com/1888games/Merge64/blob/d60989b3c8ef776f1a55cbd48a0ebad44411d62a/scripts/game/block.asm) · [source 3](https://github.com/1888games/Merge64/blob/d60989b3c8ef776f1a55cbd48a0ebad44411d62a/scripts/game/irq.asm) · [source 4](https://github.com/1888games/Merge64/blob/d60989b3c8ef776f1a55cbd48a0ebad44411d62a/scripts/common/assets.asm) · [source 5](https://github.com/1888games/Merge64/blob/d60989b3c8ef776f1a55cbd48a0ebad44411d62a/README.md) · [source 6](https://github.com/1888games/Merge64/blob/d60989b3c8ef776f1a55cbd48a0ebad44411d62a/scripts/bin/main_BuildLog.txt) · [source 7](https://github.com/1888games/Merge64/commit/d60989b3c8ef776f1a55cbd48a0ebad44411d62a)

**Classification (reviewed):** Native C64 authored game source, with direct game logic and VIC-II/SID/CIA interaction rather than a game-specific CPU emulator. README identifies Shoot ’n’ Merge as inspiration, not an original mobile binary under analysis. The standalone and collection snapshots represent one game lineage. Target is C64, while source_platforms/source_cpu/source_language remain empty because no original binary was recovered or analysed. work_kinds=reimplementation describes the evidenced game adaptation, not binary-derived reverse engineering.

Evidence: [source 1](https://github.com/1888games/Merge64/blob/d60989b3c8ef776f1a55cbd48a0ebad44411d62a/scripts/main.asm) · [source 2](https://github.com/1888games/Merge64/blob/d60989b3c8ef776f1a55cbd48a0ebad44411d62a/scripts/game/block.asm) · [source 3](https://github.com/1888games/Merge64/blob/d60989b3c8ef776f1a55cbd48a0ebad44411d62a/scripts/game/irq.asm) · [source 4](https://github.com/1888games/Merge64/blob/d60989b3c8ef776f1a55cbd48a0ebad44411d62a/scripts/common/assets.asm) · [source 5](https://github.com/1888games/Merge64/blob/d60989b3c8ef776f1a55cbd48a0ebad44411d62a/README.md) · [source 6](https://github.com/1888games/Merge64/blob/d60989b3c8ef776f1a55cbd48a0ebad44411d62a/scripts/bin/main_BuildLog.txt)

**Source architecture (not-applicable):** This is authored or adapted game source, not a disassembled/recovered original executable. Game inspiration does not establish the original binary ISA; source_cpu stays empty/not-applicable.

Evidence: [source 1](https://github.com/1888games/Merge64/blob/d60989b3c8ef776f1a55cbd48a0ebad44411d62a/scripts/main.asm) · [source 2](https://github.com/1888games/Merge64/blob/d60989b3c8ef776f1a55cbd48a0ebad44411d62a/scripts/game/block.asm) · [source 3](https://github.com/1888games/Merge64/blob/d60989b3c8ef776f1a55cbd48a0ebad44411d62a/scripts/game/irq.asm) · [source 4](https://github.com/1888games/Merge64/blob/d60989b3c8ef776f1a55cbd48a0ebad44411d62a/scripts/common/assets.asm) · [source 5](https://github.com/1888games/Merge64/blob/d60989b3c8ef776f1a55cbd48a0ebad44411d62a/README.md) · [source 6](https://github.com/1888games/Merge64/blob/d60989b3c8ef776f1a55cbd48a0ebad44411d62a/scripts/bin/main_BuildLog.txt)

**Target architecture (reviewed):** Reviewed assembly contains 6502-family LDA/STA/JSR and native hardware-access code, with a C64 assembler/entrypoint. target_cpu=6502 records the observed instruction set; it does not assert an exact 6510 silicon subtype, numerical CPU/RAM minimum, or successfully assembled output.

Evidence: [source 1](https://github.com/1888games/Merge64/blob/d60989b3c8ef776f1a55cbd48a0ebad44411d62a/scripts/main.asm) · [source 2](https://github.com/1888games/Merge64/blob/d60989b3c8ef776f1a55cbd48a0ebad44411d62a/scripts/bin/main_BuildLog.txt) · [source 3](https://github.com/1888games/Merge64/blob/d60989b3c8ef776f1a55cbd48a0ebad44411d62a/scripts/game/block.asm) · [source 4](https://github.com/1888games/Merge64/blob/d60989b3c8ef776f1a55cbd48a0ebad44411d62a/scripts/game/irq.asm) · [source 5](https://github.com/1888games/Merge64/blob/d60989b3c8ef776f1a55cbd48a0ebad44411d62a/scripts/common/assets.asm) · [source 6](https://github.com/1888games/Merge64/blob/d60989b3c8ef776f1a55cbd48a0ebad44411d62a/README.md)

**Build and verification (needs-research):** Selected main assembly and included assets define the native KickAssembler program; checked-in PRGs, symbols and historical build logs are upstream artifacts, not a current successful build. No portable automated build recipe was established. No independent assembly, runtime, original-ROM equivalence or hardware test was performed. Checked-in PRGs and historical build logs are upstream artifacts only. No explicit license was found in the inspected standalone README/source material or license-named tree entries. Public source visibility does not establish redistribution rights, including rights in game graphics, names and music. Build portability needs review: several imports use lowercase assets while the tree stores Assets, along with historical relative-path conventions. No clean case-sensitive-host rebuild was attempted. DetectMachine stores a PAL/NTSC value, but its NTSC branch has no substantive compensation in the inspected entry code. No PAL/NTSC timing claim is made. Standalone and collection variants must be treated as one game lineage. No candidate compilation, execution, emulator/gameplay test, hardware test, round-trip or byte comparison was run. compilable/runnable/playable/byte_exact all remain null.

Evidence: [source 1](https://github.com/1888games/Merge64/blob/d60989b3c8ef776f1a55cbd48a0ebad44411d62a/scripts/main.asm) · [source 2](https://github.com/1888games/Merge64/blob/d60989b3c8ef776f1a55cbd48a0ebad44411d62a/scripts/bin/main_BuildLog.txt) · [source 3](https://github.com/1888games/Merge64/blob/d60989b3c8ef776f1a55cbd48a0ebad44411d62a/scripts/game/block.asm) · [source 4](https://github.com/1888games/Merge64/blob/d60989b3c8ef776f1a55cbd48a0ebad44411d62a/scripts/game/irq.asm) · [source 5](https://github.com/1888games/Merge64/blob/d60989b3c8ef776f1a55cbd48a0ebad44411d62a/scripts/common/assets.asm) · [source 6](https://github.com/1888games/Merge64/blob/d60989b3c8ef776f1a55cbd48a0ebad44411d62a/README.md)

**Runtime requirements (no-evidence-found):** No sufficiently specific supported minimum hardware configuration was established for a runtime profile. Target C64 and observed native ISA are not evidence of a tested CPU/RAM minimum. Video/timing evidence: Native C64/MOS 6510, VIC-II raster scheduling and SID. PAL/NTSC detector exists but effective timing normalization is unverified. Relevant limits: DetectMachine stores a PAL/NTSC value, but its NTSC branch has no substantive compensation in the inspected entry code. No PAL/NTSC timing claim is made.

Evidence: [source 1](https://github.com/1888games/Merge64/blob/d60989b3c8ef776f1a55cbd48a0ebad44411d62a/scripts/main.asm) · [source 2](https://github.com/1888games/Merge64/blob/d60989b3c8ef776f1a55cbd48a0ebad44411d62a/scripts/game/block.asm) · [source 3](https://github.com/1888games/Merge64/blob/d60989b3c8ef776f1a55cbd48a0ebad44411d62a/scripts/game/irq.asm) · [source 4](https://github.com/1888games/Merge64/blob/d60989b3c8ef776f1a55cbd48a0ebad44411d62a/scripts/common/assets.asm) · [source 5](https://github.com/1888games/Merge64/blob/d60989b3c8ef776f1a55cbd48a0ebad44411d62a/README.md) · [source 6](https://github.com/1888games/Merge64/blob/d60989b3c8ef776f1a55cbd48a0ebad44411d62a/scripts/bin/main_BuildLog.txt)

**AI attribution (no-evidence-found):** No explicit generative-AI attribution found in the selected README, implementation, build or license material and the first eight default-branch commit messages/author metadata (or all returned if fewer). One selected commit detail was read where recorded. This bounded review is not proof of non-use. Opponent gameplay AI is not generative-AI tooling evidence. Unknown is not evidence of non-use; named tools are not inferred from provider addresses, ordinary automation or gameplay AI.

Evidence: [source 1](https://api.github.com/repos/1888games/Merge64/commits?per_page=8&page=1) · [source 2](https://github.com/1888games/Merge64/commit/d60989b3c8ef776f1a55cbd48a0ebad44411d62a) · [source 3](https://github.com/1888games/Merge64/blob/d60989b3c8ef776f1a55cbd48a0ebad44411d62a/scripts/main.asm) · [source 4](https://github.com/1888games/Merge64/blob/d60989b3c8ef776f1a55cbd48a0ebad44411d62a/scripts/game/block.asm) · [source 5](https://github.com/1888games/Merge64/blob/d60989b3c8ef776f1a55cbd48a0ebad44411d62a/scripts/game/irq.asm) · [source 6](https://github.com/1888games/Merge64/blob/d60989b3c8ef776f1a55cbd48a0ebad44411d62a/scripts/common/assets.asm) · [source 7](https://github.com/1888games/Merge64/blob/d60989b3c8ef776f1a55cbd48a0ebad44411d62a/README.md) · [source 8](https://github.com/1888games/Merge64/blob/d60989b3c8ef776f1a55cbd48a0ebad44411d62a/scripts/bin/main_BuildLog.txt)

**Lineage and rights (reviewed):** overlapping collection; not a second project 1888games/ArlasoftC64 The overlapping Arlasoft Complete folder is supporting provenance, not another project. Blob comparison found 56 matching standalone blobs; main-source match paths: main source differs in this snapshot. Licensing: No standalone license grant established; metadata license is null and no license-named file occurs in the complete tree. Canonical root was absent from the verified 1,621-project d654a0c publication baseline and 1,861-root normalized reviewed index. Wider lineage/source coverage is still partial.

Evidence: [source 1](https://github.com/1888games/Merge64/blob/d60989b3c8ef776f1a55cbd48a0ebad44411d62a/scripts/main.asm) · [source 2](https://github.com/1888games/Merge64/blob/d60989b3c8ef776f1a55cbd48a0ebad44411d62a/scripts/game/block.asm) · [source 3](https://github.com/1888games/Merge64/blob/d60989b3c8ef776f1a55cbd48a0ebad44411d62a/scripts/game/irq.asm) · [source 4](https://github.com/1888games/Merge64/blob/d60989b3c8ef776f1a55cbd48a0ebad44411d62a/scripts/common/assets.asm) · [source 5](https://github.com/1888games/Merge64/blob/d60989b3c8ef776f1a55cbd48a0ebad44411d62a/README.md) · [source 6](https://github.com/1888games/Merge64/blob/d60989b3c8ef776f1a55cbd48a0ebad44411d62a/scripts/bin/main_BuildLog.txt) · [source 7](https://github.com/1888games/ArlasoftC64/blob/7f70676ee2166e493e9669370f226813ea1cd5cb/README.md)

### Snout About: native C64 competition-game source

[Repository](https://github.com/1888games/SnoutAbout_C64)

- Source platforms: Unasserted / not applicable
- Target platforms: C64
- Source CPU: Unasserted / not applicable
- Target CPU: 6502
- Source material/language: Unasserted / not applicable
- Maintained language: 6502 assembly (KickAssembler)
- Classification: subject; game
- Build flags: all unknown (compilable, runnable, playable and byte_exact).
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** README explicitly names the C64 4k competition and KickAssembler. snout.asm implements joystick-controlled nose extension/retraction, timed sniffing, character drawing and boundary logic; the IRQ runs nose, sprites, score, clouds and blinking updates. The program starts with a BASIC stub and assembles native game modules and binary character/sprite assets; a checked-in build log and PRG are present. Inspected snapshot: branch master, head commit c628291d2ac627d6bd5b55ef52f12d909a1c0131, git tree fb47ffe5a2dc9e1a499a2587f9614ef36522760f. Head and tree are separate identities; the connector tree response top-level sha was not used as the actual tree identity. Inspection is a bounded sample, not all code/features.

Evidence: [source 1](https://github.com/1888games/SnoutAbout_C64/blob/c628291d2ac627d6bd5b55ef52f12d909a1c0131/SnoutAbout/scripts/main.asm) · [source 2](https://github.com/1888games/SnoutAbout_C64/blob/c628291d2ac627d6bd5b55ef52f12d909a1c0131/SnoutAbout/scripts/interrupts/snout.asm) · [source 3](https://github.com/1888games/SnoutAbout_C64/blob/c628291d2ac627d6bd5b55ef52f12d909a1c0131/SnoutAbout/scripts/interrupts/irq.asm) · [source 4](https://github.com/1888games/SnoutAbout_C64/blob/c628291d2ac627d6bd5b55ef52f12d909a1c0131/SnoutAbout/scripts/setup/assets.asm) · [source 5](https://github.com/1888games/SnoutAbout_C64/blob/c628291d2ac627d6bd5b55ef52f12d909a1c0131/README.md) · [source 6](https://github.com/1888games/SnoutAbout_C64/blob/c628291d2ac627d6bd5b55ef52f12d909a1c0131/SnoutAbout/scripts/bin/main_BuildLog.txt) · [source 7](https://github.com/1888games/SnoutAbout_C64/commit/c628291d2ac627d6bd5b55ef52f12d909a1c0131)

**Classification (reviewed):** Native C64 authored game source, with direct game logic and VIC-II/SID/CIA interaction rather than a game-specific CPU emulator. Original 6502 game for a C64 4 KiB competition; no historical-binary recovery claim. The competition description is not an independently measured packed-size result. Target is C64, while source_platforms/source_cpu/source_language remain empty because no original binary was recovered or analysed. Original homebrew is not assigned a binary-recovery work kind.

Evidence: [source 1](https://github.com/1888games/SnoutAbout_C64/blob/c628291d2ac627d6bd5b55ef52f12d909a1c0131/SnoutAbout/scripts/main.asm) · [source 2](https://github.com/1888games/SnoutAbout_C64/blob/c628291d2ac627d6bd5b55ef52f12d909a1c0131/SnoutAbout/scripts/interrupts/snout.asm) · [source 3](https://github.com/1888games/SnoutAbout_C64/blob/c628291d2ac627d6bd5b55ef52f12d909a1c0131/SnoutAbout/scripts/interrupts/irq.asm) · [source 4](https://github.com/1888games/SnoutAbout_C64/blob/c628291d2ac627d6bd5b55ef52f12d909a1c0131/SnoutAbout/scripts/setup/assets.asm) · [source 5](https://github.com/1888games/SnoutAbout_C64/blob/c628291d2ac627d6bd5b55ef52f12d909a1c0131/README.md) · [source 6](https://github.com/1888games/SnoutAbout_C64/blob/c628291d2ac627d6bd5b55ef52f12d909a1c0131/SnoutAbout/scripts/bin/main_BuildLog.txt)

**Source architecture (not-applicable):** This is authored or adapted game source, not a disassembled/recovered original executable. Game inspiration does not establish the original binary ISA; source_cpu stays empty/not-applicable.

Evidence: [source 1](https://github.com/1888games/SnoutAbout_C64/blob/c628291d2ac627d6bd5b55ef52f12d909a1c0131/SnoutAbout/scripts/main.asm) · [source 2](https://github.com/1888games/SnoutAbout_C64/blob/c628291d2ac627d6bd5b55ef52f12d909a1c0131/SnoutAbout/scripts/interrupts/snout.asm) · [source 3](https://github.com/1888games/SnoutAbout_C64/blob/c628291d2ac627d6bd5b55ef52f12d909a1c0131/SnoutAbout/scripts/interrupts/irq.asm) · [source 4](https://github.com/1888games/SnoutAbout_C64/blob/c628291d2ac627d6bd5b55ef52f12d909a1c0131/SnoutAbout/scripts/setup/assets.asm) · [source 5](https://github.com/1888games/SnoutAbout_C64/blob/c628291d2ac627d6bd5b55ef52f12d909a1c0131/README.md) · [source 6](https://github.com/1888games/SnoutAbout_C64/blob/c628291d2ac627d6bd5b55ef52f12d909a1c0131/SnoutAbout/scripts/bin/main_BuildLog.txt)

**Target architecture (reviewed):** Reviewed assembly contains 6502-family LDA/STA/JSR and native hardware-access code, with a C64 assembler/entrypoint. target_cpu=6502 records the observed instruction set; it does not assert an exact 6510 silicon subtype, numerical CPU/RAM minimum, or successfully assembled output.

Evidence: [source 1](https://github.com/1888games/SnoutAbout_C64/blob/c628291d2ac627d6bd5b55ef52f12d909a1c0131/SnoutAbout/scripts/main.asm) · [source 2](https://github.com/1888games/SnoutAbout_C64/blob/c628291d2ac627d6bd5b55ef52f12d909a1c0131/SnoutAbout/scripts/bin/main_BuildLog.txt) · [source 3](https://github.com/1888games/SnoutAbout_C64/blob/c628291d2ac627d6bd5b55ef52f12d909a1c0131/SnoutAbout/scripts/interrupts/snout.asm) · [source 4](https://github.com/1888games/SnoutAbout_C64/blob/c628291d2ac627d6bd5b55ef52f12d909a1c0131/SnoutAbout/scripts/interrupts/irq.asm) · [source 5](https://github.com/1888games/SnoutAbout_C64/blob/c628291d2ac627d6bd5b55ef52f12d909a1c0131/SnoutAbout/scripts/setup/assets.asm) · [source 6](https://github.com/1888games/SnoutAbout_C64/blob/c628291d2ac627d6bd5b55ef52f12d909a1c0131/README.md)

**Build and verification (needs-research):** Selected main assembly and included assets define the native KickAssembler program; checked-in PRGs, symbols and historical build logs are upstream artifacts, not a current successful build. No portable automated build recipe was established. No independent assembly, runtime, original-ROM equivalence or hardware test was performed. Checked-in PRGs and historical build logs are upstream artifacts only. No explicit license was found in the inspected standalone README/source material or license-named tree entries. Public source visibility does not establish redistribution rights, including rights in game graphics, names and music. The 4 KiB description is an upstream competition claim. The assembled memory map spans noncontiguous addresses, and no packed-output size was independently verified. No candidate compilation, execution, emulator/gameplay test, hardware test, round-trip or byte comparison was run. compilable/runnable/playable/byte_exact all remain null.

Evidence: [source 1](https://github.com/1888games/SnoutAbout_C64/blob/c628291d2ac627d6bd5b55ef52f12d909a1c0131/SnoutAbout/scripts/main.asm) · [source 2](https://github.com/1888games/SnoutAbout_C64/blob/c628291d2ac627d6bd5b55ef52f12d909a1c0131/SnoutAbout/scripts/bin/main_BuildLog.txt) · [source 3](https://github.com/1888games/SnoutAbout_C64/blob/c628291d2ac627d6bd5b55ef52f12d909a1c0131/SnoutAbout/scripts/interrupts/snout.asm) · [source 4](https://github.com/1888games/SnoutAbout_C64/blob/c628291d2ac627d6bd5b55ef52f12d909a1c0131/SnoutAbout/scripts/interrupts/irq.asm) · [source 5](https://github.com/1888games/SnoutAbout_C64/blob/c628291d2ac627d6bd5b55ef52f12d909a1c0131/SnoutAbout/scripts/setup/assets.asm) · [source 6](https://github.com/1888games/SnoutAbout_C64/blob/c628291d2ac627d6bd5b55ef52f12d909a1c0131/README.md)

**Runtime requirements (no-evidence-found):** No sufficiently specific supported minimum hardware configuration was established for a runtime profile. Target C64 and observed native ISA are not evidence of a tested CPU/RAM minimum. Video/timing evidence: MOS 6510 C64 game with VIC-II raster IRQ and direct SID noise-register initialization. PAL/NTSC compatibility is not established. Relevant limits: The 4 KiB description is an upstream competition claim. The assembled memory map spans noncontiguous addresses, and no packed-output size was independently verified.

Evidence: [source 1](https://github.com/1888games/SnoutAbout_C64/blob/c628291d2ac627d6bd5b55ef52f12d909a1c0131/SnoutAbout/scripts/main.asm) · [source 2](https://github.com/1888games/SnoutAbout_C64/blob/c628291d2ac627d6bd5b55ef52f12d909a1c0131/SnoutAbout/scripts/interrupts/snout.asm) · [source 3](https://github.com/1888games/SnoutAbout_C64/blob/c628291d2ac627d6bd5b55ef52f12d909a1c0131/SnoutAbout/scripts/interrupts/irq.asm) · [source 4](https://github.com/1888games/SnoutAbout_C64/blob/c628291d2ac627d6bd5b55ef52f12d909a1c0131/SnoutAbout/scripts/setup/assets.asm) · [source 5](https://github.com/1888games/SnoutAbout_C64/blob/c628291d2ac627d6bd5b55ef52f12d909a1c0131/README.md) · [source 6](https://github.com/1888games/SnoutAbout_C64/blob/c628291d2ac627d6bd5b55ef52f12d909a1c0131/SnoutAbout/scripts/bin/main_BuildLog.txt)

**AI attribution (no-evidence-found):** No explicit generative-AI attribution found in the selected README, implementation, build or license material and the first eight default-branch commit messages/author metadata (or all returned if fewer). One selected commit detail was read where recorded. This bounded review is not proof of non-use. Opponent gameplay AI is not generative-AI tooling evidence. Unknown is not evidence of non-use; named tools are not inferred from provider addresses, ordinary automation or gameplay AI.

Evidence: [source 1](https://api.github.com/repos/1888games/SnoutAbout_C64/commits?per_page=8&page=1) · [source 2](https://github.com/1888games/SnoutAbout_C64/commit/c628291d2ac627d6bd5b55ef52f12d909a1c0131) · [source 3](https://github.com/1888games/SnoutAbout_C64/blob/c628291d2ac627d6bd5b55ef52f12d909a1c0131/SnoutAbout/scripts/main.asm) · [source 4](https://github.com/1888games/SnoutAbout_C64/blob/c628291d2ac627d6bd5b55ef52f12d909a1c0131/SnoutAbout/scripts/interrupts/snout.asm) · [source 5](https://github.com/1888games/SnoutAbout_C64/blob/c628291d2ac627d6bd5b55ef52f12d909a1c0131/SnoutAbout/scripts/interrupts/irq.asm) · [source 6](https://github.com/1888games/SnoutAbout_C64/blob/c628291d2ac627d6bd5b55ef52f12d909a1c0131/SnoutAbout/scripts/setup/assets.asm) · [source 7](https://github.com/1888games/SnoutAbout_C64/blob/c628291d2ac627d6bd5b55ef52f12d909a1c0131/README.md) · [source 8](https://github.com/1888games/SnoutAbout_C64/blob/c628291d2ac627d6bd5b55ef52f12d909a1c0131/SnoutAbout/scripts/bin/main_BuildLog.txt)

**Lineage and rights (reviewed):** overlapping collection; not a second project 1888games/ArlasoftC64 The overlapping Arlasoft Complete folder is supporting provenance, not another project. Blob comparison found 37 matching standalone blobs; main-source match paths: Complete/SnoutAbout/scripts/main.asm. Licensing: No standalone license grant established; metadata license is null and no license-named file occurs in the complete tree. Canonical root was absent from the verified 1,621-project d654a0c publication baseline and 1,861-root normalized reviewed index. Wider lineage/source coverage is still partial.

Evidence: [source 1](https://github.com/1888games/SnoutAbout_C64/blob/c628291d2ac627d6bd5b55ef52f12d909a1c0131/SnoutAbout/scripts/main.asm) · [source 2](https://github.com/1888games/SnoutAbout_C64/blob/c628291d2ac627d6bd5b55ef52f12d909a1c0131/SnoutAbout/scripts/interrupts/snout.asm) · [source 3](https://github.com/1888games/SnoutAbout_C64/blob/c628291d2ac627d6bd5b55ef52f12d909a1c0131/SnoutAbout/scripts/interrupts/irq.asm) · [source 4](https://github.com/1888games/SnoutAbout_C64/blob/c628291d2ac627d6bd5b55ef52f12d909a1c0131/SnoutAbout/scripts/setup/assets.asm) · [source 5](https://github.com/1888games/SnoutAbout_C64/blob/c628291d2ac627d6bd5b55ef52f12d909a1c0131/README.md) · [source 6](https://github.com/1888games/SnoutAbout_C64/blob/c628291d2ac627d6bd5b55ef52f12d909a1c0131/SnoutAbout/scripts/bin/main_BuildLog.txt) · [source 7](https://github.com/1888games/ArlasoftC64/blob/7f70676ee2166e493e9669370f226813ea1cd5cb/README.md)

### OYUP!: native C64 Puyo-inspired game source

[Repository](https://github.com/1888games/OyupOyup)

- Source platforms: Unasserted / not applicable
- Target platforms: C64
- Source CPU: Unasserted / not applicable
- Target CPU: 6502
- Source material/language: Unasserted / not applicable
- Maintained language: 6502 assembly (KickAssembler)
- Classification: subject; game, reimplementation
- Build flags: all unknown (compilable, runnable, playable and byte_exact).
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** README documents development from 4 November to 7 December 2020 for a retro-game competition and names Puyo Puyo 2 as inspiration. grid.asm implements two 12-by-6 playfields and matching/queue state; opponents.asm implements a 22-placement heuristic search, scoring and opponent skill settings. This is gameplay AI, not evidence of generative-AI development. main.asm detects PAL/NTSC, adjusts the gameplay frames-per-second/speed settings for NTSC, and irq.asm normalizes SID scheduling; the history includes high-score fixes and color-blind/music options. Inspected snapshot: branch Release, head commit e11ff04e39f8efa6ea50c8e1672709084733e6b2, git tree ba9eb6ad9672454de22204d9a60fb01f75f1b689. Head and tree are separate identities; the connector tree response top-level sha was not used as the actual tree identity. Inspection is a bounded sample, not all code/features.

Evidence: [source 1](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/README.md) · [source 2](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/main.asm) · [source 3](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/scripts/game/grid.asm) · [source 4](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/scripts/game/opponents.asm) · [source 5](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/scripts/game/irq.asm) · [source 6](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/scripts/game/assets.asm) · [source 7](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/bin/main_BuildLog.txt) · [source 8](https://github.com/1888games/OyupOyup/commit/e11ff04e39f8efa6ea50c8e1672709084733e6b2)

**Classification (reviewed):** Native C64 authored game source, with direct game logic and VIC-II/SID/CIA interaction rather than a game-specific CPU emulator. README names Mega Drive Puyo Puyo 2 as inspiration. No Mega Drive executable, 68000 instructions or original-binary disassembly was inspected. The opponent search is ordinary gameplay AI, not generative-AI development evidence. Target is C64, while source_platforms/source_cpu/source_language remain empty because no original binary was recovered or analysed. work_kinds=reimplementation describes the evidenced game adaptation, not binary-derived reverse engineering.

Evidence: [source 1](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/README.md) · [source 2](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/main.asm) · [source 3](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/scripts/game/grid.asm) · [source 4](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/scripts/game/opponents.asm) · [source 5](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/scripts/game/irq.asm) · [source 6](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/scripts/game/assets.asm) · [source 7](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/bin/main_BuildLog.txt)

**Source architecture (not-applicable):** This is authored or adapted game source, not a disassembled/recovered original executable. Game inspiration does not establish the original binary ISA; source_cpu stays empty/not-applicable.

Evidence: [source 1](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/README.md) · [source 2](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/main.asm) · [source 3](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/scripts/game/grid.asm) · [source 4](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/scripts/game/opponents.asm) · [source 5](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/scripts/game/irq.asm) · [source 6](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/scripts/game/assets.asm) · [source 7](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/bin/main_BuildLog.txt)

**Target architecture (reviewed):** Reviewed assembly contains 6502-family LDA/STA/JSR and native hardware-access code, with a C64 assembler/entrypoint. target_cpu=6502 records the observed instruction set; it does not assert an exact 6510 silicon subtype, numerical CPU/RAM minimum, or successfully assembled output.

Evidence: [source 1](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/main.asm) · [source 2](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/bin/main_BuildLog.txt) · [source 3](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/README.md) · [source 4](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/scripts/game/grid.asm) · [source 5](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/scripts/game/opponents.asm) · [source 6](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/scripts/game/irq.asm) · [source 7](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/scripts/game/assets.asm)

**Build and verification (needs-research):** Selected main assembly and included assets define the native KickAssembler program; checked-in PRGs, symbols and historical build logs are upstream artifacts, not a current successful build. No portable automated build recipe was established. No independent assembly, runtime, original-ROM equivalence or hardware test was performed. Checked-in PRGs and historical build logs are upstream artifacts only. No explicit license was found in the inspected standalone README/source material or license-named tree entries. Public source visibility does not establish redistribution rights, including rights in game graphics, names and music. Rooted /scripts imports, binary assets and exact KickAssembler working-directory semantics need a clean build check. The related Complete/Oyup! collection folder includes more files but is the same game family, not an additional project. No candidate compilation, execution, emulator/gameplay test, hardware test, round-trip or byte comparison was run. compilable/runnable/playable/byte_exact all remain null.

Evidence: [source 1](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/main.asm) · [source 2](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/bin/main_BuildLog.txt) · [source 3](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/README.md) · [source 4](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/scripts/game/grid.asm) · [source 5](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/scripts/game/opponents.asm) · [source 6](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/scripts/game/irq.asm) · [source 7](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/scripts/game/assets.asm)

**Runtime requirements (no-evidence-found):** No sufficiently specific supported minimum hardware configuration was established for a runtime profile. Target C64 and observed native ISA are not evidence of a tested CPU/RAM minimum. Video/timing evidence: Native C64 MOS 6510 program with VIC-II/SID/CIA. Explicit PAL/NTSC speed and SID scheduling code is present but not executed. Relevant limits:

Evidence: [source 1](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/README.md) · [source 2](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/main.asm) · [source 3](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/scripts/game/grid.asm) · [source 4](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/scripts/game/opponents.asm) · [source 5](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/scripts/game/irq.asm) · [source 6](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/scripts/game/assets.asm) · [source 7](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/bin/main_BuildLog.txt)

**AI attribution (no-evidence-found):** No explicit generative-AI attribution found in the selected README, implementation, build or license material and the first eight default-branch commit messages/author metadata (or all returned if fewer). One selected commit detail was read where recorded. This bounded review is not proof of non-use. Opponent gameplay AI is not generative-AI tooling evidence. Unknown is not evidence of non-use; named tools are not inferred from provider addresses, ordinary automation or gameplay AI.

Evidence: [source 1](https://api.github.com/repos/1888games/OyupOyup/commits?per_page=8&page=1) · [source 2](https://github.com/1888games/OyupOyup/commit/e11ff04e39f8efa6ea50c8e1672709084733e6b2) · [source 3](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/README.md) · [source 4](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/main.asm) · [source 5](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/scripts/game/grid.asm) · [source 6](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/scripts/game/opponents.asm) · [source 7](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/scripts/game/irq.asm) · [source 8](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/scripts/game/assets.asm) · [source 9](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/bin/main_BuildLog.txt)

**Lineage and rights (reviewed):** overlapping collection; not a second project 1888games/ArlasoftC64 The overlapping Arlasoft Complete folder is supporting provenance, not another project. Blob comparison found 71 matching standalone blobs; main-source match paths: Complete/Oyup!/main.asm. Licensing: No standalone license grant established; metadata license is null and no license-named file occurs in the complete tree. Canonical root was absent from the verified 1,621-project d654a0c publication baseline and 1,861-root normalized reviewed index. Wider lineage/source coverage is still partial.

Evidence: [source 1](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/README.md) · [source 2](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/main.asm) · [source 3](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/scripts/game/grid.asm) · [source 4](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/scripts/game/opponents.asm) · [source 5](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/scripts/game/irq.asm) · [source 6](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/scripts/game/assets.asm) · [source 7](https://github.com/1888games/OyupOyup/blob/e11ff04e39f8efa6ea50c8e1672709084733e6b2/bin/main_BuildLog.txt) · [source 8](https://github.com/1888games/ArlasoftC64/blob/7f70676ee2166e493e9669370f226813ea1cd5cb/README.md)

### Mario’s Cement Factory: native C64 game source

[Repository](https://github.com/hayesmaker/marios-cement-factory-64)

- Source platforms: Unasserted / not applicable
- Target platforms: C64
- Source CPU: Unasserted / not applicable
- Target CPU: 6502
- Source material/language: Unasserted / not applicable
- Maintained language: 6502 assembly (KickAssembler)
- Classification: subject; game, reimplementation
- Build flags: all unknown (compilable, runnable, playable and byte_exact).
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Repository description explicitly states the C64 6502 assembly implementation. start.asm contains a native BASIC stub, Koala title-image loading, binary SID/music input and game-state module imports. player.asm implements player grid positions, elevator/landing behavior, movement and crushed/fallen sprites; mixers.asm implements hoppers, pouring counters, alarms and cement spills. The saved Sublime workspace names the Kick Assembler C64 build system. Source includes explicit C64 IRQ/SID handling; the latest inspected change fixes lives-counter reset. Inspected snapshot: branch master, head commit 70e2688b3121326f91269b69598ceb35271bffed, git tree 73e7e7ee9357f186f8e62a0c9ccf97b35f11554d. Head and tree are separate identities; the connector tree response top-level sha was not used as the actual tree identity. Inspection is a bounded sample, not all code/features.

Evidence: [source 1](https://github.com/hayesmaker/marios-cement-factory-64/blob/70e2688b3121326f91269b69598ceb35271bffed/start.asm) · [source 2](https://github.com/hayesmaker/marios-cement-factory-64/blob/70e2688b3121326f91269b69598ceb35271bffed/actors/player.asm) · [source 3](https://github.com/hayesmaker/marios-cement-factory-64/blob/70e2688b3121326f91269b69598ceb35271bffed/actors/mixers.asm) · [source 4](https://github.com/hayesmaker/marios-cement-factory-64/blob/70e2688b3121326f91269b69598ceb35271bffed/lib/irq.asm) · [source 5](https://github.com/hayesmaker/marios-cement-factory-64/blob/70e2688b3121326f91269b69598ceb35271bffed/tests/specs.asm) · [source 6](https://github.com/hayesmaker/marios-cement-factory-64/blob/70e2688b3121326f91269b69598ceb35271bffed/.propject.sublime-workspace) · [source 7](https://github.com/hayesmaker/marios-cement-factory-64/commit/70e2688b3121326f91269b69598ceb35271bffed)

**Classification (reviewed):** Native C64 authored game source, with direct game logic and VIC-II/SID/CIA interaction rather than a game-specific CPU emulator. Native game-specific C64 implementation of the handheld game. No Nintendo CPU interpreter or original handheld machine-code recovery was found in the reviewed modules. Target is C64, while source_platforms/source_cpu/source_language remain empty because no original binary was recovered or analysed. work_kinds=reimplementation describes the evidenced game adaptation, not binary-derived reverse engineering.

Evidence: [source 1](https://github.com/hayesmaker/marios-cement-factory-64/blob/70e2688b3121326f91269b69598ceb35271bffed/start.asm) · [source 2](https://github.com/hayesmaker/marios-cement-factory-64/blob/70e2688b3121326f91269b69598ceb35271bffed/actors/player.asm) · [source 3](https://github.com/hayesmaker/marios-cement-factory-64/blob/70e2688b3121326f91269b69598ceb35271bffed/actors/mixers.asm) · [source 4](https://github.com/hayesmaker/marios-cement-factory-64/blob/70e2688b3121326f91269b69598ceb35271bffed/lib/irq.asm) · [source 5](https://github.com/hayesmaker/marios-cement-factory-64/blob/70e2688b3121326f91269b69598ceb35271bffed/tests/specs.asm) · [source 6](https://github.com/hayesmaker/marios-cement-factory-64/blob/70e2688b3121326f91269b69598ceb35271bffed/.propject.sublime-workspace)

**Source architecture (not-applicable):** This is authored or adapted game source, not a disassembled/recovered original executable. Game inspiration does not establish the original binary ISA; source_cpu stays empty/not-applicable.

Evidence: [source 1](https://github.com/hayesmaker/marios-cement-factory-64/blob/70e2688b3121326f91269b69598ceb35271bffed/start.asm) · [source 2](https://github.com/hayesmaker/marios-cement-factory-64/blob/70e2688b3121326f91269b69598ceb35271bffed/actors/player.asm) · [source 3](https://github.com/hayesmaker/marios-cement-factory-64/blob/70e2688b3121326f91269b69598ceb35271bffed/actors/mixers.asm) · [source 4](https://github.com/hayesmaker/marios-cement-factory-64/blob/70e2688b3121326f91269b69598ceb35271bffed/lib/irq.asm) · [source 5](https://github.com/hayesmaker/marios-cement-factory-64/blob/70e2688b3121326f91269b69598ceb35271bffed/tests/specs.asm) · [source 6](https://github.com/hayesmaker/marios-cement-factory-64/blob/70e2688b3121326f91269b69598ceb35271bffed/.propject.sublime-workspace)

**Target architecture (reviewed):** Reviewed assembly contains 6502-family LDA/STA/JSR and native hardware-access code, with a C64 assembler/entrypoint. target_cpu=6502 records the observed instruction set; it does not assert an exact 6510 silicon subtype, numerical CPU/RAM minimum, or successfully assembled output.

Evidence: [source 1](https://github.com/hayesmaker/marios-cement-factory-64/blob/70e2688b3121326f91269b69598ceb35271bffed/start.asm) · [source 2](https://github.com/hayesmaker/marios-cement-factory-64/blob/70e2688b3121326f91269b69598ceb35271bffed/.propject.sublime-workspace) · [source 3](https://github.com/hayesmaker/marios-cement-factory-64/blob/70e2688b3121326f91269b69598ceb35271bffed/actors/player.asm) · [source 4](https://github.com/hayesmaker/marios-cement-factory-64/blob/70e2688b3121326f91269b69598ceb35271bffed/actors/mixers.asm) · [source 5](https://github.com/hayesmaker/marios-cement-factory-64/blob/70e2688b3121326f91269b69598ceb35271bffed/lib/irq.asm) · [source 6](https://github.com/hayesmaker/marios-cement-factory-64/blob/70e2688b3121326f91269b69598ceb35271bffed/tests/specs.asm)

**Build and verification (needs-research):** start.asm and the saved Sublime Kick Assembler C64 build-system selection establish intended assembly inputs. No README, portable build script or current toolchain version was established; tests/specs.asm is a trivial example, not meaningful game test evidence. No independent assembly, runtime, original-ROM equivalence or hardware test was performed. Checked-in PRGs and historical build logs are upstream artifacts only. No explicit license was found in the inspected standalone README/source material or license-named tree entries. Public source visibility does not establish redistribution rights, including rights in game graphics, names and music. No README, license file or portable build script was found in the complete tree. The Sublime workspace is historical environment evidence, not a reproducible build recipe. tests/specs.asm is a tiny 64spec sample assertion, not evidence of meaningful game regression coverage. Nintendo-branded graphics and sound inputs require separate rights review. PAL/NTSC timing behavior is not established. No candidate compilation, execution, emulator/gameplay test, hardware test, round-trip or byte comparison was run. compilable/runnable/playable/byte_exact all remain null.

Evidence: [source 1](https://github.com/hayesmaker/marios-cement-factory-64/blob/70e2688b3121326f91269b69598ceb35271bffed/start.asm) · [source 2](https://github.com/hayesmaker/marios-cement-factory-64/blob/70e2688b3121326f91269b69598ceb35271bffed/.propject.sublime-workspace) · [source 3](https://github.com/hayesmaker/marios-cement-factory-64/blob/70e2688b3121326f91269b69598ceb35271bffed/actors/player.asm) · [source 4](https://github.com/hayesmaker/marios-cement-factory-64/blob/70e2688b3121326f91269b69598ceb35271bffed/actors/mixers.asm) · [source 5](https://github.com/hayesmaker/marios-cement-factory-64/blob/70e2688b3121326f91269b69598ceb35271bffed/lib/irq.asm) · [source 6](https://github.com/hayesmaker/marios-cement-factory-64/blob/70e2688b3121326f91269b69598ceb35271bffed/tests/specs.asm)

**Runtime requirements (no-evidence-found):** No sufficiently specific supported minimum hardware configuration was established for a runtime profile. Target C64 and observed native ISA are not evidence of a tested CPU/RAM minimum. Video/timing evidence: Native MOS 6510 C64 assembly with direct VIC-II/CIA/SID access; fixed raster handlers inspected. No original handheld CPU emulation is used in the reviewed game modules. Relevant limits: Nintendo-branded graphics and sound inputs require separate rights review. PAL/NTSC timing behavior is not established.

Evidence: [source 1](https://github.com/hayesmaker/marios-cement-factory-64/blob/70e2688b3121326f91269b69598ceb35271bffed/start.asm) · [source 2](https://github.com/hayesmaker/marios-cement-factory-64/blob/70e2688b3121326f91269b69598ceb35271bffed/actors/player.asm) · [source 3](https://github.com/hayesmaker/marios-cement-factory-64/blob/70e2688b3121326f91269b69598ceb35271bffed/actors/mixers.asm) · [source 4](https://github.com/hayesmaker/marios-cement-factory-64/blob/70e2688b3121326f91269b69598ceb35271bffed/lib/irq.asm) · [source 5](https://github.com/hayesmaker/marios-cement-factory-64/blob/70e2688b3121326f91269b69598ceb35271bffed/tests/specs.asm) · [source 6](https://github.com/hayesmaker/marios-cement-factory-64/blob/70e2688b3121326f91269b69598ceb35271bffed/.propject.sublime-workspace)

**AI attribution (no-evidence-found):** No explicit generative-AI attribution found in the selected README, implementation, build or license material and the first eight default-branch commit messages/author metadata (or all returned if fewer). One selected commit detail was read where recorded. This bounded review is not proof of non-use. Opponent gameplay AI is not generative-AI tooling evidence. Unknown is not evidence of non-use; named tools are not inferred from provider addresses, ordinary automation or gameplay AI.

Evidence: [source 1](https://api.github.com/repos/hayesmaker/marios-cement-factory-64/commits?per_page=8&page=1) · [source 2](https://github.com/hayesmaker/marios-cement-factory-64/commit/70e2688b3121326f91269b69598ceb35271bffed) · [source 3](https://github.com/hayesmaker/marios-cement-factory-64/blob/70e2688b3121326f91269b69598ceb35271bffed/start.asm) · [source 4](https://github.com/hayesmaker/marios-cement-factory-64/blob/70e2688b3121326f91269b69598ceb35271bffed/actors/player.asm) · [source 5](https://github.com/hayesmaker/marios-cement-factory-64/blob/70e2688b3121326f91269b69598ceb35271bffed/actors/mixers.asm) · [source 6](https://github.com/hayesmaker/marios-cement-factory-64/blob/70e2688b3121326f91269b69598ceb35271bffed/lib/irq.asm) · [source 7](https://github.com/hayesmaker/marios-cement-factory-64/blob/70e2688b3121326f91269b69598ceb35271bffed/tests/specs.asm) · [source 8](https://github.com/hayesmaker/marios-cement-factory-64/blob/70e2688b3121326f91269b69598ceb35271bffed/.propject.sublime-workspace)

**Lineage and rights (reviewed):**  Licensing: No standalone license grant established; metadata license is null and no license-named file occurs in the complete tree. Canonical root was absent from the verified 1,621-project d654a0c publication baseline and 1,861-root normalized reviewed index. Wider lineage/source coverage is still partial.

Evidence: [source 1](https://github.com/hayesmaker/marios-cement-factory-64/blob/70e2688b3121326f91269b69598ceb35271bffed/start.asm) · [source 2](https://github.com/hayesmaker/marios-cement-factory-64/blob/70e2688b3121326f91269b69598ceb35271bffed/actors/player.asm) · [source 3](https://github.com/hayesmaker/marios-cement-factory-64/blob/70e2688b3121326f91269b69598ceb35271bffed/actors/mixers.asm) · [source 4](https://github.com/hayesmaker/marios-cement-factory-64/blob/70e2688b3121326f91269b69598ceb35271bffed/lib/irq.asm) · [source 5](https://github.com/hayesmaker/marios-cement-factory-64/blob/70e2688b3121326f91269b69598ceb35271bffed/tests/specs.asm) · [source 6](https://github.com/hayesmaker/marios-cement-factory-64/blob/70e2688b3121326f91269b69598ceb35271bffed/.propject.sublime-workspace)

### Neptune Lander: unfinished native C64 tutorial game

[Repository](https://github.com/OldSkoolCoder/NeptuneLander)

- Source platforms: Unasserted / not applicable
- Target platforms: C64
- Source CPU: Unasserted / not applicable
- Target CPU: 6502
- Source material/language: Unasserted / not applicable
- Maintained language: 6502 assembly (CBM prg Studio), Commodore BASIC
- Classification: subject; game
- Build flags: all unknown (compilable, runnable, playable and byte_exact).
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** README documents an in-progress tutorial game; the latest sampled source-changing commit reaches episode 38, beyond the README’s completed-episode list. NeptuneLander_V2.asm supplies a BASIC SYS bootstrap, asset imports and native main loop. gameLander.asm implements fixed-point velocities, sprites and collision; gameFlow.asm includes menu, flight, landing, death, levels, difficulty and input-device states. NeptuneLander.cbmprj explicitly selects C64, PRG output, John Dale as author and CBM prg Studio 3.14.0-era project format; BASIC source versions are retained alongside assembly. Inspected snapshot: branch master, head commit 5314bbb5e21268c4d6af51b2ecd42348f7a4b458, git tree 2c6c623ec5c7b5bbdd3eaa0a9733831cc78d9e2a. Head and tree are separate identities; the connector tree response top-level sha was not used as the actual tree identity. Inspection is a bounded sample, not all code/features.

Evidence: [source 1](https://github.com/OldSkoolCoder/NeptuneLander/blob/5314bbb5e21268c4d6af51b2ecd42348f7a4b458/NeptuneLander_V2.asm) · [source 2](https://github.com/OldSkoolCoder/NeptuneLander/blob/5314bbb5e21268c4d6af51b2ecd42348f7a4b458/gameLander.asm) · [source 3](https://github.com/OldSkoolCoder/NeptuneLander/blob/5314bbb5e21268c4d6af51b2ecd42348f7a4b458/gameFlow.asm) · [source 4](https://github.com/OldSkoolCoder/NeptuneLander/blob/5314bbb5e21268c4d6af51b2ecd42348f7a4b458/NeptuneLander.bas) · [source 5](https://github.com/OldSkoolCoder/NeptuneLander/blob/5314bbb5e21268c4d6af51b2ecd42348f7a4b458/README.md) · [source 6](https://github.com/OldSkoolCoder/NeptuneLander/blob/5314bbb5e21268c4d6af51b2ecd42348f7a4b458/NeptuneLander.cbmprj) · [source 7](https://github.com/OldSkoolCoder/NeptuneLander/commit/5314bbb5e21268c4d6af51b2ecd42348f7a4b458)

**Classification (reviewed):** Native C64 authored game source, with direct game logic and VIC-II/SID/CIA interaction rather than a game-specific CPU emulator. Authored BASIC prototypes and native C64 assembly developed through a workshop/tutorial series. Substantive code exists, but upstream explicitly describes ongoing development; this is not a verified finished or working release. Target is C64, while source_platforms/source_cpu/source_language remain empty because no original binary was recovered or analysed. Original homebrew is not assigned a binary-recovery work kind.

Evidence: [source 1](https://github.com/OldSkoolCoder/NeptuneLander/blob/5314bbb5e21268c4d6af51b2ecd42348f7a4b458/NeptuneLander_V2.asm) · [source 2](https://github.com/OldSkoolCoder/NeptuneLander/blob/5314bbb5e21268c4d6af51b2ecd42348f7a4b458/gameLander.asm) · [source 3](https://github.com/OldSkoolCoder/NeptuneLander/blob/5314bbb5e21268c4d6af51b2ecd42348f7a4b458/gameFlow.asm) · [source 4](https://github.com/OldSkoolCoder/NeptuneLander/blob/5314bbb5e21268c4d6af51b2ecd42348f7a4b458/NeptuneLander.bas) · [source 5](https://github.com/OldSkoolCoder/NeptuneLander/blob/5314bbb5e21268c4d6af51b2ecd42348f7a4b458/README.md) · [source 6](https://github.com/OldSkoolCoder/NeptuneLander/blob/5314bbb5e21268c4d6af51b2ecd42348f7a4b458/NeptuneLander.cbmprj)

**Source architecture (not-applicable):** This is authored or adapted game source, not a disassembled/recovered original executable. Game inspiration does not establish the original binary ISA; source_cpu stays empty/not-applicable.

Evidence: [source 1](https://github.com/OldSkoolCoder/NeptuneLander/blob/5314bbb5e21268c4d6af51b2ecd42348f7a4b458/NeptuneLander_V2.asm) · [source 2](https://github.com/OldSkoolCoder/NeptuneLander/blob/5314bbb5e21268c4d6af51b2ecd42348f7a4b458/gameLander.asm) · [source 3](https://github.com/OldSkoolCoder/NeptuneLander/blob/5314bbb5e21268c4d6af51b2ecd42348f7a4b458/gameFlow.asm) · [source 4](https://github.com/OldSkoolCoder/NeptuneLander/blob/5314bbb5e21268c4d6af51b2ecd42348f7a4b458/NeptuneLander.bas) · [source 5](https://github.com/OldSkoolCoder/NeptuneLander/blob/5314bbb5e21268c4d6af51b2ecd42348f7a4b458/README.md) · [source 6](https://github.com/OldSkoolCoder/NeptuneLander/blob/5314bbb5e21268c4d6af51b2ecd42348f7a4b458/NeptuneLander.cbmprj)

**Target architecture (reviewed):** Reviewed assembly contains 6502-family LDA/STA/JSR and native hardware-access code, with a C64 assembler/entrypoint. target_cpu=6502 records the observed instruction set; it does not assert an exact 6510 silicon subtype, numerical CPU/RAM minimum, or successfully assembled output.

Evidence: [source 1](https://github.com/OldSkoolCoder/NeptuneLander/blob/5314bbb5e21268c4d6af51b2ecd42348f7a4b458/NeptuneLander.cbmprj) · [source 2](https://github.com/OldSkoolCoder/NeptuneLander/blob/5314bbb5e21268c4d6af51b2ecd42348f7a4b458/NeptuneLander_V2.asm) · [source 3](https://github.com/OldSkoolCoder/NeptuneLander/blob/5314bbb5e21268c4d6af51b2ecd42348f7a4b458/gameLander.asm) · [source 4](https://github.com/OldSkoolCoder/NeptuneLander/blob/5314bbb5e21268c4d6af51b2ecd42348f7a4b458/gameFlow.asm) · [source 5](https://github.com/OldSkoolCoder/NeptuneLander/blob/5314bbb5e21268c4d6af51b2ecd42348f7a4b458/NeptuneLander.bas) · [source 6](https://github.com/OldSkoolCoder/NeptuneLander/blob/5314bbb5e21268c4d6af51b2ecd42348f7a4b458/README.md)

**Build and verification (needs-research):** The CBM prg Studio 3.14.0-era .cbmprj selects C64 PRG output and assembly/assets. Source conversion from BASIC is substantive, but the tutorial project remains explicitly unfinished. No independent assembly, runtime, original-ROM equivalence or hardware test was performed. Checked-in PRGs and historical build logs are upstream artifacts only. No explicit license was found in the inspected standalone README/source material or license-named tree entries. Public source visibility does not establish redistribution rights, including rights in game graphics, names and music. The README still calls development ongoing; do not report a completed/public release or independently playable state. CBM prg Studio project and proprietary sprite/charset/screen data formats are part of the build inputs. Bundled SID tracks do not have an established blanket license. NeptuneLander-1 is a related tutorial-following variant and is not counted separately. No candidate compilation, execution, emulator/gameplay test, hardware test, round-trip or byte comparison was run. compilable/runnable/playable/byte_exact all remain null.

Evidence: [source 1](https://github.com/OldSkoolCoder/NeptuneLander/blob/5314bbb5e21268c4d6af51b2ecd42348f7a4b458/NeptuneLander.cbmprj) · [source 2](https://github.com/OldSkoolCoder/NeptuneLander/blob/5314bbb5e21268c4d6af51b2ecd42348f7a4b458/NeptuneLander_V2.asm) · [source 3](https://github.com/OldSkoolCoder/NeptuneLander/blob/5314bbb5e21268c4d6af51b2ecd42348f7a4b458/gameLander.asm) · [source 4](https://github.com/OldSkoolCoder/NeptuneLander/blob/5314bbb5e21268c4d6af51b2ecd42348f7a4b458/gameFlow.asm) · [source 5](https://github.com/OldSkoolCoder/NeptuneLander/blob/5314bbb5e21268c4d6af51b2ecd42348f7a4b458/NeptuneLander.bas) · [source 6](https://github.com/OldSkoolCoder/NeptuneLander/blob/5314bbb5e21268c4d6af51b2ecd42348f7a4b458/README.md)

**Runtime requirements (no-evidence-found):** No sufficiently specific supported minimum hardware configuration was established for a runtime profile. Target C64 and observed native ISA are not evidence of a tested CPU/RAM minimum. Video/timing evidence: Native C64/MOS 6510 assembly with BASIC bootstrap and fixed raster wait; CBM prg Studio host tooling. No PAL/NTSC guarantee established. Relevant limits: The README still calls development ongoing; do not report a completed/public release or independently playable state.

Evidence: [source 1](https://github.com/OldSkoolCoder/NeptuneLander/blob/5314bbb5e21268c4d6af51b2ecd42348f7a4b458/NeptuneLander_V2.asm) · [source 2](https://github.com/OldSkoolCoder/NeptuneLander/blob/5314bbb5e21268c4d6af51b2ecd42348f7a4b458/gameLander.asm) · [source 3](https://github.com/OldSkoolCoder/NeptuneLander/blob/5314bbb5e21268c4d6af51b2ecd42348f7a4b458/gameFlow.asm) · [source 4](https://github.com/OldSkoolCoder/NeptuneLander/blob/5314bbb5e21268c4d6af51b2ecd42348f7a4b458/NeptuneLander.bas) · [source 5](https://github.com/OldSkoolCoder/NeptuneLander/blob/5314bbb5e21268c4d6af51b2ecd42348f7a4b458/README.md) · [source 6](https://github.com/OldSkoolCoder/NeptuneLander/blob/5314bbb5e21268c4d6af51b2ecd42348f7a4b458/NeptuneLander.cbmprj)

**AI attribution (no-evidence-found):** No explicit generative-AI attribution found in the selected README, implementation, build or license material and the first eight default-branch commit messages/author metadata (or all returned if fewer). One selected commit detail was read where recorded. This bounded review is not proof of non-use. Opponent gameplay AI is not generative-AI tooling evidence. Unknown is not evidence of non-use; named tools are not inferred from provider addresses, ordinary automation or gameplay AI.

Evidence: [source 1](https://api.github.com/repos/OldSkoolCoder/NeptuneLander/commits?per_page=8&page=1) · [source 2](https://github.com/OldSkoolCoder/NeptuneLander/commit/5314bbb5e21268c4d6af51b2ecd42348f7a4b458) · [source 3](https://github.com/OldSkoolCoder/NeptuneLander/blob/5314bbb5e21268c4d6af51b2ecd42348f7a4b458/NeptuneLander_V2.asm) · [source 4](https://github.com/OldSkoolCoder/NeptuneLander/blob/5314bbb5e21268c4d6af51b2ecd42348f7a4b458/gameLander.asm) · [source 5](https://github.com/OldSkoolCoder/NeptuneLander/blob/5314bbb5e21268c4d6af51b2ecd42348f7a4b458/gameFlow.asm) · [source 6](https://github.com/OldSkoolCoder/NeptuneLander/blob/5314bbb5e21268c4d6af51b2ecd42348f7a4b458/NeptuneLander.bas) · [source 7](https://github.com/OldSkoolCoder/NeptuneLander/blob/5314bbb5e21268c4d6af51b2ecd42348f7a4b458/README.md) · [source 8](https://github.com/OldSkoolCoder/NeptuneLander/blob/5314bbb5e21268c4d6af51b2ecd42348f7a4b458/NeptuneLander.cbmprj)

**Lineage and rights (reviewed):**  NeptuneLander-1 follows the same tutorial and is held as a variant rather than independently counted. Licensing: No standalone license grant established; metadata license is null and no license-named file occurs in the complete tree. Canonical root was absent from the verified 1,621-project d654a0c publication baseline and 1,861-root normalized reviewed index. Wider lineage/source coverage is still partial.

Evidence: [source 1](https://github.com/OldSkoolCoder/NeptuneLander/blob/5314bbb5e21268c4d6af51b2ecd42348f7a4b458/NeptuneLander_V2.asm) · [source 2](https://github.com/OldSkoolCoder/NeptuneLander/blob/5314bbb5e21268c4d6af51b2ecd42348f7a4b458/gameLander.asm) · [source 3](https://github.com/OldSkoolCoder/NeptuneLander/blob/5314bbb5e21268c4d6af51b2ecd42348f7a4b458/gameFlow.asm) · [source 4](https://github.com/OldSkoolCoder/NeptuneLander/blob/5314bbb5e21268c4d6af51b2ecd42348f7a4b458/NeptuneLander.bas) · [source 5](https://github.com/OldSkoolCoder/NeptuneLander/blob/5314bbb5e21268c4d6af51b2ecd42348f7a4b458/README.md) · [source 6](https://github.com/OldSkoolCoder/NeptuneLander/blob/5314bbb5e21268c4d6af51b2ecd42348f7a4b458/NeptuneLander.cbmprj) · [source 7](https://github.com/OldSkoolCoder/NeptuneLander-1/blob/14e0a5daa879c2784b17ff0006727f1701b38620/Main.asm) · [source 8](https://github.com/OldSkoolCoder/NeptuneLander-1/blob/14e0a5daa879c2784b17ff0006727f1701b38620/gameShip.asm) · [source 9](https://github.com/OldSkoolCoder/NeptuneLander-1/blob/14e0a5daa879c2784b17ff0006727f1701b38620/README.md)

### MOD Player: Java Amiga tracker-format playback

[Repository](https://github.com/SPixs/ModPlayer)

- Source platforms: Amiga
- Target platforms: Desktop
- Source CPU: Unasserted / not applicable
- Target CPU: Unasserted / not applicable
- Source material/language: Amiga MOD tracker-module data
- Maintained language: Java
- Classification: tooling; data-format-analysis, asset-tool
- Build flags: all unknown (compilable, runnable, playable and byte_exact).
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** README identifies ProTracker 31-sample and Soundtracker 15-sample playback, Java 11+, and a GUI with channel scopes/spectrum/VU display. ModPlayer.java parses MOD headers, sample metadata, pattern order and note/effect bytes, implements sample mixing and tracker effects, and outputs Java sampled audio. This is real format reimplementation, not a wrapper around a bundled MOD binary. README documents javac and jar commands; MANIFEST.MF selects modplayer.ui.ModPlayerUI. Commit history explicitly removed obsolete build.sh and build.gradle, so they should not be cited as current build instructions. No C64 source or SID runtime was found. HeroQuest-named synth support classes are not evidence of CPU emulation or a game reconstruction. Inspected snapshot: branch master, head commit 8aeea7cd6699b79fd0afce2051e1ad955290fe9d, git tree 0b9443863fc0d5cfde6e3fa0f05e2e6264f0e5d2. Head and tree are separate identities; the connector tree response top-level sha was not used as the actual tree identity. Inspection is a bounded sample, not all code/features.

Evidence: [source 1](https://github.com/SPixs/modplayer/blob/8aeea7cd6699b79fd0afce2051e1ad955290fe9d/README.md) · [source 2](https://github.com/SPixs/modplayer/blob/8aeea7cd6699b79fd0afce2051e1ad955290fe9d/src/main/java/modplayer/core/ModPlayer.java) · [source 3](https://github.com/SPixs/modplayer/blob/8aeea7cd6699b79fd0afce2051e1ad955290fe9d/src/main/java/modplayer/ui/ModPlayerUI.java) · [source 4](https://github.com/SPixs/modplayer/blob/8aeea7cd6699b79fd0afce2051e1ad955290fe9d/MANIFEST.MF) · [source 5](https://github.com/SPixs/ModPlayer/commit/8aeea7cd6699b79fd0afce2051e1ad955290fe9d)

**Classification (reviewed):** Host-side Java parser, tracker-effect engine, mixer and UI for ProTracker/Soundtracker module data. Amiga describes the input-format provenance, not a native Amiga executable. Java is a runtime rather than an inferred CPU/OS target.

Evidence: [source 1](https://github.com/SPixs/modplayer/blob/8aeea7cd6699b79fd0afce2051e1ad955290fe9d/README.md) · [source 2](https://github.com/SPixs/modplayer/blob/8aeea7cd6699b79fd0afce2051e1ad955290fe9d/src/main/java/modplayer/core/ModPlayer.java) · [source 3](https://github.com/SPixs/modplayer/blob/8aeea7cd6699b79fd0afce2051e1ad955290fe9d/src/main/java/modplayer/ui/ModPlayerUI.java) · [source 4](https://github.com/SPixs/modplayer/blob/8aeea7cd6699b79fd0afce2051e1ad955290fe9d/MANIFEST.MF)

**Source architecture (not-applicable):** The inspected input consists of legacy graphics/tracker/snapshot data, not native machine instructions. Do not assign a source CPU from the original platform or data-format association.

Evidence: [source 1](https://github.com/SPixs/modplayer/blob/8aeea7cd6699b79fd0afce2051e1ad955290fe9d/README.md) · [source 2](https://github.com/SPixs/modplayer/blob/8aeea7cd6699b79fd0afce2051e1ad955290fe9d/src/main/java/modplayer/core/ModPlayer.java) · [source 3](https://github.com/SPixs/modplayer/blob/8aeea7cd6699b79fd0afce2051e1ad955290fe9d/src/main/java/modplayer/ui/ModPlayerUI.java) · [source 4](https://github.com/SPixs/modplayer/blob/8aeea7cd6699b79fd0afce2051e1ad955290fe9d/MANIFEST.MF)

**Target architecture (not-applicable):** The delivered tooling is portable Java or browser TypeScript/JavaScript working with data, not a native code generator. No fixed host CPU target is established; do not infer one from Java, JavaScript, a browser or the legacy input format.

Evidence: [source 1](https://github.com/SPixs/modplayer/blob/8aeea7cd6699b79fd0afce2051e1ad955290fe9d/README.md) · [source 2](https://github.com/SPixs/modplayer/blob/8aeea7cd6699b79fd0afce2051e1ad955290fe9d/MANIFEST.MF) · [source 3](https://github.com/SPixs/modplayer/blob/8aeea7cd6699b79fd0afce2051e1ad955290fe9d/src/main/java/modplayer/core/ModPlayer.java) · [source 4](https://github.com/SPixs/modplayer/blob/8aeea7cd6699b79fd0afce2051e1ad955290fe9d/src/main/java/modplayer/ui/ModPlayerUI.java)

**Build and verification (needs-research):** README documents javac and jar commands; MANIFEST.MF selects modplayer.ui.ModPlayerUI. Commit history explicitly removed obsolete build.sh and build.gradle, so they should not be cited as current build instructions. README asserts MIT, but the complete tree has no LICENSE file or full MIT text; retain this as a README license claim. README calls bundled mods public domain, but no per-track provenance/license evidence was reviewed. Do not treat the claim as established rights for all supplied music. The parser recognizes 6CHN/8CHN signatures while the visualization playback buffers are fixed to four channels; broader multichannel compatibility should not be claimed. Java 11+ desktop runtime is documented; Desktop is the existing generic host label. Exact host OS support is not independently verified; JVM is a runtime note. No audio fidelity, ProTracker compatibility, runtime or build verification. No candidate compilation, execution, emulator/gameplay test, hardware test, round-trip or byte comparison was run. compilable/runnable/playable/byte_exact all remain null.

Evidence: [source 1](https://github.com/SPixs/modplayer/blob/8aeea7cd6699b79fd0afce2051e1ad955290fe9d/README.md) · [source 2](https://github.com/SPixs/modplayer/blob/8aeea7cd6699b79fd0afce2051e1ad955290fe9d/MANIFEST.MF) · [source 3](https://github.com/SPixs/modplayer/blob/8aeea7cd6699b79fd0afce2051e1ad955290fe9d/src/main/java/modplayer/core/ModPlayer.java) · [source 4](https://github.com/SPixs/modplayer/blob/8aeea7cd6699b79fd0afce2051e1ad955290fe9d/src/main/java/modplayer/ui/ModPlayerUI.java)

**Runtime requirements (reviewed):** README explicitly documents Java 11+ desktop execution, retained as a qualitative runtime requirement. No particular host OS, CPU architecture or RAM minimum is inferred. The parser/UI four-channel versus 6CHN/8CHN discrepancy prevents a broad multichannel compatibility claim; audio fidelity and runtime were not tested.

Evidence: [source 1](https://github.com/SPixs/modplayer/blob/8aeea7cd6699b79fd0afce2051e1ad955290fe9d/README.md) · [source 2](https://github.com/SPixs/modplayer/blob/8aeea7cd6699b79fd0afce2051e1ad955290fe9d/src/main/java/modplayer/core/ModPlayer.java) · [source 3](https://github.com/SPixs/modplayer/blob/8aeea7cd6699b79fd0afce2051e1ad955290fe9d/src/main/java/modplayer/ui/ModPlayerUI.java) · [source 4](https://github.com/SPixs/modplayer/blob/8aeea7cd6699b79fd0afce2051e1ad955290fe9d/MANIFEST.MF)

**AI attribution (no-evidence-found):** No explicit generative-AI attribution found in selected source/build/license files and the latest up-to-30 default-branch commits (9 returned). This bounded review is not proof of non-use. Unknown is not evidence of non-use; named tools are not inferred from provider addresses, ordinary automation or gameplay AI.

Evidence: [source 1](https://api.github.com/repos/SPixs/modplayer/commits?per_page=30) · [source 2](https://github.com/SPixs/ModPlayer/commit/8aeea7cd6699b79fd0afce2051e1ad955290fe9d) · [source 3](https://github.com/SPixs/modplayer/blob/8aeea7cd6699b79fd0afce2051e1ad955290fe9d/README.md) · [source 4](https://github.com/SPixs/modplayer/blob/8aeea7cd6699b79fd0afce2051e1ad955290fe9d/src/main/java/modplayer/core/ModPlayer.java) · [source 5](https://github.com/SPixs/modplayer/blob/8aeea7cd6699b79fd0afce2051e1ad955290fe9d/src/main/java/modplayer/ui/ModPlayerUI.java) · [source 6](https://github.com/SPixs/modplayer/blob/8aeea7cd6699b79fd0afce2051e1ad955290fe9d/MANIFEST.MF)

**Lineage and rights (reviewed):**  Licensing: README claims MIT; complete MIT text absent. Bundled tracker-module rights unverified separately. Canonical root was absent from the verified 1,621-project d654a0c publication baseline and 1,861-root normalized reviewed index. Wider lineage/source coverage is still partial.

Evidence: [source 1](https://github.com/SPixs/modplayer/blob/8aeea7cd6699b79fd0afce2051e1ad955290fe9d/README.md) · [source 2](https://github.com/SPixs/modplayer/blob/8aeea7cd6699b79fd0afce2051e1ad955290fe9d/src/main/java/modplayer/core/ModPlayer.java) · [source 3](https://github.com/SPixs/modplayer/blob/8aeea7cd6699b79fd0afce2051e1ad955290fe9d/src/main/java/modplayer/ui/ModPlayerUI.java) · [source 4](https://github.com/SPixs/modplayer/blob/8aeea7cd6699b79fd0afce2051e1ad955290fe9d/MANIFEST.MF)

Documented profiles: [{"name": "Documented Java desktop runtime", "platform": "Desktop", "notes": "README requires Java 11 or later. This is a portable JVM desktop playback program for Amiga MOD inputs, not a native Amiga binary. No host OS/CPU/RAM minimum or playback fidelity was independently tested.", "evidence": ["https://github.com/SPixs/modplayer/blob/8aeea7cd6699b79fd0afce2051e1ad955290fe9d/README.md"]}]

### Painter: Windows image editor with Amiga ILBM support

[Repository](https://github.com/GeorgRottensteiner/Painter)

- Source platforms: Amiga
- Target platforms: Windows
- Source CPU: Unasserted / not applicable
- Target CPU: x86 (32-bit)
- Source material/language: Amiga IFF/ILBM image data
- Maintained language: C++, Lua
- Classification: tooling; data-format-analysis, asset-tool
- Build flags: all unknown (compilable, runnable, playable and byte_exact).
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** FormatManager.cpp registers both load/save handlers for IFF and integrates image format conversion. PainterLua.cpp registers pixel, image, selection and crop operations. scripts/cutc64screen.lua only calls CreateNewImageFromRect(67,112,640,350); it does not establish a C64 image decoder/exporter or native C64 executable. painter.vcxproj targets Windows Win32 with static MFC and v145 toolset, and directly compiles external P:\Common image, stream, Lua, codec and utility sources. The referenced Common FormatIFF implementation reads ILBM BMHD/CMAP/BODY chunks and writes ILBM bitplanes; this is the substantive Amiga-format connection. No README is present in the complete tree. Build and source, rather than the short GitHub description, establish the app's role. Inspected snapshot: branch master, head commit 5ffdd2ec88262246a011b9a71ea2a1ba06120b57, git tree 5a0523970c2c92ba64b152b231f3640515e7f0a7. Head and tree are separate identities; the connector tree response top-level sha was not used as the actual tree identity. Inspection is a bounded sample, not all code/features.

Evidence: [source 1](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/FormatManager.cpp) · [source 2](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/painterDoc.cpp) · [source 3](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/PainterLua.cpp) · [source 4](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/scripts/cutc64screen.lua) · [source 5](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/painter.vcxproj) · [source 6](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/UNLICENSE) · [source 7](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/FreeImage.h) · [source 8](https://github.com/GeorgRottensteiner/Painter/commit/5ffdd2ec88262246a011b9a71ea2a1ba06120b57)

**Classification (reviewed):** Windows Win32/MFC image editor using a directly compiled Common IFF/ILBM implementation. Amiga identifies a concrete image-data format, not a native 68000 program. The C64-named crop script does not establish a native C64 decoder or output.

Evidence: [source 1](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/FormatManager.cpp) · [source 2](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/painterDoc.cpp) · [source 3](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/PainterLua.cpp) · [source 4](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/scripts/cutc64screen.lua) · [source 5](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/painter.vcxproj) · [source 6](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/UNLICENSE) · [source 7](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/FreeImage.h)

**Source architecture (not-applicable):** The inspected input consists of legacy graphics/tracker/snapshot data, not native machine instructions. Do not assign a source CPU from the original platform or data-format association.

Evidence: [source 1](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/FormatManager.cpp) · [source 2](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/painterDoc.cpp) · [source 3](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/PainterLua.cpp) · [source 4](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/scripts/cutc64screen.lua) · [source 5](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/painter.vcxproj) · [source 6](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/UNLICENSE) · [source 7](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/FreeImage.h)

**Target architecture (reviewed):** painter.vcxproj explicitly selects Win32 configurations and MFC host build, supporting x86 (32-bit) as the produced host architecture. This is not a 68000/C64 CPU target, nor a verified minimum Windows version or runtime.

Evidence: [source 1](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/painter.vcxproj) · [source 2](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/FormatManager.cpp) · [source 3](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/painterDoc.cpp) · [source 4](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/PainterLua.cpp) · [source 5](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/scripts/cutc64screen.lua)

**Build and verification (needs-research):** painter.vcxproj targets Windows Win32 with static MFC and v145 toolset, and directly compiles external P:\Common image, stream, Lua, codec and utility sources. No README is present in the complete tree. Build and source, rather than the short GitHub description, establish the app's role. Absolute P:\Common dependencies and included binary libraries mean a standalone clone is not a demonstrated reproducible build. UNLICENSE applies to the project's own software; bundled FreeImage and other third-party components carry separate notices. Common has no root license identified. The imported IFF code skips CAMG and other special chunks; do not claim complete Amiga graphics-mode compatibility. No image round-trip or runtime tests performed. Sample IFF images include named game/scene assets; their individual rights were not established. No candidate compilation, execution, emulator/gameplay test, hardware test, round-trip or byte comparison was run. compilable/runnable/playable/byte_exact all remain null.

Evidence: [source 1](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/painter.vcxproj) · [source 2](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/FormatManager.cpp) · [source 3](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/painterDoc.cpp) · [source 4](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/PainterLua.cpp) · [source 5](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/scripts/cutc64screen.lua) · [source 6](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/UNLICENSE) · [source 7](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/FreeImage.h)

**Runtime requirements (no-evidence-found):** No fixed numerical CPU/RAM/OS minimum or independently verified runnable configuration was established. Host-language/runtime and legacy input format are kept separate from native legacy hardware; runtime_profiles remains empty. Win32 x86 MFC host; manipulates legacy image data, does not execute Amiga or C64 CPU code. Absolute P:\Common dependencies and included binary libraries mean a standalone clone is not a demonstrated reproducible build. UNLICENSE applies to the project's own software; bundled FreeImage and other third-party components carry separate notices. Common has no root license identified. The imported IFF code skips CAMG and other special chunks; do not claim complete Amiga graphics-mode compatibility. No image round-trip or runtime tests performed. Sample IFF images include named game/scene assets; their individual rights were not established.

Evidence: [source 1](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/FormatManager.cpp) · [source 2](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/painterDoc.cpp) · [source 3](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/PainterLua.cpp) · [source 4](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/scripts/cutc64screen.lua) · [source 5](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/painter.vcxproj) · [source 6](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/UNLICENSE) · [source 7](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/FreeImage.h)

**AI attribution (no-evidence-found):** No explicit generative-AI attribution found in selected source/build/license files and the latest up-to-30 default-branch commits (6 returned). This bounded review is not proof of non-use. Unknown is not evidence of non-use; named tools are not inferred from provider addresses, ordinary automation or gameplay AI.

Evidence: [source 1](https://api.github.com/repos/GeorgRottensteiner/Painter/commits?per_page=30) · [source 2](https://github.com/GeorgRottensteiner/Painter/commit/5ffdd2ec88262246a011b9a71ea2a1ba06120b57) · [source 3](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/FormatManager.cpp) · [source 4](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/painterDoc.cpp) · [source 5](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/PainterLua.cpp) · [source 6](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/scripts/cutc64screen.lua) · [source 7](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/painter.vcxproj) · [source 8](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/UNLICENSE) · [source 9](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/FreeImage.h)

**Lineage and rights (reviewed):** Directly compiled shared source dependency, including IFF handler; not an independent new project in this review. georgrottensteiner/common Common FormatIFF.cpp is directly compiled by Painter and supplies the ILBM parser/writer; Common is recorded as a dependency reference, not a second tool project. Licensing: UNLICENSE is explicit for project software; FreeImage.h has separate covered-code notices, and external Common/third-party source needs independent licensing review. Canonical root was absent from the verified 1,621-project d654a0c publication baseline and 1,861-root normalized reviewed index. Wider lineage/source coverage is still partial.

Evidence: [source 1](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/FormatManager.cpp) · [source 2](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/painterDoc.cpp) · [source 3](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/PainterLua.cpp) · [source 4](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/scripts/cutc64screen.lua) · [source 5](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/painter.vcxproj) · [source 6](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/UNLICENSE) · [source 7](https://github.com/GeorgRottensteiner/Painter/blob/5ffdd2ec88262246a011b9a71ea2a1ba06120b57/FreeImage.h) · [source 8](https://github.com/GeorgRottensteiner/Common/blob/e0715dc60b28e079c4f0b37ddeb59486791cd8f5/Grafik/ImageFormate/FormatIFF.cpp) · [source 9](https://github.com/GeorgRottensteiner/Common/blob/e0715dc60b28e079c4f0b37ddeb59486791cd8f5/Grafik/ImageFormate/FormatIFF.h)

### Spritemate: C64 sprite editor and snapshot tools

[Repository](https://github.com/Esshahn/spritemate)

- Source platforms: C64
- Target platforms: Web
- Source CPU: Unasserted / not applicable
- Target CPU: Unasserted / not applicable
- Source material/language: C64 SpritePad sprite data, VICE snapshot data
- Maintained language: TypeScript, JavaScript
- Classification: tooling; data-format-analysis, asset-tool, binary-analysis
- Build flags: all unknown (compilable, runnable, playable and byte_exact).
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** README specifies 24x21 single-color/12x21 multicolor sprite canvases, C64 palette constraints and client-side browser operation; source is TypeScript, despite older JavaScript wording. Load.ts parses SpritePad data and constructs internal sprite pixels; Save.ts packs sprite bytes and color/overlay metadata back into SpritePad output. Sprite.ts and Editor.ts implement sprite state and canvas editing. Snapshot.ts locates C64MEM, CIA2 and VIC-II blocks in a VICE snapshot, uses VIC/CIA memory registers, and exposes sprite-address/grab commands. This is static snapshot analysis, not CPU emulation. package.json provides npm run dev/build using Vite, with JSZip runtime dependency; vite.config.js outputs dist with relative base path. README's no-dependency phrasing is qualified by its later JSZip note and package manifest. LICENSE supplies complete MIT text and copyright 2017 Ingo Hinterding. Latest 30 commits and selected sources contain no explicit AI-tool attribution. A further bounded exact-name Claude commit search returned no matches; Dependabot entries are dependency automation, not generative-AI evidence. Inspected snapshot: branch main, head commit e70a29d32a2040cc217193dfafc7f11418fc9cf4, git tree 7f907ca1521a178f85be20fa456b02181cc1276c. Head and tree are separate identities; the connector tree response top-level sha was not used as the actual tree identity. Inspection is a bounded sample, not all code/features.

Evidence: [source 1](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/README.md) · [source 2](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/src/js/Sprite.ts) · [source 3](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/src/js/Editor.ts) · [source 4](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/src/js/Load.ts) · [source 5](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/src/js/Save.ts) · [source 6](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/src/js/Snapshot.ts) · [source 7](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/src/js/Export-Base.ts) · [source 8](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/package.json) · [source 9](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/vite.config.js) · [source 10](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/tsconfig.json) · [source 11](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/LICENSE) · [source 12](https://github.com/Esshahn/spritemate/commit/e70a29d32a2040cc217193dfafc7f11418fc9cf4)

**Classification (reviewed):** Browser-hosted sprite authoring and static VICE snapshot analysis. It parses C64-specific graphics/machine-state data, but does not execute 6502 instructions or reconstruct a historical game. No CPU architecture is assigned from TypeScript or the formats.

Evidence: [source 1](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/README.md) · [source 2](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/src/js/Sprite.ts) · [source 3](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/src/js/Editor.ts) · [source 4](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/src/js/Load.ts) · [source 5](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/src/js/Save.ts) · [source 6](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/src/js/Snapshot.ts) · [source 7](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/src/js/Export-Base.ts) · [source 8](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/package.json) · [source 9](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/vite.config.js) · [source 10](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/tsconfig.json) · [source 11](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/LICENSE)

**Source architecture (not-applicable):** The inspected input consists of legacy graphics/tracker/snapshot data, not native machine instructions. Do not assign a source CPU from the original platform or data-format association.

Evidence: [source 1](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/README.md) · [source 2](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/src/js/Sprite.ts) · [source 3](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/src/js/Editor.ts) · [source 4](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/src/js/Load.ts) · [source 5](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/src/js/Save.ts) · [source 6](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/src/js/Snapshot.ts) · [source 7](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/src/js/Export-Base.ts) · [source 8](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/package.json) · [source 9](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/vite.config.js) · [source 10](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/tsconfig.json) · [source 11](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/LICENSE)

**Target architecture (not-applicable):** The delivered tooling is portable Java or browser TypeScript/JavaScript working with data, not a native code generator. No fixed host CPU target is established; do not infer one from Java, JavaScript, a browser or the legacy input format.

Evidence: [source 1](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/package.json) · [source 2](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/vite.config.js) · [source 3](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/tsconfig.json) · [source 4](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/README.md) · [source 5](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/src/js/Sprite.ts) · [source 6](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/src/js/Editor.ts) · [source 7](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/src/js/Load.ts) · [source 8](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/src/js/Save.ts) · [source 9](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/src/js/Snapshot.ts) · [source 10](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/src/js/Export-Base.ts)

**Build and verification (needs-research):** package.json provides npm run dev/build using Vite, with JSZip runtime dependency; vite.config.js outputs dist with relative base path. README's no-dependency phrasing is qualified by its later JSZip note and package manifest. No npm install/build, browser UI exercise, SpritePad round-trip test or VICE-version compatibility test performed. Snapshot parsing uses module markers and assumptions; support for every VICE snapshot version is not established. Bundled examples named after commercial C64 games and any sprites extracted from commercial snapshots have separate asset rights; the MIT software grant does not establish permission for all artwork. README and package version labels differ; preserve inspected commit identity rather than assume a release/version from one label. Related conversion tools/forks such as png2spd, charset2png and SpriteMateX were not counted as additional projects or reviewed here. No candidate compilation, execution, emulator/gameplay test, hardware test, round-trip or byte comparison was run. compilable/runnable/playable/byte_exact all remain null.

Evidence: [source 1](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/package.json) · [source 2](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/vite.config.js) · [source 3](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/tsconfig.json) · [source 4](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/README.md) · [source 5](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/src/js/Sprite.ts) · [source 6](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/src/js/Editor.ts) · [source 7](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/src/js/Load.ts) · [source 8](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/src/js/Save.ts) · [source 9](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/src/js/Snapshot.ts) · [source 10](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/src/js/Export-Base.ts) · [source 11](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/LICENSE)

**Runtime requirements (no-evidence-found):** No fixed numerical CPU/RAM/OS minimum or independently verified runnable configuration was established. Host-language/runtime and legacy input format are kept separate from native legacy hardware; runtime_profiles remains empty. No CPU emulator. Host TypeScript/JavaScript manipulates VIC-II sprite formats and stored C64 machine snapshots. No npm install/build, browser UI exercise, SpritePad round-trip test or VICE-version compatibility test performed. Snapshot parsing uses module markers and assumptions; support for every VICE snapshot version is not established. Bundled examples named after commercial C64 games and any sprites extracted from commercial snapshots have separate asset rights; the MIT software grant does not establish permission for all artwork. README and package version labels differ; preserve inspected commit identity rather than assume a release/version from one label. Related conversion tools/forks such as png2spd, charset2png and SpriteMateX were not counted as additional projects or reviewed here.

Evidence: [source 1](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/README.md) · [source 2](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/src/js/Sprite.ts) · [source 3](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/src/js/Editor.ts) · [source 4](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/src/js/Load.ts) · [source 5](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/src/js/Save.ts) · [source 6](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/src/js/Snapshot.ts) · [source 7](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/src/js/Export-Base.ts) · [source 8](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/package.json) · [source 9](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/vite.config.js) · [source 10](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/tsconfig.json) · [source 11](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/LICENSE)

**AI attribution (no-evidence-found):** No explicit generative-AI attribution found in selected repository evidence and latest up-to-30 commit metadata/messages (30 returned). Bounded review, not proof of non-use. Unknown is not evidence of non-use; named tools are not inferred from provider addresses, ordinary automation or gameplay AI.

Evidence: [source 1](https://api.github.com/repos/Esshahn/spritemate/commits?per_page=30) · [source 2](https://github.com/Esshahn/spritemate/commit/e70a29d32a2040cc217193dfafc7f11418fc9cf4) · [source 3](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/README.md) · [source 4](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/src/js/Sprite.ts) · [source 5](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/src/js/Editor.ts) · [source 6](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/src/js/Load.ts) · [source 7](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/src/js/Save.ts) · [source 8](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/src/js/Snapshot.ts) · [source 9](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/src/js/Export-Base.ts) · [source 10](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/package.json) · [source 11](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/vite.config.js) · [source 12](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/tsconfig.json) · [source 13](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/LICENSE)

**Lineage and rights (reviewed):**  Licensing: Complete root MIT license. Example/extracted game graphics require separate rights review. Canonical root was absent from the verified 1,621-project d654a0c publication baseline and 1,861-root normalized reviewed index. Wider lineage/source coverage is still partial.

Evidence: [source 1](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/README.md) · [source 2](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/src/js/Sprite.ts) · [source 3](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/src/js/Editor.ts) · [source 4](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/src/js/Load.ts) · [source 5](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/src/js/Save.ts) · [source 6](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/src/js/Snapshot.ts) · [source 7](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/src/js/Export-Base.ts) · [source 8](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/package.json) · [source 9](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/vite.config.js) · [source 10](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/tsconfig.json) · [source 11](https://github.com/Esshahn/spritemate/blob/e70a29d32a2040cc217193dfafc7f11418fc9cf4/LICENSE)

### AmiFTP 2 — restored native Amiga FTP client

[Repository](https://github.com/amigazen/AmiFTP)

- Source platforms: Amiga
- Target platforms: Amiga
- Source CPU: Unasserted / not applicable
- Target CPU: Unasserted / not applicable
- Source material/language: C
- Maintained language: C
- Classification: subject; application, source-restoration
- Build flags: all unknown (compilable, runnable, playable and byte_exact).
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Magnus Lilja’s native Amiga FTP client revived for modern ReAction/NDK 3.2 and bsdsocket.library. Source snapshot 661bfd66943399356817ad978e2aa275a11e1868; screened new against all 1,621 projects, sources, decisions and prior reviews.

Evidence: [source 1](https://github.com/amigazen/AmiFTP/blob/main/README.md) · [source 2](https://github.com/amigazen/AmiFTP/blob/main/Source/amiftp/ftp.c) · [source 3](https://github.com/amigazen/AmiFTP)

**Classification (reviewed):** original-source Amiga FTP client modernization. README documents GUI transfers, Aminet mode, ARexx scripting, transfer resume and PASV/PORT support; ftp.c implements socket connection, command/reply, send/receive and passive fallback paths. The SAS/C smakefile links ReAction, rtasl.lib and tcp.lib with the UI/FTP implementation; AS225 support is disabled in the current documented version. Structured class subject preserves ordinary original source/port work without inventing binary decompilation.

Evidence: [source 1](https://github.com/amigazen/AmiFTP/blob/main/README.md) · [source 2](https://github.com/amigazen/AmiFTP/blob/main/Source/amiftp/ftp.c)

**Source architecture (no-evidence-found):** Preserved original C application, not disassembled machine code. The selected C source and SAS/C configuration do not independently establish an exact original ISA; source_cpu remains unknown rather than inferred from Amiga.

Evidence: [source 1](https://github.com/amigazen/AmiFTP/blob/main/README.md) · [source 2](https://github.com/amigazen/AmiFTP/blob/main/Source/amiftp/ftp.c)

**Target architecture (no-evidence-found):** Current SAS/C makefile links native Amiga ReAction/TCP libraries but has no explicit CPU setting or inspected ISA-specific module. Target CPU remains unasserted; this does not imply the Amiga target is absent.

Evidence: [source 1](https://github.com/amigazen/AmiFTP/blob/main/Source/amiftp/SMakefile) · [source 2](https://github.com/amigazen/AmiFTP/blob/main/Source/amiftp/SCOPTIONS) · [source 3](https://github.com/amigazen/AmiFTP/blob/main/README.md)

**Build and verification (reviewed):** README documents GUI transfers, Aminet mode, ARexx scripting, transfer resume and PASV/PORT support; ftp.c implements socket connection, command/reply, send/receive and passive fallback paths. The SAS/C smakefile links ReAction, rtasl.lib and tcp.lib with the UI/FTP implementation; AS225 support is disabled in the current documented version. README requires AmigaOS 3.2 with ReAction; older ClassAct systems are only described as possible. External SDK/toolchain assignments and link libraries must be supplied. No secure-FTP/TLS functionality or security audit is established by this review. Top-level MIT terms do not erase the legacy four-clause Berkeley notice retained in ftp.c. No candidate was built, run or byte-compared. All build flags remain unknown; checked-in binaries, build recipes and upstream claims are not independent tests.

Evidence: [source 1](https://github.com/amigazen/AmiFTP/blob/main/Source/amiftp/SMakefile) · [source 2](https://github.com/amigazen/AmiFTP/blob/main/Source/amiftp/SCOPTIONS) · [source 3](https://github.com/amigazen/AmiFTP/blob/main/README.md)

**Runtime requirements (no-evidence-found):** Classic 68k Amiga target; no exact minimum CPU enforced by the inspected current makefile. AmigaOS 3.2/ReAction and bsdsocket.library are documented runtime requirements. README requires AmigaOS 3.2 with ReAction; older ClassAct systems are only described as possible. External SDK/toolchain assignments and link libraries must be supplied. No secure-FTP/TLS functionality or security audit is established by this review. Top-level MIT terms do not erase the legacy four-clause Berkeley notice retained in ftp.c. No complete independently verified hardware matrix is asserted.

Evidence: [source 1](https://github.com/amigazen/AmiFTP/blob/main/README.md) · [source 2](https://github.com/amigazen/AmiFTP/blob/main/Source/amiftp/SMakefile) · [source 3](https://github.com/amigazen/AmiFTP/blob/main/Source/amiftp/SCOPTIONS)

**AI attribution (no-evidence-found):** No unambiguous AI-tool implementation/review attribution found in inspected documentation, source/build/license files and 18 latest returned commits. This is a bounded sample, not proof of no AI use.

Evidence: [source 1](https://github.com/amigazen/AmiFTP/commits/main/) · [source 2](https://github.com/amigazen/AmiFTP/blob/main/README.md)

**Lineage and rights (reviewed):** MIT for current release, with retained third-party four-clause Berkeley notice in ftp.c; preserve per-file terms. README requires AmigaOS 3.2 with ReAction; older ClassAct systems are only described as possible. External SDK/toolchain assignments and link libraries must be supplied. No secure-FTP/TLS functionality or security audit is established by this review. Top-level MIT terms do not erase the legacy four-clause Berkeley notice retained in ftp.c.  Related source graph remains partial.

Evidence: [source 1](https://github.com/amigazen/AmiFTP/blob/main/LICENSE.md) · [source 2](https://github.com/amigazen/AmiFTP/blob/main/Source/amiftp/ftp.c) · [source 3](https://github.com/amigazen/AmiFTP/blob/main/README.md) · [source 4](https://github.com/amigazen/AmiFTP)

### IFFTools — native Amiga image and audio converters

[Repository](https://github.com/amigazen/ifftools)

- Source platforms: Amiga
- Target platforms: Amiga
- Source CPU: Unasserted / not applicable
- Target CPU: Unasserted / not applicable
- Source material/language: Unasserted / not applicable
- Maintained language: C
- Classification: tooling; asset-tool
- Build flags: all unknown (compilable, runnable, playable and byte_exact).
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Native Amiga IFF image/audio decoding libraries plus iff2png and iff2aiff converters, with SAS/C build integration. Source snapshot 7d7cfefcfc5d4066cbd9a58c33f5e3def4ad0ff4; screened new against all 1,621 projects, sources, decisions and prior reviews.

Evidence: [source 1](https://github.com/amigazen/IFFTools/blob/main/README.md) · [source 2](https://github.com/amigazen/IFFTools/blob/main/Source/iffpicturelib/image_decoder.c) · [source 3](https://github.com/amigazen/ifftools)

**Classification (reviewed):** native Amiga image/audio format libraries and converters. image_decoder.c contains concrete bitplane extraction and IFF bitmap decoding; sound_decoder.c implements sound decompression/conversion paths. SMakefile builds iffpicture.lib, iffsound.lib and two conversion commands; bundled libpng/zlib are dependencies rather than extra projects. Structured class tooling preserves ordinary original source/port work without inventing binary decompilation.

Evidence: [source 1](https://github.com/amigazen/IFFTools/blob/main/README.md) · [source 2](https://github.com/amigazen/IFFTools/blob/main/Source/iffpicturelib/image_decoder.c) · [source 3](https://github.com/amigazen/IFFTools/blob/main/Source/iffsoundlib/sound_decoder.c)

**Source architecture (not-applicable):** Inputs are IFF image/audio data, not original CPU instructions. source_cpu is not applicable; Amiga names the actual format ecosystem.

Evidence: [source 1](https://github.com/amigazen/IFFTools/blob/main/README.md) · [source 2](https://github.com/amigazen/IFFTools/blob/main/Source/iffpicturelib/image_decoder.c) · [source 3](https://github.com/amigazen/IFFTools/blob/main/Source/iffsoundlib/sound_decoder.c)

**Target architecture (no-evidence-found):** The inspected C and SAS/C recipes lack an explicit CPU model or ISA-specific module. A CPU is not inferred from the platform/compiler label alone; native Amiga APIs remain explicit.

Evidence: [source 1](https://github.com/amigazen/IFFTools/blob/main/Source/SMakefile) · [source 2](https://github.com/amigazen/IFFTools/blob/main/README.md)

**Build and verification (reviewed):** image_decoder.c contains concrete bitplane extraction and IFF bitmap decoding; sound_decoder.c implements sound decompression/conversion paths. SMakefile builds iffpicture.lib, iffsound.lib and two conversion commands; bundled libpng/zlib are dependencies rather than extra projects. README lists a broad format matrix, but not every advertised variant was independently audited or exercised. Requires Amiga SDK/SAS/C setup, libpng/zlib dependencies and Amiga library interfaces. No independent corpus-conformance tests; bundled data and third-party dependency notices need their own rights checks. No candidate was built, run or byte-compared. All build flags remain unknown; checked-in binaries, build recipes and upstream claims are not independent tests.

Evidence: [source 1](https://github.com/amigazen/IFFTools/blob/main/Source/SMakefile) · [source 2](https://github.com/amigazen/IFFTools/blob/main/README.md)

**Runtime requirements (no-evidence-found):** Classic 68k Amiga native code; exact minimum CPU and OS not established by inspected build. IEEE math runtime used for audio path. README lists a broad format matrix, but not every advertised variant was independently audited or exercised. Requires Amiga SDK/SAS/C setup, libpng/zlib dependencies and Amiga library interfaces. No independent corpus-conformance tests; bundled data and third-party dependency notices need their own rights checks. No complete independently verified hardware matrix is asserted.

Evidence: [source 1](https://github.com/amigazen/IFFTools/blob/main/README.md) · [source 2](https://github.com/amigazen/IFFTools/blob/main/Source/SMakefile)

**AI attribution (no-evidence-found):** No unambiguous AI-tool implementation/review attribution found in inspected documentation, source/build/license files and 28 latest returned commits. This is a bounded sample, not proof of no AI use.

Evidence: [source 1](https://github.com/amigazen/IFFTools/commits/main/) · [source 2](https://github.com/amigazen/IFFTools/blob/main/README.md)

**Lineage and rights (reviewed):** BSD-2-Clause notices for original IFFTools components; bundled libpng and zlib retain their own terms. README lists a broad format matrix, but not every advertised variant was independently audited or exercised. Requires Amiga SDK/SAS/C setup, libpng/zlib dependencies and Amiga library interfaces. No independent corpus-conformance tests; bundled data and third-party dependency notices need their own rights checks.  Related source graph remains partial.

Evidence: [source 1](https://github.com/amigazen/IFFTools/blob/main/LICENSE.md) · [source 2](https://github.com/amigazen/IFFTools/blob/main/Source/iffpicturelib/LICENSE.md) · [source 3](https://github.com/amigazen/IFFTools/blob/main/README.md) · [source 4](https://github.com/amigazen/ifftools)

### BGUI — preserved Amiga BOOPSI GUI framework

[Repository](https://github.com/amigazen/BGUI)

- Source platforms: Amiga
- Target platforms: Amiga
- Source CPU: Unasserted / not applicable
- Target CPU: m68020
- Source material/language: C
- Maintained language: C
- Classification: hybrid; development-tool, source-restoration, development-environment
- Build flags: all unknown (compilable, runnable, playable and byte_exact).
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Preserved and repackaged native Amiga BGUI framework, with class implementation, SDK, examples and preferences. Source snapshot 2b5f6a7b20bbf42ce1fa94d99129fb5ca47bac47; screened new against all 1,621 projects, sources, decisions and prior reviews.

Evidence: [source 1](https://github.com/amigazen/BGUI/blob/main/README.md) · [source 2](https://github.com/amigazen/BGUI/blob/main/src/baseclass.c) · [source 3](https://github.com/amigazen/BGUI)

**Classification (reviewed):** original-source Amiga BOOPSI GUI framework. baseclass.c implements BOOPSI object creation/render/layout/interaction and retains long historical RCS change notes; bgui_init.c opens native Amiga library dependencies. SAS/C build has standard/debug/enhanced variants; enhanced explicitly selects CPU=68020, while historical build notes say the standard build supports OS 2/68000. Structured class hybrid preserves ordinary original source/port work without inventing binary decompilation.

Evidence: [source 1](https://github.com/amigazen/BGUI/blob/main/README.md) · [source 2](https://github.com/amigazen/BGUI/blob/main/src/baseclass.c) · [source 3](https://github.com/amigazen/BGUI/blob/main/src/bgui_init.c)

**Source architecture (no-evidence-found):** Original framework source is preserved, but inspected generic/AROS-conditioned C does not uniquely establish an original CPU model. Historical platform descriptions alone are not native instruction evidence.

Evidence: [source 1](https://github.com/amigazen/BGUI/blob/main/README.md) · [source 2](https://github.com/amigazen/BGUI/blob/main/src/baseclass.c) · [source 3](https://github.com/amigazen/BGUI/blob/main/src/bgui_init.c)

**Target architecture (reviewed):** src/smakefile ENHANCED_OPTIONS explicitly selects CPU=68020. This field describes that build variant only; standard/debug variants and the historical standard OS2/68000 note do not establish an identical whole-suite minimum.

Evidence: [source 1](https://github.com/amigazen/BGUI/blob/main/src/smakefile) · [source 2](https://github.com/amigazen/BGUI/blob/main/src/make.cfg) · [source 3](https://github.com/amigazen/BGUI/blob/main/README.md)

**Build and verification (reviewed):** baseclass.c implements BOOPSI object creation/render/layout/interaction and retains long historical RCS change notes; bgui_init.c opens native Amiga library dependencies. SAS/C build has standard/debug/enhanced variants; enhanced explicitly selects CPU=68020, while historical build notes say the standard build supports OS 2/68000. Historical standard-build compatibility is a documented claim, not a tested current deployment profile. AROS support is visible in conditional source/build layout, but no new AROS platform label or tested AROS runtime is claimed. LICENSE.md is BSD-3-Clause, while LICENSE has an older use/copy permission notice; retain both and per-file copyrights rather than asserting uniform relicensing. No candidate was built, run or byte-compared. All build flags remain unknown; checked-in binaries, build recipes and upstream claims are not independent tests.

Evidence: [source 1](https://github.com/amigazen/BGUI/blob/main/src/smakefile) · [source 2](https://github.com/amigazen/BGUI/blob/main/src/make.cfg) · [source 3](https://github.com/amigazen/BGUI/blob/main/README.md)

**Runtime requirements (no-evidence-found):** Historical standard OS 2/68000 claim; enhanced SAS/C variant explicitly CPU=68020. Current build/runtime unverified. Historical standard-build compatibility is a documented claim, not a tested current deployment profile. AROS support is visible in conditional source/build layout, but no new AROS platform label or tested AROS runtime is claimed. LICENSE.md is BSD-3-Clause, while LICENSE has an older use/copy permission notice; retain both and per-file copyrights rather than asserting uniform relicensing. No complete independently verified hardware matrix is asserted.

Evidence: [source 1](https://github.com/amigazen/BGUI/blob/main/README.md) · [source 2](https://github.com/amigazen/BGUI/blob/main/src/smakefile) · [source 3](https://github.com/amigazen/BGUI/blob/main/src/make.cfg)

**AI attribution (no-evidence-found):** No unambiguous AI-tool implementation/review attribution found in inspected documentation, source/build/license files and 6 latest returned commits. This is a bounded sample, not proof of no AI use.

Evidence: [source 1](https://github.com/amigazen/BGUI/commits/main/) · [source 2](https://github.com/amigazen/BGUI/blob/main/README.md)

**Lineage and rights (reviewed):** BSD-3-Clause LICENSE.md alongside a legacy custom use/copy notice in LICENSE; provenance and per-file notices remain relevant. Historical standard-build compatibility is a documented claim, not a tested current deployment profile. AROS support is visible in conditional source/build layout, but no new AROS platform label or tested AROS runtime is claimed. LICENSE.md is BSD-3-Clause, while LICENSE has an older use/copy permission notice; retain both and per-file copyrights rather than asserting uniform relicensing.  Related source graph remains partial.

Evidence: [source 1](https://github.com/amigazen/BGUI/blob/main/LICENSE.md) · [source 2](https://github.com/amigazen/BGUI/blob/main/LICENSE) · [source 3](https://github.com/amigazen/BGUI/blob/main/README.md) · [source 4](https://github.com/amigazen/BGUI)

### ClassAction — restored Amiga file manager

[Repository](https://github.com/amigazen/ClassAction)

- Source platforms: Amiga
- Target platforms: Amiga
- Source CPU: Unasserted / not applicable
- Target CPU: m68020
- Source material/language: C, C++
- Maintained language: C, C++
- Classification: subject; application, source-restoration, source-reconstruction
- Build flags: all unknown (compilable, runnable, playable and byte_exact).
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** ClassAction’s historical Amiga file manager restored for a SAS/C 68020 build, including reconstructed preference/string-list helpers. Source snapshot b998b16d70be17844ba14860beb22b11e2add2c8; screened new against all 1,621 projects, sources, decisions and prior reviews.

Evidence: [source 1](https://github.com/amigazen/ClassAction/blob/main/classaction.readme) · [source 2](https://github.com/amigazen/ClassAction/blob/main/Source/ClassAction/ClassAction.cpp) · [source 3](https://github.com/amigazen/ClassAction)

**Classification (reviewed):** original-source Amiga file manager with reconstructed missing support code. Main C++ source implements ReAction file-manager setup, actions and library initialization. smakefile states missing Global/ IniFile and StringList sources were reconstructed from the 4.6 object API; concrete replacements are present. Current build embeds relocated resource objects through generated ClassAction_res_embed.c because original StormC resource objects have relocations rejected by SAS/C. Structured class subject preserves ordinary original source/port work without inventing binary decompilation.

Evidence: [source 1](https://github.com/amigazen/ClassAction/blob/main/classaction.readme) · [source 2](https://github.com/amigazen/ClassAction/blob/main/Source/ClassAction/ClassAction.cpp) · [source 3](https://github.com/amigazen/ClassAction/blob/main/Source/ClassAction/IniFile.cpp) · [source 4](https://github.com/amigazen/ClassAction/blob/main/Source/ClassAction/StringList.cpp)

**Source architecture (no-evidence-found):** The restoration preserves C/C++ and uses historical object APIs to replace missing Global support sources. The original object instruction stream was not disassembled in this pass; source CPU remains unasserted.

Evidence: [source 1](https://github.com/amigazen/ClassAction/blob/main/classaction.readme) · [source 2](https://github.com/amigazen/ClassAction/blob/main/Source/ClassAction/ClassAction.cpp) · [source 3](https://github.com/amigazen/ClassAction/blob/main/Source/ClassAction/IniFile.cpp) · [source 4](https://github.com/amigazen/ClassAction/blob/main/Source/ClassAction/StringList.cpp)

**Target architecture (reviewed):** The current Source/ClassAction/smakefile explicitly sets CPU=68020 for SAS/C. That build target is distinct from older source versions and from a verified runtime minimum.

Evidence: [source 1](https://github.com/amigazen/ClassAction/blob/main/Source/ClassAction/smakefile) · [source 2](https://github.com/amigazen/ClassAction/blob/main/classaction.readme)

**Build and verification (reviewed):** Main C++ source implements ReAction file-manager setup, actions and library initialization. smakefile states missing Global/ IniFile and StringList sources were reconstructed from the 4.6 object API; concrete replacements are present. Current build embeds relocated resource objects through generated ClassAction_res_embed.c because original StormC resource objects have relocations rejected by SAS/C. This is partial source restoration, not a clean all-source rebuild: object inputs remain required for resource regeneration. Documented AmigaOS 3.5/3.9 and resource.library/popupmenu/xadmaster/xfdmaster dependencies must be supplied. Historical binary distribution was mailware with noncommercial/no-alteration restrictions; source publication and preservation do not establish a standard open-source license. No candidate was built, run or byte-compared. All build flags remain unknown; checked-in binaries, build recipes and upstream claims are not independent tests.

Evidence: [source 1](https://github.com/amigazen/ClassAction/blob/main/Source/ClassAction/smakefile) · [source 2](https://github.com/amigazen/ClassAction/blob/main/classaction.readme)

**Runtime requirements (no-evidence-found):** Current SAS/C makefile CPU=68020; documented AmigaOS 3.5/3.9 + ReAction. Source checks individual library versions and dependencies; no runtime test. This is partial source restoration, not a clean all-source rebuild: object inputs remain required for resource regeneration. Documented AmigaOS 3.5/3.9 and resource.library/popupmenu/xadmaster/xfdmaster dependencies must be supplied. Historical binary distribution was mailware with noncommercial/no-alteration restrictions; source publication and preservation do not establish a standard open-source license. No complete independently verified hardware matrix is asserted.

Evidence: [source 1](https://github.com/amigazen/ClassAction/blob/main/classaction.readme) · [source 2](https://github.com/amigazen/ClassAction/blob/main/Source/ClassAction/smakefile)

**AI attribution (no-evidence-found):** No unambiguous AI-tool implementation/review attribution found in inspected documentation, source/build/license files and 4 latest returned commits. This is a bounded sample, not proof of no AI use.

Evidence: [source 1](https://github.com/amigazen/ClassAction/commits/main/) · [source 2](https://github.com/amigazen/ClassAction/blob/main/classaction.readme)

**Lineage and rights (reviewed):** Source-visible historical release; LICENSE.md preserves historical mailware restrictions and source-release provenance rather than a standard open-source grant. This is partial source restoration, not a clean all-source rebuild: object inputs remain required for resource regeneration. Documented AmigaOS 3.5/3.9 and resource.library/popupmenu/xadmaster/xfdmaster dependencies must be supplied. Historical binary distribution was mailware with noncommercial/no-alteration restrictions; source publication and preservation do not establish a standard open-source license.  Related source graph remains partial.

Evidence: [source 1](https://github.com/amigazen/ClassAction/blob/main/LICENSE.md) · [source 2](https://github.com/amigazen/ClassAction/blob/main/classaction.readme) · [source 3](https://github.com/amigazen/ClassAction)

### gtlayout.library — preserved Amiga GadTools layout toolkit

[Repository](https://github.com/amigazen/gtlayout.library)

- Source platforms: Amiga
- Target platforms: Amiga
- Source CPU: Unasserted / not applicable
- Target CPU: Unasserted / not applicable
- Source material/language: C
- Maintained language: C
- Classification: hybrid; development-tool, source-restoration, development-environment
- Build flags: all unknown (compilable, runnable, playable and byte_exact).
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Olaf Barthel’s native GadTools layout toolkit preserved with later fixes and NDK 3.2 integration. Source snapshot 6def16d9252c7bae4f5480e576b3fde76bbf9921; screened new against all 1,621 projects, sources, decisions and prior reviews.

Evidence: [source 1](https://github.com/amigazen/gtlayout.library/blob/main/README.md) · [source 2](https://github.com/amigazen/gtlayout.library/blob/main/Source/LTP_LayoutGadgets.c) · [source 3](https://github.com/amigazen/gtlayout.library)

**Classification (reviewed):** original-source Amiga GadTools layout library. LTP_LayoutGadgets.c contains the substantial native gadget layout implementation and optional BOOPSI class loading. SAS/C smakefile compiles the source suite and generates documentation/header material; current CPU setting is ANY, with old 68020 option commented out. Structured class hybrid preserves ordinary original source/port work without inventing binary decompilation.

Evidence: [source 1](https://github.com/amigazen/gtlayout.library/blob/main/README.md) · [source 2](https://github.com/amigazen/gtlayout.library/blob/main/Source/LTP_LayoutGadgets.c)

**Source architecture (no-evidence-found):** The selected historical source is C and does not independently establish a specific original ISA. A platform label is not promoted into a CPU fact.

Evidence: [source 1](https://github.com/amigazen/gtlayout.library/blob/main/README.md) · [source 2](https://github.com/amigazen/gtlayout.library/blob/main/Source/LTP_LayoutGadgets.c)

**Target architecture (no-evidence-found):** The current SAS/C recipe sets CPU=ANY with an older 68020 option commented out. No exact CPU/model is asserted; do not activate a commented build choice as a runtime requirement.

Evidence: [source 1](https://github.com/amigazen/gtlayout.library/blob/main/Source/smakefile) · [source 2](https://github.com/amigazen/gtlayout.library/blob/main/README.md)

**Build and verification (reviewed):** LTP_LayoutGadgets.c contains the substantial native gadget layout implementation and optional BOOPSI class loading. SAS/C smakefile compiles the source suite and generates documentation/header material; current CPU setting is ANY, with old 68020 option commented out. README’s future AROS/MorphOS porting intent is not an implemented runtime claim. SAS/C 6.58, NDK 3.2R4, ctags, LibDescConverter and Autodoc are documented dependencies. The source is marked freely distributable; that is not automatically equivalent to a modern permissive license. No candidate was built, run or byte-compared. All build flags remain unknown; checked-in binaries, build recipes and upstream claims are not independent tests.

Evidence: [source 1](https://github.com/amigazen/gtlayout.library/blob/main/Source/smakefile) · [source 2](https://github.com/amigazen/gtlayout.library/blob/main/README.md)

**Runtime requirements (no-evidence-found):** Classic 68k Amiga with SAS/C CPU=ANY in current makefile; do not invent a 68020 minimum from the commented option. README’s future AROS/MorphOS porting intent is not an implemented runtime claim. SAS/C 6.58, NDK 3.2R4, ctags, LibDescConverter and Autodoc are documented dependencies. The source is marked freely distributable; that is not automatically equivalent to a modern permissive license. No complete independently verified hardware matrix is asserted.

Evidence: [source 1](https://github.com/amigazen/gtlayout.library/blob/main/README.md) · [source 2](https://github.com/amigazen/gtlayout.library/blob/main/Source/smakefile)

**AI attribution (no-evidence-found):** No unambiguous AI-tool implementation/review attribution found in inspected documentation, source/build/license files and 9 latest returned commits. This is a bounded sample, not proof of no AI use.

Evidence: [source 1](https://github.com/amigazen/gtlayout.library/commits/main/) · [source 2](https://github.com/amigazen/gtlayout.library/blob/main/README.md)

**Lineage and rights (reviewed):** Historic copyright retained with freely-distributable notice; no standardized open-source license established. README’s future AROS/MorphOS porting intent is not an implemented runtime claim. SAS/C 6.58, NDK 3.2R4, ctags, LibDescConverter and Autodoc are documented dependencies. The source is marked freely distributable; that is not automatically equivalent to a modern permissive license.  Related source graph remains partial.

Evidence: [source 1](https://github.com/amigazen/gtlayout.library/blob/main/README) · [source 2](https://github.com/amigazen/gtlayout.library/blob/main/Source/LTP_LayoutGadgets.c) · [source 3](https://github.com/amigazen/gtlayout.library/blob/main/README.md) · [source 4](https://github.com/amigazen/gtlayout.library)

### iffparse and iffar — Amiga IFF inspection and archive tools

[Repository](https://github.com/amigazen/iffparse)

- Source platforms: Amiga
- Target platforms: Amiga
- Source CPU: Unasserted / not applicable
- Target CPU: m68020
- Source material/language: Unasserted / not applicable
- Maintained language: C
- Classification: tooling; binary-analysis, disk-filesystem-tool
- Build flags: all unknown (compilable, runnable, playable and byte_exact).
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** A native Amiga IFF chunk inspector and IFF CAT/LIST archiver; distinct from the operating system’s iffparse.library. Source snapshot 9e88bbf148bd15b2a8f16721e1ebadf9ea7661d8; screened new against all 1,621 projects, sources, decisions and prior reviews.

Evidence: [source 1](https://github.com/amigazen/iffparse/blob/main/Source/main.c) · [source 2](https://github.com/amigazen/iffparse/blob/main/Source/iff.c) · [source 3](https://github.com/amigazen/iffparse)

**Classification (reviewed):** native Amiga IFF inspector and archive utilities. main.c parses/displays IFF chunk metadata through Amiga iffparse.library and supports file/clipboard modes. iff.c and companion archive sources preserve an iffar lineage based on Karl Lehenbauer’s public-domain 1988 EA IFF code, ported to Amiga DOS I/O/C89. SMakefile builds iffparse and iffar as one related command suite. Structured class tooling preserves ordinary original source/port work without inventing binary decompilation.

Evidence: [source 1](https://github.com/amigazen/iffparse/blob/main/Source/main.c) · [source 2](https://github.com/amigazen/iffparse/blob/main/Source/iff.c) · [source 3](https://github.com/amigazen/iffparse/blob/main/BUILD.md)

**Source architecture (not-applicable):** The utilities inspect IFF chunks and archive data, not executable instructions; source_cpu is not applicable. This project is not Commodore iffparse.library.

Evidence: [source 1](https://github.com/amigazen/iffparse/blob/main/Source/main.c) · [source 2](https://github.com/amigazen/iffparse/blob/main/Source/iff.c) · [source 3](https://github.com/amigazen/iffparse/blob/main/BUILD.md)

**Target architecture (reviewed):** BUILD.md explicitly documents a default 68020 build target. The checked makefile/SCOPTIONS do not enforce a CPU flag, so this is documented intent rather than a demonstrated output ISA or runtime minimum.

Evidence: [source 1](https://github.com/amigazen/iffparse/blob/main/Source/SMakefile) · [source 2](https://github.com/amigazen/iffparse/blob/main/Source/SCOPTIONS) · [source 3](https://github.com/amigazen/iffparse/blob/main/Source/main.c)

**Build and verification (reviewed):** main.c parses/displays IFF chunk metadata through Amiga iffparse.library and supports file/clipboard modes. iff.c and companion archive sources preserve an iffar lineage based on Karl Lehenbauer’s public-domain 1988 EA IFF code, ported to Amiga DOS I/O/C89. SMakefile builds iffparse and iffar as one related command suite. The repository name must not be mistaken for a recreation of Commodore’s iffparse.library. BUILD.md calls the default CPU 68020, but inspected SCOPTIONS/SMakefile do not enforce an explicit CPU flag; retain this as documented intent. SAS/C 6.58 and NDK 3.2R4 are required; no independent parsing/round-trip corpus validation. No candidate was built, run or byte-compared. All build flags remain unknown; checked-in binaries, build recipes and upstream claims are not independent tests.

Evidence: [source 1](https://github.com/amigazen/iffparse/blob/main/Source/SMakefile) · [source 2](https://github.com/amigazen/iffparse/blob/main/Source/SCOPTIONS) · [source 3](https://github.com/amigazen/iffparse/blob/main/Source/main.c)

**Runtime requirements (no-evidence-found):** BUILD.md documents 68020 intent; makefile does not explicitly enforce it. Native Amiga library/DOS dependencies apply. The repository name must not be mistaken for a recreation of Commodore’s iffparse.library. BUILD.md calls the default CPU 68020, but inspected SCOPTIONS/SMakefile do not enforce an explicit CPU flag; retain this as documented intent. SAS/C 6.58 and NDK 3.2R4 are required; no independent parsing/round-trip corpus validation. No complete independently verified hardware matrix is asserted.

Evidence: [source 1](https://github.com/amigazen/iffparse/blob/main/Source/main.c) · [source 2](https://github.com/amigazen/iffparse/blob/main/Source/SMakefile) · [source 3](https://github.com/amigazen/iffparse/blob/main/Source/SCOPTIONS)

**AI attribution (no-evidence-found):** No unambiguous AI-tool implementation/review attribution found in inspected documentation, source/build/license files and 4 latest returned commits. This is a bounded sample, not proof of no AI use.

Evidence: [source 1](https://github.com/amigazen/iffparse/commits/main/) · [source 2](https://github.com/amigazen/iffparse/blob/main/Source/main.c)

**Lineage and rights (reviewed):** BSD-2-Clause original inspector code; archive support credits public-domain EA IFF/Karl Lehenbauer material. The repository name must not be mistaken for a recreation of Commodore’s iffparse.library. BUILD.md calls the default CPU 68020, but inspected SCOPTIONS/SMakefile do not enforce an explicit CPU flag; retain this as documented intent. SAS/C 6.58 and NDK 3.2R4 are required; no independent parsing/round-trip corpus validation.  Related source graph remains partial.

Evidence: [source 1](https://github.com/amigazen/iffparse/blob/main/LICENSE.md) · [source 2](https://github.com/amigazen/iffparse/blob/main/Source/main.c) · [source 3](https://github.com/amigazen/iffparse/blob/main/Source/iff.c) · [source 4](https://github.com/amigazen/iffparse)

### LZXa — Amiga LZX-compatible archive reimplementation

[Repository](https://github.com/amigazen/LZXa)

- Source platforms: Amiga
- Target platforms: Amiga, portable host
- Source CPU: Unasserted / not applicable
- Target CPU: m68000
- Source material/language: LZX archive data
- Maintained language: C
- Classification: hybrid; application, reimplementation, disk-filesystem-tool
- Build flags: all unknown (compilable, runnable, playable and byte_exact).
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** C89 LZX archive-format and command-line reimplementation targeting classic Amiga, with a portable library and host-development build. Source snapshot bd0710878617357b525e36f4f75053718b1d5c93; screened new against all 1,621 projects, sources, decisions and prior reviews.

Evidence: [source 1](https://github.com/amigazen/lzxa/blob/main/README.md) · [source 2](https://github.com/amigazen/lzxa/blob/main/Source/src/alzx_decoder.c) · [source 3](https://github.com/amigazen/LZXa)

**Classification (reviewed):** LZX-compatible archiver reimplementation. README describes an independent reimplementation of LZX 1.21; inspected code contains hash-chain LZ77 encoding, bitstream decompression and real command parsing. vbcc +aos68k_posix build emits lzx and libalzx.a; HOST=1 switches to a C89 host build for smoke testing. The decoder header explicitly says it is ported from unlzx.c logic, and README credits UnLZX2/amiga-lzx cross-checks; preserve that lineage rather than certifying clean-room independence. Structured class hybrid preserves ordinary original source/port work without inventing binary decompilation.

Evidence: [source 1](https://github.com/amigazen/lzxa/blob/main/README.md) · [source 2](https://github.com/amigazen/lzxa/blob/main/Source/src/alzx_decoder.c) · [source 3](https://github.com/amigazen/lzxa/blob/main/Source/src/alzx_lz77.c) · [source 4](https://github.com/amigazen/lzxa/blob/main/Source/cli/lzx_parse.c)

**Source architecture (not-applicable):** This reimplements archive format and command syntax, not a directly inspected original machine-code binary. The original LZX is described as 68k assembly, but no source CPU is assigned merely from a data format.

Evidence: [source 1](https://github.com/amigazen/lzxa/blob/main/README.md) · [source 2](https://github.com/amigazen/lzxa/blob/main/Source/src/alzx_decoder.c) · [source 3](https://github.com/amigazen/lzxa/blob/main/Source/src/alzx_lz77.c) · [source 4](https://github.com/amigazen/lzxa/blob/main/Source/cli/lzx_parse.c)

**Target architecture (reviewed):** README explicitly identifies the default 68000 vbcc Amiga target; the CLI banner also says 68000. The HOST=1 portable C build is separate and does not inherit this CPU.

Evidence: [source 1](https://github.com/amigazen/lzxa/blob/main/Source/Makefile) · [source 2](https://github.com/amigazen/lzxa/blob/main/README.md)

**Build and verification (reviewed):** README describes an independent reimplementation of LZX 1.21; inspected code contains hash-chain LZ77 encoding, bitstream decompression and real command parsing. vbcc +aos68k_posix build emits lzx and libalzx.a; HOST=1 switches to a C89 host build for smoke testing. The decoder header explicitly says it is ported from unlzx.c logic, and README credits UnLZX2/amiga-lzx cross-checks; preserve that lineage rather than certifying clean-room independence. README’s clean-room and tested-on-Amiga assertions are upstream claims, not independently certified facts. It decodes merged groups but writes separate streams; no LHA/LZH, multivolume or recursive directory walking. Several compatibility switches are parsed as no-ops. No archive interchange, byte equivalence, compression quality or damaged-file behavior was independently tested. No candidate was built, run or byte-compared. All build flags remain unknown; checked-in binaries, build recipes and upstream claims are not independent tests.

Evidence: [source 1](https://github.com/amigazen/lzxa/blob/main/Source/Makefile) · [source 2](https://github.com/amigazen/lzxa/blob/main/README.md)

**Runtime requirements (reviewed):** README targets 68000 and AmigaOS 2.04+; default vbcc config is +aos68k_posix with 131072-byte stack. Portable host target separate from native Amiga target. README’s clean-room and tested-on-Amiga assertions are upstream claims, not independently certified facts. It decodes merged groups but writes separate streams; no LHA/LZH, multivolume or recursive directory walking. Several compatibility switches are parsed as no-ops. No archive interchange, byte equivalence, compression quality or damaged-file behavior was independently tested. No complete independently verified hardware matrix is asserted.

Evidence: [source 1](https://github.com/amigazen/lzxa/blob/main/README.md) · [source 2](https://github.com/amigazen/lzxa/blob/main/Source/Makefile)

**AI attribution (no-evidence-found):** No unambiguous AI-tool implementation/review attribution found in inspected documentation, source/build/license files and 3 latest returned commits. This is a bounded sample, not proof of no AI use.

Evidence: [source 1](https://github.com/amigazen/lzxa/commits/main/) · [source 2](https://github.com/amigazen/lzxa/blob/main/README.md)

**Lineage and rights (reviewed):** BSD-2-Clause notices in current tree; original proprietary LZX is not bundled source. Community decompressor lineage is explicitly noted. README’s clean-room and tested-on-Amiga assertions are upstream claims, not independently certified facts. It decodes merged groups but writes separate streams; no LHA/LZH, multivolume or recursive directory walking. Several compatibility switches are parsed as no-ops. No archive interchange, byte equivalence, compression quality or damaged-file behavior was independently tested.  Related source graph remains partial.

Evidence: [source 1](https://github.com/amigazen/lzxa/blob/main/LICENSE.md) · [source 2](https://github.com/amigazen/lzxa/blob/main/Source/src/alzx_decoder.c) · [source 3](https://github.com/amigazen/lzxa/blob/main/README.md) · [source 4](https://github.com/amigazen/LZXa)

Documented profiles: [{"name": "Documented default LZXa Amiga build", "platform": "Amiga", "cpu_family": "68000 family", "min_cpu": "m68000", "os": "AmigaOS 2.04 or later", "notes": "Upstream-documented target, not independently run. Memory figures are approximate comparisons to original LZX and are not recorded as verified RAM minima. Compatibility omissions remain documented.", "evidence": ["https://github.com/amigazen/lzxa/blob/main/README.md", "https://github.com/amigazen/lzxa/blob/main/Source/Makefile"]}]

### SDL — native PowerPC AmigaOS4 multimedia port

[Repository](https://github.com/AmigaPorts/SDL)

- Source platforms: Unasserted / not applicable
- Target platforms: Amiga
- Source CPU: Unasserted / not applicable
- Target CPU: PowerPC
- Source material/language: Unasserted / not applicable
- Maintained language: C
- Classification: tooling; development-environment
- Build flags: all unknown (compilable, runnable, playable and byte_exact).
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Maintained SDL library port with native PowerPC AmigaOS4 video/audio/input backends; current main is SDL3. Source snapshot 52644a682bd5707ec457bd77dbc663fc524dfabc; screened new against all 1,621 projects, sources, decisions and prior reviews.

Evidence: [source 1](https://github.com/AmigaPorts/SDL/blob/main/README.md) · [source 2](https://github.com/AmigaPorts/SDL/blob/main/docs/README-amigaos4.md) · [source 3](https://github.com/AmigaPorts/SDL)

**Classification (reviewed):** native AmigaOS4 multimedia-library port. SDL_os4video.c creates the native AmigaOS4 SDL video device and connects display/window/event/OpenGL backend functions. Makefile.amigaos4 uses ppc-amigaos GCC and produces SDL3 static/shared libraries and preferences tooling; current docs require AmigaOS 4.1 Final Edition. The older SDL2-AmigaOS4 repository explicitly redirects here and remains lineage-only rather than a second candidate. Structured class tooling preserves ordinary original source/port work without inventing binary decompilation.

Evidence: [source 1](https://github.com/AmigaPorts/SDL/blob/main/README.md) · [source 2](https://github.com/AmigaPorts/SDL/blob/main/docs/README-amigaos4.md) · [source 3](https://github.com/AmigaPorts/SDL/blob/main/src/video/amigaos4/SDL_os4video.c)

**Source architecture (not-applicable):** SDL is portable library source, not a historical original-platform binary under analysis. No fixed source platform/CPU is inferred from upstream portability.

Evidence: [source 1](https://github.com/AmigaPorts/SDL/blob/main/README.md) · [source 2](https://github.com/AmigaPorts/SDL/blob/main/docs/README-amigaos4.md) · [source 3](https://github.com/AmigaPorts/SDL/blob/main/src/video/amigaos4/SDL_os4video.c)

**Target architecture (reviewed):** Makefile.amigaos4 explicitly selects ppc-amigaos GCC/G++ and builds SDL3 libraries. PowerPC is the native AmigaOS4 output architecture, not a 68k target or implied modern-host ISA.

Evidence: [source 1](https://github.com/AmigaPorts/SDL/blob/main/Makefile.amigaos4) · [source 2](https://github.com/AmigaPorts/SDL/blob/main/README.md)

**Build and verification (reviewed):** SDL_os4video.c creates the native AmigaOS4 SDL video device and connects display/window/event/OpenGL backend functions. Makefile.amigaos4 uses ppc-amigaos GCC and produces SDL3 static/shared libraries and preferences tooling; current docs require AmigaOS 4.1 Final Edition. The older SDL2-AmigaOS4 repository explicitly redirects here and remains lineage-only rather than a second candidate. Current AmigaOS4 docs state configure/CMake are unsupported; use the dedicated makefile, not generic SDL build assumptions. Altivec disabled; Camera/GPU/Haptic/Pen/Power/Sensor and Vulkan backends unsupported per current docs. Compositing geometry has limitations. No generic SDL host platforms are added merely because upstream SDL supports them; this candidate is the Amiga port. No candidate was built, run or byte-compared. All build flags remain unknown; checked-in binaries, build recipes and upstream claims are not independent tests.

Evidence: [source 1](https://github.com/AmigaPorts/SDL/blob/main/Makefile.amigaos4) · [source 2](https://github.com/AmigaPorts/SDL/blob/main/README.md)

**Runtime requirements (no-evidence-found):** PowerPC via ppc-amigaos toolchain; AmigaOS 4.1 Final Edition. Optional MiniGL/OGLES2/Mesa and software-renderer caveats are upstream documented. Current AmigaOS4 docs state configure/CMake are unsupported; use the dedicated makefile, not generic SDL build assumptions. Altivec disabled; Camera/GPU/Haptic/Pen/Power/Sensor and Vulkan backends unsupported per current docs. Compositing geometry has limitations. No generic SDL host platforms are added merely because upstream SDL supports them; this candidate is the Amiga port. No complete independently verified hardware matrix is asserted.

Evidence: [source 1](https://github.com/AmigaPorts/SDL/blob/main/README.md) · [source 2](https://github.com/AmigaPorts/SDL/blob/main/Makefile.amigaos4)

**AI attribution (no-evidence-found):** No unambiguous AI-tool implementation/review attribution found in inspected documentation, source/build/license files and 30 latest returned commits. This is a bounded sample, not proof of no AI use.

Evidence: [source 1](https://github.com/AmigaPorts/SDL/commits/main/) · [source 2](https://github.com/AmigaPorts/SDL/blob/main/README.md)

**Lineage and rights (reviewed):** zlib license, with source origin and altered-source marking requirements. Current AmigaOS4 docs state configure/CMake are unsupported; use the dedicated makefile, not generic SDL build assumptions. Altivec disabled; Camera/GPU/Haptic/Pen/Power/Sensor and Vulkan backends unsupported per current docs. Compositing geometry has limitations. No generic SDL host platforms are added merely because upstream SDL supports them; this candidate is the Amiga port.  Related source graph remains partial.

Evidence: [source 1](https://github.com/AmigaPorts/SDL/blob/main/LICENSE.txt) · [source 2](https://github.com/AmigaPorts/SDL/blob/main/src/video/amigaos4/SDL_os4video.c) · [source 3](https://github.com/AmigaPorts/SDL/blob/main/README.md) · [source 4](https://github.com/AmigaPorts/SDL)

### ILBMToIcon — Amiga icon-format converter

[Repository](https://github.com/AmigaPorts/ilbmtoicon)

- Source platforms: Amiga
- Target platforms: portable host, Amiga
- Source CPU: Unasserted / not applicable
- Target CPU: m68k
- Source material/language: Unasserted / not applicable
- Maintained language: C
- Classification: tooling; asset-tool, development-environment
- Build flags: all unknown (compilable, runnable, playable and byte_exact).
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** AROS-derived C tooling converts ILBM/PNG artwork to native Amiga .info/icon files, with portable host and Amiga build integration. Source snapshot f2508fbad6420bac4761f537c5392a8f5b67cfb4; screened new against all 1,621 projects, sources, decisions and prior reviews.

Evidence: [source 1](https://github.com/AmigaPorts/ILBMToIcon/blob/master/README.md) · [source 2](https://github.com/AmigaPorts/ILBMToIcon/blob/master/ilbmtoicon.c) · [source 3](https://github.com/AmigaPorts/ilbmtoicon)

**Classification (reviewed):** Amiga icon-format development converter. ilbmtoicon.c contains concrete IFF ILBM/ByteRun1/chunk and icon serialization logic with libpng/zlib dependencies. README distinguishes old-style/pre3.5 image data, appended IFF ICON data and PNG icon output. Makefile uses HOST_CC; CMake also advertises m68k-amigaos packaging and builds infoinfo as companion utility. Structured class tooling preserves ordinary original source/port work without inventing binary decompilation.

Evidence: [source 1](https://github.com/AmigaPorts/ILBMToIcon/blob/master/README.md) · [source 2](https://github.com/AmigaPorts/ILBMToIcon/blob/master/ilbmtoicon.c)

**Source architecture (not-applicable):** Input ILBM/PNG artwork and output icon data do not have an executable CPU. source_cpu is not applicable; Amiga is the real icon-format/development relationship.

Evidence: [source 1](https://github.com/AmigaPorts/ILBMToIcon/blob/master/README.md) · [source 2](https://github.com/AmigaPorts/ILBMToIcon/blob/master/ilbmtoicon.c)

**Target architecture (reviewed):** CMake packaging explicitly names m68k-amigaos. Broad m68k describes that variant only; the portable HOST_CC build has no fixed host ISA. Neither establishes a numeric CPU or OS minimum.

Evidence: [source 1](https://github.com/AmigaPorts/ILBMToIcon/blob/master/Makefile) · [source 2](https://github.com/AmigaPorts/ILBMToIcon/blob/master/CMakeLists.txt) · [source 3](https://github.com/AmigaPorts/ILBMToIcon/blob/master/README.md)

**Build and verification (reviewed):** ilbmtoicon.c contains concrete IFF ILBM/ByteRun1/chunk and icon serialization logic with libpng/zlib dependencies. README distinguishes old-style/pre3.5 image data, appended IFF ICON data and PNG icon output. Makefile uses HOST_CC; CMake also advertises m68k-amigaos packaging and builds infoinfo as companion utility. Output icon format and development target are Amiga; portable host build is not a claim of execution on every OS. No independent format compatibility or icon rendering test; input artwork rights remain the user’s responsibility. No candidate was built, run or byte-compared. All build flags remain unknown; checked-in binaries, build recipes and upstream claims are not independent tests.

Evidence: [source 1](https://github.com/AmigaPorts/ILBMToIcon/blob/master/Makefile) · [source 2](https://github.com/AmigaPorts/ILBMToIcon/blob/master/CMakeLists.txt) · [source 3](https://github.com/AmigaPorts/ILBMToIcon/blob/master/README.md)

**Runtime requirements (no-evidence-found):** Native packaging names m68k-amigaos but does not pin CPU minimum; portable HOST_CC build is CPU-independent source. Output icon format and development target are Amiga; portable host build is not a claim of execution on every OS. No independent format compatibility or icon rendering test; input artwork rights remain the user’s responsibility. No complete independently verified hardware matrix is asserted.

Evidence: [source 1](https://github.com/AmigaPorts/ILBMToIcon/blob/master/README.md) · [source 2](https://github.com/AmigaPorts/ILBMToIcon/blob/master/Makefile) · [source 3](https://github.com/AmigaPorts/ILBMToIcon/blob/master/CMakeLists.txt)

**AI attribution (no-evidence-found):** No unambiguous AI-tool implementation/review attribution found in inspected documentation, source/build/license files and 30 latest returned commits. This is a bounded sample, not proof of no AI use.

Evidence: [source 1](https://github.com/AmigaPorts/ILBMToIcon/commits/master/) · [source 2](https://github.com/AmigaPorts/ILBMToIcon/blob/master/README.md)

**Lineage and rights (reviewed):** AROS Public License 1.1 and retained AROS source notices; libpng/zlib dependency terms separate. Output icon format and development target are Amiga; portable host build is not a claim of execution on every OS. No independent format compatibility or icon rendering test; input artwork rights remain the user’s responsibility.  Related source graph remains partial.

Evidence: [source 1](https://github.com/AmigaPorts/ILBMToIcon/blob/master/LICENSE) · [source 2](https://github.com/AmigaPorts/ILBMToIcon/blob/master/ilbmtoicon.c) · [source 3](https://github.com/AmigaPorts/ILBMToIcon/blob/master/README.md) · [source 4](https://github.com/AmigaPorts/ilbmtoicon)

### CAMD I2C — native Amiga MIDI transmit driver

[Repository](https://github.com/AmigaPorts/camd-i2c-driver)

- Source platforms: Unasserted / not applicable
- Target platforms: Amiga
- Source CPU: Unasserted / not applicable
- Target CPU: m68040
- Source material/language: Unasserted / not applicable
- Maintained language: C
- Classification: subject; system-software
- Build flags: all unknown (compilable, runnable, playable and byte_exact).
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Native Amiga CAMD driver routes MIDI transmit data through i2c.library instead of a serial MIDI port. Source snapshot 31e3ba4e5c2cdb0f204496c94a032f987fe17157; screened new against all 1,621 projects, sources, decisions and prior reviews.

Evidence: [source 1](https://github.com/AmigaPorts/camd-i2c-driver/blob/main/README.md) · [source 2](https://github.com/AmigaPorts/camd-i2c-driver/blob/main/camd-i2c.driver/src/camd-i2c.c) · [source 3](https://github.com/AmigaPorts/camd-i2c-driver)

**Classification (reviewed):** native Amiga MIDI-to-I2C driver. camd-i2c.c implements CAMD callback handling and SendI2C at default address 0x42; main.c defines the resident driver entry points. CMake builds a freestanding driver with -m68040 and fetches i2c.library through CPM. Structured class subject preserves ordinary original source/port work without inventing binary decompilation.

Evidence: [source 1](https://github.com/AmigaPorts/camd-i2c-driver/blob/main/README.md) · [source 2](https://github.com/AmigaPorts/camd-i2c-driver/blob/main/camd-i2c.driver/src/camd-i2c.c) · [source 3](https://github.com/AmigaPorts/camd-i2c-driver/blob/main/camd-i2c.driver/src/main.c)

**Source architecture (not-applicable):** Original modern driver source rather than recovered legacy firmware or an analyzed original executable; source_cpu is not applicable.

Evidence: [source 1](https://github.com/AmigaPorts/camd-i2c-driver/blob/main/README.md) · [source 2](https://github.com/AmigaPorts/camd-i2c-driver/blob/main/camd-i2c.driver/src/camd-i2c.c) · [source 3](https://github.com/AmigaPorts/camd-i2c-driver/blob/main/camd-i2c.driver/src/main.c)

**Target architecture (reviewed):** camd-i2c.driver/CMakeLists.txt explicitly selects -m68040, while source callbacks bind a/d registers. The build ISA is recorded independently of untested attached hardware.

Evidence: [source 1](https://github.com/AmigaPorts/camd-i2c-driver/blob/main/CMakeLists.txt) · [source 2](https://github.com/AmigaPorts/camd-i2c-driver/blob/main/camd-i2c.driver/CMakeLists.txt) · [source 3](https://github.com/AmigaPorts/camd-i2c-driver/blob/main/README.md)

**Build and verification (reviewed):** camd-i2c.c implements CAMD callback handling and SendI2C at default address 0x42; main.c defines the resident driver entry points. CMake builds a freestanding driver with -m68040 and fetches i2c.library through CPM. Hardware and i2c.library are required; no particular attached MIDI device or working hardware configuration was independently verified. The inspected implementation establishes transmit functionality, not a complete bidirectional MIDI hardware stack. Bundled source is small but concrete; it is not a generic Amiga keyword-only hit. No candidate was built, run or byte-compared. All build flags remain unknown; checked-in binaries, build recipes and upstream claims are not independent tests.

Evidence: [source 1](https://github.com/AmigaPorts/camd-i2c-driver/blob/main/CMakeLists.txt) · [source 2](https://github.com/AmigaPorts/camd-i2c-driver/blob/main/camd-i2c.driver/CMakeLists.txt) · [source 3](https://github.com/AmigaPorts/camd-i2c-driver/blob/main/README.md)

**Runtime requirements (no-evidence-found):** Inspected build explicitly -m68040; source opens dos.library 37, camd.library and i2c.library. Hardware compatibility not tested. Hardware and i2c.library are required; no particular attached MIDI device or working hardware configuration was independently verified. The inspected implementation establishes transmit functionality, not a complete bidirectional MIDI hardware stack. Bundled source is small but concrete; it is not a generic Amiga keyword-only hit. No complete independently verified hardware matrix is asserted.

Evidence: [source 1](https://github.com/AmigaPorts/camd-i2c-driver/blob/main/README.md) · [source 2](https://github.com/AmigaPorts/camd-i2c-driver/blob/main/CMakeLists.txt) · [source 3](https://github.com/AmigaPorts/camd-i2c-driver/blob/main/camd-i2c.driver/CMakeLists.txt)

**AI attribution (no-evidence-found):** No unambiguous AI-tool implementation/review attribution found in inspected documentation, source/build/license files and 9 latest returned commits. This is a bounded sample, not proof of no AI use.

Evidence: [source 1](https://github.com/AmigaPorts/camd-i2c-driver/commits/main/) · [source 2](https://github.com/AmigaPorts/camd-i2c-driver/blob/main/README.md)

**Lineage and rights (reviewed):** MPL-2.0 repository and source notices. Hardware and i2c.library are required; no particular attached MIDI device or working hardware configuration was independently verified. The inspected implementation establishes transmit functionality, not a complete bidirectional MIDI hardware stack. Bundled source is small but concrete; it is not a generic Amiga keyword-only hit.  Related source graph remains partial.

Evidence: [source 1](https://github.com/AmigaPorts/camd-i2c-driver/blob/main/LICENSE) · [source 2](https://github.com/AmigaPorts/camd-i2c-driver/blob/main/camd-i2c.driver/src/camd-i2c.c) · [source 3](https://github.com/AmigaPorts/camd-i2c-driver/blob/main/README.md) · [source 4](https://github.com/AmigaPorts/camd-i2c-driver)

### Poseidon USB — standalone AmigaOS3 source restoration

[Repository](https://github.com/BlitterStudio/poseidon-usb)

- Source platforms: Amiga
- Target platforms: Amiga
- Source CPU: Unasserted / not applicable
- Target CPU: m68k
- Source material/language: C
- Maintained language: C
- Classification: subject; system-software, source-restoration
- Build flags: all unknown (compilable, runnable, playable and byte_exact).
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Chris Hodges’s Poseidon USB stack extracted from AROS with substantive native AmigaOS 3 startup/build/packaging work. Source snapshot bc56025c33345739963e65ce8253f747be9ab6bd; screened new against all 1,621 projects, sources, decisions and prior reviews.

Evidence: [source 1](https://github.com/BlitterStudio/poseidon-usb/blob/main/README.md) · [source 2](https://github.com/BlitterStudio/poseidon-usb/blob/main/src/poseidon/poseidon.library.c) · [source 3](https://github.com/BlitterStudio/poseidon-usb)

**Classification (reviewed):** original-source USB stack extraction and native OS3 restoration. Main library source contains the full USB stack implementation; OS3 class_startup.c provides resident startup/open/close/expunge glue. upstream/aros.json pins the imported AROS commit and relocation map; src/LEGAL records Hodges’s 2009 AROS Public License release. Makefile builds OS3 library, class modules, GUI/tools and release packaging from source; components stay one stack candidate. Structured class subject preserves ordinary original source/port work without inventing binary decompilation.

Evidence: [source 1](https://github.com/BlitterStudio/poseidon-usb/blob/main/README.md) · [source 2](https://github.com/BlitterStudio/poseidon-usb/blob/main/src/poseidon/poseidon.library.c) · [source 3](https://github.com/BlitterStudio/poseidon-usb/blob/main/support/os3/class_startup.c) · [source 4](https://github.com/BlitterStudio/poseidon-usb/blob/main/upstream/aros.json)

**Source architecture (no-evidence-found):** Original Poseidon C source was imported through AROS. Its original source and later portable AROS maintenance are not reduced to a CPU inferred from the name; source_cpu remains unasserted.

Evidence: [source 1](https://github.com/BlitterStudio/poseidon-usb/blob/main/README.md) · [source 2](https://github.com/BlitterStudio/poseidon-usb/blob/main/src/poseidon/poseidon.library.c) · [source 3](https://github.com/BlitterStudio/poseidon-usb/blob/main/support/os3/class_startup.c) · [source 4](https://github.com/BlitterStudio/poseidon-usb/blob/main/upstream/aros.json)

**Target architecture (reviewed):** OS3 Makefile uses -m68020-60 -mtune=68030 and class startup binds d0/a0/a6. This establishes the native m68k OS3 build family; tuning does not mean a universal 68030 minimum.

Evidence: [source 1](https://github.com/BlitterStudio/poseidon-usb/blob/main/Makefile) · [source 2](https://github.com/BlitterStudio/poseidon-usb/blob/main/README.md)

**Build and verification (reviewed):** Main library source contains the full USB stack implementation; OS3 class_startup.c provides resident startup/open/close/expunge glue. upstream/aros.json pins the imported AROS commit and relocation map; src/LEGAL records Hodges’s 2009 AROS Public License release. Makefile builds OS3 library, class modules, GUI/tools and release packaging from source; components stay one stack candidate. Upstream explicitly says linked OS3 binaries still need real runtime validation, despite build checks. AROS hardware-controller code is retained but not staged for OS3; old closed E3B drivers, PsdLoadModule/PsdRestart and other unreleased pieces are absent. A complete compatible USB setup remains required; this is not a tested drop-in complete historical release. No candidate was built, run or byte-compared. All build flags remain unknown; checked-in binaries, build recipes and upstream claims are not independent tests.

Evidence: [source 1](https://github.com/BlitterStudio/poseidon-usb/blob/main/Makefile) · [source 2](https://github.com/BlitterStudio/poseidon-usb/blob/main/README.md)

**Runtime requirements (no-evidence-found):** OS3 makefile uses -m68020-60 -mtune=68030. Native AmigaOS 3 target; actual controller/hardware and runtime compatibility unverified. Upstream explicitly says linked OS3 binaries still need real runtime validation, despite build checks. AROS hardware-controller code is retained but not staged for OS3; old closed E3B drivers, PsdLoadModule/PsdRestart and other unreleased pieces are absent. A complete compatible USB setup remains required; this is not a tested drop-in complete historical release. No complete independently verified hardware matrix is asserted.

Evidence: [source 1](https://github.com/BlitterStudio/poseidon-usb/blob/main/README.md) · [source 2](https://github.com/BlitterStudio/poseidon-usb/blob/main/Makefile)

**AI attribution (no-evidence-found):** No unambiguous AI-tool implementation/review attribution found in inspected documentation, source/build/license files and 9 latest returned commits. This is a bounded sample, not proof of no AI use.

Evidence: [source 1](https://github.com/BlitterStudio/poseidon-usb/commits/main/) · [source 2](https://github.com/BlitterStudio/poseidon-usb/blob/main/README.md)

**Lineage and rights (reviewed):** AROS Public License 1.1, with explicit author source-release declaration; artworks/translations retain credit/provenance. Upstream explicitly says linked OS3 binaries still need real runtime validation, despite build checks. AROS hardware-controller code is retained but not staged for OS3; old closed E3B drivers, PsdLoadModule/PsdRestart and other unreleased pieces are absent. A complete compatible USB setup remains required; this is not a tested drop-in complete historical release.  Related source graph remains partial.

Evidence: [source 1](https://github.com/BlitterStudio/poseidon-usb/blob/main/LICENSE) · [source 2](https://github.com/BlitterStudio/poseidon-usb/blob/main/src/LEGAL) · [source 3](https://github.com/BlitterStudio/poseidon-usb/blob/main/README.md) · [source 4](https://github.com/BlitterStudio/poseidon-usb)

### ZZ9000 — native AmigaOS driver suite

[Repository](https://github.com/BlitterStudio/zz9000-drivers)

- Source platforms: Unasserted / not applicable
- Target platforms: Amiga
- Source CPU: Unasserted / not applicable
- Target CPU: m68020
- Source material/language: Unasserted / not applicable
- Maintained language: C
- Classification: subject; system-software
- Build flags: all unknown (compilable, runnable, playable and byte_exact).
- AI: Codex

**Identity and scope (reviewed):** Independent continuation of MNT’s ZZ9000 Amiga-side driver suite, with RTG, network/audio/USB/SD and native control utilities. Source snapshot 701ee6e9bf96f19e302d874b166e22e06952e0b6; screened new against all 1,621 projects, sources, decisions and prior reviews.

Evidence: [source 1](https://github.com/BlitterStudio/zz9000-drivers/blob/master/README.md) · [source 2](https://github.com/BlitterStudio/zz9000-drivers/blob/master/net/device.c) · [source 3](https://github.com/BlitterStudio/zz9000-drivers)

**Classification (reviewed):** native Amiga hardware-driver continuation. Network device.c implements native SANA-II Amiga driver dispatch and hardware access; rtg/mntgfx-gcc.c implements graphics-card integration. README identifies the original MNT source and independent fork status, with firmware and ARM-side logic in separate repositories. Top-level build invokes pinned Amiga toolchain workflows; net/Makefile sets68020 and includes host-side test targets elsewhere in the suite. A reviewed code-fix commit explicitly credits Codex review; attribution is limited to review assistance. Structured class subject preserves ordinary original source/port work without inventing binary decompilation.

Evidence: [source 1](https://github.com/BlitterStudio/zz9000-drivers/blob/master/README.md) · [source 2](https://github.com/BlitterStudio/zz9000-drivers/blob/master/net/device.c) · [source 3](https://github.com/BlitterStudio/zz9000-drivers/blob/master/rtg/mntgfx-gcc.c)

**Source architecture (not-applicable):** Maintained Amiga-side hardware driver source, not a reconstruction of a historical original binary. No source CPU is inferred from the modern hardware family.

Evidence: [source 1](https://github.com/BlitterStudio/zz9000-drivers/blob/master/README.md) · [source 2](https://github.com/BlitterStudio/zz9000-drivers/blob/master/net/device.c) · [source 3](https://github.com/BlitterStudio/zz9000-drivers/blob/master/rtg/mntgfx-gcc.c)

**Target architecture (reviewed):** net/Makefile explicitly defaults to CPU=68020 and soft float. This records the inspected native network-driver target; other suite components can vary. The board ARM/FPGA firmware lives elsewhere and is not the Amiga driver CPU.

Evidence: [source 1](https://github.com/BlitterStudio/zz9000-drivers/blob/master/Makefile) · [source 2](https://github.com/BlitterStudio/zz9000-drivers/blob/master/net/Makefile) · [source 3](https://github.com/BlitterStudio/zz9000-drivers/blob/master/README.md)

**Build and verification (reviewed):** Network device.c implements native SANA-II Amiga driver dispatch and hardware access; rtg/mntgfx-gcc.c implements graphics-card integration. README identifies the original MNT source and independent fork status, with firmware and ARM-side logic in separate repositories. Top-level build invokes pinned Amiga toolchain workflows; net/Makefile sets68020 and includes host-side test targets elsewhere in the suite. A reviewed code-fix commit explicitly credits Codex review; attribution is limited to review assistance. Requires ZZ9000 ZorroII/III hardware; ZZ9000AX audio and Picasso96/USB/network dependencies vary by component. Matched firmware/bitstream/SDK versions matter, especially ZorroII memory-layout negotiation; driver source alone does not provide a complete setup. The board’s ARM coprocessors are not the CPU executing the Amiga-side network driver; retain separate roles. No independent hardware/runtime/test execution; original MNT lineage is one family, not an extra project count. No candidate was built, run or byte-compared. All build flags remain unknown; checked-in binaries, build recipes and upstream claims are not independent tests.

Evidence: [source 1](https://github.com/BlitterStudio/zz9000-drivers/blob/master/Makefile) · [source 2](https://github.com/BlitterStudio/zz9000-drivers/blob/master/net/Makefile) · [source 3](https://github.com/BlitterStudio/zz9000-drivers/blob/master/README.md)

**Runtime requirements (no-evidence-found):** Amiga-side m68k toolchain; inspected network component default 68020 and soft float. Board FPGA/ARM firmware separate from host driver CPU. Requires ZZ9000 ZorroII/III hardware; ZZ9000AX audio and Picasso96/USB/network dependencies vary by component. Matched firmware/bitstream/SDK versions matter, especially ZorroII memory-layout negotiation; driver source alone does not provide a complete setup. The board’s ARM coprocessors are not the CPU executing the Amiga-side network driver; retain separate roles. No independent hardware/runtime/test execution; original MNT lineage is one family, not an extra project count. No complete independently verified hardware matrix is asserted.

Evidence: [source 1](https://github.com/BlitterStudio/zz9000-drivers/blob/master/README.md) · [source 2](https://github.com/BlitterStudio/zz9000-drivers/blob/master/Makefile) · [source 3](https://github.com/BlitterStudio/zz9000-drivers/blob/master/net/Makefile)

**AI attribution (reviewed):** Multiple sampled commits explicitly credit Codex review. Commit 6944da9 fixes a concrete ZZDiag control-flow problem identified in that review; no broad claim that all driver code is AI-generated. Role: code review. No broad AI-generated-code claim.

Evidence: [source 1](https://github.com/BlitterStudio/zz9000-drivers/commit/6944da9d4777a96192b64cd1f910ce80839ad829) · [source 2](https://github.com/BlitterStudio/zz9000-drivers/blob/master/README.md)

**Lineage and rights (reviewed):** GPL-3.0-or-later for driver tree with retained MNT/contributor and third-party notices; external payload licenses remain separate. Requires ZZ9000 ZorroII/III hardware; ZZ9000AX audio and Picasso96/USB/network dependencies vary by component. Matched firmware/bitstream/SDK versions matter, especially ZorroII memory-layout negotiation; driver source alone does not provide a complete setup. The board’s ARM coprocessors are not the CPU executing the Amiga-side network driver; retain separate roles. No independent hardware/runtime/test execution; original MNT lineage is one family, not an extra project count.  Related source graph remains partial.

Evidence: [source 1](https://github.com/BlitterStudio/zz9000-drivers/blob/master/LICENSE) · [source 2](https://github.com/BlitterStudio/zz9000-drivers/blob/master/net/device.c) · [source 3](https://github.com/BlitterStudio/zz9000-drivers/blob/master/README.md) · [source 4](https://github.com/BlitterStudio/zz9000-drivers)

### ProTrackerTools — Amiga MOD optimization and conversion

[Repository](https://github.com/djh0ffman/ProTrackerTools)

- Source platforms: Amiga
- Target platforms: Windows
- Source CPU: Unasserted / not applicable
- Target CPU: Unasserted / not applicable
- Source material/language: Unasserted / not applicable
- Maintained language: C#
- Classification: tooling; asset-tool, development-environment
- Build flags: all unknown (compilable, runnable, playable and byte_exact).
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** C# library and Windows OptiMod editor optimize and serialize native Amiga ProTracker modules, including Player 6.1 conversion. Source snapshot eb8089abfa53215684ab1920b0ada463e62451a4; screened new against all 1,621 projects, sources, decisions and prior reviews.

Evidence: [source 1](https://github.com/djh0ffman/ProTrackerTools/blob/master/README.md) · [source 2](https://github.com/djh0ffman/ProTrackerTools/blob/master/PTSerializer/Serializer.cs) · [source 3](https://github.com/djh0ffman/ProTrackerTools)

**Classification (reviewed):** Amiga MOD development and serialization toolkit. Serializer.cs parses sample headers, song order, four-channel pattern data and M.K./M!K! signatures, and serializes modules back. P61Convert.cs contains actual sample/pattern cleanup and P61 packing; OptiMod is the same toolkit’s frontend, not a separate entry. Projects target .NET Framework 4.8, with Windows Forms frontend and AnyCPU managed build. Structured class tooling preserves ordinary original source/port work without inventing binary decompilation.

Evidence: [source 1](https://github.com/djh0ffman/ProTrackerTools/blob/master/README.md) · [source 2](https://github.com/djh0ffman/ProTrackerTools/blob/master/PTSerializer/Serializer.cs) · [source 3](https://github.com/djh0ffman/ProTrackerTools/blob/master/PTSerializer/P61Convert.cs)

**Source architecture (not-applicable):** Source material is ProTracker MOD music data, not 68000 instructions. source_cpu is not applicable.

Evidence: [source 1](https://github.com/djh0ffman/ProTrackerTools/blob/master/README.md) · [source 2](https://github.com/djh0ffman/ProTrackerTools/blob/master/PTSerializer/Serializer.cs) · [source 3](https://github.com/djh0ffman/ProTrackerTools/blob/master/PTSerializer/P61Convert.cs)

**Target architecture (no-evidence-found):** Managed AnyCPU/.NET Framework 4.8 code and Windows Forms establish the Windows host, not a hardware ISA. Amiga is the music-format/development ecosystem.

Evidence: [source 1](https://github.com/djh0ffman/ProTrackerTools/blob/master/PTSerializer/ProTrackerTools.csproj) · [source 2](https://github.com/djh0ffman/ProTrackerTools/blob/master/OptiMod/OptiMod.csproj) · [source 3](https://github.com/djh0ffman/ProTrackerTools/blob/master/README.md)

**Build and verification (reviewed):** Serializer.cs parses sample headers, song order, four-channel pattern data and M.K./M!K! signatures, and serializes modules back. P61Convert.cs contains actual sample/pattern cleanup and P61 packing; OptiMod is the same toolkit’s frontend, not a separate entry. Projects target .NET Framework 4.8, with Windows Forms frontend and AnyCPU managed build. Amiga is the module-format/development relationship; Windows is the inspected executable host. No standalone license in the complete tree or explicit license grant in inspected source/README; source visibility is not an open-source permission. No byte-exact round-trip, playback or P61 runtime compatibility was tested; input music/sample rights separate. No candidate was built, run or byte-compared. All build flags remain unknown; checked-in binaries, build recipes and upstream claims are not independent tests.

Evidence: [source 1](https://github.com/djh0ffman/ProTrackerTools/blob/master/PTSerializer/ProTrackerTools.csproj) · [source 2](https://github.com/djh0ffman/ProTrackerTools/blob/master/OptiMod/OptiMod.csproj) · [source 3](https://github.com/djh0ffman/ProTrackerTools/blob/master/README.md)

**Runtime requirements (no-evidence-found):** Managed AnyCPU/.NET Framework 4.8 on Windows; not native68000 code. Amiga is the module-format/development relationship; Windows is the inspected executable host. No standalone license in the complete tree or explicit license grant in inspected source/README; source visibility is not an open-source permission. No byte-exact round-trip, playback or P61 runtime compatibility was tested; input music/sample rights separate. No complete independently verified hardware matrix is asserted.

Evidence: [source 1](https://github.com/djh0ffman/ProTrackerTools/blob/master/README.md) · [source 2](https://github.com/djh0ffman/ProTrackerTools/blob/master/PTSerializer/ProTrackerTools.csproj) · [source 3](https://github.com/djh0ffman/ProTrackerTools/blob/master/OptiMod/OptiMod.csproj)

**AI attribution (no-evidence-found):** No unambiguous AI-tool implementation/review attribution found in inspected documentation, source/build/license files and 27 latest returned commits. This is a bounded sample, not proof of no AI use.

Evidence: [source 1](https://github.com/djh0ffman/ProTrackerTools/commits/master/) · [source 2](https://github.com/djh0ffman/ProTrackerTools/blob/master/README.md)

**Lineage and rights (reviewed):** No explicit project-wide license located in tree/inspected files. Amiga is the module-format/development relationship; Windows is the inspected executable host. No standalone license in the complete tree or explicit license grant in inspected source/README; source visibility is not an open-source permission. No byte-exact round-trip, playback or P61 runtime compatibility was tested; input music/sample rights separate.  Related source graph remains partial.

Evidence: [source 1](https://github.com/djh0ffman/ProTrackerTools/blob/master/README.md) · [source 2](https://github.com/djh0ffman/ProTrackerTools)

### wav2amiga — ProTracker sample preparation

[Repository](https://github.com/djh0ffman/Wav2Amiga)

- Source platforms: Unasserted / not applicable
- Target platforms: Windows
- Source CPU: Unasserted / not applicable
- Target CPU: Unasserted / not applicable
- Source material/language: Unasserted / not applicable
- Maintained language: C#
- Classification: tooling; asset-tool
- Build flags: all unknown (compilable, runnable, playable and byte_exact).
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Windows C# sample converter prepares eight-bit PCM at ProTracker note rates, with single/stacked/aligned sample modes. Source snapshot 7d2ca60d38e4ab5d2eb4ba763f22b32f9b1b3d52; screened new against all 1,621 projects, sources, decisions and prior reviews.

Evidence: [source 1](https://github.com/djh0ffman/wav2amiga/blob/main/README.md) · [source 2](https://github.com/djh0ffman/wav2amiga/blob/main/Wav2Amiga/MainForm.cs) · [source 3](https://github.com/djh0ffman/Wav2Amiga)

**Classification (reviewed):** ProTracker sample preparation tool. MainForm.cs resamples via NAudio MediaFoundation, extracts the high byte of 16-bit PCM and writes raw sample files. Stacked modes align samples to 256-byte ProTracker offset boundaries; csproj targets .NET Framework 4.8/Windows Forms. Structured class tooling preserves ordinary original source/port work without inventing binary decompilation.

Evidence: [source 1](https://github.com/djh0ffman/wav2amiga/blob/main/README.md) · [source 2](https://github.com/djh0ffman/wav2amiga/blob/main/Wav2Amiga/MainForm.cs)

**Source architecture (not-applicable):** Inputs are WAV audio; the purpose is preparing Amiga ProTracker sample data. Neither input nor output data is an original CPU binary.

Evidence: [source 1](https://github.com/djh0ffman/wav2amiga/blob/main/README.md) · [source 2](https://github.com/djh0ffman/wav2amiga/blob/main/Wav2Amiga/MainForm.cs)

**Target architecture (no-evidence-found):** Windows Forms/.NET Framework 4.8 and MediaFoundation are explicit host dependencies. AnyCPU is managed-code configuration, not a native ISA; the output sample target does not turn the program into Amiga code.

Evidence: [source 1](https://github.com/djh0ffman/wav2amiga/blob/main/Wav2Amiga/Wav2Amiga.csproj) · [source 2](https://github.com/djh0ffman/wav2amiga/blob/main/Wav2Amiga/packages.config) · [source 3](https://github.com/djh0ffman/wav2amiga/blob/main/README.md)

**Build and verification (reviewed):** MainForm.cs resamples via NAudio MediaFoundation, extracts the high byte of 16-bit PCM and writes raw sample files. Stacked modes align samples to 256-byte ProTracker offset boundaries; csproj targets .NET Framework 4.8/Windows Forms. This prepares Amiga tracker assets on Windows; it is not an Amiga-native executable. The resampling code retains the source channel count despite a monoSource variable name; do not promise automatic stereo-to-mono conversion. No license file in the tree; NAudio/Newtonsoft are external dependencies with separate terms. No output playback or sample fidelity testing. No candidate was built, run or byte-compared. All build flags remain unknown; checked-in binaries, build recipes and upstream claims are not independent tests.

Evidence: [source 1](https://github.com/djh0ffman/wav2amiga/blob/main/Wav2Amiga/Wav2Amiga.csproj) · [source 2](https://github.com/djh0ffman/wav2amiga/blob/main/Wav2Amiga/packages.config) · [source 3](https://github.com/djh0ffman/wav2amiga/blob/main/README.md)

**Runtime requirements (no-evidence-found):** Managed AnyCPU/.NET Framework 4.8/Windows MediaFoundation runtime; output targets ProTracker data use. This prepares Amiga tracker assets on Windows; it is not an Amiga-native executable. The resampling code retains the source channel count despite a monoSource variable name; do not promise automatic stereo-to-mono conversion. No license file in the tree; NAudio/Newtonsoft are external dependencies with separate terms. No output playback or sample fidelity testing. No complete independently verified hardware matrix is asserted.

Evidence: [source 1](https://github.com/djh0ffman/wav2amiga/blob/main/README.md) · [source 2](https://github.com/djh0ffman/wav2amiga/blob/main/Wav2Amiga/Wav2Amiga.csproj) · [source 3](https://github.com/djh0ffman/wav2amiga/blob/main/Wav2Amiga/packages.config)

**AI attribution (no-evidence-found):** No unambiguous AI-tool implementation/review attribution found in inspected documentation, source/build/license files and 9 latest returned commits. This is a bounded sample, not proof of no AI use.

Evidence: [source 1](https://github.com/djh0ffman/wav2amiga/commits/main/) · [source 2](https://github.com/djh0ffman/wav2amiga/blob/main/README.md)

**Lineage and rights (reviewed):** No explicit project-wide license located; third-party library and input sample rights remain separate. This prepares Amiga tracker assets on Windows; it is not an Amiga-native executable. The resampling code retains the source channel count despite a monoSource variable name; do not promise automatic stereo-to-mono conversion. No license file in the tree; NAudio/Newtonsoft are external dependencies with separate terms. No output playback or sample fidelity testing.  Related source graph remains partial.

Evidence: [source 1](https://github.com/djh0ffman/wav2amiga/blob/main/README.md) · [source 2](https://github.com/djh0ffman/Wav2Amiga)

### TTE Track Loaders — native Amiga floppy loading

[Repository](https://github.com/djh0ffman/TTETrackLoaders)

- Source platforms: Unasserted / not applicable
- Target platforms: Amiga
- Source CPU: Unasserted / not applicable
- Target CPU: m68000
- Source material/language: Unasserted / not applicable
- Maintained language: m68k assembly
- Classification: tooling; disk-filesystem-tool, development-environment
- Build flags: all unknown (compilable, runnable, playable and byte_exact).
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Single- and double-buffered 68000 Amiga disk loaders with direct hardware access and integrated ZX0 decompression. Source snapshot cffb857aacf356ef34a3aa194e419088eb1d1196; screened new against all 1,621 projects, sources, decisions and prior reviews.

Evidence: [source 1](https://github.com/djh0ffman/TTETrackLoaders/blob/main/README.md) · [source 2](https://github.com/djh0ffman/TTETrackLoaders/blob/main/ttetrack.asm) · [source 3](https://github.com/djh0ffman/TTETrackLoaders)

**Classification (reviewed):** native Amiga floppy-loader source suite. ttetrack.asm and tteturbo.asm implement CIA/custom-chip floppy DMA, MFM decoding, sector checks and retries. Turbo uses two MFM buffers so decompression can overlap disk DMA; both contain a 68000 ZX0 decompressor and credit Frank Wille loader lineage. Structured class tooling preserves ordinary original source/port work without inventing binary decompilation.

Evidence: [source 1](https://github.com/djh0ffman/TTETrackLoaders/blob/main/README.md) · [source 2](https://github.com/djh0ffman/TTETrackLoaders/blob/main/ttetrack.asm) · [source 3](https://github.com/djh0ffman/TTETrackLoaders/blob/main/tteturbo.asm)

**Source architecture (not-applicable):** Original loader source with credited Frank Wille and ZX0 lineage rather than a directly disassembled historical subject; source_cpu is not applicable.

Evidence: [source 1](https://github.com/djh0ffman/TTETrackLoaders/blob/main/README.md) · [source 2](https://github.com/djh0ffman/TTETrackLoaders/blob/main/ttetrack.asm) · [source 3](https://github.com/djh0ffman/TTETrackLoaders/blob/main/tteturbo.asm)

**Target architecture (reviewed):** README explicitly identifies 68000 assembly and both implementations contain native d/a-register disk-DMA/MFM logic plus an unzx0_68000 decompressor. No accelerator/cache or video-standard compatibility is inferred.

Evidence: [source 1](https://github.com/djh0ffman/TTETrackLoaders/blob/main/README.md)

**Build and verification (reviewed):** ttetrack.asm and tteturbo.asm implement CIA/custom-chip floppy DMA, MFM decoding, sector checks and retries. Turbo uses two MFM buffers so decompression can overlap disk DMA; both contain a 68000 ZX0 decompressor and credit Frank Wille loader lineage. Headers document drive-number selection as not implemented. External hardware include files such as hw.i/intbits.i/cia.i and a suitable assembler/integration harness are required; no standalone makefile is present. Embedded ZX0 code has a zlib-style grant, but no clear top-level license covering the entire loader suite was found. No PAL/NTSC, accelerator/cache or physical floppy behavior was independently verified. No candidate was built, run or byte-compared. All build flags remain unknown; checked-in binaries, build recipes and upstream claims are not independent tests.

Evidence: [source 1](https://github.com/djh0ffman/TTETrackLoaders/blob/main/README.md)

**Runtime requirements (no-evidence-found):** Explicit68000 assembly and Amiga CIA/custom disk hardware; host development tool not confused with target CPU. Headers document drive-number selection as not implemented. External hardware include files such as hw.i/intbits.i/cia.i and a suitable assembler/integration harness are required; no standalone makefile is present. Embedded ZX0 code has a zlib-style grant, but no clear top-level license covering the entire loader suite was found. No PAL/NTSC, accelerator/cache or physical floppy behavior was independently verified. No complete independently verified hardware matrix is asserted.

Evidence: [source 1](https://github.com/djh0ffman/TTETrackLoaders/blob/main/README.md)

**AI attribution (no-evidence-found):** No unambiguous AI-tool implementation/review attribution found in inspected documentation, source/build/license files and 6 latest returned commits. This is a bounded sample, not proof of no AI use.

Evidence: [source 1](https://github.com/djh0ffman/TTETrackLoaders/commits/main/) · [source 2](https://github.com/djh0ffman/TTETrackLoaders/blob/main/README.md)

**Lineage and rights (reviewed):** Embedded ZX0 decompressor has zlib-style terms; whole-suite license unresolved, with Frank Wille lineage credit. Headers document drive-number selection as not implemented. External hardware include files such as hw.i/intbits.i/cia.i and a suitable assembler/integration harness are required; no standalone makefile is present. Embedded ZX0 code has a zlib-style grant, but no clear top-level license covering the entire loader suite was found. No PAL/NTSC, accelerator/cache or physical floppy behavior was independently verified.  Related source graph remains partial.

Evidence: [source 1](https://github.com/djh0ffman/TTETrackLoaders/blob/main/ttetrack.asm) · [source 2](https://github.com/djh0ffman/TTETrackLoaders/blob/main/tteturbo.asm) · [source 3](https://github.com/djh0ffman/TTETrackLoaders/blob/main/README.md) · [source 4](https://github.com/djh0ffman/TTETrackLoaders)

### TTE Disk Builder — Amiga bootable ADF authoring

[Repository](https://github.com/djh0ffman/TTEDiskBuilder)

- Source platforms: Unasserted / not applicable
- Target platforms: Windows
- Source CPU: Unasserted / not applicable
- Target CPU: Unasserted / not applicable
- Source material/language: Unasserted / not applicable
- Maintained language: C#
- Classification: tooling; disk-filesystem-tool, development-environment
- Build flags: all unknown (compilable, runnable, playable and byte_exact).
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Original C# host tool builds custom bootable Amiga ADF images from a JSON file manifest and supplied bootblock. Source snapshot e47a5b2825ab689c3ce18aad5b30b9cb02da1b4f; screened new against all 1,621 projects, sources, decisions and prior reviews.

Evidence: [source 1](https://github.com/djh0ffman/TTEDiskBuilder/blob/main/README.md) · [source 2](https://github.com/djh0ffman/TTEDiskBuilder/blob/main/Program.cs) · [source 3](https://github.com/djh0ffman/TTEDiskBuilder)

**Classification (reviewed):** Amiga bootable disk-image development utility. Program.cs writes a 1024-byte bootblock, 16-byte file-table entries at 0x400, packed payloads and pads to 0xDC000 bytes; it calculates the boot checksum. It invokes external Windows packers and targets .NET Framework 4.7.2; input bootblock and selected compressor executables are separate prerequisites. Existing decision markyturtle-ttedisbuilder-netcore-port excludes a .NET Core port as separate lineage. This original upstream utility is not currently a project and does not reverse that fork exclusion. Structured class tooling preserves ordinary original source/port work without inventing binary decompilation.

Evidence: [source 1](https://github.com/djh0ffman/TTEDiskBuilder/blob/main/README.md) · [source 2](https://github.com/djh0ffman/TTEDiskBuilder/blob/main/Program.cs)

**Source architecture (not-applicable):** The tool consumes a manifest, opaque bootblock and packed data to create an Amiga disk image. Those inputs do not establish an analyzed source CPU.

Evidence: [source 1](https://github.com/djh0ffman/TTEDiskBuilder/blob/main/README.md) · [source 2](https://github.com/djh0ffman/TTEDiskBuilder/blob/main/Program.cs)

**Target architecture (no-evidence-found):** The .NET Framework 4.7.2 AnyCPU program invokes Windows .exe packers. Windows is the development host; generated Amiga disk data is not the executable CPU target.

Evidence: [source 1](https://github.com/djh0ffman/TTEDiskBuilder/blob/main/TTEDiskBuilder.csproj) · [source 2](https://github.com/djh0ffman/TTEDiskBuilder/blob/main/packages.config) · [source 3](https://github.com/djh0ffman/TTEDiskBuilder/blob/main/README.md)

**Build and verification (reviewed):** Program.cs writes a 1024-byte bootblock, 16-byte file-table entries at 0x400, packed payloads and pads to 0xDC000 bytes; it calculates the boot checksum. It invokes external Windows packers and targets .NET Framework 4.7.2; input bootblock and selected compressor executables are separate prerequisites. Existing decision markyturtle-ttedisbuilder-netcore-port excludes a .NET Core port as separate lineage. This original upstream utility is not currently a project and does not reverse that fork exclusion. No original bootblock is supplied; a compatible 1024-byte bootblock and disk manifest are required. Source invokes shrinkler.exe, salvador.exe, zopfli.exe and optional other packers; tool availability is not verified. No explicit project-wide license in tree; bootblock/data and compressor rights are separate. No image boot, loader interoperability or output checksum test performed. No candidate was built, run or byte-compared. All build flags remain unknown; checked-in binaries, build recipes and upstream claims are not independent tests.

Evidence: [source 1](https://github.com/djh0ffman/TTEDiskBuilder/blob/main/TTEDiskBuilder.csproj) · [source 2](https://github.com/djh0ffman/TTEDiskBuilder/blob/main/packages.config) · [source 3](https://github.com/djh0ffman/TTEDiskBuilder/blob/main/README.md)

**Runtime requirements (no-evidence-found):** Managed AnyCPU/.NET Framework 4.7.2 Windows host; creates Amiga disk data, not an Amiga executable itself. No original bootblock is supplied; a compatible 1024-byte bootblock and disk manifest are required. Source invokes shrinkler.exe, salvador.exe, zopfli.exe and optional other packers; tool availability is not verified. No explicit project-wide license in tree; bootblock/data and compressor rights are separate. No image boot, loader interoperability or output checksum test performed. No complete independently verified hardware matrix is asserted.

Evidence: [source 1](https://github.com/djh0ffman/TTEDiskBuilder/blob/main/README.md) · [source 2](https://github.com/djh0ffman/TTEDiskBuilder/blob/main/TTEDiskBuilder.csproj) · [source 3](https://github.com/djh0ffman/TTEDiskBuilder/blob/main/packages.config)

**AI attribution (no-evidence-found):** No unambiguous AI-tool implementation/review attribution found in inspected documentation, source/build/license files and 13 latest returned commits. This is a bounded sample, not proof of no AI use.

Evidence: [source 1](https://github.com/djh0ffman/TTEDiskBuilder/commits/main/) · [source 2](https://github.com/djh0ffman/TTEDiskBuilder/blob/main/README.md)

**Lineage and rights (reviewed):** No explicit project-wide license located in tree/inspected files. No original bootblock is supplied; a compatible 1024-byte bootblock and disk manifest are required. Source invokes shrinkler.exe, salvador.exe, zopfli.exe and optional other packers; tool availability is not verified. No explicit project-wide license in tree; bootblock/data and compressor rights are separate. No image boot, loader interoperability or output checksum test performed. The excluded MarkyTurtle .NET Core port remains a separate unpromoted lineage decision; the original upstream is counted once. Related source graph remains partial.

Evidence: [source 1](https://github.com/djh0ffman/TTEDiskBuilder/blob/main/README.md) · [source 2](https://github.com/djh0ffman/TTEDiskBuilder)

## Non-promoted decisions

- [climbyskies](https://github.com/Ozzyboshi/climbyskies): duplicate. Build-only Docker wrapper for existing alpine9000/climbyskies; no independent game source. Retain only as related build reference. README explicitly points to alpine9000/climbyskies and says its music-containing asset archive is omitted for copyright reasons. Two-file tree consists of README and Dockerfile. Inspected commit c3b83daf49c01356950b3731e3844149cb67e4ea; actual root tree 26de6f657e009864bdb7e1eabb78045191c9bc5f.
- [game1](https://github.com/JoystickAndCursorKeys/game1): excluded. Only loosely inspired by Amiga AMOS/Blitz Basic; inspected source implements a new generic browser game engine without actual Amiga source, target or asset/development role. README and metadata describe a browser engine loosely based on AMOS/Blitz Basic. core/boot.js contains JavaScript state-machine and rendering machinery. Inspected commit 14b03dc588ee1385dd80f327e75a9a1ccdb77165; actual root tree 7524515d881c3adb559dc2d176e011b632d40199.
- [alsfs](https://github.com/Ozzyboshi/alsfs): duplicate. Linux FUSE component of the accepted ALSFS suite; do not count separately. C implementation, configure.ac and GPLv3 source notice inspected. Inspected commit 3b8e4b69842cf278bb4918c3653491b0d6e02d85; actual root tree 5c066da28540d86e2d38c0435f6bb3802cc94489.
- [alsfsNodejsServer](https://github.com/Ozzyboshi/alsfsNodejsServer): duplicate. HTTP/serial component of the accepted ALSFS suite; do not count separately. Node serial bridge inspected; package.json states GPL-2.0. Inspected commit 311e4f2a8abea25481cc7f2ec5612ece40b96244; actual root tree 9c0930bd4017611da4e51a1bf6de452be20d9eef.
- [alsfsdocumentation](https://github.com/Ozzyboshi/alsfsdocumentation): duplicate. Author documentation for the accepted ALSFS suite; not a source project. Clarifies 1 MB A600 upstream setup, Workbench 2.1 bootstrap and related repositories. Inspected commit 424389ac464ddba14161cd17cd25f6a110e14d4e; actual root tree 7c092cc38828182f67f7b6de0f6eacc634b6fb18.
- [adf-tools](https://github.com/weiju/adf-tools): deferred. Substantial related Scala ADF Tools/Arr!Jay precursor retained as lineage/context; not separately counted alongside the same author’s Python disk-development toolkit in this conservative batch. README claims OFS/FFS double-density filesystem creation/editing and icon viewing. LogicalVolume.scala implements actual disk-volume allocation/data operations; Main.scala is the Arr!Jay Swing UI; BSD-3-Clause notices and sbt build inspected. Could merit its own entry only after deliberate same-family identity review; no assumption that a new language automatically creates a new independent project. This is deferred related-tool identity review, not an established exact duplicate or proven code derivation. Inspected commit 334aedc4dbc3036e1437f2fab24c241760dd8449; actual root tree 9bd40ee339d186f6d20985789da3410ec0f55ba7.
- [BlockOff](https://github.com/colinvella/BlockOff): deferred. Implementation remains tokenized; without a reliable text export or detokenization review, this pass cannot claim substantive source review. README heading calls the project Blockhead while the repository and executable are BlockOff. The repository description and README identify an Amiga AMOS Professional puzzle game. Fetched all 74,808 bytes of BlockOff.AMOS through the base64 file endpoint. Decoded header is AMOS Basic v134; printable identifiers include game states for title/play/credits/high scores/editor/completion. This proves identifiable tokenized program material, not control-flow or correctness review. Tree includes 26 numbered level files, an executable, TileGrabber.AMOS, ABK tile/audio banks, MOD music, IFF/WAV sounds and bundled libraries. Latest ten commit messages concern new levels and an in-game joystick-menu fix in May 2018. Inspected commit 2189afa61fcfb21deaee783744323f426a381851; actual root tree 39256801ec257f2637ba675f5bd0f639b0f44dd7.
- [AIPong](https://github.com/daedalus2097/AIPong): deferred. Explicit introduction-to-coding workshop example; retain as a teaching reference, not a substantial standalone game in this batch. README explicitly describes a simple Pong game for the Amiga Ireland Blitz Basic tutorial; source header identifies the January 2018 workshop. The complete small source loads background/paddle/14 ball images, builds a 320x256 five-bitplane display, reads joystick and arrow-key paddle inputs, accelerates/bounces the ball, checks paddle collision and increments scores. Only two November 2023 commits are present in the inspected history page, initial commit and source/assets upload. Inspected commit 07277fd4d3ca812ecd2a77521fa80ed81dab3ade; actual root tree 1b16b1655bdf6bb5e9f5901a2ea0a1a23935d8a3.
- [BeliSw AMOS Simple Amiga Game](https://github.com/bennylindstedt/BeliSw.Amos.SimpleAmigaGame): deferred. The latest/longest ASCII example is predominantly empty procedures and does not implement the proposed game. README identifies this as example code for the YouTube course How to make a simple Amiga game. Episode3_3.Asc calls initialization, game-loop and termination procedures, but movement, input, collisions, scoring, spawning, cleanup and persistence procedures are empty; the only visible screen behavior prints Hello World and a cursor-movement message. Tree contains three Episode 3 AMOS/ASCII pairs, README, LICENSE and .gitignore. History has an initial commit and an Episode 3 upload in April 2022. Inspected commit e6841e5dae4d4076a2353c64715b5b9145480367; actual root tree 7005b9f9dfcb0de4f4495a7e071575c870295ec4.
- [BlockLevelScroller](https://github.com/coderMaff/BlockLevelScroller): deferred. Rendering/scrolling demonstration lacks gameplay, objectives or game state; retain as a small technique reference. The entire 1,984-byte plain-text source uses two 352x256 three-bitplane bitmaps, a 16-pixel tile grid and a colour-block array. A/D keys adjust pixel and column offsets; each frame swaps buffers and draws blocks. Left mouse exits. No player entity, collision system, game objectives or scoring are implemented. No README exists in the complete tree; the repository has only scroll.bb2 and MIT LICENSE. Three February 27, 2022 commits were inspected. Inspected commit eaebeb5a5d810cac96ab2d3d8569d9b332ed7423; actual root tree ff17364cf9eebc5ea448060f7c4c7e8cb5ddcd55.
- [Arlasoft C64 source collection — scope hold](https://github.com/1888games/ArlasoftC64): deferred. Overlapping collection retained as provenance, not independently counted. Uninspected unique unfinished/graphics-only portions remain potential future research, so this is not an exclusion of the entire corpus. README categorizes Complete, Partially Complete and Graphics Only folders; the complete recursive tree contains 6,048 entries. All ten standalone Arlasoft games reviewed in this pass have corresponding Complete folders. Nine have identical main-source blob SHAs; Merge64 has a differing main file but 56 identical blobs. This supports lineage collapse rather than separate collection/game counts. The collection also overlaps existing Caveman and Donkey Kong Junior entries and contains substantial unreviewed work-in-progress and graphics-only material. Hold as provenance/corpus inventory rather than a new umbrella project duplicating those games. Distinct unreviewed games may be investigated in a later focused pass. README requests no as-is unfinished preview releases and permits completion with credit. This is not a blanket open-source license; the isolated Graphics Only/Kye COPYING file does not license the corpus. Only README, complete tree, bounded history and exact-blob overlap were reviewed; the entire source corpus was not inspected. License: Informal author permission for completing WIP projects with credit and explicit objection to preview releases; no general license grant established.
- [Overdosed — scope hold](https://github.com/1888games/Overdosed): excluded. Unity project has no established C64/Amiga reconstruction connection. Repository metadata identifies a 48-hour Ludum Dare 40 game. The complete tree contains Unity scenes, materials, 3D models, audio and C# scripts; GameController.cs imports UnityEngine/TMPro and manages Unity objects, patients and nursing-game state. No native C64 assembly, build target or legacy-platform reconstruction evidence was found in this bounded screen. Do not infer C64 relevance from the author account. This is an out-of-scope hold, not a low-quality C64 candidate. Only metadata, tree, one source excerpt and bounded history inspected; no build or license verified. License: No license grant established in the bounded out-of-scope inspection.
- [Neptune Lander tutorial variant — lineage reference](https://github.com/OldSkoolCoder/NeptuneLander-1): duplicate. Related tutorial-following variant, not an independently counted game. README explicitly says it follows OldSkoolCoder and lists pending sound, levels, combined music/effects and high-score work. Main.asm enters native C64 initialization/IRQ/game flow; gameShip.asm implements landing pads, safe-zone collision and explosion animation. The CBM prg Studio project selects C64. Latest history merges C64-Mark’s work; GitHub fork=false does not negate the explicit tutorial lineage. Do not count as an independent game alongside NeptuneLander. Differences can inform provenance and alternate-source notes. No independent build/runtime result; license and bundled SID/music permissions unestablished. License: No standalone license grant established; metadata license is null and no license-named file occurs in the complete tree.
- [Erasoft / RQ progs preservation archive — scope hold](https://github.com/ricardoquesada/c64-c128-erasoft): deferred. Hold at the demonstrated incomplete/binary-provenance scope; no project promoted. README provides author provenance, addresses and runtime notes for several games and tools; tree contains D64/D71/ZIP images, scans and screenshots rather than textual implementations. LICENSE explicitly says there is no source code because the programs were entered in machine language via the C128 monitor. It licenses that code under Apache-2.0, other assets under CC-BY-4.0, and specifically forbids reuse of ripped TMRT music/clouds. CHANGELOG documents binary-era fixes including load addresses, C128 bank setup and modified intros. README specifies NTSC origins and a True Drive Emulation caveat for The Race. Hold for binary-preservation provenance; do not promote as a source reconstruction merely because code is licensed. Disk contents were not extracted and no substantive machine-code disassembly was independently reviewed. Original unmodified binaries and cleaned-up variants are not interchangeable; changelog lists changes. Ripped assets and third-party recracks require careful rights separation. License: Code Apache-2.0; most assets CC-BY-4.0; explicitly excludes ripped TMRT music and BC’s Quest for Tires clouds.
- [Droid64 — scope hold](https://github.com/rolandshacks/Droid64): deferred. Generic emulator implementations are visible, but Frodo family lineage remains collapsed with deferred vita64 rather than promoting another uncertain lineage record. README explicitly attributes the emulator to Christian Bauer's Frodo and says it was used nearly unchanged, with integration work. Older rosc77/Droid64 links are repository-name history, not another project. C64.cpp allocates a complete MOS6510/MOS6502-1541/VIC-II/SID/CIA/IEC/REU machine and copies embedded BASIC/Kernal/character/drive ROM arrays. CPUC64.cpp implements line-based CPU memory decoding and dispatches opcodes through CPU_emulline.h. Android build uses Gradle, Android SDK 23/build-tools 24.0.1, minSdk 15 and targetSdk 16. CMake 3.4.1 builds a shared Droid64 library from main, emu, pc and rom C++ directories. AudioControl.java uses Android AudioTrack; README describes OpenGL rendering, D64/T64 and zipped game archives. This is a generic emulator, not a game-specific emulation wrapper. The root Apache-2.0 notice does not resolve the licensing of the inherited Frodo core. The sister webOS port explicitly calls Frodo GPL; retain the mismatch rather than label all contents uniformly Apache-2.0. Embedded Commodore ROM arrays have separate redistribution rights; the app license does not establish those rights or game-archive rights. Build configuration contains a developer-specific signing path and obsolete Android toolchain versions; reproducibility on current tools is untested. Credential-like signing values were redacted from the evidence cache. Current-source files and 12 recent commit records inspected; last default-branch commit is in 2017 even though repository pushed_at is 2018. License: Root LICENSE and README state Apache-2.0; inherited Frodo and ROM rights unresolved. GitHub labels license NOASSERTION.
- [Frodo for webOS — scope hold](https://github.com/rolandshacks/frodo4webos): deferred. Generic emulator implementations are visible, but Frodo family lineage remains collapsed with deferred vita64 rather than promoting another uncertain lineage record. README identifies Roland Schabenberger as porter and Christian Bauer as original Frodo author; generic C64 hardware emulation is confirmed by C64.cpp's chip/drive construction and CPUC64.cpp. src/Makefile defaults to LINEBASED/FRODO_PC and exposes a SINGLECYCLE/FRODO_SC alternative. generic.mak defaults PLATFORM=PALM and WEBOS=1, uses Palm PDK ARM GNU toolchains, SDL/SDL_ttf/SDL_image, GLES_CM and pdl; it also contains g++ Windows/Linux alternatives. manual.txt specifically describes HP TouchPad corners/touch areas, disk/tape browsing, joystick-port switching and optional true 1541 emulation. No standalone license file appears in the complete tree. README asserts GPL without an exact version; source headers attribute Christian Bauer. Bundled resources contain 1541.ROM, Basic.ROM, Char.ROM and Kernal.ROM; their rights remain separate. Palm PDK, dated compiler/deployment assumptions, and mixed host-specific commands mean current reproducibility is not established. webOS is absent from the baseline platform-label set. Preserve webOS in runtime notes rather than introduce a new platform label or relabel it Android/Amiga. License: README says GPL (version unspecified); no complete license text found in tree. ROM rights unresolved.
- [VS64 Developer Tools bundle — lineage reference](https://github.com/rolandshacks/vs64devtools): duplicate. Binary-package manifest for the already tracked VS64 development environment, not a new tool implementation. The complete tree has README/LICENSE/packages.json plus ZIP packages; no assembler/emulator implementation is present. packages.json lists Windows ACME, Exomizer, VICE, JRE, Oscar64, LLVM-MOS, cc65, X16 emulator and Denise, a macOS ACME package, generic KickAssembler, and an empty Linux section. README documents jdeps/jlink construction of a Java runtime for KickAssembler; LICENSE.md explicitly calls this a collection of binary packages. ZIP contents were not unpacked or executed; listed package names and versions are manifest evidence, not verified functioning toolchains. Component-specific licenses differ; KickAssembler is explicitly described as Unknown/Freeware. The bundle's GPL/Zlib/Apache/BSD/PSF listings do not make one repository-wide license. Some distributed tools also target Commander X16, Amiga or other machines; that does not create additional projects for this packaging root. License: LICENSE.md is a component inventory, not a uniform grant: GPL-2.0, GPL-3.0, Zlib, Apache-2.0-with-LLVM-exception, BSD-2-Clause, PSF-2.0, JRE Classpath exception, and KickAssembler unknown/freeware.
- [SID FX Editor/Player prototype — scope hold](https://github.com/og2t/sid-fixer): deferred. Hold at the demonstrated incomplete/binary-provenance scope; no project promoted. README's detailed status limits completion to phases 1-2; phases 3-6 (editor UI, input, live editing, multi-slot management/file I/O) remain planned despite the opening 'complete' description. sid-player.kc contains three-voice SID register writes, frequency interpolation, filter settings, raster-IRQ setup, FX bank and start/stop API; main.kc implements only keyboard-driven explosion/laser/coin demonstrations. Makefile compiles only src/main.kc with KickC -t c64basic -O2. test-effects.kc is a prerequisite, but main.kc does not include it or call its five extra effect initializers, so 'eight effects' is not the actual wired demo scope. The IRQ handler's acknowledgement block writes VIC_RASTER, defined as $D012; IRQ installation uses a raw $FFFE vector. These are concrete source locations requiring hardware/banking validation, not independently reproduced failures. Comments claim 14 bytes per voice and 48 bytes per FX slot, while the listed primitive byte/word fields and padding do not substantiate that layout. No sizeof/assertion or generated-map evidence was found to reconcile it. The single returned commit explicitly names Claude as both author and committer, and the default branch also begins claude/. This supports Claude attribution only, not a further Claude Code/model claim. No build, emulator run, SID listening test, cycle measurement, PAL/NTSC timing validation, or memory-layout validation was performed. make test prints that manual testing is required; it is not an automated correctness suite. Frequency sweeps use frame counts; advertised PAL/NTSC and <500-cycle performance remain upstream claims. README license section is a placeholder asking the author to choose a license, not a grant. No license file exists in the complete tree. License: Unlicensed/undetermined: README contains '[Choose your license: MIT, GPL, Public Domain, etc.]'; no actual license grant identified. Explicit AI attribution: Claude. Explicit Claude name is the attribution basis. Branch name corroborates but does not independently establish product/model. Do not infer Claude Code from provider address.
- [Georg Rottensteiner Common library — lineage reference](https://github.com/GeorgRottensteiner/Common): duplicate. Directly compiled shared dependency and format evidence for Painter; not an independent new application record. Recursive tree contains 1,564 entries spanning graphics/UI, filesystem, codecs, networking, rendering and third-party support rather than a focused C64 program. FormatIFF.cpp implements IFF ILBM header/palette/bitplane loading plus saving; FormatIFF.h declares FORM/ILBM/BMHD/CMAP/BODY and auxiliary chunk identifiers. Painter's project file directly references this repository-shaped P:\Common hierarchy, including Grafik\ImageFormate\FormatIFF.cpp. No root README, root license text or independent build project was found in the complete tree; the verified consumer is Painter. No repository-wide license grant was established. Third-party libraries and source notices must remain separately attributed. CAMG handling is skipped, so special Amiga display-mode support cannot be inferred from generic IFF handling. Broad host portability and build completeness were not validated; no direct C64-specific format implementation was established. License: No root LICENSE/README grant found; no license assigned to repository as a whole.
- [Hyperload binary snapshot — scope hold](https://github.com/OldSkoolCoder/Hyperload): deferred. Hold at the demonstrated incomplete/binary-provenance scope; no project promoted. Repository description calls it a high-speed tape load/save routine for C64; initial content commit says it is a C64 program the author wrote. The complete three-file tree exposes one 1,793-byte PRG. It was fetched as base64 for static header inspection only. PRG begins with load address $0801 and tokenized BASIC SYS(2064) bootstrap followed by a machine-code payload; this does not constitute a complete editable BASIC/assembly implementation. Both returned commit messages and metadata contain no explicit generative-AI attribution. Not disassembled or executed. No loader timing, tape compatibility, recoverability or source-equivalence claims. No source/build/license paths exist in the inspected tree; a program binary alone is not counted as recovered source. No explicit license grant identified. License: No license file or other grant found.
- [amigazen/toolkit](https://github.com/amigazen/ToolKit): deferred. SDK distribution/collection with many shipped binaries, headers and existing component copies. No distinct source implementation selected for a new project; keep as collection discovery source. Its Codex name refers to an Amiga C lint tool, not evidence of OpenAI Codex use.
- [djh0ffman/xmtools](https://github.com/djh0ffman/XmTools): deferred. Substantive Windows/.NET XM serialization and injector source, but README ties it to an XMPlay tracker-music demonstration; inspected source does not establish actual Amiga or C64 implementation/development relevance. Shared author alone is insufficient.
- [amigaports/sdl2-amigaos4](https://github.com/AmigaPorts/sdl2-amigaos4): duplicate. Older SDL2 AmigaOS4 repository directs users to AmigaPorts/SDL. Preserve lineage; do not count a second multimedia-library port family.

## Publication boundary

Authored changes are the 44 approved projects, 352 audit areas, linked source/decision/research records, this report, sources.md and log.md. All 1,621 existing project and audit objects are preserved before automation. No application/workflow code, generated Activity/RSS or polling state is authored. Existing metadata and Pages workflows generate the live outputs; all 44 catalogue records, Activity additions in both generated windows, RSS additions, GitHub metadata and typed fields are verified separately.
