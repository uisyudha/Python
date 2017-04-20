import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('127.0.0.1', 4444))

a = input("Masukkan bilangan pertama : ")
b = input("Masukkan bilangan kedua : ")

sock.send(str(a))
sock.send(str(b))

data = sock.recv(100)

print data

sock.close()
