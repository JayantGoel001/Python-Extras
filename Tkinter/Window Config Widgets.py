from tkinter import *

win = Tk()
frame = Frame(win)
frame.pack()

frame2 = Frame(win)
frame2.pack(side=BOTTOM)

rb = Button(frame, text='red', fg='red')
rb.pack(side=LEFT)

bb = Button(frame, text='Blue', fg='blue')
bb.pack(side=LEFT)

blb = Button(frame, text='Black', fg='black')
blb.pack(side=LEFT)

gb = Button(frame2, text='green', fg='green')
gb.pack(side=BOTTOM)

win.geometry("200x100")
win.mainloop()
