import zmq

port = 5556

context = zmq.Context()
socket = context.socket(zmq.SUB)

topic = raw_input("==========TOPIK========\n1. GANJIL\n2. GENAP\n Pilih Topik :  ")

socket.connect("tcp://localhost:%s" %port)

if topic == "1":
    topic = "ganjil"
elif topic == "2":
    topic = "genap"
else:
    print "ERROR INPUT"
    socket.close()

socket.setsockopt(zmq.SUBSCRIBE, topic)

while True:
    string = socket.recv()
    topic, msg = string.split()
    print topic, msg