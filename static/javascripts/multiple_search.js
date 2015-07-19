$( document ).ready(function() {
    $('#for-and').text($('#for-and').text() + ' AND search results for terms: ' + window.location.href.split('=')[1].split('+').join());
    $('#for-or').text($('#for-or').text() + ' OR search results for terms: ' + window.location.href.split('=')[1].split('+').join());
});