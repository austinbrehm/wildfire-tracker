// Theme toggle: switch between light and dark, persist in localStorage
document.addEventListener('DOMContentLoaded', function() {
    var toggle = document.querySelector('.theme-toggle');
    if (toggle) {
        toggle.addEventListener('click', function() {
            var root = document.documentElement;
            var isDark = root.getAttribute('data-theme') === 'dark';
            var next = isDark ? 'light' : 'dark';
            root.setAttribute('data-theme', next);
            try { localStorage.setItem('theme', next); } catch (e) {}
        });
    }
});

// Homepage: Add fade-in effect to hero section
document.addEventListener('DOMContentLoaded', function() {
    const hero = document.querySelector('.hero');
    if (hero) {
        hero.style.opacity = '0';
        hero.style.transition = 'opacity 1s';
        setTimeout(() => {
            hero.style.opacity = '1';
        }, 100);
    }
});

// General: Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});