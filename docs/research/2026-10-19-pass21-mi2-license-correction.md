# Correct MI2 Redux source-license attribution from the pinned README.

Correct MI2 Redux source-license attribution from the pinned README.

Date: 2026-10-19 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- monkey-island2-amiga-resource-redux / Target CPU (no-evidence-found): The inspected portable/high-level build material does not establish a fixed output CPU or minimum hardware requirement; the target CPU stays unknown.
- monkey-island2-amiga-resource-redux / Runtime profiles (no-evidence-found): No independently verified runtime profile was established for Monkey Island 2 Redux — Amiga resource re-encoding tools. Upstream platform or test claims are recorded as claims rather than verified hardware requirements.
- monkey-island2-amiga-resource-redux / AI (no-evidence-found): No explicit development-AI use statement was established in the inspected material and pinned commit. Usage stays unknown; no non-use claim is made.

## monkey-island2-amiga-resource-redux

Project ID: monkey-island2-amiga-resource-redux · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "monkey-island2-amiga-resource-redux"
}
```

Expected existing project SHA256: 9d1219afd1bde2d5de0e4fc4c774ee1c0b1abf2b882ef4002686dc3ae2cb2f24

### Identity (reviewed)

Re-encodes Monkey Island 2 graphics/resources for Amiga OCS constraints, including a real SMAP zigzag encoder and resource rebuild pipeline, using owner-supplied PC/Amiga game material.
- https://github.com/tinic/mi2-redux/blob/975c09defd2075197125825c77630114fe20dc37/README.md
- https://github.com/tinic/mi2-redux/blob/975c09defd2075197125825c77630114fe20dc37/tools/encode_amiga.py
- https://github.com/tinic/mi2-redux/blob/975c09defd2075197125825c77630114fe20dc37/build.sh
- https://github.com/tinic/mi2-redux/commit/975c09defd2075197125825c77630114fe20dc37

### Classification (reviewed)

This is a source-backed resource enhancement/conversion pipeline, not a reconstructed SCUMM game engine. The pinned README explicitly licenses repository source code as MIT. Monkey Island 2 original assets and patched/derived game data remain LucasArts/Disney material; that MIT statement is not extended to original game content.
- https://github.com/tinic/mi2-redux/blob/975c09defd2075197125825c77630114fe20dc37/README.md
- https://github.com/tinic/mi2-redux/blob/975c09defd2075197125825c77630114fe20dc37/tools/encode_amiga.py
- https://github.com/tinic/mi2-redux/blob/975c09defd2075197125825c77630114fe20dc37/build.sh
- https://github.com/tinic/mi2-redux/commit/975c09defd2075197125825c77630114fe20dc37

### Source CPU (not-applicable)

No predecessor binary CPU is assigned: this is native work or format/language tooling. A platform name or gameplay inspiration is not treated as proof of recovered code lineage.
- https://github.com/tinic/mi2-redux/blob/975c09defd2075197125825c77630114fe20dc37/README.md
- https://github.com/tinic/mi2-redux/blob/975c09defd2075197125825c77630114fe20dc37/tools/encode_amiga.py
- https://github.com/tinic/mi2-redux/blob/975c09defd2075197125825c77630114fe20dc37/build.sh
- https://github.com/tinic/mi2-redux/commit/975c09defd2075197125825c77630114fe20dc37

### Target CPU (no-evidence-found)

The inspected portable/high-level build material does not establish a fixed output CPU or minimum hardware requirement; the target CPU stays unknown.
- https://github.com/tinic/mi2-redux/blob/975c09defd2075197125825c77630114fe20dc37/README.md
- https://github.com/tinic/mi2-redux/blob/975c09defd2075197125825c77630114fe20dc37/tools/encode_amiga.py
- https://github.com/tinic/mi2-redux/blob/975c09defd2075197125825c77630114fe20dc37/build.sh
- https://github.com/tinic/mi2-redux/commit/975c09defd2075197125825c77630114fe20dc37

### Build (reviewed)

build.sh and Python/C++ asset tools perform resource conversion; README requires GCC 15 for its C++26 converter. This is an asset/resource enhancement pipeline, not a reconstructed SCUMM engine. No candidate source, build tool, emulator or binary was executed during this review; build/runtime/byte-exact flags remain unknown.
- https://github.com/tinic/mi2-redux/blob/975c09defd2075197125825c77630114fe20dc37/README.md
- https://github.com/tinic/mi2-redux/blob/975c09defd2075197125825c77630114fe20dc37/tools/encode_amiga.py
- https://github.com/tinic/mi2-redux/blob/975c09defd2075197125825c77630114fe20dc37/build.sh
- https://github.com/tinic/mi2-redux/commit/975c09defd2075197125825c77630114fe20dc37

### Runtime profiles (no-evidence-found)

No independently verified runtime profile was established for Monkey Island 2 Redux — Amiga resource re-encoding tools. Upstream platform or test claims are recorded as claims rather than verified hardware requirements.
- https://github.com/tinic/mi2-redux/blob/975c09defd2075197125825c77630114fe20dc37/README.md
- https://github.com/tinic/mi2-redux/blob/975c09defd2075197125825c77630114fe20dc37/tools/encode_amiga.py
- https://github.com/tinic/mi2-redux/blob/975c09defd2075197125825c77630114fe20dc37/build.sh
- https://github.com/tinic/mi2-redux/commit/975c09defd2075197125825c77630114fe20dc37

### AI (no-evidence-found)

No explicit development-AI use statement was established in the inspected material and pinned commit. Usage stays unknown; no non-use claim is made.
- https://github.com/tinic/mi2-redux/blob/975c09defd2075197125825c77630114fe20dc37/README.md
- https://github.com/tinic/mi2-redux/blob/975c09defd2075197125825c77630114fe20dc37/tools/encode_amiga.py
- https://github.com/tinic/mi2-redux/blob/975c09defd2075197125825c77630114fe20dc37/build.sh
- https://github.com/tinic/mi2-redux/commit/975c09defd2075197125825c77630114fe20dc37

### Relationships (reviewed)

Uses existing SCUMM resource formats and game copies; no independent engine reconstruction or ownership of original art is implied.
- https://github.com/tinic/mi2-redux/blob/975c09defd2075197125825c77630114fe20dc37/README.md
- https://github.com/tinic/mi2-redux/blob/975c09defd2075197125825c77630114fe20dc37/tools/encode_amiga.py
- https://github.com/tinic/mi2-redux/blob/975c09defd2075197125825c77630114fe20dc37/build.sh
- https://github.com/tinic/mi2-redux/commit/975c09defd2075197125825c77630114fe20dc37

## Research event notes

Follow-up correction to the pass21 license narrative: the same pinned README explicitly states MIT for source code; no build/runtime or original-asset rights claim is changed.
