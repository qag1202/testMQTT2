
import time
import paho.mqtt.client as paho
from paho import mqtt
import keyboard

broker_address = "1f876e65679c4d7f9afe21ead0366379.s1.eu.hivemq.cloud"
broker_port = 8883
topic = "test/topic"
username = "quang"
password = "Light@1202"

def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)
    client.publish(topic,"Hi")
def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))
def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def on_key_press(event):
    if event.name == "a":
        client.publish(topic, "Message sent by pressing 'a' key")
keyboard.on_press(on_key_press)
client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set(username, password)
client.connect(broker_address, 8883)
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_publish = on_publish
client.subscribe(topic, qos=1)
client.publish("encyclopedia/temperature", payload="hot", qos=1)
client.loop_forever()