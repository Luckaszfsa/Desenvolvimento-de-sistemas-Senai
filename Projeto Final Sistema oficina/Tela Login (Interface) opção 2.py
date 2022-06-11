from tkinter import *

class Tela_de_Login:
    def __init__(self):
        self.janela = Tk()
        self.janela.minsize(width=1200,height=600)
        self.janela.title("Sistema Automotivo Soluções")
        self.janela.resizable(False,False)
        self.LoginCanvas = Canvas(self.janela, width = 500, height=370)
        self.LoginCanvas.pack(expand=1,fill=BOTH)
     

        self.Back = PhotoImage(file="back.png")
        self.LoginCanvas.create_image(0,0,image=self.Back, anchor=NW)

        self.Fundo = PhotoImage(file="fundo.png")
        self.LoginCanvas.create_image(600,370,image=self.Fundo)
        self.LoginCanvas.create_rectangle(400,200,800,547,width=2,outline="black")

        self.logo = PhotoImage(file="logo.png")
        self.LoginCanvas.create_image(500,330, image=self.logo)

        
        self.LoginCanvas.create_text(630,300,text="Login",font=("Arial",12,"bold"),fill="white")
        self.LoginUser = Entry(self.LoginCanvas,width=20,highlightcolor="blue")
        self.LoginCanvas.create_window(730,300,window=self.LoginUser)
        self.LoginCanvas.create_text(630,380,text="Senha",font=("Arial",12,"bold"),fill="white")
        self.SenhaUser = Entry(self.LoginCanvas,width=20,highlightcolor="blue",show="*")
        self.LoginCanvas.create_window(730,380,window=self.SenhaUser)
        self.ButtonAccept = Button(self.LoginCanvas,text="ENTRAR",width=10,bg="#4682B4",fg="white",relief=RAISED,command=self.verificaLogin)
        self.LoginCanvas.create_window(600,430,window=self.ButtonAccept)
        
        self.ButtonAccept.bind("<Enter>", self.hoverIn)
        self.ButtonAccept.bind('<Leave>', self.hoverOut)
      

        mainloop()

    def hoverIn(self, event):
           event.widget.config(bg="#00FF00",fg="white")

    def hoverOut(self, event):
            event.widget.config(bg="#4682B4")
        
        

    def verificaLogin(self):
        return

minhaTela = Tela_de_Login()
