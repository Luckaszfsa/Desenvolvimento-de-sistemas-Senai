#Crie um programa utilizando Tkinter que, dado um tempo em
#segundos, converta este tempo em horas, minutos e segundos.
from tkinter import *

class Tela:
    def __init__(self):

        self.janela = Tk()

        self.frameCima = Frame(self.janela)
        self.frameCima.pack(padx=30, pady=30)

        self.label = Label(self.frameCima,
                           text = "insira os segundos:")
        self.label.pack(side = LEFT)

        self.entrada = Entry(self.frameCima)
        self.entrada.pack(side = LEFT, padx=20)

        self.frameMeio = Frame(self.janela)
        self.frameMeio.pack()

        self.botao = Button(self.frameMeio, text="Converter",
                            bg="blue", command=self.conversor)
        self.botao.pack()

        self.frameBaixo = Frame(self.janela)
        self.frameBaixo.pack()

        self.saida = Label(self.frameBaixo, font=("Arial", 16))
        self.saida.pack(pady=15)
                
        mainloop()

    def conversor(self):
        segundos = int(self.entrada.get())

        horas = str(segundos//3600)
        # // retorna o resultado de uma divisão como inteiro
        #Exemplo: 7600//3600 = 2

        minutos = str((segundos%3600)//60)
        # % retorna o resto de uma divisão com resultado inteiro
        #Exemplo: 7600%3600 = 400, 400//60 = 6
        #Logo: (7600%3600)//60 = 6

        segundos = str((segundos%3600)%60)
        #Exemplo: 7600%3600 = 400, 400%60 = 40
        #Logo: (7600%3600)%60 = 40

        conversao = f"{horas} Horas {minutos} Minutos {segundos} Segundos"

        self.saida["text"] = conversao
        
minhaTela = Tela()
