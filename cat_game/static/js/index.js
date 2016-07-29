
function sendId(element) {

    $("button").attr('disabled', 'disabled');
    $.post("game",
        {
            cell_id: $(element).attr('id')
        },
        function(data, status) {
            if (data.status = 'ok') {
                $(element).text(data.user_sign);
                // alert(data.game_over);
                if (data.game_over == 'false') {
                    // alert("hahaha");
                    $('#'+data.computer_move).text(data.computer_sign);
                    $("button").removeAttr('disabled');
                } 
            } else {
                $("button").removeAttr('disabled');
            };
        }
    );



}