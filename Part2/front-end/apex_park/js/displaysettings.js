const visitor_type = {
    'IN': 'Individual',
    'GR': 'Group',
    'ME': 'Member',
    'ST': 'Student',
    'Student': 'ST',
    'Member': 'ME',
    'Group' : 'GR',
    'Individual': 'IN'
}

if (sessionStorage.getItem('userId') !== null && window.location.href.includes('my_account.html')) {
    console.log("what?")
    $.ajax({
        url: 'http://127.0.0.1:8000/api/data_models/setting_details/' + sessionStorage.getItem('userId'),
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            var personalInfo = data;
            var nameField = document.querySelector('#MySettings #nameFieldText');
            var emailField = document.querySelector('#MySettings #emailFieldText');
            var passwordField = document.querySelector('#MySettings #passwordFieldText');

            var birthdayField = document.querySelector('#MySettings #birthdayFieldText');
            var phoneField = document.querySelector('#MySettings #phoneFieldText');

            var addressField = document.querySelector('#MySettings #addressFieldText');
            var cityField = document.querySelector('#MySettings #cityFieldText');
            var stateField = document.querySelector('#MySettings #stateFieldText');
            var zipField = document.querySelector('#MySettings #zipFieldText');

            var visitorTField = document.querySelector('#MySettings #visitorTFieldText')

            nameField.textContent = personalInfo['name'];
            emailField.textContent = personalInfo['email'];
            //passwordField.textContent = "************"//personalInfo['password'];

            const birthDate = new Date(personalInfo['birth_date']);
            const formattedDate = birthDate.toISOString().split('T')[0];

            birthdayField.textContent = formattedDate;
            phoneField.textContent = personalInfo['phone'];
            addressField.textContent = personalInfo['address'];
            cityField.textContent = personalInfo['city'];
            stateField.textContent = personalInfo['state'];
            zipField.textContent = personalInfo['zip'];
            visitorTField.textContent = visitor_type[personalInfo['visitor_type']];
        },
        error: function (xhr, status, error) {
            console.log(xhr.responseText);
        }
    });
}