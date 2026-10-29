#!/usr/bin/env python3
"""Remove redundant proof bodies from retained, already-applied submissions.

Receipts deliberately continue to identify the original input blob in Git history,
not the compact archive representation. No catalogue, report or receipt is edited.
"""
from pathlib import Path
import argparse
import hashlib
import json

from catalogue_storage import encode
from research_record import review_digest
from research_submission import INBOX, RECEIPTS, checked, checked_receipt, decode, git


def compact(root, *, write=False):
    root = Path(root)
    changes = []
    proofs = 0
    for path in sorted((root / INBOX).glob('*.json')):
        raw = path.read_bytes()
        document = decode(raw)
        if not any('text' in proof for proof in document.get('proofs', {}).values()):
            continue
        event, digest = checked(document, path.stem)
        receipt = checked_receipt(decode((root / RECEIPTS / path.name).read_bytes()), event)
        if receipt['digest'] != digest:
            raise ValueError('Archive differs from applied review: ' + event)
        original = git(root, 'cat-file', 'blob', receipt['input_blob']).stdout
        original_document = decode(original)
        if (checked(original_document, event)[1] != digest
                or hashlib.sha1(b'blob ' + str(len(original)).encode() + b'\0' + original).hexdigest() != receipt['input_blob']):
            raise ValueError('Original receipt input is not recoverable: ' + event)
        report = (root / f'docs/research/{event}.md').read_bytes()
        if hashlib.sha256(report).hexdigest() != receipt['report_sha256']:
            raise ValueError('Report differs from applied receipt: ' + event)
        for proof in document.get('proofs', {}).values():
            if 'text' in proof:
                del proof['text']
                proofs += 1
        assert review_digest(document) == digest
        checked(document, event)
        changes.append((path, raw, encode(document)))
    # Validate the entire migration before writing; fail closed on unique or
    # unverifiable evidence. Re-running after compaction makes no changes.
    if write:
        try:
            for path, _, raw in changes:
                path.write_bytes(raw)
        except OSError:
            for path, raw, _ in changes:
                path.write_bytes(raw)
            raise
    before = sum(len(old) for _, old, _ in changes)
    after = sum(len(new) for _, _, new in changes)
    return {'submissions': len(changes), 'proof_bodies': proofs,
            'before_bytes': before, 'after_bytes': after, 'saved_bytes': before - after,
            'written': write}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path.cwd())
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    print(json.dumps(compact(args.root, write=args.write)))
