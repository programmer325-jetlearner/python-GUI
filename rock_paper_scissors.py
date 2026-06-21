from tkinter import *
import random

user_score=0
computer_score=0
choices=["rock","paper","scissors"]

root=Tk()
root.geometry("900x300")
root.title("rock paper scissors game")
root.config(background="#9FA2B2")
heading_lbl=Label(text="rock paper scissors",font=("Calbiri",20,"bold"),bg="#9FA2B2",fg="black")
heading_lbl.pack()
winner_lbl=Label(text="let the games begin",font=("Calbiri",18,"normal"),bg="#9FA2B2",fg="blue",pady=8)
winner_lbl.pack()
frame=Frame(root,background="#9FA2B2")
frame.pack()
player_options_lbl=Label(frame,text="your options: ",font=("Calbiri",18,"normal"),bg="#9FA2B2",fg="dark green")
player_options_lbl.grid(row=0,column=0,pady=8)
rock_btn=Button(frame,text="rock",font=("Calbiri",18,"bold"),background="#274853",fg="white",width=12,pady=5)
rock_btn.grid(row=1,column=1,padx=8,pady=5)
paper_btn=Button(frame,text="paper",font=("Calbiri",18,"bold"),background="#15357A",fg="white",width=12,pady=5)
paper_btn.grid(row=1,column=2,padx=8,pady=5)
scissors_btn=Button(frame,text="scissors",font=("Calbiri",18,"bold"),background="#520000",fg="white",width=12,pady=5)
scissors_btn.grid(row=1,column=3,padx=8,pady=5)











root.mainloop()