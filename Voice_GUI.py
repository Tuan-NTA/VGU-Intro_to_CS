import tkinter as tk
class Voice_GUI:
    def __init__(self,scheduler,chatbot_app):
        self.chatbot_app = chatbot_app
        self.scheduler = scheduler

    def Voice_GUI_run(self):
        if self.scheduler.voice_status[0]==1:
            print("Voice bot activated")
            #do sth here
            pass

