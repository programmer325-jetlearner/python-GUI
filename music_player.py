from tkinter import *
from tkinter.filedialog import *

root=Tk()
root.configure(background="#989FCE")
root.title("music player")
root.geometry("500x500")


play_btn=Button(root,text="PLAY",font=("Arial",40,"bold"),background="#BFCC94",foreground="black")
play_btn.pack(side=LEFT)

play_lbl=Label(root,text="Now Playing",font=("Arial",30,"bold"),background=("#E6AACE"),foreground="black")
play_lbl.place(x=150,y=50)

listbox=Listbox(root)
listbox.pack(side=RIGHT,padx=20)

























root.mainloop()