# Fact sheet: Mục tiêu tiết kiệm + Quỹ tiết kiệm nhóm (Moni)

Repo gốc: `/Users/rotationba/Luan/money-mate`. Mọi đường dẫn tính từ repo đó. Đọc ngày 2026-10-12, nhánh main; các file savings/group-savings không nằm trong danh sách file đang sửa dở (git status đầu phiên).
Ký hiệu: `file:dòng`. "vi.json" = `src/i18n/locales/vi.json`.

---------------------------------------------------------------------
## A. MỤC TIÊU TIẾT KIỆM CÁ NHÂN (màn `/savings`)
---------------------------------------------------------------------

### A1. Có thật

**Tên và lối vào**
- Tên màn: "Mục tiêu tiết kiệm" (`savings.title`, vi.json block `savings` bắt đầu dòng 1087). Phụ đề: "Tiết kiệm cho ước mơ của bạn" (`savings.subtitle`), hiện ở quick link ngân sách (`src/components/budget/budget-quick-links.tsx:23-24`).
- Lối vào có thật:
  1. Tab Khám Phá > nhóm "Tài Sản" > "Mục Tiêu Tiết Kiệm" -> `/savings` (`src/lib/hooks/use-explore-sections.ts:83-91`; nhãn `explore.savings` vi.json:1683).
  2. Màn Ngân sách: dòng quick link "Mục tiêu tiết kiệm / Tiết kiệm cho ước mơ của bạn" (`app/budget-view.tsx:131-134`, `budget-quick-links.tsx:19-26`).
  3. Trang chủ: ô lối tắt "Tiết kiệm" (`src/components/home/quick-access-grid.tsx:28-33`, `home.quickAccess.savings`; grid render ở `app/(tabs)/index.tsx:128`).
  4. Thẻ gợi ý ngữ cảnh trang chủ "Gần Đạt Rồi! / Đạt X% mục tiêu tiết kiệm" khi trung bình tiến độ >= 70% (`src/lib/services/context-card-engine.ts:92-103`, `src/lib/hooks/use-context-cards.ts:53-61`; chuỗi vi.json block `contextCard` dòng 1702). Trung bình tính trên TẤT CẢ mục tiêu trong store, kể cả đã hoàn thành (`use-context-cards.ts:21,54`).
- Không bị ẩn theo vùng: chỉ dòng gợi ý "tài sản" dùng `isVietnamRegion` (`app/savings/index.tsx:59,85`).

**A1.1 Trường khi tạo mục tiêu** (`src/components/savings/goal-form.tsx`)
- Bắt buộc: Tên mục tiêu (placeholder "VD: iPhone mới", tối đa 60 ký tự: dòng 103-111; lỗi "Vui lòng nhập tên mục tiêu" dòng 72-75); Số tiền mục tiêu > 0 (dòng 76-79, 113-124, tối đa 15 ký tự nhập).
- Tùy chọn: "Hạn chót (tùy chọn)" (date picker, ngày nhỏ nhất = hôm nay, có "Xoá hạn chót": dòng 126-154); Biểu tượng (12 emoji cố định: dòng 19-32, mặc định 🎯); Màu sắc (8 màu cố định: dòng 33-42, mặc định cam).
- Không có trường ghi chú (schema SQLite `src/lib/db/savings-goals-schema.ts:3-14`, schema server `api/src/db/schema/sync-tables.ts:232-253`).
- Không thấy giới hạn số lượng mục tiêu (`src/lib/api/savings-goals.ts:55-103`, `src/stores/savings-store.ts:34-45`, `api/src/routes/savings-goals.ts:62-80`).
- Nút "Tạo mục tiêu" / "Cập nhật" (`goal-form.tsx:216-220`); tiêu đề modal "Mục tiêu mới" / "Sửa mục tiêu" (`app/savings/index.tsx:196`, `app/savings/[id].tsx:270`). Mở form tạo bằng nút "Thêm" ở header (`app/savings/index.tsx:93-103`).

**A1.2 Nạp / rút tiền**
- Nạp: nút "+ Nạp tiền" trên thẻ mục tiêu đang chạy (`src/components/savings/goal-card.tsx:146-160`) hoặc nút "Nạp tiền" ở màn chi tiết (`app/savings/[id].tsx:215-224`). Bottom sheet có công tắc "Nạp tiền" / "Rút tiền" (`src/components/savings/goal-deposit-modal.tsx:27,108-130`).
- Nạp: số tiền > 0 (`goal-deposit-modal.tsx:45-48`; `savings-goals.ts:166`). Không chặn nạp vượt mục tiêu; % bị cắt ở 100 (`goal-calc-utils.ts:26-29`).
- Rút: số tiền > 0 và <= số đã tiết kiệm, lỗi "Không đủ tiền trong mục tiêu để rút" (`goal-deposit-modal.tsx:51-54`; `savings-goals.ts:203-205`).
- Tự đánh dấu hoàn thành khi `current >= target` (`savings-goals.ts:171-181`); rút tiền xoá `completed_at` (`savings-goals.ts:207-213`).
- Sửa: nút "Sửa" ở header màn chi tiết (tên/mục tiêu/hạn/icon/màu) (`app/savings/[id].tsx:123-130`, `savings-goals.ts:105-154`). Xoá: "Xóa mục tiêu" + xác nhận "Bạn có chắc muốn xóa mục tiêu này?" (`app/savings/[id].tsx:75-87,227-231`). Xoá cứng ở máy + đồng bộ DELETE (`savings-goals.ts:156-160`); server soft-delete (`api/src/routes/savings-goals.ts:101-112`). Số đã nạp nằm ngay trong bản ghi mục tiêu nên mất cùng mục tiêu.
- Nạp/rút là sổ sách trong app: chỉ cộng/trừ một con số `current_amount` (`savings-goals.ts:171-181, 207-213`).

**A1.3 Hiển thị tiến độ** (`src/components/savings/goal-calc-utils.ts`)
- % = current/target, tối đa 100 (`:26-29`). "Còn lại" = target - current, tối thiểu 0 (`:25`; chi tiết `app/savings/[id].tsx:115,193-197`).
- Thanh tiến độ trên thẻ có vạch "kỳ vọng" mờ = % thời gian đã trôi giữa ngày tạo và hạn chót (`goal-card.tsx:100-114`, `goal-calc-utils.ts:55-66`).
- 5 trạng thái: Hoàn thành; Cấp bách (còn <= 7 ngày); Chậm tiến độ (thực tế thấp hơn kỳ vọng hơn 5 điểm %); Đúng tiến độ; Không hạn chót (`goal-calc-utils.ts:80-89`; nhãn dùng key động `goal-card.tsx:37-41`).
- Cần/ngày = còn lại / số ngày còn lại; cần/tháng = cần/ngày x 30 (`goal-calc-utils.ts:68-70`) -> thẻ: "Cần tiết kiệm X/ngày để đúng tiến độ" (`goal-card.tsx:51-55`); nếu chậm: "Bạn đang chậm X% so với kế hoạch" (`:46-50`).
- Dự báo "Với tốc độ hiện tại, hoàn thành sau ~N ngày" = còn lại / (đã có / số ngày từ lúc tạo), chỉ có khi mục tiêu có hạn chót (`goal-calc-utils.ts:55-66,74-78`; `goal-card.tsx:56-60`). Là số ngày, không phải ngày lịch.
- Thẻ tổng hợp đầu màn (khi có >= 1 mục tiêu): "Tổng đã tiết kiệm", % tổng, "Còn lại" + tối đa 3 dòng: "Bạn cần tiết kiệm X/tháng để đạt mục tiêu", "N mục tiêu đang chậm tiến độ", "Với tốc độ hiện tại, mục tiêu xa nhất hoàn thành sau N ngày" (`goal-hero-card.tsx:16-56,66-95`).
- "Còn N ngày" cạnh % (`goal-card.tsx:128-134`).
- Hoàn thành: màn chi tiết hiện "Đã hoàn thành 🎉" (chỉ chữ + emoji) (`app/savings/[id].tsx:150-154`); thẻ có trạng thái ✅ (`goal-card.tsx:17-23`); mục tiêu xong vào nhóm "Đã hoàn thành" (`app/savings/index.tsx:141-155`, `src/lib/hooks/use-savings-goals.ts:34-35`). Chỉ có 2 nhóm: đang chạy / hoàn thành.
- Hộp "Gợi ý thông minh" (tối đa 3 dòng): "Thêm X hôm nay để giữ "tên" đúng tiến độ", "Tăng tiết kiệm hàng tháng lên X để hoàn thành đúng hạn", "Bạn đang có X tài sản có thể dùng cho mục tiêu", "Tài sản hiện tại đủ để hoàn thành tất cả mục tiêu còn lại" (`goal-suggestion-card.tsx:20-80`). Dòng tài sản chỉ cho người dùng vùng Việt Nam, giá trị lấy từ danh mục vàng/tài sản (`app/savings/index.tsx:59-60,84-85`).

**A1.4 Tiền tệ**
- Lưu dạng cents (x100), hiển thị theo đơn vị tiền người dùng chọn trong cài đặt (`goal-card.tsx:93`, `app/savings/[id].tsx:29,157`; `src/lib/utils/currency.ts:17-31,58-60`). Định dạng cho VND, USD, EUR, GBP, JPY, KRW, CNY, THB, IDR, BRL (`currency.ts:4-15`). Mọi mục tiêu hiển thị cùng 1 đơn vị toàn cục, không quy đổi.

**A1.5 Đồng bộ / offline**
- Ghi SQLite cục bộ rồi vào hàng đợi đồng bộ (`savings-goals.ts:62-89, 138-153, 186-190`); store gọi `triggerSync` sau mỗi thao tác (`savings-store.ts:38,51,67,78,91`); kéo-làm-mới gọi `pullScreenTables` (`app/savings/index.tsx:28,67-72`). Server có CRUD `/api/savings-goals` (`api/src/routes/savings-goals.ts`).

**A1.6 Liên hệ giao dịch / ngân sách / thử thách**
- Nạp/rút không tạo giao dịch và không đổi số dư: `depositToGoal`/`withdrawFromGoal` chỉ UPDATE bảng `savings_goals` (`savings-goals.ts:162-220`).
- Với Ngân sách: chỉ là quick link (Mục tiêu tiết kiệm + Thử thách chi tiêu) ngay dưới phần tóm tắt (`budget-quick-links.tsx:19-34`, `app/budget-view.tsx:131-134`).
- Thử thách: "Thử thách chi tiêu" - "Mục tiêu gamification để kiểm soát chi tiêu" (`challenges.title/subtitle`, vi.json block `challenges` dòng 1144). Tách biệt hoàn toàn khỏi mục tiêu tiết kiệm (không dùng chung code); chỉ chung chỗ đặt lối vào (quick link, Khám Phá > "Thói Quen" > "Thử Thách" `use-explore-sections.ts:206-214`).

### A2. KHÔNG có (không được nói)
- Không có lịch sử từng lần nạp/rút (chỉ một số dư): `src/lib/db/savings-goals-schema.ts:3-14`; `app/savings/[id].tsx` không có danh sách.
- Không có ghi chú/ảnh cho mục tiêu.
- Không có nhắc nhở / thông báo đẩy cho mục tiêu cá nhân (quét `api/src/jobs`, `api/src/services`, `src/` không thấy loại thông báo savings goal; job duy nhất liên quan là nhắc quỹ nhóm, mục B). Không tự động nạp theo lịch.
- Không tự trích tiền từ ví hay tài khoản ngân hàng.
- Không hiệu ứng ăn mừng (confetti/âm thanh/push), chỉ "Đã hoàn thành 🎉".
- Không "lưu trữ" mục tiêu; không chia sẻ mục tiêu cá nhân.
- Không nạp/rút được ở mục tiêu ĐÃ hoàn thành qua UI: màn chi tiết ẩn nút Nạp tiền khi hoàn thành (`app/savings/[id].tsx:215`), danh sách "Đã hoàn thành" không truyền `onDeposit` (`app/savings/index.tsx:149-153`).
- Không có "ngày hoàn thành dự kiến" dạng lịch.

### A3. Cần xác minh / lưu ý
- Màn kéo bảng `transactions` (`app/savings/index.tsx:28`) nhưng không có code dùng nó cho mục tiêu: đừng nói "tự tính từ giao dịch".
- Sửa số tiền mục tiêu xuống dưới số đã nạp: `completed_at` không được tính lại (`savings-goals.ts:105-154`); thẻ hiện "Hoàn thành" vì dùng `remaining <= 0` (`goal-calc-utils.ts:30`) nhưng danh sách vẫn xếp "đang chạy" (`use-savings-goals.ts:34-35`). Trường hợp biên, không quảng cáo.
- "Cần/tháng" dùng 30 ngày cố định; "tốc độ hiện tại" tính từ ngày tạo mục tiêu và chỉ có khi có hạn chót: dùng chữ "ước tính".
- Key i18n `savings.*` không dùng trong code (kết quả quét `app/` + `src/`, trừ test, key động đã tính): `savings.remaining`, `savings.deadlinePassed`, `savings.deadlineToday`, `savings.deadlineTomorrow`, `savings.invalidDate`. Không có hiển thị "Đã quá hạn / Hôm nay / Ngày mai" thực tế.
- Bản build/OTA đang chạy có chứa đúng code này hay không: không kiểm được từ repo.

---------------------------------------------------------------------
## B. QUỸ TIẾT KIỆM NHÓM (màn `/group-savings`)
---------------------------------------------------------------------

### B0. Tên đúng trong app
- Tiêu đề màn: "Tiết kiệm nhóm" (`groupSavings.title`, vi.json block `groupSavings` dòng 1759; `app/group-savings/index.tsx:95-96`); mục Khám Phá (đang ẩn) cũng "Tiết kiệm nhóm" (`explore.groupSavings`). Trong phần Cặp đôi gọi là "Quỹ tiết kiệm" (`couple.statsPoolsTitle` vi.json:1514; "Chuyển vào quỹ tiết kiệm" vi.json:1517). Hai loại quỹ: "Quỹ chung" (`shared_pot`) và "Mục tiêu cá nhân" (`individual_goals`) (`app/group-savings/create.tsx:195-223`). "Quỹ tiết kiệm nhóm" không phải tên chính thức trong app.

### B1. Có thật

**Lối vào**
- Mục Khám Phá cho Tiết kiệm nhóm ĐANG BỊ ẨN: nằm trong khối chú thích `// TODO: unhide when ready` (`src/lib/hooks/use-explore-sections.ts:136-160`). Không có ô trang chủ/Ngân sách nào trỏ tới `/group-savings` (grep `app/`+`src/`: chỉ các điểm dưới đây).
- Lối vào thực tế:
  1. Cặp đôi > biểu tượng biểu đồ ở header "Quỹ gia đình" (`app/couple/index.tsx:268-276`) -> Thống kê -> thẻ "Quỹ tiết kiệm": liệt kê tối đa 3 quỹ có thanh tiến độ, nút "Tạo quỹ" khi chưa có, "Xem tất cả quỹ" khi > 3 (`app/couple/stats.tsx:43`, `src/components/couple/couple-savings-pools-summary.tsx:23,79-160`).
  2. Cặp đôi > thẻ quỹ tháng > "Chuyển vào quỹ tiết kiệm ›" (chỉ hiện khi `remaining > 0`) (`src/components/couple/couple-fund-hero.tsx:153-163`); nếu chưa có quỹ thì đưa thẳng sang màn tạo quỹ của cặp đôi (`app/couple/index.tsx:111-125`).
  3. Cặp đôi > Cài đặt > phân bổ "Tiết kiệm" > "Chuyển tiền tiết kiệm ban đầu" hoặc "✓ Đã chuyển vào quỹ {tên}" (bấm mở quỹ) (`app/couple/settings.tsx:252-264, 520-558`).
  4. Chi tiết nhóm -> thẻ "Liên quan" (B7), chỉ hiện nếu nhóm đã có quỹ hoặc khoản nợ (`src/components/groups/group-related-items-card.tsx:48-49`; gắn ở `app/groups/[id].tsx:195`).

**B1.1 Ai tạo, trường dữ liệu**
- API: mọi THÀNH VIÊN nhóm đều tạo được quỹ (`requireMember` rồi insert, `api/src/routes/group-savings.ts:172-183`); không kiểm theo loại nhóm (`groups.type` = group | trip | couple: `api/src/db/schema/groups.ts:33`).
- App: bộ chọn nhóm cuộn ngang (`app/group-savings/create.tsx:149-184`) lấy từ `useGroupStore().groups`, danh sách đầy đủ gồm cả nhóm cặp đôi, khác `filteredGroups` đã loại couple (`src/stores/group-store.ts:57-65,82-98`). Bỏ bước chọn khi mở từ Cặp đôi (tham số `groupId`).
- Trường: Chọn nhóm*, Tên quỹ* ("VD: Quỹ du lịch nhóm"), Loại quỹ* (Quỹ chung / Mục tiêu cá nhân), Mục tiêu (chỉ khi "Quỹ chung"; nhãn "Mục tiêu (VND, không bắt buộc)"), "Đóng góp hàng tháng (tùy chọn)", Ngày bắt đầu* (gõ tay `YYYY-MM-DD`, mặc định hôm nay), Biểu tượng (8 emoji), Màu sắc (8 màu) (`create.tsx:22-32,186-300`). Tên tối đa 200 ký tự (`api/src/schemas/group-savings.ts:8`).
- Chỉ người tạo quỹ hoặc admin nhóm được sửa/xoá quỹ (`api/src/lib/pool-access.ts:41-51`; PATCH/DELETE `group-savings.ts:186-225`; RLS `api/src/db/sql/policies/group-savings.sql:16-24`).

**B1.2 Đóng góp**
- Mọi thành viên đóng góp vào quỹ đang `active` (`group-savings.ts:228-255`). App: ô nhập tiền + nút "Thêm", chip nguồn "Nhập tay" / "Dư chi tiêu" (`app/group-savings/[id].tsx:278-355`; `groupSavings.sourceManual/sourceSurplus`). Được đóng nhiều lần cùng kỳ (không UNIQUE: `api/src/db/schema/group-savings.ts:65-69`). Kỳ `YYYY-MM` theo giờ Việt Nam (`group-savings.ts:239-241`).
- KHÔNG gắn tiền thật: chỉ là bản ghi số liệu; chip "Dư chi tiêu" chỉ gắn `note='monthly-surplus'`, không tạo giao dịch (`[id].tsx:111-132`, `src/lib/utils/contribution-source.ts:6-20`).
- "Lịch sử đóng góp": 20 dòng gần nhất (số tiền, người đóng "Bạn"/tên, "Tháng M/YYYY", nhãn nguồn, ngày) (`[id].tsx:64-72,410-464`).
- Khối "Thành viên": avatar, tên, tổng đã đóng, thanh tỉ lệ trên tổng quỹ (`[id].tsx:357-408`). Không phải bảng xếp hạng có thứ hạng (không sắp xếp: `group-savings.ts:105-110`).
- Quỹ chung có mục tiêu: pill %, thanh, "Mục tiêu X", "Còn X" (`[id].tsx:162-165,216-275`; API `percentage = round(tổng/mục tiêu*100)` `group-savings.ts:120-132`). Không chặn đóng vượt mục tiêu; thanh cắt 100% (`[id].tsx:251`).

**B1.3 Cặp đôi: chuyển số dư còn lại**
- Nút "Chuyển vào quỹ tiết kiệm" -> sheet "Chuyển số dư còn lại": chọn quỹ đang hoạt động của cặp đôi, số tiền mặc định = số còn lại, không vượt số còn lại, "Xác nhận chuyển" (`src/components/couple/couple-leftover-transfer-sheet.tsx:48-58,60-95,96-171`; vi.json:1517-1530).
- Backend làm trong 1 transaction DB: (a) tạo giao dịch chi thật `expense` ở ví chung cặp đôi, tiêu đề "Chuyển vào {tên quỹ}", danh mục hệ thống `system-savings-transfer`; (b) cộng đóng góp vào quỹ, note `monthly-surplus`. Kiểm quỹ thuộc đúng cặp đôi, khoá chống chuyển trùng, tính lại số còn lại ở server và từ chối nếu vượt (`api/src/routes/couples.ts:723-866`; cụ thể 740, 749, 803-806, 831-852, 854-865; hằng số category dòng 51). Hệ quả: số "Còn lại" của tháng giảm tương ứng.
- "Chuyển tiền tiết kiệm ban đầu": chỉ ghi đóng góp (tag riêng), KHÔNG tạo giao dịch vì khoản tiết kiệm đã được trừ khỏi quỹ gia đình ở bước phân bổ (`couple-initial-savings-transfer-sheet.tsx:35-39,76-100`).

**B1.4 Thông báo**
- Chỉ 1 loại: `pool_contribution_reminder` - "Nhắc đóng quỹ tiết kiệm: Hôm nay là ngày đóng quỹ "{tên}". Đừng quên chuyển tiền nhé!" (`api/src/jobs/handlers/pool-contribution-reminder.ts:54-62`). Cron 08:00 mỗi ngày (`api/src/jobs/scheduler.ts:66`), gửi 9h sáng (`targetTime: 'daily_9am'`), chỉ cho người có lịch định kỳ đang bật, đúng ngày trong tháng, quỹ `active`, và chưa đóng trong kỳ hiện tại (`:31-50`).
- Tạo quỹ / đóng góp KHÔNG gửi thông báo cho thành viên khác (không có enqueueNotification trong `api/src/routes/group-savings.ts`).

**B1.5 Đồng bộ**
- Dữ liệu quỹ gọi thẳng API mỗi lần mở/kéo làm mới (`app/group-savings/index.tsx:74-87`, `[id].tsx:64-76`); cần đăng nhập (`AuthGuard`, `index.tsx:90`). Không có offline-queue hay realtime cho quỹ: danh sách bảng realtime chỉ có `savings_goals`, không có bảng pool (`api/src/realtime/types.ts:14`; grep "pool" trong file = không có). Thành viên khác phải mở lại/kéo làm mới mới thấy số mới.

### B2. KHÔNG có (không được nói)
- Mục tiêu riêng từng thành viên: API có `/targets` + bảng `group_savings_member_targets` (`group-savings.ts:314-351`) nhưng client không có hàm gọi (`src/lib/api/group-savings.ts` toàn file không có targets; grep `/targets` trong `app/`+`src/` = không có) và không có UI. Hệ quả: quỹ "Mục tiêu cá nhân" trong app không có mục tiêu/tiến độ: form ẩn ô Mục tiêu khi chọn loại này (`create.tsx:225-236`); API progress trả `total_target` (`group-savings.ts:159-167`) còn màn chi tiết chỉ đọc `progress.target_amount` (`[id].tsx:164`) nên không hiện thanh/%/còn lại. Thực chất chỉ là quỹ không mục tiêu có thống kê đóng góp theo người.
- Đóng góp định kỳ tự động: bảng `group_savings_recurring` chỉ ghi được qua `POST /:id/recurring` (`group-savings.ts:388-410`); client không có hàm gọi, không có UI (grep `/recurring` gắn pool trong `app/`+`src/` = không có). Job nhắc chỉ xét các dòng trong bảng này -> trong thực tế app không ai nhận nhắc. Kể cả khi có, đó chỉ là NHẮC, không tự trừ/cộng tiền. Tần suất duy nhất: "ngày X mỗi tháng" (`contribution_day` 1-31: `api/src/schemas/group-savings.ts:71`).
- Bình luận quỹ: `pool_comments` chỉ có API (`group-savings.ts:354-385`), client không gọi.
- Sửa/xoá từng đóng góp trong app: `deleteContribution` tồn tại (`src/lib/api/group-savings.ts:135-143`) nhưng không có màn nào gọi (grep). Chỉ xoá được cả quỹ, kéo theo mọi đóng góp (cascade: `api/src/db/schema/group-savings.ts:51-53`).
- Hoàn thành / đóng quỹ / rút tiền khỏi quỹ: `status` (active|completed|cancelled) chỉ đổi được qua API PATCH; app không bao giờ gửi `status` (`create.tsx:94-114`). Danh sách chỉ lấy quỹ `active` (`index.tsx:76,83`). Không có rút tiền; đóng góp chỉ cộng thêm.
- `target_date` (ngày đích) và `contribution_day` không có trong form tạo (cột có ở DB/API). "Đóng góp hàng tháng" có nhập nhưng không được hiển thị hay dùng để nhắc ở màn nào (`monthly_contribution` chỉ xuất hiện ở `create.tsx:74,98,110`).
- Không phải tiền thật / tài khoản chung: không kết nối ngân hàng, không thanh toán.
- Không thông báo cho thành viên khi có người đóng góp.

### B3. Lỗi / sai lệch (tránh quảng cáo hoặc báo dev)
1. Nút "Sửa quỹ" và "Xóa quỹ" hiện cho MỌI thành viên (`app/group-savings/[id].tsx:466-483`) nhưng API chỉ cho người tạo hoặc admin nhóm (`pool-access.ts:47-49`). Riêng xoá: `handleDelete` không try/catch quanh `deletePool` (`[id].tsx:143-146`; store ném lỗi `group-savings-store.ts:85-93`) -> rejection chưa xử lý, `router.back()` không chạy.
2. Màn quỹ dùng `formatCurrency(x)` không truyền đơn vị -> mặc định VND (`[id].tsx:236,265,270,385,429`; `index.tsx:58`; mặc định ở `src/lib/utils/currency.ts:19`), trong khi ô nhập dùng ký hiệu theo cài đặt (`[id].tsx:328`) và nhãn mục tiêu ghi cứng "VND" (`groupSavings.targetAmount`). Chỉ nên quảng cáo quỹ nhóm với VND.
3. Thẻ "Liên quan" hiện trạng thái quỹ dạng thô tiếng Anh (`active`/`completed`) (`group-related-items-card.tsx:128-132`).
4. Thẻ "Liên quan": mũi tên của mục quỹ mở `/group-savings` (danh sách mọi quỹ của người dùng, không lọc theo nhóm) (`:108-113`); mục Nợ trỏ `/debts`, tính năng cũng đang ẩn ở Khám Phá (`use-explore-sections.ts:136-147`). Backend giới hạn 3 quỹ + 3 nợ gần nhất (`api/src/routes/groups.ts:313-350`).
5. Sửa quỹ: xoá "Mục tiêu"/"Đóng góp hàng tháng" về 0 -> app gửi `undefined` (không gửi), giá trị cũ vẫn giữ (`create.tsx:97-98`). Cho đổi `type` khi sửa (`:96`). Ngày bắt đầu gõ tay, client không validate (API có regex `schemas/group-savings.ts:13`).
6. RLS xoá đóng góp chỉ cho chính người đóng (`policies/group-savings.sql:39-42`) trong khi route cho cả người tạo quỹ xoá của người khác (`group-savings.ts:300-305`). Chưa dùng ở UI; không quảng cáo "người tạo quỹ xoá được khoản của người khác". Chưa kiểm DB production có áp file SQL này.
7. Push nhắc có `data.route='group-savings'`, nhưng `handleNotificationNavigation` không có case này -> chạm thông báo không mở màn nào (`src/lib/utils/notification-navigation.ts:20-68`).
8. Với quỹ `individual_goals`, "Thành viên" chỉ liệt kê người đã có đóng góp (GROUP BY trên bảng đóng góp: `group-savings.ts:105-110,145-154`).
9. Key i18n không dùng: `groupSavings.progress`, `couple.leftoverTransferCategoryRequired` (script quét).

### B4. Cần xác minh
- Tiết kiệm nhóm đã ra production cho người dùng cuối chưa? Khám Phá đang TODO; lối vào hiện qua Cặp đôi. Với nhóm chi tiêu/chuyến đi thường chưa thấy đường dẫn để tạo quỹ LẦN ĐẦU (thẻ "Liên quan" ẩn khi chưa có quỹ/nợ; nút "+" ở màn danh sách nhưng màn danh sách chỉ vào được qua thẻ này hoặc qua Cặp đôi), dù API cho phép mọi loại nhóm. Cần hỏi chủ sản phẩm trước khi viết "quỹ cho nhóm bạn bè / chuyến đi".
- Có nhánh/OTA nào có UI "định kỳ", "mục tiêu từng thành viên", "bình luận" chưa merge không (chỉ kiểm main hiện tại).
- Cron `pool-contribution-reminder` đã đăng ký (`api/src/jobs/scheduler.ts:66`, `api/src/jobs/register-handlers.ts:37,64`), chưa kiểm chứng đang chạy ở production.

---------------------------------------------------------------------
## C. Cách nói an toàn cho landing page
- Cá nhân (an toàn): "Đặt mục tiêu tiết kiệm với tên, số tiền, hạn chót (tùy chọn), biểu tượng và màu sắc. Nạp/rút tiền, xem % tiến độ, số tiền cần tiết kiệm mỗi ngày/tháng (ước tính), cảnh báo 'chậm tiến độ' khi có hạn chót." Không nói: lịch sử nạp, nhắc nhở, tự trích tiền, liên kết giao dịch/ngân sách, hiệu ứng ăn mừng.
- Nhóm (chỉ phần cặp đôi): "Cặp đôi tạo quỹ tiết kiệm chung, chuyển số dư còn lại cuối tháng vào quỹ (đồng thời ghi một khoản chi ở ví chung), xem tổng và đóng góp của từng người." Không nói: nhắc đóng quỹ định kỳ, mục tiêu riêng từng thành viên, bình luận, rút tiền, hoàn thành quỹ, quỹ cho nhóm bạn/chuyến đi.

## D. Câu hỏi chưa giải quyết
1. Tiết kiệm nhóm đã bật cho người dùng cuối chưa (mục Khám Phá đang TODO)? Có kế hoạch mở cho nhóm thường/chuyến đi?
2. Landing nên gọi "Tiết kiệm nhóm" (tên màn) hay "Quỹ tiết kiệm" (tên trong Cặp đôi)?
3. UI mục tiêu từng thành viên, đóng góp định kỳ, bình luận (hiện chỉ có API) sẽ làm hay bỏ?
4. Hành vi mong muốn khi thành viên không phải người tạo bấm Sửa/Xóa quỹ (nút hiện nhưng API từ chối)?
5. Mục tiêu cá nhân: có kế hoạch thêm lịch sử nạp/rút và nhắc nhở không?
6. Có chuẩn hóa đơn vị tiền ở màn quỹ nhóm (đang mặc định VND) không?
