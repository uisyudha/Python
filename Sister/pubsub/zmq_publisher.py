import zmq
import random

port = "5556"

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:%s" % port)


while True:
    msg = random.randrange(1, 9999)

    if msg % 2 == 0:
        topic = "genap"
    else:
        topic = "ganjil"

    print "%s %d" % (topic, msg)
    socket.send("%s %d" % (topic, msg))
