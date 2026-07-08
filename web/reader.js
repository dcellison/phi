/* Reading memory for the manual, primer, texts, and pamphlets:
   remembers where you left off in each section, and lets you bookmark
   any heading. Everything lives in this browser's localStorage, like
   the theme choice; nothing is sent anywhere. */
(function () {
  "use strict";

  var SECTIONS = { manual: 1, primer: 1, texts: 1, pamphlets: 1 };

  var parts = location.pathname.split("/").filter(function (p) { return p; });
  var file = parts[parts.length - 1] || "index.html";
  var section = parts[parts.length - 2] || "";
  if (!/\.html$/.test(file)) { section = file; file = "index.html"; }
  if (!SECTIONS[section]) return;

  var isHome = file === "index.html";
  var POS_KEY = "phi-reader-pos:" + section;
  var MARKS_KEY = "phi-reader-marks";

  function load(key, fallback) {
    try {
      var v = localStorage.getItem(key);
      return v ? JSON.parse(v) : fallback;
    } catch (e) { return fallback; }
  }
  function store(key, value) {
    try { localStorage.setItem(key, JSON.stringify(value)); } catch (e) {}
  }
  function marks() { return load(MARKS_KEY, []); }
  function pageTitle() {
    var t = document.title;
    var i = t.indexOf("—");
    return i >= 0 ? t.slice(i + 1).trim() : t;
  }
  function slugify(text) {
    var s = text.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "");
    return s.slice(0, 60) || "section";
  }
  function esc(s) {
    return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;")
      .replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }
  function markIndex(list, f, id) {
    for (var i = 0; i < list.length; i++) {
      if (list[i].section === section && list[i].file === f && list[i].id === id) return i;
    }
    return -1;
  }

  document.addEventListener("DOMContentLoaded", function () {
    var main = document.querySelector("main");
    if (!main) return;
    if (isHome) homePage(main); else contentPage(main);
  });

  /* ---- content pages: stable heading ids, bookmark buttons, and
     a remembered reading position ---- */

  function contentPage(main) {
    var headings = main.querySelectorAll("h1, h2, h3");
    var used = {};
    Array.prototype.forEach.call(headings, function (h) {
      var text = h.textContent.trim();
      if (!h.id) {
        var base = slugify(text);
        var id = base, n = 2;
        while (used[id] || document.getElementById(id)) id = base + "-" + n++;
        h.id = id;
      }
      used[h.id] = true;
      addMarkButton(h, text);
    });

    glossPopovers(main);

    /* anchors exist only now, so do the jump the browser could not */
    if (location.hash) {
      var target = document.getElementById(location.hash.slice(1));
      if (target) target.scrollIntoView();
    } else {
      var pos = load(POS_KEY, null);
      if (pos && pos.file === file && pos.y > 40) window.scrollTo(0, pos.y);
    }

    var pending = null;
    function remember() {
      store(POS_KEY, { file: file, title: pageTitle(), y: Math.round(window.scrollY || window.pageYOffset || 0), when: Date.now() });
    }
    window.addEventListener("scroll", function () {
      if (pending) return;
      pending = setTimeout(function () { pending = null; remember(); }, 400);
    }, { passive: true });
    window.addEventListener("pagehide", remember);
    remember();
  }

  function addMarkButton(h, text) {
    var b = document.createElement("button");
    b.className = "markbtn";
    b.type = "button";
    paint(b, markIndex(marks(), file, h.id) >= 0);
    b.addEventListener("click", function () {
      var list = marks();
      var i = markIndex(list, file, h.id);
      if (i >= 0) {
        list.splice(i, 1);
        paint(b, false);
      } else {
        list.push({ section: section, file: file, id: h.id, text: text, page: pageTitle(), when: Date.now() });
        paint(b, true);
      }
      store(MARKS_KEY, list);
    });
    h.appendChild(b);
  }

  function paint(b, on) {
    b.textContent = on ? "⚑" : "⚐";
    b.classList.toggle("marked", on);
    b.title = on ? "remove bookmark" : "bookmark this section";
    b.setAttribute("aria-label", b.title);
  }

  /* ---- appendix A: click-to-toggle for gloss row popovers (hover
     and keyboard focus already reveal them from CSS alone; this adds
     tap support on touch devices and a way to dismiss on demand) ---- */

  function glossPopovers(main) {
    var rows = main.querySelectorAll(".gloss-row");
    if (!rows.length) return;
    function closeAll() {
      Array.prototype.forEach.call(rows, function (r) { r.classList.remove("open"); });
    }
    Array.prototype.forEach.call(rows, function (row) {
      row.addEventListener("click", function (ev) {
        var wasOpen = row.classList.contains("open");
        closeAll();
        row.classList.toggle("open", !wasOpen);
        ev.stopPropagation();
      });
      row.addEventListener("keydown", function (ev) {
        if (ev.key === "Enter" || ev.key === " ") {
          ev.preventDefault();
          row.click();
        }
      });
    });
    document.addEventListener("click", closeAll);
    document.addEventListener("keydown", function (ev) {
      if (ev.key === "Escape") closeAll();
    });
  }

  /* ---- section contents page: continue-reading link and the
     section's bookmarks ---- */

  function homePage(main) {
    var pos = load(POS_KEY, null);
    var list = marks().filter(function (m) { return m.section === section; });
    if (!pos && !list.length) return;

    list.sort(function (a, b) { return b.when - a.when; });
    var html = "";
    if (pos && pos.file) {
      html += '<p class="reader-continue">Continue where you left off: <a href="' +
        esc(pos.file) + '">' + esc(pos.title || pos.file) + "</a></p>";
    }
    if (list.length) {
      html += '<p class="reader-marks-label">Bookmarks</p><ul class="reader-marks">';
      for (var i = 0; i < list.length; i++) {
        var m = list[i];
        html += '<li><a href="' + esc(m.file) + "#" + esc(m.id) + '">' +
          esc(m.page) + " · " + esc(m.text) +
          '</a><button class="unmark" type="button" data-file="' + esc(m.file) +
          '" data-id="' + esc(m.id) + '" aria-label="remove bookmark" title="remove bookmark">&#215;</button></li>';
      }
      html += "</ul>";
    }

    var box = document.createElement("div");
    box.className = "readerhome";
    box.innerHTML = html;
    var h1 = main.querySelector("h1");
    if (h1 && h1.parentNode === main) main.insertBefore(box, h1.nextSibling);
    else main.insertBefore(box, main.firstChild);

    box.addEventListener("click", function (ev) {
      var b = ev.target;
      if (!b.classList || !b.classList.contains("unmark")) return;
      var all = marks();
      var i = markIndex(all, b.getAttribute("data-file"), b.getAttribute("data-id"));
      if (i >= 0) { all.splice(i, 1); store(MARKS_KEY, all); }
      var li = b.parentNode;
      var ul = li.parentNode;
      ul.removeChild(li);
      if (!ul.children.length) {
        var label = box.querySelector(".reader-marks-label");
        if (label) label.parentNode.removeChild(label);
        ul.parentNode.removeChild(ul);
        if (!box.querySelector(".reader-continue")) box.parentNode.removeChild(box);
      }
    });
  }
})();
