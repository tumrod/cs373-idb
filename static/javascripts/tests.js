$(document).ready(function (){
    
    var $result= $('#result');
    
    $.ajax({
        type: 'GET',
        url: '/api/tests',
        success: function(result) {
           console.log(result)
           $result.append("<p>" + result + "</p>")
        }
    });
});
