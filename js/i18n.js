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
    },
  };

  var currentLang = localStorage.getItem('mm-lang') || 'en';

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

    if (currentLang !== 'en') {
      setLanguage(currentLang);
    } else {
      // Set initial toggle text
      document.querySelectorAll('.lang-toggle').forEach(function (btn) {
        btn.textContent = 'VI';
        btn.setAttribute('aria-label', 'Chuyển sang Tiếng Việt');
      });
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
