from tkinter import *

win = Tk()

sb = Scrollbar(win)
sb.pack(side=RIGHT, fill=Y)
listBox = Listbox(win, yscrollcommand=sb.set)

for line in range(100):
    listBox.insert(END, 'This is line no ' + str(line))
listBox.pack(side=LEFT, fill=BOTH)

sb.config(command=listBox.yview)

win.geometry("200x200")
win.mainloop()
