# Collection status

Machine-generated operational evidence; this is not a scientific review.

```json
{
  "all_github_coverage_verified": false,
  "attempted_at": "2026-10-27T08:57:51Z",
  "coverage_gaps": {
    "historical": 30,
    "recent": 3
  },
  "error": "GitHubError: GitHub returned HTTP 403 for /search/repositories",
  "finished_at": "2026-10-27T08:59:19Z",
  "last_healthy_at": "2026-10-26T08:53:10Z",
  "last_historical_pass_at": null,
  "maintainer_accounts": {
    "cycle": 4,
    "new_repositories": 68,
    "observed_at": "2026-10-27T08:57:51Z",
    "pages": 10,
    "remaining_accounts_or_pages": 24
  },
  "new_repository_identities": 2,
  "owner_listing_gaps": 0,
  "pending_search_jobs": {
    "historical": 411,
    "recent": 300
  },
  "previous_healthy_at": "2026-10-26T08:53:10Z",
  "refresh": {
    "checked_repositories": 40,
    "known_identities": 28150,
    "new_repositories": 0,
    "observed_at": "2026-10-27T08:57:51Z",
    "seed_count": 15291
  },
  "requests": 110,
  "status": "failed",
  "tracked_repositories": 28152
}
```

A partial run resumes on the next attempt. Failed attempts preserve the last healthy timestamp. See state/discovery.json for exact pending time windows and disclosed coverage gaps.
