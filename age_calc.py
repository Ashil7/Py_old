from tkinter import *
from datetime import date

def calculate():
    global result
    result=str(entry.get())
    today=date.today()
    dob_data=result.split("/")
    date1=int(dob_data[0])
    month=int(dob_data[1])
    year=int(dob_data[2])
    dob=date(year,month,date1)
    numberOfDays=(today-dob).days
    age=numberOfDays//365
    label=Label(window,text="AGE : " +str(age))
    label.pack()

window=Tk()
window.geometry('800x400')
window.resizable(0,0)
entry=Entry(window)
entry.pack()

but=Button(window,text="calculate your age",font=("arial",20,"bold"),command=calculate)
but.pack()
window.mainloop()