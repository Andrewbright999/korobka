var form = document.getElementById('register-form');
var messageContainer = document.getElementById('user-message-container');
form.addEventListener('submit', function(event) {
    event.preventDefault();
    var data = {
        email: this.email.value,
        password: this.password.value,
        phone:  this.phone.value,
        first_name:  this.first_name.value,
        second_name:  this.second_name.value,
        role:  this.role.value
    };
    axios.post('auth/register', data, {
        headers: {
            'Authorization': 'Bearer ' + token
        },
    })
    .then(function(response) {
        loadTableData();
        form.reset();
        messageContainer.style.display = 'flex';
        var printBtn = document.getElementById('ok-btn');
        printBtn.onclick = function() {
            messageContainer.style.display = 'none';
        };

        var Modal = document.getElementById('user-message-modal-container');
        Modal.onclick = function() {
            messageContainer.style.display = 'none';
        };

    })
    .catch(function(error) {
        console.error(error);
    });
});
