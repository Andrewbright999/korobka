let body = document.querySelector("header");
axios.get(
    '/users/profile',
    {
        headers: {
            'Authorization': 'Bearer ' + localStorage.getItem('token')
        },
    }
)
    .then(response => {
        if (response.status === 200) {
            console.log(response.data);
            const profiledata = response.data;
            let profilename = profiledata.second_name + " " + profiledata.first_name[0] + ".";
            const header = document.querySelector('h1');
            const profile = document.getElementById('profile-name');
            header.innerText = profiledata.role;
            profile.innerText = profilename;
        }
    })
    .catch(error => {
        console.log(error.response);
        console.log();
        if (error.response.data.detail == 'Unauthorized') {
            window.location.href = '/login';
        }
    });
