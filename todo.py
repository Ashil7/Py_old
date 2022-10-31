from tkinter import *
window=Tk()

label= Label(window,bg='cyan',text="TO_DO_LIST")
label.pack()

list=Listbox(window,width=200,height=200,bg='yellow')
list.insert(1,'I')
list.insert(2,'AM')
list.insert(3,'A')
list.insert(4,'legend')
list.pack()

window.configure(bg='Black')
window.geometry('400x400')
window.title("TO - Do")
window.resizable(0,0)










window.mainloop()