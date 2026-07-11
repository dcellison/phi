/* Phi lexicon explorer — read-only search over web/lexicon.json,
   with the compound registry (web/compounds.json) beside it */
(async function () {
  const $ = (id) => document.getElementById(id);
  const PAGE = 50;
  const BASE_VOCABULARY = "base-vocabulary";
  let lexicon = [], compounds = [], words = new Set(), shown = 0, current = [];

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
    $("status").textContent = "lexicon.json not found — run: python3 scripts/build_explorer.py";
    return;
  }
  try {
    compounds = await (await fetch("compounds.json")).json();
  } catch {
    compounds = []; // the explorer stands without the registry file
  }
  words = new Set(lexicon.map((e) => e.word));
  const compoundsOf = new Map();
  for (const c of compounds)
    for (const w of new Set(c.tokens)) {
      if (!compoundsOf.has(w)) compoundsOf.set(w, []);
      compoundsOf.get(w).push(c);
    }
  $("count").textContent = lexicon.length;

  // filter options from the data
  const opts = { pos: new Set(), tag: new Set(), module: new Set(), pillar: new Set() };
  for (const e of lexicon) {
    e.pos.forEach((p) => opts.pos.add(p));
    Object.keys(e.tags || {}).forEach((t) => opts.tag.add(t));
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
  fill($("f-tag"), opts.tag);
  fill($("f-module"), opts.module, (v) => MODULE_NAMES[v] || v);
  fill($("f-pillar"), opts.pillar, (v) => PILLAR_NAMES[v] || v);
  const requestedModule = new URLSearchParams(window.location.search).get("module");
  if (requestedModule === BASE_VOCABULARY || opts.module.has(requestedModule)) $("f-module").value = requestedModule;

  const esc = (s) => s.replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

  // wrap quoted Phi in .phi spans; clicking a known Phi word searches it
  const phiify = (s) =>
    esc(s).replace(/'([a-z][a-z .]*?)'/g, (m, inner) => {
      const tok = inner.replace(/\.$/, "");
      const link = words.has(tok) && !inner.includes(" ");
      return `<span class="phi"${link ? ` data-w="${tok}" role="link" tabindex="0"` : ""}>${inner}</span>`;
    });

  const score = (e, q) => {
    if (e.word === q || e.gloss.toLowerCase() === q) return 0;
    if (e.word.startsWith(q)) return 1;
    if (e.gloss.toLowerCase().includes(q)) return 2;
    if (e.word.includes(q)) return 3;
    if (e.concept.toLowerCase().includes(q)) return 4;
    if (e.description.toLowerCase().includes(q)) return 5;
    if ((e.grammatical_notes || "").toLowerCase().includes(q)) return 6;
    return -1;
  };

  const compScore = (c, q) => {
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

  function search() {
    const q = $("q").value.trim().toLowerCase();
    const fp = $("f-pos").value, ft = $("f-tag").value;
    const fm = $("f-module").value, fl = $("f-pillar").value;
    current = lexicon
      .map((e) => ({ e, s: q ? score(e, q) : 7 }))
      .filter(({ e, s }) =>
        s >= 0 &&
        (!fp || e.pos.includes(fp)) &&
        (!ft || (e.tags && ft in e.tags)) &&
        (!fm || (fm === BASE_VOCABULARY ? (e.modules || []).length === 0 : (e.modules || []).includes(fm))) &&
        (!fl || (e.pillars && fl in e.pillars)))
      .sort((a, b) => a.s - b.s || a.e.word.localeCompare(b.e.word))
      .map(({ e }) => e);
    // registered compounds answer plain searches; the filters are word facets
    const compMatches = (q && !fp && !ft && !fm && !fl)
      ? compounds
          .map((c) => ({ c, s: compScore(c, q) }))
          .filter(({ s }) => s >= 0)
          .sort((a, b) => a.s - b.s || a.c.compound.localeCompare(b.c.compound))
          .map(({ c }) => c)
      : [];
    const wordCount = `${current.length} ${current.length === 1 ? "word" : "words"}`;
    $("status").textContent =
      current.length === lexicon.length ? "" :
      current.length === 0 && compMatches.length === 0 ? "nothing found — the lexicon may simply not have it yet" :
      compMatches.length === 0 ? wordCount :
      `${wordCount}, ${compMatches.length} ${compMatches.length === 1 ? "compound" : "compounds"}`;
    $("results").innerHTML = "";
    shown = 0;
    for (const c of compMatches) $("results").appendChild(compRow(c));
    renderMore();
  }

  function renderMore() {
    const slice = current.slice(shown, shown + PAGE);
    shown += slice.length;
    const frag = document.createDocumentFragment();
    for (const e of slice) frag.appendChild(row(e));
    $("results").appendChild(frag);
    $("more").hidden = shown >= current.length;
  }

  function row(e) {
    const li = document.createElement("li");
    const head = document.createElement("button");
    head.className = "entry-head";
    head.setAttribute("aria-expanded", "false");
    head.innerHTML =
      `<span class="w">${esc(e.word)}</span>` +
      `<span class="g">${esc(e.gloss)}</span>` +
      `<span class="pos">${e.pos.join(" · ")}</span>` +
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

  function body(e) {
    const div = document.createElement("div");
    div.className = "entry-body";
    let h = `<p class="concept">${esc(e.concept)}</p>`;
    h += `<p>${phiify(e.description)}</p>`;
    if (e.pos.includes("verb") && !e.pos.includes("noun"))
      h += `<p class="rule-note">Also its own noun, the act or its result, by the event-noun rule.</p>`;
    if (e.sound_symbolism) h += `<h3>Sound</h3><p>${phiify(e.sound_symbolism)}</p>`;
    if (e.grammatical_notes) h += `<h3>Usage</h3><p>${phiify(e.grammatical_notes)}</p>`;
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
    const tags = Object.keys(e.tags || {});
    if (tags.length)
      h += `<p class="tagrow">${tags.map((t) => `<span class="tag">${esc(t)}</span>`).join("")}</p>`;
    const modules = e.modules || [];
    if (modules.length)
      h += `<p class="tagrow">${modules.map((m) => `<span class="tag">module: ${esc(MODULE_NAMES[m] || m)}</span>`).join("")}</p>`;
    div.innerHTML = h;
    return div;
  }

  // cross-reference clicks
  document.addEventListener("click", (ev) => {
    const w = ev.target?.dataset?.w;
    if (w) { $("q").value = w; search(); window.scrollTo({ top: 0, behavior: "smooth" }); }
  });

  // wiring
  let t;
  $("q").addEventListener("input", () => { clearTimeout(t); t = setTimeout(search, 120); });
  for (const id of ["f-pos", "f-tag", "f-module", "f-pillar"]) $(id).addEventListener("change", search);
  $("clear").addEventListener("click", () => {
    $("q").value = ""; for (const id of ["f-pos", "f-tag", "f-module", "f-pillar"]) $(id).value = "";
    search();
  });
  $("more").addEventListener("click", renderMore);
  document.addEventListener("keydown", (ev) => {
    if (ev.key === "/" && document.activeElement !== $("q")) { ev.preventDefault(); $("q").focus(); }
  });

  search();
})();
