const loginButton = document.getElementById('login');
const backendURL = 'http://127.0.0.1:8000';

loginButton.addEventListener('click', function(event) {
	event.preventDefault();

	const email = document.getElementById('email').value;
	const password = document.getElementById('password').value;
	const rememberMe = document.getElementById('remember_me').value;

	const formData = new FormData();
	formData.append('email', email);
	formData.append('password', password);
	formData.append('rememberMe', rememberMe);

	fetch(backendURL+'/api/register/user_regis/', {
		method: 'POST',
		body: formData
	})
	.then(response => response.json())
	.then(data => {
		console.log('Success post')
	})
	.catch(error => {
		console.log('error')
	});
});