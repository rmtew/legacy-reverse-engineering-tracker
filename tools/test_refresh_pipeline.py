"""Bounded collection and durable offline refresh/recovery contracts."""

import copy
from contextlib import ExitStack, redirect_stdout, redirect_stderr
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
import pages_publication as pages
import research_submission as submission
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
        elif path.endswith("/languages"):
            value = {"C": 100}
        elif path.endswith("/contents"):
            value = []
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

    def research(self, added=(), updated=(), index=1):
        digest = f"{index:064x}"
        event = "research-" + str(index)
        self.put(submission.path_for(submission.RECEIPTS, event), {
            "version": 1, "event_id": event, "digest": digest, "input_blob": SHA,
            "summary": {"projects": list(added), "updated_projects": list(updated)},
        })
        return "research-" + digest

    def assert_publication_handoff(self, applied):
        with patch.object(pages, "request", return_value={"requested": True}) as request:
            result = pages.request_after_refresh(
                self.root, object(), result="success",
                continuation=str(applied["continue"]).lower(), handoff="success",
            )
        self.assertEqual(request.called, not applied["continue"])
        self.assertEqual(result["requested"], not applied["continue"])

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
        self.assert_publication_handoff(first)
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
        self.assert_publication_handoff(first)
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
        stale = self.apply(other)
        self.assertTrue(stale["stale"])
        self.assert_publication_handoff(stale)
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
                self.assert_publication_handoff(result)
                self.assertEqual(result["conflicts"], ["owner/a"])
                self.assertEqual(load_projects(self.root / "data/projects.json")[0][field], records[0][field])
                self.assertIn("owner/a", pipeline.progress_read(self.root)["cycle"]["pending"]["probe"])

    def test_pending_placeholders_and_publication_gate_survive_partial_batch(self):
        self.seed([project()])
        self.put("data/pending-projects.json", [project("new"), project("later")])
        batch = self.collect(full=True, limit=1)
        self.assertEqual(self.read("data/pending-projects.json")[0]["id"], "new")
        self.apply(batch)
        self.assertEqual(self.read("data/pending-projects.json"), [])
        self.assertEqual({p["id"] for p in load_projects(self.root / "data/projects.json")}, {"a", "new", "later"})
        self.assertEqual(
            {a["project_id"] for a in load_dataset(self.root / "data", "project-audits.json")["projects"]},
            {"a", "new", "later"},
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
        self.assert_publication_handoff(result)
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

    def test_completed_publication_marker_never_resets_incremental_history(self):
        self.activity_only(
            publication={"metadata_complete": True, "history_complete": True, "reset_project_ids": ["a"]}
        )
        old = pipeline.activity.event_from_commit("a", "owner/a", commit(1))
        old["branches"] = ["main"]
        self.put(
            "data/activity.json", {"generated_at": pipeline.stamp(NOW), "window_days": 180, "events": [old]}
        )
        self.net.pages = {1: [commit(2)]}
        self.apply(self.collect())
        self.assertEqual(
            {e["sha"] for e in self.read("data/activity.json")["events"]},
            {commit(1)["sha"], commit(2)["sha"]},
        )

    def test_empty_changed_tracking_resets_old_history_before_completion(self):
        self.activity_only(
            publication={"metadata_complete": True, "history_complete": False, "reset_project_ids": ["a"]}
        )
        old = pipeline.activity.event_from_commit("a", "owner/a", commit(1))
        old["branches"] = ["main"]
        self.put(
            "data/activity.json", {"generated_at": pipeline.stamp(NOW), "window_days": 180, "events": [old]}
        )
        self.net.empty = True
        result = self.apply(self.collect())
        self.assertEqual(result["completed"]["activity"], 1)
        self.assertEqual(self.read("data/activity.json")["events"], [])
        self.assertTrue(
            self.read(pipeline.POLL)["repositories"]["owner/a"]["publication"]["history_complete"]
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

    def test_research_additions_and_updates_do_not_start_unrelated_due_work(self):
        records = load_projects(self.root / "data/projects.json")
        records[1]["notes"] = "Reviewed update"
        write_projects(self.root / "data/projects.json", records)
        self.put("data/pending-projects.json", [project("new")])
        request = self.research(added=["new"], updated=["b"])
        batch = self.collect(request_id=request)
        self.assertEqual({r["repo"] for r in batch["results"]}, {"owner/b", "owner/new"})
        self.assertEqual(batch["summary"]["completed"], {"probe": 2, "activity": 2})
        self.assertEqual(batch["progress_after"]["cycle"]["mode"], "research")
        self.assertTrue(all("/owner/a" not in url and "/owner/c" not in url for url, _ in self.net.calls))
        self.assertFalse(self.apply(batch)["continue"])
        check_publishable(self.read(pipeline.POLL), load_projects(self.root / "data/projects.json"),
                          self.read("state/project-catalog-state.json"))

    def test_research_continuations_recovery_and_duplicate_keep_scope(self):
        request = self.research(added=["a", "b", "a"], updated=["b"])
        first = self.collect(request_id=request, limit=1)
        self.assertEqual(first["progress_after"]["cycle"]["targets"]["probe"], ["owner/a", "owner/b"])
        with patch.object(pipeline, "perform", side_effect=AssertionError("Replay must stay offline")):
            applied = self.apply(first)
            replayed = self.apply(first)
        self.assertTrue(applied["continue"])
        self.assertTrue(replayed["duplicate"])
        self.assertEqual(replayed["token"], applied["token"])
        second = self.collect(request_id=request, continuation=applied["token"], limit=1,
                              now=NOW + timedelta(minutes=1))
        self.assertEqual({r["repo"] for r in second["results"]}, {"owner/b"})
        self.assertFalse(self.apply(second)["continue"])
        self.net.calls = []
        repeated = self.collect(request_id=request, now=NOW + timedelta(days=1))
        self.assertEqual(repeated["summary"]["repositories"], 0)
        self.assertEqual(self.net.calls, [])
        self.assertFalse(self.apply(repeated)["continue"])
        stale = self.collect(request_id=request, continuation=applied["token"])
        self.assertTrue(stale["stale"])
        self.assertEqual(self.net.calls, [])

    def test_research_duplicate_after_unrelated_cycle_does_not_restart_due_sweep(self):
        request = self.research(added=["a"])
        self.apply(self.collect(request_id=request))
        ordinary = self.collect(request_id="scheduled", now=NOW + timedelta(days=1))
        self.assertEqual({r["repo"] for r in ordinary["results"]}, {"owner/a", "owner/b", "owner/c"})
        self.apply(ordinary, NOW + timedelta(days=1))
        self.net.calls = []
        repeated = self.collect(request_id=request, now=NOW + timedelta(days=2))
        self.assertEqual(repeated["summary"]["repositories"], 0)
        self.assertEqual(self.net.calls, [])

    def test_research_request_coalesces_without_restarting_active_maintenance(self):
        first = self.apply(self.collect(limit=1))
        progress = pipeline.progress_read(self.root)
        progress["retry"]["activity"]["owner/c"] = {"retry_at": "2026-10-20T00:00:00Z"}
        self.put(pipeline.PROGRESS, progress)
        poll = self.read(pipeline.POLL)
        poll["repositories"].setdefault("owner/c", {})["refresh_activity"] = {"cursor": "retained"}
        self.put(pipeline.POLL, poll)
        self.put("data/pending-projects.json", [project("new")])
        request = self.research(added=["new"])
        batch = self.collect(request_id=request, limit=1, now=NOW + timedelta(minutes=1))
        after = batch["progress_after"]
        self.assertEqual(after["cycle"]["id"], first["cycle"])
        self.assertEqual(after["cycle"]["mode"], "adaptive")
        self.assertEqual(set(after["cycle"]["targets"]["probe"]), {"owner/a", "owner/b", "owner/c", "owner/new"})
        self.assertEqual(set(after["cycle"]["pending"]["probe"]), {"owner/b", "owner/c"})
        self.assertNotIn("owner/a", {r["repo"] for r in batch["results"]})
        self.assertEqual(after["retry"]["activity"]["owner/c"], progress["retry"]["activity"]["owner/c"])
        self.apply(batch)
        self.assertEqual(self.read(pipeline.POLL)["repositories"]["owner/c"]["refresh_activity"], {"cursor": "retained"})

    def test_new_research_request_joins_active_research_cycle(self):
        first_request = self.research(added=["a", "b"])
        first = self.apply(self.collect(request_id=first_request, limit=1))
        second_request = self.research(updated=["c"], index=2)
        joined = self.collect(request_id=second_request, requests=0)
        self.assertEqual(joined["progress_after"]["cycle"]["id"], first["cycle"])
        self.assertEqual(joined["progress_after"]["cycle"]["pending"]["probe"], ["owner/b", "owner/c"])
        self.assertEqual(joined["progress_after"]["research_requests"], [first_request, second_request])

    def test_research_edit_requeues_completed_repo_without_replacing_active_sweep(self):
        first = self.apply(self.collect(limit=1))
        original = pipeline.progress_read(self.root)["cycle"]
        self.assertEqual(original["pending"]["probe"], ["owner/b", "owner/c"])
        self.assertNotIn("owner/a", original["pending"]["activity"])
        records = load_projects(self.root / "data/projects.json")
        records[0]["notes"] = "New research after this repository completed"
        write_projects(self.root / "data/projects.json", records)
        request = self.research(updated=["a"])
        queued = self.collect(request_id=request, requests=0, now=NOW + timedelta(minutes=1))
        cycle = queued["progress_after"]["cycle"]
        self.assertEqual(cycle["id"], first["cycle"])
        self.assertEqual(cycle["mode"], "adaptive")
        self.assertEqual(cycle["targets"]["probe"], original["targets"]["probe"])
        for work in ("probe", "activity"):
            self.assertEqual(cycle["pending"][work], original["pending"][work] + ["owner/a"])
        row = next(row for row in queued["results"] if row["repo"] == "owner/a")
        self.assertFalse(row["state_after"]["publication"]["metadata_complete"])
        self.assertFalse(row["state_after"]["publication"]["history_complete"])
        applied = self.apply(queued)
        refreshed = self.collect(request_id=request, continuation=applied["token"], limit=1,
                                 now=NOW + timedelta(minutes=2))
        self.assertEqual({row["repo"] for row in refreshed["results"]}, {"owner/a"})
        self.assertEqual(refreshed["summary"]["completed"], {"probe": 1, "activity": 1})
        self.assertEqual(refreshed["progress_after"]["cycle"]["pending"], original["pending"])
        self.assertTrue(self.apply(refreshed)["continue"])

    def test_pending_catalogue_work_joins_scope_without_all_due_repositories(self):
        self.put("data/pending-projects.json", [project("unrelated-new")])
        request = self.research(added=["a"])
        batch = self.collect(request_id=request, requests=0)
        queues = batch["progress_after"]["cycle"]["pending"]
        self.assertEqual(set(queues["probe"]), {"owner/a", "owner/unrelated-new"})
        self.assertIn("owner/unrelated-new", queues["activity"])
        applied = self.apply(batch)
        self.assertTrue(applied["continue"])
        self.assertEqual(self.read("data/pending-projects.json"), [])

    def test_concurrent_catalogue_change_during_research_replay_is_retained(self):
        request = self.research(added=["a"])
        batch = self.collect(request_id=request)
        records = load_projects(self.root / "data/projects.json")
        records[1]["notes"] = "Concurrent authored update"
        write_projects(self.root / "data/projects.json", records)
        applied = self.apply(batch)
        progress = pipeline.progress_read(self.root)
        self.assertEqual(progress["cycle"]["pending"]["probe"], ["owner/b"])
        self.assertEqual(progress["cycle"]["pending"]["activity"], ["owner/b"])
        self.assertTrue(applied["continue"])
        self.assertNotIn("owner/c", progress["cycle"]["targets"]["probe"])

    def test_research_resume_uses_changed_repo_and_prunes_removed_target(self):
        request = self.research(added=["a", "b"])
        applied = self.apply(self.collect(request_id=request, limit=1))
        records = load_projects(self.root / "data/projects.json")
        records[1]["repo"] = "https://github.com/Changed/B.git/"
        write_projects(self.root / "data/projects.json", records)
        batch = self.collect(request_id=request, continuation=applied["token"], requests=0)
        self.assertEqual(batch["progress_after"]["cycle"]["pending"]["probe"], ["Changed/B"])
        self.assertNotIn("owner/b", batch["progress_after"]["cycle"]["targets"]["probe"])
        applied = self.apply(batch)
        self.seed([project("a"), project("c")], poll=self.read(pipeline.POLL)["repositories"])
        self.net.calls = []
        removed = self.collect(request_id=request, continuation=applied["token"])
        self.assertEqual(removed["summary"]["repositories"], 0)
        self.assertEqual(removed["progress_after"]["cycle"]["pending"], {"probe": [], "activity": []})
        self.assertEqual(self.net.calls, [])

    def test_empty_non_github_or_removed_research_scope_never_falls_back_to_due(self):
        self.seed([project("a"), project("web", repo="https://example.org/source")])
        request = self.research(added=["gone"], updated=["web"])
        batch = self.collect(request_id=request)
        self.assertEqual(batch["summary"]["repositories"], 0)
        self.assertEqual(batch["progress_after"]["cycle"]["targets"], {"probe": [], "activity": []})
        self.assertEqual(self.net.calls, [])
        self.assertFalse(self.apply(batch)["continue"])

    def test_missing_invalid_or_conflicting_research_request_fails_before_network(self):
        for request in ("research-", "research-" + "f" * 64):
            with self.subTest(request=request), self.assertRaises(ValueError):
                self.collect(request_id=request)
            self.assertEqual(self.net.calls, [])
            self.assertFalse(self.bundle_path.exists())
        request = self.research(added=["a"])
        with self.assertRaisesRegex(ValueError, "full sweep"):
            self.collect(request_id=request, full=True)
        self.assertEqual(self.net.calls, [])

    def test_bounded_research_history_late_duplicate_still_stays_scoped(self):
        records = [project("a"), project("b")]
        poll = {"repositories": {}}
        progress = pipeline.progress_read(self.root)
        first = "research-" + "0" * 64
        with patch.object(pipeline, "RESEARCH_REQUEST_HISTORY", 2):
            for index in range(3):
                request = "research-" + f"{index:064x}"
                progress = pipeline.plan(progress, records, poll, NOW, request, research_repositories=set())
            self.assertEqual(len(progress["research_requests"]), 2)
            self.assertNotIn(first, progress["research_requests"])
            late = pipeline.plan(progress, records, poll, NOW, first, research_repositories={"owner/a"})
        self.assertEqual(late["cycle"]["pending"]["probe"], ["owner/a"])

    def unavailable_source_fixture(self, status=404, healthy=False):
        rows = [project('a', last_checked='2026-10-17')]
        if healthy:
            rows.append(project('b'))
        states = {p['github']['repository']: {
            'last_probe_at': pipeline.stamp(NOW - timedelta(days=1)),
            'project_ids': [p['id']], 'default_branch': 'main',
            'last_deep_scan': pipeline.stamp(NOW - timedelta(days=1)),
            'last_deep_scan_project_ids': [p['id']],
        } for p in rows}
        self.seed(rows, states)
        prior = copy.deepcopy(rows[0])
        rows[0]['title'] = 'Existing reviewed classification update'
        write_projects(self.root / 'data/projects.json', rows)
        normal = self.net.open
        def unavailable(request, timeout):
            if urlsplit(request.full_url).path == '/repos/owner/a':
                self.net.calls.append((request.full_url, timeout))
                raise HTTPError(request.full_url, status, 'Unavailable', {}, BytesIO(b'not found'))
            return normal(request, timeout)
        self.net.open = unavailable
        return prior, normal

    def test_root_404_resolves_existing_attempt_honestly_and_replays_idempotently(self):
        prior, _ = self.unavailable_source_fixture()
        old = pipeline.activity.event_from_commit("a", "owner/a", commit(1))
        old["branches"] = ["main"]
        old.pop("message")  # Canonical history omits a message identical to the title.
        self.put("data/activity.json", {"generated_at": pipeline.stamp(NOW), "window_days": 180, "events": [old]})
        batch = self.collect()
        self.assertEqual(batch['summary']['completed'], {'probe': 0, 'activity': 0})
        self.assertEqual(len(self.net.calls), 1)  # No dependent history or missing-file probes.
        self.apply(batch)
        actual = load_projects(self.root / 'data/projects.json')[0]
        gh = copy.deepcopy(actual['github']); availability = gh.pop('source_availability')
        self.assertEqual(gh, prior['github'])
        self.assertEqual(availability, {'status': 'unavailable', 'http_status': 404, 'retryable': True})
        self.assertEqual(actual['last_checked'], prior['last_checked'])
        self.assertEqual(actual['last_activity'], prior['last_activity'])
        self.assertEqual([e for e in self.read('data/activity.json')['events'] if e.get('sha')], [old])
        rs = self.read(pipeline.POLL)['repositories']['owner/a']
        self.assertEqual(rs['last_probe_at'], pipeline.stamp(NOW - timedelta(days=1)))
        self.assertEqual(rs['last_deep_scan'], pipeline.stamp(NOW - timedelta(days=1)))
        self.assertFalse(rs['publication']['metadata_complete'])
        self.assertFalse(rs['publication']['history_complete'])
        self.assertEqual(rs['publication']['outcome'], 'source-unavailable')
        self.assertNotIn('_repository_lookup_status', rs)
        self.assertEqual(rs['repository_availability']['retry_at'], pipeline.stamp(NOW + timedelta(days=1)))
        check_publishable(self.read(pipeline.POLL), [actual], self.read('state/project-catalog-state.json'))
        before = self.bytes(); self.apply(batch); self.assertEqual(self.bytes(), before)

    def test_public_availability_schema_rejects_false_or_ambiguous_status(self):
        self.unavailable_source_fixture(); self.apply(self.collect())
        rows = load_projects(self.root / 'data/projects.json')
        for invalid in ({"status": "removed", "http_status": 404, "retryable": True},
                        {"status": "unavailable", "http_status": 403, "retryable": True},
                        {"status": "unavailable", "http_status": 404, "retryable": False},
                        {"status": "unavailable", "http_status": 404, "retryable": True, "observed_at": "new"}):
            with self.subTest(invalid=invalid):
                rows[0]['github']['source_availability'] = invalid
                write_projects(self.root / 'data/projects.json', rows)
                errors = StringIO()
                with redirect_stderr(errors), self.assertRaises(SystemExit):
                    pipeline.validate(self.root / 'data/projects.json', self.root / 'data/activity.json')
                self.assertIn('invalid source_availability', errors.getvalue())

    def test_unavailable_backoff_does_not_pin_healthy_future_cycles(self):
        _, _ = self.unavailable_source_fixture(healthy=True)
        self.apply(self.collect())
        calls = sum('/repos/owner/a' in url for url, _ in self.net.calls)
        later = NOW + timedelta(hours=2)
        second = self.collect(now=later, request_id='healthy-next-cycle')
        self.apply(second, later)
        self.assertEqual(sum('/repos/owner/a' in url for url, _ in self.net.calls), calls)
        self.assertIn('owner/b', [r['repo'] for r in second['results']])
        self.assertNotIn('owner/a', second['progress_after']['cycle']['pending']['probe'])
        self.assertIn('owner/a', second['progress_after']['retry']['probe'])
        check_publishable(self.read(pipeline.POLL), load_projects(self.root / 'data/projects.json'), self.read('state/project-catalog-state.json'))

    def test_unavailable_probe_blocks_future_forced_history_without_pending_publication(self):
        self.unavailable_source_fixture()
        records = load_projects(self.root / 'data/projects.json')
        baseline = self.read('state/project-catalog-state.json')
        baseline['projects'] = {p['id']: snapshot(p) for p in records}
        self.put('state/project-catalog-state.json', baseline)
        first = self.collect()
        self.apply(first)
        self.assertIn('owner/a', first['progress_after']['retry']['activity'])
        calls = len(self.net.calls)
        later = NOW + timedelta(hours=1)
        self.apply(self.collect(now=later, request_id='forced-before-backoff', full=True), later)
        self.assertEqual(len(self.net.calls), calls)

    def test_unavailable_source_recovery_resumes_real_metadata_and_history(self):
        _, normal = self.unavailable_source_fixture()
        self.apply(self.collect())
        self.net.open = normal; self.net.pages = {1: [commit(10)]}
        later = NOW + timedelta(days=1)
        recovered = self.collect(now=later, request_id='recovered')
        self.apply(recovered, later)
        actual = load_projects(self.root / 'data/projects.json')[0]
        rs = self.read(pipeline.POLL)['repositories']['owner/a']
        self.assertNotIn('source_availability', actual['github'])
        self.assertNotIn('repository_availability', rs)
        self.assertNotIn('outcome', rs['publication'])
        self.assertTrue(rs['publication']['metadata_complete'])
        self.assertTrue(rs['publication']['history_complete'])
        self.assertEqual(rs['last_probe_at'], pipeline.stamp(later))
        check_publishable(self.read(pipeline.POLL), [actual], self.read('state/project-catalog-state.json'))

    def test_reachable_root_with_partial_metadata_failure_reopens_gate(self):
        prior, normal = self.unavailable_source_fixture()
        self.apply(self.collect())
        def partial(request, timeout):
            if urlsplit(request.full_url).path.endswith('/languages'):
                raise HTTPError(request.full_url, 500, 'Temporary', {}, BytesIO(b'server error'))
            return normal(request, timeout)
        self.net.open = partial
        later = NOW + timedelta(days=1)
        self.apply(self.collect(now=later, request_id='partial-recovery'), later)
        actual = load_projects(self.root / 'data/projects.json')[0]
        self.assertNotIn('source_availability', actual['github'])
        self.assertEqual(actual['github'], prior['github'])
        rs = self.read(pipeline.POLL)['repositories']['owner/a']
        self.assertNotIn('outcome', rs['publication'])
        self.assertNotIn('repository_availability', rs)
        with self.assertRaises(SystemExit):
            check_publishable(self.read(pipeline.POLL), [actual], self.read('state/project-catalog-state.json'))

    def test_new_source_root_404_does_not_waive_initial_context(self):
        self.seed([project('b')])
        self.put('data/pending-projects.json', [project('a')])
        normal = self.net.open
        def unavailable(request, timeout):
            if urlsplit(request.full_url).path == '/repos/owner/a':
                raise HTTPError(request.full_url, 404, 'Unavailable', {}, BytesIO())
            return normal(request, timeout)
        self.net.open = unavailable
        self.apply(self.collect())
        rs = self.read(pipeline.POLL)['repositories']['owner/a']
        self.assertNotIn('outcome', rs['publication'])
        self.assertEqual(rs['publication']['reset_project_ids'], ['a'])
        with self.assertRaises(SystemExit):
            check_publishable(self.read(pipeline.POLL), load_projects(self.root / 'data/projects.json'), self.read('state/project-catalog-state.json'))

    def test_changed_tracking_root_404_does_not_waive_new_context(self):
        for field, value in (("github_path", "new-path"), ("github_branch", "new-branch"),
                             ("repo", "https://github.com/owner/new")):
            with self.subTest(field=field):
                (self.root / pipeline.PROGRESS).unlink(missing_ok=True)
                self.net = Network(); self.unavailable_source_fixture()
                if field == "repo":
                    normal = self.net.open
                    def missing_root(request, timeout):
                        if urlsplit(request.full_url).path == '/repos/owner/new':
                            raise HTTPError(request.full_url, 404, 'Unavailable', {}, BytesIO())
                        return normal(request, timeout)
                    self.net.open = missing_root
                records = load_projects(self.root / 'data/projects.json'); records[0][field] = value
                write_projects(self.root / 'data/projects.json', records)
                self.apply(self.collect(request_id=field))
                with self.assertRaises(SystemExit):
                    check_publishable(self.read(pipeline.POLL), load_projects(self.root / 'data/projects.json'), self.read('state/project-catalog-state.json'))

    def test_missing_retained_metadata_cannot_resolve_as_unavailable(self):
        self.unavailable_source_fixture()
        records = load_projects(self.root / 'data/projects.json'); records[0]['github'] = {}
        write_projects(self.root / 'data/projects.json', records)
        self.apply(self.collect())
        rs = self.read(pipeline.POLL)['repositories']['owner/a']
        self.assertNotIn('outcome', rs['publication'])
        with self.assertRaises(SystemExit):
            check_publishable(self.read(pipeline.POLL), load_projects(self.root / 'data/projects.json'), self.read('state/project-catalog-state.json'))

    def test_repeated_root_404_keeps_facts_and_history_without_freshness(self):
        prior, _ = self.unavailable_source_fixture()
        self.apply(self.collect())
        first = load_projects(self.root / 'data/projects.json')[0]
        later = NOW + timedelta(days=1)
        self.apply(self.collect(now=later, request_id='retry-unavailable'), later)
        self.assertEqual(load_projects(self.root / 'data/projects.json')[0], first)
        rs = self.read(pipeline.POLL)['repositories']['owner/a']
        self.assertEqual(rs['last_probe_at'], pipeline.stamp(NOW - timedelta(days=1)))
        self.assertEqual(rs['last_deep_scan'], pipeline.stamp(NOW - timedelta(days=1)))
        self.assertFalse(rs['publication']['metadata_complete'])
        self.assertFalse(rs['publication']['history_complete'])
        self.assertEqual(rs['repository_availability']['observed_at'], pipeline.stamp(later))
        check_publishable(self.read(pipeline.POLL), [first], self.read('state/project-catalog-state.json'))

    def test_server_auth_and_file_errors_do_not_create_unavailable_outcome(self):
        for status in (401, 403, 429, 500):
            with self.subTest(status=status):
                (self.root / pipeline.PROGRESS).unlink(missing_ok=True)
                self.net = Network(); self.unavailable_source_fixture(status)
                self.apply(self.collect(request_id=str(status)))
                rs = self.read(pipeline.POLL)['repositories']['owner/a']
                self.assertNotIn('repository_availability', rs)
                self.assertNotIn('outcome', rs['publication'])
                with self.assertRaises(SystemExit):
                    check_publishable(self.read(pipeline.POLL), load_projects(self.root / 'data/projects.json'), self.read('state/project-catalog-state.json'))
        (self.root / pipeline.PROGRESS).unlink(missing_ok=True)
        self.net = Network(); _, normal = self.unavailable_source_fixture()
        def missing_file(request, timeout):
            if urlsplit(request.full_url).path.endswith('/languages'):
                raise HTTPError(request.full_url, 404, 'Missing file', {}, BytesIO())
            return normal(request, timeout)
        self.net.open = missing_file; self.apply(self.collect(request_id='file-404'))
        rs = self.read(pipeline.POLL)['repositories']['owner/a']
        self.assertNotIn('repository_availability', rs)
        self.assertNotIn('outcome', rs['publication'])

    def test_unavailable_observation_cannot_bless_concurrent_research(self):
        self.unavailable_source_fixture(); batch = self.collect()
        records = load_projects(self.root / 'data/projects.json'); records[0]['notes'] = 'Concurrent reviewed source update'
        write_projects(self.root / 'data/projects.json', records)
        result = self.apply(batch)
        self.assertEqual(result['conflicts'], ['owner/a'])
        self.assertEqual(load_projects(self.root / 'data/projects.json')[0]['notes'], 'Concurrent reviewed source update')
        with self.assertRaises(SystemExit):
            check_publishable(self.read(pipeline.POLL), load_projects(self.root / 'data/projects.json'), self.read('state/project-catalog-state.json'))

    def test_unavailable_resolution_fails_closed_for_invalid_or_stale_proof(self):
        self.unavailable_source_fixture(); self.apply(self.collect())
        state = self.read(pipeline.POLL); projects = load_projects(self.root / 'data/projects.json')
        mutations = [
            lambda r: r['repository_availability'].update(repository='other/repo'),
            lambda r: r['repository_availability'].update(http_status=500),
            lambda r: r['repository_availability'].update(retryable=False),
            lambda r: r['repository_availability'].update(observed_at='invalid'),
            lambda r: r['publication'].update(fingerprint='0' * 64),
            lambda r: r['publication'].update(reset_project_ids=['a']),
        ]
        for mutate in mutations:
            changed = copy.deepcopy(state); mutate(changed['repositories']['owner/a'])
            with self.assertRaises(SystemExit):
                check_publishable(changed, projects, self.read('state/project-catalog-state.json'))


if __name__ == "__main__":
    unittest.main()
