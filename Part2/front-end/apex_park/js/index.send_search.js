const form = document.querySelector('#main-search');


const BURL = 'http://127.0.0.1:8000/'
form.addEventListener('submit', (event) =>{
    event.preventDefault();

    const formData = new FormData(form);

    fetch(BURL+'api/search_bar/', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log(response)
    })
    .catch(error => {
        console.log(error)
    });

    form.submit();
});