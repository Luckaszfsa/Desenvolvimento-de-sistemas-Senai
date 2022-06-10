from tkinter import *
from tkinter import messagebox


class Mecanico:
    def __init__(self):
        self.janela = Tk()
        self.janela.title('Mecânico')
        self.titleStyles = ('Arial', 14)
        self.textStyles = ('Roboto', 13)
        self.janela.configure(bg='#363636')
        self.janela.minsize(width=1200,height=600)
        self.janela.state("zoomed")
        
        self.LoginCanvas = Canvas(self.janela, width = 600, height=370)
        self.LoginCanvas.pack(expand=1,fill=BOTH)
        
        self.Back = PhotoImage(file="mecanico.png")
        self.LoginCanvas.create_image(800,400,image=self.Back)
        
       
        self.hoverColor2 = '#1E90FF'
        self.hoverColor3 = '#FF0000'

        self.botaoCadastrar = Button(self.LoginCanvas,text="Cadastrar\nOrçamento",font=self.textStyles,width=15,height=4,pady=5,bg="#4682B4",fg="white",relief=RAISED,command=self.cadastrarOrcamento)
        self.LoginCanvas.create_window(1100,330,window=self.botaoCadastrar)
        self.botaoCadastrar.bind("<Enter>", self.hoverIn1)
        self.botaoCadastrar.bind("<Leave>", self.hoverOut)
        

        self.botaoOrdem = Button(self.LoginCanvas,text="Ordem\n de \nServiço",font=self.textStyles,width=15,height=4,pady=1,bg="#4682B4",fg="white",relief=RAISED,command=self.verOrdem)
        self.LoginCanvas.create_window(1100,450,window=self.botaoOrdem)
        self.botaoOrdem.bind("<Enter>", self.hoverIn1)
        self.botaoOrdem.bind("<Leave>", self.hoverOut)
        

        self.botaoSair = Button(self.LoginCanvas,text="SAIR",font=self.textStyles,width=5,bg="#4682B4",fg="white",pady=5,relief=RAISED,command=self.saiu)
        self.LoginCanvas.create_window(1100,650,window=self.botaoSair)
        self.botaoSair.bind("<Enter>", self.hoverIn3)
        self.botaoSair.bind("<Leave>", self.hoverOut)
       

        self.titulo = Label(self.janela,bg='#363636',fg='white', font=self.titleStyles, text='MECÂNICO')
        self.titulo.pack(padx=0, pady=10)

               
        
        mainloop()

    def cadastrarOrcamento(self):
        return

    def hoverIn1(self, event):
        event.widget.configure(bg=self.hoverColor2, fg="white",relief=GROOVE)
    def hoverIn3(self, event):
        event.widget.configure(bg=self.hoverColor3, fg="white",relief=GROOVE)
    def hoverOut(self, event):
        event.widget.configure(bg='#4682B4',relief=RAISED)
    def hoverOut2(self, event):
        event.widget.configure(relief=RAISED)

    def saiu(self):
        return

    def verOrdem(self):
        return
           
        
        

minhaTela = Mecanico()
