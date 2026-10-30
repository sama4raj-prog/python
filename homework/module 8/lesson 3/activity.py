from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("My After-School Activity")
window.geometry("400x400")

frame = Frame(master=window, width=360, height=200, bg='#6d8a80')
frame.place(x=20, y=0)

lbl1 = Label(master=frame, text="Your after-school activity:", bg='#24302c', fg='white', width=20, font=("Arial", 20))
lbl1.place(x=20, y=20)
name_entry = Entry(master=frame)
name_entry.place(x=200, y=100)

def handle_keypress(event):
    print(f"Key pressed: {event.char}")

window.bind("<Key>", handle_keypress)

window.mainloop()