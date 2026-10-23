"""Resumable, budgeted GitHub repository search (not a completeness proof)."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
import hashlib
import json


_EPOCH = "2007-01-01T00:00:00Z"
_COVERAGE_NOTE = (
    "Completion means this query plan was traversed. GitHub search is mutable, "
    "may omit repositories, and does not prove coverage of all GitHub."
)


def _timestamp(value: str) -> str:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("now must include a UTC offset")
    return parsed.astimezone(timezone.utc).replace(microsecond=0).strftime("%Y-%m-%dT%H:%M:%SZ")


def _datetime(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def _job(query: dict, start: str, end: str) -> dict:
    return {
        "query_id": query["id"], "query": query["query"],
        "start": start, "end": end, "page": 1,
        "last_total": None, "fetched_items": 0, "seen_ids": [],
    }


def _gap(state: dict, job: dict, reason: str, **details) -> None:
    gap = {
        "cycle": state["cycle"], "query_id": job["query_id"],
        "start": job["start"], "end": job["end"],
        "page": job["page"], "reason": reason, **details,
    }
    if gap not in state["coverage_gaps"]:
        state["coverage_gaps"].append(gap)


def _repo_id(repository: dict) -> int | None:
    value = repository.get("id")
    if isinstance(value, str) and value.isdecimal():
        value = int(value)
    if isinstance(value, int) and not isinstance(value, bool) and value > 0:
        return value
    return None


def _pending(state: dict) -> dict[int, dict]:
    pending = {}
    for repository in state.setdefault("pending_repositories", []):
        identifier = _repo_id(repository)
        if identifier is not None and repository.get("private") is False:
            previous = pending.get(identifier, {})
            provenance = list(dict.fromkeys(
                previous.get("_discovered_by", []) + repository.get("_discovered_by", [])
            ))
            pending[identifier] = {**repository, "id": identifier, "_discovered_by": provenance}
    state["pending_repositories"] = list(pending.values())
    return pending


def _begin_cycle(state: dict, queries: list[dict], fingerprint: str, now: str, since: str) -> None:
    if state.get("cycle") and not state.get("plan_completed"):
        state.setdefault("cycle_history", []).append({
            "cycle": state["cycle"], "status": "superseded",
            "plan_fingerprint": state.get("plan_fingerprint"),
            "cycle_end": state.get("cycle_end"),
            "completed_windows": len(state.get("completed_windows", [])),
        })
    state.update({
        "plan_fingerprint": fingerprint, "queries": queries,
        "cycle": state.get("cycle", 0) + 1,
        "cycle_started_at": now, "cycle_start": since, "cycle_end": now,
        "queue": [_job(query, since, now) for query in queries],
        "completed_windows": [], "plan_completed": False,
        "last_query_id": None,
    })
    state.setdefault("coverage_gaps", [])
    state.setdefault("repo_queries", {})
    state.setdefault("cycle_history", [])


def _next_job(state: dict) -> tuple[int, dict]:
    """Round-robin query IDs, independently of how many windows each has."""
    query_ids = [query["id"] for query in state["queries"]]
    last = state.get("last_query_id")
    start = query_ids.index(last) + 1 if last in query_ids else 0
    for offset in range(len(query_ids)):
        identifier = query_ids[(start + offset) % len(query_ids)]
        for index, job in enumerate(state["queue"]):
            if job["query_id"] == identifier:
                return index, job
    raise ValueError("search queue has no job matching the query plan")


def _report(state: dict, now: str, requests: int, status: str) -> dict:
    report = {
        "status": status, "plan_completed": state["plan_completed"],
        "cycle": state["cycle"], "requests": requests,
        "remaining_jobs": len(state["queue"]),
        "completed_windows": len(state["completed_windows"]),
        "coverage_gaps": [gap for gap in state["coverage_gaps"] if gap["cycle"] == state["cycle"]],
        "unresolved_gap_count": len(state["coverage_gaps"]),
        "discovered_repositories": len(state["pending_repositories"]),
        "cycle_started_at": state["cycle_started_at"],
        "cycle_start": state["cycle_start"], "cycle_end": state["cycle_end"],
        "observed_at": now, "coverage_note": _COVERAGE_NOTE,
    }
    state["last_run"] = report
    return report


def discover(
    client, state: dict, queries: list[dict], now: str, max_pages: int = 40,
    since: str | None = None,
) -> tuple[list[dict], dict]:
    """Search at most ``max_pages`` times, updating ``state`` after each page.

    The caller must persist state in ``finally``. It must also merge
    ``state['pending_repositories']`` into its catalog before clearing that list;
    successful pages survive a later API exception through this outbox.
    A subsequent call after plan completion begins a fresh cycle. ``since``
    defaults to full history, and only sets the window when a new cycle starts.
    """
    now = _timestamp(now)
    if now < _EPOCH:
        raise ValueError("now must be on or after 2007-01-01")
    if not isinstance(max_pages, int) or isinstance(max_pages, bool) or max_pages < 0:
        raise ValueError("max_pages must be a nonnegative integer")
    plan = [{"id": query["id"], "query": query["query"]} for query in queries]
    if not plan or any(not isinstance(q["id"], str) or not q["id"] or
                       not isinstance(q["query"], str) or not q["query"].strip() for q in plan):
        raise ValueError("queries need nonempty string id and query fields")
    if len({query["id"] for query in plan}) != len(plan):
        raise ValueError("query IDs must be unique")
    fingerprint = hashlib.sha256(json.dumps(plan, sort_keys=True).encode()).hexdigest()
    if state.get("plan_fingerprint") != fingerprint or state.get("plan_completed"):
        start = _timestamp(since) if since is not None else _EPOCH
        if not _EPOCH <= start <= now:
            raise ValueError("since must be between 2007-01-01 and now")
        _begin_cycle(state, plan, fingerprint, now, start)
    pending = _pending(state)
    requests = 0
    _report(state, now, requests, "partial")

    while state["queue"] and requests < max_pages:
        index, job = _next_job(state)
        params = {
            "q": f'{job["query"]} is:public created:{job["start"]}..{job["end"]}',
            "per_page": 100, "page": job["page"], "sort": "updated", "order": "asc",
        }
        requests += 1
        try:
            response = client.get("/search/repositories", params=params)
            total = response["total_count"]
            items = response["items"]
            if not isinstance(total, int) or isinstance(total, bool) or total < 0 or not isinstance(items, list):
                raise ValueError("invalid GitHub search response")
            if any(not isinstance(item, dict) for item in items):
                raise ValueError("invalid repository item in GitHub search response")
        except Exception:
            _report(state, now, requests, "interrupted")
            raise

        state["last_query_id"] = job["query_id"]
        if response.get("incomplete_results", False):
            _gap(state, job, "incomplete_results", reported_total=total)
        if job["last_total"] is not None and job["last_total"] != total:
            _gap(state, job, "result_count_changed", previous_total=job["last_total"], reported_total=total)
        job["last_total"] = total

        seen = set(job["seen_ids"])
        invalid = duplicates = 0
        for repository in items:
            identifier = _repo_id(repository)
            if identifier is None or repository.get("private") is not False:
                invalid += 1
                continue
            if identifier in seen:
                duplicates += 1
            seen.add(identifier)
            provenance = state["repo_queries"].setdefault(str(identifier), [])
            for query_id in repository.get("_discovered_by", []) + [job["query_id"]]:
                if query_id not in provenance:
                    provenance.append(query_id)
            existing_provenance = pending.get(identifier, {}).get("_discovered_by", [])
            merged = list(dict.fromkeys(existing_provenance + provenance))
            pending[identifier] = {**repository, "id": identifier, "_discovered_by": merged}
        state["pending_repositories"] = list(pending.values())
        job["seen_ids"] = sorted(seen)
        job["fetched_items"] += len(items)
        if invalid:
            _gap(state, job, "nonpublic_or_invalid_items", count=invalid)
        if duplicates:
            _gap(state, job, "duplicate_items_across_pages", count=duplicates)

        if total > 1000 and job["start"] < job["end"]:
            start, end = _datetime(job["start"]), _datetime(job["end"])
            middle = start + timedelta(seconds=int((end - start).total_seconds()) // 2)
            left_end = middle.strftime("%Y-%m-%dT%H:%M:%SZ")
            right_start = (middle + timedelta(seconds=1)).strftime("%Y-%m-%dT%H:%M:%SZ")
            query = {"id": job["query_id"], "query": job["query"]}
            state["queue"][index:index + 1] = [
                _job(query, job["start"], left_end), _job(query, right_start, job["end"])
            ]
        else:
            if total > 1000:
                _gap(state, job, "search_cap_at_one_second", reported_total=total, accessible_limit=1000)
            if len(items) < 100 and (job["page"] - 1) * 100 + len(items) < min(total, 1000):
                _gap(state, job, "short_page_before_reported_total", reported_total=total, returned=len(items))
            if len(items) < 100 or job["page"] >= 10:
                state["completed_windows"].append({
                    "query_id": job["query_id"], "start": job["start"], "end": job["end"],
                    "pages": job["page"], "reported_total": total,
                    "fetched_items": job["fetched_items"], "unique_repositories": len(seen),
                })
                del state["queue"][index]
            else:
                job["page"] += 1
        _report(state, now, requests, "partial")

    if not state["queue"]:
        state["plan_completed"] = True
        state["cycle_history"].append({
            "cycle": state["cycle"], "status": "completed",
            "plan_fingerprint": fingerprint, "cycle_end": state["cycle_end"],
            "completed_windows": len(state["completed_windows"]),
            "coverage_gaps": sum(gap["cycle"] == state["cycle"] for gap in state["coverage_gaps"]),
        })
    status = "completed" if state["plan_completed"] else "partial"
    return list(pending.values()), _report(state, now, requests, status)
