from tkinter import *
import tkinter.messagebox
import random

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
btn_ok=Button(root,text="ok",font=("Arial",18,"bold"),bg="yellow",fg="black")
btn_ok.place(x=400,y=90)
guess_lbl=Label(root,text="make your guess: ",font=("Arial",18,"bold"),bg="#0090A3",fg="dark red")
guess_lbl.place(x=10,y=250)
guess_entry=Entry(root)
guess_entry.place(x=230,y=250,height=30)









root.mainloop()