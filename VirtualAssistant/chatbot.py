import requests
import tkinter as tk


class RasaBot:
    def __init__(self, scheduler, chatbot_app):
        self.chatbot_app = chatbot_app
        self.scheduler = scheduler
        self.rasa_url = "http://localhost:5005/webhooks/rest/webhook"
        self.last_response = None  # Store the last response

    def run_chatbot(self):
        payload = {
            "sender": "user",
            "message": self.scheduler.userinput
        }

        response = requests.post(self.rasa_url, json=payload)

        if response.status_code == 200:
            if response.json():
                rasa_response = response.json()[0]

                # Check if the response has changed
                if rasa_response['text'] != self.last_response:
                    print(f"Bot: {rasa_response['text']}")
                    self.chatbot_app.Insert_response(rasa_response['text'])
                    self.chatbot_app.submit_button.config(state=tk.NORMAL)

                    # Update the last response
                    self.last_response = rasa_response['text']


        else:
            print(f"Error: {response.status_code}, {response.text}")

