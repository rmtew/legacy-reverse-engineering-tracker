"""Idempotent execution-method migration using already recorded architecture evidence.

No discovery, source fetching, audit changes, clock updates or history rewriting.
"""
import argparse
import hashlib
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


# Exact reviewed path baselines: concurrent architecture edits require review.
EXPECTED_COMPILED_PATHS = {
    "chipschallenge-lynx-native-recomp": "c5b1ac8c7e8f29c234e2bd634782b1f44ea4d0cadd3a7065ee45b4d0d1d1efcf",
    "crystalmines2-lynx-native-recomp": "a75e8cabd3d9b5b4bf275333b08e28b0ee5b8ce32b3f2eb47b768398790aa209",
    "dr-mario-nes-mstan-recomp": "365355ee41950bdbdbf4b4b5594d5843154f4881dcbce02e73a3d7c4f9f19fa6",
    "duck-hunt-nes-mstan-recomp": "9264660a5e35dc836f2411af0c590c149ac680645b75f5503e5d22ef70c3e441",
    "faxanadu-nes-mstan-recomp": "9f3cde755eb96d732a225bba120e8105185a08d32709ca559fc8679419f1569c",
    "gumshoe-nes-mstan-recomp": "29ba6884cad6887d59b3173047689c8a582ed552a13266af0da8f9c7618ffc04",
    "legend-of-zelda-nes-mstan-recomp": "4a487ad62dc27d94eafbd5978faa8a6a0f4ddc24c2bb11a663387eb02244fb2c",
    "mega-man-3-nes-mstan-recomp": "fecbaa25d7435fde0a648d872682bb790887f2b59f1e281c5bdd4b63555fa140",
    "platoon-native-swift-macos": "11d79d2b42877ff191b9b8a97ed602027e617a60aff16de77461def0b9dad5b5",
    "pop2-macintosh-static-recompilation": "8348c615a06b0df35dad1f734d22305a328707c4c8fc45420db95072fdebc1e1",
    "shufflepuck-cafe-mac-static-recomp": "e4cc93ea23a024a46b4ea0d453afd5f89a4f541233dea1c022d0365ec316286a",
    "super-mario-bros-nes-mstan-recomp": "01f46d870ab7b4cc208c69d19fd48b570d6c7202e1e406ba2b84137db62f98cc",
    "virtual-hydlide-saturn-static-recompilation": "e6c91daf7031f8d6b40e3b4d78e9b5c24a9bdfab6faf0a4a621fc6e6fc5f0ae5",
    "yoshi-nes-mstan-recomp": "0067fd95fc0f7af977c60ac15d563286fd6188bb51a217786741940563565209",
    "yoshis-cookie-nes-mstan-recomp": "cc3736bbab24db686c371fc4b12500719dfd0db61b9eda229e67a98507ade3ed"
}


def path_digest(path):
    return hashlib.sha256(json.dumps(path, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode()).hexdigest()


def migrate_record(record):
    result = research_v1_project(record)
    selected = COMPILED.get(result.get('id'))
    for path in result.get('execution_paths') or []:
        if selected and path.get('name') == selected[0]:
            if path.get('method') == 'baked-emulation':
                continue
            if path_digest(path) != EXPECTED_COMPILED_PATHS[result['id']]:
                raise ValueError('Execution path changed; review migration mapping: ' + result['id'])
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
