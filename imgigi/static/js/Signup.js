!/**
 * Created by User on 4/11/15.
 */
$(document).ready(function(){
    var longPass = false ;
    var allfield = false ;
    var validEmail = false ;
    var matchPasswords = false ;
    var validDates = false ;

    var username = $("#id_username");
    var password = $("#id_password");
    var password_confirm = $("#id_password_confirm");
    var display_name = $("#id_display_name");
    var birthday = $("#id_birthday");
    var mail = $("#id_email");
    var captcha = $("#id_captcha_1");

    hideLabels();

    var checkAllFilled = function() {
        console.log("all"+allfield+"pass"+longPass+"date"+validDates+"mail"+validEmail+"match"+matchPasswords);

        if(longPass && allfield && validEmail && matchPasswords && validDates){
            $('.submit').removeClass('disabled');
        }
        else{
            $('.submit').addClass('disabled');
        }
    };
    function test(){
//        console.log('keyup');
        if(isFilled()){
            allfield = true;
        }
        else{
            allfield = false;
        }
        checkAllFilled();
    }

    birthday.on('change' ,
       function(){
           if(isValidDate($(this).val())){
                (birthday).parent().parent().addClass('has-success');
                (birthday).parent().parent().removeClass('has-error');
                validDates = true ;
           }
            else{
               (birthday).parent().parent().addClass('has-error');
               (birthday).parent().parent().removeClass('has-success');
               validDates = false ;
           }
           test();
    });
    username.keyup(function(){
        //console.log(username.val());
       if(username.val().length > 0){
           username.parent().parent().addClass('has-success');
           username.parent().parent().removeClass('has-error');
       }
        else{
           username.parent().parent().addClass('has-error');
           username.parent().parent().removeClass('has-success');
       }
        test();
    });
    display_name.keyup(function(){
       if($(this).val().length > 0){
           $(this).parent().parent().addClass('has-success');
           $(this).parent().parent().removeClass('has-error');
       }
        else{
           $(this).parent().parent().addClass('has-error');
           $(this).parent().parent().removeClass('has-success');
       }
        test();
    });
    password.keyup(function(){
        if(($(this).val().length < 6)&& ($(this).val().length > 0)){
            $(this).parent().parent().addClass('has-error');
            $(this).parent().parent().removeClass('has-success');
            longPass =  false
        }
        else if((password.val().length >= 6)){
            $(this).parent().parent().addClass('has-success');
            $(this).parent().parent().removeClass('has-error');
            longPass = true ;
        }
        else{
            $(this).parent().parent().removeClass('has-success');
            $(this).parent().parent().removeClass('has-error');
            longPass = false ;
        }

        if((password.val().length > 0) && (password_confirm.val().length > 0) && (password.val() !== password_confirm.val())){
//            $('#not-match').show();
            password_confirm.parent().parent().addClass('has-error');
            password_confirm.parent().parent().removeClass('has-success');

            matchPasswords = false ;
        }
        else if((password.val().length > 0) && (password_confirm.val().length > 0) && (password.val() === password_confirm.val())){
            password_confirm.parent().parent().removeClass('has-error');
            password_confirm.parent().parent().addClass('has-success');
//            $('#not-match').hide();
            matchPasswords = true ;
        }

        test();

    });
    password_confirm.keyup(function(){
        console.log('sec');
        if((password.val().length > 0) && (password_confirm.val().length > 0) && (password.val() !== password_confirm.val())){
            password_confirm.parent().parent().addClass('has-error');
            password_confirm.parent().parent().removeClass('has-success');
//            $('#not-match').show();
            matchPasswords = false ;
        }
        else if((password_confirm.val().length ==0)){
            password_confirm.parent().parent().removeClass('has-error');
            password_confirm.parent().parent().removeClass('has-success');
            matchPasswords = false ;
        }
        else{
            password_confirm.parent().parent().removeClass('has-error');
            password_confirm.parent().parent().addClass('has-success');
            matchPasswords = true ;
        }
        test();
    });
    mail.keyup(function(){
        if((isValidEmailAddress(mail.val()))){
            mail.parent().parent().addClass('has-success');
            mail.parent().parent().removeClass('has-error');
            validEmail = true ;
        }
        else if((mail.val().length>0)&&(!isValidEmailAddress(mail.val()))){
            mail.parent().parent().addClass('has-error');
            mail.parent().parent().removeClass('has-success');
            validEmail = false;
        }
        else{
            mail.parent().parent().removeClass('has-success');
            mail.parent().parent().removeClass('has-error');
        }
        test();
    });
    birthday.bootstrapMaterialDatePicker({ weekStart : 0 ,time: false } );
    var minDate = '1910-01-01' ;
    var maxDate = '2014-01-01' ;
//    $('#inputDate').bootstrapMaterialDatePicker('setMaxDate' , maxDate);
    birthday.bootstrapMaterialDatePicker('setMinDate' , minDate);

    captcha.on('change' ,
       function(){

           test();
    });

    $('.submit').on('click',function(){

       //$('#success-modal').show();
    });

    //$('#signup_form').on

 });
function isValidEmailAddress(emailAddress) {
        var pattern = new RegExp(/^((([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+(\.([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+)*)|((\x22)((((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(([\x01-\x08\x0b\x0c\x0e-\x1f\x7f]|\x21|[\x23-\x5b]|[\x5d-\x7e]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(\\([\x01-\x09\x0b\x0c\x0d-\x7f]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))))*(((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(\x22)))@((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?$/i);
        return pattern.test(emailAddress);
};
function isFilled(){
    console.log("in isFelled!");
            var filled = true ;
            $('.form-control').each(function(){
                    if($(this).val() === ""){
                        filled = false ;
                        console.log($(this).id);
                    };
                });
    console.log(filled);
    return filled;
};
function hideLabels(){
        $('.warning-label').hide();
}
function isValidDate(str){
	// STRING FORMAT yyyy-mm-dd
	if(str=="" || str==null){return false;}

	// m[1] is year 'YYYY' * m[2] is month 'MM' * m[3] is day 'DD'
	var m = str.match(/(\d{4})-(\d{2})-(\d{2})/);

	// STR IS NOT FIT m IS NOT OBJECT
	if( m === null || typeof m !== 'object'){return false;}

	// CHECK m TYPE
	if (typeof m !== 'object' && m !== null && m.size!==3){return false;}

	var ret = true; //RETURN VALUE
	var thisYear = new Date().getFullYear(); //YEAR NOW
	var minYear = 1910; //MIN YEAR

	// YEAR CHECK
	if( (m[1].length < 4) || m[1] < minYear || m[1] > thisYear){ret = false;}
	// MONTH CHECK
	if( (m[1].length < 2) || m[2] < 1 || m[2] > 12){ret = false;}
	// DAY CHECK
	if( (m[1].length < 2) || m[3] < 1 || m[3] > 31){ret = false;}

	return ret;
}

