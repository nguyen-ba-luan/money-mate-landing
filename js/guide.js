// Guide pages: highlights the section being read in the table of contents, shows reading
// progress, opens screenshots full size and offers a back-to-top button.
(function () {
  var links = Array.prototype.slice.call(document.querySelectorAll('.gd-toc a[data-sec]'));
  var secs = links.map(function (a) { return document.getElementById(a.getAttribute('data-sec')); });
  var bar = document.querySelector('.gd-progress span');
  var tocBar = document.querySelector('.gd-toc-bar span');
  var topBtn = document.querySelector('.gd-top');
  var main = document.querySelector('.gd-main');
  var current = -1;
  var ticking = false;

  function update() {
    ticking = false;
    var doc = document.documentElement;
    var max = doc.scrollHeight - window.innerHeight;
    if (bar) bar.style.transform = 'scaleX(' + (max > 0 ? Math.min(1, window.scrollY / max) : 0) + ')';
    if (topBtn) topBtn.classList.toggle('show', window.scrollY > 800);

    // Active section = last one whose top has passed a line 35% down the viewport
    var line = window.innerHeight * 0.35;
    var idx = 0;
    secs.forEach(function (s, i) { if (s && s.getBoundingClientRect().top <= line) idx = i; });
    if (tocBar && main) {
      var r = main.getBoundingClientRect();
      var pct = Math.max(0, Math.min(1, (line - r.top) / r.height));
      tocBar.style.width = (pct * 100).toFixed(1) + '%';
    }
    if (idx === current) return;
    current = idx;
    links.forEach(function (a, i) {
      a.classList.toggle('active', i === idx);
      a.classList.toggle('done', i < idx);
      if (i === idx) a.setAttribute('aria-current', 'true'); else a.removeAttribute('aria-current');
    });
    // Phone chip bar scrolls horizontally: keep the active chip in view without moving the page
    var list = links[idx] && links[idx].closest('ol');
    if (list && list.scrollWidth > list.clientWidth) {
      var a = links[idx];
      list.scrollTo({ left: a.parentNode.offsetLeft - (list.clientWidth - a.offsetWidth) / 2, behavior: 'smooth' });
    }
  }

  window.addEventListener('scroll', function () {
    if (!ticking) { ticking = true; window.requestAnimationFrame(update); }
  }, { passive: true });
  window.addEventListener('resize', update);
  update();

  // In-page links: main.js only offsets the nav; on phones the sticky TOC bar sits under it too.
  // Capture phase so this runs instead of main.js's handler.
  var nav = document.getElementById('navbar');
  var toc = document.querySelector('.gd-toc');
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href^="#"]');
    if (!a || a.getAttribute('href') === '#') return;
    var target = document.querySelector(a.getAttribute('href'));
    if (!target) return;
    e.preventDefault();
    e.stopPropagation();
    var tocH = toc && window.innerWidth < 1024 ? toc.offsetHeight : 0;
    var offset = (nav ? nav.offsetHeight : 0) + tocH + 16;
    window.scrollTo({ top: target.getBoundingClientRect().top + window.pageYOffset - offset, behavior: 'smooth' });
    if (history.replaceState) history.replaceState(null, '', a.getAttribute('href'));
  }, true);

  if (topBtn) topBtn.addEventListener('click', function () { window.scrollTo({ top: 0, behavior: 'smooth' }); });

  // Screenshot lightbox
  var box = document.querySelector('.gd-lightbox');
  if (box && typeof box.showModal === 'function') {
    var big = box.querySelector('img');
    document.querySelectorAll('.gd-zoom').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var img = btn.querySelector('img');
        big.src = img.currentSrc || img.src;
        big.alt = img.alt;
        box.showModal();
      });
    });
    box.addEventListener('click', function () { box.close(); });
  }
})();
