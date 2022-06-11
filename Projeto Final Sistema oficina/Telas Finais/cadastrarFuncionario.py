from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from funcionario import TabFunc


class ver_cadastrar_func():
    def __init__(self):

        self.janelaCad_Func = Tk()
        self.janelaCad_Func.title('Cadastro de Funcionários')
        self.janelaCad_Func.geometry('1200x600')
        self.janelaCad_Func.config(bg="#484848")
        self.janelaCad_Func.state("zoomed")

# ============= SEÇÕES ================ #

        self.container1 = LabelFrame(self.janelaCad_Func,bg="#484848",fg="#e1e3db")

        self.wrapper1 = LabelFrame(
            self.container1, text='Dados do Funcionário',font=("Roboto",16),bg="#484848",fg="#e1e3db")
        self.wrapper2 = LabelFrame(
            self.janelaCad_Func, text='Funcionários',font=("Roboto",16),bg="#484848",fg="#e1e3db")
        self.wrapper3 = LabelFrame(
            self.container1,font=("Roboto",16), text='Procurar',bg="#484848",fg="#e1e3db")
        self.rodape = Frame(self.janelaCad_Func, bg="#484848")

        self.container1.pack(fill='both', expand='no', padx=30, pady=10)
        self.wrapper1.pack(fill='both', expand='yes',
                           padx=100, pady=10, side="left")
        self.wrapper2.pack(fill='both', expand='no', padx=20, pady=10)
        self.wrapper3.pack(fill='both', expand='no',
                           padx=20, pady=10, side="right")
        self.rodape.pack(fill='both', expand='no', padx=20, pady=(0, 20))


# ========= SEÇÃO DADOS DO FUNCIONÁRIO ======= #
# ---------- LABELS & ENTRYS ----------- #
        self.lbl2 = Label(self.wrapper1, text='Nome',bg="#484848",fg="#e1e3db")
        self.lbl2.grid(row=0, column=0, padx=5, pady=3)
        self.ent2 = Entry(self.wrapper1)
        self.ent2.grid(row=0, column=1, padx=5, pady=3)

        self.lbl3 = Label(self.wrapper1, text='CPF',bg="#484848",fg="#e1e3db")
        self.lbl3.grid(row=1, column=0, padx=5, pady=3)
        self.ent3 = Entry(self.wrapper1)
        self.ent3.grid(row=1, column=1, padx=5, pady=3)

        self.lbl4 = Label(self.wrapper1, text='Cargo',bg="#484848",fg="white")
        self.lbl4.grid(row=2, column=0, padx=5, pady=3)
        self.ent4 = Entry(self.wrapper1)
        self.ent4.grid(row=2, column=1, padx=5, pady=3)

        self.lbl5 = Label(self.wrapper1, text='Login',bg="#484848",fg="#e1e3db")
        self.lbl5.grid(row=3, column=0, padx=5, pady=3)
        self.ent5 = Entry(self.wrapper1)
        self.ent5.grid(row=3, column=1, padx=5, pady=3)

        self.lbl6 = Label(self.wrapper1, text='Senha',bg="#484848",fg="#e1e3db")
        self.lbl6.grid(row=0, column=2, padx=5, pady=3)
        self.ent6 = Entry(self.wrapper1)
        self.ent6.grid(row=0, column=3, padx=5, pady=3)

        self.lbl7 = Label(self.wrapper1, text='ID Funcionário',bg="#484848",fg="#e1e3db")
        self.lbl7.grid(row=1, column=2, padx=5, pady=3)
        self.ent7 = Entry(self.wrapper1)
        self.ent7.grid(row=1, column=3, padx=5, pady=3, sticky='W')

# ------------ BOTÕES -------------- #
        self.addBtn = Button(self.wrapper1, text='Adicionar',
                             command=self.inserir_func,bg="#566981",fg="#e1e3db",relief=RAISED)
        self.addBtn.bind("<Enter>", self.hoverIn1)
        self.addBtn.bind("<Leave>", self.hoverOut)
        self.alterarBtn = Button(
            self.wrapper1, text='Alterar', command=self.alterar_func,bg="#566981",fg="#e1e3db",relief=RAISED)
        self.alterarBtn .bind("<Enter>", self.hoverIn4)
        self.alterarBtn .bind("<Leave>", self.hoverOut)
        self.excluirBtn = Button(
            self.wrapper1, text='Excluir', command=self.excluir_func,bg="#566981",fg="#e1e3db",relief=RAISED)
        self.excluirBtn.bind("<Enter>", self.hoverIn3)
        self.excluirBtn.bind("<Leave>", self.hoverOut)
        self.addBtn.grid(row=4, column=0, padx=5, pady=3, ipadx=25)
        self.alterarBtn.grid(row=4, column=1, padx=2, pady=3, ipadx=20)
        self.excluirBtn.grid(row=4, column=2, padx=2, pady=3, ipadx=25)


# ========== SEÇÃO FUNCIONÁRIOS CADASTRADOS ============ #
# ------------------- TREEVIEW ------------------ #
        self.cabecalho = ('#', 'nome', 'cpf', 'cargo',
                          'login', 'senha')
        self.trv = ttk.Treeview(
            self.wrapper2, selectmode='browse', columns=self.cabecalho, show='headings')

        self.trv.column('#', width=30)
        self.trv.column('nome', anchor='center', width=350)
        self.trv.column('cpf', anchor='center', width=130)
        self.trv.column('cargo', anchor='center', width=120)
        self.trv.column('login', anchor='center', width=110)
        self.trv.column('senha', anchor='center', width=110)

        self.trv.heading('#', text='#')
        self.trv.heading('nome', text='Nome')
        self.trv.heading('cpf', text='CPF')
        self.trv.heading('cargo', text='Cargo')
        self.trv.heading('login', text='Login')
        self.trv.heading('senha', text='Senha')

        self.trv.bind('<Double 1>', self.pegar_linha)
        self.trv.pack()

        self.popular()


# ============= SEÇÃO PROCURAR =========== #
# ---------- LABELS & ENTRYS ----------- #
        self.lbl1 = Label(self.wrapper3, text='Palavra-Chave',bg="#566981",fg="#e1e3db",relief=RAISED)
        self.lbl1.pack(side='right', padx=10, pady=10, ipadx=50)

        self.busca = Entry(self.wrapper3)
        self.busca.pack(side='right', padx=6, pady=10, ipadx=15)


# ------------- BOTÕES ------------- #
        self.procurarBtn = Button(
            self.wrapper3, text='Procurar', command=self.procurar, bg="#566981",fg="#e1e3db",relief=RAISED)
        self.procurarBtn.pack(side='right', padx=6, pady=10)
        self.procurarBtn.bind("<Enter>", self.hoverIn2)
        self.procurarBtn.bind("<Leave>", self.hoverOut)

        self.limparBtn = Button(
            self.wrapper3, text='Limpar', command=self.limpar,bg="#566981",fg="#e1e3db",relief=RAISED)
        self.limparBtn.pack(side='right', padx=6, pady=10)
        self.limparBtn .bind("<Enter>", self.hoverIn4)
        self.limparBtn .bind("<Leave>", self.hoverOut)

        self.mostrarBtn = Button(
            self.wrapper2, text='Mostrar Todos', command=self.popular,bg="#566981",fg="#e1e3db",relief=RAISED)
        self.mostrarBtn.pack(side='right', padx=600, pady=10)
        self.mostrarBtn.bind("<Enter>", self.hoverIn2)
        self.mostrarBtn.bind("<Leave>", self.hoverOut)


# ========= SEÇÃO RODAPÉ ======= #
# ---------- BOTÃO ----------- #
        self.voltarBtn = Button(
            self.rodape, text='Voltar', width='20', command=self.voltar_tela,bg="#cc0000",fg="#e1e3db",relief=RAISED)
        self.voltarBtn.pack(side='right')

        mainloop()

# ============= FUNÇÕES ============== #
    def pegar_linha(self, identificador):
        staff = TabFunc()
        self.normal()
        self.limpar_caixas()
        for item in self.trv.selection():
            self.id = self.trv.item(item, 'values')
        identificador = self.id[0]

        staff.identificar_linha(identificador)
        self.ent8.insert(INSERT, staff.idfunc)
        self.ent2.insert(INSERT, staff.nome)
        self.ent3.insert(INSERT, staff.cpf)
        self.ent4.insert(INSERT, staff.cargo)
        self.ent5.insert(INSERT, staff.login)
        self.ent6.insert(INSERT, staff.senha)
        self.leitura_apenas()

    def limpar_caixas(self):
        self.normal()
        self.ent2.delete(0, END)
        self.ent3.delete(0, END)
        self.ent4.delete(0, END)
        self.ent5.delete(0, END)
        self.ent6.delete(0, END)
        self.ent8.delete(0, END)

    def procurar(self):
        self.trv.delete(*self.trv.get_children())
        staff = TabFunc()
        nome = self.busca.get()
        for i in staff.filtrar_func(nome):
            self.trv.insert('', 'end', values=i)

    def limpar(self):
        self.normal()
        self.busca.delete(0, END)
        self.ent2.delete(0, END)
        self.ent3.delete(0, END)
        self.ent4.delete(0, END)
        self.ent5.delete(0, END)
        self.ent6.delete(0, END)
        self.ent8.delete(0, END)

    def inserir_func(self):
        staff = TabFunc()
        staff.nome = self.ent2.get()
        staff.cpf = self.ent3.get()
        staff.cargo = self.ent4.get()
        staff.login = self.ent5.get()
        staff.senha = self.ent6.get()
        staff.add_func()
        self.popular()
        self.limpar_caixas()

    def alterar_func(self):
        staff = TabFunc()
        staff.nome = self.ent2.get()
        staff.cpf = self.ent3.get()
        staff.cargo = self.ent4.get()
        staff.login = self.ent5.get()
        staff.senha = self.ent6.get()
        staff.idfunc = self.ent8.get()
        staff.atualizar_func()
        self.popular()
        self.limpar_caixas()

    def excluir_func(self):
        staff = TabFunc()
        staff.idfunc = self.ent8.get()
        staff.deletar_func()
        self.popular()
        self.limpar_caixas()

    def voltar_tela(self):
        self.janelaCad_Func.destroy()
        from tela_Gerencia import Gerente
        Gerente()
        return 

    def popular(self):
        self.trv.delete(*self.trv.get_children())
        staff = TabFunc()
        for i in staff.populate():
            self.trv.insert('', 'end', values=i)

    def leitura_apenas(self):
        self.ent8.configure(state='disabled')

    def normal(self):
        self.ent8.configure(state='normal')

    def hoverIn1(self, event):#verde
           event.widget.config(bg="#32CD32",fg="white",relief=GROOVE)
    def hoverIn2(self, event):#azul
           event.widget.config(bg="#6495ED",fg="white",relief=GROOVE)
    def hoverIn3(self, event):#vermelho
           event.widget.config(bg="#FF0000",fg="white",relief=GROOVE)
    def hoverIn4(self, event):#amarelo
           event.widget.config(bg="#FFD700",fg="white",relief=GROOVE)

    def hoverOut(self, event):
            event.widget.config(bg="#566981",fg="#e1e3db",relief=RAISED)


minhaTela = ver_cadastrar_func()
