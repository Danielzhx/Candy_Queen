/* $(document).ready(function() {
    $.ajax({
        url: 'profiles/',
        type: 'GET',
        success: function(resp) {
            console.log(resp.data)
            $("#profile_pic").attr("src", resp.data['profile'].pic)
        },
        error: function(xhr, status, error) {
            console.error(error);
        }
    })
}) */

$(document).ready(function() {
    console.log(document)
    $.get('profiles/get_pic/' + document.user.id,
        getPic = () => {
            console.log(response)
    })
})