import tkinter as tk  # Importar o tkinter e usar esse "as tk", serve para que qdo ele for chamado no codigo poder ser digitado somente com "tk"
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD


class Ordem_de_servico:
    def __init__(self):
        self.janela = Tk()
        self.janela.title('Gerenciar Funcionarios')

        # <<< CONFIGURAÇÕES DA JANELA >>>
        self.janela.configure(bg="#363636")
        self.janela.minsize(810, 330)
        self.janela.maxsize(810, 330)

        # <<< lABEL PARA TENTAR ORGANIZAR >>>
        self.titulo = Label(self.janela, text="Ordem de Serviço",
                            bg="#363636", font=("bold", 15), fg="white")
        self.titulo.grid(row=0, column=0, pady=10)

        self.conteudo = Label(self.janela, bg="#363636")
        self.conteudo.grid(row=1, column=0, padx=2)

        self.botoes = Label(self.janela, bg="#363636")
        self.botoes.grid(row=2)
        self.botoes.columnconfigure([0, 1, 2, 3], minsize=200)

        

        

        # <<< TOPO DAS COLUNAS >>>
        self.colunasTop = ("OS", "MECANICO", "CARRO", "VALOR")
        self.colunasPrincipais = ttk.Treeview(
            self.conteudo, columns=self.colunasTop, show="headings")

        self.colunasPrincipais.heading("OS", text="OS")
        self.colunasPrincipais.heading("MECANICO", text="MECANICO")
        self.colunasPrincipais.heading("CARRO", text="CARRO")
        self.colunasPrincipais.heading("VALOR", text="VALOR")

        self.colunasPrincipais.bind("<<TreeviewSelect>>", self.selecionar)
        self.colunasPrincipais.grid(row=1, column=1)

        # <<< "banco de dados" >>>
        conteudos = []
        conteudos.append(
            ('Creuza Socorro', '12345678901', 'Mecânica', 'MECA123'))
        conteudos.append(('Ordaldo Machado', '12345678901',
                         'Recepcionista', 'RECEP123'))
        conteudos.append(('Vini Color', '12345678901', 'Gerente', 'BOSS123'))
        for conteudo in conteudos:
            self.colunasPrincipais.insert("", tk.END, values=conteudo)

       
        # <<< BOTOES >>>
        self.botaoAdicionar = Button(self.botoes, text="Abrir", width=20, bg="#4682B4", fg="white")
        self.botaoAdicionar.grid(row=2, column=0, pady=10,  ipady=5)

        self.botaoApagar = Button(self.botoes, text="Finalizada", width=20, bg="#006400", fg="white")
        self.botaoApagar.grid(row=2, column=1,pady=10,  ipady=5)

        self.botaoApagar = Button(self.botoes, text="Apagar", width=20, bg="#8B0000", fg="white")
        self.botaoApagar.grid(row=2, column=2,pady=10,  ipady=5)

        self.botaoVoltar = Button(
            self.botoes, text="Voltar", width=20, command=self.janela.destroy)
        self.botaoVoltar.grid(row=2, column=3,pady=10,  ipady=5)

        mainloop()

    # Messagem que aparece quando apertar em algum funcionario
    def selecionar(self, event):
        for itemSelecionado in self.colunasPrincipais.selection():
            item = self.colunasPrincipais.item(itemSelecionado)
            mostrar = item['values']

            messagebox.showinfo(title='Information', message=f'{mostrar}')

    # Abrir Ordem de Serviço
    def abrir(self):
       return
    
    # Finalizar Ordem de Serviço
    def finalizar(self):
       return
    
    # Apagar funcionario
    def apagar():
        return

    # Voltar para tela de gerencia
    def voltar(self):
        return


minhaTela = Ordem_de_servico()
