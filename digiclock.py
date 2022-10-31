from tkinter import *
import time
digiclock=Tk()
digiclock.geometry("1100x300")
digiclock.configure(bg="black")

def update():
    clk.configure(text=time.strftime("%I:%M:%S"))
    clk.after(1000,update)



clk=Label(digiclock,bg="black",foreground="red",font=('arial',40,'bold'))
clk.pack()

update()

digiclock.mainloop()