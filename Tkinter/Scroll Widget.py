from tkinter import *

win = Tk()
s = Scale(win)
s.pack()

spinbox = Spinbox(win, from_=0, to_=10)
spinbox.pack()

win.geometry("200x200")
win.mainloop()
