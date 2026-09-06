from tkinter import *
from tkinter.filedialog import *

root=Tk()
root.title("memorizer")
root.configure(background="#246A73")


def addItem():
    listbox.insert(END, item.get())
    item.delete(0, END)
def deleteItem():
    index=listbox.curselection()
    if index:
        listbox.delete(index)
    
def save_file():
    file=asksaveasfile(defaultextension=".txt")
    if file is not None:
        for item in listbox.get(0, END):
            print(item.strip(),file=file)
        listbox.delete(0,END)
def open_file():
    file=askopenfile(title="open file")
    if file is not None:
        listbox.delete(0,END)
        items=file.readlines()
        for item in items:
            listbox.insert(END,item.strip())





open_btn=Button(root,text="OPEN",width=15,background="white",foreground="black",font=("Calibri",18,"bold"),command=open_file)
open_btn.pack(side=LEFT,padx=5,pady=5)
delete_btn=Button(root,text="DELETE",width=15,background="white",foreground="black",font=("Calibri",18,"bold"),command=deleteItem)
delete_btn.pack(side=RIGHT,padx=5,pady=5)
add_btn=Button(root,text="ADD",width=15,background="white",foreground="black",font=("Calibri",18,"bold"),command=addItem)
add_btn.pack(padx=5,pady=5)
item=Entry(root,width=35)
item.pack(padx=5,pady=5)
save_btn=Button(root,text="SAVE",width=15,background="white",foreground="black",font=("Calibri",18,"bold"),command=save_file)
save_btn.pack(padx=5,pady=5)


frame=Frame(root)
frame.pack(side=RIGHT)
scrollbar=Scrollbar(frame,orient="vertical")
scrollbar.pack(side=RIGHT,fill=Y)



listbox=Listbox(frame,width=70,yscrollcommand=scrollbar.set,background="green",foreground="white")
for i in range(1,11):
    listbox.insert(END, f"List{i}")
listbox.pack(side=LEFT,padx=5)
scrollbar.config(command=listbox.yview)



















root.mainloop()