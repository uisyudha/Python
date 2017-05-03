import paho.mqtt.client as mqtt
import random

mqttc = mqtt.Client("pub", clean_session=True)

mqttc.connect("127.0.0.1", 1883)

# Publish
while True:
    msg = random.randrange(1, 9999)

    if msg % 2 == 0:
        topic = "genap"
    else:
        topic = "ganjil"
    mqttc.publish(topic, payload=msg)
