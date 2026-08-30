from tkinter import *
from tkinter.filedialog import *

root=Tk()
root.title("memorizer")
root.configure(background="#246A73")





open_btn=Button(root,text="OPEN",width=15,background="white",foreground="black",font=("Calibri",18,"bold"))
open_btn.pack(side=LEFT,padx=5,pady=5)
delete_btn=Button(root,text="DELETE",width=15,background="white",foreground="black",font=("Calibri",18,"bold"))
delete_btn.pack(side=RIGHT,padx=5,pady=5)
add_btn=Button(root,text="ADD",width=15,background="white",foreground="black",font=("Calibri",18,"bold"))
add_btn.pack(padx=5,pady=5)
item=Entry(root,width=35)
item.pack(padx=5,pady=5)
save_btn=Button(root,text="SAVE",width=15,background="white",foreground="black",font=("Calibri",18,"bold"))
save_btn.pack(padx=5,pady=5)


frame=Frame(root)
frame.pack(side=RIGHT)
scrollbar=Scrollbar(frame,orient="vertical")
scrollbar.pack(side=RIGHT,fill=Y)





















root.mainloop()