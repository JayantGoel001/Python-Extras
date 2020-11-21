from tkinter import *

win = Tk()
win.geometry("300x300")


def sayHello():
    print("Hello World")


button3 = Button(win, text="Button3", command=sayHello, padx=10, pady=10, activeforeground='red')
button3.place(x=120, y=120)

win.mainloop()
