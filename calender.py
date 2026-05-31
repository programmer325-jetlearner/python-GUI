from tkinter import *
import calendar

def showcal():
    new_root=Tk()
    new_root.config(background="cyan")
    new_root.title("calender window")
    new_root.geometry("550x550")
    fetch_year=int(year_box.get())
    cal_content=calendar.calendar(fetch_year)
    cal_year=Label(new_root,text=cal_content,font=("Consolas",10,"bold"))
    cal_year.grid(row=5,column=1,padx=20)
    new_root.mainloop()


#main window
root=Tk()
root.config(background="yellow")
root.title("calendar")
root.geometry("250x200")
cal_label=Label(root,text="calendar",bg="red",font=("Arial",28,"bold"))
cal_label.pack()
year_label=Label(root,text="enter year",bg="blue",fg="white",font=("Times",18,"bold"))
year_label.pack()
year_box=Entry(root)
year_box.pack()
show_btn=Button(root,text="show calendar",bg="green",fg="white",font=("Arial",18,"bold"),command=showcal)
show_btn.pack()
exit_btn=Button(root,text="exit",bg="green",fg="white",font=("Arial",18,"bold"),command=exit)
exit_btn.pack()













root.mainloop()
