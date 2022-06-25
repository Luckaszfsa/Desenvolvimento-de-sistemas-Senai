from tkinter import *
class Tela:
    def __init__(self):
        self.janela = Tk()

        self.fontePadrao = ("Arial", "10")

        self.container1 = Frame(self.janela, pady=10)
        self.container1.pack()

        self.container2 = Frame(self.janela, padx=20)
        self.container2.pack()

        self.container3 = Frame(self.janela, padx=20)
        self.container3.pack()

        self.container4 = Frame(self.janela, pady=20)
        self.container4.pack()

        self.titulo = Label(self.container1,
                            text="Dados do usuário",
                            font=("Arial", "10", "bold"))
        self.titulo.pack()

        self.nome = Label(self.container2,
                          text="Nome:",
                          font=self.fontePadrao)
        self.nome.pack(side=LEFT)

        self.caixaNome = Entry(self.container2,
                               width=30,
                               font=self.fontePadrao)
        self.caixaNome.pack(side=LEFT)

        self.senha = Label(self.container3,
                          text="Senha:",
                          font=self.fontePadrao)
        self.senha.pack(side=LEFT)

        self.caixaSenha = Entry(self.container3,
                               width=30,
                               font=self.fontePadrao,
                                show="*")
        self.caixaSenha.pack(side=LEFT)

        self.autenticar = Button(self.container4,
                                 text="Autenticar",
                                 width=12,
                                 command=self.verificaSenha,
                                 font=("Calibri", "8"))
        self.autenticar.pack()

        self.msg = Label(self.container4,
                         text="", font=self.fontePadrao)
        self.msg.pack()
        
        mainloop()

    def verificaSenha(self):
        usuario = self.caixaNome.get()
        senha = self.caixaSenha.get()
        if usuario == "Ícaro" and senha == "dev123":
            self.msg["text"] = "Autenticado"
        else:
            self.msg["text"] = "Erro na autenticação"

minhatela = Tela()




