# Import lib
import socket
import pickle

# Inisiasi socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Koneksi ke ip dan port server
sock.connect(('127.0.0.1', 7887))

data =  [
            {'NamaKelompok': ('Uis Yudha', 'Landika Hari', 'Test Subject 1', 'Test Subject 2')},
            {'NIM' : ('145150200111176', '145150200111177', '12345', '123456')}
        ]


sock.send(pickle.dumps(data))

sock.close()



