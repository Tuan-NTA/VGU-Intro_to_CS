print("MQTT with Adafruit IO")
import time
import sys
from Adafruit_IO import MQTTClient
AIO_USERNAME = "*username*"
AIO_KEY = "*ada key*"

class Cargo:
    def __init__(self,cargo: str, where: str):
        self.cargo = cargo
        self.where = where


    def feed_cargo(self):
        temp = self.cargo
        temp = temp.isnumeric() #check to see if have to convert to float
        if temp == True:
            self.cargo = float(self.cargo)
        client.publish(self.where, self.cargo) #uploads data to adafruit to the feed specified

def connected(client):
    print("Server connected ...") #connect to certain switches if you want
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

client = MQTTClient(AIO_USERNAME, AIO_KEY )

client.on_connect = connected  #function pointer
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe

client.connect()
client.loop_background()

#This part below pushes data to the server
while True:
    time.sleep(5) #every 5 seconds it pushes
    cargo = input("Enter data: ") #Data gets supplied here
    where = input("Enter what feed: ") #The feed it goes to goes here
    Load = Cargo(cargo, where)
    Load.feed_cargo()
    #You can keep doing this as much as you want
    pass
