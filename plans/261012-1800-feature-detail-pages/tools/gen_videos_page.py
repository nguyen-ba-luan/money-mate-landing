"""Generate /videos/index.html (all YouTube guide videos by playlist) + js/videos-en.js.

Usage: python3 gen_videos_page.py   (run from the tools dir). Reuses head/nav/footer of gen_feature_pages.
Cards show the local poster; before the publish time (19:00 GMT+7) the card is labelled "coming"
and is not playable, afterwards js/video-embed.js loads the YouTube player on click.
"""
import json, os, re
import gen_feature_pages as G
from gen_feature_pages import esc, Page

CHANNEL = 'https://www.youtube.com/@MoniAppVN'
SPEC = {
    'slug': 'videos',
    'meta_title': 'Video hướng dẫn dùng Moni - Quản lý chi tiêu, nhóm, cặp đôi | Moni',
    'meta_desc': 'Xem video ngắn hướng dẫn từng tính năng của Moni: ghi chi tiêu, ngân sách, tiết kiệm, chia tiền nhóm, tài chính cặp đôi, hoàn tiền Shopee và TikTok.',
    'foot_intro': ('Video hướng dẫn', 'Video guides'),
    'foot_guide': ('Kênh YouTube', 'YouTube channel'),
    'og_alt': 'Video hướng dẫn dùng app Moni',
}
PLAYLISTS = [
    ('ca-nhan', ('Chi tiêu cá nhân', 'Personal spending'), ('Ghi chi tiêu, đặt ngân sách, tiết kiệm và theo dõi giá vàng.', 'Track spending, set budgets, save and follow gold prices.')),
    ('nhom-cap-doi', ('Nhóm và cặp đôi', 'Groups and couples'), ('Chia tiền khi đi chơi, quỹ nhóm và chi tiêu chung của hai người.', 'Split costs on trips, group funds and shared spending for two.')),
    ('tien-ich', ('Tiện ích', 'Extras'), ('Bảo mật, đồng bộ, widget, tự ghi từ thông báo ngân hàng, quét QR thanh toán, bản đồ chi tiêu, hoàn tiền và Moni trên web.', 'Security, sync, widgets, bank auto-log, scan-to-pay QR, spending map, cashback and Moni on the web.')),
]
# (playlist, youtube id, publish date, title vi/en, hook vi/en, related guide page or None); one per day from 22/11/2026
VIDEOS = [
    ('ca-nhan', 'xQgsCwSZHco', '2026-11-22', ('Moni: Quản lý chi tiêu thật dễ', 'Moni: spending made easy'), ('Tiền đi đâu hết rồi? Moni giúp bạn biết rõ từng đồng.', 'Where did the money go? Moni shows you every dong.'), None),
    ('ca-nhan', 'zdjgbBdpOE8', '2026-11-23', ('Bắt đầu nhanh', 'Quick start'), ('Tiền đi đâu hết mỗi tháng? Moni giúp bạn biết, chỉ trong vài giây.', 'Where does the money go each month? Moni tells you in seconds.'), None),
    ('ca-nhan', 'e8MdrDVgIbI', '2026-11-24', ('Danh mục tùy chỉnh', 'Custom categories'), ('Danh mục có sẵn không hợp ý? Bạn tự tạo danh mục của riêng mình.', 'Built-in categories not quite right? Create your own.'), None),
    ('ca-nhan', 'p3no5FciK78', '2026-11-25', ('Ngân sách', 'Budgets'), ('Cuối tháng hết tiền mà không biết đi đâu? Đặt ngân sách để Moni canh giúp.', 'Broke by month end? Set a budget and let Moni keep watch.'), '/budget/guide/'),
    ('ca-nhan', 'na9rFLUEWMw', '2026-11-26', ('Phân tích và báo cáo', 'Analytics and reports'), ('Tiền tiêu vào đâu nhiều nhất? Xem biểu đồ là biết ngay.', 'Where do you spend the most? The charts show you at a glance.'), '/analytics/guide/'),
    ('ca-nhan', '5vpx3JSNfi4', '2026-11-27', ('Chi tiêu định kỳ', 'Recurring spending'), ('Tiền nhà, Netflix, mỗi tháng đều phải ghi lại? Để Moni tự lo.', 'Rent, Netflix, logged by hand every month? Let Moni do it.'), '/recurring/guide/'),
    ('ca-nhan', 'v4VmKUb1aOc', '2026-11-28', ('Sự kiện sắp tới', 'Upcoming events'), ('Sắp tới đám cưới, sinh nhật, Tết? Báo trước để không bị bất ngờ.', 'A wedding, birthday or Tet coming up? Plan ahead, no surprises.'), None),
    ('ca-nhan', '3qCLWZWBdAE', '2026-11-29', ('Tiết kiệm', 'Savings'), ('Muốn mua đồ lớn mà tiền cứ trôi mất? Đặt mục tiêu tiết kiệm đi.', 'Saving for something big? Set a savings goal.'), '/savings/guide/'),
    ('ca-nhan', 'IKY6snglJ-g', '2026-11-30', ('Quản lý nợ', 'Debts'), ('Cho bạn mượn tiền rồi quên mất? Ghi nợ vào Moni cho chắc.', 'Lent a friend money and forgot? Note it in Moni.'), None),
    ('ca-nhan', '67y6oTZCKPo', '2026-12-01', ('Thử thách', 'Challenges'), ('Tháng nào cũng lỡ tay tiêu quá? Thử thách giúp bạn kiềm lại.', 'Overspending every month? A challenge helps you hold back.'), None),
    ('ca-nhan', 'BfsUD85ih3k', '2026-12-02', ('Công thức quản lý tiền', 'Money-management formulas'), ('Có thu nhập mà không biết chia thế nào? Dùng công thức có sẵn.', 'Not sure how to split your income? Use a ready-made formula.'), '/budget/guide/#cong-thuc'),
    ('ca-nhan', 'NumdiDjsbYQ', '2026-12-03', ('Giá vàng', 'Gold prices'), ('Muốn biết giá vàng hôm nay mà phải lướt nhiều trang? Xem ngay trong Moni.', "Today's gold price without hopping between sites? Check it in Moni."), '/gold/guide/'),
    ('ca-nhan', '-NQiNx513gY', '2026-12-16', ('Quét hóa đơn', 'Scan receipts'), ('Lười gõ từng khoản? Chụp hóa đơn, Moni tự đọc số tiền cho bạn.', 'Too lazy to type every expense? Snap the receipt and Moni reads the amount.'), None),
    ('nhom-cap-doi', '8n-Wvbssxag', '2026-12-04', ('Tạo nhóm và mời bạn bè', 'Create a group and invite friends'), ('Đi chơi chung, ai trả bao nhiêu? Moni tính giúp bạn, không cần máy tính.', 'Out with friends, who paid what? Moni does the maths.'), '/groups/guide/'),
    ('nhom-cap-doi', '-Fps8CbJ63A', '2026-12-05', ('Thêm khoản chi và thanh toán', 'Add costs and settle up'), ('Ăn xong ai trả? Ghi một lần, Moni chia sẵn cho cả nhóm.', 'Who pays after dinner? Log it once, Moni splits it for everyone.'), '/groups/guide/#them-chi-tieu'),
    ('nhom-cap-doi', 'BzAcl17PZgM', '2026-12-06', ('Tổng kết chuyến đi', 'Trip summary'), ('Đi chơi về, ai chi nhiều nhất? Moni tổng kết cho bạn.', 'Back from the trip, who spent the most? Moni sums it up.'), '/groups/guide/#tong-ket'),
    ('nhom-cap-doi', 'bUY2WX9yoY0', '2026-12-07', ('Quỹ nhóm nạp và rút', 'Group fund deposits and withdrawals'), ('Cả nhóm cùng góp tiền cho một mục tiêu? Quỹ nhóm lo việc đó.', 'Pooling money for a shared goal? A group fund handles it.'), None),
    ('nhom-cap-doi', 'MeIbyKNR5QI', '2026-12-08', ('Ghép đôi với người ấy', 'Pair up with your partner'), ('Hai người, một ví chung. Ghép đôi trong Moni chỉ mất một phút.', 'Two people, one shared wallet. Pairing takes a minute.'), '/couple/guide/'),
    ('nhom-cap-doi', 'OGq-Sh-eFGk', '2026-12-09', ('Chi tiêu chung và hoàn ứng', 'Shared spending and reimbursement'), ('Ai ứng tiền trước? Moni giúp hai người tính rõ ràng, không giận nhau.', 'Who paid up front? Moni keeps it clear between the two of you.'), '/couple/guide/#chi-tieu-chung'),
    ('tien-ich', 'tGakdssNDBw', '2026-12-10', ('Khóa bảo mật', 'App lock'), ('Điện thoại lọt vào tay người khác, dữ liệu tiền bạc của bạn có lộ không?', 'If someone else picks up your phone, is your money data safe?'), None),
    ('tien-ich', 'akdOBQfmv-8', '2026-12-11', ('Đồng bộ và đổi ngôn ngữ', 'Sync and language'), ('Đổi điện thoại hay dùng hai máy, dữ liệu chi tiêu có đi theo bạn không?', 'New phone or two devices, does your data come along?'), None),
    ('tien-ich', 'LUZ2K0ArxlE', '2026-12-17', ('Widget', 'Widgets'), ('Muốn xem chi tiêu mà không cần mở app? Thêm widget Moni ra màn hình chính.', 'Check your spending without opening the app: add a Moni widget to your home screen.'), None),
    ('tien-ich', 'yPDwLlu_gkY', '2026-12-12', ('Bản đồ chi tiêu', 'Spending map'), ('Tháng này bạn tiêu ở đâu nhiều nhất? Bản đồ chi tiêu cho bạn thấy ngay.', 'Where did you spend the most this month? The map shows you.'), None),
    ('tien-ich', 'pBxaav5qT0Y', '2026-12-13', ('Hoàn tiền Shopee và TikTok', 'Shopee and TikTok cashback'), ('Mua Shopee, TikTok Shop mà được hoàn tiền? Moni làm được, nhưng chỉ ở Việt Nam.', 'Cashback on Shopee and TikTok Shop? Moni does it, in Vietnam only.'), '/affiliate-guide/'),
    ('tien-ich', '8q2Yw_wX1a4', '2026-12-14', ('Giới thiệu bạn bè', 'Refer friends'), ('Mời bạn bè dùng Moni để nhận hoa hồng mỗi khi bạn bè mua sắm.', 'Invite friends to Moni and earn a commission when they shop.'), None),
    ('tien-ich', 'M36612lfOUg', '2026-12-18', ('Tự ghi từ thông báo ngân hàng', 'Auto-log from bank alerts'), ('Chuyển khoản xong là Moni tự ghi khoản chi, không cần mở app.', 'Make a transfer and Moni logs the expense for you, no app opening needed.'), None),
    ('tien-ich', '5t6HaOBbP4M', '2026-12-19', ('Quét QR thanh toán', 'Scan-to-pay QR'), ('Trả tiền bằng mã QR mà vẫn muốn ghi chi tiêu? Quét mã ngay trong Moni.', 'Paying by QR but still want it logged? Scan the code inside Moni.'), None),
    ('tien-ich', 'WEOCMnC3kjY', '2026-12-15', ('Moni trên web', 'Moni on the web'), ('Không có điện thoại bên cạnh? Bạn vẫn dùng Moni được trên trình duyệt.', 'No phone at hand? Use Moni in your browser.'), None),
]
POSTERS = G.POSTERS


def card(p, i, v):
    pl, vid, date, title, hook, guide = v
    d = date.split('-'); soon_vi = f'Lên sóng 19:00 {int(d[2])}/{int(d[1])}'
    p.en[f'v{i}.t'], p.en[f'v{i}.h'] = title[1], hook[1]
    p.en[f'v{i}.soon'] = f'Coming {int(d[2])}/{int(d[1])} at 19:00'
    link = ''
    if guide:
        p.en[f'v{i}.g'] = 'Read the written guide →'
        link = f'<a class="cp-video-guide" href="{guide}" data-i18n="v{i}.g">Đọc hướng dẫn chi tiết →</a>'
    return (f'<article class="cp-video-card"><figure class="cp-video" data-yt="{vid}" data-publish="{date}T19:00:00+07:00" data-soon>'
            f'<button type="button" class="cp-video-btn" aria-label="{esc(title[0])}">'
            f'<img src="/images/videos/{POSTERS[vid]}.webp" alt="" width="960" height="540" loading="lazy">'
            f'<span class="cp-video-play" aria-hidden="true"></span>'
            f'<span class="cp-video-soon" data-i18n="v{i}.soon">{soon_vi}</span></button></figure>'
            f'<h3 class="cp-video-title" data-i18n="v{i}.t">{esc(title[0])}</h3>'
            f'<p class="cp-video-hook" data-i18n="v{i}.h">{esc(hook[0])}</p>{link}</article>')


def build(en):
    s = SPEC; p = Page(en); url = 'https://moni.live/videos/'
    def jsonld(title, desc, u):
        return [{'@context': 'https://schema.org', '@type': 'CollectionPage', 'name': title, 'description': desc, 'url': u, 'inLanguage': 'vi'},
                {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
                    {'@type': 'ListItem', 'position': 1, 'name': 'Moni', 'item': 'https://moni.live/'},
                    {'@type': 'ListItem', 'position': 2, 'name': 'Video hướng dẫn', 'item': u}]}]
    out = [G.head(s, 'intro', jsonld)]
    # Nav/footer of the feature generator link Overview/Guide; here: Home + Videos only
    nv = G.nav(s)
    nv = re.sub(r'<a class="nav-link[^"]*" data-i18n="nav.guide" href="/videos/guide/">Hướng dẫn</a>', '', nv)
    nv = re.sub(r'<a class="mobile-menu-link" data-i18n="nav.guide.m" href="/videos/guide/">Hướng dẫn</a>', '', nv)
    nv = nv.replace('>Giới thiệu</a>', '>Video hướng dẫn</a>')
    out.append(nv)
    en['nav.intro'] = en['nav.intro.m'] = 'Video guides'
    p.en['vh.title'], p.en['vh.desc'] = 'Moni video guides', 'Short videos showing each Moni feature, step by step. A new episode every evening at 19:00.'
    p.en['vh.yt'] = 'Subscribe on YouTube'
    out.append(f'''  <section class="hero-gradient cp-hero cp-hero-sm pt-28 pb-24" id="hero">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
      <nav aria-label="breadcrumb" class="cp-crumbs"><a href="/">Moni</a><span>/</span><span data-i18n="nav.intro">Video hướng dẫn</span></nav>
      <h1 class="font-display text-4xl sm:text-5xl font-extrabold text-white leading-tight mb-5" data-i18n="vh.title">Video hướng dẫn dùng Moni</h1>
      <p class="text-white/70 text-lg max-w-2xl mx-auto mb-8" data-i18n="vh.desc">Video ngắn chỉ từng tính năng của Moni, từng bước một. Mỗi tối 19:00 có tập mới.</p>
      <a class="btn-gold" href="{CHANNEL}" target="_blank" rel="noopener noreferrer" data-i18n="vh.yt">Theo dõi trên YouTube</a>
    </div>
  </section>
''')
    out.append('  <main class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-16">\n')
    for pid, name, desc in PLAYLISTS:
        p.en[f'pl.{pid}.h'], p.en[f'pl.{pid}.d'] = name[1], desc[1]
        cards = [card(p, i, v) for i, v in enumerate(VIDEOS, 1) if v[0] == pid]
        out.append(f'    <section class="cp-video-pl" id="{pid}"><h2 class="cp-h3" data-i18n="pl.{pid}.h">{esc(name[0])}</h2>'
                   f'<p class="text-gray-500 mb-6" data-i18n="pl.{pid}.d">{esc(desc[0])}</p><div class="cp-video-grid">{"".join(cards)}</div></section>\n')
    out.append('  </main>\n')
    out.append(f'''  <section class="cta-section py-20 lg:py-28" id="download">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center relative z-10">
      <p class="text-gold font-mono text-sm font-medium tracking-wider uppercase mb-4"><span data-i18n="cta.tagline">Sẵn sàng chưa?</span></p>
      <h2 class="font-display text-3xl sm:text-4xl lg:text-5xl font-extrabold text-white mb-6" data-i18n="cta.title">Tải Moni và làm theo ngay</h2>
      <p class="text-white/60 text-lg max-w-lg mx-auto mb-10" data-i18n="cta.desc">Miễn phí trên iPhone và Android.</p>
      {G.stores('justify-center')}
    </div>
  </section>
''')
    en['cta.title'], en['cta.desc'] = 'Get Moni and follow along', 'Free on iPhone and Android.'
    ft = G.footer(s, p).replace('<a href="/videos/guide/" ', f'<a href="{CHANNEL}" target="_blank" rel="noopener noreferrer" ')
    out.append(ft)
    return ''.join(out)


def main():
    en = dict(G.COMMON_EN)
    en['foot.intro'], en['foot.guide'] = SPEC['foot_intro'][1], SPEC['foot_guide'][1]
    page = build(en)
    path = os.path.join(G.ROOT, 'videos', 'index.html'); os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w', encoding='utf-8').write(page)
    body = ',\n'.join(f'  {json.dumps(k, ensure_ascii=False)}: {json.dumps(v, ensure_ascii=False)}' for k, v in en.items())
    open(os.path.join(G.ROOT, 'js', 'videos-en.js'), 'w', encoding='utf-8').write(
        f'// English strings for /videos/. Vietnamese lives in the HTML.\nwindow.PAGE_EN = {{\n{body}\n}};\n')
    print('generated videos', len(VIDEOS), 'videos', len(en), 'en keys')


if __name__ == '__main__':
    main()
