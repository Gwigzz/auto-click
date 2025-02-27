import pyautogui
import time
import tkinter as tk
from tkinter import messagebox
import threading
import keyboard
import webbrowser
from winotify import Notification, audio

BG_COLOR = "#101218"
APP_V    = "1.0"

def open_github_link(event):
    webbrowser.open("https://github.com/Gwigzz/auto-click")

"""
    Stop autoclicker
"""
def stop():
    global running
    running = False
    status_label.config(text="STOP", fg="red", font=("Arial", 10, "bold"))
    notif = Notification(app_id="Auto Clicker", title="Auto Clicker", msg="Stop", duration="short")
    notif.show()
    notif.set_audio(audio.Default, loop=False)
    
"""
    Started autoclicker
"""
def start():
    global running
    if not running:
        running = True
        status_label.config(text="RUNNING...", fg="#45D134", font=("Arial", 10, "bold"))
        threading.Thread(target=auto_click, daemon=True).start()
        notif = Notification(app_id="Auto Clicker", title="Auto Clicker", msg="Running ...", duration="short")
        notif.show()
        notif.set_audio(audio.Default, loop=False)

running = False

# Create Window
root = tk.Tk()
root.title(f"Auto Clicker {APP_V}")
root.geometry("280x100")

# Check icon app
try:
    root.iconbitmap("ico.ico")
except:
    messagebox.showinfo("No Icon Found", "Missing application icon. \nPlease create or download ico.ico from github repo")

root.resizable(False, False)

root.configure(bg=f"{BG_COLOR}") # #1F1F23 (dark)

frame = tk.Frame(root, bg=f"{BG_COLOR}")
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

status_label = tk.Label(root, text="STOP", fg="red", font=("Arial", 10, "bold"), bg=f"{BG_COLOR}")
status_label.pack(pady=10)

start_button = tk.Button(frame, text="Start", command=start, borderwidth=1)
start_button.pack(side=tk.LEFT, padx=10)

stop_button = tk.Button(frame, text="Stop", command=stop, borderwidth=1)
stop_button.pack(side=tk.LEFT, padx=10)

labelGHLink = tk.Label(root, text="github", fg="#0c91ff", cursor="hand2", font=("Arial", 10, "underline italic"), bg=f"{BG_COLOR}")
labelGHLink.bind("<Button-1>", open_github_link)
labelGHLink.place(relx=1.0, y=5, anchor="ne")

def auto_click():
    while running:
        pyautogui.click()
        time.sleep(0.005)  # speed click

def toggle_auto_clicker():
    if running:
        stop()
    else:
        start()

bottom_text = tk.Label(root, text="Type (F9) to start or stop", fg="orange", bg=f"{BG_COLOR}", font=("Helvetica", 8, "italic"))
bottom_text.pack(side=tk.BOTTOM, pady=5)

keyboard.add_hotkey('F9', toggle_auto_clicker)

root.mainloop()