#!/usr/bin/python2.7
import socket
from util import recvall_termination, sendall_termination, sendall_number, recvall_number

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('127.0.0.1', 7777))

while True:
    user_input = raw_input("Masukkan data yg dikirim : ")
    sendall_number(sock, user_input)

    data = recvall_number(sock)

    print data

# sock.close()f
