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
        })
    }

//    $('.btn-danger').hover(function(){
//
//    });
//
//    $('.btn-danger').click(function(){
//       $(this).removeClass('btn-danger');
//       $(this).addClass('btn-info');
//       $(this).text("follow");
//       $(this).removeClass('following');
//       $(this).addClass('follow');
//    });

});
