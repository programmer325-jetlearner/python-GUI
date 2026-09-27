import random
from tkinter import *
import tkinter.messagebox

root=Tk()
root.geometry("500x500+500+150")
root.title("word jumble")
root.configure(background="#50A6F3")

answers=["building","icecream","vehicle","truck","crayon","animal","crystal","donut","milk","baby","place","brain"]
words=["dnbligiu","riacecme","evhceli","ctrku","ncayor","amanil","csyralt","ndotu","imkl","yabb","pcale","ibnar"]

score_text=""
score=0
l=Label(root)
num=random.randrange(0,len(words),1)
q_count=0

def default():
    global num, words
    jumble_lbl.config(text=words[num])
def reset():
    global num, words
    num=random.randrange(0,len(words),1)
    jumble_lbl.config(text=words[num])
    input_box.delete(0, END)
def check_ans():
    global l, score,score_text,num,q_count,words,answers
    q_count+=1
    ans=input_box.get()
    if ans==answers[num]:
        tkinter.messagebox.showinfo("congratulations","YOU ARE CORRECT!!")
        score+=1
    else:
        tkinter.messagebox.showerror("sorry","you have got the wrong answer")
    score_text=f"score: {score}/{q_count}"
    l.forget()
    l=Label(root,text=score_text,font=("Verdana",20,"normal"),bg="#50A6F3",foreground="#8C1267")
    l.pack(side=LEFT)
    reset()


heading_lbl=Label(root,text="JUMBLE WORD GAME",background="#50A6F3",foreground="#1E382B",font=("Verdana",30,"bold"))
heading_lbl.pack(pady=5)
jumble_lbl=Label(root,font=("Verdana",22),background="#50A6F3",foreground="#081E2F")
jumble_lbl.pack(pady=30,ipadx=10,ipady=10)
ans=StringVar()
input_box=Entry(root,font=("Verdana",22),justify="center",textvariable=ans)
input_box.pack(ipady=5,ipadx=5)
check_btn=Button(root,text="check",font=("Verdana",20,"bold"),width=10,background="#F7971E",foreground="red",command=check_ans)
check_btn.pack(pady=40)
reset_btn=Button(root,text="reset",background="#E5E327",foreground="#C49A5A",font=("Verdana",20,"bold"),width=10,command=reset)
reset_btn.pack()
score_label=Label(root,text="10",font=("Verdana",22),background="#50A6F3",foreground="green")
default()






root.mainloop()