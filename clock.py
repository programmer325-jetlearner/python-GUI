from tkinter import *
from tkinter.ttk import *
from time import strftime

def time():
    str_time=strftime("%H:%M:%S %p")
    lbl.config(text=str_time)
    lbl.after(1000,time)

root=Tk()
root.config(background="red")
root.title("digital clock")

lbl=Label(root,font=("Calibri",50,"bold"),background="red",foreground="yellow")
lbl.pack(anchor="center")
time()

















root.mainloop()