// script.js

// Toggle Mobile Navigation Menu
function toggleMenu() {
    const navLinks = document.querySelector('.nav-links');
    const hamburger = document.querySelector('.hamburger');
    if (navLinks && hamburger) {
        navLinks.classList.toggle('active');
        hamburger.classList.toggle('active');
    }
}

// Toggle Search Bar
function toggleSearch() {
    const searchBar = document.getElementById('search-bar');
    if (searchBar) {
        searchBar.classList.toggle('active');
    }
}

// Toggle User Menu
function toggleUserMenu(event) {
    // Prevent the click from propagating to the document (which would close the menu)
    event.stopPropagation();
    const userMenu = document.querySelector('.user-menu');
    if (userMenu) {
        userMenu.classList.toggle('active');
    }
}

// Close User Menu When Clicking Outside
function closeUserMenuOnClickOutside(event) {
    const userMenu = document.querySelector('.user-menu');
    const userIcon = document.querySelector('.user-icon');
    // If the click is not inside the user icon, close the user menu
    if (userMenu && userIcon && !userIcon.contains(event.target)) {
        userMenu.classList.remove('active');
    }
}

document.addEventListener("DOMContentLoaded", function() {
    // Hamburger Menu Toggle
    const hamburger = document.querySelector('.hamburger');
    if (hamburger) {
        hamburger.addEventListener('click', toggleMenu);
    }
    
// Toggle search bar
    const searchIcon = document.querySelector('.search-symbol');
    const searchBar = document.querySelector('.search-bar');

searchIcon.addEventListener('click', () => {
    searchBar.classList.toggle('active');
});

// Toggle user menu
    const userIcon = document.querySelector('.user-icon');

userIcon.addEventListener('click', () => {
    userIcon.classList.toggle('active');
});
    
// Cart Icon: Redirect to cart page
    const cartSymbol = document.getElementById('cart-symbol');
    if (cartSymbol) {
        cartSymbol.addEventListener('click', function() {
            window.location.href = "{% url 'cart' %}"; // Ensure this URL is correct in your Django urls
        });
    }
    
// Close User Menu When Clicking Outside
    document.addEventListener('click', closeUserMenuOnClickOutside);
});
