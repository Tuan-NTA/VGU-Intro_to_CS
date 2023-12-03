from Adafruit_IO import MQTTClient
from open_weather import Weather

AIO_USERNAME = "TuanNT"
AIO_KEY = "aio_CdQT11M9w4MIlEV9RVY7Krnfa45H"

class Cargo:
    def __init__(self, cargo: str, where: str):
        self.cargo = cargo
        self.where = where

    def feed_cargo(self):
        if isinstance(self.cargo, (int, float)):
            client.publish(self.where, self.cargo)  # uploads data to Adafruit to the feed specified
        else:
            print(f"Invalid cargo data: {self.cargo}")

def connected(client):
    print("Server connected ...")  # connect to certain switches if you want
    client.subscribe("temperature")
    client.subscribe("humidity")
    client.subscribe("wind-speed")

def subscribe(client, userdata, mid, granted_qos):
    print("Subscribed!!!")

def disconnected(client):
    print("Disconnected from the server!!!")
    sys.exit(1)

def message(client, feed_id, payload):
    print(f"Received on {feed_id}: {payload}")

def push_data_to_adafruit_io(weather):
    # Use data from the Weather class to push to Adafruit IO feeds
    cargo1 = weather.temp_celsius
    where1 = "temperature"
    Load1 = Cargo(cargo1, where1)
    Load1.feed_cargo()

    cargo2 = weather.humidity
    where2 = "humidity"
    Load2 = Cargo(cargo2, where2)
    Load2.feed_cargo()

    cargo3 = weather.wind_speed
    where3 = "wind-speed"
    Load3 = Cargo(cargo3, where3)
    Load3.feed_cargo()

def setup_adafruit_io():
    # Instantiate the Weather class
    weather = Weather(api_key="41521cb866d6e4db1a9dded79fcf08c8", city="Ho Chi Minh city", scheduler=None, chat_botapp=None)

    # Instantiate the Adafruit IO MQTT client
    client = MQTTClient(AIO_USERNAME, AIO_KEY)
    client.on_connect = connected
    client.on_disconnect = disconnected
    client.on_message = message
    client.on_subscribe = subscribe
    client.connect()
    client.loop_background()

    return client, weather
