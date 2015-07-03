$( document ).ready(function() {
  if((window.location.href).indexOf('sort_by') != -1) {
     select_value = (window.location.href).split("=")[1]
     $('#sort-order').val('name');
  }
});

$("#sort-order").change(function() {
    sort_attr = $('#sort-order option:selected').text();
    sortTable(sort_attr);
});

function sortTable(sort_attr) {
  switch(sort_attr) {
    case 'Name':
      window.location.href = "http://127.0.0.1:5000/characters/sort_by=name"
      break;
    case 'gender':
        break;
    case 'birth':
        break;
    case 'planet':
        break;
    case 'species':
        break;
    default:
  }
}

