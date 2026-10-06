#!/usr/bin/env python3
"""Regression tests for evidence-only AI co-author tool attribution."""
import copy
import unittest

from collect_activity import coauthor_tools, detect_ai


class CoauthorAttributionTests(unittest.TestCase):
    def test_below_the_root_pi_is_not_chatgpt(self):
        message = "Improve game\n\nCo-Authored-By: Pi (GPT-6 Astra) <noreply@openai.com>"
        record = {"ai": {"usage": None, "tools": []}}
        detect_ai(record, [{"sha": "e53583b9ef05bc116aa897523849c8f8aadcde56",
                            "commit": {"message": message}}])
        self.assertEqual(record["ai"]["tools"], ["Pi"])
        self.assertTrue(record["ai"]["usage"])
        self.assertIn("e53583b9ef05; Pi (GPT-6 Astra)", record["ai"]["evidence"][0])

    def test_provider_or_email_alone_does_not_identify_tool(self):
        for identity in ("OpenAI <noreply@openai.com>", "noreply@openai.com",
                         "Developer <noreply@openai.com>", "Anthropic <noreply@anthropic.com>",
                         "Developer <chatgpt@openai.com>", "<claude@anthropic.com>",
                         "GPT-6 Astra <noreply@openai.com>"):
            with self.subTest(identity=identity):
                self.assertEqual(coauthor_tools("Co-authored-by: " + identity), {})
                record = {"ai": {"usage": None, "tools": []}}
                detect_ai(record, [{"commit": {"message": "Co-authored-by: " + identity}}])
                self.assertEqual(record["ai"], {"usage": None, "tools": []})

    def test_explicit_tools_are_recognized_independent_of_email(self):
        for name, tool in (("ChatGPT", "ChatGPT"), ("Codex (GPT-6)", "Codex"),
                           ("OpenAI Codex", "Codex"), ("Claude Opus 5.5", "Claude"),
                           ("Claude Code", "Claude"), ("Copilot", "GitHub Copilot"),
                           ("GitHub Copilot", "GitHub Copilot"), ("Gemini", "Gemini")):
            with self.subTest(name=name):
                self.assertEqual(coauthor_tools(f"Co-authored-by: {name} <bot@example.com>"),
                                 {tool: name})

    def test_pi_backend_and_model_are_not_mistaken_for_tools(self):
        for name in ("Pi openai-codex/gpt-6-astra", "Pi openai-codex/gpt-5.6-sol",
                     "Pi gpt-6-astra", "Pi (Claude Opus 5.5)"):
            with self.subTest(name=name):
                self.assertEqual(coauthor_tools(f"Co-Authored-By: {name} <noreply@pi.dev>"),
                                 {"Pi": name})

    def test_case_spacing_and_unbracketed_address(self):
        self.assertEqual(coauthor_tools("Work\n\tco-AUTHORED-by:  Codex noreply@openai.com\r\n"),
                         {"Codex": "Codex"})

    def test_multiple_trailers_count_each_tool_once_per_commit(self):
        message = ("Work\nCo-authored-by: Codex <noreply@openai.com>\n"
                   "Co-authored-by: Claude <noreply@anthropic.com>\n"
                   "Co-authored-by: Claude Opus 5 <noreply@anthropic.com>")
        record = {}
        detect_ai(record, [{"sha": "abc", "commit": {"message": message}}])
        self.assertEqual(record["ai"]["tools"], ["Claude", "Codex"])
        self.assertTrue(all(": 1 in this scan" in e for e in record["ai"]["evidence"]))

    def test_prose_and_quoted_examples_are_not_trailers(self):
        for message in ("Explain co-authored-by: ChatGPT <noreply@openai.com>",
                        "> Co-authored-by: Claude <noreply@anthropic.com>",
                        "Co-authored-by: Human <bot@example.com>\nChatGPT helped elsewhere"):
            with self.subTest(message=message):
                self.assertEqual(coauthor_tools(message), {})

    def test_existing_independent_evidence_is_preserved(self):
        record = {"ai": {"usage": True, "tools": ["ChatGPT", "Claude"],
                         "evidence": ["README explicitly credits ChatGPT", "Claude configuration present"]}}
        original = copy.deepcopy(record)
        detect_ai(record, [{"commit": {"message": "Co-authored-by: OpenAI <noreply@openai.com>"}}])
        self.assertEqual(record, original)
        detect_ai(record, [{"commit": {"message": "Co-authored-by: Pi (GPT-6 Astra) <noreply@openai.com>"}}])
        self.assertEqual(record["ai"]["tools"], ["ChatGPT", "Claude", "Pi"])
        self.assertEqual(record["ai"]["evidence"][:2], original["ai"]["evidence"])


if __name__ == "__main__":
    unittest.main()
