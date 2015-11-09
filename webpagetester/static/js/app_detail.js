function update_test(d) {
    $("#overlay").fadeIn();

    $.ajax({
        url : "/update_test/", // the endpoint
        type : "POST", // http method
        data : { test_id : d.name }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            $("#overlay").fadeOut();
            location.reload();
        },


        error : function(xhr,errmsg,err) {
            alert('Erro! ' +  xhr.responseText)
            $("#overlay").fadeOut();

            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });


}

$(document).ready(function(){
    $('.updater').on('submit', function(event){
    event.preventDefault();
    update_test(this);
    });

    $t = $("#alerts_table");
    $("#overlay").css({
      opacity : 0.5,
      top     : $t.offset().top,
      width   : $t.outerWidth(),
      height  : $t.outerHeight()
    });

    $("#img-load").css({
      top  : ($t.height() / 2),
      left : ($t.width() / 2)
    });

    $(".fancybox").fancybox();
});

$(function() {
    $('input[name=selection]').click(function(){
        if($(this).parent().parent().siblings().children().children("input[name=selection]:checkbox:checked").length >= 2)
            this.checked = false;
    });
});

