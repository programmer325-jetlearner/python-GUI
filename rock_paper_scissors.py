from tkinter import *
import random

user_score=0
computer_score=0
choices=["rock","paper","scissors"]


def computer_wins():
    global computer_score, user_score
    computer_score+=1
    winner_lbl.config(text="COMPUTER WINS!!!")
    computer_score_lbl.config(text=f"computer score: {computer_score}")
    player_score_lbl.config(text=f"player score: {user_score}")

def player_wins():
    global computer_score, user_score
    user_score+=1
    winner_lbl.config(text="PLAYER WINS!!!")
    computer_score_lbl.config(text=f"computer score: {computer_score}")
    player_score_lbl.config(text=f"player score: {user_score}")

def tie():
    global computer_score, user_score
    winner_lbl.config(text="TIE!!!")
    computer_score_lbl.config(text=f"computer score: {computer_score}")
    player_score_lbl.config(text=f"player score: {user_score}")

def computer_choice():
    return random.choice(choices)

def player_choice(player_input):
    global computer_score, user_score
    print(f"player choice: {player_input}")
    player_choice_lbl.config(text=f"you selected: {player_input}")
    computer_input=computer_choice()
    print(computer_input)
    computer_choice_lbl.config(text=f"computer selected: {computer_input}")

    if computer_input==player_input:
        tie()
    if player_input=="rock":
        if computer_input=="scissors":
            player_wins()
        elif computer_input=="paper":
            computer_wins()
    if player_input=="paper":
        if computer_input=="rock":
            player_wins()
        elif computer_input=="scissors":
            computer_wins()
    if player_input=="scissors":
        if computer_input=="paper":
            player_wins()
        elif computer_input=="rock":
            computer_wins()
            
    






root=Tk()
root.geometry("900x600")
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

score_lbl=Label(frame,text="score: ",font=("Calbiri",18,"normal"),bg="#9FA2B2",fg="dark green")
score_lbl.grid(row=2,column=0)
player_choice_lbl=Label(frame,text="you selected: ",font=("Calbiri",18,"normal"),bg="#9FA2B2",fg="red")
player_choice_lbl.grid(row=3,column=1,pady=5)
player_score_lbl=Label(frame,text="your score: ",font=("Calbiri",18,"normal"),bg="#9FA2B2",fg="red")
player_score_lbl.grid(row=3,column=2,pady=5)
computer_choice_lbl=Label(frame,text="computer selected: ",font=("Calbiri",18,"normal"),bg="#9FA2B2",fg="red")
computer_choice_lbl.grid(row=4,column=1,pady=5)
computer_score_lbl=Label(frame,text="computer score: ",font=("Calbiri",18,"normal"),bg="#9FA2B2",fg="red")
computer_score_lbl.grid(row=4,column=2,pady=5)











root.mainloop()