"""
Pickle dapat digunakan untuk serialisasi object
Sedangkan json tidak bisa
Anda tidak percaya? Coba saja 
"""
import socket
import pickle
from Mahasiswa import *

# Inisiasi socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Koneksi ke ip dan port server
sock.connect(('127.0.0.1', 7887))

# Buat objek mahasiswa
m1 = Mahasiswa("Uis Yudha", "145150200111176")
m2 = Mahasiswa("Landika Hari", "145150200111156")
m3 = Mahasiswa("Hilman", "145150")
m4 = Mahasiswa("Akbar", "08098999")

# data yang akan dikirim berupa list object mahasiswa
data = [m1, m2, m3, m4]

# Encode data
str_data = pickle.dumps(data)

sock.send(str_data)

sock.close()



