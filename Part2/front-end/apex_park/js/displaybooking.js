// // Your JSON data
// var data = [{      "hotel_name": "Best ipsum hotel",     
//  "booking_number": "123378673755",     
//   "room_type": "Twin room with balcony",      
//   "checkin_date": "23-05-14",      
//   "checkout_date": "30-05-14",     
//    "total_price": "$55,00"    },    
//    {     
//      "hotel_name": "Awesome hotel",     
//       "booking_number": "456789012345",      
//       "room_type": "Luxury suite",      
//       "checkin_date": "01-06-14",      
//       "checkout_date": "08-06-14",      
//       "total_price": "$200,00"    }];

// // Loop through the data and generate HTML for each booking
// // Loop through the data and generate HTML for each booking
// var showsHtml = "";
// var parkingHtml = "";
// var storesHtml = "";
// for (var i = 0; i < data.length; i++) {
// 	var booking = data[i];
// 	var html = '<article class="bookings">';
// 	html += '<h2><a href="#">' + booking.hotel_name + '</a></h2>';
// 	html += '<div class="b-info">';
// 	html += '<table>';
// 	html += '<tr><th>Booking number</th><td>' + booking.booking_number + '</td></tr>';
// 	html += '<tr><th>Room</th><td>' + booking.room_type + '</td></tr>';
// 	html += '<tr><th>Check-in Date</th><td>' + booking.checkin_date + '</td></tr>';
// 	html += '<tr><th>Check-out Date</th><td>' + booking.checkout_date + '</td></tr>';
// 	html += '<tr><th>Total Price:</th><td><strong>' + booking.total_price + '</strong></td></tr>';
// 	html += '</table></div>';
// 	html += '<div class="actions">';
// 	html += '<a href="#" class="gradient-button">Change booking</a>';
// 	html += '<a href="#" class="gradient-button">Cancel booking</a>';
// 	html += '<a href="#" class="gradient-button">View confirmation</a>';
// 	html += '<a href="#" class="gradient-button">Print confirmation</a>';
// 	html += '</div></article>';

//   showsHtml += html;
// 	parkingHtml += html;
// 	storesHtml += html;
// }

// // Add the generated HTML to the correct section
// document.getElementById("shows-container").innerHTML = showsHtml;
// document.getElementById("parking-container").innerHTML = parkingHtml;
// document.getElementById("stores-container").innerHTML = storesHtml;

var data = [];
// Fetch the data from the backend API
fetch('http://127.0.0.1:8000/api/data_models/booking_details/' + sessionStorage.getItem('userId'), {
  method: 'GET'
})
  .then(response => response.json())
  .then(json => {
    data = json;
    console.log(data)
    // Loop through the data and generate HTML for each booking
    var showsHtml = "";
    var parkingHtml = "";
    var storesHtml = "";
    for (var i = 0; i < data.show.length; i++) {
      var booking = data.show[i];
      var html = '<article class="bookings">';

      var timeIn = new Date(booking.start_time).toLocaleString().replace(',','');
      var timeOut = new Date(booking.end_time).toLocaleString().replace(',','');


      html += '<h2><a href="#">' + booking.show_name + '</a></h2>';
      html += '<div class="b-info">';
      html += '<table>';
      html += '<tr><th>Show Description</th><td>' + booking.show_description + '</td></tr>';
      html += '<tr><th>Show Type</th><td>' + booking.show_type + '</td></tr>';
      html += '<tr><th>Time In</th><td>' + timeIn + '</td></tr>';
      html += '<tr><th>Time Out</th><td>' + timeOut + '</td></tr>';
      html += '<tr><th>Show Price:</th><td><strong>$</strong>' + booking.show_price + '</td></tr>';
      html += '</table></div>';
      html += '<div class="actions">';
      html += '<a href="#" class="gradient-button">Book Tickets</a>';
      html += '</div></article>';

      showsHtml += html;
    }
    for (var i = 0; i < data.park.length; i++) {
      var parking = data.park[i];
      var timeIn = new Date(parking.time_in).toLocaleString().replace(',','');
      var timeOut = new Date(parking.time_out).toLocaleString().replace(',','');

      var html = '<article class="bookings">';
      html += '<h2><a href="#">Parking Spot ' + parking.spot + ' in Lot ' + parking.lot + '</a></h2>';
      html += '<div class="b-info">';
      html += '<table>';
      html += '<tr><th>Time In</th><td>' + timeIn + '</td></tr>';
      html += '<tr><th>Time Out</th><td>' + timeOut + '</td></tr>';
      html += '<tr><th>Fee</th><td><strong>$</strong>' + parking.fee + '</td></tr>';
      html += '</table></div>';
      html += '<div class="actions">';
      html += '<a href="#" class="gradient-button">Reserve Spot</a>';
      html += '</div></article>';

      parkingHtml += html;
    }
    for (var i = 0; i < data.store.length; i++) {
      var store = data.store[i];
      var html = '<article class="bookings">';
      html += '<h2><a href="#">' + store.store_name + '</a></h2>';
      html += '<div class="b-info">';
      html += '<table>';
      html += '<tr><th>Category</th><td>' + store.category + '</td></tr>';
      html += '</table></div>';
      html += '<div class="actions">';
      html += '<a href="#" class="gradient-button">Visit Store</a>';
      html += '</div></article>';

      storesHtml += html;
    }

    // Add the generated HTML to the correct section
    document.getElementById("shows-container").innerHTML = showsHtml;
    document.getElementById("parking-container").innerHTML = parkingHtml;
    document.getElementById("stores-container").innerHTML = storesHtml;
  })
  .catch(error => console.error(error));
