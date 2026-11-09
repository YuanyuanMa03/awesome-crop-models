# Collection status

Machine-generated operational evidence; this is not a scientific review.

```json
{
  "all_github_coverage_verified": false,
  "attempted_at": "2026-11-09T11:28:26Z",
  "coverage_gaps": {
    "historical": 190,
    "recent": 3
  },
  "finished_at": "2026-11-09T11:33:03Z",
  "last_healthy_at": "2026-11-09T11:28:26Z",
  "last_historical_pass_at": null,
  "maintainer_accounts": {
    "cycle": 7,
    "new_repositories": 97,
    "observed_at": "2026-11-09T11:28:26Z",
    "pages": 10,
    "remaining_accounts_or_pages": 14
  },
  "new_repository_identities": 65,
  "owner_listing_gaps": 0,
  "pending_search_jobs": {
    "historical": 68,
    "recent": 45
  },
  "previous_healthy_at": "2026-11-08T10:18:40Z",
  "recent_search": {
    "completed_windows": 482,
    "coverage_gaps": [
      {
        "cycle": 2,
        "end": "2026-10-22T11:09:10Z",
        "page": 1,
        "query_id": "crop-alfalfa",
        "reason": "incomplete_results",
        "reported_total": 1,
        "start": "2026-09-22T11:09:10Z"
      },
      {
        "cycle": 2,
        "end": "2026-10-22T11:09:10Z",
        "page": 1,
        "query_id": "crop-alfalfa",
        "reason": "short_page_before_reported_total",
        "reported_total": 1,
        "returned": 0,
        "start": "2026-09-22T11:09:10Z"
      },
      {
        "cycle": 2,
        "end": "2026-10-22T11:09:10Z",
        "page": 1,
        "query_id": "dd-crop-yield-prediction",
        "reason": "incomplete_results",
        "reported_total": 239,
        "start": "2026-09-22T11:09:10Z"
      }
    ],
    "coverage_note": "Completion means this query plan was traversed. GitHub search is mutable, may omit repositories, and does not prove coverage of all GitHub.",
    "cycle": 2,
    "cycle_end": "2026-10-22T11:09:10Z",
    "cycle_start": "2026-09-22T11:09:10Z",
    "cycle_started_at": "2026-10-22T11:09:10Z",
    "discovered_repositories": 29,
    "observed_at": "2026-11-09T11:28:26Z",
    "plan_completed": false,
    "remaining_jobs": 45,
    "requests": 20,
    "status": "partial",
    "unresolved_gap_count": 3
  },
  "refresh": {
    "checked_repositories": 40,
    "known_identities": 28500,
    "new_repositories": 0,
    "observed_at": "2026-11-09T11:28:26Z",
    "seed_count": 15291
  },
  "requests": 160,
  "status": "partial_budget",
  "tracked_repositories": 28565
}
```

A partial run resumes on the next attempt. Failed attempts preserve the last healthy timestamp. See state/discovery.json for exact pending time windows and disclosed coverage gaps.
