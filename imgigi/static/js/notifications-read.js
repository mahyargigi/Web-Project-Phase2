$('#notification').on('click',function(){
    console.log("here");
    $.ajax({
        url: '/read-notifications/',
        type: 'POST',
        data:{'message':'mark all as read'},
        success:function(result){
            if(result === "success"){
                $('#notification-count').html('');

            }
        }

    }) ;
});