---
phase: 4
title: Wire up site and SEO
status: completed
priority: P2
effort: S
dependencies:
  - 2
  - 3
---

# Phase 4: Wire up site and SEO

## Overview
Nối hai trang mới vào phần còn lại của site.

## Related Code Files
- Modify: `index.html` (thẻ "Tài chính cặp đôi" bấm được → `/couple/`; footer; JSON-LD featureList nếu cần), `js/i18n.js` (nhãn link), `sitemap.xml`, `invite/index.html` (khối "Moni là gì" + link `/couple/`, `/couple/guide/#tham-gia`), `vi/index.html` (sinh lại từ root bằng script như đợt trước).

## Implementation Steps
1. Thẻ cặp đôi trang chủ: thêm link "Xem chi tiết" (vi/en).
2. Footer: thêm "Tài chính cặp đôi" và "Hướng dẫn cặp đôi".
3. `sitemap.xml`: thêm 2 URL, `lastmod` hôm nay.
4. `/invite/`: thêm khối ngắn giải thích app + link; giữ `noindex`, không đổi logic mã mời.
5. Sinh lại `vi/index.html` (bake chuỗi vi) vì thẻ cặp đôi trang chủ đổi; kiểm tra không lệch. KHÔNG tạo `/vi/couple/`.
6. Nút trong app: xem phase 6.

## Success Criteria
- [ ] Mọi link mới bấm đúng từ trang chủ, footer, invite
- [ ] sitemap hợp lệ XML
- [ ] `/vi/` khớp root

## Risk Assessment
- Sửa `invite/index.html` có thể ảnh hưởng luồng mời nhóm: chỉ thêm khối tĩnh, test với `?code=` mẫu cả hai trạng thái có/không có mã.
