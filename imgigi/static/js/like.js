/**
 * Created by User on 6/29/15.
 */
$(document).ready(function(){
    $('body').on('click','.glyphicon-heart-empty',function(){
    var $button = $(this);
    post_id = (this).id;
    post_id = post_id.split('-').pop();
    data = { 'id':post_id};

    $.ajax({
        url : '/like/',
        type : "POST" ,
        data : data,
        success:function(result){
    //            console.log(result);
            console.log("hoora");
            console.log('it is : '+ $($button).next("span").html());
        $($button).next("span").html(result);


        }
    });
    });
});
