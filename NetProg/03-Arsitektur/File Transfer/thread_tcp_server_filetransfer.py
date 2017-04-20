import socket
from thread import start_new_thread

# Inisiasi socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding ip dan port
sock.bind(('', 4444))

# Reclaim port
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Listen 10, 3 way handshake
sock.listen(10)


def handle_connection(conn, addr):
    try:
        while True:
            data = conn.recv(10)
            print "Menerima" + data + "dari", addr
            print "Transfer file......."

            # Open file
            file = open("serverfile.txt", "r")

            # Membaca file
            readfile = file.read(100)

            # Looping readfile sampai habis
            while (readfile):
                conn.send(readfile)
                readfile = file.read(100)
            file.close()

            print "Transfer selesai"

            # Close read write socket
            conn.shutdown(socket.SHUT_WR)

    except socket.error:
        print "Koneksi ke client ", addr, " mati"


try:
    while True:
        # Terima permintaan koneksi
        conn, addr = sock.accept()

        start_new_thread(handle_connection, (conn, addr,))
except KeyboardInterrupt:
    print "Server Terminated"
