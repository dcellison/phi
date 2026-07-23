/* Phi lexicon explorer: read-only search over the generated lexicon.json,
   with the generated compound registry beside it. */
(async function () {
  const $ = (id) => document.getElementById(id);
  const PAGE = 50;
  const BASE_VOCABULARY = "base-vocabulary";
  const REGISTERED_COMPOUNDS = "registered-compounds";
  const WORD_FILTERS = ["f-pos", "f-domain", "f-module", "f-pillar"];
  const HONORIFIC_GLOSSES = new Set(["HON.RESPECT", "HON.INTIM", "HON.ROLE"]);
  let lexicon = [], compounds = [], words = new Set(), glosses = new Map();
  let currentResults = [], currentPage = 1, emptyStatus = "";
  let resultCounts = { words: 0, compounds: 0, compoundOnly: false };

  const PILLAR_NAMES = {
    "solarpunk-values": "solarpunk",
    "secular-buddhist-philosophy": "secular buddhist",
    "art-nouveau-aesthetics": "art nouveau",
    "peace-linguistics-practices": "peace linguistics",
    "pre-industrial-wisdom": "pre-industrial wisdom",
  };

  const MODULE_NAMES = {
    "household-and-daily-life": "household and daily life",
    "medical-and-bodily-care": "medical and bodily care",
    "systems-and-shared-infrastructure": "systems and shared infrastructure",
    "philosophical-reasoning": "philosophical reasoning",
    "accessibility-and-participation": "accessibility and participation",
    "commons-and-collective-governance": "commons and collective governance",
    "ecological-systems-and-material-life": "ecological systems and material life",
    "work-craft-and-repair": "work, craft, and repair",
  };

  try {
    lexicon = await (await fetch("lexicon.json")).json();
  } catch {
    $("status").textContent = "lexicon.json not found. Run: python3 scripts/build_site.py";
    return;
  }
  try {
    compounds = await (await fetch("compounds.json")).json();
  } catch {
    compounds = []; // the explorer stands without the registry file
  }
  let teng = { glyphs: {}, words: {} };
  try {
    teng = await (await fetch("tengwar_words.json")).json();
  } catch {
    // the explorer stands without the tengwar hand
  }
  words = new Set(lexicon.map((e) => e.word));
  glosses = new Map(lexicon.map((e) => [e.word, e.gloss]));
  const compoundsOf = new Map();
  for (const c of compounds)
    for (const w of new Set(c.tokens)) {
      if (!compoundsOf.has(w)) compoundsOf.set(w, []);
      compoundsOf.get(w).push(c);
    }
  $("count").textContent = lexicon.length;

  // filter options from the data
  const opts = { pos: new Set(), domain: new Set(), module: new Set(), pillar: new Set() };
  for (const e of lexicon) {
    opts.pos.add(e.pos);
    Object.keys(e.semantic_domains || {}).forEach((domain) => opts.domain.add(domain));
    (e.modules || []).forEach((m) => opts.module.add(m));
    Object.keys(e.pillars || {}).forEach((p) => opts.pillar.add(p));
  }
  const fill = (sel, values, label) => {
    for (const v of [...values].sort()) {
      const o = document.createElement("option");
      o.value = v;
      o.textContent = label ? label(v) : v;
      sel.appendChild(o);
    }
  };
  fill($("f-pos"), opts.pos);
  fill($("f-domain"), opts.domain);
  fill($("f-module"), opts.module, (v) => MODULE_NAMES[v] || v);
  fill($("f-pillar"), opts.pillar, (v) => PILLAR_NAMES[v] || v);

  const esc = (s) => s.replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

  // wrap quoted Phi in .phi spans; clicking a known Phi word searches it
  const phiify = (s) =>
    esc(s).replace(/'([a-z][a-z .]*?)'/g, (m, inner) => {
      const tok = inner.replace(/\.$/, "");
      const link = words.has(tok) && !inner.includes(" ");
      return `<span class="phi"${link ? ` data-w="${tok}" role="link" tabindex="0"` : ""}>${inner}</span>`;
    });

  const textScore = (value, q) => {
    const text = (value || "").normalize("NFC").toLowerCase();
    if (text === q) return 0;
    if (text.startsWith(q)) return 1;
    if (text.includes(q)) return 2;
    return -1;
  };

  const valuesScore = (values, q) => {
    const scores = values.map((value) => textScore(value, q)).filter((s) => s >= 0);
    return scores.length ? Math.min(...scores) : -1;
  };

  const exampleValues = (e) => (e.examples || []).flatMap((example) => [
    example.phi,
    example.translation,
  ]);

  const fieldScore = (e, q, field) => {
    if (field === "pronunciation") {
      const values = [e.ipa, e.syllables.join(" "), e.syllables.join(" · ")];
      return valuesScore(values, q);
    }
    if (field === "keywords")
      return valuesScore([...(e.search_terms || []), e.concept], q);
    if (field === "usage_and_examples")
      return valuesScore([
        e.usage_notes,
        e.grammatical_notes,
        ...exampleValues(e),
      ], q);
    return textScore(e[field], q);
  };

  const score = (e, q, field) => {
    if (field !== "all") return fieldScore(e, q, field);
    if (e.word === q || e.gloss.toLowerCase() === q) return 0;
    if (e.word.startsWith(q)) return 1;
    if (e.gloss.toLowerCase().includes(q)) return 2;
    if (e.word.includes(q)) return 3;
    if (fieldScore(e, q, "keywords") >= 0) return 4;
    if (textScore(e.description, q) >= 0) return 5;
    if (fieldScore(e, q, "usage_and_examples") >= 0) return 6;
    if (textScore(e.articulatory_notes, q) >= 0) return 7;
    if (textScore(e.sound_symbolism, q) >= 0) return 8;
    if (fieldScore(e, q, "pronunciation") >= 0) return 9;
    return -1;
  };

  const compScore = (c, q, field) => {
    if (field !== "all" && field !== REGISTERED_COMPOUNDS) return -1;
    if (c.compound === q || c.meaning.toLowerCase() === q) return 0;
    if (c.meaning.toLowerCase().includes(q)) return 1;
    if (c.compound.includes(q)) return 2;
    if (c.literal.toLowerCase().includes(q)) return 3;
    return -1;
  };

  // a compound phrase with each member word clickable
  const compPhrase = (c) =>
    c.compound.split(" ").map((t) => {
      const tok = t.replace(/[\[\]]/g, "");
      return words.has(tok)
        ? t.replace(tok, `<span class="phi" data-w="${tok}" role="link" tabindex="0">${tok}</span>`)
        : esc(t);
    }).join(" ");

  function search({ page = 1, historyMode = "replace", moveFocus = false } = {}) {
    const q = $("q").value.trim().normalize("NFC").toLowerCase();
    const field = $("f-field").value;
    const compoundOnly = field === REGISTERED_COMPOUNDS;
    const fp = $("f-pos").value, fd = $("f-domain").value;
    const fm = $("f-module").value, fl = $("f-pillar").value;
    const wordMatches = lexicon
      .map((e) => ({ e, s: q ? score(e, q, field) : (compoundOnly ? -1 : 9) }))
      .filter(({ e, s }) =>
        s >= 0 &&
        (!fp || e.pos === fp) &&
        (!fd || (e.semantic_domains && fd in e.semantic_domains)) &&
        (!fm || (fm === BASE_VOCABULARY ? (e.modules || []).length === 0 : (e.modules || []).includes(fm))) &&
        (!fl || (e.pillars && fl in e.pillars)))
      .sort((a, b) => a.s - b.s || a.e.word.localeCompare(b.e.word))
      .map(({ e }) => e);
    // Registered compounds answer all-field searches or their own scope.
    // Word facets stay available for lexicon entries only.
    const showCompounds = compoundOnly || (field === "all" && q && !fp && !fd && !fm && !fl);
    const compMatches = showCompounds
      ? compounds
          .map((c) => ({ c, s: q ? compScore(c, q, field) : 4 }))
          .filter(({ s }) => s >= 0)
          .sort((a, b) => a.s - b.s || a.c.compound.localeCompare(b.c.compound))
          .map(({ c }) => c)
      : [];

    currentResults = [
      ...compMatches.map((value) => ({ kind: "compound", value })),
      ...wordMatches.map((value) => ({ kind: "word", value })),
    ];
    resultCounts = {
      words: wordMatches.length,
      compounds: compMatches.length,
      compoundOnly,
    };
    emptyStatus = compoundOnly
      ? "nothing found: the compound registry may simply not have it yet"
      : "nothing found: the lexicon may simply not have it yet";
    currentPage = clampPage(page);
    renderPage();
    syncUrl(historyMode);
    if (moveFocus) moveToResults();
  }

  function totalPages() {
    return Math.ceil(currentResults.length / PAGE);
  }

  function clampPage(page) {
    const last = Math.max(1, totalPages());
    const requested = Number.parseInt(page, 10);
    return Number.isFinite(requested) ? Math.min(Math.max(requested, 1), last) : 1;
  }

  function renderPage() {
    const start = (currentPage - 1) * PAGE;
    const slice = currentResults.slice(start, start + PAGE);
    const frag = document.createDocumentFragment();
    for (const result of slice)
      frag.appendChild(result.kind === "compound" ? compRow(result.value) : row(result.value));
    $("results").replaceChildren(frag);
    renderStatus(start, slice.length);
    renderPagination($("pages-top"));
    renderPagination($("pages-bottom"));
  }

  function renderStatus(start, count) {
    if (!currentResults.length) {
      $("status").textContent = emptyStatus;
      return;
    }
    const first = start + 1;
    const last = start + count;
    const firstLabel = first.toLocaleString("en-US");
    const lastLabel = last.toLocaleString("en-US");
    const range = first === last ? firstLabel : `${firstLabel}-${lastLabel}`;
    const total = currentResults.length.toLocaleString("en-US");
    if (resultCounts.compoundOnly) {
      $("status").textContent =
        `showing ${range} of ${total} registered ${resultCounts.compounds === 1 ? "compound" : "compounds"}`;
      return;
    }
    if (!resultCounts.compounds) {
      $("status").textContent =
        `showing ${range} of ${total} ${resultCounts.words === 1 ? "word" : "words"}`;
      return;
    }
    const wordsLabel = `${resultCounts.words.toLocaleString("en-US")} ${resultCounts.words === 1 ? "word" : "words"}`;
    const compoundsLabel =
      `${resultCounts.compounds.toLocaleString("en-US")} ${resultCounts.compounds === 1 ? "compound" : "compounds"}`;
    $("status").textContent =
      `showing ${range} of ${total} results: ${wordsLabel}, ${compoundsLabel}`;
  }

  function pageWindow(last) {
    const compact = window.matchMedia("(max-width: 560px)").matches;
    if (last <= (compact ? 4 : 7)) return Array.from({ length: last }, (_, i) => i + 1);
    const pages = new Set([1, last, currentPage]);
    const radius = compact ? 0 : 1;
    for (let page = currentPage - radius; page <= currentPage + radius; page++)
      if (page > 1 && page < last) pages.add(page);
    const edge = compact ? 2 : 4;
    if (currentPage <= edge)
      for (let page = 2; page <= edge; page++) pages.add(page);
    if (currentPage >= last - edge + 1)
      for (let page = last - edge + 1; page < last; page++) pages.add(page);
    return [...pages].sort((a, b) => a - b);
  }

  function pageButton(text, label, page, disabled = false) {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "page-button";
    button.textContent = text;
    button.setAttribute("aria-label", label);
    button.title = label;
    button.disabled = disabled;
    if (!disabled) button.addEventListener("click", () => goToPage(page));
    return button;
  }

  function renderPagination(nav) {
    const last = totalPages();
    nav.replaceChildren();
    nav.hidden = last <= 1;
    if (last <= 1) return;

    nav.appendChild(pageButton("←", "previous page", currentPage - 1, currentPage === 1));
    let previous = 0;
    for (const page of pageWindow(last)) {
      if (previous && page - previous > 1) {
        const ellipsis = document.createElement("span");
        ellipsis.className = "page-ellipsis";
        ellipsis.textContent = "…";
        ellipsis.setAttribute("aria-hidden", "true");
        nav.appendChild(ellipsis);
      }
      if (page === currentPage) {
        const current = document.createElement("span");
        current.className = "page-current";
        current.textContent = page;
        current.setAttribute("aria-current", "page");
        current.setAttribute("aria-label", `page ${page}, current page`);
        nav.appendChild(current);
      } else {
        nav.appendChild(pageButton(`${page}`, `page ${page}`, page));
      }
      previous = page;
    }
    nav.appendChild(pageButton("→", "next page", currentPage + 1, currentPage === last));
  }

  function goToPage(page) {
    const next = clampPage(page);
    if (next === currentPage) return;
    currentPage = next;
    renderPage();
    syncUrl("push");
    moveToResults();
  }

  function moveToResults() {
    $("results").focus({ preventScroll: true });
    $("results").scrollIntoView({ behavior: "smooth", block: "start" });
  }

  function row(e) {
    const li = document.createElement("li");
    const head = document.createElement("button");
    head.className = "entry-head";
    head.setAttribute("aria-expanded", "false");
    head.innerHTML =
      `<span class="w">${esc(e.word)}</span>` +
      `<span class="g">${esc(e.gloss)}</span>` +
      `<span class="pos">${esc(e.pos)}</span>` +
      `<span class="ipa-line">${esc(e.ipa)}<span class="syll">${e.syllables.join(" · ")}</span></span>`;
    head.addEventListener("click", () => {
      const open = li.querySelector(".entry-body");
      if (open) { open.remove(); head.setAttribute("aria-expanded", "false"); }
      else { li.appendChild(body(e)); head.setAttribute("aria-expanded", "true"); }
    });
    li.appendChild(head);
    return li;
  }

  function compRow(c) {
    const li = document.createElement("li");
    const head = document.createElement("button");
    head.className = "entry-head";
    head.setAttribute("aria-expanded", "false");
    head.innerHTML =
      `<span class="w">${esc(c.compound)}</span>` +
      `<span class="g">${esc(c.meaning)}</span>` +
      `<span class="pos">compound</span>` +
      `<span class="ipa-line">${esc(c.literal)}</span>`;
    head.addEventListener("click", () => {
      const open = li.querySelector(".entry-body");
      if (open) { open.remove(); head.setAttribute("aria-expanded", "false"); }
      else { li.appendChild(compBody(c)); head.setAttribute("aria-expanded", "true"); }
    });
    li.appendChild(head);
    return li;
  }

  function compBody(c) {
    const div = document.createElement("div");
    div.className = "entry-body";
    div.innerHTML =
      `<p class="concept">${compPhrase(c)}, ${esc(c.literal)}: ${esc(c.meaning)}.</p>` +
      `<p>${c.why_html}</p>` +
      `<p class="rule-note">A canonized compound from the registry; each word inside it is an ordinary lexicon word.</p>` +
      `<p class="tagrow"><span class="tag">${esc(c.section.toLowerCase())}</span></p>`;
    return div;
  }

  function tengSvg(t) {
    // Mirrors scripts/tengwar.py render_line(): same markup, same numbers,
    // assembled from the shared glyph dictionary.
    const paths = t.p
      .map(([k, gx, gy]) => `<path transform="translate(${gx} ${gy})" d="${teng.glyphs[k]}"/>`)
      .join("");
    return `<svg class="teng-svg" xmlns="http://www.w3.org/2000/svg" ` +
      `viewBox="${t.vb[0]} ${t.vb[1]} ${t.vb[2]} ${t.vb[3]}" ` +
      `style="height:${t.em}em" fill="currentColor">` +
      `<g transform="scale(1,-1)">${paths}</g></svg>`;
  }

  function body(e) {
    const div = document.createElement("div");
    div.className = "entry-body";
    const t = teng.words[e.word];
    let h = t ? `<p class="entry-teng">${tengSvg(t)}</p>` : "";
    h += e.concept ? `<p class="concept">${esc(e.concept)}</p>` : "";
    h += `<p>${phiify(e.description)}</p>`;
    if (e.pos === "verb")
      h += `<p class="rule-note">Also its own noun, the act or its result, by the event-noun rule.</p>`;
    if (e.articulatory_notes) h += `<h3>Articulation</h3><p>${phiify(e.articulatory_notes)}</p>`;
    if (e.sound_symbolism) h += `<h3>Sound symbolism</h3><p>${phiify(e.sound_symbolism)}</p>`;
    const usage = e.usage_notes || e.grammatical_notes;
    if (usage) h += `<h3>Usage</h3><p>${phiify(usage)}</p>`;
    if ((e.examples || []).length) {
      h += `<h3>Examples</h3>`;
      for (const example of e.examples)
        h += `<div class="example"><p class="phi-line">${esc(example.phi)}</p>` +
          `<p class="gloss-line">${esc(exampleGloss(example.phi))}</p>` +
          `<p class="translation">${esc(example.translation)}</p></div>`;
    }
    const comps = compoundsOf.get(e.word) || [];
    if (comps.length) {
      h += `<h3>Compounds</h3>`;
      for (const c of comps)
        h += `<p class="compound">${compPhrase(c)} (${esc(c.literal)}): ${esc(c.meaning)}</p>`;
    }
    const pillars = Object.entries(e.pillars || {});
    if (pillars.length) {
      h += `<h3>Pillars</h3>`;
      for (const [k, v] of pillars)
        h += `<p class="pillar"><b>${esc(PILLAR_NAMES[k] || k)}</b>${phiify(v)}</p>`;
    }
    const domains = Object.keys(e.semantic_domains || {});
    if (domains.length)
      h += `<p class="tagrow">${domains.map((domain) => `<span class="tag">${esc(domain)}</span>`).join("")}</p>`;
    const modules = e.modules || [];
    if (modules.length)
      h += `<p class="tagrow">${modules.map((m) => `<span class="tag">module: ${esc(MODULE_NAMES[m] || m)}</span>`).join("")}</p>`;
    div.innerHTML = h;
    return div;
  }

  function exampleGloss(phi) {
    let expectingName = false;
    return phi.split(" ").map((token) => {
      const core = token.replace(/\.$/, "");
      const stop = token.endsWith(".") ? "." : "";
      const gloss = (glosses.get(core) || core).replace(/\s*\([^)]*\)/g, "");
      const isLabel = gloss === gloss.toUpperCase();
      const shown = expectingName && !isLabel ? core : gloss;
      if (core === "ne" || HONORIFIC_GLOSSES.has(gloss)) expectingName = true;
      else if (!isLabel) expectingName = false;
      if (stop) expectingName = false;
      return shown + stop;
    }).join(" ");
  }

  function updateWordFilters() {
    const disabled = $("f-field").value === REGISTERED_COMPOUNDS;
    for (const id of WORD_FILTERS) {
      if (disabled) $(id).value = "";
      $(id).disabled = disabled;
    }
  }

  function selectHasValue(id, value) {
    return [...$(id).options].some((option) => option.value === value);
  }

  function applyUrlState() {
    const params = new URLSearchParams(window.location.search);
    $("q").value = params.get("q") || "";
    const selections = [
      ["f-field", "field", "all"],
      ["f-pos", "pos", ""],
      ["f-domain", "domain", ""],
      ["f-module", "module", ""],
      ["f-pillar", "pillar", ""],
    ];
    for (const [id, key, fallback] of selections) {
      const requested = params.get(key);
      $(id).value = requested && selectHasValue(id, requested) ? requested : fallback;
    }
    updateWordFilters();
    const page = Number.parseInt(params.get("page"), 10);
    return Number.isFinite(page) && page > 0 ? page : 1;
  }

  function syncUrl(mode) {
    if (!mode) return;
    const params = new URLSearchParams();
    const q = $("q").value.trim();
    if (q) params.set("q", q);
    if ($("f-field").value !== "all") params.set("field", $("f-field").value);
    if ($("f-pos").value) params.set("pos", $("f-pos").value);
    if ($("f-domain").value) params.set("domain", $("f-domain").value);
    if ($("f-module").value) params.set("module", $("f-module").value);
    if ($("f-pillar").value) params.set("pillar", $("f-pillar").value);
    if (currentPage > 1) params.set("page", currentPage);

    const query = params.toString();
    const next = `${window.location.pathname}${query ? `?${query}` : ""}${window.location.hash}`;
    const here = `${window.location.pathname}${window.location.search}${window.location.hash}`;
    if (next === here) return;
    window.history[mode === "push" ? "pushState" : "replaceState"]({}, "", next);
  }

  // cross-reference clicks
  document.addEventListener("click", (ev) => {
    const w = ev.target?.dataset?.w;
    if (w) {
      $("q").value = w;
      $("f-field").value = "word";
      updateWordFilters();
      search({ historyMode: "push", moveFocus: true });
    }
  });

  // wiring
  let t;
  $("q").addEventListener("input", () => { clearTimeout(t); t = setTimeout(search, 120); });
  $("f-field").addEventListener("change", () => { updateWordFilters(); search(); });
  for (const id of WORD_FILTERS) $(id).addEventListener("change", search);
  $("clear").addEventListener("click", () => {
    $("q").value = "";
    $("f-field").value = "all";
    for (const id of WORD_FILTERS) $(id).value = "";
    updateWordFilters();
    search();
  });
  window.addEventListener("popstate", () => {
    clearTimeout(t);
    const page = applyUrlState();
    search({ page, historyMode: null });
  });
  const compactPages = window.matchMedia("(max-width: 560px)");
  const refreshPagination = () => {
    renderPagination($("pages-top"));
    renderPagination($("pages-bottom"));
  };
  if (compactPages.addEventListener) compactPages.addEventListener("change", refreshPagination);
  else compactPages.addListener(refreshPagination);
  document.addEventListener("keydown", (ev) => {
    if (ev.key === "/" && document.activeElement !== $("q")) { ev.preventDefault(); $("q").focus(); }
  });

  const initialPage = applyUrlState();
  search({ page: initialPage, historyMode: "replace" });
})();
