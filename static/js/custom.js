function get_meme() {
    $.ajax({
        type: 'POST',
        url: '/meme',
        data: '',
        contentType: 'application/json',
        success: function (data) {
            console.log(data)
            const meme_desc = JSON.parse(data.ResultSet).meme_desc
            const meme_image = JSON.parse(data.ResultSet).meme_image
            document.getElementById('meme_desc').innerHTML = meme_desc
            document.getElementById('meme_image').src = meme_image
        },
        error: function () {
            document.getElementById('meme_desc').innerHTML = "Cannot get the data. DB conenction lost."
        }
    })
}