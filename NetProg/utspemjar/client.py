# Client
import socket, struct

# Inisialisasi socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

# Connect ke server
sock.connect(('127.0.0.1', 4444))

# Data yang akan dikirim
data = [1,2,3,4,5]
print "Data will be send ", data

# hitung panjang data
len_dt = len(data)

# Pack data
data = struct.pack("I"*len_dt, *data)
# Pack panjang data
len_dt = struct.pack(">I", len_dt)

# Append data ke len_dt
data = len_dt + data

# Kirim data ke server
sock.send(data)

# Receive hasil perhitugan dari server
data = sock.recv(4)
# Unpack data dari server
data = struct.unpack(">I", data)[0]
print "Total : ", data
