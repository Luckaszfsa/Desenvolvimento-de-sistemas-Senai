#Crie uma interface com dois campos de entrada e um label.
#Os dois campos receberão dois inteiros, um em cada campo
#O label servirá para aplicar o evento de clique do mouse
#com o intuito de somar os dois inteiros das entradas
#e printar no console o resultado.
from tkinter import *
class Tela:
    def __init__(self):
        self.janela = Tk()
        self.frameCima = Frame(self.janela, height = 75)
        self.frameMeio = Frame(self.janela, height = 75)
        self.frameBaixo = Frame(self.janela, height = 75)
        self.frameCima.pack()
        self.frameMeio.pack()
        self.frameBaixo.pack()
        self.valor1 = Entry(self.frameCima, width=25)
        self.valor1.pack(side = LEFT, padx=10)
        self.valor2 = Entry(self.frameMeio, width=25)
        self.valor2.pack(side = LEFT, padx=10)
        self.evento = Label(self.frameBaixo, text="Clique aqui")
        self.evento.bind("<Button-1>", self.somar)
        self.evento.pack()
        mainloop()

    def somar(self, event):
        inteiro1 = int(self.valor1.get())
        inteiro2 = int(self.valor2.get())
        resultado = inteiro1 + inteiro2
        #self.evento["text"] = resultado
        print(resultado)
        
minhaTela = Tela()
