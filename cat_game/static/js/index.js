
function sendId(element) {
    $(".cell").attr('disabled', 'disabled');

    if ($.inArray($(element).text(), ['X', 'O']) == -1) {

        $.post("game",
            {
                cell_id: $(element).attr('id')
            },
            function(data, status) {
                $(element).text(data.user_sign);
                if (data.game_over == 'false') {
                    $('#'+data.computer_move).text(data.computer_sign);
                    $(".cell").removeAttr('disabled');
                } else {
                    if (data.win_line != null) {
                        var win_line = data.win_line;
                        for (id in win_line) {
                            $('#'+win_line[id]).css('background-color', '#f7786b');
                        }
                        var congrats_message = '"'+data.winner+'"'+' won!';
                        if (data.winner == data.user_sign) {
                            congrats_message += 'Congratulations!';
                        } else {
                            congrats_message += 'Try next time';
                        }
                        alert(congrats_message);
                        $(location).attr('href','index');
                    }
                } 
            }
        );
    } else {
        $(".cell").removeAttr('disabled');
    }
}