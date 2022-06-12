from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import BOLD
from turtle import width
from orcamentos import Orcamentos


class CadastrarOrcamento():
    def __init__(self):

        self.janela = Tk()

        self.janela.title('Automativo Soluções')
        self.janela.geometry('1200x600')
        self.janela.config(bg="#484848")
        self.janela.state("zoomed")

# ============= SEÇÕES ================ #

        self.container1 = LabelFrame(self.janela, bg="#484848", fg="#e1e3db")

        self.wrapper1 = LabelFrame(
            self.container1, text='Clientes Cadastrados', font=("Roboto", 18, 'bold'), bg="#484848", fg="#e1e3db")
        self.wrapper2 = LabelFrame(
            self.janela, text='Procurar Cliente', font=("Roboto", 18, 'bold'), bg="#484848", fg="#e1e3db")
        self.wrapper3 = LabelFrame(
            self.container1, text='Dados do Cliente', font=("Roboto", 18, 'bold'), bg="#484848", fg="#e1e3db")
        self.rodape = Frame(self.janela, bg='#484848')

        self.container1.pack(fill='both', expand='no', padx=30, pady=10)
        self.wrapper1.pack(fill='both', expand='yes',
                           padx=25, pady=10, ipady=30, side="left")
        self.wrapper2.pack(fill='none', expand='no',
                           padx=10, pady=10)
        self.wrapper3.pack(fill='x', expand='no', ipadx=30,
                           padx=30, ipady=75, side="right")
        self.rodape.pack(fill='both', expand='yes', padx=20)

# ========= SEÇÃO DADOS DO CLIENTE ======= #
# ---------- LABELS & ENTRYS ----------- #
        self.labelCliente = Label(
            self.wrapper1, text='Nome Cliente', font=(
            "Roboto", 16), bg='#484848', fg='#e1e3db')
        self.labelCliente.grid(row=0, column=0, padx=5, pady=3)
        self.caixaCliente = Entry(self.wrapper1)
        self.caixaCliente.grid(row=0, column=1, padx=5, pady=3)

        self.labelCpfCliente = Label(
            self.wrapper1, text='CPF Cliente', font=(
            "Roboto", 16), bg='#484848', fg='#e1e3db')
        self.labelCpfCliente.grid(row=1, column=0, padx=5, pady=3)
        self.caixaCpfCliente = Entry(self.wrapper1)
        self.caixaCpfCliente.grid(row=1, column=1, padx=5, pady=3)

        self.labelMecanico = Label(
            self.wrapper1, text='Nome Mecânico', font=(
            "Roboto", 16), bg='#484848', fg='#e1e3db')
        self.labelMecanico.grid(row=2, column=0, padx=5, pady=3)
        self.caixaMecanico = Entry(self.wrapper1)
        self.caixaMecanico.grid(row=2, column=1, padx=5, pady=3)

        self.labelCpfMecanico = Label(
            self.wrapper1, text='CPF Mecânico', font=(
            "Roboto", 16), bg='#484848', fg='#e1e3db')
        self.labelCpfMecanico.grid(row=3, column=0, padx=5, pady=3)
        self.caixaCpfMecanico = Entry(self.wrapper1)
        self.caixaCpfMecanico.grid(row=3, column=1, padx=5, pady=3)

        self.labelPlaca = Label(
            self.wrapper1, text='Carro/Placa', font=(
            "Roboto", 16), bg='#484848', fg='#e1e3db')
        self.labelPlaca.grid(row=0, column=2, padx=5, pady=3)
        self.caixaPlaca = Entry(self.wrapper1)
        self.caixaPlaca.grid(row=0, column=3, padx=5, pady=3, ipadx=40)

        self.labelItens = Label(
            self.wrapper1, text='Serviços', font=(
            "Roboto", 16), bg='#484848', fg='#e1e3db')
        self.labelItens .grid(row=1, column=2, padx=5, pady=3)
        self.caixaItens = Entry(self.wrapper1)
        self.caixaItens.grid(row=1, column=3, padx=5, pady=3, ipadx=40)

        self.labelValor = Label(
            self.wrapper1, text='Valor', font=(
            "Roboto", 16), bg='#484848', fg='#e1e3db')
        self.labelValor.grid(row=2, column=2, padx=5, pady=3)
        self.caixaValor = Entry(self.wrapper1)
        self.caixaValor.grid(row=2, column=3, padx=5, pady=3, ipadx=40)

        self.labelId = Label(
            self.wrapper1, text='ID Orçamento', font=(
            "Roboto", 16), bg='#484848', fg='#e1e3db')
        self.labelId.grid(row=3, column=2, padx=5, pady=3)
        self.caixaId = Entry(self.wrapper1)
        self.caixaId.grid(row=3, column=3, padx=5, pady=3, sticky='W')

# ------------ BOTÕES -------------- #
        self.addBtn = Button(self.wrapper1, text='Adicionar', font=("Roboto", 16),
                             command=self.inserir_orcamento, bg='#566981', fg='#e1e3db', relief=RAISED)
        self.addBtn.bind("<Enter>", self.hoverIn1)
        self.addBtn.bind("<Leave>", self.hoverOut)

        self.alterarBtn = Button(
            self.wrapper1, text='Alterar', font=("Roboto", 16), command=self.alterar_orcamento, bg='#566981', fg='#e1e3db', relief=RAISED)
        self.alterarBtn.bind("<Enter>", self.hoverIn1)
        self.alterarBtn.bind("<Leave>", self.hoverOut)

        self.excluirBtn = Button(
            self.wrapper1, text='Excluir', font=("Roboto", 16), command=self.excluir_orcamento, bg='#566981', fg='#e1e3db', relief=RAISED)
        self.excluirBtn.bind("<Enter>", self.hoverIn3)
        self.excluirBtn.bind("<Leave>", self.hoverOut)

        self.addBtn.grid(row=4, column=0, padx=5, pady=10, ipadx=25)
        self.alterarBtn.grid(row=4, column=1, padx=5, pady=3, ipadx=20)
        self.excluirBtn.grid(row=4, column=2, padx=5, pady=3, ipadx=25)


# ============ SEÇÃO CLIENTES CADASTRADOS =============== #
# ------------------- TREEVIEW ------------------ #
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("mystyle.Treeview", font=("Roboto", 14))
        style.configure("mystyle.Treeview.Heading", font=("Roboto", 16))
        style.configure("Treeview", background="silver", rowheight=25, fieldbackground="#E0FFFF",)
        style.configure("Heading", background="#4682B4", foreground = "white")

        self.cabecalho = ('#', 'nome_cliente', 'cpf_cliente', 'nome_mecanico',
                          'cpf_mecanico', 'carro_placa', 'itens', 'valor')

        self.trv = ttk.Treeview(
            self.wrapper2, style="mystyle.Treeview", selectmode='browse', columns=self.cabecalho, show='headings')

        self.trv.column('#', width=30)
        self.trv.column('nome_cliente', width=350, anchor='center')
        self.trv.column('cpf_cliente', width=180)
        self.trv.column('nome_mecanico', width=350)
        self.trv.column('cpf_mecanico', width=180)
        self.trv.column('carro_placa', width=180)
        self.trv.column('itens', width=200)
        self.trv.column('valor', width=180)

        self.trv.heading('#', text='#')
        self.trv.heading('nome_cliente', text='Nome')
        self.trv.heading('cpf_cliente', text='CPF Cliente')
        self.trv.heading('nome_mecanico', text='Nome Mecânico')
        self.trv.heading('cpf_mecanico', text='CPF Mecânico')
        self.trv.heading('carro_placa', text='Carro/Placa')
        self.trv.heading('itens', text='Serviço')
        self.trv.heading('valor', text='Valor')

        self.trv.bind('<Double 1>', self.pegar_linha)
        self.trv.pack()

        self.popular()

# ============= SEÇÃO PROCURAR =========== #
# ---------- LABELS & ENTRYS ----------- #
        self.labelChave = Label(self.wrapper3, font=(
            "Roboto", 14), text='Palavra-Chave', bg="#566981", fg="#e1e3db", relief=RAISED)
        self.labelChave.pack(side='left', padx=10, pady=10, ipadx=50)

        self.busca = Entry(self.wrapper3)
        self.busca.pack(side='left', padx=6, pady=10, ipadx=80, ipady=2)


# ------------- BOTÃO ------------- #
        self.procurarBtn = Button(
            self.wrapper3, text='Procurar', font=("Roboto", 14), command=self.procurar, bg="#566981", fg="#e1e3db", relief=RAISED)
        self.procurarBtn.pack(side='left', padx=20, pady=10, ipadx=10)
        self.procurarBtn.bind("<Enter>", self.hoverIn2)
        self.procurarBtn.bind("<Leave>", self.hoverOut)

        self.limparBtn = Button(self.wrapper3, text='Limpar', font=("Roboto", 14), command=self.limpar, bg="#566981", fg="#e1e3db", relief=RAISED)
        self.limparBtn.pack(side='left', padx=6, pady=10, ipadx=10)
        self.limparBtn .bind("<Enter>", self.hoverIn4)
        self.limparBtn .bind("<Leave>", self.hoverOut)

        self.mostrarBtn = Button(
            self.wrapper2, padx=30, text='Mostrar Todos', font=("Roboto", 16), command=self.popular, bg="#566981", fg="#e1e3db", relief=RAISED)
        self.mostrarBtn.pack(side='right', padx=750, pady=10)
        self.mostrarBtn.bind("<Enter>", self.hoverIn2)
        self.mostrarBtn.bind("<Leave>", self.hoverOut)


# ========= SEÇÃO RODAPÉ ======= #
# ---------- BOTÃO ----------- #
        self.voltarBtn = Button(
            self.rodape, text='Voltar', font=("Roboto", 12), width='15', command=self.voltar_tela, bg="#800000", fg="#e1e3db", relief=RAISED)
        self.voltarBtn.pack(side='right', padx=2, ipadx=2)

        mainloop()

# ============= FUNÇÕES ============== #
    def pegar_linha(self, identificador):
        customer = Orcamentos()
        self.limpar_caixas()
        for item in self.trv.selection():
            self.id = self.trv.item(item, 'values')
        identificador = self.id[0]

        customer.identificar_linha(identificador)
        self.caixaId.insert(INSERT, customer.idorcamento)
        self.caixaCliente.insert(INSERT, customer.nome_cliente)
        self.caixaCpfCliente.insert(INSERT, customer.cpf_cliente)
        self.caixaMecanico.insert(INSERT, customer.nome_mecanico)
        self.caixaCpfMecanico.insert(INSERT, customer.cpf_mecanico)
        self.caixaPlaca.insert(INSERT, customer.carro_placa)
        self.caixaItens.insert(INSERT, customer.itens)
        self.caixaValor.insert(INSERT, customer.valor)

    def limpar_caixas(self):
        self.normal()
        self.caixaCliente.delete(0, END)
        self.caixaCpfCliente.delete(0, END)
        self.caixaMecanico.delete(0, END)
        self.caixaCpfMecanico.delete(0, END)
        self.caixaPlaca.delete(0, END)
        self.caixaItens.delete(0, END)
        self.caixaValor.delete(0, END)

    def procurar(self):
        self.trv.delete(*self.trv.get_children())
        staff = Orcamentos()
        nome = self.busca.get()
        for i in staff.filtrar_func(nome):
            self.trv.insert('', 'end', values=i)

    def limpar(self):
        self.normal()
        self.busca.delete(0, END)
        self.caixaCliente.delete(0, END)
        self.caixaCpfCliente.delete(0, END)
        self.caixaMecanico.delete(0, END)
        self.caixaCpfMecanico.delete(0, END)
        self.caixaPlaca.delete(0, END)
        self.caixaItens.delete(0, END)
        self.caixaValor.delete(0, END)
        self.caixaId.delete(0, END)

    def inserir_orcamento(self):
        customer = Orcamentos()
        customer.nome_cliente = self.caixaCliente.get()
        customer.cpf_cliente = self.caixaCpfCliente.get()
        customer.nome_mecanico = self.caixaMecanico.get()
        customer.cpf_mecanico = self.caixaCpfMecanico.get()
        customer.carro_placa = self.caixaPlaca.get()
        customer.itens = self.caixaItens.get()
        customer.valor = self.caixaValor.get()
        customer.add_orcamento()
        self.popular()
        self.limpar_caixas()

    def alterar_orcamento(self):
        customer = Orcamentos()
        customer.nome_cliente = self.caixaCliente.get()
        customer.cpf_cliente = self.caixaCpfCliente.get()
        customer.nome_mecanico = self.caixaMecanico.get()
        customer.cpf_mecanico = self.caixaCpfMecanico.get()
        customer.carro_placa = self.caixaPlaca.get()
        customer.itens = self.caixaItens.get()
        customer.valor = self.caixaValor.get()
        customer.idorcamento = self.caixaId.get()
        customer.atualizar_orcamento()
        self.popular()
        self.limpar_caixas()

    def excluir_orcamento(self):
        customer = Orcamentos()
        customer.idorcamento = self.caixaId.get()
        customer.deletar_orcamento()
        self.popular()
        self.limpar_caixas()

    def voltar_tela(self):
        self.janela.destroy()
        #from telaMecanico import TelaMecanico
        return

    def popular(self):
        self.trv.delete(*self.trv.get_children())
        costumer = Orcamentos()
        for i in costumer.populate():
            self.trv.insert('', 'end', values=i)

    def leitura_apenas(self):
        self.caixaId.configure(state='disabled')

    def normal(self):
        self.caixaId.configure(state='normal')
    
    def hoverIn1(self, event):  # verde
        event.widget.config(bg="#32CD32", fg="white", relief=GROOVE)

    def hoverIn2(self, event):  # azul
        event.widget.config(bg="#6495ED", fg="white", relief=GROOVE)

    def hoverIn3(self, event):  # vermelho
        event.widget.config(bg="#FF0000", fg="white", relief=GROOVE)

    def hoverIn4(self, event):  # amarelo
        event.widget.config(bg="#FFD700", fg="white", relief=GROOVE)

    def hoverOut(self, event):
        event.widget.config(bg="#566981", fg="#e1e3db", relief=RAISED)


minhaTela = CadastrarOrcamento()
