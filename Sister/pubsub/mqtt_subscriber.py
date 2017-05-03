import paho.mqtt.client as mqtt

mqttc = mqtt.Client("sub", clean_session=True)

mqttc.connect("127.0.0.1", 1883)


def on_connect(mqttc, obj, flags, rc):
    print "Connected"


def on_message(mqttc, obj, msg):
    print "Topik " + msg.topic + " Payload : " + msg.payload


mqttc.on_connect = on_connect
mqttc.on_message = on_message

topic = raw_input("==========TOPIK========\n1. GANJIL\n2. GENAP\nPilih Topik :  ")
if topic == "1":
    topic = "ganjil"
    mqttc.subscribe(topic)
    mqttc.loop_forever()
elif topic == "2":
    mqttc.subscribe(topic)
    mqttc.loop_forever()
else:
    print "ERROR INPUT"


