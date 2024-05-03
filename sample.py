import tkinter as tk
import subprocess

process = None

def start_stop_command():
    global process
    if process is None:
        process = subprocess.Popen(["./01.sh"])
        button1.config(text="Stop")
    else:
        process.terminate()
        process = None
        button1.config(text="Button 1")

def open():
    global process
    if process is None:
        process = subprocess.Popen(["./01.sh"])
        button1.config(text="Stop")
    else:
        process.terminate()
        process = None
        button1.config(text="Button 2")

def close():
    global process
    if process is None:
        process = subprocess.Popen(["./01.sh"])
        button1.config(text="Stop")
    else:
        process.terminate()
        process = None
        button1.config(text="Button 3")






root = tk.Tk()
root.title("KakkoSYS Moduole Gui Sample")
root.geometry("320x180")

button1 = tk.Button(root, text="Button 1", command=start_stop_command)
button1.pack()

button2 = tk.Button(root, text="Button 2", command=open)
button2.pack()

button3 = tk.Button(root, text="Button 3", command=close)
button3.pack()

root.mainloop()