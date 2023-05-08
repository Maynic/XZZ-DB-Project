var data = [];
// Fetch the data from the backend API
fetch('http://127.0.0.1:8000/api/data_models/booking_details/' + sessionStorage.getItem('userId'), {
  method: 'GET'
})
  .then(response => response.json())
  .then(json => {
    data = json;
    //console.log(data)
    // Loop through the data and generate HTML for each booking
    var ticketsHTML = "";
    var showsHtml = "";
    var parkingHtml = "";
    var storesHtml = "";
    for (var i = 0; i < data.ticket.length; i++) {
      var tickets = data.ticket[i];
      console.log(tickets)
      var html = '<article class="bookings">';

      var ticket_date = new Date(tickets.visit_date).toLocaleString().replace(',','');


      html += '<h2><th>Order Number  #</th><a href="#">' + tickets.order_number + '</a></h2>';
      html += '<div class="b-info">';
      html += '<table>';
      html += '<tr><th>Ticket Type</th><td>' + tickets.ticket_method + '</td></tr>';
      html += '<tr><th>Visit Date</th><td>' + tickets.visit_date + '</td></tr>';
      html += '<tr><th>Purchase price</th><td><strong>$</strong>' + tickets.ticket_price + '</td></tr>';
      html += '</table></div></article>';

      ticketsHTML += html;
    }
    for (var i = 0; i < data.show.length; i++) {
      var show = data.show[i];
      var html = '<article class="bookings">';

      var timeIn = new Date(show.start_time).toLocaleString().replace(',','');
      var timeOut = new Date(show.end_time).toLocaleString().replace(',','');


      html += '<h2><a href="#">' + show.show_name + '</a></h2>';
      html += '<div class="b-info">';
      html += '<table>';
      html += '<tr><th>Show Description</th><td>' + show.show_description + '</td></tr>';
      html += '<tr><th>Show Type</th><td>' + show.show_type + '</td></tr>';
      html += '<tr><th>Time In</th><td>' + timeIn + '</td></tr>';
      html += '<tr><th>Time Out</th><td>' + timeOut + '</td></tr>';
      html += '<tr><th>Show Price:</th><td><strong>$</strong>' + show.show_price + '</td></tr>';
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
    document.getElementById("tickets-container").innerHTML = ticketsHTML;
    document.getElementById("shows-container").innerHTML = showsHtml;
    document.getElementById("parking-container").innerHTML = parkingHtml;
    document.getElementById("stores-container").innerHTML = storesHtml;
  })
  .catch(error => console.error(error));
