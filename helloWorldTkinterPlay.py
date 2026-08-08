import tkinter as tk
from tkinter import *

def hello():
  print("hello world!")

tk = tk.Tk()

btn = Button(tk, text = 'click me', command = hello)

btn.pack()

tk.mainloop()