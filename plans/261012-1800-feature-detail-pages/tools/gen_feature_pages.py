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
ICONS['heart'] = 'M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z'
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


POSTERS = {  # youtube id -> poster file in images/videos/
    'xQgsCwSZHco': '00-trailer', 'zdjgbBdpOE8': '01-bat-dau-nhanh', 'e8MdrDVgIbI': '02-danh-muc-tuy-chinh', 'p3no5FciK78': '04-ngan-sach',
    'na9rFLUEWMw': '05-phan-tich-bao-cao', '5vpx3JSNfi4': '06-chi-tieu-dinh-ky', 'v4VmKUb1aOc': '07-khoan-du-chi', '3qCLWZWBdAE': '08-tiet-kiem',
    'IKY6snglJ-g': '09-quan-ly-no', '67y6oTZCKPo': '10-thu-thach', 'BfsUD85ih3k': '11-cong-thuc-quan-ly-tien', 'NumdiDjsbYQ': '12-gia-vang',
    '8n-Wvbssxag': '13-nhom-tao-va-moi', '-Fps8CbJ63A': '14-nhom-chi-tieu-thanh-toan', 'BzAcl17PZgM': '15-tong-ket-chuyen-di', 'bUY2WX9yoY0': '16-quy-nhom',
    'MeIbyKNR5QI': '17-cap-doi-ghep-doi', 'OGq-Sh-eFGk': '18-cap-doi-chi-chung', 'tGakdssNDBw': '19-khoa-sinh-trac-hoc', 'akdOBQfmv-8': '20-dong-bo-thiet-bi-ngon-ngu',
    'yPDwLlu_gkY': '22-ban-do-chi-tieu', 'pBxaav5qT0Y': '23-hoan-tien-shopee-tiktok', '8q2Yw_wX1a4': '24-gioi-thieu-ban-be-hang-thuong', 'WEOCMnC3kjY': '27-moni-tren-web',
    '-NQiNx513gY': '03-quet-hoa-don', 'LUZ2K0ArxlE': '21-widget', 'M36612lfOUg': '25-tu-ghi-thong-bao', '5t6HaOBbP4M': '26-quet-qr-thanh-toan',
}


def video_block(p, key, v):
    """Click-to-play YouTube embed with a local poster (YouTube serves no thumbnail for private videos)."""
    vid, label = v['id'], v['title']
    p.en[key] = 'Watch the video guide: ' + label[1]
    return (f'<figure class="cp-video" data-yt="{vid}" data-publish="{v["date"]}T19:00:00+07:00" hidden>'
            f'<button type="button" class="cp-video-btn" aria-label="{esc(label[0])}">'
            f'<img src="/images/videos/{POSTERS[vid]}.webp" alt="" width="960" height="540" loading="lazy">'
            f'<span class="cp-video-play" aria-hidden="true"></span></button>'
            f'<figcaption data-i18n="{key}">Xem video hướng dẫn: {esc(label[0])}</figcaption></figure>')


def head(spec, page_kind, jsonld):
    extra = '  <link rel="stylesheet" href="/css/guide.css">\n' if page_kind == 'guide' else ''
    s = spec
    if page_kind == 'intro':
        title, desc, url = s['meta_title'], s['meta_desc'], f'https://moni.live/{s["slug"]}/'
    else:
        title, desc, url = s['guide_meta_title'], s['guide_meta_desc'], f'https://moni.live/{s["slug"]}/guide/'
    og = f'https://moni.live/images/og-image-{s["slug"]}{"" if page_kind == "intro" else "-guide"}.jpg?v=1'
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
{extra}{ld}</head>
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


def footer(spec, p, guide=False):
    gjs = '  <script src="/js/guide.js" defer></script>\n' if guide else ''
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
  <script src="/js/video-embed.js" defer></script>
  <script src="/js/main.js"></script>
{gjs}</body>
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


# Every guide page, for the "more guides" cards at the bottom of each guide.
GUIDES = [
    ('budget', 'wallet', ('Ngân sách', 'Budgets'), ('Đặt hạn mức theo danh mục và dùng công thức 50/30/20.', 'Set category limits and use the 50/30/20 formula.')),
    ('couple', 'heart', ('Tài chính cặp đôi', 'Couple finance'), ('Kết nối với người ấy, chi chung và hoàn ứng.', 'Connect with your partner, share costs and pay each other back.')),
    ('groups', 'users', ('Nhóm chi tiêu', 'Spending groups'), ('Chia tiền chuyến đi, thêm khách và tất toán.', 'Split trip costs, add guests and settle up.')),
    ('savings', 'flag', ('Mục tiêu tiết kiệm', 'Savings goals'), ('Đặt mục tiêu, nạp rút và theo dõi tiến độ.', 'Set goals, add or withdraw and track progress.')),
    ('recurring', 'refresh', ('Giao dịch định kỳ', 'Recurring transactions'), ('Tự ghi tiền nhà, lương và hóa đơn hàng tháng.', 'Log rent, salary and monthly bills automatically.')),
    ('analytics', 'chart', ('Phân tích & báo cáo', 'Analytics & reports'), ('Đọc biểu đồ, báo cáo tháng và xuất dữ liệu.', 'Read the charts, monthly report and export data.')),
    ('gold', 'coin', ('Giá vàng & tín hiệu AI', 'Gold prices & AI signals'), ('Xem giá, đặt cảnh báo và theo dõi tài sản vàng.', 'Check prices, set alerts and track your gold.')),
]
GUIDE_EN = {
    'ghero.kicker': 'Step-by-step guide', 'meta.sections': 'sections', 'meta.read': 'min read', 'meta.videos': 'videos',
    'meta.video': 'video', 'ghero.start': 'Start reading', 'ghero.watch': 'Watch the video', 'toc.title': 'In this guide',
    'toc.dl.t': 'No Moni yet?', 'toc.dl.d': 'Free, no ads. Follow along on your phone.', 'toc.dl.btn': 'Download free',
    'next': 'Next:', 'rel.tag': 'Keep learning', 'rel.title': 'More Moni guides', 'rel.open': 'Read guide',
}
CALLOUT_ICON = {
    'info': 'M11.25 11.25l.041-.02a.75.75 0 011.063.852l-.708 2.836a.75.75 0 001.063.853l.041-.021M21 12a9 9 0 11-18 0 9 9 0 0118 0zm-9-3.75h.008v.008H12V8.25z',
    'warn': 'M12 9v3.75m-9.303 3.376c-.866 1.5.217 3.374 1.948 3.374h14.71c1.73 0 2.813-1.874 1.948-3.374L13.949 3.378c-.866-1.5-3.032-1.5-3.898 0L2.697 16.126zM12 15.75h.007v.008H12v-.008z',
}


def svg(path, size=20, sw=1.75):
    return (f'<svg width="{size}" height="{size}" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="{sw}" '
            f'aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="{path}"/></svg>')


def _texts(sec):
    """All Vietnamese strings in a section, for the reading-time estimate."""
    out = [sec['h'][0]]
    for b in sec['blocks']:
        if b[0] == 'ol': out += [x[0] for x in b[1]]
        elif b[0] == 'note': out.append(b[2][0])
        elif b[0] == 'h4': out.append(b[1][0])
        elif b[0] == 'table': out += [c[0] for row in b[2] for c in row]
    return out


def shot(p, im, al, ca):
    """Screenshot in a phone bezel; the button opens it full size (js/guide.js)."""
    fig = p.img(im, al, ca).replace('<figure class="cp-shot"><img', '<figure class="cp-shot gd-shot"><button type="button" class="gd-zoom" aria-label="Phóng to ảnh"><img', 1)
    cut = '<figcaption' if ca else '</figure>'
    return fig.replace(cut, '</button>' + cut, 1)


PLAY = 'M5.25 5.653c0-.856.917-1.398 1.667-.986l11.54 6.348a1.125 1.125 0 010 1.971l-11.54 6.347a1.125 1.125 0 01-1.667-.985V5.653z'
ARROW_R = 'M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3'


def read_minutes(words):
    return max(2, round(words / 200))


def guide_hero(p, crumb, base, title, desc, sec_ids, video_ids, read_min, shot_img):
    """Hero: crumbs, title, meta chips, CTAs and a tilted phone. crumb/title/desc are (vi, key) and
    their English must already be in p.en; shot_img is an already-rendered <figure>."""
    meta = (f'<li>{svg(ICONS["receipt"], 16)}<b>{len(sec_ids)}</b> <span data-i18n="meta.sections">phần</span></li>'
            f'<li>{svg("M12 6v6h4.5m4.5 0a9 9 0 11-18 0 9 9 0 0118 0z", 16)}<b>{read_min}</b> <span data-i18n="meta.read">phút đọc</span></li>')
    watch = ''
    if video_ids:
        meta += f'<li>{svg(PLAY, 16)}<b>{len(video_ids)}</b> <span data-i18n="meta.video{"s" if len(video_ids) > 1 else ""}">video</span></li>'
        watch = f'<a class="gd-btn-ghost" href="#{video_ids[0]}">{svg(PLAY, 18)}<span data-i18n="ghero.watch">Xem video</span></a>'
    return f'''  <div class="gd-progress" aria-hidden="true"><span></span></div>
  <section class="gd-hero" id="hero">
    <div class="gd-hero-inner max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="gd-hero-text">
        <nav aria-label="breadcrumb" class="gd-crumbs"><a href="/">Moni</a><span>/</span><a href="{base}"><span data-i18n="{crumb[1]}">{esc(crumb[0])}</span></a><span>/</span><span data-i18n="crumb.guide">Hướng dẫn</span></nav>
        <p class="gd-kicker"><span class="gd-kicker-dot"></span><span data-i18n="ghero.kicker">Hướng dẫn từng bước</span></p>
        <h1 class="gd-h1" data-i18n="ghero.title">{esc(title)}</h1>
        <p class="gd-lead" data-i18n="ghero.desc">{esc(desc)}</p>
        <ul class="gd-meta">{meta}</ul>
        <div class="gd-hero-cta"><a class="btn-gold" href="#{sec_ids[0]}" data-i18n="ghero.start">Bắt đầu đọc</a>{watch}</div>
      </div>
      <div class="gd-hero-shot" aria-hidden="true">{shot_img}</div>
    </div>
  </section>
'''


def guide_open(toc_items):
    """Body wrapper, TOC and the opening of <main>. toc_items: [(id, vi label)], keys toc.<id>."""
    toc = ''.join(f'<li><a data-sec="{i}" href="#{i}"><span class="gd-toc-n">{n:02d}</span><span data-i18n="toc.{i}">{esc(label)}</span></a></li>'
                  for n, (i, label) in enumerate(toc_items, 1))
    return f'''  <div class="gd-body">
  <div class="gd-wrap max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
    <aside class="gd-toc" aria-label="Mục lục">
      <p class="gd-toc-title" data-i18n="toc.title">Nội dung hướng dẫn</p>
      <div class="gd-toc-bar"><span></span></div>
      <nav><ol>{toc}</ol></nav>
      <div class="gd-toc-dl"><p class="gd-toc-dl-t" data-i18n="toc.dl.t">Chưa có Moni?</p><p class="gd-toc-dl-d" data-i18n="toc.dl.d">Miễn phí, không quảng cáo. Mở app làm theo từng bước.</p><a class="btn-gold" data-i18n="toc.dl.btn" href="https://moni.live/download" target="_blank" rel="noopener noreferrer">Tải miễn phí</a></div>
    </aside>
    <main class="gd-main">
'''


def sec_head(n, h2):
    return f'<header class="gd-sec-head"><span class="gd-sec-n">{n:02d}</span>{h2}</header>'


def next_link(nx_id, nx_label):
    return (f'<a class="gd-next" href="#{nx_id}"><span data-i18n="next">Tiếp theo:</span> <b data-i18n="toc.{nx_id}">{esc(nx_label)}</b>'
            f'{svg("M19.5 13.5L12 21m0 0l-7.5-7.5M12 21V3", 16, 2)}</a>')


def callout(kind, inner_p):
    return f'<div class="gd-callout gd-callout-{kind}"><span class="gd-callout-i">{svg(CALLOUT_ICON[kind], 20)}</span>{inner_p}</div>'


def guide_close(slug, en):
    """Closes <main>, adds the other guides, back-to-top and the lightbox. Registers English keys."""
    en.update(GUIDE_EN)
    cards = ''
    for k, (g_slug, ic, name, desc) in enumerate(x for x in GUIDES if x[0] != slug):
        en[f'rel.{g_slug}.n'], en[f'rel.{g_slug}.d'] = name[1], desc[1]
        cards += (f'<a class="gd-rel-card" href="/{g_slug}/guide/"><span class="cp-icon cp-tone-{TONES[k % 4]} gd-rel-ic">{icon_svg(ic)}</span>'
                  f'<span class="gd-rel-n" data-i18n="rel.{g_slug}.n">{esc(name[0])}</span><span class="gd-rel-d" data-i18n="rel.{g_slug}.d">{esc(desc[0])}</span>'
                  f'<span class="gd-rel-go"><span data-i18n="rel.open">Xem hướng dẫn</span>{svg(ARROW_R, 16, 2)}</span></a>')
    return f'''    </main>
  </div>
  <section class="gd-related">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
      <p class="cp-eyebrow" data-i18n="rel.tag">Học tiếp</p>
      <h2 class="gd-rel-title" data-i18n="rel.title">Các hướng dẫn khác của Moni</h2>
      <div class="gd-rel-grid">{cards}</div>
    </div>
  </section>
  </div>
'''


GUIDE_TAIL = (f'  <button type="button" class="gd-top" aria-label="Lên đầu trang">{svg("M4.5 10.5L12 3m0 0l7.5 7.5M12 3v18", 20, 2)}</button>\n'
              '  <dialog class="gd-lightbox" aria-label="Ảnh phóng to"><img alt=""></dialog>\n')


def build_guide(spec, en):
    s = spec; p = Page(en); g = s['guide']; base = f'/{s["slug"]}/'
    secs = g['sections']
    def jsonld(title, desc, url):
        steps = []
        for sec in secs:
            if sec.get('faq'): continue
            first = next((b[1] for b in sec['blocks'] if b[0] == 'ol'), [])
            steps.append({'@type': 'HowToStep', 'name': sec['h'][0], 'url': f'{url}#{sec["id"]}',
                          'text': ' '.join(x[0] for x in first)})
        return [
            {'@context': 'https://schema.org', '@type': 'HowTo', 'name': g['title'][0], 'description': g['desc'][0],
             'inLanguage': 'vi', 'totalTime': f'PT{read_min}M', 'step': steps},
            {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
                {'@type': 'ListItem', 'position': 1, 'name': 'Moni', 'item': 'https://moni.live/'},
                {'@type': 'ListItem', 'position': 2, 'name': s['name'][0], 'item': f'https://moni.live{base}'},
                {'@type': 'ListItem', 'position': 3, 'name': 'Hướng dẫn', 'item': url}]},
        ]
    words = sum(len(t.split()) for sec in secs for t in _texts(sec)) + sum(len(a[0].split()) + len(q[0].split()) for q, a in s['faq'])
    read_min = read_minutes(words)
    out = [head(s, 'guide', jsonld), nav(s)]
    en['crumb.feature'] = s['name'][1]; en['ghero.title'] = g['title'][1]; en['ghero.desc'] = g['desc'][1]
    out.append(guide_hero(p, (s['name'][0], 'crumb.feature'), base, g['title'][0], g['desc'][0], [x['id'] for x in secs],
                          [x['id'] for x in secs if x.get('video')], read_min, p.img(s['hero']['shot'][0], s['hero']['shot'][1], lazy=False)))
    for x in secs: en[f'toc.{x["id"]}'] = x['toc'][1]
    out.append(guide_open([(x['id'], x['toc'][0]) for x in secs]))
    for idx, x in enumerate(secs):
        sid = x['id']
        body = [sec_head(idx + 1, p.el("h2", "gd-h2", f"g.{sid}.h", x["h"]))]
        if x.get('video'):
            body.append(video_block(p, f'g.{sid}.video', x['video']))
        n = {}
        for b in x['blocks']:
            k = b[0]; n[k] = n.get(k, 0) + 1; i = n[k]
            if k == 'h4':
                body.append(f'<h3 class="gd-h3">{p.t(f"g.{sid}.h4.{i}", b[1])}</h3>')
            elif k == 'ol':
                body.append('<ol class="gd-steps">' + ''.join(f'<li>{p.t(f"g.{sid}.o{i}.{j}", it)}</li>' for j, it in enumerate(b[1], 1)) + '</ol>')
            elif k == 'note':
                body.append(callout(b[1], p.el("p", "", f"g.{sid}.n{i}", b[2])))
            elif k == 'table':
                hdr = ''.join(f'<th>{p.t(f"g.{sid}.t{i}.h{j}", c)}</th>' for j, c in enumerate(b[1], 1))
                # a cell may carry a third item, a colour tone, shown as a status dot before the text
                def td(key, cell):
                    dot = f'<span class="gd-dot gd-dot-{cell[2]}" aria-hidden="true"></span>' if len(cell) > 2 else ''
                    return f'<td>{dot}{p.t(key, cell[:2])}</td>'
                rows = ''.join('<tr>' + ''.join(td(f"g.{sid}.t{i}.r{r}c{c}", cell) for c, cell in enumerate(row, 1)) + '</tr>' for r, row in enumerate(b[2], 1))
                body.append(f'<div class="gd-table-wrap"><table class="gd-table"><thead><tr>{hdr}</tr></thead><tbody>{rows}</tbody></table></div>')
            elif k == 'link':
                body.append(f'<a class="gd-link-card" href="{b[1]}"><span data-i18n="g.{sid}.l{i}">{esc(b[2][0])}</span>{svg(ARROW_R, 18)}</a>')
                en[f'g.{sid}.l{i}'] = b[2][1]
            elif k == 'shots':
                body.append('<div class="gd-shots">' + ''.join(shot(p, im, al, ca) for im, al, ca in b[1]) + '</div>')
        if x.get('faq'):
            body.append('<div class="space-y-3">\n' + faq_items(p, s['faq']) + '\n      </div>')
        if idx + 1 < len(secs):
            body.append(next_link(secs[idx + 1]['id'], secs[idx + 1]['toc'][0]))
        out.append(f'      <section class="gd-sec" id="{sid}">{"".join(body)}</section>\n')
    out.append(guide_close(s['slug'], en))
    out.append(f'''  <section class="cta-section py-20 lg:py-28" id="download">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center relative z-10">
      <p class="text-gold font-mono text-sm font-medium tracking-wider uppercase mb-4"><span data-i18n="cta.tagline">Sẵn sàng chưa?</span></p>
      <h2 class="font-display text-3xl sm:text-4xl lg:text-5xl font-extrabold text-white mb-6" data-i18n="cta.title">{esc(s['cta']['title'][0])}</h2>
      <p class="text-white/60 text-lg max-w-lg mx-auto mb-10" data-i18n="cta.desc">{esc(s['cta']['desc'][0])}</p>
      {stores('justify-center')}
    </div>
  </section>
''' + GUIDE_TAIL)
    en['cta.title'], en['cta.desc'] = s['cta']['title'][1], s['cta']['desc'][1]
    out.append(footer(s, p, guide=True))
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
