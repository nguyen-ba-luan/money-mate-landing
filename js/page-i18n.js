/**
 * Language switcher for static pages whose Vietnamese copy lives in the HTML.
 *
 * The Vietnamese text is the source of truth (crawlers read it). On first run
 * it is cached in data-vi, so switching to English and back restores it without
 * a second Vietnamese dictionary. English strings come from window.PAGE_EN.
 *
 *   data-i18n="key"       -> textContent
 *   data-i18n-html="key"  -> innerHTML (trusted, authored by us)
 *   data-i18n-alt="key"   -> alt attribute
 *
 * Shares the mm-lang preference with the home page.
 */
(function () {
  var EN = window.PAGE_EN || {};
  var STORAGE_KEY = 'mm-lang';

  function readLang() {
    try {
      return localStorage.getItem(STORAGE_KEY) === 'en' ? 'en' : 'vi';
    } catch (e) {
      return 'vi';
    }
  }

  function saveLang(lang) {
    try {
      localStorage.setItem(STORAGE_KEY, lang);
    } catch (e) {
      /* private mode: preference just won't persist */
    }
  }

  // Each target: [selector, attribute, how to read/write]
  var TARGETS = [
    { attr: 'data-i18n', read: function (el) { return el.textContent; }, write: function (el, v) { el.textContent = v; } },
    { attr: 'data-i18n-html', read: function (el) { return el.innerHTML; }, write: function (el, v) { el.innerHTML = v; } },
    { attr: 'data-i18n-alt', read: function (el) { return el.getAttribute('alt') || ''; }, write: function (el, v) { el.setAttribute('alt', v); } },
  ];

  function cacheVietnamese() {
    TARGETS.forEach(function (t) {
      document.querySelectorAll('[' + t.attr + ']').forEach(function (el) {
        if (!el.hasAttribute('data-vi')) el.setAttribute('data-vi', t.read(el));
      });
    });
  }

  function apply(lang) {
    document.documentElement.lang = lang;
    TARGETS.forEach(function (t) {
      document.querySelectorAll('[' + t.attr + ']').forEach(function (el) {
        var value = lang === 'en' ? EN[el.getAttribute(t.attr)] : el.getAttribute('data-vi');
        if (value !== undefined && value !== null) t.write(el, value);
      });
    });
    document.querySelectorAll('.lang-toggle').forEach(function (btn) {
      btn.textContent = lang === 'en' ? '🇻🇳 VI' : '🇬🇧 EN';
      btn.setAttribute('aria-label', lang === 'en' ? 'Chuyển sang Tiếng Việt' : 'Switch to English');
    });
  }

  function init() {
    cacheVietnamese();
    var lang = readLang();
    document.querySelectorAll('.lang-toggle').forEach(function (btn) {
      btn.addEventListener('click', function () {
        lang = lang === 'en' ? 'vi' : 'en';
        saveLang(lang);
        apply(lang);
      });
    });
    // Vietnamese is already in the HTML; only touch the DOM when English is stored.
    if (lang === 'en') apply(lang);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
