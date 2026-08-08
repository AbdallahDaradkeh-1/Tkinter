from tkinter import *
from tkinter import ttk

tk = Tk()

frame = ttk.Frame(tk, padding=10)
frame.grid()
ttk.Label(frame, text= "Hello World!").grid(column=0, row=0)
ttk.Button(frame, text = "Quit", command= tk.destroy).grid(column=1, row=0)
tk.mainloop()