#!/usr/bin/env python3
"""Regression tests for evidence-only AI co-author tool attribution."""
import copy
import unittest

from collect_activity import coauthor_tools, detect_ai
from refresh_github import update_ai_config


class ConfigurationAttributionTests(unittest.TestCase):
    def test_each_instruction_file_is_context_not_contribution(self):
        for root, github in (([{"name": "CLAUDE.md"}], []),
                             ([{"name": ".claude", "type": "dir"}], []),
                             ([{"name": "CODEX.md"}], []),
                             ([], [{"name": "copilot-instructions.md"}])):
            for usage in (None, False):
                with self.subTest(root=root, github=github, usage=usage):
                    record = {"ai": {"usage": usage, "tools": []}}
                    update_ai_config([record], root, github)
                    self.assertIs(record["ai"]["usage"], usage)
                    self.assertEqual(record["ai"]["tools"], [])
                    self.assertEqual(len(record["ai"]["evidence"]), 1)
                    self.assertIn("does not establish AI contribution", record["ai"]["evidence"][0])

    def test_missing_ai_defaults_to_unknown_only_when_configuration_found(self):
        record = {}
        update_ai_config([record], [{"name": "README.md"}, None], [])
        self.assertEqual(record, {})
        update_ai_config([record], [{"name": "AGENTS.md"}], [])
        self.assertIsNone(record["ai"]["usage"])
        self.assertEqual(record["ai"]["tools"], [])

    def test_configuration_does_not_add_tools_to_verified_generic_usage(self):
        record = {"ai": {"usage": True, "tools": ["Retro Diffusion"],
                         "evidence": ["README credits AI-built examples and Retro Diffusion art"]}}
        update_ai_config([record], [{"name": "CLAUDE.md"}, {"name": "codex.md"}],
                         [{"name": "copilot-instructions.md"}])
        self.assertTrue(record["ai"]["usage"])
        self.assertEqual(record["ai"]["tools"], ["Retro Diffusion"])
        self.assertEqual(record["ai"]["evidence"][0],
                         "README credits AI-built examples and Retro Diffusion art")

    def test_existing_tool_list_never_promotes_unknown_usage(self):
        record = {"ai": {"usage": None, "tools": ["Claude"]}}
        update_ai_config([record], [], [])
        self.assertIsNone(record["ai"]["usage"])
        update_ai_config([record], [{"name": "CLAUDE.md"}], [])
        self.assertIsNone(record["ai"]["usage"])

    def test_repeated_scans_qualify_legacy_context_without_duplicate_evidence(self):
        record = {"ai": {"usage": None, "tools": [],
                         "evidence": ["Claude project instructions/configuration present"]}}
        entries = [{"name": "CLAUDE.md"}, {"name": ".claude"}]
        update_ai_config([record], entries, [])
        expected = copy.deepcopy(record)
        update_ai_config([record], entries, [])
        self.assertEqual(record, expected)
        self.assertEqual(len(record["ai"]["evidence"]), 1)

    def test_actual_attribution_survives_refresh_in_either_order(self):
        commit = {"sha": "abc123", "commit": {
            "message": "Implement feature\n\nCo-authored-by: Claude Code <bot@example.com>"}}
        for config_first in (True, False):
            with self.subTest(config_first=config_first):
                record = {"ai": {"usage": None, "tools": []}}
                if config_first:
                    update_ai_config([record], [{"name": "CLAUDE.md"}], [])
                detect_ai(record, [commit])
                update_ai_config([record], [{"name": "CLAUDE.md"}], [])
                self.assertTrue(record["ai"]["usage"])
                self.assertEqual(record["ai"]["tools"], ["Claude"])
                self.assertTrue(any("abc123; Claude Code" in e for e in record["ai"]["evidence"]))


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


class LinkedBotTests(unittest.TestCase):
    def test_bot_requires_linked_allowlisted_actor_and_preserves_curated_no(self):
        real = {"sha": "a" * 40, "html_url": "https://github.com/owner/repo/commit/" + "a" * 40,
                "author": {"type": "Bot", "login": "copilot-swe-agent[bot]"}, "commit": {"message": "Work"}}
        record = {"ai": {"usage": None, "tools": []}}
        detect_ai(record, [real])
        self.assertTrue(record["ai"]["usage"])
        self.assertEqual(record["ai"]["tools"], ["GitHub Copilot"])
        self.assertIn(real["html_url"], record["ai"]["evidence"][0])
        for author in ({"type": "User", "login": "copilot-swe-agent[bot]"},
                       {"type": "Bot", "login": "someone[bot]"}, {}):
            unknown = {"ai": {"usage": None, "tools": []}}
            detect_ai(unknown, [{**real, "author": author}])
            self.assertIsNone(unknown["ai"]["usage"])
        curated = {"ai": {"usage": False, "tools": []}}
        detect_ai(curated, [real])
        self.assertIs(curated["ai"]["usage"], False)
        self.assertIn(real["html_url"], curated["ai"]["evidence"][0])

    def test_explicit_subject_preserves_curated_no_for_review(self):
        from datetime import datetime, timezone
        from unittest.mock import patch
        import record_project_activity as recorder
        project = {"id": "p", "ai": {"usage": False, "tools": []}}
        event = {"type": "commit", "project_id": "p", "sha": "abc", "title": "Claude fixed the display",
                 "date": "2026-10-19T00:00:00Z"}
        with patch.object(recorder, "CUTOFF", datetime(2000, 1, 1, tzinfo=timezone.utc)):
            recorder.enrich_explicit_ai([project], {"events": [event]})
        self.assertIs(project["ai"]["usage"], False)
        self.assertEqual(project["ai"]["tools"], [])
        self.assertIn("Explicit Claude involvement", project["ai"]["evidence"][0])

    def test_existing_tool_label_alone_never_promotes_usage(self):
        record = {"ai": {"usage": None, "tools": ["Claude"]}}
        detect_ai(record, [{"commit": {"message": "Ordinary work"}}])
        self.assertIsNone(record["ai"]["usage"])


if __name__ == "__main__":
    unittest.main()
