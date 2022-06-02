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
          
        photo = PhotoImage(file = r"C:\Users\lucka\OneDrive\Documentos\SENAI\Logica-de-programa-o-senai\Projeto Final Sistema oficina\logo.png" )
        login = PhotoImage(file = r"C:\Users\lucka\OneDrive\Documentos\SENAI\Logica-de-programa-o-senai\Projeto Final Sistema oficina\Login.png")
        senha = PhotoImage(file = r"C:\Users\lucka\OneDrive\Documentos\SENAI\Logica-de-programa-o-senai\Projeto Final Sistema oficina\SENHA.png")
        self.titulo = Label(self.janela,image = photo, bg="#363636")
        self.titulo.pack()

        self.frameCima = Frame(self.janela, bg="#363636")
        self.frameCima.pack()

        self.frameBaixo = Frame(self.janela, bg="#363636")
        self.frameBaixo.pack()
        

        self.loginTxt = Label(self.frameCima, image = login ,width=50, height=20)
        self.loginTxt.pack(side='left',padx=5, pady=10)
        self.loginEnt = Entry(self.frameCima, width=30)
        self.loginEnt.pack(side='left',padx=5, pady=5)

        self.senhaTxt = Label(self.frameBaixo, image = senha,width=50, height=20)
        self.senhaTxt.pack(side='left',padx=5, pady=5)
        self.senhaEnt = Entry(self.frameBaixo, width=30)
        self.senhaEnt.pack(side='left', padx=5, pady=5)

        self.entrarBotao = Button(command=self.verificaLogin, bg="#00BFFF",relief=RAISED,text='ENTRAR')
        self.entrarBotao.pack(padx=5, pady=5)

        self.entrarBotao.bind("<Enter>", self.hoverIn)
        self.entrarBotao.bind('<Leave>', self.hoverOut)

        mainloop()

    def hoverIn(self, event):
           event.widget.config(bg="#00FF00",fg="white")

    def hoverOut(self, event):
            event.widget.config(bg="#00BFFF")
        
        

    def verificaLogin(self):
        return

minhaTela = Tela_de_Login()
