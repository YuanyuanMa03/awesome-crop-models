# Collection status

Machine-generated operational evidence; this is not a scientific review.

```json
{
  "all_github_coverage_verified": false,
  "attempted_at": "2026-11-07T10:04:25Z",
  "coverage_gaps": {
    "historical": 157,
    "recent": 3
  },
  "finished_at": "2026-11-07T10:09:31Z",
  "last_healthy_at": "2026-11-07T10:04:25Z",
  "last_historical_pass_at": null,
  "maintainer_accounts": {
    "cycle": 6,
    "new_repositories": 24,
    "observed_at": "2026-11-07T10:04:25Z",
    "pages": 5,
    "remaining_accounts_or_pages": 0
  },
  "new_repository_identities": 22,
  "owner_listing_gaps": 0,
  "pending_search_jobs": {
    "historical": 97,
    "recent": 85
  },
  "previous_healthy_at": "2026-11-06T10:50:43Z",
  "recent_search": {
    "completed_windows": 442,
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
    "discovered_repositories": 5,
    "observed_at": "2026-11-07T10:04:25Z",
    "plan_completed": false,
    "remaining_jobs": 85,
    "requests": 20,
    "status": "partial",
    "unresolved_gap_count": 3
  },
  "refresh": {
    "checked_repositories": 40,
    "known_identities": 28395,
    "new_repositories": 0,
    "observed_at": "2026-11-07T10:04:25Z",
    "seed_count": 15291
  },
  "requests": 160,
  "status": "partial_budget",
  "tracked_repositories": 28417
}
```

A partial run resumes on the next attempt. Failed attempts preserve the last healthy timestamp. See state/discovery.json for exact pending time windows and disclosed coverage gaps.
