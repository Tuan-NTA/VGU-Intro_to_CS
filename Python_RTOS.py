import tkinter as tk
from Chatbot_GUI import ChatbotApp
import time
from Chatbot_scheduler import *
from open_weather import *
from task2 import *
from task1 import *
from Voice_GUI import *
import threading
from SensorManager import*

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
    speechrec=Voice_GUI(scheduler,chatbot_app)
    weather=Weather("1ba298b96119df3e3c4163ee93eafd4f","binh duong",scheduler,chatbot_app)
    sensor=SensorManager(scheduler,chatbot_app)

    scheduler.SCH_Add_Task(task2.Task2_Run, 3000, 6000)
    scheduler.SCH_Add_Task(task1.Task1_Run, 3000, 3000)
    scheduler.SCH_Add_Task(speechrec.Voice_GUI_run,3000,1000)
    scheduler.SCH_Add_Task(weather.Weather_run,3000,6000)
    scheduler.SCH_Add_Task(sensor.SensorManager_run,3000,6000)

    scheduler_thread = threading.Thread(target=run_scheduler, args=(scheduler,))
    scheduler_thread.daemon = True
    scheduler_thread.start()

    root.protocol("WM_DELETE_WINDOW", lambda: close_app())

    root.mainloop()

def close_app():
    global exit_threads
    exit_threads = True
    root.quit()
    scheduler_thread.join()  # Wait for the scheduler thread to finish

