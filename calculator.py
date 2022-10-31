from tkinter import *



def btn_click(item):
    global expression
    expression=expression+str(item)
    text_input.set(expression)

def btn_clear():
    global expression
    expression=""
    text_input.set(expression)

def btn_equal(result):
   try:
    global expression
    result=str(eval(expression))
    text_input.set(result)
    expression=" "
   except:
     result=print("Error")
     text_input.set(result)
     expression=""

expression=""

cal=Tk()

cal.geometry("420x500")
cal.configure(bg="#222121")
cal.title("Calculator")
cal.resizable(0,0)

text_input=StringVar()
text_area=Frame(cal, width=420, height=150, background="#373434")
text_area.pack(side=TOP)

text_field=Entry(text_area,font=('arial',16,'bold',),foreground="grey",textvariable=text_input,width=50, background="#373434", justify=RIGHT)
text_field.grid(row=0,column=0)
text_field.pack(ipady=50)

btn_frame=Frame(cal,width=420, height=400, bg="#373434")
btn_frame.pack()

clear=Button(btn_frame,text="Clear",fg="black",width=36,height=3,background="orange",cursor="hand2",command=lambda: btn_clear())
clear.grid(row=0,column=0,columnspan=3,padx=1,pady=1)
divide=Button(btn_frame,text="/",fg="black",width=13,height=3,background="orange",cursor="hand2",command=lambda: btn_click("/"))
divide.grid(row=0,column=3,padx=1,pady=1)

one=Button(btn_frame,text="1",fg="white",width=11,height=3,background="#222121",cursor="hand2",command=lambda: btn_click("1"))
one.grid(row=1,column=0,padx=1,pady=1)
two=Button(btn_frame,text="2",fg="white",width=11,height=3,background="#222121",cursor="hand2",command=lambda: btn_click("2"))
two.grid(row=1,column=1,padx=1,pady=1)
three=Button(btn_frame,text="3",fg="white",width=11,height=3,background="#222121",cursor="hand2",command=lambda: btn_click("3"))
three.grid(row=1,column=2,padx=1,pady=1)
multiply=Button(btn_frame,text="*",fg="black",width=13,height=3,background="orange",cursor="hand2",command=lambda: btn_click("*"))
multiply.grid(row=1,column=3,padx=1,pady=1)


four=Button(btn_frame,text="4",fg="white",width=11,height=3,background="#222121",cursor="hand2",command=lambda: btn_click("4"))
four.grid(row=2,column=0,padx=1,pady=1)
five=Button(btn_frame,text="5",fg="white",width=11,height=3,background="#222121",cursor="hand2",command=lambda: btn_click("5"))
five.grid(row=2,column=1,padx=1,pady=1)
six=Button(btn_frame,text="6",fg="white",width=11,height=3,background="#222121",cursor="hand2",command=lambda: btn_click("6"))
six.grid(row=2,column=2,padx=1,pady=1)
subtract=Button(btn_frame,text="-",fg="black",width=13,height=3,background="orange",cursor="hand2",command=lambda: btn_click("-"))
subtract.grid(row=2,column=3,padx=1,pady=1)

seven=Button(btn_frame,text="7",fg="white",width=11,height=3,background="#222121",cursor="hand2",command=lambda: btn_click("7"))
seven.grid(row=3,column=0,padx=1,pady=1)
eight=Button(btn_frame,text="8",fg="white",width=11,height=3,background="#222121",cursor="hand2",command=lambda: btn_click("8"))
eight.grid(row=3,column=1,padx=1,pady=1)
nine=Button(btn_frame,text="9",fg="white",width=11,height=3,background="#222121",cursor="hand2",command=lambda: btn_click("9"))
nine.grid(row=3,column=2,padx=1,pady=1)
add=Button(btn_frame,text="+",fg="black",width=13,height=3,background="orange",cursor="hand2",command=lambda: btn_click("+"))
add.grid(row=3,column=3,padx=1,pady=1)

zero=Button(btn_frame,text="0",fg="white",width=23,height=3,background="#222121",cursor="hand2",command=lambda: btn_click("0"))
zero.grid(row=4,column=0,columnspan=2,padx=1,pady=1)
comma=Button(btn_frame,text=".",fg="white",width=11,height=3,background="#222121",cursor="hand2",command=lambda: btn_click("."))
comma.grid(row=4,column=2,padx=1,pady=1)
equal=Button(btn_frame,text="=",fg="black",width=13,height=3,background="orange",cursor="hand2",command=lambda: btn_equal("="))
equal.grid(row=4,column=3,padx=1,pady=1)




cal.mainloop()