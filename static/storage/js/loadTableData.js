var qrCodeContainer = document.getElementById('qr-modal-container');
let token = localStorage.getItem('token');
const table = document.querySelector("table")
const notFoundImg = document.getElementById("not-found")
console.log(token)
function loadTableData() {
    axios.get(
        '/api/boxes',
        {
            headers: {
                'Authorization': 'Bearer ' + token
            },
        },
    )
    .then(response => {
        if (response.status === 200) {
            console.log(response.data);
            notFoundImg.style.display = 'none';
            table.innerHTML = `
            <thead>
                <tr>
                    <th scope="col" class="id">ID</th> 
                    <th scope="col" class="state">Статус</th>
                    <th scope="col" class="size">Размер</th>
                    <th scope="col" class="adres">Адрес</th>
                    <th scope="col" class="client">Клиент</th>
                    <th scope="col" class="phone-number">Телефон</th>
                    <th scope="col" class="courier">Курьер</th>
                </tr>
            </thead>
            <tbody>`;
            const tableTbody = document.querySelector("table > tbody")
            const data = response.data
            for (const item of data) {
            let className;
            if (item.status === 'Завершен') {
                className = 'state-done';
            } else if (item.status === 'Доставка') {
                className = 'state-delivery';
            } else {
                className = 'state-new';
            }
            const row = document.createElement('tr');
                row.innerHTML = `<th scope="row" class="id">${item.id}</th>
                    <td class="state"> <div class=${className}>${item.status}</div> </td>
                    <td class="size">${item.size}</td>
                    <td class="adres">${item.address}</td>
                    <td class="client">${item.client}</td>
                    <td class="phone-number">${item.phone}</td>
                    <td class="courier">${item.courier}</td>`;
                tableTbody.appendChild(row);
            }
        } 
    })
    .catch(error => {
    if (error.status === 404) {
        console.log(404)
        notFoundImg.style.display = 'flex'
        table.set.innerHTML = ``;
        table.style.display = 'none';
    };
    console.log(error.response);
    console.log();

    if (error.response.data.detail == 'Unauthorized'){
        window.location.href = '/login';
    }
    });
}
loadTableData();
setInterval(loadTableData, 15000);
