// script.js
document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;    
    var userPass = {};
    userPass.name = username;
    userPass.password = password;

    response = fetch('http://localhost:4000/login', {
        method: 'POST',
        params: JSON.stringify({ userPass }) 
    }).then(response => response.json());
    if (response.user_id !== 0) {
        alert('Login successful!');
        // Redirect to another page or perform further actions
        sessionStorage.setItem('user_id', response.user_id[0]);
    } else {
        document.getElementById('errorMsg').innerText = 'Invalid username or password';
    }
});


document.getElementById('updateButton').addEventListener('click', () => {
    const name = 'assignment_name'; // Replace with the actual name value
    const user_id = sessionStorage.getItem('user_id');

    fetch('http://localhost:4000/update', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name }),
        params: JSON.stringify({ user_id })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = JSON.stringify(data, null, 2);
    })
    .catch(error => console.error('Error:', error));
});

document.getElementById('fetchButton').addEventListener('click', () => {
    fetch('http://localhost:4000/fetch', {
        method: 'GET'
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = JSON.stringify(data, null, 2);
    })
    .catch(error => console.error('Error:', error));
});
