from tkinter import *
from tkinter import ttk
from tkinter import Tk
from tkinter import messagebox

if __name__ == "__main__":
    window = Tk()
    window.title("Calculator")
    window.geometry("300x300+500+100")
    equation = StringVar()

    TxtNumbers = Entry(window,textvariable=equation,width=30)
    #Text(window,height=2,width=40)
    TxtNumbers.place(x=60,y=20)
    expresion = ""
    #TxtNumbers.get(1.0,"end-1c")
    
    def press(num):
        global expresion
        expresion  = expresion + str(num)
        equation.set(expresion)

    def clear():
        global expresion
        expresion = ""
        equation.set("")

    def error_window():
        top = Toplevel(window)
        top.geometry("560x100")
        top.title("Error Massage")
        top.config(background="black")
        errorLabel = Label(top,text="Inavaled Input !!!!",fg="red",bg="black",font="30",height=3).pack()
        Btn = Button(top,text="OK",width=4,height=2,fg="red",bg='gray',command=top.destroy)
        Btn.pack()
        
    
    def AppendInFile(result):
        global expresion
        file = open("History" , 'a')
        file.write("{} = {} \n".format(expresion,result))
        file.close
    def equale():
        try:
            global expresion
            total = str(eval(expresion))
            equation.set(total)
            AppendInFile(total)
            expresion = ""
        except:
            error_window()
            equation.set("Inavaled Input !!!!")
            expresion = ""
    
    OperFrame = Frame(window).pack()
    BtnFrame = Frame(window,bg="black").pack()
    
    Btn1 = Button(BtnFrame,text="1",width=6,height=2,command=lambda :press(1))
    Btn1.place(x=60,y=60)
    #Btn1.grid(column=1,row=2)

    Btn2 = Button(BtnFrame,text="2",width=6,height=2,command=lambda :press(2))
    Btn2.place(x=110,y=60)

    Btn3 = Button(BtnFrame,text="3",width=6,height=2,command=lambda :press(3))
    Btn3.place(x=160,y=60)

    Btn4 = Button(BtnFrame,text="4",width=6,height=2,command=lambda :press(4))
    Btn4.place(x=60,y=100)

    Btn5 = Button(BtnFrame,text="5",width=6,height=2,command=lambda :press(5))
    Btn5.place(x=110,y=100)

    Btn6 = Button(BtnFrame,text="6",width=6,height=2,command=lambda :press(6))
    Btn6.place(x=160,y=100)

    Btn7 = Button(BtnFrame,text="7",width=6,height=2,command=lambda :press(7))
    Btn7.place(x=60,y=140)

    Btn8 = Button(BtnFrame,text="8",width=6,height=2,command=lambda :press(8))
    Btn8.place(x=110,y=140)

    Btn9 = Button(BtnFrame,text="9",width=6,height=2,command=lambda :press(9))
    Btn9.place(x=160,y=140)

    Btn0 = Button(BtnFrame,text="0",width=6,height=2,command=lambda :press(0))
    Btn0.place(x=110,y=180)

    Btnplus = Button(OperFrame,text="+",width=6,height=2,command=lambda :press("+"))
    Btnplus.place(x=210,y=60)

    Btnmin = Button(OperFrame,text="-",width=6,height=2,command=lambda :press("-"))
    Btnmin.place(x=210,y=100)

    Btnmult = Button(OperFrame,text="x",width=6,height=2,command=lambda :press("*"))
    Btnmult.place(x=210,y=140)

    Btndivd = Button(OperFrame,text="/",width=6,height=2,command=lambda :press("/"))
    Btndivd.place(x=210,y=180)

    BtnQuit = Button(OperFrame,text="Exit",width=6,height=2,bg = "orange",fg="black",command=lambda:quit())
    BtnQuit.place(x=200,y=240)

    BtnClr = Button(OperFrame,text="Clear",width=6,height=2,command=clear)
    BtnClr.place(x=160,y=180)
    
    BtnEqual = Button(OperFrame,text="=",width=2,height=10,bg='orange',command=equale)
    BtnEqual.place(x=36,y=60)
        
    BtnDot = Button(OperFrame,text=".",width=6,height=2,bg='gray',command=lambda:press('.'))
    BtnDot.place(x=60,y=180)

    window.mainloop()