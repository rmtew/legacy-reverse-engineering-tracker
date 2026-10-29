"""Offline pinned evidence retrieval, membership and resource bounds."""
import base64
import copy
import tempfile
import unittest
from unittest.mock import patch

import research_evidence as evidence
from research_record import git_blob_sha


class EvidenceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.text = 'exact source\r\nwith Unicode: π\n'
        self.proof = {'repository': 'https://github.com/Owner/Repo', 'commit': 'a' * 40,
                      'path': 'src/file.txt', 'blob': git_blob_sha(self.text)}
        self.document = {'proofs': {'one': self.proof}}
        self.base = 'https://api.github.com/repos/owner/repo/git/'
        self.responses = {
            'commits/' + 'a' * 40: {'sha': 'a' * 40, 'tree': {'sha': 'b' * 40}},
            'trees/' + 'b' * 40: {'sha': 'b' * 40, 'truncated': False, 'tree': [
                {'path': 'src', 'type': 'tree', 'mode': '040000', 'sha': 'c' * 40}]},
            'trees/' + 'c' * 40: {'sha': 'c' * 40, 'truncated': False, 'tree': [
                {'path': 'file.txt', 'type': 'blob', 'mode': '100644', 'sha': self.proof['blob']}]},
            'blobs/' + self.proof['blob']: {'sha': self.proof['blob'], 'size': len(self.text.encode()),
                'encoding': 'base64', 'content': base64.b64encode(self.text.encode()).decode()}}
        self.calls = []

    def fetch(self, url, *, timeout, max_bytes):
        self.assertTrue(0 < timeout <= 30)
        self.assertEqual(max_bytes, evidence.MAX_RESPONSE_BYTES)
        self.assertTrue(url.startswith(self.base))
        self.calls.append(url)
        return copy.deepcopy(self.responses[url.removeprefix(self.base)])

    def hydrate(self):
        return evidence.hydrate(self.document, self.temp.name, self.fetch)

    def test_exact_bytes_and_deduplication(self):
        self.document['proofs']['duplicate'] = {**self.proof, 'text': self.text}
        cache = self.hydrate()
        self.assertEqual(cache.get(self.proof), self.text)
        self.assertEqual(len(self.calls), 4)

    def test_same_blob_at_two_paths_checks_both_paths(self):
        self.document['proofs']['other'] = {**self.proof, 'path': 'src/other.txt'}
        with self.assertRaisesRegex(ValueError, 'not in commit'):
            self.hydrate()

    def test_missing_or_wrong_commit_and_truncated_tree(self):
        for endpoint, field, value in [('commits/' + 'a'*40, 'sha', 'd'*40),
                                       ('trees/' + 'b'*40, 'truncated', True),
                                       ('trees/' + 'b'*40, 'sha', 'd'*40)]:
            original = copy.deepcopy(self.responses)
            self.responses[endpoint][field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                self.hydrate()
            self.responses = original

    def test_reject_symlinks_submodules_and_wrong_blob(self):
        leaf = self.responses['trees/' + 'c'*40]['tree'][0]
        for fields in ({'mode': '120000'}, {'mode': '160000', 'type': 'commit'}, {'sha': 'd'*40}):
            original = leaf.copy()
            leaf.update(fields)
            with self.subTest(fields=fields), self.assertRaisesRegex(ValueError, 'membership mismatch'):
                self.hydrate()
            leaf.clear(); leaf.update(original)

    def test_tampered_blob_non_utf8_size_and_encoding(self):
        blob = self.responses['blobs/' + self.proof['blob']]
        for fields in ({'content': base64.b64encode(b'wrong').decode()},
                       {'content': '/w==', 'size': 1}, {'size': 0},
                       {'encoding': 'none'}, {'size': True}, {'content': '$invalid'}):
            original = blob.copy()
            blob.update(fields)
            with self.subTest(fields=fields), self.assertRaises(ValueError):
                self.hydrate()
            blob.clear(); blob.update(original)

    def test_limits(self):
        for name, value in [('MAX_PROOFS', 0), ('MAX_REQUESTS', 1), ('MAX_SOURCE_BYTES', 1),
                            ('MAX_TOTAL_BYTES', 1), ('MAX_TRANSFER_BYTES', 1),
                            ('MAX_RESPONSE_BYTES', 1), ('MAX_SECONDS', 0)]:
            with self.subTest(limit=name), patch.object(evidence, name, value), self.assertRaises(ValueError):
                self.hydrate()

    def test_manifest_and_inline_hash_checked_before_fetch(self):
        self.document['proofs']['other'] = {**self.proof, 'path': '../escape'}
        with self.assertRaises(ValueError):
            self.hydrate()
        self.assertEqual(self.calls, [])
        self.document['proofs'].pop('other')
        self.proof['text'] = 'tampered'
        with self.assertRaises(ValueError):
            self.hydrate()
        self.assertEqual(self.calls, [])

    def test_network_error_propagates(self):
        with self.assertRaises(OSError):
            evidence.hydrate(self.document, self.temp.name, lambda *a, **k: (_ for _ in ()).throw(OSError('offline')))

    def test_transport_origin_token_timeout_and_response_bound(self):
        from unittest.mock import MagicMock
        response = MagicMock()
        response.read.return_value = b'{}'
        opener = MagicMock()
        opener.open.return_value.__enter__.return_value = response
        with patch.object(evidence, 'build_opener', return_value=opener), patch.dict(evidence.os.environ, {'GITHUB_TOKEN': 'test-only-token'}):
            self.assertEqual(evidence.fetch_json(self.base + 'commits/' + 'a'*40, timeout=7, max_bytes=10), {})
            request = opener.open.call_args.args[0]
            self.assertEqual(request.get_header('Authorization'), 'Bearer test-only-token')
            self.assertEqual(opener.open.call_args.kwargs['timeout'], 7)
            response.read.assert_called_once_with(11)
            for url in ('https://api.github.com.evil/repos/o/r', 'https://elsewhere.example/repos/o/r',
                        'http://api.github.com/repos/o/r'):
                with self.assertRaises(ValueError):
                    evidence.fetch_json(url, timeout=7, max_bytes=10)
            self.assertEqual(opener.open.call_count, 1)
            response.read.return_value = b'x'*11
            with self.assertRaisesRegex(ValueError, 'byte limit'):
                evidence.fetch_json(self.base + 'commits/' + 'a'*40, timeout=7, max_bytes=10)

    def test_transport_rejects_redirect_without_forwarding_auth(self):
        with self.assertRaisesRegex(ValueError, 'redirects'):
            evidence.NoRedirect().redirect_request(None, None, 302, '', {}, 'https://elsewhere.example')


if __name__ == '__main__':
    unittest.main()
