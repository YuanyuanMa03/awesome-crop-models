import json
from pathlib import Path
import tempfile
import unittest

from cropmodels.catalog import save_json, upsert
from cropmodels.site import build


FIRST = "2026-10-21T03:17:00Z"


def metadata(identifier, name, stars=0, **extra):
    return {"id": identifier, "full_name": name, "private": False, "description": "A crop model",
            "license": {"spdx_id": "MIT", "name": "MIT License"}, "language": "Python",
            "stargazers_count": stars, **extra}


class SiteTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        (self.root / "site").mkdir()
        (self.root / "site/index.html").write_text("<!doctype html>", encoding="utf-8")
        seeds = [
            {"repo": "a/wheat", "github_id": 1, "type": "model", "subject": "wheat", "description": "Wheat growth"},
            {"repo": "b/wrapper", "github_id": 2, "type": "tool", "subject": "interfaces"},
            {"repo": "c/yield", "github_id": 3, "type": "data-driven", "subject": "maize", "language": "R"},
        ]
        registry = {}
        upsert(registry, metadata(1, "a/wheat", 5), FIRST, seeds)
        upsert(registry, metadata(2, "b/wrapper", 40, license={"spdx_id": "NOASSERTION"}, archived=True), FIRST, seeds)
        upsert(registry, metadata(3, "c/yield", 900), FIRST, seeds)
        upsert(registry, metadata(4, "d/candidate"), FIRST, seeds)
        upsert(registry, metadata(5, "e/fork", fork=True), FIRST, seeds)
        save_json(self.root / "catalog/repositories.json", registry)
        save_json(self.root / "config/seeds.json", seeds)
        save_json(self.root / "config/excluded.json", {"9": {"repo": "x/noise", "reason": "off-topic"}})
        save_json(self.root / "config/queries.json", [{"id": "crop", "query": "crop model"}])
        save_json(self.root / "config/owners.json", [{"kind": "org", "login": "test"}])
        save_json(self.root / "state/health.json", {"last_healthy_at": FIRST})

    def test_build_copies_the_page_and_exports_listed_repositories_by_stars(self):
        out = self.root / "_site"
        build(self.root, out)
        self.assertEqual((out / "index.html").read_text(), "<!doctype html>")
        rows = json.loads((out / "data/catalogue.json").read_text())
        self.assertEqual(rows, [
            ["c/yield", "A crop model.", 900, "R", "d", "maize", "MIT", 0],
            ["b/wrapper", "A crop model.", 40, "Python", "t", "interfaces", "custom", 1],
            ["a/wheat", "Wheat growth.", 5, "Python", "m", "wheat", "MIT", 0],
        ])
        meta = json.loads((out / "data/meta.json").read_text())
        self.assertEqual((meta["listed"], meta["cropModels"], meta["tracked"], meta["excluded"], meta["awaiting"]), (3, 1, 6, 1, 1))
        self.assertEqual(meta["types"], {"d": 1, "t": 1, "m": 1})
        self.assertEqual(meta["subjects"]["maize"], {"total": 1, "types": {"d": 1}, "languages": ["R"]})
        self.assertEqual([row[0] for row in meta["top"]], ["b/wrapper", "a/wheat"])
        self.assertEqual(meta["updated"], "2026-10-21")


if __name__ == "__main__":
    unittest.main()
