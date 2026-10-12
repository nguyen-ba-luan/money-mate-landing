---
phase: 1
title: Content and assets
status: completed
priority: P1
effort: S
dependencies: []
---

# Phase 1: Content and assets

## Overview
Chốt nội dung đúng theo app và nhận ảnh. Mọi chữ viết ở phase 2-3 lấy từ đây để khỏi sai lệch.

## Requirements
- Functional: bảng sự thật (fact sheet) đối chiếu code; bộ chuỗi vi+en; 8 ảnh.
- Non-functional: vi có dấu đầy đủ; ảnh nén webp, mỗi ảnh ≤ 150KB, có width/height.

## Related Code Files
- Read (app repo): `app/couple/index.tsx`, `create.tsx`, `join.tsx`, `settings.tsx`, `stats.tsx`, `transactions.tsx`, `requests/*`, `src/i18n/locales/vi.json` mục `couple`, `api/src/routes` phần couple/payment-requests.
- Create: `images/couple/*.webp`, `plans/261012-1500-couple-finance-pages/reports/couple-fact-sheet.md`.

## Implementation Steps
1. Đọc code app, lập fact sheet: mỗi người được mấy cặp (commit 49c4526: một cặp active/người), ngắt kết nối thì dữ liệu chung chỉ xem được, 2 chế độ riêng tư, mốc ngày lương 1-28, luồng hoàn ứng (pending → paid → confirmed/declined/cancelled), VietQR cần đối phương khai ngân hàng, app điền sẵn, thanh toán gộp. Người kia có cần cài app không: xác minh.
2. Gửi user danh sách 8 ảnh (iPhone, dữ liệu mẫu, che tên/STK thật): dashboard; mời đối tác QR+mã; cài đặt tỷ lệ + riêng tư; thiết lập quỹ tháng; chọn nhiều giao dịch hoàn ứng; VietQR + chọn app; chi tiết yêu cầu timeline; thống kê tháng.
3. Chuyển ảnh sang webp vào `images/couple/`, đặt tên kebab-case có ý nghĩa.
4. Soạn chuỗi vi+en cho cả hai trang (khóa `couple.*`, `coupleGuide.*`).

## Success Criteria
- [ ] Fact sheet có nguồn file:dòng cho từng khẳng định
- [ ] 8 ảnh webp trong `images/couple/`
- [ ] Bộ chuỗi vi+en đủ cho 2 trang

## Risk Assessment
- Ảnh trễ: phase 2-3 dùng ô trống có kích thước cố định, thay sau, không đổi bố cục.
- Khẳng định sai về app: mọi câu FAQ phải có nguồn trong fact sheet.
