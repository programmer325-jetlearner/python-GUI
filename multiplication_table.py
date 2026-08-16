from tkinter import *
from tkinter import ttk


def generate_table():
    tables=""
    for i in range(1,end_val.get()+1):
        mult=num.get() * i
        tables+=f"{num.get()} X {i} = {mult} \n"
    display_lbl.configure(text=tables)


root=Tk()
root.config(background="#4A5899")
root.title("multiplication table")

title_lbl=Label(root,text="multiplication table",font=("Comic Sans",35,"bold"),background="#4A5899",foreground="#F0A868")
title_lbl.grid(row=0,column=0,columnspan=3,pady=25)
number_lbl=Label(root,text="number range: ",font=("Comic Sans",18,"bold"),background="#4A5899",foreground="#C0C5C1")
number_lbl.grid(column=0,row=1,padx=10)
#combo box creation
num=IntVar()
numbers_box=ttk.Combobox(root,textvariable=num,width=6,state="readonly")
numbers_box.grid(row=1,column=1)
numbers_box["values"]=tuple(range(101))

#radio button creation
end_val=IntVar()
r10=Radiobutton(root,text="10",variable=end_val,value=10,bg="#4A5899",fg="white",selectcolor="black")
r10.grid(row=1,column=2)
r20=Radiobutton(root,text="20",variable=end_val,value=20,bg="#4A5899",fg="white",selectcolor="black")
r20.grid(row=2,column=2,padx=30)
r30=Radiobutton(root,text="30",variable=end_val,value=30,bg="#4A5899",fg="white",selectcolor="black")
r30.grid(row=3,column=2,padx=30)
end_val.set(10)

generate_btn=Button(root,text="generate",bg="#F4A5AE",fg="black",width=20,command=generate_table)
generate_btn.grid(row=4,column=0)

display_lbl=Label(root,background="#4A5899",foreground="black",font=("Arial",15,"bold"))
display_lbl.grid(row=5,column=1,pady=25)









root.mainloop()