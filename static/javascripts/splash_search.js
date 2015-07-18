$( document ).ready(function() {
    $(".input-sm").keyup(function (e) {
        if (e.keyCode == 13) {
            window.location.href = '/search/query=' + $(this).val().split(' ').join('+');
        }
    });
});