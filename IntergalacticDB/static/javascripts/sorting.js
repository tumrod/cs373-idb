$( document ).ready(function() {

    // When document is ready, check the url and set the select value and button to the current sorting option if any
    if((window.location.href).indexOf('sort_by') != -1) {
       select_value = (decodeURI(window.location.href).split("=")[1]);
       $('#' + select_value.split('_')[0]).text(select_value.split('_')[1]);
    }

});

// Manage select value redirects for characters
$(".generic-select-characters").click(function() {

    var info = (this.id).split('-');
    var siblingSelect = $('#sort-order-character-' + info[5]);
    var model = siblingSelect.attr('value');
    var selectedValue = siblingSelect.val();

    window.location.href = '/' + model + '/' + selectedValue
});

// Manage select value redirects for species
$(".generic-select-species").click(function() {
    var info = (this.id).split('-');
    var siblingSelect = $('#sort-order-species-' + info[5]);
    var model = siblingSelect.attr('value');
    var selectedValue = siblingSelect.val();

    window.location.href = '/' + model + '/' + selectedValue
});

// Manage select value redirects
$(".order").click(function() {

    modelRoute = (window.location.href).split('/')[3];
    sortOrder = $('#' + this.id);

    if(sortOrder.text() == '^') {
        sortOrder.text('v');
    }
    else {
        sortOrder.text('^');
    }

    window.location.href = "/" + modelRoute + "/sort_by=" + this.id + '_' + sortOrder.text();

});



