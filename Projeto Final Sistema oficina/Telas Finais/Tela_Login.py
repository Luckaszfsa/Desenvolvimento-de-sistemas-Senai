from tkinter import *
import sqlite3
from tkinter import messagebox

class Tela_de_Login:
   def __init__(self):
      self.janela = Tk()
      self.janela.minsize(width=1200,height=600)
      self.janela.title("Sistema Automotivo Soluções")
      self.janela.resizable(False,False)
      self.LoginCanvas = Canvas(self.janela, width = 600, height=370)
      self.LoginCanvas.pack(expand=1,fill=BOTH)


      self.Back = PhotoImage(master=self.janela, file="login.png")
      self.LoginCanvas.create_image(0,0,image=self.Back, anchor=NW)

      # self.Fundo = PhotoImage(master=self.janela, file="back.png")
      # self.LoginCanvas.create_image(600,370,image=self.Fundo)
      # self.LoginCanvas.create_rectangle(400,200,800,547,width=2,outline="black")

      self.logo = PhotoImage(master=self.janela, file="logo.png")
      self.LoginCanvas.create_image(900,150, image=self.logo)


      self.LoginCanvas.create_text(800,300,text="Login",font=("Arial",12,"bold"),fill="white")
      self.LoginUser = Entry(self.LoginCanvas,width=20,highlightcolor="blue")
      self.LoginCanvas.create_window(900,300,window=self.LoginUser)
      self.LoginCanvas.create_text(800,350,text="Senha",font=("Arial",12,"bold"),fill="white")
      self.SenhaUser = Entry(self.LoginCanvas,width=20,highlightcolor="blue",show="*")
      self.LoginCanvas.create_window(900,350,window=self.SenhaUser)
      self.ButtonAccept = Button(self.LoginCanvas,text="ENTRAR",width=10,bg="#4682B4",fg="white",relief=RAISED,command=self.verificaLogin)
      self.LoginCanvas.create_window(900,430,window=self.ButtonAccept)

      self.ButtonAccept.bind("<Enter>", self.hoverIn)
      self.ButtonAccept.bind('<Leave>', self.hoverOut)


      mainloop()

   def hoverIn(self, event):
         event.widget.config(bg="#00FF00",fg="white")

   def hoverOut(self, event):
         event.widget.config(bg="#4682B4")


   def verificaCargo(self, cargo):
      print(cargo[0][0])
      if cargo[0][0] == 'GERENTE':
         self.janela.destroy()
         from Tela_Gerencia import Gerente
         return 
      if cargo[0][0] == 'MECANICO':
         self.janela.destroy()
         from Tela_Mecanico import Mecanico
         return 
      if cargo[0][0] == 'RECEPCIONISTA':
         self.janela.destroy()
         from Tela_Recepção import Recepcao
         return 
      return 

   def verificaLogin(self):
      login = self.LoginUser.get()
      senha = self.SenhaUser.get()
      banco = sqlite3.connect('banco.db')
      cursor = banco.cursor()
      try:
         cursor.execute(f"SELECT senha FROM funcionario WHERE login = '{login}'")
         senhaBD = cursor.fetchall()
         cursor.execute(f"SELECT cargo FROM funcionario WHERE login = '{login}'")
         cargoDB = cursor.fetchall()
         print(senhaBD[0][0])
         # banco.close()
         self.verificaCargo(cargoDB)
         return banco.close()
      except:
         banco.close()
         return messagebox.showinfo('Erro', 'Login ou senha incorretos')


minhaTela = Tela_de_Login()