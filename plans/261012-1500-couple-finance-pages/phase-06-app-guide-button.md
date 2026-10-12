---
phase: 6
title: App guide button
status: completed
priority: P2
effort: S
dependencies:
  - 3
---

# Phase 6: App guide button

## Overview
Thêm nút "Hướng dẫn" ở màn tài chính cặp đôi trong repo app (`/Users/rotationba/Luan/money-mate`), mở `https://moni.live/couple/guide/#ket-noi`.

## Requirements
- Functional: nút trong `app/couple/index.tsx` (cả trạng thái chưa kết nối và đã kết nối) mở link bằng `Linking.openURL` (đúng pattern `app/cashback-redirect.tsx:90`). Có thể trỏ anchor khác theo ngữ cảnh (`#hoan-ung` ở màn yêu cầu hoàn).
- Non-functional: thêm khóa i18n ở đủ 10 locale (de, en, es, fr, ja, ko, pt, th, vi, zh) theo quy ước repo; chỉ JS nên OTA được, không cần build store. Landing chỉ có vi/en: các locale khác vẫn mở trang vi (mặc định).

## Related Code Files
- Modify: `app/couple/index.tsx` (ScreenHeader dòng ~223 và ~265), `app/couple/requests/index.tsx`, `src/i18n/locales/*.json` (khóa `couple.guide`).

## Implementation Steps
1. Quyết định vị trí (icon "?" cạnh tiêu đề hoặc dòng link cuối màn), bám `ScreenHeader` hiện có.
2. Mở link bằng `Linking.openURL(...).catch(() => {})`; không dùng WebView.
3. Thêm khóa i18n 10 locale; chạy test i18n parity có sẵn nếu có.
4. Test thiết bị: bấm nút mở trình duyệt đúng URL + anchor.

## Success Criteria
- [ ] Nút hiển thị và mở đúng URL trên iOS và Android
- [ ] 10 locale đủ khóa
- [ ] Không commit/OTA khi user chưa test; chỉ bật sau khi landing đã deploy (tránh link 404)

## Risk Assessment
- Link 404 nếu OTA trước khi landing deploy: bắt buộc deploy landing trước.
