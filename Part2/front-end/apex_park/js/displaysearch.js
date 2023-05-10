const show_information = [
    {
      "id": 1,
      "show_name": "The Phantom of the Opera",
      "show_price": 100
    },
    {
      "id": 2,
      "show_name": "Hamlet",
      "show_price": 75
    },
    {
      "id": 3,
      "show_name": "The Lion King",
      "show_price": 125
    },
    {
      "id": 4,
      "show_name": "The Addams Family",
      "show_price": 90
    },
    {
      "id": 5,
      "show_name": "Sweeney Todd: The Demon Barber of Fleet Street",
      "show_price": 110
    },
    {
      "id": 6,
      "show_name": "The Crucible",
      "show_price": 80
    },
    {
      "id": 7,
      "show_name": "Wicked",
      "show_price": 130
    },
    {
      "id": 8,
      "show_name": "The Book of Mormon",
      "show_price": 95
    },
    {
      "id": 9,
      "show_name": "Death of a Salesman",
      "show_price": 85
    },
    {
      "id": 10,
      "show_name": "The Rocky Horror Picture Show",
      "show_price": 70
    },
    {
      "id": 11,
      "show_name": "The Exorcist",
      "show_price": 120
    },
    {
      "id": 12,
      "show_name": "The Importance of Being Earnest",
      "show_price": 95
    },
    {
      "id": 13,
      "show_name": "Cats",
      "show_price": 110
    },
    {
      "id": 14,
      "show_name": "Dracula",
      "show_price": 80
    },
    {
      "id": 15,
      "show_name": "The Sound of Music",
      "show_price": 125
    },
    {
      "id": 16,
      "show_name": "A Midsummer Nights Dream",
      "show_price": 90
    },
    {
      "id": 17,
      "show_name": "Jekyll and Hyde",
      "show_price": 100
    },
    {
      "id": 18,
      "show_name": "The Great Gatsby",
      "show_price": 85
    },
    {
      "id": 19,
      "show_name": "Little Shop of Horrors",
      "show_price": 95
    },
    {
      "id": 20,
      "show_name": "A Streetcar Named Desire",
      "show_price": 90
    },
    {
      "id": 21,
      "show_name": "The Rocky Horror Show",
      "show_price": 70
    },
    {
      "id": 22,
      "show_name": "Carrie",
      "show_price": 80
    },
    {
      "id": 23,
      "show_name": "The Importance of Being Earnest",
      "show_price": 95
    },
    {
      "id": 24,
      "show_name": "Les Mis茅rables",
      "show_price": 130
    },
    {
      "id": 25,
      "show_name": "The Glass Menagerie",
      "show_price": 85
    }
   ];
function getIdByShowName(show_name) {
  for (let i = 0; i < show_information.length; i++) {
    if (show_information[i].show_name === show_name) {
      return show_information[i].id;
    }
  }
  return null;
}
function getPriceByid(id) {
    for (let i = 0; i < show_information.length; i++) {
      if (show_information[i].id === id) {
        return show_information[i].show_price;
      }
    }
    return 0;
  }

function calculateTotalPrice(booking_info) {

    if(booking_info.form == 'park'){
        return Math.floor(Math.random() * 20) + 1;
    }

    if(booking_info.form == 'show'){
        show_id = getIdByShowName(booking_info.show_select);
        show_price = getPriceByid(show_id);
        return show_price;
    }
    const basePrice = 50;
    let totalPrice = 0;

    const date = new Date(booking_info.tdate);
    const dayOfWeek = date.getDay();
    const isWeekend = dayOfWeek === 0 || dayOfWeek === 6;
    const isHoliday = false; // You can implement this if you want

    if (!isWeekend && !isHoliday) {
        const numAdults = parseInt(booking_info.tadults);
        const numChildren = parseInt(booking_info.tchildren);
        const numSeniors = parseInt(booking_info.tsenior);

        totalPrice += (numAdults + numChildren) * basePrice;
        totalPrice += numSeniors * basePrice * 0.85; // 15% discount for seniors
        totalPrice *= 0.95; // 5% discount for online purchase
    }

    return totalPrice;
}

// assuming that data1, data2, and data3 are defined

// get the booking details container element
const bookingDetailsContainer = document.getElementById("booking-info");

// get the total price element
const totalPriceElement = document.getElementById("total-price");

// set default values for the booking details
let bookingDetailsHtml = "";
var booking_info = JSON.parse(sessionStorage.getItem('booking_information'));
//console.log(booking_info)
// check the form type and set the booking details accordingly
switch (booking_info.form) {
    case "ticket":
        bookingDetailsHtml += `<dt></dt><dd><strong>${booking_info.form.toUpperCase()}</strong></dd>
                            <dt>Ticket Date</dt><dd>${booking_info.tdate}</dd>
                            <dt>Children (15% discount): </dt><dd>${booking_info.tchildren}</dd>
                            <dt>Adults: </dt><dd>${booking_info.tadults}</dd>
                            <dt>Senior (15% discount): </dt><dd>${booking_info.tsenior}</dd>`;

        // set the total price
        var total_price = calculateTotalPrice(booking_info)
        totalPriceElement.textContent = `Total Price: $${total_price}`;

        break;
    case "show":
        bookingDetailsHtml += `<dt>Show</dt><dd>${booking_info.show_select}</dd>
                            <dt>Date</dt><dd>${booking_info.sdate}</dd>
                            <dt>People</dt><dd>${booking_info.sp}</dd>`;
        var total_price = calculateTotalPrice(booking_info) * parseInt(booking_info.sp);
        totalPriceElement.textContent = `Total Price: $${total_price}`;
        break;
    case "park":
        bookingDetailsHtml += `<dt>Parking order</dt><dd></dd>
                            <dt>Slot</dt><dd>${booking_info.park_place}</dd>
                            <dt>In date</dt><dd>${booking_info.park_in_date}</dd>
                            <dt>In time</dt><dd>${booking_info.park_in}</dd>
                            <dt>Out date</dt><dd>${booking_info.park_out_date}</dd>
                            <dt>Out time</dt><dd>${booking_info.park_out}</dd>`;
        var total_price = calculateTotalPrice(booking_info);
        totalPriceElement.textContent = `Total Price: $${total_price}`;
        break;
}

// set the booking details HTML
bookingDetailsContainer.innerHTML = bookingDetailsHtml;


// //remove from local storage:
// sessionStorage.removeItem('booking_information')

var visitor_id = sessionStorage.getItem('visitorId');
var order_date =  new Date().toISOString();
var orderdata = {
    order_date: order_date,
    xzz_visitor: visitor_id,
}; 
const API = 'http://127.0.0.1:8000/';

const submitButton = document.querySelector('#next-step');
const paymentform = document.querySelector('#payment');
console.log("paymentform", paymentform)


submitButton.addEventListener('click', (event) => {
    event.preventDefault();
    
    // First create new order and get order_id back
    $.ajax({
        url: API+'api/data_models/order/',
        method: 'POST',
        data: orderdata,
    }).then(function (response1) {
      sessionStorage.setItem('order_id', response1.order_id)
      const checkbox = document.querySelector('#cash');
      if (checkbox.checked) {
        data_payment = {
          payment_amount: total_price.toFixed(2),
          payment_method: 'CA',
          order: '' + response1.order_id
        }
      } else {
        var card_type = paymentform.querySelector("select[name=card_type]").value;
        var card_number = paymentform.querySelector("input[name=card_number]").value;
        var name_on_card = paymentform.querySelector("input[name=card_holder]").value;
        var expiration_date = paymentform.querySelector("input[name=expiration_date]").value;
        var cvv = paymentform.querySelector("input[name=cv2_number]").value;
        const date = new Date(expiration_date);
        const formattedDate = date.toISOString();
        data_payment = {
          payment_method: card_type,
          payment_amount: total_price.toFixed(2),
          card_number: card_number,
          name_on_card: name_on_card,
          expiration_date: formattedDate,
          cvv: cvv,
          order: '' + response1.order_id
        }
      }


      return $.ajax({
        url: API + 'api/data_models/payment/',
        method: 'POST',
        data: data_payment,
      });
    })
    .then(function(response2) {
        switch (booking_info.form) {
            case 'ticket':
                const ticketdate = new Date(booking_info.tdate);
                const formattedticketDate = ticketdate.toISOString();
                ticket_record = {
                    ticket_method: 'Online',
                    visit_date: formattedticketDate,
                    ticket_price: total_price.toFixed(2),
                    order: sessionStorage.getItem('order_id'),
                    visitor: visitor_id
                };
                return $.ajax({
                    url: API + 'api/data_models/ticket/',
                    method: 'POST',
                    data: ticket_record,
                  });
                
            case 'show':
                const showName = booking_info.show_select;
                const showId = getIdByShowName(showName);

                const show_name_data = {
                    show: showId,
                    order: sessionStorage.getItem('order_id')
                };
                return $.ajax({
                    url: API + 'api/data_models/show_order/',
                    method: 'POST',
                    data: show_name_data,
                  });
                
            case 'park':
                const [day, month, year] = booking_info.park_in_date.split('/');
                const p_time_in = new Date(`${year}-${month}-${day}T${booking_info.park_in}`);
                const formattedp_time_in = p_time_in.toISOString();

                const [day1, month1, year1] = booking_info.park_out_date.split('/');
                const p_time_out = new Date(`${year1}-${month1}-${day1}T${booking_info.park_out}`);
                const formattedp_time_out = p_time_out.toISOString();

                const park_record = {
                    lot: booking_info.park_place,
                    spot: 1,
                    time_in: formattedp_time_in,
                    time_out: formattedp_time_out,
                    fee: total_price.toFixed(2),
                    order: sessionStorage.getItem('order_id')
                };
                return $.ajax({
                    url: API + 'api/data_models/parking/',
                    method: 'POST',
                    data: park_record,
                  });
                
            default:
                console.log('Invalid booking form');
                break;
        }
    })
    .then(function() {
      //change window after all things has submit:
      window.location.href = '/my_account.html'
    });
});

