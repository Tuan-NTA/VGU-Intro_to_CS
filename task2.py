import tkinter as tk
from data_Process import answer
class Task2:
    def __init__(self, scheduler, chatbot_app):
        self.chatbot_app = chatbot_app
        self.scheduler = scheduler
        self.api_key="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"

        
    def Task2_Run(self):
        if self.scheduler.inp_status[0] == 1:
            if self.scheduler.userinput == "":
                self.chatbot_app.Insert_response("Please enter something")
                self.chatbot_app.submit_button.config(state=tk.NORMAL)
                return

            response = answer(self.scheduler.userinput)

            if response:
                if response == "Retrieving weather data":
                    self.scheduler.shared_data[0] = "Retrieving weather data"
                    self.chatbot_app.submit_button.config(state=tk.NORMAL)
                elif response in ["sensor 1 on", "sensor 2 on", "sensor 3 on","sensor 1 off", "sensor 2 off", "sensor 3 off", "Request", "date time"]:
                   
                    self.scheduler.shared_data[0] = response
                    self.chatbot_app.submit_button.config(state=tk.NORMAL)
                else:
                    self.chatbot_app.Insert_response(response)
                    self.chatbot_app.submit_button.config(state=tk.NORMAL)
            else:
                response="I'm sorry, I cannot answer that question"
                self.chatbot_app.Insert_response(response)
                self.chatbot_app.submit_button.config(state=tk.NORMAL)
                
           
            self.scheduler.inp_status[0] = 0




