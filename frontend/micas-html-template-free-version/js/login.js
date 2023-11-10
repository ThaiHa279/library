const signup_form = document.getElementById('signup_form');
const signin_form = document.getElementById('signin_form');
const name = document.getElementById('name');

signup_form.addEventListener('submit', (e) => {
    e.preventDefault();
    e.stopPropagation();
    let formData = $("#signup_form").serializeArray();
    signup(formData)
});

signin_form.addEventListener('submit', (e) => {
    e.preventDefault();
    e.stopPropagation();
    let formData = $("#signin_form").serializeArray();
    signin(formData)
});

function signup(data) {
    data = data.reduce((acc, cur) => {
        acc[cur.name] = cur.value;
        return acc;
      }, {});
      
    console.log(data);
    fetch('http://localhost:8000/api-user/signup', {
        method: 'POST', // or 'POST'
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data =>  {
        alert("Đăng ký thành công.")
        sessionStorage.setItem('name', data.user.name)
        sessionStorage.setItem('id', data.user.id)
    })
    .catch((error) => {
        console.error('Error:', error);
    });

}

function signin(data) {
    data = data.reduce((acc, cur) => {
        acc[cur.name] = cur.value;
        return acc;
      }, {});
      
    console.log(data);
    fetch('http://localhost:8000/api-user/login', {
        method: 'POST', // or 'POST'
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        alert("Đăng nhập thành công.")
        sessionStorage.setItem('name', data.user.name)
        sessionStorage.setItem('id', data.user.id)
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

 