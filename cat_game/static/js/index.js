
function sendId(element) {

    $("button").attr('disabled', 'disabled');
    $.post("game",
        {
            cell_id: element.value
        },
        function(data, status) {
            $(element).text(data.sign);
            $("button").removeAttr('disabled');
        }
    );



}