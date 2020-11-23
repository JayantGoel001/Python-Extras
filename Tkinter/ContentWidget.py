from tkinter import *
from functools import partial


def Sum(label, x, y):
    n1 = int(x.get())
    n2 = int(y.get())
    add = n1 + n2
    label.config(text='Sum is %d' % add)


win = Tk()

# text = Text()
# text.insert(INSERT, 'Hello')
# text.pack()

label1 = Label(win, text='First number')
label1.grid(row=1, column=0)

label2 = Label(win, text='Second Number')
label2.grid(row=2, column=0)

label = Label(win)
label.grid(row=6, column=2)

x1 = StringVar()
entry1 = Entry(win, textvariable=x1)
entry1.grid(row=1, column=2)

x2 = StringVar()
entry2 = Entry(win, textvariable=x2)
entry2.grid(row=2, column=2)

Sum = partial(Sum, label, x1, x2)
button = Button(win, text='Calculate', command=Sum)
button.grid(row=3, column=3)

win.geometry("300x300")
win.mainloop()
