import socket
import json
from thread import start_new_thread

# Inisiasi socket tcp
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding ke ip port
sock.bind(('', 4444))

# Listen 10 3 way handshake
sock.listen(10)

# Mengatasi masalah port already in use
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

dict_subs = {}


def handle_connection(conn):
    try:
        while True:
            data = conn.recv(100)
            # Jika client memutus koneksi akan ada string kosong yang dikirim client
            if data != "":
                msg = json.loads(data)

                if msg["tipe"] == "SUB":
                    topik = msg["topik"]
                    if topik in dict_subs:
                        dict_subs[topik].append(conn)
                    else:
                        dict_subs[topik] = []
                        dict_subs[topik].append(conn)
                    conn.send("OK")
                elif msg["tipe"] == "PUB":
                    topik = msg["topik"]
                    konten = msg["konten"]
                    if topik in dict_subs:
                        list_subs = dict_subs[topik]
                        for sub in list_subs:
                            sub.send(konten)
                        conn.send("OK")
                    else:
                        conn.send("PUBLISH GAGAL")

                else:
                    conn.send("WRONG COMMAND")

    except socket.error:
        for key in dict_subs:
            dict_subs[key].remove(conn)
        conn.close()


try:
    while True:
        # Accept permintaan 3 way handshake
        conn, addr = sock.accept()

        start_new_thread(handle_connection, (conn,))
    # Receive data dari client
except KeyboardInterrupt:
    print "Server Mati"