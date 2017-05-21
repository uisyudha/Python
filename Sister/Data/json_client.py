# Import lib
import socket
import json

# Inisilisasi socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Koneksi ke ip dan port server
sock.connect(('127.0.0.1', 7887))

# Struktur data yang akan di kirim
data = {
    'NamaKelompok': [
        'Uis Yudha',
        'Landika Hari',
        'Hilman Nihri',
        'Suhadak Akbar'
    ],
    'NIM' : [
        '145150200111176',
        '145150201111156',
        '145150201111145',
        '145150207111086'
    ]
}

# Encode data (marshalling)
str_data = json.dumps(data)

sock.send(str_data)

sock.close()



