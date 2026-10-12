"""Link a generated feature page from the rest of the landing site (idempotent).

Usage: wire_site.py <slug> <i18nKey> <card-title-vi> <footer-vi> <footerGuide-vi> <footer-en> <footerGuide-en> [footerLabel-vi footerLabel-en]
(showcase mode: i18nKey like solution.f2, card-title-vi = text of the showcase heading, footer-* = link text under it)
Touches: index.html, vi/index.html (clickable card link + footer), js/i18n.js (3 keys per language), sitemap.xml.
"""
import os, re, sys
slug, key, title_vi, f_vi, fg_vi, f_en, fg_en = sys.argv[1:8]
# Footer label; differs from the link text only in showcase mode (optional args 8, 9 = vi, en)
F_VI, F_EN = (sys.argv[8], sys.argv[9]) if len(sys.argv) > 9 else (f_vi, f_en)
root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
def rd(p): return open(os.path.join(root, p), encoding='utf-8').read()
def wr(p, s): open(os.path.join(root, p), 'w', encoding='utf-8').write(s)
LINK_CLS = 'card-link text-gold text-sm font-semibold mt-3 inline-block hover:text-gold-light'

SHOWCASE = key.startswith('solution.')  # e.g. solution.f2: link under a showcase block instead of a feature card
SC_CLS = 'inline-flex items-center gap-1.5 text-sm font-semibold text-gold hover:underline mb-6'
# --- index.html (English default, data-i18n) ---
s = rd('index.html')
if SHOWCASE and f'href="/{slug}/"' not in s:
    m = re.search(rf'(<p [^>]*data-i18n="{re.escape(key)}\.desc">.*?</p>)', s, re.S)
    s = s[:m.end(1)] + f'\n          <a href="/{slug}/" class="{SC_CLS}"><span data-i18n="{key}.guide">{f_en}</span><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"/></svg></a>' + s[m.end(1):]
    anchor = '            <li><a href="/couple/guide/" data-i18n="footer.coupleGuide">Couple Guide</a></li>\n'
    s = s.replace(anchor, anchor + f'            <li><a href="/{slug}/" data-i18n="footer.{slug}">{F_EN}</a></li>\n            <li><a href="/{slug}/guide/" data-i18n="footer.{slug}Guide">{fg_en}</a></li>\n')
    wr('index.html', s)
elif not SHOWCASE and f'href="/{slug}/"' not in s:
    m = re.search(rf'(<p [^>]*data-i18n="features\.{key}\.desc">.*?</p>)\n(\s*)', s, re.S)
    s = s[:m.end(1)] + f'\n          <a href="/{slug}/" class="{LINK_CLS}" data-i18n="features.{key}.more">Learn more →</a>' + s[m.end(1):]
    anchor = '            <li><a href="/couple/guide/" data-i18n="footer.coupleGuide">Couple Guide</a></li>\n'
    s = s.replace(anchor, anchor + f'            <li><a href="/{slug}/" data-i18n="footer.{key}">{f_en}</a></li>\n            <li><a href="/{slug}/guide/" data-i18n="footer.{key}Guide">{fg_en}</a></li>\n')
    wr('index.html', s)
# --- vi/index.html (Vietnamese baked) ---
s = rd('vi/index.html')
if SHOWCASE and f'href="/{slug}/"' not in s:
    i = s.index(title_vi); j = s.index('</p>', s.index('<p ', i)) + 4  # title_vi = text unique to the showcase heading
    s = s[:j] + f'\n          <a href="/{slug}/" class="{SC_CLS}"><span>{f_vi}</span><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"/></svg></a>' + s[j:]
    anchor = '            <li><a href="/couple/guide/">Hướng Dẫn Cặp Đôi</a></li>\n'
    s = s.replace(anchor, anchor + f'            <li><a href="/{slug}/">{F_VI}</a></li>\n            <li><a href="/{slug}/guide/">{fg_vi}</a></li>\n')
    wr('vi/index.html', s)
elif not SHOWCASE and f'href="/{slug}/"' not in s:
    i = s.index(title_vi); j = s.index('</p>', s.index('<p', i)) + 4
    ind = re.search(r'\n(\s*)$', s[:s.rfind('\n', 0, i)+1]) 
    s = s[:j] + f'\n          <a href="/{slug}/" class="{LINK_CLS}">Xem chi tiết →</a>' + s[j:]
    anchor = '            <li><a href="/couple/guide/">Hướng Dẫn Cặp Đôi</a></li>\n'
    s = s.replace(anchor, anchor + f'            <li><a href="/{slug}/">{f_vi}</a></li>\n            <li><a href="/{slug}/guide/">{fg_vi}</a></li>\n')
    wr('vi/index.html', s)
# --- i18n.js: keys in both dictionaries (en first, then vi) ---
s = rd('js/i18n.js')
fk = key if not SHOWCASE else slug
if f"'footer.{fk}'" not in s:
    if SHOWCASE:  # link text under the showcase block
        ln = [f_en, f_vi]
        s = re.sub(rf"(      '{re.escape(key)}\.title': [^\n]*\n)", lambda m, it=iter(ln): m.group(1) + f"      '{key}.guide': '{next(it)}',\n", s)
    else:
        ln = ['Learn more →', 'Xem chi tiết →']
        s = re.sub(r"(      'features\.couple\.more': [^\n]*\n)", lambda m, it=iter(ln): m.group(1) + f"      'features.{key}.more': '{next(it)}',\n", s)
    fl = iter([(F_EN, fg_en), (F_VI, fg_vi)])
    def foot(m):
        a, b = next(fl)
        return m.group(1) + f"      'footer.{fk}': '{a}',\n      'footer.{fk}Guide': '{b}',\n"
    s = re.sub(r"(      'footer\.coupleGuide': [^\n]*\n)", foot, s)
    wr('js/i18n.js', s)
# --- sitemap ---
s = rd('sitemap.xml')
if f'/{slug}/</loc>' not in s:
    blk = ''.join(f'  <url>\n    <loc>https://moni.live/{slug}/{p}</loc>\n    <lastmod>2026-10-12</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>{pr}</priority>\n  </url>\n' for p, pr in (('', '0.8'), ('guide/', '0.7')))
    s = s.replace('  <url>\n    <loc>https://moni.live/affiliate-guide/</loc>', blk + '  <url>\n    <loc>https://moni.live/affiliate-guide/</loc>')
    wr('sitemap.xml', s)
print('wired', slug)
