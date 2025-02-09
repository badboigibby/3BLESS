document.addEventListener("DOMContentLoaded", function () {
    // Toggle search bar
    document.getElementById("search-icon").addEventListener("click", function () {
        var searchBar = document.getElementById("search-bar");
        searchBar.style.display = (searchBar.style.display === "none") ? "block" : "none";
    });

    // Toggle mobile menu
    document.getElementById("hamburger").addEventListener("click", function () {
        var navLinks = document.getElementById("nav-links");
        navLinks.classList.toggle("active");
    });
});
