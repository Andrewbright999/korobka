async function generateQRCode(box_id) {
    let int_id = parseInt(box_id)
    console.log(typeof int_id)
    var qrCodeElement = document.getElementById('qr-code');
    var boxIdElement = document.getElementById('box-id');
    qrCodeElement.innerHTML = ""; // Очистить предыдущий QR-код, если он есть
    // const url = await QRCode.toDataURL(int_id, { errorCorrectionLevel: 'H' });
    // const img = document.createElement('img');
    // img.src = url;
    // img.width = 245;
    // img.height = 245;
    // qrCodeElement.appendChild(img);

    var qr = qrcode(3, 'H');
    qr.addData(box_id);
    qr.make();
    var img = document.createElement('img');
    img.src = qr.createDataURL();
    img.width = 600;
    img.height = 600;
    img.style.width = '230px';
    img.style.height = '230px';
    qrCodeElement.appendChild(img);



    qrCodeContainer.style.display = 'flex';
        var boxIdElement = document.getElementById('box-id');
        boxIdElement.innerText = 'ID: ' + box_id;
        var printBtn = document.getElementById('print-btn');
        var qrCodeModal = document.getElementById('qr-modal-container');
        qrCodeModal.onclick = function() {
            qrCodeContainer.style.display = 'none';
        };
        printBtn.onclick = function() {
            printQRCode(box_id);
        };
};

function printQRCode(boxId) {
    var qrCodeElement = document.getElementById('qr-code');
    var boxIdElement = document.getElementById('box-id');
    var printWindow = window.open('', 'Print QR Code', 'height=600,width=800');
    printWindow.document.write('<html><head><title>Print QR Code</title>');
    printWindow.document.write('</head><body>');
    printWindow.document.write('<div style="text-align: center;">');
    printWindow.document.write(qrCodeElement.innerHTML);
    printWindow.document.write('<div font-family="Onest" font-weight="600">ID: ' + boxId + '</div>');
    printWindow.document.write('</div>');
    printWindow.document.write('</body></html>');
    printWindow.document.close();
    printWindow.print();
    console.log();
}



var form = document.getElementById('create-box-form');
var qrCodeContainer = document.getElementById('qr-code-container');
form.addEventListener('submit', async function(event) {
    event.preventDefault();
    var data = {
        size: this.size.value,
        client: this.client.value,
        phone: this.phone.value,
        address: this.address.value
    };
    
    axios.post('/api/boxes', data, {
        headers: {
            'Authorization': 'Bearer ' + token
        },
    })
    .then(function(response) {
        var boxId = response.data.box_id.toString();
        generateQRCode(boxId);
        loadTableData();
        form.reset();
        document.getElementById('size-s').checked = true;
    })
    .catch(function(error) {
        console.error(error);
    });
});