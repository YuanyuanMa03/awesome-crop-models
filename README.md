<div align="center">

# Awesome Crop Models [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

**A curated map of open-source crop and agricultural process models on GitHub**<br>crop or process → programming language → repository

[![repositories](https://img.shields.io/badge/repositories-15%2C291-2ea44f?style=flat-square)](#contents) [![last collection](https://img.shields.io/badge/last_collection-2026--10--26-informational?style=flat-square)](docs/status.md) [![licence](https://img.shields.io/badge/licence-MIT-blue?style=flat-square)](LICENSE) [![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](CONTRIBUTING.md)

[English](README.md) · [简体中文](docs/README.zh-CN.md) · [Review queue](docs/discovered.md) · [Collection status](docs/status.md)

</div>

Crop growth simulators; soil, water, nutrient and climate process models; the frameworks and tools that run them; studies that apply them; and data-driven yield and process models. Each repository appears once, under its main crop or process and its main programming language, ordered by stars. Crop models are listed below, and the other branches have their own pages. Listing is not a scientific endorsement: check each project's licence before reuse.

> **15,291 repositories** · 437 crop models · 1,675 process models · 1,584 frameworks and tools · 769 applications · 10,826 data-driven models. Screened from 106,986 GitHub repositories found by 525 searches and 33 maintainer accounts.

## Contents

- [Most starred](#most-starred)
- [Crop models](#crop-models) (437)
  - [General and multi-crop](#general-crop) (183): [C](#general-crop-c) · [C#](#general-crop-csharp) · [C++](#general-crop-cplusplus) · [Fortran](#general-crop-fortran) · [FST](#general-crop-fst) · [Go](#general-crop-go) · [IDL](#general-crop-idl) · [Java](#general-crop-java) · [JavaScript](#general-crop-javascript) · [Julia](#general-crop-julia) · [MATLAB](#general-crop-matlab) · [NetLogo](#general-crop-netlogo) · [Python](#general-crop-python) · [R](#general-crop-r) · [Scheme](#general-crop-scheme) · [Visual Basic](#general-crop-visual-basic) · [Vue](#general-crop-vue) · [Wolfram Language](#general-crop-wolfram-language) · [Other](#general-crop-other)
  - [Rice](#rice) (25): [C++](#rice-cplusplus) · [Fortran](#rice-fortran) · [Java](#rice-java) · [MATLAB](#rice-matlab) · [NetLogo](#rice-netlogo) · [Python](#rice-python) · [R](#rice-r) · [Other](#rice-other)
  - [Wheat](#wheat) (28): [C#](#wheat-csharp) · [Fortran](#wheat-fortran) · [JavaScript](#wheat-javascript) · [Python](#wheat-python) · [R](#wheat-r) · [Raku](#wheat-raku)
  - [Maize](#maize) (20): [C#](#maize-csharp) · [C++](#maize-cplusplus) · [Fortran](#maize-fortran) · [Java](#maize-java) · [Python](#maize-python) · [R](#maize-r) · [TypeScript](#maize-typescript) · [Other](#maize-other)
  - [Barley, sorghum, millet and other cereals](#other-cereals) (4): [Fortran](#other-cereals-fortran) · [Python](#other-cereals-python) · [R](#other-cereals-r) · [Other](#other-cereals-other)
  - [Soybean](#soybean) (5): [C++](#soybean-cplusplus) · [Fortran](#soybean-fortran) · [Python](#soybean-python) · [R](#soybean-r)
  - [Other legumes and oilseeds](#legumes-oilseeds) (9): [C++](#legumes-oilseeds-cplusplus) · [Fortran](#legumes-oilseeds-fortran) · [Python](#legumes-oilseeds-python) · [R](#legumes-oilseeds-r) · [Other](#legumes-oilseeds-other)
  - [Potato](#potato) (6): [Fortran](#potato-fortran) · [Pascal](#potato-pascal) · [Python](#potato-python)
  - [Cassava and other roots and tubers](#roots-tubers) (8): [Fortran](#roots-tubers-fortran) · [FST](#roots-tubers-fst) · [Pascal](#roots-tubers-pascal) · [Python](#roots-tubers-python) · [R](#roots-tubers-r)
  - [Cotton](#cotton) (9): [Fortran](#cotton-fortran) · [Java](#cotton-java) · [Python](#cotton-python) · [R](#cotton-r) · [Rust](#cotton-rust) · [Other](#cotton-other)
  - [Sugarcane and sugar beet](#sugar-crops) (2): [Fortran](#sugar-crops-fortran)
  - [Vegetables](#vegetables) (37): [C++](#vegetables-cplusplus) · [Fortran](#vegetables-fortran) · [GAML](#vegetables-gaml) · [JavaScript](#vegetables-javascript) · [Julia](#vegetables-julia) · [MATLAB](#vegetables-matlab) · [Python](#vegetables-python) · [R](#vegetables-r) · [Rust](#vegetables-rust) · [TypeScript](#vegetables-typescript) · [Other](#vegetables-other)
  - [Fruit trees and grapevine](#fruit-vine) (33): [C#](#fruit-vine-csharp) · [Fortran](#fruit-vine-fortran) · [Java](#fruit-vine-java) · [JavaScript](#fruit-vine-javascript) · [Julia](#fruit-vine-julia) · [Python](#fruit-vine-python) · [R](#fruit-vine-r) · [Ruby](#fruit-vine-ruby) · [Shell](#fruit-vine-shell) · [Other](#fruit-vine-other)
  - [Oil palm, coffee, cocoa and other plantation crops](#plantation) (23): [C++](#plantation-cplusplus) · [Fortran](#plantation-fortran) · [FST](#plantation-fst) · [Julia](#plantation-julia) · [NetLogo](#plantation-netlogo) · [Python](#plantation-python) · [R](#plantation-r) · [Visual Basic](#plantation-visual-basic) · [Other](#plantation-other)
  - [Grassland, pasture and forage](#grassland) (36): [C](#grassland-c) · [C++](#grassland-cplusplus) · [Fortran](#grassland-fortran) · [JavaScript](#grassland-javascript) · [Julia](#grassland-julia) · [NCL](#grassland-ncl) · [Python](#grassland-python) · [R](#grassland-r) · [Other](#grassland-other)
  - [Bioenergy and other crops](#bioenergy-other) (9): [C++](#bioenergy-other-cplusplus) · [Fortran](#bioenergy-other-fortran) · [Python](#bioenergy-other-python) · [R](#bioenergy-other-r)
- [Process models](docs/process-models.md) (1,675): [Phenology and development](docs/process-models.md#phenology) · [Photosynthesis, canopy and transpiration](docs/process-models.md#photosynthesis) · [Plant architecture and FSPM](docs/process-models.md#architecture) · [Roots and rhizosphere](docs/process-models.md#roots) · [Soil water and heat](docs/process-models.md#soil-water) · [Soil carbon, nitrogen and nutrients](docs/process-models.md#soil-nutrients) · [Agricultural greenhouse gases](docs/process-models.md#greenhouse-gases) · [Evapotranspiration and irrigation](docs/process-models.md#evapotranspiration) · [Weather and agroclimate](docs/process-models.md#weather) · [Pests, diseases and weeds](docs/process-models.md#pests-diseases) · [Hydrology, erosion and watersheds](docs/process-models.md#hydrology) · [Land surface and global vegetation](docs/process-models.md#land-surface) · [Greenhouses and controlled environments](docs/process-models.md#controlled-environment)
- [Frameworks and tools](docs/tools.md) (1,584): [Modelling frameworks and platforms](docs/tools.md#frameworks) · [Model interfaces and wrappers](docs/tools.md#interfaces) · [Calibration, sensitivity and uncertainty](docs/tools.md#calibration) · [Data assimilation and remote sensing](docs/tools.md#data-assimilation) · [Regional and gridded simulation](docs/tools.md#gridded) · [Inputs, parameters and data](docs/tools.md#model-data) · [Tutorials and teaching](docs/tools.md#learning)
- [Applications and case studies](docs/applications.md) (769), arranged by crop or process
- [Data-driven models](docs/data-driven.md) (10,826), arranged by crop or process
- [Contributing](#contributing)
- [How this list is built](#how-this-list-is-built)

## Most starred

The most-starred process-based models and tools on the list. Each also appears in its branch of the tree.

| # | Repository | Description | Language | ★ |
|---:|---|---|---|---:|
| 1 | [altmenorg/HAsmartirrigation](https://github.com/altmenorg/HAsmartirrigation) | Smart Irrigation custom component for Home Assistant. | Python | 564 |
| 2 | [ESCOMP/CTSM](https://github.com/ESCOMP/CTSM) | Community Terrestrial Systems Model (includes the Community Land Model of CESM). | Fortran | 352 |
| 3 | [ajwdewit/pcse](https://github.com/ajwdewit/pcse) | Python environment for running crop growth and production models. | Python | 292 |
| 4 | [PecanProject/pecan](https://github.com/PecanProject/pecan) | The Predictive Ecosystem Analyzer (PEcAn) is an integrated ecological bioinformatics toolbox. | R | 248 |
| 5 | [DSSAT/dssat-csm-os](https://github.com/DSSAT/dssat-csm-os) | Cropping-system simulations across crop species, soils, weather, and management. | Fortran | 239 |
| 6 | [APSIMInitiative/ApsimX](https://github.com/APSIMInitiative/ApsimX) | Next-generation APSIM framework for agricultural system simulations. | C# | 218 |
| 7 | [woodcrafty/PyETo](https://github.com/woodcrafty/PyETo) | Reference and potential evapotranspiration calculation routines. | Python | 179 |
| 8 | [aquacropos/aquacrop](https://github.com/aquacropos/aquacrop) | Python implementation of AquaCrop-OS for crop growth and water use. | Python | 173 |
| 9 | [hectornieto/pyTSEB](https://github.com/hectornieto/pyTSEB) | Two-source energy balance calculations for vegetation evapotranspiration. | Python | 172 |
| 10 | [ajwdewit/pcse_notebooks](https://github.com/ajwdewit/pcse_notebooks) | A collection of Jupyter notebooks that demonstrate usage of PCSE. | Python | 168 |
| 11 | [pyet-org/pyet](https://github.com/pyet-org/pyet) | Reference and potential evaporation estimation methods in Python. | Python | 166 |
| 12 | [phydrus/phydrus](https://github.com/phydrus/phydrus) | :sweat_drops: Python implementation of the HYDRUS-1D unsaturated zone model. | Python | 112 |
| 13 | [ropensci/nasapower](https://github.com/ropensci/nasapower) | API Client for NASA POWER Global Meteorology, Surface Solar Energy and Climatology in R. | R | 108 |
| 14 | [sbegueria/SPEI](https://github.com/sbegueria/SPEI) | An R package for computing the Standardized Precipitation-Evapotranspiration Index (SPEI), Penman-Monteith and other… | R | 108 |
| 15 | [lzwei196/RS-DPCF](https://github.com/lzwei196/RS-DPCF) | Parallel, distributed framework for RZ-SHAW model calibration and multi-site simulations of seasonal frost in croplands. | Python | 107 |
| 16 | [Christiaanvandertol/SCOPE](https://github.com/Christiaanvandertol/SCOPE) | SCOPE is a simulation model for radiative transfer, photosynthesis and energy fluxes in vegetation and soil. | MATLAB | 105 |
| 17 | [gicait/PyAEZ](https://github.com/gicait/PyAEZ) | Python implementation of FAO's agro-ecological zoning (GAEZ) for climate, soil and crop suitability and potential yield. | Python | 105 |
| 18 | [openalea/lpy](https://github.com/openalea/lpy) | An open source python version of the Lindenmayer Systems. | C++ | 99 |
| 19 | [PIK-LPJmL/LPJmL](https://github.com/PIK-LPJmL/LPJmL) | Managed-land and vegetation simulations linking carbon and water cycles. | C | 98 |
| 20 | [kthorp/pyfao56](https://github.com/kthorp/pyfao56) | FAO-56 crop water use and irrigation calculations using dual coefficients. | Python | 97 |

## Crop models

*Whole-crop and cropping-system models, and process models built for one crop.*

<a id="general-crop"></a>

### General and multi-crop

<a id="general-crop-c"></a>

#### C

- [BramDr/wofost_c_bmi](https://github.com/BramDr/wofost_c_bmi) - WOFOST crop model (derived from https://github.com/isupit/wofost_c) with Basic Model Interface (BMI) implementation. `no licence`
- [isupit/wofost_c](https://github.com/isupit/wofost_c) - WOFOST crop model in C. `no licence`
- [RuolingTang996/WOFOST_daily](https://github.com/RuolingTang996/WOFOST_daily) - WOFOST crop model set up for daily simulations. `no licence`
- [yixuan953/WOFOST-noNutrientLimit](https://github.com/yixuan953/WOFOST-noNutrientLimit) - WOFOST crop model variant without nutrient limitation. `no licence`

<a id="general-crop-csharp"></a>

#### C#

- [APSIMInitiative/ApsimX](https://github.com/APSIMInitiative/ApsimX) - Next-generation APSIM framework for agricultural system simulations. `★ 218` `custom licence`
- [APSIMInitiative/APSIM710](https://github.com/APSIMInitiative/APSIM710) - Earlier APSIM implementation with crop, soil, and management modules. `★ 45` `no licence`

<a id="general-crop-cplusplus"></a>

#### C++

- [biocro/biocro](https://github.com/biocro/biocro) - Modular crop growth simulations assembled from physiological process models. `★ 52` `custom licence`
- [zalf-rpm/monica](https://github.com/zalf-rpm/monica) - Crop and soil processes linking carbon, nitrogen, and water dynamics. `★ 33` `MPL-2.0`
- [cropmodels/Rwofost](https://github.com/cropmodels/Rwofost) - C++ implementation of the WOFOST crop growth model with an R interface. `★ 21` `GPL-3.0`
- [perabrahamsen/daisy-model](https://github.com/perabrahamsen/daisy-model) - Daisy implementation for coupled crop and soil system processes. `★ 18` `GPL-2.0` `archived`
- [cropmodels/Recocrop](https://github.com/cropmodels/Recocrop) - ecocrop model of plant environmental suitability. `★ 10` `GPL-3.0`
- [cropmodels/Rlintul](https://github.com/cropmodels/Rlintul) - R package implementing the LINTUL crop growth model. `★ 4` `GPL-3.0`
- [mingliangwsu/CropSyst_MicroBasin](https://github.com/mingliangwsu/CropSyst_MicroBasin) - CropSyst cropping-systems model in a micro-basin setting. `★ 3` `no licence`
- [PhenomenModel/rSamara](https://github.com/PhenomenModel/rSamara) - Samara Crop Model. `★ 1` `no licence`
- [annsterling97-coder/AgriAlgorithm](https://github.com/annsterling97-coder/AgriAlgorithm) - Agricultural computing plugin based on the WOFOST core algorithm (C++/Qt), integrating DVS, LAI, and crop water requirement prediction, including complete UI and database management modules. `no licence`
- [leeeeeeeee2/AquaCrop_cpp](https://github.com/leeeeeeeee2/AquaCrop_cpp) - C++ port of the FAO AquaCrop crop-water productivity model. This repository provides a lightweight C++ scaffolding for the AquaCrop model. `custom licence`
- [NatalieRosenberg/BioCroWP_1](https://github.com/NatalieRosenberg/BioCroWP_1) - BioCro module library (BioCroWP). `custom licence`
- [quesnel/safihr.cropmodel](https://github.com/quesnel/safihr.cropmodel) - A generic crop model. `custom licence`
- [r-forge/cropsim](https://github.com/r-forge/cropsim) - Read-only mirror of "cropsim" from r-forge SVN. `no licence`
- [tbmcoding/Generic_Crop_Growth](https://github.com/tbmcoding/Generic_Crop_Growth) - Generic crop growth model in C++ based on the book Introduction to mathematical modeling of crop growth by Christopher Teh. `no licence`

<a id="general-crop-fortran"></a>

#### Fortran

- [DSSAT/dssat-csm-os](https://github.com/DSSAT/dssat-csm-os) - Cropping-system simulations across crop species, soils, weather, and management. `★ 239` `BSD-3-Clause`
- [KUL-RSDA/AquaCrop](https://github.com/KUL-RSDA/AquaCrop) - FAO-endorsed AquaCrop source for crop response to water availability. `★ 84` `custom licence`
- [ajwdewit/WOFOST](https://github.com/ajwdewit/WOFOST) - Fortran implementation of WOFOST crop production simulations. `★ 75` `custom licence`
- [chporter/SimpleCrop](https://github.com/chporter/SimpleCrop) - Ricardo Braga's Simple Crop model. Used as a simple example of a modular crop model in the style of DSSAT-CSM. `★ 12` `no licence`
- [ltsb-etsmtl/crop-model](https://github.com/ltsb-etsmtl/crop-model) - This project includes crop models used in various studied that were published by members of LTSB. The crops model. `★ 5` `no licence`
- [CEMPD/FESTC-EPIC0509](https://github.com/CEMPD/FESTC-EPIC0509) - Fertilizer Emission Scenario Tool for CMAQ (FEST-C): Generate fertilizer application input for CMAQ bi-directional NH3 modeling. `★ 4` `no licence`
- [jinyun1tang/EcoSIM](https://github.com/jinyun1tang/EcoSIM) - Biogeochemical agro-ecosystem modelling library spun off from the ecosys model. `★ 4` `custom licence`
- [GCEL/DALEC-CropN](https://github.com/GCEL/DALEC-CropN) - DALEC-Crop model developments for simulating the impacts of N dilution on the ACM equation used to determine a leaf N and temperature limited rate of photosynthesis. `★ 1` `no licence`
- [hutx2309/EPIC-RP](https://github.com/hutx2309/EPIC-RP) - A restructure and modularized EPIC model integrating radiative transfer and photosynthesis models for crop growth. `★ 1` `no licence`
- [Longitude103/rzwqm_science](https://github.com/Longitude103/rzwqm_science) - Science code of the RZWQM2 Root Zone Water Quality Model, version 4.5. `★ 1` `no licence`
- [luxkwang/SimpleCropModel](https://github.com/luxkwang/SimpleCropModel) - Source code of the SIMPLE crop model (Zhao et al., 2019). `★ 1` `GPL-3.0`
- [LiviaBrazp/DSSAT-CSM-ET](https://github.com/LiviaBrazp/DSSAT-CSM-ET) - Initial version of DSSAT-CSM with a customized implementation of new ET models (Penman–Monteith) featuring dynamic resistances. `BSD-3-Clause`
- [model-library-pps/LINTUL-4_archive](https://github.com/model-library-pps/LINTUL-4_archive) - LINTUL-4: generic crop growth model for potential, water-limited and nitrogen-limited production. `custom licence`
- [model-library-pps/LINTUL-5_archive](https://github.com/model-library-pps/LINTUL-5_archive) - LINTUL-5: crop growth model for many crops under potential, water-limited and nutrient-limited conditions. `custom licence`
- [model-library-pps/LINTUL-6_archive](https://github.com/model-library-pps/LINTUL-6_archive) - Archived LINTUL-6 crop growth model. `custom licence`
- [model-library-pps/LINTUL4-VSHT_archive](https://github.com/model-library-pps/LINTUL4-VSHT_archive) - LINTUL4-VSHT: LINTUL4 variant for potential, water-limited and nitrogen-limited growth of many crops. `custom licence`

<a id="general-crop-fst"></a>

#### FST

- [model-library-pps/LINTUL-1_archive](https://github.com/model-library-pps/LINTUL-1_archive) - LINTUL-1 (FST): simple crop growth model for potential production. `custom licence`
- [model-library-pps/LINTUL-2_archive](https://github.com/model-library-pps/LINTUL-2_archive) - LINTUL-2 (FST): crop growth under potential and water-limited conditions. `custom licence`
- [model-library-pps/LINTUL-3_archive](https://github.com/model-library-pps/LINTUL-3_archive) - LINTUL-3 (FST): crop growth under potential, water-limited and nitrogen-limited conditions. `custom licence`
- [model-library-pps/SUCROS_archive](https://github.com/model-library-pps/SUCROS_archive) - Archived SUCROS implementations for potential and water-limited crop growth. `custom licence`
- [model-library-pps/WaterStress--PureStand-Intercrops_archive](https://github.com/model-library-pps/WaterStress--PureStand-Intercrops_archive) - FST models of water stress in pure stands and intercrops of legumes and maize. `custom licence`

<a id="general-crop-go"></a>

#### Go

- [zalf-rpm/Hermes2Go](https://github.com/zalf-rpm/Hermes2Go) - HERMES - A simulation model for N-dynamics in arable fields. `★ 3` `MPL-2.0`

<a id="general-crop-idl"></a>

#### IDL

- [ajwdewit/IDL_WOFOST_7.1](https://github.com/ajwdewit/IDL_WOFOST_7.1) - IDL version of the WOFOST 7.1 crop simulation model. `GPL-3.0`

<a id="general-crop-java"></a>

#### Java

- [hisafe/hisafe](https://github.com/hisafe/hisafe) - Hi-sAFe is a 3-D mechanistic simulation model for agroforestry plots. `★ 11` `custom licence`
- [Topol/Crop-Model](https://github.com/Topol/Crop-Model) - Parametized Crop Model on the Physical Phenomenon. `★ 2` `no licence`
- [thesalmanx/Modular-Crop-Growth-Model-and-Simulation](https://github.com/thesalmanx/Modular-Crop-Growth-Model-and-Simulation) - This OOP project, written in Java programming language, aims to simulate the growth of plants using a complex engineering model. The project's goal is to understand the various factors that… `★ 1` `no licence`
- [Dev-Abs/crop-growth-simulation](https://github.com/Dev-Abs/crop-growth-simulation) - Crop growth simulation driven by weather and soil moisture, with a simple GUI. `no licence`
- [lubarbosa/simsafe](https://github.com/lubarbosa/simsafe) - SIMPLACE-Hi-sAFe Integrated AgroForesty Simulation Environment. `no licence`

<a id="general-crop-javascript"></a>

#### JavaScript

- [jvail/crop.js](https://github.com/jvail/crop.js) - A dynamic crop and grassland growth model. `★ 1` `MPL-2.0`
- [zalf-rpm/monica-js](https://github.com/zalf-rpm/monica-js) - JavaScript port of MONICA model. `★ 1` `GPL-3.0`
- [claudio9russo7/SIMPLE-Crop-simulation-on-web](https://github.com/claudio9russo7/SIMPLE-Crop-simulation-on-web) - Web version of the SIMPLE crop model. `no licence`
- [XCXUFO/WHCNS](https://github.com/XCXUFO/WHCNS) - Water and nitrogen management assistant based on the WHCNS soil–crop system model for North China (Chinese). `no licence`
- [YahyaAsmara/high-fidelity-agriculture-simulation](https://github.com/YahyaAsmara/high-fidelity-agriculture-simulation) - (WIP) An agricultural simulation system that models crop growth, environmental factors, soil conditions, weather patterns, pest management, and farming operations with scientific accuracy. The… `MIT`
- [zjti/ROTOR](https://github.com/zjti/ROTOR) - ROTOR crop rotation generator for agricultural land-use planning. `no licence`

<a id="general-crop-julia"></a>

#### Julia

- [gabo-di/AquaCrop.jl](https://github.com/gabo-di/AquaCrop.jl) - FAO's Aqua Crop in Julia as part of Persefone.jl. `★ 12` `custom licence`
- [rafaqz/DEBplant](https://github.com/rafaqz/DEBplant) - Scripts for a Dynamic Energy Budget plant model with microclimate interaction. `★ 10` `no licence`
- [yunan-l/NeuralCrop.jl](https://github.com/yunan-l/NeuralCrop.jl) - A global gridded crop model combining physics with machine learning. `★ 9` `custom licence`
- [yunan-l/Agrocosm.jl](https://github.com/yunan-l/Agrocosm.jl) - A fast and flexible crop model supporting automatic differentiation and GPU acceleration. `★ 5` `custom licence`
- [cropbox/SimpleCrop.jl](https://github.com/cropbox/SimpleCrop.jl) - 🌱 example of DSSAT-like crop model written in Cropbox. `★ 2` `MIT`
- [cropbox/LegacyCropModels.jl](https://github.com/cropbox/LegacyCropModels.jl) - 🍂 oldies but goodies. `MIT`
- [hutx2309/AIECO](https://github.com/hutx2309/AIECO) - This is AI-enhanced ECOsystem (AiECO), a hybrid AI-process ecosystem modeling platform. `Apache-2.0`
- [jeffersonfparil/CropGrowth.jl](https://github.com/jeffersonfparil/CropGrowth.jl) - Modelling crop growth using logistic curves. `GPL-3.0`
- [VEZY/Agrivoltaics.jl](https://github.com/VEZY/Agrivoltaics.jl) - Tools for modeling and simulating agrivoltaic systems. `MIT`

<a id="general-crop-matlab"></a>

#### MATLAB

- [aquacropos/aquacrop-matlab](https://github.com/aquacropos/aquacrop-matlab) - AquaCrop-OS: Matlab and Octave implementation of FAO AquaCrop model. `★ 7` `Apache-2.0`
- [EdgarStevenC/Crop-Growth-Modelling](https://github.com/EdgarStevenC/Crop-Growth-Modelling) - Crop growth modelling code in MATLAB. `★ 2` `Apache-2.0`
- [alaive/agriculture](https://github.com/alaive/agriculture) - Plant growth simulator using delay differential equations for leaf growth and colour. `★ 1` `no licence`
- [EcoExtreML/STEMMUS_SCOPE_PG](https://github.com/EcoExtreML/STEMMUS_SCOPE_PG) - Integrated model of STEMMUS-SCOPE and WOFOST model. `★ 1` `no licence`
- [fpant1/AgrivoltaicsDP5Model](https://github.com/fpant1/AgrivoltaicsDP5Model) - Simulation and design optimisation of agrivoltaics: solar generation and crop yields. `★ 1` `no licence`
- [atefero/Thornley-model-dynamics-and-the-modified-chapter2](https://github.com/atefero/Thornley-model-dynamics-and-the-modified-chapter2) - MATLAB code for Chapter 2: An in-depth study of the dynamics of Thornley's mathematical model in plant biology with a view to an improved model. `GPL-3.0`
- [JoeriRR/LINTUL3_MATLAB](https://github.com/JoeriRR/LINTUL3_MATLAB) - LINTUL3 crop model in MATLAB. `no licence`
- [kirstentt/flooding-stress](https://github.com/kirstentt/flooding-stress) - A mechanistic model for simulating plant responses to flooding stress. The model describes oxygen and carbon dynamics of plants subjected to flooding stress, and their dependence on plant rooting… `GPL-3.0`
- [MaartenVL/aquacrop_spatiallyexplicit](https://github.com/MaartenVL/aquacrop_spatiallyexplicit) - AquaCrop adaptations made for paper Van Loo & Verstraeten 2021. `no licence`
- [SobhyMahmoud/AquaCrop_Modifications](https://github.com/SobhyMahmoud/AquaCrop_Modifications) - Modified version of the AquaCrop crop water productivity model in MATLAB. `no licence`

<a id="general-crop-netlogo"></a>

#### NetLogo

- [sustentarea/logonia](https://github.com/sustentarea/logonia) - 🌿 Plant Growth Response Model in NetLogo. `★ 2` `GPL-3.0`
- [Andros-Spica/SIMPLE-crop-model](https://github.com/Andros-Spica/SIMPLE-crop-model) - NetLogo implementation of the SIMPLE crop model by Zhao et al. 2019 (https://doi.org/10.1016/j.eja.2019.01.009). `GPL-3.0`
- [kavinpreethi/WATERING_CROPGROWTH_RBB](https://github.com/kavinpreethi/WATERING_CROPGROWTH_RBB) - A NetLogo Reusable Building Block (RBB) model to simulate water flow and crop growth in an irrigation scheme. `MIT`

<a id="general-crop-python"></a>

#### Python

- [ajwdewit/pcse](https://github.com/ajwdewit/pcse) - Python environment for running crop growth and production models. `★ 292` `custom licence`
- [aquacropos/aquacrop](https://github.com/aquacropos/aquacrop) - Python implementation of AquaCrop-OS for crop growth and water use. `★ 173` `Apache-2.0`
- [gicait/PyAEZ](https://github.com/gicait/PyAEZ) - Python implementation of FAO's agro-ecological zoning (GAEZ) for climate, soil and crop suitability and potential yield. `★ 105` `MIT`
- [BerkeleyAutomation/AlphaGarden](https://github.com/BerkeleyAutomation/AlphaGarden) - A fast, first order open-access simulator that integrates single plant growth models with inter-plant competition for sun light and water. `★ 94` `no licence`
- [RuminantFarmSystems/RuFaS](https://github.com/RuminantFarmSystems/RuFaS) - Ruminant Farm Systems (RuFaS) is an open-source, next-generation, whole-farm modeling environment that simulates dairy farm production and environmental impact. `★ 45` `GPL-3.0`
- [WUR-AI/DeepCGM](https://github.com/WUR-AI/DeepCGM) - A deep learning based crop growth model. `★ 30` `custom licence`
- [WUR-AI/diffWOFOST](https://github.com/WUR-AI/diffWOFOST) - Differentiable implementation of WOFOST. `★ 25` `custom licence`
- [OmbreaPV/pySTICS](https://github.com/OmbreaPV/pySTICS) - Python Implementation of a simplified version of STICS crop model. `★ 16` `MIT`
- [PSUmodeling/Cycles](https://github.com/PSUmodeling/Cycles) - Releases, documentation and issue tracker of the Cycles multi-year agroecosystem model. `★ 13` `custom licence`
- [Carlitosh/AquaCrop_Py](https://github.com/Carlitosh/AquaCrop_Py) - Python implementation of AquaCropOS. `★ 10` `no licence`
- [un-fao/gaezv5](https://github.com/un-fao/gaezv5) - Global Agro-Ecological Zoning (GAEZ) version 5 GitHub repository. `★ 10` `no licence`
- [SARRA-cropmodels/SARRA-Py](https://github.com/SARRA-cropmodels/SARRA-Py) - Python crop model from the SARRA family (SARRA-H, SARRA-O). `★ 9` `GPL-3.0`
- [un-fao/fao-AquaCrop](https://github.com/un-fao/fao-AquaCrop) - FAO AquaCrop website available here:. `★ 7` `custom licence`
- [ataraxno/SIMPLE_crop_model](https://github.com/ataraxno/SIMPLE_crop_model) - Python implementation of the SIMPLE crop model (Zhao et al., 2019). `★ 6` `Apache-2.0`
- [benlaken/PyCrop](https://github.com/benlaken/PyCrop) - Python implementation of a simple modular 1D crop model. `★ 6` `CC0-1.0`
- [YuanyuanMa03/a-simple-crop-model](https://github.com/YuanyuanMa03/a-simple-crop-model) - Python implementation of the SIMPLE process-based crop model. `★ 5` `no licence`
- [Fantaso/farm-simulator](https://github.com/Fantaso/farm-simulator) - Object-oriented crop growth simulator (course project). `★ 4` `no licence`
- [NortonAlex/DAESIM](https://github.com/NortonAlex/DAESIM) - The python implementation of the Dynamic Agro-Ecosystem SIMulator (DAESIM) model. `★ 4` `AGPL-3.0`
- [andres-berger/pygecros](https://github.com/andres-berger/pygecros) - A pythonic version of GECROS. `★ 3` `GPL-3.0`
- [kcxsid/APSIM](https://github.com/kcxsid/APSIM) - Python framework for the Soil Predictive Model as part of the Agricultural Production System Simulator (APSIM) Crop Production Model. `★ 3` `no licence`
- [zackaryleady/Py_N_SSM_iCrop2](https://github.com/zackaryleady/Py_N_SSM_iCrop2) - Python Translation of the SSM iCrop2 model capable of simulating Nitrogen. `★ 3` `no licence`
- [zheng-jinhui/WOFOST-EW](https://github.com/zheng-jinhui/WOFOST-EW) - WOFOST enhanced for extreme weather (WOFOST-EW v1). `★ 3` `no licence`
- [RS-iCM/RSCM_Spatial](https://github.com/RS-iCM/RSCM_Spatial) - Remote Sensing-integrated Crop Model for geospatial simulations. `★ 2` `no licence`
- [rsk-ff/Dmitte](https://github.com/rsk-ff/Dmitte) - Tritium transfer through air, soil and crops, coupled with WOFOST via PCSE. `★ 2` `no licence`
- [thebigfotos/Plant-Growth-Modelling](https://github.com/thebigfotos/Plant-Growth-Modelling) - Model Plant Growth based on Weather data. `★ 2` `no licence`
- [ashutosh2203/cropsModel](https://github.com/ashutosh2203/cropsModel) - Simple Crop Model based on Irrigation and fertilization. `★ 1` `no licence`
- [boku-met/ARIS_lite](https://github.com/boku-met/ARIS_lite) - ARIS models plant growth based on environmental parameter. `★ 1` `MIT`
- [bzb0060/CropModels](https://github.com/bzb0060/CropModels) - python_project_cropModel. `★ 1` `no licence`
- [DanilaEremenko/Agrotool](https://github.com/DanilaEremenko/Agrotool) - Python port of AGROTOOL, a dynamic crop model from the Agrophysical Research Institute. `★ 1` `no licence`
- [Dojo456/aqua-crap](https://github.com/Dojo456/aqua-crap) - A simplified replication of the AquaCrop crop growth model by the UN FAO. `★ 1` `no licence`
- [jjmaynard/GAEZ-Hyperlocalization](https://github.com/jjmaynard/GAEZ-Hyperlocalization) - What the Package Does (One Line, Title Case). `★ 1` `custom licence`
- [Longitude103/pyCropSim](https://github.com/Longitude103/pyCropSim) - Python implementation of the Nebraska CropSim model, version 8. `★ 1` `GPL-3.0`
- [moendopi/cropsModel](https://github.com/moendopi/cropsModel) - A Python class to simulate crop yield. `★ 1` `GPL-3.0`
- [PascalKlH/NRSimulation](https://github.com/PascalKlH/NRSimulation) - Simulation of crop growth and weed management. `★ 1` `no licence`
- [RnoB/Plants-Kinematics](https://github.com/RnoB/Plants-Kinematics) - A simple Python software to model the growth of plants. `★ 1` `MIT`
- [agyaatcoder/jax-crop-model](https://github.com/agyaatcoder/jax-crop-model) - The SIMPLE crop model in JAX, wrapped as a hillclimbing environment for coding agents: five blocking gates, a frozen f64 oracle, and a null-calibrated paired A/B. `MIT`
- [AntoineHaddon/doubleModel](https://github.com/AntoineHaddon/doubleModel) - Double Modelling for Crop Irrigation and Fertilisation. `no licence`
- [ARVIOR-DSS/arvior-labs](https://github.com/ARVIOR-DSS/arvior-labs) - Interactive crop–soil–water modelling for research, education and scenario exploration. `no licence`
- [atefero/Thornley-original-modified-models-python](https://github.com/atefero/Thornley-original-modified-models-python) - Python simulations comparing the dynamics of the original Thornley carbon–nitrogen allocation model and the modified version. `MIT`
- [BenLatham/FLOSS-Agricultural-Simulation](https://github.com/BenLatham/FLOSS-Agricultural-Simulation) - A Farm Level Open Source Simulation. `MIT`
- [bigborras/Agrieli](https://github.com/bigborras/Agrieli) - Agrivoltaic simulation with the PASE framework: photovoltaic and crop outputs. `MIT`
- [CMits/PSoup-APSIM](https://github.com/CMits/PSoup-APSIM) - In this repository there is the code for the connection between PSoup and APSIM. `MIT`
- [Digital-Energy-and-Agriculture-Lab/PASE](https://github.com/Digital-Energy-and-Agriculture-Lab/PASE) - Agrivoltaic system simulator computing photovoltaic and crop outputs. `MIT`
- [dinarwali4/crop-stress-sim](https://github.com/dinarwali4/crop-stress-sim) - KP Crop Simulation Model. `no licence`
- [eurrag/SolRatio](https://github.com/eurrag/SolRatio) - Ground irradiance and crop yield model for single-axis tracker agrivoltaic systems &#124; Modello di irradianza al suolo e stima delle rese colturali per impianti agrivoltaici a tracker monoassiale. `Apache-2.0`
- [Faaaaaaki/agro-climat-benin](https://github.com/Faaaaaaki/agro-climat-benin) - Moteur de simulation agro-climatique du Benin (Python OOP + Tkinter). `no licence`
- [Herani-yir/climate-bee-crop-model](https://github.com/Herani-yir/climate-bee-crop-model) - Modeling climate change impact on wild bee-driven pollination and optimal planting strategies in agro-ecosystems. `no licence`
- [israeltankam/cropmix](https://github.com/israeltankam/cropmix) - To set later. `GPL-3.0`
- [IvanSerina/aquacrop-jax](https://github.com/IvanSerina/aquacrop-jax) - Porting of aquacrop on jax. `custom licence`
- [Jaysaly-cn/AgriWorld](https://github.com/Jaysaly-cn/AgriWorld) - Physics-guided differentiable agricultural model for county-level maize and soybean. `MIT`
- [JoCook1997/DO3SE-CropN](https://github.com/JoCook1997/DO3SE-CropN) - The N module add-on for the DO3SE-Crop model. `no licence`
- [kendallpknight/crop-growth](https://github.com/kendallpknight/crop-growth) - Small Python crop growth simulation script. `no licence`
- [LEANDERANTONY/Microclimate_Crop_Design_System](https://github.com/LEANDERANTONY/Microclimate_Crop_Design_System) - Predicts the microclimate of agroforestry environments, scores crop suitability and disease risk under it, and optimises the design (canopy, windbreak, variety, timing) to make a target crop viable. `MIT`
- [lv215244-oss/SAS_Simulator_Agronomico](https://github.com/lv215244-oss/SAS_Simulator_Agronomico) - Experimental cropping-system simulator (climate, soil and crop) for Sombrerete, Zacatecas, Mexico. `no licence`
- [maceiraluisa/saffron](https://github.com/maceiraluisa/saffron) - Saffron farm simulator. `no licence`
- [melycg2001/CGM-WGP](https://github.com/melycg2001/CGM-WGP) - Crop growth model coupled with whole-genome prediction of flowering time. `no licence`
- [model-library-pps/LINTUL](https://github.com/model-library-pps/LINTUL) - Python LINTUL implementation using light-use efficiency and resource limitations. `custom licence`
- [orianebro/PhD_Oriane](https://github.com/orianebro/PhD_Oriane) - Multiscale hybrid modeling framework for intercrops : the best of plant and crop models. `no licence`
- [PascalKlH/Grid-Based-Polycultural-Simulation](https://github.com/PascalKlH/Grid-Based-Polycultural-Simulation) - Grid-based simulation of polyculture crop growth. `no licence`
- [PLACE-at-Berkeley/Simple_Crop_Model](https://github.com/PLACE-at-Berkeley/Simple_Crop_Model) - Simple crop growth model in Python. `no licence`
- [rian-souza/AgriYieldSimulator](https://github.com/rian-souza/AgriYieldSimulator) - Simulation of crop yield based on weather data. Provides daily recommendations for optimal planting and harvesting using temperature and precipitation inputs, with support for both real and… `no licence`
- [rickpira/zona_agro](https://github.com/rickpira/zona_agro) - Programa de estimativa da produtividade agrícola pelo método da Zona Agroecológica da FAO. `no licence`
- [rrizkipd/LUMENS-Crop-Simulation](https://github.com/rrizkipd/LUMENS-Crop-Simulation) - Crop simulation component for LUMENS land-use planning. `no licence`
- [RS-iCM/RSCM](https://github.com/RS-iCM/RSCM) - Remote Sensing-integrated Crop Model. `MIT`
- [Seji-jam/Generic-Object-Oriented-Plant-Model](https://github.com/Seji-jam/Generic-Object-Oriented-Plant-Model) - This GitHub repository hosts a project for creating a generic object-oriented plant model, designed for modularity and adaptability. `no licence`
- [Seji-jam/Minimum_Plant_Model](https://github.com/Seji-jam/Minimum_Plant_Model) - Testing new structure for MPM. `no licence`
- [sjmf/tgrains-crop-model](https://github.com/sjmf/tgrains-crop-model) - Backend of the TGRAINS crop modelling tool. `no licence`
- [thy-1-1/AgroEcoSim](https://github.com/thy-1-1/AgroEcoSim) - Organic Agriculture Ecosystem Modeling & Decision Analysis. `MIT`
- [un-fao/pyaez](https://github.com/un-fao/pyaez) - Python package for Agro-Ecological Zoning (AEZ). `no licence`
- [ZhiyiLiao/crop_model_modules](https://github.com/ZhiyiLiao/crop_model_modules) - The model includes modules for phenology, photosynthesis, leaf area index (LAI), respiration, soil water balance, and soil nitrogen balance, and is applicable to rice and wheat. `no licence`

<a id="general-crop-r"></a>

#### R

- [andysouth/climcropr](https://github.com/andysouth/climcropr) - R package for simple crop modelling at global scale. `★ 3` `MIT`
- [degi/wanulcas](https://github.com/degi/wanulcas) - Water, Nutrient and Light Capture in Agroforestry Systems. `★ 2` `no licence`
- [GLAM-Leeds/GLAM-Parti-ML](https://github.com/GLAM-Leeds/GLAM-Parti-ML) - GLAM-Parti crop model combined with machine learning to predict biomass, yield and phenology. `★ 2` `AGPL-3.0`
- [lucabutikofer/WofostR](https://github.com/lucabutikofer/WofostR) - R implementation of Wofost. `★ 2` `no licence`
- [Onogi/IntegratingCGMwithGP](https://github.com/Onogi/IntegratingCGMwithGP) - Files for "Integration of crop growth models and genomic prediction" by Akio Onogi, a chapter of "Genomic prediction of complex traits" editted by Nour Ahmadi and Jerome Bartholomé. `★ 2` `MIT`
- [icraf-indonesia/wanulcas](https://github.com/icraf-indonesia/wanulcas) - Water, Nutrient and Light Capture in Agroforestry Systems. `★ 1` `no licence`
- [assignUser/icrop2r](https://github.com/assignUser/icrop2r) - R implementation of the crop model SSM-iCrop2 in R. `custom licence`
- [Chuang2016/spacsysr](https://github.com/Chuang2016/spacsysr) - R implementation of core SPACSYS soil biogeochemistry, photosynthesis and soil water/heat modules (Wu 2022). `no licence`
- [cran/TTR.PGM](https://github.com/cran/TTR.PGM) - :exclamation: This is a read-only mirror of the CRAN R package repository. TTR.PGM — Thornley Transport Resistance Plant Growth Model. `no licence`
- [DataFusion18/T_s_s](https://github.com/DataFusion18/T_s_s) - This is an implementation of Thornley's (https://doi.org/10.1006/anbo.1997.0529) model which includes substrate transport and separate growth for each plant compartment. Transport is now… `no licence`
- [dignatgr/SIMPLEModel](https://github.com/dignatgr/SIMPLEModel) - SIMPLE crop model from Zhao et al 2019. `MIT`
- [kamapu/cropgrowth](https://github.com/kamapu/cropgrowth) - Some functions related to the work with growth models. `no licence`
- [kwadjoahodo/SAFMOD](https://github.com/kwadjoahodo/SAFMOD) - SAFMOD (Sheffield Arable Farm Model) is an arable farm level model, which consists of four modules: profit maximisation, nitrate leaching and risk minimisation models, and a goal programming model… `no licence`
- [model-library-pps/FARMSIM_archive](https://github.com/model-library-pps/FARMSIM_archive) - FARMSIM: integrated crop–livestock farm model coupling crop-soil (FIELD), livestock (LIVSIM) and manure (HEAPSIM) modules. `custom licence`
- [model-library-pps/LINTUL-1-and-2-in-R_archive](https://github.com/model-library-pps/LINTUL-1-and-2-in-R_archive) - LINTUL-1 and LINTUL-2 in R with parameters for spring wheat and maize. `custom licence`
- [SticsRPacks/miniSTICS](https://github.com/SticsRPacks/miniSTICS) - A simplified crop model derived from STICS. `Apache-2.0`
- [Tesfahun54/Grop_Growth_ODE_Rproject](https://github.com/Tesfahun54/Grop_Growth_ODE_Rproject) - Developing Crop growth model with ODE. `no licence`

<a id="general-crop-scheme"></a>

#### Scheme

- [OpenCLIM/ecocrop](https://github.com/OpenCLIM/ecocrop) - Crop suitability model using the FAO EcoCrop crop characteristic database. `★ 15` `no licence`

<a id="general-crop-visual-basic"></a>

#### Visual Basic

- [CropModelingPlatform/CelsiusV32](https://github.com/CropModelingPlatform/CelsiusV32) - CELSIUS Crop Model. `BSD-3-Clause`
- [model-library-pps/CroppingCalendarConstructionModel_archive](https://github.com/model-library-pps/CroppingCalendarConstructionModel_archive) - Cropping Calendar Construction (CCC) model (Excel/VBA) testing whether two or three crops fit into one year. `custom licence`

<a id="general-crop-vue"></a>

#### Vue

- [ternandsparrow/pollin8-web-client](https://github.com/ternandsparrow/pollin8-web-client) - A webapp to run simulations on how planting revegetation and varroa mite influence crop pollination and therefore yield. `MIT`

<a id="general-crop-wolfram-language"></a>

#### Wolfram Language

- [MuhmmadUmerShehzad/DigitalTwin](https://github.com/MuhmmadUmerShehzad/DigitalTwin) - Crop Growth Simulator - providing insights on yield increase based on the fertilizer applied. `no licence`

<a id="general-crop-other"></a>

#### Other

- [gc13141112/agriculture](https://github.com/gc13141112/agriculture) - Python reimplementations of crop models, starting with DSSAT (Chinese). `★ 3` `no licence`
- [Xuxu2233/AHC-model-v2.1R](https://github.com/Xuxu2233/AHC-model-v2.1R) - AHC v2.1R, a one-dimensional agro-hydrological, chemical and crop systems simulator. `★ 3` `no licence`
- [gcostaneto/CropGrowthModels](https://github.com/gcostaneto/CropGrowthModels) - Simple crop growth models and water balance routines for envirotyping and phenotypic prediction. `★ 2` `no licence`
- [CaybleS/PlantSim](https://github.com/CaybleS/PlantSim) - A Multi-Agent simulation utilizing Repast Simphony that models the behavior of the growth of Sorghum and Maize. Created under research grant to model the root and shoot of a plant simultaneously. `no licence`
- [degi/talas](https://github.com/degi/talas) - Trees and Agroforestry to Leverage Agroecosystem Service. `no licence`
- [garofalopasquale/EaSiCroM](https://github.com/garofalopasquale/EaSiCroM) - Crop simulation model very simple to use. `no licence`
- [GiuliaVico/M3-MinimalistMixtureModel](https://github.com/GiuliaVico/M3-MinimalistMixtureModel) - M3 Minimalist Mixture Model. `GPL-3.0`
- [jchburmester/perennial-crop](https://github.com/jchburmester/perennial-crop) - Modelling and Evaluation framework for the Master Thesis "Rooting in Soil and Science: Process-Based Modelling and Uncertainty Quantification of Perennial Wheat Growth in Skane, Sweden" (2026, Lund… `no licence`
- [Kikysee/WOFOST-with-YRF](https://github.com/Kikysee/WOFOST-with-YRF) - This repository introduces the yield reduction factor added to the WOFOST model, its function, and how it modifies carbon dioxide assimilation. `CC0-1.0`
- [MoBerg97/TB-AgroEcoSystem](https://github.com/MoBerg97/TB-AgroEcoSystem) - A trait-based agroecosystem model. `no licence`
- [MuahmmadDanyalAashar/Modular-Crop-Growth-Model-and-Simulation-](https://github.com/MuahmmadDanyalAashar/Modular-Crop-Growth-Model-and-Simulation-) - Crop growth model is an excellent example of object oriented paradigm. Such a model is composed of a number of parts like plant, soil, weather, etc. Being able to handle all of these separately as… `no licence`
- [PSUmodeling/Cycles-L](https://github.com/PSUmodeling/Cycles-L) - Landscape-scale agroecosystem and hydrology model coupling Flux-PIHM with Cycles. `no licence`
- [SARRA-cropmodels/SARRA-H](https://github.com/SARRA-cropmodels/SARRA-H) - SARRA-H crop model software for Windows. `no licence`
- [SARRA-cropmodels/SARRA-O](https://github.com/SARRA-cropmodels/SARRA-O) - SARRA-O spatial crop model software for Windows. `custom licence`
- [VVXU98/Code_Improving-photosynthate-allocation-dynamic-simulations-of-crops-under-water-stress-conditions](https://github.com/VVXU98/Code_Improving-photosynthate-allocation-dynamic-simulations-of-crops-under-water-stress-conditions) - Agro-C model optimization code. `no licence`

<a id="rice"></a>

### Rice

<a id="rice-cplusplus"></a>

#### C++

- [cropmodels/Roryza](https://github.com/cropmodels/Roryza) - R package for the ORYZA2000 rice growth model. `no licence`

<a id="rice-fortran"></a>

#### Fortran

- [Krish962/PRISM](https://github.com/Krish962/PRISM) - Web decision-support system for rice simulation with DSSAT run through R. `★ 1` `no licence`
- [spark-hydro/swatp-paddy](https://github.com/spark-hydro/swatp-paddy) - swatplus model with paddy module. `GPL-3.0`
- [USDA-ARS-ACSL/RICESIM-ORYZA](https://github.com/USDA-ARS-ACSL/RICESIM-ORYZA) - Modified ORYZA rice model from USDA-ARS ACSL, with nonlinear temperature responses for development. `no licence`

<a id="rice-java"></a>

#### Java

- [lfxu1/riceSpacingOpt](https://github.com/lfxu1/riceSpacingOpt) - Combining a rice FSPM and an optimization algorithm MPSA to obtain the optimal plant spacing. `★ 2` `no licence`
- [RomuloPBenedetti/CropModelsUFSM-Framework](https://github.com/RomuloPBenedetti/CropModelsUFSM-Framework) - Crop Models UFSM. `no licence`

<a id="rice-matlab"></a>

#### MATLAB

- [svijayakumar32/ePhotosynthesis-Rice](https://github.com/svijayakumar32/ePhotosynthesis-Rice) - A workflow for calibration, parameter optimisation, and input scaling in a metabolic model of rice photosynthesis. `GPL-3.0`

<a id="rice-netlogo"></a>

#### NetLogo

- [mjstoroz/Balinese-Irrigation-System-Simulation-Lansing-Kremer1993](https://github.com/mjstoroz/Balinese-Irrigation-System-Simulation-Lansing-Kremer1993) - This is a NetLogo replication of the hill-climbing version of the Lansing-Kremer model of Balinese irrigation found on CoMSES and updated to work out of the box for Netlogo 6.3.0. `no licence`

<a id="rice-python"></a>

#### Python

- [atoz03/rice_growth](https://github.com/atoz03/rice_growth) - Rice growth simulation and trajectory prediction with PCSE/WOFOST and an ORYZA interface. `★ 2` `no licence`
- [ky0on/pysimriw](https://github.com/ky0on/pysimriw) - SIMRIW (SImulation Model for RIce-weather relations). `★ 2` `no licence`
- [IsaacIgb/Phytoacoustics-Rice-Simulator](https://github.com/IsaacIgb/Phytoacoustics-Rice-Simulator) - Made to simulate how sound treatments affect rice growth, yield, water status and stress resilience. It combines rice growth modeling, sound effect prediction, field acoustics, and a virtual paddy… `★ 1` `no licence`
- [PlantSystemsBiology/mCanopyRice](https://github.com/PlantSystemsBiology/mCanopyRice) - Rice canopy model and 3D point cloud data. `★ 1` `GPL-3.0`
- [3LuisF/Gemelo-Digital-Cultivos-arroz](https://github.com/3LuisF/Gemelo-Digital-Cultivos-arroz) - Proyecto de ingenieria universitaria para el desarrollo de un gemelo digital de cultivos colombianos. `no licence`
- [lqc00001-coder/Sleepstill](https://github.com/lqc00001-coder/Sleepstill) - A Hybrid machine-learning and process-based regional crop modelling framework to improve rice production strategies under data constraints. `no licence`
- [mauriceccy/rice-crop-fba-model](https://github.com/mauriceccy/rice-crop-fba-model) - Flux balance analysis model of rice growth under normal and stress conditions. `no licence`
- [SmartAG-NWAFU/rice_phenology_hypernet](https://github.com/SmartAG-NWAFU/rice_phenology_hypernet) - Rice phenology prediction with learned corrections to photothermal response models. `no licence`

<a id="rice-r"></a>

#### R

- [Onogi/HeadingDatePrediction](https://github.com/Onogi/HeadingDatePrediction) - The input files, scripts, and results of "Integrating genomic prediction with crop modelling: application in predicting rice heading date" by Onogi et al. are provided. `★ 4` `no licence`
- [malachycampbell/RiceCGM](https://github.com/malachycampbell/RiceCGM) - Data and code for "Leveraging genome-enabled growth models to study shoot growth responses to water deficit in rice (Oryza sativa)". `★ 1` `no licence`
- [agrocompuepidemlab/Rice-agroclimatic-model](https://github.com/agrocompuepidemlab/Rice-agroclimatic-model) - Agroclimatic model for rice. `no licence`
- [EcoInfoLab/YIN](https://github.com/EcoInfoLab/YIN) - Yin et al. (1995) nonlinear model for estimating rice heading dates. `no licence`
- [NJAU-ZJH/RiceGrow_phenology](https://github.com/NJAU-ZJH/RiceGrow_phenology) - Phenology module of the RiceGrow rice model. `no licence`

<a id="rice-other"></a>

#### Other

- [AtsushiMaruyama/A-water-temperarture-model-for-rice-paddies](https://github.com/AtsushiMaruyama/A-water-temperarture-model-for-rice-paddies) - A calculation sample of "A water temperature simulation model for rice paddies with variable water depths". `no licence`
- [shymamangalath/SWAT-Rice](https://github.com/shymamangalath/SWAT-Rice) - Process-based paddy irrigation module for SWAT. `no licence`
- [TaoLi999/ORYZA_v3](https://github.com/TaoLi999/ORYZA_v3) - Use to files transpotation among ORYZA community. `no licence`
- [vnfms3259/CERES-rice](https://github.com/vnfms3259/CERES-rice) - CERES-rice model source code share. `no licence`

<a id="wheat"></a>

### Wheat

<a id="wheat-csharp"></a>

#### C#

- [SiriusQuality/SiriusQuality-BioMa-WheatPotentialLAI-Component](https://github.com/SiriusQuality/SiriusQuality-BioMa-WheatPotentialLAI-Component) - BioMa component of Leaf Area Index in wheat crop model Sirius Quality. `★ 1` `MIT`
- [SiriusQuality/SiriusQuality-BioMa-Irradiance-Component](https://github.com/SiriusQuality/SiriusQuality-BioMa-Irradiance-Component) - A BioMa component for irradiance absorbed by leaves in SiriusQuality Crop Model. `MIT`

<a id="wheat-fortran"></a>

#### Fortran

- [SiriusQuality/Release](https://github.com/SiriusQuality/Release) - Sirius Quality 2 Public version. `★ 1` `MIT`
- [USDA-ARS-ACSL/WheatSim](https://github.com/USDA-ARS-ACSL/WheatSim) - Wheat simulation model (Fortran) from the USDA-ARS Adaptive Cropping Systems Laboratory. `★ 1` `no licence`
- [model-library-pps/NWHEAT_archive](https://github.com/model-library-pps/NWHEAT_archive) - Archived wheat growth model with water and nitrogen limitations. `custom licence`

<a id="wheat-javascript"></a>

#### JavaScript

- [Anhouse-Sakai/Wheat-Spike-Layer-Modeler](https://github.com/Anhouse-Sakai/Wheat-Spike-Layer-Modeler) - Open-source multilingual wheat spike-layer simulation modeler for Windows, macOS, and the web. `★ 5` `MIT`
- [YixiangShan/FSP_wheat_domestication](https://github.com/YixiangShan/FSP_wheat_domestication) - GroIMP functional-structural model of wheat growth for a domestication study. `no licence`

<a id="wheat-python"></a>

#### Python

- [AgriculturalModelExchangeInitiative/SQ_Wheat_Phenology](https://github.com/AgriculturalModelExchangeInitiative/SQ_Wheat_Phenology) - Model of wheat phenology of the crop growth simulation model SiriusQuality. `★ 6` `MIT`
- [openalea/WALTer](https://github.com/openalea/WALTer) - WALTer is a 3D FSPM Wheat model. `★ 6` `custom licence`
- [egiron/pywheat](https://github.com/egiron/pywheat) - Python library for simulation of wheat phenological development, crop growth and yield. `★ 3` `MIT`
- [openalea-incubator/cn-wheat](https://github.com/openalea-incubator/cn-wheat) - Functional-structural model of carbon and nitrogen distribution in wheat culms. `★ 2` `custom licence`
- [openalea-incubator/fspm-wheat](https://github.com/openalea-incubator/fspm-wheat) - Coupled functional-structural plant model of wheat. `★ 2` `custom licence`
- [egiron/TemperatureFunct](https://github.com/egiron/TemperatureFunct) - Library to apply Temperature Functions in crop modelling. `★ 1` `GPL-3.0`
- [JohnnyHewson/Plant-Growth](https://github.com/JohnnyHewson/Plant-Growth) - Code for ABC-PV project on projecting plant growth using 'A winter wheat crop simulation model without water or nutrient limitations' by A. H. Weir (1984). `★ 1` `MIT`
- [openalea-incubator/echap](https://github.com/openalea-incubator/echap) - Wheat canopy simulations from the OpenAlea Echap project. `★ 1` `custom licence`
- [openalea-incubator/elong-wheat](https://github.com/openalea-incubator/elong-wheat) - Leaf elongation model for wheat that accounts for carbon and nitrogen status. `★ 1` `custom licence`
- [WheatGrow/WG4GEE](https://github.com/WheatGrow/WG4GEE) - WG4GEE model implementation approach. `★ 1` `no licence`
- [baiyileilei/wheat-tritium-model](https://github.com/baiyileilei/wheat-tritium-model) - Model of organically bound tritium in wheat organs after exposure to atmospheric HTO. `no licence`
- [GeraultTr/Wheat-BRIDGES](https://github.com/GeraultTr/Wheat-BRIDGES) - Wheat Biogeochemical Root-shoot Integration by Development and Growth of heterogeneous Environmental Signals. `custom licence`
- [openalea-incubator/farquhar-wheat](https://github.com/openalea-incubator/farquhar-wheat) - Farquhar photosynthesis model for wheat, a component of FSPM-Wheat. `custom licence`
- [openalea-incubator/growth-wheat](https://github.com/openalea-incubator/growth-wheat) - Mechanistic model of wheat growth, a component of FSPM-Wheat. `custom licence`
- [openalea-incubator/respi-wheat](https://github.com/openalea-incubator/respi-wheat) - Respiration model for wheat, a component of FSPM-Wheat. `custom licence`
- [openalea-incubator/senesc-wheat](https://github.com/openalea-incubator/senesc-wheat) - Senescence model for wheat, a component of FSPM-Wheat. `custom licence`
- [SmartDigitalAg/APSIM_Wheat_Phenology](https://github.com/SmartDigitalAg/APSIM_Wheat_Phenology) - APSIM Wheat Phenology 모델 분리. `no licence`

<a id="wheat-r"></a>

#### R

- [APSIMInitiative/APSIMWheatPhenology](https://github.com/APSIMInitiative/APSIMWheatPhenology) - R rewrite of the APSIM wheat phenology model for fast repeated simulation. `★ 2` `custom licence`
- [byzheng/rapsimng.wheat](https://github.com/byzheng/rapsimng.wheat) - Wheat Model for APSIM NG. `custom licence`
- [ikawah799/WheatCNmodel](https://github.com/ikawah799/WheatCNmodel) - Crop growth–nitrogen uptake model. `no licence`

<a id="wheat-raku"></a>

#### Raku

- [robertocesetti/winter-wheat-growth-cycle](https://github.com/robertocesetti/winter-wheat-growth-cycle) - The wheat growth cycle is characterized by several phases, each of which is influenced by certain factors. It is interesting to observe and analyze how a wheat plantation grows under different… `★ 1` `MIT`

<a id="maize"></a>

### Maize

<a id="maize-csharp"></a>

#### C#

- [SiriusQuality/-SiriusQuality-BioMa-MaizeLAI-Component](https://github.com/SiriusQuality/-SiriusQuality-BioMa-MaizeLAI-Component) - Maize LAI BioMa Component. `MIT`

<a id="maize-cplusplus"></a>

#### C++

- [bocinsky/Bocinsky_Varien_2017](https://github.com/bocinsky/Bocinsky_Varien_2017) - Source code for Bocinsky and Varien 2017, "Calibrating Maize Paleoproduction Models using Experimental Data". `★ 2` `MIT`

<a id="maize-fortran"></a>

#### Fortran

- [USDA-ARS-ACSL/MAIZSIM](https://github.com/USDA-ARS-ACSL/MAIZSIM) - Maize simulation code from the USDA adaptive cropping systems laboratory. `★ 17` `Unlicense`
- [jonlizaso/CSM46-ASI](https://github.com/jonlizaso/CSM46-ASI) - CERES-ASI. `no licence`
- [USDA-REE-ARS/MAIZSIM-Simulation-Model](https://github.com/USDA-REE-ARS/MAIZSIM-Simulation-Model) - A simulator for Maize plants. `Unlicense`

<a id="maize-java"></a>

#### Java

- [plantmodelling/planetBatch](https://github.com/plantmodelling/planetBatch) - PlaNet-Maize model. `★ 3` `Apache-2.0`

<a id="maize-python"></a>

#### Python

- [ecohydro/maize-Toff](https://github.com/ecohydro/maize-Toff) - Repo for modeling analysis of of maize yield variability and tradeoffs between yield and crop failure. `★ 5` `no licence`
- [mserouar/CORNIBU](https://github.com/mserouar/CORNIBU) - 3D architectural canopy structure of maize plants. `★ 3` `MIT`
- [juksentang/agri-jax](https://github.com/juksentang/agri-jax) - Differentiable, batch-parallel field-scale crop-soil models in JAX (CERES-Maize + RZWQM-style soil water/PET). pip install agrijax. `★ 2` `custom licence`
- [langmm/canopy_factory](https://github.com/langmm/canopy_factory) - Attempt at maize canopy architecture model. `★ 1` `GPL-3.0`
- [Anti-Shane/extreme-risk-maize-dss](https://github.com/Anti-Shane/extreme-risk-maize-dss) - A Decision Support System for maize resilience using FAO-56 physiology and CVaR optimization. `no licence`
- [ckwee/Agricultural-Production-System-Simulator](https://github.com/ckwee/Agricultural-Production-System-Simulator) - Agricultural Production System Simulator. `no licence`
- [MossLouvan/agrosim](https://github.com/MossLouvan/agrosim) - Gymnasium-compatible, LLM-native simulation environment for agricultural decision-making. Iowa corn season in &lt;1s; benchmark across irrigation, pest, and harvest tasks. `MIT`

<a id="maize-r"></a>

#### R

- [plantmodelling/simple_fspm](https://github.com/plantmodelling/simple_fspm) - Web interface for a simple plant model. `★ 1` `Apache-2.0`
- [AhmadShahnewaz/SOC_cropbiomass](https://github.com/AhmadShahnewaz/SOC_cropbiomass) - The aim of the code is to develop a maize growth model to simulate biomass production and partitioning; apply the ICBM model to simulate SOC dynamics based on maize biomass inputs. `no licence`
- [ansleybrown1337/Corn-yield-salinity-response](https://github.com/ansleybrown1337/Corn-yield-salinity-response) - Tool used to calibrate and compare salinity tolerance index functions, using a real corn dataset as an example. `MIT`
- [drshaymac/Maize_model](https://github.com/drshaymac/Maize_model) - Exercise implementing the simple maize model of Wallach et al. (2014). `no licence`
- [KevinOluoch/MSPP](https://github.com/KevinOluoch/MSPP) - Tool for modelling maize phenology to predict the number of days to the flowering date and maturity date. `no licence`

<a id="maize-typescript"></a>

#### TypeScript

- [lmnitzsche/corn-production-simulation](https://github.com/lmnitzsche/corn-production-simulation) - Built an interactive TypeScript application with Vite for real-time corn growth simulation. Implemented GDU calculation algorithms based on University of Illinois research; integrated Chart.js and… `★ 5` `MIT`

<a id="maize-other"></a>

#### Other

- [tallnutt/GMcalculator](https://github.com/tallnutt/GMcalculator) - Excel VBA code for implementing a model to extimate GM pollination between maize fields. `no licence`

<a id="other-cereals"></a>

### Barley, sorghum, millet and other cereals

<a id="other-cereals-fortran"></a>

#### Fortran

- [USDA-ARS-ACSL/RYESIM](https://github.com/USDA-ARS-ACSL/RYESIM) - Rye simulation implementation from the USDA cropping systems laboratory. `GPL-3.0`

<a id="other-cereals-python"></a>

#### Python

- [SmartAG-Team/qing_ke_model](https://github.com/SmartAG-Team/qing_ke_model) - A Winter Barley Model for Optimizing Sowing Dates and Variety Selection on the Tibetan Plateau. `MIT`

<a id="other-cereals-r"></a>

#### R

- [GuillermoMarcillo/RyeBiom](https://github.com/GuillermoMarcillo/RyeBiom) - A set of functions to simulate cover crop growth under non-stress conditions. `no licence`

<a id="other-cereals-other"></a>

#### Other

- [sorghum21/Panelo-et-al-2025_The-Plant-Genome](https://github.com/sorghum21/Panelo-et-al-2025_The-Plant-Genome) - Crop growth model‐enabled genetic mapping of biomass accumulation dynamics in photoperiod‐sensitive sorghum. `no licence`

<a id="soybean"></a>

### Soybean

<a id="soybean-cplusplus"></a>

#### C++

- [Matthews-Research-Group/UTRSoybeanBML](https://github.com/Matthews-Research-Group/UTRSoybeanBML) - BioCro module library with a Thornley utilization–transport–resistance model for soybean. `custom licence`

<a id="soybean-fortran"></a>

#### Fortran

- [USDA-ARS-ACSL/2DGLYCIM](https://github.com/USDA-ARS-ACSL/2DGLYCIM) - Soybean simulation implementation from the USDA GLYCIM model family. `★ 2` `no licence`

<a id="soybean-python"></a>

#### Python

- [RodrigoAgronomia/SoybeanMaturityModel](https://github.com/RodrigoAgronomia/SoybeanMaturityModel) - Temporary Repository. `★ 1` `no licence`
- [Chuchung0604/GLYCIM_phenol](https://github.com/Chuchung0604/GLYCIM_phenol) - simulating growth stage of GLYCIM model. `no licence`

<a id="soybean-r"></a>

#### R

- [cropsinsilico/Soybean-BioCro](https://github.com/cropsinsilico/Soybean-BioCro) - Soybean version of the BioCro crop growth model, now part of BioCro. `★ 2` `no licence`

<a id="legumes-oilseeds"></a>

### Other legumes and oilseeds

<a id="legumes-oilseeds-cplusplus"></a>

#### C++

- [AndreyAgeev/SSM_2018](https://github.com/AndreyAgeev/SSM_2018) - SSM-chickpea is a model for chickpea development, growth and yield (Soltani and Sinclair, 2011). This SSM model is the same as that described by Soltani and Sinclair with modifications. `no licence`

<a id="legumes-oilseeds-fortran"></a>

#### Fortran

- [model-library-pps/LINTUL-BRASNAP_archive](https://github.com/model-library-pps/LINTUL-BRASNAP_archive) - LINTUL-BRASNAP: growth model of winter oilseed rape (Brassica napus). `custom licence`

<a id="legumes-oilseeds-python"></a>

#### Python

- [openalea-incubator/colzette](https://github.com/openalea-incubator/colzette) - A Parametric Model for oilseed rape and legume. `★ 1` `custom licence`
- [veenaplohiya7/The-Lupin-crop-model](https://github.com/veenaplohiya7/The-Lupin-crop-model) - Masters Thesis - Veena Lohiya/Uni-Bonn/RWTHAachen/The Matuszyńska Lab. `no licence`

<a id="legumes-oilseeds-r"></a>

#### R

- [picasa/rsunflo](https://github.com/picasa/rsunflo) - Tools for phenotyping, simulating and modelling with the SUNFLO crop model. `★ 11` `no licence`
- [byzheng/rapsimng.fababean](https://github.com/byzheng/rapsimng.fababean) - Fababean Model for APSIM NG. `custom licence`
- [byzheng/rapsimng.lentil](https://github.com/byzheng/rapsimng.lentil) - Lentil Model for APSIM NG. `custom licence`
- [byzheng/rapsimng.lupin](https://github.com/byzheng/rapsimng.lupin) - Lupin Model for APSIM NG. `custom licence`

<a id="legumes-oilseeds-other"></a>

#### Other

- [picasa/sunflower](https://github.com/picasa/sunflower) - An ecophysiological model for the sunflower crop. `no licence`

<a id="potato"></a>

### Potato

<a id="potato-fortran"></a>

#### Fortran

- [model-library-pps/NPOTATO_archive](https://github.com/model-library-pps/NPOTATO_archive) - Archived potato growth model with water and nitrogen limitations. `custom licence`
- [model-library-pps/POTATOS_archive](https://github.com/model-library-pps/POTATOS_archive) - POTATOS: simple LINTUL-type potato growth model. `custom licence`
- [USDA-ARS-ACSL/SPUDSIM](https://github.com/USDA-ARS-ACSL/SPUDSIM) - Potato simulation code from the USDA adaptive cropping systems laboratory. `no licence`

<a id="potato-pascal"></a>

#### Pascal

- [jose-g/solanum](https://github.com/jose-g/solanum) - SOLANUM is a user-friendly crop growth model that simulates tuber dry mass assimilation in different potato species (Solanum sp.), varieties and hybrids. The model estimates the tuber yield under… `★ 4` `no licence`

<a id="potato-python"></a>

#### Python

- [kundun14/py_solanum](https://github.com/kundun14/py_solanum) - A Python Implementation of the SOLANUM Potato Crop Model for Andean Conditions. `★ 1` `no licence`
- [saanvikakde/potato-dt](https://github.com/saanvikakde/potato-dt) - Lightweight digital twin of potato growth in greenhouses and other controlled environments. `no licence`

<a id="roots-tubers"></a>

### Cassava and other roots and tubers

<a id="roots-tubers-fortran"></a>

#### Fortran

- [mylesjfisher/ciatcas](https://github.com/mylesjfisher/ciatcas) - DSSAT cassava code derived from Tony Hunt's CSCAS, with the complete MY13 code. `no licence`

<a id="roots-tubers-fst"></a>

#### FST

- [model-library-pps/LINTUL2-Cassava_archive](https://github.com/model-library-pps/LINTUL2-Cassava_archive) - LINTUL2-CASSAVA (Fortran/FST): water-limited growth model of cassava. `custom licence`

<a id="roots-tubers-pascal"></a>

#### Pascal

- [jose-g/sweetpo](https://github.com/jose-g/sweetpo) - SWEETPO is a user-friendly crop growth model that simulates dry mass assimilation in different sweet potato (Ipomea batata) varieties. The model simulates daily dry matter increments in storage… `★ 1` `no licence`

<a id="roots-tubers-python"></a>

#### Python

- [herman-berghuijs/lintul_cassava_standalone](https://github.com/herman-berghuijs/lintul_cassava_standalone) - Example of how lintul_cassava can be run with PCSE functionality, but without actually implementing it in PCSE. `custom licence`
- [model-library-pps/lintul-cassava-npk](https://github.com/model-library-pps/lintul-cassava-npk) - Python implementation of the LINTUL Cassava NPK model. `custom licence`

<a id="roots-tubers-r"></a>

#### R

- [cropmodels/LINTULcassava](https://github.com/cropmodels/LINTULcassava) - R package for the LINTUL-CASSAVA crop growth model. `★ 1` `EUPL-1.2`
- [model-library-pps/LINTUL-2-Cassava-in-R_archive](https://github.com/model-library-pps/LINTUL-2-Cassava-in-R_archive) - LINTUL2-CASSAVA in R for rainfed and irrigated cassava. `custom licence`
- [model-library-pps/LINTUL_Cassava_NPK_archive](https://github.com/model-library-pps/LINTUL_Cassava_NPK_archive) - Archived cassava implementation with nutrient-related growth constraints. `custom licence`

<a id="cotton"></a>

### Cotton

<a id="cotton-fortran"></a>

#### Fortran

- [USDA-ARS-ACSL/GOSSYM-2DSOIL](https://github.com/USDA-ARS-ACSL/GOSSYM-2DSOIL) - GOSSYM cotton model merged with the 2DSOIL soil model. `★ 1` `no licence`
- [USDA-ARS-ACSL/GOSSYM_Orig](https://github.com/USDA-ARS-ACSL/GOSSYM_Orig) - Historical GOSSYM cotton growth simulation code. `★ 1` `no licence`

<a id="cotton-java"></a>

#### Java

- [jinyuling/CottonGrowthModelManage](https://github.com/jinyuling/CottonGrowthModelManage) - Java (Spring Boot) system for simulating and managing cotton growth data. `no licence`

<a id="cotton-python"></a>

#### Python

- [md-noman-research/cotton-yield-simulation](https://github.com/md-noman-research/cotton-yield-simulation) - Understanding cotton yield penalties under coastal salinity and heat stress: a mechanistic simulation and statistical audit. `MIT`
- [ruilibuaa/Cotton_Growth_-Curve_Simulation](https://github.com/ruilibuaa/Cotton_Growth_-Curve_Simulation) - Five-parameter growth curve simulation for cotton. `no licence`
- [tcztzy/cotton2k-core](https://github.com/tcztzy/cotton2k-core) - Cotton2K Model core. `no licence`

<a id="cotton-r"></a>

#### R

- [uace-azmet/cotton-growth-stages-and-heat-units](https://github.com/uace-azmet/cotton-growth-stages-and-heat-units) - Shiny app estimating cotton growth stages from cumulative heat units at Arizona AZMet stations. `no licence`

<a id="cotton-rust"></a>

#### Rust

- [tcztzy/cotton2k](https://github.com/tcztzy/cotton2k) - Simulation model for cotton. `★ 4` `custom licence`

<a id="cotton-other"></a>

#### Other

- [tcztzy/cotton2k-app](https://github.com/tcztzy/cotton2k-app) - Cotton2K is a cotton simulation model specially adapted for irrigated cotton production in arid regions. `no licence`

<a id="sugar-crops"></a>

### Sugarcane and sugar beet

<a id="sugar-crops-fortran"></a>

#### Fortran

- [ChristinaMathias/MOSICAS](https://github.com/ChristinaMathias/MOSICAS) - Sugarcane crop growth model. `★ 4` `GPL-3.0`
- [Murilodsv/SWAP-SAMUCA](https://github.com/Murilodsv/SWAP-SAMUCA) - Process-based crop model for simulations of sugarcane growth and water dynamics. `★ 1` `LGPL-2.1`

<a id="vegetables"></a>

### Vegetables

<a id="vegetables-cplusplus"></a>

#### C++

- [uwkimlab/cropbox-garlic](https://github.com/uwkimlab/cropbox-garlic) - Garlic Crop Simulation Model. `MIT`

<a id="vegetables-fortran"></a>

#### Fortran

- [itsjameshan/CN-strawberryDSSAT](https://github.com/itsjameshan/CN-strawberryDSSAT) - Python implementation of the CROPGRO-Strawberry model adapted from DSSAT. `★ 2` `BSD-3-Clause`
- [TM-Abir-Ahsan/Tomato-Crop-Growth-Model](https://github.com/TM-Abir-Ahsan/Tomato-Crop-Growth-Model) - Tomato crop growth model in Fortran. `★ 2` `no licence`

<a id="vegetables-gaml"></a>

#### GAML

- [czh16/Greenhouse_Strawberry_Bee_Simulation](https://github.com/czh16/Greenhouse_Strawberry_Bee_Simulation) - Agent-based GAMA simulation of bee pollination of greenhouse strawberries. `Apache-2.0`
- [LiliDupDev/hydroponics](https://github.com/LiliDupDev/hydroponics) - An ABM model to simulate hydroponic tomato based on TOMGRO. `no licence`

<a id="vegetables-javascript"></a>

#### JavaScript

- [Micbut/FSP-model-dwarf-tomato](https://github.com/Micbut/FSP-model-dwarf-tomato) - Functional–structural plant (FSP) model of dwarf tomato implemented in GroIMP to simulate 3D plant architecture, light interception, photosynthesis, and growth in vertical farming systems. Supports… `★ 4` `no licence`
- [ksmolen2/vtc](https://github.com/ksmolen2/vtc) - Virtual Tomato Crop repository with a dynamic (4D) tomato FSP model. `★ 3` `no licence`

<a id="vegetables-julia"></a>

#### Julia

- [cropbox/Garlic.jl](https://github.com/cropbox/Garlic.jl) - Garlic growth simulation model implemented with Cropbox. `★ 8` `MIT`
- [MinjiShin/Radish.jl](https://github.com/MinjiShin/Radish.jl) - Radish growth model built on the Cropbox framework. `MIT`

<a id="vegetables-matlab"></a>

#### MATLAB

- [jayed008/tomato_growth_model](https://github.com/jayed008/tomato_growth_model) - Whole-season tomato growth model with photosynthesis and dry-matter partitioning. `★ 1` `no licence`
- [DeustoTech/KPI-Simulation-AGROSOFC](https://github.com/DeustoTech/KPI-Simulation-AGROSOFC) - Tomato production simulation for greenhouse KPIs in the AGROSOFC project. `no licence`

<a id="vegetables-python"></a>

#### Python

- [openalea/strawberry](https://github.com/openalea/strawberry) - Strawberry architecture analysis and reconstruction. `★ 20` `custom licence`
- [gyosit/Reduced_TOMGRO.Lab_2019](https://github.com/gyosit/Reduced_TOMGRO.Lab_2019) - Reduced TOMGRO tomato growth model. `★ 14` `no licence`
- [EthanSeok/Cabbage_PBM](https://github.com/EthanSeok/Cabbage_PBM) - Process-based cabbage growth model in Python. `★ 8` `no licence`
- [EthanSeok/lettuce_PBM](https://github.com/EthanSeok/lettuce_PBM) - Process-based lettuce growth model in Python for greenhouse control. `★ 6` `no licence`
- [cariso27001/Garcumber](https://github.com/cariso27001/Garcumber) - Cucumber model adapted from Garlic.jl on the Cropbox framework. `★ 1` `MIT`
- [cariso27001/Garttuce](https://github.com/cariso27001/Garttuce) - Lettuce model adapted from the Cropbox garlic model. `★ 1` `MIT`
- [EthanSeok/Kale_PBM](https://github.com/EthanSeok/Kale_PBM) - Cabbage_PBM 기반 Process Based 케일 생육 모델 (Kale growth model). `★ 1` `no licence`
- [MinjiShin/radish-fspm-openalea](https://github.com/MinjiShin/radish-fspm-openalea) - Functional-structural radish model built with OpenAlea. `★ 1` `no licence`
- [naofujiuchi/tomgrosim-on-pcse](https://github.com/naofujiuchi/tomgrosim-on-pcse) - Growth model of tomato based on PCSE. `★ 1` `GPL-3.0`
- [ataraxno/pap_crop_model](https://github.com/ataraxno/pap_crop_model) - Python crop model for sweet peppers. `Apache-2.0`
- [Ayanoinlab/Mustard-Greens-FSPM](https://github.com/Ayanoinlab/Mustard-Greens-FSPM) - Analysis pipeline for a GroIMP functional-structural model of mustard greens. `no licence`
- [chillguyaliali/Reduced-State-Tomgro](https://github.com/chillguyaliali/Reduced-State-Tomgro) - Python implementation of reduced state TOMGRO. First time hand coding a mechanistic crop model. Not the most elegant. 5 sections. Parameters, Functions, Data Aquisition & Cleaning, Main, &… `no licence`
- [maybornegit/observer-nicolet](https://github.com/maybornegit/observer-nicolet) - Prediction model for the growth trajectory of lettuce. Simulation of growth based on real-time environmental data and predicts biomass information. `no licence`
- [nisheri-ascar/WaterSpinachLSystemResearch](https://github.com/nisheri-ascar/WaterSpinachLSystemResearch) - Code repository for research. `no licence`
- [skkim76/Cucumber](https://github.com/skkim76/Cucumber) - Process-based cucumber growth model: canopy photosynthesis, biomass and partitioning. `no licence`
- [StefanBaar/FruitSizeEstimator](https://github.com/StefanBaar/FruitSizeEstimator) - Supplementary material for the publication: A logistic model for precise tomato fruit-growth prediction based on diameter-time evolution. `GPL-3.0`
- [suleymagination/mechanistic-tomato-crop-model](https://github.com/suleymagination/mechanistic-tomato-crop-model) - Mechanistic dwarf tomato growth & water-use model in Python, calibrated using WUR 4th Autonomous Greenhouse Challenge datasets. Built for controlled environment agriculture modeling. `MIT`

<a id="vegetables-r"></a>

#### R

- [hortibonn/Climate_Impact_on_Crop_Yield](https://github.com/hortibonn/Climate_Impact_on_Crop_Yield) - R Shiny decision-support app estimating future crop yields under climate change. `custom licence`
- [sohaibhassan1122/single-truss-tomato-digital-twin](https://github.com/sohaibhassan1122/single-truss-tomato-digital-twin) - Hourly mechanistic carbon-balance model of single-truss greenhouse tomato in base R (SUCROS/WOFOST-inspired) — verified to machine-precision conservation. `no licence`
- [statbiscuit/simgro](https://github.com/statbiscuit/simgro) - Simplified TOMGRO tomato growth and yield model. `no licence`

<a id="vegetables-rust"></a>

#### Rust

- [Nick-lt/Simulation-of-Environmental-Capsicum-Kinetics-and-Structure](https://github.com/Nick-lt/Simulation-of-Environmental-Capsicum-Kinetics-and-Structure) - Functional-structural model of auxin transport in growing pepper (Capsicum) plants, in Rust. `no licence`

<a id="vegetables-typescript"></a>

#### TypeScript

- [rajithadesilva/autotom_ui](https://github.com/rajithadesilva/autotom_ui) - User Interface for Autotom Digital Twin. `MIT`
- [viakisun/bioengine](https://github.com/viakisun/bioengine) - Greenhouse tomato digital twin built on Reduced TOMGRO, TOMSIM photosynthesis and fruit growth models. `no licence`
- [yusufal-qodri/Simulasi_Pertumbuhan_Cabe](https://github.com/yusufal-qodri/Simulasi_Pertumbuhan_Cabe) - Web dashboard simulating growth, phenology and water balance of red chili under ENSO scenarios in Bandung, Indonesia. `no licence`

<a id="vegetables-other"></a>

#### Other

- [XiaolongNWAFU/tomatoXL](https://github.com/XiaolongNWAFU/tomatoXL) - 3D canopy photosynthesis model of tomatoes based on XL language in GroIMP platform. `★ 3` `no licence`
- [ChrisPHP/L-Strawb-Py](https://github.com/ChrisPHP/L-Strawb-Py) - L-system based generation of a strawberry plant using lpy. `★ 1` `MIT`

<a id="fruit-vine"></a>

### Fruit trees and grapevine

<a id="fruit-vine-csharp"></a>

#### C#

- [junqi108/APSIM_Grapevine](https://github.com/junqi108/APSIM_Grapevine) - APSIM Next Generation copy used to develop a grapevine model. `custom licence`

<a id="fruit-vine-fortran"></a>

#### Fortran

- [DennisTimlin-USDA/2DSOIL_Grape](https://github.com/DennisTimlin-USDA/2DSOIL_Grape) - A modified version of 2dsoil that will simulate water balances for a grape orchard. `★ 1` `no licence`

<a id="fruit-vine-java"></a>

#### Java

- [filippo-lampa/PATModel](https://github.com/filippo-lampa/PATModel) - Agent-Based Model simulating the lifecycle of multiple pink apple trees in an orchard, made using Repast Symphony ABM toolkit. More info about this apple variety can be found at… `★ 1` `AGPL-3.0`

<a id="fruit-vine-javascript"></a>

#### JavaScript

- [ismi9/grapevine-model](https://github.com/ismi9/grapevine-model) - Interactive season model of grapevine physiology: carbon, nitrogen, BBCH phenology and berry sugar and acidity. `no licence`

<a id="fruit-vine-julia"></a>

#### Julia

- [dmetivie/Phenology.jl](https://github.com/dmetivie/Phenology.jl) - A package for apple and grapevine phenology modelling. `custom licence`

<a id="fruit-vine-python"></a>

#### Python

- [openalea-incubator/MAppleT](https://github.com/openalea-incubator/MAppleT) - Functional_Structural Plant Model of Apple Tree. `★ 8` `no licence`
- [openalea/vmango-lab](https://github.com/openalea/vmango-lab) - A tool for modeling mango tree growth, development, fruit production and architecture. `★ 8` `custom licence`
- [Plant-Food-Research-Open/FruitCropXL](https://github.com/Plant-Food-Research-Open/FruitCropXL) - Modular GroIMP/XL functional–structural plant model coupling 3D architecture, radiation, gas exchange, hydraulics, carbon allocation and fruit growth in grapevine and apple. `★ 3` `GPL-3.0`
- [djacob65/growthmodel](https://github.com/djacob65/growthmodel) - Growth modeling applied to several fruit species. `★ 2` `no licence`
- [openalea/gafam](https://github.com/openalea/gafam) - Growing AgroForestry with Apple in Mediterranean climate. `★ 2` `no licence`
- [openalea/sigflow](https://github.com/openalea/sigflow) - Architectural Model of flowering on fruit trees. `★ 2` `custom licence`
- [vanaprashanth/mango-digital-twin](https://github.com/vanaprashanth/mango-digital-twin) - Sensor-free mango orchard digital twin using weather, soil, Sentinel-2, FAO-56 water balance, and forecast-aware irrigation advisory. `★ 2` `no licence`
- [jvail/vmapplet](https://github.com/jvail/vmapplet) - Refactored implementation of the MAppleT/StocaTree apple tree architecture model. `★ 1` `custom licence`
- [marta2amoros/HMT-Agrivoltaics](https://github.com/marta2amoros/HMT-Agrivoltaics) - Heat and. `★ 1` `MIT`
- [Pepe-Correa/VSIMpy](https://github.com/Pepe-Correa/VSIMpy) - a GUI implementation of the Vineyard Soil Irrigation Model (Pierce et at. 2006) in python. `★ 1` `no licence`
- [CMCC-Foundation/Olive-phenology-models](https://github.com/CMCC-Foundation/Olive-phenology-models) - Phenology models for olive trees. `no licence`
- [openalea-incubator/GrapeInSilico](https://github.com/openalea-incubator/GrapeInSilico) - A user oriented framework for modelling GrapeVine with openalea modules. `no licence`
- [openalea-incubator/topvine](https://github.com/openalea-incubator/topvine) - 3D statistical reconstruction of grapevine canopy structure by cultivar and training system. `no licence`
- [rmoazed/Apple-Orchard-Yield-Modeling-ODEs](https://github.com/rmoazed/Apple-Orchard-Yield-Modeling-ODEs) - This project models apple orchard fruit production as influenced by a variety of environmental and operational factors using ordinary differential equations. A paper on the topic is included in the… `no licence`
- [wsolow/grape_model](https://github.com/wsolow/grape_model) - Grape phenology models (Keller, Washington State University) in WOFOST8/PCSE. `MIT`

<a id="fruit-vine-r"></a>

#### R

- [cran/chillR](https://github.com/cran/chillR) - :exclamation: This is a read-only mirror of the CRAN R package repository. chillR — Statistical Methods for Phenology Analysis in Temperate Fruit Trees. `★ 2` `no licence`
- [ElizabethHoughton/cherrycoldhardiness](https://github.com/ElizabethHoughton/cherrycoldhardiness) - Sweet cherry cold hardiness estimations in cold climate regions. `★ 1` `no licence`
- [amimis/climatree](https://github.com/amimis/climatree) - CO2 sequestration model in tree crops. `GPL-3.0`
- [dschmidt-hgu/ViRi-dev](https://github.com/dschmidt-hgu/ViRi-dev) - Virtual Riesling: GroIMP functional-structural grapevine model (development version). `MIT`
- [elisehellwig/phenoclim](https://github.com/elisehellwig/phenoclim) - An R package to automate the fitting of flowering and maturity models for fruit and nut trees. `no licence`
- [fredboudon/vmango](https://github.com/fredboudon/vmango) - Simulation and modelling of mango trees. `custom licence`
- [mdredwanahmad/FST_CropSyst_EHM](https://github.com/mdredwanahmad/FST_CropSyst_EHM) - This project is for a unified energy balance model to estimate fruit surface temperature and track changes in agricultural water demand for extreme heat management. `no licence`
- [mpngo/pistachio_nut_growth_model](https://github.com/mpngo/pistachio_nut_growth_model) - Nut growth prediction model using Growing Degree Days for Pistachio using real-time weather data. `no licence`
- [openalea-incubator/VirtualBerry](https://github.com/openalea-incubator/VirtualBerry) - Virtual Berry: grapevine berry growth and development model. `no licence`

<a id="fruit-vine-ruby"></a>

#### Ruby

- [alexanderjsingleton/logarithmic-orchard](https://github.com/alexanderjsingleton/logarithmic-orchard) - A Ruby forecasting model simulating annual orange orchard yield from creation to maturity. `★ 1` `no licence`

<a id="fruit-vine-shell"></a>

#### Shell

- [noshita/GrapevineXL](https://github.com/noshita/GrapevineXL) - Functional-structural grapevine model. `★ 1` `no licence`

<a id="fruit-vine-other"></a>

#### Other

- [CampillayLLanos/Spatio-Temporal-Cherry-Phenology](https://github.com/CampillayLLanos/Spatio-Temporal-Cherry-Phenology) - Spatio-temporal bioclimatic modelling and validation of sweet cherry phenology under humid temperate climate conditions. `no licence`
- [Jerome-openclassroom/LimonTree_NPP_Model](https://github.com/Jerome-openclassroom/LimonTree_NPP_Model) - Open-source demonstration of water monitoring and Net Primary Production (NPP) modeling for a potted lemon tree, using low-cost sensors and cross-validated methods (equation-based photosynthetic… `no licence`

<a id="plantation"></a>

### Oil palm, coffee, cocoa and other plantation crops

<a id="plantation-cplusplus"></a>

#### C++

- [GBeurier/XPalm](https://github.com/GBeurier/XPalm) - Palm tree simulation model. `★ 2` `no licence`

<a id="plantation-fortran"></a>

#### Fortran

- [wendylovetc/ORCHIDEE-MICT-OP-r6850](https://github.com/wendylovetc/ORCHIDEE-MICT-OP-r6850) - Folk ORCHIDEE-MICT-OP-r6850 model from https://forge.ipsl.jussieu.fr/orchidee/browser/branches/publications/ORCHIDEE-MICT-OP-r6850?order=name. `★ 2` `no licence`
- [i-Ecoclimatology-lab/clm-palm-dev](https://github.com/i-Ecoclimatology-lab/clm-palm-dev) - Development of CLM-Palm, an oil palm version of the Community Land Model. `custom licence`
- [model-library-pps/CASE2_archive](https://github.com/model-library-pps/CASE2_archive) - CASE2 (Cacao Simulation Engine): FSE model of cacao growth and yield driven by daily weather. `custom licence`

<a id="plantation-fst"></a>

#### FST

- [model-library-pps/LINTUL_banana_archive](https://github.com/model-library-pps/LINTUL_banana_archive) - Archived LINTUL implementation for banana growth. `custom licence`

<a id="plantation-julia"></a>

#### Julia

- [cbsteh/Sawit.jl](https://github.com/cbsteh/Sawit.jl) - Oil palm growth and yield model for Malaysian growing conditions. `★ 7` `MIT`
- [PalmStudio/XPalm.jl](https://github.com/PalmStudio/XPalm.jl) - Oil-palm growth and yield simulations linking development and resource use. `★ 7` `MIT`
- [VEZY/DynACof.jl](https://github.com/VEZY/DynACof.jl) - The Dynamic Agroforestry Coffee Crop Model in Julia. `★ 5` `custom licence`
- [PalmStudio/VPalm.jl](https://github.com/PalmStudio/VPalm.jl) - Automata for building 3d mock-ups of oil palm. `★ 1` `MIT` `archived`

<a id="plantation-netlogo"></a>

#### NetLogo

- [lrcomolli/ABM-of-Inter-Species-Interactions-in-Agroforestry](https://github.com/lrcomolli/ABM-of-Inter-Species-Interactions-in-Agroforestry) - Our ABM model is a comprehensive simulation of an integrated multispecies agroforestry system for yerba mate (Ilex paraguariensis) cultivation in conjunction with nine consociated tree species. This… `GPL-3.0`

<a id="plantation-python"></a>

#### Python

- [cbsteh/PySawit](https://github.com/cbsteh/PySawit) - Oil Palm Growth and Yield Model. `★ 27` `MIT` `archived`
- [cbsteh/PySawit-Web](https://github.com/cbsteh/PySawit-Web) - Web-based Oil Palm Growth and Yield Model. `custom licence`
- [jirawatd/pysawit-thaioilpalm](https://github.com/jirawatd/pysawit-thaioilpalm) - Oil Palm Growth and Yield Model in part of the thaioilpalm project for smart solution which refer PySawit Model by Christopher Teh Boon Sung. `no licence`
- [model-library-pps/PALMSIM](https://github.com/model-library-pps/PALMSIM) - Oil-palm growth model maintained in the PPS model library. `custom licence`
- [model-library-pps/PALMSIM_archive](https://github.com/model-library-pps/PALMSIM_archive) - Archived PALMSIM: potential growth model of oil palm. `custom licence`

<a id="plantation-r"></a>

#### R

- [VEZY/DynACof](https://github.com/VEZY/DynACof) - The Dynamic Agroforestry Coffee Crop Model. `★ 7` `GPL-3.0`
- [MarcelVanOijen/CAF2014](https://github.com/MarcelVanOijen/CAF2014) - CAF2014: a process-based model for coffee agroforestry systems. `★ 1` `no licence`
- [PalmStudio/biomech](https://github.com/PalmStudio/biomech) - Biomechanical deformation model (torsion + bending). `MIT`
- [PalmStudio/VPalm_IDE](https://github.com/PalmStudio/VPalm_IDE) - A shiny application to compute virtual palm scenes from architectural data. `GPL-3.0`
- [PalmStudio/Vpalmr](https://github.com/PalmStudio/Vpalmr) - VPALMr is an R package to build palm tree mockups from field data. `GPL-3.0`

<a id="plantation-visual-basic"></a>

#### Visual Basic

- [Huichi17/Oil-Palm-Growth-Stage-and-Evapotranspiration](https://github.com/Huichi17/Oil-Palm-Growth-Stage-and-Evapotranspiration) - Oil palm growth stages and evapotranspiration (Penman–Monteith, Priestley–Taylor). `★ 1` `no licence`

<a id="plantation-other"></a>

#### Other

- [cpohagwu/py-simba-pop-docs](https://github.com/cpohagwu/py-simba-pop-docs) - A transparent, reproducible Python implementation of the SIMBA-POP banana cohort model. `Apache-2.0`
- [yfa008/clm-palm-dev](https://github.com/yfa008/clm-palm-dev) - Development of CLM-Palm model (Yuanchao Fan, Tsinghua University, China / University of Goettingen, Germany). `no licence`

<a id="grassland"></a>

### Grassland, pasture and forage

<a id="grassland-c"></a>

#### C

- [EcoSimZL/biome-bgc-muso_6.1_src_TP_wintergrazing](https://github.com/EcoSimZL/biome-bgc-muso_6.1_src_TP_wintergrazing) - This project includes modifications to the original Biome-BGCMuSo model (version 6.1) to enable simulation of the unique winter grazing processes on the Qinghai-Tibetan Plateau (QTP). `no licence`

<a id="grassland-cplusplus"></a>

#### C++

- [BioDT/uc-grassland-model](https://github.com/BioDT/uc-grassland-model) - grassland simulation model source code. `★ 3` `EUPL-1.2`
- [hugohu789-droid/Paddock](https://github.com/hugohu789-droid/Paddock) - Spatial NZ pastoral farm simulation in C++17 — pasture, soil water, grazing, livestock and irrigation on real geospatial data, with scenario comparison, explainable decisions and sourced validation.… `custom licence`

<a id="grassland-fortran"></a>

#### Fortran

- [GCEL/DALEC-Grass](https://github.com/GCEL/DALEC-Grass) - DALEC-Grass : A biogeochemical model of carbon dynamics in managed grassland ecosystems. `★ 6` `GPL-3.0`
- [bluegreen-labs/phenograss-example](https://github.com/bluegreen-labs/phenograss-example) - Grassland model example, recreating Figure 1 from my Nature Climate Change paper. `★ 2` `AGPL-3.0`
- [model-library-pps/LINGRA-N_archive](https://github.com/model-library-pps/LINGRA-N_archive) - LINGRA-N: simple grass growth model for potential, water-limited and nitrogen-limited yields. `custom licence`
- [model-library-pps/LINGRA_archive](https://github.com/model-library-pps/LINGRA_archive) - Archived grass growth model from the PPS model library. `no licence`

<a id="grassland-javascript"></a>

#### JavaScript

- [hoyeungw/pasture](https://github.com/hoyeungw/pasture) - A pasture growth model. `no licence`
- [jframirez161/BASGRA](https://github.com/jframirez161/BASGRA) - Web implementation of the BASGRA grass growth model. `no licence`

<a id="grassland-julia"></a>

#### Julia

- [FelixNoessler/GrasslandTraitSim.jl](https://github.com/FelixNoessler/GrasslandTraitSim.jl) - Simulation model of the biomass of grassland plant species. `★ 4` `GPL-3.0`
- [FelixNoessler/RegionalGrasslandSim.jl](https://github.com/FelixNoessler/RegionalGrasslandSim.jl) - Simulation model of the biomass of grassland plant species. `★ 1` `GPL-3.0`

<a id="grassland-ncl"></a>

#### NCL

- [gabriel-abrahao/modelo_lue_past_v7_oliveira](https://github.com/gabriel-abrahao/modelo_lue_past_v7_oliveira) - A simple LUE pasture model. `★ 1` `no licence`

<a id="grassland-python"></a>

#### Python

- [openalea-incubator/lgrass](https://github.com/openalea-incubator/lgrass) - A 3D Functionnal Structural Plant Model of perennial grasses morphogenesis and phenology. `★ 12` `custom licence`
- [natcap/rangeland_production](https://github.com/natcap/rangeland_production) - Rangeland Production Model built on raster-based Python implementation of Century. `★ 8` `custom licence`
- [YannChemin/modvege](https://github.com/YannChemin/modvege) - ModVege pasture model in Python (Jouven et al. 2006). `★ 5` `Unlicense`
- [openalea-incubator/l-egume](https://github.com/openalea-incubator/l-egume) - L-egume is an individual-based model for the simulation of population dynamics in herbaceous legume species. It is part of the Virtual GrassLand model (VGL) developed on the OpenAlea platfom. `★ 2` `custom licence`
- [Komanawa/komanawa-basgra-nz-py](https://github.com/Komanawa/komanawa-basgra-nz-py) - BASGRA or The BASic GRAssland model is a simple pasture growth model. This version, BASGRA_NZ has been specifically modified to model perennial ryegrass in New Zealand. This adaptation creates a… `★ 1` `LGPL-3.0`
- [YannChemin/LINGRA_RS](https://github.com/YannChemin/LINGRA_RS) - LINGRA grass growth and production model translated in Python and bypassed by RS data. `★ 1` `Unlicense`
- [ksaurabh95/Grass_growth_model](https://github.com/ksaurabh95/Grass_growth_model) - Simple grass growth model in Python. `CC0-1.0`
- [RegenAI-Backup/pasture_growth_potential](https://github.com/RegenAI-Backup/pasture_growth_potential) - Streamlit app for growth potential of perennials based on temperature. `MIT`
- [sdtaylor/GrasslandModels](https://github.com/sdtaylor/GrasslandModels) - Python implementations of grassland productivity and phenology models. `MIT`
- [subhashlorajat/pasture-grazing-simulation](https://github.com/subhashlorajat/pasture-grazing-simulation) - ODE simulation of Irish pasture growth and cattle grazing, calibrated to Teagasc data - identifies optimal stocking rate, turnout timing and grazing season length. `no licence`
- [vakowal/rangeland_production_11_26_18](https://github.com/vakowal/rangeland_production_11_26_18) - Beta rangeland production model using point-based version of Century. `custom licence`
- [vandoirb/ggrowtools](https://github.com/vandoirb/ggrowtools) - Grass Growth Model for urban management. `MIT`

<a id="grassland-r"></a>

#### R

- [davcam/BASGRA](https://github.com/davcam/BASGRA) - The BASic GRAssland model. `★ 6` `no licence`
- [kuadrat/growR](https://github.com/kuadrat/growR) - R implementation of the grassland model ModVege. `★ 4` `custom licence`
- [MarcelVanOijen/BASGRA_N](https://github.com/MarcelVanOijen/BASGRA_N) - A version of the BASic GRAssland model (BASGRA) that includes simulation of the N-cycle and digestibility. `★ 4` `GPL-3.0`
- [Jinyan-Yang/empirical_grassland_pheno_model](https://github.com/Jinyan-Yang/empirical_grassland_pheno_model) - Fits the Choler–Hufkens grassland phenology model to observed vegetation cover. `★ 3` `no licence`
- [lucabutikofer/LingraNR](https://github.com/lucabutikofer/LingraNR) - R Interface to LINGRA-N Tool. `★ 2` `custom licence`
- [woodwards/basgra_nz](https://github.com/woodwards/basgra_nz) - Adaptation of BASGRA pasture model to modelling perennial ryegrass in New Zealand. `★ 2` `MIT`
- [griffithdan/grass3PG](https://github.com/griffithdan/grass3PG) - A modification of r3PG specifically for modeling grass growth. `★ 1` `no licence`
- [AdrianBerzal97/Mediterranean-grassland-climate-model](https://github.com/AdrianBerzal97/Mediterranean-grassland-climate-model) - Ecohydrological modelling of Mediterranean grassland biomass under CMIP6 climate change scenarios. `no licence`
- [akpost21/fall_pheno_grassland](https://github.com/akpost21/fall_pheno_grassland) - modeling fall (autumn) phenology in grasslands. `MIT`
- [akpost21/Spring_pheno_grassland](https://github.com/akpost21/Spring_pheno_grassland) - Modeling spring phenology in grasslands. `no licence`
- [CodyGruber/CG-ForageMass-App](https://github.com/CodyGruber/CG-ForageMass-App) - app for documenting forage mass changes and expected changes due to growing degree days. `no licence`

<a id="grassland-other"></a>

#### Other

- [santiagoutsumi/SmartGrassIntake](https://github.com/santiagoutsumi/SmartGrassIntake) - Applied Grazing Management Model (AGMM) to assess herbage mass depletion rate and effects on grass intake and grazing behavior of dairy cattle. `no licence`

<a id="bioenergy-other"></a>

### Bioenergy and other crops

<a id="bioenergy-other-cplusplus"></a>

#### C++

- [Matthews-Research-Group/BioCroWP](https://github.com/Matthews-Research-Group/BioCroWP) - BioCro module library from the Matthews Research Group. `custom licence`
- [Matthews-Research-Group/MiscanthusBML](https://github.com/Matthews-Research-Group/MiscanthusBML) - BioCro module library with partitioning and senescence modules for miscanthus. `custom licence`

<a id="bioenergy-other-fortran"></a>

#### Fortran

- [DSSAT/TreeGro_legacy](https://github.com/DSSAT/TreeGro_legacy) - Legacy (2012) Fortran code of TreeGro, a 2D tree growth model built on DSSAT-CSM components. `BSD-3-Clause`

<a id="bioenergy-other-python"></a>

#### Python

- [uwkimlab/Poplar.jl](https://github.com/uwkimlab/Poplar.jl) - A process-based model of Poplar growth. `★ 4` `MIT`
- [evasinha-pnnl/Sinha-etal-2022-JAMES](https://github.com/evasinha-pnnl/Sinha-etal-2022-JAMES) - Modeling perennial bioenergy crops in the E3SM land model (ELMv2). `BSD-2-Clause`
- [Miscanthus-Germination/Miscanthus-model](https://github.com/Miscanthus-Germination/Miscanthus-model) - A model for Miscanthus germination and early growth, based on the SimPlE model (SIMulated Plant Emergense) (C. Dürr et al., 2001, & 2003). `MIT`

<a id="bioenergy-other-r"></a>

#### R

- [BrzostekEcologyLab/FUN-BioCROP](https://github.com/BrzostekEcologyLab/FUN-BioCROP) - Bioenergy model of plant C spent on N acquistion and SOM cycling. `★ 3` `BSD-3-Clause`
- [Miscanthus-Germination/Model_with_Interface](https://github.com/Miscanthus-Germination/Model_with_Interface) - A model for Miscanthus germination and early growth with a R Shiny Web interface. Based on the SimPlE model (SIMulated Plant Emergense) (C. Dürr et al., 2001, & 2003). `MIT`
- [yufenghe22/Miscanthus_R_version](https://github.com/yufenghe22/Miscanthus_R_version) - Minimal setup for running a miscanthus version of BioCro. `no licence`

## Contributing

Contributions are welcome! Read the [contribution guidelines](CONTRIBUTING.md) first. To add a repository, give it a type and a crop or process in `config/seeds.json`. Unclassified search results wait in the [review queue](docs/discovered.md).

## How this list is built

A dependency-free Python collector searches GitHub with 525 queries (model names, process terms, crops, several languages and topics), enumerates the accounts of model maintainers, and refreshes metadata of known repositories. A scheduled workflow runs it daily at 03:17 UTC and commits only data, health records and generated pages. Search results are only candidates; a repository is listed only by a recorded decision in `config/seeds.json`.

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
