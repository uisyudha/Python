# Import socket lib
import socket

# Inisialisasi object socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect ke server
sock.connect(('ip.jsontest.com', 80))

# Send GET request
sock.sendall(
    'GET / HTTP/1.1\r\n'
    'Host: ip.jsontest.com:80\r\n'
    'User-Agent: httprequest_socket.py\r\n'
    'Connection: close\r\n'
    '\r\n'
)

# Read all received messaged
while True:
    buf = sock.recv(1024)
    if not buf:
        break;
    print buf
sock.close()