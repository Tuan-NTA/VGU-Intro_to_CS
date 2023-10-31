from tkinter import messagebox
import socket

class Task1:
    def __init__(self,scheduler, host="www.google.com", port=80, timeout=5):
        self.host = host
        self.port = port
        self.timeout = timeout

    def is_internet_available(self):
        try:
            socket.setdefaulttimeout(self.timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((self.host, self.port))
            return True
        except socket.error:
            return False

    def Task1_Run(self):
        a = self.is_internet_available()
        if a == False:
            messagebox.showwarning("Internet Connection Error", "Please check your internet connection.")







