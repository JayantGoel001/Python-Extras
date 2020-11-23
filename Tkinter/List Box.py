from tkinter import *

win = Tk()

lb = Listbox(win)
lb.insert(1, 'python')
lb.insert(2, 'cpp')
lb.insert(3, 'java')
lb.insert(4, 'c')
lb.insert(5, 'ruby')
lb.pack()

win.geometry("250x250")
win.mainloop()
