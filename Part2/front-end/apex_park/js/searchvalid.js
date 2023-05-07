function valid(formData) {
    const radioValue = formData.get('radio');
    const ticketDateValue = formData.get('ticket_date');
    const ticketCValue = formData.get('ticket_c');
    const ticketAValue = formData.get('ticket_a');
    const ticketSValue = formData.get('ticket_s');
    const showDateValue = formData.get('show_date');
    const showCValue = formData.get('show_c');
    const showAValue = formData.get('show_a');
    const showSValue = formData.get('show_s');
    const storeCategoryValue = formData.get('store_category');
    const parkPlaceValue = formData.get('park_place');
  
    if (
      radioValue === 'form1' &&
      (ticketDateValue === '' ||
        (ticketDateValue !== '' &&
          ticketCValue === '' &&
          ticketAValue === '' &&
          ticketSValue === ''))
    ) {
      return false;
    } else if (
      radioValue === 'form2' &&
      (showDateValue === '' ||
        (showDateValue !== '' &&
          showCValue === '' &&
          showAValue === '' &&
          showSValue === ''))
    ) {
      return false;
    } else if (radioValue === 'form3' && storeCategoryValue === 'Select choice') {
      return false;
    } else if (radioValue === 'form4' && parkPlaceValue === 'Select choice') {
      return false;
    }
    return true;
  }
  