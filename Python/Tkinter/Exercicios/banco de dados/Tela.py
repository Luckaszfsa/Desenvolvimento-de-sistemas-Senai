from Usuarios import Usuarios
from tkinter import *

class Tela:
    def __init__(self):

        self.janela = Tk()

        self.fonte = ("Verdana", "8")

        self.container1 = Frame(self.janela, pady=10)
        self.container1.pack()

        self.container2 = Frame(self.janela, padx = 20, pady = 5)
        self.container2.pack()

        self.container3 = Frame(self.janela, padx = 20, pady = 5)
        self.container3.pack()

        self.container4 = Frame(self.janela, padx = 20, pady = 5)
        self.container4.pack()

        self.container5 = Frame(self.janela, padx = 20, pady = 5)
        self.container5.pack()

        self.container6 = Frame(self.janela, padx = 20, pady = 5)
        self.container6.pack()

        self.container7 = Frame(self.janela, padx = 20, pady = 5)
        self.container7.pack()

        self.container8 = Frame(self.janela, padx = 20, pady = 5)
        self.container8.pack()

        self.container9 = Frame(self.janela, pady=15)
        self.container9.pack()

        self.titulo = Label(self.container1,
                            text = "Informe os dados: ",
                            font = ("Calibri", "9", "bold"))
        self.titulo.pack()

        self.labelid = Label(self.container2,
                             text= "Id Usuario: ",
                             font=self.fonte,
                             width=10)
        self.labelid.pack(side = LEFT)

        self.caixaid = Entry(self.container2, width = 14,
                             font=self.fonte)
        self.caixaid.pack(side = LEFT)

        self.buscar = Button(self.container2, text="Buscar",
                             font=self.fonte, width=10,
                             command=self.buscarUsuario)
        self.buscar.pack(side = RIGHT)

        self.labelNome = Label(self.container3,
                               text="Nome: ",
                               font=self.fonte, width=10)
        self.labelNome.pack(side = LEFT)

        self.caixaNome = Entry(self.container3, width=25,
                               font=self.fonte)
        self.caixaNome.pack(side = LEFT)

        self.labelTelefone = Label(self.container4,
                               text="Telefone: ",
                               font=self.fonte, width=10)
        self.labelTelefone.pack(side = LEFT)

        self.caixaTelefone = Entry(self.container4, width=25,
                               font=self.fonte)
        self.caixaTelefone.pack(side = LEFT)

        self.labelEmail = Label(self.container5,
                               text="Email: ",
                               font=self.fonte, width=10)
        self.labelEmail.pack(side = LEFT)

        self.caixaEmail = Entry(self.container5, width=25,
                               font=self.fonte)
        self.caixaEmail.pack(side = LEFT)

        self.labelUsuario = Label(self.container6,
                               text="Usuario: ",
                               font=self.fonte, width=10)
        self.labelUsuario.pack(side = LEFT)

        self.caixaUsuario = Entry(self.container6, width=25,
                               font=self.fonte)
        self.caixaUsuario.pack(side = LEFT)

        self.labelSenha = Label(self.container7,
                               text="Senha: ",
                               font=self.fonte, width=10)
        self.labelSenha.pack(side = LEFT)

        self.caixaSenha = Entry(self.container7, width=25,
                               font=self.fonte, show="*")
        self.caixaSenha.pack(side = LEFT)

        self.insert = Button(self.container8,
                             width=12, text="Inserir",
                             command=self.inserirUsuario,
                             font=self.fonte)
        self.insert.pack(side = LEFT)

        self.update = Button(self.container8,
                             width=12, text="Alterar",
                             command=self.alterarUsuario,
                             font=self.fonte)
        self.update.pack(side = LEFT)

        self.delete = Button(self.container8,
                             width=12, text="Excluir",
                             command=self.excluirUsuario,
                             font=self.fonte)
        self.delete.pack(side = LEFT)

        self.mensagem = Label(self.container9,
                              text="",
                              font=("Verdana","9", "italic"))
        self.mensagem.pack()

        mainloop()

    def buscarUsuario(self):
        user = Usuarios()
        idusuario = self.caixaid.get()

        self.mensagem["text"] = user.selectUser(idusuario)

        self.caixaid.delete(0, END)
        self.caixaNome.delete(0, END)
        self.caixaTelefone.delete(0, END)
        self.caixaEmail.delete(0, END)
        self.caixaUsuario.delete(0, END)
        self.caixaSenha.delete(0, END)

        self.caixaid.insert(INSERT, user.idusuario)
        self.caixaNome.insert(INSERT, user.nome)
        self.caixaTelefone.insert(INSERT, user.telefone)
        self.caixaEmail.insert(INSERT, user.email)
        self.caixaUsuario.insert(INSERT, user.usuario)
        self.caixaSenha.insert(INSERT, user.senha)
        

    def inserirUsuario(self):
        user = Usuarios()
        user.nome = self.caixaNome.get()
        user.telefone = self.caixaTelefone.get()
        user.email = self.caixaEmail.get()
        user.usuario = self.caixaUsuario.get()
        user.senha = self.caixaSenha.get()

        self.mensagem["text"] = user.insertUser()

        self.caixaid.delete(0, END)
        self.caixaNome.delete(0, END)
        self.caixaTelefone.delete(0, END)
        self.caixaEmail.delete(0, END)
        self.caixaUsuario.delete(0, END)
        self.caixaSenha.delete(0, END)

    def alterarUsuario(self):
        user = Usuarios()
        user.idusuario = self.caixaid.get()
        user.nome = self.caixaNome.get()
        user.telefone = self.caixaTelefone.get()
        user.email = self.caixaEmail.get()
        user.usuario = self.caixaUsuario.get()
        user.senha = self.caixaSenha.get()

        self.mensagem["text"] = user.updateUser()

        self.caixaid.delete(0, END)
        self.caixaNome.delete(0, END)
        self.caixaTelefone.delete(0, END)
        self.caixaEmail.delete(0, END)
        self.caixaUsuario.delete(0, END)
        self.caixaSenha.delete(0, END)

    def excluirUsuario(self):
        user = Usuarios()
        user.idusuario = self.caixaid.get()

        self.mensagem["text"] = user.deleteUser()

        self.caixaid.delete(0, END)
        self.caixaNome.delete(0, END)
        self.caixaTelefone.delete(0, END)
        self.caixaEmail.delete(0, END)
        self.caixaUsuario.delete(0, END)
        self.caixaSenha.delete(0, END)

minhatela=Tela()









        
