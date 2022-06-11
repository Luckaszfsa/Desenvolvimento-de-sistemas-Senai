from tkinter import *
from tkinter import messagebox

class Tela:
    def __init__(self):
        self.janela = Tk()

        self.frameCima = Frame(self.janela)
        self.frameCima.pack()
        self.frameBaixo = Frame(self.janela)
        self.frameBaixo.pack()

        self.radio_valor = IntVar()
        self.radio_valor.set(1)

        self.label = Label(self.frameCima,
        text="Qual sua linguagem de programação preferida?")

        self.python = Radiobutton(self.frameCima,
                                  text="Python",
                                  variable = self.radio_valor,
                                  value = 1)
        self.java = Radiobutton(self.frameCima,
                                  text="Java",
                                  variable = self.radio_valor,
                                  value = 2)
        self.c = Radiobutton(self.frameCima,
                                  text="C",
                                  variable = self.radio_valor,
                                  value = 3)
        self.label.pack(anchor = "w")
        self.python.pack(anchor = "w")
        self.java.pack(anchor = "w")
        self.c.pack(anchor = "w")

        self.botao = Button(self.frameBaixo,
                            text="Exibir escolha",
                            command=self.exibe)
        self.sair = Button(self.frameBaixo,
                           text="Sair",
                           command=self.janela.destroy)
        self.botao.pack(side=LEFT)
        self.sair.pack(side=LEFT)

        mainloop()

    def exibe(self):
        nome = str(self.radio_valor.get())
        messagebox.showinfo("Resposta", "Você escolheu a opção " + nome)

minhaTela = Tela()












        
        
