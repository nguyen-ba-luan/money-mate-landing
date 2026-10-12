---
phase: 5
title: Verify
status: completed
priority: P1
effort: S
dependencies:
  - 4
---

# Phase 5: Verify

## Overview
Kiểm tra trong Chrome (user yêu cầu luôn mở Chrome review UI) rồi giao user test. Không commit/deploy khi chưa được duyệt.

## Implementation Steps
1. Chạy `python3 -m http.server` cục bộ; mở `/couple/`, `/couple/guide/`, `/`, `/vi/`, `/invite/?code=ABCD1234`.
2. Mỗi trang: viewport 375 và 1280, toggle vi/en, kiểm console, ảnh vỡ, tràn ngang, `data-i18n` còn trần.
3. Mở từng URL guide kèm `#anchor`.
4. Parse JSON-LD mọi trang bằng node; kiểm `i18n.js` bằng `vm`.
5. Rà từng khẳng định FAQ với fact sheet.
5b. View-source `/couple/` và `/couple/guide/` xác nhận tiếng Việt trong HTML gốc.
6. Tắt server; báo cáo; chờ user test trước khi commit/push (GitHub Pages).

## Success Criteria
- [ ] Không lỗi console, không ảnh vỡ, không tràn ngang
- [ ] vi/en đầy đủ
- [ ] JSON-LD + sitemap hợp lệ
- [ ] Đủ 8 ảnh thật, không còn ô trống trước khi deploy
- [ ] User đã test và duyệt trước khi commit
