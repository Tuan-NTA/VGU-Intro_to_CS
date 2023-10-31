import tkinter as tk

class Task2:
    def __init__(self, scheduler, chatbot_app):
        self.chatbot_app = chatbot_app
        self.scheduler = scheduler

    def Task2_Run(self):
        # Retrieve data from the shared data store (Task1's data)
        data_from_task1 = self.scheduler.shared_data.get("task1_data", "No data available")
        if self.scheduler.inp_status[0] == 1:
            print("ngu")
            self.chatbot_app.submit_button.config(state=tk.NORMAL)
            self.scheduler.inp_status[0] = 0

        print("Data received by Task2:", data_from_task1)
        print("Task 2 is activated!!!!\n")


