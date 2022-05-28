from tkinter import *
from turtle import back

raiz=Tk() 
raiz.resizable(width=False,height=False)
raiz.geometry("350x200")
raiz.title("Calculadora Python")
raiz.iconbitmap('calculator.ico')
miFrame=Frame(raiz)

 
miFrame.pack()

operacion=""

#------------Pantalla---------------#
numeroPantalla=StringVar()

pantalla=Entry(miFrame,width=40,textvariable=numeroPantalla)
pantalla.grid(row=1,column=1,padx=10,pady=10,columnspan="4")
pantalla.config(background="black",fg="#03f943",justify="right")

#-----------Funciones-----------------#
def numeroPulsado(num):
    numeroPantalla.set(numeroPantalla.get() + num)
#-----------Funcion Suma-----------------#
def suma():
    global operacion

    operacion="suma"

#------------Fila 1-------------------#
bnt7=Button(miFrame,text="7",width=10, command=lambda:numeroPulsado("7"))
bnt7.grid(row=2,column=1,padx=3,pady=3)

bnt8=Button(miFrame,text="8",width=10, command=lambda:numeroPulsado("8"))
bnt8.grid(row=2,column=2,padx=3,pady=3)

bnt9=Button(miFrame,text="9",width=10, command=lambda:numeroPulsado("9"))
bnt9.grid(row=2,column=3,padx=3,pady=3)

bntDiv=Button(miFrame,text="/",width=10)
bntDiv.grid(row=2,column=4,padx=3,pady=3)

#------------Fila 2-------------------#
bnt4=Button(miFrame,text="4",width=10, command=lambda:numeroPulsado("4"))
bnt4.grid(row=3,column=1,padx=3,pady=3)

bnt5=Button(miFrame,text="5",width=10, command=lambda:numeroPulsado("5"))
bnt5.grid(row=3,column=2,padx=3,pady=3)

bnt6=Button(miFrame,text="6",width=10, command=lambda:numeroPulsado("6"))
bnt6.grid(row=3,column=3,padx=3,pady=3)

bntMult=Button(miFrame,text="X",width=10)
bntMult.grid(row=3,column=4,padx=3,pady=3)

#------------Fila 3-------------------#
bnt1=Button(miFrame,text="1",width=10, command=lambda:numeroPulsado("1"))
bnt1.grid(row=4,column=1,padx=3,pady=3)

bnt2=Button(miFrame,text="2",width=10, command=lambda:numeroPulsado("2"))
bnt2.grid(row=4,column=2,padx=3,pady=3)

bnt3=Button(miFrame,text="3",width=10, command=lambda:numeroPulsado("3"))
bnt3.grid(row=4,column=3,padx=3,pady=3)

bntRest=Button(miFrame,text="-",width=10)
bntRest.grid(row=4,column=4,padx=3,pady=3)

#------------Fila 4-------------------#
bnt0=Button(miFrame,text="0",width=10,command=lambda:numeroPulsado("0"))
bnt0.grid(row=5,column=1,padx=3,pady=3)

bntComa=Button(miFrame,text=",",width=10)
bntComa.grid(row=5,column=2,padx=3,pady=3)

bnt3=Button(miFrame,text="x²",width=10)
bnt3.grid(row=5,column=3,padx=3,pady=3)

bntSuma=Button(miFrame,text="+",width=10,command=lambda:suma())
bntSuma.grid(row=5,column=4,padx=3,pady=3)

#------------Fila 5-------------------#
bntIgual=Button(miFrame,text="=",width=9)
bntIgual.grid(row=6,column=1,padx=10,pady=10,columnspan="4")


raiz.mainloop()