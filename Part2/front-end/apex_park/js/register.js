
//This scrtipts used to register user into backend 
$(document).ready(function () {
    $('#regis-form').submit(function (event) {
        event.preventDefault();

        // form check
        const password = $('#password').val();
        const repeatPassword = $('#repeat_password').val();
        const email = $('#email').val();
        const confirmEmail = $('#confirm_email').val();
        const phone = $('#phone').val();
        const zip = $('#zip').val();

        if (password !== repeatPassword) {
            alert('Password and Repeat Password do not match');
            return;
        }
        if (email !== confirmEmail) {
            alert('Email and Confirm Email do not match');
            return;
        }
        if (phone.length !== 10) {
            alert('Phone Number should be 10 digits');
            return;
        }
        if (zip.length !== 5) {
            alert('Zip Code should be 5 digits');
            return;
        }

        const formData = $(this).serialize();
        // create new visitor profile
        const request1 = $.ajax({
            url: 'http://127.0.0.1:8000/api/data_models/visitor/',
            type: 'POST',
            data: formData,
        });

        //create new user login profile
        const request2 = $.ajax({
            url: 'http://127.0.0.1:8000/api/data_models/user/',
            type: 'POST',
            data: formData,
        });

        // Create a promise that resolves when both requests complete successfully
        Promise.all([request1, request2])
            .then(function (responses) {
                alert("Register success!");
                window.location.href = "/login.html";
            })
            .catch(function (error) {
                alert("Error: " + error);
            });
    });
});

function validationFormdata(formData) {
    let fields = ["full_name", "password", "repeat_password", "email", "confirm_email", "birthday_date", "phone", "address", "city", "states", "zip", "membership", "account_type"];
  
    for (let i = 0; i < fields.length; i++) {
      let fieldValue = formData[fields[i]];
      if (fieldValue === undefined) {
        alert(`Please fill in ${fields[i]} field`);
        return false;
      }
    }
    return true;
  }
  
  