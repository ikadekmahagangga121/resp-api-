from flask import Flask, request, jsonify

app = Flask(__name__)

# Contoh data sementara
data = [
    {"id": 1, "nama": "Data 1"},
    {"id": 2, "nama": "Data 2"},
    {"id": 3, "nama": "Data 3"}
]

# Endpoint untuk menambahkan data
@app.route('/api/data', methods=['POST'])
def add_data():
    new_data = request.json
    data.append(new_data)
    return 'Data berhasil ditambahkan', 201

# Endpoint untuk mendapatkan data
@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(data)

# Endpoint untuk menampilkan data berdasarkan ID
@app.route('/api/data/<int:data_id>', methods=['GET'])
def show_data(data_id):
    for item in data:
        if item['id'] == data_id:
            return jsonify(item)
    return 'Data tidak ditemukan', 404

# Endpoint untuk menghapus data berdasarkan ID
@app.route('/api/data/<int:data_id>', methods=['DELETE'])
def delete_data(data_id):
    for item in data:
        if item['id'] == data_id:
            data.remove(item)
            return 'Data dengan ID {} berhasil dihapus.'.format(data_id)
    return 'Data tidak ditemukan', 404

# Menjalankan aplikasi Flask
if __name__ == '__main__':
    app.run(debug=True)
