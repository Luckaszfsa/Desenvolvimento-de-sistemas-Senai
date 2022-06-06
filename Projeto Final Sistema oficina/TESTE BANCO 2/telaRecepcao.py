from tkinter import *
from tkinter import messagebox


class TelaRecepcao:
    def __init__(self):
        self.janela = Tk()
        self.janela.title('Recepção')
        self.titleStyles = ('Arial', 14)
        self.textStyles = ('Roboto', 12)
        self.janela.configure(bg='#363636')
        self.janela.geometry('1200x600')

        self.hoverColor1 = '#008000'
        self.hoverColor2 = '#1E90FF'
        self.hoverColor3 = '#FF0000'

        self.section = Frame(self.janela,bg='#363636')
        self.section.pack(padx=100)

        self.titulo = Label(self.section,bg='#363636',fg='white', font=self.titleStyles, text='RECEPÇÃO')
        self.titulo.pack(padx=0, pady=10)

        self.botaoCadastrar = Button(self.section, command=self.cadastrarCliente,
                                     font=self.textStyles,
                                     text='Cadastrar\nCliente',bg='#4682B4',fg='white',
                                     width=15)
        self.botaoCadastrar.bind("<Enter>", self.hoverIn1)
        self.botaoCadastrar.bind("<Leave>", self.hoverOut)
        self.botaoCadastrar.pack(pady=4)

        self.botaoOrcamento = Button(self.section, command=self.verOrcamento,
                                     font=self.textStyles, bg='#4682B4', fg='white',
                                     text='Ver\nOrçamento',
                                     width=15)
        self.botaoOrcamento.bind("<Enter>", self.hoverIn2)
        self.botaoOrcamento.bind("<Leave>", self.hoverOut)
        self.botaoOrcamento.pack(pady=4)

        self.frameVazio1 = Frame(self.section)
        self.frameVazio1.pack(pady=20)

        self.botaoSair = Button(self.section,bg='#FF0000',fg='white', command=self.saiu,
                                font=self.textStyles,text='Sair',width=10)
        self.botaoSair.bind("<Enter>", self.hoverIn3)
        self.botaoSair.bind("<Leave>", self.hoverOut2)
        self.botaoSair.pack(pady=4)

        self.frameVazio2 = Frame(self.section)
        self.frameVazio2.pack(pady=5)
        
        
        mainloop()

    def cadastrarCliente(self):
        self.janela.destroy()
        from cadastrarCliente import tela_ver_cadastrar_clientes
        return tela_ver_cadastrar_clientes()
        

    def hoverIn1(self, event):
        event.widget.configure(bg=self.hoverColor1, fg="white",relief=GROOVE)
    def hoverIn2(self, event):
        event.widget.configure(bg=self.hoverColor2, fg="white",relief=GROOVE)
    def hoverIn3(self, event):
        event.widget.configure(bg=self.hoverColor3, fg="white",relief=GROOVE)
    def hoverOut(self, event):
        event.widget.configure(bg='#4682B4',relief=RAISED)
    def hoverOut2(self, event):
        event.widget.configure(relief=RAISED)

    def saiu(self):
        return self.janela.destroy()

    def verOrcamento(self):
        return
           
        
        

minhaTela = TelaRecepcao()
