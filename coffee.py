from tkinter import *
from tkinter.ttk import Combobox


def brew():
    string=""
    combo=coffee_box.get()
    sugar_choice=end_val.get()
    milk_choice=end_value.get()
    string=f"brewing some {combo} with {sugar_choice} sugar and using {milk_choice} milk"
    brew_lbl.configure(text=string)











root=Tk()
root.title("coffee machine")
root.config(background="#4AE89C")
root.geometry("1000x500")

coffee_list=["espresso","americano","cappuccino","black coffee"]


drink_lbl=Label(root,text="drink: ",font=("Arial",18,"bold"),background="#4AE89C",foreground="black")
drink_lbl.place(x=150,y=40)

coffee_box=Combobox(root,value=coffee_list,width=6,state="readonly")
coffee_box.place(x=250,y=40)


sugar_lbl=Label(root,text="sugar",font=("Arial",18,"bold"),background="#4AE89C",foreground="black")
sugar_lbl.place(x=150,y=140)

end_val=StringVar()

r_no=Radiobutton(root,text="none",value="none",variable=end_val)
r_low=Radiobutton(root,text="low",value="low",variable=end_val)
r_high=Radiobutton(root,text="high",value="high",variable=end_val)

end_val.set("none")


r_no.place(x=230,y=150)
r_low.place(x=310,y=150)
r_high.place(x=390,y=150)




milk_lbl=Label(root,text="milk: ",font=("Arial",18,"bold"),background=("#4AE89C"),foreground="black")
milk_lbl.place(x=150,y=240)

end_value=StringVar()

r_dairy=Radiobutton(root,text="dairy",value="dairy",variable=end_value)
r_soy=Radiobutton(root,text="soy",value="soy",variable=end_value)
r_almond=Radiobutton(root,text="almond",value="almond",variable=end_value)

end_value.set("dairy")

r_dairy.place(x=230,y=240)
r_soy.place(x=310,y=240)
r_almond.place(x=390,y=240)

brew_btn=Button(root,text="brew",command=brew)
brew_btn.place(x=250,y=340,width=100)

brew_lbl=Label(root,text="",font=("Arial",18,"bold"),background="#4AE89C",foreground="black")
brew_lbl.place(x=10,y=440)







root.mainloop()