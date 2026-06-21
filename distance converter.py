import tkinter
from tkinter import *

root=Tk()
root.configure(background="dark red")

def convert():
      km=float(dist_box.get())
      miles=km*0.621371
      result_lbl.config(text=f"miles:{miles}")



distance_lbl=Label(root,text="distance converter",font=("Comic Sans MS",40,"bold"),foreground="white",background="dark red")
distance_lbl.grid(row=0,column=0)
kilometre_lbl=Label(root,text="enter the distance in kilometres",font=("Comic Sans MS",20,"bold"),foreground="white",background="dark red")
kilometre_lbl.grid(row=1,column=0)
dist_box=Entry(root,font=("Comic Sans MS",20,"normal"),justify="center")
dist_box.grid(row=2,column=0)
convert_btn=Button(root,text="convert",font=("Comic Sans MS",20,"bold"),foreground="white",background="black",command=convert)
convert_btn.grid(row=3,column=0)
result_lbl=Label(root,text="",font=("Comic Sans MS",20,"bold"),foreground="blue",background="red")
result_lbl.grid(row=4,column=0)



root.mainloop()
