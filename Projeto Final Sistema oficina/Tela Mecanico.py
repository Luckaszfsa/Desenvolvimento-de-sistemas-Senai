from tkinter import *

class Mecanico:
    def __init__(self):
        self.janela = Tk()
        self.titleStyles = ('Arial', 14)
        self.textStyles = ('Roboto', 12)

        self.section = Frame(self.janela)
        self.section.pack(padx=100)

        self.titulo = Label(self.section, font=self.titleStyles, text='OFICINA')
        self.titulo.pack(padx=0, pady=10)

        self.botaoCadastrar = Button(self.section, command=self.cadastrarOrcamento,
                                     font=self.textStyles,
                                     text='Cadastrar\nOrçamento',
                                     width=15)
        self.botaoCadastrar.pack(pady=4)

        self.botaoOrdem = Button(self.section, command=self.verOrdem,
                                     font=self.textStyles,
                                     text='Ver\nOrdem de Serviço',
                                     width=15)
        self.botaoOrdem.pack(pady=4)

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

    def cadastrarOrcamento(self):
        return

    def verOrdem(self):
        return
    
    
    def sair(self):
        return

minhaTela = Mecanico()
