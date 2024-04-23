from tkinter import *
from tkinter import messagebox
import subprocess

def click():
    print("Hello")

def run_snapshot():
    try:
        subprocess.run(["python", "C:/Users/Владик/PycharmProjects/face"])
    except Exception as e:
        print(e)

root = Tk()

root.geometry("300x300+200+50")

btn = Button(root, text="Hello", background="red", foreground="black", padx=20, pady=10, activebackground="blue", activeforeground="white", command=run_snapshot)
btn.place(x=150, y=150)
btn.pack(side=BOTTOM)

root.mainloop()