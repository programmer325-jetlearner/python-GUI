from tkinter import *
from tkinter.ttk import *


coffee_options=["cappuccino","americano","espresso"]

root=Tk()
root.title("coffee machine")
root.config(background="#4AE89C")
root.geometry("500x500")

drink_lbl=Label(root,text="drink: ",font=("Arial",18,"bold"),background="#4AE89C",foreground="black")
drink_lbl.place(x=150,y=40)

coffee_box=Combobox(root,textvariable=coffee_options,width=6,state="readonly")
coffee_box.place(x=250,y=40)


sugar_lbl=Label(root,text="sugar",font=("Arial",18,"bold"),background="#4AE89C",foreground="black")
sugar_lbl.place(x=150,y=140)

r_no=Radiobutton(root,text="none",value=10)
r_low=Radiobutton(root,text="low",value=20)
r_high=Radiobutton(root,text="high",value=30)

r_no.place(x=230,y=150)
r_low.place(x=310,y=150)
r_high.place(x=390,y=150)


milk_lbl=Label(root,text="milk: ",font=("Arial",18,"bold"),background=("#4AE89C"),foreground="black")








root.mainloop()