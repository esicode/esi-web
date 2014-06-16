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

var fields = {
  'firstname': $('#name'),
  'lastname': $('#lastname'),
  'user': $('#usuario'),
  'idnumber': $('#ci'),
  'email': $('#emailaddr'),
  'telephone': $('#tel'),
  'cellphone': $('#cel'),
  'password1': $('#password1'),
  'password2': $('#password2'),
}

$(document).ready(function () {
  $('#btnsignup').click(function (){
    var _form = {}
    Object.keys(fields).forEach(function (field) {
      _form[field] = fields[field].val();
    });
    $.ajax({
      type: 'POST',
      url: '/api/signup',
      data: _form,
      success: function(data){
        var sucess = true;
	      Object.keys(data).forEach(function (key) {
			    if (!data[key]) {
			      sucess = false;
			      fields[key].setCustomValidity('Datos inválidos');
			    }
		    });
		    if (sucess) {
			    window.location.href = '/';
		    }
      }
    });
  });
});
