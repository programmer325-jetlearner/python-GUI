import random
from tkinter import *
import tkinter.messagebox

root=Tk()
root.geometry("500x500+500+150")
root.title("word jumble")
root.configure(background="#50A6F3")


heading_lbl=Label(root,text="JUMBLE WORD GAME",background="#50A6F3",foreground="#1E382B",font=("Verdana",30,"bold"))
heading_lbl.pack(pady=5)
jumble_lbl=Label(root,text="hello",font=("Verdana",22),background="#50A6F3",foreground="#105EA4")
jumble_lbl.pack(pady=30,ipadx=10,ipady=10)
ans=StringVar()
input_box=Entry(root,font=("Verdana",22),justify="center",textvariable=ans)
input_box.pack(ipady=5,ipadx=5)
check_btn=Button(root,text="check",font=("Verdana",20,"bold"),width=10,background="#F7971E",foreground="red")
check_btn.pack(pady=40)
reset_btn=Button(root,text="reset",background="#E5E327",foreground="#C49A5A",font=("Verdana",20,"bold"),width=10)
reset_btn.pack()
score_label=Label(root,text="10",font=("Verdana",22),background="#50A6F3",foreground="green")















root.mainloop()