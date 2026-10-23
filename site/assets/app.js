/* Awesome Crop Models site: loads data/meta.json and data/catalogue.json, renders and filters them. */
(function () {
  "use strict";

  var DEFAULT_REPO = "https://github.com/YuanyuanMa03/awesome-crop-models";
  var PAGE = 30;
  // Catalogue row: [name, description, stars, language, type, subject, licence, archived]
  var NAME = 0, DESC = 1, STARS = 2, LANG = 3, TYPE = 4, SUBJECT = 5, LICENCE = 6, ARCHIVED = 7;
  var TYPES = ["m", "t", "a", "d"];

  var TEXT = {
    en: {
      skip: "Skip to the catalogue",
      nav_browse: "Browse", nav_starred: "Most starred", nav_explore: "Explore", nav_method: "Method",
      eyebrow: "Refreshed daily from GitHub",
      title: "Open-source crop models, <em>mapped</em>.",
      lede: "Crop growth simulators; soil, water and climate process models; and the frameworks, studies and data-driven methods around them. Sorted by crop or process, then programming language.",
      search_ph: "Search {n} repositories, e.g. wofost or maize",
      search_go: "Search",
      stat_listed: "Repositories listed", stat_crop: "Crop models", stat_process: "Process models",
      stat_tools: "Frameworks & tools", stat_data: "Data-driven models",
      stat_note: "Screened from {tracked} GitHub repositories found by {queries} searches and {owners} maintainer accounts · updated {updated}",
      browse_kicker: "01 — Browse", browse_title: "Start from a crop or a process",
      browse_text: "Every repository appears once: under its main crop or process, then its main programming language.",
      tab_crops: "Crops", tab_processes: "Processes", tab_tools: "Tools",
      repositories: "repositories",
      starred_kicker: "02 — Most starred", starred_title: "The community’s favourites",
      starred_text: "The most-starred process-based models and tools on the list.",
      explore_kicker: "03 — Explore", explore_title: "The full catalogue",
      explore_text: "Filter every listed repository by type, crop or process, and programming language.",
      f_search: "Search", f_search_ph: "Name or description", f_type: "Type", f_subject: "Crop or process",
      f_language: "Language", f_sort: "Sort", sort_stars: "Most stars", sort_name: "Name A–Z",
      all_types: "All types", all_subjects: "All crops and processes", all_languages: "All languages",
      reset: "Reset filters", loading: "Loading the catalogue…",
      count: "{n} repositories", showing: "Showing {shown} of {n} repositories",
      none: "No repositories match these filters.", more: "Show more",
      archived: "archived", no_licence: "no licence", custom_licence: "custom licence",
      group_crops: "Crops", group_processes: "Processes", group_tools: "Frameworks & tools",
      method_kicker: "04 — Method", method_title: "How the list is built",
      m1_title: "Search widely",
      m1_text: "{queries} GitHub searches cover model names, process terms, crops, several languages and topics, and {owners} maintainer accounts are listed in full. Searches are split by creation date to get past GitHub’s 1,000-result cap.",
      m2_title: "Decide explicitly",
      m2_text: "Search results are only candidates. A repository is listed only by a recorded decision; {excluded} rejections keep their reasons, and {awaiting} candidates wait for review.",
      m3_title: "Refresh daily",
      m3_text: "A scheduled workflow refreshes stars, licences and archive flags every day at 03:17 UTC, keeps resumable search state, and republishes this site.",
      cta_title: "Know a model we missed?", cta_text: "Suggest it with its crop or process. Corrections are welcome too.",
      cta_issue: "Suggest a repository", cta_guide: "Contribution guide",
      footer_text: "Data from GitHub, refreshed {updated}. Listing is not a scientific endorsement: check each project’s licence before reuse.",
      f_queue: "Review queue", f_status: "Collection status",
      fineprint: "MIT licence. Repository data comes from GitHub; each project keeps its own licence.",
      theme: "Toggle dark mode", language_switch: "中文",
      type: { m: "Model", t: "Tool", a: "Application", d: "Data-driven" },
      types: { m: "Models", t: "Tools", a: "Applications", d: "Data-driven" },
      breakdown: { m: "{n} models", t: "{n} tools", a: "{n} applications", d: "{n} data-driven" }
    },
    zh: {
      skip: "跳到目录",
      nav_browse: "浏览", nav_starred: "星标最多", nav_explore: "检索", nav_method: "方法",
      eyebrow: "每日从 GitHub 自动更新",
      title: "开源作物模型，<em>一图尽览</em>。",
      lede: "作物生长模拟器，土壤、水分与气候过程模型，以及围绕它们的框架、研究与数据驱动方法。先按作物或过程，再按编程语言整理。",
      search_ph: "搜索 {n} 个仓库，例如 wofost、maize",
      search_go: "搜索",
      stat_listed: "收录仓库", stat_crop: "作物模型", stat_process: "过程模型",
      stat_tools: "框架与工具", stat_data: "数据驱动模型",
      stat_note: "从 {queries} 条检索和 {owners} 个维护者账号找到的 {tracked} 个 GitHub 仓库中筛选 · 更新于 {updated}",
      browse_kicker: "01 — 浏览", browse_title: "从作物或过程开始",
      browse_text: "每个仓库只出现一次：挂在它最主要的作物或过程下，再按主要编程语言归类。",
      tab_crops: "作物", tab_processes: "过程", tab_tools: "框架与工具",
      repositories: "个仓库",
      starred_kicker: "02 — 星标最多", starred_title: "社区最常收藏的项目",
      starred_text: "清单里星标最多的过程模型与工具。",
      explore_kicker: "03 — 检索", explore_title: "完整目录",
      explore_text: "按类型、作物或过程、编程语言筛选全部收录仓库。",
      f_search: "搜索", f_search_ph: "名称或描述", f_type: "类型", f_subject: "作物或过程",
      f_language: "编程语言", f_sort: "排序", sort_stars: "星标最多", sort_name: "名称 A–Z",
      all_types: "全部类型", all_subjects: "全部作物与过程", all_languages: "全部语言",
      reset: "重置筛选", loading: "正在加载目录…",
      count: "共 {n} 个仓库", showing: "显示 {shown} / {n} 个仓库",
      none: "没有符合条件的仓库。", more: "显示更多",
      archived: "已归档", no_licence: "无许可", custom_licence: "自定义许可",
      group_crops: "作物", group_processes: "过程", group_tools: "框架与工具",
      method_kicker: "04 — 方法", method_title: "清单如何生成",
      m1_title: "广泛检索",
      m1_text: "{queries} 条 GitHub 检索覆盖模型名称、过程术语、作物、多种语言和 topic，并完整枚举 {owners} 个维护者账号；检索按创建时间切片，突破 GitHub 单次检索 1,000 条的上限。",
      m2_title: "明确决定",
      m2_text: "检索结果只是候选。只有记录在案的决定才会收录：{excluded} 个排除都写明理由，另有 {awaiting} 个候选等待审核。",
      m3_title: "每日刷新",
      m3_text: "定时工作流每天 UTC 03:17 刷新星标、许可和归档状态，保存可续跑的检索进度，并重新发布本站。",
      cta_title: "发现遗漏的模型？", cta_text: "告诉我们它模拟的作物或过程，也欢迎指正已有条目。",
      cta_issue: "推荐仓库", cta_guide: "贡献指南",
      footer_text: "数据来自 GitHub，更新于 {updated}。收录不代表科学背书，复用前请查看各项目的许可。",
      f_queue: "待审队列", f_status: "采集状态",
      fineprint: "MIT 许可。仓库数据来自 GitHub，各项目保留自己的许可。",
      theme: "切换深色模式", language_switch: "EN",
      type: { m: "模型", t: "工具", a: "应用", d: "数据驱动" },
      types: { m: "模型", t: "工具", a: "应用", d: "数据驱动" },
      breakdown: { m: "{n} 个模型", t: "{n} 个工具", a: "{n} 个应用", d: "{n} 个数据驱动" }
    }
  };

  var SUBJECT_ZH = {
    "general-crop": "通用与多作物", rice: "水稻", wheat: "小麦", maize: "玉米",
    "other-cereals": "大麦、高粱、谷子等其他谷物", soybean: "大豆", "legumes-oilseeds": "其他豆类与油料",
    potato: "马铃薯", "roots-tubers": "木薯等根茎类", cotton: "棉花", "sugar-crops": "甘蔗与甜菜",
    vegetables: "蔬菜", "fruit-vine": "果树与葡萄", plantation: "油棕、咖啡、可可等种植园作物",
    grassland: "草地、牧草与饲草", "bioenergy-other": "生物能源及其他作物",
    phenology: "物候与发育", photosynthesis: "光合、冠层与蒸腾", architecture: "植株结构与 FSPM",
    roots: "根系与根际", "soil-water": "土壤水热", "soil-nutrients": "土壤碳氮与养分",
    "greenhouse-gases": "农业温室气体", evapotranspiration: "蒸散与灌溉", weather: "天气与农业气候",
    "pests-diseases": "病虫草害", hydrology: "水文、侵蚀与流域", "land-surface": "陆面与全球植被",
    "controlled-environment": "温室与可控环境",
    frameworks: "建模框架与平台", interfaces: "模型接口与封装", calibration: "率定、敏感性与不确定性",
    "data-assimilation": "数据同化与遥感", gridded: "区域与格点模拟", "model-data": "输入、参数与数据",
    learning: "教程与教学"
  };

  // Hero shortcuts; "en" shortens a long English subject label.
  var CHIPS = [
    { subject: "maize" }, { subject: "rice" }, { subject: "wheat" },
    { subject: "evapotranspiration", en: "Evapotranspiration" }, { subject: "soil-water", en: "Soil water" },
    { q: "wofost" }, { q: "apsim" }, { q: "dssat" }
  ];

  var root = document.documentElement;
  var lang = root.dataset.lang === "zh" ? "zh" : "en";
  var meta = null;
  var rows = null;
  var group = "crops";
  var shown = PAGE;
  var state = { q: "", type: "", subject: "", lang: "", sort: "stars" };
  var repoUrl = repositoryUrl();

  function $(selector) { return document.querySelector(selector); }

  function t(key, values) {
    var value = TEXT[lang][key];
    if (value === undefined) value = TEXT.en[key];
    if (typeof value !== "string") return value;
    return value.replace(/\{(\w+)\}/g, function (_, name) {
      return values && values[name] !== undefined ? values[name] : "";
    });
  }

  function number(value) {
    return new Intl.NumberFormat(lang === "zh" ? "zh-CN" : "en-US").format(value);
  }

  function stars(count) {
    if (count < 1000) return String(count);
    if (count < 10000) return (Math.round(count / 100) / 10).toString().replace(/\.0$/, "") + "k";
    return Math.floor(count / 1000) + "k";
  }

  function label(subject) {
    if (lang === "zh" && SUBJECT_ZH[subject]) return SUBJECT_ZH[subject];
    return meta && meta.labels[subject] ? meta.labels[subject] : subject;
  }

  function el(tag, className, text) {
    var node = document.createElement(tag);
    if (className) node.className = className;
    if (text !== undefined) node.textContent = text;
    return node;
  }

  function repositoryUrl() {
    // On <owner>.github.io/<repository>/ link to that repository, so a fork links to itself.
    var host = location.hostname.match(/^([^.]+)\.github\.io$/i);
    var path = location.pathname.split("/").filter(Boolean);
    return host && path.length ? "https://github.com/" + host[1] + "/" + path[0] : DEFAULT_REPO;
  }

  function figures() {
    if (!meta) return {};
    return {
      n: number(meta.listed), tracked: number(meta.tracked), queries: number(meta.queries),
      owners: number(meta.owners), excluded: number(meta.excluded), awaiting: number(meta.awaiting),
      updated: meta.updated || "—"
    };
  }

  /* Static text */

  function applyText() {
    var values = figures();
    root.lang = lang === "zh" ? "zh-CN" : "en";
    document.querySelectorAll("[data-i18n]").forEach(function (node) {
      node.textContent = t(node.dataset.i18n, values);
    });
    document.querySelectorAll("[data-i18n-html]").forEach(function (node) {
      node.innerHTML = t(node.dataset.i18nHtml); // trusted strings from TEXT only
    });
    document.querySelectorAll("[data-i18n-placeholder]").forEach(function (node) {
      node.placeholder = t(node.dataset.i18nPlaceholder);
    });
    $("#hero-q").placeholder = t("search_ph", values);
    $("#lang-toggle").textContent = t("language_switch");
    $("#theme-toggle").setAttribute("aria-label", t("theme"));
    if (meta) $("#stat-note").textContent = t("stat_note", values);
  }

  /* Hero */

  function renderChips() {
    var box = $("#hero-chips");
    box.textContent = "";
    CHIPS.forEach(function (chip) {
      var button = el("button", "chip");
      button.type = "button";
      if (chip.subject) {
        button.textContent = lang === "en" && chip.en ? chip.en : label(chip.subject);
        button.addEventListener("click", function () { go({ subject: chip.subject }); });
      } else {
        button.appendChild(el("span", "mono", chip.q));
        button.addEventListener("click", function () { go({ q: chip.q }); });
      }
      box.appendChild(button);
    });
  }

  function renderStats() {
    var types = meta.types;
    var values = {
      listed: meta.listed, cropModels: meta.cropModels, processModels: (types.m || 0) - meta.cropModels,
      tools: types.t || 0, dataDriven: types.d || 0
    };
    document.querySelectorAll("[data-stat]").forEach(function (node) {
      node.textContent = number(values[node.dataset.stat]);
    });
  }

  /* Browse */

  function renderCards() {
    var grid = $("#subject-grid");
    grid.textContent = "";
    meta.groups[group].forEach(function (subject) {
      var info = meta.subjects[subject];
      if (!info) return;
      var card = el("button", "subject-card");
      card.type = "button";
      card.appendChild(el("span", "name", label(subject)));
      card.insertAdjacentHTML("beforeend", '<svg class="arrow" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>');
      var count = el("span", "count", number(info.total));
      count.appendChild(el("small", "", t("repositories")));
      card.appendChild(count);
      var breakdown = el("span", "breakdown");
      TYPES.forEach(function (type) {
        if (!info.types[type]) return;
        var item = el("span");
        item.appendChild(el("span", "dot t-" + type));
        item.appendChild(document.createTextNode(t("breakdown")[type].replace("{n}", number(info.types[type]))));
        breakdown.appendChild(item);
      });
      card.appendChild(breakdown);
      card.appendChild(el("span", "langs", info.languages.join(" · ")));
      card.addEventListener("click", function () { go({ subject: subject }); });
      grid.appendChild(card);
    });
  }

  /* Most starred */

  function repoLink(name) {
    var link = el("a", "repo");
    link.href = "https://github.com/" + name;
    link.target = "_blank";
    link.rel = "noopener";
    var slash = name.indexOf("/");
    link.appendChild(el("span", "owner", name.slice(0, slash + 1)));
    link.appendChild(document.createTextNode(name.slice(slash + 1)));
    return link;
  }

  function licenceText(value) {
    if (!value) return t("no_licence");
    return value === "custom" ? t("custom_licence") : value;
  }

  function metaLine(row, withStars) {
    var line = el("div", "meta");
    var tag = el("span", "tag");
    tag.appendChild(el("span", "dot t-" + row[TYPE]));
    tag.appendChild(document.createTextNode(t("type")[row[TYPE]]));
    line.appendChild(tag);
    line.appendChild(el("span", "", label(row[SUBJECT])));
    line.appendChild(el("span", "", row[LANG]));
    if (withStars) line.appendChild(el("span", "stars", "★ " + stars(row[STARS])));
    line.appendChild(el("span", "", licenceText(row[LICENCE])));
    return line;
  }

  function renderStarred() {
    var list = $("#starred-list");
    list.textContent = "";
    meta.top.forEach(function (row, index) {
      var item = el("li", "starred-item");
      item.appendChild(el("span", "rank", String(index + 1).padStart(2, "0")));
      var body = el("div");
      body.appendChild(repoLink(row[NAME]));
      body.appendChild(el("p", "desc", row[DESC]));
      body.appendChild(metaLine(row, true));
      item.appendChild(body);
      list.appendChild(item);
    });
  }

  /* Explore */

  function readHash() {
    var match = location.hash.match(/^#explore\?(.*)$/);
    if (!match) return;
    var params = new URLSearchParams(match[1]);
    state.q = params.get("q") || "";
    state.type = TYPES.indexOf(params.get("type")) >= 0 ? params.get("type") : "";
    state.subject = params.get("subject") || "";
    state.lang = params.get("lang") || "";
    state.sort = params.get("sort") === "name" ? "name" : "stars";
  }

  function writeHash() {
    var params = new URLSearchParams();
    if (state.q) params.set("q", state.q);
    if (state.type) params.set("type", state.type);
    if (state.subject) params.set("subject", state.subject);
    if (state.lang) params.set("lang", state.lang);
    if (state.sort !== "stars") params.set("sort", state.sort);
    var query = params.toString();
    history.replaceState(null, "", query ? "#explore?" + query : location.pathname + location.search);
  }

  function matches(row, terms, skipType) {
    if (!skipType && state.type && row[TYPE] !== state.type) return false;
    if (state.subject && row[SUBJECT] !== state.subject) return false;
    if (state.lang && row[LANG] !== state.lang) return false;
    for (var i = 0; i < terms.length; i++) if (row.hay.indexOf(terms[i]) < 0) return false;
    return true;
  }

  function fillSelects() {
    var subject = $("#subject");
    subject.textContent = "";
    subject.appendChild(new Option(t("all_subjects"), ""));
    [["crops", "group_crops"], ["processes", "group_processes"], ["tools", "group_tools"]].forEach(function (pair) {
      var optgroup = document.createElement("optgroup");
      optgroup.label = t(pair[1]);
      meta.groups[pair[0]].forEach(function (key) {
        if (meta.subjects[key]) optgroup.appendChild(new Option(label(key), key));
      });
      subject.appendChild(optgroup);
    });
    subject.value = state.subject;
    var language = $("#language");
    language.textContent = "";
    language.appendChild(new Option(t("all_languages"), ""));
    if (rows) {
      var counts = {};
      rows.forEach(function (row) { counts[row[LANG]] = (counts[row[LANG]] || 0) + 1; });
      Object.keys(counts).sort(function (a, b) { return counts[b] - counts[a] || a.localeCompare(b); }).forEach(function (name) {
        language.appendChild(new Option(name + " (" + number(counts[name]) + ")", name));
      });
    }
    language.value = state.lang;
    $("#sort").value = state.sort;
    $("#q").value = state.q;
  }

  function renderTypes(terms) {
    var counts = { "": 0 };
    TYPES.forEach(function (type) { counts[type] = 0; });
    rows.forEach(function (row) {
      if (matches(row, terms, true)) { counts[""]++; counts[row[TYPE]]++; }
    });
    var list = $("#type-list");
    list.textContent = "";
    [""].concat(TYPES).forEach(function (type) {
      var option = el("button", "type-option");
      option.type = "button";
      option.setAttribute("role", "radio");
      option.setAttribute("aria-checked", String(state.type === type));
      option.appendChild(el("span", "dot " + (type ? "t-" + type : "all")));
      option.appendChild(document.createTextNode(type ? t("types")[type] : t("all_types")));
      option.appendChild(el("span", "n", number(counts[type])));
      option.addEventListener("click", function () { state.type = type; update(true); });
      list.appendChild(option);
    });
  }

  function resultItem(row) {
    var item = el("li", "result");
    var top = el("div", "result-top");
    top.appendChild(repoLink(row[NAME]));
    if (row[ARCHIVED]) top.appendChild(el("span", "badge", t("archived")));
    if (row[STARS]) top.appendChild(el("span", "stars", "★ " + stars(row[STARS])));
    item.appendChild(top);
    if (row[DESC]) item.appendChild(el("p", "desc", row[DESC]));
    item.appendChild(metaLine(row, false));
    return item;
  }

  function renderResults() {
    if (!rows) return;
    var terms = state.q.toLowerCase().split(/\s+/).filter(Boolean);
    renderTypes(terms);
    var list = rows.filter(function (row) { return matches(row, terms, false); });
    if (state.sort === "name") list.sort(function (a, b) { return a[NAME].localeCompare(b[NAME], "en", { sensitivity: "base" }); });
    var results = $("#results");
    results.textContent = "";
    if (!list.length) {
      results.appendChild(el("li", "empty", t("none")));
    } else {
      var fragment = document.createDocumentFragment();
      list.slice(0, shown).forEach(function (row) { fragment.appendChild(resultItem(row)); });
      results.appendChild(fragment);
    }
    var visible = Math.min(shown, list.length);
    $("#results-count").textContent = list.length > visible
      ? t("showing", { shown: number(visible), n: number(list.length) })
      : t("count", { n: number(list.length) });
    $("#more").hidden = list.length <= visible;
  }

  function update(resetPage) {
    if (resetPage) shown = PAGE;
    writeHash();
    renderResults();
  }

  function go(change) {
    state.q = change.q || "";
    state.subject = change.subject || "";
    state.type = "";
    state.lang = "";
    if (meta) fillSelects();
    update(true);
    $("#explore").scrollIntoView({ behavior: matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth" });
  }

  function skeleton() {
    var results = $("#results");
    results.textContent = "";
    for (var i = 0; i < 6; i++) {
      var item = el("li", "result");
      [38, 92, 64].forEach(function (width) {
        var bar = el("div", "skeleton");
        bar.style.width = width + "%";
        item.appendChild(bar);
      });
      results.appendChild(item);
    }
    $("#results-count").textContent = t("loading");
  }

  /* Wiring */

  function renderAll() {
    applyText();
    renderChips();
    if (!meta) return;
    renderStats();
    renderCards();
    renderStarred();
    fillSelects();
    if (rows) renderResults();
  }

  function bind() {
    var timer = null;
    $("#q").addEventListener("input", function (event) {
      clearTimeout(timer);
      timer = setTimeout(function () { state.q = event.target.value; update(true); }, 120);
    });
    $("#subject").addEventListener("change", function (event) { state.subject = event.target.value; update(true); });
    $("#language").addEventListener("change", function (event) { state.lang = event.target.value; update(true); });
    $("#sort").addEventListener("change", function (event) { state.sort = event.target.value; update(true); });
    $("#reset").addEventListener("click", function () {
      state = { q: "", type: "", subject: "", lang: "", sort: "stars" };
      fillSelects();
      update(true);
    });
    $("#more").addEventListener("click", function () { shown += PAGE; renderResults(); });
    $("#hero-search").addEventListener("submit", function (event) {
      event.preventDefault();
      go({ q: $("#hero-q").value.trim() });
    });
    $("#browse-tabs").addEventListener("click", function (event) {
      var button = event.target.closest("button[data-group]");
      if (!button) return;
      group = button.dataset.group;
      document.querySelectorAll("#browse-tabs button").forEach(function (tab) {
        tab.setAttribute("aria-selected", String(tab === button));
      });
      if (meta) renderCards();
    });
    $("#lang-toggle").addEventListener("click", function () {
      lang = lang === "zh" ? "en" : "zh";
      root.dataset.lang = lang;
      try { localStorage.setItem("acm-lang", lang); } catch (e) {}
      renderAll();
    });
    $("#theme-toggle").addEventListener("click", function () {
      var dark = root.dataset.theme ? root.dataset.theme === "dark" : matchMedia("(prefers-color-scheme: dark)").matches;
      root.dataset.theme = dark ? "light" : "dark";
      try { localStorage.setItem("acm-theme", root.dataset.theme); } catch (e) {}
    });
    document.addEventListener("keydown", function (event) {
      if (event.key !== "/" || event.metaKey || event.ctrlKey || event.altKey) return;
      var tag = (document.activeElement && document.activeElement.tagName) || "";
      if (tag === "INPUT" || tag === "SELECT" || tag === "TEXTAREA") return;
      event.preventDefault();
      $("#hero-q").focus();
    });
    var nav = $("#nav");
    var onScroll = function () { nav.classList.toggle("scrolled", window.scrollY > 8); };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
    document.querySelectorAll(".repo-link").forEach(function (link) {
      link.href = repoUrl + (link.dataset.path || "");
    });
  }

  function load(path) {
    return fetch(path).then(function (response) {
      if (!response.ok) throw new Error(path + ": " + response.status);
      return response.json();
    });
  }

  readHash();
  bind();
  renderAll();
  skeleton();
  load("data/meta.json").then(function (data) {
    meta = data;
    renderAll();
    if (!rows) skeleton();
    return load("data/catalogue.json");
  }).then(function (data) {
    data.forEach(function (row) { row.hay = (row[NAME] + " " + row[DESC]).toLowerCase(); });
    rows = data;
    fillSelects();
    renderResults();
    if (/^#explore\?/.test(location.hash)) $("#explore").scrollIntoView();
  }).catch(function (error) {
    $("#results-count").textContent = String(error.message || error);
  });
})();
