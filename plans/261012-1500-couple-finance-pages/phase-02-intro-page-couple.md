---
phase: 2
title: Intro page couple
status: completed
priority: P1
effort: M
dependencies:
  - 1
---

# Phase 2: Intro page couple

## Overview
Trang `/couple/` để chuyển đổi và SEO. Khối nổi nhất: hoàn ứng qua VietQR.

## Requirements
- Functional: hero (headline "Cùng nhau, tiền bạc rõ ràng hơn", nút tải), vấn đề, 6 khối tính năng, 3 bước, FAQ, CTA, link sang guide.
- Non-functional: bám style trang chủ/affiliate-guide; chỉ dùng class Tailwind đã build; HTML gốc chứa tiếng Việt thật + `lang="vi"`; en qua `data-i18n` (từ điển en), toggle ngôn ngữ như trang chủ.
<!-- Updated: Validation Session 1 - vi baked into HTML, no /vi/couple/ -->

## Architecture
Tĩnh `couple/index.html`, load `/css/tailwind-compiled.css`, `/js/i18n.js`, `/js/main.js`. KHÔNG sửa `js/i18n.js` (nó bỏ qua key thiếu nên không khôi phục được vi sau khi chuyển EN). Thay bằng `js/page-i18n.js` dùng chung cho 2 trang: lần đầu lưu text vi gốc vào `data-vi`, từ điển en nằm ở `js/couple-en.js`; đọc/ghi `localStorage mm-lang` như trang chủ. Bản vi chỉ tồn tại một chỗ (HTML). Meta/JSON-LD viết bằng tiếng Việt, `og:locale` vi_VN, hreflang vi + x-default. Dùng `/`-tuyệt đối cho tài nguyên để khỏi lỗi đường dẫn.

## Related Code Files
- Create: `couple/index.html`
- Create: `js/page-i18n.js`, `js/couple-en.js` (từ điển en cho cả 2 trang)
- Reference: `index.html` (header/footer/CTA), `affiliate-guide/index.html`

## Implementation Steps
1. Sao khung header/footer/nút tải từ `index.html`.
2. Viết 6 khối tính năng + khối hoàn ứng lớn (3 bước QR) + FAQ (nguồn: fact sheet).
3. Viết `page-i18n.js` + `couple-en.js`; kiểm tra cú pháp bằng node; thử vi→en→vi không mất bản vi.
4. Meta: title/description/canonical `https://moni.live/couple/`, og, hreflang vi/x-default.
5. JSON-LD: WebPage + FAQPage (+ BreadcrumbList).
6. Ảnh có `alt`, `width/height`, `loading="lazy"` (trừ hero).

## Success Criteria
- [ ] Render đúng ở 375/768/1280px, không tràn ngang
- [ ] Toggle vi/en đổi toàn bộ chữ, không còn khóa trần
- [ ] View-source thấy tiếng Việt thật (không phải khóa/tiếng Anh)
- [ ] JSON-LD hợp lệ
- [ ] Không dùng class Tailwind chưa build (cyan/fuchsia)

## Risk Assessment
- Class mới thiếu trong CSS build: dùng class sẵn có hoặc chạy build `tailwind` trong repo.
- `i18n.js` phình: chấp nhận; nếu >60KB thêm thì tách `js/i18n-couple.js`.
