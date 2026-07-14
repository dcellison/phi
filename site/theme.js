(function () {
  var stored = null;
  try { stored = localStorage.getItem("phi-theme"); } catch (e) {}
  var theme = stored || (window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
  document.documentElement.dataset.theme = theme;
  window.phiToggleTheme = function () {
    var next = document.documentElement.dataset.theme === "dark" ? "light" : "dark";
    document.documentElement.dataset.theme = next;
    try { localStorage.setItem("phi-theme", next); } catch (e) {}
  };
  document.addEventListener("DOMContentLoaded", function () {
    var b = document.querySelector(".themetoggle");
    if (b) b.addEventListener("click", window.phiToggleTheme);
  });
})();
