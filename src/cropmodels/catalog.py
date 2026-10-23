"""Small, portable JSON catalogue and deterministic Awesome pages."""

import json
import os
import re
import tempfile
from pathlib import Path
from urllib.parse import quote


CROPS = {
    "general-crop": "General and multi-crop", "rice": "Rice", "wheat": "Wheat", "maize": "Maize",
    "other-cereals": "Barley, sorghum, millet and other cereals", "soybean": "Soybean",
    "legumes-oilseeds": "Other legumes and oilseeds", "potato": "Potato",
    "roots-tubers": "Cassava and other roots and tubers", "cotton": "Cotton",
    "sugar-crops": "Sugarcane and sugar beet", "vegetables": "Vegetables",
    "fruit-vine": "Fruit trees and grapevine", "plantation": "Oil palm, coffee, cocoa and other plantation crops",
    "grassland": "Grassland, pasture and forage", "bioenergy-other": "Bioenergy and other crops",
}
PROCESSES = {
    "phenology": "Phenology and development", "photosynthesis": "Photosynthesis, canopy and transpiration",
    "architecture": "Plant architecture and FSPM", "roots": "Roots and rhizosphere",
    "soil-water": "Soil water and heat", "soil-nutrients": "Soil carbon, nitrogen and nutrients",
    "greenhouse-gases": "Agricultural greenhouse gases", "evapotranspiration": "Evapotranspiration and irrigation",
    "weather": "Weather and agroclimate", "pests-diseases": "Pests, diseases and weeds",
    "hydrology": "Hydrology, erosion and watersheds", "land-surface": "Land surface and global vegetation",
    "controlled-environment": "Greenhouses and controlled environments",
}
TOOLS = {
    "frameworks": "Modelling frameworks and platforms", "interfaces": "Model interfaces and wrappers",
    "calibration": "Calibration, sensitivity and uncertainty", "data-assimilation": "Data assimilation and remote sensing",
    "gridded": "Regional and gridded simulation", "model-data": "Inputs, parameters and data",
    "learning": "Tutorials and teaching",
}
SUBJECTS = {**CROPS, **PROCESSES, **TOOLS}
# Entry type -> subjects it may use. A process model specific to one crop goes under that crop.
TYPES = {
    "model": {**CROPS, **PROCESSES}, "tool": TOOLS,
    "application": {**CROPS, **PROCESSES}, "data-driven": {**CROPS, **PROCESSES},
}
# GitHub's linguist labels -> one display language. F* is how linguist labels FST (Fortran
# Simulation Translator) files in Wageningen models.
LANGUAGE_NAMES = {
    "FORTRAN": "Fortran", "F*": "FST", "Jupyter Notebook": "Python", "Matlab": "MATLAB", "RMarkdown": "R",
    "Visual Basic .NET": "Visual Basic", "Visual Basic 6.0": "Visual Basic", "VBA": "Visual Basic", "Delphi": "Pascal",
}
NOT_CODE = {
    "HTML", "CSS", "SCSS", "Less", "TeX", "Roff", "Rich Text Format", "Makefile", "CMake", "Dockerfile",
    "Markdown", "XSLT", "Inno Setup", "NSIS", "Gnuplot", "Vim Script", "PostScript",
}
OTHER_LANGUAGE = "Other"
QUEUE_ROWS = 1000  # the review queue page lists the most-starred candidates only
REPO_NAME = re.compile(r"[A-Za-z0-9][A-Za-z0-9-]*/[A-Za-z0-9_.-]+\Z")


def read_json(path, default=None):
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"{path}: invalid JSON at line {exc.lineno}, column {exc.colno}") from None


def save_json(path, value):
    """Replace complete JSON files, never leave partially written data."""
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, delete=False) as handle:
            temporary = Path(handle.name)
            json.dump(value, handle, ensure_ascii=False, indent=2, sort_keys=True)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        temporary.replace(path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def upsert(registry, metadata, now, seeds=()):
    """Allowlist public metadata; keep identity through renames and transfers."""
    identifier = metadata.get("id")
    name = metadata.get("full_name", "")
    if metadata.get("private") is not False or not isinstance(identifier, int) or isinstance(identifier, bool) or identifier <= 0 or not REPO_NAME.fullmatch(name):
        raise ValueError("Repository must have a public identity, numeric ID and valid owner/name")
    key = str(identifier)
    old = registry.get(key, {})
    aliases = set(old.get("aliases", []))
    if old.get("full_name") and old["full_name"] != name:
        aliases.add(old["full_name"])
    licence = metadata.get("license") or {}
    row = {
        "id": identifier, "full_name": name, "html_url": f"https://github.com/{name}",
        "description": metadata.get("description") or "", "topics": sorted(set(metadata.get("topics") or [])),
        "language": metadata.get("language"), "license_spdx": licence.get("spdx_id"),
        "languages": old.get("languages", {}), "language_status": old.get("language_status", "primary_language_only"),
        "license_name": licence.get("name"), "fork": bool(metadata.get("fork")),
        "parent": (metadata.get("parent") or {}).get("full_name", old.get("parent")),
        "archived": bool(metadata.get("archived")), "default_branch": metadata.get("default_branch"),
        "pushed_at": metadata.get("pushed_at"), "created_at": metadata.get("created_at"),
        "stars": metadata.get("stargazers_count", 0), "visibility": "public", "availability": "available",
        "first_seen_at": old.get("first_seen_at", now), "last_seen_at": now, "last_checked_at": now,
        "aliases": sorted(aliases),
        "discovered_by": sorted(set(old.get("discovered_by", [])) | set(metadata.get("_discovered_by", []))),
        "selection": old.get("selection"), "scientific_review": "not_evaluated",
    }
    # Prefer a seed's verified stable ID; a renamed repository retains its selection.
    for seed in seeds:
        matches_id = seed.get("github_id") == identifier
        matches_name = not seed.get("github_id") and seed["repo"].casefold() == name.casefold()
        if not matches_id and not matches_name:
            continue
        bindings = {r["id"] for r in registry.values() if r.get("selection") and r["selection"]["repo"].casefold() == seed["repo"].casefold()}
        if matches_id or not bindings or identifier in bindings:
            row["selection"] = {k: seed[k] for k in ("repo", "type", "subject", "language", "description") if k in seed}
            break
    registry[key] = row
    return not bool(old)


def selected(registry, seeds):
    """An inclusion decision is explicit; discovery never promotes itself."""
    by_id = {seed["github_id"]: seed for seed in reversed(seeds) if seed.get("github_id")}
    by_name = {seed["repo"].casefold(): seed for seed in reversed(seeds) if not seed.get("github_id")}
    results = []
    for row in registry.values():
        seed = by_id.get(row["id"]) or by_name.get(((row.get("selection") or {}).get("repo") or "").casefold())
        if seed:
            results.append({**row, "selection": seed})
    return results


def language(row):
    """One display language: the curated override, else GitHub's main code language."""
    if row["selection"].get("language"):
        return row["selection"]["language"]
    ranked = [row["language"]] if row.get("language") else []
    ranked += sorted(row.get("languages") or {}, key=lambda name: (-row["languages"][name], name))
    for name in ranked:
        if name not in NOT_CODE:
            return LANGUAGE_NAMES.get(name, name)
    return OTHER_LANGUAGE


def anchor(value):
    return re.sub(r"[^a-z0-9 -]", "", value.lower()).replace(" ", "-")


def language_anchor(subject, language):
    return subject + "-" + anchor(language.replace("+", "plus").replace("#", "sharp").replace("*", "star"))


def text(value):
    return re.sub(r"[\r\n\t]+", " ", str(value)).replace("|", "&#124;").replace("<", "&lt;").replace(">", "&gt;").replace("[", "&#91;").replace("]", "&#93;").strip()


def describe(row, limit=200):
    value = " ".join(str(row["selection"].get("description") or row.get("description") or "").split())
    if len(value) > limit:
        value = value[:limit - 1].rsplit(" ", 1)[0].rstrip(",;:") + "…"
    if value and value[-1] not in ".!?…":
        value += "."
    return text(value) or "No description provided."


def stars(count):
    """A GitHub-style star count: 950, 1.6k, 12k."""
    if count < 1000:
        return str(count)
    return f"{count / 1000:.1f}".rstrip("0").rstrip(".") + "k" if count < 10000 else f"{count // 1000}k"


def entry(row):
    licence = row.get("license_spdx")
    flags = [f"★ {stars(row['stars'])}"] if row.get("stars") else []
    flags.append(licence if licence and licence != "NOASSERTION" else "custom licence" if licence else "no licence")
    flags += [label for label in ("fork", "archived") if row[label]]
    if row["availability"] != "available":
        flags.append(row["availability"].replace("_", " "))
    return f"- [{row['full_name']}]({row['html_url']}) - {describe(row)} " + " ".join(f"`{text(flag)}`" for flag in flags)


def branches(entries, groups):
    """(group, subject, language, repositories) in display order; repositories are ordered by stars."""
    parts = []
    for title, kind, subjects in groups:
        for subject in subjects:
            branch = {}
            for row in entries:
                if row["selection"]["type"] == kind and row["selection"]["subject"] == subject:
                    branch.setdefault(language(row), []).append(row)
            for name in sorted(branch, key=lambda value: (value == OTHER_LANGUAGE, value.casefold())):
                parts.append((title, subject, name, sorted(branch[name], key=lambda row: (-(row.get("stars") or 0), row["full_name"].casefold()))))
    return parts


def paginate(parts, budget=None, notes=None):
    """Body pages of the tree, with an optional note under each group heading. A page that would
    pass budget bytes continues on the next page, which first repeats the headings still open."""
    pages, size, headings, previous = [[]], 0, [], (None, None)
    for title, subject, name, rows in parts:
        level = 1 if title != previous[0] else 2 if subject != previous[1] else 3
        opening = [f"## {title}", ""] if level == 1 else []
        opening += [(notes or {})[title], ""] if level == 1 and title in (notes or {}) else []
        opening += [f'<a id="{subject}"></a>', "", f"### {SUBJECTS[subject]}", ""] if level < 3 else []
        opening += [f'<a id="{language_anchor(subject, name)}"></a>', "", f"#### {name}", ""]
        # Each block opens headings from its level: 1 group, 2 subject, 3 language, 4 none.
        for block_level, lines in [(level, opening + [entry(rows[0])])] + [(4, [entry(row)]) for row in rows[1:]]:
            cost = sum(len(line.encode()) + 1 for line in lines)
            if budget and size and size + cost > budget:
                pages.append([line for heading in headings[:block_level - 1] for line in (f"{heading} (continued)", "")])
                size = sum(len(line.encode()) + 1 for line in pages[-1])
            pages[-1].extend(lines)
            size += cost
            headings = headings[:block_level - 1] + [line for line in lines if line.startswith("#")]
        pages[-1].append("")
        size += 1
        previous = (title, subject)
    return pages


def sections(pages):
    """Page number of each section anchor."""
    where = {}
    for number, lines in enumerate(pages):
        for line in lines:
            if line.startswith('<a id="'):
                where.setdefault(line[7:line.index('"', 7)], number)
            elif line.startswith("## ") and not line.endswith(" (continued)"):
                where.setdefault(anchor(line[3:]), number)
    return where


def contents(parts, link, grouped=True):
    """Contents lines; link(anchor) addresses a section. An ungrouped list starts at subjects."""
    lines, indent = [], "  " if grouped else ""
    for title in dict.fromkeys(part[0] for part in parts):
        group = [part for part in parts if part[0] == title]
        if grouped:
            lines.append(f"- [{title}]({link(anchor(title))}) ({sum(len(part[3]) for part in group)})")
        for subject in dict.fromkeys(part[1] for part in group):
            branch = [part for part in group if part[1] == subject]
            lines.append(f"{indent}- [{SUBJECTS[subject]}]({link(subject)}) ({sum(len(part[3]) for part in branch)})")
            lines.extend(f"{indent}  - [{name}]({link(language_anchor(subject, name))}) ({len(rows)})" for _, _, name, rows in branch)
    return lines


def most_starred(curated, limit=20):
    """Table of the most-starred process-based models and tools."""
    rows = sorted((row for row in curated if row["selection"]["type"] in ("model", "tool")),
                  key=lambda row: (-(row.get("stars") or 0), row["full_name"].casefold()))[:limit]
    lines = ["| # | Repository | Description | Language | ★ |", "|---:|---|---|---|---:|"]
    lines += [f"| {rank} | [{row['full_name']}]({row['html_url']}) | {describe(row, 120)} | {text(language(row))} | {stars(row.get('stars') or 0)} |"
              for rank, row in enumerate(rows, 1)]
    return lines if rows else []


def badge(label, message, colour, link):
    escape = lambda value: quote(str(value).replace("-", "--").replace("_", "__").replace(" ", "_"))
    return f"[![{label}](https://img.shields.io/badge/{escape(label)}-{escape(message)}-{colour}?style=flat-square)]({link})"


# GitHub stops rendering a Markdown file after 500 KiB, so a longer page continues on numbered pages.
PAGE_BYTES = 400_000
# The README lists crop models; every other branch of the tree has its own page.
PAGES = {
    "docs/process-models.md": ("Process models", "process",
                               "Process-based models of soil, water, climate, pests and other agricultural processes that are not specific to one crop. Crop models are listed in the [main tree](../README.md).",
                               [("Process models", "model", PROCESSES)]),
    "docs/tools.md": ("Frameworks and tools", "purpose",
                      "Modelling frameworks, model interfaces and wrappers, calibration and data-assimilation tools, regional simulation, input data and teaching material for crop and agricultural process models.",
                      [("Frameworks and tools", "tool", TOOLS)]),
    "docs/applications.md": ("Applications and case studies", "crop or process",
                             "Repositories that apply a crop, soil or environmental model to a particular study, region or analysis: simulation setups, scenario runs and analysis code. Models themselves are listed in the [main tree](../README.md).",
                             [("Crops", "application", CROPS), ("Processes", "application", PROCESSES)]),
    "docs/data-driven.md": ("Data-driven models", "crop or process",
                            "Statistical and machine-learning models that predict crop variables (yield, growth, phenology, water use) or agricultural process dynamics (soil moisture, evapotranspiration, nutrients) from data. Image classification, crop recommendation and price prediction are out of scope.",
                            [("Crops", "data-driven", CROPS), ("Processes", "data-driven", PROCESSES)]),
}


def write_pages(root, path, title, arrangement, intro, groups, curated):
    """Write one page of the tree, continued on numbered pages; return its README contents line."""
    parts = branches(curated, groups)
    pages = paginate(parts, PAGE_BYTES)
    where = sections(pages)
    names = [Path(path).name] + [f"{Path(path).stem}-{number}.md" for number in range(2, len(pages) + 1)]
    total = sum(len(part[3]) for part in parts)
    back = "Back to [Awesome Crop Models](../README.md)."
    for number, body in enumerate(pages):
        if number == 0:
            more = f" The list continues on {len(pages) - 1} more page{'s' if len(pages) > 2 else ''}." if len(pages) > 1 else ""
            local = lambda target: ("" if where[target] == 0 else names[where[target]]) + f"#{target}"
            lines = [f"# {title}", "", intro, "", f"**{total:,} repositories**, arranged by {arrangement}, then programming language.{more} {back}", "",
                     "## Contents", "", *contents(parts, local, grouped=len(groups) > 1), "", *body]
        else:
            lines = [f"# {title} (page {number + 1} of {len(pages)})", "",
                     f"Continued from [page {number}]({names[number - 1]}). See the [contents]({names[0]}#contents). {back}", "", *body]
        page = "\n".join(lines).rstrip("\n") + "\n"
        if number + 1 < len(pages):
            page += f"\nContinued on [page {number + 2}]({names[number + 1]}).\n"
        (root / Path(path).parent / names[number]).write_text(page, encoding="utf-8")
    for stale in (root / Path(path).parent).glob(f"{Path(path).stem}-*.md"):
        suffix = stale.stem[len(Path(path).stem) + 1:]
        if suffix.isdecimal() and int(suffix) > len(pages):
            stale.unlink()
    if len(groups) > 1:  # crops and processes: too many subjects for one README line
        return f"- [{title}]({path}) ({total:,}), arranged by {arrangement}"
    folder = Path(path).parent.as_posix()
    subjects = " · ".join(f"[{SUBJECTS[subject]}]({folder}/{names[where[subject]]}#{subject})" for subject in dict.fromkeys(part[1] for part in parts))
    return f"- [{title}]({path}) ({total:,})" + (f": {subjects}" if subjects else "")


def render(root):
    registry = read_json(root / "catalog/repositories.json", {})
    seeds = read_json(root / "config/seeds.json", [])
    excluded = read_json(root / "config/excluded.json", {})
    queries = read_json(root / "config/queries.json", [])
    owners = read_json(root / "config/owners.json", [])
    health = read_json(root / "state/health.json", {})
    curated = selected(registry, seeds)
    counts = {kind: sum(row["selection"]["type"] == kind for row in curated) for kind in TYPES}
    tracked = len(set(registry) | set(excluded))
    crop_models = branches(curated, [("Crop models", "model", CROPS)])
    crops = sum(len(part[3]) for part in crop_models)
    starred = most_starred(curated)
    toc = ["- [Most starred](#most-starred)"] if starred else []
    toc.append(f"- [Crop models](#crop-models) ({crops:,})")
    for subject in dict.fromkeys(part[1] for part in crop_models):
        branch = [part for part in crop_models if part[1] == subject]
        languages = " · ".join(f"[{name}](#{language_anchor(subject, name)})" for _, _, name, _ in branch)
        toc.append(f"  - [{SUBJECTS[subject]}](#{subject}) ({sum(len(part[3]) for part in branch):,}): {languages}")
    toc += [write_pages(root, path, title, arrangement, intro, groups, curated) for path, (title, arrangement, intro, groups) in PAGES.items()]
    toc += ["- [Contributing](#contributing)", "- [How this list is built](#how-this-list-is-built)"]
    badges = [badge("repositories", f"{len(curated):,}", "2ea44f", "#contents")]
    if health.get("last_healthy_at"):
        badges.append(badge("last collection", health["last_healthy_at"][:10], "informational", "docs/status.md"))
    badges += [badge("licence", "MIT", "blue", "LICENSE"), badge("PRs", "welcome", "brightgreen", "CONTRIBUTING.md")]
    badge_line = " ".join(badges)
    header = f"""<div align="center">

# Awesome Crop Models [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

**A curated map of open-source crop and agricultural process models on GitHub**<br>crop or process → programming language → repository

{badge_line}

[English](README.md) · [简体中文](docs/README.zh-CN.md) · [Review queue](docs/discovered.md) · [Collection status](docs/status.md)

</div>

Crop growth simulators; soil, water, nutrient and climate process models; the frameworks and tools that run them; studies that apply them; and data-driven yield and process models. Each repository appears once, under its main crop or process and its main programming language, ordered by stars. Crop models are listed below, and the other branches have their own pages. Listing is not a scientific endorsement: check each project's licence before reuse.

> **{len(curated):,} repositories** · {crops:,} crop models · {counts['model'] - crops:,} process models · {counts['tool']:,} frameworks and tools · {counts['application']:,} applications · {counts['data-driven']:,} data-driven models. Screened from {tracked:,} GitHub repositories found by {len(queries)} searches and {len(owners)} maintainer accounts.

## Contents

"""
    footer = f"""## Contributing

Contributions are welcome! Read the [contribution guidelines](CONTRIBUTING.md) first. To add a repository, give it a type and a crop or process in `config/seeds.json`. Unclassified search results wait in the [review queue](docs/discovered.md).

## How this list is built

A dependency-free Python collector searches GitHub with {len(queries)} queries (model names, process terms, crops, several languages and topics), enumerates the accounts of model maintainers, and refreshes metadata of known repositories. A scheduled workflow runs it daily at 03:17 UTC and commits only data, health records and generated pages. Search results are only candidates; a repository is listed only by a recorded decision in `config/seeds.json`.

```bash
python scripts/catalog.py validate
python scripts/catalog.py update --max-requests 160 --discovery-pages 80 --refresh-limit 40
python scripts/catalog.py render
```

Set `GH_TOKEN` or `GITHUB_TOKEN` for GitHub's authenticated quota; never commit a token. GitHub search can miss repositories, so complete coverage cannot be proven. See [collection status](docs/status.md), the [design notes](docs/automation-design.md) and the [maintenance guide](docs/MAINTENANCE.md).

## Related lists

[Awesome Agriculture](https://github.com/brycejohnston/awesome-agriculture) covers agricultural technology broadly. [EDSEL's Awesome Crop Models](https://github.com/EDSEL-skoltech/awesome_crop_models) is an earlier, now archived crop-model list. See [the comparison](docs/competitor-landscape.md).

## Licence

This project's code and original writing use the [MIT licence](LICENSE). Repository metadata comes from GitHub; listed projects keep their own licences and authorship.
"""
    readme = [header + "\n".join(toc), ""]
    if starred:
        readme += ["## Most starred", "", "The most-starred process-based models and tools on the list. Each also appears in its branch of the tree.", "", *starred, ""]
    readme += [*paginate(crop_models, notes={"Crop models": "*Whole-crop and cropping-system models, and process models built for one crop.*"})[0], footer]
    (root / "README.md").write_text("\n".join(readme), encoding="utf-8")
    status = ["# Collection status", "", "Machine-generated operational evidence; this is not a scientific review.", "", "```json", json.dumps(health, ensure_ascii=False, indent=2, sort_keys=True), "```", "", "A partial run resumes on the next attempt. Failed attempts preserve the last healthy timestamp. See state/discovery.json for exact pending time windows and disclosed coverage gaps.", ""]
    (root / "docs/status.md").write_text("\n".join(status), encoding="utf-8")
    listed = {row["id"] for row in curated}
    forks = sum(row["fork"] and row["id"] not in listed for row in registry.values())
    queue = [row for row in registry.values() if row["id"] not in listed and str(row["id"]) not in excluded and not row["fork"]]
    rows = ["# Review queue", "", "Repositories found by discovery that nobody has classified yet. To list one, add it to `config/seeds.json`; to reject one, record it with a reason in `config/excluded.json`. Forks are not listed unless curated.", "",
            f"{tracked} tracked · {len(listed)} listed · {len(excluded)} excluded · {forks} forks · **{len(queue)} awaiting review**", "",
            "| Repository | ★ | Language | Description | Found by |", "|---|---|---|---|---|"]
    queue.sort(key=lambda item: (-(item.get("stars") or 0), item["full_name"].casefold()))
    for row in queue[:QUEUE_ROWS]:
        found = ", ".join(row.get("discovered_by", [])[:2])
        rows.append(f"| [{row['full_name']}]({row['html_url']}) | {row.get('stars') or 0} | {text(row.get('language') or '')} | {text((row.get('description') or '')[:120])} | {text(found)} |")
    if len(queue) > QUEUE_ROWS:
        rows.extend(["", f"The {len(queue) - QUEUE_ROWS} remaining candidates, with fewer stars, are in `catalog/repositories.json`."])
    rows.append("")
    (root / "docs/discovered.md").write_text("\n".join(rows), encoding="utf-8")


def validate(root):
    seeds = read_json(root / "config/seeds.json")
    queries = read_json(root / "config/queries.json")
    owners = read_json(root / "config/owners.json")
    registry = read_json(root / "catalog/repositories.json", {})
    if not seeds or not queries or not owners:
        raise ValueError("Seeds, queries and maintainer accounts must be nonempty")
    ids = [s["github_id"] for s in seeds if "github_id" in s]
    if len({s["repo"].casefold() for s in seeds}) != len(seeds) or len(set(ids)) != len(ids) or len({q["id"] for q in queries}) != len(queries):
        raise ValueError("Seed names, seed IDs and query IDs must be unique")
    for seed in seeds:
        if (not REPO_NAME.fullmatch(seed["repo"]) or seed.get("type") not in TYPES or seed.get("subject") not in TYPES[seed["type"]]
                or ("github_id" in seed and (not isinstance(seed["github_id"], int) or isinstance(seed["github_id"], bool) or seed["github_id"] <= 0))
                or any(not isinstance(seed.get(field, ""), str) for field in ("language", "description"))):
            raise ValueError(f"Invalid seed record: {seed.get('repo')}")
    excluded = read_json(root / "config/excluded.json", {})
    if not isinstance(excluded, dict) or any(not key.isdecimal() or not isinstance(value, dict) or not REPO_NAME.fullmatch(value.get("repo", "")) or not value.get("reason") for key, value in excluded.items()):
        raise ValueError("config/excluded.json must map repository IDs to {repo, reason}")
    if set(map(str, ids)) & set(excluded):
        raise ValueError("A repository cannot be both listed and excluded")
    for query in queries:
        if not query["id"] or not query["query"].strip() or re.search(r"\b(created|pushed|fork|is):", query["query"]):
            raise ValueError("Query scopes are controlled by the collector")
    for owner in owners:
        if owner["kind"] not in ("org", "user") or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9-]*", owner["login"]):
            raise ValueError("Invalid maintainer account")
    for identifier, row in registry.items():
        if not isinstance(row["id"], int) or isinstance(row["id"], bool) or row["id"] <= 0 or identifier != str(row["id"]) or row["visibility"] != "public" or not REPO_NAME.fullmatch(row["full_name"]) or row["html_url"] != f"https://github.com/{row['full_name']}":
            raise ValueError("Invalid catalogue identity")
        if row["scientific_review"] != "not_evaluated":
            raise ValueError("The collector cannot certify scientific review")
    for name in ("discovery", "refresh", "health"):
        state = read_json(root / f"state/{name}.json", {})
        if not isinstance(state, dict):
            raise ValueError(f"state/{name}.json must be an object; restore its last valid version")
        if name == "discovery":
            for lane_name, lane in state.items():
                location = f"state/discovery.json:{lane_name}"
                if lane_name not in ("recent", "historical") or not isinstance(lane, dict):
                    raise ValueError(f"{location} must be a recent/historical lane object")
                for field in ("queue", "queries", "pending_repositories", "coverage_gaps", "completed_windows", "cycle_history"):
                    if field in lane and (not isinstance(lane[field], list) or any(not isinstance(item, dict) for item in lane[field])):
                        raise ValueError(f"{location}.{field} must be a list of objects")
                if not isinstance(lane.get("repo_queries", {}), dict):
                    raise ValueError(f"{location}.repo_queries must be an object")
                ids = {query.get("id") for query in lane.get("queries", [])}
                for job in lane.get("queue", []):
                    if job.get("query_id") not in ids or not isinstance(job.get("page"), int) or isinstance(job["page"], bool) or not 1 <= job["page"] <= 10 or not all(isinstance(job.get(field), str) for field in ("query", "start", "end")):
                        raise ValueError(f"{location}.queue contains an invalid query/page checkpoint")
        if name == "refresh":
            if not isinstance(state.get("seed_checks", {}), dict) or any(not isinstance(check, dict) for check in state.get("seed_checks", {}).values()):
                raise ValueError("state/refresh.json:seed_checks must map names to check objects")
            if not isinstance(state.get("owner_queue", []), list):
                raise ValueError("state/refresh.json:owner_queue must be a list")
            for job in state.get("owner_queue", []):
                if not isinstance(job, dict) or job.get("kind") not in ("org", "user") or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9-]*", job.get("login", "")) or not isinstance(job.get("page"), int) or isinstance(job["page"], bool) or job["page"] < 1:
                    raise ValueError("state/refresh.json:owner_queue contains an invalid account/page checkpoint")
    return {"repositories": len(registry), "seeds": len(seeds), "excluded": len(excluded), "queries": len(queries), "owners": len(owners)}
