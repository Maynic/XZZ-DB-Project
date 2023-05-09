// This scripts check whether the user has logged in so that display
// LOGIN or LOGOUT botton respecitively
function getCurrentUser() {
  var isloggin = sessionStorage.getItem('userId');
  if (isloggin !== null) {
    console.log("isloggin:", isloggin)
    // user is logged in, hide login button and show logout button
    $('.login-button').hide();
    $('.logout-button').show();
    return true;
  } else {
    console.log("isloggin2", isloggin)
    // user is not logged in, show login button and hide logout button
    $('.login-button').show();
    $('.logout-button').hide();
    return false;
  }
};

// This scripts check whether the input form data is valid,
// prevent invalid search request 
// and ready for submit
function valid(formData) {
  var formid = formData.form;
  var ticketDateValue = formData.tdate;
  var ticketCValue = formData.tchildren ?? null;
  var ticketAValue = formData.tadults ?? null;
  var ticketSValue = formData.tsenior ?? null;
  var showDateValue = formData.sdate ?? null;
  var showCValue = formData.schildren ?? null;
  var showAValue = formData.sadults ?? null;
  var showSValue = formData.ssenior ?? null;
  var storeCategoryValue = formData.sstore_category ?? null;
  var parkPlaceValue = formData.park_place ?? null;
  
  if (
    formid === 'ticket' &&
    (ticketDateValue === '' ||
      (ticketDateValue !== '' &&
        ticketCValue === '' &&
        ticketAValue === '' &&
        ticketSValue === ''))
  ) {
    return false;
  } else if (
    formid === 'show' &&
    (showDateValue === '' ||
      (showDateValue !== '' &&
        showCValue === '' &&
        showAValue === '' &&
        showSValue === ''))
  ) {
    return false;
  } else if (formid === 'store' && storeCategoryValue === 'Select choice') {
    return false;
  } else if (formid === 'park' && parkPlaceValue === 'Select choice') {
    return false;
  }
  return true;
}


// This function actually translate the raw data into formated jason file
function getFormData() {
  var formId = document.querySelector('input[name="radio"]:checked').value;
  var form = document.getElementById(formId);

  if(formId === 'form1'){
    // ticket search
    var date = form.querySelector("input[name=ticket_date]").value;
    var children = form.querySelector("input[name=ticket_c]").value;
    var adults = form.querySelector("input[name=ticket_a]").value;
    var senior = form.querySelector("input[name=ticket_s]").value;
    var data = {
      form: 'ticket',
      tdate: date,
      tchildren: children,
        tadults: adults,
        tsenior: senior
    };
    //console.log(data)
    return data;
  } else if(formId === 'form2'){
    var show_select = form.querySelector("select[name=show_select]").value;
    var show_date = form.querySelector("input[name=show_date]").value;
    var children = form.querySelector("input[name=show_c]").value;
    var adults = form.querySelector("input[name=show_a]").value;
    var senior = form.querySelector("input[name=show_s]").value;
    var data = {
      form: 'show',
      show_select, show_select,
      sdate: show_date,
      schildren: children,
      sadults: adults,
      ssenior: senior
    };
    //console.log(data)
    return data;
  } else if(formId === 'form3'){
    var store_category = form.querySelector("select[name=store_category]").value;
    var data = {
      form: 'store',
      sstore_category: store_category
    };
    //console.log(data)
    return data;
  } else if(formId === 'form4'){
    var park_place = form.querySelector("select[name=park_place]").value;
    var park_in_date = form.querySelector("input[name=park_in_date]").value;
    var park_in = form.querySelector("select[name=park_in]").value;
    var park_out_date = form.querySelector("input[name=park_out_date]").value;
    var park_out = form.querySelector("select[name=park_out]").value;
    var data = {
      form: 'park',
      park_place: park_place,
      park_in_date: park_in_date,
      park_in: park_in,
      park_out_date: park_out_date,
      park_out: park_out
    };
    //console.log(data)
    return data;
  }
}

// This functiuon call the getFormData function
// Then submit the search based on different radio (search types)
function submitForm(){
  var data = getFormData();
  //console.log("data", data)
  var isFormValid = valid(data);
  //console.log(isFormValid)

  if(!isFormValid){
    alert('Do not submit empty search')
    //console.log("empty search")
    return;
  }

  if(getCurrentUser() === false) {
    alert('Please Login before using search function')
    return;
  }

  console.log(data)
  $.ajax({
    url: 'http://127.0.0.1:8000/api/data_models/search/',
    method: 'POST',
    data: data,
    success: function(response) {
      console.log("submit success")
      // handle success response from server
    },
    error: function(error) {
      console.log("submit failed")
      // handle error response from server
    }
  });
}