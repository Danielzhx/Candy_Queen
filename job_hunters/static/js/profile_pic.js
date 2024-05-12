$.ajax({
    url: 'profile/pic/' + "{{ user.id }}",
    type: 'GET',
    success: function(resp) {
        let newHTML = resp.data.map(d => {
            return `<img src="/${d.url}" width=40, height=40 style="border-radius:50%">`
        });
        $('#profile.pic').html(newHTML);
    },
    error: function(xhr, status, error) {
        console.error(error);
    }
  })