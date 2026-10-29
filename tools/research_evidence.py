"""Bounded, read-only retrieval of immutable research evidence.

Only hydrate unapplied research. The caller owns the temporary directory; none
of these source bytes belong in retained submissions or repository state.
"""
from __future__ import annotations

import base64
import binascii
import json
import os
import time
from urllib.request import HTTPRedirectHandler, Request, build_opener

from research_record import EvidenceCache, git_blob_sha, proof_identity

MAX_PROOFS = 500
MAX_REQUESTS = 500
MAX_RESPONSE_BYTES = 4 * 1024 * 1024
MAX_SOURCE_BYTES = 1024 * 1024
MAX_TOTAL_BYTES = 16 * 1024 * 1024
MAX_TRANSFER_BYTES = 32 * 1024 * 1024
MAX_SECONDS = 300


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise ValueError('Pinned evidence redirects are not permitted')


def fetch_json(url, *, timeout, max_bytes):
    """Fetch a bounded GitHub API response without redirects or token forwarding."""
    if not url.startswith('https://api.github.com/repos/'):
        raise ValueError('Pinned evidence must use the GitHub repository API')
    headers = {'Accept': 'application/vnd.github+json', 'User-Agent': 'tracker-research-evidence'}
    token = os.environ.get('GITHUB_TOKEN')
    if token:
        headers['Authorization'] = 'Bearer ' + token
    with build_opener(NoRedirect()).open(Request(url, headers=headers), timeout=timeout) as response:
        raw = response.read(max_bytes + 1)
    if len(raw) > max_bytes:
        raise ValueError('Pinned evidence response exceeds byte limit')
    return json.loads(raw)


def hydrate(document, directory, fetcher=None):
    """Verify commit/path membership and exact UTF-8 blob bytes into a local cache.

    ``fetcher(url, *, timeout, max_bytes)`` returns a decoded JSON object. Tests
    inject it; production uses the bounded transport above. No upstream code is
    executed. Even an existing local cache does not substitute for membership.
    """
    fetcher = fetcher or fetch_json
    proofs = document.get('proofs', {})
    if not isinstance(proofs, dict) or len(proofs) > MAX_PROOFS:
        raise ValueError('Pinned evidence proof limit exceeded or invalid manifest')
    # Validate every identity and inline hash before any request/cache write.
    identities = []
    locations = {}
    for proof in proofs.values():
        identity = proof_identity(proof)
        location = tuple(identity[k] for k in ('repository', 'commit', 'path'))
        if location in locations and locations[location] != identity['blob']:
            raise ValueError('Conflicting pinned evidence blobs')
        locations[location] = identity['blob']
        if 'text' in proof and git_blob_sha(proof['text']) != identity['blob']:
            raise ValueError('Mismatched inline proof text/blob')
        identities.append(identity)
    cache = EvidenceCache(directory)
    started = time.monotonic()
    requests, total, transferred = 0, 0, 0
    responses, contents, verified = {}, {}, set()

    def get(url):
        nonlocal requests, transferred
        remaining = MAX_SECONDS - (time.monotonic() - started)
        if remaining <= 0:
            raise ValueError('Pinned evidence time limit exceeded')
        if url not in responses:
            if requests >= MAX_REQUESTS:
                raise ValueError('Pinned evidence request limit exceeded')
            requests += 1
            value = fetcher(url, timeout=min(30, remaining), max_bytes=MAX_RESPONSE_BYTES)
            if time.monotonic() - started > MAX_SECONDS:
                raise ValueError('Pinned evidence time limit exceeded')
            if not isinstance(value, dict):
                raise ValueError('Invalid pinned evidence API response')
            # Bound injected transports as well as the production byte reader.
            response_bytes = len(json.dumps(value, ensure_ascii=False).encode('utf-8'))
            if response_bytes > MAX_RESPONSE_BYTES:
                raise ValueError('Pinned evidence response exceeds byte limit')
            transferred += response_bytes
            if transferred > MAX_TRANSFER_BYTES:
                raise ValueError('Pinned evidence transfer byte limit exceeded')
            responses[url] = value
        return responses[url]

    for identity in identities:
        key = tuple(identity.values())
        if key in verified:
            continue
        repo = identity['repository'].removeprefix('https://github.com/')
        base = 'https://api.github.com/repos/' + repo + '/git/'
        commit = get(base + 'commits/' + identity['commit'])
        if commit.get('sha') != identity['commit'] or not isinstance(commit.get('tree'), dict):
            raise ValueError('Mismatched pinned evidence commit')
        tree_sha = commit['tree'].get('sha')
        parts = identity['path'].split('/')
        for index, part in enumerate(parts):
            if not isinstance(tree_sha, str) or len(tree_sha) != 40 or any(c not in '0123456789abcdef' for c in tree_sha):
                raise ValueError('Invalid pinned evidence tree SHA')
            tree = get(base + 'trees/' + tree_sha)
            if tree.get('sha') != tree_sha or tree.get('truncated') is not False or not isinstance(tree.get('tree'), list):
                raise ValueError('Incomplete or mismatched pinned evidence tree')
            matches = [entry for entry in tree['tree'] if isinstance(entry, dict) and entry.get('path') == part]
            if len(matches) != 1:
                raise ValueError('Pinned evidence path is not in commit')
            entry = matches[0]
            if index < len(parts) - 1:
                if entry.get('type') != 'tree' or entry.get('mode') != '040000':
                    raise ValueError('Pinned evidence path traverses a non-tree')
                tree_sha = entry.get('sha')
            elif (entry.get('type') != 'blob' or entry.get('mode') not in {'100644', '100755'}
                  or entry.get('sha') != identity['blob']):
                raise ValueError('Pinned evidence path/blob membership mismatch')
        blob_key = (repo, identity['blob'])
        if blob_key not in contents:
            blob = get(base + 'blobs/' + identity['blob'])
            size = blob.get('size')
            if (blob.get('sha') != identity['blob'] or blob.get('encoding') != 'base64'
                    or type(size) is not int or not 0 <= size <= MAX_SOURCE_BYTES
                    or not isinstance(blob.get('content'), str)):
                raise ValueError('Invalid or oversized pinned evidence blob')
            try:
                raw = base64.b64decode(''.join(blob['content'].split()), validate=True)
                text = raw.decode('utf-8')
            except (ValueError, binascii.Error, UnicodeError) as exc:
                raise ValueError('Pinned evidence is not exact UTF-8 base64') from exc
            if len(raw) != size or git_blob_sha(text) != identity['blob']:
                raise ValueError('Pinned evidence blob hash/size mismatch')
            total += len(raw)
            if total > MAX_TOTAL_BYTES:
                raise ValueError('Pinned evidence total byte limit exceeded')
            contents[blob_key] = text
        cache.put(identity, contents[blob_key])
        verified.add(key)
    return cache
