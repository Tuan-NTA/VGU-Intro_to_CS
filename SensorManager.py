from Adafruit_IO import MQTTClient
import tkinter as tk
from datetime import datetime

class SensorManager:
    def __init__(self, scheduler, chatbot_app):
        self.scheduler = scheduler
        self.chatbot_app = chatbot_app
        self.client = MQTTClient("SuSername", "aio_ZDmb35GGUPYuLMkZqZnwpRwGnJND")
        self.current_datetime = datetime.now()
        self.formatted_datetime = self.current_datetime.strftime("%Y-%m-%d %H:%M:%S")

        self.client.connect()
        self.client.loop_background()   

    def publish_sensor_state(self, sensor_number, state):
        topic = f"sensor-{sensor_number}"
        self.client.publish(topic, state)

    def get_sensor_value(self):
        # Return the latest stored sensor value
        return self.latest_sensor_value

    def SensorManager_run(self):
        if "on" in self.scheduler.shared_data[0] and "off" not in self.scheduler.shared_data[0]:
            shared_data = self.scheduler.shared_data[0]
            sensor_number = shared_data.split()[1]
            self.publish_sensor_state(sensor_number, "1")
            self.chatbot_app.Insert_response("Sensor " + str(sensor_number ) +"turned on")

        elif "off" in self.scheduler.shared_data[0] and "on" not in self.scheduler.shared_data[0]:
            shared_data = self.scheduler.shared_data[0]
            sensor_number = shared_data.split()[1]
            self.publish_sensor_state(sensor_number, "0")
            self.chatbot_app.Insert_response("Sensor " + str(sensor_number ) +"turned off")

        elif "date time" in self.scheduler.shared_data[0]:
             self.chatbot_app.Insert_response("Data time is: "+str(self.formatted_datetime))
       

        self.scheduler.shared_data[0] = " "
        self.chatbot_app.submit_button.config(state=tk.NORMAL)







