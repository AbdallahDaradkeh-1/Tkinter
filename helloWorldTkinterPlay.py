import tkinter as tk
from tkinter import *

def hello():
  print("hello world!")

tk = tk.Tk()
tk.geometry("400x200")
btn = Button(tk, text = 'click me', command = hello)

btn.pack(side=LEFT, fill = X, expand = True)# The X(horizontal), expand = False by default, so we should make it
tk.mainloop()                 # True To stretch the button horizontally