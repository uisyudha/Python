# Import socket
import socket

# Alamat server dan port
SERVER_IP = '127.0.0.1'
PORT = 4444

# Inisialisasi socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print 'Address before sending message: ', sock.getsockname()
# Send message
sock.sendto('HELLO', ((SERVER_IP, PORT)))
print 'Address after sending message:', sock.getsockname()
# Receive data from server
data, addr = sock.recvfrom(100)
print 'The server', addr, 'says', data


