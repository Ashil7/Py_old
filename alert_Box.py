from tkinter import *
from tkinter import messagebox

window=Tk()
window.geometry("250x150")
window.resizable(0,0)
def message():

    messagebox.showwarning("Alert Box","Stop VIRUS Found")


ok=Button(window,text="OK",command=message)
ok.place(x=100,y=100)

window.mainloop()