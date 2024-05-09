$(document).ready(function() {
    /* Function to change light/dark theme */
    const change_mode = (e) => {
        /* e.preventDefault(); */
        if (html.getAttribute('data-bs-theme') === 'dark') {
            html.setAttribute('data-bs-theme', 'light');
            localStorage.setItem('bs-theme', 'light');
            button.text = "Dark Theme";
            $(".bg-dark.text-light").attr('class', 'light_option');
        } else {
            html.setAttribute('data-bs-theme', 'dark');
            localStorage.setItem('bs-theme', 'dark');
            button.text = "Light Theme";
            $(".light_option").attr('class', 'bg-dark text-light');
        };
    };
    /* Get relevant elements */
    const html = document.getElementById('html_tag');
    const button = document.getElementById('mode_button');

    /* Retrieve saved theme when page loads */
    const current = localStorage.getItem('bs-theme') || 'dark';
    html.setAttribute('data-bs-theme', current);
    if (current === 'light') {
        $(".bg-dark.text-light").attr('class', 'light_option');
        button.text = "Dark Theme";
        button.checked = true;
    };

    /* When to trigger the function */
    $('#mode_button').on('click', change_mode);
    
});