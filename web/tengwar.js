(function () {
  var stored = null;
  try { stored = localStorage.getItem("phi-tengwar"); } catch (e) {}
  if (stored === "on") document.documentElement.classList.add("tengwar-on");
  document.addEventListener("DOMContentLoaded", function () {
    var b = document.querySelector(".tengtoggle");
    if (!b) return;
    b.addEventListener("click", function () {
      var on = document.documentElement.classList.toggle("tengwar-on");
      try { localStorage.setItem("phi-tengwar", on ? "on" : "off"); } catch (e) {}
    });
  });
})();
