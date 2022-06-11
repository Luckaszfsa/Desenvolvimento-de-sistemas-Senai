from tkinter import *
from tkinter import messagebox


class Recepcao:
    def __init__(self):
        self.janela = Tk()
        self.janela.title('Recepção')
        self.titleStyles = ('Arial', 14)
        self.textStyles = ('Roboto', 13)
        self.janela.configure(bg='#363636')
        self.janela.minsize(width=1200,height=600)
        self.janela.state("zoomed")
        
        self.LoginCanvas = Canvas(self.janela, width = 600, height=370)
        self.LoginCanvas.pack(expand=1,fill=BOTH)
        
        self.Back = PhotoImage(file="back1.png")
        self.LoginCanvas.create_image(700,350,image=self.Back)
        
        
        self.hoverColor1 = '#1E90FF'
        self.hoverColor2 = '#FF0000'

        self.botaoCadastrar = Button(self.LoginCanvas,text="Cadastrar\nCliente",font=self.textStyles,width=15,height=4,pady=5,bg="#4682B4",fg="white",relief=RAISED,command=self.cadastrarCliente)
        self.LoginCanvas.create_window(1000,250,window=self.botaoCadastrar)
        self.botaoCadastrar.bind("<Enter>", self.hoverIn)
        self.botaoCadastrar.bind("<Leave>", self.hoverOut)
        

        self.botaoOrcamento = Button(self.LoginCanvas,text="Ver\nOrçamento",font=self.textStyles,width=15,height=4,pady=1,bg="#4682B4",fg="white",relief=RAISED,command=self.verOrcamento)
        self.LoginCanvas.create_window(1000,400,window=self.botaoOrcamento)
        self.botaoOrcamento.bind("<Enter>", self.hoverIn)
        self.botaoOrcamento.bind("<Leave>", self.hoverOut)
        

        self.botaoSair = Button(self.LoginCanvas,text="SAIR",font=self.textStyles,width=5,bg="#4682B4",fg="white",pady=5,relief=RAISED,command=self.saiu)
        self.LoginCanvas.create_window(1000,500,window=self.botaoSair)
        self.botaoSair.bind("<Enter>", self.hoverIn2)
        self.botaoSair.bind("<Leave>", self.hoverOut)
       

        self.titulo = Label(self.janela,bg='#363636',fg='white', font=self.titleStyles, text='RECEPÇÃO')
        self.titulo.pack(padx=0, pady=10)

               
        
        mainloop()

    def cadastrarCliente(self):
        return

    def hoverIn(self, event):
        event.widget.configure(bg=self.hoverColor1, fg="white",relief=GROOVE)
    def hoverIn2(self, event):
        event.widget.configure(bg=self.hoverColor2, fg="white",relief=GROOVE)
    def hoverOut(self, event):
        event.widget.configure(bg='#4682B4',relief=RAISED)
    

    def saiu(self):
        return

    def verOrcamento(self):
        return
           
        
        

minhaTela = Recepcao()
