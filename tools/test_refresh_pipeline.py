"""Bounded collection and durable offline refresh/recovery contracts."""

import copy
from contextlib import ExitStack, redirect_stdout
from datetime import datetime, timedelta, timezone
from io import BytesIO, StringIO
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from urllib.error import HTTPError
from urllib.parse import parse_qs, urlsplit

import refresh_pipeline as pipeline
from catalogue_storage import encode, load_projects, load_dataset, write_all, write_projects
from merge_pending_projects import new_audit
from record_project_activity import snapshot
from refresh_scope import check_publishable

NOW = datetime(2026, 10, 19, tzinfo=timezone.utc)
SHA = "a" * 40


def project(pid="a", **extra):
    return {
        "id": pid,
        "title": pid,
        "upstream_name": pid,
        "display_title": pid,
        "subjects": [pid],
        "repo": "https://github.com/owner/" + pid,
        "record_class": "subject",
        "target_kinds": ["game"],
        "work_kinds": [],
        "tool_kinds": [],
        "github": {
            "repository": "owner/" + pid,
            "default_branch": "main",
            "tracking_branch": "main",
            "languages": ["C"],
            "latest_commit": {"sha": SHA, "date": "2026-10-18"},
        },
        "last_activity": "2026-10-18",
        **extra,
    }


def commit(index):
    return {
        "sha": f"{index:040x}",
        "html_url": f"https://github.com/owner/a/commit/{index:040x}",
        "commit": {"message": f"Commit {index}", "committer": {"date": "2026-10-18T12:00:00Z"}},
    }


class Response(BytesIO):
    status = 200
    headers = {}


class Network:
    def __init__(self):
        self.calls, self.time, self.delay = [], 0, 0
        self.pages, self.empty, self.failure = {}, False, None

    def clock(self):
        return self.time

    def open(self, request, timeout):
        url = request.full_url
        self.calls.append((url, timeout))
        self.time += self.delay
        path = urlsplit(url).path
        query = parse_qs(urlsplit(url).query)
        if self.failure and self.failure in path:
            raise HTTPError(url, 429, "Rate limited", {}, BytesIO(b"secondary rate limit"))
        if path.endswith("/branches"):
            value = [] if self.empty else [{"name": "main", "commit": {"sha": SHA}}]
        elif "/branches/" in path:
            raise HTTPError(url, 404, "Not Found", {}, BytesIO())
        elif path.endswith("/commits"):
            value = self.pages.get(int(query.get("page", ["1"])[0]), [])
        elif path.endswith("/releases/latest"):
            raise HTTPError(url, 404, "Not Found", {}, BytesIO())
        elif path.count("/") == 3 and path.startswith("/repos/"):
            value = {
                "default_branch": "main",
                "pushed_at": "2026-10-18T00:00:00Z",
                "updated_at": "2026-10-18T00:00:00Z",
                "archived": False,
            }
        else:
            raise AssertionError("Unexpected request: " + url)
        return Response(encode(value))


class RefreshPipelineTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "repo"
        self.root.mkdir()
        (self.root / "state").mkdir()
        self.bundle_path = Path(self.temp.name) / "bundle.json"
        self.net = Network()
        self.stack = ExitStack()
        self.addCleanup(self.stack.close)
        self.stack.enter_context(redirect_stdout(StringIO()))
        for module in (pipeline.probe, pipeline.activity):
            self.stack.enter_context(patch.object(module, "REQUEST_DELAY", 0))
        self.seed([project("a"), project("b"), project("c")])

    def seed(self, records, poll=None):
        write_all(
            self.root / "data",
            {
                "projects.json": records,
                "project-audits.json": {"projects": [new_audit(p["id"]) for p in records]},
                "discovery-sources.json": {"sources": [], "backlog": []},
                "discovery-decisions.json": {"indexed_at": "2026-10-19", "decisions": []},
                "research-activity.json": {"events": []},
            },
        )
        self.put("data/pending-projects.json", [])
        self.put(
            "data/activity.json", {"generated_at": pipeline.stamp(NOW), "window_days": 180, "events": []}
        )
        self.put(
            "state/project-catalog-state.json",
            {"version": 1, "projects": {p["id"]: snapshot(p) for p in records}, "removed": {}},
        )
        self.put(pipeline.POLL, {"version": 1, "repositories": poll or {}})

    def put(self, name, value):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(encode(value))

    def read(self, name):
        return json.loads((self.root / name).read_bytes())

    def bytes(self):
        return {str(p.relative_to(self.root)): p.read_bytes() for p in self.root.rglob("*.json")}

    def collect(
        self,
        *,
        limit=500,
        requests=1000,
        seconds=600,
        now=NOW,
        full=False,
        continuation="",
        request_id="test",
    ):
        self.bundle_path.unlink(missing_ok=True)
        budget = pipeline.Budget(seconds, requests, api_requests=requests, clock=self.net.clock)
        result = pipeline.collect(
            self.root,
            self.bundle_path,
            budget,
            limit=limit,
            full=full,
            request_id=request_id,
            continuation=continuation,
            now=now,
            opener=self.net.open,
        )
        self.assertLessEqual(result.get("summary", {}).get("repositories", 0), limit)
        self.assertLessEqual(budget.requests, requests)
        return result

    def apply(self, bundle, now=NOW):
        return pipeline.apply_bundle(self.root, bundle, now=now)

    def activity_only(self, **state):
        self.seed(
            [project()],
            {
                "owner/a": {
                    "project_ids": ["a"],
                    "next_probe_due_at": "2026-10-20T00:00:00Z",
                    "last_probe_at": pipeline.stamp(NOW),
                    "scan_requested": True,
                    **state,
                }
            },
        )

    def test_results_and_both_queues_commit_together_and_resume_finite_cycle(self):
        before = self.bytes()
        batch = self.collect(limit=1, full=True)
        self.assertEqual(before, self.bytes())
        self.assertEqual(batch["summary"]["completed"], {"probe": 1, "activity": 1})
        first = self.apply(batch)
        self.assertTrue(first["continue"])
        self.assertEqual(first["remaining"], {"probe": 2, "activity": 2})
        records = load_projects(self.root / "data/projects.json")
        self.assertIn("checked_at", next(p for p in records if p["id"] == "a")["github"])
        for index in range(2):
            batch = self.collect(
                limit=1, full=True, continuation=first["token"], now=NOW + timedelta(minutes=index + 1)
            )
            self.assertNotIn("owner/a", [r["repo"] for r in batch["results"]])
            first = self.apply(batch)
        self.assertFalse(first["continue"])
        self.assertEqual(first["completed"], {"probe": 3, "activity": 3})
        self.assertFalse(first["active"])
        # An identical full request cannot restart the completed sweep.
        done = self.collect(full=True)
        self.assertEqual(done["summary"]["repositories"], 0)
        self.assertFalse(self.apply(done)["continue"])

    def test_zero_requests_does_not_mark_repositories_failed_or_spin(self):
        batch = self.collect(requests=0, full=True)
        self.assertEqual(batch["results"], [])
        self.assertEqual(batch["progress_after"]["retry"], {"probe": {}, "activity": {}})
        self.apply(batch)
        again = self.collect(requests=0, full=True, now=NOW + timedelta(minutes=1))
        self.assertFalse(self.apply(again)["published"])
        self.assertFalse(self.apply(again)["continue"])

    def test_wall_exhaustion_rolls_back_incomplete_unit(self):
        self.net.delay = 2
        batch = self.collect(seconds=1, full=True)
        self.assertEqual(batch["summary"]["completed"], {"probe": 0, "activity": 0})
        self.assertEqual(batch["progress_after"]["retry"], {"probe": {}, "activity": {}})
        self.assertTrue(all(t <= 1 for _, t in self.net.calls))
        self.assertFalse(any(r["outcomes"] for r in batch["results"]))

    def test_shared_request_budget_reserves_activity_work(self):
        self.activity_only()
        self.net.pages[1] = [commit(1)]
        batch = self.collect(requests=1)
        self.assertEqual(batch["summary"]["requests"], 1)
        self.assertEqual(batch["summary"]["completed"]["activity"], 0)
        self.apply(batch)
        self.assertIn("refresh_activity", self.read(pipeline.POLL)["repositories"]["owner/a"])
        batch = self.collect(requests=1, now=NOW + timedelta(minutes=1))
        self.apply(batch)
        self.assertEqual(batch["summary"]["completed"]["activity"], 1)
        self.assertEqual(len(self.read("data/activity.json")["events"]), 1)

    def test_pinned_paginated_history_resumes_without_fetching_previous_pages(self):
        self.activity_only(scan_reason="backfill")
        self.net.pages = {1: [commit(i) for i in range(100)], 2: [commit(101)]}
        first = self.collect(requests=2)
        self.assertEqual(first["summary"]["completed"]["activity"], 0)
        self.apply(first)
        cursor = self.read(pipeline.POLL)["repositories"]["owner/a"]["refresh_activity"]
        self.assertEqual(cursor["queries"][0]["page"], 2)
        self.assertEqual(len(self.read("data/activity.json")["events"]), 100)
        self.net.calls = []
        second = self.collect(
            requests=1,
            continuation=pipeline.token(pipeline.progress_read(self.root)),
            now=NOW + timedelta(minutes=1),
        )
        self.apply(second)
        self.assertEqual(len(self.net.calls), 1)
        self.assertIn("page=2", self.net.calls[0][0])
        self.assertIn("sha=" + SHA, self.net.calls[0][0])
        self.assertEqual(len(self.read("data/activity.json")["events"]), 101)
        self.assertNotIn("refresh_activity", self.read(pipeline.POLL)["repositories"]["owner/a"])

    def test_offline_retry_duplicate_bundle_and_stale_continuation(self):
        batch = self.collect(limit=1, full=True)
        before = self.bytes()
        with patch.object(pipeline, "validate", side_effect=SystemExit("validation interrupted")):
            with self.assertRaises(SystemExit):
                self.apply(batch)
        self.assertEqual(self.bytes(), before)
        with patch.object(pipeline, "perform", side_effect=AssertionError("No network during replay")):
            first = self.apply(batch)
            after = self.bytes()
            duplicate = self.apply(batch)
        self.assertTrue(duplicate["duplicate"])
        self.assertEqual(duplicate["continue"], first["eligible"])
        self.assertEqual(after, self.bytes())
        self.net.calls = []
        stale = self.collect(continuation=first["token"] + "-old")
        self.assertTrue(stale["stale"])
        self.assertEqual(self.net.calls, [])
        self.assertFalse(self.apply(stale)["continue"])

    def test_stale_progress_baseline_does_not_overwrite_newer_state(self):
        batch = self.collect(limit=1, full=True)
        self.apply(batch)
        other = copy.deepcopy(batch)
        other["id"] = "other"
        before = self.bytes()
        self.assertTrue(self.apply(other)["stale"])
        self.assertEqual(before, self.bytes())

    def test_concurrent_authored_or_generated_edits_are_preserved_and_requeued(self):
        for field in ("notes", "github"):
            with self.subTest(field=field):
                (self.root / pipeline.PROGRESS).unlink(missing_ok=True)
                self.seed([project()])
                batch = self.collect(full=True)
                records = load_projects(self.root / "data/projects.json")
                records[0][field] = "Human edit" if field == "notes" else {"stars": 987}
                write_projects(self.root / "data/projects.json", records)
                result = self.apply(batch)
                self.assertEqual(result["conflicts"], ["owner/a"])
                self.assertEqual(load_projects(self.root / "data/projects.json")[0][field], records[0][field])
                self.assertIn("owner/a", pipeline.progress_read(self.root)["cycle"]["pending"]["probe"])

    def test_pending_placeholders_and_publication_gate_survive_partial_batch(self):
        self.seed([project()])
        self.put("data/pending-projects.json", [project("new")])
        batch = self.collect(full=True, limit=1)
        self.assertEqual(self.read("data/pending-projects.json")[0]["id"], "new")
        self.apply(batch)
        self.assertEqual(self.read("data/pending-projects.json"), [])
        self.assertEqual({p["id"] for p in load_projects(self.root / "data/projects.json")}, {"a", "new"})
        self.assertEqual(
            {a["project_id"] for a in load_dataset(self.root / "data", "project-audits.json")["projects"]},
            {"a", "new"},
        )
        with self.assertRaises(SystemExit):
            check_publishable(
                self.read(pipeline.POLL),
                load_projects(self.root / "data/projects.json"),
                self.read("state/project-catalog-state.json"),
            )

    def test_rate_stop_persists_completed_units_and_stops_until_reset(self):
        self.activity_only()
        self.net.failure = "/commits"
        batch = self.collect(requests=20)
        self.assertIn("blocked_until", batch["progress_after"])
        result = self.apply(batch)
        self.assertFalse(result["continue"])
        self.assertIn("refresh_activity", self.read(pipeline.POLL)["repositories"]["owner/a"])
        self.net.calls = []
        self.collect(now=NOW + timedelta(minutes=1))
        self.assertEqual(self.net.calls, [])

    def test_empty_repo_finishes_and_missing_configured_branch_does_not(self):
        self.activity_only()
        self.net.empty = True
        batch = self.collect(requests=20)
        self.assertEqual(batch["summary"]["completed"]["activity"], 1)
        self.apply(batch)
        self.assertFalse(self.read(pipeline.POLL)["repositories"]["owner/a"]["scan_requested"])
        (self.root / pipeline.PROGRESS).unlink()
        self.activity_only()
        records = load_projects(self.root / "data/projects.json")
        records[0]["github_branch"] = "missing"
        write_projects(self.root / "data/projects.json", records)
        # Keep the catalogue snapshot current to isolate tracked-branch behavior.
        self.put("state/project-catalog-state.json", {"projects": {"a": snapshot(records[0])}})
        self.net.empty = False
        batch = self.collect(requests=20)
        self.assertEqual(batch["summary"]["completed"]["activity"], 0)
        self.assertIn("retry_at", batch["progress_after"]["retry"]["activity"]["owner/a"])

    def test_both_lanes_advance_under_one_small_shared_budget(self):
        batch = self.collect(requests=4, full=True)
        self.assertLessEqual(batch["summary"]["requests"], 4)
        self.assertGreater(batch["summary"]["completed"]["probe"], 0)
        self.assertGreater(batch["summary"]["units"]["activity"], 0)
        self.assertGreater(batch["summary"]["lanes"]["probe"], 0)
        self.assertGreater(batch["summary"]["lanes"]["activity"], 0)

    def test_permanent_failure_is_deferred_without_blocking_future_healthy_cycles(self):
        self.seed([project("a"), project("b")])
        original = pipeline.perform

        def fail_one(repo, work, *args, **kwargs):
            if repo == "owner/a" and work == "probe":
                raise ValueError("Repository unavailable")
            return original(repo, work, *args, **kwargs)

        with patch.object(pipeline, "perform", side_effect=fail_one):
            first = self.collect(full=True)
        published = self.apply(first)
        self.assertFalse(published["active"])
        self.assertFalse(published["continue"])
        self.assertEqual(published["completed"]["probe"], 1)
        self.assertEqual(published["deferred"]["probe"], 1)
        self.assertEqual(published["retry_pending"]["probe"], 1)
        self.assertIn("owner/a", pipeline.progress_read(self.root)["retry"]["probe"])
        with patch.object(pipeline, "perform", side_effect=fail_one):
            second = self.collect(now=NOW + timedelta(hours=1), request_id="next-hour")
        self.assertIn("owner/b", [r["repo"] for r in second["results"]])
        self.assertEqual(second["summary"]["completed"]["probe"], 1)
        self.apply(second, NOW + timedelta(hours=1))

    def test_failed_required_probe_defers_dependent_history_and_keeps_gate_closed(self):
        self.seed([project()])
        self.put("data/pending-projects.json", [project("new")])
        original = pipeline.perform

        def fail_new(repo, work, *args, **kwargs):
            if repo == "owner/new" and work == "probe":
                raise ValueError("Unavailable")
            return original(repo, work, *args, **kwargs)

        with patch.object(pipeline, "perform", side_effect=fail_new):
            batch = self.collect(full=True)
        result = self.apply(batch)
        self.assertFalse(result["active"])
        self.assertEqual(result["deferred"], {"probe": 1, "activity": 1})
        with self.assertRaises(SystemExit):
            check_publishable(
                self.read(pipeline.POLL),
                load_projects(self.root / "data/projects.json"),
                self.read("state/project-catalog-state.json"),
            )

    def test_actual_distinct_repository_ceiling_and_shared_roots(self):
        records = [project(f"p{i:04}") for i in range(502)]
        records.append(project("shared", repo=records[0]["repo"]))
        self.seed(records)
        visited = set()

        def work(repo, lane, records, rs, events, budget, now, *args):
            visited.add(repo)
            if lane == "probe":
                rs = {**rs, "last_probe_at": pipeline.stamp(now)}
            return records, rs, events, True, {}

        with patch.object(pipeline, "perform", side_effect=work):
            batch = self.collect(limit=500, full=True)
        self.assertEqual(len(visited), 500)
        self.assertEqual(batch["summary"]["repositories"], 500)
        self.assertEqual(len(batch["progress_after"]["cycle"]["pending"]["probe"]), 2)
        self.assertEqual(len(batch["progress_after"]["cycle"]["pending"]["activity"]), 2)

    def test_full_request_upgrades_active_adaptive_cycle(self):
        records = [project("a"), project("b")]
        poll = {"repositories": {"owner/a": {}, "owner/b": {"next_probe_due_at": "2026-10-20T00:00:00Z"}}}
        first = pipeline.plan(pipeline.progress_read(self.root), records, poll, NOW, "adaptive")
        self.assertEqual(first["cycle"]["pending"]["probe"], ["owner/a"])
        full = pipeline.plan(first, records, poll, NOW, "full", True)
        self.assertEqual(set(full["cycle"]["pending"]["probe"]), {"owner/a", "owner/b"})
        self.assertEqual(set(full["cycle"]["pending"]["activity"]), {"owner/a", "owner/b"})

    def test_oldest_work_receives_capacity_under_publication_priority(self):
        records = [project(str(i)) for i in range(20)]
        poll = {
            "repositories": {f"owner/{i}": {"publication": {"metadata_complete": False}} for i in range(19)}
        }
        progress = pipeline.plan(pipeline.progress_read(self.root), records, poll, NOW, "fair", True)
        candidates = pipeline.candidates(progress, poll, "probe", NOW, 4)
        self.assertIn("owner/19", candidates[:4])


if __name__ == "__main__":
    unittest.main()
