from tkinter import *

window = Tk()
window.title("Event Handler")
window.geometry("100x100")

def handle_keypress(event):
    print(f"Key pressed: {event.char}")

window.bind("<Key>", handle_keypress)

def handle_mouse_click(event):
    print("The mouse is clicked.")

button = Button(window, text="Click me")
button.pack()

button.bind("<Button-1>", handle_mouse_click)


window.mainloop()