// script.js
fetch('/api/data')
    .then(response => response.json())
    .then(data => {
        const dataList = document.getElementById('data-list');
        data.forEach(item => {
            const listItem = document.createElement('li');
            
            // Tambahkan teks data
            const dataText = document.createElement('span');
            dataText.textContent = item.nama;
            
            // Tombol ubah data
            const editButton = document.createElement('button');
            editButton.textContent = 'Ubah';
            editButton.addEventListener('click', () => {
                // Logika untuk mengubah data
                // Misalnya, munculkan dialog pengubahan data
                console.log('Ubah data dengan ID ' + item.id);
            });
            
            // Tombol hapus data
            const deleteButton = document.createElement('button');
            deleteButton.textContent = 'Hapus';
            deleteButton.addEventListener('click', () => {
                // Logika untuk menghapus data
                // Misalnya, tampilkan konfirmasi penghapusan
                console.log('Hapus data dengan ID ' + item.id);
            });
            
            // Tambahkan elemen ke dalam item list
            listItem.appendChild(dataText);
            listItem.appendChild(editButton);
            listItem.appendChild(deleteButton);
            
            dataList.appendChild(listItem);
        });
    });
