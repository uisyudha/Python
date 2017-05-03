import socket
import json

# Inisialisasi socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

# Binding ke ipr dan port tertentu
sock.bind(('', 7887))

# Listen connection
sock.listen(10)

while True:
    conn, addr = sock.accept()

    # Receive data
    str_data = conn.recv(1024)

    # Decdoe data (unmarshalling)
    data = json.loads(str_data)

    print "%-20s %s" % ("Nama Kelompok", "NIM")
    for nk, nim in zip(data['NamaKelompok'], data['NIM']):
        print "%-20s %s" % (nk, nim)

