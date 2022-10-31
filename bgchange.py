from tkinter import *
from random import randint

change=Tk()
def colorch():
    color="%05x" %randint(0,0xFFFFFF)
    change.configure(bg='#00F5FF'+color)
    change.after(200,colorch)

colorch()
change.geometry("400x300")
change.title("BG Changer")


change.mainloop()