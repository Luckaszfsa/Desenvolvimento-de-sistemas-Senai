from tkinter import *

class Tela_de_Login:
    def __init__(self):
        self.janela = Tk()
        self.janela.geometry("500x500") 
        #self.janela.minsize(200, 150) 
        self.janela.maxsize(500, 500)
        self.janela.configure(bg="#363636")

        #Grid.rowconfigure(self.janela,0,weight=1) 
        #Grid.columnconfigure(self.janela,0,weight=1) 
          
        #Grid.rowconfigure(self.janela,1,weight=1) 
          
        photo = PhotoImage(file = r"C:\Users\aluno\Downloads\logo.png" )
        self.titulo = Label(self.janela,image = photo,compound = LEFT, bg="#363636")
        self.titulo.pack(padx=5, pady=5)

        self.frameCima = Frame(self.janela)
        self.frameCima.pack()

        self.frameBaixo = Frame(self.janela)
        self.frameBaixo.pack()
        

        self.loginTxt = Label(self.frameCima, text='LOGIN',width=5)
        self.loginTxt.pack(side='left',padx=5, pady=5)
        self.loginEnt = Entry(self.frameCima, width=30)
        self.loginEnt.pack(side='left',padx=5, pady=5)

        self.senhaTxt = Label(self.frameBaixo, text='SENHA',width=5)
        self.senhaTxt.pack(side='left',padx=5, pady=5)
        self.senhaEnt = Entry(self.frameBaixo, width=30)
        self.senhaEnt.pack(side='left', padx=5, pady=5)

        self.entrarBotao = Button(command=self.verificaLogin, bg="#00BFFF", text='ENTRAR')
        self.entrarBotao.pack(padx=5, pady=5)

        self.entrarBotao.bind("<Enter>", self.hoverIn)
        self.entrarBotao.bind('<Leave>', self.hoverOut)

        mainloop()

    def hoverIn(self, event):
           event.widget.config(bg="#1E90FF")

    def hoverOut(self, event):
            event.widget.config(bg="#00BFFF")
        
        

    def verificaLogin(self):
        return

minhaTela = Tela_de_Login()
