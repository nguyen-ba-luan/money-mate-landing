/**
 * Money Mate Landing Page - Internationalization (i18n)
 * Supports: English (en), Vietnamese (vi)
 */

(function () {
  'use strict';

  var translations = {
    en: {
      // Nav
      'nav.features': 'Features',
      'nav.how': 'How It Works',
      'nav.testimonials': 'Testimonials',
      'nav.download': 'Download App',

      // Hero
      'hero.tagline': 'Personal Finance, Simplified',
      'hero.title': 'Take Control of<br><span class="text-gold">Your Money</span>',
      'hero.desc': 'Track expenses by voice or photo, split costs with friends, manage budgets, earn Shopee cashback, and hit savings goals — all in one beautiful app.',
      'hero.badge.appstore.top': 'Download on the',
      'hero.badge.appstore.bottom': 'App Store',
      'hero.badge.google.top': 'GET IT ON',
      'hero.badge.google.bottom': 'Google Play',
      'hero.trust.rating': '4.8 Rating',
      'hero.trust.secure': 'Secure & Private',
      'hero.trust.languages': '10 Languages',

      // Features
      'features.tagline': 'Everything You Need',
      'features.title': 'Powerful Features for<br>Smart Finance',
      'features.desc': 'From voice-powered expense tracking to group trips, savings goals, challenges, and cashback rewards — Money Mate has everything.',
      'features.expense.title': 'Expense Tracking',
      'features.expense.desc': 'Log expenses instantly with categories, notes, and receipt photos. See where every dollar goes.',
      'features.sharing.title': 'Expense Sharing & Groups',
      'features.sharing.desc': 'Split bills with friends, track group expenses with trip timelines, and settle debts easily. Perfect for trips and shared living.',
      'features.budget.title': 'Budget Management',
      'features.budget.desc': 'Set monthly budgets by category, get smart alerts before overspending, and stay on track.',
      'features.analytics.title': 'Analytics Dashboard',
      'features.analytics.desc': 'Beautiful charts — daily trends, category breakdowns, month comparisons, and spending predictions — all in one view.',
      'features.language.title': '10 Languages Supported',
      'features.language.desc': 'Use Money Mate in your preferred language. English, Vietnamese, Spanish, French, and more.',
      'features.sync.title': 'Cloud Sync & Offline-first',
      'features.sync.desc': 'Your data syncs across devices automatically. Works offline too — never miss tracking an expense.',
      'features.voice.title': 'Voice Input',
      'features.voice.desc': 'Add expenses hands-free by speaking naturally. Just say "Coffee 50k" and it\'s logged instantly.',
      'features.savings.title': 'Savings Goals',
      'features.savings.desc': 'Set savings targets, track deposits, and watch your progress grow. Turn dreams into achievable milestones.',
      'features.challenges.title': 'Spending Challenges',
      'features.challenges.desc': 'Join spending challenges, earn badges, and build streaks to gamify your journey to better financial habits.',
      'features.reports.title': 'Smart Monthly Reports',
      'features.reports.desc': 'Get auto-generated monthly reports with spending trends, category insights, and personalized saving tips.',
      'features.recurring.title': 'Recurring Expenses',
      'features.recurring.desc': 'Set up subscriptions, rent, and bills as recurring transactions. Never forget a payment again.',
      'features.security.title': 'Biometric Security',
      'features.security.desc': 'Protect your financial data with Face ID, Touch ID, or PIN lock. Your data stays private, always.',
      'features.cashback.title': 'Cashback Rewards',
      'features.cashback.desc': 'Earn cashback on Shopee purchases through our affiliate program. Shop, earn, and withdraw — all tracked inside the app with your personal balance, streak rewards, and order history.',
      'features.cashback.badge1': 'Streak Rewards',
      'features.cashback.badge2': 'Real-time Balance',
      'features.cashback.badge3': 'Easy Withdrawal',
      'features.cashback.partner': 'via Shopee',

      // How it works
      'how.tagline': 'Get Started in Minutes',
      'how.title': 'How It Works',
      'how.desc': 'Four simple steps to financial clarity — and cashback rewards.',
      'how.step1.title': 'Download the App',
      'how.step1.desc': 'Get Money Mate free from the App Store or Google Play. Set up your account in seconds.',
      'how.step2.title': 'Track Your Expenses',
      'how.step2.desc': 'Add expenses by typing, voice, or photo. Categorize, tag, and split with friends effortlessly.',
      'how.step3.title': 'Set Budgets & Goals',
      'how.step3.desc': 'Get smart insights, set budgets by category, and create savings goals to reach your targets.',
      'how.step4.title': 'Earn Cashback',
      'how.step4.desc': 'Shop on Shopee through Money Mate, earn cashback on every purchase, and withdraw your balance anytime.',

      // Screenshots
      'screenshots.tagline': 'See It In Action',
      'screenshots.title': 'Beautiful & Intuitive Design',
      'screenshots.desc': 'Designed to make managing money feel effortless.',

      // Testimonials
      'stats.downloads': 'Downloads',
      'stats.rating': 'App Rating',
      'stats.languages': 'Languages',
      'testimonials.tagline': 'What Users Say',
      'testimonials.title': 'Loved by Thousands',
      'testimonials.1.text': '"Money Mate completely changed how I manage my finances. The group expense splitting is a lifesaver for our monthly apartment costs!"',
      'testimonials.1.name': 'Sarah A.',
      'testimonials.1.role': 'Freelance Designer',
      'testimonials.2.text': '"Best finance app I\'ve used. The analytics dashboard gives me insights I never had before. Finally understand where my money goes each month."',
      'testimonials.2.name': 'Mike T.',
      'testimonials.2.role': 'Software Engineer',
      'testimonials.3.text': '"The Vietnamese language support is perfect! I love using it to track expenses during our family trips. The offline mode works flawlessly."',
      'testimonials.3.name': 'Linh N.',
      'testimonials.3.role': 'Travel Blogger',

      // CTA
      'cta.tagline': 'Ready to Get Started?',
      'cta.title': 'Start Tracking Your<br>Finances Today',
      'cta.desc': 'Download Money Mate for free and take the first step toward financial clarity.',
      'cta.qr': 'Scan to download on App Store',

      // Footer
      'footer.desc': 'Personal finance management made simple. Track, split, budget, and earn.',
      'footer.product': 'Product',
      'footer.company': 'Company',
      'footer.legal': 'Legal',
      'footer.features': 'Features',
      'footer.how': 'How It Works',
      'footer.testimonials': 'Testimonials',
      'footer.download': 'Download',
      'footer.contact': 'Contact Us',
      'footer.support': 'Support',
      'footer.privacy': 'Privacy Policy',
      'footer.terms': 'Terms of Service',
      'footer.copyright': '&copy; 2026 Code4change. All rights reserved.',

      // Feature Showcase
      'showcase.tagline': 'Deep Dive',
      'showcase.title': 'Explore Key Features',
      'showcase.budget.title': 'Budget Management',
      'showcase.budget.desc': 'Set monthly budgets by category, get visual progress bars, and receive smart alerts before you overspend. Stay in control of every category — from food to entertainment.',
      'showcase.cashback.title': 'Cashback Rewards',
      'showcase.cashback.desc': 'Shop on Shopee through Moni and earn cashback on every purchase. Track your balance, streak rewards, and order history — all inside the app.',
      'showcase.group.title': 'Group Expenses',
      'showcase.group.desc': 'Create groups for trips, shared apartments, or dinner parties. Add expenses, and Moni automatically calculates who owes whom. Settlement is just one tap away.',
      'showcase.security.title': 'Secure & Private',
      'showcase.security.desc': 'Your financial data is protected with biometric authentication (Face ID, Touch ID), local encryption, and secure cloud sync. We never share your data with third parties.',

      // Comparison
      'compare.tagline': 'Why Moni?',
      'compare.title': 'How We Compare',
      'compare.feature': 'Feature',
      'compare.price': 'Price',
      'compare.group': 'Group Splitting',
      'compare.cashback': 'Cashback Rewards',
      'compare.voice': 'Voice Input',
      'compare.offline': 'Offline Mode',
      'compare.analytics': 'Analytics',
      'compare.languages': 'Languages',
      'compare.free': 'Free',
      'compare.yes': 'Yes',
      'compare.no': 'No',
      'compare.moni.rec': 'Recommended',

      // FAQ
      'faq.tagline': 'Got Questions?',
      'faq.title': 'Frequently Asked Questions',
      'faq.q1': 'Is Moni free to use?',
      'faq.a1': 'Yes, Moni is completely free to download and use. All core features — expense tracking, budgets, group splitting, and analytics — are free. Premium features may be added in the future.',
      'faq.q2': 'Is my financial data secure?',
      'faq.a2': 'Absolutely. We use biometric authentication (Face ID, Touch ID), local encryption with AES-256, and secure cloud sync via TLS 1.3. We never share your data with third parties.',
      'faq.q3': 'Does Moni work offline?',
      'faq.a3': 'Yes, Moni is offline-first. Track expenses without internet and your data syncs automatically when you reconnect.',
      'faq.q4': 'Which devices are supported?',
      'faq.a4': 'Moni is currently available for iOS (iPhone). Android support is coming soon.',
      'faq.q5': 'Can I export my data?',
      'faq.a5': 'Yes, you can export your expense data for personal records or accounting purposes.',
      'faq.q6': 'How does group expense splitting work?',
      'faq.a6': 'Create a group, add members, and log shared expenses. Moni automatically calculates who owes whom. Settlement is just one tap away.',
      'faq.q7': 'How does cashback work?',
      'faq.a7': 'Shop on Shopee through Moni\'s affiliate links, earn cashback on purchases, and withdraw your balance anytime.',

      // Email Signup
      'email.tagline': 'Stay Updated',
      'email.title': 'Get Tips & Updates',
      'email.desc': 'Subscribe for personal finance tips and new feature announcements.',
      'email.btn': 'Subscribe',
      'email.success': 'Thanks! We\'ll keep you updated.',
      'email.error': 'Please enter a valid email address.',
    },

    vi: {
      // Nav
      'nav.features': 'Tính Năng',
      'nav.how': 'Cách Hoạt Động',
      'nav.testimonials': 'Đánh Giá',
      'nav.download': 'Tải Ứng Dụng',

      // Hero
      'hero.tagline': 'Quản Lý Tài Chính, Đơn Giản Hóa',
      'hero.title': 'Kiểm Soát<br><span class="text-gold">Tài Chính Của Bạn</span>',
      'hero.desc': 'Theo dõi chi tiêu bằng giọng nói hoặc ảnh, chia chi phí với bạn bè, quản lý ngân sách, kiếm hoàn tiền Shopee và đạt mục tiêu tiết kiệm — tất cả trong một ứng dụng.',
      'hero.badge.appstore.top': 'Tải về trên',
      'hero.badge.appstore.bottom': 'App Store',
      'hero.badge.google.top': 'TẢI VỀ TRÊN',
      'hero.badge.google.bottom': 'Google Play',
      'hero.trust.rating': 'Đánh giá 4.8',
      'hero.trust.secure': 'Bảo Mật & Riêng Tư',
      'hero.trust.languages': '10 Ngôn Ngữ',

      // Features
      'features.tagline': 'Tất Cả Những Gì Bạn Cần',
      'features.title': 'Tính Năng Mạnh Mẽ Cho<br>Tài Chính Thông Minh',
      'features.desc': 'Từ theo dõi chi tiêu bằng giọng nói đến chuyến đi nhóm, mục tiêu tiết kiệm, thử thách và hoàn tiền — Money Mate có tất cả.',
      'features.expense.title': 'Theo Dõi Chi Tiêu',
      'features.expense.desc': 'Ghi nhận chi tiêu ngay lập tức với danh mục, ghi chú và ảnh hóa đơn. Biết rõ từng đồng đi đâu.',
      'features.sharing.title': 'Chia Sẻ Chi Phí & Nhóm',
      'features.sharing.desc': 'Chia hóa đơn với bạn bè, theo dõi chi phí nhóm theo dòng thời gian chuyến đi và thanh toán nợ dễ dàng.',
      'features.budget.title': 'Quản Lý Ngân Sách',
      'features.budget.desc': 'Đặt ngân sách hàng tháng theo danh mục, nhận cảnh báo thông minh trước khi chi tiêu quá mức.',
      'features.analytics.title': 'Bảng Phân Tích',
      'features.analytics.desc': 'Biểu đồ xu hướng hàng ngày, phân tích danh mục, so sánh tháng và dự báo chi tiêu — tất cả trong một màn hình.',
      'features.language.title': 'Hỗ Trợ 10 Ngôn Ngữ',
      'features.language.desc': 'Sử dụng Money Mate bằng ngôn ngữ yêu thích. Tiếng Anh, Tiếng Việt, Tiếng Tây Ban Nha, Tiếng Pháp và nhiều hơn nữa.',
      'features.sync.title': 'Đồng Bộ & Ngoại Tuyến',
      'features.sync.desc': 'Dữ liệu tự động đồng bộ trên các thiết bị. Hoạt động ngoại tuyến — không bao giờ bỏ lỡ ghi nhận chi tiêu.',
      'features.voice.title': 'Nhập Bằng Giọng Nói',
      'features.voice.desc': 'Thêm chi tiêu rảnh tay bằng cách nói tự nhiên. Chỉ cần nói "Cà phê 50k" là được ghi lại ngay.',
      'features.savings.title': 'Mục Tiêu Tiết Kiệm',
      'features.savings.desc': 'Đặt mục tiêu tiết kiệm, theo dõi tiến độ nạp tiền và xem tăng trưởng. Biến ước mơ thành cột mốc đạt được.',
      'features.challenges.title': 'Thử Thách Chi Tiêu',
      'features.challenges.desc': 'Tham gia thử thách chi tiêu, kiếm huy hiệu và duy trì chuỗi ngày để gamify hành trình tài chính.',
      'features.reports.title': 'Báo Cáo Tháng Thông Minh',
      'features.reports.desc': 'Nhận báo cáo hàng tháng tự động với xu hướng chi tiêu, phân tích danh mục và mẹo tiết kiệm cá nhân hóa.',
      'features.recurring.title': 'Chi Tiêu Định Kỳ',
      'features.recurring.desc': 'Thiết lập đăng ký, tiền thuê và hóa đơn dưới dạng giao dịch tự động. Không bao giờ bỏ lỡ thanh toán.',
      'features.security.title': 'Bảo Mật Sinh Trắc Học',
      'features.security.desc': 'Bảo vệ dữ liệu tài chính bằng Face ID, Touch ID hoặc mã PIN. Dữ liệu của bạn luôn riêng tư.',
      'features.cashback.title': 'Hoàn Tiền Thưởng',
      'features.cashback.desc': 'Kiếm hoàn tiền khi mua sắm trên Shopee qua chương trình affiliate. Mua sắm, kiếm tiền và rút — tất cả được theo dõi trong ứng dụng với số dư, thưởng chuỗi ngày và lịch sử đơn hàng.',
      'features.cashback.badge1': 'Thưởng Chuỗi Ngày',
      'features.cashback.badge2': 'Số Dư Thời Gian Thực',
      'features.cashback.badge3': 'Rút Tiền Dễ Dàng',
      'features.cashback.partner': 'qua Shopee',

      // How it works
      'how.tagline': 'Bắt Đầu Trong Vài Phút',
      'how.title': 'Cách Hoạt Động',
      'how.desc': 'Bốn bước đơn giản để quản lý tài chính rõ ràng — và kiếm hoàn tiền.',
      'how.step1.title': 'Tải Ứng Dụng',
      'how.step1.desc': 'Tải Money Mate miễn phí từ App Store hoặc Google Play. Thiết lập tài khoản trong vài giây.',
      'how.step2.title': 'Theo Dõi Chi Tiêu',
      'how.step2.desc': 'Thêm chi tiêu bằng gõ phím, giọng nói hoặc ảnh. Phân loại, gắn thẻ và chia sẻ dễ dàng.',
      'how.step3.title': 'Đặt Ngân Sách & Mục Tiêu',
      'how.step3.desc': 'Nhận thống kê thông minh, đặt ngân sách theo danh mục và tạo mục tiêu tiết kiệm.',
      'how.step4.title': 'Kiếm Hoàn Tiền',
      'how.step4.desc': 'Mua sắm Shopee qua Money Mate, kiếm hoàn tiền cho mỗi đơn hàng và rút số dư bất cứ lúc nào.',

      // Screenshots
      'screenshots.tagline': 'Xem Thực Tế',
      'screenshots.title': 'Thiết Kế Đẹp & Trực Quan',
      'screenshots.desc': 'Được thiết kế để quản lý tiền trở nên dễ dàng.',

      // Testimonials
      'stats.downloads': 'Lượt Tải',
      'stats.rating': 'Đánh Giá',
      'stats.languages': 'Ngôn Ngữ',
      'testimonials.tagline': 'Người Dùng Nói Gì',
      'testimonials.title': 'Được Yêu Thích Bởi Hàng Ngàn Người',
      'testimonials.1.text': '"Money Mate đã thay đổi hoàn toàn cách tôi quản lý tài chính. Tính năng chia chi phí nhóm rất hữu ích cho chi phí chung hàng tháng!"',
      'testimonials.1.name': 'Sarah A.',
      'testimonials.1.role': 'Nhà Thiết Kế Tự Do',
      'testimonials.2.text': '"Ứng dụng tài chính tốt nhất tôi từng dùng. Bảng phân tích cho tôi những thông tin chưa từng có. Cuối cùng cũng hiểu tiền đi đâu mỗi tháng."',
      'testimonials.2.name': 'Mike T.',
      'testimonials.2.role': 'Kỹ Sư Phần Mềm',
      'testimonials.3.text': '"Hỗ trợ tiếng Việt hoàn hảo! Tôi rất thích dùng để theo dõi chi tiêu trong các chuyến đi gia đình. Chế độ ngoại tuyến hoạt động rất tốt."',
      'testimonials.3.name': 'Linh N.',
      'testimonials.3.role': 'Blogger Du Lịch',

      // CTA
      'cta.tagline': 'Sẵn Sàng Bắt Đầu?',
      'cta.title': 'Bắt Đầu Theo Dõi<br>Tài Chính Ngay Hôm Nay',
      'cta.desc': 'Tải Money Mate miễn phí và thực hiện bước đầu tiên hướng tới sự rõ ràng tài chính.',
      'cta.qr': 'Quét để tải trên App Store',

      // Footer
      'footer.desc': 'Quản lý tài chính cá nhân đơn giản. Theo dõi, chia sẻ, ngân sách và hoàn tiền.',
      'footer.product': 'Sản Phẩm',
      'footer.company': 'Công Ty',
      'footer.legal': 'Pháp Lý',
      'footer.features': 'Tính Năng',
      'footer.how': 'Cách Hoạt Động',
      'footer.testimonials': 'Đánh Giá',
      'footer.download': 'Tải Về',
      'footer.contact': 'Liên Hệ',
      'footer.support': 'Hỗ Trợ',
      'footer.privacy': 'Chính Sách Bảo Mật',
      'footer.terms': 'Điều Khoản Dịch Vụ',
      'footer.copyright': '&copy; 2026 Code4change. Bảo lưu mọi quyền.',

      // Feature Showcase
      'showcase.tagline': 'Khám Phá Chi Tiết',
      'showcase.title': 'Tính Năng Nổi Bật',
      'showcase.budget.title': 'Quản Lý Ngân Sách',
      'showcase.budget.desc': 'Đặt ngân sách hàng tháng theo danh mục, xem thanh tiến độ trực quan và nhận cảnh báo thông minh trước khi chi tiêu quá mức. Kiểm soát mọi danh mục — từ ăn uống đến giải trí.',
      'showcase.cashback.title': 'Hoàn Tiền Thưởng',
      'showcase.cashback.desc': 'Mua sắm trên Shopee qua Moni và kiếm hoàn tiền cho mọi đơn hàng. Theo dõi số dư, thưởng chuỗi ngày và lịch sử đơn hàng — tất cả trong ứng dụng.',
      'showcase.group.title': 'Chi Tiêu Nhóm',
      'showcase.group.desc': 'Tạo nhóm cho chuyến đi, phòng trọ chung hoặc tiệc tùng. Thêm chi phí và Moni tự động tính ai nợ ai. Thanh toán chỉ với một chạm.',
      'showcase.security.title': 'Bảo Mật & Riêng Tư',
      'showcase.security.desc': 'Dữ liệu tài chính được bảo vệ bằng xác thực sinh trắc học (Face ID, Touch ID), mã hóa cục bộ và đồng bộ đám mây an toàn. Chúng tôi không bao giờ chia sẻ dữ liệu với bên thứ ba.',

      // Comparison
      'compare.tagline': 'Tại Sao Chọn Moni?',
      'compare.title': 'So Sánh Với Đối Thủ',
      'compare.feature': 'Tính Năng',
      'compare.price': 'Giá',
      'compare.group': 'Chia Tiền Nhóm',
      'compare.cashback': 'Hoàn Tiền',
      'compare.voice': 'Nhập Giọng Nói',
      'compare.offline': 'Ngoại Tuyến',
      'compare.analytics': 'Phân Tích',
      'compare.languages': 'Ngôn Ngữ',
      'compare.free': 'Miễn Phí',
      'compare.yes': 'Có',
      'compare.no': 'Không',
      'compare.moni.rec': 'Khuyên Dùng',

      // FAQ
      'faq.tagline': 'Câu Hỏi Thường Gặp?',
      'faq.title': 'Câu Hỏi Thường Gặp',
      'faq.q1': 'Moni có miễn phí không?',
      'faq.a1': 'Có, Moni hoàn toàn miễn phí để tải và sử dụng. Tất cả tính năng cốt lõi — theo dõi chi tiêu, ngân sách, chia tiền nhóm và phân tích — đều miễn phí. Các tính năng cao cấp có thể được thêm trong tương lai.',
      'faq.q2': 'Dữ liệu tài chính của tôi có an toàn không?',
      'faq.a2': 'Hoàn toàn. Chúng tôi sử dụng xác thực sinh trắc học (Face ID, Touch ID), mã hóa cục bộ AES-256 và đồng bộ đám mây an toàn qua TLS 1.3. Chúng tôi không bao giờ chia sẻ dữ liệu với bên thứ ba.',
      'faq.q3': 'Moni có hoạt động ngoại tuyến không?',
      'faq.a3': 'Có, Moni ưu tiên ngoại tuyến. Theo dõi chi tiêu không cần internet và dữ liệu tự động đồng bộ khi có kết nối.',
      'faq.q4': 'Những thiết bị nào được hỗ trợ?',
      'faq.a4': 'Moni hiện có sẵn cho iOS (iPhone). Phiên bản Android sẽ ra mắt sớm.',
      'faq.q5': 'Tôi có thể xuất dữ liệu không?',
      'faq.a5': 'Có, bạn có thể xuất dữ liệu chi tiêu cho mục đích cá nhân hoặc kế toán.',
      'faq.q6': 'Chia tiền nhóm hoạt động như thế nào?',
      'faq.a6': 'Tạo nhóm, thêm thành viên và ghi nhận chi phí chung. Moni tự động tính ai nợ ai. Thanh toán chỉ với một chạm.',
      'faq.q7': 'Hoàn tiền hoạt động như thế nào?',
      'faq.a7': 'Mua sắm Shopee qua liên kết của Moni, kiếm hoàn tiền cho mỗi đơn hàng và rút số dư bất cứ lúc nào.',

      // Email Signup
      'email.tagline': 'Cập Nhật Tin Tức',
      'email.title': 'Nhận Mẹo & Cập Nhật',
      'email.desc': 'Đăng ký nhận mẹo tài chính cá nhân và thông báo tính năng mới.',
      'email.btn': 'Đăng Ký',
      'email.success': 'Cảm ơn! Chúng tôi sẽ gửi cập nhật cho bạn.',
      'email.error': 'Vui lòng nhập địa chỉ email hợp lệ.',
    },
  };

  var currentLang = localStorage.getItem('mm-lang') || 'vi';

  function setLanguage(lang) {
    currentLang = lang;
    localStorage.setItem('mm-lang', lang);
    document.documentElement.lang = lang;

    document.querySelectorAll('[data-i18n]').forEach(function (el) {
      var key = el.getAttribute('data-i18n');
      var text = translations[lang][key];
      if (text) el.textContent = text;
    });

    document.querySelectorAll('[data-i18n-html]').forEach(function (el) {
      var key = el.getAttribute('data-i18n-html');
      var html = translations[lang][key];
      if (html) el.innerHTML = html;
    });

    // Update toggle buttons
    document.querySelectorAll('.lang-toggle').forEach(function (btn) {
      btn.textContent = lang === 'en' ? 'VI' : 'EN';
      btn.setAttribute('aria-label', lang === 'en' ? 'Chuyển sang Tiếng Việt' : 'Switch to English');
    });
  }

  // Initialize on DOM ready
  function init() {
    document.querySelectorAll('.lang-toggle').forEach(function (btn) {
      btn.addEventListener('click', function () {
        setLanguage(currentLang === 'en' ? 'vi' : 'en');
      });
    });

    // Always apply language on init
    setLanguage(currentLang);
    if (currentLang === 'vi') {
      document.querySelectorAll('.lang-toggle').forEach(function (btn) {
        btn.textContent = 'EN';
        btn.setAttribute('aria-label', 'Switch to English');
      });
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
