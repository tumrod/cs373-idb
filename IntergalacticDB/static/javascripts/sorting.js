$( document ).ready(function() {
  if((window.location.href).indexOf('sort_by') != -1) {
     select_value = (window.location.href).split("=")[1]
     $('#sort-order').val(select_value);
  }
});

$("#sort-order").change(function() {
    sort_attr = $('#sort-order option:selected').text();
    sortTable(sort_attr);
});

function sortTable(sort_attr) {
    sort_attr = sort_attr.toLowerCase()
    if(sort_attr != '-select-') {

        if(aContainsB(window.location.href, 'characters')) {
            model = 'characters'
        }
        else if(aContainsB(window.location.href, 'planets')) {
            model = 'planets'
        }
        else if(aContainsB(window.location.href, 'species')) {
            model = 'species'
        }
        window.location.href = "http://127.0.0.1:5000/" + model + "/sort_by=" + sort_attr
    }
}

function aContainsB (a, b) {
    return a.indexOf(b) >= 0;
}

