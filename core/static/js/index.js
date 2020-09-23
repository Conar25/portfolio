// Nav toggle
const nav_toggle_btn = document.querySelector('.nav-toggle');
const overlay = document.querySelector('.overlay');
const nav = document.querySelector('nav');
const nav_elements = document.querySelectorAll('.nav-element');

nav_toggle_btn.addEventListener("click", (e) => {
    e.preventDefault();
    nav_toggle();
});

nav_elements.forEach(element => {
    element.addEventListener("click", e => {
        nav_toggle();
    });
});

function nav_toggle() {
    nav_toggle_btn.classList.toggle('active');
    overlay.classList.toggle('active');
    nav.classList.toggle('nav-hide');
}
