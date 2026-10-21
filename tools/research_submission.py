#!/usr/bin/env python3
"""Trusted-main, data-only research ingestion with atomic receipts and a durable outbox."""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

from catalogue_storage import bounded, encode, load_dataset
from publication_pipeline import prepare, safe_path, verify_files, file_entry, digest as content_digest
from research_record import EvidenceCache, compile_records, review_digest
from build_site import build
from refresh_scope import repository

INBOX = 'submissions/research'
RECEIPTS = 'state/research-receipts'
OUTBOX = 'state/research-outbox'
MAX_BYTES = 1024 * 1024
MAX_SCAN = 2048
MAX_BATCHES = 4
EVENT = re.compile(r'[A-Za-z0-9][A-Za-z0-9_.-]{0,127}\Z')
SHA = re.compile(r'[0-9a-f]{40}\Z')
REFRESH_REQUEST = re.compile(r'research-[0-9a-f]{64}\Z')
CODE_GUARDS = {}


def event_name(value):
    if not isinstance(value, str) or not EVENT.fullmatch(value):
        raise ValueError('Invalid research event ID (safe filename, maximum 128 characters)')
    return value


def path_for(prefix, event):
    return f'{prefix}/{event_name(event)}.json'


def pairs(items):
    result = {}
    for key, value in items:
        if key in result:
            raise ValueError('Duplicate JSON key: ' + key)
        result[key] = value
    return result


def decode(raw):
    if len(raw) > MAX_BYTES:
        raise ValueError('Research submission exceeds the 1 MiB input ceiling')
    try:
        return json.loads(raw, object_pairs_hook=pairs,
                          parse_constant=lambda value: (_ for _ in ()).throw(ValueError('Non-finite JSON')))
    except (UnicodeError, RecursionError) as exc:
        raise ValueError('Invalid UTF-8 JSON research submission') from exc


def checked(document, event=None):
    if not isinstance(document, dict):
        raise ValueError('Research submission must be an object')
    name = event_name(document.get('event_id'))
    if event is not None and event != name:
        raise ValueError('Submission filename does not match its research event ID')
    review = document.get('review') or {}
    if review.get('status') != 'ready' or review.get('digest') != review_digest(document):
        raise ValueError('Research submission needs a ready, matching explicit review seal')
    arrays = ('records', 'sources', 'source_updates', 'tasks', 'task_updates', 'decisions', 'source_ids')
    if any(not isinstance(document.get(k, []), list) for k in arrays):
        raise ValueError('Research batch collections must be arrays')
    if len(document.get('records', [])) > 100 or sum(len(document.get(k, [])) for k in arrays) > 500:
        raise ValueError('Research submission exceeds bounded batch entry limits')
    compile_records(document)  # Includes inline proof integrity and all authoring checks; no fetches.
    bounded(encode(document), name)
    return name, review_digest(document)


def package(document, cache=None):
    document = copy.deepcopy(document)
    for proof in document.get('proofs', {}).values():
        if 'text' not in proof and cache is not None:
            proof['text'] = EvidenceCache(cache).get(proof)
    event, digest = checked(document)
    raw = encode(document)
    if len(raw) > MAX_BYTES:
        raise ValueError('Research submission exceeds the 1 MiB input ceiling; split the reviewed pass')
    return raw, {'event_id': event, 'digest': digest, 'path': path_for(INBOX, event), 'bytes': len(raw)}


def submission_bundle(document, root, output, baseline=None, cache=None):
    """The existing connector publisher uploads exactly one reviewed input blob."""
    root, output = Path(root), Path(output)
    if output.resolve() == root.resolve() or root.resolve() in output.resolve().parents:
        raise ValueError('Submission bundle must be outside the checkout')
    baseline = baseline or revision(root)
    if not SHA.fullmatch(baseline):
        raise ValueError('Submission baseline must be a full commit SHA')
    raw, info = package(document, cache)
    existing = blob(root, baseline, info['path'], optional=True)
    baseline_files = []
    if existing is not None:
        _, old_digest = checked(decode(existing), info['event_id'])
        if old_digest != info['digest']:
            raise ValueError('Research event ID already has conflicting reviewed content')
        baseline_files.append(file_entry(info['path'], existing))
    manifest = {'version': 1, 'baseline_commit': baseline, 'event_id': info['event_id'],
                'input_digest': content_digest({'baseline': baseline, 'document': decode(raw)}),
                'files': [file_entry(info['path'], raw)], 'baseline_files': baseline_files,
                'submission': {'version': 1, 'event_id': info['event_id'], 'digest': info['digest']}}
    if output.exists():
        if decode((output / 'manifest.json').read_bytes()) != manifest:
            raise ValueError('Submission bundle already belongs to another input/baseline')
        verify_files(output / 'payload', manifest)
    else:
        output.mkdir(parents=True)
        target = output / 'payload' / info['path']
        target.parent.mkdir(parents=True)
        target.write_bytes(raw)
        (output / 'manifest.json').write_bytes(encode(manifest))
    return {**info, 'files': 1, 'request_bytes': manifest['files'][0]['request_bytes']}


def git(root, *args, check=True):
    return subprocess.run(['git', *args], cwd=root, check=check, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE, timeout=90)


def revision(root):
    value = git(root, 'rev-parse', 'HEAD').stdout.decode().strip()
    if not SHA.fullmatch(value):
        raise ValueError('Invalid checkout baseline')
    return value


def tree(root, ref):
    result = []
    for entry in git(root, 'ls-tree', '-r', '-z', ref).stdout.split(b'\0'):
        if entry:
            meta, path = entry.split(b'\t', 1)
            _, kind, sha = meta.decode().split()
            result.append({'path': path.decode(), 'type': kind, 'sha': sha})
    return {'tree': result, 'truncated': False}


def blob(root, ref, path, optional=False):
    result = git(root, 'show', f'{ref}:{path}', check=False)
    if result.returncode:
        if optional:
            return None
        raise ValueError('Missing committed research input: ' + path)
    return result.stdout


def receipt(root, ref, event):
    raw = blob(root, ref, path_for(RECEIPTS, event), optional=True)
    if raw is None:
        return None
    return checked_receipt(decode(raw), event)


def checked_receipt(value, event):
    if not isinstance(value, dict):
        raise ValueError('Invalid research receipt: ' + event)
    if (value.get('version') != 1 or value.get('event_id') != event
            or not re.fullmatch('[0-9a-f]{64}', value.get('digest', ''))
            or not SHA.fullmatch(value.get('input_blob', ''))):
        raise ValueError('Invalid research receipt: ' + event)
    return value


def refresh_repositories(root, request_id, records):
    """Resolve a research handoff from durable provenance, never from due work.

    None means an ordinary adaptive request; an empty set is a valid, empty
    research scope (for example, a removed or now non-GitHub project).
    Preserve the catalogue's repository keys, including their existing casing.
    """
    if not request_id.startswith('research-'):
        return None
    if not REFRESH_REQUEST.fullmatch(request_id):
        raise ValueError('Invalid research refresh request ID')
    paths = sorted((Path(root) / RECEIPTS).glob('*.json'))
    if len(paths) > MAX_SCAN:
        raise ValueError('Research receipt scan ceiling reached')
    matches = []
    for path in paths:
        try:
            value = decode(path.read_bytes())
        except ValueError:
            # Unrelated damaged historical receipts cannot prevent a valid
            # handoff. A damaged intended receipt still fails the match below.
            continue
        if not isinstance(value, dict) or value.get('digest') != request_id.removeprefix('research-'):
            continue
        event = event_name(path.stem)
        matches.append(checked_receipt(value, event))
    if len(matches) != 1:
        raise ValueError('Research refresh needs exactly one matching durable receipt')
    summary = matches[0].get('summary')
    if not isinstance(summary, dict):
        raise ValueError('Invalid research receipt project summary')
    ids = set()
    for key in ('projects', 'updated_projects'):
        values = summary.get(key)
        if not isinstance(values, list) or any(not isinstance(pid, str) or not pid for pid in values):
            raise ValueError('Invalid research receipt project summary')
        ids.update(values)
    # The authored repo URL, not possibly stale github.repository metadata, is
    # authoritative after repository moves. Removed IDs cannot widen the scope.
    return {repo for record in records if record['id'] in ids if (repo := repository(record))}


def selected(root, event=None):
    ref = revision(root)
    if event:
        return [event_name(event)]
    entries = {e['path']: e['sha'] for e in tree(root, ref)['tree'] if e['type'] == 'blob'}
    inputs = sorted(p for p in entries if p.startswith(INBOX + '/'))
    if len(inputs) > MAX_SCAN:
        raise ValueError('Research inbox scan ceiling reached; archive completed submissions with review')
    pending = []
    for path in inputs:
        name = event_name(path.removeprefix(INBOX + '/').removesuffix('.json'))
        if path != path_for(INBOX, name):
            raise ValueError('Invalid research inbox path')
        old = receipt(root, ref, name)
        if old:
            if old['input_blob'] != entries[path]:
                _, digest = checked(decode(blob(root, ref, path)), name)
                if digest != old['digest']:
                    raise ValueError('Research event ID already has conflicting reviewed content: ' + name)
            if path_for(OUTBOX, name) not in entries:
                continue
        pending.append(name)
        if len(pending) == MAX_BATCHES:
            break
    return pending


def apply(root, event):
    """Validate in isolation; caller publishes data, receipt and outbox in one commit."""
    root = Path(root)
    baseline = revision(root)
    input_path = path_for(INBOX, event)
    raw = blob(root, baseline, input_path)
    document = decode(raw)
    _, digest = checked(document, event)
    old = receipt(root, baseline, event)
    if old:
        if old['digest'] != digest:
            raise ValueError('Research event ID already has conflicting reviewed content: ' + event)
        history = load_dataset(root / 'data', 'research-activity.json')['events']
        report = blob(root, baseline, f'docs/research/{event}.md')
        if (sum(e['id'] == event for e in history) != 1
                or hashlib.sha256(report).hexdigest() != old['report_sha256']):
            raise ValueError('Research receipt does not match published provenance: ' + event)
        return {'event_id': event, 'digest': digest, 'changed': [], 'duplicate': True}
    with tempfile.TemporaryDirectory(prefix='research-apply-') as directory:
        temporary = Path(directory)
        bundle = temporary / 'bundle'
        manifest = prepare(document, root, bundle, baseline, tree(root, baseline))
        verify_files(bundle / 'payload', manifest)
        allowed = {'data/projects.index.json', 'data/project-audits.index.json', 'data/discovery-sources.json',
                   'data/discovery-decisions.json', 'data/research-activity.json', 'sources.md', 'log.md',
                   f'docs/research/{event}.md'}
        names = []
        for entry in manifest['files']:
            name = entry['path']
            safe_path(name)
            if name not in allowed and not re.fullmatch(r'data/(?:projects|project-audits)/[0-9a-f]{1,64}\.json', name):
                raise ValueError('Unsupported research output path: ' + name)
            names.append(name)
        # Projection generation runs on the server, before any canonical writes.
        stage = temporary / 'site-root'
        shutil.copytree(root / 'data', stage / 'data')
        shutil.copytree(root / 'web', stage / 'web')
        shutil.copy2(root / 'index.html', stage / 'index.html')
        for entry in manifest['files']:
            if entry['path'].startswith('data/'):
                target = stage / entry['path']
                if entry['sha'] is None:
                    target.unlink(missing_ok=True)
                else:
                    target.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(bundle / 'payload' / entry['path'], target)
        build(stage, temporary / 'site')
        value = {'version': 1, 'event_id': event, 'digest': digest, 'baseline_commit': baseline,
                 'input_blob': hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest(),
                 'report_sha256': hashlib.sha256((bundle / 'payload' / f'docs/research/{event}.md').read_bytes()).hexdigest(),
                 'summary': manifest['summary']}
        extras = {path_for(RECEIPTS, event): encode(value), path_for(OUTBOX, event): encode({'digest': digest})}
        changes = {e['path']: None if e['sha'] is None else (bundle / 'payload' / e['path']).read_bytes()
                   for e in manifest['files']}
        changes.update(extras)
        backups = {name: (root / name).read_bytes() if (root / name).exists() else None for name in changes}
        try:
            for name, content in changes.items():
                target = root / name
                target.parent.mkdir(parents=True, exist_ok=True)
                if content is None:
                    target.unlink(missing_ok=True)
                else:
                    target.write_bytes(content)
        except OSError:
            for name, content in backups.items():
                if content is None:
                    (root / name).unlink(missing_ok=True)
                else:
                    (root / name).write_bytes(content)
            raise
    return {'event_id': event, 'digest': digest, 'changed': sorted(changes), 'duplicate': False}


def sync(root):
    key = str(Path(root).resolve())
    def code_identity():
        return {e['path']: e['sha'] for e in tree(root, revision(root))['tree']
                if e['path'].startswith('tools/') and e['path'].endswith(('.py', '.js'))}
    original = CODE_GUARDS.setdefault(key, code_identity())
    git(root, 'fetch', 'origin', 'main')
    git(root, 'reset', '--hard', 'origin/main')
    if code_identity() != original:
        raise ValueError('Publication tools changed on main; rerun with the latest trusted code')
    # Only generated canonical paths; the reviewed inbox is tracked and retained.
    git(root, 'clean', '-fd', '--', 'data/', 'docs/research/', RECEIPTS + '/', OUTBOX + '/')


def publish_one(root, event):
    for attempt in range(3):
        sync(root)
        result = apply(root, event)
        if not result['changed']:
            return result
        git(root, 'add', '-A', '--', *result['changed'])
        git(root, 'commit', '-m', 'Apply reviewed research ' + event)
        if git(root, 'push', 'origin', 'HEAD:main', check=False).returncode == 0:
            return result
    raise RuntimeError('Research publication lost three fast-forward races; rerun to resume safely')


def publish(root, result_path, event=None):
    if git(root, 'status', '--porcelain').stdout.strip():
        raise ValueError('Publication requires a clean dedicated checkout')
    sync(root)
    events = selected(root, event)
    # Reject invalid/unreviewed selected inputs before publishing any of them.
    for name in events:
        checked(decode(blob(root, revision(root), path_for(INBOX, name))), name)
    results = [publish_one(root, name) for name in events]
    Path(result_path).write_bytes(encode({'events': [r['event_id'] for r in results]}))
    print(json.dumps({'processed': len(results), 'applied': sum(not r['duplicate'] for r in results)}))


def dispatch_refresh(digest):
    subprocess.run(['gh', 'workflow', 'run', 'refresh-github.yml', '--ref', 'main', '-f',
                    'request_id=research-' + digest], check=True, timeout=60)


def handoff(root, result_path):
    if git(root, 'status', '--porcelain').stdout.strip():
        raise ValueError('Handoff requires a clean dedicated checkout')
    events = decode(Path(result_path).read_bytes()).get('events')
    if not isinstance(events, list) or len(events) > MAX_BATCHES:
        raise ValueError('Invalid research handoff result')
    for name in events:
        event_name(name)
        sync(root)
        ref = revision(root)
        old = receipt(root, ref, name)
        pending = blob(root, ref, path_for(OUTBOX, name), optional=True)
        if pending is None:
            continue
        if old is None or decode(pending) != {'digest': old['digest']}:
            raise ValueError('Invalid research publication outbox')
        if old['summary']['projects'] or old['summary']['updated_projects']:
            dispatch_refresh(old['digest'])
        # Uses the existing completeness/material-change gate; no premature deployment.
        from pages_publication import GitHub, request
        request(Path(root), GitHub())
        for attempt in range(3):
            sync(root)
            path = path_for(OUTBOX, name)
            pending = blob(root, revision(root), path, optional=True)
            if pending is None:
                break
            if decode(pending) != {'digest': old['digest']}:
                raise ValueError('Research outbox changed during acknowledgement')
            git(root, 'rm', '--', path)
            git(root, 'commit', '-m', 'Acknowledge research publication ' + name)
            if git(root, 'push', 'origin', 'HEAD:main', check=False).returncode == 0:
                break
        else:
            raise RuntimeError('Research handoff completed; acknowledgement needs retry')
    print(json.dumps({'handoffs_checked': len(events)}))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    pack = commands.add_parser('package')
    pack.add_argument('input', type=Path)
    pack.add_argument('--output', type=Path, required=True)
    pack.add_argument('--cache', type=Path)
    prepare_command = commands.add_parser('prepare')
    prepare_command.add_argument('input', type=Path)
    prepare_command.add_argument('--out', type=Path, required=True)
    prepare_command.add_argument('--root', type=Path, default=Path.cwd())
    prepare_command.add_argument('--baseline')
    prepare_command.add_argument('--cache', type=Path)
    for name in ('publish', 'handoff'):
        command = commands.add_parser(name)
        command.add_argument('--root', type=Path, default=Path.cwd())
        command.add_argument('--result', type=Path, required=True)
        if name == 'publish':
            command.add_argument('--event', default='')
    args = parser.parse_args()
    try:
        if args.command == 'package':
            raw, info = package(decode(args.input.read_bytes()), args.cache)
            args.output.write_bytes(raw)
            print(json.dumps(info))
        elif args.command == 'prepare':
            print(json.dumps(submission_bundle(decode(args.input.read_bytes()), args.root, args.out,
                                                args.baseline, args.cache)))
        elif args.command == 'publish':
            publish(args.root, args.result, args.event or None)
        else:
            handoff(args.root, args.result)
    except (ValueError, OSError, KeyError, TypeError, subprocess.CalledProcessError) as exc:
        parser.exit(1, f'Research submission failed: {exc}\n')


if __name__ == '__main__':
    main()
