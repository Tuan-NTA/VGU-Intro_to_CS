import tkinter as tk
import chatbot
from Chatbot_GUI import *
from Chatbot_scheduler import *
from push import push_data_to_adafruit_io, setup_adafruit_io
from task1 import *
from Voice_GUI import *



from chatbot import  *  # Import the RasaBot class
import threading
import time

# Global flag variable to signal thread termination
exit_threads = False

def run_scheduler(scheduler):
    try:
        while not exit_threads:
            scheduler.SCH_Update()
            scheduler.SCH_Dispatch_Tasks()
            time.sleep(0.1)
    except Exception as e:
        print("Scheduler Thread Error:", e)

if __name__ == "__main__":
    root = tk.Tk()
    scheduler = Scheduler()
    scheduler.SCH_Init()
    chatbot_app = ChatbotApp(root, scheduler)

    task1 = Task1(scheduler)
    speechrec = Voice_GUI(scheduler, chatbot_app)
    rasabot= RasaBot(scheduler,chatbot_app)


    scheduler.SCH_Add_Task(task1.Task1_Run, 3000, 3000)
    scheduler.SCH_Add_Task(speechrec.Voice_GUI_run, 3000, 1000)

    scheduler.SCH_Add_Task(rasabot.run_chatbot, 5000, 5000)

    client, weather = setup_adafruit_io()


    scheduler_thread = threading.Thread(target=run_scheduler, args=(scheduler,))
    scheduler_thread.daemon = True
    scheduler_thread.start()

    root.protocol("WM_DELETE_WINDOW", lambda: close_app())

    root.mainloop()

def close_app():
    global exit_threads
    exit_threads = True
    root.quit()
    scheduler_thread.join()
