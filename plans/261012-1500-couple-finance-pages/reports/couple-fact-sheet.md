# Couple feature fact sheet (nguồn: repo money-mate, đọc code 2026-10-12)

## Được phép quảng cáo
- Mời: tên cặp ≤40 ký tự (app/couple/create.tsx:102); mã 20 hex, dùng 1 lần, hết hạn 7 ngày (api/src/routes/group-invitations.ts:68,210-223; src/lib/api/group-invitations.ts:47). Người được mời PHẢI có tài khoản + đăng nhập (group-invitations.ts:203; app/invite/[code].tsx:73-99).
- Mỗi người 1 cặp active (api/src/lib/group-membership.ts:55-78). Server KHÔNG giới hạn số thành viên (group-invitations.ts:163) -> không viết "chỉ 2 người".
- Ví: công tắc Cá nhân/Chung khi thêm giao dịch, mặc định Cá nhân (add-transaction-form.tsx:85-90,214-218). Đối tác chỉ thấy ví chung; chỉ người tạo giao dịch sửa được (sync-tables.sql:12-24).
- Quỹ: quỹ = thu nhập − chi cá nhân A − chi cá nhân B − tiết kiệm (use-couple.ts:13-18); còn lại = max(quỹ − đã chi, 0). Ngày lương 1–28 (fiscal-period.ts). Tháng sau lấy sẵn số tháng trước để sửa; số dư KHÔNG cộng dồn. Cả hai sửa được thiết lập (couples.ts:223).
- Dự kiến còn lại trừ khoản lặp lại chưa đến; khoản biến động ("điện, nước") nhập số khi đến hạn (couple-fund-hero.tsx:35; recurring/add.tsx:453).
- Thống kê: 4 thẻ, biểu đồ 12 tháng, so trung bình, theo danh mục/theo người, quỹ tiết kiệm, chuyển số dư vào quỹ (stats.tsx; couple-leftover-transfer-sheet.tsx).
- Hoàn ứng: pending→paid (payee), →confirmed (requester), →declined (payee, lý do ≤500), →cancelled (requester, khi pending). Tối đa 50 giao dịch/yêu cầu; chỉ khoản chi ví chung do requester tạo, chưa nằm trong yêu cầu khác. Push: tạo, paid, confirmed, declined (không push khi hủy). payment-requests.ts.
- VietQR: cần requester khai ngân hàng + STK; nội dung mặc định "MONI HOAN <8 ký tự>"; app ngân hàng: chỉ một số app "autofill", còn lại chỉ mở (viet-qr-bank-apps.ts). Danh sách thật lấy từ api.vietqr.io.
- Gộp thanh toán: ≥2 yêu cầu pending mình là payee; 1 QR tổng; mỗi yêu cầu vẫn cần xác nhận riêng (pay-together.tsx).
- Ngắt kết nối: CHỈ người tạo (admin) thực hiện được (groups.ts:202); nút hiện với cả hai; dữ liệu không bị xóa; kết nối lại được (cặp ended không tính giới hạn).
- Tiền tệ: chỉ VND (settings-store.ts:58-61). Không có paywall trong code couple.

## KHÔNG quảng cáo (app có chuỗi nhưng không có tính năng)
- "Tỷ lệ thu nhập/chia công bằng": incomeSplitRatio legacy-unused (src/types/index.ts:463), không có màn chỉnh.
- "Chế độ riêng tư 2 mức": privacyMode legacy-unused (types:464); không có công tắc. Quyền xem do RLS.
- "Quyết toán / tự động tính ai nợ ai": CoupleSettlementCard không được render ở đâu.
-> Gợi ý sửa app: bỏ/đổi chuỗi couple.feat_fairSplit_desc, feat_privacyControl trong màn giới thiệu (couple-setup-prompt.tsx:75).

## Gắn nút Hướng dẫn (phase 6)
- ScreenHeader có `rightElement` (screen-header.tsx:8-12). app/couple/index.tsx:223 (chưa liên kết, chưa dùng rightElement); :265-293 (đã liên kết, đã có 2 nút trong View headerActions); app/couple/requests/index.tsx:155 (chưa có).
