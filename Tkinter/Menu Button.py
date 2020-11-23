from tkinter import *

win = Tk()

mb = Menubutton(win, text='File')
mb.grid()
mb.menu = Menu(mb)
mb['menu'] = mb.menu

x1 = IntVar()
x2 = IntVar()

mb.menu.add_checkbutton(label='open', variable=x1)
mb.menu.add_checkbutton(label='close', variable=x2)
mb.pack()
win.geometry("300x300")

win.mainloop()
