#Crie, usando o componente Label e o
#método pack a seguinte interface
from tkinter import *
class Tela:
    def __init__(self):
        self.janela = Tk()

        self.fontePadrao = ("Arial","10")

        self.label1 = Label(self.janela,
                            text="label 1",
                            font=self.fontePadrao)
        self.label1.pack()
        self.label2 = Label(self.janela,
                            text="label 2",
                            font=self.fontePadrao)
        self.label2.pack(side = BOTTOM)
        self.label3 = Label(self.janela,
                            text="label 3",
                            font=self.fontePadrao)
        self.label3.pack(side = LEFT)
        self.label4 = Label(self.janela,
                            text="label 4",
                            font=self.fontePadrao)
        self.label4.pack(side = RIGHT)
        mainloop()

minhaTela = Tela()
        
