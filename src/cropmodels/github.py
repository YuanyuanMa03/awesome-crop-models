"""Bounded, rate-aware reads of GitHub's public REST API."""

import json
import os
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import HTTPRedirectHandler, Request, build_opener


class GitHubError(RuntimeError):
    pass


class NotFound(GitHubError):
    pass


class BudgetExceeded(GitHubError):
    pass


class RateLimited(GitHubError):
    pass


class ApiRedirects(HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, message, headers, newurl):
        if not newurl.startswith("https://api.github.com/"):
            raise GitHubError("Refused an API redirect outside api.github.com")
        return super().redirect_request(request, fp, code, message, headers, newurl)


class GitHubClient:
    def __init__(self, max_requests=160, token=None, opener=None, sleep=time.sleep):
        self.max_requests = max_requests
        self.requests = 0
        self.successful_responses = 0
        self.token = token if token is not None else os.environ.get("GH_TOKEN", os.environ.get("GITHUB_TOKEN", ""))
        self.opener = opener or build_opener(ApiRedirects())
        self.sleep = sleep
        self.last_search = None

    def get(self, path, params=None):
        if not path.startswith("/") or path.startswith("//") or "?" in path:
            raise ValueError("Use a relative API path and a separate params dictionary")
        url = "https://api.github.com" + path
        if params:
            url += "?" + urlencode(params)
        headers = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28", "User-Agent": "awesome-crop-models/0.1"}
        if self.token:
            headers["Authorization"] = "Bearer " + self.token
        for attempt in range(3):
            if self.requests >= self.max_requests:
                raise BudgetExceeded(f"Request budget exhausted ({self.requests})")
            if path.startswith("/search/"):
                interval = 2.1 if self.token else 6.1
                if self.last_search is not None:
                    self.sleep(max(0, interval - (time.monotonic() - self.last_search)))
                self.last_search = time.monotonic()
            self.requests += 1
            try:
                with self.opener.open(Request(url, headers=headers), timeout=30) as response:
                    result = json.load(response)
                    self.successful_responses += 1
                    return result
            except HTTPError as exc:
                if exc.code in (404, 410):
                    raise NotFound(f"GitHub returned {exc.code} for {path}") from None
                if exc.code == 429 or (exc.code == 403 and (exc.headers.get("Retry-After") or exc.headers.get("X-RateLimit-Remaining") == "0")):
                    raise RateLimited(f"GitHub rate limit reached for {path}; resume on a later run") from None
                if exc.code >= 500 and attempt < 2:
                    self.sleep(2 ** attempt)
                    continue
                raise GitHubError(f"GitHub returned HTTP {exc.code} for {path}") from None
            except (URLError, TimeoutError, OSError) as exc:
                if attempt < 2:
                    self.sleep(2 ** attempt)
                    continue
                raise GitHubError(f"GitHub connection failed ({type(exc).__name__}) for {path}") from None
        raise GitHubError(f"GitHub request failed for {path}")
