#!/usr/bin/env python3
"""Retain collected evidence in Actions artifacts; acknowledge replay atomically in Git."""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
from pathlib import Path
import re
import subprocess
import zipfile

from catalogue_storage import encode
from enrichment_pipeline import apply_bundle, PublicationPending
from research_submission import git, revision, sync, blob

STATE = 'state/enrichment-publication.json'
ARTIFACT = 'enrichment-bundle'
SOURCE = '.github/workflows/enrich-evidence.yml'
MAX_PAGES = 4
MAX_RUNS = 8
MAX_BUNDLES = 4
MAX_ZIP = 16 * 1024 * 1024
MAX_BUNDLE = 32 * 1024 * 1024


def number(value):
    if type(value) is not int or value < 1:
        raise ValueError('Invalid Actions artifact/run identifier')
    return value


def checkpoint(root):
    raw = blob(root, revision(root), STATE, optional=True)
    value = json.loads(raw) if raw is not None else {'version': 1, 'artifact_id': 0}
    if value.get('version') != 1 or type(value.get('artifact_id')) is not int or value['artifact_id'] < 0:
        raise ValueError('Invalid enrichment publication checkpoint')
    return value


class GitHub:
    def __init__(self, repository=None):
        self.repository = repository or os.environ['GITHUB_REPOSITORY']
        if not re.fullmatch(r'[\w.-]+/[\w.-]+', self.repository):
            raise ValueError('Invalid enrichment repository')
        self.runs = {}

    def get(self, endpoint):
        result = subprocess.run(['gh', 'api', f'repos/{self.repository}/{endpoint}'], check=True,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=30)
        return json.loads(result.stdout)

    def trusted(self, artifact):
        run_id = (artifact.get('workflow_run') or {}).get('id')
        if type(run_id) is not int or run_id < 1:
            return False
        if run_id not in self.runs:
            if len(self.runs) >= MAX_RUNS:
                raise ValueError('Retained enrichment source inspection ceiling reached')
            self.runs[run_id] = self.get(f'actions/runs/{run_id}')
        run = self.runs[run_id]
        return (run.get('path', '').split('@')[0] == SOURCE
                and (run.get('repository') or {}).get('full_name', '').casefold() == self.repository.casefold()
                and (run.get('head_repository') or {}).get('full_name', '').casefold() == self.repository.casefold()
                and run.get('head_branch') == 'main'
                and run.get('event') in {'push', 'schedule', 'workflow_dispatch'})

    def pending(self, after):
        pending, previous = [], None
        for page in range(1, MAX_PAGES + 1):
            rows = self.get(f'actions/artifacts?name={ARTIFACT}&per_page=100&page={page}')['artifacts']
            for artifact in rows:
                identity = number(artifact['id'])
                # GitHub lists newest artifact IDs first. Fail closed if this
                # ordering changes; never advance past an unexamined bundle.
                if previous is not None and identity >= previous:
                    raise ValueError('Unexpected Actions artifact order; investigate before collecting')
                previous = identity
                if identity <= after:
                    return sorted(pending, key=lambda a: a['id'])
                if artifact.get('name') != ARTIFACT or not self.trusted(artifact):
                    continue
                if artifact.get('expired'):
                    raise ValueError('Unpublished enrichment artifact expired; operator review required')
                if not 0 < artifact.get('size_in_bytes', 0) <= MAX_ZIP:
                    raise ValueError('Retained enrichment archive exceeds the bounded size')
                pending.append(artifact)
            if len(rows) < 100:
                return sorted(pending, key=lambda a: a['id'])
        raise ValueError('Retained enrichment scan ceiling reached; no work was discarded')

    def download(self, artifact):
        identity = number(artifact['id'])
        result = subprocess.run(['gh', 'api', f'repos/{self.repository}/actions/artifacts/{identity}/zip'],
                                check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=60)
        raw = result.stdout
        if len(raw) > MAX_ZIP:
            raise ValueError('Retained enrichment archive exceeds the bounded size')
        digest = artifact.get('digest')
        if digest and digest != 'sha256:' + hashlib.sha256(raw).hexdigest():
            raise ValueError('Retained enrichment artifact digest mismatch')
        return unpack(raw)


def unpack(raw):
    if len(raw) > MAX_ZIP:
        raise ValueError('Oversized enrichment archive')
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        entries = archive.infolist()
        if (len(entries) != 1 or entries[0].filename != 'enrichment-bundle.json'
                or entries[0].is_dir() or entries[0].file_size > MAX_BUNDLE
                or entries[0].flag_bits & 1 or (entries[0].external_attr >> 16) & 0o170000 == 0o120000):
            raise ValueError('Enrichment artifact must contain exactly one bounded JSON bundle')
        with archive.open(entries[0]) as handle:
            payload = handle.read(MAX_BUNDLE + 1)
    if len(payload) > MAX_BUNDLE:
        raise ValueError('Oversized enrichment bundle')
    document = json.loads(payload)
    if not isinstance(document, dict) or document.get('version') != 1 or not isinstance(document.get('results'), list):
        raise ValueError('Invalid retained enrichment bundle')
    return payload, document


def publish(root, client):
    """Replay bounded retained work; metadata waits leave the artifact unacknowledged."""
    root = Path(root)
    if git(root, 'status', '--porcelain').stdout.strip():
        raise ValueError('Enrichment publication requires a clean dedicated checkout')
    sync(root)
    candidates = client.pending(checkpoint(root)['artifact_id'])
    published, handled = False, []
    for artifact in candidates[:MAX_BUNDLES]:
        payload, bundle = client.download(artifact)  # Once per bundle, never once per push retry.
        for attempt in range(3):
            sync(root)
            if checkpoint(root)['artifact_id'] >= artifact['id']:
                published = True
                handled.append(artifact['id'])
                break  # A push succeeded before its response was lost.
            try:
                summary = apply_bundle(root, bundle)
            except PublicationPending:
                return {'published': published, 'handled': handled, 'waiting_metadata': True,
                        'retained_artifact': artifact['id']}
            state = {'version': 1, 'artifact_id': number(artifact['id']),
                     'run_id': number(artifact['workflow_run']['id']),
                     'bundle_sha256': hashlib.sha256(payload).hexdigest(),
                     'accepted': len(summary['accepted']), 'conflicts': len(summary['conflicts'])}
            (root / STATE).parent.mkdir(parents=True, exist_ok=True)
            (root / STATE).write_bytes(encode(state))
            git(root, 'add', '-A', '--', 'data/projects.index.json', 'data/projects/', 'data/activity.json',
                'state/project-catalog-state.json', 'state/enrichment-state.json', STATE)
            git(root, 'commit', '-m', 'Publish retained enrichment artifact ' + str(artifact['id']))
            if git(root, 'push', 'origin', 'HEAD:main', check=False).returncode == 0:
                published = True
                handled.append(artifact['id'])
                break
        else:
            raise RuntimeError('Retained enrichment lost three fast-forward races; next wake-up resumes it')
    return {'published': published, 'handled': handled, 'waiting_metadata': False}


def output(values):
    print(json.dumps(values, separators=(',', ':')))
    if path := os.environ.get('GITHUB_OUTPUT'):
        with open(path, 'a') as handle:
            for key in ('published', 'collect'):
                if key in values:
                    handle.write(f'{key}={str(values[key]).lower()}\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=('collect-allowed', 'publish'))
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        client = GitHub()
        if args.command == 'collect-allowed':
            sync(args.root)
            pending = client.pending(checkpoint(args.root)['artifact_id'])
            output({'collect': not bool(pending), 'retained_pending': len(pending)})
        else:
            output(publish(args.root, client))
    except (OSError, ValueError, KeyError, TypeError, zipfile.BadZipFile, subprocess.SubprocessError) as exc:
        parser.exit(1, f'Retained enrichment failed: {exc}\n')


if __name__ == '__main__':
    main()
