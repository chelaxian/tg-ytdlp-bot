// Applied before first paint: theme (light / dark / auto) and language attribute.
(function () {
  var theme = localStorage.getItem("dash.theme") || "auto";
  document.documentElement.dataset.theme = theme;
  var lang = localStorage.getItem("dash.lang");
  if (lang === "en" || lang === "ru") document.documentElement.lang = lang;
})();
