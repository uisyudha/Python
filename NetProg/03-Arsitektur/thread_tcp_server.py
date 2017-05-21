import socket
from thread import start_new_thread

# Inisiasi socket tcp
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding ke ip port
sock.bind(('', 4444))

# Listen 10 3 way handshake
sock.listen(10)

# Mengatasi masalah port already in use
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


def handle_connection(conn):
    try:
        while True:
            data = conn.recv(100)
            print data
            data = "OK " + data
            conn.send(data)
    except socket.error:
        print "Koneksi ke client" + str(conn) + "mati";
        conn.close()


try:
    while True:
        # Accept permintaan 3 way handshake
        conn, addr = sock.accept()

        start_new_thread(handle_connection, (conn,))
    # Receive data dari client
except KeyboardInterrupt:
    print "Server Mati"
