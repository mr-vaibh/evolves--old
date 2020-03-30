const username = document.getElementById("id_username")
const password = document.getElementById("id_password"); 

username.placeholder = "Username";
try{    password.placeholder = "Password";     } catch(e) {}

$('.requiredField').remove();

// For registration page
const tnc = document.getElementById('agree-term');
const signup = document.getElementById('signup');
signup.disabled = true;
$('#signup').css({opacity: 0.5});
// when unchecked or checked, run the function
tnc.onchange = function(){
    if(this.checked){
    signup.disabled = false;
    $('#signup').css({opacity: 1});
    } else {
        signup.disabled = true;
        $('#signup').css({opacity: 0.5});
    }
}