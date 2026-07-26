from tkinter import *
import random

val1=random.randint(1,10)
val2=random.randint(1,10)
def give():
    val1=random.randint(1,10)
    val2=random.randint(1,10)
    answer=val1*val2

root=Tk()
root.geometry("500x500")
root.title("number guessing game")
root.config(background="#845033")
heading_lbl=Label(root,text="multiplication game",font=("Arial",20,"bold"),background="#845033",foreground="black")
heading_lbl.pack()
name_lbl=Label(root,text="enter your name: ",font=("Arial",18,"bold"),bg="#845033",fg="navy")
name_lbl.place(x=30,y=100)
name_entry=Entry(root)
name_entry.place(x=230,y=110,height=32)
ok_btn=Button(root,text="OK",font=("Arial",18,"bold"),background="violet",foreground="white")
ok_btn.place(x=380,y=110,width=100,height=32)










root.mainloop()