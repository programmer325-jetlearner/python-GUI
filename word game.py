import random
from tkinter import *
import tkinter.messagebox




root=Tk()
root.geometry("500x500+500+150")
root.title("word decipher game")
root.configure(background="#23CE6B")



score=0
lives=3

score_lbl=Label(root,text="score:",font=("Verdana",15,"bold"),background="#23CE6B",foreground="red")
score_lbl.grid(row=0,column=0,padx=10)
lives_lbl=Label(root,text="lives:",font=("Verdana",15,"bold"),background="#23CE6B",foreground="blue")
lives_lbl.grid(row=1,column=0,padx=10)
decode_word_lbl=Label(root,text="hello",font=("Verdana",30,"bold"),background="#23CE6B",foreground="black")
decode_word_lbl.grid(row=10,column=8)
entry=Entry(root,width=50)
entry.grid(row=12,column=8,pady=10)
check_btn=Button(root,text="CHECK",font=("Verdana",30,"bold"),background="green",foreground="yellow")
check_btn.grid(row=15,column=8,pady=20)
reset_btn=Button(root,text="RESET",font=("Verdana",30,"bold"),background="#FF521B",foreground="#A01A7D")
reset_btn.grid(row=18,column=8,pady=20)












root.mainloop()