"""Idempotent execution-method migration using already recorded architecture evidence.

No discovery, source fetching, audit changes, clock updates or history rewriting.
"""
import argparse
import json
from pathlib import Path

from catalogue_storage import load_projects, load_dataset, write_projects
from execution_architecture import research_v1_project

# Explicit reviewed paths, never a heuristic over all native translations.
# The evidence URLs and execution status of each path are preserved.
COMPILED = {
    **{pid: ('native PC build', 'Generated host code retains the NES hardware runtime; removing the instruction interpreter does not remove the embedded machine.') for pid in (
        'dr-mario-nes-mstan-recomp', 'duck-hunt-nes-mstan-recomp', 'faxanadu-nes-mstan-recomp',
        'gumshoe-nes-mstan-recomp', 'legend-of-zelda-nes-mstan-recomp', 'mega-man-3-nes-mstan-recomp',
        'super-mario-bros-nes-mstan-recomp', 'yoshi-nes-mstan-recomp', 'yoshis-cookie-nes-mstan-recomp')},
    **{pid: ('Generated native-C host', 'The compiled guest program retains the Lynx Suzy/Mikey hardware runtime. BAKED EMULATION includes compiled execution, not only interpreters.') for pid in (
        'chipschallenge-lynx-native-recomp', 'crystalmines2-lynx-native-recomp')},
    'platoon-native-swift-macos': ('Native Swift macOS application', 'Translated Swift routines retain the original data layout and reconstructed blitter/copper/Paula hardware runtime. BAKED EMULATION does not require a guest instruction interpreter.'),
    'pop2-macintosh-static-recompilation': ('Statically translated C++ with Toolbox API shims', 'Retained guest registers and machine-memory semantics make this BAKED EMULATION; API replacement alone would not.'),
    'shufflepuck-cafe-mac-static-recomp': ('Statically lifted C with Toolbox API shims', 'Retained guest registers and flat machine memory make this BAKED EMULATION; API replacement alone would not.'),
    'virtual-hydlide-saturn-static-recompilation': ('recompiled native runtime', 'Compiled Saturn programs retain the recreated hardware runtime, including the original sound driver alongside emulated SCSP; this is BAKED EMULATION.'),
}


def migrate_record(record):
    result = research_v1_project(record)
    selected = COMPILED.get(result.get('id'))
    for path in result.get('execution_paths') or []:
        if selected and path.get('name') == selected[0]:
            path['method'] = 'baked-emulation'
            notes = path.get('notes', '').replace('it is not a guest-CPU emulator path.',
                'compilation removes the instruction interpreter, not the retained machine runtime.')
            if selected[1] not in notes:
                notes = (notes + ' ' + selected[1]).strip()
            path['notes'] = notes
    return result


def migrate(root):
    root = Path(root)
    before = load_projects(root / 'data/projects.json')
    ids = {p['id'] for p in before}
    audits = load_dataset(root / 'data', 'project-audits.json')['projects']
    if len(ids) != len(before) or len(audits) != len(before) or ids != {a['project_id'] for a in audits}:
        raise ValueError('Migration requires exact unique project/audit coverage')
    after = [migrate_record(p) for p in before]
    # The comparison baseline is prior published evidence. Leave it untouched:
    # normal metadata recording emits the real architecture change events and
    # advances it atomically with validated metadata/history. Pages holds until
    # that prerequisite completes; pending unrelated changes cannot be blessed.
    changed = [p['id'] for p, q in zip(before, after) if p != q]
    paths = write_projects(root / 'data/projects.json', after)
    return {'projects': len(after), 'changed_projects': changed, 'changed_partitions': paths}



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    print(json.dumps(migrate(parser.parse_args().root)))
