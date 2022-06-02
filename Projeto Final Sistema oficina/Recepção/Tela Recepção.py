from tkinter import *
from tkinter import messagebox


class Recepcao:
    def __init__(self):
        self.janela = Tk()
        self.janela.title('Recepção')
        self.titleStyles = ('Arial', 14)
        self.textStyles = ('Roboto', 12)
        self.janela.configure(bg='#363636')

        self.section = Frame(self.janela,bg='#363636')
        self.section.pack(padx=100)

        self.titulo = Label(self.section,bg='#363636',fg='white', font=self.titleStyles, text='RECEPÇÃO')
        self.titulo.pack(padx=0, pady=10)

        self.botaoCadastrar = Button(self.section, command=self.cadastrarCliente,
                                     font=self.textStyles,
                                     text='Cadastrar\nCliente',bg='#1E90FF',fg='white',
                                     width=15)
        self.botaoCadastrar.bind("<Enter>", self.passou)
        self.botaoCadastrar.bind("<Leave>", self.saiu)
        self.botaoCadastrar.pack(pady=4)

        self.botaoOrcamento = Button(self.section, command=self.verOrcamento,
                                     font=self.textStyles, bg='#4682B4', fg='white',
                                     text='Ver\nOrçamento',
                                     width=15)
        self.botaoOrcamento.bind("<Enter>", self.passou)
        self.botaoOrcamento.bind("<Leave>", self.saiu)
        self.botaoOrcamento.pack(pady=4)

        self.frameVazio1 = Frame(self.section)
        self.frameVazio1.pack(pady=20)

        self.botaoSair = Button(self.section,bg='#800000',fg='white', command=self.saiu,
                                font=self.textStyles,text='Sair',width=10)
        self.botaoSair.bind("<Enter>", self.passou)
        self.botaoSair.bind("<Leave>", self.saiu)
        self.botaoSair.pack(pady=4)

        self.frameVazio2 = Frame(self.section)
        self.frameVazio2.pack(pady=5)
        
        
        mainloop()

    def cadastrarCliente(self):
        return

    def passou(self, event):
        event.widget.config(relief = RIDGE)

    def saiu(self, event):
        event.widget.config(relief = RAISED)

    def verOrcamento(self):
        return
           
        
        

minhaTela = Recepcao()
