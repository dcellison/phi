/* Phi lexicon explorer — phase one: read-only search over web/lexicon.json */
(async function () {
  const $ = (id) => document.getElementById(id);
  const PAGE = 50;
  let lexicon = [], words = new Set(), shown = 0, current = [];

  const PILLAR_NAMES = {
    "solarpunk-values": "solarpunk",
    "secular-buddhist-philosophy": "secular buddhist",
    "art-nouveau-aesthetics": "art nouveau",
    "peace-linguistics-practices": "peace linguistics",
    "pre-industrial-wisdom": "pre-industrial wisdom",
  };

  try {
    lexicon = await (await fetch("lexicon.json")).json();
  } catch {
    $("status").textContent = "lexicon.json not found — run: python3 scripts/build_explorer.py";
    return;
  }
  words = new Set(lexicon.map((e) => e.word));
  $("count").textContent = lexicon.length;

  // filter options from the data
  const opts = { pos: new Set(), tag: new Set(), pillar: new Set() };
  for (const e of lexicon) {
    e.pos.forEach((p) => opts.pos.add(p));
    Object.keys(e.tags || {}).forEach((t) => opts.tag.add(t));
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
  fill($("f-pillar"), opts.pillar, (v) => PILLAR_NAMES[v] || v);

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

  function search() {
    const q = $("q").value.trim().toLowerCase();
    const fp = $("f-pos").value, ft = $("f-tag").value, fl = $("f-pillar").value;
    current = lexicon
      .map((e) => ({ e, s: q ? score(e, q) : 7 }))
      .filter(({ e, s }) =>
        s >= 0 &&
        (!fp || e.pos.includes(fp)) &&
        (!ft || (e.tags && ft in e.tags)) &&
        (!fl || (e.pillars && fl in e.pillars)))
      .sort((a, b) => a.s - b.s || a.e.word.localeCompare(b.e.word))
      .map(({ e }) => e);
    $("status").textContent =
      current.length === lexicon.length ? "" :
      current.length === 0 ? "nothing found — the lexicon may simply not have it yet" :
      `${current.length} ${current.length === 1 ? "word" : "words"}`;
    $("results").innerHTML = "";
    shown = 0;
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

  function body(e) {
    const div = document.createElement("div");
    div.className = "entry-body";
    let h = `<p class="concept">${esc(e.concept)}</p>`;
    h += `<p>${phiify(e.description)}</p>`;
    if (e.pos.includes("verb") && !e.pos.includes("noun"))
      h += `<p class="rule-note">Also its own noun, the act or its result, by the event-noun rule.</p>`;
    if (e.sound_symbolism) h += `<h3>Sound</h3><p>${phiify(e.sound_symbolism)}</p>`;
    if (e.grammatical_notes) h += `<h3>Usage</h3><p>${phiify(e.grammatical_notes)}</p>`;
    const pillars = Object.entries(e.pillars || {});
    if (pillars.length) {
      h += `<h3>Pillars</h3>`;
      for (const [k, v] of pillars)
        h += `<p class="pillar"><b>${esc(PILLAR_NAMES[k] || k)}</b>${phiify(v)}</p>`;
    }
    const tags = Object.keys(e.tags || {});
    if (tags.length)
      h += `<p class="tagrow">${tags.map((t) => `<span class="tag">${esc(t)}</span>`).join("")}</p>`;
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
  for (const id of ["f-pos", "f-tag", "f-pillar"]) $(id).addEventListener("change", search);
  $("clear").addEventListener("click", () => {
    $("q").value = ""; for (const id of ["f-pos", "f-tag", "f-pillar"]) $(id).value = "";
    search();
  });
  $("more").addEventListener("click", renderMore);
  document.addEventListener("keydown", (ev) => {
    if (ev.key === "/" && document.activeElement !== $("q")) { ev.preventDefault(); $("q").focus(); }
  });

  search();
})();
