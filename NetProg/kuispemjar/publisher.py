import socket
import json

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.connect(('127.0.0.1', 7887))

try:
    while True:
        print "1. Pemrograman\n2. Design\n"
        topik = raw_input("Pilih Topik :")
        isi_pesan = raw_input("Isi Pesan : ")

        if topik == "1":
            data = {
                "id": "publisher",
                "topik": "Pemrograman",
                "isi_pesan": isi_pesan}
            sock.send(json.dumps(data))
        elif topik == "2":
            data = {
                "id": "publisher",
                "topik": "Design",
                "isi_pesan": isi_pesan}
            sock.send(json.dumps(data))

        #data = sock.recv(100)

        #print data
except KeyboardInterrupt:
    print "Client Terminated"
