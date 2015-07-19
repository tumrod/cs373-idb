$( document ).ready(function() {
    $(".input-sm").keyup(function (e) {
        if (e.keyCode == 13) {
            var search_terms = $(this).val().split(' ');

            if(search_terms.length == 1) {
                window.location.href = '/search/query=' + search_terms[0];
            } else {
                window.location.href = '/search/query=' + search_terms.join('+');
            }
        }
    });
});