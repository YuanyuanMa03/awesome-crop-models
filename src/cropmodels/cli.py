"""CLI shared by a local checkout and the scheduled GitHub workflow."""

import argparse
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path

from .catalog import read_json, render, save_json, upsert, validate
from .discovery import discover
from .github import BudgetExceeded, GitHubClient
from .site import build
from .sources import enumerate_owners, refresh


def utc_now():
    return datetime.now(timezone.utc).replace(microsecond=0).strftime("%Y-%m-%dT%H:%M:%SZ")


def update(root, client, now, discovery_pages=80, refresh_limit=40, owner_pages=10):
    validate(root)
    registry = read_json(root / "catalog/repositories.json", {})
    seeds = read_json(root / "config/seeds.json")
    queries = read_json(root / "config/queries.json")
    owners = read_json(root / "config/owners.json")
    excluded = read_json(root / "config/excluded.json", {})
    discovery = read_json(root / "state/discovery.json", {"historical": {}, "recent": {}})
    discovery.setdefault("historical", {})
    discovery.setdefault("recent", {})
    refresh_state = read_json(root / "state/refresh.json", {})
    previous = read_json(root / "state/health.json", {})
    report = {"attempted_at": now, "status": "running", "previous_healthy_at": previous.get("last_healthy_at"),
              "last_healthy_at": previous.get("last_healthy_at"),
              "last_historical_pass_at": previous.get("last_historical_pass_at"),
              "all_github_coverage_verified": False}
    before = set(registry)
    exit_code = 0
    try:
        report["refresh"] = refresh(client, registry, refresh_state, seeds, now, refresh_limit)
        report["maintainer_accounts"] = enumerate_owners(client, registry, refresh_state, owners, seeds, now, owner_pages)
        recent_pages = min(20, discovery_pages // 3)
        if recent_pages:
            since = (datetime.fromisoformat(now.replace("Z", "+00:00")) - timedelta(days=30)).strftime("%Y-%m-%dT%H:%M:%SZ")
            _, report["recent_search"] = discover(client, discovery["recent"], queries, now, max_pages=recent_pages, since=since)
        if discovery_pages - recent_pages:
            _, report["historical_search"] = discover(client, discovery["historical"], queries, now, max_pages=discovery_pages - recent_pages)
        lanes = [discovery[lane] for lane in ("recent", "historical")]
        completed = all(lane.get("plan_completed") for lane in lanes)
        current_gaps = any(lane.get("last_run", {}).get("coverage_gaps") for lane in lanes)
        report["status"] = "completed_with_gaps" if completed and current_gaps else "completed_plan" if completed else "partial"
        if getattr(client, "successful_responses", 0):
            report["last_healthy_at"] = now
        elif not client.requests:
            report["status"] = "idle"
        historical_run = report.get("historical_search", {})
        if historical_run.get("plan_completed") and historical_run.get("requests", 0) and not historical_run.get("coverage_gaps"):
            report["last_historical_pass_at"] = now
    except BudgetExceeded:
        report["status"] = "partial_budget"
        if getattr(client, "successful_responses", 0):
            report["last_healthy_at"] = now
    except Exception as exc:
        report["status"] = "failed"
        report["error"] = f"{type(exc).__name__}: {exc}"
        exit_code = 1
    finally:
        # Commit data before advancing the search checkpoint. If the second write
        # fails, a resumed run may reread a page but cannot lose its repositories.
        for lane in ("recent", "historical"):
            for metadata in discovery[lane].get("pending_repositories", []):
                try:
                    upsert(registry, metadata, now, seeds)
                except ValueError:
                    report["status"] = "failed"
                    report["error"] = "Rejected invalid public repository metadata; valid prior pages were retained"
                    report["rejected_repository_records"] = report.get("rejected_repository_records", 0) + 1
                    exit_code = 1
            discovery[lane]["pending_repositories"] = []
        # A rejected repository is remembered in config/excluded.json only, keeping the catalogue small.
        for identifier in excluded:
            registry.pop(identifier, None)
            for lane in ("recent", "historical"):
                discovery[lane].get("repo_queries", {}).pop(identifier, None)
        report["new_repository_identities"] = len(set(registry) - before)
        report["tracked_repositories"] = len(registry)
        report["requests"] = client.requests
        report["finished_at"] = utc_now()
        report["pending_search_jobs"] = {lane: len(discovery[lane].get("queue", [])) for lane in ("recent", "historical")}
        report["coverage_gaps"] = {lane: len(discovery[lane].get("coverage_gaps", [])) for lane in ("recent", "historical")}
        report["owner_listing_gaps"] = len(refresh_state.get("owner_gaps", []))
        if report["status"] == "failed":
            report["last_healthy_at"] = previous.get("last_healthy_at")
            report["last_historical_pass_at"] = previous.get("last_historical_pass_at")
        save_json(root / "catalog/repositories.json", registry)
        save_json(root / "state/discovery.json", discovery)
        save_json(root / "state/refresh.json", refresh_state)
        save_json(root / "state/health.json", report)
        render(root)
    return report, exit_code


def main(argv=None):
    parser = argparse.ArgumentParser(description="A living Awesome list and resumable public crop-model discovery")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("render", help="Regenerate the Awesome tree, candidate list and status")
    sub.add_parser("validate", help="Check catalogue/config/state offline")
    sub.add_parser("status", help="Print the most recent real collection outcome")
    site = sub.add_parser("site", help="Build the static website (site/ plus catalogue data) into a folder")
    site.add_argument("--out", type=Path, default=Path("_site"))
    collect = sub.add_parser("update", help="Run a bounded public-API update and save resumable progress")
    collect.add_argument("--max-requests", type=int, default=160)
    collect.add_argument("--discovery-pages", type=int, default=80)
    collect.add_argument("--refresh-limit", type=int, default=40)
    collect.add_argument("--owner-pages", type=int, default=10)
    args = parser.parse_args(argv)
    root = args.root.resolve()
    if args.command == "render":
        render(root)
        print("Rendered README.md, docs/discovered.md and docs/status.md")
    elif args.command == "validate":
        print(json.dumps(validate(root), indent=2))
    elif args.command == "site":
        meta = build(root, args.out.resolve())
        print(f"Built the website for {meta['listed']} repositories in {args.out}")
    elif args.command == "status":
        print(json.dumps(read_json(root / "state/health.json", {"status": "not_run"}), ensure_ascii=False, indent=2))
    else:
        if any(getattr(args, name) < 0 for name in ("max_requests", "discovery_pages", "refresh_limit", "owner_pages")):
            parser.error("Budgets must be nonnegative")
        report, code = update(root, GitHubClient(args.max_requests), utc_now(), args.discovery_pages, args.refresh_limit, args.owner_pages)
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return code
    return 0
