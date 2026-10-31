from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Denomination calculator")
window.configure(bg="Light blue")
window.geometry("650x400")

label1 = Label(
    window, 
    text="Hello, user! Welcome to Denomination Counter Application",
    bg="Light blue",
)
label1.place(relx=0.5, y=340, anchor=CENTER)


def msg():
    msgBox = messagebox.showinfo(
        "Alert", "Do you want to calculate the denomination count?"
    )
    if msgBox == "ok":
        topWin()


button1 = Button(
    window, text="Let's get started!", command=msg, bg="brown", fg="white"
)
button1.place(x=260, y=360)


def topWin():
    top = Toplevel()
    top.title("Denomination calculator")
    top.geometry("650x400")
    top.configure(bg="Light blue")

    label2 = Label(
        top, text="Enter the amount", bg="Light grey"
    )
    entry = Entry(top)
    lbl = Label(
        top, text="Here are number of notes for each denomination:", bg="Light grey"
        )

    l1 = Label(top, text="1000", bg="Light grey")
    l2 = Label(top, text="500", bg="Light grey")
    l3 = Label(top, text="100", bg="Light grey")

    e1 = Entry(top)
    e2 = Entry(top)
    e3 = Entry(top)

    def calculate():
        try:
            amount = int(entry.get())
            note1000 = amount // 1000
            amount = amount % 1000
            note500 = amount // 500
            amount = amount % 500
            note100 = amount // 100

            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)

            e1.insert(END, str(note1000))
            e2.insert(END, str(note500))
            e3.insert(END, str(note100))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    btn = Button(top, text="Calculate", command=calculate, bg="brown", fg="white")

    label2.place(x=230, y=50)
    entry.place(x=200, y=80)
    btn.place(x=240, y=120)
    lbl.place(x=140, y=170)

    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)

    e1.place(x=270, y=200)
    e2.place(x=270, y=230)
    e3.place(x=270, y=260)


window.mainloop()