import socket

# Inisiasi objek socket UDP/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Set option broadcast
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# Bind ke prot
sock.bind(('', 4444))
# Read incoming message
while True:
	data, addr = sock.recvfrom(100)
	print "The client at %r says %r" % (addr, data)
