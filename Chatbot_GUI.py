import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class ChatbotApp:
    def __init__(self, root, scheduler):
        self.root = root
        self.root.withdraw()
        self.window = tk.Toplevel(root)
        self.window.title("Python Virtual Helper")
        self.window.geometry('900x600+300+70')
        self.window.configure(bg="#fff")
        self.window.resizable(False, False)
        self.load_images()
        self.create_widgets()
        self.load_chatFrame()
        self.Boxchat

        self.scheduler = scheduler #get direct attributes from scheduler

    def load_images(self):
        try:
            self.imagebg = Image.open("Content_bg0.png")
            self.framebg = ImageTk.PhotoImage(self.imagebg)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image: {str(e)}")
            self.imagebg = None
            self.framebg = None

    def create_widgets(self):
        if self.framebg:
            background_label = tk.Label(self.window, image=self.framebg)
            background_label.place(x=0, y=0, relwidth=1)

        self.Chatscreen = tk.Text(self.window, bg='#18181C', font=("Microsoft Yahei light", 12), width=65, wrap=tk.WORD,
                                  height=21, border=0, fg="#FAF9DD")
        self.Chatscreen.config(state=tk.DISABLED)
        self.Chatscreen.place(x=150, y=37)

        Chatscreen_scroll = tk.Scrollbar(self.window, command=self.Chatscreen.yview, width=20, highlightthickness=20)
        self.Chatscreen.configure(yscrollcommand=Chatscreen_scroll.set)
        Chatscreen_scroll.place(x=715, y=220)

        Menu_frame = tk.Frame(self.window, width=32, height=495, bg='#220257')
        Menu_frame.place(x=0, y=5)

        Go_back = tk.Button(Menu_frame, text="<--", font=('Microsoft Yahei light', 11), fg="#FFFEF6", bg='#220257', border=0)
        Go_back.place(x=0, y=10)

    def Insert_text(self):
        self.scheduler.inp_status[0] = 1
        text = self.Boxchat.get("1.0", tk.END).strip()
        self.Chatscreen.config(state=tk.NORMAL)
        self.Chatscreen.insert(tk.END, "\n----------------------------------\n\n" + "you:   " + text + "\n\n----------------------------------\n")
        self.Chatscreen.config(state=tk.DISABLED)
        self.Boxchat.delete(1.0, tk.END)
        self.submit_button.config(state=tk.DISABLED)

    def load_chatFrame(self):
        chatFrame = tk.Frame(self.window, width=900, height=100, bg='#002d51')
        chatFrame.place(x=0, y=500)
        self.Boxchat = tk.Text(chatFrame, bg='white', width=40, font=("Microsoft Yahei light", 14), wrap=tk.WORD, height=3)
        self.Boxchat.place(x=180, y=10)
        scrollbar = tk.Scrollbar(chatFrame, command=self.Boxchat.yview)
        self.Boxchat.configure(yscrollcommand=scrollbar.set)
        scrollbar.place(x=595, y=25)

        self.submit_button = tk.Button(chatFrame, text="Submit", padx=18, pady=12, font=("Helvetica Bold", 12),
                                  bg="green", fg="white", border=0, command=self.Insert_text)
        self.submit_button.place(x=640, y=25)






