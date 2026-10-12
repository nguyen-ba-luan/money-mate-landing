# Recurring fact sheet (code-verified 2026-10-12)
## Shipped, advertise
- Entry: Khám Phá > "Giao Dịch Định Kỳ" (hidden for guests); Home quick tile "Định kỳ"; couple screen card "Mục lặp lại".
- List `/recurring`: summary "Ước tính mỗi tháng", "{n} đang chạy"; cards: category icon, amount, frequency, due label (Hôm nay / Ngày mai / Còn N ngày / Tiếp theo), "Biến động" badge, pause Switch ("Đã tạm dừng"). Sorted: active soonest first, paused last. Empty: "Chưa có giao dịch định kỳ" + "Thêm định kỳ".
- Form (Thêm/Sửa định kỳ): Chi tiêu/Thu nhập, Số tiền, Tên (VD: Tiền nhà, Netflix, Lương), Danh mục chips, Tần suất (Hàng ngày, Hàng tuần, Hai tuần một lần, Hàng tháng, Hàng năm), Ngày bắt đầu, Ngày kết thúc (tùy chọn), Số ngày thông báo trước (1-30, NOT functional), "Số tiền biến động (điện, nước,...)" switch, Lưu/Hủy, "Xóa quy tắc" (confirm).
- Auto-create: CLIENT only, on app open: one transaction per missed period (catch-up, max 90/rule). Skipped for variable rules and couple rules (date still advances). No server/background creation.
- Variable rules: no transaction; server cron 08:00 VN push "Đến hạn mục lặp lại" / `Đến hạn "{title}" — nhập số tiền thực tế nhé!` → opens add-transaction prefilled, linked via recurring_rule_id ("Mục lặp lại: {title}").
- Couple rules: shown in /couple card + "Dự kiến còn lại" sheet, "Bỏ qua tháng này"/"Khôi phục" (couple only).
## NOT advertise
- "Thông báo trước N ngày" (saved but nothing reads it). Reminders for fixed-amount rules (none). Background/server auto-creation (needs app open). Rule history/log screen. Skip for personal rules.
## Bugs (unfixed)
- Monthly rollover drift for day 29-31 (client date-fns clamp). Edit form shows nextRunDate as start date. Possible x100 prefill bug in /transaction/add?ruleId (verify). Dedupe merges rules with same title+amount+frequency.
