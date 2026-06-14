import tkinter
from tkinter import *

root=Tk()
root.configure(background="#299EAD")

def convert():
    celsius=float(temp_box.get())
    fah=(celsius*9/5)+32
    result_lbl.config(text=f"fahrenheit:{fah}")


temperature_lbl=Label(root,text="Temperature converter",font=("Comic Sans MS",40,"bold"),foreground="black",background="#299EAD")
temperature_lbl.grid(row=0,column=0)
celsius_lbl=Label(root,text="Enter your temperature in celsius: ",font=("Comic Sans MS",20,"bold"),foreground="black",background="#299EAD")
celsius_lbl.grid(row=1,column=0)
temp_box=Entry(root,font=("Comic Sans MS",20,"normal"),justify="center")
temp_box.grid(row=2,column=0)
convert_btn=Button(root,text="convert",font=("Comic Sans MS",20,"bold"),foreground="white",background="red",command=convert)
convert_btn.grid(row=3,column=0)
result_lbl=Label(root,text="",font=("Comic Sans MS",20,"bold"),foreground="green",background="#299EAD")
result_lbl.grid(row=4,column=0)





root.mainloop()