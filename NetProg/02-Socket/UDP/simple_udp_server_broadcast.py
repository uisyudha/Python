import socket, sys

# Inisiasi objek socket UDP/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Set option to broadcast
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

if len(sys.argv) > 1:
	network = sys.argv[1]
	# Send broadcast message
	sock.sendto("This is broadcast!", ((network, 4444)))
else:
	print "use parameter address"

