from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Virus Detected")
window.geometry("200x200")

def msg():
    messagebox.showwarning("Alert", "Stop! Virus found.")

button = Button(window, text="Scan for Virus", command=msg)
button.place(x=40, y=80)

window.mainloop()
