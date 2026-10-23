"""Complement keyword search with known identities and maintainer accounts."""

from .catalog import upsert
from .github import NotFound


def refresh(client, registry, state, seeds, now, limit):
    """Rotate seed checks and known identities without either starving."""
    checks = state.setdefault("seed_checks", {})
    known_seed_names = {row.get("selection", {}).get("repo", "").casefold()
                        for row in registry.values() if row.get("selection")}
    missing = [seed for seed in seeds if
               (str(seed["github_id"]) not in registry if seed.get("github_id")
                else seed["repo"].casefold() not in known_seed_names)]
    missing.sort(key=lambda seed: (checks.get(seed["repo"], {}).get("checked_at", ""), seed["repo"].casefold()))
    known = sorted(registry.values(), key=lambda row: (row["last_checked_at"], row["id"]))
    targets = []
    for index in range(max(len(missing), len(known))):
        if index < len(missing):
            targets.append((None, missing[index]))
        if index < len(known):
            targets.append((known[index]["id"], None))
    # An odd one-request budget alternates the two source groups across runs.
    if limit == 1 and missing and known and state.get("single_refresh_group") == "seed":
        targets.insert(0, targets.pop(1))
    checked = new = 0
    for identifier, seed in targets[:limit]:
        state["single_refresh_group"] = "seed" if seed else "known"
        name = seed["repo"] if seed else registry[str(identifier)]["full_name"]
        stable_id = identifier or (seed or {}).get("github_id")
        path = f"/repositories/{stable_id}" if stable_id else f"/repos/{name}"
        try:
            metadata = client.get(path)
        except NotFound:
            if identifier:
                registry[str(identifier)]["availability"] = "not_found_or_inaccessible"
                registry[str(identifier)]["last_checked_at"] = now
            checks[name] = {"checked_at": now, "outcome": "not_found_or_inaccessible"}
            checked += 1
            continue
        if metadata.get("private") is not False:
            if identifier:
                registry[str(identifier)]["availability"] = "no_longer_public_or_unverified"
                registry[str(identifier)]["last_checked_at"] = now
            checks[name] = {"checked_at": now, "outcome": "nonpublic_response_not_saved"}
            checked += 1
            continue
        if stable_id and metadata.get("id") != stable_id:
            raise ValueError("Stable repository ID did not match API response")
        new += upsert(registry, metadata, now, seeds)
        row = registry[str(metadata["id"])]
        # A separate languages read records all reported languages, not only the dominant one.
        try:
            languages = client.get(f"/repos/{row['full_name']}/languages")
        except NotFound:
            row["language_status"] = "endpoint_unavailable"
        else:
            if not isinstance(languages, dict) or any(not isinstance(k, str) or not isinstance(v, int) or isinstance(v, bool) or v < 0 for k, v in languages.items()):
                raise ValueError("Invalid GitHub languages response")
            row["languages"] = {k: v for k, v in sorted(languages.items()) if v > 0}
            row["language_status"] = "github_languages_endpoint"
        checks[name] = {"checked_at": now, "outcome": "public_metadata_checked"}
        checked += 1
    report = {"checked_repositories": checked, "new_repositories": new,
              "known_identities": len(registry), "seed_count": len(seeds), "observed_at": now}
    state["last_refresh"] = report
    return report


def enumerate_owners(client, registry, state, owners, seeds, now, max_pages=10):
    plan = [{"login": row["login"], "kind": row["kind"]} for row in owners]
    if state.get("owner_plan") != plan or not state.get("owner_queue"):
        state["owner_plan"] = plan
        state["owner_queue"] = [{**owner, "page": 1} for owner in plan]
        state["owner_cycle"] = state.get("owner_cycle", 0) + 1
    queue = state["owner_queue"]
    new = checked = 0
    while queue and checked < max_pages:
        job = queue[0]
        prefix = "orgs" if job["kind"] == "org" else "users"
        params = {"per_page": 100, "page": job["page"], "sort": "full_name", "direction": "asc",
                  "type": "public" if prefix == "orgs" else "owner"}
        try:
            items = client.get(f"/{prefix}/{job['login']}/repos", params=params)
        except NotFound:
            state.setdefault("owner_gaps", []).append({"login": job["login"], "observed_at": now, "reason": "account_not_found_or_inaccessible"})
            del queue[0]
            checked += 1
            continue
        if not isinstance(items, list):
            raise ValueError("Invalid maintainer repository listing")
        for metadata in items:
            if metadata.get("private") is not False:
                continue
            metadata = {**metadata, "_discovered_by": [f"owner:{job['login']}"]}
            new += upsert(registry, metadata, now, seeds)
        del queue[0]
        if len(items) == 100:
            queue.append({**job, "page": job["page"] + 1})
        checked += 1
    report = {"pages": checked, "new_repositories": new, "remaining_accounts_or_pages": len(queue),
              "cycle": state["owner_cycle"], "observed_at": now}
    state["last_owner_scan"] = report
    return report
