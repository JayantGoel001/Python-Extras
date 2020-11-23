from tkinter import *

win = Tk()

b = 0
for i in range(6):
    for j in range(6):
        b += 1
        button = Button(win, text=str(b), borderwidth=4)
        button.grid(row=i, column=j)

win.geometry("160x180")
win.mainloop()
