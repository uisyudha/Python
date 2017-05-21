import socket
from util import recvall_termination, sendall_termination, sendall_number, recvall_number

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('127.0.0.1', 7777))


sendall_number(sock, "Hello Hello Hello Hello")

data = recvall_number(sock)

print data

sock.close()
