import socket
import json

# Inisialisasi socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('127.0.0.1', 4444))

# Ambil input topik dari user
topik = raw_input("Masukkan topiknya : ")
# Buat dictionary message
dict_msg = {
    'topik': topik,
    'tipe': 'SUB'
}
# Serialisasi ke string
msg = json.dumps(dict_msg)
# Kirim ke broker
sock.send(msg)
# Receive status from broker
status = sock.recv(100)
# Cek status
if status == "OK":
    print "Subscribe berhasil"
else:
    print "Subscribe gagal"

try:
    while True:
        data = sock.recv(100)
        print data
except KeyboardInterrupt:
    print "Client Terminated"
