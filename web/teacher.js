/* The transmutation teacher: a deterministic pattern engine over the
   lexicon and the primer's taught patterns (documents/taught_patterns.md).
   No model runs here — every step is a rule, authored and reviewed like
   everything else in the repository, so every step can be explained. */

"use strict";

/* ---------------- index building ---------------- */

function buildIndex(lexicon, cfg) {
  const byGloss = new Map();   // english gloss -> entry
  const byWord = new Map();    // phi word -> entry
  for (const e of lexicon) {
    byWord.set(e.word, e);
    const g = e.gloss.replace(/\s*\(.*?\)/g, "").trim().toLowerCase();
    if (!byGloss.has(g)) byGloss.set(g, e);
  }
  const clfOf = {};
  for (const [clf, words] of Object.entries(cfg.classifier_kinds))
    for (const w of words) clfOf[w] = clf;
  return { byGloss, byWord, clfOf, cfg };
}

function lookup(ix, en) {
  // english token -> lexicon entry, via verb forms and aliases
  let w = en.toLowerCase();
  if (ix.cfg.verb_forms[w]) w = ix.cfg.verb_forms[w];
  if (ix.cfg.aliases[w]) w = ix.cfg.aliases[w];
  if (ix.cfg.verb_forms[w]) w = ix.cfg.verb_forms[w];
  return ix.byGloss.get(w) || null;
}

function isVerb(ix, en) {
  const e = lookup(ix, en);
  return e && e.pos.includes("verb");
}
function isAdj(ix, en) {
  const e = lookup(ix, en);
  return e && e.pos.includes("adjective");
}
function isNoun(ix, en) {
  const e = lookup(ix, en);
  return e && e.pos.includes("noun");
}
/* ---------------- gloss lines ---------------- */

function glossToken(ix, phiTok, prevTok) {
  const core = phiTok.replace(/[.]/g, "");
  if (prevTok === "ne") return phiTok;              // a name glosses as itself
  const e = ix.byWord.get(core);
  if (!e) return phiTok;                            // carried names
  let g = e.gloss.replace(/\s*\(.*?\)/g, "").trim();
  return phiTok.endsWith(".") ? g + "." : g;
}

function glossLine(ix, phi) {
  const toks = phi.split(/\s+/);
  const out = [];
  let prev = null;
  for (const t of toks) {
    out.push(glossToken(ix, t, prev));
    prev = t.replace(/[.]/g, "");
  }
  return out.join(" ");
}

/* ---------------- the pipeline ---------------- */

const SLOT1_RANK = { to: 1, so: 1, si: 2, ki: 2, te: 2, pa: 2, ro: 2,
                     se: 3, ka: 3, hi: 4, ke: 4, ti: 4, ho: 4,
                     po: 5, na: 5, ma: 6 };

function transmute(text, ix) {
  const trace = [];
  const original = text.trim();
  let t = original.toLowerCase().replace(/[""]/g, '"');

  // punctuation
  const isQuestion = /\?\s*$/.test(t);
  if (/!\s*$/.test(t))
    trace.push(["The exclamation, worded",
      "Phi has one written mark: the period. Urgency is carried by short words, not loud marks — see the pamphlet Punctuation you can hear. The sentence keeps its calm period."]);
  if (t.includes(","))
    trace.push(["No commas", "Phi speaks its punctuation. The comma's work is done by word order and the small announcing words."]);
  t = t.replace(/[?!.,]/g, " ").replace(/\s+/g, " ").trim();

  // idioms first — the teaching moments
  for (const idiom of ix.cfg.idioms) {
    if (t === idiom.en) {
      trace.push(["A Phi idiom", idiom.note]);
      return { ok: true, phi: idiom.phi, gloss: idiom.gloss, trace, original };
    }
  }

  // refusals
  const words0 = t.split(" ");
  for (const r of ix.cfg.refusals) {
    const hit = words0.find(w => r.words.includes(w));
    if (hit) {
      return { ok: false, refusal: hit, teach: r.teach, trace, original };
    }
  }

  let words = words0.slice();

  // politeness
  let polite = false;
  if (words[0] === "please") { polite = true; words.shift();
    trace.push(["Politeness first (P14)", "please becomes pi, standing at the very front — respect is announced before anything else, even before the question."]); }

  // negative imperative: a ruled empty cell
  if ((words[0] === "don't" || (words[0] === "do" && words[1] === "not")) ) {
    return { ok: false, refusal: "the negative command", trace, original,
      teach: "Phi has never issued a negative command — the interaction tables rule the no + ma cell empty. The household warns with teo. (watch out) or states the harm plainly: name what the action would hurt." };
  }

  // conditionals
  if (words[0] === "if") {
    return conditional(words.slice(1), ix, trace, original, polite);
  }

  // embedded statement / question
  const thatIdx = words.indexOf("that");
  const whetherIdx = words.indexOf("whether");
  if (whetherIdx > 0 || thatIdx > 0) {
    const r = embedded(words, thatIdx, whetherIdx, ix, trace, original, polite, isQuestion);
    if (r) return r;
  }

  // plain question: trailing ? or aux inversion
  let question = isQuestion;
  const INVERT = ["is", "are", "am", "was", "were", "do", "does", "did", "will", "can", "may", "must"];
  if (!question && INVERT.includes(words[0]) && words.length > 1) question = true;
  if (question && INVERT.includes(words[0])) {
    // de-invert: move the auxiliary after the subject noun phrase
    const aux = words.shift();
    let i = 0;
    while (i < words.length && !isVerb(ix, words[i]) && words[i] !== "not") i++;
    words.splice(i, 0, aux);
  }
  if (question)
    trace.push(["The plain question (P09)", "wa stands before the sentence and nothing else moves — the question is announced, then the sentence arrives unchanged."]);

  // imperative: verb-first, no question
  let imperative = false;
  if (!question && words.length && isVerb(ix, words[0]) && !isNoun(ix, words[0])) {
    imperative = true;
    trace.push(["The gentle imperative (P27)", "A request-to-do begins with no and has no subject — the sentence is handed to whoever is listening."]);
  }

  const clause = parseClause(words, ix, trace, { imperative });
  if (!clause) return unknownFallback(words, ix, trace, original);
  if (clause.doubleObject) return { ok: false, trace, original, refusal: null,
    teach: "Phi announces the receiver before the gift: wei stands before the one who receives (P19). Say it with to — give the flower to the child — and the teacher can show you the giving-sentence." };
  if (clause.unknown.length) return unknownFallback(words, ix, trace, original, clause.unknown);

  const slot0 = [];
  if (polite) slot0.push("pi");
  if (question) slot0.push("wa");
  if (imperative) slot0.push("no");

  const phi = assemble(slot0, clause);
  trace.push(["Announce, then deliver",
    "Final order: " + orderStory(slot0, clause) + " — every element that modifies or relates comes before what it affects, and the verb closes the door."]);
  return { ok: true, phi, gloss: glossLine(ix, phi), trace, original };
}

function conditional(rest, ix, trace, original, polite) {
  // split condition / consequence at "then" or mid-sentence pronoun start
  let condWords, consWords;
  const thenIdx = rest.indexOf("then");
  if (thenIdx > 0) { condWords = rest.slice(0, thenIdx); consWords = rest.slice(thenIdx + 1); }
  else return { ok: false, trace, original,
    teach: "Write the condition and the consequence with a comma or then between them — if rain falls, then we rest — and the teacher can bracket them. (Commas vanish in Phi; the two sentences stand side by side.)",
    refusal: null };
  const irrealis = condWords.includes("were") || consWords.includes("would");
  if (irrealis) {
    condWords = condWords.map(w => (w === "were" ? "is" : w));
    consWords = consWords.filter(w => w !== "would");
    trace.push(["The unreal if (P36)", "were and would mark a wish or a never-was: lu takes he, the particle of the unreal — one extra syllable buys the whole kingdom of the imagination."]);
  } else {
    trace.push(["If (P35)", "The condition comes first as its own small sentence opened by lu; the consequence follows. Announce the door, then walk through it."]);
  }
  const c1 = parseClause(condWords, ix, trace, {});
  const c2 = parseClause(consWords, ix, trace, {});
  if (!c1 || !c2) return unknownFallback(rest, ix, trace, original);
  if (c1.unknown.length || c2.unknown.length)
    return unknownFallback(rest, ix, trace, original, c1.unknown.concat(c2 ? c2.unknown : []));
  const phi = assemble(irrealis ? ["lu", "he"] : ["lu"], c1) + " " + assemble([], c2);
  return { ok: true, phi, gloss: glossLine(ix, phi), trace, original };
}

function embedded(words, thatIdx, whetherIdx, ix, trace, original, polite, isQuestion) {
  const idx = whetherIdx > 0 ? whetherIdx : thatIdx;
  const opener = whetherIdx > 0 ? "wela" : "mena";
  const closer = whetherIdx > 0 ? "welo" : "meno";
  const left = words.slice(0, idx);
  const inner = words.slice(idx + 1);
  const mat = parseClause(left, ix, trace, { silent: true });
  const inn = parseClause(inner, ix, trace, { silent: true });
  if (!mat || !inn || !mat.verb || !inn.verb) return null;
  if (mat.unknown.length || inn.unknown.length)
    return unknownFallback(words, ix, trace, original, mat.unknown.concat(inn.unknown));
  trace.push([whetherIdx > 0 ? "The embedded question (P32)" : "The embedded statement (P31)",
    (whetherIdx > 0
      ? "wela … welo brackets a question held without asking — Phi is precise about which question one cannot answer."
      : "mena … meno brackets a whole sentence into a thing that can be known, said, or felt.")
    + " The inner sentence keeps its own tense; the closer exists so the two verbs never collide."]);
  const innerPhi = assemble([], inn).replace(/\.$/, "");
  const slot0 = [];
  if (polite) slot0.push("pi");
  if (isQuestion) slot0.push("wa");
  const phi = (slot0.length ? slot0.join(" ") + " " : "")
    + mat.subject.join(" ") + (mat.subject.length ? " " : "")
    + opener + " " + innerPhi + " " + closer
    + (mat.slot1.length ? " " + mat.slot1.map(s => s[0]).join(" ") : "")
    + " " + mat.verb + ".";
  trace.push(["Announce, then deliver",
    "The bracketed thought stands where an object stands — before the main verb, which closes the sentence."]);
  return { ok: true, phi, gloss: glossLine(ix, phi), trace, original };
}

/* parseClause: one simple clause -> {subject:[], pps:[], object:[], slot1:[[particle, why]], manner:[], verb, predicate, unknown:[]} */
function parseClause(words, ix, trace, opts) {
  const c = { subject: [], pps: [], object: [], slot1: [], manner: [], verb: null,
              predicate: null, unknown: [], also: false };
  const say = (title, body) => { if (!opts.silent) trace.push([title, body]); };
  let i = 0;
  let sawVerb = false;
  let copula = null;
  let expectNP = opts.imperative ? "object" : "subject";

  const np = (target) => {
    // consume one noun phrase into target ([] of phi tokens)
    const out = [];
    let consumed = false;
    let counted = false;
    while (i < words.length) {
      const w = words[i];
      if (w === "the" || w === "a" || w === "an") {
        say("No articles", "Phi has no the or a — the noun stands alone, and shared attention does the pointing (manual ch. 13, the zero-article system).");
        i++; consumed = true; continue;
      }
      if (w === "all" || w === "every") { out.push("theula");
        say("All (P07)", "theula before a noun gathers every one of its kind."); i++; consumed = true; continue; }
      if (w === "no" || w === "none") { out.push("mawha");
        say("None (P07)", "mawha before a noun empties it the way lo fills it."); i++; consumed = true; continue; }
      if (w === "one" || w === "two" || w === "three") {
        const num = w === "one" ? "ta" : w === "two" ? "wi" : "ta shao";
        const head = words[i + 1] ? lookup(ix, words[i + 1].replace(/s$/, "")) : null;
        const clf = head ? (ix.clfOf[head.word] || "themo") : "themo";
        out.push(num, clf);
        counted = true;
        say("Counting (P08)", `Number, then kind, then thing: ${num} ${clf} — the classifier names what nature of thing is being counted (people himo, living things lipha, objects themo, ideas nophe). It is optional, and it is good manners toward the things counted.`);
        i++; consumed = true; continue;
      }
      if (ix.cfg.pronouns[w]) {
        const p = ix.cfg.pronouns[w];
        out.push(...p.split(" "));
        if (w === "we" || w === "us" || w === "our")
          say("The many-I", "lo mia — many-I — is how Phi says we: the plural particle owned since chapter 3, set before I.");
        if (["he", "she", "him", "her", "his"].includes(w))
          say("One third person", "Phi has a single, ungendered third person: shia. He and she arrive at the same word, by design.");
        if (["my", "your", "our", "their", "his", "her"].includes(w))
          say("Possession (P06)", "The owner stands directly before the owned — no of, no apostrophe; position is the whole grammar.");
        i++; consumed = true; continue;
      }
      if (w.endsWith("'s")) {
        const owner = lookup(ix, w.slice(0, -2));
        if (owner) { out.push(owner.word);
          say("Possession (P06)", "The owner stands directly before the owned — no of, no apostrophe; position is the whole grammar.");
          i++; consumed = true; continue; }
      }
      if (isAdj(ix, w) && words[i + 1] && (isNoun(ix, words[i + 1]) || isNoun(ix, words[i + 1].replace(/s$/, "")))) {
        out.push(lookup(ix, w).word);
        say("The describer before the noun (P05)", "The quality is announced before the thing: " + lookup(ix, w).word + " stands before its noun.");
        i++; consumed = true; continue;
      }
      // head noun (with plural)
      let e = lookup(ix, w);
      if (!e && /s$/.test(w)) {
        e = lookup(ix, w.replace(/s$/, ""));
        if (e && e.pos.includes("noun")) {
          if (!counted) { out.push("lo");
            say("Plural (P04)", "lo before the noun makes it many — one small word, and the garden fills with wings."); }
          else say("Counted plural", "The number already carries the many — lo is not needed beside ta, wi, or shao.");
        }
      }
      if (e && (e.pos.includes("noun") || e.pos.includes("adjective"))) {
        out.push(e.word); i++; consumed = true; break;
      }
      // a name: capitalized in the original, or simply unknown here
      break;
    }
    return consumed ? out : null;
  };

  while (i < words.length) {
    const w = words[i];

    // prepositions open a place/receiver phrase
    if (["in", "at", "on", "from", "to", "toward", "into", "for"].includes(w)) {
      const prep = w;
      i++;
      const obj = np("pp");
      if (!obj) { c.unknown.push(prep); continue; }
      let phiPrep, why;
      if (["in", "at", "on"].includes(prep)) { phiPrep = "mua"; why = "mua announces that a place is coming — one word covers in, at, and on, and the things themselves tell you which (P16)."; }
      else if (prep === "from") { phiPrep = "lue"; why = "lue announces the source before the leaving is said (P18)."; }
      else if (prep === "for" || (["to", "toward", "into"].includes(prep) && c.verbEn && ["give", "tell", "share", "send"].includes(c.verbEn))) {
        phiPrep = "wei"; why = "wei announces the receiver before the gift changes hands — the giving-sentence, Phi's favorite (P19).";
      } else { phiPrep = "kau"; why = "kau announces the destination before anyone takes a step (P20)."; }
      c.pps.push([phiPrep, ...obj]);
      say("The relation announced", why);
      continue;
    }

    // auxiliaries and small structure words
    if (w === "will") { c.slot1.push(["so", "P22"]); say("Future (P22)", "will becomes so, touching the verb: the doing is announced as still ahead."); i++; continue; }
    if (w === "did") { c.slot1.push(["to", "P21"]); say("Past (P21)", "did carries the past: to steps in before the verb, a small backward step."); i++; continue; }
    if (w === "do" || w === "does") { i++; continue; }
    if (["is", "are", "am", "was", "were"].includes(w)) {
      copula = w; if (w === "was" || w === "were") c.slot1.push(["to", "P21"]);
      i++; continue;
    }
    if (w === "has" || w === "have" || w === "had") {
      if (w === "had") c.slot1.push(["to", "P21"]);
      c.slot1.push(["ki", "P23"]); say("Aspect (P23)", "have done becomes ki: the doing announced as complete, the tools set down.");
      i++; continue;
    }
    if (w === "not" || w === "n't") { c.slot1.push(["ma", "P26"]);
      say("Not (P26)", "ma stands after the time particles, touching the verb — one particle, and the sentence becomes its shadow."); i++; continue; }
    if (w === "may" || w === "can") { c.slot1.push(["po", "P28"]);
      say("May (P28)", "po before the verb opens a door: may, can."); i++; continue; }
    if (w === "cannot" || w === "can't") { c.slot1.push(["po", "P28"], ["ma", "P26"]);
      say("Cannot (P28)", "po ma — the opened door, turned around. The stack keeps canon order: modality before negation."); i++; continue; }
    if (w === "must") { c.slot1.push(["na", "P28"]);
      say("Must (P28)", "na before the verb holds: must — Phi saves it for the rules that matter."); i++; continue; }
    if (w === "always") { c.slot1.push(["ro", "P23"]);
      say("Habit (P23)", "always becomes ro, the habitual — the way a household breathes."); i++; continue; }
    if ((w === "begins" || w === "began" || w === "starts" || w === "started") && words[i + 1] === "to") {
      if (w === "began" || w === "started") c.slot1.push(["to", "P21"]);
      c.slot1.push(["pa", "P23"]); say("Beginning (P23)", "begins to becomes pa: the doing caught at its edge — the first note, not the song.");
      i += 2; continue; }
    if (w === "stops" || w === "stopped") {
      if (w === "stopped") c.slot1.push(["to", "P21"]);
      c.slot1.push(["te", "P23"]); say("Ceasing (P23)", "stops becomes te, the gentlest stop in the language: not finished, just no longer happening.");
      i++; continue; }
    if (w === "also" || w === "too") { c.also = true;
      say("Also (P15)", "we — also — stands before the thing it adds."); i++; continue; }
    if (w === "together") { c.manner.push("nuawe");
      say("Together (P30)", "nuawe is togetherness as manner, standing before the verb: the doing done as more than one."); i++; continue; }
    if (w === "here" || w === "there") {
      c.predicate = [w === "here" ? "ha" : "ra"];
      say("Here and there (P17)", "ha and ra stand alone as locative predicates with nai."); i++; continue; }

    // manner adverbs
    const adv = ix.cfg.aliases[w] && isAdj(ix, ix.cfg.aliases[w]) ? ix.cfg.aliases[w]
      : (/ly$/.test(w) && isAdj(ix, w.replace(/ly$/, "")) ? w.replace(/ly$/, "") : null);
    if (adv && (sawVerb || words.slice(i + 1).some(x => isVerb(ix, x)))) {
      c.manner.push(lookup(ix, adv).word);
      say("Manner (P24)", "A describing word before a doing describes the doing — it stands inside the particle block, immediately before the verb, so the verb phrase takes the noun phrase's shape.");
      i++; continue;
    }

    // the verb
    if (!sawVerb && !copula && isVerb(ix, w) && (expectNP !== "subject" || c.subject.length)) {
      const e = lookup(ix, w);
      c.verb = e.word; c.verbEn = ix.cfg.verb_forms[w] || ix.cfg.aliases[w] || w;
      const lw = w.toLowerCase();
      const base = ix.cfg.verb_forms[lw] || (ix.cfg.aliases[lw] ? (ix.cfg.verb_forms[ix.cfg.aliases[lw]] || ix.cfg.aliases[lw]) : lw);
      const isPast = ix.cfg.verb_forms[lw] && !/(s|ing)$/.test(lw) && lw !== base;
      const isIng = /ing$/.test(lw) && lw !== base;
      if (isPast && !c.slot1.some(s => s[0] === "to") && !c.slot1.some(s => s[0] === "ki")) {
        c.slot1.push(["to", "P21"]);
        say("Past (P21)", `${w} is a past form: to steps in before the verb — a small backward step, taken right where Phi keeps the truth about time.`);
      }
      if (isIng && !c.slot1.some(s => s[0] === "si")) c.slot1.push(["si", "P23"]);
      sawVerb = true; i++; expectNP = "object"; continue;
    }
    if (copula && (isVerb(ix, w) && /ing$/.test(w))) {
      // is walking -> si walk
      c.slot1.push(["si", "P23"]);
      say("Ongoing (P23)", "is …-ing becomes si: the doing held open, still unfolding as you speak.");
      const e = lookup(ix, w); c.verb = e.word; sawVerb = true; copula = null; i++; continue;
    }

    // noun phrases: subject then object; adjectives after copula are predicates
    if (copula && (isAdj(ix, w) || isNoun(ix, w))) {
      const e = lookup(ix, w);
      c.predicate = [e.word];
      say("Predication (P01)", "The quiet is of Phi is nai, and it arrives last — after you already know what is being said about what.");
      i++; continue;
    }
    const phrase = np(expectNP);
    if (phrase) {
      if (expectNP === "subject" && !sawVerb && !copula) { c.subject.push(...phrase); }
      else {
        if (sawVerb && c.object.length) { c.doubleObject = true; }
        c.object.push(...phrase);
      }
      continue;
    }

    c.unknown.push(w);
    i++;
  }

  if (copula && !c.verb && !c.predicate && c.object.length) {
    c.predicate = c.object.splice(0);
  }
  if (copula && !c.verb) c.isNai = true;
  if (copula && c.predicate)
    void 0;
  if (!c.verb && !c.isNai && !opts.silent && !c.predicate) return c.unknown.length ? c : null;
  return c;
}

function assemble(slot0, c) {
  const rank = (p) => SLOT1_RANK[p] || 9;
  const slot1 = c.slot1.map(s => s[0]).sort((a, b) => rank(a) - rank(b));
  const parts = [];
  parts.push(...slot0);
  if (c.also) parts.push("we");
  parts.push(...c.subject);
  for (const pp of c.pps) parts.push(...pp);
  parts.push(...c.object);
  if (c.isNai || c.predicate) {
    if (c.predicate) parts.push(...c.predicate);
    parts.push(...slot1);
    parts.push("nai");
  } else {
    parts.push(...slot1);
    parts.push(...c.manner);
    parts.push(c.verb);
  }
  return parts.join(" ") + ".";
}

function orderStory(slot0, c) {
  const bits = [];
  if (slot0.length) bits.push("the frame (" + slot0.join(" ") + ")");
  if (c.subject.length) bits.push("the doer");
  if (c.pps.length) bits.push("the announced relations");
  if (c.object.length) bits.push("the acted-on");
  if (c.slot1.length) bits.push("the particle stack in canon order");
  if (c.manner.length) bits.push("the manner");
  bits.push(c.isNai || c.predicate ? "nai" : "the verb");
  return bits.join(", then ");
}

function unknownFallback(words, ix, trace, original, unknown) {
  const rows = [];
  for (const w of words) {
    const e = lookup(ix, w) || lookup(ix, w.replace(/s$/, ""));
    rows.push([w, e ? e.word : "—", e ? e.gloss.replace(/\s*\(.*?\)/g, "") : "not in the lexicon, or not yet taught to this teacher"]);
  }
  return { ok: false, partial: true, rows, trace, original,
    teach: "This sentence needs a human transmuter — the teacher only demonstrates the primer's taught patterns, and transmutation itself is judgment, not lookup. Here is what it recognizes, word by word; the lexicon holds the rest." };
}

/* ---------------- page wiring ---------------- */

if (typeof document !== "undefined") (async function () {
  const [lexicon, cfg] = await Promise.all([
    fetch("lexicon.json").then(r => r.json()),
    fetch("teacher_patterns.json").then(r => r.json()),
  ]);
  const ix = buildIndex(lexicon, cfg);
  let tengwarWords = null;

  const $ = (id) => document.getElementById(id);
  const input = $("q"), out = $("out");

  function esc(s) { return s.replace(/&/g, "&amp;").replace(/</g, "&lt;"); }

  async function tengwarLine(phi) {
    if (!tengwarWords)
      tengwarWords = await fetch("tengwar_words.json").then(r => r.json()).catch(() => ({}));
    const spans = [];
    for (const tok of phi.split(/\s+/)) {
      const core = tok.replace(/\./g, "");
      const svg = tengwarWords[core];
      spans.push(svg ? svg : `<span class="rom">${esc(core)}</span>`);
      if (tok.endsWith(".") && tengwarWords["."]) spans.push(tengwarWords["."]);
    }
    return spans.join(" ");
  }

  async function show(res) {
    let html = "";
    if (res.ok) {
      html += `<div class="panel"><h3>Phi</h3><p class="phi-out">${esc(res.phi)}</p></div>`;
      html += `<div class="panel"><h3>gloss</h3><p class="gloss-out">${esc(res.gloss)}</p></div>`;
      html += `<div class="panel"><h3>the original</h3><p>${esc(res.original)}</p></div>`;
      html += `<div class="panel"><h3>tengwar</h3><p class="teng-out">${await tengwarLine(res.phi)}</p></div>`;
      html += `<div class="panel dim"><h3>glyph blocks</h3><p>The Mayan-inspired glyph block system is still being designed in the workshop. This panel is waiting for it.</p></div>`;
    } else if (res.teach && !res.partial) {
      html += `<div class="panel refusal"><h3>Phi declines${res.refusal ? " — " + esc(res.refusal) : ""}</h3><p>${esc(res.teach)}</p></div>`;
    } else if (res.partial) {
      html += `<div class="panel"><h3>word by word</h3><p>${esc(res.teach)}</p><table><tr><th>English</th><th>Phi</th><th>gloss</th></tr>`;
      for (const [en, phi, g] of res.rows)
        html += `<tr><td>${esc(en)}</td><td>${esc(phi)}</td><td>${esc(g)}</td></tr>`;
      html += `</table></div>`;
    }
    if (res.trace && res.trace.length) {
      html += `<div class="panel"><h3>how the transmutation was done</h3><ol class="trace">`;
      for (const [title, body] of res.trace)
        html += `<li><strong>${esc(title)}.</strong> ${esc(body)}</li>`;
      html += `</ol></div>`;
    }
    out.innerHTML = html;
  }

  $("go").addEventListener("click", () => show(transmute(input.value, ix)));
  input.addEventListener("keydown", (e) => { if (e.key === "Enter") show(transmute(input.value, ix)); });

  for (const chip of document.querySelectorAll(".chip"))
    chip.addEventListener("click", () => { input.value = chip.textContent; show(transmute(chip.textContent, ix)); });

  // the pattern browser
  const pb = $("patterns");
  let phtml = "";
  for (const p of cfg.patterns) {
    phtml += `<details><summary><strong>${p.id}</strong> · ${esc(p.name)} <span class="shape">${esc(p.shape)}</span></summary>` +
      `<pre>${esc(p.phi)}\n${esc(p.gloss)}\n(${esc(p.en)})</pre>` +
      `<p class="dim">Taught in primer chapter ${p.ch}.</p></details>`;
  }
  pb.innerHTML = phtml;
})();

if (typeof module !== "undefined") module.exports = { buildIndex, transmute, glossLine };
