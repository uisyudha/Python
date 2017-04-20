import socket
from util import recvall_termination, sendall_termination, sendall_number, recvall_number

# Inisiasi socket tcp
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding ke ip port
sock.bind(('', 7777))

# Listen 10 3 way handshake
sock.listen(10)

while True:
    # Accept permintaan 3 way handshake
    conn, addr = sock.accept()
    # Receive data dari client

    data = recvall_number(conn)
    print data

    sendall_number(conn, data)

# conn.close()
