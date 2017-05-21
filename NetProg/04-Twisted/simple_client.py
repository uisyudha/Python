import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('127.0.0.1', 7887))

data = "Hello \r\n"

sock.send(data)

data = sock.recv(100)

print data

sock.close()
