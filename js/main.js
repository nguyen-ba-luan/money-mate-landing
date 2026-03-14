/**
 * Money Mate Landing Page - Interactions
 */

(function () {
  'use strict';

  // --- Scroll-triggered nav background ---
  const navbar = document.getElementById('navbar');

  function handleNavScroll() {
    if (window.scrollY > 50) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  }

  window.addEventListener('scroll', handleNavScroll, { passive: true });
  handleNavScroll();

  // --- Mobile hamburger menu ---
  const hamburgerBtn = document.getElementById('hamburger-btn');
  const mobileMenu = document.getElementById('mobile-menu');
  let menuOpen = false;

  function toggleMenu() {
    menuOpen = !menuOpen;
    hamburgerBtn.classList.toggle('active', menuOpen);
    mobileMenu.classList.toggle('open', menuOpen);
    document.body.style.overflow = menuOpen ? 'hidden' : '';
  }

  hamburgerBtn.addEventListener('click', toggleMenu);

  // Close mobile menu on link click
  mobileMenu.querySelectorAll('a').forEach(function (link) {
    link.addEventListener('click', function () {
      if (menuOpen) toggleMenu();
    });
  });

  // --- Smooth scroll for anchor links ---
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      var targetId = this.getAttribute('href');
      if (targetId === '#') return;

      var target = document.querySelector(targetId);
      if (target) {
        e.preventDefault();
        var offset = navbar.offsetHeight + 16;
        var top = target.getBoundingClientRect().top + window.pageYOffset - offset;
        window.scrollTo({ top: top, behavior: 'smooth' });
      }
    });
  });

  // --- Intersection Observer for fade-in animations ---
  var prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  if (!prefersReducedMotion) {
    var fadeObserver = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            fadeObserver.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.1, rootMargin: '0px 0px -40px 0px' }
    );

    document.querySelectorAll('.fade-up').forEach(function (el) {
      fadeObserver.observe(el);
    });
  } else {
    // If reduced motion, just show everything
    document.querySelectorAll('.fade-up').forEach(function (el) {
      el.classList.add('visible');
    });
  }

  // --- Count-up animation for stats ---
  var statElements = document.querySelectorAll('[data-count]');
  var statsAnimated = false;

  function animateCountUp(el) {
    var target = parseFloat(el.getAttribute('data-count'));
    var isDecimal = el.getAttribute('data-decimal') === 'true';
    var duration = 2000;
    var startTime = null;
    var suffix = '';

    // Add suffix for large numbers
    if (target >= 1000 && !isDecimal) {
      suffix = '+';
    }

    function step(timestamp) {
      if (!startTime) startTime = timestamp;
      var progress = Math.min((timestamp - startTime) / duration, 1);
      // Ease out cubic
      var eased = 1 - Math.pow(1 - progress, 3);
      var current = eased * target;

      if (isDecimal) {
        el.textContent = current.toFixed(1);
      } else {
        el.textContent = Math.floor(current).toLocaleString() + (progress >= 1 ? suffix : '');
      }

      if (progress < 1) {
        requestAnimationFrame(step);
      }
    }

    requestAnimationFrame(step);
  }

  if (statElements.length > 0 && !prefersReducedMotion) {
    var statsObserver = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting && !statsAnimated) {
            statsAnimated = true;
            statElements.forEach(animateCountUp);
            statsObserver.disconnect();
          }
        });
      },
      { threshold: 0.3 }
    );

    statElements.forEach(function (el) {
      statsObserver.observe(el);
    });
  } else {
    // If reduced motion, show final values immediately
    statElements.forEach(function (el) {
      var target = el.getAttribute('data-count');
      var isDecimal = el.getAttribute('data-decimal') === 'true';
      if (isDecimal) {
        el.textContent = parseFloat(target).toFixed(1);
      } else {
        var num = parseInt(target, 10);
        el.textContent = num.toLocaleString() + (num >= 1000 ? '+' : '');
      }
    });
  }

  // --- FAQ Accordion ---
  var faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(function (item) {
    var btn = item.querySelector('.faq-question');
    if (!btn) return;
    btn.addEventListener('click', function () {
      var isActive = item.classList.contains('active');
      // Close all
      faqItems.forEach(function (other) {
        other.classList.remove('active');
        var otherBtn = other.querySelector('.faq-question');
        if (otherBtn) otherBtn.setAttribute('aria-expanded', 'false');
      });
      // Open clicked (if it was closed)
      if (!isActive) {
        item.classList.add('active');
        btn.setAttribute('aria-expanded', 'true');
      }
    });
  });

  // --- Mobile Sticky CTA Bar ---
  var stickyCta = document.getElementById('sticky-cta');
  var heroSection = document.getElementById('hero');
  var ctaSection = document.getElementById('download');

  if (stickyCta && heroSection) {
    function handleStickyCta() {
      var heroBottom = heroSection.offsetTop + heroSection.offsetHeight;
      var ctaTop = ctaSection ? ctaSection.offsetTop - window.innerHeight : Infinity;
      var scrollY = window.scrollY;

      // Show after scrolling past hero, hide when reaching final CTA
      if (scrollY > heroBottom && scrollY < ctaTop) {
        stickyCta.classList.add('visible');
      } else {
        stickyCta.classList.remove('visible');
      }
    }

    window.addEventListener('scroll', handleStickyCta, { passive: true });
    handleStickyCta();
  }

  // --- Active nav link highlighting ---
  var sections = document.querySelectorAll('section[id]');
  var navLinks = document.querySelectorAll('.nav-link');

  function highlightNav() {
    var scrollPos = window.scrollY + navbar.offsetHeight + 100;

    sections.forEach(function (section) {
      var top = section.offsetTop;
      var height = section.offsetHeight;
      var id = section.getAttribute('id');

      if (scrollPos >= top && scrollPos < top + height) {
        navLinks.forEach(function (link) {
          link.classList.remove('active');
          if (link.getAttribute('href') === '#' + id) {
            link.classList.add('active');
          }
        });
      }
    });
  }

  window.addEventListener('scroll', highlightNav, { passive: true });
  highlightNav();
})();
