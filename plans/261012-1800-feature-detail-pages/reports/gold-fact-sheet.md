# Gold fact sheet (code-verified, 2026-10-12)

## Shipped, advertise
- Tab "Vàng" (app/(tabs)/gold.tsx), 5 sub-tabs: Giá vàng | Tín hiệu | Vĩ mô | Tin tức | Cảnh báo. Not gated by country/premium.
- Giá vàng: selector chips "Vùng / Nguồn" + "Sản phẩm" (persist AsyncStorage); hero card Mua/Bán + %Δ; chart 1D/1W/1M/3M/6M/1Y, line/candle (not on 1D); "So sánh" list across brands with "Rẻ nhất" badge; "Lịch sử giá" 5 rows + Xem thêm; "Theo tiệm" board + follow (max 5 shops, daily digest 08:30); "+ Đề xuất thêm cửa hàng" form.
- Sources: national, BTMC, SJC, DOJI, PNJ, Bảo Tín Mạnh Hải, Phú Quý, Ngọc Thẩm; shops: Kim Khánh Việt Hùng, Mi Hồng, Ngọc Thịnh, Phú Quý store. Crawled every 15/45 min.
- Tín hiệu: type SJC/9999/Nữ Trang × Mua/Bán (national only). Card MUA/GIỮ/BÁN + "Độ tin cậy" + factor rows (ARIMA, RSI, MACD, Tin tức) + "Dự báo 7 ngày tới" table with confidence band + disclaimer "chỉ mang tính tham khảo, không phải lời khuyên đầu tư". Needs >=90 days OHLC else "Dự báo sắp ra mắt" x/90. Engine: ARIMA(1,1,1) 60% + macro 40%, vote ARIMA x2 + RSI14 + MACD + sentiment; cron 08:00 VN.
- Vĩ mô: XAU/USD, USD/VND, DXY, cảm xúc tin tức. Tin tức: gauge + headlines.
- Cảnh báo (login required): form Loại vàng, Mua/Bán, Vượt qua/Xuống dưới, Vùng+Nguồn (optional, both or none), Ngưỡng (₫/chỉ). ONE-SHOT, checked 09:30 and 15:30 VN only (not real time).
- Tài sản tích luỹ (/assets; home quick tile + Khám Phá "Vàng & Đầu Tư"): hero tổng giá trị + lời/lỗ, phân bổ, nhận định; Đang giữ / Đã bán; add (SJC/9999/trang sức; giá thị trường hoặc thủ công; ngày mua; giá mua VNĐ/chỉ; số lượng chỉ, = x lượng; ghi chú); detail: sửa, xóa, đánh dấu đã bán. P&L uses national SELL price.
- Settings > "Tín hiệu vàng" toggle: local daily 08:30 reminder (static text), VN timezone only.

## NOT advertise
- Bollinger (computed, never shown, not in signal). RSI/MACD only as factor badges/bullets, no charts.
- "Gần tôi" (placeholder). Free province picker (none; region follows source). LLM chat advisor (none; Gemini only scores news). Real-time alerts. Per-brand/shop forecast or assets.
- Streak badge not marketed.

## Bugs (not fixed)
- Push taps gold_alert / gold_daily_digest don't navigate (only gold_daily_signal mapped).
- Gold tab hardcoded Vietnamese strings (tabs, alert confirms, "Cảm xúc thị trường"...).
- Asset form validation alert just shows field label.
- Dead code: app/assets/market.tsx, gold-alerts-section, gold-analysis-section.
- Home page over-claims: Bollinger Bands, "tỉnh thành".

## Seed needs
gold_sources/regions/products (migrations), gold_quotes, gold_ohlc_daily >=90d x 3 types x buy/sell, gold_indicators_daily, gold_forecasts, macro_indicators, news_headlines, gold_assets, gold_price_alerts, gold_source_subscriptions.
