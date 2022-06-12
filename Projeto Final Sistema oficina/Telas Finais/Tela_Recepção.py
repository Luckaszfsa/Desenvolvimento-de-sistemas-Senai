from tkinter import *
from tkinter import messagebox


class Recepcao:
   def __init__(self):
      janela = Tk()
      janela.title('Recepção')
      self.titleStyles = ('Arial', 14)
      self.textStyles = ('Roboto', 13)
      janela.configure(bg='#363636')
      janela.minsize(width=1200,height=600)
      
      self.LoginCanvas = Canvas(master=janela, width = 600, height=370)
      self.LoginCanvas.pack(expand=1,fill=BOTH)
      
      self.Back = PhotoImage(master=janela, file="recepcao.png")
      self.LoginCanvas.create_image(0,0,image=self.Back, anchor=NW)
      
      self.hoverColor1 = '#008000'
      self.hoverColor2 = '#1E90FF'
      self.hoverColor3 = '#FF0000'

      self.botaoCadastrar = Button(self.LoginCanvas,text="Cadastrar\nCliente",font=self.textStyles,width=15,height=4,pady=5,bg="#4682B4",fg="white",relief=RAISED,command=self.cadastrarCliente)
      self.LoginCanvas.create_window(900,130,window=self.botaoCadastrar)
      self.botaoCadastrar.bind("<Enter>", self.hoverIn1)
      self.botaoCadastrar.bind("<Leave>", self.hoverOut)
      

      self.botaoOrcamento = Button(self.LoginCanvas,text="Ver\nOrçamento",font=self.textStyles,width=15,height=4,pady=1,bg="#4682B4",fg="white",relief=RAISED,command=self.verOrcamento)
      self.LoginCanvas.create_window(900,250,window=self.botaoOrcamento)
      self.botaoOrcamento.bind("<Enter>", self.hoverIn2)
      self.botaoOrcamento.bind("<Leave>", self.hoverOut)
      

      self.botaoSair = Button(self.LoginCanvas,text="SAIR",font=self.textStyles,width=5,bg="#4682B4",fg="white",pady=5,relief=RAISED,command=self.saiu)
      self.LoginCanvas.create_window(900,400,window=self.botaoSair)
      self.botaoSair.bind("<Enter>", self.hoverIn3)
      self.botaoSair.bind("<Leave>", self.hoverOut)
      

      self.titulo = Label(janela,bg='#363636',fg='white', font=self.titleStyles, text='RECEPÇÃO')
      self.titulo.pack(padx=0, pady=10)

            
      
      mainloop()

   def cadastrarCliente(self):
      return

   def hoverIn1(self, event):
      event.widget.configure(bg=self.hoverColor1, fg="white",relief=GROOVE)
   def hoverIn2(self, event):
      event.widget.configure(bg=self.hoverColor2, fg="white",relief=GROOVE)
   def hoverIn3(self, event):
      event.widget.configure(bg=self.hoverColor3, fg="white",relief=GROOVE)
   def hoverOut(self, event):
      event.widget.configure(bg='#4682B4',relief=RAISED)
   def hoverOut2(self, event):
      event.widget.configure(relief=RAISED)

   def saiu(self):
      return

   def verOrcamento(self):
      return
         
   def exeRecepcionista(self):
      Recepcao.janela

minhaTela = Recepcao()
