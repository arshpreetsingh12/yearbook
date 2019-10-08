
	function matchPassword() {
    var password = $.trim($('#password').val());
    var cpassword = $.trim($('#confirm_password').val());
     if (password != cpassword){
	   $("#mismatch_pass").css("display",'block');
   
               return false;

            }

     return true;
}


	