# Import socket
import socket

# Inisialisasi socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind ke ip dan port
sock.bind(('', 4444))

print 'Listening at', sock.getsockname()

try:
    while True:
        # Terima data
        data, addr = sock.recvfrom(100)
        print 'Receive ', data, 'from ', addr
        # Ubah data
        data = data + ' OK'
        # Kirim ke client
        sock.sendto(data, addr)
except KeyboardInterrupt:
    print 'Server down'