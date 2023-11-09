print("MQTT with Adafruit IO")
import time
import sys
from Adafruit_IO import MQTTClient
AIO_USERNAME = "*username*"
AIO_KEY = "*key goes here*"

def connected(client):
    print("Server connected ...")
    client.subscribe("led")
    client.subscribe("waterpump")
    client.subscribe("equation")
def subscribe(client , userdata , mid , granted_qos):
    print("Subscribed!!!")

def disconnected(client):
    print("Disconnected from the server!!!")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Received: " + payload)
    if(feed_id == "equation"):
        global global_equation
        global_equation = payload
        print(global_equation)

client = MQTTClient("*username*", "*key goes here*")

client.on_connect = connected  #function pointer
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe

client.connect()
client.loop_background()

#This part below pushes data to the server
while True:
    time.sleep(5) #every 5 seconds it pushes
    client.publish("*the feed*", "*the data*")
    client.publish("sensor2", "I did it!!!")
    #You can keep doing this as much as you want
    pass