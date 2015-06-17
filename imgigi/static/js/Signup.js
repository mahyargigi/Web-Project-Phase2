!/**
 * Created by User on 4/11/15.
 */
$(document).ready(function(){
    var longPass = false ;
    var allfield = false ;
    var validEmail = false ;
    var matchPasswords = false ;
    var validDates = false ;

    hideLabels();
    console.log("loaded!");
    var checkAllFilled = function() {
//        console.log("caf");
        if(longPass && allfield && validEmail && matchPasswords && validDates){
            $('.submit').removeClass('disabled');
            console.log("longpass="+longPass);
            console.log("allfield="+allfield);
            console.log("valideEmail="+validEmail);
            console.log("matchpasswords="+matchPasswords);
            console.log("validDates="+validDates);

        }
        else{
            console.log("longpass="+longPass);
            console.log("allfield="+allfield);
            console.log("valideEmail="+validEmail);
            console.log("matchpasswords="+matchPasswords);
            console.log("validDates="+validDates);
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


//    $('input').keyup(function(){
//        console.log('keyup');
//        if(isFilled()){
//            allfield = true;
//        }
//        else{
//            allfield = false;
//        }
//        checkAllFilled();
//    });

//    $('select').on('change', function(){ //keyup bood avalesh
//        if(($('.birthMonth').val()!= 0) && ($('.birthDate').val()!= 0) && ($('.birthYear').val()!= 0)){
//            validDates = true ;
//        }
//        else{
//            validDates = false;
//        }
//        console.log('change');
//        checkAllFilled();
//    });
    $('#inputDate').on('change' ,
       function(){

           if(isValidDate($('#inputDate').val())){
                $('#inputDate').parent().parent().addClass('has-success');
                $('#inputDate').parent().parent().removeClass('has-error');
                validDates = true ;
           }
            else{
               $('#inputDate').parent().parent().addClass('has-error');
               $('#inputDate').parent().parent().removeClass('has-success');
               validDates = false ;
           }
           test();
    });
    $('#id_username').keyup(function(){
       if($('#id_username').val().length > 0){
           $('#id_username').parent().parent().addClass('has-success');
           $('#id_username').parent().parent().removeClass('has-error');
       }
        else{
           $('#id_username').parent().parent().addClass('has-error');
           $('#id_username').parent().parent().removeClass('has-success');
       }
        test();
    });
    $('#inputDisplayname').keyup(function(){
       if($('#inputDisplayname').val().length > 0){
           $('#inputDisplayname').parent().parent().addClass('has-success');
           $('#inputDisplayname').parent().parent().removeClass('has-error');
       }
        else{
           $('#inputDisplayname').parent().parent().addClass('has-error');
           $('#inputDisplayname').parent().parent().removeClass('has-success');
       }
        test();
    });
    $('#inputPassword').keyup(function(){
        if(($('#inputPassword').val().length < 6)&& ($('#inputPassword').val().length > 0)){
            $('#inputPassword').parent().parent().addClass('has-error');
            $('#inputPassword').parent().parent().removeClass('has-success');
            longPass =  false
        }
        else if(($('#inputPassword').val().length >= 6)){
            $('#inputPassword').parent().parent().addClass('has-success');
            $('#inputPassword').parent().parent().removeClass('has-error');
            longPass = true ;
        }
        else{
            $('#inputPassword').parent().parent().removeClass('has-success');
            $('#inputPassword').parent().parent().removeClass('has-error');
            longPass = false ;
        }

        if(($('#inputPassword').val().length > 0) && ($('#ConfirmPassword').val().length > 0) && ($('#inputPassword').val() !== $('#ConfirmPassword').val())){
//            $('#not-match').show();
            $('#ConfirmPassword').parent().parent().addClass('has-error');
            $('#ConfirmPassword').parent().parent().removeClass('has-success');

            matchPasswords = false ;
        }
        else if(($('#inputPassword').val().length > 0) && ($('#ConfirmPassword').val().length > 0) && ($('#inputPassword').val() === $('#ConfirmPassword').val())){
            $('#ConfirmPassword').parent().parent().removeClass('has-error');
            $('#ConfirmPassword').parent().parent().addClass('has-success');
//            $('#not-match').hide();
            matchPasswords = true ;
        }

        test();

    });
    $('#ConfirmPassword').keyup(function(){
        console.log('sec');
        if(($('#inputPassword').val().length > 0) && ($('#ConfirmPassword').val().length > 0) && ($('#inputPassword').val() !== $('#ConfirmPassword').val())){
            $('#ConfirmPassword').parent().parent().addClass('has-error');
            $('#ConfirmPassword').parent().parent().removeClass('has-success');
//            $('#not-match').show();
            matchPasswords = false ;
        }
        else if(($('#ConfirmPassword').val().length ==0)){
            $('#ConfirmPassword').parent().parent().removeClass('has-error');
            $('#ConfirmPassword').parent().parent().removeClass('has-success');
            matchPasswords = false ;
        }
        else{
            $('#ConfirmPassword').parent().parent().removeClass('has-error');
            $('#ConfirmPassword').parent().parent().addClass('has-success');
            matchPasswords = true ;
        }
        test();
    });
    $('#inputEmail').keyup(function(){
        if((isValidEmailAddress($('#inputEmail').val()))){
            $('#inputEmail').parent().parent().addClass('has-success');
            $('#inputEmail').parent().parent().removeClass('has-error');
            validEmail = true ;
        }
        else if(($('#inputEmail').val().length>0)&&(!isValidEmailAddress($('#inputEmail').val()))){
            $('#inputEmail').parent().parent().addClass('has-error');
            $('#inputEmail').parent().parent().removeClass('has-success');
            validEmail = false;
        }
        else{
            $('#inputEmail').parent().parent().removeClass('has-success');
            $('#inputEmail').parent().parent().removeClass('has-error');
        }
        test();
    });
    $('#inputDate').bootstrapMaterialDatePicker({ weekStart : 0 ,time: false } );
    var minDate = '1910-01-01' ;
    var maxDate = '2014-01-01' ;
//    $('#inputDate').bootstrapMaterialDatePicker('setMaxDate' , maxDate);
    $('#inputDate').bootstrapMaterialDatePicker('setMinDate' , minDate);

    $('.submit').on('click',function(){
       $('#success-modal').show();
    });
 });
function isValidEmailAddress(emailAddress) {
        var pattern = new RegExp(/^((([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+(\.([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+)*)|((\x22)((((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(([\x01-\x08\x0b\x0c\x0e-\x1f\x7f]|\x21|[\x23-\x5b]|[\x5d-\x7e]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(\\([\x01-\x09\x0b\x0c\x0d-\x7f]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))))*(((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(\x22)))@((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?$/i);
        return pattern.test(emailAddress);
};
function isFilled(){
            var filled = true ;
            $('.form-control').each(function(){
                    if($(this).val() === ""){
                        filled = false ;
                        console.log($(this).id);
                    };
                });
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

