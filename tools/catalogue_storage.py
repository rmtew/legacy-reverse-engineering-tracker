"""Canonical partition storage; legacy monoliths are read-only snapshot inputs.

SHA-256 ID prefixes route records independently of insertion order. Start with
one hex digit; split only an overflowing prefix. Indexes preserve original order and
metadata; shards contain no copied global timestamps. All writes use this module.
"""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import re
import subprocess

KINDS = {'projects.json': ('projects', 'id'), 'project-audits.json': ('project-audits', 'project_id')}
FILES = (*KINDS, 'discovery-sources.json', 'discovery-decisions.json', 'research-activity.json')
# One quarter of the connector's 16 MiB limit, including escaped content/envelope.
REQUEST_LIMIT = 4 * 1024 * 1024
REPOSITORY = 'rmtew/legacy-reverse-engineering-tracker'


def encode(value):
    return (json.dumps(value, ensure_ascii=False, separators=(',', ':'), allow_nan=False) + '\n').encode('utf-8')


def request_size(content):
    return len(json.dumps({'repository_full_name': REPOSITORY, 'encoding': 'utf-8',
                           'content': content.decode('utf-8')}, ensure_ascii=False,
                          separators=(',', ':')).encode('utf-8'))


def bounded(content, label, limit=REQUEST_LIMIT):
    size = request_size(content)
    if size > limit:
        raise ValueError(f'{label}: escaped connector request {size} exceeds {limit} bytes; split/review oversized record or index')
    return content


def index_name(name):
    return KINDS[name][0] + '.index.json'


def route(pid):
    if not isinstance(pid, str) or not pid:
        raise ValueError('Record needs a nonempty string ID')
    return hashlib.sha256(pid.encode('utf-8')).hexdigest()


def render(name, value, limit=REQUEST_LIMIT):
    kind, key = KINDS[name]
    records = value if name == 'projects.json' else value['projects']
    ids = [r[key] for r in records]
    if len(set(ids)) != len(ids):
        raise ValueError(f'Duplicate IDs in {name}')
    groups = {}
    for record in records:
        groups.setdefault(route(record[key])[:1], []).append(record)
    output, refs = {}, []

    def partition(prefix, items):
        items = sorted(items, key=lambda r: r[key])
        content = encode(items)
        if request_size(content) > limit:
            if len(items) == 1 or len(prefix) == 64:
                bounded(content, f'{kind}/{items[0][key]}', limit)
            children = {}
            for item in items:
                children.setdefault(route(item[key])[:len(prefix)+1], []).append(item)
            for child, subset in sorted(children.items()):
                partition(child, subset)
            return
        path = f'{kind}/{prefix}.json'
        output[path] = content
        refs.append({'path': path, 'count': len(items), 'sha256': hashlib.sha256(content).hexdigest()})

    for prefix, items in sorted(groups.items()):
        partition(prefix, items)
    index = {'format': 'tracker-partitions/v1', 'kind': kind, 'order': ids, 'shards': refs}
    if name != 'projects.json':
        index['metadata'] = {k: v for k, v in value.items() if k != 'projects'}
    output[index_name(name)] = bounded(encode(index), index_name(name), limit)
    return output


def load_dataset(data_dir, name, *, read=None, exists=None):
    """Read one layout, rejecting mixed, corrupt, missing or unsafe references.

    Optional byte reader supports historical Git snapshots without materializing
    another checkout. No fallback from an invalid partition layout to legacy data.
    """
    data_dir = Path(data_dir)
    def local_read(path):
        target = data_dir / path
        if not target.resolve().is_relative_to(data_dir.resolve()):
            raise ValueError(f'Storage path escapes data directory: {path}')
        return target.read_bytes()
    read = read or local_read
    exists = exists or (lambda p: (data_dir / p).exists())
    if name not in KINDS:
        return json.loads(read(name))
    ix = index_name(name)
    if exists(name) and exists(ix):
        raise ValueError(f'Ambiguous mixed storage layout: {name} and {ix}')
    if not exists(ix):
        return json.loads(read(name))
    index_content = read(ix)
    bounded(index_content, ix)
    index = json.loads(index_content)
    kind, key = KINDS[name]
    if not isinstance(index, dict):
        raise ValueError(f'Invalid storage index: {ix}')
    if name != 'projects.json' and not isinstance(index.get('metadata'), dict):
        raise ValueError(f'Invalid audit metadata: {ix}')
    if index.get('format') != 'tracker-partitions/v1' or index.get('kind') != kind:
        raise ValueError(f'Invalid storage index: {ix}')
    refs, order = index.get('shards'), index.get('order')
    if not isinstance(refs, list) or not isinstance(order, list) or any(not isinstance(x, str) for x in order) or len(set(order)) != len(order):
        raise ValueError(f'Invalid shard references/order: {ix}')
    records, paths, prefixes = {}, set(), []
    for ref in refs:
        if not isinstance(ref, dict) or not isinstance(ref.get('path'), str):
            raise ValueError('Invalid shard reference')
        if type(ref.get('count')) is not int or ref['count'] <= 0:
            raise ValueError('Invalid shard count')
        path = ref['path']
        match = re.fullmatch(re.escape(kind) + r'/([0-9a-f]{1,64})\.json', path)
        if not match or path in paths:
            raise ValueError(f'Invalid shard reference: {path}')
        prefix = match[1]
        if any(prefix.startswith(p) or p.startswith(prefix) for p in prefixes):
            raise ValueError('Overlapping shard routes')
        prefixes.append(prefix)
        paths.add(path)
        content = read(path)
        bounded(content, path)
        if hashlib.sha256(content).hexdigest() != ref.get('sha256'):
            raise ValueError(f'Shard digest mismatch: {path}')
        items = json.loads(content)
        if not isinstance(items, list) or not items or len(items) != ref.get('count'):
            raise ValueError(f'Shard count mismatch: {path}')
        for record in items:
            if not isinstance(record, dict) or key not in record:
                raise ValueError(f'Invalid shard record: {path}')
            pid = record[key]
            if pid in records or not route(pid).startswith(prefix):
                raise ValueError(f'Duplicate or misrouted record: {pid}')
            records[pid] = record
    if set(records) != set(order):
        raise ValueError(f'Index record coverage mismatch: {ix}')
    result = [records[pid] for pid in order]
    return result if name == 'projects.json' else {**index['metadata'], 'projects': result}


def load_projects(path):
    return load_dataset(Path(path).parent, 'projects.json')


def load_all(data_dir):
    return {name: load_dataset(data_dir, name) for name in FILES}


def storage_paths(data_dir, names=FILES):
    paths = []
    for name in names:
        if name in KINDS and (Path(data_dir) / index_name(name)).exists():
            load_dataset(data_dir, name)  # Validate before trusting paths.
            index = json.loads((Path(data_dir) / index_name(name)).read_bytes())
            paths.extend([index_name(name), *(r['path'] for r in index['shards'])])
        else:
            paths.append(name)
    return paths


def write_all(data_dir, data):
    """Render/check everything first; write only changed files, remove old layout.

    Callers needing cross-file validation stage this in an isolated directory
    before replacing their checkout. Git publication commits the resulting tree
    atomically with the expected baseline SHA.
    """
    data_dir = Path(data_dir)
    output = {}
    old = {p for p in storage_paths(data_dir, data) if (data_dir / p).exists()} if data_dir.exists() else set()
    for name, value in data.items():
        if name in KINDS:
            output.update(render(name, value))
        else:
            current = data_dir / name
            content = current.read_bytes() if current.exists() and json.loads(current.read_bytes()) == value else encode(value)
            output[name] = bounded(content, name)
    changed = []
    for path, content in output.items():
        target = data_dir / path
        if target.exists() and target.read_bytes() == content:
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)
        changed.append(path)
    for path in sorted(old - output.keys()):
        (data_dir / path).unlink(missing_ok=True)
        changed.append(path)
    return changed


def write_projects(path, projects):
    return write_all(Path(path).parent, {'projects.json': projects})


def load_git_dataset(revision, name, cwd=None):
    def read(path):
        return subprocess.check_output(['git', 'show', f'{revision}:data/{path}'], cwd=cwd)
    names = set(subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', revision, '--', 'data'], cwd=cwd).decode().splitlines())
    if not any('data/' + p in names for p in (name, index_name(name))):
        return []
    return load_dataset('data', name, read=read, exists=lambda p: 'data/' + p in names)


def load_git_projects(revision, cwd=None):
    return load_git_dataset(revision, 'projects.json', cwd)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data', type=Path, default=Path(__file__).resolve().parents[1] / 'data')
    args = parser.parse_args()
    before = load_all(args.data)
    changed = write_all(args.data, before)
    if before != load_all(args.data):
        raise ValueError('Migration changed logical data')
    print(f'Preserved {len(before["projects.json"])} projects and {len(before["project-audits.json"]["projects"])} audits; changed {len(changed)} files')
