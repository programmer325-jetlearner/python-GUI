from tkinter import *
from tkinter.ttk import *

root=Tk()
root.geometry("500x500")
root.config(bg="red")

def change_color():
    color=end_val.get()
    if color=="red":
        root.config(background="red")
    elif color=="green":
        root.config(background="green")
    elif color=="blue":
        root.config(background="blue")



lbl=Label(root,text="choose background color",font=("Arial",18,"bold"),background="red",foreground="black")
lbl.pack()
end_val=StringVar()
r10=Radiobutton(root,text="red",variable=end_val,value="red",command=change_color)
r10.place(x=100,y=250)
r20=Radiobutton(root,text="green",variable=end_val,value="green",command=change_color)
r20.place(x=200,y=250)
r30=Radiobutton(root,text="blue",variable=end_val,value="blue",command=change_color)
r30.place(x=300,y=250)
end_val.set("red")












root.mainloop()