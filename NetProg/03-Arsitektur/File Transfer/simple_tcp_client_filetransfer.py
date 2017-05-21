import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('127.0.0.1', 4444))

milis = int(round(time.time() * 10000))

filename = "client" + str(milis)

sock.send("PING")

try:
    with open(filename, 'w') as file:
        while True:
            # print "receiving data.........."
            data = sock.recv(100)

            if not data:
                break
            # write data to file
            file.write(data)

    file.close()
    # print "Succesfully get the file"
    sock.close()
    # print "Connection closed"
except socket.error:
    pass
