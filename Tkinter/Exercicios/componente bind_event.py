#componente.bind(evento, função)
from tkinter import *
class Tela:
    def __init__(self):
        self.janela =  Tk()
        self.meuFrame =  Frame(self.janela, width=100, height=100)
        self.meuFrame.bind("<Button-1>", self.tratadorEvento)
        self.meuFrame.pack()
        
        mainloop()

    def tratadorEvento(self, event):
        print("Você clicou na posição:", event.x, event.y)

minhaTela = Tela()
