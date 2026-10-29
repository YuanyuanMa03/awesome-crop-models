# Applications and case studies

Repositories that apply a crop, soil or environmental model to a particular study, region or analysis: simulation setups, scenario runs and analysis code. Models themselves are listed in the [main tree](../README.md).

**769 repositories**, arranged by crop or process, then programming language. Back to [Awesome Crop Models](../README.md).

## Contents

- [Crops](#crops) (380)
  - [General and multi-crop](#general-crop) (214)
    - [AGS Script](#general-crop-ags-script) (2)
    - [AMPL](#general-crop-ampl) (1)
    - [Batchfile](#general-crop-batchfile) (1)
    - [Fortran](#general-crop-fortran) (3)
    - [Java](#general-crop-java) (3)
    - [JavaScript](#general-crop-javascript) (3)
    - [Julia](#general-crop-julia) (1)
    - [MATLAB](#general-crop-matlab) (1)
    - [Python](#general-crop-python) (140)
    - [R](#general-crop-r) (44)
    - [Shell](#general-crop-shell) (2)
    - [Other](#general-crop-other) (13)
  - [Rice](#rice) (13)
    - [GAML](#rice-gaml) (1)
    - [Python](#rice-python) (8)
    - [R](#rice-r) (3)
    - [Other](#rice-other) (1)
  - [Wheat](#wheat) (18)
    - [Python](#wheat-python) (11)
    - [R](#wheat-r) (6)
    - [Other](#wheat-other) (1)
  - [Maize](#maize) (36)
    - [Python](#maize-python) (27)
    - [R](#maize-r) (7)
    - [Other](#maize-other) (2)
  - [Barley, sorghum, millet and other cereals](#other-cereals) (10)
    - [JavaScript](#other-cereals-javascript) (1)
    - [Python](#other-cereals-python) (3)
    - [R](#other-cereals-r) (6)
  - [Soybean](#soybean) (11)
    - [C++](#soybean-cplusplus) (1)
    - [Python](#soybean-python) (5)
    - [R](#soybean-r) (3)
    - [Other](#soybean-other) (2)
  - [Other legumes and oilseeds](#legumes-oilseeds) (5)
    - [JavaScript](#legumes-oilseeds-javascript) (1)
    - [Python](#legumes-oilseeds-python) (2)
    - [R](#legumes-oilseeds-r) (2)
  - [Potato](#potato) (10)
    - [AMPL](#potato-ampl) (1)
    - [Python](#potato-python) (4)
    - [R](#potato-r) (2)
    - [Other](#potato-other) (3)
  - [Cassava and other roots and tubers](#roots-tubers) (2)
    - [C#](#roots-tubers-csharp) (1)
    - [Python](#roots-tubers-python) (1)
  - [Cotton](#cotton) (6)
    - [Python](#cotton-python) (4)
    - [R](#cotton-r) (1)
    - [Other](#cotton-other) (1)
  - [Sugarcane and sugar beet](#sugar-crops) (3)
    - [Python](#sugar-crops-python) (1)
    - [R](#sugar-crops-r) (2)
  - [Vegetables](#vegetables) (6)
    - [Python](#vegetables-python) (3)
    - [R](#vegetables-r) (2)
    - [Other](#vegetables-other) (1)
  - [Fruit trees and grapevine](#fruit-vine) (15)
    - [JavaScript](#fruit-vine-javascript) (1)
    - [POV-Ray SDL](#fruit-vine-pov-ray-sdl) (1)
    - [Python](#fruit-vine-python) (5)
    - [R](#fruit-vine-r) (7)
    - [Other](#fruit-vine-other) (1)
  - [Oil palm, coffee, cocoa and other plantation crops](#plantation) (7)
    - [Python](#plantation-python) (3)
    - [R](#plantation-r) (2)
    - [Other](#plantation-other) (2)
  - [Grassland, pasture and forage](#grassland) (16)
    - [Python](#grassland-python) (3)
    - [R](#grassland-r) (10)
    - [Other](#grassland-other) (3)
  - [Bioenergy and other crops](#bioenergy-other) (8)
    - [C++](#bioenergy-other-cplusplus) (1)
    - [Fortran](#bioenergy-other-fortran) (1)
    - [Python](#bioenergy-other-python) (3)
    - [R](#bioenergy-other-r) (3)
- [Processes](#processes) (389)
  - [Phenology and development](#phenology) (26)
    - [Python](#phenology-python) (13)
    - [R](#phenology-r) (10)
    - [Other](#phenology-other) (3)
  - [Photosynthesis, canopy and transpiration](#photosynthesis) (5)
    - [Julia](#photosynthesis-julia) (2)
    - [Python](#photosynthesis-python) (1)
    - [R](#photosynthesis-r) (2)
  - [Plant architecture and FSPM](#architecture) (4)
    - [Python](#architecture-python) (2)
    - [R](#architecture-r) (2)
  - [Roots and rhizosphere](#roots) (5)
    - [C++](#roots-cplusplus) (1)
    - [R](#roots-r) (1)
    - [Shell](#roots-shell) (3)
  - [Soil water and heat](#soil-water) (28)
    - [C](#soil-water-c) (1)
    - [MATLAB](#soil-water-matlab) (1)
    - [Python](#soil-water-python) (19)
    - [R](#soil-water-r) (4)
    - [Other](#soil-water-other) (3)
  - [Soil carbon, nitrogen and nutrients](#soil-nutrients) (61)
    - [AGS Script](#soil-nutrients-ags-script) (1)
    - [C#](#soil-nutrients-csharp) (1)
    - [Eagle](#soil-nutrients-eagle) (1)
    - [JavaScript](#soil-nutrients-javascript) (1)
    - [MATLAB](#soil-nutrients-matlab) (1)
    - [NetLogo](#soil-nutrients-netlogo) (1)
    - [Python](#soil-nutrients-python) (25)
    - [R](#soil-nutrients-r) (26)
    - [Other](#soil-nutrients-other) (4)
  - [Agricultural greenhouse gases](#greenhouse-gases) (8)
    - [Python](#greenhouse-gases-python) (3)
    - [R](#greenhouse-gases-r) (5)
  - [Evapotranspiration and irrigation](#evapotranspiration) (106)
    - [JavaScript](#evapotranspiration-javascript) (4)
    - [MATLAB](#evapotranspiration-matlab) (2)
    - [Perl](#evapotranspiration-perl) (1)
    - [Python](#evapotranspiration-python) (75)
    - [R](#evapotranspiration-r) (14)
    - [Other](#evapotranspiration-other) (10)
  - [Weather and agroclimate](#weather) (6)
    - [Python](#weather-python) (2)
    - [R](#weather-r) (4)
  - [Pests, diseases and weeds](#pests-diseases) (1)
    - [R](#pests-diseases-r) (1)
  - [Hydrology, erosion and watersheds](#hydrology) (131)
    - [Batchfile](#hydrology-batchfile) (1)
    - [Forth](#hydrology-forth) (1)
    - [Fortran](#hydrology-fortran) (2)
    - [Java](#hydrology-java) (1)
    - [JavaScript](#hydrology-javascript) (12)
    - [MATLAB](#hydrology-matlab) (2)
    - [NetLogo](#hydrology-netlogo) (1)
    - [Python](#hydrology-python) (56)
    - [R](#hydrology-r) (28)
    - [Scala](#hydrology-scala) (1)
    - [Smarty](#hydrology-smarty) (1)
    - [Visual Basic](#hydrology-visual-basic) (1)
    - [Other](#hydrology-other) (24)
  - [Land surface and global vegetation](#land-surface) (2)
    - [Python](#land-surface-python) (1)
    - [R](#land-surface-r) (1)
  - [Greenhouses and controlled environments](#controlled-environment) (6)
    - [Python](#controlled-environment-python) (5)
    - [R](#controlled-environment-r) (1)

## Crops

<a id="general-crop"></a>

### General and multi-crop

<a id="general-crop-ags-script"></a>

#### AGS Script

- [zalf-rpm/switch](https://github.com/zalf-rpm/switch) - No description provided. `MPL-2.0`
- [zalf-rpm/yieldGEM](https://github.com/zalf-rpm/yieldGEM) - No description provided. `MPL-2.0`

<a id="general-crop-ampl"></a>

#### AMPL

- [fredi-agbohessou/stics_uzf_dtc_zw](https://github.com/fredi-agbohessou/stics_uzf_dtc_zw) - No description provided. `no licence`

<a id="general-crop-batchfile"></a>

#### Batchfile

- [WangdanUF/work](https://github.com/WangdanUF/work) - DSSAT input files for my data in 2015-2016. `★ 2` `no licence`

<a id="general-crop-fortran"></a>

#### Fortran

- [VEZY/STICS-IC-paper](https://github.com/VEZY/STICS-IC-paper) - No description provided. `★ 2` `custom licence`
- [cjchandler/AquaCropOptimise](https://github.com/cjchandler/AquaCropOptimise) - python programs to optimise planting dates using on AquaCrop growth simulations. `custom licence`
- [jboscariol/CROPGRO-4.5x4.8](https://github.com/jboscariol/CROPGRO-4.5x4.8) - Comparison between Cropgro 4.8 and 4.5. `no licence`

<a id="general-crop-java"></a>

#### Java

- [amitesh4u/weatherprediction](https://github.com/amitesh4u/weatherprediction) - Java application that runs DSSAT 4.0 crop simulations with weather data for districts. `no licence`
- [HarshiniUF/DSSAT-Chatbot](https://github.com/HarshiniUF/DSSAT-Chatbot) - No description provided. `no licence`
- [nocdoggo/Nitrogen-Tracking-and-Harvest-Simulation](https://github.com/nocdoggo/Nitrogen-Tracking-and-Harvest-Simulation) - This is a Nitrogen concentration tracking and simulation software which utilizes the world leading DSSAT decision making software. `MIT`

<a id="general-crop-javascript"></a>

#### JavaScript

- [MaxwellMkondiwa/Rice_Wheat_System_SDS_Tool](https://github.com/MaxwellMkondiwa/Rice_Wheat_System_SDS_Tool) - We showcase a rice-wheat system spatial decision support tool that allows researchers and decision makers to explore the implications of changing different components of the system inputs. The tool… `★ 1` `no licence`
- [efolimatthew/crop-modelling-portfolio](https://github.com/efolimatthew/crop-modelling-portfolio) - Independent postgraduate-level portfolio of crop modelling projects simulating multi-stress responses, disease risk, and yield interactions using R. `CC0-1.0`
- [hamedsabzchi/libya-length-of-growing-period](https://github.com/hamedsabzchi/libya-length-of-growing-period) - Google Earth Engine and Python workflows for Length of Growing Period (LGP) mapping and climate-soil water balance analysis in Libya. `no licence`

<a id="general-crop-julia"></a>

#### Julia

- [nicomignoni/tcst26-agrivoltaic](https://github.com/nicomignoni/tcst26-agrivoltaic) - Simulation code for the paper "Controlling pv panels tilt orientation for optimal crop shading and power generation in agrivoltaics". `★ 1` `Apache-2.0`

<a id="general-crop-matlab"></a>

#### MATLAB

- [mmp2192/GGCMI-GWLs](https://github.com/mmp2192/GGCMI-GWLs) - No description provided. `no licence`

<a id="general-crop-python"></a>

#### Python

- [jingwu6/LM_AG](https://github.com/jingwu6/LM_AG) - No description provided. `★ 18` `no licence`
- [irripro/Test_PCSE_Jupyter_Notbooks](https://github.com/irripro/Test_PCSE_Jupyter_Notbooks) - Comparison of crop simulation model under different natural, irrigation and fertilization conditions by PCSE/LINTUL. `★ 15` `GPL-3.0`
- [poomstas/AgTech_DRL](https://github.com/poomstas/AgTech_DRL) - Optimize plant growth conditions using deep reinforcement learning techniques (DDPG, TD3, SAC) and a crop simulator (PCSE-v0). `★ 7` `no licence`
- [Kizito16/SMARTFARMER](https://github.com/Kizito16/SMARTFARMER) - Agro-advisory service for western Kenya combining satellite imagery, weather and soil data with the WOFOST crop model. `★ 6` `no licence`
- [sulekahraman/wofost-study](https://github.com/sulekahraman/wofost-study) - No description provided. `★ 6` `no licence`
- [mcmancini/UkWofost](https://github.com/mcmancini/UkWofost) - Implementation of the WOFOST crop yield model to simulate crop yields in the UK. `★ 4` `no licence`
- [mariecombe/fluxnet-compare](https://github.com/mariecombe/fluxnet-compare) - This is a side project from the main PCSE-carbon cycle, where we compare FluxNet observations of the GPP, TER and NEE fluxes to simulated fluxes from PCSE and SiBCASA. `★ 3` `MIT`
- [xflorameng/wofost-bandits](https://github.com/xflorameng/wofost-bandits) - Integration of WOFOST simulation with bandit algorithms. `★ 3` `no licence`
- [ed2014/GEM_code](https://github.com/ed2014/GEM_code) - GxExM project. `★ 2` `no licence`
- [ehquinteroc/WOFOST-model](https://github.com/ehquinteroc/WOFOST-model) - No description provided. `★ 2` `MIT`
- [Kakoyi945/digital_twins_for_crop_growth](https://github.com/Kakoyi945/digital_twins_for_crop_growth) - It's a project that simulates a crop(exactly wheat and maize) in Shandong Qihe, which is also my undergraduate project. `★ 2` `no licence`
- [tmrob2/agriculture-RL](https://github.com/tmrob2/agriculture-RL) - A multi-objective reinforcement learning solution for multiagent agricultural setups. `★ 2` `no licence`
- [allfed/nw-crop-yield-change](https://github.com/allfed/nw-crop-yield-change) - Calculates percentage change in crop yields under different nuclear winter scenarios (soot levels), by country. `★ 1` `Apache-2.0`
- [BabakZolghadrAsli/Aquacrop_OSPy_extension](https://github.com/BabakZolghadrAsli/Aquacrop_OSPy_extension) - Work in progress. `★ 1` `MIT`
- [hernansanchez34/modelo-productividad-cultivos](https://github.com/hernansanchez34/modelo-productividad-cultivos) - No description provided. `★ 1` `no licence`
- [iiasa/ggcm-feature-importance](https://github.com/iiasa/ggcm-feature-importance) - Feature attribution pipeline for Global Gridded Crop Model (GGCM) simulations. `★ 1` `MIT`
- [isuforesite/Foresite](https://github.com/isuforesite/Foresite) - No description provided. `★ 1` `MIT`
- [JJguri/VarianceDecomposition](https://github.com/JJguri/VarianceDecomposition) - Decompose crop yield variance - Assess which factors (G*E*M) drive yield variability. `★ 1` `no licence`
- [McoVale/TSAgriPV](https://github.com/McoVale/TSAgriPV) - Data process from crop orientation and PVP geometry to electrical production and agricultural yield. `★ 1` `GPL-3.0`
- [milan8955/koshi-basin-crop-irrigation-aquacrop](https://github.com/milan8955/koshi-basin-crop-irrigation-aquacrop) - AquaCrop-OSPy simulations of rice, wheat and maize yield and soil-moisture-threshold irrigation in the Koshi River Basin, Nepal (MSc dissertation). `★ 1` `MIT`
- [mirzaaamir10/aquacrop-water-quality](https://github.com/mirzaaamir10/aquacrop-water-quality) - No description provided. `★ 1` `no licence`
- [NDE18/crop-portfolio-dss](https://github.com/NDE18/crop-portfolio-dss) - No description provided. `★ 1` `no licence`
- [RodrigoAgronomia/APSIMDL](https://github.com/RodrigoAgronomia/APSIMDL) - No description provided. `★ 1` `no licence`
- [WUR-AI/CropGym-ToMeasureOrNot](https://github.com/WUR-AI/CropGym-ToMeasureOrNot) - No description provided. `★ 1` `GPL-3.0`
- [WUR-AI/QuzhouAITrials](https://github.com/WUR-AI/QuzhouAITrials) - Repository things related to the crop management trials in Quzhou. `★ 1` `GPL-3.0`
- [wuyang060826/llama_ppo_rnd_in_gymDssat](https://github.com/wuyang060826/llama_ppo_rnd_in_gymDssat) - No description provided. `★ 1` `no licence`
- [xuqch/NEC_CropYield](https://github.com/xuqch/NEC_CropYield) - No description provided. `★ 1` `no licence`
- [Yangclock/WOFOST_AP](https://github.com/Yangclock/WOFOST_AP) - No description provided. `★ 1` `no licence` `archived`
- [zalf-rpm/agmip_waterlogging](https://github.com/zalf-rpm/agmip_waterlogging) - Simulation setup for the AgMIP waterlogging study (ZALF). `★ 1` `MPL-2.0`
- [zalf-rpm/CC_germany](https://github.com/zalf-rpm/CC_germany) - setup to run MONICA simulations throughout Germany under current and future climate conditions. `★ 1` `MPL-2.0`
- [abdoufaci/gym_dssat_project_4th_year](https://github.com/abdoufaci/gym_dssat_project_4th_year) - No description provided. `no licence`
- [agrimanager875-ux/agrimanager-code](https://github.com/agrimanager875-ux/agrimanager-code) - No description provided. `no licence`
- [agroimpacts/aquacrop_simulation](https://github.com/agroimpacts/aquacrop_simulation) - No description provided. `no licence`
- [AlbertAM-TIA/APSIM-AgroProcess-XAI](https://github.com/AlbertAM-TIA/APSIM-AgroProcess-XAI) - An integrated workflow linking APSIM outputs with timescale-aware variance decomposition, grouped-year predictive modelling and Shapley explanations. `no licence`
- [albertdaniell/wofost_kalro](https://github.com/albertdaniell/wofost_kalro) - No description provided. `MIT`
- [AneNJ/IO_cropFeedback](https://github.com/AneNJ/IO_cropFeedback) - No description provided. `no licence`
- [anujak7/mode-wofost-repo](https://github.com/anujak7/mode-wofost-repo) - wofost model. `no licence`
- [Assimila/Cheng_MSc_reading_2020](https://github.com/Assimila/Cheng_MSc_reading_2020) - No description provided. `no licence`
- [assoumemba/sys866_digital_twin](https://github.com/assoumemba/sys866_digital_twin) - No description provided. `no licence`
- [BerheAA/planting-date-option-v10](https://github.com/BerheAA/planting-date-option-v10) - planting time evaluation. `no licence`
- [BerheAA10/kansas-rotation-animated-map](https://github.com/BerheAA10/kansas-rotation-animated-map) - animated yield map of crop rotation in Kansas. `no licence`
- [cschulte7/AquaCrop-Calibrations](https://github.com/cschulte7/AquaCrop-Calibrations) - This is a repository being used by University of Arizona students and faculty. `no licence`
- [danilosarti/jules-crop-vivid](https://github.com/danilosarti/jules-crop-vivid) - No description provided. `no licence`
- [danyoungday/evoaquacrop](https://github.com/danyoungday/evoaquacrop) - No description provided. `no licence`
- [Djihad-derbal/DQN-gym-Dssat](https://github.com/Djihad-derbal/DQN-gym-Dssat) - No description provided. `no licence`
- [DrAhmedKheir/APSIMx_ML_AF_MENA_Germany](https://github.com/DrAhmedKheir/APSIMx_ML_AF_MENA_Germany) - No description provided. `no licence`
- [ecucuzzella/DynamicCropModelingandAPSIM](https://github.com/ecucuzzella/DynamicCropModelingandAPSIM) - No description provided. `no licence`
- [EvanDamron/Aquacrop-Simulations](https://github.com/EvanDamron/Aquacrop-Simulations) - No description provided. `no licence`
- [frank0434/No-modelling-without-experimentation](https://github.com/frank0434/No-modelling-without-experimentation) - No description provided. `no licence`
- [gavinedd/DelayRL-PCSE](https://github.com/gavinedd/DelayRL-PCSE) - No description provided. `GPL-3.0`
- [geonextgis/brandenburg-climate-scenarios](https://github.com/geonextgis/brandenburg-climate-scenarios) - No description provided. `no licence`
- [geonextgis/soil-amelioration-scenarios](https://github.com/geonextgis/soil-amelioration-scenarios) - No description provided. `no licence`
- [goharghazary/CropClim](https://github.com/goharghazary/CropClim) - No description provided. `no licence`
- [gru13/Final-Year-Project](https://github.com/gru13/Final-Year-Project) - No description provided. `no licence`
- [HamishBrownPFR/APSIMArbitrator](https://github.com/HamishBrownPFR/APSIMArbitrator) - Simulations and analysis for arbitrator testing paper. `no licence`
- [haoli19990511-lab/agripv-optimizer](https://github.com/haoli19990511-lab/agripv-optimizer) - Multi-objective optimisation of agrivoltaic designs (LER vs. annual net income) with NSGA-II, Radiance ray tracing and WOFOST - bachelor thesis, FH Aachen / Solar-Institut Jülich, 2026. `MIT`
- [Hazard-cn/CA_soil_moisture](https://github.com/Hazard-cn/CA_soil_moisture) - Reproducible analysis code for straw-return buffering of compound drought-heat yield losses in Chinese maize. `no licence`
- [HEAL-KGS/EGGS-Aquacrop](https://github.com/HEAL-KGS/EGGS-Aquacrop) - No description provided. `no licence`
- [herman-berghuijs/wofost_example_yue](https://github.com/herman-berghuijs/wofost_example_yue) - No description provided. `no licence`
- [hhajae/farmer](https://github.com/hhajae/farmer) - No description provided. `no licence`
- [homoludens/kenya_digital_twin_farm](https://github.com/homoludens/kenya_digital_twin_farm) - PyQt app, Digital Twin Farm for locations in Kenya. Using PCSE and WOFOST models. `no licence`
- [Human-Centered-Optimization-Lab/pi-cropopt](https://github.com/Human-Centered-Optimization-Lab/pi-cropopt) - No description provided. `no licence`
- [imec-idlab/sowing-dss-kenya](https://github.com/imec-idlab/sowing-dss-kenya) - Sowing Decision Support System for Smallholder Farmers in Kenya Integrated in a Simulation Environment. `MIT`
- [izuku-franck1555/crop-model-case-studies](https://github.com/izuku-franck1555/crop-model-case-studies) - No description provided. `no licence`
- [JaeminEun/AquaCrop-CropMaps](https://github.com/JaeminEun/AquaCrop-CropMaps) - AquaCrop with crop maps and crop calendars (Eun et al., 2025). `no licence`
- [Jason010815/DSSAT-LLM](https://github.com/Jason010815/DSSAT-LLM) - No description provided. `no licence`
- [Jayanth24/ComputationalAgriculture](https://github.com/Jayanth24/ComputationalAgriculture) - Local work for the Computational Agriculture Project. `no licence`
- [jcvl-udg/collab_notebooks](https://github.com/jcvl-udg/collab_notebooks) - No description provided. `no licence`
- [Jintpong/Dissertation-ppo](https://github.com/Jintpong/Dissertation-ppo) - No description provided. `no licence`
- [juliavilutis/zoneamento-agroclimatico-cmip6](https://github.com/juliavilutis/zoneamento-agroclimatico-cmip6) - No description provided. `MIT`
- [jvasco323/nfood-yield-plateau](https://github.com/jvasco323/nfood-yield-plateau) - No description provided. `no licence`
- [Lidaeus/TianShouDSSAT](https://github.com/Lidaeus/TianShouDSSAT) - No description provided. `no licence`
- [Linruili651/Wofost_Model_APV](https://github.com/Linruili651/Wofost_Model_APV) - No description provided. `no licence`
- [M-M-VS-Lab/BioCro_DSSAT_WOFOST_Egorov_etal_paper](https://github.com/M-M-VS-Lab/BioCro_DSSAT_WOFOST_Egorov_etal_paper) - No description provided. `no licence`
- [MayerT1/LLM_Dev_Crop](https://github.com/MayerT1/LLM_Dev_Crop) - No description provided. `no licence`
- [mirpulatov/monica_modeling](https://github.com/mirpulatov/monica_modeling) - MyDiploma. `no licence`
- [nick-transition/PCSE](https://github.com/nick-transition/PCSE) - Notebooks assessing the suitability of PCSE for crop simulation studies. `no licence`
- [nina-grant/indian-agriculture-paper](https://github.com/nina-grant/indian-agriculture-paper) - Code from Grant et al. (2024) - Impacts on Indian Agriculture Due to Stratospheric Aerosol Intervention Using Agroclimatic Indices submitted to Earth's Future. `no licence`
- [Obsidjan/agririsktestcode](https://github.com/Obsidjan/agririsktestcode) - No description provided. `no licence`
- [olive-jy-song/rl_agriculture](https://github.com/olive-jy-song/rl_agriculture) - No description provided. `no licence`
- [os-climate/physrisk-crop](https://github.com/os-climate/physrisk-crop) - Crop vulnerability modelling. `Apache-2.0`
- [pamudu123/RL-Farming](https://github.com/pamudu123/RL-Farming) - No description provided. `no licence`
- [patatasal/WUR_INF_CropModel](https://github.com/patatasal/WUR_INF_CropModel) - This repository contains the related work of my master research practice project, which was done at the Information Technology group in Wageningen University & Research, 2023-2024. `no licence`
- [pitcheverlasting/africa-forcing-scenarios](https://github.com/pitcheverlasting/africa-forcing-scenarios) - A project to evaluate the climate change on crop yield in Africa (2014). `no licence`
- [PradeepKadubandi/Agroecology-Agent](https://github.com/PradeepKadubandi/Agroecology-Agent) - A mirror of private repository of Agro Ecology project. `no licence`
- [PSUmodeling/Antares-IOWA](https://github.com/PSUmodeling/Antares-IOWA) - No description provided. `no licence`
- [PSUmodeling/Cycles-COBS](https://github.com/PSUmodeling/Cycles-COBS) - No description provided. `MIT`
- [PSUmodeling/Cycles-EFR-simulations](https://github.com/PSUmodeling/Cycles-EFR-simulations) - No description provided. `no licence`
- [PSUmodeling/Cycles-EOW-simulations](https://github.com/PSUmodeling/Cycles-EOW-simulations) - No description provided. `no licence`
- [PSUmodeling/Cycles-HOA-simulation-matrix](https://github.com/PSUmodeling/Cycles-HOA-simulation-matrix) - No description provided. `MIT`
- [PSUmodeling/Cycles-L-WE38-simulations](https://github.com/PSUmodeling/Cycles-L-WE38-simulations) - No description provided. `no licence`
- [PSUmodeling/Ethiopia-Cycles-simulation-matrix](https://github.com/PSUmodeling/Ethiopia-Cycles-simulation-matrix) - No description provided. `no licence`
- [Rachel0305/gym-dssat-pdi](https://github.com/Rachel0305/gym-dssat-pdi) - gym-dssat-pdi experiments. `no licence`
- [RajulUpadhyay/Climate-Variability-and-Change-Impact-on-Crop-Yield](https://github.com/RajulUpadhyay/Climate-Variability-and-Change-Impact-on-Crop-Yield) - No description provided. `no licence`
- [RonaldTao/AAMAS_code](https://github.com/RonaldTao/AAMAS_code) - No description provided. `no licence`
- [rsw1998/TPAI-SPA-Curve-for-WOFOST](https://github.com/rsw1998/TPAI-SPA-Curve-for-WOFOST) - No description provided. `no licence`
- [saqibutm/PK-PyAEZ](https://github.com/saqibutm/PK-PyAEZ) - No description provided. `MIT`
- [Shalika-WUR/Project-codes-ACS](https://github.com/Shalika-WUR/Project-codes-ACS) - No description provided. `no licence`
- [yarasarrouh/Crop-Model-Analysis](https://github.com/yarasarrouh/Crop-Model-Analysis) - These are the codes used for my Dissertation. `no licence`
- [Yuanli-lxt/apsim](https://github.com/Yuanli-lxt/apsim) - apsim. `no licence`
- [Yue729/WOFOST_yuepan_2026](https://github.com/Yue729/WOFOST_yuepan_2026) - No description provided. `no licence`
- [YuqiLiunx/AHG](https://github.com/YuqiLiunx/AHG) - AHG. `no licence`
- [zalf-rpm/AgMIP_BNI](https://github.com/zalf-rpm/AgMIP_BNI) - MONICA simulation setup for the AgMIP BNI exercise. `MPL-2.0`
- [zalf-rpm/AgMIP_Calibration](https://github.com/zalf-rpm/AgMIP_Calibration) - AgMIP Calibration study coordinated by Daniel Wallach and Sabine Seidel. `no licence`
- [zalf-rpm/AgMIP_LIS](https://github.com/zalf-rpm/AgMIP_LIS) - MONICA setup for the AgMIP modelling exercise on low-input systems. `MPL-2.0`
- [zalf-rpm/agora_natura](https://github.com/zalf-rpm/agora_natura) - Scripts and data to run MONICA over a large area (Agora Natura project). `MPL-2.0`
- [zalf-rpm/bgr_flow](https://github.com/zalf-rpm/bgr_flow) - Flow-based MONICA simulation workflow for a BGR project. `MPL-2.0`
- [zalf-rpm/C3S2_414_po_ebro](https://github.com/zalf-rpm/C3S2_414_po_ebro) - MONICA calibration and simulations for the Po and Ebro basins (C3S2_414 project). `MPL-2.0`
- [zalf-rpm/carbiocial-2017](https://github.com/zalf-rpm/carbiocial-2017) - MONICA crop rotation simulations for the CarBioCial project in Brazil. `no licence`
- [zalf-rpm/carbiocial-project](https://github.com/zalf-rpm/carbiocial-project) - MONICA setup and climate data conversion for the CarBioCial project in Brazil. `MPL-2.0`
- [zalf-rpm/cropMapsEU](https://github.com/zalf-rpm/cropMapsEU) - Gridded MONICA inputs and output maps for European crops. `MPL-2.0`
- [zalf-rpm/CZ_site_calibration](https://github.com/zalf-rpm/CZ_site_calibration) - Data and scripts to calibrate MONICA crop parameters against experiments in the Czech Republic. `MPL-2.0`
- [zalf-rpm/czech-globe](https://github.com/zalf-rpm/czech-globe) - MONICA simulations for CzechGlobe. `no licence`
- [zalf-rpm/divCROP](https://github.com/zalf-rpm/divCROP) - MONICA crop rotation simulations for the divCROP project. `MPL-2.0`
- [zalf-rpm/Ehsan_data_aggregation_paper](https://github.com/zalf-rpm/Ehsan_data_aggregation_paper) - MONICA simulations for a study on input data aggregation. `MPL-2.0`
- [zalf-rpm/ethiopia-cc-impact](https://github.com/zalf-rpm/ethiopia-cc-impact) - MONICA simulations of climate change impacts in Ethiopia. `MPL-2.0`
- [zalf-rpm/irrigation_multiexp](https://github.com/zalf-rpm/irrigation_multiexp) - Calibration of MONICA against irrigation experiments with several crops. `MPL-2.0`
- [zalf-rpm/klima_konform](https://github.com/zalf-rpm/klima_konform) - MONICA simulations for the KlimaKonform project. `MPL-2.0`
- [zalf-rpm/klimertrag](https://github.com/zalf-rpm/klimertrag) - MONICA yield simulations for the KlimErtrag project. `MPL-2.0`
- [zalf-rpm/klimertrag_2](https://github.com/zalf-rpm/klimertrag_2) - Second MONICA simulation setup for the KlimErtrag project. `MPL-2.0`
- [zalf-rpm/macsur-cc-scaling-nrw](https://github.com/zalf-rpm/macsur-cc-scaling-nrw) - MACSUR climate-change scaling simulations for North Rhine-Westphalia with MONICA. `no licence`
- [zalf-rpm/macsur-cc-scaling-tuscany](https://github.com/zalf-rpm/macsur-cc-scaling-tuscany) - MACSUR climate-change scaling simulations for Tuscany with MONICA. `no licence`
- [zalf-rpm/macsur-croprotations-cz](https://github.com/zalf-rpm/macsur-croprotations-cz) - MACSUR crop rotation simulations for the Czech Republic. `no licence`
- [zalf-rpm/macsur-eu-heat-stress-assessment](https://github.com/zalf-rpm/macsur-eu-heat-stress-assessment) - MONICA assessment of heat stress on European crops (MACSUR). `no licence`
- [zalf-rpm/MACSUR_BCD](https://github.com/zalf-rpm/MACSUR_BCD) - Simulations part of the MACSUR BCD study organized by Fulu Tao. `MPL-2.0`
- [zalf-rpm/mettools_xii_paper_monica_simulations](https://github.com/zalf-rpm/mettools_xii_paper_monica_simulations) - MONICA simulations for a MetTools XII paper. `MPL-2.0`
- [zalf-rpm/modoklim](https://github.com/zalf-rpm/modoklim) - MONICA simulations for the MODOKLIM project. `MPL-2.0`
- [zalf-rpm/MODOKLIM_WL](https://github.com/zalf-rpm/MODOKLIM_WL) - MONICA simulations for the MODOKLIM project (WL setup). `no licence`
- [zalf-rpm/monica-agritwin](https://github.com/zalf-rpm/monica-agritwin) - MONICA simulation setups for the EOAgriTwin project. `MPL-2.0`
- [zalf-rpm/monica-cz](https://github.com/zalf-rpm/monica-cz) - MONICA simulations for the Czech Republic. `MPL-2.0`
- [zalf-rpm/monica-germany](https://github.com/zalf-rpm/monica-germany) - MONICA simulations across Germany. `MPL-2.0`
- [zalf-rpm/monica-germany-q4b](https://github.com/zalf-rpm/monica-germany-q4b) - Scripts and data to run MONICA across Germany (Q4B setup). `MPL-2.0`
- [zalf-rpm/monica_africa](https://github.com/zalf-rpm/monica_africa) - MONICA simulations for Africa. `MPL-2.0`
- [zalf-rpm/monica_italy_alessandro_setup](https://github.com/zalf-rpm/monica_italy_alessandro_setup) - MONICA simulation setup for Italy. `MPL-2.0`
- [zalf-rpm/monica_nigeria](https://github.com/zalf-rpm/monica_nigeria) - MONICA simulations for Nigeria. `MPL-2.0` `archived`
- [zalf-rpm/muencheberg_v140](https://github.com/zalf-rpm/muencheberg_v140) - MONICA simulation inputs for the Müncheberg V140 long-term experiment. `MPL-2.0`
- [zalf-rpm/SUSTAg-NRW](https://github.com/zalf-rpm/SUSTAg-NRW) - No description provided. `no licence`
- [zalf-rpm/SUSTAg-NRW-spinup](https://github.com/zalf-rpm/SUSTAg-NRW-spinup) - No description provided. `no licence`
- [zalf-rpm/voce-project](https://github.com/zalf-rpm/voce-project) - No description provided. `no licence`
- [zalf-rpm/yieldstat_east_germany](https://github.com/zalf-rpm/yieldstat_east_germany) - python producer/consumer for running over east germany. `MPL-2.0`

<a id="general-crop-r"></a>

#### R

- [CIAT-DAPA/dapa-climate-change](https://github.com/CIAT-DAPA/dapa-climate-change) - Automatically exported from code.google.com/p/dapa-climate-change. `★ 15` `no licence`
- [AramburuMerlos/gGYGA](https://github.com/AramburuMerlos/gGYGA) - Gridded yield potential estimates for the Global Yield Gap Atlas (GYGA). `★ 5` `GPL-3.0`
- [xavierign/MORDMAgro](https://github.com/xavierign/MORDMAgro) - Scripts associated to the paper to be published. `★ 4` `no licence`
- [germanmandrini/apsim_illinois](https://github.com/germanmandrini/apsim_illinois) - Codes to run multiple APSIM simulations on Illinois-US. `★ 3` `no licence`
- [jdeines/Deines_etal_LEMA_SALUS](https://github.com/jdeines/Deines_etal_LEMA_SALUS) - code, crop simulation files, and data for manuscript. `★ 3` `MIT`
- [TianyiQiu13/Cover-crop-multiservices](https://github.com/TianyiQiu13/Cover-crop-multiservices) - No description provided. `★ 3` `GPL-3.0`
- [CatherineGilbert/SCE](https://github.com/CatherineGilbert/SCE) - Seasonal Characterization Engine. Describes a crop's environment in terms of conditions encountered during each stage of the crop's development. Returns seasonal profiles, including seasonal… `★ 2` `custom licence`
- [frank0434/MasterThesis](https://github.com/frank0434/MasterThesis) - Book is published https://frank0434.github.io/MasterThesis/. `★ 2` `no licence`
- [ILVO-PEILIMPACT/model_users](https://github.com/ILVO-PEILIMPACT/model_users) - Use SWAP-WOFOST together with data layers covering Flanders entirely to launch a simulation for your specific location / case. `★ 2` `custom licence`
- [ILVO-PEILIMPACT/model_users_growing_season](https://github.com/ILVO-PEILIMPACT/model_users_growing_season) - Use SWAP-WOFOST together with data layers covering Flanders entirely to launch a simulation for your specific location / case. Specify the planting and harvest dates. `★ 2` `custom licence`
- [BiologicalRecordsCentre/future_rotations_explorer](https://github.com/BiologicalRecordsCentre/future_rotations_explorer) - A shiny app to enable farmers to visualise predicted impacts of future climate and weather on crop yields across Europe under different crop rotations. `★ 1` `MIT`
- [Dorcas-Sang/Multi_objective_achievement](https://github.com/Dorcas-Sang/Multi_objective_achievement) - No description provided. `★ 1` `no licence`
- [GuilleMarc/PhD_Codes](https://github.com/GuilleMarc/PhD_Codes) - Several scripts/snippets I wrote during my PhD in the agron department at Iowa state (statistical and process-based modeling of winter rye). `★ 1` `no licence`
- [hacamargoa/Global_Evaluation](https://github.com/hacamargoa/Global_Evaluation) - Evaluation of the LPJ GUESS crops output. `★ 1` `no licence`
- [Illustratien/Wang_2023_TAAG](https://github.com/Illustratien/Wang_2023_TAAG) - Reproducible scientific pipeline for stability analysis. `★ 1` `no licence`
- [laila1986/Agro590_project](https://github.com/laila1986/Agro590_project) - APSIM simulations of corn and soybean systems in Iowa behind an interactive extension tool. `★ 1` `GPL-3.0`
- [saraheikonen/crop-diversity](https://github.com/saraheikonen/crop-diversity) - Code from the journal article 'Diverging impacts of climate change on the global potential diversity of food crops'. '. `★ 1` `no licence`
- [shreevatsakodur/SCOMA](https://github.com/shreevatsakodur/SCOMA) - SCOMA APSIM Project. `★ 1` `no licence`
- [byzheng/apsimng-crops](https://github.com/byzheng/apsimng-crops) - No description provided. `custom licence`
- [cafltar/CafModelingFlexCropping_R](https://github.com/cafltar/CafModelingFlexCropping_R) - Scripts to process collated data - see scripts folder in CafModelingFlexCropping_CropSyst for collating scripts. `CC0-1.0`
- [CGIAR-AgWise/agwise-cropping-innovation](https://github.com/CGIAR-AgWise/agwise-cropping-innovation) - Cropping innovation research modules. `MIT`
- [Chinwa1/Yield_Gaps_analysis](https://github.com/Chinwa1/Yield_Gaps_analysis) - No description provided. `no licence`
- [chporter/CGRA_Rscripts](https://github.com/chporter/CGRA_Rscripts) - some plotting scripts for the CGRA +1.5 project. `BSD-3-Clause`
- [ed2014/DeepSouthOLW](https://github.com/ed2014/DeepSouthOLW) - Analysis of Deep South and Our Land and Water Crop datset. `no licence`
- [eggenm/crop_model_analysis](https://github.com/eggenm/crop_model_analysis) - These are R files for the analysis and visualization of aquacrop Senegal crop model. `no licence`
- [FarmerAssist/Simulation](https://github.com/FarmerAssist/Simulation) - No description provided. `no licence`
- [hacamargoa/Harvest_index](https://github.com/hacamargoa/Harvest_index) - Exraction of harvest index data and covariables to analyse HI. `no licence`
- [hugowinkfield/APSIM-Soil-ES](https://github.com/hugowinkfield/APSIM-Soil-ES) - No description provided. `no licence`
- [ILVO-PEILIMPACT/regional_model](https://github.com/ILVO-PEILIMPACT/regional_model) - SWAP-WOFOST at regional level. `custom licence`
- [jninanya/Ramirez-et-al-2024](https://github.com/jninanya/Ramirez-et-al-2024) - R markdown for the crop modeling simulation exercise performed by Ramirez et al. (2024). `no licence`
- [KeLiu7/Waterlogging-Crop-rotations](https://github.com/KeLiu7/Waterlogging-Crop-rotations) - No description provided. `no licence`
- [keyvan-malek/Yield-Variability](https://github.com/keyvan-malek/Yield-Variability) - No description provided. `no licence`
- [Kpadonoue/Written-Assessment-Kpadonou](https://github.com/Kpadonoue/Written-Assessment-Kpadonou) - No description provided. `no licence`
- [leilamuhoma27-cloud/Crop-Modelling-and-Climate-production-risk-analysis](https://github.com/leilamuhoma27-cloud/Crop-Modelling-and-Climate-production-risk-analysis) - No description provided. `no licence`
- [MollicMeyer/APSIM-DSM-AEL](https://github.com/MollicMeyer/APSIM-DSM-AEL) - No description provided. `custom licence`
- [Muhammad1599/DSSAT_Durnast](https://github.com/Muhammad1599/DSSAT_Durnast) - No description provided. `no licence`
- [paliAli/Modeling_yield](https://github.com/paliAli/Modeling_yield) - Biogeochemical modelling course group project. `no licence`
- [pches/Femeena_etal_How_can_crop_production_adapt](https://github.com/pches/Femeena_etal_How_can_crop_production_adapt) - This collection is designed to ensure the transparency and verifiability of the research presented in: "Supporting Information - How can crop production adapt to growing groundwater restrictions in… `MIT`
- [PedroDrim/Analise-fenotipica-DSSAT](https://github.com/PedroDrim/Analise-fenotipica-DSSAT) - Repositório para o projeto de estágio, de mesmo nome, realizado na Embrapa Arroz e Feijão Sob a orientação do Dr. Alexandre Bryan Heinemann. `no licence`
- [sbuis/AgMIP_calibration_PhaseIV_step2_synthetic_experiment](https://github.com/sbuis/AgMIP_calibration_PhaseIV_step2_synthetic_experiment) - Application of AgMIP Calibration Phase IV protocol with the STICS soil-crop model on synthetic data. `AGPL-3.0`
- [scmcclelland/daycent-global-analysis-SSP370](https://github.com/scmcclelland/daycent-global-analysis-SSP370) - No description provided. `no licence`
- [vbs0303/Precision-Ag-Pipeline](https://github.com/vbs0303/Precision-Ag-Pipeline) - Code pipelines for processing and analyzing DSSAT crop model outputs using linear/mixed models, GLMMs, and visualization tools. Includes workflows for leaf area index, nitrogen uptake, biomass, and… `MIT`
- [yeanukkim/watertable_crop_risk_assessment](https://github.com/yeanukkim/watertable_crop_risk_assessment) - R-script to analyze the effect of watertable on soil water balance and crop growth using the default and improved SIMPLACE &lt;LINTUL5, SLIM&gt; process-based crop model. `no licence`
- [zalf-rpm/Europ_Crop_Rot](https://github.com/zalf-rpm/Europ_Crop_Rot) - R scripts and study design for a European crop rotation model ensemble study. `no licence`

<a id="general-crop-shell"></a>

#### Shell

- [cafltar/CafModelingFlexCropping_CropSyst](https://github.com/cafltar/CafModelingFlexCropping_CropSyst) - No description provided. `CC0-1.0`
- [mihaelacaian/Crop_Scenarios_Modelling-](https://github.com/mihaelacaian/Crop_Scenarios_Modelling-) - This repository includes code to perform and analyse coupled climate-agromanagement scenarios for a given region. This can be used for other regions with small modifications indicated in… `no licence`

<a id="general-crop-other"></a>

#### Other

- [dpasquel/spatial_calibration_data](https://github.com/dpasquel/spatial_calibration_data) - No description provided. `★ 1` `no licence`
- [ikisekka/Irrigation](https://github.com/ikisekka/Irrigation) - Modeling Deficit Irrigation with DSSAT. `★ 1` `no licence`
- [nick-gauthier/neolithic-crop-model](https://github.com/nick-gauthier/neolithic-crop-model) - Application of computational crop models to understanding the spread of farming. `★ 1` `no licence`
- [Xin-Chenyu/Crop-model_Kenya](https://github.com/Xin-Chenyu/Crop-model_Kenya) - Generate historical localized crop yield data in sub-Saharan Africa with AquaCrop -OSPy. `★ 1` `no licence`
- [AlbertAM-TIA/Statistical_Analysis-Chapter5](https://github.com/AlbertAM-TIA/Statistical_Analysis-Chapter5) - Statistical analyses for large data sets from crop modelling studies. `no licence`
- [ambashalishe/AquaCrop-model-simulation](https://github.com/ambashalishe/AquaCrop-model-simulation) - AquaCrop model simulations and analysis scripts used to estimate irrigation water demand for agricultural water management studies. `no licence`
- [Chloe0317/SoilCRC](https://github.com/Chloe0317/SoilCRC) - No description provided. `no licence`
- [d-leclere/ISIMIP3b_CropModels_Shifters_LongTerm](https://github.com/d-leclere/ISIMIP3b_CropModels_Shifters_LongTerm) - Processing of crop model outputs from ISIMIP3b protocol (long-term impacts of climate change based on CMIP6) into spatially explicit long-term (i.e., 30y moving average every 10 years) shock to crop… `no licence`
- [GregMcLean-UQ/Tillering](https://github.com/GregMcLean-UQ/Tillering) - No description provided. `no licence`
- [LaydenDenning/locust-farm-sim](https://github.com/LaydenDenning/locust-farm-sim) - No description provided. `no licence`
- [Muhammad-Hasan-DU/Chapter2](https://github.com/Muhammad-Hasan-DU/Chapter2) - Preliminary Analysis and Non-linear Yield Modelling. `no licence`
- [sno036/APSIMXWorking](https://github.com/sno036/APSIMXWorking) - No description provided. `no licence`
- [zalf-rpm/monica-EAR-saxony](https://github.com/zalf-rpm/monica-EAR-saxony) - MONICA simulations for Saxony, Germany. `MPL-2.0`

<a id="rice"></a>

### Rice

<a id="rice-gaml"></a>

#### GAML

- [Star-farm/gama-oryza](https://github.com/Star-farm/gama-oryza) - No description provided. `★ 1` `no licence`

<a id="rice-python"></a>

#### Python

- [maso0310/DSSAT_Test](https://github.com/maso0310/DSSAT_Test) - No description provided. `★ 1` `no licence`
- [arjunhegde19-max/Meta_Rice](https://github.com/arjunhegde19-max/Meta_Rice) - Meta analysis of climate change impact of rice based on crop simulation studies. `no licence`
- [gaurpushkar/crop-modelling-Odisha](https://github.com/gaurpushkar/crop-modelling-Odisha) - Climate data processing and yield analysis for APSIM rice simulations (transplanted and direct-seeded) in Odisha, India. `no licence`
- [johanericka/phenology-fuzzy](https://github.com/johanericka/phenology-fuzzy) - phenology aware fuzzy logic for paddy irrigation. `no licence`
- [mcdavyz/bende-agroclimatic-risk-analysis](https://github.com/mcdavyz/bende-agroclimatic-risk-analysis) - Python workflow for agroclimatic risk assessment of rainfed rice production in Bende LGA, Nigeria (1981–2025). `no licence`
- [Shakawat098/Aronghata](https://github.com/Shakawat098/Aronghata) - Agro-hydrological modelling and carbon footprint of Boro rice under alternate wetting and drying versus continuous flooding (Khulna, Bangladesh). `no licence`
- [shentianlin/Claude](https://github.com/shentianlin/Claude) - Controlled-release blended fertiliser formula maps for 50 rice regions and 73 rice seasons in China, with model code. `no licence`
- [xuxuan1103/Rice_Yield_CMIP5_CMIP6](https://github.com/xuxuan1103/Rice_Yield_CMIP5_CMIP6) - Processed datasets and Python scripts supporting the analysis of rice yield changes under CMIP5 and CMIP6 climate scenarios in China. `no licence`

<a id="rice-r"></a>

#### R

- [jrodriguez88/CROP_MODELING_CIAT_NICARAGUA](https://github.com/jrodriguez88/CROP_MODELING_CIAT_NICARAGUA) - UPLAND RICE CROP MODELING CIAT-Nicaragua. `no licence`
- [jrodriguez88/rice_guyana](https://github.com/jrodriguez88/rice_guyana) - Scripts to rice simulation in Guyana using aquacrop. `no licence`
- [Narayan1985/Rice_model](https://github.com/Narayan1985/Rice_model) - Test for rice agroclimatic model and smart agriculture in rice and maize. `no licence`

<a id="rice-other"></a>

#### Other

- [NabilaRahmanMedha/Deep-Reinforcement-Learning-Based-Optimization-of-Rice-Irrigation-in-Bangladesh-Using-AquaCrop-Ospy](https://github.com/NabilaRahmanMedha/Deep-Reinforcement-Learning-Based-Optimization-of-Rice-Irrigation-in-Bangladesh-Using-AquaCrop-Ospy) - Deep Reinforcement Learning-based smart irrigation optimization for Bangladesh paddy cultivation using AquaCrop-OSPy. `no licence`

<a id="wheat"></a>

### Wheat

<a id="wheat-python"></a>

#### Python

- [EOA-team/winter_wheat_phenology](https://github.com/EOA-team/winter_wheat_phenology) - Simulation of winter wheat heading dates in Switzerland using WOFOST. `★ 1` `MIT`
- [paulianoprescu/winter-wheat-frost-kill](https://github.com/paulianoprescu/winter-wheat-frost-kill) - No description provided. `★ 1` `custom licence`
- [SmartDigitalAg/APSIM_calibration](https://github.com/SmartDigitalAg/APSIM_calibration) - APSIM 밀(전국) 생산량 추정. `★ 1` `no licence`
- [DrAhmedKheir/CropOracle-Egypt](https://github.com/DrAhmedKheir/CropOracle-Egypt) - AI multi-agent WhatsApp-based wheat advisory system for Egypt using APSIM Next Gen, Flask, weather/soil data, and scenario simulations. `MIT`
- [emmaiyke/ERT_RWU_Wheat_Project](https://github.com/emmaiyke/ERT_RWU_Wheat_Project) - This project uses field-based ERT with ML calibration to quantify root water uptake in wheat. Root architectures were pre-selected in greenhouse experiments, and field results are validated with… `no licence`
- [EthanSeok/APSIM_Wheat_Scenario](https://github.com/EthanSeok/APSIM_Wheat_Scenario) - 밀 작물 모형인 APSIM-wheat를 이용하여 과거 40년 기상자료를 시뮬레이션하는 관수(irrigation) 의사결정 지원 프로그램. `no licence`
- [granawkins/apsim_wheat](https://github.com/granawkins/apsim_wheat) - No description provided. `no licence`
- [Lidaeus/Wheat](https://github.com/Lidaeus/Wheat) - No description provided. `no licence`
- [SmartAG-Team/paper_cc_impact_wheat_disease](https://github.com/SmartAG-Team/paper_cc_impact_wheat_disease) - European wheat climate-change impacts on crop development, Septoria canopy damage and conditional yield response; manuscript, code and reproducibility evidence. `no licence`
- [zalf-rpm/AgMIP_BADJAM](https://github.com/zalf-rpm/AgMIP_BADJAM) - New AgMIP simulation initiated by Stefano Galmarini; uses AgMIP-Wheat data. `no licence`
- [zalf-rpm/clim4cast](https://github.com/zalf-rpm/clim4cast) - MONICA winter wheat calibration and simulations for the Clim4Cast project. `MPL-2.0`

<a id="wheat-r"></a>

#### R

- [pmartre/AgMIPWheat4](https://github.com/pmartre/AgMIPWheat4) - R scripts to analyze the simulation results of the AgMIPWheat4 global simulations. `★ 2` `MIT`
- [pwolper/SIMPLE-project](https://github.com/pwolper/SIMPLE-project) - Modeling wheat growth in northern Brazil using the SIMPLE crop model. `★ 2` `no licence`
- [ZCL-wyn/-wheat-dev-enviromics](https://github.com/ZCL-wyn/-wheat-dev-enviromics) - R scripts for the developmental enviromics framework: wheat TKW GxE dissection (under review). `★ 1` `MIT`
- [nosnibor27/WHEAT_phenology_forecaster](https://github.com/nosnibor27/WHEAT_phenology_forecaster) - Scripts utilizing a wheat model from the 1980s to forecast timing of growth stages through 2100 under climate change. `no licence`
- [nosnibor27/WSU_variety_testing_model](https://github.com/nosnibor27/WSU_variety_testing_model) - Calibrating the CERES-Wheat growth model using WSU Variety Testing reports from 2014 to 2018. `no licence`
- [RDKilgour/VLML4_dissertation_appendix_1](https://github.com/RDKilgour/VLML4_dissertation_appendix_1) - Key scripts (python & R) for running the CropNET winter wheat model locally (MacOS). `no licence`

<a id="wheat-other"></a>

#### Other

- [NTU-STEMLab/kinmen-wheat-dssat-remote-sensing](https://github.com/NTU-STEMLab/kinmen-wheat-dssat-remote-sensing) - Integrated remote sensing and DSSAT-based framework for wheat yield monitoring, management optimization, and climate change impact assessment in Kinmen, Taiwan. `no licence`

<a id="maize"></a>

### Maize

<a id="maize-python"></a>

#### Python

- [jennhsiao/ideotype](https://github.com/jennhsiao/ideotype) - workflow and data analysis for maizsim ideotype project. `★ 4` `MIT`
- [ErikaWarnatzsch/Malawi-Future-Climate-Modelling-Assessment](https://github.com/ErikaWarnatzsch/Malawi-Future-Climate-Modelling-Assessment) - Python scripts used for paper Warnatzsch and Reay (2019). Assessing Climate Change Projections and Impacts on Central Malawi’s Maize Yield: The Risk of Maladaptation… `★ 2` `MIT`
- [jennhsiao/upscale](https://github.com/jennhsiao/upscale) - MAIZSIM simulation setups to investigate climate impacts on maize growth and yield across continental US. `★ 2` `no licence`
- [LAMPSYORKU/NCOMMS_MaizeProduction](https://github.com/LAMPSYORKU/NCOMMS_MaizeProduction) - This repository contains Jupyter Notebook Python code used to analyze GGCMI Maize yield output data and generate figures for the manuscript titled "Climate Change Poses Significant Risks to Maize… `★ 1` `MIT`
- [AbdullahButt-00/irrigation-optimization-ppo-a2c](https://github.com/AbdullahButt-00/irrigation-optimization-ppo-a2c) - Reinforcement learning–based optimization of maize irrigation using PPO and A2C, with comparative evaluation of water efficiency and control performance. `no licence`
- [BerheAA10/kansas-maize-climate-risk-guide](https://github.com/BerheAA10/kansas-maize-climate-risk-guide) - No description provided. `no licence`
- [BerheAA10/kansas-maize-dssat-pythiaV1](https://github.com/BerheAA10/kansas-maize-dssat-pythiaV1) - Gridded model application for Kansas Maize. `no licence`
- [BerheAA10/kansas-maize-dssat-pythiaV2](https://github.com/BerheAA10/kansas-maize-dssat-pythiaV2) - spatial Kansas maize simulation. `no licence`
- [BerheAA10/kansas-maize-yield-dashboard-v3](https://github.com/BerheAA10/kansas-maize-yield-dashboard-v3) - No description provided. `no licence`
- [BerheAA10/kansas-maize-yield-gap-stability](https://github.com/BerheAA10/kansas-maize-yield-gap-stability) - Yield gap and Stability for Kansas Maize. `no licence`
- [bjc204/Clarketal_EarthsFuture_24](https://github.com/bjc204/Clarketal_EarthsFuture_24) - Figure generation code for Earth's Future aticle "Maize Yield Changes Under Sulfate Aerosol Climate Intervention Using Three Global Gridded Crop Models". `no licence`
- [darshrank/Maize-Runner](https://github.com/darshrank/Maize-Runner) - LLM agents that schedule nitrogen and irrigation for a simulated maize field, evaluated over Gainesville seasons. `no licence`
- [DrAhmedKheir/Egypt-Maize-APSIM-ML-Downscaling-Pipeline](https://github.com/DrAhmedKheir/Egypt-Maize-APSIM-ML-Downscaling-Pipeline) - This script integrates APSIM Next Generation, climate data, soil information, and machine learning to generate high-resolution (0.1°) maize yield maps for Egypt, including uncertainty and… `no licence`
- [franklineronoh/crop-modeling](https://github.com/franklineronoh/crop-modeling) - No description provided. `no licence`
- [gaurpushkar/lpjml-analysis](https://github.com/gaurpushkar/lpjml-analysis) - Notebooks evaluating LPJmL maize outputs (rainfed and irrigated) against remote-sensing and statistical data. `no licence`
- [heidinguyenViterra/iowa_corn](https://github.com/heidinguyenViterra/iowa_corn) - Simulating corn growth for the state of Iowa, USA using WOFOST 7.2. `no licence`
- [israeltankam/grainly](https://github.com/israeltankam/grainly) - This app helps farmers and agronomists optimize maize production through scientific simulations powered by the STICS crop model. `no licence`
- [j-vukosi/maize-drl-benchmark](https://github.com/j-vukosi/maize-drl-benchmark) - Research benchmark for evaluating deep reinforcement learning algorithms for adaptive maize irrigation scheduling. `MIT`
- [jbkze/agwat2026-dit-rl](https://github.com/jbkze/agwat2026-dit-rl) - Experiments for the DIT-RL revision (deficit irrigation, DRL under a seasonal water budget). `no licence`
- [pneague/Genetic-Algorithm-for-Corn-Genotype-Planting-Date-Optimization](https://github.com/pneague/Genetic-Algorithm-for-Corn-Genotype-Planting-Date-Optimization) - No description provided. `BSD-2-Clause`
- [princessplum/DSSAT-evolutionary-optimization](https://github.com/princessplum/DSSAT-evolutionary-optimization) - No description provided. `no licence`
- [PSUmodeling/Cycles-MW-maize](https://github.com/PSUmodeling/Cycles-MW-maize) - No description provided. `MIT`
- [PSUmodeling/Cycles-MW-maize-CMIP5](https://github.com/PSUmodeling/Cycles-MW-maize-CMIP5) - No description provided. `MIT`
- [ritviksahajpal/crop-models](https://github.com/ritviksahajpal/crop-models) - No description provided. `no licence`
- [rokuk/aquacrop-slovenia](https://github.com/rokuk/aquacrop-slovenia) - Data, figures and code for a calibration of Aquacrop for maize based on two sites in Slovenia. The calibrated model is used to make yield projections based on climate scenarios. `MIT`
- [wyq9303/NSGA-III_DSSAT_CERES_Maize](https://github.com/wyq9303/NSGA-III_DSSAT_CERES_Maize) - No description provided. `no licence`
- [ZhaoanWang/Learning-based-agricultural-Management](https://github.com/ZhaoanWang/Learning-based-agricultural-Management) - No description provided. `no licence`

<a id="maize-r"></a>

#### R

- [CalebTek/APSIM-Maize-Modelling](https://github.com/CalebTek/APSIM-Maize-Modelling) - APSIM-Maize-Modelling: A comprehensive repository leveraging the power of R for in-depth analysis and interpretation of maize crop growth simulations within the APSIM framework. Dive into the world… `★ 4` `no licence`
- [DanielKick-USDA/apsimxSimData](https://github.com/DanielKick-USDA/apsimxSimData) - This project has the goal of simulating realistic maize yield data across the USA using APSIMX. Simulated data is to be used for pretraining machine learning models. `★ 1` `no licence`
- [vanichols/ghproj_ccgap](https://github.com/vanichols/ghproj_ccgap) - How to get APSIM to simulate continuous corn yield gaps. `★ 1` `no licence`
- [amkusmec/maize_climate](https://github.com/amkusmec/maize_climate) - Efficacy of phenological adaptation for maize under climate change. `GPL-3.0`
- [egbendito/mashawara](https://github.com/egbendito/mashawara) - Variety and planting date advisories. The name comes from a mix of "maize advisory" (shawarar masara) in Hausa. `GPL-3.0`
- [nosnibor27/MAIZE_phenology_forecaster](https://github.com/nosnibor27/MAIZE_phenology_forecaster) - Scripts utilizing a maize model from the 1980s to forecast timing of growth stages through 2100 under climate change. `no licence`
- [peter-devoil/MaizeSunflowerUA](https://github.com/peter-devoil/MaizeSunflowerUA) - Maize & Sunflower simulations in Ukraine, 2023. `no licence`

<a id="maize-other"></a>

#### Other

- [Ehtsham-ai/Maize-Project-GR4](https://github.com/Ehtsham-ai/Maize-Project-GR4) - No description provided. `no licence`
- [mtigchelaar/maize-variability](https://github.com/mtigchelaar/maize-variability) - Data of maize yield projections under 2 and 4 dgC warming. `no licence`

<a id="other-cereals"></a>

### Barley, sorghum, millet and other cereals

<a id="other-cereals-javascript"></a>

#### JavaScript

- [jflater/sorghum-rye-modeling](https://github.com/jflater/sorghum-rye-modeling) - No description provided. `no licence`

<a id="other-cereals-python"></a>

#### Python

- [eggenm/senegal_aquacrop_model](https://github.com/eggenm/senegal_aquacrop_model) - No description provided. `★ 1` `no licence`
- [agrometjodhpur/pearl-millet-yield](https://github.com/agrometjodhpur/pearl-millet-yield) - AquaCrop-OSPy simulations of rainfed pearl millet yield across the 33 districts of Rajasthan, India. `custom licence`
- [gaurpushkar/crop-modelling-Ethiopia](https://github.com/gaurpushkar/crop-modelling-Ethiopia) - AquaCrop-OSPy simulations of teff yield and water use under planting dates and water management in the Ethiopian highlands. `no licence`

<a id="other-cereals-r"></a>

#### R

- [Ciampitti-Lab/CostNutriSenegalApp](https://github.com/Ciampitti-Lab/CostNutriSenegalApp) - No description provided. `★ 1` `no licence`
- [Janewanguimugo/APSIM_Sorghum](https://github.com/Janewanguimugo/APSIM_Sorghum) - You can plant these sorghum varieties in any country in the world. `★ 1` `no licence`
- [KeLiu7/Waterlogging-Barley](https://github.com/KeLiu7/Waterlogging-Barley) - No description provided. `★ 1` `no licence`
- [lindenwells/winter-research](https://github.com/lindenwells/winter-research) - No description provided. `no licence`
- [rmartinezferia/ryeSALUS](https://github.com/rmartinezferia/ryeSALUS) - Rye cover crop simulations with SALUS. `GPL-3.0`
- [spababu-sudo/CropModel-Sorghum](https://github.com/spababu-sudo/CropModel-Sorghum) - Library that contains all the codes I have done in the last three months. `no licence`

<a id="soybean"></a>

### Soybean

<a id="soybean-cplusplus"></a>

#### C++

- [Matthews-Research-Group/UTR-Soybean-BioCro](https://github.com/Matthews-Research-Group/UTR-Soybean-BioCro) - No description provided. `★ 1` `no licence`

<a id="soybean-python"></a>

#### Python

- [zalf-rpm/soybean-EU](https://github.com/zalf-rpm/soybean-EU) - No description provided. `★ 1` `no licence`
- [AnithaM55/Irrigation_DSS_Soybean](https://github.com/AnithaM55/Irrigation_DSS_Soybean) - Data_Driven Irrigation Decision Support System for Soybean using Remote Sensing and FAO_56 ET. `CC0-1.0`
- [BerheAA10/kansas-soybean-corn-dashboard](https://github.com/BerheAA10/kansas-soybean-corn-dashboard) - No description provided. `no licence`
- [GabyQueiroz/RLDSSAT_Soybean](https://github.com/GabyQueiroz/RLDSSAT_Soybean) - No description provided. `no licence`
- [Yan-wen-yao/soybean-climate-soil](https://github.com/Yan-wen-yao/soybean-climate-soil) - Python scripts for data processing, APSIM control, and Random Forest analysis of soybean yield response to climate and soil factors. `no licence`

<a id="soybean-r"></a>

#### R

- [infotroph/soyface_daycent](https://github.com/infotroph/soyface_daycent) - Daycent parameters and model-handling code for SoyFACE CO2 & temperature change simulations. `★ 5` `no licence`
- [cropsinsilico/Soybean-Sensitivity](https://github.com/cropsinsilico/Soybean-Sensitivity) - No description provided. `no licence`
- [sujatabogati/Soybean_Biocro_MS_Codes](https://github.com/sujatabogati/Soybean_Biocro_MS_Codes) - No description provided. `no licence`

<a id="soybean-other"></a>

#### Other

- [changmeng759/Configuration-aware-crop-model-comparison-of-APSIM-and-WOFOST-soybean-simulations](https://github.com/changmeng759/Configuration-aware-crop-model-comparison-of-APSIM-and-WOFOST-soybean-simulations) - My first independent project: data reproduction in an article. `no licence`
- [emmavanver/APSIM_PD_MG_Soybean](https://github.com/emmavanver/APSIM_PD_MG_Soybean) - Repository containing R code to run APSIM & evaluating Soybean optimum Planting Date x Maturity Group. `no licence`

<a id="legumes-oilseeds"></a>

### Other legumes and oilseeds

<a id="legumes-oilseeds-javascript"></a>

#### JavaScript

- [derekmichaelwright/AGILE_LDP_Phenology](https://github.com/derekmichaelwright/AGILE_LDP_Phenology) - Understanding photothermal interactions can help expand production range and increase genetic diversity of lentil (Lens culinaris Medik.). `★ 2` `no licence`

<a id="legumes-oilseeds-python"></a>

#### Python

- [cschulte7/Guar-AquaCrop-Calibrations-DO-NOT-EDIT-](https://github.com/cschulte7/Guar-AquaCrop-Calibrations-DO-NOT-EDIT-) - These files were created for the purposes of Caroline Schulte's accelerated masters thesis project and defense at the University of Arizona. Please do not make changes to these files. `no licence`
- [cschulte7/Guar-AquaCrop-Do-Not-Edit-](https://github.com/cschulte7/Guar-AquaCrop-Do-Not-Edit-) - These files were created for the purposes of Caroline Schulte's accelerated masters project and defense at the University of Arizona. Please do not make changes to these files. `no licence`

<a id="legumes-oilseeds-r"></a>

#### R

- [MarionDesRoseaux/sunflo-climat-futur](https://github.com/MarionDesRoseaux/sunflo-climat-futur) - No description provided. `★ 2` `CC-BY-SA-4.0`
- [Namita-J/climate-impacts-legumes](https://github.com/Namita-J/climate-impacts-legumes) - No description provided. `no licence`

<a id="potato"></a>

### Potato

<a id="potato-ampl"></a>

#### AMPL

- [marpols/irrigation_assessment](https://github.com/marpols/irrigation_assessment) - STICS crop model workspace and simulation results for PEI russet burbank potato irrigation assessment. `no licence`

<a id="potato-python"></a>

#### Python

- [luzagudelopalacio/Agroclimatica_Boyaca.Betek](https://github.com/luzagudelopalacio/Agroclimatica_Boyaca.Betek) - El proyecto trata sobre el proceso agroclimático de la papa en algunos municipios del Departamento de Boyacá, Colombia. `★ 1` `no licence`
- [EmeraldMP/S8-Irrigation-control](https://github.com/EmeraldMP/S8-Irrigation-control) - S8: Irrigation controle for pole the project. `no licence`
- [frank0434/ch1_sa](https://github.com/frank0434/ch1_sa) - No description provided. `MIT`
- [shohei/lintul-potato-dss-satellite](https://github.com/shohei/lintul-potato-dss-satellite) - Prototype decision support combining the LINTUL potato model with satellite data. `no licence`

<a id="potato-r"></a>

#### R

- [frank0434/Apsim_potato](https://github.com/frank0434/Apsim_potato) - No description provided. `no licence`
- [jninanya/Potato_Yield_Gap](https://github.com/jninanya/Potato_Yield_Gap) - Workflow for potato yield gap decomposition. `no licence`

<a id="potato-other"></a>

#### Other

- [caequezlam/APEX_Potato__Bolivia](https://github.com/caequezlam/APEX_Potato__Bolivia) - APEX model tabs calibration and validation - potato cultivars Bolivia. `no licence`
- [marpols/STICS_irrigation](https://github.com/marpols/STICS_irrigation) - STICS crop model workspace and simulation results for PEI russet burbank potato irrigation assessment. `no licence`
- [RobZys/RSPotato](https://github.com/RobZys/RSPotato) - No description provided. `no licence`

<a id="roots-tubers"></a>

### Cassava and other roots and tubers

<a id="roots-tubers-csharp"></a>

#### C#

- [Opamelas83/RDSSATMICH](https://github.com/Opamelas83/RDSSATMICH) - No description provided. `★ 1` `no licence`

<a id="roots-tubers-python"></a>

#### Python

- [research2441-tech/MDLM-RC](https://github.com/research2441-tech/MDLM-RC) - No description provided. `MIT`

<a id="cotton"></a>

### Cotton

<a id="cotton-python"></a>

#### Python

- [chenbin98/aquacrop_cotton_workflow](https://github.com/chenbin98/aquacrop_cotton_workflow) - Site-level AquaCrop cotton workflow scripts for data preparation, simulation, and calibration. `no licence`
- [DanavathGanesh/Round-2-Cotton-PyFAO56](https://github.com/DanavathGanesh/Round-2-Cotton-PyFAO56) - Round 2 task: PyFAO56 soil-water balance and SMAP comparison for irrigated and rainfed cotton fields. `no licence`
- [SmartAG-NWAFU/xinjiang-cotton-smt-irrigation](https://github.com/SmartAG-NWAFU/xinjiang-cotton-smt-irrigation) - Optimizing cotton irrigation strategy in Xinjiang. `MIT`
- [xuruifeng123/NDRL](https://github.com/xuruifeng123/NDRL) - NDRL: Cotton Irrigation and Nitrogen Application with Nested Dual-Agent Reinforcement Learning. `no licence`

<a id="cotton-r"></a>

#### R

- [attia3/texas-cotton-arid-enso](https://github.com/attia3/texas-cotton-arid-enso) - Reproducible R workflow for phenology-based ARID, relative cotton yield loss, and ENSO composites across Texas, 1975–2025. `MIT`

<a id="cotton-other"></a>

#### Other

- [wwwwwwangyuhao/awm](https://github.com/wwwwwwangyuhao/awm) - No description provided. `no licence`

<a id="sugar-crops"></a>

### Sugarcane and sugar beet

<a id="sugar-crops-python"></a>

#### Python

- [flossie-brown/Sugarcane_paper](https://github.com/flossie-brown/Sugarcane_paper) - Scripts for analysis of JULES model output. Characterizing the ozone (O3) yield gap in Sugarcane production in São Paulo Brazil. `no licence`

<a id="sugar-crops-r"></a>

#### R

- [djaiswal/SugarcaneBrazill](https://github.com/djaiswal/SugarcaneBrazill) - No description provided. `no licence`
- [mnqoliveira/future-sugar](https://github.com/mnqoliveira/future-sugar) - Source code for the analysis submitted to the Brazilian Bioenergy Science and Technology Conference (BBEST 2017). Abstract in folder 'publications'. `GPL-3.0`

<a id="vegetables"></a>

### Vegetables

<a id="vegetables-python"></a>

#### Python

- [kothawadegs/geoaquacrop-mustard](https://github.com/kothawadegs/geoaquacrop-mustard) - Mustard greens (leafy Brassica juncea) crop and greenhouse simulation for AquaCrop-OSPy / GeoAquaCrop. `no licence`
- [nayoung2da/garlic_Ideotype](https://github.com/nayoung2da/garlic_Ideotype) - No description provided. `no licence`
- [zalf-rpm/tomato-irrigation](https://github.com/zalf-rpm/tomato-irrigation) - No description provided. `MPL-2.0`

<a id="vegetables-r"></a>

#### R

- [mlabadie/StrawArchitecturalAnalysis](https://github.com/mlabadie/StrawArchitecturalAnalysis) - Strawberry Architectural analysis data from openalea.strawberry python library https://github.com/openalea/strawberry. `★ 1` `no licence`
- [Paul1D/Simulating-Climate-Change-Impacts-on-Onion-Cultivation](https://github.com/Paul1D/Simulating-Climate-Change-Impacts-on-Onion-Cultivation) - Repository for scriots and additinal for master thesis of paul daiber. `no licence`

<a id="vegetables-other"></a>

#### Other

- [falibabaei/DQN_irrigation-in-agriculture](https://github.com/falibabaei/DQN_irrigation-in-agriculture) - An DQN model was train to irrigate a tomato field. `★ 1` `no licence`

<a id="fruit-vine"></a>

### Fruit trees and grapevine

<a id="fruit-vine-javascript"></a>

#### JavaScript

- [Padilla331/riesgo-agroclimatico-vid-guadalupe](https://github.com/Padilla331/riesgo-agroclimatico-vid-guadalupe) - No description provided. `no licence`

<a id="fruit-vine-pov-ray-sdl"></a>

#### POV-Ray SDL

- [RamiALBASHA/Leaf_burn](https://github.com/RamiALBASHA/Leaf_burn) - Simulations of potted grapevine leaf temperatures during a summer heatwave in the South of France. `custom licence` `archived`

<a id="fruit-vine-python"></a>

#### Python

- [estergsancho26/carbonSequestration](https://github.com/estergsancho26/carbonSequestration) - My Bachelor Thesis code. `no licence`
- [imbaterry11/tetralone-ABA-simulation](https://github.com/imbaterry11/tetralone-ABA-simulation) - Details and code for the simulation of tetralone-ABA's impact on grapevine cold hardiness in North America. `MIT`
- [Mathilde1704/modelisation_hydroshoot](https://github.com/Mathilde1704/modelisation_hydroshoot) - HydroShoot. `custom licence`
- [RamiALBASHA/grapevine_stomatal_traits](https://github.com/RamiALBASHA/grapevine_stomatal_traits) - Study using HydroShoot to explore interesting stomatal traits to mitigate increasing temperature effects. `MIT` `archived`
- [shqwu/Almond_project](https://github.com/shqwu/Almond_project) - No description provided. `no licence`

<a id="fruit-vine-r"></a>

#### R

- [MoralesCastilla/PhenoDiversity](https://github.com/MoralesCastilla/PhenoDiversity) - Code utilized in Morales-Castilla et al. (2020) to forecast phenology and climatic suitability for winegrape cultivars over the 1950-2100 period. `★ 4` `GPL-3.0`
- [larscaspersen/AdaMedOr_climate-change-projections](https://github.com/larscaspersen/AdaMedOr_climate-change-projections) - No description provided. `★ 1` `no licence`
- [Mathilde1704/Using-FSPM-to-design-architectural-ideotypes-of-grapevine-](https://github.com/Mathilde1704/Using-FSPM-to-design-architectural-ideotypes-of-grapevine-) - No description provided. `★ 1` `no licence`
- [eikeluedeling/WashingtonCherry](https://github.com/eikeluedeling/WashingtonCherry) - No description provided. `no licence`
- [hortibonn/Walnut_Hedgerow_Agroforestry](https://github.com/hortibonn/Walnut_Hedgerow_Agroforestry) - No description provided. `custom licence`
- [larscaspersen/apple_budbreak_to_fullbloom](https://github.com/larscaspersen/apple_budbreak_to_fullbloom) - No description provided. `MIT`
- [szmoe/Cherry_blossom_prediction](https://github.com/szmoe/Cherry_blossom_prediction) - No description provided. `no licence`

<a id="fruit-vine-other"></a>

#### Other

- [nadja1390/water_use](https://github.com/nadja1390/water_use) - First results almond evapotranspiration in Idanha-a-Nova. `no licence`

<a id="plantation"></a>

### Oil palm, coffee, cocoa and other plantation crops

<a id="plantation-python"></a>

#### Python

- [casaroo/tea-plant-management](https://github.com/casaroo/tea-plant-management) - Tea plantation management toolkit combining growth modelling (LAI and yield via WOFOST/PCSE), pest recognition and weather data. `★ 1` `no licence`
- [3erMundo/monitor-agroclimatico-cacao](https://github.com/3erMundo/monitor-agroclimatico-cacao) - Automatizacion Python: descarga clima ERA5 (Open-Meteo) sobre la zona cacaotera de Santander y genera indicadores y mapas agroclimaticos. `no licence`
- [nina-grant/cocoa-chapter](https://github.com/nina-grant/cocoa-chapter) - Code for Grant et al. (2025) - Modeling the Impacts of Climate Change on Cocoa. `custom licence`

<a id="plantation-r"></a>

#### R

- [PalmStudio/Light_interception_vs_ages](https://github.com/PalmStudio/Light_interception_vs_ages) - Simulation of the light interception for different palm tree ages. `★ 1` `no licence`
- [PalmStudio/PLPE](https://github.com/PalmStudio/PLPE) - No description provided. `no licence`

<a id="plantation-other"></a>

#### Other

- [Iman04701/-Pineapple-Plantations-project-](https://github.com/Iman04701/-Pineapple-Plantations-project-) - Evapotranspiration Rates in Pineapple Plantations. `no licence`
- [PalmStudio/Palm_agroforestry](https://github.com/PalmStudio/Palm_agroforestry) - Agroforestry using palm trees. `GPL-3.0`

<a id="grassland"></a>

### Grassland, pasture and forage

<a id="grassland-python"></a>

#### Python

- [ClimAg/ClimAg](https://github.com/ClimAg/ClimAg) - EPA Research Project: Multifactorial causes of fodder crises in Ireland and risks due to climate change. `★ 3` `Apache-2.0`
- [zalf-rpm/IPP_grassland](https://github.com/zalf-rpm/IPP_grassland) - MONICA grassland calibration and simulations for Germany. `MPL-2.0`
- [zalf-rpm/sattgruen-germany](https://github.com/zalf-rpm/sattgruen-germany) - SattGrün germany cutting regimes. `MPL-2.0`

<a id="grassland-r"></a>

#### R

- [hjhawkins/Daycent-validation](https://github.com/hjhawkins/Daycent-validation) - Biogeochemical model (Daycent) savanna model. `★ 4` `no licence`
- [frank0434/Master](https://github.com/frank0434/Master) - repo for the master project - water stress for APSIMX lucerne model. `★ 3` `CC0-1.0`
- [enervifa/Daycent_Pasturas_UY](https://github.com/enervifa/Daycent_Pasturas_UY) - Visualizador de modelación de biomasa den DAYCENT de pasturas por región agroecológica en Uruguay. `MIT`
- [MikeJorge/DSSAT_produtividade_pastagens_brasileiras](https://github.com/MikeJorge/DSSAT_produtividade_pastagens_brasileiras) - As rotinas de processamento descritas a seguir são essenciais para modelar e visualizar o crescimento da forrageira Urochloa brizantha cv. Marandu em diferentes cenários de fertilização, nos biomas… `no licence`
- [monteiroleonardo/GlobalPastureYieldGapAnalysis](https://github.com/monteiroleonardo/GlobalPastureYieldGapAnalysis) - No description provided. `no licence`
- [mosterloh7/APSIM-Prairie-Model](https://github.com/mosterloh7/APSIM-Prairie-Model) - This repository contains code, input files, and documentation for simulating biomass production and nitrate-N loss in managed prairie agroecosystems using the APSIM Next Generation AgPasture module. `no licence`
- [Priyanath88/DairyMod-Tropical](https://github.com/Priyanath88/DairyMod-Tropical) - This repository containing the R code to parameters estimation, soil, climate data extraction, model validation, data analysis and reproduce all the figures and tables of the manuscript titled… `CC0-1.0`
- [Ranae/APSIM_Prairie](https://github.com/Ranae/APSIM_Prairie) - An APSIM model for prairie and everything I need to write a manuscript about it. `GPL-3.0`
- [Taisekwa/BASGRA-model-Resilient-pastures-project-](https://github.com/Taisekwa/BASGRA-model-Resilient-pastures-project-) - This repository contains codes that will be used for the resilient pastures project. `no licence`
- [yaron1000/DSSAT-BPPP](https://github.com/yaron1000/DSSAT-BPPP) - No description provided. `no licence`

<a id="grassland-other"></a>

#### Other

- [tcobian/Bison_Grazing](https://github.com/tcobian/Bison_Grazing) - Code that accounts for the soil carbon sequestration of bison grazing on perennial grasslands. Data was gathered from model outputs using the Decomposition and Denitrification (DNDC) model produced… `★ 1` `no licence`
- [hjhawkins/Mvenyane-modelling](https://github.com/hjhawkins/Mvenyane-modelling) - Model outputs from process-based models, linked with a manuscript entitled "Models can help identify people-environment trade-offs, enabling improved planning of grazing and burning in communal… `CC0-1.0`
- [huntercmackin/Agro-IBIS-Grassland-and-Grazing-Simulation-Processing-and-Analysis](https://github.com/huntercmackin/Agro-IBIS-Grassland-and-Grazing-Simulation-Processing-and-Analysis) - Processing simulation data from Agro-IBIS (originally simulated in FORTRAN on in-house supercomputers). This repo focuses on processing and analyzing updates made to the C3/C4 grassland code as well… `no licence`

<a id="bioenergy-other"></a>

### Bioenergy and other crops

<a id="bioenergy-other-cplusplus"></a>

#### C++

- [Matthews-Research-Group/biomass-crops-marginal-land](https://github.com/Matthews-Research-Group/biomass-crops-marginal-land) - No description provided. `GPL-2.0`

<a id="bioenergy-other-fortran"></a>

#### Fortran

- [IMMM-SFA/CLM5_bioenergy](https://github.com/IMMM-SFA/CLM5_bioenergy) - user namelist settings, code changes and driving scripts to set up CLM5 on Constance for bioenergy crop simulations. `★ 3` `no licence`

<a id="bioenergy-other-python"></a>

#### Python

- [wanyuhuangyqt/Aquacrop-Guayule](https://github.com/wanyuhuangyqt/Aquacrop-Guayule) - No description provided. `★ 3` `no licence`
- [paulianoprescu/biofuel-feedstock-forecasting](https://github.com/paulianoprescu/biofuel-feedstock-forecasting) - No description provided. `★ 1` `MIT`
- [johnlfield/Stover_postprocessing](https://github.com/johnlfield/Stover_postprocessing) - Post-processing and mapping DayCent stover harvest simulation results. `MIT`

<a id="bioenergy-other-r"></a>

#### R

- [NandhanaSunil/Using-HPC-for-climate-change-impact-assessment](https://github.com/NandhanaSunil/Using-HPC-for-climate-change-impact-assessment) - No description provided. `★ 1` `no licence`
- [dlebauer/lebauer2010ldr](https://github.com/dlebauer/lebauer2010ldr) - data and code used in manuscript. `no licence`
- [rmartinezferia/switchgrass_climate_change](https://github.com/rmartinezferia/switchgrass_climate_change) - No description provided. `no licence`

## Processes

<a id="phenology"></a>

### Phenology and development

<a id="phenology-python"></a>

#### Python

- [gettecr/Visualize_ND_GDDs](https://github.com/gettecr/Visualize_ND_GDDs) - Visualization of growing degree days for North Dakota. `★ 2` `MIT`
- [ajwdewit/isidora](https://github.com/ajwdewit/isidora) - System generating near-real-time, phenology-driven crop and weather advisories. `★ 1` `EUPL-1.2`
- [bs6523/CMSC6950_Group_Project](https://github.com/bs6523/CMSC6950_Group_Project) - Growing Degree Days Group project. `★ 1` `no licence`
- [cw7734/CMSC6950-Growing-Degree-Days](https://github.com/cw7734/CMSC6950-Growing-Degree-Days) - Course project computing growing degree days. `★ 1` `no licence`
- [Boxuanli2013/GDD](https://github.com/Boxuanli2013/GDD) - Growing Degree Days in Canada. `no licence`
- [byron-evers/project](https://github.com/byron-evers/project) - Thermal time indices (biometeorological time, physiological days) merged with UAV data; agronomy course project. `no licence`
- [cmsc6950-spring-2018/GDD-Project--Team1](https://github.com/cmsc6950-spring-2018/GDD-Project--Team1) - Course project computing growing degree days. `MIT`
- [hby-125/compound-extremes-crop-phenology-code](https://github.com/hby-125/compound-extremes-crop-phenology-code) - Code for “Compound climate extremes reshape staple-crop phenology and cropping-system turnaround windows across China”. `MIT`
- [hliu666/GDD](https://github.com/hliu666/GDD) - No description provided. `no licence`
- [mirhendi/GDD-visualization](https://github.com/mirhendi/GDD-visualization) - Canada growing degree days (GDD) data visualization. `no licence`
- [shawnatwsu/GrowingDegreeDay_Gridmet_Jan_Apr](https://github.com/shawnatwsu/GrowingDegreeDay_Gridmet_Jan_Apr) - No description provided. `no licence`
- [StavromularBeta/GDD](https://github.com/StavromularBeta/GDD) - This is the growing degree days project. `no licence`
- [zalf-rpm/crop-tsum-EU](https://github.com/zalf-rpm/crop-tsum-EU) - Calculation of crop temperature sums and sowing dates across Europe. `MPL-2.0`

<a id="phenology-r"></a>

#### R

- [HajarMojahid/phenoflex_cross_validation](https://github.com/HajarMojahid/phenoflex_cross_validation) - PhenoFlex cross-regional validation across Germany and Spain. `★ 3` `no licence`
- [mcrimmins/GDD-climate](https://github.com/mcrimmins/GDD-climate) - Growing Degree Day Project with TopoWx data. `★ 1` `no licence`
- [Atifshinwari/Chill_quantification_in_Afghanistan](https://github.com/Atifshinwari/Chill_quantification_in_Afghanistan) - No description provided. `no licence`
- [climateindicators/growing-degree-days](https://github.com/climateindicators/growing-degree-days) - This indicator shows changes in growing degree days, which can signal changes in the timing and length of pollen seasons in the United States. `no licence`
- [EduardoFernandezC/chill_mediterranean](https://github.com/EduardoFernandezC/chill_mediterranean) - This repository contains data and scripts for producing chill projection in the Mediterranean area. `no licence`
- [ElsitaK/Growing-Degree-Days](https://github.com/ElsitaK/Growing-Degree-Days) - Calculation of Growing Degree Days using projected future maximum and minimum temperatures from MACA downscaled climate datasets (available at… `no licence`
- [jeremylweiss/azmet-cgdd-graphs](https://github.com/jeremylweiss/azmet-cgdd-graphs) - R project to create time series graphs of cumulative growing degree days for meteorological stations in the AZMET network. `no licence`
- [JNBauer/aws-shiny-PLS](https://github.com/JNBauer/aws-shiny-PLS) - No description provided. `no licence`
- [larscaspersen/phenoflex_toyproblem](https://github.com/larscaspersen/phenoflex_toyproblem) - No description provided. `no licence`
- [Lunalo/johnlunalomsccodes](https://github.com/Lunalo/johnlunalomsccodes) - No description provided. `no licence`

<a id="phenology-other"></a>

#### Other

- [anam16/Potted-Tree-Experiments](https://github.com/anam16/Potted-Tree-Experiments) - No description provided. `no licence`
- [apkovaleski/EL_Methods](https://github.com/apkovaleski/EL_Methods) - No description provided. `no licence`
- [qjhart/amerines-california](https://github.com/qjhart/amerines-california) - Comparison of Growing Degree Days (GDD). `no licence`

<a id="photosynthesis"></a>

### Photosynthesis, canopy and transpiration

<a id="photosynthesis-julia"></a>

#### Julia

- [VEZY/PlantBiophysics-paper](https://github.com/VEZY/PlantBiophysics-paper) - Code related to the PlantBiophysics.jl package paper. `★ 3` `custom licence`
- [VEZY/FSPM2026_AgriPV_Design](https://github.com/VEZY/FSPM2026_AgriPV_Design) - Designing Agrivoltaics systems optimizing photosynthesis. `MIT`

<a id="photosynthesis-python"></a>

#### Python

- [simonrobjones/stomatal-decoupling](https://github.com/simonrobjones/stomatal-decoupling) - Code to produce the figures in Jones et al - "Stomatal decoupling from photosynthesis under high temperatures is consistent with stomatal optimisation theory". `no licence`

<a id="photosynthesis-r"></a>

#### R

- [JulienLamour/Comparison_FvCB_JB](https://github.com/JulienLamour/Comparison_FvCB_JB) - Evaluation of the Johnson and Berry (2021) model of photosynthesis. `no licence`
- [williamtsalter/stomatal-kinetics-wheat](https://github.com/williamtsalter/stomatal-kinetics-wheat) - No description provided. `CC-BY-4.0`

<a id="architecture"></a>

### Plant architecture and FSPM

<a id="architecture-python"></a>

#### Python

- [Pepe-oss/3D-Reconstruction-analysis-of-maize-soybean-intercropping-competition-under-water-stress](https://github.com/Pepe-oss/3D-Reconstruction-analysis-of-maize-soybean-intercropping-competition-under-water-stress) - Calculating Light Interception for Intercropping Using Helios. `no licence`
- [thkhavi/leafangle_supplement](https://github.com/thkhavi/leafangle_supplement) - Scripts for examining light environment of virtual sorghum Lpy that vary in leaf angle. `GPL-2.0`

<a id="architecture-r"></a>

#### R

- [Plant-Root-Soil-Interactions-Modelling/CPB-LiDAR](https://github.com/Plant-Root-Soil-Interactions-Modelling/CPB-LiDAR) - A virtual pipeline to study sensitivity of UAV-like LiDAR metrics to plant parameters using CPlantBox. `GPL-3.0`
- [VEZY/ENSAYO_Transmittance_Map](https://github.com/VEZY/ENSAYO_Transmittance_Map) - No description provided. `GPL-3.0`

<a id="roots"></a>

### Roots and rhizosphere

<a id="roots-cplusplus"></a>

#### C++

- [m-giraud/CPB20R3](https://github.com/m-giraud/CPB20R3) - No description provided. `no licence`

<a id="roots-r"></a>

#### R

- [HydraulicViper/Peng2023](https://github.com/HydraulicViper/Peng2023) - Script used for Peng et al. 2023. `GPL-3.0`

<a id="roots-shell"></a>

#### Shell

- [ilovaldivia/Lopez-Valdivia_2023_RootEvolution](https://github.com/ilovaldivia/Lopez-Valdivia_2023_RootEvolution) - No description provided. `no licence`
- [ilovaldivia/LopezValdivia_2024_YieldStability](https://github.com/ilovaldivia/LopezValdivia_2024_YieldStability) - No description provided. `no licence`
- [ilovaldivia/Sidhu_et_al_2023](https://github.com/ilovaldivia/Sidhu_et_al_2023) - OpenSimRoot simulations. `no licence`

<a id="soil-water"></a>

### Soil water and heat

<a id="soil-water-c"></a>

#### C

- [vlatorre847/SWAMPOPT](https://github.com/vlatorre847/SWAMPOPT) - A repository for the optimization of water irrigation scheduling problem from the DICAM Group of the Alma Mater Studiorum University of Bologna. `★ 1` `GPL-3.0`

<a id="soil-water-matlab"></a>

#### MATLAB

- [iaelraij/Hydrus_variability](https://github.com/iaelraij/Hydrus_variability) - No description provided. `no licence`

<a id="soil-water-python"></a>

#### Python

- [lizhengyu1118/Hydrus3D-dataanalyse](https://github.com/lizhengyu1118/Hydrus3D-dataanalyse) - lizhengyu1118@gmail.com. `★ 1` `no licence`
- [prqpfkjw8c-jpg/LLM-Irrigation-Scheduling](https://github.com/prqpfkjw8c-jpg/LLM-Irrigation-Scheduling) - Simulation models, LLM workflow, prompting strategies, experimental results, and deployment interface examples for LLM-driven autonomous irrigation scheduling. `★ 1` `no licence`
- [AhmadShahnewaz/solarin](https://github.com/AhmadShahnewaz/solarin) - Soil Infiltration Model with Hydrus 2D. `MIT`
- [EdwinLSA/gota-pp-optimization-monte-carlo-simulation](https://github.com/EdwinLSA/gota-pp-optimization-monte-carlo-simulation) - Monte Carlo simulation engine for irrigation optimization. It runs thousands of randomized scenarios over NASA POWER variables to estimate outcome probability distributions and identify the… `no licence`
- [egpark-knu/aquaagent-ospy-reproducibility](https://github.com/egpark-knu/aquaagent-ospy-reproducibility) - Public reproducibility snapshot for AquaAgent-OSPy irrigation DSS paper. `custom licence`
- [Flora0627/irrigation-PPO](https://github.com/Flora0627/irrigation-PPO) - No description provided. `no licence`
- [GabyQueiroz/RBS_RL_Irrigation](https://github.com/GabyQueiroz/RBS_RL_Irrigation) - Source code for the article "Comparative Analysis of Reinforcement Learning and Rule-Based system Approaches for Irrigation Using AquaCrop". `no licence`
- [giubrune/Sugar](https://github.com/giubrune/Sugar) - No description provided. `no licence`
- [halilunaziru73-creator/Coupled-Water-Fluxes-Pore-Scale-Dynamics-Precision-Irrigation-Mulching-Feedback-Loops](https://github.com/halilunaziru73-creator/Coupled-Water-Fluxes-Pore-Scale-Dynamics-Precision-Irrigation-Mulching-Feedback-Loops) - Results of 10,190 Daisy soil-plant-atmosphere simulations: how precision irrigation and evaporation-control mulching jointly shape soil water fluxes, pore-structure-mediated dynamics, yield and… `MIT`
- [jbkze/dit-rl-implementation](https://github.com/jbkze/dit-rl-implementation) - No description provided. `Apache-2.0`
- [jerabekjak/runpractices](https://github.com/jerabekjak/runpractices) - run agricultural managemet practices sensitivity analysis of soil hydraulic parameters using hydrus. `no licence`
- [Jintpong/PPO-Irrigation](https://github.com/Jintpong/PPO-Irrigation) - No description provided. `no licence`
- [kp-square/Aquacrop-Richards-dRL](https://github.com/kp-square/Aquacrop-Richards-dRL) - No description provided. `no licence`
- [lizhengyu1118/Python-Hydrus](https://github.com/lizhengyu1118/Python-Hydrus) - No description provided. `no licence`
- [mouslim003/drl-alhaouz-irrigation](https://github.com/mouslim003/drl-alhaouz-irrigation) - No description provided. `MIT`
- [Project-Resilience/praise](https://github.com/Project-Resilience/praise) - Project Resilience Aquacrop Irrigation Strategy with Evolution. `Apache-2.0`
- [sergio-titus/Shared-Irrigation-Water-Allocation](https://github.com/sergio-titus/Shared-Irrigation-Water-Allocation) - AquaCrop-OSPy framework comparing PPO reinforcement learning with lightweight strategies for shared irrigation-water allocation across multiple climates. `MIT`
- [TecqHarishKrish/IrriVise](https://github.com/TecqHarishKrish/IrriVise) - IrriVise is a Digital Twin-based smart irrigation research framework combining Reinforcement Learning, counterfactual decision-regret estimation, and adaptive soil-state sensing to optimize water… `no licence`
- [zalf-rpm/amei_exercises](https://github.com/zalf-rpm/amei_exercises) - MONICA exercises from the AMEI soil temperature model exchange (bare soil and Maricopa wheat FACE). `no licence`

<a id="soil-water-r"></a>

#### R

- [Ikenna10/TAPS-Hackathon-2024](https://github.com/Ikenna10/TAPS-Hackathon-2024) - Irrigation Scheduling Tool using TAPS data in Western Kansas USA. `★ 2` `no licence`
- [ddlawton/soil_moisture_modeling](https://github.com/ddlawton/soil_moisture_modeling) - Looking at the effects of cover crop on soil moisture. `no licence`
- [EntingTang/Data_analysis](https://github.com/EntingTang/Data_analysis) - No description provided. `no licence`
- [KWB-R/flextreat.hydrus1d](https://github.com/KWB-R/flextreat.hydrus1d) - Soil Water Balance and Solute Transport Modelling Scenarios for Project Flextreat. `MIT`

<a id="soil-water-other"></a>

#### Other

- [El-Naggar8876/VRI-Decision-Support-Tool-Using-R](https://github.com/El-Naggar8876/VRI-Decision-Support-Tool-Using-R) - No description provided. `no licence`
- [giubrune/Paper_Sugar](https://github.com/giubrune/Paper_Sugar) - No description provided. `no licence`
- [salitree-PID/Hydrus-Projects](https://github.com/salitree-PID/Hydrus-Projects) - Hydrus projects to evaluate management alternatives sopin soil salinization. `no licence`

<a id="soil-nutrients"></a>

### Soil carbon, nitrogen and nutrients

<a id="soil-nutrients-ags-script"></a>

#### AGS Script

- [zalf-rpm/spreewasserN](https://github.com/zalf-rpm/spreewasserN) - No description provided. `MPL-2.0`

<a id="soil-nutrients-csharp"></a>

#### C#

- [MAGALA-RICHARD/CarbonYieldEvaluationMorrowPlots](https://github.com/MAGALA-RICHARD/CarbonYieldEvaluationMorrowPlots) - Carbon and Yield Evaluation Morrow Plots. `★ 2` `MIT`

<a id="soil-nutrients-eagle"></a>

#### Eagle

- [jungej62/Carbernza](https://github.com/jungej62/Carbernza) - Modeling carbon flux in IWG cropping systems. `no licence`

<a id="soil-nutrients-javascript"></a>

#### JavaScript

- [AAVADI/global_SOC_SSP](https://github.com/AAVADI/global_SOC_SSP) - Global soil organic carbon modelling under SSP climate trajectories. `★ 1` `MIT`

<a id="soil-nutrients-matlab"></a>

#### MATLAB

- [wangyakai01/Nleaching](https://github.com/wangyakai01/Nleaching) - Adaptive Strategies for Reducing Yield-Scaled Nitrate Leaching in the US Midwest. `no licence`

<a id="soil-nutrients-netlogo"></a>

#### NetLogo

- [KaziMaselUllah/Incentive_SOC_Carinata](https://github.com/KaziMaselUllah/Incentive_SOC_Carinata) - Evaluating the Incentive for Soil Organic Carbon Sequestration from Carinata Production in the Southeast United States. `no licence`

<a id="soil-nutrients-python"></a>

#### Python

- [Rickon566/Fertilizer-Management-for-Global-Ammonia-Emission-Reduction](https://github.com/Rickon566/Fertilizer-Management-for-Global-Ammonia-Emission-Reduction) - Code for this paper. `★ 9` `GPL-3.0`
- [bokofod/RothC_SOC](https://github.com/bokofod/RothC_SOC) - This methodology accepts the use of the RothC (Rothamsted Carbon) model for assessing the content of Soil Organic Carbon (SOC) in topsoils. The RothC model assess carbon turnover based on… `★ 6` `no licence`
- [asb219/evaluate-SOC-models](https://github.com/asb219/evaluate-SOC-models) - Evaluate the performance of new-generation soil organic carbon models with radiocarbon data of soil density fractions. `★ 4` `GPL-3.0`
- [C-Ameseder/1.2_Change_in_SOC_for_agr_practice](https://github.com/C-Ameseder/1.2_Change_in_SOC_for_agr_practice) - This project predicts the change in soil organic carbon when changing agricultural practice. `★ 2` `no licence`
- [carbonplan/ew-byte-03](https://github.com/carbonplan/ew-byte-03) - Code to support modeling bytes project on the time resolution of meteorological forcing. `★ 1` `MIT`
- [greenbackdev/soc_targets_europe](https://github.com/greenbackdev/soc_targets_europe) - Code associated to the publication "A new approach to estimate soil organic carbon content targets in European croplands.". `★ 1` `no licence`
- [carbajalmariella/chugay_model](https://github.com/carbajalmariella/chugay_model) - Crop rotation maps and soil organic carbon modeling to predict carbon. `MIT`
- [Christhel-Andrade/Land-carbon-and-bioeconomy-modelling](https://github.com/Christhel-Andrade/Land-carbon-and-bioeconomy-modelling) - Scripts illustrating workflows for soil carbon modelling, bioeconomy scenarios, spatial data processing, and LCA uncertainty analysis. `MIT`
- [climatecarbonlanduse/MRV_for_SOC_article](https://github.com/climatecarbonlanduse/MRV_for_SOC_article) - Code sharing for the article Building a platform for regionalized monitoring, reporting and verification (MRV) for soil organic carbon (SOC) change in agriculture – case Sweden. `no licence`
- [Coljak/Spreewasser-N](https://github.com/Coljak/Spreewasser-N) - No description provided. `GPL-3.0`
- [ElkeBrandes/dndc_iowa](https://github.com/ElkeBrandes/dndc_iowa) - SQL scripts, lists of assumptions, markdown scripts, and other data relevant for the INRC funded project of nutrient leaching from corn/soybean and switchgrass in Iowa. `GPL-3.0`
- [hereugo-ak/mini-mrv-varaha](https://github.com/hereugo-ak/mini-mrv-varaha) - No description provided. `no licence`
- [ilmenichetti/SweSOC_Py](https://github.com/ilmenichetti/SweSOC_Py) - No description provided. `no licence`
- [johnlfield/BRC_SoilC](https://github.com/johnlfield/BRC_SoilC) - No description provided. `no licence`
- [mdw7fc/soil-n-resilience](https://github.com/mdw7fc/soil-n-resilience) - Code and data for: Soil health buffers nitrogen supply disruptions (Wallenstein & Manning 2026, Nature Food). `custom licence`
- [mihirobendre/RothC_Implementation_Axam](https://github.com/mihirobendre/RothC_Implementation_Axam) - RothC soil organic carbon implementation (Python) for the Axam project. `no licence`
- [mihirobendre/RothC_Implementation_Ecobliss](https://github.com/mihirobendre/RothC_Implementation_Ecobliss) - RothC soil organic carbon implementation (Python) for the Ecobliss project. `no licence`
- [mihirobendre/RothC_updating_C_in_by_yr](https://github.com/mihirobendre/RothC_updating_C_in_by_yr) - RothC with yearly updates of carbon inputs (Python). `no licence`
- [mikevogt/Analyzing-Model-Free-RL-Algorithms-for-Fertilizer-Management-in-Simulated-Crop-Growth](https://github.com/mikevogt/Analyzing-Model-Free-RL-Algorithms-for-Fertilizer-Management-in-Simulated-Crop-Growth) - This GitHub represents the code-base relating to the paper "Analyzing Model-Free Reinforcement Learning Algorithms for Fertilizer Management in Simulated Crop Growth". `no licence`
- [Scarlett-Yu/ABMI-intern-project](https://github.com/Scarlett-Yu/ABMI-intern-project) - Environment data processing, data visualization. `no licence`
- [Sparkxt-0318/LoAM](https://github.com/Sparkxt-0318/LoAM) - Limits of Agricultural Monitoring. `MIT`
- [yollotl-mumina/ammonia_emissions_GrignonFrance](https://github.com/yollotl-mumina/ammonia_emissions_GrignonFrance) - Models ALFAM2 and EMEP. `MIT`
- [zalf-rpm/macsur-cgra-soc-spinup](https://github.com/zalf-rpm/macsur-cgra-soc-spinup) - MONICA soil organic carbon spin-up simulations for MACSUR. `no licence`
- [zalf-rpm/RapSmartN](https://github.com/zalf-rpm/RapSmartN) - No description provided. `MPL-2.0`
- [zalf-rpm/Safe-H2O-Farm](https://github.com/zalf-rpm/Safe-H2O-Farm) - No description provided. `MPL-2.0`

<a id="soil-nutrients-r"></a>

#### R

- [whrc/Soil-Carbon-Debt](https://github.com/whrc/Soil-Carbon-Debt) - R code and spatial predictions for WHRC-TNC project modeling spatial extent of soil carbon loss due to agriculture. `★ 18` `MIT`
- [FAO-SID/GSOCseq](https://github.com/FAO-SID/GSOCseq) - No description provided. `★ 7` `no licence`
- [ncss-tech/gsp-gsocseq](https://github.com/ncss-tech/gsp-gsocseq) - Workspace for US Global Soil Organic Carbon Sequestration Project. `★ 6` `GPL-3.0`
- [FAO-SID/GSOCseq-scripts](https://github.com/FAO-SID/GSOCseq-scripts) - GSOCseq Scripts. `★ 5` `no licence`
- [yuanhongdeng/DAYCENT-soil-carbon-pools](https://github.com/yuanhongdeng/DAYCENT-soil-carbon-pools) - The respository include script for running DAYCENT model and postprocessing DAYCENT outputs for the manuscript entitled "Regional modeling of soil carbon dynamics: Linking conceptual pools against… `★ 4` `no licence`
- [YuqingWUR/Paper_code](https://github.com/YuqingWUR/Paper_code) - Code for RothC initialization and simulation. `★ 3` `no licence`
- [Zairpv/RothC-Process-based-modeling](https://github.com/Zairpv/RothC-Process-based-modeling) - This repository contains scripts for implementing the RothC (Rothamsted Carbon) model to simulate **soil organic carbon (SOC) dynamics** in managed forests. `★ 3` `MIT`
- [BjnNowak/PhotosynteticActivity](https://github.com/BjnNowak/PhotosynteticActivity) - Data and script for "Plot-scale assessment of photosynthetic activity to promote soil carbon sequestration". `★ 2` `no licence`
- [aj-sykes92/legumes-translated-soil-c](https://github.com/aj-sykes92/legumes-translated-soil-c) - Repository for soil carbon modelling and analyses performed for the Legumes Translated project. `★ 1` `GPL-3.0`
- [NilsDroste/SoilCarbonInsurance](https://github.com/NilsDroste/SoilCarbonInsurance) - Data and Code repository for Droste et al. (2020) ERL. `★ 1` `no licence`
- [PeraltaLab/PWES_SoilBio](https://github.com/PeraltaLab/PWES_SoilBio) - Perennial grain crop, soil food web and soil carbon dynamics. `★ 1` `GPL-3.0`
- [AgroVisionProject/miniApplet](https://github.com/AgroVisionProject/miniApplet) - No description provided. `no licence`
- [aj-sykes92/soil-c-macc](https://github.com/aj-sykes92/soil-c-macc) - Repository for code used to develop simulations underlying soil C marginal abatement cost curve paper. `GPL-3.0`
- [annam-esd/P_EU](https://github.com/annam-esd/P_EU) - No description provided. `no licence`
- [boristupek/OPAL_LUC_C_sink_Finland](https://github.com/boristupek/OPAL_LUC_C_sink_Finland) - Input data and R code for soil carbon modelling supporting study on "Extensification and afforestation of cultivated mineral soil for climate change mitigation in Finland" by Tupek et al. 2020. `custom licence`
- [ilmenichetti/SweSOC](https://github.com/ilmenichetti/SweSOC) - No description provided. `no licence`
- [JanBlanke/climate_sensitivity](https://github.com/JanBlanke/climate_sensitivity) - R scripts for the manuscript "Effect of climate data on simulated carbon and nitrogen balances for Europe". `no licence`
- [JanBlanke/N_application](https://github.com/JanBlanke/N_application) - R scripts for the manuscript "The impact of changes in land use intensity and climate on balances of crop yield and nitrogen leaching". `no licence`
- [karla-dominguez/NC_SARE_project](https://github.com/karla-dominguez/NC_SARE_project) - Nitrogen Tracking Tool. `no licence`
- [mmlaan/CAF_P18O](https://github.com/mmlaan/CAF_P18O) - soilR modeling of P at CAF. `no licence`
- [MPIBGC-TEE/subsoilCseq](https://github.com/MPIBGC-TEE/subsoilCseq) - Publication files related to subsoil C sequestration. `no licence`
- [Pcatis/RothC-Climate-Change](https://github.com/Pcatis/RothC-Climate-Change) - No description provided. `no licence`
- [QianqianDu1122/OFPE_heterogeneity_residual_N](https://github.com/QianqianDu1122/OFPE_heterogeneity_residual_N) - No description provided. `no licence`
- [scmcclelland/DayCent-Soil-C-Statistics](https://github.com/scmcclelland/DayCent-Soil-C-Statistics) - R project for DayCent Soil Carbon (C) Statistics. `no licence`
- [stefanospotorno/RothC-Flanders](https://github.com/stefanospotorno/RothC-Flanders) - No description provided. `no licence` `archived`
- [Teneille97/nel_sweden_agsoil_2026](https://github.com/Teneille97/nel_sweden_agsoil_2026) - Modeling decomposition rates of soil organic matter thermal stability pools. `no licence`

<a id="soil-nutrients-other"></a>

#### Other

- [claraqin/Nitrogen-Balance-Corn-County](https://github.com/claraqin/Nitrogen-Balance-Corn-County) - Validation of remote sensing of nitrogen balance. `★ 1` `MIT`
- [EthiopiaCiatGit/RothC-Model](https://github.com/EthiopiaCiatGit/RothC-Model) - No description provided. `no licence`
- [katecoelli/RothC_Transpiration-based_Inputs](https://github.com/katecoelli/RothC_Transpiration-based_Inputs) - Calibrating RothC according to b parameter of Transpiration based plant residue inputs. `no licence`
- [yanefsilva/Daycent_ICLS](https://github.com/yanefsilva/Daycent_ICLS) - Code with schedule files used in Daycent calibration and validation for ICLS in Atlantic Forest, Brazil. `no licence`

<a id="greenhouse-gases"></a>

### Agricultural greenhouse gases

<a id="greenhouse-gases-python"></a>

#### Python

- [drylse/fil_rouge](https://github.com/drylse/fil_rouge) - Hosting group work on N2O emissions at the farm of Grignon. `★ 1` `no licence`
- [JenniferGao191/ClimateData](https://github.com/JenniferGao191/ClimateData) - No description provided. `★ 1` `no licence`
- [Jayan-V/DNDC---DayCent-style-analysis](https://github.com/Jayan-V/DNDC---DayCent-style-analysis) - Compared the Outcome of two Process based models to Analyse GHG Emissions. `no licence`

<a id="greenhouse-gases-r"></a>

#### R

- [snailslowrun/N2O](https://github.com/snailslowrun/N2O) - The representation of environmental factors that influence N2O emissions in DAYCENT, DNDC and SWAT. `★ 3` `no licence`
- [edvlmaas/national_gwp](https://github.com/edvlmaas/national_gwp) - National sustainable agriculture study. `★ 1` `no licence`
- [whitfieldmg/trinityghg](https://github.com/whitfieldmg/trinityghg) - No description provided. `★ 1` `no licence`
- [aj-sykes92/agroforestry-defra-prelim](https://github.com/aj-sykes92/agroforestry-defra-prelim) - Preliminary modelling and data preparation for assessment of the cost-effectiveness of agroforestry systems as a GHG mitigation measure in UK agriculture. `GPL-3.0`
- [Priyanath88/GarssGro_APSIM_Livestock_GHG_Model](https://github.com/Priyanath88/GarssGro_APSIM_Livestock_GHG_Model) - This repository contains the scripts to run the GrassGro (GGTactical) and APSIM to simulate the livestock GHG emissions in sheep and beef farming systems. `CC0-1.0`

<a id="evapotranspiration"></a>

### Evapotranspiration and irrigation

<a id="evapotranspiration-javascript"></a>

#### JavaScript

- [mostafajavadian/ET_Trend_GEE](https://github.com/mostafajavadian/ET_Trend_GEE) - In this study which has entirely done by Google Earth Engine, we developed a user-friendly evapotranspiration Trend monitoring (ETM) application that enables users to produce annual AET map for any… `★ 5` `no licence`
- [Osman-Geomatics93/Sudan-Evapotranspiration-Analysis-Project-](https://github.com/Osman-Geomatics93/Sudan-Evapotranspiration-Analysis-Project-) - Overview This project provides a comprehensive analysis of evapotranspiration (ET) patterns in Sudan using Google Earth Engine. The analysis includes temporal trends, drought assessment, and climate… `★ 3` `MIT`
- [Satwik-1234/Crop-water-Balance-Analysis-GEE-](https://github.com/Satwik-1234/Crop-water-Balance-Analysis-GEE-) - GEE script for the assessment of the crop water requirement and water balance for the Satara, Sangli, Kolhapur. `★ 1` `Apache-2.0`
- [rumahpenelitian/bogor-city-evapotranspiration](https://github.com/rumahpenelitian/bogor-city-evapotranspiration) - Penggunaan evapotranspiration pda wilayah Kota Bogor. `MIT`

<a id="evapotranspiration-matlab"></a>

#### MATLAB

- [t-sekai/cop](https://github.com/t-sekai/cop) - A Computational Platform to Optimize Irrigation for Maximum Farming Yield using Deep Learning and Dynamic Modeling &#91;2021 Syopsys Science Fair Honorable Mention&#93;. `★ 1` `no licence`
- [wuhuill/multiobjective-irrigation-scheduling-de](https://github.com/wuhuill/multiobjective-irrigation-scheduling-de) - MATLAB demo for irrigation scheduling optimization with multi-objective DE and the EPIC crop growth module. `no licence`

<a id="evapotranspiration-perl"></a>

#### Perl

- [dancejod/masters-thesis](https://github.com/dancejod/masters-thesis) - Code for my Master's thesis on UAV thermal calibration and evapotranspiration estimation (Charles University in Prague, 2026). `no licence`

<a id="evapotranspiration-python"></a>

#### Python

- [EDSEL-skoltech/multi_objective_irrigation](https://github.com/EDSEL-skoltech/multi_objective_irrigation) - Multi-objective irrigation optimization using a crop simulation model and historical weather data. `★ 20` `MIT` `archived`
- [nelsbjarke/PET](https://github.com/nelsbjarke/PET) - This repository contains the scripts used to generate the CMIP derived ensemble of potential and reference evapotranspiration. `★ 9` `no licence`
- [sciencebyAJ/Robust-Ecosystem-Water-and-Energy-Fluxes](https://github.com/sciencebyAJ/Robust-Ecosystem-Water-and-Energy-Fluxes) - Evapotranspiration flux estimation using a variety of eddy covariance data sources. `★ 8` `MIT`
- [Kripankc/evapotranspiration-mapping-on-GEE](https://github.com/Kripankc/evapotranspiration-mapping-on-GEE) - day 1 evapotranspiration mapping. `★ 4` `no licence`
- [nicolast911/ET_master_project](https://github.com/nicolast911/ET_master_project) - Master Thesis Project on modelling Evapotranspiration with SEBAL. `★ 3` `no licence`
- [sherzodr/agriclimuz](https://github.com/sherzodr/agriclimuz) - Evapotranspiration for the reference crop in Uzbekistan. Based on UN-FAO's Irrigation and Drainage Paper 56 and Penman-Monteith Equation. `★ 3` `MIT`
- [water3d/ca_ssebop_stats](https://github.com/water3d/ca_ssebop_stats) - Code to export and analyze SSEBOP ET data using OpenET-SSEBOP, Earth Engine, and GDAL. `★ 3` `no licence`
- [Alok8321/pyfao56_Model](https://github.com/Alok8321/pyfao56_Model) - This is a repository for Soil Physics with Python Course Semester Project at Oklahoma State University. `★ 2` `no licence`
- [Arman-Ahmadi-1/Exploratory-Data-Analysis-ET](https://github.com/Arman-Ahmadi-1/Exploratory-Data-Analysis-ET) - Code and sample data for the paper "Meteorological driving forces of reference evapotranspiration and their trends in California" (STOTEN, 2022). `★ 2` `MIT`
- [kothawadegs/Crop-Water-Requirement](https://github.com/kothawadegs/Crop-Water-Requirement) - No description provided. `★ 2` `no licence`
- [tommylees112/et_comparison](https://github.com/tommylees112/et_comparison) - Comparison of different evapotranspiration products over East Africa, for submission to a Poster at EGU2019. `★ 2` `no licence`
- [Abohlool/Evapotranspiration_analysis](https://github.com/Abohlool/Evapotranspiration_analysis) - FAO-56 evapotranspiration analysis for a pistachio orchard in Torbat-e Heydarieh, Razavi Khorasan, Iran. Implements the Penman-Monteith method with 10-minute weather data to calculate reference… `★ 1` `MIT`
- [Apavankumar15/evapotranspiration-ssebop-kolhapur](https://github.com/Apavankumar15/evapotranspiration-ssebop-kolhapur) - ET Flux estimation using NDVI-based SSEBop and FAO-56 with ERA5-Land. `★ 1` `no licence`
- [arch-linux-dev/gnangara-et-density-analysis](https://github.com/arch-linux-dev/gnangara-et-density-analysis) - Python and Google Earth Engine workflows for DDR-based evapotranspiration benchmarking, satellite ET comparison, and geospatial ET-density analysis at Gnangara Pines. `★ 1` `MIT`
- [Bego44/irrigation_water_optimization](https://github.com/Bego44/irrigation_water_optimization) - Optimization of the quantity of irrigation water while conserving the crop yield using LP and ML. `★ 1` `Apache-2.0`
- [cantekinkivrak/sebal-et-gee](https://github.com/cantekinkivrak/sebal-et-gee) - SEBAL-style daily ET from Landsat 8/9 + ERA5-Land on Google Earth Engine — applied to Turkish Thrace. `★ 1` `MIT`
- [curtiscrandall/Thesis_Research](https://github.com/curtiscrandall/Thesis_Research) - Scripts related to spatially modeling evapotranspiration. `★ 1` `no licence`
- [erica-mccormick/sfe_et_and_triple_collocation](https://github.com/erica-mccormick/sfe_et_and_triple_collocation) - Code for "Triple collocation validates CONUS-wide ET inferred from atmospheric conditions" (McCormick et al., Minor Revisions). `★ 1` `MIT`
- [JLHM1998/METRIC-Olive-HyperArid-Peru](https://github.com/JLHM1998/METRIC-Olive-HyperArid-Peru) - This repository contains the full code, processing workflow, and auxiliary scripts used in the study “Evapotranspiration Dynamics in a Hyper-Arid Olive Orchard Using METRIC Model (Tacna, Peru)”. `★ 1` `no licence`
- [LSCogill/SatelliteDerived_ET_RSA](https://github.com/LSCogill/SatelliteDerived_ET_RSA) - Evaluating the performance of satellite-derived evapotranspiration products across varying bioclimates in South Africa. `★ 1` `no licence`
- [mahdimohammadnezhad/evapotranspiration](https://github.com/mahdimohammadnezhad/evapotranspiration) - No description provided. `★ 1` `no licence`
- [MonaMaze/Evapotranspiration](https://github.com/MonaMaze/Evapotranspiration) - Calculating the actual crop Evapotranspiration by using high resolution satellite images. `★ 1` `no licence`
- [MTDNRC-WRD/openet](https://github.com/MTDNRC-WRD/openet) - Analysis of modern remote sensing-based ET and comparison with existing DNRC methodology. `★ 1` `no licence`
- [Open-ET/CRAU-Review](https://github.com/Open-ET/CRAU-Review) - No description provided. `★ 1` `no licence`
- [Open-ET/openet-bias-correction-comment-afm](https://github.com/Open-ET/openet-bias-correction-comment-afm) - No description provided. `★ 1` `custom licence`
- [Peteroyanoghafo/irrigation_efficiency_analysis_for_maize_using_python](https://github.com/Peteroyanoghafo/irrigation_efficiency_analysis_for_maize_using_python) - A Python hands-on on Applied NumPy numerical analytics and precision agriculture modeling for daily irrigation and heat stress management. `★ 1` `no licence`
- [RAD-ET/radet-analysis](https://github.com/RAD-ET/radet-analysis) - Analysis scripts and outputs for the RADET model (Radiation Advection Diffusivity-independent Evapotranspiration), a Google Earth Engine-based approach for estimating actual evapotranspiration (ET). `★ 1` `Apache-2.0`
- [SanaCheema123/-SEBAL-Irrigation-Planning-Dashboard-](https://github.com/SanaCheema123/-SEBAL-Irrigation-Planning-Dashboard-) - No description provided. `★ 1` `no licence`
- [thorerismann/aquacrop-deficit-irrig](https://github.com/thorerismann/aquacrop-deficit-irrig) - Aquacrop-OSPY implementation to analyze the effects of changing irrigation schedules and irrigation depths on key crop parameters. `★ 1` `GPL-3.0`
- [trngbich/ReanalysisMeteoRET](https://github.com/trngbich/ReanalysisMeteoRET) - Jupyter notebooks with analyses for paper "Evaluation of reanalysis datasets as meteorological input for estimating reference evapotranspiration over Africa and the Near East". `★ 1` `MIT`
- [vriv06/ETc-research](https://github.com/vriv06/ETc-research) - Agricultural Research carried out with PyFAO56 library by kthorp using evapotranspiration as an irrigation reference. `★ 1` `no licence`
- [8499866092/Internship-work](https://github.com/8499866092/Internship-work) - No description provided. `no licence`
- [A-kinyua/Landsat-evapotranspiration-modelling-](https://github.com/A-kinyua/Landsat-evapotranspiration-modelling-) - using gee, and python Api. `no licence`
- [agrorony/irrigation_proj](https://github.com/agrorony/irrigation_proj) - No description provided. `no licence`
- [aryalbhaskar/Atmospheric_Reference_Evapotranspiration_Kansas](https://github.com/aryalbhaskar/Atmospheric_Reference_Evapotranspiration_Kansas) - No description provided. `no licence`
- [aswin-skk21/physical-ai-irrigation](https://github.com/aswin-skk21/physical-ai-irrigation) - AquaCrop-based irrigation simulations and training pipeline for a physical AI agent. `no licence`
- [Bhuvantejakomera/smart-irrigation-drl](https://github.com/Bhuvantejakomera/smart-irrigation-drl) - Deep Reinforcement Learning (PPO & SAC) benchmark for smart precision irrigation using real FAO-56 dual crop physics. `no licence`
- [brunomartinsmv/eto-methods-comparison](https://github.com/brunomartinsmv/eto-methods-comparison) - Comparative study of empirical and semi-empirical methods for reference evapotranspiration (ETo) estimation in Brazilian tropical climates. Reproducible Python pipeline with analysis of Piracicaba… `MIT`
- [Christina-Pop/irri_resolution_analysis](https://github.com/Christina-Pop/irri_resolution_analysis) - This repository contains the scripts for the analysis of irrigation effects from model simulations at 0.0275! and 0.11° horizontal resolution. The paper with the analysis was submitted to JGR… `no licence`
- [cleeb0703/IAV_ET](https://github.com/cleeb0703/IAV_ET) - The Climatology, SIF Modeled ET, and OpenET modeled ET of 4 Eddy Covariance flux tower sites is compared to EC ET data through plotting and varying statistic metrics, focusing on interannual… `no licence`
- [colediggins/CRONOS_Fao56_adjustment](https://github.com/colediggins/CRONOS_Fao56_adjustment) - This repository is to serve as the submittal of my semester project for the class "Soil Physics Theory" at Oklahoma State University. Over the course of this project I want to take in field soil… `no licence`
- [danghh333/Penman-Monteith-vs-Hargreaves](https://github.com/danghh333/Penman-Monteith-vs-Hargreaves) - No description provided. `no licence`
- [devinsimmons/Senior_Thesis](https://github.com/devinsimmons/Senior_Thesis) - scripts related to my senior thesis project. The goal of this project is to compare evapotranspiration measurements taken at flux towers to evapotranspiration estimates generated by the MOD16… `no licence`
- [dvdjng/CSET_AV_Chile](https://github.com/dvdjng/CSET_AV_Chile) - No description provided. `no licence`
- [elhachimi-ch/ddpg_ocis_paper](https://github.com/elhachimi-ch/ddpg_ocis_paper) - Implementation of DDPG and GA in R3 OCIS. `no licence`
- [elsiver/evapotranspiration_calcs_plots](https://github.com/elsiver/evapotranspiration_calcs_plots) - No description provided. `no licence`
- [eth0-02/mdb-future-climate-iwu](https://github.com/eth0-02/mdb-future-climate-iwu) - No description provided. `no licence`
- [geoaialignment/aquaagent-ospy](https://github.com/geoaialignment/aquaagent-ospy) - Companion code and reproducibility artifacts for AquaAgent-OSPy, an auditable A4-class LLM tool-agent for simulation-grounded irrigation decision support (COMPAG-D-26-04013). `custom licence`
- [goliprajwalitha-cell/PET-using-FAO-Penman-Monteith-equation](https://github.com/goliprajwalitha-cell/PET-using-FAO-Penman-Monteith-equation) - Working with ERA5 monthly reanalysis data. `no licence`
- [Harshabhi6129/IoT-Based-Daily-Evapotranspiration-Estimation-for-Sustainable-Crop-Management](https://github.com/Harshabhi6129/IoT-Based-Daily-Evapotranspiration-Estimation-for-Sustainable-Crop-Management) - No description provided. `no licence`
- [JamalHaddouche/Estimation-de-la-valeur-d-evapotranspiration](https://github.com/JamalHaddouche/Estimation-de-la-valeur-d-evapotranspiration) - No description provided. `no licence`
- [kashingtonDC/CIMIS](https://github.com/kashingtonDC/CIMIS) - CIMIS / SSEBop ET integration. `no licence`
- [Kwakuopokuware401/Estimating_Crop_Evapotranspiration_Uncertainty_with_HRMET](https://github.com/Kwakuopokuware401/Estimating_Crop_Evapotranspiration_Uncertainty_with_HRMET) - Simulating crop evapotranspiration uncertainty by perturbing weather inputs to the HRMET model in Jupyter Notebooks. Focuses on temperature and radiation errors impacting spatial ET estimates via… `no licence`
- [llin-csiss/IrrigationScheduling](https://github.com/llin-csiss/IrrigationScheduling) - No description provided. `no licence`
- [lorenafc/cwp_project](https://github.com/lorenafc/cwp_project) - Internship project - crop water productivity. `no licence`
- [LucasMajor/turfgrass-irrigation-scheduling-project](https://github.com/LucasMajor/turfgrass-irrigation-scheduling-project) - No description provided. `no licence`
- [montimaj/iwv-bcm-et-eval](https://github.com/montimaj/iwv-bcm-et-eval) - Actual ET assessments over the Indian Wells Valley, CA in the Great Basin. `MIT`
- [mph21/CCDC-and-SSEBop-Integration](https://github.com/mph21/CCDC-and-SSEBop-Integration) - No description provided. `no licence`
- [okkevaneck/ai_based_irrigation](https://github.com/okkevaneck/ai_based_irrigation) - No description provided. `GPL-3.0`
- [peterphamsd/urban-ag-optimizer](https://github.com/peterphamsd/urban-ag-optimizer) - Probabilistic urban agriculture site optimizer using FAO-56 Penman-Monteith evapotranspiration modeling and Monte Carlo simulation. `MIT`
- [rafiachmadfr/Evapotranspiration-Analysis](https://github.com/rafiachmadfr/Evapotranspiration-Analysis) - SKRIPSI - Evaluasi Metode Blaney-criddle, Hargreaves-samani, dan Penman-monteith Dalam Menentukan Evapotranspirasi Tanaman Alpukat. `no licence`
- [RamiALBASHA/energy_balance_model_paper](https://github.com/RamiALBASHA/energy_balance_model_paper) - Project of the paper that describes the energy balance model. `no licence`
- [Reenastha/Evapotranspiration](https://github.com/Reenastha/Evapotranspiration) - No description provided. `no licence`
- [ren-de-leon/Comparison-of-Evapotranspiration-Estimates](https://github.com/ren-de-leon/Comparison-of-Evapotranspiration-Estimates) - Comparison of Evapotranspiration Estimate using the Eddy Covariance Method and some Selected Empirical Models. `no licence`
- [robduos/Master_Thesis_RA](https://github.com/robduos/Master_Thesis_RA) - Supplementary material to the Master Thesis. `no licence`
- [sarahclaude/PET](https://github.com/sarahclaude/PET) - Workflow to calculate potential evapotranspiration. `no licence`
- [shDavlatbek/Andijon](https://github.com/shDavlatbek/Andijon) - No description provided. `no licence`
- [shimmer-cx/Irrigation-Decision-System-2.0](https://github.com/shimmer-cx/Irrigation-Decision-System-2.0) - 灌溉决策系统2.0 - Built with Anvil. `no licence`
- [SmartAG-Team/agri_water_management](https://github.com/SmartAG-Team/agri_water_management) - Self-contained reproduction of wheat–maize irrigation allocation and regional water-use scenarios in the North China Plain. `no licence`
- [Sora-at/Evapotranspiration](https://github.com/Sora-at/Evapotranspiration) - No description provided. `no licence`
- [textbookRP/ETStuff](https://github.com/textbookRP/ETStuff) - Project for looking at agrivoltaics and evapotranspiration. `no licence`
- [tpokoski/refet-mesonet](https://github.com/tpokoski/refet-mesonet) - Comparing the reference ET provided by a Mesonet system to a reference ET calculation from pyfao56. `no licence`
- [vilcagamarracf/prueba-jupyterbook](https://github.com/vilcagamarracf/prueba-jupyterbook) - No description provided. `no licence`
- [yjx90620/irrigation-decision](https://github.com/yjx90620/irrigation-decision) - No description provided. `no licence`
- [zinebkarim/Evapotranspiration](https://github.com/zinebkarim/Evapotranspiration) - No description provided. `no licence`

<a id="evapotranspiration-r"></a>

#### R

- [mikejohnson51/ET](https://github.com/mikejohnson51/ET) - Code for mapping, modeling, and validating evapotranspiration data across spatial and temporal scales. `★ 9` `MIT`
- [environmentalinformatics-marburg/paper_kilimanjaro_areawide_et](https://github.com/environmentalinformatics-marburg/paper_kilimanjaro_areawide_et) - Generate remote sensing-based area-wide datasets of evapotranspiration (ET) and validate against in situ Scintillometer estimates. `★ 4` `no licence`
- [tbiggsgithub/SEBAL_ET_CA](https://github.com/tbiggsgithub/SEBAL_ET_CA) - Rfiles and manuscript for CA central valley SEBAL cf MOD16. `★ 4` `no licence`
- [amyoung01/phenology_evapotranspiration_analysis](https://github.com/amyoung01/phenology_evapotranspiration_analysis) - Collection of scripts to run analysis evaluating importance of phenology as a control of ET. Findings published in JGR: Biogeosciences 2022. `★ 3` `no licence`
- [arnaldpuy/irrigation_efficiency](https://github.com/arnaldpuy/irrigation_efficiency) - No description provided. `★ 1` `no licence`
- [Yonaba/ET0_Analysis_Burkina_Faso](https://github.com/Yonaba/ET0_Analysis_Burkina_Faso) - R scripts for Figures and Data Analysis Accompanying an academic paper on reference evapotranspiration analysis in Burkina Faso. `★ 1` `CC0-1.0`
- [drmerlot/evapotranspiration](https://github.com/drmerlot/evapotranspiration) - Calculate and compare various evapotranspiration methods with the Evapotraspiration package. `no licence`
- [emdigman/ETOscript](https://github.com/emdigman/ETOscript) - Upload of (rough) script for calculating district-level evapotranspiration and crop water demand using FAO-PM method. `no licence`
- [flaviobastoscampos/ET_dynamics_and_partitioning_vineyard](https://github.com/flaviobastoscampos/ET_dynamics_and_partitioning_vineyard) - code source for the figures of the work "Evapotranspiration dynamics and partitioning in a grassed vineyard: ecophysiological and computational modelling approaches". `no licence`
- [hamdiibtissem688-star/Crop-water-requirment](https://github.com/hamdiibtissem688-star/Crop-water-requirment) - No description provided. `no licence`
- [jessicaguo/evapotranspiration](https://github.com/jessicaguo/evapotranspiration) - No description provided. `no licence`
- [khairaniai/Meteorology-for-Evapotranspiration](https://github.com/khairaniai/Meteorology-for-Evapotranspiration) - No description provided. `no licence`
- [mrani307/Reference_Evapotranspiration_Contribution_Assessment](https://github.com/mrani307/Reference_Evapotranspiration_Contribution_Assessment) - No description provided. `no licence`
- [taj771/AqaCrop-OSpy](https://github.com/taj771/AqaCrop-OSpy) - Economic value of irrigation water and climate change impacts (working). `no licence`

<a id="evapotranspiration-other"></a>

#### Other

- [Haseeb-oss-eng/ET_GEE_SSEBop](https://github.com/Haseeb-oss-eng/ET_GEE_SSEBop) - This is GEE Javascript coded Estimation of ET. `★ 1` `MIT`
- [WSWUP/dri-owrd-et](https://github.com/WSWUP/dri-owrd-et) - OWRD-DRI Statewide ET Project: Field- and HUC-level geopackage development workflow. `★ 1` `Apache-2.0`
- [DelaTheAnalyst/Analysis-of-Evapotranspiration-formulas](https://github.com/DelaTheAnalyst/Analysis-of-Evapotranspiration-formulas) - Using variables gathered at the CSIR Weather Station in Accra, this project compares various evapotranspiration formulas to the standardized Evo transpiration formula (Penman Monteith). `no licence`
- [DJagad/Cal-SIMETAW-Data-Science-15-Year-Crop-Evapotranspiration-Analysis](https://github.com/DJagad/Cal-SIMETAW-Data-Science-15-Year-Crop-Evapotranspiration-Analysis) - Data Analysis and Data Visualization on the Cal-SIMETAW Dataset. `no licence`
- [Engr-MuradAli/SEBAL-GEE-Wheat-ETa](https://github.com/Engr-MuradAli/SEBAL-GEE-Wheat-ETa) - Google Earth Engine implementation of SEBAL for field-scale ETa and WEF Nexus assessment in Swabi District, Pakistan. `no licence`
- [fernandoputti/Paper_Irriga_ETo_Minas_Gerais](https://github.com/fernandoputti/Paper_Irriga_ETo_Minas_Gerais) - Title: REFERENCE EVAPOTRANSPIRATION THROUGHOUT THE STATE OF MINAS GERAIS AS A GUIDE FOR REGIONALIZED IRRIGATION MANAGEMENT Abstract: Minas Gerais is the third Brazilian state with the largest… `CC0-1.0`
- [hirunigunawardena8-ui/Eppawala-ET-Thesis-Code](https://github.com/hirunigunawardena8-ui/Eppawala-ET-Thesis-Code) - "GEE scripts for SEBAL-based ET estimation, Random Forest classification, and Mann-Kendall trend analysis — Eppawala Phosphate Mine thesis. `no licence`
- [Prince-walker/Evapotranspiration](https://github.com/Prince-walker/Evapotranspiration) - Project "Comparison Of Evapotranspiration using the Eddy Covariance Method and Some Selected Empirical Models. `GPL-3.0`
- [samlimaico/Crop-Water-Productivity-Thesis](https://github.com/samlimaico/Crop-Water-Productivity-Thesis) - The script downloads WaPOR data (AETI, NPP), Aggregate dekadal → seasonal Apply crop masks, Compute yield and CWP. `no licence`
- [wederniichrak013-creator/TFM-DigitalTwin-Pistachio-ET](https://github.com/wederniichrak013-creator/TFM-DigitalTwin-Pistachio-ET) - Python scripts for evapotranspiration estimation using TSEB-PT and 3SEB-PT models in a pistachio orchard. `no licence`

<a id="weather"></a>

### Weather and agroclimate

<a id="weather-python"></a>

#### Python

- [takyurp09/edd-bias-adjustment-europe](https://github.com/takyurp09/edd-bias-adjustment-europe) - Code and analysis for evaluating bias-adjusted CMIP6 climate data for agricultural extreme heat metrics across Europe (1994-2014). `MIT`
- [VICTORSIG1985/agroclimatic-risk-imbabura](https://github.com/VICTORSIG1985/agroclimatic-risk-imbabura) - Reproducible pipeline for parish-level agroclimatic risk assessment of Andean crops under CMIP6 scenarios in Imbabura, Ecuador. Random Forest + Bayesian Networks + IPCC AR6 framework. `MIT`

<a id="weather-r"></a>

#### R

- [agroecosystemsmodelingwsu/AgClimateAnalog](https://github.com/agroecosystemsmodelingwsu/AgClimateAnalog) - No description provided. `no licence`
- [pierre-ed-ds/Herault_Aggroclimatic_Classification_Mapping](https://github.com/pierre-ed-ds/Herault_Aggroclimatic_Classification_Mapping) - Agroclimatic Units of Hérault: Spatial Analysis and Interactive Mapping. `MIT`
- [sospicy77/Impact-oriented-evaluation-of-WG](https://github.com/sospicy77/Impact-oriented-evaluation-of-WG) - Data and analysis results for the "Impact-oriented evaluation of stochastic weather generators for rice blast risk modeling: implications for agricultural climate services". `no licence`
- [vitibois/TerraClimate-Agroclim](https://github.com/vitibois/TerraClimate-Agroclim) - Global agroclimatic indices for viticulture from TerraClimate data. `MIT`

<a id="pests-diseases"></a>

### Pests, diseases and weeds

<a id="pests-diseases-r"></a>

#### R

- [da94829/aflatoxin_dssat_model](https://github.com/da94829/aflatoxin_dssat_model) - No description provided. `no licence`

<a id="hydrology"></a>

### Hydrology, erosion and watersheds

<a id="hydrology-batchfile"></a>

#### Batchfile

- [zml0120/Shaxi-SWAT-Model](https://github.com/zml0120/Shaxi-SWAT-Model) - Software and Data of ”The spatial variations of water cycle components based on the simulation of SWAT model with dual-component calibration“. `no licence`

<a id="hydrology-forth"></a>

#### Forth

- [biopsichas/Zglowiaczka](https://github.com/biopsichas/Zglowiaczka) - Zglowiaczka SWAT+ model for the OPTAIN project. `no licence`

<a id="hydrology-fortran"></a>

#### Fortran

- [go-bananas-wwj/hongxin_swat_plus](https://github.com/go-bananas-wwj/hongxin_swat_plus) - 红心村流域建模. `no licence`
- [icra/traca](https://github.com/icra/traca) - Projecte Q-SWAT+TRAÇA. `no licence`

<a id="hydrology-java"></a>

#### Java

- [egetahun/DecisionModel](https://github.com/egetahun/DecisionModel) - Decision support models to evaluate water quality impacts of best management practices. `no licence`

<a id="hydrology-javascript"></a>

#### JavaScript

- [japhethkimeu/soil_loss_assessment](https://github.com/japhethkimeu/soil_loss_assessment) - Implementation of RUSLE method in GEE. `★ 12` `no licence`
- [taha328/Soil_Erosion_Google_Earth_Engine_V2.0](https://github.com/taha328/Soil_Erosion_Google_Earth_Engine_V2.0) - This GEE script performs a complete RUSLE soil erosion analysis, including final calculation, classification, visualization, and statistics. It builds upon and completes the work of a previous… `★ 3` `no licence`
- [santiagotironi-tech/Modelo-RUSLE-con-imagenes-satelitales-](https://github.com/santiagotironi-tech/Modelo-RUSLE-con-imagenes-satelitales-) - Modelo RUSLE con imagenes satelitales. `★ 2` `no licence`
- [sohan-khan31/RUSLE-SDR-based-Sediment-Yield-Estimation-in-GEE](https://github.com/sohan-khan31/RUSLE-SDR-based-Sediment-Yield-Estimation-in-GEE) - Google Earth Engine (GEE) code for assessing sediment yield in the lower Teesta River Basin of Bangladesh. `★ 1` `no licence`
- [alrahaman/Soil-Erosion-Prediction-using-RUSLE-in-Google-Earth-Engine](https://github.com/alrahaman/Soil-Erosion-Prediction-using-RUSLE-in-Google-Earth-Engine) - The RUSLE (Revised Universal Soil Loss Equation) model in Google Earth Engine integrates rainfall erosivity (R), soil erodibility (K), slope length/steepness (LS), cover-management (C), and support… `no licence`
- [AMANKANOJIYA/RUSLE-MODEL-Kutch](https://github.com/AMANKANOJIYA/RUSLE-MODEL-Kutch) - No description provided. `no licence`
- [isidoravidal-prieto/guatemala-erosion-rusle](https://github.com/isidoravidal-prieto/guatemala-erosion-rusle) - No description provided. `no licence`
- [Jaival1/Estimation-of-Soil-Erosion-using-RUSLE-in-Dhanera-Gujarat](https://github.com/Jaival1/Estimation-of-Soil-Erosion-using-RUSLE-in-Dhanera-Gujarat) - No description provided. `no licence`
- [Niyogsubizo-Jean-De-Dieu/rusle-rwanda-gee](https://github.com/Niyogsubizo-Jean-De-Dieu/rusle-rwanda-gee) - No description provided. `no licence`
- [nouredinekel/Soil-Erosion-RF-RUSLE](https://github.com/nouredinekel/Soil-Erosion-RF-RUSLE) - Soil erosion modeling using RUSLE and Random Forest. `no licence`
- [SmallYie/RUSLE-NDVI-C-Robustness-Minsk](https://github.com/SmallYie/RUSLE-NDVI-C-Robustness-Minsk) - RUSLE-C-Parameterisation-Robustness. `no licence`
- [Suman1801/soil-erosion-RUSLE-GEE](https://github.com/Suman1801/soil-erosion-RUSLE-GEE) - GEE script for estimating soil loss using RUSLE model. `MIT`

<a id="hydrology-matlab"></a>

#### MATLAB

- [steveforczyk/USRainFall-Code](https://github.com/steveforczyk/USRainFall-Code) - This repo is intended to hold files for reading US Rain Fall data and applying the RUSLE Erosion algorithm to that data. `BSD-3-Clause`
- [YettimXie/Spatiotemporal-evolution-of-cropland-related-soil-erosion-in-China-over-the-past-four-decades](https://github.com/YettimXie/Spatiotemporal-evolution-of-cropland-related-soil-erosion-in-China-over-the-past-four-decades) - This study applied high-resolution remote sensing datasets to investigate the spatially-explicit dynamics of crop-specific soil erosion in China from 1980 to 2018 at a 30 m resolution based on the… `no licence`

<a id="hydrology-netlogo"></a>

#### NetLogo

- [baskargroup/INFEWS-MSA](https://github.com/baskargroup/INFEWS-MSA) - No description provided. `MIT`

<a id="hydrology-python"></a>

#### Python

- [VUB-HYDR/2019_Chawanda_etal_EMS](https://github.com/VUB-HYDR/2019_Chawanda_etal_EMS) - Scripts used to process data and namelist used in Chawanda et al. (2019). `★ 4` `MIT`
- [pnnl-sbrsfa/SWAT_Modeling_PR_Watershed](https://github.com/pnnl-sbrsfa/SWAT_Modeling_PR_Watershed) - Hydrological Modeling and Water Quality. `★ 3` `no licence` `archived`
- [DoaaHegazy/hydrological-drought-forcating-in-the-Nile-basin](https://github.com/DoaaHegazy/hydrological-drought-forcating-in-the-Nile-basin) - Reproducible notebooks for Nile Basin drought propagation, CMIP6 model selection, SWAT+ simulations, SRI-12, and drought return-period analysis. `★ 2` `MIT`
- [PSUmodeling/PIHM-Simulations](https://github.com/PSUmodeling/PIHM-Simulations) - No description provided. `★ 2` `no licence`
- [taha328/Tangier-Soil-Erosion-RUSLE-Model-](https://github.com/taha328/Tangier-Soil-Erosion-RUSLE-Model-) - Soil erosion risk assessment in Tangier using the RUSLE model. `★ 2` `no licence`
- [VUB-HYDR/2021_Nkwasa_etal_HESS](https://github.com/VUB-HYDR/2021_Nkwasa_etal_HESS) - Scripts used to incorporate global phenology datasets into regional-global SWAT+ models. `★ 2` `MIT`
- [wanderam/codigos-modelagem-hidro](https://github.com/wanderam/codigos-modelagem-hidro) - Códigos escritos (Jupyter notebooks) para processar e analisar dados da modelagem hidrológica realizada com os modelos hidrológicos SWAT e SWAT-MODFLOW. Este é um projeto de uma tese desenvolvida na… `★ 2` `no licence`
- [Yilkalg3/RUSLE](https://github.com/Yilkalg3/RUSLE) - A framework to estimate soil loss amounts in the headwaters of Upper Blue Nile (Abbay) Basin using Google Earth Engine Python API. `★ 2` `no licence`
- [cshuler/Tutuila-SWB-Scenarios](https://github.com/cshuler/Tutuila-SWB-Scenarios) - Application of the Soil Water Balance 2 Water Budget Model with participatory land cover and future climate scenarios, Tutuila American Samoa. `★ 1` `no licence`
- [danielbabin/Zambezi_RUSLE](https://github.com/danielbabin/Zambezi_RUSLE) - Using a suite of satellite data to calculate models for erosion in the Zambezi RIver Basin. `★ 1` `no licence`
- [Hai-mian-33/WEC-Risk-Platform](https://github.com/Hai-mian-33/WEC-Risk-Platform) - Integrated SWAT-based water environmental capacity & two-class pollution-risk desktop tool. `★ 1` `MIT`
- [HimanshuSingh39/SWAT-LSTM-Coupling-for-Mahanadi-Basin](https://github.com/HimanshuSingh39/SWAT-LSTM-Coupling-for-Mahanadi-Basin) - This repository contains code, data structure, and results for coupling the SWAT hydrological model with an LSTM neural network to improve daily streamflow simulation in the Mahanadi River Basin… `★ 1` `no licence`
- [LEE-Gen-Chen/RUSLE](https://github.com/LEE-Gen-Chen/RUSLE) - Scripts for RUSLE Raw Data Retrieval via GEE and Processing with Python. `★ 1` `no licence`
- [majidabd24/RUSLE-soil-loss-GEE](https://github.com/majidabd24/RUSLE-soil-loss-GEE) - A project for estimating soil loss using the RUSLE model in Google Earth Engine. `★ 1` `no licence`
- [MarlenaRosaBarille/Python-Code-BachelorThesis_barille](https://github.com/MarlenaRosaBarille/Python-Code-BachelorThesis_barille) - Google Earth Engine implementation of the Revised Universal Soil Loss Equation (RUSLE) for national-scale soil erosion modelling in Madagascar, with a comparative analysis of three LS-factor… `★ 1` `no licence`
- [mit2880/Soil-loss-equation-RUSLE-](https://github.com/mit2880/Soil-loss-equation-RUSLE-) - No description provided. `★ 1` `no licence`
- [Satwik-1234/RUSLE_Western-Maharashtra_V1](https://github.com/Satwik-1234/RUSLE_Western-Maharashtra_V1) - No description provided. `★ 1` `custom licence`
- [alzaber-moulick/RUSLE-InVEST-Environmental-Modeling](https://github.com/alzaber-moulick/RUSLE-InVEST-Environmental-Modeling) - Python workflows, spatial scripts, and environmental degradation modeling using RUSLE and InVEST frameworks in Miniconda. `MIT`
- [angrinochirandiegofernando-bot/rusle-amaime](https://github.com/angrinochirandiegofernando-bot/rusle-amaime) - Modelo USLE/RUSLE de erodabilidad y pérdidas de suelo — cuenca del río Amaime. `no licence`
- [asco2004-bot/SWAT-AquaCrop-Optimization](https://github.com/asco2004-bot/SWAT-AquaCrop-Optimization) - Python implementation of a SWAT–AquaCrop multi-objective optimization framework for irrigation allocation. `MIT`
- [baiyuekuidedagongzai/TLSTM-for-post-processing](https://github.com/baiyuekuidedagongzai/TLSTM-for-post-processing) - Post-processing of SWAT model–derived physical variables to enhance simulation accuracy.The Excel file serves as a demonstration of how to format and process the physical variables extracted from… `no licence`
- [BijayRaj810/streamflow-uncertainty-climate-landuse](https://github.com/BijayRaj810/streamflow-uncertainty-climate-landuse) - Quantifying streamflow uncertainty under climate and land-use change using bias-corrected GCM projections and SWAT+ hydrological modeling, with source attribution across climate models, emissions… `no licence`
- [bvorak/swat_pipeline](https://github.com/bvorak/swat_pipeline) - A pipeline for running the SWAT models needed for a watershed pollution attribution research project: modular input data transforms, Monte Carlo orchestration, dashboard analysis and extensive… `no licence`
- [cez198244/Soil-Loss-India](https://github.com/cez198244/Soil-Loss-India) - Annual Soil Loss (t/ha/yr) has been estimated using RUSLE factor in India. `no licence`
- [cshuler/Maui_SWAT_code](https://github.com/cshuler/Maui_SWAT_code) - Code base for Maui PacRISA SWAT models. `no licence`
- [dmmf1g15/RUSLE](https://github.com/dmmf1g15/RUSLE) - Soil erosion modelling in portugal. `no licence`
- [duyns0302/erosionrisk-base-on-RUSLE](https://github.com/duyns0302/erosionrisk-base-on-RUSLE) - No description provided. `no licence`
- [egpark-knu/hwaseong-map-dependence-swatplus](https://github.com/egpark-knu/hwaseong-map-dependence-swatplus) - Supporting data, figures, and code for the Hwaseong SWAT+ map-dependence manuscript (v18 submission). `custom licence`
- [egpark-knu/lulc-aef-swatplus](https://github.com/egpark-knu/lulc-aef-swatplus) - Code for: From Satellite Embeddings to Catchment Hydrology: Spatial-Support Matching and Source-Gauge Observability in Two Korean Urban Watersheds (Jin et al., JHRS). `custom licence`
- [Elias183/Integrated-Climate-Water-Allocation-Decision-Support-Framework-ICWADSF-](https://github.com/Elias183/Integrated-Climate-Water-Allocation-Decision-Support-Framework-ICWADSF-) - Develop a Python-based water allocation model in Google Colab that integrates SWAT+ outputs with socio-economic data. The model will calculate sectoral water demands, allocate water based on defined… `GPL-3.0`
- [elitohidi42-lgtm/web-based-watershed-management](https://github.com/elitohidi42-lgtm/web-based-watershed-management) - Development of a Web-Based Framework Integrating an Agent-Based Model with a Hydrological–Agricultural Model for Watershed Management. `no licence`
- [emmaaagolub/ABM_SWAT_Upsang_Coupling](https://github.com/emmaaagolub/ABM_SWAT_Upsang_Coupling) - This repository contains an adjusted ABM model, calibrated SWAT model, miscanthus adoption scripts, and other processing files. `no licence`
- [gabriel-bohnke/SmapDownloadAndCompareWithSwatPlus](https://github.com/gabriel-bohnke/SmapDownloadAndCompareWithSwatPlus) - Download of SMAP rasters and compare with SWAT+ model output. `no licence`
- [GerhardtB/UNDP-SADC](https://github.com/GerhardtB/UNDP-SADC) - Agricultural and hydrological modelling for watershed restoration in SADC countries. `no licence`
- [HaqqanUddin/SWATPlus](https://github.com/HaqqanUddin/SWATPlus) - No description provided. `no licence`
- [jeevitha17234/rusle-geoai-copilot](https://github.com/jeevitha17234/rusle-geoai-copilot) - RUSLE soil erosion risk mapping in GEE (CHIRPS, SRTM, Sentinel-2, MODIS, OpenLandMap) + a GeoAI copilot (Llama 3.1 + LangChain, FastAPI/Streamlit) for natural-language querying of results. `no licence`
- [jonatanmoreno777/GIS](https://github.com/jonatanmoreno777/GIS) - Blue and green water flows in the SWAT semi-distributed hydrological model in a river basin. `no licence`
- [jopator/SWATPlusForCRIDA](https://github.com/jopator/SWATPlusForCRIDA) - Scripts used to perform climate scenarios using Climate data from CORDEX and SWAT+ for implementation of CRIDA Framework. `MIT`
- [joy-bhattacharjee/Climate-Change-Impact-Analysis-Subirrigation-Water-Balance-Components](https://github.com/joy-bhattacharjee/Climate-Change-Impact-Analysis-Subirrigation-Water-Balance-Components) - No description provided. `no licence`
- [landevaluation4sde/RUSLE](https://github.com/landevaluation4sde/RUSLE) - No description provided. `no licence`
- [ngninhhai-cmd/rusle-uncertainty-gialai](https://github.com/ngninhhai-cmd/rusle-uncertainty-gialai) - Reproducible Python package for RUSLE uncertainty analysis in Gia Lai, Vietnam. `MIT`
- [NidhiGusai/Soil-erosion-estimation](https://github.com/NidhiGusai/Soil-erosion-estimation) - To estimate potential zones of soil erosion in Kheda district of Gujarat using RUSLE model equation. `no licence`
- [nshahi60/Modelling-water-quality-using-APEX-for-Vinkenloop-catchment-Netherlands](https://github.com/nshahi60/Modelling-water-quality-using-APEX-for-Vinkenloop-catchment-Netherlands) - No description provided. `no licence`
- [oybcst/watershed-simulated-vs-observed](https://github.com/oybcst/watershed-simulated-vs-observed) - Watershed modeling in the Mobile River Basin. `MIT`
- [paulinelemenkova/amanos-erosion-rusle-xai](https://github.com/paulinelemenkova/amanos-erosion-rusle-xai) - RUSLE + explainable ML for soil erosion in the Amanos (Nur) Mountains, Türkiye. `custom licence`
- [plateroD/Metamorphic-Differential-Testing-for-Landlab-and-Watem-Sedem-for-Indian-Creek](https://github.com/plateroD/Metamorphic-Differential-Testing-for-Landlab-and-Watem-Sedem-for-Indian-Creek) - Replication code and test harnesses for metamorphic and differential testing of WaTEM/SEDEM, Landlab, GeoWEPP, and U-Net erosion workflows for the Indian Creek watershed. `no licence`
- [robotayyyyy/waterBalanceScript](https://github.com/robotayyyyy/waterBalanceScript) - No description provided. `no licence`
- [Saryace/rusle-ren237](https://github.com/Saryace/rusle-ren237) - Google Colab para desarrollar un modelo RUSLE simple. `no licence`
- [Satwik-1234/RUSLE_Western-Maharashtra](https://github.com/Satwik-1234/RUSLE_Western-Maharashtra) - No description provided. `custom licence`
- [siremey/RUSLE_Assessment](https://github.com/siremey/RUSLE_Assessment) - Code for estimating RUSLE soil erosion susceptibility for my study site. `MIT`
- [sticks0220/rusle-c-factor](https://github.com/sticks0220/rusle-c-factor) - RUSLE_c_factor. `no licence`
- [SWATGenX/SWATGenX-reproducibility](https://github.com/SWATGenX/SWATGenX-reproducibility) - Reproducibility package for the SWATGenX platform paper — scripts, configs & benchmark models to regenerate every figure and result. `no licence`
- [UH-WRRC-SWB-model/SWB2-Tutuila](https://github.com/UH-WRRC-SWB-model/SWB2-Tutuila) - Tutuila water budget model. `GPL-3.0`
- [VUB-HYDR/2024_Nkwasa_et_al](https://github.com/VUB-HYDR/2024_Nkwasa_et_al) - Contains scripts used in processing files of the global water quality model (CoSWAT-WQ v1.0). `MIT`
- [whq552800/crop_double_water_stress](https://github.com/whq552800/crop_double_water_stress) - this issue contains code for analysis and draw. `no licence`
- [yangjiab/Irri_groundwater_HRB](https://github.com/yangjiab/Irri_groundwater_HRB) - No description provided. `no licence`

<a id="hydrology-r"></a>

#### R

- [kika1002/RCP](https://github.com/kika1002/RCP) - Preparing data to run RCP8.5 as future scenario for SWAT model. `★ 3` `no licence`
- [AstroMac26/RUSLE-Bromont](https://github.com/AstroMac26/RUSLE-Bromont) - The provided Git repository hosts R scripts dedicated to implementing the Revised Universal Soil Loss Equation (RUSLE) erosion model on a watershed in Québec. These scripts are crafted to analyze… `★ 2` `no licence`
- [EtheridgeLab/Tar_Pam_SWAT](https://github.com/EtheridgeLab/Tar_Pam_SWAT) - SWAT+ Model for the Tar-Pamlico River Basin. `★ 2` `no licence`
- [ryali93/SedimentYield](https://github.com/ryali93/SedimentYield) - Espacialización de los sedimentos en la cuenca del río Jequtepeque a partir de la erosión de suelo calculada por RUSLE y el coeficiente de aporte de sedimentos (SDR). `★ 2` `no licence`
- [alejandrosgz/HSJ_SA_SC_SWATPlus](https://github.com/alejandrosgz/HSJ_SA_SC_SWATPlus) - This repository contains data related to the manuscript Using sensitivity analysis and soft calibration of geological regions to improve the representation of hydrological processes in a SWAT+ model. `★ 1` `MIT`
- [AndreaKaim/Biophysical-optimization-and-economic-preferences-supplemental-material](https://github.com/AndreaKaim/Biophysical-optimization-and-economic-preferences-supplemental-material) - Code and exemplarly input data for the SWAT agronomy model (social value of agricultural production) and the Bird Habitat model (social value of biodiversity) as used in Kaim et al.: "Combining… `★ 1` `GPL-3.0`
- [danielbuhr/REMM_SWATplus_SensitivityAnalysis](https://github.com/danielbuhr/REMM_SWATplus_SensitivityAnalysis) - No description provided. `★ 1` `MIT`
- [EtheridgeLab/Cape_Fear_SWAT](https://github.com/EtheridgeLab/Cape_Fear_SWAT) - SWAT+ Model for the Cape Fear River Basin in North Carolina. `★ 1` `no licence`
- [sheilasaia/paper-yadkin-swat-study](https://github.com/sheilasaia/paper-yadkin-swat-study) - Data repository for paper titled: "Assessment of Hydrologic Vulnerability to Urbanization and Climate Change in a Rapidly Changing Watershed in the Southeast U.S.". `★ 1` `no licence`
- [arnaldpuy/uncertainy_irrigation_modelling](https://github.com/arnaldpuy/uncertainy_irrigation_modelling) - No description provided. `no licence`
- [arnanaraza/AbuanSWAT](https://github.com/arnanaraza/AbuanSWAT) - No description provided. `no licence`
- [arsalvacion/prob-rusle-marinduque](https://github.com/arsalvacion/prob-rusle-marinduque) - No description provided. `no licence`
- [AugustoSouto/Integrated_Modelling](https://github.com/AugustoSouto/Integrated_Modelling) - Integrated Biophysical and Economic Models using the Soil and Water Assessment Model (SWAT). `no licence`
- [biopsichas/full_workflow_cs6](https://github.com/biopsichas/full_workflow_cs6) - No description provided. `no licence`
- [biopsichas/PLSWAT](https://github.com/biopsichas/PLSWAT) - No description provided. `no licence`
- [JoanaEichenberger/Impact-of-Soil-Data-Representation-on-Streamflow-Modeling-with-COCOA-SWAT-Workflow](https://github.com/JoanaEichenberger/Impact-of-Soil-Data-Representation-on-Streamflow-Modeling-with-COCOA-SWAT-Workflow) - The R scripts used to assess soil texture before and after dominant soil aggregation, conduct the sensitivity analysis, calibrate and evaluate the models, and generate the figures and tables. `MIT`
- [kevin-wallington/Instream_LegacyP](https://github.com/kevin-wallington/Instream_LegacyP) - Code and SWAT model input files for paper. `MIT`
- [kmendoza24/IndigoAg_CaseStudy_SWAT](https://github.com/kmendoza24/IndigoAg_CaseStudy_SWAT) - SWAT model and code used for interview case study. `no licence`
- [LifengYuan111/Two-Stage-SWAT-SVR-](https://github.com/LifengYuan111/Two-Stage-SWAT-SVR-) - SWAT+–SVR hybrid streamflow modeling framework for the Roubidoux Creek Watershed, integrating physically based SWAT+ simulations with machine-learning correction models at both monthly and daily… `no licence`
- [lm-costa/swat_ex](https://github.com/lm-costa/swat_ex) - No description provided. `MIT`
- [merijn-smits/Thesis-SWAT-Chilobwe](https://github.com/merijn-smits/Thesis-SWAT-Chilobwe) - No description provided. `no licence`
- [merijn-smits/Thesis-SWAT-Likangala](https://github.com/merijn-smits/Thesis-SWAT-Likangala) - R-code to run SWAT+ for the Likangala catchment and create graphs. `no licence`
- [microbial-genomics/wu_redcedar2](https://github.com/microbial-genomics/wu_redcedar2) - No description provided. `no licence`
- [river-corridors-sfa/rc_sfa-rc-3-wenas-modeling](https://github.com/river-corridors-sfa/rc_sfa-rc-3-wenas-modeling) - Repository for manuscript and analysis of SWAT numerical model output. `MIT`
- [Rojakaveh/CEAP-ARS-watersheds](https://github.com/Rojakaveh/CEAP-ARS-watersheds) - No description provided. `no licence`
- [sheilasaia/paper-yadkin-swat-svi-study](https://github.com/sheilasaia/paper-yadkin-swat-svi-study) - Data repository for paper titled: "Applying Climate Change Risk Management Tools to Combine Streamflow Projections and Social Vulnerability". `no licence`
- [shubhamjain15/HAWQS-SWAT-LSTM](https://github.com/shubhamjain15/HAWQS-SWAT-LSTM) - Process HAWQS data as inputs to Entity Aware LSTM models and calibrating SWAT models. `no licence`
- [waternk/UMRBSWAT](https://github.com/waternk/UMRBSWAT) - Script relating to processing input and output of SWAT model. `no licence`

<a id="hydrology-scala"></a>

#### Scala

- [martinzbinden/ch.eros](https://github.com/martinzbinden/ch.eros) - erosion risk simulation with RUSLE for Switzerland. `no licence`

<a id="hydrology-smarty"></a>

#### Smarty

- [jmrodriguez19/SWAT-gwflow-PEST-setup](https://github.com/jmrodriguez19/SWAT-gwflow-PEST-setup) - SWAT+gwflow model repository configured with PEST++ for the headwaters of the Tagus River basin. It contains inputs, observations, executables, and model data, while avoiding large output files. `no licence`

<a id="hydrology-visual-basic"></a>

#### Visual Basic

- [madeleineholland/MarthasVineyardSWB](https://github.com/madeleineholland/MarthasVineyardSWB) - Soil Water Balance model for Martha's Vineyard. `no licence`

<a id="hydrology-other"></a>

#### Other

- [asadisara/CoupledSWATLSTM](https://github.com/asadisara/CoupledSWATLSTM) - SWAT+ model outputs used as input for LSTM model to improve streamflow estimation through coupled modeling. `★ 6` `no licence`
- [ankushv18/Runoff-RUSLE](https://github.com/ankushv18/Runoff-RUSLE) - Rainfall runoff based soil erosion modeling for GEE environment. `★ 1` `no licence`
- [FahryDjuraini/Future-Soil-Erosion-CMIP6](https://github.com/FahryDjuraini/Future-Soil-Erosion-CMIP6) - This repository provides a complete and reproducible workflow for assessing soil erosion dynamics under climate change scenarios in a tropical watershed. The framework integrates Regional Climate… `★ 1` `no licence`
- [anashadri/Drainage_ZH](https://github.com/anashadri/Drainage_ZH) - sensitivity analysis of the tool used to assess the surface area impacted by agricultural drainage for the protection of wetlands. `MIT`
- [anastasiachuburina/soil-erosion-rusle](https://github.com/anastasiachuburina/soil-erosion-rusle) - GIS-based modeling of potential soil erosion using the RUSLE model. `no licence`
- [avay-risal/UMRB-HUC12-SWAT-project_and_input-datasets](https://github.com/avay-risal/UMRB-HUC12-SWAT-project_and_input-datasets) - A repository to host our entire HUC12- SWAT project and input datasets for our Upper Mississippi River Watershed. `no licence`
- [bemacedom/RUSLEatGEE](https://github.com/bemacedom/RUSLEatGEE) - No description provided. `no licence`
- [dehonambiental/swat-cross-nutrient-sensitivity](https://github.com/dehonambiental/swat-cross-nutrient-sensitivity) - Code, model inputs and preserved results for cross-nutrient parameter sensitivity in SWAT and phosphorus modelling in the Edson Queiroz watershed, Brazil. `custom licence`
- [Divyaprajapati040901/RUSLE-Project](https://github.com/Divyaprajapati040901/RUSLE-Project) - No description provided. `no licence`
- [Filbra/HLC-RUSLE-HiLSS-Project](https://github.com/Filbra/HLC-RUSLE-HiLSS-Project) - No description provided. `CC0-1.0`
- [georgearhonditsis21/SWAT-Lake-Erie-Modelling](https://github.com/georgearhonditsis21/SWAT-Lake-Erie-Modelling) - Codes and data related to the study titled "A framework to evaluate the impact of wetlands on phosphorus loading in agricultural watersheds: connectivity and inundation in a wetlandscape context."". `no licence`
- [HosnaBaninajar/SWAT_model_for_Ilam_dam](https://github.com/HosnaBaninajar/SWAT_model_for_Ilam_dam) - Model inputs, outputs and the R codes used in research paper "A comprehensive sensitivity analysis, calibration and validation of SWAT model using discharge and evapotranspiration datasets in R… `no licence`
- [icra/traca_contaminacio](https://github.com/icra/traca_contaminacio) - Running SWAT+ projects with Python. `no licence`
- [kansesohan/Soil_Erosion_Modelling](https://github.com/kansesohan/Soil_Erosion_Modelling) - Godavari Basin, Maharashtra, India. `no licence`
- [noayarae/dmw_swat_model](https://github.com/noayarae/dmw_swat_model) - This folder contains the files from the "TxtInOut" folder generated by the SWAT model. `no licence`
- [Obed2022/ThesisFIU-data](https://github.com/Obed2022/ThesisFIU-data) - input and output data of hydrological modeling of Mayales Watershed using SWAT. `no licence`
- [ryusyaoming-glitch/Kangding_SoilErosion](https://github.com/ryusyaoming-glitch/Kangding_SoilErosion) - Public repository containing three key components for reproducibility of the PLOS ONE study — (1) raw datasets including land use and soil erodibility factor data, (2) original vector boundary files… `no licence`
- [sasishiva/RUSLE](https://github.com/sasishiva/RUSLE) - No description provided. `GPL-3.0`
- [sergiomlr/github-rswat-ver](https://github.com/sergiomlr/github-rswat-ver) - Run swat model and evaluate discharge in Veracruz Mexico. `no licence`
- [Sila88/SWAT_model_calibrated_Sesan_Srepok-River-Basin](https://github.com/Sila88/SWAT_model_calibrated_Sesan_Srepok-River-Basin) - SWAT model is free too used in the hydrological model to simulate unguage streamflow. In this model, we simulate streamflow of tributaries of Mekong Rivers, Sesan and Srepok River Bains from 2001 to… `no licence`
- [sonja419/LPJmL-Irrigation-Change](https://github.com/sonja419/LPJmL-Irrigation-Change) - No description provided. `no licence`
- [SREESRUTHYMS/soil-erosion-narmada-basin-gee](https://github.com/SREESRUTHYMS/soil-erosion-narmada-basin-gee) - This project focuses on estimating soil erosion in the Narmada Basin using the RUSLE (Revised Universal Soil Loss Equation) model in Google Earth Engine (GEE). integrates land use/land cover (LULC)… `no licence`
- [vani88/SWAT](https://github.com/vani88/SWAT) - SWAT model files and input data for Pakhal Watershed. `LGPL-2.1`
- [WeiZhiWater/The-Shallow-and-Deep-hypothesis-Subsurface-Vertical-Chemical-Contrasts-Shape-Nitrate-Export-Pattern](https://github.com/WeiZhiWater/The-Shallow-and-Deep-hypothesis-Subsurface-Vertical-Chemical-Contrasts-Shape-Nitrate-Export-Pattern) - This work tests the shallow and deep hypothesis: subsurface vertical chemical contrasts regulate nitrate export patterns under different land use conditions. We synthesized data from 228 watersheds… `no licence`

<a id="land-surface"></a>

### Land surface and global vegetation

<a id="land-surface-python"></a>

#### Python

- [ShannonRoos/CTSM5.2_CropHeatStress_postprocessing_evaluation](https://github.com/ShannonRoos/CTSM5.2_CropHeatStress_postprocessing_evaluation) - Python code for postprocessing and evaluation of analysis described in de Roos et al. (in prep). `no licence`

<a id="land-surface-r"></a>

#### R

- [pik-tess/boundaries](https://github.com/pik-tess/boundaries) - A systematic approach to quantify the status of the terrestrial planetary boundaries based on the Dynamic Global Vegetation Model (DGVM) Lund-Potsdam-Jena managed Land (LPJmL). The supported… `★ 10` `AGPL-3.0`

<a id="controlled-environment"></a>

### Greenhouses and controlled environments

<a id="controlled-environment-python"></a>

#### Python

- [BartvLaatum/RL-MPC-GreenLight](https://github.com/BartvLaatum/RL-MPC-GreenLight) - Code for implementation of Trajectory-selection RL-MPC applied to greenhouse fruit production control. `★ 1` `no licence`
- [flying-spagetti/digital-twin-for-hydrosprout](https://github.com/flying-spagetti/digital-twin-for-hydrosprout) - No description provided. `no licence`
- [growmatics/greenhouse-control-benchmark](https://github.com/growmatics/greenhouse-control-benchmark) - Code, run records and manuscript of record: a physics-informed vs black-box benchmark for greenhouse climate control on GreenLight-Gym2 (frozen artifact; the maintained benchmark is… `AGPL-3.0`
- [ImanHindi/AACSGH_Paper](https://github.com/ImanHindi/AACSGH_Paper) - Code and minimal dataset for Enhancing Autonomous Agriculture Control Systems in Greenhouses (PLOS ONE submission). `custom licence`
- [Surya891981/greenlight-rl](https://github.com/Surya891981/greenlight-rl) - Advanced Greenhouse Reinforcement Learning System. `no licence`

<a id="controlled-environment-r"></a>

#### R

- [AMIRMAHMOUDINIA/Lettuce-Artificial-Light-Photosynthesis-Vertical-Farming](https://github.com/AMIRMAHMOUDINIA/Lettuce-Artificial-Light-Photosynthesis-Vertical-Farming) - R-based analysis of LED spectrum effects on lettuce photosynthesis and chlorophyll fluorescence. `no licence`
