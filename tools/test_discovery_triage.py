"""Bounded preflight reads root inventories and case-insensitive README files."""
from __future__ import annotations

import base64
import unittest

from discovery_triage import inventory, triage


class Client:
    def __init__(self):
        self.count, self.max_requests = 0, 2

    def get(self, url):
        self.count += 1
        if url.endswith("/contents"):
            return [{"name": "ReadMe.md", "type": "file"},
                    {"name": "game.bin", "type": "file"},
                    {"name": "src", "type": "dir"}]
        self.last = url
        return {"content": base64.b64encode(b"# A game\nDetails").decode(),
                "html_url": "https://github.com/example/repo/blob/main/ReadMe.md"}


class TriageTests(unittest.TestCase):
    def test_nested_tree_directory_uses_two_ref_pinned_requests(self):
        class DirectoryClient(Client):
            def __init__(self):
                super().__init__()
                self.urls = []

            def get(self, url):
                self.urls.append(url)
                if url.endswith('/contents/Amiga/Tools?ref=master'):
                    self.count += 1
                    return [{'name': 'readme.md', 'type': 'file'},
                            {'name': 'ADFinder', 'type': 'dir'}]
                return super().get(url)

        client = DirectoryClient()
        url = 'https://github.com/example/repo/tree/master/Amiga/Tools'
        lead = triage([(url, {})], client, 1)['leads'][0]
        self.assertEqual(client.count, 2)
        self.assertEqual(client.urls, [
            'https://api.github.com/repos/example/repo/contents/Amiga/Tools?ref=master',
            'https://api.github.com/repos/example/repo/contents/Amiga/Tools/readme.md?ref=master'])
        self.assertEqual(lead['directory_path'], 'Amiga/Tools')
        self.assertEqual(lead['ref'], 'master')
        self.assertEqual(lead['root_names'], ['readme.md', 'ADFinder'])

    def test_readme_surfaces_related_repositories_without_extra_requests(self):
        class RelatedClient(Client):
            def get(self, url):
                if url.endswith('/contents'):
                    return super().get(url)
                self.count += 1
                page = ('Based on https://github.com/parent/original/blob/main/readme.md and '
                        'https://github.com/PARENT/ORIGINAL/tree/main/src; '
                        'CI https://github.com/example/repo/actions')
                return {'content': base64.b64encode(page.encode()).decode(), 'html_url': url}

        report = triage([('https://github.com/example/repo', {})], RelatedClient(), 1)
        self.assertEqual(report['requests'], 2)
        self.assertEqual(report['leads'][0]['related_repositories'],
                         ['https://github.com/parent/original'])
        self.assertEqual(report['leads'][0]['related_repository_count'], 1)

    def test_readme_screens_all_links_locally_beyond_display_cap(self):
        class ManyLinksClient(Client):
            def get(self, url):
                if url.endswith('/contents'):
                    return super().get(url)
                self.count += 1
                body = ' '.join(f'https://github.com/example/project{i}' for i in range(22))
                return {'content': base64.b64encode(body.encode()).decode(), 'html_url': url}

        class Index:
            def screen(self, url):
                return {'status': 'new' if url.endswith('project21') else 'tracked_project'}

        report = triage([('https://github.com/example/repo', {})], ManyLinksClient(), 1, Index())
        lead = report['leads'][0]
        self.assertEqual(report['requests'], 2)
        self.assertEqual(len(lead['related_repositories']), 20)
        self.assertEqual(lead['related_repository_count'], 22)
        self.assertEqual(lead['related_status_counts'], {'new': 1, 'tracked_project': 21})
        self.assertEqual(lead['related_new_repositories'], ['https://github.com/example/project21'])

    def test_redirected_repository_is_screened_from_existing_inventory(self):
        class RedirectedClient(Client):
            def get(self, url):
                self.count += 1
                return [{"name": "source.asm", "type": "file",
                         "html_url": "https://github.com/new-owner/new-repo/blob/main/source.asm"}]

        class Index:
            def screen(self, url):
                self_url = "https://github.com/new-owner/new-repo"
                return {"status": "tracked_project" if url == self_url else "new"}

        client = RedirectedClient()
        lead = triage([("https://github.com/old-owner/old-repo", {})], client, 1, Index())["leads"][0]
        self.assertEqual(client.count, 1)
        self.assertEqual(lead["canonical_repository_url"], "https://github.com/new-owner/new-repo")
        self.assertEqual(lead["canonical_status"], "tracked_project")

    def test_prefers_english_readme_and_surfaces_workbooks(self):
        row = inventory([{'name': n, 'type': 'file'} for n in
                         ('README.de.md', 'README.md', 'a2-hires-lab.xlsm')])
        self.assertEqual(row['readme_path'], 'README.md')
        self.assertEqual(row['root_signals']['analysis_workbooks'], ['a2-hires-lab.xlsm'])
        self.assertFalse(row['root_signals']['binary_files'])
        translated = inventory([{'name': n, 'type': 'file'} for n in
                                ('README.de.md', 'README.en.md')])
        self.assertEqual(translated['readme_path'], 'README.en.md')

    def test_nested_research_hints_use_the_existing_directory_listing(self):
        row = inventory([{'name': name, 'type': 'dir'} for name in
                         ('Kernal ROM Disassembly', 'tools', 'Software', 'screenshots', 'readme')])
        self.assertEqual(row['root_signals']['review_directories'],
                         ['Kernal ROM Disassembly', 'tools', 'Software'])

    def test_index_only_site_exposes_bounded_github_links(self):
        class SiteClient:
            def __init__(self):
                self.count, self.max_requests = 0, 2

            def get(self, url):
                self.count += 1
                if url.endswith('/contents'):
                    return [{'name': 'index.html', 'type': 'file'}]
                self_url = 'https://github.com/example/first'
                html = (f'<a href="{self_url}">one</a><a href="{self_url}/tree/main/src">repeat</a>'
                        '<a href="https://github.com/other/second">two</a>')
                return {'content': base64.b64encode(html.encode()).decode(), 'html_url': url}

        report = triage([('https://github.com/example/site', {})], SiteClient(), 1)
        lead = report['leads'][0]
        self.assertEqual(report['requests'], 2)
        self.assertIsNone(lead['readme_path'])
        self.assertEqual(lead['outbound_repository_count'], 2)
        self.assertEqual(lead['outbound_repositories'],
                         ['https://github.com/example/first', 'https://github.com/other/second'])

    def test_release_artifacts_keep_tool_and_source_visible(self):
        row = inventory([{'name': n, 'type': 'file'} for n in
                         ('README.md', 'MAD-example.6502', 'machine-auto-detect.ssd',
                          'machine-auto-detect.uef', 'max65.vsix')])
        self.assertTrue(row['root_signals']['source_files'])
        self.assertTrue(row['root_signals']['binary_files'])
        self.assertEqual(len(row['root_signals']['release_artifacts']), 3)
        self.assertNotIn('decision', row)

    def test_case_insensitive_readme_and_bounded_root_signals(self):
        client = Client()
        report = triage([("https://github.com/example/repo", {"origins": []})], client, 1)
        lead = report["leads"][0]
        self.assertEqual(report["requests"], 2)
        self.assertEqual(lead["readme_path"], "ReadMe.md")
        self.assertTrue(client.last.endswith("/contents/ReadMe.md"))
        self.assertIn("# A game", lead["readme_intro"])
        self.assertTrue(lead["root_signals"]["binary_files"])
        self.assertFalse(lead["root_signals"]["source_files"])
        self.assertEqual(lead["root_signals"]["source_directories"], ["src"])
        self.assertNotIn("decision", lead)


if __name__ == "__main__":
    unittest.main()
