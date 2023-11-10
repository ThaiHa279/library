function load_categories() {
    fetch('http://localhost:8000//api-book/genres/', {
        method: 'GET', // or 'POST'
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then(response => response.json())
    .then(data => {
        for (let i=1; i< 50; i++) {
            $("#list_categories").append(`
                <li class="cat-item">
                    <a class="query" onclick={fillter(${data[i].id})} href="#">${data[i].name}</a>
                </li>
            `);
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function load_name() {
    let name = sessionStorage.getItem('name');
    console.log(name);
    if (name) {
        $('#name').text(name);
    }
}

function borrow_book(book_id) {
    let user_id = sessionStorage.getItem('id');
    let data = {
        "user_id": user_id,
        "book_id": book_id
    }
    console.log(data);
    fetch(`http://localhost:8000/api-user/borrow`, {
        method: 'POST', // or 'POST'
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        alert(data)
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function load_book(url) {
    fetch(url, {
        method: 'GET', // or 'POST'
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then(response => response.json())
    .then(data => {
        
        $('#list_book').empty();
        data.results.map((book) => {
            $("#list_book").append(`
                <div class="col-lg-4 col-md-6">
                    <div class="product-card mb-4">
                        <div class="image-holder d-flex align-items-center justify-content-center " style="height: 400px;">
                            <img class="mx-auto d-block" src="https://www.jstor.org/cover-image/${book.book_id}" alt="product-item" class="img-fluid">
                        </div>
                        <div class="card-detail text-center pt-3 pb-2">
                        <h5 class="card-title fs-4 text-uppercase m-0">
                            <a href="https://www.jstor.org/stable/${book.book_id}">${book.title}</a>
                        </h5>
                        <div class="cart-button mt-1">
                            <a onclick="borrow_book(${book.id})" href=#" class="btn">Borrow</a>
                        </div>
                        </div>
                    </div>
                </div>
            `);
        });
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function load_history() {
    let id = sessionStorage.getItem('id');
    fetch(`http://localhost:8000/api-user/view_history?user_id=${id}`, {
        method: 'GET', // or 'POST'
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then(response => response.json())
    .then(data => {
        data = JSON.parse(data);
        console.log(data);
        data.map((book) => {
            if (book[1] != 'paid') {
                $("#cart").append(`
                <li class="list-group-item bg-transparent border-gray d-flex justify-content-between lh-sm">
                    <div>
                    <h5 class="card-title fs-3 text-uppercase mb-0">
                        <a href="#">${book[0]}</a>
                    </h5>
                    </div>
                </li>`)
            }

        })
    })
    .catch((error) => {
        console.error('Error:', error);
    });

    fetch(`http://localhost:8000/api-user/cal_fee?user_id=${id}`, {
        method: 'GET', // or 'POST'
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        $("#total").text(data)
    })
    .catch((error) => {
        console.error('Error:', error);
    });
    
}

function search(e) {
    e.preventDefault();
    e.stopPropagation();
    let formData = $("#search_input").val();
    let url = `http://127.0.0.1:8000/api-book/book/?title=${formData}`;
    load_book(url);
}

function fillter(genre_id) {
    let url = `http://127.0.0.1:8000/api-book/book/?genre_id=${genre_id}&?page=1`;
    load_book(url);
}

window.onload = function() {
    load_name();
    load_categories();
    let url = 'http://127.0.0.1:8000/api-book/book/?page=1';
    load_book(url);
    $('#search_form').on('submit', (e) => search(e))

    $('#submit').click(function(event) {
        event.preventDefault();
        $('#search_form').submit();
    }) 

    $('.query').click(function(event){
        event.preventDefault();
        console.log(1);
    });

    load_history();
}