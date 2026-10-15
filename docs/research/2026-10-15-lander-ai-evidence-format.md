# Normalize Lander AI evidence for the activity collector



## lander-bbc-micro-ebenupton

### identity (reviewed)

Eben Upton ports David Braben's 1987 Lander demo, including landscape, ship, flight model, landing, fuel, map and sound.

- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/README.md
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/src/land.s
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/ref/lander/NOTES.md
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/ref/lander/flight.py
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/build.sh

### classification (reviewed)

Native 6502 implementation informed by Mark Moxon's annotated ARM reconstruction; not an original-source release or an embedded ARM emulation host.

- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/README.md
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/src/land.s
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/ref/lander/NOTES.md
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/ref/lander/flight.py
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/build.sh

### source_cpu (reviewed)

ref/lander/NOTES.md identifies Lander.arm as the reconstructed Archimedes source, and flight.py explicitly transcribes its routines and 32-bit arithmetic. ARM source and 6502 output are distinct.

- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/README.md
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/src/land.s
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/ref/lander/NOTES.md
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/ref/lander/flight.py
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/build.sh

### target_cpu (reviewed)

README explicitly targets a 2 MHz 6502; src/land.s implements the native renderer and sideways-RAM loader.

- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/README.md
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/src/land.s
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/ref/lander/NOTES.md
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/ref/lander/flight.py
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/build.sh

### build (reviewed)

README supplies lander.ssd and cc65/Python/numpy build instructions, with py65 reference comparisons. Its deterministic match is to the port's checked-in disk, not the original Archimedes executable. No independent compilation, execution, gameplay or byte comparison was performed; all four build flags remain unknown.

- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/README.md
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/src/land.s
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/ref/lander/NOTES.md
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/ref/lander/flight.py
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/build.sh

### runtime_profiles (reviewed)

README requires BBC Micro Model B, four writable 16 KB sideways-RAM banks and DFS. No independent hardware validation.

- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/README.md

### ai (reviewed)

The inspected head commit explicitly credits Claude Fable 5.1. This applies to Upton's port, independently of the predecessor's AI policy.

- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/README.md
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/src/land.s
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/ref/lander/NOTES.md
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/ref/lander/flight.py
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/build.sh
- https://github.com/ebenupton/lander/commit/8f2f11833d28254719264e496bd2f74bec02700c

### relationships (reviewed)

README and ref/lander/NOTES.md credit Mark Moxon's lander-source-code-acorn-archimedes and lander.bbcelite.com; loader and disk builder derive from ebenupton/beebgame. No blanket licensing claim is made. The repository URL and title were compared with the current catalogue; no equivalent project record was found.

- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/README.md
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/src/land.s
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/ref/lander/NOTES.md
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/ref/lander/flight.py
- https://github.com/ebenupton/lander/blob/8f2f11833d28254719264e496bd2f74bec02700c/build.sh
