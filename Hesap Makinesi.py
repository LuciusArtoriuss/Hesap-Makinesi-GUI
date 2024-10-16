import tkinter as tk
from tkinter import *
from PIL.ImageOps import expand

pencere = Tk()
pencere.title("Hesap Makinesi")
pencere.geometry("570x600+100+200")
pencere.configure(bg="#17161b")
pencere.resizable(False,False)

denklem = ""

def show(value):
    global denklem
    denklem+=value
    denklem_sonuc.config(text=denklem)

def clear():
    global denklem
    denklem = ""
    denklem_sonuc.config(text=denklem)

def hesapla():
    global denklem
    sonuc = ""
    if denklem != "":
        try:
            sonuc = eval(denklem)
        except:
            sonuc = "ERROR"
            denklem = ""
    denklem_sonuc.config(text=sonuc)

def backspace():
    global denklem
    denklem = denklem[:-1]
    denklem_sonuc.config(text=denklem)

denklem_sonuc = Label(pencere,height=2, width=25, text="", font=("arial",30), fg="#fff", bg="#17161b")
denklem_sonuc.pack()

Button(pencere,text="C", width= 5, height= 1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#20b2aa", command=lambda: clear()).place(x=10, y=100)
Button(pencere,text="/", width= 5, height= 1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#1f2128", command=lambda: show("/")).place(x=430, y=100)
Button(pencere,text="⌫", width= 11, height= 1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#1f2128", command=lambda: backspace()).place(x=150, y=100)
Button(pencere,text="×", width= 5, height= 1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#1f2128", command=lambda: show("*")).place(x=430, y=200)

Button(pencere,text="7", width= 5, height= 1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("7")).place(x=10, y=200)
Button(pencere,text="8", width= 5, height= 1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("8")).place(x=150, y=200)
Button(pencere,text="9", width= 5, height= 1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("9")).place(x=290, y=200)
Button(pencere,text="-", width= 5, height= 1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#1f2128", command=lambda: show("-")).place(x=430, y=300)

Button(pencere,text="4", width= 5, height= 1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("4")).place(x=10, y=300)
Button(pencere,text="5", width= 5, height= 1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("5")).place(x=150, y=300)
Button(pencere,text="6", width= 5, height= 1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("6")).place(x=290, y=300)
Button(pencere,text="+", width= 5, height= 1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#1f2128", command=lambda: show("+")).place(x=430, y=400)

Button(pencere,text="1", width= 5, height= 1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("1")).place(x=10, y=400)
Button(pencere,text="2", width= 5, height= 1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("2")).place(x=150, y=400)
Button(pencere,text="3", width= 5, height= 1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("3")).place(x=290, y=400)
Button(pencere,text="0", width= 11, height= 1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("0")).place(x=10, y=500)

Button(pencere,text=".", width= 5, height= 1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show(".")).place(x=290, y=500)
Button(pencere,text="=", width= 5, height= 1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#20b2aa", command=lambda: hesapla()).place(x=430, y=500)


pencere.mainloop()
