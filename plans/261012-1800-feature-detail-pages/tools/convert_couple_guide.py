"""One-off: move the hand-edited /couple/guide/ page onto the guide layout that
gen_feature_pages.py produces (gd- classes, css/guide.css, js/guide.js).

The couple guide has no spec module (its HTML was edited by hand after generation), so this
rewrites the existing markup in place, reusing the generator's building blocks. It refuses to
run twice. English strings for the new pieces are appended to js/couple-en.js.

Usage (from the tools dir): python3 convert_couple_guide.py
"""
import html, json, os, re, sys

sys.path.insert(0, os.path.dirname(__file__))
import gen_feature_pages as g  # noqa: E402

PAGE = os.path.join(g.ROOT, 'couple', 'guide', 'index.html')
INTRO = os.path.join(g.ROOT, 'couple', 'index.html')
EN_JS = os.path.join(g.ROOT, 'js', 'couple-en.js')


def text(fragment):
    return html.unescape(re.sub(r'<[^>]+>', ' ', fragment))


def zoomable(fig):
    """Wrap a .cp-shot figure's image in the zoom button, like gen_feature_pages.shot()."""
    fig = fig.replace('<figure class="cp-shot"><img', '<figure class="cp-shot gd-shot"><button type="button" class="gd-zoom" aria-label="Phóng to ảnh"><img', 1)
    cut = '<figcaption' if '<figcaption' in fig else '</figure>'
    return fig.replace(cut, '</button>' + cut, 1)


def convert_body(body):
    body = body.replace('class="cp-ol"', 'class="gd-steps"').replace('class="cp-h4"', 'class="gd-h3"')
    body = body.replace('<div class="cp-table-wrap"><table class="cp-table">', '<div class="gd-table-wrap"><table class="gd-table">')
    body = re.sub(r'<p class="cp-callout cp-callout-(info|warn)"><span ([^>]+)>(.*?)</span></p>',
                  lambda m: g.callout(m.group(1), f'<p {m.group(2)}>{m.group(3)}</p>'), body, flags=re.S)
    body = body.replace('<div class="cp-shots-row">', '<div class="gd-shots">')
    body = re.sub(r'<figure class="cp-shot">.*?</figure>', lambda m: zoomable(m.group(0)), body, flags=re.S)
    return body


def main():
    s = open(PAGE, encoding='utf-8').read()
    if 'gd-hero' in s:
        sys.exit('couple guide already converted')
    en = {}

    hero_a = s.index('  <section class="hero-gradient cp-hero')
    main_a = s.index('<main class="cp-guide-main">')
    hero = s[hero_a:main_a]
    crumb = re.search(r'<span data-i18n="crumb.couple">([^<]+)</span>', hero).group(1)
    title = re.search(r'data-i18n="ghero.title">([^<]+)<', hero).group(1)
    desc = re.search(r'data-i18n="ghero.desc">([^<]+)<', hero).group(1)
    toc = re.findall(r'<a data-i18n="toc\.([^"]+)" href="#[^"]+">([^<]+)</a>', hero)

    main_b = s.index('</main>', main_a)
    inner = s[main_a + len('<main class="cp-guide-main">'):main_b]
    parts = re.split(r'(?=<section class="cp-guide-sec")', inner)
    secs = [x for x in parts if x.startswith('<section class="cp-guide-sec"')]
    assert [re.match(r'<section class="cp-guide-sec" id="([^"]+)"', x).group(1) for x in secs] == [t[0] for t in toc]

    video_ids, words, out = [], 0, []
    for n, sec in enumerate(secs, 1):
        sid = re.match(r'<section class="cp-guide-sec" id="([^"]+)">', sec).group(1)
        body = re.match(r'<section class="cp-guide-sec" id="[^"]+"><div class="cp-guide-body">(.*)</div></section>\s*$', sec, re.S).group(1)
        if 'class="cp-video"' in body:
            video_ids.append(sid)
        words += len(text(body).split())
        h2 = re.match(r'<h2 class="cp-h3" ([^>]+)>(.*?)</h2>', body, re.S)
        body = g.sec_head(n, f'<h2 class="gd-h2" {h2.group(1)}>{h2.group(2)}</h2>') + convert_body(body[h2.end():])
        if n < len(secs):
            body += g.next_link(toc[n][0], html.unescape(toc[n][1]))
        out.append(f'      <section class="gd-sec" id="{sid}">{body}</section>\n')

    shot = re.search(r'<div class="cp-hero-shot">(<figure.*?</figure>)</div>', open(INTRO, encoding='utf-8').read(), re.S).group(1)
    p = g.Page(en)
    new = (g.guide_hero(p, (html.unescape(crumb), 'crumb.couple'), '/couple/', html.unescape(title), html.unescape(desc),
                        [t[0] for t in toc], video_ids, g.read_minutes(words), shot)
           + g.guide_open([(t[0], html.unescape(t[1])) for t in toc]) + ''.join(out) + g.guide_close('couple', en))
    s = s[:hero_a] + new + s[main_b + len('</main>\n  </div>\n'):]

    # assets, back-to-top + lightbox before the footer
    s = s.replace('<link rel="stylesheet" href="/css/couple.css">\n', '<link rel="stylesheet" href="/css/couple.css">\n  <link rel="stylesheet" href="/css/guide.css">\n', 1)
    s = s.replace('  <footer class="footer', g.GUIDE_TAIL + '  <footer class="footer', 1)
    s = s.replace('<script src="/js/main.js"></script>\n', '<script src="/js/main.js"></script>\n  <script src="/js/guide.js" defer></script>\n', 1)
    open(PAGE, 'w', encoding='utf-8').write(s)

    body = ',\n'.join(f'  {json.dumps(k, ensure_ascii=False)}: {json.dumps(v, ensure_ascii=False)}' for k, v in en.items())
    with open(EN_JS, 'a', encoding='utf-8') as f:
        f.write(f'// Guide layout strings (meta chips, TOC, other guides).\nObject.assign(window.PAGE_EN, {{\n{body}\n}});\n')
    print('converted couple guide:', len(secs), 'sections,', len(video_ids), 'videos,', len(en), 'en keys')


if __name__ == '__main__':
    main()
