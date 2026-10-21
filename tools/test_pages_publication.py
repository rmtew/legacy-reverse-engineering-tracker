"""Pages decisions, successful receipts, coalescing and durable follow-up."""

import copy
from contextlib import redirect_stdout
from io import StringIO
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

import pages_publication as pages
from build_site import build
from catalogue_storage import load_projects, write_all, write_projects
from merge_pending_projects import new_audit
from record_project_activity import snapshot


class API:
    def __init__(self, deployed):
        self.last = deployed
        self.busy = False
        self.requests = []

    def deployed(self):
        return self.last

    def collecting(self, snapshot):
        return self.busy

    def dispatch(self, attempt):
        self.requests.append(attempt)


class PublicationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.git("init", "--initial-branch=main")
        self.git("config", "user.name", "Test")
        self.git("config", "user.email", "test@example.org")
        self.project = {
            "id": "p",
            "title": "Game",
            "upstream_name": "Game",
            "display_title": "Game",
            "subjects": ["Game"],
            "repo": "https://github.com/owner/repo",
            "record_class": "subject",
            "target_kinds": ["game"],
            "work_kinds": [],
            "tool_kinds": [],
            "github": {"checked_at": "2026-10-19"},
        }
        write_all(
            self.root / "data",
            {
                "projects.json": [self.project],
                "project-audits.json": {"projects": [new_audit("p")]},
                "discovery-sources.json": {"sources": [], "backlog": []},
                "discovery-decisions.json": {"indexed_at": "2026-10-19", "decisions": []},
                "research-activity.json": {"events": []},
            },
        )
        self.put("data/pending-projects.json", [])
        self.put(
            "data/activity.json", {"generated_at": "2026-10-19T00:00:00Z", "window_days": 180, "events": []}
        )
        self.put("state/project-catalog-state.json", {"projects": {"p": snapshot(self.project)}})
        self.put("state/github-poll-state.json", {"repositories": {}})
        (self.root / "index.html").write_text(
            '<link href="web/tracker.css"><script src="web/tracker.js"></script>'
        )
        (self.root / "web").mkdir()
        (self.root / "web/tracker.css").write_text("body{color:red}")
        (self.root / "web/tracker.js").write_text('console.log("ok")')
        self.a = self.commit()
        self.api = API(self.a)
        original = pages.git
        self.fetch = patch.object(
            pages,
            "git",
            side_effect=lambda root, *args: "" if args[:1] == ("fetch",) else original(root, *args),
        )
        self.fetch.start()
        self.addCleanup(self.fetch.stop)

    def git(self, *args):
        return (
            subprocess.check_output(["git", *args], cwd=self.root, stderr=subprocess.DEVNULL).decode().strip()
        )

    def put(self, path, value):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(value))

    def commit(self):
        self.git("add", "-A")
        self.git("commit", "-qm", "Snapshot")
        sha = self.git("rev-parse", "HEAD")
        self.git("update-ref", "refs/remotes/origin/main", sha)
        return sha

    def change(self, color="blue"):
        (self.root / "web/tracker.css").write_text("body{color:" + color + "}")
        return self.commit()

    def test_no_change_clock_only_and_private_state_do_not_deploy(self):
        self.assertEqual(pages.inspect(self.root, self.api, self.a)["reason"], "already-deployed")
        rows = load_projects(self.root / "data/projects.json")
        rows[0]["github"]["checked_at"] = "2026-10-20"
        write_projects(self.root / "data/projects.json", rows)
        self.put(
            "data/activity.json", {"generated_at": "2026-10-20T00:00:00Z", "window_days": 180, "events": []}
        )
        self.put("state/refresh-progress.json", {"revision": 987})
        b = self.commit()
        self.assertEqual(pages.fingerprint(self.root, self.a), pages.fingerprint(self.root, b))
        self.assertFalse(pages.request(self.root, self.api)["requested"])
        self.assertEqual(self.api.requests, [])

    def test_public_assets_research_and_build_inputs_are_material(self):
        original = pages.fingerprint(self.root, self.a)
        self.change()
        self.assertNotEqual(original, pages.fingerprint(self.root, self.git("rev-parse", "HEAD")))
        self.put("data/discovery-sources.json", {"sources": [], "backlog": [], "note": "New source evidence"})
        b = self.commit()
        self.assertNotEqual(original, pages.fingerprint(self.root, b))
        path = self.root / "tools/build_site.py"
        path.parent.mkdir()
        path.write_text("# New output renderer")
        c = self.commit()
        self.assertNotEqual(pages.fingerprint(self.root, b), pages.fingerprint(self.root, c))

    def test_workflow_and_validation_only_changes_do_not_deploy(self):
        self.put(".github/workflows/pages.yml", {"test": "A control-plane change"})
        (self.root / "tools").mkdir()
        (self.root / "tools/test_new.py").write_text("# A test")
        (self.root / "tools/validate_site_data.py").write_text("# A validator")
        b = self.commit()
        self.assertEqual(pages.fingerprint(self.root, self.a), pages.fingerprint(self.root, b))
        self.assertFalse(pages.inspect(self.root, self.api, b)["deploy"])

    def test_catalogue_incomplete_and_pending_placeholders_hold_all_requests(self):
        b = self.change()
        self.put("data/pending-projects.json", [{"id": "new"}])
        c = self.commit()
        self.assertFalse(pages.publishable(self.root, c))
        self.assertEqual(pages.request(self.root, self.api)["reason"], "publication-incomplete")
        self.put("data/pending-projects.json", [])
        self.put(
            "state/github-poll-state.json",
            {
                "repositories": {
                    "owner/repo": {"publication": {"metadata_complete": True, "history_complete": False}}
                }
            },
        )
        c = self.commit()
        self.assertFalse(pages.publishable(self.root, c))
        self.put("state/github-poll-state.json", {"repositories": {}})
        rows = load_projects(self.root / "data/projects.json")
        rows[0]["title"] = "Unrecorded authored change"
        write_projects(self.root / "data/projects.json", rows)
        c = self.commit()
        self.assertFalse(pages.publishable(self.root, c))
        self.assertEqual(self.api.requests, [])

    def test_overlapping_collectors_coalesce_and_failed_peer_finalizer_repairs_request(self):
        b = self.change()
        self.api.busy = True
        self.assertEqual(pages.request(self.root, self.api)["reason"], "collector-publishing")
        self.assertEqual(self.api.requests, [])
        # The peer can fail after another collector published successfully. Its
        # finalizer still requests the complete latest public content.
        self.api.busy = False
        self.assertTrue(pages.request(self.root, self.api)["requested"])
        self.api.last = b
        self.assertFalse(pages.request(self.root, self.api)["requested"])
        self.assertEqual(self.api.requests, [0])

    def test_changes_during_deployment_and_superseded_pending_requests_are_not_lost(self):
        b = self.change()
        admitted = pages.inspect(self.root, self.api, b)
        self.assertTrue(admitted["deploy"])
        c = self.change("green")  # B is still building under the shared lock.
        self.api.last = b  # B succeeds; follow-up must deploy C.
        self.assertTrue(pages.request(self.root, self.api)["requested"])
        stale = pages.inspect(self.root, self.api, self.a)
        self.assertEqual(stale["reason"], "superseded-request")
        self.assertFalse(stale["deploy"])
        fresh = pages.inspect(self.root, self.api, c)
        self.assertTrue(fresh["deploy"])
        self.api.last = c
        # Any delayed older request reads C and cannot overwrite it with A/B.
        self.assertEqual(pages.inspect(self.root, self.api, b)["reason"], "already-deployed")
        self.assertFalse(pages.request(self.root, self.api)["requested"])

    def test_unchanged_failed_deployment_retries_are_bounded_new_material_resets_budget(self):
        b = self.change()
        digest = pages.fingerprint(self.root, b)
        self.assertTrue(
            pages.request(self.root, self.api, failure=True, attempt=0, failed_digest=digest)["requested"]
        )
        self.assertEqual(self.api.requests, [1])
        self.assertEqual(
            pages.request(self.root, self.api, failure=True, attempt=2, failed_digest=digest)["reason"],
            "retry-limit",
        )
        self.assertEqual(self.api.requests, [1])
        self.change("green")
        self.assertTrue(
            pages.request(self.root, self.api, failure=True, attempt=2, failed_digest=digest)["requested"]
        )
        self.assertEqual(self.api.requests, [1, 0])
        self.api.last = self.git("rev-parse", "HEAD")
        self.assertFalse(pages.request(self.root, self.api)["requested"])

    def test_unknown_failed_gate_baseline_also_has_a_retry_limit(self):
        self.change()
        self.assertEqual(pages.request(self.root, self.api, failure=True, attempt=2)["reason"], "retry-limit")
        self.assertEqual(self.api.requests, [])

    def test_refresh_batches_coalesce_only_after_successful_continuation_handoff(self):
        self.change()
        result = pages.request_after_refresh(
            self.root, self.api, result="success", continuation="true", handoff="success"
        )
        self.assertEqual(result, {"requested": False, "reason": "refresh-continuing"})
        self.assertEqual(self.api.requests, [])
        for reason in ("complete", "backoff", "paused", "stale", "zero-progress"):
            with self.subTest(reason=reason):
                # All terminal/paused refresh apply outcomes emit continue=false.
                result = pages.request_after_refresh(
                    self.root, self.api, result="success", continuation="false", handoff="success"
                )
                self.assertTrue(result["requested"])
        for result, continuation, handoff in (
            ("failure", "true", "success"),  # Failed push with artifact recovery queued.
            ("failure", "true", "failure"),  # Exhausted publication recovery.
            ("success", "true", "failure"),  # Failed next-batch dispatch.
            ("success", "true", "skipped"),
            ("success", "", "success"),
        ):
            with self.subTest(result=result, continuation=continuation, handoff=handoff):
                self.assertTrue(pages.request_after_refresh(
                    self.root, self.api, result=result, continuation=continuation, handoff=handoff
                )["requested"])

    def test_refresh_coalescing_does_not_strand_independent_or_failed_publications(self):
        b = self.change()
        self.assertFalse(pages.request_after_refresh(
            self.root, self.api, result="success", continuation="true", handoff="success"
        )["requested"])
        # A lost or delayed successor never holds the gate. The existing hourly
        # Pages schedule, another collector, or a manual request can reconcile.
        self.assertTrue(pages.request(self.root, self.api)["requested"])
        self.assertTrue(pages.inspect(self.root, self.api, b)["deploy"])
        with patch.object(self.api, "dispatch", side_effect=RuntimeError("request unavailable")):
            with self.assertRaises(RuntimeError):
                pages.request_after_refresh(
                    self.root, self.api, result="success", continuation="false", handoff="success"
                )
        self.assertEqual(self.api.last, self.a)
        self.assertTrue(pages.request(self.root, self.api)["requested"])
        self.api.last = b
        self.assertFalse(pages.request_after_refresh(
            self.root, self.api, result="success", continuation="false", handoff="success"
        )["requested"])

    def test_refresh_finalizer_cli_uses_handoff_outcome_and_fails_open_to_reconciliation(self):
        self.change()
        with patch.dict(os.environ, {
            "REFRESH_RESULT": "success", "REFRESH_CONTINUE": "true", "REFRESH_HANDOFF": "success"
        }), patch.object(pages, "GitHub", return_value=self.api), patch("sys.argv", [
            "pages", "request-refresh", "--root", str(self.root)
        ]), redirect_stdout(StringIO()):
            pages.main()
            self.assertEqual(self.api.requests, [])
            with patch.dict(os.environ, {"REFRESH_HANDOFF": "failure"}):
                pages.main()
        self.assertEqual(self.api.requests, [0])

    def test_actual_snapshot_matches_event_and_retains_strict_verification(self):
        with patch.dict(os.environ, {"GITHUB_SHA": self.a}), patch(
            "sys.argv", ["pages", "verify", "--root", str(self.root), "--snapshot", self.a]
        ):
            pages.main()
        b = self.change()
        with patch.dict(os.environ, {"GITHUB_SHA": self.a}), patch(
            "sys.argv", ["pages", "verify", "--root", str(self.root), "--snapshot", b]
        ):
            with self.assertRaises(SystemExit):
                pages.main()

    def test_build_preserves_feeds_assets_and_validates_the_export(self):
        with redirect_stdout(StringIO()):
            build(self.root, self.root / "site")
        html = (self.root / "site/index.html").read_text()
        self.assertRegex(html, r"web/tracker\.js\?v=[0-9a-f]{12}")
        self.assertRegex(html, r"web/tracker\.css\?v=[0-9a-f]{12}")
        self.assertTrue((self.root / "site/activity.xml").exists())
        self.assertEqual(json.loads((self.root / "site/data/activity-30d.json").read_bytes())["events"], [])
        self.assertFalse((self.root / "site/data/activity-180d.json").exists())
        self.assertEqual(json.loads((self.root / "site/data/activity.json").read_bytes())["window_days"], 30)


class GitHubStateTests(unittest.TestCase):
    def test_last_successful_deployment_ignores_failed_newer_attempts(self):
        api = pages.GitHub("owner/repo")

        def get(path):
            if path.startswith("deployments?"):
                return [{"id": 3, "sha": "b" * 40}, {"id": 2, "sha": "a" * 40}]
            if "/3/" in path:
                return [{"state": "failure"}]
            if "/2/" in path:
                return [{"state": "success"}]
            raise AssertionError(path)

        with patch.object(api, "get", side_effect=get):
            self.assertEqual(api.deployed(), "a" * 40)
        with patch.object(api, "get", side_effect=RuntimeError("API unavailable")):
            with self.assertRaises(RuntimeError):
                api.deployed()

    def test_finalizers_do_not_deadlock_on_each_other_but_collection_defers(self):
        api = pages.GitHub("owner/repo")
        step = {"name": pages.COLLECTORS[".github/workflows/refresh-github.yml"], "status": "completed"}

        def get(path):
            if path.startswith("actions/runs?"):
                return {"workflow_runs": [{"id": 2, "path": ".github/workflows/refresh-github.yml"}]}
            return {"jobs": [{"name": "refresh", "status": "in_progress", "steps": [step]}]}

        with patch.dict(os.environ, {"GITHUB_RUN_ID": "1"}), patch.object(api, "get", side_effect=get):
            self.assertFalse(api.collecting("a" * 40))
            step["status"] = "in_progress"
            self.assertTrue(api.collecting("a" * 40))
            # The next batch reads the already-published snapshot; it cannot
            # hold that snapshot behind the entire collector backlog.
            with patch.object(
                api,
                "get",
                side_effect=lambda path: (
                    {
                        "workflow_runs": [
                            {"id": 2, "path": ".github/workflows/refresh-github.yml", "head_sha": "a" * 40}
                        ]
                    }
                    if path.startswith("actions/runs?")
                    else {"jobs": [{"name": "refresh", "status": "in_progress", "steps": [step]}]}
                ),
            ):
                self.assertFalse(api.collecting("a" * 40))
            step["status"] = "completed"
            self.assertFalse(api.collecting("a" * 40))

    def test_dispatch_transient_failure_retries_and_terminal_failure_is_visible(self):
        api = pages.GitHub("owner/repo")
        with patch.object(
            pages.subprocess,
            "run",
            side_effect=[subprocess.CompletedProcess([], 1), subprocess.CompletedProcess([], 0)],
        ) as call, patch.object(pages.time, "sleep"):
            api.dispatch(1)
            self.assertEqual(call.call_count, 2)
        with patch.object(
            pages.subprocess, "run", return_value=subprocess.CompletedProcess([], 1)
        ), patch.object(pages.time, "sleep"):
            with self.assertRaises(RuntimeError):
                api.dispatch(0)


if __name__ == "__main__":
    unittest.main()
