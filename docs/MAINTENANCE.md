# Maintenance and handover

The directory should be able to outlive its founder's research role. Keep at least two organization owners and more than one maintainer when organizational hosting is available. The collector needs a Python interpreter, GitHub API access, the saved JSON files and a scheduler; it does not require the founder's machine, account token, private dataset or an AI provider.

## Publish and activate

1. Review this standalone project's code, seed decisions, licence, public metadata and generated files. Do not copy a private research workspace into it.
2. Create the intended public repository and push this project's default branch. This local build does not create a remote or publish anything.
3. Enable Actions and permit the update workflow's repository token to write contents. Organization rules and branch protection may require a reviewed publishing process instead of automatic pushes.
4. Run **Collect crop model repositories** manually. Verify its API outcome, pending queue, committed health record and resulting README tree.
5. Verify a subsequent scheduled run at 03:17 UTC. Manual success does not prove the schedule works. In a fork, explicitly enable its workflows.

## The ordinary update

`python scripts/catalog.py update` performs a bounded run. It prioritizes missing seed identities, rotates older metadata checks, enumerates maintainer accounts, then continues recent and historical query lanes. All sources are read-only public API queries; it never executes code from the repositories it finds.

Generated paths are `catalog/repositories.json`, `state/discovery.json`, `state/refresh.json`, `state/health.json`, `README.md` and the generated pages in `docs/`: `process-models.md`, `tools.md`, `applications.md`, `data-driven.md`, `discovered.md` and `status.md`. Keep these files together. The registry is saved before its search checkpoint: a crash may repeat a page, and stable-ID merging makes that safe.

GitHub truncates a README after 500 KiB, so a generated page whose entries would pass 400 KB continues on numbered pages (`data-driven-2.md`, …), and rendering deletes numbered pages that are no longer needed. The registry holds listed and unreviewed repositories only: a rejected repository is remembered in `config/excluded.json`, and each update drops it from the registry and from search provenance. This keeps `catalog/repositories.json` far below GitHub's 50 MiB warning and 100 MiB push limit.

Every valid update record contains an attempt time, actual outcome, request count, new identity count, pending jobs and retained coverage observations. A zero-discovery run records zero. A request-budget stop is partial. API errors remain failed workflow outcomes and preserve the prior healthy time.

To test or regenerate without networking:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
python scripts/catalog.py validate
python scripts/catalog.py render
```

## Review a newly found repository

New search results appear in the [review queue](discovered.md). For each one, read the author's own description and decide:

- **List it**: add a record to `config/seeds.json` with `github_id`, a `type` (`model`, `tool`, `application` or `data-driven`) and one `subject`. Add a `language` override when GitHub's primary language misrepresents the code, and a `description` when GitHub's is missing or not in English. [CONTRIBUTING.md](../CONTRIBUTING.md) lists the subjects and the scope rules.
- **Reject it**: add `"<github_id>": {"repo": "owner/name", "reason": "..."}` to `config/excluded.json`, so it leaves the queue for good. The next update also removes its metadata from the registry.

Forks never enter the queue. Do not infer every crop a model family supports, or guess implementation languages from papers.

`config/queries.json` expands search coverage. Do not add popularity, language, `created`, `pushed`, `fork` or visibility restrictions to hide missing results; the collector controls creation-time partitioning and visibility, and leaves forks out. `config/owners.json` is an additional public-account enumeration route; its repositories remain candidates until reviewed.

## Recover a stale or failed collection

1. Inspect `state/health.json`, `docs/status.md` and Actions logs. Old success timestamps can be stale.
2. Check Actions enablement, default branch, scheduled-workflow actor, token permissions, runner access, branch protection and rate limits. A schedule can be disabled after prolonged repository inactivity; genuine bot records are not a guaranteed keepalive.
3. Keep all saved state. Resolve the failure and run the same command or dispatch manually. Do not delete queues or old failures simply to produce a green status.
4. After restoring a schedule, verify a real later scheduled run. If the cron actor has left, an authorized maintainer can edit the cron expression and confirm the new actor operates correctly.
5. If GitHub scheduling is unsuitable, run this same CLI from an independently operated systemd timer, cron or other scheduler. Provisioning and monitoring that external scheduler are separate deployment tasks.

Changes to query configuration begin a new query cycle while retaining known identities and prior gap evidence. Historical searches repeat so that old repositories with newly descriptive README/topics can be rediscovered. Repository names can change; IDs and aliases preserve continuity. Public repositories that become inaccessible remain recorded with an explicit status rather than silently disappearing.

See the [officially sourced automation design](automation-design.md) for platform limits and ownership continuity. The project has no guarantee of permanent hosting or complete search indexing; its practical promise is transparent progress, portable state and recoverability.
