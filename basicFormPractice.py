from tkinter import *
from tkinter import ttk

root = Tk()


label1 = Label(root, text="Name")
label1.grid(column=0,row=0) # We made the grid on a seperate line, becuase grid return None, and we don't need the label1 value to be None, we want the label1 to have the widget itself

Entry(root).grid(column=1, row=0)

label2 = Label(root,text="Password")
label2.grid(column=0, row=1)
Entry(root).grid(column=1,row=1)
Button(root, text="Quit", command=root.destroy).grid(column=0, row=2)

root.mainloop()