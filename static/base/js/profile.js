let body = document.querySelector("header");
let checktoken = localStorage.getItem('token')
if (!checktoken) {
    window.location.href = '/login';
  }
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
            localStorage.setItem('role', profiledata.role)
            let profilename = profiledata.second_name + " " + profiledata.first_name[0] + ".";
            const header = document.querySelector('h1');
            const profile = document.getElementById('profile-name');
            const first_name =  document.getElementById('first-name');
            const second_name =  document.getElementById('second-name');
            const email =  document.getElementById('email');
            const phone =  document.getElementById('phone');
            header.innerText = profiledata.role;
            profile.innerText = profilename;
            first_name.innerText = profiledata.first_name;
            second_name.innerText = profiledata.second_name;
            email.innerText = profiledata.email;
            phone.innerText = profiledata.phone;
        }
    })
    .catch(error => {
        console.log(error.response);
        console.log();
        if (error.response.data.detail == 'Unauthorized') {
            window.location.href = '/login';
        }
    });

function show_profile(){
    profile_data_container.style.display = 'flex';
    const nameRect = profile.getBoundingClientRect();

    profile_data_container.style.right = '32px';
    profile_data_container.style.top = nameRect.bottom + 'px';
}

const profile_data_container = document.getElementById('profile-data');
const profile = document.getElementById('profile-name');
profile.addEventListener('mouseenter', () => {
    show_profile()
});

profile_data_container.addEventListener('mouseenter', () => {
    show_profile()
  });
  
profile.addEventListener('mouseleave', () => {
  profile_data_container.style.display = 'none';
});

profile_data_container.addEventListener('mouseleave', () => {
    profile_data_container.style.display = 'none';
  });

const logout_link = document.getElementById('logout');
logout_link.addEventListener('click', () => {
    let token = localStorage.getItem('token')
    console.log(token)
    axios.post(
        '/auth/jwt/logout',{},  
        {
            headers: {
                'Authorization': 'Bearer ' + token
            },
        })
    .then(response => {
        if (response.status === 204) {
            localStorage.removeItem('token');
            console.log("exit")
            window.location.href = '/login';
        }
    }).catch(error => {
        console.log(error)
        localStorage.removeItem('token');
        console.log("erroerretgregrefbgefdsb")
        window.location.href = '/login';
        })
  });
