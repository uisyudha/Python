import socket
import pickle

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(('', 7887))

sock.listen(10)

while True:
    conn, addr = sock.accept()

    data = conn.recv(1024)

    print pickle.loads(data)