import socket
import tkinter as tk
from tkinter import messagebox

def is_internet_available(host="8.8.8.8", port=53, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except OSError:
        return False

# Kiểm tra kết nối internet
if not is_internet_available():
    root = tk.Tk()
    root.withdraw()  # Ẩn cửa sổ chính

    messagebox.showwarning("Internet Connection Error", "Please check your internet connection.")
