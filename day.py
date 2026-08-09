from tkinter import *
from tkinter.ttk import *
from time import strftime


def time():
    str_time=strftime("today is %A")
    lbl.config(text=str_time)
    lbl.after(1000)



root=Tk()
root.config(background="blue")
root.title("Today is:")
lbl=Label(root,text="",font=("Arial",40,"bold"),background="blue",foreground="white")
lbl.pack(anchor="center")
time()









root.mainloop()