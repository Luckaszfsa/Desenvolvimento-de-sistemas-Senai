from tkinter import *


class Gerente:
   def __init__(self):
      self.janela = Tk()
      self.janela.title('Gerência')
      self.titleStyles = ('Arial', 14)
      self.textStyles = ('Roboto', 14)
      self.imgStyles = ('Roboto', 15)
      self.janela.minsize(1200, 600)
      self.janela.maxsize(1200, 600)

      self.img = PhotoImage(master=self.janela, file="tela-gerente.png")
      self.img1 = self.img.subsample(1, 1)

      self.localIMG = Label(master=self.janela, image=self.img1)
      self.localIMG.pack(fill='both', anchor='nw')

      self.botaoGerenciar = Button(self.localIMG, command=self.gerenciarFuncionarios,
                                    font=self.textStyles, text='Gerenciar\nFuncionários', width=20, height=2, bg="#87CEFA")
      self.botaoGerenciar.bind("<Enter>", self.hoverIn)
      self.botaoGerenciar.bind("<Leave>", self.hoverOut)
      self.botaoGerenciar.place(x=810, y=150)

      self.botaoOrdem = Button(self.localIMG, command=self.verOrdem, font=self.textStyles,
                              text='Ordens de Serviços', width=20, height=2, bg="#87CEFA")
      self.botaoOrdem.bind("<Enter>", self.hoverIn)
      self.botaoOrdem.bind("<Leave>", self.hoverOut)
      self.botaoOrdem.place(x=810, y=250)

      self.botaoCliente = Button(self.localIMG, command=self.verCliente,
                                 font=self.textStyles, text='Cliente', width=20, height=2, bg="#87CEFA")
      self.botaoCliente.bind("<Enter>", self.hoverIn)
      self.botaoCliente.bind("<Leave>", self.hoverOut)
      self.botaoCliente.place(x=810, y=350)

      self.botaoSair = Button(self.localIMG, command=self.sair,
                              font=self.textStyles, text='Sair', width=15, height=2, bg="#87CEFA")
      self.botaoSair.bind("<Enter>", self.hoverIn2)
      self.botaoSair.bind("<Leave>", self.hoverOut)
      self.botaoSair.place(x=837, y=500)

      mainloop()

   def gerenciarFuncionarios(self):
      #from tela_Gerenciar_Funcionarios import Gerenciar_Funcionarios
      return

   def verOrdem(self):
      return

   def verCliente(self):
      return

   def sair(self):
      return

   def hoverIn(self, event):
      event.widget.config(bg="#1E90FF", fg="white")

   def hoverIn2(self, event):
      event.widget.config(bg="#FF0000", fg="white")

   def hoverOut(self, event):
      event.widget.config(bg="#87CEFA", fg="black")


minhaTela = Gerente()