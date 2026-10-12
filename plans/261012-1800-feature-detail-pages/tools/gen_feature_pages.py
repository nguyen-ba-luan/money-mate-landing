"""Generate /<slug>/ and /<slug>/guide/ pages (vi in HTML, en via js/<slug>-en.js).

Usage: python3 gen_feature_pages.py <spec-module-name>   (run from the tools dir)
A spec module defines SPEC (see features/budget.py). Every user-facing string is a
(vi, en) tuple. Output goes to the landing repo root (../../..). Re-running overwrites
the three generated files, so edit the spec, not the output.
"""
import html, importlib, json, os, subprocess, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
STORE_APPLE = 'https://apps.apple.com/vn/app/moni-s%E1%BB%95-thu-chi-ho%C3%A0n-ti%E1%BB%81n/id6759211409'
STORE_GOOGLE = 'https://play.google.com/store/apps/details?id=com.code4change.moneymate'
FONTS = 'https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500&display=swap'
APPLE_SVG = '<svg class="w-7 h-7" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.81-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83M13 3.5c.73-.83 1.94-1.46 2.94-1.5.13 1.17-.34 2.35-1.04 3.19-.69.85-1.83 1.51-2.95 1.42-.15-1.15.41-2.35 1.05-3.11z"/></svg>'
GPLAY_SVG = '<svg class="w-7 h-7" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M3.609 1.814L13.792 12 3.61 22.186a.996.996 0 01-.61-.92V2.734a1 1 0 01.609-.92zm10.89 10.893l2.302 2.302-10.937 6.333 8.635-8.635zm3.199-3.198l2.807 1.626a1 1 0 010 1.73l-2.808 1.626L15.206 12l2.492-2.491zM5.864 2.658L16.802 8.99l-2.303 2.303-8.635-8.635z"/></svg>'
STORES = (f'<div class="flex flex-wrap gap-4 @@CLS@@"><a href="{STORE_APPLE}" target="_blank" rel="noopener noreferrer" class="store-badge">{APPLE_SVG}<div><span class="badge-text-sm block">App Store</span><span class="badge-text-lg block">iPhone</span></div></a>'
          f'<a href="{STORE_GOOGLE}" target="_blank" rel="noopener noreferrer" class="store-badge">{GPLAY_SVG}<div><span class="badge-text-sm block">Google Play</span><span class="badge-text-lg block">Android</span></div></a></div>')
def stores(cls):
    return STORES.replace('@@CLS@@', cls)


ICONS = {  # heroicons outline, 24px
    'link': 'M13.19 8.688a4.5 4.5 0 011.242 7.244l-4.5 4.5a4.5 4.5 0 01-6.364-6.364l1.757-1.757m13.35-.622l1.757-1.757a4.5 4.5 0 00-6.364-6.364l-4.5 4.5a4.5 4.5 0 001.242 7.244',
    'wallet': 'M21 12a2.25 2.25 0 00-2.25-2.25H15a3 3 0 11-6 0H5.25A2.25 2.25 0 003 12m18 0v6a2.25 2.25 0 01-2.25 2.25H5.25A2.25 2.25 0 013 18v-6m18 0V9M3 12V9m18 0a2.25 2.25 0 00-2.25-2.25H5.25A2.25 2.25 0 003 9m18 0V6a2.25 2.25 0 00-2.25-2.25H5.25A2.25 2.25 0 003 6v3',
    'coin': 'M12 6v12m-3-2.818l.879.659c1.171.879 3.07.879 4.242 0 1.172-.879 1.172-2.303 0-3.182C13.536 12.219 12.768 12 12 12c-.725 0-1.45-.22-2.003-.659-1.106-.879-1.106-2.303 0-3.182s2.9-.879 4.006 0l.415.33M21 12a9 9 0 11-18 0 9 9 0 0118 0z',
    'calendar': 'M6.75 3v2.25M17.25 3v2.25M3 18.75V7.5a2.25 2.25 0 012.25-2.25h13.5A2.25 2.25 0 0121 7.5v11.25m-18 0A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75m-18 0v-7.5A2.25 2.25 0 015.25 9h13.5A2.25 2.25 0 0121 11.25v7.5',
    'refresh': 'M16.023 9.348h4.992v-.001M2.985 19.644v-4.992m0 0h4.992m-4.993 0l3.181 3.183a8.25 8.25 0 0013.803-3.7M4.031 9.865a8.25 8.25 0 0113.803-3.7l3.181 3.182m0-4.991v4.99',
    'chart': 'M3 13.125C3 12.504 3.504 12 4.125 12h2.25c.621 0 1.125.504 1.125 1.125v6.75C7.5 20.496 6.996 21 6.375 21h-2.25A1.125 1.125 0 013 19.875v-6.75zM9.75 8.625c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125v11.25c0 .621-.504 1.125-1.125 1.125h-2.25a1.125 1.125 0 01-1.125-1.125V8.625zM16.5 4.125c0-.621.504-1.125 1.125-1.125h2.25C20.496 3 21 3.504 21 4.125v15.75c0 .621-.504 1.125-1.125 1.125h-2.25a1.125 1.125 0 01-1.125-1.125V4.125z',
    'lock': 'M16.5 10.5V6.75a4.5 4.5 0 10-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 002.25-2.25v-6.75a2.25 2.25 0 00-2.25-2.25H6.75a2.25 2.25 0 00-2.25 2.25v6.75a2.25 2.25 0 002.25 2.25z',
    'users': 'M15 19.128a9.38 9.38 0 002.625.372 9.337 9.337 0 004.121-.952 4.125 4.125 0 00-7.533-2.493M15 19.128v-.003c0-1.113-.285-2.16-.786-3.07M15 19.128v.106A12.318 12.318 0 018.624 21c-2.331 0-4.512-.645-6.374-1.766l-.001-.109a6.375 6.375 0 0111.964-3.07M12 6.375a3.375 3.375 0 11-6.75 0 3.375 3.375 0 016.75 0zm8.25 2.25a2.625 2.625 0 11-5.25 0 2.625 2.625 0 015.25 0z',
    'bell': 'M14.857 17.082a23.848 23.848 0 005.454-1.31A8.967 8.967 0 0118 9.75v-.7V9A6 6 0 006 9v.75a8.967 8.967 0 01-2.312 6.022c1.733.64 3.56 1.085 5.455 1.31m5.714 0a24.255 24.255 0 01-5.714 0m5.714 0a3 3 0 11-5.714 0',
    'home': 'M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25',
    'sliders': 'M10.5 6h9.75M10.5 6a1.5 1.5 0 11-3 0m3 0a1.5 1.5 0 10-3 0M3.75 6H7.5m3 12h9.75m-9.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-3.75 0H7.5m9-6h3.75m-3.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-9.75 0h9.75',
    'pie': 'M10.5 6a7.5 7.5 0 107.5 7.5h-7.5V6zM13.5 10.5H21A7.5 7.5 0 0013.5 3v7.5z',
    'flag': 'M3 3v1.5M3 21v-6m0 0l2.77-.693a9 9 0 016.208.682l.108.054a9 9 0 006.086.71l3.114-.732a48.524 48.524 0 01-.005-10.499l-3.11.732a9 9 0 01-6.085-.711l-.108-.054a9 9 0 00-6.208-.682L3 4.5M3 15V4.5',
    'receipt': 'M9 12h3.75M9 15h3.75M9 18h3.75m3 .75H18a2.25 2.25 0 002.25-2.25V6.108c0-1.135-.845-2.098-1.976-2.192a48.424 48.424 0 00-1.123-.08m-5.801 0c-.065.21-.1.433-.1.664 0 .414.336.75.75.75h4.5a.75.75 0 00.75-.75 2.25 2.25 0 00-.1-.664m-5.8 0A2.251 2.251 0 0113.5 2.25H15c1.012 0 1.867.668 2.15 1.586m-5.8 0c-.376.023-.75.05-1.124.08C9.095 4.01 8.25 4.973 8.25 6.108V8.25m0 0H4.875c-.621 0-1.125.504-1.125 1.125v11.25c0 .621.504 1.125 1.125 1.125h9.75c.621 0 1.125-.504 1.125-1.125V9.375c0-.621-.504-1.125-1.125-1.125H8.25z',
}
TONES = ['orange', 'navy', 'emerald', 'blue']
CHEV = '<svg class="faq-icon w-5 h-5 text-gray-400 flex-shrink-0" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7"/></svg>'
COMMON_EN = {
    'nav.home': 'Home', 'nav.intro': 'Overview', 'nav.guide': 'Guide', 'nav.home.m': 'Home',
    'nav.intro.m': 'Overview', 'nav.guide.m': 'Guide', 'nav.download': 'Download Free', 'nav.download.m': 'Download Free',
    'crumb.guide': 'Guide', 'cta.tagline': 'Ready?', 'foot.home': 'Home', 'foot.privacy': 'Privacy Policy',
    'foot.copy': '© 2026 Code4change. All rights reserved.', 'faq.tag': 'FAQ', 'faq.title': 'Quick answers',
}
_dims = {}


def esc(s):
    return html.escape(s, quote=False)


def dims(img):
    if img not in _dims:
        out = subprocess.run(['magick', 'identify', '-format', '%w %h', os.path.join(ROOT, img.lstrip('/'))],
                             capture_output=True, text=True, check=True).stdout.split()
        _dims[img] = (out[0], out[1])
    return _dims[img]


class Page:
    def __init__(self, en):
        self.en = en

    def t(self, key, pair, tag=None, attr='data-i18n'):
        """Register the English string and return the Vietnamese text wrapped for i18n."""
        vi, en = pair
        self.en[key] = en
        return f'<span {attr}="{key}">{esc(vi)}</span>' if tag is None else f'<{tag} {attr}="{key}">{esc(vi)}</{tag}>'

    def el(self, tag, cls, key, pair):
        vi, en = pair
        self.en[key] = en
        c = f' class="{cls}"' if cls else ''
        return f'<{tag}{c} data-i18n="{key}">{esc(vi)}</{tag}>'

    def img(self, path, alt, cap=None, lazy=True, w=None):
        name = os.path.splitext(os.path.basename(path))[0]
        key = f'shot.{name}'
        self.en[key] = alt[1]
        wd, ht = dims(path)
        c = ''
        if cap:
            self.en[key + '.cap'] = cap[1]
            c = f'<figcaption data-i18n="{key}.cap">{esc(cap[0])}</figcaption>'
        ld = ' loading="lazy"' if lazy else ''
        return (f'<figure class="cp-shot"><img src="{path}" alt="{esc(alt[0])}" data-i18n-alt="{key}" '
                f'width="{wd}" height="{ht}"{ld}>{c}</figure>')


def head(spec, page_kind, jsonld):
    s = spec
    if page_kind == 'intro':
        title, desc, url = s['meta_title'], s['meta_desc'], f'https://moni.live/{s["slug"]}/'
    else:
        title, desc, url = s['guide_meta_title'], s['guide_meta_desc'], f'https://moni.live/{s["slug"]}/guide/'
    og = f'https://moni.live/images/og-image-{s["slug"]}.jpg?v=1'
    ld = ''.join(f'  <script type="application/ld+json">\n{json.dumps(j, ensure_ascii=False, indent=2)}\n  </script>\n' for j in jsonld(title, desc, url))
    return f'''<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(desc)}">
  <meta name="author" content="Code4change">
  <meta name="robots" content="index, follow">
  <meta name="theme-color" content="#1e3a5f">
  <link rel="canonical" href="{url}">
  <link rel="alternate" hreflang="vi" href="{url}">
  <link rel="alternate" hreflang="x-default" href="{url}">
  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(desc)}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{url}">
  <meta property="og:site_name" content="Moni">
  <meta property="og:image" content="{og}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:type" content="image/jpeg">
  <meta property="og:image:alt" content="{esc(s['og_alt'])}">
  <meta property="og:locale" content="vi_VN">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{esc(title)}">
  <meta name="twitter:description" content="{esc(desc)}">
  <meta name="twitter:image" content="{og}">
  <link rel="icon" href="/favicon.ico">
  <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="{FONTS}" rel="stylesheet" media="print" onload="this.media='all'">
  <noscript><link href="{FONTS}" rel="stylesheet"></noscript>
  <link rel="stylesheet" href="/css/tailwind-compiled.css">
  <link rel="stylesheet" href="/css/styles.css">
  <link rel="stylesheet" href="/css/couple.css">
{ld}</head>
'''


def nav(spec):
    s = spec; base = f'/{s["slug"]}/'
    return f'''<body>
  <nav class="nav py-4" id="navbar">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between">
      <a href="/" class="flex items-center gap-3">
        <img src="/images/logo.png" alt="Moni" class="w-10 h-10 rounded-xl" width="40" height="40">
        <span class="text-white font-bold text-xl">Moni</span>
      </a>
      <div class="hidden md:flex items-center gap-8">
        <a class="nav-link text-white/80 hover:text-white text-sm font-medium" data-i18n="nav.home" href="/">Trang chủ</a><a class="nav-link text-white/80 hover:text-white text-sm font-medium" data-i18n="nav.intro" href="{base}">Giới thiệu</a><a class="nav-link text-white/80 hover:text-white text-sm font-medium" data-i18n="nav.guide" href="{base}guide/">Hướng dẫn</a>
        <button class="lang-toggle text-white/80 hover:text-white text-sm font-medium cursor-pointer bg-transparent border border-white/20 rounded-lg px-3 py-1.5 hover:border-white/50 transition-all" aria-label="Switch to English">🇬🇧 EN</button>
        <a class="btn-gold text-sm" data-i18n="nav.download" href="https://moni.live/download" target="_blank" rel="noopener noreferrer">Tải miễn phí</a>
      </div>
      <button class="hamburger md:hidden" id="hamburger-btn" aria-label="Toggle menu"><span></span><span></span><span></span></button>
    </div>
  </nav>
  <div class="mobile-menu" id="mobile-menu">
    <a class="mobile-menu-link" data-i18n="nav.home.m" href="/">Trang chủ</a><a class="mobile-menu-link" data-i18n="nav.intro.m" href="{base}">Giới thiệu</a><a class="mobile-menu-link" data-i18n="nav.guide.m" href="{base}guide/">Hướng dẫn</a>
    <button class="lang-toggle text-white/80 hover:text-white text-lg font-medium cursor-pointer bg-transparent border border-white/20 rounded-lg px-4 py-2 hover:border-white/50 transition-all" aria-label="Switch to English">🇬🇧 EN</button>
    <a class="btn-gold text-lg" data-i18n="nav.download.m" href="https://moni.live/download" target="_blank" rel="noopener noreferrer">Tải miễn phí</a>
  </div>
'''


def footer(spec, p):
    s = spec; base = f'/{s["slug"]}/'
    return f'''  <footer class="footer py-12">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex flex-col sm:flex-row items-center justify-between gap-6">
        <a href="/" class="flex items-center gap-3"><img src="/images/logo.png" alt="Moni" class="w-8 h-8 rounded-lg" width="32" height="32"><span class="text-white font-bold text-lg">Moni</span></a>
        <ul class="flex flex-wrap justify-center gap-6 text-sm">
          <li><a data-i18n="foot.home" href="/">Trang chủ</a></li>
          <li>{p.t('foot.intro', s['foot_intro']).replace('<span ', f'<a href="{base}" ').replace('</span>', '</a>')}</li>
          <li>{p.t('foot.guide', s['foot_guide']).replace('<span ', f'<a href="{base}guide/" ').replace('</span>', '</a>')}</li>
          <li><a data-i18n="foot.privacy" href="/privacy-policy.html">Chính sách bảo mật</a></li>
          <li><a href="mailto:moni.support@gmail.com">moni.support@gmail.com</a></li>
        </ul>
      </div>
      <div class="border-t border-white/10 mt-8 pt-6 text-center"><p class="text-sm"><span data-i18n="foot.copy">© 2026 Code4change. Bảo lưu mọi quyền.</span></p></div>
    </div>
  </footer>
  <script src="/js/{s['slug']}-en.js"></script>
  <script src="/js/page-i18n.js"></script>
  <script src="/js/main.js"></script>
</body>
</html>
'''


def faq_items(p, faq):
    out = []
    for i, (q, a) in enumerate(faq, 1):
        out.append(f'''        <div class="faq-item border border-gray-200 rounded-xl overflow-hidden">
          <button class="faq-question w-full text-left px-6 py-4 flex items-center justify-between gap-4" aria-expanded="false">
            {p.t(f"faq.q{i}", q)}
            {CHEV}
          </button>
          <div class="faq-answer px-6 pb-4">{p.el("p", "text-gray-500 text-sm leading-relaxed", f"faq.a{i}", a)}</div>
        </div>''')
    return '\n'.join(out)


def icon_svg(name):
    return f'<svg width="28" height="28" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="1.5" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="{ICONS[name]}"/></svg>'


def build_intro(spec, en):
    s = spec; p = Page(en); base = f'/{s["slug"]}/'
    def jsonld(title, desc, url):
        return [
            {'@context': 'https://schema.org', '@type': 'WebPage', 'name': title, 'description': desc, 'url': url, 'inLanguage': 'vi',
             'isPartOf': {'@type': 'WebSite', 'name': 'Moni', 'url': 'https://moni.live/'}},
            {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
                {'@type': 'ListItem', 'position': 1, 'name': 'Moni', 'item': 'https://moni.live/'},
                {'@type': 'ListItem', 'position': 2, 'name': s['name'][0], 'item': url}]},
            {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
                {'@type': 'Question', 'name': q[0], 'acceptedAnswer': {'@type': 'Answer', 'text': a[0]}} for q, a in s['faq']]},
        ]
    h = s['hero']
    out = [head(s, 'intro', jsonld), nav(s)]
    out.append(f'''  <section class="hero-gradient cp-hero pt-28 pb-32" id="hero">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full">
      <div class="cp-hero-grid">
        <div class="cp-hero-text">
          <div class="inline-flex items-center gap-2 bg-white/10 rounded-full px-4 py-1.5 mb-6 border border-white/10">
            <span class="w-2 h-2 bg-emerald-400 rounded-full animate-pulse"></span>
            <span class="text-white/70 text-sm font-medium" data-i18n="hero.badge">{esc(h['badge'][0])}</span>
          </div>
          <h1 class="font-display text-4xl sm:text-5xl lg:text-6xl font-extrabold text-white leading-tight mb-6" data-i18n="hero.title">{esc(h['h1'][0])}</h1>
          <p class="text-white/70 text-lg leading-relaxed mb-8 max-w-xl" data-i18n="hero.desc">{esc(h['desc'][0])}</p>
          {stores('mb-6')}
          <a class="text-gold hover:text-gold-light font-semibold" data-i18n="hero.guide" href="{base}guide/">Xem hướng dẫn chi tiết →</a>
        </div>
        <div class="cp-hero-shot">{p.img(h['shot'][0], h['shot'][1], lazy=False)}</div>
      </div>
    </div>
  </section>
''')
    en['hero.badge'], en['hero.title'], en['hero.desc'] = h['badge'][1], h['h1'][1], h['desc'][1]
    en['hero.guide'] = s['guide_link'][1]
    out[-1] = out[-1].replace('>Xem hướng dẫn chi tiết →<', f'>{esc(s["guide_link"][0])}<')
    # problem
    pr = s['problems']
    cards = ''.join(f'<div class="cp-card fade-up">{p.el("h3","cp-card-title",f"problem.p{i}.t",t)}{p.el("p","cp-card-text",f"problem.p{i}.d",d)}</div>' for i, (t, d) in enumerate(pr['items'], 1))
    out.append(f'''  <section class="cp-section cp-bg-soft" id="problem">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="cp-head fade-up">{p.el("p","cp-eyebrow","problem.tag",pr['tag'])}{p.el("h2","cp-h2","problem.title",pr['title'])}</div>
      <div class="cp-grid-3">{cards}</div>
    </div>
  </section>
''')
    ft = s['features']
    cards = ''.join(f'<div class="cp-card fade-up"><div class="cp-icon cp-tone-{TONES[(i-1)%4]}">{icon_svg(ic)}</div>{p.el("h3","cp-card-title",f"feat.f{i}.t",t)}{p.el("p","cp-card-text",f"feat.f{i}.d",d)}</div>' for i, (ic, t, d) in enumerate(ft['items'], 1))
    out.append(f'''  <section class="cp-section" id="features">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="cp-head fade-up">{p.el("p","cp-eyebrow","feat.tag",ft['tag'])}{p.el("h2","cp-h2","feat.title",ft['title'])}</div>
      <div class="cp-grid-3">{cards}</div>
    </div>
  </section>
''')
    hl = s['highlight']
    steps = ''.join(f'<li class="cp-step fade-up"><span class="cp-step-n">{i}</span><div>{p.el("h3","cp-step-title",f"hl.r{i}.t",t)}{p.el("p","cp-card-text",f"hl.r{i}.d",d)}</div></li>' for i, (t, d) in enumerate(hl['steps'], 1))
    notes = ''.join(f'<li>{p.t(f"hl.n{i}", n)}</li>' for i, n in enumerate(hl['notes'], 1))
    shots = ''.join(p.img(i, a, c) for i, a, c in hl['shots'])
    out.append(f'''  <section class="cp-section cp-bg-navy" id="highlight">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="cp-split">
        <div class="cp-split-text">
          {p.el("p","cp-eyebrow","hl.tag",hl['tag'])}
          {p.el("h2","cp-h2 cp-on-dark","hl.title",hl['title'])}
          {p.el("p","cp-lead","hl.desc",hl['desc'])}
          <ol class="cp-steps">{steps}</ol>
          <ul class="cp-notes">{notes}</ul>
        </div>
        <div class="cp-split-shots">{shots}</div>
      </div>
    </div>
  </section>
''')
    hw = s['how']
    steps = ''.join(f'<li class="cp-step cp-step-col fade-up"><span class="cp-step-n">{i}</span>{p.el("h3","cp-step-title",f"how.h{i}.t",t)}{p.el("p","cp-card-text",f"how.h{i}.d",d)}</li>' for i, (t, d) in enumerate(hw['items'], 1))
    out.append(f'''  <section class="cp-section cp-bg-soft" id="how-it-works">
    <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="cp-head fade-up">{p.el("p","cp-eyebrow","how.tag",hw['tag'])}{p.el("h2","cp-h2","how.title",hw['title'])}</div>
      <ol class="cp-grid-3 cp-steps-row">{steps}</ol>
      <p class="cp-cta-row"><a class="btn-gold" data-i18n="how.cta" href="{base}guide/">{esc(s['how_cta'][0])}</a></p>
    </div>
  </section>
''')
    en['how.cta'] = s['how_cta'][1]
    inf = s['info']
    out.append(f'''  <section class="cp-section" id="info">
    <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 text-center fade-up">
      <div class="cp-icon cp-icon-center cp-tone-navy">{icon_svg(inf['icon'])}</div>
      {p.el("h2","cp-h2","info.title",inf['title'])}
      {p.el("p","cp-lead cp-lead-dark","info.desc",inf['desc'])}
    </div>
  </section>
  <section class="cp-section cp-bg-soft" id="faq">
    <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="cp-head fade-up"><p class="cp-eyebrow" data-i18n="faq.tag">Câu hỏi thường gặp</p><h2 class="cp-h2" data-i18n="faq.title">Giải đáp nhanh</h2></div>
      <div class="space-y-3 fade-up">
{faq_items(p, s['faq'])}
      </div>
    </div>
  </section>
  <section class="cta-section py-20 lg:py-28" id="download">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center relative z-10">
      <p class="text-gold font-mono text-sm font-medium tracking-wider uppercase mb-4"><span data-i18n="cta.tagline">Sẵn sàng chưa?</span></p>
      <h2 class="font-display text-3xl sm:text-4xl lg:text-5xl font-extrabold text-white mb-6" data-i18n="cta.title">{esc(s['cta']['title'][0])}</h2>
      <p class="text-white/60 text-lg max-w-lg mx-auto mb-10" data-i18n="cta.desc">{esc(s['cta']['desc'][0])}</p>
      {stores('justify-center')}
    </div>
  </section>
''')
    en['cta.title'], en['cta.desc'] = s['cta']['title'][1], s['cta']['desc'][1]
    out.append(footer(s, p))
    return ''.join(out)


def build_guide(spec, en):
    s = spec; p = Page(en); g = s['guide']; base = f'/{s["slug"]}/'
    def jsonld(title, desc, url):
        steps = []
        for sec in g['sections']:
            if sec.get('faq'): continue
            first = next((b[1] for b in sec['blocks'] if b[0] == 'ol'), [])
            steps.append({'@type': 'HowToStep', 'name': sec['h'][0], 'url': f'{url}#{sec["id"]}',
                          'text': ' '.join(x[0] for x in first)})
        return [
            {'@context': 'https://schema.org', '@type': 'HowTo', 'name': g['title'][0], 'description': g['desc'][0],
             'inLanguage': 'vi', 'step': steps},
            {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
                {'@type': 'ListItem', 'position': 1, 'name': 'Moni', 'item': 'https://moni.live/'},
                {'@type': 'ListItem', 'position': 2, 'name': s['name'][0], 'item': f'https://moni.live{base}'},
                {'@type': 'ListItem', 'position': 3, 'name': 'Hướng dẫn', 'item': url}]},
        ]
    out = [head(s, 'guide', jsonld), nav(s)]
    en['crumb.feature'] = s['name'][1]; en['ghero.title'] = g['title'][1]; en['ghero.desc'] = g['desc'][1]
    out.append(f'''  <section class="hero-gradient cp-hero cp-hero-sm pt-28 pb-24" id="hero">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
      <nav aria-label="breadcrumb" class="cp-crumbs"><a href="/">Moni</a><span>/</span><a href="{base}"><span data-i18n="crumb.feature">{esc(s['name'][0])}</span></a><span>/</span><span data-i18n="crumb.guide">Hướng dẫn</span></nav>
      <h1 class="font-display text-4xl sm:text-5xl font-extrabold text-white leading-tight mb-5" data-i18n="ghero.title">{esc(g['title'][0])}</h1>
      <p class="text-white/70 text-lg max-w-2xl mx-auto" data-i18n="ghero.desc">{esc(g['desc'][0])}</p>
    </div>
  </section>
''')
    toc = ''.join(f'<a data-i18n="toc.{x["id"]}" href="#{x["id"]}">{esc(x["toc"][0])}</a>' for x in g['sections'])
    for x in g['sections']: en[f'toc.{x["id"]}'] = x['toc'][1]
    en['toc.label'] = 'Table of contents'
    out.append(f'  <div class="cp-guide-wrap max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">\n    <aside class="cp-toc" aria-label="Mục lục"><nav>{toc}</nav></aside>\n    <main class="cp-guide-main">\n')
    for x in g['sections']:
        sid = x['id']; body = [p.el('h2', 'cp-h3', f'g.{sid}.h', x['h'])]
        n = {'ol': 0, 'h4': 0, 'note': 0, 'table': 0}
        for b in x['blocks']:
            k = b[0]; n[k] = n.get(k, 0) + 1; i = n[k]
            if k == 'h4':
                body.append(f'<h3 class="cp-h4">{p.t(f"g.{sid}.h4.{i}", b[1])}</h3>')
            elif k == 'ol':
                body.append('<ol class="cp-ol">' + ''.join(f'<li>{p.t(f"g.{sid}.o{i}.{j}", it)}</li>' for j, it in enumerate(b[1], 1)) + '</ol>')
            elif k == 'note':
                body.append(f'<p class="cp-callout cp-callout-{b[1]}">{p.t(f"g.{sid}.n{i}", b[2])}</p>')
            elif k == 'table':
                hdr = ''.join(f'<th>{p.t(f"g.{sid}.t{i}.h{j}", c)}</th>' for j, c in enumerate(b[1], 1))
                rows = ''.join('<tr>' + ''.join(f'<td>{p.t(f"g.{sid}.t{i}.r{r}c{c}", cell)}</td>' for c, cell in enumerate(row, 1)) + '</tr>' for r, row in enumerate(b[2], 1))
                body.append(f'<div class="cp-table-wrap"><table class="cp-table"><thead><tr>{hdr}</tr></thead><tbody>{rows}</tbody></table></div>')
            elif k == 'link':
                body.append(f'<p class="cp-callout cp-callout-info"><a class="text-gold font-semibold" href="{b[1]}" data-i18n="g.{sid}.l{i}">{esc(b[2][0])}</a></p>')
                en[f'g.{sid}.l{i}'] = b[2][1]
            elif k == 'shots':
                body.append('<div class="cp-shots-row">' + ''.join(p.img(im, al, ca) for im, al, ca in b[1]) + '</div>')
        if x.get('faq'):
            body.append('<div class="space-y-3">\n' + faq_items(p, s['faq']) + '\n      </div>')
        out.append(f'<section class="cp-guide-sec" id="{sid}"><div class="cp-guide-body">{"".join(body)}</div></section>\n')
    out.append('    </main>\n  </div>\n')
    out.append(f'''  <section class="cta-section py-20 lg:py-28" id="download">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center relative z-10">
      <p class="text-gold font-mono text-sm font-medium tracking-wider uppercase mb-4"><span data-i18n="cta.tagline">Sẵn sàng chưa?</span></p>
      <h2 class="font-display text-3xl sm:text-4xl lg:text-5xl font-extrabold text-white mb-6" data-i18n="cta.title">{esc(s['cta']['title'][0])}</h2>
      <p class="text-white/60 text-lg max-w-lg mx-auto mb-10" data-i18n="cta.desc">{esc(s['cta']['desc'][0])}</p>
      {stores('justify-center')}
    </div>
  </section>
''')
    en['cta.title'], en['cta.desc'] = s['cta']['title'][1], s['cta']['desc'][1]
    out.append(footer(s, p))
    return ''.join(out)


def main(name):
    spec = importlib.import_module('features.' + name).SPEC
    slug = spec['slug']
    en = dict(COMMON_EN)
    en['foot.intro'] = spec['foot_intro'][1]; en['foot.guide'] = spec['foot_guide'][1]
    pages = {f'{slug}/index.html': build_intro(spec, en), f'{slug}/guide/index.html': build_guide(spec, en)}
    for rel, content in pages.items():
        path = os.path.join(ROOT, rel); os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, 'w', encoding='utf-8').write(content)
    body = ',\n'.join(f'  {json.dumps(k, ensure_ascii=False)}: {json.dumps(v, ensure_ascii=False)}' for k, v in en.items())
    open(os.path.join(ROOT, 'js', f'{slug}-en.js'), 'w', encoding='utf-8').write(
        f'// English strings for /{slug}/ and /{slug}/guide/. Vietnamese lives in the HTML.\nwindow.PAGE_EN = {{\n{body}\n}};\n')
    print('generated', slug, len(en), 'en keys')


if __name__ == '__main__':
    sys.path.insert(0, os.path.dirname(__file__))
    main(sys.argv[1])
