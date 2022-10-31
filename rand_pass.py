from tkinter import *
import random
import string

window=Tk()
window.geometry("1280x720")
window.configure(bg="white")


def gen():
    password=[]
    for i in range(4):
        lower=random.choice(string.ascii_lowercase)
        upper=random.choice(string.ascii_uppercase)
        password.append(lower)
        password.append(upper)
        passs="".join(str(x)for x in password)
        label.config(text=passs)

label=Label(window,font=('arial',40,'bold'))
label.pack()

but=Button(window,text="Generate",font=('arial',40,'bold'),command=gen).place(x=500,y=300)


window.mainloop()