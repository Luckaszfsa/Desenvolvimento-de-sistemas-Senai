import tkinter as tk  # Importar o tkinter e usar esse "as tk", serve para que qdo ele for chamado no codigo poder ser digitado somente com "tk"
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD

class Cadastro_Orcamento:
    def __init__(self):
        self.janela = Tk()
        #self.janela.geometry("500x500") 
        #self.janela.minsize(200, 150) 
        #self.janela.maxsize(800, 800)
        self.janela.configure(bg="#708090")

        #ESTILIZAÇÃO PADRÃO
        
        self.titleStyles = ('Arial', 20)
        self.textStyles = ('Roboto', 12)
        self.textFg = '#666fff'
        self.padronBg = '#363636'
             

        #FRAMES PARA DIVISÃO DE COMPONENTES
        self.container1 = Frame(self.janela, pady=10)
        self.container1.pack()
        
        self.titulo = Label(self.container1,text='CADASTRO DE ORÇAMENTO')
        self.titulo.pack()

        self.container2 = Frame(self.janela, pady=10)
        self.container2.pack()

        self.frameCima = Frame(self.janela, padx=5, pady=5)
        self.frameCima.pack()

        self.frameMeio = Frame(self.janela, padx=5, pady=5)
        self.frameMeio.pack()

        self.frameBaixo = Frame(self.janela, padx=5, pady=5)
        self.frameBaixo.pack()

        # CAMPOS NOME/ CPF/ CARRO / PLACA

        self.nome = Label(self.frameCima, text='NOME:',width=12)
        self.nome.pack(side='left')
        self.nomeEnt = Entry(self.frameCima, width=61)
        self.nomeEnt.pack(side='left')

        self.senhaTxt = Label(self.frameMeio, text='CPF CLIENTE:',width=12)
        self.senhaTxt.pack(side='left')
        self.senhaEnt = Entry(self.frameMeio, width=30)
        self.senhaEnt.pack(side='left')


        self.senhaTxt = Label(self.frameMeio, text='CARRO:', width=8)
        self.senhaTxt.pack(side='left')
        self.senhaEnt = Entry(self.frameMeio, width=20)
        self.senhaEnt.pack(side='left')

        self.senhaTxt = Label(self.frameBaixo, text='CPF MECÂNICO:', width=12)
        self.senhaTxt.pack(side='left')
        self.senhaEnt = Entry(self.frameBaixo, width=30)
        self.senhaEnt.pack(side='left')

        self.senhaTxt = Label(self.frameBaixo, text='PLACA:',width=8)
        self.senhaTxt.pack(side='left')
        self.senhaEnt = Entry(self.frameBaixo, width=20)
        self.senhaEnt.pack(side='left')

        self.container3 = Frame(self.janela, pady=10)
        self.container3.pack()

        self.tabela = Frame(self.janela, pady=10)
        self.tabela.pack()

        # INÍCIO TABELA DE DADOS

        self.titulo2 = Label(self.container3,text='DESCRIÇÃO')
        self.titulo2.pack()

         
         
        self.janela.resizable(width = 1, height = 1) 
        treev = ttk.Treeview(self.tabela, selectmode ='browse') 
        treev.pack(side ='left') 
        verscrlbar = ttk.Scrollbar(self.tabela,  
                                   orient ="vertical",  
                                   command = treev.yview) 
        verscrlbar.pack(side ='left', fill ='both') 
        treev.configure(xscrollcommand = verscrlbar.set) 
        treev["columns"] = ("1", "2") 
        treev['show'] = 'headings'
        treev.column("1", width = 220, anchor ='c') 
        treev.column("2", width = 220, anchor ='c') 
        treev.heading("1", text ="ITENS") 
        treev.heading("2", text ="VALOR") 
        treev.insert("", 'end', text ="L1",  
                     values =("Suspensão", "200.50")) 
        treev.insert("", 'end', text ="L2", 
                     values =("Pneu", "50.00")) 
        treev.insert("", 'end', text ="L3", 
                     values =("Lanterna", "75.00")) 
        treev.insert("", 'end', text ="L4", 
                     values =("Motor", "90.00")) 
        treev.insert("", 'end', text ="L5",  
                     values =("Escapamento", "70.00")) 
        treev.insert("", 'end', text ="L6", 
                     values =("Porta", "80.00")) 
        treev.insert("", 'end', text ="L7",  
                     values =("Suspensão", "89.50")) 
      
         #FIM TABELA DE DADOS
       
        self.frameVazio1 = Frame(self.janela, height=10)
        self.frameVazio1.pack(side='left')

        self.frameVazio2 = Frame(self.janela, height=10, width = 200, pady=10)
        self.frameVazio2.pack(side='right', padx=150)

        #BOTÕES CADASTRAR / VOLTAR

        self.titulo3 = Label(self.frameVazio2,text='R$')
        self.titulo3.pack(side='right', ipadx=20, padx=10)
        self.titulo4 = Label(self.frameVazio2,text='VALOR FINAL')
        self.titulo4.pack(side='right', padx=10)

        self.container4 = Frame(self.janela,bg="#708090", height=200, width = 300, pady=10)
        self.container4.pack(side='left', padx=150)

        self.cadastrar = Button(self.container4,command=self.cadastrar, bg="#00BFFF", text='CADASTRAR')
        self.cadastrar.pack(side='left', ipady=5, padx=5)
        

        self.voltar = Button(self.container4,command=self.voltar, bg="#00BFFF", text='VOLTAR')
        self.voltar.pack(side='left', ipady=5, padx=5)
        

        
        
        
        mainloop()

    def voltar(self):
        return
    def cadastrar(self):
        return

minhaTela = Cadastro_Orcamento()
