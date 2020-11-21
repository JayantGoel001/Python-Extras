from tkinter import *

win = Tk()

c1 = IntVar()
c2 = IntVar()

cb = Checkbutton(win, text='Music', offvalue=0, onvalue=1, height=5, width=10, variable=c1)
cb.pack()
cb2 = Checkbutton(win, text='Songs', offvalue=0, onvalue=1, height=5, width=10, variable=c2)
cb2.pack()

r1 = IntVar()

rb1 = Radiobutton(win, text='Option 1', variable=r1, value=1)
rb1.pack()

rb2 = Radiobutton(win, text='Option 2', variable=r1, value=2)
rb2.pack()

rb3 = Radiobutton(win, text='Option 3', variable=r1, value=3)
rb3.pack()

rb4 = Radiobutton(win, text='Option 4', variable=r1, value=1)
rb4.pack()
win.geometry("300x300")
win.mainloop()
