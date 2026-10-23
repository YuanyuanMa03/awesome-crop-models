# Contributing

Help people discover agricultural biophysical models and keep their public repository records useful over time. Small corrections, missing model implementations, better search terms, and reproducible collector fixes are welcome.

## Scope

The list covers GitHub repositories about crop models and the agricultural processes behind them. Every entry has one of four types:

- **model**: process-based models. These include whole-crop and cropping-system models, crop-specific models, and models of plant processes (phenology, photosynthesis, architecture, roots), soil processes (water, heat, carbon, nutrients), water (evapotranspiration, irrigation, hydrology), weather, pests and diseases, and agricultural greenhouse gases. Reimplementations, ports, teaching versions and archived code count.
- **tool**: frameworks, interfaces and wrappers, calibration, data assimilation, gridded runners, input and parameter data, and tutorials that serve such models.
- **application**: repositories that apply a model to a particular study, region or analysis.
- **data-driven**: statistical or machine-learning models that predict crop variables (yield, biomass, phenology, water use) or agricultural process dynamics (soil moisture, evapotranspiration, nutrients).

Out of scope: image classification (disease, weed or fruit detection), crop or fertiliser recommendation, price prediction, IoT and sensor dashboards, farm-management or marketplace apps, and generic data processing with no crop or process model. Plain forks and read-only mirrors are not listed. A fork with substantial independent development can be listed. So can a mirror of a package whose source is not on GitHub, such as a CRAN mirror.

**Listing a repository records relevance, not scientific validity, numerical correctness or licence permission.** Keep unknown or conflicting licence information visible. Public visibility does not by itself establish an open-source licence.

## Add or correct an entry

Check the [README](README.md), the [review queue](docs/discovered.md), [config/seeds.json](config/seeds.json) and open issues first. Then add or edit a record in `config/seeds.json`:

```json
{
  "repo": "owner/repository",
  "github_id": 123456789,
  "type": "model",
  "subject": "maize",
  "language": "Fortran",
  "description": "One factual sentence in your own words."
}
```

- `type`: `model`, `tool`, `application` or `data-driven`.
- `subject` is the first level of the tree. Choose one:
  - Crops, for models, applications and data-driven models: `general-crop`, `rice`, `wheat`, `maize`, `other-cereals`, `soybean`, `legumes-oilseeds`, `potato`, `roots-tubers`, `cotton`, `sugar-crops`, `vegetables`, `fruit-vine`, `plantation`, `grassland`, `bioenergy-other`.
  - Processes, for the same types: `phenology`, `photosynthesis`, `architecture`, `roots`, `soil-water`, `soil-nutrients`, `greenhouse-gases`, `evapotranspiration`, `weather`, `pests-diseases`, `hydrology`, `land-surface`, `controlled-environment`.
  - Tools, for type `tool` only: `frameworks`, `interfaces`, `calibration`, `data-assimilation`, `gridded`, `model-data`, `learning`.

  A multi-crop model is `general-crop`. A process model built for one crop goes under that crop, and a generic process model goes under its process.
- `language` (optional) is the second level. By default the list uses GitHub's primary language, normalised (`FORTRAN` → Fortran, `F*` → FST, the Fortran Simulation Translator; `Jupyter Notebook` → Python). Set it when that is misleading, for example a C++ model whose repository is mostly Python bindings.
- `description` (optional) replaces the GitHub description. Write one when GitHub has none or it is not in English. Do not copy text from another list.
- `github_id` is the stable repository ID (`gh api repos/OWNER/NAME --jq .id`). It keeps the entry through renames and transfers.

To reject a repository in the review queue, record it in `config/excluded.json` with a short reason:

```json
"123456789": {"repo": "owner/repository", "reason": "image processing or computer vision"}
```

## Improve discovery

[config/queries.json](config/queries.json) holds stable query IDs and GitHub repository-search queries. Add targeted model names, process phrases, alternate spellings, languages, and relevant topics. Explain why a query should recover missed biophysical models. Avoid generic terms that mainly retrieve unrelated image-cropping software, product platforms, or disease-image classifiers.

Do not put `created:` time limits, `is:public`, or `fork:` restrictions in configured queries. The collector adds public visibility and creation-time partitions consistently, and leaves forks out of search results. Changing a query ID or wording can change the meaning of saved discovery state; follow the collector's reset/recovery guidance when rerunning an altered plan.

[config/owners.json](config/owners.json) lists public model-maintainer accounts to enumerate. Each record uses `login` and `kind` (`org` or `user`). Verify account type against first-party GitHub metadata. An owner route is a discovery source: it does not assert that all of that account's repositories are relevant, scientifically reviewed, or permissively licensed.

## Work locally and submit a change

1. Fork the project and clone your fork. Create a branch for the specific correction.
2. Keep the change small and include its public evidence and intended scope.
3. Follow the project README and CLI help for the supported collection commands. Keep interrupted-run state when resuming; do not replace incomplete work with a “complete” coverage claim. Preserve the last successful catalogue when an API request fails.
4. For configuration changes, run `python scripts/catalog.py validate` (JSON syntax, unique repository/query/owner identities, valid types and subjects) and `python scripts/catalog.py render`. For code changes, run the relevant tests and report the actual result, including skipped or failed checks.
5. Open a pull request explaining the change, evidence, checks performed, and remaining uncertainty.

A local collector run can be restarted using its saved state according to the supported CLI recovery procedure. Forks do not automatically run scheduled workflows: enable and configure the workflow in your fork if you want scheduled collection. Keep credentials in the supported local environment or GitHub secrets. Never commit tokens. GitHub may disable public-repository schedules after 60 days without activity; see the [official workflow documentation](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/disable-and-enable-workflows). A maintained recovery path and transferable configuration support continuity; automation alone is not a guarantee of permanent operation.

## Coverage and publication boundaries

Report the query plan, observation date, pages or partitions checked, API failures, and incomplete results. “Found by these searches” is evidence; “all GitHub repositories covered” requires a completeness argument this project does not currently have. Do not treat forks as independent model families, repository activity as scientific validation, or search absence as proof that a model does not exist.

This project collects public repository references and its own metadata. Do not submit third-party model source code, copied data, hidden answers, private research notes, unpublished manuscripts, credentials, or machine/session files. Proposed metadata should use public sources and respect their provenance. Inclusion in this catalogue does not authorize redistribution of a model's code or data, and does not make the repository a benchmark or scientific gold standard.
