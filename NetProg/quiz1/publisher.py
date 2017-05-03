import socket
import json
# Inisialisasi socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect
sock.connect(('127.0.0.1', 4444))
# Terima input dari user
topik = raw_input("Masukkan topiknay: ")
konten = raw_input("Masukkan konten: ")
# Buat dictionary
dict_msg = {
    "tipe": "PUB",
    "topik": topik,
    "konten": konten
}
# Serialisasi ke string
msg = json.dumps(dict_msg)
# Kirim ke broker
sock.send(msg)
data = sock.recv(100)
print data
# Close koneksi
sock.close()
