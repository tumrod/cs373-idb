$( document ).ready(function() {
    $('#for').text($('#for').text() + ' search results for term: ' + window.location.href.split('=')[1]);
});