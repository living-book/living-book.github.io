/* Cross-app links in the Material header on book pages:
   Library · Atlas · 3D · Ask reachable from anywhere. */
(function () {
  var header = document.querySelector('.md-header__inner');
  if (!header || document.querySelector('.app-links')) return;
  var nav = document.createElement('nav');
  nav.className = 'app-links';
  nav.setAttribute('aria-label', 'Living Books apps');
  nav.innerHTML =
    '<a href="/shelf/">Shelf</a>' +
    '<a href="/ask/">Ask</a>' +
    '<a href="/atlas/">Atlas</a>' +
    '<a href="/atlas/3d/">◈ 3D</a>';
  var search = header.querySelector('.md-search');
  header.insertBefore(nav, search || null);
})();
