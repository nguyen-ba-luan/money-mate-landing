---
phase: 3
title: Guide page couple guide
status: completed
priority: P1
effort: M
dependencies:
  - 1
---

# Phase 3: Guide page couple guide

## Overview
Trang `/couple/guide/` hướng dẫn từng bước; mỗi bước có anchor ổn định để app trỏ tới.

## Requirements
- Functional: anchors `#ket-noi #tham-gia #thiet-lap-quy #chi-tieu-chung #quyet-toan #hoan-ung #thanh-toan-gop #quyen-rieng-tu #ngat-ket-noi #cau-hoi-thuong-gap`; mục lục dính (desktop) / chip cuộn ngang (mobile); mỗi bước: mô tả ngắn, ảnh, lưu ý.
- Non-functional: id anchor KHÔNG đổi theo ngôn ngữ (ổn định cho deep link); HTML gốc chứa tiếng Việt thật + `lang="vi"`; en qua `data-i18n`.
<!-- Updated: Validation Session 1 - vi baked into HTML -->

## Architecture
Tĩnh `couple/guide/index.html`; cùng stack phase 2. Khóa `coupleGuide.*` chỉ có bản en trong `couple-en.js`. Scroll-margin cho header cố định.

## Related Code Files
- Create: `couple/guide/index.html`
- Modify: `js/couple-en.js` (thêm khóa guide en); dùng lại `js/page-i18n.js` từ phase 2

## Implementation Steps
1. Dựng khung + mục lục (`scroll-margin-top`, `scroll-behavior: smooth`).
2. Viết 10 mục theo fact sheet; hoàn ứng chia 3 bước (gửi → chuyển QR → xác nhận) và nêu trường hợp từ chối/hủy.
3. Meta + canonical + hreflang; JSON-LD HowTo cho luồng hoàn ứng + BreadcrumbList.
3b. hreflang vi/x-default, `og:locale` vi_VN.
4. Link ngược về `/couple/`, nút tải app cuối trang.

## Success Criteria
- [ ] Mọi anchor cuộn đúng khi mở thẳng URL có `#...`
- [ ] Mục lục highlight mục đang xem (nếu làm được bằng JS nhỏ)
- [ ] vi/en đủ, JSON-LD hợp lệ

## Risk Assessment
- App đổi luồng sau này: ghi fact sheet làm nguồn, cập nhật cùng changelog app.
