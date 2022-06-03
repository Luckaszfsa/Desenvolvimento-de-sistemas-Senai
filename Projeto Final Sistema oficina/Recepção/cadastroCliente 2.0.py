from cgitb import text
from tkinter import *
from tkinter import messagebox




class Cadastro_Cliente:

    def __init__(self):

        self.janela = Tk()

        #self.janela.geometry("500x500") 

        #self.janela.minsize(200, 150) 

        #self.janela.maxsize(800, 800)

        self.janela.configure(bg="#363636")
        self.janela.title('Cadastro de clientes') 


#================== VARIÁVEIS DE ESTILIZAÇÃO ===================
        self.hoverColor1 = '#008000'
        self.hoverColor2 = '#8B0000'
        self.hoverColor3 = '#191970'




        self.container1 = Frame(self.janela, pady=10,bg="#363636")

        self.container1.grid(column=1, row=0, padx=5, pady=5)

        

        self.titulo = Label(self.container1,text='CADASTRO DE CLIENTE',bg="#363636",fg="white")

        self.titulo.grid(row=0, column=1, padx=5, pady=5, sticky='NWSE')




        self.container2 = Frame(self.janela, pady=10)

        self.container2.grid(column=1, row=0, padx=5, pady=5)




        self.nome = Label(self.janela, text='NOME:',bg="#4682B4", fg="white")

        self.nome.grid(row=1, column=0, padx=5, pady=5,sticky='NWSE')

        self.nomeEnt = Entry(self.janela, width=50, text='Crodosvaldo')

        self.nomeEnt.grid(row=1, column=1, padx=5, pady=5,sticky='NWSE')




        self.cpfTxt = Label(self.janela, text='CPF:',bg="#4682B4", fg="white")

        self.cpfTxt.grid(row=2, column=0, padx=5, pady=5,sticky='NWSE')

        self.cpfEnt = Entry(self.janela, width=30)

        self.cpfEnt.grid(row=2, column=1, padx=5, pady=5,sticky='NWSE')




        self.emailTxt = Label(self.janela, text='E-MAIL:',bg="#4682B4", fg="white")

        self.emailTxt.grid(row=3, column=0, padx=5, pady=5,sticky='NWSE')

        self.emailEnt = Entry(self.janela, width=30)

        self.emailEnt.grid(row=3, column=1, padx=5, pady=5,sticky='NWSE')




        self.telTxt = Label(self.janela, text='TELEFONE:',bg="#4682B4", fg="white")

        self.telTxt.grid(row=4, column=0, padx=5, pady=5,sticky='NWSE')

        self.telEnt = Entry(self.janela, width=30)

        self.telEnt.grid(row=4, column=1, padx=5, pady=5,sticky='NWSE')




        self.enderecoTxt = Label(self.janela, text='ENDEREÇO:',bg="#4682B4", fg="white")

        self.enderecoTxt.grid(row=5, column=0, padx=5, pady=5,sticky='NWSE')

        self.enderecoEnt = Entry(self.janela, width=30)

        self.enderecoEnt.grid(row=5, column=1, padx=5, pady=5,sticky='NWSE')




        self.carroTxt = Label(self.janela, text='CARRO:',bg="#4682B4", fg="white")

        self.carroTxt.grid(row=6, column=0, padx=5, pady=5,sticky='NWSE')

        self.carroEnt = Entry(self.janela, width=30)

        self.carroEnt.grid(row=6, column=1, padx=5, pady=5,sticky='NWSE')




        self.container3 = Frame(self.janela,bg="#363636", height=200, width = 400, pady=10)

        self.container3.grid(column=1, row=7, padx=5, pady=5)




        self.cadastrar = Button(self.container3,command=self.cadastrar, bg="#00BFFF", text='CADASTRAR', relief=RAISED)

        self.cadastrar.grid(row=7, column=1, padx=5, pady=5,sticky='NWSE')
        self.cadastrar.bind('<Enter>', self.hoverIn1)
        self.cadastrar.bind('<Leave>', self.hoverOut)

        




        self.voltar = Button(self.container3,command=self.voltar, bg="#00BFFF", text='VOLTAR')

        self.voltar.grid(row=7, column=2, padx=5, pady=5,sticky='NWSE')
        self.voltar.bind('<Enter>', self.hoverIn2)
        self.voltar.bind('<Leave>', self.hoverOut)

        self.limparCampos = Button(self.container3,command=self.limpaCampos, bg="#00BFFF", text='LIMPAR CAMPOS')

        self.limparCampos.grid(row=7, column=0, padx=5, pady=5,sticky='NWSE')

        self.limparCampos.bind("<1>", self.limpaCampos)
        self.limparCampos.bind('<Enter>', self.hoverIn3)
        self.limparCampos.bind('<Leave>', self.hoverOut)
        

        mainloop()


    def hoverIn1(self, event):
        event.widget.configure(bg=self.hoverColor1, fg="white",relief=GROOVE)
    def hoverIn2(self, event):
        event.widget.configure(bg=self.hoverColor2, fg="white",relief=GROOVE)
    def hoverIn3(self, event):
        event.widget.configure(bg=self.hoverColor3, fg="white",relief=GROOVE)
    def hoverOut(self, event):
        event.widget.configure(bg='#1E90FF',relief=RAISED)

    def voltar(self):
        return

    def limpaCampos(self):
        self.nomeEnt.delete(0, END)
        self.enderecoEnt.delete(0, END)
        self.emailEnt.delete(0, END)
        self.telEnt.delete(0, END)
        self.carroEnt.delete(0, END)
        self.cpfEnt.delete(0, END)
        return messagebox.showinfo('INFORMATIVO','Todos os campos foram limpos!')#primeiro texto é título, segundo texto é conteúdo

    def cadastrar(self):
        nome = self.nomeEnt.get()
        cpf = self.cpfEnt.get()
        email = self.emailEnt.get()
        telefone = self.telEnt.get()
        carro = self.carroEnt.get()
        endereco = self.enderecoEnt.get()
        messagebox.showinfo('INFORMATIVO', f'CLIENTE CADASTRADO COM SUCESSO!\n\nNOME:{nome}\nCPF:{cpf}\nE-MAIL:{email}\nTELEFONE:{telefone}\nCARRO:{carro}\nENDEREÇO:{endereco}')
        return self.limpaCampos()



minhaTela = Cadastro_Cliente()
