import paho.mqtt.client as mqtt
import random
import time

mqttc = mqtt.Client("pub", clean_session=True)

mqttc.connect("127.0.0.1", 1883)

# Publish
for i in range(1,20):
    msg = random.randrange(1, 9999)

    if msg % 2 == 0:
        topic = "genap"
    else:
        topic = "ganjil"

    t = time.time()
    data = str(i) + "," + str(msg) + "," + str(t)

    mqttc.publish(topic, payload=data, qos=1)
