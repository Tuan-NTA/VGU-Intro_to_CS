import tkinter as tk
from Chatbot_GUI import ChatbotApp
import time
from Chatbot_scheduler import *

from task2 import *
from task1 import *
import threading

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

    task2 = Task2(scheduler,chatbot_app)
    task1 = Task1(scheduler)

    scheduler.SCH_Add_Task(task2.Task2_Run, 3000, 6000)
    scheduler.SCH_Add_Task(task1.Task1_Run, 3000, 12000)
    
    scheduler_thread = threading.Thread(target=run_scheduler, args=(scheduler,))
    scheduler_thread.daemon = True
    scheduler_thread.start()

    root.protocol("WM_DELETE_WINDOW", lambda: close_app())

    root.mainloop()

def close_app():
    global exit_threads
    exit_threads = True
    root.quit()
