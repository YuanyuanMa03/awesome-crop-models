# Durable collection, with explicit limits

Design and GitHub documentation checked on 2026-10-22. This document describes the intended operating model; it is not evidence that a published workflow has run.

The goal is a community-maintained catalogue that keeps collecting after its original author changes research areas. The project must remain useful when a run fails, credentials expire, or maintainers change. No hosted service can promise that a crawler will run forever.

## What the automation can claim

- **Discovery** means that a query returned a repository or a contributor supplied a public source.
- **A completed search pass** means that every planned query shard was fetched without unresolved truncation or incomplete responses, at a recorded time. It does not establish coverage of every crop model on GitHub.
- **A curated entry** requires an explicit relevance decision. Search matches remain candidates until that decision is recorded.
- **Publicly visible** does not establish an open-source licence. Keep unknown or incompatible licence status visible; do not copy model code into this catalogue.
- **A successful health check with no new repositories** is still useful evidence. It must report zero discoveries and must not inflate counts or refresh a failed scan's success timestamp.

GitHub repository search covers names, descriptions, topics, and optionally README text. It cannot search arbitrary repository content through the repository-search endpoint. Forks require explicit inclusion. Therefore query expansion, organization enumeration, model-name seeds, references from existing lists, and community submissions remain necessary complements to keyword search. [GitHub repository-search qualifiers](https://docs.github.com/en/search-github/searching-on-github/searching-for-repositories)

## Search queue and reproducible coverage

The implementation should persist a queue rather than restart an unbounded crawl on every run:

1. Freeze each search pass's upper time boundary and query-set version. Record query text, creation interval, page, fetched time, observed total, received count, and result status.
2. Query a shard's first page. GitHub returns at most 1,000 results per search and at most 100 per page. If a shard exceeds the cap, recursively divide its `created` interval before fetching all pages.
3. Treat timestamps as integer UTC seconds and inclusive intervals: split `[start, end]` into `[start, midpoint]` and `[midpoint + 1 second, end]`. This avoids boundary gaps. GitHub supports date ranges and timestamps with seconds. [Search syntax](https://docs.github.com/en/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax)
4. If even a one-second interval exceeds the cap, save a visible unresolved coverage gap. Additional disjoint partitions may be added only if their union is documented; filtering to popular languages or starred repositories must not masquerade as full coverage.
5. An `incomplete_results: true` response cannot complete a shard. Split or retry within bounded limits, then retain the gap. Deduplicate by numeric repository ID, not only `owner/name`, because repositories can be renamed or transferred.
6. Persist page progress and completed shards atomically. If interrupted, resume pending work. A run that exhausts its configured request budget is partial, not globally complete.

GitHub documents the result cap, separate search limits, and timeout responses. This design's recursive partitioning and queue are mitigation choices, not a GitHub guarantee that search is an exhaustive database export. Results may also change during pagination. [REST search documentation](https://docs.github.com/en/rest/search/search)

Incremental discovery should overlap a recent window and periodically repeat historical queries. New README terms, topics, licence declarations, or renamed models can expose an old repository; an exclusive `created` or `pushed` watermark would miss some such changes. Metadata refresh must rotate fairly through already known repositories. Preserve last-seen identity and status when a repository disappears; do not silently delete its provenance.

A rejected repository is different from one that disappears. Its ID, name and reason stay in `config/excluded.json`, but its full metadata leaves the registry. Most search hits are rejected, so this keeps the committed catalogue compact. GitHub warns about files over 50 MiB and blocks files over 100 MiB. [Large files on GitHub](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github)

## Request and runtime budgets

Use one request queue, finite HTTP timeouts, a finite retry count, a maximum number of requests per run, and a runner timeout. Read rate-limit headers rather than relying only on nominal quotas. GitHub currently documents separate authenticated search limits of 30 requests per minute and a `GITHUB_TOKEN` primary limit of 1,000 REST requests per hour per repository. These are ceilings, not a target request rate. [Search limits](https://docs.github.com/en/rest/search/search), [REST rate limits](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api)

For a rate-limited `403` or `429`, respect `Retry-After`; otherwise respect the reset time when remaining requests are zero. If neither applies to a secondary limit, wait at least one minute, back off exponentially, and stop after bounded retries. A permission-denied `403` is a configuration error, not an invitation to retry indefinitely. Repeated rate-limit abuse can lead to an integration ban. [REST rate-limit handling](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api)

Authenticated conditional requests may reduce metadata-refresh cost when an endpoint returns `304`. Keep requests serial and follow pagination links and redirects. Do not assume search calls or every endpoint will support an effective conditional-cache strategy. [REST integration practices](https://docs.github.com/en/rest/using-the-rest-api/best-practices-for-using-the-rest-api)

Use standard Ubuntu GitHub-hosted runners. Public repositories currently receive free standard hosted execution; larger runners and storage have different billing rules. Keep job duration and request counts bounded, avoid paid model calls, retain compact evidence in Git, and give optional workflow artifacts a short retention period. A fork made private needs its own billing review. [GitHub Actions billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions)

## GitHub Actions operating model

The proposed daily schedule uses a non-round minute and supports `workflow_dispatch` recovery. The workflow must exist on the default branch, and scheduled runs execute its latest commit. GitHub may delay or drop scheduled runs during heavy load, especially at the start of an hour. Public scheduled workflows are automatically disabled after 60 days without repository activity. The minimum supported interval is five minutes; daily collection is sufficient here. UTC is used explicitly for portability. [Workflow events](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule)

The publishing sequence should be:

1. Check out the default branch and run the bounded collector.
2. Save the new search queue and health outcome; keep the last valid catalogue and last successful scan on errors.
3. Validate persisted data and render the list before publishing.
4. Commit only the catalogue, generated list, and explicitly approved state paths if they changed. Never commit credentials, arbitrary runner files, or a checked-out model repository.
5. Preserve a failing exit status after saving a valid failure report. A failed collection must remain visible as a failed Actions run.

Use concurrency control to prevent overlapping writers. On a rejected push, preserve output in logs/artifacts and fail; do not force-push over a maintainer's work. Branch protection or organization policy may prohibit automatic writes and require a different publishing route.

Do not depend on an automatic commit triggering another `push` workflow. Events made with the repository's `GITHUB_TOKEN` normally do not start new workflow runs. GitHub documents exceptions for dispatch events and some automated pull-request events, the latter potentially requiring approval. Run catalogue validation in the same update workflow; do not assume a bot PR creates fully unattended CI. [Triggering workflows from workflows](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow)

The updater may receive `contents: write`; ordinary pull-request validation should remain read-only. Pin third-party actions to verified full commit references from their original repositories, with a version comment, and arrange dependency updates. Do not invent or copy an unverified reference. [Secure use of Actions](https://docs.github.com/en/actions/reference/security/secure-use)

## Honest health records and the inactivity problem

Record substantive health evidence on every attempted collection: attempted/completed time, outcome, request count, queries attempted/completed, pending shards, unresolved gaps, discoveries, and the last successful pass. A run with zero new matches can truthfully update the last-checked record. If nothing changed between scans, a monthly health audit may record the checks actually performed and their outcome.

These are operational records, not dummy commits and not scientific discoveries. No empty commit, random text change, false repository addition, or fabricated success should be used to make the project appear active.

**The official documentation does not precisely define every event counted as repository activity or promise that a bot's audit commit prevents the 60-day rule.** Committing genuine check evidence is a reasonable implementation choice, but it must not be advertised as a guaranteed keepalive. A scheduled workflow also cannot diagnose its own absence while disabled. [Inactivity rule](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule)

For higher durability, an independently operated scheduler can run the same CLI or dispatch the update workflow, and an external check can alert on stale last-attempt/last-success times. Such infrastructure introduces its own owner, availability, authentication, and cost dependencies. It is an optional deployment, not provisioned by this repository's local build.

## Ownership, recovery, and migration

Prefer an organization with at least two owners and multiple maintainers, written relevance criteria, reviewable query configuration, a contribution path, and a permissive framework licence. GitHub itself recommends at least two organization owners for continuity. [Ownership continuity](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/maintaining-ownership-continuity-for-your-organization)

The cron's associated actor remains a dependency. A suspended, deleted, or deprovisioned actor can stop scheduled execution, even when manual execution works. A maintainer with write access can edit the cron expression to reactivate the schedule and become its actor. Handover must therefore include the workflow actor, not just adding another repository collaborator. [Troubleshooting stopped schedules](https://docs.github.com/en/actions/how-tos/troubleshoot-workflows)

Portable operation requires all query configuration, seeds, decisions, identity records, and pending search state in ordinary documented files, plus a CLI that works outside Actions. A successor should be able to clone or fork, run validation, resume a bounded scan, and publish to their own repository without the founder's personal token or computer.

Forked public repositories do not automatically inherit an active schedule. Their new maintainer must enable Actions/workflows, confirm repository permissions, and test a manual run. A new fork must not claim prior workflow runs as its own verification. [Enabling a fork's workflows](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/disable-and-enable-workflows)

Recovery checklist:

- Inspect the recorded attempt and success times, queue status, and Actions history. An old success date is not evidence of current operation.
- Check Actions enablement, the default branch, cron actor status, allowed actions, runner availability, token permissions, and branch rules.
- Resolve configuration errors; run a manual bounded collection and validation; verify the persisted state and catalogue diff.
- Resume pending shards without resetting old failures or silently dropping gaps. Re-enable a disabled schedule and verify a later scheduled run.
- If the host is unavailable, clone the data and run the CLI on another scheduler; preserve source dates and disclose the hosting change.

Permanent unattended operation is conditional on hosting, API policy, search indexing, accounts, permissions, funding where needed, and maintainers capable of recovery. The engineering target is to remove dependence on one researcher's daily attention and make failures visible and recovery transferable.
