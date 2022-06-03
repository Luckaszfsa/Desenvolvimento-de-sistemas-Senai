from tkinter import *

class Cadastro_Cliente:
    def __init__(self):
        self.janela = Tk()
        #self.janela.geometry("500x500") 
        #self.janela.minsize(200, 150) 
        #self.janela.maxsize(800, 800)
        self.janela.configure(bg="#708090")
             

        self.container1 = Frame(self.janela, pady=10)
        self.container1.grid(column=1, row=0, padx=5, pady=5)
        
        self.titulo = Label(self.container1,text='CADASTRO DE CLIENTE')
        self.titulo.grid(row=0, column=1, padx=5, pady=5, sticky='NWSE')

        self.container2 = Frame(self.janela, pady=10)
        self.container2.grid(column=1, row=0, padx=5, pady=5)

        self.nome = Label(self.janela, text='NOME:')
        self.nome.grid(row=1, column=0, padx=5, pady=5,sticky='NWSE')
        self.nomeEnt = Entry(self.janela, width=50)
        self.nomeEnt.grid(row=1, column=1, padx=5, pady=5,sticky='NWSE')

        self.senhaTxt = Label(self.janela, text='CPF:')
        self.senhaTxt.grid(row=2, column=0, padx=5, pady=5,sticky='NWSE')
        self.senhaEnt = Entry(self.janela, width=30)
        self.senhaEnt.grid(row=2, column=1, padx=5, pady=5,sticky='NWSE')

        self.senhaTxt = Label(self.janela, text='E-MAIL:')
        self.senhaTxt.grid(row=3, column=0, padx=5, pady=5,sticky='NWSE')
        self.senhaEnt = Entry(self.janela, width=30)
        self.senhaEnt.grid(row=3, column=1, padx=5, pady=5,sticky='NWSE')

        self.senhaTxt = Label(self.janela, text='TELEFONE:')
        self.senhaTxt.grid(row=4, column=0, padx=5, pady=5,sticky='NWSE')
        self.senhaEnt = Entry(self.janela, width=30)
        self.senhaEnt.grid(row=4, column=1, padx=5, pady=5,sticky='NWSE')

        self.senhaTxt = Label(self.janela, text='ENDEREÇO:')
        self.senhaTxt.grid(row=5, column=0, padx=5, pady=5,sticky='NWSE')
        self.senhaEnt = Entry(self.janela, width=30)
        self.senhaEnt.grid(row=5, column=1, padx=5, pady=5,sticky='NWSE')

        self.senhaTxt = Label(self.janela, text='CARRO:')
        self.senhaTxt.grid(row=6, column=0, padx=5, pady=5,sticky='NWSE')
        self.senhaEnt = Entry(self.janela, width=30)
        self.senhaEnt.grid(row=6, column=1, padx=5, pady=5,sticky='NWSE')

        self.frameVazio1 = Frame(self.janela, height=10)
        self.frameVazio1.grid()

        self.container3 = Frame(self.janela,bg="#708090", height=200, width = 400, pady=10)
        self.container3.grid(column=1, row=7, padx=5, pady=5)

        self.cadastrar = Button(self.container3,command=self.cadastrar, bg="#00BFFF", text='CADASTRAR')
        self.cadastrar.grid(row=7, column=1, padx=5, pady=5,sticky='NWSE')
        

        self.voltar = Button(self.container3,command=self.voltar, bg="#00BFFF", text='VOLTAR')
        self.voltar.grid(row=7, column=2, padx=5, pady=5,sticky='NWSE')
        
        mainloop()

    def voltar(self):
        return
    def cadastrar(self):
        return

minhaTela = Cadastro_Cliente()
