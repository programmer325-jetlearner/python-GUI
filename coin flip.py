from tkinter import *
import random


user_score=0
computer_score=0
correct_list=["heads","tails"]

computer_choice=""

def heads():

    correct=random.choice(correct_list)
    player_choice_lbl.config(text="you selected heads")
    if correct=="heads":
        winner_lbl.config(text="USER WON!!!")
    else:
        winner_lbl.config(text="COMPUTER WON!!!")

def tails():

    correct=random.choice(correct_list)
    player_choice_lbl.config(text="you selected tails")
    if correct=="tails":
        winner_lbl.config(text="USER WON!!!")
    else:
        winner_lbl.config(text="COMPUTER WON!!!")


root=Tk()
root.geometry("900x600")
root.title("coinflip")
root.config(background="#213BCB")
heading_lbl=Label(text="coinflip",font=("Calbiri",20,"bold"),bg="#213BCB",fg="black")
heading_lbl.pack()
winner_lbl=Label(text="let the games begin",font=("Calbiri",18,"normal"),bg="#213BCB",
fg="black")
winner_lbl.pack()
frame=Frame(root,background="#213BCB")
frame.pack()
player_options_lbl=Label(frame,text="your options: ",font=("Calbiri",18,"normal"),bg="#213BCB",fg="grey")
player_options_lbl.grid(row=0,column=0,pady=8)
heads_btn=Button(frame,text="heads",font=("Calbiri",18,"bold"),background="#3B9960",fg="white",width=12,pady=5,command=heads)
heads_btn.grid(row=1,column=1,padx=8,pady=5)
tails_btn=Button(frame,text="tails",font=("Calbiri",18,"bold"),background="#69BA28",fg="white",width=12,pady=5,command=tails)
tails_btn.grid(row=1,column=2,padx=8,pady=5)
score_lbl=Label(frame,text="score: ",font=("Calbiri",18,"normal"),bg="#213BCB",fg="black")
score_lbl.grid(row=2,column=0)
player_choice_lbl=Label(frame,text="you selected: ",font=("Calbiri",18,"normal"),bg="#213BCB",fg="orange")
player_choice_lbl.grid(row=3,column=1,pady=5)
player_score_lbl=Label(frame,text="your score: ",font=("Calbiri",18,"normal"),bg="#213BCB",fg="orange")
player_score_lbl.grid(row=3,column=2,pady=5)



root.mainloop()