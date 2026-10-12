# Fact sheet: Ngân sách + công thức (nguồn: app repo, 2026-10-12)

## Có thật
- Ngân sách theo **danh mục chi** + **tháng/năm**; mỗi danh mục tối đa 1 ngân sách/tháng, trùng → báo "Trùng lặp", sửa thay thế (`app/budget/add.tsx`, `budget.duplicateMessage`; API 409 `Duplicate budget` `api/src/routes/budgets.ts:82`).
- Màn Ngân sách (`app/budget-view.tsx`): điều hướng tháng trước/sau, biểu đồ donut tổng (ngân sách/đã chi/còn lại/% dùng), danh sách ngân sách, bấm vào xem chi tiết + giao dịch thuộc ngân sách (`app/budget/[id].tsx`), nút xóa có xác nhận, sửa.
- Thanh tiến độ đổi màu: <60% xanh `#26AA99`, 60–85% cam, ≥85% đỏ (`budget-progress.tsx:getStatusColor`); thẻ hiện "Vượt ngân sách" khi chi > ngân sách (`budget.overBudget`).
- Tháng tài chính theo ngày bắt đầu (`getFiscalMonthLabel(now, startDay)` trong `src/lib/api/formulas.ts`).
- Trang chủ hiện số còn lại của ngân sách (`app/(tabs)/index.tsx:49`); thẻ gợi ý ngữ cảnh theo % đã dùng (`use-context-cards.ts`).
- Lối tắt sang Tiết kiệm và Thử thách ngay trong màn Ngân sách (`BudgetQuickLinks`).
- **Công thức tài chính** (`src/lib/constants/formula-templates.ts`), 7 mẫu: 6 Lọ (55/10/10/10/10/5), 50/30/20, 80/20, 70/20/10, Kakeibo (50/30/10/10), Zero-Based (50/30/20), Tùy chỉnh (50/30/20 mặc định). Luồng: chọn công thức → nhập thu nhập tháng → xem phân bổ → Áp dụng. Áp dụng tạo **danh mục riêng cho từng lọ + ngân sách tháng hiện tại** (`applyFormula`). Đổi công thức xóa ngân sách/danh mục của công thức cũ rồi tạo mới (`switchFormula`); đổi thu nhập tính lại số tiền (`updateFormulaIncome`). Màn Ngân sách có nút chuyển "Công thức"/"Danh sách" và tiến độ từng lọ.

- **Thông báo** khi dùng 80% và khi vượt 100%, mỗi mốc 1 lần/ngân sách/tháng, chạm vào mở màn Ngân sách (`src/lib/utils/budget-alert-checker.ts`, `notification-navigation.ts`; chạy lúc mở trang chủ `use-home-data.ts:160` và sau khi ghi chi tiêu). Chỉ cho người dùng đã đăng nhập.
- Lối vào: tab Khám Phá > mục Ngân sách (`use-explore-sections.ts:70`), thẻ "ngân sách còn lại" ở trang chủ (`daily-allowance-card.tsx:52`).
- Tiến độ từng lọ chỉ cộng chi tiêu ghi vào **danh mục của lọ đó** (`getFormulaProgress`, theo tháng lương `startDay`).

## KHÔNG có (không được nói trên landing)
- Chuyển tiếp ngân sách sang tháng sau (`budget.rolledOver` chỉ có trong i18n, không dùng trong code).
- Ngân sách tổng không theo danh mục; tự sao chép ngân sách sang tháng sau (không thấy code).

- Sửa % trong công thức "Tùy chỉnh": wizard chỉ hiển thị tỷ lệ 50/30/20, không có ô nhập (`formula-wizard-steps.tsx`). Không quảng cáo "tự định nghĩa tỷ lệ".

## Ghi chú
- Ngày bắt đầu tháng: `settings.salaryStartDay` 1–28 (`src/types/index.ts:470`).
