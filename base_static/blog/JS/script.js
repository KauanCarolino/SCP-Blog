$(document).ready(function () {
    $('#id_question').keypress(function (e) {
        if (e.which === 13) {
            e.preventDefault();
            $('#filtrar-btn').click();
        }
    });
});