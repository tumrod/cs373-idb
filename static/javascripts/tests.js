$(document).ready(function (){
    
    var $result= $('#result');
    
    $.ajax({
        type: 'GET',
        url: '/api/tests',
        success: function(result) {
           console.log(result)
           var jsonObj = JSON.parse(result)
           $result.append("<p>" + jsonObj.result + "</p>")
        }
    });
});

$(".unit-test").click(function() {

    window.location.href = '/api/tests'

});
