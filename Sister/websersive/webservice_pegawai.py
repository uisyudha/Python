# Import lib flask
from flask import Flask, request, abort
import json

# Inisialisasi flask
app = Flask(__name__)

# Inisalisasi data pegawai di dictionary
data_pegawai = [
    {
        'id' : 1,
        'nip' : '1234',
        'nama' : 'Uis Yudha',
        'alamat' : 'Kedawung'
    },
    {
        'id' : 2,
        'nip' : '1235',
        'nama' : 'Uis Yudha T',
        'alamat' : 'Lowokwaru'
    }
]

# Definisi route dan fungsi REST Webservice
@app.route('/pegawai', methods=['GET'])
def index():
    str_pegawai = json.dumps(data_pegawai)
    return str_pegawai

@app.route('/pegawai/<int:id>', methods=['GET'])
def get_pegawai(id):
    pegawai = None
    # Cari pegawai
    for p in data_pegawai:
        if p['id'] == id:
            pegawai = p
            break
    # Tidak ada return 404
    if pegawai is None:
        abort(404)

    # Ada
    str_pegawai = json.dumps(pegawai)
    return str_pegawai

@app.route('/pegawai', methods=['POST'])
def create_pegawai():
    # Get dari dari parameter post
    nama = request.form.get('nama')
    nip = request.form.get('nip')
    alamat = request.form.get('alamat')
    # Auto increment ID pegawai
    id_terakhir = data_pegawai[-1]["id"]
    id_terakhir = id_terakhir + 1

    # Buat data pegawai baru
    pegawai_baru = {
            'id' : id_terakhir,
            'nip' : nip,
            'nama' : nama,
            'alamat' : alamat
    }


    # Insert data pegawai baru ke data_pegawai
    data_pegawai.append(pegawai_baru)
    return "OK"

@app.route('/pegawai/<int:id>', methods=['PUT'])
def update_pegawai(id):
    # Get semua data yang di post
    nama = request.form.get('nama')
    nip = request.form.get('nip')
    alamat = request.form.get('alamat')

    # Cari pegawai di dictionary
    pegawai = None
    index = 0
    for p in data_pegawai:
        if p['id'] == id:
            pegawai = p
            break
        index = index + 1

    # Tidak ketemu return 404
    if pegawai is None:
        abort(404)

    # Jika ketemu update
    pegawai['nip'] = nip
    pegawai['nama'] = nama
    pegawai['alamat'] = alamat

    data_pegawai[index] = pegawai

    # Return data pegawai baru
    str_pegawai = json.dumps(pegawai)
    return str_pegawai

@app.route('/pegawai/<int:id>', methods=['DELETE'])
def delete_pegawai(id):
    pegawai = None

    for p in data_pegawai:
        if p['id'] == id:
            pegawai = p
            break

    if pegawai is None:
        abort(404)

    data_pegawai.remove(pegawai)

    return "Deleted"

app.run(port=9997, debug=True)





