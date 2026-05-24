from tkinter import *
import calendar


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
show_btn=Button(root,text="show calendar",bg="green",fg="white",font=("Arial",18,"bold"))
show_btn.pack()
exit_btn=Button(root,text="exit",bg="green",fg="white",font=("Arial",18,"bold"))
exit_btn.pack()









root.mainloop()
