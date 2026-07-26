from tkinter import *
import tkinter.messagebox
import random


num=random.randint(1,20)

def check_num():
    guess=guess_entry.get()
    guess=int(guess)

    if guess==num:
        tkinter.messagebox.showinfo("correct","Congratulations you guessed it correctly!!!")
    elif guess<num:
        tkinter.messagebox.showinfo("low","your answer is too low")
    else:
        tkinter.messagebox.showinfo("high","your answer is too high")

def name_confirm():
    name=name_entry.get()
    tkinter.messagebox.showinfo("name",f"hello {name} im thinking of a number between 1 and 20, can you guess it???")

root=Tk()
root.geometry("500x500")
root.title("guess the number")
root.configure(background="#0090A3")

heading_lbl=Label(root,text="Guessing game",font=("Arial",30,"bold"),bg="#0090A3",fg="black")
heading_lbl.pack()
name_lbl=Label(root,text="enter your name: ",font=("Arial",18,"bold"),bg="#0090A3",fg="dark blue")
name_lbl.place(x=10,y=80)
name_entry=Entry(root)
name_entry.place(x=230,y=90,height=30)
btn_ok=Button(root,text="ok",font=("Arial",18,"bold"),bg="yellow",fg="black",command=name_confirm)
btn_ok.place(x=380,y=90,width=100,height=35)
guess_lbl=Label(root,text="make your guess: ",font=("Arial",18,"bold"),bg="#0090A3",fg="dark red")
guess_lbl.place(x=10,y=250)
guess_entry=Entry(root)
guess_entry.place(x=230,y=250,height=30)
btn_check=Button(root,text="guess",font=("Arial",18,"bold"),bg="green",fg="white",command=check_num)
btn_check.place(x=380,y=250,width=100,height=35)













root.mainloop()