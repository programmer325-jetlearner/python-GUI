import random
from tkinter import *


root=Tk()
root.geometry("500x500")
colors=["red","blue","green","yellow","purple","orange"]
color=random.choice(colors)
root.configure(background=color)

def change_color():
   color=random.choice(colors)
   root.configure(background=color)
   color_magic_lbl=Label(root,text="color magic",font=("Calbiri",30,"bold"),background=color,fg="black")
   color_magic_lbl.grid(row=0,column=3,padx=10)


color_magic_lbl=Label(root,text="color magic",font=("Calbiri",30,"bold"),background=color,fg="black",)
color_magic_lbl.grid(row=0,column=3,padx=10)

color_btn=Button(root,text="change color",font=("Calbiri",20,"bold"),background="black",fg="white",command=change_color,width=20)
color_btn.grid(row=1,column=3,padx=10)






root.mainloop()