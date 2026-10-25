# Collection status

Machine-generated operational evidence; this is not a scientific review.

```json
{
  "all_github_coverage_verified": false,
  "attempted_at": "2026-10-25T08:23:33Z",
  "coverage_gaps": {
    "historical": 28,
    "recent": 0
  },
  "finished_at": "2026-10-25T08:27:04Z",
  "last_healthy_at": "2026-10-25T08:23:33Z",
  "last_historical_pass_at": null,
  "maintainer_accounts": {
    "cycle": 3,
    "new_repositories": 124,
    "observed_at": "2026-10-25T08:23:33Z",
    "pages": 10,
    "remaining_accounts_or_pages": 5
  },
  "new_repository_identities": 4,
  "owner_listing_gaps": 0,
  "pending_search_jobs": {
    "historical": 453,
    "recent": 334
  },
  "previous_healthy_at": "2026-10-24T08:06:24Z",
  "recent_search": {
    "completed_windows": 192,
    "coverage_gaps": [],
    "coverage_note": "Completion means this query plan was traversed. GitHub search is mutable, may omit repositories, and does not prove coverage of all GitHub.",
    "cycle": 2,
    "cycle_end": "2026-10-22T11:09:10Z",
    "cycle_start": "2026-09-22T11:09:10Z",
    "cycle_started_at": "2026-10-22T11:09:10Z",
    "discovered_repositories": 16,
    "observed_at": "2026-10-25T08:23:33Z",
    "plan_completed": false,
    "remaining_jobs": 334,
    "requests": 20,
    "status": "partial",
    "unresolved_gap_count": 0
  },
  "refresh": {
    "checked_repositories": 40,
    "known_identities": 28145,
    "new_repositories": 0,
    "observed_at": "2026-10-25T08:23:33Z",
    "seed_count": 15291
  },
  "requests": 160,
  "status": "partial_budget",
  "tracked_repositories": 28149
}
```

A partial run resumes on the next attempt. Failed attempts preserve the last healthy timestamp. See state/discovery.json for exact pending time windows and disclosed coverage gaps.
