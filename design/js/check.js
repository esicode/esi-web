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