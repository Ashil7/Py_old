from tkinter import *
from tkinter import messagebox

count=0
board=[['','',''],
       ['','',''],
       ['','','']]

def displayWinner(winner):
    global root,WinnerWin,Id
    WinnerWin=Tk()
    WinnerWin.configure(bg='black')
    l1 = Label(WinnerWin, text="THE WINNER IS: ", font=("arial", 15), bg="Black", fg="White")
    l1.pack()
    l2 = Label(WinnerWin, text=winner, font=("COMIC SANS MS", 15), bg="Black", fg="White")
    l2.pack()

def CheckWinner():
    global count,board
    if (board[0][0]==board[0][1]==board[0][2]=="X" or board[1][0]==board[1][1]==board[1][2]=="X" or board[2][0]==board[2][1]==board[2][2]=="X" or
        board[0][0]==board[1][0]==board[2][0]=="X" or board[0][1]==board[1][1]==board[2][1]=="X" or board[0][2]==board[1][2]==board[2][2]=="X" or
        board[0][0]==board[1][1]==board[2][2]=="X" or board[0][2]==board[1][1]==board[2][0]=="X"):
            displayWinner("Player X")
    elif (board[0][0]==board[0][1]==board[0][2]=="O" or board[1][0]==board[1][1]==board[1][2]=="O" or board[2][0]==board[2][1]==board[2][2]=="O" or
          board[0][0]==board[1][0]==board[2][0]=="O" or board[0][1]==board[1][1]==board[2][1]=="O" or board[0][2]==board[1][2]==board[2][2]=="O" or
          board[0][0]==board[1][1]==board[2][2]=="O" or board[0][2]==board[1][1]==board[2][0]=="O"):
            displayWinner("Player O")
    elif count==9:
        displayWinner("NONE! IT IS A TIE!")

def ChangeVal(button,boardVaR,boardVaC):
    global count

    if button["text"]=="":
        if count % 2==0:
            button["text"]="X"
            l1=Label(root,text='Player 2 (O)',height=3,font=('arial',12,'bold'),bg='grey').grid(row=0,column=1)
            board[boardVaR][boardVaC]='X'
        else:
            button["text"]="O"
            l2=Label(root,text='Player 1 (X)',height=3,font=('arial',12,'bold'),bg='grey').grid(row=0,column=1)
            board[boardVaR][boardVaC]='O'
        count=count+1
        if count>=5:
            CheckWinner()
    else:
         messagebox.showerror("Error","!")

def TicTacToe():
    global root
    root =Tk()
    root.title("TIC TAC TOE Game")
    root.configure(bg="grey")

    l1 = Label(root, text='Player 1 (X)', height=3, font=('arial', 12, 'bold'), bg='grey').grid(row=0, column=1)



    b01=Button(root,text="",height=5,width=10,bg='white',activebackground="black",fg="black",font=('arial',18,'bold'),command=lambda: ChangeVal(b01,0,0))
    b02=Button(root,text="",height=5,width=10,bg='white',activebackground="black",fg="black",font=('arial',18,'bold'),command=lambda: ChangeVal(b02,0,1))
    b03=Button(root,text="",height=5,width=10,bg='white',activebackground="black",fg="black",font=('arial',18,'bold'),command=lambda: ChangeVal(b03,0,2))
    b04=Button(root,text="",height=5,width=10,bg='white',activebackground="black",fg="black",font=('arial',18,'bold'),command=lambda: ChangeVal(b04,1,0))
    b05=Button(root,text="",height=5,width=10,bg='white',activebackground="black",fg="black",font=('arial',18,'bold'),command=lambda: ChangeVal(b05,1,1))
    b06=Button(root,text="",height=5,width=10,bg='white',activebackground="black",fg="black",font=('arial',18,'bold'),command=lambda: ChangeVal(b06,1,2))
    b07=Button(root,text="",height=5,width=10,bg='white',activebackground="black",fg="black",font=('arial',18,'bold'),command=lambda: ChangeVal(b07,2,0))
    b08=Button(root,text="",height=5,width=10,bg='white',activebackground="black",fg="black",font=('arial',18,'bold'),command=lambda: ChangeVal(b08,2,1))
    b09=Button(root,text="",height=5,width=10,bg='white',activebackground="black",fg="black",font=('arial',18,'bold'),command=lambda: ChangeVal(b09,2,2))


    b01.grid(row=2,column=0)
    b02.grid(row=2,column=1)
    b03.grid(row=2,column=2)

    b04.grid(row=3,column=0)
    b05.grid(row=3,column=1)
    b06.grid(row=3,column=2)

    b07.grid(row=4, column=0)
    b08.grid(row=4, column=1)
    b09.grid(row=4, column=2)

TicTacToe()
root.mainloop()

