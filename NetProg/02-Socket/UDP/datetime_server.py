import socket
from datetime import date, timedelta

#Inisiasi objek socket UDP/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Bind
sock.bind(('', 7777))

try:
	print "Server up"
	while True:
		#Receive data
		data, address = sock.recvfrom(100)
		if data == "today":
			data = str(date.today());		
			#Kirim balik ke client
			sock.sendto(data, address)
		elif data == "yesterday":
			data = str(date.today() - timedelta(1));		
			#Kirim balik ke client
			sock.sendto(data, address)
		elif data == "tommorow":
			data = str(date.today() + timedelta(1));		
			#Kirim balik ke client
			sock.sendto(data, address)
	
		
except KeyboardInterrupt:
	print "Server down"
	
