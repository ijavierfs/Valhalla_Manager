$(document).ready(function(){

    $('#search-user-form').submit(function(e){
        e.preventDefault();
        $.ajax({
            url: $(this).attr('action'),
            type: $(this).attr('method'),
            data: $(this).serialize(),

            success: function(json){
                var html ="";
                var link = window.location.pathname + "add/";

                for(let elem of json){
                    href= link + elem.username + "/"
                    html += '<li>' + elem.username + '<a href="' + href + '">Añadir</a></li>'
                }
                $('#ajax-result ul').empty()
                $('#ajax-result ul').append(html)
            }
        })
    })

})