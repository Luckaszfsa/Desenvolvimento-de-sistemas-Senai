from tkinter import *

class Recepcao:
    def __init__(self):
        self.janela = Tk()
        self.titleStyles = ('Arial', 14)
        self.textStyles = ('Roboto', 12)

        self.section = Frame(self.janela)
        self.section.pack(padx=100)

        self.titulo = Label(self.section, font=self.titleStyles, text='RECEPÇÃO')
        self.titulo.pack(padx=0, pady=10)

        self.botaoCadastrar = Button(self.section, command=self.cadastrarCliente,
                                     font=self.textStyles,
                                     text='Cadastrar\nCliente',
                                     width=15)
        self.botaoCadastrar.pack(pady=4)

        self.botaoOrcamento = Button(self.section, command=self.verOrcamento,
                                     font=self.textStyles,
                                     text='Ver\nOrçamento',
                                     width=15)
        self.botaoOrcamento.pack(pady=4)

        self.frameVazio1 = Frame(self.section)
        self.frameVazio1.pack(pady=20)

        self.botaoSair = Button(self.section, command=self.sair,
                                font=self.textStyles,
                                text='Sair',
                                width=15)
        self.botaoSair.pack(pady=4)

        self.frameVazio2 = Frame(self.section)
        self.frameVazio2.pack(pady=5)
        
        
        mainloop()

    def cadastrarCliente(self):
        return

    def verOrcamento(self):
        return
    

    def sair(self):
        return

minhaTela = Recepcao()
