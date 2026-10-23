from tkinter import *

window = Tk()
window.title("Number Pad")
window.geometry("250x300")

frame = Frame(master=window, width=360, height=200, bg='#d0efff')
frame.place(x=20, y=0)

lbl1 = Label(master=frame, text="Full Name:", bg='#3895d3', fg='white', width=20)
lbl1.place(x=20, y=20)
name_entry = Entry(master=frame)
name_entry.place(x=200, y=20)

lbl2 = Label(master=frame, text="Email Address:", bg='#3895d3', fg='white', width=20)
lbl2.place(x=20, y=60)
email_entry = Entry(master=frame)
email_entry.place(x=200, y=60)

lbl3 = Label(master=frame, text="Password:", bg='#3895d3', fg='white', width=20)
lbl3.place(x=20, y=100)
password_entry = Entry(master=frame, show='*')
password_entry.place(x=200, y=100)

def display():
    name = name_entry.get()
    message = f"Hello {name}. Congratulations! You have successfully logged in."
    textbox.insert(END, message)

textbox= Text(master=window, width=47, height=5)
textbox.place(x=20, y=250)

btn = Button(master=frame, text="Create an account", bg='#3895d3', fg='white', width=20, command=display)
btn.place(x=100, y=160)

window.mainloop()