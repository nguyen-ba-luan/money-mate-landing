# Fact sheet: Nhóm chi tiêu / chia tiền (Moni)

Nguồn: repo `/Users/rotationba/Luan/money-mate` (đường dẫn cite tính từ gốc repo). Đọc code 2026-10-12, KHÔNG chạy app. "Có thật" = đã đọc code gọi tới. Mọi cặp `file:dòng` đã mở thực tế.
Viết tắt: API = `api/src/routes`, FE-API = `src/lib/api`, STORE = `src/stores/group-store.ts`.

---
## 1. CÓ THẬT (được nói)

### 1.1 Hai loại: Nhóm chi tiêu chung vs Chuyến đi (+ couple, bỏ qua)
- DB: `groups.type` = 'group'|'trip'|'couple', `status` = 'active'|'ended' (`api/src/db/schema/groups.ts:33-34`). Field trip: destination, start_date, end_date, default_currency (mặc định VND), budget (`groups.ts:35-39`).
- Bottom sheet tạo mới: "Nhóm chi tiêu chung" (mô tả "Tiền nhà, ăn uống hàng ngày...") và "Chuyến đi" (mô tả "Du lịch, team building, picnic...") (`src/components/groups/create-type-bottom-sheet.tsx:46-90`; vi `trip.groupOption/Desc`, `trip.tripOption/Desc`).
- Màn nhóm không hiện couple; couple có màn riêng (`STORE:57-65`).
- Chuyến đi có thêm: Tên chuyến đi, Điểm đến, Ngày bắt đầu/kết thúc (date range picker), Ngân sách (tuỳ chọn) (`app/groups/create.tsx:136-195`). Nhóm thường chỉ có tên + mô tả (tuỳ chọn) (`create.tsx:86-134`).
- Chuyến đi có 3 tab: "Dòng thời gian", "Số dư", "Thành viên" (`app/groups/[id].tsx:201-267`; vi `trip.tabTimeline/Balances/Members`), thanh tiến độ ngân sách "Đã chi: X / ngân sách" + % + đỏ khi vượt, badge "Đang diễn ra"/"Đã kết thúc" (`src/components/groups/trip-header.tsx:92-139`). Nhóm thường: không tab, hiện số dư + danh sách chi tiêu (`[id].tsx:268-304`).
- Ngân sách: chỉ người tạo nhóm sửa được (bấm vào thanh ngân sách) (`[id].tsx:193-199`, `trip-header.tsx:109-114`).
- Danh sách nhóm có bộ lọc "Tất cả / Nhóm / Chuyến đi" (`app/(tabs)/groups.tsx:72-76`; vi `trip.filterAll/Group/Trip`).

### 1.2 Tạo nhóm
- Bắt buộc: chỉ tên (`create.tsx:38-43`; server tên 1-200 ký tự `api/src/schemas/groups.ts:14-15`). Còn lại tuỳ chọn.
- Người tạo tự thành thành viên role `admin` (`API/groups.ts:171-188`) và là `created_by`.
- Yêu cầu đăng nhập (khách chưa login thấy "Đăng nhập để tạo nhóm và chia sẻ chi tiêu với bạn bè") (`app/(tabs)/groups.tsx:81`, `app/groups/index.tsx:19,31`; vi `groups.signInToJoin`).

### 1.3 Mời / thêm thành viên
- Link mời: `https://moni.live/invite/?code=<mã>` (`FE-API/group-invitations.ts:64`), chia sẻ qua share sheet hệ thống với câu: `Tham gia nhóm "{tên}" của tôi trên Moni: {link}` (`app/groups/members.tsx:72-92`; vi `groups.inviteShareMessage`). Nút: "Chia sẻ liên kết mời".
- Mã mời: 20 ký tự hex ngẫu nhiên (`API/group-invitations.ts:66-68`); hạn mặc định 7 ngày, server cho 1-30 ngày (`api/src/schemas/groups.ts:38-41`), app luôn gửi 7 (`group-invitations.ts:47`). DÙNG MỘT LẦN: nhận xong status = 'accepted', mã không dùng lại được (`API/group-invitations.ts:210-236`). Lỗi: "Lời mời đã hết hạn"/"đã được sử dụng".
- Nhập mã thủ công: nút "Nhập mã mời" ở đầu danh sách nhóm -> modal "Dán mã mời tại đây" -> "Tham gia" (`app/(tabs)/groups.tsx:90-99`, `src/components/groups/join-by-code-modal.tsx:43-59`).
- Mở link: màn `app/invite/[code].tsx` – hiện tên nhóm, nút "Tham gia nhóm"; chưa đăng nhập thì bắt đăng nhập rồi quay lại (`invite/[code].tsx:33,52-97`). => Người được mời PHẢI có tài khoản Moni (và cài app); trang web `moni.live/invite` là landing dẫn tải app (landing repo `invite/index.html`).
- Thêm bằng email: admin gõ email -> chỉ thêm được người ĐÃ đăng ký; chưa có tài khoản báo "Người dùng với email này chưa đăng ký. Vui lòng dùng liên kết mời." (`FE-API/group-members.ts:47-64`; server lookup `api/src/routes/users-lookup.ts:25-35`, rate limit 10/phút).
- Ai mời được: chỉ admin (nút chia sẻ link + ô email chỉ hiện cho admin `members.tsx:171-208,271-295`; server `requireAdmin` ở POST invitations `group-invitations.ts:64`, POST members `group-members.ts:68`).
- Danh sách "Lời mời đang chờ": admin xem mã, email (nếu có), hạn, nút "Thu hồi" (`members.tsx:212-269`; server `GET invitations` admin-only `API/group-invitations.ts:42-52`). Lưu ý: danh sách trả về cả lời mời đã dùng (không lọc status) (`group-invitations.ts:46-50`) – chưa kiểm xem UI có lọc không (`members.tsx:214` chỉ lọc `length>0`).
- Số thành viên tối đa: KHÔNG giới hạn (`API/group-invitations.ts:163` "no max-member limit currently").

### 1.4 Thêm chi tiêu (`app/groups/add-expense.tsx`)
- Trường có thật: Số tiền (`:466`), Chi tiêu/Thu nhập (toggle "Chi tiêu"/"Thu nhập", `:473-509`), Tiêu đề (bắt buộc, `:298`, ô nhập `:510`), Ngày (không cho chọn tương lai `:568`, ô `:534`), Người trả (chọn 1 trong mọi thành viên kể cả khách, `:588-627`), Chia sẻ (loại chia, `:657`), Hóa đơn (đính kèm ảnh, `:711-724`).
- Danh mục: CHỈ trong chuyến đi – 6 loại: Ăn uống, Chỗ ở, Di chuyển, Vé, Mua sắm, Khác (`add-expense.tsx:576-586`, `src/lib/constants/trip-categories.ts:12-33`). Nhóm thường: không chọn danh mục (lưu 'other').
- Ghi chú (notes): server & type có, nhưng KHÔNG có ô nhập trong form (biến `notes` chỉ đọc lại khi sửa, `add-expense.tsx:116,172,346`). Không quảng cáo "ghi chú cho khoản chi nhóm".
- 3 kiểu chia: "Đều nhau" / "Chính xác" / "%" (`src/components/groups/split-type-selector.tsx`; vi `groups.splitEqual/Exact/Percentage`).
  - Đều: chia nguyên, phần dư rải 1 đơn vị nhỏ nhất cho người đầu (`FE-API/shared-expenses.ts:78-85`).
  - Chính xác: tổng phải bằng tổng chi, lỗi "Tổng số tiền chia phải bằng tổng chi tiêu" (`add-expense.tsx:304-307`).
  - %: tổng phải bằng 100%, lỗi "Tổng phần trăm phải bằng 100%" (`:300-303`); chênh làm tròn cộng vào người có phần lớn nhất (`shared-expenses.ts:88-102`). Còn hiện "Còn lại ..." theo thời gian thực (`add-expense.tsx:699-707`).
  - Server kiểm lại tổng splits = tổng tiền, sai trả 400 (`API/shared-expenses.ts:208-213`).
- "Chia cho" một số người (bỏ chọn bớt thành viên): CHỈ chuyến đi ("Chia cho", chip thành viên, "n/tổng thành viên") (`add-expense.tsx:628-655`, `src/components/groups/member-toggle-list.tsx`). Nhóm thường: chia cho TẤT CẢ thành viên (`add-expense.tsx:220-222`).
- Mẫu chia ("Mẫu chia"): lưu / áp dụng / xoá, theo từng nhóm, chỉ cho kiểu Chính xác và %, ví dụ "Cặp đôi 60/40" (`src/components/groups/split-preset-picker.tsx:67-127`; server `API/split-presets.ts:28-97`; schema chỉ 'exact'|'percentage' `schemas/groups.ts:92-96`). Mọi thành viên đều xem/xoá được mẫu của nhóm (`split-presets.ts:86-97`).
- Hóa đơn: đính kèm ảnh từ app, nén rồi upload; server nhận JPEG/PNG ≤ 1 MB, lưu R2 (`API/shared-expenses.ts:35-64`, `FE-API/shared-expenses.ts:134-146`). Xem lại ở chi tiết chi tiêu "Xem hóa đơn" (`app/groups/expense-detail.tsx:310-335`).
- Nhập nhanh: nút Máy ảnh (quét hóa đơn), Thư viện ảnh, Micro (giọng nói; chỉ hiện khi thiết bị hỗ trợ) điền sẵn tiêu đề/số tiền, giọng nói còn gợi ý danh mục trip (`add-expense.tsx:241-285,745-775`). Quét hóa đơn đi qua backend proxy (commit e24fa3e).
- Thu nhập ("Thu nhập") trong nhóm: người trả chia tiền cho các thành viên (số dư tính ngược) (`FE-API/balance-service.ts:40-51`).
- Sửa chi tiêu: mở chi tiết -> Sửa (cùng form) (`expense-detail.tsx:83-87`, `add-expense.tsx:337-353`).
- Quyền sửa/xoá (UI): chỉ NGƯỜI TRẢ (hoặc chi tiêu do khách trả) và chuyến đi chưa kết thúc (`expense-detail.tsx:63-68`; xoá bằng nhấn giữ: `src/lib/hooks/use-group-detail-data.ts:95-104`, câu "Chỉ người trả mới có thể xóa chi tiêu này").
- Xuất dữ liệu: nút xuất CSV / PDF chi tiêu nhóm (có bảng số dư trong PDF) (`[id].tsx:308`, `use-group-detail-data.ts:163-187`).
- Hiển thị tiền: dùng tiền tệ trong Cài đặt của người xem (`use-group-detail-data.ts:32-37`).
- Mọi thành viên khác nhận push "Chi tiêu nhóm mới": "{tên} vừa thêm "{tiêu đề}" ({số tiền}đ)" (xem mục 1.8).

### 1.5 Khách (guest, người không dùng app)
- Khách = "user ma" (`is_ghost=true`) do hệ thống tạo, có tên hiển thị ≤ 50 ký tự, vào nhóm với role 'guest', tham gia chia tiền/thanh toán như thành viên (`API/group-guests.ts:44-87`, `schemas/groups.ts:82-84`, `db/schema/groups.ts:182-200`). Không cần email/số điện thoại, không đăng nhập được.
- Cách thêm trong app: nút "Thêm khách mới" trong form thêm chi tiêu của CHUYẾN ĐI (ô nhập "Tên khách", VD "Chú Bình") (`add-expense.tsx:640-654`, vi `groups.addNewGuest`, `groups.guestNamePlaceholder`). Khách mới tự được chọn vào danh sách chia. Mọi thành viên (không chỉ admin) thêm được khách (`group-guests.ts:55`).
- Nhớ khách đã chọn cho lần thêm chi tiêu sau (AsyncStorage) (`add-expense.tsx:142-158`).
- Khách có thể là người trả (chọn trong "Người trả") (`add-expense.tsx:588-627`; server cho phép payer là ghost `API/shared-expenses.ts:228-236`).
- Thanh toán thay khách ("Đã thu tiền"): trong "Thanh toán tối ưu", dòng khách nợ mình hiện nút "Đã thu tiền" -> màn "Xác nhận đã thu tiền" ("Bạn đang xác nhận thay mặt {tên}" / "Xác nhận đã nhận") -> ghi 1 settlement từ khách -> mình, có `proxy_user_id` (`balance-summary.tsx:78-82,198-203`, `settle.tsx:62-71,105-118`, `API/settlements.ts:53-68`).
- Nhãn "Khách" cạnh tên trong danh sách nợ (`balance-summary.tsx:123-139`).
- Save button hiện "(n khách)" (`add-expense.tsx:790-797`).

### 1.6 Số dư và "Thanh toán tối ưu"
- Cách tính (client, `FE-API/balance-service.ts:24-81`): số dư mỗi người = tổng đã trả − tổng phần phải chịu + khoản đã thanh toán; có tính cả chi tiêu loại Thu nhập và các khoản thanh toán đã ghi.
- Rút gọn nợ: thuật toán tham lam – ghép người nợ nhiều nhất với người được nợ nhiều nhất cho đến khi hết (`balance-service.ts:83-131`). Kết quả luôn tối đa (số người có số dư ≠ 0) − 1 giao dịch; KHÔNG đảm bảo tối thiểu toàn cục tuyệt đối trong mọi trường hợp. Tiêu đề UI: "Thanh toán tối ưu" + phụ đề "Số dư của bạn" (`balance-summary.tsx:63-70`; vi `groups.optimalPayment`, `groups.netBalance`). Dùng ở cả nhóm thường lẫn chuyến đi.
- Khi hết nợ: "Tất cả đã thanh toán! – Mọi người đều hòa — tuyệt vời!" (`balance-summary.tsx:27-46`).
- Thẻ số dư cá nhân (`src/components/groups/personal-balance-hero.tsx`): "Bạn đang nợ" (đỏ) / "Bạn sẽ nhận" (xanh) / "Bạn không nợ ai" kèm số tiền lớn, gợi ý ("Thanh toán sớm để tránh quên" / "Có thể nhắc nhẹ mọi người" / "Tuyệt vời, không ai nợ ai!"), và "n người đã thanh toán · Còn n người chưa trả" (`:84-165`). Dòng này chỉ hiện khi nhóm có hơn 1 thành viên (`:133`).
- Số dư tổng hợp mọi nhóm (không gồm couple): endpoint `GET /api/groups/debt-summary` -> {totalOwed, totalOwedToYou, groupsWithDebt} (`API/groups.ts:82-150`; FE `FE-API/groups.ts:124-135`). Chưa kiểm màn hình nào gọi (xem mục 3).

### 1.7 Các nút của thẻ số dư – THỰC SỰ làm gì (`app/groups/[id].tsx:108-124`)
| Nút (vi) | Điều kiện hiện | Hành vi thật |
|---|---|---|
| "Thanh toán ngay" (`groups.payNow`) | bạn đang nợ | Mở màn "Ghi nhận thanh toán" cho khoản nợ đầu tiên của bạn (`handlePayNow` -> `handleSettle`). KHÔNG tạo QR/VietQR, không mở app ngân hàng, không chuyển tiền. |
| "Xem cách chia" (`groups.viewSplitDetail`) | bạn đang nợ | Chỉ chuyển sang tab "Số dư" khi là CHUYẾN ĐI; ở nhóm thường không làm gì (`handleViewSplit`). |
| "Nhắc mọi người trả" (`groups.remindAll`) | bạn sẽ nhận | CHỈ chuyển sang tab "Số dư" khi là chuyến đi; ở nhóm thường không làm gì. KHÔNG gửi push/nhắc nhở nào (`handleRemindAll` :114-116, không gọi API). |
| "Xem ai đang nợ" (`groups.viewWhoOwes`) | bạn sẽ nhận | Chỉ chuyển sang tab "Thành viên" khi là chuyến đi; nhóm thường không làm gì (`handleViewWhoOwes`). |
=> Không được viết "nhắc nợ tự động / gửi nhắc cho từng người".

### 1.8 Thanh toán (settlement)
- Luồng thật: ghi nhận một khoản đã trả ("Ghi nhận thanh toán"): chọn người nhận ("Trả cho"), số tiền (điền sẵn), ghi chú tuỳ chọn (placeholder "VD: Chuyển khoản ngân hàng") -> lưu ngay vào sổ, trừ nợ (`settle.tsx:55-96,134-213`; `FE-API/settlements.ts:43-67`; `API/settlements.ts:42-83`). Có thể ghi số tiền nhỏ hơn nợ (thanh toán một phần): server chỉ yêu cầu amount ≥ 1 (`schemas/groups.ts:72-79`).
- Không có trạng thái chờ/đã duyệt cho settlement: bảng chỉ có settled_at, không có status (`db/schema/groups.ts:154-177`). Không có VietQR/mã QR/deeplink ngân hàng trong luồng nhóm (grep `qr|vietqr` trong `app/groups`, `src/components/groups` = 0 kết quả). (VietQR chỉ có ở luồng hoàn ứng cặp đôi `app/couple/requests/*`, `api/src/routes/payment-requests.ts:1-15` – ngoài phạm vi.)
- Thông báo: sau khi ghi, người còn lại nhận push "Đã nhận thanh toán": "{tên} đã thanh toán {số tiền} cho bạn" (`FE-API/settlements.ts:69-81`, `src/lib/api/group-notifications.ts:101-120`). Fire-and-forget, lỗi bị bỏ qua.
- Xoá settlement: bất kỳ thành viên nào gọi API được (`API/settlements.ts:86-97`, chưa thấy UI gọi – xem mục 3).

### 1.9 Tổng kết chuyến đi (`app/groups/trip-summary.tsx`)
- Hiển thị: tên, điểm đến, khoảng ngày + số ngày; "Tổng chi tiêu"; "Trung bình mỗi người" (tổng / số thành viên, gồm cả khách) (`:119-162`, `FE-API/trip-summary.ts:38-93`); "Theo danh mục" (thanh tỉ lệ %, 6 danh mục) (`:164-230`); "Chi nhiều nhất" (xếp hạng người TRẢ nhiều nhất, huy chương 1-3) (`:232-259`); "Cần thanh toán" (cùng bảng Thanh toán tối ưu, bấm thanh toán được) (`:261-272`).
- "Chia sẻ tổng kết": chia sẻ VĂN BẢN THUẦN qua share sheet hệ thống (có emoji; tổng, TB/người, theo danh mục, top 3 người trả) (`:28-53,74-77`). KHÔNG phải ảnh/PDF/link. Nội dung chia sẻ là chuỗi cứng tiếng Anh ("Total", "Avg/person", "By category", "Top spenders") không i18n (`:33-44`).
- Nút "Kết thúc chuyến đi" ở đây chỉ hiện cho người tạo khi chuyến còn active (`:283-300`).
- Chỉ có ở Chuyến đi (nút "Tổng kết chuyến đi" chỉ hiện khi isTrip `[id].tsx:309-329`).

### 1.10 Kết thúc chuyến đi
- Chỉ người tạo nhóm thấy "Vùng nguy hiểm" -> "Kết thúc chuyến đi?" ("Bạn sẽ không thể thêm chi tiêu mới. Số dư hiện tại vẫn có thể thanh toán.") (`[id].tsx:353-383`, `use-group-detail-data.ts:41,125-140`; vi `trip.endTripMessage`). Server: PATCH group yêu cầu admin (`API/groups.ts:202`).
- Sau khi kết thúc (UI): ẩn nút "Thêm chi tiêu" (`[id].tsx:399`), form thêm chi tiêu tự thoát với "Chuyến đi đã kết thúc. Không thể thêm chi tiêu mới." (`add-expense.tsx:213-218`), không sửa được chi tiêu (`expense-detail.tsx:68`). Vẫn thanh toán/ghi nhận được, vẫn xem tổng kết.
- Mọi thành viên khác nhận push "Chuyến đi đã kết thúc": "{tên chuyến}: n khoản nợ cần thanh toán" hoặc "Tất cả khoản nợ đã được giải quyết" (`STORE:188-216`, `group-notifications.ts:155-174`).
- Nhóm thường: KHÔNG có nút kết thúc (`[id].tsx:366` điều kiện isTrip).

### 1.11 Bảng thành viên (leaderboard) và chi tiêu theo thành viên
- Tab "Thành viên" của chuyến đi: xếp hạng theo số dư ròng (người sẽ nhận nhiều nhất lên đầu); mỗi dòng: thứ hạng, avatar, tên, "Tổng đã trả: X", nhãn "sẽ nhận" / "đang nợ" / "đã cân bằng" + số tiền (`[id].tsx:68-88,449-579`). Chỉ trong chuyến đi (nhóm thường không có tab).
- Bấm 1 người -> màn riêng: tên người đó, "Tổng đã trả", "n khoản chi tiêu", danh sách khoản họ đã trả (sắp theo ngày mới nhất) (`app/groups/member-expenses.tsx:29-83`). Chỉ gồm khoản người đó TRẢ, không gồm khoản họ chỉ phải chịu.
- Nút "Quản lý thành viên" dẫn tới màn Thành viên (`[id].tsx:243-264`).

### 1.12 Thẻ "Liên quan" của nhóm (GroupRelatedItemsCard)
- Hiện dưới thẻ số dư; ẩn hoàn toàn nếu không có gì (`group-related-items-card.tsx:48-49`). Gồm tối đa 3 "Khoản nợ" (module Nợ, link tới `/debts`, mỗi dòng còn lại = amount − paid_amount) và tối đa 3 "Quỹ tiết kiệm nhóm" (link `/group-savings/{id}`, hiện icon, tên, trạng thái) có gắn với nhóm này (`group-related-items-card.tsx:59-130`; server `API/groups.ts:316-353`, `.limit(3)`).
- Là lối tắt tới 2 tính năng khác (Nợ và Tiết kiệm nhóm), không phải một phần của chia tiền. Quỹ nhóm tạo từ `app/group-savings/create.tsx` chọn nhóm (`:82,106,164-173`). Cách gắn khoản Nợ vào nhóm chưa tìm thấy trong UI (xem mục 3).

### 1.13 Lối vào trong app (nhãn vi.json)
- Tab "groups" bị ẩn khỏi thanh tab (`app/(tabs)/_layout.tsx:103`, `href: null`) – không phải tab dưới.
- Màn Khám phá, mục "Cộng Tác" (`explore.collab`) -> dòng "Nhóm Chi Tiêu" (`explore.groups`) (`src/lib/hooks/use-explore-sections.ts:112-124`).
- Trang chủ, lưới lối tắt: ô "Nhóm chi tiêu" (`home.quickAccess.groups`) -> `/groups` (`src/components/home/quick-access-grid.tsx:40-45`).
- Onboarding: lựa chọn "Với Bạn Bè – Chia tiền chi tiêu nhóm" (`onboarding.profileGroup/Sub`; chưa đọc code onboarding).
- Tiêu đề màn: "Nhóm" / "Chuyến đi" / "Thành viên" / "Tham gia nhóm" (`headers.group/trip/groupMembers/joinGroup`).
- Link mời `moni.live/invite/?code=...` mở thẳng màn tham gia (`app/invite/[code].tsx`).

### 1.14 Quyền và rời nhóm
- Xoá nhóm: nút "Xóa nhóm" ("Thao tác này sẽ xóa vĩnh viễn nhóm và toàn bộ dữ liệu.") chỉ người tạo thấy (`[id].tsx:353-395`, `use-group-detail-data.ts:142-161`); server cần admin, xoá cascade chi tiêu/splits/thanh toán/lời mời/khách (`API/groups.ts:356-367`, FK onDelete cascade `db/schema/groups.ts`).
- Rời nhóm: nút "Rời nhóm" ("Bạn có chắc muốn rời nhóm?") chỉ hiện cho thành viên KHÔNG phải admin (`members.tsx:296-306`). Admin/người tạo không rời được trong UI (phải xoá nhóm). Server chặn xoá admin cuối cùng: "Cannot remove the last admin" (`API/group-members.ts:129-148`).
- Số dư khi rời: code không chặn, không tất toán, không báo trước. Chi tiêu/thanh toán cũ của người đó vẫn nằm trong sổ (`group-members.ts:106-151` chỉ xoá dòng thành viên). Không được hứa "tự tất toán khi rời".
- Chuyển quyền admin: API có (`PATCH members/:id` `API/group-members.ts:83-104`) nhưng KHÔNG có UI (xem mục 2).

### 1.15 Đồng bộ
- Màn nhóm tải lại khi nhận sự kiện realtime của shared_expenses / settlements / group_members (`src/hooks/use-group-realtime.ts:1-30`, mục 3 về việc chưa xác minh phía server) và kéo để làm mới (`[id].tsx:132-139`).

### 1.16 Push liên quan nhóm (xác minh ở `src/lib/api/group-notifications.ts` + `api/src/routes/notifications.ts:116-189`)
Cơ chế: client gọi `/api/notifications/fanout`; server kiểm tra người gọi và người nhận đều là thành viên, lưu thông báo trong app + gửi push Expo (best-effort) (`notifications.ts:116-189`).
| Sự kiện | Ai nhận | Tiêu đề push | Có gọi từ UI? |
|---|---|---|---|
| Thêm chi tiêu | mọi thành viên trừ người thêm | "Chi tiêu nhóm mới" | CÓ (`FE-API/shared-expenses.ts:173`) |
| Ghi nhận thanh toán | bên còn lại | "Đã nhận thanh toán" | CÓ (`settlements.ts:75`) |
| Kết thúc chuyến đi | mọi thành viên trừ người kết thúc | "Chuyến đi đã kết thúc" | CÓ (`STORE:194`) |
| Sửa / xoá chi tiêu | – | – | KHÔNG có thông báo |
| Nhắc nợ | – | – | KHÔNG có |
Ghi chú: khách không có thiết bị nên không nhận push.

---
## 2. KHÔNG CÓ (không được nói)

1. Nhắc nợ / "Nhắc mọi người trả" gửi thông báo: KHÔNG. Nút chỉ chuyển tab (chỉ chuyến đi), nhóm thường bấm không có tác dụng (`[id].tsx:114-124`).
2. "Thanh toán ngay" tạo mã VietQR / mở app ngân hàng / chuyển tiền: KHÔNG. Chỉ ghi nhận thủ công (`settle.tsx`, không có qr/bank trong `app/groups`, `src/components/groups`). Moni không chuyển tiền, không giữ tiền.
3. Quy đổi đa tiền tệ cho người dùng: KHÔNG có đường vào UI. Bộ chọn tiền tệ của nhóm tồn tại (`src/components/groups/currency-picker.tsx`) nhưng không màn nào dùng (grep: chỉ test + màn Cài đặt dùng bộ khác); tiền tệ khi tạo cố định 'VND' (`create.tsx:55`); form thêm chi tiêu ghi "Currency picker removed from UI" (`add-expense.tsx:134`). DB/API có original_currency, exchange_rate nhưng người dùng không nhập được. Số tiền hiển thị theo tiền tệ trong Cài đặt của người xem (`use-group-detail-data.ts:32-37`).
4. Sửa tên/điểm đến/ngày chuyến đi sau khi tạo: KHÔNG có UI (`updateGroup` chỉ được gọi cho ngân sách: `create.tsx:62`, `trip-header.tsx:63`; key `trip.editTrip` không dùng).
5. Ghi chú cho khoản chi nhóm: không có ô nhập (xem 1.4).
6. Kết thúc nhóm thường; danh mục cho nhóm thường; chọn tập con người chia ở nhóm thường: KHÔNG (chỉ chuyến đi).
7. Chuyển quyền admin, đổi role, rời nhóm cho admin, xoá khách khỏi nhóm: KHÔNG có UI (`PATCH members` và `removeGuest` không được gọi từ màn hình nào: grep `removeGuest|deleteGroupGuest` chỉ có store + api).
8. Giới hạn thành viên: không có (không được hứa "tối đa N người" hoặc "không giới hạn" như cam kết sản phẩm; chỉ nói "không giới hạn cứng trong code hiện tại").
9. Xác nhận 2 chiều (người nhận phải duyệt khoản thanh toán): KHÔNG có. Settlement ghi là có hiệu lực ngay, không trạng thái chờ.
10. Mời bằng email gửi mail/ push: KHÔNG qua UI. Ô "Email để thêm" thêm thẳng người đã có tài khoản vào nhóm, không cần họ đồng ý, không gửi thông báo (hàm `notifyMemberAdded` không được gọi ở đâu). Hàm gửi push mời theo email (`notifyGroupInvitation`) chỉ chạy khi `createInviteLink(groupId, email)` có email, mà màn Thành viên luôn gọi không có email (`members.tsx:76`).
11. Chia sẻ tổng kết dạng ảnh / PDF / link đẹp: KHÔNG, chỉ văn bản.
12. Xếp hạng "tiết kiệm nhất"/gamification nhóm: không có; leaderboard là số dư & tổng đã trả.
13. Tính năng web (xem/quản lý nhóm trên web): không có trong repo này; `moni.live/invite` chỉ là trang dẫn tải app.
14. Gom nợ chéo giữa nhiều nhóm: KHÔNG (mỗi nhóm tính riêng; `debt-summary` chỉ cộng tổng hiển thị).

---
## 3. CẦN XÁC MINH (chưa chắc / có dấu hiệu lỗi – đừng quảng cáo cho tới khi test)

1. **Người nhận bấm "Xác nhận" cho khoản nợ của thành viên thật**: UI (`balance-summary.tsx:198-203`, `settle.tsx:72-80`) gửi settlement với from_user = người nợ, không có proxy; server chỉ cho from_user ≠ người gọi khi proxy = người gọi VÀ người nợ là khách (`API/settlements.ts:53-68`) -> theo code sẽ bị 403 "from_user_id must be the caller". Chỉ luồng người nợ tự "Ghi nhận thanh toán" và luồng "Đã thu tiền" cho khách chắc chắn khớp server. Cần test 2 máy trước khi viết "người nhận xác nhận".
2. **Admin "Xóa thành viên"**: `members.tsx:104` truyền `member.userId` vào `removeMember` nhưng hàm cần id dòng group_members (`FE-API/group-members.ts:66-76`, server `WHERE id = ...` `API/group-members.ts:111-123`) -> nhiều khả năng 404. Push "Bạn đã rời nhóm" khi bị xoá cũng dùng sai id và chạy sau khi đã xoá (người nhận không còn là thành viên nên fanout từ chối) -> không bao giờ tới. "Rời nhóm" thì dùng đúng id (`group-members.ts:86-93`).
3. **Push lời mời theo email** (nếu sau này bật): tên người mời gửi là userId và tên nhóm rỗng (`group-invitations.ts:55-60`) -> nội dung xấu. Hiện không chạy từ UI nên không ảnh hưởng, nhưng đừng quảng cáo.
4. **Ai được sửa/xoá chi tiêu ở server**: route không kiểm người trả (`API/shared-expenses.ts:281-363` chỉ `requireMember`); file RLS `api/src/db/sql/policies/groups.sql:78-84` nói payer-only, nhưng chưa xác minh RLS có thực sự áp dụng (kết nối DB có thể bypass RLS). Cũng theo file RLS: chi tiêu do KHÁCH trả (`INSERT ... auth_uid() = paid_by` `:74-76`) và settlement thay mặt khách (`:122-124`) có thể bị chặn nếu RLS hiệu lực, trái với route. Không có test cho 2 luồng khách. Cần test thật "thêm chi tiêu do khách trả" và "Đã thu tiền" trước khi quảng cáo mạnh tính năng khách.
5. **Kết thúc chuyến đi chỉ chặn ở UI**: server không kiểm `status='ended'` khi thêm chi tiêu (`API/shared-expenses.ts:201-277`); nhấn giữ để xoá chi tiêu trong chuyến đã kết thúc không bị chặn ở UI (`use-group-detail-data.ts:95-104`). Không viết "khóa vĩnh viễn".
6. **Tổng chi tiêu / ngân sách đang cộng cả khoản "Thu nhập"**: `totalSpent` cộng mọi expense không lọc type (`[id].tsx:62-65`; `computeTripSummary` `FE-API/trip-summary.ts:38`) -> nếu nhóm có khoản "Thu nhập" thì tổng/ngân sách/TB mỗi người bị lệch. (Endpoint `/trip-summary` của server có lọc theo type nhưng app KHÔNG gọi nó; `API/trip-summary.ts:34-35`.)
7. **Số dư tham gia đúng khi thành viên rời nhóm**: người đã rời vẫn còn nợ trong sổ; client có thể hiện tên "Unknown" cho họ (`balance-service.ts:35,73`). Chưa test.
8. **Realtime**: app lắng nghe sự kiện bảng nhóm (`use-group-realtime.ts`) nhưng tôi không tìm thấy trigger phát sự kiện cho shared_expenses/settlements/group_members trong `api/src/db/sql/triggers/30-sync-event-emission.sql` (grep rỗng). Chưa chắc có "cập nhật tức thì giữa các máy"; chỉ chắc chắn có kéo-để-làm-mới và tải lại khi mở màn.
9. **Danh sách "Lời mời đang chờ" có hiện cả lời mời đã dùng không**: API trả mọi status, UI không lọc status (`members.tsx:214-219`). Cần mở app xem.
10. **Cách gắn "Khoản nợ" vào nhóm** (nguồn của thẻ Liên quan): API nợ nhận `group_id` (`api/src/routes/debts.ts:39,104`) nhưng không tìm thấy UI chọn nhóm khi tạo nợ. Thẻ "Khoản nợ" có thể hiếm khi xuất hiện; thẻ "Quỹ tiết kiệm nhóm" thì có đường tạo (`app/group-savings/create.tsx`). Cần xem group-savings có dành cho nhóm thường hay chỉ couple.
11. **Màn gọi `getDebtSummary` / `deleteSettlement`**: không đọc hết code home; chưa xác nhận có UI "tổng nợ mọi nhóm" hay "xoá khoản thanh toán". Đừng đề cập.
12. **Hiển thị tiền "đ" trong push** quy đổi từ đơn vị nhỏ nhất ÷100 (`group-notifications.ts:33-43`), luôn đuôi "đ" kể cả khi người xem dùng tiền tệ khác.
13. **Role hiển thị** trong màn Thành viên là chuỗi thô "admin"/"member"/"guest" chưa dịch (`members.tsx:149-151`) – nếu chụp màn hình quảng cáo sẽ thấy tiếng Anh.

---
## Key i18n có trong vi.json nhưng KHÔNG dùng trong code (đừng dựa vào chúng để viết tính năng)
`groups.balances`, `groups.cannotEditOthers` (UI ẩn nút sửa thay vì báo), `groups.includingGuests`, `groups.joined`, `groups.memberExpensesTitle`, `groups.memberSpent`, `groups.presetName`, `groups.saveChanges`, `trip.defaultCurrency`, `trip.editTrip`, `trip.expenseDate`, `trip.tripCreated`, `trip.tripEnded`, `trip.days` (dùng `_one/_other`). Phương pháp: grep nguyên chuỗi key trong `app/` và `src/` (trừ tests/locales); key dựng động (`groups.expenseType*`, `trip.tab*`, nhãn danh mục `trip.category*`) đã tính là dùng.

## Chuỗi hợp lệ để trích dẫn (vi.json)
- Nhóm: "Nhóm chi tiêu chung", "Chuyến đi", "Tạo nhóm", "Tạo chuyến đi", "Thêm chi tiêu", "Chia sẻ liên kết mời", "Nhập mã mời", "Lời mời đang chờ", "Thêm khách mới", "Tên khách".
- Số dư: "Bạn đang nợ", "Bạn sẽ nhận", "Bạn không nợ ai", "Thanh toán tối ưu", "Ghi nhận thanh toán", "Đã thu tiền", "Xác nhận đã thu tiền".
- Chuyến đi: "Dòng thời gian", "Số dư", "Thành viên", "Ngân sách", "Tổng kết chuyến đi", "Tổng chi tiêu", "Trung bình mỗi người", "Theo danh mục", "Chi nhiều nhất", "Cần thanh toán", "Chia sẻ tổng kết", "Kết thúc chuyến đi", "Chia cho", "Mẫu chia".

## Câu hỏi chưa giải quyết
1. Luồng "Xác nhận" của người nhận (mục 3.1) và "Xóa thành viên" (3.2) có thực sự lỗi trên production không? Cần test 2 tài khoản.
2. RLS có đang hiệu lực với kết nối API trên Railway không (quyết định "chỉ người trả sửa/xoá" là bảo đảm ở server hay chỉ ở UI)?
3. Trigger realtime cho nhóm có tồn tại ở DB thật không?
4. Khoản "Thu nhập" trong nhóm có phải tính năng định quảng cáo không (tổng/ngân sách đang tính lẫn)?
5. Onboarding "Với Bạn Bè" dẫn tới màn nào (chưa đọc)?
6. Giá trị `groups.list` bị filter couple: nhóm ended của loại 'group' có hiển thị không (chưa kiểm).
