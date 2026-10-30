# Process models

Process-based models of soil, water, climate, pests and other agricultural processes that are not specific to one crop. Crop models are listed in the [main tree](../README.md).

**1,675 repositories**, arranged by process, then programming language. Back to [Awesome Crop Models](../README.md).

## Contents

- [Phenology and development](#phenology) (82)
  - [C#](#phenology-csharp) (1)
  - [C++](#phenology-cplusplus) (1)
  - [Clojure](#phenology-clojure) (1)
  - [Go](#phenology-go) (1)
  - [Java](#phenology-java) (1)
  - [JavaScript](#phenology-javascript) (11)
  - [Python](#phenology-python) (29)
  - [R](#phenology-r) (28)
  - [Stan](#phenology-stan) (1)
  - [Svelte](#phenology-svelte) (1)
  - [TypeScript](#phenology-typescript) (2)
  - [Other](#phenology-other) (5)
- [Photosynthesis, canopy and transpiration](#photosynthesis) (156)
  - [C](#photosynthesis-c) (1)
  - [C#](#photosynthesis-csharp) (2)
  - [C++](#photosynthesis-cplusplus) (7)
  - [Fortran](#photosynthesis-fortran) (2)
  - [GLSL](#photosynthesis-glsl) (1)
  - [JavaScript](#photosynthesis-javascript) (1)
  - [Julia](#photosynthesis-julia) (12)
  - [Mathematica](#photosynthesis-mathematica) (1)
  - [MATLAB](#photosynthesis-matlab) (29)
  - [Modelica](#photosynthesis-modelica) (1)
  - [OCaml](#photosynthesis-ocaml) (1)
  - [Python](#photosynthesis-python) (49)
  - [R](#photosynthesis-r) (41)
  - [TypeScript](#photosynthesis-typescript) (1)
  - [Other](#photosynthesis-other) (7)
- [Plant architecture and FSPM](#architecture) (25)
  - [C](#architecture-c) (1)
  - [C++](#architecture-cplusplus) (1)
  - [GLSL](#architecture-glsl) (1)
  - [Java](#architecture-java) (1)
  - [Julia](#architecture-julia) (1)
  - [Python](#architecture-python) (14)
  - [R](#architecture-r) (2)
  - [Other](#architecture-other) (4)
- [Roots and rhizosphere](#roots) (55)
  - [C++](#roots-cplusplus) (5)
  - [Fortran](#roots-fortran) (7)
  - [Groovy](#roots-groovy) (1)
  - [Julia](#roots-julia) (4)
  - [Mathematica](#roots-mathematica) (1)
  - [MATLAB](#roots-matlab) (7)
  - [Python](#roots-python) (23)
  - [R](#roots-r) (4)
  - [Other](#roots-other) (3)
- [Soil water and heat](#soil-water) (257)
  - [C](#soil-water-c) (5)
  - [C#](#soil-water-csharp) (3)
  - [C++](#soil-water-cplusplus) (3)
  - [D](#soil-water-d) (1)
  - [Dart](#soil-water-dart) (1)
  - [Fortran](#soil-water-fortran) (21)
  - [Go](#soil-water-go) (1)
  - [Java](#soil-water-java) (4)
  - [Julia](#soil-water-julia) (8)
  - [Mathematica](#soil-water-mathematica) (1)
  - [MATLAB](#soil-water-matlab) (23)
  - [Python](#soil-water-python) (134)
  - [R](#soil-water-r) (21)
  - [Rust](#soil-water-rust) (2)
  - [TypeScript](#soil-water-typescript) (5)
  - [Other](#soil-water-other) (24)
- [Soil carbon, nitrogen and nutrients](#soil-nutrients) (126)
  - [Assembly](#soil-nutrients-assembly) (1)
  - [C++](#soil-nutrients-cplusplus) (9)
  - [Fortran](#soil-nutrients-fortran) (14)
  - [FST](#soil-nutrients-fst) (1)
  - [JavaScript](#soil-nutrients-javascript) (4)
  - [MATLAB](#soil-nutrients-matlab) (4)
  - [Python](#soil-nutrients-python) (45)
  - [R](#soil-nutrients-r) (38)
  - [Other](#soil-nutrients-other) (10)
- [Agricultural greenhouse gases](#greenhouse-gases) (21)
  - [C](#greenhouse-gases-c) (1)
  - [C#](#greenhouse-gases-csharp) (1)
  - [Fortran](#greenhouse-gases-fortran) (1)
  - [GAML](#greenhouse-gases-gaml) (1)
  - [MATLAB](#greenhouse-gases-matlab) (1)
  - [Python](#greenhouse-gases-python) (4)
  - [R](#greenhouse-gases-r) (3)
  - [Other](#greenhouse-gases-other) (9)
- [Evapotranspiration and irrigation](#evapotranspiration) (478)
  - [AMPL](#evapotranspiration-ampl) (1)
  - [C](#evapotranspiration-c) (8)
  - [C#](#evapotranspiration-csharp) (3)
  - [C++](#evapotranspiration-cplusplus) (2)
  - [Clojure](#evapotranspiration-clojure) (1)
  - [Cuda](#evapotranspiration-cuda) (4)
  - [Dart](#evapotranspiration-dart) (1)
  - [Elixir](#evapotranspiration-elixir) (2)
  - [Fortran](#evapotranspiration-fortran) (5)
  - [Go](#evapotranspiration-go) (1)
  - [Go Template](#evapotranspiration-go-template) (1)
  - [Groovy](#evapotranspiration-groovy) (1)
  - [IDL](#evapotranspiration-idl) (4)
  - [Java](#evapotranspiration-java) (5)
  - [JavaScript](#evapotranspiration-javascript) (32)
  - [Julia](#evapotranspiration-julia) (4)
  - [MATLAB](#evapotranspiration-matlab) (14)
  - [OCaml](#evapotranspiration-ocaml) (1)
  - [Perl](#evapotranspiration-perl) (1)
  - [PHP](#evapotranspiration-php) (5)
  - [PLpgSQL](#evapotranspiration-plpgsql) (1)
  - [Python](#evapotranspiration-python) (276)
  - [R](#evapotranspiration-r) (55)
  - [Ruby](#evapotranspiration-ruby) (4)
  - [Rust](#evapotranspiration-rust) (4)
  - [Shell](#evapotranspiration-shell) (2)
  - [TypeScript](#evapotranspiration-typescript) (10)
  - [Visual Basic](#evapotranspiration-visual-basic) (3)
  - [Other](#evapotranspiration-other) (27)
- [Weather and agroclimate](#weather) (103)
  - [C](#weather-c) (1)
  - [C#](#weather-csharp) (2)
  - [C++](#weather-cplusplus) (3)
  - [Fortran](#weather-fortran) (8)
  - [Java](#weather-java) (4)
  - [JavaScript](#weather-javascript) (3)
  - [Julia](#weather-julia) (5)
  - [MATLAB](#weather-matlab) (4)
  - [Python](#weather-python) (41)
  - [R](#weather-r) (26)
  - [Rust](#weather-rust) (1)
  - [Other](#weather-other) (5)
- [Pests, diseases and weeds](#pests-diseases) (131)
  - [C#](#pests-diseases-csharp) (2)
  - [C++](#pests-diseases-cplusplus) (3)
  - [Fortran](#pests-diseases-fortran) (2)
  - [GAML](#pests-diseases-gaml) (1)
  - [JavaScript](#pests-diseases-javascript) (4)
  - [Julia](#pests-diseases-julia) (4)
  - [Mathematica](#pests-diseases-mathematica) (1)
  - [MATLAB](#pests-diseases-matlab) (6)
  - [NetLogo](#pests-diseases-netlogo) (1)
  - [Objective-C](#pests-diseases-objective-c) (1)
  - [Python](#pests-diseases-python) (48)
  - [R](#pests-diseases-r) (46)
  - [Shell](#pests-diseases-shell) (1)
  - [TypeScript](#pests-diseases-typescript) (1)
  - [Wolfram Language](#pests-diseases-wolfram-language) (2)
  - [Other](#pests-diseases-other) (8)
- [Hydrology, erosion and watersheds](#hydrology) (153)
  - [C](#hydrology-c) (6)
  - [C#](#hydrology-csharp) (1)
  - [C++](#hydrology-cplusplus) (4)
  - [Fortran](#hydrology-fortran) (51)
  - [JavaScript](#hydrology-javascript) (2)
  - [Mathematica](#hydrology-mathematica) (1)
  - [MATLAB](#hydrology-matlab) (3)
  - [NetLogo](#hydrology-netlogo) (1)
  - [Perl](#hydrology-perl) (1)
  - [Python](#hydrology-python) (52)
  - [R](#hydrology-r) (9)
  - [Reason](#hydrology-reason) (1)
  - [Rust](#hydrology-rust) (2)
  - [Shell](#hydrology-shell) (2)
  - [Visual Basic](#hydrology-visual-basic) (1)
  - [Other](#hydrology-other) (16)
- [Land surface and global vegetation](#land-surface) (25)
  - [C](#land-surface-c) (7)
  - [C++](#land-surface-cplusplus) (1)
  - [Fortran](#land-surface-fortran) (10)
  - [Julia](#land-surface-julia) (1)
  - [Python](#land-surface-python) (4)
  - [R](#land-surface-r) (1)
  - [Other](#land-surface-other) (1)
- [Greenhouses and controlled environments](#controlled-environment) (63)
  - [C](#controlled-environment-c) (1)
  - [C#](#controlled-environment-csharp) (1)
  - [C++](#controlled-environment-cplusplus) (1)
  - [Fortran](#controlled-environment-fortran) (1)
  - [Julia](#controlled-environment-julia) (1)
  - [MATLAB](#controlled-environment-matlab) (7)
  - [Modelica](#controlled-environment-modelica) (2)
  - [Python](#controlled-environment-python) (39)
  - [R](#controlled-environment-r) (1)
  - [Shell](#controlled-environment-shell) (1)
  - [TypeScript](#controlled-environment-typescript) (2)
  - [Other](#controlled-environment-other) (6)

## Process models

<a id="phenology"></a>

### Phenology and development

<a id="phenology-csharp"></a>

#### C#

- [SiriusQuality/SiriusQuality-BioMa-Phenology-Component](https://github.com/SiriusQuality/SiriusQuality-BioMa-Phenology-Component) - BioMa component of Phenology in Sirius Quality. `★ 1` `MIT`

<a id="phenology-cplusplus"></a>

#### C++

- [eloch216/oscillator-based-circadian-clock-analysis](https://github.com/eloch216/oscillator-based-circadian-clock-analysis) - Data and analysis scripts for "Integrating oscillator-based circadian clocks with crop growth simulations". `★ 1` `CC0-1.0`

<a id="phenology-clojure"></a>

#### Clojure

- [briprowe/gdd-service](https://github.com/briprowe/gdd-service) - An API to return Growing Degree Days. `no licence`

<a id="phenology-go"></a>

#### Go

- [edizyurdakul/gdd-cli](https://github.com/edizyurdakul/gdd-cli) - No description provided. `MIT`

<a id="phenology-java"></a>

#### Java

- [MemoryDust/GrowingDegreeDay](https://github.com/MemoryDust/GrowingDegreeDay) - No description provided. `no licence`

<a id="phenology-javascript"></a>

#### JavaScript

- [ChartKillers/CropTracker](https://github.com/ChartKillers/CropTracker) - Track the growing degree days of your crop. `★ 3` `MIT`
- [Ivykimathi/GrowingDegreeDays](https://github.com/Ivykimathi/GrowingDegreeDays) - No description provided. `★ 1` `no licence`
- [aasmith/gdd](https://github.com/aasmith/gdd) - Garden Planner using Growing Degree Days. `no licence`
- [BenHTC/gdd-tracker](https://github.com/BenHTC/gdd-tracker) - Receive daily emails from user selected, Colorado based monitoring stations about accumulated growing degree days. `no licence`
- [cueas-rickmoore/cicss-gddtool](https://github.com/cueas-rickmoore/cicss-gddtool) - Growing degree day calculator and comparison to historical records. `custom licence`
- [luisangelbg/PhenologyPro](https://github.com/luisangelbg/PhenologyPro) - Agroclimatología y fenología de cultivos en el navegador: grados-día, ETo FAO-56, balance hídrico, riego, etapas BBCH, frío invernal, climogramas y riesgos. Agroclimatology and crop phenology in the… `GPL-3.0`
- [Nate-Nutrition-Agronomy/Climate-Dashboard](https://github.com/Nate-Nutrition-Agronomy/Climate-Dashboard) - Dashboard showing chill portion accumulation/growing degree days and temperature/precipitation data for horticultural crops through South Australia and Sunraysia, Victoria. `no licence`
- [nrcc-cornell/csf-gddtool](https://github.com/nrcc-cornell/csf-gddtool) - Cornell CSF Growing degree day calculator (2018). `GPL-3.0`
- [nrcc-cornell/csf-gddtool-v3](https://github.com/nrcc-cornell/csf-gddtool-v3) - Cornell CSF Growing degree day calculator V3. `GPL-3.0`
- [nrcc-cornell/csf-gddtool-v4](https://github.com/nrcc-cornell/csf-gddtool-v4) - Cornell CSF Growing degree day calculator V4 (uses ACIS). `no licence`
- [Xanderewa/AgroGerm-H-T](https://github.com/Xanderewa/AgroGerm-H-T) - Simulador hidrotérmico de germinación para enseñanza agronómica. Herramienta didáctica que conecta el modelo científico con datos reales de Paraguay. Funciona offline. 46 cultivares · 13 especies ·… `custom licence`

<a id="phenology-python"></a>

#### Python

- [sdtaylor/pyPhenology](https://github.com/sdtaylor/pyPhenology) - Plant phenology models in python with a scikit-learn inspired API. `★ 36` `MIT`
- [phenology/springtime](https://github.com/phenology/springtime) - Spatiotemporal phenology research with interpretable models. `★ 4` `Apache-2.0`
- [SongWon03/PhenoFECT](https://github.com/SongWon03/PhenoFECT) - A Python package for Phenology Forecasting and Examining for plants under ClimaTe change (PhenoFECT). `★ 3` `MIT`
- [datatribe-collective-labs/gdd-app](https://github.com/datatribe-collective-labs/gdd-app) - Web application for estimating plant growth by calculating Growing Degree Days (GDD) from weather data. `★ 2` `MIT`
- [wateas/GDD_calculator](https://github.com/wateas/GDD_calculator) - Calculate Growing Degree Days from weather history data available from NOAA. `★ 2` `GPL-3.0`
- [Ciampitti-Lab/WheatPhenologyHRW](https://github.com/Ciampitti-Lab/WheatPhenologyHRW) - Field-scale winter-wheat phenology across the U.S. HRW belt: physiology-informed (WES) with machine learning. `★ 1` `MIT`
- [elimelecmunoz/sath](https://github.com/elimelecmunoz/sath) - SATH: Sistema Avanzado de Análisis Térmico para Agricultura — predicción de fechas óptimas de cosecha mediante GDD y machine learning. `★ 1` `MIT`
- [Muhammad1599/Wheat_Pheno_G-cover-estimator](https://github.com/Muhammad1599/Wheat_Pheno_G-cover-estimator) - No description provided. `★ 1` `no licence`
- [yoocha1/GDD](https://github.com/yoocha1/GDD) - Python Web App Calculating the Growing Degree Days of Plants. `★ 1` `no licence`
- [adelejmz/Agro-Climate-Analysis](https://github.com/adelejmz/Agro-Climate-Analysis) - A Python-based toolkit for agricultural climate analysis. Specifically focused on calculating Growing Degree Days (GDD) and visualizing monthly air temperature trends from raw weather station data. `MIT`
- [byron-evers/Thermal-Time-Indices](https://github.com/byron-evers/Thermal-Time-Indices) - No description provided. `no licence`
- [ChenyaoYang123/PyPhenoModels](https://github.com/ChenyaoYang123/PyPhenoModels) - This is a repository for the development of an ensemble of different phenology models that are widely used in the field of viticulture research. Implementation of these models will be performed in… `MIT`
- [choco-chip-melon/growing_degree_days](https://github.com/choco-chip-melon/growing_degree_days) - オープン気象データ Open-Meteo からその地域の平均気温を取得し、野菜に応じた有効積算温度（Growing Degree Days: GDD）を計算して収穫時期を判定するPythonプログラム. `no licence`
- [cropbox/rda](https://github.com/cropbox/rda) - Phenology models from the RDA (Korea) phenology modelling project. `no licence`
- [EcoInfoLab/PTU](https://github.com/EcoInfoLab/PTU) - No description provided. `no licence`
- [EthanSeok/Korean_wheat_phenology](https://github.com/EthanSeok/Korean_wheat_phenology) - 국산 밀 품종의 생물계절 모델링 (APSIM Phenology Module). `no licence`
- [jafernandez01/TT-pipeline](https://github.com/jafernandez01/TT-pipeline) - Pipeline for calculating HTT (Hourly Thermal Time) and DTT (Daily Thermal Time) using Mesonet database in python. `no licence`
- [krupali4655/Crop-Weather-Calendar-and-Phenology-Prediction-Using-Heat-Indices](https://github.com/krupali4655/Crop-Weather-Calendar-and-Phenology-Prediction-Using-Heat-Indices) - No description provided. `MIT`
- [larscaspersen/phenoflex_meets_bayes](https://github.com/larscaspersen/phenoflex_meets_bayes) - No description provided. `MIT`
- [m-udby/GDD_Calc](https://github.com/m-udby/GDD_Calc) - Growing Degree Days calculator for Nebraska State Climate Office. `GPL-3.0`
- [meijian-yang/fast-crop-stage-cycle](https://github.com/meijian-yang/fast-crop-stage-cycle) - Fast (numba) re-implementations of the NASA Harvest / Agmatix crop cycle and crop stage models, plus a gridded 30 m / 1 km / 9 km mapping pipeline. `Apache-2.0`
- [NIDHICHAUDHARY26/Phenology-prediction-using-Heat-indices-and-crop-weather-calender.](https://github.com/NIDHICHAUDHARY26/Phenology-prediction-using-Heat-indices-and-crop-weather-calender.) - No description provided. `no licence`
- [pallavisingh150-bit/GDD_Calculator](https://github.com/pallavisingh150-bit/GDD_Calculator) - It helps to calculate GDD for various crops and the thermal time between various stages. It can also support multiple experiments. `no licence`
- [sandeeppvn/Numerical-Optimization-for-Wheat-crop-Phenology-Estimation](https://github.com/sandeeppvn/Numerical-Optimization-for-Wheat-crop-Phenology-Estimation) - No description provided. `no licence`
- [sunqling91/GSI](https://github.com/sunqling91/GSI) - This project implements seasonal phenology date simulations based on the growing season index (GSI) models. It provides a comprehensive framework for calculating the phenological dates of spring and… `no licence`
- [todddole/Growing-Degree-Days](https://github.com/todddole/Growing-Degree-Days) - No description provided. `no licence`
- [Unmolsharma/Crop-Phenology-prediction](https://github.com/Unmolsharma/Crop-Phenology-prediction) - No description provided. `no licence`
- [uor25/GDD_calculator_and_Drying_Algorithm](https://github.com/uor25/GDD_calculator_and_Drying_Algorithm) - Interactive Growing Degree Day (GDD) Calculator & Crop Drying Predictor with real-time weather API data and dynamic Plotly visualizations. `no licence`
- [uranchung/SimpleCalcGDD-Kor](https://github.com/uranchung/SimpleCalcGDD-Kor) - test Calculation Growing Degree Days (Korean version). `no licence`

<a id="phenology-r"></a>

#### R

- [bluegreen-labs/phenor](https://github.com/bluegreen-labs/phenor) - A phenology modelling framework in R. `★ 51` `custom licence`
- [AgMIP-GGCMI/cropCalendars](https://github.com/AgMIP-GGCMI/cropCalendars) - R-package for simulating climate-driven crop calendars. `★ 16` `AGPL-3.0`
- [EduardoFernandezC/dormancyR](https://github.com/EduardoFernandezC/dormancyR) - Alternative chill models and functions to handle or download weather data. `★ 7` `no licence`
- [agronomy4future/gdds](https://github.com/agronomy4future/gdds) - Calculation for Growing Degree Days (GDDs, ºC d). `★ 5` `custom licence`
- [Carm1r/fruclimadapt](https://github.com/Carm1r/fruclimadapt) - Evaluation tools for assessing climate adaptation of fruit tree species. `★ 5` `no licence`
- [cran/cropgrowdays](https://github.com/cran/cropgrowdays) - :exclamation: This is a read-only mirror of the CRAN R package repository. cropgrowdays — Crop Growing Degree Days and Agrometeorological Calculations. Homepage… `★ 3` `custom licence`
- [UCANR-IGIS/degday](https://github.com/UCANR-IGIS/degday) - Compute degree days from daily min and max temperatures to model growth of plants and animals. `★ 3` `GPL-3.0`
- [efernandezpascual/seedr](https://github.com/efernandezpascual/seedr) - seedr: Hydro and Thermal Time Seed Germination Models in R. `★ 2` `GPL-3.0`
- [cran/phenolocrop](https://github.com/cran/phenolocrop) - :exclamation: This is a read-only mirror of the CRAN R package repository. phenolocrop — Time-Series Models to the Crop Phenology. `★ 1` `no licence`
- [douglask3/PhenologyModels](https://github.com/douglask3/PhenologyModels) - No description provided. `★ 1` `GPL-2.0`
- [ftschurr/DyMEP](https://github.com/ftschurr/DyMEP) - No description provided. `★ 1` `LGPL-3.0`
- [larscaspersen/addition_chillR](https://github.com/larscaspersen/addition_chillR) - Functions which can be added to chillR. `★ 1` `no licence`
- [ledtrip/GDD](https://github.com/ledtrip/GDD) - Growing Degree Day Calculations. `★ 1` `no licence`
- [MR-Eini/ThermoPheno](https://github.com/MR-Eini/ThermoPheno) - ThermoPheno. `★ 1` `custom licence`
- [bbarker505/ddrp_plants](https://github.com/bbarker505/ddrp_plants) - A version of DDRP designed for modeling plants. The platform can use daily soil moisture data in the degree-day and climatic suitaiblity model. `no licence`
- [jbmchls/wthr_app](https://github.com/jbmchls/wthr_app) - This web application retrieves air temp and precipitation from NOAA, calculates growing degree days, and charts both precipitation and GDD over the selected time range. Dates for emergence… `no licence`
- [John-Kean/phenologysim](https://github.com/John-Kean/phenologysim) - R library for phenology simulation modelling. `no licence`
- [larscaspersen/eval_phenoflex](https://github.com/larscaspersen/eval_phenoflex) - Construct and calibrate phenology models. `GPL-3.0`
- [larscaspersen/pheno-population](https://github.com/larscaspersen/pheno-population) - Allows for bud-population level prediction of phenology. `GPL-3.0`
- [mcrimmins/gdd-plotter](https://github.com/mcrimmins/gdd-plotter) - Shiny App that interactively plots local cumulative growing degree day curves. `no licence`
- [mcrimmins/nature-cast-prototype](https://github.com/mcrimmins/nature-cast-prototype) - Prototype Shiny App to track/forecast phenological events using growing degree days. `no licence`
- [MrJGao/pspm](https://github.com/MrJGao/pspm) - Process-based spring phenology models. `no licence`
- [pcoddo/weatherAPI](https://github.com/pcoddo/weatherAPI) - Downloads weather and calculates growing degree days (GDD) for Maryland counties. `GPL-3.0`
- [planttrt/phenoCDM](https://github.com/planttrt/phenoCDM) - Continuous development models for incremental time-series analysis: applications on leaf phenology. `AGPL-3.0`
- [RPertille/ChillModels](https://github.com/RPertille/ChillModels) - No description provided. `GPL-3.0`
- [russellkong/dissertation_model](https://github.com/russellkong/dissertation_model) - R code for crop phenology models developed for a dissertation. `no licence`
- [uace-azmet/chill-accumulation-calculator](https://github.com/uace-azmet/chill-accumulation-calculator) - Shiny app to calculate chill accumulation at AZMet stations and by date range. `no licence`
- [uace-azmet/heat-accumulation-calculator](https://github.com/uace-azmet/heat-accumulation-calculator) - Shiny app to calculate heat accumulation at AZMet stations and by date range during the growing season. `no licence`

<a id="phenology-stan"></a>

#### Stan

- [phenostan/phenostan](https://github.com/phenostan/phenostan) - Stan backend for phenology models. `phenosurvr` (R) and `phenosurv` (python) APIs use these models. `no licence`

<a id="phenology-svelte"></a>

#### Svelte

- [egiron/GDD](https://github.com/egiron/GDD) - Calculates thermal time/growing degree days (GDD). `no licence`

<a id="phenology-typescript"></a>

#### TypeScript

- [justin-schmitz-smsc/smsc-gdd-page](https://github.com/justin-schmitz-smsc/smsc-gdd-page) - Growing Degree Day Calculator Page. `no licence`
- [paige-millz/bulb-forecast-ai](https://github.com/paige-millz/bulb-forecast-ai) - Predictive modeling system for seasonal bulb removal timing using Growing Degree Days (GDD) and Easter date regression. `no licence`

<a id="phenology-other"></a>

#### Other

- [shilosh/emergence2heading](https://github.com/shilosh/emergence2heading) - Google Earth Engine code for a web app that can estimate the number of days from emergence to heading in wheat field based on growing degree days. `★ 1` `no licence`
- [anam16/R-workflow-ChillPLS](https://github.com/anam16/R-workflow-ChillPLS) - No description provided. `no licence`
- [CampillayLLanos/Biomathematical-Phenology-Climate-Adaptation](https://github.com/CampillayLLanos/Biomathematical-Phenology-Climate-Adaptation) - Biomathematical phenology models and technological tools for climate adaptation in the fruit and wine industries. `no licence`
- [CampillayLLanos/Mathematical-Crop-Phenology](https://github.com/CampillayLLanos/Mathematical-Crop-Phenology) - Mathematical framework for modelling crop phenology under climate change using differential equations, scientific computing, and predictive modelling. Integrates mathematics, biology, and… `no licence`
- [QwagPerson/ChillPy](https://github.com/QwagPerson/ChillPy) - Pure Python implementation based on the R package chillR, providing tools for temperate fruit tree phenology analysis, including chilling metrics, heat accumulation, hourly temperature… `no licence`

<a id="photosynthesis"></a>

### Photosynthesis, canopy and transpiration

<a id="photosynthesis-c"></a>

#### C

- [yongguangzhang/BEPS-SIF-model](https://github.com/yongguangzhang/BEPS-SIF-model) - BEPS-SIF is a global sun-induced chlorophyll fluorescence model which considers the multiple scattering effects within a canopy. `★ 23` `no licence`

<a id="photosynthesis-csharp"></a>

#### C#

- [QAAFI/DCaPST](https://github.com/QAAFI/DCaPST) - No description provided. `★ 9` `no licence`
- [QAAFI/DCaPS](https://github.com/QAAFI/DCaPS) - Diurnal Canopy Photosynthesis Simulator. `★ 3` `no licence`

<a id="photosynthesis-cplusplus"></a>

#### C++

- [USDA-ARS-ACSL/PhotoSynthesisModule](https://github.com/USDA-ARS-ACSL/PhotoSynthesisModule) - Leaf photosynthesis and transpiration coupling Farquhar and Ball-Berry models. `★ 12` `Unlicense`
- [ahornero/SILVO](https://github.com/ahornero/SILVO) - SILVO: a lightweight 3D ray-tracing model for vegetation canopy structure, light interception, gap fraction, and illumination. `★ 3` `AGPL-3.0`
- [openalea/spice](https://github.com/openalea/spice) - Photon mapping with python wrapper (Spectral Photon Interception in Controlled Environment). `★ 2` `custom licence`
- [ForestEcophys-OSU/garisom](https://github.com/ForestEcophys-OSU/garisom) - A git repository for the compiling code of the Stomatal Optimization Model developed by John Sperry. `★ 1` `no licence`
- [jrpleban/Beta_photosynthesis_model](https://github.com/jrpleban/Beta_photosynthesis_model) - No description provided. `no licence`
- [Matthews-Research-Group/BML-ePhotosynthesis](https://github.com/Matthews-Research-Group/BML-ePhotosynthesis) - No description provided. `custom licence`
- [traitecoevo/phylloptim](https://github.com/traitecoevo/phylloptim) - No description provided. `AGPL-3.0`

<a id="photosynthesis-fortran"></a>

#### Fortran

- [geco-bern/rsofun](https://github.com/geco-bern/rsofun) - Implements the Simulating Optimal FUNctioning framework for site-scale simulations of ecosystem processes, including model calibration. It contains Fortran 90 modules for the P-model, SPLASH, and… `★ 34` `GPL-3.0`
- [USDA-ARS-ACSL/2DLEAF](https://github.com/USDA-ARS-ACSL/2DLEAF) - This is an adaptation of 2DSOIL that was developed by Ludmilla Pachepsky to simulate gas transport and photosynthesis inside a leaf. `★ 1` `no licence`

<a id="photosynthesis-glsl"></a>

#### GLSL

- [openalea/PyRATP](https://github.com/openalea/PyRATP) - RATP: Radiation Absorption, Transpiration and Photosynthesis. `★ 5` `custom licence`

<a id="photosynthesis-javascript"></a>

#### JavaScript

- [AgronomyKiel/PhotoRad](https://github.com/AgronomyKiel/PhotoRad) - Some functions for photosynthesis and radiation transfer in crop canopies. `custom licence`

<a id="photosynthesis-julia"></a>

#### Julia

- [VEZY/PlantBiophysics.jl](https://github.com/VEZY/PlantBiophysics.jl) - Plant biophysical models for photosynthesis, conductance, and energy exchange. `★ 34` `MIT`
- [cropbox/LeafGasExchange.jl](https://github.com/cropbox/LeafGasExchange.jl) - 🍃 coupled leaf gas-exchange model. `★ 6` `MIT`
- [rafaqz/Photosynthesis.jl](https://github.com/rafaqz/Photosynthesis.jl) - A dedicated photosynthesis library in Julia. `★ 4` `custom licence`
- [Yujie-W/Photosynthesis.jl](https://github.com/Yujie-W/Photosynthesis.jl) - Photosynthesis models for C3 and C4 photosynthesis. `★ 3` `Apache-2.0`
- [VirtualPlantLab/Ecophys.jl](https://github.com/VirtualPlantLab/Ecophys.jl) - Repository for simple models of ecophysiological processes. `★ 2` `MIT`
- [Yujie-W/PlantHydraulics.jl](https://github.com/Yujie-W/PlantHydraulics.jl) - Plant hydraulics using numerical method. `★ 2` `Apache-2.0`
- [AleMorales/MultilayerCanopy.jl](https://github.com/AleMorales/MultilayerCanopy.jl) - Multilayer model of canopy photosynthesis. `★ 1` `MIT`
- [PeterFransson/CCPH.jl](https://github.com/PeterFransson/CCPH.jl) - Coupled canopy photosynthesis and hydraulics model. `★ 1` `MIT`
- [Yujie-W/CanopyRadiativeTransfer.jl](https://github.com/Yujie-W/CanopyRadiativeTransfer.jl) - Models for canopy radiative transfer schemes. `★ 1` `Apache-2.0`
- [fevalero19/In_silico_fspm](https://github.com/fevalero19/In_silico_fspm) - Work on FSPM leaf optical properties. `no licence`
- [VEZY/ArchimedLight.jl](https://github.com/VEZY/ArchimedLight.jl) - Radiation interception in discrete direction. `MIT`
- [wusunlab/Canopy.jl](https://github.com/wusunlab/Canopy.jl) - &#91;under construction&#93; A Julia package for biometeorology and biosphere--atmosphere interactions. `MIT`

<a id="photosynthesis-mathematica"></a>

#### Mathematica

- [wusunlab/FvCB-solutions](https://github.com/wusunlab/FvCB-solutions) - Analytical solutions of Farquhar--von Caemmerer--Berry (FvCB) photosynthetic assimilation model. `★ 1` `MIT`

<a id="photosynthesis-matlab"></a>

#### MATLAB

- [Christiaanvandertol/SCOPE](https://github.com/Christiaanvandertol/SCOPE) - SCOPE is a simulation model for radiative transfer, photosynthesis and energy fluxes in vegetation and soil. `★ 105` `custom licence`
- [jenjohnson/johnson-berry-2021-pres](https://github.com/jenjohnson/johnson-berry-2021-pres) - MATLAB code for photosynthesis model in Johnson and Berry (2021) Photosynthesis Research. `★ 7` `MIT`
- [zhangyaonju/Global_sensitivity_analysis_for_Farquhar](https://github.com/zhangyaonju/Global_sensitivity_analysis_for_Farquhar) - the global sensitivity analysis for Farquhar photosynthesis model, with Sellers 1992 et al. upscaling. `★ 7` `no licence`
- [jenjohnson/johnson-field-berry-2021-oeco](https://github.com/jenjohnson/johnson-field-berry-2021-oeco) - MATLAB code for C3, C3-C4, and C4 photosynthesis model in Johnson, Field, and Berry (2021) Oecologia. `★ 5` `MIT`
- [baldocchi/CanVeg](https://github.com/baldocchi/CanVeg) - CanVeg is a Matlab version of a 1 dimensional canopy model. `★ 4` `no licence`
- [yixiao2/eLeaf_rice](https://github.com/yixiao2/eLeaf_rice) - A 3D mechanistic model of leaf photosynthesis for rice. `★ 4` `GPL-3.0`
- [FusangLiu/C4-photosynthesis](https://github.com/FusangLiu/C4-photosynthesis) - No description provided. `★ 3` `no licence`
- [HydroComplexity/MLCan2.0](https://github.com/HydroComplexity/MLCan2.0) - Multi-Layer Canopy Root Soil Model version 2.0. `★ 3` `no licence`
- [Prikaziuk/FvCB_photosynthesis](https://github.com/Prikaziuk/FvCB_photosynthesis) - GUI for the C3 photosynthesis Farquhar, von Caemmerer & Berry model (1980). `★ 3` `GPL-3.0`
- [FusangLiu/example-of-calculation-canopy-photosynthesis](https://github.com/FusangLiu/example-of-calculation-canopy-photosynthesis) - No description provided. `★ 2` `no licence`
- [yuwangcn/C4_dynamic_model](https://github.com/yuwangcn/C4_dynamic_model) - No description provided. `★ 2` `Apache-2.0`
- [yuwangcn/Chld_Chlf_in_soybean](https://github.com/yuwangcn/Chld_Chlf_in_soybean) - No description provided. `★ 2` `no licence`
- [ecohydrologylab/vLeaf](https://github.com/ecohydrologylab/vLeaf) - This code is associated with our publication "Stomatal conductance reduction tradeoffs in maize leaves: A theoretical study". You can access the paper from DOI: https://doi.org/10.1111/pce.14821. `★ 1` `custom licence`
- [manishverma09/VPRM](https://github.com/manishverma09/VPRM) - Old code to estimate photosynthesis from a simple model. `★ 1` `no licence`
- [TESTgroup-BNL/Matlab-Canopy_Photosynthesis](https://github.com/TESTgroup-BNL/Matlab-Canopy_Photosynthesis) - Testbed for canopy scaling and modeling of Photosynthesis and GPP. `★ 1` `GPL-3.0` `archived`
- [yaoganchenchi/GMC-OPT](https://github.com/yaoganchenchi/GMC-OPT) - Global Multilayer Canopy OPTimization. `★ 1` `no licence`
- [zr-sunflower/RTAS-Model](https://github.com/zr-sunflower/RTAS-Model) - A Radiative Transfer Model for Agricultural Strip-Intercropping Structures. `★ 1` `no licence`
- [cropsinsilico/C3PhotosynthesisMetabolicModel](https://github.com/cropsinsilico/C3PhotosynthesisMetabolicModel) - No description provided. `GPL-3.0` `archived`
- [debsunder/SCOPE_V1.70_Revised](https://github.com/debsunder/SCOPE_V1.70_Revised) - Revised version of SCOPE model v1.70. `GPL-3.0`
- [ecohydrologylab/vCanopy](https://github.com/ecohydrologylab/vCanopy) - vCanopy is a process-based canopy-soil model developed to simulate crop photosynthesis, transpiration, and energy fluxes under varying environmental and physiological conditions. `custom licence`
- [githu8tan/1-2-n-leafCanopyPhotosynthesis](https://github.com/githu8tan/1-2-n-leafCanopyPhotosynthesis) - No description provided. `no licence`
- [liuerxie/adaptation-acclimation](https://github.com/liuerxie/adaptation-acclimation) - Code for the manuscript "Incorporating thermal adaptation and acclimation improves light-use efficiency modeling for estimating gross primary production in Tibetan Plateau grasslands". `no licence`
- [long-lab/Cassava_model](https://github.com/long-lab/Cassava_model) - No description provided. `no licence`
- [long-lab/Dynamic-photosynthesis-model-of-soybean-canopy](https://github.com/long-lab/Dynamic-photosynthesis-model-of-soybean-canopy) - No description provided. `no licence`
- [mdetto/Photosynthesis-Hydraulic-Model](https://github.com/mdetto/Photosynthesis-Hydraulic-Model) - No description provided. `no licence`
- [sabyasachi-sen/Isothermal-model-Non-stomatal-control-of-transpiration](https://github.com/sabyasachi-sen/Isothermal-model-Non-stomatal-control-of-transpiration) - This repository contains the dataset and analysis scripts used in the paper: "Loss of conductance between mesophyll symplasm and intercellular air spaces explains nonstomatal control of transpiration". `MIT`
- [sanozmen/matlabGEM](https://github.com/sanozmen/matlabGEM) - Photosynthesis models. `no licence`
- [SicongGao/FLUSPECT_RETRIEVE](https://github.com/SicongGao/FLUSPECT_RETRIEVE) - Retrieval of leaf biochemical parameters with the FLUSPECT leaf fluorescence model. `no licence`
- [TalosSources/stomatal_hybrid_modelling](https://github.com/TalosSources/stomatal_hybrid_modelling) - No description provided. `no licence`

<a id="photosynthesis-modelica"></a>

#### Modelica

- [akashjoshi4/Photosynthesis](https://github.com/akashjoshi4/Photosynthesis) - A Modelica model of photosynthesis. `★ 1` `no licence`

<a id="photosynthesis-ocaml"></a>

#### OCaml

- [wusunlab/leaf-pst](https://github.com/wusunlab/leaf-pst) - &#91;WORK IN PROGRESS&#93; Coupled Leaf Photosynthesis--Stomatal Conductance--Temperature (PST) Solver. `MIT`

<a id="photosynthesis-python"></a>

#### Python

- [tglauch/pyVPRM](https://github.com/tglauch/pyVPRM) - pyVPRM: a Python implementation of data-driven biosphere models, including the Vegetation Photosynthesis and Respiration Model (VPRM), for NEE partitioning, response-function interpretation, and… `★ 41` `MIT`
- [ImperialCollegeLondon/pyrealm](https://github.com/ImperialCollegeLondon/pyrealm) - Development of the pyrealm package, providing an integrated toolbox for modelling plant productivity, growth and demography using Python. `★ 38` `MIT`
- [openalea/hydroshoot](https://github.com/openalea/hydroshoot) - Plant hydraulic, gas-exchange, and energy processes on a shoot architecture. `★ 20` `custom licence`
- [samhartz/Photo3](https://github.com/samhartz/Photo3) - Unified modeling of C3, C4, and CAM photosynthesis. `★ 17` `GPL-3.0`
- [JPL-Evapotranspiration-Algorithms/BESS-JPL](https://github.com/JPL-Evapotranspiration-Algorithms/BESS-JPL) - Breathing Earth System Simulator (BESS) Gross Primary Production (GPP) Model Python Implementation. `★ 14` `Apache-2.0`
- [openalea/caribu](https://github.com/openalea/caribu) - Light interception calculations for explicit plant canopies. `★ 10` `custom licence`
- [rootchang/3dCAP-wheat](https://github.com/rootchang/3dCAP-wheat) - No description provided. `★ 9` `GPL-3.0`
- [tquaife/pySellersTwoStream](https://github.com/tquaife/pySellersTwoStream) - Python implementation of the Sellers two-stream canopy radiative transfer model. `★ 8` `GPL-2.0`
- [Georgy-Nerobelov/VPRM-code](https://github.com/Georgy-Nerobelov/VPRM-code) - Vegetation Photosynthesis and Respiration Model (Mahadevan et al., 2008) in Python. `★ 6` `no licence`
- [cropbox/plants2020](https://github.com/cropbox/plants2020) - coupled leaf gas-exchange model for C₄ leaves comparing stomatal conductance models. `★ 4` `no licence`
- [Gntakos/pyFvCB](https://github.com/Gntakos/pyFvCB) - Farquhar, von Caemmerer and Berry model of C3 leaf photosynthesis, as described in doi.org/10.1017/9781107339217.012. `★ 4` `no licence`
- [codexf/Modeling_Photosynthesis](https://github.com/codexf/Modeling_Photosynthesis) - Custom scripts for modelling the photosynthetic responses to carbon dioxide concentration and photosynthetic responses during oxygen transients. `★ 2` `no licence`
- [mdekauwe/Coupled_Canopy](https://github.com/mdekauwe/Coupled_Canopy) - No description provided. `★ 2` `no licence`
- [mdekauwe/pydesica](https://github.com/mdekauwe/pydesica) - Plant hydraulic model. `★ 2` `no licence`
- [nomurako/RowCropPhotosynthesisModel](https://github.com/nomurako/RowCropPhotosynthesisModel) - A mathematical model for calculating the canopy photosynthetic rate of a row-planted crop canopy. `★ 2` `MIT`
- [s-kganz/leaf_eb_julia](https://github.com/s-kganz/leaf_eb_julia) - Leaf energy balance in Julia. `★ 2` `no licence`
- [bnulzq/MLR-SIF](https://github.com/bnulzq/MLR-SIF) - Leaf-level and canopy-level mechanistic light reaction (MLR) model to mechanistically link solar-induced chlorophyll fluorescence and gross primary production (GPP). `★ 1` `MIT`
- [Drfengze/SCOPE_python_prerelease](https://github.com/Drfengze/SCOPE_python_prerelease) - ver 0.1.0. `★ 1` `no licence`
- [openalea-incubator/riri5](https://github.com/openalea-incubator/riri5) - RIRI5 is a simplified version of the radiation transfer model RIRI, from RATP. It is part of the Virtual GrassLand model (VGL) developed on the OpenAlea platfom. `★ 1` `custom licence`
- [openalea/fractalysis](https://github.com/openalea/fractalysis) - 3D Fractal Analysis. Application to Light Interception. `★ 1` `custom licence`
- [QTB-HHU/photosynthesismodel](https://github.com/QTB-HHU/photosynthesismodel) - Computational model of photosynthesis resulted from a merge of two previously published mathematical models of relevant subprocesses. `★ 1` `no licence`
- [adjablonski/Plant-Physiology](https://github.com/adjablonski/Plant-Physiology) - Models for carbon and light reactions of photosynthesis. `no licence`
- [benbenbeatit912002/stomatal-conductance-modeling](https://github.com/benbenbeatit912002/stomatal-conductance-modeling) - No description provided. `no licence`
- [CCGCAM/scopeinpython](https://github.com/CCGCAM/scopeinpython) - Python port of SCOPEinR for SCOPE simulations of canopy radiative transfer, photosynthesis, chlorophyll fluorescence and energy balance. `GPL-3.0`
- [chilperic/photosynthesis-climate-adaptation-model](https://github.com/chilperic/photosynthesis-climate-adaptation-model) - Coupled C3/C4 photosynthesis, heat-balance, hydraulics, sensitivity-analysis, and evolutionary trait-adaptation model from my postdoctoral research. `custom licence`
- [desai-sahil/stomatal-conductance-model](https://github.com/desai-sahil/stomatal-conductance-model) - No description provided. `no licence`
- [drdmitrymikhaylov/biochempinn-crop-photosynthesis-boost](https://github.com/drdmitrymikhaylov/biochempinn-crop-photosynthesis-boost) - What a biostimulant changes inside the leaf, measured. `CC-BY-4.0`
- [ecamo19/plant_hydraulics](https://github.com/ecamo19/plant_hydraulics) - No description provided. `Apache-2.0`
- [gcamargo1/SolarRadInterception](https://github.com/gcamargo1/SolarRadInterception) - Three methods to calculate solar radiation interception in multi species canopies. `no licence`
- [GitHub-srivastava/pyLeaf-torch](https://github.com/GitHub-srivastava/pyLeaf-torch) - No description provided. `MIT`
- [ishasanjaypopat-spec/glycolatepathway](https://github.com/ishasanjaypopat-spec/glycolatepathway) - No description provided. `no licence`
- [LewisYork/Simulation-of-Photosynthesis-in-the-Plant-Canopy](https://github.com/LewisYork/Simulation-of-Photosynthesis-in-the-Plant-Canopy) - No description provided. `no licence`
- [McHailey/Carbon.Tree](https://github.com/McHailey/Carbon.Tree) - Simulate Canopy Photosynthesis. `no licence`
- [mdekauwe/optimise_nitrogen_allocation](https://github.com/mdekauwe/optimise_nitrogen_allocation) - Optimise allocation of nitrogen within leaf to maximise net photosynthesis. `no licence`
- [mhpi/diffEcosys_Acclimation](https://github.com/mhpi/diffEcosys_Acclimation) - No description provided. `custom licence`
- [Moges-Retta/3D_reaction_diffuion_model_photosynthesis](https://github.com/Moges-Retta/3D_reaction_diffuion_model_photosynthesis) - No description provided. `no licence`
- [mpetalcorin/c3-photosynthesis-enhancement](https://github.com/mpetalcorin/c3-photosynthesis-enhancement) - Simulation framework and benchmark datasets for evaluating fast-impact genetic strategies that enhance C3 photosynthesis, water use efficiency, and nitrogen efficiency as a bridge toward C4-like crops. `no licence`
- [mpetalcorin/C3.5-Photosynthesis-Reprogramming-mitochondria-as-carbon-recycling-organelles](https://github.com/mpetalcorin/C3.5-Photosynthesis-Reprogramming-mitochondria-as-carbon-recycling-organelles) - This repository contains code, simulated datasets, and analyses exploring the feasibility of C3.5 photosynthesis: a synthetic biology strategy that repurposes mitochondria as carbon-recycling… `no licence`
- [mpetalcorin/Photorespiration-Bypass-Rubisco-Optimisation-and-Stomatal-Tuning-Simulation-Framework](https://github.com/mpetalcorin/Photorespiration-Bypass-Rubisco-Optimisation-and-Stomatal-Tuning-Simulation-Framework) - This repository contains simulation and analysis scripts used in the study “Integrative Simulation of Photorespiration Bypass, Rubisco Optimisation, and Stomatal Tuning Predicts Synergistic… `no licence`
- [nasla-96/canopy_data_generation_surrogate_pipeline](https://github.com/nasla-96/canopy_data_generation_surrogate_pipeline) - pipeline for maize canopy data generation, Helios light capture simulation, and machine learning surrogate training. `no licence`
- [pwendering/C4TUNE](https://github.com/pwendering/C4TUNE) - Prediction of parameters for a kinetic model of C4 photosynthesis. `MIT`
- [roandejager/Plant-Physiology-Optimizer-Simulator](https://github.com/roandejager/Plant-Physiology-Optimizer-Simulator) - A plant physiology simulator and optimizer that uses Differential Evolution and the Medlyn stomatal model to find optimal botanical traits for environmental stress. `no licence`
- [SonyCSLParis/photosynthesis_models](https://github.com/SonyCSLParis/photosynthesis_models) - Models of the photosynthetic electron transport chain. `no licence`
- [TUM-PIK-ESM/LPJmL-hybrid-photosynthesis](https://github.com/TUM-PIK-ESM/LPJmL-hybrid-photosynthesis) - No description provided. `MIT`
- [URBAG-ICTA/VPRM_offline](https://github.com/URBAG-ICTA/VPRM_offline) - Vegetation Photosynthesis and Respiration Model offline version. `no licence`
- [VivianaCelis/stomatal_conductance_model](https://github.com/VivianaCelis/stomatal_conductance_model) - No description provided. `MIT`
- [yinyi11/Leaf-level-photosynthesis-model](https://github.com/yinyi11/Leaf-level-photosynthesis-model) - Simple leaf level photosynthesis model to diagose C3/C4 CO2 fertilization effect. `no licence`
- [ymaltsman/Photosynthesis](https://github.com/ymaltsman/Photosynthesis) - A project with Jinyun Tang at Lawrence Berkeley Lab to develop an updated model of photosynthesis. `no licence`
- [zhujiedong/plantecopyts_py](https://github.com/zhujiedong/plantecopyts_py) - No description provided. `no licence`

<a id="photosynthesis-r"></a>

#### R

- [cdmuir/photosynthesis](https://github.com/cdmuir/photosynthesis) - Plant ecophysiology calculations and process-modeling tools. `★ 39` `custom licence`
- [RemkoDuursma/plantecophys](https://github.com/RemkoDuursma/plantecophys) - R tools for fitting and simulating leaf gas exchange. `★ 18` `no licence`
- [Timothy-W-Hilton/VPRMLandSfcModel](https://github.com/Timothy-W-Hilton/VPRMLandSfcModel) - pure R implementation of the Vegetation Photosynthesis and Respiration Model (VPRM) of Mahadevan et al (2008) with parameter optimization. `★ 10` `no licence`
- [eloch216/PhotoGEA](https://github.com/eloch216/PhotoGEA) - No description provided. `★ 8` `custom licence`
- [TESTgroup-BNL/LeafGasExchange](https://github.com/TESTgroup-BNL/LeafGasExchange) - An R package for fitting and simulating leaf level gas exchange. `★ 8` `GPL-3.0`
- [jstinzi/plantecowrap](https://github.com/jstinzi/plantecowrap) - Enhancing the capabilities of plantecophys by Duursma (2015). `★ 7` `custom licence`
- [Matthews-Research-Group/BioCro-ePhotosynthesis](https://github.com/Matthews-Research-Group/BioCro-ePhotosynthesis) - No description provided. `★ 4` `no licence`
- [TESTgroup-BNL/R-Canopy_Photosynthesis](https://github.com/TESTgroup-BNL/R-Canopy_Photosynthesis) - Testbed for canopy scaling and modeling of Photosynthesis and GPP. `★ 4` `GPL-3.0`
- [zhouhaoran06/C3C4OptPhotosynthesis-](https://github.com/zhouhaoran06/C3C4OptPhotosynthesis-) - Calculate C3 and C4 photosynthesis by optimizing stomatal conductance and leaf root allocation. `★ 4` `no licence`
- [CCGCAM/RTM-Suite](https://github.com/CCGCAM/RTM-Suite) - R tools for vegetation radiative transfer modelling — leaf/canopy optics (ToolsRTM) and full SCOPE energy-balance simulation (SCOPEinR). `★ 3` `MIT`
- [zhujiedong/plantecophys2](https://github.com/zhujiedong/plantecophys2) - No description provided. `★ 3` `no licence`
- [GCEL/ACM_GPP_ET](https://github.com/GCEL/ACM_GPP_ET) - The Aggregated Canopy Model. `★ 2` `no licence`
- [stcolema/photosynthesis](https://github.com/stcolema/photosynthesis) - Notes and code for modelling the Farquhar-van Caemmerer-Berry model of steady-state photosynthesis. `★ 2` `no licence`
- [ascafaro/photosynthesis_temperature_response_models](https://github.com/ascafaro/photosynthesis_temperature_response_models) - Models the response of net assimilation to rising leaf temperature. `★ 1` `CC0-1.0`
- [cdmuir/bayCi](https://github.com/cdmuir/bayCi) - Bayesian analysis of A-Ci response curves using RStan. `★ 1` `custom licence`
- [Jiangong-Liu/thermal_acclimation_canopy_photosynthesis](https://github.com/Jiangong-Liu/thermal_acclimation_canopy_photosynthesis) - This repository contains files and code scripts needed to reproduce the results and analysis presented in Liu et al. submitted to Nature Plants. `★ 1` `no licence`
- [PalmStudio/Farquhar](https://github.com/PalmStudio/Farquhar) - Fitting the Farquhar model parameters. `★ 1` `no licence`
- [vflo/Acclimated_gs_optimization_models](https://github.com/vflo/Acclimated_gs_optimization_models) - This repository contains the code necessary to obtain the results of the paper "Incorporating the photosynthetic acclimation into stomatal optimisation models" (Flo et al. 2023). `★ 1` `no licence`
- [bpetersen18/agro-ibis_photosynthesis](https://github.com/bpetersen18/agro-ibis_photosynthesis) - No description provided. `no licence`
- [CamilleSicangco/gsthermal](https://github.com/CamilleSicangco/gsthermal) - R package for stomatal optimization accounting for thermal and hydraulic costs. `custom licence`
- [CCGCAM/SCOPEinR](https://github.com/CCGCAM/SCOPEinR) - No description provided. `no licence`
- [chandrabellasio/C4-Electron-Transportand-biochemistry](https://github.com/chandrabellasio/C4-Electron-Transportand-biochemistry) - A biochemical model of C4 photosynthesis and electron transport. `no licence`
- [emmeliab/DAT_Proj](https://github.com/emmeliab/DAT_Proj) - Scripts and results from Dynamic Assimilation Manuscript. `custom licence`
- [flaviobastoscampos/SFmodel_Plt](https://github.com/flaviobastoscampos/SFmodel_Plt) - code source for the Sap Flow model used in the work "Evapotranspiration dynamics and partitioning in a grassed vineyard: ecophysiological and computational modelling approaches". Data for this… `no licence`
- [heliotropichuman/photosynthesisLRC](https://github.com/heliotropichuman/photosynthesisLRC) - R package github repository to test photosynthetic models, and get functional traits from light response curves. `MIT`
- [Iqbalwasim01/Sunlit-shaded-canopy-photosynthesis-model](https://github.com/Iqbalwasim01/Sunlit-shaded-canopy-photosynthesis-model) - For the R scripts/code to work you must have these R packages installed:. `no licence`
- [juergenknauer/leaf_photosyn](https://github.com/juergenknauer/leaf_photosyn) - A simple photosynthesis model. `GPL-3.0`
- [KillianWUR/Review_paper_wind_photosynthesis](https://github.com/KillianWUR/Review_paper_wind_photosynthesis) - No description provided. `no licence`
- [lovelilyinfall/Photosynthesis-model](https://github.com/lovelilyinfall/Photosynthesis-model) - C3 and C4 Bayesian model code and documentation. `no licence`
- [MilanFischer/LeafAreaIndex](https://github.com/MilanFischer/LeafAreaIndex) - R code computing leaf area index from PAR measured above and below the canopy under all sky conditions. `GPL-3.0`
- [mxdurand/dynamo](https://github.com/mxdurand/dynamo) - Dynamic stomata modelling. `GPL-3.0`
- [QinJian-cug/rTRIPLEX_SIF](https://github.com/QinJian-cug/rTRIPLEX_SIF) - This photosynthesis model integrates solar-induced chlorophyll fluorescence (SIF) into leaf photosynthesis process to calculate the instantaneous leaf gross photosynthetic rate, and is an integrated… `custom licence`
- [rmcnellis/johnsonberry_photosynthesis_R](https://github.com/rmcnellis/johnsonberry_photosynthesis_R) - R implementation for Johnson & Berry photosynthesis model. `no licence`
- [SmithEcophysLab/c4_lsm_comparison](https://github.com/SmithEcophysLab/c4_lsm_comparison) - Comparison of C4 leaf photosynthesis simulations in LSMs. `no licence`
- [SmithEcophysLab/c4_model_comparison](https://github.com/SmithEcophysLab/c4_model_comparison) - Code to compare different versions of models of C4 photosynthesis. `no licence`
- [SmithEcophysLab/c4_model_sensitivity](https://github.com/SmithEcophysLab/c4_model_sensitivity) - Repository to explore the parameter sensitivity of the von Caemmerer C4 photosynthesis model. `no licence`
- [SmithEcophysLab/photosynthesis_model_drake](https://github.com/SmithEcophysLab/photosynthesis_model_drake) - Repository to simulate photosynthesis using data from Drake et al. experiment. `no licence`
- [SmithEcophysLab/photosynthesis_timescale_model](https://github.com/SmithEcophysLab/photosynthesis_timescale_model) - Repository to calculate photosynthesis based on the Farquhar et al. (1980) model using data from Eve Gray's thesis project on the acclimation timescale of photosynthesis in G. max. `no licence`
- [SmithEcophysLab/photosynthesis_variability_model](https://github.com/SmithEcophysLab/photosynthesis_variability_model) - Repository to calculate photosynthesis using the Farquhar model for Christine Vanginault's variability experiment. `no licence`
- [vinjacob88/c4-aci-fitting](https://github.com/vinjacob88/c4-aci-fitting) - Testing different methods for fitting C4 ACi curves. `no licence`
- [Zinny-E/C4_photosynthesis](https://github.com/Zinny-E/C4_photosynthesis) - Repository for C4 model. `no licence`

<a id="photosynthesis-typescript"></a>

#### TypeScript

- [javiermazo-gc/PhotoModel](https://github.com/javiermazo-gc/PhotoModel) - Working photosynthesis metabolic model interface. `no licence`

<a id="photosynthesis-other"></a>

#### Other

- [rootchang/3dCAP](https://github.com/rootchang/3dCAP) - This project aims at reconstructing plant canopy structures by 2D images of plants and plant organs, and calculating canopy photosynthesis with further measurement of leaves nitrogen content and… `★ 11` `no licence`
- [wangyakai01/APSIM-SIF](https://github.com/wangyakai01/APSIM-SIF) - APSIM extended with equations coupling solar-induced fluorescence (SIF) to photosynthesis. `★ 5` `no licence`
- [YachangHe/SIP-Canopy-Web-Demo](https://github.com/YachangHe/SIP-Canopy-Web-Demo) - Browser-based SIP canopy radiative transfer demo for optical BRF and solar-induced chlorophyll fluorescence simulations. `★ 1` `MIT`
- [Computational-Biology-Aachen/GoPMF](https://github.com/Computational-Biology-Aachen/GoPMF) - Mechanistic, computatioanl models of photosynthesis across species. `GPL-3.0`
- [erika-serrano/Cold-acclimation-of-mesophyll-conductance-bundle-sheath-conductance-and-leakiness-in-Miscanthus-x-g](https://github.com/erika-serrano/Cold-acclimation-of-mesophyll-conductance-bundle-sheath-conductance-and-leakiness-in-Miscanthus-x-g) - R script for combined model of C4 enzyme limited photosynthesis and discrimination. `no licence`
- [nicocas7ro/Light-interception](https://github.com/nicocas7ro/Light-interception) - Solar light interception for a vertical canopy. `no licence`
- [Rith32/PRLC](https://github.com/Rith32/PRLC) - Utilizing photosynthesis data extracted from plants, this model applies a fit to create a smooth photosynthetic light response curve in hopes to display data such as a max saturation value. `no licence`

<a id="architecture"></a>

### Plant architecture and FSPM

<a id="architecture-c"></a>

#### C

- [openalea/libcaribu](https://github.com/openalea/libcaribu) - C++ compiled extension of openalea.caribu. `custom licence`

<a id="architecture-cplusplus"></a>

#### C++

- [Plant-Root-Soil-Interactions-Modelling/CPlantBox](https://github.com/Plant-Root-Soil-Interactions-Modelling/CPlantBox) - Plant architecture with functional water and carbon process coupling. `★ 79` `GPL-3.0`

<a id="architecture-glsl"></a>

#### GLSL

- [openalea-incubator/plantik](https://github.com/openalea-incubator/plantik) - The PlanTiK package provides standard modules to simulate plant growth. It provides simple simulation module but also biological classes. `★ 2` `custom licence`

<a id="architecture-java"></a>

#### Java

- [junqi108/Functional-structural-plant-model-prototype](https://github.com/junqi108/Functional-structural-plant-model-prototype) - Developing the next generation functional-structural-plant-model for facilitating flexible configuration. `★ 1` `no licence`

<a id="architecture-julia"></a>

#### Julia

- [VEZY/Archimed.jl](https://github.com/VEZY/Archimed.jl) - The ARCHIMED model in Julia. `★ 2` `MIT`

<a id="architecture-python"></a>

#### Python

- [openalea/adel](https://github.com/openalea/adel) - Three-dimensional development and architecture models for grass crops. `★ 23` `custom licence`
- [openalea/cnwgrass](https://github.com/openalea/cnwgrass) - Grass architecture coupled to organ-scale carbon, nitrogen, and water processes. `★ 15` `custom licence`
- [openalea/ArchiCrop](https://github.com/openalea/ArchiCrop) - Three-dimensional crop architecture built from crop growth information. `★ 9` `custom licence`
- [tquaife/layeredCanopyTwoStream](https://github.com/tquaife/layeredCanopyTwoStream) - Radiative transfer code for vertically inhomogeneous canopies using the Meador and Weavor two stream approximation with adding. `★ 7` `GPL-2.0`
- [zmoon/crt1d](https://github.com/zmoon/crt1d) - 1-D vegetation canopy radiative transfer schemes. `★ 6` `MIT`
- [kernelshreyak/plant_growth_simulation](https://github.com/kernelshreyak/plant_growth_simulation) - Simulation of plant growth in 2D. Accelerated with Numba. `★ 3` `MIT`
- [openalea/rose](https://github.com/openalea/rose) - Rose architecture reconstruction and light interception. `★ 2` `custom licence`
- [BasvdHerik/BR_Branching](https://github.com/BasvdHerik/BR_Branching) - No description provided. `★ 1` `GPL-3.0`
- [mzschwartz5/PlantGrowthModeling](https://github.com/mzschwartz5/PlantGrowthModeling) - Python simulation of plant growth. `★ 1` `no licence`
- [nasla-96/maize-canopy-modeling](https://github.com/nasla-96/maize-canopy-modeling) - code and data for "Towards smart canopies: Algorithmic design of maize canopy architectures that maximize light use efficiency". `no licence`
- [openalea-incubator/turgor-growth](https://github.com/openalea-incubator/turgor-growth) - No description provided. `custom licence`
- [orianebro/ArchiCrop_for_STICS-IC_light](https://github.com/orianebro/ArchiCrop_for_STICS-IC_light) - No description provided. `LGPL-2.1`
- [QiaoqiaoTeng/soybean-4d-digital-twin](https://github.com/QiaoqiaoTeng/soybean-4d-digital-twin) - Code, trained surrogate models, simulation outputs, and reviewer testing materials for a geometry-driven 4D soybean digital twin framework. `no licence`
- [Socoton/APTOS](https://github.com/Socoton/APTOS) - No description provided. `custom licence`

<a id="architecture-r"></a>

#### R

- [cran/LAD](https://github.com/cran/LAD) - :exclamation: This is a read-only mirror of the CRAN R package repository. LAD — Derive Leaf Angle Distribution (LAD) from Measured Leaf Inclination Angles. `★ 2` `custom licence`
- [mone27/radiative-transfer-model](https://github.com/mone27/radiative-transfer-model) - Model for radiative transfer in canopies. `★ 2` `GPL-3.0`

<a id="architecture-other"></a>

#### Other

- [dhelmrich/SplineConcepts](https://github.com/dhelmrich/SplineConcepts) - A library that enables the geometrization of small plant organs using templated splines. `★ 2` `MIT`
- [ghyangyh/VPlant](https://github.com/ghyangyh/VPlant) - Virtual Plant Modeler. `no licence`
- [mroutley/PlantArchitectureMod](https://github.com/mroutley/PlantArchitectureMod) - An l-system for modelling plant architecture. `no licence`
- [VeroniqueLC/PlantStructureFactoryStochastic](https://github.com/VeroniqueLC/PlantStructureFactoryStochastic) - Simulation of plant structure - stochastic version - GreenLab model. `no licence`

<a id="roots"></a>

### Roots and rhizosphere

<a id="roots-cplusplus"></a>

#### C++

- [Plant-Root-Soil-Interactions-Modelling/CRootBox](https://github.com/Plant-Root-Soil-Interactions-Modelling/CRootBox) - No description provided. `★ 20` `custom licence`
- [Plant-Root-Soil-Interactions-Modelling/dumux-rosi](https://github.com/Plant-Root-Soil-Interactions-Modelling/dumux-rosi) - Soil and root interaction simulations through DuMuX-based interfaces. `★ 10` `no licence`
- [iba5104/RootSlice](https://github.com/iba5104/RootSlice) - No description provided. `★ 1` `GPL-3.0`
- [GiorgioRaimondi10422330/Tree_root_Project](https://github.com/GiorgioRaimondi10422330/Tree_root_Project) - No description provided. `no licence`
- [m-giraud/Giraud2025_C_W_Rhizo](https://github.com/m-giraud/Giraud2025_C_W_Rhizo) - No description provided. `no licence`

<a id="roots-fortran"></a>

#### Fortran

- [laagee/pflotran-dev-root-system](https://github.com/laagee/pflotran-dev-root-system) - No description provided. `★ 2` `no licence`
- [wjin33/R-SWMS](https://github.com/wjin33/R-SWMS) - Root system architecture modeling in unsaturated soil with obstacles. `★ 2` `no licence`
- [femeunier/RSWMS](https://github.com/femeunier/RSWMS) - R-SWMS repository of the old versions. `★ 1` `no licence`
- [arsonc/R-SWMS](https://github.com/arsonc/R-SWMS) - No description provided. `no licence`
- [LiuYangly5555/RWU](https://github.com/LiuYangly5555/RWU) - HYDRUS-1D source code and JV-CR model code for model root water uptake. `no licence`
- [marinalamelo/MFlux_Brooks-Corey](https://github.com/marinalamelo/MFlux_Brooks-Corey) - This program refers to the analytical solution of the microscopic root water uptake model developed by Quirijn de Jong van Lier for the special case of Brooks and Corey soils. Run it online… `MIT`
- [qdjvlier/MFlux](https://github.com/qdjvlier/MFlux) - Calculates root water uptake and soil and crop potentials according to a process-based model. `no licence`

<a id="roots-groovy"></a>

#### Groovy

- [braghiere/3D_FSPM](https://github.com/braghiere/3D_FSPM) - No description provided. `★ 1` `MIT`

<a id="roots-julia"></a>

#### Julia

- [cropbox/CropRootBox.jl](https://github.com/cropbox/CropRootBox.jl) - 🪴 example of root system architecture simulation like CRootBox. `★ 2` `MIT`
- [bspanoghe/ERT_Roots](https://github.com/bspanoghe/ERT_Roots) - No description provided. `MIT`
- [lobetb/ArchiJulia](https://github.com/lobetb/ArchiJulia) - Translation of ArchiSimple from cpp to Julia. `no licence`
- [takashi2024/root-fspm-minirhizotron](https://github.com/takashi2024/root-fspm-minirhizotron) - Parameterization of a Functional-Structural Plant Model from Minirhizotron Observations: CMA-ES vs Simulation-Based Inference. `no licence`

<a id="roots-mathematica"></a>

#### Mathematica

- [seki-design/sucrose-transport](https://github.com/seki-design/sucrose-transport) - No description provided. `no licence`

<a id="roots-matlab"></a>

#### MATLAB

- [GERUlab/Soil-Plant-Hydraulics](https://github.com/GERUlab/Soil-Plant-Hydraulics) - Matlab files related to the Carminati_Javaux model from the article 'Soil Rather Than Xylem Vulnerability Controls Stomatal Response to Drought'. Download… `★ 2` `no licence`
- [Eric-J-Neil/Multi-PRIME-model](https://github.com/Eric-J-Neil/Multi-PRIME-model) - 'Multimodal Physically-Based Root Water Uptake Isotope Mixing Estimation'. `★ 1` `no licence`
- [pvjeetze/Heterogeneity-RootWaterUptake](https://github.com/pvjeetze/Heterogeneity-RootWaterUptake) - MATLAB code for modelling root water uptake in heterogeneous soil. `★ 1` `no licence`
- [StochasticBiology/root-inference](https://github.com/StochasticBiology/root-inference) - Implements an approximate Bayesian computation (ABC) inference and model selection using summary statistics for plant root systems to learn about the mechanisms underlying root growth. `★ 1` `no licence`
- [clareziegler/Root-inference](https://github.com/clareziegler/Root-inference) - Code and analysis for the paper Model selection and parameter estimation for root architecture models using likelihood-free inference C Ziegler, RJ Dyson, IG Johnston Journal of the Royal Society… `no licence`
- [Eric-J-Neil/PRIME-Model](https://github.com/Eric-J-Neil/PRIME-Model) - No description provided. `no licence`
- [FlowSto/SingleRoot_Model](https://github.com/FlowSto/SingleRoot_Model) - Single Root water uptake model for four different maize root types (brace, crown, seminal. lateral). `no licence`

<a id="roots-python"></a>

#### Python

- [cojacoo/rootwater](https://github.com/cojacoo/rootwater) - Calculate root water uptake from change in rhizosphere soil moisture plus some misc sap flow tools. `★ 8` `MIT`
- [openalea/rhizodep](https://github.com/openalea/rhizodep) - Root development and rhizodeposition linked to plant carbon balance. `★ 5` `custom licence`
- [fdifonzo/shooting-roots-python-code](https://github.com/fdifonzo/shooting-roots-python-code) - Python code for shooting method applied to Richards' equation with root water uptake models. `★ 4` `no licence`
- [JBris/deep-root-gen](https://github.com/JBris/deep-root-gen) - A simulation model for the digital reconstruction of 3D root system architectures. Integrated with a simulation-based inference generative deep learning model. `★ 4` `GPL-3.0`
- [jangojangojango/PINN-RWU-Hydrogeophysics](https://github.com/jangojangojango/PINN-RWU-Hydrogeophysics) - A physics-informed neural network workflow for forward and inverse modeling of unsaturated flow and root water uptake from hydrogeophysical data. `★ 3` `no licence`
- [junqi108/Root-architecture-generator](https://github.com/junqi108/Root-architecture-generator) - During the summer student internship of James Bristow, we developed a generic methods for generating root architecture based on simple rules and could optimize the parameters to match the field… `★ 2` `GPL-3.0`
- [openalea/hydroroot](https://github.com/openalea/hydroroot) - Simulation of hydraulic root architecture. `★ 2` `custom licence`
- [openalea/Root-CyNAPS](https://github.com/openalea/Root-CyNAPS) - Root nitrogen cycling represented across plant scales. `★ 2` `custom licence`
- [Plant-Food-Research-Open/deep-root-gen](https://github.com/Plant-Food-Research-Open/deep-root-gen) - No description provided. `★ 2` `GPL-3.0`
- [gcamargo1/WaterUptakeModels](https://github.com/gcamargo1/WaterUptakeModels) - This repo is part of the supplemental material of a crop water uptake models comparison. `★ 1` `MIT`
- [GeraultTr/Root_BRIDGES](https://github.com/GeraultTr/Root_BRIDGES) - No description provided. `★ 1` `no licence`
- [HydraulicViper/HydraulicViper](https://github.com/HydraulicViper/HydraulicViper) - No description provided. `★ 1` `GPL-3.0`
- [jpalacios84/sapflow](https://github.com/jpalacios84/sapflow) - PDE solver for soil infiltration problem with root water uptake term (Richard's equation). `★ 1` `no licence`
- [MDagostino1/TRoot](https://github.com/MDagostino1/TRoot) - No description provided. `★ 1` `no licence`
- [openalea-incubator/GRANAP-dev](https://github.com/openalea-incubator/GRANAP-dev) - No description provided. `★ 1` `GPL-3.0`
- [openalea-incubator/MECHA-dev](https://github.com/openalea-incubator/MECHA-dev) - No description provided. `★ 1` `GPL-3.0`
- [andrewmair1994/rhizodeposits_code_and_data](https://github.com/andrewmair1994/rhizodeposits_code_and_data) - Code and data associated with the manuscript "Modelling the influence of rhizodeposits on root water uptake". `no licence`
- [GreenSmart-DSS/RootWaterSim](https://github.com/GreenSmart-DSS/RootWaterSim) - Interactive simulator of 1D soil water flow and root water uptake. `MIT`
- [Jannetty/ARORA](https://github.com/Jannetty/ARORA) - ARORA: Agent-based representation of root architecture. `no licence`
- [luisferangulob/3d-root-architecture-simulator](https://github.com/luisferangulob/3d-root-architecture-simulator) - Reproducible scientific-computing framework for stochastic 3D root architecture simulation, quantitative analysis, and scalable Monte Carlo experiments. `no licence`
- [malikwaseem857/Agricultural_Crop_Root_Architecture-_Simulator-](https://github.com/malikwaseem857/Agricultural_Crop_Root_Architecture-_Simulator-) - Stress-Modeling Simulator for Crop Analytics. `no licence`
- [openalea-incubator/branchingnetwork](https://github.com/openalea-incubator/branchingnetwork) - Workshop on Branching Networks for OpenAlea. `custom licence`
- [Ridorichard04/Cos-Persistence-Model](https://github.com/Ridorichard04/Cos-Persistence-Model) - Open-source Python simulation of chitosan oligosaccharide (COS) degradation and adsorption dynamics in the rhizosphere. `MIT`

<a id="roots-r"></a>

#### R

- [jknigh0813/LSM_RWU](https://github.com/jknigh0813/LSM_RWU) - Root water uptake model files. `★ 2` `no licence`
- [MARSHAL-ROOT/marshal](https://github.com/MARSHAL-ROOT/marshal) - R package for MARSHAL. `★ 2` `Apache-2.0`
- [AgronomyKiel/RootDataRuthe](https://github.com/AgronomyKiel/RootDataRuthe) - Parameterisation of simple root growth model from soil core and minirhizotrone data. `MIT`
- [OliverHargreaves/Root_Depth](https://github.com/OliverHargreaves/Root_Depth) - Calculates crop root depth according to the FAO 56 model. `no licence`

<a id="roots-other"></a>

#### Other

- [GDanielGzz/OpenSimRootDJ123](https://github.com/GDanielGzz/OpenSimRootDJ123) - Work In Progress for DJ123 Rice Root Architectural Model. `★ 2` `no licence`
- [Qiuyang1997/Root-Water-Uptake-Based-on-Distributed-Moisture-Storage-Dynamic](https://github.com/Qiuyang1997/Root-Water-Uptake-Based-on-Distributed-Moisture-Storage-Dynamic) - No description provided. `no licence`
- [SchornacklabSLCU/MycorRhize3D](https://github.com/SchornacklabSLCU/MycorRhize3D) - 3D root growth and Mycorrhiza colonisation simulator. `MIT`

<a id="soil-water"></a>

### Soil water and heat

<a id="soil-water-c"></a>

#### C

- [DrylandEcology/SOILWAT2](https://github.com/DrylandEcology/SOILWAT2) - An ecosystem water balance simulation model. `★ 8` `GPL-3.0`
- [fred-ogden/DSBM](https://github.com/fred-ogden/DSBM) - Discrete Soil Moisture Balance Model. `Apache-2.0`
- [jaapschellekens/vamps](https://github.com/jaapschellekens/vamps) - vamps - a Vegetation-AtMosPhere-Soil water model. `BSD-2-Clause`
- [PSUmodeling/Richards-equation-CVODE-test](https://github.com/PSUmodeling/Richards-equation-CVODE-test) - No description provided. `no licence`
- [YannChemin/r.hydro.swap](https://github.com/YannChemin/r.hydro.swap) - GRASS GIS Addon to run SWAP 4 on each pixel. `custom licence`

<a id="soil-water-csharp"></a>

#### C#

- [AgriculturalModelExchangeInitiative/SoilTemperatureModels](https://github.com/AgriculturalModelExchangeInitiative/SoilTemperatureModels) - Agricultural Model Exchange Initiative for Crop2ML components. `★ 2` `no licence`
- [Crop2ML-Catalog/DSSAT_EPICST_standalone](https://github.com/Crop2ML-Catalog/DSSAT_EPICST_standalone) - No description provided. `BSD-3-Clause`
- [zalf-rpm/ETModels](https://github.com/zalf-rpm/ETModels) - Soil temperature models from several crop models, exchanged across platforms via Crop2ML (AMEI workshop). `no licence`

<a id="soil-water-cplusplus"></a>

#### C++

- [ARPA-SIMC/CRITERIA1D](https://github.com/ARPA-SIMC/CRITERIA1D) - CRITERIA 1D is a one-dimensional agro-hydrological model. It includes soil water fluxes, crop development and crop water needs, a GIS interface (CRITERIA GEO) for geographical simulations and tools… `★ 16` `GPL-3.0`
- [markmbaum/Richards](https://github.com/markmbaum/Richards) - A finite-volume model solving the Richards equation (partially saturated groundwater flow) in one dimension with periodic wetting of the surface. `★ 8` `MIT`
- [UG4/plugin_Richards](https://github.com/UG4/plugin_Richards) - UG4 plugin for Richards' equation. `★ 1` `no licence`

<a id="soil-water-d"></a>

#### D

- [NumericalEnvironmental/vadose_multiphase](https://github.com/NumericalEnvironmental/vadose_multiphase) - A python script for modeling 1-D multiphase flow, based on a method-of-lines approach to solving a modified form of the Richards equation. `★ 5` `no licence`

<a id="soil-water-dart"></a>

#### Dart

- [outobecca/soilscope-public](https://github.com/outobecca/soilscope-public) - SoilScope-biosimulaattori on Dart- ja Flutter-pohjainen, tieteellinen maaperä-kasvi-ilmakehä-jatkumon (SPAC) biosimulaattori ja digitaalinen kaksonen. Se yhdistää laskennallisen ekofysiologian ja… `★ 1` `custom licence`

<a id="soil-water-fortran"></a>

#### Fortran

- [AgriHarmony/HYDRUS-1-D-gfortran](https://github.com/AgriHarmony/HYDRUS-1-D-gfortran) - A runnable version of HYDRUS-1d in Unix-based OS by gfortran. `★ 17` `GPL-3.0`
- [phydrus/source_code](https://github.com/phydrus/source_code) - Repository to host the Phydrus optimised Fortran code for the Hydrus-1D Model. `★ 16` `LGPL-3.0`
- [hydrogo/SWAP](https://github.com/hydrogo/SWAP) - SWAP (Soil Water–Atmosphere–Plants) land-surface model of Gusev and Nasonova. `★ 14` `no licence`
- [bilke/hydrus](https://github.com/bilke/hydrus) - CMake-ified Hydrus-1D. `★ 7` `GPL-3.0`
- [AgriHarmony/soil-hydraulic-simulation-backup](https://github.com/AgriHarmony/soil-hydraulic-simulation-backup) - Backup collection of soil–plant hydraulic simulation codes. `★ 5` `no licence`
- [DennisTimlin-USDA/2DSOILRunoff](https://github.com/DennisTimlin-USDA/2DSOILRunoff) - Soil water simulation including infiltration and runoff based on 2DSOIL. `★ 4` `no licence`
- [311-lab/UBMOD](https://github.com/311-lab/UBMOD) - An efficient soil water balance model based on hybrid numerical and statistical methods. `★ 2` `Apache-2.0`
- [goose888/1DRichards](https://github.com/goose888/1DRichards) - Describe soil water movement using 1-D theta based Richards Equation. Equation is solved through Picard iteration. `★ 2` `no licence`
- [Deltares-research/UZ_SequentialSteadyState](https://github.com/Deltares-research/UZ_SequentialSteadyState) - Python prototype and Fortran implementation of a meta-model of moisture transport in the unsaturated (vadose) zone, using a database of structured model results. To be operated in a coupled… `★ 1` `no licence`
- [mjpuma/SoilWaterFlow](https://github.com/mjpuma/SoilWaterFlow) - One dimensional, block-centered finite difference code to solve unsaturated flow equation with soil-water loss due to transpiration and evaporation. `★ 1` `MIT`
- [SiMokraneSIAD/FortranToolsForSoilScienceModeling](https://github.com/SiMokraneSIAD/FortranToolsForSoilScienceModeling) - This Fortran repository contains scientific routines for soil science modeling, focusing on soil moisture, infiltration, nutrient cycling, and soil respiration processes. All algorithms follow… `★ 1` `custom licence`
- [WaterlinePL/Hydrus-1D-for-Linux](https://github.com/WaterlinePL/Hydrus-1D-for-Linux) - No description provided. `★ 1` `MIT`
- [AgriculturalModelExchangeInitiative/FortranApsimCampbell](https://github.com/AgriculturalModelExchangeInitiative/FortranApsimCampbell) - No description provided. `no licence`
- [cojacoo/hydrus1Dpy](https://github.com/cojacoo/hydrus1Dpy) - The original Hydrus1D (Simunek et al. 2008) available as a python Richards solver. `no licence`
- [felipeiug/HYDRUS_1D_Python](https://github.com/felipeiug/HYDRUS_1D_Python) - Projeto para converter o código do Hydrus1D de Fortran para Python. `GPL-3.0`
- [gustolley/SWBM](https://github.com/gustolley/SWBM) - Soil-Water Budget Model. `GPL-3.0`
- [HydroCSLab/hydrus-1d](https://github.com/HydroCSLab/hydrus-1d) - HYDRUS-1D. `GPL-3.0`
- [kumayer/min3p-dp-perzan](https://github.com/kumayer/min3p-dp-perzan) - Enhanced dual permeability version of MIN3P including depth- and time-varying root water uptake and a new boundary condition option for dual permeability simulations including ponding. `MIT`
- [mark-decker/oneD_richards_sim_test](https://github.com/mark-decker/oneD_richards_sim_test) - Solves Richards Equation using Fortran OOP features. `no licence`
- [ovevans/richards_eqn](https://github.com/ovevans/richards_eqn) - Richards equation from Gottardi / Venutelli (1993). `no licence`
- [SWAP-model/SWAP](https://github.com/SWAP-model/SWAP) - Unofficial repository of SWAP Fortran code (begins with v4.2.0). `GPL-2.0`

<a id="soil-water-go"></a>

#### Go

- [maseology/goVSF](https://github.com/maseology/goVSF) - a go solution to one-dimensional Richards equation of vertical variably saturated flow. `★ 1` `MIT`

<a id="soil-water-java"></a>

#### Java

- [drww/newhall](https://github.com/drww/newhall) - A Java implementation of the Newhall model for soil temperature and moisture regime determination. Given a year of monthly averages for precipitation and temperature at a location, the model will… `★ 5` `custom licence`
- [HydroMewes/IPA](https://github.com/HydroMewes/IPA) - Agent-based framework for soil water movement modelling. `★ 1` `GPL-3.0`
- [mothlight/Simpel](https://github.com/mothlight/Simpel) - No description provided. `★ 1` `no licence`
- [ConcettaDAmato/Broker](https://github.com/ConcettaDAmato/Broker) - Broker is a numerical model to couple infiltration and evapotranspiration in GEOframe. This is the second version of the model, with the computation of a water stress for the evaporation. `GPL-3.0`

<a id="soil-water-julia"></a>

#### Julia

- [NumericalEnvironmental/Coupled_gas_water_flow_and_transport_porous_media](https://github.com/NumericalEnvironmental/Coupled_gas_water_flow_and_transport_porous_media) - This Julia language (version 0.5) script solves the coupled partial differential equations associated with (1) compressible gas flow in partially water-saturated porous media, (2)… `★ 10` `no licence`
- [NumericalEnvironmental/Unsaturated_Flow_2D_Steady-state](https://github.com/NumericalEnvironmental/Unsaturated_Flow_2D_Steady-state) - This script, written in Julia (v. 1.0), solves the steady-state form of the Richards equation for variably-saturated flow in porous media in a two-dimensional vertical cross section. `★ 10` `no licence`
- [SiMokraneSIAD/JuliaToolsForSoilScienceModeling](https://github.com/SiMokraneSIAD/JuliaToolsForSoilScienceModeling) - A Julia-based, high-performance soil science modeling toolkit for simulating physical, hydrological, biogeochemical, and erosion processes. `★ 4` `custom licence`
- [kmdeck/soil_implicit_solvers](https://github.com/kmdeck/soil_implicit_solvers) - Benchmarking ODE.jl when solving Richards equation. `★ 2` `no licence`
- [rodolfomssouza/SoilMoisture.jl](https://github.com/rodolfomssouza/SoilMoisture.jl) - No description provided. `★ 1` `MIT` `archived`
- [rodolfomssouza/Soil-Shrink-Swell](https://github.com/rodolfomssouza/Soil-Shrink-Swell) - No description provided. `MIT`
- [tristanmontoya/paper-2026-adaptive-richards](https://github.com/tristanmontoya/paper-2026-adaptive-richards) - Reproducibility repository for "A Fully Discrete, Mass-Conservative Adaptive Discontinuous Spectral-Element Method for the One-Dimensional Richards Equation in Mixed Form". `MIT`
- [Yujie-W/SoilHydraulics.jl](https://github.com/Yujie-W/SoilHydraulics.jl) - Soil hydraulics module for Soil-Plant-Air Continuum modeling. `Apache-2.0`

<a id="soil-water-mathematica"></a>

#### Mathematica

- [AbitathaRoy/Crop-Water-Simulator](https://github.com/AbitathaRoy/Crop-Water-Simulator) - Combined a theoretical framework with field data to simulate the movement of water in a single-crop system. `no licence`

<a id="soil-water-matlab"></a>

#### MATLAB

- [PMFlow/RichardsEquation](https://github.com/PMFlow/RichardsEquation) - Data repository accompanying the paper "Global random walk solvers for fully coupled flow and transport in saturated/unsaturated porous media" by Nicolae Suciu, Davide Illiano, Alexander Prechtel… `★ 8` `GPL-3.0`
- [jhabriel/RE-MPFA](https://github.com/jhabriel/RE-MPFA) - RE-MPFA is a package that implements a cell-centered finite volume discretization, specifically Multi-Point Flux Approximation (MPFA) in order to solve the three-dimensional incompressible… `★ 7` `GPL-3.0`
- [wayXing/RichardPoFlow](https://github.com/wayXing/RichardPoFlow) - Richards equation on porous media. `★ 5` `LGPL-3.0`
- [zLi90/rich1d](https://github.com/zLi90/rich1d) - Solve 1D Richards equation. `★ 5` `no licence`
- [sperriprinceton/Primary-Salinization-Model](https://github.com/sperriprinceton/Primary-Salinization-Model) - This code includes a parsimonious model of primary (i.e., natural) soil salinization. It solves the balance equations for the vertically-averaged relative soil moisture and salt mass dynamics under… `★ 4` `no licence`
- [iaelraij/Scup-VBC](https://github.com/iaelraij/Scup-VBC) - Matlab-HYDRUS-PHREEQC subroutine for a variable boundary condition at a suction cup with chemistry. `★ 3` `no licence`
- [yijianzeng/STEMMUS](https://github.com/yijianzeng/STEMMUS) - Simultaneous Transfer of Energy, Momentum, and Mass in Unsaturated Soil. `★ 3` `Apache-2.0`
- [MahyarGarshasbi/Soil-Moisture-Dynamics-Simulation](https://github.com/MahyarGarshasbi/Soil-Moisture-Dynamics-Simulation) - No description provided. `★ 2` `no licence`
- [SaeidKalantari/Richards-Equation](https://github.com/SaeidKalantari/Richards-Equation) - No description provided. `★ 2` `no licence`
- [SiMokraneSIAD/MATLABToolsForSoilScienceModeling](https://github.com/SiMokraneSIAD/MATLABToolsForSoilScienceModeling) - This repository provides a collection of MATLAB functions for simulating and analyzing key soil processes. It integrates models for soil physics, hydrology, biogeochemistry, and erosion, with a… `★ 2` `custom licence`
- [MiguelPanqueva2023/soil-moisture-mpc-greybox](https://github.com/MiguelPanqueva2023/soil-moisture-mpc-greybox) - Model Predictive Control of soil moisture using a water balance model with climatic disturbances, nonlinear dynamics, and a Grey-Box residual neural network. `★ 1` `no licence`
- [onaraighl/RESolve](https://github.com/onaraighl/RESolve) - 1D Richards Equation Solver (Matlab). `★ 1` `no licence`
- [86311972/Soil-Temperature-Amplitude-Phase-Prediction](https://github.com/86311972/Soil-Temperature-Amplitude-Phase-Prediction) - MATLAB code for predicting soil temperature amplitude (STAmp) and phase (STPhase) using MLR, RF, and Ensemble models with 10-fold cross-validation. `custom licence`
- [asighor/IvG](https://github.com/asighor/IvG) - IvG fits soil water retention model to measured data based on an improved van Genuchten. `MIT`
- [Dzidoula/AquaTwin-Drip-Hybrid-Digital-Twin-for-Controlling-Drip-Irrigation](https://github.com/Dzidoula/AquaTwin-Drip-Hybrid-Digital-Twin-for-Controlling-Drip-Irrigation) - The Challenge of Irrigation: From Empirical Decision-Making to Precision Management. `MIT`
- [Fahimearabi/SoilHeatFlux](https://github.com/Fahimearabi/SoilHeatFlux) - Soil_Heat_Flux. `no licence`
- [ivaninasetec/ACAP](https://github.com/ivaninasetec/ACAP) - ACAP Model. An alternative continuous form of Arya and Paris model to predict the soil water retention curve of a soil. `custom licence`
- [lucabrocca78/Soil-Moisture-Model-Matlab](https://github.com/lucabrocca78/Soil-Moisture-Model-Matlab) - Soil water balance model for estimating soil moisture. `no licence`
- [mengcao-prog/R-FLX-soil-moisture-model](https://github.com/mengcao-prog/R-FLX-soil-moisture-model) - This code provide revised soil moisture model based on a bulk model, with different complexity. `no licence`
- [SalimGoudarzi/RSEEP](https://github.com/SalimGoudarzi/RSEEP) - A model to Retrieve Soil-moisture and Estimate Ecohydrological Partitioning. `MIT`
- [sukishergill/soil_heat](https://github.com/sukishergill/soil_heat) - No description provided. `no licence`
- [woshizj123/Inverse-Modeling-of-Frequency-Domain-Based-RRE](https://github.com/woshizj123/Inverse-Modeling-of-Frequency-Domain-Based-RRE) - Inverse Modeling of Frequency Domain-Based One-Dimensional Soil Water Flow in Layered Soils. `no licence`
- [zshigrit/soil_heat_flow](https://github.com/zshigrit/soil_heat_flow) - No description provided. `no licence`

<a id="soil-water-python"></a>

#### Python

- [phydrus/phydrus](https://github.com/phydrus/phydrus) - :sweat_drops: Python implementation of the HYDRUS-1D unsaturated zone model. `★ 112` `LGPL-3.0`
- [ToshiyukiBandai/PINNs_RRE](https://github.com/ToshiyukiBandai/PINNs_RRE) - Physics-informed neural networks for the Richardson-Richards equation. `★ 34` `no licence`
- [amireson/openRE](https://github.com/amireson/openRE) - A simple, efficient, mass conservative approach to solving Richards’ Equation. `★ 28` `GPL-3.0`
- [amireson/RichardsEquation](https://github.com/amireson/RichardsEquation) - Richards' Equation model. `★ 28` `GPL-3.0`
- [EcoExtreML/STEMMUS_SCOPE](https://github.com/EcoExtreML/STEMMUS_SCOPE) - Integrated code of STEMMUS and SCOPE. `★ 26` `GPL-3.0`
- [martinvonk/pedon](https://github.com/martinvonk/pedon) - A Python package for analyzing unsaturated soil hydraulic properties. `★ 25` `MIT`
- [amireson/RichardsEquation_improved](https://github.com/amireson/RichardsEquation_improved) - A 1D Richards Equation solver written in python. `★ 24` `no licence`
- [cbsteh/PyWaterBal](https://github.com/cbsteh/PyWaterBal) - Unsaturated soil water flow model. `★ 15` `MIT`
- [arthur-e/simsoil](https://github.com/arthur-e/simsoil) - Very simple, point-scale soil hydrology model. `★ 14` `MIT`
- [ToshiyukiBandai/DD-PINNs-RRE](https://github.com/ToshiyukiBandai/DD-PINNs-RRE) - No description provided. `★ 12` `MIT`
- [raffalba/MYSIRR](https://github.com/raffalba/MYSIRR) - MY SIRR, (Minimalist agro-hYdrologicalmodel for Sustainable IRRigation management- soil moisture and crop dynamics), is a quantitative tool to assess and compare agricultural enterprises across… `★ 9` `GPL-3.0`
- [openalea-incubator/soil3ds](https://github.com/openalea-incubator/soil3ds) - 3DS is a 3D soil model simulating water and nitrogen fluxes into the soil which was adapted from the STICS soil module. It is part of the Virtual GrassLand model (VGL) developed on the OpenAlea… `★ 8` `custom licence`
- [XueziGong/KLE-PINN-EC](https://github.com/XueziGong/KLE-PINN-EC) - KLE-PINN-EC: Physics-Informed Neural Network with Enhanced Coupling for Inverse Modeling of Unsaturated Flow in Heterogeneous Soils. `★ 8` `no licence`
- [lucabrocca78/Soil-Moisture-Model-Python](https://github.com/lucabrocca78/Soil-Moisture-Model-Python) - Soil water balance model for estimating soil moisture (Python version). `★ 7` `no licence`
- [octavia-crompton/SVE-R](https://github.com/octavia-crompton/SVE-R) - A coupled Saint Venant Equations (SVE)- Richards Equation solver. `★ 6` `MIT`
- [AlainPascalFrances/MARMITES](https://github.com/AlainPascalFrances/MARMITES) - Water balance soil model coupled to MODFLOW. `★ 5` `no licence`
- [cvjena/InverseRRE](https://github.com/cvjena/InverseRRE) - Inverse problem of Richardson-Richards Equation. `★ 5` `MIT`
- [dgketchum/swim-rs](https://github.com/dgketchum/swim-rs) - Soil Water balance Inverse Modeling using Remote Sensing. `★ 5` `Apache-2.0`
- [Hamza-Kamil/PINN-MPINN-Water-Solute](https://github.com/Hamza-Kamil/PINN-MPINN-Water-Solute) - Paper: Modeling water and nitrogen dynamics in unsaturated soils using physics and multi-physics informed neural networks. `★ 5` `no licence`
- [thestochasticman/DownscalingMoistureModel](https://github.com/thestochasticman/DownscalingMoistureModel) - Producing higher resolution soil moisture maps using a water balancing approach. `★ 5` `no licence`
- [thskaggs/2014-steady-state](https://github.com/thskaggs/2014-steady-state) - Analytical steady-state solutions for water-limited cropping systems irrigated with saline water (Skaggs et al. 2014). `★ 5` `no licence`
- [yuyi13/PySWEB](https://github.com/yuyi13/PySWEB) - The Sydney Soil Water-Energy Balance Model. `★ 5` `MIT`
- [Hamza-Kamil/DeepONet-WaterFlow-Soils](https://github.com/Hamza-Kamil/DeepONet-WaterFlow-Soils) - Physics-informed neural operators for efficient modeling of water flow in unsaturated soils. `★ 4` `no licence`
- [HydroComplexity/SoilMoisture](https://github.com/HydroComplexity/SoilMoisture) - 1D Vertical Soil Moisture model. `★ 4` `GPL-3.0`
- [openmeteo/swb](https://github.com/openmeteo/swb) - Calculate soil water balance. `★ 4` `custom licence`
- [feng-ecohydro/soil-plant-model](https://github.com/feng-ecohydro/soil-plant-model) - Repository for the coupled soil-plant model used in Feng et al. (2018), Ecology Letters. `★ 3` `no licence`
- [GauravPahwa2021/Richards-Equation-Project](https://github.com/GauravPahwa2021/Richards-Equation-Project) - This is a Hydrology project.In this project I solved nonlinear partial differential equation which represents movement of water in unsaturated soils. `★ 3` `MIT`
- [jandepue/pyHydrus1D](https://github.com/jandepue/pyHydrus1D) - python implementation of Hydrus-1D. `★ 3` `MIT`
- [mashadab/hyperbolic-infiltration-theory](https://github.com/mashadab/hyperbolic-infiltration-theory) - This repository contains codes for performing hyperbolic analysis in infiltration. The figures correspond to Shadab and Hesse's 2022 paper on "Gravity driven infiltration with the development of a… `★ 3` `MIT`
- [trulsmoholt/RichardsEquation](https://github.com/trulsmoholt/RichardsEquation) - No description provided. `★ 3` `no licence`
- [inkenbrandt/soil_heat](https://github.com/inkenbrandt/soil_heat) - package to calculate soil heat flux using temperature gradients and other approaches. `★ 2` `MIT`
- [Khadrawi/Physics-Informed-Neural-Networks-for-Estimation-of-Hydraulic-Conductivity](https://github.com/Khadrawi/Physics-Informed-Neural-Networks-for-Estimation-of-Hydraulic-Conductivity) - This repository contains the data used for the paper "Novel Physics Informed-Neural Networks for Estimation of Hydraulic Conductivity of Green Infrastructure as a Performance Metric by Solving… `★ 2` `MIT`
- [mariaw-hub/SMBM](https://github.com/mariaw-hub/SMBM) - A soil moisture balance model based on the FAO bucket approach to estimate soil water within a homogenous soil column. `★ 2` `no licence`
- [mashadab/VarSatFlow](https://github.com/mashadab/VarSatFlow) - VarSatFlow: A Variably Saturated groundwater Flow model to simulate large scale multidimensional problems proposed in Shadab and Hesse (2024), Advances in Water Resources, Elsevier. The repository… `★ 2` `MIT`
- [MrShuffle/RichardsEquation](https://github.com/MrShuffle/RichardsEquation) - No description provided. `★ 2` `GPL-2.0`
- [openalea-incubator/soiltemp](https://github.com/openalea-incubator/soiltemp) - No description provided. `★ 2` `custom licence`
- [radwinskis/GEE_UBM](https://github.com/radwinskis/GEE_UBM) - Package for performing spatially distributed Soil Water Balance Utah Basin Model (UBM) calculations entirely within Google Earth Engine (GEE). `★ 2` `MIT`
- [SolSeyoum/PixSWAB_v1](https://github.com/SolSeyoum/PixSWAB_v1) - pixel based soil water balance model. `★ 2` `GPL-2.0`
- [AmiciNoctis/Soil-Heat-Diffusion-Simulation](https://github.com/AmiciNoctis/Soil-Heat-Diffusion-Simulation) - Este repositório contém algoritmos em python para geração de gráficos para a análise da variação da temperatura do solo em relação ao periodo de e superfícies a difusão de calor no solo. `★ 1` `no licence`
- [arowley2/richards-aot](https://github.com/arowley2/richards-aot) - No description provided. `★ 1` `MIT`
- [charan-008/IrriSnap_Irrigation_advisory_Ujjain_MP](https://github.com/charan-008/IrriSnap_Irrigation_advisory_Ujjain_MP) - No description provided. `★ 1` `no licence`
- [David-Freebairn/HowwetPlus](https://github.com/David-Freebairn/HowwetPlus) - No description provided. `★ 1` `no licence`
- [David-Freebairn/Riskaware](https://github.com/David-Freebairn/Riskaware) - Four climate related analyses. `★ 1` `no licence`
- [eliasmassaro-hub/Finite-Elements-Richards-Equation](https://github.com/eliasmassaro-hub/Finite-Elements-Richards-Equation) - No description provided. `★ 1` `no licence`
- [FranciscoSoltermann/RichardsEquation-and-FlowInPorousMedia](https://github.com/FranciscoSoltermann/RichardsEquation-and-FlowInPorousMedia) - Numerical simulation of flow in porous media using the Richards Equation. Includes 1D/2D finite difference implementations, nonlinear models (Brooks–Corey), and analytical validation using Python. `★ 1` `no licence`
- [g-adopt/gwassess](https://github.com/g-adopt/gwassess) - Analytical Solutions for the Richards Equation in 2D and 3D Domains. `★ 1` `custom licence`
- [GuoSFPLab/PFAS-LEACH-Numerical-1D](https://github.com/GuoSFPLab/PFAS-LEACH-Numerical-1D) - PFAS-LEACH-Numerical-1D is the Tier 2 model of PFAS-LEACH, which is a one-dimensional numerical model for simulating variably saturated water flow and contaminant fate and transport in porous media… `★ 1` `custom licence`
- [HedgehogDonut/PyVadose](https://github.com/HedgehogDonut/PyVadose) - Python-based 1-D Richards equation solver for vadose zone infiltration, clogging, and water balance analysis. `★ 1` `GPL-3.0`
- [j-h-cui/Biochar-Soil-Moisture-Model](https://github.com/j-h-cui/Biochar-Soil-Moisture-Model) - No description provided. `★ 1` `no licence`
- [JonathanKless/Richards_Equation](https://github.com/JonathanKless/Richards_Equation) - Linearised Model. `★ 1` `no licence`
- [KamelSOUDANI/WaterBudgetModelingInAridRegions](https://github.com/KamelSOUDANI/WaterBudgetModelingInAridRegions) - Python, R and GEE codes (see links to GEE in R code) : Modeling soil water budget in Australia (Collab. PhD MD). `★ 1` `no licence`
- [MaritHendrickx/SWIM2](https://github.com/MaritHendrickx/SWIM2) - SWIM² is a Python framework for uncertainty-aware soil water balance modeling, enabling Bayesian parameter inference and real-time soil moisture prediction using sensor data. `★ 1` `GPL-3.0`
- [martina01natali/WCM_SWB_Irri](https://github.com/martina01natali/WCM_SWB_Irri) - A Water Cloud Model coupled to a Soil Water Balance model (WCM-SWB), calibrated per field with Bayesian MCMC (PyMC) against Sentinel-1 backscatter, to estimate irrigation from satellite data. `★ 1` `GPL-3.0`
- [mdekauwe/soil_drainage](https://github.com/mdekauwe/soil_drainage) - Check I have the Richards' equation working. `★ 1` `no licence`
- [mostafa-ghasemzadeh/SoilFlow1D](https://github.com/mostafa-ghasemzadeh/SoilFlow1D) - SoilFlow 1D is a Python-based desktop simulation tool for modeling 1D vertical water flow, solute transport, and heat transfer through layered soil profiles using the Richards equation with a GUI… `★ 1` `no licence`
- [OnurSahin20/Flux1Dpy](https://github.com/OnurSahin20/Flux1Dpy) - 1D Richard Solver without I/O handling under 500 line of code. `★ 1` `MIT`
- [oyeyemidamilola/samba-model](https://github.com/oyeyemidamilola/samba-model) - A Visualization tool for Runoff estimation of soil moisture using semi arid moisture balance technique. `★ 1` `MIT`
- [rodolfomssouza/SoilWPRDynamics](https://github.com/rodolfomssouza/SoilWPRDynamics) - Soil penetration modeling. `★ 1` `LGPL-3.0`
- [SiMokraneSIAD/PythonToolsForSoilScienceModeling](https://github.com/SiMokraneSIAD/PythonToolsForSoilScienceModeling) - This Python repository provides scientific modules for soil science applications, emphasizing soil moisture dynamics, infiltration, nutrient cycling, and soil respiration. `★ 1` `custom licence`
- [Vaassaa/heatConductOpt](https://github.com/Vaassaa/heatConductOpt) - Collection of codes used for calibration of soil heat conductivity of heat transport model through measured soil temperature data in three types of forest biomes. `★ 1` `no licence`
- [WaterlinePL/hmse-monorepo](https://github.com/WaterlinePL/hmse-monorepo) - No description provided. `★ 1` `MIT`
- [YasYeganeh/Richards-Equation-Code](https://github.com/YasYeganeh/Richards-Equation-Code) - This repository contains an example of water flow through a column of soil. The respective codes depict the soil moisture content of this soil column at any distance and at any given time. An… `★ 1` `no licence`
- [4SAnalyticsnModelling/ABAgSoilHydroTemp](https://github.com/4SAnalyticsnModelling/ABAgSoilHydroTemp) - Simple 1D Soil Moisture Temperature Simulator for Agricultural Areas in Alberta. `MIT`
- [AgriculturalModelExchangeInitiative/STICS_SNOW](https://github.com/AgriculturalModelExchangeInitiative/STICS_SNOW) - Snow process in STICS model. `MIT`
- [arihydro/Horton-Infiltration-Model](https://github.com/arihydro/Horton-Infiltration-Model) - The Horton infiltration model is an empirical equation that describes how the rate of water entering the soil decreases exponentially over time. `no licence`
- [Atieng/Hydrosense-Kenya](https://github.com/Atieng/Hydrosense-Kenya) - A Scientific Computing System for Smart Irrigation, Water Balance Simulation, and Climate-Aware Decision Support. `no licence`
- [balajissp/pyRZWQM](https://github.com/balajissp/pyRZWQM) - python translation of RZWQM model. `MIT`
- [blck04/irrigation_model](https://github.com/blck04/irrigation_model) - No description provided. `no licence`
- [celinooo360-art/zahle-irrigation](https://github.com/celinooo360-art/zahle-irrigation) - No description provided. `no licence`
- [chelseakmorris/SMR-Python](https://github.com/chelseakmorris/SMR-Python) - Soil Moisture Routing Model in Python. `no licence`
- [cojacoo/echoRD_model](https://github.com/cojacoo/echoRD_model) - The echoRD model (eco-hydrological particle model based on representative structured domains) is a hydrological model treating water as particles and simulating interactive advective and diffusive… `GPL-3.0`
- [Crop2ML-Catalog/Simplace_Soil_Temperature](https://github.com/Crop2ML-Catalog/Simplace_Soil_Temperature) - Simplace Soil temperature model component is transformed to Crop2ML and is made available for other platforms and different programming languages. `BSD-3-Clause`
- [David-Freebairn/Watbal2026](https://github.com/David-Freebairn/Watbal2026) - No description provided. `no licence`
- [david0811/pyWBM](https://github.com/david0811/pyWBM) - Python implementation of the soil moisture subroutine of the University of New Hampshire Water Balance Model (WBM). `GPL-3.0`
- [david0811/wbm_toy_model](https://github.com/david0811/wbm_toy_model) - Python scripts for reproducing WBM soil moisture submodule. `GPL-3.0`
- [dh565/HydroSoil_py](https://github.com/dh565/HydroSoil_py) - HydroSoil is a numerical model for soil-water flow simulations under construction. `no licence`
- [dmmf1g15/RichardsEquationSolution](https://github.com/dmmf1g15/RichardsEquationSolution) - No description provided. `no licence`
- [dpartalis/petrichor](https://github.com/dpartalis/petrichor) - Know when not to water — a CLI soil water balance for your garden, powered by free weather data. `MIT`
- [Edgar-Bello/dos-ojos](https://github.com/Edgar-Bello/dos-ojos) - No description provided. `no licence`
- [efthymios19/Hydrus_Phreeqc_coupling](https://github.com/efthymios19/Hydrus_Phreeqc_coupling) - No description provided. `GPL-3.0`
- [farah-y-sadoon/lethbridge-soil-moisture-model](https://github.com/farah-y-sadoon/lethbridge-soil-moisture-model) - No description provided. `no licence`
- [fatemekhamse12/Soil](https://github.com/fatemekhamse12/Soil) - This model simulates soil moisture and evapotranspiration time series. `no licence`
- [felipehuerta17/richards_mixed](https://github.com/felipehuerta17/richards_mixed) - Implementation of Richards Equation. `no licence`
- [FlorianHerz/SWM](https://github.com/FlorianHerz/SWM) - Soil Water Model für ArcGIS in Python. `no licence`
- [geekyifei/3D_richards_numpy](https://github.com/geekyifei/3D_richards_numpy) - 3D richards equation solver based on finite volume in lumpy. `no licence`
- [grimmjule/pinn_soil_water_model](https://github.com/grimmjule/pinn_soil_water_model) - Master's project on physics-informed machine learning for soil water modeling. `no licence`
- [gstinoco/Richards2D-DL](https://github.com/gstinoco/Richards2D-DL) - Reproducible time-conditioned U-Net surrogate for two-dimensional Richards-equation soil infiltration, with a qualified numerical reference, a 208-scenario corpus, locked evaluation, and portable… `custom licence`
- [hkzhao7/soil-moisture-sensing-and-modeling](https://github.com/hkzhao7/soil-moisture-sensing-and-modeling) - No description provided. `no licence`
- [HX-net/Soil_Water_Balance](https://github.com/HX-net/Soil_Water_Balance) - No description provided. `no licence`
- [javinoram/soil_heat_flow](https://github.com/javinoram/soil_heat_flow) - No description provided. `MIT`
- [jlschonlau-jpg/Richards-1d-Solver](https://github.com/jlschonlau-jpg/Richards-1d-Solver) - Code to run to numerically solve the Richards Equation to simulate water flowing through soil. `no licence`
- [jlschonlau-jpg/Richards-2d-Solver](https://github.com/jlschonlau-jpg/Richards-2d-Solver) - Numerical solver for 2d Richards Equation. `no licence`
- [juanpablodelafuente/EFV_solver](https://github.com/juanpablodelafuente/EFV_solver) - Processed benchmark data and reproduction scripts for the 1-D EFV Richards equation manuscript. `MIT`
- [juanpablodelafuente/richards-benchmark](https://github.com/juanpablodelafuente/richards-benchmark) - Benchmarking numerical solvers for the 1D Richards Equation. `no licence`
- [ksaurabh95/1D_RE](https://github.com/ksaurabh95/1D_RE) - Python based solver for 1D Richards Equation. `GPL-3.0`
- [ksaurabh95/1D_RE_Model_MonteCarlo](https://github.com/ksaurabh95/1D_RE_Model_MonteCarlo) - Code to run Monte Carlo simulation of python based 1D Richards Equation. `no licence`
- [ksaurabh95/richards_equation_numerical_model](https://github.com/ksaurabh95/richards_equation_numerical_model) - No description provided. `no licence`
- [Lagat27/HydroSense-Kenya](https://github.com/Lagat27/HydroSense-Kenya) - HydroSense-Kenya is a Python-based scientific computing project that models soil-water balance, estimates water deficits, simulates future soil moisture under climate uncertainty, and recommends… `no licence`
- [lee5226/daily-newhall-simulation-model](https://github.com/lee5226/daily-newhall-simulation-model) - Code for developing, running, and evaluating the Daily Newhall Simulation Model (D-NSM) for surface and rootzone soil moisture estimation. `BSD-3-Clause`
- [Li-N-K/SSMModel](https://github.com/Li-N-K/SSMModel) - Simplified Soil Moisture Model (SSMM) — a 1D, 5-layer soil water balance model using Darcy's Law and Richards' equation. `MIT`
- [lucashataishi/Soil-Moisture-Dynamics](https://github.com/lucashataishi/Soil-Moisture-Dynamics) - Simulation of soil moisture dynamics as a function of plant distribution and soil characteristics. `MIT`
- [mahdimohammadnezhad/PC-PTF_hydraulic_properties](https://github.com/mahdimohammadnezhad/PC-PTF_hydraulic_properties) - No description provided. `no licence`
- [mdfahimhasan/SWB_ETa_Irr](https://github.com/mdfahimhasan/SWB_ETa_Irr) - No description provided. `no licence`
- [merijn-smits/1D-FV-Soil-Moisture-Richards-equation](https://github.com/merijn-smits/1D-FV-Soil-Moisture-Richards-equation) - 1D finite soil moisture Richards equation as described in https://doi.org/10.1002/2015WR017126. `MIT`
- [MGuimaraes706/Deep-Drainage---Richards-Equations](https://github.com/MGuimaraes706/Deep-Drainage---Richards-Equations) - No description provided. `no licence`
- [Mohammed-khlifi/Wee-PINN-Richards](https://github.com/Mohammed-khlifi/Wee-PINN-Richards) - Physics-Informed Neural Network for the Richards equation. `no licence`
- [nikhilrajdeep/PTF_Retention_Curve](https://github.com/nikhilrajdeep/PTF_Retention_Curve) - Physics-constrained deep-ensemble pedotransfer functions (Classic VG, dry-end VG, PDI) for soil water retention, K(h), Ksat, FC/PWP/PAW — single soil or 100 m SOLUS maps of Florida. `MIT`
- [oakuoko1/IrrigationDecision-Dashboard](https://github.com/oakuoko1/IrrigationDecision-Dashboard) - Real-time irrigation scheduling dashboard using soil water balance and CWSI methodologies. `no licence`
- [Oluwatobi-coder/2D-Soil-Moisture-Infiltration-FDM](https://github.com/Oluwatobi-coder/2D-Soil-Moisture-Infiltration-FDM) - This project implements a Finite Difference numerical solver to model moisture transport in unsaturated porous media. This project simulates the radial expansion of a "wetting bulb" from a drip… `MIT`
- [percegd/hydrus-react](https://github.com/percegd/hydrus-react) - No description provided. `no licence`
- [pradeep2005/irrigation-environment-service](https://github.com/pradeep2005/irrigation-environment-service) - No description provided. `no licence`
- [pranjalanimesh/soil-water-simulation](https://github.com/pranjalanimesh/soil-water-simulation) - No description provided. `no licence`
- [regDaniel/richards_standalone](https://github.com/regDaniel/richards_standalone) - Solver for a saturation-form Richards'equation based on the approach of Schlemmer et al. (2018). `MIT`
- [RumiShishir/-soil-infiltration-model](https://github.com/RumiShishir/-soil-infiltration-model) - 1D soil water infiltration model with rainfall boundary conditions. `no licence`
- [S-Kanzari/vGFit-1.0](https://github.com/S-Kanzari/vGFit-1.0) - Fitting Soil Water Retention Curve using the van Genuchten Model. `GPL-3.0`
- [Sarah-Keghian/irrigation-mpc](https://github.com/Sarah-Keghian/irrigation-mpc) - This internship optimizes irrigation using MPC. Soil moisture dynamics are modeled in state-space, with bilinear terms linearized via McCormick envelopes to form a MILP solved with Gurobi.… `no licence`
- [Seline254/Hydro-Sense](https://github.com/Seline254/Hydro-Sense) - A scientific computing project using numerical methods and data analysis to optimize irrigation systems in Kenya. `no licence`
- [ShashankAnand1996/Climate-Smart-Irrigation](https://github.com/ShashankAnand1996/Climate-Smart-Irrigation) - Well-commented Python code to simulate crop growth and soil processes under different water management scenarios. `custom licence`
- [Shrinidhi064/soilHeatFlux_dynamics_modelling](https://github.com/Shrinidhi064/soilHeatFlux_dynamics_modelling) - No description provided. `no licence`
- [simreaney/thetaFlow](https://github.com/simreaney/thetaFlow) - A 1D and 2D Richards equation simulator for simulating catchment hydrological dynamics. `GPL-3.0`
- [solisgb/basic-swb](https://github.com/solisgb/basic-swb) - Water balance in soil. `GPL-3.0`
- [SouvikCSSL-UWM/fdm_richards_1D](https://github.com/SouvikCSSL-UWM/fdm_richards_1D) - Finite difference solution of 1D Richards' equation (head-based) using Picard iteration. Backward Euler for time, central difference for space, and Crank–Nicolson scheme for diffusion and advection.… `no licence`
- [SouvikCSSL-UWM/Richards_3D_FenicsX](https://github.com/SouvikCSSL-UWM/Richards_3D_FenicsX) - Simulates the 3D Richards Equation using FEniCSx with Picard iterations and 1-hour time steps. Hexahedral mesh data is interpolated onto a regular grid using cubic interpolation for post-processing… `no licence`
- [thestochasticman/TerraSim](https://github.com/thestochasticman/TerraSim) - No description provided. `MIT`
- [VaishnaviGhogare/Assignment-Dora](https://github.com/VaishnaviGhogare/Assignment-Dora) - No description provided. `no licence`
- [veethahavya-CU-cz/gwswex](https://github.com/veethahavya-CU-cz/gwswex) - No description provided. `custom licence`
- [WinnieMG-111/HydroSense-Kenya](https://github.com/WinnieMG-111/HydroSense-Kenya) - No description provided. `no licence`
- [xelywn/HydroSense-Kenya-Project](https://github.com/xelywn/HydroSense-Kenya-Project) - Scientific Computing and Irrigation Modeling Project. `MIT`
- [xfan-01/multilayer-soil-water-model](https://github.com/xfan-01/multilayer-soil-water-model) - Multi-layer Soil Water Model Based on Bidirectional Percolation. `no licence`
- [yangtianci-mailbox/SoftVG-PINN](https://github.com/yangtianci-mailbox/SoftVG-PINN) - No description provided. `MIT`
- [yangym58/Python-for-GPPDE](https://github.com/yangym58/Python-for-GPPDE) - This is a repository used to run the GPPDE method on Richards equation with sink term. `no licence`
- [Yongqiang100/richards-fenicsx](https://github.com/Yongqiang100/richards-fenicsx) - No description provided. `MIT`
- [ziyaddmaa/Green-Ampt-Infiltration-Model-Interactive-Simulator](https://github.com/ziyaddmaa/Green-Ampt-Infiltration-Model-Interactive-Simulator) - This project implements the Green-Ampt Infiltration Model, a physically-based hydrological model used to estimate water infiltration into soil over time. The model is widely used in soil science… `MIT`
- [Zulach/Hydrosense-Kenya](https://github.com/Zulach/Hydrosense-Kenya) - No description provided. `no licence`

<a id="soil-water-r"></a>

#### R

- [RobelTakele/AquaBEHER](https://github.com/RobelTakele/AquaBEHER) - Estimation and Prediction of Wet Season Calendar and Soil Water Balance for Agriculture. `★ 16` `GPL-3.0`
- [DrylandEcology/rSFSW2](https://github.com/DrylandEcology/rSFSW2) - rSFSW2: A R package to create soil water balance simulation experiment. `★ 8` `GPL-3.0`
- [johannaklpr/SoilHydrology-Temperature](https://github.com/johannaklpr/SoilHydrology-Temperature) - Model for Soil Hydrology and Soil Temperature. `★ 4` `no licence`
- [SiMokraneSIAD/RToolsForSoilScienceModeling](https://github.com/SiMokraneSIAD/RToolsForSoilScienceModeling) - An R-based repository for modeling and analyzing soil processes, integrating physics, hydrology, biogeochemistry, and erosion dynamics. `★ 3` `custom licence`
- [Verena-L/NEWRIAN_in_R](https://github.com/Verena-L/NEWRIAN_in_R) - The NEWRIAN method was originally written in Matlab and translated into R in 2020. The model is used to obtain soil hydraulic parameters from the measurement results of forest soil samples in the… `★ 3` `no licence`
- [gowusu/vadose](https://github.com/gowusu/vadose) - Estimations of soil water characteristics in the vadose zone. `★ 2` `no licence`
- [inyo-gov/pumping-management](https://github.com/inyo-gov/pumping-management) - soil-plant water balance, groundwater and pumping management. `★ 1` `MIT`
- [lotichydrological/soilwaterbalance](https://github.com/lotichydrological/soilwaterbalance) - A set of R functions that support computation of soil water balances and lagged groundwater return flows in response to agricultural irrigation. `★ 1` `MIT`
- [paulhegedus/SWSTM-1D](https://github.com/paulhegedus/SWSTM-1D) - Soil Water and Solute Transport Model - 1D. `★ 1` `no licence`
- [ZoeBov/SIMPLE_fun](https://github.com/ZoeBov/SIMPLE_fun) - No description provided. `★ 1` `custom licence`
- [aaloksk/SoilMoistureAnalysis](https://github.com/aaloksk/SoilMoistureAnalysis) - R scripts to compute PET using the Thornthwaite method and simulate soil moisture with a water balance model (Huang et al., 1993) from PRISM data. `MIT`
- [akleinhesselink/model_soil_moisture](https://github.com/akleinhesselink/model_soil_moisture) - No description provided. `GPL-3.0`
- [andrea261097/ACQUAOUNT-Farm](https://github.com/andrea261097/ACQUAOUNT-Farm) - No description provided. `no licence`
- [cran/soilhypfit](https://github.com/cran/soilhypfit) - :exclamation: This is a read-only mirror of the CRAN R package repository. soilhypfit — Modelling of Soil Water Retention and Hydraulic Conductivity Data. `no licence`
- [elias-nelson/infiltrastat](https://github.com/elias-nelson/infiltrastat) - Statistical tools for fitting and evaluating soil water infiltration models in R. `custom licence`
- [mgwalsh/WRC](https://github.com/mgwalsh/WRC) - Soil water retention models. `no licence`
- [ncss-tech/DSS-water-balance](https://github.com/ncss-tech/DSS-water-balance) - Dynamic Soil Survey - Water Balance. `no licence`
- [niranman/Water-Balance-Site-Based](https://github.com/niranman/Water-Balance-Site-Based) - Estimate soil water of a point at of an area of interest. `no licence`
- [rcichota/SoilTemperatureModels_inR](https://github.com/rcichota/SoilTemperatureModels_inR) - Code to run soil temperature models from Crop2ML in R environment. `no licence`
- [Taakefyrsten/tidysoilwater](https://github.com/Taakefyrsten/tidysoilwater) - Tidy tools for Van Genuchten soil water retention and Mualem-Van Genuchten hydraulic conductivity modelling. `custom licence`
- [tommaso-martini/sm.drydowns.models](https://github.com/tommaso-martini/sm.drydowns.models) - DES and muSEC Models for Soil Moisture Drydowns (R implementation). `MIT`

<a id="soil-water-rust"></a>

#### Rust

- [Longitude103/soil_balance](https://github.com/Longitude103/soil_balance) - rust implementation of Hydrus-1D. `★ 1` `GPL-3.0`
- [muteNut/Rusteau-1D](https://github.com/muteNut/Rusteau-1D) - Rusteau-1D simulates one-dimensional water flow, heat transport and solute transport in variably saturated soils. It is a port of the numerical engine of HYDRUS-1D to Rust, with a desktop interface… `GPL-3.0`

<a id="soil-water-typescript"></a>

#### TypeScript

- [aliyan212/AgriTwin](https://github.com/aliyan212/AgriTwin) - Combines satellite vegetation observations, real-time agrometeorology, Saxton-Rawls soil physics, canal rotational rights (Warabandi), and thermal crop phenology into a bilingual Punjabi/English… `★ 1` `custom licence`
- [FabioSeixas/SoilWaterBalance](https://github.com/FabioSeixas/SoilWaterBalance) - The server side part of an app to easily get data from INMET API and use it for soil water balance analysis. `★ 1` `no licence`
- [ldor80/soil-moisture-simulation-fullStack](https://github.com/ldor80/soil-moisture-simulation-fullStack) - An interactive web application for simulating and visualizing soil moisture dynamics. `★ 1` `no licence`
- [fuleinist/soak](https://github.com/fuleinist/soak) - Garden watering advisor: tracks soil-water deficit from free weather data, and advises when to water, how long, and when rain makes watering pointless. `MIT`
- [OpenATK/sswab-js](https://github.com/OpenATK/sswab-js) - No description provided. `no licence`

<a id="soil-water-other"></a>

#### Other

- [Parfait0123/AquaTwin-Drip](https://github.com/Parfait0123/AquaTwin-Drip) - No description provided. `★ 2` `no licence`
- [PublicDomainRelease/Hydrus-1D](https://github.com/PublicDomainRelease/Hydrus-1D) - (non-official) Finite element model for simulating the 1D movement of water, heat, and multiple solutes in variably saturated media. `★ 2` `no licence`
- [skp703/SMITUV](https://github.com/skp703/SMITUV) - System Dynamic Modelling of Infiltration, Solute Transport, and Root Water Uptake in Vadose Zone. `★ 2` `GPL-3.0`
- [AgriHarmony/Soilphia](https://github.com/AgriHarmony/Soilphia) - An interactive computation model of solving 1d Richard equation for evaluation drip-irrigation management. `★ 1` `no licence`
- [kuntalnr/soil_water](https://github.com/kuntalnr/soil_water) - This is an implementation of a simple 1-D soil water balance. `★ 1` `GPL-3.0`
- [NayumShaikh/IIT](https://github.com/NayumShaikh/IIT) - A Java-based simulator for daily soil water balance during the Kharif season. Supports deep and shallow soils using rainfall data to compute runoff, crop uptake, soil moisture, and groundwater… `★ 1` `no licence`
- [ubcgif/2018-cockett-etal-computers-geosciences](https://github.com/ubcgif/2018-cockett-etal-computers-geosciences) - Fluid flow in the vadose zone, governed by the Richards equation, requires characterizing hydraulic properties using direct and proxy measurements. We present an efficient inversion technique for… `★ 1` `no licence`
- [Amithgowdaa/pinn-for-soil](https://github.com/Amithgowdaa/pinn-for-soil) - This repository explores the application of PINNs to model and solve soil heat diffusion equations. Please note that this is currently an experimental/test repository. I welcome any feedback, bug… `MIT`
- [AndrewBierer-USDA/SoilWaterRetentionCurveEstimateFunction](https://github.com/AndrewBierer-USDA/SoilWaterRetentionCurveEstimateFunction) - Uses arguments of soil texture to generate a soil water retention curve with help from the Rosetta 3 model to generate Van Genuchten hydraulic parameters according to texture. `MIT`
- [butlerm0405/uncertainty-in-boundary-values-Richards-Equation](https://github.com/butlerm0405/uncertainty-in-boundary-values-Richards-Equation) - No description provided. `no licence`
- [cauwzj/VaporModelExamples](https://github.com/cauwzj/VaporModelExamples) - Examples in "Modeling vapor transfer in soil water and heat simulations: A modularized, partially-coupled approach". `no licence`
- [chelseakmorris/SMR-R](https://github.com/chelseakmorris/SMR-R) - Soil Moisture Routing Model. `no licence`
- [ChengWeiHuang1206/Groundwater-vadose-zone-plant-atmosphere-continuum-model](https://github.com/ChengWeiHuang1206/Groundwater-vadose-zone-plant-atmosphere-continuum-model) - Groundwater-vadose zone-plant-atmosphere continuum (GVPAC) model. `GPL-3.0`
- [christophherbert/SoilMoisture](https://github.com/christophherbert/SoilMoisture) - Soil moisture model. `no licence`
- [daisy-model/richards-equation](https://github.com/daisy-model/richards-equation) - Solvers for Richards' equation. `GPL-3.0`
- [egraham/FFT_and_Soil_Temperatures](https://github.com/egraham/FFT_and_Soil_Temperatures) - R Shiny script to visualize and model sub-surface soil temperatures. `no licence`
- [garg4466/Phytodesalination_in_agroecosystems_codes](https://github.com/garg4466/Phytodesalination_in_agroecosystems_codes) - This repository provides the MATLAB code used for the analyses presented in the accepted Water Resources Research manuscript titled “Phytodesalination in Water Limited Agroecosystems: Effects of… `no licence`
- [gokgozragip-creator/konya-tarim-dijital](https://github.com/gokgozragip-creator/konya-tarim-dijital) - Konya'da Tarım Artık Dijital - Richards Denklemi Penman-Monteith van Genuchten &#124; Fizik Tabanlı Akıllı Sulama Sistemi. `MIT`
- [javrugt/Infiltration](https://github.com/javrugt/Infiltration) - Codes and data of 2021 Vadose Zone Journal papers. `no licence`
- [jl-pkgs/Richards_Equation.jl](https://github.com/jl-pkgs/Richards_Equation.jl) - No description provided. `no licence`
- [koondax/Aposteriori](https://github.com/koondax/Aposteriori) - A posteriori error estimate code for the Richards equation (Nonlinear degenerate evolution equation). `no licence`
- [Nasrin1234567/Data-Codes-Soil-temperature-modeling-at-deep-layers-for-estimation-of-active-soil-zone-depth](https://github.com/Nasrin1234567/Data-Codes-Soil-temperature-modeling-at-deep-layers-for-estimation-of-active-soil-zone-depth) - No description provided. `no licence`
- [pks19/Richards_equation](https://github.com/pks19/Richards_equation) - Matlab Script for solving stochastic Richards Equation used in the paper: A parametric acceleration of multilevel Monte Carlo convergence for nonlinear variably saturated flow… `no licence`
- [simpeg-research/cockett_2018_richards_inversion](https://github.com/simpeg-research/cockett_2018_richards_inversion) - Efficient 3D inversions for the Richards equation. `no licence`

<a id="soil-nutrients"></a>

### Soil carbon, nitrogen and nutrients

<a id="soil-nutrients-assembly"></a>

#### Assembly

- [ASMHSE/RothC-in-Assembly](https://github.com/ASMHSE/RothC-in-Assembly) - Rothamsted Carbon Model (RothC) Simulator. `★ 1` `Apache-2.0`

<a id="soil-nutrients-cplusplus"></a>

#### C++

- [cropmodels/Rquefts](https://github.com/cropmodels/Rquefts) - No description provided. `★ 3` `GPL-3.0`
- [domwoolf/somic1](https://github.com/domwoolf/somic1) - No description provided. `★ 3` `GPL-3.0`
- [ktoddbrown/decomPower](https://github.com/ktoddbrown/decomPower) - A soil carbon model power study. `★ 3` `MIT`
- [philippkraft/decomp](https://github.com/philippkraft/decomp) - A four component soil organic matter decomposition model. `★ 2` `MIT`
- [cran/sorcering](https://github.com/cran/sorcering) - :exclamation: This is a read-only mirror of the CRAN R package repository. sorcering — Soil Organic Carbon and CN Ratio Driven Nitrogen Modelling Framework. `★ 1` `no licence`
- [adityain2003/2DSOIL_PHREEQCRM_PUBLICATION](https://github.com/adityain2003/2DSOIL_PHREEQCRM_PUBLICATION) - This Repository hosts 2Dsoil-PhreeqcRM integrated model along with three validation studies. `Unlicense`
- [adityain2003/EGU-2026---Adding-reactive-transport-capabilities-to-the-2DSOIL-model-by-integrating-PhreeqcRM](https://github.com/adityain2003/EGU-2026---Adding-reactive-transport-capabilities-to-the-2DSOIL-model-by-integrating-PhreeqcRM) - No description provided. `no licence`
- [CnrIacBaGit/In-Depth-Fractional-RothC](https://github.com/CnrIacBaGit/In-Depth-Fractional-RothC) - Solver for in-depth fractional-order RothC-based SOC dynamics model. `CC0-1.0`
- [USDA-ARS-ACSL/EGU-2026-Adding-reactive-transport-capabilities-to-the-2DSOIL-model-by-integrating-PhreeqcRM](https://github.com/USDA-ARS-ACSL/EGU-2026-Adding-reactive-transport-capabilities-to-the-2DSOIL-model-by-integrating-PhreeqcRM) - Companion code coupling the 2DSOIL soil model with PhreeqcRM for reactive transport (EGU 2026). `no licence`

<a id="soil-nutrients-fortran"></a>

#### Fortran

- [fmyuan/DAYCENT-HYDRUS](https://github.com/fmyuan/DAYCENT-HYDRUS) - DAYCENT coupled with 1-D HYDRUS. `★ 14` `no licence`
- [Rothamsted-Models/RothC_Code](https://github.com/Rothamsted-Models/RothC_Code) - RothC implementation for organic carbon turnover in topsoil. `★ 6` `Apache-2.0`
- [tarahudiburg/DayCent](https://github.com/tarahudiburg/DayCent) - DayCent code for ITEAM/Hudiburg et al. publications. `★ 6` `no licence`
- [bsulman/INTERFACE-model-experiment-synthesis](https://github.com/bsulman/INTERFACE-model-experiment-synthesis) - Code from soil carbon model-experiment synthesis project coming out of INTERFACE workshop. `★ 3` `MIT`
- [YASSOmodel/Yasso20](https://github.com/YASSOmodel/Yasso20) - No description provided. `★ 3` `GPL-3.0`
- [CALIPSO-MESC/MESC](https://github.com/CALIPSO-MESC/MESC) - A Fortran-based microbial-explicit soil carbon cycle model. `★ 2` `GPL-3.0`
- [YASSOmodel/YASSO15](https://github.com/YASSOmodel/YASSO15) - No description provided. `★ 2` `GPL-3.0`
- [wanggangsheng/MENDokw](https://github.com/wanggangsheng/MENDokw) - Microbial-ENzyme Decomposition (MEND) Model with Oklahoma Grassland Data. `★ 1` `no licence`
- [ecaas/MIMICSplus](https://github.com/ecaas/MIMICSplus) - This repo contains a model that simulates the decomposition of soil, and keep track of the carbon. `no licence`
- [flamholz/soil_diskin](https://github.com/flamholz/soil_diskin) - disordered kinetics for soil carbon. `MIT`
- [jvardilos/godaycent](https://github.com/jvardilos/godaycent) - my rewrite of the daycent model. `no licence`
- [Manojhariharan/Toymodel](https://github.com/Manojhariharan/Toymodel) - No description provided. `no licence`
- [model-library-pps/QUEFTS_archive](https://github.com/model-library-pps/QUEFTS_archive) - Archived Fortran QUEFTS: evaluation of native fertility of tropical soils and nutrient-limited yields. `custom licence`
- [YASSOmodel/Mycorrhizal-Yasso](https://github.com/YASSOmodel/Mycorrhizal-Yasso) - Yasso model version that incorporates arbuscular and ectomycorrhiza fractions as driver data. `no licence`

<a id="soil-nutrients-fst"></a>

#### FST

- [model-library-pps/RC-P_archive](https://github.com/model-library-pps/RC-P_archive) - RC-P: simple model of the long-term effect of phosphorus fertiliser on crop P uptake and yield. `custom licence`

<a id="soil-nutrients-javascript"></a>

#### JavaScript

- [cpchoudhary2024/agricarbon-platform](https://github.com/cpchoudhary2024/agricarbon-platform) - Field-scale screening of agricultural carbon contracts — soil carbon saturation (Hassink 1997) from USDA SSURGO and CDL, priced net of yield drag and cost-share. `no licence`
- [Fangelito/RothC](https://github.com/Fangelito/RothC) - RothC soil carbon model in JavaScript. `no licence`
- [Fangelito75/RothC_prueba](https://github.com/Fangelito75/RothC_prueba) - RothC_prueba. `no licence`
- [xwtylife-gif/fertilizer-model-site](https://github.com/xwtylife-gif/fertilizer-model-site) - Static web prototype of a lightweight daily crop management model inspired by DNDC (Chinese). `no licence`

<a id="soil-nutrients-matlab"></a>

#### MATLAB

- [bsulman/FUN-CORPSE](https://github.com/bsulman/FUN-CORPSE) - Coupled model of plant nitrogen demand and rhizosphere carbon allocation (FUN) and soil SOM cycling (CORPSE). `★ 10` `no licence`
- [3100362274/STEMMUS-N](https://github.com/3100362274/STEMMUS-N) - Crop rooting depth acts a hydraulic lever mediating the fate of deep legacy nitrate. `★ 1` `MIT`
- [gj221/T-C-SMEW-N-v1.0](https://github.com/gj221/T-C-SMEW-N-v1.0) - No description provided. `no licence`
- [kevin-wallington/ReachabilitySoilP](https://github.com/kevin-wallington/ReachabilitySoilP) - Reachability code for agricultural soil phosphorus model. `MIT`

<a id="soil-nutrients-python"></a>

#### Python

- [mishagrol/pyRothC](https://github.com/mishagrol/pyRothC) - python version of RothC 26.3 Soil Carbon Model. `★ 24` `CC0-1.0`
- [Rothamsted-Models/RothC_Py](https://github.com/Rothamsted-Models/RothC_Py) - RothC code in Python language. `★ 18` `Apache-2.0`
- [DEMENT-Model/DEMENTpy](https://github.com/DEMENT-Model/DEMENTpy) - A spatially explicit trait- and individual-based microbial systems modelling framework. `★ 16` `MIT`
- [MatteoBertagni/SMEW](https://github.com/MatteoBertagni/SMEW) - Soil Model for Enhanced Weathering (SMEW): a dynamic, depth-averaged ecohydrological and biogeochemical model for enhanced weathering dynamics in the upper soil layers. `★ 8` `AGPL-3.0`
- [bsulman/CORPSE-N](https://github.com/bsulman/CORPSE-N) - Code for microbe/mineral/rhizosphere model of plant-mycorrhizal-soil interactions. `★ 5` `no licence`
- [Andros78/Easy_Roth_Carbon](https://github.com/Andros78/Easy_Roth_Carbon) - Easy to use Roth Carbon model that predicts soil carbon emission and soil carbon stocks dynamics. `★ 4` `GPL-3.0`
- [flathers/soilCarbonFramework](https://github.com/flathers/soilCarbonFramework) - Code to accompany the paper 'Building an Open Science Framework to Model Soil Organic Carbon'. `★ 4` `MIT`
- [Plant-Root-Soil-Interactions-Modelling/KEYLINK](https://github.com/Plant-Root-Soil-Interactions-Modelling/KEYLINK) - In the KEYLINK model, we integrate new knowledge on soil structure and its importance for soil organic matter (SOM) stabilisation and hydrology, with the existing concepts on SOM pools, and elements… `★ 4` `GPL-3.0`
- [behrambzkrr/agricultural-nitrogen-simulation](https://github.com/behrambzkrr/agricultural-nitrogen-simulation) - A 5-compartment ODE-based simulation of the nitrogen cycle in agriculture using Python, Scipy, and Matplotlib. Includes scenario analyses for fertilizer efficiency and soil health. `★ 3` `MIT`
- [Hamza-Kamil/Transfer-Learning-PINN-Nitrogen](https://github.com/Hamza-Kamil/Transfer-Learning-PINN-Nitrogen) - No description provided. `★ 3` `no licence`
- [JariLiski/Yasso15](https://github.com/JariLiski/Yasso15) - Yasso15 soil carbon model. `★ 3` `custom licence`
- [Plant-Food-Research-Open/FieldNBalance](https://github.com/Plant-Food-Research-Open/FieldNBalance) - Nitrogen balance model components and test procedures. `★ 3` `GPL-3.0`
- [vivas24/centurypy](https://github.com/vivas24/centurypy) - Library to train and run the CENTURY (Soil Organic Matter) model. `★ 3` `MIT`
- [bsulman/CORPSE_rhizosphere_Moore_etal_2019](https://github.com/bsulman/CORPSE_rhizosphere_Moore_etal_2019) - Model code for rhizosphere simulations using in Moore et al (2019) manuscript. `★ 2` `MIT`
- [MANADIP/ERW_Reactive_Transport_Model](https://github.com/MANADIP/ERW_Reactive_Transport_Model) - PHREEQC geochemical modeling of Enhanced Rock Weathering in Darjeeling tea plantations for carbon removal quantification and agricultural soil enhancement. `★ 2` `MIT`
- [Abdul-Gwadabe/Soil_CN_Model](https://github.com/Abdul-Gwadabe/Soil_CN_Model) - Educational and exploratory soil carbon–nitrogen cycling model linking soil processes, crop growth, and climate scenarios in Python. `★ 1` `MIT`
- [CnrIacBaGit/NSRothC](https://github.com/CnrIacBaGit/NSRothC) - NSRothC - NonStandard RothC models. `★ 1` `no licence`
- [deepikanijwala-ui/rothc-soil-carbon-model](https://github.com/deepikanijwala-ui/rothc-soil-carbon-model) - No description provided. `★ 1` `no licence`
- [JariLiski/yasso07ui](https://github.com/JariLiski/yasso07ui) - Automatically exported from code.google.com/p/yasso07ui. `★ 1` `no licence`
- [mainearth/DLCM](https://github.com/mainearth/DLCM) - Codes for the process-oriented soil carbon model—Double Layer Carbon Model. `★ 1` `GPL-3.0`
- [rasmuse/bnf-faostat](https://github.com/rasmuse/bnf-faostat) - No description provided. `★ 1` `MIT`
- [andresf5/codigos_modelos_agronomico](https://github.com/andresf5/codigos_modelos_agronomico) - En este repositorio se encuentran los codigos desarrollados para el modelo agronomico para disponibilidad de nitrogeno en cultivos de cafe en colombia. `no licence`
- [ArjunChakrawal/chemodiv-litter-model](https://github.com/ArjunChakrawal/chemodiv-litter-model) - Python codebase for simulating litter decomposition dynamics using molecular-level input traits, with support for flexible substrate and microbial representations. `MIT`
- [BerheAA/Integrated-Crop-Legume-Livestock--N-balance-in-Ethiopia_v1](https://github.com/BerheAA/Integrated-Crop-Legume-Livestock--N-balance-in-Ethiopia_v1) - Crop-Legume-Livestock-Nitrogen Balance. `no licence`
- [eliottelin/soc](https://github.com/eliottelin/soc) - No description provided. `no licence`
- [frankP-92/RothCpy-AFM](https://github.com/frankP-92/RothCpy-AFM) - RothCpy-AFM: A Python version of the RothC model accounting for different C-input sources in agricultural and agroforestry systems across diverse pedoclimatic conditions. `custom licence`
- [huangysmile/ORCHIMIC](https://github.com/huangysmile/ORCHIMIC) - a microbe-driven model for soil organic matter decomposition designed for large-scale applications. `no licence`
- [jjpantano/EWmodel](https://github.com/jjpantano/EWmodel) - Model for Enhanced Weathering (EW) dynamics in the soil upper layers. `BSD-3-Clause`
- [leizhang-geo/SoilProcMod](https://github.com/leizhang-geo/SoilProcMod) - This repository contains the code of mechanistic (process-based) models for simulating soil carbon dynamics. `no licence`
- [Lianlei66/Model-structures-determine-the-distribution-of-soil-carbon-age](https://github.com/Lianlei66/Model-structures-determine-the-distribution-of-soil-carbon-age) - all codes about the age paper. `no licence`
- [LukeEcomod/SimplePeat](https://github.com/LukeEcomod/SimplePeat) - Simple mass-conserving model for drained peatland soil C budget. Separates young post-drainage litter and mor layer from decomposition of old peat. Development goal: use in forest scenarios… `no licence`
- [mdw7fc/soil-n-carrying-capacity](https://github.com/mdw7fc/soil-n-carrying-capacity) - Code and data for: Soil feedback dynamics amplify the consequences of nitrogen supply disruptions (Wallenstein 2026, Nature Food). `no licence`
- [mihirobendre/RothC_VM42](https://github.com/mihirobendre/RothC_VM42) - Simplifying the RothC SOC model for implementation under Verra's VM0042 methodology, by including Weihermuller's pedotransfer functions, with project and baseline scenario runs in a single script… `no licence`
- [mihirobendre/RothC_without_inputs](https://github.com/mihirobendre/RothC_without_inputs) - This version of RothC defines input parameters w/in code itself, w/out relying on external input datasheets, which is useful if inputs stay constant from year-to-year (e.g. in future-projections). `no licence`
- [mms-boku/vsomm2-modeler](https://github.com/mms-boku/vsomm2-modeler) - Stand-alone version of the Vienna Soil-Organic-Matter Modeler. `no licence`
- [nkz-os/nkz-module-carbon](https://github.com/nkz-os/nkz-module-carbon) - Carbon sequestration and biomass analytics module for Nekazari platform. LUE-based GPP/NPP with RothC soil carbon, Verra VM0042 MRV. `AGPL-3.0`
- [pihchikk/bmi-soc-model](https://github.com/pihchikk/bmi-soc-model) - Four-pool energy-limited soil organic carbon model, with a BMI 2.0 wrapper. `MIT`
- [ShashankAnand1996/SMEW_SS](https://github.com/ShashankAnand1996/SMEW_SS) - This repository contains SMEW_SS, an extension of the SMEW model that simulates enhanced weathering processes while accounting for soil structure and rock powder mixing. `custom licence`
- [shenzhou1120/Zinc-enriched-rice-minimal](https://github.com/shenzhou1120/Zinc-enriched-rice-minimal) - No description provided. `no licence`
- [ShibliSadik/T-dependence-of-Fe-redox](https://github.com/ShibliSadik/T-dependence-of-Fe-redox) - Quantifying temperature dependence of Fe reduction in humid tropical soils: a Bayesian model-data integration. `no licence`
- [SiyaShao/Myco-CORPSE](https://github.com/SiyaShao/Myco-CORPSE) - Myco-CORPSE: a soil carbon-nitrogen model with saprotrophs, ectomycorrhizal and arbuscular mycorrhizal fungi (Shao et al. 2023, Soil Biology and Biochemistry, doi:10.1016/j.soilbio.2023.109073). `MIT`
- [vcorcoro/EndoPotNitrogen](https://github.com/vcorcoro/EndoPotNitrogen) - plant growth model incorporating nitrogen dynamics and biological nitrogen fixation from endophytes. `no licence`
- [voltAntonio/rothCStandAlone](https://github.com/voltAntonio/rothCStandAlone) - a stand alone version of RothC written in C++. `no licence`
- [YASSOmodel/Yasso-GUI](https://github.com/YASSOmodel/Yasso-GUI) - Yasso07, Yasso15 and Yasso20 graphical UI for Windows. `no licence`
- [YYC-JNU/Soil-SCM](https://github.com/YYC-JNU/Soil-SCM) - Just for fun. `no licence`

<a id="soil-nutrients-r"></a>

#### R

- [MPIBGC-TEE/SoilR](https://github.com/MPIBGC-TEE/SoilR) - Development version of the SoilR package. `★ 34` `no licence`
- [LukeEcomod/SoilCarbon](https://github.com/LukeEcomod/SoilCarbon) - Soil Carbon models. `★ 13` `no licence`
- [climatefarmers/soil-modelling](https://github.com/climatefarmers/soil-modelling) - Modelling of Carbon in Soil. `★ 10` `no licence`
- [Rothamsted-Models/RothC_R](https://github.com/Rothamsted-Models/RothC_R) - RothC code in R language. `★ 6` `Apache-2.0`
- [Microbial-Explicit-Model/MEMC](https://github.com/Microbial-Explicit-Model/MEMC) - Microbial Explicit Model Consortium: an R package supporting exploration of microbial explicit soil carbon models. `★ 5` `custom licence`
- [MJDavoudabadi/Modelling-soil-carbon-Tarlee-and-Brigalow](https://github.com/MJDavoudabadi/Modelling-soil-carbon-Tarlee-and-Brigalow) - The codes of one, two, three and five-pool models of Tarlee and Brigalow along with the code of LFO-CV are provided. `★ 5` `no licence`
- [nmi-agro/BLN](https://github.com/nmi-agro/BLN) - Bodemindicatoren voor Landbouwgronden in Nederland. A soil quality assessment framework for application in the Netherlands. `★ 5` `GPL-3.0`
- [pik-piam/mrsoil](https://github.com/pik-piam/mrsoil) - Package contains soil organic carbon cycling model based on IPCC Guidelines 2019 for data prepared in the madrat universe. `★ 4` `LGPL-3.0`
- [malgren/CSNAPNI](https://github.com/malgren/CSNAPNI) - The Commodity-Specific Net Anthropogenic Phosphorus and Nitrogen Inputs (CSNAPNI) model is designed to estimate real and embodied N and P nutrient inputs to specific products, including crops, corn… `★ 3` `no licence`
- [nmi-agro/rotsee](https://github.com/nmi-agro/rotsee) - Simulation tool for soil organic carbon stocks in agricultural soils. `★ 3` `GPL-3.0`
- [cropmodels/limer](https://github.com/cropmodels/limer) - R package implementing lime requirement models. `★ 2` `GPL-3.0`
- [elisabruni/me4soc](https://github.com/elisabruni/me4soc) - User-friendly interface launching a multi-model ensemble to predict SOC stocks and GHG fluxes under climate, land-use and land management changes. `★ 2` `MIT`
- [katierocci/SSA_soils_workshop_models](https://github.com/katierocci/SSA_soils_workshop_models) - Combined Millenial and MIMICS model code for running AFSIS data. `★ 2` `no licence`
- [markeburton/Soil-Carbon-Dynamics](https://github.com/markeburton/Soil-Carbon-Dynamics) - This repository includes R code for SNAP (Ritchie 2014) and SNAPGRAZE (Ritchie 2020) soil carbon models with additional versions allowing for updated functionality, customizability, and additional… `★ 2` `GPL-3.0`
- [robertwbuchkowski/soil-food-webs-2020](https://github.com/robertwbuchkowski/soil-food-webs-2020) - A repository of soil food web theoretical models that calculate the flow of carbon and nitrogen through a soil food web. `★ 2` `no licence`
- [BrzostekEcologyLab/FUN-BioCROP-LIDET](https://github.com/BrzostekEcologyLab/FUN-BioCROP-LIDET) - Version of FUN-BioCROP model with LIDET-derived litter decomposition parameters. `★ 1` `BSD-3-Clause`
- [DSeitz/RothC-LUC](https://github.com/DSeitz/RothC-LUC) - repo of the RothC-LUC model described in Seitz et al (2025, EJSS). `★ 1` `GPL-3.0`
- [inrae/AMG_base](https://github.com/inrae/AMG_base) - AMG_base simulates topsoil organic carbon stock evolution in arable cropping systems. `★ 1` `custom licence`
- [jstreich/global_theoretical_soil_nutrient_availability_calculator](https://github.com/jstreich/global_theoretical_soil_nutrient_availability_calculator) - This script uses theoretical soil nutrient availability curves, temperature, pH, precipitation, and soil water concentration data to model raster maps of the 12 most important micro and macro… `★ 1` `no licence`
- [model-library-pps/QUEFTS](https://github.com/model-library-pps/QUEFTS) - Soil nutrient supply, crop uptake, and nutrient-limited yield calculations. `★ 1` `custom licence`
- [YASSOmodel/YASSO15-R](https://github.com/YASSOmodel/YASSO15-R) - YASSO15 written in R. `★ 1` `GPL-3.0`
- [aj-sykes92/msc-morocco-soil-c-modelling](https://github.com/aj-sykes92/msc-morocco-soil-c-modelling) - Repository for materials to build implementation of IPCC Tier 2 steady-state soil C model. Implementation designed for MSc EPM students to use to model soil C sequestration in Moroccan agricultural… `GPL-3.0`
- [AshBonner310/FOLD_complexity](https://github.com/AshBonner310/FOLD_complexity) - Taking a traditional Soil Carbon Model with First-Order Linear Decay kinetics and finding ways to reduce the complexity without accuracy. `no licence`
- [boristupek/Yasso07swcGMD23](https://github.com/boristupek/Yasso07swcGMD23) - Yasso07 soil carbon model coupled with the soil moisture function. `no licence`
- [BrzostekEcologyLab/CORPSE-LIDET](https://github.com/BrzostekEcologyLab/CORPSE-LIDET) - CORPSE version with LIDET derived litter decomposition parameters. `BSD-3-Clause`
- [DrRufiSalis/RothCO2](https://github.com/DrRufiSalis/RothCO2) - Functions to create variations of the RothC Model such as GWP100 with emissions delay or C tails to create dynamic C balances. `no licence`
- [Holinwj/Model-POC-MAOC](https://github.com/Holinwj/Model-POC-MAOC) - No description provided. `no licence`
- [ilhuber/bc-script](https://github.com/ilhuber/bc-script) - No description provided. `no licence`
- [ilmenichetti/Porous](https://github.com/ilmenichetti/Porous) - No description provided. `no licence`
- [ilmenichetti/YaYasso](https://github.com/ilmenichetti/YaYasso) - A collection of functions to run the Yasso model in use at LUKE Finland. `CC-BY-4.0`
- [LukeEcomod/SOCFramework](https://github.com/LukeEcomod/SOCFramework) - No description provided. `no licence`
- [mbask/fertplan](https://github.com/mbask/fertplan) - R package to compute fertilization plans for Nitrogen, Phosphorus, and Potassium. `no licence`
- [mjimenezmartinez/CDR_AlleyCropping_field](https://github.com/mjimenezmartinez/CDR_AlleyCropping_field) - Simulate carbon dynamics of an agroforestry field. `no licence`
- [model-library-pps/MINIPb_archive](https://github.com/model-library-pps/MINIPb_archive) - MINIPb: soil organic carbon decay model after Yang and Janssen (R). `custom licence`
- [model-library-pps/RC_KP_archive](https://github.com/model-library-pps/RC_KP_archive) - RC-KP model code (R) with input data for two datasets, from the WUR model library. `custom licence`
- [SoilTSSM/yasso15-1](https://github.com/SoilTSSM/yasso15-1) - Yasso15 soil carbon dynamics model. `no licence`
- [SurajMelkani/Soil-Carbon-Dynamics-Simulator-Model](https://github.com/SurajMelkani/Soil-Carbon-Dynamics-Simulator-Model) - n interactive Shiny application to compare multiple soil organic carbon model structures. `no licence`
- [waltscience/phytotron_model](https://github.com/waltscience/phytotron_model) - A new model for soil carbon, with ectomycorrhizal and saprotrophic fungal competition. `no licence`

<a id="soil-nutrients-other"></a>

#### Other

- [ehfmsilva/rCTOOL](https://github.com/ehfmsilva/rCTOOL) - rCTOOL documentation: soil organic carbon modelling in R, tutorials and function reference. `★ 1` `no licence`
- [KevColeman/RothC_Win2_1](https://github.com/KevColeman/RothC_Win2_1) - windows zip files for RothC (win2.1). `★ 1` `no licence`
- [BereketAssa714/scaling-octo-umbrella](https://github.com/BereketAssa714/scaling-octo-umbrella) - Computational modeling framework for rainfall-driven nitrate transport dynamics in agricultural watersheds using geospatial analysis and symbolic hydrological systems. `no licence`
- [cbiondo84/Yasso.c](https://github.com/cbiondo84/Yasso.c) - Yasso - Soil Carbon Model package in C language. `no licence`
- [fenfold/SOMPROF](https://github.com/fenfold/SOMPROF) - SOMPROF vertically explicit soil organic matter model. `MIT`
- [ghr0705/-the-source-labelled-soil-wheat-nitrogen-model](https://github.com/ghr0705/-the-source-labelled-soil-wheat-nitrogen-model) - `wheatNrobust` is the archived analysis package for the source-labelled soil–wheat nitrogen model used in *Guaranteeing wheat nitrogen acquisition to improve yield in a warming climate*. `no licence`
- [kovanhuissteden/Peatland-3.1](https://github.com/kovanhuissteden/Peatland-3.1) - Peatland is a soil carbon cycle model specifically developed for modelling peat carbon loss by peat drainage. It includes also CH4 emission to calculate trade-off betweeen rewetting of peat soils… `no licence`
- [YaxianCHEN/Simulation-and-Decision-Making-Platform-for-Soil-Carbon-Pool-Dynamics-Recovery-](https://github.com/YaxianCHEN/Simulation-and-Decision-Making-Platform-for-Soil-Carbon-Pool-Dynamics-Recovery-) - Transform the SOC dynamic model that only exists in static formulas/charts in the master's thesis into an interactive multi-scenario deduction tool. I led the hierarchical decomposition of the model… `no licence`
- [yousefha1373-max/Simulating-Soil-Phosphorus-Fractionations-and-Uptake](https://github.com/yousefha1373-max/Simulating-Soil-Phosphorus-Fractionations-and-Uptake) - This model simulates: The dynamics of soil phosphorus pools (solution, exchangeable, precipitated) Daily and cumulative plant uptake (in kg P ha⁻¹) How salinity (ECe) reduces uptake and alters P… `no licence`
- [yyhuang2016/matrix_orchidee](https://github.com/yyhuang2016/matrix_orchidee) - The matrix representation of ORCHIDEE/Century soil carbon module. `no licence`

<a id="greenhouse-gases"></a>

### Agricultural greenhouse gases

<a id="greenhouse-gases-c"></a>

#### C

- [erwanpersonne/SURFATM](https://github.com/erwanpersonne/SURFATM) - No description provided. `GPL-3.0`

<a id="greenhouse-gases-csharp"></a>

#### C#

- [GeoModelLab/breath-api](https://github.com/GeoModelLab/breath-api) - No description provided. `no licence`

<a id="greenhouse-gases-fortran"></a>

#### Fortran

- [SongHanxiong/TRIPLEX-GHG-model-N2O-cropland](https://github.com/SongHanxiong/TRIPLEX-GHG-model-N2O-cropland) - TRIPLEX-GHG model is a process-based biogeochemical model which is designed to simulate major green-house gas emissions (carbon dioxide, methane and nitrous oxide) from terrestrial ecosystems from… `★ 4` `GPL-3.0`

<a id="greenhouse-gases-gaml"></a>

#### GAML

- [ScriBanana/SahelFlux](https://github.com/ScriBanana/SahelFlux) - Agent-based and stock-flow model to assess the effect of crop-livestock integration on carbon balance in Sahel territories. `★ 3` `no licence`

<a id="greenhouse-gases-matlab"></a>

#### MATLAB

- [dobreecker/transient_soil_CO2_with_GW_exchange](https://github.com/dobreecker/transient_soil_CO2_with_GW_exchange) - This code uses a one-dimensional, transient state CO2 production-diffusion model to simulate the concentrations and stable carbon isotope compositions of soil CO2 profiles. It assumes gas-water… `no licence`

<a id="greenhouse-gases-python"></a>

#### Python

- [agstack/field-carbon-model](https://github.com/agstack/field-carbon-model) - Field-specific carbon model leveraging SMAP L4C. `★ 4` `Apache-2.0`
- [danmulat/GHG_WholeFarm](https://github.com/danmulat/GHG_WholeFarm) - No description provided. `no licence`
- [lesaullianachmadargito/paddy-emissions-microalgae](https://github.com/lesaullianachmadargito/paddy-emissions-microalgae) - IPCC Tier 1 CH4 and N2O model for rice paddies, testing whether microalgae biofertiliser actually reduces emissions (Teknofest TRNC 2025 finalist). `MIT`
- [lql820/coupled-HYDRUS-DNDC](https://github.com/lql820/coupled-HYDRUS-DNDC) - No description provided. `no licence`

<a id="greenhouse-gases-r"></a>

#### R

- [damian-oswald/process-rate-estimator](https://github.com/damian-oswald/process-rate-estimator) - A GitHub repository for the process rate estimator developed for the Sustainable Agroecosystems Group at ETH. `★ 5` `no licence`
- [alicialedo/PerennialsGHGs-Rcode](https://github.com/alicialedo/PerennialsGHGs-Rcode) - R code for the PerennialGHGPerennial-GHG: A generic allometric model to estimate biomass accumulation and greenhouse gas emissions in perennial food and bioenergy crops. `★ 1` `no licence`
- [mutyalusheshu/DNDC-GHG-Model](https://github.com/mutyalusheshu/DNDC-GHG-Model) - No description provided. `no licence`

<a id="greenhouse-gases-other"></a>

#### Other

- [BrianBGrant/DNDCv.CAN](https://github.com/BrianBGrant/DNDCv.CAN) - This is our development version of DNDCv.CAN. The model is under ongoing development. Please report issues. `★ 19` `no licence`
- [jzw787/DNDC-Biochar-CI](https://github.com/jzw787/DNDC-Biochar-CI) - A new version of DNDCv9.5, DNDC-Biochar-CI was developed by researchers in Hohai University. Biochar was added as a new type of manure, including different genres of parameters, C/N ratio, organic… `★ 6` `no licence`
- [GlobalResearchAllianceModelingPlatform/DNDC-CAN](https://github.com/GlobalResearchAllianceModelingPlatform/DNDC-CAN) - Development Version of the Canadian Version of DNDC for surface manure-slurry work. `no licence`
- [HOLOS-IE/HOLOS-IE-Releases](https://github.com/HOLOS-IE/HOLOS-IE-Releases) - Releases and installer of HOLOS-IE, a whole-farm greenhouse-gas model for Irish agriculture. `no licence`
- [junyuqi1984/SWAT-N2O](https://github.com/junyuqi1984/SWAT-N2O) - Century/Daycent-based soil N cycling and N2O emission model. `no licence`
- [lzu-NingChai/lzu-DNDC](https://github.com/lzu-NingChai/lzu-DNDC) - No description provided. `no licence`
- [sativa/DNDC-CLI-releases](https://github.com/sativa/DNDC-CLI-releases) - Command line version of DNDC. `custom licence`
- [sativa/FEAT](https://github.com/sativa/FEAT) - Farm Energy Analysis Tool (FEAT): whole-farm model of energy use and greenhouse-gas emissions of agricultural systems. `custom licence`
- [SumilThakrar/switchgrass_NH3](https://github.com/SumilThakrar/switchgrass_NH3) - Modelling NH3 emissions from potential switchgrass cultivars in the Upper Midwest. `no licence`

<a id="evapotranspiration"></a>

### Evapotranspiration and irrigation

<a id="evapotranspiration-ampl"></a>

#### AMPL

- [OliPerkins1987/dualsourcehybrid_ETmodel](https://github.com/OliPerkins1987/dualsourcehybrid_ETmodel) - This is a process-based model of evapotranspiration, developed in the PC raster spatial modelling environment. It is principally driven by the Penman-Monteith equations. `no licence`

<a id="evapotranspiration-c"></a>

#### C

- [NOAA-OWP/evapotranspiration](https://github.com/NOAA-OWP/evapotranspiration) - Basic Model Interface (BMI) for potential evapotranspiration (PET) functions. `★ 5` `Apache-2.0`
- [OpfinAI/safina](https://github.com/OpfinAI/safina) - Penman-Monteith simulation with drip irrigation. `★ 2` `MIT`
- [cloclacordis/FieldEdge-Evapotranspiration](https://github.com/cloclacordis/FieldEdge-Evapotranspiration) - C11 reference evapotranspiration (FAO-56 Penman–Monteith) kernel for embedded irrigation control. `AGPL-3.0`
- [jetuk/pypet](https://github.com/jetuk/pypet) - Python Potential Evapotranspiration functions. `MIT`
- [jmframe/bmi_et](https://github.com/jmframe/bmi_et) - BMI for evapotranspiration functions. `no licence`
- [natrucha/irrigation](https://github.com/natrucha/irrigation) - Calculates when to irrigate garden based on CIMIS evapotranspiration data. `GPL-3.0`
- [QXue529/generalized-PM-evaporation](https://github.com/QXue529/generalized-PM-evaporation) - Code accompanying the Generalized Penman‑Monteith evaporation paper. `no licence`
- [yxhu08/Smart_Irrigation_Assistant](https://github.com/yxhu08/Smart_Irrigation_Assistant) - This project presents a Smart Irrigation Assistant, a C-language–based system that helps farmers calculate water requirements for selected crops, determine suitable growing seasons, and adjust daily… `no licence`

<a id="evapotranspiration-csharp"></a>

#### C#

- [Crash777/EvapotranspirationCalculator](https://github.com/Crash777/EvapotranspirationCalculator) - A small library calculating evaportranspiration using Weather Underground API as a source. Uses formulae found here: http://edis.ifas.ufl.edu/pdffiles/ae/ae45900.pdf. Ported from a javascript… `no licence`
- [Crop2ML-Catalog/SQ_Energy_Balance](https://github.com/Crop2ML-Catalog/SQ_Energy_Balance) - This component allows to estimate crop canopy temperature and soil-plant energy fluxes. `BSD-3-Clause`
- [OptiAquaProject/OptiaquaV3](https://github.com/OptiAquaProject/OptiaquaV3) - No description provided. `no licence`

<a id="evapotranspiration-cplusplus"></a>

#### C++

- [dsval/rsplash](https://github.com/dsval/rsplash) - rsplash is the R implementation of the Simple process-led algorithms for simulating habitats (SPLASH v.2.0), which comprises robust formulations to compute energy and water fluxes. This R package… `★ 8` `no licence`
- [ufcg-lsd/fast-sebal](https://github.com/ufcg-lsd/fast-sebal) - proof of concept of a fast implementation of the SEBAL algorithm. `★ 1` `no licence`

<a id="evapotranspiration-clojure"></a>

#### Clojure

- [zalf-rpm/berest-core](https://github.com/zalf-rpm/berest-core) - Core components of BEREST, ZALF's irrigation scheduling model (Clojure). `MPL-2.0`

<a id="evapotranspiration-cuda"></a>

#### Cuda

- [SalmaGL/sebs-gpu](https://github.com/SalmaGL/sebs-gpu) - Collection of code and sample data to estimate Evapotranspiration (Evaporation + Transpiration) using meteorological and remote sensing data. The code make use of many cores available on NVIDIA GPUs. `★ 1` `no licence`
- [cilasmarques/landsat-evapo](https://github.com/cilasmarques/landsat-evapo) - No description provided. `no licence`
- [ufcg-lsd/sebal-rah-cycle](https://github.com/ufcg-lsd/sebal-rah-cycle) - Implemation of SEBAL Rah Cycle using CUDA-C. `no licence`
- [yanggis/sebs-gpu](https://github.com/yanggis/sebs-gpu) - SEBS--acutal evapotranspiration estimation. `no licence`

<a id="evapotranspiration-dart"></a>

#### Dart

- [derbila/bitirme_projesi](https://github.com/derbila/bitirme_projesi) - Bitki su tüketimin Penman-Monteith yöntemine göre belirlenmsini sağlayan program. `no licence`

<a id="evapotranspiration-elixir"></a>

#### Elixir

- [vegahu/et_faopenmon](https://github.com/vegahu/et_faopenmon) - Implementation of the FAO Penman-Monteith equation for determining reference evapotranspiration (ETo). `★ 3` `no licence`
- [brycejohnston/ex_eto](https://github.com/brycejohnston/ex_eto) - Elixir package for calculating reference/potential evapotranspiration (ETo). `★ 1` `MIT`

<a id="evapotranspiration-fortran"></a>

#### Fortran

- [beerelf/IDSCU](https://github.com/beerelf/IDSCU) - IDSCU - Integrated Decision Support Consumptive Use Model. The CU Model is a windows 95/98/NT interface with monthly and daily ET estimation methods, a soil moisture budget, water supply components… `★ 1` `no licence`
- [hieulel/CUPID](https://github.com/hieulel/CUPID) - Soil-Vegetation-Atmosphere-Temperature Model. `★ 1` `MIT`
- [prasanthvkrishna/PET](https://github.com/prasanthvkrishna/PET) - Estimate Potential EvapoTranspiration from WRF-Noah Output. `no licence`
- [smwesten-usgs/eagleman_actual_et](https://github.com/smwesten-usgs/eagleman_actual_et) - Fortran IV code from Eagleman (1971) for estimating potential and actual evapotranspiration. `CC0-1.0`
- [zambreski/dssat_kcb](https://github.com/zambreski/dssat_kcb) - DSSAT-CSM with a basal crop coefficient (Kcb) approach for evapotranspiration (Kansas State University). `no licence`

<a id="evapotranspiration-go"></a>

#### Go

- [jiayunwork-dotcom/et0-fao56](https://github.com/jiayunwork-dotcom/et0-fao56) - No description provided. `MIT`

<a id="evapotranspiration-go-template"></a>

#### Go Template

- [nodomain/ha-smart-irrigation](https://github.com/nodomain/ha-smart-irrigation) - 🌿 Smart Irrigation — ET-Based Scheduling for Home Assistant. `MIT`

<a id="evapotranspiration-groovy"></a>

#### Groovy

- [relifram/Hubitat-SprinklerSchedulePlusET](https://github.com/relifram/Hubitat-SprinklerSchedulePlusET) - An advanced irrigation scheduler, including evapotranspiration water requirement calculations. `no licence`

<a id="evapotranspiration-idl"></a>

#### IDL

- [wangshuaiszo/IFEM-ET-model-for-dual-source](https://github.com/wangshuaiszo/IFEM-ET-model-for-dual-source) - An Independent Framework-based Evapotranspiration Model (IFEM) for dual-source: from field to regional scale. `★ 7` `no licence`
- [dh565/Crop-RS-Met](https://github.com/dh565/Crop-RS-Met) - Crop RS-Met is a proximal sensing-based model for ET and soil water content for crops in IDL. `★ 1` `no licence`
- [amiralid/SEBAL_IDL](https://github.com/amiralid/SEBAL_IDL) - Script developed for estimating Evapotranspiration using SEBAL algorithm in IDL programing language. `no licence`
- [luis-olivera/SEBTools](https://github.com/luis-olivera/SEBTools) - Surface Energy Balance (SEB) methods (SSEBI, SEB1s,SEB4S,TSEB) and partitioning tools for surface variables (LST,albedo). `no licence`

<a id="evapotranspiration-java"></a>

#### Java

- [ufcg-lsd/saps-engine](https://github.com/ufcg-lsd/saps-engine) - No description provided. `★ 5` `GPL-3.0`
- [waltermaldonado/EVAPO](https://github.com/waltermaldonado/EVAPO) - Instantly estimate soil water loss worldwide! `★ 2` `no licence`
- [ufcg-lsd/SEBAL](https://github.com/ufcg-lsd/SEBAL) - SebalHelper. `★ 1` `no licence`
- [ConcettaDAmato/ETP-Lysimeter](https://github.com/ConcettaDAmato/ETP-Lysimeter) - Evapotranspiration model modified for the lysimeter in the Prospero component. Second version of the model with the split of evaporation and transpiration and a evaporation stress. `GPL-3.0`
- [geoframecomponents/BrokerGEO](https://github.com/geoframecomponents/BrokerGEO) - BrokerGEO is a Java-based modeling environment to split evapotranspiration flux according to the WHETGEO grid discretization. `GPL-3.0`

<a id="evapotranspiration-javascript"></a>

#### JavaScript

- [gee-hydro/gee_PML](https://github.com/gee-hydro/gee_PML) - Penman-Monteith-Leuning Evapotranspiration on GEE. `★ 96` `GPL-2.0`
- [et-brasil/geeSEBAL](https://github.com/et-brasil/geeSEBAL) - A new open source and web tool to estimate actual ET based on SEBAL model. `★ 50` `MIT`
- [hwestbrook/evapotranspiration_calculator](https://github.com/hwestbrook/evapotranspiration_calculator) - No description provided. `★ 7` `no licence`
- [jpkabala96/geeSSEBI](https://github.com/jpkabala96/geeSSEBI) - Google Earth Engine implementation of the S-SEBI surface energy balance model. Available both as GEE application and library. `★ 5` `Apache-2.0`
- [h-sharif/gee_aet_result_demo](https://github.com/h-sharif/gee_aet_result_demo) - Automatic actual evapotranspiration app developed in Google Earth Engine based on METRIC (Mapping Evapotranspiration with Internalized Calibration) algorithm and Landsat 8 imagery in my B.Sc. project. `★ 3` `GPL-3.0`
- [rae-hill/SEBAL_Drone_Process](https://github.com/rae-hill/SEBAL_Drone_Process) - Uses drone technology to calculate soil saturation. `★ 3` `MIT`
- [Abhishekvk04/KrishiJal](https://github.com/Abhishekvk04/KrishiJal) - KrishiJal - A Smart tool for Irrigation Scheduling and Soil Image Analysis. Bridges FAO-56 science with AI/ML for farmer-friendly irrigation. Sustainable water use, higher yields for small farmers. `★ 2` `MIT`
- [jasonnickel-org/smart-watering-system](https://github.com/jasonnickel-org/smart-watering-system) - Self-hosted smart irrigation controller for Rachio with ET-based soil moisture modeling, Ambient Weather/Open-Meteo fallbacks, MQTT/Home Assistant, and systemd automation. `★ 2` `MIT`
- [GreenDev-PR/Pragma](https://github.com/GreenDev-PR/Pragma) - Web irrigation scheduling tool. `★ 1` `no licence`
- [MaheshRautrao/Evapotranspiration-Web-App](https://github.com/MaheshRautrao/Evapotranspiration-Web-App) - No description provided. `★ 1` `no licence`
- [reliasdomi/riego-calc](https://github.com/reliasdomi/riego-calc) - Calculadora de evapotranspiración y riego para cultivos de México — FAO-56 Penman-Monteith. `★ 1` `no licence`
- [soilwater/etcrop](https://github.com/soilwater/etcrop) - A tool for estimating crop evapotranspiration based on canopy cover. `★ 1` `no licence`
- [soilwater/fdk](https://github.com/soilwater/fdk) - Soil water balance forecasting model based on the FAO 56 dual crop coefficient method. `★ 1` `MIT`
- [basantsayed058-web/field-et-lab](https://github.com/basantsayed058-web/field-et-lab) - A professional full-stack web application for crop evapotranspiration (ETc) calculations using weather, NDVI, soil moisture, and field-level calibration. `no licence`
- [brianpajares/smallholder-irrigation-scheduler](https://github.com/brianpajares/smallholder-irrigation-scheduler) - PWA beta FAO-56 para calendario de riego explicable de pequenos productores. `no licence`
- [chawboiii/fao56-scheduler](https://github.com/chawboiii/fao56-scheduler) - FAO-56 Penman-Monteith reference evapotranspiration calculator and irrigation scheduler, tuned for Mediterranean and North-African cropping systems. `MIT`
- [dgaust/sunsight](https://github.com/dgaust/sunsight) - Home Assistant integration that infers sky conditions - direct sun on a window, clear-sky index, and FAO-56 evapotranspiration - from a window light sensor, weather station and solar PV array. `MIT`
- [DHI-GRAS/forward-et](https://github.com/DHI-GRAS/forward-et) - Evapotranspiration model for FORWARD project :ear_of_rice:. `no licence`
- [ericwangjcu/waterbalancesimulation](https://github.com/ericwangjcu/waterbalancesimulation) - No description provided. `no licence`
- [foomoon/node-red-contrib-et](https://github.com/foomoon/node-red-contrib-et) - Node-RED module to calculate evapotranspiration. `MIT`
- [hejazyayman17-spec/syria-irrigation-platform](https://github.com/hejazyayman17-spec/syria-irrigation-platform) - «المنصة السورية لإدارة وجدولة الري — FAO-56 والموازنة المائية في منطقة الجذور». `no licence`
- [izworskic/national-garden-water](https://github.com/izworskic/national-garden-water) - National garden watering decision intelligence using weather, evapotranspiration, soil, crop stage and gardener inputs. `no licence`
- [Kavya-1507/Automated_Irrigation_scheduling_90](https://github.com/Kavya-1507/Automated_Irrigation_scheduling_90) - No description provided. `no licence`
- [knightfox789/Crop-Irrigation-scheduling](https://github.com/knightfox789/Crop-Irrigation-scheduling) - No description provided. `GPL-3.0`
- [luizz-neto/Saldo_de_Radiacao_GEE](https://github.com/luizz-neto/Saldo_de_Radiacao_GEE) - 🌍 Script em Google Earth Engine para processamento de imagens Landsat 8 — calcula albedo, NDVI, SAVI, IAF, emissividade, temperatura da superfície, fluxos radiativos e radiação líquida (Rn) para… `no licence`
- [mxnueel/riego](https://github.com/mxnueel/riego) - Calculadora de riego con el método FAO-56 Penman-Monteith: coeficientes de cultivo oficiales + pronóstico real del clima, sin servidor. `MIT`
- [remifabbri/ET0-Penman](https://github.com/remifabbri/ET0-Penman) - Calcul de l'évapotranspiration par la méthode de PENMAN-MONTEITH, module javascript. `MIT`
- [rinociardo/waterwise](https://github.com/rinociardo/waterwise) - No description provided. `no licence`
- [soilwater/dualkcstudio](https://github.com/soilwater/dualkcstudio) - Web app for modeling the soil water balance using the dual crop coefficient method. `MIT`
- [soilwater/etgo](https://github.com/soilwater/etgo) - A mobile-first crop ET applications for irrigation scheduling. `MIT`
- [soilwater/fieldcaster](https://github.com/soilwater/fieldcaster) - A soil water balance model based on the FAO-56. `no licence`
- [yedenov/water-demand-scenarios](https://github.com/yedenov/water-demand-scenarios) - Reproducible irrigation water-budget scenarios using crop coefficients and efficiency sensitivity. Research prototype with synthetic demo. `MIT`

<a id="evapotranspiration-julia"></a>

#### Julia

- [AquaPore/PenmanMonteithTimeStep.jl](https://github.com/AquaPore/PenmanMonteithTimeStep.jl) - No description provided. `MIT`
- [bgctw/ETPart.jl](https://github.com/bgctw/ETPart.jl) - Partitioning Evapotranspiration into Transpiration and Evaporation components. `MIT`
- [GlenHertz/Evapotranspiration.jl](https://github.com/GlenHertz/Evapotranspiration.jl) - Calculations for the ultimate sprinkler system. `custom licence`
- [ikawah799/transpiration_model](https://github.com/ikawah799/transpiration_model) - Canopy transpiration model based on Ikawa et al (2024, Plant, Cell & Environment). `no licence`

<a id="evapotranspiration-matlab"></a>

#### MATLAB

- [kaighin/ET](https://github.com/kaighin/ET) - Code for estimating ET using the alternative to the Penman-Monteith equation given in McColl et al. (2020, WRR). `★ 13` `MIT`
- [nishan3/LandModETmapper](https://github.com/nishan3/LandModETmapper) - The LandMOD ET mapper is a Matlab based GUI for implementation of SEBAL and METRIC models on Landsat and MODIS. `★ 12` `no licence`
- [samzipper/HRMET](https://github.com/samzipper/HRMET) - High Resolution Mapping of EvapoTranspiration (HRMET) energy balance model. `★ 9` `GPL-3.0`
- [kunlz/PT_JPL_global](https://github.com/kunlz/PT_JPL_global) - Global Terrestrial Evapotranspiration via PT_JPL model. `★ 7` `no licence`
- [ZhongenNiu/PT-JPL](https://github.com/ZhongenNiu/PT-JPL) - Priestly-Taylor Jet Propulsion Laboratory model. `★ 5` `Apache-2.0`
- [derek591/penman-monteith](https://github.com/derek591/penman-monteith) - Matlab scripts to calculate the Penman-Monteith Flux Estimates. `★ 1` `no licence`
- [pankajcivil/PotentialEvapotranspiration](https://github.com/pankajcivil/PotentialEvapotranspiration) - Codes for estimating Potential Evapotranspiration. `★ 1` `no licence`
- [Abay2392/FAO-56-Penman-Monteith-Reference-Evapotranspiration-ETo-Calculation-in-MATLAB](https://github.com/Abay2392/FAO-56-Penman-Monteith-Reference-Evapotranspiration-ETo-Calculation-in-MATLAB) - MATLAB code for FAO-56 Penman-Monteith reference evapotranspiration (ETo) estimation using meteorological observations. `no licence`
- [CenidRaspaRiego/Evapotranspiration](https://github.com/CenidRaspaRiego/Evapotranspiration) - Este repositorio contiene un scripts en MATLAB para estimar la **evapotranspiración real diaria (ETa diaria)** utilizando imágenes de ETa obtenidas en fechas específicas y valores diarios de… `no licence`
- [jingyi-bu/Gc-TSEB](https://github.com/jingyi-bu/Gc-TSEB) - No description provided. `no licence`
- [luis-olivera/FAO56models](https://github.com/luis-olivera/FAO56models) - Crop water balance model based on FAO56. Application to R3. `no licence`
- [luis-olivera/Irrigation_WB-EO](https://github.com/luis-olivera/Irrigation_WB-EO) - Simulate actual irrigation from FAO56-based model and Earth Observation data. `no licence`
- [QiangyuLi/SprinklerEvapotranspirationMATLAB](https://github.com/QiangyuLi/SprinklerEvapotranspirationMATLAB) - This repository implements the Frost & Schwalen nomograph for estimating water loss due to evaporation during sprinkler irrigation. `MIT`
- [yqh0610/ET](https://github.com/yqh0610/ET) - calculate reference evapotranspiration according to FAO56. `no licence`

<a id="evapotranspiration-ocaml"></a>

#### OCaml

- [nickapos/eto](https://github.com/nickapos/eto) - A small collection of python classes that can calculate among others thing the reference evaportranspiration according the corrected penman-monteith method. `★ 2` `GPL-3.0`

<a id="evapotranspiration-perl"></a>

#### Perl

- [noaa-nws-cpc/libperl-cpc-pet](https://github.com/noaa-nws-cpc/libperl-cpc-pet) - CPC::PET - Calculate potential evapotranspiration (PET). `custom licence`

<a id="evapotranspiration-php"></a>

#### PHP

- [allanglen/evapotrans-php](https://github.com/allanglen/evapotrans-php) - A PHP implementation of the United Nations Food and Agriculture Organization (FAO) Penman-Monteith evapotranspiration equation. `★ 6` `no licence`
- [Dispositif/evapotrans](https://github.com/Dispositif/evapotrans) - PHP library to calculate evapotranspiration (Penman-Monteith) from weather & agronomical datas. `★ 3` `LGPL-3.0`
- [open-agroclimate/php-refet](https://github.com/open-agroclimate/php-refet) - Reference Evapotranspiration (ET) Tool (pure PHP). `★ 2` `BSD-3-Clause`
- [fcorra/INIA_FAO56](https://github.com/fcorra/INIA_FAO56) - Implementation of FAO56 algorithm to estimate daily reference evapotranspiration. `no licence`
- [timanders22/LoxBerry-Plugin-Bewaesserung](https://github.com/timanders22/LoxBerry-Plugin-Bewaesserung) - Giessen nach Wasserbilanz statt nach Zeitplan - FAO-56 Penman-Monteith, herstellerneutrale Messwertquellen, Regenvorhersage. `MIT`

<a id="evapotranspiration-plpgsql"></a>

#### PLpgSQL

- [simobouzarki/seve-agtech](https://github.com/simobouzarki/seve-agtech) - 🌱 SEVE AgTech — Simulateur techno-économique agricole professionnel pour le Maroc. 47 cultures, 48 régions, FAO-56, FDA. 100% offline. `MIT`

<a id="evapotranspiration-python"></a>

#### Python

- [altmenorg/HAsmartirrigation](https://github.com/altmenorg/HAsmartirrigation) - Smart Irrigation custom component for Home Assistant. `★ 564` `MIT`
- [woodcrafty/PyETo](https://github.com/woodcrafty/PyETo) - Reference and potential evapotranspiration calculation routines. `★ 179` `BSD-3-Clause`
- [hectornieto/pyTSEB](https://github.com/hectornieto/pyTSEB) - Two-source energy balance calculations for vegetation evapotranspiration. `★ 172` `GPL-3.0`
- [pyet-org/pyet](https://github.com/pyet-org/pyet) - Reference and potential evaporation estimation methods in Python. `★ 166` `MIT`
- [kthorp/pyfao56](https://github.com/kthorp/pyfao56) - FAO-56 crop water use and irrigation calculations using dual coefficients. `★ 98` `custom licence`
- [kaust-halo/geeet](https://github.com/kaust-halo/geeet) - Evapotranspiration (ET) models for use in python and with integration into Google Earth Engine. `★ 68` `MIT`
- [Open-ET/openet-ssebop](https://github.com/Open-ET/openet-ssebop) - Earth Engine SSEBop ET Model. `★ 58` `Apache-2.0`
- [NASA-DEVELOP/METRIC](https://github.com/NASA-DEVELOP/METRIC) - For estimating daily evapotranspiration from Landsat data. `★ 55` `custom licence`
- [never-dry/NeverDry](https://github.com/never-dry/NeverDry) - Smart irrigation for Home Assistant — scientific water balance model with per-zone crop coefficients. `★ 55` `MIT`
- [sherzodr/penmon](https://github.com/sherzodr/penmon) - Implements weather station class in Python that calculates ETo (reference crop's evapotranspiration) based on UN-FAO Irrigation and Drainage Paper 56. `★ 41` `MIT`
- [jvdkwast/PySEBS](https://github.com/jvdkwast/PySEBS) - The Surface Energy Balance System (SEBS) in Python. `★ 39` `no licence`
- [WSWUP/pymetric](https://github.com/WSWUP/pymetric) - Python implementation of the METRIC model. `★ 37` `Apache-2.0`
- [Open-ET/openet-refet-gee](https://github.com/Open-ET/openet-refet-gee) - ASCE Standardized Reference Evapotranspiration Functions for Google Earth Engine (GEE). `★ 32` `Apache-2.0`
- [hectornieto/pyMETRIC](https://github.com/hectornieto/pyMETRIC) - Python code for Mapping EvapoTranspiration at high Resolution with Internalized Calibration model. `★ 30` `GPL-3.0`
- [TimHessels/SEBAL](https://github.com/TimHessels/SEBAL) - The Surface Energy Balance Algorithm for Land. `★ 30` `Apache-2.0`
- [rafatieppo/sebal](https://github.com/rafatieppo/sebal) - Python code to run SEBAL method. `★ 28` `BSD-3-Clause`
- [WSWUP/RefET](https://github.com/WSWUP/RefET) - ASCE Standardized Reference Evapotranspiration Functions. `★ 24` `Apache-2.0`
- [wateraccounting/PySEBAL_dev](https://github.com/wateraccounting/PySEBAL_dev) - Python implementation of SEBAL. `★ 23` `Apache-2.0`
- [Open-ET/openet-ptjpl](https://github.com/Open-ET/openet-ptjpl) - Earth Engine PT-JPL ET Model. `★ 20` `Apache-2.0`
- [wwolff7/SEBAL_GRASS](https://github.com/wwolff7/SEBAL_GRASS) - Script to calculate daily evapotranspiration for Landsat images in GRASS GIS 7.X. `★ 19` `no licence`
- [xlsadai/Potential-Evapotranspiration](https://github.com/xlsadai/Potential-Evapotranspiration) - 应用Penman-Monteith公式计算气象站的潜在蒸散发（PET）. `★ 19` `no licence`
- [JPL-Evapotranspiration-Algorithms/PT-JPL](https://github.com/JPL-Evapotranspiration-Algorithms/PT-JPL) - Priestley Taylor Jet Propulsion Laboratory (PT-JPL) Evapotranspiration Model Python Implementation. `★ 18` `Apache-2.0`
- [aquacropos/aquacrop-eto](https://github.com/aquacropos/aquacrop-eto) - Python package for calculating reference/potential evapotranspiration (ETo). `★ 17` `BSD-3-Clause`
- [avalero92/CropWater-RS](https://github.com/avalero92/CropWater-RS) - Remote Sensing-based Crop Water Requirement and Phenology Toolkit. `★ 15` `GPL-3.0`
- [et-brasil/openet-geesebal](https://github.com/et-brasil/openet-geesebal) - A new open source model based on the SEBAL (Surface Energy Balance Algorithm for Land) to estimate actual daily and monthly evapotranspiration using historical and recent Landsat images and global… `★ 15` `MIT`
- [Evapotranspiration/ETo](https://github.com/Evapotranspiration/ETo) - A Python package for calculating reference evapotranspiration. `★ 14` `Apache-2.0`
- [sciencebyAJ/PTJPL-1D](https://github.com/sciencebyAJ/PTJPL-1D) - Priestley-Taylor Jet Propulsion Laboratory Evapotranspiration Code for 1-dimensional implementation. `★ 14` `MIT`
- [JPL-Evapotranspiration-Algorithms/PT-JPL-SM](https://github.com/JPL-Evapotranspiration-Algorithms/PT-JPL-SM) - Priestley Taylor Jet Propulsion Laboratory Soil Moisture (PT-JPL-SM) Evapotranspiration Model Python Implementation. `★ 13` `Apache-2.0`
- [JPL-Evapotranspiration-Algorithms/STIC-JPL](https://github.com/JPL-Evapotranspiration-Algorithms/STIC-JPL) - Surface Temperature Initiated Closure (STIC) Evapotranspiration Model Python Implementation. `★ 11` `no licence`
- [agstack/OpenAgri-IrrigationManagement](https://github.com/agstack/OpenAgri-IrrigationManagement) - The IRM service does Evapotranspiration (ETo) calculations and Soil Moisture Analysis, depending on the specific data input. `★ 10` `EUPL-1.2`
- [arthur-e/MOD16](https://github.com/arthur-e/MOD16) - A Python implementation of the MOD16 terrestrial evapotranspiration algorithm. `★ 10` `custom licence`
- [Open-ET/openet-disalexi](https://github.com/Open-ET/openet-disalexi) - Earth Engine DisALEXI ET Model. `★ 10` `Apache-2.0`
- [montimaj/pyCropWat](https://github.com/montimaj/pyCropWat) - A Python Package for Computing Effective Precipitation Using Google Earth Engine Climate Data. `★ 8` `MIT`
- [Open-ET/openet-core](https://github.com/Open-ET/openet-core) - OpenET Core Components. `★ 8` `Apache-2.0`
- [WSWUP/WREVAP](https://github.com/WSWUP/WREVAP) - Operational Estimates of Areal Evapotranspiration and Lake Evaporation. `★ 8` `no licence`
- [Yilkalg3/SEBALIGEEpy](https://github.com/Yilkalg3/SEBALIGEEpy) - A python implementation of the open source Google Earth Engine based Surface Energy Balance Algorithm for Land (SEBALIGEE) model with improved high resolution land use and land cover data for… `★ 8` `no licence`
- [adrHuerta/Evaporation](https://github.com/adrHuerta/Evaporation) - collect code(s) to compute evaporation/evapotranspiration. `★ 7` `no licence`
- [FloEll/QWaterModel](https://github.com/FloEll/QWaterModel) - QWaterModel is a simple QGis plugin tool to calculate Evapotranspiration from thermal images. `★ 7` `GPL-3.0`
- [rslab-ntua/senet](https://github.com/rslab-ntua/senet) - Energy Balance model approach for crop water demand estimation. `★ 7` `GPL-3.0`
- [sbg-tir/SBG-TIR-L4-JET](https://github.com/sbg-tir/SBG-TIR-L4-JET) - Level 4 evapotranspiration (ET), evaporative stress index (ESI) and water use efficiency (WUE). `★ 6` `Apache-2.0`
- [akorkovelos/agrodem](https://github.com/akorkovelos/agrodem) - agrodem - a GIS based model on water and electricity requirements for ground and/or surface water irrigation. `★ 5` `MIT`
- [ECOSTRESS-Collection-3/ECOv003-L3T-L4T-JET](https://github.com/ECOSTRESS-Collection-3/ECOv003-L3T-L4T-JET) - ECOSTRESS Collection 3 JPL Evapotranspiration (JET) Product Generating Executable (PGE). `★ 5` `Apache-2.0`
- [edscos/Python-Code-to-Calculate-Daily-Actual-Evapotranspiration-Using-an-Aerodynamic-Temperature-Model](https://github.com/edscos/Python-Code-to-Calculate-Daily-Actual-Evapotranspiration-Using-an-Aerodynamic-Temperature-Model) - Python code to calculate actual daily evapotranspiration from an one-source surface energy balance approach using point-based data inputs. `★ 5` `no licence`
- [JPL-Evapotranspiration-Algorithms/PM-JPL](https://github.com/JPL-Evapotranspiration-Algorithms/PM-JPL) - JPL implementation of the MOD16 evapotranspiration remote sensing model. `★ 5` `Apache-2.0`
- [NMTHydro/RefET](https://github.com/NMTHydro/RefET) - Daily Penman-Monteith Reference ET. `★ 5` `no licence`
- [RAD-ET/radet-gee](https://github.com/RAD-ET/radet-gee) - RADET model (Radiation Advection Diffusivity-independent Evapotranspiration) for estimating actual evapotranspiration (ET). `★ 5` `Apache-2.0`
- [dgketchum/SSEBop](https://github.com/dgketchum/SSEBop) - Operational Simplified Surface Energy Balance Model. `★ 4` `no licence`
- [DHI/Sen-ET-OpenEO-toolbox](https://github.com/DHI/Sen-ET-OpenEO-toolbox) - This repository contains openEO workflows for various python modules used in Evapotranspiration (ET) modeling and Irrigation mapping. `★ 4` `GPL-3.0`
- [Hidrovales/Balanco_Hidrico](https://github.com/Hidrovales/Balanco_Hidrico) - Necessidades hídricas das culturas e consumo de água na irrigação. `★ 4` `no licence`
- [Hydrometeorological-Remote-Sensing/RS-SIF-T](https://github.com/Hydrometeorological-Remote-Sensing/RS-SIF-T) - code for the paper Modeling transpiration with sun-induced chlorophyll fluorescence observations via water-use efficiency and stomatal conductance methods. `★ 4` `MIT`
- [ikramelhazdour/Daily_TSEB_GEE_ET](https://github.com/ikramelhazdour/Daily_TSEB_GEE_ET) - A GEE TSEB Workflow for estimating Daily High Resolution (30m) fully Remote Sensing Evapotranspiration (ET). `★ 4` `AGPL-3.0`
- [JakubBrom/SEBCS](https://github.com/JakubBrom/SEBCS) - SEBCS for QGIS - Module for calculation of energy balance features and vegetation water stress indices. `★ 4` `GPL-3.0`
- [linuxha/EvapoTranspiration](https://github.com/linuxha/EvapoTranspiration) - Adaption of an OpenSprinker Penmen-Monteith ETO method Python script. `★ 4` `AGPL-3.0`
- [WSWUP/et-demands](https://github.com/WSWUP/et-demands) - Dual Crop Coefficient Evapotranspiration and Net Irrigation Water Requirement Model. `★ 4` `Apache-2.0`
- [collinsemmalise/Priestly_Taylor_Python_Implementation](https://github.com/collinsemmalise/Priestly_Taylor_Python_Implementation) - A python implementation of potential evapotranspiration modeling using the Priestly-Taylor equations. `★ 3` `no licence`
- [ET-Toolbox/ET-Toolbox-Product-Generator](https://github.com/ET-Toolbox/ET-Toolbox-Product-Generator) - Evapotranspiration Product Generator for the USBR-JPL Second Generation ET Toolbox. `★ 3` `no licence`
- [frankpc3/ET](https://github.com/frankpc3/ET) - Evapotranspiration: Homeseer adaptation of an ET script written in Python. `★ 3` `no licence`
- [JPL-Evapotranspiration-Algorithms/JET3](https://github.com/JPL-Evapotranspiration-Algorithms/JET3) - Jet Propulsion Laboratory Evapotranspiration Ensemble ECOSTRESS Collection 3. `★ 3` `Apache-2.0`
- [JPL-Evapotranspiration-Algorithms/SEBAL-soil-heat-flux](https://github.com/JPL-Evapotranspiration-Algorithms/SEBAL-soil-heat-flux) - Soil Heat Flux Remote Sensing Method from the Surface Energy Balance for Land (SEBAL) Evapotranspiration Model in Python. `★ 3` `Apache-2.0`
- [moienr/SEBAL](https://github.com/moienr/SEBAL) - Evapotranspiration Computation. `★ 3` `no licence`
- [Mosheur-Rahman/Evapotranspiration-calculation-with-penman-monteith-formula](https://github.com/Mosheur-Rahman/Evapotranspiration-calculation-with-penman-monteith-formula) - Basic Evapotranspiration calculation with penman-monteith formula for grass,trees and soil. `★ 3` `no licence`
- [RamiALBASHA/crop_energy_balance](https://github.com/RamiALBASHA/crop_energy_balance) - A model for simulating energy balance in the soil-crop-atmosphere continuum. `★ 3` `custom licence`
- [RNehara/Sentinel2_PET_ASCE_EWRI_Model.py](https://github.com/RNehara/Sentinel2_PET_ASCE_EWRI_Model.py) - Python script to estimate potential evapotranspiration (PET) using the Penman-Monteith FAO-52 method with ASCE-PM references (ASCE-EWRI) with Sentinel-2 L2A imagery. Includes NDVI and albedo… `★ 3` `MIT`
- [tuncaemre/ET-Estimation-BasedOn-EnergyBalance](https://github.com/tuncaemre/ET-Estimation-BasedOn-EnergyBalance) - Evapotranspiration estimation Based on Surface Energy Balance. `★ 3` `no licence`
- [UW-SASWE/sDRIPS](https://github.com/UW-SASWE/sDRIPS) - Satellite Data Rendered Irrigation Using Penman-Monteith and Sebal (sDRIPS) for Surface Water Irrigation Optimization. `★ 3` `GPL-3.0`
- [yoannMoreau/Evapo_GFS](https://github.com/yoannMoreau/Evapo_GFS) - calculate EVAPOTRANSPIRATION (Et0) from GFS data on a specific area and for a date within the last 14 days. `★ 3` `CC0-1.0`
- [AgriculturalModelExchangeInitiative/SQ_Energy_Balance](https://github.com/AgriculturalModelExchangeInitiative/SQ_Energy_Balance) - Model of Energy Balance of the crop growth simulation model SiriusQuality. `★ 2` `BSD-3-Clause`
- [dgketchum/etrm](https://github.com/dgketchum/etrm) - The EvapoTranspiration and Recharge Model. `★ 2` `Apache-2.0`
- [DHI-GRAS/eo4all-potential-et](https://github.com/DHI-GRAS/eo4all-potential-et) - Potential ET processor for ADB's EO4ALL project. `★ 2` `GPL-3.0`
- [DOI-BOR/et-demands](https://github.com/DOI-BOR/et-demands) - Dual crop coefficient crop water demand model. `★ 2` `no licence`
- [DrAldabsa/Irrigation_Scheduling_-App](https://github.com/DrAldabsa/Irrigation_Scheduling_-App) - برنامج يعنى باحتساب مقدار الري الدقيق للمحاصيل الزراعية. `★ 2` `no licence`
- [DroughtMonitor/Calculation-of-potential-evapotranspiration](https://github.com/DroughtMonitor/Calculation-of-potential-evapotranspiration) - 33 potential evapotranspiration models. `★ 2` `no licence`
- [ECOSTRESS-Collection-2/ECOv002-L3T-L4T-JET](https://github.com/ECOSTRESS-Collection-2/ECOv002-L3T-L4T-JET) - ECOSTRESS Collection 2 JPL Evapotranspiration (JET) Product Generating Executable (PGE). `★ 2` `Apache-2.0`
- [JPL-Evapotranspiration-Algorithms/daylight-evapotranspiration](https://github.com/JPL-Evapotranspiration-Algorithms/daylight-evapotranspiration) - Instantaneous/Daily Evapotranspiration Upscaling Utilities Python Package. `★ 2` `Apache-2.0`
- [JPL-Evapotranspiration-Algorithms/FLiESANN](https://github.com/JPL-Evapotranspiration-Algorithms/FLiESANN) - Forest Light Environmental Simulator (FLiES) Radiative Transfer Model Artificial Neural Network (ANN) Implementation in Python. `★ 2` `Apache-2.0`
- [JPL-Evapotranspiration-Algorithms/FLiESLUT](https://github.com/JPL-Evapotranspiration-Algorithms/FLiESLUT) - Forest Light Environmental Simulator (FLiES) Radiative Transfer Model Look-Up Table (LUT) Implementation in Python. `★ 2` `Apache-2.0`
- [JPL-Evapotranspiration-Algorithms/priestley-taylor](https://github.com/JPL-Evapotranspiration-Algorithms/priestley-taylor) - Priestley-Taylor Evapotranspiration Utilities in Python. `★ 2` `Apache-2.0`
- [Keerthykaushik/Evapotranspiration](https://github.com/Keerthykaushik/Evapotranspiration) - No description provided. `★ 2` `no licence`
- [licm13/ET-partition](https://github.com/licm13/ET-partition) - uWUE/PP/TEA 主要ET拆分方法对比和研究. `★ 2` `custom licence`
- [manish-111/CROP-WATER-REQUIREMENT-USING-DUAL-CROP-COEFFICIENT](https://github.com/manish-111/CROP-WATER-REQUIREMENT-USING-DUAL-CROP-COEFFICIENT) - This model is developed in python to calculate the crop water requirement using penman montieth equation and using dual crop coefficient. model also calculate the availabe water content in the soil… `★ 2` `no licence`
- [Nakooya/ET-Based-Irrigation](https://github.com/Nakooya/ET-Based-Irrigation) - Deficit Irrigation Scheduling System using Penman-Monteith Equation and Hargreaves Equation to Estimate Evapotranspiration. `★ 2` `no licence`
- [Open-ET/openet-sims](https://github.com/Open-ET/openet-sims) - Openet version of SIMS. `★ 2` `Apache-2.0`
- [pipe98/ETo-Estimation-Tool-](https://github.com/pipe98/ETo-Estimation-Tool-) - Python script to estimate Reference Evapotranspiration (ETo) using the FAO Penman-Monteith method. This tool includes a graphical user interface (GUI) and is designed for ease of use by agronomists… `★ 2` `MIT`
- [rdhungel/Single-source-Penman-Monteith](https://github.com/rdhungel/Single-source-Penman-Monteith) - Calculation of ET based on Penman Monteith with surface energy balance. `★ 2` `no licence`
- [thomasmcz/SEBAL_STARFM](https://github.com/thomasmcz/SEBAL_STARFM) - This script describes an application of SEBAL model combined with STARFM. `★ 2` `GPL-3.0`
- [Xavier-clx/sebal-tools](https://github.com/Xavier-clx/sebal-tools) - QGIS plugin for evapotranspiration estimation using SEBAL methodology. `★ 2` `custom licence`
- [ADM-Kenya/ET_HighRes_S3](https://github.com/ADM-Kenya/ET_HighRes_S3) - No description provided. `★ 1` `no licence`
- [AgyeDark/irrigation-auditor](https://github.com/AgyeDark/irrigation-auditor) - Most farmers irrigate by "gut feeling" or a fixed schedule (e.g., "every 3 days"). This wastes water and washes away nutrients. We will build a tool that tells them exactly how much to water based… `★ 1` `no licence`
- [ajaybaghel0047/Potential-Evapotranspiration-PET-Modeling](https://github.com/ajaybaghel0047/Potential-Evapotranspiration-PET-Modeling) - Compute PET using Penman-Monteith method. `★ 1` `no licence`
- [AniGerm/IrrigationPro](https://github.com/AniGerm/IrrigationPro) - Scientific FAO-56 irrigation controller for Home Assistant with HomeKit bridge, backup/restore and HACS support. `★ 1` `custom licence`
- [baramousa/ET_FAO56_Hydrus](https://github.com/baramousa/ET_FAO56_Hydrus) - Python code for calculating ET according to FAO56 and separate it into evaporation and transpiration based on LAI (leaf area index), An output file is produced which is an input for Hydrus1-d model. `★ 1` `no licence`
- [BenjMy/centum](https://github.com/BenjMy/centum) - Centum is a Python package that facilitates water accounting through energy and water balance modeling. `★ 1` `GPL-3.0`
- [buildwithadi/gridsphere-backend-api](https://github.com/buildwithadi/gridsphere-backend-api) - No description provided. `★ 1` `no licence`
- [Catmosphere314/IrriGator](https://github.com/Catmosphere314/IrriGator) - Projet de suivi des besoins en irrigation de l'agriculture céréalière au travers de données météorologiques, pédologiques et physiques. `★ 1` `custom licence`
- [changbing2019/DemoFAOPenman-MonteithReferenceETatHourlystep](https://github.com/changbing2019/DemoFAOPenman-MonteithReferenceETatHourlystep) - This repo is a demo to calculate reference ET at hourly time step based on FAO Penman_Monteith Equation. `★ 1` `no licence`
- [CNES/sweat](https://github.com/CNES/sweat) - Spatial Waterstress and Evapotranspiration Assessment for TRISHNA: Python implementation of EVASPA, STIC and ET timeseries algorithms. `★ 1` `AGPL-3.0`
- [ConnectedSystems/agtor](https://github.com/ConnectedSystems/agtor) - Agtor: an agricultural water management model built in Python 3. `★ 1` `MIT`
- [Fantaso/crop-evapotranspiration](https://github.com/Fantaso/crop-evapotranspiration) - This model is design by FAO and its use for calculating the amount of water that is lost due to evaporation or absorbed by the plant due to transpiration during the cultivation cycle. `★ 1` `no licence`
- [geoframecomponents/GEOET](https://github.com/geoframecomponents/GEOET) - GEOET is a Java-based modeling environment to simulate evapotranspiration. `★ 1` `GPL-3.0`
- [GreenSmart-DSS/IrrigationScheduler](https://github.com/GreenSmart-DSS/IrrigationScheduler) - A lightweight Python framework for daily root-zone water balance and depletion-based irrigation scheduling. `★ 1` `MIT`
- [idriss-lemnouni/crop-water-demand](https://github.com/idriss-lemnouni/crop-water-demand) - FAO-56 reference ET0 on Moroccan gridded weather, published-case checks and explicit hypothetical Kc scenarios. `★ 1` `custom licence`
- [JPL-Evapotranspiration-Algorithms/santanello-soil-heat-flux](https://github.com/JPL-Evapotranspiration-Algorithms/santanello-soil-heat-flux) - Soil Heat Flux Remote Sensing Method from Santanello & Friedl 2003 Python Package. `★ 1` `Apache-2.0`
- [JRoehrig/evapotranspiration](https://github.com/JRoehrig/evapotranspiration) - evapotranspiration. `★ 1` `MIT`
- [jvitorpinto/agmetpy](https://github.com/jvitorpinto/agmetpy) - No description provided. `★ 1` `MIT`
- [kawsikasundarapandian/Water-Usage-Predictor](https://github.com/kawsikasundarapandian/Water-Usage-Predictor) - “A Python-based tool that forecasts daily water requirements for crops using weather simulation and growth stage multipliers. Includes safety tips, irrigation alerts, CSV reports, and Tamil… `★ 1` `no licence`
- [KrishnaBhargavi92/Evapotranspiration](https://github.com/KrishnaBhargavi92/Evapotranspiration) - No description provided. `★ 1` `no licence`
- [krpeace/cropwater](https://github.com/krpeace/cropwater) - FAO-56 기반 노지 작물 물수지 분석 도구. `★ 1` `MIT`
- [Kyrk98/ArcPy-Metric-Sebal](https://github.com/Kyrk98/ArcPy-Metric-Sebal) - SEBAL/METRIC evapotranspiration ArcPy pipeline for Landsat 8/9 and ERA5-Land. `★ 1` `MIT`
- [leolaipelt/gee_eto](https://github.com/leolaipelt/gee_eto) - Calculo da Evapotranspiração de referência para a grama utilizando o método proposto em "The ASCE Standardized Reference Evapotranspiration Equation". `★ 1` `MIT`
- [LukeEcomod/FAO_dailyET](https://github.com/LukeEcomod/FAO_dailyET) - daily evapotranspiration using FAO 56 (Allen et al. 1998). `★ 1` `no licence`
- [M-salah-8/crop_monitoring_products](https://github.com/M-salah-8/crop_monitoring_products) - Evapotranspiration (SEBAL and senET) and crop growth models. `★ 1` `no licence`
- [martinedb/morton-crae-evapotranspiration-calculator](https://github.com/martinedb/morton-crae-evapotranspiration-calculator) - This Python implementation calculates daily evapotranspiration using the Morton Comprehensive Reference Atmosphere Evapotranspiration (CRAE) method. `★ 1` `MIT`
- [MarwaSamyBadr/FAO-Penman-Monteith](https://github.com/MarwaSamyBadr/FAO-Penman-Monteith) - python script to calculate FAO Penman-Monteith ET0 for a point or xarray. `★ 1` `no licence`
- [mishraratnakar2025-gif/FULL-PUBLICATION-READY-SSEBOP-WORKFLOW-MODIS-LANDSAT-Fused-ET-Indices-](https://github.com/mishraratnakar2025-gif/FULL-PUBLICATION-READY-SSEBOP-WORKFLOW-MODIS-LANDSAT-Fused-ET-Indices-) - FULL PUBLICATION-READY SSEBOP WORKFLOW MODIS + LANDSAT + Fused ET Indices, Uncertainty, Confidence, Quadrants, Chart. `★ 1` `no licence`
- [nehakn/ET0](https://github.com/nehakn/ET0) - Computing Reference Evapotranspiration (ET0) using various existing methods and ANN. `★ 1` `no licence`
- [NERC-CEH/hydro-pe](https://github.com/NERC-CEH/hydro-pe) - A package to calculate Hydro-PE potential evapotranspiration. `★ 1` `MIT`
- [Okstate-WaDE/et_forecast_lambda](https://github.com/Okstate-WaDE/et_forecast_lambda) - No description provided. `★ 1` `MIT`
- [Open-ET/openet-eemetric](https://github.com/Open-ET/openet-eemetric) - Earth Engine EEMETRIC ET Model. `★ 1` `AGPL-3.0`
- [OpenAgriTech/opencroplib](https://github.com/OpenAgriTech/opencroplib) - Opencroplib is a collection of Python libraries for simulating evapostranspiration processes. It includes code for extremely precise ephemeris calculations, and more. `★ 1` `MIT`
- [OpenCLIM/UKCP18-PET-and-Bias-Correction-for-Hydrology](https://github.com/OpenCLIM/UKCP18-PET-and-Bias-Correction-for-Hydrology) - These scripts can be used to calculate PET (potential evapotranspiration) from UKCP18 data, using Penman-Montieth, and to then apply a bias correction to PET, precipitation and temperature. `★ 1` `no licence`
- [polk96/crop_water_requirement](https://github.com/polk96/crop_water_requirement) - Python modules for estimating crop water requirement thru local climatic data. `★ 1` `GPL-3.0`
- [praghav444/Modeling_Stomatal_Conductance_for_ET_Partitioning](https://github.com/praghav444/Modeling_Stomatal_Conductance_for_ET_Partitioning) - No description provided. `★ 1` `no licence`
- [rishitalole/etr_calculator_app](https://github.com/rishitalole/etr_calculator_app) - This is an easy to use app for estimating reference evapotranspiration using historical weather data. You can use it for single day calcualtions, batch calcualtions using historical data and also… `★ 1` `no licence`
- [RonjaIffi/PyETo_crop](https://github.com/RonjaIffi/PyETo_crop) - Extention of the python libary PyETo for crop-specific settings in calculating potential evapotranspiration. `★ 1` `BSD-3-Clause`
- [SaeidTaleghani/SEBAL_Evapotranspiration](https://github.com/SaeidTaleghani/SEBAL_Evapotranspiration) - Estimating evapotranspiration from Landsat imagery using the SEBAL surface energy balance method (Python). `★ 1` `MIT`
- [sehnem/simdualkc](https://github.com/sehnem/simdualkc) - SIMDualKc core package — Dual Crop Coefficient water balance model (FAO-56). `★ 1` `GPL-3.0`
- [tanushripahari/Transformative-Predictions-for-Land-Water-Requirements](https://github.com/tanushripahari/Transformative-Predictions-for-Land-Water-Requirements) - used a modified version of the Penman Monteith Equation, and future climate projection over India to examine the relationship btw atm co2 and reference evapotranspiration and developed a… `★ 1` `no licence`
- [TheodorB/Penman](https://github.com/TheodorB/Penman) - Daily and hourly penman calculator according to FAO56. `★ 1` `no licence`
- [Thijs91/Garden_watering](https://github.com/Thijs91/Garden_watering) - Determine the needed amount of water to water the garden based on FAO56 method with a local weather station. `★ 1` `MIT`
- [VB011201/Evapotranspiration_Estimation-for-Irrigation-](https://github.com/VB011201/Evapotranspiration_Estimation-for-Irrigation-) - Used the meteorological data collected from IMD and used these parameters to estimate the ET0 value using four different supervised models. `★ 1` `no licence`
- [vilcagamarracf/Inv_arroz_METRIC](https://github.com/vilcagamarracf/Inv_arroz_METRIC) - Replicación del modelo de estimación de evapotranspiración METRIC con Python. `★ 1` `MIT`
- [wefallforbeauty/FAO-Model](https://github.com/wefallforbeauty/FAO-Model) - No description provided. `★ 1` `no licence`
- [XT-the-first/plant-hive](https://github.com/XT-the-first/plant-hive) - A sensor fleet that decides which plant to water — FAO-56 physics, five layers of validation, and a spec the code is audited against. `★ 1` `MIT`
- [A-Marambe/referenceET](https://github.com/A-Marambe/referenceET) - This code generate FAO 56 - reference evapotranspiration using meterological data. `no licence`
- [aarisalan/evapotranspiration_calculation](https://github.com/aarisalan/evapotranspiration_calculation) - Daily ET0 (FAO-56 Penman–Monteith) from hourly weather data: PostgreSQL + psycopg2, Python, Excel export; robust unit handling and gaps interpolation. `no licence`
- [aarisalan/weather_based_water_consumption](https://github.com/aarisalan/weather_based_water_consumption) - Kc-driven, weather-based water consumption and bucket simulation from ET₀ + irrigation time series; Excel/PNG outputs. `no licence`
- [abdulkadiratici7-ai/sensorless-irrigation-advisor](https://github.com/abdulkadiratici7-ai/sensorless-irrigation-advisor) - Sensor-free, crop-agnostic FAO-56 irrigation advisory system (olive validated; more crops on the roadmap). `MIT`
- [abrinlee/Evaptranspiration](https://github.com/abrinlee/Evaptranspiration) - FAO-56 Penman-Monteith evapotranspiration dashboard and nightly pipeline for landscape irrigation (IEM ASOS + NOAA GHCND + NASA POWER, MariaDB, Chart.js). `GPL-3.0`
- [AgriculturalModelExchangeInitiative/EvapoTranspirationModels](https://github.com/AgriculturalModelExchangeInitiative/EvapoTranspirationModels) - A collection of reference and crop evapotranspiration models commonly used in crop models. `no licence`
- [agroscope-ch/Irrigation](https://github.com/agroscope-ch/Irrigation) - Irrigation model of Philippe Monney, based on his work and on a publication of Antonio Roberto Pereira and Steve R. Green (2007, Water agricultural management). `no licence`
- [AHOwlia/MPySEBAL](https://github.com/AHOwlia/MPySEBAL) - Modified Version of pySEBAL version 3.4.4 - For Urmia Lake Basin. `Apache-2.0`
- [ajgal/py3SEB-UAV](https://github.com/ajgal/py3SEB-UAV) - A Python implementation of the Three-Source Energy Balance (3SEB) model for high-resolution UAV imagery. `no licence`
- [alexandre-codes/IrriSynk](https://github.com/alexandre-codes/IrriSynk) - Home Assistant integration for smart FAO-56-based irrigation control via solenoid valves. `GPL-3.0`
- [almuomo/irrigation_decision_support_system](https://github.com/almuomo/irrigation_decision_support_system) - Decision support system for agricultural irrigation based on open meteorological data. The project integrates climate data to calculate reference evapotranspiration (ET₀) and crop water requirements… `no licence`
- [andrewdotexs/fitosim](https://github.com/andrewdotexs/fitosim) - No description provided. `MIT`
- [AngryGeology/penmon](https://github.com/AngryGeology/penmon) - An object oreintated approach for estimation potential evapotranspiration with python (after Allen et al., 1998). `GPL-3.0`
- [arunthanga/FarmTwin](https://github.com/arunthanga/FarmTwin) - A digital twin solution for farming needs. `no licence`
- [AthiraNG/SAFER](https://github.com/AthiraNG/SAFER) - The SAFER was developed to address the need for real-time operational ET that did not require anchor pixels, as opposed to other SEB models, to operationalize real ET modeling.It is a simple… `no licence`
- [AtrCheema/ETUtil](https://github.com/AtrCheema/ETUtil) - calculate evapotranspiration from monthly to sub-hourly time step. `MIT`
- [AustinArrington87/evapotranspiration](https://github.com/AustinArrington87/evapotranspiration) - Scripts for calculating pET and cropET. `no licence`
- [Axiom32/et0-water-stress-pipeline](https://github.com/Axiom32/et0-water-stress-pipeline) - Evapotranspiration-based water stress estimation using FAO-56 Penman–Monteith and daily meteorological data. `no licence`
- [ayahmn/al-ahsa-irrigation-advisor](https://github.com/ayahmn/al-ahsa-irrigation-advisor) - AI-powered irrigation advisory for smallholder date palm farmers in Al-Ahsa, Saudi Arabia — built on FAO-56 Penman-Monteith and real NASA weather data. `no licence`
- [BerheAA/et-based-irrigation-scheduling](https://github.com/BerheAA/et-based-irrigation-scheduling) - Kansas Irrigation Water Management Dashboard. `no licence`
- [BerheAA/US-Irrigation-Water-Management-Dashboard](https://github.com/BerheAA/US-Irrigation-Water-Management-Dashboard) - Irrigation scheduling and management. `no licence`
- [bingqing-dev/etc-calculation](https://github.com/bingqing-dev/etc-calculation) - Python tools for crop water requirement calculation. `no licence`
- [biswashk920/evapotranspiration-lab](https://github.com/biswashk920/evapotranspiration-lab) - No description provided. `custom licence`
- [BJeannot1/Compute_actual_ET_over_space_and_time](https://github.com/BJeannot1/Compute_actual_ET_over_space_and_time) - No description provided. `no licence`
- [BryanNsoh/et_project](https://github.com/BryanNsoh/et_project) - No description provided. `no licence`
- [charlesmudima/716Hackathon](https://github.com/charlesmudima/716Hackathon) - PyWaPOR code for mapping and modelling evapotranspiration data. `Apache-2.0`
- [codebobaa/IrriSmart](https://github.com/codebobaa/IrriSmart) - IrriSmart is a web application designed to determine the necessary irrigation amount by using past meteorological and crop growth data. Through using the water balance model, the goal of IrriSmart… `no licence`
- [CorentinBarban/My-Garden-Irrigation](https://github.com/CorentinBarban/My-Garden-Irrigation) - Home Assistant integration that estimates garden watering needs using evapotranspiration (FAO-56) and Open-Meteo data. `GPL-3.0`
- [cse-kiet/PCSE26-05](https://github.com/cse-kiet/PCSE26-05) - No description provided. `no licence`
- [curtiscrandall/RemoteSensing_Evapotranspiration](https://github.com/curtiscrandall/RemoteSensing_Evapotranspiration) - Scripts that use processed satellite imagery (EVI and NDVI) and calculates evapotranspiration based on pixel values. Evapotranspiration calculation based on the FAO56/ASCE standardized grass and… `GPL-3.0`
- [dead-can-dance/agua-eficiente](https://github.com/dead-can-dance/agua-eficiente) - Sistema de Gestión Hídrica — Sonora, México. Motor FAO-56, Monte Carlo, Acuíferos CONAGUA. Desplegado en Streamlit Community Cloud. `no licence`
- [dgketchum/ptjpl](https://github.com/dgketchum/ptjpl) - Jet Propulsion Laboratory's Priestly-Taylor Evapotranspiration Algorithm. `Apache-2.0`
- [dgketchum/sims](https://github.com/dgketchum/sims) - Satellite Irrigation Management Support Evapotranspiration Algorithm. `Apache-2.0`
- [DHI-GRAS/py-esvep](https://github.com/DHI-GRAS/py-esvep) - Python implementation of End-member-based Soil and Vegetation Energy Partitioning (ESVEP) model. `GPL-3.0`
- [dodge-ttu/reference-ET-calculator](https://github.com/dodge-ttu/reference-ET-calculator) - Python code to calculate reference evapotranspiration via FAO-56. `no licence`
- [edscos/Python-Code-for-Remotely-Sensed-Crop-Coefficient](https://github.com/edscos/Python-Code-for-Remotely-Sensed-Crop-Coefficient) - Support material from Python coding to estimate daily evapotranspiration using reflectance-based crop coefficient models. `no licence`
- [egamberdiyevotabek/ai-irrigation-demo](https://github.com/egamberdiyevotabek/ai-irrigation-demo) - No description provided. `no licence`
- [El-Naggar8876/PI-Advisor](https://github.com/El-Naggar8876/PI-Advisor) - Spatiotemporal Irrigation Decision Support System. `MIT`
- [emuriu125-cmd/Hydroscope-The-Precision-Irrigation-Planner.](https://github.com/emuriu125-cmd/Hydroscope-The-Precision-Irrigation-Planner.) - HydroScope is designed to help farmers and communities manage water resources efficiently using science-based methods (FAO CROPWAT guidelines). `no licence`
- [fazogird/gee_et](https://github.com/fazogird/gee_et) - Sebal modeli yordamida Evapotrasnpiratsiyani aniqlash. `no licence`
- [fazogird/SEBAL](https://github.com/fazogird/SEBAL) - ET hisoblashning SEBAL modeli. `no licence`
- [gabe-parrish/refET_meteorology](https://github.com/gabe-parrish/refET_meteorology) - An open source implementation of the SSEBop model using GDAL based on the original ArcPy implementation by Gabriel, Steffie Matt n Mac. `Apache-2.0`
- [GEOframeOMSProjects/OMS_Project_GEOET](https://github.com/GEOframeOMSProjects/OMS_Project_GEOET) - OMS project of GEOET model to estimate evapotranspiration. `GPL-3.0`
- [ghidosoft/ha-et-irrigator](https://github.com/ghidosoft/ha-et-irrigator) - No description provided. `custom licence`
- [guymckrone/agrivoltaics-ET](https://github.com/guymckrone/agrivoltaics-ET) - A Python script to pull evapotranspiration (ET) data and provide an adjusted ET due to the addition of shade from the RUTE Suntracker solar array. `no licence`
- [hakanoguz/ET_for_Landsat_8_Python_Script](https://github.com/hakanoguz/ET_for_Landsat_8_Python_Script) - This python code calculates evapotranspiration (ET) from Landsat 8 imagery. `no licence`
- [halilunaziru73-creator/NaCROP](https://github.com/halilunaziru73-creator/NaCROP) - A modular Python pipeline with a Tkinter desktop GUI for reference/crop evapotranspiration, soil-water balance, irrigation scheduling, and a 4-step crop-growth simulation (canopy, transpiration… `MIT`
- [halilunaziru73-creator/Zaria-Crop-ET-and-Irrigation-DSS](https://github.com/halilunaziru73-creator/Zaria-Crop-ET-and-Irrigation-DSS) - A modular Python pipeline with a Tkinter desktop GUI for reference/crop evapotranspiration, soil-water balance, irrigation scheduling, and full farm-report generation for five crops grown around… `MIT`
- [hamza-aziz-ai/Dubai-Irrigation-Advisor](https://github.com/hamza-aziz-ai/Dubai-Irrigation-Advisor) - Physics-first irrigation advisor for Dubai: FAO-56 evapotranspiration cross-validated against 30 years of NASA observations, a root-zone water balance, and RF/XGBoost/LSTM predictors scored on… `no licence`
- [happy-tomato-farm/kansui](https://github.com/happy-tomato-farm/kansui) - Streamlit tool estimating daily irrigation from physically computed transpiration driven by solar radiation forecasts (Japanese). `no licence`
- [hckaraman/Hourly-POT-Calculation](https://github.com/hckaraman/Hourly-POT-Calculation) - Hourly Reference Evapotranspiration Calculation. `no licence`
- [HeitererGarten/fao56_scheduler](https://github.com/HeitererGarten/fao56_scheduler) - A predictive irrigation scheduler based on AquaCrop crop simulation model. `no licence`
- [hydrocodeir/Potential-Evapotranspiration](https://github.com/hydrocodeir/Potential-Evapotranspiration) - Estimation of Reference and Potential Evapotranspiration (1D (pandas.Series) and 3D (xarray.DataArrray) Data). `GPL-3.0`
- [iliasmachairas/Evapotranspiration-Calculator](https://github.com/iliasmachairas/Evapotranspiration-Calculator) - No description provided. `GPL-3.0`
- [iwmihq/geeSEBAL](https://github.com/iwmihq/geeSEBAL) - No description provided. `MIT`
- [Javier-JAQM/METRIC-MODEL](https://github.com/Javier-JAQM/METRIC-MODEL) - METRIC model for ET mapping with Landsat 5/7/8/9 over GEE. `MIT`
- [jmouthon/Simulad_ET_FAO](https://github.com/jmouthon/Simulad_ET_FAO) - Simulador que usa la ecuación de Penman Monteith de la FAO para estimar la evapotranspiración. `no licence`
- [JTUU98/pet-thornthwaite](https://github.com/JTUU98/pet-thornthwaite) - Calculate potential evapotranspiration (PET) from sub-annual temperature data using a modified Thornthwaite equation (Semenov et al., 1997). `MIT`
- [Junis-k/SEBAL_Algorithm](https://github.com/Junis-k/SEBAL_Algorithm) - Script Python pour exécuter la méthode SEBAL du bilan énergétique pour l'estimation de l'évapotranpiration réelle. `no licence`
- [KashyapAnurag/Penman-Monteith-Equation](https://github.com/KashyapAnurag/Penman-Monteith-Equation) - No description provided. `no licence`
- [KasperSaint07/DalaSu](https://github.com/KasperSaint07/DalaSu) - ML-based irrigation advisor for small farms in Kazakhstan: FAO-56 water balance calibrated with Sentinel-2 NDVI and machine learning. AITU diploma project. `no licence`
- [kazeemIshola/SURFLEX](https://github.com/kazeemIshola/SURFLEX) - Surface radiation and energy flux estimations using routine weather data and a land surface scheme. `no licence`
- [kickapoo/aira](https://github.com/kickapoo/aira) - An IRrigation Advisor. `no licence`
- [KIT-HYD/bridget](https://github.com/KIT-HYD/bridget) - Evapotranspiration toolbox. `no licence`
- [kreasteve/Iriy](https://github.com/kreasteve/Iriy) - Iriy – Smart Irrigation für Home Assistant (FAO-56 ET0 + Zonen-Defizit-Bilanz). `custom licence`
- [Kwakuopokuware401/HRMET_in_Python](https://github.com/Kwakuopokuware401/HRMET_in_Python) - Translating the HRMET evapotranspiration model to Python and applying it over gridded crop fields to estimate spatial ET uncertainty resulting from weather input errors. Focuses on perturbing inputs… `no licence`
- [leolaipelt/etr_inmet](https://github.com/leolaipelt/etr_inmet) - Cálculo da Evapotranspiração de Referência para as estações INMET utilizando o método proposto em "The ASCE Standardized Reference Evapotranspiration Equation". `MIT`
- [liborong123/RTEM-evapotranspiration-partitioning](https://github.com/liborong123/RTEM-evapotranspiration-partitioning) - Python implementation of the RTEM framework for regional vegetation transpiration estimation in the Three-River Headwaters Region. `no licence`
- [licm13/ET-Formula-Comparison](https://github.com/licm13/ET-Formula-Comparison) - 对比不同ET公式，考虑其应用影响和改进可能. `MIT`
- [licm13/PET-CR](https://github.com/licm13/PET-CR) - 蒸发互补理论分析. `no licence`
- [Lordratt/ETo-approximation-Mycropython-](https://github.com/Lordratt/ETo-approximation-Mycropython-) - recollection of Weather data through APIs for ETo approximation. Reference: Simplified forms for the standardized FAO-56 Penman–Monteith reference evapotranspiration using limited weather data… `Apache-2.0`
- [lotichydrological/pyMETRIC-UAV](https://github.com/lotichydrological/pyMETRIC-UAV) - An implementation of the METRIC energy balance model for UAV acquired images. `no licence`
- [lross2k/pyevap](https://github.com/lross2k/pyevap) - GUI application that helps calculate evapotranspiration. `no licence`
- [LucianoMDF/Calculo_ETo](https://github.com/LucianoMDF/Calculo_ETo) - Código para qualquer um que quiser calcular a Eto pelo método Penman-Monteith; dê os devidos créditos se for usar na sua Tese, obg ! `no licence`
- [LUMS-WIT/WIT-SEBAL-Val](https://github.com/LUMS-WIT/WIT-SEBAL-Val) - Code Repository for "Rafique, Hamza and Muhammad, Abubakr,Calibration and validation of field scale soil moisture estimates from an Energy Balance Model for the data-scarce Indus River Basin".". `no licence`
- [Mahdikalantari555/metric](https://github.com/Mahdikalantari555/metric) - No description provided. `no licence`
- [Makram-BHF/IWMI_Scheduling_IREY](https://github.com/Makram-BHF/IWMI_Scheduling_IREY) - IWMI new code for irrigation scheduling into IREY Gen3. `no licence`
- [malfihasan/PyPani](https://github.com/malfihasan/PyPani) - Python for Irrigation scheduler, PANI. `MIT`
- [MarcusBarrozo1/meca-qgis-plugin](https://github.com/MarcusBarrozo1/meca-qgis-plugin) - Modelo Estimativo de Consumo na Agricultura. `no licence`
- [mcrimaldi/ET0-PMFAO56](https://github.com/mcrimaldi/ET0-PMFAO56) - Code to download GRIB meteo files from ERA5-LAND repository, calculate ET0 and produce geographic rasters. `no licence`
- [mdfahimhasan/CWSI_EB_reflectance_ETa](https://github.com/mdfahimhasan/CWSI_EB_reflectance_ETa) - No description provided. `no licence`
- [mhcylnbl/bowen-energy-balance-and-evapotranspiration](https://github.com/mhcylnbl/bowen-energy-balance-and-evapotranspiration) - The Python codes include detailed visualizations of evapotranspiration and surface energy flux calculations using the Bowen Ratio Energy Balance (BREB) method. Monthly evapotranspiration estimates… `MIT`
- [Mich-O/smart_kilimo](https://github.com/Mich-O/smart_kilimo) - No description provided. `no licence`
- [MiguelAlejandroB/ET_UI_pyet](https://github.com/MiguelAlejandroB/ET_UI_pyet) - No description provided. `no licence`
- [mike-debney/adaptive-irrigation](https://github.com/mike-debney/adaptive-irrigation) - No description provided. `custom licence`
- [MohammadMirmazloumi/Evapotranspiration-Estimation-Sentinel3-pyTSEB](https://github.com/MohammadMirmazloumi/Evapotranspiration-Estimation-Sentinel3-pyTSEB) - No description provided. `no licence`
- [MoiTorVal/AquaAlert](https://github.com/MoiTorVal/AquaAlert) - FAO-56 water balance engine with FastAPI REST API, SQLAlchemy, and PostgreSQL. Predicts crop water stress 48 hours in advance for San Joaquin Valley farms. `MIT`
- [MoritzNelle/Calculate_PET_In_Real_Time](https://github.com/MoritzNelle/Calculate_PET_In_Real_Time) - Potential evapotranspiration (FAO-56) and field water deficit from live weather-station data, with an irrigation log. `MIT`
- [MostafaSaghafi/Evapotranspiration](https://github.com/MostafaSaghafi/Evapotranspiration) - No description provided. `no licence`
- [muhammedrashidx/irrigation-pet-model](https://github.com/muhammedrashidx/irrigation-pet-model) - No description provided. `no licence`
- [mvcastro/pet_equations](https://github.com/mvcastro/pet_equations) - Equations for Estimate Potential Evapotranspiration. `MIT`
- [nicolas0lucas/EvapoGIS](https://github.com/nicolas0lucas/EvapoGIS) - No description provided. `no licence`
- [nkz-os/nekazari-module-crop-health](https://github.com/nkz-os/nekazari-module-crop-health) - Crop Health Engine — Real-time biophysical inference (CWSI, MDS, Water Balance) for Nekazari platform. `AGPL-3.0`
- [Nora-Research-Lab/thornthwaite-pet-calculator](https://github.com/Nora-Research-Lab/thornthwaite-pet-calculator) - For climatologists and hydrologists: enter monthly mean temperatures and latitude to instantly compute potential evapotranspiration using the Thornthwaite method. `no licence`
- [nrs23/waterlogged-core](https://github.com/nrs23/waterlogged-core) - Core library for the waterlogged evapotranspiration app. `no licence`
- [OmarGarTe/SPAC-Py](https://github.com/OmarGarTe/SPAC-Py) - No description provided. `GPL-3.0`
- [Paolitoes/IrrigationScheduling](https://github.com/Paolitoes/IrrigationScheduling) - Calculating the irrigation schedule of my little garden. `no licence`
- [parallax-geo/Auto-PySEBAL](https://github.com/parallax-geo/Auto-PySEBAL) - PySEBAL Script Automated with Google Earth Engine API & Open MeteoAPI (For ET Estimation). `no licence`
- [passi277/Ha-Smarte-Bew-sserung](https://github.com/passi277/Ha-Smarte-Bew-sserung) - No description provided. `no licence`
- [PeterECarlson/tempest-et](https://github.com/PeterECarlson/tempest-et) - A side project to calculate evapotranspiration rates for. `no licence`
- [praghav444/pade_approximant_for_fully_explicit_analytical_solution_for_evapotranspiration_estimation](https://github.com/praghav444/pade_approximant_for_fully_explicit_analytical_solution_for_evapotranspiration_estimation) - This code implements and evaluates four analytical solutions for the evapotranspiration (ET) from the Penman-Monteith framework, each using a different approximation of the saturation specific… `MIT`
- [pratham291101/crop-irrigation-ai](https://github.com/pratham291101/crop-irrigation-ai) - 💧🌱 An AI-powered irrigation planning tool that calculates crop water requirements, simulates quota-based water allocation, and provides trading recommendations for farm fields. `no licence`
- [Rajasivaranjan/ET](https://github.com/Rajasivaranjan/ET) - No description provided. `no licence`
- [Ramonmurilo/ESTIMATIVA_EVAPOTRANSPIRACAO_TCC](https://github.com/Ramonmurilo/ESTIMATIVA_EVAPOTRANSPIRACAO_TCC) - Geração de estimativa de evapotranspiração pelo método Penman-Monteith FAO. `no licence`
- [rcasari/SSEBop-UnB](https://github.com/rcasari/SSEBop-UnB) - Python Script created for SSEBop calculation using satellite images and UAV Images. `no licence`
- [reaganames/ET-Calculator-Demonstration](https://github.com/reaganames/ET-Calculator-Demonstration) - Allows user to modify weather conditions and see what components change the calculated evapotranspiration most drastically. `no licence`
- [Revanth-3105/Estimation-of-Reference-Evapotranspiration-ET0-](https://github.com/Revanth-3105/Estimation-of-Reference-Evapotranspiration-ET0-) - Estimation of Reference Evapotranspiration(ET0)-By using Penman-Monteith method. `no licence`
- [rinkurinks9/Potential_Evapotranspiration](https://github.com/rinkurinks9/Potential_Evapotranspiration) - Code to find Potential_Evapotranspiration. `no licence`
- [RISHITASHARMA01/aquasense](https://github.com/RISHITASHARMA01/aquasense) - Smart Irrigation Advisory System — FAO-56 Penman-Monteith ET0, soil water balance, live weather, React+FastAPI. `MIT`
- [rizfre/PMFAO56-ET](https://github.com/rizfre/PMFAO56-ET) - This project presents a tool for estimating evapotranspiration based on the Penman-Monteith equation. `no licence`
- [ruiduobao/geoskill-evapotranspiration-estimation](https://github.com/ruiduobao/geoskill-evapotranspiration-estimation) - Priestley-Taylor 与简化 SEBAL 蒸散发估算，从净辐射/气温/LST/NDVI 计算 ET (mm/day)。Priestley-Taylor and simplified SEBAL evapotranspiration estimation from net radiation/air temperature/LST/NDVI. 输出 ET 栅格 + 统计 JSON。. `MIT`
- [ruiduobao/geoskill-irrigation-efficiency](https://github.com/ruiduobao/geoskill-irrigation-efficiency) - 基于作物蒸散发与有效降水计算灌溉需水量，并评估灌溉效率空间分布. `MIT`
- [ruiduobao/geoskill-irrigation-scheduling](https://github.com/ruiduobao/geoskill-irrigation-scheduling) - 基于 Penman-Monteith 需水与土壤水分平衡，按阈值触发灌溉日历。Computes crop water demand with Penman-Monteith, runs a soil water balance and triggers an irrigation calendar. `MIT`
- [RuiGao9/pyETo](https://github.com/RuiGao9/pyETo) - A Python package for calculating reference crop evapotranspiration (ETo). `MIT`
- [RuiGao9/pySAFER](https://github.com/RuiGao9/pySAFER) - Under developing ~. `MIT`
- [rusulucian85/hydrobalance](https://github.com/rusulucian85/hydrobalance) - HydroBalance - Smart irrigation based on real water deficit, not guesswork. `MIT`
- [rzgehu/ET-Toolbox-Product-Generator](https://github.com/rzgehu/ET-Toolbox-Product-Generator) - Evapotranspiration Product Generator for the ET Toolbox. `custom licence`
- [rzgehu/EvapoGIS-Plugin](https://github.com/rzgehu/EvapoGIS-Plugin) - Evapogis is a plugin developed based on the Surface Energy Balance Algorithm for Land (SEBAL) algorithm, aimed at obtaining evapotranspiration data and different components of the energy balance… `no licence`
- [SaadZahem/WaterManager](https://github.com/SaadZahem/WaterManager) - Calculate reference evapotranspiration and more. `MIT`
- [sachingodishela/evapotranspiration](https://github.com/sachingodishela/evapotranspiration) - As part of course CE4500, this assignment has been coded in python to calculate required ET values. `no licence` `archived`
- [sadick-adamu-p/irrigation-scheduling-model](https://github.com/sadick-adamu-p/irrigation-scheduling-model) - A Python model for demonstrating ET-based irrigation scheduling and root-zone soil moisture simulation. `no licence`
- [sbhoek/schedirr](https://github.com/sbhoek/schedirr) - Python package that can do calculations needed for the scheduling of irrigation in tertiary units. `GPL-3.0`
- [schultz-it/hose-assistant](https://github.com/schultz-it/hose-assistant) - Smart irrigation add-on for Home Assistant — FAO-56 ET-based, weather-aware, with its own mobile-first UI. 🚿. `MIT`
- [sepidehhazhir/OPTRAM_ET_Sentinel2](https://github.com/sepidehhazhir/OPTRAM_ET_Sentinel2) - Evapotranspiration estimation using the OPTRAM-ET model with Sentinel-2 satellite data. `no licence`
- [sepidehhazhir/sebal-always-Evatransportation-estimation-forever](https://github.com/sepidehhazhir/sebal-always-Evatransportation-estimation-forever) - Evapotranspiration estimation using the SEBAL model with Sentinel-2 satellite data. `no licence`
- [shreyamkhamari/CropFlow](https://github.com/shreyamkhamari/CropFlow) - No description provided. `no licence`
- [SidharrthSingh25/STIC-Pipeline](https://github.com/SidharrthSingh25/STIC-Pipeline) - Water stress pipeline built on Sentinel-3, Sentinel-2, and Landsat-8. Computes daily ET and SWSI per agricultural field using STIC-JPL energy balance, TsHARP LST sharpening, and S3 pan-sharpening… `no licence`
- [singamalaomsai/smart-irrigation-optimizer](https://github.com/singamalaomsai/smart-irrigation-optimizer) - An interactive web application built with Python and Streamlit to calculate dynamic crop water requirements and optimize smart irrigation schedules. `no licence`
- [SiorConsultingDev/irrigation-scheduler](https://github.com/SiorConsultingDev/irrigation-scheduler) - Agricultural irrigation scheduler using Síor Consulting rainfall data. `MIT`
- [sjbern/BucketIR](https://github.com/sjbern/BucketIR) - Bucket irrigation scheduling provides users with custom irrigation scheduling information determined from real time weather data, local irrigation system information, and other user-set parameters. `MIT`
- [SteenChr/edcrop](https://github.com/SteenChr/edcrop) - A Python package to simulate field-scale evapotranspiration and drainage from crop, wetland, or forest. `MIT`
- [sulavkandel/et0-kalkulator](https://github.com/sulavkandel/et0-kalkulator) - No description provided. `MIT`
- [Susanreefman/evapotranspiration](https://github.com/Susanreefman/evapotranspiration) - No description provided. `no licence`
- [szamaria/IrrigationSchedulingModels](https://github.com/szamaria/IrrigationSchedulingModels) - No description provided. `no licence`
- [tonyctsrpi/AgroFlux](https://github.com/tonyctsrpi/AgroFlux) - Sistema de prescripción inteligente de riego agrícola basado en la metodología FAO-56 con balance hídrico, mapa interactivo y exportación a Excel. `no licence`
- [Twark/ha_evapotranspiration_crops](https://github.com/Twark/ha_evapotranspiration_crops) - No description provided. `MIT`
- [udit1904/Hourly-Reference-ET-ASCE-Standardized-](https://github.com/udit1904/Hourly-Reference-ET-ASCE-Standardized-) - Python script that calculates hourly standardized reference evapotranspiration for short crop (clipped grass, 0.12 m) and tall crop (alfalfa, 0.50 m). `no licence`
- [Vikash12w2/Boond-Live](https://github.com/Vikash12w2/Boond-Live) - No description provided. `no licence`
- [wateraccounting/PI-Advisor](https://github.com/wateraccounting/PI-Advisor) - PI-Advisor: precision irrigation decision support with farmer-in-the-loop control (FAO-56, Streamlit, Google Earth Engine) – SoftwareX 2026. `MIT`
- [whiskas85/irrigazione-smart](https://github.com/whiskas85/irrigazione-smart) - Irrigazione a bilancio idrico FAO-56 per Home Assistant. `MIT`
- [Windyhhh/DCWRISM-CropIrrigation](https://github.com/Windyhhh/DCWRISM-CropIrrigation) - 作物灌溉模型 — FAO Penman-Monteith + 物理经验混合 + DE 优化. `MIT`
- [zengtianli/hydro-irrigation](https://github.com/zengtianli/hydro-irrigation) - Daily water balance calculator for paddy and dryland crop irrigation demand. `MIT`
- [zervakisai/vinea](https://github.com/zervakisai/vinea) - Nightly vineyard advisories — should I irrigate? can I spray? FAO-56 physics computes every number; LLM agents judge and explain, never calculate. Postgres RLS, SLOs in SQL, Helm, self-hosted tracing. `custom licence`

<a id="evapotranspiration-r"></a>

#### R

- [sbegueria/SPEI](https://github.com/sbegueria/SPEI) - An R package for computing the Standardized Precipitation-Evapotranspiration Index (SPEI), Penman-Monteith and other reference evapotranspiration, SPI, etc. `★ 108` `no licence`
- [midraed/water](https://github.com/midraed/water) - R package to calculate surface energy balance models. `★ 26` `no licence`
- [gowusu/sebkc](https://github.com/gowusu/sebkc) - R package for surface energy balance and crop coefficient evapotranspiration (ET) from satellite and thermal imagery: SEBAL, METRIC, SEBI, SSEB, SEBS and Two-Source (TSEB) models integrated with the… `★ 20` `no licence`
- [jacobteter/CropWatR](https://github.com/jacobteter/CropWatR) - Implementation of FAO 56 (similar to CropWat, but with expanded features) in R. `★ 13` `no licence`
- [cesarofs/agriwater](https://github.com/cesarofs/agriwater) - an R package for energy balance and actual evapotranspiration retrieving using satellite images and agrometeorological data. `★ 9` `custom licence`
- [cran/Evapotranspiration](https://github.com/cran/Evapotranspiration) - :exclamation: This is a read-only mirror of the CRAN R package repository. Evapotranspiration — Modelling Actual, Potential and Reference Crop Evapotranspiration. `★ 9` `no licence`
- [cug-xyx/hydroET](https://github.com/cug-xyx/hydroET) - A Cpp-based R package featuring multiple (potential) evapotranspiration algorithms. `★ 8` `GPL-3.0`
- [gabrielblain/CropWaterBalance](https://github.com/gabrielblain/CropWaterBalance) - Climate Water Balance For Irrigation Purposes. `★ 6` `custom licence`
- [pramitghosh/RS_ET](https://github.com/pramitghosh/RS_ET) - Measuring evapotranspiration using remote sensing data. `★ 6` `no licence`
- [AVJdataminer/Landsat_ET_Rtools](https://github.com/AVJdataminer/Landsat_ET_Rtools) - R scripts to create surface radiation components of evapotranspiration from Landsat Satellite data. `★ 5` `no licence`
- [bgctw/etpart](https://github.com/bgctw/etpart) - Partitioning Evapotranspiration into Evaporation and Transpiration. `★ 4` `AGPL-3.0`
- [FilgueirasR/cropDemand](https://github.com/FilgueirasR/cropDemand) - Package that aims to carry out the crop water balance with images from TerraClimate. `★ 4` `CC-BY-4.0`
- [daniel-althoff/Easy-ETo](https://github.com/daniel-althoff/Easy-ETo) - Easy Reference Evapotranspiration (ShinyApp). `★ 3` `no licence`
- [kaliczp/Thorntwaite2](https://github.com/kaliczp/Thorntwaite2) - Rebuild of our Thortwaite-like monthly evapotranspiration model. `★ 3` `GPL-2.0`
- [micahwoods/ETo](https://github.com/micahwoods/ETo) - Evapotranspiration (ET) by date and latitude from Hargreaves equation. `★ 3` `GPL-2.0`
- [DanluGuo/Evapotranspiration](https://github.com/DanluGuo/Evapotranspiration) - Version 1.12 as cran. `★ 2` `no licence`
- [prenticelab/ETpartitioning_R_OPerezPriego](https://github.com/prenticelab/ETpartitioning_R_OPerezPriego) - Perez-Priego et al used the P model to partition transpiration from eddy covariance evapotranspiration observations. Published in JGR Biogeosciences 2018… `★ 2` `no licence`
- [rmcnellis/evapotranspiration_R](https://github.com/rmcnellis/evapotranspiration_R) - Calculate evapotranspiration in R. `★ 2` `no licence`
- [rsh249/raster_PET](https://github.com/rsh249/raster_PET) - An R script for calculating the Thornthwaite Potential Evapotranspiration on global temperature raster layers. `★ 2` `no licence`
- [VicenteYago/ET.PenmanMonteith](https://github.com/VicenteYago/ET.PenmanMonteith) - ET.PenmanMonteith: A package for calculate daily Penman-Monteith Evapotranspiration from hourly data. `★ 2` `no licence`
- [adrHuerta/PISCOeo_pm](https://github.com/adrHuerta/PISCOeo_pm) - PISCOeo_pm, a reference evapotranspiration gridded database based on FAO Penman-Monteith in Peru. `★ 1` `GPL-3.0`
- [AkbarR1184/evapoRe](https://github.com/AkbarR1184/evapoRe) - An open access tool for efficient global evapotranspiration analysis, estimation, and downloading. `★ 1` `no licence`
- [DanluGuo/ETinfilling](https://github.com/DanluGuo/ETinfilling) - Parsimonious gap-filling models for actual evapotranspiration observations from eddy-covariance systems. `★ 1` `CC0-1.0`
- [egreich/A-semi-mechanistic-model-for-partitioning-evapotranspiration](https://github.com/egreich/A-semi-mechanistic-model-for-partitioning-evapotranspiration) - This repository contains the code and models for the paper A semi-mechanistic model for partitioning evapotranspiration reveals scale-dependent moisture supply and demand controls water-use… `★ 1` `no licence`
- [hydrosolutions/IrrigationCalc_NCP_EDSS](https://github.com/hydrosolutions/IrrigationCalc_NCP_EDSS) - Heilonggang Irrigation Calculator for deployment with the EDSS framework. `★ 1` `MIT`
- [Manish-met/cropwatMUL](https://github.com/Manish-met/cropwatMUL) - An R package for multi-location crop water requirement estimation, irrigation scheduling, and FAO-56 based crop evapotranspiration modelling. `★ 1` `GPL-3.0`
- [pruettm/cropsyst](https://github.com/pruettm/cropsyst) - CropSyst Crop Evapotranspiration Modeling Framework. `★ 1` `custom licence`
- [samirigfri/ET0RadModels](https://github.com/samirigfri/ET0RadModels) - Evapotranspiration Estimation Using Radiation-Based Models. `★ 1` `no licence`
- [XiaoxiangGuanGFZ/PET_models](https://github.com/XiaoxiangGuanGFZ/PET_models) - potential evapotranspiration models in hydrology. `★ 1` `no licence`
- [AthiraNG/FAO-56-PM](https://github.com/AthiraNG/FAO-56-PM) - The FAO-56 Penman-Monteith is considered the standard technique to calculate ETo. Penman technique yields a precise output with minimal error. The radiation approach is commonly in the area where… `no licence`
- [AthiraNG/Metric-Sebal](https://github.com/AthiraNG/Metric-Sebal) - Space-based technology, especially remote sensing of the land surface, has revolutionized surface energy flux studies. It has enabled the study of energy fluxes over a larger area, beyond the limits… `no licence`
- [aWhereAPI/CalculateWeatherVars_aWhere](https://github.com/aWhereAPI/CalculateWeatherVars_aWhere) - Repo that contains fxns for calculating intermediate vars used in Penman Monteith Calculation of PET. `no licence`
- [Bikalpa1234/METRIC-Evapotranspiration](https://github.com/Bikalpa1234/METRIC-Evapotranspiration) - No description provided. `no licence`
- [Breinerdan/SpatialET](https://github.com/Breinerdan/SpatialET) - Here we have different script mainly in R to process and calculate evapotranspiration data. `GPL-3.0`
- [cran/FAO56](https://github.com/cran/FAO56) - :exclamation: This is a read-only mirror of the CRAN R package repository. FAO56 — Evapotranspiration Based on FAO Penman-Monteith Equation. `no licence`
- [cran/PMEvapotranspiration](https://github.com/cran/PMEvapotranspiration) - :exclamation: This is a read-only mirror of the CRAN R package repository. PMEvapotranspiration — Calculation of the Penman-Monteith Evapotranspiration using Weather Variables. `no licence`
- [cran/simET](https://github.com/cran/simET) - :exclamation: This is a read-only mirror of the CRAN R package repository. simET — Tools for Simulation of Evapotranspiration of Field Crops and Soil Water Balance. `no licence`
- [erichseamon/evapotranspiration](https://github.com/erichseamon/evapotranspiration) - Evapotranspiration. `no licence`
- [francorvillalba/ETo_sg_PenmanMonteith](https://github.com/francorvillalba/ETo_sg_PenmanMonteith) - Procedimientos para el cálculo de la Evapotranspiración de referencia usando el método Penman Monteith según el Estudio de Riego y Drenaje de la FAO 56, a partir de datos de una estación automática… `no licence`
- [geografiaenviz/ETR-turc-MSAVI](https://github.com/geografiaenviz/ETR-turc-MSAVI) - This code estimates evapotranspiration using historical precipitation data from meteorological stations. It also calculates surface evaporation using Landsat 8 thermal imagery and integrates MSAVI… `no licence`
- [hieum01/DailyPET](https://github.com/hieum01/DailyPET) - Estimation of daily potential evapotranspiration (PET). `MIT`
- [Jeikosd/bio_vars_etp](https://github.com/Jeikosd/bio_vars_etp) - bio variables for potential evapotranspiration. `no licence`
- [joaobtj/irritool](https://github.com/joaobtj/irritool) - Irrigation Tools in R. `custom licence`
- [juliuseberhard/echse-et-code](https://github.com/juliuseberhard/echse-et-code) - Evapotranspiration modeling in ECHSE -- R code, data, miscellanea. For the structure of the R code, see README. `no licence` `archived`
- [juliuseberhard/echse-et-models](https://github.com/juliuseberhard/echse-et-models) - Evapotranspiration modeling in ECHSE -- models. `no licence` `archived`
- [jvitorpinto/agmet](https://github.com/jvitorpinto/agmet) - No description provided. `MIT`
- [mafhoumchaimae/hydroAgri](https://github.com/mafhoumchaimae/hydroAgri) - Package R pour le bilan hydrique des cultures - FAO-56. `custom licence`
- [MichaelRGrant/ETHourly](https://github.com/MichaelRGrant/ETHourly) - R package that calculates hourly evapotranspiration for both short and tall reference crops. `no licence`
- [Rapha7021/cawet](https://github.com/Rapha7021/cawet) - No description provided. `AGPL-3.0`
- [rsibajam-max/evapotranspiracion-metric](https://github.com/rsibajam-max/evapotranspiracion-metric) - Balance de energía satelital (METRIC) para estimación de evapotranspiración de cultivos a partir de imágenes Landsat 8. `no licence`
- [samirigfri/ET0MassModels](https://github.com/samirigfri/ET0MassModels) - Evapotranspiration Estimation Using Mass Transfer-Based Models. `no licence`
- [samirigfri/ET0TempModels](https://github.com/samirigfri/ET0TempModels) - Evapotranspiration Estimation Using Temperature-Based Models. `no licence`
- [Tim2110/Codes_wateravailabilityconstraints_PML](https://github.com/Tim2110/Codes_wateravailabilityconstraints_PML) - Contains the codes used to optimize and evaluate water availability constraint functions integrated into the Penman-Monteith-Leuning model. Functions were applied microsite-specifically (sub-canopy… `MIT`
- [TPMarques/EvapoR](https://github.com/TPMarques/EvapoR) - R package to estimate ETo using FAO56 Penman-Monteith equation. (Currently a test version). `no licence`
- [Yingjie4Science/ETo_FAO](https://github.com/Yingjie4Science/ETo_FAO) - A demo function to calculate Reference evapotranspiration (ETo) according to FAO standards. `MIT`

<a id="evapotranspiration-ruby"></a>

#### Ruby

- [brycejohnston/evapotranspiration](https://github.com/brycejohnston/evapotranspiration) - Ruby library for calculating reference crop evapotranspiration (ETo). `★ 15` `BSD-3-Clause`
- [uwent/wisp](https://github.com/uwent/wisp) - Wisconsin Irrigation Scheduling Program (WISP). `★ 2` `no licence`
- [arsturges/et0](https://github.com/arsturges/et0) - The Reference Evapotranspiration Project. `no licence`
- [uwent/wisp3](https://github.com/uwent/wisp3) - Wisconsin Irrigation Scheduling Program, version 3. `no licence`

<a id="evapotranspiration-rust"></a>

#### Rust

- [silenthooligan/localsky](https://github.com/silenthooligan/localsky) - Weather-aware irrigation on your hardware. Local weather, soil water balance, sprinkler control, and an optional Home Assistant companion. `★ 8` `Apache-2.0`
- [Longitude103/crop_coefficients](https://github.com/Longitude103/crop_coefficients) - No description provided. `★ 1` `no licence`
- [syntheticChemistry/airSpring](https://github.com/syntheticChemistry/airSpring) - Pure Rust precision agriculture — FAO-56 evapotranspiration, Richards equation soil physics, irrigation scheduling. GPU-accelerated. AGPL-3.0. `custom licence`
- [Twark/irrigation-calc](https://github.com/Twark/irrigation-calc) - No description provided. `custom licence`

<a id="evapotranspiration-shell"></a>

#### Shell

- [sherzodr/libpenmon](https://github.com/sherzodr/libpenmon) - Implements weather station class in C++ that calculates ETo based on Penman-Monteith equation. `★ 2` `MIT`
- [codein007/crop-water-stress-simulator](https://github.com/codein007/crop-water-stress-simulator) - A field-scale soil moisture bucket model with weather-driven evapotranspiration and an adaptive irrigation scheduler to minimize water use while keeping crop water stress below critical thresholds. `★ 1` `MIT`

<a id="evapotranspiration-typescript"></a>

#### TypeScript

- [KingGloose/fao-penman-monteith-js](https://github.com/KingGloose/fao-penman-monteith-js) - This is a repository for calculating the FAO-Penman-Monteith equation using JavaScript. `★ 11` `MIT`
- [alejandroechev/cropet](https://github.com/alejandroechev/cropet) - cropet. `no licence`
- [alviandf/furrow](https://github.com/alviandf/furrow) - Irrigation planner for farm managers: Expo (React Native) app, Hono API on Postgres, and an explainable FAO-56 model. `no licence`
- [giftdayo54/CWR-Intelligent-Irrigation-Scheduler](https://github.com/giftdayo54/CWR-Intelligent-Irrigation-Scheduler) - No description provided. `no licence`
- [leif-Simplified/Simplified-Irrigation-Calculator](https://github.com/leif-Simplified/Simplified-Irrigation-Calculator) - A smart irrigation calculator that uses ET, soil type, nozzle selection, sun exposure, slope, and pressure to generate accurate watering schedules. `no licence`
- [MohammedBelfellah/OleaSat](https://github.com/MohammedBelfellah/OleaSat) - OleaSat is a smart irrigation advisory platform for olive farms. It combines satellite indices, weather-based FAO-56 irrigation logic, and a dashboard workflow to help farmers decide when and how… `no licence`
- [mustefakamil/IRR2](https://github.com/mustefakamil/IRR2) - No description provided. `no licence`
- [nylaimanii/aquifer](https://github.com/nylaimanii/aquifer) - AI irrigation advisor that tells farmers the minimum water needed to keep yield stable, using FAO-56 Penman-Monteith math + free public weather/soil data. `no licence`
- [saisudhamshu-999/Project-SunShift](https://github.com/saisudhamshu-999/Project-SunShift) - Project SunShift: feeder-level irrigation scheduling for the solar era (FAO-56, pvlib, OR-Tools CP-SAT, React + Three.js). `no licence`
- [yathboss/Risk-Aware-Irrigation-Lab](https://github.com/yathboss/Risk-Aware-Irrigation-Lab) - Virtual Lab MVP: 7-day soil moisture simulation + Monte Carlo stress-risk (%) + minimum irrigation recommendation (Next.js + TypeScript + Recharts). `no licence`

<a id="evapotranspiration-visual-basic"></a>

#### Visual Basic

- [claytonscottlewis/GridET](https://github.com/claytonscottlewis/GridET) - Gridded Evapotranspiration Estimation. `★ 5` `no licence`
- [apvinod31/FAO_Penman_monteith_ET](https://github.com/apvinod31/FAO_Penman_monteith_ET) - FAO_Penman_monteith_ET. `no licence`
- [apvinod31/Temperature-based-Evapotranspiration-estimation-using-Hargreaves-Method](https://github.com/apvinod31/Temperature-based-Evapotranspiration-estimation-using-Hargreaves-Method) - Temperature based Evapotranspiration estimation using Hargreaves Method (FAO Based). `no licence`

<a id="evapotranspiration-other"></a>

#### Other

- [DHI-GRAS/senEtSnapSta](https://github.com/DHI-GRAS/senEtSnapSta) - :gear: SNAP STA for Sen-ET. `★ 11` `GPL-3.0`
- [mariomhawej/SEBALI-SEBALIGEE](https://github.com/mariomhawej/SEBALI-SEBALIGEE) - Automated evapotranspiration retrieval model with missing soil-related datasets. `★ 9` `GPL-3.0`
- [SoothingMist/Embeddable-Software-for-Irrigation-Control](https://github.com/SoothingMist/Embeddable-Software-for-Irrigation-Control) - This project develops C++ and Python standard-language software for embedding in irrigation controllers for human-supervised fully-automated distributed systems. `★ 8` `AGPL-3.0`
- [rogierwesterhoff/pet2aet](https://github.com/rogierwesterhoff/pet2aet) - Google Earth Engine files used for conversion of potential evapotranspiration (ET) to actual ET. `★ 3` `no licence`
- [CenidRaspaRiego/EvapoGEE](https://github.com/CenidRaspaRiego/EvapoGEE) - The design principles for EvapoGEE were that it should provide a site-specific reference evapotranspiration (ET0) estimate for a range of dates using different reanalysis data sets (CFSv2, GLDAS… `★ 2` `MIT`
- [7ony7he7iger/ag_tamu_et](https://github.com/7ony7he7iger/ag_tamu_et) - This project is to construct calculation tools for crop evapotranspiration using the FAO-56 meteorological approach. Data are collected from the researchers at the Texas A&M AgriLife Research at… `★ 1` `no licence`
- [California-Data-Collaborative/Evapotranspiration](https://github.com/California-Data-Collaborative/Evapotranspiration) - Improve on current ET estimates by incorporating heterogeneous sources of weather data. `★ 1` `no licence`
- [23garyd/pet-calculator](https://github.com/23garyd/pet-calculator) - Uses global scale climate data, CO2 simulations, and net radiation data in order to predict potential evapotranspiration. `no licence`
- [Abdelbaki-H/Smart-Irrigation-Manager](https://github.com/Abdelbaki-H/Smart-Irrigation-Manager) - A user-friendly software application for estimating reference evapotranspiration (ET), calculating irrigation water requirements, and scheduling irrigation using various methods. `no licence`
- [abdelrazekelnashar/ETMapper](https://github.com/abdelrazekelnashar/ETMapper) - No description provided. `no licence`
- [Ayotochtle/SpatialET](https://github.com/Ayotochtle/SpatialET) - Evapotranspiration Estimation from Satellite Images. `no licence`
- [Ayotochtle/SpatialETEST](https://github.com/Ayotochtle/SpatialETEST) - R Package to calculate potential and real evapotranspiration using Landsat 8 and 9 imagery and meteorological data. `no licence`
- [BetsabeBA/tomato-kc-greenhouse](https://github.com/BetsabeBA/tomato-kc-greenhouse) - Data and code for estimating stage-specific crop coefficients (Kc) and evapotranspiration (ETc) in greenhouse tomato using lysimeter measurements and mixed-effects models. Fully reproducible R-based… `no licence`
- [dahoal2/et0_barra](https://github.com/dahoal2/et0_barra) - Calculation of FAO56 crop reference evapotranspiration from BARRA temperature, humidity, wind and solar radiation inputs. `no licence`
- [fftfewere4445-del/Evapotranspiration-Driven-Irrigation](https://github.com/fftfewere4445-del/Evapotranspiration-Driven-Irrigation) - No description provided. `no licence`
- [HaoranRS/Evapotranspiration-retrieval](https://github.com/HaoranRS/Evapotranspiration-retrieval) - This is an automatic evapotranspiration retrieval program for Landsat imagery. `no licence`
- [Has9A/SEBAL-and-Penman-Monteith-Evapotranspiration](https://github.com/Has9A/SEBAL-and-Penman-Monteith-Evapotranspiration) - No description provided. `no licence`
- [hugodesrutins/INRAE_TRISHNA_evapotranspiration](https://github.com/hugodesrutins/INRAE_TRISHNA_evapotranspiration) - Ce répertoire regroupe l'ensemble des codes pour le calcul d'évapotranspiration à partir de différentes données. `no licence`
- [indirabose/Improved-Irrigation-Advisory-System-IAS-](https://github.com/indirabose/Improved-Irrigation-Advisory-System-IAS-) - No description provided. `no licence`
- [MaluMassiel/Evapotranspiration](https://github.com/MaluMassiel/Evapotranspiration) - Evapotranspiration calculation using the Penman method modified by García. `no licence`
- [mdredwanahmad/CropSyst-EHM](https://github.com/mdredwanahmad/CropSyst-EHM) - CropSyst-EHM: A Novel Modeling Framework to Quantify Total Crop Water Demand, Including Evapotranspiration and Heat-Stress Management. `no licence`
- [mickenordin/weather](https://github.com/mickenordin/weather) - Some pythonscripts that get weather data from SMHI and calculates evapotranspiration. `no licence`
- [shuwen2tingting5/wwolff7](https://github.com/shuwen2tingting5/wwolff7) - Script to calculate daily evapotranspiration for Landsat images in GRASS GIS 7.X. `no licence`
- [soilwater/dip](https://github.com/soilwater/dip) - Daily Irrigation Planner. `no licence`
- [timmybowman/homeassistant-smart-sprinklers](https://github.com/timmybowman/homeassistant-smart-sprinklers) - Adaptive Home Assistant irrigation system using ESPHome, virtual soil moisture modelling and weather forecasting. `MIT`
- [ufcg-lsd/saps-scripts-processing](https://github.com/ufcg-lsd/saps-scripts-processing) - No description provided. `no licence`
- [yashnamahilang08-eng/SMART-IRRIGATE-](https://github.com/yashnamahilang08-eng/SMART-IRRIGATE-) - Smart Irrigate - Intelligent crop water management. Real-time weather + FAO Penman-Monteith calculations. Responsive SPA w/ glassmorphism UI, auth, dashboard. Mobile-first • Chart.js • PWA-ready.… `no licence`

<a id="weather"></a>

### Weather and agroclimate

<a id="weather-c"></a>

#### C

- [Rheinwalt/WeatherGenerator](https://github.com/Rheinwalt/WeatherGenerator) - Data-driven and event-based time series generator that preserves inter-arrival time and burst length distributions. `★ 1` `MIT`

<a id="weather-csharp"></a>

#### C#

- [Crop2ML-Catalog/STICS_SNOW](https://github.com/Crop2ML-Catalog/STICS_SNOW) - It allows to estimate snow cover and to recalculate precipitation, and temperatures data. `MIT`
- [welitonalmeida/Calculadora_Agroclimatica](https://github.com/welitonalmeida/Calculadora_Agroclimatica) - Calculadora para Cálculos Agroclimáticos. `MIT`

<a id="weather-cplusplus"></a>

#### C++

- [ropensci/agroclimatico](https://github.com/ropensci/agroclimatico) - Conjunto de funciones para calcular índices y estadísticos climáticos hidrológicos a partir de datos tidy. Incluye una función para graficar resultados georeferenciados y e información cartográfica. `★ 19` `custom licence`
- [ARPA-SIMC/PRAGA](https://github.com/ARPA-SIMC/PRAGA) - PRAGA PRogram for AGrometeorological Analysis. `★ 2` `no licence`
- [ARPA-SIMC/WeatherGenerator](https://github.com/ARPA-SIMC/WeatherGenerator) - A suite of programs aimed at producing temporal series based on the observational dataset. Daily data of precipitation, maximum temperature and minimum temperature are produced. Two different… `★ 2` `LGPL-3.0`

<a id="weather-fortran"></a>

#### Fortran

- [Emerson-D-Oliveira/dinsol-v1.0](https://github.com/Emerson-D-Oliveira/dinsol-v1.0) - The Daily INSOLationi (DINSOL-v1.0) is a model that simulates the incoming solar radiation at the top of the atmosphere following the Milankovitch cycles. The program is ideal for preparing the… `★ 3` `GPL-3.0`
- [ARVE-Research/gwgen_f90](https://github.com/ARVE-Research/gwgen_f90) - The FORTRAN code base for a global weather generator. `★ 2` `GPL-2.0`
- [rogerlew/jimf-cligen532](https://github.com/rogerlew/jimf-cligen532) - Cligen 5.32 (Cligen 5.3 with Jim's TP fixes). `★ 1` `no licence`
- [DSSAT/WGEN_sa](https://github.com/DSSAT/WGEN_sa) - Stand-alone WGEN for generating daily weather data from monthly summaries. Output to DSSAT format. `BSD-3-Clause`
- [jfrankenberger/cligen4](https://github.com/jfrankenberger/cligen4) - Older CLIGEN 4 code. `no licence`
- [jfrankenberger/cligen5](https://github.com/jfrankenberger/cligen5) - CLIGEN V5 source. `no licence`
- [Richard-Chandler/Rglimclim](https://github.com/Richard-Chandler/Rglimclim) - A multisite, multivariate weather generator based on generalised linear models. `custom licence`
- [takyurp09/agroclim-fortran](https://github.com/takyurp09/agroclim-fortran) - Validated crop-season climate exposure calculations in modern Fortran with OpenMP, strict QC, and reproducible provenance. `MIT`

<a id="weather-java"></a>

#### Java

- [julsdym/Weather-Generator](https://github.com/julsdym/Weather-Generator) - Predicts the weather conditions for a specified month, simulating the likelihood of wet or dry days using historical transition probabilities. Generates weather forecasts based on a location's… `no licence`
- [Myxhal/WeatherGenerator-Java](https://github.com/Myxhal/WeatherGenerator-Java) - Java program that simulates daily weather patterns based on probabilistic models, generating forecasts of temperature and precipitation. `no licence`
- [patelagni21/WeatherGenerator](https://github.com/patelagni21/WeatherGenerator) - No description provided. `no licence`
- [ShaunM042/Weather-Generator](https://github.com/ShaunM042/Weather-Generator) - A Java library that uses historical data to create and analyze simulated weather forecasts. This study uses predictive models of historical weather data to simulate patterns of precipitation in the… `no licence`

<a id="weather-javascript"></a>

#### JavaScript

- [jvail/weather.js](https://github.com/jvail/weather.js) - Solar radiation and daylength. `★ 2` `GPL-3.0`
- [CCAFS/MarkSIM](https://github.com/CCAFS/MarkSIM) - No description provided. `GPL-3.0`
- [Kaysharp-cloud/Agroclime](https://github.com/Kaysharp-cloud/Agroclime) - Agroclimatic indices calculator. `no licence`

<a id="weather-julia"></a>

#### Julia

- [dmetivie/StochasticWeatherGenerators.jl](https://github.com/dmetivie/StochasticWeatherGenerators.jl) - A Julia package for la pluie et le beau temps. `★ 20` `MIT`
- [fabern/VegetationPeriods.jl](https://github.com/fabern/VegetationPeriods.jl) - No description provided. `★ 1` `GPL-3.0`
- [cbsteh/MsiaGen.jl](https://github.com/cbsteh/MsiaGen.jl) - Stochastic Daily Weather Generator for Malaysia. `MIT`
- [cbsteh/SawitEdu](https://github.com/cbsteh/SawitEdu) - Daily weather generator for Malaysia. `MIT` `archived`
- [dmetivie/PeriodicARModels.jl](https://github.com/dmetivie/PeriodicARModels.jl) - A package to use AR models with periodic parameters (often monthly) for Stochastic Weather Generators. `custom licence`

<a id="weather-matlab"></a>

#### MATLAB

- [andungbayu/awgenscp_matlab](https://github.com/andungbayu/awgenscp_matlab) - Articulated Weather Generator for Seasonal Climate Prediction (AWGenSCP) matlab development. `★ 1` `no licence`
- [brayantz/MulGETS](https://github.com/brayantz/MulGETS) - Multi-site weather Generator of École de Technologie Supérieure - MUlGETS (precipitation only). `MIT`
- [h-cel/StochGen](https://github.com/h-cel/StochGen) - Code for running and evaluating the stochastic weather generator of Van de Velde et al. (accepted for publication). `GPL-3.0`
- [suhail017/Stochastic-Weather-Genearator](https://github.com/suhail017/Stochastic-Weather-Genearator) - It is a temporary repo for all the work related to build a stochastic Weather generator for Mid atlantic region. `no licence`

<a id="weather-python"></a>

#### Python

- [IBM/IBMWeatherGen](https://github.com/IBM/IBMWeatherGen) - A daily stochastic weather generator based on resampling methodology. `★ 46` `MIT`
- [metno/wxgen](https://github.com/metno/wxgen) - Weather generator software. `★ 26` `LGPL-3.0`
- [ARVE-Research/gwgen](https://github.com/ARVE-Research/gwgen) - A global WGEN-like weather generator. `★ 25` `custom licence`
- [roe-dl/weewx-GTS](https://github.com/roe-dl/weewx-GTS) - XType extension for WeeWX to provide solar energy, "Grünlandtemperatursumme" (a kind of growing degree days) and "dayET" and "ET24" as some kind of opposite to "dayRain" and "rain24". `★ 15` `GPL-3.0`
- [JiriVales/agroclimatic-factors](https://github.com/JiriVales/agroclimatic-factors) - Algorithms of creation agroclimatic factors from climatic dataset ERA5-Land (Necdf files). `★ 4` `BSD-3-Clause`
- [mdekauwe/weather_generator](https://github.com/mdekauwe/weather_generator) - No description provided. `★ 4` `no licence`
- [WSWUP/evaporative-demand-drought-index](https://github.com/WSWUP/evaporative-demand-drought-index) - Calculate the Evaporative Demand Drought Index (EDDI). `★ 4` `Apache-2.0`
- [jemsethio/AgClimateAF_indices](https://github.com/jemsethio/AgClimateAF_indices) - The AgroClimate Indices Engine is a production-ready Python pipeline that transforms raw climate data (hourly to seasonal NetCDF) into standardized agro-climate indicators for crop, livestock, and… `★ 2` `no licence`
- [PabloLavin12/AgroClimaticIndices](https://github.com/PabloLavin12/AgroClimaticIndices) - Notebooks y resultados del cálculo de índices agroclimáticos. `★ 2` `MIT`
- [alexschuddeboom/EGGS-WG](https://github.com/alexschuddeboom/EGGS-WG) - Open source ERA5 based stochastic weather generator. `★ 1` `GPL-3.0`
- [openamundsen/openamundsen-climategenerator](https://github.com/openamundsen/openamundsen-climategenerator) - Stochastic weather generator for producing synthetic meteorological data. `★ 1` `MIT`
- [111fu/AgroMeteorological-Data-Analysis-Tool](https://github.com/111fu/AgroMeteorological-Data-Analysis-Tool) - Common agrometeorological indicators within the calculable phenological period. `no licence`
- [Agrobitsrl/FD-freezinginjury](https://github.com/Agrobitsrl/FD-freezinginjury) - Frost Injury Alert Model: Standalone Python module that generates BBCH-stage-specific frost-risk alerts for 19 perennial crops by combining growing-degree-day phenology with stage-specific critical… `Apache-2.0`
- [aldeano/driade](https://github.com/aldeano/driade) - Webtool for calculating agroclimatic and phenological indexes. `no licence`
- [aybulatf/weather-generator-django](https://github.com/aybulatf/weather-generator-django) - Stochastic weather generator. API service built with Django REST Framework . `no licence`
- [bgroenks96/wxsbi](https://github.com/bgroenks96/wxsbi) - Toolkit for stochastic weather generation using probabilistic programming (numpyro) and simulation-based inference (SBI) in python. `MIT`
- [Critical-Infrastructure-Systems-Lab/Multivariate-Weather-Generator](https://github.com/Critical-Infrastructure-Systems-Lab/Multivariate-Weather-Generator) - No description provided. `no licence`
- [crtjer/noaa-wine-climate](https://github.com/crtjer/noaa-wine-climate) - NOAA climate pipeline for US wine regions — growing degree days, frost dates, precipitation, Winkler index by AVA (2000–present). `no licence`
- [cylin928/MultiWG](https://github.com/cylin928/MultiWG) - A uni-site and multi-site stochastic weather generator. `GPL-3.0`
- [DAReHub/WeatherGenerator](https://github.com/DAReHub/WeatherGenerator) - This repository contains multiple python scripts for the weather generator. `no licence`
- [deniseiras/PROFESSIONAL_WG_land_eval](https://github.com/deniseiras/PROFESSIONAL_WG_land_eval) - Weather Generator Land evaluation. `GPL-3.0`
- [farafehizoro/weather_generator](https://github.com/farafehizoro/weather_generator) - No description provided. `MIT`
- [gracechuan2/WGEN](https://github.com/gracechuan2/WGEN) - Weather generation scripts based off of the Richardson (1984) climate model WGEN. Generates daily weather data for rainfall, min temperature, max temperature, and solar radiation from input daily… `no licence`
- [hari-sree/weather-generator](https://github.com/hari-sree/weather-generator) - Generate reasonably realistic weather sequences. `no licence`
- [ICSC-CN-HPC-Spoke-4-Earth-Climate/hammon_weather_generator](https://github.com/ICSC-CN-HPC-Spoke-4-Earth-Climate/hammon_weather_generator) - Weather generator for precipitation over Emilia Romagna. `MIT`
- [iskur/varwg](https://github.com/iskur/varwg) - A single-site, vector-autoregressive weather generator. `custom licence`
- [iskur/weathercop](https://github.com/iskur/weathercop) - A copula-based weather generator. `MIT`
- [Ju-Aln/Canopy_microclimate_project](https://github.com/Ju-Aln/Canopy_microclimate_project) - Tools to simulate and study in-canopy microclimate with a proper user interface. `no licence`
- [LCB0B/sto-weather-gen](https://github.com/LCB0B/sto-weather-gen) - Stochastic weather generator. `no licence`
- [manmeet3591/crop-weather-tools](https://github.com/manmeet3591/crop-weather-tools) - Crop weather decision tools for Kentucky fruit and Arizona field crops, with S2S outlooks (WKU prototype). `MIT`
- [marielary/drought-analysis-haute-matsiatra](https://github.com/marielary/drought-analysis-haute-matsiatra) - Pipeline for computing agroclimatic indicators (SPI, SPEI, ET₀, GDD, WRSI, NDVI…) for the Haute Matsiatra region, Madagascar, agricultural seasons 2011/12 to 2017/18. `MIT`
- [meteFANS/dynalogic-agro-met-equations-pkg](https://github.com/meteFANS/dynalogic-agro-met-equations-pkg) - Package for custom agro met equations. `BSD-3-Clause`
- [mintproject/simplewg](https://github.com/mintproject/simplewg) - Weather Generators made simple. `GPL-3.0`
- [mmejiam-eafit/weather_generator](https://github.com/mmejiam-eafit/weather_generator) - No description provided. `no licence`
- [MutaharChalmers/wgen](https://github.com/MutaharChalmers/wgen) - Another statistical weather generator. `MIT`
- [nmartin198/wattrib_wg_eaa](https://github.com/nmartin198/wattrib_wg_eaa) - Weather Attribution Constrained Weather Generator – EAA Basins. `AGPL-3.0`
- [nmartin198/wattrib_wg_frio](https://github.com/nmartin198/wattrib_wg_frio) - Weather Attribution, Constrained Weather Generator – Frio. `AGPL-3.0`
- [np-ndri-org/WG_CRA_tool](https://github.com/np-ndri-org/WG_CRA_tool) - Weather Generator and Climate Change Scenario Generator for Climate Risk Assessment. `MIT`
- [Shail241996/Stochastic-weather-simlulator.-](https://github.com/Shail241996/Stochastic-weather-simlulator.-) - I created a weather prediction model for Delhi - based on the current data. `no licence`
- [UF-CRS/SpatialWeatherGenerator](https://github.com/UF-CRS/SpatialWeatherGenerator) - No description provided. `no licence`
- [xthames/swxg](https://github.com/xthames/swxg) - Pythonic multivariate, multisite stochastic weather generator. `MIT`

<a id="weather-r"></a>

#### R

- [nassernajibi/WGEN-v2.0](https://github.com/nassernajibi/WGEN-v2.0) - User Manual (Documentation Guide) for Stochastic Weather Generator v2.0. `★ 41` `GPL-3.0`
- [rnuske/vegperiod](https://github.com/rnuske/vegperiod) - R Package to determine Thermal Vegetation Periods. `★ 10` `no licence`
- [HydrosystemsGroup/Weather-Generator](https://github.com/HydrosystemsGroup/Weather-Generator) - No description provided. `★ 7` `no licence`
- [MNLR/BNWeatherGen](https://github.com/MNLR/BNWeatherGen) - Weather Generators with Bayesian Networks. `★ 7` `MIT`
- [ec-jrc/Clisagri](https://github.com/ec-jrc/Clisagri) - No description provided. `★ 6` `no licence`
- [sobakrim/MSTWeatherGen](https://github.com/sobakrim/MSTWeatherGen) - A multivariate and spatio-temporal stochastic weather generator in R. `★ 6` `GPL-3.0`
- [andrew-verdin/glmgen-workshop](https://github.com/andrew-verdin/glmgen-workshop) - R scripts for GLM based stochastic weather generation. Single-, multi-site, and gridded simulation. `★ 2` `no licence`
- [cadillac-desert/wgen](https://github.com/cadillac-desert/wgen) - Weather Generator from Cornell. `★ 2` `MIT`
- [CRC-SAS/weather-generator](https://github.com/CRC-SAS/weather-generator) - No description provided. `★ 2` `no licence`
- [Atreyagaurav/weather-geneator-south-africa](https://github.com/Atreyagaurav/weather-geneator-south-africa) - Weather generator code and other scripts for south africa. `★ 1` `no licence`
- [Chair-Geolearning/MSTWeatherGen](https://github.com/Chair-Geolearning/MSTWeatherGen) - A multivariate and spatio-temporal stochastic weather generator in R. `★ 1` `GPL-3.0`
- [cran/sirad](https://github.com/cran/sirad) - :exclamation: This is a read-only mirror of the CRAN R package repository. sirad — Functions for Calculating Daily Solar Radiation and Evapotranspiration. Homepage… `★ 1` `no licence`
- [LidongMo/FrostRiskProject](https://github.com/LidongMo/FrostRiskProject) - No description provided. `★ 1` `no licence`
- [MNLR/wilksWG](https://github.com/MNLR/wilksWG) - Wilks Multisite Weather Generator. `★ 1` `MIT`
- [SantanderMetGroup/climate4R.agro](https://github.com/SantanderMetGroup/climate4R.agro) - Agroclimatic indices. `★ 1` `GPL-3.0`
- [taschillerberg/AgroClmIndCode](https://github.com/taschillerberg/AgroClmIndCode) - PhD work with Agroclimate Indices relating too crop failure. `★ 1` `MIT`
- [cbarriosperez/Agroclimatic-Indices](https://github.com/cbarriosperez/Agroclimatic-Indices) - No description provided. `no licence`
- [ccadiou/Analogues-SWG](https://github.com/ccadiou/Analogues-SWG) - This stochastic weather generator (SWG) uses analogues of circulation to simulate realistic climate events. With empirical importance sampling, it allows to simulate worst-case scenario of extreme… `GPL-3.0`
- [CIAT-DAPA/subsetting_indicators](https://github.com/CIAT-DAPA/subsetting_indicators) - No description provided. `no licence`
- [DrAhmedKheir/calculate_HDW_hours.R](https://github.com/DrAhmedKheir/calculate_HDW_hours.R) - No description provided. `no licence`
- [drkupi/APWS](https://github.com/drkupi/APWS) - Asia Pacific Weather Statistics (APWS) for generating synthetic weather data in hydrologic models. `no licence`
- [hdorado/Weather_forecast](https://github.com/hdorado/Weather_forecast) - No description provided. `no licence`
- [MelWhitehead/SWM](https://github.com/MelWhitehead/SWM) - Stochastic Weather Model (SWM) code. `no licence`
- [njdepsky/GCM-Downscaling-Tool](https://github.com/njdepsky/GCM-Downscaling-Tool) - A GCM model data explorer and stochastic synthetic weather generator tool aimed at regional evaluation of GCM model performance and the production of downscaled temperature and precipitation… `no licence`
- [rarabzad/weatherGenerator](https://github.com/rarabzad/weatherGenerator) - Weather Generator Tool. `no licence`
- [wep69/agriClimateRisk](https://github.com/wep69/agriClimateRisk) - Stage-Aware Agroclimatic Risk Analysis for Crops (R package 1.0.0). `custom licence`

<a id="weather-rust"></a>

#### Rust

- [rogerlew/cligen-rs](https://github.com/rogerlew/cligen-rs) - No description provided. `Apache-2.0`

<a id="weather-other"></a>

#### Other

- [CREA-AgroMeteorology/AgroMIND](https://github.com/CREA-AgroMeteorology/AgroMIND) - Agro-meteorological Monitoring INDices. `custom licence`
- [esmoreido/newgen](https://github.com/esmoreido/newgen) - Multisite stochastic weather generator by IWP RAS (Gelfan, Moreido). `no licence`
- [EunjinHan-USDA/HWGEN](https://github.com/EunjinHan-USDA/HWGEN) - About A hybrid stochastic weather generator (HWGEN) is designed to temporally downscale seasonal tercile forecasts for both precipitation and temperature, generating synthetic daily weather… `no licence`
- [JohnRushKucharski/tempest](https://github.com/JohnRushKucharski/tempest) - A weather generator with a Jupyter Notebook interface. `BSD-3-Clause`
- [sohrab4748/KNN-WG](https://github.com/sohrab4748/KNN-WG) - Presenting the KNN Weather Generator, a robust tool for efficient weather data generation on Windows. Experience advanced lead time capabilities with this powerful tool, crafted to simulate daily… `no licence`

<a id="pests-diseases"></a>

### Pests, diseases and weeds

<a id="pests-diseases-csharp"></a>

#### C#

- [dgebelein/swat-rfp](https://github.com/dgebelein/swat-rfp) - Modeling and forecasting of vegetable fly population dynamics. `★ 1` `AGPL-3.0`
- [VibertJerome/ddrp-dotnet](https://github.com/VibertJerome/ddrp-dotnet) - A rewritten DDRP platform in C#. "The objective of the Degree-Day, establishment Risk, and Pest event mapping system (DDRP) is to predict phenology and climate suitability of invasive, biocontrol.". `GPL-3.0`

<a id="pests-diseases-cplusplus"></a>

#### C++

- [picasa/archidemio](https://github.com/picasa/archidemio) - A Generic Model to Simulate Air-Borne Diseases as a Function of Crop Architecture (doi:10.1371/journal.pone.0049406). `★ 3` `GPL-3.0`
- [adelynflowers/HLB-ABM](https://github.com/adelynflowers/HLB-ABM) - An agent-based model written in C++ that simulates the interactions between disease vectors, agricultural crops, and agricultural managers. Disease vectors have customizable behavior for… `no licence`
- [hmetcalfe1/spatial_blackgrass](https://github.com/hmetcalfe1/spatial_blackgrass) - A spatially-explicit simulation model of black-grass (Alopecurus myosuroides) population dynamics. `MIT`

<a id="pests-diseases-fortran"></a>

#### Fortran

- [gutluca/dismo_dssat](https://github.com/gutluca/dismo_dssat) - Repository containing the Disease Impact and Severity Module, coupled within the Generic-Pest framework in the DSSAT-CSM. `BSD-3-Clause`
- [gutluca/dssat-csm-disease](https://github.com/gutluca/dssat-csm-disease) - Repository containing the DSSAT software source code, combined with the generic and adaptable epidemiological model for fungal diseases (DISMO.for) integrated into CROPGRO.for. The codes used for… `BSD-3-Clause`

<a id="pests-diseases-gaml"></a>

#### GAML

- [jpcabatingan/pest-management](https://github.com/jpcabatingan/pest-management) - Standalone Pest Management Model for my internship at ACROSS. `no licence`

<a id="pests-diseases-javascript"></a>

#### JavaScript

- [buriansandor/PlantDiseaseForecast](https://github.com/buriansandor/PlantDiseaseForecast) - This web app is designed to forecast plant diseases by analyzing weather conditions, helping growers take timely action to protect their crops. This project was created to Gemini API Developer… `★ 2` `no licence`
- [AlbinJosephroy/blastcast-web](https://github.com/AlbinJosephroy/blastcast-web) - AI-powered rice blast disease forecasting for 7 Kerala districts. EPIRICE model + live Open-Meteo weather data. `no licence`
- [pest-spread-project/pest-spread-project](https://github.com/pest-spread-project/pest-spread-project) - Grid-based pest spread simulation using Cellular Automata to predict crop infestation risk based on environmental factors. `no licence`
- [tomazrg/paper_TS_weather](https://github.com/tomazrg/paper_TS_weather) - In this study, our objective was to introduce a new modeling framework in plant disease epidemiology and characterize the effect of climate proxies across the different epidemiological phases of… `no licence`

<a id="pests-diseases-julia"></a>

#### Julia

- [agimenezromero/PierceDisease-GlobalRisk-Predictions](https://github.com/agimenezromero/PierceDisease-GlobalRisk-Predictions) - A model to assess the global risk of Pierce's Disease of grapevines. `★ 4` `GPL-3.0`
- [ecorecipes/PhysiologicallyBasedDemographicModels.jl](https://github.com/ecorecipes/PhysiologicallyBasedDemographicModels.jl) - No description provided. `★ 2` `MIT`
- [JuliaEpi/Epicrop.jl](https://github.com/JuliaEpi/Epicrop.jl) - Simulation modelling of crop diseases using a Healthy-Latent-Infectious-Postinfectious (HLIP) model in Julia. `MIT`
- [manuvanegas/SpatialRustModel](https://github.com/manuvanegas/SpatialRustModel) - Spatially explicit process-based model of Coffee Leaf Rust epidemics in coffee agroforestry systems — Julia, SLURM, Approximate Bayesian Computation. `MIT`

<a id="pests-diseases-mathematica"></a>

#### Mathematica

- [SimulationEverywhere-Models/CDPP-DBM](https://github.com/SimulationEverywhere-Models/CDPP-DBM) - DBM are a pest that can cause serious damage to crops. This model is to capture relationship of Diamondback moth and parasitoids. Download model and sample simulations. `no licence`

<a id="pests-diseases-matlab"></a>

#### MATLAB

- [alaviyan-dr/maize-streak-ga-pid-control](https://github.com/alaviyan-dr/maize-streak-ga-pid-control) - MATLAB code and simulation outputs for fractional-order maize streak disease modelling with bounded GA-optimized PID intervention control and repeatability analysis. `MIT`
- [Bernard0541/-Mitigating-Black-Pod-Disease](https://github.com/Bernard0541/-Mitigating-Black-Pod-Disease) - Mathematical modeling and analysis of Black Pod Disease (BPD) transmission dynamics in cocoa plants using compartmental modeling, bifurcation theory, optimal control, sensitivity analysis… `no licence`
- [ChristianNembot/Cocoa-spatial-model](https://github.com/ChristianNembot/Cocoa-spatial-model) - Simulation and estimation code comsol with matlab. `no licence`
- [PetrosDamos-Research/Hybrid-Climate-Resilient-Plant-Disease-Forecasting](https://github.com/PetrosDamos-Research/Hybrid-Climate-Resilient-Plant-Disease-Forecasting) - Hybrid computational framework for climate-resilient plant disease forecasting. Developed by Dr. Petros Damos as part of the research paper entitled: ''Hybrid computational framework for… `custom licence`
- [Rothamsted/CBS-Dispersal-Model](https://github.com/Rothamsted/CBS-Dispersal-Model) - A landscape-scale model of Cassava Brown Streak dispersal within and between growers’ fields, and the response of growers to the disease through a behavioural model of clean seed use. `Apache-2.0`
- [Rothamsted/CBSDispersalModel](https://github.com/Rothamsted/CBSDispersalModel) - A landscape-scale model of Cassava Brown Streak dispersal within and between growers’ fields, and the response of growers to the disease through a behavioural model of clean seed use. `no licence`

<a id="pests-diseases-netlogo"></a>

#### NetLogo

- [israeltankam/CMD4.0-Cassava-Mosaic-Disease-Simulator](https://github.com/israeltankam/CMD4.0-Cassava-Mosaic-Disease-Simulator) - Agent-based NetLogo model simulating Cassava Mosaic Disease dynamics through interactions between cassava varieties and whitefly vectors. Includes roguing, replanting, and economic outcomes.… `no licence`

<a id="pests-diseases-objective-c"></a>

#### Objective-C

- [kbhalerao/SCNSim](https://github.com/kbhalerao/SCNSim) - Simulation software for the Soybean Cyst Nematode Agent Based Model. `no licence`

<a id="pests-diseases-python"></a>

#### Python

- [julienmalard/Tikon](https://github.com/julienmalard/Tikon) - Modelos tróficos agroecológicos sin pena. `★ 6` `AGPL-3.0`
- [UW-Madison-DSI/ag_forecasting_api](https://github.com/UW-Madison-DSI/ag_forecasting_api) - Ag Forecasting API - soybean and corn, sourced from Wisconet Weather stations and IBM Environmental Intelligence for Wisconsin. `★ 3` `MIT`
- [breecummins/WheatVirusCompartmentalModel](https://github.com/breecummins/WheatVirusCompartmentalModel) - No description provided. `★ 2` `no licence`
- [mararizasentis/BBR](https://github.com/mararizasentis/BBR) - An open-source model based on phenological parameters for automatic Botrytis cinerea detection in vineyards. `★ 2` `MIT`
- [openalea/EpyMix](https://github.com/openalea/EpyMix) - A Python Model to study Epidemic dilution and barrier factors in Mixture crops. `★ 2` `no licence`
- [agrocompuepidemlab/Long-term-epidemiological-surveillance-of-Polerovirus-SCYLV-dynamics-in-Colombian-sugarcane](https://github.com/agrocompuepidemlab/Long-term-epidemiological-surveillance-of-Polerovirus-SCYLV-dynamics-in-Colombian-sugarcane) - This repository contains the code used in 'Long-term epidemiological surveillance integrated with data science and multi-model approaches advances understanding of Polerovirus SCYLV dynamics in… `★ 1` `no licence`
- [agstack/opensource-pestmodels](https://github.com/agstack/opensource-pestmodels) - Hierarchical pest and disease modeling framework for AgStack (Linux Foundation). 13 models, 19 crops, 54 threats. Python wheel + FastAPI + MCP server. `★ 1` `Apache-2.0`
- [IcedDino/moth-dynamics](https://github.com/IcedDino/moth-dynamics) - This project simulates the population dynamics of pest moths and their interaction with two biological control agents—Trichogramma and Diadegma insulare—as well as pesticide interventions. The model… `★ 1` `no licence`
- [icipe-official/MaDiPHS-project](https://github.com/icipe-official/MaDiPHS-project) - Unified pest modeling repository and tools for research, inference, validation, and deployment of pest models under the MaDiPHS project. `★ 1` `no licence`
- [NehuenVill/Growing-Degree-Days-Tracker](https://github.com/NehuenVill/Growing-Degree-Days-Tracker) - A Django/Python Based project to track the evolution of GDDs through the time for controlling plagues in different farms across Guatemala. `★ 1` `no licence`
- [openalea-incubator/alep](https://github.com/openalea-incubator/alep) - Alep: an FSPM for Architecture & Leaf Pathogen. `★ 1` `custom licence`
- [openalea/DSS](https://github.com/openalea/DSS) - Repository containing DSS model code. `★ 1` `custom licence`
- [rmshimomura/Scientific-initiation](https://github.com/rmshimomura/Scientific-initiation) - Scientific initiation results about spores movement prediction models on soy beans crops on the State of Paraná. `★ 1` `no licence`
- [Sdavid66/Meteo-Sentinelle](https://github.com/Sdavid66/Meteo-Sentinelle) - Home Assistant integration that predicts frost and plant disease risk (late blight, powdery mildew) from any weather station's sensors, using published agronomic models: Hutton criteria… `★ 1` `GPL-3.0`
- [AgIOModeling/Generic-Modeling-Engine](https://github.com/AgIOModeling/Generic-Modeling-Engine) - A repository of agricultural models focusing on disease, pest and leaf wetness models. `no licence`
- [Agrobitsrl/PDM-fuzzymodel](https://github.com/Agrobitsrl/PDM-fuzzymodel) - Open-source, multi-crop fuzzy-logic engine that estimates daily pest and disease infection risk from weather data and crop phenology. `Apache-2.0`
- [agrocompepidemlab/Climate-driven-modelling-potato-crop-diseases-Approach-to-evidence-based-decision-system](https://github.com/agrocompepidemlab/Climate-driven-modelling-potato-crop-diseases-Approach-to-evidence-based-decision-system) - Climate-driven epidemiological modeling and data science frameworks for potato crop diseases, designed to support evidence-based agricultural decision-making systems. `no licence`
- [agrocompuepidemlab/Phytosanitary-Status-and-Mesoscale-Spatiotemporal-Modeling-of-Potato-Diseases-in-Colombia](https://github.com/agrocompuepidemlab/Phytosanitary-Status-and-Mesoscale-Spatiotemporal-Modeling-of-Potato-Diseases-in-Colombia) - This repository contains the code used in 'Phytosanitary Status and Mesoscale Spatial, Temporal, and Spatiotemporal Modeling of Major Potato Diseases in Colombia for Data-Driven Epidemiological… `no licence`
- [agroscope-ch/plasmopy](https://github.com/agroscope-ch/plasmopy) - Infection prediction modeling of Plasmopara viticola life cycle stages in vineyards using weather data. This project represents a revisited and customizable Python version of the models used by… `AGPL-3.0`
- [All-Purpose-Monkey/agro_detection_api](https://github.com/All-Purpose-Monkey/agro_detection_api) - No description provided. `no licence`
- [AMIRMAHMOUDINIA/tomato-fusarium-disease-progress-modeling](https://github.com/AMIRMAHMOUDINIA/tomato-fusarium-disease-progress-modeling) - tomato-fusarium-disease-progress-modeling. `MIT`
- [arnob-r/P4-model](https://github.com/arnob-r/P4-model) - Codes for the P4 model analyzing pollinator–plant–pest dynamics under pesticide regulation and IPM adoption. It includes transition of pollinator population from extinct to non-extinct states, basin… `no licence`
- [asmitty55-cloud/Disease-modeling-program](https://github.com/asmitty55-cloud/Disease-modeling-program) - weather data driven disease modeling. `no licence`
- [BishwaBS/Crop_Weed_Interaction_Modeling](https://github.com/BishwaBS/Crop_Weed_Interaction_Modeling) - No description provided. `MIT`
- [Chelsea357/CWC](https://github.com/Chelsea357/CWC) - Final Project for maize disease model. `no licence`
- [dh565/RS-PestDyn](https://github.com/dh565/RS-PestDyn) - RS-PestDyn is an insect pest population dynamics model driven by satellite-derived information. `no licence`
- [djohnanderson/DegreeDays](https://github.com/djohnanderson/DegreeDays) - Python program to calculate degree days for insect models used in pest management. Uses SensorPush gateway and sensor for temperature data. `no licence`
- [doct-rubens/predator-prey-beetle-wasp](https://github.com/doct-rubens/predator-prey-beetle-wasp) - # predator-prey-beetles-waspsPredator prey model based on beetle-wasp interactions with direct application to sugar cane plague control using natural methods (without pesticides). `BSD-2-Clause`
- [eleanorecc/MICCORDEA](https://github.com/eleanorecc/MICCORDEA) - An AfricaRice and IRRI project for modelling effects of climate change on rice disease in Tanzania. `no licence`
- [fredsonaguiar/parasitoid-sugarcane-control](https://github.com/fredsonaguiar/parasitoid-sugarcane-control) - Modeling and Control of Host–Parasitoid Dynamics in Sugarcane Borer Biological Management. `no licence`
- [harshandev/crop-disease-forecasting](https://github.com/harshandev/crop-disease-forecasting) - No description provided. `no licence`
- [israeltankam/cvsmart](https://github.com/israeltankam/cvsmart) - CVSMART is an advanced agricultural decision-support system designed to predict and manage Cassava Mosaic Disease (CMD) spread in Sub-Saharan Africa. Combining epidemiological models with geospatial… `no licence`
- [KaziJahidurRahaman/simpest](https://github.com/KaziJahidurRahaman/simpest) - No description provided. `MIT`
- [lakla8/aphid_population_check](https://github.com/lakla8/aphid_population_check) - No description provided. `no licence`
- [LuisGabriel27/mango-point](https://github.com/LuisGabriel27/mango-point) - No description provided. `no licence`
- [mainalibishwo/mainali-ipm-forecast](https://github.com/mainalibishwo/mainali-ipm-forecast) - No description provided. `MIT`
- [mihir-m-gandhi/Tree-Disease-Spread-Cellular-Automata](https://github.com/mihir-m-gandhi/Tree-Disease-Spread-Cellular-Automata) - We propose a system that models the spread of disease throughout the branches of individual fruit trees, in which we will compute the “optimal” shape that a tree should be pruned to prior to the… `no licence`
- [namedummy568-stack/pest-modeling-scripts](https://github.com/namedummy568-stack/pest-modeling-scripts) - Repository for pest population modeling scripts. `no licence`
- [naranjo-jd/CMD_ABM](https://github.com/naranjo-jd/CMD_ABM) - Stochastic Agent-Based Model for Cassava Mosaic Disease transmission using Python and Mesa. `no licence`
- [NYSIPM/seedcorn-maggot](https://github.com/NYSIPM/seedcorn-maggot) - A Python module that estimates seedcorn maggot first adult emergence using multiple published models. `no licence`
- [PacificBird/InsectPhenologyCaptureSim](https://github.com/PacificBird/InsectPhenologyCaptureSim) - Simulator for observed insect capture by degree day + analysis for WSU Department of Entomology research. `no licence`
- [pedroaaguarnieri/spb-leprose-citros](https://github.com/pedroaaguarnieri/spb-leprose-citros) - Modelo de Graus-Dia para Brevipalpus yothersi (ácaro da leprose dos citros): sistema preditivo open source de apoio ao manejo. TCC de Engenharia Agronômica. `MIT`
- [rab-ferrari/predator-prey-beetles-wasps](https://github.com/rab-ferrari/predator-prey-beetles-wasps) - Predator prey model based on beetle-wasp interactions with direct application to sugar cane plague control using natural methods (without pesticides). `no licence`
- [schoyt/PraiseGDD](https://github.com/schoyt/PraiseGDD) - Interactive web-based dashboard for Growing Degree Day (GDD) information with phenological context for arborists. `no licence`
- [SCSLabISU/AgGym](https://github.com/SCSLabISU/AgGym) - No description provided. `no licence`
- [Tungdil01/Spodoptera](https://github.com/Tungdil01/Spodoptera) - Welcome to the repository for the mathematical models and code associated with the research paper 'Modelling the biocontrol of Spodopterafrugiperda: A mechanistic approach considering Bt crops and… `GPL-3.0`
- [Tungdil01/TrophicDynamicsCode](https://github.com/Tungdil01/TrophicDynamicsCode) - Code for the chapter "Pest Biocontrol and Allee Effects Acting on the Control Agent Population: Insights from Predator-Prey Models". Models ODEs to simulate Allee effects in pest and control agent… `MIT`
- [ysaikai/BTABM](https://github.com/ysaikai/BTABM) - An agent-based model of insect resistance management and mitigation for Bt maize: A social science perspective. `no licence`

<a id="pests-diseases-r"></a>

#### R

- [bbarker505/ddrp_v2](https://github.com/bbarker505/ddrp_v2) - A final production version of the DDRP platform that includes cohorts, parallel processing, and improving mapping routines. The objective of the Degree-Day, establishment Risk, and Pest event… `★ 12` `no licence`
- [emdelponte/r4pde](https://github.com/emdelponte/r4pde) - R package developed as a companion to the book "R for Plant Disease Epidemiology" (R4PDE). `★ 7` `custom licence`
- [TREC-Agroecology/aflatoxin](https://github.com/TREC-Agroecology/aflatoxin) - This is a repository for data and code associated with modeling aflatoxin contamination and risk in peanut. `★ 6` `no licence`
- [bbarker505/ddrp_v3](https://github.com/bbarker505/ddrp_v3) - An updated version of the DDRP platform (from v2) that uses newer R packages ("terra" and "sf"). The objective of the Degree-Day, establishment Risk, and Pest event mapping system (DDRP) is to… `★ 4` `no licence`
- [nosnibor27/soil_fusarium_model](https://github.com/nosnibor27/soil_fusarium_model) - Treating highly variable fungal soil population like flood data, attaching a weather-based proxy for soil moisture, and forecasting future shifts under climate change. `★ 4` `no licence`
- [bzbradford/cpn-crop-risk-tool](https://github.com/bzbradford/cpn-crop-risk-tool) - R Shiny app for viewing and downloading weather data and crop risk models. `★ 3` `MIT`
- [EcologyR/mappestRisk](https://github.com/EcologyR/mappestRisk) - Create Maps Forecasting Risk of Pest Occurrence. `★ 3` `GPL-3.0`
- [IhsanKhaliq/ascotraceR](https://github.com/IhsanKhaliq/ascotraceR) - A mechanistic model to simulate the spread of Ascochyta blight in a chickpea field. `★ 3` `custom licence`
- [junqi108/Grapevine_Botrytis_disease_model](https://github.com/junqi108/Grapevine_Botrytis_disease_model) - No description provided. `★ 3` `no licence`
- [bbarker505/ddrp-cohorts-v1](https://github.com/bbarker505/ddrp-cohorts-v1) - The objective of the Degree-Day, establishment Risk, and Pest event mapping system (DDRP) is to predict phenology and climate suitability of invasive, biocontrol, and IPM species for the… `★ 2` `no licence`
- [UW-Madison-DSI/crop_disease_forecasting_tool](https://github.com/UW-Madison-DSI/crop_disease_forecasting_tool) - This open source plant disease forecasting API and Dashboard opens new opportunities for proactive and data-driven decision-making in agriculture. `★ 2` `custom licence`
- [cbchisanga/Global-Late-Blight-MetaModelling](https://github.com/cbchisanga/Global-Late-Blight-MetaModelling) - R Scripts and supporting data for creating metamodels, as published in Ecosphere, and using them to generate global estimates of potato late blight risk based on climate data as published in Global… `★ 1` `GPL-2.0`
- [cesaraustralia/darabug2](https://github.com/cesaraustralia/darabug2) - A tool for predicting the phenology of invertebrate crop pests across Australia. `★ 1` `no licence`
- [da94829/Peanut-Aflatoxin-Project](https://github.com/da94829/Peanut-Aflatoxin-Project) - No description provided. `★ 1` `no licence`
- [felipedevargas/weather-based-model](https://github.com/felipedevargas/weather-based-model) - A weather-based model for predicting inoculum build-up, dispersal and infection by the wheat blast pathogen. `★ 1` `no licence`
- [GeoModelLab/FraNchEstYN](https://github.com/GeoModelLab/FraNchEstYN) - Framework for synchronous estimation of yield reduction. `★ 1` `custom licence`
- [PaulMelloy/viticolR](https://github.com/PaulMelloy/viticolR) - A mechanistic compartment model to assist in fungicide decision support for downy mildew infections in grapevines. `★ 1` `GPL-3.0`
- [alexblake1290/phenology](https://github.com/alexblake1290/phenology) - Evolving archive/tutorial for phenology models. `no licence`
- [ames-fowler/rkn_degree_day_tool](https://github.com/ames-fowler/rkn_degree_day_tool) - R shiny app example of a degree day pest management tool with a leaflet and open-meteo api utility for specific location soil temperature. `MIT`
- [Aria-Dolatabadian/Examples-of-growth-models-for-plant-disease-progress](https://github.com/Aria-Dolatabadian/Examples-of-growth-models-for-plant-disease-progress) - No description provided. `no licence`
- [Arnoldkirui/Pest_Risk_Kenya](https://github.com/Arnoldkirui/Pest_Risk_Kenya) - Open pest early-warning pipeline for tomato leafminer and whitefly - Kirinyaga County, Kenya. `MIT`
- [ben-ovenden/leaf-blast-epirice](https://github.com/ben-ovenden/leaf-blast-epirice) - Weekly rice leaf blast risk using the EPIRICE model (Savary et al. 2012), driven by Open-Meteo weather. Runs on GitHub Actions and emails a risk map. `no licence`
- [BrandonJVanderbush/ACMV_Project](https://github.com/BrandonJVanderbush/ACMV_Project) - Modeling the spread of the African Cassava mosaic virus through simple SI equations, and determining best intervention methods through manipulation of variables. `no licence`
- [clarkevansteenderen/CRI-1388-fruitfly-modelling](https://github.com/clarkevansteenderen/CRI-1388-fruitfly-modelling) - Citrus Research International (CRI) Project 1388: fruit fly mortality predictions using modelling approaches. `no licence`
- [cran/phenModel](https://github.com/cran/phenModel) - :exclamation: This is a read-only mirror of the CRAN R package repository. phenModel — Insect Phenology Model Evaluation Based on Daily Temperatures. `no licence`
- [cran/TrackTrap](https://github.com/cran/TrackTrap) - :exclamation: This is a read-only mirror of the CRAN R package repository. TrackTrap — Model Cumulative Growing Degree-Days for Pest Monitoring. `custom licence`
- [deoclecioamorim/seinfitR](https://github.com/deoclecioamorim/seinfitR) - Modeling the Relationship Between Nematode Densities and Plant Growth. `custom licence`
- [dslabcena/seinfitR](https://github.com/dslabcena/seinfitR) - Modeling the Relationship Between Nematode Densities and Plant Growth. `GPL-3.0`
- [HelenKettle/HopperModel](https://github.com/HelenKettle/HopperModel) - Model code for the paper: "Quantifying parasitoid and predator controls on rice hopper eggs using a dynamic stage-structured model and field data". `GPL-3.0`
- [icaruso21/Insect-Phenology-Forecaster](https://github.com/icaruso21/Insect-Phenology-Forecaster) - An interactive R-Shiny based insect phenology forecasting tool built on Leaflet and Plotly sourcing current and historical weather data from gridMET and GHCND. `no licence`
- [jekaterina-butkevica/dbm_project](https://github.com/jekaterina-butkevica/dbm_project) - A reproducible R workflow for identifying candidate Plutella xylostella generation intervals from pheromone trap data and modelling their temperature-dependent development. `no licence`
- [jrodriguez88/Model_Diseases](https://github.com/jrodriguez88/Model_Diseases) - Script to plot growth models for plant disease progress. `no licence`
- [KuldeepSJadon/epirice](https://github.com/KuldeepSJadon/epirice) - Simulation modelling of rice crop diseases. `GPL-3.0`
- [LauraMansier/ArableLandscape-PestControl](https://github.com/LauraMansier/ArableLandscape-PestControl) - "Modeling the dynamics of pest-regulating hoverflies and their aphid prey across various agricultural and non-crop habitats. This repository includes the model code used to simulate the impact of… `no licence`
- [MarEsponda/CBSD_model](https://github.com/MarEsponda/CBSD_model) - R scripts for the creation, proccess and analysis of the Cassava Brown Streak Disease Model for the Southeast Asia. `MIT`
- [mauricio-fernandes/wheat-blast](https://github.com/mauricio-fernandes/wheat-blast) - No description provided. `no licence`
- [mladencucak/epiCrop](https://github.com/mladencucak/epiCrop) - Set of functions and data for crop disease epidemiology work. `no licence`
- [pablostat/ILCYM_Predictor](https://github.com/pablostat/ILCYM_Predictor) - To improve accessibility for plant health researchers through an interactive website called ILCYM Predictor, which allows users to choose validated pest or natural enemy models developed in ILCYM… `GPL-3.0`
- [PaulMelloy/cercospoRa](https://github.com/PaulMelloy/cercospoRa) - A R package for determining the timing of Cercospora beticola epidemics in sugar beet. `custom licence`
- [pridiltal/cropguard](https://github.com/pridiltal/cropguard) - The riceblast package provides data and tools for forecasting rice blast disease outbreaks using weather-based parameters. `no licence`
- [ravimm2099/PhytoEpiQuant](https://github.com/ravimm2099/PhytoEpiQuant) - PhytoEpiQuant is an R Shiny GUI for plant disease epidemiology, integrating disease assessment, epidemic modelling, AUDPC, statistical and spatial analyses, interactive 3D PCA, exploratory… `custom licence`
- [rretkute/PestDynamicsAndDispersal](https://github.com/rretkute/PestDynamicsAndDispersal) - A framework for modelling migratory pest population dynamics and large-scale dispersal. `no licence`
- [SaviKoissi/SamplingEstimation](https://github.com/SaviKoissi/SamplingEstimation) - No description provided. `no licence`
- [smallfruitUMD/DF2-NN_GH2-DT_for_field_trials](https://github.com/smallfruitUMD/DF2-NN_GH2-DT_for_field_trials) - This is two ripe rot models that have been adapted for utilization with vineyard envrionmental and phenological data for the prediction of ripe rot risk. `no licence`
- [wsu-das/MatingDisruptionCM](https://github.com/wsu-das/MatingDisruptionCM) - This code emulates mating disruption effects of codling moth phenology models described in Pest Manag Sci 2021; 77: 1081–1093 and implemented in the pesticide evaluator tool in DAS. `no licence`
- [Yo-B/dynapop-oft](https://github.com/Yo-B/dynapop-oft) - A population dynamics model accounting for the individual process of resource foraging on heterogeneous agricultural landscapes. `GPL-3.0`

<a id="pests-diseases-shell"></a>

#### Shell

- [ca500/SWEDEN_NAME_runs](https://github.com/ca500/SWEDEN_NAME_runs) - Running NAME model for Sweden wheat stem rust. `no licence`

<a id="pests-diseases-typescript"></a>

#### TypeScript

- [Canborda/Epidemiology-in-rice-backend](https://github.com/Canborda/Epidemiology-in-rice-backend) - This web application explores the Google Earth Engine API to fit models that help to predict the status of rice crops. `MIT`

<a id="pests-diseases-wolfram-language"></a>

#### Wolfram Language

- [JuanD-Pimiento/Feedback-Control-for-Pest-Population-Systems](https://github.com/JuanD-Pimiento/Feedback-Control-for-Pest-Population-Systems) - Simulations of feedback controllers for 3 models of pests population dynamics. `custom licence`
- [sebrodfal/DiaphorinaModel](https://github.com/sebrodfal/DiaphorinaModel) - Numerical implementations used to model parasitoid-based population control in citrus agroecosystems. `no licence`

<a id="pests-diseases-other"></a>

#### Other

- [beart01/SWD-population-dynamics](https://github.com/beart01/SWD-population-dynamics) - This is a Leslis Matrix- style simulation for population dynamics of spotted-wing drosophila (SWD) (Drosophila suzukii; Diptera: Drosophilidae). It uses temperature and host availibility data (crop… `no licence`
- [jbenma/PsySpread](https://github.com/jbenma/PsySpread) - An IBM model to simulate the colonization and spread of a vector of HLB (e.g. Trioza erytreae or Diaphorina citri) throughout an hypothetical citrus orchard. `no licence`
- [mesgaran-lab/broomrape-gdd-calculator](https://github.com/mesgaran-lab/broomrape-gdd-calculator) - Growing Degree Day (GDD) calculator for branched broomrape in California processing tomato. `no licence`
- [mladencucak/Modelling_Nematode_Populations](https://github.com/mladencucak/Modelling_Nematode_Populations) - This document recreates the models for population densities of _Pratylenchus thornei_ as described in "Modelling population densities of root-lesion nematode (_P. thornei_) from soil profile… `MIT`
- [MoralesCastilla/MaCroPheST](https://github.com/MoralesCastilla/MaCroPheST) - Macroecological forecasting of Crop-pest Phenology across Space and Time. `no licence`
- [pannareeb/EpidemiologyRiceTungroDisease](https://github.com/pannareeb/EpidemiologyRiceTungroDisease) - &#91;R&#93; Deterministic model based on synergistic relationship between viruses - Stochastic model built by using Gillespies' Direct Method. `no licence`
- [TomKenda/Modeling_beet-root_and_nematodes_interactions](https://github.com/TomKenda/Modeling_beet-root_and_nematodes_interactions) - In the project we tryed to model the interactions between beet's root and the nematodes to understand how root architecture could affect the nematodes population. We did this by combining, root… `CC0-1.0`
- [YanMaldonado/Netlogo-HTML-JS](https://github.com/YanMaldonado/Netlogo-HTML-JS) - A reproducible web-based agent-based simulation framework for analyzing coffee leaf rust infection dynamics under agrometeorological scenarios. `no licence`

<a id="hydrology"></a>

### Hydrology, erosion and watersheds

<a id="hydrology-c"></a>

#### C

- [PSUmodeling/MM-PIHM](https://github.com/PSUmodeling/MM-PIHM) - Multi-Modular Penn State Integrated Hydrologic Model. `★ 19` `MIT`
- [PSUmodeling/BioRT-Flux-PIHM](https://github.com/PSUmodeling/BioRT-Flux-PIHM) - Watershed Biogeochemistry Model (the biogeochemical reactive transport model of PIHM family code). `★ 8` `MIT`
- [hydrotian/VIC_irr](https://github.com/hydrotian/VIC_irr) - VIC irrigation model based on VIC 4.2.a. `★ 2` `GPL-2.0`
- [liujunzhi321/SEIMS](https://github.com/liujunzhi321/SEIMS) - Spatially Explicit Integrated Modeling System. `★ 1` `GPL-2.0`
- [mingliangwsu/VCS](https://github.com/mingliangwsu/VCS) - VIC-CropSyst V5. `no licence`
- [Shenfang1993/SEIMS_PADDY](https://github.com/Shenfang1993/SEIMS_PADDY) - Spatially Explicit Integrated Modeling System --- open-source, cross-platform, and high performance computation. `GPL-2.0`

<a id="hydrology-csharp"></a>

#### C#

- [jjmonebi/Water-Balance-Modelling](https://github.com/jjmonebi/Water-Balance-Modelling) - A desktop app for simulating runoff from rainfall and potential evapotranspiration data. `no licence`

<a id="hydrology-cplusplus"></a>

#### C++

- [lreis2415/SEIMS](https://github.com/lreis2415/SEIMS) - Spatially Explicit Integrated Modeling System --- open-source, cross-platform, and high performance computation. `★ 58` `GPL-3.0`
- [ARPA-SIMC/CRITERIA3D](https://github.com/ARPA-SIMC/CRITERIA3D) - CRITERIA-3D is a three-dimensional agro-hydrological model. `★ 38` `GPL-3.0`
- [jx-qqq/SEIMSBMPUpdate](https://github.com/jx-qqq/SEIMSBMPUpdate) - No description provided. `★ 1` `GPL-3.0`
- [mingliangwsu/VIC-CropSyst-Package](https://github.com/mingliangwsu/VIC-CropSyst-Package) - No description provided. `no licence`

<a id="hydrology-fortran"></a>

#### Fortran

- [swat-model/swatplus](https://github.com/swat-model/swatplus) - Watershed soil, water, and agricultural management process simulations. `★ 86` `LGPL-2.1`
- [crazyzlj/SWAT](https://github.com/crazyzlj/SWAT) - An unofficial SWAT (Soil & Water Assessment Tool) code collection from official historical releases and the scientific community. `★ 80` `no licence`
- [smwesten-usgs/swb](https://github.com/smwesten-usgs/swb) - Soil-Water-Balance: A Modified Thornthwaite-Mather Soil-Water-Balance Code for Estimating Groundwater Recharge. `★ 42` `custom licence`
- [smwesten-usgs/swb2](https://github.com/smwesten-usgs/swb2) - SWB 2.0: a refactored version of the Soil-Water-Balance code. `★ 25` `custom licence`
- [mlt/swat](https://github.com/mlt/swat) - SWAT is a river basin scale model developed to quantify the impact of land management practices in large, complex watersheds. SWAT is a public domain model actively supported by the USDA… `★ 10` `custom licence`
- [cran/SWATmodel](https://github.com/cran/SWATmodel) - :exclamation: This is a read-only mirror of the CRAN R package repository. SWATmodel — A multi-OS implementation of the TAMU SWAT model. `★ 7` `no licence`
- [JayandraShrestha/ROSMan](https://github.com/JayandraShrestha/ROSMan) - A new hydropower reservoir routine (ROSMan) into the SWAT model. `★ 6` `BSD-2-Clause`
- [modflow-owhm/mf-owhm](https://github.com/modflow-owhm/mf-owhm) - GitHub Mirror of https://code.usgs.gov/modflow/mf-owhm USGS Homepage: https://www.usgs.gov/software/modflow-one-water-hydrologic-flow-model-mf-owhm. `★ 6` `custom licence`
- [ougx/unswat](https://github.com/ougx/unswat) - A hydrologic model coupling a Richards' equation with the SWAT model. `★ 6` `no licence`
- [ryanpmcg/WEPP-WQ](https://github.com/ryanpmcg/WEPP-WQ) - Water Erosion Prediction Project Water Quality (WEPP-WQ) Model Code. `★ 5` `AGPL-3.0`
- [ShengLanLuKPHDK/SWATAU](https://github.com/ShengLanLuKPHDK/SWATAU) - New modules developed for Soil and Water Assessment Tool (SWAT) revision 664. `★ 5` `no licence`
- [spark-hydro/SWAT-MODFLOW3](https://github.com/spark-hydro/SWAT-MODFLOW3) - SWAT-MODFLOW3 model. `★ 5` `LGPL-2.1`
- [JiangCong1990/AHMS-IRRIG](https://github.com/JiangCong1990/AHMS-IRRIG) - Atmospheric and Hydrological Modelling System integrated IRRigation module (AHMS-IRRIG) (Jiang et al., 2022). `★ 3` `no licence`
- [swat-model/swat2012](https://github.com/swat-model/swat2012) - SWAT development migrated from Bitbucket. `★ 3` `no licence`
- [Arcenic4444/swatplus-SFS](https://github.com/Arcenic4444/swatplus-SFS) - An extended SWAT+ model (SWAT+SFS) for simulating temporally heterogeneous and rainfall-responsive fertilization in smallholder farming systems. `★ 2` `no licence`
- [junyuqi1984/SWAT-FT](https://github.com/junyuqi1984/SWAT-FT) - An enhanced SWAT model with a physically-based soil temperature module. `★ 2` `no licence`
- [XYang-EcoHydroWQ/mHM-Nitrate_v2.0](https://github.com/XYang-EcoHydroWQ/mHM-Nitrate_v2.0) - A fully distributed, process-based catchment nitrate model. `★ 2` `custom licence`
- [Arcenic4444/swatplus-otherFert](https://github.com/Arcenic4444/swatplus-otherFert) - A debugged version of the SWAT+ model modified to support regular and custom fertilization functions, including multi-modal and temporally distributed fertilizer application schemes. `★ 1` `no licence`
- [C-SPA/SWATFarm](https://github.com/C-SPA/SWATFarm) - SWAT Model * Farm Routines. `★ 1` `GPL-3.0`
- [celray/swatplus_transient_lu](https://github.com/celray/swatplus_transient_lu) - This is the repo for developing land use update aternatives through decision tables. `★ 1` `no licence`
- [gpignotti/swat_swc](https://github.com/gpignotti/swat_swc) - No description provided. `★ 1` `no licence`
- [IchinoseHimeki/SWAT-SNOW](https://github.com/IchinoseHimeki/SWAT-SNOW) - A modified SWAT Model Accordingly. `★ 1` `GPL-3.0`
- [Jippe-FAO/GlobWat](https://github.com/Jippe-FAO/GlobWat) - Global water balance model to assess water use in irrigated agriculture. `★ 1` `MIT`
- [JosePedroMatos/SWATADAPT](https://github.com/JosePedroMatos/SWATADAPT) - Modifications of the African Dams Project (ADAPT) to the Soil & Water Assessment Tool (SWAT) hydrological model. `★ 1` `no licence`
- [jsta/swatr](https://github.com/jsta/swatr) - A multi-OS implementation of the TAMU SWAT model. `★ 1` `no licence` `archived`
- [junyuqi1984/SWAT-WE](https://github.com/junyuqi1984/SWAT-WE) - SWAT for coupled Water Energy cycling from soil to stream. `★ 1` `no licence`
- [kevin-wallington/SWAT_P.RR](https://github.com/kevin-wallington/SWAT_P.RR) - SWAT+P.R&R source code, input files for the Upper Sangamon watershed, and list of bugs in SWAT+. `★ 1` `MIT`
- [kwanghun/DMMF](https://github.com/kwanghun/DMMF) - An R package for estimating runoff and soil erosion rate on a daily basis using DMMF soil erosion model. `★ 1` `no licence`
- [nfmsu/Integrated_models](https://github.com/nfmsu/Integrated_models) - Integrated SWAT_MODFLOW_DSSAT. `★ 1` `CC-BY-4.0`
- [nfmsu/SWAT-MODFLOW_DSSAT](https://github.com/nfmsu/SWAT-MODFLOW_DSSAT) - This repository is original code of SWAT modflow- SWAT Mar 17 2015 VER 2012/Rev 636_smrt. `★ 1` `Unlicense`
- [ougx/SWATSA](https://github.com/ougx/SWATSA) - A modified SWAT model accounting for bidirectional interactions. `★ 1` `no licence`
- [StoneEnv/SwatPestPlantUptake](https://github.com/StoneEnv/SwatPestPlantUptake) - Extended SWAT model to account for chemical plant uptake as described in HESS Technical Note (https://doi.org/10.5194/egusphere-2025-877). This version also includes transport of chemicals through… `★ 1` `no licence`
- [thanhnh-infinity/thanhnh-apex0806](https://github.com/thanhnh-infinity/thanhnh-apex0806) - APEX – Agricultural Policy/Environmental eXtender Model. `★ 1` `no licence`
- [TheSoilman/EUROSEM](https://github.com/TheSoilman/EUROSEM) - Source code, documentation and user manual for the European Soil Erosion model. `★ 1` `CC0-1.0` `archived`
- [AARTHI-PADMANABHAN/SWATplus_development](https://github.com/AARTHI-PADMANABHAN/SWATplus_development) - Developed Fortran subroutines with HDF5 and MPI integration for the SWAT+ model, replacing CSV outputs to improve data storage efficiency and processing speed. Conducted an experimental approach by… `no licence`
- [ankwasa/wetlands_swatplus](https://github.com/ankwasa/wetlands_swatplus) - implementing wetlands in the swatplus source code. `MIT`
- [ARS-SWRC/rhem_engine_cligen](https://github.com/ARS-SWRC/rhem_engine_cligen) - No description provided. `MIT`
- [dailyerosion/dep](https://github.com/dailyerosion/dep) - Iowa Daily Erosion Project (version 2). `MIT`
- [edf-org/edf_custom_swat](https://github.com/edf-org/edf_custom_swat) - custom fork of SWAT2012. `GPL-3.0`
- [fanjiawei6/pflotran_ET](https://github.com/fanjiawei6/pflotran_ET) - PFLOTRAN with an ET module for simulating field-scale hydrology in tile-drained agroecosystems. `custom licence`
- [grmpfhmbl/swatmodel-trusty64](https://github.com/grmpfhmbl/swatmodel-trusty64) - SWAT 2012 source with a build setup for gfortran on Ubuntu. `CC0-1.0`
- [JuancaLazo23/Swat_PrN_prob](https://github.com/JuancaLazo23/Swat_PrN_prob) - No description provided. `MIT`
- [nsammons/swatplus](https://github.com/nsammons/swatplus) - SWAT modular code creation of repository. `no licence`
- [oshs/SWAT-DF](https://github.com/oshs/SWAT-DF) - Customized SWAT2012 with integrated microeconomic model for dynamic crop allocation, water availability response. `no licence`
- [oshs/SWAT-SOC](https://github.com/oshs/SWAT-SOC) - Customized SWAT2012 version with integrated micro-economic decision modelling for dynamic crop allocation, water availability response, and hydro-economic scenario analysis. Includes modified source… `GPL-3.0`
- [ougx/rev637_source_irri](https://github.com/ougx/rev637_source_irri) - This is a SWAT model with modifications to the irrigation component. `no licence`
- [RevanthMamidala/SWATPlus_Rev-ControlDrainage](https://github.com/RevanthMamidala/SWATPlus_Rev-ControlDrainage) - The repository contains control drainage application of SWAT+ Rev model, a modified version of SWAT+ Version 61.0.2. `no licence`
- [StoneEnv/SwatPestTileGw](https://github.com/StoneEnv/SwatPestTileGw) - Extended SWAT model to transport chemicals through tile and groundwater flow as described in HESS Technical Note. `no licence`
- [swat-model/SWIFT](https://github.com/swat-model/SWIFT) - No description provided. `LGPL-2.1`
- [WelberFerreira/SWAT-Model-664-CN-GW](https://github.com/WelberFerreira/SWAT-Model-664-CN-GW) - SWAT hydrological model version 664 (modified). This version was modified in order to allow changes in lambda relates to SCS-CN and groundwater delay. `no licence`
- [xiekangwhu/CWSC_monthly_water_balance_models](https://github.com/xiekangwhu/CWSC_monthly_water_balance_models) - Soil moisture storage capacity (SMSC) links the atmosphere and terrestrial ecosystems, which is required as spatial parameters for geoscientific models, but there are currently no available… `GPL-3.0`

<a id="hydrology-javascript"></a>

#### JavaScript

- [VasilisAle/RUSLE_model_in_GEE](https://github.com/VasilisAle/RUSLE_model_in_GEE) - General RUSLE model. `★ 11` `MIT`
- [VasilisAle/Modified_RUSLE_model](https://github.com/VasilisAle/Modified_RUSLE_model) - RUSLE model. `★ 8` `MIT`

<a id="hydrology-mathematica"></a>

#### Mathematica

- [SimulationEverywhere-Models/CDPP-SOIL-EROSION](https://github.com/SimulationEverywhere-Models/CDPP-SOIL-EROSION) - It models the effects of uniform rain falling on a volume of earth as the rain falls. It is represented as a 4D model, each 3D plane representing a different phenomenon. `no licence`

<a id="hydrology-matlab"></a>

#### MATLAB

- [myli1993/DDPM_ver1.0](https://github.com/myli1993/DDPM_ver1.0) - Distributed dynamic process model (DDPM) is a bidirectional coupling eco-hydrological model for (but not limited to) steppe inland river basins in arid and semi-arid regions, which is driven by… `★ 10` `GPL-3.0`
- [HanneVG/AquaCrop-Hydro](https://github.com/HanneVG/AquaCrop-Hydro) - AquaCrop-Hydro model code and related scripts. `★ 2` `MIT`
- [SoilWaterLab/matlab-hct-chem](https://github.com/SoilWaterLab/matlab-hct-chem) - MATLAB HCT-chem model, used with USDA WEPP to predict hillslope transport of phosphorus, nitrogen and pesticides. `★ 1` `no licence`

<a id="hydrology-netlogo"></a>

#### NetLogo

- [kavinpreethi/WATERING_IRRIGATION_RBB](https://github.com/kavinpreethi/WATERING_IRRIGATION_RBB) - A NetLogo Reusable Building Block (RBB) model to simulate water flow in an irrigation scheme. `★ 1` `MIT`

<a id="hydrology-perl"></a>

#### Perl

- [wsag/wbm-ncascade](https://github.com/wsag/wbm-ncascade) - Branch of WBM used for enhanced agricultural nitrogen processing. `no licence`

<a id="hydrology-python"></a>

#### Python

- [wieka29/RUSLE_GEE](https://github.com/wieka29/RUSLE_GEE) - The RUSLE model on Google Earth Engine. `★ 27` `no licence`
- [rogerlew/wepppy](https://github.com/rogerlew/wepppy) - No description provided. `★ 19` `custom licence`
- [songjun-wu/EcoTWIN](https://github.com/songjun-wu/EcoTWIN) - EcoTWIN. `★ 15` `GPL-3.0`
- [NOAA-OCM/QNSPECT](https://github.com/NOAA-OCM/QNSPECT) - QGIS Plugin for NOAA Nonpoint Source Pollution and Erosion Comparison Tool (NSPECT). `★ 13` `GPL-2.0`
- [juannat7/qgis_soil_erosion](https://github.com/juannat7/qgis_soil_erosion) - This QGIS plugin takes in precipitation level, DEM, and shapefile boundary (Malaysia context) to generate soil erosion risk assessment based on the Revised Universal Soil Loss Equation (RUSLE). `★ 9` `GPL-2.0`
- [nriveras/RUSLE](https://github.com/nriveras/RUSLE) - Revised Universal Soil Loss Equation (RUSLE) implemented in google earth engine (GEE) with the python-API. `★ 8` `no licence`
- [Yang12960821/-SWAT-DayCent-](https://github.com/Yang12960821/-SWAT-DayCent-) - 软著项目代码文件. `★ 6` `no licence`
- [cylin928/PyCHAMP](https://github.com/cylin928/PyCHAMP) - PyCHAMP (Crop-Hydrological-Agent Modeling Platform) is an open-source Python package specifically developed for analyzing policies and assessing decision-making processes in agro-hydrological systems. `★ 4` `BSD-3-Clause`
- [Moisture-Matters/fluxpark](https://github.com/Moisture-Matters/fluxpark) - FluxPark. A Spatially-explicit hydrological model for simulating evaporation fluxes and groundwater recharge. `★ 4` `custom licence`
- [acellular/erosion_flow](https://github.com/acellular/erosion_flow) - A QGIS plugin with processing algorithms for erosion analysis on DEMs (digital elevation models) using the RUSLE and USPED models. `★ 3` `MIT`
- [ajoros/bcm-py-daily](https://github.com/ajoros/bcm-py-daily) - Python port of USGS BCM Daily. `★ 3` `custom licence`
- [AleenaTahir1/Adaptive-water-extraction](https://github.com/AleenaTahir1/Adaptive-water-extraction) - Mesa-based agent-based model simulating irrigator farmers who share a common water resource (river / aquifer) and learn extraction strategies via tabular Q-learning. `★ 3` `no licence`
- [davefavismortlock/FieldFlow](https://github.com/davefavismortlock/FieldFlow) - FieldFlow is a software tool that identifies and characterises those landscape elements which affect flow routing patterns in a catchment. It can be used as a kind of preprocessor, to be run before… `★ 3` `no licence`
- [ec-jrc/lisflood-epic](https://github.com/ec-jrc/lisflood-epic) - No description provided. `★ 3` `no licence`
- [KMouris/Sediment_Load_Calculation](https://github.com/KMouris/Sediment_Load_Calculation) - Model chain to compute sediment loads using RUSLE and the SEDD model. `★ 3` `GPL-3.0`
- [rlilhare/Modified-MMF-Morgan-Morgan-Finney-model](https://github.com/rlilhare/Modified-MMF-Morgan-Morgan-Finney-model) - Modified MMF (Morgan–Morgan–Finney) model (2008) "in Python" for evaluating effects of crops and vegetation cover on soil erosion. `★ 3` `no licence`
- [maheaneja/sle_rusle](https://github.com/maheaneja/sle_rusle) - Soil loss estimation based on RUSLE model using python. `★ 2` `no licence`
- [Nick-Kinsella/RUSLE-in-Python](https://github.com/Nick-Kinsella/RUSLE-in-Python) - (WORK IN PROGRESS) Revised Universal Soil Loss Equation made in a Python Jupyter notebook. Free to download and use. `★ 2` `MIT`
- [Odzinic/RUSLE](https://github.com/Odzinic/RUSLE) - No description provided. `★ 2` `no licence`
- [roushankumar11/Soil-Loss-Estimation](https://github.com/roushankumar11/Soil-Loss-Estimation) - The Universal Soil Loss Equa- tion (USLE), an empirical modelling approach, is introduced along with its factors: rainfall erosivity, soil erodibility, slope length-gradient, land cover and… `★ 2` `no licence`
- [smwesten-usgs/pyswb](https://github.com/smwesten-usgs/pyswb) - Experimental soil-water-balance code in Python. `★ 2` `CC0-1.0`
- [SnehaChevuru/Coupled_PCR-GLOBWB2-WOFOST_model_framework](https://github.com/SnehaChevuru/Coupled_PCR-GLOBWB2-WOFOST_model_framework) - A new fully coupled PCR-GLOBWB2 - WOFOST model framework is developed to include the feedbacks between crop growth and hydrology. `★ 2` `no licence`
- [celray/wetspass-M](https://github.com/celray/wetspass-M) - WetSPASS-M is a spatially distributed water balance model for simulating groundwater recharge, soil water storage, evapotranspiration, runoff, and interception at monthly, seasonal, and annual… `★ 1` `no licence`
- [cylin928/AgriHydro](https://github.com/cylin928/AgriHydro) - Agriculture and Hydrological assessment model. `★ 1` `no licence`
- [dzn1254/RUSLE-Project](https://github.com/dzn1254/RUSLE-Project) - 批量计算土壤侵蚀. `★ 1` `no licence`
- [Lafto/wetspass_modern](https://github.com/Lafto/wetspass_modern) - Modernized Wetspass-M 2016 — spatially distributed monthly water balance for QGIS. Adds a dynamic soil-water bucket, GeoTIFF I/O, automatic spin-up convergence, focused recharge, and a mass balance… `★ 1` `custom licence`
- [matfran/WaTEM_SEDEM_dynamic_EU](https://github.com/matfran/WaTEM_SEDEM_dynamic_EU) - The code respository for a multitemporal implementation of the WaTEM/SEDEM soil erosion and sediment delivery model. `★ 1` `no licence`
- [mjasher/integrated](https://github.com/mjasher/integrated) - Integrated surface water, groundwater, farm process, water policy, ecological model. `★ 1` `no licence`
- [trngbich/Waterbal](https://github.com/trngbich/Waterbal) - :file_folder: Simple Waterpix model based on Water Balance. `★ 1` `Apache-2.0`
- [ajprice16/swatplus-modflow6-coupling](https://github.com/ajprice16/swatplus-modflow6-coupling) - No description provided. `MIT`
- [antonioannis/flood-risk-agriculture](https://github.com/antonioannis/flood-risk-agriculture) - Modular Python framework for agricultural flood risk: vine-copula/cascade stochastic storm generation, HEC-RAS 2D simulation, and phenology-aware crop damage modelling, producing seasonal… `MIT`
- [ARS-SWRC/RHEM-Snow-Standalone](https://github.com/ARS-SWRC/RHEM-Snow-Standalone) - No description provided. `MIT`
- [Deode22/rusle-cli](https://github.com/Deode22/rusle-cli) - Cálculo distribuido de erosión hídrica mediante RUSLE integrando Sentinel-2, MDT y SoilGrids. Incluye análisis de escenarios y generación de informes automáticos. `no licence`
- [DISES-PyCHAMP/PyCHAMP](https://github.com/DISES-PyCHAMP/PyCHAMP) - PyCHAMP: A Crop-Hydrological-Agent Modeling Platform. `BSD-3-Clause`
- [huangysh/RUSLE_model](https://github.com/huangysh/RUSLE_model) - RESLE for soil erosion modelling. `no licence`
- [kashingtonDC/cvwbm](https://github.com/kashingtonDC/cvwbm) - central valley water balance model. `custom licence`
- [l5d1l5/Ages](https://github.com/l5d1l5/Ages) - Agricultural Ecosystems Service (AgES) spatial watershed model. `no licence`
- [LabSid-USP/pywr-extension-irrigation](https://github.com/LabSid-USP/pywr-extension-irrigation) - No description provided. `GPL-3.0`
- [mojikone/RUSLE](https://github.com/mojikone/RUSLE) - No description provided. `no licence`
- [montimaj/Kydro](https://github.com/montimaj/Kydro) - Graf's soil erosion model implemented in Python 3. `GPL-3.0`
- [muzzy-141104/STEM](https://github.com/muzzy-141104/STEM) - Soil & Terrain Erosion Model. `no licence`
- [Nora-Research-Lab/rusle-soil-loss-estimator](https://github.com/Nora-Research-Lab/rusle-soil-loss-estimator) - For environmental geoscientists and land managers: enter rainfall erosivity, soil erodibility, slope, cover, and support practice factors to compute annual soil loss and erosion risk classification… `no licence`
- [omerorucu/erosense-qgis](https://github.com/omerorucu/erosense-qgis) - RUSLE-based soil erosion modelling + independent ML erosion susceptibility mapping (EroNet). Raster input, multiple algorithms, advanced spatial statistics. `MIT`
- [ruiduobao/geoskill-sediment-transport-modeling](https://github.com/ruiduobao/geoskill-sediment-transport-modeling) - RUSLE 土壤侵蚀模型 + 泥沙输移比(SDR)估算流域产沙量，识别关键泥沙源区. `MIT`
- [ruiduobao/geoskill-soil-erosion-modeling](https://github.com/ruiduobao/geoskill-soil-erosion-modeling) - RUSLE 模型空间化估算土壤侵蚀模数：A = R×K×L×S×C×P，含降雨侵蚀力、土壤可蚀性、坡长坡度、植被覆盖与水保措施六因子。Computes soil erosion modulus with RUSLE (R K L S C P) spatialized factors. 输出侵蚀模数与强度分级 GeoTIFF。. `MIT`
- [sertit/Rusle](https://github.com/sertit/Rusle) - No description provided. `GPL-3.0`
- [shirazipooya/WaterBalance](https://github.com/shirazipooya/WaterBalance) - No description provided. `GPL-3.0`
- [Shiruo-Hu/ABM-for-irrigation-efficiency-paradox](https://github.com/Shiruo-Hu/ABM-for-irrigation-efficiency-paradox) - An agent-based model to simulate farmers' water-land use dynamics in response to both technical irrigation efficiency improvements and economic policy adjustments. `no licence`
- [SongshGeoLab/CWatQIM](https://github.com/SongshGeoLab/CWatQIM) - Crop-Water Quota Irrigation Model. `Apache-2.0`
- [SWATGenX/swatplus-engine-acceleration](https://github.com/SWATGenX/swatplus-engine-acceleration) - Benchmarks & reproducibility for the accelerated SWAT+ engine — OpenMP HRU land phase (byte-identical), wavefront channel routing, NetCDF output, 7.14x end-to-end. `MIT`
- [YinZuotang/RUSLE-TLSD](https://github.com/YinZuotang/RUSLE-TLSD) - No description provided. `no licence`
- [Zhonghao2023/LAWS](https://github.com/Zhonghao2023/LAWS) - No description provided. `GPL-3.0`

<a id="hydrology-r"></a>

#### R

- [atsyplenkov/rusleR](https://github.com/atsyplenkov/rusleR) - An R package for soil erosion modeling. `★ 20` `custom licence`
- [SNO-HYBAM/SWATplusHybam](https://github.com/SNO-HYBAM/SWATplusHybam) - No description provided. `★ 5` `no licence`
- [sofiazaruchas/aridRUSLE](https://github.com/sofiazaruchas/aridRUSLE) - Implements a modified RUSLE approach for soil erosion risk analysis in semi-arid and arid regions using rainfall erosivity (R), topographic influence (LS), and vegetation cover (C) derived from… `★ 1` `custom licence`
- [AstroMac26/RUSLE_Arctic](https://github.com/AstroMac26/RUSLE_Arctic) - RUSLE-Arctic. `no licence`
- [fickse/RHEM](https://github.com/fickse/RHEM) - Rangeland Hydrology Erosion Model. `no licence`
- [jimmyokeeffe/jimmyokeeffe-Farmer_irrigation_behavior_sociohydrological_model_WRR2018](https://github.com/jimmyokeeffe/jimmyokeeffe-Farmer_irrigation_behavior_sociohydrological_model_WRR2018) - This repository contains code used in O'Keeffe, J., Moulds, S., Bergin E., Brozovic N., Mijic A., and Buytaert W., Including farmer irrigation behavior in a socio‐hydrological modelling framework… `no licence`
- [mrani307/PARAM](https://github.com/mrani307/PARAM) - Pixel-based Agro-hydrological model in R for water Accounting and Management. `MIT`
- [rutujact/blue-water](https://github.com/rutujact/blue-water) - A socio-hydrological framework to scale water budgets from plot to agrarian system. `LGPL-3.0`
- [Zhujiayaohello/APEX-SWAT-GW-model](https://github.com/Zhujiayaohello/APEX-SWAT-GW-model) - The linked APEX-SWAT-GW model was constructed to transfer variable values between the APEX and SWAT-GW simulation subroutines.The linking of these two models is forced by transferring the PRK (APEX… `no licence`

<a id="hydrology-reason"></a>

#### Reason

- [spark-hydro/AMRS](https://github.com/spark-hydro/AMRS) - APEX-MODFLOW-RT3D-Salt integrated model. `LGPL-2.1`

<a id="hydrology-rust"></a>

#### Rust

- [L4Ph/Rusle](https://github.com/L4Ph/Rusle) - Rust reimplementation version of ULE4JIS. `★ 1` `MIT`
- [rogerlew/openWEPP](https://github.com/rogerlew/openWEPP) - No description provided. `★ 1` `custom licence`

<a id="hydrology-shell"></a>

#### Shell

- [Vahidr32/PFAS-fate-and-transport-model](https://github.com/Vahidr32/PFAS-fate-and-transport-model) - This repository contains the source code for the most recent version of the SWAT-MODFLOW-RT3D (SMR-W) model, which we modified to simulate PFAS fate and transport at the watershed scale in the… `★ 4` `no licence`
- [mingliangwsu/VIC-CropSyst_v3_CRB](https://github.com/mingliangwsu/VIC-CropSyst_v3_CRB) - No description provided. `no licence`

<a id="hydrology-visual-basic"></a>

#### Visual Basic

- [bejranonda/coupling-model-SWAT-MODFLOW](https://github.com/bejranonda/coupling-model-SWAT-MODFLOW) - Modeling framework (2006): Surface and groundwater dynamic interactions is being explored. SWAT and MODFLOW, surface-soil water and groundwater models, are semi-coupled to determine flow behaviour… `no licence`

<a id="hydrology-other"></a>

#### Other

- [rtbailey8/SWAT_Salinity](https://github.com/rtbailey8/SWAT_Salinity) - Source code for original SWAT model and new salt transport subroutines. `★ 6` `no licence`
- [hooriajami/SMART](https://github.com/hooriajami/SMART) - A computationally efficient semi-distributed hydrologic modeling application for soil moisture and runoff simulation. `★ 5` `GPL-3.0`
- [RyanTBailey/SWAT-MODFLOW-Salt](https://github.com/RyanTBailey/SWAT-MODFLOW-Salt) - Source code for the hydro-chemical watershed model SWAT-MODFLOW-Salt. `★ 5` `no licence`
- [hongmingzhang/LS-factor](https://github.com/hongmingzhang/LS-factor) - Extension of a GIS procedure for calculating the RUSLE equation LS factor. `★ 3` `no licence`
- [lzq0129/SWATpld](https://github.com/lzq0129/SWATpld) - An improved version of SWAT model which is integrated with a polder module. `★ 3` `GPL-3.0`
- [m1s1m/SWAT-SF](https://github.com/m1s1m/SWAT-SF) - A flexible SWAT-based model for watershed-scale water and soil salinity modeling. `★ 2` `no licence`
- [JimmyQi1984/SolSWAT](https://github.com/JimmyQi1984/SolSWAT) - Soil moisture and heat transfer model coupled with SWAT. `★ 1` `no licence`
- [xiaogeiii/SWAT_CO2_FT](https://github.com/xiaogeiii/SWAT_CO2_FT) - Optimized Soil and Water Assessment Tool (SWAT) model including a dynamic CO2 input method and a Freeze-Thaw cycle module. `★ 1` `no licence`
- [aashi95/Modification-of-SWAT-Carbon-Plant-Growth-Module](https://github.com/aashi95/Modification-of-SWAT-Carbon-Plant-Growth-Module) - This repository contains modifications to the SWAT carbon plant growth module, improving forest dynamics and LAI simulation. It includes updated equations for capturing LAI senescence, adjustment… `no licence`
- [AlanOvidio/RUSLE-analyzer](https://github.com/AlanOvidio/RUSLE-analyzer) - An application to estimate potential soil erosion using a web implementation of the RUSLE equation. `no licence`
- [HaasHen/SWAT-Canopy-Interception](https://github.com/HaasHen/SWAT-Canopy-Interception) - This repository contains an .exe file with a modified canopy interception and evaporation method for the SWAT model. `no licence`
- [junyuqi1984/SWAT-CNP](https://github.com/junyuqi1984/SWAT-CNP) - The SWAT-CNP model integrates Century-based terrestrial C/N/P cycling with aquatic C/N/P dynamics based on QUAL2K/CE-QUAL-W2 frameworks. It is an extension of the previously published SWAT-Carbon… `no licence`
- [junyuqi1984/SWAT-IR](https://github.com/junyuqi1984/SWAT-IR) - SWAT model for intermittent rivers. `no licence`
- [junyuqi1984/SWAT-R](https://github.com/junyuqi1984/SWAT-R) - Richards-equation-based soil water movement with the sub-daily time step. `no licence`
- [NavajyothyN/Water-Model---Agricultural-Field](https://github.com/NavajyothyN/Water-Model---Agricultural-Field) - Spatially explicit Python model for agricultural water accounting (blue, green & grey water) following WFLDB v3.10 & ISO 14046. Computes all 5 water output flows as GeoTIFF rasters using Pfister et… `no licence`
- [trandhir/HydroSimGlobal](https://github.com/trandhir/HydroSimGlobal) - Advances watershed modeling. `MIT`

<a id="land-surface"></a>

### Land surface and global vegetation

<a id="land-surface-c"></a>

#### C

- [PIK-LPJmL/LPJmL](https://github.com/PIK-LPJmL/LPJmL) - Managed-land and vegetation simulations linking carbon and water cycles. `★ 98` `custom licence`
- [PecanProject/sipnet](https://github.com/PecanProject/sipnet) - Simplified Photosynthesis and Evapotranspiration Model: process-based ecosystem model for simulating carbon and water fluxes. `★ 42` `BSD-3-Clause`
- [JChen-UToronto/BEPS_hourly_site](https://github.com/JChen-UToronto/BEPS_hourly_site) - Bioshpere-atmosphere Exchange Process Simulator, hourly version for site. `★ 4` `GPL-3.0`
- [dorihidy/Biome-BGCMuSo](https://github.com/dorihidy/Biome-BGCMuSo) - No description provided. `★ 2` `no licence`
- [hidydora/Biome-BGCMuSo](https://github.com/hidydora/Biome-BGCMuSo) - Biogeochemical model simulating carbon, nitrogen and water fluxes of different vegetation types (derivating from Biome-BGC v4.1.1). `★ 2` `no licence`
- [mohamedAyache/LPJmL_version1](https://github.com/mohamedAyache/LPJmL_version1) - The source code of the LPJmL-Med version are available here through osupytheas gitlab server and should be referenced as Ayache et al. `★ 1` `no licence`
- [HDahlmann/lpjml_waterstress](https://github.com/HDahlmann/lpjml_waterstress) - No description provided. `AGPL-3.0`

<a id="land-surface-cplusplus"></a>

#### C++

- [dbampoh/LPJ-GUESS-integrated-LandSyMM](https://github.com/dbampoh/LPJ-GUESS-integrated-LandSyMM) - LPJ-GUESS 4.1 integrated with LandSyMM features — dual-mode codebase with runtime parameter switching. `MPL-2.0`

<a id="land-surface-fortran"></a>

#### Fortran

- [ESCOMP/CTSM](https://github.com/ESCOMP/CTSM) - Community Terrestrial Systems Model (includes the Community Land Model of CESM). `★ 352` `custom licence`
- [ArseneD/OPEN_SURFEX_V81_IRR](https://github.com/ArseneD/OPEN_SURFEX_V81_IRR) - New irrigation scheme in the ISBA land surface model, with the new ECOPLIMAP-SG vegetation description. It based on the open access SURFEX version 8.1 (ref f70f6454) under a CECILL-C License (French… `★ 1` `custom licence`
- [HuiminMeng/NoahMP_SE_root](https://github.com/HuiminMeng/NoahMP_SE_root) - Here, I have modified the Noah-MP-Cop model (https://github.com/NCAR/noahmp ) codes to develop a soil‑environment‑responsive dynamic root distribution scheme (SE_root) that accounts for soil… `★ 1` `no licence`
- [LYU1110/Noah-MP-Crop-Rotation-Extension](https://github.com/LYU1110/Noah-MP-Crop-Rotation-Extension) - Crop rotation module extension for Noah-MP Land Surface Model. Includes patches and modified files only. Requires original Noah-MP source code. `★ 1` `no licence`
- [YiYaoVUB/2022_Yao_etal_JAMES](https://github.com/YiYaoVUB/2022_Yao_etal_JAMES) - Scripts used for study: Implementation and evaluation of irrigation techniques in the Community Land Model. `★ 1` `no licence`
- [galaxyyouyouyouzi/SIBcrop](https://github.com/galaxyyouyouyouzi/SIBcrop) - No description provided. `no licence`
- [KNR8070/CLM5_IndianCrop_improvements](https://github.com/KNR8070/CLM5_IndianCrop_improvements) - No description provided. `no licence`
- [ShannonRoos/CTSM5.2_CropHeatStress](https://github.com/ShannonRoos/CTSM5.2_CropHeatStress) - code changes to CTSM5.2.019 to include crop heat stress functions. `custom licence`
- [Siqing-XU/ORCHIDEE-CROP](https://github.com/Siqing-XU/ORCHIDEE-CROP) - No description provided. `no licence`
- [zhangxianglinzju/ORCHIDEE-CROP-SOJ](https://github.com/zhangxianglinzju/ORCHIDEE-CROP-SOJ) - No description provided. `MIT`

<a id="land-surface-julia"></a>

#### Julia

- [jl-pkgs/ModernBEPS.jl](https://github.com/jl-pkgs/ModernBEPS.jl) - BEPS Evapotranspiration and Photosynthesis model in Julia. `★ 18` `GPL-3.0`

<a id="land-surface-python"></a>

#### Python

- [pnnl/JAX-CanVeg](https://github.com/pnnl/JAX-CanVeg) - No description provided. `★ 26` `custom licence`
- [jnnsbrr/landmanager](https://github.com/jnnsbrr/landmanager) - Models build with the copan:LPJmL framework. `★ 1` `AGPL-3.0`
- [e-workman/Biospheric_model](https://github.com/e-workman/Biospheric_model) - Model written to simulate the biosphere with the aim to find the total evapotranspiration and the mean carbon uptake under three different conditions: plants are not limited by soil water, soil… `no licence`
- [SatTerC/sgam](https://github.com/SatTerC/sgam) - The Simplified Growth and Allocation Model (SGAM) simulates the allocation of gross primary productivity (GPP) to plant carbon pools (leaves, stem, roots) across different plant types (tree, grass… `GPL-3.0`

<a id="land-surface-r"></a>

#### R

- [jnnsbrr/PhotoBioDynamics](https://github.com/jnnsbrr/PhotoBioDynamics) - Small model to simulate biomass production on a global scale. Products are Gross Primary Production (GPP), Net Primary Production (NPP). It is based on a modified version of the Farquhar approach… `★ 7` `MIT`

<a id="land-surface-other"></a>

#### Other

- [yufenghe22/cwrf-biocro](https://github.com/yufenghe22/cwrf-biocro) - No description provided. `no licence`

<a id="controlled-environment"></a>

### Greenhouses and controlled environments

<a id="controlled-environment-c"></a>

#### C

- [Sirokujira/OpenPPFD](https://github.com/Sirokujira/OpenPPFD) - No description provided. `MIT`

<a id="controlled-environment-csharp"></a>

#### C#

- [WindyGPTBot/PlantModelling](https://github.com/WindyGPTBot/PlantModelling) - Master Thesis about Plant Modelling in Controlled Environment Agriculture Systems. `no licence`

<a id="controlled-environment-cplusplus"></a>

#### C++

- [NorthernLoki/Horticulture_Tools](https://github.com/NorthernLoki/Horticulture_Tools) - No description provided. `★ 8` `custom licence`

<a id="controlled-environment-fortran"></a>

#### Fortran

- [kapil-161/DSSAT-HYDRO](https://github.com/kapil-161/DSSAT-HYDRO) - No description provided. `BSD-3-Clause`

<a id="controlled-environment-julia"></a>

#### Julia

- [JRockBB/PersonalGreenhouse](https://github.com/JRockBB/PersonalGreenhouse) - Backyard greenhouse simulation using Dyad. `no licence`

<a id="controlled-environment-matlab"></a>

#### MATLAB

- [YikaiZeng/GreenhouseSimulation](https://github.com/YikaiZeng/GreenhouseSimulation) - A Simulation Model for greenhouse inner climate. `★ 5` `no licence`
- [EfraimManurung/mini-greenhouse-greenlight-model](https://github.com/EfraimManurung/mini-greenhouse-greenlight-model) - No description provided. `★ 2` `no licence`
- [AMRprojects/GreenhouseControls](https://github.com/AMRprojects/GreenhouseControls) - Objective of project was to recreate a simulation from a published article and use the recreated simulation to obtain additional insights. Showcases proficiency in MATLAB and Simulink. Article found… `no licence`
- [dong0705/greenhouse-two-stage-optimization](https://github.com/dong0705/greenhouse-two-stage-optimization) - MATLAB code for greenhouse climate control and MPC-based multi-source irrigation scheduling under demand uncertainty. `MIT`
- [humaya/Vertical-Farm-Model-](https://github.com/humaya/Vertical-Farm-Model-) - The reference code of the paper. `BSD-3-Clause`
- [MinaAsghari/Greenhouse-Control-System-](https://github.com/MinaAsghari/Greenhouse-Control-System-) - MATLAB simulation and control of a smart greenhouse using PID controllers, dynamic modeling, and sustainability analysis. `no licence`
- [Zoeyzoey1220/Venlo-Greenhouse-Simulation-Platform-GUI](https://github.com/Zoeyzoey1220/Venlo-Greenhouse-Simulation-Platform-GUI) - No description provided. `no licence`

<a id="controlled-environment-modelica"></a>

#### Modelica

- [queraltab/Greenhouses-Library](https://github.com/queraltab/Greenhouses-Library) - The Greenhouse Modelica Library aims at providing a fully open-source modeling framework for the simulation of greenhouse climate, crop yield and the energy integration of greenhouses with thermal… `★ 56` `BSD-3-Clause`
- [cjchandler/solarGreenhouseV2](https://github.com/cjchandler/solarGreenhouseV2) - greenhouse simulation- unvalidated. `★ 1` `GPL-3.0`

<a id="controlled-environment-python"></a>

#### Python

- [davkat1/GreenLight](https://github.com/davkat1/GreenLight) - A platform for creating, modifying, and combining dynamic models, with a focus on horticultural greenhouses and crops. `★ 65` `BSD-3-Clause-Clear`
- [greenpeer/GreenLightPlus](https://github.com/greenpeer/GreenLightPlus) - GreenLightPlus is a ToolKit for greenhouse environment simulation and energy consumption-yield analysis. It combines the original GreenLight model with the EnergyPlus simulation tool to investigate… `★ 30` `GPL-3.0`
- [EECi/GES](https://github.com/EECi/GES) - Greenhouse Energy Simulation. `★ 24` `MIT`
- [GaiaKnowledge/VerticalFarming](https://github.com/GaiaKnowledge/VerticalFarming) - Vertical Farming Wizard is an open-source project that centralises vertical farming (VF) and controlled environment agriculture (CEA) solutions. The objective of this decision support system is to… `★ 24` `MIT`
- [jdsjxin/CSGtom](https://github.com/jdsjxin/CSGtom) - A Chineses solar greenhouse climate model combined with tomato yield model. `★ 8` `GPL-3.0`
- [kensaku-okada/Greenhouse-with-OPV-film-Model](https://github.com/kensaku-okada/Greenhouse-with-OPV-film-Model) - The lettuce produce and electricity generation model for "Crop Production and Energy Generation in a Greenhouse Integrated with Semi-transparent Organic Photovoltaics (OPV) film". `★ 6` `MIT`
- [linucks/fu_evapotranspiration](https://github.com/linucks/fu_evapotranspiration) - A python implementation of the model from: Plant factories; crop transpiration and energy balance by Gaamans et al. `★ 4` `no licence`
- [rebekahewaller/be-423-523-project](https://github.com/rebekahewaller/be-423-523-project) - OPV greenhouse solar radiation, shading, and plant growth model. `★ 3` `no licence`
- [shennongwm/ShennongWM-G](https://github.com/shennongwm/ShennongWM-G) - Open-source greenhouse world model for action-conditioned climate-crop simulation and counterfactual audit. `★ 3` `custom licence`
- [aaronli7/CEA-Simulator](https://github.com/aaronli7/CEA-Simulator) - No description provided. `★ 2` `no licence` `archived`
- [breuderink/green-fingers](https://github.com/breuderink/green-fingers) - Simulate crop model for autonomous greenhouse simulation. `★ 2` `no licence`
- [luminousphotonics/horticulture-lighting-simulator](https://github.com/luminousphotonics/horticulture-lighting-simulator) - Radiance-based horticultural lighting simulation and 3D visualization engine. `★ 2` `BSD-3-Clause-Clear`
- [cc0ffee/greensim](https://github.com/cc0ffee/greensim) - internal greenhouse climate modeling. `★ 1` `no licence`
- [ThomasXIONG151215/vertical-farm-energy-designer](https://github.com/ThomasXIONG151215/vertical-farm-energy-designer) - Vertical farm energy simulation and design tool (formerly called OpenCROPS). `★ 1` `MIT`
- [VaGlar/Greenhouse-Digital-Twin](https://github.com/VaGlar/Greenhouse-Digital-Twin) - Parameterizable digital twin for a CHP-powered hydroponic tomato greenhouse — MVP simulating climate (temperature, CO2) and yield, built to be recalibrated with real sensor data once the greenhouse… `★ 1` `no licence`
- [AbbyHodson/cea-energy-water-model](https://github.com/AbbyHodson/cea-energy-water-model) - Repository for the paper "A Simplified Approach to Energy-Water Modeling for Controlled Environment Agriculture". `no licence`
- [AJBoth/CEAOS](https://github.com/AJBoth/CEAOS) - CEA Open Simulator. `MIT`
- [alamkashani/WASA-VERDE-API](https://github.com/alamkashani/WASA-VERDE-API) - No description provided. `no licence`
- [assamite/greenhouse](https://github.com/assamite/greenhouse) - Greenhouse light control system simulations. `no licence`
- [BlueTerraenergyexperts/mto_dashboard-local](https://github.com/BlueTerraenergyexperts/mto_dashboard-local) - No description provided. `no licence`
- [colbyamiee31-boop/vpd-heat-tradeoff-greenhouse-radc](https://github.com/colbyamiee31-boop/vpd-heat-tradeoff-greenhouse-radc) - Clean release package for RADC greenhouse VPD-heat diagnostic simulation. `custom licence`
- [daanheeling/PlantBalanceModel](https://github.com/daanheeling/PlantBalanceModel) - The Plant Balance Model used in the paper: "Sinks not sources: how vertical farming's potential is limited by crop breeding". `no licence`
- [donaldscoon/Energy_Cascade_Models](https://github.com/donaldscoon/Energy_Cascade_Models) - Implementations of the Energy Cascade crop systems models for prediction of biomass, photosynthesis, oxygen production and transpiration based on variable environmental conditions. `MIT`
- [FateDawnLeon/Greenhouse-Growing-Challenge](https://github.com/FateDawnLeon/Greenhouse-Growing-Challenge) - For the machine learning challenge, teams will get access to a simple greenhouse climate and lettuce production model (simple simulator) during the preparation phase. Teams will have to develop… `no licence`
- [joaquinperaza/AGRON893-Aeroponics](https://github.com/joaquinperaza/AGRON893-Aeroponics) - No description provided. `no licence`
- [lirei-lab/greenflux](https://github.com/lirei-lab/greenflux) - Modular greenhouse climate, crop and energy simulator with traceable physics, measured-data calibration, and declarative studies for MPC, planning under uncertainty and anomaly detection. `MIT`
- [mehran-hmdpr/GHEpy](https://github.com/mehran-hmdpr/GHEpy) - GHEpy is a python tool for evaluation of heating demand in greenhouses when data are not provided elsewhere. `MIT`
- [miem215/greenhouse_mimo_mpc](https://github.com/miem215/greenhouse_mimo_mpc) - Augmented State MPC for Greenhouse Climate Control. `no licence`
- [PGTBoos/Greenhouse-Climate-simulation](https://github.com/PGTBoos/Greenhouse-Climate-simulation) - A simulation environment for greenhouse climate power engineering. Not to grow crops directly but rather to simulate crops and simulate energy demands. it keeps track though of the biomass… `no licence`
- [prashanthjarapla17/nutrient-dosing-app](https://github.com/prashanthjarapla17/nutrient-dosing-app) - Mobile-friendly Streamlit application for soilless crop nutrient dosing, fertilizer balancing and stage-wise irrigation scheduling using location-based weather and evapotranspiration data, with… `no licence`
- [rajeswari090/Agritwin-GH](https://github.com/rajeswari090/Agritwin-GH) - No description provided. `custom licence`
- [rajithadesilva/autotom_climate_engine](https://github.com/rajithadesilva/autotom_climate_engine) - AutoTom Climate Engine is a climate simulation engine for modelling glasshouse weather and crop-growing environments. It is designed to support greenhouse climate analysis, scenario testing, and… `Apache-2.0`
- [ShuyiPeng/portable_vf_study](https://github.com/ShuyiPeng/portable_vf_study) - No description provided. `AGPL-3.0`
- [srivastavaraj37/avinya-twin](https://github.com/srivastavaraj37/avinya-twin) - Physics-based digital twin of a plastic polyhouse (tomato, Guwahati, Assam) for humidity/disease-pressure controller research. `no licence`
- [Sver0411/AgriTwin-CPS](https://github.com/Sver0411/AgriTwin-CPS) - Simulation-Based Greenhouse Digital Twin and Cyber-Physical Systems Research Platform. Reproducible Python simulations for state estimation, closed-loop control, and fault resilience. `MIT`
- [sxwd4ever/GSim](https://github.com/sxwd4ever/GSim) - Greenhouse micro climate simulation codes using E+ and openstudio. `no licence`
- [ucb-msol/AgroPV](https://github.com/ucb-msol/AgroPV) - Standalone source code for simulation and optimization of Agrophotovoltaic greenhouse systems. Authored by Roger Isied, Emre Mengi, and Tarek Zohdi. `MIT`
- [westlab/GreenLight-ADV](https://github.com/westlab/GreenLight-ADV) - No description provided. `BSD-3-Clause-Clear`
- [YPing-A/Greenhouse-Discrete_MPC](https://github.com/YPing-A/Greenhouse-Discrete_MPC) - No description provided. `MIT`

<a id="controlled-environment-r"></a>

#### R

- [mahima72539-sketch/AstroCROP-AI](https://github.com/mahima72539-sketch/AstroCROP-AI) - Autonomous Bio-Simulation Model for Space Agriculture based on NASA ECLSS framework. Built by Mahima Devi (M.Sc. Agronomy & Data Analytics) to simulate Crop Biomass, Capillary Fluid Flow Coefficient… `MIT`

<a id="controlled-environment-shell"></a>

#### Shell

- [Citte00/Biophysical-model-of-plant-growth](https://github.com/Citte00/Biophysical-model-of-plant-growth) - Project for the NAPDE course at PoliMi in collaboration with Agricola Moderna. `no licence`

<a id="controlled-environment-typescript"></a>

#### TypeScript

- [ThomasXIONG151215/indoor-farming-science](https://github.com/ThomasXIONG151215/indoor-farming-science) - Open-source TypeScript library for scientifically-validated indoor farming simulation models. `★ 1` `MIT`
- [MeadowMakerAi/greenhouse-cannabis-model](https://github.com/MeadowMakerAi/greenhouse-cannabis-model) - Open-source decision-support model for cannabis greenhouse design. React 19 + R3F + Tailwind. Screening-level — validate against stamped engineering before capex. `custom licence`

<a id="controlled-environment-other"></a>

#### Other

- [alwinhopf/GreenhouseCFDOpenFOAM](https://github.com/alwinhopf/GreenhouseCFDOpenFOAM) - Simulation of airflow within horticulture high-tunnel greenhouses using open-source CFD software. `no licence`
- [Dan-Brooks/MATLAB-GreenHouse](https://github.com/Dan-Brooks/MATLAB-GreenHouse) - A MATLAB simulation of a greenhouse. `no licence`
- [inanici/Kybele-GH](https://github.com/inanici/Kybele-GH) - Kybele Greenhouse Simulations: provide the capabilities of the Radiance software, custom-tailored for greenhouse modeling and metrics. `custom licence`
- [TanmoyAcharya/Smart-Greenhouse-Simulink](https://github.com/TanmoyAcharya/Smart-Greenhouse-Simulink) - No description provided. `no licence`
- [TM-Abir-Ahsan/Greenhouse-Crop-ET-Models](https://github.com/TM-Abir-Ahsan/Greenhouse-Crop-ET-Models) - No description provided. `MIT`
- [Weiyifan/agri-pv-simulator](https://github.com/Weiyifan/agri-pv-simulator) - Agri-PV Greenhouse Digital Twin. `no licence`
