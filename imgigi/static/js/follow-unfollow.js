/**
 * Created by User on 4/29/15.
 */
$(document).ready(function () {
    notClicked($('.follow'));
    clicked($('.following'));

    function notClicked($element) {
        $element.unbind();
        $element.removeClass('btn-danger')
            .addClass('btn-info')
            .text('follow')
            .removeClass('following')
            .addClass('follow');
        $element.click(function () {
            clicked($(this));
            var element_id = $(this).attr('identifier').split('-').pop();
            data = {'id':element_id , 'action':"follow"};
            $.ajax({
                url: '/follow-unfollow',
                type: 'POST',
                data: data,
                success:function(result){
                    console.log(result);
                }

            });
        });
    }

    function clicked($element) {
        $element.unbind();
        $element.removeClass('btn-info')
            .addClass('btn-success')
            .text("following")
            .removeClass('follow')
            .addClass('following');
        $element.hover(function () {
                $(this).removeClass('btn-success')
                    .addClass('btn-danger')
                    .text("Unfollow");
            },
            function () {
                $(this).removeClass('btn-danger')
                    .addClass('btn-success')
                    .text("following");
            });
        $element.click(function () {
            notClicked($(this));
            var element_id = $(this).attr('identifier').split('-').pop();
            data = {'id':element_id , 'action':"unfollow"};
            $.ajax({
                url: '/follow-unfollow',
                type: 'POST',
                data: data,
                success:function(result){
                    console.log(result);
                }

            });
        })
    }


});
