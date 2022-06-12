from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import BOLD
from turtle import width
from clientes import Clientes


class tela_ver_cadastrar_clientes():
    def __init__(self):

        self.janelaCad_Cliente = Tk()

        self.janelaCad_Cliente.title('Automativo Soluções')
        self.janelaCad_Cliente.geometry('1200x600')
        self.janelaCad_Cliente.title('Recepção')
        self.janelaCad_Cliente.config(bg="#484848")
        self.janelaCad_Cliente.state("zoomed")

# ============= SEÇÕES ================ #

        self.container1 = LabelFrame(
            self.janelaCad_Cliente, bg="#484848", fg="#e1e3db")

        self.wrapper1 = LabelFrame(
            self.container1, text='Clientes Cadastrados', font=("Roboto", 18, 'bold'), bg="#484848", fg="#e1e3db")
        self.wrapper2 = LabelFrame(
            self.janelaCad_Cliente, text='Procurar Cliente', font=("Roboto", 18, 'bold'), bg="#484848", fg="#e1e3db")
        self.wrapper3 = LabelFrame(
            self.container1, width=400, text='Dados do Cliente', font=("Roboto", 18, 'bold'), bg="#484848", fg="#e1e3db")
        self.rodape = Frame(self.janelaCad_Cliente, bg="#484848")

        self.container1.pack(fill='both', expand='no', padx=30, pady=10)
        self.wrapper1.pack(fill='both', expand='yes',
                           padx=25, pady=10, ipady=30, side="left")
        self.wrapper2.pack(fill='none', expand='no', padx=10, pady=10)
        self.wrapper3.pack(fill='x', expand='no', ipadx=30,
                           padx=30, ipady=75, side="right")
        self.rodape.pack(fill='both', expand='yes', padx=20)


# ========= SEÇÃO DADOS DO CLIENTE ======= #
# ---------- LABELS & ENTRYS ----------- #
        self.lbl2 = Label(self.wrapper1, text='Nome', font=(
            "Roboto", 16), bg="#484848", fg="#e1e3db")
        self.lbl2.grid(row=0, column=0, padx=5, pady=3)
        self.ent2 = Entry(self.wrapper1, width=40)
        self.ent2.grid(row=0, column=1, padx=5, pady=3)

        self.lbl3 = Label(self.wrapper1, text='CPF', font=(
            "Roboto", 16), bg="#484848", fg="#e1e3db")
        self.lbl3.grid(row=1, column=0, padx=5, pady=3)
        self.ent3 = Entry(self.wrapper1, width=40)
        self.ent3.grid(row=1, column=1, padx=5, pady=3)

        self.lbl4 = Label(self.wrapper1, text='Carro/Placa', font=(
            "Roboto", 16), bg="#484848", fg="#e1e3db")
        self.lbl4.grid(row=2, column=0, padx=5, pady=3)
        self.ent4 = Entry(self.wrapper1, width=40)
        self.ent4.grid(row=2, column=1, padx=5, pady=3)

        self.lbl5 = Label(self.wrapper1, text='Telefone', font=(
            "Roboto", 16), bg="#484848", fg="#e1e3db")
        self.lbl5.grid(row=3, column=0, padx=5, pady=3)
        self.ent5 = Entry(self.wrapper1, width=40)
        self.ent5.grid(row=3, column=1, padx=5, pady=3)

        self.lbl6 = Label(self.wrapper1, text='E-mail', font=(
            "Roboto", 16), bg="#484848", fg="#e1e3db")
        self.lbl6.grid(row=0, column=2, padx=5, pady=3)
        self.ent6 = Entry(self.wrapper1, width=40)
        self.ent6.grid(row=0, column=3, padx=5, pady=3)

        self.lbl7 = Label(self.wrapper1, text='Endereço', font=(
            "Roboto", 16), bg="#484848", fg="#e1e3db")
        self.lbl7.grid(row=1, column=2, padx=5, pady=3)
        self.ent7 = Entry(self.wrapper1, width=40)
        self.ent7.grid(row=1, column=3, padx=5, pady=3)

        self.lbl8 = Label(self.wrapper1, text='ID Cliente', font=(
            "Roboto", 16), bg="#484848", fg="#e1e3db")
        self.lbl8.grid(row=2, column=2, padx=5, pady=3)
        self.ent8 = Entry(self.wrapper1)
        self.ent8.grid(row=2, column=3, padx=5, pady=3, sticky='W')

# ------------ BOTÕES -------------- #
        self.addBtn = Button(self.wrapper1, text='Adicionar', font=(
            "Roboto", 16), command=self.inserir_cliente, bg="#566981", fg="#e1e3db", relief=RAISED)
        self.addBtn.bind("<Enter>", self.hoverIn1)
        self.addBtn.bind("<Leave>", self.hoverOut)

        self.alterarBtn = Button(self.wrapper1, text='Alterar', font=(
            "Roboto", 16), command=self.alterar_cliente, bg="#566981", fg="#e1e3db", relief=RAISED)
        self.alterarBtn .bind("<Enter>", self.hoverIn4)
        self.alterarBtn .bind("<Leave>", self.hoverOut)

        self.excluirBtn = Button(self.wrapper1, font=("Roboto", 16), text='Excluir',
                                 command=self.excluir_cliente, bg="#566981", fg="#e1e3db", relief=RAISED)
        self.excluirBtn.bind("<Enter>", self.hoverIn3)
        self.excluirBtn.bind("<Leave>", self.hoverOut)

        self.addBtn.grid(row=4, column=1, padx=10, pady=10, ipadx=25)
        self.alterarBtn.grid(row=4, column=2, padx=5, pady=3, ipadx=20)
        self.excluirBtn.grid(row=4, column=3, padx=5, pady=3, ipadx=25)

# ============ SEÇÃO CLIENTES CADASTRADOS =============== #
# ------------------- TREEVIEW ------------------ #
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("mystyle.Treeview", font=("Roboto", 14))
        style.configure("mystyle.Treeview.Heading", font=("Roboto", 16))
        style.configure("Treeview", background="silver",
                        rowheight=25, fieldbackground="#E0FFFF",)
        style.configure("Heading", background="#4682B4", foreground="white")

        self.cabecalho = ('#', 'nome', 'cpf', 'carro',
                          'telefone', 'email', 'endereco')
        self.trv = ttk.Treeview(
            self.wrapper2, selectmode='browse', columns=self.cabecalho, show='headings')

        self.trv.column('#', width=30)
        self.trv.column('nome', width=350, anchor='center')
        self.trv.column('cpf', width=180, anchor='center')
        self.trv.column('carro', width=180, anchor='center')
        self.trv.column('telefone', width=180, anchor='center')
        self.trv.column('endereco', width=320, anchor='center')

        self.trv.heading('#', text='#')
        self.trv.heading('nome', text='Nome')
        self.trv.heading('cpf', text='CPF')
        self.trv.heading('carro', text='Carro/Placa')
        self.trv.heading('telefone', text='Telefone')
        self.trv.heading('email', text='E-mail')
        self.trv.heading('endereco', text='Endereço')

        self.trv.bind('<Double 1>', self.pegar_linha)
        self.trv.pack()

        self.popular()

# ============= SEÇÃO PROCURAR =========== #
# ---------- LABELS & ENTRYS ----------- #
        self.lbl1 = Label(self.wrapper3, font=(
            "Roboto", 14), text='Palavra-Chave', bg="#566981", fg="#e1e3db", relief=RAISED)
        self.lbl1.pack(side='left', padx=10, pady=10, ipadx=50)

        self.busca = Entry(self.wrapper3)
        self.busca.pack(side='left', padx=6, pady=10, ipadx=80, ipady=2)


# ------------- BOTÃO ------------- #
        self.procurarBtn = Button(self.wrapper3, text='Procurar', font=(
            "Roboto", 14), command=self.procurar, bg="#566981", fg="#e1e3db", relief=RAISED)
        self.procurarBtn.pack(side='left', padx=20, pady=10, ipadx=10)
        self.procurarBtn.bind("<Enter>", self.hoverIn2)
        self.procurarBtn.bind("<Leave>", self.hoverOut)

        self.limparBtn = Button(self.wrapper3, text='Limpar', font=(
            "Roboto", 14), command=self.limpar, bg="#566981", fg="#e1e3db", relief=RAISED)
        self.limparBtn.pack(side='left', padx=6, pady=10, ipadx=10)
        self.limparBtn .bind("<Enter>", self.hoverIn4)
        self.limparBtn .bind("<Leave>", self.hoverOut)

        self.mostrarBtn = Button(
            self.wrapper2, padx=30, text='Mostrar Todos', font=("Roboto", 16), command=self.popular, bg="#566981", fg="#e1e3db", relief=RAISED)
        self.mostrarBtn.pack(side='left', padx=700, pady=10)
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
        customer = Clientes()
        self.limpar_caixas()
        for item in self.trv.selection():
            self.id = self.trv.item(item, 'values')
        identificador = self.id[0]

        customer.identificar_linha(identificador)
        self.ent8.insert(INSERT, customer.idcliente)
        self.ent2.insert(INSERT, customer.nome)
        self.ent3.insert(INSERT, customer.cpf)
        self.ent4.insert(INSERT, customer.carro)
        self.ent5.insert(INSERT, customer.telefone)
        self.ent6.insert(INSERT, customer.email)
        self.ent7.insert(INSERT, customer.endereco)

    def limpar_caixas(self):
        self.normal()
        self.ent2.delete(0, END)
        self.ent3.delete(0, END)
        self.ent4.delete(0, END)
        self.ent5.delete(0, END)
        self.ent6.delete(0, END)
        self.ent7.delete(0, END)
        self.ent8.delete(0, END)

    def procurar(self):
        customer = Clientes()
        nome = self.busca.get()
        self.normal()
        self.limpar_caixas()

        customer.buscar_cliente(nome)

        self.ent2.insert(INSERT, customer.nome)
        self.ent3.insert(INSERT, customer.cpf)
        self.ent4.insert(INSERT, customer.carro)
        self.ent5.insert(INSERT, customer.telefone)
        self.ent6.insert(INSERT, customer.email)
        self.ent7.insert(INSERT, customer.endereco)
        self.ent8.insert(INSERT, customer.idcliente)
        self.leitura_apenas()

    def limpar(self):
        self.normal()
        self.busca.delete(0, END)
        self.ent2.delete(0, END)
        self.ent3.delete(0, END)
        self.ent4.delete(0, END)
        self.ent5.delete(0, END)
        self.ent6.delete(0, END)
        self.ent7.delete(0, END)
        self.ent8.delete(0, END)

    def inserir_cliente(self):
        customer = Clientes()
        customer.nome = self.ent2.get()
        customer.cpf = self.ent3.get()
        customer.carro = self.ent4.get()
        customer.telefone = self.ent5.get()
        customer.email = self.ent6.get()
        customer.endereco = self.ent7.get()
        customer.add_cliente()
        self.popular()
        self.limpar_caixas()

    def alterar_cliente(self):
        customer = Clientes()
        customer.nome = self.ent2.get()
        customer.cpf = self.ent3.get()
        customer.carro = self.ent4.get()
        customer.telefone = self.ent5.get()
        customer.email = self.ent6.get()
        customer.endereco = self.ent7.get()
        customer.idcliente = self.ent8.get()
        customer.atualizar_cliente()
        self.popular()
        self.limpar_caixas()

    def excluir_cliente(self):
        customer = Clientes()
        customer.idcliente = self.ent8.get()
        customer.deletar_cliente()
        self.popular()
        self.limpar_caixas()

    def voltar_tela(self):
        self.janelaCad_Cliente.destroy()
    #     # from telaRecepcao import Tela_de_Recepcao
        return

    def popular(self):
        self.trv.delete(*self.trv.get_children())
        costumer = Clientes()
        for i in costumer.populate():
            self.trv.insert('', 'end', values=i)

    def leitura_apenas(self):
        self.ent8.configure(state='disabled')

    def normal(self):
        self.ent8.configure(state='normal')

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


minhaTela = tela_ver_cadastrar_clientes()
