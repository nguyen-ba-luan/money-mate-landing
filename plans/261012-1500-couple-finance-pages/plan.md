---
title: Couple finance intro + guide pages
description: >-
  Trang giới thiệu /couple/ và hướng dẫn /couple/guide/ cho Tài chính cặp đôi,
  vi+en, nối với trang chủ, sitemap, /invite/
status: completed
priority: P2
branch: main
tags:
  - landing
  - couple
  - seo
  - i18n
blockedBy: []
blocks: []
created: '2026-10-12T02:31:00.135Z'
createdBy: 'ck:plan'
source: skill
---

# Couple finance intro + guide pages

Brainstorm: [brainstorm-261012-couple-finance-pages.md](../reports/brainstorm-261012-couple-finance-pages.md)

## Overview

Thêm 2 trang tĩnh vào landing: `/couple/` (giới thiệu, SEO, index) và `/couple/guide/` (hướng dẫn từng bước, anchor cho deep link từ app). Ngôn ngữ: HTML lưu sẵn tiếng Việt (`lang="vi"`), tiếng Anh qua `js/i18n.js` khi bấm EN. Ảnh do user chụp.

**Thay đổi so với brainstorm:** bỏ `/couple/invite/`. Link mời cặp đôi trong app dùng chung `https://moni.live/invite/?code=` với nhóm (`src/lib/api/group-invitations.ts:64`), mã không phân biệt loại, nên không thể trỏ riêng. Thay bằng: thêm khối "Moni là gì + link sang /couple/ và /couple/guide/#tham-gia" vào `/invite/` hiện có.

## Phases

| Phase | Name | Status |
|-------|------|--------|
| 1 | [Content and assets](./phase-01-content-and-assets.md) | Completed |
| 2 | [Intro page couple](./phase-02-intro-page-couple.md) | Completed |
| 3 | [Guide page couple guide](./phase-03-guide-page-couple-guide.md) | Completed |
| 4 | [Wire up site and SEO](./phase-04-wire-up-site-and-seo.md) | Completed |
| 5 | [Verify](./phase-05-verify.md) | Completed |
| 6 | [App guide button](./phase-06-app-guide-button.md) | Completed |

## Dependencies

- Phase 1 chờ user chụp 8 ảnh (có thể dùng ô trống tạm để phase 2-3 chạy trước).
- Phase 6 độc lập với phase 2-5 về code nhưng link chỉ hoạt động sau khi landing deploy.
- Phase 2, 3 độc lập sau phase 1 (khác file). Phase 4 sau cả hai.
- Không chặn/bị chặn bởi plan nào khác (`260314-1757-landing-page-redesign` đã xong phần liên quan, không đụng file mới).

## Acceptance criteria

- `/couple/` và `/couple/guide/` hiển thị đúng vi và en, không vỡ ở 375px và 1280px, không lỗi console, không ảnh vỡ.
- Mỗi bước guide có anchor hoạt động; mục lục cuộn tới đúng chỗ.
- JSON-LD (WebPage/FAQPage/HowTo) parse hợp lệ; sitemap có 2 URL mới; canonical + hreflang đúng.
- Nội dung khớp hành vi thật trong app (riêng tư, hoàn ứng, ngắt kết nối).
- HTML gốc của 2 trang chứa tiếng Việt thật (crawler đọc được vi), không có `/vi/couple/`.
- Không deploy cho đến khi đủ 8 ảnh thật (ô trống chỉ dùng khi dev).
- Nút Hướng dẫn trong app mở được `/couple/guide/#ket-noi`.
- Không commit/deploy khi user chưa test.

## Validation Log

### Session 1 (2026-10-12)

#### Verification Results
- Claims checked: 10 | Verified: 10 | Failed: 0 | Unverified: 0 | Tier: Full (lấy mẫu)
- Lệch nhỏ đã sửa: `affiliate-guide/` KHÔNG dùng i18n (chỉ vi); bám `index.html`, không bám affiliate-guide.

#### Decisions
1. Ngôn ngữ mặc định: tiếng Việt trong HTML, en qua i18n. Bỏ câu hỏi `/vi/couple/`. Lý do: trang chủ mặc định en nên phải có `/vi/` tĩnh; trang này nhắm VN nên bake vi.
2. Ảnh: dựng ô trống trước, thay sau; KHÔNG deploy khi chưa đủ ảnh.
4. Kỹ thuật i18n: `js/i18n.js` bỏ qua key thiếu → không dùng cho 2 trang mới; dùng `js/page-i18n.js` + `js/couple-en.js` (vi nằm trong HTML, en trong từ điển).
3. Nút Hướng dẫn trong app: làm luôn, thêm phase 6 (repo app).

#### Whole-Plan Consistency Sweep
- Đã đọc plan.md + 6 phase; đã bỏ mọi chỗ nói tới `/vi/couple/`, HTML mặc định en. Không còn mâu thuẫn.

