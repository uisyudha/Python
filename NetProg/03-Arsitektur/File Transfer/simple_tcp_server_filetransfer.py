import socket

# Inisiasi socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Fix address already in use
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Binding IP
sock.bind(('', 4444))

# Listen 10 3 way handshake
sock.listen(10)

print "Server on"

while True:
    # Accept permintaan 3 way handshake
    conn, addr = sock.accept()

    filename = "serverfile.txt"
    f = open(filename, "r")
    l = f.read(100)

    while (l):
        conn.send(l)
        print "Sent", repr(l)
        l = f.read(100)
    f.close()

    print "Done sending"
    conn.close()
