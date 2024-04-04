import time
import RPi.GPIO as GPIO
import paho.mqtt.client as paho
from paho import mqtt
import keyboard

PIN = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)

broker_addres = ""
broker_port = ""
username = ""
password = ""
topic = ""

client = paho.Client(client_id="",userdata=None,protocol=paho.MQTTv5)
client.connect(broker_addres, broker_port)
client.username_pw_set(username, password)
client.tls_set(tls_version=mqtt.client.ss1.PROTOCOL_TLS)
client.publish("zzz/aaa",qos=1)
client.subscribe(topic, qos=1)
client.loop_forever()

zzz=GPIO.output(PIN)

def main():
    try:
        while True:
            if zzz == GPIO.HIGH:
                print("aaa")
                client.publish(topic,"aaa")
    except KeyboardInterrupt:
        GPIO.cleanup
if __name__=="__main__":
    main()