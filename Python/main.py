import random
import time
import sys
from Adafruit_IO import MQTTClient
from uart import *

AIO_FEED_ID = ["v1", "v2", "v3", "v10", "v11", "v12"]
AIO_USERNAME = "HCMUT_IOT"
AIO_KEY = "aio_fgfv82snB4cQE4Gg2NLdn0ZQblFN"

def connected(client):
    print("Ket noi thanh cong ...")
    for id in AIO_FEED_ID:
        client.subscribe(id)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit(1)

def message(client , feed_id , payload):
    if feed_id == "v1":
        feed_id_temp = "temp_sensor"
    if feed_id == "v2":
        feed_id_temp = "humid_sensor"
    if feed_id == "v3":
        feed_id_temp = "light_sensor"
    if feed_id == "v10":
        feed_id_temp = "light_button"
    if feed_id == "v11":
        feed_id_temp = "light_color"
    if feed_id == "v12":
        feed_id_temp = "speed_fan"
    print("Data is from: " + payload + ", Feed_id: " + feed_id_temp)

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

#declare the var
counter = 10
counter_ai = 5
temp = 1
previous_result = ""

while True:
    time.sleep(1)
    counter = counter - 1
    # if counter == 0:
    #     counter = 10
    #     if temp == 1:
    #         temp = random.randint(20,40)
    #         client.publish("v1", temp)
    #         print("Temperture: ", temp)
    #         temp = 2
    #     elif temp == 2:
    #         lux = random.randint(0, 100)
    #         client.publish("v3", lux)
    #         print("Light: ", lux)
    #         temp = 3
    #     else:
    #         humid = random.randint(0, 400)
    #         client.publish("v2", humid)
    #         print("Moisture: ", humid)
    #         temp = 1
    readSerial(client)
