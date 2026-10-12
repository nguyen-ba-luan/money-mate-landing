# Analytics/Reports fact sheet (code-verified 2026-10-12)
## Shipped, advertise
- Entry: Khám Phá > mục "Báo Cáo": "Phân Tích Chi Tiêu" (/analytics-view), "Báo Cáo Chi Tiết" (/report); Home hero analytics; open for guests; no premium gate.
- Phân Tích Chi Tiêu: period selector Hôm nay/Tuần/Tháng/Năm/Tùy chỉnh (7/30/90 ngày presets or DD/MM/YYYY); Xuất CSV / Xuất PDF; 4 cards Thu nhập, Chi tiêu, Số dư, TB Ngày; "Chi tiêu dự báo" (linear regression, needs 3+ days; "Đúng kế hoạch"/"Vượt ngân sách"); "Tháng này vs Tháng trước" (up to 6 categories); "Danh mục hàng đầu" (top 5); "Phân loại chi tiêu"; "Xu hướng chi tiêu hàng ngày" (last 14 days, TB); banner "Báo cáo tháng".
- Báo cáo tháng (/report): month picker; Thu nhập/Chi tiêu/Tiết kiệm + Tỷ lệ + TB mỗi ngày; Danh mục hàng đầu; "Tuân thủ ngân sách" (Vượt/OK); "Chi tiêu lớn nhất"; "Nhận xét" (7 rule-based insights); export PDF (Xuất).
- Personal wallet only (couple shared and group excluded).
## NOT advertise
- Pie/line charts (all bars), multi-month trends, search/filter, CSV for report, couple/group analytics, "Bảng Phân Tích" marketing text has no source in code. PDF report text is English.
## Bugs (unfixed)
- "Tháng này vs Tháng trước" and forecast break for non-Tháng periods; TB Ngày divides by fixed 30/365; PDF report hardcoded English.
