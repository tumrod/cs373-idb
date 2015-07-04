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
        window.location.href = "http://127.0.0.1:5000/characters/sort_by=" + sort_attr
    }
}

