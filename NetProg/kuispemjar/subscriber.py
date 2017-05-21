import socket
import json

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.connect(('127.0.0.1', 7887))

try:
    print "1. Pemrograman\n2. Design\n3. Semua"
    topik = raw_input("Pilih Topik :")

    if topik == "1":
        data = {
            "id": "subscriber",
            "topik": "Pemrograman"}
        sock.send(json.dumps(data))
    elif topik == "2":
        data = {
            "id": "subscriber",
            "topik": "Design"}
        sock.send(json.dumps(data))
    elif topik == "3":
        data = {
            "id": "subscriber",
            "topik": "Semua"}
        sock.send(json.dumps(data))

    while True:

        data = sock.recv(1024)

        print data
except KeyboardInterrupt:
    print "Client Terminated"
