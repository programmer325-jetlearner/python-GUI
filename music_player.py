from tkinter import *
from tkinter.filedialog import *

root=Tk()
root.configure(background="#989FCE")
root.title("music player")
root.geometry("1000x800")

def play():
    selected_index=listbox.curselection()[0]
    song_name=songs[selected_index]
    if song_name:
        play_lbl.config(text=f"Now playing {song_name}:")




songs=["like a rolling stone","i cant get no satisfaction","imagine","whats going on","respect"]

play_btn=Button(root,text="PLAY",font=("Arial",40,"bold"),background="#BFCC94",foreground="black",command=play)
play_btn.pack(side=LEFT)

play_lbl=Label(root,text="Now Playing",font=("Arial",30,"bold"),background=("#E6AACE"),foreground="black")
play_lbl.place(x=150,y=50)

scrollbar=Scrollbar(root,orient="vertical")
scrollbar.pack(side=RIGHT)

listbox=Listbox(root,yscrollcommand=scrollbar.set,background="blue",foreground="yellow")
listbox.pack(side=RIGHT,padx=20)
i=0
for song in songs:
    listbox.insert(END, song)
scrollbar.config(command=listbox.yview)
























root.mainloop()