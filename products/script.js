// scripts.js

// Toggle Menu for Mobile
function toggleMenu() {
    const navLinks = document.querySelector('.nav-links');
    navLinks.classList.toggle('active');
}

// Toggle Search Bar
function toggleSearch() {
    const searchBar = document.querySelector('.search-bar');
    searchBar.classList.toggle('active');
}

// Toggle User Menu
function toggleUserMenu() {
    const userMenu = document.querySelector('.user-menu');
    userMenu.classList.toggle('active');
}

// Close User Menu When Clicking Outside
function closeUserMenuOnClickOutside(event) {
    const userMenu = document.querySelector('.user-menu');
    const userIcon = document.querySelector('.user-icon');
    if (userMenu && userIcon && !userIcon.contains(event.target) && !userMenu.contains(event.target)) {
        userMenu.classList.remove('active');
    }
}

// Add Event Listeners
document.addEventListener('DOMContentLoaded', function () {
    // Hamburger Menu
    const hamburger = document.querySelector('.hamburger');
    if (hamburger) {
        hamburger.addEventListener('click', toggleMenu);
    }

    // Search Symbol
    const searchSymbol = document.querySelector('.search-symbol');
    if (searchSymbol) {
        searchSymbol.addEventListener('click', toggleSearch);
    }

    // User Icon
    const userIcon = document.querySelector('.user-icon');
    if (userIcon) {
        userIcon.addEventListener('click', toggleUserMenu);
    }

    // Close User Menu When Clicking Outside
    document.addEventListener('click', closeUserMenuOnClickOutside);

    // Cart Symbol
    const cartSymbol = document.querySelector('.cart-symbol');
    if (cartSymbol) {
        cartSymbol.addEventListener('click', function () {
            window.location.href = "{% url 'cart' %}";
        });
    }
});

// scripts.js

document.addEventListener('DOMContentLoaded', function() {
    // Mobile Menu Toggle
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
        userIcon.addEventListener('click', (e) => {
            e.stopPropagation();
            userMenu.classList.toggle('active');
        });
    }

    // Country Selector Toggle
    const countrySelector = document.querySelector('.country-selector');
    
    if (countrySelector) {
        countrySelector.addEventListener('click', (e) => {
            e.stopPropagation();
            countrySelector.classList.toggle('active');
        });
    }

    // Close dropdowns when clicking outside
    document.addEventListener('click', (e) => {
        if (userMenu && !userIcon.contains(e.target)) {
            userMenu.classList.remove('active');
        }
        if (countrySelector && !countrySelector.contains(e.target)) {
            countrySelector.classList.remove('active');
        }
    });

    // Close mobile menu when clicking links
    document.querySelectorAll('.nav-links a').forEach(link => {
        link.addEventListener('click', () => {
            navLinks.classList.remove('active');
            hamburger.classList.remove('active');
        });
    });
});