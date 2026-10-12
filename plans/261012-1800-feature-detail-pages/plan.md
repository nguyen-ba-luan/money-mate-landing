---
title: Trang chi tiết cho các tính năng còn lại
status: in-progress  # 3/4 trang xong local, chờ user duyệt rồi mới commit
created: 2026-10-12
---

# Trang chi tiết các tính năng (sau Tài Chính Cặp Đôi)

Mẫu: `couple/` + `couple/guide/` (vi baked, en qua `js/page-i18n.js` + `js/<slug>-en.js`, css prefix riêng). Làm từng tính năng một, duyệt xong mới sang tính năng sau.

| # | Tính năng | URL | Trạng thái |
|---|-----------|-----|-----------|
| 1 | Ngân sách + công thức | `/budget/`, `/budget/guide/` | XONG local, chưa commit (trang, OG, nối trang chủ/footer/sitemap, nút "?" trong app) |
| 2 | Nhóm + chia tiền (+ khách) | `/groups/`, `/groups/guide/` | XONG local, chưa commit (21 ảnh, OG, wire showcase `solution.f2`, nút "?" ở members/[id]/trip-summary) |
| 3 | Tiết kiệm cá nhân | `/savings/`, `/savings/guide/` | XONG local, chưa commit. Quỹ tiết kiệm nhóm KHÔNG làm: lối vào Khám Phá đang ẩn (TODO), định kỳ/mục tiêu thành viên chỉ có API; phần cặp đôi đã nằm trong /couple/guide/#thong-ke |
| 4 | Sổ nợ | `/debts/`, `/debts/guide/` | BỎ: tính năng chưa phát hành (mục Khám Phá bị ẩn, nhắc hạn không chạy, UI thiếu trả một phần/sửa, nghi lỗi hiển thị tiền). Xem reports/debts-fact-sheet.md |

Mỗi tính năng: fact sheet đối chiếu code → seed API/DB local + chụp simulator (xem memory `reference_local_api_simulator_screenshots`) → 2 trang vi/en → sitemap, footer, thẻ trang chủ clickable, OG riêng → nút "?" trong app (+ 10 locale nếu thêm chuỗi) → test Chrome desktop/mobile.

Ràng buộc: không quảng cáo tính năng không có trong code; không dùng dữ liệu production; không commit/push/OTA khi chưa có lệnh.

## Công cụ (tools/)
- `gen_feature_pages.py <slug>` + `features/<slug>.py` (spec song ngữ) sinh `<slug>/index.html`, `<slug>/guide/index.html`, `js/<slug>-en.js`. Sửa spec rồi chạy lại, đừng sửa HTML tay.
- `make_og.py` render `images/og-image-<slug>.jpg` bằng Chrome headless.
- `wire_site.py` nối thẻ trang chủ (index + vi), footer, `js/i18n.js`, sitemap (idempotent).
- App: `GuideLinkButton` (src/components/ui) + `<Feature>GuideButton`; khóa `common.guide` đã có đủ 10 locale.
Server local: DB `money_mate_screens`, API :3100, Metro :8081 với `.env.development.local` (xóa khi xong), http.server :8765.
