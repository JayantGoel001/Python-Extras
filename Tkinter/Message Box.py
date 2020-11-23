from tkinter import *
from tkinter import messagebox

win = Tk()


def PopUp():
    messagebox.showinfo('from computer', "Hey What's up?")


b = Button(win, text='popup', command=PopUp)
b.pack()

win.geometry("300x300")
win.mainloop()
