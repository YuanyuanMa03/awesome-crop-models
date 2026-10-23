import copy
from datetime import datetime, timedelta, timezone
import unittest

from cropmodels.discovery import discover


EPOCH = "2007-01-01T00:00:00Z"
NOW = "2026-10-22T10:00:00Z"
QUERIES = [{"id": "crop", "query": "crop model"}]


def repo(identifier, name=None, private=False):
    return {"id": identifier, "full_name": name or f"owner/model-{identifier}", "private": private}


def page(total=0, items=None, incomplete=False):
    return {"total_count": total, "items": items or [], "incomplete_results": incomplete}


class Client:
    def __init__(self, responses):
        self.responses = responses
        self.calls = []

    def get(self, path, params=None):
        self.calls.append((path, copy.deepcopy(params)))
        response = self.responses(params) if callable(self.responses) else self.responses.pop(0)
        if isinstance(response, Exception):
            raise response
        return response


class DiscoveryTests(unittest.TestCase):
    def test_searches_public_non_forks_in_fixed_creation_window(self):
        state = {}
        client = Client([page(1, [repo(10)])])
        found, report = discover(client, state, QUERIES, NOW)
        path, params = client.calls[0]
        self.assertEqual(path, "/search/repositories")
        self.assertIn("is:public created:", params["q"])
        self.assertNotIn("fork:", params["q"])
        self.assertIn(f"created:{EPOCH}..{NOW}", params["q"])
        self.assertEqual(params["per_page"], 100)
        self.assertEqual(found[0]["_discovered_by"], ["crop"])
        self.assertTrue(report["plan_completed"])
        self.assertIn("does not prove", report["coverage_note"])

    def test_over_limit_splits_into_nonoverlapping_inclusive_seconds(self):
        now = "2007-01-01T00:00:03Z"
        state = {}
        client = Client([page(1001)])
        _, report = discover(client, state, QUERIES, now, max_pages=1)
        self.assertEqual(report["status"], "partial")
        left, right = state["queue"]
        self.assertEqual((left["start"], left["end"]), (EPOCH, "2007-01-01T00:00:01Z"))
        self.assertEqual((right["start"], right["end"]), ("2007-01-01T00:00:02Z", now))
        self.assertEqual(left["page"], 1)
        self.assertFalse(state["completed_windows"])

    def test_large_minute_is_split_down_to_seconds_and_records_cap(self):
        state = {}
        now = "2007-01-01T00:01:00Z"
        client = Client(lambda params: page(1001))
        _, report = discover(client, state, QUERIES, now, max_pages=200)
        self.assertTrue(report["plan_completed"])
        windows = state["completed_windows"]
        self.assertEqual(len(windows), 61)
        seconds = sorted(window["start"] for window in windows)
        expected = [
            (datetime(2007, 1, 1, tzinfo=timezone.utc) + timedelta(seconds=i)).strftime("%Y-%m-%dT%H:%M:%SZ")
            for i in range(61)
        ]
        self.assertEqual(seconds, expected)
        self.assertTrue(all(window["start"] == window["end"] for window in windows))
        capped = [gap for gap in report["coverage_gaps"] if gap["reason"] == "search_cap_at_one_second"]
        self.assertEqual(len(capped), 61)
        self.assertGreater(report["unresolved_gap_count"], 0)

    def test_exactly_1000_results_fit_ten_pages_without_splitting(self):
        def respond(params):
            start = (params["page"] - 1) * 100 + 1
            return page(1000, [repo(i) for i in range(start, start + 100)])

        state = {}
        found, report = discover(Client(respond), state, QUERIES, NOW)
        self.assertEqual(len(found), 1000)
        self.assertEqual(report["requests"], 10)
        self.assertTrue(report["plan_completed"])
        self.assertEqual(report["completed_windows"], 1)
        self.assertEqual(report["coverage_gaps"], [])

    def test_full_page_continues_and_budget_resumes_at_next_page(self):
        state = {}
        first = Client([page(100, [repo(i) for i in range(1, 101)])])
        _, report = discover(first, state, QUERIES, NOW, max_pages=1)
        self.assertEqual(report["status"], "partial")
        self.assertEqual(state["queue"][0]["page"], 2)
        second = Client([page(100)])
        found, report = discover(second, state, QUERIES, "2026-10-23T10:00:00Z", max_pages=1)
        self.assertEqual(second.calls[0][1]["page"], 2)
        self.assertIn(f"..{NOW}", second.calls[0][1]["q"])
        self.assertEqual(len(found), 100)
        self.assertTrue(report["plan_completed"])
        self.assertEqual(report["cycle_end"], NOW)

    def test_incomplete_response_retains_gap_even_if_plan_finishes(self):
        state = {}
        _, report = discover(Client([page(0, incomplete=True)]), state, QUERIES, NOW)
        self.assertTrue(report["plan_completed"])
        self.assertEqual(report["coverage_gaps"][0]["reason"], "incomplete_results")
        self.assertEqual(state["coverage_gaps"], report["coverage_gaps"])

    def test_short_page_and_count_drift_are_disclosed(self):
        state = {}
        client = Client([
            page(300, [repo(i) for i in range(1, 101)]),
            page(250, [repo(101)]),
        ])
        _, report = discover(client, state, QUERIES, NOW)
        reasons = {gap["reason"] for gap in report["coverage_gaps"]}
        self.assertIn("result_count_changed", reasons)
        self.assertIn("short_page_before_reported_total", reasons)
        self.assertEqual(state["completed_windows"][0]["fetched_items"], 101)

    def test_queries_round_robin_despite_many_split_windows(self):
        queries = [{"id": "big", "query": "big"}, {"id": "small", "query": "small"}]
        client = Client(lambda params: page(1001) if params["q"].startswith("big ") else
                        page(200, [repo(i) for i in range(1, 101)]))
        state = {}
        discover(client, state, queries, NOW, max_pages=4)
        self.assertEqual([params["q"].split()[0] for _, params in client.calls], ["big", "small", "big", "small"])
        resumed = Client(lambda params: page(0))
        discover(resumed, state, queries, NOW, max_pages=1)
        self.assertTrue(resumed.calls[0][1]["q"].startswith("big "))

    def test_completed_cycle_rescans_old_repositories(self):
        state = {}
        discover(Client([page(0)]), state, QUERIES, NOW)
        state["pending_repositories"] = []
        client = Client([page(1, [repo(7)])])
        found, report = discover(client, state, QUERIES, "2026-10-23T10:00:00Z")
        self.assertEqual(report["cycle"], 2)
        self.assertEqual(found[0]["id"], 7)
        self.assertIn(f"created:{EPOCH}..2026-10-23T10:00:00Z", client.calls[0][1]["q"])
        self.assertEqual(len(state["cycle_history"]), 2)

    def test_same_id_rename_merges_query_provenance(self):
        state = {}
        queries = [{"id": "first", "query": "a"}, {"id": "second", "query": "b"}]
        client = Client([page(1, [repo(42, "old/name")]), page(1, [repo(42, "new/name")])])
        found, _ = discover(client, state, queries, NOW)
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0]["full_name"], "new/name")
        self.assertEqual(found[0]["_discovered_by"], ["first", "second"])
        self.assertEqual(state["repo_queries"]["42"], ["first", "second"])

    def test_private_missing_or_unknown_public_status_are_excluded(self):
        state = {}
        items = [repo(1), repo(2, private=True), {"private": False}, {"id": 4}, repo(True)]
        found, report = discover(Client([page(5, items)]), state, QUERIES, NOW)
        self.assertEqual([item["id"] for item in found], [1])
        self.assertEqual(report["coverage_gaps"][0]["reason"], "nonpublic_or_invalid_items")
        self.assertEqual(report["coverage_gaps"][0]["count"], 4)

    def test_api_failure_keeps_job_and_previous_pages_in_outbox(self):
        state = {}
        client = Client([page(150, [repo(i) for i in range(1, 101)]), RuntimeError("rate limit")])
        with self.assertRaisesRegex(RuntimeError, "rate limit"):
            discover(client, state, QUERIES, NOW)
        self.assertEqual(state["queue"][0]["page"], 2)
        self.assertEqual(len(state["pending_repositories"]), 100)
        self.assertEqual(state["last_run"]["status"], "interrupted")
        self.assertEqual(state["last_run"]["requests"], 2)
        resumed = Client([page(150, [repo(i) for i in range(101, 151)])])
        found, report = discover(resumed, state, QUERIES, NOW)
        self.assertEqual(resumed.calls[0][1]["page"], 2)
        self.assertEqual(len(found), 150)
        self.assertEqual(len(state["pending_repositories"]), 150)
        self.assertTrue(report["plan_completed"])

    def test_invalid_response_keeps_current_job_and_outbox(self):
        state = {}
        client = Client([page(100, [repo(i) for i in range(1, 101)]), {"items": []}])
        with self.assertRaises(KeyError):
            discover(client, state, QUERIES, NOW)
        self.assertEqual(state["queue"][0]["page"], 2)
        self.assertEqual(len(state["pending_repositories"]), 100)

    def test_zero_budget_preserves_pending_without_requests(self):
        state = {"pending_repositories": [repo(1)]}
        client = Client([])
        found, report = discover(client, state, QUERIES, NOW, max_pages=0)
        self.assertEqual(len(found), 1)
        self.assertEqual(client.calls, [])
        self.assertEqual(report["requests"], 0)
        self.assertFalse(report["plan_completed"])

    def test_new_query_plan_preserves_prior_gaps_and_pending(self):
        state = {}
        discover(Client([page(1, [repo(1)], incomplete=True)]), state, QUERIES, NOW)
        queries = [{"id": "new", "query": "new"}]
        found, report = discover(Client([page(0)]), state, queries, NOW)
        self.assertEqual(len(found), 1)
        self.assertEqual(report["cycle"], 2)
        self.assertEqual(report["coverage_gaps"], [])
        self.assertEqual(report["unresolved_gap_count"], 1)

    def test_duplicate_page_results_are_disclosed(self):
        state = {}
        duplicate = [repo(i) for i in range(1, 101)]
        _, report = discover(Client([page(200, duplicate), page(200, [repo(1)])]), state, QUERIES, NOW)
        self.assertIn("duplicate_items_across_pages", {gap["reason"] for gap in report["coverage_gaps"]})

    def test_recent_lane_slides_window_only_after_cycle_completion(self):
        state = {}
        first_since = "2026-09-22T10:00:00Z"
        first = Client([page(0)])
        _, report = discover(first, state, QUERIES, NOW, since=first_since)
        self.assertEqual(report["cycle_start"], first_since)
        fingerprint = state["plan_fingerprint"]
        second_since = "2026-09-23T10:00:00Z"
        second_now = "2026-10-23T10:00:00Z"
        second = Client([page(0)])
        _, report = discover(second, state, QUERIES, second_now, since=second_since)
        self.assertEqual(report["cycle"], 2)
        self.assertEqual(state["plan_fingerprint"], fingerprint)
        self.assertIn(f"created:{second_since}..{second_now}", second.calls[0][1]["q"])

    def test_in_progress_recent_lane_ignores_new_since_and_now(self):
        state = {}
        since = "2026-09-22T10:00:00Z"
        first = Client([page(100, [repo(i) for i in range(1, 101)])])
        discover(first, state, QUERIES, NOW, max_pages=1, since=since)
        second = Client([page(100)])
        _, report = discover(second, state, QUERIES, "2026-10-23T10:00:00Z",
                             since="2026-09-23T10:00:00Z")
        self.assertEqual(report["cycle"], 1)
        self.assertIn(f"created:{since}..{NOW}", second.calls[0][1]["q"])
        self.assertEqual(second.calls[0][1]["page"], 2)

    def test_invalid_inputs_make_no_requests(self):
        for queries, now, budget in [
            ([], NOW, 1), (QUERIES * 2, NOW, 1),
            (QUERIES, "2026-01-01T00:00:00", 1), (QUERIES, NOW, -1),
        ]:
            with self.subTest(queries=queries, now=now, budget=budget):
                client = Client([])
                with self.assertRaises(ValueError):
                    discover(client, {}, queries, now, budget)
                self.assertEqual(client.calls, [])


if __name__ == "__main__":
    unittest.main()
