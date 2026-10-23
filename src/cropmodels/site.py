"""Static website: the hand-written page in site/ plus JSON exports of the listed catalogue."""

from collections import Counter
import json
import shutil

from .catalog import CROPS, OTHER_LANGUAGE, PROCESSES, TOOLS, language, read_json, selected, sentence

TYPE_CODES = {"model": "m", "tool": "t", "application": "a", "data-driven": "d"}


def licence(row):
    spdx = row.get("license_spdx")
    return "custom" if spdx == "NOASSERTION" else spdx or ""


def build(root, out):
    """Copy site/ to out, then write data/meta.json (summary) and data/catalogue.json (one row per listed repository)."""
    registry = read_json(root / "catalog/repositories.json", {})
    seeds = read_json(root / "config/seeds.json", [])
    excluded = read_json(root / "config/excluded.json", {})
    health = read_json(root / "state/health.json", {})
    curated = sorted(selected(registry, seeds), key=lambda row: (-(row.get("stars") or 0), row["full_name"].casefold()))
    # [name, description, stars, language, type, subject, licence, archived]
    rows = [[row["full_name"], sentence(row), row.get("stars") or 0, language(row), TYPE_CODES[row["selection"]["type"]],
             row["selection"]["subject"], licence(row), int(row["archived"])] for row in curated]
    subjects = {}
    for _, _, _, name, kind, subject, _, _ in rows:
        entry = subjects.setdefault(subject, {"total": 0, "types": Counter(), "languages": Counter()})
        entry["total"] += 1
        entry["types"][kind] += 1
        if name != OTHER_LANGUAGE:
            entry["languages"][name] += 1
    listed = {row["id"] for row in curated}
    meta = {
        "updated": (health.get("last_healthy_at") or "")[:10],
        "listed": len(rows),
        "types": dict(Counter(row[4] for row in rows)),
        "cropModels": sum(row[4] == "m" and row[5] in CROPS for row in rows),
        "tracked": len(set(registry) | set(excluded)),
        "excluded": len(excluded),
        "awaiting": sum(row["id"] not in listed and str(row["id"]) not in excluded and not row["fork"] for row in registry.values()),
        "queries": len(read_json(root / "config/queries.json", [])),
        "owners": len(read_json(root / "config/owners.json", [])),
        "groups": {"crops": list(CROPS), "processes": list(PROCESSES), "tools": list(TOOLS)},
        "labels": {**CROPS, **PROCESSES, **TOOLS},
        "subjects": {subject: {"total": entry["total"], "types": dict(entry["types"]),
                               "languages": [name for name, _ in entry["languages"].most_common(3)]}
                     for subject, entry in subjects.items()},
        "top": [row for row in rows if row[4] in "mt"][:20],
    }
    shutil.copytree(root / "site", out, dirs_exist_ok=True)
    (out / "data").mkdir(exist_ok=True)
    dump = lambda value: json.dumps(value, ensure_ascii=False, separators=(",", ":"))
    (out / "data/meta.json").write_text(dump(meta), encoding="utf-8")
    (out / "data/catalogue.json").write_text(dump(rows), encoding="utf-8")
    return meta
