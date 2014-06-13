function check(input, idPrincipal) {
	if (input.value != document.getElementById(idPrincipal).value) {
		input.setCustomValidity('Las contraseñas deben coincidir');
	} else {
		input.setCustomValidity('');
	}
}

function validationCI(input) {
	if (input.value.length > input.maxLength) {
		input.value = input.value.slice(0, input.maxLength);
	}
	if (input.value.length < input.maxLength) {
		input.setCustomValidity('Cédula inválida');
	} else {
		input.setCustomValidity('');
	}
}

$(document).ready(function () {
  $('#btnsignup').click(function (){
    var _form = {
      'firstname': $('#name').val(),
      'lastname': $('#lastname').val(),
      'user': $('#usuario').val(),
      'idnumber': $('#ci').val(), 
      'email': $('#emailaddr').val(),
      'telephone': $('#tel').val(),
      'cellphone': $('#cel').val(),
      'password1': $('#password1').val(),
      'password2': $('#password2').val() 
      }
    console.log(JSON.stringify(_form));
    $.ajax({
      type: 'POST',
      url: '/api/signup',
      data: _form
    });
    console.log(_form);
  })
})