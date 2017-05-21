import socket, select

# Inisiasi socket tcp
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding ke ip port
sock.bind(('', 7777))

# Listen 10 3 way handshake
sock.listen(10)

# Buat list untuk menampung koneksi yg akan dimonitor oleh select
list_koneksi = [sock]

while True:
    # 3 parameter input, output, error
    inputready, outputready, errorready = select.select(list_koneksi, [], [])

    for n in inputready:
        # Jika input yg ready adalah socket server
        if n == sock:
            # Terima permintaan koneksi
            conn, addr = sock.accept()
            # Tambbah koneksi baru ke list koneksi
            list_koneksi.append(conn)
        else:
            try:
                data = n.recv(100)
                data = "OK" + data
                n.send(data)
            except socket.error:
                # Hapus koneksi yang putus dari list
                list_koneksi.remove(n)
                n.close()
                print "Koneksi ke client terminated"
