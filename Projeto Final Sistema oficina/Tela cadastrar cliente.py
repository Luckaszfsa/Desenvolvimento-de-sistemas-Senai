from tkinter import *

class Tela_de_Login:
    def __init__(self):
        self.janela = Tk()
        self.janela.geometry("250x200") 
        self.janela.minsize(200, 150) 
        self.janela.maxsize(400, 300)
        self.janela.configure(bg="#708090")

        #Grid.rowconfigure(self.janela,0,weight=1) 
        #Grid.columnconfigure(self.janela,0,weight=1) 
          
        #Grid.rowconfigure(self.janela,1,weight=1) 
      
        
        self.titulo = Label(self.janela,text='PROTÓTIPO DO PROJETO')
        self.titulo.grid(row=0, column=1, padx=5, pady=5, sticky='NWSE')

        self.loginTxt = Label(self.janela, text='LOGIN')
        self.loginTxt.grid(row=1, column=0, padx=5, pady=5,sticky='NWSE')
        self.loginEnt = Entry(self.janela, width=30)
        self.loginEnt.grid(row=1, column=1, padx=5, pady=5,sticky='NWSE')

        self.senhaTxt = Label(self.janela, text='SENHA')
        self.senhaTxt.grid(row=3, column=0, padx=5, pady=5,sticky='NWSE')
        self.senhaEnt = Entry(self.janela, width=30)
        self.senhaEnt.grid(row=3, column=1, padx=5, pady=5,sticky='NWSE')

        self.entrarBotao = Button(command=self.verificaLogin, bg="#00BFFF", text='ENTRAR')
        self.entrarBotao.grid(row=5, column=1, padx=5, pady=5,sticky='NWSE')
        mainloop()

    def verificaLogin(self):
        return

minhaTela = Tela_de_Login()
