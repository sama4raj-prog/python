from tkinter import *
from datetime import date

window = Tk()

window.title("demo window")
window.title("Getting Started with Widgets")
window.geometry("600x600")

lb1 = Label(window, text="Hey there!", fg="goldenrod", bg="black", height=1, width=300)
lb1.pack()
name_lb1 = Label(window, text="Full name",fg="black", bg="goldenrod")
name_lb1.pack()
name_entry = Entry(window, width=20)
name_entry.pack()

def display():
    name = name_entry.get()
    global message
    message = f"Hello {name}. \nWelcome to the world of Python Tkinter!\nToday's date is {date.today()}."
    text_box.insert(END, message)

text_box = Text(height=3)
text_box.pack()

btn = Button(window, text="Click me!", command=display)
btn.pack()

window.mainloop()