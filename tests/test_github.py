import io
import json
import unittest
from unittest.mock import patch
from urllib.error import HTTPError, URLError
from urllib.request import Request

from cropmodels.github import (
    ApiRedirects, BudgetExceeded, GitHubClient, GitHubError, NotFound, RateLimited,
)


class Opener:
    def __init__(self, outcomes):
        self.outcomes = iter(outcomes)
        self.calls = []

    def open(self, request, timeout):
        self.calls.append((request, timeout))
        outcome = next(self.outcomes)
        if isinstance(outcome, Exception):
            raise outcome
        return io.BytesIO(json.dumps(outcome).encode())


def http_error(code, headers=None, secret=""):
    return HTTPError(
        "https://api.github.com/repos/test/model?secret=" + secret,
        code, "server detail " + secret, headers or {}, io.BytesIO(secret.encode()),
    )


class GitHubClientTests(unittest.TestCase):
    def test_authenticated_request_has_fixed_host_and_separate_encoded_query(self):
        opener = Opener([{"items": []}])
        client = GitHubClient(token="test-only-secret", opener=opener)
        self.assertEqual(client.get("/search/repositories", {"q": "crop model fork:true"}), {"items": []})
        request, timeout = opener.calls[0]
        self.assertEqual(request.full_url, "https://api.github.com/search/repositories?q=crop+model+fork%3Atrue")
        self.assertEqual(request.get_header("Authorization"), "Bearer test-only-secret")
        self.assertNotIn("test-only-secret", request.full_url)
        self.assertGreater(timeout, 0)

    def test_invalid_api_paths_never_reach_the_opener(self):
        opener = Opener([])
        client = GitHubClient(opener=opener)
        for path in ("https://evil.example/repos", "//evil.example/repos", "repos/a/b", "/repos/a/b?token=x"):
            with self.subTest(path=path), self.assertRaises(ValueError):
                client.get(path)
        self.assertEqual(opener.calls, [])

    def test_request_budget_includes_failed_attempts(self):
        opener = Opener([http_error(503), {"unexpected": "must not be requested"}])
        client = GitHubClient(max_requests=1, token="secret", opener=opener, sleep=lambda _: None)
        with self.assertRaises(BudgetExceeded):
            client.get("/repos/test/model")
        self.assertEqual(client.requests, 1)
        self.assertEqual(len(opener.calls), 1)

    def test_zero_budget_does_not_make_a_request(self):
        opener = Opener([])
        with self.assertRaises(BudgetExceeded):
            GitHubClient(max_requests=0, opener=opener).get("/repos/test/model")
        self.assertEqual(opener.calls, [])

    def test_transient_server_errors_retry_and_can_recover(self):
        waits = []
        opener = Opener([http_error(502), http_error(503), {"id": 7}])
        client = GitHubClient(opener=opener, sleep=waits.append)
        self.assertEqual(client.get("/repos/test/model"), {"id": 7})
        self.assertEqual(len(opener.calls), 3)
        self.assertEqual(waits, [1, 2])

    def test_server_error_retries_are_bounded_and_do_not_expose_details(self):
        secret = "test-token-not-for-logs"
        opener = Opener([http_error(503, secret=secret) for _ in range(3)])
        client = GitHubClient(token=secret, opener=opener, sleep=lambda _: None)
        with self.assertRaises(GitHubError) as result:
            client.get("/repos/test/model")
        self.assertEqual(len(opener.calls), 3)
        self.assertNotIn(secret, str(result.exception))

    def test_connection_failures_retry_without_exposing_exception_reason(self):
        secret = "test-token-not-for-logs"
        opener = Opener([URLError(secret), TimeoutError(secret), OSError(secret)])
        waits = []
        client = GitHubClient(token=secret, opener=opener, sleep=waits.append)
        with self.assertRaises(GitHubError) as result:
            client.get("/repos/test/model")
        self.assertEqual(len(opener.calls), 3)
        self.assertEqual(waits, [1, 2])
        self.assertNotIn(secret, str(result.exception))

    def test_rate_limits_stop_this_run_without_an_immediate_retry(self):
        cases = [(429, {}), (403, {"X-RateLimit-Remaining": "0"}), (403, {"Retry-After": "120"})]
        for code, headers in cases:
            with self.subTest(code=code, headers=headers):
                opener = Opener([http_error(code, headers)])
                waits = []
                client = GitHubClient(opener=opener, sleep=waits.append)
                with self.assertRaises(RateLimited):
                    client.get("/repos/test/model")
                self.assertEqual(len(opener.calls), 1)
                self.assertEqual(waits, [])

    def test_permission_denied_is_not_misreported_as_a_rate_limit(self):
        opener = Opener([http_error(403)])
        with self.assertRaises(GitHubError) as result:
            GitHubClient(opener=opener).get("/repos/test/model")
        self.assertNotIsInstance(result.exception, RateLimited)
        self.assertEqual(len(opener.calls), 1)

    def test_missing_or_gone_repository_is_not_retried(self):
        for code in (404, 410):
            with self.subTest(code=code):
                opener = Opener([http_error(code)])
                with self.assertRaises(NotFound):
                    GitHubClient(opener=opener).get("/repos/test/model")
                self.assertEqual(len(opener.calls), 1)

    def test_search_requests_are_paced_even_with_an_instant_response(self):
        waits = []
        client = GitHubClient(token="test-only-token", opener=Opener([{}, {}]), sleep=waits.append)
        with patch("cropmodels.github.time.monotonic", return_value=0):
            client.get("/search/repositories", {"q": "crop"})
            client.get("/search/repositories", {"q": "wheat"})
        self.assertEqual(len(waits), 1)
        self.assertGreaterEqual(waits[0], 2)


class RedirectTests(unittest.TestCase):
    def test_redirect_cannot_forward_credentials_to_another_host(self):
        request = Request("https://api.github.com/repos/a/b", headers={"Authorization": "Bearer local-test-token"})
        targets = [
            "https://evil.example/collect", "http://api.github.com/repos/a/b",
            "https://api.github.com.evil.example/collect", "https://api.github.com@evil.example/collect",
        ]
        for target in targets:
            with self.subTest(target=target), self.assertRaises(GitHubError) as result:
                ApiRedirects().redirect_request(request, None, 302, "Found", {}, target)
            self.assertNotIn("local-test-token", str(result.exception))

    def test_same_api_host_redirect_supports_renamed_repositories(self):
        request = Request("https://api.github.com/repos/old/model", headers={"Authorization": "Bearer local-test-token"})
        redirected = ApiRedirects().redirect_request(
            request, None, 301, "Moved", {}, "https://api.github.com/repositories/123",
        )
        self.assertEqual(redirected.full_url, "https://api.github.com/repositories/123")
        self.assertEqual(redirected.get_header("Authorization"), "Bearer local-test-token")


if __name__ == "__main__":
    unittest.main()
