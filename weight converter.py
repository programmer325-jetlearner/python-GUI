from tkinter import *

root=Tk()
root.configure(background="#8ABD61")

#function to convert weight
def convert():
    gram=float(weight_box.get())*1000
    pound=float(weight_box.get())*2.20462
    ounce=float(weight_box.get())*35.274

    t1.delete("1.0",END)
    t1.insert(END,gram)

    t2.delete("1.0",END)
    t2.insert(END,pound)
    t3.delete("1.0",END)
    t3.insert(END,ounce)

#create the label widgets
weight_lbl=Label(root,text="enter the weight in kg: ",font=("Roboto",16,"bold"),foreground="black",background="#8ABD61")
weight_lbl.grid(row=0,column=0)
weight_val=StringVar()
weight_box=Entry(root,textvariable=weight_val,width=20)
weight_box.grid(row=0,column=1)
grams_lbl=Label(root,text="grams",font=("Roboto",16,"bold"),background="#8ABD61",foreground="#1F446B")
grams_lbl.grid(row=1,column=0)
pounds_lbl=Label(root,text="pounds",font=("Roboto",16,"bold"),background="#8ABD61",foreground="#1F446B")
pounds_lbl.grid(row=1,column=1,pady=8)
ounce_lbl=Label(root,text="ounces",font=("Roboto",16,"bold"),background="#8ABD61",foreground="#1F446B")
ounce_lbl.grid(row=1,column=2)
#create the text widgets
t1=Text(root,height=1,width=30)
t1.grid(row=2,column=0)
t2=Text(root,height=1,width=30)
t2.grid(row=2,column=1)
t3=Text(root,height=1,width=30)
t3.grid(row=2,column=2)
#create the button widget
btn=Button(root,text="convert",font=("Roboto",16,"bold"),background="red",foreground="white",command=convert)
btn.grid(row=0,column=2)


root.mainloop()



