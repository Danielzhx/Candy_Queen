$(document).ready(function() {
    const change_mode = (e) => {
        e.preventDefault();
        if (html.getAttribute('data-bs-theme') === 'dark') {
            html.setAttribute('data-bs-theme', 'light');
            localStorage.setItem('bs-theme', 'light')
        } else {
            html.setAttribute('data-bs-theme', 'dark');
            localStorage.setItem('bs-theme', 'dark')
        };
    };
    const html = document.getElementById('html_tag');
    const current = localStorage.getItem('bs-theme') || 'dark';
    html.setAttribute('data-bs-theme', current);

    $('#mode_button').on('click', change_mode);
    
});