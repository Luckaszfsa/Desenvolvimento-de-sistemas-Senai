from tkinter import *

class Tela_de_Login:
    def __init__(self):
        self.janela = Tk()
        self.janela.geometry("250x200") 
        self.janela.minsize(200, 150) 
        self.janela.maxsize(600, 400)
        
        self.titulo = Label(self.janela,text='PROTÓTIPO DO PROJETO')
        self.titulo.grid(row=0, column=1, padx=5, pady=5, sticky='nwse')

        self.loginTxt = Label(self.janela, text='LOGIN')
        self.loginTxt.grid(row=1, column=0, padx=5, pady=5,sticky='nwse')
        self.loginEnt = Entry(self.janela, width=30)
        self.loginEnt.grid(row=1, column=1, padx=5, pady=5,sticky='nwse')

        self.senhaTxt = Label(self.janela, text='SENHA')
        self.senhaTxt.grid(row=3, column=0, padx=5, pady=5,sticky='nwse')
        self.senhaEnt = Entry(self.janela, width=30)
        self.senhaEnt.grid(row=3, column=1, padx=5, pady=5,sticky='nwse')

        self.entrarBotao = Button(command=self.verificaLogin, text='ENTRAR')
        self.entrarBotao.grid(row=5, column=1, padx=5, pady=5,sticky='nwse')
        mainloop()

    def verificaLogin(self):
        return

minhaTela = Tela_de_Login()
