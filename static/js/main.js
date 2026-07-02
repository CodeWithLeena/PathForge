// PathForge — Main JavaScript

document.addEventListener('DOMContentLoaded', function () {

  // Mobile menu toggle
  const toggle = document.getElementById('mobileToggle');
  const menu = document.getElementById('mobileMenu');
  if (toggle && menu) {
    toggle.addEventListener('click', () => menu.classList.toggle('open'));
  }

  // Animate elements on scroll
  const observerOptions = { threshold: 0.1, rootMargin: '0px 0px -40px 0px' };
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  document.querySelectorAll('.step-card, .feature-card, .roadmap-card, .about-card').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
    observer.observe(el);
  });

  // Navbar scroll effect
  const navbar = document.querySelector('.navbar');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 20) {
      navbar.style.background = 'rgba(10,10,15,0.97)';
    } else {
      navbar.style.background = 'rgba(10,10,15,0.85)';
    }
  });

  // Animate hero preview bars
  setTimeout(() => {
    document.querySelectorAll('.pp-fill').forEach(bar => {
      const target = bar.style.width;
      bar.style.width = '0%';
      setTimeout(() => { bar.style.width = target; }, 100);
    });
  }, 500);

});
