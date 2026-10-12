# Brainstorm: Trang giới thiệu + hướng dẫn Tài Chính Cặp Đôi

Date: 2026-10-12 | Repo: money-mate-landing (static HTML, Tailwind compiled, i18n vi/en) | Status: design approved

## Problem
Landing chỉ có 1 thẻ 2 dòng cho Couple. Không có nơi giới thiệu sâu, hướng dẫn dùng, hay đón người được mời. Điểm khác biệt (hoàn ứng VietQR) không được kể.

## Decisions (user)
- Cấu trúc: 3 trang (giới thiệu, hướng dẫn, đón mời). Làm giới thiệu trước.
- Ngôn ngữ: vi + en (i18n runtime như trang chủ, mặc định vi).
- Ảnh: user chụp màn hình thật.
- Mục tiêu: SEO từ Google + link đích từ app + trang cho người được mời.

## Pages
1. `/couple/` (index, vào sitemap): hero, vấn đề, 6 khối tính năng (ví chung/riêng, chia tỷ lệ, quỹ gia đình theo ngày lương, riêng tư 2 chế độ, thống kê + quỹ tiết kiệm, hoàn ứng VietQR nổi nhất), 3 bước, FAQ + JSON-LD, CTA.
2. `/couple/guide/`: anchor mỗi bước: `#ket-noi #tham-gia #thiet-lap-quy #chi-tieu-chung #quyet-toan #hoan-ung #thanh-toan-gop #quyen-rieng-tu #ngat-ket-noi #cau-hoi-thuong-gap`. TOC dính trái (desktop), chip (mobile).
3. `/couple/invite/` (noindex): người được mời hiểu app làm gì, nút tải, cách nhập mã. `/invite/` hiện chỉ cho nhóm.

## Source of truth (app)
`app/couple/*`, `src/i18n/locales/vi.json` mục `couple` (headline "Cùng nhau, tiền bạc rõ ràng hơn", reimbursement.*, privacy modes sharedSummary/fullTransparent, salaryDay).

## Screenshots needed (8)
Dashboard; mời đối tác QR+mã; cài đặt tỷ lệ + riêng tư; thiết lập quỹ tháng; chọn nhiều giao dịch hoàn ứng; VietQR + chọn app ngân hàng; chi tiết yêu cầu timeline; thống kê tháng.

## Constraints / risks
- Tailwind compiled: chỉ class có sẵn (cyan/fuchsia không có); thêm class mới cần build.
- Ảnh là rủi ro chính; thiếu ảnh thì guide chỉ còn chữ.
- Phải đối chiếu code app cho riêng tư / ngắt kết nối / số người trong một cặp trước khi viết FAQ.
- Trang 3: kiểm tra link mời cặp đôi app đang share (`shareMessage` có `{{link}}`) trước khi làm.
- Sinh lại `/vi/` nếu sửa trang chủ (thẻ cặp đôi trỏ sang `/couple/`).
- Cập nhật sitemap, footer, thẻ cặp đôi trang chủ, deep link từ app (cần sửa app repo, tách riêng).

## Unresolved
- Link mời cặp đôi hiện trỏ đâu? (cần xác minh trước trang 3)
- App mở link guide từ đâu (nút "?" ở màn couple)? Phạm vi sửa app repo chưa chốt.
- Trang `/vi/` tĩnh: có cần bản `/vi/couple/` hay chỉ dùng i18n runtime?
