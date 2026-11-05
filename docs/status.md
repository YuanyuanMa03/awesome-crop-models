# Collection status

Machine-generated operational evidence; this is not a scientific review.

```json
{
  "all_github_coverage_verified": false,
  "attempted_at": "2026-11-05T10:52:57Z",
  "coverage_gaps": {
    "historical": 117,
    "recent": 3
  },
  "finished_at": "2026-11-05T10:57:34Z",
  "last_healthy_at": "2026-11-05T10:52:57Z",
  "last_historical_pass_at": null,
  "maintainer_accounts": {
    "cycle": 6,
    "new_repositories": 97,
    "observed_at": "2026-11-05T10:52:57Z",
    "pages": 10,
    "remaining_accounts_or_pages": 14
  },
  "new_repository_identities": 19,
  "owner_listing_gaps": 0,
  "pending_search_jobs": {
    "historical": 102,
    "recent": 125
  },
  "previous_healthy_at": "2026-11-04T10:53:17Z",
  "recent_search": {
    "completed_windows": 402,
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
    "discovered_repositories": 186,
    "observed_at": "2026-11-05T10:52:57Z",
    "plan_completed": false,
    "remaining_jobs": 125,
    "requests": 20,
    "status": "partial",
    "unresolved_gap_count": 3
  },
  "refresh": {
    "checked_repositories": 40,
    "known_identities": 28338,
    "new_repositories": 0,
    "observed_at": "2026-11-05T10:52:57Z",
    "seed_count": 15291
  },
  "requests": 160,
  "status": "partial_budget",
  "tracked_repositories": 28357
}
```

A partial run resumes on the next attempt. Failed attempts preserve the last healthy timestamp. See state/discovery.json for exact pending time windows and disclosed coverage gaps.
