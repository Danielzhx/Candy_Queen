$(document).ready(function() {
    $('#filter_button').on('click', get_jobs);

    $("#search_name").keyup(function (event) {
        if (event.keyCode == 13) {
            event.preventDefault();
            get_jobs(event);
        }});

    function get_jobs(e) {{
        e.preventDefault();        
        let search = $('#search_name').val();
        $.ajax({
            url: '?query=True' + '&search_name=' + search,
            type: 'GET',
            success: function(resp) {
                let newHTML = resp.data.map(d => {
                    return `<div class="col">
                                <div class="card" style="width:40%">
                                <div class="card-body">
                                    <h5 class="card-title"><a href="${d.id}">${d.title}</a></h5>
                                    <p class="card-text">${d.company}</p>
                                </div>
                                </div>
                            </div>`
                });
                $('#job_list').html(newHTML.join(''));
                $('#searchName').val('');
            },
            error: function(xhr, status, error) {
                console.error(error);
            }
        })
    }};
    get_jobs(new Event('click'))
});