from tkinter import *
from tkinter import messagebox

class Tela():
    def __init__(self):
        self.janela = Tk()
        self.frame = Frame()
        self.frame.pack(fill=BOTH, expand=YES)
        self.janela.geometry("300x200")

        self.mousePosicao = StringVar()
        self.mousePosicao.set("Mouse fora da janela")

        self.label = Label(self.frame,
                           textvariable = self.mousePosicao)
        self.label.pack(side=BOTTOM)

        self.frame.bind("<Button-1>", self.botaoPressionado)
        self.frame.bind("<ButtonRelease-1>", self.botaoLiberado)
        self.frame.bind("<B1-Motion>", self.mouseArrastado)
        self.frame.bind("<Enter>", self.entrouJanela)
        mainloop()

    def botaoPressionado(self, event):
        self.mousePosicao.set("Pressionado em ["+str(event.x) + ", " + str(event.y) + "]")

    def botaoLiberado(self, event):
        self.mousePosicao.set("Solto em ["+str(event.x) + ", " + str(event.y) + "]")

    def mouseArrastado(self, event):
        self.mousePosicao.set("Arrastado até ["+str(event.x) + ", " + str(event.y) + "]")

    def entrouJanela(self, event):
        self.mousePosicao.set("Entrou na janela")
minhaTela = Tela()
