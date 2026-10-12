# Fact sheet: Sổ nợ / Công nợ (Debts) — Moni

Đường dẫn gốc: /Users/rotationba/Luan/money-mate. Ngày xác minh: 2026-10-12. Chỉ đọc code, không chạy app.
Tên hiển thị trong app là "Công nợ" (vi.json `debts.title`, src/i18n/locales/vi.json:1719+), KHÔNG phải "Sổ nợ".

## KẾT LUẬN NHANH
Tính năng có code (màn hình + API), nhưng hiện KHÔNG có lối vào nào cho người dùng bình thường: mục Khám Phá bị comment (`// TODO: unhide when ready`). Chưa nên quảng cáo là tính năng đã phát hành. Nếu vẫn viết, chỉ ghi "sắp ra mắt" và chỉ dùng mục "Có thật" bên dưới.

## 1. Có thật (đã xác minh)
Màn hình
- 3 màn: danh sách `app/debts/index.tsx`, tạo `app/debts/create.tsx`, chi tiết `app/debts/[id].tsx`; đăng ký route tại app/_layout.tsx:457-465.
- Cần đăng nhập: danh sách bọc `AuthGuard` (app/debts/index.tsx:94, :167); khách (guest) không tải dữ liệu (index.tsx:80).

Tạo khoản nợ (app/debts/create.tsx)
- Trường bắt buộc: Mô tả (create.tsx:34-37, nhãn "Mô tả *" :84), Số tiền (:38-41, nhãn "Số tiền (VND) *" vi.json `debts.amount`), Tên người nợ (:42-45, nhãn "Tên người nợ *", placeholder "Ai đang nợ bạn?").
- Trường tùy chọn: Hạn thanh toán (:111-118, ô nhập chữ placeholder `YYYY-MM-DD`, không có date picker), Ghi chú (:120-129).
- Chỉ một hướng trong UI tạo: "người khác nợ bạn" (người tạo luôn là chủ nợ: api/src/routes/debts.ts:108; placeholder "Ai đang nợ bạn?"). Đối tượng là tên tự nhập (chuỗi `debtor_name`), có thể là người hoặc cửa hàng vì chỉ là text; không có phân loại tổ chức/cá nhân (schema api/src/db/schema/debts.ts:21-27).
- Giới hạn server: mô tả tối đa 500 ký tự, ghi chú 1000, tên 200, số tiền số nguyên dương (api/src/schemas/debts.ts:10-23).

Danh sách (index.tsx)
- Bộ lọc 3 nút: "Tất cả" / "Tôi cho vay" / "Tôi nợ" (index.tsx:113-134; vi.json `debts.role_*`).
- Mỗi dòng: mô tả, số còn lại (amount - paid_amount, :27, :47), tên người nợ, nhãn trạng thái (:61).
- Kéo để làm mới (:146-148). Trạng thái rỗng: "Không có công nợ nào" (`debts.empty`).
- Trạng thái (vi.json): Chờ thanh toán / Thanh toán một phần / Đã thanh toán / Đã hủy (schema api/src/schemas/debts.ts:3-8).

Chi tiết (`[id].tsx`)
- Hiển thị Còn lại, Tổng, Đã trả, Hạn thanh toán, nhãn trạng thái, Lịch sử thanh toán (ngày + số tiền), Bình luận (:154-195, :231-316).
- Nút chỉ hiện cho chủ nợ và khi khoản chưa đóng (:199): "Đánh dấu đã trả" (xác nhận đủ, :68-79), "Hủy công nợ" (:81-93, "Không thể hoàn tác"), "Xóa" (:95-107, "Xóa vĩnh viễn").
- Đánh dấu đã trả: server tự ghi một khoản thanh toán bằng số còn lại, note "Marked paid (full settlement)", đặt paid_amount = amount (api/src/routes/debts.ts:144-165).
- Hủy chỉ cho khoản pending/partial (routes/debts.ts:172-174).
- Xóa xóa luôn lịch sử thanh toán và bình luận (FK cascade: schema debts.ts:52-54, :72-74; route :185-192).
- Bình luận: gửi được trên màn chi tiết (:109-119); server: người nợ (nếu có tài khoản) gõ "đã chuyển / đã trả / paid / transferred" thì tạo hàng đợi thông báo `debt_paid_request` cho chủ nợ (routes/debts.ts:264-280).

Dữ liệu / đồng bộ / quyền
- Dữ liệu nằm trên server (API Hono `/api/debts`, routes/debts.ts; api/src/index.ts:100), app gọi qua src/lib/api/debts.ts và store src/stores/debt-store.ts. Không có bản lưu cục bộ SQLite cho nợ (store chỉ giữ state tạm trong RAM: debt-store.ts:20-23).
- RLS: nợ cá nhân (group_id NULL) chỉ chủ nợ hoặc người nợ (có tài khoản) đọc được; nợ nhóm thì mọi thành viên nhóm đọc (api/src/db/sql/policies/debts.sql:7-11). Ghi/sửa/xóa chỉ chủ nợ (:13-23; routes dùng `loadDebtForCreditorAction`, api/src/lib/debt-access.ts:40-49).
- Đơn vị: nhãn "Số tiền (VND)" (vi.json `debts.amount`); số nguyên (bigint, schema debts.ts:31). Không có chọn đa tiền tệ trong màn tạo.

## 2. KHÔNG có (không được nói)
- Lãi suất / lịch trả / tính lãi: không có cột, không có logic (schema debts.ts:17-39; grep `interest` trong màn hình/route nợ: không có).
- Chiều "Tôi nợ người khác" tạo từ UI: không có; màn tạo cố định chủ nợ = người dùng (create.tsx:102-109, routes/debts.ts:108). Bộ lọc "Tôi nợ" chỉ có ý nghĩa nếu ai đó khác tạo nợ ghi tên bạn, mà UI không cho chọn người nợ có tài khoản (create.tsx chỉ gửi `debtor_name`, :52) nên `debtor_user_id` không bao giờ được UI đặt.
- Ghi nhận trả một phần trong app: KHÔNG có nút/ô nhập. `addPayment` (src/lib/api/debts.ts:104-114) không được màn hình nào gọi (grep toàn src/app: chỉ định nghĩa). Màn chi tiết chỉ có "Đánh dấu đã trả" (trả đủ). Trạng thái "Thanh toán một phần" chỉ xảy ra qua API trực tiếp.
- Sửa khoản nợ trong UI: không có (updateDebt có ở src/lib/api/debts.ts:73-82 nhưng không được gọi; chi tiết không có nút Sửa).
- Gắn nợ vào nhóm khi tạo: UI không có chọn nhóm (create.tsx không gửi `group_id`); API có hỗ trợ (schemas/debts.ts:14, routes/debts.ts:104).
- Trạng thái "quá hạn" (overdue): không có trạng thái/nhãn/màu quá hạn trong app; danh sách không tính quá hạn. Hạn chỉ hiển thị chữ ở chi tiết (:173-182).
- Tổng "bạn nợ / nợ bạn", gom theo người: không có màn tổng hợp hay nhóm theo người cho module này (index.tsx chỉ là danh sách phẳng). Lưu ý: thẻ nhóm `getDebtSummary` (src/lib/api/groups.ts:124-135) và `pendingGroupDebts` ở use-context-cards.ts:34-36 là số dư chia tiền nhóm, KHÔNG phải module Công nợ.
- Liên kết giao dịch/số dư: trả nợ KHÔNG tạo khoản chi/thu và không đổi số dư ví (routes/debts.ts đầu file ghi "Standalone: not linked to settlements"; chỉ chèn debt_payments, không đụng bảng giao dịch).
- Chia sẻ/xuất file, đính kèm ảnh, chọn từ danh bạ: không có (grep trong 3 màn hình: không có).
- Thông báo nhắc cho người dùng nhận được: xem mục 3, không đáng tin.
- Nhắc hạn bằng push cục bộ do người dùng bật trong cài đặt: không có công tắc nào cho nợ.

## 3. Cần xác minh / nghi lỗi (đã đọc cả hai phía)
1. LỖI HIỂN THỊ SỐ TIỀN (rất nghi ngờ): màn hình dùng `formatCurrency(remaining)` (index.tsx:47, [id].tsx:163/167/170) nhưng hàm này chia cho 100 (src/lib/utils/currency.ts:17-23, tham số tên `amountInCents`). Màn tạo lưu số nguyên VND thô (CurrencyInput trả `parseInt`, currency-input.tsx:84; create.tsx:51 không nhân 100). Suy ra nhập 500.000 sẽ hiện ~5.000 ₫. Chưa chạy app để xác nhận; đừng chụp màn hình số tiền từ module này.
2. JOB NHẮC HẠN CÓ THỂ KHÔNG BAO GIỜ GỬI ĐƯỢC: api/src/jobs/handlers/debt-reminder.ts:34-38 truy vấn cột `total_amount` và `status = 'active'`, nhưng bảng thật có cột `amount` và status là pending|partial|paid|cancelled (schema debts.ts:31, :35; migration api/drizzle/0008_fast_unicorn.sql:19-31). Truy vấn sẽ lỗi cột không tồn tại hoặc không khớp dòng nào. Cron có đăng ký 08:00 hằng ngày (scheduler.ts:65), lịch gửi `daily_9am` (handler :76). Thiết kế dự kiến: chỉ gửi cho NGƯỜI NỢ có tài khoản (`debtor_user_id IS NOT NULL`, :39), mốc: còn 1 ngày, đúng hạn, quá hạn 3 ngày (:41). Vì UI không đặt `debtor_user_id` và chủ nợ không được nhắc, thực tế không ai nhận. KHÔNG quảng cáo "nhắc hạn nợ".
3. Bấm thông báo nợ không mở được màn Công nợ: handler gửi `data.route = 'debts'` (debt-reminder.ts:75) nhưng notification-navigation.ts:20-68 không có case 'debts' và routeFromType (:74-101) không có type nợ.
4. Lối vào ẩn: mục Khám Phá "Công nợ" (`explore.debts`) đang comment (src/lib/hooks/use-explore-sections.ts:19-30, ghi "TODO: unhide when ready"). Lối còn lại là thẻ "Liên quan" trong chi tiết nhóm: `GroupRelatedItemsCard` (app/groups/[id].tsx:195) hiện mục "Công nợ" + nút mũi tên mở `/debts` (group-related-items-card.tsx:58-80) chỉ khi nhóm có khoản nợ gắn group_id (:48; API `related-summary` lấy tối đa 3, api/src/routes/groups.ts:318-345). Vì UI không thể tạo nợ gắn nhóm, thẻ này thực tế không hiện. Không tìm thấy lối vào khác (grep `/debts` trong src/app).
5. Bình luận hiển thị 8 ký tự đầu của user id thay vì tên ([id].tsx:287); danh sách người nợ không tên hiển thị 8 ký tự id (index.tsx:52).
6. Nhập hạn thanh toán là text tự do; sai định dạng sẽ bị server từ chối (regex YYYY-MM-DD, schemas/debts.ts:17-21) và UI chỉ báo "Không thể tạo công nợ" (create.tsx:57-59).
7. `/api/debts/:id` chi tiết chỉ lấy 10 thanh toán, nhưng màn hình dùng endpoint riêng /payments lấy đủ (routes/debts.ts:79-96, :235-246): không ảnh hưởng.
8. Chưa kiểm tra: bản build production có đã chứa các màn này không (có thể khác nhánh/OTA); lịch sử git: màn tạo ở commit ed6ebcd, chưa thấy commit bật lại lối vào.

## Câu hỏi chưa giải quyết
- Chủ app có định bật lối vào Khám Phá và sửa 3 vấn đề (tiền /100, job nhắc, thêm UI trả một phần) trước khi landing page nhắc đến không?
- Landing nên dùng tên "Công nợ" (đúng app) hay "Sổ nợ"?
- Có muốn tôi chạy app (simulator) xác nhận lỗi hiển thị số tiền (mục 3.1) không?
