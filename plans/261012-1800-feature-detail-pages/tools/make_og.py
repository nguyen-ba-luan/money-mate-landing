"""Render images/og-image-<slug>.jpg (1200x630) via headless Chrome. Usage: make_og.py slug TAG H1_html "pill1|pill2|pill3" img1 img2"""
import os, subprocess, sys, tempfile
slug, tag, h1, pills, i1, i2 = sys.argv[1:7]
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.abspath(os.path.join(here, '..', '..', '..'))
t = open(os.path.join(here, 'og-template.html'), encoding='utf-8').read()
t = t.replace('file://LOGO', 'file://' + root + '/images/logo.png').replace('file://IMG1', 'file://' + root + i1).replace('file://IMG2', 'file://' + root + i2)
t = t.replace('__TAG__', tag).replace('__H1__', h1).replace('__PILLS__', ''.join(f'<span>{p}</span>' for p in pills.split('|')))
d = tempfile.mkdtemp(); f = os.path.join(d, 'og.html'); open(f, 'w', encoding='utf-8').write(t)
png = os.path.join(d, 'og.png')
subprocess.run(['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', '--headless=new', '--disable-gpu', '--hide-scrollbars',
                '--allow-file-access-from-files', '--window-size=1200,630', '--virtual-time-budget=6000', f'--screenshot={png}', 'file://' + f], check=True, capture_output=True)
subprocess.run(['magick', png, '-quality', '85', os.path.join(root, 'images', f'og-image-{slug}.jpg')], check=True)
print('ok', slug)
