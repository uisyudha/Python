import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('127.0.0.1', 7887))

try:
    while True:
        data = raw_input("Input : ")
        sock.send(data)
        data = sock.recv(100)

        print data
except KeyboardInterrupt:
    print "Client Terminated"
