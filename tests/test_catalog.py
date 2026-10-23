import copy
import json
from pathlib import Path
import re
import tempfile
import unittest
from unittest.mock import patch

from cropmodels.catalog import language, read_json, render, save_json, selected, upsert, validate


FIRST = "2026-10-21T03:17:00Z"
LATER = "2026-10-22T03:17:00Z"


def metadata(identifier=12, name="test/model", **extra):
    row = {
        "id": identifier, "full_name": name, "private": False,
        "description": "A crop model", "topics": ["wheat", "crop-model", "wheat"],
        "license": {"spdx_id": "MIT", "name": "MIT License"}, "language": "Python",
        "languages": {"Python": 500, "Fortran": 200},
    }
    row.update(extra)
    return row


def seed(name="test/model", identifier=12, **extra):
    return {
        "repo": name, "github_id": identifier, "type": "model", "subject": "general-crop",
        "description": "A process-based crop simulation model.", **extra,
    }


class CatalogueTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        (self.root / "docs").mkdir()
        self.seeds = [seed()]
        self.registry = {}
        upsert(self.registry, metadata(), FIRST, self.seeds)
        save_json(self.root / "config/seeds.json", self.seeds)
        save_json(self.root / "config/queries.json", [{"id": "crop", "query": "crop model in:readme"}])
        save_json(self.root / "config/owners.json", [{"kind": "org", "login": "test"}])
        self.save_registry()

    def save_registry(self):
        save_json(self.root / "catalog/repositories.json", self.registry)

    def test_upsert_drops_non_allowlisted_old_and_incoming_fields(self):
        self.registry["12"]["legacy_private_note"] = "must disappear"
        source = metadata(
            owner={"email": "not-catalogued@example.test"}, permissions={"admin": True},
            token="not-a-real-token", private_notes="unpublished work", html_url="https://evil.example/model",
            _discovered_by=["process-query"],
        )
        upsert(self.registry, source, LATER, self.seeds)
        row = self.registry["12"]
        for key in ("owner", "permissions", "token", "private_notes", "legacy_private_note", "_discovered_by"):
            self.assertNotIn(key, row)
        self.assertEqual(row["html_url"], "https://github.com/test/model")
        self.assertEqual(row["topics"], ["crop-model", "wheat"])
        self.assertEqual(row["discovered_by"], ["process-query"])
        self.assertEqual(row["scientific_review"], "not_evaluated")

    def test_invalid_or_private_identity_cannot_mutate_the_registry(self):
        bad = [metadata(private=True), metadata(private=None), metadata(name="invalid-name")]
        bad.extend(metadata(identifier=value) for value in (True, False, 0, -1, 12.0, "12", None))
        for source in bad:
            with self.subTest(source=source):
                before = copy.deepcopy(self.registry)
                with self.assertRaises(ValueError):
                    upsert(self.registry, source, LATER, self.seeds)
                self.assertEqual(self.registry, before)

    def test_stable_identity_preserves_selection_aliases_and_provenance_after_rename(self):
        upsert(self.registry, metadata(_discovered_by=["query-b"]), FIRST, self.seeds)
        source = metadata(name="successor/renamed", _discovered_by=["query-a", "query-b"])
        self.assertFalse(upsert(self.registry, source, LATER, self.seeds))
        row = self.registry["12"]
        self.assertEqual(len(self.registry), 1)
        self.assertEqual(row["aliases"], ["test/model"])
        self.assertEqual(row["first_seen_at"], FIRST)
        self.assertEqual(row["last_seen_at"], LATER)
        self.assertEqual(row["discovered_by"], ["query-a", "query-b"])
        self.assertEqual([item["id"] for item in selected(self.registry, self.seeds)], [12])

    def test_seed_with_explicit_id_does_not_select_a_different_same_named_repo(self):
        registry = {}
        upsert(registry, metadata(identifier=99), FIRST, self.seeds)
        self.assertIsNone(registry["99"]["selection"])
        self.assertEqual(selected(registry, self.seeds), [])

    def test_reused_name_does_not_keep_a_withdrawn_stable_id_selected(self):
        new_seeds = [seed(identifier=99)]
        upsert(self.registry, metadata(identifier=99), LATER, new_seeds)
        self.assertEqual([item["id"] for item in selected(self.registry, new_seeds)], [99])

    def test_withdrawing_a_seed_removes_it_from_the_selected_page(self):
        save_json(self.root / "config/seeds.json", [seed("other/model", 99)])
        render(self.root)
        readme = (self.root / "README.md").read_text()
        discovered = (self.root / "docs/discovered.md").read_text()
        self.assertIn("**0 repositories:**", readme)
        self.assertNotIn("[test/model]", readme)
        self.assertIn("| [test/model](https://github.com/test/model) |", discovered)
        self.assertIn("**1 awaiting review**", discovered)

    def test_render_is_deterministic_across_registry_and_seed_order(self):
        other_seed = seed("aaa/crop", 3)
        self.seeds.append(other_seed)
        upsert(self.registry, metadata(3, "aaa/crop"), FIRST, self.seeds)
        save_json(self.root / "config/seeds.json", self.seeds)
        self.save_registry()
        render(self.root)
        paths = ("README.md", "docs/process-models.md", "docs/tools.md", "docs/applications.md", "docs/data-driven.md", "docs/discovered.md", "docs/status.md")
        before = {path: (self.root / path).read_bytes() for path in paths}
        self.registry = dict(reversed(list(self.registry.items())))
        self.save_registry()
        save_json(self.root / "config/seeds.json", list(reversed(self.seeds)))
        render(self.root)
        self.assertEqual(before, {path: (self.root / path).read_bytes() for path in paths})
        self.assertLess(before["README.md"].index(b"[aaa/crop]"), before["README.md"].index(b"[test/model]"))

    def test_language_prefers_override_then_normalised_main_code_language(self):
        def resolve(primary, languages=None, override=None):
            row = {"language": primary, "languages": languages or {}, "selection": {"language": override} if override else {}}
            return language(row)

        self.assertEqual(resolve("Python", override="C++"), "C++")
        self.assertEqual(resolve("F*"), "FST")
        self.assertEqual(resolve("Jupyter Notebook"), "Python")
        self.assertEqual(resolve("FORTRAN"), "Fortran")
        self.assertEqual(resolve("HTML", {"HTML": 900, "R": 300, "CSS": 400}), "R")
        self.assertEqual(resolve(None, {"TeX": 10}), "Other")

    def test_validate_rejects_subjects_outside_the_entry_type(self):
        for bad in (seed(type="tool"), seed(subject="interfaces"), seed(type="benchmark"), seed(language=3)):
            with self.subTest(seed=bad):
                save_json(self.root / "config/seeds.json", [bad])
                with self.assertRaisesRegex(ValueError, "Invalid seed record"):
                    validate(self.root)

    def test_validate_rejects_malformed_or_conflicting_exclusions(self):
        for excluded in ({"12": {"repo": "test/model", "reason": "off-topic"}}, {"x": {"repo": "a/b", "reason": "r"}}, {"5": {"repo": "a/b"}}):
            with self.subTest(excluded=excluded):
                save_json(self.root / "config/excluded.json", excluded)
                with self.assertRaises(ValueError):
                    validate(self.root)
        save_json(self.root / "config/excluded.json", {"5": {"repo": "other/repo", "reason": "off-topic"}})
        self.assertEqual(validate(self.root)["excluded"], 1)

    def test_review_queue_omits_listed_excluded_and_forked_repositories(self):
        upsert(self.registry, metadata(20, "noise/excluded"), FIRST, self.seeds)
        upsert(self.registry, metadata(21, "noise/fork", fork=True), FIRST, self.seeds)
        upsert(self.registry, metadata(22, "new/candidate"), FIRST, self.seeds)
        self.save_registry()
        save_json(self.root / "config/excluded.json", {"20": {"repo": "noise/excluded", "reason": "off-topic"}})
        render(self.root)
        queue = (self.root / "docs/discovered.md").read_text()
        self.assertIn("4 tracked · 1 listed · 1 excluded · 1 forks · **1 awaiting review**", queue)
        self.assertIn("[new/candidate]", queue)
        for name in ("test/model", "noise/excluded", "noise/fork"):
            self.assertNotIn(f"[{name}]", queue)

    def test_applications_and_data_driven_models_get_their_own_trees(self):
        self.seeds += [seed("study/rice-runs", 30, type="application", subject="rice"),
                       seed("ml/yield", 31, type="data-driven", subject="maize", language="R")]
        upsert(self.registry, metadata(30, "study/rice-runs"), FIRST, self.seeds)
        upsert(self.registry, metadata(31, "ml/yield"), FIRST, self.seeds)
        self.save_registry()
        save_json(self.root / "config/seeds.json", self.seeds)
        render(self.root)
        readme = (self.root / "README.md").read_text()
        applications = (self.root / "docs/applications.md").read_text()
        data_driven = (self.root / "docs/data-driven.md").read_text()
        self.assertIn("- [Applications and case studies](docs/applications.md) (1)\n  - [Rice](docs/applications.md#rice) (1)", readme)
        self.assertNotIn("[study/rice-runs]", readme)
        self.assertIn('<a id="rice-python"></a>', applications)
        self.assertIn("[study/rice-runs](https://github.com/study/rice-runs)", applications)
        self.assertIn('<a id="maize-r"></a>', data_driven)
        self.assertNotIn("[ml/yield]", applications)

    def test_readme_lists_crop_models_and_links_process_models_and_tools_to_their_pages(self):
        self.seeds += [seed("soil/water", 32, subject="soil-water"), seed("run/wrapper", 33, type="tool", subject="interfaces")]
        upsert(self.registry, metadata(32, "soil/water"), FIRST, self.seeds)
        upsert(self.registry, metadata(33, "run/wrapper"), FIRST, self.seeds)
        self.save_registry()
        save_json(self.root / "config/seeds.json", self.seeds)
        render(self.root)
        readme = (self.root / "README.md").read_text()
        processes = (self.root / "docs/process-models.md").read_text()
        tools = (self.root / "docs/tools.md").read_text()
        self.assertIn("[test/model](https://github.com/test/model)", readme)
        self.assertIn("- [Process models](docs/process-models.md) (1)\n  - [Soil water and heat](docs/process-models.md#soil-water) (1)", readme)
        self.assertIn("- [Frameworks and tools](docs/tools.md) (1)\n  - [Model interfaces and wrappers](docs/tools.md#interfaces) (1)", readme)
        for name in ("soil/water", "run/wrapper"):
            self.assertNotIn(f"[{name}]", readme)
        self.assertIn("- [Soil water and heat](#soil-water) (1)\n  - [Python](#soil-water-python) (1)", processes)
        self.assertIn("[soil/water](https://github.com/soil/water)", processes)
        self.assertIn('<a id="interfaces-python"></a>', tools)
        self.assertIn("[run/wrapper](https://github.com/run/wrapper)", tools)

    def test_long_page_continues_on_numbered_pages_and_contents_follow_each_section(self):
        names = [f"ml/maize-{number}" for number in range(6)] + ["ml/soil"]
        for number, name in enumerate(names):
            subject = "soil-water" if name == "ml/soil" else "maize"
            self.seeds.append(seed(name, 40 + number, type="data-driven", subject=subject))
            upsert(self.registry, metadata(40 + number, name), FIRST, self.seeds)
        self.save_registry()
        save_json(self.root / "config/seeds.json", self.seeds)
        with patch("cropmodels.catalog.PAGE_BYTES", 500):
            render(self.root)
        pages = {path.name: path.read_text() for path in (self.root / "docs").glob("data-driven*.md")}
        self.assertGreater(len(pages), 1)
        self.assertIn("# Data-driven models (page 2 of", pages["data-driven-2.md"])
        self.assertIn("Continued on [page 2](data-driven-2.md).", pages["data-driven.md"])
        self.assertIn("## Crops (continued)\n\n### Maize (continued)\n\n#### Python (continued)", "".join(pages.values()))
        for name in names:
            self.assertEqual(sum(page.count(f"[{name}](") for page in pages.values()), 1)
        links = re.findall(r"\]\(((?:data-driven-\d+\.md)?)#((?:maize|soil-water)[a-z-]*)\)", pages["data-driven.md"])
        self.assertEqual(len(links), 4)
        for page, target in links:
            self.assertIn(f'<a id="{target}"></a>', pages[page or "data-driven.md"])
        readme = (self.root / "README.md").read_text()
        self.assertRegex(readme, r"  - \[Soil water and heat\]\(docs/data-driven(-\d+)?\.md#soil-water\) \(1\)")
        render(self.root)
        self.assertEqual(sorted(path.name for path in (self.root / "docs").glob("data-driven*.md")), ["data-driven.md"])

    def test_validate_accepts_minimal_public_fixture(self):
        self.assertEqual(validate(self.root)["repositories"], 1)

    def test_validate_rejects_invalid_stored_ids_even_if_key_matches(self):
        for value in (True, 0, -12, 12.5, "12"):
            with self.subTest(identifier=value):
                row = copy.deepcopy(self.registry["12"])
                row["id"] = value
                save_json(self.root / "catalog/repositories.json", {str(value): row})
                with self.assertRaises(ValueError):
                    validate(self.root)

    def test_validate_rejects_private_catalogue_rows(self):
        self.registry["12"]["visibility"] = "private"
        self.save_registry()
        with self.assertRaises(ValueError):
            validate(self.root)


class AtomicSaveTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.path = Path(self.directory.name) / "state.json"
        save_json(self.path, {"completed": "previous"})

    def test_old_file_stays_readable_until_complete_new_json_replaces_it(self):
        replace = Path.replace

        def inspect_then_replace(temporary, destination):
            self.assertEqual(read_json(destination), {"completed": "previous"})
            self.assertEqual(read_json(temporary), {"completed": "new"})
            return replace(temporary, destination)

        with patch("cropmodels.catalog.Path.replace", autospec=True, side_effect=inspect_then_replace):
            save_json(self.path, {"completed": "new"})
        self.assertEqual(read_json(self.path), {"completed": "new"})
        self.assertEqual(list(self.path.parent.iterdir()), [self.path])

    def test_replace_failure_preserves_old_json_and_removes_temporary_file(self):
        with patch("cropmodels.catalog.Path.replace", side_effect=OSError("simulated full filesystem")):
            with self.assertRaises(OSError):
                save_json(self.path, {"completed": "new"})
        self.assertEqual(json.loads(self.path.read_text()), {"completed": "previous"})
        self.assertEqual(list(self.path.parent.iterdir()), [self.path])

    def test_serialization_failure_preserves_old_json_and_removes_partial_temporary_file(self):
        with self.assertRaises(TypeError):
            save_json(self.path, {"partial": object()})
        self.assertEqual(read_json(self.path), {"completed": "previous"})
        self.assertEqual(list(self.path.parent.iterdir()), [self.path])


if __name__ == "__main__":
    unittest.main()
