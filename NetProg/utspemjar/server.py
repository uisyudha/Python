# Server
import socket, struct
# Inisialisasi socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
# Bind ke ip port tertentu
sock.bind(('', 4444))
# Listen
sock.listen(10)

while True:
    conn, addr = sock.accept()
    # Receive 4 byte dari server untuk mendapatkan panjang array datanya
    len_dt = conn.recv(4)
    # Unpack len_dt
    len_dt = struct.unpack(">I", len_dt)[0]
    # receive all data, len_dt * 4 karena 1 data integer memerlukan 4 byte
    data = conn.recv(len_dt*4)
    # Unpack data
    data = struct.unpack("I"*len_dt, data)
    print "Receive ", data, " from ", addr
    # Hitung total data
    total = 0
    for i in data:
        total = total + i
    # pack total ke integer
    data = struct.pack(">I", total)
    # Kirim ke client
    conn.send(data)

