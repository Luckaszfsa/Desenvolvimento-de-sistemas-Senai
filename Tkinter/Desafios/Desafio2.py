#Reproduza a seguinte interface
from tkinter import *
class Tela:
    def __init__(self):
        self.janela = Tk()

        self.frameCima = Frame(self.janela)
        self.frameMeio = Frame(self.janela)
        self.frameBaixo = Frame(self.janela)

        self.frameCima.pack()
        self.frameMeio.pack()
        self.frameBaixo.pack()

        self.btn1 = Button(self.frameCima,
                           width=3, height=2,
                           text="1") 
        self.btn2 = Button(self.frameMeio,
                           width=3, height=2,
                           text="2")
        self.btn3 = Button(self.frameMeio,
                           width=3, height=2,
                           text="3")
        self.btn4 = Button(self.frameBaixo,
                           width=3, height=2,
                           text="4")
        self.btn5 = Button(self.frameBaixo,
                           width=3, height=2,
                           text="5")
        self.btn6 = Button(self.frameBaixo,
                           width=3, height=2,
                           text="6")

        self.btn1.pack()

        self.btn2.pack(side=LEFT)
        self.btn3.pack(side=LEFT)

        self.btn4.pack(side=LEFT)
        self.btn5.pack(side=LEFT)
        self.btn6.pack(side=LEFT)
        
        mainloop()

minhaTela = Tela()
