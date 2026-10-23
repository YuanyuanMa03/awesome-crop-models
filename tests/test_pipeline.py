"""Offline acceptance tests for collection, persistence and rendered browsing."""

import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from cropmodels.catalog import read_json, render, save_json, upsert
from cropmodels.cli import update
from cropmodels.github import BudgetExceeded, GitHubError, NotFound
from cropmodels.sources import enumerate_owners, refresh


BEFORE = "2026-10-21T03:17:00Z"
NOW = "2026-10-22T03:17:00Z"
LATER = "2026-10-23T03:17:00Z"


def repository(identifier, name=None, **extra):
    metadata = {
        "id": identifier, "full_name": name or f"owner/model-{identifier}",
        "private": False, "language": "Python", "description": "Public crop simulation",
        "license": {"spdx_id": "MIT", "name": "MIT License"},
    }
    metadata.update(extra)
    return metadata


def search_page(items=(), total=None, incomplete=False):
    return {"items": list(items), "total_count": len(items) if total is None else total,
            "incomplete_results": incomplete}


def seed(identifier=10, name="owner/model-10", **extra):
    return {
        "repo": name, "github_id": identifier, "type": "model", "subject": "general-crop",
        "description": "A process-based crop model.", **extra,
    }


class FakeClient:
    """Count actual requests and successful JSON responses independently."""

    def __init__(self, responses=(), max_requests=1000):
        self.responses = responses if callable(responses) else iter(responses)
        self.max_requests = max_requests
        self.requests = 0
        self.successful_responses = 0
        self.calls = []

    def get(self, path, params=None):
        if self.requests >= self.max_requests:
            raise BudgetExceeded("offline request budget exhausted")
        self.requests += 1
        self.calls.append((path, copy.deepcopy(params)))
        outcome = self.responses(path, params) if callable(self.responses) else next(self.responses)
        if isinstance(outcome, Exception):
            raise outcome
        self.successful_responses += 1
        return copy.deepcopy(outcome)


class RootFixture(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        (self.root / "docs").mkdir()
        self.seeds = [seed()]
        self.queries = [{"id": "crop", "query": "crop model in:readme"}]
        self.owners = [{"kind": "org", "login": "owner"}]
        save_json(self.root / "config/seeds.json", self.seeds)
        save_json(self.root / "config/queries.json", self.queries)
        save_json(self.root / "config/owners.json", self.owners)
        save_json(self.root / "catalog/repositories.json", {})
        save_json(self.root / "state/health.json", {
            "status": "partial", "last_healthy_at": BEFORE, "last_historical_pass_at": BEFORE,
        })

    def collect(self, client, now=NOW, discovery_pages=3, refresh_limit=0, owner_pages=0):
        with patch("cropmodels.cli.utc_now", return_value=now):
            return update(self.root, client, now, discovery_pages, refresh_limit, owner_pages)

    def read(self, path):
        return read_json(self.root / path)


class PipelineTests(RootFixture):
    def test_api_failure_saves_completed_pages_and_both_search_checkpoints(self):
        recent = [repository(i) for i in range(1, 101)]
        historical = [repository(i) for i in range(101, 201)]
        client = FakeClient([
            search_page(recent, 150), search_page(historical, 150), GitHubError("offline outage"),
        ])
        report, code = self.collect(client)
        self.assertEqual(code, 1)
        self.assertEqual(report["status"], "failed")
        self.assertEqual(report["last_healthy_at"], BEFORE)
        self.assertEqual(report["last_historical_pass_at"], BEFORE)
        self.assertEqual(report["requests"], 3)
        catalog = self.read("catalog/repositories.json")
        self.assertEqual(set(catalog), {str(i) for i in range(1, 201)})
        for row in catalog.values():
            self.assertEqual(row["discovered_by"], ["crop"])
        state = self.read("state/discovery.json")
        for lane in ("recent", "historical"):
            self.assertEqual(state[lane]["queue"][0]["page"], 2)
            self.assertEqual(state[lane]["pending_repositories"], [])
        self.assertEqual(state["historical"]["last_run"]["status"], "interrupted")
        self.assertEqual(self.read("state/health.json")["last_healthy_at"], BEFORE)

        resumed = FakeClient([
            search_page([repository(i) for i in range(201, 251)], total=150),
            search_page([repository(i) for i in range(251, 301)], total=150),
        ])
        report, code = self.collect(resumed, LATER)
        self.assertEqual(code, 0)
        self.assertEqual(report["status"], "completed_plan")
        self.assertEqual([params["page"] for _, params in resumed.calls], [2, 2])
        self.assertTrue(all(f"..{NOW}" in params["q"] for _, params in resumed.calls))
        self.assertEqual(len(self.read("catalog/repositories.json")), 300)
        resumed_state = self.read("state/discovery.json")
        self.assertTrue(all(resumed_state[lane]["plan_completed"] for lane in ("recent", "historical")))

    def test_excluded_repositories_are_not_kept_in_the_catalogue_or_provenance(self):
        save_json(self.root / "config/excluded.json", {"5": {"repo": "owner/model-5", "reason": "off-topic"}})
        client = FakeClient(lambda path, params: search_page([repository(5), repository(6)]))
        report, code = self.collect(client)
        self.assertEqual(code, 0)
        self.assertEqual(set(self.read("catalog/repositories.json")), {"6"})
        self.assertEqual(report["new_repository_identities"], 1)
        state = self.read("state/discovery.json")
        for lane in ("recent", "historical"):
            self.assertEqual(set(state[lane]["repo_queries"]), {"6"})
        self.assertIn("2 tracked · 0 listed · 1 excluded · 0 forks · **1 awaiting review**", (self.root / "docs/discovered.md").read_text())

    def test_failed_attempt_keeps_last_healthy_timestamp_after_successful_refresh(self):
        client = FakeClient([repository(10), GitHubError("languages endpoint unavailable")])
        report, code = self.collect(client, discovery_pages=0, refresh_limit=1)
        self.assertEqual(code, 1)
        self.assertEqual(client.successful_responses, 1)
        self.assertEqual(report["last_healthy_at"], BEFORE)
        self.assertEqual(report["previous_healthy_at"], BEFORE)
        self.assertEqual(self.read("catalog/repositories.json")["10"]["full_name"], "owner/model-10")

    def test_zero_request_budget_does_not_fake_a_healthy_collection(self):
        report, code = self.collect(FakeClient(max_requests=0), refresh_limit=1)
        self.assertEqual(code, 0)
        self.assertEqual(report["requests"], 0)
        self.assertEqual(report["status"], "partial_budget")
        self.assertEqual(report["last_healthy_at"], BEFORE)
        self.assertEqual(report["last_historical_pass_at"], BEFORE)
        self.assertEqual(self.read("catalog/repositories.json"), {})

    def test_zero_work_limits_do_not_claim_plan_completion_or_new_health(self):
        report, _ = self.collect(FakeClient(), discovery_pages=0)
        self.assertEqual(report["requests"], 0)
        self.assertEqual(report["last_healthy_at"], BEFORE)
        self.assertNotEqual(report["status"], "completed_plan")
        self.assertFalse(report["all_github_coverage_verified"])

    def test_healthy_bounded_run_reports_pending_work_and_recent_history_split(self):
        items = [repository(i) for i in range(1, 101)]
        client = FakeClient(lambda path, params: search_page(items, 500))
        report, code = self.collect(client, discovery_pages=3)
        self.assertEqual(code, 0)
        self.assertEqual(report["status"], "partial")
        self.assertEqual(report["last_healthy_at"], NOW)
        self.assertEqual(report["requests"], 3)
        state = self.read("state/discovery.json")
        self.assertEqual(state["recent"]["queue"][0]["page"], 2)
        self.assertEqual(state["historical"]["queue"][0]["page"], 3)
        self.assertEqual(state["recent"]["cycle_start"], "2026-09-22T03:17:00Z")
        self.assertEqual(state["historical"]["cycle_start"], "2007-01-01T00:00:00Z")
        self.assertEqual(report["last_historical_pass_at"], BEFORE)

    def test_new_query_configuration_preserves_existing_catalogue_and_gap_evidence(self):
        client = FakeClient(lambda path, params: search_page([repository(5)], incomplete=True))
        self.collect(client)
        before_state = self.read("state/discovery.json")
        self.assertEqual(len(self.read("catalog/repositories.json")), 1)
        queries = self.queries + [{"id": "soil", "query": "soil crop in:readme"}]
        save_json(self.root / "config/queries.json", queries)
        resumed = FakeClient(lambda path, params: search_page())
        report, code = self.collect(resumed, LATER)
        self.assertEqual(code, 0)
        self.assertIn("5", self.read("catalog/repositories.json"))
        after_state = self.read("state/discovery.json")
        for lane in ("recent", "historical"):
            self.assertEqual(after_state[lane]["cycle"], before_state[lane]["cycle"] + 1)
            self.assertTrue(all(gap in after_state[lane]["coverage_gaps"] for gap in before_state[lane]["coverage_gaps"]))
            self.assertEqual(after_state[lane]["repo_queries"]["5"], ["crop"])
        self.assertGreaterEqual(report["tracked_repositories"], 1)

    def test_invalid_outbox_entry_retains_valid_neighbors_without_claiming_a_healthy_pass(self):
        invalid = repository(2, "invalid-name-without-owner")
        client = FakeClient([search_page(), search_page([repository(1), invalid, repository(3)])])
        report, code = self.collect(client)
        self.assertEqual(code, 1)
        self.assertEqual(report["status"], "failed")
        self.assertEqual(report["rejected_repository_records"], 1)
        self.assertEqual(set(self.read("catalog/repositories.json")), {"1", "3"})
        self.assertEqual(report["last_healthy_at"], BEFORE)
        self.assertEqual(report["last_historical_pass_at"], BEFORE)
        state = self.read("state/discovery.json")
        self.assertTrue(state["historical"]["plan_completed"])
        self.assertEqual(state["historical"]["pending_repositories"], [])

    def test_idle_run_does_not_refresh_a_previous_historical_pass_timestamp(self):
        report, code = self.collect(FakeClient([search_page(), search_page()]))
        self.assertEqual(code, 0)
        self.assertEqual(report["last_historical_pass_at"], NOW)
        report, code = self.collect(FakeClient(), LATER, discovery_pages=0)
        self.assertEqual(code, 0)
        self.assertEqual(report["requests"], 0)
        self.assertEqual(report["last_healthy_at"], NOW)
        self.assertEqual(report["last_historical_pass_at"], NOW)
        self.assertNotEqual(report["status"], "completed_plan")

    def test_registry_is_saved_before_the_checkpoint_and_checkpoint_write_failure_is_recoverable(self):
        old_state = {"recent": {}, "historical": {}}
        save_json(self.root / "state/discovery.json", old_state)
        writes = []

        def fail_checkpoint(path, value):
            writes.append(path.relative_to(self.root).as_posix())
            if path == self.root / "state/discovery.json":
                self.assertIn("55", self.read("catalog/repositories.json"))
                raise OSError("offline checkpoint write failure")
            return save_json(path, value)

        with patch("cropmodels.cli.save_json", side_effect=fail_checkpoint):
            with self.assertRaisesRegex(OSError, "checkpoint write"):
                self.collect(FakeClient([search_page([repository(55)])]), discovery_pages=1)
        self.assertEqual(writes[:2], ["catalog/repositories.json", "state/discovery.json"])
        self.assertEqual(self.read("state/discovery.json"), old_state)
        self.assertEqual(set(self.read("catalog/repositories.json")), {"55"})
        # The old checkpoint rereads the page; stable-ID upsert prevents duplicates.
        self.collect(FakeClient([search_page([repository(55)])]), discovery_pages=1)
        self.assertEqual(set(self.read("catalog/repositories.json")), {"55"})

    def test_registry_write_failure_never_advances_checkpoint(self):
        old_state = {"recent": {}, "historical": {}}
        save_json(self.root / "state/discovery.json", old_state)
        writes = []

        def fail_registry(path, value):
            writes.append(path.relative_to(self.root).as_posix())
            if path == self.root / "catalog/repositories.json":
                raise OSError("offline catalog write failure")
            return save_json(path, value)

        with patch("cropmodels.cli.save_json", side_effect=fail_registry):
            with self.assertRaisesRegex(OSError, "catalog write"):
                self.collect(FakeClient([search_page([repository(55)])]), discovery_pages=1)
        self.assertEqual(writes, ["catalog/repositories.json"])
        self.assertEqual(self.read("state/discovery.json"), old_state)
        self.assertEqual(self.read("catalog/repositories.json"), {})


class SourceTests(RootFixture):
    def test_refresh_uses_stable_id_after_rename_and_collects_all_languages(self):
        registry = {}
        upsert(registry, repository(10), BEFORE, self.seeds)
        client = FakeClient([
            repository(10, "successor/renamed", language="Python"),
            {"Python": 500, "Fortran": 200, "C++": 50, "Shell": 0},
        ])
        state = {}
        report = refresh(client, registry, state, self.seeds, NOW, 1)
        self.assertEqual([path for path, _ in client.calls], ["/repositories/10", "/repos/successor/renamed/languages"])
        self.assertEqual(set(registry), {"10"})
        row = registry["10"]
        self.assertEqual(row["full_name"], "successor/renamed")
        self.assertEqual(row["aliases"], ["owner/model-10"])
        self.assertEqual(row["selection"]["repo"], "owner/model-10")
        self.assertEqual(row["languages"], {"Python": 500, "Fortran": 200, "C++": 50})
        self.assertEqual(row["language_status"], "github_languages_endpoint")
        self.assertEqual(report["checked_repositories"], 1)

    def test_private_refresh_response_does_not_publish_private_metadata(self):
        registry = {}
        upsert(registry, repository(10), BEFORE, self.seeds)
        private = repository(10, "private-owner/unpublished-name", private=True,
                             description="unpublished-private-description", topics=["private-topic"])
        state = {}
        refresh(FakeClient([private]), registry, state, self.seeds, NOW, 1)
        serialized = json.dumps(registry)
        for marker in ("private-owner", "unpublished-name", "unpublished-private-description", "private-topic"):
            self.assertNotIn(marker, serialized)
        self.assertEqual(registry["10"]["full_name"], "owner/model-10")
        self.assertEqual(registry["10"]["availability"], "no_longer_public_or_unverified")
        self.assertEqual(state["seed_checks"]["owner/model-10"]["outcome"], "nonpublic_response_not_saved")

    def test_unknown_private_seed_is_not_added_to_public_catalogue(self):
        registry = {}
        refresh(FakeClient([repository(10, private=True)]), registry, {}, self.seeds, NOW, 1)
        self.assertEqual(registry, {})

    def test_owner_pagination_is_fair_and_404_remains_visible_as_gap(self):
        owners = [{"kind": "org", "login": "large"}, {"kind": "user", "login": "missing"}]
        state, registry = {}, {}
        client = FakeClient([[repository(i) for i in range(1, 101)], NotFound("offline 404")])
        report = enumerate_owners(client, registry, state, owners, self.seeds, NOW, max_pages=2)
        self.assertEqual([path for path, _ in client.calls], ["/orgs/large/repos", "/users/missing/repos"])
        self.assertEqual([params["page"] for _, params in client.calls], [1, 1])
        self.assertEqual(state["owner_queue"], [{"login": "large", "kind": "org", "page": 2}])
        self.assertEqual(state["owner_gaps"][0]["login"], "missing")
        self.assertIn("not_found", state["owner_gaps"][0]["reason"])
        self.assertEqual(report["pages"], 2)
        self.assertEqual(len(registry), 100)
        self.assertEqual(registry["1"]["discovered_by"], ["owner:large"])
        resumed = FakeClient([[]])
        enumerate_owners(resumed, registry, state, owners, self.seeds, LATER, max_pages=1)
        self.assertEqual(resumed.calls[0], ("/orgs/large/repos", {
            "per_page": 100, "page": 2, "sort": "full_name", "direction": "asc", "type": "public",
        }))
        self.assertEqual(state["owner_queue"], [])
        self.assertEqual(len(state["owner_gaps"]), 1)

    def test_owner_api_failure_preserves_next_job_and_prior_page_results(self):
        owners = [{"kind": "org", "login": "large"}, {"kind": "user", "login": "second"}]
        state, registry = {}, {}
        client = FakeClient([[repository(i) for i in range(1, 101)], GitHubError("offline outage")])
        with self.assertRaises(GitHubError):
            enumerate_owners(client, registry, state, owners, self.seeds, NOW)
        self.assertEqual(len(registry), 100)
        self.assertEqual([(job["login"], job["page"]) for job in state["owner_queue"]], [("second", 1), ("large", 2)])

    def test_changed_stable_id_is_rejected_without_replacing_identity(self):
        registry = {}
        upsert(registry, repository(10), BEFORE, self.seeds)
        before = copy.deepcopy(registry)
        with self.assertRaisesRegex(ValueError, "Stable repository ID"):
            refresh(FakeClient([repository(11)]), registry, {}, self.seeds, NOW, 1)
        self.assertEqual(registry, before)

    def test_renderer_lists_each_repository_once_under_subject_then_main_language(self):
        save_json(self.root / "config/seeds.json", [seed(subject="wheat")])
        registry = {}
        refresh(FakeClient([repository(10), {"Python": 500, "Fortran": 100, "C++": 20, "Shell": 0}]),
                registry, {}, [seed(subject="wheat")], NOW, 1)
        save_json(self.root / "catalog/repositories.json", registry)
        render(self.root)
        readme = (self.root / "README.md").read_text()
        discovered = (self.root / "docs/discovered.md").read_text()
        self.assertIn("**1 repositories:** 1 process-based models", readme)
        self.assertIn("  - [Wheat](#wheat) (1)\n    - [Python](#wheat-python) (1)", readme)
        self.assertIn('<a id="wheat-python"></a>\n\n#### Python', readme)
        self.assertNotIn("#### Fortran", readme)
        self.assertEqual(readme.count("- [owner/model-10](https://github.com/owner/model-10) - "), 1)
        self.assertLess(readme.index("## Crop models"), readme.index("#### Python"))
        self.assertIn("**0 awaiting review**", discovered)

if __name__ == "__main__":
    unittest.main()
