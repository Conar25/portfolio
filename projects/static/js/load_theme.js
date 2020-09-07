// Theme picker
document.addEventListener("DOMContentLoaded", () => {
    const themes = document.querySelectorAll('.theme');
    const theme_link = document.getElementById('link-theme')

    if (themes)
        themes.forEach(element => {
            element.addEventListener("click", change_theme);
        });


    function change_theme(event) {
        element = event.currentTarget;
        theme_color = element.dataset.theme;    
        set_theme(theme_color);
    }

    function set_theme(theme_color) {
        theme_link.href = `/css/theme-${theme_color}.css`;
        theme_link.type = 'text/css';
        localStorage.setItem('theme', theme_color);
    }

    theme_color = localStorage.getItem('theme');
    if (theme_color) {
        console.log(theme_color);
        set_theme(theme_color);
    }
});