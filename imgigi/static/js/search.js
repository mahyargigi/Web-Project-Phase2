$('form').keydown(function(event){
    if ($(this).attr('role') === 'search'){
        if (event.which == 13){
            console.log("enter");
            var query = $(this).find('input[name="search"].tt-input').val();
            $(this).find('input[name="search"].tt-input').val("");
            data = {'query':query};
            $.ajax({
                url:'/search/',
                type:"POST",
                data: data,
                success:function(result){
                    $('#center').html(result);
                    $('#center .rating').rating();
                }
            });
        }

    }
});

