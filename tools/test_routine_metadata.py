"""Scoped deterministic observations, conservative promotions and provenance."""
import copy
import unittest
import enrich_evidence as evidence
import routine_metadata as routine


class RoutineMetadataTests(unittest.TestCase):
    def scan(self, text, path='games/demo/README.md'):
        return routine.scan(text, 'owner/repo', 'a' * 40, path, evidence)

    def test_unsafe_and_excessive_scopes_are_rejected(self):
        for path in ('../other', 'game/../other', 'game//other', 'game\\other', '/'.join(['x'] * 33)):
            with self.subTest(path=path), self.assertRaises(ValueError):
                routine.instruction_paths(path)

    def test_positive_generic_and_named_disclosures_but_not_mentions_plans_or_negation(self):
        for text, expected in [('This project was developed using Claude Code.', 'Claude'),
                               ('AI-assisted coding', 'Unspecified AI'), ('We used ChatGPT.', 'ChatGPT')]:
            with self.subTest(text=text):
                auto = self.scan(text)
                self.assertEqual(auto['ai_use'][0]['value'], expected)
                self.assertIn('/blob/' + 'a' * 40 + '/', auto['ai_use'][0]['url'])
        for text in ['```text\nWe used Claude.\n```', '> We used Claude.', 'Claude is supported.', 'We never used Claude.', 'Can I use ChatGPT?',
                     'We plan to build with Codex.', 'No AI-generated code.', 'Built without Claude.']:
            with self.subTest(text=text):
                self.assertEqual(self.scan(text)['ai_use'], [])

    def test_instruction_scope_and_presence_stay_unknown(self):
        paths = routine.instruction_paths('games/demo')
        self.assertIn('AGENTS.md', paths)
        self.assertIn('games/CLAUDE.md', paths)
        self.assertIn('games/demo/AGENTS.md', paths)
        self.assertFalse(any('vendor' in p or 'sibling' in p for p in paths))
        auto = self.scan('Instructions for coding agents.', 'games/demo/AGENTS.md')
        record = {'ai': {'usage': None, 'tools': []}}
        routine.apply(record, auto)
        self.assertIsNone(record['ai']['usage'])
        self.assertEqual(auto['ai_config'][0]['strength'], 'supporting')
        self.assertNotIn('OpenAI Codex', record['ai']['tools'])
        inherited = routine.scan('We used Claude.\nTarget CPU: Z80', 'owner/repo', 'a' * 40,
                                 'AGENTS.md', evidence, context_only=True)
        self.assertFalse(inherited['ai_use'])
        self.assertFalse(inherited['target_cpu'])

    def test_explicit_declarations_only_fill_unknown_and_preserve_variants(self):
        auto = self.scan('Source CPU: Z80\nTarget CPU: 68020\nTarget platform: Amiga AGA')
        record = {'source_cpu': ['6502'], 'target_cpu': [], 'notes': 'Curated', 'title': 'Keep'}
        routine.apply(record, auto)
        self.assertEqual({k: v for k, v in record.items() if k != 'evidence'},
                         {'source_cpu': ['6502'], 'target_cpu': ['68020'],
                          'target_platforms': ['Amiga AGA'], 'notes': 'Curated', 'title': 'Keep'})
        self.assertIn('/blob/' + 'a' * 40, record['evidence']['routine']['target_cpu'][0]['url'])
        conflicting = self.scan('Target CPU: 68000\nTarget CPU: 68020\nCFLAGS=-m68040\nRequires 68060')
        other = {}
        routine.apply(other, conflicting)
        self.assertNotIn('target_cpu', other)

    def test_ai_preserves_curated_no_and_persistent_first_source(self):
        auto = self.scan('The project was written with Claude.')
        record = {'ai': {'usage': False, 'tools': [], 'evidence': ['Curated non-use claim']}}
        routine.apply(record, auto)
        self.assertIs(record['ai']['usage'], False)
        self.assertIn('Curated non-use claim', record['ai']['evidence'])
        self.assertEqual(len(record['ai']['evidence']), 2)
        record['ai']['usage'] = None
        routine.apply(record, auto)
        self.assertIs(record['ai']['usage'], True)
        self.assertEqual(record['ai']['tools'], ['Claude'])
        once = copy.deepcopy(record)
        auto['ai_use'][0]['url'] = auto['ai_use'][0]['url'].replace('a' * 40, 'b' * 40)
        routine.apply(record, auto)
        self.assertEqual(once, record)
