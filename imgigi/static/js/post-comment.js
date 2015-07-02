/**
 * Created by User on 6/19/15.
 */
$(document).ready(function(){
    $('body').on('click','.post-comment',
    function(e){
        var id= (this).id;
        parts = id.split('-');
        id = parts.pop();
        var textAreaID = 'focusedInput-'+id;
        if($('#'+textAreaID).val() !== ''){
            var comment = $('#'+textAreaID).val();
            var post_id = $(this).parent().closest('div').attr('id');
            post_id = post_id.split('-').pop();
            dictionary = {
              'name' : 'name',
              'comment' : comment,
              'post_id' : post_id
            };
            $.ajax({
                url : '/post-comment/',
                type: "POST",
                data: dictionary,
                success:function(result){
//                    $('<li><div class="list-group-item"><div class="row-picture"><img class="circle" src="#" alt="icon"></div><div class="row-content"><h4 class="list-group-item-heading">Mahyar Gigi</h4><p class="list-group-item-text">'+comment+'</p></div></div><!--</div>--><div class="list-group-separator"></div></li>').insertBefore('#text-button-'+id);
//                    $('.post-'+post_id+' comments').val('');

                    $('#post-' +post_id.toString()+ ' .comments')[0].innerHTML = result;
//                    $(result).insertBefore('#text-button-'+id);
                    $('#focusedInput-'+id).val('');
                }
            });

        }
    }
);
});