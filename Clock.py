from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("WATCH")

def time():
    string = strftime("%H:%M:%S")
    label.config(text=string)
    label.after(1000,time)

    
label = Label(root,font=("Arial",80),background = "GREEN",foreground = "RED")
label.pack(anchor='center')
time()
mainloop()
