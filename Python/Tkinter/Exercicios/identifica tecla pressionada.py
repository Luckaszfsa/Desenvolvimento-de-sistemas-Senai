from tkinter import *

class Tela:
    def __init__(self):
        self.janela = Tk()
        self.frame = Frame(self.janela)
        self.frame.pack(fill=BOTH, expand=YES)
        self.janela.geometry("250x50")
        self.janela.title("Eventos de teclado")

        self.mensagem = StringVar()
        self.label = Label(self.frame,
                           textvariable = self.mensagem)
        self.mensagem.set("Aperte uma tecla")
        self.label.pack()

        self.janela.bind("<KeyPress>", self.teclaPressionada)
        self.janela.bind("<KeyRelease>", self.teclaLiberada)
        self.janela.bind("<KeyPress-Alt_L>", self.altPressionado)
        self.janela.bind("<KeyRelease-Alt_L>", self.altLiberado)

        mainloop()

    def teclaPressionada(self, event):
        self.mensagem.set("Tecla pressionada: " + event.char)

    def teclaLiberada(self, event):
        self.mensagem.set("Tecla solta: " + event.char)
        
    def altPressionado(self, event):
        self.mensagem.set("Alt pressionado")

    def altLiberado(self, event):
        self.mensagem.set("Alt liberado")

minhaTela = Tela()
