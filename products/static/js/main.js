// main.js

document.addEventListener('DOMContentLoaded', function () {
    // Mobile Navigation Toggle
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');

    if (hamburger) {
        hamburger.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            hamburger.classList.toggle('active');
        });
    }

    // User Menu Toggle
    const userIcon = document.querySelector('.user-icon');
    const userMenu = document.querySelector('.user-menu');

    if (userIcon) {
        userIcon.addEventListener('click', (event) => {
            event.stopPropagation();
            userMenu.classList.toggle('active');
        });
    }

    // Country Selector Toggle
    const countrySelector = document.querySelector('.country-selector');

    if (countrySelector) {
        countrySelector.addEventListener('click', (event) => {
            event.stopPropagation();
            countrySelector.classList.toggle('active');
        });
    }

    // Fix: Close dropdowns when clicking outside
    document.addEventListener('click', (event) => {
        if (userMenu && !userMenu.contains(event.target) && !userIcon.contains(event.target)) {
            userMenu.classList.remove('active');
        }
        if (countrySelector && !countrySelector.contains(event.target)) {
            countrySelector.classList.remove('active');
        }
    });

    // Fix: Close mobile menu when clicking links
    document.querySelectorAll('.nav-links a').forEach(link => {
        link.addEventListener('click', () => {
            navLinks.classList.remove('active');
            hamburger.classList.remove('active');
        });
    });

    // Fix: Ensure cart redirect only runs if the element exists
    const cartSymbol = document.querySelector('.cart-symbol');
    if (cartSymbol) {
        cartSymbol.addEventListener('click', function () {
            window.location.href = "/cart"; // Update with actual cart URL
        });
    }
});
