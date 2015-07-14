// Manage select value redirects for characters
$(".generic-select-characters").click(function() {

    var info = (this.id).split('_');
    info[5] = info[5].replace(" ", "\\ ");
    info[5] = info[5].replace("'", "\\'");
    var siblingSelect = $('#sort_order_character_' + info[5]);
    var selectedValue = siblingSelect.val();

    window.location.href = '/characters/' + selectedValue
});

// Manage select value redirects for species
$(".generic-select-species").click(function() {
    var info = (this.id).split('_');
    info[5] = info[5].replace(" ", "\\ ");
    info[5] = info[5].replace("'", "\'");
    var siblingSelect = $('#sort-order-species-' + info[5]);
    var selectedValue = siblingSelect.val();

    window.location.href = '/species/' + selectedValue
});