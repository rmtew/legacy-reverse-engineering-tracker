import copy
from datetime import datetime, timezone
from io import BytesIO
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from urllib.error import HTTPError

import wikidata_games as wd


STAMP = "2026-11-05T19:00:00Z"


def game(qid="Q1", title="Example", platforms=("Amiga",), aliases=(), **kw):
    return {"qid": qid, "label": title, "aliases": list(aliases),
            "platforms": [{"qid": "Q" + str(100 + i), "label": label} for i, label in enumerate(platforms)],
            "release_dates": ["1991-01-01T00:00:00Z"], "lemon_amiga": ["123"], "lemon64": [], "moby": ["456"], **kw}


def index(games=None, subjects=("Example",)):
    return {"format": wd.INDEX_FORMAT, "complete": True, "generated_at": STAMP,
            "source": {"subjects": list(subjects), "subjects_sha256": wd.subjects_fingerprint(subjects)},
            "games": [game()] if games is None else games}


def project(pid="p", subjects=("Example",), platforms=("Amiga",), **kw):
    return {"id": pid, "subjects": list(subjects), "source_platforms": list(platforms),
            "record_class": "subject", "target_kinds": ["game"], **kw}


def override(subject="Example", qid="Q1", reason="Reviewed item identity"):
    return {"format": wd.OVERRIDE_FORMAT, "projects": {"p": {subject: {"qid": qid, "reason": reason}}}}


def binding(qid, kind=None, value=None, platform=None):
    result = {"item": {"type": "uri", "value": "http://www.wikidata.org/entity/" + qid}}
    if kind is not None:
        result.update(kind={"type": "literal", "value": kind}, value={"type": "literal", "value": value})
    if platform:
        result["platform"] = {"type": "uri", "value": "http://www.wikidata.org/entity/" + platform}
    return result


class MatchingTests(unittest.TestCase):
    def resolve(self, projects=None, idx=None, overrides=None):
        return wd.project_game_links(projects or [project()], idx or index(), overrides, generated_at=STAMP)

    def test_exact_title_platform_ids_and_provenance(self):
        links, review = self.resolve()
        self.assertEqual(links["projects"]["p"], [{"subject": "Example", "qid": "Q1", "match": "exact-title-platform", "evidence": "https://www.wikidata.org/wiki/Q1", "lemon_amiga": "123", "lemon64": None, "moby": "456"}])
        self.assertEqual(review["subjects"], [])

    def test_alias_and_equivalent_platform(self):
        links, _ = self.resolve([project(subjects=("Alias",), platforms=("Commodore Amiga",))], index([game(aliases=["Alias"])], subjects=["Alias"]))
        self.assertEqual(links["projects"]["p"][0]["qid"], "Q1")

    def test_case_punctuation_normalization_is_not_fuzzy(self):
        links, _ = self.resolve([project(subjects=("example!",))], index(subjects=["example!"]))
        self.assertIn("p", links["projects"])
        links, review = self.resolve([project(subjects=("Example 2",))], index(subjects=["Example 2"]))
        self.assertEqual(links["projects"], {})
        self.assertEqual(review["subjects"][0]["status"], "unmatched")

    def test_multiple_games_and_aliases_keep_subject_association(self):
        p = project(subjects=("Example", "Second"))
        links, _ = self.resolve([p], index([game(), game("Q2", "Second")], subjects=p["subjects"]))
        self.assertEqual([v["qid"] for v in links["projects"]["p"]], ["Q1", "Q2"])

    def test_same_name_same_platform_is_ambiguous(self):
        links, review = self.resolve(idx=index([game(), game("Q2")]))
        self.assertFalse(links["projects"])
        self.assertEqual(review["subjects"][0]["status"], "ambiguous")
        self.assertEqual(review["subjects"][0]["candidate_count"], 2)

    def test_known_platform_conflict_can_disambiguate(self):
        links, _ = self.resolve(idx=index([game(), game("Q2", platforms=["Commodore 64"])]))
        self.assertEqual(links["projects"]["p"][0]["qid"], "Q1")

    def test_unknown_other_platform_does_not_silently_disambiguate(self):
        links, review = self.resolve(idx=index([game(), game("Q2", platforms=[])]))
        self.assertFalse(links["projects"])
        self.assertEqual(review["subjects"][0]["status"], "ambiguous")

    def test_missing_platforms_are_not_matches(self):
        for p, idx in [(project(platforms=[]), index()), (project(), index([game(platforms=[])]))]:
            links, review = self.resolve([p], idx)
            self.assertFalse(links["projects"])
            self.assertEqual(review["subjects"][0]["status"], "missing-platform-evidence")

    def test_mismatched_platforms_are_distinguished(self):
        links, review = self.resolve([project(platforms=["Commodore 64"])])
        self.assertFalse(links["projects"])
        self.assertEqual(review["subjects"][0]["status"], "conflicting-evidence")
        self.assertEqual(review["subjects"][0]["candidates"][0]["reason"], "platform-mismatch")

    def test_target_platform_is_not_source_platform(self):
        links, _ = self.resolve([project(platforms=[], target_platforms=["Amiga"])])
        self.assertFalse(links["projects"])

    def test_explicit_release_year_only_refines_matching(self):
        links, _ = self.resolve([project(subjects=["Example (1991)"])], index(subjects=["Example (1991)"]))
        self.assertIn("p", links["projects"])
        links, review = self.resolve([project(subjects=["Example (1992)"])], index(subjects=["Example (1992)"]))
        self.assertFalse(links["projects"])
        self.assertEqual(review["subjects"][0]["candidates"][0]["reason"], "release-year-mismatch")
        links, _ = self.resolve([project(re_started="1992")])
        self.assertIn("p", links["projects"])

    def test_application_tooling_and_engine_only_records_excluded(self):
        for changes in [{"target_kinds": ["application"]}, {"record_class": "tooling"}, {"record_class": None}, {"target_kinds": ["game-engine"]}]:
            links, _ = self.resolve([project(**changes)])
            self.assertFalse(links["projects"])
        links, _ = self.resolve([project(record_class="hybrid")])
        self.assertIn("p", links["projects"])

    def test_new_subject_after_collection_waits_for_refresh(self):
        links, review = self.resolve([project(subjects=["Alias"])], index([game(aliases=["Alias"])]))
        self.assertFalse(links["projects"])
        self.assertEqual(review["subjects"][0]["status"], "not-indexed")

    def test_manual_match_exclusion_and_missing_item_preserved(self):
        links, _ = self.resolve(idx=index([game(), game("Q2")]), overrides=override(qid="Q2"))
        self.assertEqual(links["projects"]["p"][0]["match"], "manual")
        links, review = self.resolve(overrides=override(qid=None))
        self.assertFalse(links["projects"])
        self.assertEqual(review["subjects"][0]["status"], "excluded")
        links, review = self.resolve(overrides=override(qid="Q999"))
        self.assertEqual(links["projects"]["p"][0]["qid"], "Q999")
        self.assertIsNone(links["projects"]["p"][0]["moby"])
        self.assertIn("absent", review["subjects"][0]["warning"])

    def test_stale_override_retained_and_reported(self):
        value = override(subject="Removed")
        original = copy.deepcopy(value)
        _, review = self.resolve(overrides=value)
        self.assertEqual(value, original)
        self.assertEqual(review["subjects"][0]["status"], "stale-override")

    def test_multiple_external_ids_are_not_arbitrarily_selected(self):
        links, review = self.resolve(idx=index([game(moby=["123", "456"])]))
        self.assertIsNone(links["projects"]["p"][0]["moby"])
        self.assertIn("Multiple", review["subjects"][0]["warning"])

    def test_invalid_identifiers_and_overrides_rejected(self):
        for value in ["Q0", "javascript:bad", "Q1/x"]:
            with self.assertRaises(ValueError):
                self.resolve(overrides=override(qid=value))
        with self.assertRaises(ValueError):
            self.resolve(idx=index([game(moby=["//bad"])]))
        with self.assertRaises(ValueError):
            self.resolve(overrides=override(reason=""))


class CollectionTests(unittest.TestCase):
    def fake_query(self, query):
        if "SELECT DISTINCT" in query:
            return [binding("Q1")]
        return [binding("Q1", "label", "Example"), binding("Q1", "alias", "Other name"), binding("Q1", "platform", "Amiga", "Q100"), binding("Q1", "released", "1991-01-01T00:00:00Z"), binding("Q1", "moby", "123")]

    def test_bounded_queries_and_fact_collection(self):
        value = wd.collect_index(self.fake_query, ["Example"], generated_at=STAMP)
        self.assertEqual(value["games"][0]["moby"], ["123"])
        self.assertEqual(value["games"][0]["platforms"], [{"qid": "Q100", "label": "Amiga"}])
        query = wd.item_query(['Example "name"'])
        self.assertIn('"Example \\"name\\""@en', query)
        self.assertNotIn("OFFSET", query)
        self.assertIn("LIMIT 1001", query)
        self.assertIn("P11688", query)
        self.assertIn("skos:altLabel", query)

    def test_query_timeouts_split_batches(self):
        calls = []
        def query(text):
            calls.append(text)
            if "SELECT DISTINCT" in text and '"Second"' in text and '"Example"' in text:
                raise HTTPError(wd.ENDPOINT, 504, "timeout", {}, BytesIO())
            return self.fake_query(text)
        value = wd.collect_index(query, ["Example", "Second"])
        self.assertEqual(len(value["games"]), 1)
        self.assertGreater(len(calls), 2)

    def test_cap_and_detail_failures_fail_closed(self):
        with self.assertRaises(ValueError):
            wd.collect_index(lambda _: [binding("Q1")] * 1001, ["Example"])
        with self.assertRaises(ValueError):
            wd.collect_index(self.fake_query, ["Example", "Other"], page_size=1, max_pages=1)
        with self.assertRaises(ValueError):
            wd.collect_index(lambda q: [binding("Q1")] if "SELECT DISTINCT" in q else [], ["Example"])

    def test_empty_scoped_index_is_valid(self):
        value = wd.collect_index(lambda _: [], ["Unindexed homebrew"])
        self.assertEqual(value["games"], [])

    def test_foreign_details_and_bad_uri_rejected(self):
        with self.assertRaises(ValueError):
            wd.collect_index(lambda q: [binding("Q1")] if "SELECT DISTINCT" in q else [binding("Q2", "moby", "123")], ["Example"])
        with self.assertRaises(ValueError):
            wd.item_id("https://bad.example/Q1")

    def test_explicit_qid_fetch_does_not_require_title_hit(self):
        seen = []
        def query(text):
            seen.append(text)
            self.assertIn("wd:Q99", text)
            return [binding("Q99", "label", "Unrelated title"), binding("Q99", "moby", "789")]
        value = wd.collect_index(query, [], explicit_qids=["Q99"])
        self.assertEqual(value["games"][0]["moby"], ["789"])
        self.assertEqual(len(seen), 1)

    def test_multilingual_labels_and_platforms_are_retained(self):
        def query(text):
            if "SELECT DISTINCT" in text:
                self.assertIn('"Example"@mul', text)
                return [binding("Q1")]
            self.assertIn('"mul"', text)
            return [binding("Q1", "label-mul", "Example"), binding("Q1", "platform", "Commodore Amiga", "Q100047"), binding("Q1", "moby", "123")]
        value = wd.collect_index(query, ["Example"])
        links, _ = wd.project_game_links([project()], value)
        self.assertEqual(links["projects"]["p"][0]["qid"], "Q1")

    def test_english_label_preferred_with_multilingual_alias_retained(self):
        for facts in [[binding("Q1", "label", "English"), binding("Q1", "label-mul", "Shared")],
                      [binding("Q1", "label-mul", "Shared"), binding("Q1", "label", "English")]]:
            value = wd.collect_index(lambda q: [binding("Q1")] if "SELECT DISTINCT" in q else facts + [binding("Q1", "moby", "123")], ["English"])
            self.assertEqual(value["games"][0]["label"], "English")
            self.assertIn("Shared", value["games"][0]["aliases"])


class FilesystemTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        wd.atomic_json(self.root / "data/projects.json", [project()])
        wd.atomic_json(self.root / "state/wikidata-index.json", index())

    def test_matching_idempotent_and_offline(self):
        with patch.object(wd, "urlopen", side_effect=AssertionError("Offline matching used network")):
            wd.match(self.root)
            paths = [self.root / "data/game-links.json", self.root / "state/wikidata-review.json"]
            before = [p.read_bytes() for p in paths]
            with patch.object(wd, "now_text", return_value="2027-01-01T00:00:00Z"):
                wd.match(self.root)
            self.assertEqual(before, [p.read_bytes() for p in paths])

    def test_refresh_failure_preserves_cache_and_links(self):
        wd.match(self.root)
        paths = [self.root / "state/wikidata-index.json", self.root / "data/game-links.json"]
        before = [p.read_bytes() for p in paths]
        with self.assertRaises(OSError):
            wd.refresh(self.root, force=True, query=lambda _: (_ for _ in ()).throw(OSError("offline")))
        self.assertEqual(before, [p.read_bytes() for p in paths])

    def test_cache_reuse_and_subject_change_invalidation(self):
        fresh = index()
        fresh["generated_at"] = datetime.now(timezone.utc).isoformat()
        wd.atomic_json(self.root / "state/wikidata-index.json", fresh)
        def no_network(_):
            raise AssertionError("Unexpected query")
        self.assertEqual(wd.refresh(self.root, query=no_network)["status"], "cached")
        wd.atomic_json(self.root / "data/projects.json", [project(subjects=["New"])] )
        with self.assertRaises(AssertionError):
            wd.refresh(self.root, query=no_network)

    def test_bad_override_does_not_replace_published_links(self):
        wd.match(self.root)
        before = (self.root / "data/game-links.json").read_bytes()
        wd.atomic_json(self.root / "config/wikidata-overrides.json", override(qid="bad"))
        with self.assertRaises(ValueError):
            wd.match(self.root)
        self.assertEqual(before, (self.root / "data/game-links.json").read_bytes())

    def test_atomic_serialization_failure_leaves_old_file(self):
        path = self.root / "test.json"
        wd.atomic_json(path, {"value": 1})
        with self.assertRaises(ValueError):
            wd.atomic_json(path, {"value": float("nan")})
        self.assertEqual(wd.read_json(path), {"value": 1})

    def test_new_subjects_incremental_and_full_refresh_age_preserved(self):
        fresh = index()
        stamp = datetime.now(timezone.utc).isoformat()
        fresh["generated_at"] = stamp
        wd.atomic_json(self.root / "state/wikidata-index.json", fresh)
        wd.atomic_json(self.root / "data/projects.json", [project(subjects=["Example", "Second"])])
        queries = []
        def query(text):
            queries.append(text)
            self.assertNotIn('"Example"@en', text)
            if "SELECT DISTINCT" in text:
                return [binding("Q2")]
            return [binding("Q2", "label", "Second"), binding("Q2", "moby", "789")]
        summary = wd.refresh(self.root, query=query)
        value = wd.read_json(self.root / "state/wikidata-index.json")
        self.assertEqual(summary["status"], "incremental")
        self.assertEqual(summary["queried_subjects"], 1)
        self.assertEqual([g["qid"] for g in value["games"]], ["Q1", "Q2"])
        self.assertEqual(value["source"]["full_refresh_at"], stamp)
        self.assertEqual(value["source"]["subjects"], ["Example", "Second"])

    def test_override_qid_changes_invalidate_cache_and_fetch_details(self):
        fresh = index()
        fresh["generated_at"] = datetime.now(timezone.utc).isoformat()
        wd.atomic_json(self.root / "state/wikidata-index.json", fresh)
        wd.atomic_json(self.root / "config/wikidata-overrides.json", override(qid="Q9"))
        def query(text):
            self.assertNotIn("SELECT DISTINCT", text)
            self.assertIn("wd:Q9", text)
            return [binding("Q9", "label", "Other title"), binding("Q9", "moby", "999")]
        summary = wd.refresh(self.root, query=query)
        self.assertEqual(summary["queried_subjects"], 0)
        self.assertEqual(summary["queried_manual_qids"], 1)
        wd.match(self.root)
        link = wd.read_json(self.root / "data/game-links.json")["projects"]["p"][0]
        self.assertEqual(link["qid"], "Q9")
        self.assertEqual(link["moby"], "999")

    def test_identical_refresh_does_not_republish_links_or_reviews(self):
        wd.match(self.root)
        paths = [self.root / "data/game-links.json", self.root / "state/wikidata-review.json"]
        before = [p.read_bytes() for p in paths]
        refreshed = index()
        refreshed["generated_at"] = "2027-01-01T00:00:00Z"
        wd.atomic_json(self.root / "state/wikidata-index.json", refreshed)
        wd.match(self.root)
        self.assertEqual(before, [p.read_bytes() for p in paths])


if __name__ == "__main__":
    unittest.main()
