$( document ).ready(function() {

    // When document is ready, check the url and set the select value and button to the current sorting option if any
    if((window.location.href).indexOf('sort_by') != -1) {
       select_value = (decodeURI(window.location.href).split("=")[1]);
       $('#sort-order').val(select_value.split('_')[0]);
       $('#order').text(select_value.split('_')[1]);
    }

    // If the sorting option is currently -select-, disable the order button
    if($('#sort-order option:selected').text() == '-Select-') {
        $('#order').prop("disabled",true);
    }
});

// Detect when a new value has been passed selected on sort
$("#sort-order").change(function() {
    sort_attr = $('#sort-order option:selected').text();
    sortTable(sort_attr);
});

// Detect when order button has been toggled
$('#order').click(function() {
   sort_attr = $('#sort-order option:selected').text();
   if ($(this).text() == "v") {
      $(this).text("^");
      sortTable(sort_attr);
   }
   else {
      $(this).text("v");
      sortTable(sort_attr);
   }
});

// Given a sort_attr, make redirect to a url that supports sorting
function sortTable(sort_attr) {
    sort_attr = sort_attr.toLowerCase();
    if(sort_attr != '-select-') {

        $('#order').prop("disabled",false);

        if(aContainsB(window.location.href, 'characters')) {
            model = 'characters'
        }
        else if(aContainsB(window.location.href, 'planets')) {
            model = 'planets'
        }
        else if(aContainsB(window.location.href, 'species')) {
            model = 'species'
        }
        window.location.href = "/" + model + "/sort_by=" + sort_attr + '_' + $('#order').text()
    }
    else {
        $('#order').prop("disabled",true);
    }
}

function aContainsB (a, b) {
    return a.indexOf(b) >= 0;
}

// Manage select value redirects
$(".generic-select").click(function(){
    button = $('#'+this.id)
    var model = button.siblings()[0].id;
    var select_id = button.siblings()[1].id;

    selectedValue = $('#' + select_id + ' option:selected').text();

    window.location.href = '/' + model + '/' + selectedValue

});

