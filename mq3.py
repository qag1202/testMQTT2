import time
import RPi.GPIO as GPIO
import paho.mqtt.client as paho
from paho import mqtt
import keyboard

BUTTON = 19
BUZZER = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN)
GPIO.setup(BUZZER, GPIO.OUT)

broker_address = ""
broker_port = ""
username = ""
password = ""
topic = ""

client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set(username, password)
client.connect(broker_address, 8883)
client.subscribe(topic, qos=1)
client.publish("encyclopedia/temperature", payload="hot", qos=1)
client.loop_forever()

def keyboardz(event):
    if event.name == "a":
        print("aaa")
        client.publish(topic, "a")
keyboard.on_press(keyboardz)

button = GPIO.input(BUTTON)
def Button():
    while True:
        if button == GPIO.HIGH:
            GPIO.output(BUZZER, GPIO.HIGH)
            print("buzzer")
            client.publish(topic, "buzzer")
            time.sleep(1)
if __name__ == "__main__":
    Button()
