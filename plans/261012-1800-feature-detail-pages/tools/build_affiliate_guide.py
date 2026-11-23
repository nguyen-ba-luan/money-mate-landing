"""Rebuild /affiliate-guide/ (Shopee cashback, Vietnamese only) on the shared guide layout.

The page has no intro page and no English copy, so it does not fit gen_feature_pages.main();
it reuses that module's building blocks instead. The <head> (meta, Open Graph, JSON-LD) is kept
from the current file up to the font links, so SEO tags stay exactly as they are; everything
after is rebuilt from the content below. Safe to re-run.

Usage (from the tools dir): python3 build_affiliate_guide.py
"""
import os, sys

sys.path.insert(0, os.path.dirname(__file__))
import gen_feature_pages as g  # noqa: E402

PAGE = os.path.join(g.ROOT, 'affiliate-guide', 'index.html')
# ?v= busts browser/CDN caches when an image is edited in place (step1 had the owner's name redacted)
IMG1, IMG3 = '/images/guide/step1.webp?v=2', '/images/guide/step3.webp'

# Steps are trusted HTML (they keep their <strong> highlights).
SECTIONS = [
    {'id': 'cach-hoat-dong', 'toc': 'Cách hoạt động', 'h': 'Hoàn tiền Shopee hoạt động thế nào', 'steps': [
        '<strong>Mở link qua Moni.</strong> Dán link hoặc chia sẻ sản phẩm sang Moni.',
        '<strong>Mua sắm bình thường.</strong> Đặt hàng trên Shopee như mọi khi.',
        '<strong>Nhận hoàn tiền.</strong> Hoàn tiền được ghi nhận tự động vào Moni.',
    ], 'video': True},
    {'id': 'cach-1', 'toc': 'Cách 1: Dán link', 'h': 'Cách 1: Dán link sản phẩm',
     'lead': 'Copy link sản phẩm Shopee và dán vào Moni để tự động tạo link hoàn tiền.', 'steps': [
        '<strong>Mở app Shopee.</strong> Tìm sản phẩm bạn muốn mua trên Shopee. Bấm <strong>"Sao chép link"</strong> hoặc copy URL của sản phẩm.',
        '<strong>Dán vào Moni.</strong> Mở app Moni, tại mục <strong>"Hoàn tiền Shopee"</strong> trên trang chủ, dán link vào ô nhập và bấm <strong>"Dán &amp; Kiếm tiền"</strong>.',
        '<strong>Mua sắm &amp; nhận hoàn tiền.</strong> Moni sẽ mở Shopee với link hoàn tiền. Bạn mua sắm bình thường và hoàn tiền sẽ tự động được ghi nhận.',
    ], 'shot': (IMG1, 'Hướng dẫn dán link Shopee vào app Moni để nhận hoàn tiền', 'Dán link vào ô nhập rồi bấm "Dán & Kiếm tiền"',
                '<div class="annot-rect" style="top:58.12%;left:8.09%;width:83.91%;height:7.48%"></div>')},
    {'id': 'cach-2', 'toc': 'Cách 2: Chia sẻ (iPhone)', 'h': 'Cách 2: Chia sẻ từ Shopee',
     'lead': 'Chia sẻ sản phẩm trực tiếp từ Shopee sang Moni chỉ với 2 bước.',
     'note': ('warn', 'Cách 2 chỉ hoạt động trên iPhone/iPad. Người dùng Android vui lòng dùng Cách 1.'), 'steps': [
        '<strong>Bấm nút Chia sẻ trên Shopee.</strong> Tại trang chi tiết sản phẩm Shopee, bấm vào <strong>biểu tượng chia sẻ</strong> (mũi tên) ở góc trên bên phải.',
        '<strong>Chọn Moni.</strong> Trong bảng chia sẻ, tìm và chọn <strong>app Moni</strong> (biểu tượng con heo). Nếu không thấy, vuốt sang phải hoặc bấm <strong>"Thêm"</strong> để tìm.',
        '<strong>Mua sắm &amp; nhận hoàn tiền.</strong> Moni sẽ tự động tạo link hoàn tiền và mở Shopee. Tiếp tục mua sắm bình thường, hoàn tiền sẽ được ghi nhận!',
    ], 'shot': (IMG3, 'Cách chia sẻ sản phẩm Shopee sang Moni trên iOS để kiếm hoàn tiền', 'Bấm Chia sẻ (1) rồi chọn Moni (2)',
                '<div class="annot-circle" style="top:10%;left:71.79%;width:10.18%"></div><div class="annot-badge" style="top:7.65%;left:76.88%">1</div>'
                '<div class="annot-circle" style="top:72.99%;left:39.2%;width:13.57%"></div><div class="annot-badge" style="top:69.86%;left:45.99%">2</div>')},
    {'id': 'luu-y', 'toc': 'Lưu ý quan trọng', 'h': 'Lưu ý quan trọng', 'notes': [
        ('warn', 'Phải đăng nhập tài khoản Moni', 'Bạn cần đăng nhập vào app Moni để hệ thống biết hoàn tiền cho ai. Nếu chưa đăng nhập, hoàn tiền sẽ không được ghi nhận vào tài khoản của bạn.'),
        ('info', 'Phải mở link qua Moni', 'Hoàn tiền chỉ được ghi nhận khi bạn mở link sản phẩm qua Moni. Nếu bạn mở trực tiếp trên Shopee thì sẽ không có hoàn tiền.'),
        ('info', 'Đơn hàng hiển thị ngày hôm sau', 'Đặt hàng hôm nay, đơn hàng sẽ hiển thị trên hệ thống Moni vào ngày hôm sau. Tiền hoàn được xử lý tự động vào thứ 2 hàng tuần.'),
        ('info', 'Tự động chuyển tiền mỗi thứ 2', 'Tiền hoàn được Moni xử lý tự động vào thứ 2 hàng tuần. Cập nhật đầy đủ thông tin tài khoản ngân hàng trong app để nhận tiền.'),
    ]},
    {'id': 'cau-hoi-thuong-gap', 'toc': 'Câu hỏi thường gặp', 'h': 'Câu hỏi thường gặp', 'faq': True},
]
FAQ = [
    ('Hoàn tiền Shopee qua Moni có thật không?', 'Có. Moni là đối tác affiliate chính thức của Shopee. Khi bạn mua hàng qua link Moni tạo ra, Shopee trả hoa hồng cho Moni và Moni chia sẻ lại cho bạn dưới dạng hoàn tiền.'),
    ('Hoàn được bao nhiêu phần trăm mỗi đơn Shopee?', 'Tỷ lệ hoàn tiền phụ thuộc vào từng sản phẩm và chiến dịch của Shopee, thường từ 2–15%. Tỷ lệ cụ thể hiển thị trong mục Hoàn tiền Shopee của app Moni.'),
    ('Hoàn tiền Shopee mất bao lâu?', 'Đơn hàng sẽ hiển thị trên hệ thống Moni vào ngày hôm sau khi bạn đặt hàng. Tiền hoàn sẽ được Moni xử lý tự động vào thứ 2 hàng tuần. Bạn cần cập nhật đầy đủ thông tin tài khoản nhận tiền trong app để nhận hoàn tiền.'),
    ('Moni lấy tiền từ đâu để hoàn tiền cho tôi?', 'Shopee trả hoa hồng affiliate cho Moni khi bạn mua hàng qua link được tạo từ Moni. Moni chia sẻ hoa hồng này lại cho bạn. Bạn không mất thêm tiền nào cả.'),
    ('Rút tiền hoàn về ngân hàng có mất phí không?', 'Không mất phí. Tiền hoàn được Moni xử lý tự động vào thứ 2 hàng tuần và chuyển về tài khoản ngân hàng của bạn. Bạn cần cập nhật đầy đủ thông tin tài khoản nhận tiền (số tài khoản, ngân hàng) trong app Moni để nhận tiền.'),
    ('Cách 2 có hoạt động trên Android không?', 'Cách 2 sử dụng iOS Share Extension, chỉ hoạt động trên iPhone/iPad. Người dùng Android vui lòng dùng Cách 1: copy link sản phẩm và dán vào app Moni.'),
]
VIDEO = {'id': 'pBxaav5qT0Y', 'date': '2026-12-13', 'title': ('Hoàn tiền Shopee và TikTok', 'Shopee and TikTok cashback')}

# Red callouts drawn over the screenshots, positioned in % of the image.
STYLE = '''  <style>
    .gd-annot .phone-screen { position: relative; overflow: hidden; border: 5px solid #0f172a; border-radius: 1.6rem; box-shadow: 0 18px 40px rgba(15, 23, 42, 0.18); }
    .gd-annot .phone-screen img { border: 0; border-radius: 0; box-shadow: none; }
    .gd-shots .gd-annot { max-width: 15rem; }
    .annot-circle, .annot-rect, .annot-badge { position: absolute; pointer-events: none; }
    .annot-circle { border: 3px solid #ff3b30; border-radius: 50%; transform: translate(-50%, -50%); aspect-ratio: 1; }
    .annot-rect { border: 3px solid #ff3b30; border-radius: 5%; }
    .annot-badge { width: 6%; aspect-ratio: 1; background: #ff3b30; border-radius: 50%; color: #fff; font-size: 60%; font-weight: 800;
      display: flex; align-items: center; justify-content: center; transform: translate(-50%, -50%); line-height: 1; }
  </style>
'''


def annotated(img, alt, cap, marks):
    w, h = g.dims(img.split('?')[0])
    return (f'<figure class="cp-shot gd-shot gd-annot"><button type="button" class="gd-zoom" aria-label="Phóng to ảnh"><div class="phone-screen">'
            f'<img src="{img}" alt="{g.esc(alt)}" width="{w}" height="{h}" loading="lazy">{marks}</div></button>'
            f'<figcaption>{g.esc(cap)}</figcaption></figure>')


def nav():
    links = (('/', 'Trang chủ'), ('/videos/', 'Video hướng dẫn'))
    desk = ''.join(f'<a class="nav-link text-white/80 hover:text-white text-sm font-medium" href="{u}">{t}</a>' for u, t in links)
    mob = ''.join(f'<a class="mobile-menu-link" href="{u}">{t}</a>' for u, t in links)
    return f'''<body>
  <nav class="nav py-4" id="navbar">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between">
      <a href="/" class="flex items-center gap-3">
        <img src="/images/logo.png" alt="Moni" class="w-10 h-10 rounded-xl" width="40" height="40">
        <span class="text-white font-bold text-xl">Moni</span>
      </a>
      <div class="hidden md:flex items-center gap-8">
        {desk}
        <a class="btn-gold text-sm" href="https://moni.live/download" target="_blank" rel="noopener noreferrer">Tải miễn phí</a>
      </div>
      <button class="hamburger md:hidden" id="hamburger-btn" aria-label="Toggle menu"><span></span><span></span><span></span></button>
    </div>
  </nav>
  <div class="mobile-menu" id="mobile-menu">
    {mob}
    <a class="btn-gold text-lg" href="https://moni.live/download" target="_blank" rel="noopener noreferrer">Tải miễn phí</a>
  </div>
'''


def main():
    old = open(PAGE, encoding='utf-8').read()
    head = old[:old.index('  <link rel="preconnect" href="https://fonts.googleapis.com">')]
    head += f'''  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="{g.FONTS}" rel="stylesheet" media="print" onload="this.media='all'">
  <noscript><link href="{g.FONTS}" rel="stylesheet"></noscript>
  <link rel="icon" href="/favicon.ico">
  <link rel="stylesheet" href="/css/tailwind-compiled.css">
  <link rel="stylesheet" href="/css/styles.css">
  <link rel="stylesheet" href="/css/couple.css">
  <link rel="stylesheet" href="/css/guide.css">
{STYLE}</head>
'''
    en = {}
    p = g.Page(en)
    words = sum(len(g.html.unescape(x).split()) for s in SECTIONS for x in s.get('steps', [])) + sum(len(a.split()) + len(q.split()) for q, a in FAQ)
    hero_shot = f'<figure class="cp-shot"><img src="{IMG1}" alt="" width="1179" height="2556"></figure>'
    out = [head, nav(),
           g.guide_hero(p, ('Hoàn tiền Shopee', 'crumb.feature'), '/affiliate-guide/', 'Hướng dẫn kiếm hoàn tiền Shopee qua Moni',
                        'Mua sắm trên Shopee qua Moni và kiếm hoàn tiền mỗi đơn hàng. Chỉ cần 2 bước đơn giản!',
                        [s['id'] for s in SECTIONS], ['cach-hoat-dong'], g.read_minutes(words), hero_shot),
           g.guide_open([(s['id'], s['toc']) for s in SECTIONS])]
    for n, s in enumerate(SECTIONS, 1):
        body = [g.sec_head(n, f'<h2 class="gd-h2">{g.esc(s["h"])}</h2>')]
        if s.get('video'):
            body.append(g.video_block(p, 'g.video', VIDEO))
        if s.get('lead'):
            body.append(f'<p class="gd-lead-dark">{g.esc(s["lead"])}</p>')
        if s.get('note'):
            body.append(g.callout(s['note'][0], f'<p>{g.esc(s["note"][1])}</p>'))
        if s.get('steps'):
            body.append('<ol class="gd-steps">' + ''.join(f'<li>{x}</li>' for x in s['steps']) + '</ol>')
        if s.get('shot'):
            body.append('<div class="gd-shots">' + annotated(*s['shot']) + '</div>')
        for kind, title, text in s.get('notes', []):
            body.append(g.callout(kind, f'<p><strong>{g.esc(title)}.</strong> {g.esc(text)}</p>'))
        if s.get('faq'):
            body.append('<div class="space-y-3">\n' + g.faq_items(p, [((q, q), (a, a)) for q, a in FAQ]) + '\n      </div>')
        if n < len(SECTIONS):
            body.append(g.next_link(SECTIONS[n]['id'], SECTIONS[n]['toc']))
        out.append(f'      <section class="gd-sec" id="{s["id"]}">{"".join(body)}</section>\n')
    out.append(g.guide_close('affiliate', en))
    out.append(f'''  <section class="cta-section py-20 lg:py-28" id="download">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center relative z-10">
      <p class="text-gold font-mono text-sm font-medium tracking-wider uppercase mb-4">Sẵn sàng chưa?</p>
      <h2 class="font-display text-3xl sm:text-4xl lg:text-5xl font-extrabold text-white mb-6">Bắt đầu kiếm hoàn tiền ngay!</h2>
      <p class="text-white/60 text-lg max-w-lg mx-auto mb-10">Tải Moni miễn phí và bắt đầu kiếm hoàn tiền từ mỗi đơn hàng Shopee.</p>
      {g.stores('justify-center')}
    </div>
  </section>
{g.GUIDE_TAIL}  <footer class="footer py-12">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex flex-col sm:flex-row items-center justify-between gap-6">
        <a href="/" class="flex items-center gap-3"><img src="/images/logo.png" alt="Moni" class="w-8 h-8 rounded-lg" width="32" height="32"><span class="text-white font-bold text-lg">Moni</span></a>
        <ul class="flex flex-wrap justify-center gap-6 text-sm">
          <li><a href="/">Trang chủ</a></li>
          <li><a href="/videos/">Video hướng dẫn</a></li>
          <li><a href="/privacy-policy.html">Chính sách bảo mật</a></li>
          <li><a href="mailto:moni.support@gmail.com">moni.support@gmail.com</a></li>
        </ul>
      </div>
      <div class="border-t border-white/10 mt-8 pt-6 text-center"><p class="text-sm">© 2026 Code4change. Bảo lưu mọi quyền.</p></div>
    </div>
  </footer>
  <script src="/js/video-embed.js" defer></script>
  <script src="/js/main.js"></script>
  <script src="/js/guide.js" defer></script>
</body>
</html>
''')
    open(PAGE, 'w', encoding='utf-8').write(''.join(out))
    print('built affiliate guide:', len(SECTIONS), 'sections')


if __name__ == '__main__':
    main()
