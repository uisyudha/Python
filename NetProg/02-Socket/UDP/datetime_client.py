import socket

#Inisiasi objek socket UDP/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Kirim ke server
print "Perintah : today, yesterday, tommorow, exit"
data = raw_input("Input : ");
while data != "exit":
	sock.sendto(data,('127.0.0.1', 7777))
	#Terima data
	data, address = sock.recvfrom(100)
	print data
