import tkinter as tk
from Data_proccesor import ChatGPTAssistant
class Task2:
    def __init__(self, scheduler, chatbot_app):
        self.chatbot_app = chatbot_app
        self.scheduler = scheduler
        self.api_key="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"

        
    def Task2_Run(self):
        # Retrieve data from the shared data store (Task1's data)
        data_from_task1 = self.scheduler.shared_data.get("task1_data", "No data available")
        if self.scheduler.inp_status[0] == 1:
            if self.scheduler.userinput=="":
                self.chatbot_app.Insert_response("Please enter something")
                self.chatbot_app.submit_button.config(state=tk.NORMAL)
                return 
            response=ChatGPTAssistant(self.api_key).generate_response(self.scheduler.userinput)
            self.chatbot_app.Insert_response(response)
            self.chatbot_app.submit_button.config(state=tk.NORMAL)
            self.scheduler.inp_status[0] = 0

        print("Data received by Task2:", data_from_task1)
        print("Task 2 is activated!!!!\n")
