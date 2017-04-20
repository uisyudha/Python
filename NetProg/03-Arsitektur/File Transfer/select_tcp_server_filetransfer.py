import socket, select

#Inisiasi socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Reclaim port
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#Bind ip dan port
sock.bind(('', 4444))

#Listen 10 3 way handshake
sock.listen(10)

#List untuk menampung koneksi yg akan di monitor
list_koneksi = [sock]


try:
    while True:
        # select mereturn 3 parameter : input, output, error
        inputready, outputready, errorready = select.select(list_koneksi, [], [])

        for n in inputready:
            #Jika input yg ready socket server
            if n == sock:
                #Terima permintaan koneksi
                conn, addr = sock.accept()
                print "Menerima koneksi dari ", addr
                #Tambah koneksi baru ke list koneksi
                list_koneksi.append(conn)
            else:
                try:
                    # Menerima ping dari client
                    data = n.recv(10)
                    print "Menerima " + data + " dari ", addr
                    print "Transfer file .........."

                    file = open("serverfile.txt", "r")

                    # Membaca file
                    readfile = file.read(100)

                    # Looping readfile sampai habis
                    while (readfile):
                        n.send(readfile)
                        readfile = file.read(100)
                    file.close()

                    print "Transfer selesai"

                    #Remove koneksi dari list_koneksi
                    list_koneksi.remove(n)

                    #Close read write socket
                    n.shutdown(socket.SHUT_WR)
                except socket.error:
                    print "Koneksi ke client ", addr, " mati"
except KeyboardInterrupt:
    print "Server Terminated"



