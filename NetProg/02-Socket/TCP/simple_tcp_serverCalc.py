import socket

#Inisiasi socket tcp
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Binding ke ip port
sock.bind(('', 4444))

#Listen 10 3 way handshake
sock.listen(10) 

while True:
	# Accept permintaan 3 way handshake
	conn, addr = sock.accept()
	#Receive data dari client

	a = conn.recv(100)
	b = conn.recv(100)
	
	
	#ubah data
	data = int(a) +int(b)
	conn.send(str(data))
	conn.close()
	
