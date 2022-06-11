#componente.bind(evento, função)
from tkinter import *
class Tela:
    def __init__(self):
        self.janela =  Tk()
        self.meuFrame =  Frame(self.janela, width=100, height=100)        
        self.meuFrame.pack()
        self.msg = Label(self.meuFrame, text="primeiro componente")
        self.msg.pack()
        self.botao = Button(self.meuFrame, text="clique aqui",
                            width=10)
        self.botao.bind("<Button-1>", self.tratadorEvento)
        self.botao.pack()
        
        mainloop()

    def tratadorEvento(self, event):
        if self.msg["text"] == "primeiro componente":
            self.msg["text"] = "O botão recebeu um clique"
        else:
            self.msg["text"] = "primeiro componente"

minhaTela = Tela()
