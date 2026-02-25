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
      'hero.desc': 'Track expenses, split costs with friends, manage budgets, and earn cashback rewards — all in one beautiful app.',
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
      'features.desc': 'From daily expense tracking to group splitting — Money Mate has you covered.',
      'features.expense.title': 'Expense Tracking',
      'features.expense.desc': 'Log expenses instantly with categories, notes, and receipt photos. See where every dollar goes.',
      'features.sharing.title': 'Expense Sharing & Groups',
      'features.sharing.desc': 'Split bills with friends, track group expenses, and settle debts easily. Perfect for trips and shared living.',
      'features.budget.title': 'Budget Management',
      'features.budget.desc': 'Set monthly budgets by category, get smart alerts before overspending, and stay on track.',
      'features.analytics.title': 'Analytics Dashboard',
      'features.analytics.desc': 'Beautiful charts and insights to understand your spending patterns and make smarter decisions.',
      'features.language.title': '10 Languages Supported',
      'features.language.desc': 'Use Money Mate in your preferred language. English, Vietnamese, Spanish, French, and more.',
      'features.sync.title': 'Cloud Sync & Offline-first',
      'features.sync.desc': 'Your data syncs across devices automatically. Works offline too — never miss tracking an expense.',
      'features.cashback.title': 'Cashback Rewards',
      'features.cashback.desc': 'Earn cashback on everyday purchases through our affiliate partners. Shop smarter and get rewarded for the spending you already do.',

      // How it works
      'how.tagline': 'Get Started in Minutes',
      'how.title': 'How It Works',
      'how.desc': 'Three simple steps to financial clarity.',
      'how.step1.title': 'Download the App',
      'how.step1.desc': 'Get Money Mate free from the App Store or Google Play. Set up your account in seconds.',
      'how.step2.title': 'Track Your Expenses',
      'how.step2.desc': 'Add expenses with one tap. Categorize, tag, and split with friends effortlessly.',
      'how.step3.title': 'Manage Your Budget',
      'how.step3.desc': 'See insights, set budgets, and take control of your financial future with confidence.',

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
      'hero.desc': 'Theo dõi chi tiêu, chia sẻ chi phí với bạn bè, quản lý ngân sách và nhận hoàn tiền — tất cả trong một ứng dụng.',
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
      'features.desc': 'Từ theo dõi chi tiêu hàng ngày đến chia sẻ nhóm — Money Mate luôn đồng hành cùng bạn.',
      'features.expense.title': 'Theo Dõi Chi Tiêu',
      'features.expense.desc': 'Ghi nhận chi tiêu ngay lập tức với danh mục, ghi chú và ảnh hóa đơn. Biết rõ từng đồng đi đâu.',
      'features.sharing.title': 'Chia Sẻ Chi Phí & Nhóm',
      'features.sharing.desc': 'Chia hóa đơn với bạn bè, theo dõi chi phí nhóm và thanh toán nợ dễ dàng. Hoàn hảo cho các chuyến đi và ở chung.',
      'features.budget.title': 'Quản Lý Ngân Sách',
      'features.budget.desc': 'Đặt ngân sách hàng tháng theo danh mục, nhận cảnh báo thông minh trước khi chi tiêu quá mức.',
      'features.analytics.title': 'Bảng Phân Tích',
      'features.analytics.desc': 'Biểu đồ đẹp mắt và thông tin chi tiết giúp bạn hiểu rõ thói quen chi tiêu và đưa ra quyết định thông minh hơn.',
      'features.language.title': 'Hỗ Trợ 10 Ngôn Ngữ',
      'features.language.desc': 'Sử dụng Money Mate bằng ngôn ngữ yêu thích. Tiếng Anh, Tiếng Việt, Tiếng Tây Ban Nha, Tiếng Pháp và nhiều hơn nữa.',
      'features.sync.title': 'Đồng Bộ & Ngoại Tuyến',
      'features.sync.desc': 'Dữ liệu tự động đồng bộ trên các thiết bị. Hoạt động ngoại tuyến — không bao giờ bỏ lỡ ghi nhận chi tiêu.',
      'features.cashback.title': 'Hoàn Tiền Thưởng',
      'features.cashback.desc': 'Nhận hoàn tiền từ các giao dịch hàng ngày qua đối tác liên kết. Mua sắm thông minh hơn và được thưởng.',

      // How it works
      'how.tagline': 'Bắt Đầu Trong Vài Phút',
      'how.title': 'Cách Hoạt Động',
      'how.desc': 'Ba bước đơn giản để quản lý tài chính rõ ràng.',
      'how.step1.title': 'Tải Ứng Dụng',
      'how.step1.desc': 'Tải Money Mate miễn phí từ App Store hoặc Google Play. Thiết lập tài khoản trong vài giây.',
      'how.step2.title': 'Theo Dõi Chi Tiêu',
      'how.step2.desc': 'Thêm chi tiêu chỉ với một chạm. Phân loại, gắn thẻ và chia sẻ với bạn bè dễ dàng.',
      'how.step3.title': 'Quản Lý Ngân Sách',
      'how.step3.desc': 'Xem thống kê, đặt ngân sách và kiểm soát tương lai tài chính với sự tự tin.',

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
