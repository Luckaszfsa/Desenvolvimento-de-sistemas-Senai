from tkinter import *

class Gerente:
    def __init__(self):
        self.janela = Tk()
        self.titleStyles = ('Arial', 14)
        self.textStyles = ('Roboto', 12)

        self.section = Frame(self.janela)
        self.section.pack(padx=100)

        self.titulo = Label(self.section, font=self.titleStyles, text='GERÊNCIA')
        self.titulo.pack(padx=0, pady=10)

        self.botaoGerenciar = Button(self.section, command=self.gerenciarFuncionarios,
                                     font=self.textStyles,
                                     text='Gerenciar\nFuncionários',
                                     width=15)
        self.botaoGerenciar.pack(pady=4)

        self.botaoOrdem = Button(self.section, command=self.verOrdem,
                                     font=self.textStyles,
                                     text='Ver\nOrdem de Serviço',
                                     width=15)
        self.botaoOrdem.pack(pady=4)

        self.botaoCliente = Button(self.section, command=self.verCliente,
                                     font=self.textStyles,
                                     text='Ver\nCliente',
                                     width=15)
        self.botaoCliente.pack(pady=4)

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

    def gerenciarFuncionarios(self):
        return

    def verOrdem(self):
        return

    def verCliente(self):
        return
        
    
    def sair(self):
        return

minhaTela = Gerente()
