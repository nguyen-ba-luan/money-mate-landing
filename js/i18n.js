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
      'nav.download': 'Download Free',

      // Hero
      'hero.tagline': '100% Free \u00B7 No Ads \u00B7 No Hidden Costs',
      'hero.title': 'Stop Wondering Where<br><span class="text-gold">Your Money Went</span>',
      'hero.desc': 'Track spending by voice, split costs with friends, and earn Shopee cashback \u2014 the only free finance app you\'ll ever need.',
      'hero.badge.appstore.top': 'Download on the',
      'hero.badge.appstore.bottom': 'App Store',
      'hero.badge.google.top': 'COMING SOON',
      'hero.badge.google.bottom': 'Google Play',
      'hero.bullet1': 'Track by voice, photo, or typing',
      'hero.bullet2': 'Split costs with friends instantly',
      'hero.bullet3': 'Earn real cashback on Shopee',
      'hero.trust.rating': '4.8 App Store Rating',
      'hero.trust.secure': 'Secure & Private',
      'hero.trust.users': '5,000+ Users',
      'sticky.subtitle': 'Free Finance App',
      'sticky.btn': 'Download Free',

      // Stats bar
      'stats.downloads': 'Downloads',
      'stats.rating': 'App Store Rating',
      'stats.languages': 'Languages',
      'stats.price': 'Forever Free',

      // Problem awareness
      'problem.tagline': 'Sound Familiar?',
      'problem.title': 'Managing Money Shouldn\'t Be This Hard',
      'problem.pain1.title': 'Where did it all go?',
      'problem.pain1.desc': 'You check your balance and can\'t explain where half your salary went this month.',
      'problem.pain2.title': 'Splitting bills is awkward',
      'problem.pain2.desc': 'Group dinners and trips turn into math nightmares. Someone always forgets to pay back.',
      'problem.pain3.title': 'Budgeting apps cost too much',
      'problem.pain3.desc': 'The best finance apps charge $10\u201315/month. Others are free but limited or full of ads.',

      // Solution / Key Features
      'solution.tagline': 'Moni Fixes This',
      'solution.title': 'One App for <span class="text-gold">Everything</span>',
      'solution.desc': 'Track, split, budget, analyze, and earn cashback \u2014 completely free, forever.',
      'solution.f1.badge': 'Core Feature',
      'solution.f1.title': 'Track Every Dong in Seconds',
      'solution.f1.desc': 'Add expenses by typing, voice command, or snapping a receipt photo. Moni auto-categorizes everything so you always know where your money goes.',
      'solution.f1.tag1': 'Voice Input',
      'solution.f1.tag2': 'Photo Receipts',
      'solution.f1.tag3': 'Auto Categories',
      'solution.f2.badge': 'Social Feature',
      'solution.f2.title': 'Split Costs Without the Awkwardness',
      'solution.f2.desc': 'Create groups for trips, shared apartments, or dinner parties. Add expenses and Moni automatically calculates who owes whom. No more mental math or forgotten debts.',
      'solution.f2.tag1': 'Unlimited Groups',
      'solution.f2.tag2': 'Auto Calculate',
      'solution.f2.tag3': 'Share via Link',
      'solution.f3.badge': 'Unique to Moni',
      'solution.f3.title': 'Earn Cashback While You Shop',
      'solution.f3.desc': 'Shop on Shopee through Moni and earn cashback on every purchase. Track your balance, build streak rewards, and withdraw anytime. No other finance app does this.',
      'solution.f3.tag1': 'Streak Rewards',
      'solution.f3.tag2': 'Real Withdrawals',
      'solution.f3.tag3': 'via Shopee',

      // More features grid
      'more.tagline': 'And Much More',
      'more.title': 'Everything Else You Need',
      'features.budget.title': 'Budget Management',
      'features.budget.desc': 'Set monthly budgets by category. Get alerts before you overspend.',
      'features.analytics.title': 'Analytics Dashboard',
      'features.analytics.desc': 'Beautiful charts and insights to understand your spending patterns.',
      'features.savings.title': 'Savings Goals',
      'features.savings.desc': 'Set targets, track deposits, and turn dreams into achievable milestones.',
      'features.couple.title': 'Couple Finance',
      'features.couple.desc': 'Manage money together with your partner. Shared view, joint tracking.',
      'features.recurring.title': 'Recurring Transactions',
      'features.recurring.desc': 'Auto-track rent, subscriptions, and bills. Never miss a recurring expense.',
      'features.challenges.title': 'Savings Challenges',
      'features.challenges.desc': 'Fun challenges to build better saving habits and reach goals faster.',

      // Inline CTA
      'inline-cta.title': 'Ready to take control?',
      'inline-cta.desc': 'Join 5,000+ users who finally understand where their money goes.',
      'inline-cta.btn': 'Download Free on App Store',

      // How it works
      'how.tagline': 'Get Started in Minutes',
      'how.title': 'How It Works',
      'how.desc': 'Three simple steps to financial clarity.',
      'how.step1.title': 'Download Moni',
      'how.step1.desc': 'Free from the App Store. Set up your account in 30 seconds.',
      'how.step2.title': 'Track & Split',
      'how.step2.desc': 'Add expenses by typing, voice, or photo. Split with friends in groups.',
      'how.step3.title': 'See Insights & Earn',
      'how.step3.desc': 'Get analytics, set budgets, reach savings goals, and earn Shopee cashback.',

      // Screenshots
      'screenshots.tagline': 'See It In Action',
      'screenshots.title': 'Beautiful & Intuitive Design',
      'screenshots.desc': 'Designed to make managing money feel effortless.',

      // Comparison
      'compare.tagline': 'Why Moni?',
      'compare.title': 'The Only Free App That Does It All',
      'compare.feature': 'Feature',
      'compare.price': 'Price',
      'compare.group': 'Group Splitting',
      'compare.cashback': 'Cashback Rewards',
      'compare.voice': 'Voice Input',
      'compare.offline': 'Offline Mode',
      'compare.analytics': 'Analytics',
      'compare.couple': 'Couple Finance',
      'compare.recurring': 'Recurring Tracking',
      'compare.languages': 'Languages',
      'compare.free': 'Free',
      'compare.yes': 'Yes',
      'compare.no': 'No',
      'compare.moni.rec': 'Recommended',

      // Testimonials
      'testimonials.tagline': 'What Users Say',
      'testimonials.title': 'Loved by Thousands',
      'testimonials.1.text': '"Moni completely changed how I manage my finances. The group expense splitting is a lifesaver for our monthly apartment costs!"',
      'testimonials.1.name': 'Sarah A.',
      'testimonials.1.role': 'Freelance Designer',
      'testimonials.2.text': '"Best finance app I\'ve used. The analytics dashboard gives me insights I never had before. Finally understand where my money goes each month."',
      'testimonials.2.name': 'Mike T.',
      'testimonials.2.role': 'Software Engineer',
      'testimonials.3.text': '"The Vietnamese language support is perfect! I love using it to track expenses during our family trips. The offline mode works flawlessly."',
      'testimonials.3.name': 'Linh N.',
      'testimonials.3.role': 'Travel Blogger',

      // FAQ
      'faq.tagline': 'Got Questions?',
      'faq.title': 'Frequently Asked Questions',
      'faq.q1': 'Is Moni free to use?',
      'faq.a1': 'Yes, Moni is completely free to download and use. All core features \u2014 expense tracking, budgets, group splitting, and analytics \u2014 are free. Premium features may be added in the future.',
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

      // CTA
      'cta.tagline': 'Ready to Get Started?',
      'cta.title': 'Your Money Deserves<br>Better Than Guesswork',
      'cta.desc': 'Download Moni for free and take the first step toward financial clarity.',
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
      'nav.features': 'T\u00EDnh N\u0103ng',
      'nav.how': 'C\u00E1ch Ho\u1EA1t \u0110\u1ED9ng',
      'nav.testimonials': '\u0110\u00E1nh Gi\u00E1',
      'nav.download': 'T\u1EA3i Mi\u1EC5n Ph\u00ED',

      // Hero
      'hero.tagline': 'Mi\u1EC5n ph\u00ED 100% \u00B7 Kh\u00F4ng qu\u1EA3ng c\u00E1o \u00B7 Kh\u00F4ng ph\u00ED \u1EA9n',
      'hero.title': 'H\u1EBFt Th\u1EAFc M\u1EAFc<br><span class="text-gold">Ti\u1EC1n \u0110i \u0110\u00E2u</span>',
      'hero.desc': 'Theo d\u00F5i chi ti\u00EAu b\u1EB1ng gi\u1ECDng n\u00F3i, chia chi ph\u00ED v\u1EDBi b\u1EA1n b\u00E8, v\u00E0 ki\u1EBFm ho\u00E0n ti\u1EC1n Shopee \u2014 \u1EE9ng d\u1EE5ng t\u00E0i ch\u00EDnh mi\u1EC5n ph\u00ED duy nh\u1EA5t b\u1EA1n c\u1EA7n.',
      'hero.badge.appstore.top': 'T\u1EA3i v\u1EC1 tr\u00EAn',
      'hero.badge.appstore.bottom': 'App Store',
      'hero.badge.google.top': 'S\u1EAEP RA M\u1EAET',
      'hero.badge.google.bottom': 'Google Play',
      'hero.bullet1': 'Ghi nh\u1EADn b\u1EB1ng gi\u1ECDng n\u00F3i, \u1EA3nh, ho\u1EB7c g\u00F5 ph\u00EDm',
      'hero.bullet2': 'Chia ti\u1EC1n v\u1EDBi b\u1EA1n b\u00E8 ngay l\u1EADp t\u1EE9c',
      'hero.bullet3': 'Ki\u1EBFm ho\u00E0n ti\u1EC1n th\u1EADt tr\u00EAn Shopee',
      'hero.trust.rating': '\u0110\u00E1nh gi\u00E1 4.8 App Store',
      'hero.trust.secure': 'B\u1EA3o M\u1EADt & Ri\u00EAng T\u01B0',
      'hero.trust.users': '5.000+ Ng\u01B0\u1EDDi D\u00F9ng',
      'sticky.subtitle': 'App T\u00E0i Ch\u00EDnh Mi\u1EC5n Ph\u00ED',
      'sticky.btn': 'T\u1EA3i Mi\u1EC5n Ph\u00ED',

      // Stats bar
      'stats.downloads': 'L\u01B0\u1EE3t T\u1EA3i',
      'stats.rating': '\u0110\u00E1nh Gi\u00E1 App Store',
      'stats.languages': 'Ng\u00F4n Ng\u1EEF',
      'stats.price': 'Mi\u1EC5n Ph\u00ED M\u00E3i M\u00E3i',

      // Problem awareness
      'problem.tagline': 'Nghe Quen Kh\u00F4ng?',
      'problem.title': 'Qu\u1EA3n L\u00FD Ti\u1EC1n Kh\u00F4ng N\u00EAn Kh\u00F3 Nh\u01B0 V\u1EADy',
      'problem.pain1.title': 'Ti\u1EC1n \u0111i \u0111\u00E2u h\u1EBFt r\u1ED3i?',
      'problem.pain1.desc': 'B\u1EA1n ki\u1EC3m tra s\u1ED1 d\u01B0 v\u00E0 kh\u00F4ng hi\u1EC3u n\u1EEDa l\u01B0\u01A1ng \u0111\u00E3 bi\u1EBFn m\u1EA5t \u0111i \u0111\u00E2u trong th\u00E1ng n\u00E0y.',
      'problem.pain2.title': 'Chia ti\u1EC1n th\u1EADt phi\u1EC1n',
      'problem.pain2.desc': '\u0102n nh\u00F3m hay \u0111i ch\u01A1i chung bi\u1EBFn th\u00E0nh b\u00E0i to\u00E1n \u0111au \u0111\u1EA7u. Ai \u0111\u00F3 lu\u00F4n qu\u00EAn tr\u1EA3 l\u1EA1i.',
      'problem.pain3.title': '\u1EE8ng d\u1EE5ng qu\u00E1 \u0111\u1EAFt',
      'problem.pain3.desc': 'Nh\u1EEFng app t\u00E0i ch\u00EDnh t\u1ED1t nh\u1EA5t t\u00EDnh 250\u2013350k/th\u00E1ng. App mi\u1EC5n ph\u00ED th\u00EC h\u1EA1n ch\u1EBF ho\u1EB7c nhi\u1EC1u qu\u1EA3ng c\u00E1o.',

      // Solution / Key Features
      'solution.tagline': 'Moni Gi\u1EA3i Quy\u1EBFt T\u1EA5t C\u1EA3',
      'solution.title': 'M\u1ED9t \u1EE8ng D\u1EE5ng Cho <span class="text-gold">M\u1ECDi Th\u1EE9</span>',
      'solution.desc': 'Theo d\u00F5i, chia ti\u1EC1n, ng\u00E2n s\u00E1ch, ph\u00E2n t\u00EDch v\u00E0 ho\u00E0n ti\u1EC1n \u2014 mi\u1EC5n ph\u00ED ho\u00E0n to\u00E0n, m\u00E3i m\u00E3i.',
      'solution.f1.badge': 'T\u00EDnh N\u0103ng Ch\u00EDnh',
      'solution.f1.title': 'Ghi Nh\u1EADn T\u1EEBng \u0110\u1ED3ng Trong V\u00E0i Gi\u00E2y',
      'solution.f1.desc': 'Th\u00EAm chi ti\u00EAu b\u1EB1ng g\u00F5 ph\u00EDm, gi\u1ECDng n\u00F3i ho\u1EB7c ch\u1EE5p \u1EA3nh h\u00F3a \u0111\u01A1n. Moni t\u1EF1 \u0111\u1ED9ng ph\u00E2n lo\u1EA1i \u0111\u1EC3 b\u1EA1n lu\u00F4n bi\u1EBFt ti\u1EC1n \u0111i \u0111\u00E2u.',
      'solution.f1.tag1': 'Nh\u1EADp Gi\u1ECDng N\u00F3i',
      'solution.f1.tag2': 'Ch\u1EE5p H\u00F3a \u0110\u01A1n',
      'solution.f1.tag3': 'T\u1EF1 \u0110\u1ED9ng Ph\u00E2n Lo\u1EA1i',
      'solution.f2.badge': 'T\u00EDnh N\u0103ng X\u00E3 H\u1ED9i',
      'solution.f2.title': 'Chia Ti\u1EC1n Kh\u00F4ng C\u00F2n Ng\u1EA1i Ng\u00F9ng',
      'solution.f2.desc': 'T\u1EA1o nh\u00F3m cho chuy\u1EBFn \u0111i, ph\u00F2ng tr\u1ECDng chung hay ti\u1EC7c t\u00F9ng. Th\u00EAm chi ph\u00ED v\u00E0 Moni t\u1EF1 \u0111\u1ED9ng t\u00EDnh ai n\u1EE3 ai. Kh\u00F4ng c\u1EA7n t\u00EDnh nh\u1EA9m.',
      'solution.f2.tag1': 'Nh\u00F3m Kh\u00F4ng Gi\u1EDBi H\u1EA1n',
      'solution.f2.tag2': 'T\u1EF1 \u0110\u1ED9ng T\u00EDnh',
      'solution.f2.tag3': 'Chia S\u1EBB Qua Link',
      'solution.f3.badge': 'Ch\u1EC9 C\u00F3 \u1EDE Moni',
      'solution.f3.title': 'Ki\u1EBFm Ho\u00E0n Ti\u1EC1n Khi Mua S\u1EAFm',
      'solution.f3.desc': 'Mua s\u1EAFm tr\u00EAn Shopee qua Moni v\u00E0 ki\u1EBFm ho\u00E0n ti\u1EC1n m\u1ED7i \u0111\u01A1n h\u00E0ng. Theo d\u00F5i s\u1ED1 d\u01B0, th\u01B0\u1EDFng chu\u1ED7i ng\u00E0y, r\u00FAt ti\u1EC1n b\u1EA5t c\u1EE9 l\u00FAc n\u00E0o.',
      'solution.f3.tag1': 'Th\u01B0\u1EDFng Chu\u1ED7i Ng\u00E0y',
      'solution.f3.tag2': 'R\u00FAt Ti\u1EC1n Th\u1EADt',
      'solution.f3.tag3': 'qua Shopee',

      // More features grid
      'more.tagline': 'V\u00E0 Nhi\u1EC1u H\u01A1n',
      'more.title': 'M\u1ECDi Th\u1EE9 Kh\u00E1c B\u1EA1n C\u1EA7n',
      'features.budget.title': 'Qu\u1EA3n L\u00FD Ng\u00E2n S\u00E1ch',
      'features.budget.desc': '\u0110\u1EB7t ng\u00E2n s\u00E1ch theo danh m\u1EE5c. Nh\u1EADn c\u1EA3nh b\u00E1o khi s\u1EAFp v\u01B0\u1EE3t m\u1EE9c.',
      'features.analytics.title': 'B\u1EA3ng Ph\u00E2n T\u00EDch',
      'features.analytics.desc': 'Bi\u1EC3u \u0111\u1ED3 \u0111\u1EB9p v\u00E0 th\u00F4ng tin chi ti\u1EBFt v\u1EC1 xu h\u01B0\u1EDBng chi ti\u00EAu.',
      'features.savings.title': 'M\u1EE5c Ti\u00EAu Ti\u1EBFt Ki\u1EC7m',
      'features.savings.desc': '\u0110\u1EB7t m\u1EE5c ti\u00EAu, theo d\u00F5i ti\u1EBFn \u0111\u1ED9 v\u00E0 bi\u1EBFn \u01B0\u1EDBc m\u01A1 th\u00E0nh hi\u1EC7n th\u1EF1c.',
      'features.couple.title': 'T\u00E0i Ch\u00EDnh C\u1EB7p \u0110\u00F4i',
      'features.couple.desc': 'Qu\u1EA3n l\u00FD ti\u1EC1n c\u00F9ng ng\u01B0\u1EDDi y\u00EAu. Xem chung, theo d\u00F5i chung.',
      'features.recurring.title': 'Giao D\u1ECBch \u0110\u1ECBnh K\u1EF3',
      'features.recurring.desc': 'T\u1EF1 \u0111\u1ED9ng ghi nh\u1EADn ti\u1EC1n nh\u00E0, g\u00F3i d\u1ECBch v\u1EE5, h\u00F3a \u0111\u01A1n h\u00E0ng th\u00E1ng.',
      'features.challenges.title': 'Th\u00E1ch Th\u1EE9c Ti\u1EBFt Ki\u1EC7m',
      'features.challenges.desc': 'Th\u00E1ch th\u1EE9c vui \u0111\u1EC3 x\u00E2y d\u1EF1ng th\u00F3i quen ti\u1EBFt ki\u1EC7m v\u00E0 \u0111\u1EA1t m\u1EE5c ti\u00EAu nhanh h\u01A1n.',

      // Inline CTA
      'inline-cta.title': 'S\u1EB5n s\u00E0ng ki\u1EC3m so\u00E1t?',
      'inline-cta.desc': 'Tham gia c\u00F9ng 5.000+ ng\u01B0\u1EDDi d\u00F9ng \u0111\u00E3 hi\u1EC3u r\u00F5 ti\u1EC1n \u0111i \u0111\u00E2u.',
      'inline-cta.btn': 'T\u1EA3i Mi\u1EC5n Ph\u00ED Tr\u00EAn App Store',

      // How it works
      'how.tagline': 'B\u1EAFt \u0110\u1EA7u Trong V\u00E0i Ph\u00FAt',
      'how.title': 'C\u00E1ch Ho\u1EA1t \u0110\u1ED9ng',
      'how.desc': 'Ba b\u01B0\u1EDBc \u0111\u01A1n gi\u1EA3n \u0111\u1EC3 qu\u1EA3n l\u00FD t\u00E0i ch\u00EDnh r\u00F5 r\u00E0ng.',
      'how.step1.title': 'T\u1EA3i Moni',
      'how.step1.desc': 'Mi\u1EC5n ph\u00ED tr\u00EAn App Store. Thi\u1EBFt l\u1EADp t\u00E0i kho\u1EA3n trong 30 gi\u00E2y.',
      'how.step2.title': 'Theo D\u00F5i & Chia Ti\u1EC1n',
      'how.step2.desc': 'Th\u00EAm chi ti\u00EAu b\u1EB1ng g\u00F5 ph\u00EDm, gi\u1ECDng n\u00F3i ho\u1EB7c \u1EA3nh. Chia ti\u1EC1n v\u1EDBi b\u1EA1n b\u00E8 trong nh\u00F3m.',
      'how.step3.title': 'Xem Th\u1ED1ng K\u00EA & Ki\u1EBFm Ti\u1EC1n',
      'how.step3.desc': 'Xem ph\u00E2n t\u00EDch, \u0111\u1EB7t ng\u00E2n s\u00E1ch, \u0111\u1EA1t m\u1EE5c ti\u00EAu v\u00E0 ki\u1EBFm ho\u00E0n ti\u1EC1n Shopee.',

      // Screenshots
      'screenshots.tagline': 'Xem Th\u1EF1c T\u1EBF',
      'screenshots.title': 'Thi\u1EBFt K\u1EBF \u0110\u1EB9p & Tr\u1EF1c Quan',
      'screenshots.desc': '\u0110\u01B0\u1EE3c thi\u1EBFt k\u1EBF \u0111\u1EC3 qu\u1EA3n l\u00FD ti\u1EC1n tr\u1EDF n\u00EAn d\u1EC5 d\u00E0ng.',

      // Comparison
      'compare.tagline': 'T\u1EA1i Sao Ch\u1ECDn Moni?',
      'compare.title': '\u1EE8ng D\u1EE5ng Mi\u1EC5n Ph\u00ED Duy Nh\u1EA5t L\u00E0m \u0110\u01B0\u1EE3c T\u1EA5t C\u1EA3',
      'compare.feature': 'T\u00EDnh N\u0103ng',
      'compare.price': 'Gi\u00E1',
      'compare.group': 'Chia Ti\u1EC1n Nh\u00F3m',
      'compare.cashback': 'Ho\u00E0n Ti\u1EC1n',
      'compare.voice': 'Nh\u1EADp Gi\u1ECDng N\u00F3i',
      'compare.offline': 'Ngo\u1EA1i Tuy\u1EBFn',
      'compare.analytics': 'Ph\u00E2n T\u00EDch',
      'compare.couple': 'T\u00E0i Ch\u00EDnh C\u1EB7p \u0110\u00F4i',
      'compare.recurring': 'Giao D\u1ECBch \u0110\u1ECBnh K\u1EF3',
      'compare.languages': 'Ng\u00F4n Ng\u1EEF',
      'compare.free': 'Mi\u1EC5n Ph\u00ED',
      'compare.yes': 'C\u00F3',
      'compare.no': 'Kh\u00F4ng',
      'compare.moni.rec': 'Khuy\u00EAn D\u00F9ng',

      // Testimonials
      'testimonials.tagline': 'Ng\u01B0\u1EDDi D\u00F9ng N\u00F3i G\u00EC',
      'testimonials.title': '\u0110\u01B0\u1EE3c Y\u00EAu Th\u00EDch B\u1EDFi H\u00E0ng Ng\u00E0n Ng\u01B0\u1EDDi',
      'testimonials.1.text': '"Moni \u0111\u00E3 thay \u0111\u1ED5i ho\u00E0n to\u00E0n c\u00E1ch t\u00F4i qu\u1EA3n l\u00FD t\u00E0i ch\u00EDnh. T\u00EDnh n\u0103ng chia chi ph\u00ED nh\u00F3m r\u1EA5t h\u1EEFu \u00EDch cho chi ph\u00ED chung h\u00E0ng th\u00E1ng!"',
      'testimonials.1.name': 'Sarah A.',
      'testimonials.1.role': 'Nh\u00E0 Thi\u1EBFt K\u1EBF T\u1EF1 Do',
      'testimonials.2.text': '"\u1EE8ng d\u1EE5ng t\u00E0i ch\u00EDnh t\u1ED1t nh\u1EA5t t\u00F4i t\u1EEBng d\u00F9ng. B\u1EA3ng ph\u00E2n t\u00EDch cho t\u00F4i nh\u1EEFng th\u00F4ng tin ch\u01B0a t\u1EEBng c\u00F3. Cu\u1ED1i c\u00F9ng c\u0169ng hi\u1EC3u ti\u1EC1n \u0111i \u0111\u00E2u m\u1ED7i th\u00E1ng."',
      'testimonials.2.name': 'Mike T.',
      'testimonials.2.role': 'K\u1EF9 S\u01B0 Ph\u1EA7n M\u1EC1m',
      'testimonials.3.text': '"H\u1ED7 tr\u1EE3 ti\u1EBFng Vi\u1EC7t ho\u00E0n h\u1EA3o! T\u00F4i r\u1EA5t th\u00EDch d\u00F9ng \u0111\u1EC3 theo d\u00F5i chi ti\u00EAu trong c\u00E1c chuy\u1EBFn \u0111i gia \u0111\u00ECnh. Ch\u1EBF \u0111\u1ED9 ngo\u1EA1i tuy\u1EBFn ho\u1EA1t \u0111\u1ED9ng r\u1EA5t t\u1ED1t."',
      'testimonials.3.name': 'Linh N.',
      'testimonials.3.role': 'Blogger Du L\u1ECBch',

      // FAQ
      'faq.tagline': 'C\u00E2u H\u1ECFi Th\u01B0\u1EDDng G\u1EB7p?',
      'faq.title': 'C\u00E2u H\u1ECFi Th\u01B0\u1EDDng G\u1EB7p',
      'faq.q1': 'Moni c\u00F3 mi\u1EC5n ph\u00ED kh\u00F4ng?',
      'faq.a1': 'C\u00F3, Moni ho\u00E0n to\u00E0n mi\u1EC5n ph\u00ED \u0111\u1EC3 t\u1EA3i v\u00E0 s\u1EED d\u1EE5ng. T\u1EA5t c\u1EA3 t\u00EDnh n\u0103ng c\u1ED1t l\u00F5i \u2014 theo d\u00F5i chi ti\u00EAu, ng\u00E2n s\u00E1ch, chia ti\u1EC1n nh\u00F3m v\u00E0 ph\u00E2n t\u00EDch \u2014 \u0111\u1EC1u mi\u1EC5n ph\u00ED.',
      'faq.q2': 'D\u1EEF li\u1EC7u t\u00E0i ch\u00EDnh c\u1EE7a t\u00F4i c\u00F3 an to\u00E0n kh\u00F4ng?',
      'faq.a2': 'Ho\u00E0n to\u00E0n. Ch\u00FAng t\u00F4i s\u1EED d\u1EE5ng x\u00E1c th\u1EF1c sinh tr\u1EAFc h\u1ECDc (Face ID, Touch ID), m\u00E3 h\u00F3a c\u1EE5c b\u1ED9 AES-256 v\u00E0 \u0111\u1ED3ng b\u1ED9 \u0111\u00E1m m\u00E2y an to\u00E0n qua TLS 1.3.',
      'faq.q3': 'Moni c\u00F3 ho\u1EA1t \u0111\u1ED9ng ngo\u1EA1i tuy\u1EBFn kh\u00F4ng?',
      'faq.a3': 'C\u00F3, Moni \u01B0u ti\u00EAn ngo\u1EA1i tuy\u1EBFn. Theo d\u00F5i chi ti\u00EAu kh\u00F4ng c\u1EA7n internet v\u00E0 d\u1EEF li\u1EC7u t\u1EF1 \u0111\u1ED9ng \u0111\u1ED3ng b\u1ED9 khi c\u00F3 k\u1EBFt n\u1ED1i.',
      'faq.q4': 'Nh\u1EEFng thi\u1EBFt b\u1ECB n\u00E0o \u0111\u01B0\u1EE3c h\u1ED7 tr\u1EE3?',
      'faq.a4': 'Moni hi\u1EC7n c\u00F3 s\u1EB5n cho iOS (iPhone). Phi\u00EAn b\u1EA3n Android s\u1EBD ra m\u1EAFt s\u1EDBm.',
      'faq.q5': 'T\u00F4i c\u00F3 th\u1EC3 xu\u1EA5t d\u1EEF li\u1EC7u kh\u00F4ng?',
      'faq.a5': 'C\u00F3, b\u1EA1n c\u00F3 th\u1EC3 xu\u1EA5t d\u1EEF li\u1EC7u chi ti\u00EAu cho m\u1EE5c \u0111\u00EDch c\u00E1 nh\u00E2n ho\u1EB7c k\u1EBF to\u00E1n.',
      'faq.q6': 'Chia ti\u1EC1n nh\u00F3m ho\u1EA1t \u0111\u1ED9ng nh\u01B0 th\u1EBF n\u00E0o?',
      'faq.a6': 'T\u1EA1o nh\u00F3m, th\u00EAm th\u00E0nh vi\u00EAn v\u00E0 ghi nh\u1EADn chi ph\u00ED chung. Moni t\u1EF1 \u0111\u1ED9ng t\u00EDnh ai n\u1EE3 ai. Thanh to\u00E1n ch\u1EC9 v\u1EDBi m\u1ED9t ch\u1EA1m.',
      'faq.q7': 'Ho\u00E0n ti\u1EC1n ho\u1EA1t \u0111\u1ED9ng nh\u01B0 th\u1EBF n\u00E0o?',
      'faq.a7': 'Mua s\u1EAFm Shopee qua li\u00EAn k\u1EBFt c\u1EE7a Moni, ki\u1EBFm ho\u00E0n ti\u1EC1n cho m\u1ED7i \u0111\u01A1n h\u00E0ng v\u00E0 r\u00FAt s\u1ED1 d\u01B0 b\u1EA5t c\u1EE9 l\u00FAc n\u00E0o.',

      // CTA
      'cta.tagline': 'S\u1EB5n S\u00E0ng B\u1EAFt \u0110\u1EA7u?',
      'cta.title': 'Ti\u1EC1n C\u1EE7a B\u1EA1n X\u1EE9ng \u0110\u00E1ng<br>\u0110\u01B0\u1EE3c Qu\u1EA3n L\u00FD T\u1ED1t H\u01A1n',
      'cta.desc': 'T\u1EA3i Moni mi\u1EC5n ph\u00ED v\u00E0 th\u1EF1c hi\u1EC7n b\u01B0\u1EDBc \u0111\u1EA7u ti\u00EAn h\u01B0\u1EDBng t\u1EDBi s\u1EF1 r\u00F5 r\u00E0ng t\u00E0i ch\u00EDnh.',
      'cta.qr': 'Qu\u00E9t \u0111\u1EC3 t\u1EA3i tr\u00EAn App Store',

      // Footer
      'footer.desc': 'Qu\u1EA3n l\u00FD t\u00E0i ch\u00EDnh c\u00E1 nh\u00E2n \u0111\u01A1n gi\u1EA3n. Theo d\u00F5i, chia s\u1EBB, ng\u00E2n s\u00E1ch v\u00E0 ho\u00E0n ti\u1EC1n.',
      'footer.product': 'S\u1EA3n Ph\u1EA9m',
      'footer.company': 'C\u00F4ng Ty',
      'footer.legal': 'Ph\u00E1p L\u00FD',
      'footer.features': 'T\u00EDnh N\u0103ng',
      'footer.how': 'C\u00E1ch Ho\u1EA1t \u0110\u1ED9ng',
      'footer.testimonials': '\u0110\u00E1nh Gi\u00E1',
      'footer.download': 'T\u1EA3i V\u1EC1',
      'footer.contact': 'Li\u00EAn H\u1EC7',
      'footer.support': 'H\u1ED7 Tr\u1EE3',
      'footer.privacy': 'Ch\u00EDnh S\u00E1ch B\u1EA3o M\u1EADt',
      'footer.terms': '\u0110i\u1EC1u Kho\u1EA3n D\u1ECBch V\u1EE5',
      'footer.copyright': '&copy; 2026 Code4change. B\u1EA3o l\u01B0u m\u1ECDi quy\u1EC1n.',
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
      btn.textContent = lang === 'en' ? '\uD83C\uDDFB\uD83C\uDDF3 VI' : '\uD83C\uDDEC\uD83C\uDDE7 EN';
      btn.setAttribute('aria-label', lang === 'en' ? 'Chuy\u1EC3n sang Ti\u1EBFng Vi\u1EC7t' : 'Switch to English');
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
        btn.textContent = '\uD83C\uDDEC\uD83C\uDDE7 EN';
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
