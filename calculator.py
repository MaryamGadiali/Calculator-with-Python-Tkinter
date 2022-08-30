#input boxes
from tkinter import *
root=Tk()
root.title("Simple calculator")
e= Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def buttonClick(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def buttonClear():
    e.delete(0,END)

def buttonAdd():
    firstNumber=e.get()
    global fNum
    global math
    math='addition'
    fNum=int(firstNumber)
    e.delete(0,END)

def buttonEqual():
    secondNumber=e.get()
    e.delete(0,END)
    if math=='addition':
        e.insert(0,fNum+int(secondNumber))
    if math=='subtraction':
        e.insert(0,fNum-int(secondNumber))
    if math=='multiplication':
        e.insert(0,fNum*int(secondNumber))
    if math=='division':
        e.insert(0,fNum/int(secondNumber))    

def buttonSubtract():
    firstNumber=e.get()
    global fNum
    global math
    math='subtraction'
    fNum=int(firstNumber)
    e.delete(0,END)
    
def buttonMultiply():
    firstNumber=e.get()
    global fNum
    global math
    math='multiplication'
    fNum=int(firstNumber)
    e.delete(0,END)

def buttonDivide():
    firstNumber=e.get()
    global fNum
    global math
    math='division'
    fNum=int(firstNumber)
    e.delete(0,END)



    
#define buttons
button1=Button(root, text="1", padx=40, pady=20, command=lambda: buttonClick(1))
button2=Button(root, text="2", padx=40, pady=20, command=lambda: buttonClick(2))
button3=Button(root, text="3", padx=40, pady=20, command=lambda: buttonClick(3))
button4=Button(root, text="4", padx=40, pady=20, command=lambda: buttonClick(4))
button5=Button(root, text="5", padx=40, pady=20, command=lambda: buttonClick(5))
button6=Button(root, text="6", padx=40, pady=20, command=lambda: buttonClick(6))
button7=Button(root, text="7", padx=40, pady=20, command=lambda: buttonClick(7))
button8=Button(root, text="8", padx=40, pady=20, command=lambda: buttonClick(8))
button9=Button(root, text="9", padx=40, pady=20, command=lambda: buttonClick(9))
button0=Button(root, text="0", padx=40, pady=20, command=lambda: buttonClick(0))
buttonAdd=Button(root, text="+", padx=39, pady=20, command=buttonAdd)
buttonEqual=Button(root, text="=", padx=91, pady=20, command=buttonEqual)
buttonClear=Button(root, text="Clear", padx=79, pady=20, command=buttonClear)

buttonSubtract=Button(root, text="-", padx=40, pady=20, command=buttonSubtract)
buttonMultiply=Button(root, text="*", padx=40, pady=20, command=buttonMultiply)
buttonDivide=Button(root, text="/", padx=40, pady=20, command=buttonDivide)

#Put the buttons on the screen
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button0.grid(row=4, column=0)
buttonAdd.grid(row=5, column=0)
buttonClear.grid(row=4, column=1, columnspan=2)
buttonEqual.grid(row=5, column=1, columnspan=2)

buttonSubtract.grid(row=6, column=0)
buttonMultiply.grid(row=6, column=1)
buttonDivide.grid(row=6, column=2)



root.mainloop()
