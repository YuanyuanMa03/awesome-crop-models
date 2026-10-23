"""Regression checks for fair refreshes and rejected damaged checkpoints."""

from pathlib import Path
import tempfile
import unittest

from cropmodels.catalog import save_json, upsert, validate
from cropmodels.github import NotFound
from cropmodels.sources import refresh


FIRST = "2026-10-22T03:17:00Z"
NEXT = "2026-10-23T03:17:00Z"


def seed(name):
    return {"repo": name, "type": "model", "subject": "general-crop", "description": "A crop model."}


def repository(identifier, name):
    return {"id": identifier, "full_name": name, "private": False, "language": "Python"}


class RefreshClient:
    def __init__(self):
        self.calls = []

    def get(self, path, params=None):
        self.calls.append(path)
        if path.endswith("/languages"):
            return {"Python": 100}
        if path == "/repos/b-valid/model":
            return repository(7, "b-valid/model")
        if path == "/repositories/42":
            return repository(42, "known/model")
        raise NotFound("offline missing repository")


class FairRefreshRecoveryTests(unittest.TestCase):
    def test_missing_first_seed_does_not_prevent_the_next_seed_on_the_second_run(self):
        seeds = [seed("a-missing/model"), seed("b-valid/model")]
        registry, state, client = {}, {}, RefreshClient()
        refresh(client, registry, state, seeds, FIRST, limit=1)
        refresh(client, registry, state, seeds, NEXT, limit=1)
        self.assertEqual(client.calls[:2], ["/repos/a-missing/model", "/repos/b-valid/model"])
        self.assertIn("7", registry)
        self.assertEqual(state["seed_checks"]["a-missing/model"]["outcome"], "not_found_or_inaccessible")

    def test_many_missing_seeds_leave_a_refresh_slot_for_an_existing_repository(self):
        registry, state, client = {}, {}, RefreshClient()
        upsert(registry, repository(42, "known/model"), FIRST)
        seeds = [seed(f"missing-{index}/model") for index in range(20)]
        report = refresh(client, registry, state, seeds, NEXT, limit=2)
        self.assertEqual(report["checked_repositories"], 2)
        self.assertIn("/repositories/42", client.calls)
        self.assertEqual(registry["42"]["last_checked_at"], NEXT)
        self.assertEqual(registry["42"]["languages"], {"Python": 100})

    def test_one_repository_budget_alternates_missing_and_known_groups_across_runs(self):
        registry, state, client = {}, {}, RefreshClient()
        upsert(registry, repository(42, "known/model"), FIRST)
        seeds = [seed("a-missing/model"), seed("b-missing/model")]
        refresh(client, registry, state, seeds, FIRST, limit=1)
        refresh(client, registry, state, seeds, NEXT, limit=1)
        repository_calls = [path for path in client.calls if not path.endswith("/languages")]
        self.assertEqual(repository_calls, ["/repos/a-missing/model", "/repositories/42"])


class CheckpointValidationRecoveryTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        save_json(self.root / "config/seeds.json", [seed("known/model")])
        save_json(self.root / "config/queries.json", [{"id": "crop", "query": "crop model in:readme"}])
        save_json(self.root / "config/owners.json", [{"kind": "org", "login": "known"}])
        save_json(self.root / "catalog/repositories.json", {})

    def assert_rejected_without_rewriting(self, relative, value):
        path = self.root / relative
        save_json(path, value)
        before = path.read_bytes()
        with self.assertRaises(ValueError) as error:
            validate(self.root)
        self.assertIn(relative, str(error.exception))
        self.assertEqual(path.read_bytes(), before)

    def test_invalid_search_lane_is_rejected_before_update_and_is_not_cleared(self):
        self.assert_rejected_without_rewriting("state/discovery.json", {"historical": [], "recent": {}})

    def test_invalid_search_queue_is_rejected_with_its_file_location(self):
        for queue in ({}, ["lost checkpoint"], [{"query_id": "crop", "page": 0}]):
            with self.subTest(queue=queue):
                self.assert_rejected_without_rewriting("state/discovery.json", {"historical": {"queue": queue}})

    def test_invalid_owner_queue_is_rejected_and_is_not_cleared(self):
        bad = [{}, ["lost account"], [{"kind": "org", "login": "known", "page": 0}],
               [{"kind": "org", "login": "known", "page": True}]]
        for queue in bad:
            with self.subTest(queue=queue):
                self.assert_rejected_without_rewriting("state/refresh.json", {"owner_queue": queue})

    def test_valid_pending_search_and_owner_checkpoints_are_preserved(self):
        search = {"historical": {"queries": [{"id": "crop", "query": "crop model"}],
                                 "queue": [{"query_id": "crop", "query": "crop model", "page": 2,
                                            "start": FIRST, "end": NEXT}]}, "recent": {}}
        owners = {"owner_queue": [{"kind": "org", "login": "known", "page": 2}],
                  "seed_checks": {"known/model": {"checked_at": FIRST}}}
        paths = [self.root / "state/discovery.json", self.root / "state/refresh.json"]
        save_json(paths[0], search)
        save_json(paths[1], owners)
        before = [path.read_bytes() for path in paths]
        self.assertEqual(validate(self.root)["queries"], 1)
        self.assertEqual([path.read_bytes() for path in paths], before)


if __name__ == "__main__":
    unittest.main()
