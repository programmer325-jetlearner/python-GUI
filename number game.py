from tkinter import *
import random
import tkinter.messagebox
val1=random.randint(1,10)
val2=random.randint(1,10)
def name():
    name=name_entry.get()
    tkinter.messagebox.showinfo("name",f"hello {name} im thinking of a number that is the multiple of {val1} and {val2}, can you guess it!??")

def check():
    answer=val1*val2
    user_input=answer_entry.get()
    user_input=int(user_input)
    if user_input==answer:
        tkinter.messagebox.showinfo("correct","good job, you have put the correct answer!!!")
    else:
        tkinter.messagebox.showinfo("wrong","you have the incorrect answer, try again!")

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
ok_btn=Button(root,text="OK",font=("Arial",18,"bold"),background="violet",foreground="white",command=name)
ok_btn.place(x=380,y=110,width=100,height=35)
value_lbl=Label(root,text="enter the answer: ",font=("Arial",18,"bold"),background="#845033",fg="orange")
value_lbl.place(x=30,y=300)
answer_entry=Entry(root)
answer_entry.place(x=250,y=310,height=32)
ok2_btn=Button(root,text="check",font=("Calibri",18,"bold"),background="red",foreground="pink",command=check)
ok2_btn.place(x=390,y=310,width=100,height=35)








root.mainloop()