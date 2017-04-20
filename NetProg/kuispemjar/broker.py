import socket
import select
import json

# Inisiasi socket tcp
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding ke ip port
sock.bind(('', 7887))

# Listen 10 3 way handshake
sock.listen(10)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Buat list untuk menampung koneksi yg akan dimonitor oleh select
list_koneksi = [sock]
list_sub = {"Pemrograman": [], "Design": []}
try:
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
                    raw_data = n.recv(1024)
                    data = json.loads(raw_data)

                    if data["id"] == "subscriber":
                        if data["topik"] == "Pemrograman":
                            print addr, "Subscribe Topik Pemrograman"
                            list_sub["Pemrograman"].append(conn)
                        elif data["topik"] == "Design":
                            print addr, "Subscribe Topik Design"
                            list_sub["Design"].append(conn)
                        elif data["topik"] == "Semua":
                            print addr, "Subscribe Semua Topik"
                            list_sub["Design"].append(conn)
                            list_sub["Pemrograman"].append(conn)
                    elif data["id"] == "publisher":
                        if data["topik"] == "Pemrograman":
                            print "Publish Topik Pemrograman ---> send to subscriber"
                            for i in list_sub["Pemrograman"]:
                                i.send(data["isi_pesan"])
                        elif data["topik"] == "Design":
                            print "Publish Topik Design ---> send to subscriber"
                            for i in list_sub["Design"]:
                                i.send(data["isi_pesan"])
                except socket.error:
                    # Hapus koneksi yang putus dari list
                    list_koneksi.remove(n)
                    n.close()
                    print "Koneksi ke client terminated"
                except ValueError:
                    print "Koneksi ke client terminated"
except KeyboardInterrupt:
    "Broker Down"
