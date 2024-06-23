const regForm = document.getElementById('form-container');
let token = localStorage.getItem('token');
const table = document.querySelector("table")
const forbiddenImg = document.getElementById("no-admin")
console.log(token)
function loadTableData() {
    if (!token) {
        window.location.href = '/login';
      }
    axios.get(
        '/users',
        {
            headers: {
                'Authorization': 'Bearer ' + token
            },
        },
    )
    .then(response => {
        if (response.status === 200) {
            console.log(response.data);
            forbiddenImg.style.display = 'none';
            table.style.display = 'block';
            regForm.style.display = 'flex';
            table.innerHTML = `
            <thead>
                <tr>
                    <th scope="col" class="id">ID</th> 
                    <th scope="col" class="client">Имя</th>
                    <th scope="col" class="client">Фамилия</th>
                    <th scope="col" class="client">Роль</th>
                    <th scope="col" class="phone-number">Телефон</th>
                    <th scope="col" class="phone-number">Email</th>
                </tr>
            </thead>
            <tbody>`;
            const tableTbody = document.querySelector("table > tbody")
            const data = response.data
            for (const item of data) {
            const row = document.createElement('tr');
                row.innerHTML = `<th scope="row" class="id">${item.id}</th>
                    <td class="client">${item.first_name}</td>
                    <td class="client">${item.second_name}</td>
                    <td class="client">${item.role}</td>
                    <td class="phone-number">${item.phone}</td>
                    <td class="phone-number">${item.email}</td>`;
                tableTbody.appendChild(row);
            }
        } 
    })
    .catch(error => {
    if (error.status === 403) {
        console.log(403)

    };
    console.log(error.response);
    console.log();
    forbiddenImg.style.display = 'flex';
    table.innerHTML = ``;
    table.style.display = 'none';
    regForm.style.display = 'none';


    if (error.response.data.detail == 'Unauthorized'){
        window.location.href = '/login';
    }
    });
}
loadTableData();
setInterval(loadTableData, 15000);
