localStorage.removeItem('token');
document.getElementById('email-form').addEventListener('submit', async function(event) {
    event.preventDefault();
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const error_message = document.getElementById('error-message');
    const formData = new FormData();
    formData.set('username', email);
    formData.set('password', password);
    axios.post(
        '/auth/jwt/login',
        formData,
        {
            headers: {
                'Content-Type': 'multipart/form-data',
            },
        },
    )
    .then(response => {
        if (response.status === 200) {
            localStorage.setItem('token', response.data.access_token);
            window.location.href = '/storage';
            console.log(response);
        }
    })
    .catch(error => {
        error_message.textContent = 'Неправильный логин или пароль';
        console.log(error);
    });
})
