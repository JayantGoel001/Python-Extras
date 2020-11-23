from tkinter import *

win = Tk()

def nothing():
    file = Toplevel(win)
    button = Button(file,text='Do Nothing')
    button.pack()
    file.geometry("50x50")

menubar = Menu(win)

filemenu = Menu(menubar)
filemenu.add_command(label='New Window',command=nothing)
filemenu.add_command(label='New File',command=nothing)
filemenu.add_command(label='Open...',command=nothing)
filemenu.add_command(label='Add Project Folder...',command=nothing)
filemenu.add_command(label='Reopen Project',command=nothing)
filemenu.add_command(label='Reopen Last Item',command=nothing)
filemenu.add_separator()
filemenu.add_command(label='Save',command=nothing)
filemenu.add_command(label='Save As...',command=nothing)
filemenu.add_command(label='Save All',command=nothing)
filemenu.add_separator()
filemenu.add_command(label='Close Tab',command=nothing)
filemenu.add_command(label='Close Pane',command=nothing)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=win.quit)

menubar.add_cascade(label="File",menu=filemenu)


editmenu = Menu(menubar)
editmenu.add_command(label='Cut',command=nothing)
editmenu.add_command(label='Copy',command=nothing)
editmenu.add_command(label='Paste',command=nothing)
editmenu.add_command(label='Undo',command=nothing)
editmenu.add_command(label='Redo',command=nothing)
editmenu.add_command(label='Select All',command=nothing)
editmenu.add_separator()
editmenu.add_command(label='Find',command=nothing)
editmenu.add_command(label='Replace',command=nothing)
editmenu.add_command(label='Search',command=nothing)
editmenu.add_separator()
editmenu.add_command(label='Exit',command=win.quit)

menubar.add_cascade(label='Edit',menu=editmenu)

win.config(menu=menubar)
win.geometry("300x300")
win.mainloop()