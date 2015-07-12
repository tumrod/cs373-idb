// Manage select value redirects for characters
$(".generic-select-characters").click(function() {

    var info = (this.id).split('-');
    var siblingSelect = $('#sort-order-character-' + info[5]);
    var selectedValue = siblingSelect.val();

    window.location.href = '/characters/' + selectedValue
});

// Manage select value redirects for species
$(".generic-select-species").click(function() {
    var info = (this.id).split('-');
    var siblingSelect = $('#sort-order-species-' + info[5]);
    var selectedValue = siblingSelect.val();

    window.location.href = '/species/' + selectedValue
});